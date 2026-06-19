import streamlit as st
from engine import OracleRamrouComplet

oracle = OracleRamrouComplet()
st.title("Oracle géomancie")

theme = {}
for i in range(1, 17):
    theme[f'M{i}'] = st.selectbox(f"Figure M{i}", list(oracle.db.keys()))

question = st.selectbox("Sujet de consultation", ["mariage", "delai", "vol"])

if st.button("Obtenir le verdict"):
    resultat = oracle.generer_verdict(question, theme)
    st.success(resultat)
