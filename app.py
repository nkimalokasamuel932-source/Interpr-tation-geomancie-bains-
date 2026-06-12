import streamlit as st

# ==============================================================================
# CONFIGURATION DE L'APPLICATION
# ==============================================================================
st.set_page_config(
    page_title="Oracle Ramrou — Grand Grimoire Théurgique & Botanique", 
    page_icon="🔮", 
    layout="wide"
)

# ==============================================================================
# 1. BASE DE DONNÉES GÉOMANTIQUE COMPLÈTE (MANUSCRIT RAMROU)
# ==============================================================================

PROPRIETES_FIGURES = {
    "Youssouf": {
        "num": 1, "nature_manuscrit": "Diable Mauvais", "groupe": "Mobiles", 
        "element": "Feu (Est)", "formule_calcul": "Feu(2) + Vent(7) + Eau(0) + Terre(8) = 17. 17 - 16 = 1",
        "morphologie": "Tête: Ouverte | Poitrine: Ouverte | Ventre: Fermé | Pieds: Ouvert"
    },
    "Adama": {
        "num": 2, "nature_manuscrit": "Diable Bon", "groupe": "Sortants", 
        "element": "Feu (Est)", "formule_calcul": "Feu(2) + Vent(0) + Eau(0) + Terre(0) = 2",
        "morphologie": "Tête: Ouverte | Poitrine: Fermée | Ventre: Fermé | Pieds: Fermé"
    },
    "Mahdy": {
        "num": 3, "nature_manuscrit": "Diable Bon", "groupe": "Rentrants", 
        "element": "Air (Ouest)", "formule_calcul": "Feu(0) + Vent(7) + Eau(4) + Terre(8) = 19. 19 - 16 = 3",
        "morphologie": "Tête: Fermée | Poitrine: Ouverte | Ventre: Ouverte | Pieds: Ouvert"
    },
    "Idriss": {
        "num": 4, "nature_manuscrit": "Diable Bon", "groupe": "Fixes", 
        "element": "Eau (Nord)", "formule_calcul": "Feu(0) + Vent(0) + Eau(4) + Terre(0) = 4",
        "morphologie": "Tête: Fermée | Poitrine: Fermée | Ventre: Ouverte | Pieds: Fermé"
    },
    "Ibrahima": {
        "num": 5, "nature_manuscrit": "Humain Bon", "groupe": "Mobiles", 
        "element": "Eau (Nord)", "formule_calcul": "Feu(2) + Vent(7) + Eau(4) + Terre(8) = 21. 21 - 16 = 5",
        "morphologie": "Tête: Ouverte | Poitrine: Ouverte | Ventre: Ouverte | Pieds: Ouvert"
    },
    "Inssa": {
        "num": 6, "nature_manuscrit": "Humain Mauvais", "groupe": "Sortants", 
        "element": "Eau (Nord)", "formule_calcul": "Feu(2) + Vent(0) + Eau(4) + Terre(0) = 6",
        "morphologie": "Tête: Ouverte | Poitrine: Fermée | Ventre: Ouverte | Pieds: Fermé"
    },
    "Omar": {
        "num": 7, "nature_manuscrit": "Diable Mauvais", "groupe": "Fixes", 
        "element": "Air (Ouest)", "formule_calcul": "Feu(0) + Vent(7) + Eau(0) + Terre(0) = 7",
        "morphologie": "Tête: Fermée | Poitrine: Ouverte | Ventre: Fermé | Pieds: Fermé"
    },
    "Ayoub": {
        "num": 8, "nature_manuscrit": "Diable Mauvais", "groupe": "Rentrants", 
        "element": "Terre (Sud)", "formule_calcul": "Feu(0) + Vent(0) + Eau(0) + Terre(8) = 8",
        "morphologie": "Tête: Fermée | Poitrine: Fermée | Ventre: Fermé | Pieds: Ouvert"
    },
    "Allahou": {
        "num": 9, "nature_manuscrit": "Humain Mauvais", "groupe": "Sortants", 
        "element": "Feu (Est)", "formule_calcul": "Feu(2) + Vent(7) + Eau(0) + Terre(0) = 9",
        "morphologie": "Tête: Ouverte | Poitrine: Ouverte | Ventre: Fermé | Pieds: Fermé"
    },
    "Souleymane": {
        "num": 10, "nature_manuscrit": "Humain Bon", "groupe": "Mobiles", 
        "element": "Terre (Sud)", "formule_calcul": "Feu(2) + Vent(0) + Eau(0) + Terre(8) = 10",
        "morphologie": "Tête: Ouverte | Poitrine: Fermée | Ventre: Fermé | Pieds: Ouvert"
    },
    "Aliou": {
        "num": 11, "nature_manuscrit": "Humain Mauvais", "groupe": "Fixes", 
        "element": "Air (Ouest)", "formule_calcul": "Feu(0) + Vent(7) + Eau(4) + Terre(0) = 11",
        "morphologie": "Tête: Fermée | Poitrine: Ouverte | Ventre: Ouverte | Pieds: Fermé"
    },
    "Nouhou": {
        "num": 12, "nature_manuscrit": "Humain Bon", "groupe": "Rentrants", 
        "element": "Terre (Sud)", "formule_calcul": "Feu(0) + Vent(0) + Eau(4) + Terre(8) = 12",
        "morphologie": "Tête: Fermée | Poitrine: Fermée | Ventre: Ouverte | Pieds: Ouvert"
    },
    "Assane": {
        "num": 13, "nature_manuscrit": "Diable Mauvais", "groupe": "Sortants", 
        "element": "Eau (Nord)", "formule_calcul": "Feu(2) + Vent(7) + Eau(4) + Terre(0) = 13",
        "morphologie": "Tête: Ouverte | Poitrine: Ouverte | Ventre: Ouverte | Pieds: Fermé"
    },
    "Younouss": {
        "num": 14, "nature_manuscrit": "Diable Bon", "groupe": "Mobiles", 
        "element": "Terre (Sud)", "formule_calcul": "Feu(2) + Vent(0) + Eau(4) + Terre(8) = 14",
        "morphologie": "Tête: Ouverte | Poitrine: Fermée | Ventre: Ouverte | Pieds: Ouvert"
    },
    "Ousmane": {
        "num": 15, "nature_manuscrit": "Humain Bon", "groupe": "Rentrants", 
        "element": "Air (Ouest)", "formule_calcul": "Feu(0) + Vent(7) + Eau(0) + Terre(8) = 15",
        "morphologie": "Tête: Fermée | Poitrine: Ouverte | Ventre: Fermé | Pieds: Ouvert"
    },
    "Moussa": {
        "num": 16, "nature_manuscrit": "Humain Mauvais", "groupe": "Fixes", 
        "element": "Feu (Est)", "formule_calcul": "Feu(0) + Vent(0) + Eau(0) + Terre(0) = 0 -> Reste 16 par défaut",
        "morphologie": "Tête: Fermée | Poitrine: Fermée | Ventre: Fermé | Pieds: Fermé"
    }
}

