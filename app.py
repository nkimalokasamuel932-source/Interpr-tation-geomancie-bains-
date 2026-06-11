import streamlit as st
from collections import defaultdict

# Configuration de la page
st.set_page_config(page_title="Théurgie & Géomancie Sacrée", page_icon="🔮", layout="wide")

# ==============================================================================
# ACCÈS SÉCURISÉS
# ==============================================================================
ID_SECRET = "theurge2026"
MDP_SECRET = "Salomon777"

# ==============================================================================
# MATRICE SACRÉE DE RÉFÉRENCE POUR L'INTERPRÉTATION AUTOMATIQUE
# ==============================================================================
DATA = {
    "Youssouf (Dianfa Almami)": {
        "ref": "Youssouf (Dianfa Almami)", "nature": "Bénéfique", "element": "Feu", "direction": "Est",
        "txt": "Maison du demandeur par extension l'esprit, l'âme.",
        "psaume": "Psaume 20", "verset": "Verset 5", "texte_biblique": "Qu'il te donne ce que ton cœur désire, et qu'il accomplisse tous tes desseins !",
        "huile": "Laurier Noble (Victoire et clarté spirituelle)", 
        "aromatiques": "Feuilles de Laurier sauce, Menthe poivrée fraîche",
        "zikr": "Ya Wahhab (Ô Donateur Suprême) — 14 fois",
        "mots_application": "Que mon âme soit purifiée et que les intentions de ce thème reçoivent la clarté et le succès divin. Amen.", "moment": "Matin au lever"
    },
    "Adam (Adama)": {
        "ref": "Adam (Adama)", "nature": "Bénéfique", "element": "Feu", "direction": "Est",
        "txt": "Maison des biens, des chances, des énergies positives et négatives.",
        "psaume": "Psaume 8", "verset": "Verset 6", "texte_biblique": "Tu lui as donné l'empire sur les œuvres de tes mains, tu as tout mis sous ses pieds.",
        "huile": "Cèdre de l'Atlas (Ancrage et prospérité royale)", 
        "aromatiques": "Basilic sacré (Tulsi), Romarin officinal",
        "zikr": "Ya Rafi'u (Ô Celui qui élève) — 351 fois",
        "mots_application": "Que l'abondance matérielle, la chance et l'élévation financière s'installent durablement dans ma vie. Amen.", "moment": "Matin"
    },
    "Mahdiou (Malejou)": {
        "ref": "Mahdiou (Malejou)", "nature": "Neutre", "element": "Vent", "direction": "Sud",
        "txt": "Maison de la famille, des voisins, des parents, des collègues, l'entourage proche.",
        "psaume": "Psaume 4", "verset": "Verset 7", "texte_biblique": "Fais lever sur nous la lumière de ta face, ô Éternel !",
        "huile": "Orange Douce (Harmonie et joie relationnelle)", 
        "aromatiques": "Zestes d'Orange douce, Menthe douce (Nanah), Coriandre",
        "zikr": "Ya Nour (Ô Lumière) — 256 fois",
        "mots_application": "Que la concorde et la paix illuminent mes relations avec mon entourage et ma famille. Amen.", "moment": "Matin"
    },
    "Idriss (Albayada)": {
        "ref": "Idriss (Albayada)", "nature": "Bénéfique", "element": "Eau", "direction": "Nord",
        "txt": "Maison du foyer, du pays, de l'autorité parentale.",
        "psaume": "Psaume 112", "verset": "Verset 3", "texte_biblique": "Il a dans sa maison bien-être et richesse, et sa justice subsiste à jamais.",
        "huile": "Patchouli (Attraction terrestre et matérialisation)", 
        "aromatiques": "Bâtons de Cannelle concassés, Clous de Girofle entiers",
        "zikr": "Ya Razzaq (Ô Pourvoyeur) — 308 fois",
        "mots_application": "Que la stabilité, le bien-être et la richesse s'ancrent au cœur de mon foyer. Amen.", "moment": "Matin"
    },
    "Ibrahim (Târiki)": {
        "ref": "Ibrahim (Târiki)", "nature": "Bénéfique", "element": "Eau", "direction": "Nord",
        "txt": "Maison des enfants et des nouvelles.",
        "psaume": "Psaume 100", "verset": "Verset 2", "texte_biblique": "Servez l'Éternel avec joie, venez avec allégresse en sa présence !",
        "huile": "Pamplemousse (Énergie positive et renouveau)", 
        "aromatiques": "Verveine odorante, Citronnelle en tiges",
        "zikr": "Ya Latif (Ô Doux) — 129 fois",
        "mots_application": "Que les nouvelles qui me parviennent apportent la joie, la réussite et l'allégresse. Amen.", "moment": "Matin"
    },
    "Issa (Ngansa)": {
        "ref": "Issa (Ngansa)", "nature": "Neutre à Mauvais", "element": "Eau", "direction": "Nord",
        "txt": "Maison de la maladie, de la chose accomplie, des esclaves, du cheptel.",
        "psaume": "Psaume 51", "verset": "Verset 12", "texte_biblique": "Ô Dieu ! crée en moi un cœur pur, renouvelle en moi un esprit bien disposé.",
        "huile": "Lavande Vraie (Purification absolue des corps subtils)", 
        "aromatiques": "Fleurs de Lavande séchées, Camomille matricaire",
        "zikr": "Ya Chafi (Ô Guérisseur) — 391 fois",
        "mots_application": "Purifie mon être de toute négativité, entrave ou influence maladive cachée. Amen.", "moment": "Soir"
    },
    "Oumar (Lomara)": {
        "ref": "Oumar (Lomara)", "nature": "Mauvais", "element": "Vent", "direction": "Sud",
        "txt": "Maison des adversaires, du mariage, des époux.",
        "psaume": "Psaume 35", "verset": "Verset 1", "texte_biblique": "Éternel ! Attaque ceux qui m'attaquent, combats ceux qui me combattent !",
        "huile": "Cannelle Écorce (Feu purificateur de combat)", 
        "aromatiques": "Poivre noir en grains, Thym fort, Ortie piquante",
        "zikr": "Ya Jabbar (Ô Contraignant) — 206 fois",
        "mots_application": "Que toute opposition, conflit ou rivalité se brise face à la justice divine. Amen.", "moment": "Soir (Ne pas s'essuyer)"
    },
    "Ayoube (Mankoussi)": {
        "ref": "Ayoube (Mankoussi)", "nature": "Mauvais", "element": "Terre", "direction": "Ouest",
        "txt": "Maison de la mort, de l'angoisse, du malheur, de la peur, de la contrainte.",
        "psaume": "Psaume 142", "verset": "Verset 8", "texte_biblique": "Tire mon âme de sa prison, afin que je célèbre ton nom !",
        "huile": "Cyprès de Provence (Libération et passage des blocages)", 
        "aromatiques": "Sauge officinale, Racine de Gingembre frais râpé",
        "zikr": "Ya Moukhrij (Ô Celui qui fait sortir) — 201 fois",
        "mots_application": "Je me libère des angoisses, des blocages et de toute forme d'enfermement matériel ou spirituel. Amen.", "moment": "Soir"
    },
    "Allahou talla (Kalalaw)": {
        "ref": "Allahou talla (Kalalaw)", "nature": "Bénéfique", "element": "Feu", "direction": "Est",
        "txt": "Maison des déplacements, des voyages, de la mobilité, du dynamisme.",
        "psaume": "Psaume 133", "verset": "Verset 1", "texte_biblique": "Voici, qu'il est agréable, qu'il est doux pour des frères de demeurer ensemble !",
        "huile": "Ylang-Ylang (Attraction, charisme et union)", 
        "aromatiques": "Pétales de Rose de Damas, Anis étoilé (Badiane)",
        "zikr": "Ya Wadoud (Ô Aimant) — 20 fois",
        "mots_application": "Que mes routes et mes déplacements créent des alliances heureuses et fructueuses. Amen.", "moment": "Matin"
    },
    "Souleymane (Mansa Solomani)": {
        "ref": "Souleymane (Mansa Solomani)", "nature": "Bénéfique", "element": "Terre", "direction": "Ouest",
        "txt": "Maison du service, lieu de travail, maison de la royauté, de l'autorité.",
        "psaume": "Psaume 45", "verset": "Verset 2", "texte_biblique": "Des paroles pleines de charme bouillonnent dans mon cœur. Je dis : Mon œuvre est pour le roi !",
        "huile": "Géranium Bourbon (Magnétisme professionnel et éclat)", 
        "aromatiques": "Feuilles de Géranium odorant, Marjolaine à coquilles",
        "zikr": "Ya Jamil (Ô Beau) — 83 fois",
        "mots_application": "Accorde-moi le charisme, le respect et l'autorité morale nécessaires dans mes entreprises et mon travail. Amen.", "moment": "Matin"
    },
    "Ali (Badara Aliou)": {
        "ref": "Ali (Badara Aliou)", "nature": "Bénéfique", "element": "Vent", "direction": "Sud",
        "txt": "Maison des espoirs, de la protection, de la chose espérée, des envies.",
        "psaume": "Psaume 144", "verset": "Verset 1", "texte_biblique": "Béni soit l'Éternel, mon rocher, qui exerce mes mains au combat, mes doigts à la bataille !",
        "huile": "Gingembre Bleu (Force, dynamisme et courage)", 
        "aromatiques": "Graines de Cardamome, Menthe des champs",
        "zikr": "Ya Qawiyyou (Ô Fort Invincible) — 116 fois",
        "mots_application": "Que mes espérances les plus profondes soient fortifiées et protégées contre tout obstacle. Amen.", "moment": "Matin"
    },
    "Nouhou (Nounkoro)": {
        "ref": "Nouhou (Nounkoro)", "nature": "Mauvais", "element": "Terre", "direction": "Ouest",
        "txt": "Maison des difficultés, des problèmes, maison ennemis, des obstacles, des entraves.",
        "psaume": "Psaume 30", "verset": "Verset 12", "texte_biblique": "Tu as changé mon deuil en allégresse, tu as délié mon sac, et tu m'as ceint de joie.",
        "huile": "Citronnelle Java (Nettoyage des ondes lourdes)", 
        "aromatiques": "Tiges de Citronnelle fraîches, Thym blanc, Estragon",
        "zikr": "Ya Latif (Ô Bienveillant) — 129 fois",
        "mots_application": "Que tous les pièges de l'ombre soient déracinés et dissous, laissant place au triomphe. Amen.", "moment": "Soir"
    },
    "Houssaini (Ioussiné)": {
        "ref": "Houssaini (Ioussiné)", "nature": "Neutre", "element": "Eau", "direction": "Nord",
        "txt": "Maison de la situation présente, des informations diverses, du dortoir, informations dans la chambre.",
        "psaume": "Psaume 18", "verset": "Verset 38", "texte_biblique": "Je les brise, et ils ne peuvent se relever ; ils tombent sous mes pieds.",
        "huile": "Clou de Girofle (Scellage et protection du lieu)", 
        "aromatiques": "Feuilles d'Eucalyptus globulus, Clous de girofle",
        "zikr": "Ya Moumit (Ô Maître de la libération) — 490 fois",
        "mots_application": "Que ma situation actuelle soit clarifiée, purifiée et libérée des énergies stagnantes. Amen.", "moment": "Soir"
    },
    "Younouss (Tontigui)": {
        "ref": "Younouss (Tontigui)", "nature": "Bénéfique", "element": "Terre", "direction": "Ouest",
        "txt": "Maison de la richesse, de l'argent, maison qui décrit la situation à venir, ce qui n'est pas encore accompli.",
        "psaume": "Psaume 91", "verset": "Verset 11", "texte_biblique": "Car il ordonnera à ses anges de te garder dans toutes tes voies.",
        "huile": "Arbre à Thé / Tea Tree (Bouclier défensif financier)", 
        "aromatiques": "Laurier noble séché, Coriandre en graines",
        "zikr": "Ya Hafiz (Ô Protecteur Suprême) — 998 fois",
        "mots_application": "Que la prospérité future promise par ce thème soit scellée et divinement protégée. Amen.", "moment": "Matin"
    },
    "Ousmane (Mori Zoumana)": {
        "ref": "Ousmane (Mori Zoumana)", "nature": "Bénéfique", "element": "Vent", "direction": "Sud",
        "txt": "La conclusion du thème, l'environnement, la situation générale, le résumé du thème.",
        "psaume": "Psaume 119", "verset": "Verset 105", "texte_biblique": "Ta parole est une lampe à mes pieds, et une lumière sur mon sentier.",
        "huile": "Encens d'Oliban (Haute connexion divine et conclusion céleste)", 
        "aromatiques": "Résine pure d'Oliban, Fleurs de Jasmin",
        "zikr": "Ya Alim (Ô Omniscient) — 150 fois",
        "mots_application": "Que la lumière parfaite éclaire la conclusion de mes démarches et m'apporte la réussite globale. Amen.", "moment": "Soir"
    },
    "Moussa (Moussa)": {
        "ref": "Moussa (Moussa)", "nature": "Neutre à Fort", "element": "Feu", "direction": "Est",
        "txt": "La précision, la confirmation, le décret final.",
        "psaume": "Psaume 4", "verset": "Verset 7", "texte_biblique": "Fais lever sur nous la lumière de ta face, ô Éternel !",
        "huile": "Orange Douce (Rapidité et scellage solaire)", 
        "aromatiques": "Zestes de Citron vert, Menthe poivrée, Cannelle",
        "zikr": "Ya Sari'u (Ô Rapidie) — 202 fois",
        "mots_application": "Que le décret final de cette consultation s'exécute en ma faveur avec force et rapidité. Amen.", "moment": "Matin"
    }
}

