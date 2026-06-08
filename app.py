import streamlit as st
import datetime

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Somadjely : Géomancie & Théurgie", layout="wide")

# 2. BASE DE DONNÉES MAGISTRALE (16 FIGURES)
FIGURES_DATA = {
    "1111": {
        "nom": "Via", "psaume": "Ps 51", "verset": "Ps 51:7", "huile": "Cèdre", "plante": "Hysope", "planete": "Lune",
        "signification": "Chemin de vie, fluidité, changement nécessaire.",
        "priere_salomonique": "Au nom d'Adonaï, que les sentiers se lissent et que l'eau vive emporte tout obstacle sur mon chemin de lumière."
    },
    "1112": {
        "nom": "Cauda Draconis", "psaume": "Ps 59", "verset": "Pr 26:27", "huile": "Sauge", "plante": "Sauge", "planete": "Soleil",
        "signification": "Fin d'un cycle, besoin de protection contre les retours.",
        "priere_salomonique": "Par Agla, je scelle la porte du passé et je commande aux ombres de se dissiper devant l'éclat du Nom Saint."
    },
    "1121": {
        "nom": "Puer", "psaume": "Ps 35", "verset": "Ex 15:3", "huile": "Laurier", "plante": "Laurier", "planete": "Mars",
        "signification": "Énergie nouvelle, courage, action offensive.",
        "priere_salomonique": "Par Elohim Gibor, que ma force soit renouvelée et que mon bras soit celui du juste combattant pour la vérité."
    },
    "1122": {
        "nom": "Puella", "psaume": "Ps 121", "verset": "Ps 46:2", "huile": "Rose", "plante": "Pétales de Rose", "planete": "Vénus",
        "signification": "Harmonie, beauté, attraction de la grâce.",
        "priere_salomonique": "Par El Shaddaï, que la douceur m'entoure et que la beauté divine se manifeste dans chaque fibre de mon être."
    },
    "1211": {
        "nom": "Fortuna Minor", "psaume": "Ps 1", "verset": "Pr 10:22", "huile": "Anis", "plante": "Anis étoilé", "planete": "Mercure",
        "signification": "Petite chance rapide, saisissez les opportunités.",
        "priere_salomonique": "Par Tétragrammaton, que les vents favorables m'apportent le succès rapide et la clarté dans mes affaires."
    },
    "1212": {
        "nom": "Amissio", "psaume": "Ps 102", "verset": "Jl 2:25", "huile": "Encens", "plante": "Sel bénit", "planete": "Vénus",
        "signification": "Lâcher-prise nécessaire pour un renouveau.",
        "priere_salomonique": "Par Emmanuel, je rends ce qui n'est plus mien pour recevoir ce qui m'est promis dans l'abondance de l'Esprit."
    },
    "1221": {
        "nom": "Carcer", "psaume": "Ps 142", "verset": "Es 22:22", "huile": "Girofle", "plante": "Clous de Girofle", "planete": "Saturne",
        "signification": "Blocage, patience et persévérance spirituelle.",
        "priere_salomonique": "Par Cassiel, que les chaînes invisibles se brisent et que ma patience se transforme en une forteresse inébranlable."
    },
    "1222": {
        "nom": "Laetitia", "psaume": "Ps 4", "verset": "Né 8:10", "huile": "Citron", "plante": "Zeste de Citron", "planete": "Jupiter",
        "signification": "Joie intérieure, réussite, expansion.",
        "priere_salomonique": "Par Zadkiel, que la joie du Seigneur soit ma force et que mon horizon s'élargisse vers des hauteurs infinies."
    },
    "2111": {
        "nom": "Caput Draconis", "psaume": "Ps 128", "verset": "Ex 20:12", "huile": "Romarin", "plante": "Romarin", "planete": "Jupiter",
        "signification": "Début de réussite, sagesse, direction claire.",
        "priere_salomonique": "Par Alpha et Oméga, je pose le premier pas vers ma victoire, guidé par la sagesse des anciens et la faveur divine."
    },
    "2112": {
        "nom": "Conjunctio", "psaume": "Ps 133", "verset": "Rt 1:16", "huile": "Curcuma", "plante": "Poudre de Curcuma", "planete": "Mercure",
        "signification": "Union, association, rassemblement des énergies.",
        "priere_salomonique": "Par Elohim Sabaoth, que l'unité soit ma force et que les alliances sacrées se nouent pour le bien de ma mission."
    },
    "2121": {
        "nom": "Acquisitio", "psaume": "Ps 23", "verset": "Ps 23:1", "huile": "Cannelle", "plante": "Bâtons de Cannelle", "planete": "Jupiter",
        "signification": "Gain, succès matériel et bénédictions.",
        "priere_salomonique": "Par Jéhovah Jireh, le Seigneur qui pourvoit, je reçois maintenant la récompense de mes travaux et l'abondance sans fin."
    },
    "2122": {
        "nom": "Rubeus", "psaume": "Ps 29", "verset": "Ct 8:6", "huile": "Gingembre", "plante": "Racine de Gingembre", "planete": "Mars",
        "signification": "Passion intense, feu intérieur, tempérance.",
        "priere_salomonique": "Par Samael, que mon feu soit purifié et qu'il brûle pour éclairer sans jamais détruire, au nom de la Paix divine."
    },
    "2211": {
        "nom": "Fortuna Major", "psaume": "Ps 20", "verset": "Ps 20:7", "huile": "Basilic", "plante": "Basilic frais", "planete": "Soleil",
        "signification": "Grande chance, autorité, bénédiction stable.",
        "priere_salomonique": "Par Michael, Prince de la Lumière, que l'éclat du succès brille sur moi et que ma victoire soit gravée dans l'éternité."
    },
    "2212": {
        "nom": "Albus", "psaume": "Ps 119", "verset": "Es 1:18", "huile": "Menthe", "plante": "Feuilles de Menthe", "planete": "Mercure",
        "signification": "Pureté de pensée, vérité, clarté mentale.",
        "priere_salomonique": "Par Raphaël, guérisseur de l'âme, que mon esprit soit blanc comme la neige et ma parole tranchante comme le diamant."
    },
    "2221": {
        "nom": "Tristitia", "psaume": "Ps 130", "verset": "Es 61:3", "huile": "Verveine", "plante": "Verveine séchée", "planete": "Saturne",
        "signification": "Épreuve purificatrice, transformation profonde.",
        "priere_salomonique": "Par Tétragrammaton Elohim, je transmute ma peine en sagesse et mes larmes en une rosée de renouveau spirituel."
    },
    "2222": {
        "nom": "Populus", "psaume": "Ps 3", "verset": "Gn 22:17", "huile": "Thym", "plante": "Thym commun", "planete": "Lune",
        "signification": "Stabilité collective, influence, paix intérieure.",
        "priere_salomonique": "Par Gabriel, messager céleste, que la paix soit sur mon assemblée et que ma voix résonne avec la force des multitudes."
    }
}

