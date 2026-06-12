import streamlit as st

# ==============================================================================
# CONFIGURATION DE L'APPLICATION
# ==============================================================================
st.set_page_config(
    page_title="Oracle Ramrou — Grand Grimoire Théurgique", 
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
    1: {"nom": "M1 (Maison de l'Âme)", "description": "L'être physique, sa force, sa personnalité. Décrit le consultant."},
    2: {"nom": "M2 (Maison de la Chance)", "description": "La matérialité de l'argent, les finances et richesses matérielles."},
    3: {"nom": "M3 (Maison des Mères)", "description": "L'entourage proche, les relations de voisinage et courts déplacements."},
    4: {"nom": "M4 (Maison des Pères)", "description": "Le patrimoine familial, l'immobilier, le foyer et la fin des choses."},
    5: {"nom": "M5 (Maison des Enfants)", "description": "Les plaisirs, la vie amoureuse, la créativité, les lettres et la descendance."},
    6: {"nom": "M6 (Maison des Malades)", "description": "Le travail quotidien, la santé, les épreuves et les blocages corporels."},
    7: {"nom": "M7 (Maison du Mariage)", "description": "Le conjoint, l'épouse, les contrats, les associations et les rivaux ouverts."},
    8: {"nom": "M8 (Maison du Changement)", "description": "La tombe, l'extérieur, l'étranger, les peurs et transformations radicales."},
    9: {"nom": "M9 (Maison de Dieu)", "description": "La spiritualité, la religion, les écrits de haute science et les grands voyages."},
    10: {"nom": "M10 (Maison des Rois)", "description": "Le travail, la réalisation sociale, le pouvoir, les honneurs et l'élévation professionnelle."},
    11: {"nom": "M11 (Maison de l'Espoir)", "description": "Les projets, les espoirs futurs, les cercles d'amis et les promesses."},
    12: {"nom": "M12 (Maison des Ennemis)", "description": "Les blocages cachés, la méchanceté sournoise, le maraboutage et les pièges d'ennemis dissimulés."},
    13: {"nom": "M13 (Maison de la Chambre)", "description": "L'intimité du foyer, le lit conjugal, les secrets de chambre et le présent immédiat."},
    14: {"nom": "M14 (Maison des Fortunes)", "description": "Les gains futurs, le commerce à venir et les rentrées financières décalées."},
    15: {"nom": "M15 (Maison de l'Espace)", "description": "Les rumeurs, l'ambiance environnante, la clarté d'esprit et le juge de synthèse."},
    16: {"nom": "M16 (Maison de Finition)", "description": "La conclusion ultime, irrévocable et le décret divin final sur l'affaire."}
}

DICTIONNAIRE_CAS = {
    "Adama": {
        1: "Joie intérieure intense, élévation, l'âme est en paix parfaite.",
        2: "Chance financière rapide, acquisition matérielle imminente.",
        3: "Relations de voisinage excellentes, démarches fructueuses.",
        4: "Paix absolue au foyer, stabilité totale du patrimoine immobilier.",
        7: "Union heureuse et sincère, mariage béni ou contrat commercial validé.",
        12: "Annonce un blocage temporaire, votre chance excite la jalousie secrète des autres.",
        16: "Conclusion lumineuse : annonce une bonne nouvelle définitive pour l'affaire."
    },
    "Mahdy": {
        1: "Annonce une élévation morale ou spirituelle, besoin de hauteur difficile à atteindre.",
        2: "Annonce des profits et gains importants, augmentation de la chance commerciale.",
        7: "Prévoit une très bonne union, une excellente association basée sur la sagesse et la sincérité.",
        12: "Annonce des difficultés d'ordre administratif ou des risques d'enfermement mystique.",
        16: "L'affaire se conclut sur un compromis hautement profitable et pérenne."
    },
    "Nouhou": {
        1: "L'esprit traverse une tempête, résistance face à l'adversité.",
        6: "Maladie rampante ou fatigue physique liée à une charge mystique négative.",
        12: "Attaques mystiques intenses de l'entourage, tentative de blocage total de votre destin.",
        16: "Délivrance finale accordée après une épreuve de foi majeure."
    },
    "Omar": {
        1: "Annonce une révolte interne, des colères dévastatrices ou une rancœur installée.",
        2: "Fatigue financière sévère, blocage de l'argent dû à des conflits d'intérêt.",
        7: "Grave crise conjugale, partenaire colérique ou violences verbales destructrices.",
        10: "Conflit direct avec la justice, l'autorité patronale ou risque de blâme sévère.",
        16: "Annonce de la frustration et des blocages persistants en fin de course."
    },
    "Moussa": {
        1: "Annonce le rassemblement, le voyage, les réunions collectives ou le retour des alliés.",
        2: "Annonce la chance globale, le succès commercial et les profits partagés à plusieurs.",
        4: "Réunion de famille importante ou arbitrage nécessaire concernant l'héritage.",
        16: "Finition complète. Le projet ou l'épreuve se termine pour ouvrir un nouveau cycle de gloire."
    }
}

