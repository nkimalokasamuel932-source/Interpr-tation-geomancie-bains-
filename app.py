import streamlit as st
# ==============================================================================
# 1. DÉFINITION DES FIGURES 
# ==============================================================================
# Cette liste doit être définie avant votre dictionnaire DB_TH
FIGURES = [Djanvalimam", "Adama", "Malidjou", "Bayadou", "Tariqi", "Issa", 
    "Lomara", "Mangoussi", "Kalalaho", "Massa Souleymane", "Badra Ali", 
    "Noukoro", "Lacina", "Totiqi", "Mori Zoumana", "Moussa"]
DB_CASES = {
    "Case 1": {
        "Djanvalimam": "Aggravation de maladie. Ce qui est perdu, lâ€™est dÃ©finitivement.",
        "Adama": "Bon employÃ© et bon matÃ©riel et retrouvaille de ce qui est perdu.",
        "Malidjou": "EnvoÃ»tement sur problÃ¨me difficile se dissipera et gain Ã  la fin.",
        "Bayadou": "ActivitÃ© menÃ©e comme un malade.",
        "Tariqi": "Angoisse sâ€™en ira et voyage en compagnie dâ€™un bien aimÃ©.",
        "Issa": "Angoisse, trouble. Peur des malfaiteurs.",
        "Lomara": "Information qui ne donne pas joie.",
        "Mangoussi": "Destruction et fatigue.",
        "Kalalaho": "Situation qui ne sâ€™amÃ©liore pas et affaire qui fait peur.",
        "Massa Souleymane": "Ce sur quoi il se renseigne amÃ¨nera beaucoup de bien.",
        "Badra Ali": "Voie difficile et ce qui se prÃ©sentera Ã  lui sera difficile.",
        "Noukoro": "RentrÃ©e dâ€™argent aprÃ¨s dÃ©gÃ¢t ou sortie.",
        "Lacina": "Maladie grave. Hypocrisie et Ã©touffement.",
        "Totiqi": "PÃ©nurie en un temps court. Fin de difficultÃ©s.",
        "Mori Zoumana": "RÃ©paration et victoire sur les ennemis.",
        "Moussa": "Faillite aprÃ¨s difficultÃ©s. Grand soucis."
    },
    "Case 7": {
        "Djanvalimam": "DÃ©sir irrÃ©alisable. Mauvais lieu de rÃ©sidence.",
        "Adama": "Beaucoup de soucis pour de lâ€™argent, mais gain de cause.",
        "Malidjou": "Bon domicile et gaietÃ© et quiÃ©tude dans la peur.",
        "Bayadou": "RÃ©union avec la personne recherchÃ©e.",
        "Tariqi": "Amis, enfants et compagnons (Relations, enfants et social).",
        "Issa": "Ce quâ€™on recherche. La destruction sur laquelle on se renseigne.",
        "Lomara": "Destruction de domicile. Mensonge au grand jour.",
        "Mangoussi": "MalÃ©diction qui sâ€™en ira avec difficultÃ©s.",
        "Kalalaho": "Position de la chambre est bonne et bonne femme.",
        "Massa Souleymane": "Lâ€™entente entre deux antagonistes va voler en Ã©clats.",
        "Badra Ali": "Sera en compagnie de bonnes personnes.",
        "Noukoro": "Joie Ã  venir Ã©manant dâ€™une promesse vÃ©ridique.",
        "Lacina": "Gain faible dâ€™argent. Ne peut tirer profit.",
        "Totiqi": "Voie. On retrouvera ce qui est perdu.",
        "Mori Zoumana": "Affaire bÃ©nÃ©fique et une demeure bÃ©nÃ©fique.",
        "Moussa": "RÃ©alisation rapide de dÃ©sir. Bien aimÃ© et compagnie."
    },
        "Case 8": {
        "Djanvalimam": "GuÃ©rison de malade.",
        "Adama": "Cherche une promotion. Perdra et retrouvera quelque chose.",
        "Malidjou": "Ce sur quoi tout le monde sâ€™accorde sur difficile et dÃ©penses.",
        "Bayadou": "Aura promotion et rentrÃ©e de convoitise.",
        "Tariqi": "Sortie. DÃ©placement de situation en situation.",
        "Issa": "Malfaiteur. Commerce mauvais.",
        "Lomara": "Lâ€™affaire importante recherchÃ©e est derriÃ¨re. Corruption.",
        "Mangoussi": "Ce que lâ€™on ne peut avoir. La mort.",
        "Kalalaho": "SÃ©paration aprÃ¨s entente de protagonistes. Grande peur.",
        "Massa Souleymane": "Peu dâ€™ennemis dÃ©voilÃ©s sur lâ€™ensemble. Bonne fin.",
        "Badra Ali": "Le demandeur est serrÃ© mais la voie va sâ€™ouvrir.",
        "Noukoro": "Travail occulte trÃ¨s difficile et victoire partielle.",
        "Lacina": "Contrainte coupÃ©e et sÃ©paration.",
        "Totiqi": "Voie sans intÃ©rÃªt et ne peut avoir ce dont il a besoin.",
        "Mori Zoumana": "Perte de quelque chose. Le consultant a des soucis.",
        "Moussa": "Clameur et affaire Ã©touffante et mauvaise chose arrivÃ©e."
    },
    "Case 9": {
        "Djanvalimam": "Voyage sans profit. Le dÃ©sir cachÃ© se rÃ©alisera.",
        "Adama": "Voyage bÃ©nÃ©fique et rencontre de celui qui est absent.",
        "Malidjou": "Bonne activitÃ©. Et les activitÃ©s empÃªchÃ©es reprendront.",
        "Bayadou": "Rejeter mauvais voyage. ArrivÃ©e dâ€™information vÃ©ridique.",
        "Tariqi": "Joie Ã  lâ€™intÃ©rieur. Bienfait Ã  la fin de lâ€™affaire.",
        "Issa": "Atteinte dâ€™espÃ©rance dans voyage.",
        "Lomara": "Tu auras ce qui est cachÃ© (information ou argent).",
        "Mangoussi": "Perte de recours. Voyage mÃ©diocre.",
        "Kalalaho": "Voyage sera bÃ©nÃ©fique. MontÃ©e en situation.",
        "Massa Souleymane": "ArrivÃ©e de renommÃ©e aprÃ¨s attente.",
        "Badra Ali": "Sortie. Voie et faillite proche.",
        "Noukoro": "Il ne peut avoir ce quâ€™il veut quâ€™avec insistance.",
        "Lacina": "GaietÃ©. ActivitÃ© rentable. Voyage bon et gloire.",
        "Totiqi": "Rang Ã©levÃ© et classe sociale.",
        "Mori Zoumana": "Voyage avec espoir, considÃ©ration et joie.",
        "Moussa": "Voyage avec espoir, considÃ©ration et joie et retour absent."
    },
    "Case 10": {
        "Djanvalimam": "Promotion dÃ©sirÃ©e se rÃ©alisera avec bienfait.",
        "Adama": "Consultant dans la difficultÃ© sans aide. DÃ©sir se rÃ©alisera.",
        "Malidjou": "Perdra quelque chose mais aura gloire et ascension.",
        "Bayadou": "ConsidÃ©ration et ascension. RentrÃ©e rapide dâ€™argent.",
        "Tariqi": "Rassemblement avec sÃ©paration et ascension.",
        "Issa": "Aide de la part des autoritÃ©s dans le lointain.",
        "Lomara": "Gloire, ascension au moment opportun suivi de joie.",
        "Mangoussi": "Recherche de bienfait dans lâ€™immobilier qui se concrÃ©tisera.",
        "Kalalaho": "RÃ©alisation de but suivi de pouvoir et fortune.",
        "Massa Souleymane": "Le demandeur aura gaietÃ© et gloire.",
        "Badra Ali": "La fin du problÃ¨me amÃ¨nera la gaietÃ©.",
        "Noukoro": "Fin bÃ©nÃ©fique et joie et explosion de joie.",
        "Lacina": "Ce qui est perdu recherchÃ© le sera en vain.",
        "Totiqi": "GaietÃ© et joie. Ce qui est cachÃ© sera retrouvÃ©.",
        "Mori Zoumana": "Aide et bien-Ãªtre et acquisition de pouvoir.",
        "Moussa": "Pouvoir. Acquisition de rang et classe sociale."
    },
    "Case 11": {
        "Djanvalimam": "DÃ©sespoir Ã  cause de dÃ©sir irrÃ©alisable.",
        "Adama": "Pouvoir et ascension, quittera difficultÃ© pour facilitÃ©.",
        "Malidjou": "AngoissÃ© et soumis par les ennemis. Mais espoir.",
        "Bayadou": "Information imminente. Acquisition dÃ©sir aprÃ¨s long moment.",
        "Tariqi": "Acquisition dâ€™espÃ©rance. Les ennemis seront dÃ©Ã§us.",
        "Issa": "Aura de lâ€™aide dans sa recherche.",
        "Lomara": "Chance et bienfait et aggravation de ce dont on a peur.",
        "Mangoussi": "Exaucement de dÃ©sir aprÃ¨s problÃ¨mes.",
        "Kalalaho": "Information en route est vraie et se rÃ©alisera vite.",
        "Massa Souleymane": "Aura gain de cause sur lâ€™objet recherchÃ©.",
        "Badra Ali": "Retour de pensÃ©es.",
        "Noukoro": "Ce qui est recherchÃ© restera toujours recherchÃ©.",
        "Lacina": "Retour de personne partie. EspÃ©rance avec renommÃ©e.",
        "Totiqi": "Joie Ã  venir. Acquisition dans la joie.",
        "Mori Zoumana": "Lieu oÃ¹ existe aisance.",
        "Moussa": "RapiditÃ© dans convoitise est mieux."
    },
    "Case 12": {
        "Djanvalimam": "Celui qui sâ€™informe a beaucoup de dÃ©sirs.",
        "Adama": "Destruction et mensonge mais gain de cause dans joie.",
        "Malidjou": "Mauvaise information. QuiÃ©tude envers ennemis.",
        "Bayadou": "Contrainte et soumission.",
        "Tariqi": "Retour de joie aprÃ¨s dÃ©ception.",
        "Issa": "Lâ€™ennemi sera dÃ©masquÃ©, sera attachÃ© et nâ€™aura rien.",
        "Lomara": "Ce quâ€™on cherche chez les ennemis apportera quiÃ©tude.",
        "Mangoussi": "Ennemi capable et traitre ; nâ€™aura pas convoitise.",
        "Kalalaho": "Aura pouvoir et davantage.",
        "Massa Souleymane": "ActivitÃ© non fructueuse. Patience dÃ©bloquera.",
        "Badra Ali": "Gain facile et victoire sur ennemis.",
        "Noukoro": "Capture et travail mystique.",
        "Lacina": "Ennemis des 2 sexes. Capture, trahison, mÃ©chancetÃ©.",
        "Totiqi": "Perte dÃ©finitive de quelque chose ou dâ€™argent.",
        "Mori Zoumana": "Les ennemis perdront leurs relations.",
        "Moussa": "Acquisition de chance et joie dans gestion."
    },
    "Case 13": {
        "Djanvalimam": "DifficultÃ© et dÃ©sir difficile.",
        "Adama": "Voie ouverte. GaietÃ©. DÃ©sir bÃ©nÃ©fique.",
        "Malidjou": "Obtention de convoitise et rentrÃ©e dâ€™argent.",
        "Bayadou": "Bonne femme. Bon vivant et aura bienfait.",
        "Tariqi": "Regroupement et beaucoup de mÃ©cÃ¨nes.",
        "Issa": "Le demandeur sera informÃ© que lâ€™enquÃªteur est dans la peur.",
        "Lomara": "Amis menteurs. Nouvelle mensongÃ¨re.",
        "Mangoussi": "Voie dangereuse. Rapporteur.",
        "Kalalaho": "Grande gaietÃ© et bon signe.",
        "Massa Souleymane": "RÃ©union avec compagnons et personnes qui aident.",
        "Badra Ali": "Information venant de dehors propagÃ©e par toi-mÃªme.",
        "Noukoro": "Assez de contraintes et long soucis.",
        "Lacina": "Bienfait. Recherche dâ€™argent.",
        "Totiqi": "RÃ©ception de quelque chose avec bienfait.",
        "Mori Zoumana": "Sortie sans profit et un bon terme.",
        "Moussa": "Voie et joie et fin bÃ©nÃ©fique."
    },
    "Case 14": {
        "Djanvalimam": "Aura gain de cause auprÃ¨s des femmes.",
        "Adama": "Gain dâ€™argent et bon endroit pour dormir.",
        "Malidjou": "Destruction et peur et mÃ©faits des ennemis.",
        "Bayadou": "Changement rÃ©pÃ©titif de statut social.",
        "Tariqi": "RentrÃ©e de pouvoir et ascension et joie.",
        "Issa": "Tous les dÃ©gÃ¢ts viennent de ce que lâ€™on cherche.",
        "Lomara": "ProblÃ¨mes engendrÃ©s par les ennemis.",
        "Mangoussi": "Abandon de convoitise parce que difficile.",
        "Kalalaho": "A la fin, aura gain de cause avec des objectifs.",
        "Massa Souleymane": "Compagnon ou associÃ© nâ€™est pas bon.",
        "Badra Ali": "Le demandeur aura quelque chose de sa convoitise.",
        "Noukoro": "Faillite et reprise Ã  la fin.",
        "Lacina": "Information mensongÃ¨re. MÃ©chancetÃ©.",
        "Totiqi": "Responsable non mÃ©ritant. Son soutien nâ€™est pas bon.",
        "Mori Zoumana": "Quelques mensonges et affaire convenable.",
        "Moussa": "Quelque chose qui aboutira, situation non bÃ©nÃ©fique."
    },
    "Case 15": {
        "Djanvalimam": "SÃ©curitÃ© et vaincra sa peur.",
        "Adama": "Sortie et acquisition de quelque chose de force.",
        "Malidjou": "Aura ce quâ€™il espÃ¨re.",
        "Bayadou": "Mensonge. Hypocrisie et dÃ©sespoir.",
        "Tariqi": "Bienfaits multiples.",
        "Issa": "Ce qui se renouvelle et voyage Ã©vident.",
        "Lomara": "Atteinte de tout dÃ©sir.",
        "Mangoussi": "Situation sâ€™arrÃªtera. Patience.",
        "Kalalaho": "Action imprÃ©vue favorable.",
        "Massa Souleymane": "Changement de direction soudain.",
        "Badra Ali": "Protection divine et aide inattendue.",
        "Noukoro": "Perte d'opportunitÃ© soudaine.",
        "Lacina": "RÃ©alisation lente mais certaine.",
        "Totiqi": "Rencontre imprÃ©vue qui dÃ©bloque.",
        "Mori Zoumana": "DÃ©couverte dâ€™une vÃ©ritÃ© cachÃ©e.",
        "Moussa": "SuccÃ¨s total et inespÃ©rÃ©."
    },
    "Case 16": {
        "Djanvalimam": "Prendre femme de caractÃ¨re moyen et laisser mauvaise.",
        "Adama": "DifficultÃ© vÃ©cue terminera sur facilitÃ©, rÃ©solution rapide.",
        "Malidjou": "Bonne fin dans les activitÃ©s et joie.",
        "Bayadou": "ArrivÃ©e de joie et voie bonne.",
        "Tariqi": "On aura ce quâ€™on dÃ©sire avec insistance.",
        "Issa": "Voie qui se dÃ©voile. Bienfait irrÃ©alisable.",
        "Lomara": "Lâ€™issue de lâ€™affaire est bonne et bÃ©nÃ©fique.",
        "Mangoussi": "Acquisition difficile. Vide. Malchance acquis.",
        "Kalalaho": "Lâ€™affaire trainera mais gain de cause Ã  la fin.",
        "Massa Souleymane": "Femme. Gain de considÃ©ration et bienfait.",
        "Badra Ali": "Bonne fin et aucune crainte des gens.",
        "Noukoro": "Recherche dâ€™espoir pour atteindre succÃ¨s.",
        "Lacina": "Mauvaise fin dâ€™affaire et mensonge.",
        "Totiqi": "SÃ©rÃ©nitÃ© et bonnes annonces.",
        "Mori Zoumana": "RentrÃ©e dâ€™argent sur place sans crainte.",
        "Moussa": "RentrÃ©e dâ€™argent sur place sans crainte."
    }
}
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
# 3. INTERFACE STREAMLIT
# ==============================================================================
st.set_page_config(page_title="Oracle Ramrou", layout="wide")
st.title("ðŸ”® Oracle Ramrou â€” Cabinet de Haute ThÃ©urgie")

st.sidebar.header("Configuration du Tirage")
theme = {m: st.sidebar.selectbox(f"Maison M{m}", list(DB_TH.keys()), key=f"m{m}") for m in range(1, 17)}

if st.button("ðŸ”® ANALYSER LE TIRAGE COMPLET"):
    st.subheader("ðŸ“‹ Analyse des Maisons")
    cols = st.columns(4)
    for i, m in enumerate(range(1, 17)):
        with cols[i % 4]:
            fig_name = theme[m]
            case_key = f"Case {m}"
            interp = DB_CASES.get(case_key, {}).get(fig_name, "Information non disponible")
            st.write(f"**M{m} ({fig_name})**: {interp}")

    st.divider()
    
    # Verdict ThÃ©urgique (Juge M16)
    juge = theme[16]
    d = DB_TH[juge]
    st.subheader(f"âš–ï¸ Verdict ThÃ©urgique (Juge: {juge})")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Psaume :** {d['psaume']}\n**PriÃ¨re :** {d['priere']}")
    with col2:
        st.success(f"**Plantes :** {d['plantes']}\n**Huiles :** {d['huiles']}")
    st.error(f"**Protocole Nassi :** {d['nassi']}")
