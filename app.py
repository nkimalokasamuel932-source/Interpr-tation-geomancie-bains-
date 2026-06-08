# -*- coding: utf-8 -*-

def addition_geomantique(f1, f2):
    """
    Effectue la copulation binaire exacte entre deux figures géomantiques.
    Règle de parité universelle du Maître Somadjely : 
    Impair+Impair=Pair (1+1=2), Pair+Pair=Pair (2+2=2), Impair+Pair=Impair (1+2=1)
    """
    res = ""
    for i in range(4):
        if (int(f1[i]) + int(f2[i])) % 2 == 0:
            res += "2"
        else:
            res += "1"
    return res

# Base de données théurgique sacrée : Figures, Plantes douces, Psaumes et Éléments
DICTIONNAIRE_THEURGIQUE = {
    "1121": {
        "nom": "Youssouf (Puer / Le Garçon)",
        "plante": "Laurier noble (Feuilles)",
        "element": "Feu",
        "direction": "EST",
        "vertu": "Force, victoire éclatante, surmonter les trahisons et les rivalités de l'ombre.",
        "verset": "Proverbes 24:5 — 'Un homme sage est plein de force, et celui qui a de la science affermit sa vigueur.'"
    },
    "1222": {
        "nom": "Adama (Laetitia / La Joie)",
        "plante": "Citronnier (Écorce ou feuilles) ou Orange",
        "element": "Air",
        "direction": "OUEST",
        "vertu": "Clarté de l'esprit, joie de vivre, déblocage et ouverture financière immédiate.",
        "verset": "Psaume 126:5 — 'Ceux qui sèment avec larmes moissonneront avec chants de triomphe.'"
    },
    "2111": {
        "nom": "Madiou / Mouhamadou (Caput Draconis / La Tête du Dragon)",
        "plante": "Romarin ou Menthe poivrée",
        "element": "Terre",
        "direction": "SUD",
        "vertu": "Illumination mystique, intuition accrue, élévation intellectuelle et nouveaux contrats.",
        "verset": "Sagesse de Salomon 7:17 — 'C'est lui qui m'a donné une science véritable de ce qui existe...'"
    },
    "2212": {
        "nom": "Idrissa (Albus / Le Blanc)",
        "plante": "Menthe blanche ou Camomille",
        "element": "Air",
        "direction": "OUEST",
        "vertu": "Pureté spirituelle, paix profonde, clarté mentale et neutralisation de la haine.",
        "verset": "Ésaïe 1:18 — 'Si vos péchés sont comme le cramoisi, ils deviendront blancs comme la neige.'"
    },
    "1111": {
        "nom": "Ibrahima (Via / Le Chemin)",
        "plante": "Hysope (Plante majeure de purification)",
        "element": "Eau",
        "direction": "NORD",
        "vertu": "Ouverture des routes bloquées, grand nettoyage des impuretés et des poisses du destin.",
        "verset": "Psaume 51:7 — 'Purifie-moi avec l'hysope, et je serai pur; lave-moi, et je serai plus blanc que la neige.'"
    },
    "1212": {
        "nom": "Nabbi Issa (Amissio / La Perte)",
        "plante": "Hysope + une pincée de Sel bénit",
        "element": "Eau",
        "direction": "NORD",
        "vertu": "Acceptation sacrée, briser la pauvreté ou la poisse tenace par le dépouillement spirituel.",
        "verset": "Ecclésiaste 3:6 — 'Il y a un temps pour chercher, et un temps pour perdre; un temps pour garder...'"
    },
    "2122": {
        "nom": "Seyyidina Oumarou (Rubeus / Le Rouge)",
        "plante": "Gingembre frais ou Ortie",
        "element": "Feu",
        "direction": "EST",
        "vertu": "Théurgie de légitime défense, retour à l'envoyeur et brisement des complots de sang/colère.",
        "verset": "Psaume 35:1 — 'Seigneur, défends-moi contre mes adversaires, combats ceux qui me combattent !'"
    },
    "2221": {
        "nom": "Nabbi Ayouba (Tristitia / La Tristesse)",
        "plante": "Verveine ou Clou de Girofle",
        "element": "Terre",
        "direction": "SUD",
        "vertu": "Consolation divine, libération de la dépression et brisement des décrets de ruine matérielle.",
        "verset": "Psaume 130:1 — 'Du fond de l'abîme je t'invoque, ô Éternel ! Seigneur, écoute ma voix !'"
    },
    "1122": {
        "nom": "Abubakar Sidiki (Puella / La Fille)",
        "plante": "Pétales de Rose ou feuilles de Framboisier",
        "element": "Air",
        "direction": "OUEST",
        "vertu": "Grâce, harmonie relationnelle, retour d'affection sain et pacification des conflits.",
        "verset": "Cantique des Cantiques 2:1 — 'Je suis un narcisse de Saron, un lys des vallées.'"
    },
    "1221": {
        "nom": "Massasouleymane (Carcer / La Prison)",
        "plante": "Clou de Girofle (Infusion très concentrée)",
        "element": "Terre",
        "direction": "SUD",
        "vertu": "Briser les chaînes invisibles, débloquer les situations totalement figées ou emprisonnées.",
        "verset": "Sagesse de Salomon 17:16 — 'Quiconque tombait là restait prisonnier, enfermé dans cette prison sans barreaux.'"
    },
    "2112": {
        "nom": "Badra Aliou (Conjunctio / L'Union)",
        "plante": "Curcuma (Poudre ou racine)",
        "element": "Air",
        "direction": "OUEST",
        "vertu": "Alliances commerciales solides, mariages harmonieux, sceller des pactes durables.",
        "verset": "Matthieu 19:6 — 'Que l'homme ne sépare donc pas ce que Dieu a joint.'"
    },
    "2211": {
        "nom": "Nouhou (Fortuna Major / La Grande Chance)",
        "plante": "Laurier noble + Basilic (Mélange royal)",
        "element": "Eau",
        "direction": "NORD",
        "vertu": "Protection souveraine absolue, triomphe complet face aux épreuves, stabilisation des acquis.",
        "verset": "Psaume 20:2 — 'Que l'Éternel t'exauce au jour de la détresse, que le nom du Dieu de Jacob te protège !'"
    },
    "2222": {
        "nom": "Moussa (Populus / Le Peuple)",
        "plante": "Thym ou Basilic commun",
        "element": "Eau",
        "direction": "NORD",
        "vertu": "Protection contre les calomnies, se faire aimer des foules, charisme public et commercial.",
        "verset": "Psaume 3:7 — 'Je ne crains pas les milliers de peuples qui m'environnent de tous côtés.'"
    },
    "2121": {
        "nom": "Ousmane (Acquisitio / Le Gain)",
        "plante": "Cannelle (Bâtons infusés ou poudre)",
        "element": "Feu",
        "direction": "EST",
        "vertu": "Attraction magnétique de l'argent, succès commercial, prospérité dans les affaires.",
        "verset": "Proverbes 3:14 — 'Car le gain qu'elle procure est préférable à celui de l'argent, et le profit vaut mieux que l'or.'"
    },
    "1112": {
        "nom": "Allahou Taala (Cauda Draconis / La Queue du Dragon)",
        "plante": "Sauge officinale",
        "element": "Feu",
        "direction": "EST",
        "vertu": "Purification des lieux, coupure nette avec les liens toxiques et les envoûtements.",
        "verset": "Proverbes 26:27 — 'Celui qui creuse une fosse y tombe, et la pierre revient sur celui qui la roule.'"
    },
    "1211": {
        "nom": "Fortuna Minor (La Petite Chance)",
        "plante": "Anis étoilé (Badiane)",
        "element": "Air",
        "direction": "OUEST",
        "vertu": "Succès rapide mais éphémère, étincelle créative, protection mineure en voyage.",
        "verset": "Proverbes 10:22 — 'C'est la bénédiction de l'Éternel qui enrichit, et il n'y joint aucun chagrin.'"
    }
}

