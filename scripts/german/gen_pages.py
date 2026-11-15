#!/usr/bin/env python3
"""
Generate dedicated CEFR level pages (a1.html, a2.html, b1.html, b2.html, c1.html, c2.html)
"""
import os

levels_info = {
    "A1": {
        "slug": "a1",
        "title": "A1 Deutsche Grammatik (105 Themen)",
        "subtitle": "Grundstufe I (Breakthrough / Anfänger)",
        "desc": "Der vollständige A1-Grundwortschatz & Grammatik-Grundstock: Bestimmte & unbestimmte Artikel, Nominativ & Akkusativ, regelmäßige & unregelmäßige Verben im Präsens, trennbare Verben, Satzstellung (V2 & W-Fragen), Negation mit nicht/kein, Modalverben, Imperativ und erste Präpositionen.",
        "badge_color": "var(--level-a1)",
        "badge_bg": "var(--level-a1-bg)",
        "competencies": [
            "Elementare Sätze verstehen und bilden",
            "Nominativ und Akkusativ sicher unterscheiden",
            "Präsens und trennbare Verben im Alltag anwenden",
            "W-Fragen und Ja/Nein-Entscheidungsfragen formulieren",
            "Modalverben (können, müssen, wollen) gezielt einsetzen"
        ]
    },
    "A2": {
        "slug": "a2",
        "title": "A2 Deutsche Grammatik (105 Themen)",
        "subtitle": "Grundstufe II (Waystage / Grundlegende Kenntnisse)",
        "desc": "Der Dativ-Kasus, die 9 Wechselpräpositionen (Akkusativ vs. Dativ), Lage- und Richtungsverben (legen/liegen, stellen/stehen), Vergangenheitsformen (Perfekt & Präteritum von Hilfs-/Modalverben), erste Adjektivdeklinationen, Nebensätze mit weil, wenn, dass, ob, reflexive Verben sowie Komparativ & Superlativ.",
        "badge_color": "var(--level-a2)",
        "badge_bg": "var(--level-a2-bg)",
        "competencies": [
            "Dativ und Akkusativ bei Wechselpräpositionen präzise wählen",
            "Perfektbildung mit haben und sein bei allen Verbtypen",
            "Nebensätze mit Verbletztstellung flüssig sprechen",
            "Adjektivendungen nach bestimmtem und unbestimmtem Artikel meistern",
            "Reflexivpronomen im Akkusativ und Dativ anwenden"
        ]
    },
    "B1": {
        "slug": "b1",
        "title": "B1 Deutsche Grammatik (105 Themen)",
        "subtitle": "Mittelstufe I (Threshold / Selbstständige Sprachverwendung)",
        "desc": "Der Genitiv und Genitivpräpositionen (wegen, während, trotz), Relativsätze in allen 4 Kasus mit Präpositionen, Infinitivkonstruktionen (um...zu, ohne...zu, anstatt...zu), das Vorgangspassiv in allen Zeitformen, Konjunktiv II der Gegenwart und Vergangenheit, n-Deklination schwacher Maskulina, TeKaMoLo und Verben mit festen Präpositionen.",
        "badge_color": "var(--level-b1)",
        "badge_bg": "var(--level-b1-bg)",
        "competencies": [
            "Relativsätze mit Präpositionen und dessen/deren fehlerfrei bilden",
            "Vorgangspassiv in Präsens, Präteritum und Perfekt formulieren",
            "Irreale Bedingungen und höfliche Bitten mit Konjunktiv II ausdrücken",
            "Infinitivsätze mit zu und zweigliedrige Konnektoren einsetzen",
            "Verben mit festen Präpositionen und Da-Komposita beherrschen"
        ]
    },
    "B2": {
        "slug": "b2",
        "title": "B2 Deutsche Grammatik (105 Themen)",
        "subtitle": "Mittelstufe II (Vantage / Fließende Sprachbeherrschung)",
        "desc": "Zustandspassiv (sein + Partizip II), Passiversatzformen (sich lassen, sein+zu, -bar/-lich), Konjunktiv I in der indirekten Rede, Nomen-Verb-Verbindungen (Funktionsverbgefüge), systematische Transformation zwischen Nominalstil und Verbalstil, subjektive Modalverben (müssen, dürfte, sollen, wollen), erweiterte Partizipialattribute und Satztopologie.",
        "badge_color": "var(--level-b2)",
        "badge_bg": "var(--level-b2-bg)",
        "competencies": [
            "Funktionsverbgefüge (FVG) idiomatisch im Berufsalltag gebrauchen",
            "Indirekte Rede im Konjunktiv I über längere Absätze anwenden",
            "Passiversatzformen präzise im schriftlichen Ausdruck nutzen",
            "Nominalstil und Verbalstil flexibel ineinander transformieren",
            "Subjektive Modalverben zur Nuancierung von Wahrscheinlichkeiten einsetzen"
        ]
    },
    "C1": {
        "slug": "c1",
        "title": "C1 Deutsche Grammatik (105 Themen)",
        "subtitle": "Oberstufe I (Effective Operational Proficiency / Fach- & Hochschulsprache)",
        "desc": "Die deutsche Satztopologie & Felderlehre im Detail, mehrfach erweiterte Partizipialketten, das Gerundiv (zu + Partizip I) in allen Kasus, hypothetische Gefüge ohne wenn (Inversion), synthetischer Konjunktiv II starker Verben, gehobene Genitivverben (entbehren, bezichtigen, bedürfen), Modalpartikeln (wohl kaum, nun einmal), Litotes, Chiasmus und akademische Diskursmarker.",
        "badge_color": "var(--level-c1)",
        "badge_bg": "var(--level-c1-bg)",
        "competencies": [
            "Komplexe Partizipialattribute und Gerundivkonstruktionen auflösen",
            "Satzgefüge mit Vorfeld, Mittelfeld und Nachfeld souverän rhythmisieren",
            "Synthetischen Konjunktiv II und gehobene Genitivverben anwenden",
            "Rhetorische Figuren wie Litotes, Chiasmus und Antithese zielsicher setzen",
            "Akademische und juristische Diskurse mit Textkohärenz verfassen"
        ]
    },
    "C2": {
        "slug": "c2",
        "title": "C2 Deutsche Grammatik (105 Themen)",
        "subtitle": "Oberstufe II (Mastery / Höchste muttersprachliche Meisterschaft)",
        "desc": "Historische Grammatik & archaischer Dativ-e, Doppelformen starker Verben, Zeugma, Hendiadyoin, Aposiopese, Anakoluth, Theodor-W.-Adorno-Parenthesen, Kanzlei- & Notariatsdeutsch, bildungsbürgerliche Redewendungen (Rubikon, Pudels Kern, Eulen nach Athen), feinste semantische Nuancen (versichern vs. beteuern, billigen vs. sanktionieren), Sprachkritik und Hermeneutik.",
        "badge_color": "var(--level-c2)",
        "badge_bg": "var(--level-c2-bg)",
        "competencies": [
            "Virtuoser Wechsel zwischen allen Registern von Kanzleideutsch bis Glosse",
            "Meisterhafte Beherrschung historischer Formen und dichterischer Figuren",
            "Verschachtelte philosophische Parenthesen ohne syntaktischen Bruch führen",
            "Subtilste semantische Unterschiede hochpräzise zur Wirkung bringen",
            "Vollendete sprachliche Eloquenz auf muttersprachlichem Spitzenlevel"
        ]
    }
}

