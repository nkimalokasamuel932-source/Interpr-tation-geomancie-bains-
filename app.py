import streamlit as st

# ==============================================================================
# CONFIGURATION DE L'APPLICATION
# ==============================================================================
st.set_page_config(
    page_title="Oracle Ramrou — Grand Grimoire Théurgique", 
    page_icon="🔮", 
    layout="wide"
)

st.title("🔮 Oracle Ramrou — Cabinet Théurgique & Grand Grimoire")
st.markdown("Analyse complète et structurée : Passations, 70 règles d'engendrement des Maîtres, et Pharmacie Spirituelle (Psaumes, Versets, Salomon & Procédés Nassi).")

# ==============================================================================
# 1. BASE DE DONNÉES THÉURGIQUE COMPLÈTE DES 16 FIGURES
# ==============================================================================
PROPRIETES_FIGURES = {
    "Youssouf": {
        "num": 1, "nature": "Diable Mauvais", "groupe": "Mobiles", "element": "Feu (Est)",
        "psaume": "Psaume 109 (Contre les calomnies et les ennemis acharnés)",
        "verset": "Genèse 39:2 — 'L'Éternel fut avec Joseph, et la prospérité l'accompagna...'",
        "salomon": "Prière pour briser les complots secrets, déjouer les trahisons de l'ombre et restaurer la dignité.",
        "nassi": "Écrire la figure 111 fois sur une tablette en bois, laver avec de l'eau de puits, y ajouter du safran et du parfum de rose. À utiliser en bain rituel pendant 7 jours consécutifs avant le lever du soleil."
    },
    "Adama": {
        "num": 2, "nature": "Diable Bon", "groupe": "Sortants", "element": "Feu (Est)",
        "psaume": "Psaume 121 (Pour la protection dans les déplacements et les voyages)",
        "verset": "Genèse 2:7 — 'L'Éternel Dieu forma l'homme de la poussière de la terre...'",
        "salomon": "Prière d'ancrage territorial, de déblocage des biens fonciers et d'ouverture des portes matérielles fermées.",
        "nassi": "Tracer la figure 45 fois sur une ardoise. Recueillir l'eau dans un récipient propre, ajouter une poignée de gros sel béni. S'en asperger le corps et laver le seuil de son entrée pour attirer les opportunités terrestres."
    },
    "Mahdy": {
        "num": 3, "nature": "Diable Bon", "groupe": "Rentrants", "element": "Air (Ouest)",
        "psaume": "Psaume 23 (Pour l'abondance financière, la subsistance et la paix de l'esprit)",
        "verset": "Jérémie 29:11 — 'Car je connais les projets que j'ai formés sur vous...'",
        "salomon": "Prière pour l'attraction de la grâce, l'obtention de bourses, de crédits et l'accomplissement des promesses.",
        "nassi": "Écrire la figure 66 fois (valeur mystique du nom divin) avec de l'eau de rose et du musc. Diviser le Nassi en deux : boire une gorgée chaque matin à jeun et utiliser le reste pour l'onction quotidienne du visage."
    },
    "Idriss": {
        "num": 4, "nature": "Diable Bon", "groupe": "Fixes", "element": "Eau (Nord)",
        "psaume": "Psaume 119:9-16 (Pour la clarté mentale, la sagesse et l'illumination spirituelle)",
        "verset": "Hébreux 11:5 — 'C'est par la foi qu'Énoch fut enlevé pour qu'il ne vît point la mort...'",
        "salomon": "Prière de Salomon pour l'acquisition d'une intelligence supérieure, la mémoire infaillible et le discernement.",
        "nassi": "Écrire la figure 360 fois (nombre de l'élévation sphérique). Diluer dans de l'eau de pluie collectée un jeudi. Utiliser cette eau sacrée pour oindre la tête et le front avant les séances d'études ou de méditation."
    },
    "Ibrahima": {
        "num": 5, "nature": "Humain Bon", "groupe": "Mobiles", "element": "Eau (Nord)",
        "psaume": "Psaume 112 (Bénédiction majeure sur la postérité, la lignée et la prospérité de la maison)",
        "verset": "Genèse 12:2 — 'Je ferai de toi une grande nation, et je te bénirai...'",
        "salomon": "Prière d'alliance sacrée, de protection contre le feu, de fécondité et d'extension des limites.",
        "nassi": "Écrire la figure 72 fois. Infuser l'écriture obtenue avec des feuilles de menthe fraîche. Boire en famille ou asperger discrètement la chambre des enfants pour pérenniser la paix et la protection du foyer."
    },
    "Inssa": {
        "num": 6, "nature": "Humain Mauvais", "groupe": "Sortants", "element": "Eau (Nord)",
        "psaume": "Psaume 6 (Pour la guérison des maladies physiques et l'apaisement des douleurs de l'âme)",
        "verset": "Ésaïe 53:5 — 'Mais il était wounded pour nos péchés, brisé pour nos iniquités...'",
        "salomon": "Prière de délivrance contre les afflictions biologiques, les opérations chirurgicales et les crises psychologiques.",
        "nassi": "Écrire la figure 99 fois à l'encre noire traditionnelle (Sami). Laver la tablette avec une décoction de feuilles de neem ou de verveine. Laver entièrement le corps du malade avec ce liquide purificateur."
    },
    "Omar": {
        "num": 7, "nature": "Diable Mauvais", "groupe": "Fixes", "element": "Air (Ouest)",
        "psaume": "Psaume 35 (Contre les adversaires injustes, les procès, les rivaux et les litiges)",
        "verset": "Proverbes 31:10 — 'Qui peut trouver une femme vertueuse ? Elle a bien plus de valeur que les perles.'",
        "salomon": "Prière pour pacifier les relations conjugales, neutraliser la discorde amoureuse et exposer les comploteurs.",
        "nassi": "Tracer la figure 28 fois (liée aux demeures lunaires). Diluer dans de l'eau de source. Ajouter sept gouttes de parfum sans alcool. Utiliser en aspersion dans les quatre coins de la maison pour chasser les ondes de jalousie."
    },
    "Ayoub": {
        "num": 8, "nature": "Diable Mauvais", "groupe": "Rentrants", "element": "Terre (Sud)",
        "psaume": "Psaume 88 (Prière de secours dans la détresse profonde, la solitude et la stagnation totale)",
        "verset": "Job 19:25 — 'Mais je sais que mon rédempteur est vivant, et qu'il se lèvera le dernier...'",
        "salomon": "Prière de restauration des biens perdus, de patience prophétique et de brisement du décret de ruine ou de deuil.",
        "nassi": "Écrire la figure 88 fois sur une tablette. Dissoudre dans de l'eau tiède mélangée à une cuillère de miel pur. Se laver entièrement un samedi soir pour rompre la lourdeur karmique et les blocages héréditaires."
    },
    "Allahou": {
        "num": 9, "nature": "Humain Mauvais", "groupe": "Sortants", "element": "Feu (Est)",
        "psaume": "Psaume 91 (La forteresse divine, bouclier impénétrable et protection absolue)",
        "verset": "Exode 20:2 — 'Je suis l'Éternel, ton Dieu, qui t'ai fait sortir du pays d'Égypte...'",
        "salomon": "Invocation de la Souveraineté Divine pour détruire et annuler les rituels inverses et les envoûtements.",
        "nassi": "Écrire la figure 114 fois (nombre de sourates/vibrations de complétude). Utiliser de l'eau de puits non polluée. Diviser en flacons : un pour boire un verre chaque vendredi matin, un autre pour purifier le lieu de commerce."
    },
    "Souleymane": {
        "num": 10, "nature": "Humain Bon", "groupe": "Fixes", "element": "Terre (Sud)",
        "psaume": "Psaume 72 (Pour l'élévation sociale, le pouvoir politique, la justice et la royauté)",
        "verset": "1 Rois 3:12 — 'Voici, j'agirai selon ta parole. Je te donnerai un cœur sage et intelligent...'",
        "salomon": "La Grande Prière de Sagesse, de Domination sur les éléments et d'Héritage Royal de Salomon.",
        "nassi": "Écrire la figure 110 fois. Utiliser une eau purifiée infusée au bois de santal. S'en oindre les mains, le visage et les pieds avant tout rendez-vous d'affaires capital ou démarche administrative majeure."
    },
    "Aliou": {
        "num": 11, "nature": "Humain Mauvais", "groupe": "Fixes", "element": "Air (Ouest)",
        "psaume": "Psaume 144 (Pour la victoire éclatante dans les combats spirituels et physiques)",
        "verset": "Éphésiens 6:11 — 'Revêtez-vous de toutes les armes de Dieu, afin de pouvoir tenir ferme...'",
        "salomon": "Prière du Bouclier de Salomon contre les attaques frontales, les agressions armées et les forces de la nuit.",
        "nassi": "Écrire la figure 63 fois. Ajouter un morceau de camphre écrasé à l'eau de lavage. Se laver le corps un mardi à l'heure de Mars pour acquérir une force invincible et repousser les ennemis."
    },
    "Nouhou": {
        "num": 12, "nature": "Humain Bon", "groupe": "Rentrants", "element": "Terre (Sud)",
        "psaume": "Psaume 29 (La voix de l'Éternel sur les grandes eaux et contre les forces destructrices)",
        "verset": "Genèse 6:8 — 'Mais Noé trouva grâce aux yeux de l'Éternel.'",
        "salomon": "Prière de préservation au milieu des tempêtes de la vie, des inondations et des complots de sorcellerie noire.",
        "nassi": "Écrire la figure 77 fois. Laver à l'eau de mer (ou ajouter du gros sel marin). Laver le sol de votre concession, magasin ou maison pour dissoudre instantanément toute charge occulte enfouie."
    },
    "Assane": {
        "num": 13, "nature": "Diable Mauvais", "groupe": "Sortants", "element": "Eau (Nord)",
        "psaume": "Psaume 3 (Contre l'humiliation publique, le déshonneur et le grand nombre d'ennemis)",
        "verset": "Psaume 3:3 — 'Mais toi, ô Éternel ! tu es mon bouclier, tu es ma gloire, et tu relèves ma tête.'",
        "salomon": "Prière de retournement de situation pour transmuter la honte publique en victoire et respect éclatant.",
        "nassi": "Écrire la figure 55 fois avec une encre safranée. Diluer dans de l'eau claire, ajouter des feuilles de laurier bénies. Se laver pendant 3 jours consécutifs pour nettoyer l'aura des souillures de l'opprobre."
    },
    "Younouss": {
        "num": 14, "nature": "Diable Bon", "groupe": "Mobiles", "element": "Terre (Sud)",
        "psaume": "Psaume 4 (Pour la délivrance immédiate des blocages financiers et l'effacement des dettes)",
        "verset": "Jonas 2:10 — 'L'Éternel parla au poisson, et le poisson vomit Jonas sur la terre...'",
        "salomon": "Prière d'urgence pour sortir des situations de faillite, d'étouffement financier et de pièges monétaires.",
        "nassi": "Écrire la figure 40 fois (en mémoire des 40 jours de Jonas). Utiliser de l'eau de source pure. Y plonger une pièce de monnaie en argent pendant 24 heures, offrir la pièce en aumône, puis utiliser le Nassi en friction sur les mains."
    },
    "Ousmane": {
        "num": 15, "nature": "Humain Bon", "groupe": "Rentrants", "element": "Air (Ouest)",
        "psaume": "Psaume 119:105 — 'Ta parole est une lampe à mes pieds, Et une lumière sur mon sentier.'",
        "verset": "Actes 2:4 — 'Et ils furent tous remplis du Saint-Esprit, et se mirent à parler en d'autres langues...'",
        "salomon": "Prière d'intercession spirituelle, d'éveil des canaux prophétiques et de haute connexion théurgique.",
        "nassi": "Écrire la figure 19 fois. Infuser l'écriture avec quelques larmes de résine d'encens d'Oliban mâle. Boire un demi-verre de ce Nassi avant les séances de haute consultation pour ouvrir le troisième œil."
    },
    "Moussa": {
        "num": 16, "nature": "Humain Mauvais", "groupe": "Fixes", "element": "Feu (Est)",
        "psaume": "Psaume 68 (Que Dieu se lève, et que ses ennemis se dispersent devant sa face !)",
        "verset": "Exode 14:13 — 'Moïse répondit au peuple : Ne craignez rien, restez en place, et regardez...'",
        "salomon": "Prière d'ouverture de la Mer Rouge (Brise les barrières majeures et crée des voies là où tout semble bloqué).",
        "nassi": "Écrire la figure 16 fois (symbole de la complétude géomantique). Diluer dans de l'eau de source prélevée à l'aube. Utiliser pour nettoyer le seuil de la maison, l'espace commercial ou à employer en grand bain de libération."
    }
}

