import sqlite3

# Dictionnaire des figures
noms_bambara = {
    "Laetitia": "Laya", "Tristitia": "Taratigué", "Fortuna Major": "Gouroussou",
    "Fortuna Minor": "Gouroussou-ni", "Acquisitio": "Ousmane", "Amissio": "Mangousi",
    "Caput Draconis": "Allassan", "Cauda Draconis": "Oussoufou", "Conjunctio": "Solomana",
    "Carcer": "Issa", "Puella": "Laoussana", "Puer": "Bara",
    "Albus": "Allahou-Talla", "Rubeus": "Djafal Almani", "Via": "Younouss", "Populus": "Ibrahim"
}

def init_db():
    conn = sqlite3.connect('geomancie.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS historique 
                      (id INTEGER PRIMARY KEY, nom_consultant TEXT, tirage TEXT, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def sauvegarder_tirage(nom, tirage_dict):
    conn = sqlite3.connect('geomancie.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO historique (nom_consultant, tirage) VALUES (?, ?)", (nom, str(tirage_dict)))
    conn.commit()
    conn.close()

def obtenir_analyse_par_axes(t):
    analyse = {
        "Axe Manifestation (Partenaires)": [],
        "Axe Prospérité (Finances)": [],
        "Axe Vérité (Prière)": [],
        "Axe Quotidien (Épreuves)": []
    }
    # Exemple d'intégration de vos règles
    if t.get("M7") == "Rubeus" or t.get("M16") == "Rubeus":
        analyse["Axe Manifestation (Partenaires)"].append("👁️ Risque de jalousie/trahison d'un partenaire.")
    if t.get("M14") == "Albus":
        analyse["Axe Vérité (Prière)"].append("🙏 Prière et dévotion forte malgré finances basses.")
    if t.get("M15") == "Populus":
        analyse["Axe Quotidien (Épreuves)"].append("⚖️ Difficultés surmontables par l'effort.")
    return analyse

def analyser_axes_specifiques(t):
    synthese = []
    # Règle Idriss-Issa-Allassan
    if t.get("M8") == "Idriss" and t.get("M4") == "Carcer":
        synthese.append("📬 Nouvelle extérieure concernant le patrimoine.")
        if t.get("M6") == "Caput Draconis":
            synthese.append("⚠️ Déception ou perte liée à cette nouvelle.")
    return synthese