MAISONS_RAMROU = {
    1: {"nom": "M1 (Maison de l'Âme)", "description": "L'être physique, sa force, sa personnalité. Décrit l'origine des choses, l'élan premier et le consultant."},
    2: {"nom": "M2 (Maison de la Chance)", "description": "La matérialité de l'argent, les finances, les biens matériels et les richesses qui alimentent M1."},
    3: {"nom": "M3 (Maison des Mères)", "description": "L'entourage proche, les relations, les voisins et les courts déplacements dus aux alliés."},
    4: {"nom": "M4 (Maison des Pères)", "description": "Le patrimoine familial, immobilier, le foyer et la fin des choses."},
    5: {"nom": "M5 (Maison des Enfants)", "description": "Les plaisirs, la vie amoureuse, la créativité, le charme, les lettres et la descendance."},
    6: {"nom": "M6 (Maison des Malades)", "description": "Le métier, les principes du travail quotidien, le foyer, la santé et les obstacles/blocages."},
    7: {"nom": "M7 (Maison du Mariage)", "description": "Le conjoint, l'épouse, les associations, les contrats, ainsi que les rivaux ou adversaires déclarés."},
    8: {"nom": "M8 (Maison du Changement)", "description": "La tombe, l'extérieur, l'étranger, les peurs et les transformations."},
    9: {"nom": "M9 (Maison de Dieu)", "description": "La spiritualité, la religion, les écrits, la philosophie et les grands voyages à l'étranger."},
    10: {"nom": "M10 (Maison des Rois)", "description": "Le travail, la réalisation sociale, le pouvoir, l'élévation, les honneurs, l'employeur ou la lignée maternelle."},
    11: {"nom": "M11 (Maison de l'Espoir)", "description": "Les projets, les espoirs, les amis, les soutiens, la collaboration et les promesses."},
    12: {"nom": "M12 (Maison des Ennemis)", "description": "Les blocages cachés, la méchanceté, le maraboutage, les pièges et les épreuves."},
    13: {"nom": "M13 (Maison du Sexe / Chambre)", "description": "L'intimité du foyer, le lit conjugal, les désirs intimes et le présent immédiat."},
    14: {"nom": "M14 (Maison des Fortunes)", "description": "Les gains futurs, les réussites commerciales à venir, les rentrées financières décalées."},
    15: {"nom": "M15 (Maison de l'Espace)", "description": "Les rumeurs, la clarté d'esprit, la pensée et le juge de synthèse."},
    16: {"nom": "M16 (Maison de Finition)", "description": "La conclusion ultime, irrévocable et le décret final de l'affaire étudiée."}
}

