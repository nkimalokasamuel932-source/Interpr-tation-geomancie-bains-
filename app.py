import streamlit as st

# ==============================================================================
# BASE DE DONNÉES MAÎTRE
# ==============================================================================
DB = {
    "Youssouf": {"element": "Feu (Est)", "psaume": "Psaume 109", "verset": "Genèse 39:2", "priere": "Seigneur, Dieu de Joseph, par Ton Nom Adonaï, dissipe les ténèbres de la calomnie.", "nassi": "111 fois, eau de puits, safran, rose. Bain 7j", "plantes": "Laurier, Cannelle", "huiles": "Encens (Oliban), Clou de girofle", "heure": "Mardi, Aube", "support": "Parchemin, Encre Safran", "couleur": "Rouge", "cloture": "Psaume 117", "sadaka": "Pain, dattes"},
    "Adama": {"element": "Feu (Est)", "psaume": "Psaume 121", "verset": "Genèse 2:7", "priere": "Par le Nom Elohim, j'invoque l'ancrage de mes racines.", "nassi": "45 fois, eau + gros sel. Aspersion seuil", "plantes": "Gingembre, Laurier", "huiles": "Orange douce, Encens", "heure": "Samedi, Soir", "support": "Ardoise, Craie blanche", "couleur": "Vert/Noir", "cloture": "Psaume 128", "sadaka": "Denrées rouges"},
    "Mahdy": {"element": "Air (Ouest)", "psaume": "Psaume 23", "verset": "Jérémie 29:11", "priere": "Par le Nom El-Shaddaï, débouche les canaux de l'abondance.", "nassi": "66 fois, eau de rose + musc. Boire à jeun", "plantes": "Menthe, Sauge", "huiles": "Citron, Bergamote", "heure": "Mercredi, Midi", "support": "Papier blanc, Encre noire", "couleur": "Jaune", "cloture": "Psaume 150", "sadaka": "Sucre et lait"},
    "Idriss": {"element": "Eau (Nord)", "psaume": "Psaume 119:9-16", "verset": "Hébreux 11:5", "priere": "Par le Nom El-Choura, accorde-moi le discernement.", "nassi": "360 fois, eau de pluie. Oindre la tête", "plantes": "Aloès, Verveine", "huiles": "Lavande, Camomille", "heure": "Lundi, Aube", "support": "Feuille d'arbre, Encre bleue", "couleur": "Bleu", "cloture": "Psaume 23", "sadaka": "Eau pure"},
    "Ibrahima": {"element": "Eau (Nord)", "psaume": "Psaume 112", "verset": "Genèse 12:2", "priere": "Par le Nom El-Elyon, je scelle la protection de ma lignée.", "nassi": "72 fois, menthe fraîche. Asperger la chambre", "plantes": "Verveine, Neem", "huiles": "Camomille, Ylang-Ylang", "heure": "Jeudi, Aube", "support": "Papier, Encre Noire", "couleur": "Blanc", "cloture": "Psaume 112", "sadaka": "Lait"},
    "Inssa": {"element": "Eau (Nord)", "psaume": "Psaume 6", "verset": "Ésaïe 53:5", "priere": "Par le Nom Rapha, efface la maladie et restaure la vigueur.", "nassi": "99 fois, feuilles de neem. Bain rituel", "plantes": "Neem, Aloès", "huiles": "Ylang-Ylang, Lavande", "heure": "Lundi, Nuit", "support": "Ardoise", "couleur": "Bleu pâle", "cloture": "Psaume 6", "sadaka": "Aumône"},
    "Omar": {"element": "Air (Ouest)", "psaume": "Psaume 35", "verset": "Proverbes 31:10", "priere": "Par le Nom Shalom, neutralise les intrigues et discordes.", "nassi": "28 fois, parfum sans alcool. Aspersion", "plantes": "Sauge, Menthe", "huiles": "Menthe poivrée, Citron", "heure": "Mercredi, Coucher", "support": "Parchemin", "couleur": "Gris", "cloture": "Psaume 35", "sadaka": "Sucre"},
    "Ayoub": {"element": "Terre (Sud)", "psaume": "Psaume 88", "verset": "Job 19:25", "priere": "Par le Nom Yahvé, demande la restauration après la ruine.", "nassi": "88 fois, miel. Bain samedi soir", "plantes": "Santal, Patchouli", "huiles": "Vétiver, Santal", "heure": "Samedi, Nuit", "support": "Terre cuite", "couleur": "Marron", "cloture": "Psaume 88", "sadaka": "Céréales"},
    "Allahou": {"element": "Feu (Est)", "psaume": "Psaume 91", "verset": "Exode 20:2", "priere": "Par le Nom El-Qahhar, sois ma Forteresse, annule tout sortilège.", "nassi": "114 fois, eau de puits. Purifier commerce", "plantes": "Laurier, Gingembre", "huiles": "Encens, Clou de girofle", "heure": "Mardi, Midi", "support": "Papier, Encre Safran", "couleur": "Rouge vif", "cloture": "Psaume 91", "sadaka": "Pain"},
    "Souleymane": {"element": "Terre (Sud)", "psaume": "Psaume 72", "verset": "1 Rois 3:12", "priere": "Par le Nom Malek, accorde-moi l'autorité et la justice.", "nassi": "110 fois, eau de santal. Oindre les mains", "plantes": "Patchouli, Cèdre", "huiles": "Santal, Vétiver", "heure": "Samedi, Aube", "support": "Parchemin", "couleur": "Or", "cloture": "Psaume 72", "sadaka": "Pièces"},
    "Aliou": {"element": "Air (Ouest)", "psaume": "Psaume 144", "verset": "Éphésiens 6:11", "priere": "Par le Nom Tsébaot, sois mon bouclier contre les agressions.", "nassi": "63 fois, camphre. Laver le mardi", "plantes": "Eucalyptus, Menthe", "huiles": "Bergamote, Menthe", "heure": "Mercredi, Aube", "support": "Papier blanc", "couleur": "Violet", "cloture": "Psaume 144", "sadaka": "Eau sucrée"},
    "Nouhou": {"element": "Terre (Sud)", "psaume": "Psaume 29", "verset": "Genèse 6:8", "priere": "Par le Nom El-Hafiz, préserve-moi de la tempête.", "nassi": "77 fois, eau de mer. Laver le sol", "plantes": "Cèdre, Santal", "huiles": "Cèdre, Vétiver", "heure": "Samedi, Minuit", "support": "Ardoise", "couleur": "Noir", "cloture": "Psaume 29", "sadaka": "Céréales"},
    "Assane": {"element": "Eau (Nord)", "psaume": "Psaume 3", "verset": "Psaume 3:3", "priere": "Par le Nom El-Adl, transmute la honte en honneur.", "nassi": "55 fois, laurier. Bain 3 jours", "plantes": "Neem, Aloès", "huiles": "Lavande, Camomille", "heure": "Lundi, Midi", "support": "Papier, Encre Safran", "couleur": "Bleu", "cloture": "Psaume 3", "sadaka": "Lait"},
    "Younouss": {"element": "Terre (Sud)", "psaume": "Psaume 4", "verset": "Jonas 2:10", "priere": "Par le Nom El-Latif, libère-moi des chaînes de la dette.", "nassi": "40 fois, pièce argent. Friction des mains", "plantes": "Santal, Cèdre", "huiles": "Vétiver, Santal", "heure": "Samedi, Aube", "support": "Parchemin", "couleur": "Vert", "cloture": "Psaume 4", "sadaka": "Pièces"},
    "Ousmane": {"element": "Air (Ouest)", "psaume": "Psaume 119:105", "verset": "Actes 2:4", "priere": "Par le Nom El-Rouah, guide mes pas dans la haute guidance.", "nassi": "19 fois, encens Oliban. Boire avant consultation", "plantes": "Sauge, Menthe", "huiles": "Citron, Bergamote", "heure": "Mercredi, Nuit", "support": "Feuille", "couleur": "Bleu ciel", "cloture": "Psaume 119", "sadaka": "Sucre"},
    "Moussa": {"element": "Feu (Est)", "psaume": "Psaume 68", "verset": "Exode 14:13", "priere": "Par le Nom El-Fattah, ouvre les chemins du succès.", "nassi": "16 fois, eau aube. Nettoyer seuil", "plantes": "Cannelle, Laurier", "huiles": "Encens, Orange", "heure": "Mardi, Midi", "support": "Papier, Encre Safran", "couleur": "Rouge", "cloture": "Psaume 68", "sadaka": "Dattes"}
}

