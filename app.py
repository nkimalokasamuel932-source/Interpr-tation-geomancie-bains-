        theme[5] = next(k for k, v in FIGURES_DB.items() if v["code"] == [f1["code"][0], f2["code"][0], f3["code"][0], f4["code"][0]])
        theme[6] = next(k for k, v in FIGURES_DB.items() if v["code"] == [f1["code"][1], f2["code"][1], f3["code"][1], f4["code"][1]])
        theme[7] = next(k for k, v in FIGURES_DB.items() if v["code"] == [f1["code"][2], f2["code"][2], f3["code"][2], f4["code"][2]])
        theme[8] = next(k for k, v in FIGURES_DB.items() if v["code"] == [f1["code"][3], f2["code"][3], f3["code"][3], f4["code"][3]])
    except StopIteration:
        # Solution de repli de secours (Fallback) pour éviter un crash complet de l'interface
        st.error("🚨 Une asymétrie critique est détectée dans la matrice. Réinitialisation sur les valeurs fondamentales.")
        theme[5], theme[6], theme[7], theme[8] = m1, m2, m3, m4

    # Calcul du reste du Tribunal (Neveux M9-M12, Témoins M13-M14, Juge M15, Sentence M16)
    theme[9] = copuler_figures(FIGURES_DB[theme[1]], FIGURES_DB[theme[2]])
    theme[10] = copuler_figures(FIGURES_DB[theme[3]], FIGURES_DB[theme[4]])
    theme[11] = copuler_figures(FIGURES_DB[theme[5]], FIGURES_DB[theme[6]])
    theme[12] = copuler_figures(FIGURES_DB[theme[7]], FIGURES_DB[theme[8]])
    theme[13] = copuler_figures(FIGURES_DB[theme[9]], FIGURES_DB[theme[10]])
    theme[14] = copuler_figures(FIGURES_DB[theme[11]], FIGURES_DB[theme[12]])
    theme[15] = copuler_figures(FIGURES_DB[theme[13]], FIGURES_DB[theme[14]])
    theme[16] = copuler_figures(FIGURES_DB[theme[15]], FIGURES_DB[theme[1]])
    return theme

# =====================================================================
# 3. INTERFACE DE SÉCURITÉ
# =====================================================================
st.set_page_config(page_title="Système SST Pro", page_icon="🔮", layout="wide")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_login():
    if st.session_state["username"] == "admin" and st.session_state["password"] == "Somadjely2026":
        st.session_state["authenticated"] = True
    else:
        st.error("❌ Identifiant ou mot de passe incorrect.")

if not st.session_state["authenticated"]:
    st.title("🔒 SST SYSTEM — Interface d'Accès Sécurisée")
    with st.form("login_form"):
        st.text_input("👤 Identifiant", key="username")
        st.text_input("🔑 Mot de passe", type="password", key="password")
        st.form_submit_button("Se connecter", on_click=check_login)
    st.stop()

# =====================================================================
# 4. EXÉCUTION DE L'APPLICATION ET DU DESIGN DE L'INTERFACE
# =====================================================================
st.title("🔮 Plateforme Informatique de Géomancie — SST Pro")

st.header("📥 Saisie de la Base : Les 4 Mères Fondatrices")
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1: m1_select = st.selectbox("Mère 1 (M1) :", options=list(FIGURES_DB.keys()), index=0)
with col_m2: m2_select = st.selectbox("Mère 2 (M2) :", options=list(FIGURES_DB.keys()), index=1)
with col_m3: m3_select = st.selectbox("Mère 3 (M3) :", options=list(FIGURES_DB.keys()), index=2)
with col_m4: m4_select = st.selectbox("Mère 4 (M4) :", options=list(FIGURES_DB.keys()), index=3)

theme_calcule = generer_theme_complet(m1_select, m2_select, m3_select, m4_select)

