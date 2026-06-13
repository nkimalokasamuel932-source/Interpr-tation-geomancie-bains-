import streamlit as st

# ==============================================================================
# 1. BASE DE DONNÉES THÉURGIQUE ET PRIÈRES
# ==============================================================================
PROPRIETES_FIGURES = {
    "Youssouf": {"psaume": "Psaume 109", "verset": "Genèse 39:2", "priere": "Seigneur, Dieu de Joseph, par Ton Nom Adonaï, dissipe les ténèbres de la calomnie. Comme Tu as transformé la captivité de Joseph en gloire, restaure mon honneur.", "nassi": "Écrire 111 fois, laver avec eau de puits, safran et parfum de rose. Bain 7 jours."},
    "Adama": {"psaume": "Psaume 121", "verset": "Genèse 2:7", "priere": "Par le Nom Elohim, j'invoque l'ancrage de mes racines dans la terre fertile. Que mes biens soient protégés et multipliés.", "nassi": "Tracer 45 fois sur ardoise. Eau + gros sel béni. Aspersion du corps et du seuil."},
    "Mahdy": {"psaume": "Psaume 23", "verset": "Jérémie 29:11", "priere": "Par le Nom El-Shaddaï, Source de toute subsistance, débouche les canaux de l'abondance. Que Ta faveur attire les ressources.", "nassi": "Écrire 66 fois avec eau de rose et musc. Boire chaque matin à jeun."},
    "Idriss": {"psaume": "Psaume 119:9-16", "verset": "Hébreux 11:5", "priere": "Par le Nom El-Choura, Dieu de Sagesse, accorde-moi le discernement pour lire à travers les mystères.", "nassi": "Écrire 360 fois. Diluer dans eau de pluie. Oindre la tête avant étude."},
    "Ibrahima": {"psaume": "Psaume 112", "verset": "Genèse 12:2", "priere": "Par le Nom El-Elyon, je scelle la protection de ma lignée. Que Ta bénédiction s'étende sur ma maison.", "nassi": "Écrire 72 fois. Infuser avec menthe fraîche. Boire ou asperger la chambre."},
    "Inssa": {"psaume": "Psaume 6", "verset": "Ésaïe 53:5", "priere": "Par le Nom Rapha, Dieu qui guérit, efface la maladie et restaure la vigueur de mon esprit.", "nassi": "Écrire 99 fois à l'encre Sami. Laver avec décoction de feuilles de neem."},
    "Omar": {"psaume": "Psaume 35", "verset": "Proverbes 31:10", "priere": "Par le Nom Shalom, j'invoque l'harmonie. Que les discordes soient neutralisées et les intrigues dissoutes.", "nassi": "Tracer 28 fois. Eau de source + 7 gouttes de parfum sans alcool. Aspersion maison."},
    "Ayoub": {"psaume": "Psaume 88", "verset": "Job 19:25", "priere": "Par le Nom Yahvé, demande la restauration. Que la patience soit ma force face à la ruine.", "nassi": "Écrire 88 fois. Dissoudre dans eau tiède et miel. Se laver un samedi soir."},
    "Allahou": {"psaume": "Psaume 91", "verset": "Exode 20:2", "priere": "Par le Nom El-Qahhar, sois ma Forteresse. Que chaque sortilège soit annulé par Ta Protection.", "nassi": "Écrire 114 fois. Eau de puits. Boire le vendredi, purifier le commerce."},
    "Souleymane": {"psaume": "Psaume 72", "verset": "1 Rois 3:12", "priere": "Par le Nom Malek, Roi des Rois, accorde-moi l'autorité pour diriger mes affaires avec justice.", "nassi": "Écrire 110 fois. Eau infusée au santal. Oindre mains et visage avant affaires."},
    "Aliou": {"psaume": "Psaume 144", "verset": "Éphésiens 6:11", "priere": "Par le Nom Tsébaot, revêts-moi de Ton Armure. Sois mon bouclier contre toute agression.", "nassi": "Écrire 63 fois. Eau + camphre. Se laver un mardi."},
    "Nouhou": {"psaume": "Psaume 29", "verset": "Genèse 6:8", "priere": "Par le Nom El-Hafiz, demande à être préservé au milieu de la tempête. Que Ta Grâce soit mon arche.", "nassi": "Écrire 77 fois. Eau de mer ou sel marin. Laver le sol de la concession."},
    "Assane": {"psaume": "Psaume 3", "verset": "Psaume 3:3", "priere": "Par le Nom El-Adl, demande le retournement de mon sort. Que la honte soit transmutée en honneur.", "nassi": "Écrire 55 fois (encre safranée). Eau + laurier. Bain 3 jours."},
    "Younouss": {"psaume": "Psaume 4", "verset": "Jonas 2:10", "priere": "Par le Nom El-Latif, libère-moi des chaînes de la dette. Fais sortir mes finances de toute impasse.", "nassi": "Écrire 40 fois. Eau + pièce d'argent trempée. Friction sur les mains."},
    "Ousmane": {"psaume": "Psaume 119:105", "verset": "Actes 2:4", "priere": "Par le Nom El-Rouah, Esprit de Vérité, guide mes pas dans la lumière de la haute guidance.", "nassi": "Écrire 19 fois. Infuser avec encens Oliban. Boire avant consultation."},
    "Moussa": {"psaume": "Psaume 68", "verset": "Exode 14:13", "priere": "Par le Nom El-Fattah, demande le passage. Ouvre devant moi les chemins du succès.", "nassi": "Écrire 16 fois. Eau de source de l'aube. Nettoyer le seuil ou grand bain."}
}

