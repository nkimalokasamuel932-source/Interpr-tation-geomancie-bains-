# -*- coding: utf-8 -*-
"""
SST - SYSTÈME INFORMATIQUE DE GÉOMANCIE TRADITIONNELLE (VERSION SÉCURISÉE UI)
"""

# Base de données immuable des 16 figures
FIGURES_DB = {
    "1121": {"nom": "Youssouf (Sedjou / Puer)", "sexe": "Mâle", "nature": "Variable/Difficulté", "arbres": ["Djala", "N'zèrènidjè", "Djatiguifaga", "Zaban", "Balanzan"], "plantes_sacrees": "Zaban, Balanzan, Poudre de fusil", "psaume": "Psaume 35", "verset": "Exode 15:3", "sceau": "2e Pentacle de Mars", "jour_sacrifice": "Mardi"},
    "1222": {"nom": "Adama (Letitia / La joie)", "sexe": "Mâle", "nature": "Bénéfique/Joie", "arbres": ["Sana", "Gounan", "Frogofraga", "N'gouna", "Sérétoro"], "plantes_sacrees": "Frogofraga, N'gouna, Sérétoro", "psaume": "Psaume 4", "verset": "Néhémie 8:10", "sceau": "2e Pentacle de Jupiter", "jour_sacrifice": "Jeudi"},
    "2111": {"nom": "Mahamadou / Malidjou (Caput Draconis)", "sexe": "Femelle", "nature": "Variable/Élévation", "arbres": ["Djoulassounkalani", "Sébé"], "plantes_sacrees": "Arbres qui poussent sur colline ou toile, Djoun", "psaume": "Psaume 128", "verset": "Exode 20:12", "sceau": "1er Pentacle de la Terre", "jour_sacrifice": "Jeudi"},
    "2212": {"nom": "Idrissa (Albayaro / Idriss)", "sexe": "Mâle", "nature": "Bénéfique", "arbres": ["Dougalén", "N'gokou"], "plantes_sacrees": "N'gokou, tous les arbres qui vivent sur les fleuves", "psaume": "Psaume 119 (Beth)", "verset": "Isaïe 1:18", "sceau": "2e Pentacle de Mercure", "jour_sacrifice": "Vendredi"},
    "1111": {"nom": "Ibrahima (Taliki / Bourama / Via)", "sexe": "Mâle", "nature": "Variable/Mouvement", "arbres": ["Tièkala", "Zongnè", "Zondjè"], "plantes_sacrees": "Zondjè, arbres poussant au bord des sources d'eau", "psaume": "Psaume 120", "verset": "Psaume 121:8", "sceau": "5e Pentacle de la Lune", "jour_sacrifice": "Lundi"},
    "1212": {"nom": "Issa (Nabbi Issa / Enzan)", "sexe": "Mâle", "nature": "Maléfique/Échec", "arbres": ["N'gagnaka", "Sourou N'tomo", "Niama", "Chi"], "plantes_sacrees": "N'gagnaka, Niama, Chi", "psaume": "Psaume 102", "verset": "Joël 2:25", "sceau": "5e Pentacle de Vénus", "jour_sacrifice": "Mercredi"},
    "2122": {"nom": "Oumarou (Seyyidina Oumarou / Lomara)", "sexe": "Femelle", "nature": "Maléfique/Feu/Sang", "arbres": ["Gabablen", "Foronto", "Wo", "Djati tgui fa djiri"], "plantes_sacrees": "Gaba blé, Djati tgui fa djiri", "psaume": "Psaume 29", "verset": "Cantique 8:6", "sceau": "4e Pentacle de Mars", "jour_sacrifice": "Mardi"},
    "2221": {"nom": "Ayouba (Nabbi Ayouba / Almangoussi)", "sexe": "Mâle", "nature": "Maléfique/Tristesse", "arbres": ["Koronifing", "Koto", "Ngokou"], "plantes_sacrees": "Herbes qui poussent sur tombeau, Koroni fin", "psaume": "Psaume 40", "verset": "Isaïe 61:3", "sceau": "5e Pentacle de Saturne", "jour_sacrifice": "Samedi"},
    "1122": {"nom": "Allahou talla (Aboubakr Sidik)", "sexe": "Mâle", "nature": "Bénéfique", "arbres": ["Alladjô", "Congo Sirani"], "plantes_sacrees": "Aladjon, racines d'arbres coupant la route", "psaume": "Psaume 121", "verset": "Psaume 46:2", "sceau": "4e Pentacle du Soleil", "jour_sacrifice": "Dimanche"},
    "1221": {"nom": "Solomana (Manssa Souleymane)", "sexe": "Femelle", "nature": "Bénéfique/Fermeture", "arbres": ["Zamba", "Sira (Baobab)", "Mandé sounsoun", "Sounsoun"], "plantes_sacrees": "Mandé sounsoun, Sounsoun", "psaume": "Psaume 142", "verset": "Isaïe 22:22", "sceau": "7e Pentacle de Saturne", "jour_sacrifice": "Samedi"},
    "2112": {"nom": "Badra (Badra Aliou / Conjunctio)", "sexe": "Femelle", "nature": "Difficulté/Union", "arbres": ["Triki", "Gouélé"], "plantes_sacrees": "Guélé", "psaume": "Psaume 133", "verset": "Ruth 1:16", "sceau": "4e Pentacle de Mercure", "jour_sacrifice": "Mercredi"},
    "2211": {"nom": "Nouhou (Nouhoum / Cauda Draconis)", "sexe": "Femelle", "nature": "Maléfique", "arbres": ["Koudjè", "Zèguènè", "Goundjè"], "plantes_sacrees": "Goundjè", "psaume": "Psaume 59", "verset": "Psaume 68:2", "sceau": "6e Pentacle de Saturne", "jour_sacrifice": "Dimanche"},
    "1112": {"nom": "Laoussana (Alhoussein / Lacina)", "sexe": "Femelle", "nature": "Difficulté/Plaisir", "arbres": ["Herbes des vieux puits", "Les ravins"], "plantes_sacrees": "Djoulasonkalani", "psaume": "Psaume 119 (Aleph)", "verset": "Cantique 4:7", "sceau": "2e Pentacle de Vénus", "jour_sacrifice": "Samedi"},
    "1211": {"nom": "Ousmane (Mory Zoumana / Acquisitio)", "sexe": "Mâle", "nature": "Bénéfique/Réalisation", "arbres": ["Troubala", "Dougalen"], "plantes_sacrees": "N'doubalé, Frogofraga", "psaume": "Psaume 23", "verset": "Psaume 23:1", "sceau": "3e Pentacle de Jupiter", "jour_sacrifice": "Jeudi"},
    "2121": {"nom": "Younouss (Tontigui / Puella)", "sexe": "Femelle", "nature": "Difficulté/Richesse", "arbres": ["Fogofogo", "N'tomotigui"], "plantes_sacrees": "N'tomotigui, Zondjè", "psaume": "Psaume 112", "verset": "Deutéronome 28:12", "sceau": "6e Pentacle de Jupiter", "jour_sacrifice": "Vendredi"},
    "2222": {"nom": "Moussa (Djama / Populus)", "sexe": "Femelle", "nature": "Bénéfique/Réalisation", "arbres": ["Tomy", "Sounzoufing"], "plantes_sacrees": "N'tomi, N'galama", "psaume": "Psaume 47", "verset": "Genèse 22:17", "sceau": "1er Pentacle de la Lune", "jour_sacrifice": "Lundi"}
}

