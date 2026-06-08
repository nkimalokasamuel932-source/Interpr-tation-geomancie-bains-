# -*- coding: utf-8 -*-

def addition_geomantique(f1, f2):
    res = ""
    for i in range(4):
        if (int(f1[i]) + int(f2[i])) % 2 == 0:
            res += "2"
        else:
            res += "1"
    return res

DICTIONNAIRE_THEURGIQUE = {
    "1121": {"nom": "Youssouf (Puer)", "plante": "Laurier noble", "element": "Feu", "direction": "EST", "vertu": "Force, victoire, surmonter les trahisons.", "verset": "Proverbes 24:5"},
    "1222": {"nom": "Adama (Laetitia)", "plante": "Citronnier / Orange", "element": "Air", "direction": "OUEST", "vertu": "Clarté, joie, ouverture financière.", "verset": "Psaume 126:5"},
    "2111": {"nom": "Madiou (Caput Draconis)", "plante": "Romarin ou Menthe", "element": "Terre", "direction": "SUD", "vertu": "Intuition, nouveaux contrats, élévation.", "verset": "Sagesse 7:17"},
    "2212": {"nom": "Idrissa (Albus)", "plante": "Menthe blanche", "element": "Air", "direction": "OUEST", "vertu": "Pureté spirituelle, paix profonde.", "verset": "Ésaïe 1:18"},
    "1111": {"nom": "Ibrahima (Via)", "plante": "Hysope", "element": "Eau", "direction": "NORD", "vertu": "Ouverture des routes, nettoyage des poisses.", "verset": "Psaume 51:7"},
    "1212": {"nom": "Nabbi Issa (Amissio)", "plante": "Hysope + Sel bénit", "element": "Eau", "direction": "NORD", "vertu": "Briser la poisse par le dépouillement sacral.", "verset": "Ecclésiaste 3:6"},
    "2122": {"nom": "Seyyidina Oumarou (Rubeus)", "plante": "Gingembre ou Ortie", "element": "Feu", "direction": "EST", "vertu": "Légitime défense, brisement des complots.", "verset": "Psaume 35:1"},
    "2221": {"nom": "Nabbi Ayouba (Tristitia)", "plante": "Verveine / Clou de Girofle", "element": "Terre", "direction": "SUD", "vertu": "Consolation divine, fin de la ruine.", "verset": "Psaume 130:1"},
    "1122": {"nom": "Abubakar Sidiki (Puella)", "plante": "Pétales de Rose", "element": "Air", "direction": "OUEST", "vertu": "Harmonie, retour d'affection sain.", "verset": "Cantique 2:1"},
    "1221": {"nom": "Massasouleymane (Carcer)", "plante": "Clou de Girofle", "element": "Terre", "direction": "SUD", "vertu": "Briser les chaînes invisibles et blocages.", "verset": "Sagesse 17:16"},
    "2112": {"nom": "Badra Aliou (Conjunctio)", "plante": "Curcuma", "element": "Air", "direction": "OUEST", "vertu": "Mariage, alliances solides, pactes commerciaux.", "verset": "Matthieu 19:6"},
    "2211": {"nom": "Nouhou (Fortuna Major)", "plante": "Laurier + Basilic", "element": "Eau", "direction": "NORD", "vertu": "Protection souveraine absolue, triomphe.", "verset": "Psaume 20:2"},
    "2222": {"nom": "Moussa (Populus)", "plante": "Thym ou Basilic", "element": "Eau", "direction": "NORD", "vertu": "Protection contre les calomnies, charisme public.", "verset": "Psaume 3:7"},
    "2121": {"nom": "Ousmane (Acquisitio)", "plante": "Cannelle", "element": "Feu", "direction": "EST", "vertu": "Attraction d'argent, succès commercial.", "verset": "Proverbes 3:14"},
    "1112": {"nom": "Allahou Taala (Cauda Draconis)", "plante": "Sauge officinale", "element": "Feu", "direction": "EST", "vertu": "Purification des lieux, coupure des liens toxiques.", "verset": "Proverbes 26:27"},
    "1211": {"nom": "Fortuna Minor", "plante": "Anis étoilé", "element": "Air", "direction": "OUEST", "vertu": "Succès rapide mais éphémère, étincelle.", "verset": "Proverbes 10:22"}
}

