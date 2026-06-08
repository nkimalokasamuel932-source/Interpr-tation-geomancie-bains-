import streamlit as st

# 1. DICTIONNAIRE THÉURGIQUE (Psaumes, Versets, Huiles)
FIGURES = {
    "1121": {"nom": "Youssouf", "psaume": "Psaume 35", "verset": "Exode 15:3", "huile": "Laurier noble"},
    "1222": {"nom": "Adama", "psaume": "Psaume 4", "verset": "Néhémie 8:10", "huile": "Citron"},
    "2111": {"nom": "Madiou", "psaume": "Psaume 128", "verset": "Exode 20:12", "huile": "Romarin"},
    "2212": {"nom": "Idrissa", "psaume": "Psaume 119", "verset": "Ésaïe 1:18", "huile": "Menthe"},
    "1111": {"nom": "Ibrahima", "psaume": "Psaume 120", "verset": "Psaume 121:8", "huile": "Hysope"},
    "1212": {"nom": "Issa", "psaume": "Psaume 102", "verset": "Joël 2:25", "huile": "Sel bénit/Cèdre"},
    "2122": {"nom": "Oumarou", "psaume": "Psaume 29", "verset": "Cantique 8:6", "huile": "Gingembre"},
    "2221": {"nom": "Ayouba", "psaume": "Psaume 40", "verset": "Ésaïe 61:3", "huile": "Verveine"},
    "1122": {"nom": "Abubakar", "psaume": "Psaume 121", "verset": "Psaume 46:2", "huile": "Rose"},
    "1221": {"nom": "Massasouleymane", "psaume": "Psaume 142", "verset": "Ésaïe 22:22", "huile": "Girofle"},
    "2112": {"nom": "Badra", "psaume": "Psaume 133", "verset": "Ruth 1:16", "huile": "Curcuma"},
    "2211": {"nom": "Nouhou", "psaume": "Psaume 59", "verset": "Psaume 68:2", "huile": "Basilic"},
    "2222": {"nom": "Moussa", "psaume": "Psaume 47", "verset": "Genèse 22:17", "huile": "Thym"},
    "2121": {"nom": "Ousmane", "psaume": "Psaume 23", "verset": "Psaume 23:1", "huile": "Cannelle"},
    "1112": {"nom": "Allahou", "psaume": "Psaume 59", "verset": "Proverbes 26:27", "huile": "Sauge"},
    "1211": {"nom": "Fortuna Minor", "psaume": "Psaume 1", "verset": "Proverbes 10:22", "huile": "Anis étoilé"}
}

def addition(f1, f2):
    return "".join(["2" if (int(f1[i]) + int(f2[i])) % 2 == 0 else "1" for i in range(4)])

def calcul_theme(mères):
    m = [None] + mères
    m.append(m[1][0]+m[2][0]+m[3][0]+m[4][0]); m.append(m[1][1]+m[2][1]+m[3][1]+m[4][1])
    m.append(m[1][2]+m[2][2]+m[3][2]+m[4][2]); m.append(m[1][3]+m[2][3]+m[3][3]+m[4][3])
    m.append(addition(m[1], m[2])); m.append(addition(m[3], m[4]))
    m.append(addition(m[5], m[6])); m.append(addition(m[7], m[8]))
    m.append(addition(m[9], m[10])); m.append(addition(m[11], m[12]))
    m.append(addition(m[13], m[14])); m.append(addition(m[1], m[15]))
    return m

# INTERFACE
st.title("📿 Théurgie & Géomancie Somadjely")

with st.expander("Configurer les 4 Mères"):
    mères = [st.text_input(f"Mère {i}", "1121") for i in range(1, 5)]

if st.button("Lancer le diagnostic"):
    theme = calcul_theme(mères)
    
    st.subheader("Protocole de Traitement (Maison 2)")
    fig_m2 = FIGURES.get(theme[2])
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Figure Maison 2** : {fig_m2['nom']}")
        st.write(f"**Huile Essentielle** : {fig_m2['huile']}")
    with col2:
        st.write(f"**Psaume conseillé** : {fig_m2['psaume']}")
        st.write(f"**Verset clé** : {fig_m2['verset']}")
    
    st.divider()
    st.subheader("Thème Complet")
    cols = st.columns(4)
    for i in range(1, 17):
        cols[(i-1)%4].write(f"**M{i}**: {theme[i]}")
