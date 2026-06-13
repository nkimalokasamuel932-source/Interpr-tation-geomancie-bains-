import streamlit as st

# ==============================================================================
# BASE DE DONNÉES TOTALE ET EXHAUSTIVE
# ==============================================================================
DB = {
    "Youssouf": {
        "el": "Feu", "couleur": "Rouge", "heure": "Mardi, Aube", "support": "Papier/Encre Safran", "cloture": "Psaume 117", "sadaka": "Pain/Dattes",
        "psaume": "Psaume 109", "verset": "Genèse 39:2", "nassi": "111 fois, eau de puits + safran + rose. Bain 7j",
        "priere": "Seigneur, Dieu de Joseph, par Ton Nom Adonaï, dissipe les ténèbres de la calomnie. Restaure mon honneur.",
        "plantes": "Laurier, Cannelle", "huiles": "Encens (Oliban)"
    },
    "Adama": {
        "el": "Terre", "couleur": "Vert", "heure": "Samedi, Soir", "support": "Ardoise/Craie", "cloture": "Psaume 128", "sadaka": "Pièces",
        "psaume": "Psaume 121", "verset": "Genèse 2:7", "nassi": "45 fois, eau + gros sel. Aspersion corps/seuil",
        "priere": "Par le Nom Elohim, j'invoque l'ancrage de mes racines dans la terre fertile.",
        "plantes": "Gingembre", "huiles": "Orange douce"
    },
    "Mahdy": {
        "el": "Air", "couleur": "Jaune", "heure": "Mercredi, Midi", "support": "Papier blanc", "cloture": "Psaume 150", "sadaka": "Sucre/Lait",
        "psaume": "Psaume 23", "verset": "Jérémie 29:11", "nassi": "66 fois, eau de rose + musc. Boire à jeun",
        "priere": "Par le Nom El-Shaddaï, débouche les canaux de l'abondance.",
        "plantes": "Menthe", "huiles": "Citron"
    },
    "Idriss": {
        "el": "Eau", "couleur": "Bleu", "heure": "Lundi, Aube", "support": "Feuille d'arbre", "cloture": "Psaume 23", "sadaka": "Eau pure",
        "psaume": "Psaume 119:9-16", "verset": "Hébreux 11:5", "nassi": "360 fois, eau de pluie. Oindre la tête",
        "priere": "Par le Nom El-Choura, Dieu de Sagesse, accorde-moi le discernement.",
        "plantes": "Aloès", "huiles": "Lavande"
    },
    "Ibrahima": {
        "el": "Eau", "couleur": "Blanc", "heure": "Jeudi, Aube", "support": "Papier/Encre Noire", "cloture": "Psaume 112", "sadaka": "Lait",
        "psaume": "Psaume 112", "verset": "Genèse 12:2", "nassi": "72 fois, menthe fraîche. Boire ou asperger",
        "priere": "Par le Nom El-Elyon, scelle la protection de ma lignée.",
        "plantes": "Verveine", "huiles": "Camomille"
    },
    "Inssa": {
        "el": "Eau", "couleur": "Bleu pâle", "heure": "Lundi, Nuit", "support": "Ardoise", "cloture": "Psaume 6", "sadaka": "Aumône",
        "psaume": "Psaume 6", "verset": "Ésaïe 53:5", "nassi": "99 fois, feuilles de neem. Bain rituel",
        "priere": "Par le Nom Rapha, efface la maladie et restaure la vigueur.",
        "plantes": "Neem", "huiles": "Ylang-Ylang"
    },
    "Omar": {
        "el": "Air", "couleur": "Gris", "heure": "Mercredi, Coucher", "support": "Parchemin", "cloture": "Psaume 35", "sadaka": "Sucre",
        "psaume": "Psaume 35", "verset": "Proverbes 31:10", "nassi": "28 fois, parfum sans alcool. Aspersion maison",
        "priere": "Par le Nom Shalom, neutralise les intrigues et discorde.",
        "plantes": "Sauge", "huiles": "Menthe poivrée"
    },
    "Ayoub": {
        "el": "Terre", "couleur": "Marron", "heure": "Samedi, Nuit", "support": "Terre cuite", "cloture": "Psaume 88", "sadaka": "Céréales",
        "psaume": "Psaume 88", "verset": "Job 19:25", "nassi": "88 fois, miel. Laver le samedi soir",
        "priere": "Par le Nom Yahvé, demande la restauration de ce qui est perdu.",
        "plantes": "Santal", "huiles": "Vétiver"
    },
    "Allahou": {
        "el": "Feu", "couleur": "Rouge vif", "heure": "Mardi, Midi", "support": "Papier/Encre Safran", "cloture": "Psaume 91", "sadaka": "Pain",
        "psaume": "Psaume 91", "verset": "Exode 20:2", "nassi": "114 fois, eau de puits. Purifier commerce",
        "priere": "Par le Nom El-Qahhar, sois ma Forteresse, annule tout sortilège.",
        "plantes": "Laurier", "huiles": "Clou de girofle"
    },
    "Souleymane": {
        "el": "Terre", "couleur": "Or", "heure": "Samedi, Aube", "support": "Parchemin", "cloture": "Psaume 72", "sadaka": "Pièces",
        "psaume": "Psaume 72", "verset": "1 Rois 3:12", "nassi": "110 fois, santal. Oindre mains et visage",
        "priere": "Par le Nom Malek, accorde-moi l'autorité et la justice.",
        "plantes": "Patchouli", "huiles": "Santal"
    },
    "Aliou": {
        "el": "Air", "couleur": "Violet", "heure": "Mercredi, Aube", "support": "Papier blanc", "cloture": "Psaume 144", "sadaka": "Eau sucrée",
        "psaume": "Psaume 144", "verset": "Éphésiens 6:11", "nassi": "63 fois, camphre. Laver le mardi",
        "priere": "Par le Nom Tsébaot, sois mon bouclier contre les agressions.",
        "plantes": "Eucalyptus", "huiles": "Bergamote"
    },
    "Nouhou": {
        "el": "Terre", "couleur": "Noir", "heure": "Samedi, Minuit", "support": "Ardoise", "cloture": "Psaume 29", "sadaka": "Céréales",
        "psaume": "Psaume 29", "verset": "Genèse 6:8", "nassi": "77 fois, eau de mer. Laver le sol",
        "priere": "Par le Nom El-Hafiz, préserve-moi de la tempête.",
        "plantes": "Cèdre", "huiles": "Cèdre"
    },
    "Assane": {
        "el": "Eau", "couleur": "Bleu", "heure": "Lundi, Midi", "support": "Papier/Encre Safran", "cloture": "Psaume 3", "sadaka": "Lait",
        "psaume": "Psaume 3", "verset": "Psaume 3:3", "nassi": "55 fois, laurier. Bain 3 jours",
        "priere": "Par le Nom El-Adl, transmute la honte en honneur.",
        "plantes": "Neem", "huiles": "Lavande"
    },
    "Younouss": {
        "el": "Terre", "couleur": "Vert", "heure": "Samedi, Aube", "support": "Parchemin", "cloture": "Psaume 4", "sadaka": "Pièces",
        "psaume": "Psaume 4", "verset": "Jonas 2:10", "nassi": "40 fois, pièce argent. Friction des mains",
        "priere": "Par le Nom El-Latif, libère-moi des chaînes de la dette.",
        "plantes": "Santal", "huiles": "Vétiver"
    },
    "Ousmane": {
        "el": "Air", "couleur": "Bleu ciel", "heure": "Mercredi, Nuit", "support": "Feuille", "cloture": "Psaume 119", "sadaka": "Sucre",
        "psaume": "Psaume 119:105", "verset": "Actes 2:4", "nassi": "19 fois, encens Oliban. Boire avant consultation",
        "priere": "Par le Nom El-Rouah, guide mes pas dans la haute guidance.",
        "plantes": "Sauge", "huiles": "Citron"
    },
    "Moussa": {
        "el": "Feu", "couleur": "Rouge", "heure": "Mardi, Midi", "support": "Papier/Encre Safran", "cloture": "Psaume 68", "sadaka": "Dattes",
        "psaume": "Psaume 68", "verset": "Exode 14:13", "nassi": "16 fois, eau aube. Nettoyer seuil ou bain",
        "priere": "Par le Nom El-Fattah, ouvre les chemins du succès.",
        "plantes": "Cannelle", "huiles": "Encens (Oliban)"
    }
}

# ==============================================================================
# INTERFACE
# ==============================================================================
st.set_page_config(page_title="Oracle Ramrou", layout="wide")
st.title("🔮 Oracle Ramrou — Cabinet Théurgique Complet")

juge = st.sidebar.selectbox("Sélectionnez la figure du Juge (M16) :", list(DB.keys()))

if juge:
    d = DB[juge]
    st.subheader(f"⚖️ Verdict du Juge : {juge}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("### 📜 Ordonnance Théurgique")
        st.markdown(f"**Psaume :** {d['psaume']}")
        st.markdown(f"**Verset (Nassi) :** {d['verset']}")
        st.info(f"**Protocole Nassi :** {d['nassi']}")
        st.warning(f"**Prière Salomonique :**\n\n> *{d['priere']}*")
        
    with col2:
        st.write("### 🌿 Supports & Rituels")
        st.success(f"**Plantes :** {d['plantes']} | **Huiles :** {d['huiles']}")
        st.write(f"**Préparation :** Heure: {d['heure']} | Support: {d['support']} | Bougie: {d['couleur']}")
        st.error(f"**Clôture :** {d['cloture']} | **Sadaka :** {d['sadaka']}")
