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
        import streamlit as st
import datetime
import math

# 

# 1. DONNÉES PLANÉTAIRES
PLANETES = ["Saturne", "Jupiter", "Mars", "Soleil", "Vénus", "Mercure", "Lune"]
PLANETES_PAR_JOUR = {
    "Monday": ["Lune", "Saturne", "Jupiter", "Mars", "Soleil", "Vénus", "Mercure"],
    "Tuesday": ["Mars", "Soleil", "Vénus", "Mercure", "Lune", "Saturne", "Jupiter"],
    "Wednesday": ["Mercure", "Lune", "Saturne", "Jupiter", "Mars", "Soleil", "Vénus"],
    "Thursday": ["Jupiter", "Mars", "Soleil", "Vénus", "Mercure", "Lune", "Saturne"],
    "Friday": ["Vénus", "Mercure", "Lune", "Saturne", "Jupiter", "Mars", "Soleil"],
    "Saturday": ["Saturne", "Jupiter", "Mars", "Soleil", "Vénus", "Mercure", "Lune"],
    "Sunday": ["Soleil", "Vénus", "Mercure", "Lune", "Saturne", "Jupiter", "Mars"]
}

def get_heure_planetaire():
    now = datetime.datetime.now()
    # Approximation : lever du soleil à 06h, coucher à 18h (ajustable)
    jour_semaine = now.strftime("%A")
    heure_actuelle = now.hour
    
    # Simple calcul de cycle (0h-24h)
    index = heure_actuelle % 7
    return PLANETES_PAR_JOUR[jour_semaine][index]

# 2. INTÉGRATION DANS LE PROTOCOLE
st.title("📿 Calculateur de Théurgie Somadjely")

# Affichage de l'heure actuelle
planete_actuelle = get_heure_planetaire()
st.sidebar.markdown(f"---")
st.sidebar.write(f"🪐 **Heure Planétaire actuelle** : `{planete_actuelle}`")

if st.button("Calculer le Protocole de Soin"):
    # ... (logique de calcul du thème identique) ...
    
    st.info(f"""
    **Conseil de Maître :**
    Votre figure est régie par **{data['planete']}**. 
    Pour une efficacité maximale, préparez votre Nassi à une heure régie par cette planète.
    
    *Heure actuelle :* **{planete_actuelle}**
    *Si vous êtes en heure {data['planete']}, vous pouvez commencer immédiatement.*
    """)
    import streamlit as st

# 1. BASE DE DONNÉES COMPLÈTE (Heures et Jours)
FIGURES_DATA = {
    "1121": {"nom": "Youssouf", "psaume": "Psaume 35", "jour": "Mardi", "planete": "Mars", "huile": "Laurier noble"},
    "1222": {"nom": "Adama", "psaume": "Psaume 4", "jour": "Jeudi", "planete": "Jupiter", "huile": "Citron"},
    "2111": {"nom": "Madiou", "psaume": "Psaume 128", "jour": "Jeudi", "planete": "Jupiter", "huile": "Romarin"},
    "2212": {"nom": "Idrissa", "psaume": "Psaume 119", "jour": "Vendredi", "planete": "Mercure", "huile": "Menthe"},
    "1111": {"nom": "Ibrahima", "psaume": "Psaume 120", "jour": "Lundi", "planete": "Lune", "huile": "Cèdre"},
    "1212": {"nom": "Issa", "psaume": "Psaume 102", "jour": "Mercredi", "planete": "Vénus", "huile": "Encens"},
    "2122": {"nom": "Oumarou", "psaume": "Psaume 29", "jour": "Mardi", "planete": "Mars", "huile": "Gingembre"},
    "2221": {"nom": "Ayouba", "psaume": "Psaume 40", "jour": "Samedi", "planete": "Saturne", "huile": "Verveine"},
    "1122": {"nom": "Abubakar", "psaume": "Psaume 121", "jour": "Dimanche", "planete": "Soleil", "huile": "Rose"},
    "1221": {"nom": "Massasouleymane", "psaume": "Psaume 142", "jour": "Samedi", "planete": "Saturne", "huile": "Girofle"},
    "2112": {"nom": "Badra", "psaume": "Psaume 133", "jour": "Mercredi", "planete": "Mercure", "huile": "Curcuma"},
    "2211": {"nom": "Nouhou", "psaume": "Psaume 59", "jour": "Dimanche", "planete": "Soleil", "huile": "Basilic"},
    "2222": {"nom": "Moussa", "psaume": "Psaume 47", "jour": "Lundi", "planete": "Lune", "huile": "Thym"},
    "2121": {"nom": "Ousmane", "psaume": "Psaume 23", "jour": "Jeudi", "planete": "Jupiter", "huile": "Cannelle"},
    "1112": {"nom": "Allahou", "psaume": "Psaume 59", "jour": "Dimanche", "planete": "Soleil", "huile": "Sauge"},
    "1211": {"nom": "Fortuna Minor", "psaume": "Psaume 1", "jour": "Vendredi", "planete": "Mercure", "huile": "Anis"}
}

# 2. LOGIQUE DE CALCUL (inchangée)
def addition(f1, f2):
    return "".join(["2" if (int(f1[i]) + int(f2[i])) % 2 == 0 else "1" for i in range(4)])

def calcul_theme(mères):
    m = [None] + mères
    m.extend([m[1][0]+m[2][0]+m[3][0]+m[4][0], m[1][1]+m[2][1]+m[3][1]+m[4][1], m[1][2]+m[2][2]+m[3][2]+m[4][2], m[1][3]+m[2][3]+m[3][3]+m[4][3]])
    m.extend([addition(m[1], m[2]), addition(m[3], m[4]), addition(m[5], m[6]), addition(m[7], m[8])])
    m.extend([addition(m[9], m[10]), addition(m[11], m[12]), addition(m[13], m[14]), addition(m[1], m[15])])
    return m

# 3. INTERFACE AVEC TEMPORALITÉ
st.title("📿 Protocole Temporel Somadjely")
mères = [st.sidebar.text_input(f"Mère {i}", "1121") for i in range(1, 5)]
maison_choisie = st.sidebar.number_input("Maison à traiter (1-16)", 1, 16, 2)

if st.button("Générer le Protocole"):
    theme = calcul_theme(mères)
    code = theme[maison_choisie]
    data = FIGURES_DATA.get(code)

    st.success(f"Figure : {data['nom']} (Code: {code})")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"📅 **Jour Sacré** : {data['jour']}")
        st.write(f"🪐 **Planète régente** : {data['planete']}")
    with col2:
        st.write(f"💧 **Huile clé** : {data['huile']}")
        st.write(f"📖 **Psaume** : {data['psaume']}")

    st.info(f"💡 **Conseil d'application** : Effectuez le bain de Nassi le **{data['jour']}** pendant l'heure régie par **{data['planete']}** pour une efficacité vibratoire maximale.")
