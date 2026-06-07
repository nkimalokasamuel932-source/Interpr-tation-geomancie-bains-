# -*- coding: utf-8 -*-
"""
SST - SYSTÈME INFORMATIQUE INTÉGRAL DE GÉOMANCIE TRADITIONNELLE (PRODUCTION CODES CORRIGÉS)
Conforme à 100% au document de formation de Zoumana Koné-Somadjely.
"""

import json

# =====================================================================
# BASE DE DONNÉES SÉCURISÉE DES 16 FIGURES GÉOMANTIQUES
# Les clés binaires ont été vérifiées et recalibrées pour éviter les KeyError
# =====================================================================
FIGURES_DB = {
    "1121": {
        "nom": "Youssouf (Sedjou / Puer)", "sexe": "Mâle", "nature": "Variable/Difficulté", "qualite": "Difficulté",
        "arbres": ["Djala", "N'zèrènidjè", "Djatiguifaga", "Zaban", "Balanzan"], "plantes_sacrees": "Zaban, Balanzan, Poudre de fusil",
        "psaume": "Psaume 35", "verset": "Exode 15:3", "sceau": "2e Pentacle de Mars", "jour_sacrifice": "Mardi"
    },
    "1222": {
        "nom": "Adama (Letitia / La joie)", "sexe": "Mâle", "nature": "Bénéfique/Joie", "qualite": "Chose probable",
        "arbres": ["Sana", "Gounan", "Frogofraga", "N'gouna", "Sérétoro"], "plantes_sacrees": "Frogofraga, N'gouna, Sérétoro",
        "psaume": "Psaume 4", "verset": "Néhémie 8:10", "sceau": "2e Pentacle de Jupiter", "jour_sacrifice": "Jeudi"
    },
    "2111": {
        "nom": "Mahamadou / Malidjou (Caput Draconis)", "sexe": "Femelle", "nature": "Variable/Élévation", "qualite": "Fixe et d'accroissement",
        "arbres": ["Djoulassounkalani", "Sébé"], "plantes_sacrees": "Arbres qui poussent sur colline ou toile, Djoun",
        "psaume": "Psaume 128", "verset": "Exode 20:12", "sceau": "1er Pentacle de la Terre", "jour_sacrifice": "Jeudi"
    },
    "2212": {
        "nom": "Idrissa (Albayaro / Idriss / Albus)", "sexe": "Mâle", "nature": "Bénéfique", "qualite": "Fixe et bonne",
        "arbres": ["Dougalén", "N'gokou"], "plantes_sacrees": "N'gokou, tous les arbres qui vivent sur les fleuves",
        "psaume": "Psaume 119 (Beth)", "verset": "Isaïe 1:18", "sceau": "2e Pentacle de Mercure", "jour_sacrifice": "Vendredi"
    },
    "1111": {
        "nom": "Ibrahima (Taliki / Bourama / Via)", "sexe": "Mâle", "nature": "Variable/Mouvement", "qualite": "Difficulté",
        "arbres": ["Tièkala", "Zongnè", "Zondjè"], "plantes_sacrees": "Zondjè, arbres poussant au bord des sources d'eau",
        "psaume": "Psaume 120", "verset": "Psaume 121:8", "sceau": "5e Pentacle de la Lune", "jour_sacrifice": "Lundi"
    },
    "1212": {
        "nom": "Issa (Nabbi Issa / Enzan / Amissio)", "sexe": "Mâle", "nature": "Maléfique/Échec", "qualite": "Chose probable",
        "arbres": ["N'gagnaka", "Sourou N'tomo", "Niama", "Chi"], "plantes_sacrees": "N'gagnaka, Niama, Chi",
        "psaume": "Psaume 102", "verset": "Joël 2:25", "sceau": "5e Pentacle de Vénus", "jour_sacrifice": "Mercredi"
    },
    "2122": {
        "nom": "Oumarou (Seyyidina Oumarou / Lomara / Rubeus)", "sexe": "Femelle", "nature": "Maléfique/Feu/Sang", "qualite": "Chaude",
        "arbres": ["Gabablen", "Foronto", "Wo", "Djati tgui fa djiri"], "plantes_sacrees": "Gaba blé, Djati tgui fa djiri",
        "psaume": "Psaume 29", "verset": "Cantique 8:6", "sceau": "4e Pentacle de Mars", "jour_sacrifice": "Mardi"
    },
    "2221": {
        "nom": "Ayouba (Nabbi Ayouba / Almangoussi / Tristitia)", "sexe": "Mâle", "nature": "Maléfique/Tristesse", "qualite": "Mauvaise / Fixe",
        "arbres": ["Koronifing", "Koto", "Ngokou"], "plantes_sacrees": "Herbes qui poussent sur tombeau, Koroni fin",
        "psaume": "Psaume 40", "verset": "Isaïe 61:3", "sceau": "5e Pentacle de Saturne", "jour_sacrifice": "Samedi"
    },
    "1122": {
        "nom": "Allahou talla (Aboubakr Sidik / Fortuna Minor)", "sexe": "Mâle", "nature": "Bénéfique", "qualite": "Bénéfique / Rapide",
        "arbres": ["Alladjô", "Congo Sirani"], "plantes_sacrees": "Aladjon, racines d'arbres coupant la route",
        "psaume": "Psaume 121", "verset": "Psaume 46:2", "sceau": "4e Pentacle du Soleil", "jour_sacrifice": "Dimanche"
    },
    "1221": {
        "nom": "Solomana (Manssa Souleymane / Carcer)", "sexe": "Femelle", "nature": "Bénéfique/Fermeture", "qualite": "Fixe et d'arrêt",
        "arbres": ["Zamba", "Sira (Baobab)", "Mandé sounsoun", "Sounsoun"], "plantes_sacrees": "Mandé sounsoun, Sounsoun",
        "psaume": "Psaume 142", "verset": "Isaïe 22:22", "sceau": "7e Pentacle de Saturne", "jour_sacrifice": "Samedi"
    },
    "2112": {
        "nom": "Badra (Badra Aliou / Conjunctio)", "sexe": "Femelle", "nature": "Difficulté/Union", "qualite": "Difficulté",
        "arbres": ["Triki", "Gouélé"], "plantes_sacrees": "Guélé",
        "psaume": "Psaume 133", "verset": "Ruth 1:16", "sceau": "4e Pentacle de Mercure", "jour_sacrifice": "Mercredi"
    },
    "2211": {
        "nom": "Nouhou (Nouhoum / Cauda Draconis)", "sexe": "Femelle", "nature": "Maléfique", "qualite": "Fixe et mauvaise",
        "arbres": ["Koudjè", "Zèguènè", "Goundjè"], "plantes_sacrees": "Goundjè",
        "psaume": "Psaume 59", "verset": "Psaume 68:2", "sceau": "6e Pentacle de Saturne", "jour_sacrifice": "Dimanche"
    },
    "1112": {
        "nom": "Laoussana (Alhoussein / Lacina / Puella)", "sexe": "Femelle", "nature": "Difficulté/Plaisir", "qualite": "Difficulté / Instable",
        "arbres": ["Herbes des vieux puits", "Les ravins", "Rigoles", "Plantes gluantes"], "plantes_sacrees": "Djoulasonkalani",
        "psaume": "Psaume 119 (Aleph)", "verset": "Cantique 4:7", "sceau": "2e Pentacle de Vénus", "jour_sacrifice": "Samedi"
    },
    "1211": {
        "nom": "Ousmane (Mory Zoumana / Acquisitio)", "sexe": "Mâle", "nature": "Bénéfique/Réalisation", "qualite": "La réalisation d'une chose / Fixe",
        "arbres": ["Troubala", "Dougalen", "Chou Toro", "N'doubalé", "Frogofraga"], "plantes_sacrees": "N'doubalé, Frogofraga",
        "psaume": "Psaume 23", "verset": "Psaume 23:1", "sceau": "3e Pentacle de Jupiter", "jour_sacrifice": "Jeudi"
    },
    "2121": {
        "nom": "Younouss (Tontigui / Puella)", "sexe": "Femelle", "nature": "Difficulté/Richesse", "qualite": "Chose probable / Difficulté",
        "arbres": ["Fogofogo", "N'tomotigui", "Zondjè"], "plantes_sacrees": "N'tomotigui, Zondjè",
        "psaume": "Psaume 112", "verset": "Deutéronome 28:12", "sceau": "6e Pentacle de Jupiter", "jour_sacrifice": "Vendredi"
    },
    "2222": {
        "nom": "Moussa (Djama / Populus)", "sexe": "Femelle", "nature": "Bénéfique/Réalisation", "qualite": "La réalisation d'une chose / Groupe",
        "arbres": ["Tomy", "Sounzoufing", "N'tomi", "N'galama"], "plantes_sacrees": "N'tomi, N'galama",
        "psaume": "Psaume 47", "verset": "Genèse 22:17", "sceau": "1er Pentacle de la Lune", "jour_sacrifice": "Lundi"
    }
}

