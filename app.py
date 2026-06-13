import streamlit as st

# ==============================================================================
# BASE DE DONNÉES COMPLÈTE
# ==============================================================================
PROTOCOLE_COMPLET = {
    "Youssouf": {"el": "Feu", "couleur": "Rouge", "heure": "Mardi, Aube", "support": "Papier/Encre Safran", "cloture": "Psaume 117", "sadaka": "Pain et dattes"},
    "Adama": {"el": "Terre", "couleur": "Vert", "heure": "Samedi, Soir", "support": "Ardoise/Craie blanche", "cloture": "Psaume 128", "sadaka": "Pièces de monnaie"},
    "Mahdy": {"el": "Air", "couleur": "Jaune", "heure": "Mercredi, Midi", "support": "Papier blanc", "cloture": "Psaume 150", "sadaka": "Sucre et lait"},
    "Idriss": {"el": "Eau", "couleur": "Bleu", "heure": "Lundi, Aube", "support": "Feuille d'arbre", "cloture": "Psaume 23", "sadaka": "Eau pure"},
    "Ibrahima": {"el": "Eau", "couleur": "Blanc", "heure": "Jeudi, Aube", "support": "Papier/Encre Noire", "cloture": "Psaume 112", "sadaka": "Lait"},
    "Inssa": {"el": "Eau", "couleur": "Bleu pâle", "heure": "Lundi, Nuit", "support": "Ardoise", "cloture": "Psaume 6", "sadaka": "Aumône nécessiteux"},
    "Omar": {"el": "Air", "couleur": "Gris", "heure": "Mercredi, Coucher", "support": "Parchemin", "cloture": "Psaume 35", "sadaka": "Sucre"},
    "Ayoub": {"el": "Terre", "couleur": "Marron", "heure": "Samedi, Nuit", "support": "Terre cuite", "cloture": "Psaume 88", "sadaka": "Céréales"},
    "Allahou": {"el": "Feu", "couleur": "Rouge vif", "heure": "Mardi, Midi", "support": "Papier/Encre Safran", "cloture": "Psaume 91", "sadaka": "Pain"},
    "Souleymane": {"el": "Terre", "couleur": "Or", "heure": "Samedi, Aube", "support": "Parchemin", "cloture": "Psaume 72", "sadaka": "Pièces"},
    "Aliou": {"el": "Air", "couleur": "Violet", "heure": "Mercredi, Aube", "support": "Papier blanc", "cloture": "Psaume 144", "sadaka": "Eau sucrée"},
    "Nouhou": {"el": "Terre", "couleur": "Noir", "heure": "Samedi, Minuit", "support": "Ardoise", "cloture": "Psaume 29", "sadaka": "Céréales"},
    "Assane": {"el": "Eau", "couleur": "Bleu", "heure": "Lundi, Midi", "support": "Papier/Encre Safran", "cloture": "Psaume 3", "sadaka": "Lait"},
    "Younouss": {"el": "Terre", "couleur": "Vert", "heure": "Samedi, Aube", "support": "Parchemin", "cloture": "Psaume 4", "sadaka": "Pièces"},
    "Ousmane": {"el": "Air", "couleur": "Bleu ciel", "heure": "Mercredi, Nuit", "support": "Feuille", "cloture": "Psaume 119", "sadaka": "Sucre"},
    "Moussa": {"el": "Feu", "couleur": "Rouge", "heure": "Mardi, Midi", "support": "Papier/Encre Safran", "cloture": "Psaume 68", "sadaka": "Dattes"}
}

# ==============================================================================
# INTERFACE
# ==============================================================================
st.set_page_config(page_title="Oracle Ramrou", layout="wide")
st.title("🔮 Oracle Ramrou — Système Théurgique Complet")

# Sidebar
st.sidebar.header("Paramètres")
juge_select = st.sidebar.selectbox("Sélectionnez le Juge (M16) :", list(PROTOCOLE_COMPLET.keys()))

# Main Display
if juge_select:
    data = PROTOCOLE_COMPLET[juge_select]
    
    st.subheader(f"⚖️ Protocole pour la figure : {juge_select}")
    
    # Utilisation de colonnes pour une meilleure lisibilité
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### 🔑 Ouverture & Préparation")
        st.info(f"**Heure Planétaire :** {data['heure']}")
        st.info(f"**Support Rituel :** {data['support']}")
        st.info(f"**Couleur (Bougie) :** {data['couleur']}")
        
    with col2:
        st.write("### 🔒 Clôture & Équilibre")
        st.warning(f"**Rituel de fermeture :** {data['cloture']}")
        st.success(f"**Sadaka obligatoire :** {data['sadaka']}")
        
    st.divider()
    st.write("💡 *Note : Assurez-vous d'être dans un état de calme absolu avant de commencer.*")
else:
    st.write("Veuillez sélectionner une figure dans le menu latéral pour afficher le protocole.")
