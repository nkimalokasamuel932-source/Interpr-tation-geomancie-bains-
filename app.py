import streamlit as st

# 1. Configuration de la page de l'application
st.set_page_config(page_title="Oracle Géomantique PRO", page_icon="🔮", layout="wide")

# =====================================================================
# REPERTOIRE THEURGIQUE COMPLET DES 16 FIGURES GÉOMANTIQUES
# =====================================================================
DICTIONNAIRE_FIGURES = {
    "1.1.1.1": {
        "nom": "Hibrahim (Via)",
        "signification": "Le Mouvement, la Route, l'Instabilité. Flux constants, déplacements nécessaires, déblocage des visas, accouchement facile.",
        "psaume_nom": "Psaume 120",
        "cle_psaume": "Écrire le premier verset (V.1) and le dernier verset (V.7) du Psaume 120.",
        "verset_biblique": "Psaume 121:8 — 'L'Éternel gardera ton départ et ton arrivée, dès maintenant et à jamais.'",
        "texte_salomonique": "5e Pentacle de la Lune — \"Sert contre les barrières, les embûches et pour voyager en totale sécurité sur l'eau et sur terre.\"",
        "encre": "Encre d'argent ou bleu clair (faite avec de l'eau de coco pure ou de l'eau de puits).",
        "parfum": "Musc Blanc léger ou essence de Lotus.",
        "huiles_essentielles": "Menthe Poivrée ou Citronnelle (3 à 5 gouttes émulsionnées dans une cuillère de lait).",
        "plantes": "Feuilles de Citronnelle fraîches et Feuilles de Palmier.",
        "encens": "Camphre naturel.",
        "moment": "Lundi matin très tôt au lever du soleil.",
        "saraka": "Partage de fruits ou de friandises à des enfants (Énergie du futur)."
    },
    "1.1.1.2": {
        "nom": "Laoussana (Puella)",
        "signification": "L'Hésitation, la Beauté, les Douces pensées. Mariage, séduction, retour d'affection et apaisement des tensions.",
        "psaume_nom": "Psaume 119 (Section Aleph)",
        "cle_psaume": "Écrire le premier verset (V.1) and le huitième verset (V.8) du Psaume 119.",
        "verset_biblique": "Cantique des Cantiques 4:7 — \"Tu es toute belle, mon amie, et il n'y a point de défaut en toi.\"",
        "texte_salomonique": "2e Pentacle de Vénus — 'Pour obtenir la grâce, l'amour, les faveurs et pour voir ses désirs s'accomplir.'",
        "encre": "Encre rose ou encre traditionnelle parfumée à l'eau de rose (infusion d'hibiscus blanc).",
        "parfum": "Musc Blanc ou essence pure de Jasmin.",
        "huiles_essentielles": "Palmarosa ou Géranium Rosat (5 gouttes dans une cuillère de lait frais).",
        "plantes": "Fleurs de Jasmin ou de Lavande, infusées avec 3 cuillères à soupe de Lait frais.",
        "encens": "Santal Blanc.",
        "moment": "Vendredi matin à l'aube.",
        "saraka": "Donner du lait frais ou des objets blancs à des personnes de votre âge."
    },
    "1.2.1.1": {
        "nom": "Garia (Fortuna Major)",
        "signification": "La Grande Chance, la Protection, le Succès durable. Réussite totale, élévation royale et charisme majeur.",
        "psaume_nom": "Psaume 91",
        "cle_psaume": "Écrire le premier verset (V.1) and le dernier verset (V.16) du Psaume 91.",
        "verset_biblique": "Genèse 12:2 — 'Je ferai de toi une grande nation, et je te bénirai ; je rendrai ton nom grand, et tu seras une source de bénédiction.'",
        "texte_salomonique": "1er Pentacle du Soleil — 'Voici la Face et la Figure de Celui qui a tout créé, devant qui toutes les créatures obéissent.'",
        "encre": "Encre Jaune Safranée (Infusion de filaments de vrai safran ou de curcuma pur dans de l'eau de rose). NE JAMAIS UTILISER DE SOUFRE.",
        "parfum": "Ambre pur ou Musc ambré.",
        "huiles_essentielles": "Encens Oliban (Frankincense) ou Orange Douce (5 à 7 gouttes mélangées dans du miel).",
        "plantes": "Feuilles de Laurier noble et Feuilles de Basilic frais.",
        "encens": "Oliban pur en larmes.",
        "moment": "Dimanche matin (Laisser charger l'eau 1 heure au soleil avant le bain).",
        "saraka": "Préparer un grand repas ou donner un vêtement de valeur à un indigent."
    },
    "1.2.2.1": {
        "nom": "Solomana (Carcer)",
        "signification": "La Chefferie, le Blocage, la Concentration. Autorité administrative, protection des secrets, domination d'un litige juridique.",
        "psaume_nom": "Psaume 142",
        "cle_psaume": "Écrire le premier verset (V.1) and le dernier verset (V.8) du Psaume 142.",
        "verset_biblique": "Isaïe 22:22 — 'Je mettrai sur son épaule la clé de la maison de David : quand il ouvrira, nul ne fermera ; quand il fermera, nul n'ouvrira.'",
        "texte_salomonique": "7e Pentacle de Saturne — 'Pour commander aux puissances de l'ombre et faire trembler les oppresseurs.'",
        "encre": "Encre noire traditionnelle très concentrée au noir de fumée.",
        "parfum": "Ambre Noir ou Huile pure de Cèdre.",
        "huiles_essentielles": "Bois de Santal ou Cèdre de l'Atlas (5 gouttes dispersées dans du gros sel).",
        "plantes": "Feuilles de Cyprès ou de Lierre grimpant.",
        "encens": "Myrrhe brute.",
        "moment": "Samedi soir tard dans le calme.",
        "saraka": "Offrir du cola fendu ou du pain traditionnel à un gardien ou chef de famille."
    },
    "1.2.1.2": {
        "nom": "Inza (Amissio)",
        "signification": "La Perte, la Fatigue, le Renoncement. Stopper d'urgence les fuites d'argent et contrer les vols mystiques.",
        "psaume_nom": "Psaume 102",
        "cle_psaume": "Écrire le premier verset (V.1) and le dernier verset (V.29) du Psaume 102.",
        "verset_biblique": "Joël 2:25 — 'Je vous remplacerai les années qu'ont dévorées la sauterelle.' (Restauration spirituelle des biens).",
        "texte_salomonique": "5e Pentacle de Vénus — \"Quand on le montre à n'importe quelle personne, cela invite à l'amour et au respect instantané.\"",
        "encre": "Encre marron terre ou encre traditionnelle adoucie à l'eau de source.",
        "parfum": "Ambre précieux ou essence de Myrte.",
        "huiles_essentielles": "Lavande Vraie ou Sauge Sclarée (5 gouttes dans du gros sel).",
        "plantes": "Feuilles de Sauge et Feuilles de Thym frais.",
        "encens": "Muscade râpée ou résine de Mastic.",
        "moment": "Vendredi soir après le coucher du soleil.",
        "saraka": "Faire l'aumône de pièces de monnaie ou de vêtements usagés pour conjurer la perte."
    },
    "1.2.2.2": {
        "nom": "Adama (Laetitia)",
        "signification": "La Joie, l'Élévation, la Chance. Fête, prospérité, expansion financière, réussite aux examens et grand bonheur.",
        "psaume_nom": "Psaume 4",
        "cle_psaume": "Écrire le premier verset (V.1) and le dernier verset (V.9) du Psaume 4.",
        "verset_biblique": "Néhémie 8:10 — 'Ne vous affligez pas, car la joie de l'Éternel sera votre force.'",
        "texte_salomonique": "2e Pentacle de Jupiter — 'Pour acquérir la gloire, les honneurs, les richesses, avec une paix d'esprit absolue.'",
        "encre": "Encre bleue céleste ou encre traditionnelle mélangée à du musc blanc.",
        "parfum": "Musc Blanc pur (pour la douceur et l'attraction).",
        "huiles_essentielles": "Bergamote ou Orange Douce (7 gouttes mélangées dans une cuillère de miel).",
        "plantes": "Feuilles de Menthe poivrée fraîches (7 ou 14 feuilles) and Fleurs de Camomille.",
        "encens": "Résine de Benjoin.",
        "moment": "Jeudi matin à l'aube.",
        "saraka": "Donner 100 colas blanches ou partager de la viande de mouton blanc."
    },
    "1.1.2.1": {
        "nom": "Youssouf (Puer)",
        "signification": "L'Action, la Force masculine, le Combat. Protection blindée, destruction des complots et des langues de jalousie.",
        "psaume_nom": "Psaume 35",
        "cle_psaume": "Écrire le premier verset (V.1) and le dernier verset (V.28) du Psaume 35.",
        "verset_biblique": "Exode 15:3 — 'L'Éternel est un vaillant guerrier ; l'Éternel est son nom.'",
        "texte_salomonique": "2e Pentacle de Mars — 'Contre les maladies et les plaies, et pour soumettre les esprits rebelles.'",
        "encre": "Encre Rouge (Encre classique chargée d'une pointe de poudre de piment ou de gingembre).",
        "parfum": "Musc Noir ou essence de Patchouli.",
        "huiles_essentielles": "Poivre Noir ou Gingembre (3 à 5 gouttes maximum dans du lait. Attention : très chaud).",
        "plantes": "Feuilles de Tabac ou feuilles de pissenlit, and feuilles d'Ortie.",
        "encens": "Sang de Dragon.",
        "moment": "Mardi soir tard (Ne plus sortir après le bain).",
        "saraka": "Donner de la nourriture épicée ou des objets tranchants/métalliques."
    },
    "1.1.2.2": {
        "nom": "Allahou talla (Fortuna Minor)",
        "signification": "Le Succès rapide, l'Opportunité urgente. Protection sur les routes, secours divin immédiat face à une détresse.",
        "psaume_nom": "Psaume 121",
        "cle_psaume": "Écrire le premier verset (V.1) and le dernier verset (V.8) du Psaume 121.",
        "verset_biblique": "Psaume 46:2 — 'Dieu est pour nous un refuge et un appui, un secours toujours présent dans la détresse.'",
        "texte_salomonique": "4e Pentacle du Soleil — 'Pour voir les esprits invisibles et acquérir une renommée ou un secours céleste immédiat.'",
        "encre": "Encre Orange ou Jaune vif (Curcuma concentré dans de l'eau bénite).",
        "parfum": "Musc Ambre ou huile essentielle de Bergamote.",
        "huiles_essentielles": "Orange Douce ou Bergamote (5 gouttes dans de la crème).",
        "plantes": "Écorces d'Orange séchées and feuilles de Romarin.",
        "encens": "Oliban pur en larmes.",
        "moment": "À l'aube un jeudi ou un dimanche pour déblocage sous 48 heures.",
        "saraka": "Partager des beignets ou de la nourriture légère à l'aube."
    },
    "2.1.1.1": {
        "nom": "Maldiou (Caput Draconis)",
        "signification": "La Réalisation, la Stabilité, l'Enracinement. Projets immobiliers, investissements durables, connexion à la lignée maternelle.",
        "psaume_nom": "Psaume 128",
        "cle_psaume": "Écrire le premier verset (V.1) and le dernier verset (V.6) du Psaume 128.",
        "verset_biblique": "Exode 20:12 — 'Honore ton père et ta mère, afin que tes jours se prolongent dans le pays que l'Éternel ton Dieu te donne.'",
        "texte_salomonique": "1er Pentacle de la Terre (ou de Saturne) — 'Pour donner force aux fondations et appeler les esprits de stabilité matérielle.'",
        "encre": "Encre brune ou traditionnelle mélangée à une pincée de terre fine et fertile de forêt.",
        "parfum": "Ambre lourd ou essence de Vétiver (odeur de terre humide).",
        "huiles_essentielles": "Vétiver ou Bois de Santal (5 gouttes diluées dans du gros sel).",
        "plantes": "Feuilles de Chêne ou de Ficus (symbole de longévité).",
        "encens": "Myrrhe.",
        "moment": "Mercredi ou samedi matin.",
        "saraka": "Faire une offrande ou un cadeau direct à votre mère (ou à une figure maternelle)."
    },
    "2.1.1.2": {
        "nom": "Badra (Conjunctio)",
        "signification": "L'Union, le Contrat, l'Association. Rencontres majeures, signature de pactes commerciaux, mariages, réconciliations.",
        "psaume_nom": "Psaume 133",
        "cle_psaume": "Écrire le premier verset (V.1) and le dernier verset (V.3) — 'Qu'il est doux pour des frères de demeurer ensemble !'",
        "verset_biblique": "Ruth 1:16 — 'Où tu iras j'irai, où tu demeureras je demeurerai ; ton peuple sera mon peuple, et ton Dieu sera mon Dieu.'",
        "texte_salomonique": "4e Pentacle de Mercure — \"Pour acquérir l'éloquence, l'esprit d'assimilation et ouvrir l'esprit de l'autre.\"",
        "encre": "Encre Jaune Pâle ou bicolore (mélange safran et noir pour l'union des opposés).",
        "parfum": "Musc précieux mélangé à de l'essence de Lavande.",
        "huiles_essentielles": "Patchouli (idéal pour les contrats) ou Lavande (5 gouttes dans du lait).",
        "plantes": "Brins de Lavande and feuilles de Romarin.",
        "encens": "Fleurs de Lavande ou Macis séché.",
        "moment": "Mercredi matin au lever du soleil.",
        "saraka": "Offrir des céréales (fonio, riz) à des personnes de votre tranche d'âge un mercredi."
    },
    "2.1.2.1": {
        "nom": "Ousmane (Acquisitio)",
        "signification": "Le Gain, l'Abondance financière. RéUSSITE commerciale, profits en hausse, héritages et commerce de grande envergure.",
        "psaume_nom": "Psaume 112",
        "cle_psaume": "Écrire le premier verset (V.1) and le dernier verset (V.10) du Psaume 112.",
        "verset_biblique": "Deutéronome 28:12 — 'L'Éternel t'ouvrira son bon trésor, le ciel, pour envoyer à ton pays la pluie en son temps et pour bénir le travail de tes mains.'",
        "texte_salomonique": "6e Pentacle de Jupiter — 'Protège contre tous les dangers terrestres et assure une immense fortune à celui qui s'en lave.'",
        "encre": "Encre Verte ou Violette royale (mélange traditionnel chargé d'infusion de menthe).",
        "parfum": "Ambre Gris précieux ou essence de Santal.",
        "huiles_essentielles": "Cannelle Écorce (2 gouttes max ! TRÈS PIQUANTE) ou Oliban (5 gouttes) mélangées dans du miel.",
        "plantes": "Feuilles de Trèfle (ou de luzerne) and une bonne pincée de Poudre de Cannelle vraie.",
        "encens": "Benjoin et éclats de Cannelle.",
        "moment": "Jeudi matin à l'aube (Jour de Jupiter).",
        "saraka": "Faire un don financier important dans un lieu de culte ou à une œuvre de charité."
    },
    "2.1.2.2": {
        "nom": "Lamora (Rubeus)",
        "signification": "La Passion, la Colère, le Magnétisme. Canaliser l'agressivité d'un homme ou raviver le feu charnel d'un couple.",
        "psaume_nom": "Psaume 29",
        "cle_psaume": "Écrire le premier verset (V.1) and le dernier verset (V.11) — 'La voix de l'Éternel brise les cèdres...'",
        "verset_biblique": "Cantique des Cantiques 8:6 — 'Mets-moi comme un sceau sur ton cœur... Car l'amour est fort comme la mort.'",
        "texte_salomonique": "4e Pentacle de Mars — 'Pour la victoire finale dans les duels et pour apaiser les ardeurs agressives.'",
        "encre": "Encre Rouge Vif (chargée de quelques gouttes de jus de grenade ou de betterave).",
        "parfum": "Musc Rouge (Musc Ghazal) ou essence de Rose rouge.",
        "huiles_essentielles": "Laurier Noble (huile des vainqueurs) ou Géranium (5 gouttes dans du lait).",
        "plantes": "Pétales de Rose rouge and feuilles de Verveine fraîche.",
        "encens": "Clous de Girofle écrasés.",
        "moment": "Mardi soir (À prendre dans le calme pour transmuter les énergies).",
        "saraka": "Offrir du cola rouge ou des fruits rouges à une assemblée."
    },
    "2.2.1.1": {
        "nom": "Nouhou (Cauda Draconis)",
        "signification": "La Sortie, l'Exorcisme, la Rupture. Briser définitivement les mauvais sorts, les liens toxiques et les blocages de nuit.",
        "psaume_nom": "Psaume 59",
        "cle_psaume": "Écrire le premier verset (V.1) and le dernier verset (V.18) du Psaume 59.",
        "verset_biblique": "Psaume 68:2 — 'Dieu se lève, ses ennemis se dispersent, et ses adversaires fuient devant sa face !'",
        "texte_salomonique": "6e Pentacle de Saturne — 'Pour faire fuir les démons, détruire les complots de nuit et annuler les mauvais sorts.'",
        "encre": "Encre Noire brute au noir de fumée, pure, sans aucun ajout sucré ou aromatique.",
        "parfum": "Pas de parfum doux ! Laisser l'encre brute ou ajouter 2 gouttes d'huile de Cade.",
        "huiles_essentielles": "Arbre à thé (Tea Tree) ou Eucalyptus Globulus (7 gouttes mélangées dans du gros sel).",
        "plantes": "Feuilles d'Eucalyptus and feuilles d'Armoise (balaye les larves astrales).",
        "encens": "Feuilles de Laurier séchées. (Note : Soufre ou Asafoetida brûlés à côté en encens uniquement, JAMAIS dans l'encre).",
        "moment": "Samedi soir tard à l'extérieur ou dans un espace neutre.",
        "saraka": "Faire un sacrifice d'un vieil habit ou nettoyer bénévolement un espace public."
    },
    "2.2.1.2": {
        "nom": "Idriss (Albus)",
        "signification": "La Sagesse, la Clarté blanche, la Paix. Révélation de la vérité, éclat de l'aura, rêves prophétiques nets.",
        "psaume_nom": "Psaume 119 (Section Beth)",
        "cle_psaume": "Écrire le neuvième verset (V.9) and le seizième verset (V.16) du Psaume 119.",
        "verset_biblique": "Isaïe 1:18 — 'Si vos péchés sont comme le cramoisi, ils deviendront blancs comme la neige.'",
        "texte_salomonique": "2e Pentacle de Mercure — 'Pour obtenir l'illumination spirituelle, la clarté dans les rêves et comprendre les secrets.'",
        "encre": "Encre Blanche (ou eau pure chargée de camphre naturel et de craie blanche spirituelle).",
        "parfum": "Musc Blanc pur à 100 % (Honnêteté et transparence).",
        "huiles_essentielles": "Bois de Santal ou Lavande (5 gouttes émulsionnées dans du lait frais).",
        "plantes": "Feuilles de Lys ou pétales de Rose blanche, avec un morceau de Camphre dissous dans l'eau.",
        "encens": "Santal Blanc.",
        "moment": "Mercredi matin à l'aube.",
        "saraka": "Donner du savon, du sel ou de l'eau claire à un démuni."
    },
    "2.2.2.1": {
        "nom": "mangousi (Tristitia)",
        "signification": "La Reconstruction, la Consolation. Surmonter la mélancolie, un deuil ou relever une entreprise en faillite.",
        "psaume_nom": "Psaume 40",
        "cle_psaume": "Écrire le deuxième verset (V.2) and le dernier verset (V.18) — 'Il m'a retiré de la fosse de destruction...'",
        "verset_biblique": "Isaïe 61:3 — 'Pour donner aux affligés un diadème au lieu de la cendre, une huile de joie au lieu du deuil.'",
        "texte_salomonique": "5e Pentacle de Saturne — 'Pour consoler les cœurs tristes, défendre votre demeure et repousser la ruine.'",
        "encre": "Encre Bleu Nuit ou Noire profonde.",
        "parfum": "Ambre précieux ou essence de Patchouli.",
        "huiles_essentielles": "Vétiver (pour l'ancrage et la reconstruction) ou Cèdre (5 gouttes dans du sel).",
        "plantes": "Racines de Gingembre frais écrasées (redonne de la force à la terre) and aiguilles de Pin.",
        "encens": "Myrrhe ou Storax.",
        "moment": "Samedi soir dans le calme.",
        "saraka": "Offrir des produits de la terre (tubercules, sel) à des vieillards le samedi."
    },
    "2.2.2.2": {
        "nom": "Moussa (Populus)",
        "signification": "La Foule, le Collectif, l'Audience. Attirer la clientèle en masse, influence publique, célébrité politique ou commerciale.",
        "psaume_nom": "Psaume 47",
        "cle_psaume": "Écrire le premier verset (V.1) and le dernier verset (V.10) du Psaume 47.",
        "verset_biblique": "Genèse 22:17 — 'Je multiplierai ta postérité, comme les étoiles du ciel and comme le sable qui est sur le bord de la mer.'",
        "texte_salomonique": "1er Pentacle de la Lune — 'Pour ouvrir toutes les portes closes, briser les verrous and invoquer les esprits de l'eau.'",
        "encre": "Encre Gris Perle ou encre chargée d'eau de pluie collectée une nuit de pleine lune.",
        "parfum": "Musc Blanc ou essence de Lys.",
        "huiles_essentielles": "Lavande Vraie (pour la paix publique and l'attraction - 7 gouttes dans du lait).",
        "plantes": "Feuilles de Persil frais (multiplication) and feuilles de Sauge.",
        "encens": "Benjoin blanc ou Storax.",
        "moment": "Lundi (De préférence en période de Lune Croissante).",
        "saraka": "Distribuer du pain ou des aliments de base à une foule ou à un groupe d'enfants."
    }
}

