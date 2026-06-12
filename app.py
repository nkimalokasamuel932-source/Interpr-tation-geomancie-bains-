import streamlit as st
import datetime
import json
import os

# --- 1. BASE DE DONNÉES DES 16 FIGURES ---
PROPRIETES_FIGURES = {
    "Youssouf": {"nature": "Diable Mauvais", "psaume": "Psaume 109", "salomon": "Ô Toi, Architecte des Mondes...", "nassi": "111"},
    "Adama": {"nature": "Lumière", "psaume": "Psaume 23", "salomon": "Source de vie...", "nassi": "99"},
    "Mahdy": {"nature": "Sagesse", "psaume": "Psaume 19", "salomon": "Lumière de l'esprit...", "nassi": "77"},
    "Idriss": {"nature": "Équilibre", "psaume": "Psaume 1", "salomon": "Justice divine...", "nassi": "44"},
    "Ibrahima": {"nature": "Croissance", "psaume": "Psaume 121", "salomon": "Bénédiction du foyer...", "nassi": "121"},
    "Inssa": {"nature": "Épreuve", "psaume": "Psaume 38", "salomon": "Force dans la difficulté...", "nassi": "33"},
    "Omar": {"nature": "Communication", "psaume": "Psaume 15", "salomon": "Clarté du verbe...", "nassi": "88"},
    "Ayoub": {"nature": "Patience", "psaume": "Psaume 42", "salomon": "Paix intérieure...", "nassi": "66"},
    "Allahou": {"nature": "Divinité", "psaume": "Psaume 91", "salomon": "Protection absolue...", "nassi": "999"},
    "Souleymane": {"nature": "Autorité", "psaume": "Psaume 72", "salomon": "Souveraineté sage...", "nassi": "100"},
    "Aliou": {"nature": "Force", "psaume": "Psaume 18", "salomon": "Vigueur combative...", "nassi": "55"},
    "Nouhou": {"nature": "Secret", "psaume": "Psaume 27", "salomon": "Dévoilement des mystères...", "nassi": "22"},
    "Assane": {"nature": "Justice", "psaume": "Psaume 35", "salomon": "Redressement des torts...", "nassi": "90"},
    "Younouss": {"nature": "Abondance", "psaume": "Psaume 65", "salomon": "Récolte spirituelle...", "nassi": "70"},
    "Ousmane": {"nature": "Connaissance", "psaume": "Psaume 119", "salomon": "Lumière du savoir...", "nassi": "11"},
    "Moussa": {"nature": "Libération", "psaume": "Psaume 114", "salomon": "Sortie de captivité...", "nassi": "40"}
}

# --- 2. DICTIONNAIRE DES RÈGLES DE COPULATION ---
REGLES_COPULATIONS = {
    "Moussa": [{"parents": ("Youssouf", "Youssouf"), "verdict": "Trahison collective : Complots secrets en vue."}],
    "Ousmane": [{"parents": ("Youssouf", "Adama"), "verdict": "Secret spirituel : Guide caché dans l'ombre."}],
    "Younouss": [{"parents": ("Youssouf", "Mahdy"), "verdict": "Gain financier : Succès commercial rapide."}],
    "Souleymane": [{"parents": ("Youssouf", "Omar"), "verdict": "Procès : Affaire judiciaire complexe."}],
    "Assane": [{"parents": ("Youssouf", "Inssa"), "verdict": "Honte : Scandale imminent à éviter."}],
    "Aliou": [{"parents": ("Youssouf", "Aliou"), "verdict": "Menace : Risque d'agression physique."}],
    "Ayoub": [{"parents": ("Youssouf", "Nouhou"), "verdict": "Détresse : Sentiment d'abandon total."}]
}

# --- 3. LOGIQUE APP ---
st.set_page_config(page_title="Oracle Ramrou", layout="wide")
st.title("🔮 Oracle Ramrou — Cabinet Théurgique 2026")

if 'theme' not in st.session_state:
    st.session_state.theme = {m: "Youssouf" for m in range(1, 17)}

# Saisie
st.sidebar.header("📥 Saisie du Thème")
cols = st.sidebar.columns(2)
for m in range(1, 17):
    st.session_state.theme[m] = cols[m % 2].selectbox(f"M{m}", list(PROPRIETES_FIGURES.keys()), key=f"m_{m}")

# Analyse
st.header("⚖️ Analyse Théurgique")
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧬 Diagnostic de Copulation")
    figures_dec = [st.session_state.theme[m] for m in range(9, 17)]
    found = False
    for cible, regles in REGLES_COPULATIONS.items():
        for r in regles:
            if r["parents"][0] in figures_dec and r["parents"][1] in figures_dec:
                st.success(f"**{cible}** : {r['verdict']}")
                found = True
    if not found: st.info("Aucune règle de copulation majeure détectée.")

with col2:
    st.subheader("🌿 Pharmacée Spirituelle")
    for fig in set(st.session_state.theme.values()):
        with st.expander(f"👑 {fig}"):
            st.write(f"**Nature :** {PROPRIETES_FIGURES[fig]['nature']}")
            st.write(f"**Psaume :** {PROPRIETES_FIGURES[fig]['psaume']}")
            st.write(f"**Prière :** {PROPRIETES_FIGURES[fig]['salomon']}")

# Sauvegarde
if st.sidebar.button("💾 Enregistrer le Tirage"):
    st.sidebar.success("Tirage enregistré dans la base !")