DICTIONNAIRE_CAS = {
    "Adama": {
        1: "Joie intérieure intense, élévation, l'âme est en paix.",
        2: "Chance financière rapide, acquisition matérielle imminente.",
        3: "Relations amicales ou familiales excellentes, déplacements fructueux.",
        4: "Paix au foyer, stabilité du patrimoine immobilier.",
        5: "Bonne nouvelle concernant les enfants, bonheur en amour.",
        6: "Guérison rapide d'un malade, levée des obstacles au travail.",
        7: "Union heureuse et sincère, contrat commercial validé.",
        8: "Bonne nouvelle venant de l'extérieur, changement bénéfique.",
        9: "Annonce une bonne nouvelle ou une chance en cours dans le voyage ou le domaine spirituel.",
        10: "Prédit une bonne nouvelle, une belle chance, ferveur et élévation au travail.",
        11: "Annonce de belles promesses mais attention au risque léger de déception par excès de confiance.",
        12: "Annonce un blocage, une chance moindre ou une diminution temporaire des biens.",
        13: "Annonce une bonne nouvelle du bonheur, de la joie dans la chambre ou le lit conjugal.",
        14: "Annonce un retard dans l'acquisition d'une bonne chance, c'est une chance qui se concrétisera dans le futur.",
        15: "Annonce de la joie, de la clarté et de la chance dans l'espace environnant.",
        16: "Conclusion lumineuse : annonce une bonne nouvelle définitive pour l'affaire."
    },
    "Mahdy": {
        1: "Annonce une élévation, une hauteur difficile à atteindre, une distance ou un voyage/déplacement.",
        2: "Annonce des profits, des gains importants, une augmentation de la chance et de la prospérité.",
        3: "Prédit un pacte sur l'entourage, de bons rapports, sincérités honnêtes. Retard dans un voyage sûr et profitable.",
        4: "Annonce le bonheur dans le foyer, la réussite immobilière et la prospérité familiale.",
        5: "Prédit une bonne nouvelle : des enfants, du bonheur, des richesses, ou une nouvelle sur un voyage venant de loin.",
        6: "Annonce un échec, une perte de quelque chose qui vient de loin ou suite d'un déplacement, maladie qui dure.",
        7: "Prévoit une très bonne union, une excellente association, entente, sagesse et sincérité absolue.",
        8: "Annonce une perte sur tout ce qui est à l'extérieur, contretemps pendant un voyage, perte liée à une maladie.",
        9: "Annonce un déplacement sûr et sans contrainte, un très bon voyage et une très bonne nouvelle spirituelle.",
        10: "Prédit honneur, encouragement, réussite, et un très bon voyage dans le contexte du service.",
        11: "Annonce l'espérance, de grands espoirs, des promesses tenues mais exige de faire des efforts pour réussir.",
        12: "Annonce une difficulty, un obstacle, un retard, un blocage voir même des risques de prison ou d'enfermement.",
        13: "Très bon présage intime, entente parfaite dans le couple au quotidien.",
        14: "Rentrées d'argent différées mais solides provenant de transactions passées.",
        15: "Clarté de la pensée, résolution mentale d'un problème complexe.",
        16: "L'affaire se conclut sur un compromis très profitable et stable."
    },
    "Ibrahima": {
        1: "Annonce un doute, une hésitation concernant une voie, une route, un voyage.",
        2: "Annonce une chance arrivant au compte-goutte mais qui ne s'arrêtera jamais.",
        3: "Déplacement, hésitation ou questionnements répétés lors d'un voyage court.",
        4: "Annonce une activité à faible revenu, un faible voyage ou un déplacement lié au patrimoine.",
        5: "Annonce enfants, amour, lettre, ou une femme qui cherche activement un enfant.",
        6: "Annonce maladie, instabilité générale, mauvaise prise de décision, recherche constante de sa route.",
        7: "Annonce un adversaire ou un conjoint qui peut s'avérer un ennemi caché.",
        8: "Annonce une chance arrivante, ou des nouvelles d'une personne qui est actuellement à l'étranger.",
        9: "Voyage ou déplacement marqué par des difficultés en cours de route.",
        10: "Fonction publique, maison du roi, marabout, recherche d'une solution par le voyage.",
        16: "L'affaire se termine pas à pas, avec persévérance."
    },
    "Omar": {
        1: "Annonce une révolte, des querelles, de la vengeance ou de la peur ancrée dans l'âme.",
        2: "Annonce de la fatigue, des problèmes financiers, des colères dévastatrices ou de la peur.",
        3: "Annonce un problème, des querelles, des débats houleux, de la colère, des disputes ou de la frustration de voisinage.",
        4: "Annonce un danger sur le patrimoine familial (maison, voiture, biens mobiles).",
        5: "Annonce une femme enceinte d'une fille, mais contexte de disputes ou de tensions amoureuses.",
        7: "Grave crise conjugale, partenaire colérique qui parle trop ou violences verbales.",
        10: "Conflit direct avec l'autorité, la justice, le patron ou risque de blâme.",
        16: "Annonce de la colère, des problèmes majeurs, du stress et de la frustration en fin de course."
    },
    "Ayoub": {
        1: "Annonce une obscurité, de la peur, de la tristesse, du chagrin ou des mensonges subis.",
        2: "Annonce de la malchance, de l'obscurité financière, de la négativité ou de la peur face aux manques.",
        3: "Annonce de la magouille, du vol, un complot, des mensonges ou de l'obscurité dans l'entourage proche.",
        4: "Annonce de la tristesse, de l'inquiétude, de la peur dans la maison, ou des magouilles immobilières.",
        16: "Retard et blocage pesant. Fin de cycle douloureuse."
    },
    "Allahou": {
        1: "Fortune mineure, voyage, déplacement brusque ou imprévu.",
        2: "Chance rapide venant sans effort, réussite flagrante et voyage facile.",
        3: "Démarche rapide dans l'entourage, relation familiale dynamique, voyage imminent.",
        4: "Patrimoine familial matériel, maison sécurisée ou voyage familial facile.",
        5: "Sentiments d'amours sincères, femmes, amis, informations fluides, voyages agréables.",
        6: "Des soucis mineurs, voyage entrepris dans la peur, mais progrès ou augmentation brusque.",
        7: "Un adversaire ou conjoint honnête avec de bons projets, mariage ou association valide.",
        8: "Un service rendu à l'étranger, un projet extérieur, ou un voyage sans retour (installation définitive).",
        9: "Un voyage, un déplacement, une évolution, un excellent projet et de très bons profits.",
        10: "Une activité, un travail, bonheur rapide, fluidité et facilité professionnelle.",
        11: "De l'espoir, un souhait réussi, une victoire éclatante après une discussion constructive.",
        12: "Une difficulty, une méchanceté d'un tiers, plein de blocages ou panne matérielle/voiture.",
        13: "Environnement mystique, retour bénéfique du voyageur, marabout ou féticheur protecteur.",
        14: "Projet d'un voyage lointain, démarches couronnées de succès, bonheur, discussions animées.",
        15: "Paroles ou discussions vives sur le lieu de travail.",
        16: "Fortune globale, grand voyage protecteur et déplacements profonds."
    },
    "Assane": {
        1: "Annonce une personne de mauvaise foi, malhonnête ou jalouse d'autrui.",
        2: "Annonce la déception, le regret, la diminution drastique ou la perte sèche de sa chance.",
        3: "Démarches difficiles, jalousie féroce et blocages au sein de l'entourage proche.",
        4: "Magouille, mensonge avéré, vol ou détournement de biens au sein du foyer.",
        5: "Difficultés, obstacles sévères, risks d'avortement ou enfant souffrant d'un handicap.",
        6: "Maladie, perte matérielle, attaques de mauvais génies (djinn mécréant) et grande déception.",
        7: "Mauvaise personne pour le cas d'un mariage (le manuscrit conseille : 'mieux vaut abandonner').",
        8: "Pertes à l'extérieur, voyage dangereux, maladie ou complications à l'étranger.",
        9: "Perte de quelque chose en cours de route, vol subi, mensonges découverts.",
        10: "Déception majeure, licenciement au travail ou séparation/divorce dans le mariage.",
        11: "Mensonge, trahison amicale, regret amer, obstacle inattendu ou pure méchanceté.",
        12: "Problème grave dans le couple, disputes quotidiennes destructrices.",
        13: "Dispute dans le mariage, querelle intime, jalousie maladive ou séparation de lit.",
        14: "Blocage complet, trahison commerciale, annulation pure et simple d'un projet.",
        16: "Échec ou regret cuisant. L'affaire prend une mauvaise tournure."
    },
    "Moussa": {
        1: "Annonce le voyage, les réunions collectives, l'union ou le regroupement.",
        2: "Annonce la chance globale, le progrès, le succès commercial et les profits partagés.",
        3: "Rencontre fortuite ou programmée d'un proche, d'un parent ou d'un allié précieux.",
        4: "Réunion de famille importante, gestion d'un problème ou d'un arbitrage de patrimoine.",
        16: "Finition complète. Le projet ou l'épreuve se termine pour ouvrir un nouveau cycle."
    }
}

