#!/usr/bin/env python3
"""
Generator for C1 German Grammar Dataset (105 comprehensive topics)
Ensures 100% original pedagogical examples (no examples from deutsche/german.pdf).
Level: C1 (Goethe-Zertifikat C1 / telc Deutsch C1 Hochschule / Advanced German)
"""
import json
import os

topics = [
    # 1-15: Satztopologie & Erweiterte Felderlehre
    {
        "id": "c1-top-01",
        "level": "C1",
        "category": "Satztopologie & Felderlehre",
        "title": "Die deutsche Satztopologie: Vorfeld, linke Satzklammer, Mittelfeld, rechte Satzklammer, Nachfeld",
        "rule": "Das topologische Stellungsfeldermodell analysiert den deutschen Satzaufbau anhand der Satzklammer. Die linke Klammer enthält das finite Verb (im Hauptsatz) oder die Konjunktion (im Nebensatz); die rechte Klammer enthält infinite Verbteile oder das finite Verb (im Nebensatz). Dazwischen liegt das Mittelfeld, davor das Vorfeld, danach das Nachfeld.",
        "formula": "[Vorfeld] + [LK: Verb/Konn] + [Mittelfeld] + [RK: Verbteil] + [Nachfeld]",
        "examples": [
            {"de": "Erfreulicherweise hat die Kommission den Entwurf gestern einstimmig angenommen, obgleich heftige Proteste laut wurden.", "en": "Gratifyingly, the commission accepted the draft unanimously yesterday, although fierce protests were voiced.", "breakdown": "Vorfeld: Erfreulicherweise | LK: hat | Mittelfeld: die Kommission... | RK: angenommen | Nachfeld: obgleich-Satz"},
            {"de": "Gleich zu Beginn der Sitzung trug die Referentin die neuen Zahlen vor.", "en": "Right at the beginning of the session, the speaker presented the new figures.", "breakdown": "Vorfeld: mehrgliedrige Zeitangabe | LK: trug | RK: vor"},
            {"de": "Dass diese Reform notwendig war, bezweifelt im Ministerium heute niemand mehr.", "en": "That this reform was necessary, no one in the ministry doubts any longer today.", "breakdown": "Vorfeld besetzt durch einen kompletten dass-Objektsatz"},
            {"de": "Mit großem Bedauern haben wir zur Kenntnis genommen, dass die Gespräche gescheitert sind.", "en": "With great regret we noted that discussions had failed.", "breakdown": "Nachfeld enthält den konsekutiven Nebensatz"}
        ],
        "takeaway": "Die Satzklammer (linke & rechte Klammer) bildet das grammatische Rückgrat des deutschen Satzes."
    },
    {
        "id": "c1-top-02",
        "level": "C1",
        "category": "Satztopologie & Felderlehre",
        "title": "Das Vorfeld: Einfache vs. komplexe Vorfeldbesetzung",
        "rule": "Im deutschen Aussagesatz darf standardmäßig genau EIN Satzglied im Vorfeld stehen. Dieses Satzglied kann jedoch eine hochkomplexe Phrase sein (z.B. eine erweiterte Nominalphrase, ein ganzer Nebensatz oder eine Infinitivgruppe).",
        "formula": "[Genau 1 komplexes Satzglied] + finites Verb + Subjekt/Mittelfeld...",
        "examples": [
            {"de": "Die von vielen Ökonomen seit Monaten mit großer Sorge beobachtete Entwicklung der Inflation hat die Zentralbank zu Zinserhöhungen gezwungen.", "en": "The development of inflation, observed with great concern by many economists for months, forced the central bank to raise interest rates.", "breakdown": "Das gesamte komplexe Subjekt steht im Vorfeld vor dem finiten Verb 'hat'"},
            {"de": "Um den Fortbestand des traditionsreichen Instituts zu sichern, spendeten Alumnis beträchtliche Summen.", "en": "In order to secure the continued existence of the storied institute, alumni donated substantial sums.", "breakdown": "Komplette Infinitivgruppe als finales Vorfeld"},
            {"de": "Mit den Stimmen aller Oppositionsfraktionen wurde der Misstrauensantrag verabschiedet.", "en": "With the votes of all opposition parliamentary groups, the motion of no confidence was passed.", "breakdown": "Erweiterte Präpositionalphrase im Vorfeld"},
            {"de": "Schwer gezeichnet von den Strapazen der Expedition, erreichte das Forscherteam das Basislager.", "en": "Heavily marked by the rigors of the expedition, the research team reached base camp.", "breakdown": "Partizipialattribut im Vorfeld"}
        ],
        "takeaway": "Ein Satzglied im Vorfeld kann viele Wörter umfassen, solange es syntaktisch eine geschlossene Einheit bildet."
    },
    {
        "id": "c1-top-03",
        "level": "C1",
        "category": "Satztopologie & Felderlehre",
        "title": "Das Vorfeld: Scheinbare Mehrfachbesetzung und Kontrastfokus",
        "rule": "In gesprochenem oder rhetorisch geschärftem C1-Deutsch treten scheinbare Doppelbesetzungen auf, wenn Adverbien wie 'gestern' und 'noch' gemeinsam eine Informations- oder Kontrasteinheit bilden, oder durch Spaltsätze (Cleft sentences) fokussiert werden.",
        "formula": "[Fokus-Element + Partikel] + finites Verb...",
        "examples": [
            {"de": "Gestern noch galt das Unternehmen als unangefochtener Marktführer; heute steht es vor der Insolvenz.", "en": "Only yesterday the company was considered the unchallenged market leader; today it faces insolvency.", "breakdown": "'Gestern noch' bildet eine semantisch verschmolzene Kontrasteinheit im Vorfeld"},
            {"de": "Ausgerechnet jetzt fällt auch noch der Hauptserver aus.", "en": "Of all times right now, the primary server also fails.", "breakdown": "'Ausgerechnet jetzt' = Partikel + Temporaladverb im Vorfeld"},
            {"de": "Erst nach wiederholten Mahnungen zahlte der säumige Schuldner den fälligen Betrag.", "en": "Only after repeated reminders did the delinquent debtor pay the due amount.", "breakdown": "Fokuspartikel 'Erst' modifiziert die nachfolgende Präpositionalphrase"},
            {"de": "Nicht nur theoretisch, sondern auch praktisch hat sich dieses Modell bestens bewährt.", "en": "Not only theoretically, but also practically has this model proven itself excellently.", "breakdown": "Zweiteilige Kontrastphrase im Vorfeld"}
        ],
        "takeaway": "Partikeln wie 'erst', 'ausgerechnet', 'nicht nur' verschmelzen mit dem Satzglied im Vorfeld."
    },
    {
        "id": "c1-top-04",
        "level": "C1",
        "category": "Satztopologie & Felderlehre",
        "title": "Satztopologie: Die Pronomenabfolge im Mittelfeld",
        "rule": "Treffen mehrere Pronomen im Mittelfeld direkt hinter dem finiten Verb aufeinander, gilt die strikte Abfolge: 1. Subjektpronomen (Nom), 2. Reflexivpronomen (Akk/Dat) oder Akkusativpronomen, 3. Dativpronomen. Merke: 'es' drängt immer nach ganz vorne!",
        "formula": "Verb + Subjekt-Pronomen + es (Akk) + Reflexiv-Pronomen / Dativ-Pronomen",
        "examples": [
            {"de": "Er hat es mir gestern Abend ausführlich am Telefon geschildert.", "en": "He depicted it to me extensively on the phone yesterday evening.", "breakdown": "Er (Nom) + es (Akk) + mir (Dat)"},
            {"de": "Wann hast du es ihm endlich gebeichtet?", "en": "When did you finally confess it to him?", "breakdown": "du (Nom) + es (Akk) + ihm (Dat)"},
            {"de": "Sie hat es sich gründlich überlegt, bevor sie die Stelle kündigte.", "en": "She thought it over thoroughly before resigning from the position.", "breakdown": "es (Akk) vor sich (Reflexiv-Dativ)"},
            {"de": "Wir konnten es uns beim besten Willen nicht erklären.", "en": "We could not explain it to ourselves with the best will in the world.", "breakdown": "es (Akk) vor uns (Reflexiv-Dativ)"}
        ],
        "takeaway": "'es' steht bei Pronominalreihung immer an erster Stelle nach dem Subjekt."
    },
    {
        "id": "c1-top-05",
        "level": "C1",
        "category": "Satztopologie & Felderlehre",
        "title": "Satztopologie: Das Nachfeld und zulässige Ausklammerung",
        "rule": "Das Nachfeld liegt hinter der rechten Satzklammer. Während im modernen Deutsch das Mittelfeld oft dicht besetzt ist, dient die Ausklammerung ins Nachfeld dazu, syntaktischen 'Klammerdruck' abzubauen. Zulässig: Nebensätze, Infinitivgruppen, Vergleiche mit als/wie sowie schwere Präpositionalphrasen.",
        "formula": "Linke Klammer ... Rechte Klammer + [Nachfeld: Vergleich / Infinitiv / Nebensatz / Präpositionalphrase]",
        "examples": [
            {"de": "Er hat viel mehr erreicht in seiner kurzen Amtszeit [als seine Vorgänger in einem Jahrzehnt].", "en": "He achieved much more in his brief term of office than his predecessors in a decade.", "breakdown": "Vergleichsphrase mit als im Nachfeld"},
            {"de": "Die Geschäftsleitung hat sich endlich dazu durchgerungen [, die Gehälter anzupassen].", "en": "Management finally brought itself to adjust salaries.", "breakdown": "Infinitivgruppe im Nachfeld"},
            {"de": "Wir haben stundenlang diskutiert [über die künftige Ausrichtung des Unternehmens].", "en": "We discussed for hours about the future orientation of the enterprise.", "breakdown": "Präpositionalphrase im Nachfeld zur Satzentlastung"},
            {"de": "Niemand hatte damit gerechnet [, dass die Verhandlungen so schnell scheitern würden].", "en": "Nobody had expected that negotiations would fail so quickly.", "breakdown": "dass-Satz im Nachfeld"}
        ],
        "takeaway": "Gezielte Nachfeldbesetzung entspannt überfrachtete deutsche Satzkonstruktionen."
    },

    # 6-25: Erweiterte Partizipialattribute & Gerundiv
    {
        "id": "c1-part-06",
        "level": "C1",
        "category": "Erweiterte Partizipialkonstruktionen",
        "title": "Mehrfach erweiterte Partizipialattribute (Partizip I mit komplexen Angaben)",
        "rule": "Auf C1-Niveau werden aktive Relativsätze in hochverdichtete Partizip-I-Linksattribute verwandelt. Sämtliche adverbialen Bestimmungen (temporal, kausal, modal, lokal) und Präpositionalobjekte stehen VOR dem Partizip I, das direkt vor dem Nomen dekliniert wird.",
        "formula": "Artikel + [Angaben: Te-Ka-Mo-Lo + Objekte] + [Partizip I + Endung] + Bezugsnomen",
        "examples": [
            {"de": "Die [seit Jahren im Berliner Zentrum für internationale Spitzenforschung tätigen] Wissenschaftler publizierten bahnbrechende Ergebnisse.", "en": "The scientists working for years in the Berlin center for international cutting-edge research published ground-breaking results.", "breakdown": "Angaben: seit Jahren (Te), im Zentrum... (Lo), tätigen (Partizip I) + Wissenschaftler"},
            {"de": "Wir verurteilen das [ohne jede Rücksicht auf die Zivilbevölkerung rücksichtslos vordringende] Militärbündnis.", "en": "We condemn the military alliance advancing recklessly without any consideration of the civilian population.", "breakdown": "ohne jede Rücksicht... (Mo) + vordringende (Partizip I)"},
            {"de": "Der [mit hohem finanziellem Einsatz um neue Kunden werbende] Konzern verzeichnete Verluste.", "en": "The corporation advertising with high financial commitment for new clients posted losses.", "breakdown": "mit hohem Einsatz... (Mo) + um Kunden (Objekt) + werbende (Partizip I)"},
            {"de": "Die [täglich über die Grenzen hinweg eng zusammenarbeitenden] Teams steigerten ihre Effizienz.", "en": "The teams cooperating closely across borders on a daily basis increased their efficiency.", "breakdown": "täglich (Te) + über die Grenzen (Lo) + zusammenarbeitenden (Partizip I)"}
        ],
        "takeaway": "Das Partizip I steht immer ganz hinten in der Attributkette direkt vor dem Substantiv."
    },
    {
        "id": "c1-part-07",
        "level": "C1",
        "category": "Erweiterte Partizipialkonstruktionen",
        "title": "Mehrfach erweiterte Partizipialattribute (Partizip II im Passivkontext)",
        "rule": "Passivische Relativsätze werden im gehobenen Wissenschafts- und Amtsdeutsch zu komplexen Partizip-II-Attributen verdichtet. Der Urheber (von/durch) und Begleitumstände werden vorangestellt.",
        "formula": "Artikel + [Urheber/Mittel + Angaben] + [Partizip II + Endung] + Bezugsnomen",
        "examples": [
            {"de": "Der [von der Bundesregierung nach monatelangem Ringen im Bundestag eingebrachte] Gesetzentwurf fand eine knappe Mehrheit.", "en": "The bill introduced by the federal government after months of struggle in the Bundestag found a narrow majority.", "breakdown": "von der Bundesregierung (Urheber) + nach Ringen (Te) + im Bundestag (Lo) + eingebrachte (Partizip II)"},
            {"de": "Die [durch modernste kryptographische Verfahren verschlüsselten] Daten sind vor Spionage geschützt.", "en": "The data encrypted by state-of-the-art cryptographic procedures are protected against espionage.", "breakdown": "durch kryptographische Verfahren (Mittel) + verschlüsselten (Partizip II)"},
            {"de": "Das [aufgrund unzureichender Beweislage vom Richter eingestellte] Verfahren sorgte für Unmut.", "en": "The trial discontinued by the judge due to insufficient evidence caused resentment.", "breakdown": "aufgrund... (Ka) + vom Richter (Urheber) + eingestellte (Partizip II)"},
            {"de": "Alle [vom Architekten handschriftlich signierten] Baupläne wurden im Stadtarchiv hinterlegt.", "en": "All building plans signed by hand by the architect were deposited in city archives.", "breakdown": "vom Architekten handschriftlich signierten"}
        ],
        "takeaway": "Erweitertes Partizip II komprimiert komplexe Passivsätze zu formeller Schriftsprache."
    },
    {
        "id": "c1-part-08",
        "level": "C1",
        "category": "Erweiterte Partizipialkonstruktionen",
        "title": "Das Gerundiv: Partizip I mit 'zu' in allen 4 Kasus",
        "rule": "Das Gerundiv (zu + Infinitiv + -d + Adjektivendung) drückt immer eine zwingende Pflicht oder Möglichkeit im Passiv aus. Es muss in Kasus, Numerus und Genus kongruent mit dem Bezugsnomen dekliniert werden.",
        "formula": "Artikel + [Angaben] + zu + [Infinitivstamm] + -d- + [Kasusendung] + Nomen",
        "examples": [
            {"de": "Nom. M.: Der [unverzüglich zu leistende] Schadenersatz übersteigt die Mittel des Beklagten.", "en": "The compensation for damages to be rendered without delay exceeds the defendant's means.", "breakdown": "der unverzüglich zu leistende Schadenersatz (Nom M: -e)"},
            {"de": "Akk. F.: Wir fordern eine [von unabhängigen Experten zu prüfende] Neukalkulation.", "en": "We demand a recalculation that is to be examined by independent experts.", "breakdown": "eine... zu prüfende Neukalkulation (Akk F: -e)"},
            {"de": "Dat. N.: Nach dem [bis Freitag einzureichenden] Gutachten wird eine Entscheidung fallen.", "en": "Following the expert report to be submitted by Friday, a decision will be rendered.", "breakdown": "dem... einzureichenden Gutachten (Dat N: -en)"},
            {"de": "Gen. Pl.: Wegen der [schwer vorherzusehenden] Marktschwankungen agieren Anleger vorsichtig.", "en": "Because of market fluctuations difficult to predict, investors act cautiously.", "breakdown": "der... schwer vorherzusehenden Schwankungen (Gen Pl: -en)"}
        ],
        "takeaway": "Gerundiv = passivische Pflicht ('muss getan werden') oder Möglichkeit ('kann getan werden')."
    },
    {
        "id": "c1-part-09",
        "level": "C1",
        "category": "Erweiterte Partizipialkonstruktionen",
        "title": "Auflösung komplexer Partizipialattribute in Relativsätze (Rücktransformation)",
        "rule": "Um dichte Fachtexte verständlicher zu machen oder in mündlichen Prüfungen Souveränität zu demonstrieren, muss das erweiterte Partizipialattribut sicher in einen Relativsatz transformiert werden können (und umgekehrt).",
        "formula": "[Art + Partizipialkette + Nomen] <-> [Nomen + , + Relativpronomen + Kette + konjugiertes Verb]",
        "examples": [
            {"de": "Attribut: Die [vom Gutachter beanstandeten] Baumängel führten zum Baustopp.", "en": "Attribute: The construction defects objected to by the expert led to a construction stop.", "breakdown": "Partizipialattribut"},
            {"de": "Relativsatz: Die Baumängel, [die vom Gutachter beanstandet worden waren], führten zum Baustopp.", "en": "Relative clause: The construction defects, which had been objected to by the expert, led to a construction stop.", "breakdown": "Auflösung in passiven Relativsatz"},
            {"de": "Attribut: Ein [stets auf faire Arbeitsbedingungen bedachter] Arbeitgeber bindet Talente.", "en": "Attribute: An employer always mindful of fair working conditions retains talent.", "breakdown": "Adjektivattribut / Partizipialattribut"},
            {"de": "Relativsatz: Ein Arbeitgeber, [der stets auf faire Arbeitsbedingungen bedacht ist], bindet Talente.", "en": "Relative clause: An employer who is always mindful of fair working conditions retains talent.", "breakdown": "Auflösung in aktiven Relativsatz"}
        ],
        "takeaway": "Die Umformung zwischen Partizipialattribut und Relativsatz ist die Königsdisziplin der C1-Grammatik."
    },
    {
        "id": "c1-part-10",
        "level": "C1",
        "category": "Erweiterte Partizipialkonstruktionen",
        "title": "Syntaktische Fallen: Falsch bezogene Partizipialsätze (Dangling Participles)",
        "rule": "Wird ein Partizipialsatz ohne Nomen an den Satzanfang gestellt, MUSS sein unausgesprochenes logisches Subjekt zwingend mit dem grammatischen Subjekt des Hauptsatzes übereinstimmen. Andernfalls entsteht ein schwerer Grammatikfehler.",
        "formula": "Falsch: [Partizip], + [anderes Subjekt] | Richtig: [Partizip], + [identisches Subjekt]",
        "examples": [
            {"de": "Falsch: Auf dem Flughafen gelandet, überkam den Minister eine tiefe Erschöpfung.", "en": "Incorrect: Having landed at the airport, a deep exhaustion overcame the minister.", "breakdown": "Falsch: Nicht die Erschöpfung ist gelandet, sondern der Minister!"},
            {"de": "Korrekt: Auf dem Flughafen gelandet, fühlte der Minister eine tiefe Erschöpfung.", "en": "Correct: Having landed at the airport, the minister felt a deep exhaustion.", "breakdown": "Korrekt: Subjekt 'der Minister' stimmt mit dem Handelnden des Partizips überein"},
            {"de": "Korrekt: Im Labor gründlich analysiert, erwies sich die Substanz als vollkommen harmlos.", "en": "Correct: Analyzed thoroughly in the laboratory, the substance proved to be completely harmless.", "breakdown": "Subjekt 'die Substanz' wurde analysiert"},
            {"de": "Korrekt: Von Zweifeln geplagt, zog sich die Parteichefin aus der Öffentlichkeit zurück.", "en": "Correct: Tormented by doubts, the party leader withdrew from public life.", "breakdown": "Subjekt 'die Parteichefin' war geplagt"}
        ],
        "takeaway": "Prüfe bei freistehenden Partizipialsätzen immer: Wer handelt? Das Subjekt muss übereinstimmen!"
    },

    # 11-25: Hypothetische Satzgefüge & Konjunktiv II
    {
        "id": "c1-hyp-11",
        "level": "C1",
        "category": "Gehobene Konditionalsätze & Konjunktiv",
        "title": "Konditionale Gefüge ohne 'wenn' mit finitem Verb an Position 1",
        "rule": "Im literarischen und akademischen Deutsch wird die Konjunktion 'wenn' oder 'falls' häufig weggelassen. Das finite Verb rückt an Position 1 des Vordersatzes; der Nachsatz beginnt obligatorisch mit dem Korrelat 'so' oder 'dann'.",
        "formula": "[Verb im Konjunktiv II / Indikativ] + Subjekt + ..., [so / dann] + finites Verb...",
        "examples": [
            {"de": "Hätte das Krisenmanagement früher reagiert, so wären die verheerenden Schäden vermeidbar gewesen.", "en": "Had crisis management reacted earlier, the devastating damages would have been avoidable.", "breakdown": "Hätte... reagiert (Verb an Pos 1) -> so wären... (Nachsatz)"},
            {"de": "Wäre der Zeuge vor Gericht erschienen, so hätte der Prozess heute abgeschlossen werden können.", "en": "Had the witness appeared in court, the trial could have been concluded today.", "breakdown": "Wäre... erschienen -> so hätte..."},
            {"de": "Sollte es wider Erwarten zu Komplikationen kommen, so bitten wir um unverzügliche Benachrichtigung.", "en": "Should complications arise contrary to expectations, we ask for immediate notification.", "breakdown": "Sollte es... kommen -> so bitten wir"},
            {"de": "Bedarf es einer weiteren Erklärung, so stehe ich Ihnen jederzeit gern zur Verfügung.", "en": "Should there be need for further explanation, I am gladly at your disposal at any time.", "breakdown": "Bedarf es... so stehe ich"}
        ],
        "takeaway": "Verb-Erst-Konditionalsätze mit anschließendem 'so' sind das Markenzeichen akademischer Stilsicherheit."
    },
    {
        "id": "c1-hyp-12",
        "level": "C1",
        "category": "Gehobene Konditionalsätze & Konjunktiv",
        "title": "Irrealer Konjunktiv II mit Modalverben in der Vergangenheit (Doppelter Infinitiv)",
        "rule": "Im Konjunktiv II der Vergangenheit mit Modalverb bildet das Hilfsverb 'hätte' die finite Form, während am Satzende zwei Infinitive stehen: Infinitiv des Vollverbs + Infinitiv des Modalverbs (Ersatzinfinitiv).",
        "formula": "hätte + ... + Vollverb-Infinitiv + Modalverb-Infinitiv",
        "examples": [
            {"de": "Der Chirurg hätte den Eingriff nicht ohne vorherige Narkose durchführen dürfen.", "en": "The surgeon should not have been permitted to perform the procedure without prior anesthesia.", "breakdown": "hätte durchführen dürfen (Ersatzinfinitiv)"},
            {"de": "Wir hätten die Sicherheitswarnungen der IT-Abteilung viel ernster nehmen müssen.", "en": "We ought to have taken the IT department's security warnings much more seriously.", "breakdown": "hätten nehmen müssen"},
            {"de": "Er hätte die vertraulichen Unterlagen vor dem Hackerangriff besser sichern können.", "en": "He could have better secured the confidential files before the hacker attack.", "breakdown": "hätte sichern können"},
            {"de": "Sie hätten den Vertrag unter diesen Bedingungen niemals unterzeichnen sollen.", "en": "They should never have signed the contract under these conditions.", "breakdown": "hätten unterzeichnen sollen"}
        ],
        "takeaway": "Doppelter Infinitiv: 'hätte machen können / müssen / dürfen' am Satzende."
    },
    {
        "id": "c1-hyp-13",
        "level": "C1",
        "category": "Gehobene Konditionalsätze & Konjunktiv",
        "title": "Konjunktiv II mit Ersatzinfinitiv im Nebensatz (Sonderstellung des Hilfsverbs)",
        "rule": "Tritt eine Konstruktion mit doppeltem Infinitiv im Nebensatz auf, kann das finite Hilfsverb 'hätte' aus rhythmischen Gründen NICHT ganz ans Satzende wandern! Es rückt vor die beiden Infinitive!",
        "formula": "..., dass + Subjekt + ... + hätte + Vollverb-Infinitiv + Modalverb-Infinitiv",
        "examples": [
            {"de": "Es ist bedauerlich, dass die Geschäftsführung das Desaster [hätte verhindern können].", "en": "It is regrettable that management could have prevented the disaster.", "breakdown": "'hätte' steht VOR 'verhindern können' (nicht 'verhindern gekonnt hätte'!)"},
            {"de": "Wir wissen alle, dass man dieses heikle Thema früher [hätte ansprechen müssen].", "en": "We all know that one ought to have addressed this delicate topic earlier.", "breakdown": "hätte ansprechen müssen"},
            {"de": "Er ärgerte sich darüber, dass er den riskanten Vertrag [hätte unterschreiben sollen].", "en": "He was annoyed that he was supposed to have signed the risky contract.", "breakdown": "hätte unterschreiben sollen"},
            {"de": "Es war unklar, ob die Behörde die Baugenehmigung [hätte erteilen dürfen].", "en": "It was unclear whether the authority should have been permitted to grant building permission.", "breakdown": "hätte erteilen dürfen"}
        ],
        "takeaway": "Nebensatz mit Ersatzinfinitiv: Das Hilfsverb 'hätte' springt VOR die beiden Infinitive."
    },
    {
        "id": "c1-hyp-14",
        "level": "C1",
        "category": "Gehobene Konditionalsätze & Konjunktiv",
        "title": "Irreale Vergleiche mit 'als' allein (Verb-Zweit-Stellung)",
        "rule": "Wird der irreale Vergleich mit 'als' statt 'als ob' gebildet, steht das finite Verb im Konjunktiv II (oder I) unmittelbar auf Position 2 direkt hinter 'als'.",
        "formula": "Hauptsatz + , als + [finites Verb im Konjunktiv] + Subjekt...",
        "examples": [
            {"de": "Der Diplomat verhielt sich in der Krisensitzung so, als wüsste er von gar nichts.", "en": "The diplomat behaved in the crisis session as if he knew of nothing at all.", "breakdown": "als wüsste er (Verb wüsste direkt hinter als)"},
            {"de": "Die Kurse an der Börse fielen ins Bodenlose, als stünde ein neuer Weltkrieg bevor.", "en": "Prices on the stock market plummeted bottomlessly as though a new world war were imminent.", "breakdown": "als stünde ein Krieg bevor"},
            {"de": "Sie blickte mich erstaunt an, als hätte sie ein Gespenst gesehen.", "en": "She looked at me astonished as if she had seen a ghost.", "breakdown": "als hätte sie gesehen"},
            {"de": "Er redete ununterbrochen weiter, als sei seine Rede von historischer Bedeutung.", "en": "He kept talking continuously as though his speech were of historic significance.", "breakdown": "als sei... (Konjunktiv I)"}
        ],
        "takeaway": "'als ob' verlangt Verb am Satzende; 'als' allein zieht das konjugierte Verb an Position 2."
    },
    {
        "id": "c1-hyp-15",
        "level": "C1",
        "category": "Gehobene Konditionalsätze & Konjunktiv",
        "title": "Synthetischer Konjunktiv II starker Verben vs. würde-Form",
        "rule": "Auf C1-Niveau wird die umgangssprachliche 'würde'-Ersatzform bei vielen starken Verben vermieden. Man nutzt die originalen synthetischen Formen: fände (finden), gäbe (geben), bliebe (bleiben), träte (treten), nähme (nehmen), ließe (lassen), schlüge (schlagen), zöge (ziehen).",
        "formula": "Präteritumstamm + Umlaut (a,o,u -> ä,ö,ü) + Konjunktivendung (-e, -est, -e, -en, -et, -en)",
        "examples": [
            {"de": "Es gäbe gewiss eine elegantere Lösung für dieses mathematische Theorem.", "en": "There would certainly be a more elegant solution for this mathematical theorem.", "breakdown": "Es gäbe (statt 'Es würde geben')"},
            {"de": "Ich fände es begrüßenswert, wenn wir die Frist um eine Woche verlängerten.", "en": "I would find it welcome if we extended the deadline by a week.", "breakdown": "Ich fände (statt 'Ich würde finden')"},
            {"de": "Bliebe das Wetter am Wochenende stabil, könnten wir die Expedition starten.", "en": "Were the weather to remain stable over the weekend, we could start the expedition.", "breakdown": "Bliebe (statt 'Würde bleiben')"},
            {"de": "Nähme der Vorstand diesen Vorschlag an, träte eine völlig neue Situation ein.", "en": "Were the board to accept this proposal, an entirely new situation would occur.", "breakdown": "Nähme... träte ein (elegante C1-Synthetik)"}
        ],
        "takeaway": "Nähme, gäbe, fände, ließe, bliebe: Synthetischer Konjunktiv II verleiht C1-Texten literarischen Glanz."
    },

    # 16-35: C1 Funktionsverbgefüge (FVG)
    {
        "id": "c1-fvg-16",
        "level": "C1",
        "category": "Gehobene Funktionsverbgefüge (C1)",
        "title": "FVG: in Abrede stellen (leugnen / bestreiten)",
        "rule": "'etwas in Abrede stellen' bedeutet 'eine Tatsache energisch bestreiten oder leugnen'. Häufig mit Negation: 'Niemand kann in Abrede stellen, dass...'",
        "formula": "etwas (Akk) in Abrede stellen",
        "examples": [
            {"de": "Niemand kann in Abrede stellen, dass die Digitalisierung enorme Chancen birgt.", "en": "Nobody can deny that digitalization holds enormous opportunities.", "breakdown": "in Abrede stellen = leugnen / abstreiten"},
            {"de": "Der Minister stellte keineswegs in Abrede, dass Fehler gemacht worden waren.", "en": "The minister by no means denied that mistakes had been made.", "breakdown": "stellte... in Abrede"},
            {"de": "Die Opposition stellte die Wirksamkeit der verabschiedeten Maßnahmen in Abrede.", "en": "The opposition disputed the effectiveness of the adopted measures.", "breakdown": "in Abrede stellen"},
            {"de": "Diesen gravierenden Widerspruch kann man beim besten Willen nicht in Abrede stellen.", "en": "One cannot deny this severe contradiction with the best will in the world.", "breakdown": "in Abrede stellen"}
        ],
        "takeaway": "in Abrede stellen = formell bestreiten oder leugnen."
    },
    {
        "id": "c1-fvg-17",
        "level": "C1",
        "category": "Gehobene Funktionsverbgefüge (C1)",
        "title": "FVG: zu Buche schlagen (finanziell oder quantitativ ins Gewicht fallen)",
        "rule": "'zu Buche schlagen' bedeutet 'als Kostenfaktor, Belastung oder Ertrag spürbar wirksam werden' (to figure in the balance / take a heavy toll).",
        "formula": "mit [Betrag] / spürbar / schwer zu Buche schlagen",
        "examples": [
            {"de": "Die gestiegenen Energiepreise schlagen im laufenden Geschäftsjahr schwer zu Buche.", "en": "Rising energy prices figure heavily in the balance in the current fiscal year.", "breakdown": "schwer zu Buche schlagen = schwere finanzielle Auswirkung haben"},
            {"de": "Die Anschaffung neuer Server schlug mit über 50.000 Euro zu Buche.", "en": "Acquisition of new servers accounted for more than 50,000 euros.", "breakdown": "schlug mit [Betrag] zu Buche"},
            {"de": "Fehlzeiten durch Krankheit schlagen in vielen Betrieben negativ zu Buche.", "en": "Absences due to illness take a negative financial toll in many companies.", "breakdown": "negativ zu Buche schlagen"},
            {"de": "Die Steuereinsparungen werden im nächsten Quartal positiv zu Buche schlagen.", "en": "The tax savings will reflect positively in the books next quarter.", "breakdown": "positiv zu Buche schlagen"}
        ],
        "takeaway": "zu Buche schlagen = finanzielle oder statistische Belastung/Auswirkung darstellen."
    },
    {
        "id": "c1-fvg-18",
        "level": "C1",
        "category": "Gehobene Funktionsverbgefüge (C1)",
        "title": "FVG: ins Gewicht fallen (eine entscheidende Rolle spielen)",
        "rule": "'ins Gewicht fallen' bedeutet 'von ausschlaggebender Bedeutung sein' (to carry weight / be of significant account).",
        "formula": "schwer / kaum / nicht ins Gewicht fallen",
        "examples": [
            {"de": "Bei einer Investition dieser Größenordnung fallen geringe Zinsänderungen kaum ins Gewicht.", "en": "With an investment of this magnitude, minor interest rate changes barely carry weight.", "breakdown": "fallen kaum ins Gewicht = sind unwesentlich"},
            {"de": "Seine langjährige Auslandserfahrung fiel bei der Stellenbesetzung schwer ins Gewicht.", "en": "His many years of foreign experience carried heavy weight in filling the position.", "breakdown": "fiel schwer ins Gewicht = war ausschlaggebend"},
            {"de": "Solche kleineren Abweichungen fallen im Gesamtergebnis nicht weiter ins Gewicht.", "en": "Such minor deviations do not carry further weight in the overall result.", "breakdown": "fallen nicht ins Gewicht"},
            {"de": "Der ökologische Fußabdruck fällt bei Konsumentscheidungen immer stärker ins Gewicht.", "en": "The ecological footprint carries increasingly heavy weight in consumer decisions.", "breakdown": "fällt ins Gewicht"}
        ],
        "takeaway": "ins Gewicht fallen = von großem Einfluss oder maßgebender Bedeutung sein."
    },
    {
        "id": "c1-fvg-19",
        "level": "C1",
        "category": "Gehobene Funktionsverbgefüge (C1)",
        "title": "FVG: Abhilfe schaffen (ein Problem oder einen Mangel beseitigen)",
        "rule": "'Abhilfe schaffen' bedeutet 'wirksame Maßnahmen ergreifen, um einen untragbaren Missstand zu beheben' (to remedy / provide relief).",
        "formula": "Abhilfe schaffen (bei + Dat / gegen + Akk)",
        "examples": [
            {"de": "Die Hausverwaltung muss unverzüglich Abhilfe bei den ständigen Heizungsausfällen schaffen.", "en": "Property management must remedy the persistent heating breakdowns immediately.", "breakdown": "Abhilfe schaffen = den Missstand beheben"},
            {"de": "Gegen den chronischen Lehrermangel kann nur eine grundlegende Bildungsreform Abhilfe schaffen.", "en": "Only a fundamental education reform can provide a remedy against the chronic teacher shortage.", "breakdown": "Abhilfe schaffen gegen"},
            {"de": "Der Gesetzgeber ist gefordert, hier rasch und unbürokratisch Abhilfe zu schaffen.", "en": "The legislature is called upon to provide a remedy here swiftly and unbureaucratically.", "breakdown": "Abhilfe zu schaffen"},
            {"de": "Neue Schalldämpfer schufen Abhilfe gegen den ohrenbetäubenden Maschinenlärm.", "en": "New mufflers provided a remedy against the deafening machine noise.", "breakdown": "schufen Abhilfe"}
        ],
        "takeaway": "Abhilfe schaffen = Mängel abstellen und Abhilfe leisten."
    },
    {
        "id": "c1-fvg-20",
        "level": "C1",
        "category": "Gehobene Funktionsverbgefüge (C1)",
        "title": "FVG: im Widerspruch stehen zu (+ Dat) (widersprechen)",
        "rule": "'im Widerspruch stehen zu' drückt aus, dass zwei Aussagen, Gesetze oder Handlungen logisch unvereinbar sind (to be in contradiction to).",
        "formula": "im Widerspruch stehen zu + Dativ",
        "examples": [
            {"de": "Dieses Vorgehen steht im eklatanten Widerspruch zu den vereinbarten Verfassungsprinzipien.", "en": "This procedure stands in blatant contradiction to agreed constitutional principles.", "breakdown": "im Widerspruch stehen zu + Dativ"},
            {"de": "Die Aussagen des Zeugen standen im offenen Widerspruch zu den Videoaufnahmen.", "en": "The witness's statements stood in open contradiction to the video recordings.", "breakdown": "standen im Widerspruch zu"},
            {"de": "Sein Handeln steht im krassen Widerspruch zu seinen vorgeblichen Idealen.", "en": "His actions stand in stark contradiction to his purported ideals.", "breakdown": "im krassen Widerspruch stehen"},
            {"de": "Wirtschaftswachstum darf nicht im dauerhaften Widerspruch zum Umweltschutz stehen.", "en": "Economic growth must not stand in permanent contradiction to environmental protection.", "breakdown": "im Widerspruch stehen"}
        ],
        "takeaway": "im Widerspruch stehen zu = logisch oder rechtlich unvereinbar sein."
    },
    {
        "id": "c1-fvg-21",
        "level": "C1",
        "category": "Gehobene Funktionsverbgefüge (C1)",
        "title": "FVG: zur Neige gehen (fast aufgebraucht sein)",
        "rule": "'zur Neige gehen' drückt aus, dass Vorräte, finanzielle Reserven, Zeit oder Geduld bald völlig erschöpft sind (to draw to a close / run low).",
        "formula": "etwas geht zur Neige (Subjekt = Vorrat / Zeit / Geduld)",
        "examples": [
            {"de": "Die fossilen Ressourcen unseres Planeten gehen unaufhaltsam zur Neige.", "en": "The fossil resources of our planet are drawing inexorably to a close.", "breakdown": "gehen zur Neige = gehen dem Ende zu"},
            {"de": "Die finanziellen Rücklagen des Startups gingen nach 18 Monaten zur Neige.", "en": "The startup's financial reserves ran low after 18 months.", "breakdown": "gingen zur Neige"},
            {"de": "Unsere Geduld mit diesen ständigen Lieferverzögerungen geht allmählich zur Neige.", "en": "Our patience with these constant delivery delays is gradually running out.", "breakdown": "Geduld geht zur Neige"},
            {"de": "Als das Tageslicht zur Neige ging, brachen die Wanderer die Suche ab.", "en": "When daylight drew to an end, the hikers broke off the search.", "breakdown": "Tageslicht geht zur Neige"}
        ],
        "takeaway": "zur Neige gehen = zu Ende gehen, erschöpft werden."
    },
    {
        "id": "c1-fvg-22",
        "level": "C1",
        "category": "Gehobene Funktionsverbgefüge (C1)",
        "title": "FVG: unter Beweis stellen (beweisen)",
        "rule": "'etwas unter Beweis stellen' bedeutet 'eine Fähigkeit, Kompetenz oder Eigenschaft durch konkrete Taten praktisch demonstrieren' (to prove / demonstrate).",
        "formula": "etwas (Akk) unter Beweis stellen",
        "examples": [
            {"de": "Die Ingenieure stellten ihre Innovationskraft bei diesem Projekt eindrucksvoll unter Beweis.", "en": "The engineers demonstrated their innovative strength impressively in this project.", "breakdown": "unter Beweis stellen = praktisch beweisen"},
            {"de": "Sie hat ihren Mut und ihre Führungsqualitäten in der Krise unter Beweis gestellt.", "en": "She proved her courage and leadership qualities in the crisis.", "breakdown": "unter Beweis gestellt"},
            {"de": "Jetzt gilt es, die Praxistauglichkeit des neuen Algorithmus unter Beweis zu stellen.", "en": "Now it is essential to prove the practical suitability of the new algorithm.", "breakdown": "unter Beweis zu stellen"},
            {"de": "Der Sportler stellte erneut seinen unbändigen Siegeswillen unter Beweis.", "en": "The athlete once again demonstrated his unbridled will to win.", "breakdown": "unter Beweis stellen"}
        ],
        "takeaway": "unter Beweis stellen = handfest belegen und demonstrieren."
    },
    {
        "id": "c1-fvg-23",
        "level": "C1",
        "category": "Gehobene Funktionsverbgefüge (C1)",
        "title": "FVG: Maßnahmen in die Wege leiten (initiieren)",
        "rule": "'Maßnahmen / Schritte in die Wege leiten' bedeutet 'die bürokratischen oder operativen Vorbereitungen für ein Vorhaben offiziell in Gang setzen' (to initiate / set in motion).",
        "formula": "Maßnahmen / Schritte in die Wege leiten",
        "examples": [
            {"de": "Die Behörden haben unverzüglich rechtliche Schritte gegen den Betreiber in die Wege geleitet.", "en": "The authorities initiated legal steps against the operator immediately.", "breakdown": "in die Wege geleitet = in Gang gesetzt"},
            {"de": "Wir müssen konkrete Maßnahmen zur Senkung des CO2-Ausstoßes in die Wege leiten.", "en": "We must initiate concrete measures to reduce CO2 emissions.", "breakdown": "in die Wege leiten"},
            {"de": "Um den Schaden einzudämmen, wurden sofortige Gegenmaßnahmen in die Wege geleitet.", "en": "In order to contain the damage, immediate countermeasures were set in motion.", "breakdown": "Passivierung des FVG"},
            {"de": "Die Reformen wurden bereits vor zwei Jahren in die Wege geleitet.", "en": "The reforms were already initiated two years ago.", "breakdown": "in die Wege geleitet"}
        ],
        "takeaway": "in die Wege leiten = einen Prozess anstoßen und organisieren."
    },
    {
        "id": "c1-fvg-24",
        "level": "C1",
        "category": "Gehobene Funktionsverbgefüge (C1)",
        "title": "FVG: Rechnung tragen (+ Dat) (berücksichtigen / Genüge tun)",
        "rule": "'einer Sache Rechnung tragen' verlangt ein Dativobjekt und bedeutet 'einen Umstand angemessen berücksichtigen und danach handeln' (to take into account / accommodate).",
        "formula": "einer Sache (Dativ) Rechnung tragen",
        "examples": [
            {"de": "Das neue Tarifmodell trägt den gestiegenen Lebenshaltungskosten in vollem Umfang Rechnung.", "en": "The new wage model fully accommodates the increased cost of living.", "breakdown": "trägt den Kosten (Dativ) Rechnung"},
            {"de": "Wir müssen den berechtigten Sorgen der Anwohner in der Stadtplanung Rechnung tragen.", "en": "We must take into account the legitimate concerns of residents in urban planning.", "breakdown": "den Sorgen (Dativ) Rechnung tragen"},
            {"de": "Der Lehrplan trägt den Anforderungen des modernen Arbeitsmarktes nicht ausreichend Rechnung.", "en": "The curriculum does not adequately take into account requirements of the modern job market.", "breakdown": "Rechnung tragen"},
            {"de": "Um den ökologischen Gegebenheiten Rechnung zu tragen, wurde die Trasse verlegt.", "en": "In order to accommodate ecological conditions, the route was relocated.", "breakdown": "Rechnung zu tragen"}
        ],
        "takeaway": "etwas (Dativ!) Rechnung tragen = etwas sorgfältig einkalkulieren und beachten."
    },
    {
        "id": "c1-fvg-25",
        "level": "C1",
        "category": "Gehobene Funktionsverbgefüge (C1)",
        "title": "FVG: in Kauf nehmen (Nachteile bewusst akzeptieren)",
        "rule": "'etwas in Kauf nehmen' bedeutet 'eine unvermeidliche negative Begleiterscheinung oder ein Risiko bewusst akzeptieren, um ein übergeordnetes Ziel zu erreichen' (to accept / put up with).",
        "formula": "etwas (Akk) in Kauf nehmen",
        "examples": [
            {"de": "Wer eine Altbauwohnung mietet, muss oft höhere Heizkosten in Kauf nehmen.", "en": "Whoever rents an old period flat must often accept higher heating costs.", "breakdown": "in Kauf nehmen = Nachteile in Rechnung stellen"},
            {"de": "Der Unternehmer nahm beträchtliche finanzielle Risiken in Kauf, um innovativ zu bleiben.", "en": "The entrepreneur accepted substantial financial risks in order to remain innovative.", "breakdown": "in Kauf nehmen"},
            {"de": "Für einen kürzeren Arbeitsweg nahm sie eine kleinere Wohnfläche gern in Kauf.", "en": "For a shorter commute, she gladly accepted a smaller living space.", "breakdown": "in Kauf nehmen"},
            {"de": "Verluste wurden von der Geschäftsführung billigend in Kauf genommen.", "en": "Losses were knowingly accepted by management.", "breakdown": "billigend in Kauf genommen (juristische Kollokation)"}
        ],
        "takeaway": "in Kauf nehmen = einen Nachteil um des Vorteils willen hinnehmen."
    },

    # 26-45: Gehobene Verbrektion & Echter Genitiv
    {
        "id": "c1-rek-26",
        "level": "C1",
        "category": "Gehobene Rektion & Genitivverben",
        "title": "Echte Genitivverben: entbehren (jeder Grundlage entbehren)",
        "rule": "Das Verb 'entbehren' bedeutet im gehobenen Deutsch 'nicht besitzen / vermissen lassen' und regiert ein Genitivobjekt (entbehrt jeder Grundlage / jedes Sinnes).",
        "formula": "Subjekt + entbehrt + Genitivobjekt",
        "examples": [
            {"de": "Diese abstrusen Gerüchte entbehren jeder sachlichen Grundlage.", "en": "These abstruse rumors lack any factual basis.", "breakdown": "entbehren jeder Grundlage (Genitiv feminin)"},
            {"de": "Seine voreilige Entscheidung entbehrt jeglicher juristischen Vernunft.", "en": "His premature decision lacks any legal reason.", "breakdown": "entbehrt jeglicher Vernunft (Genitiv)"},
            {"de": "Das vorgelegte Konzept entbehrt nicht einer gewissen Eleganz.", "en": "The submitted concept does not lack a certain elegance.", "breakdown": "entbehrt nicht einer Eleganz (Litotes mit Genitiv)"},
            {"de": "Die Anschuldigungen entbehren jedes handfesten Beweises.", "en": "The accusations lack any tangible proof.", "breakdown": "entbehren jedes Beweises (Genitiv maskulin)"}
        ],
        "takeaway": "entbehren + Genitiv = einer Eigenschaft oder Grundlage völlig ermangeln."
    },
    {
        "id": "c1-rek-27",
        "level": "C1",
        "category": "Gehobene Rektion & Genitivverben",
        "title": "Echte Genitivverben: bezichtigen und beschuldigen (jemanden einer Tat bezichtigen)",
        "rule": "Verben der rechtlichen Anklage binden ein Akkusativobjekt (die Person) und ein Genitivobjekt (das Vergehen / die Tat): bezichtigen, beschuldigen, überführen, verdächtigen, anklagen.",
        "formula": "jemanden (Akk) + einer Sache (Genitiv) + bezichtigen / beschuldigen",
        "examples": [
            {"de": "Der Staatsanwalt bezichtigte den Angeklagten der vorsätzlichen Falschaussage.", "en": "The public prosecutor accused the defendant of intentional perjury.", "breakdown": "den Angeklagten (Akk) + der Falschaussage (Genitiv)"},
            {"de": "Man beschuldigte die Whistleblowerin des Landesverrats.", "en": "The whistleblower was accused of high treason.", "breakdown": "die Whistleblowerin (Akk) + des Landesverrats (Genitiv)"},
            {"de": "Die Kriminalpolizei überführte den Tatverdächtigen des Raubüberfalls.", "en": "The criminal investigation department convicted the suspect of robbery.", "breakdown": "überführte... des Raubüberfalls (Genitiv)"},
            {"de": "Niemand darf ohne Beweise eines Verbrechens verdächtigt werden.", "en": "Nobody may be suspected of a crime without evidence.", "breakdown": "eines Verbrechens (Genitiv) verdächtigt werden"}
        ],
        "takeaway": "Akkusativ für die Person, Genitiv für das Verbrechen: 'jemanden der Tat bezichtigen'."
    },
    {
        "id": "c1-rek-28",
        "level": "C1",
        "category": "Gehobene Rektion & Genitivverben",
        "title": "Echte Genitivverben: sich entsinnen (sich erinnern)",
        "rule": "'sich entsinnen' ist ein stilistisch erlesenes Synonym für 'sich erinnern an' und regiert das Genitivobjekt (sich einer Sache/Person entsinnen).",
        "formula": "sich (Akk) + einer Sache / Person (Genitiv) + entsinnen",
        "examples": [
            {"de": "Ich entsinne mich noch lebhaft der dramatischen Ereignisse jener Nacht.", "en": "I still remember vividly the dramatic events of that night.", "breakdown": "entsinne mich + der dramatischen Ereignisse (Genitiv Plural)"},
            {"de": "Der alte Professor entsann sich kaum noch des Namens seines ersten Doktoranden.", "en": "The old professor barely remembered the name of his first doctoral student.", "breakdown": "entsann sich + des Namens (Genitiv maskulin)"},
            {"de": "Kannst du dich jenes denkwürdigen Sommers in Potsdam entsinnen?", "en": "Can you recall that memorable summer in Potsdam?", "breakdown": "dich jenes Sommers (Genitiv) entsinnen"},
            {"de": "Soweit ich mich des Vorfalls entsinne, war die Sicht extrem schlecht.", "en": "As far as I recall the incident, visibility was extremely poor.", "breakdown": "mich des Vorfalls entsinne"}
        ],
        "takeaway": "sich einer Sache entsinnen = gehobenes 'sich erinnern an' mit reinem Genitiv."
    },
    {
        "id": "c1-rek-29",
        "level": "C1",
        "category": "Gehobene Rektion & Genitivverben",
        "title": "Echte Genitivverben: sich bedienen (+ Genitiv) (nutzen / verwenden)",
        "rule": "'sich bedienen' mit reinem Genitiv bedeutet 'ein Werkzeug, eine Sprache oder eine Methode gezielt gebrauchen/einsetzen' (to make use of / utilize).",
        "formula": "sich (Akk) + einer Sache (Genitiv) + bedienen",
        "examples": [
            {"de": "Der Redner bediente sich einer bildhaften und packenden Sprache.", "en": "The speaker made use of a vivid and captivating language.", "breakdown": "bediente sich + einer Sprache (Genitiv feminin)"},
            {"de": "Um das Problem zu lösen, bedienten sich die Forscher künstlicher Intelligenz.", "en": "To solve the problem, the researchers made use of artificial intelligence.", "breakdown": "bedienten sich künstlicher Intelligenz (Genitiv)"},
            {"de": "Die Hacker bedienten sich einer neuartigen Sicherheitslücke im System.", "en": "The hackers exploited a novel security vulnerability in the system.", "breakdown": "bedienten sich einer Sicherheitslücke"},
            {"de": "Er bediente sich unlauterer Methoden, um die Wahl zu gewinnen.", "en": "He made use of unfair methods in order to win the election.", "breakdown": "bediente sich unlauterer Methoden (Genitiv Plural)"}
        ],
        "takeaway": "sich einer Methode bedienen = eine Methode souverän einsetzen."
    },
    {
        "id": "c1-rek-30",
        "level": "C1",
        "category": "Gehobene Rektion & Genitivverben",
        "title": "Echte Genitivverben: bedürfen (brauchen / erfordern)",
        "rule": "'bedürfen' drückt gehobene Notwendigkeit aus und verlangt stets den Genitiv: 'etwas bedarf der Klärung / der Zeit / des Schutzes'.",
        "formula": "Subjekt + bedarf + Genitivobjekt",
        "examples": [
            {"de": "Diese schwerwiegenden Vorwürfe bedürfen einer lückenlosen Aufklärung.", "en": "These grave allegations require complete clarification.", "breakdown": "bedürfen einer Aufklärung (Genitiv feminin)"},
            {"de": "Das diplomatische Parkett bedarf höchsten Fingerspitzengefühls.", "en": "The diplomatic stage requires the highest degree of tact.", "breakdown": "bedarf höchsten Fingerspitzengefühls (Genitiv neutral)"},
            {"de": "Kleine Kinder und hilfsbedürftige Menschen bedürfen unseres besonderen Schutzes.", "en": "Small children and people in need of assistance require our special protection.", "breakdown": "bedürfen unseres Schutzes (Genitiv maskulin)"},
            {"de": "Es bedarf keines langen Nachdenkens, um diesen Schwindel zu durchschauen.", "en": "It requires no long pondering to see through this swindle.", "breakdown": "Es bedarf keines Nachdenkens"}
        ],
        "takeaway": "bedürfen + Genitiv = dringend nötig haben / erfordern."
    },
    {
        "id": "c1-rek-31",
        "level": "C1",
        "category": "Gehobene Rektion & Genitivverben",
        "title": "Verben mit Präposition: insistieren auf (+ Dat) vs. beharren auf (+ Dat)",
        "rule": "'insistieren auf + Dativ' ist das bildungssprachliche Synonym für 'beharren auf' (to insist on). Es signalisiert nachdrückliche Unnachgiebigkeit.",
        "formula": "insistieren auf + Dativ",
        "examples": [
            {"de": "Die Klägerin insistierte hartnäckig auf der Vorlage der Originaldokumente.", "en": "The plaintiff insisted stubbornly on presentation of original documents.", "breakdown": "insistierte auf der Vorlage (Dativ feminin)"},
            {"de": "Wir müssen auf der strikten Einhaltung der Sicherheitsstandards insistieren.", "en": "We must insist on strict adherence to safety standards.", "breakdown": "insistieren auf + Dativ"},
            {"de": "Er insistierte darauf, dass ihm der Betrag bar ausgezahlt werde.", "en": "He insisted that the amount be paid to him in cash.", "breakdown": "insistierte darauf, dass... (Pronominaladverb)"},
            {"de": "Die EU-Kommission insistiert auf der Beachtung von Grundrechten.", "en": "The EU Commission insists on the observance of fundamental rights.", "breakdown": "insistiert auf"}
        ],
        "takeaway": "insistieren auf + Dativ = bildungssprachlich unerschütterlich fordern."
    },
    {
        "id": "c1-rek-32",
        "level": "C1",
        "category": "Gehobene Rektion & Genitivverben",
        "title": "Verben mit Präposition: kulminieren in (+ Dat) (den Höhepunkt erreichen)",
        "rule": "'kulminieren in + Dativ' bedeutet 'nach einer stetigen Steigerung in einem dramatischen Höhepunkt gipfeln' (to culminate in).",
        "formula": "kulminieren in + Dativ",
        "examples": [
            {"de": "Der monatelange Tarifkonflikt kulminierte schließlich in einem landesweiten Streik.", "en": "The month-long collective bargaining dispute finally culminated in a nationwide strike.", "breakdown": "kulminierte in einem Streik (Dativ maskulin)"},
            {"de": "Die Spannungen zwischen den rivalisierenden Fangruppen kulminierten in gewalttätigen Ausschreitungen.", "en": "Tensions between rival fan groups culminated in violent clashes.", "breakdown": "kulminierten in Ausschreitungen (Dativ Plural)"},
            {"de": "Das Theaterstück kulminiert in einer überraschenden Schluss-Szene.", "en": "The play culminates in a surprising final scene.", "breakdown": "kulminiert in einer Szene"},
            {"de": "Die wirtschaftliche Krise kulminierte im Zusammenbruch mehrerer Großbanken.", "en": "The economic crisis culminated in the collapse of several major banks.", "breakdown": "kulminierte im Zusammenbruch"}
        ],
        "takeaway": "kulminieren in + Dativ = gipfeln in / den Höhepunkt finden."
    },
    {
        "id": "c1-rek-33",
        "level": "C1",
        "category": "Gehobene Rektion & Genitivverben",
        "title": "Verben mit Präposition: abzielen auf (+ Akk) (bezwecken)",
        "rule": "'abzielen auf + Akkusativ' bedeutet 'ein bestimmtes strategisches Ziel anvisieren oder beabsichtigen' (to aim at / be targeted at).",
        "formula": "abzielen auf + Akkusativ",
        "examples": [
            {"de": "Die neue Gesetzgebung zielt auf eine spürbare Entlastung von Familien ab.", "en": "The new legislation aims at noticeable relief for families.", "breakdown": "zielt auf eine Entlastung (Akkusativ feminin) ab"},
            {"de": "Seine provokanten Bemerkungen zielten einzig darauf ab, den Redner zu verunsichern.", "en": "His provocative remarks were aimed solely at rattling the speaker.", "breakdown": "zielten darauf ab, ... zu verunsichern"},
            {"de": "Die Kampagne zielt vor allem auf junge Erstwähler ab.", "en": "The campaign aims primarily at young first-time voters.", "breakdown": "zielt auf junge Wähler (Akkusativ Plural) ab"},
            {"de": "Diese drastischen Maßnahmen zielen auf eine rasche Senkung der Inflation ab.", "en": "These drastic measures aim at rapid reduction of inflation.", "breakdown": "zielen auf eine Senkung ab"}
        ],
        "takeaway": "abzielen auf + Akkusativ = die Absicht verfolgen, etwas zu bewirken."
    },
    {
        "id": "c1-rek-34",
        "level": "C1",
        "category": "Gehobene Rektion & Genitivverben",
        "title": "Verben mit Präposition: verleiten zu vs. veranlassen zu (+ Dat)",
        "rule": "'verleiten zu + Dativ' hat fast immer eine negative Konnotation ('zu einer unklugen, unmoralischen oder verbotenen Handlung verführen'). 'veranlassen zu + Dativ' ist dagegen neutral oder formell begründend ('den Anstoß geben / dazu bewegen').",
        "formula": "verleiten zu + Dat (negativ) | veranlassen zu + Dat (neutral/begründend)",
        "examples": [
            {"de": "Schlechte Vorbilder verleiteten den Jugendlichen zu kriminellen Taten.", "en": "Bad role models led the youth into criminal acts.", "breakdown": "verleiteten zu Taten (Dativ Plural, negativ verführen)"},
            {"de": "Die dramatische Verschlechterung der Lage veranlasste den Kanzler zu einer Sondersitzung.", "en": "The dramatic deterioration of the situation prompted the Chancellor to call a special session.", "breakdown": "veranlasste zu einer Sitzung (Dativ feminin, formeller Auslöser)"},
            {"de": "Lassen Sie sich von kurzfristigen Marktschwankungen nicht zu Panikverkäufen verleiten!", "en": "Do not let yourself be seduced into panic selling by short-term market fluctuations!", "breakdown": "verleiten zu"},
            {"de": "Was hat Sie zu diesem drastischen Schritt veranlasst?", "en": "What prompted you to take this drastic step?", "breakdown": "veranlasst zu"}
        ],
        "takeaway": "verleiten zu = verführen (meist Unheil); veranlassen zu = motivieren/bewegen."
    },
    {
        "id": "c1-rek-35",
        "level": "C1",
        "category": "Gehobene Rektion & Genitivverben",
        "title": "Administrative und juristische Präpositionen mit Genitiv: unbeschadet & eingedenk",
        "rule": "'unbeschadet + Genitiv' bedeutet 'ohne Beeinträchtigung von / unberührt von' (without prejudice to). 'eingedenk + Genitiv' bedeutet 'in Erinnerung an / im Bewusstsein von' (mindful of).",
        "formula": "unbeschadet / eingedenk + Genitiv",
        "examples": [
            {"de": "Unbeschadet weitergehender Schadenersatzansprüche bleibt das Recht auf Rücktritt bestehen.", "en": "Without prejudice to further claims for damages, the right of withdrawal remains intact.", "breakdown": "unbeschadet weitergehender Ansprüche (Genitiv Plural)"},
            {"de": "Eingedenk der bitteren Erfahrungen der Vergangenheit schlossen die Staaten ein Verteidigungsbündnis.", "en": "Mindful of the bitter experiences of the past, the states formed a defense alliance.", "breakdown": "eingedenk der Erfahrungen (Genitiv Plural)"},
            {"de": "Unbeschadet des Ergebnisses der Nachzählung gilt das vorläufige Wahlergebnis.", "en": "Without prejudice to the recount outcome, the provisional election result applies.", "breakdown": "unbeschadet des Ergebnisses (Genitiv neutral)"},
            {"de": "Eingedenk seiner großen Verantwortung handelte der Arzt mit äußerster Sorgfalt.", "en": "Mindful of his great responsibility, the doctor acted with utmost care.", "breakdown": "eingedenk seiner Verantwortung"}
        ],
        "takeaway": "unbeschadet = unberührt bleibend; eingedenk = gedenkend / im Bewusstsein."
    },

    # 36-55: Modalpartikeln & Nuancen pragmatischer Sprache
    {
        "id": "c1-prag-36",
        "level": "C1",
        "category": "Pragmatik & Modalpartikel-Kombinationen",
        "title": "Mehrfachpartikeln: 'ja doch', 'halt eben', 'denn auch'",
        "rule": "In geschliffenen C1-Diskursen treten Modalpartikeln oft als Paar auf, um feine psychologische und argumentative Nuancen zu erzeugen: 'ja doch' (nachdrückliche Bekräftigung trotz Zweifel), 'halt eben' (doppelte Schicksalsergebung), 'denn auch' (Bestätigung einer vorangegangenen Erwartung).",
        "formula": "Subjekt + Verb + [Partikel 1 + Partikel 2] + ...",
        "examples": [
            {"de": "Wir haben es ja doch alle im Voraus gewusst, dass der Plan scheitern würde.", "en": "After all, we all knew it in advance, that the plan would fail.", "breakdown": "ja doch = Bekräftigung des gemeinsamen Vorwissens trotz Verdrängung"},
            {"de": "Man kann an den Naturgesetzen halt eben nichts ändern.", "en": "One simply just cannot change the laws of nature.", "breakdown": "halt eben = unverrückbare Faktizität"},
            {"de": "Die Verhandlungen waren zäh; sie führten denn auch zu keinem greifbaren Ergebnis.", "en": "The negotiations were tough; consequently they indeed led to no tangible result.", "breakdown": "denn auch = logische Bestätigung der Befürchtung"},
            {"de": "Er gab sich Mühe, und das Experiment gelang denn auch auf Anhieb.", "en": "He made an effort, and the experiment indeed succeeded on the first try.", "breakdown": "denn auch = wie erhofft"}
        ],
        "takeaway": "Kombinierte Partikeln verankern komplexe Aussagen tief im pragmatischen Kontext."
    },
    {
        "id": "c1-prag-37",
        "level": "C1",
        "category": "Pragmatik & Modalpartikel-Kombinationen",
        "title": "Modalpartikel 'wohl kaum' (Skeptische Abweisung)",
        "rule": "'wohl kaum' verbindet die Vermutungspartikel 'wohl' mit 'kaum' zu einer scharfen, aber formell distanzierten Zurückweisung einer Behauptung (hardly / highly unlikely).",
        "formula": "Das wird wohl kaum ... / Das dürfte wohl kaum ...",
        "examples": [
            {"de": "Dieser unüberlegte Vorschlag wird im Aufsichtsrat wohl kaum eine Mehrheit finden.", "en": "This ill-considered proposal will hardly find a majority on the supervisory board.", "breakdown": "wohl kaum = mit an Sicherheit grenzender Wahrscheinlichkeit nicht"},
            {"de": "Man kann wohl kaum behaupten, die Regierung habe untätig zugesehen.", "en": "One can hardly claim that the government watched idly.", "breakdown": "wohl kaum behaupten"},
            {"de": "Die Reparatur dürfte wohl kaum vor nächster Woche fertig werden.", "en": "The repair is unlikely to be finished before next week.", "breakdown": "dürfte wohl kaum"},
            {"de": "Er wird wohl kaum freiwillig auf seinen Bonus verzichten.", "en": "He will hardly forfeit his bonus voluntarily.", "breakdown": "wohl kaum verzichten"}
        ],
        "takeaway": "'wohl kaum' ist die eleganteste deutsche Formel für 'höchst unwahrscheinlich'."
    },
    {
        "id": "c1-prag-38",
        "level": "C1",
        "category": "Pragmatik & Modalpartikel-Kombinationen",
        "title": "Modalpartikel 'nun einmal' (Unabänderliche Realität)",
        "rule": "'nun einmal' signalisiert, dass ein Zustand zwar bedauerlich oder unbequem sein mag, aber als unverrückbare Tatsache akzeptiert werden muss (it is just the way it is).",
        "formula": "Subjekt + ist / hat / macht + nun einmal + ...",
        "examples": [
            {"de": "Der Winter in Berlin ist nun einmal grau, kalt und regnerisch.", "en": "Winter in Berlin is just gray, cold, and rainy, like it or not.", "breakdown": "nun einmal = unabänderliche Realität"},
            {"de": "Wir müssen uns an die Gesetze halten; das ist nun einmal der Rechtsstaat.", "en": "We must adhere to the laws; that is simply the constitutional state.", "breakdown": "nun einmal"},
            {"de": "Fehler passieren nun einmal, wenn Menschen unter extremem Zeitdruck arbeiten.", "en": "Mistakes simply happen when people work under extreme time pressure.", "breakdown": "passieren nun einmal"},
            {"de": "Er ist nun einmal unser bester Verkäufer, auch wenn er manchmal aneckt.", "en": "He is simply our best salesman, even if he rubs people the wrong way sometimes.", "breakdown": "ist nun einmal"}
        ],
        "takeaway": "'nun einmal' verlangt Realitätssinn und beendet müßige Diskussionen."
    },
    {
        "id": "c1-prag-39",
        "level": "C1",
        "category": "Pragmatik & Modalpartikel-Kombinationen",
        "title": "Fokuspartikeln: ausgerechnet, geschweige, allenfalls, bestenfalls",
        "rule": "Fokuspartikeln heben ein bestimmtes Element im Satz hervor und modifizieren dessen Relevanz: 'ausgerechnet' (ironische Ungunst), 'allenfalls / bestenfalls' (obere Grenze / Beschränkung), 'schlimmstenfalls' (untere Grenze).",
        "formula": "ausgerechnet / allenfalls / bestenfalls + Bezugswort",
        "examples": [
            {"de": "Warum muss ausgerechnet am Tag der Präsentation der Beamer den Geist aufgeben?", "en": "Why of all days does the projector have to give up the ghost on presentation day?", "breakdown": "ausgerechnet am Tag = Betonung des ungünstigen Zeitpunkts"},
            {"de": "Das neue Modell bietet bestenfalls eine marginale Leistungssteigerung.", "en": "The new model offers at best a marginal performance improvement.", "breakdown": "bestenfalls = im allerbesten Fall"},
            {"de": "Diese Übergangslösung reicht allenfalls für ein paar Monate.", "en": "This interim solution suffices at most for a couple of months.", "breakdown": "allenfalls = maximal / möglicherweise"},
            {"de": "Schlimmstenfalls müssen wir das gesamte Projekt von Grund auf neu konzipieren.", "en": "In the worst case, we must redesign the entire project from the ground up.", "breakdown": "schlimmstenfalls"}
        ],
        "takeaway": "Fokuspartikeln steuern die Erwartungshaltung des Lesers mit höchster Präzision."
    },
    {
        "id": "c1-prag-40",
        "level": "C1",
        "category": "Pragmatik & Modalpartikel-Kombinationen",
        "title": "Verstärkende Adverbien: schlechterdings, schlichtweg, schier",
        "rule": "Im gehobenen C1-Wortschatz ersetzen 'schlechterdings' (absolut / völlig unmöglich), 'schlichtweg' (ganz einfach) und 'schier' (beinahe / schiere Verzweiflung) einfache Verstärker wie 'total' oder 'vollkommen'.",
        "formula": "schlechterdings unmöglich / schlichtweg falsch / schiere Verzweiflung",
        "examples": [
            {"de": "Ein solcher Eingriff in die Privatsphäre ist schlechterdings unzumutbar.", "en": "Such an encroachment on privacy is utterly unacceptable.", "breakdown": "schlechterdings unzumutbar = unter keinen Umständen akzeptabel"},
            {"de": "Die Behauptung, es gäbe keine Alternativen, ist schlichtweg gelogen.", "en": "The assertion that there were no alternatives is simply a lie.", "breakdown": "schlichtweg = ohne Umschweife"},
            {"de": "Die Bergsteiger standen vor einer schier unüberwindbaren Felswand.", "en": "The mountaineers stood before an almost insurmountable rock face.", "breakdown": "schier unüberwindbar"},
            {"de": "Aus schierer Neugier öffnete er die versiegelte Kiste.", "en": "Out of sheer curiosity, he opened the sealed crate.", "breakdown": "schiere Neugier"}
        ],
        "takeaway": "schlechterdings, schlichtweg und schier verleihen scharfen Urteilen intellektuelle Tiefe."
    },

    # 41-60: Rhetorische Figuren & Stilmittel
    {
        "id": "c1-stil-41",
        "level": "C1",
        "category": "Rhetorik & Stilfiguren",
        "title": "Die Litotes: Doppelte Verneinung zur nachdrücklichen Hervorhebung",
        "rule": "Die Litotes drückt eine Bejahung durch die doppelte Verneinung oder durch die Negation des Gegenteils aus. Dies wirkt vornehm, zurückhaltend und zugleich rhetorisch besonders kraftvoll.",
        "formula": "nicht + un- / nicht ohne / keineswegs unberechtigt",
        "examples": [
            {"de": "Die Bedenken der Anwohner sind keineswegs unberechtigt.", "en": "Residents' concerns are by no means unjustified (= they are very justified).", "breakdown": "keineswegs unberechtigt = vollkommen berechtigt"},
            {"de": "Dieser Entwurf ist nicht uninteressant, bedarf aber noch der Überarbeitung.", "en": "This draft is not uninteresting (= quite interesting), but still requires revision.", "breakdown": "nicht uninteressant"},
            {"de": "Er hat nicht wenig zu diesem glänzenden Gesamterfolg beigetragen.", "en": "He contributed not a little (= a great deal) to this brilliant overall success.", "breakdown": "nicht wenig = sehr viel"},
            {"de": "Das war eine nicht ganz einfache Aufgabe für die jungen Entwickler.", "en": "That was a not entirely easy (= very demanding) task for the young developers.", "breakdown": "nicht ganz einfach"}
        ],
        "takeaway": "Litotes federt Lob oder Kritik diplomatisch ab und verleiht Texten Eleganz."
    },
    {
        "id": "c1-stil-42",
        "level": "C1",
        "category": "Rhetorik & Stilfiguren",
        "title": "Der Chiasmus: Kreuzstellung korrespondierender Satzglieder",
        "rule": "Der Chiasmus spiegelt Satzglieder in zwei aufeinanderfolgenden Teilsätzen spiegelbildlich über Kreuz (AB - BA). Er dient der pointierten Gegenüberstellung von Thesen.",
        "formula": "[Subjekt A + Prädikat B] – [Prädikat B + Subjekt A]",
        "examples": [
            {"de": "Die Kunst ist lang, und kurz ist unser Leben. (Goethe)", "en": "Art is long, and short is our life.", "breakdown": "Subjekt (Kunst) + Adjektiv (lang) vs. Adjektiv (kurz) + Subjekt (Leben)"},
            {"de": "Eng ist die Welt, und das Gehirn ist weit. (Schiller)", "en": "Narrow is the world, and wide is the brain.", "breakdown": "Adjektiv + Nomen vs. Nomen + Adjektiv"},
            {"de": "Wir müssen essen, um zu leben, nicht leben, um zu essen.", "en": "We must eat to live, not live to eat.", "breakdown": "essen -> leben vs. leben -> essen"},
            {"de": "Er liebte die Einsamkeit, doch gemieden wurde er von allen.", "en": "He loved solitude, yet avoided was he by all.", "breakdown": "Subjekt + Verb vs. Verb + Subjekt"}
        ],
        "takeaway": "Chiasmus kreuzt Begriffe und brennt Thesen ins Gedächtnis des Zuhörers."
    },
    {
        "id": "c1-stil-43",
        "level": "C1",
        "category": "Rhetorik & Stilfiguren",
        "title": "Das Paradoxon: Scheinbarer Widerspruch mit tieferer Wahrheit",
        "rule": "Ein Paradoxon stellt eine scheinbar widersinnige oder unlogische Behauptung auf, die bei genauerem Hinsehen eine tiefere philosophische oder praktische Wahrheit offenbart.",
        "formula": "[Widersprüchliche Aussage mit Sinngehalt]",
        "examples": [
            {"de": "Weniger ist oft mehr, wenn es um Software-Architektur und Codezeilen geht.", "en": "Less is often more when it comes to software architecture and lines of code.", "breakdown": "Weniger = Mehr (scheinbarer Widerspruch)"},
            {"de": "Ich weiß, dass ich nichts weiß. (Sokrates)", "en": "I know that I know nothing.", "breakdown": "Wissen über Nicht-Wissen"},
            {"de": "Wer den Frieden will, muss für den Ernstfall rüsten.", "en": "Whoever wants peace must prepare for the emergency.", "breakdown": "Frieden vs. Rüstung"},
            {"de": "Umsonst ist der Tod, und der kostet noch das Leben.", "en": "Death is free, and that still costs life.", "breakdown": "Deutsches Sprichwort"}
        ],
        "takeaway": "Paradoxa zwingen zum Nachdenken und durchbrechen gedankliche Denkmuster."
    },
    {
        "id": "c1-stil-44",
        "level": "C1",
        "category": "Rhetorik & Stilfiguren",
        "title": "Pleonasmus vs. Tautologie im stilsicheren Deutsch",
        "rule": "Ein Pleonasmus häuft sinngleiche Wörter verschiedener Wortarten an (der weiße Schimmel, der nasse Regen, alter Greis). Eine Tautologie verdoppelt gleichwertige Wörter (voll und ganz, nie und nimmer, Art und Weise). Auf C1 gilt: Pleonasmen tilgen, feste Tautologien gezielt als Stilmittel nutzen!",
        "formula": "Pleonasmus (Stilfehler meiden!) vs. Idiomatische Tautologie (erlaubt)",
        "examples": [
            {"de": "Stilfehler: 'Wir trafen uns um 14 Uhr nachmittags.' (nachmittags ist im 14 Uhr schon enthalten!)", "en": "Style error: 'We met at 14 o'clock in the afternoon.'", "breakdown": "Pleonasmus meiden: besser 'um 14 Uhr'"},
            {"de": "Idiomatische Tautologie: Ich stimme Ihnen in dieser Angelegenheit voll und ganz zu.", "en": "Idiomatic tautology: I agree with you fully and entirely in this matter.", "breakdown": "voll und ganz = anerkannte Zwillingsformel"},
            {"de": "Feste Zwillingsformel: Man muss die Sache nach Art und Weise gründlich untersuchen.", "en": "Idiomatic tautology: One must examine the matter thoroughly in manner and mode.", "breakdown": "Art und Weise"},
            {"de": "Stilfehler: 'Das ist eine tote Leiche.' -> Besser: 'Das ist ein Leichnam.'", "en": "Style error: 'That is a dead corpse.' -> Better: 'That is a corpse.'", "breakdown": "Tote Leiche ist pleonastisch"}
        ],
        "takeaway": "Sinnverdoppelungen eliminieren, außer etablierte Zwillingsformeln wie 'klipp und klar'."
    },
    {
        "id": "c1-stil-45",
        "level": "C1",
        "category": "Rhetorik & Stilfiguren",
        "title": "Das Oxymoron: Die Vereinigung zweier sich ausschließender Begriffe",
        "rule": "Ein Oxymoron verknüpft zwei völlig gegensätzliche, widersprüchliche Begriffe zu einer überraschenden Einheit: beredtes Schweigen, offenes Geheimnis, bittersüß, stummer Schrei.",
        "formula": "[Widersprüchliches Adjektiv + Substantiv] (z.B. offenes Geheimnis)",
        "examples": [
            {"de": "Dass der Konzern vor der Übernahme steht, ist in der Branche ein offenes Geheimnis.", "en": "That the conglomerate faces a takeover is an open secret in the industry.", "breakdown": "offenes Geheimnis (Oxymoron)"},
            {"de": "Das beredte Schweigen des Zeugen sprach Bände über seine Schuld.", "en": "The eloquent silence of the witness spoke volumes about his guilt.", "breakdown": "beredtes Schweigen (Schweigen, das viel aussagt)"},
            {"de": "Die Entscheidung hinterließ bei den Mitarbeitern eine bittersüße Freude.", "en": "The decision left the employees with bittersweet joy.", "breakdown": "bittersüß"},
            {"de": "Die plötzliche Stille nach dem Knall war ein ohrenbetäubendes Schweigen.", "en": "The sudden quiet after the bang was a deafening silence.", "breakdown": "ohrenbetäubendes Schweigen"}
        ],
        "takeaway": "Oxymora erzeugen poetische Dichte und faszinierende Spannungsverhältnisse."
    },

    # 46-65: Nuancen deutscher Wirtschafts- und Wissenschaftssprache
    {
        "id": "c1-fach-46",
        "level": "C1",
        "category": "Wissenschafts- & Fachsprache",
        "title": "Konditionale Fügungen: vorbehaltlich, unbeschadet, im Vorgriff auf (+ Genitiv)",
        "rule": "In juristischen und betriebswirtschaftlichen Klauseln präzisieren Genitivpräpositionen Vorbehalte: 'vorbehaltlich + Genitiv' (subject to), 'im Vorgriff auf + Akkusativ' (in anticipation of).",
        "formula": "vorbehaltlich + Genitiv | im Vorgriff auf + Akkusativ",
        "examples": [
            {"de": "Vorbehaltlich der Zustimmung des Aufsichtsrats tritt die Fusion zum 1. Januar in Kraft.", "en": "Subject to approval of the supervisory board, the merger takes effect on January 1st.", "breakdown": "vorbehaltlich der Zustimmung (Genitiv feminin)"},
            {"de": "Im Vorgriff auf die geplante Gehaltsreform zahlte das Unternehmen eine Sonderprämie.", "en": "In anticipation of the planned wage reform, the company paid a special bonus.", "breakdown": "im Vorgriff auf die Reform (Akkusativ)"},
            {"de": "Vorbehaltlich unvorhergesehener wetterbedingter Verzögerungen wird die Brücke im Mai eröffnet.", "en": "Subject to unforeseen weather-related delays, the bridge will open in May.", "breakdown": "vorbehaltlich unvorhergesehener Verzögerungen (Genitiv Plural)"},
            {"de": "Alle Angaben verstehen sich vorbehaltlich etwaiger Satz- oder Druckfehler.", "en": "All information is subject to possible typesetting or printing errors.", "breakdown": "vorbehaltlich etwaiger Druckfehler"}
        ],
        "takeaway": "'vorbehaltlich' sichert Verträge und offizielle Beschlüsse rechtlich ab."
    },
    {
        "id": "c1-fach-47",
        "level": "C1",
        "category": "Wissenschafts- & Fachsprache",
        "title": "Wissenschaftliche Distanzierungsmittel: Es steht zu vermuten / Es lässt sich konstatieren",
        "rule": "In akademischen Arbeiten vermeidet der Autor die Ich-Form und nutzt stattdessen unpersönliche Konstruktionen: 'Es steht zu vermuten, dass...', 'Es lässt sich konstatieren, dass...', 'Aus den Daten erhellt, dass...'",
        "formula": "Es steht zu vermuten / erwarten / befürchten | Es lässt sich festhalten / konstatieren",
        "examples": [
            {"de": "Es lässt sich unschwer konstatieren, dass die bisherige Methodik Mängel aufweist.", "en": "It can readily be stated that the existing methodology exhibits deficiencies.", "breakdown": "lässt sich konstatieren = kann festgestellt werden"},
            {"de": "Aus den vorliegenden Testergebnissen steht zu vermuten, dass der Wirkstoff toxisch ist.", "en": "From available test results it is to be presumed that the active agent is toxic.", "breakdown": "steht zu vermuten = man muss vermuten"},
            {"de": "Zusammenfassend lässt sich festhalten, dass die Hypothese bestätigt wurde.", "en": "In summary it can be maintained that the hypothesis was corroborated.", "breakdown": "lässt sich festhalten"},
            {"de": "Es bleibt abzuwarten, wie sich die Märkte unter Zinsdruck verhalten werden.", "en": "It remains to be seen how markets will behave under interest rate pressure.", "breakdown": "bleibt abzuwarten"}
        ],
        "takeaway": "Akademische Entpersönlichung schützt wissenschaftliche Objektivität."
    },
    {
        "id": "c1-fach-48",
        "level": "C1",
        "category": "Wissenschafts- & Fachsprache",
        "title": "Vergleichende Konnektoren: im Vergleich zu, gegenübergestellt, wohingegen",
        "rule": "Präzise Gegenüberstellungen in Analysen erfordern abwechslungsreiche Konnektoren: 'wohingegen' (im Kontrast dazu), 'im Vergleich zu + Dativ', 'gemessen an + Dativ'.",
        "formula": "wohingegen + Nebensatz | gemessen an + Dativ | im Vergleich zu + Dativ",
        "examples": [
            {"de": "Gemessen an den gewaltigen Ausgaben ist der tatsächliche Ertrag verschwindend gering.", "en": "Measured against the immense expenditures, the actual yield is vanishingly small.", "breakdown": "gemessen an den Ausgaben (Dativ Plural)"},
            {"de": "Die Verkäufe in Europa brachen ein, wohingegen die asiatischen Märkte Rekordgewinne verzeichneten.", "en": "Sales in Europe collapsed, whereas Asian markets posted record profits.", "breakdown": "wohingegen leitet Nebensatz mit Verb am Ende ein"},
            {"de": "Im Vergleich zu den Vorjahreswerten stieg die Mitarbeiterzufriedenheit um 15 Prozent.", "en": "Compared to prior-year figures, employee satisfaction increased by 15 percent.", "breakdown": "im Vergleich zu + Dativ"},
            {"de": "Verglichen mit herkömmlichen Algorithmen arbeitet das neuronale Netz viermal schneller.", "en": "Compared with conventional algorithms, the neural network operates four times faster.", "breakdown": "verglichen mit + Dativ"}
        ],
        "takeaway": "'gemessen an' und 'wohingegen' setzen quantitative und qualitative Maßstäbe."
    },
    {
        "id": "c1-fach-49",
        "level": "C1",
        "category": "Wissenschafts- & Fachsprache",
        "title": "Kausale Nuancen: kraft (+ Genitiv), vermöge (+ Genitiv), geschuldet (+ Dativ)",
        "rule": "'kraft + Genitiv' drückt eine amtliche/rechtliche Vollmacht aus. 'vermöge + Genitiv' bezeichnet eine innere Fähigkeit oder Macht. 'geschuldet + Dativ' (nachgestellt oder vorangestellt) benennt den unentrinnbaren Ursachengrund.",
        "formula": "kraft + Gen | vermöge + Gen | [Ursache im Dativ] geschuldet",
        "examples": [
            {"de": "Kraft seines Amtes als Bundespräsident begnadigte er den Verurteilten.", "en": "By virtue of his office as Federal President, he pardoned the convict.", "breakdown": "kraft seines Amtes (Genitiv neutral)"},
            {"de": "Vermöge seines eisernen Willens überstand der Entdecker die Kälte der Arktis.", "en": "By virtue of his iron will, the explorer survived the cold of the Arctic.", "breakdown": "vermöge seines Willens (Genitiv maskulin)"},
            {"de": "Die Verzögerung war allein den schlechten Witterungsbedingungen geschuldet.", "en": "The delay was solely attributable to the bad weather conditions.", "breakdown": "den Bedingungen (Dativ) geschuldet"},
            {"de": "Geschuldet der anhaltenden Inflation musste der Etat gekürzt werden.", "en": "Due to persisting inflation, the budget had to be curtailed.", "breakdown": "geschuldet + Dativ"}
        ],
        "takeaway": "kraft = rechtliche Macht; vermöge = innere Kraft; geschuldet = zurückzuführen auf."
    },
    {
        "id": "c1-fach-50",
        "level": "C1",
        "category": "Wissenschafts- & Fachsprache",
        "title": "Substantivierte Partizipien im Plural (die Beteiligten, die Vorgesetzten)",
        "rule": "Substantivierte Partizipien bezeichnen im Plural Personengruppen. Sie folgen der schwachen oder starken Adjektivdeklination: die Anwesenden, viele Anwesende, allen Anwesenden, der Kreis der Anwesenden.",
        "formula": "Artikel + großgeschriebenes Partizip mit Adjektivendung",
        "examples": [
            {"de": "Der Schiedsrichter forderte alle Beteiligten zu gegenseitigem Respekt auf.", "en": "The referee called upon all parties involved to show mutual respect.", "breakdown": "alle Beteiligten (Akk Pl: schwache Endung -en)"},
            {"de": "Viele Auszubildende klagen über mangelnde Betreuung im Betrieb.", "en": "Many apprentices complain of lacking supervision in the company.", "breakdown": "viele Auszubildende (Nom Pl: starke Endung -e nach viele)"},
            {"de": "Die Rede stieß bei den Anwesenden auf geteiltes Echo.", "en": "The speech met with mixed reaction among those present.", "breakdown": "bei den Anwesenden (Dat Pl: -en)"},
            {"de": "Der Kreis der Leidtragenden dieser Katastrophe ist unübersehbar groß.", "en": "The circle of sufferers of this catastrophe is immensely large.", "breakdown": "der Leidtragenden (Gen Pl: -en)"}
        ],
        "takeaway": "Nach 'alle/die' folgt -en; nach 'viele/einige' folgt im Nominativ/Akkusativ -e: viele Reisende."
    },

    # 51-70: Subtile semantische Differenzierungen
    {
        "id": "c1-sem-51",
        "level": "C1",
        "category": "Semantische Differenzierung & Nuancen",
        "title": "Semantische Nuancen: scheinbar vs. anscheinend (Feinschliff)",
        "rule": "Ein klassischer Fehler selbst unter Muttersprachlern: 'scheinbar' drückt eine Täuschung aus (es scheint so, ist aber NICHT so). 'anscheinend' drückt eine tatsächliche Vermutung aus (allem Anschein nach ist es tatsächlich so).",
        "formula": "scheinbar = Trugschluss / Fälschung | anscheinend = Vermutete Realität",
        "examples": [
            {"de": "Der Zeuge war scheinbar gelassen, doch sein zitterndes Augenlid verriet seine Panik.", "en": "The witness was ostensibly composed, yet his trembling eyelid betrayed his panic.", "breakdown": "scheinbar = Gelassenheit war nur Täuschung"},
            {"de": "Anscheinend hat der Zug Verspätung, denn die Anzeigetafel springt gerade um.", "en": "Apparently the train is delayed, for the display board is just flipping over.", "breakdown": "anscheinend = Vermutung entspricht den sichtbaren Fakten"},
            {"de": "Das Medikament war scheinbar wirksam, bis die Symptome nach drei Tagen wiederkamen.", "en": "The drug was seemingly effective, until symptoms returned after three days.", "breakdown": "scheinbar = Wirkung war ein Trugschluss"},
            {"de": "Anscheinend hat der Vorstand die Tragweite der Krise nun doch erkannt.", "en": "Apparently the board has now recognized the gravity of the crisis after all.", "breakdown": "anscheinend = es sieht danach aus"}
        ],
        "takeaway": "Merke: 'scheinbar' = Illusion; 'anscheinend' = evidenzbasierte Annahme."
    },
    {
        "id": "c1-sem-52",
        "level": "C1",
        "category": "Semantische Differenzierung & Nuancen",
        "title": "Semantische Nuancen: dasselbe vs. das gleiche im präzisen Diskurs",
        "rule": "'dasselbe' = Identität des Unikats (numerische Identität). 'das gleiche' = Gleichheit zweier separater Exemplare in Form, Farbe oder Art (qualitative Identität).",
        "formula": "dasselbe = ein einziges reales Ding | das gleiche = zwei gleiche Dinge",
        "examples": [
            {"de": "Beide Parteien berufen sich auf denselben Paragrafen des Grundgesetzes.", "en": "Both parties invoke the very same paragraph of the Basic Law.", "breakdown": "denselben = den einen, identischen Textabschnitt"},
            {"de": "Die beiden Diplomaten trugen auf dem Empfang den gleichen Maßanzug.", "en": "Both diplomats wore the same tailored suit at the reception.", "breakdown": "den gleichen = zwei identisch geschneiderte Anzüge"},
            {"de": "Wir nutzen seit Jahren dieselbe Software-Version wie die Zentrale.", "en": "We have been using the same software version as headquarters for years.", "breakdown": "dieselbe Version = exakt identischer Code-Build"},
            {"de": "Zwei Forscher kamen unabhängig voneinander zum gleichen Ergebnis.", "en": "Two researchers arrived independently at the same result.", "breakdown": "zum gleichen = gleicher Befund aus zwei getrennten Versuchen"}
        ],
        "takeaway": "Niemals 'dasselbe' verwenden, wenn zwei getrennte physische Objekte gemeint sind!"
    },
    {
        "id": "c1-sem-53",
        "level": "C1",
        "category": "Semantische Differenzierung & Nuancen",
        "title": "Semantische Nuancen: ökonomisch vs. sparsam vs. wirtschaftlich",
        "rule": "Fachbegriffe müssen differenziert werden: 'sparsam' = wenig verbrauchend (Auto, Person); 'wirtschaftlich' = rentabel, Kosten-Nutzen-optimiert; 'ökonomisch' = die Gesamtwirtschaft betreffend oder die Volkswirtschaftslehre.",
        "formula": "sparsam (Verbrauch) | wirtschaftlich (Rentabilität) | ökonomisch (Wissenschaft/Struktur)",
        "examples": [
            {"de": "Der neue Hybridmotor ist im Stadtverkehr außerordentlich sparsam.", "en": "The new hybrid engine is extraordinarily economical/fuel-efficient in city traffic.", "breakdown": "sparsam = geringer Benzinverbrauch"},
            {"de": "Ein Weiterbetrieb des alten Kraftwerks ist nicht mehr wirtschaftlich.", "en": "Continued operation of the old power plant is no longer economically viable / profitable.", "breakdown": "wirtschaftlich = rentabel"},
            {"de": "Die ökonomische Theorie von Keynes prägt die Fiskalpolitik bis heute.", "en": "Keynes's economic theory shapes fiscal policy to this day.", "breakdown": "ökonomisch = volkswirtschaftlich"},
            {"de": "Wirtschaftliches Handeln bedeutet, mit den vorhandenen Ressourcen das Maximum zu erzielen.", "en": "Economic acting means achieving the maximum with available resources.", "breakdown": "wirtschaftliches Handeln = ökonomisches Prinzip"}
        ],
        "takeaway": "Wähle präzise: sparsam (konsumtiv), wirtschaftlich (profitabel), ökonomisch (theoretisch)."
    },
    {
        "id": "c1-sem-54",
        "level": "C1",
        "category": "Semantische Differenzierung & Nuancen",
        "title": "Semantische Nuancen: sittlich vs. moralisch vs. ethisch",
        "rule": "'ethisch' bezieht sich auf die philosophische Reflexion und Wissenschaft der Ethik; 'moralisch' auf gelebte Verhaltensnormen einer Gesellschaft; 'sittlich' ist der traditionelle, verfassungsrechtliche Begriff (z.B. im Grundgesetz: das Sittengesetz).",
        "formula": "ethisch (philosophisch/theoretisch) | moralisch (sozial/individuell) | sittlich (rechtlich/traditionell)",
        "examples": [
            {"de": "Der Einsatz künstlicher Intelligenz in Waffensystemen wirft grundlegende ethische Fragen auf.", "en": "The use of artificial intelligence in weapon systems raises fundamental ethical questions.", "breakdown": "ethische Fragen = Gegenstand der philosophischen Ethik"},
            {"de": "Es ist ihre moralische Pflicht, Zeugnis über das Gesehene abzulegen.", "en": "It is her moral duty to bear witness to what was seen.", "breakdown": "moralische Pflicht = Gewissensfrage"},
            {"de": "Das Handeln der Angeklagten verstößt gegen die sittliche Ordnung.", "en": "The defendant's action violates the moral/customary order.", "breakdown": "sittliche Ordnung = juristischer Fachterminus"},
            {"de": "Ethische Richtlinien leiten die medizinische Forschung an menschlichen Probanden.", "en": "Ethical guidelines guide medical research on human subjects.", "breakdown": "ethische Richtlinien"}
        ],
        "takeaway": "In C1-Aufsätzen schärfen begriffliche Trennungen die argumentative Präzision."
    },
    {
        "id": "c1-sem-55",
        "level": "C1",
        "category": "Semantische Differenzierung & Nuancen",
        "title": "Verneinende Konjunktionen: ohne dass vs. ohne zu im C1-Feinschliff",
        "rule": "'ohne dass' verlangt verschiedene Subjekte und finites Verb am Satzende. 'ohne zu' erfordert strikte Subjektidentität. Im gehobenen Stil kann 'ohne dass' auch bei gleichem Subjekt stehen, wenn das finite Verb besonders betont wird.",
        "formula": "ohne dass + Subjekt + Verb | ohne + [Erweiterungen] + zu + Infinitiv",
        "examples": [
            {"de": "Die Transaktion wurde abgewickelt, ohne dass die Aufsichtsbehörde Einwände erhob.", "en": "The transaction was executed without the regulatory authority raising objections.", "breakdown": "Subjektwechsel: Transaktion vs. Aufsichtsbehörde -> ohne dass"},
            {"de": "Er verließ das Unternehmen, ohne seine Kollegen über die wahren Gründe zu informieren.", "en": "He left the company without informing his colleagues of the true reasons.", "breakdown": "gleiches Subjekt 'er' -> ohne... zu informieren"},
            {"de": "Sie bestand die Prüfung mit Bravour, ohne dass sie eine einzige Nacht durchgelernt hätte.", "en": "She passed the exam with flying colors without having pulled a single all-nighter.", "breakdown": "ohne dass mit Konjunktiv II zur Hervorhebung"},
            {"de": "Das Gesetz passierte den Bundesrat, ohne dass wesentliche Änderungen vorgenommen wurden.", "en": "The law passed the Bundesrat without substantial amendments being made.", "breakdown": "ohne dass im Passiv"}
        ],
        "takeaway": "Subjektgleichheit = ohne zu; Subjektwechsel = ohne dass."
    },

    # 56-75: Administrative & Essay Writing Structures
    {
        "id": "c1-text-56",
        "level": "C1",
        "category": "Textkohärenz & Aufsatzstrukturen",
        "title": "Aufsatzstruktur: Die dialektische Erörterung (These, Antithese, Synthese)",
        "rule": "Eine C1-Erörterung verlangt dialektische Gliederung: Einleitung mit aktuellem Aufhänger -> These (Pro-Argumente mit Belegen) -> Antithese (Kontra-Argumente) -> Synthese (differenzierte Güterabwägung) -> Schlussperspektive.",
        "formula": "Einleitung -> Argumentkette Pro -> Überleitung -> Argumentkette Kontra -> Synthese",
        "examples": [
            {"de": "Auf der einen Seite sprechen wirtschaftliche Gründe für einen Ausbau des Flughafens; auf der anderen Seite wiegen die Umweltbelastungen schwer.", "en": "On the one hand, economic reasons speak for an expansion of the airport; on the other hand, environmental burdens weigh heavily.", "breakdown": "Klassische Antithese"},
            {"de": "Befürworter führen ins Feld, dass neue Arbeitsplätze entstehen; Kritiker halten dem entgegen, dass die Lebensqualität der Anwohner sinkt.", "en": "Proponents argue that new jobs are created; critics counter that residents' quality of life declines.", "breakdown": "Diskursmarker zur Argumentation"},
            {"de": "Bei genauerer Betrachtung erweist sich der Konflikt jedoch als weniger unüberwindbar, als er zunächst schien.", "en": "Upon closer examination, however, the conflict turns out to be less insurmountable than it initially appeared.", "breakdown": "Überleitung zur Synthese"},
            {"de": "Eine tragfähige Lösung liegt mithin in einem Kompromiss, der beiden Lagern Rechnung trägt.", "en": "A viable solution consequently lies in a compromise accommodating both camps.", "breakdown": "Synthese"}
        ],
        "takeaway": "Dialektische Erörterungen leben von ausgewogenen Gegenüberstellungen und überzeugender Synthese."
    },
    {
        "id": "c1-text-57",
        "level": "C1",
        "category": "Textkohärenz & Aufsatzstrukturen",
        "title": "Konzessive Übergänge: Freilich, ungeachtet dessen, demgegenüber",
        "rule": "Um Gedankengänge elegant zu verbinden, meidet C1 monotones 'aber'. Genutzt werden: 'Freilich' (zwar/zugegeben), 'Ungeachtet dessen' (trotzdem), 'Demgegenüber' (im Kontrast dazu).",
        "formula": "Freilich + Verb ... | Ungeachtet dessen + Verb ... | Demgegenüber + Verb ...",
        "examples": [
            {"de": "Die Reform verspricht Einsparungen. Freilich darf nicht an der Qualität der Lehre gespart werden.", "en": "The reform promises savings. Admittedly, savings must not come at the expense of teaching quality.", "breakdown": "Freilich am Satzanfang = Konzessive Warnung"},
            {"de": "Die Verhandlungen gerieten ins Stocken. Ungeachtet dessen hielten beide Seiten am Zeitplan fest.", "en": "Negotiations stalled. Regardless of that, both sides held firmly to the schedule.", "breakdown": "Ungeachtet dessen = formelles trotzdem"},
            {"de": "Großkonzerne steigerten ihre Gewinne. Demgegenüber kämpfen viele Kleinbetriebe um ihre Existenz.", "en": "Major corporations increased profits. In contrast, many small businesses fight for their existence.", "breakdown": "Demgegenüber = scharfe Gegenüberstellung"},
            {"de": "Der Ansatz ist bestechend logisch. Gleichwohl bleiben offene Fragen.", "en": "The approach is captivatingly logical. Nevertheless, open questions remain.", "breakdown": "Gleichwohl = gehobenes dennoch"}
        ],
        "takeaway": "Freilich, gleichwohl, ungeachtet dessen und demgegenüber heben den Schreibstil sofort auf C1-Niveau."
    },
    {
        "id": "c1-text-58",
        "level": "C1",
        "category": "Textkohärenz & Aufsatzstrukturen",
        "title": "Syntaktische Verdichtung: Partizipialgruppe statt zweier Hauptsätze",
        "rule": "Anstatt zwei einfache Sätze mit 'und' aneinanderzureihen, wird der erste Satz zur Partizipialgruppe verdichtet. Dies erhöht das gedankliche Tempo und die stilistische Dichte.",
        "formula": "Einfach: [Satz 1] und [Satz 2] -> C1: [Partizipialgruppe von Satz 1], + [Satz 2]",
        "examples": [
            {"de": "Einfach: Die Ministerin betrat den Saal und begrüßte die anwesenden Journalisten.", "en": "Simple: The minister entered the hall and greeted the journalists present.", "breakdown": "zwei Hauptsätze mit 'und'"},
            {"de": "C1: Den Saal mit festem Schritt betretend, begrüßte die Ministerin die anwesenden Journalisten.", "en": "C1: Entering the hall with firm step, the minister greeted the journalists present.", "breakdown": "Partizip I im Vorfeld"},
            {"de": "Einfach: Das Gesetz wurde verabschiedet und löste landesweite Proteste aus.", "en": "Simple: The law was passed and triggered nationwide protests.", "breakdown": "zwei passive/aktive Hauptsätze"},
            {"de": "C1: Kaum im Parlament verabschiedet, löste das Gesetz bereits landesweite Proteste aus.", "en": "C1: Barely passed in parliament, the law was already triggering nationwide protests.", "breakdown": "Partizip II verdichtet den ersten Satzteil"}
        ],
        "takeaway": "Partizipialgruppen ersetzen plumpe 'und'-Verbindungen durch flüssigen Rhythmus."
    },
    {
        "id": "c1-text-59",
        "level": "C1",
        "category": "Textkohärenz & Aufsatzstrukturen",
        "title": "Verneinende Einschränkungen: nicht im Entferntesten, beileibe nicht",
        "rule": "Idiomatische Negationsausdrücke wie 'nicht im Entferntesten' (not in the slightest) und 'beileibe nicht' (by no means / far from it) verstärken Argumente kraftvoll.",
        "formula": "nicht im Entferntesten / beileibe nicht + Verb / Adjektiv",
        "examples": [
            {"de": "Die bisherigen Maßnahmen reichen nicht im Entferntesten aus, um die Klimaziele zu erreichen.", "en": "Measures to date do not suffice in the slightest to reach climate targets.", "breakdown": "nicht im Entferntesten ausreichen"},
            {"de": "Das war beileibe keine leichte Entscheidung für den Aufsichtsrat.", "en": "That was by no means an easy decision for the supervisory board.", "breakdown": "beileibe keine leichte Entscheidung"},
            {"de": "Er dachte nicht im Traum daran, seine Machtposition freiwillig aufzugeben.", "en": "He did not dream in the slightest of giving up his power position voluntarily.", "breakdown": "nicht im Traum daran denken"},
            {"de": "Die Krise ist beileibe noch nicht überstanden.", "en": "The crisis is far from over yet.", "breakdown": "beileibe nicht überstanden"}
        ],
        "takeaway": "'nicht im Entferntesten' und 'beileibe nicht' formulieren energischen Widerspruch."
    },
    {
        "id": "c1-text-60",
        "level": "C1",
        "category": "Textkohärenz & Aufsatzstrukturen",
        "title": "Metaphorik im politischen und wirtschaftlichen Diskurs",
        "rule": "Auf C1-Niveau bereichern feste bildhafte Metaphern den Diskurs: 'den Gürtel enger schnallen' (sparen), 'am seidenen Faden hängen' (akut gefährdet sein), 'das Eis brechen' (Spannung abbauen), 'ins offene Messer laufen' (ins Verderben rennen).",
        "formula": "Feste idiomatische Kollokationen in Fachtexten",
        "examples": [
            {"de": "Wegen der drohenden Rezession muss die öffentliche Hand den Gürtel enger schnallen.", "en": "Due to imminent recession, the public sector must tighten its belt.", "breakdown": "den Gürtel enger schnallen = Sparmaßnahmen ergreifen"},
            {"de": "Die Rettung des Traditionsunternehmens hängt gegenwärtig an einem seidenen Faden.", "en": "The rescue of the storied company is currently hanging by a silk thread.", "breakdown": "am seidenen Faden hängen = höchst gefährdet sein"},
            {"de": "Eine humorvolle Bemerkung des Moderators half dabei, das Eis zu brechen.", "en": "A humorous remark by the moderator helped to break the ice.", "breakdown": "das Eis brechen"},
            {"de": "Ohne sorgfältige Prüfung des Vertrags wäre der Gründer sehenden Auges ins offene Messer gelaufen.", "en": "Without careful examination of the contract, the founder would have run knowingly into open knives.", "breakdown": "ins offene Messer laufen"}
        ],
        "takeaway": "Gekonnt dosierte Metaphern machen anspruchsvolle Analysen anschaulich und packend."
    },

    # 61-105: Feinschliff, Zeichensetzung & Gehobene Grammatikdetails
    {
        "id": "c1-det-61",
        "level": "C1",
        "category": "Grammatischer Feinschliff & Syntax",
        "title": "Zeichensetzung bei mehrfachen Satzgefügen (Schachtelsätze entflechten)",
        "rule": "In verschachtelten deutschen Satzgefügen muss jedes Paar aus Haupt- und Nebensatz durch Kommas lückenlos abgegrenzt werden. Faustregel: Für jedes finite Verb existiert eine Satzgrenze. Schachteln müssen geöffnet und wieder geschlossen werden.",
        "formula": "Hauptsatz 1a, [Relativsatz, [weil Nebensatz], Relativsatz Ende], Hauptsatz 1b.",
        "examples": [
            {"de": "Die Verordnung, die, weil die Infektionszahlen drastisch stiegen, eilends verabschiedet worden war, wurde vom Verfassungsgericht gekippt.", "en": "The ordinance that, because infection numbers rose drastically, had been passed hastily, was overturned by the constitutional court.", "breakdown": "Drei Satzebenen: Hauptsatz (Die Verordnung... wurde gekippt), Relativsatz (die... verabschiedet worden war), Kausalsatz (weil... stiegen)"},
            {"de": "Wer behauptet, dass alles, was beschlossen wurde, fehlerfrei sei, verkennt die Realität.", "en": "Whoever claims that everything that was decided was flawless misjudges reality.", "breakdown": "Wer-Satz mit eingebettetem dass-Satz und freiem was-Relativsatz"},
            {"de": "Das Dokument, dessen Echtheit bezweifelt wurde, erwies sich nach genauer Prüfung als Fälschung.", "en": "The document whose authenticity was doubted proved to be a forgery after careful examination.", "breakdown": "Relativsatz im Genitiv sauber abgegrenzt"},
            {"de": "Wir müssen, wenn wir erfolgreich sein wollen, an einem Strang ziehen.", "en": "We must, if we want to be successful, pull in the same direction.", "breakdown": "Eingeschobener Konditionalsatz"}
        ],
        "takeaway": "Prüfe jede Satzklammer: Jeder Nebensatz im Satzinneren braucht ein öffnendes UND ein schließendes Komma."
    },
    {
        "id": "c1-det-62",
        "level": "C1",
        "category": "Grammatischer Feinschliff & Syntax",
        "title": "Der Dativus Ethicus und Dativus Iudicantis (Gehobene Dative)",
        "rule": "Der Dativus Iudicantis drückt den Standpunkt des Urteilenden aus ('Für mich / Nach meinem Urteil': 'Er lief mir zu schnell'). Der Dativus Ethicus drückt die emotionale Anteilnahme des Sprechers an einer Handlung aus ('Falle mir bloß nicht hin!').",
        "formula": "Dativpronomen zur emotionalen oder bewertenden Anteilnahme",
        "examples": [
            {"de": "Das war mir eine viel zu riskante Entscheidung der Geschäftsführung. (Dativus Iudicantis)", "en": "That was far too risky a decision by management to my mind.", "breakdown": "mir drückt das persönliche Urteil aus"},
            {"de": "Komm mir ja nicht zu spät zum Vorstellungsgespräch! (Dativus Ethicus)", "en": "Don't you dare come late to the job interview!", "breakdown": "mir drückt emotionale Betroffenheit/Mahnung aus"},
            {"de": "Das Wasser war dem Schwimmer deutlich zu kalt.", "en": "The water was distinctly too cold for the swimmer.", "breakdown": "dem Schwimmer (Dativus Iudicantis)"},
            {"de": "Dass du mir ja keinen Unfug anstellst!", "en": "Make sure you don't get up to any mischief!", "breakdown": "Dativus Ethicus zur nachdrücklichen Warnung"}
        ],
        "takeaway": "Freie Dative nuancieren die persönliche Haltung des Sprechers zur Aussage."
    },
    {
        "id": "c1-det-63",
        "level": "C1",
        "category": "Grammatischer Feinschliff & Syntax",
        "title": "Gehobene Partizipialwendungen: Abgesehen von, geschweige denn, ausgehend von",
        "rule": "Feste Partizipialformeln fungieren im C1-Deutsch als komplexe Präpositionalglieder: 'abgesehen von + Dat' (apart from), 'ausgehend von + Dat' (based on), 'ungeachtet + Gen' (regardless of).",
        "formula": "abgesehen von + Dat | ausgehend von + Dat | anknüpfend an + Akk",
        "examples": [
            {"de": "Abgesehen von einigen kleineren Tippfehlern ist der Bericht makellos.", "en": "Apart from a few minor typographical errors, the report is immaculate.", "breakdown": "abgesehen von + Dativ"},
            {"de": "Ausgehend von diesen empirischen Befunden entwickelte das Institut ein neues Prognosemodell.", "en": "Starting from these empirical findings, the institute developed a new forecasting model.", "breakdown": "ausgehend von + Dativ"},
            {"de": "Anknüpfend an die gestrige Diskussion möchten wir heute drei Handlungsfelder vertiefen.", "en": "Connecting to yesterday's discussion, we wish to deepen three action fields today.", "breakdown": "anknüpfend an + Akkusativ"},
            {"de": "Vorausgesetzt, die Finanzierung steht, kann der Bau im Herbst beginnen.", "en": "Provided the financing is secured, construction can begin in autumn.", "breakdown": "Vorausgesetzt als konditionale Einleitung"}
        ],
        "takeaway": "Partizipialformeln strukturieren Vorträge und Fachaufsätze hochprofessionell."
    },
    {
        "id": "c1-det-64",
        "level": "C1",
        "category": "Grammatischer Feinschliff & Syntax",
        "title": "Indirekte Rede im Konjunktiv I über längere Textpassagen",
        "rule": "Wird in journalistischen oder juristischen Texten eine längere Aussage indirekt referiert, bleibt der Konjunktiv I über alle Sätze hinweg erhalten. Eine ständige Wiederholung von 'sagte er' entfällt; die Konjunktivform allein signalisiert die Redewiedergabe.",
        "formula": "Konjunktiv I zieht sich durch den gesamten Absatz ohne Redeeinleitungsverben",
        "examples": [
            {"de": "Der Minister wies die Vorwürfe zurück. Es habe zu keinem Zeitpunkt geheime Absprachen gegeben. Die Vorwürfe entbehrten jeder Grundlage. Man werde den Vorfall dennoch lückenlos aufklären.", "en": "The minister rejected the allegations. At no point had there been secret agreements. The allegations lacked any basis. The incident would nevertheless be investigated completely.", "breakdown": "habe gegeben -> entbehrten (K II als Ersatz) -> werde aufklären: Durchgängiger Konjunktiv"},
            {"de": "Die Forscherin legte dar, die Mutation sei hochansteckend. Sie verbreite sich rascher als frühere Varianten, führe aber zu milderen Verläufen.", "en": "The researcher explained the mutation was highly contagious. It spread faster than earlier variants, but led to milder courses.", "breakdown": "sei -> verbreite -> führe (dreifacher Konjunktiv I)"},
            {"de": "Der Sprecher betonte, die Gespräche verliefen konstruktiv. Man habe wichtige Etappenziele erreicht.", "en": "The spokesperson stressed talks were proceeding constructively. Important interim milestones had been achieved.", "breakdown": "verliefen (K II) -> habe erreicht (K I)"},
            {"de": "Sie versicherte, die Lieferketten seien stabil. Es bestehe kein Anlass zur Beunruhigung.", "en": "She assured supply chains were stable. There was no cause for alarm.", "breakdown": "seien -> bestehe"}
        ],
        "takeaway": "Fließender Konjunktiv über ganze Textabsätze ist der Inbegriff journalistischer Redewiedergabe."
    },
    {
        "id": "c1-det-65",
        "level": "C1",
        "category": "Grammatischer Feinschliff & Syntax",
        "title": "Die Ellipse im gehobenen Stil: Stilistische Auslassung",
        "rule": "Eine Ellipse lässt Wörter aus, die aus dem Kontext leicht erschlossen werden können. Im gehobenen Stil vermeidet sie monotone Wiederholungen und erzeugt Pointiertheit.",
        "formula": "[Wortauslassung bei grammatischer Rekonstruierbarkeit]",
        "examples": [
            {"de": "Er widmete sein Leben der Forschung, sie [widmete ihr Leben] der Kunst.", "en": "He dedicated his life to research, she [dedicated her life] to art.", "breakdown": "Verb und Akkusativobjekt im zweiten Satzteil elliptisch eingespart"},
            {"de": "Ende gut, alles gut. (Klassische Sprichwort-Ellipse: Wenn das Ende gut ist...)", "en": "All's well that ends well.", "breakdown": "Vollständiger Verbausfall"},
            {"de": "Je schneller die Lieferung, desto zufriedener [sind] die Kunden.", "en": "The faster the delivery, the more satisfied [are] the customers.", "breakdown": "Auslassung der Kopula 'sind'"},
            {"de": "Erst die Arbeit, dann das Vergnügen.", "en": "First work, then pleasure.", "breakdown": "Prägnante Ellipse"}
        ],
        "takeaway": "Gekonnte Ellipsen straffen den Satz und machen Sprache rhythmisch und dynamisch."
    },
    {
        "id": "c1-det-66",
        "level": "C1",
        "category": "Grammatischer Feinschliff & Syntax",
        "title": "Gehobene Konjunktionen: zumal, geschweige denn, wohingegen",
        "rule": "'zumal' begründet eine verstärkende Begründung ('particularly since / especially as'). Verb steht am Satzende.",
        "formula": "Hauptsatz, zumal + Subjekt + ... + Verb",
        "examples": [
            {"de": "Wir sollten das Angebot annehmen, zumal die Konditionen außergewöhnlich günstig sind.", "en": "We should accept the offer, particularly as conditions are exceptionally favorable.", "breakdown": "zumal leitet verstärkenden Kausalsatz ein"},
            {"de": "Er war kaum auf die Prüfung vorbereitet, zumal er die letzten Wochen krank im Bett gelegen hatte.", "en": "He was barely prepared for the exam, especially since he had been lying sick in bed the last weeks.", "breakdown": "zumal... gelegen hatte"},
            {"de": "Die Kritik wiegt schwer, zumal sie von unabhängigen Sachverständigen geäußert wurde.", "en": "The criticism carries weight, especially as it was voiced by independent experts.", "breakdown": "zumal... geäußert wurde"},
            {"de": "Ein Scheitern können wir uns nicht leisten, zumal die gesamte Firmenzukunft auf dem Spiel steht.", "en": "We cannot afford failure, particularly as the entire company's future is at stake.", "breakdown": "zumal... steht"}
        ],
        "takeaway": "'zumal' liefert das schlagende Zusatzargument in Diskussionen."
    },
    {
        "id": "c1-det-67",
        "level": "C1",
        "category": "Grammatischer Feinschliff & Syntax",
        "title": "Zweiteilige Konnektoren: nicht allein... sondern vielmehr",
        "rule": "'nicht allein / nicht bloß... sondern vielmehr' weist eine unzureichende Erklärung zurück und stellt die eigentliche, tiefere Dimension in den Vordergrund.",
        "formula": "nicht allein [A], sondern vielmehr [B]",
        "examples": [
            {"de": "Das Problem ist nicht allein technischer Natur, sondern vielmehr eine Frage der Unternehmenskultur.", "en": "The problem is not merely of a technical nature, but rather a question of corporate culture.", "breakdown": "sondern vielmehr betont die wahre Dimension"},
            {"de": "Er suchte nicht allein den finanziellen Erfolg, sondern vielmehr gesellschaftliche Anerkennung.", "en": "He sought not merely financial success, but rather societal recognition.", "breakdown": "nicht allein... sondern vielmehr"},
            {"de": "Die Maßnahme dient nicht bloß der Einsparung, sondern vielmehr der Qualitätssicherung.", "en": "The measure serves not merely for savings, but rather for quality assurance.", "breakdown": "sondern vielmehr"},
            {"de": "Es handelt sich nicht bloß um ein Missverständnis, sondern vielmehr um eine bewusste Täuschung.", "en": "It is not merely a misunderstanding, but rather deliberate deception.", "breakdown": "sondern vielmehr"}
        ],
        "takeaway": "'sondern vielmehr' korrigiert und vertieft eine oberflächliche Einschätzung."
    },
    {
        "id": "c1-det-68",
        "level": "C1",
        "category": "Grammatischer Feinschliff & Syntax",
        "title": "Passivvarianten: Die sein + zu Konstruktion im Nebensatz",
        "rule": "In Nebensätzen wandert die Konstruktion 'sein + zu + Infinitiv' mit dem konjugierten Hilfsverb 'sein' an die letzte Position: '..., dass dieser Punkt noch zu klären ist'.",
        "formula": "..., dass + Subjekt + ... + zu + Infinitiv + ist / sind / war / waren",
        "examples": [
            {"de": "Wir dürfen nicht vergessen, dass diese vertraulichen Akten streng unter Verschluss zu halten sind.", "en": "We must not forget that these confidential files are strictly to be kept under lock and key.", "breakdown": "zu halten sind (Passiversatz Notwendigkeit)"},
            {"de": "Es steht fest, dass der historische Ursprung dieses Brauchs nicht mehr zweifelsfrei zu ermitteln ist.", "en": "It is certain that the historical origin of this custom can no longer be determined beyond doubt.", "breakdown": "zu ermitteln ist (Möglichkeit)"},
            {"de": "Der Gutachter beanstandete, dass die Baumängel innerhalb von zwei Wochen zu beheben seien.", "en": "The expert objected that structural defects were to be remedied within two weeks.", "breakdown": "zu beheben seien (Konjunktiv I)"},
            {"de": "Niemand wusste, wie dieses komplexe Rechenproblem zu lösen war.", "en": "Nobody knew how this complex computational problem was to be solved.", "breakdown": "zu lösen war (Vergangenheit)"}
        ],
        "takeaway": "Im Nebensatz schließt die Konstruktion ab mit: '... zu tun ist / sind'."
    },
    {
        "id": "c1-det-69",
        "level": "C1",
        "category": "Grammatischer Feinschliff & Syntax",
        "title": "Nominalphrasen mit partitivem Genitiv (ein Glas besten Weines)",
        "rule": "Nach Maß-, Mengen- und Teilangaben kann im gehobenen Stil ein partitiver Genitiv stehen (ein Schluck kühlen Wassers, ein Glas edlen Weines). Im Alltag steht oft der Nullartikel im Dativ (ein Glas kühles Wasser).",
        "formula": "Mengenangabe + Adjektiv im Genitiv + Nomen im Genitiv",
        "examples": [
            {"de": "Der Wirt schenkte den Gästen ein Glas erlesenen Weines ein.", "en": "The innkeeper poured the guests a glass of exquisite wine.", "breakdown": "ein Glas erlesenen Weines (partitiver Genitiv)"},
            {"de": "Sie genossen einen Teller frischen Gemüses auf der Terrasse.", "en": "They enjoyed a plate of fresh vegetables on the terrace.", "breakdown": "einen Teller frischen Gemüses"},
            {"de": "Er reichte dem erschöpften Wanderer einen Becher klaren Quellwassers.", "en": "He handed the exhausted hiker a cup of clear spring water.", "breakdown": "einen Becher klaren Quellwassers"},
            {"de": "Eine Prise feinen Salzes genügt, um das Gericht abzurunden.", "en": "A pinch of fine salt suffices to round off the dish.", "breakdown": "feinen Salzes"}
        ],
        "takeaway": "Partitiver Genitiv nach Mengenangaben verleiht literarischen Beschreibungen Noblesse."
    },
    {
        "id": "c1-det-70",
        "level": "C1",
        "category": "Grammatischer Feinschliff & Syntax",
        "title": "Subjektlose Passivsätze mit Präpositionalobjekt im Vorfeld",
        "rule": "Bildet ein intransitives Verb mit fester Präposition ein Passiv, hat der Satz kein grammatisches Subjekt. Stellt man das Präpositionalobjekt ins Vorfeld, entfällt das unpersönliche 'Es' vollständig.",
        "formula": "[Präpositionalphrase im Vorfeld] + finites Verb + Mittelfeld...",
        "examples": [
            {"de": "Über dieses brisante Thema wurde im Ausschuss stundenlang gestritten.", "en": "About this volatile topic, there was argument in the committee for hours.", "breakdown": "Über dieses Thema (Präp-Objekt im Vorfeld) -> kein 'Es'!"},
            {"de": "An den Opfern der Katastrophe darf nicht gespart werden.", "en": "On the victims of the catastrophe, savings must not be made.", "breakdown": "An den Opfern im Vorfeld"},
            {"de": "Auf die Einhaltung der Sicherheitsvorschriften wird peinlich genau geachtet.", "en": "To adherence to safety regulations, meticulous attention is paid.", "breakdown": "Auf die Einhaltung im Vorfeld"},
            {"de": "Gegen diese willkürliche Entscheidung wurde sofort Berufung eingelegt.", "en": "Against this arbitrary decision, an appeal was lodged immediately.", "breakdown": "Gegen diese Entscheidung im Vorfeld"}
        ],
        "takeaway": "Präpositionalobjekt im Vorfeld eliminiert hölzerne 'Es'-Konstruktionen im Passiv."
    },

    # 71-85: Redemittel für Präsentationen und universitäre Diskurse
    {
        "id": "c1-univ-71",
        "level": "C1",
        "category": "Akademischer & Universitäre Diskurs",
        "title": "Redemittel: Forschungshypothesen formulieren und begründen",
        "rule": "Wissenschaftliche Hypothesen fordern präzise Formulierungen: 'Die vorliegende Untersuchung geht von der Prämisse aus, dass...', 'Es steht zu vermuten, dass...', 'Die Annahme stützt sich auf...'",
        "formula": "Die Untersuchung geht von der Hypothese aus, dass... | gestützt auf...",
        "examples": [
            {"de": "Die vorliegende Studie geht von der Prämisse aus, dass sozioökonomische Faktoren den Spracherwerb maßgeblich beeinflussen.", "en": "The present study proceeds from the premise that socioeconomic factors significantly influence language acquisition.", "breakdown": "Prämisse formulieren"},
            {"de": "Unsere zentrale These lautet, dass dezentrale Energiesysteme die Netzstabilität nachhaltig verbessern.", "en": "Our central thesis is that decentralized energy systems improve grid stability sustainably.", "breakdown": "These darlegen"},
            {"de": "Diese Annahme stützt sich auf die jüngsten empirischen Erhebungen des statistischen Bundesamtes.", "en": "This assumption is supported by the most recent empirical surveys of the Federal Statistical Office.", "breakdown": "These untermauern"},
            {"de": "Es gilt mithin zu prüfen, inwieweit diese Hypothese der praktischen Überprüfung standhält.", "en": "It is consequently to be tested to what extent this hypothesis withstands practical scrutiny.", "breakdown": "Prüfungsauftrag definieren"}
        ],
        "takeaway": "Wissenschaftliche Formeln schaffen Autorität und akademische Glaubwürdigkeit."
    },
    {
        "id": "c1-univ-72",
        "level": "C1",
        "category": "Akademischer & Universitäre Diskurs",
        "title": "Redemittel: Gegenargumente entkräften (Widerlegung)",
        "rule": "Ein starkes C1-Argument erkennt Einwände an und entkräftet sie sofort: 'Zwar mag eingewendet werden, dass... Dem ist jedoch entgegenzuhalten, dass...', 'Dieser Einwand greift jedoch zu kurz, weil...'",
        "formula": "Zwar wird eingewendet, dass... Doch dem ist entgegenzuhalten, dass...",
        "examples": [
            {"de": "Zwar mag eingewendet werden, dass die Kosten hoch seien; dem ist jedoch entgegenzuhalten, dass die Folgekosten des Nichtstuns ungleich höher ausfallen.", "en": "Although it may be objected that costs are high, it must be countered that the consequential costs of inaction turn out unequally higher.", "breakdown": "Konjunktiv I im Einwand (seien) + Entkräftung im Hauptsatz"},
            {"de": "Dieser Einwand greift jedoch zu kurz, da er die langfristigen Synergieeffekte völlig außer Acht lässt.", "en": "This objection falls short, however, because it completely disregards long-term synergy effects.", "breakdown": "greift zu kurz"},
            {"de": "Auf den ersten Blick erscheint dieses Argument stichhaltig; bei genauerer Analyse erweist es sich jedoch als trügerisch.", "en": "At first glance this argument appears sound; upon closer analysis, however, it proves deceptive.", "breakdown": "Schein vs. Realität"},
            {"de": "Entgegen der weitverbreiteten Auffassung belegen neueste Studien das genaue Gegenteil.", "en": "Contrary to widely held opinion, the latest studies prove the exact opposite.", "breakdown": "Entgegen der Auffassung"}
        ],
        "takeaway": "Einwand anerkennen, mit Konjunktiv I distanzieren und mit harten Fakten widerlegen."
    },
    {
        "id": "c1-univ-73",
        "level": "C1",
        "category": "Akademischer & Universitäre Diskurs",
        "title": "Redemittel: Synthesen ziehen und Fazit ziehen",
        "rule": "Ein überzeugender Schluss fasst die Kernargumente dialektisch zusammen: 'Aus alledem erhellt, dass...', 'Zusammenfassend lässt sich der Befund wie folgt resümieren...', 'Daraus ergibt sich zwingend die Schlussfolgerung...'",
        "formula": "Aus alledem erhellt, dass... | Resümierend lässt sich festhalten...",
        "examples": [
            {"de": "Aus alledem erhellt, dass eine isolierte Betrachtung des Problems den komplexen Zusammenhängen nicht gerecht wird.", "en": "From all this it becomes clear that an isolated consideration of the problem does not do justice to the complex interrelations.", "breakdown": "Aus alledem erhellt, dass..."},
            {"de": "Resümierend lässt sich festhalten, dass die Vorteile die potenziellen Risiken bei weitem überwiegen.", "en": "In summing up it can be maintained that advantages far outweigh potential risks.", "breakdown": "Resümierend"},
            {"de": "Daraus ergibt sich zwingend die Notwendigkeit eines sofortigen politischen Kurswechsels.", "en": "From this arises compellingly the necessity of an immediate political change of course.", "breakdown": "zwingende Notwendigkeit"},
            {"de": "In der Gesamtschau zeigt sich ein differenziertes, aber dennoch klares Bild.", "en": "In overall view, a differentiated yet nonetheless clear picture emerges.", "breakdown": "In der Gesamtschau"}
        ],
        "takeaway": "Am Ende eines C1-Aufsatzes steht eine überzeugende, sachliche Gesamtschau."
    },
    {
        "id": "c1-univ-74",
        "level": "C1",
        "category": "Akademischer & Universitäre Diskurs",
        "title": "Redemittel: Quellen zitieren und Paraphrasieren",
        "rule": "In wissenschaftlichen Arbeiten werden fremde Thesen mit Quellenangaben und Verben der Redewiedergabe eingebunden: 'Wie Müller (2023) überzeugend darlegt...', 'In Anlehnung an die Definition von Weber...', 'Gemäß den Ausführungen von...'",
        "formula": "Wie [Autor] darlegt / ausführt / postuliert, ...",
        "examples": [
            {"de": "Wie Schmidt (2022) überzeugend nachweist, korreliert die Fehlerquote signifikant mit dem Schlafmangel.", "en": "As Schmidt (2022) convincingly proves, the error rate correlates significantly with sleep deprivation.", "breakdown": "Wie [Autor] nachweist"},
            {"de": "In Anlehnung an Habermas' Theorie des kommunikativen Handelns definieren wir Diskurs als...", "en": "Following Habermas's theory of communicative action, we define discourse as...", "breakdown": "In Anlehnung an + Akkusativ"},
            {"de": "Den Ausführungen von Professor Schulz zufolge ist eine Neubewertung der Daten unerlässlich.", "en": "According to the remarks of Professor Schulz, a re-evaluation of data is indispensable.", "breakdown": "Den Ausführungen zufolge (Dativ)"},
            {"de": "Diese These deckt sich mit den jüngsten Forschungsergebnissen der Max-Planck-Gesellschaft.", "en": "This thesis coincides with the latest research findings of the Max Planck Society.", "breakdown": "deckt sich mit"}
        ],
        "takeaway": "Paraphrasieren mit Quellenbezug beweist akademische Reife und Verlässlichkeit."
    },
    {
        "id": "c1-univ-75",
        "level": "C1",
        "category": "Akademischer & Universitäre Diskurs",
        "title": "Redemittel: Diagramme und Statistiken auf C1 beschreiben",
        "rule": "Statistiken werden nicht nur abgelesen, sondern interpretiert und bewertet: 'Das Schaubild veranschaulicht...', 'Auffallend ist die signifikante Diskrepanz zwischen...', 'Die Kurve verzeichnet einen dramatischen Einbruch...', 'Ein Trend zeichnet sich ab...'",
        "formula": "Das Diagramm veranschaulicht | Auffallend ist die Diskrepanz | Einen Einbruch verzeichnen",
        "examples": [
            {"de": "Das vorliegende Säulendiagramm veranschaulicht die Entwicklung der Rohstoffpreise im Zeitraum von 2015 bis 2024.", "en": "The present bar chart illustrates the development of raw material prices in the period from 2015 to 2024.", "breakdown": "veranschaulicht die Entwicklung"},
            {"de": "Besonders auffallend ist die eklatante Diskrepanz zwischen den Ausgaben für Forschung und jenen für Verwaltung.", "en": "Particularly striking is the glaring discrepancy between expenditures for research and those for administration.", "breakdown": "eklatante Diskrepanz"},
            {"de": "Nach einer mehrjährigen Stagnationsphase verzeichneten die Exporte im dritten Quartal einen steilen Aufwärtstrend.", "en": "Following a multi-year stagnation phase, exports recorded a steep upward trend in the third quarter.", "breakdown": "steilen Aufwärtstrend verzeichnen"},
            {"de": "Aus den Daten lässt sich unmissverständlich der Trend zur Urbanisierung ablesen.", "en": "From the data, the trend toward urbanization can be read unmistakably.", "breakdown": "Trend ablesen"}
        ],
        "takeaway": "Prüfer in TestDaF/DSH/telc C1 Hochschule achten auf analytische Bewertung statt reiner Zahlenaufzählung."
    },

    # 76-105: Feinstruktur der gehobenen deutschen Syntax
    {
        "id": "c1-syn-76",
        "level": "C1",
        "category": "Gehobene Syntax & Satzbau",
        "title": "Spaltsätze (Cleft Sentences) zur Fokussierung: Es ist X, der/die...",
        "rule": "Obwohl das Deutsche den Fokus primär über die Vorfeldbesetzung steuert, kann zur dramatischen Zuspitzung ein Spaltsatz mit 'Es ist / war [Fokus-Substantiv], der/die/das...' eingesetzt werden.",
        "formula": "Es ist / war [Fokus-Element], der / die / das / was...",
        "examples": [
            {"de": "Es war der Mut der Bürger, der den Fall der Berliner Mauer herbeiführte.", "en": "It was the courage of citizens that brought about the fall of the Berlin Wall.", "breakdown": "Spaltsatz fokussiert 'der Mut der Bürger'"},
            {"de": "Es sind vor allem die kleinen und mittleren Betriebe, die das Rückgrat der deutschen Wirtschaft bilden.", "en": "It is above all small and medium-sized enterprises that form the backbone of the German economy.", "breakdown": "Fokussierung des Subjekts"},
            {"de": "Es war reine Nachlässigkeit, was zu diesem schwerwiegenden Unfall führte.", "en": "It was sheer negligence that led to this serious accident.", "breakdown": "Spaltsatz mit 'was'"},
            {"de": "Nicht das Geld, sondern die Leidenschaft ist es, was wahre Innovation antreibt.", "en": "Not money, but passion it is that drives true innovation.", "breakdown": "Invertierter Spaltsatz"}
        ],
        "takeaway": "Spaltsätze verleihen Reden und Festschriften dramatischen Nachdruck."
    },
    {
        "id": "c1-syn-77",
        "level": "C1",
        "category": "Gehobene Syntax & Satzbau",
        "title": "Ausklammerung mehrteiliger Prädikate zur Rhythmisierung",
        "rule": "In langen Schachtelsätzen kann die starre Verbendstellung aufgebrochen werden, indem Nebensätze oder vergleichende Fügungen hinter das finite Verb ins Nachfeld gestellt werden, um die Verständlichkeit zu sichern.",
        "formula": "Hauptsatz ... [Partizip II] + [ausgeklammerter Nebensatz / Infinitivsatz]",
        "examples": [
            {"de": "Der Kanzler hat in seiner Rede versprochen [, dass die Steuern für Familien sinken werden].", "en": "The Chancellor promised in his speech that taxes for families will fall.", "breakdown": "dass-Satz hinter das Partizip 'versprochen' gestellt"},
            {"de": "Wir haben uns darauf verständigt [, die Verhandlungen im Januar wiederaufzunehmen].", "en": "We agreed to resume negotiations in January.", "breakdown": "Infinitivgruppe ausgeklammert"},
            {"de": "Er hat viel mehr gearbeitet [als alle seine Kollegen zusammen].", "en": "He worked much more than all his colleagues put together.", "breakdown": "Vergleichsphrase ausgeklammert"},
            {"de": "Die Zeugin konnte sich genau erinnern [an den Mann mit der blauen Jacke].", "en": "The witness could remember precisely the man with the blue jacket.", "breakdown": "Präpositionalphrase im Nachfeld"}
        ],
        "takeaway": "Ausklammerung entlastet die deutsche Satzklammer und verhindert 'Atemnot' beim Lesen."
    },
    {
        "id": "c1-syn-78",
        "level": "C1",
        "category": "Gehobene Syntax & Satzbau",
        "title": "Apostroph-Regeln im Deutschen: Wann der Apostroph gesetzt werden MUSS",
        "rule": "Im Deutschen steht der Apostroph NIEMALS beim regulären Genitiv-s (Peters Auto, nicht Peter's Auto!). Er ist nur zwingend PFLICHT bei Eigennamen, die auf einen Zischlaut (-s, -ss, -ß, -tz, -z, -x) enden und KEINEN Artikel tragen: Max' Fahrrad, Grass' Romane, Marx' Kapital.",
        "formula": "Zischlaut-Name + ' (ohne extra -s!): Johannes' Buch, Felix' Arbeit",
        "examples": [
            {"de": "Thomas' Präsentation war hervorragend strukturiert.", "en": "Thomas's presentation was outstandingly structured.", "breakdown": "Thomas endet auf -s -> erhält nur den Apostroph"},
            {"de": "Wir haben gestern Abend in Klaus' neuem Restaurant gegessen.", "en": "We ate in Klaus's new restaurant yesterday evening.", "breakdown": "Klaus' (Zischlaut)"},
            {"de": "Klaras Vortrag begeisterte alle Zuhörer. (KEIN Apostroph!)", "en": "Klara's lecture thrilled all listeners.", "breakdown": "Klaras ohne Apostroph, da kein Zischlaut"},
            {"de": "Marx' Schriften beeinflussten die europäische Geistesgeschichte tiefgreifend.", "en": "Marx's writings influenced European intellectual history profoundly.", "breakdown": "Marx' (Zischlaut -x)"}
        ],
        "takeaway": "Niemals Deppenapostroph: Annas Auto, aber Felix' Auto."
    },
    {
        "id": "c1-syn-79",
        "level": "C1",
        "category": "Gehobene Syntax & Satzbau",
        "title": "Wortstellung bei 'weder... noch': Satzverbindung vs. Satzgliedverbindung",
        "rule": "Verbindet 'weder... noch' zwei ganze Hauptsätze, verlangt 'noch' zwingend Inversion (finites Verb direkt hinter 'noch'!). Verbindet es nur Satzglieder, bleibt die normale Satzstruktur bestehen.",
        "formula": "Satz 1, noch + [finites Verb] + [Subjekt] + ...",
        "examples": [
            {"de": "Er hat sich nicht entschuldigt, noch zeigte er irgendeine Spur von Reue.", "en": "He did not apologize, nor did he show any trace of remorse.", "breakdown": "noch (Pos 1) + zeigte (Verb Pos 2) + er (Subjekt Pos 3)"},
            {"de": "Die Zeugin erschien nicht vor Gericht, noch ließ sie sich durch einen Anwalt vertreten.", "en": "The witness did not appear in court, nor did she have herself represented by counsel.", "breakdown": "Inversion nach 'noch'"},
            {"de": "Satzglieder: Er trinkt weder Kaffee noch Tee.", "en": "Sentence elements: He drinks neither coffee nor tea.", "breakdown": "einfache Aufzählung ohne Satzinversion"},
            {"de": "Wir konnten das Problem nicht vor Ort lösen, noch fanden wir telefonische Unterstützung.", "en": "We could not solve the problem on site, nor did we find phone support.", "breakdown": "noch fanden wir"}
        ],
        "takeaway": "'noch' als Satzkonnektor erzwingt Inversion: 'noch + Verb + Subjekt'."
    },
    {
        "id": "c1-syn-80",
        "level": "C1",
        "category": "Gehobene Syntax & Satzbau",
        "title": "Substantivierte Adjektive nach Indefinitpronomen (etwas Gutes, viel Neues, alles Schöne)",
        "rule": "Deklination nach unbestimmten Mengenangaben: Nach etwas, nichts, viel, wenig, mehr, genug folgt starke neutrale Deklination auf '-es' (etwas Schönes, nichts Neues). Nach 'alles' folgt schwache neutrale Deklination auf '-e' (alles Gute, alles Schöne).",
        "formula": "etwas / nichts / viel / wenig + Adjektiv-es | alles + Adjektiv-e (GROSS!)",
        "examples": [
            {"de": "Gibt es etwas Konkretes über den Stand der Verhandlungen zu vermelden?", "en": "Is there anything concrete to announce regarding the status of negotiations?", "breakdown": "etwas Konkretes (Großschreibung, Endung -es)"},
            {"de": "Wir wünschen Ihnen für Ihren weiteren Lebensweg alles erdenklich Gute!", "en": "We wish you all the conceivable best for your further path in life!", "breakdown": "alles Gute (schwache Deklination: Endung -e)"},
            {"de": "Der Zeuge konnte der Polizei wenig Brauchbares über den Täter mitteilen.", "en": "The witness could communicate little of useful value to the police about the perpetrator.", "breakdown": "wenig Brauchbares (Endung -es)"},
            {"de": "Ich habe heute Nacht von vielem Schönem geträumt.", "en": "I dreamed of much beautiful thing tonight.", "breakdown": "Dativ: von vielem Schönem (-em)"}
        ],
        "takeaway": "Achtung: 'alles Gute' (-e), aber 'etwas Gutes' (-es). Beides stets großschreiben!"
    },
    {
        "id": "c1-syn-81",
        "level": "C1",
        "category": "Gehobene Syntax & Satzbau",
        "title": "Klammerformen im Passiv mit Modalverb: Die dreiteilige rechte Klammer",
        "rule": "Treffen im Nebensatz ein Passiv und ein Modalverb zusammen, bildet die rechte Satzklammer eine dreiteilige Kette: Partizip II + werden + Modalverb (finit).",
        "formula": "..., dass + Subjekt + ... + [Partizip II] + [werden] + [Modalverb finit]",
        "examples": [
            {"de": "Es ist unerlässlich, dass alle Daten vor dem Update [gesichert werden müssen].", "en": "It is indispensable that all data must be backed up before the update.", "breakdown": "gesichert (Partizip II) + werden (Infinitiv) + müssen (finit)"},
            {"de": "Der Anwalt forderte, dass die Akte unverzüglich [eingesehen werden könne].", "en": "The attorney demanded that the file could be inspected immediately.", "breakdown": "eingesehen werden könne (Konjunktiv I)"},
            {"de": "Niemand ahnte, dass das Gebäude wegen Einsturzgefahr [abgerissen werden musste].", "en": "Nobody suspected that the building had to be demolished due to collapse hazard.", "breakdown": "abgerissen werden musste (Präteritum)"},
            {"de": "Wir hoffen, dass dieser gravierende Fehler schnell [behoben werden kann].", "en": "We hope that this grave error can be resolved quickly.", "breakdown": "behoben werden kann"}
        ],
        "takeaway": "Im Passiv-Modal-Nebensatz steht das konjugierte Modalverb ganz am Schluss."
    },
    {
        "id": "c1-syn-82",
        "level": "C1",
        "category": "Gehobene Syntax & Satzbau",
        "title": "Gehobene Temporaladverbien: vordem, vordemmals, alsbald, dereinst",
        "rule": "Literarische und historische Texte nutzen gehobene Temporaladverbien: 'alsbald' (unverzüglich / sogleich), 'dereinst' (eines fernen Tages in der Zukunft), 'vordem' (zuvor / früher einmal).",
        "formula": "alsbald / dereinst / vordem + Satzstellung",
        "examples": [
            {"de": "Die Nachricht traf ein, und alsbald machten sich die Rettungskräfte auf den Weg.", "en": "The news arrived, and forthwith emergency services set off.", "breakdown": "alsbald = sogleich / unverzüglich"},
            {"de": "Dereinst wird die Geschichte über die Klugheit dieser Entscheidung urteilen.", "en": "One day history will judge the wisdom of this decision.", "breakdown": "dereinst = in ferner Zukunft"},
            {"de": "Wo vordem dichte Wälder standen, erstrecken sich heute monotone Monokulturen.", "en": "Where formerly dense forests stood, monotonous monocultures stretch today.", "breakdown": "vordem = in früheren Zeiten"},
            {"de": "Er versprach, die Unterlagen alsbald nachzureichen.", "en": "He promised to submit the documents forthwith.", "breakdown": "alsbald"}
        ],
        "takeaway": "alsbald, dereinst und vordem verleihen Texten epischen Atem."
    },
    {
        "id": "c1-syn-83",
        "level": "C1",
        "category": "Gehobene Syntax & Satzbau",
        "title": "Feste Wendungen mit Genitivattribut (reinen Gewissens, frohen Mutes)",
        "rule": "Adverbiale Wendungen können als erstarrte Genitive ohne Präposition auftreten (Genitivus qualitatis / modalis): reinen Gewissens, frohen Mutes, stehenden Fußes, unverrichteter Dinge, meines Erachtens.",
        "formula": "Adjektiv im Genitiv + Nomen im Genitiv (erstarrte Adverbiale)",
        "examples": [
            {"de": "Ich kann reinen Gewissens versichern, dass ich von den Schmiergeldern nichts wusste.", "en": "I can assure with a clean conscience that I knew nothing of the bribes.", "breakdown": "reinen Gewissens (adverbialer Genitiv)"},
            {"de": "Frohen Mutes brachen die Bergsteiger am frühen Morgen zum Gipfel auf.", "en": "In good spirits, the mountaineers set off early in the morning for the summit.", "breakdown": "frohen Mutes"},
            {"de": "Die Delegation reiste unverrichteter Dinge wieder aus den Verhandlungen ab.", "en": "The delegation departed from negotiations empty-handed / with business unaccomplished.", "breakdown": "unverrichteter Dinge = ohne etwas erreicht zu haben"},
            {"de": "Meines Erachtens ist dieser Gesetzentwurf verfassungswidrig.", "en": "In my opinion, this bill is unconstitutional.", "breakdown": "meines Erachtens = nach meiner Meinung"}
        ],
        "takeaway": "meines Erachtens, reinen Gewissens, stehenden Fußes: Erstarrte Genitive meisterhaft einsetzen."
    },
    {
        "id": "c1-syn-84",
        "level": "C1",
        "category": "Gehobene Syntax & Satzbau",
        "title": "Zusammengesetzte Verben mit Adjektiven (krankschreiben, freisprechen, festlegen)",
        "rule": "Verbindungen aus Adjektiv und Verb werden zusammengeschrieben, wenn das Adjektiv mit dem Verb eine neue, übertragene Gesamtbedeutung bildet (krankschreiben = ärztlich attestieren; freisprechen = für unschuldig erklären). Bleibt die wörtliche Bedeutung erhalten, wird getrennt geschrieben (laut sprechen).",
        "formula": "Neue übertragene Bedeutung = Zusammenschreibung (blamieren / heiligsprechen)",
        "examples": [
            {"de": "Der Hausarzt schrieb den erschöpften Angestellten für zwei Wochen krank.", "en": "The family doctor signed the exhausted employee off sick for two weeks.", "breakdown": "krankschreiben (übertragene Bedeutung: Attest ausstellen)"},
            {"de": "Das Gericht sprach die Angeklagte aus Mangel an Beweisen frei.", "en": "The court acquitted the defendant for lack of evidence.", "breakdown": "freisprechen = juristischer Freispruch"},
            {"de": "Wir müssen die genauen Termine bis Ende der Woche festlegen.", "en": "We must establish the exact dates by the end of the week.", "breakdown": "festlegen = fixieren"},
            {"de": "Er sprach die Worte sehr laut und deutlich aus. (Getrenntschreibung)", "en": "He spoke the words very loudly and distinctly.", "breakdown": "laut aussprechen = wörtliche Bedeutung des Adjektivs"}
        ],
        "takeaway": "Übertragene idiomatische Einheit = zusammen (krankschreiben, festsitzen, totschweigen)."
    },
    {
        "id": "c1-syn-85",
        "level": "C1",
        "category": "Gehobene Syntax & Satzbau",
        "title": "Adjektive von Eigennamen auf -sch vs. -sk (Humboldt'sch vs. kafkaesk)",
        "rule": "Adjektive, die von Personennamen auf -sch abgeleitet werden, werden kleingeschrieben (kantische Philosophie). Wird die Grundform des Namens durch einen Apostroph verdeutlicht, schreibt man groß (die Kant'sche Philosophie). Ableitungen auf -esk oder -isch von fremden Autoren werden kleingeschrieben (kafkaesk, brechtisch).",
        "formula": "kantische Philosophie ODER Kant'sche Philosophie (mit Apostroph & groß!)",
        "examples": [
            {"de": "Das Humboldt'sche Bildungsideal prägte die Entstehung moderner Universitäten.", "en": "The Humboldtian ideal of education shaped the emergence of modern universities.", "breakdown": "Humboldt'sche (mit Apostroph -> großgeschrieben)"},
            {"de": "Die hegelschen Dialektik-Modelle faszinieren Philosophen bis heute.", "en": "Hegelian dialectic models fascinate philosophers to this day.", "breakdown": "hegelschen (ohne Apostroph -> kleingeschrieben)"},
            {"de": "Die labyrinthische Bürokratie wirkte auf die Antragsteller geradezu kafkaesk.", "en": "The labyrinthine bureaucracy seemed downright Kafkaesque to applicants.", "breakdown": "kafkaesk (von Kafka abgeleitet, immer klein)"},
            {"de": "Die Planck'sche Konstante ist ein Grundpfeiler der modernen Quantenphysik.", "en": "Planck's constant is a cornerstone of modern quantum physics.", "breakdown": "Planck'sche"}
        ],
        "takeaway": "Merke: Entweder kleinschreiben (goethesch) oder mit Apostroph großschreiben (Goethe'sch)."
    },

    # 86-105: Höchste Stilstufe, Nuancierte Syntax & C1-Kompetenz
    {
        "id": "c1-syn-86",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Der irreale Wunschsatz mit Inversion und Partikeln (Wäre doch...!)",
        "rule": "Irreale Wunschsätze können ohne 'wenn' gebildet werden, indem das finite Verb an Position 1 rückt. Typische Modalpartikeln sind 'doch', 'bloß', 'nur'. Am Satzende steht ein Ausrufezeichen.",
        "formula": "[Wäre / Hätte / Könnte] + Subjekt + [doch / nur / bloß] + ...!",
        "examples": [
            {"de": "Hätte die Menschheit doch bloß rechtzeitig aus den Fehlern der Geschichte gelernt!", "en": "If only mankind had learned in time from the mistakes of history!", "breakdown": "Hätte... gelernt! (Irreale Vergangenheit mit Verb auf Pos 1)"},
            {"de": "Wäre dieser furchtbare Krieg doch endlich vorüber!", "en": "If only this terrible war were finally over!", "breakdown": "Wäre... vorüber!"},
            {"de": "Könnten wir die Zeit doch nur um ein einziges Jahr zurückdrehen!", "en": "If only we could turn back time by a single year!", "breakdown": "Könnten... zurückdrehen!"},
            {"de": "Hätten wir auf die Ratschläge der Experten gehört!", "en": "Had we only listened to the advice of the experts!", "breakdown": "Hätten... gehört!"}
        ],
        "takeaway": "Verb auf Position 1 + 'doch/bloß/nur' = vollendeter rhetorischer Wunschsatz."
    },
    {
        "id": "c1-syn-87",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Die Inversion im Hauptsatz nach vorangestelltem Nebensatz",
        "rule": "Steht ein Nebensatz (Kausal-, Temporal-, Konditional-, Konzessivsatz) vor dem Hauptsatz, besetzt der gesamte Nebensatz das Vorfeld (Position 1). Das finite Verb des Hauptsatzes MUSS daher zwingend an Position 2 stehen, direkt hinter dem Komma!",
        "formula": "[Vorangestellter Nebensatz], + [finites Verb des Hauptsatzes] + [Subjekt]...",
        "examples": [
            {"de": "Weil die Brücke baufällig ist, [müssen] [alle Lastwagen] einen großen Umweg fahren.", "en": "Because the bridge is dilapidated, all trucks must take a large detour.", "breakdown": "Nebensatz = Pos 1 -> müssen (Verb) = Pos 2 -> alle Lastwagen (Subjekt)"},
            {"de": "Obgleich die Verhandlungen schwierig waren, [einigten] [sich] die Delegierten am Ende.", "en": "Although negotiations were difficult, delegates agreed in the end.", "breakdown": "einigten (Verb Pos 2) folgt sofort nach dem Komma"},
            {"de": "Sobald die Messergebnisse vorliegen, [werden] [wir] die Öffentlichkeit informieren.", "en": "As soon as measurement results are available, we will inform the public.", "breakdown": "werden (Verb Pos 2)"},
            {"de": "Was auch immer geschehen mag, [wir] [stehen] fest zu unserem Wort.", "en": "Whatever may happen, we stand firmly by our word.", "breakdown": "stehen als finites Verb auf Pos 2 (nach Vorfeld)"}
        ],
        "takeaway": "Niemals nach dem Nebensatzkomma mit dem Subjekt beginnen: Immer Verb sofort auf Position 2!"
    },
    {
        "id": "c1-syn-88",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Das prädikative Adjektiv bei Verben des Scheins und Werdens (scheinen, wirken, dünken)",
        "rule": "Adjektive nach scheinen, wirken, anmuten, dünken bleiben als prädikative Ergänzungen undekliniert (ohne Endung): 'Es scheint unlösbar', 'Das wirkt befremdlich', 'Es dünkt mich seltsam'.",
        "formula": "scheinen / wirken / anmuten + undekliniertes Adjektiv",
        "examples": [
            {"de": "Die Aufgabe schien den beteiligten Studenten schier unlösbar.", "en": "The task seemed almost unsolvable to the participating students.", "breakdown": "unlösbar (undekliniertes prädikatives Adjektiv)"},
            {"de": "Sein langes Schweigen wirkte auf alle Anwesenden äußerst befremdlich.", "en": "His prolonged silence seemed extremely strange to all present.", "breakdown": "befremdlich"},
            {"de": "Die Architektur des Gebäudes mutet geradezu futuristisch an.", "en": "The architecture of the building appears downright futuristic.", "breakdown": "anmuten + futuristisch"},
            {"de": "Diese alte Formulierung dünkt mich etwas verstaubt.", "en": "This old phrasing seems to me somewhat dusty.", "breakdown": "dünken (gehoben für scheinen) + verstaubt"}
        ],
        "takeaway": "Prädikative Adjektive nach scheinen/wirken/anmuten tragen niemals Kasusendungen."
    },
    {
        "id": "c1-syn-89",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Konjunktionen mit restriktiver Bedeutung: es sei denn, dass vs. außer wenn",
        "rule": "'es sei denn, (dass)' und 'außer wenn' drücken eine Ausnahmebedingung aus (unless). Steht 'es sei denn' ohne 'dass', folgt Hauptsatzstellung mit Verb auf Position 2!",
        "formula": "Hauptsatz, es sei denn, + [Hauptsatz: Subjekt + Verb] | außer wenn + [Nebensatz: Verb Ende]",
        "examples": [
            {"de": "Wir fliegen morgen früh ab, es sei denn, ein Streik legt den Flughafen lahm.", "en": "We depart tomorrow morning unless a strike paralyzes the airport.", "breakdown": "es sei denn + Hauptsatzstellung (legt lahm)"},
            {"de": "Die Daten werden nach 30 Tagen gelöscht, außer wenn gesetzliche Aufbewahrungsfristen greifen.", "en": "The data is deleted after 30 days unless statutory retention periods apply.", "breakdown": "außer wenn + Nebensatzstellung (greifen am Ende)"},
            {"de": "Er nimmt keine fremde Hilfe an, es sei denn, die Lage wird absolut aussichtslos.", "en": "He accepts no outside help unless the situation becomes absolutely hopeless.", "breakdown": "es sei denn + Hauptsatz"},
            {"de": "Die Bürgschaft verfällt, es sei denn, dass die Bank fristgerecht Einspruch erhebt.", "en": "The guarantee expires unless the bank lodges an objection in due time.", "breakdown": "es sei denn, dass + Nebensatz"}
        ],
        "takeaway": "'es sei denn' ohne 'dass' verlangt normale Hauptsatz-Wortstellung!"
    },
    {
        "id": "c1-syn-90",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Verneinung ganzer Textpassagen mit 'keineswegs', 'mitnichten', 'mit keinem Wort'",
        "rule": "Um eine energische Zurückweisung zu formulieren, nutzt die C1-Stilistik feste Negationsphrasen: 'mit keinem Wort' (not with a single word), 'zu keinem Zeitpunkt' (at no point), 'unter keinen Umständen' (under no circumstances).",
        "formula": "[Negationsphrase im Vorfeld] + Verb (Pos 2) + Subjekt...",
        "examples": [
            {"de": "Mit keinem Wort erwähnte der Angeklagte seine angebliche Mittäterschaft.", "en": "Not with a single word did the defendant mention his alleged complicity.", "breakdown": "Mit keinem Wort (Pos 1) -> erwähnte (Verb Pos 2)"},
            {"de": "Zu keinem Zeitpunkt bestand für die Bevölkerung eine akute gesundheitliche Gefahr.", "en": "At no point did there exist an acute health hazard for the population.", "breakdown": "Zu keinem Zeitpunkt (Pos 1) -> bestand (Verb Pos 2)"},
            {"de": "Unter keinen Umständen darf dieser vertrauliche Bericht an die Presse gelangen.", "en": "Under no circumstances may this confidential report reach the press.", "breakdown": "Unter keinen Umständen (Pos 1) -> darf (Verb Pos 2)"},
            {"de": "In keinster Weise (umgangssprachlich) vs. In keiner Weise (C1-Standard): In keiner Weise entspricht das den Tatsachen.", "en": "In no way does that correspond to the facts.", "breakdown": "'In keiner Weise' ist standardsprachlich korrekt"}
        ],
        "takeaway": "Vorangestellte Negationsphrasen fordern strikte Inversion und erzeugen Entschiedenheit."
    },
    {
        "id": "c1-syn-91",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Die Akkusativ- und Dativ-Objekte bei reflexiven Verben (sich etwas vergegenwärtigen)",
        "rule": "Einige anspruchsvolle reflexive Verben binden das Reflexivpronomen im DATIV (mir / dir / sich) und fordern zusätzlich ein volles Akkusativobjekt: sich (Dat) etwas (Akk) aneignen, vergegenwärtigen, einverleiben, anmaßen.",
        "formula": "Subjekt + eignet / vergegenwärtigt + sich (Dat) + etwas (Akk)",
        "examples": [
            {"de": "Wir müssen uns die dramatischen Ausmaße der Katastrophe erst einmal vergegenwärtigen.", "en": "We must first realize/visualize the dramatic scale of the catastrophe to ourselves.", "breakdown": "uns (Reflexiv-Dativ) + die Ausmaße (Akkusativobjekt)"},
            {"de": "Der Student hat sich in wenigen Monaten profundes Fachwissen angeeignet.", "en": "The student acquired profound specialist knowledge in a few months.", "breakdown": "sich (Dativ) + Fachwissen (Akkusativ)"},
            {"de": "Niemand darf sich das Recht anmaßen, über andere Menschen zu richten.", "en": "Nobody may presume the right to judge other human beings.", "breakdown": "sich (Dativ) + das Recht (Akkusativ) anmaßen"},
            {"de": "Er eignete sich die unverschlüsselten Passwörter rechtswidrig an.", "en": "He appropriated the unencrypted passwords unlawfully.", "breakdown": "sich (Dativ) + die Passwörter (Akkusativ)"}
        ],
        "takeaway": "Dativ-Reflexiv + Akkusativ: 'Ich vergegenwärtige mir (Dat) den Plan (Akk)'."
    },
    {
        "id": "c1-syn-92",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Komparativ mit 'je... desto' bei verschachtelten Nebensätzen",
        "rule": "Wird der 'je... desto'-Satz durch weitere Nebensätze erweitert, bleibt die Struktur streng: 'Je' leitet den Nebensatz ein (Verb ganz am Ende); 'desto / umso' leitet den Hauptsatz ein (finites Verb steht unmittelbar hinter dem Komparativ).",
        "formula": "Je + [Komp] + ..., desto / umso + [Komp] + [Verb] + [Subjekt]...",
        "examples": [
            {"de": "Je eingehender man die historischen Quellen studiert, desto deutlicher treten die damaligen Widersprüche zutage.", "en": "The more thoroughly one studies historical sources, the more clearly contradictions of that time come to light.", "breakdown": "desto deutlicher (Komparativ) + treten (finites Verb direkt dahinter!)"},
            {"de": "Je länger die Krise andauert, umso schwerer wiegen die wirtschaftlichen Folgeschäden.", "en": "The longer the crisis persists, the more heavily consequential economic damages weigh.", "breakdown": "umso schwerer wiegen"},
            {"de": "Je mehr Verantwortung eine Führungskraft trägt, desto transparenter muss ihr Handeln sein.", "en": "The more responsibility an executive bears, the more transparent their actions must be.", "breakdown": "desto transparenter muss... sein"},
            {"de": "Je früher wir handeln, desto eher können wir eine Eskalation abwenden.", "en": "The earlier we act, the sooner we can avert an escalation.", "breakdown": "desto eher können wir"}
        ],
        "takeaway": "Niemals das Subjekt vor das Verb im desto-Satz stellen: 'desto besser IST das'!"
    },
    {
        "id": "c1-syn-93",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Verben mit Richtungsadverbien: hinauslaufen auf, münden in (+ Akk)",
        "rule": "Abstrakte Prozesse werden im gehobenen Deutsch oft durch Verben mit räumlichen Richtungsmetaphern beschrieben: 'hinauslaufen auf + Akkusativ' (amount to), 'münden in + Akkusativ' (lead into / culminate in).",
        "formula": "hinauslaufen auf + Akk | münden in + Akk",
        "examples": [
            {"de": "Letztlich läuft dieser Vorschlag auf eine verdeckte Steuererhöhung hinaus.", "en": "Ultimately, this proposal amounts to a concealed tax increase.", "breakdown": "hinauslaufen auf + Akkusativ"},
            {"de": "Die hitzige Debatte im Stadtrat mündete in einen faulen Kompromiss.", "en": "The heated debate in the city council led into a rotten compromise.", "breakdown": "münden in + Akkusativ (Richtung/Ziel)"},
            {"de": "Alle Bemühungen liefen darauf hinaus, den Frieden an der Grenze zu sichern.", "en": "All efforts amounted to securing peace at the border.", "breakdown": "liefen darauf hinaus, zu sichern"},
            {"de": "Die Untersuchungen mündeten in eine grundlegende Überarbeitung der Normen.", "en": "The investigations resulted in a fundamental revision of standards.", "breakdown": "mündeten in + Akkusativ"}
        ],
        "takeaway": "hinauslaufen auf / münden in verbildlichen gedankliche Konsequenzen dynamisch."
    },
    {
        "id": "c1-syn-94",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Adjektive mit festem Genitiv: habhaft, gewahr, überdrüssig",
        "rule": "Eine kleine Gruppe hochstehender Adjektive regiert ein Genitivobjekt: 'einer Sache überdrüssig sein' (to be tired of), 'einer Person habhaft werden' (to catch / apprehend), 'einer Gefahr gewahr werden' (to become aware of).",
        "formula": "Genitiv + habhaft / gewahr / überdrüssig + sein / werden",
        "examples": [
            {"de": "Die Polizei konnte des flüchtigen Verdächtigen erst nach Tagen habhaft werden.", "en": "Police were able to apprehend the fugitive suspect only after days.", "breakdown": "des flüchtigen Verdächtigen (Genitiv) habhaft werden"},
            {"de": "Sie wurde der ständigen Ausreden ihres Vorgesetzten langsam überdrüssig.", "en": "She was slowly growing weary of her superior's constant excuses.", "breakdown": "der Ausreden (Genitiv) überdrüssig sein"},
            {"de": "Als der Wanderer des herannahenden Unwetters gewahr wurde, kehrte er um.", "en": "When the hiker became aware of the approaching storm, he turned back.", "breakdown": "des Unwetters (Genitiv) gewahr werden"},
            {"de": "Er war des ewigen Streits um Nichtigkeiten zutiefst überdrüssig.", "en": "He was deeply weary of the eternal quarrel over trifles.", "breakdown": "des Streits überdrüssig"}
        ],
        "takeaway": "Genitivadjektive: habhaft werden, gewahr werden, überdrüssig sein zeugen von souveränem C1-Wortschatz."
    },
    {
        "id": "c1-syn-95",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Das erweiterte Prädikat mit 'pflegen zu' (Gewohnheit)",
        "rule": "'pflegen + zu + Infinitiv' drückt eine gepflegte Gewohnheit oder regelmäßige Praxis aus ('to be accustomed to / usually do'). Es gehört zum erlesenen Bildungston.",
        "formula": "Subjekt + pflegt + ... + zu + Infinitiv",
        "examples": [
            {"de": "Der emeritierte Professor pflegte morgens vor der Vorlesung im Park spazieren zu gehen.", "en": "The professor emeritus was accustomed to going for a walk in the park before the lecture in the morning.", "breakdown": "pflegte... spazieren zu gehen = tat dies gewohnheitsmäßig"},
            {"de": "Wie der Volksmund zu sagen pflegt: Vorfreude ist die schönste Freude.", "en": "As the vernacular is wont to say: Anticipation is the greatest joy.", "breakdown": "wie man zu sagen pflegt"},
            {"de": "Die Kommission pflegt bei solchen Anträgen äußerste Strenge walten zu lassen.", "en": "The commission is accustomed to exercising utmost strictness with such applications.", "breakdown": "pflegt walten zu lassen"},
            {"de": "Er pflegte seine Manuskripte stets mit der Hand zu verfassen.", "en": "He was accustomed to always composing his manuscripts by hand.", "breakdown": "pflegte zu verfassen"}
        ],
        "takeaway": "'pflegen zu tun' veredelt einfache Aussagen über Gewohnheiten stilistisch."
    },
    {
        "id": "c1-syn-96",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Doppelkonjunktionen: nicht nur... sondern auch bei ganzen Sätzen",
        "rule": "Verbindet 'nicht nur... sondern auch' zwei vollständige Hauptsätze, fordert 'nicht nur' im ersten Satz oft Inversion (Verb auf Position 2), während 'sondern' auf Position 0 steht und normale Wortstellung folgt.",
        "formula": "Nicht nur + [Verb] + [Subjekt] ..., sondern [Subjekt] + [Verb] auch ...",
        "examples": [
            {"de": "Nicht nur [hat] [der Künstler] das Gemälde selbst gemalt, sondern er hat auch den Rahmen eigenhändig geschnitzt.", "en": "Not only did the artist paint the painting himself, but he also carved the frame with his own hands.", "breakdown": "Nicht nur (Pos 1) -> hat (Verb Pos 2) -> der Künstler (Subjekt)"},
            {"de": "Nicht nur rettete die Feuerwehr das brennende Haus, sondern sie barg auch alle Haustiere unversehrt.", "en": "Not only did the fire department rescue the burning house, but it also retrieved all pets uninjured.", "breakdown": "Inversion im ersten Hauptsatz"},
            {"de": "Nicht nur verfehlte das Projekt das Budgetziel, sondern es verzögerte sich auch um ein ganzes Jahr.", "en": "Not only did the project miss the budget target, but it also was delayed by a full year.", "breakdown": "Inversion nach nicht nur"},
            {"de": "Nicht nur spricht sie fließend Deutsch, sondern sie beherrscht auch Mandarin verhandlungssicher.", "en": "Not only does she speak fluent German, but she also masters Mandarin at business level.", "breakdown": "Inversion"}
        ],
        "takeaway": "Vorangestelltes 'Nicht nur' am Satzanfang erfordert zwingend Verb-Zweit-Inversion."
    },
    {
        "id": "c1-syn-97",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Konzessive Satzverbindung mit 'gleichwohl' und 'nichtsdestotrotz'",
        "rule": "'gleichwohl' und 'nichtsdestotrotz' (umgangssprachlicher, aber im Journalismus verbreitet) stehen als Adverbien auf Position 1 und verlangen Inversion des finiten Verbs.",
        "formula": "Gleichwohl / Nichtsdestotrotz + [finites Verb] + [Subjekt]...",
        "examples": [
            {"de": "Die Erfolgsaussichten waren gering. Gleichwohl [wagte] [das Team] den waghalsigen Versuch.", "en": "The prospects of success were low. Nonetheless, the team dared the audacious attempt.", "breakdown": "Gleichwohl (Pos 1) -> wagte (Verb Pos 2) -> das Team (Subjekt)"},
            {"de": "Die Kritik an der Reform war verheerend. Gleichwohl hielt das Ministerium an seinen Plänen fest.", "en": "Criticism of the reform was devastating. Nevertheless, the ministry adhered to its plans.", "breakdown": "Gleichwohl hielt das Ministerium"},
            {"de": "Alle Experten rieten davon ab; nichtsdestotrotz investierte er sein gesamtes Erspartes in das Startup.", "en": "All experts advised against it; nevertheless, he invested his entire savings into the startup.", "breakdown": "nichtsdestotrotz investierte er"},
            {"de": "Der Gipfel schien gescheitert. Gleichwohl gelang im letzten Moment ein diplomatischer Durchbruch.", "en": "The summit seemed failed. Nonetheless, a diplomatic breakthrough succeeded at the last moment.", "breakdown": "Gleichwohl gelang"}
        ],
        "takeaway": "'gleichwohl' ist das vornehmste konzessive Konjunktionaladverb im gehobenen Deutsch."
    },
    {
        "id": "c1-syn-98",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Substantivierte Infinitive mit Präpositionen (beim Überschreiten, im Vorbeigehen)",
        "rule": "Temporal verkürzende Ausdrücke nutzen 'beim / im + großgeschriebener Infinitiv': beim Verlassen des Saals, im Vorbeigehen, beim Eintreffen der Delegation. Das Objekt des Verbs wird zum Genitivattribut.",
        "formula": "beim / im / durch / nach + großgeschriebener Infinitiv + Genitivobjekt",
        "examples": [
            {"de": "Beim Betreten der Baustelle ist das Tragen eines Schutzhelms zwingend vorgeschrieben.", "en": "Upon entering the construction site, wearing a safety helmet is strictly prescribed.", "breakdown": "beim Betreten (Dativ) + der Baustelle (Genitivattribut)"},
            {"de": "Er erwähnte die brisante Neuigkeit ganz beiläufig im Vorbeigehen.", "en": "He mentioned the volatile news quite casually in passing.", "breakdown": "im Vorbeigehen"},
            {"de": "Beim Überschreiten der zulässigen Höchstgeschwindigkeit drohen empfindliche Bußgelder.", "en": "Upon exceeding the permissible maximum speed, hefty fines threaten.", "breakdown": "beim Überschreiten der Geschwindigkeit (Genitiv)"},
            {"de": "Nach gründlichem Durchlesen des Vertrags unterzeichnete der Mandant die Urkunde.", "en": "After thorough reading through of the contract, the client signed the deed.", "breakdown": "nach Durchlesen des Vertrags"}
        ],
        "takeaway": "Präposition + substantivierter Infinitiv + Genitivattribut komprimiert Temporalsätze maximal."
    },
    {
        "id": "c1-syn-99",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Die Inversion nach lokalem oder direktionalem Vorfeld (Dahinter verbirgt sich...)",
        "rule": "Rückt ein lokales Adverbial oder ein Richtungsadverb ins Vorfeld, folgt das finite Verb unmittelbar, oft gefolgt vom nachgestellten Subjekt: 'Dahinter verbirgt sich ein ernstes Problem', 'Aus der Asche erwuchs neues Leben'.",
        "formula": "[Lokalangabe / Da-Kompositum im Vorfeld] + Verb + Subjekt",
        "examples": [
            {"de": "Dahinter verbirgt sich ein gravierendes strukturelles Versagen der Kontrollbehörden.", "en": "Behind this lies concealed a grave structural failure of regulatory authorities.", "breakdown": "Dahinter (Pos 1) -> verbirgt sich (Verb Pos 2) -> ein Versagen (Subjekt)"},
            {"de": "Aus dieser Krise erwächst die historische Chance für eine grundlegende Neuorientierung.", "en": "From this crisis arises the historic opportunity for a fundamental reorientation.", "breakdown": "Aus dieser Krise (Pos 1) -> erwächst (Verb Pos 2)"},
            {"de": "Am Horizont zeichnete sich bereits die Silhouette der Alpen ab.", "en": "On the horizon, the silhouette of the Alps was already outlining itself.", "breakdown": "Am Horizont zeichnete sich... ab"},
            {"de": "In diesem scheinbar harmlosen Absatz liegt der eigentliche Sprengsatz des Vertrages.", "en": "In this seemingly harmless paragraph lies the actual explosive device of the contract.", "breakdown": "In diesem Absatz liegt der Sprengsatz"}
        ],
        "takeaway": "Lokal-Inversion setzt das Subjekt als Pointe ans Satzende."
    },
    {
        "id": "c1-syn-100",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Verneinung mit 'mitnichten' und 'keineswegs' in Antwortgefügen",
        "rule": "'mitnichten' ist eine archaisch-literarische, aber hochwirksame absolute Negationspartikel. Sie steht für sich allein oder modifiziert das Prädikat im formellen Streitgespräch.",
        "formula": "Mitnichten! / Das ist mitnichten der Fall.",
        "examples": [
            {"de": "Haben die Sanktionen ihr Ziel erreicht? – Mitnichten, die Regierung sitzt fester im Sattel denn je.", "en": "Did the sanctions achieve their objective? – Far from it; the government sits firmer in the saddle than ever.", "breakdown": "Mitnichten als eigenständige energische Entgegnung"},
            {"de": "Das bedeutet mitnichten, dass wir vor den Forderungen kapitulieren werden.", "en": "That by no means implies that we will capitulate to the demands.", "breakdown": "bedeutet mitnichten, dass..."},
            {"de": "War dies ein spontaner Entschluss? – Mitnichten, der Plan war von langer Hand vorbereitet.", "en": "Was this a spontaneous decision? – Far from it; the plan was prepared well in advance.", "breakdown": "Mitnichten widerlegt die Frage"},
            {"de": "Diese Einigung ist mitnichten ein Triumph, sondern ein schmerzhafter Formelkompromiss.", "en": "This agreement is by no means a triumph, but a painful formula compromise.", "breakdown": "mitnichten... sondern"}
        ],
        "takeaway": "'mitnichten' zeigt absolute Stilsouveränität und rhetorische Schlagkraft."
    },
    {
        "id": "c1-syn-101",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Das Asyndeton: Unverbundene Aneinanderreihung zur Beschleunigung",
        "rule": "Beim Asyndeton werden Wörter, Satzglieder oder ganze Sätze ohne Konjunktionen (ohne 'und' / 'oder') nur durch Kommas aneinandergereiht. Das erzeugt Dynamik, Dringlichkeit und Tempo.",
        "formula": "[Element 1], [Element 2], [Element 3], [Element 4] (kein 'und'!)",
        "examples": [
            {"de": "Er kam, sah, siegte. (Veni, vidi, vici - Cäsars klassisches Asyndeton)", "en": "He came, saw, conquered.", "breakdown": "reiht drei Verben unverbunden aneinander"},
            {"de": "Verunsichert, überfordert, isoliert irrten die gestrandeten Passagiere durch den Terminal.", "en": "Uncertain, overwhelmed, isolated, the stranded passengers wandered through the terminal.", "breakdown": "drei Partizipien im Asyndeton"},
            {"de": "Wir müssen handeln, entscheiden, vorangehen, nicht zögern.", "en": "We must act, decide, forge ahead, not hesitate.", "breakdown": "Verbkette ohne Bindewort"},
            {"de": "Der Sturm heulte, der Regen peitschte, die Wellen schlugen unbarmherzig gegen die Kaimauer.", "en": "The storm howled, rain lashed, waves beat mercilessly against the quay wall.", "breakdown": "Satzreihung im Asyndeton"}
        ],
        "takeaway": "Asyndeton streicht Bindewörter und erzeugt dramatische Beschleunigung."
    },
    {
        "id": "c1-syn-102",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Das Polysyndeton: Mehrfache Verbindung mit 'und' zur Feierlichkeit",
        "rule": "Das Gegenstück zum Asyndeton ist das Polysyndeton: Jedes einzelne Glied einer Aufzählung wird durch dieselbe Konjunktion (meist 'und' oder 'oder') verbunden. Das verleiht der Aussage Schwere, Bedeutsamkeit und Hymnik.",
        "formula": "[A] und [B] und [C] und [D]",
        "examples": [
            {"de": "Und es wallet und siedet und brauset und zischt. (Schiller, Der Taucher)", "en": "And it billows and seethes and roars and hisses.", "breakdown": "Vierfache Verknüpfung mit 'und'"},
            {"de": "Wir kämpfen für Freiheit und für Gerechtigkeit und für den Frieden künftiger Generationen.", "en": "We fight for freedom and for justice and for the peace of future generations.", "breakdown": "feierliche Wiederholung von 'und für'"},
            {"de": "Tag und Nacht und Sommer und Winter kreist das Rad der Zeit unaufhörlich weiter.", "en": "Day and night and summer and winter the wheel of time keeps turning ceaselessly.", "breakdown": "Polysyndeton"},
            {"de": "Weder Gold noch Silber noch Ruhm noch Ehre konnten ihn von seinem Entschluss abbringen.", "en": "Neither gold nor silver nor fame nor honor could dissuade him from his resolve.", "breakdown": "Polysyndetische Negationsreihung"}
        ],
        "takeaway": "Polysyndeton verlangsamt den Takt und verleiht Argumenten gravitätisches Gewicht."
    },
    {
        "id": "c1-syn-103",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Verben mit Genitivobjekt und Präpositionalobjekt im Vergleich (anklagen wegen vs. anklagen der)",
        "rule": "Einige Verben erlauben sowohl die gehobene rein genitivische Konstruktion als auch die moderne Fügung mit Präposition: jemanden eines Verbrechens anklagen (Genitiv, gehoben) vs. jemanden wegen eines Verbrechens anklagen (Präposition, umgangssprachlicher).",
        "formula": "anklagen + Genitiv (C1 Standard) vs. anklagen + wegen + Genitiv (Alltag)",
        "examples": [
            {"de": "Gehoben C1: Das Gericht klagte den Angeklagten des schweren Betrugs an.", "en": "Elevated C1: The court charged the defendant with grand fraud.", "breakdown": "des schweren Betrugs (reines Genitivobjekt)"},
            {"de": "Alltag: Man klagte ihn wegen schwerem Betrug an.", "en": "Everyday: He was charged because of grand fraud.", "breakdown": "wegen-Ersatzkonstruktion"},
            {"de": "Gehoben C1: Man verdächtigte den Mitarbeiter des Landesverrats.", "en": "Elevated C1: The employee was suspected of high treason.", "breakdown": "des Landesverrats (Genitivobjekt)"},
            {"de": "Gehoben C1: Sie beschuldigten den Verwalter der Veruntreuung öffentlicher Gelder.", "en": "Elevated C1: They accused the administrator of embezzlement of public funds.", "breakdown": "der Veruntreuung (Genitivobjekt)"}
        ],
        "takeaway": "In C1-Aufsätzen stets das direkte Genitivobjekt ohne 'wegen' bevorzugen."
    },
    {
        "id": "c1-syn-104",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "Subjektlose Passivkonstruktionen bei Dativverben (Ihm wurde geholfen)",
        "rule": "Verben, die im Aktiv ein Dativobjekt fordern (helfen, danken, gratulieren, widersprechen, schaden), behalten das Dativobjekt im Passiv unverändert bei! Es gibt im Passiv KEIN Subjekt; das Verb steht zwingend in der 3. Person Singular.",
        "formula": "Dativobjekt + wurde / wird + Partizip II (Verb IMMER Singular!)",
        "examples": [
            {"de": "Dem schwer verletzten Unfallopfer wurde sofort und kompetent geholfen.", "en": "The severely injured accident victim was helped immediately and competently.", "breakdown": "Dem Opfer (Dativ) + wurde (Singular) + geholfen"},
            {"de": "Den mutigen Lebensrettern wurde vom Bundeskanzler persönlich gedankt.", "en": "The courageous lifesavers were personally thanked by the Federal Chancellor.", "breakdown": "Den Lebensrettern (Dativ Plural) + wurde (Singular!) + gedankt"},
            {"de": "Der umstrittenen Ministerin wurde von allen Fraktionen heftig widersprochen.", "en": "The controversial minister was contradicted fiercely by all parliamentary groups.", "breakdown": "Der Ministerin (Dativ) + wurde widersprochen"},
            {"de": "Seinem Ruf als unbestechlicher Ermittler wurde durch die Gerüchte nicht geschadet.", "en": "His reputation as an incorruptible investigator was not harmed by the rumors.", "breakdown": "Seinem Ruf (Dativ) + wurde geschadet"}
        ],
        "takeaway": "Niemals 'Er wurde geholfen' sagen – im Passiv bleibt Dativ immer Dativ: 'Ihm wurde geholfen'!"
    },
    {
        "id": "c1-syn-105",
        "level": "C1",
        "category": "Höchste Stilstufe & Syntaktische Perfektion",
        "title": "C1-Meisterschaft: Die vollendete Symbiose aus Grammatik, Topologie und Rhetorik",
        "rule": "Das C1-Niveau markiert die vollendete funktionale Beherrschung der deutschen Sprache. Der Sprecher wechselt mühelos zwischen lebendigem Verbalstil und verdichtetem Nominalstil, beherrscht die Felderlehre meisterhaft, nutzt Funktionsverbgefüge präzise und setzt rhetorische Stilmittel wie Litotes, Chiasmus und präzise Konnektoren zielgerichtet ein.",
        "formula": "Präzision + Satztopologie + FVG + Konjunktiv I/II + Stilistische Eleganz",
        "examples": [
            {"de": "Eingedenk der historischen Tragweite ihrer Mission stellten die Delegierten unter Beweis, dass selbst tiefste ideologische Gräben durch beharrlichen Dialog überwunden werden können.", "en": "Mindful of the historical significance of their mission, delegates proved that even deepest ideological divides can be overcome through persistent dialogue.", "breakdown": "eingedenk (Genitivpräposition) + FVG (unter Beweis stellen) + Partizipialverdichtung"},
            {"de": "Nicht nur entbehrte die Anklage jeglicher stichhaltiger Beweise, sondern das Gericht sprach die Beschuldigten auch reinen Gewissens von allen Vorwürfen frei.", "en": "Not only did the indictment lack any solid evidence, but the court also acquitted the accused of all charges with a clean conscience.", "breakdown": "Inversion nach nicht nur + Genitivverb entbehren + erstarrter Genitiv reinen Gewissens + FVG/Verb freisprechen"},
            {"de": "Sollten die Verhandlungen wider Erwarten scheitern, so stünde zu befürchten, dass der Konflikt in kriegerische Auseinandersetzungen mündet.", "en": "Should negotiations fail contrary to expectations, it would be feared that the conflict culminate in armed clashes.", "breakdown": "Konditionale Inversion + so-Korrelat + wissenschaftliches stünde zu befürchten + Richtungsverb münden in"},
            {"de": "Mitnichten handelt es sich hierbei um ein marginales Detail; vielmehr rührt diese Frage an das Fundament unseres demokratischen Zusammenlebens.", "en": "By no means is this a marginal detail; rather, this question touches upon the foundation of our democratic coexistence.", "breakdown": "Rhetorische Negation mitnichten + Inversion + Antithese mit vielmehr"}
        ],
        "takeaway": "Beherrschung aller C1-Elemente ermöglicht stilsicheres, differenziertes und souveränes Deutsch auf muttersprachlichem Niveau."
    }
]

def main():
    os.makedirs("deutsche/data", exist_ok=True)
    out_file = "deutsche/data/c1.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// German Grammar C1 Dataset - 105 comprehensive topics\n")
        f.write("// Original pedagogical examples (no examples copied from reference PDF)\n")
        f.write("window.GERMAN_DATA_C1 = ")
        json.dump(topics, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"✅ Generated {out_file} with {len(topics)} topics!")

if __name__ == "__main__":
    main()
