#!/usr/bin/env python3
"""
Generator for B2 German Grammar Dataset (105 comprehensive topics)
Ensures 100% original pedagogical examples (no examples from deutsche/german.pdf).
Level: B2 (Goethe-Zertifikat B2 / telc Deutsch B2 / Upper Intermediate)
"""
import json
import os

topics = [
    # 1-12: Zustandspassiv & Passiversatzformen
    {
        "id": "b2-pas-01",
        "level": "B2",
        "category": "Zustandspassiv & Passiversatzformen",
        "title": "Zustandspassiv im Präsens (sein + Partizip II)",
        "rule": "Das Zustandspassiv drückt nicht die fortschreitende Handlung aus, sondern das vollendete Ergebnis bzw. den resultierenden Zustand eines vorangegangenen Prozesses. Es wird mit konjugiertem 'sein' und dem Partizip II gebildet.",
        "formula": "Subjekt + sein (Präsens) + ... + Partizip II",
        "examples": [
            {"de": "Die Eingangstür ist bereits seit 20 Uhr abgeschlossen.", "en": "The entrance door has already been locked since 8 PM.", "breakdown": "ist abgeschlossen (Zustand) vs. wird abgeschlossen (Handlung)"},
            {"de": "Alle Rechnungen für das laufende Quartal sind bezahlt.", "en": "All invoices for the current quarter are paid.", "breakdown": "sind bezahlt = abgeschlossener Endzustand"},
            {"de": "Die Berliner Niederlassung ist wegen Renovierung vorübergehend geschlossen.", "en": "The Berlin branch is temporarily closed due to renovation.", "breakdown": "ist geschlossen"},
            {"de": "Das neue Softwaremodul ist vollständig konfiguriert und einsatzbereit.", "en": "The new software module is completely configured and ready for use.", "breakdown": "ist konfiguriert"}
        ],
        "takeaway": "Vorgangspassiv (werden) = Film / Handlung; Zustandspassiv (sein) = Foto / fertiges Resultat."
    },
    {
        "id": "b2-pas-02",
        "level": "B2",
        "category": "Zustandspassiv & Passiversatzformen",
        "title": "Zustandspassiv im Präteritum: war + Partizip II",
        "rule": "Das Zustandspassiv der Vergangenheit drückt aus, dass sich ein Gegenstand oder Sachverhalt in einem früheren Zustand befand. Bildung: war / waren + Partizip II.",
        "formula": "Subjekt + war / waren + ... + Partizip II",
        "examples": [
            {"de": "Als wir am Museum ankamen, war der Ticketschalter bereits geschlossen.", "en": "When we arrived at the museum, the ticket counter was already closed.", "breakdown": "war geschlossen (Zustand in der Vergangenheit)"},
            {"de": "Die Autobahn war stundenlang wegen Glatteis gesperrt.", "en": "The motorway was blocked for hours due to black ice.", "breakdown": "war gesperrt"},
            {"de": "Das Angebot war bis Ende letzten Monats befristet.", "en": "The offer was limited until the end of last month.", "breakdown": "war befristet"},
            {"de": "Alle Dokumente waren ordentlich im Archivordner abgelegt.", "en": "All documents were neatly filed away in the archive folder.", "breakdown": "waren abgelegt"}
        ],
        "takeaway": "war + Partizip II beschreibt einen Zustand, der in der Vergangenheit vorlag."
    },
    {
        "id": "b2-pas-03",
        "level": "B2",
        "category": "Zustandspassiv & Passiversatzformen",
        "title": "Passiversatzform: man + Aktiv",
        "rule": "Anstelle des Passivs kann im Deutschen sehr häufig das unbestimmte Pronomen 'man' mit der 3. Person Singular Aktiv verwendet werden. Dies wirkt lebendiger und persönlicher.",
        "formula": "man + Verb (3. Pers. Sing. Aktiv)",
        "examples": [
            {"de": "In modernen Büros arbeitet man oft in agilen Teams.", "en": "In modern offices, people often work in agile teams.", "breakdown": "man arbeitet = es wird gearbeitet"},
            {"de": "Hier spricht man Deutsch und Englisch.", "en": "German and English are spoken here.", "breakdown": "man spricht = es wird gesprochen"},
            {"de": "Den Vertrag kann man online innerhalb weniger Minuten kündigen.", "en": "The contract can be cancelled online within a few minutes.", "breakdown": "kann man kündigen = kann gekündigt werden"},
            {"de": "Man feiert das Festival jedes Jahr im Spätsommer.", "en": "The festival is celebrated every year in late summer.", "breakdown": "man feiert = wird gefeiert"}
        ],
        "takeaway": "'man' ersetzt Passivstrukturen im Alltag und gesprochenen Deutsch elegant."
    },
    {
        "id": "b2-pas-04",
        "level": "B2",
        "category": "Zustandspassiv & Passiversatzformen",
        "title": "Passiversatzform: sein + zu + Infinitiv (Möglichkeit / Notwendigkeit)",
        "rule": "'sein + zu + Infinitiv' hat IMMER passive Bedeutung. Je nach Kontext drückt es eine Notwendigkeit ('müssen / sollen getan werden') oder eine Möglichkeit ('können getan werden') aus.",
        "formula": "Subjekt + sein (konjugiert) + zu + Infinitiv",
        "examples": [
            {"de": "Diese vertraulichen Sicherheitsfragen sind strengstens zu beachten.", "en": "These confidential safety questions are strictly to be observed.", "breakdown": "sind zu beachten = müssen beachtet werden (Notwendigkeit)"},
            {"de": "Der neue Roman von Juli Zeh ist in jeder Buchhandlung zu finden.", "en": "The new novel by Juli Zeh is to be found in every bookstore.", "breakdown": "ist zu finden = kann gefunden werden (Möglichkeit)"},
            {"de": "Die Ursachen für den Serverausfall sind noch zu klären.", "en": "The causes of the server failure remain to be clarified.", "breakdown": "sind zu klären = müssen noch geklärt werden"},
            {"de": "Diese alten Akten sind sofort zu vernichten.", "en": "These old files are to be destroyed immediately.", "breakdown": "sind zu vernichten = müssen vernichtet werden"}
        ],
        "takeaway": "'sein + zu + Infinitiv' = muss gemacht werden (Notwendigkeit) oder kann gemacht werden (Möglichkeit)."
    },
    {
        "id": "b2-pas-05",
        "level": "B2",
        "category": "Zustandspassiv & Passiversatzformen",
        "title": "Passiversatzform: sich lassen + Infinitiv (Möglichkeit)",
        "rule": "'sich lassen + Infinitiv' drückt immer eine MÖGLICHKEIT im Passiv aus ('kann gemacht werden'). Das Subjekt ist eine Sache.",
        "formula": "Sache + lässt sich / lassen sich + Infinitiv",
        "examples": [
            {"de": "Die Batterie dieses neuen Elektroautos lässt sich in zwanzig Minuten aufladen.", "en": "The battery of this new electric car can be charged in twenty minutes.", "breakdown": "lässt sich aufladen = kann aufgeladen werden"},
            {"de": "Dieses knifflige Computerproblem lässt sich nicht so einfach beheben.", "en": "This tricky computer problem cannot be solved so easily.", "breakdown": "lässt sich nicht beheben = kann nicht behoben werden"},
            {"de": "Solche Missverständnisse lassen sich durch offene Kommunikation vermeiden.", "en": "Such misunderstandings can be avoided through open communication.", "breakdown": "lassen sich vermeiden = können vermieden werden"},
            {"de": "Die Schriftgröße lässt sich in den Systemeinstellungen flexibel anpassen.", "en": "The font size can be adjusted flexibly in system settings.", "breakdown": "lässt sich anpassen = kann angepasst werden"}
        ],
        "takeaway": "'lässt sich machen' = 'kann gemacht werden' (drückt rein passive Machbarkeit aus)."
    },
    {
        "id": "b2-pas-06",
        "level": "B2",
        "category": "Zustandspassiv & Passiversatzformen",
        "title": "Passiversatzform: Adjektive auf -bar, -lich und -abel (Möglichkeit)",
        "rule": "Adjektive mit den Suffixen -bar (machbar, lösbar, erkennbar), -lich (verständlich, vermeidbar) oder Fremdwörter auf -abel/-ibel (reparabel, flexibel) drücken das passive Potenzial 'kann getan werden' aus.",
        "formula": "Adjektiv auf -bar / -lich / -abel = kann + Partizip II + werden",
        "examples": [
            {"de": "Die Aufgabe ist innerhalb des Budgets durchaus lösbar.", "en": "The task is definitely solvable within budget.", "breakdown": "lösbar = kann gelöst werden"},
            {"de": "Der Handschrift des Arztes war kaum leserlich.", "en": "The doctor's handwriting was barely legible.", "breakdown": "leserlich = konnte kaum gelesen werden"},
            {"de": "Dieser Schaden an der Stoßstange ist glücklicherweise reparabel.", "en": "This damage to the bumper is fortunately repairable.", "breakdown": "reparabel = kann repariert werden"},
            {"de": "Das Leitungswasser in Berlin ist bedenkenlos trinkbar.", "en": "Tap water in Berlin is drinkable without hesitation.", "breakdown": "trinkbar = kann getrunken werden"}
        ],
        "takeaway": "-bar / -lich / -abel verkürzen passive Passivsätze zu prägnanten Adjektiven."
    },
    {
        "id": "b2-pas-07",
        "level": "B2",
        "category": "Zustandspassiv & Passiversatzformen",
        "title": "Passiversatzform: es gilt + zu + Infinitiv (Notwendigkeit)",
        "rule": "Der unpersönliche Ausdruck 'es gilt + zu + Infinitiv' drückt gehobene Notwendigkeit oder ein wichtiges Gebot aus ('es muss getan werden' / 'it is essential to').",
        "formula": "Es gilt, ... zu + Infinitiv",
        "examples": [
            {"de": "Im kommenden Geschäftsjahr gilt es, die Marktanteile in Europa auszubauen.", "en": "In the upcoming fiscal year, it is essential to expand market share in Europe.", "breakdown": "gilt es auszubauen = muss ausgebaut werden"},
            {"de": "Jetzt gilt es, Ruhe zu bewahren und überlegte Schritte einzuleiten.", "en": "Now it is crucial to remain calm and initiate deliberate steps.", "breakdown": "gilt es zu bewahren = muss bewahrt werden"},
            {"de": "Es gilt, die Privatsphäre der Nutzer stets verlässlich zu schützen.", "en": "It is essential to protect users' privacy reliably at all times.", "breakdown": "gilt es zu schützen"},
            {"de": "Bei dieser Verhandlung gilt es, keine voreiligen Zugeständnisse zu machen.", "en": "In this negotiation, it is vital not to make premature concessions.", "breakdown": "gilt es... zu machen"}
        ],
        "takeaway": "'Es gilt zu tun' ist eine stilistisch elegante Notwendigkeitsformel für Berichte und Reden."
    },
    {
        "id": "b2-pas-08",
        "level": "B2",
        "category": "Zustandspassiv & Passiversatzformen",
        "title": "Passiversatzform: gehören + Partizip II (Umgangssprachliche Notwendigkeit)",
        "rule": "In der Alltagssprache drückt 'gehören + Partizip II' eine dringende Notwendigkeit oder moralische Pflicht aus ('sollte dringend gemacht werden').",
        "formula": "Subjekt + gehört / gehören + Partizip II",
        "examples": [
            {"de": "Diese gefährliche Kreuzung gehört dringend mit einer Ampel geregelt.", "en": "This dangerous intersection urgently needs to be regulated with a traffic light.", "breakdown": "gehört geregelt = sollte geregelt werden"},
            {"de": "Dieses uralte Smartphone gehört längst auf den Elektroschrott geworfen.", "en": "This ancient smartphone should have been thrown onto the electronic scrap long ago.", "breakdown": "gehört geworfen"},
            {"de": "Solch betrügerisches Verhalten gehört gesetzlich verboten.", "en": "Such fraudulent behavior ought to be prohibited by law.", "breakdown": "gehört verboten = muss/sollte verboten werden"},
            {"de": "Deine durchnässte Jacke gehört sofort auf die Heizung gehängt.", "en": "Your soaked jacket ought to be hung on the radiator right away.", "breakdown": "gehört gehängt"}
        ],
        "takeaway": "'gehört gemacht' = nachdrückliche alltägliche Aufforderung: Das gehört bestraft!"
    },
    {
        "id": "b2-pas-09",
        "level": "B2",
        "category": "Zustandspassiv & Passiversatzformen",
        "title": "Passiversatzform: Passivierende Reflexivverben (sich verkaufen, sich finden)",
        "rule": "Einige Verben können reflexiv gebraucht werden, um auszudrücken, wie ein Gegenstand gehandhabt oder beurteilt werden kann (meist in Verbindung mit einem bewertenden Adverb: gut, leicht, schwer).",
        "formula": "Sache + lässt sich / verkauft sich / liest sich + Adverb",
        "examples": [
            {"de": "Der neue Kriminalroman liest sich wie ein spannender Kinofilm.", "en": "The new crime novel reads like an exciting cinematic movie.", "breakdown": "liest sich = kann spannend gelesen werden"},
            {"de": "Das neue Elektrofahrrad verkauft sich derzeit hervorragend.", "en": "The new e-bike is currently selling outstandingly.", "breakdown": "verkauft sich = wird viel verkauft"},
            {"de": "Für dieses knifflige Rätsel findet sich sicher bald eine clevere Lösung.", "en": "A clever solution for this tricky riddle will surely be found soon.", "breakdown": "findet sich = wird gefunden werden"},
            {"de": "Dieser weiche Wollstoff wäscht sich überraschend unkompliziert.", "en": "This soft wool fabric washes surprisingly easily.", "breakdown": "wäscht sich gut = kann gut gewaschen werden"}
        ],
        "takeaway": "Verben wie sich lesen, sich verkaufen, sich öffnen nehmen passivische Eigenschaften an."
    },
    {
        "id": "b2-pas-10",
        "level": "B2",
        "category": "Zustandspassiv & Passiversatzformen",
        "title": "Passiversatzform: stehen / zur Verfügung stehen vs. stellen",
        "rule": "Funktionsverbgefüge mit 'stehen' drücken oft einen passiven Zustand aus ('wird bereitgestellt'), während Verbindungen mit 'stellen' die aktive Handlung bezeichnen ('jemand stellt bereit').",
        "formula": "stehen = passiv (wird geboten) | stellen = aktiv (jemand bietet an)",
        "examples": [
            {"de": "Den Konferenzteilnehmern steht kostenloses WLAN zur Verfügung.", "en": "Free Wi-Fi is available to the conference attendees.", "breakdown": "steht zur Verfügung = wird bereitgestellt (passiv)"},
            {"de": "Das Hotel stellt seinen Gästen Leihräder zur Verfügung.", "en": "The hotel provides rental bikes to its guests.", "breakdown": "stellt zur Verfügung = stellt bereit (aktiv)"},
            {"de": "Der Gesetzentwurf steht morgen im Bundestag zur Abstimmung.", "en": "The bill is up for a vote in the Bundestag tomorrow.", "breakdown": "steht zur Abstimmung = wird abgestimmt (passiv)"},
            {"de": "Die Opposition stellte den Ministerpräsidenten zur Rede.", "en": "The opposition called the prime minister to account.", "breakdown": "stellte zur Rede = forderte Erklärung (aktiv)"}
        ],
        "takeaway": "stehen zur Verfügung (Passiv) vs. stellen zur Verfügung (Aktiv)."
    },

    # 11-25: Konjunktiv I (Indirekte Rede)
    {
        "id": "b2-k1-11",
        "level": "B2",
        "category": "Konjunktiv I (Indirekte Rede)",
        "title": "Konjunktiv I: Grundprinzip und Einsatz in Presse und Nachrichten",
        "rule": "Der Konjunktiv I wird vor allem im Journalismus, in Protokollen und wissenschaftlichen Berichten verwendet, um Aussagen Dritter neutral und ohne eigene Wertung in der indirekten Rede wiederzugeben.",
        "formula": "Verbstamm Präsens + Konjunktiv-Endung (-e, -est, -e, -en, -et, -en)",
        "examples": [
            {"de": "Der Finanzminister betonte, die Inflation gehe in diesem Quartal spürbar zurück.", "en": "The finance minister emphasized that inflation is declining noticeably this quarter.", "breakdown": "gehe = Konjunktiv I von gehen (3. Person Singular)"},
            {"de": "Die Zeugin sagte aus, der Angeklagte sei zur Tatzeit nicht am Tatort gewesen.", "en": "The witness testified that the defendant was not at the crime scene at the time of the crime.", "breakdown": "sei gewesen = Konjunktiv I Vergangenheit"},
            {"de": "Die Sprecherin erklärte, das Unternehmen plane weitere Investitionen.", "en": "The spokesperson declared that the company plans further investments.", "breakdown": "plane = Konjunktiv I von planen"},
            {"de": "Der Wetterbericht meldet, morgen falle im gesamten Bergland Schnee.", "en": "The weather forecast reports that snow will fall tomorrow across all mountain regions.", "breakdown": "falle = Konjunktiv I von fallen"}
        ],
        "takeaway": "Konjunktiv I signalisiert Neutralität: 'Ich berichte nur, was jemand gesagt hat, ohne Garantie'."
    },
    {
        "id": "b2-k1-12",
        "level": "B2",
        "category": "Konjunktiv I (Indirekte Rede)",
        "title": "Konjunktiv I von 'sein': sei, seiest, sei, seien, seiet, seien",
        "rule": "'sein' ist das einzige deutsche Verb, dessen Konjunktiv-I-Formen in ALLEN Personen völlig eindeutig sind und sich vom Indikativ unterscheiden. Daher wird 'sein' am häufigsten im Konjunktiv I angetroffen.",
        "formula": "ich sei, du sei(e)st, er/sie/es sei, wir seien, ihr seiet, sie/Sie seien",
        "examples": [
            {"de": "Der Arzt versicherte, der Patient sei außer Lebensgefahr.", "en": "The doctor assured that the patient is out of danger of life.", "breakdown": "sei = Konjunktiv I Singular"},
            {"de": "Sie sagte, sie seien mit dem neuen Vertrag sehr zufrieden.", "en": "She said they are very satisfied with the new contract.", "breakdown": "seien = Konjunktiv I Plural"},
            {"de": "Er behauptete, er sei gestern den ganzen Abend zu Hause gewesen.", "en": "He claimed that he had been home all evening yesterday.", "breakdown": "sei gewesen = Vergangenheit im Konjunktiv I"},
            {"de": "Die Prüfer erklärten, die Resultate seien überdurchschnittlich gut.", "en": "The examiners explained that results are above average.", "breakdown": "seien = Konjunktiv I von sein"}
        ],
        "takeaway": "Er sei, sie seien – die Paradeformen des Konjunktiv I."
    },
    {
        "id": "b2-k1-13",
        "level": "B2",
        "category": "Konjunktiv I (Indirekte Rede)",
        "title": "Konjunktiv I: Die wichtige 3. Person Singular (er/sie/es)",
        "rule": "Da die 1. Person Singular (ich) und die Pluralformen (wir, sie) im Konjunktiv I oft identisch mit dem Indikativ Präsens sind (z.B. wir haben, sie kommen), wird Konjunktiv I fast ausschließlich in der 3. Person Singular verwendet: er habe, er wolle, er wisse.",
        "formula": "Stamm + -e: er gehe, sie habe, es gebe, er könne",
        "examples": [
            {"de": "Der Pressesprecher teilte mit, der Vorstand habe alle Vorwürfe zurückgewiesen.", "en": "The press spokesman communicated that the executive board has rejected all allegations.", "breakdown": "habe = Konjunktiv I von haben"},
            {"de": "Sie meinte, das neue Konzept funktioniere in der Praxis hervorragend.", "en": "She reckoned that the new concept works outstandingly in practice.", "breakdown": "funktioniere = Konjunktiv I von funktionieren"},
            {"de": "Er versprach, er werde das Dokument noch heute Nachmittag überarbeiten.", "en": "He promised that he would revise the document this afternoon.", "breakdown": "werde = Konjunktiv I von werden"},
            {"de": "Der Forscher berichtete, der Wirkstoff zeige bereits positive Effekte.", "en": "The researcher reported that the active agent is already showing positive effects.", "breakdown": "zeige = Konjunktiv I von zeigen"}
        ],
        "takeaway": "In der 3. Person Singular ist der Konjunktiv I immer glasklar unterscheidbar: er habe, er komme, er lebe."
    },
    {
        "id": "b2-k1-14",
        "level": "B2",
        "category": "Konjunktiv I (Indirekte Rede)",
        "title": "Ersatzregel: Konjunktiv II bei Formengleichheit mit dem Indikativ",
        "rule": "Wenn die Konjunktiv-I-Form mit dem Indikativ Präsens IDENTISCH ist (z.B. 'sie haben', 'wir machen'), weicht man zwingend auf den Konjunktiv II aus ('sie hätten', 'wir machten / würden machen'), um die indirekte Rede zu kennzeichnen.",
        "formula": "Wenn Konjunktiv I == Indikativ -> Ersetze durch Konjunktiv II!",
        "examples": [
            {"de": "Die Abgeordneten sagten, sie hätten (K II) keine Zeit für Debatten.", "en": "The MPs said they had no time for debates.", "breakdown": "sie haben (Indikativ) == sie haben (K I) -> Ausweichform: hätten (K II)"},
            {"de": "Die Nachbarn behaupteten, sie wüssten (K II) von keinem Einbruch.", "en": "The neighbors claimed they knew nothing of any burglary.", "breakdown": "Ausweichform zu 'sie wissen'"},
            {"de": "Sie erklärten, sie würden (K II) das Projekt unverzüglich stoppen.", "en": "They explained that they would stop the project immediately.", "breakdown": "würden stoppen statt stießen"},
            {"de": "Die Zeugen gaben an, sie schliefen (oder: würden schlafen), als der Alarm losging.", "en": "The witnesses stated that they were sleeping when the alarm went off.", "breakdown": "Ersatzform Konjunktiv II"}
        ],
        "takeaway": "Goldene Regel: Ist Konjunktiv I gleich Indikativ, muss Konjunktiv II einspringen."
    },
    {
        "id": "b2-k1-15",
        "level": "B2",
        "category": "Konjunktiv I (Indirekte Rede)",
        "title": "Indirekte Rede in der Vergangenheit: sei / habe + Partizip II",
        "rule": "In der indirekten Rede gibt es für alle drei Vergangenheitsformen des Indikativs (Perfekt, Präteritum, Plusquamperfekt) NUR EINE EINZIGE Konjunktivform: Konjunktiv I von haben/sein + Partizip II.",
        "formula": "er habe + Partizip II (haben-Verben) | er sei + Partizip II (sein-Verben)",
        "examples": [
            {"de": "Aktiv Indikativ: 'Er kam gestern an.' -> Indirekt: Er sagte, er sei gestern angekommen.", "en": "Direct: 'He arrived yesterday.' -> Indirect: He said he arrived yesterday.", "breakdown": "sei angekommen fasst Präteritum/Perfekt zusammen"},
            {"de": "Aktiv Indikativ: 'Ich habe das Buch gelesen.' -> Indirekt: Sie meinte, sie habe das Buch gelesen.", "en": "Direct: 'I read the book.' -> Indirect: She reckoned she had read the book.", "breakdown": "habe gelesen"},
            {"de": "Der Pilot meldete, das Flugzeug sei pünktlich gestartet.", "en": "The pilot reported that the airplane had taken off on time.", "breakdown": "sei gestartet"},
            {"de": "Er behauptete, er habe die Geschwindigkeitsbegrenzung nicht gesehen.", "en": "He claimed that he had not seen the speed limit.", "breakdown": "habe... gesehen"}
        ],
        "takeaway": "Präteritum, Perfekt und Plusquamperfekt schrumpfen in der indirekten Rede zu: habe/sei + Partizip II."
    },
    {
        "id": "b2-k1-16",
        "level": "B2",
        "category": "Konjunktiv I (Indirekte Rede)",
        "title": "Indirekte Fragesätze: W-Fragen und Ja/Nein-Fragen (ob)",
        "rule": "Bei der Umwandlung direkter Fragen in die indirekte Rede bleibt das Fragewort (wo, wann, wer) als Einleitung erhalten. Entscheidungsfragen (Ja/Nein) werden mit der Konjunktion 'ob' eingeleitet. Das Verb steht am Satzende im Konjunktiv.",
        "formula": "Fragewort / ob + Subjekt + ... + Verb im Konjunktiv",
        "examples": [
            {"de": "Direkt: 'Kommt der Chef heute?' -> Indirekt: Die Sekretärin fragte, ob der Chef heute komme.", "en": "Direct: 'Is the boss coming today?' -> Indirect: The secretary asked whether the boss was coming today.", "breakdown": "ob + komme (Konjunktiv I)"},
            {"de": "Direkt: 'Wann fährt der Zug ab?' -> Indirekt: Der Tourist erkundigte sich, wann der Zug abfahre.", "en": "Direct: 'When does the train depart?' -> Indirect: The tourist inquired when the train departs.", "breakdown": "wann + abfahre"},
            {"de": "Sie wollte wissen, wer für das Budget verantwortlich sei.", "en": "She wanted to know who was responsible for the budget.", "breakdown": "wer + verantwortlich sei"},
            {"de": "Er fragte die Kollegen, ob sie den neuen Entwurf schon geprüft hätten.", "en": "He asked colleagues whether they had checked the new draft already.", "breakdown": "ob + geprüft hätten (K II als Ersatzform)"}
        ],
        "takeaway": "Entscheidungsfrage = ob; Ergänzungsfrage = W-Wort; Verb rückt ans Satzende."
    },
    {
        "id": "b2-k1-17",
        "level": "B2",
        "category": "Konjunktiv I (Indirekte Rede)",
        "title": "Indirekte Aufforderung und Imperativ mit 'sollen' und 'mögen'",
        "rule": "Befehle, Bitten oder Aufforderungen aus der direkten Rede können im Konjunktiv nicht direkt als Imperativ wiedergegeben werden. Sie werden durch die Modalverben 'sollen' (Aufforderung) oder 'mögen' (höfliche Bitte) im Konjunktiv I umschrieben.",
        "formula": "er solle / sie möge + Infinitiv am Satzende",
        "examples": [
            {"de": "Direkt: 'Öffnen Sie das Fenster!' -> Indirekt: Die Lehrerin bat ihn, er solle das Fenster öffnen.", "en": "Direct: 'Open the window!' -> Indirect: The teacher asked him to open the window.", "breakdown": "solle öffnen"},
            {"de": "Der Arzt ordnete an, der Patient solle täglich zwei Liter Wasser trinken.", "en": "The doctor ordered that the patient should drink two liters of water daily.", "breakdown": "solle trinken"},
            {"de": "Die Gastgeberin ließ ausrichten, die Gäste möchten bitte Platz nehmen.", "en": "The hostess had word sent that the guests might please take a seat.", "breakdown": "möchten = höfliche Bitte"},
            {"de": "Der Polizist forderte den Fahrer auf, er solle unverzüglich anhalten.", "en": "The police officer demanded of the driver that he should halt immediately.", "breakdown": "solle anhalten"}
        ],
        "takeaway": "Imperativ in indirekter Rede: immer 'sollen' (Befehl) oder 'mögen' (höfliche Bitte)."
    },
    {
        "id": "b2-k1-18",
        "level": "B2",
        "category": "Konjunktiv I (Indirekte Rede)",
        "title": "Pronominalanpassung und Zeitverschiebung in der indirekten Rede",
        "rule": "Beim Wechsel von direkter zu indirekter Rede müssen Personalpronomen, Possessivpronomen und Orts-/Zeitangaben an die Sprecherperspektive angepasst werden (ich -> er/sie; heute -> an jenem Tag; hier -> dort).",
        "formula": "ich -> er/sie | mein -> sein/ihr | hier -> dort | heute -> an jenem Tag",
        "examples": [
            {"de": "Direkt: 'Ich bringe heute mein neues Auto mit.' -> Indirekt: Er sagte, er bringe an jenem Tag sein neues Auto mit.", "en": "Direct: 'I bring my new car today.' -> Indirect: He said he brings his new car that day.", "breakdown": "ich -> er, mein -> sein, heute -> an jenem Tag"},
            {"de": "Sie versicherte: 'Wir wohnen gerne hier.' -> Sie versicherte, sie wohnten gerne dort.", "en": "She assured: 'We like living here.' -> She assured that they liked living there.", "breakdown": "wir -> sie, hier -> dort"},
            {"de": "Er betonte: 'Morgen besuche ich meine Eltern.' -> Er betonte, er besuche am folgenden Tag seine Eltern.", "en": "He stressed: 'Tomorrow I visit my parents.' -> He stressed that he visited his parents the following day.", "breakdown": "morgen -> am folgenden Tag"},
            {"de": "Sie sagte: 'Ich habe gestern meinen Schlüssel verloren.' -> Sie sagte, sie habe am Vortag ihren Schlüssel verloren.", "en": "She said: 'I lost my key yesterday.' -> She said she had lost her key the previous day.", "breakdown": "gestern -> am Vortag"}
        ],
        "takeaway": "Nicht nur das Verb ändert sich: Pronomen und Zeitwörter müssen mitwandern."
    },
    {
        "id": "b2-k1-19",
        "level": "B2",
        "category": "Konjunktiv I (Indirekte Rede)",
        "title": "Indirekte Rede mit 'dass' vs. ohne 'dass' (Hauptsatzstellung)",
        "rule": "Indirekte Rede kann mit 'dass' eingeleitet werden (dann steht das konjugierte Verb am Satzende). Lässt man 'dass' weg, folgt Hauptsatzstellung mit Verb auf Position 2!",
        "formula": "Mit dass: ..., dass er komme (Verb Ende) | Ohne dass: ..., er komme morgen (Verb Pos 2)",
        "examples": [
            {"de": "Mit 'dass': Er behauptete, dass er den Schlüssel nicht gesehen habe.", "en": "With 'that': He claimed that he hadn't seen the key.", "breakdown": "Verb habe am Satzende"},
            {"de": "Ohne 'dass': Er behauptete, er habe den Schlüssel nicht gesehen.", "en": "Without 'that': He claimed he hadn't seen the key.", "breakdown": "Verb habe auf Position 2 nach dem Subjekt er"},
            {"de": "Die Kanzlerin teilte mit, die Regierung werde das Paket rasch umsetzen.", "en": "The Chancellor communicated that the government will implement the package swiftly.", "breakdown": "ohne dass, Verb werde auf Pos 2"},
            {"de": "Der Wetterdienst warnte, dass starke Unwetter über das Land zögen.", "en": "The weather service warned that severe storms were moving across the country.", "breakdown": "mit dass, Verb zögen am Satzende"}
        ],
        "takeaway": "Ohne 'dass' steht das Verb im Konjunktiv auf Position 2 – das ist im Journalismus der Regelfall."
    },
    {
        "id": "b2-k1-20",
        "level": "B2",
        "category": "Konjunktiv I (Indirekte Rede)",
        "title": "Subjektive Distanzierung: Laut / Nach Angaben von vs. Konjunktiv I",
        "rule": "Neben dem Konjunktiv I kann die Urheberschaft einer Information auch durch Präpositionalphrasen wie 'laut + Dativ/Genitiv' oder 'nach Angaben + Genitiv' ausgedrückt werden. Beide Mittel können kombiniert werden.",
        "formula": "Laut + Dat/Gen / Nach Angaben von + Dat + Indikativ oder Konjunktiv I",
        "examples": [
            {"de": "Laut Polizeiangaben ereignete sich der Unfall am frühen Montagmorgen.", "en": "According to police information, the accident occurred early Monday morning.", "breakdown": "Laut Polizeiangaben"},
            {"de": "Nach Angaben des Ministeriums liege die Arbeitslosenquote auf einem Tiefstand.", "en": "According to ministry data, the unemployment rate is at a record low.", "breakdown": "nach Angaben + Konjunktiv I liege"},
            {"de": "Wie der Sprecher mitteilte, seien alle Verhandlungen vorerst ausgesetzt.", "en": "As the spokesperson communicated, all negotiations are suspended for now.", "breakdown": "Wie mitteilte + seien"},
            {"de": "Dem Bericht zufolge hat das Startup sein Umsatzziel vorzeitig erreicht.", "en": "According to the report, the startup reached its sales target ahead of time.", "breakdown": "Dem Bericht zufolge (nachgestelltes zufolge + Dativ)"}
        ],
        "takeaway": "Laut, nach Angaben und zufolge kennzeichnen Quellen präzise."
    },

    # 21-45: Funktionsverbgefüge (Nomen-Verb-Verbindungen)
    {
        "id": "b2-fvg-21",
        "level": "B2",
        "category": "Nomen-Verb-Verbindungen (FVG)",
        "title": "Grundprinzip der Funktionsverbgefüge (FVG)",
        "rule": "Ein Funktionsverbgefüge besteht aus einem Substantiv (oft mit Präposition) und einem verblassten Verb (Funktionsverb). Die eigentliche semantische Bedeutung liegt im Substantiv, während das Verb nur grammatische Aufgaben übernimmt. FVG gehören zum gehobenen B2/C1-Sprachstil.",
        "formula": "Nomen (+ Präposition) + Funktionsverb (z.B. eine Entscheidung treffen = entscheiden)",
        "examples": [
            {"de": "Der Vorstand muss heute eine endgültige Entscheidung treffen.", "en": "The board must make a definitive decision today.", "breakdown": "eine Entscheidung treffen = entscheiden"},
            {"de": "Wir müssen alle relevanten Faktoren in Betracht ziehen.", "en": "We must take all relevant factors into consideration.", "breakdown": "in Betracht ziehen = berücksichtigen"},
            {"de": "Der neue Vorschlag stieß bei den Mitarbeitern auf scharfe Kritik.", "en": "The new proposal met with sharp criticism among employees.", "breakdown": "auf Kritik stoßen = kritisiert werden"},
            {"de": "Die neuen Umweltauflagen treten ab Januar in Kraft.", "en": "The new environmental regulations come into effect from January.", "breakdown": "in Kraft treten = wirksam/gültig werden"}
        ],
        "takeaway": "FVG machen Texte präziser, sachlicher und fachsprachlicher: Nomen trägt die Bedeutung."
    },
    {
        "id": "b2-fvg-22",
        "level": "B2",
        "category": "Nomen-Verb-Verbindungen (FVG)",
        "title": "FVG: eine Entscheidung treffen (entscheiden)",
        "rule": "'eine Entscheidung treffen' bedeutet 'sich entscheiden' oder 'einen Entschluss fassen'. Häufig mit Adjektiven: eine schwere / mutige / weitreichende Entscheidung treffen.",
        "formula": "eine Entscheidung treffen (über + Akk)",
        "examples": [
            {"de": "Nach wochenlangen Debatten hat die Kommission endlich eine Entscheidung getroffen.", "en": "After weeks of debate, the commission finally made a decision.", "breakdown": "eine Entscheidung getroffen"},
            {"de": "Wir müssen bald eine Entscheidung über den künftigen Standort treffen.", "en": "We must make a decision about the future location soon.", "breakdown": "Entscheidung über + Akkusativ"},
            {"de": "Der Richter hat ein gerechtes Urteil gefällt.", "en": "The judge handed down a fair verdict.", "breakdown": "ein Urteil fällen = juristische Variante"},
            {"de": "Es fällt mir schwer, in solchen Notfällen rasch eine Entscheidung zu treffen.", "en": "I find it hard to make a quick decision in such emergencies.", "breakdown": "eine Entscheidung treffen"}
        ],
        "takeaway": "eine Entscheidung treffen = sich entscheiden."
    },
    {
        "id": "b2-fvg-23",
        "level": "B2",
        "category": "Nomen-Verb-Verbindungen (FVG)",
        "title": "FVG: in Betracht ziehen (berücksichtigen)",
        "rule": "'etwas in Betracht ziehen' bedeutet 'etwas erwägen / berücksichtigen' (to consider / take into account).",
        "formula": "etwas (Akk) in Betracht ziehen",
        "examples": [
            {"de": "Wir sollten auch alternative Energieträger ernsthaft in Betracht ziehen.", "en": "We should also seriously consider alternative energy sources.", "breakdown": "in Betracht ziehen = erwägen"},
            {"de": "Haben Sie bei Ihrer Finanzkalkulation unvorhergesehene Ausgaben in Betracht gezogen?", "en": "Did you take unforeseen expenses into account in your financial calculation?", "breakdown": "in Betracht gezogen"},
            {"de": "Diese Option kommt für unser Unternehmen gar nicht in Betracht.", "en": "This option is entirely out of the question for our company.", "breakdown": "in Betracht kommen = in Frage kommen (passivisch)"},
            {"de": "Man muss alle Risiken sorgfältig in Betracht ziehen.", "en": "One must consider all risks carefully.", "breakdown": "in Betracht ziehen"}
        ],
        "takeaway": "in Betracht ziehen (aktiv) vs. in Betracht kommen (passiv/Möglichkeit)."
    },
    {
        "id": "b2-fvg-24",
        "level": "B2",
        "category": "Nomen-Verb-Verbindungen (FVG)",
        "title": "FVG: in Frage stellen vs. in Frage kommen",
        "rule": "'etwas in Frage stellen' bedeutet 'an etwas zweifeln / etwas anzweifeln' (to call into question). Dagegen bedeutet 'in Frage kommen' 'möglich / denkbar sein' (to be an option).",
        "formula": "in Frage stellen (aktiv = zweifeln) | in Frage kommen (passiv = möglich sein)",
        "examples": [
            {"de": "Niemand stellt deine fachliche Kompetenz in Frage.", "en": "Nobody calls your technical competence into question.", "breakdown": "in Frage stellen = bezweifeln"},
            {"de": "Eine Gehaltskürzung kommt für uns unter keinen Umständen in Frage.", "en": "A salary cut is out of the question for us under any circumstances.", "breakdown": "in Frage kommen = denkbar sein"},
            {"de": "Die neuen Beweise stellen die gesamte bisherige Theorie in Frage.", "en": "The new evidence calls the entire existing theory into question.", "breakdown": "in Frage stellen"},
            {"de": "Welche Bewerber kommen für die Leitungsposition in Frage?", "en": "Which applicants are eligible for the managerial position?", "breakdown": "in Frage kommen = geeignet/möglich sein"}
        ],
        "takeaway": "in Frage stellen = anzweifeln; in Frage kommen = möglich/akzeptabel sein."
    },
    {
        "id": "b2-fvg-25",
        "level": "B2",
        "category": "Nomen-Verb-Verbindungen (FVG)",
        "title": "FVG: zur Sprache bringen vs. zur Sprache kommen",
        "rule": "'etwas zur Sprache bringen' ist aktiv ('ein Thema ansprechen / erwähnen'). 'zur Sprache kommen' ist passivisch ('besprochen werden').",
        "formula": "zur Sprache bringen (aktiv) | zur Sprache kommen (passiv)",
        "examples": [
            {"de": "Ich möchte im heutigen Teammeeting das Problem der Überstunden zur Sprache bringen.", "en": "I want to bring up the problem of overtime in today's team meeting.", "breakdown": "zur Sprache bringen = ansprechen"},
            {"de": "In der gestrigen Konferenz kamen viele drängende Fragen zur Sprache.", "en": "In yesterday's conference, many pressing questions were discussed.", "breakdown": "kamen zur Sprache = wurden besprochen"},
            {"de": "Dieses heikle Thema wurde von niemandem zur Sprache gebracht.", "en": "This delicate topic was brought up by no one.", "breakdown": "Passivierung des FVG"},
            {"de": "Finanzielle Engpässe kamen während der Beratung gar nicht zur Sprache.", "en": "Financial bottlenecks were not brought up at all during the consultation.", "breakdown": "kamen... zur Sprache"}
        ],
        "takeaway": "bringen = jemand spricht es an; kommen = es wird thematisiert."
    },
    {
        "id": "b2-fvg-26",
        "level": "B2",
        "category": "Nomen-Verb-Verbindungen (FVG)",
        "title": "FVG: Rücksicht nehmen auf (+ Akk) (berücksichtigen)",
        "rule": "'Rücksicht nehmen auf' bedeutet 'die Bedürfnisse oder Gefühle anderer schonend beachten' (to be considerate of).",
        "formula": "Rücksicht nehmen auf + Akkusativ",
        "examples": [
            {"de": "Autofahrer müssen besondere Rücksicht auf spielende Kinder nehmen.", "en": "Drivers must take special consideration of playing children.", "breakdown": "Rücksicht nehmen auf + Akkusativ"},
            {"de": "Im Großraumbüro nehmen alle Kollegen aufeinander Rücksicht.", "en": "In the open-plan office, all colleagues are considerate of one another.", "breakdown": "Rücksicht nehmen"},
            {"de": "Wir müssen auf die Wünsche unserer älteren Kunden Rücksicht nehmen.", "en": "We must take our elderly clients' wishes into consideration.", "breakdown": "Rücksicht auf + Akkusativ"},
            {"de": "Er handelte rücksichtslos, ohne Rücksicht auf die Konsequenzen zu nehmen.", "en": "He acted recklessly without taking consideration of the consequences.", "breakdown": "ohne Rücksicht... zu nehmen"}
        ],
        "takeaway": "Rücksicht nehmen auf + Akkusativ = rücksichtsvoll sein."
    },
    {
        "id": "b2-fvg-27",
        "level": "B2",
        "category": "Nomen-Verb-Verbindungen (FVG)",
        "title": "FVG: Kritik üben an (+ Dat) vs. auf Kritik stoßen",
        "rule": "'Kritik üben an' bedeutet aktiv 'jemanden oder etwas kritisieren'. Dagegen bedeutet 'auf Kritik stoßen', dass der Sprecher oder Plan selbst kritisiert wird (passivisch).",
        "formula": "Kritik üben an + Dat (aktiv kritisieren) | auf Kritik stoßen (kritisiert werden)",
        "examples": [
            {"de": "Die Medien übten scharfe Kritik an den Plänen der Regierung.", "en": "The media leveled sharp criticism at government plans.", "breakdown": "Kritik üben an + Dativ = kritisieren"},
            {"de": "Die geplante Steuererhöhung stieß in der Bevölkerung auf heftige Kritik.", "en": "The planned tax increase met with fierce criticism among the populace.", "breakdown": "auf Kritik stoßen = wurde kritisiert"},
            {"de": "Der Trainer übte nach dem Spiel konstruktive Kritik an der Abwehrleistung.", "en": "The coach leveled constructive criticism at the defense performance after the match.", "breakdown": "Kritik üben an"},
            {"de": "Sein unüberlegter Vorstoß stieß überall auf Ablehnung.", "en": "His ill-considered advance met with rejection everywhere.", "breakdown": "auf Ablehnung stoßen"}
        ],
        "takeaway": "Kritik üben an = aktiv tadeln; auf Kritik stoßen = getadelt werden."
    },
    {
        "id": "b2-fvg-28",
        "level": "B2",
        "category": "Nomen-Verb-Verbindungen (FVG)",
        "title": "FVG: Verantwortung übernehmen / tragen für (+ Akk)",
        "rule": "'die Verantwortung übernehmen für' bedeutet 'die Haftung oder Führung übernehmen'. 'Verantwortung tragen' drückt den andauernden Zustand aus.",
        "formula": "Verantwortung übernehmen / tragen für + Akkusativ",
        "examples": [
            {"de": "Die Projektleiterin übernimmt die volle Verantwortung für das Gelingen.", "en": "The project manager assumes full responsibility for the success.", "breakdown": "Verantwortung übernehmen für + Akkusativ"},
            {"de": "Wer trägt die Verantwortung für die katastrophale Verzögerung?", "en": "Who bears the responsibility for the catastrophic delay?", "breakdown": "Verantwortung tragen für"},
            {"de": "Er war bereit, Verantwortung für sein Fehlverhalten zu übernehmen.", "en": "He was willing to take responsibility for his misconduct.", "breakdown": "Verantwortung übernehmen"},
            {"de": "Führungskräfte tragen eine hohe gesellschaftliche Verantwortung.", "en": "Executives bear high social responsibility.", "breakdown": "Verantwortung tragen"}
        ],
        "takeaway": "Verantwortung übernehmen = zuständig werden; Verantwortung tragen = zuständig sein."
    },
    {
        "id": "b2-fvg-29",
        "level": "B2",
        "category": "Nomen-Verb-Verbindungen (FVG)",
        "title": "FVG: zur Kenntnis nehmen (wahrnehmen/registrieren)",
        "rule": "'etwas zur Kenntnis nehmen' ist eine formelle Redewendung für 'eine Information registrieren / beachten / wahrnehmen' (to take note of / acknowledge).",
        "formula": "etwas (Akk) zur Kenntnis nehmen",
        "examples": [
            {"de": "Ich habe Ihr Schreiben aufmerksam gelesen und zur Kenntnis genommen.", "en": "I read your letter attentively and took note of it.", "breakdown": "zur Kenntnis genommen = registriert"},
            {"de": "Die Geschäftsführung nahm die Warnungen des Betriebsrats zur Kenntnis.", "en": "Management took note of the works council's warnings.", "breakdown": "zur Kenntnis nehmen"},
            {"de": "Wir müssen diese neuen rechtlichen Vorgaben zur Kenntnis nehmen.", "en": "We must take note of these new statutory requirements.", "breakdown": "zur Kenntnis nehmen"},
            {"de": "Bitte nehmen Sie zur Kenntnis, dass unser Büro freitags früher schließt.", "en": "Please take note that our office closes earlier on Fridays.", "breakdown": "zur Kenntnis nehmen, dass..."}
        ],
        "takeaway": "Formelle Korrespondenz: 'Ich habe Ihre Nachricht zur Kenntnis genommen'."
    },
    {
        "id": "b2-fvg-30",
        "level": "B2",
        "category": "Nomen-Verb-Verbindungen (FVG)",
        "title": "FVG: in Anspruch nehmen (nutzen / beanspruchen)",
        "rule": "'etwas in Anspruch nehmen' bedeutet 'eine Dienstleistung oder ein Recht beanspruchen/nutzen' oder 'Zeit/Kraft kosten'.",
        "formula": "etwas (Akk) in Anspruch nehmen",
        "examples": [
            {"de": "Viele Berliner Startups nehmen professionelle Rechtsberatung in Anspruch.", "en": "Many Berlin startups take advantage of professional legal counsel.", "breakdown": "in Anspruch nehmen = nutzen / beanspruchen"},
            {"de": "Die detaillierte Ausarbeitung des Antrags nimmt viel Zeit in Anspruch.", "en": "The detailed preparation of the application requires a lot of time.", "breakdown": "Zeit in Anspruch nehmen = Zeit kosten"},
            {"de": "Sie können das Rückgaberecht innerhalb von 14 Tagen in Anspruch nehmen.", "en": "You can exercise the right of return within 14 days.", "breakdown": "ein Recht wahrnehmen"},
            {"de": "Das Projekt nahm all unsere Ressourcen voll in Anspruch.", "en": "The project taxed all our resources to the full.", "breakdown": "beanspruchen"}
        ],
        "takeaway": "in Anspruch nehmen = nutzen (Beratung) oder beanspruchen (Zeit/Geduld)."
    },

    # 31-45: Subjektive Bedeutung der Modalverben
    {
        "id": "b2-mod-31",
        "level": "B2",
        "category": "Subjektive Modalverben (Epistemischer Gebrauch)",
        "title": "Subjektive Modalverben: Übersicht über die Wahrscheinlichkeitsgrade",
        "rule": "Modalverben können objektiv (Fähigkeit, Pflicht, Erlaubnis) oder subjektiv (Vermutung des Sprechers über einen Sachverhalt) verwendet werden. Grade: müssen (~95% Sicherheit), dürfte (~75% hohe Wahrscheinlichkeit), können/könnte (~50% Möglichkeit), mag (~50% Einräumung).",
        "formula": "müssen (95%) > dürfte (75%) > können / könnte (50%) > mögen (Einräumung)",
        "examples": [
            {"de": "Das Licht im Büro brennt noch; die Chefin muss noch arbeiten.", "en": "The light in the office is still on; the boss must still be working.", "breakdown": "müssen = fast 100% sicher"},
            {"de": "Der Zug dürfte in wenigen Minuten eintreffen.", "en": "The train should arrive in a few minutes.", "breakdown": "dürfte = sehr wahrscheinlich"},
            {"de": "Er könnte den Termin vergessen haben.", "en": "He could have forgotten the appointment.", "breakdown": "könnte = möglich"},
            {"de": "Das mag stimmen, aber es hilft uns jetzt nicht weiter.", "en": "That may be true, but it doesn't help us now.", "breakdown": "mag = Einräumung (Zugegeben, dass...)"}
        ],
        "takeaway": "Subjektive Modalverben drücken den Grad der Gewissheit des Sprechers aus."
    },
    {
        "id": "b2-mod-32",
        "level": "B2",
        "category": "Subjektive Modalverben (Epistemischer Gebrauch)",
        "title": "Subjektives 'müssen': Höchste Gewissheit (~95-100%)",
        "rule": "Subjektives 'müssen' drückt aus, dass eine Schlussfolgerung zwingend logisch ist ('es gibt keine andere Erklärung').",
        "formula": "Subjekt + muss + ... + Infinitiv (Präsens) / Infinitiv Perfekt (Vergangenheit)",
        "examples": [
            {"de": "Niemand öffnet die Tür; sie müssen im Urlaub sein.", "en": "Nobody opens the door; they must be on vacation.", "breakdown": "müssen sein = fast sicher"},
            {"de": "Er zittert am ganzen Körper; ihm muss furchtbar kalt sein.", "en": "He is shivering all over; he must be terribly cold.", "breakdown": "muss sein = logischer Schluss"},
            {"de": "Die Straße ist nass; es muss vor Kurzem geregnet haben.", "en": "The street is wet; it must have rained recently.", "breakdown": "muss geregnet haben (Vergangenheit mit Infinitiv Perfekt)"},
            {"de": "Sie weiß alles über das Projekt; sie muss die Unterlagen genau gelesen haben.", "en": "She knows everything about the project; she must have read the files carefully.", "breakdown": "muss gelesen haben"}
        ],
        "takeaway": "Subjektives müssen = logische Schlussfolgerung ('Es kann gar nicht anders sein')."
    },
    {
        "id": "b2-mod-33",
        "level": "B2",
        "category": "Subjektive Modalverben (Epistemischer Gebrauch)",
        "title": "Subjektives 'dürfte': Hohe Wahrscheinlichkeit (~75%)",
        "rule": "'dürfte' (immer im Konjunktiv II!) drückt aus, dass der Sprecher eine Annahme für sehr wahrscheinlich hält, ohne sie absolut garantieren zu können.",
        "formula": "Subjekt + dürfte + ... + Infinitiv",
        "examples": [
            {"de": "Nach dieser überzeugenden Präsentation dürfte er die Stelle bekommen.", "en": "After this convincing presentation, he ought to get the job.", "breakdown": "dürfte bekommen = sehr wahrscheinlich"},
            {"de": "Die Reparatur des Autos dürfte etwa 300 Euro kosten.", "en": "The car repair is likely to cost about 300 euros.", "breakdown": "dürfte kosten = geschätzte Wahrscheinlichkeit"},
            {"de": "Sie dürften inzwischen am Flughafen angekommen sein.", "en": "They are likely to have arrived at the airport by now.", "breakdown": "dürften angekommen sein (Vergangenheit)"},
            {"de": "Das Wetter dürfte sich am Wochenende wieder beruhigen.", "en": "The weather should calm down again over the weekend.", "breakdown": "dürfte sich beruhigen"}
        ],
        "takeaway": "'dürfte' steht immer im Konjunktiv II und bedeutet 'sehr wahrscheinlich'."
    },
    {
        "id": "b2-mod-34",
        "level": "B2",
        "category": "Subjektive Modalverben (Epistemischer Gebrauch)",
        "title": "Subjektives 'können / könnte': Ungewisse Möglichkeit (~50%)",
        "rule": "'können' (oder vorsichtiger 'könnte') drückt eine bloße Möglichkeit oder Spekulation aus ('vielleicht / es ist möglich').",
        "formula": "kann / könnte + ... + Infinitiv",
        "examples": [
            {"de": "Wo ist mein Schlüssel? – Er könnte noch im Auto liegen.", "en": "Where is my key? – It could still be in the car.", "breakdown": "könnte liegen = vielleicht liegt er dort"},
            {"de": "Der Flug hat Verspätung; es kann an den Unwettern über den Alpen liegen.", "en": "The flight is delayed; it may be due to storms over the Alps.", "breakdown": "kann liegen = mögliche Erklärung"},
            {"de": "Er könnte den Zug verpasst haben, weil die S-Bahn ausfiel.", "en": "He might have missed the train because the commuter rail was cancelled.", "breakdown": "könnte verpasst haben (Vergangenheit)"},
            {"de": "Diese Entscheidung könnte schwerwiegende Folgen für das Unternehmen haben.", "en": "This decision could have severe consequences for the enterprise.", "breakdown": "könnte haben"}
        ],
        "takeaway": "könnte = es ist möglich, aber keineswegs sicher (vielleicht)."
    },
    {
        "id": "b2-mod-35",
        "level": "B2",
        "category": "Subjektive Modalverben (Epistemischer Gebrauch)",
        "title": "Subjektives 'wollen': Eigene Behauptung (Distanzierung des Sprechers)",
        "rule": "Subjektives 'wollen' drückt aus, dass eine Person etwas über SICH SELBST behauptet, der Sprecher dieser Aussage jedoch misstraut oder skeptisch gegenübersteht ('Er behauptet, dass...').",
        "formula": "Subjekt + will + ... + Infinitiv Perfekt / Präsens",
        "examples": [
            {"de": "Der Angeklagte will von dem Schwarzgeldkonto nichts gewusst haben.", "en": "The defendant claims to have known nothing of the slush fund account.", "breakdown": "will gewusst haben = behauptet über sich, man glaubt es ihm aber nicht"},
            {"de": "Er will mit bekannten Hollywood-Stars befreundet sein.", "en": "He claims to be friends with well-known Hollywood stars.", "breakdown": "will befreundet sein = behauptet er selbst"},
            {"de": "Sie will die Lösung des Problems als Erste entdeckt haben.", "en": "She claims to have been the first to discover the solution.", "breakdown": "will entdeckt haben"},
            {"de": "Der Politiker will die E-Mail nie erhalten haben.", "en": "The politician claims never to have received the email.", "breakdown": "will erhalten haben"}
        ],
        "takeaway": "Subjektives wollen = Selbstbehauptung mit Skepsis ('Er behauptet, er habe...')."
    },
    {
        "id": "b2-mod-36",
        "level": "B2",
        "category": "Subjektive Modalverben (Epistemischer Gebrauch)",
        "title": "Subjektives 'sollen': Fremde Behauptung / Gerücht ('Man sagt, dass...')",
        "rule": "Subjektives 'sollen' gibt ein Gerücht, Hörensagen oder fremde Berichte wieder ('Man behauptet / Angeblich / Es heißt, dass...'). Der Sprecher distanziert sich von der Wahrheit.",
        "formula": "Subjekt + soll + ... + Infinitiv (Präsens oder Perfekt)",
        "examples": [
            {"de": "Das neue Restaurant am Ku'damm soll hervorragende Pasta servieren.", "en": "The new restaurant on Ku'damm is said to serve outstanding pasta.", "breakdown": "soll servieren = man sagt, es serviert"},
            {"de": "Die Schauspielerin soll sich von ihrem Partner getrennt haben.", "en": "The actress is said to have parted from her partner.", "breakdown": "soll getrennt haben = Gerücht in der Presse"},
            {"de": "Der Vorstandsvorsitzende soll bald zurücktreten.", "en": "The CEO is rumored to step down soon.", "breakdown": "soll zurücktreten = Gerücht"},
            {"de": "In diesem alten Schloss soll es angeblich spuken.", "en": "This old castle is allegedly said to be haunted.", "breakdown": "soll spuken"}
        ],
        "takeaway": "Subjektives sollen = Gerücht / Hörensagen ('Man sagt, dass... / He is said to...')."
    },
    {
        "id": "b2-mod-37",
        "level": "B2",
        "category": "Subjektive Modalverben (Epistemischer Gebrauch)",
        "title": "Subjektives 'mögen': Konzessive Einräumung ('Das mag sein, aber...')",
        "rule": "Subjektives 'mögen' räumt eine Tatsache oder Meinung ein, schränkt sie aber im darauffolgenden Hauptsatz sogleich ein ('Zugegeben, dass... aber...').",
        "formula": "Das mag [Adjektiv / Verb] sein, aber...",
        "examples": [
            {"de": "Das mag theoretisch richtig sein, aber in der Praxis ist es unbrauchbar.", "en": "That may be theoretically correct, but in practice it is unusable.", "breakdown": "mag richtig sein = ich räume es ein, aber..."},
            {"de": "Er mag ein begabter Programmierer sein, doch ihm fehlt jede Teamfähigkeit.", "en": "He may be a gifted programmer, yet he lacks all teamwork skills.", "breakdown": "mag sein, doch..."},
            {"de": "Das neue Modell mag sparsamer sein, aber es ist viel zu teuer.", "en": "The new model may be more economical, but it is far too expensive.", "breakdown": "mag sparsamer sein"},
            {"de": "Sie mag Recht haben, trotzdem gefällt mir ihr Ton nicht.", "en": "She may be right; nevertheless, I dislike her tone.", "breakdown": "mag Recht haben"}
        ],
        "takeaway": "Subjektives mögen = Zugeständnis mit anschließendem Gegenargument ('may be, but')."
    },
    {
        "id": "b2-mod-38",
        "level": "B2",
        "category": "Subjektive Modalverben (Epistemischer Gebrauch)",
        "title": "Modalverben mit Infinitiv Perfekt: Vermutung über Vergangenes",
        "rule": "Bezieht sich eine subjektive Vermutung auf ein vergangenes Ereignis, wird das Modalverb im Präsens (oder Konjunktiv II) mit dem Infinitiv Perfekt (Partizip II + haben/sein) kombiniert.",
        "formula": "Modalverb (Präsens/K II) + Partizip II + haben / sein",
        "examples": [
            {"de": "Er muss den Bus verpasst haben, sonst wäre er schon hier.", "en": "He must have missed the bus, otherwise he would already be here.", "breakdown": "muss verpasst haben = sichere Vermutung über Vergangenes"},
            {"de": "Sie dürfte gestern spät eingeschlafen sein.", "en": "She is likely to have fallen asleep late yesterday.", "breakdown": "dürfte eingeschlafen sein (mit sein)"},
            {"de": "Der Einbrecher könnte durch das Kellerfenster eingedrungen sein.", "en": "The burglar could have penetrated through the basement window.", "breakdown": "könnte eingedrungen sein"},
            {"de": "Er will den Brief bereits gestern abgeschickt haben.", "en": "He claims to have sent the letter already yesterday.", "breakdown": "will abgeschickt haben"}
        ],
        "takeaway": "Vermutung über Vergangenheit: Modalverb bleibt vorne im Präsens, hinten steht 'Partizip II + haben/sein'."
    },

    # 39-55: Nominalstil vs. Verbalstil (Nominalisierung)
    {
        "id": "b2-nom-39",
        "level": "B2",
        "category": "Nominalstil vs. Verbalstil",
        "title": "Nominalstil vs. Verbalstil: Prinzip und Stilebenen",
        "rule": "Der Verbalstil nutzt Nebensätze mit finiten Verben (lebendig, erzählend, gesprochene Sprache). Der Nominalstil komprimiert diese Nebensätze in Präpositionalphrasen mit Nomen (verdichtet, formell, Wissenschafts- und Behördensprache).",
        "formula": "Verbalstil (Nebensatz: weil er krank ist) <-> Nominalstil (Präpositionalphrase: wegen seiner Krankheit)",
        "examples": [
            {"de": "Verbal: Weil die Mieten stark steigen, ziehen viele Menschen an den Stadtrand.", "en": "Verbal: Because rents are rising sharply, many people move to the outskirts.", "breakdown": "Nebensatz mit weil und finite Verb steigen"},
            {"de": "Nominal: Wegen des starken Mietanstiegs ziehen viele Menschen an den Stadtrand.", "en": "Nominal: Due to the sharp rise in rents, many people move to the outskirts.", "breakdown": "Präposition wegen + Genitiv des Nomen Anstieg"},
            {"de": "Verbal: Als der Zug ankam, begannen die Passagiere auszusteigen.", "en": "Verbal: When the train arrived, passengers began to alight.", "breakdown": "Temporalsatz mit als"},
            {"de": "Nominal: Bei der Ankunft des Zuges begannen die Passagiere auszusteigen.", "en": "Nominal: Upon the arrival of the train, passengers began to alight.", "breakdown": "Präposition bei + Nomen Ankunft"}
        ],
        "takeaway": "Nominalstil ersetzt Nebensatz durch [Präposition + Nomen im Genitiv/Dativ]."
    },
    {
        "id": "b2-nom-40",
        "level": "B2",
        "category": "Nominalstil vs. Verbalstil",
        "title": "Kausale Transformation: weil / da -> wegen / aufgrund",
        "rule": "Kausalsätze mit 'weil' oder 'da' werden im Nominalstil mit den Genitivpräpositionen 'wegen', 'aufgrund' oder 'infolge' nominalisiert. Das Verb wird zum Nomen, das Adverb zum Adjektiv.",
        "formula": "weil [Subjekt] [adverb] [verb] -> wegen / aufgrund + [Genitivartikel] + [Adjektiv] + [Nomen]",
        "examples": [
            {"de": "Verbal: Weil der Zug sich erheblich verspätete, verpassten wir den Anschluss.", "en": "Verbal: Because the train was significantly delayed, we missed the connection.", "breakdown": "weil... sich verspätete"},
            {"de": "Nominal: Wegen der erheblichen Zugverspätung verpassten wir den Anschluss.", "en": "Nominal: Due to the significant train delay, we missed the connection.", "breakdown": "wegen + Genitiv: der erheblichen Zugverspätung"},
            {"de": "Verbal: Da das Budget unerwartet gekürzt wurde, stoppte man das Vorhaben.", "en": "Verbal: Since the budget was unexpectedly cut, the project was stopped.", "breakdown": "da... gekürzt wurde"},
            {"de": "Nominal: Aufgrund der unerwarteten Budgetkürzung stoppte man das Vorhaben.", "en": "Nominal: Due to the unexpected budget cut, the project was stopped.", "breakdown": "aufgrund + Genitiv"}
        ],
        "takeaway": "weil + Verb -> wegen / aufgrund + Nomen im Genitiv."
    },
    {
        "id": "b2-nom-41",
        "level": "B2",
        "category": "Nominalstil vs. Verbalstil",
        "title": "Temporale Transformation: wenn / als -> bei (+ Dativ)",
        "rule": "Gleichzeitige Temporalsätze mit 'wenn' oder 'als' verwandeln sich im Nominalstil in 'bei + Dativ'.",
        "formula": "wenn / als + Satz -> bei + Dativ des Nomens",
        "examples": [
            {"de": "Verbal: Wenn Sie das Dokument unterschreiben, prüfen Sie alle Klauseln.", "en": "Verbal: When you sign the document, check all clauses.", "breakdown": "wenn... unterschreiben"},
            {"de": "Nominal: Bei der Unterschrift des Dokuments prüfen Sie alle Klauseln.", "en": "Nominal: Upon signing the document, check all clauses.", "breakdown": "bei + Dativ: bei der Unterschrift"},
            {"de": "Verbal: Als die Delegation das Werk besichtigte, kam es zu Protesten.", "en": "Verbal: When the delegation inspected the plant, protests occurred.", "breakdown": "als... besichtigte"},
            {"de": "Nominal: Bei der Werksbesichtigung der Delegation kam es zu Protesten.", "en": "Nominal: During the plant inspection by the delegation, protests occurred.", "breakdown": "bei der Werksbesichtigung"}
        ],
        "takeaway": "wenn/als + Verb -> bei + Nomen im Dativ: beim Essen, bei der Ankunft."
    },
    {
        "id": "b2-nom-42",
        "level": "B2",
        "category": "Nominalstil vs. Verbalstil",
        "title": "Temporale Transformation: nachdem -> nach (+ Dativ)",
        "rule": "Vorzeitige Temporalsätze mit 'nachdem' werden im Nominalstil durch die Präposition 'nach + Dativ' wiedergegeben.",
        "formula": "nachdem + Satz -> nach + Dativ des Nomens",
        "examples": [
            {"de": "Verbal: Nachdem der Vertrag unterzeichnet worden war, stießen alle an.", "en": "Verbal: After the contract had been signed, everyone clinked glasses.", "breakdown": "nachdem... unterzeichnet worden war"},
            {"de": "Nominal: Nach der Unterzeichnung des Vertrags stießen alle an.", "en": "Nominal: After the signing of the contract, everyone clinked glasses.", "breakdown": "nach + Dativ: nach der Unterzeichnung"},
            {"de": "Verbal: Nachdem die Konferenz beendet war, gab es ein festliches Abendessen.", "en": "Verbal: After the conference had ended, there was a festive dinner.", "breakdown": "nachdem... beendet war"},
            {"de": "Nominal: Nach Beendigung der Konferenz gab es ein festliches Abendessen.", "en": "Nominal: After conclusion of the conference, there was a festive dinner.", "breakdown": "nach Beendigung"}
        ],
        "takeaway": "nachdem + Verb -> nach + Nomen im Dativ."
    },
    {
        "id": "b2-nom-43",
        "level": "B2",
        "category": "Nominalstil vs. Verbalstil",
        "title": "Temporale Transformation: bevor -> vor (+ Dativ)",
        "rule": "Nachzeitige Temporalsätze mit 'bevor' oder 'ehe' werden im Nominalstil durch die Präposition 'vor + Dativ' ersetzt.",
        "formula": "bevor + Satz -> vor + Dativ des Nomens",
        "examples": [
            {"de": "Verbal: Bevor das Flugzeug startete, überprüften die Techniker die Triebwerke.", "en": "Verbal: Before the aircraft took off, technicians checked the engines.", "breakdown": "bevor... startete"},
            {"de": "Nominal: Vor dem Start des Flugzeugs überprüften die Techniker die Triebwerke.", "en": "Nominal: Prior to takeoff of the aircraft, technicians checked the engines.", "breakdown": "vor + Dativ: vor dem Start"},
            {"de": "Verbal: Bevor die Verhandlung begann, sprachen die Anwälte miteinander.", "en": "Verbal: Before the trial began, the attorneys spoke with one another.", "breakdown": "bevor... begann"},
            {"de": "Nominal: Vor Beginn der Verhandlung sprachen die Anwälte miteinander.", "en": "Nominal: Prior to the start of the trial, the attorneys spoke with each other.", "breakdown": "vor Beginn"}
        ],
        "takeaway": "bevor + Verb -> vor + Nomen im Dativ."
    },
    {
        "id": "b2-nom-44",
        "level": "B2",
        "category": "Nominalstil vs. Verbalstil",
        "title": "Konditionale Transformation: wenn / falls -> bei / im Falle (+ Genitiv)",
        "rule": "Bedingungssätze mit 'wenn' oder 'falls' werden im Nominalstil durch 'bei + Dativ' oder gehoben durch 'im Falle + Genitiv' ausgedrückt.",
        "formula": "wenn / falls + Satz -> bei + Dat / im Falle + Genitiv",
        "examples": [
            {"de": "Verbal: Falls es zu einem Stromausfall kommt, schaltet sich der Notstrom ein.", "en": "Verbal: If a power failure occurs, emergency power turns on.", "breakdown": "falls... kommt"},
            {"de": "Nominal: Im Falle eines Stromausfalls schaltet sich der Notstrom ein.", "en": "Nominal: In the event of a power failure, emergency power switches on.", "breakdown": "im Falle + Genitiv: eines Stromausfalls"},
            {"de": "Verbal: Wenn Sie Fragen haben, wenden Sie sich bitte an den Support.", "en": "Verbal: If you have questions, please turn to support.", "breakdown": "wenn Sie Fragen haben"},
            {"de": "Nominal: Bei Fragen wenden Sie sich bitte an den Support.", "en": "Nominal: In case of questions, please turn to support.", "breakdown": "bei + Dativ: bei Fragen"}
        ],
        "takeaway": "wenn/falls -> bei + Dativ / im Falle + Genitiv."
    },
    {
        "id": "b2-nom-45",
        "level": "B2",
        "category": "Nominalstil vs. Verbalstil",
        "title": "Konzessive Transformation: obwohl -> trotz / ungeachtet (+ Genitiv)",
        "rule": "Konzessivsätze mit 'obwohl' verwandeln sich im Nominalstil in Phrasen mit 'trotz + Genitiv' oder noch gehobener 'ungeachtet + Genitiv'.",
        "formula": "obwohl + Satz -> trotz / ungeachtet + Genitiv des Nomens",
        "examples": [
            {"de": "Verbal: Obwohl es heftig stürmte, legte die Fähre pünktlich ab.", "en": "Verbal: Although it stormed violently, the ferry departed on time.", "breakdown": "obwohl es heftig stürmte"},
            {"de": "Nominal: Trotz des heftigen Sturms legte die Fähre pünktlich ab.", "en": "Nominal: Despite the fierce storm, the ferry departed on time.", "breakdown": "trotz + Genitiv: des heftigen Sturms"},
            {"de": "Verbal: Obwohl die Proteste anhielten, wurde das Bauvorhaben fortgesetzt.", "en": "Verbal: Although protests persisted, the building project was continued.", "breakdown": "obwohl... anhielten"},
            {"de": "Nominal: Ungeachtet der anhaltenden Proteste wurde das Bauvorhaben fortgesetzt.", "en": "Nominal: Regardless of persisting protests, the construction project was continued.", "breakdown": "ungeachtet + Genitiv"}
        ],
        "takeaway": "obwohl + Verb -> trotz / ungeachtet + Nomen im Genitiv."
    },
    {
        "id": "b2-nom-46",
        "level": "B2",
        "category": "Nominalstil vs. Verbalstil",
        "title": "Finale Transformation: um... zu / damit -> zu / zwecks (+ Genitiv)",
        "rule": "Finalsätze (um... zu, damit) werden im Nominalstil durch 'zu + Dativ' (zur Verbesserung), 'für + Akkusativ' oder formell durch 'zwecks + Genitiv' wiedergegeben.",
        "formula": "damit / um... zu -> zu + Dativ / zwecks + Genitiv",
        "examples": [
            {"de": "Verbal: Wir testen die Software gründlich, um Fehler frühzeitig zu entdecken.", "en": "Verbal: We test the software thoroughly in order to detect bugs early.", "breakdown": "um... zu entdecken"},
            {"de": "Nominal: Zur frühzeitigen Entdeckung von Fehlern testen wir die Software gründlich.", "en": "Nominal: For early detection of bugs, we test the software thoroughly.", "breakdown": "zu + Dativ: zur Entdeckung"},
            {"de": "Verbal: Man richtete Straßensperren ein, damit die Sicherheit gewährleistet wird.", "en": "Verbal: Roadblocks were established so that security is ensured.", "breakdown": "damit... gewährleistet wird"},
            {"de": "Nominal: Zwecks Gewährleistung der Sicherheit richtete man Straßensperren ein.", "en": "Nominal: For the purpose of guaranteeing safety, roadblocks were set up.", "breakdown": "zwecks + Genitiv: der Gewährleistung"}
        ],
        "takeaway": "um... zu / damit -> zur + Nomen / zwecks + Genitiv."
    },
    {
        "id": "b2-nom-47",
        "level": "B2",
        "category": "Nominalstil vs. Verbalstil",
        "title": "Modale Transformation: indem -> durch / mittels (+ Genitiv)",
        "rule": "Modalsätze mit 'indem' oder 'dadurch, dass' verwandeln sich im Nominalstil in Präpositionalphrasen mit 'durch + Akkusativ' oder formell 'mittels + Genitiv'.",
        "formula": "indem -> durch + Akkusativ / mittels + Genitiv",
        "examples": [
            {"de": "Verbal: Das Team sparte Zeit, indem es repetitive Prozesse automatisierte.", "en": "Verbal: The team saved time by automating repetitive processes.", "breakdown": "indem... automatisierte"},
            {"de": "Nominal: Durch die Automatisierung repetitiver Prozesse sparte das Team Zeit.", "en": "Nominal: Through the automation of repetitive processes, the team saved time.", "breakdown": "durch + Akkusativ: durch die Automatisierung"},
            {"de": "Verbal: Man verifizierte die Identität, indem man biometrische Daten scannte.", "en": "Verbal: Identity was verified by scanning biometric data.", "breakdown": "indem... scannte"},
            {"de": "Nominal: Mittels biometrischen Scans verifizierte man die Identität.", "en": "Nominal: By means of biometric scanning, identity was verified.", "breakdown": "mittels + Genitiv"}
        ],
        "takeaway": "indem + Verb -> durch + Akkusativ / mittels + Genitiv."
    },
    {
        "id": "b2-nom-48",
        "level": "B2",
        "category": "Nominalstil vs. Verbalstil",
        "title": "Suffixe zur Nominalisierung: -ung, -heit, -keit, -schaft, -tät",
        "rule": "Viele Verben und Adjektive werden durch typische Suffixe zu femininen Nomen (Artikel IMMER 'die'): -ung (erklären -> die Erklärung), -heit (gesund -> die Gesundheit), -keit (pünktlich -> die Pünktlichkeit), -schaft (bereit -> die Bereitschaft), -tät (aktiv -> die Aktivität).",
        "formula": "-ung, -heit, -keit, -schaft, -tät = IMMER DIE (Feminin!)",
        "examples": [
            {"de": "Die Beschleunigung des Prozesses erfordert modernere Maschinen.", "en": "The acceleration of the process requires more modern machines.", "breakdown": "beschleunigen -> die Beschleunigung"},
            {"de": "Zuverlässigkeit und Pünktlichkeit sind im Berufsleben unabdingbar.", "en": "Reliability and punctuality are indispensable in professional life.", "breakdown": "die Zuverlässigkeit / die Pünktlichkeit (-keit)"},
            {"de": "Die Bereitschaft zur Veränderung zeichnet innovative Firmen aus.", "en": "Willingness to change distinguishes innovative firms.", "breakdown": "die Bereitschaft (-schaft)"},
            {"de": "Die Flexibilität der Arbeitszeiten wird von den Angestellten geschätzt.", "en": "The flexibility of working hours is valued by employees.", "breakdown": "die Flexibilität (-tät)"}
        ],
        "takeaway": "Alle Nomen auf -ung, -heit, -keit, -schaft, -tät sind ausnahmslos feminin (die)."
    },

    # 49-65: Partizipialkonstruktionen & Erweiterte Attribute
    {
        "id": "b2-part-49",
        "level": "B2",
        "category": "Partizipialkonstruktionen & Erweiterte Attribute",
        "title": "Erweitertes Partizip I als Linksattribut (die stetig wachsende Stadt)",
        "rule": "Wird ein Partizip I mit Adverbien oder Objekten erweitert und vor das Nomen gestellt, entsteht ein erweitertes Partizipialattribut. Es entspricht einem aktiven Relativsatz im Präsens.",
        "formula": "Artikel + [Erweiterungen + Partizip I + Adjektivendung] + Nomen",
        "examples": [
            {"de": "Die rasant wachsende Berliner Tech-Szene zieht internationale Talente an.", "en": "The rapidly growing Berlin tech scene attracts international talent.", "breakdown": "rasant wachsende = die Tech-Szene, die rasant wächst"},
            {"de": "Wir bewundern die unermüdlich für den Klimaschutz kämpfenden Aktivisten.", "en": "We admire the activists fighting tirelessly for climate protection.", "breakdown": "die Aktivisten, die unermüdlich kämpfen"},
            {"de": "Der seit vielen Jahren in Deutschland lebende Autor veröffentlicht ein neues Buch.", "en": "The author living in Germany for many years is publishing a new book.", "breakdown": "der Autor, der seit vielen Jahren lebt"},
            {"de": "Das stark nach Rauch riechende Zimmer musste gründlich gelüftet werden.", "en": "The room smelling strongly of smoke had to be aired thoroughly.", "breakdown": "das Zimmer, das stark nach Rauch roch"}
        ],
        "takeaway": "Erweitertes Partizip I = verdichteter aktiver Relativsatz vor dem Substantiv."
    },
    {
        "id": "b2-part-50",
        "level": "B2",
        "category": "Partizipialkonstruktionen & Erweiterte Attribute",
        "title": "Erweitertes Partizip II als Linksattribut (das kürzlich verabschiedete Gesetz)",
        "rule": "Ein erweitertes Partizip II vor dem Nomen fasst einen passiven oder vollendeten Relativsatz zusammen. Das Partizip II erhält die reguläre Adjektivendung.",
        "formula": "Artikel + [Erweiterungen + Partizip II + Adjektivendung] + Nomen",
        "examples": [
            {"de": "Das gestern vom Bundestag beschlossene Gesetz tritt nächsten Monat in Kraft.", "en": "The law passed by the Bundestag yesterday comes into effect next month.", "breakdown": "das Gesetz, das gestern vom Bundestag beschlossen wurde"},
            {"de": "Die von führenden Wissenschaftlern entwickelten Algorithmen arbeiten hochpräzise.", "en": "The algorithms developed by leading scientists operate with high precision.", "breakdown": "die Algorithmen, die entwickelt wurden"},
            {"de": "Er reparierte die durch den Sturm beschädigte Dachrinne.", "en": "He repaired the rain gutter damaged by the storm.", "breakdown": "die Dachrinne, die beschädigt worden war"},
            {"de": "Alle im Voraus bezahlten Tickets können am Einlass digital vorgezeigt werden.", "en": "All tickets paid for in advance can be presented digitally at the entrance.", "breakdown": "die Tickets, die im Voraus bezahlt wurden"}
        ],
        "takeaway": "Erweitertes Partizip II komprimiert Passivsätze zu eleganten Attributen."
    },
    {
        "id": "b2-part-51",
        "level": "B2",
        "category": "Partizipialkonstruktionen & Erweiterte Attribute",
        "title": "Das Gerundiv: Partizip I mit 'zu' (die zu lösenden Aufgaben)",
        "rule": "Wird 'zu' vor ein Partizip I gesetzt und das Wort als Adjektiv dekliniert, entsteht das Gerundiv. Es hat rein passive Bedeutung und drückt eine Notwendigkeit ('muss getan werden') oder Möglichkeit ('kann getan werden') aus.",
        "formula": "Artikel + [zu + Infinitiv + -d + Endung] + Nomen",
        "examples": [
            {"de": "Die bis morgen einzureichenden Dokumente müssen vollständig sein.", "en": "The documents to be submitted by tomorrow must be complete.", "breakdown": "die Dokumente, die eingereicht werden müssen"},
            {"de": "Das ist ein nicht zu unterschätzendes Sicherheitsrisiko für das Netzwerk.", "en": "That is a security risk not to be underestimated for the network.", "breakdown": "ein Risiko, das nicht unterschätzt werden darf/kann"},
            {"de": "Die im Meeting zu besprechenden Themen stehen auf der Agenda.", "en": "The topics to be discussed in the meeting are on the agenda.", "breakdown": "die Themen, die besprochen werden sollen"},
            {"de": "Das schwer zu lösende Rechenrätsel forderte die Mathematiker heraus.", "en": "The math puzzle that was difficult to solve challenged the mathematicians.", "breakdown": "das Rätsel, das schwer gelöst werden konnte"}
        ],
        "takeaway": "Gerundiv: zu + Partizip I = passive Notwendigkeit ('die zu erledigende Arbeit')."
    },
    {
        "id": "b2-part-52",
        "level": "B2",
        "category": "Partizipialkonstruktionen & Erweiterte Attribute",
        "title": "Partizipialsätze als Satzverkürzung (In Berlin angekommen, ...)",
        "rule": "Partizipialgruppen können anstelle von Adverbialsätzen (temporal, kausal) stehen, wenn das Subjekt im Haupt- und Nebensatz IDENTISCH ist. Sie werden durch ein Komma abgetrennt.",
        "formula": "[Partizipialgruppe mit Partizip I/II], + finites Verb + Subjekt...",
        "examples": [
            {"de": "In Berlin angekommen, suchte er sogleich nach einem gemütlichen Café.", "en": "Having arrived in Berlin, he immediately searched for a cozy café.", "breakdown": "Nachdem er in Berlin angekommen war -> In Berlin angekommen"},
            {"de": "Erschöpft von der langen Wanderung, schliefen die Bergsteiger früh ein.", "en": "Exhausted from the long hike, the mountaineers fell asleep early.", "breakdown": "Weil sie erschöpft waren -> Erschöpft von der Wanderung"},
            {"de": "Das Smartphone in der Hand haltend, überquerte der Fußgänger die Straße.", "en": "Holding the smartphone in hand, the pedestrian crossed the street.", "breakdown": "Während er das Smartphone hielt -> haltend"},
            {"de": "Vom Wahlsieg überrascht, bedankte sich die Politikerin bei ihren Wählern.", "en": "Surprised by the election victory, the politician thanked her voters.", "breakdown": "Da sie überrascht war -> Vom Wahlsieg überrascht"}
        ],
        "takeaway": "Subjektgleichheit ist Pflicht bei Partizipialsätzen: 'Angekommen, suchte ER...'"
    },

    # 53-75: Complex Connectors & Prepositions
    {
        "id": "b2-kon-53",
        "level": "B2",
        "category": "Komplexe Konnektoren",
        "title": "Zweiteilige Konnektoren: geschweige denn (Verstärkte Verneinung)",
        "rule": "'geschweige denn' schließt eine noch unwahrscheinlichere Möglichkeit nach einem bereits verneinten Satz kategorisch aus (let alone / not to mention).",
        "formula": "Hauptsatz (mit Negation), geschweige denn + Substantiv / Infinitiv",
        "examples": [
            {"de": "Er hat nicht einmal genug Geld für die Miete, geschweige denn für einen Urlaub.", "en": "He doesn't even have enough money for rent, let alone for a holiday.", "breakdown": "geschweige denn verstärkt die Negation"},
            {"de": "Sie kann kaum ein paar Sätze Deutsch sprechen, geschweige denn einen Vortrag halten.", "en": "She can barely speak a few sentences of German, let alone deliver a lecture.", "breakdown": "geschweige denn für Vortrag"},
            {"de": "Das alte Auto schafft keine hundert Kilometer, geschweige denn die Fahrt nach Italien.", "en": "The old car can't manage a hundred kilometers, let alone the drive to Italy.", "breakdown": "geschweige denn"},
            {"de": "Ich habe keine Zeit zum Frühstücken, geschweige denn zum ausgiebigen Kochen.", "en": "I have no time for breakfast, let alone for elaborate cooking.", "breakdown": "geschweige denn"}
        ],
        "takeaway": "'geschweige denn' steht immer nach einer Negation und bedeutet 'geschweige erst recht nicht'."
    },
    {
        "id": "b2-kon-54",
        "level": "B2",
        "category": "Komplexe Konnektoren",
        "title": "Zweiteilige Konnektoren: nicht dass... sondern (Korrektur einer Fehlannahme)",
        "rule": "'nicht dass... sondern' weist eine vermutete falsche Begründung zurück und stellt die wahre Ursache klar.",
        "formula": "Nicht dass [falsche Annahme], sondern [wahre Ursache]",
        "examples": [
            {"de": "Nicht dass er faul wäre, sondern ihm fehlt im Moment einfach die Orientierung.", "en": "Not that he were lazy, but he simply lacks direction at the moment.", "breakdown": "nicht dass... (oft mit Konjunktiv II) sondern..."},
            {"de": "Nicht dass wir kein Interesse hätten, sondern unser Budget lässt die Investition nicht zu.", "en": "Not that we lacked interest, but our budget doesn't permit the investment.", "breakdown": "Klarstellung"},
            {"de": "Nicht dass die Prüfung zu schwer war, sondern ich hatte mich zu spät vorbereitet.", "en": "Not that the exam was too difficult, but I had prepared too late.", "breakdown": "Indikativ-Variante"},
            {"de": "Nicht dass sie mich beleidigt hätte, aber ihr abweisender Blick tat weh.", "en": "Not that she had insulted me, but her dismissive glance hurt.", "breakdown": "Differenzierung"}
        ],
        "takeaway": "'Nicht dass... sondern' räumt falsche Verdächtigungen elegant aus dem Weg."
    },
    {
        "id": "b2-kon-55",
        "level": "B2",
        "category": "Komplexe Konnektoren",
        "title": "Konzessive Konnektoren: wenngleich / wennschon / obzwar",
        "rule": "'wenngleich', 'wennschon' und 'obzwar' sind gehobene schriftliche Synonyme für 'obwohl'. Sie leiten einen Nebensatz mit finitem Verb am Satzende ein.",
        "formula": "wenngleich / obzwar + Subjekt + ... + Verb",
        "examples": [
            {"de": "Er nahm das Jobangebot an, wenngleich das Gehalt unter seinen Erwartungen lag.", "en": "He accepted the job offer, although the salary lay below his expectations.", "breakdown": "wenngleich = gehobenes obwohl"},
            {"de": "Das Gemälde erzielte einen hohen Preis, obzwar der Künstler zu Lebzeiten verarmt war.", "en": "The painting fetched a high price, although the artist had been impoverished during his lifetime.", "breakdown": "obzwar = literarisches obwohl"},
            {"de": "Die Verhandlungen machten Fortschritte, wenngleich noch viele Details offen sind.", "en": "Negotiations made progress, although many details remain open.", "breakdown": "wenngleich"},
            {"de": "Wennschon die Aufgabe gewaltig erschien, gaben die Forscher niemals auf.", "en": "Even though the task seemed immense, the researchers never gave up.", "breakdown": "wennschon = konzessiv"}
        ],
        "takeaway": "wenngleich / obzwar bereichern gehobene schriftliche Texte als elegante Obwohl-Varianten."
    },
    {
        "id": "b2-kon-56",
        "level": "B2",
        "category": "Komplexe Konnektoren",
        "title": "Restriktive Konnektoren: insofern als / soweit / soviel",
        "rule": "Restriktive Konnektoren schränken die Gültigkeit einer Aussage auf einen bestimmten Rahmen ein (insofar as / as far as). Verb am Satzende.",
        "formula": "insofern (als) / soweit / soviel + Subjekt + ... + Verb",
        "examples": [
            {"de": "Soweit ich weiß, hat das Bürgeramt heute bis 18 Uhr geöffnet.", "en": "As far as I know, the citizens' registration office is open until 6 PM today.", "breakdown": "soweit ich weiß = Einschränkung"},
            {"de": "Das Experiment war erfolgreich, insofern als die Hypothese bestätigt wurde.", "en": "The experiment was successful insofar as the hypothesis was confirmed.", "breakdown": "insofern als"},
            {"de": "Soviel man hört, plant der Konzern umfangreiche Entlassungen.", "en": "As far as one hears, the group plans extensive layoffs.", "breakdown": "soviel man hört"},
            {"de": "Die Software ist stabil, soweit wir das nach den ersten Stresstests beurteilen können.", "en": "The software is stable, as far as we can judge after the initial stress tests.", "breakdown": "soweit wir beurteilen können"}
        ],
        "takeaway": "soweit / soviel / insofern als stecken den vorsichtigen Gültigkeitsbereich einer Aussage ab."
    },
    {
        "id": "b2-kon-57",
        "level": "B2",
        "category": "Komplexe Konnektoren",
        "title": "Proportionale Konnektoren: umso mehr als / je nachdem",
        "rule": "'umso mehr, als' begründet eine Steigerung ('all the more so since'). 'je nachdem, ob/wie' drückt eine Abhängigkeit von variablen Bedingungen aus ('depending on').",
        "formula": "umso mehr als + Nebensatz | je nachdem, ob/wie + Nebensatz",
        "examples": [
            {"de": "Sein Erfolg ist bewundernswert, umso mehr als er ohne fremde Hilfe startete.", "en": "His success is admirable, all the more so since he started without outside help.", "breakdown": "umso mehr als = verstärkende Begründung"},
            {"de": "Wir fahren am Wochenende an die Ostsee, je nachdem, wie das Wetter wird.", "en": "We will travel to the Baltic Sea this weekend, depending on how the weather turns out.", "breakdown": "je nachdem, wie..."},
            {"de": "Die Kosten variieren, je nachdem, welches Hotelpaket Sie wählen.", "en": "Costs vary depending on which hotel package you select.", "breakdown": "je nachdem, welches..."},
            {"de": "Die Kritik wiegt schwer, umso mehr als sie von einem anerkannten Fachmann stammt.", "en": "The criticism carries weight, all the more so as it comes from a recognized expert.", "breakdown": "umso mehr als"}
        ],
        "takeaway": "umso mehr als = 'erst recht weil'; je nachdem = 'abhängig davon'."
    },
    {
        "id": "b2-kon-58",
        "level": "B2",
        "category": "Komplexe Konnektoren",
        "title": "Gehobene Genitivpräpositionen: hinsichtlich, bezüglich, anlässlich",
        "rule": "'hinsichtlich' (regarding / with regard to), 'bezüglich' (concerning) und 'anlässlich' (on the occasion of) sind formelle Präpositionen, die den Genitiv regieren.",
        "formula": "hinsichtlich / bezüglich / anlässlich + Genitiv",
        "examples": [
            {"de": "Hinsichtlich der Datensicherheit bestehen bei den Kunden noch erhebliche Bedenken.", "en": "Regarding data security, considerable concerns still exist among customers.", "breakdown": "hinsichtlich der Datensicherheit (Genitiv feminin)"},
            {"de": "Bezüglich Ihrer Anfrage vom 15. Oktober senden wir Ihnen unser Angebot.", "en": "Concerning your inquiry of October 15th, we are sending you our quotation.", "breakdown": "bezüglich Ihrer Anfrage (Genitiv feminin)"},
            {"de": "Anlässlich des Firmenjubiläums lud der Gründer die gesamte Belegschaft ein.", "en": "On the occasion of the company anniversary, the founder invited the entire workforce.", "breakdown": "anlässlich des Firmenjubiläums (Genitiv neutral)"},
            {"de": "Hinsichtlich der Umsetzbarkeit des Projekts müssen wir noch Rücksprache halten.", "en": "With regard to feasibility of the project, we still need to consult.", "breakdown": "hinsichtlich + Genitiv"}
        ],
        "takeaway": "Formelle Briefe: hinsichtlich, bezüglich und anlässlich verlangen Genitiv."
    },
    {
        "id": "b2-kon-59",
        "level": "B2",
        "category": "Komplexe Konnektoren",
        "title": "Gehobene Genitivpräpositionen: mangels, kraft, zugunsten",
        "rule": "'mangels' (for lack of), 'kraft' (by virtue of) und 'zugunsten' (in favor of) gehören zum juristischen und behördlichen Standardrepertoire mit Genitiv.",
        "formula": "mangels / kraft / zugunsten + Genitiv",
        "examples": [
            {"de": "Das Gerichtsverfahren wurde mangels stichhaltiger Beweise eingestellt.", "en": "The court proceeding was discontinued for lack of solid evidence.", "breakdown": "mangels stichhaltiger Beweise (Genitiv Plural)"},
            {"de": "Kraft seines Amtes erließ der Ministerpräsident eine Eilverordnung.", "en": "By virtue of his office, the prime minister issued an urgent decree.", "breakdown": "kraft seines Amtes (Genitiv neutral)"},
            {"de": "Der ältere Bruder verzichtete zugunsten seiner jüngeren Schwester auf das Erbe.", "en": "The older brother renounced the inheritance in favor of his younger sister.", "breakdown": "zugunsten seiner Schwester (Genitiv feminin)"},
            {"de": "Mangels finanzieller Mittel musste das Theater die Spielzeit verkürzen.", "en": "For lack of financial means, the theater had to shorten the season.", "breakdown": "mangels finanzieller Mittel"}
        ],
        "takeaway": "mangels = aus Mangel an; kraft = durch Vollmacht von; zugunsten = zum Wohl von."
    },
    {
        "id": "b2-kon-60",
        "level": "B2",
        "category": "Komplexe Konnektoren",
        "title": "Gehobene Genitivpräpositionen: anhand, mithilfe, seitens",
        "rule": "'anhand' (by means of / on the basis of), 'mithilfe' (with the help of) und 'seitens' (on the part of) verlangen den Genitiv.",
        "formula": "anhand / mithilfe / seitens + Genitiv",
        "examples": [
            {"de": "Der Dozent veranschaulichte die Theorie anhand anschaulicher Praxisbeispiele.", "en": "The lecturer illustrated the theory by means of vivid practical examples.", "breakdown": "anhand anschaulicher Praxisbeispiele (Genitiv Plural)"},
            {"de": "Mithilfe modernster Satellitentechnik konnte der Waldbrand früh lokalisiert werden.", "en": "With the aid of state-of-the-art satellite technology, the wildfire was localized early.", "breakdown": "mithilfe modernster Satellitentechnik (Genitiv feminin)"},
            {"de": "Seitens der Geschäftsführung gab es keinerlei Einwände gegen den Vorschlag.", "en": "On the part of management, there were no objections whatsoever to the proposal.", "breakdown": "seitens der Geschäftsführung (Genitiv feminin)"},
            {"de": "Wir erklären die Architektur anhand einer schematischen Grafik.", "en": "We explain the architecture on the basis of a schematic graphic.", "breakdown": "anhand einer Grafik"}
        ],
        "takeaway": "anhand, mithilfe, seitens verleihen wissenschaftlichen Texten Präzision."
    },

    # 61-80: Advanced Verb Valency & Prepositions
    {
        "id": "b2-rek-61",
        "level": "B2",
        "category": "Gehobene Verbrektion",
        "title": "Verben mit Präposition: plädieren für vs. appellieren an",
        "rule": "'plädieren für + Akkusativ' bedeutet 'sich nachdrücklich für etwas aussprechen'. 'appellieren an + Akkusativ' bedeutet 'eine eindringliche Mahnung an jemanden richten'.",
        "formula": "plädieren für + Akk | appellieren an + Akk",
        "examples": [
            {"de": "Der Umweltexperte plädiert für einen schnelleren Ausbau des Schienennetzes.", "en": "The environmental expert pleads for faster expansion of the rail network.", "breakdown": "plädieren für + Akkusativ"},
            {"de": "Der Bürgermeister appellierte an den Gemeinsinn der Bürger.", "en": "The mayor appealed to the citizens' sense of community.", "breakdown": "appellieren an + Akkusativ"},
            {"de": "Die Anwältin plädierte vor Gericht auf Freispruch.", "en": "The attorney pleaded in court for acquittal.", "breakdown": "auf Freispruch plädieren (juristisch)"},
            {"de": "Hilfsorganisationen appellieren an die Spendenbereitschaft der Bevölkerung.", "en": "Charities appeal to the population's willingness to donate.", "breakdown": "appellieren an"}
        ],
        "takeaway": "plädieren FÜR eine Sache; appellieren AN eine Person oder Eigenschaft."
    },
    {
        "id": "b2-rek-62",
        "level": "B2",
        "category": "Gehobene Verbrektion",
        "title": "Verben mit Präposition: beharren auf (+ Dat) vs. bestehen auf (+ Dat/Akk)",
        "rule": "'beharren auf + Dativ' bedeutet 'stur und unnachgiebig an einer Meinung festhalten'. 'bestehen auf + Dativ' drückt ein festes Einfordern aus ('Ich bestehe auf meinem Recht').",
        "formula": "beharren auf + Dativ | bestehen auf + Dativ",
        "examples": [
            {"de": "Trotz aller Gegenargumente beharrte der Abteilungsleiter stur auf seiner Position.", "en": "Despite all counter-arguments, the department head stubbornly insisted on his position.", "breakdown": "beharren auf + Dativ"},
            {"de": "Der Kunde bestand auf einer schriftlichen Bestätigung der Reklamation.", "en": "The customer insisted on written confirmation of the complaint.", "breakdown": "bestehen auf + Dativ"},
            {"de": "Wir dürfen nicht starr auf veralteten Prinzipien beharren.", "en": "We must not rigidly insist on outdated principles.", "breakdown": "beharren auf"},
            {"de": "Sie besteht darauf, die Übersetzung selbst zu korrigieren.", "en": "She insists on correcting the translation herself.", "breakdown": "besteht darauf (Pronominaladverb)"}
        ],
        "takeaway": "beharren / bestehen + AUF + Dativ = unnachgiebig fordern/festhalten."
    },
    {
        "id": "b2-rek-63",
        "level": "B2",
        "category": "Gehobene Verbrektion",
        "title": "Verben mit Präposition: resultieren aus (+ Dat) vs. führen zu (+ Dat)",
        "rule": "'resultieren aus + Dativ' benennt die URSACHE von hinten her (Folge <- Ursache). 'führen zu + Dativ' beschreibt die WIRKUNG nach vorne hin (Ursache -> Folge).",
        "formula": "resultieren aus + Dat (Ursache) | führen zu + Dat (Wirkung)",
        "examples": [
            {"de": "Der Schaden resultiert aus einem schwerwiegenden Bedienungsfehler.", "en": "The damage results from a serious operating error.", "breakdown": "resultieren aus + Dativ"},
            {"de": "Die permanente Überlastung führte schließlich zu einem Burnout.", "en": "Permanent overload eventually led to burnout.", "breakdown": "führen zu + Dativ"},
            {"de": "Diese Probleme resultieren größtenteils aus mangelnder Kommunikation.", "en": "These problems result largely from a lack of communication.", "breakdown": "resultieren aus"},
            {"de": "Schlechte Vorbereitung führt fast immer zu schlechten Resultaten.", "en": "Poor preparation almost always leads to poor results.", "breakdown": "führen zu"}
        ],
        "takeaway": "Wirkung resultiert AUS der Ursache; die Ursache führt ZUR Wirkung."
    },
    {
        "id": "b2-rek-64",
        "level": "B2",
        "category": "Gehobene Verbrektion",
        "title": "Verben mit Präposition: anknüpfen an (+ Akk) vs. basieren auf (+ Dat)",
        "rule": "'anknüpfen an + Akkusativ' bedeutet 'eine Verbindung zu einem früheren Thema herstellen'. 'basieren auf + Dativ' bedeutet 'sich auf eine Grundlage stützen'.",
        "formula": "anknüpfen an + Akk | basieren auf + Dat",
        "examples": [
            {"de": "Ich möchte kurz an die Ausführungen meines Vorredners anknüpfen.", "en": "I would like to briefly connect to the remarks of the previous speaker.", "breakdown": "anknüpfen an + Akkusativ"},
            {"de": "Die neue Software basiert auf einem robusten Cloud-Fundament.", "en": "The new software is based on a robust cloud foundation.", "breakdown": "basieren auf + Dativ"},
            {"de": "Der zweite Teil des Buches knüpft nahtlos an die Ereignisse des ersten Bandes an.", "en": "The second part of the book connects seamlessly to events of the first volume.", "breakdown": "anknüpfen an"},
            {"de": "Unsere Prognosen basieren auf den verifizierten Wirtschaftsdaten der Zentralbank.", "en": "Our forecasts are based on verified economic data from the central bank.", "breakdown": "basieren auf"}
        ],
        "takeaway": "anknüpfen AN + Akk (Verbindung aufnehmen); basieren AUF + Dat (Grundlage)."
    },
    {
        "id": "b2-rek-65",
        "level": "B2",
        "category": "Gehobene Verbrektion",
        "title": "Verben mit Präposition: sich abfinden mit (+ Dat) (akzeptieren)",
        "rule": "'sich abfinden mit + Dativ' bedeutet 'eine unangenehme oder unabänderliche Tatsache resigniert oder pragmatisch akzeptieren' (to come to terms with / resign oneself to).",
        "formula": "sich abfinden mit + Dativ",
        "examples": [
            {"de": "Er konnte sich lange nicht mit der schmerzhaften Niederlage abfinden.", "en": "For a long time he could not come to terms with the painful defeat.", "breakdown": "sich abfinden mit + Dativ"},
            {"de": "Wir müssen uns wohl oder übel mit den höheren Rohstoffpreisen abfinden.", "en": "Like it or not, we must come to terms with the higher raw material prices.", "breakdown": "sich abfinden mit"},
            {"de": "Sie fand sich schließlich mit der Versetzung ins andere Team ab.", "en": "She eventually resigned herself to the transfer to the other team.", "breakdown": "fand sich ab mit"},
            {"de": "Niemand sollte sich einfach mit Ungerechtigkeit abfinden.", "en": "Nobody should simply resign themselves to injustice.", "breakdown": "sich abfinden mit"}
        ],
        "takeaway": "sich abfinden mit = sich fügen, etwas Zähneknirschend annehmen."
    },
    {
        "id": "b2-rek-66",
        "level": "B2",
        "category": "Gehobene Verbrektion",
        "title": "Verben mit Präposition: sich distanzieren von (+ Dat)",
        "rule": "'sich distanzieren von + Dativ' drückt eine ausdrückliche Ablehnung oder Trennung von Aussagen, Handlungen oder Personen aus (to distance oneself from).",
        "formula": "sich distanzieren von + Dativ",
        "examples": [
            {"de": "Der Sprecher distanzierte sich ausdrücklich von den radikalen Äußerungen des Autors.", "en": "The spokesperson explicitly distanced himself from the author's radical remarks.", "breakdown": "sich distanzieren von + Dativ"},
            {"de": "Die Parteiführung distanzierte sich geschlossen von diesem Skandal.", "en": "Party leadership distanced itself as one from this scandal.", "breakdown": "sich distanzieren von"},
            {"de": "Wir möchten uns in aller Schärfe von Diskriminierung jeder Art distanzieren.", "en": "We wish to distance ourselves in the sharpest terms from discrimination of any kind.", "breakdown": "sich distanzieren von"},
            {"de": "Er distanzierte sich später von seinen frühen Veröffentlichungen.", "en": "He later distanced himself from his early publications.", "breakdown": "sich distanzieren von"}
        ],
        "takeaway": "sich distanzieren von = klare Grenze zu zweifelhaften Inhalten ziehen."
    },
    {
        "id": "b2-rek-67",
        "level": "B2",
        "category": "Gehobene Verbrektion",
        "title": "Verben mit reinem Genitiv (gedenken, bedürfen, anklagen)",
        "rule": "Einige wenige gehobene und juristische Verben verlangen ein direktes Genitivobjekt OHNE Präposition: gedenken (gedenken der Opfer), bedürfen (bedarf der Klärung), sich rühmen (rühmt sich seiner Taten), anklagen (klagt ihn des Mordes an).",
        "formula": "Subjekt + Verb + Genitivobjekt",
        "examples": [
            {"de": "Die Versammelten gedachten schweigend der Opfer der Katastrophe.", "en": "Those gathered commemorated the victims of the catastrophe in silence.", "breakdown": "gedachten der Opfer (Genitiv Plural)"},
            {"de": "Diese heikle Angelegenheit bedarf noch gründlicher Überprüfung.", "en": "This delicate matter still requires thorough verification.", "breakdown": "bedarf gründlicher Überprüfung (Genitiv feminin)"},
            {"de": "Er rühmt sich gern seiner angeblich zahllosen Auslandserfolge.", "en": "He likes to boast of his allegedly countless foreign successes.", "breakdown": "sich rühmen + Genitiv"},
            {"de": "Die Staatsanwaltschaft klagte den Manager der Steuerhinterziehung an.", "en": "The prosecution charged the manager with tax evasion.", "breakdown": "anklagen + Akkusativ (den Manager) + Genitiv (der Steuerhinterziehung)"}
        ],
        "takeaway": "Echte Genitivverben: gedenken, bedürfen, anklagen, verdächtigen, beschuldigen."
    },
    {
        "id": "b2-rek-68",
        "level": "B2",
        "category": "Gehobene Verbrektion",
        "title": "Verben mit doppeltem Akkusativ (nennen, schelten, schimpfen)",
        "rule": "Eine sehr kleine Gruppe von Verben bindet ZWEI Akkusativobjekte gleichzeitig: nennen (er nannte ihn einen Lügner), schimpfen, kosten (das kostet mich viel Geld).",
        "formula": "Subjekt + Verb + Akk-Objekt 1 (Person) + Akk-Objekt 2 (Bezeichnung/Preis)",
        "examples": [
            {"de": "Er nannte den neuen Kollegen einen begnadeten Coder.", "en": "He called the new colleague a gifted coder.", "breakdown": "den Kollegen (Akk 1) + einen begnadeten Coder (Akk 2)"},
            {"de": "Diese unüberlegte Reparatur kostete mich ein ganzes Monatsgehalt.", "en": "This ill-considered repair cost me a whole month's salary.", "breakdown": "mich (Akk 1) + ein Monatsgehalt (Akk 2)"},
            {"de": "Sie schimpfte den unhöflichen Autofahrer einen rücksichtslosen Raser.", "en": "She called the impolite motorist a reckless speeder.", "breakdown": "den Autofahrer (Akk 1) + einen Raser (Akk 2)"},
            {"de": "Man taufte das neue Schiff die Königin der Meere.", "en": "They christened the new ship the Queen of the Seas.", "breakdown": "das Schiff + die Königin"}
        ],
        "takeaway": "Verben wie nennen/kosten verlangen gleich zwei Akkusative."
    },
    {
        "id": "b2-rek-69",
        "level": "B2",
        "category": "Gehobene Verbrektion",
        "title": "Adjektive mit Dativ (mir vertraut, ihm gewachsen, der Lage bewusst)",
        "rule": "Viele gehobene Adjektive fordern eine feste Kasus-Rektion: meist Dativ (bekannt, vertraut, gewachsen, fremd, dankbar, behilflich), selten Genitiv (sich einer Sache bewusst sein).",
        "formula": "Dativ + Adjektiv (z.B. mir vertraut / ihm unterlegen)",
        "examples": [
            {"de": "Die Berliner Mentalität ist mir inzwischen sehr vertraut.", "en": "The Berlin mentality is very familiar to me by now.", "breakdown": "mir (Dativ) vertraut"},
            {"de": "Er war den hohen Anforderungen der neuen Position leider nicht gewachsen.", "en": "Unfortunately he was not equal to the high demands of the new position.", "breakdown": "den Anforderungen (Dativ) gewachsen"},
            {"de": "Ich wäre Ihnen für eine rasche Rückmeldung äußerst dankbar.", "en": "I would be extremely grateful to you for a prompt feedback.", "breakdown": "Ihnen (Dativ) dankbar"},
            {"de": "Sie ist sich der großen Tragweite ihrer Entscheidung voll bewusst.", "en": "She is fully aware of the great scope of her decision.", "breakdown": "sich (Dat) + der Tragweite (Genitiv) bewusst sein"}
        ],
        "takeaway": "Dativ bei Adjektiven: mir vertraut, ihm ähnlich, der Aufgabe gewachsen."
    },
    {
        "id": "b2-rek-70",
        "level": "B2",
        "category": "Gehobene Verbrektion",
        "title": "Präpositionen mit Dativ ODER Genitiv (dank, laut, gemäß)",
        "rule": "Einige Präpositionen schwanken im Sprachgebrauch zwischen Dativ und Genitiv: 'dank' (dank seines Einsatzes / dank seinem Einsatz), 'laut' (laut aktuellem Bericht / laut aktuellem Berichts), 'gemäß' (gemäß den Vorschriften). Der Dativ dominiert im Alltag.",
        "formula": "dank / laut / gemäß + Dativ oder Genitiv",
        "examples": [
            {"de": "Dank deiner tatkräftigen Hilfe haben wir den Umzug in zwei Stunden geschafft.", "en": "Thanks to your energetic help, we managed the move in two hours.", "breakdown": "dank + Genitiv (deiner Hilfe)"},
            {"de": "Dank modernem Equipment konnten die Ärzte den Eingriff minimalinvasiv durchführen.", "en": "Thanks to modern equipment, doctors were able to perform the procedure minimally invasively.", "breakdown": "dank + Dativ (modernem Equipment)"},
            {"de": "Laut vorliegendem Gutachten ist das Fundament des Hauses vollkommen intakt.", "en": "According to the available expert report, the foundation of the house is completely intact.", "breakdown": "laut + Dativ"},
            {"de": "Wir handeln streng gemäß den geltenden Datenschutzbestimmungen.", "en": "We act strictly in accordance with applicable data protection regulations.", "breakdown": "gemäß + Dativ (meist nachgestellt oder vorangestellt)"}
        ],
        "takeaway": "dank, laut und gemäß sind standardsprachlich mit Dativ oder Genitiv voll akzeptiert."
    },

    # 71-105: Sentence Topology, Nuances, Rhetoric
    {
        "id": "b2-top-71",
        "level": "B2",
        "category": "Satztopologie & Textkohärenz",
        "title": "Das deutsche Satzmodell: Vorfeld, Mittelfeld, Nachfeld",
        "rule": "Im deutschen Hauptsatz bildet das Verb die Satzklammer (linke Klammer = finites Verb auf Pos 2; rechte Klammer = infiniter Verbteil am Satzende). Davor liegt das Vorfeld (genau 1 Satzglied). Dazwischen liegt das Mittelfeld. Dahinter das Nachfeld (für Ausklammerungen).",
        "formula": "[Vorfeld] + [Linke Klammer: finites Verb] + [Mittelfeld] + [Rechte Klammer: Verbteil] + [Nachfeld]",
        "examples": [
            {"de": "[Gestern] [hat] [der Student im Lesesaal konzentriert gearbeitet] [].", "en": "Yesterday the student worked concentratedly in the reading room.", "breakdown": "Vorfeld: Gestern | L-Klammer: hat | Mittelfeld: der Student... | R-Klammer: gearbeitet"},
            {"de": "[Wegen des Gewitters] [musste] [der Pilot den Anflug abbrechen] [].", "en": "Due to the thunderstorm, the pilot had to abort the approach.", "breakdown": "Vorfeld: Kausalangabe | L-Klammer: musste | R-Klammer: abbrechen"},
            {"de": "[Niemand] [hatte] [damit gerechnet] [, dass die Zinsen so stark steigen].", "en": "Nobody had expected that interest rates would rise so sharply.", "breakdown": "Nachfeld: Nebensatz ausgeklammert hinter 'gerechnet'"},
            {"de": "[Die Präsentation] [begann] [pünktlich um neun Uhr] [].", "en": "The presentation started promptly at 9 AM.", "breakdown": "einfache Klammer"}
        ],
        "takeaway": "Felderlehre verstehen: Genau EIN Element im Vorfeld vor dem konjugierten Verb!"
    },
    {
        "id": "b2-top-72",
        "level": "B2",
        "category": "Satztopologie & Textkohärenz",
        "title": "Ausklammerung ins Nachfeld zur Entlastung des Satzes",
        "rule": "Ist das Mittelfeld zu lang oder komplex, können Vergleichsphrasen (mit wie/als), Präpositionalphrasen oder Nebensätze hinter die rechte Verbklammer ins Nachfeld verschoben werden. Das macht den Satz leichter verständlich.",
        "formula": "Verbklammer (Partizip/Infinitiv) + [Nachfeld: Vergleich / Präpositionalphrase / Nebensatz]",
        "examples": [
            {"de": "Er hat gestern viel länger gearbeitet [als sonst üblich].", "en": "He worked yesterday much longer than usual.", "breakdown": "Vergleich 'als sonst üblich' steht ausgeklammert im Nachfeld"},
            {"de": "Ich habe mich lange unterhalten [mit der neuen Projektleiterin aus Hamburg].", "en": "I chatted for a long time with the new project manager from Hamburg.", "breakdown": "schwere Präpositionalphrase ins Nachfeld gestellt"},
            {"de": "Wir haben beschlossen [, dass wir die Verhandlungen fortsetzen].", "en": "We decided that we will continue negotiations.", "breakdown": "dass-Satz steht im Nachfeld hinter 'beschlossen'"},
            {"de": "Sie hat alle Prüfungen besser bestanden [als ihre Mitschüler].", "en": "She passed all exams better than her classmates.", "breakdown": "Vergleich im Nachfeld"}
        ],
        "takeaway": "Ausklammerung verhindert 'Bandwurmsätze' und erhöht die Verständlichkeit."
    },
    {
        "id": "b2-top-73",
        "level": "B2",
        "category": "Satztopologie & Textkohärenz",
        "title": "Spannungsaufbau durch Inversion im Vorfeld",
        "rule": "Um Sätze abwechslungsreich zu gestalten und thematische Übergänge zu schaffen, rücken Adverbien, Objekte oder Nebensätze ins Vorfeld. Das Subjekt wandert dann ins Mittelfeld direkt hinter das finite Verb.",
        "formula": "[Objekt / Adverb / Nebensatz] + [Verb] + [Subjekt]...",
        "examples": [
            {"de": "Dieses faszinierende Buch habe ich in einem einzigen Zug durchgelesen.", "en": "This fascinating book I read through in a single sitting.", "breakdown": "Akkusativobjekt im Vorfeld zur Betonung"},
            {"de": "Dem mutigen Retter verlieh der Bundespräsident das Verdienstkreuz.", "en": "To the courageous rescuer, the Federal President awarded the Cross of Merit.", "breakdown": "Dativobjekt im Vorfeld"},
            {"de": "Plötzlich und völlig unerwartet stürzte die Netzwerkverbindung ab.", "en": "Suddenly and completely unexpectedly, the network connection crashed.", "breakdown": "Modaladverb im Vorfeld"},
            {"de": "Kaum war er eingeschlafen, klingelte schon wieder der Wecker.", "en": "Barely had he fallen asleep, the alarm clock rang once more.", "breakdown": "Temporale Einschränkung im Vorfeld"}
        ],
        "takeaway": "Niemals jeden Satz mit dem Subjekt beginnen – Inversion schafft Stil und Fluss."
    },
    {
        "id": "b2-top-74",
        "level": "B2",
        "category": "Satztopologie & Textkohärenz",
        "title": "Textverknüpfung durch Konnektroadverbien (hingegen, demnach, folglich)",
        "rule": "Adverbien wie 'hingegen' (on the other hand), 'demnach' (accordingly) und 'folglich' (consequently) schaffen geschmeidige logische Übergänge zwischen Sätzen in B2-Aufsätzen.",
        "formula": "Satz 1. Adverb (Pos 1) + Verb + Subjekt... ODER Subjekt + Verb + Adverb (im Mittelfeld)",
        "examples": [
            {"de": "Die Verkaufszahlen im Inland sanken. Im Ausland hingegen stiegen sie rasant.", "en": "Domestic sales fell. Abroad, on the other hand, they rose rapidly.", "breakdown": "hingegen im Mittelfeld"},
            {"de": "Alle Messwerte lagen im Normbereich. Demnach besteht kein Grund zur Sorge.", "en": "All measured values lay within standard range. Accordingly, there is no reason for concern.", "breakdown": "demnach auf Position 1 mit Inversion"},
            {"de": "Der Zeuge verwickelte sich in Widersprüche. Folglich zweifelte das Gericht an seiner Glaubwürdigkeit.", "en": "The witness tangled himself in contradictions. Consequently, the court doubted his credibility.", "breakdown": "folglich auf Position 1"},
            {"de": "Er hatte nicht gelernt. Ergo fiel er durch die Prüfung.", "en": "He had not studied. Ergo he failed the exam.", "breakdown": "ergo als lateinisches Bildungswort"}
        ],
        "takeaway": "hingegen, demnach, folglich verbinden Gedanken logisch auf akademischem Niveau."
    },
    {
        "id": "b2-top-75",
        "level": "B2",
        "category": "Satztopologie & Textkohärenz",
        "title": "Präzise Wortwahl: scheinbar vs. anscheinend",
        "rule": "'scheinbar' bedeutet 'nur dem Schein nach, in Wirklichkeit aber NICHT so' (deceptive appearance). 'anscheinend' bedeutet 'allem Anschein nach, vermutlich tatsächlich so' (apparently / evident).",
        "formula": "scheinbar = Täuschung / Unwahrheit | anscheinend = Vermutung / Realität",
        "examples": [
            {"de": "Das Problem war scheinbar gelöst, aber nach zwei Stunden trat der Fehler erneut auf.", "en": "The problem was seemingly solved, but after two hours the error occurred anew.", "breakdown": "scheinbar = war in Wahrheit nicht gelöst (Täuschung)"},
            {"de": "Anscheinend hat er den Zug verpasst, denn er ist immer noch nicht im Konferenzraum.", "en": "Apparently he missed the train, for he is still not in the conference room.", "breakdown": "anscheinend = es sieht stark danach aus (Vermutung)"},
            {"de": "Er hörte scheinbar interessiert zu, dachte aber in Wirklichkeit an seinen Urlaub.", "en": "He listened ostensibly interested, but was thinking about his holiday in reality.", "breakdown": "scheinbar = reiner Schein"},
            {"de": "Anscheinend wird das Wetter morgen wieder sonnig und warm.", "en": "Apparently the weather will be sunny and warm again tomorrow.", "breakdown": "anscheinend = Vorhersage/Wahrnehmung"}
        ],
        "takeaway": "scheinbar = Illusion / nicht wahr; anscheinend = wahrscheinlich / tatsächlich so."
    },
    {
        "id": "b2-top-76",
        "level": "B2",
        "category": "Satztopologie & Textkohärenz",
        "title": "Präzise Wortwahl: dasselbe vs. das gleiche",
        "rule": "'dasselbe' bezeichnet ein und dasselbe identische Einzelobjekt (identisch). 'das gleiche' bezeichnet zwei verschiedene Objekte von exakt gleicher Art oder Beschaffenheit (gleichartig).",
        "formula": "dasselbe = identisches Unikat | das gleiche = zwei gleiche Exemplare",
        "examples": [
            {"de": "Wir wohnen im selben Haus, aber in verschiedenen Stockwerken.", "en": "We live in the same house, but on different floors.", "breakdown": "dasselbe Haus = ein einziges physisches Gebäude"},
            {"de": "Meine Kollegin und ich tragen heute zufällig das gleiche Kleid.", "en": "My colleague and I happen to wear the same dress today.", "breakdown": "das gleiche Kleid = zwei identisch aussehende Kleidungsstücke!"},
            {"de": "Er fährt dasselbe Auto seit zehn Jahren.", "en": "He drives the same car for ten years.", "breakdown": "dasselbe Auto = sein spezifischer Wagen"},
            {"de": "Ich habe mir die gleichen Kopfhörer wie du gekauft.", "en": "I bought the same headphones as you.", "breakdown": "die gleichen = ein zweites Exemplar"}
        ],
        "takeaway": "Zwei Menschen können das gleiche Kleid tragen, aber niemals dasselbe zur selben Zeit!"
    },
    {
        "id": "b2-top-77",
        "level": "B2",
        "category": "Satztopologie & Textkohärenz",
        "title": "Modalpartikeln auf B2-Niveau: ja, doch, mal, eben",
        "rule": "Modalpartikeln (Abtönungspartikeln) verändern die emotionale Färbung, Tönung und soziale Beziehung im Satz. Sie sind unbetont und stehen im Mittelfeld: ja (Bekanntheit/Überraschung), doch (Widerspruch/Erinnerung), eben/halt (Unvermeidbarkeit).",
        "formula": "Subjekt + Verb + [ja / doch / eben / mal] + ...",
        "examples": [
            {"de": "Du weißt ja, wie pingelig der Prüfer bei Rechtschreibung ist.", "en": "You know, after all, how meticulous the examiner is with spelling.", "breakdown": "ja = appelliert an gemeinsames Vorwissen"},
            {"de": "Komm doch heute Abend einfach mit uns ins Theater!", "en": "Do just come along with us to the theater tonight!", "breakdown": "doch = ermunternde Aufforderung"},
            {"de": "Es regnet in Strömen; da kann man eben nichts machen.", "en": "It is pouring rain; there's just nothing one can do about it.", "breakdown": "eben = Resignation / unveränderliche Tatsache"},
            {"de": "Schau mal, wer da gerade zur Tür hereinkommt!", "en": "Just look who is coming in through the door right now!", "breakdown": "mal = Abschwächung / Fokussierung"}
        ],
        "takeaway": "Modalpartikeln machen Deutsch lebendig und idiomatisch authentisch."
    },
    {
        "id": "b2-top-78",
        "level": "B2",
        "category": "Satztopologie & Textkohärenz",
        "title": "Modalpartikeln: wohl, eigentlich, etwa, denn",
        "rule": "'wohl' drückt Vermutung aus; 'eigentlich' signalisiert ein Zurückkommen auf den Kern; 'etwa' in Fragen drückt ungläubige Überraschung aus; 'denn' in Fragen mildert oder schärft das Interesse.",
        "formula": "Frage + denn / etwa? | Aussage + wohl / eigentlich",
        "examples": [
            {"de": "Er wird wohl im Stau auf der Stadtautobahn stehen.", "en": "He is probably stuck in traffic on the city highway.", "breakdown": "wohl = Vermutung"},
            {"de": "Hast du denn gar keine Geduld mehr?", "en": "Do you have no patience left at all?", "breakdown": "denn in der Frage verstärkt Neugier/Vorwurf"},
            {"de": "Glaubst du etwa, ich hätte den ganzen Tag nichts zu tun?", "en": "Do you perhaps believe I had nothing to do all day?", "breakdown": "etwa in der Frage = Befürchtung/Zweifel"},
            {"de": "Was wolltest du eigentlich vorhin sagen, bevor wir unterbrochen wurden?", "en": "What did you actually want to say earlier before we were interrupted?", "breakdown": "eigentlich = Wiederanknüpfung"}
        ],
        "takeaway": "Partikeln verankern gesprochene und geschriebene Aussagen im sozialen Kontext."
    },
    {
        "id": "b2-top-79",
        "level": "B2",
        "category": "Satztopologie & Textkohärenz",
        "title": "Negation mit 'keineswegs', 'durchaus nicht', 'mitnichten'",
        "rule": "Um eine Verneinung stilistisch zu schärfen und formell zu bekräftigen, ersetzt man einfaches 'nicht' durch gehobene Negationsadverbien wie 'keineswegs', 'durchaus nicht' oder das literarische 'mitnichten'.",
        "formula": "keineswegs / durchaus nicht + Adjektiv / Verb",
        "examples": [
            {"de": "Diese Entscheidung war keineswegs leichtsinnig, sondern wohlüberlegt.", "en": "This decision was by no means reckless, but well-considered.", "breakdown": "keineswegs = by no means"},
            {"de": "Wir sind mit diesem Zwischenergebnis durchaus nicht zufrieden.", "en": "We are by no means satisfied with this interim result.", "breakdown": "durchaus nicht = definitely not"},
            {"de": "War die Mission ein Misserfolg? – Mitnichten, sie übertraf alle Erwartungen!", "en": "Was the mission a failure? – Far from it; it exceeded all expectations!", "breakdown": "mitnichten = literarische entschiedene Verneinung"},
            {"de": "Es ist keineswegs sicher, dass die Fördermittel bewilligt werden.", "en": "It is by no means certain that funding will be approved.", "breakdown": "keineswegs sicher"}
        ],
        "takeaway": "keineswegs und durchaus nicht verleihen Argumenten Nachdruck."
    },
    {
        "id": "b2-top-80",
        "level": "B2",
        "category": "Satztopologie & Textkohärenz",
        "title": "Vergleiche mit als und wie im B2-Feinschliff",
        "rule": "'wie' steht bei Gleichheit (so groß wie). 'als' steht bei Ungleichheit / Komparativ (größer als). Häufiger Fehler: Verwechslung von 'als' und 'wie' ('größer wie' ist dialektal und grammatisch falsch!).",
        "formula": "so / genauso + Adjektiv + wie | Komparativ (-er) + als",
        "examples": [
            {"de": "Der neue Motor arbeitet doppelt so effizient wie das alte Modell.", "en": "The new engine operates twice as efficiently as the old model.", "breakdown": "so... wie (Gleichheit/Vergleichsmaß)"},
            {"de": "Die Mieten in Berlin sind heute deutlich höher als vor zehn Jahren.", "en": "Rents in Berlin are significantly higher today than ten years ago.", "breakdown": "höher als (Komparativ: Ungleichheit)"},
            {"de": "Er verhält sich ganz anders, als wir es erwartet hatten.", "en": "He behaves quite differently than we had expected.", "breakdown": "anders als"},
            {"de": "Sie verdient genauso viel Geld wie ihr Kollege in gleicher Position.", "en": "She earns just as much money as her colleague in the same position.", "breakdown": "genauso viel wie"}
        ],
        "takeaway": "Merke: 'Genauso wie', aber 'Besser als'. Niemals 'besser wie' schreiben!"
    },

    # 81-105: Stylistic Mastery & Advanced Grammar Nuances
    {
        "id": "b2-fein-81",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Kommasetzung bei Infinitivgruppen: Wann ist das Komma Pflicht?",
        "rule": "Ein Komma bei 'zu + Infinitiv' ist PFLICHT, wenn die Infinitivgruppe: 1. mit um, ohne, statt, anstatt, außer eingeleitet wird, 2. von einem Nomen abhängt (die Absicht, ... zu tun), 3. durch ein Hinweiswort angekündigt wird (Ich freue mich darauf, dich zu sehen).",
        "formula": "Kommapflicht bei: um/ohne/statt... zu | Nomen + zu | Hinweiswort (darauf, es) + zu",
        "examples": [
            {"de": "Er ging früher nach Hause, um für die Prüfung zu lernen.", "en": "He went home earlier in order to study for the exam.", "breakdown": "eingeleitet mit 'um' -> Komma obligatorisch!"},
            {"de": "Ich habe die feste Absicht, mein C1-Zertifikat im Sommer abzulegen.", "en": "I have the firm intention to sit my C1 certificate in summer.", "breakdown": "hängt vom Nomen 'die feste Absicht' ab -> Komma obligatorisch!"},
            {"de": "Sie erinnerte mich daran, den Mietvertrag rechtzeitig zu kündigen.", "en": "She reminded me to cancel the tenancy agreement in time.", "breakdown": "Korrelat 'daran' -> Komma obligatorisch!"},
            {"de": "Er versuchte zu schlafen. (einfacher Infinitiv -> Komma fakultativ)", "en": "He tried to sleep.", "breakdown": "kurze, einfache Infinitivgruppe ohne Signale"}
        ],
        "takeaway": "Sobald 'um/ohne/statt', ein Nomen oder ein Da-Wort im Spiel ist: IMMER Komma vor der Infinitivgruppe!"
    },
    {
        "id": "b2-fein-82",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Kommasetzung bei mehrteiligen Nebensätzen und Reihungen",
        "rule": "Werden zwei gleichrangige Nebensätze mit 'und' oder 'oder' verbunden, steht VOR dem 'und' KEIN Komma. Trennt man jedoch Hauptsatz und Nebensatz, ist das Komma zwingend.",
        "formula": "Hauptsatz, weil [Nebensatz 1] und weil [Nebensatz 2]. (Kein Komma vor 'und'!)",
        "examples": [
            {"de": "Wir blieben zu Hause, weil es stürmte und weil die Bahnen nicht fuhren.", "en": "We stayed home because it was storming and because trains were not running.", "breakdown": "zwei weil-Sätze mit 'und' verbunden -> kein Komma vor und"},
            {"de": "Er versprach, dass er pünktlich sei, aber er kam trotzdem zu spät.", "en": "He promised that he would be on time, but he arrived late anyway.", "breakdown": "Komma vor 'aber' Pflicht"},
            {"de": "Wenn Sie ankommen und wenn das Hotelzimmer frei ist, rufen Sie mich an.", "en": "When you arrive and when the hotel room is free, call me.", "breakdown": "Reihung zweier wenn-Sätze"},
            {"de": "Ich weiß nicht, wann der Zug abfährt oder wo wir umsteigen müssen.", "en": "I don't know when the train departs or where we have to transfer.", "breakdown": "zwei indirekte Fragen mit 'oder'"}
        ],
        "takeaway": "Nebensätze mit 'und' / 'oder' gereiht = kein Komma zwischen den Nebensätzen."
    },
    {
        "id": "b2-fein-83",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Appositionen und ihre Deklination im Satzgefüge",
        "rule": "Eine Apposition ist ein Beisatz zu einem Nomen, der durch Kommas abgetrennt wird. Die lockere Apposition steht IMMER im gleichen Kasus wie das Bezugswort!",
        "formula": "Bezugswort (Kasus X), [Apposition im Kasus X], ...",
        "examples": [
            {"de": "Herr Müller, unser erfahrener Chefingenieur, leitet das neue Großprojekt.", "en": "Mr. Müller, our experienced chief engineer, leads the new major project.", "breakdown": "Herr Müller (Nom) -> unser erfahrener Chefingenieur (Nom)"},
            {"de": "Ich sprach mit Frau Dr. Schulz, der renommierten Forscherin der Charité.", "en": "I spoke with Dr. Schulz, the renowned researcher at Charité.", "breakdown": "mit Frau Dr. Schulz (Dat) -> der renommierten Forscherin (Dat)"},
            {"de": "Wir besuchten Potsdam, die historische Landeshauptstadt Brandenburgs.", "en": "We visited Potsdam, the historic state capital of Brandenburg.", "breakdown": "Potsdam (Akk) -> die Landeshauptstadt (Akk)"},
            {"de": "Das Auto meines Nachbarn, eines bekannten Musikers, steht vor der Tür.", "en": "The car of my neighbor, a well-known musician, is parked in front of the door.", "breakdown": "meines Nachbarn (Gen) -> eines bekannten Musikers (Gen)"}
        ],
        "takeaway": "Kongruenz bei Appositionen: Nomen und Apposition stehen im selben Fall."
    },
    {
        "id": "b2-fein-84",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Zusammengesetzte Nomen (Komposita) und das Fugen-s",
        "rule": "Deutsche Komposita werden aus zwei oder mehr Wörtern zusammengesetzt. Oft wird ein 'Fugen-s' eingefügt, besonders nach Nomen auf -ung, -heit, -keit, -schaft, -tion, -tät (Abfahrt-s-zeit, Wirtschaft-s-krise).",
        "formula": "Bestimmungswort + (Fugen-s / -en) + Grundwort (bestimmt den Artikel!)",
        "examples": [
            {"de": "Die Abfahrtszeit des Zuges wurde kurzfristig um zehn Minuten vorverlegt.", "en": "The departure time of the train was brought forward by ten minutes at short notice.", "breakdown": "Abfahrt + s + Zeit"},
            {"de": "Die Wirtschaftskrise forderte harte Sparmaßnahmen von vielen Unternehmen.", "en": "The economic crisis demanded tough austerity measures from many enterprises.", "breakdown": "Wirtschaft + s + Krise"},
            {"de": "Der Arbeitsplatz der Zukunft wird flexibler und digitaler sein.", "en": "The workplace of the future will be more flexible and digital.", "breakdown": "Arbeit + s + Platz"},
            {"de": "Das Forschungsinstitut erhielt erhebliche Fördermittel vom Staat.", "en": "The research institute received substantial funding from the state.", "breakdown": "Forschung + s + Institut"}
        ],
        "takeaway": "Nomen auf -ung/-heit/-keit/-schaft/-tion erhalten fast immer ein Fugen-s."
    },
    {
        "id": "b2-fein-85",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Adverbiale Bestimmungen: Kausalangaben (aus vs. vor)",
        "rule": "Bei Gefühlsursachen unterscheidet man im Deutschen präzise: 'vor + Dativ' drückt eine unwillkürliche, reflexartige Körperreaktion aus (vor Angst zittern, vor Kälte frieren). 'aus + Dativ' drückt eine bewusste oder unbewusste Motivation aus (aus Liebe, aus Neugier, aus Mitleid).",
        "formula": "vor + Dativ (Reflex / physische Reaktion) | aus + Dativ (Motivation / Beweggrund)",
        "examples": [
            {"de": "Das kleine Kind zitterte vor Kälte am ganzen Körper.", "en": "The little child was shivering all over with cold.", "breakdown": "vor Kälte (physische, automatische Reaktion)"},
            {"de": "Er handelte aus reiner Neugier, ohne die Gefahren zu bedenken.", "en": "He acted out of sheer curiosity without considering the dangers.", "breakdown": "aus Neugier (Motivation/Beweggrund)"},
            {"de": "Sie konnte vor Aufregung die ganze Nacht kein Auge zudrücken.", "en": "She could not sleep a wink all night out of excitement.", "breakdown": "vor Aufregung (blockierender Zustand)"},
            {"de": "Aus Höflichkeit lehnte er das zweite Stück Kuchen nicht ab.", "en": "Out of politeness, he did not turn down the second piece of cake.", "breakdown": "aus Höflichkeit (sozialer Beweggrund)"}
        ],
        "takeaway": "'vor' = unkontrollierbare Reaktion (vor Wut weinen); 'aus' = Beweggrund (aus Mitleid helfen)."
    },
    {
        "id": "b2-fein-86",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Fremdwörter und Fachbegriffe mit deutschen Präfixen",
        "rule": "In der B2-Fachsprache werden viele Fremdwörter mit deutschen Präfixen kombiniert: deinstallieren, reaktivieren, vordefinieren, überkompensieren, zwischenspeichern.",
        "formula": "Präfix + Fremdwort-Stamm (z.B. vor-strukturieren)",
        "examples": [
            {"de": "Bitte zwischenspeichern Sie die Datei vor dem Schließen des Programms.", "en": "Please buffer/save the file temporarily before closing the program.", "breakdown": "zwischen-speichern"},
            {"de": "Der Arzt musste die Dosierung des Medikaments neu einstellen.", "en": "The doctor had to readjust the dosage of the medication.", "breakdown": "neu einstellen"},
            {"de": "Die Parameter wurden vom Systemadministrator bereits vordefiniert.", "en": "The parameters were already predefined by the system administrator.", "breakdown": "vor-definiert"},
            {"de": "Wir müssen den alten Server nach dem Ausfall wieder reaktivieren.", "en": "We must reactivate the old server after the outage.", "breakdown": "reaktivieren"}
        ],
        "takeaway": "Hybride Wortbildungen prägen die moderne deutsche IT- und Ingenieurssprache."
    },
    {
        "id": "b2-fein-87",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Verben mit trennbarem vs. untrennbarem Präfix (umfahren, durchschauen)",
        "rule": "Einige Verben können je nach Betonung trennbar ODER untrennbar sein, mit drastisch unterschiedlicher Bedeutung: umfahren (trennbar: úmfahren = überfahren/rammen; untrennbar: umfáhren = im Bogen herumfahren), durchschauen (durchscháuen = verstehen; dúrchschauen = hindurchblicken).",
        "formula": "Betontes Präfix = trennbar (úmfahren) | Unbetontes Präfix = untrennbar (umfáhren)",
        "examples": [
            {"de": "Der Autofahrer umfuhr das gefährliche Schlagloch geschickt. (untrennbar)", "en": "The motorist drove skillfully around the dangerous pothole.", "breakdown": "umfáhren = herumfahren, kein Ge- im Partizip: hat umfahren"},
            {"de": "Der Fahrer fuhr das Stoppschild versehentlich um. (trennbar)", "en": "The driver accidentally knocked down the stop sign.", "breakdown": "úmfahren = rammen/umwerfen, Partizip: hat umgefahren"},
            {"de": "Die Psychologin durchschaute sofort die Ausreden des Patienten.", "en": "The psychologist saw through the patient's excuses immediately.", "breakdown": "durchscháuen = Motive erkennen"},
            {"de": "Wir übersetzten den Vertrag ins Deutsche. (untrennbar: übersétzen)", "en": "We translated the contract into German.", "breakdown": "übersetzen = Sprache übertragen"}
        ],
        "takeaway": "Betonung bestimmt die Bedeutung: úmfahren (Crash!) vs. umfáhren (Ausweichen!)."
    },
    {
        "id": "b2-fein-88",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Passiv mit bekommen / kriegen (Das Rezipientenpassiv)",
        "rule": "Im Rezipientenpassiv (auch Adressatenpassiv) wird das Dativobjekt des Aktivsatzes zum Subjekt mit 'bekommen' oder 'kriegen' + Partizip II. Es drückt aus, was jemandem zuteilwird.",
        "formula": "Subjekt (früheres Dativobjekt) + bekommen / kriegen + Partizip II",
        "examples": [
            {"de": "Der Sieger bekam vom Bürgermeister eine goldene Medaille überreicht.", "en": "The winner was handed a gold medal by the mayor.", "breakdown": "bekam überreicht = dem Sieger wurde eine Medaille überreicht"},
            {"de": "Ich habe gestern ein neues Smartphone zum Geburtstag geschenkt bekommen.", "en": "I was given a new smartphone for my birthday yesterday.", "breakdown": "habe geschenkt bekommen"},
            {"de": "Die Mieter kriegen die Heizkostenabrechnung erst im Dezember zugestellt.", "en": "The tenants will have the heating bill delivered only in December.", "breakdown": "kriegen zugestellt"},
            {"de": "Er bekam die Kündigung völlig unerwartet überreicht.", "en": "He had the termination notice handed to him completely unexpectedly.", "breakdown": "bekam überreicht"}
        ],
        "takeaway": "Rezipientenpassiv: 'Ich bekomme geholfen' rückt den Empfänger ins Zentrum."
    },
    {
        "id": "b2-fein-89",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Modale Infinitivkonstruktionen mit 'haben... zu' (Pflicht)",
        "rule": "'haben + zu + Infinitiv' hat aktive Bedeutung und drückt eine strikte Verpflichtung oder Notwendigkeit aus ('müssen / sollen getan werden durch jemanden').",
        "formula": "Subjekt (Aktiv) + haben + ... + zu + Infinitiv",
        "examples": [
            {"de": "Die Mitarbeiter haben über alle Betriebsgeheimnisse Stillschweigen zu bewahren.", "en": "Employees are to maintain silence over all trade secrets.", "breakdown": "haben zu bewahren = müssen strikt bewahren"},
            {"de": "Du hast hier überhaupt nichts zu bestimmen!", "en": "You have absolutely nothing to decide here!", "breakdown": "hast zu bestimmen = darfst bestimmen"},
            {"de": "Wir haben bis Monatsende noch gewaltige Aufgaben zu bewältigen.", "en": "We still have immense tasks to accomplish by month's end.", "breakdown": "haben zu bewältigen = müssen bewältigen"},
            {"de": "Der Beschuldigte hat zu den Vorwürfen Stellung zu nehmen.", "en": "The accused has to take a stance on the allegations.", "breakdown": "hat Stellung zu nehmen"}
        ],
        "takeaway": "sein + zu = passiv (muss gemacht werden); haben + zu = aktiv (jemand muss tun)."
    },
    {
        "id": "b2-fein-90",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Präpositionen mit wechselnder Rektion im gehobenen Stil",
        "rule": "Präpositionen wie 'wegen' und 'trotz' stehen standardsprachlich mit Genitiv. Im gesprochenen Deutsch dringt der Dativ vor, doch im formellen B2-Schriftdeutsch gilt der Genitiv als unumstößlicher Qualitätsmaßstab.",
        "formula": "trotz / wegen + Genitiv (Standardsprache B2/C1)",
        "examples": [
            {"de": "Wegen eines plötzlichen technischen Defekts fiel die Übertragung aus.", "en": "Due to a sudden technical defect, the broadcast failed.", "breakdown": "wegen eines Defekts (Genitiv maskulin)"},
            {"de": "Trotz schlechter Witterungsbedingungen landete der Flug sicher.", "en": "Despite bad weather conditions, the flight landed safely.", "breakdown": "trotz schlechter Witterungsbedingungen (Genitiv Plural)"},
            {"de": "Während des gesamten Vortrags hörte das Publikum mucksmäuschenstill zu.", "en": "Throughout the entire lecture, the audience listened quietly as mice.", "breakdown": "während des Vortrags (Genitiv maskulin)"},
            {"de": "Innerhalb weniger Tage war die Veranstaltung restlos ausverkauft.", "en": "Within a few days, the event was completely sold out.", "breakdown": "innerhalb weniger Tage (Genitiv Plural)"}
        ],
        "takeaway": "In offiziellen Prüfungen und Briefen: Wegen/trotz/während IMMER mit Genitiv konstruieren."
    },
    {
        "id": "b2-fein-91",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Satzverknüpfung mit Partizip II im Vorfeld (Kaum ausgesprochen, ...)",
        "rule": "Ein vorangestelltes Partizip II im Vorfeld leitet eine dichte, literarische oder journalistische Schilderung eines unmittelbaren Geschehens ein.",
        "formula": "[Partizip II + Ergänzung], + finites Verb + Subjekt...",
        "examples": [
            {"de": "Kaum ausgesprochen, bereute er seine unbedachten Worte bereits zutiefst.", "en": "Barely uttered, he already deeply regretted his thoughtless words.", "breakdown": "Kaum ausgesprochen im Vorfeld"},
            {"de": "Im Bundestag verabschiedet, muss das Gesetz nun noch vom Bundesrat gebilligt werden.", "en": "Passed in the Bundestag, the bill must now still be approved by the Bundesrat.", "breakdown": "Verabschiedet leitet den Zustand ein"},
            {"de": "Einmal gestartet, ließ sich der automatische Download nicht mehr abbrechen.", "en": "Once started, the automatic download could no longer be aborted.", "breakdown": "Einmal gestartet"},
            {"de": "Von allen gefeiert, verließ der Maestro unter tosendem Applaus die Bühne.", "en": "Celebrated by all, the maestro left the stage amid thunderous applause.", "breakdown": "Von allen gefeiert"}
        ],
        "takeaway": "Partizip II an Satzanfang erzeugt Dynamik und literarische Dichte."
    },
    {
        "id": "b2-fein-92",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Verneinung durch Präfixe und Suffixe (in-, des-, un-, -los, -frei)",
        "rule": "Zur präzisen semantischen Verneinung nutzt das Deutsche vielfältige morphologische Mittel: un- (ungeduldig), in-/im- (inaktiv, irreparabel), des- (desinteressiert), -los (arbeitslos, fehlerlos), -frei (zuckerfrei, einwandfrei).",
        "formula": "un- / des- / in- / a- + Stamm | Stamm + -los / -frei / -leer",
        "examples": [
            {"de": "Das vorgelegte Konzept ist in dieser Form völlig inakzeptabel.", "en": "The presented concept is completely unacceptable in this form.", "breakdown": "in-akzeptabel"},
            {"de": "Der Programmierer lieferte einen fehlerlosen und hocheffizienten Code ab.", "en": "The programmer delivered flawless and highly efficient code.", "breakdown": "fehler-los"},
            {"de": "Der Patient verhielt sich gegenüber den Ratschlägen des Arztes desinteressiert.", "en": "The patient acted disinterested toward the doctor's advice.", "breakdown": "des-interessiert"},
            {"de": "Die Konferenz verlief reibungslos und absolut einwandfrei.", "en": "The conference proceeded smoothly and absolutely flawlessly.", "breakdown": "einwand-frei"}
        ],
        "takeaway": "Präzise Negationsadjektive bereichern den B2-Wortschatz enorm."
    },
    {
        "id": "b2-fein-93",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Gleichzeitigkeit und Nicht-Gleichzeitigkeit bei Partizipien",
        "rule": "Partizip I drückt stets Gleichzeitigkeit zum Hauptsatz aus (lachend ging er = er ging und lachte). Partizip II drückt bei transitiven Verben Vorzeitigkeit und Passivität aus (geschlagen floh er = nachdem er geschlagen worden war).",
        "formula": "Partizip I = Gleichzeitigkeit (aktiv) | Partizip II = Vorzeitigkeit (passiv/perfektiv)",
        "examples": [
            {"de": "Freundlich lächelnd begrüßte die Empfangsdame jeden einzelnen Gast.", "en": "Smiling warmly, the receptionist greeted every single guest.", "breakdown": "lächelnd = gleichzeitig mit der Begrüßung"},
            {"de": "Vom Unwetter überrascht, suchten die Wanderer Schutz in einer Berghütte.", "en": "Surprised by the storm, the hikers sought shelter in a mountain hut.", "breakdown": "überrascht = geschah vor dem Schutzsuchen"},
            {"de": "Zögernd betrat der neue Mitarbeiter das Büro des Abteilungsleiters.", "en": "Hesitatingly, the new employee entered the department manager's office.", "breakdown": "zögernd = gleichzeitige Begleithandlung"},
            {"de": "Gut vorbereitet ging sie mit großer Zuversicht in das Prüfungsgespräch.", "en": "Well prepared, she went into the examination interview with great confidence.", "breakdown": "vorbereitet = vorab vollendet"}
        ],
        "takeaway": "Partizip I = währenddessen; Partizip II = zuvor geschehen."
    },
    {
        "id": "b2-fein-94",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Stilblüten vermeiden: Doppelter Genitiv vs. Präpositionalfügung",
        "rule": "Treffen zwei Genitivattribute direkt aufeinander (z.B. 'die Veröffentlichung des Buches meines Bruders'), wirkt der Satz oft schwerfällig. Stilistisch eleganter ist die Auflösung mit einer Präpositionalphrase ('die Veröffentlichung des Buches von meinem Bruder').",
        "formula": "Schwer: [Nomen] + Genitiv 1 + Genitiv 2 -> Besser: [Nomen] + Genitiv + von + Dativ",
        "examples": [
            {"de": "Schwerfällig: Die Renovierung des Hauses des Bürgermeisters dauerte Monate.", "en": "Cumbersome: The renovation of the house of the mayor took months.", "breakdown": "zwei Genitive hintereinander klingen ungelenk"},
            {"de": "Elegant: Die Renovierung des Hauses von Bürgermeister Müller dauerte Monate.", "en": "Elegant: The renovation of Mayor Müller's house took months.", "breakdown": "Auflösung mit 'von' zur Rhythmisierung"},
            {"de": "Schwerfällig: Die Analyse der Daten der Studie ergab neue Erkenntnisse.", "en": "Cumbersome: The analysis of the data of the study yielded new insights.", "breakdown": "der Daten der Studie"},
            {"de": "Elegant: Die Analyse der Studiendaten ergab neue Erkenntnisse.", "en": "Elegant: Analysis of the study data yielded new insights.", "breakdown": "Kompositum-Bildung als eleganteste Lösung"}
        ],
        "takeaway": "Doppelgenitive meiden: Durch Komposita oder 'von + Dativ' entzerren."
    },
    {
        "id": "b2-fein-95",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Substantivierung ganzer Infinitivphrasen (das ständige Zuspätkommen)",
        "rule": "Ganze Handlungen können durch Substantivierung des Infinitivs (Neutrum: das + großgeschriebener Infinitiv) verdichtet werden. Begleitende Adverbien werden zu deklinierten Adjektiven.",
        "formula": "das + Adjektiv + großgeschriebener Infinitiv + Genitivattribut",
        "examples": [
            {"de": "Das ständige Zuspätkommen des Mitarbeiters führte zu einer Abmahnung.", "en": "The employee's persistent arriving late led to a formal warning.", "breakdown": "das ständige Zuspätkommen"},
            {"de": "Das rücksichtslose Überholen auf der Landstraße ist extrem gefährlich.", "en": "Reckless overtaking on rural roads is extremely dangerous.", "breakdown": "das rücksichtslose Überholen"},
            {"de": "Das laute Musikhören nach 22 Uhr stört die Nachtruhe der Nachbarn.", "en": "Loud music listening after 10 PM disturbs the neighbors' night rest.", "breakdown": "das laute Musikhören"},
            {"de": "Das sorgfältige Korrekturlesen verhindert peinliche Druckfehler.", "en": "Careful proofreading prevents embarrassing typographical errors.", "breakdown": "das sorgfältige Korrekturlesen"}
        ],
        "takeaway": "Das [Adjektiv] [Infinitiv]: Ein mächtiges Werkzeug für prägnante deutsche Formulierungen."
    },
    {
        "id": "b2-fein-96",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Rhetorische Stilmittel in B2-Texten: Antithese und Klimax",
        "rule": "In B2-Erörterungen und Vorträgen verstärken rhetorische Mittel wie die Antithese (Gegenüberstellung gegensätzlicher Begriffe: arm und reich, jung und alt) und die Klimax (dreigliedrige Steigerung: gut, besser, unübertroffen) die Überzeugungskraft.",
        "formula": "Antithese: [These] vs. [Antithese] | Klimax: [Stufe 1] -> [Stufe 2] -> [Stufe 3]",
        "examples": [
            {"de": "Antithese: Was heute als Segen gefeiert wird, kann sich morgen als Fluch erweisen.", "en": "Antithesis: What is celebrated as a blessing today can prove to be a curse tomorrow.", "breakdown": "Segen vs. Fluch (wirkungsvoller Kontrast)"},
            {"de": "Klimax: Wir müssen das Problem erkennen, verstehen und entschlossen lösen.", "en": "Climax: We must recognize, understand, and resolutely solve the problem.", "breakdown": "erkennen -> verstehen -> lösen (Steigerung)"},
            {"de": "Antithese: Die Mieten steigen rasant, während die Einkommen stagnieren.", "en": "Antithesis: Rents rise rapidly while incomes stagnate.", "breakdown": "steigen vs. stagnieren"},
            {"de": "Klimax: Er investierte Tage, Wochen, ja ganze Monate in diese Forschungsarbeit.", "en": "Climax: He invested days, weeks, indeed whole months in this research.", "breakdown": "Tage -> Wochen -> Monate"}
        ],
        "takeaway": "Antithese und Klimax strukturieren überzeugende Argumente in Aufsätzen."
    },
    {
        "id": "b2-fein-97",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Synonyme für 'sagen' im wissenschaftlichen und beruflichen Kontext",
        "rule": "In B2-Schreibaufgaben führt die ständige Wiederholung von 'sagen' zu Punktabzug. Nutzen Sie differenzierte Verben: behaupten (claim), betonen / hervorheben (emphasize), erläutern (explain), einräumen (concede), widersprechen (contradict).",
        "formula": "betonen / hervorheben / behaupten / darlegen / versichern statt immer nur 'sagen'",
        "examples": [
            {"de": "Die Ministerin betonte, wie entscheidend digitale Bildung für die Zukunft sei.", "en": "The minister stressed how crucial digital education was for the future.", "breakdown": "betonte statt sagte"},
            {"de": "Der Gutachter legte in seinem Bericht die baulichen Mängel ausführlich dar.", "en": "The expert set out the structural defects extensively in his report.", "breakdown": "darlegen = detailliert schildern"},
            {"de": "Der Sprecher räumte ein, dass Fehler im Vorfeld gemacht worden seien.", "en": "The spokesperson conceded that mistakes had been made beforehand.", "breakdown": "einräumen = Fehler oder Argumente anerkennen"},
            {"de": "Die Forscherin widersprach der bisherigen Lehrmeinung vehement.", "en": "The researcher contradicted the prevailing doctrine vehemently.", "breakdown": "widersprechen statt 'sagte Nein'"}
        ],
        "takeaway": "Ersetzen Sie 'sagen': betonen, erläutern, schildern, einräumen, postulieren."
    },
    {
        "id": "b2-fein-98",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Synonyme für 'machen' in gehobenen Formulierungen",
        "rule": "Auch das Alltagsverb 'machen' wird auf B2 durch präzisere Handlungsverben ersetzt: durchführen (Experiment), anfertigen (Kopie/Bericht), ausüben (Beruf/Druck), verüben (Straftat), erzielen (Gewinn).",
        "formula": "durchführen / anfertigen / leisten / erzielen statt 'machen'",
        "examples": [
            {"de": "Das Labor führte die klinische Studie unter strengsten Auflagen durch.", "en": "The laboratory carried out the clinical study under strict conditions.", "breakdown": "durchführen statt Studie machen"},
            {"de": "Der Anwalt fertigte eine Abschrift der Verhandlungsakte an.", "en": "The attorney prepared a transcript of the trial file.", "breakdown": "anfertigen statt Kopie machen"},
            {"de": "Das Startup erzielte im dritten Quartal beachtliche Gewinne.", "en": "The startup achieved considerable profits in the third quarter.", "breakdown": "erzielen statt Gewinn machen"},
            {"de": "Wir müssen alle einen spürbaren Beitrag zum Klimaschutz leisten.", "en": "We all have to make a tangible contribution to climate protection.", "breakdown": "Beitrag leisten statt Beitrag machen"}
        ],
        "takeaway": "Weg mit 'machen': durchführen, leisten, anfertigen, erzielen."
    },
    {
        "id": "b2-fein-99",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Passivumschreibungen mit 'erfahren', 'finden', 'erhalten'",
        "rule": "Funktionsverben wie 'erfahren', 'finden' oder 'erhalten' bilden elegante Umschreibungen des Passivs: Unterstützung finden (= unterstützt werden), eine Verbesserung erfahren (= verbessert werden), Anerkennung erhalten (= anerkannt werden).",
        "formula": "Unterstützung finden / Verbesserung erfahren / Anerkennung erhalten = Passiv",
        "examples": [
            {"de": "Der Vorschlag fand breite Unterstützung im gesamten Stadtrat.", "en": "The proposal found broad support across the entire city council.", "breakdown": "fand Unterstützung = wurde unterstützt"},
            {"de": "Das historische Schloss erfuhr in den letzten Jahren eine gründliche Sanierung.", "en": "The historic palace underwent a thorough renovation in recent years.", "breakdown": "erfuhr eine Sanierung = wurde saniert"},
            {"de": "Die engagierte Arbeit der Helfer erhielt höchste gesellschaftliche Anerkennung.", "en": "The dedicated work of the helpers received highest social recognition.", "breakdown": "erhielt Anerkennung = wurde anerkannt"},
            {"de": "Der Antrag stieß auf Ablehnung beim zuständigen Bauamt.", "en": "The application met with rejection at the competent building authority.", "breakdown": "stieß auf Ablehnung = wurde abgelehnt"}
        ],
        "takeaway": "Umschreibungen mit 'finden' und 'erfahren' beleben sachliche Fachtexte."
    },
    {
        "id": "b2-fein-100",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Graduierung von Adjektiven: überaus, höchst, ungemein, denkbar",
        "rule": "Statt des allgegenwärtigen 'sehr' nutzt der B2-Sprecher nuancierte Steigerungsadverbien: überaus freundlich, höchst erfreulich, ungemein spannend, denkbar einfach, zutiefst berührt.",
        "formula": "überaus / höchst / ungemein / denkbar / zutiefst + Adjektiv",
        "examples": [
            {"de": "Die Resonanz auf unseren Online-Workshop war überaus positiv.", "en": "The response to our online workshop was exceedingly positive.", "breakdown": "überaus positiv statt sehr positiv"},
            {"de": "Das Verhalten des Geschäftsführers war in dieser Krise höchst professionell.", "en": "The CEO's conduct in this crisis was highly professional.", "breakdown": "höchst professionell"},
            {"de": "Die Installation der neuen Programmierschnittstelle war denkbar einfach.", "en": "Installation of the new programming interface was as simple as could be.", "breakdown": "denkbar einfach = denkbar als Höchstmaß"},
            {"de": "Der Dokumentarfilm lieferte ein ungemein faszinierendes Porträt der Stadt.", "en": "The documentary delivered an immensely fascinating portrait of the city.", "breakdown": "ungemein faszinierend"}
        ],
        "takeaway": "Ersetzen Sie 'sehr': überaus, höchst, ungemein, denkbar, zutiefst."
    },
    {
        "id": "b2-fein-101",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Verneinung durch 'weder... noch' mit drei oder mehr Gliedern",
        "rule": "'weder... noch' kann problemlos um weitere 'noch'-Glieder erweitert werden, um mehr als zwei Elemente lückenlos zu verneinen.",
        "formula": "weder [A] noch [B] noch [C] noch [D]",
        "examples": [
            {"de": "Er besitzt weder ein Auto noch ein Fahrrad noch ein Monatsticket für die Bahn.", "en": "He owns neither a car nor a bike nor a monthly ticket for the train.", "breakdown": "Dreigliedrige Negation mit weder... noch... noch"},
            {"de": "In der verlassenen Hütte gab es weder Strom noch fließendes Wasser noch Heizung.", "en": "In the abandoned hut there was neither electricity nor running water nor heating.", "breakdown": "weder... noch... noch"},
            {"de": "Die Konferenz bot weder interessante Vorträge noch gutes Essen noch brauchbare Kontakte.", "en": "The conference offered neither interesting talks nor good food nor useful contacts.", "breakdown": "vollständige Dreifachverneinung"},
            {"de": "Sie verspürte weder Wut noch Angst noch Mitleid gegenüber dem Täter.", "en": "She felt neither anger nor fear nor pity toward the perpetrator.", "breakdown": "Gefühlsaufzählung"}
        ],
        "takeaway": "'weder A noch B noch C' ermöglicht elegante mehrgliedrige Gesamtausschlüsse."
    },
    {
        "id": "b2-fein-102",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Textstrukturierung: Erstens, zweitens, schließlich, zusammenfassend",
        "rule": "Strukturierungsformeln garantieren einen roten Faden in Aufsätzen, Präsentationen und mündlichen Prüfungen: Erstens... Zweitens... Ein weiterer Aspekt ist... Nicht zuletzt... Zusammenfassend lässt sich sagen...",
        "formula": "Erstens ... | Darüber hinaus ... | Nicht zuletzt ... | Abschließend ...",
        "examples": [
            {"de": "Erstens spart die Digitalisierung Papier; zweitens beschleunigt sie Verwaltungsprozesse.", "en": "Firstly, digitalization saves paper; secondly, it accelerates administrative processes.", "breakdown": "Klassische Gliederung"},
            {"de": "Darüber hinaus muss betont werden, dass auch der Datenschutz gewahrt bleiben muss.", "en": "Furthermore, it must be emphasized that data protection must also be preserved.", "breakdown": "ergänzender Aspekt"},
            {"de": "Nicht zuletzt spielt auch der finanzielle Rahmen eine ausschlaggebende Rolle.", "en": "Not least, the financial framework also plays a decisive role.", "breakdown": "Schlüsselargument am Ende"},
            {"de": "Zusammenfassend lässt sich festhalten, dass die Vorteile die Risiken deutlich überwiegen.", "en": "In summary it can be stated that the advantages clearly outweigh the risks.", "breakdown": "Fazit-Formulierung"}
        ],
        "takeaway": "Prüfer lieben klare Diskursmarker: Erstens, darüber hinaus, nicht zuletzt, zusammenfassend."
    },
    {
        "id": "b2-fein-103",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Konditionale Inversion ohne 'wenn' im gehobenen B2-Stil",
        "rule": "Bedingungssätze können ohne 'wenn' oder 'falls' formuliert werden, indem das finite Verb an Position 1 rückt. Im Hauptsatz folgt meist 'so' oder 'dann'.",
        "formula": "[Verb an Position 1] + Subjekt + ..., (so / dann) + Verb + Subjekt...",
        "examples": [
            {"de": "Sollten Sie weitere Fragen haben, so zögern Sie bitte nicht, uns zu kontaktieren.", "en": "Should you have further questions, please do not hesitate to contact us.", "breakdown": "Sollten Sie... haben = Wenn Sie haben sollten"},
            {"de": "Hätte ich mehr Zeit gehabt, wäre meine Präsentation noch fundierter ausgefallen.", "en": "Had I had more time, my presentation would have turned out even more substantiated.", "breakdown": "Hätte ich... gehabt"},
            {"de": "Wäre das Wetter schöner gewesen, hätten wir die Feier im Garten veranstaltet.", "en": "Had the weather been nicer, we would have organized the party in the garden.", "breakdown": "Wäre das Wetter... gewesen"},
            {"de": "Bedarf es einer Verlängerung der Frist, so muss ein schriftlicher Antrag vorliegen.", "en": "Should there be need for an extension of the deadline, a written application must be at hand.", "breakdown": "Bedarf es... so muss..."}
        ],
        "takeaway": "Verb-Erst-Konditionalsätze ('Sollten Sie...', 'Hätten wir...') signalisieren souveräne Stilsicherheit."
    },
    {
        "id": "b2-fein-104",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "Konjunktionen mit doppelter Bedeutung: da, während, bis",
        "rule": "Fortgeschrittene Lerner müssen die Mehrdeutigkeit zentraler Konjunktionen beherrschen: 'da' = kausal (weil) oder lokal (dort); 'während' = temporal (zur selben Zeit) oder adversativ (im Gegensatz dazu); 'bis' = temporal (Endpunkt) oder lokal (bis nach Berlin).",
        "formula": "Kontext bestimmt die Funktion: kausal vs. lokal / temporal vs. adversativ",
        "examples": [
            {"de": "Kausal: Da der Zug ausfiel, kam ich zu spät. | Lokal: Da drüben steht dein Koffer.", "en": "Causal: Since the train was cancelled, I arrived late. | Local: Over there stands your suitcase.", "breakdown": "da kausal vs. da lokal"},
            {"de": "Temporal: Während ich kochte, las er ein Buch.", "en": "Temporal: While I was cooking, he read a book.", "breakdown": "zeitliche Gleichzeitigkeit"},
            {"de": "Adversativ: Im Norden regnete es, während im Süden die Sonne schien.", "en": "Adversative: In the north it rained, while in the south the sun shone.", "breakdown": "gegensätzliche Gegenüberstellung"},
            {"de": "Temporal: Wir warten, bis der Regen aufhört.", "en": "Temporal: We wait until the rain stops.", "breakdown": "zeitliche Grenze"}
        ],
        "takeaway": "Prüfe stets den Kontext: Dient 'während' der Zeitangabe oder einem Kontrast?"
    },
    {
        "id": "b2-fein-105",
        "level": "B2",
        "category": "Feinschliff & Stilistik",
        "title": "B2-Meisterschaft: Die 5 Säulen des stilsicheren Deutschs",
        "rule": "Ein meisterhafter B2-Sprachstil vereint 5 Säulen: 1. Präziser Satzbau mit Inversion und flexibler Satzklammer, 2. Gekonnter Einsatz von Funktionsverbgefügen, 3. Ausgewogene Balance zwischen Nominalstil und lebendigem Verbalstil, 4. Subjektive Modalverben zur Nuancierung, 5. Vielfältige Konnektoren ohne Wiederholungen.",
        "formula": "Topologie + FVG + Nominal/Verbalstil-Balance + Subjektive Modalverben + Konnektorenvielfalt",
        "examples": [
            {"de": "Nach gründlicher Abwägung aller Optionen traf der Aufsichtsrat die Entscheidung, die Investitionen zu verdoppeln.", "en": "After thorough weighing of all options, the supervisory board made the decision to double investments.", "breakdown": "Nominalstil (nach gründlicher Abwägung) + FVG (Entscheidung treffen)"},
            {"de": "Der Gesetzentwurf dürfte nach hitzigen Debatten noch in dieser Sitzungswoche verabschiedet werden.", "en": "The bill is likely to be passed in this session week after heated debates.", "breakdown": "subjektives dürfte + Passiv"},
            {"de": "Infolgedessen traten die neuen Bestimmungen unverzüglich in Kraft, wenngleich Kritik laut wurde.", "en": "As a result, new provisions took effect immediately, although criticism was voiced.", "breakdown": "Infolgedessen (Inversion) + FVG in Kraft treten + wenngleich (Konzessiv)"},
            {"de": "Sollten sich die Rahmenbedingungen ändern, so behalten wir uns vor, den Vertrag anzupassen.", "en": "Should conditions change, we reserve the right to adapt the contract.", "breakdown": "Konditionale Inversion + Infinitivgruppe"}
        ],
        "takeaway": "Kombinieren Sie diese Techniken für flüssiges, professionelles und fehlerfreies Deutsch auf B2-Niveau."
    }
]

def main():
    os.makedirs("deutsche/data", exist_ok=True)
    out_file = "deutsche/data/b2.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// German Grammar B2 Dataset - 105 comprehensive topics\n")
        f.write("// Original pedagogical examples (no examples copied from reference PDF)\n")
        f.write("window.GERMAN_DATA_B2 = ")
        json.dump(topics, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"✅ Generated {out_file} with {len(topics)} topics!")

if __name__ == "__main__":
    main()
