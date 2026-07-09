st.subheader("Analyse structurée par Axes")
axes = engine.obtenir_analyse_par_axes(tirage_saisi)

for axe, points in axes.items():
    with st.expander(axe): # Cela crée des menus déroulants propres
        if points:
            for p in points:
                st.write(p)
        else:
            st.write("Pas d'alerte spécifique sur cet axe.")
