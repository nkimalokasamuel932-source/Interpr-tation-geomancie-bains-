# -*- coding: utf-8 -*-
"""
SST - SYSTÈME INFORMATIQUE INTÉGRAL DE GÉOMANCIE TRADITIONNELLE (VERSION PRODUCTION)
Conforme à 100% au document de formation de Zoumana Koné-Somadjely.
"""

import json

# =====================================================================
# 1. BASE DE DONNÉES UNIFIÉE DES 16 FIGURES GÉOMANTIQUES
# Les codes binaires correspondent à la structure : Tête, Poitrine, Ventre, Pied
# (1 = Impair / Un point, 2 = Pair / Deux points)
# =====================================================================
FIGURES_DB = {
    "1121": {
        "nom": "Youssouf (Sedjou / Puer)", "sexe": "Mâle", "nature": "Variable/Difficulté",
        "arbres": ["Djala", "N'zèrènidjè", "Djatiguifaga", "Zaban", "Balanzan"], 
        "plantes_sacrees": "Zaban, Balanzan, Poudre de fusil",
        "psaume": "Psaume 35", "verset": "Exode 15:3", "sceau": "2e Pentacle de Mars", "jour_sacrifice": "Mardi"
    },
    "1222": {
        "nom": "Adama (Letitia / La joie)", "sexe": "Mâle", "nature": "Bénéfique/Joie",
        "arbres": ["Sana", "Gounan", "Frogofraga", "N'gouna", "Sérétoro"], 
        "plantes_sacrees": "Frogofraga, N'gouna, Sérétoro",
        "psaume": "Psaume 4", "verset": "Néhémie 8:10", "sceau": "2e Pentacle de Jupiter", "jour_sacrifice": "Jeudi"
    },
    "2111": {
        "nom": "Mahamadou / Malidjou (Caput Draconis)", "sexe": "Femelle", "nature": "Variable/Élévation",
        "arbres": ["Djoulassounkalani", "Sébé"], 
        "plantes_sacrees": "Arbres qui poussent sur colline ou toile, Djoun",
        "psaume": "Psaume 128", "verset": "Exode 20:12", "sceau": "1er Pentacle de la Terre", "jour_sacrifice": "Jeudi"
    },
    "2212": {
        "nom": "Idrissa (Albayaro / Idriss / Albus)", "sexe": "Mâle", "nature": "Bénéfique",
        "arbres": ["Dougalén", "N'gokou"], 
        "plantes_sacrees": "N'gokou, tous les arbres qui vivent sur les fleuves",
        "psaume": "Psaume 119 (Beth)", "verset": "Isaïe 1:18", "sceau": "2e Pentacle de Mercure", "jour_sacrifice": "Vendredi"
    },
    "1111": {
        "nom": "Ibrahima (Taliki / Bourama / Via)", "sexe": "Mâle", "nature": "Variable/Mouvement",
        "arbres": ["Tièkala", "Zongnè", "Zondjè"], 
        "plantes_sacrees": "Zondjè, arbres poussant au bord des sources d'eau",
        "psaume": "Psaume 120", "verset": "Psaume 121:8", "sceau": "5e Pentacle de la Lune", "jour_sacrifice": "Lundi"
    },
    "1212": {
        "nom": "Issa (Nabbi Issa / Enzan / Amissio)", "sexe": "Mâle", "nature": "Maléfique/Échec",
        "arbres": ["N'gagnaka", "Sourou N'tomo", "Niama", "Chi"], 
        "plantes_sacrees": "N'gagnaka, Niama, Chi",
        "psaume": "Psaume 102", "verset": "Joël 2:25", "sceau": "5e Pentacle de Vénus", "jour_sacrifice": "Mercredi"
    },
    "2122": {
        "nom": "Oumarou (Seyyidina Oumarou / Lomara / Rubeus)", "sexe": "Femelle", "nature": "Maléfique/Feu/Sang",
        "arbres": ["Gabablen", "Foronto", "Wo", "Djati tgui fa djiri"], 
        "plantes_sacrees": "Gaba blé, Djati tgui fa djiri",
        "psaume": "Psaume 29", "verset": "Cantique 8:6", "sceau": "4e Pentacle de Mars", "jour_sacrifice": "Mardi"
    },
    "2221": {
        "nom": "Ayouba (Nabbi Ayouba / Almangoussi / Tristitia)", "sexe": "Mâle", "nature": "Maléfique/Tristesse",
        "arbres": ["Koronifing", "Koto", "Ngokou"], 
        "plantes_sacrees": "Herbes qui poussent sur tombeau, Koroni fin",
        "psaume": "Psaume 40", "verset": "Isaïe 61:3", "sceau": "5e Pentacle de Saturne", "jour_sacrifice": "Samedi"
    },
    "1122": {
        "nom": "Allahou talla (Aboubakr Sidik / Fortuna Minor)", "sexe": "Mâle", "nature": "Bénéfique",
        "arbres": ["Alladjô", "Congo Sirani"], 
        "plantes_sacrees": "Aladjon, racines d'arbres coupant la route",
        "psaume": "Psaume 121", "verset": "Psaume 46:2", "sceau": "4e Pentacle du Soleil", "jour_sacrifice": "Dimanche"
    },
    "1221": {
        "nom": "Solomana (Manssa Souleymane / Carcer)", "sexe": "Femelle", "nature": "Bénéfique/Fermeture",
        "arbres": ["Zamba", "Sira (Baobab)", "Mandé sounsoun", "Sounsoun"], 
        "plantes_sacrees": "Mandé sounsoun, Sounsoun",
        "psaume": "Psaume 142", "verset": "Isaïe 22:22", "sceau": "7e Pentacle de Saturne", "jour_sacrifice": "Samedi"
    },
    "2112": {
        "nom": "Badra (Badra Aliou / Conjunctio)", "sexe": "Femelle", "nature": "Difficulté/Union",
        "arbres": ["Triki", "Gouélé"], 
        "plantes_sacrees": "Guélé",
        "psaume": "Psaume 133", "verset": "Ruth 1:16", "sceau": "4e Pentacle de Mercure", "jour_sacrifice": "Mercredi"
    },
    "2211": {
        "nom": "Nouhou (Nouhoum / Cauda Draconis)", "sexe": "Femelle", "nature": "Maléfique",
        "arbres": ["Koudjè", "Zèguènè", "Goundjè"], 
        "plantes_sacrees": "Goundjè",
        "psaume": "Psaume 59", "verset": "Psaume 68:2", "sceau": "6e Pentacle de Saturne", "jour_sacrifice": "Dimanche"
    },
    "1112": {
        "nom": "Laoussana (Alhoussein / Lacina / Puella)", "sexe": "Femelle", "nature": "Difficulté/Plaisir",
        "arbres": ["Herbes des vieux puits", "Les ravins", "Rigoles", "Plantes gluantes"], 
        "plantes_sacrees": "Djoulasonkalani",
        "psaume": "Psaume 119 (Aleph)", "verset": "Cantique 4:7", "sceau": "2e Pentacle de Vénus", "jour_sacrifice": "Samedi"
    },
    "1211": {
        "nom": "Ousmane (Mory Zoumana / Acquisitio)", "sexe": "Mâle", "nature": "Bénéfique/Réalisation",
        "arbres": ["Troubala", "Dougalen", "Chou Toro", "N'doubalé", "Frogofraga"], 
        "plantes_sacrees": "N'doubalé, Frogofraga",
        "psaume": "Psaume 23", "verset": "Psaume 23:1", "sceau": "3e Pentacle de Jupiter", "jour_sacrifice": "Jeudi"
    },
    "2121": {
        "nom": "Younouss (Tontigui / Puella)", "sexe": "Femelle", "nature": "Difficulté/Richesse",
        "arbres": ["Fogofogo", "N'tomotigui", "Zondjè"], 
        "plantes_sacrees": "N'tomotigui, Zondjè",
        "psaume": "Psaume 112", "verset": "Deutéronome 28:12", "sceau": "6e Pentacle de Jupiter", "jour_sacrifice": "Vendredi"
    },
    "2222": {
        "nom": "Moussa (Djama / Populus)", "sexe": "Femelle", "nature": "Bénéfique/Réalisation",
        "arbres": ["Tomy", "Sounzoufing", "N'tomi", "N'galama"], 
        "plantes_sacrees": "N'tomi, N'galama",
        "psaume": "Psaume 47", "verset": "Genèse 22:17", "sceau": "1er Pentacle de la Lune", "jour_sacrifice": "Lundi"
    }
}

