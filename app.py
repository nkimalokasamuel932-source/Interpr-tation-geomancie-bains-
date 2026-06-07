import streamlit as st
import random

# 1. Configuration de la page
st.set_page_config(page_title="Système Expert Tourab & Ramrou", page_icon="🔮", layout="wide")

# =====================================================================
# BASE DE DONNÉES ENRICHIE (Dictionnaire Théurgique & Traditionnel)
# =====================================================================
DICTIONNAIRE_FIGURES = {
    "1.1.1.1": {
        "nom_arabe": "Hibrahim", "nom_bambara": "Lahiya", "nom_latin": "Via",
        "nature": "Feu (Instable / Route)", "temps": "Présent / Début du cheminement",
        "signification": "Le Mouvement, la Route, l'Instabilité. Flux constants, déplacements nécessaires, déblocage des visas, accouchement facile.",
        "psaume_nom": "Psaume 120", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.7) du Psaume 120.",
        "verset_biblique": "Psaume 121:8 — 'L'Éternel gardera ton départ et ton arrivée...'",
        "texte_salomonique": "5e Pentacle de la Lune — Contre les barrières et pour voyager en sécurité.",
        "encre": "Encre d'argent ou bleu clair (eau de coco pure ou eau de puits).",
        "parfum": "Musc Blanc léger ou essence de Lotus.", "huiles_essentielles": "Menthe Poivrée ou Citronnelle.",
        "plantes": "Feuilles de Citronnelle fraîches et Feuilles de Palmier.", "encens": "Camphre naturel.",
        "moment": "Lundi matin au lever du soleil.", "saraka": "Partage de fruits ou de friandises à des enfants."
    },
    "1.1.1.2": {
        "nom_arabe": "Laoussana", "nom_bambara": "Janfa Almamy", "nom_latin": "Puella",
        "nature": "Eau (Hésitation / Beauté)", "temps": "Passé proche",
        "signification": "L'Hésitation, la Beauté, les Douces pensées. Mariage, séduction, retour d'affection.",
        "psaume_nom": "Psaume 119 (Aleph)", "cle_psaume": "Écrire le premier verset (V.1) et le huitième verset (V.8) du Psaume 119.",
        "verset_biblique": "Cantique des Cantiques 4:7 — 'Tu es toute belle, mon amie...'",
        "texte_salomonique": "2e Pentacle de Vénus — Pour obtenir la grâce, l'amour et les faveurs.",
        "encre": "Encre rose ou encre traditionnelle parfumée à l'eau de rose.",
        "parfum": "Musc Blanc ou Jasmin.", "huiles_essentielles": "Palmarosa ou Géranium Rosat.",
        "plantes": "Fleurs de Jasmin ou de Lavande infusées dans du Lait frais.", "encens": "Santal Blanc.",
        "moment": "Vendredi matin à l'aube.", "saraka": "Donner du lait frais ou des objets blancs à des pairs."
    },
    "1.2.1.1": {
        "nom_arabe": "Garia", "nom_bambara": "Madi", "nom_latin": "Fortuna Major",
        "nature": "Feu / Air (Succès royal)", "temps": "Futur proche / Immédiat",
        "signification": "La Grande Chance, la Protection, le Succès durable. Réussite totale, élévation.",
        "psaume_nom": "Psaume 91", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.16) du Psaume 91.",
        "verset_biblique": "Genèse 12:2 — 'Je ferai de toi une grande nation, et je te bénirai...'",
        "texte_salomonique": "1er Pentacle du Soleil — Face et Figure du Créateur.",
        "encre": "Encre Jaune Safranée (Vrai safran ou curcuma dans eau de rose. SANS SOUFRE).",
        "parfum": "Ambre pur ou Musc ambré.", "huiles_essentielles": "Encens Oliban ou Orange Douce.",
        "plantes": "Feuilles de Laurier noble et Feuilles de Basilic frais.", "encens": "Oliban pur en larmes.",
        "moment": "Dimanche matin (Charger 1h au soleil).", "saraka": "Préparer un grand repas pour les indigents."
    },
    "1.2.2.1": {
        "nom_arabe": "Solomana", "nom_bambara": "Souleymane", "nom_latin": "Carcer",
        "nature": "Terre (Blocage / Secret)", "temps": "Futur lointain",
        "signification": "La Chefferie, le Blocage, la Concentration. Autorité administrative, protection des secrets, litiges.",
        "psaume_nom": "Psaume 142", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.8) du Psaume 142.",
        "verset_biblique": "Isaïe 22:22 — 'Je mettrai sur son épaule la clé de la maison de David...'",
        "texte_salomonique": "7e Pentacle de Saturne — Pour commander aux puissances de l'ombre.",
        "encre": "Encre noire traditionnelle concentrée au noir de fumée.",
        "parfum": "Ambre Noir ou Huile de Cèdre.", "huiles_essentielles": "Bois de Santal ou Cèdre.",
        "plantes": "Feuilles de Cyprès ou de Lierre grimpant.", "encens": "Myrrhe brute.",
        "moment": "Samedi soir tard.", "saraka": "Offrir du cola fendu ou du pain à un gardien."
    },
    "1.2.1.2": {
        "nom_arabe": "Inza", "nom_bambara": "Insa", "nom_latin": "Amissio",
        "nature": "Air / Feu (Perte / Renoncement)", "temps": "Futur",
        "signification": "La Perte, la Fatigue, le Renoncement. Stopper les fuites d'argent et contrer les vols mystiques.",
        "psaume_nom": "Psaume 102", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.29) du Psaume 102.",
        "verset_biblique": "Joël 2:25 — 'Je vous remplacerai les années qu'ont dévorées la sauterelle.'",
        "texte_salomonique": "5e Pentacle de Vénus — Invite à l'amour et au respect instantané.",
        "encre": "Encre marron terre ou encre traditionnelle à l'eau de source.",
        "parfum": "Ambre précieux.", "huiles_essentielles": "Lavande Vraie ou Sauge Sclarée.",
        "plantes": "Feuilles de Sauge et de Thym frais.", "encens": "Muscade râpée.",
        "moment": "Vendredi soir après le coucher du soleil.", "saraka": "Aumône de pièces de monnaie pour conjurer la perte."
    },
    "1.2.2.2": {
        "nom_arabe": "Adama", "nom_bambara": "Adama", "nom_latin": "Laetitia",
        "nature": "Feu (Joie / Élévation)", "temps": "Futur proche / Immédiat",
        "signification": "La Joie, l'Élévation, la Chance. Fête, prospérité, expansion financière, examens.",
        "psaume_nom": "Psaume 4", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.9) du Psaume 4.",
        "verset_biblique": "Néhémie 8:10 — 'Ne vous affligez pas, car la joie de l'Éternel sera votre force.'",
        "texte_salomonique": "2e Pentacle de Jupiter — Pour acquérir la gloire et les honneurs.",
        "encre": "Encre bleue céleste mélangée à du musc blanc.",
        "parfum": "Musc Blanc pur.", "huiles_essentielles": "Bergamote ou Orange Douce.",
        "plantes": "Feuilles de Menthe poivrée fraîches et Fleurs de Camomille.", "encens": "Résine de Benjoin.",
        "moment": "Jeudi matin à l'aube.", "saraka": "Donner 100 colas blanches ou de la viande de mouton blanc."
    },
    "1.1.2.1": {
        "nom_arabe": "Youssouf", "nom_bambara": "Sediou", "nom_latin": "Puer",
        "nature": "Feu / Métal (Combat / Force)", "temps": "Passé",
        "signification": "L'Action, la Force masculine, le Combat. Protection blindée, destruction des complots.",
        "psaume_nom": "Psaume 35", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.28) du Psaume 35.",
        "verset_biblique": "Exode 15:3 — 'L'Éternel est un vaillant guerrier...'",
        "texte_salomonique": "2e Pentacle de Mars — Contre les maladies, plaies et esprits rebelles.",
        "encre": "Encre Rouge (pointe de poudre de piment ou de gingembre).",
        "parfum": "Musc Noir ou Patchouli.", "huiles_essentielles": "Poivre Noir ou Gingembre.",
        "plantes": "Feuilles de Tabac, de pissenlit et d'Ortie.", "encens": "Sang de Dragon.",
        "moment": "Mardi soir tard.", "saraka": "Aliments épicés ou objets métalliques."
    },
    "1.1.2.2": {
        "nom_arabe": "Allahou talla", "nom_bambara": "Alou", "nom_latin": "Fortuna Minor",
        "nature": "Air / Feu (Secours rapide)", "temps": "Futur",
        "signification": "Le Succès rapide, l'Opportunité urgente. Protection sur les routes, secours immédiat.",
        "psaume_nom": "Psaume 121", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.8) du Psaume 121.",
        "verset_biblique": "Psaume 46:2 — 'Dieu est pour nous un refuge et un appui...'",
        "texte_salomonique": "4e Pentacle du Soleil — Pour acquérir une renommée ou un secours céleste.",
        "encre": "Encre Orange ou Jaune vif (Curcuma dans eau bénite).",
        "parfum": "Musc Ambre.", "huiles_essentielles": "Orange Douce.",
        "plantes": "Écorces d'Orange séchées et feuilles de Romarin.", "encens": "Oliban pur en larmes.",
        "moment": "À l'aube un jeudi ou un dimanche.", "saraka": "Partager des beignets ou de la nourriture légère à l'aube."
    },
    "2.1.1.1": {
        "nom_arabe": "Maldiou", "nom_bambara": "Mahdi", "nom_latin": "Caput Draconis",
        "nature": "Terre (Stabilité / Enracinement)", "temps": "Passé",
        "signification": "La Réalisation, la Stabilité, l'Enracinement. Projets immobiliers, investissements durables.",
        "psaume_nom": "Psaume 128", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.6) du Psaume 128.",
        "verset_biblique": "Exode 20:12 — 'Honore ton père et ta mère...'",
        "texte_salomonique": "1er Pentacle de la Terre — Pour donner force aux fondations.",
        "encre": "Encre brune mélangée à une pincée de terre fine et fertile de forêt.",
        "parfum": "Ambre lourd ou Vétiver.", "huiles_essentielles": "Vétiver ou Bois de Santal.",
        "plantes": "Feuilles de Chêne ou de Ficus.", "encens": "Myrrhe.",
        "moment": "Mercredi ou samedi matin.", "saraka": "Faire une offrande ou un cadeau direct à votre mère."
    },
    "2.1.1.2": {
        "nom_arabe": "Badra", "nom_bambara": "Oumar", "nom_latin": "Conjunctio",
        "nature": "Air (Union / Échanges)", "temps": "Futur proche",
        "signification": "L'Union, le Contrat, l'Association. Rencontres majeures, signatures, mariages.",
        "psaume_nom": "Psaume 133", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.3).",
        "verset_biblique": "Ruth 1:16 — 'Où tu iras j'irai, où tu demeureras je demeurerai...'",
        "texte_salomonique": "4e Pentacle de Mercure — Pour acquérir l'éloquence et l'assimilation.",
        "encre": "Encre Jaune Pâle ou bicolore (safran + noir).",
        "parfum": "Musc précieux à la Lavande.", "huiles_essentielles": "Patchouli ou Lavande.",
        "plantes": "Brins de Lavande et feuilles de Romarin.", "encens": "Fleurs de Lavande.",
        "moment": "Mercredi matin au lever du soleil.", "saraka": "Offrir des céréales (fonio, riz) à des pairs un mercredi."
    },
    "2.1.2.1": {
        "nom_arabe": "Ousmane", "nom_bambara": "Mori Zoumana", "nom_latin": "Acquisitio",
        "nature": "Eau (Abondance / Fleuve)", "temps": "Futur proche / Immédiat",
        "signification": "Le Gain, l'Abondance financière. Réussite commerciale, profits en hausse, héritages.",
        "psaume_nom": "Psaume 112", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.10) du Psaume 112.",
        "verset_biblique": "Deutéronome 28:12 — 'L'Éternel t'ouvrira son bon trésor...'",
        "texte_salomonique": "6e Pentacle de Jupiter — Protège et assure une immense fortune.",
        "encre": "Encre Verte ou Violette royale charged d'infusion de menthe.",
        "parfum": "Ambre Gris précieux.", "huiles_essentielles": "Cannelle Écorce ou Oliban.",
        "plantes": "Feuilles de Trèfle et une bonne pincée de Poudre de Cannelle.", "encens": "Benjoin et Cannelle.",
        "moment": "Jeudi matin à l'aube.", "saraka": "Faire un don financier important dans un lieu de culte."
    },
    "2.1.2.2": {
        "nom_arabe": "Lamora", "nom_bambara": "Tounka", "nom_latin": "Rubeus",
        "nature": "Feu (Passion / Rouge)", "temps": "Futur proche",
        "signification": "La Passion, la Colère, le Magnétisme. Canaliser l'agressivité ou raviver le couple.",
        "psaume_nom": "Psaume 29", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.11).",
        "verset_biblique": "Cantique des Cantiques 8:6 — 'Mets-moi comme un sceau sur ton cœur...'",
        "texte_salomonique": "4e Pentacle de Macau — Pour la victoire finale et apaiser l'agressivité.",
        "encre": "Encre Rouge Vif (jus de grenade ou de betterave).",
        "parfum": "Musc Rouge (Musc Ghazal).", "huiles_essentielles": "Laurier Noble ou Géranium.",
        "plantes": "Pétales de Rose rouge et feuilles de Verveine.", "encens": "Clous de Girofle écrasés.",
        "moment": "Mardi soir.", "saraka": "Offrir du cola rouge ou des fruits rouges."
    },
    "2.2.1.1": {
        "nom_arabe": "Nouhou", "nom_bambara": "Gounadyan", "nom_latin": "Cauda Draconis",
        "nature": "Terre / Sortie (Exorcisme)", "temps": "Futur",
        "signification": "La Sortie, l'Exorcisme, la Rupture. Briser les mauvais sorts, liens toxiques et blocages.",
        "psaume_nom": "Psaume 59", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.18) du Psaume 59.",
        "verset_biblique": "Psaume 68:2 — 'Dieu se lève, ses ennemis se dispersent...'",
        "texte_salomonique": "6e Pentacle de Saturne — Pour faire fuir les démons et annuler les sorts.",
        "encre": "Encre Noire brute au noir de fumée, pure.",
        "parfum": "Huile de Cade (pas de parfum doux).", "huiles_essentielles": "Arbre à thé ou Eucalyptus.",
        "plantes": "Feuilles d'Eucalyptus et d'Armoise.", "encens": "Feuilles de Laurier séchées.",
        "moment": "Samedi soir tard à l'extérieur.", "saraka": "Sacrifice d'un vieil habit ou nettoyage bénévole."
    },
    "2.2.1.2": {
        "nom_arabe": "Idriss", "nom_bambara": "Mori lani", "nom_latin": "Albus",
        "nature": "Eau / Sagesse (Blancheur)", "temps": "Futur proche / Immédiat",
        "signification": "La Sagesse, la Clarté blanche, la Paix. Révélation de la vérité, éclat de l'aura.",
        "psaume_nom": "Psaume 119 (Beth)", "cle_psaume": "Écrire le neuvième verset (V.9) et le seizième verset (V.16) du Psaume 119.",
        "verset_biblique": "Isaïe 1:18 — 'Si vos péchés sont comme le cramoisi, ils deviendront blancs...'",
        "texte_salomonique": "2e Pentacle de Mercure — Pour l'illumination et comprendre les secrets.",
        "encre": "Encre Blanche (eau chargée de camphre naturel et craie blanche).",
        "parfum": "Musc Blanc pur à 100 %.", "huiles_essentielles": "Bois de Santal ou Lavande.",
        "plantes": "Feuilles de Lys ou pétales de Rose blanche, Camphre.", "encens": "Santal Blanc.",
        "moment": "Mercredi matin à l'aube.", "saraka": "Donner du savon, du sel ou de l'eau claire à un démuni."
    },
    "2.2.2.1": {
        "nom_arabe": "Ayoub", "nom_bambara": "Mangoussi", "nom_latin": "Tristitia",
        "nature": "Terre (La Tombe / Tristesse)", "temps": "Futur proche / Immédiat",
        "signification": "La Reconstruction, la Consolation. Surmonter la mélancolie, un deuil ou une faillite.",
        "psaume_nom": "Psaume 40", "cle_psaume": "Écrire le deuxième verset (V.2) et le dernier verset (V.18).",
        "verset_biblique": "Isaïe 61:3 — 'Pour donner aux affligés un diadème au lieu de la cendre...'",
        "texte_salomonique": "5e Pentacle de Saturne — Pour consoler les cœurs tristes et repousser la ruine.",
        "encre": "Encre Bleu Nuit ou Noire profonde.",
        "parfum": "Ambre précieux ou Patchouli.", "huiles_essentielles": "Vétiver ou Cèdre.",
        "plantes": "Racines de Gingembre frais écrasées et aiguilles de Pin.", "encens": "Myrrhe ou Storax.",
        "moment": "Samedi soir.", "saraka": "Offrir des produits de la terre (tubercules) à des vieillards."
    },
    "2.2.2.2": {
        "nom_arabe": "Moussa", "nom_bambara": "Moussa", "nom_latin": "Populus",
        "nature": "Eau / Collectif (La Foule)", "temps": "Finition / Aboutissement complet",
        "signification": "La Foule, le Collectif, l'Audience. Attirer la clientèle en masse, influence publique.",
        "psaume_nom": "Psaume 47", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.10) du Psaume 47.",
        "verset_biblique": "Genèse 22:17 — 'Je multiplierai ta postérité, comme les étoiles du ciel...'",
        "texte_salomonique": "1er Pentacle de la Lune — Pour ouvrir toutes les portes closes.",
        "encre": "Encre Gris Perle chargée d'eau de pluie collectée à la pleine lune.",
        "parfum": "Musc Blanc ou essence de Lys.", "huiles_essentielles": "Lavande Vraie.",
        "plantes": "Feuilles de Persil frais et feuilles de Sauge.", "encens": "Benjoin blanc.",
        "moment": "Lundi (Lune Croissante).", "saraka": "Distribuer du pain ou des aliments de base à une foule."
    }
}

