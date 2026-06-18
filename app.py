import streamlit as st

# ==============================================================================
# BASE DE DONNÉES MAÎTRE (AVEC FIGURES GÉOMANTIQUES)
# ==============================================================================
# Figures associées aux 16 maisons

import streamlit as st

# ==============================================================================
# 1. BASE DE DONNÉES THÉURGIQUE (PROTOCOLES)
# ==============================================================================
DB_TH = {
    "Djanvalimam": {"psaume": "Psaume 109", "priere": "Par le Nom Adonaï, dissipe les ténèbres.", "nassi": "111 fois, eau de puits", "plantes": "Laurier", "huiles": "Encens"},
    "Adama": {"psaume": "Psaume 121", "priere": "Par le Nom Elohim, ancre mes racines.", "nassi": "45 fois, eau + sel", "plantes": "Gingembre", "huiles": "Orange"},
    "Malidjou": {"psaume": "Psaume 23", "priere": "Par le Nom El-Shaddaï, ouvre l'abondance.", "nassi": "66 fois, eau de rose", "plantes": "Menthe", "huiles": "Citron"},
    "Bayadou": {"psaume": "Psaume 119", "priere": "Par le Nom El-Choura, accorde discernement.", "nassi": "360 fois, eau de pluie", "plantes": "Aloès", "huiles": "Lavande"},
    "Tariqi": {"psaume": "Psaume 112", "priere": "Par le Nom El-Elyon, protège ma lignée.", "nassi": "72 fois, menthe fraîche", "plantes": "Verveine", "huiles": "Camomille"},
    "Issa": {"psaume": "Psaume 6", "priere": "Par le Nom Rapha, restaure ma vigueur.", "nassi": "99 fois, feuilles de neem", "plantes": "Neem", "huiles": "Ylang-Ylang"},
    "Lomara": {"psaume": "Psaume 35", "priere": "Par le Nom Shalom, neutralise les intrigues.", "nassi": "28 fois, parfum sans alcool", "plantes": "Sauge", "huiles": "Menthe"},
    "Mangoussi": {"psaume": "Psaume 88", "priere": "Par le Nom Yahvé, demande restauration.", "nassi": "88 fois, miel", "plantes": "Santal", "huiles": "Vétiver"},
    "Kalalaho": {"psaume": "Psaume 91", "priere": "Par le Nom El-Qahhar, sois ma Forteresse.", "nassi": "114 fois, eau de puits", "plantes": "Laurier", "huiles": "Clou de girofle"},
    "Massa Souleymane": {"psaume": "Psaume 72", "priere": "Par le Nom Malek, accorde-moi la justice.", "nassi": "110 fois, eau de santal", "plantes": "Patchouli", "huiles": "Santal"},
    "Badra Ali": {"psaume": "Psaume 144", "priere": "Par le Nom Tsébaot, sois mon bouclier.", "nassi": "63 fois, camphre", "plantes": "Eucalyptus", "huiles": "Bergamote"},
    "Noukoro": {"psaume": "Psaume 29", "priere": "Par le Nom El-Hafiz, préserve-moi.", "nassi": "77 fois, eau de mer", "plantes": "Cèdre", "huiles": "Cèdre"},
    "Lacina": {"psaume": "Psaume 3", "priere": "Par le Nom El-Adl, transmute la honte.", "nassi": "55 fois, laurier", "plantes": "Neem", "huiles": "Lavande"},
    "Totiqi": {"psaume": "Psaume 4", "priere": "Par le Nom El-Latif, libère des chaînes.", "nassi": "40 fois, pièce argent", "plantes": "Santal", "huiles": "Vétiver"},
    "Mori Zoumana": {"psaume": "Psaume 119", "priere": "Par le Nom El-Rouah, guide mes pas.", "nassi": "19 fois, encens Oliban", "plantes": "Sauge", "huiles": "Citron"},
    "Moussa": {"psaume": "Psaume 68", "priere": "Par le Nom El-Fattah, ouvre le succès.", "nassi": "16 fois, eau aube", "plantes": "Cannelle", "huiles": "Encens"}
}