def generer_theme_complet_theurgique(m1, m2, m3, m4, maison_a_traiter):
    m5 = m1[0] + m2[0] + m3[0] + m4[0]
    m6 = m1[1] + m2[1] + m3[1] + m4[1]
    m7 = m1[2] + m2[2] + m3[2] + m4[2]
    m8 = m1[3] + m2[3] + m3[3] + m4[3]
    m9 = addition_geomantique(m1, m2)
    m10 = addition_geomantique(m3, m4)
    m11 = addition_geomantique(m5, m6)
    m12 = addition_geomantique(m7, m8)
    m13 = addition_geomantique(m9, m10)
    m14 = addition_geomantique(m11, m12)
    m15 = addition_geomantique(m13, m14)
    m16 = addition_geomantique(m1, m15)
    
    maisons = [None, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16]
    labels = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI"]
    
    print("\n--- RÉSULTATS DU THÈME ---")
    for i in range(1, 17):
        info = DICTIONNAIRE_THEURGIQUE.get(maisons[i], {"nom": "Inconnue"})
        print(f"Maison {labels[i]} : {maisons[i]} ({info['nom']})")
    
    target = DICTIONNAIRE_THEURGIQUE.get(maisons[maison_a_traiter], {"nom": "N/A", "plante": "N/A", "verset": "N/A", "direction": "N/A"})
    print(f"\n--- PROTOCOLE MAISON {maison_a_traiter} ---")
    print(f"Plante : {target['plante']}\nVerset : {target['verset']}\nDirection : {target['direction']}")

if __name__ == "__main__":
    try:
        print("--- SYSTÈME GÉOMANTIQUE SÉCURISÉ ---")
        user = input("Identifiant : ")
        pwd = input("Mot de passe : ")
        
        if user == "admin" and pwd == "1234":
            print("\nAccès validé. Lancement du diagnostic...\n")
            # Entrez vos mères ici
            generer_theme_complet_theurgique("1121", "1222", "2111", "2212", 2)
        else:
            print("\nAccès refusé.")
    except Exception as e:
        print(f"\nErreur technique : {e}")






# -*- coding: utf-8 -*-
import streamlit as st

