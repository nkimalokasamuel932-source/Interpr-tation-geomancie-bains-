import streamlit as st

# ==============================================================================
# 1. BASE DE DONNÉES COMPLÈTE (PROTOCOLES ET INTERPRÉTATIONS)
# ==============================================================================
FIGURES = [
    "Via", "Populus", "Conjunctio", "Carcer", "Fortuna Major", "Fortuna Minor", 
    "Acquisitio", "Amissio", "Laetitia", "Tristitia", "Puella", "Puer", 
    "Albus", "Rubeus", "Caput Draconis", "Cauda Draconis"
]

# Fusion de vos deux sources de données
DB = {
    "Djanvalimam": {"fig": FIGURES[0], "psaume": "Psaume 109", "priere": "Par le Nom Adonaï, dissipe les ténèbres.", "nassi": "111 fois, eau de puits", "plantes": "Laurier", "huiles": "Encens", "cloture": "Psaume 117", "sadaka": "Pain, dattes"},
    "Adama": {"fig": FIGURES[1], "psaume": "Psaume 121", "priere": "Par le Nom Elohim, ancre mes racines.", "nassi": "45 fois, eau + sel", "plantes": "Gingembre", "huiles": "Orange", "cloture": "Psaume 128", "sadaka": "Denrées rouges"},
    "Malidjou": {"fig": FIGURES[2], "psaume": "Psaume 23", "priere": "Par le Nom El-Shaddaï, ouvre l'abondance.", "nassi": "66 fois, eau de rose", "plantes": "Menthe", "huiles": "Citron", "cloture": "Psaume 150", "sadaka": "Sucre et lait"},
    "Bayadou": {"fig": FIGURES[3], "psaume": "Psaume 119", "priere": "Par le Nom El-Choura, accorde discernement.", "nassi": "360 fois, eau de pluie", "plantes": "Aloès", "huiles": "Lavande", "cloture": "Psaume 23", "sadaka": "Eau pure"},
    "Tariqi": {"fig": FIGURES[4], "psaume": "Psaume 112", "priere": "Par le Nom El-Elyon, protège ma lignée.", "nassi": "72 fois, menthe fraîche", "plantes": "Verveine", "huiles": "Camomille", "cloture": "Psaume 112", "sadaka": "Lait"},
    "Issa": {"fig": FIGURES[5], "psaume": "Psaume 6", "priere": "Par le Nom Rapha, restaure ma vigueur.", "nassi": "99 fois, feuilles de neem", "plantes": "Neem", "huiles": "Ylang-Ylang", "cloture": "Psaume 6", "sadaka": "Aumône"},
    "Lomara": {"fig": FIGURES[6], "psaume": "Psaume 35", "priere": "Par le Nom Shalom, neutralise les intrigues.", "nassi": "28 fois, parfum sans alcool", "plantes": "Sauge", "huiles": "Menthe", "cloture": "Psaume 35", "sadaka": "Sucre"},
    "Mangoussi": {"fig": FIGURES[7], "psaume": "Psaume 88", "priere": "Par le Nom Yahvé, demande restauration.", "nassi": "88 fois, miel", "plantes": "Santal", "huiles": "Vétiver", "cloture": "Psaume 88", "sadaka": "Céréales"},
    "Kalalaho": {"fig": FIGURES[8], "psaume": "Psaume 91", "priere": "Par le Nom El-Qahhar, sois ma Forteresse.", "nassi": "114 fois, eau de puits", "plantes": "Laurier", "huiles": "Clou de girofle", "cloture": "Psaume 91", "sadaka": "Pain"},
    "Massa Souleymane": {"fig": FIGURES[9], "psaume": "Psaume 72", "priere": "Par le Nom Malek, accorde-moi la justice.", "nassi": "110 fois, eau de santal", "plantes": "Patchouli", "huiles": "Santal", "cloture": "Psaume 72", "sadaka": "Pièces"},
    "Badra Ali": {"fig": FIGURES[10], "psaume": "Psaume 144", "priere": "Par le Nom Tsébaot, sois mon bouclier.", "nassi": "63 fois, camphre", "plantes": "Eucalyptus", "huiles": "Bergamote", "cloture": "Psaume 144", "sadaka": "Eau sucrée"},
    "Noukoro": {"fig": FIGURES[11], "psaume": "Psaume 29", "priere": "Par le Nom El-Hafiz, préserve-moi.", "nassi": "77 fois, eau de mer", "plantes": "Cèdre", "huiles": "Cèdre", "cloture": "Psaume 29", "sadaka": "Céréales"},
    "Lacina": {"fig": FIGURES[12], "psaume": "Psaume 3", "priere": "Par le Nom El-Adl, transmute la honte.", "nassi": "55 fois, laurier", "plantes": "Neem", "huiles": "Lavande", "cloture": "Psaume 3", "sadaka": "Lait"},
    "Totiqi": {"fig": FIGURES[13], "psaume": "Psaume 4", "priere": "Par le Nom El-Latif, libère des chaînes.", "nassi": "40 fois, pièce argent", "plantes": "Santal", "huiles": "Vétiver", "cloture": "Psaume 4", "sadaka": "Pièces"},
    "Mori Zoumana": {"fig": FIGURES[14], "psaume": "Psaume 119:105", "priere": "Par le Nom El-Rouah, guide mes pas.", "nassi": "19 fois, encens Oliban", "plantes": "Sauge", "huiles": "Citron", "cloture": "Psaume 119", "sadaka": "Sucre"},
    "Moussa": {"fig": FIGURES[15], "psaume": "Psaume 68", "priere": "Par le Nom El-Fattah, ouvre le succès.", "nassi": "16 fois, eau aube", "plantes": "Cannelle", "huiles": "Encens", "cloture": "Psaume 68", "sadaka": "Dattes"}
}

