import streamlit as st

# ==============================================================================
# 1. BASE DE DONNÉES DES FIGURES ET PROTOCOLES (DB)
# ==============================================================================
FIGURES = [
    "Via", "Populus", "Conjunctio", "Carcer", "Fortuna Major", "Fortuna Minor", 
    "Acquisitio", "Amissio", "Laetitia", "Tristitia", "Puella", "Puer", 
    "Albus", "Rubeus", "Caput Draconis", "Cauda Draconis"
]

DB = {
    "Djanvalimam": {"figure": FIGURES[0], "psaume": "Psaume 109", "verset": "Genèse 39:2", "priere": "Par le Nom Adonaï, dissipe les ténèbres.", "nassi": "111 fois, eau de puits", "plantes": "Laurier", "huiles": "Encens", "cloture": "Psaume 117", "sadaka": "Pain, dattes"},
    "Adama": {"figure": FIGURES[1], "psaume": "Psaume 121", "verset": "Genèse 2:7", "priere": "Par le Nom Elohim, ancre mes racines.", "nassi": "45 fois, eau + sel", "plantes": "Gingembre", "huiles": "Orange", "cloture": "Psaume 128", "sadaka": "Denrées rouges"},
    "Malidjou": {"figure": FIGURES[2], "psaume": "Psaume 23", "verset": "Jérémie 29:11", "priere": "Par le Nom El-Shaddaï, ouvre l'abondance.", "nassi": "66 fois, eau de rose", "plantes": "Menthe", "huiles": "Citron", "cloture": "Psaume 150", "sadaka": "Sucre et lait"},
    "Bayadou": {"figure": FIGURES[3], "psaume": "Psaume 119", "verset": "Hébreux 11:5", "priere": "Par le Nom El-Choura, accorde discernement.", "nassi": "360 fois, eau de pluie", "plantes": "Aloès", "huiles": "Lavande", "cloture": "Psaume 23", "sadaka": "Eau pure"},
    "Tariqi": {"figure": FIGURES[4], "psaume": "Psaume 112", "verset": "Genèse 12:2", "priere": "Par le Nom El-Elyon, protège ma lignée.", "nassi": "72 fois, menthe fraîche", "plantes": "Verveine", "huiles": "Camomille", "cloture": "Psaume 112", "sadaka": "Lait"},
    "Issa": {"figure": FIGURES[5], "psaume": "Psaume 6", "verset": "Ésaïe 53:5", "priere": "Par le Nom Rapha, restaure ma vigueur.", "nassi": "99 fois, feuilles de neem", "plantes": "Neem", "huiles": "Ylang-Ylang", "cloture": "Psaume 6", "sadaka": "Aumône"},
    "Lomara": {"figure": FIGURES[6], "psaume": "Psaume 35", "verset": "Proverbes 31:10", "priere": "Par le Nom Shalom, neutralise les intrigues.", "nassi": "28 fois, parfum sans alcool", "plantes": "Sauge", "huiles": "Menthe", "cloture": "Psaume 35", "sadaka": "Sucre"},
    "Mangoussi": {"figure": FIGURES[7], "psaume": "Psaume 88", "verset": "Job 19:25", "priere": "Par le Nom Yahvé, demande restauration.", "nassi": "88 fois, miel", "plantes": "Santal", "huiles": "Vétiver", "cloture": "Psaume 88", "sadaka": "Céréales"},
    "Kalalaho": {"figure": FIGURES[8], "psaume": "Psaume 91", "verset": "Exode 20:2", "priere": "Par le Nom El-Qahhar, sois ma Forteresse.", "nassi": "114 fois, eau de puits", "plantes": "Laurier", "huiles": "Clou de girofle", "cloture": "Psaume 91", "sadaka": "Pain"},
    "Massa Souleymane": {"figure": FIGURES[9], "psaume": "Psaume 72", "verset": "1 Rois 3:12", "priere": "Par le Nom Malek, accorde-moi la justice.", "nassi": "110 fois, eau de santal", "plantes": "Patchouli", "huiles": "Santal", "cloture": "Psaume 72", "sadaka": "Pièces"},
    "Badra Ali": {"figure": FIGURES[10], "psaume": "Psaume 144", "verset": "Éphésiens 6:11", "priere": "Par le Nom Tsébaot, sois mon bouclier.", "nassi": "63 fois, camphre", "plantes": "Eucalyptus", "huiles": "Bergamote", "cloture": "Psaume 144", "sadaka": "Eau sucrée"},
    "Noukoro": {"figure": FIGURES[11], "psaume": "Psaume 29", "verset": "Genèse 6:8", "priere": "Par le Nom El-Hafiz, préserve-moi.", "nassi": "77 fois, eau de mer", "plantes": "Cèdre", "huiles": "Cèdre", "cloture": "Psaume 29", "sadaka": "Céréales"},
    "Lacina": {"figure": FIGURES[12], "psaume": "Psaume 3", "verset": "Psaume 3:3", "priere": "Par le Nom El-Adl, transmute la honte.", "nassi": "55 fois, laurier", "plantes": "Neem", "huiles": "Lavande", "cloture": "Psaume 3", "sadaka": "Lait"},
    "Totiqi": {"figure": FIGURES[13], "psaume": "Psaume 4", "verset": "Jonas 2:10", "priere": "Par le Nom El-Latif, libère des chaînes.", "nassi": "40 fois, pièce argent", "plantes": "Santal", "huiles": "Vétiver", "cloture": "Psaume 4", "sadaka": "Pièces"},
    "Mori Zoumana": {"figure": FIGURES[14], "psaume": "Psaume 119:105", "verset": "Actes 2:4", "priere": "Par le Nom El-Rouah, guide mes pas.", "nassi": "19 fois, encens Oliban", "plantes": "Sauge", "huiles": "Citron", "cloture": "Psaume 119", "sadaka": "Sucre"},
    "Moussa": {"figure": FIGURES[15], "psaume": "Psaume 68", "verset": "Exode 14:13", "priere": "Par le Nom El-Fattah, ouvre le succès.", "nassi": "16 fois, eau aube", "plantes": "Cannelle", "huiles": "Encens", "cloture": "Psaume 68", "sadaka": "Dattes"}
}