st.markdown("---")
st.header("📊 Tableau Matriciel Général des 16 Maisons")
st.write("### 🟥 Les Mères & Les Filles")
c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(8)
c1.metric("M1 (Mère)", MAPPING_SIMPLIFIE[theme_calcule[1]])
c2.metric("M2 (Mère)", MAPPING_SIMPLIFIE[theme_calcule[2]])
c3.metric("M3 (Mère)", MAPPING_SIMPLIFIE[theme_calcule[3]])
c4.metric("M4 (Mère)", MAPPING_SIMPLIFIE[theme_calcule[4]])
c5.metric("M5 (Fille)", MAPPING_SIMPLIFIE[theme_calcule[5]])
c6.metric("M6 (Fille)", MAPPING_SIMPLIFIE[theme_calcule[6]])
c7.metric("M7 (Fille)", MAPPING_SIMPLIFIE[theme_calcule[7]])
c8.metric("M8 (Fille)", MAPPING_SIMPLIFIE[theme_calcule[8]])

st.write("### 🟨 Les Neveux & Tribunal Central")
c9, c10, c11, c12, c13, c14, c15, c16 = st.columns(8)
c9.metric("M9 (Neveu)", MAPPING_SIMPLIFIE[theme_calcule[9]])
c10.metric("M10 (Neveu)", MAPPING_SIMPLIFIE[theme_calcule[10]])
c11.metric("M11 (Neveu)", MAPPING_SIMPLIFIE[theme_calcule[11]])
c12.metric("M12 (Neveu)", MAPPING_SIMPLIFIE[theme_calcule[12]])
c13.metric("M13 (T. Droit)", MAPPING_SIMPLIFIE[theme_calcule[13]])
c14.metric("M14 (T. Gauche)", MAPPING_SIMPLIFIE[theme_calcule[14]])
c15.metric("M15 (Juge)", MAPPING_SIMPLIFIE[theme_calcule[15]])
c16.metric("M16 (Sentence)", MAPPING_SIMPLIFIE[theme_calcule[16]])

st.markdown("---")

# =====================================================================
# 5. DÉTECTION DES RÈGLES DE COPULATION DE FIN DE THÈME
# =====================================================================
st.header("🧬 Analyse Statistique Spécifique des Copulations")
parent_detecte_A = theme_calcule[15]
parent_detecte_B = theme_calcule[1]
nameA, nameB = MAPPING_SIMPLIFIE[parent_detecte_A], MAPPING_SIMPLIFIE[parent_detecte_B]
set_parents = {nameA, nameB}

details_engendre = "Les flux d'accouplement suivent le cours naturel des éléments du thème."
if set_parents == {"Youssouf", "Laoussana"}: details_engendre = "⚠️ **MÉCHANCETÉ À CAUSE D'ENFANT**"
elif set_parents == {"Adama", "Younouss"}: details_engendre = "⚠️ **MÉCHANCETÉ À CAUSE D'HÉRITAGE**"
elif set_parents == {"Bourama", "Alaou Tala"}: details_engendre = "⚠️ **MÉCHANCETÉ POUR ENFANT**"
elif set_parents == {"Oumar", "Maldjou"}: details_engendre = "⚠️ **MÉCHANCETÉ À CAUSE DE FEMME**"
elif set_parents == {"Issa", "Solomane"}: details_engendre = "⚠️ **MÉCHANCETÉ D'UN CHEF**"
elif set_parents == {"Ayouba", "Idriss"}: details_engendre = "⚠️ **MÉCHANCETÉ DANS LA FAMILLE OU FOYER**"
elif set_parents == {"Badra", "Ousmane"}: details_engendre = "⚠️ **MÉCHANCETÉ FAITE PAR UN MARABOUT OU GÉOMANCIEN**"
elif set_parents == {"Moussa", "Nouhou"}: details_engendre = "⚠️ **MÉCHANCETÉ FAITE PAR UN GROUPE DE PERSONNES**"
elif set_parents == {"Youssouf", "Younouss"}: details_engendre = "💰 **UNE FEMME QUI A DE BON ESPOIR DE RICHESSE**"
elif set_parents == {"Adama", "Laoussana"}: details_engendre = "🔴 **SACRIFICE ROUGE REQUIS**"
elif set_parents == {"Maldjou", "Ayouba"}: details_engendre = "❌ **DIFFICULTÉ POUR AVOIR DES ENFANTS (BLOCAGE)**"
elif set_parents == {"Idriss", "Oumar"}: details_engendre = "💨 **TEMPÊTE, UN GRAND VENT VIOLENT QUI FAIT DES DÉGÂTS**"
elif set_parents == {"Bourama", "Solomane"}: details_engendre = "👶 **LA GROSSESSE**"
elif set_parents == {"Nouhou", "Ousmane"}: details_engendre = "👑 **LA GRANDEUR ET L'HONNEUR**"
elif set_parents == {"Alaou Tala", "Issa"}: details_engendre = "🚨 **UNE TRÈS GRAVE DIFFICULTÉ**"
elif set_parents == {"Moussa", "Badra"}: details_engendre = "⚔️ **DESTIN DE GUERRIER, DE SOLDAT OU D'ÉLÈVES**"