# ==============================================================================
# 2. DEFINITION ET CONFIGURATION DES MAISONS GÉOMANTIQUES
# ==============================================================================
MAISONS_RAMROU = {
    1: {"nom": "M1 (Maison de l'Âme)", "desc": "L'être physique, la personnalité profonde, l'état présent du consultant."},
    2: {"nom": "M2 (Maison de la Chance)", "desc": "Les finances, les gains financiers immédiats, la chance matérielle liquide."},
    3: {"nom": "M3 (Maison des Mères)", "desc": "L'entourage proche, les frères et sœurs, les démarches et écrits de courte durée."},
    4: {"nom": "M4 (Maison des Pères)", "desc": "Le foyer familial, le patrimoine immobilier, les secrets ancestraux, la fin de l'affaire."},
    5: {"nom": "M5 (Maison des Enfants)", "desc": "La descendance, les amours, les plaisirs, les créations, les grossesses."},
    6: {"nom": "M6 (Maison des Malades)", "desc": "La santé physique, les maladies latentes, les charges de travail, les servitudes."},
    7: {"nom": "M7 (Maison du Mariage)", "desc": "Le conjoint, le partenaire de vie, les contrats d'association, les adversaires déclarés."},
    8: {"nom": "M8 (Maison du Changement)", "desc": "L'extérieur, l'étranger, les transformations profondes, la mort mystique, les héritages."},
    9: {"nom": "M9 (Maison de Dieu)", "desc": "La spiritualité, la foi, les longs voyages, les hautes études, les visions nocturnes."},
    10: {"nom": "M10 (Maison des Rois)", "desc": "Le pouvoir, l'autorité, la profession, la renommée sociale, l'élévation."},
    11: {"nom": "M11 (Maison de l'Espoir)", "desc": "Les amis fidèles, les espoirs secrets, les protections, les aides et appuis extérieurs."},
    12: {"nom": "M12 (Maison des Ennemis)", "desc": "Les ennemis de l'ombre, la sorcellerie, les pièges cachés, les prisons, les épreuves occultes."},
    13: {"nom": "M13 (Maison du Chambre / Foyer)", "desc": "L'intimité immédiate du couple, l'ambiance du lit conjugal, le présent immédiat."},
    14: {"nom": "M14 (Maison des Fortunes)", "desc": "Les gains futurs, l'argent à moyen terme, le devenir du commerce ou des investissements."},
    15: {"nom": "M15 (Maison de l'Espace)", "desc": "La clarté publique, l'opinion de l'entourage, les rumeurs, le témoin général."},
    16: {"nom": "M16 (Maison de Finition)", "desc": "La conclusion finale, le verdict ultime et irrévocable du thème céleste."}
}

