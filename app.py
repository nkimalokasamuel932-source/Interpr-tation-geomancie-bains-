# -*- coding: utf-8 -*-
import streamlit as st

# =====================================================================
# 1. DICTIONNAIRE AUTHENTIQUE DES 16 FIGURES (Zoumana Koné-Somadjely)
# =====================================================================
# Base de données immuable contenant les secrets théurgiques et versets bibliques.
FIGURES_DB = {
    "Youssouf (Sedjou / Puer)": {
        "numero": 1, "element": "Feu", "nature": "Passé", "polarite": "Mâle",
        "psaume": "Psaume 35", "verset": "Exode 15 v.3", "sceau": "2e Pentacle de Mars",
        "sacrifice": "Cola rouge, bélier au cou rouge, maïs rouge. À donner aux handicapés ou personnes s'étant blessées le Mardi.",
        "plantes": "Zaban, Balanzan, Poudre de fusil (Arbres : Djala, N'zèrènidjè, Djatiguifaga)"
    },
    "Adama (Letitia / La joie)": {
        "numero": 2, "element": "Feu", "nature": "Passé", "polarite": "Mâle",
        "psaume": "Psaume 4", "verset": "Néhémie 8 v.10", "sceau": "2e Pentacle de Jupiter",
        "sacrifice": "Fruits secs, longs animaux. À donner à plusieurs personnes (Groupe) le Jeudi.",
        "plantes": "Frogofraga, N'gouna, Sérétoro (Arbres : Sana, Gounan)"
    },
    "Mahamadou / Malidjou (Caput Draconis)": {
        "numero": 3, "element": "Air", "nature": "Futur", "polarite": "Femelle",
        "psaume": "Psaume 128", "verset": "Exode 20 v.12", "sceau": "1er Pentacle de la Terre",
        "sacrifice": "Fruits secs, longs animaux. À donner à plusieurs personnes (Groupe) le Jeudi.",
        "plantes": "Arbres qui poussent sur colline ou toile, Djoun (Arbres : Djoulassounkalani, Sébé)"
    },
    "Idrissa (Albayaro / Albus)": {
        "numero": 4, "element": "Eau", "nature": "Futur", "polarite": "Mâle",
        "psaume": "Psaume 119 (Beth)", "verset": "Isaïe 1 v.18", "sceau": "2e Pentacle de Mercure",
        "sacrifice": "Bijoux, objets précieux, offrandes libres. À donner aux enfants le Vendredi.",
        "plantes": "N'gokou, tous les arbres qui vivent sur les fleuves (Arbres : Dougalén)"
    },
    "Ibrahima (Taliki / Via)": {
        "numero": 5, "element": "Eau", "nature": "Présent", "polarite": "Mâle",
        "psaume": "Psaume 120", "verset": "Psaume 121 v.8", "sceau": "5e Pentacle de la Lune",
        "sacrifice": "Fruits frais, graines de céréales, animaux féminins. À donner aux religieux ou personnes s'occupant de la religion le Lundi.",
        "plantes": "Zondjè, arbres poussant au bord des sources d'eau (Arbres : Tièkala, Zongnè)"
    },
    "Issa (Nabbi Issa / Amissio)": {
        "numero": 6, "element": "Eau", "nature": "Passé", "polarite": "Mâle",
        "psaume": "Psaume 102", "verset": "Joël 2 v.25", "sceau": "5e Pentacle de Vénus",
        "sacrifice": "Choses à plusieurs couleurs (pintade, fonio, poule tachetée). À donner à un chanteur, griot ou muezzin le Mercredi.",
        "plantes": "N'gagnaka, Niama, Chi (Arbres : Sourou N'tomo)"
    },
    "Oumarou (Lomara / Rubeus)": {
        "numero": 7, "element": "Air", "nature": "Passé", "polarite": "Femelle",
        "psaume": "Psaume 29", "verset": "Cantique 8 v.6", "sceau": "4e Pentacle de Mars",
        "sacrifice": "Cola rouge, bélier au cou rouge, maïs rouge. À donner aux handicapés ou personnes s'étant blessées le Mardi.",
        "plantes": "Gaba blé, Djati tgui fa djiri (Arbres : Gabablen, Foronto, Wo)"
    },
    "Ayouba (Almangoussi / Tristitia)": {
        "numero": 8, "element": "Terre", "nature": "Futur", "polarite": "Postérieur Mâle",
        "psaume": "Psaume 40", "verset": "Isaïe 61 v.3", "sceau": "5e Pentacle de Saturne",
        "sacrifice": "Tout ce qu'on trouve sous la terre, savon, sel. À donner aux vieilles et vieux le Samedi.",
        "plantes": "Herbes qui poussent sur les tombeaux, Koroni fin (Arbres : Koto, Ngokou)"
    },
    "Qala-llahou (Aboubakr Sidik / Fortuna Minor)": {
        "numero": 9, "element": "Feu", "nature": "Passé", "polarite": "Mâle",
        "psaume": "Psaume 121", "verset": "Psaume 46 v.2", "sceau": "4e Pentacle du Soleil",
        "sacrifice": "Cola blanc, habit blanc, bélier blanc. À donner aux personnages de grande renommée, chefs le Dimanche.",
        "plantes": "Aladjon, racines d'arbres coupant la route (Arbres : Alladjô, Congo Sirani)"
    },
    "Solomana (Manssa Souleymane / Carcer)": {
        "numero": 10, "element": "Terre", "nature": "Présent", "polarite": "Femelle",
        "psaume": "Psaume 142", "verset": "Isaïe 22 v.22", "sceau": "7e Pentacle de Saturne",
        "sacrifice": "Tout ce qu'on trouve sous la terre, savon, sel. À donner aux vieilles et vieux le Samedi.",
        "plantes": "Mandé sounsoun, Sounsoun (Arbres : Zamba, Sira/Baobab)"
    },
    "Badra (Badra Aliou / Conjunctio)": {
        "numero": 11, "element": "Air", "nature": "Présent", "polarite": "Femelle",
        "psaume": "Psaume 133", "verset": "Ruth 1 v.16", "sceau": "4e Pentacle de Mercure",
        "sacrifice": "Choses à plusieurs couleurs (pintade, fonio, poule). À donner à un chanteur, griot ou muezzin le Mercredi.",
        "plantes": "Guélé (Arbres : Triki, Gouélé)"
    },
    "Nouhou (Nouhoum / Cauda Draconis)": {
        "numero": 12, "element": "Terre", "nature": "Futur", "polarite": "Femelle",
        "psaume": "Psaume 59", "verset": "Psaume 68 v.2", "sceau": "6e Pentacle de Saturne",
        "sacrifice": "Cola blanc, habit blanc, bélier blanc. À donner aux renommés, grands personnages le Dimanche.",
        "plantes": "Goundjè (Arbres : Koudjè, Zèguènè)"
    },
    "Laoussana (Alhoussein / Puella)": {
        "numero": 13, "element": "Eau", "nature": "Passé", "polarite": "Femelle",
        "psaume": "Psaume 119 (Aleph)", "verset": "Cantique 4 v.7", "sceau": "2e Pentacle de Vénus",
        "sacrifice": "Tout ce qu'on trouve sous la terre, savon, sel. À donner aux vieilles et vieux le Samedi.",
        "plantes": "Djoulasonkalani (Plantes gluantes, herbes des vieux puits, ravins, rigoles)"
    },
    "Ousmane (Mory Zoumana / Acquisitio)": {
        "numero": 14, "element": "Terre", "nature": "Futur", "polarite": "Mâle",
        "psaume": "Psaume 23", "verset": "Psaume 23 v.1", "sceau": "3e Pentacle de Jupiter",
        "sacrifice": "Fruits secs, longs animaux. À donner à plusieurs personnes (Groupe) le Jeudi.",
        "plantes": "N'doubalé, Frogofraga (Arbres : Troubala, Dougalen, Chou Toro)"
    },
    "Younouss (Tontigui)": {
        "numero": 15, "element": "Air", "nature": "Futur", "polarite": "Femelle",
        "psaume": "Psaume 112", "verset": "Deutéronome 28 v.12", "sceau": "6e Pentacle de Jupiter",
        "sacrifice": "Bijoux, parures ou objets brillants. À donner aux enfants le Vendredi.",
        "plantes": "N'tomotigui, Zondjè (Arbres : Fogofogo)"
    },
    "Moussa (Djama / Populus)": {
        "numero": 16, "element": "Feu", "nature": "Présent", "polarite": "Femelle",
        "psaume": "Psaume 47", "verset": "Genèse 22 v.17", "sceau": "1er Pentacle de la Lune",
        "sacrifice": "Fruits frais, graines de céréales, animaux féminins. À donner aux religieux ou gardiens du culte le Lundi.",
        "plantes": "N'tomi, N'galama (Arbres : Tomy, Sounzoufing)"
    }
}