# Significations temporelles et sémantiques des maisons
MAISONS_META = {
    1: {"nom": "M1 (Consultant / Tête)", "temps": "Présent"},
    2: {"nom": "M2 (Gains / Argent)", "temps": "Présent"},
    3: {"nom": "M3 (Entourage / Déplacements)", "temps": "Passé"},
    4: {"nom": "M4 (Foyer / Patrimoine / Fin)", "temps": "Présent"},
    5: {"nom": "M5 (Enfants / Amours / Nouvelles)", "temps": "Présent"},
    6: {"nom": "M6 (Maladie / Obstacles)", "temps": "Passé"},
    7: {"nom": "M7 (Conjoint / Mariage / Adversaire)", "temps": "Présent"},
    8: {"nom": "M8 (Mort / Transformations / Pertes)", "temps": "Présent"},
    9: {"nom": "M9 (Voyages / Spiritualité)", "temps": "Passé"},
    10: {"nom": "M10 (Carrière / Profession / Pouvoir)", "temps": "Présent"},
    11: {"nom": "M11 (Appuis / Amis / Espoirs)", "temps": "Présent"},
    12: {"nom": "M12 (Épreuves / Ennemis / Prison)", "temps": "Passé"},
    13: {"nom": "M13 (Témoin Droit / Chambre)", "temps": "Présent"},
    14: {"nom": "M14 (Témoin Gauche / Ressources)", "temps": "Futur"},
    15: {"nom": "M15 (Le Juge final)", "temps": "Futur"},
    16: {"nom": "M16 (La Sentence / Clé ultime)", "temps": "Futur"}
}


