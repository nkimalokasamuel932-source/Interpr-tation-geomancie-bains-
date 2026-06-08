import streamlit as st

# 1. DICTIONNAIRE DES FIGURES
FIGURES = {
    "1121": "Youssouf", "1222": "Adama", "2111": "Madiou", "2212": "Idrissa",
    "1111": "Ibrahima", "1212": "Issa", "2122": "Oumarou", "2221": "Ayouba",
    "1122": "Abubakar", "1221": "Massasouleymane", "2112": "Badra", "2211": "Nouhou",
    "2222": "Moussa", "2121": "Ousmane", "1112": "Allahou", "1211": "Fortuna Minor"
}

# 2. LOGIQUE DE CALCUL
def addition_geomantique(f1, f2):
    return "".join(["2" if (int(f1[i]) + int(f2[i])) % 2 == 0 else "1" for i in range(4)])

def generer_theme(m1, m2, m3, m4):
    m = [None, m1, m2, m3, m4]
    m.append(m1[0]+m2[0]+m3[0]+m4[0]); m.append(m1[1]+m2[1]+m3[1]+m4[1])
    m.append(m1[2]+m2[2]+m3[2]+m4[2]); m.append(m1[3]+m2[3]+m3[3]+m4[3])
    m.append(addition_geomantique(m[1], m[2])); m.append(addition_geomantique(m[3], m[4]))
    m.append(addition_geomantique(m[5], m[6])); m.append(addition_geomantique(m[7], m[8]))
    m.append(addition_geomantique(m[9], m[10])); m.append(addition_geomantique(m[11], m[12]))
    m.append(addition_geomantique(m[13], m[14])); m.append(addition_geomantique(m[1], m[15]))
    return m

# 3. INTERFACE STREAMLIT
st.title("📿 Calculateur Géomantique")

st.sidebar.header("Entrez les 4 Mères")
m1 = st.sidebar.text_input("Mère 1", "1121")
m2 = st.sidebar.text_input("Mère 2", "1222")
m3 = st.sidebar.text_input("Mère 3", "2111")
m4 = st.sidebar.text_input("Mère 4", "2212")

if st.button("Calculer le Thème"):
    resultats = generer_theme(m1, m2, m3, m4)
    
    st.success("Calcul effectué avec succès !")
    
    # Affichage en 4 colonnes
    cols = st.columns(4)
    for i in range(1, 17):
        code = resultats[i]
        nom = FIGURES.get(code, "Inconnue")
        cols[(i-1)%4].write(f"**M{i}**: {code} ({nom})")

    st.divider()
    st.write("### Protocole Maison 2")
    code_m2 = resultats[2]
    st.write(f"Figure: {FIGURES.get(code_m2)}")
