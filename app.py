import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Système Théurgique Géomancie Rectifiée", page_icon="🔮", layout="wide")

# ==============================================================================
# ACCÈS SÉCURISÉS
# ==============================================================================
ID_SECRET = "theurge2026"
MDP_SECRET = "Salomon777"

# ==============================================================================
# BASE DE DONNÉES STRUCTURÉE (Basée sur l'image FB_IMG_1781201647620.jpg)
# ==============================================================================
DATA = {
    "Janfa almamy": {
        "ref": "Janfa almamy", "code": (1, 2, 1, 1), "nature": "Bénéfique", "element": "Feu",
        "maison_repos": 1, "nom_maison_repos": "M1 (Demandeur / Esprit-Âme)", "plante": "Balança",
        "txt": "Maison du demandeur, de son état physique, moral, de son âme et de sa conscience primordiale.",
        "psaume": "Psaume 20", "verset": "Verset 5", 
        "texte_biblique": "Qu'il te donne ce que ton cœur désire, et qu'il accomplisse tous tes desseins !",
        "zikr_verset": "Réciter le Verset 5 du Psaume 20 exactement 77 fois par jour.",
        "repetitions": "77",
        "bain_preparation": "Faire bouillir une poignée de feuilles ou d'écorces de Balança dans 5 litres d'eau purifiée pendant 15 minutes. Laisser tiédir et filtrer.",
        "bain_posologie": "Se laver avec cette décoction pendant 7 jours consécutifs, le matin au lever du soleil, sans utiliser de savon chimique après le rinçage.",
        "huile": "Laurier Noble", 
        "aromatiques": "Feuilles de Laurier sauce, Menthe poivrée fraîche, Safran",
        "zikr": "Ya Wahhab (Ô Donateur Suprême) — 14 fois + Nom Salomonique : EHIEH ASHER EHIEH",
        "priere_salomonique": "Par la puissance de la Couronne Suprême et le Nom Ineffable EHIEH ASHER EHIEH, j'invoque Ton rayonnement sur mon âme. Brise les verrous de mon esprit, enflamme mon aura de Ta lumière inextinguible et accorde-moi la victoire sur mes propres ombres. Que Ta grâce manifeste les désirs purs de mon cœur et que mes desseins s'accomplissent selon Ton ordre universel. Amen.",
        "mots_application": "Que mon âme soit purifiée et que les intentions de ce thème reçoivent la clarté. Amen.", "moment": "Matin au lever",
        "savon_additifs": "Feuilles de laurier broyées en poudre fine et une pincée de safran."
    },
    "Adama": {
        "ref": "Adama", "code": (1, 1, 1, 1), "nature": "Bénéfique", "element": "Feu",
        "maison_repos": 2, "nom_maison_repos": "M2 (Biens / Flux financiers)", "plante": "Sana",
        "txt": "Maison des biens, des finances, de la chance matérielle et des flux énergétiques entrants.",
        "psaume": "Psaume 8", "verset": "Verset 6", 
        "texte_biblique": "Tu lui as donné l'empire sur les œuvres de tes mains, tu as tout mis sous ses pieds.",
        "zikr_verset": "Réciter le Verset 6 du Psaume 8 exactement 88 fois après la prière du matin.",
        "repetitions": "88",
        "bain_preparation": "Infuser 100g de feuilles de Sana séchées dans de l'eau de source chauffée. Ajouter une cuillère à café de Curcuma pur.",
        "bain_posologie": "Bain à prendre pendant 3 jours consécutifs en versant l'eau de la tête aux pieds, de préférence le matin, pour attirer l'élévation financière.",
        "huile": "Cèdre de l'Atlas", 
        "aromatiques": "Basilic sacré (Tulsi), Romarin officinal, Curcuma en poudre",
        "zikr": "Ya Rafi'u (Ô Celui qui élève) — 351 fois + Nom Salomonique : ADONAI MELEKH",
        "priere_salomonique": "Ô Seigneur Souverain, Roi de la Terre, ADONAI MELEKH, Toi qui as façonné l'homme de poussière et d'esprit et l'as couronné de gloire. Par cette onction et ce bain de feu, confère-moi l'empire légitime sur la matière. Éloigne de mes mains le spectre du manque. Que l'abondance infinie se prosterne à mes pieds. Amen.",
        "mots_application": "Que l'abondance matérielle et l'élévation financière s'installent durablement. Amen.", "moment": "Matin",
        "savon_additifs": "Une demi-cuillère à café de curcuma pur en poudre pour la couleur or et la fixation financière, avec du romarin séché émietté."
    },
    "Maleju": {
        "ref": "Maleju", "code": (1, 1, 1, 2), "nature": "Neutre", "element": "Vent",
        "maison_repos": 3, "nom_maison_repos": "M3 (Famille / Entourage proche)", "plante": "Cebé",
        "txt": "Maison de la famille, des voisins, des collègues, des communications et de l'entourage proche.",
        "psaume": "Psaume 4", "verset": "Verset 7", 
        "texte_biblique": "Fais lever sur nous la lumière de ta face, ô Éternel !",
        "zikr_verset": "Réciter le Verset 7 du Psaume 4 exactement 33 fois matin et soir.",
        "repetitions": "33",
        "bain_preparation": "Laisser macérer des feuilles fraîches de Cebé dans de l'eau froide exposée aux premiers rayons de soleil pendant 4 heures. Filtrer et ajouter quelques zestes d'orange.",
        "bain_posologie": "Utiliser comme eau de rinçage après votre douche habituelle pendant 5 jours pour harmoniser les relations familiales et de voisinage.",
        "huile": "Orange Douce", 
        "aromatiques": "Zestes d'Orange douce, Menthe douce, Écorce de Cannelle",
        "zikr": "Ya Nour (Ô Lumière) — 256 fois + Nom Salomonique : ELOHIM SABAOTH",
        "priere_salomonique": "Souverain des Armées Célestes, ELOHIM SABAOTH, Source éternelle de concorde et de lumière. Que la splendeur sacrée de Ta Face descende sur mon cercle social et familial. Purifie ma langue de toute parole amère, dissout la haine ou la jalousie secrète de mon entourage. Fais de moi un canal de paix. Amen.",
        "mots_application": "Que la concorde et la paix illuminent mes relations avec mon entourage. Amen.", "moment": "Matin",
        "savon_additifs": "Poudre fine de cannelle et morceaux très fins de zestes d'orange séchés."
    },
    "Albayada": {
        "ref": "Albayada", "code": (2, 2, 1, 2), "nature": "Bénéfique", "element": "Eau",
        "maison_repos": 4, "nom_maison_repos": "M4 (Foyer / Patrimoine)", "plante": "Djou",
        "txt": "Maison du foyer, de la maison familiale, du patrimoine immobilier et de l'autorité parentale.",
        "psaume": "Psaume 112", "verset": "Verset 3", 
        "texte_biblique": "Il a dans sa maison bien-être et richesse, et sa justice subsiste à jamais.",
        "zikr_verset": "Réciter le Verset 3 du Psaume 112 exactement 44 fois au cœur de la maison.",
        "repetitions": "44",
        "bain_preparation": "Décoction lourde de racines ou feuilles de Djou avec 3 clous de girofle. Faire bouillir longuement à feu doux.",
        "bain_posologie": "Prendre ce bain protecteur et purificateur le mercredi soir. Asperger également les quatre coins de la maison avec un peu de cette eau.",
        "huile": "Patchouli", 
        "aromatiques": "Bâtons de Cannelle, Clous de Girofle, Curcuma",
        "zikr": "Ya Razzaq (Ô Pourvoyeur) — 308 fois + Nom Salomonique : SHADDAI EL CHAI",
        "priere_salomonique": "Principe Vivant et Tout-Puissant, SHADDAI EL CHAI, Fondement inébranlable des siècles. J'invoque Ta bénédiction sur ma demeure et mon sang. Fais couler le fleuve du bien-être et de la richesse intarissable dans mon foyer. Que le vice en soit chassé et que Ta justice y règne éternellement. Amen.",
        "mots_application": "Que la stabilité, le bien-être et la richesse s'ancrent au cœur de mon foyer. Amen.", "moment": "Matin",
        "savon_additifs": "Clous de girofle pilés en fine poudre et une pincée de curcuma protecteur."
    },
    "Tariki": {
        "ref": "Tariki", "code": (1, 1, 2, 1), "nature": "Bénéfique", "element": "Eau",
        "maison_repos": 5, "nom_maison_repos": "M5 (Enfants / Nouvelles)", "plante": "Djècala",
        "txt": "Maison des enfants, de la créativité, des plaisirs et des nouvelles ou messages entrants.",
        "psaume": "Psaume 100", "verset": "Verset 2", 
        "texte_biblique": "Servez l'Éternel avec joie, venez avec allégresse en sa présence !",
        "zikr_verset": "Réciter le Verset 2 du Psaume 100 exactement 55 fois avant de lire ou d'envoyer des courriers importants.",
        "repetitions": "55",
        "bain_preparation": "Infuser des tiges de Citronnelle et des feuilles de Djècala dans de l'eau bouillante. Laisser refroidir jusqu'à température agréable.",
        "bain_posologie": "Bain de clarté à effectuer pendant 3 jours consécutifs, idéalement le matin, pour débloquer les situations administratives ou obtenir de bonnes nouvelles.",
        "huile": "Pamplemousse", 
        "aromatiques": "Verveine odorante, Citronnelle, Pistils de Safran",
        "zikr": "Ya Latif (Ô Doux) — 129 fois + Nom Salomonique : YHVH SABAOTH",
        "priere_salomonique": "Seigneur Souverain de l'Allégresse, YHVH SABAOTH, dont la douceur s'étend sur toute créature. Permets que Ton parfum de joie pénètre mon temple corporel. Chasse la tristesse stérile. Fais lever sur ma vie des messages de triomphe et accorde la protection à ma lignée. Amen.",
        "mots_application": "Que les nouvelles qui me parviennent apportent la joie, la réussite et l'allégresse. Amen.", "moment": "Matin",
        "savon_additifs": "Feuilles de verveine séchées réduites en miettes et une pincée de poudre de safran."
    },
    "N'gansa": {
        "ref": "N'gansa", "code": (2, 2, 2, 2), "nature": "Neutre à Mauvais", "element": "Eau",
        "maison_repos": 6, "nom_maison_repos": "M6 (Maladies / Choses accomplies)", "plante": "Wingninga",
        "txt": "Maison de la maladie, des blocages corporels, de la servitude et des choses déjà accomplies.",
        "psaume": "Psaume 51", "verset": "Verset 12", 
        "texte_biblique": "Ô Dieu ! crée en moi un cœur pur, renouvelle en moi un esprit bien disposé.",
        "zikr_verset": "Réciter le Verset 12 du Psaume 51 exactement 66 fois à genoux avant de dormir.",
        "repetitions": "66",
        "bain_preparation": "Faire bouillir vigoureusement les feuilles de Wingninga avec du sel gemme brut dans 6 litres d'eau.",
        "bain_posologie": "Bain de purification profonde et d'exorcisme corporel à faire pendant 6 soirs d'affilée juste avant le coucher. Recueillir l'eau résiduelle si possible pour l'évacuer hors de la concession.",
        "huile": "Lavande Vraie", 
        "aromatiques": "Fleurs de Lavande, Camomille, Poudre de Santal Blanc",
        "zikr": "Ya Chafi (Ô Guérisseur) — 391 fois + Nom Salomonique : ELOHIM GIBOR",
        "priere_salomonique": "Principe de Justice et Forteresse Inflexible, ELOHIM GIBOR, Toi qui sondes les reins et les cœurs. Lave mon corps et mon âme. Crée en moi un réceptacle immaculé. Par le pouvoir de Ton Autel, calcine toute maladie occulte et brise les chaînes de la servitude. Amen.",
        "mots_application": "Purifie mon être de toute négativité, entrave ou influence maladive cachée. Amen.", "moment": "Soir",
        "savon_additifs": "Fleurs de lavande séchées, poudre de santal blanc et une cuillère à café de gros sel marin écrasé."
    },
    "Lumara": {
        "ref": "Lumara", "code": (2, 1, 2, 2), "nature": "Mauvais", "element": "Vent",
        "maison_repos": 7, "nom_maison_repos": "M7 (Adversaires / Époux)", "plante": "Gababelé",
        "txt": "Maison des adversaires, des rivaux, des conflits déclarés, du mariage et des partenaires.",
        "psaume": "Psaume 35", "verset": "Verset 1", 
        "texte_biblique": "Éternel ! Attaque ceux qui m'attaquent, combats ceux qui me combatte !",
        "zikr_verset": "Réciter le Verset 1 du Psaume 35 vigoureusement 71 fois face à l'Est en cas de conflit avéré.",
        "repetitions": "71",
        "bain_preparation": "Préparer une eau de combat tiède en infusant du Gababelé broyé avec du gingembre frais émincé.",
        "bain_posologie": "Se laver uniquement le soir tard pendant 3 jours. Ce bain agit comme un bouclier de retour à l'envoyeur contre les complots et les litiges.",
        "huile": "Cannelle Écorce", 
        "aromatiques": "Poivre noir, Thym fort, Ortie piquante, Gingembre",
        "zikr": "Ya Jabbar (Ô Contraignant) — 206 fois + Nom Salomonique : ELOHIM GIBOR",
        "priere_salomonique": "Juge Terrible des Oppresseurs, ELOHIM GIBOR, Puissance des vengeances légitimes. Tire Ton épée flamboyante et dresse Ton bouclier devant mes pas. Combat ceux qui cherchent ma ruine. Que la confusion s'abatte sur mes adversaires invisibles ou visibles. Amen.",
        "mots_application": "Que toute opposition, conflit ou rivalité se brise face à la justice supérieure. Amen.", "moment": "Soir",
        "savon_additifs": "Poudre de thym fort et une petite pincée de poivre noir moulu pour briser les attaques."
    },
    "Mankusi": {
        "ref": "Mankusi", "code": (2, 2, 2, 1), "nature": "Mauvais", "element": "Terre",
        "maison_repos": 8, "nom_maison_repos": "M8 (Mort / Peurs / Patrimoine caché)", "plante": "Kronifin",
        "txt": "Maison de la mort, des angoisses profondes, des héritages, de la fatalité et du malheur.",
        "psaume": "Psaume 142", "verset": "Verset 8", 
        "texte_biblique": "Tire mon âme de sa prison, afin que je célèbre ton nom !",
        "zikr_verset": "Réciter le Verset 8 du Psaume 142 exactement 82 fois dans l'obscurité pour briser les blocages psychologiques.",
        "repetitions": "82",
        "bain_preparation": "Faire bouillir les feuilles de Kronifin avec une poignée de charbon végétal purifié.",
        "bain_posologie": "Bain de coupure karmique à prendre à minuit pile pendant 1 seul soir. Essuyer le corps avec un tissu propre noir à jeter ensuite.",
        "huile": "Cyprès de Provence", 
        "aromatiques": "Sauge officinale, Racine de Gingembre, Charbon de bois",
        "zikr": "Ya Moukhrij (Ô Celui qui fait sortir) — 201 fois + Nom Salomonique : AGLA",
        "priere_salomonique": "Souverain Éternel, Force immuable, AGLA, Toi qui as les clés des abîmes et de la vie. Entends mon cri du fond de la fosse. Brise les portes d'airain et les verrous de fer de ma prison existentielle. Tire mon âme de l'angoisse et fais-moi remonter vers la lumière. Amen.",
        "mots_application": "Je me libère des angoisses, des blocages et de toute forme d'enfermement. Amen.", "moment": "Soir",
        "savon_additifs": "Sauge officinale réduite en poudre et une pincée de charbon actif végétal pour l'absorption des impuretés astrales."
    },
    "Kalalaw": {
        "ref": "Kalalaw", "code": (1, 2, 2, 1), "nature": "Bénéfique", "element": "Feu",
        "maison_repos": 9, "nom_maison_repos": "M9 (Voyages / Spiritualité / Mobilité)", "plante": "Sadjo ou aladjo",
        "txt": "Maison des déplacements, des voyages, de la spiritualité, de la recherche et du dynamisme.",
        "psaume": "Psaume 133", "verset": "Verset 1", 
        "texte_biblique": "Voici, qu'il est agréable, qu'il est doux pour des frères de demeurer ensemble !",
        "zikr_verset": "Réciter le Verset 1 du Psaume 133 exactement 99 fois avant d'entreprendre des démarches de visa ou de voyage.",
        "repetitions": "99",
        "bain_preparation": "Infuser des feuilles de Sadjo (ou Aladjo) avec des pétales de roses fraîches et de l'anis étoilé.",
        "bain_posologie": "Prendre ce bain d'ouverture de routes spirituelles et géographiques pendant 7 jours consécutifs le matin.",
        "huile": "Ylang-Ylang", 
        "aromatiques": "Pétales de Rose, Anis étoilé, Safran",
        "zikr": "Ya Wadoud (Ô Aimant) — 20 fois + Nom Salomonique : EL GOLAH",
        "priere_salomonique": "Souverain Miséricordieux des Univers, EL GOLAH, Source de l'Amour universel et des voies d'ouverture. Que Ton Souffle sacré dissipe les nuages de l'isolement sur mes chemins. Ouvre grand les portes des contrées lointaines et connecte mon esprit aux alliances nobles. Amen.",
        "mots_application": "Que mes routes et mes déplacements créent des alliances heureuses et fructueuses. Amen.", "moment": "Matin",
        "savon_additifs": "Pétales de roses séchées broyés et une étoile de badiane (anis étoilé) réduite en poudre très fine."
    },
    "Mansa Solomani": {
        "ref": "Mansa Solomani", "code": (2, 1, 1, 2), "nature": "Bénéfique", "element": "Terre",
        "maison_repos": 10, "nom_maison_repos": "M10 (Travail / Autorité / Royauté)", "plante": "Sira ou baobab",
        "txt": "Maison de la carrière, du statut social, du lieu de travail, de la royauté et de l'autorité.",
        "psaume": "Psaume 45", "verset": "Verset 2", 
        "texte_biblique": "Des paroles pleines de charme bouillonnent dans mon cœur. Je dis : Mon œuvre est pour le roi !",
        "zikr_verset": "Réciter le Verset 2 du Psaume 45 exactement 100 fois chaque matin avant d'aller travailler pour asseoir son charisme.",
        "repetitions": "100",
        "bain_preparation": "Faire bouillir de l'écorce ou des feuilles séchées de Sira (Baobab) pour obtenir une solution ambrée hautement magnétique.",
        "bain_posologie": "Se laver le corps pendant 9 jours consécutifs au réveil. Ce traitement impose le respect, l'autorité professionnelle et attire les promotions.",
        "huile": "Géranium Bourbon", 
        "aromatiques": "Feuilles de Géranium, Marjolaine séchée, Poudre de Curcuma",
        "zikr": "Ya Jamil (Ô Beau) — 83 fois + Nom Salomonique : ADONAI TZABAOTH",
        "priere_salomonique": "Roi des Rois, Souverain de l'Ordre Cosmique, ADONAI TZABAOTH, Toi qui as accordé la Sagesse suprême au Roi Salomon. Revêts-moi aujourd'hui de Ton manteau de majesté, de charisme et d'autorité incontestable. Que mes œuvres soient couronnées de succès. Amen.",
        "mots_application": "Accorde-moi le charisme, le respect et l'autorité nécessaire dans mes entreprises. Amen.", "moment": "Matin",
        "savon_additifs": "Poudre de feuilles de géranium séchées et une cuillère à soupe de miel pur naturel pour adoucir les relations hiérarchiques."
    },
    "Badara": {
        "ref": "Badara", "code": (2, 1, 1, 1), "nature": "Bénéfique", "element": "Vent",
        "maison_repos": 11, "nom_maison_repos": "M11 (Espoirs / Protections / Souhaits)", "plante": "Gbè yiri",
        "txt": "Maison des espoirs, de la protection, de la chose espérée, des aides providentielles et des envies.",
        "psaume": "Psaume 144", "verset": "Verset 1", 
        "texte_biblique": "Béni soit l'Éternel, mon rocher, qui exerce mes mains au combat, mes doigts à la bataille !",
        "zikr_verset": "Réciter le Verset 1 du Psaume 144 exactement 111 fois pour précipiter la réalisation d'un vœu cher.",
        "repetitions": "111",
        "bain_preparation": "Décoction de feuilles de Gbè yiri avec des graines de cardamome pilées.",
        "bain_posologie": "Bain d'activation de la chance providentielle à effectuer pendant 4 matins de suite, de préférence en début de mois lunaire.",
        "huile": "Gingembre Bleu", 
        "aromatiques": "Graines de Cardamome, Menthe des champs, Poudre de Gingembre",
        "zikr": "Ya Qawiyyou (Ô Fort Invincible) — 116 fois + Nom Salomonique : EL SHADDAI",
        "priere_salomonique": "Principe Fort et Invincible, EL SHADDAI, mon Rocher et mon rempart indéfectible. Exerce mon âme à la maîtrise des lois de la vie. Injecte Ton feu de courage au plus profond de mes os. Que mes vœux pieux se transforment en décrets de matière. Amen.",
        "mots_application": "Que mes espérances les plus profondes soient fortifiées et protégées contre tout obstacle. Amen.", "moment": "Matin",
        "savon_additifs": "Graines de cardamome écrasées et une cuillère à café de racine de gingembre séchée et pulvérisée."
    },
    "Nunkoro": {
        "ref": "Nunkoro", "code": (1, 2, 2, 2), "nature": "Mauvais", "element": "Terre",
        "maison_repos": 12, "nom_maison_repos": "M12 (Difficultés / Obstacles / Ennemis)", "plante": "kounbè",
        "txt": "Maison des grandes difficultés, des problèmes structurels, des ennemis cachés et des entraves.",
        "psaume": "Psaume 30", "verset": "Verset 12", 
        "texte_biblique": "Tu as changé mon deuil en allégresse, tu as délié mon sac, et tu m'as ceint de joie.",
        "zikr_verset": "Réciter le Verset 12 du Psaume 30 exactement 122 fois après le coucher du soleil pour dissoudre l'adversité.",
        "repetitions": "122",
        "bain_preparation": "Infuser vigoureusement une grande quantité de feuilles de Kounbè avec du thym blanc.",
        "bain_posologie": "Se laver entièrement pendant 7 soirs d'affilée pour briser les blocages répétitifs et éloigner définitivement les complots cachés.",
        "huile": "Citronnelle Java", 
        "aromatiques": "Tiges de Citronnelle, Thym blanc, Clou de Girofle",
        "zikr": "Ya Latif (Ô Bienveillant) — 129 fois + Nom Salomonique : IAH",
        "priere_salomonique": "Souverain Absolu du Salut, Nom Sublime IAH, Toi qui as sauvé Noé des eaux du déluge et changé le deuil en allégresse. Abaisse Ton regard onctueux sur mes afflictions. Déchire le sac de mes difficultés, détruis les complots des esprits ténébreux et ceins mes reins de joie. Amen.",
        "mots_application": "Que tous les pièges de l'ombre soient déracinés et dissous, laissant place au triomphe. Amen.", "moment": "Soir",
        "savon_additifs": "Poudre de thym blanc purificateur et clous de girofle moulus très fins."
    },
    "Lusiné": {
        "ref": "Lusiné", "code": (1, 1, 2, 2), "nature": "Neutre", "element": "Eau",
        "maison_repos": 13, "nom_maison_repos": "M13 (Dortoir / Lit / Présent immédiat)", "plante": "zaman",
        "txt": "Maison de la situation présente, de la chambre à coucher, du dortoir et des secrets intimes.",
        "psaume": "Psaume 18", "verset": "Verset 38", 
        "texte_biblique": "Je les brise, et ils ne peuvent se relever ; ils tombent sous mes pieds.",
        "zikr_verset": "Réciter le Verset 38 du Psaume 18 exactement 133 fois dans la chambre à coucher avant le repos nocturne.",
        "repetitions": "133",
        "bain_preparation": "Préparer une eau de purification calme en infusant de l'écorce ou des feuilles de Zaman avec des feuilles d'Eucalyptus.",
        "bain_posologie": "Bain apaisant à prendre le soir juste avant le coucher pendant 5 jours pour nettoyer l'atmosphère intime et stabiliser le couple.",
        "huile": "Clou de Girofle", 
        "aromatiques": "Feuilles d'Eucalyptus, Clous de girofle, Écorce de cannelle",
        "zikr": "Ya Moumit (Ô Maître de la libération) — 490 fois + Nom Salomonique : ELOHIM",
        "priere_salomonique": "Maître Souverain du Temps et de l'Espace, ELOHIM Juste, Toi qui fixes les frontières du jour et de la nuit. Purifie mon sanctuaire intime, ma couche et mes pensées de toute souillure. Que ma situation présente soit redressée par Ta puissance souveraine. Amen.",
        "mots_application": "Que ma situation actuelle soit clarifiée, purifiée et libérée des énergies stagnantes. Amen.", "moment": "Soir",
        "savon_additifs": "Poudre de feuilles d'eucalyptus pour la clarté et cannelle fine pour la chaleur relationnelle."
    },
    "Tontigi": {
        "ref": "Tontigi", "code": (1, 2, 1, 2), "nature": "Bénéfique", "element": "Terre",
        "maison_repos": 14, "nom_maison_repos": "M14 (Richesse future / Épargne)", "plante": "dialassogala",
        "txt": "Maison de l'argent à venir, des gains futurs, de la capitalisation et des projets financiers non accomplis.",
        "psaume": "Psaume 91", "verset": "Verset 11", 
        "texte_biblique": "Car il ordonnera à ses anges de te garder dans toutes tes voies.",
        "zikr_verset": "Réciter le Verset 11 du Psaume 91 exactement 144 fois le matin pour sécuriser vos investissements.",
        "repetitions": "144",
        "bain_preparation": "Faire bouillir des écorces de Dialassogala avec des graines de coriandre.",
        "bain_posologie": "Bain d'attraction financière durable à exécuter pendant 5 matins consécutifs en formulant clairement des vœux de prospérité commerciale.",
        "huile": "Arbre à Thé / Tea Tree", 
        "aromatiques": "Laurier noble, Coriandre en graines, Curcuma",
        "zikr": "Ya Hafiz (Ô Protecteur Suprême) — 998 fois + Nom Salomonique : JEHOVAH JIREH",
        "priere_salomonique": "Pourvoyeur Universel, JEHOVAH JIREH, Toi qui ordonnes à Tes légions d'Anges d'escorter les pas des Justes. Déploie Tes sentinelles de prospérité autour de mes finances. Scelle mes coffres, fructifie mon travail et attire à moi l'abondance. Amen.",
        "mots_application": "Que la prospérité future promise par ce thème soit scellée et divinement protégée. Amen.", "moment": "Matin",
        "savon_additifs": "Graines de coriandre pilées et une cuillère à café de poudre de laurier noble pour sceller les gains."
    },
    "Mori Sumana": {
        "ref": "Mori Sumana", "code": (2, 2, 1, 1), "nature": "Bénéfique", "element": "Vent",
        "maison_repos": 15, "nom_maison_repos": "M15 (Conclusion générale)", "plante": "Doualé",
        "txt": "Maison de la conclusion du thème, du résumé général des affaires, du bilan et de l'environnement final.",
        "psaume": "Psaume 119", "verset": "Verset 105", 
        "texte_biblique": "Ta parole est une lampe à mes pieds, et une lumière sur mon sentier.",
        "zikr_verset": "Réciter le Verset 105 du Psaume 119 exactement 150 fois le soir pour obtenir une illumination intérieure ou dénouer un problème complexe.",
        "repetitions": "150",
        "bain_preparation": "Infuser des feuilles de Doualé avec des larmes de résine pure d'Oliban dans de l'eau tiède.",
        "bain_posologie": "Bain de synthèse finale à prendre pendant 3 soirs d'affilée pour clore heureusement une affaire en cours et éclairer vos choix de vie.",
        "huile": "Encens d'Oliban", 
        "aromatiques": "Résine d'Oliban, Fleurs de Jasmin séchées, Poudre de Safran",
        "zikr": "Ya Alim (Ô Omniscient) — 150 fois + Nom Salomonique : TETRAGRAMMATON",
        "priere_salomonique": "Sagesse Suprême, TETRAGRAMMATON Ineffable, dont le Verbe Sacré est une lampe infaillible à mes pieds. Toi qui connais la fin avant le commencement, illumine l'issue de mon thème et de ma vie. Que Ta vérité triomphe de toute illusion. Amen.",
        "mots_application": "Que la lumière parfaite éclaire la conclusion de mes démarches et m'apporte la réussite globale. Amen.", "moment": "Soir",
        "savon_additifs": "Grains de résine d'oliban réduits en poussière microscopique et fleurs de jasmin émiettées."
    },
    "Jamati Moussa": {
        "ref": "Jamati Moussa", "code": (2, 1, 2, 1), "nature": "Neutre à Fort", "element": "Feu",
        "maison_repos": 16, "nom_maison_repos": "M16 (Le Décret / Confirmation)", "plante": "tomy bourou",
        "txt": "Maison du Décret de l'esprit, de la confirmation finale, de la sentence et de la haute précision.",
        "psaume": "Psaume 4", "verset": "Verset 7", 
        "texte_biblique": "Fais lever sur nous la lumière de ta face, ô Éternel !",
        "zikr_verset": "Réciter le Verset 7 du Psaume 4 exactement 166 fois pour sceller instantanément le travail géomantique.",
        "repetitions": "166",
        "bain_preparation": "Préparer une infusion forte de feuilles de Tomy bourou avec de la menthe poivrée fraîche.",
        "bain_posologie": "Prendre ce dernier bain de scellage le jeudi ou dimanche matin très tôt. Il permet de matérialiser les réponses positives et d'accélérer les signatures de contrats.",
        "huile": "Orange Douce", 
        "aromatiques": "Zestes de Citron vert, Feuilles de Menthe, Cannelle",
        "zikr": "Ya Sari'u (Ô Rapide) — 202 fois + Nom Salomonique : SCHEMHAMPHORASCH",
        "priere_salomonique": "Par le Grand Nom Sacré et Vibrant SCHEMHAMPHORASCH, Toi le Maître des décrets foudroyants et de la justice immédiate. Fais luire l'éclair de Ta face sur mon destin. Que Ta sentence brise le retard chronique, valide mes requêtes et scelle ce travail. Amen.",
        "mots_application": "Que le décret final de cette consultation s'exécute en ma faveur avec force et rapidité. Amen.", "moment": "Matin",
        "savon_additifs": "Poudre fine de cannelle et feuilles de menthe séchées broyées pour accélérer les décrets."
    }
}