# Invocations
INV_OUVERTURE = "Toi seul, ô Dieu de Salomon, règnes sur ce qui est visible et sur ce qui ne l'est pas. Je me présente devant Toi, non comme un étranger, mais comme un héritier de Ton Alliance."
ANA_BEKOACH = """Ana bekoach, Je t'en prie, par la force de la grandeur de Ta main droite, délie les nœuds (les liens).
Accueille le chant de Ton peuple, élève-nous, purifie-nous, Toi qui es Redoutable.Je T'en prie, Héros, ceux qui cherchent Ton unicité, garde-les comme la prunelle de Tes yeux.
Bénis-les, purifie-les, accorde-leur toujours Ta miséricorde et Ta justice.Puissant et Saint, par Ta grande bonté, conduis Ton assemblée.
Unique et Majestueux, tourne-Toi vers Ton peuple, ceux qui se souviennent de Ta sainteté.
Reçois notre supplique et entends notre cri, Toi qui connais les secrets."""
INV_FERMETURE = "Lève-Toi, Seigneur Dieu, pour aller à Ton lieu de repos. Que Tes serviteurs soient revêtus du salut. Que cette prière soit scellée."

# Interface
st.set_page_config(page_title="Oracle Ramrou", layout="wide")
st.title("🔮 Oracle Ramrou — Cabinet de Haute Théurgie")
st.markdown(f"> *{INV_OUVERTURE}*")
st.divider()

