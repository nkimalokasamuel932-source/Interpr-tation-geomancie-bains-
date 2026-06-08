import streamlit as st
import datetime

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Théurgie Somadjely", layout="wide")

# 2. BASE DE DONNÉES COMPLÈTE (16 FIGURES)
FIGURES_DATA = {
    "1111": {"nom": "Via", "psaume": "Psaume 51", "verset": "Ps 51:7", "huile": "Cèdre", "plante": "Hysope", "planete": "Lune", "jour": "Lundi", "signification": "Chemin de vie, fluidité, changement nécessaire."},
    "1112": {"nom": "Cauda", "psaume": "Psaume 59", "verset": "Pr 26:27", "huile": "Sauge", "plante": "Sauge", "planete": "Soleil", "jour": "Dimanche", "signification": "Fin d'un cycle, besoin de protection."},
    "1121": {"nom": "Puer", "psaume": "Psaume 35", "verset": "Ex 15:3", "huile": "Laurier", "plante": "Laurier", "planete": "Mars", "jour": "Mardi", "signification": "Énergie nouvelle, courage, action offensive."},
    "1122": {"nom": "Puella", "psaume": "Psaume 121", "verset": "Ps 46:2", "huile": "Rose", "plante": "Pétales de Rose", "planete": "Vénus", "jour": "Vendredi", "signification": "Harmonie, beauté, attraction de la grâce."},
    "1211": {"nom": "Fortuna Minor", "psaume": "Psaume 1", "verset": "Pr 10:22", "huile": "Anis", "plante": "Anis étoilé", "planete": "Mercure", "jour": "Vendredi", "signification": "Petite chance rapide, saisissez les opportunités."},
    "1212": {"nom": "Amissio", "psaume": "Psaume 102", "verset": "Jl 2:25", "huile": "Encens", "plante": "Sel bénit", "planete": "Vénus", "jour": "Mercredi", "signification": "Perte ou lâcher-prise pour un renouveau."},
    "1221": {"nom": "Carcer", "psaume": "Psaume 142", "verset": "Es 22:22", "huile": "Girofle", "plante": "Clous de Girofle", "planete": "Saturne", "jour": "Samedi", "signification": "Blocage, patience et persévérance spirituelle."},
    "1222": {"nom": "Laetitia", "psaume": "Psaume 4", "verset": "Né 8:10", "huile": "Citron", "plante": "Zeste de Citron", "planete": "Jupiter", "jour": "Jeudi", "signification": "Joie intérieure, réussite, expansion."},
    "2111": {"nom": "Caput", "psaume": "Psaume 128", "verset": "Ex 20:12", "huile": "Romarin", "plante": "Romarin", "planete": "Jupiter", "jour": "Jeudi", "signification": "Début de réussite, sagesse, direction claire."},
    "2112": {"nom": "Conjunctio", "psaume": "Psaume 133", "verset": "Rt 1:16", "huile": "Curcuma", "plante": "Curcuma", "planete": "Mercure", "jour": "Mercredi", "signification": "Union, association, rassemblement des énergies."},
    "2121": {"nom": "Acquisitio", "psaume": "Psaume 23", "verset": "Ps 23:1", "huile": "Cannelle", "plante": "Bâtons de cannelle", "planete": "Jupiter", "jour": "Jeudi", "signification": "Gain, succès matériel et bénédictions."},
    "2122": {"nom": "Rubeus", "psaume": "Psaume 29", "verset": "Ct 8:6", "huile": "Gingembre", "plante": "Gingembre", "planete": "Mars", "jour": "Mardi", "signification": "Passion intense, feu intérieur, tempérance nécessaire."},
    "2211": {"nom": "Fortuna Major", "psaume": "Psaume 20", "verset": "Ps 20:7", "huile": "Basilic", "plante": "Feuilles de Basilic", "planete": "Soleil", "jour": "Dimanche", "signification": "Grande chance, autorité, bénédiction divine stable."},
    "2212": {"nom": "Albus", "psaume": "Psaume 119", "verset": "Es 1:18", "huile": "Menthe", "plante": "Menthe", "planete": "Mercure", "jour": "Lundi", "signification": "Pureté de pensée, vérité, clarté mentale."},
    "2221": {"nom": "Tristitia", "psaume": "Psaume 130", "verset": "Es 61:3", "huile": "Verveine", "plante": "Verveine", "planete": "Saturne", "jour": "Samedi", "signification": "Épreuve, tristesse passagère, transformation."},
    "2222": {"nom": "Populus", "psaume": "Psaume 3", "verset": "Gn 22:17", "huile": "Thym", "plante": "Thym", "planete": "Lune", "jour": "Lundi", "signification": "Rassemblement, influence collective, stabilité."}
}

