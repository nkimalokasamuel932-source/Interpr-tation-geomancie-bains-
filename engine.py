# engine.py

# Dictionnaire des significations des 16 Maisons
maisons_definitions = {
    "M1": "Consultant / Personnalité",
    "M2": "Finances / Biens",
    "M3": "Entourage / Communication",
    "M4": "Foyer / Racines",
    "M5": "Projets / Créativité",
    "M6": "Travail / Santé",
    "M7": "Partenaires / Contrats",
    "M8": "Influences extérieures / Dettes",
    "M9": "Savoir / Spiritualité",
    "M10": "Carrière / Statut",
    "M11": "Appuis / Espoirs",
    "M12": "Épreuves cachées",
    "M13": "Passé récent",
    "M14": "Futur proche",
    "M15": "Juge (Synthèse)",
    "M16": "Témoin final (Confirmation)"
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

def obtenir_analyse(tirage_figures):
    """Prend un dictionnaire {'M1': 'NomFigure'} et renvoie les interprétations."""
    resultats = {}
    for maison, figure in tirage_figures.items():
        if figure in figures_definitions:
            resultats[maison] = f"{maisons_definitions[maison]} -> {figure} : {figures_definitions[figure]}"
        else:
            resultats[maison] = f"{maisons_definitions[maison]} : Figure non reconnue"
    return resultats
