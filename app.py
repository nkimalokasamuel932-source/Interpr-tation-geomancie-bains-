import streamlit as st

# ==============================================================================
# BASE DE DONNÉES MAÎTRE (AVEC FIGURES GÉOMANTIQUES)
# ==============================================================================
# Figures associées aux 16 maisons
FIGURES = [
    "Via (La Voie)", "Populus (Le Peuple)", "Conjunctio (La Réunion)", "Carcer (La Prison)",
    "Fortuna Major (Grande Fortune)", "Fortuna Minor (Petite Fortune)", "Acquisitio (Le Gain)", "Amissio (La Perte)",
    "Laetitia (La Joie)", "Tristitia (La Tristesse)", "Puella (La Jeune Fille)", "Puer (Le Jeune Homme)",
    "Albus (Le Blanc)", "Rubeus (Le Rouge)", "Caput Draconis (Tête du Dragon)", "Cauda Draconis (Queue du Dragon)"
]

DB = {
    "Youssouf": {"figure": FIGURES[0], "element": "Feu", "psaume": "Psaume 109", "verset": "Genèse 39:2", "priere": "Seigneur, Dieu de Joseph, par Ton Nom Adonaï, dissipe les ténèbres de la calomnie.", "nassi": "111 fois, eau de puits, safran, rose. Bain 7j", "plantes": "Laurier, Cannelle", "huiles": "Encens, Clou de girofle, Orange", "cloture": "Psaume 117", "sadaka": "Pain, dattes"},
    "Adama": {"figure": FIGURES[1], "element": "Feu", "psaume": "Psaume 121", "verset": "Genèse 2:7", "priere": "Par le Nom Elohim, j'invoque l'ancrage de mes racines.", "nassi": "45 fois, eau + gros sel. Aspersion seuil", "plantes": "Gingembre, Laurier", "huiles": "Orange douce, Clou de girofle, Encens", "cloture": "Psaume 128", "sadaka": "Denrées rouges"},
    "Mahdy": {"figure": FIGURES[2], "element": "Air", "psaume": "Psaume 23", "verset": "Jérémie 29:11", "priere": "Par le Nom El-Shaddaï, débouche les canaux de l'abondance.", "nassi": "66 fois, eau de rose + musc. Boire à jeun", "plantes": "Menthe, Sauge", "huiles": "Citron, Menthe poivrée, Bergamote", "cloture": "Psaume 150", "sadaka": "Sucre et lait"},
    "Idriss": {"figure": FIGURES[3], "element": "Eau", "psaume": "Psaume 119:9-16", "verset": "Hébreux 11:5", "priere": "Par le Nom El-Choura, accorde-moi le discernement.", "nassi": "360 fois, eau de pluie. Oindre la tête", "plantes": "Aloès, Verveine", "huiles": "Lavande, Camomille, Ylang-Ylang", "cloture": "Psaume 23", "sadaka": "Eau pure"},
    "Ibrahima": {"figure": FIGURES[4], "element": "Eau", "psaume": "Psaume 112", "verset": "Genèse 12:2", "priere": "Par le Nom El-Elyon, je scelle la protection de ma lignée.", "nassi": "72 fois, menthe fraîche. Asperger la chambre", "plantes": "Verveine, Neem", "huiles": "Camomille, Lavande, Ylang-Ylang", "cloture": "Psaume 112", "sadaka": "Lait"},
    "Inssa": {"figure": FIGURES[5], "element": "Eau", "psaume": "Psaume 6", "verset": "Ésaïe 53:5", "priere": "Par le Nom Rapha, efface la maladie et restaure la vigueur.", "nassi": "99 fois, feuilles de neem. Bain rituel", "plantes": "Neem, Aloès", "huiles": "Ylang-Ylang, Lavande, Camomille", "cloture": "Psaume 6", "sadaka": "Aumône"},
    "Omar": {"figure": FIGURES[6], "element": "Air", "psaume": "Psaume 35", "verset": "Proverbes 31:10", "priere": "Par le Nom Shalom, neutralise les intrigues et discordes.", "nassi": "28 fois, parfum sans alcool. Aspersion", "plantes": "Sauge, Menthe", "huiles": "Menthe poivrée, Citron, Bergamote", "cloture": "Psaume 35", "sadaka": "Sucre"},
    "Ayoub": {"figure": FIGURES[7], "element": "Terre", "psaume": "Psaume 88", "verset": "Job 19:25", "priere": "Par le Nom Yahvé, demande la restauration après la ruine.", "nassi": "88 fois, miel. Bain samedi soir", "plantes": "Santal, Patchouli", "huiles": "Vétiver, Santal, Cèdre", "cloture": "Psaume 88", "sadaka": "Céréales"},
    "Allahou": {"figure": FIGURES[8], "element": "Feu", "psaume": "Psaume 91", "verset": "Exode 20:2", "priere": "Par le Nom El-Qahhar, sois ma Forteresse, annule tout sortilège.", "nassi": "114 fois, eau de puits. Purifier commerce", "plantes": "Laurier, Gingembre", "huiles": "Clou de girofle, Encens, Orange", "cloture": "Psaume 91", "sadaka": "Pain"},
    "Souleymane": {"figure": FIGURES[9], "element": "Terre", "psaume": "Psaume 72", "verset": "1 Rois 3:12", "priere": "Par le Nom Malek, accorde-moi l'autorité et la justice.", "nassi": "110 fois, eau de santal. Oindre les mains", "plantes": "Patchouli, Santal", "huiles": "Santal, Vétiver, Cèdre", "cloture": "Psaume 72", "sadaka": "Pièces"},
    "Aliou": {"figure": FIGURES[10], "element": "Air", "psaume": "Psaume 144", "verset": "Éphésiens 6:11", "priere": "Par le Nom Tsébaot, sois mon bouclier contre les agressions.", "nassi": "63 fois, camphre. Laver le mardi", "plantes": "Eucalyptus, Menthe", "huiles": "Bergamote, Menthe poivrée, Citron", "cloture": "Psaume 144", "sadaka": "Eau sucrée"},
    "Nouhou": {"figure": FIGURES[11], "element": "Terre", "psaume": "Psaume 29", "verset": "Genèse 6:8", "priere": "Par le Nom El-Hafiz, préserve-moi de la tempête.", "nassi": "77 fois, eau de mer. Laver le sol", "plantes": "Cèdre, Santal", "huiles": "Cèdre, Santal, Vétiver", "cloture": "Psaume 29", "sadaka": "Céréales"},
    "Assane": {"figure": FIGURES[12], "element": "Eau", "psaume": "Psaume 3", "verset": "Psaume 3:3", "priere": "Par le Nom El-Adl, transmute la honte en honneur.", "nassi": "55 fois, laurier. Bain 3 jours", "plantes": "Neem, Aloès", "huiles": "Lavande, Camomille, Ylang-Ylang", "cloture": "Psaume 3", "sadaka": "Lait"},
    "Younouss": {"figure": FIGURES[13], "element": "Terre", "psaume": "Psaume 4", "verset": "Jonas 2:10", "priere": "Par le Nom El-Latif, libère-moi des chaînes de la dette.", "nassi": "40 fois, pièce argent. Friction des mains", "plantes": "Santal, Patchouli", "huiles": "Vétiver, Santal, Cèdre", "cloture": "Psaume 4", "sadaka": "Pièces"},
    "Ousmane": {"figure": FIGURES[14], "element": "Air", "psaume": "Psaume 119:105", "verset": "Actes 2:4", "priere": "Par le Nom El-Rouah, guide mes pas dans la haute guidance.", "nassi": "19 fois, encens Oliban. Boire avant consultation", "plantes": "Sauge, Menthe", "huiles": "Citron, Menthe poivrée, Bergamote", "cloture": "Psaume 119", "sadaka": "Sucre"},
    "Moussa": {"figure": FIGURES[15], "element": "Feu", "psaume": "Psaume 68", "verset": "Exode 14:13", "priere": "Par le Nom El-Fattah, ouvre les chemins du succès.", "nassi": "16 fois, eau aube. Nettoyer seuil", "plantes": "Cannelle, Laurier", "huiles": "Encens, Clou de girofle, Orange", "cloture": "Psaume 68", "sadaka": "Dattes"}
}

