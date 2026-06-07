import streamlit as st
import random

# =====================================================================
# 1. CONFIGURATION ET BASE DE DONNÉES DU RAMROU (16 Figures)
# =====================================================================
st.set_page_config(
    page_title="Système Expert de Haute Géomancie Théurgique",
    page_icon="🔮",
    layout="wide"
)

# Base de données interconnectant Code Binaire, Noms Sacrés, Éléments et Remèdes
DICTIONNAIRE_FIGURES = {
    "1.1.1.1": {
        "nom_arabe": "Ibrahima", "nom_bambara": "Lahiya", "nom_latin": "Via", "numero": 5,
        "element": "Eau", "nature": "Vent maléfique", "polarite": "Humain (Bon)",
        "nom_divin": "EHEIEH (Je suis celui qui suis)", "archange": "GABRIEL",
        "psaume_nom": "Psaume 120", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.7) du Psaume 120.",
        "verset_biblique": "Psaume 121:8 — 'L'Éternel gardera ton départ et ton arrivée...'",
        "texte_salomonique": "5e Pentacle de la Lune — Contre les barrières et pour voyager en sécurité.",
        "encre": "Encre d'argent ou bleu clair (eau de coco pure).",
        "plantes": "Zaba (Landolphia owariensis) et Feuilles de Palmier.",
        "sacrifice": "6 litres de lait avec un coq rouge ou un mouton. À donner à un homme le lundi entre 13h et 15h.",
        "moment": "Lundi matin au lever du soleil."
    },
    "1.1.1.2": {
        "nom_arabe": "Assane", "nom_bambara": "Janfa Almamy", "nom_latin": "Puella", "numero": 13,
        "element": "Eau", "nature": "Le sable", "polarite": "Diable (Mauvais)",
        "nom_divin": "SHADDAÏ (Tout-Puissant)", "archange": "ANAEL",
        "psaume_nom": "Psaume 119 (Aleph)", "cle_psaume": "Écrire le premier verset (V.1) et le huitième verset (V.8) du Psaume 119.",
        "verset_biblique": "Cantique des Cantiques 4:7 — 'Tu es toute belle, mon amie...'",
        "texte_salomonique": "2e Pentacle de Vénus — Pour obtenir la grâce, l'amour et les faveurs.",
        "encre": "Encre rose ou traditionnelle à l'eau de rose.",
        "plantes": "Plantes rampantes des zones sablonneuses, Fleurs de Jasmin.",
        "sacrifice": "Un plat de riz avec de la viande de coq. À donner à des femmes le samedi entre 10h et 12h.",
        "moment": "Vendredi matin à l'aube."
    },
    "1.2.1.1": {
        "nom_arabe": "Adama", "nom_bambara": "Adama", "nom_latin": "Fortuna Major", "numero": 2,
        "element": "Feu", "nature": "Mer / Courant électrique / Lumière", "polarite": "Diable (Bon)",
        "nom_divin": "ELOHIM (Dieu Suprême)", "archange": "MICHAEL",
        "psaume_nom": "Psaume 91", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.16) du Psaume 91.",
        "verset_biblique": "Genèse 12:2 — 'Je ferai de toi une grande nation, et je te bénirai...'",
        "texte_salomonique": "1er Pentacle du Soleil — Face et Figure du Créateur.",
        "encre": "Encre Jaune Safranée (Vrai safran ou curcuma. SANS SOUFRE).",
        "plantes": "N'gouna (Scléroarya birréa), Djalan (Khaya senegalensis), Laurier noble.",
        "sacrifice": "Tissu noir, 1 l de lait, 3 ou 7 colas blancs. À donner à un homme le jeudi ou mercredi matin.",
        "moment": "Dimanche matin au soleil."
    },
    "1.2.2.1": {
        "nom_arabe": "Soulaymane", "nom_bambara": "Souleymane", "nom_latin": "Carcer", "numero": 10,
        "element": "Terre", "nature": "Montagne", "polarite": "Humain (Bon)",
        "nom_divin": "YHVH TZABAOTH (Dieu des Armées)", "archange": "CASSIEL",
        "psaume_nom": "Psaume 142", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.8) du Psaume 142.",
        "verset_biblique": "Isaïe 22:22 — 'Je mettrai sur son épaule la clé de la maison de David...'",
        "texte_salomonique": "7e Pentacle de Saturne — Pour commander aux puissances de l'ombre.",
        "encre": "Encre noire traditionnelle concentrée au noir de fumée.",
        "plantes": "Arbres massifs à écorce dure, Feuilles de Cyprès.",
        "sacrifice": "3 plats de riz avec de la viande. À donner à une femme entre 18h et 20h, peu importe le jour.",
        "moment": "Samedi soir tard."
    },
    "1.2.1.2": {
        "nom_arabe": "Inssa", "nom_bambara": "Insa", "nom_latin": "Amissio", "numero": 6,
        "element": "Eau", "nature": "La pluie", "polarite": "Humain (Mauvais)",
        "nom_divin": "ADONAÏ (Le Seigneur)", "archange": "ANAEL",
        "psaume_nom": "Psaume 102", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.29) du Psaume 102.",
        "verset_biblique": "Joël 2:25 — 'Je vous remplacerai les années qu'ont dévorées la sauterelle.'",
        "texte_salomonique": "5e Pentacle de Vénus — Invite à l'amour et au respect instantané.",
        "encre": "Encre marron terre.",
        "plantes": "Kèlètiguè yiri, Triqi (Combretum glutinosum), Sauge.",
        "sacrifice": "6 litres de lait avec un coq blanc ou une chèvre. À donner à un homme le mardi entre 17h et 18h.",
        "moment": "Vendredi soir après le coucher du soleil."
    },
    "1.2.2.2": {
        "nom_arabe": "Ousmane", "nom_bambara": "Mori Zoumana", "nom_latin": "Laetitia", "numero": 15,
        "element": "Air", "nature": "Eau de puits", "polarite": "Humain (Bon)",
        "nom_divin": "EL (Dieu Fort)", "archange": "SACHIEL",
        "psaume_nom": "Psaume 4", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.9) du Psaume 4.",
        "verset_biblique": "Néhémie 8:10 — 'Ne vous affligez pas, car la joie de l'Éternel sera votre force.'",
        "texte_salomonique": "2e Pentacle de Jupiter — Pour acquérir la gloire et les honneurs.",
        "encre": "Encre bleue céleste mélangée à du musc blanc.",
        "plantes": "Plantes aquatiques douces, lianes d'eau, Menthe poivrée.",
        "sacrifice": "3 plats de riz avec 10 colas blancs. À donner à des hommes le dimanche entre 17h et 18h.",
        "moment": "Jeudi matin à l'aube."
    },
    "1.1.2.1": {
        "nom_arabe": "Youssouf", "nom_bambara": "Sediou", "nom_latin": "Puer", "numero": 1,
        "element": "Feu", "nature": "Feu de braise", "polarite": "Individu (Mauvais)",
        "nom_divin": "ELOHIM GIBOR (Dieu Guerrier)", "archange": "SAMAEL",
        "psaume_nom": "Psaume 35", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.28) du Psaume 35.",
        "verset_biblique": "Exode 15:3 — 'L'Éternel est un vaillant guerrier...'",
        "texte_salomonique": "2e Pentacle de Mars — Contre les maladies, plaies et esprits rebelles.",
        "encre": "Encre Rouge (poudre de piment ou gingembre).",
        "plantes": "Balanzan (Acacia albida), Diatigui Faga (Ficus sp.), Ortie.",
        "sacrifice": "Pagne ou tissu noir, 1 l de lait, 3 ou 7 colas blancs. À donner à un homme le jeudi matin.",
        "moment": "Mardi soir tard."
    },
    "1.1.2.2": {
        "nom_arabe": "Aliou", "nom_bambara": "Alou", "nom_latin": "Fortuna Minor", "numero": 11,
        "element": "Air", "nature": "Fumée", "polarite": "Humain (Mauvais)",
        "nom_divin": "YHVH (Le Tétragramme Sacré)", "archange": "MICHAEL",
        "psaume_nom": "Psaume 121", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.8) du Psaume 121.",
        "verset_biblique": "Psaume 46:2 — 'Dieu est pour nous un refuge et un appui...'",
        "texte_salomonique": "4e Pentacle du Soleil — Pour acquérir une renommée ou un secours céleste.",
        "encre": "Encre Orange ou Jaune vif (Curcuma).",
        "plantes": "Plantes à sève laiteuse, Écorces d'Orange, Romarin.",
        "sacrifice": "3 kg de riz, 3 kg de mil, 7 colas blancs. À donner à un homme entre 18h et 22h.",
        "moment": "À l'aube un jeudi ou un dimanche."
    },
    "2.1.1.1": {
        "nom_arabe": "Mahdy", "nom_bambara": "Mahdi", "nom_latin": "Caput Draconis", "numero": 3,
        "element": "Air", "nature": "Vent fort, tornade", "polarite": "Diable (Bon)",
        "nom_divin": "EL SHADDAÏ", "archange": "CASSIEL",
        "psaume_nom": "Psaume 128", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.6) du Psaume 128.",
        "verset_biblique": "Exode 20:12 — 'Honore ton père et ta mère...'",
        "texte_salomonique": "1er Pentacle de la Terre — Pour donner force aux fondations.",
        "encre": "Encre brune mélangée à de la terre fine fertile.",
        "plantes": "Sébé (Rônier), Tabacouba (Detarium senegalense).",
        "sacrifice": "7 kg de sel, une paire de chaussures noires à donner à une femme entre 17h et 21h (Lundi ou Jeudi).",
        "moment": "Mercredi ou samedi matin."
    },
    "2.1.1.2": {
        "nom_arabe": "Omar", "nom_bambara": "Oumar", "nom_latin": "Conjunctio", "numero": 7,
        "element": "Air", "nature": "Vent", "polarite": "Diable (Mauvais)",
        "nom_divin": "YHVH ELOHIM (Dieu de l'Union)", "archange": "RAPHAEL",
        "psaume_nom": "Psaume 133", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.3).",
        "verset_biblique": "Ruth 1:16 — 'Où tu iras j'irai, où tu demeureras je demeurerai...'",
        "texte_salomonique": "4e Pentacle de Mercure — Pour l'éloquence.",
        "encre": "Encre Jaune Pâle ou bicolore.",
        "plantes": "Kaba houlé (Ficus platyphylla), Brins de Lavande.",
        "sacrifice": "Chèvre ou mouton blanc, ou coq rouge. À donner à une femme le mardi ou samedi entre 22h et 00h.",
        "moment": "Mercredi matin au lever du soleil."
    },
    "2.1.2.1": {
        "nom_arabe": "Younouss", "nom_bambara": "Tounka", "nom_latin": "Acquisitio", "numero": 14,
        "element": "Terre", "nature": "Vent froid et lourd", "polarite": "Diable (Bon)",
        "nom_divin": "EL ELYON (Dieu Très-Haut)", "archange": "SACHIEL",
        "psaume_nom": "Psaume 112", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.10) du Psaume 112.",
        "verset_biblique": "Deutéronome 28:12 — 'L'Éternel t'ouvrira son bon trésor...'",
        "texte_salomonique": "6e Pentacle de Jupiter — Assure une immense fortune.",
        "encre": "Encre Verte ou Violette.",
        "plantes": "Plantes de récolte, arbres fruitiers, Trèfles.",
        "sacrifice": "Un plat de riz avec un cola blanc. À donner à une femme le vendredi entre 13h et 15h.",
        "moment": "Jeudi matin à l'aube."
    },
    "2.1.2.2": {
        "nom_arabe": "Lamora", "nom_bambara": "Mori lani", "nom_latin": "Rubeus", "numero": 12,
        "element": "Feu", "nature": "Passion / Rouge", "polarite": "Diable",
        "nom_divin": "EHYEH ASHER EHYEH", "archange": "SAMAEL",
        "psaume_nom": "Psaume 29", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.11).",
        "verset_biblique": "Cantique des Cantiques 8:6 — 'Mets-moi comme un sceau sur ton cœur...'",
        "texte_salomonique": "4e Pentacle de Mars — Pour la victoire et apaiser l'agressivité.",
        "encre": "Encre Rouge Vif (jus de grenade).",
        "plantes": "Pétales de Rose rouge, Verveine, Clous de girofle.",
        "sacrifice": "Offrir du cola rouge ou des fruits écarlates un mardi.",
        "moment": "Mardi soir."
    },
    "2.2.1.1": {
        "nom_arabe": "Nouhou", "nom_bambara": "Gounadyan", "nom_latin": "Cauda Draconis", "numero": 12,
        "element": "Terre", "nature": "Vent", "polarite": "Humain (Bon)",
        "nom_divin": "AGLA (Tu es puissant à jamais)", "archange": "URIEL",
        "psaume_nom": "Psaume 59", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.18) du Psaume 59.",
        "verset_biblique": "Psaume 68:2 — 'Dieu se lève, ses ennemis se dispersent...'",
        "texte_salomonique": "6e Pentacle de Saturne — Pour faire fuir les démons.",
        "encre": "Encre Noire brute au noir de fumée.",
        "plantes": "Plantes de nettoyage ou lavage spirituel, Eucalyptus, Armoise.",
        "sacrifice": "Un coq rouge, 3 kg de maïs, 7 colas rouges. À donner à une femme le vendredi entre 20h et 22h.",
        "moment": "Samedi soir tard."
    },
    "2.2.1.2": {
        "nom_arabe": "Idriss", "nom_bambara": "Mori lani", "nom_latin": "Albus", "numero": 4,
        "element": "Eau", "nature": "Fleuve", "polarite": "Diable (Bon)",
        "nom_divin": "SADAI (Le Miroir de Clarté)", "archange": "RAPHAEL",
        "psaume_nom": "Psaume 119 (Beth)", "cle_psaume": "Écrire le neuvième verset (V.9) et le seizième verset (V.16) du Psaume 119.",
        "verset_biblique": "Isaïe 1:18 — 'Vos péchés deviendront blancs comme la neige...'",
        "texte_salomonique": "2e Pentacle de Mercure — Pour l'illumination.",
        "encre": "Encre Blanche (camphre et craie).",
        "plantes": "N'Gokoun (Nénuphar / Nymphaea lotus), Fleurs de Lys.",
        "sacrifice": "7 kg de sel, une paire de chaussures noires à donner à une femme entre 22h et 00h (Lundi ou Jeudi).",
        "moment": "Mercredi matin à l'aube."
    },
    "2.2.2.1": {
        "nom_arabe": "Ayoub", "nom_bambara": "Mangoussi", "nom_latin": "Tristitia", "numero": 8,
        "element": "Terre", "nature": "La tombe", "polarite": "Diable (Mauvais)",
        "nom_divin": "IAH (L'Éternel Consolateur)", "archange": "CASSIEL",
        "psaume_nom": "Psaume 40", "cle_psaume": "Écrire le deuxième verset (V.2) et le dernier verset (V.18).",
        "verset_biblique": "Isaïe 61:3 — 'Pour donner aux affligés un diadème au lieu de la cendre...'",
        "texte_salomonique": "5e Pentacle de Saturne — Pour repousser la ruine.",
        "encre": "Encre Bleu Nuit ou Noire profonde.",
        "plantes": "Plantes de cimetière, racines profondes, Gingembre.",
        "sacrifice": "Mouton blanc ou coq blanc. À donner à un homme le mardi ou samedi entre 10h et 12h.",
        "moment": "Samedi soir."
    },
    "2.2.2.2": {
        "nom_arabe": "Moussa", "nom_bambara": "Moussa", "nom_latin": "Populus", "numero": 16,
        "element": "Feu", "nature": "La cendre", "polarite": "Humain (Mauvais)",
        "nom_divin": "ADONAÏ MELEKH (Le Seigneur Roi des Foules)", "archange": "GABRIEL",
        "psaume_nom": "Psaume 47", "cle_psaume": "Écrire le premier verset (V.1) et le dernier verset (V.10) du Psaume 47.",
        "verset_biblique": "Genèse 22:17 — 'Je multiplierai ta postérité, comme les étoiles du ciel...'",
        "texte_salomonique": "1er Pentacle de la Lune — Pour ouvrir toutes les portes closes.",
        "encre": "Encre Gris Perle (eau de pluie).",
        "plantes": "Arbres produisant beaucoup de cendre, Persil, Sauge.",
        "sacrifice": "Tissu blanc, un coq blanc, de la viande de chèvre. À donner à des hommes le dimanche à 06h du matin.",
        "moment": "Lundi (Lune Croissante)."
    }
}

