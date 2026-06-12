import streamlit as st

# ==============================================================================
# CONFIGURATION DE L'APPLICATION
# ==============================================================================
st.set_page_config(
    page_title="Oracle Ramrou — Théurgie, Passations & Remèdes", 
    page_icon="🔮", 
    layout="wide"
)

st.title("🔮 Oracle Ramrou — Cabinet Théurgique & Grand Grimoire")
st.markdown("Analyse automatique des passations, des 70 règles d'engendrement, et protocole de remèdes spirituels (Psaumes, Nassi, Versets & Prières de Salomon).")

# ==============================================================================
# 1. BASE DE DONNÉES GÉOMANTIQUE ET PROTOCOLES THÉURGIQUES DES 16 FIGURES
# ==============================================================================
PROPRIETES_FIGURES = {
    "Youssouf": {
        "num": 1, "nature": "Diable Mauvais", "groupe": "Mobiles", "element": "Feu (Est)",
        "psaume": "Psaume 109 (Contre les calomnies et les ennemis acharnés)",
        "verset": "Genèse 39:2 — 'L'Éternel fut avec Joseph, et la prospérité l'accompagna...'",
        "salomon": "Prière pour briser les complots secrets et restaurer la dignité.",
        "nassi": "Écrire la figure 111 fois sur une tablette en bois, laver avec de l'eau de puits, y ajouter du safran et du parfum de rose. À utiliser en bain pendant 7 jours avant le lever du soleil."
    },
    "Adama": {
        "num": 2, "nature": "Diable Bon", "groupe": "Sortants", "element": "Feu (Est)",
        "psaume": "Psaume 121 (Pour la protection dans les déplacements)",
        "verset": "Genèse 2:7 — 'L'Éternel Dieu forma l'homme de la poussière de la terre...'",
        "salomon": "Prière d'ancrage et d'ouverture des portes matérielles bloquées.",
        "nassi": "Tracer la figure 45 fois. Recueillir l'eau dans un récipient propre, ajouter une poignée de sel béni. S'en asperger et laver le seuil de la porte pour attirer les opportunités."
    },
    "Mahdy": {
        "num": 3, "nature": "Diable Bon", "groupe": "Rentrants", "element": "Air (Ouest)",
        "psaume": "Psaume 23 (Pour l'abondance et la paix de l'esprit)",
        "verset": "Jérémie 29:11 — 'Car je connais les projets que j'ai formés sur vous...'",
        "salomon": "Prière pour l'attraction de la grâce et l'accomplissement des promesses.",
        "nassi": "Écrire la figure 66 fois avec de l'eau de rose et du musc. Diviser le Nassi en deux : boire une gorgée chaque matin à jeun et utiliser le reste pour l'onction du visage."
    },
    "Idriss": {
        "num": 4, "nature": "Diable Bon", "groupe": "Fixes", "element": "Eau (Nord)",
        "psaume": "Psaume 119:9-16 (Pour la sagesse et l'illumination spirituelle)",
        "verset": "Hébreux 11:5 — 'C'est par la foi qu'Énoch fut enlevé pour qu'il ne vît point la mort...'",
        "salomon": "Prière de Salomon pour l'acquisition d'une intelligence supérieure et le discernement.",
        "nassi": "Écrire la figure 360 fois (nombre de l'élévation). Diluer dans de l'eau de pluie collectée un jeudi. Utiliser cette eau pour oindre la tête et le front pendant les heures de prière ou de méditation."
    },
    "Ibrahima": {
        "num": 5, "nature": "Humain Bon", "groupe": "Mobiles", "element": "Eau (Nord)",
        "psaume": "Psaume 112 (Bénédiction sur la postérité et la maison)",
        "verset": "Genèse 12:2 — 'Je ferai de toi une grande nation, et je te bénirai...'",
        "salomon": "Prière d'alliance sacrée, de fécondité et d'extension des limites.",
        "nassi": "Écrire la figure 72 fois. Infuser l'écriture avec des feuilles de menthe fraîche. Boire en famille ou asperger la chambre des enfants pour la paix et la protection du foyer."
    },
    "Inssa": {
        "num": 6, "nature": "Humain Mauvais", "groupe": "Sortants", "element": "Eau (Nord)",
        "psaume": "Psaume 6 (Pour la guérison des maladies et l'apaisement des douleurs)",
        "verset": "Ésaïe 53:5 — 'Mais il était blessé pour nos péchés, brisé pour nos iniquités...'",
        "salomon": "Prière de délivrance contre les afflictions physiques et psychologiques.",
        "nassi": "Écrire la figure 99 fois à l'encre noire traditionnelle (Sami). Laver la tablette avec une décoction de feuilles de neem ou de verveine. Laver le corps du malade avec ce liquide."
    },
    "Omar": {
        "num": 7, "nature": "Diable Mauvais", "groupe": "Fixes", "element": "Air (Ouest)",
        "psaume": "Psaume 35 (Contre les adversaires injustes et les litiges)",
        "verset": "Proverbes 31:10 — 'Qui peut trouver une femme vertueuse ? Elle a bien plus de valeur que les perles.'",
        "salomon": "Prière pour pacifier les relations conjugales et exposer les comploteurs.",
        "nassi": "Tracer la figure 28 fois. Diluer dans de l'eau de source. Ajouter sept gouttes de parfum sans alcool. Utiliser en aspersion dans les coins de la maison pour chasser les ondes de discorde."
    },
    "Ayoub": {
        "num": 8, "nature": "Diable Mauvais", "groupe": "Rentrants", "element": "Terre (Sud)",
        "psaume": "Psaume 88 (Prière dans la détresse profonde et la stagnation)",
        "verset": "Job 19:25 — 'Mais je sais que mon rédempteur est vivant, et qu'il se lèvera le dernier...'",
        "salomon": "Prière de restauration des biens perdus et de brisement du décret de deuil.",
        "nassi": "Écrire la figure 88 fois sur du papier parchemin ou une tablette. Dissoudre dans de l'eau tiède mélangée à un peu de miel pur. Se laver entièrement un samedi soir pour rompre la lourdeur karmique."
    },
    "Allahou": {
        "num": 9, "nature": "Humain Mauvais", "groupe": "Sortants", "element": "Feu (Est)",
        "psaume": "Psaume 91 (La forteresse divine et la protection absolue)",
        "verset": "Exode 20:2 — 'Je suis l'Éternel, ton Dieu, qui t'ai fait sortir du pays d'Égypte...'",
        "salomon": "Invocation de la Souveraineté Divine pour annuler les rituels inverses.",
        "nassi": "Écrire la figure 114 fois. Utiliser de l'eau bénite ou de l'eau de puits non polluée. Diviser en flacons : un pour boire un verre chaque vendredi, un autre pour purifier le lieu de travail."
    },
    "Souleymane": {
        "num": 10, "nature": "Humain Bon", "groupe": "Fixes", "element": "Terre (Sud)",
        "psaume": "Psaume 72 (Pour l'élévation, la justice et la royauté)",
        "verset": "1 Rois 3:12 — 'Voici, j'agirai selon ta parole. Je te donnerai un cœur sage...'",
        "salomon": "La Grande Prière de Sagesse et d'Héritage Royal de Salomon.",
        "nassi": "Écrire la figure 110 fois. Utiliser une eau parfumée au bois de santal. S'en oindre les mains et les pieds avant tout rendez-vous d'affaires important ou démarche administrative majeure."
    },
    "Aliou": {
        "num": 11, "nature": "Humain Mauvais", "groupe": "Fixes", "element": "Air (Ouest)",
        "psaume": "Psaume 144 (Pour la victoire dans les combats spirituels)",
        "verset": "Éphésiens 6:11 — 'Revêtez-vous de toutes les armes de Dieu, afin de pouvoir tenir ferme...'",
        "salomon": "Prière du Bouclier de Salomon contre les attaques frontales et les forces armées.",
        "nassi": "Écrire la figure 63 fois. Ajouter de la poudre de camphre à l'eau de lavage. Se laver le corps un mardi pour acquérir le courage et repousser les agressions physiques ou subtiles."
    },
    "Nouhou": {
        "num": 12, "nature": "Humain Bon", "groupe": "Rentrants", "element": "Terre (Sud)",
        "psaume": "Psaume 29 (La voix de l'Éternel sur les grandes eaux)",
        "verset": "Genèse 6:8 — 'Mais Noé trouva grâce aux yeux de l'Éternel.'",
        "salomon": "Prière de préservation au milieu des tempêtes de la vie et des complots de sorcellerie.",
        "nassi": "Écrire la figure 77 fois. Laver à l'eau de mer ou à défaut, ajouter du gros sel marin. Laver le sol de votre concession ou maison pour dissoudre toute charge de magie noire enfouie."
    },
    "Assane": {
        "num": 13, "nature": "Diable Mauvais", "groupe": "Sortants", "element": "Eau (Nord)",
        "psaume": "Psaume 3 (Contre l'humiliation et le grand nombre d'ennemis)",
        "verset": "Psaume 3:3 — 'Mais toi, ô Éternel ! tu es mon bouclier, tu es ma gloire...'",
        "salomon": "Prière pour transmuter la honte publique en victoire éclatante.",
        "nassi": "Écrire la figure 55 fois à l'encre rouge de safran. Diluer dans de l'eau claire, ajouter des feuilles de laurier. Se laver pendant 3 jours consécutifs pour purifier l'aura de l'opprobre."
    },
    "Younouss": {
        "num": 14, "nature": "Diable Bon", "groupe": "Mobiles", "element": "Terre (Sud)",
        "psaume": "Psaume 4 (Pour la délivrance des blocages financiers)",
        "verset": "Jonas 2:10 — 'L'Éternel parla au poisson, et le poisson vomit Jonas sur la terre...'",
        "salomon": "Prière pour sortir des situations de gouffre financier et de dettes.",
        "nassi": "Écrire la figure 40 fois (les 40 jours de Jonas). Utiliser de l'eau de source. Y ajouter une pièce de monnaie propre pendant 24h, puis retirer la pièce (à donner en aumône) et utiliser le Nassi en friction des mains."
    },
    "Ousmane": {
        "num": 15, "nature": "Humain Bon", "groupe": "Rentrants", "element": "Air (Ouest)",
        "psaume": "Psaume 119:105 — 'Ta parole est une lampe à mes pieds, Et une lumière sur mon sentier.'",
        "verset": "Actes 2:4 — 'Et ils furent tous remplis du Saint-Esprit, et se mirent à parler...'",
        "salomon": "Prière d'intercession prophétique et de haute connexion théurgique.",
        "nassi": "Écrire la figure 19 fois. Infuser l'écriture avec de l'encens de pure qualité (Oliban). Boire un verre de ce Nassi avant les séances d'études spirituelles ou d'interprétation pour ouvrir le troisième œil."
    },
    "Moussa": {
        "num": 16, "nature": "Humain Mauvais", "groupe": "Fixes", "element": "Feu (Est)",
        "psaume": "Psaume 68 (Que Dieu se lève, et que ses ennemis se dispersent !)",
        "verset": "Exode 14:13 — 'Moïse répondit au peuple : Ne craignez rien, restez en place...'",
        "salomon": "Prière d'ouverture de la Mer Rouge (Brise les barrières ultimes de la vie).",
        "nassi": "Écrire la figure 16 fois (la complétude). Diluer dans de l'eau de source prélevée à l'aube. Utiliser pour nettoyer entièrement le seuil de la maison, le commerce, ou à employer en grand bain de libération."
    }
}

