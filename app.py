import streamlit as st

# ==============================================================================
# BASE DE DONNÉES MAÎTRE ENTIÈREMENT RESTAURÉE (16 FIGURES)
# ==============================================================================
DB = {
    "Youssouf": {
        "element": "Feu (Est)", 
        "psaume": "Psaume 109", 
        "verset": "Genèse 39:2", 
        "priere": "Seigneur, Dieu de Joseph, par Ton Nom Adonaï, je Te supplie de dissiper les ténèbres de la calomnie. Comme Tu as transformé la captivité de Joseph en gloire, restaure mon honneur.", 
        "nassi": "Écrire 111 fois, laver avec eau de puits, safran et parfum de rose. Bain pendant 7 jours.", 
        "plantes": "Laurier, Cannelle", 
        "huiles": "Encens (Oliban), Clou de girofle, Orange", 
        "heure": "Mardi, Heure de Mars (Aube)", 
        "support": "Papier parchemin, Encre Safran", 
        "couleur": "Rouge", 
        "cloture": "Psaume 117", 
        "sadaka": "Mardi (Pain, dattes, denrées chaudes)"
    },
    "Adama": {
        "element": "Feu (Est)", 
        "psaume": "Psaume 121", 
        "verset": "Genèse 2:7", 
        "priere": "Par le Nom Elohim, Créateur du premier homme, j'invoque l'ancrage de mes racines dans la terre fertile. Que mes biens soient protégés et multipliés.", 
        "nassi": "Tracer 45 fois sur ardoise. Eau + gros sel béni. Aspersion du corps et du seuil.", 
        "plantes": "Gingembre, Laurier, Cannelle", 
        "huiles": "Orange douce, Clou de girofle, Encens", 
        "heure": "Samedi, Heure de Saturne (Soir)", 
        "support": "Ardoise, Craie blanche", 
        "couleur": "Vert/Noir", 
        "cloture": "Psaume 128", 
        "sadaka": "Mardi (Denrées rouges)"
    },
    "Mahdy": {
        "element": "Air (Ouest)", 
        "psaume": "Psaume 23", 
        "verset": "Jérémie 29:11", 
        "priere": "Par le Nom El-Shaddaï, Source de toute subsistance, débouche les canaux de l'abondance. Que Ta faveur attire les ressources.", 
        "nassi": "Écrire 66 fois avec eau de rose et musc. Boire chaque matin à jeun.", 
        "plantes": "Menthe, Sauge, Eucalyptus", 
        "huiles": "Citron, Menthe poivrée, Bergamote", 
        "heure": "Mercredi, Heure de Mercure (Midi)", 
        "support": "Papier blanc, Encre noire", 
        "couleur": "Jaune", 
        "cloture": "Psaume 150", 
        "sadaka": "Jeudi (Sucre et lait)"
    },
    "Idriss": {
        "element": "Eau (Nord)", 
        "psaume": "Psaume 119:9-16", 
        "verset": "Hébreux 11:5", 
        "priere": "Par le Nom El-Choura, Dieu de Sagesse, accorde-moi le discernement pour lire à travers les mystères.", 
        "nassi": "Écrire 360 fois. Diluer dans de l'eau de pluie. Oindre la tête avant l'étude.", 
        "plantes": "Aloès, Neem, Verveine", 
        "huiles": "Lavande, Camomille, Ylang-Ylang", 
        "heure": "Lundi, Heure de la Lune (Aube)", 
        "support": "Feuille d'arbre, Encre bleue", 
        "couleur": "Bleu", 
        "cloture": "Psaume 23", 
        "sadaka": "Lundi (Eau pure)"
    },
    "Ibrahima": {
        "element": "Eau (Nord)", 
        "psaume": "Psaume 112", 
        "verset": "Genèse 12:2", 
        "priere": "Par le Nom El-Elyon, je scelle la protection de ma lignée. Que Ta bénédiction s'étende sur ma maison.", 
        "nassi": "Écrire 72 fois. Infuser avec de la menthe fraîche. Boire ou en asperger la chambre.", 
        "plantes": "Verveine, Neem, Aloès", 
        "huiles": "Camomille, Lavande, Ylang-Ylang", 
        "heure": "Jeudi, Heure de Jupiter (Aube)", 
        "support": "Papier, Encre Noire", 
        "couleur": "Blanc", 
        "cloture": "Psaume 112", 
        "sadaka": "Jeudi (Lait)"
    },
    "Inssa": {
        "element": "Eau (Nord)", 
        "psaume": "Psaume 6", 
        "verset": "Ésaïe 53:5", 
        "priere": "Par le Nom Rapha, Dieu qui guérit, efface la maladie et restaure la vigueur de mon esprit.", 
        "nassi": "Écrire 99 fois à l'encre Sami. Laver le corps avec une décoction de feuilles de neem.", 
        "plantes": "Neem, Verveine, Aloès", 
        "huiles": "Ylang-Ylang, Lavande, Camomille", 
        "heure": "Lundi, Heure de la Lune (Nuit)", 
        "support": "Ardoise", 
        "couleur": "Bleu pâle", 
        "cloture": "Psaume 6", 
        "sadaka": "Lundi (Aumône aux malades et nécessiteux)"
    },
    "Omar": {
        "element": "Air (Ouest)", 
        "psaume": "Psaume 35", 
        "verset": "Proverbes 31:10", 
        "priere": "Par le Nom Shalom, j'invoque l'harmonie. Que les discordes soient neutralisées et les intrigues dissoutes.", 
        "nassi": "Tracer 28 fois. Eau de source + 7 gouttes de parfum sans alcool. Aspersion de la maison.", 
        "plantes": "Sauge, Menthe, Eucalyptus", 
        "huiles": "Menthe poivrée, Citron, Bergamote", 
        "heure": "Mercredi, Heure de Mercure (Coucher)", 
        "support": "Parchemin", 
        "couleur": "Gris", 
        "cloture": "Psaume 35", 
        "sadaka": "Jeudi (Sucre)"
    },
    "Ayoub": {
        "element": "Terre (Sud)", 
        "psaume": "Psaume 88", 
        "verset": "Job 19:25", 
        "priere": "Par le Nom Yahvé, demande la restauration. Que la patience soit ma force face à la ruine.", 
        "nassi": "Écrire 88 fois. Dissoudre dans de l'eau tiède et du miel. Se laver un samedi soir.", 
        "plantes": "Santal, Patchouli, Cèdre", 
        "huiles": "Vétiver, Santal, Cèdre", 
        "heure": "Samedi, Heure de Saturne (Nuit)", 
        "support": "Terre cuite", 
        "couleur": "Marron", 
        "cloture": "Psaume 88", 
        "sadaka": "Samedi (Pièces de monnaie, céréales)"
    },
    "Allahou": {
        "element": "Feu (Est)", 
        "psaume": "Psaume 91", 
        "verset": "Exode 20:2", 
        "priere": "Par le Nom El-Qahhar, sois ma Forteresse. Que chaque sortilège soit annulé par Ta Protection.", 
        "nassi": "Écrire 114 fois. Eau de puits. Boire le vendredi, purifier le commerce.", 
        "plantes": "Laurier, Cannelle, Gingembre", 
        "huiles": "Clou de girofle, Encens (Oliban), Orange", 
        "heure": "Mardi, Heure de Mars (Midi)", 
        "support": "Papier/Encre Safran", 
        "couleur": "Rouge vif", 
        "cloture": "Psaume 91", 
        "sadaka": "Mardi (Pain)"
    },
    "Souleymane": {
        "element": "Terre (Sud)", 
        "psaume": "Psaume 72", 
        "verset": "1 Rois 3:12", 
        "priere": "Par le Nom Malek, Roi des Rois, accorde-moi l'autorité pour diriger mes affaires avec justice.", 
        "nassi": "Écrire 110 fois. Eau infusée au santal. Oindre les mains et le visage avant les affaires.", 
        "plantes": "Patchouli, Santal, Cèdre", 
        "huiles": "Santal, Vétiver, Cèdre", 
        "heure": "Samedi, Heure de Saturne (Aube)", 
        "support": "Parchemin", 
        "couleur": "Or", 
        "cloture": "Psaume 72", 
        "sadaka": "Samedi (Pièces)"
    },
    "Aliou": {
        "element": "Air (Ouest)", 
        "psaume": "Psaume 144", 
        "verset": "Éphésiens 6:11", 
        "priere": "Par le Nom Tsébaot, revêts-moi de Ton Armure. Sois mon bouclier contre toute agression.", 
        "nassi": "Écrire 63 fois. Eau + camphre. Se laver un mardi.", 
        "plantes": "Eucalyptus, Menthe, Sauge", 
        "huiles": "Bergamote, Menthe poivrée, Citron", 
        "heure": "Mercredi, Heure de Mercure (Aube)", 
        "support": "Papier blanc", 
        "couleur": "Violet", 
        "cloture": "Psaume 144", 
        "sadaka": "Jeudi (Eau sucrée)"
    },
    "Nouhou": {
        "element": "Terre (Sud)", 
        "psaume": "Psaume 29", 
        "verset": "Genèse 6:8", 
        "priere": "Par le Nom El-Hafiz, demande à être préservé au milieu de la tempête. Que Ta Grâce soit mon arche.", 
        "nassi": "Écrire 77 fois. Eau de mer ou sel marin. Laver le sol de la concession.", 
        "plantes": "Cèdre, Santal, Patchouli", 
        "huiles": "Cèdre, Santal, Vétiver", 
        "heure": "Samedi, Heure de Saturne (Minuit)", 
        "support": "Ardoise", 
        "couleur": "Noir", 
        "cloture": "Psaume 29", 
        "sadaka": "Samedi (Céréales)"
    },
    "Assane": {
        "element": "Eau (Nord)", 
        "psaume": "Psaume 3", 
        "verset": "Psaume 3:3", 
        "priere": "Par le Nom El-Adl, demande le retournement de mon sort. Que la honte soit transmutée en honneur.", 
        "nassi": "Écrire 55 fois (encre safranée). Eau + laurier. Bain 3 jours.", 
        "plantes": "Neem, Verveine, Aloès", 
        "huiles": "Lavande, Camomille, Ylang-Ylang", 
        "heure": "Lundi, Heure de la Lune (Midi)", 
        "support": "Papier/Encre Safran", 
        "couleur": "Bleu", 
        "cloture": "Psaume 3", 
        "sadaka": "Lundi (Lait)"
    },
    "Younouss": {
        "element": "Terre (Sud)", 
        "psaume": "Psaume 4", 
        "verset": "Jonas 2:10", 
        "priere": "Par le Nom El-Latif, libère-moi des chaînes de la dette. Fais sortir mes finances de toute impasse.", 
        "nassi": "Écrire 40 fois. Eau + pièce d'argent trempée. Friction sur les mains.", 
        "plantes": "Santal, Patchouli, Cèdre", 
        "huiles": "Vétiver, Santal, Cèdre", 
        "heure": "Samedi, Heure de Saturne (Aube)", 
        "support": "Parchemin", 
        "couleur": "Vert", 
        "cloture": "Psaume 4", 
        "sadaka": "Samedi (Pièces)"
    },
    "Ousmane": {
        "element": "Air (Ouest)", 
        "psaume": "Psaume 119:105", 
        "verset": "Actes 2:4", 
        "priere": "Par le Nom El-Rouah, Esprit de Vérité, guide mes pas dans la lumière de la haute guidance.", 
        "nassi": "Écrire 19 fois. Infuser avec encens Oliban. Boire avant consultation.", 
        "plantes": "Sauge, Menthe, Eucalyptus", 
        "huiles": "Citron, Menthe poivrée, Bergamote", 
        "heure": "Mercredi, Heure de Mercure (Nuit)", 
        "support": "Feuille", 
        "couleur": "Bleu ciel", 
        "cloture": "Psaume 119", 
        "sadaka": "Jeudi (Sucre)"
    },
    "Moussa": {
        "element": "Feu (Est)", 
        "psaume": "Psaume 68", 
        "verset": "Exode 14:13", 
        "priere": "Par le Nom El-Fattah, demande le passage. Ouvre devant moi les chemins du succès.", 
        "nassi": "Écrire 16 fois. Eau de source de l'aube. Nettoyer le seuil ou grand bain.", 
        "plantes": "Cannelle, Laurier, Gingembre", 
        "huiles": "Encens (Oliban), Clou de girofle, Orange", 
        "heure": "Mardi, Heure de Mars (Midi)", 
        "support": "Papier/Encre Safran", 
        "couleur": "Rouge", 
        "cloture": "Psaume 68", 
        "sadaka": "Mardi (Denrées, dattes)"
    }
}
# Invocations
INV_OUVERTURE = "Toi seul, ô Dieu de Salomon, règnes sur ce qui est visible et sur ce qui ne l'est pas. Je me présente devant Toi, non comme un étranger, mais comme un héritier de Ton Alliance."
ANA_BEKOACH = """ANA BEKOACH (Clé des 42 Lettres) :
1. Ana bekoach, gedoulat yemincha, tatir tsourourah
2. Kabel rinat, amcha saguenu, tahareinou nora
3. Na guibor, dorshei yichoudcha, kevavat chomrem
4. Barchem taharem, rachamei tsidkat’cha, tamid gamlem
5. Chasin kadoch, berov touvcha, nahel adatecha
6. Yachid ge-e, le-amcha peneh, zochrei kedouchatecha
7. Chav’aténou kabel, ouchma tsa-akaténou, yodei-a ta-aloumout"""
INV_FERMETURE = "Lève-Toi, Seigneur Dieu, pour aller à Ton lieu de repos. Que Tes serviteurs soient revêtus du salut. Que cette prière soit scellée."
# Interface
st.set_page_config(page_title="Oracle Ramrou", layout="wide")
st.title("🔮 Oracle Ramrou — Cabinet de Haute Théurgie")
st.markdown(f"> *{INV_OUVERTURE}*")
st.divider()
st.sidebar.header("📋 Saisie des 16 Maisons")
question = st.sidebar.text_area("Question posée :")
theme_actuel = {m: st.sidebar.selectbox(f"Maison M{m}", list(DB.keys()), key=f"m{m}") for m in range(1, 17)}
st.sidebar.header("📋 Saisie des 16 Maisons")
question = st.sidebar.text_area("Question posée :")
theme_actuel = {m: st.sidebar.selectbox(f"Maison M{m}", list(DB.keys()), key=f"m{m}") for m in range(1, 17)}

