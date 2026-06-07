# -*- coding: utf-8 -*-
"""
SST - SYSTÈME INFORMATIQUE INTÉGRAL DE GÉOMANCIE TRADITIONNELLE (PRODUCTION)
Conforme à 100% au document de formation de Zoumana Koné-Somadjely.
"""

import json

# =====================================================================
# DATA BASE UNIFIÉE : LES 16 FIGURES GÉOMANTIQUES (Ordre du document)
# Code binaire lu de HAUT en BAS (Tête, Poitrine, Ventre, Pied)
# 1 = Point impair (Unique), 2 = Point pair (Double)
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
        "nom": "Idrissa (Albayaro / Idriss)", "sexe": "Mâle", "nature": "Bénéfique", "qualite": "Fixe et bonne",
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
        "nom": "Younouss (Tontigui / Puella)", "sexe": "Femelle", "nature": "Difficulté/Richesse", "qualite": "Chose probable / Difficulté",
        "arbres": ["Fogofogo", "N'tomotigui", "Zondjè"], "plantes_sacrees": "N'tomotigui, Zondjè",
        "psaume": "Psaume 112", "verset": "Deutéronome 28:12", "sceau": "6e Pentacle de Jupiter", "jour_sacrifice": "Vendredi"
    },
    "2121": {
        "nom": "Ousmane (Mory Zoumana / Acquisitio)", "sexe": "Mâle", "nature": "Bénéfique/Réalisation", "qualite": "La réalisation d'une chose / Fixe",
        "arbres": ["Troubala", "Dougalen", "Chou Toro", "N'doubalé", "Frogofraga"], "plantes_sacrees": "N'doubalé, Frogofraga",
        "psaume": "Psaume 23", "verset": "Psaume 23:1", "sceau": "3e Pentacle de Jupiter", "jour_sacrifice": "Jeudi"
    },
    "2222": {
        "nom": "Moussa (Djama / Populus)", "sexe": "Femelle", "nature": "Bénéfique/Réalisation", "qualite": "La réalisation d'une chose / Groupe",
        "arbres": ["Tomy", "Sounzoufing", "N'tomi", "N'galama"], "plantes_sacrees": "N'tomi, N'galama",
        "psaume": "Psaume 47", "verset": "Genèse 22:17", "sceau": "1er Pentacle de la Lune", "jour_sacrifice": "Lundi"
    }
}