NOMS_MAISONS = [
    "M1 : Consultant / Tête", "M2 : Gains / Argent", "M3 : Entourage / Échanges", "M4 : Foyer / Patrimoine",
    "M5 : Amours / Enfants", "M6 : Blocages / Maladie", "M7 : Conjoint / Associés", "M8 : Changements / Mort",
    "M9 : Voyages / Spiritualité", "M10 : Carrière / Honneurs", "M11 : Appuis / Espoirs", "M12 : Épreuves / Secrets",
    "M13 : Témoin Droit (Passé)", "M14 : Témoin Gauche (Futur)", "M15 : Le Juge (Verdict)", "M16 : La Sentence (Issue)"
]

# =====================================================================
# 2. FONCTIONS DE LOGIQUE GÉOMANTIQUE
# =====================================================================
def identifier_figure(liste_points):
    cle = ".".join(map(str, liste_points))
    return DICTIONNAIRE_FIGURES.get(cle, {
        "nom_arabe": "Inconnue", "element": "Inconnu", "nature": "Inconnue",
        "nom_divin": "Inconnu", "archange": "Inconnu", "psaume_nom": "Inconnu",
        "cle_psaume": "-", "verset_biblique": "-", "texte_salomonique": "-",
        "encre": "-", "plantes": "-", "sacrifice": "-", "moment": "-"
    })

