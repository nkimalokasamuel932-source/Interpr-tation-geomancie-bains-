def generer_verdict_intelligent(self, sujet_texte, theme):
        sujet = sujet_texte.lower()
        
        # 1. Détermination de la figure résultat selon le sujet
        if "mariage" in sujet or "union" in sujet or "amour" in sujet:
            res = self.copuler(self.copuler(theme['M1'], theme['M7']), theme['M5'])
            titre = "Verdict Mariage/Union"
        elif "travail" in sujet or "emploi" in sujet or "business" in sujet:
            res = self.copuler(self.copuler(theme['M1'], theme['M2']), theme['M6'])
            titre = "Verdict Travail/Business"
        elif "voyage" in sujet or "déplacement" in sujet:
            res = self.copuler(self.copuler(theme['M1'], theme['M7']), theme['M9'])
            titre = "Verdict Voyage"
        elif "argent" in sujet or "finances" in sujet or "gain" in sujet:
            res = self.copuler(theme['M2'], theme['M8'])
            titre = "Verdict Financier"
        else:
            res = self.copuler(theme['M15'], theme['M16'])
            titre = "Verdict Général"
            
        # 2. Récupération des données détaillées dans la base de données
        d = self.db.get(res)
        
        # 3. Construction du rapport complet
        rapport = (
            f"### {titre} : {res}\n\n"
            f"**1. Prière de Salomon :** {d['prière']}\n"
            f"**2. Écriture Sainte :** Psaume {d['psaume']} + {d['vrs']}\n"
            f"**3. Sacrifice / Offrande :** {d['sac']}\n"
            f"**4. Plantes :** {d['plt']} (Sacrée) + {d['arom']} (Aromatique)\n"
            f"**5. Huile Essentielle :** {d['huile']}\n"
            f"**6. Préparation Nassi :** {d['nss']}\n"
            f"   *Protocole :* Ajoutez 3 gouttes de l'huile essentielle dans l'eau de Nassi avant la prière."
        )
        return rapport
