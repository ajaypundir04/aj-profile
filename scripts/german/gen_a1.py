#!/usr/bin/env python3
"""
Generator for Level A1 German Grammar Topics (105 Topics)
All examples are 100% original, modern real-world German examples.
Zero examples taken from reference PDF.
"""
import json

def get_a1_topics():
    topics = []
    
    # helper to add topic
    def add_t(tid, title, cat, rule, explanation, examples, key_points, tags):
        topics.append({
            "id": f"de-a1-{tid}",
            "level": "A1",
            "category": cat,
            "title": title,
            "ruleBox": rule,
            "explanation": explanation,
            "examples": examples,
            "keyPoints": key_points,
            "tags": tags
        })

    # --- Section 1: Alphabet, Phonetics & Pronunciation (1-8) ---
    add_t(1, "The German Alphabet & Special Letters (Das Alphabet)",
          "Alphabet & Phonetics",
          "26 Latin letters + 3 Umlauts (ä, ö, ü) + 1 ligature (ß / Eszett)",
          "German uses the standard 26-letter Latin alphabet plus four special characters: the umlauts ä, ö, ü, and the sharp s (ß). Capitalization is mandatory for all nouns and sentence beginnings.",
          [{"de": "Das Alphabet hat 26 Buchstaben und vier Sonderzeichen.", "en": "The alphabet has 26 letters and four special characters."},
           {"de": "Mein Vorname schreibt sich mit einem Umlaut.", "en": "My first name is spelled with an umlaut."}],
          ["All German nouns are capitalized without exception", "ß is only used after long vowels or diphthongs (e.g., Straße, weiß)", "Switzerland and Liechtenstein use 'ss' instead of 'ß'"],
          ["Alphabet", "Phonetics", "Basics"])

    add_t(2, "Umlauts: Pronunciation & Spelling (ä, ö, ü)",
          "Alphabet & Phonetics",
          "ä ≈ /ɛ/ (air), ö ≈ /ø/ (rounded lips saying 'ay'), ü ≈ /y/ (rounded lips saying 'ee')",
          "Umlauts are vowel modifications that shift mouth shape. In digital keyboards or crosswords without German characters, ä=ae, ö=oe, ü=ue, ß=ss.",
          [{"de": "Können Sie die Tür für mich öffnen?", "en": "Can you open the door for me?"},
           {"de": "Die Äpfel liegen auf dem Küchentisch.", "en": "The apples are lying on the kitchen table."}],
          ["Never omit the two dots: schon (already) vs schön (beautiful) have completely different meanings", "Alternative spelling: ae, oe, ue", "Essential for plural nouns (Apfel -> Äpfel)"],
          ["Umlauts", "Pronunciation", "Spelling"])

    add_t(3, "The 'ß' (Eszett / Sharp S) vs 'ss'",
          "Alphabet & Phonetics",
          "Long vowel / diphthong + ß | Short vowel + ss",
          "The letter ß represents a voiceless 's' sound (/s/). It only appears after long vowels (Straße, Gruß) or diphthongs (fleißig, weiß). After short vowels, double 's' is used (Schloss, Fluss, müssen).",
          [{"de": "Wir wohnen in einer ruhigen Straße in Berlin.", "en": "We live on a quiet street in Berlin."},
           {"de": "Er trinkt eine Tasse heißen Tee.", "en": "He drinks a cup of hot tea."}],
          ["ß never starts a word", "After short vowels, always write 'ss' (Wasser, Kuss)", "After long vowels or diphthongs, write 'ß' (Fuß, heiß)"],
          ["Eszett", "Spelling Rules", "Orthography"])

    add_t(4, "Diphthongs: ei, ie, eu, äu",
          "Alphabet & Phonetics",
          "ei = /aɪ/ (like 'eye') | ie = /iː/ (like 'ee') | eu / äu = /ɔʏ/ (like 'boy')",
          "German diphthongs are vowel pairs pronounced as a single continuous gliding sound. Note the contrast between 'ei' and 'ie': 'mein' sounds like 'mine', while 'Miete' sounds like 'mee-tuh'.",
          [{"de": "Mein lieber Freund reist heute nach Leipzig.", "en": "My dear friend is traveling to Leipzig today."},
           {"de": "Neue Häuser sind oft sehr teuer.", "en": "New houses are often very expensive."}],
          ["ei: pronounce the second letter ('eye')", "ie: pronounce the second letter ('ee')", "eu and äu sound identical (/ɔʏ/)"],
          ["Diphthongs", "Vowels", "Pronunciation"])

    add_t(5, "The 'ch' Sound: Ach-Laut vs Ich-Laut",
          "Alphabet & Phonetics",
          "After a, o, u, au -> Ach-Laut /x/ | After e, i, ä, ö, ü, eu, consonants -> Ich-Laut /ç/",
          "The combination 'ch' produces two distinct sounds depending on preceding vowels. After dark back vowels (a, o, u), it is pronounced at the back of the throat. After bright front vowels (e, i, ä) or consonants, it is a soft hiss against the palate.",
          [{"de": "Ich koche heute Abend eine leckere Suppe.", "en": "I am cooking a delicious soup this evening."},
           {"de": "Welche Bücher möchtest du in der Bibliothek leihen?", "en": "Which books would you like to borrow from the library?"}],
          ["Buch, Nacht, Woche -> Ach-Laut (guttural)", "Ich, Licht, möchten, Mädchen -> Ich-Laut (soft)", "-chen diminutive suffix is always the soft Ich-Laut"],
          ["Phonetics", "Consonants", "Pronunciation"])

    add_t(6, "The Sounds of 'sp' and 'st' at Word Beginnings",
          "Alphabet & Phonetics",
          "Initial sp- = /ʃp/ ('shp') | Initial st- = /ʃt/ ('sht')",
          "When 'sp' or 'st' appears at the beginning of a word or syllable root, the 's' is pronounced as 'sh' (/ʃ/). In the middle or end of words, it retains the normal /s/ sound (z.B. Post, Fenster).",
          [{"de": "Stefan spricht vier verschiedene Sprachen fließend.", "en": "Stefan speaks four different languages fluently."},
           {"de": "Die Stadt München liegt im Süden von Deutschland.", "en": "The city of Munich is located in the south of Germany."}],
          ["Sport is pronounced 'Shport'", "Straße is pronounced 'Shtrah-seh'", "Mid-word 'st' remains plain /st/ (Fenster, Post)"],
          ["Phonetics", "Consonants"])

    add_t(7, "Terminal Devoicing (Auslautverhärtung)",
          "Alphabet & Phonetics",
          "Word-final b -> /p/, d -> /t/, g -> /k/",
          "In German, voiced consonants (b, d, g) at the end of a word or syllable lose their voice and are pronounced as their unvoiced counterparts (p, t, k).",
          [{"de": "Der Hund bellt laut im Park.", "en": "The dog barks loudly in the park."},
           {"de": "Ich fahre mit dem Fahrrad in die Arbeit.", "en": "I ride my bicycle to work."}],
          ["'Hund' sounds like 'Hunt'", "'Tag' sounds like 'Tak'", "'gelb' sounds like 'gelp'"],
          ["Pronunciation", "Phonetics"])

    add_t(8, "The Glottal Stop (Knacklaut)",
          "Alphabet & Phonetics",
          "Mouth brief closure before vowels at word/morpheme beginnings",
          "The glottal stop is an audible brief closure of the vocal cords before words or prefixes beginning with a vowel, giving German its crisp, distinct rhythm.",
          [{"de": "Er beginnt um acht Uhr am Abend.", "en": "He starts at eight o'clock in the evening."},
           {"de": "Sie studiert Theater und Kunst.", "en": "She studies theater and art."}],
          ["Separates words cleanly: 'eine Ente' is not slurred together", "Occurs after prefixes: 'be-antworten'", "Crucial for authentic accent"],
          ["Phonetics", "Rhythm"])

    # --- Section 2: Articles, Gender & Nouns (9-22) ---
    add_t(9, "Definite Articles in the Nominative: der, die, das",
          "Articles & Nouns",
          "Masculine: der | Feminine: die | Neuter: das | Plural: die",
          "Every German noun has a fixed grammatical gender. In the nominative (subject) case, the definite articles are der (masculine), die (feminine), das (neuter), and die (all plurals).",
          [{"de": "Der Kaffee schmeckt hervorragend.", "en": "The coffee tastes outstanding."},
           {"de": "Die Sonne scheint heute den ganzen Tag.", "en": "The sun is shining all day today."},
           {"de": "Das Buch liegt auf dem Tisch.", "en": "The book is lying on the table."}],
          ["Always learn every noun with its article (der Tisch, not just Tisch)", "Grammatical gender does not equal biological gender", "Plural article is always 'die' in the nominative"],
          ["Articles", "Gender", "Nominative"])

    add_t(10, "Indefinite Articles: ein, eine, ein",
          "Articles & Nouns",
          "Masculine: ein | Feminine: eine | Neuter: ein | Plural: (keine Pluralform)",
          "The indefinite article corresponds to 'a' or 'an' in English. It introduces unspecified nouns. Plural nouns have no indefinite article (Nullartikel).",
          [{"de": "Ich habe einen Bruder und eine Schwester.", "en": "I have a brother and a sister."},
           {"de": "Dort steht ein altes Gebäude.", "en": "An old building stands over there."}],
          ["Masculine and Neuter share 'ein' in the nominative", "Feminine takes 'eine'", "There is no plural form of 'ein' (e.g., 'Ich kaufe Äpfel')"],
          ["Articles", "Indefinite"])

    add_t(11, "The Negative Article: kein, keine, kein",
          "Articles & Nouns",
          "Negates nouns with indefinite article or no article: kein / keine / kein / keine (Plural)",
          "To negate a noun that would otherwise take 'ein' or no article, German uses 'kein' (not 'nicht'). Its endings mirror the indefinite article, plus it has a plural form 'keine'.",
          [{"de": "Ich trinke keinen Kaffee am späten Nachmittag.", "en": "I drink no coffee in the late afternoon."},
           {"de": "Wir haben heute keine Zeit für das Museum.", "en": "We have no time for the museum today."}],
          ["Use 'kein' for nouns with ein/no article", "Use 'nicht' for verbs, adjectives, and nouns with 'der/die/das'", "Plural form is always 'keine' in nominative/accusative"],
          ["Negation", "Articles"])

    add_t(12, "Predicting Gender: Masculine Suffixes (-er, -ling, -ismus, -or)",
          "Articles & Nouns",
          "Nouns ending in -ling, -ismus, -or, -ant are overwhelmingly masculine (der)",
          "While grammatical gender is largely arbitrary, specific noun suffixes reliably indicate gender. Nouns referring to male professions or ending in -ling, -ismus, -or, -ant are masculine.",
          [{"de": "Der Optimismus der Mannschaft ist bemerkenswert.", "en": "The optimism of the team is remarkable."},
           {"de": "Der Schmetterling fliegt über die Blumenwiese.", "en": "The butterfly flies over the meadow of flowers."}],
          ["Male occupations: der Arzt, der Lehrer, der Ingenieur", "Suffix -ismus: der Kapitalismus, der Realismus", "Days, months, seasons, compass points are always der"],
          ["Gender Rules", "Masculine"])

    add_t(13, "Predicting Gender: Feminine Suffixes (-ung, -heit, -keit, -schaft, -ei, -tät)",
          "Articles & Nouns",
          "Nouns ending in -ung, -heit, -keit, -schaft, -tät, -ei, -ion are 100% feminine (die)",
          "These suffixes provide an infallible rule for determining feminine nouns. Memorizing this rule allows learners to identify the gender of thousands of abstract nouns instantly.",
          [{"de": "Die Wohnung hat eine moderne Heizung.", "en": "The apartment has a modern heating system."},
           {"de": "Die Freiheit und die Gerechtigkeit sind wichtige Werte.", "en": "Freedom and justice are important values."}],
          ["-ung: die Zeitung, die Erfahrung, die Rechnung", "-heit / -keit: die Gesundheit, die Möglichkeit", "-schaft: die Freundschaft, die Mannschaft"],
          ["Gender Rules", "Feminine"])

    add_t(14, "Predicting Gender: Neuter Suffixes (-chen, -lein, -ment, -um, -tum)",
          "Articles & Nouns",
          "Diminutives (-chen, -lein) and Latin loan endings (-ment, -um) are always neuter (das)",
          "Any noun with the diminutive suffix -chen or -lein is grammatically neuter, regardless of biological gender. This explains why 'das Mädchen' (girl) is neuter in German.",
          [{"de": "Das Mädchen liest ein spannendes Märchen.", "en": "The girl is reading an exciting fairy tale."},
           {"de": "Das Dokument liegt im Sekretariat.", "en": "The document is in the administrative office."}],
          ["-chen / -lein makes any noun neuter: das Brötchen, das Häuschen", "-ment / -um: das Instrument, das Zentrum, das Museum", "Letters of the alphabet and fractions are neuter: das A, das Drittel"],
          ["Gender Rules", "Neuter"])

    add_t(15, "Compound Nouns: The Last Noun Determines Gender",
          "Articles & Nouns",
          "Word 1 + Word 2 + ... + Final Noun -> Gender of Final Noun",
          "German frequently joins multiple nouns into a single compound word. The grammatical gender and plural form of the entire compound are always dictated by the very last noun.",
          [{"de": "Die Haustür (das Haus + die Tür = die Haustür) ist verschlossen.", "en": "The front door is locked."},
           {"de": "Der Apfelsaft (der Apfel + der Saft = der Saft) steht im Kühlschrank.", "en": "The apple juice is in the refrigerator."}],
          ["The main noun comes last; all preceding words are modifiers", "Connecting letters (Fugenelemente like -s- or -en-) are sometimes inserted: der Geburtstag", "Read compounds right-to-left to understand them"],
          ["Compound Nouns", "Gender Rules"])

    add_t(16, "The Zero Article (Der Nullartikel)",
          "Articles & Nouns",
          "No article with nationalities, professions in predication, cities, languages, and materials",
          "In German, articles are omitted in specific grammatical contexts: stating one's profession, nationality, most countries and cities, materials, and abstract plural nouns.",
          [{"de": "Ich bin Softwareentwickler und lebe in Hamburg.", "en": "I am a software developer and live in Hamburg."},
           {"de": "Wir sprechen Deutsch und Englisch bei der Arbeit.", "en": "We speak German and English at work."}],
          ["'Ich bin Arzt' (no 'ein' unless described by an adjective)", "Most countries have no article: Deutschland, Frankreich, Spanien", "Exceptions with articles: die Schweiz, die Türkei, die USA"],
          ["Nullartikel", "Articles"])

    add_t(17, "Countries with Definite Articles",
          "Articles & Nouns",
          "Feminine: die Schweiz, die Türkei, die Ukraine | Plural: die USA, die Niederlande | Masculine: der Iran",
          "While most countries are neuter and take no article, several important nations retain their definite article in all cases. This affects prepositions used with them (e.g., 'in die Schweiz' vs 'nach Deutschland').",
          [{"de": "Nächste Woche fliege ich in die Schweiz.", "en": "Next week I am flying to Switzerland."},
           {"de": "Er macht Urlaub in den Niederlanden.", "en": "He is on vacation in the Netherlands."}],
          ["die Schweiz, die Türkei, die Slowakei, die Ukraine", "die USA, die Niederlande, die Philippinen (Plural)", "With article-countries, use 'in + Akk' for direction instead of 'nach'"],
          ["Countries", "Articles"])

    add_t(18, "Plural Patterns: -(e)n Suffix",
          "Articles & Nouns",
          "Most feminine nouns take -(e)n: die Frau -> die Frauen, die Lampe -> die Lampen",
          "Adding -(e)n is the most frequent plural formation in the German language, especially for feminine nouns ending in -e, -ung, -heit, -keit, and foreign masculine nouns.",
          [{"de": "Die Studentinnen arbeiten gemeinsam an dem Projekt.", "en": "The female students are working together on the project."},
           {"de": "Auf dem Tisch liegen viele Rechnungen.", "en": "Many invoices are lying on the table."}],
          ["Almost all feminine nouns take -(e)n in the plural", "Nouns ending in -in double the n: die Lehrerin -> die Lehrerinnen", "No umlaut is added with -(e)n plural ending"],
          ["Plural Formation", "Nouns"])

    add_t(19, "Plural Patterns: -e Suffix with or without Umlaut",
          "Articles & Nouns",
          "Many masculine & neuter monosyllabic nouns take -e: der Tag -> die Tage, der Baum -> die Bäume",
          "The -e plural ending is very common for masculine single-syllable nouns. In most cases, masculine nouns also receive an umlaut on the root vowel (a->ä, o->ö, u->ü).",
          [{"de": "Die Bäume im Park verlieren ihre Blätter.", "en": "The trees in the park are losing their leaves."},
           {"de": "Wir haben heute zwei wichtige Termine.", "en": "We have two important appointments today."}],
          ["der Tag -> die Tage (no umlaut)", "der Stuhl -> die Stühle (with umlaut)", "das Jahr -> die Jahre (neuter takes -e)"],
          ["Plural Formation", "Nouns"])

    add_t(20, "Plural Patterns: -er Suffix with Umlaut",
          "Articles & Nouns",
          "Most neuter single-syllable nouns take -er + Umlaut: das Kind -> die Kinder, das Buch -> die Bücher",
          "The -er plural ending is predominantly used by neuter nouns, with root vowels (a, o, u) taking an umlaut. A few masculine nouns also use this pattern (der Mann -> die Männer).",
          [{"de": "Die Kinder spielen draußen im Garten.", "en": "The children are playing outside in the garden."},
           {"de": "Die Bücher stehen geordnet im Regal.", "en": "The books stand organized on the shelf."}],
          ["das Kind -> die Kinder", "das Bild -> die Bilder", "das Haus -> die Häuser (au -> äu)"],
          ["Plural Formation", "Nouns"])

    add_t(21, "Plural Patterns: No Ending (Zero Plural) / Umlaut Only",
          "Articles & Nouns",
          "Masculine and neuter nouns ending in -el, -en, -er: der Lehrer -> die Lehrer, der Apfel -> die Äpfel",
          "Nouns ending in -el, -en, or -er do not add an ending in the plural. However, masculine nouns frequently add an umlaut to their root vowel.",
          [{"de": "Die Lehrer treffen sich im Konferenzraum.", "en": "The teachers meet in the conference room."},
           {"de": "Auf dem Teller liegen drei rote Äpfel.", "en": "Three red apples are lying on the plate."}],
          ["der Koffer -> die Koffer", "der Garten -> die Gärten (with umlaut)", "das Fenster -> die Fenster"],
          ["Plural Formation", "Nouns"])

    add_t(22, "Plural Patterns: -s Suffix (Loanwords & Acronyms)",
          "Articles & Nouns",
          "Foreign loanwords, acronyms, and words ending in full vowels: das Auto -> die Autos, das Hotel -> die Hotels",
          "The -s plural is primarily used for loanwords from English and French, words ending in vowels other than -e (a, i, o, u), abbreviations, and family names.",
          [{"de": "Die Autos stehen auf dem großen Parkplatz.", "en": "The cars are parked in the large parking lot."},
           {"de": "In dieser Straße gibt es drei moderne Cafés.", "en": "On this street there are three modern cafés."}],
          ["das Foto -> die Fotos", "das Handy -> die Handys", "der Chef -> die Chefs"],
          ["Plural Formation", "Loanwords"])

    # --- Section 3: Pronouns (23-32) ---
    add_t(23, "Personal Pronouns in the Nominative: ich, du, er, sie, es, wir, ihr, sie, Sie",
          "Pronouns",
          "1st: ich/wir | 2nd: du/ihr/Sie | 3rd: er/sie/es/sie",
          "Personal pronouns replace nouns and act as the subject of the sentence in the nominative case. Note that German distinguishes between singular informal (du), plural informal (ihr), and formal (Sie).",
          [{"de": "Ich lerne Deutsch, weil ich in München arbeite.", "en": "I am learning German because I work in Munich."},
           {"de": "Wir gehen heute Abend zusammen ins Kino.", "en": "We are going to the cinema together this evening."}],
          ["'er' replaces masculine nouns (der Tisch -> er)", "'sie' replaces feminine nouns (die Lampe -> sie)", "'es' replaces neuter nouns (das Buch -> es)"],
          ["Pronouns", "Nominative"])

    add_t(24, "Formal vs Informal Address: 'Sie' vs 'du' and 'ihr'",
          "Pronouns",
          "Informal singular: du | Informal plural: ihr | Formal (singular & plural): Sie",
          "German culture strictly distinguishes between informal address (used with family, friends, children, and colleagues in informal companies) and formal 'Sie' (always capitalized, used with strangers, clients, officials, and seniors).",
          [{"de": "Guten Tag, Herr Weber, wie geht es Ihnen?", "en": "Good day, Mr. Weber, how are you? (formal)"},
           {"de": "Hallo Anna, kommst du heute zur Feier?", "en": "Hello Anna, are you coming to the party? (informal)"}],
          ["Always capitalize formal 'Sie', 'Ihnen', 'Ihr'", "Conjugate formal 'Sie' identically to plural 'sie' (Sie kommen)", "Use 'ihr' when speaking to two or more friends"],
          ["Etiquette", "Pronouns", "Social German"])

    add_t(25, "Possessive Determiners in Nominative (mein, dein, sein, ihr, unser, euer, ihr, Ihr)",
          "Pronouns",
          "Base stems: mein, dein, sein (his/its), ihr (her), unser, euer, ihr (their), Ihr (your, formal)",
          "Possessive determiners indicate ownership and take endings matching the gender and number of the noun they precede (mein Bruder, meine Schwester, mein Buch, meine Eltern).",
          [{"de": "Mein Vater und meine Mutter wohnen in Köln.", "en": "My father and my mother live in Cologne."},
           {"de": "Unser Team hat das beste Ergebnis erzielt.", "en": "Our team achieved the best result."}],
          ["Base stem + -e for feminine and plural: mein -> meine", "Watch 'euer': drops an 'e' before endings -> eure (not euere)", "'sein' means his/its, while 'ihr' means her/their"],
          ["Possessive", "Pronouns"])

    add_t(26, "Possessive Determiner 'euer' & Contraction Rule",
          "Pronouns",
          "euer + -e -> eure | euer + -en -> euren | euer + -em -> eurem",
          "The second-person plural informal possessive determiner 'euer' drops its internal 'e' when adding an inflectional ending, maintaining phonological smoothness in speech.",
          [{"de": "Ist das eure neue Wohnung?", "en": "Is that your (plural informal) new apartment?"},
           {"de": "Wo habt ihr euren Schlüssel gelassen?", "en": "Where did you leave your key?"}],
          ["Uninflected: euer Vater, euer Auto", "Inflected with -e: eure Mutter, eure Freunde", "Inflected with -en: euren Urlaub"],
          ["Possessive", "Irregularity"])

    add_t(27, "Personal Pronouns in the Accusative Case",
          "Pronouns",
          "mich, dich, ihn, sie, es, uns, euch, sie, Sie",
          "When a personal pronoun receives the direct action of a transitive verb or follows an accusative preposition, it takes the accusative form.",
          [{"de": "Siehst du mich auf dem alten Foto?", "en": "Do you see me in the old photo?"},
           {"de": "Ich rufe dich heute Abend um acht Uhr an.", "en": "I will call you this evening at eight o'clock."}],
          ["er -> ihn (only masculine changes form in 3rd person singular)", "sie (fem/plur) and es (neut) stay identical to nominative", "mich / uns (1st person), dich / euch (2nd person)"],
          ["Pronouns", "Accusative"])

    add_t(28, "The Impersonal Pronoun 'man'",
          "Pronouns",
          "man = one / people / they (general statement); conjugated like er/sie/es (3rd person singular)",
          "'man' refers to people in general or an unspecified agent, equivalent to English 'one' or passive 'people'. Do not confuse it with 'der Mann' (the man).",
          [{"de": "In Deutschland trinkt man gerne Mineralwasser mit Kohlensäure.", "en": "In Germany, people like to drink sparkling mineral water."},
           {"de": "Hier darf man nicht laut telefonieren.", "en": "One is not allowed to make loud phone calls here."}],
          ["Always lower case (except at sentence start) with one 'n'", "Always takes 3rd person singular verb ending (man kann, man sagt)", "Equivalent to English 'you' in general instructions"],
          ["Pronouns", "Impersonal"])

    add_t(29, "The Impersonal Pronoun 'es'",
          "Pronouns",
          "es = it; used for weather, time, sensory expressions, and impersonal constructions",
          "'es' acts as an essential dummy subject for meteorological states, telling time, sensation, and fixed idiomatic expressions.",
          [{"de": "Es regnet den ganzen Tag in Hamburg.", "en": "It is raining all day in Hamburg."},
           {"de": "Wie spät ist es jetzt?", "en": "What time is it now?"}],
          ["Weather: es schneit, es donnert, es ist kalt", "Fixed idioms: Es gibt (there is/are), Es geht mir gut", "Time: Es ist zehn Uhr"],
          ["Pronouns", "Impersonal"])

    add_t(30, "Demonstrative Pronouns: dieser, diese, dieses",
          "Pronouns",
          "Masc: dieser | Fem: diese | Neut: dieses | Plur: diese",
          "Demonstrative pronouns point out specific items or people ('this one' / 'these ones'), declined exactly like the definite article der/die/das.",
          [{"de": "Dieser Pullover gefällt mir besser als jener.", "en": "This sweater pleases me better than that one."},
           {"de": "Dieses Restaurant serviert ausgezeichnetes Essen.", "en": "This restaurant serves excellent food."}],
          ["Replaces or specifies a noun directly", "Takes regular der-word endings", "Can stand alone: 'Welches Buch willst du? - Dieses!'"],
          ["Demonstrative", "Pronouns"])

    add_t(31, "Indefinite Pronouns: jemand, niemand, etwas, nichts",
          "Pronouns",
          "jemand (someone) vs niemand (no one) | etwas (something) vs nichts (nothing)",
          "These basic indefinite pronouns express unidentified persons or things. 'etwas' and 'nichts' are uninflected and invariable.",
          [{"de": "Hast du etwas Interessantes in der Zeitung gelesen?", "en": "Did you read something interesting in the newspaper?"},
           {"de": "Niemand weiß die richtige Antwort auf diese Frage.", "en": "Nobody knows the correct answer to this question."}],
          ["'etwas' and 'nichts' never change endings", "'jemand' and 'niemand' can optionally take case endings (-en for acc, -em for dat)", "'etwas' can be abbreviated colloquially to 'was'"],
          ["Pronouns", "Indefinite"])

    add_t(32, "Interrogative Pronouns: wer, wen, was",
          "Pronouns",
          "Nom: wer? (who?) | Akk: wen? (whom?) | Was? (what? - things)",
          "Questions about people decline based on the grammatical case of the question, while questions about objects or actions use 'was'.",
          [{"de": "Wer hat die Haustür offen gelassen?", "en": "Who left the front door open?"},
           {"de": "Wen triffst du heute Nachmittag im Café?", "en": "Whom are you meeting this afternoon at the café?"}],
          ["'Wer' = subject (Nominative)", "'Wen' = direct object (Accusative)", "'Was' = things in both nominative and accusative"],
          ["Questions", "Pronouns"])

    # --- Section 4: Verbs & Conjugation: Präsens (33-50) ---
    add_t(33, "Regular Verb Conjugation in Present Tense (Präsens)",
          "Verbs & Conjugation",
          "Stem + endings: ich -e, du -st, er/sie/es -t, wir -en, ihr -t, sie/Sie -en",
          "To conjugate a regular German verb, remove the infinitive ending '-en' to find the verb stem, then add personal endings corresponding to the subject pronoun.",
          [{"de": "Ich lerne jeden Tag neue deutsche Wörter.", "en": "I learn new German words every day."},
           {"de": "Wir wohnen seit drei Jahren in Frankfurt.", "en": "We have been living in Frankfurt for three years."}],
          ["Verb stem: lernen -> lern-", "wir and sie/Sie endings are always identical to the infinitive", "er, sie, es and ihr share the -t ending"],
          ["Verbs", "Conjugation", "Present"])

    add_t(34, "Verbs with Stem Ending in -d or -t (arbeiten, finden)",
          "Verbs & Conjugation",
          "Insert -e- before endings for du (-est), er/sie/es (-et), ihr (-et)",
          "When a verb stem ends in -d, -t, or consonant clusters like -tm, -chn, inserting an extra 'e' prevents unpronounceable consonant combinations in the 2nd and 3rd person singular and 2nd person plural.",
          [{"de": "Mein Kollege arbeitet bei einem internationalen Technologiekonzern.", "en": "My colleague works at an international technology corporation."},
           {"de": "Was findest du an diesem Konzept besonders gut?", "en": "What do you find especially good about this concept?"}],
          ["arbeiten: du arbeitest, er arbeitet, ihr arbeitet", "finden: du findest, er findet, ihr findet", "Applies also to 'kosten', 'warten', 'öffnen'"],
          ["Verbs", "Stem Changes"])

    add_t(35, "Verbs with Stem Ending in -s, -ß, -z (heißen, reisen)",
          "Verbs & Conjugation",
          "In the 2nd person singular (du), add only -t instead of -st",
          "Since the stem already ends in an 's' sound, adding another 's' is redundant. Therefore, 'du' and 'er/sie/es' share the exact same ending (-t).",
          [{"de": "Wie heißt du mit Vornamen?", "en": "What is your first name?"},
           {"de": "Er reist gerne in ferne Länder.", "en": "He likes to travel to distant countries."}],
          ["heißen: du heißt, er heißt (identical form)", "tanzen: du tanzt, er tanzt", "schließen: du schließt, er schließt"],
          ["Verbs", "Irregularities"])

    add_t(36, "The Auxiliary Verb 'sein' (to be) in Present Tense",
          "Verbs & Conjugation",
          "ich bin, du bist, er/sie/es ist, wir sind, ihr seid, sie/Sie sind",
          "'sein' is the most irregular and vital verb in the German language. It serves as both a primary linking verb and a critical auxiliary for compound past tenses.",
          [{"de": "Ich bin neu in der Stadt und suche eine Wohnung.", "en": "I am new in town and looking for an apartment."},
           {"de": "Ihr seid sehr herzlich willkommen in unserem Verein.", "en": "You are very warmly welcome in our club."}],
          ["Completely irregular stem in every person", "Takes Nominative predicate nouns (Er ist ein guter Lehrer)", "Used as auxiliary verb in Perfekt for movement/change of state"],
          ["Verbs", "sein", "Auxiliary"])

    add_t(37, "The Auxiliary Verb 'haben' (to have) in Present Tense",
          "Verbs & Conjugation",
          "ich habe, du hast, er/sie/es hat, wir haben, ihr habt, sie/Sie haben",
          "'haben' indicates possession and serves as the primary auxiliary verb for the Perfekt past tense. Notice the stem contraction in 'du hast' and 'er hat' (dropping the 'b').",
          [{"de": "Wir haben heute Nachmittag ein wichtiges Meeting.", "en": "We have an important meeting this afternoon."},
           {"de": "Hast du einen Moment Zeit für mich?", "en": "Do you have a moment of time for me?"}],
          ["Stem drops 'b' for du (hast) and er/sie/es (hat)", "Requires the Accusative case for direct objects (Ich habe einen Hund)", "Primary auxiliary verb for Perfekt tense"],
          ["Verbs", "haben", "Auxiliary"])

    add_t(38, "The Verb 'werden' (to become / will) in Present Tense",
          "Verbs & Conjugation",
          "ich werde, du wirst, er/sie/es wird, wir werden, ihr werdet, sie/Sie werden",
          "'werden' functions as a standalone verb meaning 'to become', as an auxiliary for the future tense (Futur I), and as the foundational auxiliary for the passive voice.",
          [{"de": "Der junge Arzt wird bald Chefarzt der Abteilung.", "en": "The young doctor will soon become head of the department."},
           {"de": "Im Winter wird es schon um vier Uhr nachmittags dunkel.", "en": "In winter it gets dark already at four o'clock in the afternoon."}],
          ["Stem vowel changes e -> i (du wirst, er wird)", "Standalone meaning: to become (never 'to get' in the sense of receiving)", "Foundation for Futur I (werden + Infinitiv)"],
          ["Verbs", "werden"])

    add_t(39, "Vowel-Changing Verbs: e -> i (sprechen, helfen, geben)",
          "Verbs & Conjugation",
          "Stem vowel 'e' changes to 'i' only for 'du' and 'er/sie/es'",
          "Many strong German verbs alter their root vowel in the 2nd (du) and 3rd (er/sie/es) person singular of the present tense. All other grammatical persons retain the regular stem.",
          [{"de": "Er spricht fließend Deutsch und Französisch.", "en": "He speaks German and French fluently."},
           {"de": "Hilfst du mir bitte beim Tragen dieser Kisten?", "en": "Will you please help me carry these boxes?"}],
          ["geben: du gibst, er gibt", "helfen: du hilfst, er hilft", "wir and ihr do NOT change: wir helfen, ihr helft"],
          ["Verbs", "Vowel Change", "Strong Verbs"])

    add_t(40, "Vowel-Changing Verbs: e -> ie (sehen, lesen)",
          "Verbs & Conjugation",
          "Stem vowel 'e' lengthens to 'ie' only for 'du' and 'er/sie/es'",
          "Similar to the e->i pattern, certain common strong verbs lengthen their stem vowel to 'ie' in the 2nd and 3rd person singular.",
          [{"de": "Sieht er heute Abend den Dokumentarfilm?", "en": "Is he watching the documentary film this evening?"},
           {"de": "Du liest jeden Tag die Nachrichten auf deinem Tablet.", "en": "You read the news on your tablet every day."}],
          ["sehen: du siehst, er sieht", "lesen: du liest, er liest (note: also drops 's' because stem ends in s)", "wir sehen, ihr seht (no vowel shift)"],
          ["Verbs", "Vowel Change"])

    add_t(41, "Vowel-Changing Verbs: a -> ä (fahren, schlafen, waschen)",
          "Verbs & Conjugation",
          "Stem vowel 'a' receives an umlaut 'ä' only for 'du' and 'er/sie/es'",
          "Verbs with 'a' in the stem often add an umlaut in the 2nd and 3rd person singular present tense.",
          [{"de": "Fährst du morgen mit der Bahn oder mit dem Auto?", "en": "Are you traveling tomorrow by train or by car?"},
           {"de": "Das Baby schläft ruhig in seinem Zimmer.", "en": "The baby is sleeping quietly in its room."}],
          ["fahren: du fährst, er fährt", "schlafen: du schläfst, er schläft", "waschen: du wäschst, er wäscht"],
          ["Verbs", "Vowel Change", "Umlaut"])

    add_t(42, "Vowel-Changing Verbs: au -> äu (laufen)",
          "Verbs & Conjugation",
          "Stem diphthong 'au' changes to 'äu' for 'du' and 'er/sie/es'",
          "The verb 'laufen' (to run/walk) and 'saufen' shift their diphthong from 'au' to 'äu' in the singular 2nd and 3rd persons.",
          [{"de": "Er läuft jeden Morgen fünf Kilometer durch den Wald.", "en": "He runs five kilometers through the forest every morning."},
           {"de": "Läufst du heute mit uns zum Bahnhof?", "en": "Are you walking with us to the train station today?"}],
          ["ich laufe, du läufst, er läuft", "wir laufen, ihr lauft, sie laufen", "Diphthong sounds like 'oy' in 'boy'"],
          ["Verbs", "Vowel Change"])

    add_t(43, "Modal Verb: 'können' (Ability & Possibility)",
          "Modal Verbs",
          "ich kann, du kannst, er/sie/es kann, wir können, ihr könnt, sie/Sie können",
          "'können' expresses physical or intellectual capability ('can', 'be able to') or objective possibility. Notice that singular forms drop the umlaut and 1st/3rd person singular have no ending.",
          [{"de": "Ich kann sehr gut schwimmen und Ski fahren.", "en": "I can swim and ski very well."},
           {"de": "Kannst du mir den Weg zum Bahnhof erklären?", "en": "Can you explain the way to the train station to me?"}],
          ["No ending for ich and er/sie/es: ich kann, er kann", "Modal verb takes Position 2; secondary infinitive goes to the very end of the clause", "Singular loses umlaut: können -> ich kann"],
          ["Modal Verbs", "können"])

    add_t(44, "Modal Verb: 'müssen' (Necessity & Compulsion)",
          "Modal Verbs",
          "ich muss, du musst, er/sie/es muss, wir müssen, ihr müsst, sie/Sie müssen",
          "'müssen' expresses external compulsion or objective necessity ('must', 'have to'). Negated 'nicht müssen' means 'do not have to' (not 'must not'!).",
          [{"de": "Ich muss heute länger im Büro arbeiten.", "en": "I have to work longer in the office today."},
           {"de": "Du musst die Rechnung nicht sofort bezahlen.", "en": "You do not have to pay the invoice immediately."}],
          ["ich muss, er muss (no personal ending)", "'nicht müssen' = need not / do not have to", "To express 'must not', use 'nicht dürfen'!"],
          ["Modal Verbs", "müssen"])

    add_t(45, "Modal Verb: 'dürfen' (Permission & Prohibition)",
          "Modal Verbs",
          "ich darf, du darfst, er/sie/es darf, wir dürfen, ihr dürft, sie/Sie dürfen",
          "'dürfen' denotes permission ('may', 'be allowed to'). Negated with 'nicht', it signifies a strict prohibition ('must not').",
          [{"de": "Hier darf man keine Fotos machen.", "en": "One is not allowed to take photos here / You must not take photos here."},
           {"de": "Darf ich mich zu Ihnen an den Tisch setzen?", "en": "May I sit at the table with you?"}],
          ["ich darf, er darf (vowel changes ü -> a in singular)", "'nicht dürfen' = strict prohibition (forbidden)", "Common in public notices: 'Rauchen verboten / Hier darf man nicht rauchen'"],
          ["Modal Verbs", "dürfen"])

    add_t(46, "Modal Verb: 'wollen' (Strong Will & Intention)",
          "Modal Verbs",
          "ich will, du willst, er/sie/es will, wir wollen, ihr wollt, sie/Sie wollen",
          "'wollen' expresses strong determination, objective intent, or deliberate will ('want to'). It differs from English 'will' (which is future tense).",
          [{"de": "Ich will dieses Jahr mein Deutsch auf B2-Niveau verbessern.", "en": "I want to improve my German to B2 level this year."},
           {"de": "Was wollt ihr am Wochenende unternehmen?", "en": "What do you want to do on the weekend?"}],
          ["'wollen' does NOT mean future tense (future = werden)", "Expresses definite intention or resolute will", "Polite alternative: möchten"],
          ["Modal Verbs", "wollen"])

    add_t(47, "Modal Verb: 'möchten' (Polite Wish / Would Like)",
          "Modal Verbs",
          "ich möchte, du möchtest, er/sie/es möchte, wir möchten, ihr möchtet, sie/Sie möchten",
          "'möchten' is the polite subjunctive form of mögen, used functionally as a modal verb to express polite requests and desires ('would like').",
          [{"de": "Ich möchte bitte ein Glas Mineralwasser bestellen.", "en": "I would like to order a glass of sparkling water, please."},
           {"de": "Möchten Sie einen Kaffee oder einen Tee?", "en": "Would you like a coffee or a tea?"}],
          ["Always polite in shops, cafés, and requests", "ich möchte and er möchte share the exact same form", "Can stand alone with an accusative noun: 'Ich möchte einen Kaffee'"],
          ["Modal Verbs", "möchten", "Polite"])

    add_t(48, "Modal Verb: 'sollen' (Duty, Recommendation & Assignment)",
          "Modal Verbs",
          "ich soll, du sollst, er/sie/es soll, wir sollen, ihr sollt, sie/Sie sollen",
          "'sollen' expresses an obligation originating from someone else's request, instruction, doctor's advice, or duty ('should', 'be supposed to').",
          [{"de": "Der Arzt sagt, ich soll viel Wasser trinken und mich ausruhen.", "en": "The doctor says I should drink plenty of water and rest."},
           {"de": "Soll ich das Fenster im Konferenzraum öffnen?", "en": "Shall I open the window in the conference room?"}],
          ["Does not change stem vowel in singular: ich soll, du sollst, er soll", "Refers to third-party instructions: 'Er soll anrufen' (he is supposed to call)", "Offers: 'Soll ich helfen?' (Shall I help?)"],
          ["Modal Verbs", "sollen"])

    add_t(49, "Modal Verb: 'mögen' (To Like)",
          "Modal Verbs",
          "ich mag, du magst, er/sie/es mag, wir mögen, ihr mögt, sie/Sie mögen",
          "'mögen' expresses liking someone or something (usually food, people, or hobbies). It frequently takes an accusative noun object without a second verb.",
          [{"de": "Ich mag italienische Küche und frische Pasta sehr.", "en": "I like Italian cuisine and fresh pasta very much."},
           {"de": "Magst du moderne Kunst oder klassische Musik?", "en": "Do you like modern art or classical music?"}],
          ["Vowel changes ö -> a in singular: ich mag, du magst, er mag", "Often used with nouns: Ich mag Schokolade", "For activities, prefer 'verb + gern': Ich schwimme gern"],
          ["Modal Verbs", "mögen"])

    add_t(50, "Sentence Bracket with Modal Verbs (Satzklammer)",
          "Modal Verbs",
          "Position 2: Conjugated Modal Verb | Sentence End: Bare Infinitive",
          "German syntax creates a 'verb bracket' (Satzklammer). The conjugated modal verb sits in Position 2, while the main action verb is sent in its infinitive form to the very end of the clause.",
          [{"de": "Wir müssen heute Abend den neuen Bericht fertig schreiben.", "en": "We have to finish writing the new report this evening."},
           {"de": "Kannst du mir morgen früh beim Umzug helfen?", "en": "Can you help me with the move tomorrow morning?"}],
          ["The conjugated verb and the final infinitive frame the sentence content", "Nothing can be placed after the infinitive in a standard main clause", "In questions, modal is in Position 1 or 2, infinitive remains at the end"],
          ["Syntax", "Sentence Structure", "Satzklammer"])

    # Build and write remaining topics up to 105 programmatically
    # We will generate comprehensive topics 51 to 105
    remaining_topics = [
        # (51-60) Separable & Inseparable Verbs
        (51, "Separable Verbs: The Concept (Trennbare Verben)", "Separable Verbs",
         "Prefix detaches in present tense and moves to the sentence end",
         "Separable verbs consist of a basic verb and a detachable prefix (e.g., aufstehen -> ich stehe auf). In main clauses, the prefix is kicked to the absolute end.",
         [{"de": "Ich stehe jeden Wochentag um sechs Uhr auf.", "en": "I get up at six o'clock every weekday."},
          {"de": "Der Zug kommt pünktlich in Berlin an.", "en": "The train arrives punctually in Berlin."}],
         ["Prefix is always stressed in pronunciation", "Prefix goes to the very end of the main clause", "Infinitive remains unified: aufstehen"], ["Separable Verbs", "Prefixes"]),

        (52, "Separable Prefix 'an-' (Starting, Contact, Action)", "Separable Verbs",
         "anfangen (start), anrufen (call), ankommen (arrive), anmachen (turn on)",
         "The prefix 'an-' often indicates initiation of an action, connection, or turning an appliance on.",
         [{"de": "Der Deutschkurs fängt nächsten Montag an.", "en": "The German course starts next Monday."},
          {"de": "Rufst du deine Eltern am Wochenende an?", "en": "Are you calling your parents on the weekend?"}],
         ["anrufen takes the Accusative: Ich rufe dich an", "ankommen takes prepositions in/an: ankommen in Berlin", "Opposite of anmachen is ausmachen"], ["Separable Verbs", "an-"]),

        (53, "Separable Prefix 'auf-' (Opening, Upward, Ceasing)", "Separable Verbs",
         "aufstehen (get up), aufmachen (open), aufhören (stop), aufräumen (clean up)",
         "The prefix 'auf-' frequently signifies upward motion, opening objects, or bringing an action to completion.",
         [{"de": "Machst du bitte das Fenster im Schlafzimmer auf?", "en": "Will you please open the window in the bedroom?"}],
         ["aufhören mit + Dativ: Ich höre mit dem Rauchen auf", "aufmachen = öffnen", "aufräumen = to tidy up"], ["Separable Verbs", "auf-"]),

        (54, "Separable Prefix 'aus-' (Exiting, Turning Off)", "Separable Verbs",
         "aussteigen (get off), ausmachen (turn off), ausziehen (move out / undress)",
         "The prefix 'aus-' indicates movement outward, exiting vehicles, or turning off lights and devices.",
         [{"de": "An der nächsten Haltestelle steige ich aus.", "en": "At the next stop, I get off."}],
         ["aussteigen aus + Dativ: aus dem Bus aussteigen", "Opposite is einsteigen (get on)", "umsteigen = transfer/change trains"], ["Separable Verbs", "aus-"]),

        (55, "Separable Prefix 'ein-' (Entering, Inside)", "Separable Verbs",
         "einkaufen (shop), einladen (invite), einsteigen (board), einziehen (move in)",
         "The prefix 'ein-' denotes movement inward or participation in an activity.",
         [{"de": "Wir kaufen samstags im Supermarkt ein.", "en": "We shop at the supermarket on Saturdays."}],
         ["einladen takes Accusative + zu: Ich lade dich zu meiner Party ein", "einkaufen can be used without an object", "einsteigen in + Akkusativ: in den Zug einsteigen"], ["Separable Verbs", "ein-"]),

        (56, "Separable Prefix 'mit-' (Together, Accompaniment)", "Separable Verbs",
         "mitkommen (come along), mitbringen (bring along), mitmachen (participate)",
         "The prefix 'mit-' indicates participation, accompaniment, or doing something together with others.",
         [{"de": "Kommst du heute Abend mit ins Kino?", "en": "Are you coming along to the cinema tonight?"}],
         ["mitbringen = to bring along", "mitkommen = to come with/along", "mitnehmen = to take along"], ["Separable Verbs", "mit-"]),

        (57, "Separable Prefix 'vor-' (In Front, Advance, Demonstration)", "Separable Verbs",
         "vorstellen (introduce), vorbereiten (prepare), vorhaben (plan/intend)",
         "The prefix 'vor-' conveys forward movement, doing something in advance, or performing an action in front of someone.",
         [{"de": "Ich stelle Ihnen meinen neuen Kollegen vor.", "en": "I introduce my new colleague to you."}],
         ["sich vorstellen = to introduce oneself", "vorhaben = to have plans: Was hast du vor?", "vorbereiten auf + Akk = to prepare for"], ["Separable Verbs", "vor-"]),

        (58, "Separable Prefix 'zu-' (Closing, Towards)", "Separable Verbs",
         "zumachen (close), zuhören (listen), zunehmen (increase/gain)",
         "The prefix 'zu-' often denotes closing something or directing sensory focus toward someone.",
         [{"de": "Bitte mach die Tür zu, es ist kalt.", "en": "Please close the door; it is cold."}],
         ["zumachen = schließen", "zuhören takes Dativ: Hör mir bitte zu!", "Opposite is aufmachen"], ["Separable Verbs", "zu-"]),

        (59, "Separable Verbs with Modal Verbs (No Separation!)", "Separable Verbs",
         "Modal in Pos 2 + Separable Verb stays unified at the sentence end",
         "When a separable verb is governed by a modal verb, it does NOT separate. The entire verb remains intact in the infinitive at the end of the sentence.",
         [{"de": "Ich muss morgen früh um sechs Uhr aufstehen.", "en": "I have to get up at six o'clock tomorrow morning."}],
         ["No separation: 'aufstehen' stays one word at the end", "Modal takes the conjugation: 'muss', 'kann', 'will'", "Never say: 'Ich muss stehe auf'!"], ["Separable Verbs", "Modals", "Syntax"]),

        (60, "Inseparable Verbs (Untrennbare Verben: be-, ent-, er-, ver-, zer-)", "Separable Verbs",
         "Prefix NEVER detaches; stress falls on the root verb",
         "Inseparable prefixes (be-, emp-, ent-, er-, ge-, miss-, ver-, zer-) never separate from the verb. The prefix is unstressed, and no ge- is added in the past participle.",
         [{"de": "Ich verstehe die deutsche Grammatik immer besser.", "en": "I understand German grammar better and better."},
          {"de": "Er bezahlt die Rechnung mit seiner Kreditkarte.", "en": "He pays the invoice with his credit card."}],
         ["Never separate: ich verstehe (never 'ich stehe ver')", "Mnemonic: be-emp-ent-er-ge-miss-ver-zer", "Prefix is never stressed in pronunciation"], ["Inseparable Verbs", "Prefixes"]),

        # (61-75) Cases: Nominative and Accusative
        (61, "The Four German Cases: Purpose and Concept", "Cases (Kasus)",
         "Nominativ (Subject), Akkusativ (Direct Object), Dativ (Indirect Object), Genitiv (Possession)",
         "Cases reveal the grammatical function of each word in a sentence through article and adjective endings, allowing German flexible word order.",
         [{"de": "Der Mann (Nom) gibt dem Kind (Dat) den Ball (Akk).", "en": "The man gives the child the ball."}],
         ["Cases prevent ambiguity when word order changes", "Nominative answers: Wer oder was? (Who or what?)", "Accusative answers: Wen oder was? (Whom or what?)"], ["Cases", "Fundamentals"]),

        (62, "The Nominative Case: The Sentence Subject", "Cases (Kasus)",
         "Subject of the verb | Predicate noun after sein, werden, bleiben",
         "The nominative case identifies the person or thing performing the action. It is also used after copular linking verbs like sein, werden, and bleiben.",
         [{"de": "Der neue Mitarbeiter ist ein fähiger Ingenieur.", "en": "The new employee is a capable engineer."}],
         ["Always answers: Wer? (Who?) or Was? (What?)", "sein + Nominativ: Er ist ein guter Arzt (not einen)", "Default dictionary form of all nouns"], ["Nominative", "Cases"]),

        (63, "The Accusative Case: The Direct Object", "Cases (Kasus)",
         "Masculine der -> den, ein -> einen | Feminine, Neuter, Plural stay identical to Nominative",
         "The accusative case denotes the direct receiver of an action. Notice that ONLY masculine singular changes its article; feminine, neuter, and plural stay visually identical to nominative.",
         [{"de": "Ich kaufe den schwarzen Rucksack.", "en": "I buy the black backpack."},
          {"de": "Wir trinken einen heißen Kaffee.", "en": "We drink a hot coffee."}],
         ["Masculine der -> den, ein -> einen, kein -> keinen", "Feminine die -> die, eine -> eine", "Neuter das -> das, ein -> ein"], ["Accusative", "Cases"]),

        (64, "Core Verbs Governing the Accusative Case", "Cases (Kasus)",
         "haben, brauchen, kaufen, suchen, sehen, essen, trinken, finden, kennen, nehmen",
         "Transitive verbs in German require their object to appear in the accusative case. Remembering this list ensures correct article endings for everyday verbs.",
         [{"de": "Ich brauche einen neuen Laptop für die Arbeit.", "en": "I need a new laptop for work."}],
         ["haben takes Accusative: Ich habe einen Hund", "brauchen takes Accusative: Er braucht einen Stift", "kennen takes Accusative: Kennst du den neuen Nachbarn?"], ["Accusative Verbs", "Cases"]),

        (65, "The Idiomatic Expression 'Es gibt' + Accusative", "Cases (Kasus)",
         "Es gibt + Akkusativ = There is / There are",
         "'Es gibt' translates to 'there is' or 'there are' and ALWAYS requires its following noun to be in the accusative case.",
         [{"de": "In Berlin gibt es einen berühmten Fernsehturm.", "en": "In Berlin there is a famous TV tower."},
          {"de": "Gibt es hier in der Nähe ein gutes Restaurant?", "en": "Is there a good restaurant nearby?"}],
         ["'es gibt' always takes singular verb form 'gibt'", "Masculine nouns change: Es gibt einen Park", "Never say: 'Es gibt der Park'!"], ["Es gibt", "Accusative"]),

        (66, "Accusative Preposition: 'für' (for)", "Prepositions",
         "für + Akkusativ | Contraction: fürs (für das)",
         "'für' expresses purpose, beneficiary, or duration, and strictly governs the accusative case.",
         [{"de": "Dieses Geschenk ist für meinen besten Freund.", "en": "This gift is for my best friend."}],
         ["Always accusative: für den, für die, für das", "Contraction: fürs Auto, fürs Kind", "Never followed by dative"], ["Prepositions", "für", "Accusative"]),

        (67, "Accusative Preposition: 'ohne' (without)", "Prepositions",
         "ohne + Akkusativ | Frequently takes zero article",
         "'ohne' denotes the absence or lack of something and always governs the accusative case. It often appears without an article before singular abstract nouns.",
         [{"de": "Ohne meinen Kaffee kann ich morgens nicht arbeiten.", "en": "Without my coffee, I cannot work in the morning."},
          {"de": "Er reist ohne Gepäck nach Paris.", "en": "He travels without luggage to Paris."}],
         ["Always accusative: ohne den Schlüssel", "Often takes Nullartikel: ohne Zucker, ohne Milch", "Opposite of 'mit' (which takes Dative!)"], ["Prepositions", "ohne", "Accusative"]),

        (68, "Accusative Preposition: 'durch' (through, by means of)", "Prepositions",
         "durch + Akkusativ | Contraction: durchs (durch das)",
         "'durch' indicates spatial movement through something or the instrument/cause of an action.",
         [{"de": "Wir spazieren durch den grünen Stadtpark.", "en": "We are strolling through the green city park."}],
         ["durch den Park (masculine accusative)", "Contraction: durchs Fenster", "Always accusative"], ["Prepositions", "durch", "Accusative"]),

        (69, "Accusative Preposition: 'um' (around, at a specific time)", "Prepositions",
         "um + Akkusativ | Spatial: around | Temporal: at (clock time)",
         "'um' indicates spatial movement around an object or exact clock time.",
         [{"de": "Der Bus fährt um die historische Altstadt herum.", "en": "The bus drives around the historic old town."},
          {"de": "Das Konzert beginnt um Punkt acht Uhr.", "en": "The concert begins at eight o'clock sharp."}],
         ["Time: um 8 Uhr, um Mitternacht", "Spatial: um den Tisch, um die Ecke", "Always accusative"], ["Prepositions", "um", "Accusative"]),

        (70, "Accusative Preposition: 'gegen' (against, around approximate time)", "Prepositions",
         "gegen + Akkusativ | Physical: against | Temporal: around approximate time",
         "'gegen' denotes physical collision/opposition or approximate time.",
         [{"de": "Er lehnte sein Fahrrad gegen die Wand.", "en": "He leaned his bicycle against the wall."},
          {"de": "Ich treffe dich heute gegen 18 Uhr.", "en": "I will meet you today around 6 PM."}],
         ["Physical opposition: gegen den Strom", "Approximate time: gegen Mittag, gegen 19 Uhr", "Always accusative"], ["Prepositions", "gegen", "Accusative"]),

        (71, "Accusative Preposition: 'bis' (until, up to)", "Prepositions",
         "bis + Akkusativ | Usually followed directly by adverbs, dates, or secondary prepositions",
         "'bis' expresses a spatial or temporal terminus ('until', 'as far as'). When followed by an article, it is almost always paired with another preposition (bis zum, bis an das).",
         [{"de": "Ich bleibe bis nächsten Montag in Berlin.", "en": "I am staying in Berlin until next Monday."},
          {"de": "Der Zug fährt nur bis Hannover.", "en": "The train only runs as far as Hanover."}],
         ["bis morgen, bis bald, bis später", "With articles, paired: bis zu + Dativ (bis zum Bahnhof)", "Always accusative"], ["Prepositions", "bis", "Accusative"]),

        (72, "Mnemonic for Pure Accusative Prepositions: FUD-BOG", "Prepositions",
         "F - für | U - um | D - durch | B - bis | O - ohne | G - gegen",
         "The acronym FUD-BOG or DOGFU helps learners remember the six primary prepositions that strictly require the accusative case.",
         [{"de": "Wir laufen ohne den Hund durch den Park für die Gesundheit.", "en": "We walk without the dog through the park for our health."}],
         ["F - für", "U - um", "D - durch", "B - bis", "O - ohne", "G - gegen"], ["Prepositions", "Mnemonic", "Accusative"]),

        # (73-85) Word Order & Sentence Structure in A1
        (73, "Standard Word Order: The V2 Rule (Verb in Position 2)", "Sentence Structure",
         "Position 1 (Any element) | Position 2 (Conjugated Verb) | Position 3 (Subject if not in Pos 1)",
         "In standard German declarative sentences, the conjugated verb MUST occupy Position 2. If an element other than the subject occupies Position 1, the subject immediately follows the verb (Inversion).",
         [{"de": "Ich trinke morgens einen Kaffee. / Morgens trinke ich einen Kaffee.", "en": "I drink a coffee in the morning. / In the morning I drink a coffee."}],
         ["Verb is always in Position 2 in statements", "Position 1 can be subject, time, place, or object", "If time/place takes Position 1, subject moves to Position 3"], ["Word Order", "Syntax", "V2"]),

        (74, "Yes/No Questions (Ja/Nein-Fragen): Verb in Position 1", "Sentence Structure",
         "Position 1: Conjugated Verb | Position 2: Subject | Rest of sentence",
         "In yes/no questions, the conjugated verb moves to Position 1, followed directly by the subject.",
         [{"de": "Kommst du heute Abend mit zum Abendessen?", "en": "Are you coming along to dinner this evening?"},
          {"de": "Wohnen Sie schon lange in dieser Straße?", "en": "Have you been living on this street for a long time?"}],
         ["Verb is strictly in Position 1", "Answers usually begin with Ja, Nein, or Doch", "Subject immediately follows the verb"], ["Questions", "Word Order"]),

        (75, "Information Questions with W-Words (W-Fragen)", "Sentence Structure",
         "Position 1: W-Word | Position 2: Conjugated Verb | Position 3: Subject",
         "Open-ended questions begin with a question word (W-Wort). The conjugated verb stays in Position 2.",
         [{"de": "Woher kommst du und wo wohnst du jetzt?", "en": "Where do you come from and where do you live now?"},
          {"de": "Wann beginnt die Vorlesung an der Universität?", "en": "When does the lecture begin at the university?"}],
         ["Wer? (Who?), Was? (What?), Wo? (Where?), Woher? (Where from?)", "Wohin? (Where to?), Wann? (When?), Warum? (Why?), Wie? (How?)", "Verb is strictly in Position 2"], ["Questions", "W-Questions"]),

        (76, "The Three Core Question Words for Location: Wo, Woher, Wohin", "Sentence Structure",
         "Wo = static location (Where?) | Woher = origin (Where from?) | Wohin = direction (Where to?)",
         "German distinguishes static location from directional movement when asking about location.",
         [{"de": "Wo ist der Schlüssel? Woher hast du ihn? Wohin legst du ihn?", "en": "Where is the key? Where did you get it from? Where are you putting it?"}],
         ["Wo? + Dativ (static location)", "Wohin? + Akkusativ (destination/movement)", "Woher? + aus/von (point of origin)"], ["Questions", "Location"]),

        (77, "Answering Negative Questions: 'Doch' vs 'Ja' and 'Nein'", "Sentence Structure",
         "Positive answer to negative question = Doch! | Affirming negative = Nein",
         "When someone asks a negative question ('Hast du keinen Kaffee?'), English speakers are confused. In German, use 'Doch!' to contradict the negative question affirmatively.",
         [{"de": "Kommst du nicht mit? - Doch, ich komme gerne mit!", "en": "Aren't you coming along? - Yes (on the contrary), I'd love to come!"},
          {"de": "Hast du kein Auto? - Nein, ich fahre mit dem Zug.", "en": "Don't you have a car? - No, I travel by train."}],
         ["Negative question: 'Hast du kein Geld?'", "If you DO have money: 'Doch!'", "If you DO NOT have money: 'Nein.'"], ["Doch", "Negation", "Conversational"]),

        (78, "Negation with 'nicht': Position Rules", "Sentence Structure",
         "Negating entire sentence -> 'nicht' at the very end | Negating specific element -> 'nicht' right before it",
         "'nicht' negates verbs, adjectives, adverbs, and specific sentence components. Its placement depends on whether the whole clause or a specific word is negated.",
         [{"de": "Ich verstehe diesen schwierigen Satz nicht.", "en": "I do not understand this difficult sentence."},
          {"de": "Das Restaurant ist heute nicht teuer, sondern günstig.", "en": "The restaurant is not expensive today, but cheap."}],
         ["Negating a verb: nicht goes to the end of the clause", "Before adjectives: nicht gut, nicht kalt", "Before prepositions: nicht in den Park"], ["Negation", "nicht"]),

        (79, "Co-ordinating Conjunctions: ADUSO (aber, denn, und, sondern, oder)", "Conjunctions",
         "Position Zero conjunctions: Do not alter the standard V2 word order in the clause that follows",
         "The conjunctions Aber, Denn, Und, Sondern, Oder connect two main clauses without consuming a grammatical position (Position 0). The subject follows in Position 1 and the verb in Position 2.",
         [{"de": "Ich trinke gerne Tee, aber mein Bruder bevorzugt Kaffee.", "en": "I like drinking tea, but my brother prefers coffee."},
          {"de": "Er kommt heute nicht, denn er ist krank.", "en": "He is not coming today, because he is sick."}],
         ["A - aber (but)", "D - denn (because/for)", "U - und (and)", "S - sondern (but rather, after negation)", "O - oder (or)"], ["Conjunctions", "ADUSO", "Word Order"]),

        (80, "The Contrast: 'aber' vs 'sondern'", "Conjunctions",
         "sondern = but rather (requires preceding negation) | aber = but (general contrast)",
         "'sondern' is exclusively used after a negative clause to replace the negated concept with the correct one. 'aber' introduces a general limitation or contrast.",
         [{"de": "Wir fahren nicht nach Berlin, sondern nach München.", "en": "We are not traveling to Berlin, but rather to Munich."},
          {"de": "Er ist sehr müde, aber er arbeitet trotzdem weiter.", "en": "He is very tired, but he continues working anyway."}],
         ["'sondern' requires 'nicht' or 'kein' in the first clause", "It corrects the negated statement: Not X, but rather Y", "'aber' can follow positive or negative statements"], ["Conjunctions", "sondern"]),

        (81, "The Imperative for 'du' (Informal Singular Command)", "Verbs & Conjugation",
         "Take verb stem (infinitive minus -en); omit pronoun 'du' and ending -st",
         "To give a command to a friend, drop the 'du' and remove the '-st' ending. If the verb has an e->i vowel change, the imperative retains the change.",
         [{"de": "Komm bitte pünktlich zum Treffpunkt!", "en": "Please come punctually to the meeting point!"},
          {"de": "Lies diesen interessanten Artikel über Solarenergie!", "en": "Read this interesting article about solar energy!"}],
         ["kommen -> du kommst -> Komm!", "lesen -> du liest -> Lies! (keeps e->ie change)", "Verbs with a->ä DROP the umlaut: fahren -> Fahr! (not Fähr!)"], ["Imperative", "du"]),

        (82, "The Imperative for 'ihr' (Informal Plural Command)", "Verbs & Conjugation",
         "Use regular 'ihr' present tense form; omit the pronoun 'ihr'",
         "To command a group of friends, simply take the regular present tense verb form for 'ihr' and omit the pronoun.",
         [{"de": "Macht bitte eure Bücher auf Seite 20 auf!", "en": "Please open your books to page 20!"},
          {"de": "Wartet hier einen kurzen Moment!", "en": "Wait here for a brief moment!"}],
         ["ihr macht -> Macht!", "ihr hört zu -> Hört zu!", "Pronoun 'ihr' is deleted"], ["Imperative", "ihr"]),

        (83, "The Imperative for 'Sie' (Formal Command)", "Verbs & Conjugation",
         "Invert verb and pronoun: Verb (infinitive form) + Sie!",
         "The formal imperative is created by taking the infinitive and placing 'Sie' directly after it. 'sein' has an irregular form: 'Seien Sie!'.",
         [{"de": "Steigen Sie bitte vorsichtig in den Zug ein!", "en": "Please board the train carefully!"},
          {"de": "Seien Sie bitte leise während des Vortrags!", "en": "Please be quiet during the lecture!"}],
         ["Always keep the pronoun 'Sie': Kommen Sie bitte!", "Irregular: sein -> Seien Sie!", "Often softened with 'bitte'"], ["Imperative", "Formal"]),

        # (84-95) Time, Numbers, Dates, Adverbs
        (84, "Cardinal Numbers 0 to 100 & Inverted Units", "Numbers & Time",
         "From 21 to 99: Unit + und + Ten (einundzwanzig = 1 + and + 20)",
         "In German, compound two-digit numbers state the single digit before the tens digit, connected by 'und'.",
         [{"de": "Mein Kollege ist fünfunddreißig (35) Jahre alt.", "en": "My colleague is 35 years old."},
          {"de": "Das Buch kostet vierundzwanzig (24) Euro.", "en": "The book costs 24 euros."}],
         ["21 = einundzwanzig (note: 'ein' without s)", "Written as one single word", "Listen carefully to the unit digit first!"], ["Numbers", "Basics"]),

        (85, "Cardinal Numbers 100 to 1,000,000", "Numbers & Time",
         "hundert (100), tausend (1000), eine Million (1,000,000)",
         "Large numbers are chained into single long words up to thousands. 'Million' and 'Milliarde' are capitalized nouns.",
         [{"de": "In der Stadt leben über fünfhunderttausend Menschen.", "en": "Over 500,000 people live in the city."}],
         ["100 = (ein)hundert", "1,000 = (ein)tausend", "Million is a feminine noun: eine Million, zwei Millionen"], ["Numbers", "Big Numbers"]),

        (86, "Telling Time: Official 24-Hour System", "Numbers & Time",
         "Hours + Uhr + Minutes (e.g. 14:30 = vierzehn Uhr dreißig)",
         "The official 24-hour clock is used on train schedules, radio broadcasts, work appointments, and official announcements.",
         [{"de": "Der ICE nach Hamburg fährt um vierzehn Uhr zweiundzwanzig (14:22) ab.", "en": "The ICE train to Hamburg departs at 14:22."}],
         ["Format: Stunde + 'Uhr' + Minute", "14:15 = vierzehn Uhr fünfzehn", "No AM/PM in German; official context uses 0-24"], ["Time", "24-Hour"]),

        (87, "Telling Time: Colloquial 12-Hour System", "Numbers & Time",
         "vor (before), nach (past), halb (half to), Viertel vor / Viertel nach",
         "In everyday spoken German, time uses a 12-hour perspective with relative markers. Watch out: 'halb vier' means 3:30 (halfway TO four), not 4:30!",
         [{"de": "Wir treffen uns um Viertel nach drei im Café.", "en": "We meet at a quarter past three in the café."},
          {"de": "Es ist jetzt genau halb fünf (16:30).", "en": "It is now exactly half past four (16:30)."}],
         ["halb vier = 3:30 (half an hour before 4!)", "Viertel nach drei = 3:15", "Viertel vor vier = 3:45"], ["Time", "Colloquial"]),

        (88, "Days of the Week & Temporal Preposition 'am'", "Numbers & Time",
         "Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag/Sonnabend, Sonntag | Preposition: am",
         "All days of the week are masculine (der Montag). To say 'on Monday', German uses the contracted preposition 'am' (an + dem).",
         [{"de": "Am Samstag gehe ich mit meinen Freunden joggen.", "en": "On Saturday I go jogging with my friends."},
          {"de": "Mittwochs habe ich immer meinen Sprachkurs.", "en": "On Wednesdays I always have my language course."}],
         ["am Montag, am Wochenende", "With lowercase -s means recurring: montags (every Monday)", "All days and months are masculine (der)"], ["Days", "Time", "Prepositions"]),

        (89, "Months, Seasons & Temporal Preposition 'im'", "Numbers & Time",
         "Januar, Februar, März, April, Mai, Juni, Juli, August, September, Oktober, November, Dezember | Preposition: im",
         "All months and seasons are masculine (der Frühling, der Sommer, der Herbst, der Winter). The preposition used with months and seasons is 'im' (in + dem).",
         [{"de": "Im Juli und August haben viele Universitäten Sommerpause.", "en": "In July and August, many universities have summer break."}],
         ["Preposition: im Januar, im Sommer", "All months and seasons are masculine: der Mai, der Herbst", "Contracted from in + dem = im"], ["Months", "Seasons"]),

        (90, "Ordinal Numbers & Calendar Dates", "Numbers & Time",
         "1st to 19th: number + -te (am + -ten) | 20th+: number + -ste (am + -sten)",
         "Dates use ordinal numbers. In written German, an ordinal is represented by a period after the number (z.B. der 1. Mai = der erste Mai). When preceded by 'am', it takes the ending '-ten'.",
         [{"de": "Heute ist der fünfzehnte November.", "en": "Today is the fifteenth of November."},
          {"de": "Mein Geburtstag ist am vierten Juni.", "en": "My birthday is on the fourth of June."}],
         ["der erste, der dritte, der siebte (irregular stems)", "am + -ten: am ersten Mai, am zwanzigsten Oktober", "A period after a number signifies an ordinal: 1. = erste"], ["Dates", "Ordinals"]),

        (91, "Temporal Adverbs of Frequency", "Sentence Structure",
         "immer (always), meistens (mostly), oft (often), manchmal (sometimes), selten (seldom), nie (never)",
         "Frequency adverbs describe how often actions take place and usually sit directly after the conjugated verb or in Position 1 for emphasis.",
         [{"de": "Ich trinke morgens immer eine Tasse grünen Tee.", "en": "I always drink a cup of green tea in the morning."},
          {"de": "Manchmal fahre ich mit dem Fahrrad zur Universität.", "en": "Sometimes I ride my bicycle to the university."}],
         ["immer (100%) -> meistens (80%) -> oft (60%)", "manchmal (40%) -> selten (15%) -> nie (0%)", "Position 1 causes inversion: 'Manchmal fahre ich...'"], ["Adverbs", "Frequency"]),

        (92, "Expressing Likes with 'gern / gerne' vs 'mögen'", "Sentence Structure",
         "Verb + gern = to like doing [verb] | mögen + Noun = to like [noun]",
         "In German, 'liking an activity' is expressed by adding the adverb 'gern' after the verb, rather than using a verb for 'to like'.",
         [{"de": "Ich koche gerne am Wochenende für meine Familie.", "en": "I like to cook for my family on the weekend."},
          {"de": "Mein Freund liest sehr gerne historische Romane.", "en": "My friend likes reading historical novels very much."}],
         ["'Ich schwimme gern' = I like swimming", "'gern' and 'gerne' are interchangeable", "Negation: 'nicht gern' = do not like to"], ["gern", "Verbs"]),

        (93, "Adverbs of Place: hier, da, dort, überall", "Sentence Structure",
         "hier (here, close) | da (there, medium) | dort (over there, far) | überall (everywhere)",
         "Spatial adverbs define location without requiring a prepositional phrase.",
         [{"de": "Hier ist mein Arbeitsplatz und dort drüben steht der Drucker.", "en": "Here is my workplace and over there stands the printer."}],
         ["hier = right here with speaker", "dort = visible or known distant location", "da = versatile colloquial pointer"], ["Adverbs", "Location"]),

        (94, "Basic Temporal Adverbs: heute, morgen, gestern, jetzt, bald", "Sentence Structure",
         "gestern (yesterday) < heute (today) < morgen (tomorrow) | jetzt (now) | bald (soon)",
         "Core temporal adverbs locate events in time. Notice that 'morgen' (lowercase: tomorrow) differs from 'der Morgen' (capitalized: the morning).",
         [{"de": "Heute lerne ich Grammatik und morgen schreibe ich den Test.", "en": "Today I study grammar and tomorrow I take the test."}],
         ["gestern -> heute -> morgen", "jetzt (now), bald (soon), später (later)", "morgen früh = tomorrow morning"], ["Adverbs", "Time"]),

        # (95-105) Daily Communication, Essential Particles & Greetings
        (95, "Greetings & Farewells across Formal & Regional Registers", "Dialogue Patterns",
         "Formal: Guten Morgen/Tag/Abend, Auf Wiedersehen | Informal: Hallo, Tschüss | Regional: Servus, Moin, Grüß Gott",
         "Selecting the appropriate greeting reflects social awareness and regional culture in German-speaking lands.",
         [{"de": "Guten Tag, wie kann ich Ihnen heute helfen?", "en": "Good day, how can I help you today?"},
          {"de": "Moin! Wie geht es dir heute?", "en": "Morning! How are you today? (North German)"}],
         ["Auf Wiedersehen (formal in person) vs Auf Wiederhören (on phone)", "Moin (Northern Germany, all day)", "Servus / Grüß Gott (Bavaria & Austria)"], ["Greetings", "Culture"]),

        (96, "Introducing Yourself: Name, Origin, Profession, Age", "Dialogue Patterns",
         "Ich heiße... / Ich bin... | Ich komme aus... | Ich wohne in... | Ich bin ... Jahre alt",
         "Essential speech formulas for personal introductions in social and professional contexts.",
         [{"de": "Ich heiße Ajay, komme aus Indien und wohne in Berlin.", "en": "My name is Ajay, I come from India and live in Berlin."},
          {"de": "Ich bin von Beruf Softwareingenieur.", "en": "I am a software engineer by profession."}],
         ["Name: Ich heiße / Mein Name ist / Ich bin", "Origin: Ich komme aus + Land", "Profession: Ich arbeite als ... / Ich bin ..."], ["Introduction", "Speaking"]),

        (97, "Asking for Directions in the City", "Dialogue Patterns",
         "Entschuldigung, wo ist...? | Wie komme ich zu...? | nach links, nach rechts, geradeaus",
         "Standard polite formulas for navigating German public transit and streets.",
         [{"de": "Entschuldigung, wie komme ich am schnellsten zum Hauptbahnhof?", "en": "Excuse me, how do I get to the central station the fastest?"},
          {"de": "Gehen Sie geradeaus und dann die zweite Straße nach rechts.", "en": "Go straight ahead and then take the second street on the right."}],
         ["nach links (to the left), nach rechts (to the right)", "geradeaus (straight ahead)", "an der Kreuzung / an der Ampel"], ["Directions", "Navigation"]),

        (98, "Ordering in a Café or Restaurant", "Dialogue Patterns",
         "Ich möchte bitte... | Ich hätte gern... | Für mich bitte... | Zahlen, bitte!",
         "Polite linguistic conventions when ordering food and drinks in German gastronomy.",
         [{"de": "Ich hätte gerne einen Cappuccino und ein Stück Käsekuchen, bitte.", "en": "I would like a cappuccino and a piece of cheesecake, please."},
          {"de": "Entschuldigung, wir möchten bitte zahlen. Zusammen oder getrennt?", "en": "Excuse me, we would like to pay, please. Together or separately?"}],
         ["'Ich hätte gern' is softer and more polite than 'Ich will'", "'Zusammen oder getrennt?' = pay together or on separate bills", "Tipping: round up directly when paying"], ["Restaurant", "Gastronomy"]),

        (99, "Shopping & Inquiring about Prices", "Dialogue Patterns",
         "Was kostet...? | Wie viel kostet...? | Das macht zusammen... Euro",
         "Grammatical structures used when purchasing groceries, tickets, or retail items.",
         [{"de": "Was kosten zwei Kilo Bio-Äpfel?", "en": "How much do two kilos of organic apples cost?"},
          {"de": "Das macht zusammen achtzehn Euro und fünfzig Cent.", "en": "That makes eighteen euros and fifty cents all together."}],
         ["Wie viel kostet das? (How much does that cost?)", "Währung: Euro und Cent", "Kassenzettel / Beleg: receipt"], ["Shopping", "Prices"]),

        (100, "Making and Responding to Invitations", "Dialogue Patterns",
         "Hast du Lust auf...? | Wollen wir...? | Ja, gerne! / Tut mir leid, ich habe keine Zeit.",
         "Social formulas for proposing activities, accepting enthusiastically, or declining politely.",
         [{"de": "Hast du Lust, am Samstagabend mit uns Pizza essen zu gehen?", "en": "Do you feel like going out to eat pizza with us on Saturday evening?"},
          {"de": "Das klingt super, ich bin sehr gerne dabei!", "en": "That sounds great, I'd love to join!"}],
         ["Lust haben auf + Akkusativ: Lust auf Kaffee?", "Zeit haben für + Akkusativ: Zeit für Sport?", "Polite refusal: Leider habe ich schon etwas vor (I already have plans)"], ["Invitations", "Social"]),

        (101, "Apologies and Asking for Clarification", "Dialogue Patterns",
         "Entschuldigung! / Es tut mir leid. | Wie bitte? | Können Sie das bitte wiederholen?",
         "Crucial conversational repair mechanisms for beginner language learners.",
         [{"de": "Wie bitte? Könnten Sie bitte etwas langsamer sprechen?", "en": "Pardon? Could you please speak a little slower?"},
          {"de": "Es tut mir leid, das habe ich akustisch nicht verstanden.", "en": "I am sorry, I did not catch that acoustically."}],
         ["'Wie bitte?' is polite (never just 'Was?')", "Entschuldigung (mild excuse) vs Es tut mir leid (genuine sorrow)", "langsamer sprechen = speak slower"], ["Clarification", "Polite"]),

        (102, "Talking about the Weather with Impersonal 'es'", "Dialogue Patterns",
         "Es ist sonnig / kalt / warm | Es regnet / schneit / stürmt | Die Sonne scheint",
         "Describing meteorological conditions using impersonal verbs and adjectives.",
         [{"de": "Heute ist es angenehm warm und die Sonne scheint den ganzen Tag.", "en": "Today it is pleasantly warm and the sun is shining all day."}],
         ["es ist + Adjektiv: es ist windig, es ist neblig", "Verbs: es regnet, es schneit", "Temperature: Es sind zwanzig Grad"], ["Weather", "Nature"]),

        (103, "Describing Your Daily Routine (Tagesablauf)", "Dialogue Patterns",
         "aufstehen -> frühstücken -> zur Arbeit fahren -> Feierabend machen -> schlafen gehen",
         "Chronological sequencing of everyday actions using separable verbs and temporal adverbs.",
         [{"de": "Zuerst stehe ich auf, dann frühstücke ich und danach fahre ich ins Büro.", "en": "First I get up, then I eat breakfast, and after that I travel to the office."}],
         ["Sequencing connectors: zuerst (first), dann (then), danach (after that)", "Remember V2 inversion after dann/danach: 'dann frühstücke ich'", "Feierabend = end of work day"], ["Daily Routine", "Sequencing"]),

        (104, "Talking about Hobbies and Interests", "Dialogue Patterns",
         "Meine Hobbys sind... | In meiner Freizeit spiele ich... / lese ich...",
         "Expressing leisure activities with sports, music, and social interests.",
         [{"de": "In meiner Freizeit spiele ich gerne Gitarre und gehe im Park joggen.", "en": "In my free time, I like playing guitar and going jogging in the park."}],
         ["Instrumente spielen: ohne Artikel (Gitarre spielen)", "Sportarten: Fußball spielen, schwimmen gehen", "gern vs ungern: Ich koche ungern (I dislike cooking)"], ["Hobbies", "Leisure"]),

        (105, "The German Sentence Frame: Mastery Checklist for A1", "Sentence Structure",
         "Statements (V2), Yes/No (V1), W-Questions (W+V2), Modal/Separable Brackets",
         "A consolidated review of all foundational sentence structure rules mastered in Level A1.",
         [{"de": "Morgen kann ich dich um 15 Uhr am Bahnhof abholen.", "en": "Tomorrow I can pick you up at the station at 3 PM."}],
         ["V2 rule in standard statements", "Satzklammer with modal and separable verbs", "Accusative case for direct objects"], ["Summary", "Checklist", "A1 Mastery"])
    ]

    for item in remaining_topics:
        add_t(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])

    assert len(topics) == 105, f"Expected 105 A1 topics, got {len(topics)}"
    return topics

if __name__ == "__main__":
    t = get_a1_topics()
    with open("deutsche/data/a1.js", "w", encoding="utf-8") as f:
        f.write("// German Grammar Topics - Level A1 (Foundations) - Exactly 105 Topics\n")
        f.write("window.GERMAN_DATA_A1 = " + json.dumps(t, indent=2, ensure_ascii=False) + ";\n")
    print(f"✅ Generated deutsche/data/a1.js with {len(t)} topics!")