def additionner_figures(fig_a, fig_b):
    return [2 if (fig_a[i] + fig_b[i]) in [2, 4] else 1 for i in range(4)]

def calcular_cle_ecriture(psaume_str):
    chiffres = [int(c) for c in psaume_str if c.isdigit()]
    total = sum(chiffres) if chiffres else 7
    while total > 9: 
        total = sum(int(c) for c in str(total))
    return 7 if total in [1, 4, 8] else (9 if total in [3, 6, 9] else 3)

def format_visuel_text(liste_points):
    return "\n".join(["●   ●" if pt == 2 else "  ●  " for pt in liste_points])

def generer_oraison_salomonique(fig_info):
    return f"""
> 📜 **Oraison Adaptée en Vertu de la Figure :**
> 
> **« Au Nom du Seigneur Dieu, le Très-Haut, Créateur des Cieux et de la Terre.**  
> 
> *Par le Saint Nom Sacré **{fig_info['nom_divin']}**, devant qui tout genou fléchit ;*  
> 
> *Et par l'intercession et la puissance du glorieux Archange **{fig_info['archange']}**, recteur de cette lumière ;*  
> 
> *Je t'invoque, ô esprit et vertu de la figure de **{fig_info['nom_arabe']} ({fig_info['nom_latin'] if 'nom_latin' in fig_info else ''})**. Viens à mon secours par la force sacrée du **{fig_info['psaume_nom']}** et que s'accomplisse pour moi la promesse :*  
> 
> *"**{fig_info['verset_biblique']}**"*  
> 
> *Que par cette écriture, ce bain et ce parfum sacrés, toutes les chaînes et influences contraires soient brisées, et que la bénédiction divine s'établisse. Amen. »*
"""