if st.button("🔮 GÉNÉRER L'ORDONNANCE"):
    juge = theme_actuel[16]
    d = DB[juge]
    
    st.subheader(f"⚖️ Verdict du Juge : {juge} ({d['element']})")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"**Psaume :** {d['psaume']}\n**Prière :** {d['priere']}")
        st.warning(f"**Clé Ana Bekoach (Méditation) :**\n{ANA_BEKOACH}")
    with c2:
        st.markdown(f"**Protocole :** {d['nassi']}\n**Sadaka :** {d['sadaka']}")
    
    export = f"{INV_OUVERTURE}\n\n{ANA_BEKOACH}\n\nORDONNANCE POUR {juge.upper()}\n{d}\n\n{INV_FERMETURE}"
    st.download_button("📥 Télécharger l'Ordonnance", data=export, file_name=f"Ordonnance_{juge}.txt")

# Invocations textuelles fixes
INV_OUVERTURE = "Toi seul, ô Dieu de Salomon, règnes sur ce qui est visible et sur ce qui ne l'est pas. Je me présente devant Toi, non comme un étranger, mais comme un héritier de Ton Alliance. Que Ta Sagesse guide cette consultation."
INV_FERMETURE = "Lève-Toi, Seigneur Dieu, pour aller à Ton lieu de repos. Que Tes serviteurs soient revêtus du salut. Que cette prière soit scellée."