MAISONS_NOMINATIVES = {
    1: "Maison 1 (Demandeur / Âme)", 2: "Maison 2 (Biens / Chances)", 3: "Maison 3 (Famille / Entourage)", 4: "Maison 4 (Foyer / Patrimoine)",
    5: "Maison 5 (Enfants / Nouvelles)", 6: "Maison 6 (Maladie / Entraves)", 7: "Maison 7 (Adversaires / Époux)", 8: "Maison 8 (Mort / Peurs)",
    9: "Maison 9 (Voyages / Déplacements)", 10: "Maison 10 (Service / Autorité)", 11: "Maison 11 (Espoirs / Protection)", 12: "Maison 12 (Difficultés / Ennemis)",
    13: "Maison 13 (Situation présente / Chambre)", 14: "Maison 14 (Richesse future)", 15: "Maison 15 (Conclusion générale)", 16: "Maison 16 (Précision / Confirmation)"
}

# ==============================================================================
# INTERFACE INTERACTIVE
# ==============================================================================
st.title("🔮 Grimoire Géomantique & Moteur de Passation des Figures")
st.write("Analyse théurgique avancée avec détection automatique des répétitions (doubles, triples ou plus).")

with st.sidebar:
    st.header("🔐 Connexion Sacrée")
    u_id = st.text_input("Identifiant")
    u_pw = st.text_input("Mot de passe", type="password")

