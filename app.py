# -*- coding: utf-8 -*-
"""
SST - SYSTÈME INFORMATIQUE DE GÉOMANCIE TRADITIONNELLE (VERSION FINALE SANS ERREUR)
Conforme à 100% au document de formation officiel de Zoumana Koné-Somadjely.
"""

# =====================================================================
# 1. BASE DE DONNÉES AVEC VERSETS BIBLIQUES STRUCTURÉS
# =====================================================================
FIGURES_DB = {
    "1121": {
        "nom": "Youssouf (Sedjou / Puer)", "sexe": "Mâle", "temps_naturel": "Passé",
        "arbres": ["Djala", "N'zèrènidjè", "Djatiguifaga", "Zaban", "Balanzan"],
        "plantes_sacrees": "Zaban, Balanzan, Poudre de fusil",
        "psaume": "Psaume 35", "verset": "Exode 15 v.3", "sceau": "2e Pentacle de Mars", 
        "jour_sacrifice": "Mardi", "destinataire_sac": "Handicapés ou personnes s'étant blessées",
        "elements_sac": "Cola rouge, bélier au cou rouge, maïs rouge"
    },
    "1222": {
        "nom": "Adama (Letitia / La joie)", "sexe": "Mâle", "temps_naturel": "Passé",
        "arbres": ["Sana", "Gounan", "Frogofraga", "N'gouna", "Sérétoro"],
        "plantes_sacrees": "Frogofraga, N'gouna, Sérétoro",
        "psaume": "Psaume 4", "verset": "Néhémie 8 v.10", "sceau": "2e Pentacle de Jupiter", 
        "jour_sacrifice": "Jeudi", "destinataire_sac": "Plusieurs personnes (Groupe)",
        "elements_sac": "Fruits secs, longs animaux"
    },
    "2111": {
        "nom": "Mahamadou / Malidjou (Caput Draconis)", "sexe": "Femelle", "temps_naturel": "Futur",
        "arbres": ["Djoulassounkalani", "Sébé", "Arbres sur colline", "Djoun"],
        "plantes_sacrees": "Arbres qui poussent sur colline ou toile, Djoun",
        "psaume": "Psaume 128", "verset": "Exode 20 v.12", "sceau": "1er Pentacle de la Terre", 
        "jour_sacrifice": "Jeudi", "destinataire_sac": "Plusieurs personnes (Groupe)",
        "elements_sac": "Fruits secs, longs animaux"
    },
    "2212": {
        "nom": "Idrissa (Albayaro / Albus)", "sexe": "Mâle", "temps_naturel": "Futur",
        "arbres": ["Dougalén", "N'gokou", "Arbres des fleuves"],
        "plantes_sacrees": "N'gokou, tous les arbres qui vivent sur les fleuves",
        "psaume": "Psaume 119 (Beth)", "verset": "Isaïe 1 v.18", "sceau": "2e Pentacle de Mercure", 
        "jour_sacrifice": "Vendredi", "destinataire_sac": "Enfants",
        "elements_sac": "Bijoux, objets précieux, offrandes libres"
    },
    "1111": {
        "nom": "Ibrahima (Taliki / Via)", "sexe": "Mâle", "temps_naturel": "Présent",
        "arbres": ["Tièkala", "Zongnè", "Zondjè", "Arbres des sources d'eau"],
        "plantes_sacrees": "Zondjè, arbres poussant au bord des sources d'eau",
        "psaume": "Psaume 120", "verset": "Psaume 121 v.8", "sceau": "5e Pentacle de la Lune", 
        "jour_sacrifice": "Lundi", "destinataire_sac": "Religieux ou personnes s'occupant de la religion",
        "elements_sac": "Fruits frais, graines de céréales, animaux féminins"
    },
    "1212": {
        "nom": "Issa (Nabbi Issa / Amissio)", "sexe": "Mâle", "temps_naturel": "Passé",
        "arbres": ["N'gagnaka", "Sourou N'tomo", "Niama", "Chi"],
        "plantes_sacrees": "N'gagnaka, Niama, Chi",
        "psaume": "Psaume 102", "verset": "Joël 2 v.25", "sceau": "5e Pentacle de Vénus", 
        "jour_sacrifice": "Mercredi", "destinataire_sac": "Chanteur, griot ou muezzin",
        "elements_sac": "Choses à plusieurs couleurs (pintade, fonio, poule tachetée)"
    },
    "2122": {
        "nom": "Oumarou (Lomara / Rubeus)", "sexe": "Femelle", "temps_naturel": "Passé",
        "arbres": ["Gabablen", "Foronto", "Wo", "Djati tgui fa djiri", "Gaba blé"],
        "plantes_sacrees": "Gaba blé, Djati tgui fa djiri",
        "psaume": "Psaume 29", "verset": "Cantique 8 v.6", "sceau": "4e Pentacle de Mars", 
        "jour_sacrifice": "Mardi", "destinataire_sac": "Handicapés ou personnes s'étant blessées",
        "elements_sac": "Cola rouge, bélier au cou rouge, maïs rouge"
    },
    "2221": {
        "nom": "Ayouba (Almangoussi / Tristitia)", "sexe": "Mâle", "temps_naturel": "Futur",
        "arbres": ["Koronifing", "Koto", "Ngokou", "Herbes de tombeau"],
        "plantes_sacrees": "Herbes qui poussent sur tombeau, Koroni fin",
        "psaume": "Psaume 40", "verset": "Isaïe 61 v.3", "sceau": "5e Pentacle de Saturne", 
        "jour_sacrifice": "Samedi", "destinataire_sac": "Vieilles et vieux",
        "elements_sac": "Tout ce qu'on trouve sous la terre, savon, sel"
    },
    "1122": {
        "nom": "Qala-llahou (Aboubakr Sidik / Fortuna Minor)", "sexe": "Mâle", "temps_naturel": "Passé",
        "arbres": ["Alladjô", "Congo Sirani", "Racines coupant la route"],
        "plantes_sacrees": "Aladjon, racines d'arbres coupant la route",
        "psaume": "Psaume 121", "verset": "Psaume 46 v.2", "sceau": "4e Pentacle du Soleil", 
        "jour_sacrifice": "Dimanche", "destinataire_sac": "Personnages de grande renommée, chefs",
        "elements_sac": "Cola blanc, habit blanc, bélier blanc"
    },
    "1221": {
        "nom": "Solomana (Manssa Souleymane / Carcer)", "sexe": "Femelle", "temps_naturel": "Présent",
        "arbres": ["Zamba", "Sira (Baobab)", "Mandé sounsoun", "Sounsoun"],
        "plantes_sacrees": "Mandé sounsoun, Sounsoun",
        "psaume": "Psaume 142", "verset": "Isaïe 22 v.22", "sceau": "7e Pentacle de Saturne", 
        "jour_sacrifice": "Samedi", "destinataire_sac": "Vieilles et vieux",
        "elements_sac": "Tout ce qu'on trouve sous la terre, savon, sel"
    },
    "2112": {
        "nom": "Badra (Badra Aliou / Conjunctio)", "sexe": "Femelle", "temps_naturel": "Présent",
        "arbres": ["Triki", "Gouélé"],
        "plantes_sacrees": "Guélé",
        "psaume": "Psaume 133", "verset": "Ruth 1 v.16", "sceau": "4e Pentacle de Mercure", 
        "jour_sacrifice": "Mercredi", "destinataire_sac": "Chanteur, griot ou muezzin",
        "elements_sac": "Choses à plusieurs couleurs (pintade, fonio, poule)"
    },
    "2211": {
        "nom": "Nouhou (Nouhoum / Cauda Draconis)", "sexe": "Femelle", "temps_naturel": "Futur",
        "arbres": ["Koudjè", "Zèguènè", "Goundjè"],
        "plantes_sacrees": "Goundjè",
        "psaume": "Psaume 59", "verset": "Psaume 68 v.2", "sceau": "6e Pentacle de Saturne", 
        "jour_sacrifice": "Dimanche", "destinataire_sac": "Renommés, grands personnages",
        "elements_sac": "Cola blanc, habit blanc, bélier blanc"
    },
    "1112": {
        "nom": "Laoussana (Alhoussein / Puella)", "sexe": "Femelle", "temps_naturel": "Passé",
        "arbres": ["Herbes des vieux puits", "Les ravins", "Rigoles", "Plantes gluantes", "Djoulasonkalani"],
        "plantes_sacrees": "Djoulasonkalani",
        "psaume": "Psaume 119 (Aleph)", "verset": "Cantique 4 v.7", "sceau": "2e Pentacle de Vénus", 
        "jour_sacrifice": "Samedi", "destinataire_sac": "Vieilles et vieux",
        "elements_sac": "Tout ce qu'on trouve sous la terre, savon, sel"
    },
    "1211": {
        "nom": "Ousmane (Mory Zoumana / Acquisitio)", "sexe": "Mâle", "temps_naturel": "Futur",
        "arbres": ["Troubala", "Dougalen", "Chou Toro", "N'doubalé", "Frogofraga"],
        "plantes_sacrees": "N'doubalé, Frogofraga",
        "psaume": "Psaume 23", "verset": "Psaume 23 v.1", "sceau": "3e Pentacle de Jupiter", 
        "jour_sacrifice": "Jeudi", "destinataire_sac": "Plusieurs personnes (Groupe)",
        "elements_sac": "Fruits secs, longs animaux"
    },
    "2121": {
        "nom": "Younouss (Tontigui)", "sexe": "Femelle", "temps_naturel": "Futur",
        "arbres": ["Fogofogo", "N'tomotigui", "Zondjè"],
        "plantes_sacrees": "N'tomotigui, Zondjè",
        "psaume": "Psaume 112", "verset": "Deutéronome 28 v.12", "sceau": "6e Pentacle de Jupiter", 
        "jour_sacrifice": "Vendredi", "destinataire_sac": "Enfants",
        "elements_sac": "Bijoux, parures ou objets brillants"
    },
    "2222": {
        "nom": "Moussa (Djama / Populus)", "sexe": "Femelle", "temps_naturel": "Présent",
        "arbres": ["Tomy", "Sounzoufing", "N'tomi", "N'galama"],
        "plantes_sacrees": "N'tomi, N'galama",
        "psaume": "Psaume 47", "verset": "Genèse 22 v.17", "sceau": "1er Pentacle de la Lune", 
        "jour_sacrifice": "Lundi", "destinataire_sac": "Religieux ou gardiens du culte",
        "elements_sac": "Fruits frais, graines de céréales, animaux féminins"
    }
}