MAISONS_META = {
    1: {"nom": "M1 (Consultant)", "temps": "Présent"}, 2: {"nom": "M2 (Gains)", "temps": "Présent"},
    3: {"nom": "M3 (Entourage)", "temps": "Passé"}, 4: {"nom": "M4 (Foyer)", "temps": "Présent"},
    5: {"nom": "M5 (Enfants)", "temps": "Présent"}, 6: {"nom": "M6 (Maladie)", "temps": "Passé"},
    7: {"nom": "M7 (Conjoint)", "temps": "Présent"}, 8: {"nom": "M8 (Mort)", "temps": "Présent"},
    9: {"nom": "M9 (Voyages)", "temps": "Passé"}, 10: {"nom": "M10 (Carrière)", "temps": "Présent"},
    11: {"nom": "M11 (Appuis)", "temps": "Présent"}, 12: {"nom": "M12 (Épreuves)", "temps": "Passé"},
    13: {"nom": "M13 (Témoin Droit)", "temps": "Présent"}, 14: {"nom": "M14 (Témoin Gauche)", "temps": "Futur"},
    15: {"nom": "M15 (Le Juge)", "temps": "Futur"}, 16: {"nom": "M16 (La Sentence)", "temps": "Futur"}
}

class EngineGeomancyPro:
    def __init__(self, m1, m2, m3, m4, question):
        # Sécurité cruciale : On force la conversion en chaîne de caractères texte nettoyée
        self.question = str(question)
        self.maisons = {
            1: str(m1).strip(),
            2: str(m2).strip(),
            3: str(m3).strip(),
            4: str(m4).strip()
        }
        self._engendrer_le_theme()
        self.passations = self._calculer_passations()

    def _addition_geomantique(self, code1, code2):
        nouveau_code = ""
        for i in range(4):
            l1 = int(code1[i])
            l2 = int(code2[i])
            nouveau_code += "2" if (l1 + l2) % 2 == 0 else "1"
        return nouveau_code

    def _engendrer_le_theme(self):
        # Vérification de sécurité pour empêcher le plantage d'index sur écran blanc
        for i in [1, 2, 3, 4]:
            if len(self.maisons[i]) != 4:
                raise ValueError(f"La maison M{i} doit contenir exactement 4 chiffres (Ex: 1121). Reçu: '{self.maisons[i]}'")

        # Calcul des Filles (M5 à M8)
        self.maisons[5] = self.maisons[1][0] + self.maisons[2][0] + self.maisons[3][0] + self.maisons[4][0]
        self.maisons[6] = self.maisons[1][1] + self.maisons[2][1] + self.maisons[3][1] + self.maisons[4][1]
        self.maisons[7] = self.maisons[1][2] + self.maisons[2][2] + self.maisons[3][2] + self.maisons[4][2]
        self.maisons[8] = self.maisons[1][3] + self.maisons[2][3] + self.maisons[3][3] + self.maisons[4][3]

        # Calcul des Neveux (M9 à M12)
        self.maisons[9]  = self._addition_geomantique(self.maisons[1], self.maisons[2])
        self.maisons[10] = self._addition_geomantique(self.maisons[3], self.maisons[4])
        self.maisons[11] = self._addition_geomantique(self.maisons[5], self.maisons[6])
        self.maisons[12] = self._addition_geomantique(self.maisons[7], self.maisons[8])

        # Témoins, Juge et Sentence
        self.maisons[13] = self._addition_geomantique(self.maisons[9], self.maisons[10])
        self.maisons[14] = self._addition_geomantique(self.maisons[11], self.maisons[12])
        self.maisons[15] = self._addition_geomantique(self.maisons[13], self.maisons[14])
        self.maisons[16] = self._addition_geomantique(self.maisons[15], self.maisons[1])

    def _calculer_passations(self):
        carte = {}
        for m, code in self.maisons.items():
            if code not in carte: carte[code] = []
            carte[code].append(m)
        return {c: m_l for c, m_l in carte.items() if len(m_l) > 1}

    def compiler_fiche_remede(self, index_maison):
        code_fig = self.maisons[index_maison]
        data = FIGURES_DB.get(code_fig, {"nom": "Inconnue", "arbres": [], "plantes_sacrees": "", "psaume": "Psaume 1", "verset": "", "sceau": "", "jour_sacrifice": "Lundi"})
        
        num_psaume = "".join([c for c in data["psaume"] if c.isdigit()])
        num_psaume = int(num_psaume) if num_psaume else 1
        cle = 7 if (num_psaume % 9) in [1, 4, 8] else (9 if (num_psaume % 9) in [3, 6, 0] else 3)
        valeur_cible = num_psaume + cle

        base = (valeur_cible - 12) // 3
        reste = (valeur_cible - 12) % 3
        c1, c2, c3, c4, c5, c6, c7, c8, c9 = [base + i for i in range(9)]
        if reste == 1: c7 += 1; c8 += 1; c9 += 1
        elif reste == 2: c4 += 1; c5 += 1; c6 += 1; c7 += 2; c8 += 2; c9 += 2

        carre_visuel = f"| {c4} | {c9} | {c2} | \\n | {c3} | {c5} | {c7} | \\n | {c8} | {c1} | {c6} |"
        return {"maison": MAISONS_META[index_maison]["nom"], "figure": data["nom"], "arbres": data["arbres"], "ordonnance": data["psaume"], "carre": carre_visuel}

    def generer_rapport(self):
        theme_complet = {f"M{m}": FIGURES_DB.get(code, {"nom": "Inconnue"})["nom"] for m, code in self.maisons.items()}
        return {
            "statut": "SUCCÈS",
            "question": self.question,
            "cartographie": theme_complet,
            "solutions": {"juge_m15": self.compiler_fiche_remede(15), "sentence_m16": self.compiler_fiche_remede(16)}
        }

# =====================================================================
# FONCTION DIRECTE D'INTERFAÇAGE (A APPELER PAR VOTRE APPLICATION)
# =====================================================================
def calculer_theme_geomantique(m1, m2, m3, m4, question):
    """
    Cette fonction encapsule tout. Si une erreur survient (Saisie vide, lettres...),
    elle renvoie un dictionnaire d'erreur au lieu de faire un écran blanc.
    """
    try:
        moteur = EngineGeomancyPro(m1, m2, m3, m4, question)
        return moteur.generer_rapport()
    except Exception as e:
        # Renvoie l'erreur proprement à l'écran plutôt que de faire crasher l'UI
        return {
            "statut": "ERREUR DE SAISIE",
            "message_erreur": str(e),
            "conseil": "Assurez-vous d'entrer 4 chiffres composés exclusivement de 1 et de 2 pour chaque Mère (Ex: 1121)."
        }