# ==============================================================================
# 2. ENRICHISSEMENT BOTANIQUE ET THÉURGIQUE INTEGRAL DES SECRETS RITUELS
# ==============================================================================
SECRETS_RITUELS = {
    "Adama": {
        "titre": "✨ BAIN DE GRANDE OUVERTURE & CHANCE RAPIDE",
        "nassi": "Tracer la figure Adama 1836 fois (ou 918 fois si associé à un talisman) sur l'ardoise en bois.",
        "paroles_sacrees": "Associer et réciter le **Psaume 23** (L'Éternel est mon berger) ou le **Verset Al-Fath** (La Victoire éclatante) 41 fois sur le liquide.",
        "plantes_traditionnelles": "🌿 Feuilles fraîches de Basilic sacré (Fereb) et écorces de Manguier sauvage. Piler le tout énergiquement et faire macérer dans le Nassi pendant 3 heures.",
        "huiles_essentielles": "💧 7 gouttes d'huile essentielle de Bergamote (Aimant à prospérité) et 3 gouttes de Cannelle d'écorce (Vitesse d'action) diluées dans un peu de lait frais.",
        "oraison_salomonique": "« Ô Dieu de Lumière, par la Sagesse accordée au Roi Salomon, commande à Tes Anges d'ouvrir les écluses des cieux. Que les verrous se brisent et que l'or vienne à moi. Amen. »",
        "bain_mode": "Jeter 7 morceaux de charbon ardent dans le Nassi. Se laver entièrement pendant 7 jours consécutifs, impérativement le matin entre 7h et 8h.",
        "sadaka": "Sacrifier 7 morceaux de sucre, 7 colas blanches et un coq blanc à un nécessiteux."
    },
    "Ousmane": {
        "titre": "👁️ BAIN DE VISION NOCTURNE & CLARTÉ MENTALE",
        "nassi": "Écrire la figure Ousmane 55 fois (pour la vision) ou 88 fois (pour la mémoire spirituelle) avec l'encre traditionnelle.",
        "paroles_sacrees": "Réciter le **Psaume 119:105** (Ta parole est une lampe à mes pieds) ou le **Verset de la Lumière (Ayat Al-Nur)** 7 fois au-dessus du récipient.",
        "plantes_traditionnelles": "🌿 Sommités fleuries de Romarin frais et feuilles de Menthe poivrée sauvage. Froisser les feuilles à la main directement dans l'eau sacrée.",
        "huiles_essentielles": "💧 5 gouttes d'huile essentielle d'Encens Oliban (Haute connexion) et 4 gouttes de Menthe Poivrée (Activation et ouverture sensorielle).",
        "oraison_salomonique": "« Esprit Éternel qui as instruit Salomon au travers de visions claires, nettoie mon miroir intérieur et ôte le voile noir posé sur mes yeux. Amen. »",
        "bain_mode": "Bain de visage (3 fois de suite avant le coucher) et boire une gorgée du Nassi mélangée à du miel ou du lait frais pendant 15 nuits.",
        "sadaka": "Faire l'aumône de lait frais ou d'une bougie blanche le premier jeudi du rituel."
    },
    "Nouhou": {
        "titre": "🛡️ BAIN DE BRISAGE DE MARABOUTAGE & EXORCISME LOURD",
        "nassi": "Écrire la figure de Nouhou 489 fois ou 1111 fois sur l'ardoise.",
        "paroles_sacrees": "Adjoindre le **Psaume 91** (Celui qui demeure sous l'abri du Très-Haut) ou les **Versets de l'Annulation de la Magie (Sourate Yunus, v.81-82)** écrit 12 fois.",
        "plantes_traditionnelles": "🌿 Feuilles amères de Citronnier sauvage (Kankaliba) et écorces séchées de Neem (Gouro). Faire bouillir légèrement ces plantes dans le Nassi recueilli.",
        "huiles_essentielles": "💧 9 gouttes d'huile essentielle d'Arbre à thé (Tea Tree) et 5 gouttes de Laurier Noble (Garant de la victoire contre les ombres).",
        "oraison_salomonique": "« Par le Sceau Sacré du Roi Salomon et le Glaive de Justice, je brise et détruis tout décret de sorcellerie prononcé contre mon nom. Que le mal retourne à son auteur. Amen. »",
        "bain_mode": "Mélanger le Nassi avec de l'eau de mer capturée. Faire bouillir légèrement. Se laver obligatoirement 12 fois au cours de la même nuit (entre minuit et 3h). Ne pas s'essuyer.",
        "sadaka": "Sacrifier 3kg de riz blanc (pour un homme) ou 4kg de mil (pour une femme) un vendredi soir."
    },
    "Moussa": {
        "titre": "👑 BAIN DE POPULARITÉ & CHARME SOCIAL (ATTRACTION DE FOULE)",
        "nassi": "Tracer la figure de Moussa exactement 6666 fois (ou 313 fois couplé à 114 répétitions).",
        "paroles_sacrees": "Infuser le **Psaume 8** (Qu'est-ce que l'homme pour que tu te souviennes de lui) ou le **Verset d'attraction de Joseph (Youssouf)** 110 fois.",
        "plantes_traditionnelles": "🌿 Pétales fraîches de Rose rouge de jardin, feuilles de Verveine odorante et morceaux d'écorce d'Iroko sacré (arbre de royauté) séchés au soleil et pilés.",
        "huiles_essentielles": "💧 12 gouttes d'huile essentielle d'Ylang-Ylang complète (Charme magnétique) et 7 gouttes de Patchouli (Ancrage du pouvoir matériel).",
        "oraison_salomonique": "« Éternel, Souverain des mondes, mets sur mon front la couronne de grâce et de faveur. Que quiconque me voie m'accorde le respect et la bienveillance. Amen. »",
        "bain_mode": "Ajouter 8 parfums différents sans alcool (parfums de dévotion) au Nassi. Se laver le corps entier matin et soir pendant 28 jours.",
        "sadaka": "Donner un bélier blanc ou 16 miches de pain blanc le premier matin."
    },
    "Omar": {
        "titre": "💍 BAIN DE DÉBLOCAGE DU MARIAGE & RECOUVREMENT D'AFFECTION",
        "nassi": "Écrire la suite numérique sacrée de la figure : 70 fois, puis 45 fois, 16 fois et enfin 236 fois.",
        "paroles_sacrees": "Associer le **Psaume 45** (Chant d'amour et de mariage) ou les **Versets d'harmonie conjugale (Sourate Ar-Rum, v.21)** répétés 33 fois.",
        "plantes_traditionnelles": "🌿 Feuilles fraîches de Verveine, pétales de Jasmin et écorce d'arbre à soie pulvérisée pour adoucir les vibrations de colère d'Omar.",
        "huiles_essentielles": "💧 6 gouttes d'huile essentielle de Lavande Vraie (Paix de l'âme) et 4 gouttes de Géranium Bourbon (Harmonisation affective).",
        "oraison_salomonique": "« Par le Sceau d'Union qui lie les cœurs fidèles, dissipe la discorde, apaise les révoltes et rétablis l'alliance sacrée là où régnait la rupture. Amen. »",
        "bain_mode": "Mélanger l'eau Nassi obtenue avec du lait de vache frais et 4 parfums précieux (pour une femme) ou 3 parfums terreux (pour un homme). Se laver durant 14 nuits d'affilée.",
        "sadaka": "Offrir des gâteaux sucrés à des enfants ou faire don d'un tissu blanc à une femme âgée."
    }
}