INTERPRETATIONS_PASSATIONS = {
    1: "Apporte un impact direct sur la vitalité, le comportement ou l'état d'esprit actuel du consultant.",
    2: "Transfère son énergie directement sur les finances, les gains immédiats ou la chance matérielle.",
    3: "Influence l'entourage proche, les démarches courtes, la fratrie ou les voisins.",
    4: "S'ancre dans le patrimoine, les relations avec le père, le foyer ou la conclusion définitive de l'affaire.",
    5: "Retentit sur la descendance, une grossesse en cours, les amours ou les désirs profonds.",
    6: "Alerte sur une maladie latente, un surcroît de travail ou des obstacles physiques évidents.",
    7: "Impacte directement le partenaire (conjoint), l'adversaire déclaré ou les contrats d'association.",
    8: "Parle de l'extérieur, de l'étranger, de transformations profondes, de peurs ou d'héritages matériels.",
    9: "Ouvre sur la quête spirituelle, la religion, la recherche intellectuelle ou un grand voyage à venir.",
    10: "Projette l'énergie sur la réussite professionnelle, le pouvoir, l'autorité ou l'élévation sociale.",
    11: "Nourrit les espoirs secrets, l'aide des amis fidèles, les appuis extérieurs et les projets futurs.",
    12: "Révèle des blocages cachés, des ennemis de l'ombre, des pièges ou des pratiques occultes.",
    13: "Se manifeste au cœur du foyer intime, dans la chambre à coucher ou dans le présent le plus immédiat.",
    14: "Indique les rentrées d'argent futures, le commerce à moyen terme ou les gains en attente.",
    15: "Diffuse la clarté d'esprit de la figure ou, au contraire, sème des rumeurs dans l'entourage public.",
    16: "Agit comme la sentence finale et l'accomplissement irrévocable du thème."
}

