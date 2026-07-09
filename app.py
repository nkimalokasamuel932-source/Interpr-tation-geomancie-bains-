import streamlit as st
import engine

engine.init_db()
st.title("Scribe Géomantique")

# Exemple de saisie simplifiée (adaptez selon vos besoins)
nom = st.text_input("Nom du consultant")
# (Ici votre interface de saisie des 16 maisons)
# ...

if st.button("Analyser"):
    # Supposez que tirage_saisi soit votre dictionnaire
    st.write("---")
    st.subheader("Synthèse de l'Interprète")
    for note in engine.analyser_axes_specifiques(tirage_saisi):
        st.info(note)
    
    if st.button("Sauvegarder"):
        engine.sauvegarder_tirage(nom, tirage_saisi)
        st.success("Sauvegardé !")