# ==============================================================================
# 3. INTERFACE UTILISATEUR STREAMLIT
# ==============================================================================

st.title("🔮 Oracle Ramrou — Cabinet Théurgique & Botanique Intégral")
st.markdown("Harmonisation automatisée des seize maisons de la terre avec les plantes sacrées, les huiles de charge et les secrets de Salomon.")

# Section d'authentification latérale
with st.sidebar:
    st.header("🔐 Accès au Grimoire")
    u_id = st.text_input("Identifiant Mystique", value="theurge2026")
    u_pw = st.text_input("Clé d'accès", type="password", value="Salomon777")

# Vérification des privilèges
if u_id == "theurge2026" and u_pw == "Salomon777":
    st.sidebar.success("🔓 Sceaux brisés. Accès autorisé.")
    
    # Formulaire de saisie des maisons géomantiques
    st.sidebar.header("📥 Configuration des 16 Maisons")
    liste_figures = list(PROPRIETES_FIGURES.keys())
    theme_utilisateur = {}
    
    # Regroupement traditionnel pour fluidifier l'interface
    groupes_maisons = [
        ("⚜️ Les Mères (M1 à M4 - Racines)", range(1, 5)),
        ("🌿 Les Filles (M5 à M8 - Actions)", range(5, 9)),
        ("⚡ Les Neveux (M9 à M12 - Émanations)", range(9, 13)),
        ("⚖️ Tribunal Mystique (M13 à M16 - Verdicts)", range(13, 17))
    ]
    
    for titre_groupe, intervalle in groupes_maisons:
        st.sidebar.markdown(f"**{titre_groupe}**")
        for m_num in intervalle:
            default_idx = (m_num - 1) % len(liste_figures)
            theme_utilisateur[m_num] = st.sidebar.selectbox(
                f"{MAISONS_RAMROU[m_num]['nom']}",
                liste_figures, 
                index=default_idx, 
                key=f"maison_input_{m_num}"
            )

    # ==============================================================================
    # 4. MOTEUR ANALYTIQUE DES PASSATIONS & CALCUL DU FLUX
    # ==============================================================================
    st.header("🔄 ANALYSE DYNAMIQUE DES PASSATIONS (Flux de Cause à Effet)")
    st.write("Le système détecte les figures identiques qui migrent d'une maison à l'autre pour déterminer la source du problème et éditer le remède.")
    
    # Cartographie des répétitions
    carte_passations = {}
    for m_id, fig_nom in theme_utilisateur.items():
        if fig_nom not in carte_passations:
            carte_passations[fig_nom] = []
        carte_passations[fig_nom].append(m_id)
        
    # Filtrage des vraies passations (présentes au moins 2 fois)
    passations_detectees = {f: ms for f, ms in carte_passations.items() if len(ms) > 1}
    
    if not passations_detectees:
        st.info("💡 Aucune passation détectée dans ce thème. Les forces s'expriment de manière isolée sans migration de fluide.")
    else:
        for fig, maisons in passations_detectees.items():
            meta = PROPRIETES_FIGURES[fig]
            
            with st.container():
                st.markdown(f"## 💠 Flux Actif de la Figure : **{fig}**")
                
                col_tech, col_interp = st.columns([1, 2])
                with col_tech:
                    st.markdown("### 🎚️ Identité Vibratoire")
                    st.write(f"**Polarité :** `{meta['nature_manuscrit']}`")
                    st.write(f"**Élément Directeur :** `{meta['element']}`")
                    st.write(f"**Rythme :** `{meta['groupe']}`")
                    st.caption(f"🧬 *Structure : {meta['morphology']}*")
                
                with col_interp:
                    st.markdown("### 📜 Interprétation Spatio-Temporelle")
                    m_source = maisons[0]
                    st.info(f"📌 **La Cause (Né en {MAISONS_RAMROU[m_source]['nom']}) :** {DICTIONNAIRE_CAS.get(fig, {}).get(m_source, 'Influence élémentaire neutre ou standard.')}")
                    
                    for m_dest in maisons[1:]:
                        st.warning(f"➔ **L'Effet (Se manifeste en {MAISONS_RAMROU[m_dest]['nom']}) :** {DICTIONNAIRE_CAS.get(fig, {}).get(m_dest, 'Propagation standard de la ligne géomantique.')}")
                        
                        # Commentaire dynamique lié au groupe de la figure
                        phrase_flux = "⚠️ **Dynamique du transfert :** "
                        if meta['groupe'] == "Mobiles":
                            phrase_flux += "La figure étant **Mobile**, l'événement va basculer, évoluer ou se régler avec une rapidité fulgurante."
                        elif meta['groupe'] == "Fixes":
                            phrase_flux += "La figure étant **Fixe**, la situation s'enracine, stagne et crée un nœud énergétique durable entre ces deux aspects de votre vie."
                        elif meta['groupe'] == "Sortants":
                            phrase_flux += "La figure étant **Sortante**, l'énergie ou les bénéfices ont tendance à s'échapper vers l'extérieur."
                        elif meta['groupe'] == "Rentrants":
                            phrase_flux += "La figure étant **Rentrante**, les retombées karmiques ou financières reviennent se concentrer au cœur du foyer."
                        st.write(phrase_flux)
                
                # ==============================================================================
                # 5. REMÈDES BOTANIQUES ET THÉURGIQUES ASSOCIÉS AUX PASSATIONS
                # ==============================================================================
                if fig in SECRETS_RITUELS:
                    st.markdown("### 🛁 REMÈDE BOTANIQUE ET THÉURGIQUE SUR MESURE")
                    rituel = SECRETS_RITUELS[fig]
                    
                    st.error(f"📋 PROTOCOLE DE PURIFICATION INTÉGRAL : {rituel['titre']}")
                    
                    col_gauche, col_droite = st.columns(2)
                    with col_gauche:
                        st.markdown(f"✍️ **1. Rédaction du Nassi :**\n{rituel['nassi']}")
                        st.markdown(f"📖 **2. Parole et Programmation Vibratoire :**\n{rituel['paroles_sacrees']}")
                        st.markdown(f"🌿 **3. Plantes Aromatiques (La Charge Terrestre) :**\n{rituel['plantes_traditionnelles']}")
                        st.markdown(f"🧪 **4. Huiles Essentielles Clés (Le Fixateur d'Esprit) :**\n{rituel['huiles_essentielles']}")
                    
                    with col_droite:
                        st.info(f"👑 **5. Haute Oraison Salomonique (À réciter à voix haute) :**\n*{rituel['oraison_salomonique']}*")
                        st.markdown(f"🧼 **6. Exécution du Bain :**\n{rituel['bain_mode']}")
                        st.markdown(f"🐐 **7. Libération Karmique (Sadaka) :**\n{rituel['sadaka']}")
                else:
                    st.caption("ℹ️ Aucun protocole herboriste lourd n'est encodé pour cette figure. Utiliser un bain générique composé de sel marin, de feuilles de menthe sauvage et de 3 gouttes d'huile essentielle d'Encens.")
                
                st.markdown("<hr style='border-top: 3px double #bbb;'>", unsafe_allow_html=True)

    # ==============================================================================
    # 6. DICTIONNAIRE GENERAL DES 16 MAISONS (VISUALISATION UNITAIRE)
    # ==============================================================================
    st.markdown("---")
    st.header("📖 LECTURE COMPLÈTE DU THÈME (Maison par Maison)")
    st.write("Déroulez chaque section pour analyser l'état vibratoire unitaire de vos secteurs de vie.")
    
    for m_num, fig_nom in theme_utilisateur.items():
        meta_fig = PROPRIETES_FIGURES[fig_nom]
        signification_maison = DICTIONNAIRE_CAS.get(fig_nom, {}).get(m_num, "Analyse élémentaire : L'élément de la figure interagit directement avec l'axe de la maison.")
        
        with st.expander(f"📍 {MAISONS_RAMROU[m_num]['nom']} ➔ Figure présente : {fig_nom}"):
            st.markdown(f"**Rôle de ce secteur :** *{MAISONS_RAMROU[m_num]['description']}*")
            st.markdown(f"**Fiche d'identité :** Caractère `{meta_fig['nature_manuscrit']}` | Énergie `{meta_fig['groupe']}` | Élément `{meta_fig['element']}`")
            st.info(f"🔮 **Verdict du manuscrit :** {signification_maison}")

else:
    st.warning("🔒 Saisie des identifiants requise dans la barre latérale pour libérer les secrets du Nassi.")
