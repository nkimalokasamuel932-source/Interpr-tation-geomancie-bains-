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

def generer_theme_auto():
    # Définition des 4 mères par défaut
    m1, m2, m3, m4 = "1121", "1222", "2111", "2212"
    maison_cible = 2
    
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
    
    print("\n--- RÉSULTATS DU THÈME AUTOMATIQUE ---")
    for i in range(1, 17):
        info = DICTIONNAIRE_THEURGIQUE.get(maisons[i], {"nom": "Inconnue"})
        print(f"Maison {labels[i]} : {maisons[i]} ({info['nom']})")
    
    target = DICTIONNAIRE_THEURGIQUE.get(maisons[maison_cible], {"nom": "N/A", "plante": "N/A", "verset": "N/A", "direction": "N/A"})
    print(f"\n--- PROTOCOLE MAISON {maison_cible} ---")
    print(f"Plante : {target['plante']}\nVerset : {target['verset']}\nDirection : {target['direction']}")

if __name__ == "__main__":
    generer_theme_auto()