# Intégration complète de vos cases d'interprétation
DB_CASES = {
    "Case 1": {"Djanvalimam": "Aggravation de maladie...", "Adama": "Bon employé et bon matériel...", "Malidjou": "Envoûtement se dissipera...", "Bayadou": "Activité menée comme un malade.", "Tariqi": "Angoisse s’en ira.", "Issa": "Angoisse, trouble.", "Lomara": "Information sans joie.", "Mangoussi": "Destruction et fatigue.", "Kalalaho": "Situation qui ne s’améliore pas.", "Massa Souleymane": "Amènera beaucoup de bien.", "Badra Ali": "Voie difficile.", "Noukoro": "Rentrée d’argent.", "Lacina": "Maladie grave.", "Totiqi": "Fin de difficultés.", "Mori Zoumana": "Victoire sur les ennemis.", "Moussa": "Faillite après difficultés."},
    "Case 7": {"Djanvalimam": "Désir irréalisable.", "Adama": "Gain de cause.", "Malidjou": "Bon domicile.", "Bayadou": "Réunion avec la personne.", "Tariqi": "Relations, enfants.", "Issa": "Ce qu’on recherche.", "Lomara": "Destruction de domicile.", "Mangoussi": "Malédiction qui s’en ira.", "Kalalaho": "Position bonne.", "Massa Souleymane": "Entente va voler en éclats.", "Badra Ali": "Bonnes personnes.", "Noukoro": "Joie à venir.", "Lacina": "Gain faible.", "Totiqi": "Voie retrouvée.", "Mori Zoumana": "Affaire bénéfique.", "Moussa": "Réalisation rapide."},
    # ... [Vous pouvez ajouter ici le reste de vos cases 8 à 16 en suivant ce modèle]
}

# ==============================================================================
# INTERFACE
# ==============================================================================
st.set_page_config(page_title="Oracle Ramrou", layout="wide")
st.title("🔮 Oracle Ramrou — Cabinet de Haute Théurgie")

# Sélection des maisons
theme = {m: st.sidebar.selectbox(f"Maison M{m}", list(DB.keys()), key=f"sel_{m}") for m in range(1, 17)}

if st.button("🔮 ANALYSER LE TIRAGE COMPLET"):
    cols = st.columns(4)
    for m in range(1, 17):
        with cols[(m-1) % 4]:
            fig = theme[m]
            # Utilisation de DB_CASES pour l'interprétation
            txt = DB_CASES.get(f"Case {m}", {}).get(fig, "Information non disponible.")
            st.write(f"**M{m} ({fig})**: {txt}")

    # Verdict
    st.divider()
    juge = theme[16]
    d = DB[juge]
    st.subheader(f"⚖️ Verdict (Juge: {juge})")
    st.info(f"**Psaume:** {d['psaume']} | **Protocole Nassi:** {d['nassi']}")