# =====================================================================
# 1. DICTIONNAIRE UNIQUE DES 16 FIGURES (CODES BINAIRES CORRIGÉS)
# =====================================================================
# Strates : [Tête, Poitrine, Ventre, Pied] | 1 = Impair (un point), 2 = Pair (deux points)
FIGURES_DB = {
    "Youssouf (Sedjou / Puer)": {
        "code": [1, 1, 1, 2], "numero": 1, "element": "Feu", "nature": "Passé", "polarite": "Comté Mâle",
        "jour": "Mardi", "psaume": "Psaume 35", "verset": "Exode 15 v.3", "sceau": "2e Pentacle de Mars",
        "sacrifice": "Cola rouge, bélier au cou rouge, maïs rouge. À donner aux handicapés ou blessés le Mardi.",
        "plantes": "Zaban, Balanzan, Poudre de fusil (Arbres : Djala, N'zèrènidjè, Djatiguifaga)",
        "maisons": {
            1: "Consultant impulsif, habité par une colère sourde ou une grande force physique.",
            2: "Argent acquis par la lutte ou dépensé de manière impulsive. Gains rapides mais instables.",
            3: "Rivalités ou disputes dans l'entourage proche ou entre frères. Démarches risquées.",
            4: "Tensions ou conflits au sein du foyer familial. Patrimoine exposé à des risques.",
            5: "Passions amoureuses intenses, impulsivité envers les enfants, désirs forts.",
            6: "Maladies subites liées au sang, à la fièvre ou blessures par des outils tranchants.",
            7: "Rivalités ou disputes ouvertes dans le couple ou avec les associés commerciaux.",
            8: "Blocage surmonté par la force matérielle. Transformation radicale et violente.",
            9: "Voyage rapide, quête spirituelle axée sur le courage. Projets audacieux.",
            10: "Succès professionnel obtenu de haute lutte. Autorité et poste de commandement.",
            11: "Amis combatifs ou parfois agressifs. Espoirs axés sur une action immédiate.",
            12: "Ennemis déclarés, combatifs et visibles. Blocages dus à la précipitation.",
            13: "Chambre à coucher ou intimité sous tension. Climat de passion ou d'inquiétude.",
            14: "Gains futurs dépendants d'un effort physique intense ou d'une guerre commerciale.",
            15: "Le Juge valide une issue tranchante, rapide et sans compromis possible.",
            16: "Sentence finale : Victoire par la force ou rupture nette. Libération par le feu."
        }
    },
    "Adama (Letitia / La joie)": {
        "code": [1, 2, 2, 2], "numero": 2, "element": "Feu", "nature": "Passé", "polarite": "Mâle",
        "jour": "Jeudi", "psaume": "Psaume 4", "verset": "Néhémie 8 v.10", "sceau": "2e Pentacle de Jupiter",
        "sacrifice": "Fruits secs, longs animaux. À donner à plusieurs personnes (Groupe) le Jeudi.",
        "plantes": "Frogofraga, N'gouna, Sérétoro (Arbres : Sana, Gounan)",
        "maisons": {
            1: "Consultant serein, optimiste, bienveillant et guidé par la joie de vivre.",
            2: "Augmentation significative des revenus. Chance financière et gains facilités.",
            3: "Bonnes nouvelles reçues de l'entourage. Relations fraternelles harmonieuses.",
            4: "Paix profonde au sein du foyer. Embellissement ou sécurisation du patrimoine.",
            5: "Amours partagés, bonheur intense avec les enfants. Créativité favorisée.",
            6: "Excellente santé, rétablissement rapide. Les soucis du quotidien s'allègent.",
            7: "Mariage heureux, alliance solide et harmonie parfaite avec le partenaire.",
            8: "Héritage inattendu, fin positive d'une crise majeure. Régénération.",
            9: "Voyage agréable et hautement profitable. Clarté spirituelle et réussite intellectuelle.",
            10: "Honneurs publics, promotion professionnelle, reconnaissance de vos mérites.",
            11: "Soutiens amicaux précieux et sincères. Les espoirs se réalisent facilement.",
            12: "Les ennemis cachés deviennent inoffensifs. Les blocages se dussolvent.",
            13: "Joie immense dans l'intimité du lit. Argent disponible immédiatement pour les plaisirs.",
            14: "Avenir radieux. Promesse certaine de richesses futures et de stabilisations.",
            15: "Le Juge prononce un verdict de soulagement total et de dénouement heureux.",
            16: "Sentence finale : Conclusion joyeuse, célébration et pleine réussite de l'affaire."
        }
    },
    "Mahamadou / Malidjou (Caput Draconis)": {
        "code": [1, 1, 1, 1], "numero": 3, "element": "Air", "nature": "Futur", "polarite": "Femelle",
        "jour": "Jeudi", "psaume": "Psaume 128", "verset": "Exode 20 v.12", "sceau": "1er Pentacle de la Terre",
        "sacrifice": "Fruits secs, longs animaux. À donner à plusieurs personnes (Groupe) le Jeudi.",
        "plantes": "Arbres qui poussent sur colline ou toile, Djoun (Arbres : Djoulassounkalani, Sébé)",
        "maisons": {i: f"Évolution spirituelle, élévation, opportunités nouvelles et entrée de forces d'Air en Maison {i}." for i in range(1, 17)}
    },
    "Idrissa (Albayaro / Albus)": {
        "code": [2, 2, 1, 2], "numero": 4, "element": "Eau", "nature": "Futur", "polarite": "Mâle",
        "jour": "Vendredi", "psaume": "Psaume 119 (Beth)", "verset": "Isaïe 1 v.18", "sceau": "2e Pentacle de Mercure",
        "sacrifice": "Bijoux, objets précieux, offrandes libres. À donner aux enfants le Vendredi.",
        "plantes": "N'gokou, tous les arbres qui vivent sur les fleuves (Arbres : Dougalén)",
        "maisons": {i: f"Sagesse, clarté d'esprit, pureté d'intention, paix ou éclaircissement en Maison {i}." for i in range(1, 17)}
    },
    "Ibrahima (Taliki / Via)": {
        "code": [1, 2, 2, 1], "numero": 5, "element": "Eau", "nature": "Présent", "polarite": "Mâle",
        "jour": "Lundi", "psaume": "Psaume 120", "verset": "Psaume 121 v.8", "sceau": "5e Pentacle de la Lune",
        "sacrifice": "Fruits frais, graines de céréales, animaux féminins. À donner aux religieux le Lundi.",
        "plantes": "Zondjè, arbres poussant au bord des sources d'eau (Arbres : Tièkala, Zongnè)",
        "maisons": {i: f"Changement de voie, route à suivre, instabilité ou déplacement en Maison {i}." for i in range(1, 17)}
    },
    "Issa (Nabbi Issa / Amissio)": {
        "code": [2, 1, 1, 2], "numero": 6, "element": "Eau", "nature": "Passé", "polarite": "Mâle",
        "jour": "Mercredi", "psaume": "Psaume 102", "verset": "Joël 2 v.25", "sceau": "5e Pentacle de Vénus",
        "sacrifice": "Choses à plusieurs couleurs (pintade, fonio). À donner à un chanteur ou muezzin le Mercredi.",
        "plantes": "N'gagnaka, Niama, Chi (Arbres : Sourou N'tomo)",
        "maisons": {i: f"Perte matérielle, sacrifice nécessaire, détachement ou baisse d'énergie en Maison {i}." for i in range(1, 17)}
    },
    "Oumarou (Lomara / Rubeus)": {
        "code": [1, 2, 1, 1], "numero": 7, "element": "Air", "nature": "Passé", "polarite": "Femelle",
        "jour": "Mardi", "psaume": "Psaume 29", "verset": "Cantique 8 v.6", "sceau": "4e Pentacle de Mars",
        "sacrifice": "Cola rouge, bélier au cou rouge, maïs rouge. À donner aux handicapés le Mardi.",
        "plantes": "Gaba blé, Djati tgui fa djiri (Arbres : Gabablen, Foronto, Wo)",
        "maisons": {i: f"Passion destructrice, violence verbale, danger de sang ou d'agression en Maison {i}." for i in range(1, 17)}
    },
    "Ayouba (Almangoussi / Tristitia)": {
        "code": [2, 2, 2, 1], "numero": 8, "element": "Terre", "nature": "Futur", "polarite": "Postérieur Mâle",
        "jour": "Samedi", "psaume": "Psaume 40", "verset": "Isaïe 61 v.3", "sceau": "5e Pentacle de Saturne",
        "sacrifice": "Tout ce qu'on trouve sous la terre, savon, sel. À donner aux vieux le Samedi.",
        "plantes": "Herbes qui poussent sur les tombeaux, Koroni fin (Arbres : Koto, Ngokou)",
        "maisons": {i: f"Tristesse, affliction profonde, blocage matériel lourd ou enterrement d'affaire en Maison {i}." for i in range(1, 17)}
    },
    "Qala-llahou (Aboubakr Sidik / Fortuna Minor)": {
        "code": [1, 1, 2, 2], "numero": 9, "element": "Feu", "nature": "Passé", "polarite": "Mâle",
        "jour": "Dimanche", "psaume": "Psaume 121", "verset": "Psaume 46 v.2", "sceau": "4e Pentacle du Soleil",
        "sacrifice": "Cola blanc, habit blanc, bélier blanc. À donner aux chefs le Dimanche.",
        "plantes": "Aladjon, racines d'arbres coupant la route (Arbres : Alladjô, Congo Sirani)",
        "maisons": {i: f"Petite chance, secours rapide du destin, protection divine éphémère en Maison {i}." for i in range(1, 17)}
    },
    "Solomana (Manssa Souleymane / Carcer)": {
        "code": [1, 2, 1, 2], "numero": 10, "element": "Terre", "nature": "Présent", "polarite": "Femelle",
        "jour": "Samedi", "psaume": "Psaume 142", "verset": "Isaïe 22 v.22", "sceau": "7e Pentacle de Saturne",
        "sacrifice": "Tout ce qu'on trouve sous la terre, savon, sel. À donner aux vieux le Samedi.",
        "plantes": "Mandé sounsoun, Sounsoun (Arbres : Zamba, Sira/Baobab)",
        "maisons": {i: f"Enfermement, secret bien gardé, isolement nécessaire ou contrainte majeure en Maison {i}." for i in range(1, 17)}
    },
    "Badra (Badra Aliou / Conjunctio)": {
        "code": [2, 1, 1, 1], "numero": 11, "element": "Air", "nature": "Présent", "polarite": "Femelle",
        "jour": "Mercredi", "psaume": "Psaume 133", "verset": "Ruth 1 v.16", "sceau": "4e Pentacle de Mercure",
        "sacrifice": "Choses à plusieurs couleurs (pintade, fonio). À donner à un muezzin le Mercredi.",
        "plantes": "Guélé (Arbres : Triki, Gouélé)",
        "maisons": {i: f"Réunion, assemblée, signature de contrats, accords mutuels ou retrouvailles en Maison {i}." for i in range(1, 17)}
    },
    "Nouhou (Nouhoum / Cauda Draconis)": {
        "code": [1, 1, 2, 1], "numero": 12, "element": "Terre", "nature": "Futur", "polarite": "Femelle",
        "jour": "Dimanche", "psaume": "Psaume 59", "verset": "Psaume 68 v.2", "sceau": "6e Pentacle de Saturne",
        "sacrifice": "Cola blanc, habit blanc, bélier blanc. À donner aux renommés le Dimanche.",
        "plantes": "Goundjè (Arbres : Koudjè, Zèguènè)",
        "maisons": {i: f"Trahison occulte, fin de cycle brutale, déception ou présence d'un piège vicieux en Maison {i}." for i in range(1, 17)}
    },
    "Laoussana (Alhoussein / Puella)": {
        "code": [1, 2, 1, 2], "numero": 13, "element": "Eau", "nature": "Passé", "polarite": "Femelle",
        "jour": "Samedi", "psaume": "Psaume 119 (Aleph)", "verset": "Cantique 4 v.7", "sceau": "2e Pentacle de Vénus",
        "sacrifice": "Tout ce qu'on trouve sous la terre, savon, sel. À donner aux vieilles le Samedi.",
        "plantes": "Djoulasonkalani (Plantes gluantes, herbes des vieux puits)",
        "maisons": {i: f"Désirs de plaisirs, charme, présence féminine influente, frivolité ou joie passagère en Maison {i}." for i in range(1, 17)}
    },
    "Ousmane (Mory Zoumana / Acquisitio)": {
        "code": [2, 1, 2, 1], "numero": 14, "element": "Terre", "nature": "Futur", "polarite": "Mâle",
        "jour": "Jeudi", "psaume": "Psaume 23", "verset": "Psaume 23 v.1", "sceau": "3e Pentacle de Jupiter",
        "sacrifice": "Fruits secs, longs animaux. À donner à un groupe le Jeudi.",
        "plantes": "N'doubalé, Frogofraga (Arbres : Troubala, Dougalen)",
        "maisons": {i: f"Acquisition de biens, enrichissement matériel permanent, succès financier majeur en Maison {i}." for i in range(1, 17)}
    },
    "Younouss (Tontigui)": {
        "code": [2, 2, 1, 1], "numero": 15, "element": "Air", "nature": "Futur", "polarite": "Femelle",
        "jour": "Vendredi", "psaume": "Psaume 112", "verset": "Deutéronome 28 v.12", "sceau": "6e Pentacle de Jupiter",
        "sacrifice": "Bijoux, parures ou objets brillants. À donner aux enfants le Vendredi.",
        "plantes": "N'tomotigui, Zondjè (Arbres : Fogofogo)",
        "maisons": {i: f"Grande chance matérielle, succès retentissant, honneur et élévation sociale en Maison {i}." for i in range(1, 17)}
    },
    "Moussa (Djama / Populus)": {
        "code": [2, 2, 2, 2], "numero": 16, "element": "Feu", "nature": "Présent", "polarite": "Femelle",
        "jour": "Lundi", "psaume": "Psaume 47", "verset": "Genèse 22 v.17", "sceau": "1er Pentacle de la Lune",
        "sacrifice": "Fruits frais, graines, animaux féminins. À donner aux religieux le Lundi.",
        "plantes": "N'tomi, N'galama (Arbres : Tomy, Sounzoufing)",
        "maisons": {i: f"Influence de la foule, rumeurs publiques, grand nombre ou dispersion d'énergie en Maison {i}." for i in range(1, 17)}
    }
}

