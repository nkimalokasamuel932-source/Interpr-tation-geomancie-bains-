import streamlit as st
from engine import OracleRamrouComplet

# Initialisation
oracle = OracleRamrouComplet()

st.title("🔮 Oracle ")

# Saisie des figures
theme = {}
st.write("Veuillez sélectionner les 16 figures du thème :")
cols = st.columns(4)
for i in range(1, 17):
    with cols[(i-1) % 4]:
        theme[f'M{i}'] = st.selectbox(f"M{i}", list(oracle.db.keys()), key=f"M{i}")

# Saisie du sujet
sujet_input = st.text_input("Posez votre question :")

# Bouton de résultat
if st.button("Obtenir le verdict"):
    if sujet_input:
        # Appel de la fonction avec la bonne variable
        resultat = oracle.generer_verdict_intelligent(sujet_input, theme)
        st.markdown(resultat)
    else:
        st.warning("Veuillez entrer une question.")