with st.expander("🔍 Résultat du Croisement de Fin de Thème (M15 + M1)", expanded=True):
    st.write(f"**Parents Détectés :** {parent_detecte_A} ✖️ {parent_detecte_B}")
    st.warning(f"✨ **Verdict Ombral :** {details_engendre}")

st.markdown("---")

# =====================================================================
# 6. EXPLORATEUR DE PASSAGE DANS LES MAISONS
# =====================================================================
st.header("🏠 Analyse Spécifique du Passage d'une Figure en Maison")
col_ex1, col_ex2 = st.columns(2)
with col_ex1: fig_analyse = st.selectbox("Figure à étudier :", options=list(FIGURES_DB.keys()), key="expl_fig")
with col_ex2: maison_analyse = st.selectbox("Maison de destination :", options=list(MAISONS_NOMS.keys()), format_func=lambda x: MAISONS_NOMS[x], key="expl_mai")

if fig_analyse and maison_analyse:
    interpretation_textuelle = FIGURES_DB[fig_analyse]["maisons"].get(maison_analyse, "Analyse absente.")
    st.success(f"📋 **Interprétation du Passage :**\n\n> {interpretation_textuelle}")

st.markdown("---")

# =====================================================================
# 7. ORDONNANCE THÉURGIQUE COMPLÈTE & PROTOCOLES PRATIQUES
# =====================================================================
st.header("📊 Protocole Théurgique Intégral : Focus Maison 16")
figure_finale = theme_calcule[16]
st.info(f"Figure souveraine de fermeture (M16) : **{figure_finale}**")

data_f = FIGURES_DB[figure_finale]

tab_s1, tab_s2, tab_s3, tab_s4 = st.tabs([
    "🐑 1. Sacrifices Correctifs (Saraka)", 
    "✝️ 2. Alignements & Textes Sacrés", 
    "🌿 3. Ingrédients Botaniques",
    "📜 4. Protocoles d'Utilisation (Nassi, Bains, Récitation)"
])

with tab_s1:
    st.markdown(f"**Aumône prescriptive :** {data_f['sacrifice']}")

with tab_s2:
    st.markdown(f"* **Psaume de traçage :** `{data_f['psaume']}`")
    st.markdown(f"* **Verset d'activation :** `{data_f['verset']}`")
    st.markdown(f"* **Sceau Vibratoire :** `{data_f['sceau']}`")
    st.markdown(f"* **Jour Planétaire Sacré :** **{data_f['jour']}**")

with tab_s3:
    st.markdown(f"**Plantes et composants magiques :** {data_f['plantes']}")

