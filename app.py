import streamlit as st
import engine

engine.init_db()
st.set_page_config(layout="wide")
st.title("Scribe Géomantique")

mode = st.sidebar.radio("Mode de saisie :", ["Saisie manuelle", "Collage rapide"])
tirage_saisi = {}

if mode == "Collage rapide":
    texte = st.text_area("Collez les 16 noms (ex: Laetitia, Tristitia...)")
    if texte:
        figures = [f.strip() for f in texte.replace('\n', ',').split(',')]
        for i in range(16):
            if i < len(figures): tirage_saisi[f"M{i+1}"] = figures[i]
else:
    cols = st.columns(4)
    for i in range(16):
        with cols[i % 4]:
            tirage_saisi[f"M{i+1}"] = st.selectbox(f"M{i+1}", list(engine.noms_bambara.keys()), key=f"M{i+1}")

if st.button("Analyser le thème"):
    st.write("---")
    # Affichage des axes
    for axe, points in engine.obtenir_analyse_par_axes(tirage_saisi).items():
        with st.expander(axe, expanded=True):
            for p in points: st.write(p)
    # Affichage des enchaînements
    for note in engine.analyser_axes_specifiques(tirage_saisi):
        st.info(note)

nom = st.text_input("Nom du consultant")
if st.button("Sauvegarder"):
    engine.sauvegarder_tirage(nom, tirage_saisi)
    st.success("Tirage enregistré.")