MAISONS_RAMROU = {
    1: {"nom": "M1 (Maison de l'Âme)", "desc": "L'être physique, la personnalité, l'état actuel."},
    2: {"nom": "M2 (Maison de la Chance)", "desc": "Les finances, les gains immédiats, l'argent."},
    3: {"nom": "M3 (Maison des Mères)", "desc": "L'entourage proche, les frères, les démarches courtes."},
    4: {"nom": "M4 (Maison des Pères)", "desc": "Le foyer, le patrimoine, la fin de l'affaire."},
    5: {"nom": "M5 (Maison des Enfants)", "desc": "Les enfants, les amours, les désirs, les grossesses."},
    6: {"nom": "M6 (Maison des Malades)", "desc": "La santé, les obstacles, les maladies, le travail physique."},
    7: {"nom": "M7 (Maison du Mariage)", "desc": "Le conjoint, l'associé, les adversaires déclarés."},
    8: {"nom": "M8 (Maison du Changement)", "desc": "L'extérieur, l'étranger, la mort, les transformations profondes."},
    9: {"nom": "M9 (Maison de Dieu)", "desc": "La spiritualité, les voyages, la religion, la recherche."},
    10: {"nom": "M10 (Maison des Rois)", "desc": "Le pouvoir, l'autorité, la profession, la réussite sociale."},
    11: {"nom": "M11 (Maison de l'Espoir)", "desc": "Les amis, les espoirs, les aides et appuis."},
    12: {"nom": "M12 (Maison des Ennemis)", "desc": "Les ennemis cachés, les obstacles occultes, les pièges."},
    13: {"nom": "M13 (Maison du Sexe / Chambre)", "desc": "L'intimité du foyer, le présent immédiat, le lit conjugal."},
    14: {"nom": "M14 (Maison des Fortunes)", "desc": "Les gains futurs, l'argent à venir, le commerce."},
    15: {"nom": "M15 (Maison de l'Espace)", "desc": "La clarté publique, les rumeurs, l'ambiance générale."},
    16: {"nom": "M16 (Maison de Finition)", "desc": "La conclusion ultime et irrévocable du thème."}
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

REGLES_COPULATIONS = {
    "Moussa": [
        {"parents": ("Youssouf", "Youssouf"), "verdict": "Trahison collective — les gens se regroupent en secret pour te trahir."},
        {"parents": ("Adama", "Adama"), "verdict": "Indique la formation ou la présence d'un groupe de jeunes."},
        {"parents": ("Mahdy", "Mahdy"), "verdict": "Convergence positive — indique un groupe de personnes réunies pour avancer ensemble sur un bon projet."},
        {"parents": ("Idriss", "Idriss"), "verdict": "Urbanisme/Communauté — indique un ensemble de maisons, un village ou une ville entière."},
        {"parents": ("Ibrahima", "Ibrahima"), "verdict": "Indique un groupe d'enfants."},
        {"parents": ("Inssa", "Inssa"), "verdict": "Épreuve collective — indique une souffrance ou un calvaire généralisé pour tout le monde."},
        {"parents": ("Omar", "Omar"), "verdict": "Indique une assemblée ou un groupe de femmes."},
        {"parents": ("Ayoub", "Ayoub"), "verdict": "Affliction — indique un rassemblement ou un groupe de personnes pour des funérailles."},
        {"parents": ("Allahou", "Allahou"), "verdict": "Indique la présence d'un groupe de jumeaux."},
        {"parents": ("Souleymane", "Souleymane"), "verdict": "Haute sphère — indique un groupe de chefs ou de patrons en réunion, unis pour un seul et unique but."},
        {"parents": ("Aliou", "Aliou"), "verdict": "Force armée — indique un groupe de soldats, de militaires ou de guerriers."},
        {"parents": ("Nouhou", "Nouhou"), "verdict": "Sorcellerie — indique un groupe de méchants, de sorciers ou de féticheurs unis dans l'intention de faire du mal."},
        {"parents": ("Assane", "Assane"), "verdict": "Opprobre public — indique un groupe de personnes qui subiront la honte ensemble."},
        {"parents": ("Younouss", "Younouss"), "verdict": "Prospérité locale — indique la richesse globale du pays, du village, de la ville ou du foyer."},
        {"parents": ("Ousmane", "Ousmane"), "verdict": "Lignée spirituelle — indique un rassemblement ou un groupe de marabouts."},
        {"parents": ("Moussa", "Moussa"), "verdict": "Harmonie parfaite — indique un groupe de personnes au sein duquel règnent l'entente cordiale et la paix absolue."}
    ],
    "Ousmane": [
        {"parents": ("Youssouf", "Adama"), "verdict": "Secret spirituel — indique la présence d'un marabout caché."},
        {"parents": ("Mahdy", "Ayoub"), "verdict": "Évolution radieuse — indique le bonheur, l'accroissement continu et l'avancement social."},
        {"parents": ("Inssa", "Ibrahima"), "verdict": "Problème de santé — indique un enfant malade, une affection sur la peau ou une maladie visible (non cachée)."},
        {"parents": ("Omar", "Ayoub"), "verdict": "Conflit intellectuel — indique que des marabouts ou des lettrés vont s'affronter."},
        {"parents": ("Allahou", "Souleymane"), "verdict": "Sagesse authentique — indique un bon marabout, sage et intègre, qui ne fait de mal à personne."},
        {"parents": ("Aliou", "Nouhou"), "verdict": "Imposture — indique un faux marabout, un trompeur, un charlatan et un menteur."},
        {"parents": ("Younouss", "Assane"), "verdict": "Énergie de la chasse — indique un chasseur."},
        {"parents": ("Moussa", "Ousmane"), "verdict": "Affluence commerciale — indique une grande foule ou une forte activité au marché."}
    ],
    "Younouss": [
        {"parents": ("Youssouf", "Aliou"), "verdict": "Richesse externe — indique explicitement la fortune ou la richesse d'une autre personne."},
        {"parents": ("Adama", "Nouhou"), "verdict": "Grâce divine — indique de façon certaine que Dieu te fera don de la richesse."},
        {"parents": ("Mahdy", "Allahou"), "verdict": "Théurgie financière — indique que des prières ou un travail spirituel intense ont été accomplis pour attirer la richesse."},
        {"parents": ("Idriss", "Souleymane"), "verdict": "Patrimoine proche — indique la richesse du foyer familial ou de la famille immédiate."},
        {"parents": ("Inssa", "Ayoub"), "verdict": "Ruine — indique une perte sèche ou un grand gaspillage d'argent."},
        {"parents": ("Ibrahima", "Omar"), "verdict": "Opulence sans descendance — indique une femme qui n'a pas d'enfant mais qui est immensément riche."},
        {"parents": ("Younouss", "Moussa"), "verdict": "Prospérité collective — indique la richesse du pays, du association ou du village."}
    ],
    "Assane": [
        {"parents": ("Youssouf", "Nouhou"), "verdict": "Amertume — indique le regret profond face à une situation."},
        {"parents": ("Adama", "Aliou"), "verdict": "Heureux présage — indique l'arrivée imminente d'une grossesse de jumeaux."},
        {"parents": ("Mahdy", "Souleymane"), "verdict": "Répétition cyclique — indique de façon formelle que la chose ou l'affaire se répétera."},
        {"parents": ("Idriss", "Allahou"), "verdict": "Menace humaine — indique les agissements ou la présence d'un jeune homme très méchant."},
        {"parents": ("Ibrahima", "Ayoub"), "verdict": "Retour cyclique — indique avec assurance que la chose ou la situation reviendra."},
        {"parents": ("Inssa", "Omar"), "verdict": "Trouble organique — indique la manifestation de maux de ventre cuisants."},
        {"parents": ("Ousmane", "Younouss"), "verdict": "Lutte vaine — indique des gens qui tentent par tous les moyens d'empêcher le tonnerre de faire pleuvoir."},
        {"parents": ("Moussa", "Assane"), "verdict": "Flux financier — indique une rentrée d'argent particulièrement rapide."}
    ],
    "Nouhou": [
        {"parents": ("Youssouf", "Assane"), "verdict": "Hostilité — indique une méchanceté ou une rancœur causée à cause d'un enfant."},
        {"parents": ("Adama", "Younouss"), "verdict": "Discorde matérielle — indique une méchanceté sous-jacente liée à une question d'héritage."},
        {"parents": ("Ibrahima", "Allahou"), "verdict": "Hostilité familiale — indique une méchanceté manifestée pour des motifs liés aux enfants."},
        {"parents": ("Omar", "Mahdy"), "verdict": "Rivalité amoureuse — indique une méchanceté déclenchée à cause d'une femme."},
        {"parents": ("Inssa", "Souleymane"), "verdict": "Abus de pouvoir — indique la méchanceté tyrannique provenant d'un chef ou d'un dirigeant."},
        {"parents": ("Ayoub", "Idriss"), "verdict": "Poison intime — indique une méchanceté sévissant directement au sein de la famille ou du foyer familial."},
        {"parents": ("Aliou", "Ousmane"), "verdict": "Occultisme noir — indique une méchanceté occulte orchestrée par un marabout ou un praticien géomancien."},
        {"parents": ("Moussa", "Nouhou"), "verdict": "Complot de groupe — indique une méchanceté flagrante perpétrée par un groupe de personnes liguées."}
    ],
    "Aliou": [
        {"parents": ("Youssouf", "Younouss"), "verdict": "Opulence en vue — indique une femme animée d'un très bon espoir d'acquérir la richesse."},
        {"parents": ("Adama", "Assane"), "verdict": "Obligation rituelle — le thème impose impérativement de faire un sacrifice de couleur rouge pour l'affaire demandée."},
        {"parents": ("Mahdy", "Ayoub"), "verdict": "Stérilité/Entrave — indique une grande difficulté pour concevoir, matérialisant un blocage net."},
        {"parents": ("Idriss", "Omar"), "verdict": "Cataclysme aérien — indique le déchaînement d'une tempête ou d'un grand vent violent causant des dégâts majeurs."},
        {"parents": ("Ibrahima", "Souleymane"), "verdict": "Conception sacrée — annonce et confirme de façon indubitable une grossesse."},
        {"parents": ("Nouhou", "Ousmane"), "verdict": "Élévation sociale — indique l'avènement certain de la grandeur et de l'honneur."},
        {"parents": ("Allahou", "Inssa"), "verdict": "Épreuve critique — indique la confrontation imminente avec une très grave difficulté."},
        {"parents": ("Moussa", "Aliou"), "verdict": "Alignement martial — indique un rassemblement ou un groupe de guerriers, de soldats ou d'élèves."}
    ],
    "Souleymane": [
        {"parents": ("Youssouf", "Omar"), "verdict": "Une femme très riche."},
        {"parents": ("Adama", "Ayoub"), "verdict": "La chance est complètement fermée."},
        {"parents": ("Mahdy", "Idriss"), "verdict": "La chose demandée est cachée ou il n’aura pas de solution sauf sacrifice rigoureux."},
        {"parents": ("Idriss", "Younouss"), "verdict": "Une grosse somme d'argent cachée."},
        {"parents": ("Nouhou", "Inssa"), "verdict": "Un chef ou une autorité méchante et impitoyable."},
        {"parents": ("Aliou", "Ibrahima"), "verdict": "Un enfant en devenir qui sera un très grand chef."},
        {"parents": ("Ousmane", "Allahou"), "verdict": "Un chef correct, juste et bon."},
        {"parents": ("Moussa", "Souleymane"), "verdict": "Une réunion imminente de grands chefs ou de présidents."}
    ],
    "Allahou": [
        {"parents": ("Youssouf", "Ayoub"), "verdict": "Un aveugle : la chose demandée n'a absolument pas de solution."},
        {"parents": ("Adama", "Omar"), "verdict": "Une prière intense pour concevoir et avoir des enfants."},
        {"parents": ("Mahdy", "Younouss"), "verdict": "Une prière ou un travail spirituel profond pour obtenir la richesse."},
        {"parents": ("Idriss", "Idriss"), "verdict": "Des prières collectives ou rituels pour obtenir la pluie."},
        {"parents": ("Souleymane", "Ousmane"), "verdict": "Une maladie ou une affection localisée au niveau de l'appareil sexuel."},
        {"parents": ("Aliou", "Inssa"), "verdict": "Une fermeture hermétique de la chose demandée."},
        {"parents": ("Nouhou", "Ibrahima"), "verdict": "Une personne heureuse et comblée qui remercie chaleureusement Dieu."},
        {"parents": ("Moussa", "Allahou"), "verdict": "Des voyageurs ou des gens actuellement en route."}
    ]
}

# ==============================================================================
# 2. INTERFACE DE SAISIE DES MAISONS (BARRE LATÉRALE)
# ==============================================================================
st.sidebar.header("📥 Saisie des 16 Maisons Géomantiques")
liste_choix = list(PROPRIETES_FIGURES.keys())
theme_actuel = {}

for m in range(1, 17):
    theme_actuel[m] = st.sidebar.selectbox(
        f"{MAISONS_RAMROU[m]['nom']}",
        liste_choix,
        index=(m - 1) % len(liste_choix),
        key=f"m_{m}"
    )

# Visualisation rapide du thème entré
st.subheader("📊 Grille Récapitulative du Thème Saisi")
cols_grille = st.columns(4)
for idx, m_id in enumerate(range(1, 17)):
    col = cols_grille[idx % 4]
    with col:
        st.markdown(f"**M{m_id}** : `{theme_actuel[m_id]}`")

st.markdown("---")

# ==============================================================================
# 3. LE MOTEUR DE PASSATION DES FIGURES
# ==============================================================================
st.header("🔄 ANALYSE DES PASSATIONS (MIGRATIONS)")
cartographie_passations = {}
for m_id, fig_nom in theme_actuel.items():
    if fig_nom not in cartographie_passations:
        cartographie_passations[fig_nom] = []
    cartographie_passations[fig_nom].append(m_id)

passations_detectees = {f: positions for f, positions in cartographie_passations.items() if len(positions) > 1}

if not passations_detectees:
    st.info("✨ Aucune passation détectée : Toutes les figures du thème sont uniques.")
else:
    for fig_nom, maisons in passations_detectees.items():
        chemin_visuel = " ➔ ".join([f"**M{m}**" for m in maisons])
        with st.expander(f"🔄 Passation de {fig_nom} : {chemin_visuel}", expanded=False):
            st.markdown(f"La figure **{fig_nom}** migre à travers le thème. Voici ses points d'impact :")
            for m_dest in maisons:
                st.markdown(f"*   **Arrivée en M{m_dest}** ({MAISONS_RAMROU[m_dest]['nom']}) : {INTERPRETATIONS_PASSATIONS[m_dest]}")

st.markdown("---")

# ==============================================================================
# 4. RÉSULTATS DES ENGENDRÈMENTS (M9 À M16)
# ==============================================================================
st.header("🧬 RÉSULTATS DES ENGENDRÈMENTS ET COPULATIONS (M9 À M16)")
figures_m9_m16 = [theme_actuel[m] for m in range(9, 17)]
trouve_copulation = False

# Vérification du conflit Ibrahima + Assane
conflit_actif = False
for i in range(len(figures_m9_m16)):
    for j in range(i + 1, len(figures_m9_m16)):
        f1, f2 = figures_m9_m16[i], figures_m9_m16[j]
        if (f1 == "Ibrahima" and f2 == "Assane") or (f1 == "Assane" and f2 == "Ibrahima"):
            conflit_actif = True

if conflit_actif:
    st.error("💥 **CONFLIT DIRECT MAJEUR DETECTÉ :** "
             "La présence simultanée d'**Ibrahima** et d'**Assane** dans les maisons M9 à M16 "
             "n'engendre que des discussions, disputes, divergences et fâcheries consécutives à une mésentente.")

# Parcours des règles d'engendrement
for cible, regles in REGLES_COPULATIONS.items():
    correspondances_cible = []
    for i in range(len(figures_m9_m16)):
        for j in range(i + 1, len(figures_m9_m16)):
            f1, f2 = figures_m9_m16[i], figures_m9_m16[j]
            for r in regles:
                if (f1 == r["parents"][0] and f2 == r["parents"][1]) or (f1 == r["parents"][1] and f2 == r["parents"][0]):
                    if r["verdict"] not in [x[2] for x in correspondances_cible]:
                        correspondances_cible.append((f1, f2, r["verdict"]))

    if correspondances_cible:
        st.markdown(f"### ➔ Alignements actifs menant à **{cible}**")
        trouve_copulation = True
        for f1, f2, verd in correspondances_cible:
            st.success(f"🤝 **{f1}** + **{f2}** : {verd}")

if not trouve_copulation:
    st.info("💡 Aucune des 70 combinaisons spécifiques n'est active avec les figures M9 à M16 actuelles.")

st.markdown("---")

# ==============================================================================
# 5. DISPOSITIF THÉURGIQUE ET PHARMACÉE SPIRITUELLE (NOUVEAU)
# ==============================================================================
st.header("🌿 PROTOCOLE DE REMÈDES SPIRITUELS ET THÉURGIQUES")
st.write("Retrouve ci-dessous les psaumes, versets bibliques, prières de Salomon ainsi que la préparation exacte du Nassi (eau de dissolution géomantique) pour chaque figure présente dans ton thème.")

# Liste des figures uniques actuellement présentes dans le tirage pour l'ordonnance spirituelle
figures_presentes = set(theme_actuel.values())

for fig in sorted(figures_presentes):
    infos = PROPRIETES_FIGURES[fig]
    with st.expander(f"✨ Ordonnance Spirituelle : {fig} (Numéro {infos['num']} — {infos['element']})", expanded=False):
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"📖 **Psaume d'activation :** \n*{infos['psaume']}*")
            st.markdown(f"📜 **Verset Biblique Pilier :** \n*{infos['verset']}*")
            st.markdown(f"👑 **Prière de Salomon :** \n{infos['salomon']}")
            
        with col2:
            st.info(f"🧪 **Préparation du Nassi & Comment procéder :** \n\n{infos['nassi']}")
            
        st.caption("📜 Règle d'usage : Les psaumes et les versets doivent être récités face à la direction de l'élément de la figure pendant l'utilisation du Nassi.")
