import streamlit as st

# 1. Configuration de la page de l'application
st.set_page_config(page_title="Oracle Géomantique", page_icon="🔮", layout="centered")

# =====================================================================
# DICTIONNAIRE COMPLET DES 16 FIGURES GÉOMANTIQUES
# =====================================================================
DICTIONNAIRE_FIGURES = {
    "1.1.1.1": {"nom": "Hibrahim (Via)", "signification": "Le Mouvement, la Route, l'Instabilité. Flux constants et déplacements nécessaires. Annonce privilégiée d'une naissance ou d'une grossesse.", "psaume": "Psaume 120", "saraka": "Partage de fruits ou de friandises à des enfants (Énergie du futur)."},
    "1.1.1.2": {"nom": "Laoussana (Puella)", "signification": "L'Hésitation, la Beauté, les Doubles pensées. Sensibilité, plaisirs, mais tiraillement face à des choix complexes.", "psaume": "Psaume 119", "saraka": "Donner du lait frais ou des objets blancs à des personnes de votre âge."},
    "1.2.1.1": {"nom": "Garia (Fortuna Major)", "signification": "La Grande Chance, la Protection, le Succès durable. Réussite totale, élévation au sommet et protection spirituelle majeure.", "psaume": "Psaume 91", "saraka": "Préparer un grand repas ou donner un vêtement de valeur à un indigent."},
    "1.2.2.1": {"nom": "Solomana (Carcer)", "signification": "La Chefferie, le Blocage, la Concentration. Figure d'autorité et de pouvoir, mais aussi d'isolement ou d'enfermement temporaire.", "psaume": "Psaume 142", "saraka": "Offrir du cola fendu ou du pain traditionnel à un gardien ou chef de famille."},
    "1.2.1.2": {"nom": "Inza (Amissio)", "signification": "La Perte, la Fatigue, le Renoncement. Baisse d'énergie matérielle ou morale. Invitation pressante à lâcher prise.", "psaume": "Psaume 102", "saraka": "Faire l'aumône de pièces de monnaie ou de vêtements usagés pour conjurer la perte."},
    "1.2.2.2": {"nom": "Adama (Laetitia)", "signification": "La Joie, l'Élévation, la Chance. Fête, soulagement, réussite des projets et grand bonheur à venir (parfois avec un léger retard).", "psaume": "Psaume 4", "saraka": "Donner 100 colas blanches ou partager de la viande de mouton blanc."},
    "1.1.2.1": {"nom": "Youssouf (Puer)", "signification": "L'Action, l'Énergie masculine, le Risque de Trahison. Impulsion, dynamisme pour chercher le bonheur, mais garde-fou contre l'avarice ou les faux amis.", "psaume": "Psaume 35", "saraka": "Donner de la nourriture épicée ou des objets tranchants/métalliques."},
    "1.1.2.2": {"nom": "Allahou talla (Fortuna Minor)", "signification": "Le Succès rapide, le Voyage, la Courte durée. Protection sur les routes, opportunité soudaine à saisir au vol car ses effets sont éphémères.", "psaume": "Psaume 121", "saraka": "Partager des beignets ou de la nourriture légère à l'aube un jeudi ou un vendredi."},
    "2.1.1.1": {"nom": "Maldiou (Caput Draconis)", "signification": "La Réalisation, la Stabilité, la Mère. Réussite à long terme, projets solides et connexion très forte avec les énergies ou la santé de la mère.", "psaume": "Psaume 128", "saraka": "Faire une offrande ou un cadeau direct à votre mère (ou à une figure maternelle)."},
    "2.1.1.2": {"nom": "Badra (Conjunctio)", "signification": "L'Union, le Contrat, l'Association. Excellente figure de rencontre, de réunion, de signature de contrat ou de mariage.", "psaume": "Psaume 133", "saraka": "Offrir des céréales (fonio, riz) à des personnes de votre tranche d'âge un mercredi."},
    "2.1.2.1": {"nom": "Ousmane (Acquisitio)", "signification": "Le Gain, l'Abondance, l'Absorption. Réussite financière, entrée de biens, profits en hausse, investissements très avantageux.", "psaume": "Psaume 112", "saraka": "Faire un don financier important dans un lieu de culte ou à une œuvre de charité."},
    "2.1.2.2": {"nom": "Lamora (Rubeus)", "signification": "La Passion, la Colère, le Mariage. Émotions intenses, union charnelle forte et rapide, ou risques de conflits violents sous le coup de l'impulsion.", "psaume": "Psaume 29", "saraka": "Offrir du cola rouge ou des fruits rouges à une assemblée."},
    "2.2.1.1": {"nom": "Nouhou (Cauda Draconis)", "signification": "La Sortie, la Fin, la Trahison cachée. Fin nécessaire d'une situation toxique, pièges dans l'ombre. Invitation à couper les ponts.", "psaume": "Psaume 59", "saraka": "Faire un sacrifice d'un vieil habit ou nettoyer bénévolement un espace public."},
    "2.2.1.2": {"nom": "Idriss (Albus)", "signification": "La Sagesse, la Clarté, la Paix. Vérité révélée, calme intérieur, honnêteté absolue et résolution propre des litiges juridiques ou financiers.", "psaume": "Psaume 119", "saraka": "Donner du savon, du sel ou de l'eau claire à un démuni."},
    "2.2.2.1": {"nom": "mangousi (Tristitia)", "signification": "La Tristesse, le Blocage, la Nostalgie. Mélancolie, retards sévères ou deuil d'une situation passée nécessaire pour avancer.", "psaume": "Psaume 40", "saraka": "Offrir des produits de la terre (tubercules, sel) à des vieillards le samedi."},
    "2.2.2.2": {"nom": "Moussa (Populus)", "signification": "La Foule, le Collectif, la Répétition. Représente l'assemblée, le public ou la famille. L'issue dépend d'une décision collective ou d'une administration.", "psaume": "Psaume 47", "saraka": "Distribuer du pain ou des aliments de base à une foule ou à un groupe d'enfants."}
}