NOMS_MAISONS = [
    "M1 : Consultant / Tête / Feu", "M2 : Gains / Argent / Vent", "M3 : Entourage / Échanges / Eau", "M4 : Foyer / Patrimoine / Terre",
    "M5 : Amours / Enfants / Feu", "M6 : Blocages / Obstacles / Vent", "M7 : Conjoint / Associés / Eau", "M8 : Changements / Mort / Terre",
    "M9 : Voyages / Spiritualité / Feu", "M10 : Carrière / Honneurs / Vent", "M11 : Appuis / Espoirs / Eau", "M12 : Épreuves / Secrets / Terre",
    "M13 : Témoin Droit (Le Passé)", "M14 : Témoin Gauche (Le Futur)", "M15 : Le Juge (Le Verdict)", "M16 : La Sentence (L'Issue)"
]

# =====================================================================
# UTILITAIRES LOGIQUES
# =====================================================================
def identifier_figure(liste_points):
    cle = ".".join(map(str, liste_points))
    return DICTIONNAIRE_FIGURES.get(cle, {"nom_arabe": "Inconnue", "signification": "-"})

def additionner_figures(fig_a, fig_b):
    return [2 if (fig_a[i] + fig_b[i]) in [2, 4] else 1 for i in range(4)]

def calculer_cle_ecriture(psaume_str):
    chiffres = [int(c) for c in psaume_str if c.isdigit()]
    total = sum(chiffres) if chiffres else 7
    while total > 9: 
        total = sum(int(c) for c in str(total))
    return 7 if total in [1, 4, 8] else (9 if total in [3, 6, 9] else 3)

