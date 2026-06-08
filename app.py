import streamlit as st
import datetime

# 1. BASE DE DONNÉES SPIRITUELLE
FIGURES_DATA = {
    "1121": {"nom": "Youssouf", "psaume": "Ps 35", "jour": "Mardi", "planete": "Mars", "huile": "Laurier noble"},
    "1222": {"nom": "Adama", "psaume": "Ps 4", "jour": "Jeudi", "planete": "Jupiter", "huile": "Citron"},
    "2111": {"nom": "Madiou", "psaume": "Ps 128", "jour": "Jeudi", "planete": "Jupiter", "huile": "Romarin"},
    "2212": {"nom": "Idrissa", "psaume": "Ps 119", "jour": "Vendredi", "planete": "Mercure", "huile": "Menthe"},
    "1111": {"nom": "Ibrahima", "psaume": "Ps 120", "jour": "Lundi", "planete": "Lune", "huile": "Cèdre"},
    "1212": {"nom": "Issa", "psaume": "Ps 102", "jour": "Mercredi", "planete": "Vénus", "huile": "Encens"},
    "2122": {"nom": "Oumarou", "psaume": "Ps 29", "jour": "Mardi", "planete": "Mars", "huile": "Gingembre"},
    "2221": {"nom": "Ayouba", "psaume": "Ps 40", "jour": "Samedi", "planete": "Saturne", "huile": "Verveine"},
    "1122": {"nom": "Abubakar", "psaume": "Ps 121", "jour": "Dimanche", "planete": "Soleil", "huile": "Rose"},
    "1221": {"nom": "Massasouleymane", "psaume": "Ps 142", "jour": "Samedi", "planete": "Saturne", "huile": "Girofle"},
    "2112": {"nom": "Badra", "psaume": "Ps 133", "jour": "Mercredi", "planete": "Mercure", "huile": "Curcuma"},
    "2211": {"nom": "Nouhou", "psaume": "Ps 59", "jour": "Dimanche", "planete": "Soleil", "huile": "Basilic"},
    "2222": {"nom": "Moussa", "psaume": "Ps 47", "jour": "Lundi", "planete": "Lune", "huile": "Thym"},
    "2121": {"nom": "Ousmane", "psaume": "Ps 23", "jour": "Jeudi", "planete": "Jupiter", "huile": "Cannelle"},
    "1112": {"nom": "Allahou", "psaume": "Ps 59", "jour": "Dimanche", "planete": "Soleil", "huile": "Sauge"},
    "1211": {"nom": "Fortuna Minor", "psaume": "Ps 1", "jour": "Vendredi", "planete": "Mercure", "huile": "Anis"}
}

# 2. LOGIQUE PLANÉTAIRE
PLANETES_CYCLE = ["Saturne", "Jupiter", "Mars", "Soleil", "Vénus", "Mercure", "Lune"]
JOURS_DEBUT = {
    "Monday": 6, "Tuesday": 2, "Wednesday": 5, "Thursday": 1, 
    "Friday": 4, "Saturday": 0, "Sunday": 3
}

def get_heure_planetaire():
    now = datetime.datetime.now()
    jour = now.strftime("%A")
    # Calcul simplifié basé sur l'ordre chaldéen
    index = (JOURS_DEBUT[jour] + now.hour) % 7
    return PLANETES_CYCLE[index]

# 3. LOGIQUE GÉOMANTIQUE
def addition(f1, f2):
    return "".join(["2" if (int(f1[i]) + int(f2[i])) % 2 == 0 else "1" for i in range(4)])

def calcul_theme(m):
    m = [None] + m
    m.extend([m[1][i]+m[2][i]+m[3][i]+m[4][i] for i in range(4)])
    m.extend([addition(m[1], m[2]), addition(m[3], m[4]), addition(m[5], m[6]), addition(m[7], m[8])])
    m.extend([addition(m[9], m[10]), addition(m[11], m[12]), addition(m[13], m[14]), addition(m[1], m[15])])
    return m

# 4. INTERFACE
st.title("📿 Théurgie Somadjely")
st.sidebar.header("Configuration")
mères = [st.sidebar.text_input(f"Mère {i}", "1121") for i in range(1, 5)]
maison = st.sidebar.number_input("Maison à traiter", 1, 16, 2)

if st.button("Générer le Protocole"):
    theme = calcul_theme(mères)
    data = FIGURES_DATA.get(theme[maison], FIGURES_DATA["1121"])
    heure_actuelle = get_heure_planetaire()
    
    st.success(f"Traitement pour {data['nom']} (Maison {maison})")
    
    c1, c2 = st.columns(2)
    c1.metric("Jour propice", data['jour'])
    c2.metric("Planète régente", data['planete'])
    
    st.write(f"💧 **Huile :** {data['huile']} | 📖 **Psaume :** {data['psaume']}")
    
    if heure_actuelle == data['planete']:
        st.balloons()
        st.success(f"Le moment est idéal ! Nous sommes en heure de {heure_actuelle}.")
    else:
        st.warning(f"Heure actuelle : {heure_actuelle}. Attendez l'heure de {data['planete']}.")
