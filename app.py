import streamlit as st
from engine import OracleRamrouComplet

oracle = OracleRamrouComplet()
st.title("🔮 Oracle de Koutala - Consultation")

# Saisie des 16 figures
theme = {f'M{i}': st.selectbox(f"Maison {i}", list(oracle.db.keys()), key=f"M{i}") for i in range(1, 17)}
sujet = st.text_input("Posez votre question :")

if st.button("Obtenir le verdict détaillé"):
    # Calcul des témoins et résultat
    t1 = oracle.copuler(theme['M1'], theme['M2'])
    t2 = oracle.copuler(theme['M15'], theme['M16'])
    res = oracle.copuler(t1, t2)
    
    details = oracle.get_details(res)
    full_text = f"VERDICT : {res}\n\n{details}"
    
    st.subheader(f"Verdict Final : {res}")
    st.markdown(details)
    
    # Bouton de téléchargement
    st.download_button(
        label="📥 Télécharger ce protocole",
        data=full_text,
        file_name="protocole_oracle.txt",
        mime="text/plain"
    )