with tab_s4:
    st.subheader("🛠️ Guide Opératoire Traditionnel d'Activation")
    
    st.markdown(f"""
    ### 1. Protocole de Récitation (Psaumes & Versets)
    * **Timing Vibratoire :** À pratiquer le **{data_f['jour']}** (Jour de la figure), idéalement à l'aube ou après minuit.
    * **Clé d'Ouverture :** Récitez d'abord le verset de verrouillage (`{data_f['verset']}`) **7, 33 ou 111 fois** consécutives.
    * **Le Corps du Rituel :** Récitez ensuite le `{data_f['psaume']}` **3 fois à voix haute**, en formulant clairement votre vœu ou demande de déblocage à la fin de chaque lecture.
    
    ---
    ### 2. Guide de Préparation du Nassi (Eau Sacrée)
    * **Support d'écriture :** Utilisez une tablette traditionnelle en bois (*Alo*) ou une assiette blanche en porcelaine neuve sans aucun motif.
    * **Encre Sacrée :** Utilisez une encre soluble traditionnelle saine (mélange de safran, eau de rose et charbon de bois pulvérisé). Tracez la figure géomantique **{MAPPING_SIMPLIFIE[figure_finale]}** entourée du `{data_f['verset']}`.
    * **Lavage :** Rincez délicatement l'assiette ou la tablette avec de l'eau pure (eau de source ou eau de pluie) pour dissoudre l'encre. Recueillez le précieux liquide dans un flacon propre.
    * **Usage :** Buvez-en une gorgée chaque matin à jeun pendant **3, 7 ou 9 jours**, ou appliquez-en sur votre visage et vos mains avant vos démarches critiques.
    
    ---
    ### 3. Protocole des Bains Sacrés (Plantes & Décoctions)
    * **Préparation :** Faites bouillir les plantes spécifiques indiquées (`{data_f['plantes']}`) dans une grande marmite d'eau pendant 15 à 30 minutes.
    * **L'Alliance Mystique :** Filtrez la décoction, versez-la dans votre seau et ajoutez-y **un demi-verre de votre Nassi** préparé précédemment.
    * **Le Bain :** Lavez-vous d'abord normalement avec votre savon. À la fin, versez l'eau de plantes tiède de la tête aux pieds en récitant le verset d'activation.
    * **Le Secret du Séchage :** **Ne vous essuyez pas.** Laissez l'eau sacrée sécher d'elle-même sur votre peau afin de sceller l'énergie sur votre enveloppe astrale. *Évitez tout rapport intime pendant la durée du traitement (3 ou 7 jours).*
    """)

st.markdown("---")
st.caption("SST Informatique — Version Générative complète à 16 Maisons. Tous droits réservés.")

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Somadjely : Géomancie & Théurgie", layout="wide")