MAISONS_META = {
    1: {"nom": "M1 (Consultant / Tête)", "temps_maison": "Présent"},
    2: {"nom": "M2 (Gains / Argent / Chance)", "temps_maison": "Présent"},
    3: {"nom": "M3 (Entourage / Frères)", "temps_maison": "Présent"},
    4: {"nom": "M4 (Foyer / Patrimoine / Fin)", "temps_maison": "Présent"},
    5: {"nom": "M5 (Enfants / Amours / Nouvelles)", "temps_maison": "Présent"},
    6: {"nom": "M6 (Maladie / Obstacles / Serviteurs)", "temps_maison": "Présent"},
    7: {"nom": "M7 (Conjoint / Mariage / Adversaire)", "temps_maison": "Présent"},
    8: {"nom": "M8 (Mort / Transformations / Craintes)", "temps_maison": "Présent"},
    9: {"nom": "M9 (Voyages lointains / Spiritualité)", "temps_maison": "Passé"},
    10: {"nom": "M10 (Carrière / Pouvoir / Chef)", "temps_maison": "Passé"},
    11: {"nom": "M11 (Appuis / Amis / Espoirs)", "temps_maison": "Futur"},
    12: {"nom": "M12 (Épreuves / Ennemis cachés)", "temps_maison": "Futur"},
    13: {"nom": "M13 (Chambre du consultant / Témoin Droit)", "temps_maison": "Passé"},
    14: {"nom": "M14 (Ressources futures / Témoin Gauche)", "temps_maison": "Futur"},
    15: {"nom": "M15 (Le Juge final)", "temps_maison": "Présent"},
    16: {"nom": "M16 (La Sentence / Issue ultime)", "temps_maison": "Passé"}
}


