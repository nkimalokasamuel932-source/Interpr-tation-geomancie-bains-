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
        "verset": "Verset 2",
