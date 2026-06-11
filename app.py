import streamlit as st
from collections import defaultdict

# Configuration de la page
st.set_page_config(page_title="Système Théurgique Expert", page_icon="🔮", layout="wide")

# ==============================================================================
# ACCÈS SÉCURISÉS
# ==============================================================================
ID_SECRET = "theurge2026"
MDP_SECRET = "Salomon777"

# ==============================================================================
# MATRICE DES FIGURES AVEC LEURS CODES BINAIRES POUR LE CALCUL AUTOMATIQUE
# (1 = impair/un point, 2 = pair/deux points pour les 4 lignes : Tête, Poitrine, Ventre, Pied)
# ==============================================================================
DATA = {
    "Youssouf (Dianfa Almami)": {
        "ref": "Youssouf (Dianfa Almami)", "code": (1, 2, 1, 1), "nature": "Bénéfique", "element": "Feu", "direction": "Est",
        "txt": "Maison du demandeur par extension l'esprit, l'âme.",
        "psaume": "Psaume 20", "nb_ecriture": 7, "lecture_intégrale": "OUI (À lire entièrement à voix haute après le bain)",
        "verset": "Verset 5", "texte_biblique": "Qu'il te donne ce que ton cœur désire, et qu'il accomplisse tous tes desseins !",
        "huile": "Laurier Noble (Victoire et clarté spirituelle)", 
        "aromatiques": "Feuilles de Laurier sauce, Menthe poivrée fraîche, Safran (Colorant solaire)",
        "zikr": "Ya Wahhab (Ô Donateur Suprême) — 14 fois + Nom Salomonique : EHIEH ASHER EHIEH",
        "mots_application": "Que mon âme soit purifiée et que les intentions de ce thème reçoivent la clarté et le succès divin. Amen.", "moment": "Matin au lever"
    },
    "Adam (Adama)": {
        "ref": "Adam (Adama)", "code": (1, 1, 1, 1), "nature": "Bénéfique", "element": "Feu", "direction": "Est",
        "txt": "Maison des biens, des chances, des énergies positives et négatives.",
        "psaume": "Psaume 8", "nb_ecriture": 8, "lecture_intégrale": "OUI (À lire entièrement à voix haute après le bain)",
        "verset": "Verset 6", "texte_biblique": "Tu lui as donné l'empire sur les œuvres de tes mains, tu as tout mis sous ses pieds.",
        "huile": "Cèdre de l'Atlas (Ancrage et prospérité royale)", 
        "aromatiques": "Basilic sacré (Tulsi), Romarin officinal, Curcuma (Poudre d'Or)",
        "zikr": "Ya Rafi'u (Ô Celui qui élève) — 351 fois + Nom Salomonique : ADONAI MELEKH",
        "mots_application": "Que l'abondance matérielle, la chance et l'élévation financière s'installent durablement dans ma vie. Amen.", "moment": "Matin"
    },
    "Mahdiou (Malejou)": {
        "ref": "Mahdiou (Malejou)", "code": (1, 1, 1, 2), "nature": "Neutre", "element": "Vent", "direction": "Sud",
        "txt": "Maison de la famille, des voisins, des parents, des collègues, l'entourage proche.",
        "psaume": "Psaume 4", "nb_ecriture": 3, "lecture_intégrale": "OUI (À lire entièrement à voix haute après le bain)",
        "verset": "Verset 7", "texte_biblique": "Fais lever sur nous la lumière de ta face, ô Éternel !",
        "huile": "Orange Douce (Harmonie et joie relationnelle)", 
        "aromatiques": "Zestes d'Orange douce, Menthe douce, Coriandre, Écorce de Cannelle",
        "zikr": "Ya Nour (Ô Lumière) — 256 fois + Nom Salomonique : ELOHIM SABAOTH",
        "mots_application": "Que la concorde et la paix illuminent mes relations avec mon entourage et ma famille. Amen.", "moment": "Matin"
    },
    "Idriss (Albayada)": {
        "ref": "Idriss (Albayada)", "code": (2, 2, 1, 2), "nature": "Bénéfique", "element": "Eau", "direction": "Nord",
        "txt": "Maison du foyer, du pays, de l'autorité parentale.",
        "psaume": "Psaume 112", "nb_ecriture": 4, "lecture_intégrale": "OUI (À lire entièrement à voix haute après le bain)",
        "verset": "Verset 3", "texte_biblique": "Il a dans sa maison bien-être et richesse, et sa justice subsiste à jamais.",
        "huile": "Patchouli (Attraction terrestre et matérialisation)", 
        "aromatiques": "Bâtons de Cannelle concassés, Clous de Girofle entiers, Curcuma de Madagascar",
        "zikr": "Ya Razzaq (Ô Pourvoyeur) — 308 fois + Nom Salomonique : SHADDAI EL CHAI",
        "mots_application": "Que la stabilité, le bien-être et la richesse s'ancrent au cœur de mon foyer. Amen.", "moment": "Matin"
    },
    "Ibrahim (Târiki)": {
        "ref": "Ibrahim (Târiki)", "code": (1, 1, 2, 1), "nature": "Bénéfique", "element": "Eau", "direction": "Nord",
        "txt": "Maison des enfants et des nouvelles.",
        "psaume": "Psaume 100", "nb_ecriture": 5, "lecture_intégrale": "OUI (À lire entièrement à voix haute après le bain)",
        "verset": "Verset 2", "texte_biblique": "Servez l'Éternel avec joie, venez avec allégresse en sa présence !",
        "huile": "Pamplemousse (Énergie positive et renouveau)", 
        "aromatiques": "Verveine odorante, Citronnelle en tiges, Pistils de Safran",
        "zikr": "Ya Latif (Ô Doux) — 129 fois + Nom Salomonique : YHVH SABAOTH",
        "mots_application": "Que les nouvelles qui me parviennent apportent la joie, la réussite et l'allégresse. Amen.", "moment": "Matin"
    },
    "Issa (Ngansa)": {
        "ref": "Issa (Ngansa)", "code": (2, 2, 2, 2), "nature": "Neutre à Mauvais", "element": "Eau", "direction": "Nord",
        "txt": "Maison de la maladie, de la chose accomplie, des esclaves, du cheptel.",
        "psaume": "Psaume 51", "nb_ecriture": 1, "lecture_intégrale": "OUI (À lire entièrement à voix haute après le bain)",
        "verset": "Verset 12", "texte_biblique": "Ô Dieu ! crée en moi un cœur pur, renouvelle en moi un esprit bien disposé.",
        "huile": "Lavande Vraie (Purification absolue des corps subtils)", 
        "aromatiques": "Fleurs de Lavande séchées, Camomille matricaire, Poudre de Santal Blanc",
        "zikr": "Ya Chafi (Ô Guérisseur) — 391 fois + Nom Salomonique : ELOHIM GIBOR",
        "mots_application": "Purifie mon être de toute négativité, entrave ou influence maladive cachée. Amen.", "moment": "Soir"
    },
    "Oumar (Lomara)": {
        "ref": "Oumar (Lomara)", "code": (2, 1, 2, 2), "nature": "Mauvais", "element": "Vent", "direction": "Sud",
        "txt": "Maison des adversaires, du mariage, des époux.",
        "psaume": "Psaume 35", "nb_ecriture": 7, "lecture_intégrale": "OUI (À lire entièrement à voix haute après le bain)",
        "verset": "Verset 1", "texte_biblique": "Éternel ! Attaque ceux qui m'attaquent, combats ceux qui me combattent !",
        "huile": "Cannelle Écorce (Feu purificateur de combat)", 
        "aromatiques": "Poivre noir en grains, Thym fort, Ortie piquante, Gingembre rouge",
        "zikr": "Ya Jabbar (Ô Contraignant) — 206 fois + Nom Salomonique : ELOHIM GIBOR",
        "mots_application": "Que toute opposition, conflit ou rivalité se brise face à la justice divine. Amen.", "moment": "Soir (Ne pas s'essuyer)"
    },
    "Ayoube (Mankoussi)": {
        "ref": "Ayoube (Mankoussi)", "code": (2, 2, 2, 1), "nature": "Mauvais", "element": "Terre", "direction": "Ouest",
        "txt": "Maison de la mort, de l'angoisse, du malheur, de la peur, de la contrainte.",
        "psaume": "Psaume 142", "nb_ecriture": 9, "lecture_intégrale": "OUI (À lire entièrement à voix haute après le bain)",
        "verset": "Verset 8", "texte_biblique": "Tire mon âme de sa prison, afin que je célèbre ton nom !",
        "huile": "Cyprès de Provence (Libération et passage des blocages)", 
        "aromatiques": "Sauge officinale, Racine de Gingembre frais, Charbon béni",
        "zikr": "Ya Moukhrij (Ô Celui qui fait sortir) — 201 fois + Nom Salomonique : AGLA",
        "mots_application": "Je me libère des angoisses, des blocages et de toute forme d'enfermement matériel ou spirituel. Amen.", "moment": "Soir"
    },
    "Allahou talla (Kalalaw)": {
        "ref": "Allahou talla (Kalalaw)", "code": (1, 2, 2, 1), "nature": "Bénéfique", "element": "Feu", "direction": "Est",
        "txt": "Maison des déplacements, des voyages, de la mobilité, du dynamisme.",
        "psaume": "Psaume 133", "nb_ecriture": 3, "lecture_intégrale": "OUI (À lire entièrement à voix haute après le bain)",
        "verset": "Verset 1", "texte_biblique": "Voici, qu'il est agréable, qu'il est doux pour des frères de demeurer ensemble !",
        "huile": "Ylang-Ylang (Attraction, charisme et union)", 
        "aromatiques": "Pétales de Rose de Damas, Anis étoilé, Safran odorant",
        "zikr": "Ya Wadoud (Ô Aimant) — 20 fois + Nom Salomonique : EL GOLAH",
        "mots_application": "Que mes routes et mes déplacements créent des alliances heureuses et fructueuses. Amen.", "moment": "Matin"
    },
    "Souleymane (Mansa Solomani)": {
        "ref": "Souleymane (Mansa Solomani)", "code": (2, 1, 1, 2), "nature": "Bénéfique", "element": "Terre", "direction": "Ouest",
        "txt": "Maison du service, lieu de travail, maison de la royauté, de l'autorité.",
        "psaume": "Psaume 45", "nb_ecriture": 10, "lecture_intégrale": "OUI (À lire entièrement à voix haute après le bain)",
        "verset": "Verset 2", "texte_biblique": "Des paroles pleines de charme bouillonnent dans mon cœur. Je dis : Mon œuvre est pour le roi !",
        "huile": "Géranium Bourbon (Magnétisme professionnel et éclat)", 
        "aromatiques": "Feuilles de Géranium odorant, Marjolaine, Curcuma pur",
        "zikr": "Ya Jamil (Ô Beau) — 83 fois + Nom Salomonique : ADONAI TZABAOTH",
        "mots_application": "Accorde-moi le charisme, le respect et l'autorité morale nécessaires dans mes entreprises et mon travail. Amen.", "moment": "Matin"
    },
    "Ali (Badara Aliou)": {
        "ref": "Ali (Badara Aliou)", "code": (2, 1, 1, 1), "nature": "Bénéfique", "element": "Vent", "direction": "Sud",
        "txt": "Maison des espoirs, de la protection, de la chose espérée, des envies.",
        "psaume": "Psaume 144", "nb_ecriture": 11, "lecture_intégrale": "OUI (À lire entièrement à voix haute après le bain)",
        "verset": "Verset 1", "texte_biblique": "Béni soit l'Éternel, mon rocher, qui exerce mes mains au combat, mes doigts à la bataille !",
        "huile": "Gingembre Bleu (Force, dynamisme et courage)", 
        "aromatiques": "Graines de Cardamome, Menthe des champs, Poudre de Gingembre",
        "zikr": "Ya Qawiyyou (Ô Fort Invincible) — 116 fois + Nom Salomonique : EL SHADDAI",
        "mots_application": "Que mes espérances les plus profondes soient fortifiées et protégées contre tout obstacle. Amen.", "moment": "Matin"
    },
    "Nouhou (Nounkoro)": {
        "ref": "Nouhou (Nounkoro)", "code": (1, 2, 2, 2), "nature": "Mauvais", "element": "Terre", "direction": "Ouest",
        "txt": "Maison des difficultés, des problèmes, maison ennemis, des obstacles, des entraves.",
        "psaume": "Psaume 30", "nb_ecriture": 12, "lecture_intégrale": "OUI (À lire entièrement à voix haute après le bain)",
        "verset": "Verset 12", "texte_biblique": "Tu as changé mon deuil en allégresse, tu as délié mon sac, et tu m'as ceint de joie.",
        "huile": "Citronnelle Java (Nettoyage des ondes lourdes)", 
        "aromatiques": "Tiges de Citronnelle fraîches, Thym blanc, Estragon, Girofle pilé",
        "zikr": "Ya Latif (Ô Bienveillant) — 129 fois + Nom Salomonique : IAH",
        "mots_application": "Que tous les pièges de l'ombre soient déracinés et dissous, laissant place au triomphe. Amen.", "moment": "Soir"
    },
    "Houssaini (Ioussiné)": {
        "ref": "Houssaini (Ioussiné)", "code": (1, 1, 2, 2), "nature": "Neutre", "element": "Eau", "direction": "Nord",
        "txt": "Maison de la situation présente, des informations diverses, du dortoir, informations dans la chambre.",
        "psaume": "Psaume 18", "nb_ecriture": 13, "lecture_intégrale": "OUI (À lire entièrement à voix haute après le bain)",
        "verset": "Verset 38", "texte_biblique": "Je les brise, et ils ne peuvent se relever ; ils tombent sous mes pieds.",
        "huile": "Clou de Girofle (Scellage et protection du lieu)", 
        "aromatiques": "Feuilles d'Eucalyptus, Clous de girofle, Écorce de cannelle",
        "zikr": "Ya Moumit (Ô Maître de la libération) — 490 fois + Nom Salomonique : ELOHIM",
        "mots_application": "Que ma situation actuelle soit clarifiée, purifiée et libérée des énergies stagnantes. Amen.", "moment": "Soir"
    },
    "Younouss (Tontigui)": {
        "ref": "Younouss (Tontigui)", "code": (1, 2, 1, 2), "nature": "Bénéfique", "element": "Terre", "direction": "Ouest",
        "txt": "Maison de la richesse, de l'argent, maison qui décrit la situation à venir, ce qui n'est pas encore accompli.",
        "psaume": "Psaume 91", "nb_ecriture": 14, "lecture_intégrale": "OUI (À lire entièrement à voix haute après le bain)",
        "verset": "Verset 11", "texte_biblique": "Car il ordonnera à ses anges de te garder dans toutes tes voies.",
        "huile": "Arbre à Thé / Tea Tree (Bouclier financier)", 
        "aromatiques": "Laurier noble séché, Coriandre en graines, Curcuma or",
        "zikr": "Ya Hafiz (Ô Protecteur Suprême) — 998 fois + Nom Salomonique : JEHOVAH JIREH",
        "mots_application": "Que la prospérité future promise par ce thème soit scellée et divinement protégée. Amen.", "moment": "Matin"
    },
    "Ousmane (Mori Zoumana)": {
        "ref": "Ousmane (Mori Zoumana)", "code": (2, 2, 1, 1), "nature": "Bénéfique", "element": "Vent", "direction": "Sud",
        "txt": "La conclusion du thème, l'environnement, la situation générale, le résumé du thème.",
        "psaume": "Psaume 119", "nb_ecriture": 15, "lecture_intégrale": "OUI (À lire entièrement à voix haute après le bain)",
        "verset": "Verset 105", "texte_biblique": "Ta parole est une lampe à mes pieds, et une lumière sur mon sentier.",
        "huile": "Encens d'Oliban (Haute connexion divine et conclusion céleste)", 
        "aromatiques": "Résine pure d'Oliban, Fleurs de Jasmin, Safran royal",
        "zikr": "Ya Alim (Ô Omniscient) — 150 fois + Nom Salomonique : TETRAGRAMMATON",
        "mots_application": "Que la lumière parfaite éclaire la conclusion de mes démarches et m'apporte la réussite globale. Amen.", "moment": "Soir"
    },
    "Moussa (Moussa)": {
        "ref": "Moussa (Moussa)", "code": (2, 1, 2, 1), "nature": "Neutre à Fort", "element": "Feu", "direction": "Est",
        "txt": "La précision, la confirmation, le décret final.",
        "psaume": "Psaume 4", "nb_ecriture": 16, "lecture_intégrale": "OUI (À lire entièrement à voix haute après le bain)",
        "verset": "Verset 7", "texte_biblique": "Fais lever sur nous la lumière de ta face, ô Éternel !",
        "huile": "Orange Douce (Rapidité et scellage solaire)", 
        "aromatiques": "Zestes de Citron vert, Menthe poivrée, Cannelle, Safran",
        "zikr": "Ya Sari'u (Ô Rapide) — 202 fois + Nom Salomonique : SCHEMHAMPHORASCH",
        "mots_application": "Que le décret final de cette consultation s'exécute en ma faveur avec force et rapidité. Amen.", "moment": "Matin"
    }
}