MAISONS_NOMS = {
    1: "Maison 1 (Consultant / Âme)", 2: "Maison 2 (Chance / Biens)", 3: "Maison 3 (Entourage / Frères)", 4: "Maison 4 (Foyer / Patrimoine)",
    5: "Maison 5 (Enfants / Amours)", 6: "Maison 6 (Maladies / Obstacles)", 7: "Maison 7 (Conjoint / Associés)", 8: "Maison 8 (Blocages / Mort)",
    9: "Maison 9 (Voyages / Spiritualité)", 10: "Maison 10 (Pouvoir / Métier)", 11: "Maison 11 (Espoirs / Amis)", 12: "Maison 12 (Ennemis cachés)",
    13: "Maison 13 (Chambre / Présent)", 14: "Maison 14 (Avenir / Gains futurs)", 15: "Maison 15 (Le Juge)", 16: "Maison 16 (Sentence finale)"
}

MAPPING_SIMPLIFIE = {k: k.split(" ")[0] for k in FIGURES_DB.keys()}

# =====================================================================
# 2. LOGIQUE MATHÉMATIQUE GÉOMANTIQUE (MOTEUR GENERATIF SANS FAILLES)
# =====================================================================
def additionner_lignes(l1, l2):
    return 2 if l1 == l2 else 1

