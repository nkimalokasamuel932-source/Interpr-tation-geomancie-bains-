import streamlit as st
from engine import OracleRamrouComplet

oracle = OracleRamrouComplet()
st.title("🔮 Oracle de geomancie - Consultation Biblique")

# Saisie des figures
theme = {f'M{i}': st.selectbox(f"Maison {i}", list(oracle.db.keys())) for i in range(1, 17)}

sujet = st.text_input("Posez votre question :")

if st.button("Obtenir le verdict détaillé"):
    # 1. Calcul du verdict selon le sujet
    if "mariage" in sujet.lower():
        res = oracle.copuler(oracle.copuler(theme['M1'], theme['M7']), theme['M5'])
        st.subheader(f"Verdict : {res}")
    else:
        res = oracle.copuler(theme['M15'], theme['M16'])
        st.subheader(f"Verdict : {res}")
    
    # 2. Affichage des détails techniques
    st.write("---")
    st.markdown(oracle.get_details(res))
    
    # 3. Explication des passations (les témoins)
    st.write("---")
    st.subheader("Analyse des Passations")
    st.write(f"Témoin 1 (Passation) : {oracle.copuler(theme['M1'], theme['M2'])}")
    st.write(f"Témoin 2 (Passation) : {oracle.copuler(theme['M15'], theme['M16'])}")
