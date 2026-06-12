import streamlit as st

# Configuration de la page Streamlit
st.set_page_config(page_title="Oracle Ramrou & Passations", page_icon="🔮", layout="wide")

# ==============================================================================
# 1. BASE DE DONNÉES GÉOMANTIQUE COMPLÈTE (EXTRAITE DU MANUSCRIT)
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

# Base textuelle brute extraite fidèlement des fiches cas par cas du livre
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
        12: "Annonce une difficulté, un obstacle, un retard, un blocage voir même des risques de prison ou d'enfermement.",
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
        12: "Une difficulté, une méchanceté d'un tiers, plein de blocages ou panne matérielle/voiture.",
        13: "Environnement mystique, retour bénéfique du voyageur, marabout ou féticheur protecteur.",
        14: "Projet d'un voyage lointain, démarches couronnées de succès, bonheur, discussions animées.",
        15: "Paroles ou discussions vives sur le lieu de travail (si à côté de Moussa, Assane ou Inssa).",
        16: "Fortune globale, grand voyage protecteur et déplacements profonds."
    },
    "Assane": {
        1: "Annonce une personne de mauvaise foi, malhonnête ou jalouse d'autrui.",
        2: "Annonce la déception, le regret, la diminution drastique ou la perte sèche de sa chance.",
        3: "Démarches difficiles, jalousie féroce et blocages au sein de l'entourage proche.",
        4: "Magouille, mensonge avéré, vol ou détournement de biens au sein du foyer.",
        5: "Difficultés, obstacles sévères, risques d'avortement ou enfant souffrant d'un handicap.",
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

# Recettes de rituels / Secrets spécifiques collectés dans le livre
SECRETS_RITUELS = {
    "Adama": "Pour avoir l'ouverture et la chance : tracer la figure Adama 1836 fois (ou 918 fois pour un gri-gri avec peau d'hyène). Récupérer l'eau bénite (nassi), y jeter 7 morceaux de charbon ardents (feu) et se laver avec pendant 7 jours entre 7h et 8h du matin.",
    "Ousmane": "Pour avoir la vision la nuit : écrire Ousmane 55 fois toutes les nuits, laver le visage 3 fois avec le nassi et boire le reste avec du miel pendant 15 jours. Pour une bonne mémoire : écrire Ousmane 88 fois, mélanger le nassi avec du lait, boire et se laver pendant 15 jours.",
    "Nouhou": "Pour détruire un mauvais travail/maraboutage sur soi : écrire la figure de Nouhou 489 fois, 594 fois ou 1111 fois. Mélanger le nassi avec de l'eau de mer, faire bouillir, en boire un peu et se laver 12 fois au cours de la même nuit. Sacrifier ensuite 3kg de riz (homme) ou 4kg de mil (femme) un vendredi soir.",
    "Moussa": "Pour être populaire ou attirer la foule : écrire la figure de Moussa 6666 fois (ou 313 fois + 114 fois). Mélanger le nassi avec 8 parfums différents et se laver avec matin et soir pendant 28 jours.",
    "Omar": "Pour trouver un mari ou une femme : écrire la figure d'Omar 70 fois + 45 fois + 16 fois + 236 fois. Récupérer le nassi, mélanger avec du lait et 4 parfums (pour une femme) ou 3 parfums (pour un homme). Se laver pendant 14 nuits. Sacrifier ensuite 41 colas blancs.",
    "Ibrahima": "Pour concevoir un enfant : écrire la figure d'Ibrahima 444 fois, 1111 fois ou 111 fois. Boire le nassi obtenu pendant 21 jours, en particulier avant les rapports avec le partenaire.",
    "Inssa": "Pour neutraliser un adversaire (sort de protection) : écrire la figure d'Inssa 68 fois sur un papier, recouvrir de miel, réciter les intentions avec le prénom de la cible, en faire un talisman et l'enterrer un mardi entre 13h et 16h dans un endroit humide."
}

# ==============================================================================
# 2. INTERFACE APPLICATION STREAMLIT
# ==============================================================================

st.title("🔮 Expert Oracle Ramrou — Moteur de Passations Complet")
st.markdown("Ce programme implémente de façon stricte la base de données issue du manuscrit d'Ousmane B. Bonaldo.")

# Saisie sécurisée
with st.sidebar:
    st.header("🔐 Authentification")
    u_id = st.text_input("Identifiant", value="theurge2026")
    u_pw = st.text_input("Mot de passe", type="password", value="Salomon777")

if u_id == "theurge2026" and u_pw == "Salomon777":
    st.sidebar.success("🔓 Accès autorisé au manuscrit.")
    
    # Choix des figures pour le thème (16 Maisons)
    st.header("📥 Configuration du Thème (Saisie des 16 Maisons)")
    liste_figures = list(PROPRIETES_FIGURES.keys())
    
    theme_utilisateur = {}
    
    # Disposition par groupes de 4 maisons (Mères, Filles, Neveux, Tribunal)
    sections_maisons = [
        ("⚜️ Les Mères (M1 à M4 - Le Questionneur / Origines)", range(1, 5)),
        ("🌿 Les Filles (M5 à M8 - L'Affaire / Présent)", range(5, 9)),
        ("⚡ Les Neveux (M9 à M12 - Portée de l'Affaire)", range(9, 13)),
        ("⚖️ Le Tribunal (M13 à M16 - Finalité / Décret)", range(13, 17))
    ]
    
    for titre, intervalle in sections_maisons:
        st.markdown(f"### {titre}")
        colonnes = st.columns(4)
        for idx, m_num in enumerate(intervalle):
            # Sélection par défaut pré-configurée pour la démonstration
            default_idx = (m_num - 1) % len(liste_figures)
            theme_utilisateur[m_num] = colonnes[idx].selectbox(
                f"{MAISONS_RAMROU[m_num]['nom']}",
                liste_figures,
                index=default_idx,
                key=f"maison_{m_num}"
            )

    # ==============================================================================
    # 3. MOTEUR ANALYTIQUE DES PASSATIONS (DÉTECTION AUTOMATIQUE)
    # ==============================================================================
    st.markdown("---")
    st.header("🔄 ANALYSE DYNAMIQUE DES PASSATIONS DÉTECTÉES")
    st.write("Le système analyse ici le déplacement des figures entre les maisons (la première apparition est la **cause/origine**, les suivantes sont les **manifestations**).")
    
    # Inversion du dictionnaire pour grouper les maisons par figure
    groupement_passations = {}
    for m_id, fig_nom in theme_utilisateur.items():
        if fig_nom not in groupement_passations:
            groupement_passations[fig_nom] = []
        groupement_passations[fig_nom].append(m_id)
        
    # Filtrer uniquement les figures présentes plus d'une fois
    passations_actives = {f: ms for f, ms in groupement_passations.items() if len(ms) > 1}
    
    if not passations_actives:
        st.info("💡 Aucune passation détectée. Toutes les figures du thème tracé sont uniques.")
    else:
        for fig, maisons in passations_actives.items():
            meta = PROPRIETES_FIGURES[fig]
            
            with st.expander(f"💠 Figure **{fig}** répétée {len(maisons)} fois dans le thème", expanded=True):
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.markdown(f"**Propriétés de la figure :**")
                    st.markdown(f"- **Nature :** {meta['nature_manuscrit']}")
                    st.markdown(f"- **Comportement :** {meta['groupe']}")
                    st.markdown(f"- **Élément :** {meta['element']}")
                    st.caption(f"🧬 *Morphologie : {meta['morphology']}*")
                    st.caption(f"🔢 *Calcul : {meta['formule_calcul']}*")
                
                with col2:
                    m_source = maisons[0]
                    st.markdown(f"📌 **Maison Source (L'Origine de la situation) :**")
                    st.info(f"**{MAISONS_RAMROU[m_source]['nom']}** : {MAISONS_RAMROU[m_source]['description']}\n\n*Signification brute :* {DICTIONNAIRE_CAS.get(fig, {}).get(m_source, 'Propriété élémentaire standard (voir lecture unitaire).')}")
                    
                    for m_dest in maisons[1:]:
                        st.markdown(f"➔ **Maison de Destination (Là où la cause se manifeste) :**")
                        st.warning(f"**{MAISONS_RAMROU[m_dest]['nom']}** : {MAISONS_RAMROU[m_dest]['description']}\n\n*Signification brute :* {DICTIONNAIRE_CAS.get(fig, {}).get(m_dest, 'Propriété élémentaire standard.')}")
                        
                        # Sentence de passation contextuelle basée sur le groupe dynamique
                        st.markdown("**📜 Sentence d'interprétation de la passation :**")
                        sentence = f"L'énergie générée à la source par **{fig}** en *{MAISONS_RAMROU[m_source]['nom']}* se déplace et vient impacter directement la sphère de *{MAISONS_RAMROU[m_dest]['nom']}*. "
                        
                        if meta['groupe'] == "Mobiles":
                            sentence += "Étant une figure **Mobile**, ce transfert d'énergie ou cet événement va s'accomplir de manière extrêmement rapide, instable ou par vagues successives (changement rapide)."
                        elif meta['groupe'] == "Fixes":
                            sentence += "Étant une figure **Fixe**, la situation s'installe durablement, stagne ou crée un nœud de blocage persistant entre ces deux domaines de votre vie."
                        elif meta['groupe'] == "Sortants":
                            sentence += "Étant une figure **Sortante**, les ressources, les secrets ou les effets fuient le cadre intime initial pour s'extérioriser publiquement."
                        elif meta['groupe'] == "Rentrants":
                            sentence += "Étant une figure **Rentrante**, les conséquences ou les bénéfices de l'affaire reviennent se recentrer directement sur le consultant ou à l'intérieur de son foyer."
                        
                        st.success(sentence)
                        
                # Vérification si un rituel spécifique existe pour cette figure
                if fig in SECRETS_RITUELS:
                    st.markdown(f"🛠️ **Secret de remède / Rituel associé (Nassi) :**")
                    st.code(SECRETS_RITUELS[fig], language="text")

    # ==============================================================================
    # 4. LECTURE TRADITIONNELLE LIGNE PAR LIGNE
    # ==============================================================================
    st.markdown("---")
    st.header("📖 LECTURE UNITAIRE DU THÈME (Maison par Maison)")
    st.write("Interprétation isolée de chaque figure selon son emplacement.")
    
    for m_num, fig_nom in theme_utilisateur.items():
        meta_fig = PROPRIETES_FIGURES[fig_nom]
        signification = DICTIONNAIRE_CAS.get(fig_nom, {}).get(m_num, "La nature élémentaire de la figure s'applique sur cette maison. (Le feu apporte la rapidité, le vent l'instabilité, l'eau la richesse/le bonheur, et la terre l'économie/lenteur).")
        
        with st.expander(f"{MAISONS_RAMROU[m_num]['nom']} ➔ {fig_nom} ({meta_fig['nature_manuscrit']})"):
            st.markdown(f"**Rôle de la Maison :** *{MAISONS_RAMROU[m_num]['description']}*")
            st.markdown(f"**Comportement de la Figure :** `{meta_fig['groupe']}` | **Élément :** `{meta_fig['element']}`")
            st.info(f"🔮 **Interprétation textuelle :** {signification}")

else:
    st.warning("🔒 Veuillez saisir des identifiants valides dans la barre latérale pour déverrouiller l'accès aux données du manuscrit.")