# ==============================================================================
# 3. BASE DES INTERPRÉTATIONS MAGISTRALES : LES 70 RÈGLES DE COPULATION
# ==============================================================================
REGLES_COPULATIONS = {
    "Moussa": [
        {"parents": ("Youssouf", "Youssouf"), "verdict": "Trahison collective — les gens se regroupent en secret pour trahir le consultant."},
        {"parents": ("Adama", "Adama"), "verdict": "Indique la formation ou la présence active d'un groupe de jeunes."},
        {"parents": ("Mahdy", "Mahdy"), "verdict": "Convergence positive — indique un groupe de personnes réunies pour avancer sur un excellent projet."},
        {"parents": ("Idriss", "Idriss"), "verdict": "Urbanisme/Communauté — indique un ensemble de maisons, un village ou une ville entière."},
        {"parents": ("Ibrahima", "Ibrahima"), "verdict": "Indique de façon certaine la présence d'un groupe d'enfants."},
        {"parents": ("Inssa", "Inssa"), "verdict": "Épreuve collective — indique une souffrance ou un calvaire généralisé pour la communauté."},
        {"parents": ("Omar", "Omar"), "verdict": "Indique une assemblée ou un rassemblement de femmes."},
        {"parents": ("Ayoub", "Ayoub"), "verdict": "Affliction collective — indique un rassemblement de personnes pour des obsèques ou funérailles."},
        {"parents": ("Allahou", "Allahou"), "verdict": "Indique la présence mystique d'un groupe de jumeaux."},
        {"parents": ("Souleymane", "Souleymane"), "verdict": "Haute sphère — indique un groupe de chefs, de ministres ou de patrons en réunion secrète pour un but unique."},
        {"parents": ("Aliou", "Aliou"), "verdict": "Force armée — indique un groupe de soldats, de forces de l'ordre ou de guerriers."},
        {"parents": ("Nouhou", "Nouhou"), "verdict": "Sorcellerie de groupe — indique un groupe d'individus malveillants ou de sorciers ligués pour détruire."},
        {"parents": ("Assane", "Assane"), "verdict": "Opprobre public — indique un groupe de personnes qui subiront ensemble le déshonneur ou la honte."},
        {"parents": ("Younouss", "Younouss"), "verdict": "Prospérité locale — indique la richesse globale du pays, de la commune ou du foyer élargi."},
        {"parents": ("Ousmane", "Ousmane"), "verdict": "Lignée spirituelle — indique une réunion sacrée ou un groupe de marabouts, prêtres ou lettrés."},
        {"parents": ("Moussa", "Moussa"), "verdict": "Harmonie parfaite — indique un groupe où règnent l'entente cordiale, la paix absolue et l'unité."}
    ],
    "Ousmane": [
        {"parents": ("Youssouf", "Adama"), "verdict": "Secret spirituel — indique la présence d'un marabout ou guide spirituel caché à l'ombre."},
        {"parents": ("Mahdy", "Ayoub"), "verdict": "Évolution radieuse — indique le bonheur stable, l'accroissement continu et l'avancement social."},
        {"parents": ("Inssa", "Ibrahima"), "verdict": "Problème de santé infantile — indique un enfant malade, une affection cutanée ou une maladie apparente."},
        {"parents": ("Omar", "Ayoub"), "verdict": "Conflit ésotérique ou intellectuel — indique des marabouts ou des lettrés qui s'affrontent mystiquement."},
        {"parents": ("Allahou", "Souleymane"), "verdict": "Sagesse authentique — désigne un marabout intègre, saint et juste, qui œuvre pour le bien."},
        {"parents": ("Aliou", "Nouhou"), "verdict": "Imposture spirituelle — désigne un faux marabout, un charlatan dangereux et menteur."},
        {"parents": ("Younouss", "Assane"), "verdict": "Énergie de la traque — indique un chasseur, un policier ou quelqu'un qui piste."},
        {"parents": ("Moussa", "Ousmane"), "verdict": "Affluence commerciale — indique une foule immense ou une forte activité au marché / foire."}
    ],
    "Younouss": [
        {"parents": ("Youssouf", "Aliou"), "verdict": "Richesse externe — indique explicitement la fortune ou les finances florissantes d'une tierce personne."},
        {"parents": ("Adama", "Nouhou"), "verdict": "Grâce providentielle — indique de manière certaine que Dieu accordera la richesse matérielle au consultant."},
        {"parents": ("Mahdy", "Allahou"), "verdict": "Théurgie financière — indique que des prières intenses ou des travaux sacrés ont été accomplis pour attirer l'argent."},
        {"parents": ("Idriss", "Souleymane"), "verdict": "Patrimoine proche — indique la richesse consolidée du foyer familial ou des parents proches."},
        {"parents": ("Inssa", "Ayoub"), "verdict": "Ruine et faillite — indique une perte sèche, un vol massif ou un grand gaspillage d'argent."},
        {"parents": ("Ibrahima", "Omar"), "verdict": "Opulence sans descendance — désigne une femme immensément riche mais qui ne parvient pas à enfanter."},
        {"parents": ("Younouss", "Moussa"), "verdict": "Prospérité collective — indique la richesse économique d'un groupe, d'une association ou du village entier."}
    ],
    "Assane": [
        {"parents": ("Youssouf", "Nouhou"), "verdict": "Amertume profonde — indique de cuisants regrets face à une opportunité manquée ou gâchée."},
        {"parents": ("Adama", "Aliou"), "verdict": "Heureux présage biologique — annonce l'arrivée imminente d'une grossesse gémellaire (jumeaux)."},
        {"parents": ("Mahdy", "Souleymane"), "verdict": "Répétition cyclique — indique formellement que l'événement ou la situation va se reproduire à l'identique."},
        {"parents": ("Idriss", "Allahou"), "verdict": "Menace humaine directe — indique la malveillance d'un jeune homme violent ou très méchant."},
        {"parents": ("Ibrahima", "Ayoub"), "verdict": "Retour karmique — indique avec certitude que la situation passée (bonne ou mauvaise) va revenir."},
        {"parents": ("Inssa", "Omar"), "verdict": "Trouble organique aigu — indique des coliques ou des maux de ventre sévères."},
        {"parents": ("Ousmane", "Younouss"), "verdict": "Lutte stérile — indique des individus tentant vainement d'arrêter un processus naturel inéluctable."},
        {"parents": ("Moussa", "Assane"), "verdict": "Flux monétaire fulgurant — indique une entrée d'argent particulièrement rapide et inattendue."}
    ],
    "Nouhou": [
        {"parents": ("Youssouf", "Assane"), "verdict": "Hostilité familiale — indique une méchanceté ou des rancœurs nées à cause d'un enfant."},
        {"parents": ("Adama", "Younouss"), "verdict": "Discorde matérielle — indique une méchanceté sous-jacente liée à une affaire d'héritage ou de partage."},
        {"parents": ("Ibrahima", "Allahou"), "verdict": "Hostilité parentale — indique des actions malveillantes portées spécifiquement sur les enfants du foyer."},
        {"parents": ("Omar", "Mahdy"), "verdict": "Rivalité destructrice — indique une méchanceté déclenchée à la suite d'une rivalité amoureuse autour d'une femme."},
        {"parents": ("Inssa", "Souleymane"), "verdict": "Abus de pouvoir tyrannique — indique la méchanceté cruelle provenant d'un chef hiérarchique ou d'une autorité."},
        {"parents": ("Ayoub", "Idriss"), "verdict": "Poison intime — indique une méchanceté active au sein même de la cellule familiale restreinte."},
        {"parents": ("Aliou", "Ousmane"), "verdict": "Occultisme noir acharné — signale des attaques occultes orchestrées par un marabout ou géomancien adverse."},
        {"parents": ("Moussa", "Nouhou"), "verdict": "Complot de faction — indique une méchanceté flagrante perpétrée par un groupe de personnes liguées contre toi."}
    ],
    "Aliou": [
        {"parents": ("Youssouf", "Younouss"), "verdict": "Espoir d'opulence — désigne une femme animée par un immense espoir de faire fortune."},
        {"parents": ("Adama", "Assane"), "verdict": "Impératif rituel — Le thème exige impérativement un sacrifice de couleur rouge (coq, tissu, dattes) pour réussir."},
        {"parents": ("Mahdy", "Ayoub"), "verdict": "Entrave ou stérilité — indique un blocage net ou de grandes difficultés biologiques pour concevoir."},
        {"parents": ("Idriss", "Omar"), "verdict": "Cataclysme ou intempérie — indique le déchaînement de vents violents ou d'une tempête causant des dégâts matériels."},
        {"parents": ("Ibrahima", "Souleymane"), "verdict": "Conception sacrée — confirme de manière indubitable une grossesse saine en cours ou imminente."},
        {"parents": ("Nouhou", "Ousmane"), "verdict": "Élévation honorifique — annonce l'avènement certain de la grandeur, de la notoriété et de l'honneur public."},
        {"parents": ("Allahou", "Inssa"), "verdict": "Épreuve critique immédiate — indique la confrontation imminente avec une immense difficulté de vie."},
        {"parents": ("Moussa", "Aliou"), "verdict": "Alignement martial — indique un rassemblement de militaires, de forces de l'ordre ou de factions en armes."}
    ],
    "Souleymane": [
        {"parents": ("Youssouf", "Omar"), "verdict": "Désigne une femme extrêmement riche, influente et autonome."},
        {"parents": ("Adama", "Ayoub"), "verdict": "Verrouillage de destin — indique que la chance matérielle ou l'opportunité recherchée est hermétiquement fermée."},
        {"parents": ("Mahdy", "Idriss"), "verdict": "Solution dissimulée — l'affaire est cachée ou n'aura d'issue positive qu'au prix d'un sacrifice rigoureux."},
        {"parents": ("Idriss", "Younouss"), "verdict": "Trésor enfoui — indique la présence d'une grosse somme d'argent cachée ou épargnée en secret."},
        {"parents": ("Nouhou", "Inssa"), "verdict": "Despotisme — désigne un chef, un directeur ou une autorité impitoyable, injuste et colérique."},
        {"parents": ("Aliou", "Ibrahima"), "verdict": "Destinée de leader — annonce la naissance ou la présence d'un enfant promis à devenir un très grand chef."},
        {"parents": ("Ousmane", "Allahou"), "verdict": "Gouvernance intègre — désigne un dirigeant ou patron correct, juste, craignant Dieu et bienveillant."},
        {"parents": ("Moussa", "Souleymane"), "verdict": "Sommet officiel — indique une réunion imminente de hauts dirigeants, de présidents ou d'autorités décisionnaires."}
    ],
    "Allahou": [
        {"parents": ("Youssouf", "Ayoub"), "verdict": "Cécité géomantique — L'affaire demandée est 'aveugle' : elle ne possède absolument aucune solution spirituelle ou matérielle."},
        {"parents": ("Adama", "Omar"), "verdict": "Théurgie de conception — indique des prières intenses accomplies pour féconder et obtenir des enfants."},
        {"parents": ("Mahdy", "Younouss"), "verdict": "Théurgie d'attraction — indique des rituels et prières profonds pour attirer la richesse financière."},
        {"parents": ("Idriss", "Idriss"), "verdict": "Prière rogatoire — indique des prières ou rituels collectifs d'urgence pour faire tomber la pluie ou apaiser la terre."},
        {"parents": ("Souleymane", "Ousmane"), "verdict": "Affliction intime — indique une maladie ou infection localisée au niveau des organes génitaux ou de l'appareil sexuel."},
        {"parents": ("Aliou", "Inssa"), "verdict": "Fermeture occulte — indique un blocage hermétique et ésotérique appliqué sur la chose demandée."},
        {"parents": ("Nouhou", "Ibrahima"), "verdict": "Action de grâce — désigne une personne comblée par les bienfaits divins qui remercie chaleureusement le Ciel."},
        {"parents": ("Moussa", "Allahou"), "verdict": "Transit — désigne des voyageurs ou des personnes actuellement en route vers le consultant."}
    ]
}

