class OracleRamrouComplet:
    def __init__(self):
        # Base de données complète : Figures, Sacrifices, Plantes, Huiles, Prières, Versets
        self.db = {
            "Adama": {"pts": [1, 0, 1, 1], "sac": "Coq blanc", "plt": "Djeka", "arom": "Basilic", "huile": "HE de Basilic Tropical", "psaume": "1", "vrs": "Genèse 1:1-3", "nss": "Infusion de basilic", "prière": "Prière pour l'ouverture des portes"},
            "Idriss": {"pts": [1, 1, 1, 1], "sac": "Poulet rouge", "plt": "Kinkeliba", "arom": "Menthe", "huile": "HE de Menthe Poivrée", "psaume": "23", "vrs": "Proverbes 3:5-6", "nss": "Eau de menthe", "prière": "Prière pour la victoire divine"},
            "Almami": {"pts": [1, 1, 0, 0], "sac": "Chèvre noire", "plt": "N'golo", "arom": "Romarin", "huile": "HE de Romarin", "psaume": "35", "vrs": "Matthieu 7:7", "nss": "Infusion de romarin", "prière": "Prière pour l'acquisition"},
            "Badra": {"pts": [0, 1, 1, 1], "sac": "Cola rouge", "plt": "Zaban", "arom": "Laurier", "huile": "HE de Laurier Noble", "psaume": "91", "vrs": "Psaume 121:7", "nss": "Eau de laurier", "prière": "Prière de protection absolue"},
            "Ousmane": {"pts": [0, 1, 0, 1], "sac": "Bélier blanc", "plt": "Baobab", "arom": "Sauge", "huile": "HE de Sauge Sclarée", "psaume": "121", "vrs": "Philippiens 4:13", "nss": "Bain de sauge", "prière": "Prière pour la stabilité"},
            "Nouhou": {"pts": [1, 1, 1, 0], "sac": "Pigeon blanc", "plt": "Tamarin", "arom": "Lavande", "huile": "HE de Lavande Vraie", "psaume": "27", "vrs": "Jérémie 29:11", "nss": "Eau de lavande", "prière": "Prière pour la paix"},
            "Moussa": {"pts": [1, 0, 0, 1], "sac": "Charbon", "plt": "Nébédaye", "arom": "Thym", "huile": "HE de Thym à Thymol", "psaume": "51", "vrs": "Psaume 34:17", "nss": "Eau de thym", "prière": "Prière pour la délivrance"},
            "Solomane": {"pts": [1, 0, 0, 0], "sac": "Sel gemme", "plt": "Karité", "arom": "Cèdre", "huile": "HE de Cèdre de l'Atlas", "psaume": "130", "vrs": "Jacques 1:5", "nss": "Fumigation de cèdre", "prière": "Prière pour la Sagesse"},
            "Mangoussi": {"pts": [0, 0, 0, 1], "sac": "Miel pur", "plt": "Goyavier", "arom": "Citron", "huile": "HE de Citron (Zeste)", "psaume": "103", "vrs": "Jean 10:10", "nss": "Eau citronnée", "prière": "Prière pour la joie"},
            "Bourama": {"pts": [0, 1, 1, 0], "sac": "Poulet noir", "plt": "N'péné", "arom": "Cannelle", "huile": "HE de Cannelle", "psaume": "34", "vrs": "Matthieu 19:6", "nss": "Eau de cannelle", "prière": "Prière pour l'union"},
            "Issa": {"pts": [0, 0, 1, 1], "sac": "Lait frais", "plt": "Fleur d'oranger", "arom": "Mélisse", "huile": "HE de Mélisse", "psaume": "25", "vrs": "2 Corinthiens 12:9", "nss": "Eau de mélisse", "prière": "Prière pour la grâce"},
            "Alaou tala": {"pts": [1, 1, 0, 1], "sac": "Bougie blanche", "plt": "Encens oliban", "arom": "Encens", "huile": "HE d'Encens (Oliban)", "psaume": "119", "vrs": "Psaume 24:7", "nss": "Eau d'encens", "prière": "Prière pour l'élévation"},
            "Laoussana": {"pts": [0, 1, 0, 0], "sac": "Pain", "plt": "Menthe", "arom": "Verveine", "huile": "HE de Verveine", "psaume": "19", "vrs": "Nombres 6:24-26", "nss": "Eau de verveine", "prière": "Prière pour la bénédiction"},
            "Tonigui": {"pts": [0, 0, 1, 0], "sac": "Tissu rouge", "plt": "Piment", "arom": "Gingembre", "huile": "HE de Gingembre", "psaume": "7", "vrs": "Éphésiens 6:10", "nss": "Eau de gingembre", "prière": "Prière pour la force"},
            "Lomara": {"pts": [1, 0, 0, 0], "sac": "Tissu noir", "plt": "Dattier", "arom": "Girofle", "huile": "HE de Clou de Girofle", "psaume": "38", "vrs": "Psaume 23:4", "nss": "Bain aux girofles", "prière": "Prière pour la méditation"},
            "Maldjou": {"pts": [0, 0, 0, 0], "sac": "Eau de source", "plt": "Citronnelle", "arom": "Eucalyptus", "huile": "HE d'Eucalyptus", "psaume": "142", "vrs": "Ésaïe 41:10", "nss": "Bain d'eucalyptus", "prière": "Prière pour la fin des maux"}
        }

    def copuler(self, fig1, fig2):
        p1 = self.db[fig1]["pts"]
        p2 = self.db[fig2]["pts"]
        res_pts = [p1[i] ^ p2[i] for i in range(4)]
        for nom, data in self.db.items():
            if data["pts"] == res_pts: return nom
        return "Adama"

    def generer_verdict_intelligent(self, sujet_texte, theme):
        sujet = sujet_texte.lower()
        if "mariage" in sujet or "union" in sujet:
            res = self.copuler(self.copuler(theme['M1'], theme['M7']), theme['M5'])
            titre = "Verdict Mariage/Union"
        elif "travail" in sujet or "emploi" in sujet:
            res = self.copuler(self.copuler(theme['M1'], theme['M2']), theme['M6'])
            titre = "Verdict Travail/Emploi"
        else:
            res = self.copuler(theme['M15'], theme['M16'])
            titre = "Verdict Général"
            
        d = self.db[res]
        return (f"### {titre} : {res}\n\n"
                f"1. **Prière de Salomon :** {d['prière']}\n"
                f"2. **Écriture Sainte :** Psaume {d['psaume']} + {d['vrs']}\n"
                f"3. **Sacrifice :** {d['sac']}\n"
                f"4. **Plantes :** {d['plt']} & {d['arom']}\n"
                f"5. **Huile Essentielle :** {d['huile']}\n"
                f"6. **Protocole Nassi :** {d['nss']} (Ajouter 3 gouttes de {d['huile']} dans l'eau).")
