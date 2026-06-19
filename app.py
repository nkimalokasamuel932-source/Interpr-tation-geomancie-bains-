import streamlit as st
from engine import OracleRamrouComplet

oracle = OracleRamrouComplet()
st.title("🔮 Oracle géomancie")

# Saisie des figures
theme = {}
cols = st.columns(4)
for i in range(1, 17):
    with cols[(i-1) % 4]:
        theme[f'M{i}'] = st.selectbox(f"M{i}", list(oracle.db.keys()), key=f"M{i}")

# Saisie du sujet
sujet_utilisateur = st.text_input("Posez votre question à l'Oracle :")

if st.button("Obtenir le verdict"):
    if sujet_utilisateur:
        # Appel du moteur intelligent
        resultat = oracle.generer_verdict_intelligent(sujet_utilisateur, theme)
        st.success(resultat)
    else:
        st.warning("Veuillez poser une question pour obtenir une interprétation.")