INV_OUVERTURE = "Toi seul, ô Dieu de Salomon, règnes sur ce qui est visible et sur ce qui ne l'est pas. Je me présente devant Toi, non comme un étranger, mais comme un héritier de Ton Alliance."
ANA_BEKOACH = "Ana bekoach, par la force de Ta main droite, délie les liens. Accueille le chant de Ton peuple, purifie-nous, Toi qui es Redoutable. Bénis-les, purifie-les, accorde-leur Ta justice. Puissant et Saint, conduis Ton assemblée. Reçois notre supplique, Toi qui connais les secrets."
INV_FERMETURE = "Lève-Toi, Seigneur Dieu, pour aller à Ton lieu de repos. Que Tes serviteurs soient revêtus du salut. Que cette prière soit scellée."

# Interface
st.set_page_config(page_title="Oracle Ramrou", layout="wide")
st.title("🔮 Oracle Ramrou — Cabinet de Haute Théurgie")

theme = {m: st.sidebar.selectbox(f"Maison M{m}", list(DB.keys()), key=f"m{m}") for m in range(1, 17)}

if st.button("🔮 GÉNÉRER L'ORDONNANCE"):
    juge = theme[16]
    d = DB[juge]
    st.subheader(f"⚖️ Verdict du Juge : {juge} ({d['figure']})")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"**📖 Psaume :** {d['psaume']}")
        st.markdown(f"**📜 Verset Biblique :** {d['verset']}")
        st.markdown(f"**🙏 Prière :** {d['priere']}")
        st.info(f"**🧪 Protocole Nassi :** {d['nassi']}")
    with c2:
        st.success(f"**🌿 Plantes :** {d['plantes']}")
        st.success(f"**💧 Huiles :** {d['huiles']}")
        st.error(f"**⚡ Clôture :** {d['cloture']} | **🪙 Sadaka :** {d['sadaka']}")
    
    st.divider()
    st.text_area("🗝️ Activation (Ana Bekoach)", ANA_BEKOACH, height=100)
    
    export = f"ORDONNANCE\n\nJuge: {juge} ({d['figure']})\nVerset: {d['verset']}\nNassi: {d['nassi']}\nPlantes: {d['plantes']}\nHuiles: {d['huiles']}\n\n{INV_FERMETURE}"
    st.download_button("📥 Télécharger", data=export, file_name=f"Ordonnance_{juge}.txt")