# =====================================================================
# 2. MOTEUR MATHÉMATIQUE GÉOMANTIQUE CORRIGÉ (COUPLES DE FILLES)
# =====================================================================
class EngineGeomancyPro:
    def __init__(self, m1, m2, m3, m4, question):
        self.question = str(question).strip()
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
        for i in [1, 2, 3, 4]:
            if len(self.maisons[i]) != 4 or not set(self.maisons[i]).issubset({"1", "2"}):
                raise ValueError(f"M{i} incorrecte.")

        # --- CORRECTION ICI : Extraction verticale stricte pour générer M5 à M8 ---
        # M5 prend la tête des 4 premières mères, M6 prend la poitrine, etc.
        self.maisons[5] = self.maisons[1][0] + self.maisons[2][0] + self.maisons[3][0] + self.maisons[4][0]
        self.maisons[6] = self.maisons[1][1] + self.maisons[2][1] + self.maisons[3][1] + self.maisons[4][1]
        self.maisons[7] = self.maisons[1][2] + self.maisons[2][2] + self.maisons[3][2] + self.maisons[4][2]
        self.maisons[8] = self.maisons[1][3] + self.maisons[2][3] + self.maisons[3][3] + self.maisons[4][3]

        # Neveux (M9 à M12)
        self.maisons[9]  = self._addition_geomantique(self.maisons[1], self.maisons[2])
        self.maisons[10] = self._addition_geomantique(self.maisons[3], self.maisons[4])
        self.maisons[11] = self._addition_geomantique(self.maisons[5], self.maisons[6])
        self.maisons[12] = self._addition_geomantique(self.maisons[7], self.maisons[8])

        # Témoins (M13, M14), Juge (M15) et Sentence (M16)
        self.maisons[13] = self._addition_geomantique(self.maisons[9], self.maisons[10])
        self.maisons[14] = self._addition_geomantique(self.maisons[11], self.maisons[12])
        self.maisons[15] = self._addition_geomantique(self.maisons[13], self.maisons[14])
        self.maisons[16] = self._addition_geomantique(self.maisons[15], self.maisons[1])

    def _calculer_passations(self):
        carte = {}
        for m, code in self.maisons.items():
            if code not in carte: carte[code] = []
            carte[code].append(m)
        return {code: m_list for code, m_list in carte.items() if len(m_list) > 1}

    def verifier_veracite_theme(self):
        alertes = []
        for code, m_list in self.passations.items():
            fig_nom = FIGURES_DB.get(code, {"nom": "Inconnue"})["nom"]
            if "Almangoussi" in fig_nom and 1 in m_list and 8 in m_list:
                alertes.append("❌ REJET FORMEL (Mensonge) : Almangoussi ne passera jamais de M1 à M8.")
            if "Youssouf" in fig_nom and 1 in m_list and 7 in m_list:
                alertes.append("❌ REJET FORMEL (Mensonge) : Youssouf ne passera jamais de M1 à M7.")
            if "Issa" in fig_nom and 1 in m_list and 6 in m_list:
                alertes.append("❌ REJET FORMEL (Mensonge) : Issa ne passera jamais de M1 à M6.")

        juge_nom = FIGURES_DB.get(self.maisons[15], {}).get("nom", "")
        if any(d in juge_nom for d in ["Nouhou", "Almangoussi"]):
            alertes.append(f"❌ THÈME KHAFIR : Un Djin ({juge_nom}) ne peut pas siéger en M15.")

        cop_1_7 = self._addition_geomantique(self.maisons[1], self.maisons[7])
        cop_4_10 = self._addition_geomantique(self.maisons[4], self.maisons[10])
        fig_verite = self._addition_geomantique(cop_1_7, cop_4_10)
        if fig_verite not in self.maisons.values():
            alertes.append(f"⚠️ CONCORDANCE FAIBLE : La figure témoin de vérité ({FIGURES_DB.get(fig_verite, {}).get('nom')}) n'apparaît nulle part.")

        return alertes

    def interpreter_temps_et_sacrifices(self):
        interpretations = []
        for code, m_list in self.passations.items():
            fig_data = FIGURES_DB.get(code)
            if not fig_data: continue
            for m in m_list:
                t_maison = MAISONS_META[m]["temps_maison"]
                t_figure = fig_data["temps_naturel"]
                if t_figure == "Passé" and t_maison == "Passé":
                    interpretations.append(f"• {fig_data['nom']} en {MAISONS_META[m]['nom']} : Événement consommé. Sacrifice dû aux VIEILLES ET VIEUX.")
                elif t_figure == "Passé" and t_maison == "Présent":
                    interpretations.append(f"• {fig_data['nom']} en {MAISONS_META[m]['nom']} : Une vieille affaire resurgit au présent. Sacrifice dû aux VIEILLES ET VIEUX.")
                elif t_figure == "Présent" and t_maison == "Présent":
                    interpretations.append(f"• {fig_data['nom']} en {MAISONS_META[m]['nom']} : Action immédiate en cours. Offrir le sacrifice à vos PAIRS (Même âge).")
                elif t_figure == "Futur" and t_maison == "Futur":
                    interpretations.append(f"• {fig_data['nom']} en {MAISONS_META[m]['nom']} : Projet d'avenir solide. Donner le sacrifice aux ENFANTS.")
        return interpretations

    def analyser_axe_mariage(self):
        m1 = self.maisons[1]
        m7 = self.maisons[7]
        if m1 == m7 or (m1 in self.passations and 7 in self.passations[m1]):
            return f"💍 MARIAGE VERROUILLÉ : Passation directe validée de M1 à M7 avec la figure {FIGURES_DB[m1]['nom']}."
        if FIGURES_DB[m1]["sexe"] == "Mâle" and FIGURES_DB[m7]["sexe"] == "Femelle":
            return "⏳ HARMONIE PARFAITE : M1 est Mâle et M7 est Femelle. L'accord est naturel mais nécessite des ouvertures de routes."
        return "❌ AXE COMPACT : Aucune passation ni concordance de polarité détectée sur l'axe M1-M7."

    def calculer_part_de_fortune_exacte(self):
        total_points = sum(int(caractere) for m_code in self.maisons.values() for caractere in m_code)
        reste = total_points % 12
        maison_chute = 12 if reste == 0 else reste
        return {
            "total_points": total_points,
            "maison_cible": f"M{maison_chute} ({MAISONS_META[maison_chute]['nom']})",
            "figure": FIGURES_DB.get(self.maisons[maison_chute], {"nom": "Inconnue"})["nom"]
        }

    def compiler_fiche_theurgique(self, maison_index):
        code = self.maisons[maison_index]
        data = FIGURES_DB.get(code)
        if not data: return {}
        
        num_psaume = int("".join([c for c in data["psaume"] if c.isdigit()]))
        cle = 7 if (num_psaume % 9) in [1, 4, 8] else (9 if (num_psaume % 9) in [3, 6, 0] else 3)
        somme_mystique = num_psaume + cle
        
        base = (somme_mystique - 12) // 3
        reste = (somme_mystique - 12) % 3
        c1, c2, c3, c4, c5, c6, c7, c8, c9 = [base + i for i in range(9)]
        if reste == 1: c7 += 1; c8 += 1; c9 += 1
        elif reste == 2: c4 += 1; c5 += 1; c6 += 1; c7 += 2; c8 += 2; c9 += 2

        carre_visuel = f"| {c4} | {c9} | {c2} | \\n | {c3} | {c5} | {c7} | \\n | {c8} | {c1} | {c6} |"

        return {
            "figure": data["nom"],
            "arbres_sacres": data["arbres"],
            "feuilles_plantes": data["plantes_sacrees"],
            "theurgie": {
                "psaume_tracer": data["psaume"],
                "verset_verrou": data["verset"],
                "sceau_salomon": data["sceau"],
                "jour_vibration": data["jour_sacrifice"],
                "destinataire": data["destinataire_sac"],
                "offrande_matiere": data["elements_sac"]
            },
            "carre_magique": {"somme": somme_mystique, "visuel": carre_visuel}
        }

    def generer_rapport_complet(self):
        alertes = self.verifier_veracite_theme()
        cartographie = {f"Maison {m} ({MAISONS_META[m]['nom']})": FIGURES_DB.get(code, {"nom": "Inconnue"})["nom"] for m, code in self.maisons.items()}

        return {
            "statut_du_theme": "VALIDE" if not alertes else "REJET / CONTRADICTION",
            "question_analysee": self.question,
            "verifications_traditionnelles": alertes if alertes else ["Le thème respecte parfaitement les lois de vérité du document."],
            "cartographie_des_16_maisons": cartographie,
            "analyse_temporelle_et_sacrifices": self.interpreter_temps_et_sacrifices(),
            "axe_mariage_et_accords": self.analyser_axe_mariage(),
            "part_de_fortune": self.calculer_part_de_fortune_exacte(),
            "remedes_theurgiques": {
                "le_juge_m15": self.compiler_fiche_theurgique(15),
                "la_sentence_m16": self.compiler_fiche_theurgique(16)
            }
        }


def executer_consultation_geomantique(mere1, mere2, mere3, mere4, question_texte):
    try:
        moteur = EngineGeomancyPro(mere1, mere2, mere3, mere4, question_texte)
        return moteur.generer_rapport_complet()
    except Exception as fatal_error:
        return {
            "statut_du_theme": "ERREUR CRITIQUE",
            "message_erreur": str(fatal_error),
            "conseil": "Saisir 4 chaînes de 4 chiffres composées de 1 et 2 uniquement."
        }