if u_id == ID_SECRET and u_pw == MDP_SECRET:
    st.success("🔓 Système connecté. Analyseur de passation actif.")
    
    st.header("📋 ENTRÉE DU THÈME GÉOMANTIQUE")
    st.info("Modifiez l'emplacement des figures. Le moteur calculera automatiquement les liens secrets créés par les répétitions.")
    
    col1, col2, col3, col4 = st.columns(4)
    options_figures = list(DATA.keys())
    
    # Configuration par défaut
    theme_initial = [
        "Youssouf (Dianfa Almami)", "Adam (Adama)", "Mahdiou (Malejou)", "Idriss (Albayada)",
        "Ibrahim (Târiki)", "Issa (Ngansa)", "Oumar (Lomara)", "Ayoube (Mankoussi)",
        "Allahou talla (Kalalaw)", "Souleymane (Mansa Solomani)", "Ali (Badara Aliou)", "Nouhou (Nounkoro)",
        "Houssaini (Ioussiné)", "Younouss (Tontigui)", "Ousmane (Mori Zoumana)", "Moussa (Moussa)"
    ]

    choix_theurge = {}
    for maison_id in range(1, 16):  # M1 à M15 sont saisies
        groupe_col = [col1, col2, col3, col4][(maison_id - 1) % 4]
        with groupe_col:
            choix_theurge[maison_id] = st.selectbox(
                f"🏠 {MAISONS_NOMINATIVES[maison_id]}", 
                options_figures, 
                index=options_figures.index(theme_initial[maison_id - 1])
            )
            
    # M16 (Le Décret) s'ajoute à la suite
    with col4:
        choix_theurge[16] = st.selectbox(
            f"🏠 {MAISONS_NOMINATIVES[16]}", 
            options_figures, 
            index=options_figures.index(theme_initial[15])
        )

    # ==============================================================================
    # ANALYSE ET MOTEUR DE PASSATION AUTOMATIQUE
    # ==============================================================================
    st.markdown("---")
    st.header("🔄 ESPACE D'INTERPRÉTATION DES PASSATIONS (Information Capitale)")
    
    # Cartographier l'emplacement de chaque figure dans le thème actuel
    repartitions = defaultdict(list)
    for maison, fig in choix_theurge.items():
        repartitions[fig].append(maison)
        
    # Filtrer uniquement les figures qui se répètent (Passations)
    passations = {fig: maisons for fig, maisons in repartitions.items() if len(maisons) > 1}
    
    if passations:
        st.warning(f"⚠️ Le système a détecté {len(passations)} figure(s) en état de passation (répétition). Voici les flux de forces générés :")
        
        for fig, maisons in passations.items():
            nb_rep = len(maisons)
            statut = "DOUBLE" if nb_rep == 2 else "TRIPLE" if nb_rep == 3 else f"RÉPÉTÉE {nb_rep} FOIS"
            
            # Formatage de la liste des maisons sous forme textuelle propre
            maisons_txt = " ➔ ".join([f"Maison {m}" for m in maisons])
            
            with st.container(border=True):
                st.markdown(f"### 🔀 **{fig}** en **{statut}**")
                st.markdown(f"**Chemin du courant énergétique :** `{maisons_txt}`")
                
                # Génération dynamique de l'analyse secrète selon le contexte des maisons traversées
                m_prem = maisons[0]
                m_dern = maisons[-1]
                
                st.markdown(f"**💡 Révélation Théurgique de la Passation :**")
                st.write(f"La force de la figure *{fig}* prend racine dans la **{MAISONS_NOMINATIVES[m_prem]}** et vient projeter son résultat, ses blocages ou ses gains de manière irréversible dans la **{MAISONS_NOMINATIVES[m_dern]}**.")
                
                # Conseil de traitement théurgique cumulé
                st.info(f"👉 **Recommandation du Maître :** Pour débloquer ou sceller ce flux de passation, vous devez impérativement combiner l'aromatique des deux maisons extrêmes dans le même bain et réciter les Mots d'Application des maisons traversées.")
    else:
        st.success("✅ Aucune passation détectée. Les énergies de ce thème sont stables et assignées de façon unique à chaque secteur de vie.")

    # ==============================================================================
    # CODES THÉURGIQUES RESTRUCTURÉS DES 16 MAISONS
    # ==============================================================================
    st.markdown("---")
    st.header("📖 ANALYSE ET COMPOSITIONS MAISON PAR MAISON")
    
    for m, fig_choisie in choix_theurge.items():
        bloc = DATA[fig_choisie]
        
        if "Mauvais" in bloc["nature"]:
            entete_style = f"🛑 {MAISONS_NOMINATIVES[m]} ➔ {fig_choisie} [PURIFICATION]"
        else:
            entete_style = f"✨ {MAISONS_NOMINATIVES[m]} ➔ {fig_choisie} [OUVERTURE]"
            
        with st.expander(entete_style):
            t1, t2, t3 = st.tabs(["📊 Diagnostic du Verbe", "🌿 Recette Aromatique & Psaumes", "📿 Clé du Zikr"])
            
            with t1:
                st.markdown(f"**Figure active :** {bloc['ref']}")
                st.markdown(f"**Courant occulte :** `{bloc['nature'].upper()}`")
                st.markdown(f"**Élément & Orientation :** {bloc['element']} | {bloc['direction']}")
                st.markdown(f"**Interprétation (txt) :** *{bloc['txt']}*")
                
            with t2:
                st.markdown("### 🧪 Éléments du Bain Sacré")
                st.markdown(f"🌱 **Plantes Aromatiques :** `{bloc['aromatiques']}`")
                st.markdown(f"💧 **Huile Essentielle :** *{bloc['huile']}*")
                st.markdown(f"⏰ **Heure d'application :** `{bloc['moment']}`")
                st.markdown("---")
                st.markdown("### ✒️ Psaumes & Versets Bibliques pour le Nassi")
                st.info(f"📜 **Référence d'Écriture :** {bloc['psaume']} ({bloc['verset']})")
                st.write(f"👉 *\"{bloc['texte_biblique']}\"*")
                
            with t3:
                st.markdown("### 📿 Activation Spirituelle")
                st.warning(f"**Zikr Numérique :** {bloc['zikr']}")
                st.markdown("### 🗣️ Formulation / Mots d'Application :")
                st.success(f"\"{bloc['mots_application']}\"")
else:
    st.warning("🔒 Renseignez vos identifiants dans le panneau latéral pour charger votre laboratoire mystique.")