# ==============================================================================
# 2. BASE DE DONNÉES DES INTERPRÉTATIONS
# ==============================================================================
DB_CASES = {
    "Case 1": {
        "Djanvalimam": "Aggravation de maladie. Ce qui est perdu, l’est définitivement.",
        "Adama": "Bon employé et bon matériel et retrouvaille de ce qui est perdu.",
        "Malidjou": "Envoûtement sur problème difficile se dissipera et gain à la fin.",
        "Bayadou": "Activité menée comme un malade.",
        "Tariqi": "Angoisse s’en ira et voyage en compagnie d’un bien aimé.",
        "Issa": "Angoisse, trouble. Peur des malfaiteurs.",
        "Lomara": "Information qui ne donne pas joie.",
        "Mangoussi": "Destruction et fatigue.",
        "Kalalaho": "Situation qui ne s’améliore pas et affaire qui fait peur.",
        "Massa Souleymane": "Ce sur quoi il se renseigne amènera beaucoup de bien.",
        "Badra Ali": "Voie difficile et ce qui se présentera à lui sera difficile.",
        "Noukoro": "Rentrée d’argent après dégât ou sortie.",
        "Lacina": "Maladie grave. Hypocrisie et étouffement.",
        "Totiqi": "Pénurie en un temps court. Fin de difficultés.",
        "Mori Zoumana": "Réparation et victoire sur les ennemis.",
        "Moussa": "Faillite après difficultés. Grand soucis."
    },
    "Case 7": {
        "Djanvalimam": "Désir irréalisable. Mauvais lieu de résidence.",
        "Adama": "Beaucoup de soucis pour de l’argent, mais gain de cause.",
        "Malidjou": "Bon domicile et gaieté et quiétude dans la peur.",
        "Bayadou": "Réunion avec la personne recherchée.",
        "Tariqi": "Amis, enfants et compagnons (Relations, enfants et social).",
        "Issa": "Ce qu’on recherche. La destruction sur laquelle on se renseigne.",
        "Lomara": "Destruction de domicile. Mensonge au grand jour.",
        "Mangoussi": "Malédiction qui s’en ira avec difficultés.",
        "Kalalaho": "Position de la chambre est bonne et bonne femme.",
        "Massa Souleymane": "L’entente entre deux antagonistes va voler en éclats.",
        "Badra Ali": "Sera en compagnie de bonnes personnes.",
        "Noukoro": "Joie à venir émanant d’une promesse véridique.",
        "Lacina": "Gain faible d’argent. Ne peut tirer profit.",
        "Totiqi": "Voie. On retrouvera ce qui est perdu.",
        "Mori Zoumana": "Affaire bénéfique et une demeure bénéfique.",
        "Moussa": "Réalisation rapide de désir. Bien aimé et compagnie."
    },
    "Case 8": {
        "Djanvalimam": "Guérison de malade.",
        "Adama": "Cherche une promotion. Perdra et retrouvera quelque chose.",
        "Malidjou": "Ce sur quoi tout le monde s’accorde sur difficile et dépenses.",
        "Bayadou": "Aura promotion et rentrée de convoitise.",
        "Tariqi": "Sortie. Déplacement de situation en situation.",
        "Issa": "Malfaiteur. Commerce mauvais.",
        "Lomara": "L’affaire importante recherchée est derrière. Corruption.",
        "Mangoussi": "Ce que l’on ne peut avoir. La mort.",
        "Kalalaho": "Séparation après entente de protagonistes. Grande peur.",
        "Massa Souleymane": "Peu d’ennemis dévoilés sur l’ensemble. Bonne fin.",
        "Badra Ali": "Le demandeur est serré mais la voie va s’ouvrir.",
        "Noukoro": "Travail occulte très difficile et victoire partielle.",
        "Lacina": "Contrainte coupée et séparation.",
        "Totiqi": "Voie sans intérêt et ne peut avoir ce dont il a besoin.",
        "Mori Zoumana": "Perte de quelque chose. Le consultant a des soucis.",
        "Moussa": "Clameur et affaire étouffante et mauvaise chose arrivée."
    },
    "Case 9": {
        "Djanvalimam": "Voyage sans profit. Le désir caché se réalisera.",
        "Adama": "Voyage bénéfique et rencontre de celui qui est absent.",
        "Malidjou": "Bonne activité. Et les activités empêchées reprendront.",
        "Bayadou": "Rejeter mauvais voyage. Arrivée d’information véridique.",
        "Tariqi": "Joie à l’intérieur. Bienfait à la fin de l’affaire.",
        "Issa": "Atteinte d’espérance dans voyage.",
        "Lomara": "Tu auras ce qui est caché (information ou argent).",
        "Mangoussi": "Perte de recours. Voyage médiocre.",
        "Kalalaho": "Voyage sera bénéfique. Montée en situation.",
        "Massa Souleymane": "Arrivée de renommée après attente.",
        "Badra Ali": "Sortie. Voie et faillite proche.",
        "Noukoro": "Il ne peut avoir ce qu’il veut qu’avec insistance.",
        "Lacina": "Gaieté. Activité rentable. Voyage bon et gloire.",
        "Totiqi": "Rang élevé et classe sociale.",
        "Mori Zoumana": "Voyage avec espoir, considération et joie.",
        "Moussa": "Voyage avec espoir, considération et joie et retour absent."
    },
    "Case 10": {
        "Djanvalimam": "Promotion désirée se réalisera avec bienfait.",
        "Adama": "Consultant dans la difficulté sans aide. Désir se réalisera.",
        "Malidjou": "Perdra quelque chose mais aura gloire et ascension.",
        "Bayadou": "Considération et ascension. Rentrée rapide d’argent.",
        "Tariqi": "Rassemblement avec séparation et ascension.",
        "Issa": "Aide de la part des autorités dans le lointain.",
        "Lomara": "Gloire, ascension au moment opportun suivi de joie.",
        "Mangoussi": "Recherche de bienfait dans l’immobilier qui se concrétisera.",
        "Kalalaho": "Réalisation de but suivi de pouvoir et fortune.",
        "Massa Souleymane": "Le demandeur aura gaieté et gloire.",
        "Badra Ali": "La fin du problème amènera la gaieté.",
        "Noukoro": "Fin bénéfique et joie et explosion de joie.",
        "Lacina": "Ce qui est perdu recherché le sera en vain.",
        "Totiqi": "Gaieté et joie. Ce qui est caché sera retrouvé.",
        "Mori Zoumana": "Aide et bien-être et acquisition de pouvoir.",
        "Moussa": "Pouvoir. Acquisition de rang et classe sociale."
    },
    "Case 11": {
        "Djanvalimam": "Désespoir à cause de désir irréalisable.",
        "Adama": "Pouvoir et ascension, quittera difficulté pour facilité.",
        "Malidjou": "Angoissé et soumis par les ennemis. Mais espoir.",
        "Bayadou": "Information imminente. Acquisition désir après long moment.",
        "Tariqi": "Acquisition d’espérance. Les ennemis seront déçus.",
        "Issa": "Aura de l’aide dans sa recherche.",
        "Lomara": "Chance et bienfait et aggravation de ce dont on a peur.",
        "Mangoussi": "Exaucement de désir après problèmes.",
        "Kalalaho": "Information en route est vraie et se réalisera vite.",
        "Massa Souleymane": "Aura gain de cause sur l’objet recherché.",
        "Badra Ali": "Retour de pensées.",
        "Noukoro": "Ce qui est recherché restera toujours recherché.",
        "Lacina": "Retour de personne partie. Espérance avec renommée.",
        "Totiqi": "Joie à venir. Acquisition dans la joie.",
        "Mori Zoumana": "Lieu où existe aisance.",
        "Moussa": "Rapidité dans convoitise est mieux."
    },
    "Case 12": {
        "Djanvalimam": "Celui qui s’informe a beaucoup de désirs.",
        "Adama": "Destruction et mensonge mais gain de cause dans joie.",
        "Malidjou": "Mauvaise information. Quiétude envers ennemis.",
        "Bayadou": "Contrainte et soumission.",
        "Tariqi": "Retour de joie après déception.",
        "Issa": "L’ennemi sera démasqué, sera attaché et n’aura rien.",
        "Lomara": "Ce qu’on cherche chez les ennemis apportera quiétude.",
        "Mangoussi": "Ennemi capable et traitre ; n’aura pas convoitise.",
        "Kalalaho": "Aura pouvoir et davantage.",
        "Massa Souleymane": "Activité non fructueuse. Patience débloquera.",
        "Badra Ali": "Gain facile et victoire sur ennemis.",
        "Noukoro": "Capture et travail mystique.",
        "Lacina": "Ennemis des 2 sexes. Capture, trahison, méchanceté.",
        "Totiqi": "Perte définitive de quelque chose ou d’argent.",
        "Mori Zoumana": "Les ennemis perdront leurs relations.",
        "Moussa": "Acquisition de chance et joie dans gestion."
    },
    "Case 13": {
        "Djanvalimam": "Difficulté et désir difficile.",
        "Adama": "Voie ouverte. Gaieté. Désir bénéfique.",
        "Malidjou": "Obtention de convoitise et rentrée d’argent.",
        "Bayadou": "Bonne femme. Bon vivant et aura bienfait.",
        "Tariqi": "Regroupement et beaucoup de mécènes.",
        "Issa": "Le demandeur sera informé que l’enquêteur est dans la peur.",
        "Lomara": "Amis menteurs. Nouvelle mensongère.",
        "Mangoussi": "Voie dangereuse. Rapporteur.",
        "Kalalaho": "Grande gaieté et bon signe.",
        "Massa Souleymane": "Réunion avec compagnons et personnes qui aident.",
        "Badra Ali": "Information venant de dehors propagée par toi-même.",
        "Noukoro": "Assez de contraintes et long soucis.",
        "Lacina": "Bienfait. Recherche d’argent.",
        "Totiqi": "Réception de quelque chose avec bienfait.",
        "Mori Zoumana": "Sortie sans profit et un bon terme.",
        "Moussa": "Voie et joie et fin bénéfique."
    },
    "Case 14": {
        "Djanvalimam": "Aura gain de cause auprès des femmes.",
        "Adama": "Gain d’argent et bon endroit pour dormir.",
        "Malidjou": "Destruction et peur et méfaits des ennemis.",
        "Bayadou": "Changement répétitif de statut social.",
        "Tariqi": "Rentrée de pouvoir et ascension et joie.",
        "Issa": "Tous les dégâts viennent de ce que l’on cherche.",
        "Lomara": "Problèmes engendrés par les ennemis.",
        "Mangoussi": "Abandon de convoitise parce que difficile.",
        "Kalalaho": "A la fin, aura gain de cause avec des objectifs.",
        "Massa Souleymane": "Compagnon ou associé n’est pas bon.",
        "Badra Ali": "Le demandeur aura quelque chose de sa convoitise.",
        "Noukoro": "Faillite et reprise à la fin.",
        "Lacina": "Information mensongère. Méchanceté.",
        "Totiqi": "Responsable non méritant. Son soutien n’est pas bon.",
        "Mori Zoumana": "Quelques mensonges et affaire convenable.",
        "Moussa": "Quelque chose qui aboutira, situation non bénéfique."
    },
    "Case 15": {
        "Djanvalimam": "Sécurité et vaincra sa peur.",
        "Adama": "Sortie et acquisition de quelque chose de force.",
        "Malidjou": "Aura ce qu’il espère.",
        "Bayadou": "Mensonge. Hypocrisie et désespoir.",
        "Tariqi": "Bienfaits multiples.",
        "Issa": "Ce qui se renouvelle et voyage évident.",
        "Lomara": "Atteinte de tout désir.",
        "Mangoussi": "Situation s’arrêtera. Patience.",
        "Kalalaho": "Action imprévue favorable.",
        "Massa Souleymane": "Changement de direction soudain.",
        "Badra Ali": "Protection divine et aide inattendue.",
        "Noukoro": "Perte d'opportunité soudaine.",
        "Lacina": "Réalisation lente mais certaine.",
        "Totiqi": "Rencontre imprévue qui débloque.",
        "Mori Zoumana": "Découverte d’une vérité cachée.",
        "Moussa": "Succès total et inespéré."
    },
    "Case 16": {
        "Djanvalimam": "Prendre femme de caractère moyen et laisser mauvaise.",
        "Adama": "Difficulté vécue terminera sur facilité, résolution rapide.",
        "Malidjou": "Bonne fin dans les activités et joie.",
        "Bayadou": "Arrivée de joie et voie bonne.",
        "Tariqi": "On aura ce qu’on désire avec insistance.",
        "Issa": "Voie qui se dévoile. Bienfait irréalisable.",
        "Lomara": "L’issue de l’affaire est bonne et bénéfique.",
        "Mangoussi": "Acquisition difficile. Vide. Malchance acquis.",
        "Kalalaho": "L’affaire trainera mais gain de cause à la fin.",
        "Massa Souleymane": "Femme. Gain de considération et bienfait.",
        "Badra Ali": "Bonne fin et aucune crainte des gens.",
        "Noukoro": "Recherche d’espoir pour atteindre succès.",
        "Lacina": "Mauvaise fin d’affaire et mensonge.",
        "Totiqi": "Sérénité et bonnes annonces.",
        "Mori Zoumana": "Rentrée d’argent sur place sans crainte.",
        "Moussa": "Rentrée d’argent sur place sans crainte."
    }
}