def interpreter_importance_element(element_str):
    if "Feu" in element_str:
        return {
            "icone": "🔥",
            "titre": "Élément FEU - Force d'Action et de Rapidité",
            "analyse": "L'issue de votre situation est tranchée par le Feu. Cela indique une résolution immédiate, intense ou exigeant de vous une action courageuse. Les blocages se consument vite, mais attention aux éclats de colère.",
            "conseil": "Priorisez les remèdes de purification matinale (encens sacrés) et agissez sans procrastiner."
        }
    elif "Air" in element_str:
        return {
            "icone": "💨",
            "titre": "Élément AIR - Force de Mouvement, de Parole et d'Esprit",
            "analyse": "Votre issue voyage avec les courants de l'Air. La situation est mobile, changeante et dépend de contrats, d'échanges verbaux, d'écrits ou de votre entourage direct.",
            "conseil": "Misez sur l'onction des parfums sacrés, les encens volatils et la clarté d'esprit pour fixer cette énergie."
        }
    elif "Eau" in element_str:
        return {
            "icone": "💧",
            "titre": "Élément EAU - Force de Fluidité, d'Abondance et de Bénédiction",
            "analyse": "L'Eau domine votre dénouement. C'est le signal de bénédictions fertiles, de richesses fluides, de retours d'affection ou d'une purification naturelle. Les blocages se dissolvent lentement.",
            "conseil": "Le bain thérapeutique (Nassi) est le cœur absolu de votre processus de déblocage."
        }
    elif "Terre" in element_str:
        return {
            "icone": "🌱",
            "titre": "Élément TERRE - Force d'Ancrage, de Secret et de Temps",
            "analyse": "La Terre gouverne votre sentence. Les résultats seront durables et solides, mais feront face à de lourdes inerties (lenteurs administratives, secrets, retards protecteurs). Tout s'enracine.",
            "conseil": "Ne forcez pas le temps. Honorez les aumônes matérielles lourdes (Saraka) et les plantes à racines profondes."
        }
    else:
        return {"icone": "✨", "titre": "Élément Équilibré", "analyse": "Influence mixte.", "conseil": "Suivez le protocole complet."}

