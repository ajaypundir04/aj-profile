#!/usr/bin/env python3
"""
Enrich German Grammar Datasets (A1-C2) with Explicit Pedagogical Rules:
- Harmonize fields across all 6 levels:
  id, level, category, title, rule, syntax, conjugation, declension, formula, examples, takeaway, tags
- Add explicit Satzbau & Syntax formulas:
  e.g. S + V + O (Subjekt + Verb Position 2 + Objekt), Inversion, W-Frage, Ja/Nein,
       Satzklammer (Modal/Perfekt/Trennbare Verben), Nebensatz (Verbletztstellung),
       TeKaMoLo, Dativ vor Akkusativ, etc.
- Add explicit Verb Conjugation patterns & tables:
  e.g. ich -e | du -st | er/sie/es -t | wir -en | ihr -t | sie/Sie -en,
       vowel changes (e->i, e->ie, a->ä), irregular auxiliary verbs, modal tables,
       Präteritum, Perfekt, Konjunktiv II, Passiv.
- Add explicit Case & Declension tables:
  e.g. Nominativ, Akkusativ, Dativ, Genitiv articles and pronoun charts.
- Enrich examples with clear [S], [V], [O], [Case] breakdowns.
"""
import json
import re
import os

def enrich_level(lvl):
    filepath = f"deutsche/data/{lvl.lower()}.js"
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    m = re.search(r'=\s*(\[.*\]);', content, re.DOTALL)
    if not m:
        raise ValueError(f"Could not parse JSON array in {filepath}")
    
    topics = json.loads(m.group(1))
    print(f"Loaded {len(topics)} topics from {filepath}")

    enriched = []
    for t in topics:
        item = enrich_topic(lvl.upper(), t)
        enriched.append(item)

    # Write back
    var_name = f"GERMAN_DATA_{lvl.upper()}"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"// German Grammar Topics - Level {lvl.upper()} - Exactly {len(enriched)} Topics\n")
        f.write(f"window.{var_name} = " + json.dumps(enriched, indent=2, ensure_ascii=False) + ";\n")
    print(f"✅ Successfully enriched and wrote {filepath} ({len(enriched)} topics)")

