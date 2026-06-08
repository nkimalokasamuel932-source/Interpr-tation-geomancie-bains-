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
import streamlit as st

# 1. BASE DE DONNÉES THÉURGIQUE ÉTENDUE
FIGURES_DATA = {
    "1121": {"nom": "Youssouf", "psaume": "Psaume 35", "verset": "Exode 15:3", "huile": "Laurier noble", "plante": "Feuilles de Laurier"},
    "1222": {"nom": "Adama", "psaume": "Psaume 4", "verset": "Néhémie 8:10", "huile": "Citron", "plante": "Zeste de Citron"},
    "2111": {"nom": "Madiou", "psaume": "Psaume 128", "verset": "Exode 20:12", "huile": "Romarin", "plante": "Romarin séché"},
    "2212": {"nom": "Idrissa", "psaume": "Psaume 119", "verset": "Ésaïe 1:18", "huile": "Menthe", "plante": "Menthe blanche"},
    "1111": {"nom": "Ibrahima", "psaume": "Psaume 120", "verset": "Psaume 121:8", "huile": "Cèdre", "plante": "Hysope"},
    "1212": {"nom": "Issa", "psaume": "Psaume 102", "verset": "Joël 2:25", "huile": "Encens", "plante": "Sel bénit"},
    "2122": {"nom": "Oumarou", "psaume": "Psaume 29", "verset": "Cantique 8:6", "huile": "Gingembre", "plante": "Racine de gingembre"},
    "2221": {"nom": "Ayouba", "psaume": "Psaume 40", "verset": "Ésaïe 61:3", "huile": "Verveine", "plante": "Verveine"},
    "1122": {"nom": "Abubakar", "psaume": "Psaume 121", "verset": "Psaume 46:2", "huile": "Rose", "plante": "Pétales de rose"},
    "1221": {"nom": "Massasouleymane", "psaume": "Psaume 142", "verset": "Ésaïe 22:22", "huile": "Girofle", "plante": "Clous de girofle"},
    "2112": {"nom": "Badra", "psaume": "Psaume 133", "verset": "Ruth 1:16", "huile": "Curcuma", "plante": "Poudre de curcuma"},
    "2211": {"nom": "Nouhou", "psaume": "Psaume 59", "verset": "Psaume 68:2", "huile": "Basilic", "plante": "Feuilles de basilic"},
    "2222": {"nom": "Moussa", "psaume": "Psaume 47", "verset": "Genèse 22:17", "huile": "Thym", "plante": "Thym commun"},
    "2121": {"nom": "Ousmane", "psaume": "Psaume 23", "verset": "Psaume 23:1", "huile": "Cannelle", "plante": "Bâtons de cannelle"},
    "1112": {"nom": "Allahou", "psaume": "Psaume 59", "verset": "Proverbes 26:27", "huile": "Sauge", "plante": "Sauge officinale"},
    "1211": {"nom": "Fortuna Minor", "psaume": "Psaume 1", "verset": "Proverbes 10:22", "huile": "Anis", "plante": "Anis étoilé"}
}

# 2. LOGIQUE DE CALCUL
def addition(f1, f2):
    return "".join(["2" if (int(f1[i]) + int(f2[i])) % 2 == 0 else "1" for i in range(4)])
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

def calcul_theme(mères):
    m = [None] + mères
    # Génération complète (16 maisons)
    m.extend([m[1][0]+m[2][0]+m[3][0]+m[4][0], m[1][1]+m[2][1]+m[3][1]+m[4][1], m[1][2]+m[2][2]+m[3][2]+m[4][2], m[1][3]+m[2][3]+m[3][3]+m[4][3]])
    m.extend([addition(m[1], m[2]), addition(m[3], m[4]), addition(m[5], m[6]), addition(m[7], m[8])])
    m.extend([addition(m[9], m[10]), addition(m[11], m[12]), addition(m[13], m[14]), addition(m[1], m[15])])
    return m

# 3. INTERFACE
st.title("📿 Théurgie Somadjely : Protocole NASSI")
mères = [st.sidebar.text_input(f"Mère {i}", "1121") for i in range(1, 5)]
maison_choisie = st.sidebar.number_input("Quelle maison traiter (1-16) ?", 1, 16, 2)

if st.button("Générer le Protocole de Soin"):
    theme = calcul_theme(mères)
    code = theme[maison_choisie]
    data = FIGURES_DATA.get(code, {"nom": "Inconnue", "psaume": "N/A", "verset": "N/A", "huile": "N/A", "plante": "N/A"})

    st.success(f"Protocole pour la Maison {maison_choisie} : {data['nom']}")
    
    tab1, tab2 = st.tabs(["Ingrédients Sacrés", "Protocole d'Application"])
    
    with tab1:
        st.write(f"🌿 **Plante de base** : {data['plante']}")
        st.write(f"💧 **Huile Essentielle** : {data['huile']}")
        st.write(f"📖 **Psaume de Puissance** : {data['psaume']}")
        st.write(f"📜 **Verset** : *{data['verset']}*")
        
    with tab2:
        st.markdown(f"""
        1. **Préparation** : Placez-vous face au NORD.
        2. **Infusion** : Faites bouillir la plante pendant 10 minutes. 
        3. **Signature** : Dessinez la figure **{code}** sur une feuille, écrivez le verset autour.
        4. **Nassi** : Dissolvez l'encre dans l'eau infusée après avoir ajouté 3 gouttes de l'huile de **{data['huile']}**.
        5. **Rituel** : Lavez-vous avec cette eau tiède, récitez le {data['psaume']} sept fois.
        """)
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