# =====================================================================
# 3. INTERFACE DE CHOIX : LE JEU OU LES 4 MÈRES MANUELLES
# =====================================================================
mode_saisie = st.radio("Méthode de génération du thème géomantique :", [
    "🎲 Frapper la Terre / Tapotements (Le Jeu)", 
    "🛠️ Intégrer manuellement les 4 Mères"
])

m1, m2, m3, m4 = None, None, None, None

if mode_saisie == "🎲 Frapper la Terre / Tapotements (Le Jeu)":
    st.markdown("### 🖐️ Tracé par Parité de Points")
    st.write("Saisissez le nombre de frappes pour générer dynamiquement vos 4 Mères.")
    
    mères_generes = []
    for m in range(1, 5):
        st.write(f"**Maison Mère {m} :**")
        cols = st.columns(4)
        lignes_mere = []
        for l in range(4):
            with cols[l]:
                points = st.number_input(f"M{m} - Ligne {l+1}", min_value=1, max_value=100, value=random.randint(10, 45), key=f"tapot_{m}_{l}")
                lignes_mere.append(1 if points % 2 != 0 else 2)
        mères_generes.append(lignes_mere)
    
    m1, m2, m3, m4 = mères_generes[0], mères_generes[1], mères_generes[2], mères_generes[3]