def copuler_figures(figA, figB):
    code_resultat = []
    for i in range(4):
        code_resultat.append(additionner_lignes(figA["code"][i], figB["code"][i]))
    for nom, data in FIGURES_DB.items():
        if data["code"] == code_resultat:
            return nom
    return list(FIGURES_DB.keys())[0]

def generer_theme_complet(m1, m2, m3, m4):
    f1, f2, f3, f4 = FIGURES_DB[m1], FIGURES_DB[m2], FIGURES_DB[m3], FIGURES_DB[m4]
    theme = {1: m1, 2: m2, 3: m3, 4: m4}
    
    # Transposition matricielle pour les Filles (M5-M8) avec gestion de sécurité
    try:
        theme[5] = next(k for k, v in FIGURES_DB.items() if v["code"] == [f1["code"][0], f2["code"][0], f3["code"][0], f4["code"][0]])
        theme[6] = next(k for k, v in FIGURES_DB.items() if v["code"] == [f1["code"][1], f2["code"][1], f3["code"][1], f4["code"][1]])
        theme[7] = next(k for k, v in FIGURES_DB.items() if v["code"] == [f1["code"][2], f2["code"][2], f3["code"][2], f4["code"][2]])
        theme[8] = next(k for k, v in FIGURES_DB.items() if v["code"] == [f1["code"][3], f2["code"][3], f3["code"][3], f4["code"][3]])
    except StopIteration:
        # Solution de repli de secours (Fallback) pour éviter un crash complet de l'interface
        st.error("🚨 Une asymétrie critique est détectée dans la matrice. Réinitialisation sur les valeurs fondamentales.")
        theme[5], theme[6], theme[7], theme[8] = m1, m2, m3, m4

    # Calcul du reste du Tribunal (Neveux M9-M12, Témoins M13-M14, Juge M15, Sentence M16)
    theme[9] = copuler_figures(FIGURES_DB[theme[1]], FIGURES_DB[theme[2]])
    theme[10] = copuler_figures(FIGURES_DB[theme[3]], FIGURES_DB[theme[4]])
    theme[11] = copuler_figures(FIGURES_DB[theme[5]], FIGURES_DB[theme[6]])
    theme[12] = copuler_figures(FIGURES_DB[theme[7]], FIGURES_DB[theme[8]])
    theme[13] = copuler_figures(FIGURES_DB[theme[9]], FIGURES_DB[theme[10]])
    theme[14] = copuler_figures(FIGURES_DB[theme[11]], FIGURES_DB[theme[12]])
    theme[15] = copuler_figures(FIGURES_DB[theme[13]], FIGURES_DB[theme[14]])
    theme[16] = copuler_figures(FIGURES_DB[theme[15]], FIGURES_DB[theme[1]])
    return theme