MAISONS_META = {
    1: {"nom": "M1 (Consultant / Tête du thème)", "temps": "Présent"},
    2: {"nom": "M2 (Gains / Chance financière / Argent)", "temps": "Présent"},
    3: {"nom": "M3 (Entourage / Frères et Sœurs / Petits déplacements)", "temps": "Passé"},
    4: {"nom": "M4 (Foyer / Patrimoine / Famille paternelle / Fin des choses)", "temps": "Présent"},
    5: {"nom": "M5 (Enfants / Amours / Nouvelles / Accouchement)", "temps": "Présent"},
    6: {"nom": "M6 (Maladie / Obstacles / Serviteurs / Employés)", "temps": "Passé"},
    7: {"nom": "M7 (Conjoint / Mariage / Associé / Adversaire)", "temps": "Présent"},
    8: {"nom": "M8 (Mort / Transformations / Pertes / Craintes)", "temps": "Présent"},
    9: {"nom": "M9 (Voyages lointains / Spiritualité / Étranger)", "temps": "Passé"},
    10: {"nom": "M10 (Carrière / Profession / Pouvoir / Activité)", "temps": "Présent"},
    11: {"nom": "M11 (Appuis / Amis / Espoirs / Satisfaction)", "temps": "Présent"},
    12: {"nom": "M12 (Épreuves / Ennemis cachés / Prison / Calamités)", "temps": "Passé"},
    13: {"nom": "M13 (Témoin Droit / Chambre du consultant / Présent)", "temps": "Présent"},
    14: {"nom": "M14 (Témoin Gauche / Ressources / Futur proche)", "temps": "Futur"},
    15: {"nom": "M15 (Le Juge final du thème)", "temps": "Futur"},
    16: {"nom": "M16 (La Sentence / Clé de l'issue ultime)", "temps": "Futur"}
}