# ==============================================================================
# 2. BASE DE DONNÉES DES INTERPRÉTATIONS (DB_CASES)
# ==============================================================================
# (J'ai abrégé pour la lecture, remettez votre bloc complet ici si besoin)
DB_CASES = {
    "Case 1": {"Djanvalimam": "Aggravation de maladie...", "Adama": "Bon employé...", "Malidjou": "Envoûtement...", "Bayadou": "Activité menée comme un malade.", "Tariqi": "Angoisse s’en ira.", "Issa": "Angoisse, trouble.", "Lomara": "Information sans joie.", "Mangoussi": "Destruction et fatigue.", "Kalalaho": "Situation difficile.", "Massa Souleymane": "Beaucoup de bien.", "Badra Ali": "Voie difficile.", "Noukoro": "Rentrée d’argent.", "Lacina": "Maladie grave.", "Totiqi": "Fin de difficultés.", "Mori Zoumana": "Victoire sur ennemis.", "Moussa": "Faillite après difficultés."}
    # ... ajoutez vos autres cases ici (7 à 16)
}

# ==============================================================================
# 3. INTERFACE
# ==============================================================================
st.set_page_config(page_title="Oracle Ramrou", layout="wide")
st.title("🔮 Oracle Ramrou — Cabinet de Haute Théurgie")

st.sidebar.header("Configuration du Tirage")
theme = {m: st.sidebar.selectbox(f"Maison M{m}", list(DB.keys()), key=f"select_m_{m}") for m in range(1, 17)}

if st.button("🔮 ANALYSER LE TIRAGE COMPLET"):
    st.subheader("📋 Analyse des Maisons")
    cols = st.columns(4)
    for m in range(1, 17):
        with cols[(m-1) % 4]:
            fig_name = theme[m]
            # Ici on utilise DB_CASES pour afficher l'interprétation
            interp = DB_CASES.get(f"Case {m}", {}).get(fig_name, "Interprétation non disponible")
            st.write(f"**M{m} ({fig_name})**: {interp}")

    st.divider()
    juge = theme[16]
    d = DB[juge]
    st.subheader(f"⚖️ Verdict Théurgique (Juge: {juge} - {d['figure']})")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"**📖 Psaume :** {d['psaume']}")
        st.markdown(f"**🙏 Prière :** {d['priere']}")
        st.info(f"**🧪 Protocole Nassi :** {d['nassi']}")
    with c2:
        st.success(f"**🌿 Plantes :** {d['plantes']}")
        st.success(f"**💧 Huiles :** {d['huiles']}")
        st.error(f"**⚡ Clôture :** {d['cloture']} | **🪙 Sadaka :** {d['sadaka']}")
