import streamlit as st
# ==============================================================================
# 1. BASES DE DONNÉES
# ==============================================================================
PROPRIETES_FIGURES = 
    "Youssouf": {"element": "Feu (Est)", "psaume": "Psaume 109", "verset": "Genèse 39:2", "priere": "Seigneur, Dieu de Joseph, par Ton Nom Adonaï, je Te supplie de dissiper les ténèbres de la calomnie. Comme Tu as transformé la captivité de Joseph en gloire, transforme cette situation présente. Que tout complot contre moi s'effondre et que Ta lumière restaure mon honneur.", "nassi": "111 fois, eau de puits + safran + rose. Bain 7 jours."},
    "Adama": {"element": "Feu (Est)", "psaume": "Psaume 121", "verset": "Genèse 2:7", "priere": "Par le Nom Elohim, Créateur du premier homme, j'invoque l'ancrage de mes racines dans la terre fertile de la bénédiction. Que les portes de mes biens soient ouvertes.", "nassi": "Tracer 45 fois, eau + gros sel béni. Aspersion du corps et du seuil."},
    "Mahdy": {"element": "Air (Ouest)", "psaume": "Psaume 23", "verset": "Jérémie 29:11", "priere": "Par le Nom El-Shaddaï, Source de toute subsistance, je demande que les canaux de l'abondance soient débouchés. Que Ta faveur attire les ressources nécessaires.", "nassi": "Écrire 66 fois, eau de rose + musc. Boire à jeun."},
    "Idriss": {"element": "Eau (Nord)", "psaume": "Psaume 119:9-16", "verset": "Hébreux 11:5", "priere": "Par le Nom El-Choura, Dieu de Sagesse, je sollicite l'illumination. Accorde-moi le discernement pour lire à travers les mystères.", "nassi": "Écrire 360 fois, eau de pluie. Oindre la tête avant étude."},
    "Ibrahima": {"element": "Eau (Nord)", "psaume": "Psaume 112", "verset": "Genèse 12:2", "priere": "Par le Nom El-Elyon, Dieu de l'Alliance, je scelle la protection de ma lignée. Que Ta bénédiction s'étende sur ma maison.", "nassi": "Écrire 72 fois, menthe fraîche. Boire ou asperger la chambre."},
    "Inssa": {"element": "Eau (Nord)", "psaume": "Psaume 6", "verset": "Ésaïe 53:5", "priere": "Par le Nom Rapha, Dieu qui guérit, je demande la délivrance de toute affliction. Que Ta main curative efface la maladie.", "nassi": "Écrire 99 fois, décoction de neem. Laver le corps."},
    "Omar": {"element": "Air (Ouest)", "psaume": "Psaume 35", "verset": "Proverbes 31:10", "priere": "Par le Nom Shalom, Dieu de Paix, j'invoque l'harmonie. Que les discordes soient neutralisées et les intrigues dissoutes.", "nassi": "Tracer 28 fois, eau + 7 gouttes parfum sans alcool. Aspersion maison."},
    "Ayoub": {"element": "Terre (Sud)", "psaume": "Psaume 88", "verset": "Job 19:25", "priere": "Par le Nom Yahvé, Rédempteur des affligés, je demande la restauration. Que la patience soit ma force face à la ruine.", "nassi": "Écrire 88 fois, eau tiède + miel. Laver le samedi soir."},
    "Allahou": {"element": "Feu (Est)", "psaume": "Psaume 91", "verset": "Exode 20:2", "priere": "Par le Nom El-Qahhar, Dieu Souverain, je Te demande d'être ma Forteresse. Que chaque sortilège soit annulé.", "nassi": "Écrire 114 fois, eau de puits. Boire le vendredi, purifier commerce."},
    "Souleymane": {"element": "Terre (Sud)", "psaume": "Psaume 72", "verset": "1 Rois 3:12", "priere": "Par le Nom Malek, Roi des Rois, je demande l'accès à la sagesse de Salomon. Accorde-moi l'autorité pour diriger avec justice.", "nassi": "Écrire 110 fois, santal. Oindre mains et visage."},
    "Aliou": {"element": "Air (Ouest)", "psaume": "Psaume 144", "verset": "Éphésiens 6:11", "priere": "Par le Nom Tsébaot, Dieu des Armées, je revêts Ton Armure. Sois mon bouclier contre toute agression.", "nassi": "Écrire 63 fois, eau + camphre. Laver le mardi."},
    "Nouhou": {"element": "Terre (Sud)", "psaume": "Psaume 29", "verset": "Genèse 6:8", "priere": "Par le Nom El-Hafiz, Dieu Protecteur, je demande à être préservé au milieu de la tempête.", "nassi": "Écrire 77 fois, eau de mer ou sel. Laver le sol."},
    "Assane": {"element": "Eau (Nord)", "psaume": "Psaume 3", "verset": "Psaume 3:3", "priere": "Par le Nom El-Adl, Dieu de Justice, je demande le retournement de mon sort. Que la honte soit transmutée en honneur.", "nassi": "Écrire 55 fois, laurier. Bain 3 jours consécutifs."},
    "Younouss": {"element": "Terre (Sud)", "psaume": "Psaume 4", "verset": "Jonas 2:10", "priere": "Par le Nom El-Latif, Dieu de Douceur, libère-moi des chaînes de la dette.", "nassi": "Écrire 40 fois, pièce d'argent trempée. Friction sur les mains."},
    "Ousmane": {"element": "Air (Ouest)", "psaume": "Psaume 119:105", "verset": "Actes 2:4", "priere": "Par le Nom El-Rouah, Esprit de Vérité, j'ouvre mon canal. Guide mes pas dans la lumière prophétique.", "nassi": "Écrire 19 fois, encens Oliban. Boire avant consultation."},
    "Moussa": {"element": "Feu (Est)", "psaume": "Psaume 68", "verset": "Exode 14:13", "priere": "Par le Nom El-Fattah, Celui qui ouvre, demande le passage. Ouvre devant moi les chemins du succès.", "nassi": "Écrire 16 fois, eau de l'aube. Nettoyer le seuil ou grand bain."}
}
PROPRIETES_FIGURES = 
    "Youssouf": {
        "psaume": "Psaume 109",
        "verset": "Genèse 39:2",
        "priere": "Seigneur, Dieu de Joseph, par Ton Nom Adonaï, dissipe les ténèbres de la calomnie. Comme Tu as transformé la captivité de Joseph en gloire, restaure mon honneur.",
        "nassi": "Écrire 111 fois, laver avec eau de puits, safran et parfum de rose. Bain 7 jours."
    },
    "Adama": {
        "psaume": "Psaume 121",
        "verset": "Genèse 2:7",
        "priere": "Par le Nom Elohim, j'invoque l'ancrage de mes racines dans la terre fertile. Que mes biens soient protégés et multipliés.",
        "nassi": "Tracer 45 fois sur ardoise. Eau + gros sel béni. Aspersion du corps et du seuil."
    },
    "Mahdy": {
        "psaume": "Psaume 23",
        "verset": "Jérémie 29:11",
        "priere": "Par le Nom El-Shaddaï, Source de toute subsistance, débouche les canaux de l'abondance. Que Ta faveur attire les ressources.",
        "nassi": "Écrire 66 fois avec eau de rose et musc. Boire chaque matin à jeun."
    },
    "Idriss": {
        "psaume": "Psaume 119:9-16",
        "verset": "Hébreux 11:5",
        "priere": "Par le Nom El-Choura, Dieu de Sagesse, accorde-moi le discernement pour lire à travers les mystères.",
        "nassi": "Écrire 360 fois. Diluer dans eau de pluie. Oindre la tête avant étude."
    },
    "Ibrahima": {
        "psaume": "Psaume 112",
        "verset": "Genèse 12:2",
        "priere": "Par le Nom El-Elyon, je scelle la protection de ma lignée. Que Ta bénédiction s'étende sur ma maison.",
        "nassi": "Écrire 72 fois. Infuser avec menthe fraîche. Boire ou asperger la chambre."
    },
    "Inssa": {
        "psaume": "Psaume 6",
        "verset": "Ésaïe 53:5",
        "priere": "Par le Nom Rapha, Dieu qui guérit, efface la maladie et restaure la vigueur de mon esprit.",
        "nassi": "Écrire 99 fois à l'encre Sami. Laver avec décoction de feuilles de neem."
    },
    "Omar": {
        "psaume": "Psaume 35",
        "verset": "Proverbes 31:10",
        "priere": "Par le Nom Shalom, j'invoque l'harmonie. Que les discordes soient neutralisées et les intrigues dissoutes.",
        "nassi": "Tracer 28 fois. Eau de source + 7 gouttes de parfum sans alcool. Aspersion maison."
    },
    "Ayoub": {
        "psaume": "Psaume 88",
        "verset": "Job 19:25",
        "priere": "Par le Nom Yahvé, demande la restauration. Que la patience soit ma force face à la ruine.",
        "nassi": "Écrire 88 fois. Dissoudre dans eau tiède et miel. Se laver un samedi soir."
    },
    "Allahou": {
        "psaume": "Psaume 91",
        "verset": "Exode 20:2",
        "priere": "Par le Nom El-Qahhar, sois ma Forteresse. Que chaque sortilège soit annulé par Ta Protection.",
        "nassi": "Écrire 114 fois. Eau de puits. Boire le vendredi, purifier le commerce."
    },
    "Souleymane": {
        "psaume": "Psaume 72",
        "verset": "1 Rois 3:12",
        "priere": "Par le Nom Malek, Roi des Rois, accorde-moi l'autorité pour diriger mes affaires avec justice.",
        "nassi": "Écrire 110 fois. Eau infusée au santal. Oindre mains et visage avant affaires."
    },
    "Aliou": {
        "psaume": "Psaume 144",
        "verset": "Éphésiens 6:11",
        "priere": "Par le Nom Tsébaot, revêts-moi de Ton Armure. Sois mon bouclier contre toute agression.",
        "nassi": "Écrire 63 fois. Eau + camphre. Se laver un mardi."
    },
    "Nouhou": {
        "psaume": "Psaume 29",
        "verset": "Genèse 6:8",
        "priere": "Par le Nom El-Hafiz, demande à être préservé au milieu de la tempête. Que Ta Grâce soit mon arche.",
        "nassi": "Écrire 77 fois. Eau de mer ou sel marin. Laver le sol de la concession."
    },
    "Assane": {
        "psaume": "Psaume 3",
        "verset": "Psaume 3:3",
        "priere": "Par le Nom El-Adl, demande le retournement de mon sort. Que la honte soit transmutée en honneur.",
        "nassi": "Écrire 55 fois (encre safranée). Eau + laurier. Bain 3 jours."
    },
    "Younouss": {
        "psaume": "Psaume 4",
        "verset": "Jonas 2:10",
        "priere": "Par le Nom El-Latif, libère-moi des chaînes de la dette. Fais sortir mes finances de toute impasse.",
        "nassi": "Écrire 40 fois. Eau + pièce d'argent trempée. Friction sur les mains."
    },
    "Ousmane": {
        "psaume": "Psaume 119:105",
        "verset": "Actes 2:4",
        "priere": "Par le Nom El-Rouah, Esprit de Vérité, guide mes pas dans la lumière de la haute guidance.",
        "nassi": "Écrire 19 fois. Infuser avec encens Oliban. Boire avant consultation."
    },
    "Moussa": {
        "psaume": "Psaume 68",
        "verset": "Exode 14:13",
        "priere": "Par le Nom El-Fattah, demande le passage. Ouvre devant moi les chemins du succès.",
        "nassi": "Écrire 16 fois. Eau de source de l'aube. Nettoyer le seuil ou grand bain."
    }