# =====================================================================
# 2. LOGIQUE D'ANALYSE MATRICIELLE DES 4 ÉLÉMENTS
# =====================================================================
def interpreter_importance_element(element_str):
    if "Feu" in element_str:
        return {
            "icone": "🔥", "titre": "Élément FEU — Dynamique d'Action Absolue et de Rapidité",
            "analyse": "La conclusion du thème est dominée par le Feu. Résolution tranchante et immédiate. Les blocages se consument vite, mais attention aux risques d'emportement ou de stress intense.",
            "conseil": "Agissez promptement. Privilégiez les purifications matinales, l'utilisation de l'encens sacré, et l'action directe sans hésitation."
        }
    elif "Air" in element_str:
        return {
            "icone": "💨", "titre": "Élément AIR — Dynamique de Mouvement, d'Esprit et de Parole",
            "analyse": "Votre issue est portée par les courants de l'Air. Situation extrêmement mobile dépendant de contrats, de négociations, d'écrits ou de l'influence de l'entourage.",
            "conseil": "Misez sur la communication claire, l'onction de parfums subtils et l'élévation de l'esprit pour stabiliser cette énergie volatile."
        }
    elif "Eau" in element_str:
        return {
            "icone": "💧", "titre": "Élément EAU — Dynamique de Fluidité, d'Abondance et de Purification",
            "analyse": "L'Eau gouverne votre sentence finale. Symbole de bénédictions fertiles, de richesse fluide et de réconciliations. Les difficultés tenaces se dissolvent naturellement comme le sel dans l'eau.",
            "conseil": "Le bain thérapeutique (Nassi) et l'utilisation de décoctions liquides purificatrices constituent le cœur stratégique de vos remèdes."
        }
    elif "Terre" in element_str:
        return {
            "icone": "🌱", "titre": "Élément TERRE — Dynamique d'Ancrage, de Secret et de Temps",
            "analyse": "La Terre scelle votre dénouement. Les résultats seront solides et pérennes, mais ils sont soumis aux lois du temps, à de lourdes résistances ou à des secrets bien gardés.",
            "conseil": "Ne forcez pas les événements. Honorez scrupuleusement les aumônes matérielles lourdes, les graines, et utilisez les racines de plantes."
        }
    return {"icone": "✨", "titre": "Élément Équilibré", "analyse": "Forces équilibrées.", "conseil": "Suivez le protocole standard."}

