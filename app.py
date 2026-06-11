import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Système Théurgique Géomancie Rectifiée", page_icon="🔮", layout="wide")

# ==============================================================================
# ACCÈS SÉCURISÉS
# ==============================================================================
ID_SECRET = "theurge2026"
MDP_SECRET = "Salomon777"

# ==============================================================================
# BASE DE DONNÉES STRICTE : 16 FIGURES AU REPOS ET LEURS ATTRIBUTS TRADITIONNELS
# ==============================================================================
DATA = {
    "Youssouf (Dianfa Almami)": {
        "ref": "Youssouf (Dianfa Almami)", "code": (1, 2, 1, 1), "nature": "Bénéfique", "element": "Feu", "direction": "Est",
        "maison_repos": 1, "nom_maison_repos": "M1 (Demandeur / Esprit-Âme)", "plante": "Balança",
        "txt": "Maison du demandeur, de son état physique, moral, de son âme et de sa conscience primordiale.",
        "psaume": "Psaume 20", "nb_ecriture": 7, "verset": "Verset 5", 
        "texte_biblique": "Qu'il te donne ce que ton cœur désire, et qu'il accomplisse tous tes desseins !",
        "vibratoire": "Émet un rayonnement doré de type solaire qui restructure l'aura, dissipe les miasmes du doute et aligne le corps éthérique.",
        "avantages": "Restauration immédiate de l'autorité intérieure, clarté mentale absolue face aux choix de vie.",
        "huile": "Laurier Noble (Victoire et clarté spirituelle)", 
        "aromatiques": "Feuilles de Laurier sauce, Menthe poivrée fraîche, Safran pur en filaments",
        "zikr": "Ya Wahhab (Ô Donateur Suprême) — 14 fois + Nom Salomonique : EHIEH ASHER EHIEH",
        "priere_salomonique": "Par la puissance de la Couronne Suprême et le Nom Ineffable EHIEH ASHER EHIEH, j'invoque Ton rayonnement sur mon âme. Brise les verrous de mon esprit, enflamme mon aura de Ta lumière inextinguible et accorde-moi la victoire sur mes propres ombres. Que Ta grâce manifeste les désirs purs de mon cœur et que mes desseins s'accomplissent selon Ton ordre universel. Amen.",
        "mots_application": "Que mon âme soit purifiée et que les intentions de ce thème reçoivent la clarté. Amen.", "moment": "Matin au lever"
    },
    "Adam (Adama)": {
        "ref": "Adam (Adama)", "code": (1, 1, 1, 1), "nature": "Bénéfique", "element": "Feu", "direction": "Est",
        "maison_repos": 2, "nom_maison_repos": "M2 (Biens / Flux financiers)", "plante": "Sana",
        "txt": "Maison des biens, des finances, de la chance matérielle et des flux énergétiques entrants.",
        "psaume": "Psaume 8", "nb_ecriture": 8, "verset": "Verset 6", 
        "texte_biblique": "Tu lui as donné l'empire sur les œuvres de tes mains, tu as tout mis sous ses pieds.",
        "vibratoire": "Fréquence d'expansion terrestre accélérée. Brise la cristallisation astrale de la pauvreté.",
        "avantages": "Manifestation de ressources financières inattendues, déblocage des affaires commerciales.",
        "huile": "Cèdre de l'Atlas (Ancrage et prospérité royale)", 
        "aromatiques": "Basilic sacré (Tulsi), Romarin officinal, Curcuma en poudre pure",
        "zikr": "Ya Rafi'u (Ô Celui qui élève) — 351 fois + Nom Salomonique : ADONAI MELEKH",
        "priere_salomonique": "Ô Seigneur Souverain, Roi de la Terre, ADONAI MELEKH, Toi qui as façonné l'homme de poussière et d'esprit et l'as couronné de gloire. Par cette onction et ce bain de feu, confère-moi l'empire légitime sur la matière. Éloigne de mes mains le spectre du manque. Que l'abondance infinie se prosterne à mes pieds. Amen.",
        "mots_application": "Que l'abondance matérielle et l'élévation financière s'installent durablement. Amen.", "moment": "Matin"
    },
    "Mahdiou (Malejou)": {
        "ref": "Mahdiou (Malejou)", "code": (1, 1, 1, 2), "nature": "Neutre", "element": "Vent", "direction": "Sud",
        "maison_repos": 3, "nom_maison_repos": "M3 (Famille / Entourage proche)", "plante": "Cebé",
        "txt": "Maison de la famille, des voisins, des collègues, des communications et de l'entourage proche.",
        "psaume": "Psaume 4", "nb_ecriture": 3, "verset": "Verset 7", 
        "texte_biblique": "Fais lever sur nous la lumière de ta face, ô Éternel !",
        "vibratoire": "Onde de fluidisation éthérique. Elle balaye les énergies stagnantes de la médisance.",
        "avantages": "Pacification des tensions de voisinage ou de bureau, harmonie relationnelle.",
        "huile": "Orange Douce (Harmonie et joie relationnelle)", 
        "aromatiques": "Zestes d'Orange douce, Menthe douce en feuilles, Écorce de Cannelle grossière",
        "zikr": "Ya Nour (Ô Lumière) — 256 fois + Nom Salomonique : ELOHIM SABAOTH",
        "priere_salomonique": "Souverain des Armées Célestes, ELOHIM SABAOTH, Source éternelle de concorde et de lumière. Que la splendeur sacrée de Ta Face descende sur mon cercle social et familial. Purifie ma langue de toute parole amère, dissout la haine ou la jalousie secrète de mon entourage. Fais de moi un canal de paix. Amen.",
        "mots_application": "Que la concorde et la paix illuminent mes relations avec mon entourage. Amen.", "moment": "Matin"
    },
    "Idriss (Albayada)": {
        "ref": "Idriss (Albayada)", "code": (2, 2, 1, 2), "nature": "Bénéfique", "element": "Eau", "direction": "Nord",
        "maison_repos": 4, "nom_maison_repos": "M4 (Foyer / Patrimoine)", "plante": "Djou",
        "txt": "Maison du foyer, de la maison familiale, du patrimoine immobilier et de l'autorité parentale.",
        "psaume": "Psaume 112", "nb_ecriture": 4, "verset": "Verset 3", 
        "texte_biblique": "Il a dans sa maison bien-être et richesse, et sa justice subsiste à jamais.",
        "vibratoire": "Fréquence de cristallisation lunaire blanche très pure. Elle agit comme un bouclier d'argent.",
        "avantages": "Facilitation des transactions immobilières, ancrage de la paix sous le toit familial.",
        "huile": "Patchouli (Attraction terrestre et matérialisation)", 
        "aromatiques": "Bâtons de Cannelle concassés, Clous de Girofle entiers, Curcuma de Madagascar",
        "zikr": "Ya Razzaq (Ô Pourvoyeur) — 308 fois + Nom Salomonique : SHADDAI EL CHAI",
        "priere_salomonique": "Principe Vivant et Tout-Puissant, SHADDAI EL CHAI, Fondement inébranlable des siècles. J'invoque Ta bénédiction sur ma demeure et mon sang. Fais couler le fleuve du bien-être et de la richesse intarissable dans mon foyer. Que le vice en soit chassé et que Ta justice y règne éternellement. Amen.",
        "mots_application": "Que la stabilité, le bien-être et la richesse s'ancrent au cœur de mon foyer. Amen.", "moment": "Matin"
    },
    "Ibrahim (Târiki)": {
        "ref": "Ibrahim (Târiki)", "code": (1, 1, 2, 1), "nature": "Bénéfique", "element": "Eau", "direction": "Nord",
        "maison_repos": 5, "nom_maison_repos": "M5 (Enfants / Nouvelles)", "plante": "Djècala",
        "txt": "Maison des enfants, de la créativité, des plaisirs et des nouvelles ou messages entrants.",
        "psaume": "Psaume 100", "nb_ecriture": 5, "verset": "Verset 2", 
        "texte_biblique": "Servez l'Éternel avec joie, venez avec allégresse en sa présence !",
        "vibratoire": "Onde hautement joyeuse, pétillante et régénératrice. Elle dissout la mélancolie.",
        "avantages": "Arrivée de bonnes nouvelles inattendues, déblocage des situations liées aux enfants.",
        "huile": "Pamplemousse (Énergie positive et renouveau)", 
        "aromatiques": "Verveine odorante, Citronnelle en tiges fraîches, Pistils de Safran royal",
        "zikr": "Ya Latif (Ô Doux) — 129 fois + Nom Salomonique : YHVH SABAOTH",
        "priere_salomonique": "Seigneur Souverain de l'Allégresse, YHVH SABAOTH, dont la douceur s'étend sur toute créature. Permets que Ton parfum de joie pénètre mon temple corporel. Chasse la tristesse stérile. Fais lever sur ma vie des messages de triomphe et accorde la protection à ma lignée. Amen.",
        "mots_application": "Que les nouvelles qui me parviennent apportent la joie, la réussite et l'allégresse. Amen.", "moment": "Matin"
    },
    "Issa (Ngansa)": {
        "ref": "Issa (Ngansa)", "code": (2, 2, 2, 2), "nature": "Neutre à Mauvais", "element": "Eau", "direction": "Nord",
        "maison_repos": 6, "nom_maison_repos": "M6 (Maladies / Choses accomplies)", "plante": "Wingninga",
        "txt": "Maison de la maladie, des blocages corporels, de la servitude et des choses déjà accomplies.",
        "psaume": "Psaume 51", "nb_ecriture": 1, "verset": "Verset 12", 
        "texte_biblique": "Ô Dieu ! crée en moi un cœur pur, renouvelle en moi un esprit bien disposé.",
        "vibratoire": "Vibration de transmutation radicale. Elle purge les poisons physiques et psychiques.",
        "avantages": "Soulagement des douleurs chroniques, expulsion des énergies négatives larvaires.",
        "huile": "Lavande Vraie (Purification absolue des corps subtils)", 
        "aromatiques": "Fleurs de Lavande séchées, Camomille matricaire, Poudre de Santal Blanc",
        "zikr": "Ya Chafi (Ô Guérisseur) — 391 fois + Nom Salomonique : ELOHIM GIBOR",
        "priere_salomonique": "Principe de Justice et Forteresse Inflexible, ELOHIM GIBOR, Toi qui sondes les reins et les cœurs. Lave mon corps et mon âme. Crée en moi un réceptacle immaculé. Par le pouvoir de Ton Autel, calcine toute maladie occulte et brise les chaînes de la servitude. Amen.",
        "mots_application": "Purifie mon être de toute négativité, entrave ou influence maladive cachée. Amen.", "moment": "Soir"
    },
    "Oumar (Lomara)": {
        "ref": "Oumar (Lomara)", "code": (2, 1, 2, 2), "nature": "Mauvais", "element": "Vent", "direction": "Sud",
        "maison_repos": 7, "nom_maison_repos": "M7 (Adversaires / Époux)", "plante": "Gababelé",
        "txt": "Maison des adversaires, des rivaux, des conflits déclarés, du mariage et des partenaires.",
        "psaume": "Psaume 35", "nb_ecriture": 7, "verset": "Verset 1", 
        "texte_biblique": "Éternel ! Attaque ceux qui m'attaquent, combats ceux qui me combattent !",
        "vibratoire": "Fréquence martienne de combat et de retour à l'envoyeur. Sature l'aura d'un bouclier de feu.",
        "avantages": "Gain de cause lors de litiges ou procès, neutralisation immédiate des rivaux ou jaloux.",
        "huile": "Cannelle Écorce (Feu purificateur de combat)", 
        "aromatiques": "Poivre noir en grains, Thym fort, Ortie piquante, Gingembre émincé",
        "zikr": "Ya Jabbar (Ô Contraignant) — 206 fois + Nom Salomonique : ELOHIM GIBOR",
        "priere_salomonique": "Juge Terrible des Oppresseurs, ELOHIM GIBOR, Puissance des vengeances légitimes. Tire Ton épée flamboyante et dresse Ton bouclier devant mes pas. Combat ceux qui cherchent ma ruine. Que la confusion s'abatte sur mes adversaires invisibles ou visibles. Amen.",
        "mots_application": "Que toute opposition, conflit ou rivalité se brise face à la justice supérieure. Amen.", "moment": "Soir"
    },
    "Ayoube (Mankoussi)": {
        "ref": "Ayoube (Mankoussi)", "code": (2, 2, 2, 1), "nature": "Mauvais", "element": "Terre", "direction": "Ouest",
        "maison_repos": 8, "nom_maison_repos": "M8 (Mort / Peurs / Patrimoine caché)", "plante": "Kronifin",
        "txt": "Maison de la mort, des angoisses profondes, des héritages, de la fatalité et du malheur.",
        "psaume": "Psaume 142", "nb_ecriture": 9, "verset": "Verset 8", 
        "texte_biblique": "Tire mon âme de sa prison, afin que je célèbre ton nom !",
        "vibratoire": "Onde de désintégration des énergies lourdes. Éradique les blocages psychologiques profonds.",
        "avantages": "Extraction immédiate des états de tristesse, déblocage des situations financières gelées.",
        "huile": "Cyprès de Provence (Libération et passage des blocages)", 
        "aromatiques": "Sauge officinale, Racine de Gingembre frais écrasée, Charbon de bois pur",
        "zikr": "Ya Moukhrij (Ô Celui qui fait sortir) — 201 fois + Nom Salomonique : AGLA",
        "priere_salomonique": "Souverain Éternel, Force immuable, AGLA, Toi qui as les clés des abîmes et de la vie. Entends mon cri du fond de la fosse. Brise les portes d'airain et les verrous de fer de ma prison existentielle. Tire mon âme de l'angoisse et fais-moi remonter vers la lumière. Amen.",
        "mots_application": "Je me libère des angoisses, des blocages et de toute forme d'enfermement. Amen.", "moment": "Soir"
    },
    "Allahou talla (Kalalaw)": {
        "ref": "Allahou talla (Kalalaw)", "code": (1, 2, 2, 1), "nature": "Bénéfique", "element": "Feu", "direction": "Est",
        "maison_repos": 9, "nom_maison_repos": "M9 (Voyages / Spiritualité / Mobilité)", "plante": "Sadjo ou aladjo",
        "txt": "Maison des déplacements, des voyages, de la spiritualité, de la recherche et du dynamisme.",
        "psaume": "Psaume 133", "nb_ecriture": 3, "verset": "Verset 1", 
        "texte_biblique": "Voici, qu'il est agréable, qu'il est doux pour des frères de demeurer ensemble !",
        "vibratoire": "Fréquence d'attraction par harmonisation supérieure. Ouvre les voies de la chance lointaine.",
        "avantages": "Facilitation des démarches de voyage, bourses ou projets internationaux, éveil de l'intuition.",
        "huile": "Ylang-Ylang (Attraction, charisme et union)", 
        "aromatiques": "Pétales de Rose, Anis étoilé (Badiane), Safran odorant pur",
        "zikr": "Ya Wadoud (Ô Aimant) — 20 fois + Nom Salomonique : EL GOLAH",
        "priere_salomonique": "Souverain Miséricordieux des Univers, EL GOLAH, Source de l'Amour universel et des voies d'ouverture. Que Ton Souffle sacré dissipe les nuages de l'isolement sur mes chemins. Ouvre grand les portes des contrées lointaines et connecte mon esprit aux alliances nobles. Amen.",
        "mots_application": "Que mes routes et mes déplacements créent des alliances heureuses et fructueuses. Amen.", "moment": "Matin"
    },
    "Souleymane (Mansa Solomani)": {
        "ref": "Souleymane (Mansa Solomani)", "code": (2, 1, 1, 2), "nature": "Bénéfique", "element": "Terre", "direction": "Ouest",
        "maison_repos": 10, "nom_maison_repos": "M10 (Travail / Autorité / Royauté)", "plante": "Sira ou baobab",
        "txt": "Maison de la carrière, du statut social, du lieu de travail, de la royauté et de l'autorité.",
        "psaume": "Psaume 45", "nb_ecriture": 10, "verset": "Verset 2", 
        "texte_biblique": "Des paroles pleines de charme bouillonnent dans mon cœur. Je dis : Mon œuvre est pour le roi !",
        "vibratoire": "Émission d'un champ magnétique de prestige. Dissout le mépris, impose le respect.",
        "avantages": "Élévation professionnelle, obtention de postes de responsabilité, succès commercial massif.",
        "huile": "Géranium Bourbon (Magnétisme professionnel et éclat)", 
        "aromatiques": "Feuilles de Géranium odorant, Marjolaine séchée, Poudre de Curcuma pur",
        "zikr": "Ya Jamil (Ô Beau) — 83 fois + Nom Salomonique : ADONAI TZABAOTH",
        "priere_salomonique": "Roi des Rois, Souverain de l'Ordre Cosmique, ADONAI TZABAOTH, Toi qui as accordé la Sagesse suprême au Roi Salomon. Revêts-moi aujourd'hui de Ton manteau de majesté, de charisme et d'autorité incontestable. Que mes œuvres soient couronnées de succès. Amen.",
        "mots_application": "Accorde-moi le charisme, le respect et l'autorité nécessaire dans mes entreprises. Amen.", "moment": "Matin"
    },
    "Ali (Badara Aliou)": {
        "ref": "Ali (Badara Aliou)", "code": (2, 1, 1, 1), "nature": "Bénéfique", "element": "Vent", "direction": "Sud",
        "maison_repos": 11, "nom_maison_repos": "M11 (Espoirs / Protections / Souhaits)", "plante": "Gbè yiri",
        "txt": "Maison des espoirs, de la protection, de la chose espérée, des aides providentielles et des envies.",
        "psaume": "Psaume 144", "nb_ecriture": 11, "verset": "Verset 1", 
        "texte_biblique": "Béni soit l'Éternel, mon rocher, qui exerce mes mains au combat, mes doigts à la bataille !",
        "vibratoire": "Onde de dynamisation éthérique. Recharge l'énergie vitale et efface le découragement.",
        "avantages": "Soutiens financiers providentiels, concrétisation de souhaits bloqués depuis longtemps.",
        "huile": "Gingembre Bleu (Force, dynamisme et courage)", 
        "aromatiques": "Graines de Cardamome craquées, Menthe des champs, Poudre fine de Gingembre",
        "zikr": "Ya Qawiyyou (Ô Fort Invincible) — 116 fois + Nom Salomonique : EL SHADDAI",
        "priere_salomonique": "Principe Fort et Invincible, EL SHADDAI, mon Rocher et mon rempart indéfectible. Exerce mon âme à la maîtrise des lois de la vie. Injecte Ton feu de courage au plus profond de mes os. Que mes vœux pieux se transforment en décrets de matière. Amen.",
        "mots_application": "Que mes espérances les plus profondes soient fortifiées et protégées contre tout obstacle. Amen.", "moment": "Matin"
    },
    "Nouhou (Nounkoro)": {
        "ref": "Nouhou (Nounkoro)", "code": (1, 2, 2, 2), "nature": "Mauvais", "element": "Terre", "direction": "Ouest",
        "maison_repos": 12, "nom_maison_repos": "M12 (Difficultés / Obstacles / Ennemis)", "plante": "kounbè",
        "txt": "Maison des grandes difficultés, des problèmes structurels, des ennemis cachés et des entraves.",
        "psaume": "Psaume 30", "nb_ecriture": 12, "verset": "Verset 12", 
        "texte_biblique": "Tu as changé mon deuil en allégresse, tu as délié mon sac, et tu m'as ceint de joie.",
        "vibratoire": "Onde de submersion des forces contraires (Fréquence de l'Arche de Salut). Nettoie l'astral lourd.",
        "avantages": "Délivrance immédiate des blocages familiaux anciens, rupture des pièges tendus dans l'ombre.",
        "huile": "Citronnelle Java (Nettoyage des ondes lourdes)", 
        "aromatiques": "Tiges de Citronnelle fraîches émincées, Thym blanc, Clou de Girofle pilé",
        "zikr": "Ya Latif (Ô Bienveillant) — 129 fois + Nom Salomonique : IAH",
        "priere_salomonique": "Souverain Absolu du Salut, Nom Sublime IAH, Toi qui as sauvé Noé des eaux du déluge et changé le deuil en allégresse. Abaisse Ton regard sur mes afflictions. Déchire le sac de mes difficultés, détruis les complots des esprits ténébreux et ceins mes reins de joie. Amen.",
        "mots_application": "Que tous les pièges de l'ombre soient déracinés et dissous, laissant place au triomphe. Amen.", "moment": "Soir"
    },
    "Houssaini (Ioussiné)": {
        "ref": "Houssaini (Ioussiné)", "code": (1, 1, 2, 2), "nature": "Neutre", "element": "Eau", "direction": "Nord",
        "maison_repos": 13, "nom_maison_repos": "M13 (Dortoir / Lit / Présent immédiat)", "plante": "zaman",
        "txt": "Maison de la situation présente, de la chambre à coucher, du dortoir et des secrets intimes.",
        "psaume": "Psaume 18", "nb_ecriture": 13, "verset": "Verset 38", 
        "texte_biblique": "Je les brise, et ils ne peuvent se relever ; ils tombent sous mes pieds.",
        "vibratoire": "Fréquence de stabilisation absolue du flux nocturne. Éloigne les cauchemars et les attaques.",
        "avantages": "Sommeil profondément réparateur, clarification de la confusion mentale, paix dans le couple.",
        "huile": "Clou de Girofle (Scellage et protection du lieu)", 
        "aromatiques": "Feuilles d'Eucalyptus, Clous de girofle entiers, Écorce de cannelle",
        "zikr": "Ya Moumit (Ô Maître de la libération) — 490 fois + Nom Salomonique : ELOHIM",
        "priere_salomonique": "Maître Souverain du Temps et de l'Espace, ELOHIM Juste, Toi qui fixes les frontières du jour et de la nuit. Purifie mon sanctuaire intime, ma couche et mes pensées de toute souillure. Que ma situation présente soit redressée par Ta puissance souveraine. Amen.",
        "mots_application": "Que ma situation actuelle soit clarifiée, purifiée et libérée des énergies stagnantes. Amen.", "moment": "Soir"
    },
    "Younouss (Tontigui)": {
        "ref": "Younouss (Tontigui)", "code": (1, 2, 1, 2), "nature": "Bénéfique", "element": "Terre", "direction": "Ouest",
        "maison_repos": 14, "nom_maison_repos": "M14 (Richesse future / Épargne)", "plante": "dialassogala",
        "txt": "Maison de l'argent à venir, des gains futurs, de la capitalisation et des projets financiers non accomplis.",
        "psaume": "Psaume 91", "nb_ecriture": 14, "verset": "Verset 11", 
        "texte_biblique": "Car il ordonnera à ses anges de te garder dans toutes tes voies.",
        "vibratoire": "Onde d'aimantation financière sécurisée. Protège les capitaux et attire l'abondance.",
        "avantages": "Rentrées d'argent rapides, blocage des pertes de capital, investissements fructueux.",
        "huile": "Arbre à Thé / Tea Tree (Bouclier financier)", 
        "aromatiques": "Laurier noble séché, Coriandre en graines entières, Curcuma de qualité",
        "zikr": "Ya Hafiz (Ô Protecteur Suprême) — 998 fois + Nom Salomonique : JEHOVAH JIREH",
        "priere_salomonique": "Pourvoyeur Universel, JEHOVAH JIREH, Toi qui ordonnes à Tes légions d'Anges d'escorter les pas des Justes. Déploie Tes sentinelles de prospérité autour de mes finances. Scelle mes coffres, fructifie mon travail et attire à moi l'abondance. Amen.",
        "mots_application": "Que la prospérité future promise par ce thème soit scellée et divinement protégée. Amen.", "moment": "Matin"
    },
    "Ousmane (Mori Zoumana)": {
        "ref": "Ousmane (Mori Zoumana)", "code": (2, 2, 1, 1), "nature": "Bénéfique", "element": "Vent", "direction": "Sud",
        "maison_repos": 15, "nom_maison_repos": "M15 (Conclusion générale)", "plante": "Doualé",
        "txt": "Maison de la conclusion du thème, du résumé général des affaires, du bilan et de l'environnement final.",
        "psaume": "Psaume 119", "nb_ecriture": 15, "verset": "Verset 105", 
        "texte_biblique": "Ta parole est une lampe à mes pieds, et une lumière sur mon sentier.",
        "vibratoire": "Fréquence de synthèse et d'harmonie finale. Aligne la décision sur la justesse karmique.",
        "avantages": "Dénouement heureux d'une affaire complexe, vision globale claire de la solution.",
        "huile": "Encens d'Oliban (Haute connexion divine et conclusion céleste)", 
        "aromatiques": "Résine pure d'Oliban en larmes, Fleurs de Jasmin séchées, Poudre de Safran",
        "zikr": "Ya Alim (Ô Omniscient) — 150 fois + Nom Salomonique : TETRAGRAMMATON",
        "priere_salomonique": "Sagesse Suprême, TETRAGRAMMATON Ineffable, dont le Verbe Sacré est une lampe infaillible à mes pieds. Toi qui connais la fin avant le commencement, illumine l'issue de mon thème et de ma vie. Que Ta vérité triomphe de toute illusion. Amen.",
        "mots_application": "Que la lumière parfaite éclaire la conclusion de mes démarches et m'apporte la réussite globale. Amen.", "moment": "Soir"
    },
    "Moussa (Moussa)": {
        "ref": "Moussa (Moussa)", "code": (2, 1, 2, 1), "nature": "Neutre à Fort", "element": "Feu", "direction": "Est",
        "maison_repos": 16, "nom_maison_repos": "M16 (Le Décret / Confirmation)", "plante": "tomy bourou",
        "txt": "Maison du Décret de l'esprit, de la confirmation finale, de la sentence et de la haute précision.",
        "psaume": "Psaume 4", "nb_ecriture": 16, "verset": "Verset 7", 
        "texte_biblique": "Fais lever sur nous la lumière de ta face, ô Éternel !",
        "vibratoire": "Fréquence d'activation instantanée. Tranche les fils d'attente et matérialise la réponse.",
        "avantages": "Validation ou signature immédiate de contrats, déblocage des verdicts juridiques ou administratifs.",
        "huile": "Orange Douce (Rapidité et scellage solaire)", 
        "aromatiques": "Zestes de Citron vert, Feuilles de Menthe poivrée, Cannelle de Ceylan",
        "zikr": "Ya Sari'u (Ô Rapide) — 202 fois + Nom Salomonique : SCHEMHAMPHORASCH",
        "priere_salomonique": "Par le Grand Nom Sacré et Vibrant SCHEMHAMPHORASCH, Toi le Maître des décrets foudroyants et de la justice immédiate. Fais luire l'éclair de Ta face sur mon destin. Que Ta sentence brise le retard chronique, valide mes requêtes et scelle ce travail. Amen.",
        "mots_application": "Que le décret final de cette consultation s'exécute en ma faveur avec force et rapidité. Amen.", "moment": "Matin"
    }
}