CORRESPONDANCES = {
    "Feu (Est)": {"plantes": "Laurier, Cannelle, Gingembre", "huiles": "Encens (Oliban), Clou de girofle, Orange"},
    "Eau (Nord)": {"plantes": "Neem, Verveine, Aloès", "huiles": "Lavande, Camomille, Ylang-Ylang"},
    "Air (Ouest)": {"plantes": "Menthe, Sauge, Eucalyptus", "huiles": "Menthe poivrée, Citron, Bergamote"},
    "Terre (Sud)": {"plantes": "Santal, Patchouli, Cèdre", "huiles": "Santal, Vétiver, Cèdre"}
}

# ==============================================================================
# 2. INTERFACE ET LOGIQUE
# ==============================================================================
st.set_page_config(page_title="Oracle Ramrou", layout="wide")
st.title("🔮 Oracle Ramrou — Cabinet de Haute Théurgie")

st.sidebar.header("📥 Saisie du Thème")
theme = {m: st.sidebar.selectbox(f"Maison {m}", list(PROPRIETES_FIGURES.keys()), key=f"m_{m}") for m in range(1, 17)}

if st.button("🔮 ANALYSER LE JUGEMENT (M16)"):
    juge = theme[16]
    data = PROPRIETES_FIGURES[juge]
    corr = CORRESPONDANCES[data['element']]
    
    st.subheader(f"⚖️ Verdict du Juge : {juge} ({data['element']})")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**Psaume :** {data['psaume']}")
        st.markdown(f"**Verset (Nassi) :** {data['verset']}")
        st.warning(f"**Prière Salomonique :**\n\n> *{data['priere']}*")
    
    with col2:
        st.info(f"**Protocole Nassi :** {data['nassi']}")
        st.success(f"**Supports Végétaux :**\n- Plantes : {corr['plantes']}\n- Huiles : {corr['huiles']}")
        
    st.divider()
    st.markdown(f"**Conseil Sadaka :** Donnez à un nécessiteux selon l'élément :")
    if "Feu" in data['element']: st.write("• Mardi (Denrées chaudes, pain, dattes)")
    elif "Terre" in data['element']: st.write("• Samedi (Pièces de monnaie, céréales)")
    else: st.write("• Lundi/Jeudi (Eau, sucre, lait)")