# ==============================================================================
# 3. INTERFACE STREAMLIT
# ==============================================================================
st.set_page_config(page_title="Oracle Ramrou", layout="wide")
st.title("🔮 Oracle Ramrou — Cabinet de Haute Théurgie")

st.sidebar.header("Configuration du Tirage")
theme = {m: st.sidebar.selectbox(f"Maison M{m}", list(DB_TH.keys()), key=f"m{m}") for m in range(1, 17)}

if st.button("🔮 ANALYSER LE TIRAGE COMPLET"):
    st.subheader("📋 Analyse des Maisons")
    cols = st.columns(4)
    for i, m in enumerate(range(1, 17)):
        with cols[i % 4]:
            fig_name = theme[m]
            case_key = f"Case {m}"
            interp = DB_CASES.get(case_key, {}).get(fig_name, "Information non disponible")
            st.write(f"**M{m} ({fig_name})**: {interp}")

    st.divider()
    
    # Verdict Théurgique (Juge M16)
    juge = theme[16]
    d = DB_TH[juge]
    st.subheader(f"⚖️ Verdict Théurgique (Juge: {juge})")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Psaume :** {d['psaume']}\n**Prière :** {d['priere']}")
    with col2:
        st.success(f"**Plantes :** {d['plantes']}\n**Huiles :** {d['huiles']}")
    st.error(f"**Protocole Nassi :** {d['nassi']}")
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
