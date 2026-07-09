# app.py
import streamlit as st
import engine

st.title("Scribe Géomantique : Analyse")

st.markdown("Saisissez la figure présente dans chaque maison pour obtenir l'analyse.")

# Création du formulaire de saisie
with st.form("geomancie_form"):
    cols = st.columns(4)
    tirage_saisi = {}
    
    # Génération des champs de saisie
    for i in range(1, 17):
        maison_id = f"M{i}"
        with cols[(i-1) % 4]:
            tirage_saisi[maison_id] = st.text_input(f"{maison_id}", key=maison_id)
            
    soumettre = st.form_submit_button("Analyser le thème")

if soumettre:
    st.subheader("Résultats de l'interprétation")
    analyse = engine.obtenir_analyse(tirage_saisi)
    for texte in analyse.values():
        st.write(texte)
