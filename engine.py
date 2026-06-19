class OracleRamrouComplet:
    def __init__(self):
        # Base de données complète avec 16 figures
        self.db = {
            "Adama": {"pts": [1, 0, 1, 1], "sac": "Coq blanc", "plt": "Djeka", "arom": "Basilic", "huile": "HE de Basilic Tropical", "psaume": "Psaume 1", "vrs": "Genèse 1:1-3", "nss": "Infusion de basilic", "prière": "Prière pour l'ouverture des portes"},
            "Idriss": {"pts": [1, 1, 1, 1], "sac": "Poulet rouge", "plt": "Kinkeliba", "arom": "Menthe", "huile": "HE de Menthe Poivrée", "psaume": "Psaume 23", "vrs": "Proverbes 3:5-6", "nss": "Eau de menthe", "prière": "Prière pour la victoire divine"},
            "Almami": {"pts": [1, 1, 0, 0], "sac": "Chèvre noire", "plt": "N'golo", "arom": "Romarin", "huile": "HE de Romarin", "psaume": "Psaume 35", "vrs": "Matthieu 7:7", "nss": "Infusion de romarin", "prière": "Prière pour l'acquisition"},
            "Badra": {"pts": [0, 1, 1, 1], "sac": "Cola rouge", "plt": "Zaban", "arom": "Laurier", "huile": "HE de Laurier Noble", "psaume": "Psaume 91", "vrs": "Psaume 121:7", "nss": "Eau de laurier", "prière": "Prière de protection absolue"},
            "Ousmane": {"pts": [0, 1, 0, 1], "sac": "Bélier blanc", "plt": "Baobab", "arom": "Sauge", "huile": "HE de Sauge Sclarée", "psaume": "Psaume 121", "vrs": "Philippiens 4:13", "nss": "Bain de sauge", "prière": "Prière pour la stabilité"},
            "Nouhou": {"pts": [1, 1, 1, 0], "sac": "Pigeon blanc", "plt": "Tamarin", "arom": "Lavande", "huile": "HE de Lavande Vraie", "psaume": "Psaume 27", "vrs": "Jérémie 29:11", "nss": "Eau de lavande", "prière": "Prière pour la paix"},
            "Moussa": {"pts": [1, 0, 0, 1], "sac": "Charbon", "plt": "Nébédaye", "arom": "Thym", "huile": "HE de Thym à Thymol", "psaume": "Psaume 51", "vrs": "Psaume 34:17", "nss": "Eau de thym", "prière": "Prière pour la délivrance"},
            "Solomane": {"pts": [1, 0, 0, 0], "sac": "Sel gemme", "plt": "Karité", "arom": "Cèdre", "huile": "HE de Cèdre de l'Atlas", "psaume": "Psaume 130", "vrs": "Jacques 1:5", "nss": "Fumigation de cèdre", "prière": "Prière pour la Sagesse"},
            "Mangoussi": {"pts": [0, 0, 0, 1], "sac": "Miel pur", "plt": "Goyavier", "arom": "Citron", "huile": "HE de Citron (Zeste)", "psaume": "Psaume 103", "vrs": "Jean 10:10", "nss": "Eau citronnée", "prière": "Prière pour la joie"},
            "Bourama": {"pts": [0, 1, 1, 0], "sac": "Poulet noir", "plt": "N'péné", "arom": "Cannelle", "huile": "HE de Cannelle", "psaume": "Psaume 34", "vrs": "Matthieu 19:6", "nss": "Eau de cannelle", "prière": "Prière pour l'union"},
            "Issa": {"pts": [0, 0, 1, 1], "sac": "Lait frais", "plt": "Fleur d'oranger", "arom": "Mélisse", "huile": "HE de Mélisse", "psaume": "Psaume 25", "vrs": "2 Corinthiens 12:9", "nss": "Eau de mélisse", "prière": "Prière pour la grâce"},
            "Alaou tala": {"pts": [1, 1, 0, 1], "sac": "Bougie blanche", "plt": "Encens oliban", "arom": "Encens", "huile": "HE d'Encens (Oliban)", "psaume": "Psaume 119", "vrs": "Psaume 24:7", "nss": "Eau d'encens", "prière": "Prière pour l'élévation"},
            "Laoussana": {"pts": [0, 1, 0, 0], "sac": "Pain", "plt": "Menthe", "arom": "Verveine", "huile": "HE de Verveine", "psaume": "Psaume 19", "vrs": "Nombres 6:24-26", "nss": "Eau de verveine", "prière": "Prière pour la bénédiction"},
            "Tonigui": {"pts": [0, 0, 1, 0], "sac": "Tissu rouge", "plt": "Piment", "arom": "Gingembre", "huile": "HE de Gingembre", "psaume": "Psaume 7", "vrs": "Éphésiens 6:10", "nss": "Eau de gingembre", "prière": "Prière pour la force"},
            "Lomara": {"pts": [1, 0, 0, 0], "sac": "Tissu noir", "plt": "Dattier", "arom": "Girofle", "huile": "HE de Clou de Girofle", "psaume": "Psaume 38", "vrs": "Psaume 23:4", "nss": "Bain aux girofles", "prière": "Prière pour la méditation"},
            "Maldjou": {"pts": [0, 0, 0, 0], "sac": "Eau de source", "plt": "Citronnelle", "arom": "Eucalyptus", "huile": "HE d'Eucalyptus", "psaume": "Psaume 142", "vrs": "Ésaïe 41:10", "nss": "Bain d'eucalyptus", "prière": "Prière pour la fin des maux"}
        }
        self.delais = {"Youssouf": 1, "Adama": 3, "Maldjou": 5, "Idriss": 10, "Tontigui": 15, "Laoussana": 21, "Oumar": 28, "Ayouba": 36, "Alaou tala": 45, "Solomane": 55, "Badra": 66, "Nouhou": 78, "Bourama": 91, "Issa": 105, "Moussa": 120, "Ousmane": 136}

    def copuler(self, fig1_nom, fig2_nom):
        p1 = self.db.get(fig1_nom, {"pts": [0,0,0,0]})["pts"]
        p2 = self.db.get(fig2_nom, {"pts": [0,0,0,0]})["pts"]
        res_pts = [p1[i] ^ p2[i] for i in range(4)]
        for nom, data in self.db.items():
            if data["pts"] == res_pts: return nom
        return "Inconnu"

    def fiche_spirituelle(self, nom_fig):
        d = self.db.get(nom_fig)
        return (f"--- PROTOCOLE SPIRITUEL : {nom_fig} ---\n"
                f"1. Prière de Salomon : {d['prière']}\n"
                f"2. Écriture : Psaume {d['psaume']} + {d['vrs']}\n"
                f"3. Sacrifice : {d['sac']}\n"
                f"4. Plantes : {d['plt']} & {d['arom']}\n"
                f"5. Huile Essentielle : {d['huile']}\n"
                f"6. Préparation Nassi : {d['nss']} (Ajouter 3 gouttes de {d['huile']} dans l'eau).")

    def generer_verdict(self, sujet, theme):
        if sujet == "mariage":
            res = self.copuler(self.copuler(theme['M1'], theme['M7']), theme['M5'])
            return f"Verdict Mariage : {res}.\n\n{self.fiche_spirituelle(res)}"
        elif sujet == "delai":
            f1 = self.copuler(theme['M5'], theme['M9'])
            f2 = self.copuler(theme['M15'], theme['M16'])
            res = self.copuler(f1, f2)
            jours = self.delais.get(res, "indéfini")
            return f"Délai : {jours} jours.\n\n{self.fiche_spirituelle(res)}"
        return "Sujet non traité."