st.sidebar.header("📋 Configuration du Thème")
question = st.sidebar.text_area("Question posée :")
intention = st.sidebar.selectbox("Intention :", ["Déblocage", "Protection", "Attraction", "Apaisement"])
theme = {m: st.sidebar.selectbox(f"Maison M{m}", list(DB.keys()), key=f"m{m}") for m in range(1, 17)}

if st.button("🔮 GÉNÉRER L'ORDONNANCE DE RÉSOLUTION"):
    juge = theme[16]
    d = DB[juge]
    st.subheader(f"⚖️ Verdict du Juge : {juge}")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"**📖 Psaume :** {d['psaume']}\n**🙏 Prière :** {d['priere']}")
        st.info(f"**🧪 Nassi :** {d['nassi']}")
        st.warning(f"**🔑 Clé Ana Bekoach :** {ANA_BEKOACH}")
    with c2:
        st.success(f"**🌿 Supports :** {d['plantes']}, {d['huiles']}")
        st.write(f"**⏰ Heure :** {d['heure']} | **🎨 Couleur :** {d['couleur']}")
        st.error(f"**⚡ Clôture :** {d['cloture']} | **🪙 Sadaka :** {d['sadaka']}")
    
    export = f"ORACLE RAMROU - ORDONNANCE\n\n{INV_OUVERTURE}\n\nANA BEKOACH: {ANA_BEKOACH}\n\nVERDICT M16: {juge}\n{d}\n\n{INV_FERMETURE}"
    st.download_button("📥 Télécharger l'Ordonnance", data=export, file_name=f"Ordonnance_{juge}.txt")