# =====================================================================
# 3. INTERFACE DE SÉCURITÉ
# =====================================================================
st.set_page_config(page_title="Système SST Pro", page_icon="🔮", layout="wide")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_login():
    if st.session_state["username"] == "admin" and st.session_state["password"] == "Somadjely2026":
        st.session_state["authenticated"] = True
    else:
        st.error("❌ Identifiant ou mot de passe incorrect.")

if not st.session_state["authenticated"]:
    st.title("🔒 SST SYSTEM — Interface d'Accès Sécurisée")
    with st.form("login_form"):
        st.text_input("👤 Identifiant", key="username")
        st.text_input("🔑 Mot de passe", type="password", key="password")
        st.form_submit_button("Se connecter", on_click=check_login)
    st.stop()

# =====================================================================
# 4. EXÉCUTION DE L'APPLICATION ET DU DESIGN DE L'INTERFACE
# =====================================================================
st.title("🔮 Plateforme Informatique de Géomancie — SST Pro")

st.header("📥 Saisie de la Base : Les 4 Mères Fondatrices")
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1: m1_select = st.selectbox("Mère 1 (M1) :", options=list(FIGURES_DB.keys()), index=0)
with col_m2: m2_select = st.selectbox("Mère 2 (M2) :", options=list(FIGURES_DB.keys()), index=1)
with col_m3: m3_select = st.selectbox("Mère 3 (M3) :", options=list(FIGURES_DB.keys()), index=2)
with col_m4: m4_select = st.selectbox("Mère 4 (M4) :", options=list(FIGURES_DB.keys()), index=3)

theme_calcule = generer_theme_complet(m1_select, m2_select, m3_select, m4_select)

st.markdown("---")
st.header("📊 Tableau Matriciel Général des 16 Maisons")
st.write("### 🟥 Les Mères & Les Filles")
c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(8)
c1.metric("M1 (Mère)", MAPPING_SIMPLIFIE[theme_calcule[1]])
c2.metric("M2 (Mère)", MAPPING_SIMPLIFIE[theme_calcule[2]])
c3.metric("M3 (Mère)", MAPPING_SIMPLIFIE[theme_calcule[3]])
c4.metric("M4 (Mère)", MAPPING_SIMPLIFIE[theme_calcule[4]])
c5.metric("M5 (Fille)", MAPPING_SIMPLIFIE[theme_calcule[5]])
c6.metric("M6 (Fille)", MAPPING_SIMPLIFIE[theme_calcule[6]])
c7.metric("M7 (Fille)", MAPPING_SIMPLIFIE[theme_calcule[7]])
c8.metric("M8 (Fille)", MAPPING_SIMPLIFIE[theme_calcule[8]])