# ==============================================================================
# 4. INTERFACE DE SAISIE DE L'ORACLE (BARRE LATÉRALE)
# ==============================================================================
st.sidebar.header("📥 Saisie des 16 Maisons Géomantiques")
liste_choix = list(PROPRIETES_FIGURES.keys())
theme_actuel = {}

# Génération des sélecteurs pour les 16 maisons
for m in range(1, 17):
    theme_actuel[m] = st.sidebar.selectbox(
        f"{MAISONS_RAMROU[m]['nom']}",
        liste_choix,
        index=(m - 1) % len(liste_choix),
        key=f"m_{m}"
    )

# Visualisation sous forme de tableau de bord principal
st.subheader("📊 Configuration actuelle de l'Échiquier Géomantique")
cols_grille = st.columns(4)
for idx, m_id in enumerate(range(1, 17)):
    col = cols_grille[idx % 4]
    with col:
        st.markdown(f"**M{m_id}** ({MAISONS_RAMROU[m_id]['nom'].split(' ')[0]}) : `{theme_actuel[m_id]}`")

st.markdown("---")

# ==============================================================================
# 5. MOTEUR DE PASSATION (MIGRATIONS GÉOMANTIQUES)
# ==============================================================================
st.header("🔄 ANALYSE DES PASSATIONS (MIGRATIONS DES FIGURES)")