# =====================================================================
# 3. INTERFACE DE SÉCURITÉ ET D'AUTHENTIFICATION
# =====================================================================
st.set_page_config(page_title="Oracle SST Pro", page_icon="🔮", layout="wide")

# Initialisation de l'état de session pour l'accès sécurisé
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_login():
    """Vérifie les informations d'identification saisies."""
    if st.session_state["username"] == "admin" and st.session_state["password"] == "Somadjely2026":
        st.session_state["authenticated"] = True
        st.success("✅ Accès accordé. Bienvenue dans l'interface SST.")
    else:
        st.error("❌ Identifiant ou mot de passe incorrect. Accès refusé.")

# Affichage de l'écran de connexion si non authentifié
if not st.session_state["authenticated"]:
    st.title("🔒 SST SYSTEM — Interface d'Accès Sécurisée")
    st.write("Veuillez saisir vos identifiants pour déverrouiller l'accès au moteur géomantique théurgique.")
    
    with st.form("login_form"):
        st.text_input("👤 Identifiant", key="username")
        st.text_input("🔑 Mot de passe", type="password", key="password")
        st.form_submit_button("Se connecter", on_click=check_login)
    st.stop()

# =====================================================================
# 4. APPLICATION PRINCIPALE (Une fois connecté)
# =====================================================================
st.title("🔮 Système Informatique de Géomancie Traditionnelle — SST Pro")
st.write("Moteur d'analyse thématique basé sur l'enseignement officiel de **Zoumana Koné-Somadjely**.")