NOMS_MAISONS = [
    "M1 : Le Consultant / L'Âme", "M2 : Les Gains / L'Argent", "M3 : L'Entourage / Les Déplacements", "M4 : Le Foyer / Le Patrimoine",
    "M5 : Les Amours / Les Enfants", "M6 : Les Blocages / La Santé", "M7 : Le Conjoint / Les Associés", "M8 : La Transformation / La Mort",
    "M9 : Les Voyages / La Spiritualité", "M10 : La Carrière / Le Succès", "M11 : Les Appuis / Les Espoirs", "M12 : Les Épreuves / Les Obstacles",
    "M13 : Témoin Droit (Passé récent)", "M14 : Témoin Gauche (Avenir proche)", "M15 : Le Juge (Le Verdict)", "M16 : La Sentence (L'Issue Ultime)"
]

# =====================================================================
# FONCTIONS LOGIQUES ET MATHÉMATIQUES
# =====================================================================
def identifier_figure(liste_points):
    cle = ".".join(map(str, liste_points))
    return DICTIONNAIRE_FIGURES.get(cle, {"nom": "Inconnue", "signification": "-", "psaume": "Psaume 0", "saraka": "-"})

def additionner_figures(fig_a, fig_b):
    return [2 if (fig_a[i] + fig_b[i]) in [2, 4] else 1 for i in range(4)]

def calculer_cle_ecriture(psaume_str):
    chiffres = [int(c) for c in psaume_str if c.isdigit()]
    total = sum(chiffres) if chiffres else 7
    while total > 9: 
        total = sum(int(c) for c in str(total))
    if total in [1, 4, 8]: return 7
    if total in [3, 6, 9]: return 9
    return 3