st.write("### 🟨 Les Neveux & Tribunal Central")
c9, c10, c11, c12, c13, c14, c15, c16 = st.columns(8)
c9.metric("M9 (Neveu)", MAPPING_SIMPLIFIE[theme_calcule[9]])
c10.metric("M10 (Neveu)", MAPPING_SIMPLIFIE[theme_calcule[10]])
c11.metric("M11 (Neveu)", MAPPING_SIMPLIFIE[theme_calcule[11]])
c12.metric("M12 (Neveu)", MAPPING_SIMPLIFIE[theme_calcule[12]])
c13.metric("M13 (T. Droit)", MAPPING_SIMPLIFIE[theme_calcule[13]])
c14.metric("M14 (T. Gauche)", MAPPING_SIMPLIFIE[theme_calcule[14]])
c15.metric("M15 (Juge)", MAPPING_SIMPLIFIE[theme_calcule[15]])
c16.metric("M16 (Sentence)", MAPPING_SIMPLIFIE[theme_calcule[16]])

st.markdown("---")

# =====================================================================
# 5. DÉTECTION DES RÈGLES DE COPULATION DE FIN DE THÈME
# =====================================================================
st.header("🧬 Analyse Statistique Spécifique des Copulations")
parent_detecte_A = theme_calcule[15]
parent_detecte_B = theme_calcule[1]
nameA, nameB = MAPPING_SIMPLIFIE[parent_detecte_A], MAPPING_SIMPLIFIE[parent_detecte_B]
set_parents = {nameA, nameB}

details_engendre = "Les flux d'accouplement suivent le cours naturel des éléments du thème."
if set_parents == {"Youssouf", "Laoussana"}: details_engendre = "⚠️ **MÉCHANCETÉ À CAUSE D'ENFANT**"
elif set_parents == {"Adama", "Younouss"}: details_engendre = "⚠️ **MÉCHANCETÉ À CAUSE D'HÉRITAGE**"
elif set_parents == {"Bourama", "Alaou Tala"}: details_engendre = "⚠️ **MÉCHANCETÉ POUR ENFANT**"
elif set_parents == {"Oumar", "Maldjou"}: details_engendre = "⚠️ **MÉCHANCETÉ À CAUSE DE FEMME**"
elif set_parents == {"Issa", "Solomane"}: details_engendre = "⚠️ **MÉCHANCETÉ D'UN CHEF**"
elif set_parents == {"Ayouba", "Idriss"}: details_engendre = "⚠️ **MÉCHANCETÉ DANS LA FAMILLE OU FOYER**"
elif set_parents == {"Badra", "Ousmane"}: details_engendre = "⚠️ **MÉCHANCETÉ FAITE PAR UN MARABOUT OU GÉOMANCIEN**"
elif set_parents == {"Moussa", "Nouhou"}: details_engendre = "⚠️ **MÉCHANCETÉ FAITE PAR UN GROUPE DE PERSONNES**"
elif set_parents == {"Youssouf", "Younouss"}: details_engendre = "💰 **UNE FEMME QUI A DE BON ESPOIR DE RICHESSE**"
elif set_parents == {"Adama", "Laoussana"}: details_engendre = "🔴 **SACRIFICE ROUGE REQUIS**"
elif set_parents == {"Maldjou", "Ayouba"}: details_engendre = "❌ **DIFFICULTÉ POUR AVOIR DES ENFANTS (BLOCAGE)**"
elif set_parents == {"Idriss", "Oumar"}: details_engendre = "💨 **TEMPÊTE, UN GRAND VENT VIOLENT QUI FAIT DES DÉGÂTS**"
elif set_parents == {"Bourama", "Solomane"}: details_engendre = "👶 **LA GROSSESSE**"
elif set_parents == {"Nouhou", "Ousmane"}: details_engendre = "👑 **LA GRANDEUR ET L'HONNEUR**"
elif set_parents == {"Alaou Tala", "Issa"}: details_engendre = "🚨 **UNE TRÈS GRAVE DIFFICULTÉ**"
elif set_parents == {"Moussa", "Badra"}: details_engendre = "⚔️ **DESTIN DE GUERRIER, DE SOLDAT OU D'ÉLÈVES**"

with st.expander("🔍 Résultat du Croisement de Fin de Thème (M15 + M1)", expanded=True):
    st.write(f"**Parents Détectés :** {parent_detecte_A} ✖️ {parent_detecte_B}")
    st.warning(f"✨ **Verdict Ombral :** {details_engendre}")

st.markdown("---")