# ==============================================================================
# 2. BASE DE DONNÉES INTEGRALE DES SECRETS EN BOTANIQUE & THÉURGIE
# ==============================================================================
SECRETS_RITUELS = {
    "Adama": {
        "titre": "✨ BAIN DE GRANDE OUVERTURE & CHANCE FINANCIÈRE RAPIDE",
        "nassi": "Tracer la figure Adama exactement 1836 fois sur l'ardoise traditionnelle (Wala).",
        "paroles_sacrees": "Programmer l'eau avec le Psaume 23 (L'Éternel est mon berger) ou la Sourate Al-Fath (La Victoire éclatante) répété(e) 41 fois.",
        "plantes_traditionnelles": "🌿 Cueillir des feuilles fraîches de Basilic sacré (Fereb) et des écorces de Manguier sauvage. Piler le tout énergiquement dans un mortier propre et faire macérer dans le Nassi pendant 3 heures.",
        "huiles_essentielles": "💧 Ajouter 7 gouttes d'huile essentielle de Bergamote (Aimant à prospérité) et 3 gouttes de Cannelle d'écorce (Vitesse d'action) préalablement diluées dans un peu de lait frais.",
        "oraison_salomonique": "« Ô Dieu de Lumière et de Clarté, par la Sagesse infinie accordée au Roi Salomon, commande à Tes Anges d'ouvrir les écluses des cieux. Que les verrous de la pauvreté se brisent et que l'or vienne à moi comme l'eau descend de la montagne. Au nom du Très-Haut. Amen. »",
        "bain_mode": "Jeter 7 morceaux de charbon ardent dans le seau. Se laver tout le corps pendant 7 jours consécutifs, impérativement à l'aube (entre 7h et 8h du matin).",
        "sadaka": "Offrir 7 morceaux de sucre, 7 colas blanches et un coq blanc à un nécessiteux."
    },
    "Ousmane": {
        "titre": "👁️ BAIN DE VISION NOCTURNE, RECOUVREMENT DE MÉMOIRE & CLARTÉ MENTALE",
        "nassi": "Écrire la figure Ousmane 88 fois à l'aide d'un calame et de l'encre de datte noire.",
        "paroles_sacrees": "Infuser dans le récipient le Psaume 119:105 (Ta parole est une lampe...) ou le Verset de la Lumière (Ayat Al-Nur) récité 7 fois de suite.",
        "plantes_traditionnelles": "🌿 Sommités fleuries de Romarin frais et feuilles de Menthe poivrée sauvage. Froisser les feuilles à la main directement dans l'eau sacrée en visualisant la dissipation des brumes mentales.",
        "huiles_essentielles": "💧 5 gouttes d'huile essentielle d'Encens Oliban (Haute connexion) et 4 gouttes de Menthe Poivrée (Activation sensorielle et ouverture du troisième œil).",
        "oraison_salomonique": "« Esprit Éternel qui as instruit Salomon au travers de visions claires et de songes nocturnes sacrés, nettoie mon miroir intérieur. Ôte le voile noir posé sur mes yeux pour que je voie la vérité derrière le mensonge des hommes. Amen. »",
        "bain_mode": "Se laver le visage et la tête 3 fois de suite chaque soir avant le coucher, puis boire une petite gorgée du liquide. Durée : 15 nuits d'affilée.",
        "sadaka": "Faire l'aumône d'un litre de lait frais de vache et d'une grande bougie blanche un jeudi soir."
    },
    "Nouhou": {
        "titre": "🛡️ BAIN DE BRISAGE DE MARABOUTAGE, RETOUR À L'ENVOYEUR & EXORCISME",
        "nassi": "Écrire la figure redoutable de Nouhou 1111 fois sur l'ardoise en bois.",
        "paroles_sacrees": "Associer le Psaume 91 (Sous l'abri du Très-Haut) ou les Versets de l'Annulation de la Magie (Sourate Yunus, v.81-82) écrit textuellement 12 fois sur le bois.",
        "plantes_traditionnelles": "🌿 Feuilles amères de Citronnier sauvage (Kankaliba) et écorces séchées de Neem (Gouro). Faire bouillir ces plantes dans une marmite neuve avec le Nassi recueilli.",
        "huiles_essentielles": "💧 Ajouter 9 gouttes d'huile essentielle d'Arbre à thé (Purification spirituelle majeure) et 5 gouttes de Laurier Noble (Garant de la victoire contre les forces de l'ombre).",
        "oraison_salomonique": "« Par le Sceau Sacré du Roi Salomon, par l'épée de l'Archange de Justice, je brise, j'annule et je détruis tout décret de sorcellerie prononcé contre mon nom. Que le feu divin consume les pièges cachés et que le mal retourne à son auteur. Amen. »",
        "bain_mode": "Coupler le mélange avec une poignée de gros sel ou de l'eau de mer. Se laver intégralement 12 fois de suite au cours de la même nuit (entre minuit et 3h du matin). Ne pas se sécher.",
        "sadaka": "Sacrifier et distribuer 3kg de riz blanc ou de mil un vendredi à l'heure de la prière."
    },
    "Moussa": {
        "titre": "👑 BAIN DE GRANDE POPULARITÉ, PRESTIGE & ATTRACTION DE FOULE",
        "nassi": "Tracer scrupuleusement la figure souveraine de Moussa exactement 6666 fois.",
        "paroles_sacrees": "Réciter au-dessus de l'eau sacrée le Psaume 8 ou le Verset d'attraction de Joseph (Youssouf) 110 fois avec ferveur.",
        "plantes_traditionnelles": "🌿 Pétales fraîches de Rose rouge de jardin, feuilles de Verveine odorante et morceaux d'écorce d'Iroko sacré (arbre de royauté) séchés au soleil et pilés.",
        "huiles_essentielles": "💧 Intégrer au Nassi 12 gouttes d'huile essentielle d'Ylang-Ylang complète (Charme magnétique puissant) et 7 gouttes de Patchouli ambré (Ancrage du leadership matériel).",
        "oraison_salomonique": "« Éternel, Souverain des mondes, Toi qui as revêtu Salomon d'une splendeur royale telle que les rois de la terre venaient l'admirer, accorde-moi ce jour la grâce et la faveur aux yeux de la multitude. Que mon nom inspire le respect et la bienveillance. Amen. »",
        "bain_mode": "Mélanger le Nassi avec 8 flacons de parfums différents de haute dévotion (sans alcool). Se laver le corps entier, de la tête aux pieds, matin et soir pendant 28 jours.",
        "sadaka": "Distribuer 16 miches de pain blanc frais à l'aube ou faire le don d'un bélier blanc sans tache."
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
    st.sidebar.success("🔓 Sceaux brisés. Accès aux arcanes autorisé.")
    
    # Formulaire de saisie des maisons géomantiques
    st.sidebar.header("📥 Configuration des 16 Maisons")
    liste_figures = list(PROPRIETES_FIGURES.keys())
    theme_utilisateur = {}
    
    # Regroupement par quaternaires traditionnels pour fluidifier la saisie
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
    st.write("Le système cherche les figures identiques qui migrent d'une maison à l'autre pour déterminer la source du problème et éditer le remède.")
    
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
                            phrase_flux += "La figure étant **Sortante**, l'énergie ou les bénéfices ont tendance à s'échapper vers l'extérieur du cercle familial."
                        elif meta['groupe'] == "Rentrants":
                            phrase_flux += "La figure étant **Rentrante**, les retombées karmiques ou financières reviennent se concentrer au cœur du foyer."
                        st.write(phrase_flux)
                
                # ==============================================================================
                # 5. CHARGEMENT AUTOMATIQUE DES REMÈDES BOTANIQUES ET THÉURGIQUES
                # ==============================================================================
                if fig in SECRETS_RITUELS:
                    st.markdown("### 🛁 REMÈDE BOTANIQUE ET THÉURGIQUE SUR MESURE")
                    rituel = SECRETS_RITUELS[fig]
                    
                    st.error(f"📋 PROTOCOLE DE PURIFICATION INTÉGRAL : {rituel['titre']}")
                    
                    col_gauche, col_droite = st.columns(2)
                    with col_gauche:
                        st.markdown(f"✍️ **1. Rédaction du Nassi :**\n{rituel['nassi']}")
                        st.markdown(f"📖 **2. Parole et Programmation Vibratoire :**\n*{rituel['paroles_sacrees']}*")
                        st.markdown(f"🌿 **3. Plantes Aromatiques Indigènes (La Charge Terrestre) :**\n**{rituel['plantes_traditionnelles']}**")
                        st.markdown(f"🧪 **4. Huiles Essentielles Clés (Le Fixateur d'Esprit) :**\n{rituel['huiles_essentielles']}")
                    
                    with col_droite:
                        st.info(f"👑 **5. Haute Oraison Salomonique (À réciter à voix haute pendant le bain) :**\n*{rituel['oraison_salomonique']}*")
                        st.markdown(f"🧼 **6. Exécution du Bain :**\n{rituel['bain_mode']}")
                        st.markdown(f"🐐 **7. Libération Karmique (Sadaka obligatoire) :**\n{rituel['sadaka']}")
                else:
                    st.caption("ℹ️ Aucun protocole herboriste lourd n'est encodé pour cette figure. Utiliser un bain générique composé de sel marin, de feuilles de menthe et de 3 gouttes d'huile essentielle d'Encens.")
                
                st.markdown("<hr style='border-top: 3px double #bbb;'>", unsafe_allow_html=True)

    # ==============================================================================
    # 6. DICTIONNAIRE GENERAL DES 16 MAISONS (VISUALISATION UNITAIRE)
    # ==============================================================================
    st.markdown("---")
    st.header("📖 LECTURE COMPLÈTE DU THÈME (Maison par Maison)")
    st.write("Déroulez chaque section pour analyser l'état vibratoire unitaire de vos secteurs de vie.")
    
    for m_num, fig_nom in theme_utilisateur.items():
        meta_fig = PROPRIETES_FIGURES[fig_nom]
        signification_maison = DICTIONNAIRE_CAS.get(fig_nom, {}).get(m_num, "Analyse élémentaire : L'élément de la figure vient interagir directement avec l'axe de la maison.")
        
        with st.expander(f"📍 {MAISONS_RAMROU[m_num]['nom']} ➔ Figure présente : {fig_nom}"):
            st.markdown(f"**Rôle de ce secteur :** *{MAISONS_RAMROU[m_num]['description']}*")
            st.markdown(f"**Fiche d'identité :** Caractère `{meta_fig['nature_manuscrit']}` | Énergie `{meta_fig['groupe']}` | Élément `{meta_fig['element']}`")
            st.info(f"🔮 **Verdict du manuscrit :** {signification_maison}")

else:
    st.warning("🔒 Accès verrouillé. Les secrets du Nassi et de la botanique sacrée exigent les identifiants d'initié valides.")
