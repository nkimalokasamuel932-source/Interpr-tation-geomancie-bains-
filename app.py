import streamlit as st
from collections import Counter

# ==============================================================================
# BASE DE DONNÉES ET FIGURES
# ==============================================================================
FIGURES = [
    "Via", "Populus", "Conjunctio", "Carcer", "Fortuna Major", "Fortuna Minor", 
    "Acquisitio", "Amissio", "Laetitia", "Tristitia", "Puella", "Puer", 
    "Albus", "Rubeus", "Caput Draconis", "Cauda Draconis"
]

DB = {
    "Youssouf": {"figure": FIGURES[0], "element": "Feu", "psaume": "Psaume 109", "verset": "Genèse 39:2", "priere": "Par le Nom Adonaï, dissipe les ténèbres.", "nassi": "111 fois, eau, safran", "plantes": "Laurier, Cannelle", "huiles": "Encens, Clou de girofle", "cloture": "Psaume 117", "sadaka": "Pain"},
    "Adama": {"figure": FIGURES[1], "element": "Feu", "psaume": "Psaume 121", "verset": "Genèse 2:7", "priere": "Par le Nom Elohim, j'invoque l'ancrage.", "nassi": "45 fois, eau + sel", "plantes": "Gingembre, Laurier", "huiles": "Orange, Encens", "cloture": "Psaume 128", "sadaka": "Denrées"},
    "Mahdy": {"figure": FIGURES[2], "element": "Air", "psaume": "Psaume 23", "verset": "Jérémie 29:11", "priere": "Par le Nom El-Shaddaï, l'abondance.", "nassi": "66 fois, rose + musc", "plantes": "Menthe, Sauge", "huiles": "Citron, Bergamote", "cloture": "Psaume 150", "sadaka": "Sucre"},
    "Idriss": {"figure": FIGURES[3], "element": "Eau", "psaume": "Psaume 119:9-16", "verset": "Hébreux 11:5", "priere": "Par le Nom El-Choura, le discernement.", "nassi": "360 fois, eau pluie", "plantes": "Aloès, Verveine", "huiles": "Lavande, Ylang", "cloture": "Psaume 23", "sadaka": "Eau"},
    "Ibrahima": {"figure": FIGURES[4], "element": "Eau", "psaume": "Psaume 112", "verset": "Genèse 12:2", "priere": "Par le Nom El-Elyon, je scelle la lignée.", "nassi": "72 fois, menthe", "plantes": "Verveine, Neem", "huiles": "Camomille, Lavande", "cloture": "Psaume 112", "sadaka": "Lait"},
    "Inssa": {"figure": FIGURES[5], "element": "Eau", "psaume": "Psaume 6", "verset": "Ésaïe 53:5", "priere": "Par le Nom Rapha, restaure la vigueur.", "nassi": "99 fois, neem", "plantes": "Neem, Aloès", "huiles": "Ylang, Lavande", "cloture": "Psaume 6", "sadaka": "Aumône"},
    "Omar": {"figure": FIGURES[6], "element": "Air", "psaume": "Psaume 35", "verset": "Proverbes 31:10", "priere": "Par le Nom Shalom, neutralise les discordes.", "nassi": "28 fois, parfum", "plantes": "Sauge, Menthe", "huiles": "Menthe, Citron", "cloture": "Psaume 35", "sadaka": "Sucre"},
    "Ayoub": {"figure": FIGURES[7], "element": "Terre", "psaume": "Psaume 88", "verset": "Job 19:25", "priere": "Par le Nom Yahvé, restauration.", "nassi": "88 fois, miel", "plantes": "Santal, Patchouli", "huiles": "Vétiver, Santal", "cloture": "Psaume 88", "sadaka": "Céréales"},
    "Allahou": {"figure": FIGURES[8], "element": "Feu", "psaume": "Psaume 91", "verset": "Exode 20:2", "priere": "Par le Nom El-Qahhar, ma Forteresse.", "nassi": "114 fois, eau", "plantes": "Laurier, Gingembre", "huiles": "Clou de girofle, Encens", "cloture": "Psaume 91", "sadaka": "Pain"},
    "Souleymane": {"figure": FIGURES[9], "element": "Terre", "psaume": "Psaume 72", "verset": "1 Rois 3:12", "priere": "Par le Nom Malek, autorité et justice.", "nassi": "110 fois, santal", "plantes": "Patchouli, Santal", "huiles": "Santal, Vétiver", "cloture": "Psaume 72", "sadaka": "Pièces"},
    "Aliou": {"figure": FIGURES[10], "element": "Air", "psaume": "Psaume 144", "verset": "Éphésiens 6:11", "priere": "Par le Nom Tsébaot, mon bouclier.", "nassi": "63 fois, camphre", "plantes": "Eucalyptus, Menthe", "huiles": "Bergamote, Menthe", "cloture": "Psaume 144", "sadaka": "Eau sucrée"},
    "Nouhou": {"figure": FIGURES[11], "element": "Terre", "psaume": "Psaume 29", "verset": "Genèse 6:8", "priere": "Par le Nom El-Hafiz, la tempête apaisée.", "nassi": "77 fois, eau mer", "plantes": "Cèdre, Santal", "huiles": "Cèdre, Santal", "cloture": "Psaume 29", "sadaka": "Céréales"},
    "Assane": {"figure": FIGURES[12], "element": "Eau", "psaume": "Psaume 3", "verset": "Psaume 3:3", "priere": "Par le Nom El-Adl, honneur.", "nassi": "55 fois, laurier", "plantes": "Neem, Aloès", "huiles": "Lavande, Camomille", "cloture": "Psaume 3", "sadaka": "Lait"},
    "Younouss": {"figure": FIGURES[13], "element": "Terre", "psaume": "Psaume 4", "verset": "Jonas 2:10", "priere": "Par le Nom El-Latif, dette libérée.", "nassi": "40 fois, pièce", "plantes": "Santal, Patchouli", "huiles": "Vétiver, Santal", "cloture": "Psaume 4", "sadaka": "Pièces"},
    "Ousmane": {"figure": FIGURES[14], "element": "Air", "psaume": "Psaume 119:105", "verset": "Actes 2:4", "priere": "Par le Nom El-Rouah, guidance.", "nassi": "19 fois, encens", "plantes": "Sauge, Menthe", "huiles": "Citron, Menthe", "cloture": "Psaume 119", "sadaka": "Sucre"},
    "Moussa": {"figure": FIGURES[15], "element": "Feu", "psaume": "Psaume 68", "verset": "Exode 14:13", "priere": "Par le Nom El-Fattah, succès.", "nassi": "16 fois, eau", "plantes": "Cannelle, Laurier", "huiles": "Encens, Clou de girofle", "cloture": "Psaume 68", "sadaka": "Dattes"}
}