NOMS_MAISONS = [
    "M1 : Consultant / Âme", "M2 : Gains / Argent", "M3 : Entourage / Échanges", "M4 : Foyer / Patrimoine",
    "M5 : Amours / Enfants", "M6 : Maladie / Obstacles", "M7 : Conjoint / Associés", "M8 : Mort / Changements",
    "M9 : Voyages / Spiritualité", "M10 : Carrière / Honneurs", "M11 : Appuis / Espoirs", "M12 : Épreuves / Secrets",
    "M13 : Témoin Droit (Passé)", "M14 : Témoin Gauche (Futur)", "M15 : Le Juge (Verdict)", "M16 : La Sentence (Issue)"
]

# =====================================================================
# FONCTIONS LOGIQUES ET MATHÉMATIQUES
# =====================================================================
def identifier_figure(liste_points):
    cle = ".".join(map(str, liste_points))
    return DICTIONNAIRE_FIGURES.get(cle, {"nom": "Inconnue", "signification": "-"})

def additionner_figures(fig_a, fig_b):
    return [2 if (fig_a[i] + fig_b[i]) in [2, 4] else 1 for i in range(4)]

def calculer_cle_ecriture(psaume_str):
    chiffres = [int(c) for c in psaume_str if c.isdigit()]
    total = sum(chiffres) if chiffres else 7
    while total > 9: 
        total = sum(int(c) for c in str(total))
    if total in [1, 4, 8]: return 7
    if total in [3, 6, 9]: return 9
    return 3

