import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Théurgie & Géomancie Sacrée", page_icon="✨", layout="wide")

# ==============================================================================
# ACCÈS
# ==============================================================================
ID_SECRET = "theurge2026"
MDP_SECRET = "Salomon777"

# ==============================================================================
# BASE DE DONNÉES THÉURGIQUE ET MYSTIQUE COMPLÈTE
# ==============================================================================
DATA = {
    "Bila (Seydiou)": {
        "ref": "Bila (ou Sira / VIA)", 
        "nature": "Neutre", 
        "txt": "Ouverture des routes, déblocage des voies sans issue, dénouement des blocages de projets.",
        "psaume": "Psaume 23", "verset": "Verset 3", "texte_biblique": "Il restaure mon âme, il me conduit dans les sentiers de la justice, à cause de son nom.",
        "huile": "Menthe Poivrée (Vitesse et clarté)", "plantes": "Feuilles de menthe fraîche, Laurier, Verveine",
        "zikr": "Ya Fattah (Ô Celui qui ouvre) — 489 fois",
        "mots_application": "Par la vertu de ce Nassi et la puissance du Psaume 23, que toutes mes routes fermées soient brisées et que la chance m'accompagne partout où mes pieds fouleront le sol. Amen.",
        "moment": "Matin au lever du soleil"
    },
    "Adama": {
        "ref": "Adama (CAPUT DRACONIS)", 
        "nature": "Bénéfique", 
        "txt": "Élévation spirituelle, charisme, autorité, obtention de postes de direction, royauté.",
        "psaume": "Psaume 8", "verset": "Verset 6", "texte_biblique": "Tu lui as donné l'empire sur les œuvres de tes mains, tu as tout mis sous ses pieds.",
        "huile": "Cèdre de l'Atlas (Ancrage royal)", "plantes": "Écorce de cèdre, Romarin, Basilic sacré",
        "zikr": "Ya Rafi'u (Ô Celui qui élève) — 351 fois",
        "mots_application": "Que l'élévation, la considération et l'autorité de Sa Majesté le Roi Salomon descendent sur ma vie. Que mes ennemis deviennent mon marchepied. Amen.",
        "moment": "Matin à la première heure"
    },
    "Mahamadou (Maldiou)": {
        "ref": "Mahamadou (FORTUNA MINOR)", 
        "nature": "Neutre", 
        "txt": "Soutien collectif, popularité rapide, protection lors des concours ou examens publics.",
        "psaume": "Psaume 4", "verset": "Verset 7", "texte_biblique": "Fais lever sur nous la lumière de ta face, ô Éternel !",
        "huile": "Orange Douce (Magnétisme solaire)", "plantes": "Zestes d'orange, Pétales de Souci (Calendula), Hibiscus",
        "zikr": "Ya Nour (Ô Lumière) — 256 fois",
        "mots_application": "Que ma présence brille parmi les hommes comme le soleil au zénith. Que la faveur populaire m'accompagne dans toutes mes démarches publiques. Amen.",
        "moment": "Matin"
    },
    "Idrissa": {
        "ref": "Idrissa (ACQUISITIO)", 
        "nature": "Bénéfique", 
        "txt": "Attraction financière magnétique, rentrées d'argent, succès commercial et prospérité matérielle.",
        "psaume": "Psaume 112", "verset": "Verset 3", "texte_biblique": "Il a dans sa maison bien-être et richesse, et sa justice subsiste à jamais.",
        "huile": "Patchouli (Magnétisme de la richesse)", "plantes": "Bâtons de cannelle concassés, Trèfle, Menthe séchée",
        "zikr": "Ya Razzaq (Ô Pourvoyeur) — 308 fois",
        "mots_application": "Que les richesses de la terre et de l'esprit soient aimantées vers ma demeure. Que l'abondance ne quitte jamais mes mains ni mes comptes. Amen.",
        "moment": "Matin (Heure du commerce)"
    },
    "Yousouf (Issa/Nouhou)": {
        "ref": "Yousouf (FORTUNA MAJOR)", 
        "nature": "Bénéfique", 
        "txt": "Grande chance durable, succès total aux examens, jeux, bénédiction de la destinée.",
        "psaume": "Psaume 20", "verset": "Verset 5", "texte_biblique": "Qu'il te donne ce que ton cœur désire, et qu'il accomplisse tous tes desseins !",
        "huile": "Laurier Noble (Victoire et Royauté)", "plantes": "Feuilles de Laurier séchées, Clous de girofle, Sauge",
        "zikr": "Ya Wahhab (Ô Donateur Suprême) — 14 fois",
        "mots_application": "Que les décrets de blocage soient annulés et remplacés par la réussite éclatante. Ce que mon cœur désire se matérialise dès aujourd'hui par la grâce céleste. Amen.",
        "moment": "Matin (Bain de Royauté)"
    },
    "Mavour (Inzan)": {
        "ref": "Mavour (ALBUS)", 
        "nature": "Bénéfique", 
        "txt": "Sagesse profonde, illumination spirituelle, paix intérieure, pureté de l'esprit.",
        "psaume": "Psaume 119", "verset": "Verset 105", "texte_biblique": "Ta parole est une lampe à mes pieds, et une lumière sur mon sentier.",
        "huile": "Encens d'Oliban (Haute vibration)", "plantes": "Résine d'oliban, Camomille matricaire, Jasmin",
        "zikr": "Ya Alim (Ô Omniscient) — 150 fois",
        "mots_application": "Que le voile de l'illusion soit levé. Donne-moi la sagesse des anciens pour guider mes pas et préserver ma maison de tout trouble. Amen.",
        "moment": "Soir au coucher (Méditation)"
    },
    "Lomara (Lamora)": {
        "ref": "Lomara Blen (RUBEUS)", 
        "nature": "Mauvais", 
        "txt": "Retour à l'envoyeur destructeur, briser les mauvais sorts immédiatement, combat occulte.",
        "psaume": "Psaume 35", "verset": "Verset 1", "texte_biblique": "Éternel ! Attaque ceux qui m'attaquent, combats ceux qui me combattent !",
        "huile": "Cannelle Écorce (Feu purificateur)", "plantes": "Feuilles de Moutarde, Piment de Cayenne (pincée), Ortie",
        "zikr": "Ya Jabbar (Ô Contraignant Suprême) — 206 fois",
        "mots_application": "Que les flèches mystiques tirées contre moi fassent demi-tour à cet instant précis. Que le feu théurgique consume mes oppresseurs. Amen.",
        "moment": "Soir (Bain de choc — Ne pas s'essuyer)"
    },
    "Nouhou-Koro (Mangoussi)": {
        "ref": "Nouhou-Koro (TRISTITIA)", 
        "nature": "Mauvais", 
        "txt": "Déracinement de la mélancolie, transmutation des épreuves familiales en joies, ancrage spirituel.",
        "psaume": "Psaume 30", "verset": "Verset 12", "texte_biblique": "Tu as changé mon deuil en allégresse, tu as délié mon sac, et tu m'as ceint de joie.",
        "huile": "Citronnelle (Purification des miasmes)", "plantes": "Tiges de citronnelle fraîche, Lavande, Thym sauvage",
        "zikr": "Ya Latif (Ô Doux / Bienveillant) — 129 fois",
        "mots_application": "Que toute lourdeur héritée ou projetée quitte mes corps subtils. Transforme mes larmes en triomphes spirituels et matériels. Amen.",
        "moment": "Soir (Déracinement)"
    },
    "Kalalahou (Kallaloua)": {
        "ref": "Kalalahou (CONIUNCTIO)", 
        "nature": "Bénéfique", 
        "txt": "Sceller des partenariats commerciaux, mariage stable, retour d'affection, réconciliation.",
        "psaume": "Psaume 133", "verset": "Verset 1", "texte_biblique": "Voici, qu'il est agréable, qu'il est doux pour des frères de demeurer ensemble !",
        "huile": "Ylang-Ylang (Harmonie relationnelle)", "plantes": "Fleurs de jasmin, Pétales de Rose rouge, Coriandre",
        "zikr": "Ya Wadoud (Ô Aimant) — 20 fois",
        "mots_application": "Que l'harmonie et l'amour inconditionnel soient ancrés entre [Nom de la personne] et moi. Que nos cœurs vibrent à l'unisson. Amen.",
        "moment": "Matin (Alliances)"
    },
    "Massa Solomane (Salomon)": {
        "ref": "Massa Solomane (PUELLA)", 
        "nature": "Bénéfique", 
        "txt": "Faveur auprès des femmes, charme commercial, esthétique, paix, diplomatie.",
        "psaume": "Psaume 45", "verset": "Verset 2", "texte_biblique": "Des paroles pleines de charme bouillonnent dans mon cœur. Je dis : Mon œuvre est pour le roi !",
        "huile": "Géranium Bourbon (Beauté et magnétisme)", "plantes": "Feuilles de Géranium, Verveine odorante, Reine-des-prés",
        "zikr": "Ya Jamil (Ô Beau) — 83 fois",
        "mots_application": "Que la grâce du Roi Salomon enveloppe ma parole. Que toute personne m'écoutant accorde sa faveur à mes requêtes. Amen.",
        "moment": "Matin avant les rendez-vous"
    },
    "Allou Badra (Badra)": {
        "ref": "Allou Badra (PUER)", 
        "nature": "Bénéfique (Ambivalent)", 
        "txt": "Force morale invincible, courage physique, gagner un procès difficile, protection routière.",
        "psaume": "Psaume 144", "verset": "Verset 1", "texte_biblique": "Béni soit l'Éternel, mon rocher, qui exerce mes mains au combat, mes doigts à la bataille !",
        "huile": "Gingembre Bleu (Vigueur et feu)", "plantes": "Racines de gingembre frais râpé, Poivre noir en grains, Romarin",
        "zikr": "Ya Qawiyyou (Ô Fort Invincible) — 116 fois",
        "mots_application": "Aucun piège tendu, aucun complot ourdi ne pourra ébranler ma marche. Je marche en vainqueur protégé par le bouclier du Très-Haut. Amen.",
        "moment": "Matin (Action)"
    },
    "Adama-Lomara (Al hassan)": {
        "ref": "Adama-Lomara (CAUDA DRACONIS)", 
        "nature": "Très Mauvais", 
        "txt": "Coupure radicale de liens toxiques, briser les dettes, nettoyage karmique en profondeur.",
        "psaume": "Psaume 18", "verset": "Verset 38", "texte_biblique": "Je les brise, et ils ne peuvent se relever ; ils tombent sous mes pieds.",
        "huile": "Clou de Girofle (Destruction de l'ombre)", "plantes": "Clous de girofle entiers, Feuille de tabac (ou sauge blanche), Sauge",
        "zikr": "Ya Moumit (Ô Celui qui fait mourir le mal) — 490 fois",
        "mots_application": "Je déracine et coupe définitivement tout lien occulte, toute dette karmique ou matérielle qui entrave mon évolution. C'est fait. Amen.",
        "moment": "Soir (Coupure nette — Ne pas s'essuyer)"
    },
    "Tontigui (Garia)": {
        "ref": "Tontigui (POPULUS)", 
        "nature": "Bénéfique", 
        "txt": "Protection blindée contre les calomnies de la foule, rumeurs et ennemis cachés du public.",
        "psaume": "Psaume 91", "verset": "Verset 11", "texte_biblique": "Car il ordonnera à ses anges de te garder dans toutes tes voies.",
        "huile": "Arbre à Thé (Bouclier défensif)", "plantes": "Feuilles d'Eucalyptus, Laurier sauce, Armoise",
        "zikr": "Ya Hafiz (Ô Protecteur) — 998 fois",
        "mots_application": "Que l'armée céleste dresse une muraille de feu autour de moi. Les complots de la foule glissent sur moi sans m'atteindre. Amen.",
        "moment": "Matin ou Soir"
    },
    "Mori-Zoumana (Ousmane)": {
        "ref": "Mori-Zoumana (LAETITIA)", 
        "nature": "Bénéfique", 
        "txt": "Joie de vivre spontanée, grands bonheurs à venir, événements heureux, chance pure.",
        "psaume": "Psaume 100", "verset": "Verset 2", "texte_biblique": "Servez l'Éternel avec joie, venez avec allégresse en sa présence !",
        "huile": "Pamplemousse (Énergie de joie)", "plantes": "Menthe, Pétales de Tournesol, Lavande",
        "zikr": "Ya Latif (Ô Bienveillant) — 129 fois",
        "mots_application": "Que l'allégresse remplace toute tristesse. J'accueille la bénédiction divine qui enrichit et ne se fait suivre d'aucun chagrin. Amen.",
        "moment": "Matin"
    },
    "Mangossi (Massa Solo)": {
        "ref": "Mangossi (CARCER)", 
        "nature": "Mauvais", 
        "txt": "Libération des prisons matérielles, des blocages juridiques majeurs et des dettes étouffantes.",
        "psaume": "Psaume 142", "verset": "Verset 8", "texte_biblique": "Tire mon âme de sa prison, afin que je célèbre ton nom !",
        "huile": "Cyprès de Provence (Libération des chaînes)", "plantes": "Feuilles de lierre, Racine de valériane, Romarin",
        "zikr": "Ya Moukhrij (Ô Celui qui fait sortir) — 201 fois",
        "mots_application": "Brise les verrous de la stagnation. Fais-moi sortir immédiatement de l'enfermement financier et professionnel. Je suis libre. Amen.",
        "moment": "Soir (Bain de Libération)"
    },
    "Moussa (Mahamadou)": {
        "ref": "Mahamadou (ou Moussa)", 
        "nature": "Neutre", 
        "txt": "Petite chance rapide, déblocage urgent d'une situation en moins de 24 heures.",
        "psaume": "Psaume 4", "verset": "Verset 7", "texte_biblique": "Fais lever sur nous la lumière de ta face, ô Éternel !",
        "huile": "Orange Douce", "plantes": "Citronnelle, Menthe, Cannelle",
        "zikr": "Ya Sari'u (Ô Rapide) — 202 fois",
        "mots_application": "Que la lumière balaye l'obscurité instantanément. Que le déblocage demandé se manifeste à ce moment précis. Amen.",
        "moment": "Matin"
    }
}

