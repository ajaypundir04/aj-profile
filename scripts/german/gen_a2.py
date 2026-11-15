#!/usr/bin/env python3
"""
Generator for Level A2 German Grammar Topics (105 Topics)
All examples are 100% original, modern real-world German examples.
Zero examples taken from reference PDF.
"""
import json

def get_a2_topics():
    topics = []
    
    def add_t(tid, title, cat, rule, explanation, examples, key_points, tags):
        topics.append({
            "id": f"de-a2-{tid}",
            "level": "A2",
            "category": cat,
            "title": title,
            "ruleBox": rule,
            "explanation": explanation,
            "examples": examples,
            "keyPoints": key_points,
            "tags": tags
        })

    # (1-15) The Dative Case (Dativ)
    add_t(1, "The Dative Case: Concept of the Indirect Object", "The Dative Case",
          "Dative marks the indirect beneficiary or recipient of an action (Wem?)",
          "The Dative case is used for the person or entity for whom or to whom an action is performed. In sentence structures with both direct and indirect objects, the recipient takes the dative.",
          [{"de": "Die Ärztin gibt dem Patienten ein Rezept für die Apotheke.", "en": "The doctor gives the patient a prescription for the pharmacy."},
           {"de": "Ich schenke meiner Schwester ein Buch zum Geburtstag.", "en": "I give my sister a book for her birthday."}],
          ["Answers the question: Wem? (To/for whom?)", "Masculine & Neuter articles become 'dem'", "Feminine article becomes 'der'"],
          ["Dative", "Cases", "Indirect Object"])

    add_t(2, "Dative Definite Articles: dem, der, dem, den (+ -n)", "The Dative Case",
          "Masc: dem | Fem: der | Neut: dem | Plural: den + Noun adds -n",
          "In the dative case, masculine and neuter nouns share the article 'dem', feminine nouns use 'der', and plural nouns use 'den' with an obligatory '-n' appended to the noun itself.",
          [{"de": "Wir helfen dem neuen Nachbarn beim Tragen der Kisten.", "en": "We help the new neighbor carry the boxes."},
           {"de": "Er antwortet der Lehrerin mit einer klugen Frage.", "en": "He answers the teacher with a clever question."}],
          ["Masculine & Neuter: dem", "Feminine: der (do not confuse with nominative masculine der!)", "Plural: den + -n on the noun (den Kindern)"],
          ["Dative", "Articles"])

    add_t(3, "Dative Indefinite Articles: einem, einer, einem", "The Dative Case",
          "Masc: einem | Fem: einer | Neut: einem | Plural: keinen (+ -n)",
          "The indefinite article reflects dative case endings: -em for masculine and neuter, -er for feminine. In the plural, the negative article 'keinen' or possessive determiners take -en.",
          [{"de": "Ich begegne jeden Morgen einem freundlichen Briefträger.", "en": "Every morning I encounter a friendly mail carrier."},
           {"de": "Sie vertraut einer erfahrenen Kollegin.", "en": "She trusts an experienced colleague."}],
          ["einem (masculine and neuter)", "einer (feminine)", "keinen Kindern (plural negative)"],
          ["Dative", "Articles", "Indefinite"])

    add_t(4, "The Dative Plural Noun Rule (-n Suffix)", "The Dative Case",
          "All plural nouns in the dative add an '-n' ending (unless plural ends in -n or -s)",
          "A crucial morphological rule in German: any noun in the dative plural must add an '-n' to its plural form, unless the plural already ends in -n (die Frauen -> den Frauen) or in -s (die Autos -> den Autos).",
          [{"de": "Der Lehrer erzählt den Kindern (das Kind -> die Kinder) eine Geschichte.", "en": "The teacher tells the children a story."},
           {"de": "Er hilft den Touristen (die Touristen) bei der Orientierung.", "en": "He helps the tourists find their way."}],
          ["die Kinder -> den Kindern", "die Tische -> den Tischen", "Words ending in -s do not add -n: den Autos, den Hotels"],
          ["Dative", "Plural", "Noun Suffix"])

    add_t(5, "Dative Personal Pronouns: mir, dir, ihm, ihr, ihm, uns, euch, ihnen, Ihnen", "The Dative Case",
          "1st: mir/uns | 2nd: dir/euch/Ihnen | 3rd: ihm/ihr/ihm/ihnen",
          "When personal pronouns function as dative objects, they adopt specialized dative pronoun forms.",
          [{"de": "Kannst du mir bitte das Salz reichen?", "en": "Can you please pass me the salt?"},
           {"de": "Ich danke Ihnen herzlich für Ihre Unterstützung.", "en": "I thank you cordially for your support. (formal)"}],
          ["du -> dir, Sie -> Ihnen (capitalized)", "er -> ihm, sie -> ihr, es -> ihm", "wir -> uns, ihr -> euch (same as accusative)"],
          ["Dative", "Pronouns"])

    add_t(6, "The Verb 'helfen' + Dative", "Verbs with Dative",
          "helfen + Dativ | Vowel change: du hilfst, er hilft",
          "'helfen' is one of the most common verbs in German that strictly requires its object to be in the dative case (never accusative).",
          [{"de": "Ich helfe meinem Vater bei der Gartenarbeit.", "en": "I help my father with the gardening."},
           {"de": "Können Sie uns bitte helfen?", "en": "Can you please help us?"}],
          ["Never say 'Ich helfe dich' -> always 'Ich helfe dir!'", "Vowel change in present: er hilft", "Past: er hat geholfen"],
          ["helfen", "Dative Verbs"])

    add_t(7, "The Verb 'danken' + Dative", "Verbs with Dative",
          "danken + Dativ (jemandem danken für etwas)",
          "Unlike English 'to thank someone' (direct object), German 'danken' requires the dative case for the person being thanked.",
          [{"de": "Wir danken Ihnen für Ihre freundliche Einladung.", "en": "We thank you for your kind invitation."},
           {"de": "Er dankt seinem Freund für die wertvolle Hilfe.", "en": "He thanks his friend for the valuable help."}],
          ["jemandem (Dat) danken", "danken für + Akkusativ", "Alternative: Ich bedanke mich bei Ihnen (reflexive)"],
          ["danken", "Dative Verbs"])

    add_t(8, "The Verb 'gefallen' + Dative", "Verbs with Dative",
          "etwas gefällt jemandem (Dativ) = something appeals to / is liked by someone",
          "'gefallen' inverts the subject-object relationship compared to English 'like'. The item being liked is the grammatical subject in nominative; the person who likes it is in the dative.",
          [{"de": "Die neue Wohnung gefällt mir sehr gut.", "en": "I like the new apartment very much (literally: The apartment pleases me)."},
           {"de": "Gefallen dir diese Schuhe?", "en": "Do you like these shoes?"}],
          ["Subject = the liked object (Singular: gefällt, Plural: gefallen)", "Person liking = Dative (mir, dir, ihm, ihr, uns, euch, ihnen)", "Never say: 'Ich gefalle das Buch'!"],
          ["gefallen", "Dative Verbs"])

    add_t(9, "The Verb 'gehören' + Dative (Ownership)", "Verbs with Dative",
          "etwas gehört jemandem (Dativ) = something belongs to someone",
          "'gehören' expresses ownership and strictly requires a dative object.",
          [{"de": "Dieses rote Fahrrad gehört meinem Bruder.", "en": "This red bicycle belongs to my brother."},
           {"de": "Wem gehört dieser Regenschirm an der Garderobe?", "en": "Whom does this umbrella on the coat rack belong to?"}],
          ["Answers question: Wem gehört das? (Whose is this?)", "gehören + Dativ", "gehören zu + Dativ = to be part of a category"],
          ["gehören", "Dative Verbs", "Ownership"])

    add_t(10, "The Verb 'schmecken' + Dative", "Verbs with Dative",
          "etwas schmeckt jemandem (Dativ) = food/drink tastes good to someone",
          "To say food tastes good to someone, the dish is the nominative subject, and the eater is in the dative case.",
          [{"de": "Das Essen im italienischen Restaurant schmeckt uns ausgezeichnet.", "en": "The food in the Italian restaurant tastes excellent to us."},
           {"de": "Schmeckt dir die Suppe nicht?", "en": "Does the soup not taste good to you?"}],
          ["Es schmeckt mir (It tastes good to me)", "Negation: Es schmeckt mir nicht", "Plural: Die Äpfel schmecken mir"],
          ["schmecken", "Dative Verbs"])

    add_t(11, "The Verb 'passen' + Dative (Fit & Schedule)", "Verbs with Dative",
          "etwas passt jemandem (Dativ) = fits someone (clothing size or calendar time)",
          "'passen' expresses that clothing fits the body or that an appointment fits someone's schedule.",
          [{"de": "Die blaue Hose passt mir leider nicht, sie ist zu eng.", "en": "The blue pants unfortunately do not fit me; they are too tight."},
           {"de": "Passt Ihnen der Termin am Donnerstag um zehn Uhr?", "en": "Does the appointment on Thursday at ten o'clock suit you?"}],
          ["Clothing size: Die Jacke passt mir gut", "Appointments: Passt es dir morgen? (Does tomorrow work for you?)", "Dative person: mir, dir, Ihnen"],
          ["passen", "Dative Verbs"])

    add_t(12, "The Verb 'stehen' + Dative (Style & Appearance)", "Verbs with Dative",
          "etwas steht jemandem (Dativ) = clothing/hair looks good on someone",
          "While 'passen' denotes physical fit or scheduling, 'stehen' with the dative denotes aesthetic appearance or style.",
          [{"de": "Dieses grüne Kleid steht dir wirklich hervorragend.", "en": "This green dress really suits you outstandingly."},
           {"de": "Die neue Brille steht ihr sehr gut.", "en": "The new glasses look very good on her."}],
          ["Style / Looks: Das Kleid steht dir (It suits your style)", "Size / Fit: Das Kleid passt dir (It fits your size)", "Requires Dative pronoun"],
          ["stehen", "Dative Verbs"])

    add_t(13, "The Expression 'Wie geht es dir / Ihnen?'", "The Dative Case",
          "Wie geht es + Dativ? (Es geht mir gut / schlecht)",
          "Asking 'How are you?' in German is an impersonal construction: 'How goes it to you?'. The person asked is always in the dative case.",
          [{"de": "Hallo Julia, wie geht es dir heute?", "en": "Hello Julia, how are you today? (informal)"},
           {"de": "Danke, es geht mir sehr gut, und Ihnen?", "en": "Thank you, I am doing very well, and you? (formal)"}],
          ["Never say 'Ich bin gut' (means: I am morally virtuous or good at something)", "Always: 'Es geht mir gut / wunderbar / so lala'", "Informal: Wie geht's? (short for Wie geht es dir?)"],
          ["Greetings", "Dative Idioms"])

    add_t(14, "Verbs 'gratulieren' and 'wünschen' with Dative", "Verbs with Dative",
          "jemandem (Dativ) zu etwas gratulieren | jemandem (Dativ) etwas (Akk) wünschen",
          "Congratulating someone requires the dative case for the recipient of the wishes, paired with the preposition 'zu' + Dativ for the occasion.",
          [{"de": "Wir gratulieren dir herzlich zum Geburtstag!", "en": "We congratulate you warmly on your birthday!"},
           {"de": "Ich wünsche Ihnen einen angenehmen Feierabend.", "en": "I wish you a pleasant evening after work."}],
          ["gratulieren + Dativ + zu + Dativ", "wünschen + Dativ (person) + Akkusativ (thing)", "zum Geburtstag, zur Hochzeit"],
          ["gratulieren", "wünschen", "Dative Verbs"])

    add_t(15, "Verbs 'antworten' and 'zuhören' + Dative", "Verbs with Dative",
          "jemandem (Dativ) antworten | jemandem (Dativ) zuhören",
          "Unlike English where you 'answer someone' or 'listen to someone' directly, German treats the person as an indirect dative object.",
          [{"de": "Der Student antwortet dem Professor auf seine Frage.", "en": "The student answers the professor to his question."},
           {"de": "Bitte hör mir genau zu, wenn ich spreche!", "en": "Please listen to me carefully when I speak!"}],
          ["antworten takes Dativ for the person: Antworte mir!", "auf + Akkusativ for the question/email: auf die Mail antworten", "zuhören is separable and takes Dative"],
          ["antworten", "zuhören", "Dative Verbs"])

    # Build the full 105 A2 topics programmatically
    a2_catalog = [
        # (16-25) Two-Way Prepositions (Wechselpräpositionen)
        (16, "Two-Way Prepositions: The Fundamental Concept (Wo vs Wohin)", "Two-Way Prepositions",
         "an, auf, hinter, in, neben, über, unter, vor, zwischen",
         "Nine prepositions in German can govern EITHER the dative or the accusative case depending on meaning: Dative for static location (Wo? / Location), Accusative for directional movement (Wohin? / Destination).",
         [{"de": "Das Buch liegt auf dem Tisch (Wo? -> Dativ).", "en": "The book is lying on the table (Location -> Dative)."},
          {"de": "Ich lege das Buch auf den Tisch (Wohin? -> Akkusativ).", "en": "I put the book onto the table (Direction -> Accusative)."}],
         ["Wo? (Static position) -> Dativ", "Wohin? (Change of location) -> Akkusativ", "Applies to 9 prepositions only: an, auf, hinter, in, neben, über, unter, vor, zwischen"], ["Wechselpräpositionen", "Cases"]),

        (17, "Two-Way Preposition: 'in' (Location vs Direction)", "Two-Way Prepositions",
         "Wo? in + Dativ (im / in der) | Wohin? in + Akkusativ (ins / in den / in die)",
         "'in' signifies inside a 3D boundary. Static presence inside takes Dative; movement entering inside takes Accusative.",
         [{"de": "Wir sind im (in dem) Supermarkt (Wo?).", "en": "We are in the supermarket."},
          {"de": "Wir gehen jetzt in den Supermarkt (Wohin?).", "en": "We are going into the supermarket now."}],
         ["in + dem = im", "in + das = ins", "in die Schweiz (Wohin? -> Akk) vs in der Schweiz (Wo? -> Dat)"], ["in", "Wechselpräpositionen"]),

        (18, "Two-Way Preposition: 'auf' (On top of horizontal surface)", "Two-Way Prepositions",
         "Wo? auf + Dativ | Wohin? auf + Akkusativ (aufs = auf das)",
         "'auf' denotes contact on top of a horizontal surface (tables, floors, balconies, squares).",
         [{"de": "Die Tasse steht auf dem Tisch (Wo? -> Dativ).", "en": "The cup is standing on the table."},
          {"de": "Ich stelle die Tasse auf den Tisch (Wohin? -> Akkusativ).", "en": "I place the cup onto the table."}],
         ["auf + das = aufs", "Horizontal surfaces: auf dem Boden, auf der Straße", "Public squares & institutions: auf dem Marktplatz, auf die Post"], ["auf", "Wechselpräpositionen"]),

        (19, "Two-Way Preposition: 'an' (At, On vertical surface / water boundary)", "Two-Way Prepositions",
         "Wo? an + Dativ (am = an dem) | Wohin? an + Akkusativ (ans = an das)",
         "'an' describes physical contact with vertical surfaces (walls, doors) or proximity to bodies of water (beaches, lakes, borders).",
         [{"de": "Das Bild hängt an der Wand (Wo? -> Dativ).", "en": "The picture hangs on the wall."},
          {"de": "Er hängt das Bild an die Wand (Wohin? -> Akkusativ).", "en": "He hangs the picture onto the wall."}],
         ["an + dem = am (am Meer, am See, am Bahnhof)", "an + das = ans (ans Meer fahren)", "Vertical surfaces: an der Wand"], ["an", "Wechselpräpositionen"]),

        (20, "Two-Way Preposition: 'neben' (Next to, beside)", "Two-Way Prepositions",
         "Wo? neben + Dativ | Wohin? neben + Akkusativ",
         "'neben' indicates side-by-side positioning without direct vertical attachment.",
         [{"de": "Die Apotheke liegt neben dem Kino.", "en": "The pharmacy is situated next to the cinema."},
          {"de": "Er setzt sich neben seinen Freund.", "en": "He sits down next to his friend."}],
         ["next to: neben dem Schreibtisch (Dat)", "moving next to: neben den Schreibtisch (Akk)", "Always applies the Wo/Wohin test"], ["neben", "Wechselpräpositionen"]),

        (21, "Two-Way Preposition: 'unter' (Under, beneath, among)", "Two-Way Prepositions",
         "Wo? unter + Dativ (unterm = unter dem) | Wohin? unter + Akkusativ (unters = unter das)",
         "'unter' signifies location beneath an object or being surrounded by a group.",
         [{"de": "Die Katze schläft unter dem Sofa (Wo?).", "en": "The cat is sleeping under the sofa."},
          {"de": "Der Hund läuft unter den Tisch (Wohin?).", "en": "The dog runs under the table."}],
         ["unter dem Tisch (Dat)", "unter den Tisch (Akk)", "Can mean 'among': unter den Studenten"], ["unter", "Wechselpräpositionen"]),

        (22, "Two-Way Preposition: 'über' (Above, over, across)", "Two-Way Prepositions",
         "Wo? über + Dativ (überm = über dem) | Wohin? über + Akkusativ (übers = über das)",
         "'über' indicates higher elevation without physical contact, or movement across an obstacle.",
         [{"de": "Die Lampe hängt über dem Esstisch.", "en": "The lamp hangs above the dining table."},
          {"de": "Wir fahren über die neue Brücke in die Stadt.", "en": "We are driving across the new bridge into the city."}],
         ["No contact above: über dem Bett", "Crossing a barrier/street: über die Straße gehen", "Contact on top = auf, hovering above = über"], ["über", "Wechselpräpositionen"]),

        (23, "Two-Way Preposition: 'vor' (In front of / Before)", "Two-Way Prepositions",
         "Spatial Wo? vor + Dativ | Spatial Wohin? vor + Akkusativ | Temporal vor + Dativ",
         "'vor' denotes spatial position in front of something, or temporal precedence ('ago' / 'before').",
         [{"de": "Das Auto parkt vor dem Haus (Wo?).", "en": "The car is parked in front of the house."},
          {"de": "Er fährt das Auto vor die Garage (Wohin?).", "en": "He drives the car in front of the garage."}],
         ["Spatial: vor dem Eingang (Dat) vs vor den Eingang (Akk)", "Temporal 'vor' ALWAYS takes Dativ: vor zwei Wochen (two weeks ago)", "Temporal 'vor' answers 'Wann?'"], ["vor", "Wechselpräpositionen"]),

        (24, "Two-Way Preposition: 'hinter' (Behind)", "Two-Way Prepositions",
         "Wo? hinter + Dativ (hinterm = hinter dem) | Wohin? hinter + Akkusativ (hinters = hinter das)",
         "'hinter' denotes the rear side of an object or building.",
         [{"de": "Der Garten liegt hinter dem Haus.", "en": "The garden lies behind the house."},
          {"de": "Die Kinder rennen hinter den Zaun.", "en": "The children run behind the fence."}],
         ["hinter dem Haus (Dat)", "hinter das Haus (Akk)", "hinterm / hinters contractions in colloquial speech"], ["hinter", "Wechselpräpositionen"]),

        (25, "Two-Way Preposition: 'zwischen' (Between)", "Two-Way Prepositions",
         "Wo? zwischen + Dativ (Plural / 2 Datives) | Wohin? zwischen + Akkusativ",
         "'zwischen' indicates a position or movement between two or more reference points.",
         [{"de": "Der Stuhl steht zwischen dem Tisch und dem Regal.", "en": "The chair stands between the table and the shelf."},
          {"de": "Er stellt den Stuhl zwischen die beiden Schränke.", "en": "He places the chair between both wardrobes."}],
         ["Between two items in Dative: zwischen dem X und dem Y", "Between plural items: zwischen den Bäumen", "Directional: zwischen die Stühle stellen"], ["zwischen", "Wechselpräpositionen"]),

        # (26-32) Positional Verbs
        (26, "Positional Verb Pair: 'stellen' vs 'stehen'", "Positional Verbs",
         "stellen (action, Wohin? + Akk) | stehen (state, Wo? + Dat)",
         "'stellen' is a regular, transitive verb meaning to place upright (active movement). 'stehen' is an irregular, intransitive verb describing standing upright (static state).",
         [{"de": "Ich stelle die Vase auf den Tisch (Wohin? -> Akk).", "en": "I place the vase onto the table."},
          {"de": "Die Vase steht auf dem Tisch (Wo? -> Dat).", "en": "The vase is standing on the table."}],
         ["stellen: stellte, hat gestellt (regular, takes Akkusativ)", "stehen: stand, hat gestanden (irregular, takes Dativ)", "Always vertical upright orientation"], ["stellen", "stehen", "Verbs"]),

        (27, "Positional Verb Pair: 'legen' vs 'liegen'", "Positional Verbs",
         "legen (action, Wohin? + Akk) | liegen (state, Wo? + Dat)",
         "'legen' means to lay something flat down (active). 'liegen' means to lie flat horizontally (static state).",
         [{"de": "Er legt das Buch auf das Sofa.", "en": "He lays the book onto the sofa."},
          {"de": "Das Buch liegt auf dem Sofa.", "en": "The book is lying on the sofa."}],
         ["legen: legte, hat gelegt (regular + Akk)", "liegen: lag, hat gelegen (irregular + Dat)", "Always horizontal flat orientation"], ["legen", "liegen", "Verbs"]),

        (28, "Positional Verb Pair: 'setzen' vs 'sitzen'", "Positional Verbs",
         "sich setzen (action, Wohin? + Akk) | sitzen (state, Wo? + Dat)",
         "'sich setzen' means to sit down (active movement). 'sitzen' means to be seated (static posture).",
         [{"de": "Ich setze mich auf den bequemen Sessel.", "en": "I sit down on the comfortable armchair."},
          {"de": "Ich sitze auf dem bequemen Sessel.", "en": "I am sitting on the comfortable armchair."}],
         ["sich setzen: setzte sich, hat sich gesetzt (+ Akk)", "sitzen: saß, hat gesessen (+ Dat)", "Watch out: 'setzen' is almost always reflexive when seating oneself"], ["setzen", "sitzen", "Verbs"]),

        (29, "Positional Verb Pair: 'hängen' (Transitive vs Intransitive)", "Positional Verbs",
         "hängen (action, weak: hängte, gehängt + Akk) | hängen (state, strong: hing, gehangen + Dat)",
         "German uses the same infinitive 'hängen' for both placing a picture on the wall (active/weak verb) and hanging there (state/strong verb).",
         [{"de": "Wir hängen das Gemälde an die Wand.", "en": "We hang the painting onto the wall."},
          {"de": "Das Gemälde hängt an der Wand.", "en": "The painting is hanging on the wall."}],
         ["Active: hängte / hat gehängt + Akkusativ", "Static state: hing / hat gehangen + Dativ", "Check whether someone is moving the object or if it is already there"], ["hängen", "Verbs"]),

        (30, "Positional Verb Pair: 'stecken' (To insert vs to stick inside)", "Positional Verbs",
         "stecken (action, Wohin? + Akk) | stecken (state, Wo? + Dat)",
         "'stecken' means to insert or plug something inside a container or socket (active) or to be stuck inside (state).",
         [{"de": "Er steckt den Schlüssel in das Schloss.", "en": "He sticks the key into the lock."},
          {"de": "Der Schlüssel steckt im Schloss.", "en": "The key is in the lock."}],
         ["steckte / hat gesteckt + Akkusativ", "steckte / hat gesteckt + Dativ", "Very common with USB drives, keys, pockets: in die Tasche stecken"], ["stecken", "Verbs"]),

        (31, "The Passive-like Meaning of Positional Verbs", "Positional Verbs",
         "Instead of 'is located', German uses stehen, liegen, sitzen, hängen",
         "German rarely uses generic 'is located' (befindet sich) for everyday objects. Instead, speakers choose the exact posture verb (stehen for vertical, liegen for flat).",
         [{"de": "Die Flasche steht im Kühlschrank (not 'ist')", "en": "The bottle is in the fridge."},
          {"de": "Der Teppich liegt im Wohnzimmer (not 'ist')", "en": "The carpet is in the living room."}],
         ["Bottles, cups, buildings 'stehen'", "Paper, rugs, towns 'liegen'", "Clothes in closets 'hängen' or 'liegen'"], ["Positional Verbs", "Idiomatic"]),

        (32, "Summary Matrix of German Positional Verbs", "Positional Verbs",
         "Action (Wohin? + Akk, Regular) vs State (Wo? + Dat, Irregular)",
         "A consolidated mental model for mastering positional verb pairs in German.",
         [{"de": "Wohin legst du das Smartphone? - Es liegt schon auf dem Schreibtisch.", "en": "Where are you putting the smartphone? - It is already lying on the desk."}],
         ["stellen -> stehen", "legen -> liegen", "setzen -> sitzen", "hängen -> hängen"], ["Review", "Positional Verbs"]),

        # (33-42) Pure Dative Prepositions
        (33, "Pure Dative Prepositions: The Core Rule", "Prepositions",
         "aus, bei, mit, nach, seit, von, zu, gegenüber -> ALWAYS DATIV",
         "Unlike two-way prepositions, these eight prepositions exclusively govern the dative case, regardless of movement or stillness.",
         [{"de": "Ich fahre mit dem Zug zur Arbeit.", "en": "I travel by train to work."}],
         ["Never use accusative with these prepositions", "Mnemonic: 'Aus bei mit nach seit von zu - immer mit dem Dativ du!'", "Fixed case assignment"], ["Dative Prepositions", "Rule"]),

        (34, "Dative Preposition: 'aus' (From inside, made of, origin)", "Prepositions",
         "aus + Dativ",
         "'aus' expresses spatial exit from an enclosed area, country of origin, or material composition.",
         [{"de": "Er kommt aus dem Büro und geht nach Hause.", "en": "He comes out of the office and goes home."},
          {"de": "Der Tisch ist aus massivem Holz gebaut.", "en": "The table is built from solid wood."}],
         ["Movement out of an interior: aus dem Haus", "Country of origin: aus Deutschland", "Material: aus Gold, aus Glas"], ["aus", "Prepositions"]),

        (35, "Dative Preposition: 'bei' (At the place of, working at, during)", "Prepositions",
         "bei + Dativ | Contraction: beim (bei dem)",
         "'bei' describes staying at someone's home, working for an employer, or concurrent circumstances.",
         [{"de": "Heute Abend übernachte ich bei einem Freund.", "en": "Tonight I am sleeping over at a friend's place."},
          {"de": "Mein Bruder arbeitet bei einem großen Softwareunternehmen.", "en": "My brother works at a large software enterprise."}],
         ["Living/staying with a person: bei den Eltern", "Company: bei Siemens, bei BMW", "Weather: bei Regen (in the rain)"], ["bei", "Prepositions"]),

        (36, "Dative Preposition: 'mit' (With, by means of transport)", "Prepositions",
         "mit + Dativ",
         "'mit' expresses accompaniment or means of transportation and instruments.",
         [{"de": "Wir fahren am Wochenende mit der Bahn nach Hamburg.", "en": "We are traveling by train to Hamburg on the weekend."},
          {"de": "Er schneidet das Brot mit einem scharfen Messer.", "en": "He cuts the bread with a sharp knife."}],
         ["Transportation: mit dem Bus, mit dem Auto, mit dem Fahrrad", "Accompaniment: mit meiner Familie", "Always dative"], ["mit", "Prepositions"]),

        (37, "Dative Preposition: 'nach' (To cities/countries, after, past)", "Prepositions",
         "nach + Dativ | Spatial: to country/city without article | Temporal: after",
         "'nach' indicates travel destinations (for cities and article-less countries) and temporal succession ('after').",
         [{"de": "Nach der Vorlesung gehen die Studenten in die Mensa.", "en": "After the lecture, the students go to the cafeteria."},
          {"de": "Nächsten Monat fliegen wir nach Spanien.", "en": "Next month we are flying to Spain."}],
         ["Destination: nach Berlin, nach Deutschland (no article countries)", "Direction: nach links, nach rechts, nach Hause", "Temporal: nach dem Essen, nach der Arbeit"], ["nach", "Prepositions"]),

        (38, "Dative Preposition: 'seit' (Since, for an ongoing duration)", "Prepositions",
         "seit + Dativ | Paired with PRESENT TENSE in German",
         "'seit' expresses an event that began in the past and continues into the present. Unlike English which requires present perfect ('have lived'), German uses the simple present tense with 'seit'.",
         [{"de": "Ich lerne seit sechs Monaten intensiv Deutsch.", "en": "I have been learning German intensively for six months."},
          {"de": "Er wohnt seit einem Jahr in dieser schönen Wohnung.", "en": "He has been living in this beautiful apartment for a year."}],
         ["Use Präsens: 'Ich wohne seit...' (NOT 'Ich habe gewohnt seit')", "Always Dative: seit einem Monat, seit einer Woche", "Action is still ongoing right now"], ["seit", "Prepositions", "Tenses"]),

        (39, "Dative Preposition: 'von' (From, of, by)", "Prepositions",
         "von + Dativ | Contraction: vom (von dem)",
         "'von' indicates a starting point, ownership/relationship (replacing genitive), or the author of a work.",
         [{"de": "Ich habe einen Brief von meiner Vermieterin bekommen.", "en": "I received a letter from my landlady."},
          {"de": "Das ist das Auto vom (von dem) Chef.", "en": "That is the boss's car."}],
         ["Starting point: von Berlin nach München", "Colloquial possession: das Fahrrad von meinem Bruder", "Contraction: vom Bahnhof"], ["von", "Prepositions"]),

        (40, "Dative Preposition: 'zu' (To people, businesses, buildings)", "Prepositions",
         "zu + Dativ | Contraction: zum (zu dem), zur (zu der)",
         "'zu' denotes movement toward a person, named store, or specific building destination.",
         [{"de": "Morgen gehe ich zum (zu dem) Zahnarzt.", "en": "Tomorrow I am going to the dentist."},
          {"de": "Wie komme ich am besten zur (zu der) Bibliothek?", "en": "How do I best get to the library?"}],
         ["People: zum Arzt, zu meinen Großeltern", "Stores/Brands: zu Aldi, zu Ikea", "Idiom: zu Hause (at home) vs nach Hause (going home)"], ["zu", "Prepositions"]),

        (41, "Dative Preposition: 'gegenüber' (Opposite, across from)", "Prepositions",
         "gegenüber + Dativ | Can appear before OR after the noun / pronoun",
         "'gegenüber' indicates spatial position directly across or facing something. When used with personal pronouns, it frequently follows the pronoun.",
         [{"de": "Das Café liegt direkt gegenüber dem Bahnhof.", "en": "The café is situated directly opposite the train station."},
          {"de": "Er saß mir gegenüber am Tisch.", "en": "He sat opposite me at the table."}],
         ["gegenüber dem Park / dem Park gegenüber", "With pronouns, postposition is common: mir gegenüber", "Always dative"], ["gegenüber", "Prepositions"]),

        (42, "Idiom: 'zu Hause' (at home) vs 'nach Hause' (going home)", "Prepositions",
         "zu Hause = static location (Dativ state) | nach Hause = directional movement",
         "A frequent beginner trap: 'zu Hause' means you are already there, while 'nach Hause' means you are heading in that direction.",
         [{"de": "Am Sonntag bleibe ich den ganzen Tag gemütlich zu Hause.", "en": "On Sunday I stay comfortably at home all day."},
          {"de": "Nach dem Feierabend fahre ich direkt nach Hause.", "en": "After work, I drive straight home."}],
         ["Ich bin zu Hause (Wo? -> static)", "Ich gehe nach Hause (Wohin? -> movement)", "Do not say: 'Ich gehe zu Hause'!"], ["zu Hause", "nach Hause", "Idioms"])
    ]

    for item in a2_catalog:
        add_t(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])

    # Continue generating A2 topics up to 105:
    # 43-60: Perfekt Tense
    # 61-70: Präteritum
    # 71-75: Futur I
    # 76-88: Adjektivdeklination & Comparison
    # 89-98: Nebensätze
    # 99-105: Reflexive Verben & Pronoun Order
    remaining_a2 = [
        (43, "The Perfekt Tense: Conversational Past Concept", "Perfekt Tense",
         "Auxiliary (haben/sein in Pos 2) + Partizip II at the very end of the clause",
         "In spoken and informal written German, the Perfekt is the primary past tense. It corresponds to both simple past ('I did') and present perfect ('I have done') in English.",
         [{"de": "Ich habe gestern Abend einen Film geschaut.", "en": "I watched / have watched a movie yesterday evening."},
          {"de": "Wir sind am Wochenende nach Leipzig gefahren.", "en": "We drove to Leipzig on the weekend."}],
         ["Dominant past tense in spoken German", "Satzklammer: Auxiliary verb in Pos 2, Partizip II at end", "Two auxiliaries: haben (most verbs) or sein (motion/change)"], ["Perfekt", "Past Tense"]),

        (44, "Auxiliary Verb Selection: 'haben' vs 'sein'", "Perfekt Tense",
         "sein: Verbs of movement (A to B), change of condition, and sein/bleiben/werden | haben: All transitive and stative verbs",
         "Choosing the correct auxiliary is essential. 'sein' is reserved for intransitive verbs indicating movement from one place to another (gehen, fahren, fliegen), a change of state (aufwachen, sterben), plus sein, bleiben, and werden.",
         [{"de": "Er ist gestern um 22 Uhr eingeschlafen (change of state -> sein).", "en": "He fell asleep yesterday at 10 PM."},
          {"de": "Er hat acht Stunden geschlafen (state without change -> haben).", "en": "He slept for eight hours."}],
         ["Movement A -> B: gehen, laufen, reisen, fliegen, schwimmen take 'sein'", "Change of state: aufstehen, wachsen, sterben take 'sein'", "Transitive verbs with accusative object ALWAYS take 'haben'"], ["Perfekt", "haben vs sein"]),

        (45, "The Exceptional Verbs taking 'sein': sein, bleiben, werden", "Perfekt Tense",
         "sein (ist gewesen), bleiben (ist geblieben), werden (ist geworden)",
         "Even though 'bleiben' (to stay) denotes zero movement, it takes 'sein' in the Perfekt. 'sein' and 'werden' also strictly take 'sein'.",
         [{"de": "Ich bin am Wochenende zu Hause geblieben.", "en": "I stayed at home on the weekend."},
          {"de": "Mein Freund ist ein erfolgreicher Unternehmer geworden.", "en": "My friend has become a successful entrepreneur."}],
         ["bleiben -> ist geblieben", "sein -> ist gewesen", "werden -> ist geworden"], ["Perfekt", "sein"]),

        (46, "Regular Past Participles (Partizip II): ge- + stem + -t", "Perfekt Tense",
         "ge- + verb stem + -t (z.B. machen -> gemacht, hören -> gehört)",
         "Weak (regular) verbs form their past participle by prefixing 'ge-' and suffixing '-t' to the infinitive stem.",
         [{"de": "Hast du deine Hausaufgaben schon gemacht?", "en": "Have you already done your homework?"},
          {"de": "Wir haben leckere Kekse gebacken.", "en": "We baked delicious cookies."}],
         ["lernen -> gelernt", "kaufen -> gekauft", "spielen -> gespielt"], ["Perfekt", "Partizip II", "Regular Verbs"]),

        (47, "Participle II with Stems ending in -d or -t: ge- + stem + -et", "Perfekt Tense",
         "Insert -e- for pronunciation: arbeiten -> gearbeitet, warten -> gewartet",
         "When a regular verb stem ends in -d, -t, or complex consonants, an extra 'e' is added before '-t' for vocal ease.",
         [{"de": "Er hat gestern zehn Stunden im Büro gearbeitet.", "en": "He worked for ten hours in the office yesterday."}],
         ["arbeiten -> gearbeitet", "warten -> gewartet", "antworten -> geantwortet"], ["Perfekt", "Stem Changes"]),

        (48, "Verbs ending in '-ieren': NO ge- in Participle II", "Perfekt Tense",
         "Infinitive in -ieren -> stem + -t (NO ge-!)",
         "Verbs of foreign origin ending in '-ieren' do not take the 'ge-' prefix in their past participle. They simply add '-t' to the stem.",
         [{"de": "Sie hat Wirtschaft an der Universität studiert.", "en": "She studied economics at the university."},
          {"de": "Ich habe die Datei auf meinem Computer reserviert.", "en": "I reserved the file on my computer."}],
         ["studieren -> studiert (never 'gestudiert')", "fotografieren -> fotografiert", "reparieren -> repariert"], ["Perfekt", "-ieren Verbs"]),

        (49, "Separable Verbs in Perfekt: Prefix + ge- + stem + -t/-en", "Perfekt Tense",
         "The 'ge-' is inserted BETWEEN the prefix and the verb stem: auf-ge-räumt, ein-ge-kauft",
         "In separable verbs, the past participle prefix 'ge-' is sandwiched directly between the separable prefix and the verbal base.",
         [{"de": "Ich habe gestern die ganze Wohnung aufgeräumt.", "en": "I tidied up the entire apartment yesterday."},
          {"de": "Wir haben viele frische Lebensmittel eingekauft.", "en": "We bought lots of fresh groceries."}],
         ["einkaufen -> eingekauft", "aufstehen -> aufgestanden", "abfahren -> abgefahren"], ["Perfekt", "Separable Verbs"]),

        (50, "Inseparable Verbs in Perfekt: NO ge- Prefix!", "Perfekt Tense",
         "Prefix (be-, ver-, etc.) + stem + -t / -en (NO ge-!)",
         "Verbs with inseparable prefixes (be-, emp-, ent-, er-, ge-, miss-, ver-, zer-) NEVER add 'ge-' in their past participle.",
         [{"de": "Ich habe die Erklärung des Lehrers sofort verstanden.", "en": "I understood the teacher's explanation immediately."},
          {"de": "Er hat die Hotelrechnung gestern bezahlt.", "en": "He paid the hotel bill yesterday."}],
         ["verstehen -> verstanden (not 'geverstanden')", "bezahlen -> bezahlt", "erzählen -> erzählt"], ["Perfekt", "Inseparable Verbs"]),

        (51, "Strong Verbs in Perfekt: ge- + (Vowel Shift) + -en", "Perfekt Tense",
         "Strong verbs end in '-en' and frequently change their root vowel",
         "Irregular (strong) verbs retain the infinitive '-en' ending in Partizip II and often change their root vowel (Ablaut).",
         [{"de": "Er hat gestern Abend einen langen Brief geschrieben (schreiben -> ie -> i).", "en": "He wrote a long letter yesterday evening."},
          {"de": "Sie haben frischen Orangensaft getrunken (trinken -> i -> u).", "en": "They drank fresh orange juice."}],
         ["schreiben -> geschrieben", "trinken -> getrunken", "helfen -> geholfen"], ["Perfekt", "Strong Verbs"]),

        (52, "Strong Verbs with Identical Infinitive and Participle Vowels", "Perfekt Tense",
         "lesen -> gelesen, sehen -> gesehen, schlafen -> geschlafen, fahren -> gefahren",
         "Some strong verbs do not alter their stem vowel in the participle; they simply add 'ge-' and end in '-en'.",
         [{"de": "Ich habe den spannenden Kriminalroman an einem Tag gelesen.", "en": "I read the exciting crime novel in one day."}],
         ["fahren -> gefahren", "sehen -> gesehen", "essen -> gegessen (adds double s)"], ["Perfekt", "Strong Verbs"]),

        (53, "The Common Strong Participles of Motion", "Perfekt Tense",
         "gehen -> ist gegangen | kommen -> ist gekommen | fahren -> ist gefahren | fliegen -> ist geflogen",
         "Movement verbs form the core of daily communication and all take 'sein' as their auxiliary in Perfekt.",
         [{"de": "Mein Kollege ist pünktlich zur Konferenz gekommen.", "en": "My colleague came punctually to the conference."}],
         ["gehen -> ist gegangen", "laufen -> ist gelaufen", "schwimmen -> ist geschwommen"], ["Perfekt", "Motion Verbs"]),

        (54, "Präteritum of 'sein' (The Written & Spoken Past of to be)", "Präteritum Tense",
         "ich war, du warst, er/sie/es war, wir waren, ihr wart, sie/Sie waren",
         "Even in spoken German, the verb 'sein' is almost universally preferred in the simple past (Präteritum) over the clunky Perfekt 'ich bin gewesen'.",
         [{"de": "Letzte Woche war ich beruflich in Frankfurt.", "en": "Last week I was in Frankfurt on business."},
          {"de": "Wo warst du gestern Nachmittag um vier Uhr?", "en": "Where were you yesterday afternoon at four o'clock?"}],
         ["Use 'war' in conversation instead of 'bin gewesen'", "1st and 3rd person singular are identical: ich war, er war", "No personal ending on 1st/3rd person singular"], ["Präteritum", "sein"]),

        (55, "Präteritum of 'haben' (The Past of to have)", "Präteritum Tense",
         "ich hatte, du hattest, er/sie/es hatte, wir hatten, ihr hattet, sie/Sie hatten",
         "Just like 'sein', speakers consistently use the simple past 'hatte' in conversation rather than 'ich habe gehabt'.",
         [{"de": "Ich hatte gestern leider keine Zeit für Sport.", "en": "Unfortunately, I had no time for sports yesterday."},
          {"de": "Wir hatten ein sehr produktives Gespräch.", "en": "We had a very productive conversation."}],
         ["Prefer 'hatte' over 'habe gehabt' in everyday speech", "ich hatte, er hatte (no -t ending on 3rd person)", "wir hatten, sie hatten"], ["Präteritum", "haben"]),

        (56, "Präteritum of Modal Verbs (können, müssen, wollen, dürfen)", "Präteritum Tense",
         "Drop umlaut + insert -te: konnte, musste, wollte, durfte, sollte",
         "Modal verbs are almost exclusively expressed in the Präteritum rather than the Perfekt in both spoken and written German.",
         [{"de": "Ich konnte gestern nicht kommen, weil ich krank war.", "en": "I could not come yesterday because I was sick."},
          {"de": "Er musste am Wochenende viele E-Mails beantworten.", "en": "He had to answer many emails on the weekend."}],
         ["Drop umlaut in Präteritum: können -> konnte, müssen -> musste, dürfen -> durfte", "1st and 3rd person singular match: ich konnte, er konnte", "Much simpler than double-infinitive Perfekt"], ["Präteritum", "Modal Verbs"]),

        (57, "Futur I: werden + Infinitiv", "Future Tense",
         "Conjugated 'werden' in Pos 2 + bare Infinitive at the sentence end",
         "Futur I expresses future intentions, predictions, or promises. The conjugated form of 'werden' sits in Position 2, while the infinitive closes the clause.",
         [{"de": "Wir werden nächstes Jahr eine neue Sprache lernen.", "en": "We will learn a new language next year."},
          {"de": "Morgen wird es den ganzen Tag sonnig sein.", "en": "Tomorrow it will be sunny all day."}],
         ["ich werde, du wirst, er wird, wir werden, ihr werdet, sie werden", "Infinitive sits at the absolute end of the clause", "Alternative: Präsens + time word (Morgen fliege ich nach Rom)"], ["Futur I", "Future"]),

        (58, "Adjective Declension Concept: Three Inflection Types", "Adjectives",
         "Type 1: Weak (after der/die/das) | Type 2: Mixed (after ein/kein/mein) | Type 3: Strong (without article)",
         "In German, an adjective standing before a noun must decline to signal case, gender, and number. The ending depends on what type of article precedes it.",
         [{"de": "Der gute Mann (Weak), ein guter Mann (Mixed), guter Wein (Strong).", "en": "The good man, a good man, good wine."}],
         ["Predicative adjectives do NOT decline: 'Der Mann ist gut'", "Attributive adjectives BEFORE nouns MUST decline", "The endings convey case, gender, and plurality"], ["Adjektivdeklination", "Adjectives"]),

        (59, "Adjective Declension Type 1: Weak (after Definite Articles der/die/das)", "Adjectives",
         "Nominative singular: -e | Accusative fem/neut: -e, masc: -en | All Dative, Genitive, Plurals: -en",
         "When a definite article already clearly signals gender and case, adjectives take the simple weak endings: only '-e' or '-en'.",
         [{"de": "Der junge Ingenieur arbeitet an einer Innovation.", "en": "The young engineer works on an innovation."},
          {"de": "Ich kaufe den schwarzen Rucksack.", "en": "I buy the black backpack."}],
         ["Nominative: der alte Mann, die junge Frau, das kleine Kind", "Accusative masculine changes to -en: den alten Mann", "All Dative and Plurals take -en: mit den neuen Freunden"], ["Adjektivdeklination", "Weak"]),

        (60, "Adjective Declension Type 2: Mixed (after Indefinite ein/kein/mein)", "Adjectives",
         "Nom: ein guter (m), eine gute (f), ein gutes (n) | Akk masc: einen guten | Dative & Plural: -en",
         "Because 'ein' in the nominative does not distinguish masculine from neuter, the adjective must carry the identifying signal (-er for masculine, -es for neuter).",
         [{"de": "Das ist ein schöner Tag für einen Ausflug.", "en": "That is a beautiful day for an excursion."},
          {"de": "Sie hat ein neues Auto gekauft.", "en": "She bought a new car."}],
         ["ein alter Mann (signals der)", "ein kleines Kind (signals das)", "eine junge Frau (signals die)"], ["Adjektivdeklination", "Mixed"]),

        (61, "Adjective Declension in the Dative: Always '-en'!", "Adjectives",
         "Any adjective after an article in the dative case ALWAYS ends in -en!",
         "The golden rule of German adjective declension: if an article precedes an adjective in the dative case (dem, der, einem, einer, meinen), the adjective ALWAYS ends in '-en'.",
         [{"de": "Ich helfe dem alten Mann beim Einsteigen.", "en": "I help the old man board."},
          {"de": "Wir wohnen in einer ruhigen Straße.", "en": "We live on a quiet street."}],
         ["No exceptions: dem guten Mann, der netten Frau, dem kleinen Kind", "Plural dative: den fleißigen Studenten", "Easiest declension rule to remember"], ["Adjektivdeklination", "Dative Rule"]),

        (62, "Comparison of Adjectives: Positiv, Komparativ, Superlativ", "Adjectives",
         "Positiv: so ... wie | Komparativ: -er als | Superlativ: am ...-sten / der ...-ste",
         "Comparing qualities uses three tiers: equality (so wie), superiority (-er als), and the highest degree (am -sten).",
         [{"de": "Mein Bruder ist so groß wie mein Vater.", "en": "My brother is as tall as my father."},
          {"de": "Ein Flugzeug ist schneller als ein Zug.", "en": "An airplane is faster than a train."},
          {"de": "Der Mount Everest ist der höchste Berg der Welt.", "en": "Mount Everest is the highest mountain in the world."}],
         ["so wie (equality - no adjective ending on base)", "Komparativ: schneller als (never 'wie' for superiority in standard German!)", "Superlativ: am schnellsten"], ["Comparative", "Superlative"]),

        (63, "Adjective Comparison with Umlaut (a->ä, o->ö, u->ü)", "Adjectives",
         "Monosyllabic adjectives add an umlaut: alt -> älter, groß -> größer, jung -> jünger",
         "Short, single-syllable German adjectives regularly add an umlaut to their root vowel in both comparative and superlative degrees.",
         [{"de": "Berlin ist älter als viele moderne Großstädte.", "en": "Berlin is older than many modern metropolises."},
          {"de": "Mein Großvater ist der älteste in unserer Familie.", "en": "My grandfather is the oldest in our family."}],
         ["alt -> älter -> am ältesten", "warm -> wärmer -> am wärmsten", "kurz -> kürzer -> am kürzesten"], ["Comparative", "Umlaut"]),

        (64, "Irregular Comparison: gut, viel, gern, teuer", "Adjectives",
         "gut/besser/am besten | viel/mehr/am meisten | gern/lieber/am liebsten | teuer/teurer",
         "These high-frequency adjectives feature irregular stems in comparative and superlative forms.",
         [{"de": "Ich trinke gerne Kaffee, aber am liebsten trinke ich Tee.", "en": "I like drinking coffee, but most of all I like drinking tea."},
          {"de": "Dieses Produkt hat eine viel bessere Qualität.", "en": "This product has a much better quality."}],
         ["gut -> besser -> am besten", "viel -> mehr -> am meisten", "gern -> lieber -> am liebsten", "teuer -> teurer (drops internal e)"], ["Irregular Comparison", "Adjectives"]),

        (65, "Subordinate Clauses (Nebensätze): The Verb-Kick Rule", "Subordinate Clauses",
         "Conjunction + Subject + ... + CONJUGATED VERB AT THE VERY END",
         "In a German subordinate clause (Nebensatz), the finite conjugated verb is pushed from Position 2 all the way to the absolute end of the clause. A comma always separates main and subordinate clauses.",
         [{"de": "Ich lerne Deutsch, weil ich in München arbeiten möchte.", "en": "I am learning German because I want to work in Munich."}],
         ["Always preceded by a comma", "Conjugated verb is the final word in the clause", "In compound tenses, auxiliary is at the very end: weil er gekommen ist"], ["Nebensätze", "Word Order", "Verb-Kick"]),

        (66, "Causal Clauses with 'weil' (because)", "Subordinate Clauses",
         "weil + conjugated verb at the end",
         "'weil' provides the reason or cause of an action and triggers subordinate verb-final word order.",
         [{"de": "Ich gehe heute früh schlafen, weil ich sehr müde bin.", "en": "I am going to sleep early today because I am very tired."}],
         ["Answers: Warum? (Why?)", "Do not confuse with 'denn' (denn keeps V2, weil kicks verb to end)", "Comma is mandatory before weil"], ["weil", "Causal", "Nebensätze"]),

        (67, "Contrast: 'weil' vs 'denn' vs 'deshalb'", "Subordinate Clauses",
         "weil (Verb at end) | denn (Pos 0, V2) | deshalb (Adverb in Pos 1, Inversion V2)",
         "Three ways to express cause and effect with three completely different word orders.",
         [{"de": "Er bleibt zu Hause, weil er krank ist.", "en": "He stays at home because he is sick (weil = verb final)."},
          {"de": "Er bleibt zu Hause, denn er ist krank.", "en": "He stays at home, for he is sick (denn = Position 0, V2)."},
          {"de": "Er ist krank, deshalb bleibt er zu Hause.", "en": "He is sick, therefore he stays at home (deshalb = Position 1, V2)."}],
         ["weil: verb at end", "denn: verb in position 2 (after subject)", "deshalb: verb in position 2 (before subject)"], ["Connectors", "Word Order"]),

        (68, "Conditional Clauses with 'wenn' (if / when)", "Subordinate Clauses",
         "wenn + conjugated verb at the end | Main clause begins with Verb if 'wenn' is first",
         "'wenn' introduces conditional conditions ('if') or recurring temporal events ('whenever'). When the 'wenn' clause comes first, the main clause begins directly with the verb.",
         [{"de": "Wenn das Wetter morgen schön ist, machen wir ein Picknick.", "en": "If the weather is nice tomorrow, we will have a picnic."}],
         ["Condition: wenn es regnet...", "If subordinate clause is first, main clause starts with verb: '...machen wir'", "'wenn' can mean 'if' or 'whenever'"], ["wenn", "Conditional", "Nebensätze"]),

        (69, "Concessive Clauses with 'obwohl' (although / even though)", "Subordinate Clauses",
         "obwohl + conjugated verb at the end",
         "'obwohl' introduces an unexpected counter-expectation or concession.",
         [{"de": "Er geht spazieren, obwohl es draußen stark regnet.", "en": "He goes for a walk even though it is raining heavily outside."}],
         ["Expresses surprise/contrast", "Verb goes to the end", "Can start the sentence: Obwohl er müde ist, lernt er weiter."], ["obwohl", "Concessive", "Nebensätze"]),

        (70, "Indirect Questions with 'ob' (whether / if)", "Subordinate Clauses",
         "ob + conjugated verb at the end (for Yes/No questions)",
         "'ob' translates to 'whether' or 'if' when reporting a yes/no question indirectly.",
         [{"de": "Ich weiß nicht, ob der Zug heute pünktlich ankommt.", "en": "I do not know whether the train arrives on time today."}],
         ["Reports Yes/No questions: Kommt er? -> Ich frage, ob er kommt.", "Never use 'wenn' for 'whether'!", "Verb at the end of the clause"], ["ob", "Indirect Questions", "Nebensätze"]),

        (71, "Complement Clauses with 'dass' (that)", "Subordinate Clauses",
         "dass + conjugated verb at the end",
         "'dass' links mental verbs (glauben, wissen, hoffen, denken, meinen) or statements of fact to their content clause.",
         [{"de": "Ich hoffe, dass du eine schöne Reise nach Wien hast.", "en": "I hope that you have a wonderful trip to Vienna."}],
         ["Spelled with double-s 'dass' (not article 'das')", "Kicks conjugated verb to the end", "Preceded by a mandatory comma"], ["dass", "Complement Clauses", "Nebensätze"]),

        (72, "Temporal Clauses: 'als' vs 'wenn' (Past Single Event vs Recurring)", "Subordinate Clauses",
         "als = single, unique completed past event | wenn = recurring event (past/present) or future",
         "A famous distinction in German: 'als' is used exclusively for a single, unique event or period in the past ('when I was a child'). 'wenn' is used for recurring events ('whenever') or present/future conditions.",
         [{"de": "Als ich ein Kind war, lebte ich auf dem Land (unique past period).", "en": "When I was a child, I lived in the countryside."},
          {"de": "Immer wenn ich nach Berlin fahre, besuche ich das Museum (recurring).", "en": "Whenever I travel to Berlin, I visit the museum."}],
         ["Single past event/time: als (Als ich 18 Jahre alt war...)", "Recurring (whenever): immer wenn...", "Present or future: wenn (Wenn ich Zeit habe...)"], ["als vs wenn", "Temporal", "Nebensätze"]),

        (73, "Temporal Clauses with 'während' (while) and 'bevor' (before)", "Subordinate Clauses",
         "während / bevor + conjugated verb at the end",
         "'während' describes two simultaneous actions occurring in parallel. 'bevor' indicates that an action precedes another in time.",
         [{"de": "Ich höre gerne Musik, während ich die Küche aufräume.", "en": "I like listening to music while I tidy up the kitchen."},
          {"de": "Bevor wir losfahren, müssen wir den Reifendruck prüfen.", "en": "Before we set off, we must check the tire pressure."}],
         ["während = simultaneous events", "bevor = prior event", "Both are subordinate conjunctions with verb at end"], ["während", "bevor", "Temporal"]),

        (74, "Temporal Conjunction 'nachdem' (after) in A2/B1", "Subordinate Clauses",
         "nachdem + conjugated verb at the end",
         "'nachdem' expresses that an action is completed before the main action begins.",
         [{"de": "Nachdem ich gefrühstückt habe, fahre ich mit der Bahn ins Büro.", "en": "After I have eaten breakfast, I travel by train to the office."}],
         ["Conjunction 'nachdem' takes a clause with verb at end", "Preposition 'nach' takes a dative noun: nach dem Frühstück", "Do not confuse conjunction and preposition!"], ["nachdem", "Temporal"]),

        (75, "Reflexive Verbs with Accusative: sich freuen, sich fühlen", "Reflexive Verbs",
         "sich + Akkusativ: mich, dich, sich, uns, euch, sich",
         "Reflexive verbs describe actions directed back toward the subject. In the accusative, 1st and 2nd persons use mich/dich/uns/euch, while 3rd person uses 'sich'.",
         [{"de": "Ich freue mich sehr auf das bevorstehende Wochenende.", "en": "I look forward very much to the upcoming weekend."},
          {"de": "Wie fühlst du dich nach dem langen Spaziergang?", "en": "How do you feel after the long walk?"}],
         ["sich freuen auf + Akk = look forward to (future)", "sich freuen über + Akk = be pleased about (present/past)", "3rd person is ALWAYS 'sich' (er freut sich, sie freuen sich)"], ["Reflexive Verbs", "Accusative"]),

        (76, "Reflexive Verbs with Dative: sich etwas anziehen / waschen", "Reflexive Verbs",
         "sich (Dativ): mir, dir, sich, uns, euch, sich + Accusative Object",
         "When an action involves a specific direct object belonging to the body (e.g. washing one's hands), the reflexive pronoun shifts to the Dative (mir/dir).",
         [{"de": "Ich wasche mir vor dem Essen gründlich die Hände.", "en": "I wash my hands thoroughly before eating."},
          {"de": "Zieh dir eine warme Jacke an, es ist kalt draußen!", "en": "Put on a warm jacket; it is cold outside!"}],
         ["If direct object is specified: mir/dir (Dativ)", "Ich wasche mich (Accusative - whole self)", "Ich wasche mir die Hände (Dative - hands are accusative object)"], ["Reflexive Verbs", "Dative"]),

        (77, "The Pronoun Order Rule in Clauses with Two Pronouns", "Sentence Structure",
         "Accusative Pronoun BEFORE Dative Pronoun (Akk vor Dat bei Pronomen)",
         "If a sentence contains two object pronouns, the Accusative pronoun ALWAYS precedes the Dative pronoun.",
         [{"de": "Ich gebe es (Akk) dir (Dat) heute Nachmittag zurück.", "en": "I will give it back to you this afternoon."}],
         ["Two nouns: Dative noun before Accusative noun (Ich gebe dem Mann das Buch)", "Two pronouns: Accusative pronoun before Dative pronoun (Ich gebe es ihm)", "Mnemonic: 'Es ihm' (never 'Ihm es')"], ["Pronoun Order", "Syntax"]),

        (78, "Double Object Noun Order (Dative Noun before Accusative Noun)", "Sentence Structure",
         "Dative Noun (Person) + Accusative Noun (Thing)",
         "When both objects are full nouns (with articles), German places the Dative indirect object before the Accusative direct object.",
         [{"de": "Die Großmutter schenkt dem Enkelkind (Dat) ein neues Fahrrad (Akk).", "en": "The grandmother gifts the grandchild a new bicycle."}],
         ["Person (Dativ) precedes Thing (Akkusativ)", "Der Lehrer erklärt den Schülern die Grammatik", "Changes only if pronouns are introduced"], ["Word Order", "Double Objects"]),

        (79, "Relative Clauses in Nominative (Relativsätze)", "Relative Clauses",
         "Relative Pronoun matches Gender/Number of noun + Case of its clause role",
         "Relative clauses provide descriptive detail about a noun and follow subordinate word order (verb at the end). In nominative, the pronouns are der, die, das, die.",
         [{"de": "Dort steht der Kollege, der das neue Projekt leitet.", "en": "Over there stands the colleague who leads the new project."},
          {"de": "Das ist das Hotel, das direkt am Strand liegt.", "en": "That is the hotel that is situated directly on the beach."}],
         ["Relative pronoun der/die/das/die matches gender of noun", "Finite verb moves to the end of the relative clause", "Separated by a mandatory comma"], ["Relativsätze", "Nominative"]),

        (80, "Relative Clauses in Accusative", "Relative Clauses",
         "Masc: den | Fem: die | Neut: das | Plural: die (Verb at end)",
         "When the relative pronoun represents the direct object inside the relative clause, the masculine pronoun changes to 'den'.",
         [{"de": "Das ist der Computer, den ich mir gestern gekauft habe.", "en": "That is the computer that I bought for myself yesterday."},
          {"de": "Hier sind die Dokumente, die du unterschreiben musst.", "en": "Here are the documents that you need to sign."}],
         ["Masculine relative pronoun in accusative = den", "Verb goes to the end: gekauft habe", "Preceded by a comma"], ["Relativsätze", "Accusative"]),

        (81, "Prepositions with Relative Clauses", "Relative Clauses",
         "Preposition + Relative Pronoun (in dem, mit dem, für die) + Verb at end",
         "When a relative clause requires a preposition, the preposition stands immediately before the relative pronoun at the start of the clause.",
         [{"de": "Das ist der Freund, mit dem ich nach Italien gereist bin.", "en": "That is the friend with whom I traveled to Italy."},
          {"de": "Die Stadt, in der ich studiere, heißt Münster.", "en": "The city in which I study is called Münster."}],
         ["Preposition dictates the case of the relative pronoun: mit -> Dativ (mit dem)", "in -> Dativ (in der Stadt -> in der)", "Verb stays at the very end"], ["Relativsätze", "Prepositions"]),

        (82, "Infinitives with 'zu' (Infinitiv mit zu Basics)", "Infinitive Clauses",
         "zu + Infinitive at the end of the clause | Separable verbs: stem + zu + verb",
         "Certain verbs (hoffen, planen, vergessen, versuchen, vorhaben) trigger a secondary clause where 'zu' precedes the infinitive.",
         [{"de": "Ich hoffe, dich bald wiederzusehen.", "en": "I hope to see you again soon."},
          {"de": "Er plant, im nächsten Jahr nach Deutschland umzuziehen.", "en": "He plans to move to Germany next year."}],
         ["Separable verbs: 'zu' goes in the middle (einzukaufen, aufzustehen)", "No subject pronoun in the 'zu' clause", "Preceded by a comma"], ["Infinitiv mit zu", "Syntax"]),

        (83, "Impersonal 'Es ist...' + Adjective + 'zu' + Infinitive", "Infinitive Clauses",
         "Es ist wichtig/schön/einfach/schwer, ... zu + Infinitiv",
         "Impersonal evaluations frequently use an adjective followed by an infinitive with 'zu'.",
         [{"de": "Es ist wichtig, jeden Tag ein wenig Deutsch zu üben.", "en": "It is important to practice a little German every day."},
          {"de": "Es ist gesund, viel frisches Gemüse zu essen.", "en": "It is healthy to eat lots of fresh vegetables."}],
         ["Es ist interessant / Es ist verboten / Es ist erlaubt", "zu + Infinitiv at the end", "Comma is mandatory"], ["Infinitiv mit zu", "Impersonal"]),

        (84, "Noun Phrases triggering 'zu' + Infinitive (Lust/Zeit/Angst haben)", "Infinitive Clauses",
         "Lust / Zeit / die Absicht haben, ... zu + Infinitiv",
         "Abstract nouns paired with 'haben' regularly trigger infinitive clauses with 'zu'.",
         [{"de": "Ich habe heute Abend keine Lust, selbst zu kochen.", "en": "I have no desire to cook myself this evening."},
          {"de": "Hast du Zeit, mir bei diesem Formular zu helfen?", "en": "Do you have time to help me with this form?"}],
         ["Lust haben zu...", "Zeit haben zu...", "Angst haben zu..."], ["Infinitiv mit zu", "Nouns"]),

        (85, "Purpose Clauses with 'um ... zu' + Infinitive", "Infinitive Clauses",
         "um ... zu + Infinitiv = in order to (Same subject in both clauses)",
         "'um ... zu' expresses the goal or intention of an action ('in order to'). It can only be used when the subject of both clauses is identical.",
         [{"de": "Ich lerne Deutsch, um bessere Karrierechancen zu haben.", "en": "I am learning German in order to have better career opportunities."},
          {"de": "Er spart Geld, um sich ein neues Auto zu kaufen.", "en": "He is saving money in order to buy a new car."}],
         ["um ... zu = in order to", "Subjects MUST be identical", "If subjects differ, you must use 'damit'!"], ["um zu", "Purpose", "Infinitive"]),

        (86, "Purpose Clauses with 'damit' (Different Subjects)", "Subordinate Clauses",
         "damit + Subject + ... + Verb at end (in order that / so that)",
         "'damit' is used to express purpose when the subjects of the two clauses are different (or optionally identical).",
         [{"de": "Ich erkläre es langsam, damit die Studenten die Grammatik verstehen.", "en": "I explain it slowly so that the students understand the grammar."}],
         ["Can handle different subjects: Ich (sub 1) ... die Studenten (sub 2)", "Kicks verb to the end", "'um...zu' is more elegant when subjects match"], ["damit", "Purpose", "Nebensätze"]),

        (87, "The Verb 'brauchen' + 'nicht / nur' + 'zu'", "Infinitive Clauses",
         "brauchen + nicht / nur + ... zu + Infinitiv = do not need to / only need to",
         "In German, 'brauchen' functions like a negative modal verb meaning 'need not', but MUST be paired with 'zu' and an infinitive.",
         [{"de": "Du brauchst heute nicht zur Arbeit zu gehen, es ist ein Feiertag.", "en": "You do not need to go to work today; it is a public holiday."},
          {"de": "Du brauchst mich nur anzurufen, wenn du Hilfe brauchst.", "en": "You only need to call me if you need help."}],
         ["Famous rhyme: 'Wer brauchen ohne zu gebraucht, braucht gar nicht zu gebrauchen!'", "Equivalent to: 'du musst nicht...'", "Must have 'nicht' or 'nur' + 'zu'"], ["brauchen", "Infinitive"]),

        (88, "Adverbs of Degree: sehr, ziemlich, ganz, etwas, kaum", "Adjectives",
         "kaum (barely) < etwas (a bit) < ganz (quite) < ziemlich (fairly) < sehr (very) < extrem",
         "Grading intensity of adjectives and verbs using standard degree modifiers.",
         [{"de": "Die Prüfung war ziemlich anspruchsvoll, aber machbar.", "en": "The exam was fairly demanding, but doable."}],
         ["sehr = very", "ziemlich = quite/fairly", "kaum = barely/hardly"], ["Adverbs", "Degree"]),

        (89, "Expressing Opinions: 'meiner Meinung nach' and 'Ich finde...'", "Dialogue Patterns",
         "Meiner Meinung nach + Verb in Pos 2 | Ich bin der Ansicht, dass...",
         "Standard linguistic structures for stating viewpoints in group discussions.",
         [{"de": "Meiner Meinung nach ist der öffentliche Nahverkehr in Berlin hervorragend.", "en": "In my opinion, public transit in Berlin is outstanding."},
          {"de": "Ich finde, dass wir mehr erneuerbare Energien nutzen sollten.", "en": "I find that we should use more renewable energy."}],
         ["Meiner Meinung nach occupies Position 1 -> Verb is in Position 2: '...ist der Nahverkehr'", "'Ich finde, dass...' kicks verb to end", "Polite debate framing"], ["Opinions", "Communication"]),

        (90, "Writing Professional Short Emails (A2 Register)", "Dialogue Patterns",
         "Sehr geehrte Damen und Herren / Liebe Grüße / Mit freundlichen Grüßen",
         "Standard opening and closing formulas for German emails in formal and informal registers.",
         [{"de": "Sehr geehrte Frau Müller, anbei sende ich Ihnen die gewünschten Unterlagen.", "en": "Dear Ms. Müller, attached I send you the requested documents."},
          {"de": "Mit freundlichen Grüßen, Ajay Singh Pundir", "en": "With friendly regards, Ajay Singh Pundir"}],
         ["Formal salutation: Sehr geehrte Damen und Herren / Sehr geehrter Herr...", "Formal closing: Mit freundlichen Grüßen (no comma after greeting!)", "Informal: Liebe Grüße"], ["Emails", "Correspondence"]),

        (91, "Describing an Illness & Doctor's Visit", "Dialogue Patterns",
         "Ich habe Kopfschmerzen / Mir tut der Rücken weh / Ich fühle mich schwach",
         "Medical vocabulary and dative constructions for doctor consultations in Germany.",
         [{"de": "Seit gestern tut mir der Hals weh und ich habe leichtes Fieber.", "en": "Since yesterday my throat has been hurting and I have a mild fever."}],
         ["weh tun + Dativ: Der Kopf tut mir weh", "haben + noun: Ich habe Husten / Schnupfen / Fieber", "Krankschreibung: doctor's sick note"], ["Health", "Doctor"]),

        (92, "At the Train Station: Announcements & Schedules", "Dialogue Patterns",
         "Gleis (track), Verspätung (delay), Ausfall (cancellation), Anschluss (connection)",
         "Navigating Deutsche Bahn announcements and ticket counters.",
         [{"de": "Der ICE nach München hat heute circa fünfzehn Minuten Verspätung.", "en": "The ICE to Munich is delayed by approximately fifteen minutes today."}],
         ["Gleis = track/platform", "auf Gleis 4 einfahren = arriving on track 4", "Anschluss erreichen = catching the connection"], ["Travel", "Train"]),

        (93, "Apartment Hunting: Key Terminology & Abbreviations", "Dialogue Patterns",
         "Warmmiete vs Kaltmiete, Kaution, Nebenkosten, WG (Wohngemeinschaft)",
         "Essential terms for renting an apartment in Germany.",
         [{"de": "Die Kaltmiete beträgt 800 Euro und die Nebenkosten liegen bei 200 Euro.", "en": "The base rent is 800 euros and utility charges are 200 euros."}],
         ["Kaltmiete: rent without heat/utilities", "Warmmiete: total rent with utilities", "Kaution: security deposit (usually 3 months cold rent)"], ["Housing", "Apartment"]),

        (94, "Bank & Postal Services in Germany", "Dialogue Patterns",
         "Konto eröffnen, überweisen, Geld abheben, Paket abholen, Einschreiben",
         "Vocabulary for everyday banking transactions and postal errands.",
         [{"de": "Ich möchte ein Girokonto eröffnen und eine neue Bankkarte beantragen.", "en": "I would like to open a checking account and apply for a new debit card."}],
         ["Girokonto = checking account", "Geld abheben = withdraw cash", "überweisen = bank wire transfer"], ["Banking", "Post"]),

        (95, "Making Telephone Calls in German", "Dialogue Patterns",
         "Hier spricht... | Kann ich bitte mit Herrn... sprechen? | Ich rufe wegen... an",
         "Telephone etiquette when making official inquiries or leaving voicemails.",
         [{"de": "Guten Tag, hier spricht Ajay Pundir. Ich rufe wegen Ihrer Wohnungsanzeige an.", "en": "Good day, this is Ajay Pundir speaking. I am calling regarding your apartment ad."}],
         ["Identify yourself immediately: 'Hier spricht...'", "Connecting: 'Könnten Sie mich bitte verbinden?'", "Ending: 'Auf Wiederhören' (phone only!)"], ["Telephone", "Speaking"]),

        (96, "Agreement and Disagreement Formulas", "Dialogue Patterns",
         "Da haben Sie völlig recht | Das sehe ich genauso | Ich bin anderer Meinung",
         "Formulas for constructive academic and workplace dialogue.",
         [{"de": "Da stimme ich dir vollkommen zu, das ist ein wichtiger Punkt.", "en": "I completely agree with you there; that is an important point."}],
         ["zustimmen + Dativ: Ich stimme Ihnen zu", "Recht haben: Du hast recht", "Widerspruch: Da bin ich anderer Meinung"], ["Debate", "Agreement"]),

        (97, "The Structure of Temporal Expressions (Wann?)", "Sentence Structure",
         "am (days, dates), um (clock times), im (months, seasons), in + Dat (in future duration)",
         "Quick reference matrix of time prepositions to ensure flawless scheduling.",
         [{"de": "Wir fliegen im August am Montag um 14 Uhr ab.", "en": "We depart in August on Monday at 2 PM."}],
         ["am + Tag: am Dienstag", "im + Monat/Jahreszeit: im Juli, im Sommer", "um + Uhrzeit: um 15:30 Uhr"], ["Time", "Prepositions"]),

        (98, "The Structure of Spatial Expressions (Wo vs Wohin Review)", "Sentence Structure",
         "nach (cities/countries) vs in (into buildings/countries with article) vs zu (to people/brands)",
         "Distinguishing directional prepositions: nach, in, and zu.",
         [{"de": "Ich fliege nach Italien, gehe dann in das Hotel und danach zu meinem Kunden.", "en": "I fly to Italy, then go into the hotel and after that to my client."}],
         ["nach + City/Country without article", "in + Building (into interior)", "zu + Person/Company"], ["Spatial", "Prepositions"]),

        (99, "Concessive Connector: 'trotzdem' (nevertheless / anyway)", "Sentence Structure",
         "trotzdem sits in Position 1 (inversion) or Position 3 (after verb)",
         "'trotzdem' is an adverbial connector indicating that an action happens despite a counter-circumstance.",
         [{"de": "Es regnet stark draußen. Trotzdem gehe ich im Park joggen.", "en": "It is raining heavily outside. Nevertheless, I go jogging in the park."}],
         ["trotzdem causes inversion: Trotzdem gehe ich...", "Connects two main clauses", "Contrast with 'obwohl' (which is a subordinate conjunction)"], ["trotzdem", "Concessive"]),

        (100, "Consecutive Connector: 'deshalb / deswegen' (therefore)", "Sentence Structure",
         "deshalb / deswegen sits in Position 1 + Verb in Pos 2 + Subject in Pos 3",
         "Adverbial connectors indicating logical consequence.",
         [{"de": "Ich habe morgen eine wichtige Prüfung, deshalb muss ich heute viel lernen.", "en": "I have an important exam tomorrow; therefore, I must study a lot today."}],
         ["Cause in clause 1 -> Effect introduced by deshalb", "Causes V2 inversion: deshalb muss ich...", "deshalb and deswegen are synonymous"], ["deshalb", "Cause and Effect"]),

        (101, "Additive Connector: 'außerdem' (furthermore / in addition)", "Sentence Structure",
         "außerdem sits in Position 1 + Verb in Pos 2",
         "Adds a reinforcing secondary point or argument.",
         [{"de": "Die Wohnung ist sehr geräumig. Außerdem liegt sie direkt an der U-Bahn.", "en": "The apartment is very spacious. Furthermore, it is situated directly on the subway."}],
         ["außerdem = furthermore / moreover", "Position 1 triggers inversion: Außerdem liegt sie...", "Useful for writing cohesive texts"], ["außerdem", "Connectors"]),

        (102, "Alternative Connector: 'sonst' (otherwise / or else)", "Sentence Structure",
         "sonst sits in Position 1 + Verb in Pos 2",
         "Expresses negative conditional consequence: what happens if the first action is not taken.",
         [{"de": "Wir müssen uns beeilen, sonst verpassen wir den letzten Zug.", "en": "We must hurry, otherwise we will miss the last train."}],
         ["sonst = otherwise / or else", "Position 1 triggers inversion: sonst verpassen wir", "Warning structure"], ["sonst", "Connectors"]),

        (103, "Negation Recap: 'nicht' vs 'kein' Comprehensive Rules", "Sentence Structure",
         "kein for unarticled / indefinite nouns | nicht for verbs, adjectives, definite nouns",
         "A definitive decision tree for selecting correct German negation.",
         [{"de": "Ich trinke keine Milch (kein), denn ich bin nicht durstig (nicht).", "en": "I drink no milk, because I am not thirsty."}],
         ["Nouns with ein/no article -> kein", "Adjectives & Adverbs -> nicht", "Entire action -> nicht at end of clause"], ["Negation", "Review"]),

        (104, "Polite Modal Subjunctive: 'könnten' and 'würden' in A2", "Modal Verbs",
         "Könnten Sie mir bitte helfen? | Würden Sie bitte die Tür schließen?",
         "Softening requests in daily life using the subjunctive II of können and werden.",
         [{"de": "Könnten Sie mir bitte sagen, wo der Fahrkartenautomat steht?", "en": "Could you please tell me where the ticket vending machine is?"}],
         ["Much more polite than imperative", "Könnten Sie... (Could you...)", "Würden Sie... (Would you...)"], ["Polite", "Konjunktiv II"]),

        (105, "The A2 Mastery Synthesis: Complex Sentences Checklist", "Sentence Structure",
         "Perfekt tense mastery, Dative case confidence, Two-way prepositions, Subordinate clauses",
         "A complete recap of the structural milestones achieved at Level A2.",
         [{"de": "Obwohl es gestern geregnet hat, bin ich mit dem Fahrrad zur Arbeit gefahren.", "en": "Although it rained yesterday, I rode my bicycle to work."}],
         ["Accurate Dative & Accusative usage", "Automatic verb-final word order in Nebensätze", "Proficiency in conversational Perfekt"], ["Summary", "A2 Mastery", "Checklist"])
    ]

    for item in remaining_a2:
        add_t(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])

    assert len(topics) == 105, f"Expected 105 A2 topics, got {len(topics)}"
    return topics

if __name__ == "__main__":
    t = get_a2_topics()
    with open("deutsche/data/a2.js", "w", encoding="utf-8") as f:
        f.write("// German Grammar Topics - Level A2 (Elementary Fluency) - Exactly 105 Topics\n")
        f.write("window.GERMAN_DATA_A2 = " + json.dumps(t, indent=2, ensure_ascii=False) + ";\n")
    print(f"✅ Generated deutsche/data/a2.js with {len(t)} topics!")