# Métadonnées et correspondance temporelle des 16 Maisons Géomantiques
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
        """
        Initialisation automatique du thème.
        L'utilisateur transmet UNIQUEMENT les codes binaires des 4 Mères fondamentales (M1 à M4).
        """
        self.question = question
        self.maisons = {1: m1, 2: m2, 3: m3, 4: m4}
        
        # Algorithme d'engendrement automatique des 16 maisons par copulations
        self._engendrer_le_theme()
        
        # Identification des répétitions (Passations)
        self.passations = self._calculer_passations()

    def _addition_geomantique(self, code1, code2):
        """Additionne deux figures ligne par ligne : Impair+Impair=Pair, Impair+Pair=Impair (2=Pair, 1=Impair)"""
        nouveau_code = ""
        for i in range(4):
            l1 = int(code1[i])
            l2 = int(code2[i])
            nouveau_code += "2" if (l1 + l2) % 2 == 0 else "1"
        return nouveau_code

    def _engendrer_le_theme(self):
        """Calcule de façon autonome les maisons 5 à 16 à partir des 4 premières Mères (Algorithme strict)"""
        # 1. Extraction et génération des 4 Filles (M5 à M8) par transposition des lignes des Mères
        self.maisons[5] = self.maisons[1][0] + self.maisons[2][0] + self.maisons[3][0] + self.maisons[4][0] # Ligne 1 (Têtes)
        self.maisons[6] = self.maisons[1][1] + self.maisons[2][1] + self.maisons[3][1] + self.maisons[4][1] # Ligne 2 (Poitrines)
        self.maisons[7] = self.maisons[1][2] + self.maisons[2][2] + self.maisons[3][2] + self.maisons[4][2] # Ligne 3 (Ventres)
        self.maisons[8] = self.maisons[1][3] + self.maisons[2][3] + self.maisons[3][3] + self.maisons[4][3] # Ligne 4 (Pieds)

        # 2. Génération des 4 Nièces / Neveux (M9 à M12) par copulation binaire directe des parents
        self.maisons[9]  = self._addition_geomantique(self.maisons[1], self.maisons[2]) # M1 + M2
        self.maisons[10] = self._addition_geomantique(self.maisons[3], self.maisons[4]) # M3 + M4
        self.maisons[11] = self._addition_geomantique(self.maisons[5], self.maisons[6]) # M5 + M6
        self.maisons[12] = self._addition_geomantique(self.maisons[7], self.maisons[8]) # M7 + M8

        # 3. Génération des Témoins (M13 et M14)
        self.maisons[13] = self._addition_geomantique(self.maisons[9], self.maisons[10]) # M9 + M10 (Témoin Droit)
        self.maisons[14] = self._addition_geomantique(self.maisons[11], self.maisons[12]) # M11 + M12 (Témoin Gauche)

        # 4. Génération du Juge final (M15)
        self.maisons[15] = self._addition_geomantique(self.maisons[13], self.maisons[14]) # M13 + M14

        # 5. Génération de la Sentence / Juge auxiliaire (M16)
        self.maisons[16] = self._addition_geomantique(self.maisons[15], self.maisons[1])  # M15 + M1

    def _calculer_passations(self):
        """Scanne le thème complet pour regrouper les passations de figures"""
        carte_passations = {}
        for m, code in self.maisons.items():
            if code not in carte_passations:
                carte_passations[code] = []
            carte_passations[code].append(m)
        return {code: m_list for code, m_list in carte_passations.items() if len(m_list) > 1}

    # --- SÉCURITÉ CONFORME AUX INTERDITS DU COURS ---
    def verifier_veracite_theme(self):
        """Vérifie si le thème a dit la vérité ou s'il doit être purement rejeté"""
        alertes = []
        
        # Interdit 1 : Répétitions excessives ou bouclages (Moussa ou Ibrahima répétés en boucle)
        for code, m_list in self.passations.items():
            fig_nom = FIGURES_DB.get(code, {}).get("nom", "")
            if ("Moussa" in fig_nom or "Ibrahima" in fig_nom) and len(m_list) >= 4:
                alertes.append(f"❌ THÈME REJETÉ : Répétition constante et excessive de la figure {fig_nom}.")
        
        # Interdit 2 : Vérification par copulation test (M1+M7 et M4+M10)
        test_code1 = self._addition_geomantique(self.maisons[1], self.maisons[7])
        test_code2 = self._addition_geomantique(self.maisons[4], self.maisons[10])
        fig_verite = self._addition_geomantique(test_code1, test_code2)
        if fig_verite not in self.maisons.values():
            alertes.append("⚠️ ATTENTION : Le test de copulation de véracité n'apparaît pas dans le thème. Fiabilité basse.")
            
        # Interdit 3 : Incohérences majeures de passation interdites par les Maîtres
        for code, m_list in self.passations.items():
            fig_nom = FIGURES_DB.get(code, {}).get("nom", "")
            if "Youssouf" in fig_nom and 1 in m_list and 7 in m_list:
                alertes.append("❌ ERREUR COMPORTEMENTALE : Youssouf ne passera jamais de M1 à M7. Thème rejeté.")
            if "Issa" in fig_nom and 1 in m_list and 6 in m_list:
                alertes.append("❌ ERREUR COMPORTEMENTALE : Nabbi Issa ne passera jamais de M1 à M6. Thème rejeté.")
                
        # Interdit 4 : Sécurité critique de santé (Oumarou/Lamora en M12 et M8)
        if self.maisons[12] == self.maisons[8] and "Oumarou" in FIGURES_DB.get(self.maisons[12], {}).get("nom", ""):
            alertes.append("🚨 ALERTE DANGER CRITIQUE (Santé) : Lomara présent simultanément en M12 et M8 (Risque d'accident ou affection grave de la tête).")

        return alertes

    # --- CALCULS EXOTÉRIQUES : PART DE FORTUNE ---
    def calculer_part_de_fortune(self):
        """Calcule la totalité des points des 16 lignes originelles des 4 mères modulo 12"""
        total_points = 0
        for m in [1, 2, 3, 4]:
            for char in self.maisons[m]:
                total_points += int(char) # Ajoute 1 pour impair, 2 pour pair
        
        reste = total_points % 12
        maison_cible = 12 if reste == 0 else reste
        fig_fortune = FIGURES_DB.get(self.maisons[maison_cible], {})
        
        return {
            "total_points_calcules": total_points,
            "maison_de_chute": f"M{maison_cible}",
            "figure_occupante": fig_fortune.get("nom", "Inconnu"),
            "impact_final": f"L'affaire se conclut sur une influence de nature {fig_fortune.get('nature')}."
        }

    # --- TIMING ET DISTRIBUTION DES SACRIFICES ---
    def evaluer_timing_sacrifices(self):
        """Analyse la position des figures pour définir quand et à qui donner le sacrifice"""
        conseils = []
        for code, m_list in self.passations.items():
            fig_data = FIGURES_DB.get(code, {})
            fig_nom = fig_data.get("nom", "")
            temps_touches = [MAISONS_META[m]["temps"] for m in m_list]
            
            # Application de la règle du temps du cours
            if "Présent" in temps_touches:
                conseils.append(f"⚡ [TIMING : AUJOURD'HUI] Le sacrifice pour {fig_nom} doit être fait immédiatement (Énergie au Présent). Jour idéal : {fig_data.get('jour_sacrifice')}.")
            elif "Passé" in temps_touches and "Présent" not in temps_touches:
                conseils.append(f"👶 [TIMING : URGENCE ENFANT] Énergie bloquée au Passé pour {fig_nom}. Offrez rapidement le sacrifice à un jeune enfant.")
        return conseils

    # --- ANALYSE DE LA QUESTION (EXEMPLE : MARIAGE M1 & M7) ---
    def analyser_dynamique_mariage(self):
        """Vérifie l'accord d'union entre la Maison du consultant (M1) et du partenaire (M7)"""
        m1_code = self.maisons[1]
        m7_code = self.maisons[7]
        
        if m1_code == m7_code:
            fig_nom = FIGURES_DB.get(m1_code, {}).get("nom", "")
            return f"💍 ÉNÉRGIE D'UNION EXCELLENTE : Passation directe de la M1 à la M7 via {fig_nom}. Le mariage/l'accord est fortement favorisé."
        elif m1_code in self.passations and 7 in self.passations[m1_code]:
            return "⏳ UNION RETARDÉE : Le mariage ou l'accord se fera mais connaîtra des délais administratifs ou familiaux."
        else:
            return "❌ AUCUN MOUVEMENT DIRECT : Pas de lien immédiat de passation détecté entre M1 et M7 pour cette affaire."

    # --- COMPILATION DES FICHES DE REMÈDES (THÉURGIE ET CARRÉS MAGIQUES) ---
    def compiler_fiche_remede(self, index_maison):
        """Génère la fiche mystique complète : Plantes, Arbres, Psaume, Sceau et Carré Magique d'activation"""
        code_fig = self.maisons[index_maison]
        data = FIGURES_DB.get(code_fig)
        if not data: return None

        # Extraction de la valeur numérique du Psaume (ex: "Psaume 35" -> 35)
        try:
            num_psaume = int("".join([c for c in data["psaume"] if c.isdigit()]))
        except ValueError:
            num_psaume = 66 # Valeur de secours par défaut si aucun chiffre
            
        # Règle de réduction théologique pour la clé d'écriture du carré
        cle_ecriture = 7 if (num_psaume % 9) in [1, 4, 8] else (9 if (num_psaume % 9) in [3, 6, 0] else 3)
        valeur_cible = num_psaume + cle_ecriture

        # Calcul automatique de la matrice 3x3 de Ghazali
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
            "elements_naturels": {
                "arbres_associes": data["arbres"],
                "elements_sacres": data["plantes_sacrees"]
            },
            "ordonnance_theurgique": {
                "psaume_a_tracer": data["psaume"],
                "verset_ancrage": data["verset"],
                "sceau_salomonique": data["sceau"],
                "jour_de_vibration": data["jour_sacrifice"]
            },
            "carre_magique_activation": {
                "somme_mystique_cible": valeur_cible,
                "grille_3x3": carre_visuel
            }
        }

    # --- PIPELINE DE SORTIE DE L'API ---
    def generer_rapport_systeme(self):
        alertes = self.verifier_veracite_theme()
        
        theme_complet = {
            f"Maison {m} - {MAISONS_META[m]['nom']}": FIGURES_DB.get(code, {}).get("nom", "Inconnu")
            for m, code in self.maisons.items()
        }

        return {
            "statut_de_la_consultation": "VALIDE" if not alertes else "REJET / ALERTE CRITIQUE",
            "question_posee": self.question,
            "messages_de_securite": alertes if alertes else ["Aucune violation des règles secrètes détectée."],
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
# SIMULATION DE PRODUCTION ET DE SAISIE DE THÈME
# =====================================================================
if __name__ == "__main__":
    # 1. Définition de la question textuelle entrée par l'utilisateur
    ma_question_application = "Vais-je réussir à stabiliser mes finances et me marier cette année ?"

    # 2. Saisie des 4 Mères uniquement (Format : chaîne de 4 caractères contenant des 1 et des 2)
    # Exemple de tirage :
    mere1_saisie = "1121"  # Youssouf en M1
    mere2_saisie = "1222"  # Adama en M2
    mere3_saisie = "2112"  # Badra en M3
    mere4_saisie = "1221"  # Solomana en M4

    # 3. Initialisation du moteur applicatif
    moteur_systeme = EngineGeomancyPro(
        m1=mere1_saisie, 
        m2=mere2_saisie, 
        m3=mere3_saisie, 
        m4=mere4_saisie, 
        question=ma_question_application
    )
    
    # 4. Exécution de l'analyse et génération du JSON complet destiné à l'interface
    rapport_final = moteur_systeme.generer_rapport_systeme()

    # Affichage propre sous format JSON lisible
    print(json.dumps(rapport_final, indent=4, ensure_ascii=False))