# Interface
st.set_page_config(page_title="Oracle Ramrou", layout="wide")
st.title("🔮 Oracle Ramrou — Cabinet de Haute Théurgie")

# Sélection des maisons
theme = {m: st.sidebar.selectbox(f"Maison M{m}", list(DB.keys()), key=f"m{m}") for m in range(1, 17)}
figures_du_theme = [DB[theme[m]]['figure'] for m in range(1, 17)]

if st.button("🔮 GÉNÉRER L'ORDONNANCE"):
    juge = theme[16]
    d = DB[juge]
    
    # Analyse de Passation
    rep = Counter(figures_du_theme)
    passations = {f: c for f, c in rep.items() if c > 1}
    
    st.subheader(f"⚖️ Verdict du Juge : {juge} ({d['figure']})")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**📖 Psaume :** {d['psaume']} | **📜 Verset :** {d['verset']}")
        st.info(f"**🧪 Nassi :** {d['nassi']}")
    with col2:
        if passations:
            st.warning("⚠️ **Passation Active détectée :**")
            for fig, n in passations.items():
                st.write(f"- La figure **{fig}** se répète **{n} fois** (Influence amplifiée).")
        else:
            st.success("✅ Énergie fluide (Aucune répétition majeure).")

    st.divider()
    st.write("### 🗝️ Rituel Complet")
    st.text(f"OUVERTURE : Toi seul, ô Dieu de Salomon...")
    st.text(f"ACTIVATION (Ana Bekoach) : Par la force de Ta main droite, délie les liens...")
    st.text(f"FERMETURE : Lève-Toi, Seigneur, scelle cette prière.")
    
    # Export
    export = f"ORDONNANCE\nJuge: {juge}\nPassations: {passations}\nNassi: {d['nassi']}"
    st.download_button("📥 Télécharger", data=export, file_name="Ordonnance.txt")
