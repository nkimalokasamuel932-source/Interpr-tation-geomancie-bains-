import streamlit as st

# ==============================================================================
# BASE DE DONNÉES COMPLÈTE
# ==============================================================================
PROPRIETES_FIGURES = {
    "Youssouf": {"element": "Feu (Est)", "psaume": "Psaume 109", "verset": "Genèse 39:2", "priere": "Par le Nom Adonaï, dissipe les calomnies.", "nassi": "Écrire 111 fois, eau de puits + safran. Bain 7j."},
    "Adama": {"element": "Feu (Est)", "psaume": "Psaume 121", "verset": "Genèse 2:7", "priere": "Par le Nom Elohim, ancre mes racines dans la terre fertile.", "nassi": "Tracer 45 fois, gros sel. Aspersion seuil."},
    "Mahdy": {"element": "Air (Ouest)", "psaume": "Psaume 23", "verset": "Jérémie 29:11", "priere": "Par le Nom El-Shaddaï, débouche les canaux de l'abondance.", "nassi": "Écrire 66 fois, eau de rose + musc. Boire à jeun."},
    "Idriss": {"element": "Eau (Nord)", "psaume": "Psaume 119", "verset": "Hébreux 11:5", "priere": "Par le Nom El-Choura, illumine mon esprit.", "nassi": "Écrire 360 fois, eau de pluie. Oindre la tête."},
    "Ibrahima": {"element": "Eau (Nord)", "psaume": "Psaume 112", "verset": "Genèse 12:2", "priere": "Par le Nom El-Elyon, protège ma lignée et ma maison.", "nassi": "Écrire 72 fois, menthe. Asperger la chambre."},
    "Inssa": {"element": "Eau (Nord)", "psaume": "Psaume 6", "verset": "Ésaïe 53:5", "priere": "Par le Nom Rapha, efface la maladie.", "nassi": "Écrire 99 fois, feuilles de neem. Bain rituel."},
    "Omar": {"element": "Air (Ouest)", "psaume": "Psaume 35", "verset": "Proverbes 31:10", "priere": "Par le Nom Shalom, neutralise les intrigues.", "nassi": "Tracer 28 fois, parfum sans alcool. Aspersion maison."},
    "Ayoub": {"element": "Terre (Sud)", "psaume": "Psaume 88", "verset": "Job 19:25", "priere": "Par le Nom Yahvé, restaure ce qui a été perdu.", "nassi": "Écrire 88 fois, miel. Laver le samedi soir."},
    "Allahou": {"element": "Feu (Est)", "psaume": "Psaume 91", "verset": "Exode 20:2", "priere": "Par le Nom El-Qahhar, sois ma Forteresse.", "nassi": "Écrire 114 fois, eau de puits. Purifier commerce."},
    "Souleymane": {"element": "Terre (Sud)", "psaume": "Psaume 72", "verset": "1 Rois 3:12", "priere": "Par le Nom Malek, accorde-moi sagesse et justice.", "nassi": "Écrire 110 fois, santal. Oindre mains et visage."},
    "Aliou": {"element": "Air (Ouest)", "psaume": "Psaume 144", "verset": "Éphésiens 6:11", "priere": "Par le Nom Tsébaot, sois mon bouclier contre les agressions.", "nassi": "Écrire 63 fois, camphre. Laver le mardi."},
    "Nouhou": {"element": "Terre (Sud)", "psaume": "Psaume 29", "verset": "Genèse 6:8", "priere": "Par le Nom El-Hafiz, préserve-moi de la tempête.", "nassi": "Écrire 77 fois, sel marin. Laver le sol."},
    "Assane": {"element": "Eau (Nord)", "psaume": "Psaume 3", "verset": "Psaume 3:3", "priere": "Par le Nom El-Adl, transmute la honte en honneur.", "nassi": "Écrire 55 fois, laurier. Bain 3 jours."},
    "Younouss": {"element": "Terre (Sud)", "psaume": "Psaume 4", "verset": "Jonas 2:10", "priere": "Par le Nom El-Latif, libère-moi de la dette.", "nassi": "Écrire 40 fois, pièce argent. Friction des mains."},
    "Ousmane": {"element": "Air (Ouest)", "psaume": "Psaume 119:105", "verset": "Actes 2:4", "priere": "Par le Nom El-Rouah, guide mes pas dans la lumière.", "nassi": "Écrire 19 fois, encens Oliban. Boire avant consultation."},
    "Moussa": {"element": "Feu (Est)", "psaume": "Psaume 68", "verset": "Exode 14:13", "priere": "Par le Nom El-Fattah, ouvre le chemin du succès.", "nassi": "Écrire 16 fois, eau de l'aube. Nettoyer le seuil."}
}

# ==============================================================================
# INTERFACE
# ==============================================================================
st.set_page_config(page_title="Oracle Ramrou", layout="wide")
st.title("🔮 Oracle Ramrou — Cabinet de Haute Théurgie")

# Saisie de la question
st.sidebar.header("📋 Contextualisation")
question = st.sidebar.text_area("Quelle est la question ou l'objet du thème ?")
intention = st.sidebar.selectbox("Intention du rituel :", ["Déblocage", "Protection", "Attraction", "Apaisement"])

# Sélection des figures
st.sidebar.header("📥 Figures du Tirage")
theme = {m: st.sidebar.selectbox(f"Maison {m}", list(PROPRIETES_FIGURES.keys()), key=f"m_{m}") for m in range(1, 17)}

# Affichage de l'analyse
if question:
    st.info(f"💡 **Analyse pour :** {question}")

def generer_ordonnance(theme, intention):
    f_maitre = theme[1]
    data = PROPRIETES_FIGURES[f_maitre]
    
    conseil_sadaka = "Donner à un nécessiteux selon l'élément de la figure (Feu: Mardi/Rouge, Terre: Samedi/Pièces, Eau/Air: Lundi/Eau-Sucre)."
    
    return f"""
    ### 🛡️ ORDONNANCE : {intention.upper()}
    **Basée sur la figure en M1 : {f_maitre}**
    
    * **Prière Salomonique :** {data['priere']}
    * **Protocole Nassi :** {data['nassi']}
    * **Activation Vibratoire :** {data['psaume']} - {data['verset']}
    * **Conseil Sadaka (Aumône) :** {conseil_sadaka}
    
    *Note : Effectuez ce rite en vous orientant selon l'élément **{data['element']}** pour charger votre travail.*
    """

if st.button("🔮 GÉNÉRER L'ORDONNANCE DE RÉSOLUTION"):
    st.markdown(generer_ordonnance(theme, intention))