def enrich_topic(lvl, t):
    item = dict(t)

    # 1. Harmonize rule / explanation
    rule_text = t.get("rule") or t.get("explanation") or ""
    item["rule"] = rule_text

    # 2. Harmonize formula / ruleBox
    formula_text = t.get("formula") or t.get("ruleBox") or ""
    item["formula"] = formula_text

    # 3. Harmonize takeaway / keyPoints
    if "takeaway" in t and t["takeaway"]:
        takeaway_text = t["takeaway"]
    elif "keyPoints" in t and isinstance(t["keyPoints"], list):
        takeaway_text = " • ".join(t["keyPoints"])
    else:
        takeaway_text = ""
    item["takeaway"] = takeaway_text

    # 4. Determine explicit Satzbau (Syntax), Verb Conjugation, and Declension
    cat = t.get("category", "")
    title = t.get("title", "")
    tid = t.get("id", "")

    syntax = ""
    conjugation = ""
    declension = ""

    # ---- SYNTAX RULES (Satzbau) ----
    if "Standard Word Order" in title or "V2 Rule" in title:
        syntax = "[S: Subjekt] + [V: Finites Verb (Pos 2)] + [O: Objekt / Mittelfeld]"
        item["syntaxNote"] = "In Aussagesätzen steht das konjugierte Verb IMMER an Position 2. Steht eine Zeit- oder Ortsangabe an Pos 1, folgt das Verb an Pos 2 und das Subjekt an Pos 3 (Inversion)."
    elif "Yes/No Questions" in title or "Ja/Nein" in title:
        syntax = "[V: Finites Verb (Pos 1)] + [S: Subjekt (Pos 2)] + [O: Objekt / Angaben]?"
        item["syntaxNote"] = "Verberststellung (V1): Das Verb rückt ganz nach vorn an Position 1."
    elif "W-Words" in title or "W-Fragen" in title or "Interrogative" in title:
        syntax = "[W-Wort (Pos 1)] + [V: Finites Verb (Pos 2)] + [S: Subjekt (Pos 3)] + [O: Objekt]?"
        item["syntaxNote"] = "Das Fragewort (Wer, Was, Wo, Wann, Warum, Wie) belegt Position 1; das Verb bleibt strikt an Position 2."
    elif "Sentence Bracket with Modal" in title or ("Modal" in cat and "Bracket" in title):
        syntax = "[S: Subjekt] + [Modalverb (Pos 2)] + [Mittelfeld: Angaben/Objekte] + [V: Infinitiv (Satzende)]"
        item["syntaxNote"] = "Satzklammer: Das finite Modalverb steht an Position 2, das Vollverb als Infinitiv am Satzende."
    elif "Modal" in cat:
        syntax = "[S: Subjekt] + [Modalverb (Pos 2)] + [Mittelfeld] + [Infinitiv (Satzende)]"
    elif "Separable Verbs" in cat or "Trennbare" in title:
        if "Modal" in title:
            syntax = "[S: Subjekt] + [Modalverb (Pos 2)] + [Mittelfeld] + [Trennbares Verb komplett (Satzende)]"
            item["syntaxNote"] = "Mit Modalverb trennt sich das Verb NICHT! Es steht als einheitlicher Infinitiv am Satzende."
        else:
            syntax = "[S: Subjekt] + [Verbstamm (Pos 2)] + [Mittelfeld] + [Präfix (Satzende)]"
            item["syntaxNote"] = "Das trennbare Präfix wandert an die allerletzte Stelle des Hauptsatzes."
    elif "Inseparable" in title:
        syntax = "[S: Subjekt] + [Untrennbares Verb komplett (Pos 2)] + [Mittelfeld / Objekt]"
        item["syntaxNote"] = "Präfixe be-, emp-, ent-, er-, ge-, miss-, ver-, zer- trennen sich NIE."
    elif "Subordinate Clauses" in cat or any(k in title.lower() for k in ["weil", "dass", "wenn", "ob", "obwohl", "während", "nachdem", "bevor", "indem", "sodass"]):
        syntax = "[Hauptsatz: S + V (Pos 2)], + [Konnektor] + [S: Subjekt] + [Mittelfeld] + [V: Finites Verb (Satzende)]"
        item["syntaxNote"] = "Verbletztstellung: Im Nebensatz wandert das konjugierte Verb an die allerletzte Position!"
    elif "Infinitiv" in cat or "Infinitive" in cat or "um ... zu" in title or "zu + Infinitiv" in title:
        syntax = "[Hauptsatz: S + V (Pos 2)], + [um / ohne / anstatt]? + [Mittelfeld] + [zu + Infinitiv (Satzende)]"
        item["syntaxNote"] = "Bei trennbaren Verben schiebt sich 'zu' zwischen Präfix und Stamm: einkaufen -> einzukaufen."
    elif "Relative Clauses" in cat or "Relativsätze" in title or "Relativ" in cat:
        syntax = "[Hauptsatz], + [Relativpronomen: der/die/das/den/dem/dessen] + [Mittelfeld] + [V: Finites Verb (Satzende)]"
        item["syntaxNote"] = "Relativsätze sind Nebensätze: Das konjugierte Verb steht immer am Satzende."
    elif "Passiv" in cat or "Passive" in cat:
        if "Perfekt" in title:
            syntax = "[S: Subjekt (Patient)] + [sein (Pos 2)] + [von + Dativ] + [Partizip II] + [worden (Satzende)]"
        elif "Präteritum" in title or "wurde" in title:
            syntax = "[S: Subjekt (Patient)] + [wurde / wurden (Pos 2)] + [von + Dativ] + [Partizip II (Satzende)]"
        elif "Modal" in title:
            syntax = "[S: Subjekt] + [Modalverb (Pos 2)] + [von + Dativ] + [Partizip II] + [werden (Satzende)]"
        elif "Zustandspassiv" in title or "sein + Partizip" in title:
            syntax = "[S: Subjekt] + [sein (konjugiert Pos 2)] + [Partizip II (Zustand am Satzende)]"
        else:
            syntax = "[S: Subjekt (Patient)] + [werden (konjugiert Pos 2)] + [von + Dativ (Agens)] + [Partizip II (Satzende)]"
        item["syntaxNote"] = "Das Akkusativobjekt des Aktivsatzes wird zum Subjekt des Passivsatzes. Der Urheber entfällt oder steht mit 'von + Dativ'."
    elif "Perfekt" in cat:
        syntax = "[S: Subjekt] + [Hilfsverb haben / sein (Pos 2)] + [Mittelfeld] + [Partizip II (Satzende)]"
        item["syntaxNote"] = "Satzklammer im Perfekt: Das finite Hilfsverb belegt Position 2, das Partizip II schließt den Satz ab."
    elif "Futur" in cat or "werden + Infinitiv" in title:
        syntax = "[S: Subjekt] + [werden (konjugiert Pos 2)] + [Mittelfeld] + [Vollverb Infinitiv (Satzende)]"
    elif "Konjunktiv II" in cat or "Konjunktiv" in cat:
        if "Vergangenheit" in title:
            syntax = "[S: Subjekt] + [wäre / hätte (Pos 2)] + [Mittelfeld] + [Partizip II (Satzende)]"
        elif "würde" in title:
            syntax = "[S: Subjekt] + [würde (konjugiert Pos 2)] + [Mittelfeld] + [Infinitiv (Satzende)]"
        else:
            syntax = "[S: Subjekt] + [Konjunktiv-II-Form (Pos 2)] + [Mittelfeld / Ergänzung]"
    elif "Double Object" in title or "Dative Noun before Accusative" in title:
        syntax = "[S: Subjekt] + [V: Finites Verb (Pos 2)] + [Dativ-Nomen (Person)] + [Akkusativ-Nomen (Sache)]"
        item["syntaxNote"] = "Zwei Nomen im Satz: Das Dativobjekt (Person/Empfänger) steht VOR dem Akkusativobjekt (Sache)."
    elif "Pronoun Order" in title:
        syntax = "[S: Subjekt] + [V: Finites Verb (Pos 2)] + [Akkusativ-Pronomen (es/ihn/sie)] + [Dativ-Pronomen (mir/dir/ihm)]"
        item["syntaxNote"] = "Zwei Pronomen im Satz: Das Akkusativpronomen steht VOR dem Dativpronomen! (z.B. Er gibt es mir)."
    elif "TeKaMoLo" in title or "Temporal, Kausal" in title:
        syntax = "[S: Subjekt] + [V finit (Pos 2)] + [Temporal (Wann?)] + [Kausal (Warum?)] + [Modal (Wie?)] + [Lokal (Wo/Wohin?)] + [Objekt]"
        item["syntaxNote"] = "Reihenfolge der Angaben im Mittelfeld: Temporal vor Kausal vor Modal vor Lokal (Te-Ka-Mo-Lo)."
    elif "Imperative for 'du'" in title:
        syntax = "[Verbstamm ohne -en (Pos 1)] + [Objekt / Höflichkeitswort 'bitte']! (kein Subjekt 'du')"
        item["syntaxNote"] = "Kommen -> Komm! / Machen -> Mach! (Ausnahme: Verben mit e->i behalten Vokalwechsel: Lies! Gib! Fahr!)"
    elif "Imperative for 'ihr'" in title:
        syntax = "[Verbstamm + -t (Pos 1)] + [Objekt / bitte]! (kein Subjekt 'ihr')"
        item["syntaxNote"] = "Ihr kommt -> Kommt! / Ihr macht -> Macht!"
    elif "Imperative for 'Sie'" in title:
        syntax = "[Finites Verb (Pos 1)] + [Sie (Pos 2)] + [Objekt / bitte]!"
        item["syntaxNote"] = "Inversion: Kommen Sie bitte! / Steigen Sie ein!"
    elif "Inversion" in title or "Adverbs" in cat and "Temporal" in title:
        syntax = "[Angabe Zeit / Ort (Pos 1)] + [V: Finites Verb (Pos 2)] + [S: Subjekt (Pos 3)] + [Objekt / Rest]"
        item["syntaxNote"] = "Inversion: Wenn ein anderes Element an Position 1 steht, tauschen Subjekt und Verb die Plätze."
    elif "Negation" in title or "nicht" in title or "kein" in title:
        syntax = "Nomen mit 'ein'/Nullartikel: kein/keine + Nomen | Verben/Adjektive: ... + nicht (am Satzende)"
    else:
        # Default declarative S + V + O for sentence-level topics
        if any(w in title.lower() for w in ["clause", "verb", "preposition", "case", "adverb", "tense", "sentence", "object", "order"]):
            syntax = "[S: Subjekt] + [V: Finites Verb (Pos 2)] + [O: Objekt / Angaben]"

    # ---- VERB CONJUGATION RULES ----
    if "Regular Verb Conjugation" in title or (cat == "Verbs & Conjugation" and "Regular" in title):
        conjugation = "ich: -e | du: -st | er/sie/es: -t | wir: -en | ihr: -t | sie/Sie: -en"
        item["conjugationPattern"] = "Stamm (Infinitive minus -en) + Personalendung: lern-en -> ich lerne, du lernst, er lernt"
    elif "Ending in -d or -t" in title:
        conjugation = "ich: -e | du: -est | er/sie/es: -et | wir: -en | ihr: -et | sie/Sie: -en"
        item["conjugationPattern"] = "Einschub von '-e-' bei du, er/sie/es und ihr zur leichteren Aussprache (arbeit-est, arbeit-et)"
    elif "Ending in -s, -ß, -z" in title:
        conjugation = "ich: -e | du: -t (nicht -st!) | er/sie/es: -t | wir: -en | ihr: -t | sie/Sie: -en"
        item["conjugationPattern"] = "Stamm endet bereits auf Zischlaut: heißen -> du heißt, tanzen -> du tanzt"
    elif "'sein'" in title and "Präsens" in title or title == "The Auxiliary Verb 'sein' (to be) in Present Tense":
        conjugation = "ich bin | du bist | er/sie/es ist | wir sind | ihr seid | sie/Sie sind"
    elif "'haben'" in title and "Präsens" in title or title == "The Auxiliary Verb 'haben' (to have) in Present Tense":
        conjugation = "ich habe | du hast (ohne -b-) | er/sie/es hat (ohne -b-) | wir haben | ihr habt | sie/Sie haben"
    elif "'werden'" in title and ("Present" in title or "Präsens" in title):
        conjugation = "ich werde | du wirst | er/sie/es wird | wir werden | ihr werdet | sie/Sie werden"
    elif "e -> i" in title:
        conjugation = "ich: -e (gebe) | du: -st mit i (gibst) | er/sie/es: -t mit i (gibt) | wir: -en (geben) | ihr: -t (gebt) | sie/Sie: -en (geben)"
        item["conjugationPattern"] = "Vokalwechsel e -> i nur in der 2. & 3. Person Singular (sprechen, helfen, geben, treffen)"
    elif "e -> ie" in title:
        conjugation = "ich: -e (sehe) | du: -st mit ie (siehst) | er/sie/es: -t mit ie (sieht) | wir: -en (sehen) | ihr: -t (seht) | sie/Sie: -en (sehen)"
        item["conjugationPattern"] = "Vokalwechsel e -> ie nur bei du und er/sie/es (sehen, lesen, empfehlen)"
    elif "a -> ä" in title:
        conjugation = "ich: -e (fahre) | du: -st mit ä (fährst) | er/sie/es: -t mit ä (fährt) | wir: -en (fahren) | ihr: -t (fahrt) | sie/Sie: -en (fahren)"
        item["conjugationPattern"] = "Umlaut a -> ä nur in der 2. & 3. Person Singular (fahren, schlafen, waschen, tragen)"
    elif "au -> äu" in title:
        conjugation = "ich: laufe | du: läufst | er/sie/es: läuft | wir: laufen | ihr: lauft | sie/Sie: laufen"
    elif "'können'" in title:
        conjugation = "ich kann | du kannst | er/sie/es kann | wir können | ihr könnt | sie/Sie können"
        item["conjugationPattern"] = "1. und 3. Person Singular sind identisch und haben KEINE Personalendung!"
    elif "'müssen'" in title:
        conjugation = "ich muss | du musst | er/sie/es muss | wir müssen | ihr müsst | sie/Sie müssen"
        item["conjugationPattern"] = "1. & 3. Person Singular: ich muss, er muss (ohne Umlaut und ohne Endung)"
    elif "'dürfen'" in title:
        conjugation = "ich darf | du darfst | er/sie/es darf | wir dürfen | ihr dürft | sie/Sie dürfen"
    elif "'wollen'" in title:
        conjugation = "ich will | du willst | er/sie/es will | wir wollen | ihr wollt | sie/Sie wollen"
    elif "'möchten'" in title:
        conjugation = "ich möchte | du möchtest | er/sie/es möchte | wir möchten | ihr möchtet | sie/Sie möchten"
    elif "'sollen'" in title:
        conjugation = "ich soll | du sollst | er/sie/es soll | wir sollen | ihr sollt | sie/Sie sollen"
    elif "'mögen'" in title:
        conjugation = "ich mag | du magst | er/sie/es mag | wir mögen | ihr mögt | sie/Sie mögen"
    elif "Präteritum of 'sein'" in title:
        conjugation = "ich war | du warst | er/sie/es war | wir waren | ihr wart | sie/Sie waren"
    elif "Präteritum of 'haben'" in title:
        conjugation = "ich hatte | du hattest | er/sie/es hatte | wir hatten | ihr hattet | sie/Sie hatten"
    elif "Präteritum of Modal" in title:
        conjugation = "ich konnte/musste/durfte/wollte | du konntest/musstest... | er/sie/es konnte/musste... | wir konnten | ihr konntet | sie konnten"
        item["conjugationPattern"] = "Modalverben im Präteritum verlieren immer den Umlaut und erhalten -te Endungen."
    elif "Regular Past Participles" in title or "Partizip II" in title:
        conjugation = "Regelmäßig: ge- + Stamm + -t (z.B. gekauft, gelernt, gemacht, gehört)"
    elif "Reflexive Verbs with Accusative" in title:
        conjugation = "ich freue MICH | du freust DICH | er/sie/es freut SICH | wir freuen UNS | ihr freut EUCH | sie freuen SICH"
    elif "Reflexive Verbs with Dative" in title:
        conjugation = "ich putze MIR | du putzt DIR | er/sie/es putzt SICH | wir putzen UNS | ihr putzt EUCH | sie putzen SICH"
    elif "Konjunktiv II" in title and "würde" in title:
        conjugation = "ich würde | du würdest | er/sie/es würde | wir würden | ihr würdet | sie/Sie würden (+ Infinitiv)"
    elif "Konjunktiv II" in title and ("hätte" in title or "wäre" in title):
        conjugation = "hätte / hättest / hätte / hätten / hättet / hätten || wäre / wärst / wäre / wären / wärt / wären"
    elif "Passiv" in title and "Präsens" in title:
        conjugation = "ich werde ... | du wirst ... | er/sie/es wird ... | wir werden ... | ihr werdet ... | sie werden ... (+ Partizip II)"
    elif "Futur I" in title:
        conjugation = "ich werde | du wirst | er/sie/es wird | wir werden | ihr werdet | sie/Sie werden (+ Infinitiv)"

    # ---- CASE & DECLENSION TABLES ----
    if "Definite Articles in the Nominative" in title:
        declension = "Maskulin: der | Feminin: die | Neutral: das | Plural: die"
    elif "Indefinite Articles" in title and "Nominative" in title or title == "Indefinite Articles: ein, eine, ein":
        declension = "Maskulin: ein | Feminin: eine | Neutral: ein | Plural: (kein Plural / Nullartikel)"
    elif "Negative Article" in title:
        declension = "Maskulin: kein (Nom) / keinen (Akk) | Feminin: keine | Neutral: kein | Plural: keine"
    elif "The Accusative Case: The Direct Object" in title or "Core Verbs Governing the Accusative" in title:
        declension = "Maskulin: den / einen / keinen | Feminin: die / eine / keine | Neutral: das / ein / kein | Plural: die / keine"
        item["declensionNote"] = "Merke: Im Akkusativ ändert sich AUSSCHLIESSLICH das Maskulinum (der -> den, ein -> einen, mein -> meinen). Feminin, Neutral und Plural bleiben völlig unverändert wie im Nominativ!"
    elif "The Dative Case" in cat or "Dative Definite Articles" in title:
        declension = "Maskulin: dem | Feminin: der | Neutral: dem | Plural: den + Nomen erhält -(e)n"
        item["declensionNote"] = "Dativ-Signal: m - r - m - n (dem Mann, der Frau, dem Kind, den Kindern)."
    elif "Dative Indefinite Articles" in title:
        declension = "Maskulin: einem | Feminin: einer | Neutral: einem | Plural: keinen + Nomen-(e)n"
    elif "Dative Personal Pronouns" in title:
        declension = "ich -> mir | du -> dir | er -> ihm | sie -> ihr | es -> ihm | wir -> uns | ihr -> euch | sie/Sie -> ihnen/Ihnen"
    elif "Personal Pronouns in the Accusative" in title:
        declension = "ich -> mich | du -> dich | er -> ihn | sie -> sie | es -> es | wir -> uns | ihr -> euch | sie/Sie -> sie/Sie"
    elif "Personal Pronouns in the Nominative" in title:
        declension = "1. Person: ich (Sg.) / wir (Pl.) | 2. Person: du, ihr, Sie (formell) | 3. Person: er, sie, es / sie (Pl.)"
    elif "Possessive Determiners in Nominative" in title:
        declension = "ich: mein | du: dein | er: sein | sie: ihr | es: sein | wir: unser | ihr: euer | sie/Sie: ihr/Ihr (+ -e bei feminin/plural)"
    elif "Two-Way Prepositions" in cat or "Wechselpräpositionen" in title:
        declension = "an, auf, hinter, in, neben, über, unter, vor, zwischen || Wo? (Lage/Stillstand) -> DATIV | Wohin? (Richtung/Ziel) -> AKKUSATIV"
    elif "Pure Dative Prepositions" in title or (cat == "Prepositions" and "Dative" in title):
        declension = "aus, bei, mit, nach, seit, von, zu, gegenüber -> IMMER + DATIV (dem / der / dem / den)"
    elif "Pure Accusative Prepositions" in title or "FUD-BOG" in title or (cat == "Prepositions" and "Accusative" in title):
        declension = "bis, durch, für, gegen, ohne, um -> IMMER + AKKUSATIV (den / die / das / die)"
    elif "Genitiv" in cat or "Genitive" in title:
        declension = "Maskulin: des + Nomen-(e)s | Feminin: der | Neutral: des + Nomen-(e)s | Plural: der"
        item["declensionNote"] = "Maskuline und neutrale Nomen erhalten im Genitiv die Endung -s oder -es (des Tages, des Kindes). Feminine und Plural-Nomen erhalten keine Nomen-Endung."
    elif "Adjektivdeklination" in cat or "Adjective Declension" in cat:
        if "Type 1" in title or "Weak" in title or "Definite" in title:
            declension = "Nach der/die/das: Nom Sg & Akk Fem/Neut = -e | Alle anderen Formen (Dativ, Genitiv, Plural, Akk Maskulin) = -en"
        elif "Type 2" in title or "Mixed" in title or "Indefinite" in title:
            declension = "Nach ein/kein/mein: Nom Maskulin = -er | Nom/Akk Neutrum = -es | Nom/Akk Feminin = -e | Dativ/Genitiv/Plural = -en"
        elif "Dative" in title:
            declension = "Adjektiv im Dativ: ausnahmslos IMMER Endung '-en' (mit dem neuen Auto, zu der alten Schule)"

    if syntax:
        item["syntax"] = syntax
    if conjugation:
        item["conjugation"] = conjugation
    if declension:
        item["declension"] = declension

    # 5. Enrich examples with breakdown if breakdown missing
    ex_list = []
    for ex in item.get("examples", []):
        de_text = ex.get("de", "")
        en_text = ex.get("en", "")
        bd = ex.get("breakdown")
        if not bd:
            # Generate a helpful structural breakdown
            bd = generate_breakdown(de_text, syntax, conjugation, declension, title)
        ex_list.append({"de": de_text, "en": en_text, "breakdown": bd})
    item["examples"] = ex_list

    return item