# =====================================================================
# 2. MOTEUR DE CALCUL INFORMATIQUE ET D'ANALYSE (SÉCURISÉ)
# =====================================================================
class EngineGeomancyPro:
    def __init__(self, m1, m2, m3, m4, question):
        """
        Initialisation et sécurisation stricte des entrées utilisateur.
        Convertit automatiquement en chaînes textuelles pour éviter les crashs.
        """
        self.question = str(question).strip()
        
        # Nettoyage et conversion forcée en chaînes de caractères
        self.maisons = {
            1: str(m1).strip(),
            2: str(m2).strip(),
            3: str(m3).strip(),
            4: str(m4).strip()
        }
        
        # Exécution de la chaîne mathématique
        self._engendrer_le_theme()
        self.passations = self._calculer_passations()

    def _addition_geomantique(self, code1, code2):
        """Additionne deux codes binaires géomantiques selon la parité."""
        nouveau_code = ""
        for i in range(4):
            l1 = int(code1[i])
            l2 = int(code2[i])
            # Règle : Somme paire = 2 (deux points), Somme impaire = 1 (un point)
            nouveau_code += "2" if (l1 + l2) % 2 == 0 else "1"
        return nouveau_code

    def _engendrer_le_theme(self):
        """Calcule automatiquement les maisons 5 à 16 à partir des 4 mères saisies."""
        # Sécurité anti-écran blanc : Vérification de la longueur des mères
        for i in [1, 2, 3, 4]:
            if len(self.maisons[i]) != 4:
                raise ValueError(f"La maison M{i} fournie n'est pas valide. Elle doit contenir exactement 4 chiffres (Ex: 1121).")

        # 1. Génération des Filles (M5 à M8) par transposition
        self.maisons[5] = self.maisons[1][0] + self.maisons[2][0] + self.maisons[3][0] + self.maisons[4][0] # Têtes
        self.maisons[6] = self.maisons[1][1] + self.maisons[2][1] + self.maisons[3][1] + self.maisons[4][1] # Poitrines
        self.maisons[7] = self.maisons[1][2] + self.maisons[2][2] + self.maisons[3][2] + self.maisons[4][2] # Ventres
        self.maisons[8] = self.maisons[1][3] + self.maisons[2][3] + self.maisons[3][3] + self.maisons[4][3] # Pieds

        # 2. Génération des Neveux (M9 à M12) par copulation
        self.maisons[9]  = self._addition_geomantique(self.maisons[1], self.maisons[2]) # M1 + M2
        self.maisons[10] = self._addition_geomantique(self.maisons[3], self.maisons[4]) # M3 + M4
        self.maisons[11] = self._addition_geomantique(self.maisons[5], self.maisons[6]) # M5 + M6
        self.maisons[12] = self._addition_geomantique(self.maisons[7], self.maisons[8]) # M7 + M8

        # 3. Génération des Témoins (M13 et M14)
        self.maisons[13] = self._addition_geomantique(self.maisons[9], self.maisons[10]) # M9 + M10
        self.maisons[14] = self._addition_geomantique(self.maisons[11], self.maisons[12]) # M11 + M12

        # 4. Génération du Juge (M15) et de la Sentence (M16)
        self.maisons[15] = self._addition_geomantique(self.maisons[13], self.maisons[14]) # M13 + M14
        self.maisons[16] = self._addition_geomantique(self.maisons[15], self.maisons[1])  # M15 + M1

    def _calculer_passations(self):
        """Scanne tout le thème pour identifier et grouper les répétitions (passations) de figures."""
        carte_passations = {}
        for m, code in self.maisons.items():
            if code not in carte_passations:
                carte_passations[code] = []
            carte_passations[code].append(m)
        # On ne retourne que les figures qui apparaissent plus d'une fois
        return {code: m_list for code, m_list in carte_passations.items() if len(m_list) > 1}

    def verifier_veracite_theme(self):
        """Applique les interdits majeurs de répétition décrits dans le cours."""
        alertes = []
        for code, m_list in self.passations.items():
            fig_data = FIGURES_DB.get(code, {"nom": "Figure Inconnue"})
            fig_nom = fig_data["nom"]
            
            # Interdit sur la répétition abusive des figures de stabilité globale
            if ("Moussa" in fig_nom or "Ibrahima" in fig_nom) and len(m_list) >= 4:
                alertes.append(f"❌ LE THÈME MENT : Répétition excessive (>= 4 fois) de la figure {fig_nom}.")
            
            # Interdits de déplacements impossibles ou bloquants selon les maîtres
            if "Youssouf" in fig_nom and 1 in m_list and 7 in m_list:
                alertes.append("❌ THÈME COMPORTEMENTAL KHAFIR : Youssouf ne peut pas passer de M1 à M7.")
            if "Issa" in fig_nom and 1 in m_list and 6 in m_list:
                alertes.append("❌ THÈME COMPORTEMENTAL KHAFIR : Nabbi Issa ne peut pas passer de M1 à M6.")
                
        # Alerte critique sur la santé physique (Lomara en M12 et M8 simultanément)
        if self.maisons[12] == self.maisons[8] and "Oumarou" in FIGURES_DB.get(self.maisons[12], {}).get("nom", ""):
            alertes.append("🚨 ALERTE SANTÉ CRITIQUE : Lomara s'est déplacé en M12 et M8 (Danger de blessure à la tête).")
            
        return alertes

    def calculer_part_de_fortune(self):
        """Somme arithmétique des points des 4 mères originelles modulo 12."""
        total_points = 0
        for m in [1, 2, 3, 4]:
            for char in self.maisons[m]:
                total_points += int(char)
        reste = total_points % 12
        maison_cible = 12 if reste == 0 else reste
        fig_fortune = FIGURES_DB.get(self.maisons[maison_cible], {"nom": "Inconnue", "nature": "Neutre"})
        return {
            "total_points_calcules": total_points,
            "maison_de_chute": f"M{maison_cible}",
            "figure_occupante": fig_fortune["nom"],
            "conclusion": f"L'affaire se stabilise sous l'influence de nature {fig_fortune['nature']}."
        }

    def evaluer_timing_sacrifices(self):
        """Détermine le timing d'exécution traditionnel des sacrifices d'après les maisons touchées."""
        conseils = []
        for code, m_list in self.passations.items():
            fig_data = FIGURES_DB.get(code, {"nom": "Inconnue", "jour_sacrifice": "Indéterminé"})
            temps_touches = [MAISONS_META[m]["temps"] for m in m_list]
            
            if "Présent" in temps_touches:
                conseils.append(f"⚡ [TIMING : IMMÉDIAT] Sacrifice pour {fig_data['nom']} requis aujourd'hui au présent. Jour de vibration : {fig_data['jour_sacrifice']}.")
            elif "Passé" in temps_touches and "Présent" not in temps_touches:
                conseils.append(f"👶 [TIMING : URGENCE] Énergie bloquée au passé pour {fig_data['nom']}. Offrir le sacrifice immédiatement à un enfant.")
        return conseils

    def analyser_dynamique_mariage(self):
        """Analyse l'axe de l'union ou des contrats (M1 et M7) d'après les règles de passations."""
        m1_code = self.maisons[1]
        m7_code = self.maisons[7]
        if m1_code == m7_code:
            return f"💍 UNION ACCORDÉE : Passation directe de M1 à M7 avec {FIGURES_DB.get(m1_code, {}).get('nom')}. Concordance parfaite."
        elif m1_code in self.passations and 7 in self.passations[m1_code]:
            return "⏳ RETARD MAJEUR : La passation indique que l'accord ou le mariage se fera, mais après de longs blocages."
        return "❌ BLOCAGE / AUCUN MOUVEMENT : Aucune passation ni lien direct détecté entre M1 et M7."

    def compiler_fiche_remede(self, index_maison):
        """Génère automatiquement la prescription théurgique et le carré magique 3x3 lié."""
        code_fig = self.maisons[index_maison]
        data = FIGURES_DB.get(code_fig, {
            "nom": "Inconnue", "arbres": [], "plantes_sacrees": "Aucune", 
            "psaume": "Psaume 1", "verset": "Aucun", "sceau": "Aucun", "jour_sacrifice": "Lundi"
        })

        # Extraction sécurisée du numéro de Psaume
        num_psaume = "".join([c for c in data["psaume"] if c.isdigit()])
        num_psaume = int(num_psaume) if num_psaume else 1
        
        # Règle de réduction théologique pour définir la clé mystique du carré
        cle_ecriture = 7 if (num_psaume % 9) in [1, 4, 8] else (9 if (num_psaume % 9) in [3, 6, 0] else 3)
        valeur_cible = num_psaume + cle_ecriture

        # Algorithme mathématique de construction de la matrice 3x3 de Ghazali
        base = (valeur_cible - 12) // 3
        reste = (valeur_cible - 12) % 3
        c1, c2, c3, c4, c5, c6, c7, c8, c9 = [base + i for i in range(9)]
        if reste == 1: c7 += 1; c8 += 1; c9 += 1
        elif reste == 2: c4 += 1; c5 += 1; c6 += 1; c7 += 2; c8 += 2; c9 += 2

        carre_visuel = f"| {c4} | {c9} | {c2} | \\n | {c3} | {c5} | {c7} | \\n | {c8} | {c1} | {c6} |"
        
        return {
            "maison_concernee": MAISONS_META[index_maison]["nom"],
            "figure_installee": data["nom"],
            "elements_naturels": {"arbres": data["arbres"], "feuilles_sacrees": data["plantes_sacrees"]},
            "theurgie": {"ecriture_sur_papier": data["psaume"], "verset_verrou": data["verset"], "sceau_salomon": data["sceau"], "jour_activation": data["jour_sacrifice"]},
            "carre_magique_activation": {"somme_mystique": valeur_cible, "matrice_3x3": carre_visuel}
        }

    def generer_rapport_complet(self):
        """Compile l'ensemble des modules d'analyse pour l'interface graphique."""
        alertes = self.verifier_veracite_theme()
        theme_nomme = {f"Maison {m} ({MAISONS_META[m]['nom']})": FIGURES_DB.get(code, {"nom": "Inconnue"})["nom"] for m, code in self.maisons.items()}

        return {
            "statut_du_theme": "VALIDE" if not alertes else "ALERTE / REJET",
            "question_du_demandeur": self.question,
            "securite_traditionnelle": alertes if alertes else ["Le thème respecte les règles de vérité du cours."],
            "cartographie_des_16_maisons": theme_nomme,
            "analyse_part_de_fortune": self.calculer_part_de_fortune(),
            "analyse_mariage_contrat": self.analyser_dynamique_mariage(),
            "timing_des_sacrifices": self.evaluer_timing_sacrifices(),
            "remedes_majeurs": {
                "le_juge_m15": self.compiler_fiche_remede(15),
                "la_sentence_m16": self.compiler_fiche_remede(16)
            }
        }


# =====================================================================
# 3. POINT D'ENTRÉE DU SYSTÈME (SÉCURISÉ CONTRE LES ÉCRANS BLANCS)
# =====================================================================
def executer_consultation_geomantique(mere1, mere2, mere3, mere4, question_texte):
    """
    Fonction maîtresse à appeler directement par l'application graphique.
    Si l'utilisateur fait une fausse manip, elle intercepte le problème
    et renvoie un texte explicite à l'écran au lieu de faire planter l'UI.
    """
    try:
        moteur = EngineGeomancyPro(mere1, mere2, mere3, mere4, question_texte)
        return moteur.generer_rapport_complet()
    except Exception as fatal_error:
        # Enveloppe de secours absolue : retourne un dictionnaire propre de diagnostic
        return {
            "statut_du_theme": "ERREUR CRITIQUE DE CONFIGURATION",
            "message_erreur": str(fatal_error),
            "conseil": "Vérifiez que vos 4 mères d'entrées (m1, m2, m3, m4) contiennent des chaînes de 4 caractères composées uniquement de 1 et de 2 (Exemple : '1121')."
        }
