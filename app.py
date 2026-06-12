import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Système Théurgique & Géomancie Ramrou", page_icon="🔮", layout="wide")

# ==============================================================================
# ACCÈS SÉCURISÉS
# ==============================================================================
ID_SECRET = "theurge2026"
MDP_SECRET = "Salomon777"

# ==============================================================================
# BASE DE DONNÉES COMPLÉMENTAIRE : INTERPRÉTATIONS RAMROU (16 Figures x 16 Maisons)
# ==============================================================================
DICTIONNAIRE_RAMROU = {
    "Youssouf": {
        1: "⚠️ Trahison, agitation, frustration. (Dépend grandement du Juge en M15).",
        2: "💰 Chance sur trahison ou obtenue suite à un emballement soudain.",
        3: "👥 Trahison ou frustration au sein de l'entourage proche ou lors des démarches.",
        4: "🏠 Trahison localisée directement dans le cercle familial ou le foyer.",
        5: "👶 Annonce une trahison venant d'un rival ou d'un ami proche.",
        6: "🩹 Se traduit par des maux de poitrine, une profonde remise en question ou des idées confuses.",
        7: "💍 Annonce une trahison dans le mariage, provenant du conjoint ou de l'adversaire direct.",
        8: "🔄 Trahison avortée (qui n'ira pas jusqu'au bout, avortée par le changement).",
        9: "🙏 Trahison en cours accompagnée de frustration sur le chemin ou dans la quête spirituelle.",
        10: "👑 Trahison dans le service (travail) ou liée à un fait professionnel précis.",
        11: "🕊️ Trahison en cours de promesse non tenue (les appuis ou espoirs font défaut).",
        12: "⛓️ Trahison avec méchanceté manifeste provenant d'un ennemi résolu.",
        13: "🛏️ Trahison à domicile (dans la chambre, le dortoir ou l'intimité du foyer).",
        14: "💵 Trahison sur des biens financiers, des vols ou des crédits non remboursés.",
        15: "🔮 Annonce clairement la trahison : le Juge confirme que le climat global est trompeur.",
        16: "📜 Le Décret final clôture et valide la finition de l'affaire de trahison."
    },
    "Adama": {
        1: "✨ Très bonne nouvelle concernant directement le consultant, joie intérieure.",
        2: "💰 Forte augmentation de la chance financière, opportunité de gain immédiat.",
        3: "👥 Entourage favorable, démarches couronnées de succès et de bienveillance.",
        4: "🏠 Stabilité et bonheur dans le foyer, réussite liée au patrimoine immobilier.",
        5: "👶 Joie liée aux enfants, plaisirs, heureuse nouvelle inattendue.",
        6: "🩹 Diminution de la chance, fatigue ou perte matérielle/financière.",
        7: "💍 Union heureuse, mariage prospère ou accord parfait avec un partenaire.",
        8: "🔄 Chance retardée ou bloquée temporairement par un changement soudain.",
        9: "✈️ Voyage chanceux, élévation spirituelle ou réussite dans les études/recherches.",
        10: "👑 Excellente opportunité professionnelle, promotion, faveurs du patron.",
        11: "🙏 Les espoirs se réalisent, les souhaits de réussite matérielle sont exaucés.",
        12: "⚠️ Obstacles majeurs bloquant la chance par la faute d'ennemis cachés.",
        13: "🛏️ La chance s'installe à domicile, sérénité retrouvée dans l'intimité.",
        14: "💵 Gains financiers futurs garantis, investissement ou épargne fructueuse.",
        15: "🔮 Le Juge confirme une issue extrêmement favorable et lumineuse.",
        16: "📜 Décret final très positif, concrétisation absolue des objectifs."
    },
    "Mahdy": {
        1: "🔄 Esprit focalisé sur le mouvement, envie de changement ou de déplacement.",
        2: "💰 Augmentation de la prospérité et gains financiers majeurs en mouvement.",
        3: "👥 Nouvelles dynamiques avec l'entourage, démarches actives de communication.",
        4: "🏠 Changement ou déplacement prévu au sein du foyer (déménagement, travaux).",
        5: "👶 Déplacement agréable pour les plaisirs ou nouvelles d'un enfant en route.",
        6: "🩹 Retards dans le rétablissement ou blocages dans les tâches quotidiennes.",
        7: "💍 Rencontre importante en voyage, ou accord dynamique avec l'adversaire.",
        8: "🔄 Changement radical de situation, transformation profonde et rapide.",
        9: "✈️ Annonce un déplacement sûr, un voyage très profitable et sans embûches.",
        10: "👑 Évolution professionnelle rapide, déplacement pour le travail.",
        11: "🙏 Appuis providentiels extérieurs facilitant les projets à venir.",
        12: "⛓️ Risque de blocage sévère, de grand retard, voire de restriction de liberté.",
        13: "🛏️ Arrivée imminente d'une personne ou d'une nouvelle au domicile.",
        14: "💵 Rentrée d'argent future liée à un commerce ou un déplacement.",
        15: "🔮 Le Juge annonce que la conclusion dépend entièrement d'un changement de voie.",
        16: "📜 Sentence rapide et dynamique qui débloque définitivement la situation."
    },
    "Idriss": {
        1: "🧘 Esprit sage, calme, serein. Clarté mentale et décisions réfléchies.",
        2: "💰 Gains financiers stables et mérités, gestion prudente et payante.",
        3: "👥 Soutien sincère de la part des parents, frères ou voisins respectables.",
        4: "🏠 Symbole d'union, de paix profonde, de sécurité et de confiance au sein de la famille.",
        5: "👶 Éducation réussie, sagesse des enfants ou joie tranquille.",
        6: "🩹 Problèmes de santé durables, maladies chroniques ou difficultés matérielles tenaces.",
        7: "💍 Mariage solide basé sur la confiance mutuelle, fidélité du conjoint.",
        8: "🔄 Fin paisible d'un problème, transition douce vers autre chose.",
        9: "🙏 Haute protection divine, réussite dans la quête spirituelle ou religieuse.",
        10: "👑 Respect de la hiérarchie, autorité légitime et reconnue au travail.",
        11: "🙏 Espoirs fondés sur du solide, promesses tenues à coup sûr.",
        12: "⛓️ Épreuves supportées avec patience, victoire finale sur les épreuves.",
        13: "🛏️ Paix et harmonie absolues au sein du lit conjugal et du foyer intime.",
        14: "💵 Patrimoine financier sécurisé, économies bien protégées.",
        15: "🔮 Le Juge valide la solidité de l'affaire avec une issue juste.",
        16: "📜 Décret immuable et protecteur qui scelle la paix."
    },
    "Ibrahima": {
        1: "🤔 État de doute, d'hésitation profonde face à une route ou un projet à entreprendre.",
        2: "💰 La chance arrive petit à petit (goutte-à-goutte) mais elle s'avère durable.",
        3: "👥 Hésitations dans les démarches ou communications floues avec l'entourage.",
        4: "🏠 Climat incertain dans la maison, attente d'une décision familiale.",
        5: "👶 Projets de conception, créativité en éveil mais demande du temps.",
        6: "🩹 Petite indisposition physique passagère ou paresse au travail.",
        7: "💍 Incertitude dans le couple, hésitation avant un engagement officiel.",
        8: "🔄 Changement lent qui demande de la patience avant de porter ses fruits.",
        9: "✈️ Voyage retardé ou doutes sur l'orientation spirituelle à prendre.",
        10: "👑 Statut professionnel en attente de validation, hésitations de la hiérarchie.",
        11: "🙏 Espoirs fragiles mais réels, les souhaits avancent lentement.",
        12: "⛓️ Difficultés mineures causées par des doutes internes plus que par des ennemis.",
        13: "🛏️ Attente ou réflexion solitaire dans la chambre à coucher.",
        14: "💵 Rentrées financières fragmentées, petits profits réguliers.",
        15: "🔮 Le Juge indique qu'il ne faut pas se précipiter, l'issue est en gestation.",
        16: "📜 Décret qui demande une vérification avant la finition complète."
    },
    "Inssa": {
        1: "🗣️ Disputes intérieures, nervosité, pensées conflictuelles et mauvaise foi.",
        2: "💰 Conflits liés à l'argent, discussions tendues pour des intérêts financiers.",
        3: "👥 Querelles de voisinage, malentendus ou mensonges dans l'entourage proche.",
        4: "🏠 Disputes familiales, mauvaise foi, mensonges ou discussions conflictuelles au foyer.",
        5: "👶 Tensions avec les enfants ou plaisirs gâchés par des paroles amères.",
        6: "🩹 Maux physiques liés au stress, ambiance de travail conflictuelle.",
        7: "💍 Fortes disputes dans le couple, rupture de dialogue ou procès avec l'adversaire.",
        8: "🔄 Querelle qui provoque une rupture ou un changement brutal.",
        9: "✈️ Incidents ou disputes durant un déplacement, blocage clérical.",
        10: "👑 Tensions majeures avec le patron, risque de blâme ou de conflit d'autorité.",
        11: "🙏 Espoirs déçus par des promesses mensongères ou des disputes.",
        12: "⛓️ Complots manifestes, médisances et attaques verbales gratuites d'ennemis.",
        13: "🛏️ Climat de tension et de dispute au sein du lit conjugal à la maison.",
        14: "💵 Pertes d'argent dues à des litiges ou des pénalités non prévues.",
        15: "🔮 Engendre des regrets, une diminution ou une perte de statut général.",
        16: "📜 Sentence conflictuelle qui nécessite un nettoyage spirituel immédiat."
    },
    "Omar": {
        1: "🔥 Impulsivité, colère intérieure, comportement à risque ou agressif.",
        2: "💰 Danger de perte financière rapide, dépenses impulsives ou vol.",
        3: "👥 Conflit violent ou rupture brutale avec un membre de l'entourage.",
        4: "🏠 Risque d'incendie, de casse ou de violente crise au sein de la famille.",
        5: "👶 Tensions extrêmes, rivalités passionnelles ou impulsivité d'un ami.",
        6: "🩹 Alerte critique sur un risque d'accident, de blessure grave ou d'incendie.",
        7: "💍 Crise conjugale majeure, affrontement direct avec la partie adverse.",
        8: "🔄 Rupture définitive, destruction d'une situation pour en rebâtir une autre.",
        9: "✈️ Grand danger lors des voyages, agressions ou pannes sévères.",
        10: "👑 Conflits graves avec l'autorité (juge, police, patron), risque de sanction lourde.",
        11: "🙏 Espoirs brisés net par une colère ou une action irréfléchie.",
        12: "⛓️ Attaques violentes d'ennemis déclarés, danger de dommages physiques.",
        13: "🛏️ Violence ou discorde intime intolérable à domicile.",
        14: "💵 Ruine financière ou blocage total de crédits par destruction de dossier.",
        15: "🔮 Le Juge tire la sonnette d'alarme : le climat général est hautement dangereux.",
        16: "📜 Décret tranchant et foudroyant qui met fin à l'affaire de manière brutale."
    },
    "Ayoub": {
        1: "🖤 Tristesse profonde, mélancolie, blocage psychologique ou angoisse.",
        2: "📉 Malchance financière sévère, pauvreté temporaire, négativité ambiante.",
        3: "👥 Isolement social, rupture de communication avec l'entourage proche.",
        4: "🏠 Climat lourd et triste dans la maison, deuil ou sensation d'enfermement.",
        5: "👶 Inquiétudes pour les enfants, absence de joie, solitude affective.",
        6: "🩹 Maladie lente, fatigue générale, épuisement au travail quotidien.",
        7: "💍 Solitude dans le couple, froideur affective ou divorce douloureux.",
        8: "🔄 Transformation par la douleur, deuil d'une ancienne situation.",
        9: "✈️ Voyage annulé ou pénible, crise de foi spirituelle.",
        10: "👑 Perte d'emploi, destitution, impuissance face à la hiérarchie.",
        11: "🙏 Perte d'espoir, découragement total face aux projets.",
        12: "⛓️ Méchanceté d'un ennemi caché, fortes douleurs physiques (maux de ventre).",
        13: "🛏️ Solitude subie ou tristesse ressentie directement dans la chambre à coucher.",
        14: "💵 Dettes lourdes, blocage total des rentrées financières à venir.",
        15: "🔮 Le Juge confirme un climat de blocage, de tristesse et de fatalité.",
        16: "📜 Conclusion difficile qui demande patience et traitements thérapeutiques."
    },
    "Allahou": {
        1: "✨ Esprit élevé, protection divine ressentie, intuition forte.",
        2: "💰 Fortune mineure, entrée d'argent rapide et inattendue.",
        3: "👥 Démarches spirituelles ou administratives facilitées avec l'entourage.",
        4: "🏠 Bénédiction sur le foyer, protection de la maison familiale.",
        5: "👶 Joie spirituelle, chance pure, cadeaux ou heureuses surprises.",
        6: "🩹 Guérison rapide d'un mal grâce à une intervention providentielle.",
        7: "💍 Alliance sacrée, mariage béni ou conciliation facile avec l'adversaire.",
        8: "🔄 Changement bénéfique et soudain guidé par la providence.",
        9: "✈️ Voyage rapide, succès éclatant et élévation spirituelle majeure.",
        10: "👑 Succès soudain au travail, reconnaissance des mérites par les chefs.",
        11: "🙏 Les souhaits les plus chers reçoivent une validation spirituelle.",
        12: "⛓️ Dissolution des pièges des ennemis par la grâce divine.",
        13: "🛏️ Paix et bénédiction dans la chambre, sommeil réparateur.",
        14: "💵 Prospérité future assurée par des voies claires et honnêtes.",
        15: "🔮 Le Juge annonce le succès et la lumière sur l'ensemble du thème.",
        16: "📜 Décret divin hautement favorable qui valide toutes les requêtes."
    },
    "Souleymane": {
        1: "🔒 Esprit préoccupé par des responsabilités lourdes ou des blocages.",
        2: "💰 Argent bloqué ou soumis à des taxes, des contrôles administratifs.",
        3: "👥 Devoirs familiaux contraignants, démarches lentes et bureaucratiques.",
        4: "🏠 Autorité paternelle forte, contraintes immobilières ou familiales.",
        5: "👶 Devoirs envers les enfants, plaisirs limités par le travail.",
        6: "🩹 Fatigue due aux responsabilités, surmenage professionnel.",
        7: "💍 Mariage de raison, contrats stricts ou blocages juridiques avec l'adversaire.",
        8: "🔄 Retards obligatoires, immobilisme nécessaire avant le changement.",
        9: "✈️ Voyage d'affaires officiel ou démarches administratives complexes.",
        10: "👑 Affaires complexes liées à un chef, rigueur absolue exigée au travail.",
        11: "🙏 Espoirs soumis à des conditions strictes, patience demandée.",
        12: "⛓️ Ennemis puissants (administration, justice) créant des contraintes.",
        13: "🛏️ Climat sérieux ou distant à la maison, manque de lâcher-prise.",
        14: "💵 Épargne bloquée à long terme, investissements lourds.",
        15: "🔮 Le Juge indique que l'affaire est freinée par des règles ou des lois.",
        16: "📜 Décret final qui structure et stabilise l'affaire après des efforts."
    },
    "Aliou": {
        1: "🤝 Esprit ouvert à la conciliation, recherche d'harmonie et d'alliances.",
        2: "💰 Gains financiers issus de partenariats ou de contrats signés.",
        3: "👥 Entente parfaite avec l'entourage, réunions amicales ou fraternelles.",
        4: "🏠 Paix partagée, réunions heureuses au sein du foyer familial.",
        5: "👶 Joie partagée, plaisirs amoureux, harmonie amicale forte.",
        6: "🩹 Amélioration de la santé grâce au soutien de l'entourage.",
        7: "💍 Union, entente parfaite, mariage d'amour ou réconciliation totale.",
        8: "🔄 Changement négocié en douceur, transition collective réussie.",
        9: "✈️ Voyage de groupe ou démarche d'alliance à l'étranger réussie.",
        10: "👑 Signature de contrat importante, association fructueuse avec les chefs.",
        11: "🙏 Union, entente, documents ou contrats espérés qui arrivent enfin.",
        12: "⛓️ Les ennemis abandonnent leurs poursuites face à vos alliances.",
        13: "🛏️ Amour, complicité et tendresse partagés au lit à domicile.",
        14: "💵 Financement obtenu, crédits accordés grâce à de bons appuis.",
        15: "🔮 Le Juge valide une issue d'entente et de bonheur partagé.",
        16: "📜 Décret final scellant définitivement une alliance heureuse."
    },
    "Nouhou": {
        1: "⏳ Esprit combatif face à l'adversité, endurance psychologique.",
        2: "💰 Retards dans les rentrées d'argent, mais déblocage financier final.",
        3: "👥 Relations compliquées avec l'entourage, démarches administratives lentes.",
        4: "🏠 Difficultés passagères au foyer, résistance face aux crises immobilières.",
        5: "👶 Inquiétudes légères vite dissipées, plaisirs mérités après l'effort.",
        6: "🩹 Maladie longue nécessitant de la patience, travail quotidien difficile.",
        7: "💍 Tensions dans le couple qui demandent de la persévérance pour être résolues.",
        8: "🔄 Transition lente mais salvatrice vers une nouvelle vie.",
        9: "✈️ Voyage long avec des escales ou des retards, mais arrivée à bon port.",
        10: "👑 Évolution de carrière lente, épreuves imposées par le patron.",
        11: "🙏 Espoirs retardés mais qui finiront par se matérialiser.",
        12: "⛓️ Difficultés majeures, retards provoqués, mais déblocage final possible.",
        13: "🛏️ Rétablissement du climat intime après une période de doute.",
        14: "💵 Rentrées d'argent différées, recouvrement de créances anciennes.",
        15: "🔮 Le Juge montre que l'issue demande du temps et de la persévérance.",
        16: "📜 Décret de délivrance qui libère l'affaire après de longs blocages."
    },
    "Assane": {
        1: "⚠️ Sentiments de jalousie, d'envie, doutes intérieurs destructeurs.",
        2: "💰 Pertes financières dues à des tromperies ou de la jalousie.",
        3: "👥 Rivalités cachées dans l'entourage proche, commérages.",
        4: "🏠 Climat de suspicion ou d'infidélité larvée au sein de la maison.",
        5: "👶 Jalousie, trahison amoureuse, déception affective, négativité.",
        6: "🩹 Fatigue morale, somatisation des angoisses amoureuses.",
        7: "💍 Risque d'adultère, crise de confiance majeure avec le conjoint.",
        8: "🔄 Rupture amoureuse ou affective causée par des tiers jaloux.",
        9: "✈️ Démarches de voyage compromises par des rivalités ou de la mauvaise foi.",
        10: "👑 Crocs-en-jambe professionnels, collègues jaloux sabotant votre statut.",
        11: "🙏 Espoirs déçus par la trahison d'un ami en qui vous aviez confiance.",
        12: "⛓️ Attaques sournoises d'ennemis agissant par pure jalousie.",
        13: "🛏️ Trahison ou déception flagrante vécue directement à domicile.",
        14: "💵 Litiges sur des partages de biens, vols d'économies.",
        15: "🔮 Le Juge confirme un environnement marqué par la jalousie et l'envie.",
        16: "📜 Décret final qui nécessite une coupure nette avec les personnes toxiques."
    },
    "Younouss": {
        1: "❤️ Esprit comblé, sentiments d'amour, de plénitude et de joie.",
        2: "💰 Excellente aisance financière, gains importants, grande chance matérielle.",
        3: "👥 Entourage extrêmement affectueux, démarches très fluides.",
        4: "🏠 Richesse et confort au sein du foyer, harmonie familiale totale.",
        5: "👶 Amour passionné, réussite totale des enfants, plaisirs intenses.",
        6: "🩹 Santé éclatante, vitalité retrouvée, épanouissement au travail.",
        7: "💍 Mariage d'amour parfait, harmonie absolue avec le partenaire.",
        8: "🔄 Changement heureux apportant l'abondance et le soulagement.",
        9: "✈️ Voyage d'amour ou d'agrément magnifique, haute lumière spirituelle.",
        10: "👑 Promotion éclatante, succès public, amour et estime du patron.",
        11: "🙏 Aisance financière, amour, gains, réussite totale de tous les vœux.",
        12: "⛓️ Triomphe total et sans effort sur tous les ennemis cachés.",
        13: "🛏️ Passion amoureuse intense et bonheur parfait vécus dans la chambre.",
        14: "💵 Prospérité financière future majeure, richesse consolidée.",
        15: "🔮 Le Juge annonce une conclusion couronnée de succès et de bonheur.",
        16: "📜 Décret de triomphe absolu validant le bonheur du consultant."
    },
    "Ousmane": {
        1: "🧘 Esprit tourné vers la réflexion profonde, la méditation et la foi.",
        2: "💰 Gains obtenus grâce à des activités de l'esprit ou de la foi.",
        3: "👥 Échanges profonds et sincères avec l'entourage, conseils avisés.",
        4: "🏠 Sérénité et calme philosophique au sein de la maison familiale.",
        5: "👶 Sagesse précoce des enfants, plaisirs simples et spirituels.",
        6: "🩹 Paix du corps obtenue par le repos de l'esprit, clarté au travail.",
        7: "💍 Union spirituelle forte, respect mutuel au sein du couple.",
        8: "🔄 Transition de vie vécue avec une grande maturité philosophique.",
        9: "✈️ Pèlerinage, voyage spirituel ou études supérieures hautement profitables.",
        10: "👑 Statut de conseiller, respect de la hiérarchie pour votre intégrité.",
        11: "🙏 Spiritualité, méditation, succès éclatant à l'issue de prières intenses.",
        12: "⛓️ Protection absolue contre le mal grâce à votre force spirituelle.",
        13: "🛏️ Atmosphère calme, propice aux rêves lucides dans la chambre.",
        14: "💵 Sécurité financière future obtenue par une gestion sage.",
        15: "🔮 Le Juge valide une conclusion d'élévation et de paix intérieure.",
        16: "📜 Décret qui apporte la lumière divine et la clarté finale sur l'affaire."
    },
    "Moussa": {
        1: "🎉 Esprit festif, soulagement d'arriver au bout d'un long chemin.",
        2: "💰 Rentrées d'argent finales, clôture de comptes très positive.",
        3: "👥 Rassemblement de l'entourage, fêtes familiales ou professionnelles.",
        4: "🏠 Joie partagée au foyer, réussite finale liée à la maison.",
        5: "👶 Célébrations, réussite publique, bonheur avec les enfants.",
        6: "🩹 Guérison complète et définitive, fin heureuse des corvées.",
        7: "💍 Mariage célébré en grande pompe, victoire publique sur l'adversaire.",
        8: "🔄 Libération totale d'un fardeau, fin heureuse d'un cycle.",
        9: "✈️ Grand déplacement réussi, retour de voyage triomphal.",
        10: "👑 Couronnement des efforts, consécration professionnelle devant tous.",
        11: "🙏 Réalisation finale et publique de tous les espoirs nourris.",
        12: "⛓️ Élimination définitive de toutes les entraves et des ennemis.",
        13: "🛏️ Joie et célébration de l'union partagées au cœur du domicile.",
        14: "💵 Fructification totale des investissements et des crédits.",
        15: "🔮 Conclusion de l'affaire, rassemblement d'une foule, joie ou déplacement final.",
        16: "📜 Le Décret final (Moussa) valide et scelle définitivement la réussite."
    }
}