MAISON_INTERP = {
    1: "Vitalité / Soi", 2: "Argent / Biens", 3: "Communication / Proches", 4: "Foyer / Ancêtres",
    5: "Chance / Projets", 6: "Santé / Travail", 7: "Relations / Union", 8: "Transformation / Crise",
    9: "Voyage / Foi", 10: "Carrière / Succès", 11: "Amis / Appuis", 12: "Épreuves / Mal Occulte",
    13: "Résultat", 14: "Influence Externe", 15: "Le Juge (Sentence)", 16: "Conclusion"
}

# 3. LOGIQUE GÉOMANTIQUE
def addition(f1, f2): return "".join(["2" if (int(f1[i]) + int(f2[i])) % 2 == 0 else "1" for i in range(4)])

def calcul_theme(m):
    m = [None] + m
    m.extend([m[1][i]+m[2][i]+m[3][i]+m[4][i] for i in range(4)])
    m.extend([addition(m[1], m[2]), addition(m[3], m[4]), addition(m[5], m[6]), addition(m[7], m[8])])
    m.extend([addition(m[9], m[10]), addition(m[11], m[12]), addition(m[13], m[14]), addition(m[1], m[15])])
    return m

def get_heure_planetaire():
    cycle = ["Saturne", "Jupiter", "Mars", "Soleil", "Vénus", "Mercure", "Lune"]
    d = {"Monday": 6, "Tuesday": 2, "Wednesday": 5, "Thursday": 1, "Friday": 4, "Saturday": 0, "Sunday": 3}
    return cycle[(d[datetime.datetime.now().strftime("%A")] + datetime.datetime.now().hour) % 7]

# 4. INTERFACE
st.title("🛡️ Somadjely : Maîtrise Théurgique")
with st.sidebar:
    st.header("Diagnostic")
    mères = [st.text_input(f"Mère {i}", "1121") for i in range(1, 5)]
    maison_choisie = st.number_input("Maison à traiter (1-16)", 1, 16, 1)

if st.button("Dévoiler le Protocole"):
    theme = calcul_theme(mères)
    data = FIGURES_DATA.get(theme[maison_choisie])
    heure_actuelle = get_heure_planetaire()
    
    st.subheader(f"Maison {maison_choisie} : {MAISON_INTERP[maison_choisie]}