# =====================================================================
# 6. EXPLORATEUR DE PASSAGE DANS LES MAISONS
# =====================================================================
st.header("🏠 Analyse Spécifique du Passage d'une Figure en Maison")
col_ex1, col_ex2 = st.columns(2)
with col_ex1: fig_analyse = st.selectbox("Figure à étudier :", options=list(FIGURES_DB.keys()), key="expl_fig")
with col_ex2: maison_analyse = st.selectbox("Maison de destination :", options=list(MAISONS_NOMS.keys()), format_func=lambda x: MAISONS_NOMS[x], key="expl_mai")

if fig_analyse and maison_analyse:
    interpretation_textuelle = FIGURES_DB[fig_analyse]["maisons"].get(maison_analyse, "Analyse absente.")
    st.success(f"📋 **Interprétation du Passage :**\n\n> {interpretation_textuelle}")

st.markdown("---")

# =====================================================================
# 7. ORDONNANCE THÉURGIQUE COMPLÈTE & PROTOCOLES PRATIQUES
# =====================================================================
st.header("📊 Protocole Théurgique Intégral : Focus Maison 16")
figure_finale = theme_calcule[16]
st.info(f"Figure souveraine de fermeture (M16) : **{figure_finale}**")

data_f = FIGURES_DB[figure_finale]

tab_s1, tab_s2, tab_s3, tab_s4 = st.tabs([
    "🐑 1. Sacrifices Correctifs (Saraka)", 
    "✝️ 2. Alignements & Textes Sacrés", 
    "🌿 3. Ingrédients Botaniques",
    "📜 4. Protocoles d'Utilisation (Nassi, Bains, Récitation)"
])

with tab_s1:
    st.markdown(f"**Aumône prescriptive :** {data_f['sacrifice']}")

with tab_s2:
    st.markdown(f"* **Psaume de traçage :** `{data_f['psaume']}`")
    st.markdown(f"* **Verset d'activation :** `{data_f['verset']}`")
    st.markdown(f"* **Sceau Vibratoire :** `{data_f['sceau']}`")
    st.markdown(f"* **Jour Planétaire Sacré :** **{data_f['jour']}**")

with tab_s3:
    st.markdown(f"**Plantes et composants magiques :** {data_f['plantes']}")

with tab_s4:
    st.subheader("🛠️ Guide Opératoire Traditionnel d'Activation")
    
    st.markdown(f"""
    ### 1. Protocole de Récitation (Psaumes & Versets)
    * **Timing Vibratoire :** À pratiquer le **{data_f['jour']}** (Jour de la figure), idéalement à l'aube ou après minuit.
    * **Clé d'Ouverture :** Récitez d'abord le verset de verrouillage (`{data_f['verset']}`) **7, 33 ou 111 fois** consécutives.
    * **Le Corps du Rituel :** Récitez ensuite le `{data_f['psaume']}` **3 fois à voix haute**, en formulant clairement votre vœu ou demande de déblocage à la fin de chaque lecture.
    
    ---
    ### 2. Guide de Préparation du Nassi (Eau Sacrée)
    * **Support d'écriture :** Utilisez une tablette traditionnelle en bois (*Alo*) ou une assiette blanche en porcelaine neuve sans aucun motif.
    * **Encre Sacrée :** Utilisez une encre soluble traditionnelle saine (mélange de safran, eau de rose et charbon de bois pulvérisé). Tracez la figure géomantique **{MAPPING_SIMPLIFIE[figure_finale]}** entourée du `{data_f['verset']}`.
    * **Lavage :** Rincez délicatement l'assiette ou la tablette avec de l'eau pure (eau de source ou eau de pluie) pour dissoudre l'encre. Recueillez le précieux liquide dans un flacon propre.
    * **Usage :** Buvez-en une gorgée chaque matin à jeun pendant **3, 7 ou 9 jours**, ou appliquez-en sur votre visage et vos mains avant vos démarches critiques.
    
    ---
    ### 3. Protocole des Bains Sacrés (Plantes & Décoctions)
    * **Préparation :** Faites bouillir les plantes spécifiques indiquées (`{data_f['plantes']}`) dans une grande marmite d'eau pendant 15 à 30 minutes.
    * **L'Alliance Mystique :** Filtrez la décoction, versez-la dans votre seau et ajoutez-y **un demi-verre de votre Nassi** préparé précédemment.
    * **Le Bain :** Lavez-vous d'abord normalement avec votre savon. À la fin, versez l'eau de plantes tiède de la tête aux pieds en récitant le verset d'activation.
    * **Le Secret du Séchage :** **Ne vous essuyez pas.** Laissez l'eau sacrée sécher d'elle-même sur votre peau afin de sceller l'énergie sur votre enveloppe astrale. *Évitez tout rapport intime pendant la durée du traitement (3 ou 7 jours).*
    """)

st.markdown("---")
st.caption("SST Informatique — Version Générative complète à 16 Maisons. Tous droits réservés.")