MAISONS_NOMINATIVES = {
    1: "M1 (Demandeur)", 2: "M2 (Biens/Chances)", 3: "M3 (Entourage)", 4: "M4 (Foyer/Patrimoine)",
    5: "M5 (Enfants/Nouvelles)", 6: "M6 (Maladies)", 7: "M7 (Adversaires/Époux)", 8: "M8 (Mort/Peurs)",
    9: "M9 (Voyages)", 10: "M10 (Travail/Autorité)", 11: "M11 (Espoirs)", 12: "M12 (Difficultés)",
    13: "M13 (Témoin Droite)", 14: "M14 (Témoin Gauche)", 15: "M15 (Conclusion)", 16: "M16 (Le Décret)"
}

# Configuration des données dictionnaire de base (Zikr / Bains / Plantes)
DATA_THEURGIQUE = {
    "Youssouf": {"ref": "Youssouf", "nature": "Bénéfique", "plante": "Djècala", "psaume": "Psaume 100", "verset": "Verset 2", "texte_biblique": "Servez l'Éternel avec joie...", "zikr": "Ya Latif — 129 fois", "bain": "Infuser des tiges de Citronnelle et du Djècala."},
    "Adama": {"ref": "Adama", "nature": "Bénéfique", "plante": "Sana", "psaume": "Psaume 8", "verset": "Verset 6", "texte_biblique": "Tu lui as donné l'empire...", "zikr": "Ya Rafi'u — 351 fois", "bain": "Infuser 100g de feuilles de Sana."},
    "Mahdy": {"ref": "Mahdy", "nature": "Neutre", "plante": "Cebé", "psaume": "Psaume 4", "verset": "Verset 7", "texte_biblique": "Fais lever sur nous la lumière...", "zikr": "Ya Nour — 256 fois", "bain": "Macération de feuilles de Cebé."},
    "Idriss": {"ref": "Idriss", "nature": "Bénéfique", "plante": "Djou", "psaume": "Psaume 112", "verset": "Verset 3", "texte_biblique": "Il a dans sa maison bien-être...", "zikr": "Ya Razzaq — 308 fois", "bain": "Décoction de racines de Djou."},
    "Ibrahima": {"ref": "Ibrahima", "nature": "Bénéfique", "plante": "M'bana", "psaume": "Psaume 1", "verset": "Verset 3", "texte_biblique": "Il est comme un arbre planté...", "zikr": "Ya Bassitou — 72 fois", "bain": "Feuilles de M'bana infusées."},
    "Inssa": {"ref": "Inssa", "nature": "Neutre à Mauvais", "plante": "Wingninga", "psaume": "Psaume 51", "verset": "Verset 12", "texte_biblique": "Crée en moi un coeur pur...", "zikr": "Ya Chafi — 391 fois", "bain": "Feuilles de Wingninga + sel gemme."},
    "Omar": {"ref": "Omar", "nature": "Mauvais", "plante": "Gababelé", "psaume": "Psaume 35", "verset": "Verset 1", "texte_biblique": "Attaque ceux qui m'attaquent...", "zikr": "Ya Jabbar — 206 fois", "bain": "Gababelé broyé + gingembre."},
    "Ayoub": {"ref": "Ayoub", "nature": "Mauvais", "plante": "Kronifin", "psaume": "Psaume 142", "verset": "Verset 8", "texte_biblique": "Tire mon âme de sa prison...", "zikr": "Ya Moukhrij — 201 fois", "bain": "Feuilles de Kronifin + charbon végétal."},
    "Allahou": {"ref": "Allahou", "nature": "Bénéfique", "plante": "Sadjo", "psaume": "Psaume 23", "verset": "Verset 1", "texte_biblique": "L'Éternel est mon berger...", "zikr": "Ya Malik — 90 fois", "bain": "Feuilles de Sadjo + fleurs de rose."},
    "Souleymane": {"ref": "Souleymane", "nature": "Bénéfique", "plante": "Sira (Baobab)", "psaume": "Psaume 45", "verset": "Verset 2", "texte_biblique": "Mon oeuvre est pour le roi...", "zikr": "Ya Jamil — 83 fois", "bain": "Écorce de Baobab bouillie."},
    "Aliou": {"ref": "Aliou", "nature": "Bénéfique", "plante": "Gbè yiri", "psaume": "Psaume 133", "verset": "Verset 1", "texte_biblique": "Qu'il est doux pour des frères...", "zikr": "Ya Wadoud — 20 fois", "bain": "Feuilles de Gbè yiri + cardamome."},
    "Nouhou": {"ref": "Nouhou", "nature": "Mauvais", "plante": "Kounbè", "psaume": "Psaume 30", "verset": "Verset 12", "texte_biblique": "Tu as changé mon deuil...", "zikr": "Ya Latif — 129 fois", "bain": "Feuilles de Kounbè + thym blanc."},
    "Assane": {"ref": "Assane", "nature": "Neutre", "plante": "Zaman", "psaume": "Psaume 18", "verset": "Verset 38", "texte_biblique": "Je les brise, ils ne peuvent...", "zikr": "Ya Moumit — 490 fois", "bain": "Écorces de Zaman + eucalyptus."},
    "Younouss": {"ref": "Younouss", "nature": "Bénéfique", "plante": "Dialassogala", "psaume": "Psaume 91", "verset": "Verset 11", "texte_biblique": "Il ordonnera à ses anges...", "zikr": "Ya Hafiz — 998 fois", "bain": "Écorces de Dialassogala."},
    "Ousmane": {"ref": "Ousmane", "nature": "Bénéfique", "plante": "Doualé", "psaume": "Psaume 119", "verset": "Verset 105", "texte_biblique": "Ta parole est une lampe...", "zikr": "Ya Alim — 150 fois", "bain": "Feuilles de Doualé + Oliban."},
    "Moussa": {"ref": "Moussa", "nature": "Neutre à Fort", "plante": "Tomy bourou", "psaume": "Psaume 4", "verset": "Verset 7", "texte_biblique": "Fais lever sur nous la lumière...", "zikr": "Ya Sari'u — 202 fois", "bain": "Feuilles de Tomy bourou + menthe."}
}