MAISONS_NOMINATIVES = {
    1: "M1 (Demandeur)", 2: "M2 (Biens/Chances)", 3: "M3 (Entourage)", 4: "M4 (Foyer/Patrimoine)",
    5: "M5 (Enfants/Nouvelles)", 6: "M6 (Maladies)", 7: "M7 (Adversaires/Époux)", 8: "M8 (Mort/Peurs)",
    9: "M9 (Voyages)", 10: "M10 (Travail/Autorité)", 11: "M11 (Espoirs)", 12: "M12 (Difficultés)",
    13: "M13 (Témoin Droite)", 14: "M14 (Témoin Gauche)", 15: "M15 (Conclusion)", 16: "M16 (Le Décret)"
}

# ==============================================================================
# FONCTIONS DE CALCUL GÉOMANTIQUE DYNAMIQUE
# ==============================================================================
def additionner_lignes(fig1, fig2):
    """Additionne deux figures ligne par ligne selon la règle géomantique (Pair + Pair = Pair, Impair + Impair = Pair, Impair + Pair = Impair)"""
    c1 = DATA[fig1]["code"]
    c2 = DATA[fig2]["code"]
    nouveau_code = []
    for i in range(4):
        total = c1[i] + c2[i]
        nouveau_code.append(2 if total % 2 == 0 else 1)
    
    # Trouver le nom de la figure correspondante au nouveau code secret généré
    for nom, bloc in DATA.items():
        if bloc["code"] == tuple(nouveau_code):
            return nom
    return fig1 # Sécurité