cartographie_passations = {}
for m_id, fig_nom in theme_actuel.items():
    if fig_nom not in cartographie_passations:
        cartographie_passations[fig_nom] = []
    cartographie_passations[fig_nom].append(m_id)

# Filtrer uniquement les figures qui apparaissent au moins deux fois
passations_detectees = {f: positions for f, positions in cartographie_passations.items() if len(positions) > 1}

if not passations_detectees:
    st.info("✨ Aucune passation détectée : Toutes les figures du thème occupent un espace unique.")
else:
    for fig_nom, maisons in passations_detectees.items():
        chemin_visuel = " ➔ ".join([f"**M{m}**" for m in maisons])
        with st.expander(f"🔄 Passation de [{fig_nom}] : {chemin_visuel}", expanded=False):
            st.markdown(f"La figure **{fig_nom}** se déplace à travers le thème. Voici les impacts de sa migration :")
            for m_dest in maisons:
                st.markdown(f"*   **Impact en M{m_dest}** ({MAISONS_RAMROU[m_dest]['nom']}) : {INTERPRETATIONS_PASSATIONS[m_dest]}")

st.markdown("---")

# ==============================================================================
# 6. ANALYSE DES COGNITIONS ET COPULATIONS MAGISTRALES (M9 À M16)
# ==============================================================================
st.header("🧬 ANALYSE DES COPULATIONS ET ENGENDRÈMENTS (M9 À M16)")