# 2. BASE DE DONNÉES MAGISTRALE (16 FIGURES)
FIGURES_DATA = {
    "1111": {
        "nom": "Via", "psaume": "Ps 51", "verset": "Ps 51:7", "huile": "Cèdre", "plante": "Hysope", "planete": "Lune",
        "signification": "Chemin de vie, fluidité, changement nécessaire.",
        "priere_salomonique": "Au nom d'Adonaï, que les sentiers se lissent et que l'eau vive emporte tout obstacle sur mon chemin de lumière."
    },
    "1112": {
        "nom": "Cauda Draconis", "psaume": "Ps 59", "verset": "Pr 26:27", "huile": "Sauge", "plante": "Sauge", "planete": "Soleil",
        "signification": "Fin d'un cycle, besoin de protection contre les retours.",
        "priere_salomonique": "Par Agla, je scelle la porte du passé et je commande aux ombres de se dissiper devant l'éclat du Nom Saint."
    },
    "1121": {
        "nom": "Puer", "psaume": "Ps 35", "verset": "Ex 15:3", "huile": "Laurier", "plante": "Laurier", "planete": "Mars",
        "signification": "Énergie nouvelle, courage, action offensive.",
        "priere_salomonique": "Par Elohim Gibor, que ma force soit renouvelée et que mon bras soit celui du juste combattant pour la vérité."
    },
    "1122": {
        "nom": "Puella", "psaume": "Ps 121", "verset": "Ps 46:2", "huile": "Rose", "plante": "Pétales de Rose", "planete": "Vénus",
        "signification": "Harmonie, beauté, attraction de la grâce.",
        "priere_salomonique": "Par El Shaddaï, que la douceur m'entoure et que la beauté divine se manifeste dans chaque fibre de mon être."
    },
    "1211": {
        "nom": "Fortuna Minor", "psaume": "Ps 1", "verset": "Pr 10:22", "huile": "Anis", "plante": "Anis étoilé", "planete": "Mercure",
        "signification": "Petite chance rapide, saisissez les opportunités.",
        "priere_salomonique": "Par Tétragrammaton, que les vents favorables m'apportent le succès rapide et la clarté dans mes affaires."
    },
    "1212": {
        "nom": "Amissio", "psaume": "Ps 102", "verset": "Jl 2:25", "huile": "Encens", "plante": "Sel bénit", "planete": "Vénus",
        "signification": "Lâcher-prise nécessaire pour un renouveau.",
        "priere_salomonique": "Par Emmanuel, je rends ce qui n'est plus mien pour recevoir ce qui m'est promis dans l'abondance de l'Esprit."
    },
    "1221": {
        "nom": "Carcer", "psaume": "Ps 142", "verset": "Es 22:22", "huile": "Girofle", "plante": "Clous de Girofle", "planete": "Saturne",
        "signification": "Blocage, patience et persévérance spirituelle.",
        "priere_salomonique": "Par Cassiel, que les chaînes invisibles se brisent et que ma patience se transforme en une forteresse inébranlable."
    },
    "1222": {
        "nom": "Laetitia", "psaume": "Ps 4", "verset": "Né 8:10", "huile": "Citron", "plante": "Zeste de Citron", "planete": "Jupiter",
        "signification": "Joie intérieure, réussite, expansion.",
        "priere_salomonique": "Par Zadkiel, que la joie du Seigneur soit ma force et que mon horizon s'élargisse vers des hauteurs infinies."
    },
    "2111": {
        "nom": "Caput Draconis", "psaume": "Ps 128", "verset": "Ex 20:12", "huile": "Romarin", "plante": "Romarin", "planete": "Jupiter",
        "signification": "Début de réussite, sagesse, direction claire.",
        "priere_salomonique": "Par Alpha et Oméga, je pose le premier pas vers ma victoire, guidé par la sagesse des anciens et la faveur divine."
    },
    "2112": {
        "nom": "Conjunctio", "psaume": "Ps 133", "verset": "Rt 1:16", "huile": "Curcuma", "plante": "Poudre de Curcuma", "planete": "Mercure",
        "signification": "Union, association, rassemblement des énergies.",
        "priere_salomonique": "Par Elohim Sabaoth, que l'unité soit ma force et que les alliances sacrées se nouent pour le bien de ma mission."
    },
    "2121": {
        "nom": "Acquisitio", "psaume": "Ps 23", "verset": "Ps 23:1", "huile": "Cannelle", "plante": "Bâtons de Cannelle", "planete": "Jupiter",
        "signification": "Gain, succès matériel et bénédictions.",
        "priere_salomonique": "Par Jéhovah Jireh, le Seigneur qui pourvoit, je reçois maintenant la récompense de mes travaux et l'abondance sans fin."
    },
    "2122": {
        "nom": "Rubeus", "psaume": "Ps 29", "verset": "Ct 8:6", "huile": "Gingembre", "plante": "Racine de Gingembre", "planete": "Mars",
        "signification": "Passion intense, feu intérieur, tempérance.",
        "priere_salomonique": "Par Samael, que mon feu soit purifié et qu'il brûle pour éclairer sans jamais détruire, au nom de la Paix divine."
    },
    "2211": {
        "nom": "Fortuna Major", "psaume": "Ps 20", "verset": "Ps 20:7", "huile": "Basilic", "plante": "Basilic frais", "planete": "Soleil",
        "signification": "Grande chance, autorité, bénédiction stable.",
        "priere_salomonique": "Par Michael, Prince de la Lumière, que l'éclat du succès brille sur moi et que ma victoire soit gravée dans l'éternité."
    },
    "2212": {
        "nom": "Albus", "psaume": "Ps 119", "verset": "Es 1:18", "huile": "Menthe", "plante": "Feuilles de Menthe", "planete": "Mercure",
        "signification": "Pureté de pensée, vérité, clarté mentale.",
        "priere_salomonique": "Par Raphaël, guérisseur de l'âme, que mon esprit soit blanc comme la neige et ma parole tranchante comme le diamant."
    },
    "2221": {
        "nom": "Tristitia", "psaume": "Ps 130", "verset": "Es 61:3", "huile": "Verveine", "plante": "Verveine séchée", "planete": "Saturne",
        "signification": "Épreuve purificatrice, transformation profonde.",
        "priere_salomonique": "Par Tétragrammaton Elohim, je transmute ma peine en sagesse et mes larmes en une rosée de renouveau spirituel."
    },
    "2222": {
        "nom": "Populus", "psaume": "Ps 3", "verset": "Gn 22:17", "huile": "Thym", "plante": "Thym commun", "planete": "Lune",
        "signification": "Stabilité collective, influence, paix intérieure.",
        "priere_salomonique": "Par Gabriel, messager céleste, que la paix soit sur mon assemblée et que ma voix résonne avec la force des multitudes."
    }
}

