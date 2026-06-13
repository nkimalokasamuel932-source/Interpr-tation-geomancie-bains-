import streamlit as st

# ==============================================================================
# CONFIGURATION DE L'APPLICATION
# ==============================================================================
st.set_page_config(page_title="Oracle Ramrou — Grand Grimoire Théurgique", page_icon="🔮", layout="wide")

st.title("🔮 Oracle Ramrou — Cabinet Théurgique & Grand Grimoire")
st.markdown("Analyse complète et structurée : Passations, 70 règles d'engendrement, et Pharmacie Spirituelle.")

# ==============================================================================
# 1. BASE DE DONNÉES THÉURGIQUE ET PRIÈRES SALOMONIQUES
# ==============================================================================
PROPRIETES_FIGURES = {
    "Youssouf": {
        "num": 1, "nature": "Diable Mauvais", "groupe": "Mobiles", "element": "Feu (Est)",
        "psaume": "Psaume 109", "verset": "Genèse 39:2",
        "salomon": "Prière pour briser les complots et restaurer la dignité.",
        "priere": "Seigneur, Dieu de Joseph, par Ton Nom Adonaï, dissipe les ténèbres de la calomnie. Comme Tu as transformé la captivité de Joseph en gloire, restaure mon honneur.",
        "nassi": "Écrire 111 fois, laver avec eau de puits, safran et parfum de rose. Bain 7 jours."
    },
    "Adama": {
        "num": 2, "nature": "Diable Bon", "groupe": "Sortants", "element": "Feu (Est)",
        "psaume": "Psaume 121", "verset": "Genèse 2:7",
        "salomon": "Prière d'ancrage territorial et ouverture des portes matérielles.",
        "priere": "Par le Nom Elohim, j'invoque l'ancrage de mes racines dans la terre fertile de la bénédiction. Que mes biens soient protégés.",
        "nassi": "Tracer 45 fois sur ardoise. Eau + gros sel béni. Aspersion du corps et du seuil."
    },
    "Mahdy": {
        "num": 3, "nature": "Diable Bon", "groupe": "Rentrants", "element": "Air (Ouest)",
        "psaume": "Psaume 23", "verset": "Jérémie 29:11",
        "salomon": "Prière pour l'attraction de la grâce et des ressources.",
        "priere": "Par le Nom El-Shaddaï, Source de subsistance, débouche les canaux de l'abondance. Que Ta faveur attire les ressources nécessaires.",
        "nassi": "Écrire 66 fois avec eau de rose et musc. Boire chaque matin à jeun."
    },
    "Idriss": {
        "num": 4, "nature": "Diable Bon", "groupe": "Fixes", "element": "Eau (Nord)",
        "psaume": "Psaume 119:9-16", "verset": "Hébreux 11:5",
        "salomon": "Prière pour l'intelligence supérieure et la mémoire.",
        "priere": "Par le Nom El-Choura, sollicite l'illumination. Accorde-moi le discernement pour lire à travers les mystères.",
        "nassi": "Écrire 360 fois. Diluer dans eau de pluie. Oindre la tête avant étude."
    },
    "Ibrahima": {
        "num": 5, "nature": "Humain Bon", "groupe": "Mobiles", "element": "Eau (Nord)",
        "psaume": "Psaume 112", "verset": "Genèse 12:2",
        "salomon": "Prière d'alliance sacrée et protection de la lignée.",
        "priere": "Par le Nom El-Elyon, je scelle la protection de ma lignée. Que Ta bénédiction s'étende sur ma maison.",
        "nassi": "Écrire 72 fois. Infuser avec menthe fraîche. Boire ou asperger la chambre."
    },
    "Inssa": {
        "num": 6, "nature": "Humain Mauvais", "groupe": "Sortants", "element": "Eau (Nord)",
        "psaume": "Psaume 6", "verset": "Ésaïe 53:5",
        "salomon": "Prière de délivrance contre les afflictions biologiques.",
        "priere": "Par le Nom Rapha, demande la délivrance. Que Ta main curative efface la maladie.",
        "nassi": "Écrire 99 fois à l'encre Sami. Laver avec décoction de feuilles de neem."
    },
    "Omar": {
        "num": 7, "nature": "Diable Mauvais", "groupe": "Fixes", "element": "Air (Ouest)",
        "psaume": "Psaume 35", "verset": "Proverbes 31:10",
        "salomon": "Prière pour pacifier les relations et neutraliser la discorde.",
        "priere": "Par le Nom Shalom, j'invoque l'harmonie. Que les discordes soient neutralisées et les intrigues dissoutes.",
        "nassi": "Tracer 28 fois. Eau de source + 7 gouttes de parfum sans alcool. Aspersion maison."
    },
    "Ayoub": {
        "num": 8, "nature": "Diable Mauvais", "groupe": "Rentrants", "element": "Terre (Sud)",
        "psaume": "Psaume 88", "verset": "Job 19:25",
        "salomon": "Prière de restauration des biens et patience prophétique.",
        "priere": "Par le Nom Yahvé, demande la restauration. Que la patience soit ma force face à la ruine.",
        "nassi": "Écrire 88 fois. Dissoudre dans eau tiède et miel. Se laver un samedi soir."
    },
    "Allahou": {
        "num": 9, "nature": "Humain Mauvais", "groupe": "Sortants", "element": "Feu (Est)",
        "psaume": "Psaume 91", "verset": "Exode 20:2",
        "salomon": "Invocation de Souveraineté pour détruire les envoûtements.",
        "priere": "Par le Nom El-Qahhar, sois ma Forteresse. Que chaque sortilège soit annulé.",
        "nassi": "Écrire 114 fois. Eau de puits. Boire le vendredi, purifier commerce."
    },
    "Souleymane": {
        "num": 10, "nature": "Humain Bon", "groupe": "Fixes", "element": "Terre (Sud)",
        "psaume": "Psaume 72", "verset": "1 Rois 3:12",
        "salomon": "Grande Prière de Sagesse et Domination Royale.",
        "priere": "Par le Nom Malek, demande la sagesse. Accorde-moi l'autorité pour diriger avec justice.",
        "nassi": "Écrire 110 fois. Eau infusée au santal. Oindre mains et visage avant affaires."
    },
    "Aliou": {
        "num": 11, "nature": "Humain Mauvais", "groupe": "Fixes", "element": "Air (Ouest)",
        "psaume": "Psaume 144", "verset": "Éphésiens 6:11",
        "salomon": "Prière du Bouclier contre les attaques frontales.",
        "priere": "Par le Nom Tsébaot, revêts-moi de Ton Armure. Sois mon bouclier contre toute agression.",
        "nassi": "Écrire 63 fois. Eau + camphre. Se laver un mardi."
    },
    "Nouhou": {
        "num": 12, "nature": "Humain Bon", "groupe": "Rentrants", "element": "Terre (Sud)",
        "psaume": "Psaume 29", "verset": "Genèse 6:8",
        "salomon": "Prière de préservation au milieu des tempêtes.",
        "priere": "Par le Nom El-Hafiz, préserve-moi. Que Ta Grâce soit mon arche contre toute malice.",
        "nassi": "Écrire 77 fois. Eau de mer ou sel marin. Laver le sol de la concession."
    },
    "Assane": {
        "num": 13, "nature": "Diable Mauvais", "groupe": "Sortants", "element": "Eau (Nord)",
        "psaume": "Psaume 3", "verset": "Psaume 3:3",
        "salomon": "Prière de retournement de situation (honte en honneur).",
        "priere": "Par le Nom El-Adl, demande le retournement. Que la honte soit transmutée en honneur.",
        "nassi": "Écrire 55 fois (encre safranée). Eau + laurier. Bain 3 jours."
    },
    "Younouss": {
        "num": 14, "nature": "Diable Bon", "groupe": "Mobiles", "element": "Terre (Sud)",
        "psaume": "Psaume 4", "verset": "Jonas 2:10",
        "salomon": "Prière d'urgence pour sortir des dettes.",
        "priere": "Par le Nom El-Latif, libère-moi des chaînes de la dette. Fais sortir mes finances de l'impasse.",
        "nassi": "Écrire 40 fois. Eau + pièce d'argent trempée. Friction sur les mains."
    },
    "Ousmane": {
        "num": 15, "nature": "Humain Bon", "groupe": "Rentrants", "element": "Air (Ouest)",
        "psaume": "Psaume 119:105", "verset": "Actes 2:4",
        "salomon": "Prière d'intercession et connexion prophétique.",
        "priere": "Par le Nom El-Rouah, j'ouvre mon canal. Guide mes pas dans la lumière prophétique.",
        "nassi": "Écrire 19 fois. Infuser avec encens Oliban. Boire avant consultation."
    },
    "Moussa": {
        "num": 16, "nature": "Humain Mauvais", "groupe": "Fixes", "element": "Feu (Est)",
        "psaume": "Psaume 68", "verset": "Exode 14:13",
        "salomon": "Prière d'ouverture (Brise les barrières majeures).",
        "priere": "Par le Nom El-Fattah, demande le passage. Ouvre devant moi les chemins du succès.",
        "nassi": "Écrire 16 fois. Eau de source de l'aube. Nettoyer le seuil ou grand bain."
    }
}