# Extraction exclusive des figures présentes dans le cercle des décisions (M9 à M16)
figures_m9_m16 = [theme_actuel[m] for m in range(9, 17)]
trouve_copulation = False

# --- RÈGLE D'OR : VÉRIFICATION DU CONFLIT MAJEUR IBRAHIMA / ASSANE ---
conflit_actif = False
for i in range(len(figures_m9_m16)):
    for j in range(i + 1, len(figures_m9_m16)):
        f1, f2 = figures_m9_m16[i], figures_m9_m16[j]
        if (f1 == "Ibrahima" and f2 == "Assane") or (f1 == "Assane" and f2 == "Ibrahima"):
            conflit_actif = True

if conflit_actif:
    st.error("💥 **CONFLIT DIRECT MAJEUR DETECTÉ (Règle des Maîtres) :** "
             "La présence simultanée d'**Ibrahima** et d'**Assane** au sein des maisons décisionnelles (M9 à M16) "
             "bloque les aspects bénéfiques et n'engendre que des discussions stériles, disputes acrimonieuses, "
             "divergences d'opinions et fâcheries sévères consécutives à une mésentente irréconciliable.")

# --- ANALYSE DES COMBINAISONS SPECIFIQUES DES CIBLES (70 RÈGLES) ---
for cible, regles in REGLES_COPULATIONS.items():
    correspondances_cible = []
    for i in range(len(figures_m9_m16)):
        for j in range(i + 1, len(figures_m9_m16)):
            f1, f2 = figures_m9_m16[i], figures_m9_m16[j]
            for r in regles:
                # Vérification de la présence du couple de parents (ordre indifférent)
                if (f1 == r["parents"][0] and f2 == r["parents"][1]) or (f1 == r["parents"][1] and f2 == r["parents"][0]):
                    if r["verdict"] not in [x[2] for x in correspondances_cible]:
                        correspondances_cible.append((f1, f2, r["verdict"]))

    if correspondances_cible:
        st.markdown(f"### ➔ Alignements actifs orientés vers l'énergie de **{cible}**")
        trouve_copulation = True
        for f1, f2, verd in correspondances_cible:
            st.success(f"🤝 Copulation Active : **{f1}** + **{f2}** ➔ **{verd}**")

