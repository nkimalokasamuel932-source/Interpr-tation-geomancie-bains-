import streamlit as st

# ==============================================================================
# 1. BASE DE CONNAISSANCES
# ==============================================================================
FIGURES = [
    "Djanvalimam", "Adama", "Malidjou", "Bayadou", "Tariqi", "Issa", 
    "Lomara", "Mangoussi", "Kalalaho", "Massa Souleymane", "Badra Ali", 
    "Noukoro", "Lacina", "Totiqi", "Mori Zoumana", "Moussa"
]

UNITES = {
    "Djanvalimam": 8, "Adama": 5, "Malidjou": 6, "Bayadou": 7, 
    "Tariqi": 5, "Issa": 6, "Lomara": 7, "Mangoussi": 6, 
    "Kalalaho": 6, "Massa Souleymane": 7, "Badra Ali": 7, 
    "Noukoro": 7, "Lacina": 6, "Totiqi": 6, "Mori Zoumana": 7, "Moussa": 8
}

DB_SACRIFICES = {
    "Djanvalimam": {"animaux": "Cabri coloris multiple, Chi saba sissè", "colas": "Marissa woro", "autres": "Poudre de fusil"},
    "Adama": {"animaux": "Pintade", "colas": "Yèrè woro", "autres": "Womi"},
    "Malidjou": {"animaux": "Bélier blanc, Tourou kèmè sissè", "colas": "Soho koungoro woro", "autres": "-"},
    "Bayadou": {"animaux": "Bélier blanc, Coq blanc", "colas": "Cola blanc", "autres": "Womi"},
    "Tariqi": {"animaux": "Bélier blanc, Coq blanc", "colas": "Da kamana woro", "autres": "-"},
    "Issa": {"animaux": "Kolo sissè", "colas": "Dimi woro", "autres": "Arachide, Sel"},
    "Lomara": {"animaux": "Bélier à cou rouge, Coq rouge", "colas": "Cola rouge", "autres": "-"},
    "Mangoussi": {"animaux": "Mouton noir, Cabri noir, Poulet noir", "colas": "Bi kènè woro", "autres": "7m tissu noir"},
    "Kalalaho": {"animaux": "Bélier blanc, Coq blanc adulte", "colas": "Cola blanc", "autres": "Takoula"},
    "Massa Souleymane": {"animaux": "Wara saga blanc, Coq blanc", "colas": "Kaba woro", "autres": "Œuf"},
    "Badra Ali": {"animaux": "Djara saga blanc, Coq blanc", "colas": "Gros cola blanc", "autres": "Côte d’animal, Sel"},
    "Noukoro": {"animaux": "Cabri, Bougouri sissè, Chi saba sissè", "colas": "Marissa woro", "autres": "Poudre de tabac"},
    "Lacina": {"animaux": "Brebis, Poule blanche", "colas": "Nama noro woro", "autres": "Eau, Argent (jumeaux)"},
    "Totiqi": {"animaux": "Doni ta sissè", "colas": "Qolon woro", "autres": "5 carpes fraîches"},
    "Mori Zoumana": {"animaux": "Bélier blanc, Poulet blanc", "colas": "Cola blanc", "autres": "Lait, Alcool"},
    "Moussa": {"animaux": "Bélier blanc, Poulet blanc", "colas": "Cola blanc", "autres": "Mélange céréales, 8m tissu blanc"}
}

DB_PLANTES = {
    fig: {"noms": "Consulter guide", "scientifiques": "-"} for fig in FIGURES
}
DB_PLANTES.update({
    "Djanvalimam": {"noms": "Balanzan, Diatigui Faga", "scientifiques": "Acacia albida, Ficus sp."},
    "Issa": {"noms": "Kèlètiguè yiri, Triqi", "scientifiques": "Combatum relitinum"},
    "Mangoussi": {"noms": "Tourou Bara, Koto, Gala", "scientifiques": "Cochtorpermum trictérium"}
})

# ==============================================================================
# 2. INTERFACE
# ==============================================================================
st.set_page_config(page_title="Oracle Ramrou", layout="wide")

st.title("🔮 Oracle Ramrou")
st.markdown("### Cabinet de Haute Théurgie & Science du Tourab")

with st.expander("🛡️ Charte de l'Utilisateur"):
    st.write("""
    1. **Humilité :** Le sacrifice est un levain pour la prière, non une monnaie d'échange pour forcer le destin.
    2. **Autonomie :** Utilisez ces outils pour vérifier et comprendre, pas par dépendance.
    3. **Sincérité :** La piété compte plus que l'ostentation.
    """)

# Sélection des 16 maisons
theme = {}
cols = st.columns(4)
for i in range(1, 17):
    with cols[(i-1) % 4]:
        theme[i] = st.selectbox(f"Maison {i}", FIGURES, key=f"m{i}")

if st.button("🔮 GÉNÉRER L'ORDONNANCE"):
    st.divider()
    
    # Analyse de la Case 13 et 15
    if theme.get(13) == "Massa Souleymane":
        st.warning("⚠️ **Conseil (Case 13) :** Passage obligé. Gardez votre calme et ne soyez pas pressé.")
    if theme.get(16) == "Moussa" and theme.get(15) == "Mori Zoumana":
        st.error("⚠️ **Conseil (Case 15) :** Blocage en tout. Soyez patient et pardonnez.")

    # Verdict
    juge = theme[16]
    st.subheader(f"⚖️ Verdict pour {juge}")
    
    c1, c2 = st.columns(2)
    with c1:
        st.write(f"**Temps de l'affaire :** {UNITES.get(juge, 0)} unités")
        st.success(f"**Sacrifice :** {DB_SACRIFICES.get(juge, {}).get('animaux')}")
    with c2:
        st.info(f"**Plantes associées :** {DB_PLANTES.get(juge, {}).get('noms')}")
        st.write("👉 *Usage : Infusion pour lavage 7 jours.*")

    # Méfaits
    if theme.get(6) != "Moussa" or theme.get(12) != "Moussa":
        st.divider()
        st.subheader("🔍 Analyse des méfaits")
        st.write(f"Vérifiez l'élément {theme[6]} (M6) et {theme[12]} (M12) pour tout signe de malversation.")