def calculer_duree_et_bloc(maison_cible):
    """
    Détermine la durée numérologique exacte et le diagnostic spirituel 
    du bloc associé selon la grille temporelle de Zoumana Koné-Somadjely.
    """
    if maison_cible in [1, 2, 3, 4, 5, 6, 7, 8, 15]:
        return 7, "BLOC DU PASSÉ (Délivrance, nettoyage karmique, briser de vieux blocages d'enfance ou d'ancêtres)."
    elif maison_cible in [9, 10, 13, 16]:
        return 3, "BLOC DU PRÉSENT (Action immédiate, déblocage urgent d'un dossier, d'un emploi ou d'un procès en cours)."
    elif maison_cible in [11, 12, 14]:
        return 9, "BLOC DU FUTUR (Sécurisation des projets à venir, installation d'une chance stable pour les mois/années à venir)."
    return 7, "Bloc Indéterminé"

def generer_theme_complet_theurgique(m1, m2, m3, m4, maison_a_traiter=1):
    """
    Calcule l'intégralité du thème géomantique à partir des 4 mères fournies,
    puis dresse le protocole thérapeutique sur-mesure (sans effusion de sang).
    """
    # Génération des 4 Filles (M5 à M8) par transposition horizontale
    m5 = m1[0] + m2[0] + m3[0] + m4[0]
    m6 = m1[1] + m2[1] + m3[1] + m4[1]
    m7 = m1[2] + m2[2] + m3[2] + m4[2]
    m8 = m1[3] + m2[3] + m3[3] + m4[3]

    # Génération des 4 Neveux (M9 à M12)
    m9 = addition_geomantique(m1, m2)
    m10 = addition_geomantique(m3, m4)
    m11 = addition_geomantique(m5, m6)
    m12 = addition_geomantique(m7, m8)

    # Calcul du Tribunal (M13 à M16)
    m13 = addition_geomantique(m9, m10)
    m14 = addition_geomantique(m11, m12)
    m15 = addition_geomantique(m13, m14)
    m16 = addition_geomantique(m1, m15)

    maisons = [None, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16]
    labels = [
        "", "I (Le Consultant)", "II (Les Finances/Chance)", "III (Entourage proche/Frères)", "IV (Le Foyer/Patrimoine)",
        "V (Amours/Enfants/Projets)", "VI (Maladies/Colères)", "VII (Le Conjoint/Les Unions)", "VIII (Les Pertes/La Mort)",
        "IX (Les Voyages/La Quête)", "X (L'Élévation/L'Emploi)", "XI (Les Espoirs/Les Appuis)", "XII (Les Obstacles/Ennemis)",
        "XIII (Le Juge Droit)", "XIV (Le Juge Gauche)", "XV (Le Juge Suprême)", "XVI (La Sentence Finale)"
    ]

    print("=" * 85)
    print("      SYSTÈME GÉOMANTIQUE D'ORIENTATION & THÉURGIE BIBLIQUE (SANS SACRIFICE)      ")
    print("=" * 85 + "\n")

    print("[1. CALCUL AUTOMATISÉ DU THÈME GÉOMANTIQUE]")
    print("-" * 85)
    for i in range(1, 17):
        code = maisons[i]
        infos = DICTIONNAIRE_THEURGIQUE.get(code, {"nom": "Figure Inconnue"})
        print(f" Maison {i:02d} | {labels[i]:28} : {code} -> {infos['nom']}")
    
    # Validation mathématique du thème (Parité universelle du Juge M15)
    total_points_m15 = sum(int(x) for x in m15)
    print("\n[2. DIAGNOSTIC DE CONFORMITÉ MATRICIELLE]")
    print("-" * 85)
    if total_points_m15 % 2 == 0:
        print(f" ✅ THÈME CONFORME : Le Juge Suprême (M15) totalise {total_points_m15} points (Nombre PAIR).")
    else:
        print(f" ❌ SÉCURITÉ EN ÉCHEC : Le Juge (M15) totalise {total_points_m15} points (Nombre IMPAIR). Vérifiez les mères.")

    # Construction de l'aide au soin de la maison sélectionnée
    print(f"\n[3. ANALYSE ET ORIENTATION DU SOIN (MAISON {maison_a_traiter})]")
    print("-" * 85)
    code_cible = maisons[maison_a_traiter]
    infos_cibles = DICTIONNAIRE_THEURGIQUE.get(code_cible)
    nb_jours, bloc_description = calculer_duree_et_bloc(maison_a_traiter)
    
    print(f" 🎯 Secteur de vie ciblé   : {labels[maison_a_traiter]}")
    print(f" ⚜️ Figure à traiter       : {infos_cibles['nom']} (Code binaire: {code_cible})")
    print(f" 🌀 Élément cosmique      : {infos_cibles['element']}")
    print(f" 🧭 Orientation de la chance: L'énergie de cette affaire se dirige vers l' {infos_cibles['direction']}.")
    print(f" 🌿 Plante douce requise  : {infos_cibles['plante']}")
    print(f" ✨ Propriété spirituelle  : {infos_cibles['vertu']}")
    print(f" 📖 Parole de Puissance   : {infos_cibles['verset']}")
    print(f" ⏳ Grille Chronologique  : {bloc_description}")
    print(f" 📅 Durée numérologique   : {nb_jours} jours consécutifs de traitement par le bain (Nassi).")
    
    print("\n[4. PROTOCOLE D'APPLICATION PRATIQUE DU NASSI CHRÉTIEN]")
    print("-" * 85)
    print(" 1. BOUSSOLE   : Installez-vous impérativement FACE AU NORD pour toutes les étapes du travail.")
    print(" 2. CALLIGRAPHIE: Dessinez la figure géomantique au centre d'une feuille propre, puis écrivez")
    print("                 le verset de puissance ou le Psaume tout autour (répété 7 fois).")
    print(" 3. INFUSION    : Faites bouillir la plante correspondante dans de l'eau claire pendant 10 minutes.")
    print(" 4. DISSOLUTION : Versez l'eau tiède sur la feuille pour y dissoudre l'encre (création de votre Nassi).")
    print(f" 5. LE BAIN     : Divisez le liquide obtenu en {nb_jours} bouteilles.")
    print("                 Chaque soir, versez une part dans un seau d'eau tiède. Lavez-vous de la tête aux pieds")
    print("                 (sans savon, ni éponge) après votre douche usuelle. Laissez sécher sur la peau.")
    print(" 6. ÉVOCATION   : Face au Nord, récitez le Psaume ou verset à haute voix 3 ou 7 fois pendant le bain.")
    print("=" * 85)


# =====================================================================
# ZONE DE COMMANDE STRICTE (L'ERREUR A ÉTÉ ENTIÈREMENT CORRIGÉE ICI)
# =====================================================================
if __name__ == "__main__":
    # 1. Définition des 4 figures mères avec la bonne nomenclature
    M1_SCRIPT = "1121"  
    M2_SCRIPT = "1222"  
    M3_SCRIPT = "2111"  
    M4_SCRIPT = "2212"  

    # 2. Définition de la maison à soigner
    MAISON_A_SOIGNER = 2 

    # 3. Appel de la fonction avec les exactes mêmes variables majuscules
    generer_theme_complet_theurgique(M1_SCRIPT, M2_SCRIPT, M3_SCRIPT, M4_SCRIPT, maison_a_traiter=MAISON_A_SOIGNER)
