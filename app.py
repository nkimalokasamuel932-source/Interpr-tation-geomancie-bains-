import streamlit as st
import engine

# 1. Initialisation de la base de données
engine.init_db()

st.title("Scribe Géomantique : Analyse & Suivi")

# 2. Interface de saisie
st.sidebar.header("Configuration du tirage")
nom_consultant = st.text_input("Nom du consultant")

# Vous pouvez ajouter ici vos menus déroulants pour les 16 maisons
# Exemple simplifié pour la structure :
st.subheader("Entrée des Figures")
col1, col2 = st.columns(2)
with col1:
    m1 = st.selectbox("Maison 1", list(engine.noms_bambara.values()))
    m2 = st.selectbox("Maison 2", list(engine.noms_bambara.values()))
    # ... ajoutez les autres maisons ici ...

# Pour l'exemple, supposons que tirage_saisi soit un dictionnaire avec vos 16 maisons
tirage_saisi = {"M1": m1, "M2": m2} # Complétez avec toutes les maisons

# 3. Analyse
if st.button("Analyser le thème"):
    st.subheader("Synthèse structurée par Axes")
    
    # Récupération de l'analyse par axes depuis engine.py
    axes = engine.obtenir_analyse_par_axes(tirage_saisi)
    
    # Affichage avec des menus déroulants (expanders)
    for axe, points in axes.items():
        with st.expander(axe):
            if points:
                for p in points:
                    st.write(p)
            else:
                st.write("Aucune tension ou événement particulier détecté sur cet axe.")
    
    # Affichage de la synthèse spécifique (Ex: Idriss, Issa, Allassan)
    st.write("---")
    st.subheader("Interprétation détaillée")
    details = engine.analyser_axes_specifiques(tirage_saisi)
    for note in details:
        st.info(note)

# 4. Sauvegarde
if st.button("Sauvegarder ce tirage"):
    if nom_consultant:
        engine.sauvegarder_tirage(nom_consultant, tirage_saisi)
        st.success(f"Tirage enregistré pour {nom_consultant} !")
    else:
        st.warning("Veuillez entrer le nom du consultant avant de sauvegarder.")

# 5. Voir l'historique
if st.checkbox("Voir le dernier tirage en base"):
    dernier = engine.recuperer_dernier_tirage()
    if dernier:
        st.write(f"Dernier tirage : {dernier[0]} - {dernier[1]}")