MAISONS = {
    1: "Maison de l'Auteur (État présent)", 2: "Maison des Biens (Finances)", 
    3: "Maison de l'Entourage (Nouvelles)", 4: "Maison du Patrimoine (Foyer)",
    5: "Maison des Enfants (Plaisirs/Chance)", 6: "Maison des Malaises (Obstacles subis)", 
    7: "Maison de l'Union (Contrats/Conjoint)", 8: "Maison de la Mort (Transformations/Crises)",
    9: "Maison des Voyages (Spiritualité)", 10: "Maison du Pouvoir (Carrière)", 
    11: "Maison des Appuis (Soutiens/Amis)", 12: "Maison des Obstacles (Ennemis cachés)",
    13: "Maison du Résultat (Conclusion)", 14: "Maison des Conséquences (Futur proche)", 
    15: "Maison de la Clarté (Témoin du thème)", 16: "Maison de la Sentence (Décret final)"
}

# ==============================================================================
# INTERFACE STREAMLIT SMART
# ==============================================================================
st.title("🔮 Grimoire Géomantique & Théurgique Interactif")
st.write("Interface sacrée pour la génération automatique de vos Nassis et rituels psalmadiques.")

with st.sidebar:
    st.header("🔐 Authentification")
    u_id = st.text_input("Identifiant")
    u_pw = st.text_input("Mot de passe", type="password")