def generer_carre_magique(valeur_cible):
    base = (valeur_cible - 12) // 3
    reste = (valeur_cible - 12) % 3
    
    c1, c2, c3, c4, c5, c6, c7, c8, c9 = [base + i for i in range(9)]
    if reste == 1: c7 += 1; c8 += 1; c9 += 1
    elif reste == 2: c4 += 1; c5 += 1; c6 += 1; c7 += 2; c8 += 2; c9 += 2
    
    ligne1 = f"|  {c4:<3} |  {c9:<3} |  {c2:<3} |"
    ligne2 = f"|  {c3:<3} |  {c5:<3} |  {c7:<3} |"
    ligne3 = f"|  {c8:<3} |  {c1:<3} |  {c6:<3} |"
    return f"+------+------+------+\n{ligne1}\n+------+------+------+\n{ligne2}\n+------+------+------+\n{ligne3}\n+------+------+------+"

def format_visuel_text(liste_points):
    lignes = []
    for pt in liste_points:
        if pt == 2: lignes.append("●   ●")
        else: lignes.append("  ●  ")
    return "\n".join(lignes)

def extraire_numero_psaume(psaume_str):
    chiffres = "".join([c for c in psaume_str if c.isdigit()])
    return int(chiffres) if chiffres else 40

# =====================================================================
# INTERFACE SÉCURISÉE ET CODE PRINCIPAL
# =====================================================================
# Définition du mot de passe
MOT_DE_PASSE_CORRECT = "MonCodeSecret123"

if "authentifie" not in st.session_state:
    st.session_state["authentifie"] = False

# Écran de verrouillage si pas connecté
if not st.session_state["authentifie"]:
    st.subheader("🔐 Accès Sécurisé")
    st.write("Veuillez entrer le code d'accès pour consulter l'oracle.")
    
    mot_de_passe_saisi = st.text_input("Mot de passe :", type="password")
    
    if st.button("Se connecter"):
        if mot_de_passe_saisi == MOT_DE_PASSE_CORRECT:
            st.session_state["authentifie"] = True
            st.success("Connexion réussie ! Cliquez à nouveau sur le bouton pour entrer.")
        else:
            st.error("❌ Mot de passe incorrect. Accès refusé.")

