import streamlit as st
# Ajoutez ceci juste après st.title("🔮 Oracle Ramrou...")
st.markdown("""
> *« Toi seul, ô Dieu de Salomon, règnes sur ce qui est visible et sur ce qui ne l'est pas. 
> Je me présente devant Toi, non comme un étranger, mais comme un héritier de Ton Alliance. 
> Que Ta Sagesse guide cette consultation. »*
""")
st.divider()

# ==============================================================================
# BASE DE DONNÉES MAÎTRE (16 FIGURES)
# ==============================================================================
DB = {
    "Youssouf": {"psaume": "Psaume 109", "verset": "Genèse 39:2", "priere": "Seigneur, Dieu de Joseph, par Ton Nom Adonaï, dissipe les ténèbres de la calomnie. Restaure mon honneur.", "nassi": "111 fois, eau de puits + safran + rose. Bain 7j", "plantes": "Laurier, Cannelle", "huiles": "Encens (Oliban)", "heure": "Mardi, Aube", "support": "Papier/Encre Safran", "cloture": "Psaume 117", "sadaka": "Pain et dattes"},
    "Adama": {"psaume": "Psaume 121", "verset": "Genèse 2:7", "priere": "Par le Nom Elohim, j'invoque l'ancrage de mes racines dans la terre fertile.", "nassi": "45 fois, eau + gros sel. Aspersion corps/seuil", "plantes": "Gingembre", "huiles": "Orange douce", "heure": "Samedi, Soir", "support": "Ardoise/Craie", "cloture": "Psaume 128", "sadaka": "Pièces"},
    "Mahdy": {"psaume": "Psaume 23", "verset": "Jérémie 29:11", "priere": "Par le Nom El-Shaddaï, débouche les canaux de l'abondance.", "nassi": "66 fois, eau de rose + musc. Boire à jeun", "plantes": "Menthe", "huiles": "Citron", "heure": "Mercredi, Midi", "support": "Papier blanc", "cloture": "Psaume 150", "sadaka": "Sucre et lait"},
    "Idriss": {"psaume": "Psaume 119:9-16", "verset": "Hébreux 11:5", "priere": "Par le Nom El-Choura, accorde-moi le discernement.", "nassi": "360 fois, eau de pluie. Oindre la tête", "plantes": "Aloès", "huiles": "Lavande", "heure": "Lundi, Aube", "support": "Feuille d'arbre", "cloture": "Psaume 23", "sadaka": "Eau pure"},
    "Ibrahima": {"psaume": "Psaume 112", "verset": "Genèse 12:2", "priere": "Par le Nom El-Elyon, scelle la protection de ma lignée.", "nassi": "72 fois, menthe fraîche. Boire ou asperger", "plantes": "Verveine", "huiles": "Camomille", "heure": "Jeudi, Aube", "support": "Papier/Encre Noire", "cloture": "Psaume 112", "sadaka": "Lait"},
    "Inssa": {"psaume": "Psaume 6", "verset": "Ésaïe 53:5", "priere": "Par le Nom Rapha, efface la maladie et restaure la vigueur.", "nassi": "99 fois, feuilles de neem. Bain rituel", "plantes": "Neem", "huiles": "Ylang-Ylang", "heure": "Lundi, Nuit", "support": "Ardoise", "cloture": "Psaume 6", "sadaka": "Aumône nécessiteux"},
    "Omar": {"psaume": "Psaume 35", "verset": "Proverbes 31:10", "priere": "Par le Nom Shalom, neutralise les intrigues et discorde.", "nassi": "28 fois, parfum sans alcool. Aspersion maison", "plantes": "Sauge", "huiles": "Menthe poivrée", "heure": "Mercredi, Coucher", "support": "Parchemin", "cloture": "Psaume 35", "sadaka": "Sucre"},
    "Ayoub": {"psaume": "Psaume 88", "verset": "Job 19:25", "priere": "Par le Nom Yahvé, demande la restauration de ce qui est perdu.", "nassi": "88 fois, miel. Laver le samedi soir", "plantes": "Santal", "huiles": "Vétiver", "heure": "Samedi, Nuit", "support": "Terre cuite", "cloture": "Psaume 88", "sadaka": "Céréales"},
    "Allahou": {"psaume": "Psaume 91", "verset": "Exode 20:2", "priere": "Par le Nom El-Qahhar, sois ma Forteresse, annule tout sortilège.", "nassi": "114 fois, eau de puits. Purifier commerce", "plantes": "Laurier", "huiles": "Clou de girofle", "heure": "Mardi, Midi", "support": "Papier/Encre Safran", "cloture": "Psaume 91", "sadaka": "Pain"},
    "Souleymane": {"psaume": "Psaume 72", "verset": "1 Rois 3:12", "priere": "Par le Nom Malek, accorde-moi l'autorité et la justice.", "nassi": "110 fois, santal. Oindre mains et visage", "plantes": "Patchouli", "huiles": "Santal", "heure": "Samedi, Aube", "support": "Parchemin", "cloture": "Psaume 72", "sadaka": "Pièces"},
    "Aliou": {"psaume": "Psaume 144", "verset": "Éphésiens 6:11", "priere": "Par le Nom Tsébaot, sois mon bouclier contre les agressions.", "nassi": "63 fois, camphre. Laver le mardi", "plantes": "Eucalyptus", "huiles": "Bergamote", "heure": "Mercredi, Aube", "support": "Papier blanc", "cloture": "Psaume 144", "sadaka": "Eau sucrée"},
    "Nouhou": {"psaume": "Psaume 29", "verset": "Genèse 6:8", "priere": "Par le Nom El-Hafiz, préserve-moi de la tempête.", "nassi": "77 fois, eau de mer. Laver le sol", "plantes": "Cèdre", "huiles": "Cèdre", "heure": "Samedi, Minuit", "support": "Ardoise", "cloture": "Psaume 29", "sadaka": "Céréales"},
    "Assane": {"psaume": "Psaume 3", "verset": "Psaume 3:3", "priere": "Par le Nom El-Adl, transmute la honte en honneur.", "nassi": "55 fois, laurier. Bain 3 jours", "plantes": "Neem", "huiles": "Lavande", "heure": "Lundi, Midi", "support": "Papier/Encre Safran", "cloture": "Psaume 3", "sadaka": "Lait"},
    "Younouss": {"psaume": "Psaume 4", "verset": "Jonas 2:10", "priere": "Par le Nom El-Latif, libère-moi des chaînes de la dette.", "nassi": "40 fois, pièce argent. Friction des mains", "plantes": "Santal", "huiles": "Vétiver", "heure": "Samedi, Aube", "support": "Parchemin", "cloture": "Psaume 4", "sadaka": "Pièces"},
    "Ousmane": {"psaume": "Psaume 119:105", "verset": "Actes 2:4", "priere": "Par le Nom El-Rouah, guide mes pas dans la haute guidance.", "nassi": "19 fois, encens Oliban. Boire avant consultation", "plantes": "Sauge", "huiles": "Citron", "heure": "Mercredi, Nuit", "support": "Feuille", "cloture": "Psaume 119", "sadaka": "Sucre"},
    "Moussa": {"psaume": "Psaume 68", "verset": "Exode 14:13", "priere": "Par le Nom El-Fattah, ouvre les chemins du succès.", "nassi": "16 fois, eau aube. Nettoyer seuil ou bain", "plantes": "Cannelle", "huiles": "Encens (Oliban)", "heure": "Mardi, Midi", "support": "Papier/Encre Safran", "cloture": "Psaume 68", "sadaka": "Dattes"}
}