# Sélection de la figure finale
figure_choisie = st.selectbox(
    "Choisissez la figure présente en Maison 16 (Sentence finale / Issue ultime) :",
    options=list(FIGURES_DB.keys())
)

if figure_choisie:
    data = FIGURES_DB[figure_choisie]
    
    # Affichage de la fiche technique
    st.subheader(f"📊 Fiche Technique : {figure_choisie}")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Numéro Unique", value=f"N° {data['numero']}")
    with col2:
        st.metric(label="Élément Majeur", value=data['element'])
    with col3:
        st.metric(label="Temps Naturel", value=data['nature'])
    with col4:
        st.metric(label="Polarité de la Figure", value=data['polarite'])

    st.markdown("---")

    # Analyse Matricielle de l'élément
    st.header("🔬 Analyse Élémentaire de l'Issue (Importance Matricielle)")
    info_element = interpreter_importance_element(data['element'])
    
    with st.expander(f"{info_element['icone']} {info_element['titre']}", expanded=True):
        st.markdown(f"**Impact vibratoire sur le thème :** {info_element['analyse']}")
        st.markdown(f"💡 **Recommandation stratégique :** *{info_element['conseil']}*")

    st.markdown("---")

    # Onglets d'ordonnances sacrées et rituelles (Prescriptions)
    st.header("📜 Votre Ordonnance Théurgique et Spirituelle")
    st.write("Appliquez strictement ces directives rituelles pour équilibrer la vibration de cette figure.")
    
    tab1, tab2, tab3 = st.tabs([
        "🐑 1. Sacrifices & Aumônes Spécifiques",
        "✝️ 2. Alignement Théurgique & Versets Bibliques",
        "🌿 3. Pharmacopée & Plantes Associées"
    ])
    
    with tab1:
        st.subheader("Plan d'Aumône Expiatoire Traditionnel")
        st.info(f"**Éléments et matières à offrir :** {data['sacrifice']}")
        st.caption("Note : Respectez scrupuleusement les jours et profils de destinataires indiqués pour valider le travail vibratoire.")
        
    with tab2:
        st.subheader("Composants Théurgiques Divins")
        col_t1, col_t2, col_t3 = st.columns(3)
        with col_t1:
            st.warning(f"📖 **Psaume à tracer :**\n{data['psaume']}")
        with col_t2:
            st.success(f"🔐 **Verset Biblique de Verrouillage :**\n{data['verset']}")
        with col_t3:
            st.info(f"🛡️ **Sceau de Salomon Associé :**\n{data['sceau']}")
            
        st.markdown("""
        ### Protocole d'application théurgique :
        1. **Écriture :** Écrivez le psaume et le verset de verrouillage sur votre support traditionnel de collecte (ardoise).
        2. **Consécration :** Utilisez le sceau de Salomon correspondant pour charger spirituellement l'eau de rinçage (Nassi).
        """)
        
    with tab3:
        st.subheader("Plantes Sacrées de Recouvrement")
        st.success(f"**Végétaux à collecter (Bains, Nassi ou Fumigations) :** {data['plantes']}")
        st.markdown("""
        **Méthode de préparation :**
        * **En Bain de purification :** Faites infuser les feuilles ou écorces récoltées directement dans l'eau sacrée théurgique (Nassi). Lavez-vous avec cette préparation selon les instructions temporelles de la figure.
        * **En Fumigation protectrice :** Pilez ou séchez les plantes pour les diffuser sous forme d'encens sur des charbons ardents.
        """)

    # Pied de page applicatif
    st.markdown("---")
    st.caption("SST Informatique — Application Finale Protégée. Tous droits réservés.")
