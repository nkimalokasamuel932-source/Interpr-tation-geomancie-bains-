import streamlit as st
import engine

def obtenir_analyse(tirage_figures):
    resultats = {}
    for maison, figure in tirage_figures.items():
        if figure in figures_definitions:
            resultats[maison] = f"{maisons_definitions[maison]} -> {figure} : {figures_definitions[figure]}"
        else:
            resultats[maison] = f"{maisons_definitions[maison]} : Figure non reconnue"
    return resultats
# Initialisation
engine.init_db()
st.set_page_config(layout="wide")
st.title("Scribe Géomantique : Analyse Rapide")

# 1. Mode de saisie
st.sidebar.header("Mode de saisie")
mode = st.sidebar.radio("Choisir le mode :", ["Saisie manuelle (Grille)", "Collage rapide"])

tirage_saisi = {}

if mode == "Collage rapide":
    st.info("Collez vos 16 figures séparées par des virgules ou des retours à la ligne.")
    texte_colle = st.text_area("Collez ici (ex: Laetitia, Tristitia, ...)")
    if texte_colle:
        lignes = texte_colle.replace('\n', ',').split(',')
        figures_propres = [f.strip() for f in lignes if f.strip()]
        for i in range(16):
            if i < len(figures_propres):
                tirage_saisi[f"M{i+1}"] = figures_propres[i]

else:
    # Grille automatique
    st.subheader("Saisie des 16 Maisons")
    cols = st.columns(4)
    for i in range(16):
        with cols[i % 4]:
            tirage_saisi[f"M{i+1}"] = st.selectbox(f"Maison {i+1}", list(engine.noms_bambara.keys()), key=f"M{i+1}")

# 2. Analyse
if st.button("Analyser le thème complet"):
    if len(tirage_saisi) == 16:
        st.write("---")
        
        # Affichage des axes
        st.subheader("Synthèse structurée par Axes")
        axes = engine.obtenir_analyse_par_axes(tirage_saisi)
        for axe, points in axes.items():
            with st.expander(axe, expanded=True):
                if points:
                    for p in points: st.write(p)
                else: st.write("Aucune alerte spécifique.")
        
        # Interprétation narrative
        st.write("---")
        st.subheader("Analyse des Enchaînements")
        details = engine.analyser_axes_specifiques(tirage_saisi)
        for note in details:
            st.info(note)
    else:
        st.warning("Veuillez remplir toutes les maisons.")

# 3. Sauvegarde
st.write("---")
nom = st.text_input("Nom du consultant pour la sauvegarde")
if st.button("Sauvegarder"):
    if nom:
        engine.sauvegarder_tirage(nom, tirage_saisi)
        st.success("Tirage enregistré.")
    else:
        st.error("Entrez un nom.")