MAISONS_NOMINATIVES = {
    1: "M1 (Demandeur)", 2: "M2 (Biens/Chances)", 3: "M3 (Entourage)", 4: "M4 (Foyer/Patrimoine)",
    5: "M5 (Enfants/Nouvelles)", 6: "M6 (Maladies)", 7: "M7 (Adversaires/Époux)", 8: "M8 (Mort/Peurs)",
    9: "M9 (Voyages)", 10: "M10 (Travail/Autorité)", 11: "M11 (Espoirs)", 12: "M12 (Difficultés)",
    13: "M13 (Témoin Droite)", 14: "M14 (Témoin Gauche)", 15: "M15 (Conclusion)", 16: "M16 (Le Décret)"
}

# ==============================================================================
# FONCTIONS DE CALCULS DU THÈME GÉOMANTIQUE
# ==============================================================================
def additionner_lignes(fig1, fig2):
    c1 = DATA[fig1]["code"]
    c2 = DATA[fig2]["code"]
    nouveau_code = []
    for i in range(4):
        total = c1[i] + c2[i]
        nouveau_code.append(2 if total % 2 == 0 else 1)
    for nom, bloc in DATA.items():
        if bloc["code"] == tuple(nouveau_code):
            return nom
    return fig1

def generer_fille(m1, m2, m3, m4, index_ligne):
    code_fille = (
        DATA[m1]["code"][index_ligne],
        DATA[m2]["code"][index_ligne],
        DATA[m3]["code"][index_ligne],
        DATA[m4]["code"][index_ligne]
    )
    for nom, bloc in DATA.items():
        if bloc["code"] == code_fille:
            return nom
    return m1