# Si l'utilisateur est authentifié, on affiche toute l'application
else:
    st.title("Mon Oracle Géomantique")
    st.write("Calculez votre blason complet et générez vos ordonnances de bains numériques.")

    question = st.text_input("✍️ Quelle est votre question ou intention ?", "Thème général")

    st.write("---")
    st.write("👉 Saisissez vos 4 Maisons Mères (1 = Un point, 2 = Deux points)")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**Maison I**")
        m1_1 = st.selectbox("L1", [1, 2], key="m1_1")
        m1_2 = st.selectbox("L2", [1, 2], key="m1_2")
        m1_3 = st.selectbox("L3", [1, 2], key="m1_3")
        m1_4 = st.selectbox("L4", [1, 2], key="m1_4")
        m1 = [m1_1, m1_2, m1_3, m1_4]

    with col2:
        st.write("**Maison II**")
        m2_1 = st.selectbox("L1", [1, 2], key="m2_1")
        m2_2 = st.selectbox("L2", [1, 2], key="m2_2")
        m2_3 = st.selectbox("L3", [1, 2], key="m2_3")
        m2_4 = st.selectbox("L4", [1, 2], key="m2_4")
        m2 = [m2_1, m2_2, m2_3, m2_4]

    with col3:
        st.write("**Maison III**")
        m3_1 = st.selectbox("L1", [1, 2], key="m3_1")
        m3_2 = st.selectbox("L2", [1, 2], key="m3_2")
        m3_3 = st.selectbox("L3", [1, 2], key="m3_3")
        m3_4 = st.selectbox("L4", [1, 2], key="m3_4")
        m3 = [m3_1, m3_2, m3_3, m3_4]

    with col4:
        st.write("**Maison IV**")
        m4_1 = st.selectbox("L1", [1, 2], key="m4_1")
        m4_2 = st.selectbox("L2", [1, 2], key="m4_2")
        m4_3 = st.selectbox("L3", [1, 2], key="m4_3")
        m4_4 = st.selectbox("L4", [1, 2], key="m4_4")
        m4 = [m4_1, m4_2, m4_3, m4_4]

    st.write("---")

    if st.button("🔮 CALCULER LE THÈME"):
        m5 = [m1[0], m2[0], m3[0], m4[0]]
        m6 = [m1[1], m2[1], m3[1], m4[1]]
        m7 = [m1[2], m2[2], m3[2], m4[2]]
        m8 = [m1[3], m2[3], m3[3], m4[3]]
        
        m9 = additionner_figures(m1, m2)
        m10 = additionner_figures(m3, m4)
        m11 = additionner_figures(m5, m6)
        m12 = additionner_figures(m7, m8)
        
        m13 = additionner_figures(m9, m10)
        m14 = additionner_figures(m11, m12)
        m15 = additionner_figures(m13, m14)
        m16 = additionner_figures(m1, m15)

        theme_complet = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16]
        
        juge = identifier_figure(m15)
        sentence = identifier_figure(m16)
        
        num_ecritures_juge = calculer_cle_ecriture(juge['psaume'])
        num_ecritures_sentence = calculer_cle_ecriture(sentence['psaume'])
        
        id_p_juge = extraire_numero_psaume(juge['psaume'])
        id_p_sent = extraire_numero_psaume(sentence['psaume'])

        st.header("⚖️ Tribunal Décisionnel")
        st.markdown(f"**Intention :** {question}")
        
        col_j, col_s = st.columns(2)
        with col_j:
            st.subheader(f"JUGE (M15) : {juge['nom']}")
            st.text(format_visuel_text(m15))
            st.caption(juge['signification'])
            
        with col_s:
            st.subheader(f"SENTENCE (M16) : {sentence['nom']}")
            st.text(format_visuel_text(m16))
            st.caption(sentence['signification'])

        st.header("🛡️ Ordonnance Spirituelle (Bains)")
        tab1, tab2, tab3 = st.tabs(["🚿 Instructions Bains", "📐 Carrés Magiques (Hatim)", "📦 Sacrifices (Saraka)"])
        
        with tab1:
            st.write(f"🔹 **Pour le Juge ({juge['nom']}) :**")
            st.write(f"Écrivez le **{juge['psaume']}** très exactement **{num_ecritures_juge} fois** à l'encre lavable.")
            st.write(f"🔹 **Pour la Sentence ({sentence['nom']}) :**")
            st.write(f"Écrivez le **{sentence['psaume']}** très exactement **{num_ecritures_sentence} fois** consécutives.")
            st.info("💡 **Utilisation :** Diluez les textes avec de l'eau pure. Lavez-vous avec cette eau (sans savon), recueillez-la et versez-la au pied d'un arbre vivant.")

        with tab2:
            st.write(f"📊 **Carré pour la feuille du Juge ({juge['psaume']}) :**")
            st.text(generer_carre_magique(id_p_juge))
            st.write(f"📊 **Carré pour la feuille de la Sentence ({sentence['psaume']}) :**")
            st.text(generer_carre_magique(id_p_sent))

        with tab3:
            st.success(f"📦 **Aumône Juge ({juge['nom']}) :** {juge['saraka']}")
            st.warning(f"📦 **Aumône Sentence ({sentence['nom']}) :** {sentence['saraka']}")

        st.header("📋 Registre des 16 Maisons")
        with st.expander("Voir le détail des 16 maisons"):
            for i, maison_points in enumerate(theme_complet):
                fig_detail = identifier_figure(maison_points)
                st.write(f"**{NOMS_MAISONS[i]}** : {fig_detail['nom']} (`{'.'.join(map(str, maison_points))}`)")
