/**
 * Deutsche Grammatik Hub - Interactive Logic
 * Controls search, filtering, progress tracking, and accordion UI
 */

(function () {
  'use strict';

  // Gather all available datasets
  let allTopics = [];
  const levels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];

  levels.forEach(lvl => {
    const key = `GERMAN_DATA_${lvl}`;
    if (window[key] && Array.isArray(window[key])) {
      allTopics = allTopics.concat(window[key]);
    }
  });

  // State
  let currentLevel = window.PAGE_LEVEL || 'ALL';
  let searchQuery = '';
  let selectedCategory = 'ALL';
  let visibleCount = 40; // initial batch for performance
  const BATCH_SIZE = 40;

  // Local Storage for Mastered Topics
  const STORAGE_KEY = 'de_mastered_topics';
  let masteredTopics = new Set();
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
      masteredTopics = new Set(JSON.parse(saved));
    }
  } catch (e) {
    console.error('Failed to load mastered topics', e);
  }

  function saveMastered() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(Array.from(masteredTopics)));
    } catch (e) {
      console.error('Failed to save mastered topics', e);
    }
    updateProgressStats();
  }

  // DOM Elements
  const container = document.getElementById('grammar-cards-container');
  const searchInput = document.getElementById('grammar-search');
  const categorySelect = document.getElementById('category-filter');
  const levelPillsContainer = document.getElementById('level-pills');
  const progressText = document.getElementById('progress-stats-text');
  const progressBarFill = document.getElementById('progress-bar-fill');
  const resultsCountEl = document.getElementById('results-count');
  const loadMoreBtn = document.getElementById('load-more-btn');
  const toggleAllBtn = document.getElementById('toggle-all-btn');

  // Initialize
  function init() {
    buildLevelPills();
    updateCategoryDropdown();
    render();
    updateProgressStats();
    attachEvents();
  }

  function getFilteredTopics() {
    return allTopics.filter(topic => {
      // Level filter
      if (currentLevel !== 'ALL' && topic.level !== currentLevel) {
        return false;
      }
      // Category filter
      if (selectedCategory !== 'ALL' && topic.category !== selectedCategory) {
        return false;
      }
      // Search filter
      if (searchQuery) {
        const q = searchQuery.toLowerCase();
        const inTitle = (topic.title || '').toLowerCase().includes(q);
        const inCategory = (topic.category || '').toLowerCase().includes(q);
        const inRule = (topic.rule || topic.explanation || '').toLowerCase().includes(q);
        const inFormula = (topic.formula || topic.ruleBox || '').toLowerCase().includes(q);
        const inSyntax = (topic.syntax || '').toLowerCase().includes(q);
        const inConjugation = (topic.conjugation || '').toLowerCase().includes(q);
        const inDeclension = (topic.declension || '').toLowerCase().includes(q);
        const inTakeaway = (topic.takeaway || (topic.keyPoints && topic.keyPoints.join(' ')) || '').toLowerCase().includes(q);
        const inExamples = topic.examples && topic.examples.some(ex => 
          (ex.de || '').toLowerCase().includes(q) || (ex.en || '').toLowerCase().includes(q) || (ex.breakdown && ex.breakdown.toLowerCase().includes(q))
        );
        return inTitle || inCategory || inRule || inFormula || inSyntax || inConjugation || inDeclension || inTakeaway || inExamples;
      }
      return true;
    });
  }

  function buildLevelPills() {
    if (!levelPillsContainer) return;
    
    // Calculate counts
    const counts = { ALL: allTopics.length };
    levels.forEach(lvl => {
      counts[lvl] = allTopics.filter(t => t.level === lvl).length;
    });

    const pillsHtml = [
      `<button class="level-pill ${currentLevel === 'ALL' ? 'active' : ''}" data-level="ALL">
        Alle Stufen <span>(${counts.ALL})</span>
      </button>`
    ];

    levels.forEach(lvl => {
      const cls = lvl.toLowerCase();
      pillsHtml.push(`
        <button class="level-pill ${cls} ${currentLevel === lvl ? 'active ' + cls : ''}" data-level="${lvl}">
          ${lvl} <span>(${counts[lvl] || 0})</span>
        </button>
      `);
    });

    levelPillsContainer.innerHTML = pillsHtml.join('');

    levelPillsContainer.querySelectorAll('.level-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        currentLevel = btn.dataset.level;
        visibleCount = currentLevel === 'ALL' ? BATCH_SIZE : 150; // Show all topics when level is selected
        selectedCategory = 'ALL';
        buildLevelPills();
        updateCategoryDropdown();
        render();
        updateProgressStats();
      });
    });
  }

  function updateCategoryDropdown() {
    if (!categorySelect) return;
    
    // Get unique categories for current level
    const relevant = currentLevel === 'ALL' 
      ? allTopics 
      : allTopics.filter(t => t.level === currentLevel);
    
    const categories = Array.from(new Set(relevant.map(t => t.category))).sort();

    let html = `<option value="ALL">Alle Kategorien (${categories.length})</option>`;
    categories.forEach(cat => {
      const count = relevant.filter(t => t.category === cat).length;
      html += `<option value="${escapeHtml(cat)}"${selectedCategory === cat ? ' selected' : ''}>${escapeHtml(cat)} (${count})</option>`;
    });

    categorySelect.innerHTML = html;
  }

  function render() {
    if (!container) return;

    const filtered = getFilteredTopics();
    const toShow = filtered.slice(0, visibleCount);

    if (resultsCountEl) {
      resultsCountEl.textContent = `Zeige ${toShow.length} von ${filtered.length} Themen`;
    }

    if (loadMoreBtn) {
      loadMoreBtn.style.display = filtered.length > visibleCount ? 'block' : 'none';
      if (filtered.length > visibleCount) {
        loadMoreBtn.textContent = `Weitere ${Math.min(BATCH_SIZE, filtered.length - visibleCount)} Themen laden`;
      }
    }

    if (filtered.length === 0) {
      container.innerHTML = `
        <div class="empty-results">
          <div style="font-size: 3rem;">🔍</div>
          <h3>Keine Grammatikthemen gefunden</h3>
          <p>Versuchen Sie einen anderen Suchbegriff oder wählen Sie eine andere Stufe.</p>
        </div>
      `;
      return;
    }

    const html = toShow.map(topic => renderCard(topic)).join('');
    container.innerHTML = html;

    // Attach card event listeners
    attachCardEvents();
  }

  function formatSyntaxTokens(str) {
    if (!str) return '';
    const matches = str.match(/\[[^\]]+\]|\+|\/|\|/g);
    if (!matches) {
      return `<div class="declension-table-badge">${escapeHtml(str)}</div>`;
    }

    const html = matches.map(token => {
      const trimmed = token.trim();
      if (trimmed === '+') {
        return '<span class="syntax-plus">+</span>';
      }
      if (trimmed === '/' || trimmed === '|') {
        return `<span class="syntax-plus" style="margin: 0 0.25rem;">${escapeHtml(trimmed)}</span>`;
      }
      const inner = trimmed.startsWith('[') && trimmed.endsWith(']') 
        ? trimmed.slice(1, -1) 
        : trimmed;

      let cls = 'token-gen';
      if (/^S\b|Subjekt/i.test(inner)) {
        cls = 'token-s';
      } else if (/^V\b|Verb|Prädikat|Pos 2|finit/i.test(inner)) {
        cls = 'token-v';
      } else if (/^O\b|Objekt|Akkusativ|Dativ/i.test(inner)) {
        cls = 'token-o';
      } else if (/Ende|Infinitiv|Partizip|Präfix/i.test(inner)) {
        cls = 'token-end';
      } else if (/Konnektor|Konjunktion|W-Wort|W-Frage/i.test(inner)) {
        cls = 'token-conn';
      }
      return `<span class="syntax-token ${cls}">${escapeHtml(inner)}</span>`;
    }).join(' ');

    return `<div class="syntax-formula-wrap">${html}</div>`;
  }

  function formatConjugationGrid(str) {
    if (!str) return '';
    if (!str.includes('|')) {
      return `<div class="declension-table-badge">${escapeHtml(str)}</div>`;
    }

    const cells = str.split('|').map(item => item.trim()).filter(Boolean);
    const html = cells.map(cell => {
      let person = '';
      let val = cell;
      if (cell.includes(':')) {
        const parts = cell.split(':');
        person = parts[0].trim();
        val = parts.slice(1).join(':').trim();
      } else {
        const words = cell.split(' ');
        if (words.length > 1) {
          person = words[0];
          val = words.slice(1).join(' ');
        }
      }
      return `
        <div class="conj-cell">
          <span class="conj-person">${escapeHtml(person)}</span>
          <span class="conj-val">${escapeHtml(val)}</span>
        </div>
      `;
    }).join('');

    return html;
  }

  function renderCard(topic) {
    const isMastered = masteredTopics.has(topic.id);
    const lvlCls = topic.level.toLowerCase();

    const ruleText = topic.rule || topic.explanation || '';
    const formulaText = topic.formula || topic.ruleBox || '';
    const syntaxText = topic.syntax || '';
    const syntaxNote = topic.syntaxNote || '';
    const conjugationText = topic.conjugation || '';
    const conjugationPattern = topic.conjugationPattern || '';
    const declensionText = topic.declension || '';
    const declensionNote = topic.declensionNote || '';
    const takeawayText = topic.takeaway || (topic.keyPoints && topic.keyPoints.join(' • ')) || '';

    const examplesHtml = (topic.examples || []).map((ex, idx) => `
      <div class="example-item">
        <div class="example-de-row">
          <div class="example-de">${escapeHtml(ex.de)}</div>
          <button class="copy-btn" data-copy="${escapeHtml(ex.de)}" title="Satz kopieren">
            Kopieren 📋
          </button>
        </div>
        <div class="example-en">${escapeHtml(ex.en)}</div>
        ${ex.breakdown ? `<div class="example-breakdown">🔍 ${escapeHtml(ex.breakdown)}</div>` : ''}
      </div>
    `).join('');

    return `
      <div class="grammar-card ${isMastered ? 'is-mastered' : ''}" id="card-${topic.id}">
        <div class="grammar-card-header" data-card-id="${topic.id}">
          <div class="header-left">
            <div class="meta-row">
              <span class="level-badge ${lvlCls}">${topic.level}</span>
              <span class="category-tag">${escapeHtml(topic.category)}</span>
              <span style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono, monospace);">${topic.id}</span>
            </div>
            <h3 class="topic-title">${escapeHtml(topic.title)}</h3>
          </div>
          <div class="header-right">
            <label class="mastered-checkbox-wrap" onclick="event.stopPropagation()">
              <input type="checkbox" class="mastered-checkbox" data-id="${topic.id}" ${isMastered ? 'checked' : ''}>
              <span>Gelernt</span>
            </label>
            <span class="toggle-icon">▼</span>
          </div>
        </div>
        <div class="grammar-card-body">
          <!-- 1. Grammatik-Regel & Erklärung -->
          <div class="rule-box">
            <div class="box-header">📋 Grammatik-Regel & Erklärung</div>
            <div class="rule-content">${escapeHtml(ruleText)}</div>
          </div>

          <!-- 2. Satzbau & Wortstellung (Syntax) -->
          ${syntaxText ? `
            <div class="syntax-rule-box">
              <div class="box-header">📐 Satzbau & Wortstellung (Syntax)</div>
              ${formatSyntaxTokens(syntaxText)}
              ${syntaxNote ? `<div class="syntax-note">💡 ${escapeHtml(syntaxNote)}</div>` : ''}
            </div>
          ` : ''}

          <!-- 3. Verb-Konjugation & Formen -->
          ${conjugationText ? `
            <div class="conjugation-rule-box">
              <div class="box-header">🔤 Verb-Konjugation & Formen</div>
              <div class="conjugation-grid">
                ${formatConjugationGrid(conjugationText)}
              </div>
              ${conjugationPattern ? `<div class="conjugation-pattern">💡 ${escapeHtml(conjugationPattern)}</div>` : ''}
            </div>
          ` : ''}

          <!-- 4. Kasus & Deklination -->
          ${declensionText ? `
            <div class="declension-rule-box">
              <div class="box-header">📊 Kasus & Deklination</div>
              <div class="declension-table-badge">${escapeHtml(declensionText)}</div>
              ${declensionNote ? `<div class="declension-note">💡 ${escapeHtml(declensionNote)}</div>` : ''}
            </div>
          ` : ''}

          <!-- 5. Formel / Leitformel -->
          ${formulaText && formulaText !== syntaxText ? `
            <div class="formula-box">
              <span class="formula-tag">📐 Leitformel:</span>
              <span class="formula-body">${escapeHtml(formulaText)}</span>
            </div>
          ` : ''}

          <!-- 6. Praktische Beispielsätze -->
          <div class="examples-title">💬 Praktische Beispielsätze & Analyse</div>
          <div class="example-list">
            ${examplesHtml}
          </div>

          <!-- 7. Merke & Lerntipp -->
          ${takeawayText ? `
            <div class="takeaway-box">
              <div><strong>💡 Merke & Lerntipp:</strong> ${escapeHtml(takeawayText)}</div>
            </div>
          ` : ''}
        </div>
      </div>
    `;
  }

  function attachCardEvents() {
    // Accordion headers
    container.querySelectorAll('.grammar-card-header').forEach(header => {
      header.addEventListener('click', () => {
        const card = header.closest('.grammar-card');
        card.classList.toggle('open');
      });
    });

    // Mastered Checkboxes
    container.querySelectorAll('.mastered-checkbox').forEach(cb => {
      cb.addEventListener('change', (e) => {
        const id = cb.dataset.id;
        const card = document.getElementById(`card-${id}`);
        if (cb.checked) {
          masteredTopics.add(id);
          if (card) card.classList.add('is-mastered');
        } else {
          masteredTopics.delete(id);
          if (card) card.classList.remove('is-mastered');
        }
        saveMastered();
      });
    });

    // Copy Buttons
    container.querySelectorAll('.copy-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const text = btn.dataset.copy;
        navigator.clipboard.writeText(text).then(() => {
          const original = btn.textContent;
          btn.textContent = 'Kopiert! ✓';
          btn.style.background = '#10b981';
          btn.style.color = '#fff';
          setTimeout(() => {
            btn.textContent = original;
            btn.style.background = '';
            btn.style.color = '';
          }, 1500);
        }).catch(err => {
          console.error('Copy failed', err);
        });
      });
    });
  }

  function updateProgressStats() {
    if (!progressText || !progressBarFill) return;

    const relevant = currentLevel === 'ALL'
      ? allTopics
      : allTopics.filter(t => t.level === currentLevel);
    
    const total = relevant.length;
    if (total === 0) return;

    let mastered = 0;
    relevant.forEach(t => {
      if (masteredTopics.has(t.id)) mastered++;
    });

    const pct = Math.round((mastered / total) * 100);
    progressText.textContent = `${mastered} von ${total} gemeistert (${pct}%)`;
    progressBarFill.style.width = `${pct}%`;
  }

  function attachEvents() {
    // Search input
    if (searchInput) {
      let debounceTimer;
      searchInput.addEventListener('input', (e) => {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => {
          searchQuery = e.target.value.trim();
          visibleCount = searchQuery ? 150 : BATCH_SIZE;
          render();
        }, 200);
      });
    }

    // Category filter
    if (categorySelect) {
      categorySelect.addEventListener('change', (e) => {
        selectedCategory = e.target.value;
        visibleCount = 150;
        render();
      });
    }

    // Load more
    if (loadMoreBtn) {
      loadMoreBtn.addEventListener('click', () => {
        visibleCount += BATCH_SIZE;
        render();
      });
    }

    // Toggle all
    if (toggleAllBtn) {
      let allOpen = false;
      toggleAllBtn.addEventListener('click', () => {
        allOpen = !allOpen;
        container.querySelectorAll('.grammar-card').forEach(card => {
          if (allOpen) {
            card.classList.add('open');
          } else {
            card.classList.remove('open');
          }
        });
        toggleAllBtn.textContent = allOpen ? 'Alle zuklappen 🔼' : 'Alle aufklappen 🔽';
      });
    }
  }

  function escapeHtml(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