# ==============================================================================
# FONCTION INTERPRÉTATIVE DE PASSATION DE MAISON
# ==============================================================================
def interpreter_passation(nom_figure, maison_actuelle):
    maison_repos = DATA[nom_figure]["maison_repos"]
    nom_maison_repos = DATA[nom_figure]["nom_maison_repos"]
    plante_associee = DATA[nom_figure]["plante"]
    
    if maison_repos == maison_actuelle:
        return f"✨ **La figure est chez elle (Maison de Repos originelle).** Ses vibrations et sa plante alternative (**{plante_associee}**) agissent à leur plein potentiel natif. L'énergie sectorielle est stable, pure et directe."
    else:
        return f"🔄 **Passation Métaphysique :** La figure originelle de *{nom_maison_repos}* a migré vers la **Maison {maison_actuelle} ({MAISONS_NOMINATIVES[maison_actuelle]})**. Elle transfère l'influence de sa plante native **{plante_associee}** et ses thématiques d'origine pour colorer, activer ou perturber les enjeux de la Maison {maison_actuelle}."

# ==============================================================================
# APPLICATION INTERFACE UTILISATEUR
# ==============================================================================
st.title("🔮 Plateforme Théurgique de Géomancie et d'Interprétation au Repos")
st.write("Dressez le thème. Le système configure automatiquement la matrice par rapport aux 16 positions de repos fondamentales et calcule la passation des figures.")