# ==============================================================================
# 2. LOGIQUE D'ORDONNANCE SYNTHÉTIQUE
# ==============================================================================
def generer_ordonnance_finale(theme):
    f_maitre = theme[1]
    verdict = theme[16]
    data = PROPRIETES_FIGURES[f_maitre]
    
    return f"""
    ### 🛡️ ORDONNANCE DE SYNTHÈSE (DÉBLOCAGE GLOBAL)
    
    **Analyse du Consultant (Maison 1 - {f_maitre}) :** 
    {data['priere']}[cite: 1]
    
    **Verdict de l'Oracle (Maison 16 - {verdict}) :** 
    Pour sceller ce verdict et débloquer la situation, appliquez ce protocole :[cite: 1]
    
    *   **Psaume d'Activation :** {data['psaume']} ({data['verset']})[cite: 1]
    *   **Protocole Nassi :** {data['nassi']}[cite: 1]
    *   **Orientation :** Pratiquez ce rite face à la direction cardinale dominante du tirage pour aligner vos énergies.[cite: 1]
    """

# ==============================================================================
# 3. INTERFACE STREAMLIT
# ==============================================================================
st.set_page_config(page_title="Oracle Ramrou", page_icon="🔮", layout="wide")
st.title("🔮 Oracle Ramrou — Cabinet Théurgique")

st.sidebar.header("📥 Saisie des Figures")
theme_actuel = {m: st.sidebar.selectbox(f"Maison {m}", list(PROPRIETES_FIGURES.keys())) for m in range(1, 17)}

st.header("🌿 Ordonnances Spirituelles")

# Affichage des détails par figure
for fig in sorted(set(theme_actuel.values())):
    d = PROPRIETES_FIGURES[fig]
    with st.expander(f"✨ Détails pour : {fig}"):
        st.markdown(f"📖 **Psaume :** {d['psaume']} | 📜 **Verset :** {d['verset']}")
        st.warning(f"🙏 **Prière :** {d['priere']}")
        st.info(f"🧪 **Protocole Nassi :** {d['nassi']}")

st.divider()

# Génération de l'ordonnance globale
if st.button("🔮 GÉNÉRER L'ORDONNANCE DE DÉBLOCAGE DU THÈME"):
    st.markdown(generer_ordonnance_finale(theme_actuel))