# 3. LOGIQUE GÉOMANTIQUE
def addition(f1, f2):
    return "".join(["2" if (int(f1[i]) + int(f2[i])) % 2 == 0 else "1" for i in range(4)])

def calcul_theme(mères):
    m = [None] + mères
    # Filles
    m.append(m[1][0]+m[2][0]+m[3][0]+m[4][0]); m.append(m[1][1]+m[2][1]+m[3][1]+m[4][1])
    m.append(m[1][2]+m[2][2]+m[3][2]+m[4][2]); m.append(m[1][3]+m[2][3]+m[3][3]+m[4][3])
    # Neveux
    m.append(addition(m[1], m[2])); m.append(addition(m[3], m[4]))
    m.append(addition(m[5], m[6])); m.append(addition(m[7], m[8]))
    # Témoins et Juge
    m.append(addition(m[9], m[10])); m.append(addition(m[11], m[12]))
    m.append(addition(m[13], m[14])); m.append(addition(m[1], m[15]))
    return m

def get_heure_planetaire():
    cycle = ["Saturne", "Jupiter", "Mars", "Soleil", "Vénus", "Mercure", "Lune"]
    d = {"Monday": 6, "Tuesday": 2, "Wednesday": 5, "Thursday": 1, "Friday": 4, "Saturday": 0, "Sunday": 3}
    return cycle[(d[datetime.datetime.now().strftime("%A")] + datetime.datetime.now().hour) % 7]

# 4. INTERFACE
st.title("📿 Système Théurgique Somadjely")
with st.sidebar:
    st.header("Saisie des 4 Mères")
    mères = [st.text_input(f"Mère {i}", "1121") for i in range(1, 5)]
    maison_cle = st.number_input("Maison à traiter (1-16)", 1, 16, 2)

if st.button("Lancer le protocole de soin"):
    theme = calcul_theme(mères)
    fig_code = theme[maison_cle]
    data = FIGURES_DATA.get(fig_code)
    heure_actuelle = get_heure_planetaire()
    
    st.success(f"La figure en Maison {maison_cle} est : **{data['nom']}** ({fig_code})")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"🌿 **Plante :** {data['plante']}")
        st.write(f"💧 **Huile :** {data['huile']}")
    with col2:
        st.write(f"📖 **Psaume :** {data['psaume']}")
        st.write(f"📜 **Verset clé :** {data['verset']}")
    
    st.info(f"💡 **Signification spirituelle :** {data['signification']}")

    st.markdown("### 🚿 Protocole de bain (Nassi)")
    st.write(f"1. **Alignement** : Travaillez face au NORD. L'heure planétaire actuelle est celle de **{heure_actuelle}**.")
    st.write(f"2. **Préparation** : Infusez la {data['plante']} dans de l'eau purifiée pendant 10 minutes.")
    st.write(f"3. **Activation** : Ajoutez 3 gouttes d'huile de {data['huile']} et 3 pincées de sel si disponible.")
    st.write(f"4. **Rituel** : Lavez-vous avec cette eau tout en récitant le {data['psaume']} sept fois.")
    
    if heure_actuelle == data['planete']:
        st.balloons()
        st.success("Le moment est parfait pour ce rituel : nous sommes sous l'influence de la planète régente.")
    else:
        st.warning(f"Attendez l'heure de {data['planete']} pour optimiser la force vibratoire du Nassi.")
