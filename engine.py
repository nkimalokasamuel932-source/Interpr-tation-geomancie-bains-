import sqlite3

# Dictionnaire des significations des 16 Maisons
maisons_definitions = {
    "M1": "Consultant / Personnalité", "M2": "Finances / Biens",
    "M3": "Entourage / Communication", "M4": "Foyer / Racines",
    "M5": "Projets / Créativité", "M6": "Travail / Santé",
    "M7": "Partenaires / Contrats", "M8": "Influences extérieures / Dettes",
    "M9": "Savoir / Spiritualité", "M10": "Carrière / Statut",
    "M11": "Appuis / Espoirs", "M12": "Épreuves cachées",
    "M13": "Passé récent", "M14": "Futur proche",
    "M15": "Juge (Synthèse)", "M16": "Témoin final (Confirmation)"
}

# Dictionnaire des significations des 16 Figures
figures_definitions = {
    "Laetitia": "Joie, réussite, énergie expansive.",
    "Tristitia": "Tristesse, blocage, repli.",
    "Fortuna Major": "Grande fortune, autorité.",
    "Fortuna Minor": "Petite fortune, aide ponctuelle.",
    "Acquisitio": "Gain, succès matériel.",
    "Amissio": "Perte, dissipation.",
    "Caput Draconis": "Début, ouverture.",
    "Cauda Draconis": "Fin, clôture, retrait.",
    "Conjunctio": "Union, contrat.",
    "Carcer": "Prison, retard.",
    "Puella": "Douceur, harmonie.",
    "Puer": "Impétuosité, énergie.",
    "Albus": "Paix, sagesse, clarté.",
    "Rubeus": "Passion, danger, intensité.",
    "Via": "Mouvement, changement.",
    "Populus": "Collectif, foule, incertitude."
}

def init_db():
    conn = sqlite3.connect('geomancie.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS historique 
                      (id INTEGER PRIMARY KEY, nom_consultant TEXT, tirage TEXT, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def obtenir_analyse_par_axes(t):
    """Regroupe les résultats par axes de lecture métier."""
    analyse_structuree = {
        "Axe de la Manifestation (Objectifs/Partenaires)": [],
        "Axe de la Prospérité (Finances/Projets)": [],
        "Axe de la Vérité (Verdict/Esprit)": [],
        "Axe du Quotidien (Épreuves/Surmontable)": []
    }
    
    # Remplissage de l'Axe de la Prospérité
    if t.get("M2") == "Acquisitio": 
        analyse_structuree["Axe de la Prospérité (Finances/Projets)"].append("💰 La source de gain est active (Acquisitio).")
    
    # Règle sur l'Axe de la Vérité
    if t.get("M14") == "Albus": 
        analyse_structuree["Axe de la Vérité (Verdict/Esprit)"].append("🙏 Dévotion forte : La prière compense les finances basses.")
        
    # Règle sur l'Axe des Épreuves 
    if t.get("M15") == "Populus": 
        analyse_structuree["Axe du Quotidien (Épreuves/Surmontable)"].append("⚖️ Difficultés présentes mais surmontables par l'effort.")

    # Règle sur l'Axe Relationnel 
    if "Rubeus" in [t.get("M7"), t.get("M16")]: 
        analyse_structuree["Axe de la Manifestation (Objectifs/Partenaires)"].append("👁️ Risque de jalousie ou trahison d'un partenaire.")
        
    return analyse_structuree

def sauvegarder_tirage(nom, tirage_dict):
    conn = sqlite3.connect('geomancie.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO historique (nom_consultant, tirage) VALUES (?, ?)", (nom, str(tirage_dict)))
    conn.commit()
    conn.close()