def generer_carre_magique(valeur_cible):
    base = (valeur_cible - 12) // 3
    reste = (valeur_cible - 12) % 3
    
    c1, c2, c3, c4, c5, c6, c7, c8, c9 = [base + i for i in range(9)]
    if reste == 1: c7 += 1; c8 += 1; c9 += 1
    elif reste == 2: c4 += 1; c5 += 1; c6 += 1; c7 += 2; c8 += 2; c9 += 2
    
    ligne1 = f"|  {c4:<3} |  {c9:<3} |  {c2:<3} |"
    ligne2 = f"|  {c3:<3} |  {c5:<3} |  {c7:<3} |"
    ligne3 = f"|  {c8:<3} |  {c1:<3} |  {c6:<3} |"
    return f"+------+------+------+\n{ligne1}\n+------+------+------+\n{ligne2}\n+------+------+------+\n{ligne3}\n+------+------+------+"

def format_visuel_text(liste_points):
    lignes = []
    for pt in liste_points:
        if pt == 2: lignes.append("●   ●")
        else: lignes.append("  ●  ")
    return "\n".join(lignes)

def extraire_numero_psaume(psaume_str):
    chiffres = "".join([c for c in psaume_str if c.isdigit()])
    return int(chiffres) if chiffres else 40

# =====================================================================
# INTERFACE D'ACCÈS
# =====================================================================
if "authentifie" not in st.session_state:
    st.session_state["authentifie"] = False