with st.sidebar:
    st.header("🔐 Accès au Temple")
    u_id = st.text_input("Identifiant")
    u_pw = st.text_input("Mot de passe", type="password")

if u_id == ID_SECRET and u_pw == MDP_SECRET:
    st.success("🔓 Outils géomantiques au repos actifs.")
    
    # Présentation didactique des figures au repos
    with st.expander("📊 Consulter la Table Fondamentale des Positions de Repos", expanded=False):
        st.markdown("### Cartographie des Figures dans leurs Maisons d'Origine (Positions au repos)")
        cols = st.columns(4)
        for idx, (nom, b) in enumerate(DATA.items()):
            with cols[idx % 4]:
                st.info(f"**Maison {b['maison_repos']}**\n\n**{nom}**\n\n🌿 Plante : `{b['plante']}`")

    st.header("📥 ENTRÉE : INTRODUIRE LES 4 MÈRES")
    options_figures = list(DATA.keys())
    
    c1, col2, col3, col4 = st.columns(4)
    with c1: m1 = st.selectbox("🏠 M1 (Première Mère)", options_figures, index=0)
    with col2: m2 = st.selectbox("🏠 M2 (Deuxième Mère)", options_figures, index=1)
    with col3: m3 = st.selectbox("🏠 M3 (Troisième Mère)", options_figures, index=2)
    with col4: m4 = st.selectbox("🏠 M4 (Quatrième Mère)", options_figures, index=3)

    # Calcul automatique de la matrice géomantique
    m5 = generer_fille(m1, m2, m3, m4, 0)
    m6 = generer_fille(m1, m2, m3, m4, 1)
    m7 = generer_fille(m1, m2, m3, m4, 2)
    m8 = generer_fille(m1, m2, m3, m4, 3)

    m9 = additionner_lignes(m1, m2)
    m10 = additionner_lignes(m3, m4)
    m11 = additionner_lignes(m5, m6)
    m12 = additionner_lignes(m7, m8)

    m13 = additionner_lignes(m9, m10)
    m14 = additionner_lignes(m11, m12)
    m15 = additionner_lignes(m13, m14)
    m16 = additionner_lignes(m15, m1)

    theme_complet = {
        1: m1, 2: m2, 3: m3, 4: m4, 5: m5, 6: m6, 7: m7, 8: m8,
        9: m9, 10: m10, 11: m11, 12: m12, 13: m13, 14: m14, 15: m15, 16: m16
    }

    # Affichage graphique de la carte calculée
    st.markdown("---")
    st.header("🖼️ THÈME ANALYSÉ ET CONFIGURATION DU CONSULTANT")
    
    with st.container(border=True):
        st.subheader("⚜️ Ligne I : Les 4 Mères")
        i1, i2, i3, i4 = st.columns(4)
        i1.metric("M1 (Le Demandeur)", theme_complet[1])
        i2.metric("M2 (Flux Financier)", theme_complet[2])
        i3.metric("M3 (Relations)", theme_complet[3])
        i4.metric("M4 (Le Foyer)", theme_complet[4])
        
        st.subheader("🌿 Ligne II : Les 4 Filles")
        i5, i6, i7, i8 = st.columns(4)
        i5.metric("M5 (Enfants/Messages)", theme_complet[5])
        i6.metric("M6 (Maladies/Accompli)", theme_complet[6])
        i7.metric("M7 (Alliances/Rivaux)", theme_complet[7])
        i8.metric("M8 (Obstacles/Angoisses)", theme_complet[8])

        st.subheader("⚡ Ligne III : Les 4 Neveux")
        i9, i10, i11, i12 = st.columns(4)
        i9.metric("M9 (Déplacements)", theme_complet[9])
        i10.metric("M10 (Statut/Carrière)", theme_complet[10])
        i11.metric("M11 (Souhaits/Espoirs)", theme_complet[11])
        i12.metric("M12 (Difficultés)", theme_complet[12])

        st.subheader("⚖️ Tribunal d'Interprétation Finale")
        i13, i14, i15, i16 = st.columns(4)
        i13.warning(f"M13 (Témoin Droite) : {theme_complet[13]}")
        i14.warning(f"M14 (Témoin Gauche) : {theme_complet[14]}")
        i15.error(f"M15 (Le Juge) : {theme_complet[15]}")
        i16.success(f"M16 (Le Décret Suprême) : {theme_complet[16]}")

    # Module d'interprétation approfondie et thérapeutique par maison
    st.markdown("---")
    st.header("📖 ANALYSE VIBRATOIRE ET POLARITÉS DE PASSATION")
    
    for m, fig_choisie in theme_complet.items():
        bloc = DATA[fig_choisie]
        statut_action = "🛑 SECTEUR CRITIQUE" if "Mauvais" in bloc["nature"] else "✨ SECTEUR HARMONIEUX"
        titre_boite = f"{MAISONS_NOMINATIVES[m]} ➔ Figure présente : {fig_choisie} [{statut_action}]"
        
        with st.expander(titre_boite):
            tab_passation, tab_recette, tab_theurgie = st.tabs(["🔄 Analyse de Passation", "🌱 Propriétés de la Plante", "📿 Protocole Salomonique"])
            
            with tab_passation:
                st.markdown("### 🗺️ Transit géomantique :")
                st.info(interpreter_passation(fig_choisie, m))
                st.markdown("---")
                st.markdown(f"**Signification originelle de la Figure au Repos :** *{bloc['txt']}*")
                st.markdown(f"**Nature de la force :** Élément `{bloc['element'].upper()}` | Direction `{bloc['direction'].upper()}`")
                st.write(f"**Effet sur le consultant :** {bloc['vibratoire']}")
                
            with tab_recette:
                st.markdown(f"### 🌿 Thérapeutique Spécifique (Plante Native : {bloc['plante']})")
                st.write(f"La figure amène avec elle l'énergie de sa plante corrective : **{bloc['plante']}**.")
                st.write(f"🧪 **Mélange d'infusion recommandé :** `{bloc['aromatiques']}`")
                st.write(f"💧 **Huile essentielle de scellage :** *{bloc['huile']}*")
                st.success(f"✍️ **Écriture sacrée :** Écrire le **{bloc['verset']}** du **{bloc['psaume']}** exactement **{bloc['nb_ecriture']} fois** pour fabriquer le support de soin.")
                
            with tab_theurgie:
                st.markdown("### 📿 Invocations Théurgiques Actives")
                st.warning(f"**Clé sacrée (Zikr) :** {bloc['zikr']}")
                st.markdown(f"> **Prière Salomonique de la Figure :** *{bloc['priere_salomonique']}*")
                st.success(f"🗣️ **Parole d'affirmation :** \"{bloc['mots_application']}\"")
                st.caption(f"⏱️ **Moment favorable :** {bloc['moment']}")
else:
    st.warning("🔒 Système Verrouillé. Veuillez inscrire les codes secrets dans le panneau de gauche.")