def generer_fille(m1, m2, m3, m4, index_ligne):
    """Génère le code d'une fille en prenant une ligne spécifique des 4 mères"""
    code_fille = (
        DATA[m1]["code"][index_ligne],
        DATA[m2]["code"][index_ligne],
        DATA[m3]["code"][index_ligne],
        DATA[m4]["code"][index_ligne]
    )
    for nom, bloc in DATA.items():
        if bloc["code"] == code_fille:
            return nom
    return m1

# ==============================================================================
# INTERFACE STREAMLIT APPLICATION EXPERT
# ==============================================================================
st.title("🔮 Plateforme Théurgique & Géomantique Automatisée")
st.write("Saisissez uniquement les 4 Mères fondamentales. Le système dresse la matrice sacrée entière.")

with st.sidebar:
    st.header("🔐 Clé d'Authentification")
    u_id = st.text_input("Identifiant")
    u_pw = st.text_input("Mot de passe", type="password")

if u_id == ID_SECRET and u_pw == MDP_SECRET:
    st.success("🔓 Temple théurgique ouvert. Algorithmes actifs.")
    
    # Étape 1 : Saisie exclusive des 4 premières maisons
    st.header("📥 ACTION : SAISIE DES 4 MÈRES FONDAMENTALES")
    options_figures = list(DATA.keys())
    
    c1, col2, col3, col4 = st.columns(4)
    with c1: m1 = st.selectbox("🏠 M1 (Première Mère)", options_figures, index=0)
    with col2: m2 = st.selectbox("🏠 M2 (Deuxième Mère)", options_figures, index=1)
    with col3: m3 = st.selectbox("🏠 M3 (Troisième Mère)", options_figures, index=2)
    with col4: m4 = st.selectbox("🏠 M4 (Quatrième Mère)", options_figures, index=3)

    # CALCULS SÉQUENTIELS AUTOMATIQUES DES MAISONS 5 À 16
    m5 = generer_fille(m1, m2, m3, m4, 0) # Ligne 1 des mères
    m6 = generer_fille(m1, m2, m3, m4, 1) # Ligne 2
    m7 = generer_fille(m1, m2, m3, m4, 2) # Ligne 3
    m8 = generer_fille(m1, m2, m3, m4, 3) # Ligne 4

    m9 = additionner_lignes(m1, m2)
    m10 = additionner_lignes(m3, m4)
    m11 = additionner_lignes(m5, m6)
    m12 = additionner_lignes(m7, m8)

    m13 = additionner_lignes(m9, m10)
    m14 = additionner_lignes(m11, m12)
    m15 = additionner_lignes(m13, m14)
    m16 = additionner_lignes(m15, m1)

    # Stockage de tout le thème calculé
    theme_complet = {
        1: m1, 2: m2, 3: m3, 4: m4, 5: m5, 6: m6, 7: m7, 8: m8,
        9: m9, 10: m10, 11: m11, 12: m12, 13: m13, 14: m14, 15: m15, 16: m16
    }

    # VISUEL DE LA MATRICE GÉOMANTIQUE TRADITIONNELLE
    st.markdown("---")
    st.header("🖼️ CARTOGRAPHIE ET VISUEL DU THÈME CALCULÉ")
    
    with st.container(border=True):
        st.subheader("⚜️ Ligne I : Les 4 Mères Fondamentales")
        i1, i2, i3, i4 = st.columns(4)
        i1.metric("Maison 1", theme_complet[1])
        i2.metric("Maison 2", theme_complet[2])
        i3.metric("Maison 3", theme_complet[3])
        i4.metric("Maison 4", theme_complet[4])
        
        st.subheader("🌿 Ligne II : Les 4 Filles Dérivées")
        i5, i6, i7, i8 = st.columns(4)
        i5.metric("Maison 5", theme_complet[5])
        i6.metric("Maison 6", theme_complet[6])
        i7.metric("Maison 7", theme_complet[7])
        i8.metric("Maison 8", theme_complet[8])

        st.subheader("⚡ Ligne III : Les 4 Neveux (Moyens de l'action)")
        i9, i10, i11, i12 = st.columns(4)
        i9.metric("Maison 9", theme_complet[9])
        i10.metric("Maison 10", theme_complet[10])
        i11.metric("Maison 11", theme_complet[11])
        i12.metric("Maison 12", theme_complet[12])

        st.subheader("⚖️ Tribunal Sacré : Témoins, Juge & Sentence Final")
        i13, i14, i15, i16 = st.columns(4)
        i13.warning(f"M13 (Témoin Droite) : {theme_complet[13]}")
        i14.warning(f"M14 (Témoin Gauche) : {theme_complet[14]}")
        i15.error(f"M15 (Le Juge Central) : {theme_complet[15]}")
        i16.success(f"M16 (Le Décret Suprême) : {theme_complet[16]}")

    # ==============================================================================
    # ANALYSE ET MOTEUR INTELLIGENT DE PASSATION
    # ==============================================================================
    st.markdown("---")
    st.header("🔄 INTERPRÉTATION EXPERTE DES PASSATIONS DE FIGURES")
    
    repartitions = defaultdict(list)
    for maison, fig in theme_complet.items():
        repartitions[fig].append(maison)
        
    passations = {fig: maisons for fig, maisons in repartitions.items() if len(maisons) > 1}
    
    if passations:
        for fig, maisons in passations.items():
            nb_rep = len(maisons)
            statut = "DOUBLE" if nb_rep == 2 else "TRIPLE" if nb_rep == 3 else f"RÉPÉTÉE {nb_rep} FOIS"
            maisons_txt = " ➔ ".join([f"M{m}" for m in maisons])
            
            with st.container(border=True):
                st.markdown(f"### 🔀 **{fig}** s'est déplacée en **{statut}**")
                st.markdown(f"**Circuit emprunté :** `{maisons_txt}`")
                
                # Règles d'interprétation contextuelle des passations majeures
                m_prem, m_dern = maisons[0], maisons[-1]
                st.markdown("**💡 Révélation Théurgique Avancée :**")
                
                if m_prem == 1 and m_dern == 2:
                    st.write("🔴 *Interprétation :* Les pensées, l'esprit et l'énergie vitale du demandeur (M1) sont actuellement totalement absorbés ou bloqués par sa situation financière (M2).")
                elif m_prem == 1 and m_dern == 12:
                    st.write("🔴 *Interprétation :* Attention critique. Le demandeur (M1) est actuellement le propre artisan de ses blocages (M12). Il s'auto-sabote ou s'enferme lui-même dans des entraves.")
                elif m_prem == 2 and m_dern == 14:
                    st.write("🍏 *Interprétation :* Présage d'Or. Les finances actuelles (M2) sont confirmées de manière imminente et irréversible par le Témoin Gauche (M14) comme source de richesse future.")
                else:
                    st.write(f"Le courant spirituel de la figure prend naissance dans la zone de vie de la **{MAISONS_NOMINATIVES[m_prem]}** et vient jeter son décret ou sa résolution finale au sein de la **{MAISONS_NOMINATIVES[m_dern]}**.")
    else:
        st.success("✅ Aucune interférence de passation. Les 16 forces agissent indépendamment.")

    # ==============================================================================
    # EXPORTATION DE LA FICHE DU CONSULTANT
    # ==============================================================================
    st.markdown("---")
    st.header("📋 EXPORTATION : FICHE DE SOIN ET RITUEL DU CONSULTANT")
    
    # Compilation dynamique des informations à copier
    texte_fiche = "--- RITUEL DU THÈME GÉOMANTIQUE ---\n\n"
    for m, fig_choisie in theme_complet.items():
        b = DATA[fig_choisie]
        texte_fiche += f"[{MAISONS_NOMINATIVES[m]}] -> {fig_choisie}\n"
        texte_fiche += f"- Aromates : {b['aromatiques']}\n"
        texte_fiche += f"- Huile : {b['huile']}\n"
        texte_fiche += f"- Écriture Nassi : {b['psaume']} ({b['verset']}) - {b['nb_ecriture']} fois\n"
        texte_fiche += f"- Activation : {b['zikr']}\n"
        texte_fiche += "----------------------------------------\n"
        
    st.text_area("Sélectionnez tout et copiez le texte ci-dessous pour votre fiche client :", value=texte_fiche, height=250)

    # ==============================================================================
    # EXPANDEURS DÉTAILLÉS MAISON PAR MAISON
    # ==============================================================================
    st.markdown("---")
    st.header("📖 DICTIONNAIRE DÉTAILLÉ DE CHAQUE SECTEUR")
    
    for m, fig_choisie in theme_complet.items():
        bloc = DATA[fig_choisie]
        entete = f"🛑 {MAISONS_NOMINATIVES[m]} ➔ {fig_choisie} [PURIFICATION]" if "Mauvais" in bloc["nature"] else f"✨ {MAISONS_NOMINATIVES[m]} ➔ {fig_choisie} [OUVERTURE]"
        
        with st.expander(entete):
            t1, t2, t3 = st.tabs(["📊 Diagnostic du Verbe", "🌿 Recette Aromatique & Psaumes", "📿 Clé du Zikr & Noms Sacrés"])
            
            with t1:
                st.markdown(f"**Interprétation Clinique (txt) :** *{bloc['txt']}*")
                st.markdown(f"**Élément & Orientation :** {bloc['element']} | {bloc['direction']} | Force : `{bloc['nature'].upper()}`")
                
            with t2:
                st.markdown("### 🧪 Préparation du Bain")
                st.markdown(f"🌱 **Aromates et Colorants Sacrés :** `{bloc['aromatiques']}`")
                st.markdown(f"💧 **Huile essentielle de scellage :** *{bloc['huile']}*")
                st.success(f"✍️ **Écriture du Nassi :** Écrire le **{bloc['verset']}** exactement **{bloc['nb_ecriture']} fois** (Encre de Safran ou Curcuma)")
                st.info(f"📜 **Lecture obligatoire :** Réciter le **{bloc['psaume']} en entier** à voix haute au-dessus de l'eau.")
                st.write(f"👉 *\"{bloc['texte_biblique']}\"*")
                
            with t3:
                st.warning(f"**Zikr & Mantra Salomonique d'activation :** {bloc['zikr']}")
                st.success(f"**Mots d'Application :** \"{bloc['mots_application']}\"")
else:
    st.warning("🔒 Saisissez vos identifiants dans le panneau latéral pour charger votre laboratoire mystique.")
