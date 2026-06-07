import streamlit as st

# =====================================================================
# 1. DICTIONNAIRE DE RÉFÉRENCE DES 16 FIGURES (Géomancie Ramrou)
# =====================================================================
# Données extraites rigoureusement des manuels de référence (Ramrou & Kamagaté)
FIGURES_DB = {
    "Youssouf": {
        "numero": 1,
        "element": "Feu",
        "nature": "Feu de braise",
        "polarite": "Diable (Mauvais)",
        "sacrifice": "Pagne ou tissu noir, 1 litre de lait, 3 ou 7 colas blancs. À donner à un homme le jeudi matin.",
        "plantes": "Balanzan (Acacia albida), Diatigui Faga (Ficus sp.)"
    },
    "Adama": {
        "numero": 2,
        "element": "Feu",
        "nature": "Mer / Courant électrique / Lumière",
        "polarite": "Diable (Bon)",
        "sacrifice": "Tissu noir, 1 litre de lait, 3 ou 7 colas blancs. À donner à un homme le jeudi matin ou mercredi.",
        "plantes": "N'gouna (Scléroarya birréa), Djalan (Khaya senegalensis), Zeguelin"
    },
    "Mahdy": {
        "numero": 3,
        "element": "Air",
        "nature": "Vent fort, tornade",
        "polarite": "Diable (Bon)",
        "sacrifice": "7 kg de sel, une paire de chaussures noires à donner à une femme entre 17h et 21h (Lundi ou Jeudi).",
        "plantes": "Sébé (Rônier / Borassus aethiopum), Tabacouba (Detarium senegalense)"
    },
    "Idriss": {
        "numero": 4,
        "element": "Eau",
        "nature": "Fleuve",
        "polarite": "Diable (Bon)",
        "sacrifice": "7 kg de sel, une paire de chaussures noires à donner à une femme entre 22h et 00h (Lundi ou Jeudi).",
        "plantes": "N'Gokoun (Nénuphar / Nymphaea lotus)"
    },
    "Ibrahima": {
        "numero": 5,
        "element": "Eau",
        "nature": "Vent maléfique",
        "polarite": "Humain (Bon)",
        "sacrifice": "6 litres de lait avec un coq rouge ou un mouton. À donner à un homme le lundi entre 13h et 15h.",
        "plantes": "Zaba (Landolphia owariensis), Karo"
    },
    "Inssa": {
        "numero": 6,
        "element": "Eau",
        "nature": "La pluie",
        "polarite": "Humain (Mauvais)",
        "sacrifice": "6 litres de lait avec un coq blanc ou une chèvre. À donner à un homme le mardi entre 17h et 18h.",
        "plantes": "Kèlètiguè yiri, Triqi (Combretum glutinosum)"
    },
    "Omar": {
        "numero": 7,
        "element": "Air",
        "nature": "Vent",
        "polarite": "Diable (Mauvais)",
        "sacrifice": "Chèvre ou mouton blanc, ou coq rouge. À donner à une femme le mardi ou samedi entre 22h et 00h.",
        "plantes": "Kaba houlé (Ficus platyphylla)"
    },
    "Ayoub": {
        "numero": 8,
        "element": "Terre",
        "nature": "La tombe",
        "polarite": "Diable (Mauvais)",
        "sacrifice": "Mouton blanc ou coq blanc. À donner à un homme le mardi ou samedi entre 10h et 12h.",
        "plantes": "Plantes de cimetière, racines profondes"
    },
    "Allahou": {
        "numero": 9,
        "element": "Feu",
        "nature": "Le désert",
        "polarite": "Humain (Mauvais)",
        "sacrifice": "Un boubou ou pagne déjà porté, de la viande. À donner à des hommes le dimanche entre 13h et 15h.",
        "plantes": "Plantes épineuses du désert"
    },
    "Soulaymane": {
        "numero": 10,
        "element": "Terre",
        "nature": "Montagne",
        "polarite": "Humain (Bon)",
        "sacrifice": "3 plats de riz avec de la viande. À donner à une femme entre 18h et 20h, peu importe le jour.",
        "plantes": "Arbres massifs à écorce dure"
    },
    "Aliou": {
        "numero": 11,
        "element": "Air",
        "nature": "Fumée",
        "polarite": "Humain (Mauvais)",
        "sacrifice": "3 kilos de riz, 3 kilos de mil, 7 colas blancs. À donner à un homme entre 18h et 22h.",
        "plantes": "Plantes à sève laiteuse"
    },
    "Nouhou": {
        "numero": 12,
        "element": "Terre",
        "nature": "Vent",
        "polarite": "Humain (Bon)",
        "sacrifice": "Un coq rouge, 3 kilos de maïs, 7 colas rouges. À donner à une femme le vendredi entre 20h et 22h.",
        "plantes": "Plantes de nettoyage ou de lavage spirituel"
    },
    "Assane": {
        "numero": 13,
        "element": "Eau",
        "nature": "Le sable",
        "polarite": "Diable (Mauvais)",
        "sacrifice": "Un plat de riz avec de la viande de coq. À donner à des femmes le samedi entre 10h et 12h.",
        "plantes": "Plantes rampantes des zones sablonneuses"
    },
    "Younouss": {
        "numero": 14,
        "element": "Terre",
        "nature": "Vent froid et lourd",
        "polarite": "Diable (Bon)",
        "sacrifice": "Un plat de riz avec un cola blanc. À donner à une femme le vendredi entre 13h et 15h.",
        "plantes": "Plantes de récolte ou arbres fruitiers"
    },
    "Ousmane": {
        "numero": 15,
        "element": "Air",
        "nature": "Eau de puits",
        "polarite": "Humain (Bon)",
        "sacrifice": "3 plats de riz avec 10 colas blancs. À donner à des hommes le dimanche entre 17h et 18h.",
        "plantes": "Plantes aquatiques douces, lianes d'eau"
    },
    "Moussa": {
        "numero": 16,
        "element": "Feu",
        "nature": "La cendre",
        "polarite": "Humain (Mauvais)",
        "sacrifice": "Tissu blanc, un coq blanc, de la viande de chèvre. À donner à des hommes le dimanche à 06h du matin.",
        "plantes": "Arbres produisant beaucoup de cendre, plantes de protection"
    }
}

