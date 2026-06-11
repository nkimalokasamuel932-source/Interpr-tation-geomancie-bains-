import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Système Théurgique Expert Pro", page_icon="🔮", layout="wide")

# ==============================================================================
# ACCÈS SÉCURISÉS
# ==============================================================================
ID_SECRET = "theurge2026"
MDP_SECRET = "Salomon777"

# ==============================================================================
# MATRICE ENRICHIE DES 16 FIGURES GÉOMANTIQUES ET RITUELS THÉURGIQUES
# ==============================================================================
DATA = {
    "Youssouf (Dianfa Almami)": {
        "ref": "Youssouf (Dianfa Almami)", "code": (1, 2, 1, 1), "nature": "Bénéfique", "element": "Feu", "direction": "Est",
        "txt": "Maison du demandeur par extension l'esprit, l'âme et la conscience primordiale.",
        "psaume": "Psaume 20", "nb_ecriture": 7, "verset": "Verset 5", 
        "texte_biblique": "Qu'il te donne ce que ton cœur désire, et qu'il accomplisse tous tes desseins !",
        "vibratoire": "Émet un rayonnement doré de type solaire qui restructure l'aura, dissipe les miasmes du doute et aligne le corps éthérique avec la volonté divine. Elle amplifie le magnétisme personnel.",
        "avantages": "Restauration immédiate de l'autorité intérieure, clarté mentale absolue face aux choix de vie, effacement des mémoires de stagnation, et attraction spontanée de la bienveillance d'autrui.",
        "huile": "Laurier Noble (Victoire et clarté spirituelle)", 
        "aromatiques": "Feuilles de Laurier sauce, Menthe poivrée fraîche, Safran pur en filaments (Teinture de l'âme)",
        "zikr": "Ya Wahhab (Ô Donateur Suprême) — 14 fois + Nom Salomonique : EHIEH ASHER EHIEH",
        "priere_salomonique": "Par la puissance de la Couronne Suprême et le Nom Ineffable EHIEH ASHER EHIEH, Éternel des Armées, j'invoque Ton rayonnement sur mon âme. Brise les verrous de mon esprit, enflamme mon aura de Ta lumière inextinguible et accorde-moi la victoire sur mes propres ombres. Que Ta grâce divine manifeste les désirs purs de mon cœur et que mes desseins s'accomplissent selon Ton ordre universel. Amen.",
        "mots_application": "Que mon âme soit purifiée et que les intentions de ce thème reçoivent la clarté et le succès divin. Amen.", "moment": "Matin au lever"
    },
    "Adam (Adama)": {
        "ref": "Adam (Adama)", "code": (1, 1, 1, 1), "nature": "Bénéfique", "element": "Feu", "direction": "Est",
        "txt": "Maison des biens, des finances, des flux de matière et des énergies créatrices.",
        "psaume": "Psaume 8", "nb_ecriture": 8, "verset": "Verset 6", 
        "texte_biblique": "Tu lui as donné l'empire sur les œuvres de tes mains, tu as tout mis sous ses pieds.",
        "vibratoire": "Fréquence d'expansion terrestre accélérée. Brise la cristallisation astrale de la pauvreté et réactive le canal géocentrique d'attraction de l'or. Elle harmonise le chakra racine avec la structure matérielle.",
        "avantages": "Manifestation de ressources financières inattendues, déblocage des affaires commerciales en perte, obtention d'opportunités lucratives de premier ordre et souveraineté matérielle retrouvée.",
        "huile": "Cèdre de l'Atlas (Ancrage et prospérité royale)", 
        "aromatiques": "Basilic sacré (Tulsi), Romarin officinal, Curcuma en poudre pure (Teinture d'Or)",
        "zikr": "Ya Rafi'u (Ô Celui qui élève) — 351 fois + Nom Salomonique : ADONAI MELEKH",
        "priere_salomonique": "Ô Seigneur Souverain, Roi de la Terre, ADONAI MELEKH, Toi qui as façonné l'homme de poussière et d'esprit et l'as couronné de gloire. Par cette onction et ce bain de feu, confère-moi l'empire légitime sur la matière. Éloigne de mes mains le spectre du manque. Que l'abondance infinie se prosterne à mes pieds et que les trésors cachés de la création se manifestent pour l'accomplissement de mon œuvre. Amen.",
        "mots_application": "Que l'abondance matérielle, la chance et l'élévation financière s'installent durablement dans ma vie. Amen.", "moment": "Matin"
    },
    "Mahdiou (Malejou)": {
        "ref": "Mahdiou (Malejou)", "code": (1, 1, 1, 2), "nature": "Neutre", "element": "Vent", "direction": "Sud",
        "txt": "Maison de la communication, de la fratrie, des alliés immédiats et du réseau relationnel.",
        "psaume": "Psaume 4", "nb_ecriture": 3, "verset": "Verset 7", 
        "texte_biblique": "Fais lever sur nous la lumière de ta face, ô Éternel !",
        "vibratoire": "Onde de fluidisation éthérique. Elle balaye les énergies stagnantes de la médisance, dissout les quiproquos dans l'astral relationnel et adoucit le corps émotionnel pour favoriser la diplomatie.",
        "avantages": "Pacification des tensions de voisinage ou de bureau, retour d'ascenseur rapide de la part de partenaires, charisme de communication lors de prises de parole ou de négociations cruciales.",
        "huile": "Orange Douce (Harmonie et joie relationnelle)", 
        "aromatiques": "Zestes d'Orange douce, Menthe douce en feuilles, Écorce de Cannelle grossière",
        "zikr": "Ya Nour (Ô Lumière) — 256 fois + Nom Salomonique : ELOHIM SABAOTH",
        "priere_salomonique": "Souverain des Armées Célestes, ELOHIM SABAOTH, Source éternelle de concorde et de lumière. Que la splendeur sacrée de Ta Face descende sur mon cercle social et familial. Purifie ma langue de toute parole amère, dissout la haine ou la jalousie secrète de mon entourage. Fais de moi un canal de paix magnétique afin que tous ceux qui m'approchent soient saisis par Ta bienveillance. Amen.",
        "mots_application": "Que la concorde et la paix illuminent mes relations avec mon entourage et ma famille. Amen.", "moment": "Matin"
    },
    "Idriss (Albayada)": {
        "ref": "Idriss (Albayada)", "code": (2, 2, 1, 2), "nature": "Bénéfique", "element": "Eau", "direction": "Nord",
        "txt": "Maison des fondations, du patrimoine immobilier, du foyer originel et du sol natal.",
        "psaume": "Psaume 112", "nb_ecriture": 4, "verset": "Verset 3", 
        "texte_biblique": "Il a dans sa maison bien-être et richesse, et sa justice subsiste à jamais.",
        "vibratoire": "Fréquence de cristallisation lunaire blanche très pure. Elle agit comme un bouclier d'argent imperméable autour des habitations, nettoyant les murs des mémoires de deuil ou d'échec.",
        "avantages": "Facilitation des transactions immobilières (achats, ventes, héritages), ancrage durable de la paix sous le toit familial, protection totale contre les intrusions malveillantes ou le vandalisme occulte.",
        "huile": "Patchouli (Attraction terrestre et matérialisation)", 
        "aromatiques": "Bâtons de Cannelle concassés, Clous de Girofle entiers, Curcuma de Madagascar",
        "zikr": "Ya Razzaq (Ô Pourvoyeur) — 308 fois + Nom Salomonique : SHADDAI EL CHAI",
        "priere_salomonique": "Principe Vivant et Tout-Puissant, SHADDAI EL CHAI, Fondement inébranlable des siècles. J'invoque Ta bénédiction sur ma demeure et mon sang. Que Tes Gardiens de l'Est et de l'Ouest scellent les portes de ma maison. Fais couler le fleuve du bien-être et de la richesse intarissable dans mon foyer. Que le vice en soit chassé et que Ta justice y règne éternellement comme un phare de paix. Amen.",
        "mots_application": "Que la stabilité, le bien-être et la richesse s'ancrent au cœur de mon foyer. Amen.", "moment": "Matin"
    },
    "Ibrahim (Târiki)": {
        "ref": "Ibrahim (Târiki)", "code": (1, 1, 2, 1), "nature": "Bénéfique", "element": "Eau", "direction": "Nord",
        "txt": "Maison de la créativité, de la progéniture, des plaisirs sains et des messages entrants.",
        "psaume": "Psaume 100", "nb_ecriture": 5, "verset": "Verset 2", 
        "texte_biblique": "Servez l'Éternel avec joie, venez avec allégresse en sa présence !",
        "vibratoire": "Onde hautement joyeuse, pétillante et régénératrice. Elle dissout la mélancolie chronique, purifie les canaux reproducteurs et émet un signal de réceptivité aux événements heureux.",
        "avantages": "Arrivée de bonnes nouvelles inattendues par courrier ou téléphone, déblocage des blocages liés à la fertilité ou aux enfants, regain d'inspiration artistique ou entrepreneuriale majeure.",
        "huile": "Pamplemousse (Énergie positive et renouveau)", 
        "aromatiques": "Verveine odorante, Citronnelle en tiges fraîches, Pistils de Safran royal",
        "zikr": "Ya Latif (Ô Doux) — 129 fois + Nom Salomonique : YHVH SABAOTH",
        "priere_salomonique": "Seigneur Souverain de l'Allégresse, YHVH SABAOTH, dont la douceur s'étend sur toute créature. Permets que Ton parfum de joie pénètre mon temple corporel à travers ces plantes sacrées. Chasse la tristesse stérile qui attire l'ombre. Fais lever sur ma vie des messages de triomphe, accorde la protection à ma lignée et permets-moi d'avancer en Ta sainte présence le cœur léger et victorieux. Amen.",
        "mots_application": "Que les nouvelles qui me parviennent apportent la joie, la réussite et l'allégresse. Amen.", "moment": "Matin"
    },
    "Issa (Ngansa)": {
        "ref": "Issa (Ngansa)", "code": (2, 2, 2, 2), "nature": "Neutre à Mauvais", "element": "Eau", "direction": "Nord",
        "txt": "Maison du corps physique, des infirmités cachées, des servitudes et du nettoyage de fond.",
        "psaume": "Psaume 51", "nb_ecriture": 1, "verset": "Verset 12", 
        "texte_biblique": "Ô Dieu ! crée en moi un cœur pur, renouvelle en moi un esprit bien disposé.",
        "vibratoire": "Vibration de transmutation radicale, s'apparentant au feu blanc alchimique. Elle agit directement au niveau cellulaire pour purger les poisons physiques, psychiques et karmiques accumulés.",
        "avantages": "Soulagement drastique des douleurs chroniques inexpliquées, expulsion des entités larvaires nichées dans l'astral inférieur du consultant, rupture définitive des liens de soumission psychologique.",
        "huile": "Lavande Vraie (Purification absolue des corps subtils)", 
        "aromatiques": "Fleurs de Lavande séchées, Camomille matricaire, Poudre de Santal Blanc de Mysore",
        "zikr": "Ya Chafi (Ô Guérisseur) — 391 fois + Nom Salomonique : ELOHIM GIBOR",
        "priere_salomonique": "Principe de Justice et Fortresse Inflexible, ELOHIM GIBOR, Toi qui sondes les reins et les cœurs. Lave mon corps et mon âme des impuretés morales et physiques. Crée en moi un réceptacle immaculé. Par le pouvoir du Sang et du Feu de Ton Autel, calcine toute maladie occulte, brise les chaînes de la servitude psychique et redresse mon esprit afin que je serve Ta gloire sans fléchir. Amen.",
        "mots_application": "Purifie mon être de toute négativité, entrave ou influence maladive cachée. Amen.", "moment": "Soir"
    },
    "Oumar (Lomara)": {
        "ref": "Oumar (Lomara)", "code": (2, 1, 2, 2), "nature": "Mauvais", "element": "Vent", "direction": "Sud",
        "txt": "Maison des conflits ouverts, des procès, de l'adversité déclarée et des ruptures d'alliances.",
        "psaume": "Psaume 35", "nb_ecriture": 7, "verset": "Verset 1", 
        "texte_biblique": "Éternel ! Attaque ceux qui m'attaquent, combats ceux qui me combattent !",
        "vibratoire": "Fréquence martienne ultra-violente de destruction des obstacles. Elle sature le champ aurique d'une barrière d'épines de feu rouge, retournant instantanément les attaques à l'envoyeur.",
        "avantages": "Gains de procès complexes, destruction des complots ourdis dans le secret professionnel, paralysie des actions de vos ennemis visibles et invisibles, fin des persécutions.",
        "huile": "Cannelle Écorce (Feu purificateur de combat)", 
        "aromatiques": "Poivre noir en grains, Thym fort, Ortie piquante, Gingembre rouge émincé",
        "zikr": "Ya Jabbar (Ô Contraignant) — 206 fois + Nom Salomonique : ELOHIM GIBOR",
        "priere_salomonique": "Juge Terrible des Oppresseurs, ELOHIM GIBOR, Puissance des vengeances légitimes. Tire Ton épée flamboyante et dresse Ton bouclier devant mes pas. Combat ceux qui cherchent ma ruine, terrasse les esprits de discorde qui s'attaquent à mon nom ou mon foyer. Que la confusion s'abatte sur mes adversaires, qu'ils reculent comme la paille devant le vent, brisés par Ton décret souverain. Amen.",
        "mots_application": "Que toute opposition, conflit ou rivalité se brise face à la justice divine. Amen.", "moment": "Soir (Ne pas s'essuyer)"
    },
    "Ayoube (Mankoussi)": {
        "ref": "Ayoube (Mankoussi)", "code": (2, 2, 2, 1), "nature": "Mauvais", "element": "Terre", "direction": "Ouest",
        "txt": "Maison de l'angoisse profonde, des héritages complexes, des blocages de la mort symbolique.",
        "psaume": "Psaume 142", "nb_ecriture": 9, "verset": "Verset 8", 
        "texte_biblique": "Tire mon âme de sa prison, afin que je célèbre ton nom !",
        "vibratoire": "Onde de désintégration tellurique lourde. Elle pénètre l'inconscient pour broyer les miasmes de la dépression, libérer les nœuds ancestraux et lever les malédictions liées à la terre.",
        "avantages": "Extraction immédiate des états de dépression ou d'angoisse paralysante, déblocage des successions notariales gelées depuis des années, libération des prisons physiques ou psychologiques.",
        "huile": "Cyprès de Provence (Libération et passage des blocages)", 
        "aromatiques": "Sauge officinale, Racine de Gingembre frais écrasée, Charbon béni en poudre",
        "zikr": "Ya Moukhrij (Ô Celui qui fait sortir) — 201 fois + Nom Salomonique : AGLA",
        "priere_salomonique": "Souverain Éternel, Force immuable, AGLA (Ate Geber Leilam Adonai), Toi qui as les clés des abîmes et de la vie. Entends mon cri du fond de la fosse. Brise les portes d'airain et les verrous de fer de ma prison existentielle. Tire mon âme des ténèbres de l'angoisse, déracine la malédiction du manque et fais-moi remonter vers la lumière des vivants pour magnifier Ton Nom Sacré. Amen.",
        "mots_application": "Je me libère des angoisses, des blocages et de toute forme d'enfermement matériel ou spirituel. Amen.", "moment": "Soir"
    },
    "Allahou talla (Kalalaw)": {
        "ref": "Allahou talla (Kalalaw)", "code": (1, 2, 2, 1), "nature": "Bénéfique", "element": "Feu", "direction": "Est",
        "txt": "Maison des horizons lointains, des voyages physiques, spirituels et de l'élévation philosophique.",
        "psaume": "Psaume 133", "nb_ecriture": 3, "verset": "Verset 1", 
        "texte_biblique": "Voici, qu'il est agréable, qu'il est doux pour des frères de demeurer ensemble !",
        "vibratoire": "Fréquence d'attraction par harmonie harmonique supérieure. Elle syntonise l'aura sur le canal des maîtres spirituels et des guides de lumière, ouvrant les routes barrées à l'international.",
        "avantages": "Obtention simplifiée de visas, bourses d'études ou contrats à l'étranger, déblocage des voyages contrariés, éveil fulgurant des capacités de clairvoyance et d'intuition.",
        "huile": "Ylang-Ylang (Attraction, charisme et union)", 
        "aromatiques": "Pétales de Rose de Damas, Anis étoilé (Badiane), Safran odorant pur",
        "zikr": "Ya Wadoud (Ô Aimant) — 20 fois + Nom Salomonique : EL GOLAH",
        "priere_salomonique": "Souverain Miséricordieux des Univers, EL GOLAH, Source de l'Amour universel et des voies d'ouverture. Que Ton Souffle sacré dissipe les nuages de l'isolement sur mes chemins. Ouvre grand les portes des contrées lointaines, connecte mon esprit aux alliances nobles et bienveillantes à travers le monde. Que chacun de mes pas soit guidé par Tes émissaires de paix. Amen.",
        "mots_application": "Que mes routes et mes déplacements créent des alliances heureuses et fructueuses. Amen.", "moment": "Matin"
    },
    "Souleymane (Mansa Solomani)": {
        "ref": "Souleymane (Mansa Solomani)", "code": (2, 1, 1, 2), "nature": "Bénéfique", "element": "Terre", "direction": "Ouest",
        "txt": "Maison de la carrière, du statut social, de la gloire, de la royauté individuelle et de l'honneur.",
        "psaume": "Psaume 45", "nb_ecriture": 10, "verset": "Verset 2", 
        "texte_biblique": "Des paroles pleines de charme bouillonnent dans mon cœur. Je dis : Mon œuvre est pour le roi !",
        "vibratoire": "Émission d'un champ géomagnétique impérial pourpre et or. Écrase le mépris des autres, impose le respect immédiat et active les décrets de promotion sociale au niveau administratif.",
        "avantages": "Promotions fulgurantes en entreprise, élection à des postes de haute responsabilité, obtention de marchés publics majeurs, protection totale du prestige contre la calomnie.",
        "huile": "Géranium Bourbon (Magnétisme professionnel et éclat)", 
        "aromatiques": "Feuilles de Géranium odorant, Marjolaine séchée, Poudre de Curcuma pur",
        "zikr": "Ya Jamil (Ô Beau) — 83 fois + Nom Salomonique : ADONAI TZABAOTH",
        "priere_salomonique": "Roi des Rois, Souverain de l'Ordre Cosmique, ADONAI TZABAOTH, Toi qui as accordé la Sagesse et la Magnificence suprême au Roi Salomon. Revêts-moi aujourd'hui de Ton manteau de majesté, de charisme et d'autorité incontestable. Que mes paroles captivent les puissants, que mes œuvres soient couronnées de succès et que mon nom soit élevé pour le bien commun et la gloire de Ton trône céleste. Amen.",
        "mots_application": "Accorde-moi le charisme, le respect et l'autorité morale nécessaires dans mes entreprises et mon travail. Amen.", "moment": "Matin"
    },
    "Ali (Badara Aliou)": {
        "ref": "Ali (Badara Aliou)", "code": (2, 1, 1, 1), "nature": "Bénéfique", "element": "Vent", "direction": "Sud",
        "txt": "Maison des espoirs secrets, des protections providentielles et des soutiens financiers majeurs.",
        "psaume": "Psaume 144", "nb_ecriture": 11, "verset": "Verset 1", 
        "texte_biblique": "Béni soit l'Éternel, mon rocher, qui exerce mes mains au combat, mes doigts à la bataille !",
        "vibratoire": "Onde de foudre spirituelle purificatrice. Elle recharge les réserves d'énergie vitale en quelques secondes, redonne une foi de plomb et détruit le doute instillé par les entités négatives.",
        "avantages": "Manifestation de mécènes ou de protecteurs financiers puissants, réalisation concrète de projets jugés impossibles ou utopiques, immunité face aux attaques de découragement.",
        "huile": "Gingembre Bleu (Force, dynamisme et courage)", 
        "aromatiques": "Graines de Cardamome craquées, Menthe des champs, Poudre fine de Gingembre",
        "zikr": "Ya Qawiyyou (Ô Fort Invincible) — 116 fois + Nom Salomonique : EL SHADDAI",
        "priere_salomonique": "Principe Fort et Invincible, EL SHADDAI, mon Rocher et mon rempart indéfectible. Exerce mon âme à la maîtrise des lois de la vie. Injecte Ton feu de courage au plus profond de mes os. Que mes vœux pieux se transforment en décrets de matière, et que l'appui des puissants de ce monde me soit accordé de plein droit sous Ton aile protectrice. Amen.",
        "mots_application": "Que mes espérances les plus profondes soient fortifiées et protégées contre tout obstacle. Amen.", "moment": "Matin"
    },
    "Nouhou (Nounkoro)": {
        "ref": "Nouhou (Nounkoro)", "code": (1, 2, 2, 2), "nature": "Mauvais", "element": "Terre", "direction": "Ouest",
        "txt": "Maison des grands obstacles structurels, de la haine secrète, des blocages karmiques et des complots.",
        "psaume": "Psaume 30", "nb_ecriture": 12, "verset": "Verset 12", 
        "texte_biblique": "Tu as changé mon deuil en allégresse, tu as délié mon sac, et tu m'as ceint de joie.",
        "vibratoire": "Onde de submersion divine (L'Arche du Salut). Elle noie littéralement les entités négatives et les pièges magiques sous un flot d'énergie baptismale éthérique de très haute fréquence.",
        "avantages": "Brise net les envoûtements familiaux ancestraux, transmutation instantanée d'une période de ruine ou de deuil en opportunité de richesse, libération définitive des pièges cachés.",
        "huile": "Citronnelle Java (Nettoyage des ondes lourdes)", 
        "aromatiques": "Tiges de Citronnelle fraîches émincées, Thym blanc, Estragon, Clou de Girofle pilé",
        "zikr": "Ya Latif (Ô Bienveillant) — 129 fois + Nom Salomonique : IAH",
        "priere_salomonique": "Souverain Absolu du Salut, Nom Sublime IAH, Toi qui as sauvé Noé des eaux du déluge et changé le deuil des justes en allégresse céleste. Abaisse Ton regard sur mes afflictions. Déchire le sac de mes difficultés, détruis les complots des esprits ténébreux tapis dans l'ombre et ceins mes reins d'un manteau de joie pure et d'immunité totale. Amen.",
        "mots_application": "Que tous les pièges de l'ombre soient déracinés et dissous, laissant place au triomphe. Amen.", "moment": "Soir"
    },
    "Houssaini (Ioussiné)": {
        "ref": "Houssaini (Ioussiné)", "code": (1, 1, 2, 2), "nature": "Neutre", "element": "Eau", "direction": "Nord",
        "txt": "Maison de la situation immédiate, des secrets du lit, de la chambre à coucher et du moment présent.",
        "psaume": "Psaume 18", "nb_ecriture": 13, "verset": "Verset 38", 
        "texte_biblique": "Je les brise, et ils ne peuvent se relever ; ils tombent sous mes pieds.",
        "vibratoire": "Fréquence de stabilisation absolue du flux astral du lieu de sommeil. Elle neutralise instantanément les réseaux telluriques négatifs (Hartmann/Curry) et stoppe les incubes/succubes.",
        "avantages": "Sommeil réparateur profond, rêves prophétiques clairs, retour de l'harmonie sexuelle et affective dans le couple, clarification immédiate de la confusion mentale du consultant.",
        "huile": "Clou de Girofle (Scellage et protection du lieu)", 
        "aromatiques": "Feuilles d'Eucalyptus, Clous de girofle entiers, Écorce de cannelle royale",
        "zikr": "Ya Moumit (Ô Maître de la libération) — 490 fois + Nom Salomonique : ELOHIM",
        "priere_salomonique": "Maître Souverain du Temps et de l'Espace, ELOHIM Juste, Toi qui fixes les frontières du jour et de la nuit. Purifie mon sanctuaire intime, ma couche et mes pensées de toute souillure. Écrase sous mes talons les larves psychiques nocturnes. Que ma situation présente soit redressée par Ta puissance souveraine et que mes ennemis invisibles s'effondrent sans pouvoir se relever. Amen.",
        "mots_application": "Que ma situation actuelle soit clarifiée, purifiée et libérée des énergies stagnantes. Amen.", "moment": "Soir"
    },
    "Younouss (Tontigui)": {
        "ref": "Younouss (Tontigui)", "code": (1, 2, 1, 2), "nature": "Bénéfique", "element": "Terre", "direction": "Ouest",
        "txt": "Maison des gains massifs futures, de la chance financière imminente et du capital accumulé.",
        "psaume": "Psaume 91", "nb_ecriture": 14, "verset": "Verset 11", 
        "texte_biblique": "Car il ordonnera à ses anges de te garder dans toutes tes voies.",
        "vibratoire": "Onde de scellage angélique fortifiée (Fréquence de la crypte aux trésors). Elle aimante de manière irrésistible les métaux précieux et l'argent liquide vers l'escarcelle du consultant.",
        "avantages": "Rentrée d'argent majeure dans les 14 jours, protection des comptes bancaires contre les saisies ou dépenses imprévues, chance insolente aux jeux de hasard raisonnés ou investissements.",
        "huile": "Arbre à Thé / Tea Tree (Bouclier financier)", 
        "aromatiques": "Laurier noble séché, Coriandre en graines entières, Curcuma or de première quality",
        "zikr": "Ya Hafiz (Ô Protecteur Suprême) — 998 fois + Nom Salomonique : JEHOVAH JIREH",
        "priere_salomonique": "Pourvoyeur Universel, JEHOVAH JIREH, Toi qui ordonnes à Tes légions d'Anges d'escorter les pas des Justes. Déploie Tes sentinelles de prospérité autour de mes finances. Scelle mes coffres, fructifie mon travail et attire à moi l'abondance qui m'est divinement due. Que Ta garde angélique me préserve du vol occulte et de la ruine soudaine. Amen.",
        "mots_application": "Que la prospérité future promise par ce thème soit scellée et divinement protégée. Amen.", "moment": "Matin"
    },
    "Ousmane (Mori Zoumana)": {
        "ref": "Ousmane (Mori Zoumana)", "code": (2, 2, 1, 1), "nature": "Bénéfique", "element": "Vent", "direction": "Sud",
        "txt": "Maison de la conclusion globale des affaires, du bilan général de vie et de l'environnement final.",
        "psaume": "Psaume 119", "nb_ecriture": 15, "verset": "Verset 105", 
        "texte_biblique": "Ta parole est une lampe à mes pieds, et une lumière sur mon sentier.",
        "vibratoire": "Fréquence d'illumination et de synthèse de l'Esprit-Saint. Elle aligne le canal coronal (Chakra Coronal) avec l'intelligence supérieure, permettant de clore définitivement un cycle karmique lourd.",
        "avantages": "Dénouement heureux et inespéré d'une crise de vie majeure, illumination spirituelle, clarté absolue sur le but de votre existence, pacification environnementale globale.",
        "huile": "Encens d'Oliban (Haute connexion divine et conclusion céleste)", 
        "aromatiques": "Résine pure d'Oliban en larmes, Fleurs de Jasmin séchées, Safran royal en poudre",
        "zikr": "Ya Alim (Ô Omniscient) — 150 fois + Nom Salomonique : TETRAGRAMMATON",
        "priere_salomonique": "Sagesse Suprême, TETRAGRAMMATON Ineffable, dont le Verbe Sacré est une lampe infaillible à mes pieds. Toi qui connais la fin avant le commencement, illumine l'issue de mon thème et de ma vie. Que Ta vérité triomphe de toute illusion, dissipe les ombres environnementales et m'accorde la paix finale des victorieux. Amen.",
        "mots_application": "Que la lumière parfaite éclaire la conclusion de mes démarches et m'apporte la réussite globale. Amen.", "moment": "Soir"
    },
    "Moussa (Moussa)": {
        "ref": "Moussa (Moussa)", "code": (2, 1, 2, 1), "nature": "Neutre à Fort", "element": "Feu", "direction": "Est",
        "txt": "Maison du Décret Suprême, de la décision irréversible de la providence et de la sentence finale.",
        "psaume": "Psaume 4", "nb_ecriture": 16, "verset": "Verset 7", 
        "texte_biblique": "Fais lever sur nous la lumière de ta face, ô Éternel !",
        "vibratoire": "Onde de choc métatronique (Éclair de foudre). Elle coupe net, comme un glaive divin, tous les fils astrals résiduels de retard ou de malédiction. Elle scelle le verdict du thème dans la matière.",
        "avantages": "Exécution ultra-rapide des requêtes formulées, signature immédiate de contrats bloqués, libération karmique instantanée, justice divine appliquée en votre faveur.",
        "huile": "Orange Douce (Rapidité et scellage solaire)", 
        "aromatiques": "Zestes de Citron vert, Feuilles de Menthe poivrée, Cannelle de Ceylan, Safran",
        "zikr": "Ya Sari'u (Ô Rapide) — 202 fois + Nom Salomonique : SCHEMHAMPHORASCH",
        "priere_salomonique": "Par le Grand Nom Sacré et Vibrant SCHEMHAMPHORASCH, Toi le Maître des décrets foudroyants et de la justice immédiate. Fais luire l'éclair de Ta face sur mon destin. Que Ta sentence brise le retard chronique, valide mes requêtes théurgiques et scelle ce travail dans le monde physique avec une rapidité miraculeuse. Ce qui est écrit par Ta main s'exécute maintenant. Amen.",
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
# MOTEUR DE CALCULS GÉOMANTIQUES MATHÉMATIQUEMENT RECTIFIÉS
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
# EXPÉRIENCE UTILISATEUR ET DESIGN APPLICATION
# ==============================================================================
st.title("🔮 Plateforme Experts de Haute Théurgique & Géomancie Rectifiée")
st.write("Dressez instantanément le thème. Le système génère automatiquement les protocoles de soins vibratoires et les prières de scellage salomoniques.")

with st.sidebar:
    st.header("🔐 Clé d'Authentification")
    u_id = st.text_input("Identifiant")
    u_pw = st.text_input("Mot de passe", type="password")

if u_id == ID_SECRET and u_pw == MDP_SECRET:
    st.success("🔓 Temple théurgique pleinement actif.")
    
    # Intégration du guide thérapeutique complet
    st.header("📜 DIRECTIVES ET CONSEIL THÉRAPEUTIQUE TRADITIONNEL")
    with st.expander("👉 Manuel Thérapeutique Avancé : Travailler avec une Figure", expanded=False):
        st.markdown("""
        Travailler avec une figure issue d'un tirage géomantique consiste à matérialiser sa fréquence énergétique dans la matière à travers trois étapes clés.
        
        ### 🟥 PHASE 1 : La Densification par l'Écriture (Le Support et l'Encre)
        * **Le Support** : Traditionnellement, utilisez une ardoise en bois noble (ou un parchemin végétal vierge).
        * **L'Encre Métaphysique et la Coloration Vibratoire** :
            * **Le Safran (Jaune d'Or éblouissant)** : À privilégier impérativement pour les figures de l'élément **Feu ou Air** ou pour toutes les demandes liées à la gloire, au charisme, à l'élévation sociale et à l'ouverture rapide (*ex: Youssouf, Souleymane, Allahou Talla*).
            * **Le Curcuma Pur (Jaune profond/orangé)** : À utiliser pour les figures de l'élément **Terre ou Eau** ou pour les demandes de fixation de l'argent, de protection structurelle du foyer et d'anéantissement de blocages ancestraux (*ex: Adam, Idriss, Ayoube*).
        * **Le Nombre Sacré** : Écrivez le verset biblique lié à la figure le **nombre exact de fois** déterminé. Chaque répétition grave l'onde de forme dans le support.

        ### 🟩 PHASE 2 : La Phase Alchimique (La Préparation du Bain)
        * **L'Infusion des Plantes** : Faites bouillir les aromates dédiés pendant 15 minutes dans de l'eau de source pure pour extraire leur charge éthérique.
        * **Le Lavage (Le Nassi)** : Recueillez l'encre colorée sacrée en lavant délicatement votre support avec cette eau de plantes tiède. 
        * **Le Scellage par l'Huile (Règle d'or)** : Les huiles essentielles capturent l'esprit de la figure. Ne les versez **jamais** directement dans l'eau sous peine de les voir flotter en surface. **Versez vos gouttes d'huile dans une poignée de gros sel béni**, puis jetez le sel dans le bain. Le sel lie les composants et purifie l'astral.

        ### 🟦 PHASE 3 : L'Activation Vocale (Le Décret et le Bain)
        * **La Récitation** : Versez l'eau lentement de la tête aux pieds sur un corps préalablement lavé. Récitez le Psaume indiqué à voix haute. La voix fait vibrer la structure moléculaire du bain.
        * **Le Verbe Salomonique** : Proclamez le Zikr et sa Prière Salomonique avec force et certitude. Vous ordonnez ainsi à la matière de s'aligner sur le décret spirituel.
        * **Le Séchage Naturel** : Ne pas utiliser de serviette. Laissez l'eau théurgique sécher d'elle-même sur votre peau afin de sceller la charge dans l'ensemble de vos corps subtils.
        
        *⚠️ **Conseil Thérapeutique Majeur :** Ne mélangez pas les énergies. Ne travaillez qu'avec **une seule figure à la fois** (ex: la figure siégeant en M1, M15 ou M16). Traiter plusieurs figures distinctes le même jour crée des interférences vibratoires destructrices.*
        """)

    st.header("📥 DEPLOIEMENT : SAISIE DES 4 MÈRES FONDAMENTALES")
    options_figures = list(DATA.keys())
    
    c1, col2, col3, col4 = st.columns(4)
    with c1: m1 = st.selectbox("🏠 M1 (Première Mère)", options_figures, index=0)
    with col2: m2 = st.selectbox("🏠 M2 (Deuxième Mère)", options_figures, index=1)
    with col3: m3 = st.selectbox("🏠 M3 (Troisième Mère)", options_figures, index=2)
    with col4: m4 = st.selectbox("🏠 M4 (Quatrième Mère)", options_figures, index=3)

    # Automatisation des calculs matriciels traditionnels
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

    # Cartographie visuelle
    st.markdown("---")
    st.header("🖼️ CARTOGRAPHIE ET RÉPARTITION DE LA MATRICE CALCULÉE")
    
    with st.container(border=True):
        st.subheader("⚜️ Ligne I : Les 4 Mères Mères Originelles")
        i1, i2, i3, i4 = st.columns(4)
        i1.metric("M1 (Le Demandeur)", theme_complet[1])
        i2.metric("M2 (Flux Financier)", theme_complet[2])
        i3.metric("M3 (Relations/Entourage)", theme_complet[3])
        i4.metric("M4 (Le Foyer/Patrimoine)", theme_complet[4])
        
        st.subheader("🌿 Ligne II : Les 4 Filles Issues des Transpositions")
        i5, i6, i7, i8 = st.columns(4)
        i5.metric("M5 (Enfants/Créativité)", theme_complet[5])
        i6.metric("M6 (Maladies/Servitudes)", theme_complet[6])
        i7.metric("M7 (Alliances/Adversaires)", theme_complet[7])
        i8.metric("M8 (Blocages/Peur/Mort)", theme_complet[8])

        st.subheader("⚡ Ligne III : Les 4 Neveux (Moyens d'action d'Évolution)")
        i9, i10, i11, i12 = st.columns(4)
        i9.metric("M9 (Horizons/Voyages)", theme_complet[9])
        i10.metric("M10 (Carrière/Autorité)", theme_complet[10])
        i11.metric("M11 (Espoirs Secrètes)", theme_complet[11])
        i12.metric("M12 (Obstacles Majeurs)", theme_complet[12])

        st.subheader("⚖️ Tribunal Sacré de la Sentence Finale")
        i13, i14, i15, i16 = st.columns(4)
        i13.warning(f"M13 (Témoin Droite) : {theme_complet[13]}")
        i14.warning(f"M14 (Témoin Gauche) : {theme_complet[14]}")
        i15.error(f"M15 (Le Juge Central) : {theme_complet[15]}")
        i16.success(f"M16 (Le Décret Suprême) : {theme_complet[16]}")

    # Section d'extraction de données textuelles
    st.markdown("---")
    st.header("📋 EXPORTATION INTÉGRALE DE LA FICHE DU CONSULTANT")
    
    texte_fiche = "--- RITUEL ET SOINS DU THÈME THÉURGIQUE ---\n\n"
    for m, fig_choisie in theme_complet.items():
        b = DATA[fig_choisie]
        texte_fiche += f"[{MAISONS_NOMINATIVES[m]}] -> {fig_choisie}\n"
        texte_fiche += f"- Aromates : {b['aromatiques']}\n"
        texte_fiche += f"- Huile : {b['huile']}\n"
        texte_fiche += f"- Nassi : {b['psaume']} ({b['verset']}) - Répétition : {b['nb_ecriture']} fois\n"
        texte_fiche += f"- Clé Sacrée Activation : {b['zikr']}\n"
        texte_fiche += "----------------------------------------\n"
        
    st.text_area("Copiez ce résumé en un clic :", value=texte_fiche, height=200)

    # Dictionnaire étendu interactif
    st.markdown("---")
    st.header("📖 GUIDE INTÉGRAL DES SOINS URBAINS PAR SECTEUR")
    
    for m, fig_choisie in theme_complet.items():
        bloc = DATA[fig_choisie]
        entete_action = "🛑 NETTOYAGE CRITIQUE REQUIS" if "Mauvais" in bloc["nature"] else "✨ ALLIANCE & OUVERTURE DE LUMIÈRE"
        titre_boite = f"{MAISONS_NOMINATIVES[m]} ➔ {fig_choisie} [{entete_action}]"
        
        with st.expander(titre_boite):
            tab_vibratoire, tab_recette, tab_invocation = st.tabs(["🔬 Diagnostic Vibratoire", "🌿 Préparation du Nassi & Bain", "📿 Clé Salomonique Active"])
            
            with tab_vibratoire:
                st.markdown(f"**Définition Sectorielle :** *{bloc['txt']}*")
                st.markdown(f"**Éléments et Coordonnées Cosmiques :** Élément `{bloc['element'].upper()}` | Orientation `{bloc['direction'].upper()}` | Nature `{bloc['nature'].upper()}`")
                st.markdown("---")
                st.markdown("### 🌀 Signature & Effet Éthérique Vibratoire :")
                st.write(bloc["vibratoire"])
                st.markdown("### 💎 Avantage Thérapeutique Concret :")
                st.write(bloc["avantages"])
                
            with tab_recette:
                st.markdown("### 🧪 Ingrédients Alchimiques Exigés :")
                st.write(f"🌱 **Plantes à infuser au feu :** `{bloc['aromatiques']}`")
                st.write(f"💧 **Fiole d'Huile de Scellage (à diluer dans du Gros Sel) :** *{bloc['huile']}*")
                st.markdown("---")
                st.markdown("### ✍️ Protocole d'Écriture :")
                st.success(f"Écrire le **{bloc['verset']}** exactement **{bloc['nb_ecriture']} fois** sur l'ardoise ou parchemin.")
                st.markdown("### 📜 Grand Psaume Récité :")
                st.info(f"Réciter à voix haute l'intégralité du **{bloc['psaume']}** au-dessus de l'eau sacrée aromatisée.")
                st.markdown(f"*Texte de l'Ancre Sacrée :* **\"{bloc['texte_biblique']}\"**")
                
            with tab_invocation:
                st.markdown("### 📿 Clé Mentale et Mantrique (Zikr) :")
                st.warning(bloc["zikr"])
                st.markdown("---")
                st.markdown("### 👑 LA PRIÈRE SALOMONIQUE DE LA FIGURE :")
                st.markdown(f"> **{bloc['priere_salomonique']}**")
                st.markdown("---")
                st.success(f"🗣️ **Mots d'Application Finale (À Proclamer) :** \"{bloc['mots_application']}\"")
                st.caption(f"⏱️ **Moment Idéal Cosmique pour le Bain :** {bloc['moment']}")
else:
    st.warning("🔒 Système Verrouillé. Veuillez inscrire les codes secrets dans le panneau latéral gauche.")