# ==============================================================================
# CONFIGURATION DE L'INTERFACE STREAMLIT
# ==============================================================================
st.set_page_config(page_title="Oracle Ramrou", layout="wide")

st.title("🔮 Oracle Ramrou — Cabinet de Haute Théurgie")

# Affichage permanent de la prière d'ouverture en haut
st.markdown(f"""
> *« {INV_OUVERTURE} »*
""")
st.divider()

# Barre latérale pour la saisie de l'ensemble du thème (16 Maisons disposées)
st.sidebar.header("📋 Saisie des 16 Maisons")
question = st.sidebar.text_area("Question posée :", placeholder="Écrivez le contexte ici...")
intention = st.sidebar.selectbox("Intention principale :", ["Déblocage", "Protection", "Attraction", "Apaisement"])

# Création dynamique des 16 sélecteurs pour les 16 Maisons de la géomancie
theme_actuel = {}
for m in range(1, 17):
    theme_actuel[m] = st.sidebar.selectbox(f"Maison M{m}", list(DB.keys()), index=0, key=f"maison_{m}")

# Bouton d'action principal
if st.button("🔮 GÉNÉRER L'ORDONNANCE DE RÉSOLUTION"):
    # Récupération de la décision via le Juge (Maison 16)
    juge = theme_actuel[16]
    d = DB[juge]
    
    st.subheader(f"⚖️ Verdict du Juge (M16) : {juge} — Élément : {d['element']}")
    if question:
        st.info(f"💡 **Contexte de la consultation :** {question} | **Intention :** {intention}")
        
    st.divider()
    
    # Répartition propre des blocs de l'ordonnance en 2 colonnes
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### 📜 Ordonnance Théurgique & Sacrée")
        st.markdown(f"**📖 Psaume assigné :** {d['psaume']}")
        st.markdown(f"**📜 Verset (Nassi) :** {d['verset']}")
        st.warning(f"**🙏 Prière Salomonique d'appel :**\n\n> *{d['priere']}*")
        st.info(f"**🧪 Protocole d'écriture du Nassi :** {d['nassi']}")
        
    with col2:
        st.write("### 🌿 Supports Rituels & Alchimie")
        st.success(f"**🌿 Support Végétal (Plantes) :** {d['plantes']}")
        st.success(f"**💧 Essences Sacrées (Huiles) :** {d['huiles']}")
        st.write(f"**⏰ Alignement temporel :** {d['heure']}")
        st.write(f"**🎨 Matière & Support physique :** {d['support']} (Bougie {d['couleur']})")
        st.error(f"**⚡ Action de Clôture :** Recenser le {d['cloture']}")
        st.error(f"**🪙 Fixation matérielle (Sadaka) :** {d['sadaka']}")
        
    st.divider()
    
    # Affichage du Sceau Sacré de Clôture
    st.markdown(f"""
    ### 🔒 Sceau de Consécration
    > *« {INV_FERMETURE} »*
    """)
    st.markdown("✨ *Le rituel est fixé dans la matière. Que la Lumière agisse.*")
    
    # Construction de la chaîne de texte propre pour le fichier téléchargeable
    ordonnance_export = (
        f"🔮 ORACLE RAMROU — CABINET DE HAUTE THÉURGIE\n"
        f"==================================================\n\n"
        f"✨ PRIÈRE D'OUVERTURE :\n{INV_OUVERTURE}\n\n"
        f"--------------------------------------------------\n"
        f"⚖️ VERDICT DU JUGE (M16) : {juge.upper()} ({d['element']})\n"
        f"--------------------------------------------------\n"
        f"• Intention : {intention}\n"
        f"• Contexte : {question if question else 'Non renseigné'}\n\n"
        f"📜 INSTRUCTIONS THÉURGIQUES :\n"
        f"  - Psaume : {d['psaume']}\n"
        f"  - Verset : {d['verset']}\n"
        f"  - Prière Salomonique : {d['priere']}\n"
        f"  - Protocole Nassi : {d['nassi']}\n\n"
        f"🌿 SUPPORTS MATÉRIELS :\n"
        f"  - Plantes : {d['plantes']}\n"
        f"  - Huiles : {d['huiles']}\n"
        f"  - Heure et moment : {d['heure']}\n"
        f"  - Support et bougie : {d['support']} (Couleur {d['couleur']})\n\n"
        f"🪙 FIXATION ET SACRIFICE :\n"
        f"  - Clôture : Réciter le {d['cloture']}\n"
        f"  - Sadaka prescrite : {d['sadaka']}\n\n"
        f"==================================================\n"
        f"🔒 PRIÈRE DE FERMETURE (SCEAU) :\n{INV_FERMETURE}\n"
    )
    
    # Bouton de téléchargement du fichier texte
    st.download_button(
        label="📥 Télécharger l'Ordonnance Rituelle Complète",
        data=ordonnance_export,
        file_name=f"Ordonnance_Theurgique_{juge}.txt",
        mime="text/plain"
    )