MAISONS_NOMS = {
    1: "Maison de l'âme (M1)",
    2: "Maison de la chance / Fortune (M2)",
    3: "Maison des frères / Mères / Entourage (M3)",
    4: "Maison du patrimoine / Pères / Foyer (M4)",
    5: "Maison des enfants / Amours (M5)",
    6: "Maison des maladies / Obstacles (M6)",
    7: "Maison du mariage / Associés (M7)",
    8: "Maison de la mort / Changement (M8)",
    9: "Maison des voyages / Dieu (M9)",
    10: "Maison du pouvoir / Succès professionnel (M10)",
    11: "Maison des espoirs / Amis (M11)",
    12: "Maison des ennemis / Blocages secrets (M12)",
    13: "Maison du lit / Intimité / Argent présent (M13)",
    14: "Maison des gains futurs / Clôture (M14)",
    15: "Maison du juge / Clarté du thème (M15)",
    16: "Maison de la sentence finale / Issue (M16)"
}

# =====================================================================
# 2. LOGIQUE D'INTERPRÉTATION MATRICIELLE DES 4 ÉLÉMENTS
# =====================================================================
def interpreter_importance_element(element_str):
    """Génère l'analyse de l'importance de l'élément de la sentence finale (M16)."""
    if "Feu" in element_str:
        return {
            "icone": "🔥",
            "titre": "Élément FEU - Dynamique d'Action Absolue et de Rapidité",
            "analyse": "La conclusion de votre thème est dominée par le Feu. Cela indique une résolution tranchante, immédiate ou exigeant de vous un courage martial. Les blocages se consument vite sous cette influence, mais attention aux risques d'emportement, de litiges ou de stress intense.",
            "conseil": "Agissez promptement. Privilégiez les purifications matinales, l'utilisation de l'encens sacré, et l'action directe sans hésitation."
        }
    elif "Air" in element_str:
        return {
            "icone": "💨",
            "titre": "Élément AIR - Dynamique de Mouvement, d'Esprit et de Parole",
            "analyse": "Votre issue est portée par les courants de l'Air. Votre situation est extrêmement mobile et dépend de contrats, de négociations, d'écrits ou de l'influence de votre entourage. L'instabilité actuelle précède une transition importante.",
            "conseil": "Misez sur la communication claire, l'onction de parfums subtils et l'élévation de l'esprit pour stabiliser et orienter cette énergie volatile."
        }
    elif "Eau" in element_str:
        return {
            "icone": "💧",
            "titre": "Élément EAU - Dynamique de Fluidité, d'Abondance et de Purification",
            "analyse": "L'Eau gouverne votre sentence finale. C'est le symbole des bénédictions fertiles, de la richesse fluide, des réconciliations amicales ou amoureuses. Les difficultés tenaces se dissolvent naturellement comme le sel dans l'eau, bien que l'évolution puisse demander de la patience.",
            "conseil": "Le bain thérapeutique (Nassi) et l'utilisation de décoctions liquides purificatrices constituent le cœur stratégique de vos remèdes."
        }
    elif "Terre" in element_str:
        return {
            "icone": "🌱",
            "titre": "Élément TERRE - Dynamique d'Ancrage, de Secret et de Temps",
            "analyse": "La Terre scelle votre dénouement. Les résultats obtenus sous cette influence seront solides et pérennes, mais ils sont soumis aux lois du temps, à de lourdes résistances ou à des secrets. Les retards administratifs ou matériels font partie du processus.",
            "conseil": "Ne forcez pas les événements. Honorez scrupuleusement les aumônes matérielles lourdes (Saraka), les graines, et utilisez les racines de plantes pour débloquer le sol."
        }
    else:
        return {
            "icone": "✨",
            "titre": "Élément Équilibré / Neutre",
            "analyse": "L'influence élémentaire demande un rééquilibrage global des différentes forces en présence.",
            "conseil": "Suivez rigoureusement l'ensemble des prescriptions sans sauter d'étape."
        }

