/**
 * Interview Prep & Blog Hub Logic
 * Handles filtering, search, accordion, review progress, and deep-linking.
 */

(function () {
  'use strict';

  // State
  let currentTrack = 'all'; // 'all' | 'dsa' | 'system-design' | 'security' | 'ai'
  let searchQuery = '';
  let selectedCategory = 'all';
  let selectedDifficulty = 'all';
  let selectedStatus = 'all'; // 'all' | 'reviewed' | 'unreviewed'

  // Reviewed questions set from localStorage
  let reviewedSet = new Set();
  try {
    const saved = localStorage.getItem('aj_reviewed_questions');
    if (saved) {
      reviewedSet = new Set(JSON.parse(saved));
    }
  } catch (e) {
    console.error('Failed to load reviewed questions', e);
  }

  function saveReviewed() {
    try {
      localStorage.setItem('aj_reviewed_questions', JSON.stringify(Array.from(reviewedSet)));
    } catch (e) {
      console.error('Failed to save reviewed questions', e);
    }
  }

  // Gather all datasets
  function getAllQuestions() {
    const dsa = (window.INTERVIEW_DATA_DSA || []).map(q => ({ ...q, track: 'dsa', trackName: 'DSA' }));
    const sd = (window.INTERVIEW_DATA_SYSTEM_DESIGN || []).map(q => ({ ...q, track: 'system-design', trackName: 'System Design' }));
    const sec = (window.INTERVIEW_DATA_SECURITY || []).map(q => ({ ...q, track: 'security', trackName: 'Security' }));
    const ai = (window.INTERVIEW_DATA_AI || []).map(q => ({ ...q, track: 'ai', trackName: 'AI & ML' }));

    return {
      dsa,
      'system-design': sd,
      security: sec,
      ai,
      all: [...dsa, ...sd, ...sec, ...ai]
    };
  }

  // DOM Elements
  const container = document.getElementById('questions-container');
  const searchInput = document.getElementById('search-input');
  const clearSearchBtn = document.getElementById('clear-search-btn');
  const categorySelect = document.getElementById('category-filter');
  const diffSelect = document.getElementById('difficulty-filter');
  const statusSelect = document.getElementById('status-filter');
  const resultsCountEl = document.getElementById('results-count');
  const trackPills = document.querySelectorAll('.track-pill');
  const progressBarFill = document.getElementById('progress-bar-fill');
  const progressStats = document.getElementById('progress-stats');

  // Detect fixed track if on dedicated page (e.g. data-track="dsa")
  const pageContainer = document.querySelector('[data-page-track]');
  if (pageContainer) {
    const fixedTrack = pageContainer.getAttribute('data-page-track');
    if (fixedTrack) {
      currentTrack = fixedTrack;
    }
  }

  function init() {
    populateCategoryFilter();
    setupEventListeners();
    render();
    handleInitialHash();
  }

  function populateCategoryFilter() {
    if (!categorySelect) return;
    const allData = getAllQuestions();
    const questions = currentTrack === 'all' ? allData.all : (allData[currentTrack] || []);
    
    const categories = new Set();
    questions.forEach(q => {
      if (q.category) categories.add(q.category);
    });

    const currentVal = categorySelect.value;
    categorySelect.innerHTML = '<option value="all">All Categories</option>';
    Array.from(categories).sort().forEach(cat => {
      const opt = document.createElement('option');
      opt.value = cat;
      opt.textContent = cat;
      if (cat === currentVal) opt.selected = true;
      categorySelect.appendChild(opt);
    });
  }

  function updateProgress() {
    if (!progressBarFill || !progressStats) return;
    const allData = getAllQuestions();
    const targetList = currentTrack === 'all' ? allData.all : (allData[currentTrack] || []);
    const total = targetList.length;
    
    let reviewedCount = 0;
    targetList.forEach(q => {
      if (reviewedSet.has(q.id)) reviewedCount++;
    });

    const percent = total > 0 ? Math.round((reviewedCount / total) * 100) : 0;
    progressBarFill.style.width = `${percent}%`;
    progressStats.textContent = `${reviewedCount} / ${total} (${percent}%) Completed`;
  }

  function filterQuestions() {
    const allData = getAllQuestions();
    let list = currentTrack === 'all' ? allData.all : (allData[currentTrack] || []);

    const query = searchQuery.toLowerCase().trim();

    return list.filter(q => {
      // Track filter
      if (currentTrack !== 'all' && q.track !== currentTrack) return false;

      // Category filter
      if (selectedCategory !== 'all' && q.category !== selectedCategory) return false;

      // Difficulty filter
      if (selectedDifficulty !== 'all' && q.difficulty.toLowerCase() !== selectedDifficulty.toLowerCase()) return false;

      // Status filter
      const isReviewed = reviewedSet.has(q.id);
      if (selectedStatus === 'reviewed' && !isReviewed) return false;
      if (selectedStatus === 'unreviewed' && isReviewed) return false;

      // Search query filter
      if (query) {
        const inTitle = (q.title || '').toLowerCase().includes(query);
        const inQuestion = (q.question || '').toLowerCase().includes(query);
        const inAnswer = (q.answer || '').toLowerCase().includes(query);
        const inTags = (q.tags || []).some(t => t.toLowerCase().includes(query));
        const inCategory = (q.category || '').toLowerCase().includes(query);
        const inId = (q.id || '').toLowerCase().includes(query);

        if (!inTitle && !inQuestion && !inAnswer && !inTags && !inCategory && !inId) {
          return false;
        }
      }

      return true;
    });
  }

  function render() {
    updateProgress();
    if (!container) return;

    const filtered = filterQuestions();

    if (resultsCountEl) {
      resultsCountEl.textContent = `Showing ${filtered.length} questions`;
    }

    if (filtered.length === 0) {
      container.innerHTML = `
        <div class="empty-state">
          <div class="empty-state-icon">🔍</div>
          <div class="empty-state-title">No matching questions found</div>
          <p>Try adjusting your search query, difficulty, or category filter.</p>
        </div>
      `;
      return;
    }

    container.innerHTML = filtered.map(q => createQuestionCardHTML(q)).join('');
  }

  function createQuestionCardHTML(q) {
    const isReviewed = reviewedSet.has(q.id);
    const diffClass = (q.difficulty || 'medium').toLowerCase();
    const hasJava = (q.answer && q.answer.includes('```java'));
    const javaBadgeHTML = hasJava ? `<span class="badge-java">☕ Java Solution</span>` : '';

    const keyPointsHTML = (q.keyPoints && q.keyPoints.length) ? `
      <div class="key-points-box">
        <div class="key-points-title">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
          Key Interview Takeaways
        </div>
        <div class="key-points-list">
          ${q.keyPoints.map(kp => `
            <div class="key-point-item">
              <span class="key-point-bullet">✓</span>
              <span>${escapeHTML(kp)}</span>
            </div>
          `).join('')}
        </div>
      </div>
    ` : '';

    const tagsHTML = (q.tags && q.tags.length) ? `
      <div class="tags-list">
        ${q.tags.map(t => `<span class="tag-item">#${escapeHTML(t)}</span>`).join('')}
      </div>
    ` : '';

    return `
      <article class="question-card ${isReviewed ? 'reviewed' : ''}" id="${q.id}" data-id="${q.id}">
        <div class="question-card-header" onclick="window.toggleQuestionCard('${q.id}')">
          <div class="card-top-row">
            <div class="card-meta-left">
              <span class="question-id-badge">#${q.id}</span>
              ${q.trackName ? `<span class="category-badge">${escapeHTML(q.trackName)}</span>` : ''}
              <span class="category-badge">${escapeHTML(q.category || '')}</span>
              <span class="diff-badge ${diffClass}">${escapeHTML(q.difficulty || 'Medium')}</span>
              ${javaBadgeHTML}
            </div>
            <div class="card-actions-right" onclick="event.stopPropagation()">
              <button class="review-toggle-btn ${isReviewed ? 'checked' : ''}" 
                      onclick="window.toggleReviewStatus('${q.id}', event)"
                      title="${isReviewed ? 'Mark as Unreviewed' : 'Mark as Reviewed'}">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>${isReviewed ? 'Reviewed' : 'Review'}</span>
              </button>
              <button class="view-solution-btn" onclick="window.toggleQuestionCard('${q.id}'); event.stopPropagation();" title="Click to view solution and code">
                <span class="btn-text-closed">View Solution</span>
                <span class="btn-text-open">Hide Solution</span>
                <svg class="expand-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </button>
            </div>
          </div>
          <h3 class="question-title">${escapeHTML(q.title)}</h3>
          <p class="question-prompt">${escapeHTML(q.question)}</p>
        </div>

        <div class="question-body">
          <div class="answer-section">
            <div class="answer-label">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
              Technical Explanation & Solution
            </div>
            <div class="answer-content">${formatAnswer(q.answer)}</div>
            ${keyPointsHTML}
          </div>

          <div class="card-footer">
            ${tagsHTML}
            <button class="copy-link-btn" onclick="window.copyQuestionLink('${q.id}', event)">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
              Copy Link
            </button>
          </div>
        </div>
      </article>
    `;
  }

  function formatAnswer(text) {
    if (!text) return '';
    // Split by fenced code blocks ```lang ... ```
    const parts = text.split(/(```[\s\S]*?```)/g);
    return parts.map(part => {
      if (part.startsWith('```') && part.endsWith('```')) {
        const trimmed = part.slice(3, -3).trim();
        const firstLineEnd = trimmed.indexOf('\n');
        let lang = 'java';
        let code = trimmed;
        if (firstLineEnd !== -1) {
          const firstWord = trimmed.slice(0, firstLineEnd).trim();
          if (/^[a-zA-Z0-9_-]+$/.test(firstWord)) {
            lang = firstWord;
            code = trimmed.slice(firstLineEnd + 1);
          }
        }
        return `<pre class="code-block"><code class="language-${lang}">${escapeHTML(code)}</code></pre>`;
      } else {
        // Plain text: escape HTML, format inline backticks, convert newlines
        let formatted = escapeHTML(part);
        formatted = formatted.replace(/`([^`]+)`/g, '<code class="inline-code">$1</code>');
        return formatted.replace(/\n/g, '<br>');
      }
    }).join('');
  }

  function escapeHTML(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // Global helper functions exposed for inline onclick handlers
  window.toggleQuestionCard = function (id) {
    const card = document.getElementById(id);
    if (!card) return;
    card.classList.toggle('open');
  };

  let allSolutionsExpanded = false;
  window.toggleAllSolutions = function () {
    const cards = document.querySelectorAll('.question-card');
    allSolutionsExpanded = !allSolutionsExpanded;
    cards.forEach(c => {
      if (allSolutionsExpanded) {
        c.classList.add('open');
      } else {
        c.classList.remove('open');
      }
    });
    const btn = document.getElementById('toggle-all-btn');
    if (btn) {
      const label = btn.querySelector('span');
      if (label) {
        label.textContent = allSolutionsExpanded ? 'Collapse All Solutions' : 'Expand All Solutions';
      }
    }
  };

  window.toggleReviewStatus = function (id, event) {
    if (event) event.stopPropagation();
    if (reviewedSet.has(id)) {
      reviewedSet.delete(id);
    } else {
      reviewedSet.add(id);
    }
    saveReviewed();

    const card = document.getElementById(id);
    if (card) {
      const isRev = reviewedSet.has(id);
      card.classList.toggle('reviewed', isRev);
      const btn = card.querySelector('.review-toggle-btn');
      if (btn) {
        btn.classList.toggle('checked', isRev);
        btn.querySelector('span').textContent = isRev ? 'Reviewed' : 'Review';
      }
    }
    updateProgress();
  };

  window.copyQuestionLink = function (id, event) {
    if (event) event.stopPropagation();
    const url = new URL(window.location.href);
    url.hash = id;
    navigator.clipboard.writeText(url.toString()).then(() => {
      const btn = event.currentTarget;
      const originalHTML = btn.innerHTML;
      btn.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Copied!`;
      setTimeout(() => {
        btn.innerHTML = originalHTML;
      }, 2000);
    });
  };

  function setupEventListeners() {
    // Search input
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value;
        if (clearSearchBtn) {
          clearSearchBtn.style.display = searchQuery ? 'block' : 'none';
        }
        render();
      });
    }

    if (clearSearchBtn) {
      clearSearchBtn.addEventListener('click', () => {
        searchQuery = '';
        if (searchInput) searchInput.value = '';
        clearSearchBtn.style.display = 'none';
        render();
      });
    }

    // Keyboard shortcut '/' to focus search
    document.addEventListener('keydown', (e) => {
      if (e.key === '/' && document.activeElement !== searchInput) {
        e.preventDefault();
        if (searchInput) searchInput.focus();
      }
    });

    // Track pills
    trackPills.forEach(pill => {
      pill.addEventListener('click', () => {
        trackPills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        currentTrack = pill.getAttribute('data-track') || 'all';
        populateCategoryFilter();
        render();
      });
    });

    // Category filter
    if (categorySelect) {
      categorySelect.addEventListener('change', (e) => {
        selectedCategory = e.target.value;
        render();
      });
    }

    // Difficulty filter
    if (diffSelect) {
      diffSelect.addEventListener('change', (e) => {
        selectedDifficulty = e.target.value;
        render();
      });
    }

    // Status filter
    if (statusSelect) {
      statusSelect.addEventListener('change', (e) => {
        selectedStatus = e.target.value;
        render();
      });
    }
  }

  function handleInitialHash() {
    const hash = window.location.hash.replace('#', '');
    if (!hash) return;

    // Check if hash matches an ID
    setTimeout(() => {
      const card = document.getElementById(hash);
      if (card) {
        card.classList.add('open');
        card.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }, 200);
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