if u_id == ID_SECRET and u_pw == MDP_SECRET:
    st.success("🔓 Temple théurgique ouvert.")
    
    # Guide du protocole de fabrication
    st.header("📜 LE PROTOCOLE DU NASSI (Étape par Étape)")
    with st.expander("👉 Cliquez ici pour voir la méthode stricte de préparation", expanded=False):
        st.markdown("""
        ### 🧪 Comment préparer votre eau sacrée (Nassi) :
        1. **Écriture Sacrée** : Écrivez sur une tablette en bois propre (ou une feuille blanche) le **Psaume** et le **Verset Clé** indiqués dans votre thème à l'aide d'une encre calligraphique traditionnelle ou pure.
        2. **Le Lavage** : Lavez la tablette ou la feuille avec de l'eau de source pure (ou eau de pluie) pour en récolter l'encre chargée. Versez cette eau sacrée dans un récipient propre. C'est votre **Nassi de base**.
        3. **L'Infusion des Plantes** : Faites bouillir les **plantes aromatiques** spécifiques à la maison ciblée dans une marmite d'eau pure, filtrez, puis mélangez cette infusion avec votre Nassi.
        4. **Le Scellage par l'Huile** : Ajoutez exactement **3 à 7 gouttes de l'Huile Essentielle** prescrite dans l'eau de votre bain.
        5. **La Consécration par le Zikr** : Asseyez-vous face à l'Est, récitez le **Zikr (Le Nom Divin)** au nombre exact de fois indiqué, puis prononcez à haute voix les **Mots d'Application** au-dessus de l'eau.
        6. **Le Bain** : Lavez-vous avec cette eau au moment opportun indiqué (Matin ou Soir). *Note pour les figures de nature 'Mauvaise' : ne pas s'essuyer après le bain, laissez sécher à l'air libre pour fixer le bouclier.*
        """)
    
    st.header("📋 Configuration Actuelle de votre Thème")
    st.info("Modifiez les figures ci-dessous en fonction de votre tracé géomantique actuel.")
    
    col1, col2, col3, col4 = st.columns(4)
    options = list(DATA.keys())
    
    # Thème dynamique préconfiguré selon vos données
    def_val = [
        "Bila (Seydiou)", "Adama", "Mahamadou (Maldiou)", "Idrissa",
        "Yousouf (Issa/Nouhou)", "Mavour (Inzan)", "Lomara (Lamora)", "Nouhou-Koro (Mangoussi)",
        "Kalalahou (Kallaloua)", "Massa Solomane (Salomon)", "Allou Badra (Badra)", "Yousouf (Issa/Nouhou)",
        "Adama-Lomara (Al hassan)", "Tontigui (Garia)", "Mori-Zoumana (Ousmane)", "Moussa (Mahamadou)"
    ]

    choix_utilisateur = {}
    for i in range(1, 17):
        current_col = [col1, col2, col3, col4][(i-1)%4]
        with current_col:
            choix_utilisateur[i] = st.selectbox(f"🏠 M {i} : {MAISONS[i]}", options, index=options.index(def_val[i-1]))

    st.markdown("---")
    st.header("📖 ANALYSE ET PROTOCOLES DE VOS 16 MAISONS")
    
    for m, fig in choix_utilisateur.items():
        info = DATA[fig]
        
        # Style d'affichage selon le tempérament de la figure
        if "Mauvais" in info["nature"]:
            titre_boite = f"🛑 MAISON {m} ({MAISONS[m]}) — {fig} [ALERTE OCCULTE]"
        else:
            titre_boite = f"✨ MAISON {m} ({MAISONS[m]}) — {fig} [COURANT LUMINEUX]"
            
        with st.expander(titre_boite):
            tabs = st.tabs(["📊 Diagnostic", "🧪 Recette du Nassi & Plantes", "📿 Zikr & Mots d'Application"])
            
            with tabs[0]:
                st.markdown(f"**Figure Géomantique :** {info['ref']}")
                st.markdown(f"**Influence vibratoire :** `{info['nature'].upper()}`")
                st.markdown(f"**Impact temporel :** {info['txt']}")
                
            with tabs[1]:
                st.markdown(f"### 🌿 Composants Organiques & Huiles")
                st.markdown(f"* **Huile Essentielle de Scellage :** {info['huile']}")
                st.markdown(f"* **Plantes Aromatiques d'Infusion :** {info['plantes']}")
                st.markdown(f"* **Moment du Bain :** `{info['moment']}`")
                st.markdown(f"---")
                st.markdown(f"### 📜 Écritures pour le Nassi")
                st.info(f"✒️ **À inscrire sur le support :** {info['psaume']} ({info['verset']})")
                st.write(f"👉 *\"{info['texte_biblique']}\"*")
                
            with tabs[2]:
                st.markdown(f"### 📿 Activation Spirituelle")
                st.warning(f"**Zikr Théurgique :** {info['zikr']}")
                st.markdown(f"### 🗣️ Mots d'Application Essentiels :")
                st.success(f"\"{info['mots_application']}\"")

else:
    st.warning("🔒 Saisissez vos identifiants secrets de Théurge dans le panneau latéral pour lever le voile sur le grimoire.")