template = """<!DOCTYPE html>
<html lang="de" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Deutsch Hub | Ajay Singh Pundir</title>
  <meta name="description" content="{desc}">

  <!-- Open Graph -->
  <meta property="og:title" content="{title} - 105 Themen">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="article">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🇩🇪</text></svg>">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">

  <!-- CSS -->
  <link rel="stylesheet" href="../assets/css/style.css">
  <link rel="stylesheet" href="css/german.css">
</head>
<body>

  <!-- Navigation -->
  <header class="site-header">
    <div class="container nav-wrapper">
      <a href="../index.html" class="logo" title="Zurück zu Ajays Profil">
        <span class="logo-badge" style="background: linear-gradient(135deg, #f59e0b 0%, #ef4444 100%);">DE</span>
        <span>Deutsch Hub 🇩🇪</span>
      </a>

      <nav class="nav-links" id="nav-links">
        <a href="../blog/index.html" class="nav-link" style="color: var(--accent-primary); font-weight: 700;">← Back to Blog</a>
        <a href="../index.html" class="nav-link">Profile</a>
        <a href="index.html" class="nav-link">Alle Stufen (630)</a>
        <a href="a1.html" class="nav-link{active_a1}">A1</a>
        <a href="a2.html" class="nav-link{active_a2}">A2</a>
        <a href="b1.html" class="nav-link{active_b1}">B1</a>
        <a href="b2.html" class="nav-link{active_b2}">B2</a>
        <a href="c1.html" class="nav-link{active_c1}">C1</a>
        <a href="c2.html" class="nav-link{active_c2}">C2</a>
      </nav>

      <div class="nav-actions">
        <button class="theme-toggle-btn" id="theme-toggle" aria-label="Theme umschalten">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
        </button>
        <button class="mobile-menu-btn" id="mobile-menu-btn" aria-label="Menü öffnen">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        </button>
      </div>
    </div>
  </header>

  <!-- Level Hero Section -->
  <main class="container" style="padding-top: 2rem; padding-bottom: 4rem;">
    <section style="text-align: center; margin-bottom: 2.5rem;">
      <div class="de-flag-ribbon">
        <span>🇩🇪</span> GER-Stufe {level} &bull; 105 Didaktische Module
      </div>
      <h1 class="german-hero-title">
        Deutsche Grammatik <span>Stufe {level}</span>
      </h1>
      <p style="font-size: 1.2rem; font-weight: 600; color: {badge_color}; margin-bottom: 0.75rem;">
        {subtitle}
      </p>
      <p style="font-size: 1.05rem; color: var(--text-secondary); max-width: 800px; margin: 0 auto 2rem; line-height: 1.6;">
        {desc}
      </p>

      <!-- Competencies Pill Box -->
      <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem 1.5rem; max-width: 850px; margin: 0 auto 2rem; text-align: left;">
        <h4 style="font-size: 0.95rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
          <span>🎯</span> Kernkompetenzen nach GER-{level}:
        </h4>
        <ul style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 0.5rem 1.5rem; font-size: 0.875rem; color: var(--text-secondary); padding-left: 1.25rem; margin: 0;">
          {competencies_html}
        </ul>
      </div>

      <!-- Quick Level Switcher -->
      <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 0.5rem;">
        <a href="index.html" class="level-pill">Alle (630)</a>
        <a href="a1.html" class="level-pill a1{active_a1}">A1 (105)</a>
        <a href="a2.html" class="level-pill a2{active_a2}">A2 (105)</a>
        <a href="b1.html" class="level-pill b1{active_b1}">B1 (105)</a>
        <a href="b2.html" class="level-pill b2{active_b2}">B2 (105)</a>
        <a href="c1.html" class="level-pill c1{active_c1}">C1 (105)</a>
        <a href="c2.html" class="level-pill c2{active_c2}">C2 (105)</a>
      </div>
    </section>

    <!-- Progress Dashboard -->
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 16px; padding: 1.5rem 2rem; margin-bottom: 2rem; box-shadow: var(--shadow-sm);">
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 0.75rem;">
        <div style="font-weight: 700; display: flex; align-items: center; gap: 0.5rem;">
          <span>📊</span>
          <span>Lernfortschritt Stufe {level}</span>
        </div>
        <div id="progress-stats-text" style="font-weight: 700; color: {badge_color};">
          0 von 105 gemeistert (0%)
        </div>
      </div>
      <div style="width: 100%; height: 10px; background: var(--bg-input); border-radius: 9999px; overflow: hidden;">
        <div id="progress-bar-fill" style="height: 100%; width: 0%; background: {badge_color}; transition: width 0.3s ease;"></div>
      </div>
    </div>

    <!-- Filter & Control Toolbar -->
    <div class="german-controls">
      <div class="filter-row">
        <div class="search-input-wrapper">
          <span class="search-icon">🔍</span>
          <input type="text" id="grammar-search" placeholder="In Stufe {level} suchen (Regeln, Formeln, Beispiele)..." autocomplete="off">
        </div>
        <select class="category-select" id="category-filter">
          <option value="ALL">Alle Kategorien</option>
        </select>
        <button id="toggle-all-btn" class="copy-btn" style="padding: 0.75rem 1.25rem; font-size: 0.9rem; font-weight: 600;">
          Alle aufklappen 🔽
        </button>
      </div>
    </div>

    <!-- Results Header -->
    <div class="results-info">
      <span id="results-count">Lade {level}-Themen...</span>
      <span style="font-size: 0.8rem; color: var(--text-muted);">Klicke auf eine Karte, um alle Beispiele und die Regelstruktur zu sehen.</span>
    </div>

    <!-- Cards Container -->
    <div id="grammar-cards-container">
      <!-- Loaded dynamically via german.js -->
    </div>

    <!-- Load More Button -->
    <div style="text-align: center; margin-top: 2rem;">
      <button id="load-more-btn" class="btn btn-secondary" style="display: none; padding: 0.85rem 2rem; font-size: 1rem;">
        Weitere Themen laden ⏬
      </button>
    </div>
  </main>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container footer-content" style="text-align: center; padding: 2rem 0; border-top: 1px solid var(--border-color); color: var(--text-muted); font-size: 0.9rem;">
      <p style="margin-bottom: 0.5rem;">
        <strong>Deutsch Hub 🇩🇪 &bull; Stufe {level}</strong> (105 Originalthemen mit didaktischen Beispielen).
      </p>
      <p>
        Zurück zur <a href="index.html" style="color: var(--accent-primary); font-weight: 600;">Gesamtübersicht (630 Themen)</a> &bull;
        Entwickelt von <a href="../index.html" style="color: var(--accent-primary); font-weight: 600;">Ajay Singh Pundir</a>.
      </p>
    </div>
  </footer>

  <!-- Data Scripts (All 6 CEFR Levels) -->
  <script src="data/a1.js"></script>
  <script src="data/a2.js"></script>
  <script src="data/b1.js"></script>
  <script src="data/b2.js"></script>
  <script src="data/c1.js"></script>
  <script src="data/c2.js"></script>

  <!-- Hub Controller -->
  <script>
    window.PAGE_LEVEL = '{level}';
  </script>
  <script src="js/german.js"></script>
  <script src="../assets/js/main.js"></script>
</body>
</html>
"""

def main():
    os.makedirs("deutsche", exist_ok=True)
    for lvl, info in levels_info.items():
        slug = info["slug"]
        filename = f"deutsche/{slug}.html"
        
        comp_html = "\n".join([f"<li>{comp}</li>" for comp in info["competencies"]])
        
        active_flags = {
            f"active_{l.lower()}": " active" if l == lvl else ""
            for l in ["A1", "A2", "B1", "B2", "C1", "C2"]
        }

        page_content = template.format(
            level=lvl,
            title=info["title"],
            subtitle=info["subtitle"],
            desc=info["desc"],
            badge_color=info["badge_color"],
            badge_bg=info["badge_bg"],
            competencies_html=comp_html,
            **active_flags
        )

        with open(filename, "w", encoding="utf-8") as f:
            f.write(page_content)
        print(f"✅ Generated {filename} for CEFR {lvl}")

if __name__ == "__main__":
    main()