if not trouve_copulation:
    st.info("💡 Aucun des couples spécifiques des 70 règles n'est actif dans le secteur M9-M16 de ce tirage.")

st.markdown("---")

# ==============================================================================
# 7. PHARMACÉE SPIRITUELLE & PROTOCOLES THÉURGIQUES COMPLETS (NASSI)
# ==============================================================================
st.header("🌿 CABINET THÉURGIQUE : PHARMACÉE ET PROTOCOLES DE REMÈDES")
st.write("Sélection automatique des ordonnances, des Psaumes d'activation, des versets bibliques piliers, des prières de Salomon et du mode opératoire précis pour la confection du Nassi.")

# Extraction des figures uniques issues du tirage pour éviter les redondances d'affichage
figures_uniques_tirage = set(theme_actuel.values())

for fig in sorted(figures_uniques_tirage):
    infos = PROPRIETES_FIGURES[fig]
    with st.expander(f"✨ Ordonnance Divine et Théurgique : {fig} (Figure {infos['num']} — Élément : {infos['element']})", expanded=False):
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"📖 **Psaume d'Activation Vibratoire :** \n\n> *{infos['psaume']}*")
            st.markdown(f"📜 **Verset Biblique Pilier Ancestral :** \n\n> *{infos['verset']}*")
            st.markdown(f"👑 **Prière de Salomon Dédiée :** \n\n{infos['salomon']}")
            
        with col2:
            st.info(f"🧪 **Protocole de Confection du Nassi & Comment procéder :** \n\n{infos['nassi']}")
            
        st.caption("⚠️ **Règle Théurgique Impérative :** Lors de l'onction, de l'aspersion ou de l'utilisation du Nassi, "
                   "le théurgiste ou le consultant doit obligatoirement s'orienter vers la direction cardinale de l'élément de la figure "
                   "pour réciter le Psaume et le Verset.")
