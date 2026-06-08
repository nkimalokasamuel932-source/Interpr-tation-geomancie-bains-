import streamlit as st
import datetime

# 1. CONFIGURATION
st.set_page_config(page_title="Théurgie Somadjely", layout="wide")

# 2. BASE DE DONNÉES
FIGURES_DATA = {
    "1121": {"nom": "Youssouf", "psaume": "Psaume 35", "verset": "Exode 15:3", "huile": "Laurier noble", "plante": "Feuilles de Laurier", "jour": "Mardi", "planete": "Mars"},
    "1222": {"nom": "Adama", "psaume": "Psaume 4", "verset": "Néhémie 8:10", "huile": "Citron", "plante": "Zeste de Citron", "jour": "Jeudi", "planete": "Jupiter"},
    "2111": {"nom": "Madiou", "psaume": "Psaume 128", "verset": "Exode 20:12", "huile": "Romarin", "plante": "Romarin séché", "jour": "Jeudi", "planete": "Jupiter"},
    "2212": {"nom": "Idrissa", "psaume": "Psaume 119", "verset": "Ésaïe 1:18", "huile": "Menthe", "plante": "Menthe blanche", "jour": "Vendredi", "planete": "Mercure"},
    "1111": {"nom": "Ibrahima", "psaume": "Psaume 120", "verset": "Psaume 121:8", "huile": "Cèdre", "plante": "Hysope", "jour": "Lundi", "planete": "Lune"},
    "1212": {"nom": "Issa", "psaume": "Psaume 102", "verset": "Joël 2:25", "huile": "Encens", "plante": "Sel bénit", "jour": "Mercredi", "planete": "Vénus"},
    "2122": {"nom": "Oumarou", "psaume": "Psaume 29", "verset": "Cantique 8:6", "huile": "Gingembre", "plante": "Racine de gingembre", "jour": "Mardi", "planete": "Mars"},
    "2221": {"nom": "Ayouba", "psaume": "Psaume 40", "verset": "Ésaïe 61:3", "huile": "Verveine", "plante": "Verveine", "jour": "Samedi", "planete": "Saturne"},
    "1122": {"nom": "Abubakar", "psaume": "Psaume 121", "verset": "Psaume 46:2", "huile": "Rose", "plante": "Pétales de rose", "jour": "Dimanche", "planete": "Soleil"},
    "1221": {"nom": "Massasouleymane", "psaume": "Psaume 142", "verset": "Ésaïe 22:22", "huile": "Girofle", "plante": "Clous de girofle", "jour": "Samedi", "planete": "Saturne"},
    "2112": {"nom": "Badra", "psaume": "Psaume 133", "verset": "Ruth 1:16", "huile": "Curcuma", "plante": "Poudre de curcuma", "jour": "Mercredi", "planete": "Mercure"},
    "2211": {"nom": "Nouhou", "psaume": "Psaume 59", "verset": "Psaume 68:2", "huile": "Basilic", "plante": "Feuilles de basilic", "jour": "Dimanche", "planete": "Soleil"},
    "2222": {"nom": "Moussa", "psaume": "Psaume 47", "verset": "Genèse 22:17", "huile": "Thym", "plante": "Thym commun", "jour": "Lundi", "planete": "Lune"},
    "2121": {"nom": "Ousmane", "psaume": "Psaume 23", "verset": "Psaume 23:1", "huile": "Cannelle", "plante": "Bâtons de cannelle", "jour": "Jeudi", "planete": "Jupiter"},
    "1112": {"nom": "Allahou", "psaume": "Psaume 59", "verset": "Proverbes 26:27", "huile": "Sauge", "plante": "Sauge officinale", "jour": "Dimanche", "planete": "Soleil"},
    "1211": {"nom": "Fortuna Minor", "psaume": "Psaume 1", "verset": "Proverbes 10:22", "huile": "Anis", "plante": "Anis étoilé", "jour": "Vendredi", "planete": "Mercure"}
}

# 3. CALCULS
def addition(f1, f2):
    return "".join(["2" if (int(f1[i]) + int(f2[i])) % 2 == 0 else "1" for i in range(4)])

def calcul_theme(mères):
    # Validation : chaque mère doit avoir 4 chiffres
    for m in mères:
        if len(m) != 4: return None
    
    m = [None] + mères
    # Filles
    m.append(m[1][0]+m[2][0]+m[3][0]+m[4][0])
    m.append(m[1][1]+m[2][1]+m[3][1]+m[4][1])
    m.append(m[1][2]+m[2][2]+m[3][2]+m[4][2])
    m.append(m[1][3]+m[2][3]+m[3][3]+m[4][3])
    # Neveux
    m.append(addition(m[1], m[2])); m.append(addition(m[3], m[4]))
    m.append(addition(m[5], m[6])); m.append(addition(m[7], m[8]))
    # Témoins et Juge
    m.append(addition(m[9], m[10])); m.append(addition(m[11], m[12]))
    m.append(addition(m[13], m[14])); m.append(addition(m[1], m[15]))
    return m

def get_heure_planetaire():
    cycle = ["Saturne", "Jupiter", "Mars", "Soleil", "Vénus", "Mercure", "Lune"]
    jour_depart = {"Monday": 6, "Tuesday": 2, "Wednesday": 5, "Thursday": 1, "Friday": 4, "Saturday": 0, "Sunday": 3}
    now = datetime.datetime.now()
    return cycle[(jour_depart[now.strftime("%A")] + now.hour) % 7]

# 4. INTERFACE
st.title("📿 Système Théurgique Somadjely")
mères = [st.sidebar.text_input(f"Mère {i}", "1121") for i in range(1, 5)]
maison = st.sidebar.number_input("Maison à traiter", 1, 16, 2)

if st.button("Lancer le Diagnostic"):
    theme = calcul_theme(mères)
    if not theme:
        st.error("Erreur : chaque mère doit contenir exactement 4 chiffres (1 ou 2).")
    else:
        data = FIGURES_DATA.get(theme[maison], FIGURES_DATA["1121"])
        heure_actuelle = get_heure_planetaire()
        
        st.success(f"Figure Maison {maison} : {data['nom']}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"🌿 **Plante :** {data['plante']}")
            st.write(f"💧 **Huile :** {data['huile']}")
            st.write(f"📅 **Jour :** {data['jour']}")
        with col2:
            st.write(f"📖 **Psaume :** {data['psaume']}")
            st.write(f"📜 **Verset :** {data['verset']}")
            st.write(f"🪐 **Planète :** {data['planete']}")
        
        if heure_actuelle == data['planete']:
            st.balloons()
            st.success(f"Moment idéal ! Nous sommes en heure de {heure_actuelle}.")
        else:
            st.warning(f"Heure actuelle : {heure_actuelle}. Attendez l'heure de {data['planete']}.")

        st.markdown("### Protocole de préparation du Nassi")
        st.write(f"1. Face au Nord, infuser la {data['plante']} pendant 10 min.")
        st.write(f"2. Ajouter 3 gouttes d'huile de {data['huile']}.")
        st.write(f"3. Réciter le {data['psaume']} 7 fois en se lavant.")
