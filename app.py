import streamlit as st

# 1. Configuration de la page et style de l'interface (Thème sombre et or)
st.set_page_config(page_title="Oracle Géomantique", page_icon="🔮", layout="centered")

st.markdown("""
    <style>
    .reportview-container { background: #0e1117; }
    h1, h2, h3 { color: #FFD700 !important; text-align: center; }
    .stButton>button { 
        background-color: #1e293b; 
        color: #FFD700; 
        border: 1px solid #FFD700;
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
        padding: 10px;
    }
    .stButton>button:hover { background-color: #FFD700; color: #0e1117; }
    .figure-box {
        background-color: #1e293b;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #FFD700;
        margin-bottom: 10px;
    }
    .points-text { 
        font-family: monospace; 
        font-size: 26px; 
        line-height: 1.2;
        color: #FFD700; 
        margin: 10px 0;
    }
    .maison-title {
        font-size: 14px;
        color: #94a3b8;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allowed_html=True)

# =====================================================================
# DICTIONNAIRE COMPLET DES 16 FIGURES GÉOMANTIQUES
# =====================================================================
DICTIONNAIRE_FIGURES = {
    "1.1.1.1": {"nom": "Hibrahim (Via)", "signification": "Le Mouvement, la Route, l'Instabilité. Flux constants et déplacements nécessaires. Annonce privilégiée d'une naissance ou d'une grossesse.", "psaume": "Psaume 120", "saraka": "Partage de fruits ou de friandises à des enfants (Énergie du futur)."},
    "1.1.1.2": {"nom": "Laoussana (Puella)", "signification": "L'