else:
    st.markdown("### 🛠️ Configuration Manuelle des 4 Mères Directes")
    st.write("Définissez la structure ligne par ligne (1 = Un point ●, 2 = Deux points ● ●)")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("**Maison I (M1)**")
        m1 = [st.selectbox(f"M1 - L{i+1}", [1, 2], index=0, key=f"man_m1_{i}") for i in range(4)]
    with col2:
        st.write("**Maison II (M2)**")
        m2 = [st.selectbox(f"M2 - L{i+1}", [1, 2], index=0, key=f"man_m2_{i}") for i in range(4)]
    with col3:
        st.write("**Maison III (M3)**")
        m3 = [st.selectbox(f"M3 - L{i+1}", [1, 2], index=0, key=f"man_m3_{i}") for i in range(4)]
    with col4:
        st.write("**Maison IV (M4)**")
        m4 = [st.selectbox(f"M4 - L{i+1}", [1, 2], index=0, key=f"man_m4_{i}") for i in range(4)]

# =====================================================================
# 4. MOTEUR DE CALCUL DU THEME ET INTERPRÉTATION
# =====================================================================
if st.button("🔮 INTERPRÉTER LE RAMROU & GÉNÉRER L'ORDONNANCE"):
    # Dérivation stricte du Ramrou
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

    st.header("📖 Diagnostic du Thème Géomantique")
    st.markdown(f"**Consultant (M1) :** *{fig_m1['nom_arabe']}* | Élément : {fig_m1['element']}")
    
    # Détecteur Automatique de Passations Énergétiques
    st.subheader("🔄 Circulation des Énergies (Passations)")
    passations = {}
    for idx_a in range(16):
        nom_a = identifier_figure(theme_complet[idx_a])['nom_arabe']
        for idx_b in range(idx_a + 1, 16):
            nom_b = identifier_figure(theme_complet[idx_b])['nom_arabe']
            if nom_a == nom_b and nom_a != "Inconnue":
                if nom_a not in passations: passations[nom_a] = []
                passations[nom_a].append((idx_a, idx_b))

    if not passations:
        st.info("✨ Énergies stables : les figures ne migrent pas.")
    else:
        for fig_nom, occurrences in passations.items():
            for (mo, md) in occurrences:
                st.warning(f"🔁 La figure **{fig_nom}** migre de la **{NOMS_MAISONS[mo]}** vers la **{NOMS_MAISONS[md]}**.")

    # Affichage de la Matrice des 16 Maisons
    st.header("📊 Matrice du Thème Étalé")
    sections = [("Mères (1-4)", 0), ("Filles (5-8)", 4), ("Nièces (9-12)", 8), ("Tribunal (13-16)", 12)]
    for titre, start in sections:
        st.subheader(titre)
        cols = st.columns(4)
        for i in range(4):
            idx = start + i
            f_curr = identifier_figure(theme_complet[idx])
            with cols[i]:
                st.markdown(f"**{NOMS_MAISONS[idx].split(' : ')[0]}**")
                st.code(format_visuel_text(theme_complet[idx]))
                st.markdown(f"✨ *{f_curr['nom_arabe']}* ({f_curr['element']})")

    st.markdown("---")

    # =====================================================================
    # VALORISATION ET IMPORTANCE DES 4 ÉLÉMENTS SUR L'ISSUE (M16)
    # =====================================================================
    st.header("🔬 Analyse Élémentaire du Verdict (L'Importance Matricielle)")
    info_element = interpreter_importance_element(sentence['element'])
    
    with st.expander(f"{info_element['icone']} {info_element['titre']}", expanded=True):
        st.markdown(f"**Impact spirituel de la Sentence (M16) :** {info_element['analyse']}")
        st.markdown(f"💡 **Directive stratégique élémentaire :** *{info_element['conseil']}*")

    st.markdown("---")

    # =====================================================================
    # ORDONNANCE ET INVOCATIONS SALOMONIQUES ADAPTÉES
    # =====================================================================
    st.header("🛡️ Ordonnance Céleste & Théurgie Pratique")
    tab1, tab2, tab3, tab4 = st.tabs([
        "🗣️ Oraisons Salomoniques", 
        "✍️ Tracés d'Ardoise (Nassi)", 
        "🧪 Botanique & Matières Sacrées", 
        "📦 Sacrifices & Aumônes (Saraka)"
    ])
    
    n_juge = calcular_cle_ecriture(juge['psaume_nom'])
    n_sent = calcular_cle_ecriture(sentence['psaume_nom'])

    with tab1:
        st.subheader("Invocations Sacrées à Réciter")
        st.markdown(f"### 🔏 Pour le Juge Décisionnel ({juge['nom_arabe']})")
        st.markdown(generer_oraison_salomonique(juge))
        st.markdown(f"### 🔏 Pour la Sentence Finale ({sentence['nom_arabe']})")
        st.markdown(generer_oraison_salomonique(sentence))

    with tab2:
        st.subheader("Directives d'Écriture Métrique sur l'Ardoise")
        st.info(f"**Juge ({juge['nom_arabe']}) :** Tracer précisément **{n_juge} fois**.\n\n* {juge['cle_psaume']}\n* Support Sceau : {juge['texte_salomonique']}")
        st.success(f"**Sentence ({sentence['nom_arabe']}) :** Tracer précisément **{n_sent} fois**.\n\n* {sentence['cle_psaume']}\n* Support Sceau : {sentence['texte_salomonique']}")

    with tab3:
        st.subheader("Pharmacopée & Ingrédients Alchimiques pour le Bain")
        col_j, col_s = st.columns(2)
        with col_j:
            st.markdown(f"#### Pour le Juge ({juge['nom_arabe']})")
            st.write(f"🎨 **Encre Sacrée :** {juge['encre']}")
            st.write(f"🌿 **Plantes Secrètes :** {juge['plantes']}")
            st.write(f"⏰ **Heure de Descente :** {juge['moment']}")
        with col_s:
            st.markdown(f"#### Pour l'Issue ({sentence['nom_arabe']})")
            st.write(f"🎨 **Encre Sacrée :** {sentence['encre']}")
            st.write(f"🌿 **Plantes Secrètes :** {sentence['plantes']}")
            st.write(f"⏰ **Heure de Descente :** {sentence['moment']}")

    with tab4:
        st.subheader("Sacrifices Expiatoires Factuels")
        st.warning(f"**Aumône requise pour le Juge (M15) :** {juge['sacrifice']}")
        st.error(f"**Aumône requise pour l'Issue Finale (M16) :** {sentence['sacrifice']}")