def generate_breakdown(de_text, syntax, conjugation, declension, title):
    # Split sentence into words
    words = re.findall(r"[\wÄÖÜäöüß]+", de_text)
    if not words:
        return "Analyse der Satzstruktur"
    
    first = words[0]
    # Identify basic components
    parts = []
    if syntax and "S + V + O" in syntax:
        parts.append(f"[Pos 1: {first}]")
        if len(words) > 1:
            parts.append(f"[Pos 2: {words[1]} (Verb)]")
        if len(words) > 2:
            parts.append(f"[Mittelfeld / Objekt: {' '.join(words[2:4])}]")
        return " + ".join(parts)
    elif "Pos 1" in syntax or "V2" in title:
        parts.append(f"[Pos 1: {first}]")
        if len(words) > 1:
            parts.append(f"[Pos 2 Verb: {words[1]}]")
        if len(words) > 2:
            parts.append(f"[Pos 3 Subjekt: {words[2]}]")
        return " + ".join(parts)
    elif "weil" in de_text.lower() or "dass" in de_text.lower() or "wenn" in de_text.lower():
        last = words[-1]
        return f"[Konnektor leitet Nebensatz ein] ... [Finites Verb am Ende: '{last}']"
    elif "Modal" in title:
        last = words[-1]
        return f"[Modalverb an Pos 2: '{words[1] if len(words)>1 else ''}'] ... [Infinitiv am Satzende: '{last}']"
    elif "Perfekt" in title:
        last = words[-1]
        return f"[Hilfsverb an Pos 2: '{words[1] if len(words)>1 else ''}'] ... [Partizip II am Satzende: '{last}']"
    elif "Dativ" in title or "Dative" in title:
        return f"Grammatische Struktur: Dativ-Objekt ({de_text.split()[0:3]}...)"
    elif declension:
        return f"Deklination & Kasusstruktur im Beispielsatz"
    else:
        return f"Strukturelle Analyse: [Subjekt: {first}] + [Prädikat: {words[1] if len(words)>1 else ''}]"

if __name__ == "__main__":
    for lvl in ["a1", "a2", "b1", "b2", "c1", "c2"]:
        enrich_level(lvl)