# ==============================================================================
# 2. MAISONS, PASSATIONS ET RÈGLES DE COPULATION (Inclure ici votre dictionnaire REGLES_COPULATIONS)
# ==============================================================================
MAISONS_RAMROU = {
    1: {"nom": "M1 (Maison de l'Âme)", "desc": "État présent du consultant."},
    2: {"nom": "M2 (Maison de la Chance)", "desc": "Finances et gains."},
    3: {"nom": "M3 (Maison des Mères)", "desc": "Entourage proche."},
    4: {"nom": "M4 (Maison des Pères)", "desc": "Foyer et patrimoine."},
    5: {"nom": "M5 (Maison des Enfants)", "desc": "Descendance et amours."},
    6: {"nom": "M6 (Maison des Malades)", "desc": "Santé et travail."},
    7: {"nom": "M7 (Maison du Mariage)", "desc": "Conjoint et contrats."},
    8: {"nom": "M8 (Maison du Changement)", "desc": "Extérieur et héritage."},
    9: {"nom": "M9 (Maison de Dieu)", "desc": "Spiritualité et voyages."},
    10: {"nom": "M10 (Maison des Rois)", "desc": "Profession et pouvoir."},
    11: {"nom": "M11 (Maison de l'Espoir)", "desc": "Appuis et projets."},
    12: {"nom": "M12 (Maison des Ennemis)", "desc": "Pièges et sorcellerie."},
    13: {"nom": "M13 (Maison du Foyer)", "desc": "Intimité du couple."},
    14: {"nom": "M14 (Maison des Fortunes)", "desc": "Gains futurs."},
    15: {"nom": "M15 (Maison de l'Espace)", "desc": "Rumeurs et témoin."},
    16: {"nom": "M16 (Maison de Finition)", "desc": "Verdict final."}
}

# (Note : Intégrer ici vos dictionnaires INTERPRETATIONS_PASSATIONS et REGLES_COPULATIONS complets)

# ==============================================================================
# 3. MOTEUR DE L'INTERFACE
# ==============================================================================
st.sidebar.header("📥 Saisie des Figures")
theme_actuel = {m: st.sidebar.selectbox(f"{MAISONS_RAMROU[m]['nom']}", list(PROPRIETES_FIGURES.keys()), key=f"m_{m}") for m in range(1, 17)}

st.subheader("📊 Configuration de l'Échiquier")
cols = st.columns(4)
for i, m in enumerate(range(1, 17)):
    cols[i % 4].markdown(f"**M{m}**: `{theme_actuel[m]}`")

st.divider()
st.header("🌿 CABINET THÉURGIQUE")

for fig in sorted(set(theme_actuel.values())):
    data = PROPRIETES_FIGURES[fig]
    with st.expander(f"✨ Ordonnance : {fig}"):
        col1, col2 = st.columns(2)
        col1.markdown(f"📖 **Psaume:** {data['psaume']}\n👑 **Prière:** {data['priere']}")
        col2.info(f"🧪 **Protocole Nassi:** {data['nassi']}")
```[cite: 1]