class EngineGeomancyPro:
    def __init__(self, m1, m2, m3, m4, question):
        """Initialisation automatique sécurisée."""
        self.question = question
        self.maisons = {1: str(m1), 2: str(m2), 3: str(m3), 4: str(m4)}
        
        # Déclenchement de l'arbre mathématique
        self._engendrer_le_theme()
        self.passations = self._calculer_passations()

    def _addition_geomantique(self, code1, code2):
        """Addition binaire sécurisée."""
        nouveau_code = ""
        for i in range(4):
            l1 = int(code1[i])
            l2 = int(code2[i])
            nouveau_code += "2" if (l1 + l2) % 2 == 0 else "1"
        return nouveau_code

    def _engendrer_le_theme(self):
        """Calcul strict des 16 maisons sans aucune faille de débordement."""
        # Génération des Filles (M5 à M8)
        self.maisons[5] = self.maisons[1][0] + self.maisons[2][0] + self.maisons[3][0] + self.maisons[4][0]
        self.maisons[6] = self.maisons[1][1] + self.maisons[2][1] + self.maisons[3][1] + self.maisons[4][1]
        self.maisons[7] = self.maisons[1][2] + self.maisons[2][2] + self.maisons[3][2] + self.maisons[4][2]
        self.maisons[8] = self.maisons[1][3] + self.maisons[2][3] + self.maisons[3][3] + self.maisons[4][3]

        # Génération des Neveux (M9 à M12)
        self.maisons[9]  = self._addition_geomantique(self.maisons[1], self.maisons[2])
        self.maisons[10] = self._addition_geomantique(self.maisons[3], self.maisons[4])
        self.maisons[11] = self._addition_geomantique(self.maisons[5], self.maisons[6])
        self.maisons[12] = self._addition_geomantique(self.maisons[7], self.maisons[8])

        # Témoins (M13 et M14)
        self.maisons[13] = self._addition_geomantique(self.maisons[9], self.maisons[10])
        self.maisons[14] = self._addition_geomantique(self.maisons[11], self.maisons[12])

        # Juge (M15) et Sentence (M16)
        self.maisons[15] = self._addition_geomantique(self.maisons[13], self.maisons[14])
        self.maisons[16] = self._addition_geomantique(self.maisons[15], self.maisons[1])

    def _calculer_passations(self):
        carte_passations = {}
        for m, code in self.maisons.items():
            if code not in carte_passations:
                carte_passations[code] = []
            carte_passations[code].append(m)
        return {code: m_list for code, m_list in carte_passations.items() if len(m_list) > 1}

    def verifier_veracite_theme(self):
        alertes = []
        for code, m_list in self.passations.items():
            # Utilisation systématique de .get pour empêcher l'écran blanc
            fig_data = FIGURES_DB.get(code, {"nom": "Inconnue"})
            fig_nom = fig_data["nom"]
            if ("Moussa" in fig_nom or "Ibrahima" in fig_nom) and len(m_list) >= 4:
                alertes.append(f"❌ THÈME REJETÉ : Répétition constante et excessive de la figure {fig_nom}.")
            if "Youssouf" in fig_nom and 1 in m_list and 7 in m_list:
                alertes.append("❌ ERREUR COMPORTEMENTALE INTERDITE : Youssouf ne passera jamais de M1 à M7.")
            if "Issa" in fig_nom and 1 in m_list and 6 in m_list:
                alertes.append("❌ ERREUR COMPORTEMENTALE INTERDITE : Nabbi Issa ne passera jamais de M1 à M6.")
                
        if self.maisons[12] == self.maisons[8] and "Oumarou" in FIGURES_DB.get(self.maisons[12], {}).get("nom", ""):
            alertes.append("🚨 ALERTE DANGER CRITIQUE (Santé) : Lomara présent simultanément en M12 et M8.")
        return alertes

    def calculer_part_de_fortune(self):
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
            "impact_final": f"L'affaire se conclut sur une influence de nature {fig_fortune['nature']}."
        }

    def evaluer_timing_sacrifices(self):
        conseils = []
        for code, m_list in self.passations.items():
            fig_data = FIGURES_DB.get(code, {"nom": "Inconnue", "jour_sacrifice": "Indéterminé"})
            temps_touches = [MAISONS_META[m]["temps"] for m in m_list]
            if "Présent" in temps_touches:
                conseils.append(f"⚡ [TIMING : AUJOURD'HUI] Sacrifice pour {fig_data['nom']} à faire de suite. Jour idéal : {fig_data['jour_sacrifice']}.")
            elif "Passé" in temps_touches and "Présent" not in temps_touches:
                conseils.append(f"👶 [TIMING : URGENCE ENFANT] Énergie bloquée au Passé pour {fig_data['nom']}. Donner à un enfant.")
        return conseils

    def analyser_dynamique_mariage(self):
        m1_code = self.maisons[1]
        m7_code = self.maisons[7]
        if m1_code == m7_code:
            return f"💍 ÉNÉRGIE D'UNION EXCELLENTE : Passation directe de M1 à M7 avec {FIGURES_DB.get(m1_code, {}).get('nom')}."
        elif m1_code in self.passations and 7 in self.passations[m1_code]:
            return "⏳ UNION RETARDÉE : Le mariage se fera mais connaîtra des délais ou blocages administratifs."
        return "❌ AUCUN MOUVEMENT DIRECT : Pas de lien immédiat détecté entre M1 et M7."

    def compiler_fiche_remede(self, index_maison):
        code_fig = self.maisons[index_maison]
        # Valeurs de secours si .get() pour parer à toute panne d'affichage
        data = FIGURES_DB.get(code_fig, {
            "nom": "Inconnue", "arbres": [], "plantes_sacrees": "Aucune", 
            "psaume": "Psaume 1", "verset": "Aucun", "sceau": "Aucun", "jour_sacrifice": "Lundi"
        })

        try:
            num_psaume = int("".join([c for c in data["psaume"] if c.isdigit()]))
        except ValueError:
            num_psaume = 11

        cle_ecriture = 7 if (num_psaume % 9) in [1, 4, 8] else (9 if (num_psaume % 9) in [3, 6, 0] else 3)
        valeur_cible = num_psaume + cle_ecriture

        base = (valeur_cible - 12) // 3
        reste = (valeur_cible - 12) % 3
        c1, c2, c3, c4, c5, c6, c7, c8, c9 = [base + i for i in range(9)]
        if reste == 1: c7 += 1; c8 += 1; c9 += 1
        elif reste == 2: c4 += 1; c5 += 1; c6 += 1; c7 += 2; c8 += 2; c9 += 2

        carre_visuel = (
            f"|  {c4:<3} |  {c9:<3} |  {c2:<3} |\n"
            f"|  {c3:<3} |  {c5:<3} |  {c7:<3} |\n"
            f"|  {c8:<3} |  {c1:<3} |  {c6:<3} |"
        )

        return {
            "maison_concernee": MAISONS_META[index_maison]["nom"],
            "figure_installee": data["nom"],
            "elements_naturels": {"arbres_associes": data["arbres"], "elements_sacres": data["plantes_sacrees"]},
            "ordonnance_theurgique": {"psaume_a_tracer": data["psaume"], "verset_ancrage": data["verset"], "sceau_salomonique": data["sceau"], "jour_de_vibration": data["jour_sacrifice"]},
            "carre_magique_activation": {"somme_mystique_cible": valeur_cible, "grille_3x3": carre_visuel}
        }

    def generer_rapport_systeme(self):
        alertes = self.verifier_veracite_theme()
        theme_complet = {f"Maison {m} - {MAISONS_META[m]['nom']}": FIGURES_DB.get(code, {"nom": "Inconnue"})["nom"] for m, code in self.maisons.items()}

        return {
            "statut_de_la_consultation": "VALIDE" if not alertes else "REJET / ALERTE CRITIQUE",
            "question_posee": self.question,
            "messages_de_securite": alertes if alertes else ["Aucune violation détectée."],
            "cartographie_des_16_maisons": theme_complet,
            "analyse_part_de_fortune": self.calculer_part_de_fortune(),
            "reponse_dynamique_mariage": self.analyser_dynamique_mariage(),
            "timing_et_jours_des_sacrifices": self.evaluer_timing_sacrifices(),
            "solutions_mystiques_majeures": {
                "fiche_du_juge_final_m15": self.compiler_fiche_remede(15),
                "fiche_de_la_sentence_m16": self.compiler_fiche_remede(16)
            }
        }