MAISON_INTERP = {
    1: "Vitalité / Soi", 2: "Argent / Biens", 3: "Communication / Proches", 4: "Foyer / Ancêtres",
    5: "Chance / Projets", 6: "Santé / Travail", 7: "Relations / Union", 8: "Transformation / Crise",
    9: "Voyage / Foi", 10: "Carrière / Succès", 11: "Amis / Appuis", 12: "Épreuves / Mal Occulte",
    13: "Résultat", 14: "Influence Externe", 15: "Le Juge (Sentence)", 16: "Conclusion"
}

# 3. LOGIQUE GÉOMANTIQUE
def addition(f1, f2): return "".join(["2" if (int(f1[i]) + int(f2[i])) % 2 == 0 else "1" for i in range(4)])

def calcul_theme(m):
    m = [None] + m
    m.extend([m[1][i]+m[2][i]+m[3][i]+m[4][i] for i in range(4)])
    m.extend([addition(m[1], m[2]), addition(m[3], m[4]), addition(m[5], m[6]), addition(m[7], m[8])])
    m.extend([addition(m[9], m[10]), addition(m[11], m[12]), addition(m[13], m[14]), addition(m[1], m[15])])
    return m

def get_heure_planetaire():
    cycle = ["Saturne", "Jupiter", "Mars", "Soleil", "Vénus", "Mercure", "Lune"]
    d = {"Monday": 6, "Tuesday": 2, "Wednesday": 5, "Thursday": 1, "Friday": 4, "Saturday": 0, "Sunday": 3}
    return cycle[(d[datetime.datetime.now().strftime("%A")] + datetime.datetime.now().hour) % 7]

# 4. INTERFACE
st.title("🛡️ Somadjely : Maîtrise Théurgique")
with st.sidebar:
    st.header("Diagnostic")
    mères = [st.text_input(f"Mère {i}", "1121") for i in range(1, 5)]
    maison_choisie = st.number_input("Maison à traiter (1-16)", 1, 16, 1)

if st.button("Dévoiler le Protocole"):
    theme = calcul_theme(mères)
    data = FIGURES_DATA.get(theme[maison_choisie])
    heure_actuelle = get_heure_planetaire()
    
    st.subheader(f"Maison {maison_choisie} : {MAISON_INTERP[maison_choisie]}