# =====================================================================
# 3. INTERFACE UTILISATEUR STREAMLIT
# =====================================================================
st.set_page_config(page_title="Oracle Ramrou Pro", page_icon="🔮", layout="wide")

st.title("🔮 Oracle de Géomancie Ramrou - Ordonnance Spirituelle Avancée")
st.write("Saisissez la figure présente dans la **Maison 16 (Sentence finale)** pour générer l'analyse complète, l'évaluation élémentaire et les remèdes sacrés.")

# Sélection de la figure finale
figure_choisie = st.selectbox(
    "Choisissez la figure de la Maison 16 (Issue du thème) :",
    options=list(FIGURES_DB.keys())
)

if figure_choisie:
    data = FIGURES_DB[figure_choisie]
    
    # Affichage de la carte d'identité de la figure
    st.subheader(f"📊 Fiche Technique : Figure {figure_choisie}")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Numéro Unique", value=f"N° {data['numero']}")
    with col2:
        st.metric(label="Élément Majeur", value=data['element'])
    with col3:
        st.metric(label="Nature Symbolique", value=data['nature'])
    with col4:
        st.metric(label="Polarité Spirituelle", value=data['polarite'])

    st.markdown("---")

    # =====================================================================
    # NOUVEAU BLOC : L'IMPORTANCE DE L'ÉLÉMENT (Correction de l'erreur)
    # =====================================================================
    st.header("🔬 Analyse Élémentaire de l'Issue (L'Importance Matricielle)")
    
    # Correction de l'erreur : On passe directement l'élément propre de la base de données
    info_element = interpreter_importance_element(data['element'])
    
    with st.expander(f"{info_element['icone']} {info_element['titre']}", expanded=True):
        st.markdown(f"**Impact vibratoire sur votre vie :** {info_element['analyse']}")
        st.markdown(f"💡 **Recommandation stratégique :** *{info_element['conseil']}*")

    st.markdown("---")

    # =====================================================================
    # 4. ONGLETS DE PRESCRIPTION PROTOCOLAIRE (L'Ordonnance)
    # =====================================================================
    st.header("📜 Votre Ordonnance Spirituelle Personnalisée")
    st.write("Appliquez ces directives dans l'ordre pour canaliser positivement l'énergie de la sentence.")
    
    tab1, tab2, tab3 = st.tabs([
        "🐑 1. Sacrifices & Aumônes (Saraka)",
        "🌿 2. Pharmacopée & Plantes Associées",
        "📝 3. Directives Protocolaires Rituelles"
    ])
    
    with tab1:
        st.subheader("Plan d'Aumône Expiatoire ou d'Ouverture")
        st.info(f"**Action requise :** {data['sacrifice']}")
        st.caption("Note : Respectez impérativement les créneaux horaires et les profils des destinataires indiqués pour valider le travail vibratoire.")
        
    with tab2:
        st.subheader("Plantes Sacrées Liées à la Figure")
        st.success(f"**Végétaux à utiliser (Bains, Nassi ou Fumigations) :** {data['plantes']}")
        st.markdown("""
        **Comment exploiter ces plantes ?**
        * **En Bain (Nassi) :** Écrire la figure le nombre de fois requis, rincer le support avec de l'eau, puis y infuser ou piler les feuilles des plantes indiquées avant le lavage[cite: 23, 26].
        * **En Fumigation :** Faire sécher les écorces ou feuilles pour les consumer sur des braises de purification.
        """)
        
    with tab3:
        st.subheader("Règles d'Or pour le Praticien et le Consultant")
        st.markdown(f"""
        1. **Alignement :** La figure finale exprime l'aboutissement de la Maison 15 (Juge). Ne tentez pas de contrecarrer une figure de Terre par la précipitation, ni une figure de Feu par l'inaction.
        2. **Intention :** Avant toute manipulation des plantes ou distribution de l'aumône, formulez clairement votre vœu à l'Est[cite: 910, 915, 916].
        3. **Pureté :** Opérez toujours en état de purification corporelle et spirituelle complète[cite: 910, 914].
        """)

    # Pied de page applicatif
    st.markdown("---")
    st.caption("Application Pro d'Interprétation Ramrou — Basée sur la tradition géomantique authentique d'Afrique de l'Ouest[cite: 1, 1089, 1092].")
