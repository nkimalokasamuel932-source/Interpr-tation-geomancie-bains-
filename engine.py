class OracleRamrouComplet:
    def __init__(self):
        self.db = {
            "Adama": {"pts": [1, 0, 1, 1], "sac": "Coq blanc", "plt": "Djeka", "arom": "Basilic", "huile": "HE de Basilic", "psaume": "1", "vrs": "Genèse 1:1", "nss": "Infusion de basilic", "prière": "Prière pour l'ouverture", "signification": "Ouverture, nouveau départ, clarté."},
            "Idriss": {"pts": [1, 1, 1, 1], "sac": "Poulet rouge", "plt": "Kinkeliba", "arom": "Menthe", "huile": "HE de Menthe", "psaume": "23", "vrs": "Proverbes 3:5", "nss": "Eau de menthe", "prière": "Prière pour la sagesse", "signification": "Connaissance, éducation, direction divine."},
            "Almami": {"pts": [1, 1, 0, 0], "sac": "Chèvre noire", "plt": "N'golo", "arom": "Romarin", "huile": "HE de Romarin", "psaume": "35", "vrs": "Matthieu 7:7", "nss": "Infusion de romarin", "prière": "Prière pour l'acquisition", "signification": "Réussite, acquisition de biens, autorité."},
            "Badra": {"pts": [0, 1, 1, 1], "sac": "Cola rouge", "plt": "Zaban", "arom": "Laurier", "huile": "HE de Laurier", "psaume": "91", "vrs": "Psaume 121:7", "nss": "Eau de laurier", "prière": "Prière de protection", "signification": "Protection divine, invincibilité, bouclier."},
            "Ousmane": {"pts": [0, 1, 0, 1], "sac": "Bélier blanc", "plt": "Baobab", "arom": "Sauge", "huile": "HE de Sauge", "psaume": "121", "vrs": "Philippiens 4:13", "nss": "Bain de sauge", "prière": "Prière pour la stabilité", "signification": "Stabilité, maison, fondations solides."},
            "Nouhou": {"pts": [1, 1, 1, 0], "sac": "Pigeon blanc", "plt": "Tamarin", "arom": "Lavande", "huile": "HE de Lavande", "psaume": "27", "vrs": "Jérémie 29:11", "nss": "Eau de lavande", "prière": "Prière pour la paix", "signification": "Tranquillité, espoir, retour au calme."},
            "Moussa": {"pts": [1, 0, 0, 1], "sac": "Charbon", "plt": "Nébédaye", "arom": "Thym", "huile": "HE de Thym", "psaume": "51", "vrs": "Psaume 34:17", "nss": "Eau de thym", "prière": "Prière pour la délivrance", "signification": "Libération des liens, purification, pardon."},
            "Solomane": {"pts": [1, 0, 0, 0], "sac": "Sel gemme", "plt": "Karité", "arom": "Cèdre", "huile": "HE de Cèdre", "psaume": "130", "vrs": "Jacques 1:5", "nss": "Fumigation de cèdre", "prière": "Prière pour la sagesse", "signification": "Justice, discernement, intelligence spirituelle."},
            "Mangoussi": {"pts": [0, 0, 0, 1], "sac": "Miel pur", "plt": "Goyavier", "arom": "Citron", "huile": "HE de Citron", "psaume": "103", "vrs": "Jean 10:10", "nss": "Eau citronnée", "prière": "Prière pour la joie", "signification": "Abondance, bonheur, vie en plénitude."},
            "Bourama": {"pts": [0, 1, 1, 0], "sac": "Poulet noir", "plt": "N'péné", "arom": "Cannelle", "huile": "HE de Cannelle", "psaume": "34", "vrs": "Matthieu 19:6", "nss": "Eau de cannelle", "prière": "Prière pour l'union", "signification": "Mariage, alliance, union sacrée."},
            "Issa": {"pts": [0, 0, 1, 1], "sac": "Lait frais", "plt": "Fleur d'oranger", "arom": "Mélisse", "huile": "HE de Mélisse", "psaume": "25", "vrs": "2 Corinthiens 12:9", "nss": "Eau de mélisse", "prière": "Prière pour la grâce", "signification": "Miséricorde, faveur divine, pardon."},
            "Alaou tala": {"pts": [1, 1, 0, 1], "sac": "Bougie blanche", "plt": "Encens oliban", "arom": "Encens", "huile": "HE d'Encens", "psaume": "119", "vrs": "Psaume 24:7", "nss": "Eau d'encens", "prière": "Prière pour l'élévation", "signification": "Élévation spirituelle, connexion avec Dieu."},
            "Laoussana": {"pts": [0, 1, 0, 0], "sac": "Pain", "plt": "Menthe", "arom": "Verveine", "huile": "HE de Verveine", "psaume": "19", "vrs": "Nombres 6:24", "nss": "Eau de verveine", "prière": "Prière pour la bénédiction", "signification": "Prosperité, chance, bénédictions terrestres."},
            "Tonigui": {"pts": [0, 0, 1, 0], "sac": "Tissu rouge", "plt": "Piment", "arom": "Gingembre", "huile": "HE de Gingembre", "psaume": "7", "vrs": "Éphésiens 6:10", "nss": "Eau de gingembre", "prière": "Prière pour la force", "signification": "Courage, combat spirituel, puissance."},
            "Lomara": {"pts": [1, 0, 0, 0], "sac": "Tissu noir", "plt": "Dattier", "arom": "Girofle", "huile": "HE de Girofle", "psaume": "38", "vrs": "Psaume 23:4", "nss": "Bain aux girofles", "prière": "Prière pour la méditation", "signification": "Protection nocturne, refuge, calme."},
            "Maldjou": {"pts": [0, 0, 0, 0], "sac": "Eau de source", "plt": "Citronnelle", "arom": "Eucalyptus", "huile": "HE d'Eucalyptus", "psaume": "142", "vrs": "Ésaïe 41:10", "nss": "Bain d'eucalyptus", "prière": "Prière pour la fin des maux", "signification": "Achèvement, guérison, repos final."}
        }
    def get_guide_activation(self):
        return (
            "### Guide de préparation du Nassi (Rituel)\n"
            "1. **Intention** : Tenez l'eau à deux mains, visualisez votre demande.\n"
            "2. **Activation** : Récitez le Psaume attribué à haute voix.\n"
            "3. **Souffle** : Assurez-vous que votre souffle touche la surface de l'eau.\n"
            "4. **Scellement** : Récitez le verset biblique et faites un signe de croix."
        )
    def copuler(self, f1, f2):
        p1, p2 = self.db[f1]["pts"], self.db[f2]["pts"]
        res = [p1[i] ^ p2[i] for i in range(4)]
        for n, d in self.db.items():
            if d["pts"] == res: return n
        return "Adama"

    def get_details(self, n):
        d = self.db[n]
        return f"**Signification :** {d['signification']}\n\n**Prière :** {d['prière']}\n**Écriture :** Psaume {d['psaume']} - {d['vrs']}\n**Sacrifice :** {d['sac']}\n**Plantes :** {d['plt']} & {d['arom']}\n**Huile :** {d['huile']}\n**Nassi :** {d['nss']}"