# ==============================================================================
# INTERFACE
# ==============================================================================
st.set_page_config(page_title="Oracle Ramrou", layout="wide")
st.title("🔮 Oracle Ramrou — Cabinet Théurgique complet")

st.sidebar.header("📥 Saisie du Tirage")
theme = {m: st.sidebar.selectbox(f"Maison {m}", list(DB.keys()), key=f"m_{m}") for m in range(1, 17)}

if st.button("🔮 GÉNÉRER L'ORDONNANCE TOTALE"):
    juge = theme[16]
    d = DB[juge]
    st.subheader(f"⚖️ Verdict du Juge (M16) : {juge}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("### 📜 Ordonnance & Prières")
        st.markdown(f"**Psaume :** {d['psaume']}")
        st.markdown(f"**Verset (Nassi) :** {d['verset']}")
        st.markdown(f"**Protocole Nassi :** {d['nassi']}")
        st.warning(f"**Prière Salomonique :**\n\n> *{d['priere']}*")
    with col2:
        st.write("### 🌿 Rituels & Supports")
        st.success(f"**Plantes :** {d['plantes']} | **Huiles :** {d['huiles']}")
        st.write(f"**Préparation :** {d['heure']} | **Support :** {d['support']}")
        st.error(f"**Clôture :** {d['cloture']} | **Sadaka :** {d['sadaka']}")