def format_visuel_text(liste_points):
    return "\n".join(["●   ●" if pt == 2 else "  ●  " for pt in liste_points])

# =====================================================================
# INTERFACE UTILISATEUR STREAMLIT
# =====================================================================
st.title("🔮 Plateforme Consolidée de Géomancie Traditionnelle")
st.write("Moteur d'analyse unifiée raccordé aux prescriptions immuables du Ramrou.")

mode_saisie = st.radio("Sélectionnez le mode d'entrée du Thème :", ["🎲 Tirage par Tapotements (Le Jeu)", "🛠️ Sélection Manuelle des Mères"])

m1, m2, m3, m4 = None, None, None, None

if mode_saisie == "🎲 Tirage par Tapotements (Le Jeu)":
    st.markdown("### 🖐️ Générateur de Lignes (Frapper la Terre)")
    st.write("Cliquez sur chaque bouton pour générer le nombre de traits. L'application calculera automatiquement le nombre pair ou impair.")
    
    mères_generes = []
    for m in range(1, 5):
        st.write(f"**Pour la Maison Mère {m} :**")
        cols = st.columns(4)
        lignes_mere = []
        for l in range(4):
            with cols[l]:
                points = st.number_input(f"Ligne {l+1}", min_value=1, max_value=50, value=random.randint(10, 30), key=f"tirage_{m}_{l}")
                lignes_mere.append(1 if points % 2 != 0 else 2)
        mères_generes.append(lignes_mere)
    
    m1, m2, m3, m4 = mères_generes[0], mères_generes[1], mères_generes[2], mères_generes[3]

else:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("**Maison I (M1)**")
        m1 = [st.selectbox(f"L{i+1}", [1, 2], key=f"m1_{i}") for i in range(4)]
    with col2:
        st.write("**Maison II (M2)**")
        m2 = [st.selectbox(f"L{i+1}", [1, 2], key=f"m2_{i}") for i in range(4)]
    with col3:
        st.write("**Maison III (M3)**")
        m3 = [st.selectbox(f"L{i+1}", [1, 2], key=f"m3_{i}") for i in range(4)]
    with col4:
        st.write("**Maison IV (M4)**")
        m4 = [st.selectbox(f"L{i+1}", [1, 2], key=f"m4_{i}") for i in range(4)]

# =====================================================================
# ZONE DE CALCUL ET INTERPRÉTATION CONTEXTUELLE
# =====================================================================
if st.button("🔮 ANALYSER LE RAMROU ET CHARGER LES REMÈDES"):
    # Dérivation mathématique exacte des 16 maisons
    m5 = [m1[0], m2[0], m3[0], m4[0]]
    m6 = [m1[1], m2[1], m3[1], m4[1]]
    m7 = [m1[2], m2[2], m3[2], m4[2]]
    m8 = [m1[3], m2[3], m3[3], m4[3]]
    
    m9 = additionner_figures(m1, m2)
    m10 = additionner_figures(m3, m4)
    m11 = additionner_figures(m5, m6)
    m12 = additionner_figures(m7, m8)
    
    m13 = additionner_figures(m9, m10)
    m14 = additionner_figures(m11, m12)
    m15 = additionner_figures(m13, m14)
    m16 = additionner_figures(m1, m15)

    theme_complet = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16]
    
    fig_m1 = identifier_figure(m1)
    juge = identifier_figure(m15)
    sentence = identifier_figure(m16)

    # 1. ANALYSE DU THEME ET ORIENTATION TEMPORELLE
    st.header("📖 Orientation et Nature du Thème")
    st.markdown(f"**Le Consultant (M1) :** Vous êtes sous l'égide de la figure **{fig_m1['nom_arabe']}** (*{fig_m1['nom_latin']}* / *{fig_m1['nom_bambara']}*).")
    st.write(f"🧬 **Nature :** {fig_m1['nature']} | ⏳ **Temps dominant :** {fig_m1['temps']}")
    st.write(f"📝 **Signification de base :** {fig_m1['signification']}")

    # 2. DETECTEUR AUTOMATIQUE DE PASSATIONS
    st.header("🔄 Analyse des Passations (Circulation des Énergies)")
    passations = {}
    for idx_a in range(16):
        nom_a = identifier_figure(theme_complet[idx_a])['nom_arabe']
        for idx_b in range(idx_a + 1, 16):
            nom_b = identifier_figure(theme_complet[idx_b])['nom_arabe']
            if nom_a == nom_b:
                if nom_a not in passations: passations[nom_a] = []
                passations[nom_a].append((idx_a, idx_b))

    if not passations:
        st.info("✨ Aucun doublon détecté. Chaque maison conserve sa pureté individuelle.")
    else:
        for fig_nom, occurrences in passations.items():
            for (mo, md) in occurrences:
                st.warning(f"🔁 La figure **{fig_nom}** se déplace de **{NOMS_MAISONS[mo]}** vers **{NOMS_MAISONS[md]}**.")
                st.caption(f"💡 *Lien invisible :* L'état ou l'enjeu lié à la première maison détermine l'issue de la seconde.")

    # 3. CONCLUSION SCELLÉE
    st.header("👑 Sceau de l'Issue (Maison 16)")
    st.error(f"**La Conclusion du thème est gouvernée par : {sentence['nom_arabe']}**\n\n📌 **Sentence finale :** {sentence['signification']}")

    # 4. AFFICHAGE DES CARTES DES 16 CASES
    st.header("📊 Cartographie du Thème")
    sections_maisons = [("Mères (1-4)", 0), ("Filles (5-8)", 4), ("Nièces (9-12)", 8), ("Tribunal (13-16)", 12)]
    for titre, start_idx in sections_maisons:
        st.subheader(titre)
        cols = st.columns(4)
        for i in range(4):
            curr_idx = start_idx + i
            fig_curr = identifier_figure(theme_complet[curr_idx])
            with cols[i]:
                st.markdown(f"**{NOMS_MAISONS[curr_idx].split(' : ')[0]}**")
                st.code(format_visuel_text(theme_complet[curr_idx]))
                st.markdown(f"✨ *{fig_curr['nom_arabe']}*")

    # =====================================================================
    # SANCTUARISATION ET CHARGEMENT DES REMÈDES FACTUELS (SANS MODIFICATION)
    # =====================================================================
    st.header("🛡️ Ordonnance Spirituelle & Prescriptions Sacrées")
    tab1, tab2, tab3 = st.tabs(["📝 Tracés d'Ardoise (Nassi)", "🧪 Ingrédients & Alchimie", "📦 Sacrifices (Saraka)"])
    
    n_juge = calculer_cle_ecriture(juge['psaume_nom'])
    n_sent = calculer_cle_ecriture(sentence['psaume_nom'])

    with tab1:
        st.subheader("📋 Quantités de tracé exactes basées sur le manuscrit")
        st.info(f"**Pour le Juge ({juge['nom_arabe']}) :** À tracer impérativement **{n_juge} fois**.\n\n* {juge['cle_psaume']}\n* {juge['verset_biblique']}\n* {juge['texte_salomonique']}")
        st.success(f"**Pour la Sentence ({sentence['nom_arabe']}) :** À tracer impérativement **{n_sent} fois**.\n\n* {sentence['cle_psaume']}\n* {sentence['verset_biblique']}\n* {sentence['texte_salomonique']}")

    with tab2:
        st.subheader("🧪 Éléments de composition pour le Bain")
        col_j, col_s = st.columns(2)
        with col_j:
            st.markdown(f"### Bain du Juge ({juge['nom_arabe']})")
            st.write(f"🎨 **Encre :** {juge['encre']}")
            st.write(f"🌿 **Plantes :** {juge['plantes']}")
            st.write(f"🧴 **Parfum & Huile :** {juge['parfum']} / {juge['huiles_essentielles']}")
            st.write(f"⏰ **Moment :** {juge['moment']}")
        with col_s:
            st.markdown(f"### Bain de l'Issue ({sentence['nom_arabe']})")
            st.write(f"🎨 **Encre :** {sentence['encre']}")
            st.write(f"🌿 **Plantes :** {sentence['plantes']}")
            st.write(f"🧴 **Parfum & Huile :** {sentence['parfum']} / {sentence['huiles_essentielles']}")
            st.write(f"⏰ **Moment :** {sentence['moment']}")

    with tab3:
        st.subheader("📦 Aumônes à distribuer pour stabiliser le thème")
        st.warning(f"**Sacrifice du Verdict (M15) :** {juge['saraka']}")
        st.error(f"**Sacrifice de l'Issue (M16) :** {sentence['saraka']}")