# =====================================================================
# BLOC DE SÉCURITÉ RUNTIME (Empêche l'écran blanc global)
# =====================================================================
if __name__ == "__main__":
    try:
        ma_question_application = "Vais-je réussir mon projet et me marier cette année ?"
        
        # Tirage d'exemple sans erreur
        mere1_saisie = "1121"  
        mere2_saisie = "1222"  
        mere3_saisie = "2112"  
        mere4_saisie = "1221"  

        moteur_systeme = EngineGeomancyPro(
            m1=mere1_saisie, 
            m2=mere2_saisie, 
            m3=mere3_saisie, 
            m4=mere4_saisie, 
            question=ma_question_application
        )
        
        rapport_final = moteur_systeme.generer_rapport_systeme()
        print(json.dumps(rapport_final, indent=4, ensure_ascii=False))

    except Exception as error_fatal:
        # En cas de problème au lieu du blanc, affiche l'emplacement exact du bug
        print(json.dumps({
            "statut_de_la_consultation": "ERREUR SYSTÈME CRITIQUE",
            "cause_du_plantage": str(error_fatal),
            "conseil": "Vérifiez que les valeurs d'entrées m1, m2, m3, m4 contiennent uniquement des suites de 4 chiffres composés de 1 et de 2."
        }, indent=4, ensure_ascii=False))