MAISONS_NOMINATIVES = {
    1: "M1 (Demandeur)", 2: "M2 (Biens/Chances)", 3: "M3 (Entourage)", 4: "M4 (Foyer/Patrimoine)",
    5: "M5 (Enfants/Nouvelles)", 6: "M6 (Maladies)", 7: "M7 (Adversaires/Époux)", 8: "M8 (Mort/Peurs)",
    9: "M9 (Voyages)", 10: "M10 (Travail/Autorité)", 11: "M11 (Espoirs)", 12: "M12 (Difficultés)",
    13: "M13 (Témoin Droite)", 14: "M14 (Témoin Gauche)", 15: "M15 (Conclusion)", 16: "M16 (Le Décret)"
}

# ==============================================================================
# FONCTIONS DE CALCULS GÉOMANTIQUES
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

def interpreter_passation(nom_figure, maison_actuelle):
    maison_repos = DATA[nom_figure]["maison_repos"]
    nom_maison_repos = DATA[nom_figure]["nom_maison_repos"]
    plante_associee = DATA[nom_figure]["plante"]
    
    if maison_repos == maison_actuelle:
        return f"✨ **La figure est chez elle (Maison de Repos originelle).** Ses vibrations et sa plante native (**{plante_associee}**) agissent à leur plein potentiel natif."
    else:
        return f"🔄 **Passation Métaphysique :** La figure originelle de *{nom_maison_repos}* a migré vers la **Maison {maison_actuelle} ({MAISONS_NOMINATIVES[maison_actuelle]})**. Elle transfère l'influence de sa plante native **{plante_associee}** pour colorer la Maison {maison_actuelle}."

