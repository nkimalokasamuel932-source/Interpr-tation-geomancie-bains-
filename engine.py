class OracleRamrouComplet:
    def __init__(self):
        self.db = {
            "Adama": {"pts": [1, 0, 1, 1], "sac": "Coq blanc", "plt": "Djeka", "psaume": "Psaume 1", "vrs": "Al-Fatiha", "nss": "Eau de rose"},
            "Idriss": {"pts": [1, 1, 1, 1], "sac": "Poulet rouge", "plt": "Kinkeliba", "psaume": "Psaume 23", "vrs": "Ayat al-Kursi", "nss": "Eau bénite"},
            "Almami": {"pts": [1, 1, 0, 0], "sac": "Chèvre noire", "plt": "N'golo", "psaume": "Psaume 35", "vrs": "Al-Ikhlas", "nss": "Eau safranée"},
            "Badra": {"pts": [0, 1, 1, 1], "sac": "Cola rouge", "plt": "Zaban", "psaume": "Psaume 91", "vrs": "Al-Falaq", "nss": "Eau de pluie"},
            "Ousmane": {"pts": [0, 1, 0, 1], "sac": "Bélier blanc", "plt": "Baobab", "psaume": "Psaume 121", "vrs": "An-Nas", "nss": "Eau pure"},
            "Nouhou": {"pts": [1, 1, 1, 0], "sac": "Pigeon blanc", "plt": "Tamarin", "psaume": "Psaume 27", "vrs": "Al-Waqi'a", "nss": "Eau de source"},
            "Moussa": {"pts": [1, 0, 0, 1], "sac": "Charbon", "plt": "Nébédaye", "psaume": "Psaume 51", "vrs": "Ya-Sin", "nss": "Eau de zam-zam"},
            "Solomane": {"pts": [1, 0, 0, 0], "sac": "Sel gemme", "plt": "Karité", "psaume": "Psaume 130", "vrs": "Al-Mulk", "nss": "Eau de mer"},
            "Mangoussi": {"pts": [0, 0, 0, 1], "sac": "Miel pur", "plt": "Goyavier", "psaume": "Psaume 103", "vrs": "Ar-Rahman", "nss": "Eau parfumée"},
            "Bourama": {"pts": [0, 1, 1, 0], "sac": "Poulet noir", "plt": "N'péné", "psaume": "Psaume 34", "vrs": "Al-Qadr", "nss": "Eau de pluie"},
            "Issa": {"pts": [0, 0, 1, 1], "sac": "Lait frais", "plt": "Fleur d'oranger", "psaume": "Psaume 25", "vrs": "Al-Kawthar", "nss": "Eau sucrée"},
            "Alaou tala": {"pts": [1, 1, 0, 1], "sac": "Bougie blanche", "plt": "Encens oliban", "psaume": "Psaume 119", "vrs": "Al-Fajr", "nss": "Eau d'encens"},
            "Laoussana": {"pts": [0, 1, 0, 0], "sac": "Pain", "plt": "Menthe", "psaume": "Psaume 19", "vrs": "Ad-Duha", "nss": "Eau de menthe"},
            "Tonigui": {"pts": [0, 0, 1, 0], "sac": "Tissu rouge", "plt": "Piment", "psaume": "Psaume 7", "vrs": "Al-Lahab", "nss": "Eau chaude"},
            "Lomara": {"pts": [1, 0, 0, 0], "sac": "Tissu noir", "plt": "Dattier", "psaume": "Psaume 38", "vrs": "At-Takathur", "nss": "Eau de datte"},
            "Maldjou": {"pts": [0, 0, 0, 0], "sac": "Eau de source", "plt": "Citronnelle", "psaume": "Psaume 142", "vrs": "An-Nasr", "nss": "Eau citronnée"}
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
        return f"Sacrifice: {d['sac']} | Plante: {d['plt']} | Récitations: {d['psaume']} + {d['vrs']} | Nassi: {d['nss']}"

    def generer_verdict(self, sujet, theme):
        if sujet == "mariage":
            res = self.copuler(self.copuler(theme['M1'], theme['M7']), theme['M5'])
            return f"Verdict Mariage : {res}. Travail : {self.fiche_spirituelle(res)}"
        elif sujet == "delai":
            f1 = self.copuler(theme['M5'], theme['M9'])
            f2 = self.copuler(theme['M15'], theme['M16'])
            res = self.copuler(f1, f2)
            jours = self.delais.get(res, "indéfini")
            return f"Délai : {jours} jours. Travail : {self.fiche_spirituelle(res)}"
        elif sujet == "vol":
            if theme['M4'] == "Issa": return f"Vol confirmé. Travail : {self.fiche_spirituelle(theme['M4'])}"
            return "Perte accidentelle."
        return "Sujet non traité."