# ==============================================================================
# INTERFACE STREAMLIT
# ==============================================================================
st.title("🔮 Oracle Géomantique Ramrou & Traitements Théurgiques")
st.write("Saisissez le thème géomantique complet pour obtenir instantanément les prédictions Ramrou du document et vos ordonnances de soins.")

with st.sidebar:
    st.header("🔐 Accès sécurisé")
    u_id = st.text_input("Identifiant")
    u_pw = st.text_input("Mot de passe", type="password")

if u_id == ID_SECRET and u_pw == MDP_SECRET:
    st.success("🔓 Connexion établie avec succès.")
    
    options_figures = list(DICTIONNAIRE_RAMROU.keys())
    
    st.header("📥 CONFIGURATION DES 16 MAISONS")
    
    st.markdown("### ⚜️ M1 à M4 : Les Mères")
    c1, c2, c3, c4 = st.columns(4)
    m1 = c1.selectbox("🏠 Maison 1 (Demandeur)", options_figures, index=0)
    m2 = c2.selectbox("🏠 Maison 2 (Argent)", options_figures, index=1)
    m3 = c3.selectbox("🏠 Maison 3 (Entourage)", options_figures, index=2)
    m4 = c4.selectbox("🏠 Maison 4 (Foyer)", options_figures, index=3)

    st.markdown("### 🌿 M5 à M8 : Les Filles")
    c5, c6, c7, c8 = st.columns(4)
    m5 = c5.selectbox("🏠 Maison 5 (Nouvelles)", options_figures, index=4)
    m6 = c6.selectbox("🏠 Maison 6 (Obstacles/Maladie)", options_figures, index=5)
    m7 = c7.selectbox("🏠 Maison 7 (Union/Adversaire)", options_figures, index=6)
    m8 = c8.selectbox("🏠 Maison 8 (Fin/Peur/Mort)", options_figures, index=7)

    st.markdown("### ⚡ M9 à M12 : Les Neveux")
    c9, c10, c11, c12 = st.columns(4)
    m9 = c9.selectbox("🏠 Maison 9 (Voyages)", options_figures, index=8)
    m10 = c10.selectbox("🏠 Maison 10 (Travail/Pouvoir)", options_figures, index=9)
    m11 = c11.selectbox("🏠 Maison 11 (Espoirs)", options_figures, index=10)
    m12 = c12.selectbox("🏠 Maison 12 (Épreuves)", options_figures, index=11)

    st.markdown("### ⚖️ M13 à M16 : Tribunal & Décret")
    c13, c14, c15, c16 = st.columns(4)
    m13 = c13.selectbox("🏠 Maison 13 (Présent/Intime)", options_figures, index=12)
    m14 = c14.selectbox("🏠 Maison 14 (Avenir/Gains)", options_figures, index=13)
    m15 = c15.selectbox("🏠 Maison 15 (Le Juge)", options_figures, index=14)
    m16 = c16.selectbox("🏠 Maison 16 (Le Décret Final)", options_figures, index=15)

    theme_complet = {
        1: m1, 2: m2, 3: m3, 4: m4, 5: m5, 6: m6, 7: m7, 8: m8,
        9: m9, 10: m10, 11: m11, 12: m12, 13: m13, 14: m14, 15: m15, 16: m16
    }

    st.markdown("---")
    st.header("📖 DICTIONNAIRE D'INTERPRÉTATION DIRECTE RAMROU")
    st.write("Dépliez chaque maison pour lire l'analyse oraculaire exacte et récupérer les protocoles théurgiques.")
    
    for m, fig_choisie in theme_complet.items():
        prediction_ramrou = DICTIONNAIRE_RAMROU[fig_choisie].get(m, "Aucune interprétation spécifique enregistrée.")
        soin_theurge = DATA_THEURGIQUE.get(fig_choisie, {})
        
        titre_boite = f"{MAISONS_NOMINATIVES[m]} ➔ Figure présente : {fig_choisie}"
        
        with st.expander(titre_boite):
            # Affichage direct et immédiat de la prédiction issue de la base de données
            st.markdown("### 📜 Interprétation Prophétique (Selon la Méthode Ramrou) :")
            st.success(f"🔮 **{prediction_ramrou}**")
            
            st.markdown("---")
            st.markdown("### 🛠️ Protocole Thérapeutique & Spirituel Associé :")
            
            tab_verset, tab_bain = st.tabs(["📿 Récitation Sacrée (Zikr)", "🌿 Médecine par les plantes"])
            
            with tab_verset:
                if soin_theurge:
                    st.write(f"📖 **Livre sacré :** {soin_theurge['psaume']}, {soin_theurge['verset']}")
                    st.info(f"*\"{soin_theurge['texte_biblique']}\"*")
                    st.warning(f"📿 **Zikr à exécuter :** {soin_theurge['zikr']}")
                else:
                    st.write("Aucun protocole de récitation enregistré pour cette figure.")
                    
            with tab_bain:
                if soin_theurge:
                    st.write(f"🍂 **Plante maîtresse :** {soin_theurge['plante']}")
                    st.info(f"🥣 **Préparation & Bain :** {soin_theurge['bain']}")
                else:
                    st.write("Aucun traitement par les plantes enregistré.")
else:
    st.warning("🔒 Accès restreint. Veuillez entrer vos identifiants secrets dans la barre latérale.")