# ==============================================================================
# INTERFACE UTILISATEUR STREAMLIT
# ==============================================================================
st.title("🔮 Plateforme Théurgique de Géomancie et d'Interprétation au Repos")
st.write("Dressez votre thème. Utilisez l'onglet adapté selon votre besoin d'analyse.")

with st.sidebar:
    st.header("🔐 Accès au Temple")
    u_id = st.text_input("Identifiant")
    u_pw = st.text_input("Mot de passe", type="password")

if u_id == ID_SECRET and u_pw == MDP_SECRET:
    st.success("🔓 Outils géomantiques actifs.")
    
    # CRÉATION DE DEUX ONGLETS EXTÊMEMENT CLAIRS ET SÉPARÉS
    tab_mode_mres, tab_mode_complet = st.tabs([
        "🌿 MODE STANDARD : Saisie des 4 Mères", 
        "✍️ MODE EXPERT : Saisie des 16 Figures (Thème complet)"
    ])
    
    options_figures = list(DATA.keys())
    theme_complet = {}

    # --------------------------------------------------------------------------
    # ONGLET 1 : SAISIE VIA LES 4 MÈRES UNIQUEMENT
    # --------------------------------------------------------------------------
    with tab_mode_mres:
        st.subheader("Entrez uniquement les 4 premières Mères")
        st.write("Le système va calculer algorithmiquement le reste des 12 maisons.")
        
        c1, col2, col3, col4 = st.columns(4)
        with c1: m1 = st.selectbox("🏠 M1 (Première Mère)", options_figures, index=0, key="std_m1")
        with col2: m2 = st.selectbox("🏠 M2 (Deuxième Mère)", options_figures, index=1, key="std_m2")
        with col3: m3 = st.selectbox("🏠 M3 (Troisième Mère)", options_figures, index=2, key="std_m3")
        with col4: m4 = st.selectbox("🏠 M4 (Quatrième Mère)", options_figures, index=3, key="std_m4")

        # Calcul algorithmique automatique
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

        theme_standard = {
            1: m1, 2: m2, 3: m3, 4: m4, 5: m5, 6: m6, 7: m7, 8: m8,
            9: m9, 10: m10, 11: m11, 12: m12, 13: m13, 14: m14, 15: m15, 16: m16
        }

    # --------------------------------------------------------------------------
    # ONGLET 2 : LE VÉRITABLE ESPACE COMPLET POUR VOS 16 FIGURES
    # --------------------------------------------------------------------------
    with tab_mode_complet:
        st.subheader("Entrez manuellement les 16 figures de votre thème tracé")
        st.warning("Ce mode désactive le calcul automatique et respecte STRICTEMENT vos attributions personnalisées.")
        
        st.markdown("#### ⚜️ Mères Fondamentales (1 à 4)")
        cx1, cx2, cx3, cx4 = st.columns(4)
        f1 = cx1.selectbox("🏠 Maison 1 (Demandeur)", options_figures, index=0, key="exp_m1")
        f2 = cx2.selectbox("🏠 Maison 2 (Argent)", options_figures, index=1, key="exp_m2")
        f3 = cx3.selectbox("🏠 Maison 3 (Entourage)", options_figures, index=2, key="exp_m3")
        f4 = cx4.selectbox("🏠 Maison 4 (Foyer)", options_figures, index=3, key="exp_m4")

        st.markdown("#### 🌿 Filles (5 à 8)")
        cx5, cx6, cx7, cx8 = st.columns(4)
        f5 = cx5.selectbox("🏠 Maison 5 (Enfants)", options_figures, index=4, key="exp_m5")
        f6 = cx6.selectbox("🏠 Maison 6 (Maladies)", options_figures, index=5, key="exp_m6")
        f7 = cx7.selectbox("🏠 Maison 7 (Union/Rivaux)", options_figures, index=6, key="exp_m7")
        f8 = cx8.selectbox("🏠 Maison 8 (Blocages/Peur)", options_figures, index=7, key="exp_m8")

        st.markdown("#### ⚡ Neveux (9 à 12)")
        cx9, cx10, cx11, cx12 = st.columns(4)
        f9 = cx9.selectbox("🏠 Maison 9 (Spiritualité)", options_figures, index=8, key="exp_m9")
        f10 = cx10.selectbox("🏠 Maison 10 (Travail)", options_figures, index=9, key="exp_m10")
        f11 = cx11.selectbox("🏠 Maison 11 (Espoirs)", options_figures, index=10, key="exp_m11")
        f12 = cx12.selectbox("🏠 Maison 12 (Ennemis)", options_figures, index=11, key="exp_m12")

        st.markdown("#### ⚖️ Tribunal et Décret (13 à 16)")
        cx13, cx14, cx15, cx16 = st.columns(4)
        f13 = cx13.selectbox("🏠 Maison 13 (Témoin D.)", options_figures, index=12, key="exp_m13")
        f14 = cx14.selectbox("🏠 Maison 14 (Témoin G.)", options_figures, index=13, key="exp_m14")
        f15 = cx15.selectbox("🏠 Maison 15 (Le Juge)", options_figures, index=14, key="exp_m15")
        f16 = cx16.selectbox("🏠 Maison 16 (Le Décret)", options_figures, index=15, key="exp_m16")

        theme_expert = {
            1: f1, 2: f2, 3: f3, 4: f4, 5: f5, 6: f6, 7: f7, 8: f8,
            9: f9, 10: f10, 11: f11, 12: f12, 13: f13, 14: f14, 15: f15, 16: f16
        }

    # SELECTION DU THÈME À TRAITER SELON L'ONGLET REQUIS
    # Nous détectons si l'utilisateur est sur l'onglet expert ou standard via un bouton d'activation
    st.markdown("---")
    st.header("⚙️ ACTIONNEZ LE TRAITEMENT")
    choix_final = st.checkbox("🔥 Cliquer ici pour VALIDER et analyser les 16 figures renseignées ci-dessus", value=True)

    # Si la case est cochée, on regarde quel thème est actif
    # Par sécurité, si l'expert a modifié des valeurs dans l'onglet expert, on priorise le thème complet
    is_expert_modified = any(theme_expert[i] != options_figures[i-1] for i in range(1, 17))
    
    if is_expert_modified:
        theme_complet = theme_expert
        st.success("🎯 ANALYSE EN COURS : Thème Expert (16 Maisons personnalisées)")
    else:
        theme_complet = theme_standard
        st.info("📊 ANALYSE EN COURS : Thème Standard (Calculé automatiquement)")

    # ==============================================================================
    # VISUALISATION DES 16 MAISONS RETENUES
    # ==============================================================================
    with st.container(border=True):
        st.subheader("🖼️ CARTOGRAPHIE SYNTHÉTIQUE DU THÈME RETENU")
        
        c_l1, c_l2, c_l3, c_l4 = st.columns(4)
        c_l1.metric("M1 (Demandeur)", theme_complet[1])
        c_l2.metric("M2 (Argent)", theme_complet[2])
        c_l3.metric("M3 (Relations)", theme_complet[3])
        c_l4.metric("M4 (Foyer)", theme_complet[4])
        
        c_l5, c_l6, c_l7, c_l8 = st.columns(4)
        c_l5.metric("M5 (Enfants)", theme_complet[5])
        c_l6.metric("M6 (Maladies)", theme_complet[6])
        c_l7.metric("M7 (Alliances)", theme_complet[7])
        c_l8.metric("M8 (Obstacles)", theme_complet[8])

        c_l9, c_l10, c_l11, c_l12 = st.columns(4)
        c_l9.metric("M9 (Spiritualité)", theme_complet[9])
        c_l10.metric("M10 (Carrière)", theme_complet[10])
        c_l11.metric("M11 (Vœux)", theme_complet[11])
        c_l12.metric("M12 (Difficultés)", theme_complet[12])

        c_l13, c_l14, c_l15, c_l16 = st.columns(4)
        c_l13.warning(f"M13 (Témoin D.) : {theme_complet[13]}")
        c_l14.warning(f"M14 (Témoin G.) : {theme_complet[14]}")
        c_l15.error(f"M15 (Le Juge) : {theme_complet[15]}")
        c_l16.success(f"M16 (Le Décret) : {theme_complet[16]}")

    # ==============================================================================
    # DÉPLOIEMENT DU DICTIONNAIRE ET DES INSTRUCTIONS DE SAVONS
    # ==============================================================================
    st.markdown("---")
    st.header("📖 DICTIONNAIRE THÉRAPEUTIQUE, RECETTES DE BAINS ET SAVONS ARTISANAUX")
    
    for m, fig_choisie in theme_complet.items():
        bloc = DATA[fig_choisie]
        statut_action = "🛑 SECTEUR CRITIQUE" if "Mauvais" in bloc["nature"] else "✨ SECTEUR HARMONIEUX"
        titre_boite = f"{MAISONS_NOMINATIVES[m]} ➔ Figure : {fig_choisie} [{statut_action}]"
        
        with st.expander(titre_boite):
            tab_passation, tab_verset, tab_bain, tab_savon = st.tabs([
                "🔄 Analyse de Passation", 
                "📿 Zikr du Verset Biblique", 
                "🌿 Recette de Bain & Posologie",
                "🧼 Fabrication du Savon Rituel"
            ])
            
            with tab_passation:
                st.info(interpreter_passation(fig_choisie, m))
                st.markdown(f"**Signification originelle au Repos :** *{bloc['txt']}*")
                
            with tab_verset:
                st.markdown(f"### 📿 Protocole de Récitation du Verset Sacré ({bloc['psaume']})")
                st.info(f"**Verset :** *\"{bloc['texte_biblique']}\"* ({bloc['psaume']}, {bloc['verset']})")
                st.warning(f"**Méthode de Zikr :** {bloc['zikr_verset']}")
                st.write(f"**Zikr additionnel :** {bloc['zikr']}")
                st.caption(f"⏱️ **Moment idéal :** {bloc['moment']}")
                
            with tab_bain:
                st.markdown(f"### 🌱 Préparation du Bain Spirituel ({bloc['plante']})")
                st.write(f"**Plante maîtresse :** **{bloc['plante']}**, Compléments : *{bloc['aromatiques']}*.")
                st.success(f"🥣 **Préparation :** {bloc['bain_preparation']}")
                st.error(f"📋 **Application :** {bloc['bain_posologie']}")
                
            with tab_savon:
                st.markdown("### 🧼 Fabrication et Consécration du Savon Thérapeutique")
                col_g, col_d = st.columns(2)
                with col_g:
                    st.markdown("**1. Ingrédients pour la base :**")
                    st.write("- **500g de base neutre :** Savon de Marseille blanc ou Savon Noir.")
                    st.write(f"- **Liquide :** Décoction ultra-concentrée de **{bloc['plante']}**.")
                with col_d:
                    st.markdown("**2. Additifs aromatiques :**")
                    st.write(f"- **Éléments :** {bloc['savon_additifs']}")
                    st.write(f"- **Huile :** 15 gouttes d'huile essentielle de **{bloc['huile']}**.")
                
                st.warning(f"🔮 **Consécration :**\n"
                           f"Une fois sec, faites le zikr du **{bloc['psaume']}** exactement **{bloc['repetitions']} fois** directement sur le savon pour figer la charge.")
                st.write(f"📋 **Formule d'activation :** *\"{bloc['mots_application']}\"*.")
else:
    st.warning("🔒 Système Verrouillé. Veuillez inscrire vos identifiants à gauche pour accéder au Temple géomantique.")