if not st.session_state["authentifie"]:
    st.subheader("🔐 Espace Sécurisé d'Oracle Géomantique")
    st.write("Veuillez entrer vos identifiants d'accès pour activer le Radar de consultation.")
    
    with st.form("formulaire_connexion_multi"):
        user_saisi = st.text_input("Nom d'utilisateur :")
        pass_saisi = st.text_input("Mot de passe :", type="password")
        bouton_validation = st.form_submit_button("🔑 Se connecter")
        
        if bouton_validation:
            try:
                admin_user = st.secrets["credentials"]["username"]
                admin_pass = st.secrets["credentials"]["password"]
                client_user = st.secrets["client_credentials"]["username"]
                client_pass = st.secrets["client_credentials"]["password"]
                
                if (user_saisi == admin_user and pass_saisi == admin_pass) or (user_saisi == client_user and pass_saisi == client_pass):
                    st.session_state["authentifie"] = True
                    st.success("Accès validé ! Lancement du moteur...")
                    st.rerun()
                else:
                    st.error("❌ Identifiants incorrects. Accès refusé.")
            except (KeyError, Exception):
                st.error("⚠️ Erreur de configuration : Profil d'accès absent ou configuration des Secrets incorrecte.")

else:
    st.title("🔮 Système Expert d'Oracle Géomantique PRO")
    st.write("Moteur de calcul théurgique configuré en mode étendu (16 Maisons).")

    question = st.text_input("✍️ Saisir le sujet ou le nom du consultant :", "Thème général")

    st.write("---")
    st.markdown("### 🛠️ Configuration des 4 Maisons Mères")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("**Maison I (M1)**")
        m1_1 = st.selectbox("Ligne 1", [1, 2], key="m1_1")
        m1_2 = st.selectbox("Ligne 2", [1, 2], key="m1_2")
        m1_3 = st.selectbox("Ligne 3", [1, 2], key="m1_3")
        m1_4 = st.selectbox("Ligne 4", [1, 2], key="m1_4")
        m1 = [m1_1, m1_2, m1_3, m1_4]

    with col2:
        st.write("**Maison II (M2)**")
        m2_1 = st.selectbox("Ligne 1", [1, 2], key="m2_1")
        m2_2 = st.selectbox("Ligne 2", [1, 2], key="m2_2")
        m2_3 = st.selectbox("Ligne 3", [1, 2], key="m2_3")
        m2_4 = st.selectbox("Ligne 4", [1, 2], key="m2_4")
        m2 = [m2_1, m2_2, m2_3, m2_4]

    with col3:
        st.write("**Maison III (M3)**")
        m3_1 = st.selectbox("Ligne 1", [1, 2], key="m3_1")
        m3_2 = st.selectbox("Ligne 2", [1, 2], key="m3_2")
        m3_3 = st.selectbox("Ligne 3", [1, 2], key="m3_3")
        m3_4 = st.selectbox("Ligne 4", [1, 2], key="m3_4")
        m3 = [m3_1, m3_2, m3_3, m3_4]

    with col4:
        st.write("**Maison IV (M4)**")
        m4_1 = st.selectbox("Ligne 1", [1, 2], key="m4_1")
        m4_2 = st.selectbox("Ligne 2", [1, 2], key="m4_2")
        m4_3 = st.selectbox("Ligne 3", [1, 2], key="m4_3")
        m4_4 = st.selectbox("Ligne 4", [1, 2], key="m4_4")
        m4 = [m4_1, m4_2, m4_3, m4_4]

    st.write("---")

    if st.button("🔮 INTERPRÉTER LE THÈME ET CALCULER LES 16 MAISONS"):
        # Calculs logiques
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
        
        m1_fig = identifier_figure(m1)
        juge = identifier_figure(m15)
        sentence = identifier_figure(m16)
        
        num_ecritures_juge = calculer_cle_ecriture(juge['psaume_nom'])
        num_ecritures_sentence = calculer_cle_ecriture(sentence['psaume_nom'])
        
        id_p_juge = extraire_numero_psaume(juge['psaume_nom'])
        id_p_sent = extraire_numero_psaume(sentence['psaume_nom'])

        # =====================================================================
        # SECTION 1 : DE QUOI PARLE LE THÈME
        # =====================================================================
        st.header("📖 Orientation Globale : De quoi parle le thème ?")
        st.write(f"**Analyse de l'intention :** Le consultant se présente sous l'influence spirituelle de la figure **{m1_fig['nom']}** en Maison I. Cela montre que son état d'esprit actuel ou sa situation de départ est marquée par : *{m1_fig['signification']}*")
        st.write(f"**Le Message du Verdict :** Le Juge suprême (**{juge['nom']}**) indique que la réponse définitive à votre préoccupation majeure (*{question}*) s'articule autour de l'énergie suivante : *{juge['signification']}*")

        st.write("---")

        # =====================================================================
        # NOUVELLE SECTION 1B : LA CONCLUSION DU THÈME (MAISON 16)
        # =====================================================================
        st.header("👑 Sceau de l'Issue : La Conclusion du Thème")
        st.markdown(
            f"En géomancie sacrée, la **Maison XVI (La Sentence)** combine l'élan initial du Consultant (M1) et la sentence du Juge (M15). "
            f"Elle représente l'étape ultime, le décret invisible qui valide la stabilité future de la situation."
        )
        
        st.error(
            f"**L'Issue Finale est régie par : {sentence['nom']}**\n\n"
            f"📌 **Verdict de l'avenir :** {sentence['signification']}\n\n"
            f"💡 *Conseil de l'Oracle :* Pour fixer cette conclusion positivement et dissoudre les derniers pièges, "
            f"l'application stricte des bains rituels liés au Psaume de la Sentence est obligatoire."
        )

        st.write("---")

        # =====================================================================
        # SECTION 2 : DETECTEUR AUTOMATIQUE DE DOUBLONS (PASSATIONS)
        # =====================================================================
        st.header("🔄 Analyse des Passations (Messages Cachés des Doublons)")
        passations_trouvees = {}
        for idx_a in range(16):
            nom_a = identifier_figure(theme_complet[idx_a])['nom']
            for idx_b in range(idx_a + 1, 16):
                nom_b = identifier_figure(theme_complet[idx_b])['nom']
                if nom_a == nom_b:
                    if nom_a not in passations_trouvees:
                        passations_trouvees[nom_a] = []
                    passations_trouvees[nom_a].append((idx_a, idx_b))

        if not passations_trouvees:
            st.info("✨ Aucune passation détectée. Les énergies agissent de manière indépendante.")
        else:
            for fig_nom, occurrences in passations_trouvees.items():
                for (maison_orig, maison_dest) in occurrences:
                    st.markdown(f"#### 🔁 Passation de **{fig_nom}**")
                    st.markdown(f"👉 Voyage entre **{NOMS_MAISONS[maison_orig]}** et **{NOMS_MAISONS[maison_dest]}**")
                    st.caption(f"💡 *Interprétation :* L'énergie liée à votre {NOMS_MAISONS[maison_orig].split(' : ')[1]} influence directement l'évolution de votre {NOMS_MAISONS[maison_dest].split(' : ')[1]}. Vous devez équilibrer la première maison pour libérer la seconde.")
                st.write("")

        st.write("---")

        # =====================================================================
        # CARTOGRAPHIE VISUELLE DES 16 MAISONS
        # =====================================================================
        st.header("📊 Cartographie Complète des 16 Maisons")
        
        st.subheader("🧱 Les 4 Maisons Mères")
        g1_1, g1_2, g1_3, g1_4 = st.columns(4)
        for idx, col in enumerate([g1_1, g1_2, g1_3, g1_4]):
            fig = identifier_figure(theme_complet[idx])
            with col:
                st.markdown(f"**{NOMS_MAISONS[idx]}**")
                st.code(format_visuel_text(theme_complet[idx]))
                st.markdown(f"🔹 **{fig['nom']}**")

        st.subheader("🌿 Les 4 Maisons Filles")
        g2_1, g2_2, g2_3, g2_4 = st.columns(4)
        for idx, col in enumerate([g2_1, g2_2, g2_3, g2_4]):
            real_idx = idx + 4
            fig = identifier_figure(theme_complet[real_idx])
            with col:
                st.markdown(f"**{NOMS_MAISONS[real_idx]}**")
                st.code(format_visuel_text(theme_complet[real_idx]))
                st.markdown(f"🔹 **{fig['nom']}**")

        st.subheader("🍃 Les 4 Maisons Nièces")
        g3_1, g3_2, g3_3, g3_4 = st.columns(4)
        for idx, col in enumerate([g3_1, g3_2, g3_3, g3_4]):
            real_idx = idx + 8
            fig = identifier_figure(theme_complet[real_idx])
            with col:
                st.markdown(f"**{NOMS_MAISONS[real_idx]}**")
                st.code(format_visuel_text(theme_complet[real_idx]))
                st.markdown(f"🔹 **{fig['nom']}**")

        st.subheader("⚖️ L'Aéropage & Le Tribunal Décisionnel")
        g4_1, g4_2, g4_3, g4_4 = st.columns(4)
        for idx, col in enumerate([g4_1, g4_2, g4_3, g4_4]):
            real_idx = idx + 12
            fig = identifier_figure(theme_complet[real_idx])
            with col:
                st.markdown(f"**{NOMS_MAISONS[real_idx]}**")
                st.code(format_visuel_text(theme_complet[real_idx]))
                st.markdown(f"🔥 **{fig['nom']}**")

        st.write("---")

        # =====================================================================
        # REMÈDES ET COUPLAGE THÉURGIQUE
        # =====================================================================
        st.header("🛡️ Ordonnance Spirituelle & Guide des Bains")
        tab1, tab2, tab3, tab4 = st.tabs([
            "⚖️ Bain du Juge (M15)", 
            "👑 Bain de la Sentence (M16)", 
            "🔮 Carrés Magiques Théurgiques", 
            "🕊️ Prescriptions Légères & Sacrifices"
        ])

        with tab1:
            st.subheader(f"🛡️ Ordonnance Majeure : Le Juge — {juge['nom']}")
            st.markdown(f"**Signification contextuelle :** {juge['signification']}")
            
            col_j1, col_j2 = st.columns(2)
            with col_j1:
                st.info(
                    f"📜 **Textes Sacrés à Graphier :**\n"
                    f"* **Psaume Référent :** {juge['psaume_nom']}\n"
                    f"* **Clé d'écriture :** {juge['cle_psaume']}\n"
                    f"* **Verset de Verrouillage :** {juge['verset_biblique']}"
                )
                st.success(
                    f"🧪 **Éléments de Composition de l'Eau :**\n"
                    f"* **Encre requise :** {juge['encre']}\n"
                    f"* **Plantes d'activation :** {juge['plantes']}\n"
                    f"* **Huiles essentielles :** {juge['huiles_essentielles']}\n"
                    f"* **Parfum de charge :** {juge['parfum']}"
                )
            with col_j2:
                st.warning(
                    f"⚡ **Protocole Cosmique :**\n"
                    f"* **Moment Idéal :** {juge['moment']}\n"
                    f"* **Encens à Brûler :** {juge['encens']}"
                )
                st.write(f"**Sceau Salomonique associé :** *{juge['texte_salomonique']}*")

        with tab2:
            st.subheader(f"🔑 Fixation Finale : La Sentence — {sentence['nom']}")
            st.markdown(f"**Signification contextuelle :** {sentence['signification']}")
            
            col_s1, col_s2 = st.columns(2)
            with col_s1:
                st.error(
                    f"📜 **Textes Sacrés à Graphier :**\n"
                    f"* **Psaume Référent :** {sentence['psaume_nom']}\n"
                    f"* **Clé d'écriture :** {sentence['cle_psaume']}\n"
                    f"* **Verset de Verrouillage :** {sentence['verset_biblique']}"
                )
                st.success(
                    f"🧪 **Éléments de Composition de l'Eau :**\n"
                    f"* **Encre requise :** {sentence['encre']}\n"
                    f"* **Plantes d'activation :** {sentence['plantes']}\n"
                    f"* **Huiles essentielles :** {sentence['huiles_essentielles']}\n"
                    f"* **Parfum de charge :** {sentence['parfum']}"
                )
            with col_s2:
                st.warning(
                    f"⚡ **Protocole Cosmique :**\n"
                    f"* **Moment Idéal :** {sentence['moment']}\n"
                    f"* **Encens à Brûler :** {sentence['encens']}"
                )
                st.write(f"**Sceau Salomonique associé :** *{sentence['texte_salomonique']}*")

        with tab3:
            st.subheader("🧮 Carrés Magiques de Protection Vibratoire")
            st.write(
                "Ces matrices numériques chiffrées doivent être dessinées au dos de votre support d'écriture "
                "ou infusées directement dans le Nassi pour sceller la charge théurgique des Psaumes."
            )
            
            cm_col1, cm_col2 = st.columns(2)
            with cm_col1:
                st.markdown(f"### 📊 Carré du Juge ({juge['psaume_nom']})")
                val_juge = id_p_juge + num_ecritures_juge
                st.code(generer_carre_magique(val_juge), language="text")
                st.caption(f"Calculé sur la base vibratoire de la valeur cible : **{val_juge}**")
                
            with cm_col2:
                st.markdown(f"### 📊 Carré de la Sentence ({sentence['psaume_nom']})")
                val_sent = id_p_sent + num_ecritures_sentence
                st.code(generer_carre_magique(val_sent), language="text")
                st.caption(f"Calculé sur la base vibratoire de la valeur cible : **{val_sent}**")

        with tab4:
            st.subheader("🕊️ Alchimie Complémentaire & Œuvres de Charité")
            
            st.markdown("### 🍎 Les Sacrifices d'Attraction (Saraka)")
            st.markdown(f"**Pour le Juge ({juge['nom']}) :** {juge['saraka']}")
            st.markdown(f"**Pour la Sentence ({sentence['nom']}) :** {sentence['saraka']}")
            
            st.write("---")
            st.markdown(
                "### 🚿 Recommandations strictes pour le Bain Spirituel (Nassi)\n"
                "1. **Liant obligatoire :** Toujours diluer les huiles essentielles dans un peu de lait frais ou de gros sel de cuisine avant de les verser dans l'eau (pour éviter qu'elles ne flottent à la surface).\n"
                "2. **Aucun produit moderne :** Ne jamais utiliser de savon industriel ni d'éponge lors du rinçage.\n"
                "3. **Séchage à l'air libre :** Laissez l'eau sacrée sécher d'elle-même sur votre corps.\n"
                "4. **Respect des Lieux :** Recueillez l'eau dans une bassine pendant votre douche pour éviter qu'elle ne finisse "
                "directement dans les égouts ou les toilettes. Jetez-la ensuite à l'extérieur, sur une terre propre ou au pied d'un arbre."
            )

        st.success("✅ Traitement théurgique calculé avec succès. Que la lumière guide votre rituel.")
