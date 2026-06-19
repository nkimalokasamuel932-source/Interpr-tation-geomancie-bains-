import streamlit as st
from engine import OracleRamrouComplet

oracle = OracleRamrouComplet()
st.title("🔮 Oracle de geomancie - Consultation")

# Saisie des 16 figures
theme = {f'M{i}': st.selectbox(f"Maison {i}", list(oracle.db.keys())) for i in range(1, 17)}
sujet = st.text_input("Posez votre question :")

if st.button("Obtenir le verdict détaillé"):
    # Calcul des témoins (Passations)
    t1 = oracle.copuler(theme['M1'], theme['M2'])
    t2 = oracle.copuler(theme['M15'], theme['M16'])
    
    st.write("---")
    st.subheader("Analyse des Passations")
    st.write(f"Témoin 1 (Début) : **{t1}** | Témoin 2 (Fin) : **{t2}**")
    
    # Verdict selon sujet
    res = oracle.copuler(t1, t2)
    st.subheader(f"Verdict Final : {res}")
    st.markdown(oracle.get_details(res))
