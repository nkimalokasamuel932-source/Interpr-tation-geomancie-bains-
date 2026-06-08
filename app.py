import streamlit as st
import datetime

# 1. CONFIGURATION
st.set_page_config(page_title="Théurgie Somadjely", layout="wide")

# 2. BASE DE DONNÉES DES 16 FIGURES
FIGURES_DATA = {
    "1111": {"nom": "Via", "psaume": "Ps 51", "verset": "Ps 51:7", "huile": "Cèdre", "plante": "Hysope", "jour": "Lundi", "planete": "Lune", "signification": "Chemin de vie, fluidité, changement nécessaire."},
    "1112": {"nom": "Cauda", "psaume": "Ps 59", "verset": "Pr 26:27", "huile": "Sauge", "plante": "Sauge", "jour": "Dimanche", "planete": "Soleil", "signification": "Fin d'un cycle, besoin de protection."},
    "1121": {"nom": "Puer", "psaume": "Ps 35", "verset": "Ex 15:3", "huile": "Laurier", "plante": "Laurier", "jour": "Mardi", "planete": "Mars", "signification": "Énergie nouvelle, courage, action offensive."},
    "1122": {"nom": "Puella", "psaume": "Ps 121", "verset": "Ps 46:2", "huile": "Rose", "plante": "Rose", "jour": "Vendredi", "planete": "Vénus", "signification": "Harmonie, beauté, attraction de la grâce."},
    "1211": {"nom": "Fortuna Minor", "psaume": "Ps 1", "verset": "Pr 10:22", "huile": "Anis", "plante": "Anis", "jour": "Vendredi", "planete": "Mercure", "signification": "Petite chance rapide, saisissez les opportunités."},
    "1212": {"nom": "Amissio", "psaume": "Ps 102", "verset": "Jl 2:25", "huile": "Encens", "plante": "Sel", "jour": "Mercredi", "planete": "Vénus", "signification": "Perte ou lâcher-prise pour un renouveau."},
    "1221": {"nom": "Carcer", "psaume": "Ps 142", "verset": "Es 22:22", "huile": "Girofle", "plante": "Girofle", "jour": "Samedi", "planete": "Saturne", "signification": "Blocage, patience et persévérance spirituelle."},
    "1222": {"nom": "Laetitia", "psaume": "Ps 4", "verset": "Né 8:10", "huile": "Citron", "plante": "Citron", "jour": "Jeudi", "planete": "Jupiter", "signification": "Joie intérieure, réussite, expansion."},
    "2111": {"nom": "Caput", "psaume": "Ps 128", "verset": "Ex 20:12", "huile": "Romarin", "plante": "Romarin", "jour": "Jeudi", "planete": "Jupiter", "signification": "Début de réussite, sagesse, direction claire."},
    "2112": {"nom": "Conjunctio", "psaume": "Ps 133", "verset": "Rt 1:16", "huile": "Curcuma", "plante": "Curcuma", "jour": "Mercredi", "planete": "Mercure", "signification": "Union, association, rassemblement des énergies."},
    "2121": {"nom": "Acquisitio", "psaume": "Ps 23", "verset": "Ps 23:1", "huile": "Cannelle", "plante": "Cannelle", "jour": "Jeudi", "planete": "Jupiter", "signification": "Gain, succès matériel et bénédictions."},
    "2122": {"nom": "Rubeus", "psaume": "Ps 29", "verset": "Ct 8:6", "huile": "Gingembre", "plante": "Gingembre", "jour": "Mardi", "planete": "Mars", "signification": "Passion intense, feu intérieur, tempérance nécessaire."},
    "2211": {"nom": "Fortuna Major", "psaume": "Ps 20", "verset": "Ps 20:7", "huile": "Basilic", "plante": "Basilic", "jour": "Dimanche", "planete": "Soleil", "signification": "Grande chance, autorité, bénédiction divine stable."},
    "2212": {"nom": "Albus", "psaume": "Ps 119", "verset": "Es 1:18", "huile": "Menthe", "plante": "Menthe", "jour": "Lundi", "planete": "Mercure", "signification": "Pureté de pensée, vérité, clarté mentale."},
    "2221": {"nom": "Tristitia", "psaume": "Ps 130", "verset": "Es 61:3", "huile": "Verveine", "plante": "Verveine", "jour": "Samedi", "planete": "Saturne", "signification": "Épreuve, tristesse passagère, transformation."},
    "2222": {"nom": "Populus", "psaume": "Ps 3", "verset": "Gn 22:17", "huile": "Thym", "plante": "Thym", "jour": "Lundi", "planete": "Lune", "signification": "Rassemblement, influence collective, stabilité."}
}

# 3. LOGIQUE CALCUL ET HEURES
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

def get_heure_planetaire():
    cycle = ["Saturne", "Jupiter", "Mars", "Soleil", "Vénus", "Mercure", "Lune"]
    d = {"Monday": 6, "Tuesday": 2, "Wednesday": 5, "Thursday": 1, "Friday": 4, "Saturday": 0, "Sunday": 3}
    return cycle[(d[datetime.datetime.now().strftime("%A")] + datetime.datetime.now().hour) % 7]

# 4. INTERFACE
st.title("📿 Système Théurgique Somadjely")
mères = [st.sidebar.text_input(f"Mère {i}", "1121") for i in range(1, 5)]
maison = st.sidebar.number_input("Maison à traiter", 1, 16, 2)

if st.button("Lancer le Diagnostic"):
    theme = calcul_theme(mères)
    data = FIGURES_DATA.get(theme[maison], FIGURES_DATA["1111"])
    heure_actuelle = get_heure_planetaire()
    
    st.subheader(f"Diagnostic Maison {maison} : {data['nom']}")
    st.info(f"**Signification** : {data['signification']}")
    
    c1, c2 = st.columns(2)
    with c1:
        st.write(f"🌿 **Plante** : {data['plante']}")
        st.write(f"💧 **Huile** : {data['huile']}")
    with c2:
        st.write(f"📖 **Psaume** : {data['psaume']} ({data['verset']})")
        st.write(f"🪐 **Planète** : {data['planete']} ({data['jour']})")
    
    if heure_actuelle == data['planete']:
        st.success(f"Moment idéal ! Nous sommes en heure de {heure_actuelle}.")
    else:
        st.warning(f"Heure actuelle : {heure_actuelle}. Attendez l'heure de {data['planete']}.")

    st.markdown("### Protocole de préparation du Nassi")
    st.write(f"Infusez la {data['plante']} 10 min, ajoutez 3 gouttes d'huile de {data['huile']}, récitez le {data['psaume']} 7 fois.")
