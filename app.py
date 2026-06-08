# -*- coding: utf-8 -*-
import streamlit as st

# =====================================================================
# 1. DICTIONNAIRE HARMONISÉ DES 16 FIGURES (CODES BINAIRES UNIQUES)
# =====================================================================
# Strates : [Tête, Poitrine, Ventre, Pied] | 1 = Impair, 2 = Pair
FIGURES_DB = {
    "Youssouf (Sedjou / Puer)": {
        "code": [1, 1, 2, 1], "numero": 1, "element": "Feu", "nature": "Passé", "polarite": "Mâle",
        "jour": "Mardi", "psaume": "Psaume 35", "verset": "Exode 15 v.3", "sceau": "2e Pentacle de Mars",
        "sacrifice": "7 colas rouges, ou un vêtement de valeur à une femme.",
        "plantes": "Zaban, Balanzan, Poudre de fusil (Arbres : Djala, N'zèrènidjè, Djatiguifaga)",
        "maisons": {
            1: "Beaucoup de bonheur en vue, personne aimée dans son milieu. Attention à une trahison latente.",
            2: "Difficultés dans la chance. Risque de fluctuations ou de pertes de richesses matérielles.",
            3: "Brouilles dans les affaires familiales ou entre frères/sœurs. Risque d'avarice.",
            4: "Perte de richesses, procès difficile en vue ou trahison flagrante dans la maison paternelle.",
            5: "Chance d'avoir un enfant. Attention aux nouvelles mensongères ou aux pertes de courriers.",
            6: "Survenue d'une maladie difficile ou d'une vive colère. Ce qui est perdu ne sera pas retrouvé.",
            7: "Difficulté d'avoir satisfaction dans une entreprise ou une union. Risque de trahison.",
            8: "Annonce la mort d'une situation, d'une idée ou l'emprisonnement/fermeture de quelque chose.",
            9: "Voyage désagréable provoqué par une trahison ou un manque de parole.",
            10: "Acquisition du pouvoir pour celui qui cherche. Pour les autres, trahison chez les hauts placés.",
            11: "Déception ou traîtrise causée directement par un ou des amis proches.",
            12: "Prolifération d'ennemis cachés et trahison imminente. Risque de destruction.",
            13: "Difficulté de déplacement pour le voyageur. Trahison de l'entourage immédiat.",
            14: "Annonce un gain d'argent rapide. On retrouve un objet perdu. Faveurs venant des femmes.",
            15: "Climat de suspicion et de doutes au cours d'une assemblée. Révélation d'une ruse.",
            16: "Annonce la guérison du malade. Pour toute autre affaire : trahison finale au bout de l'effort."
        }
    },
    "Adama (Letitia / La joie)": {
        "code": [1, 2, 2, 2], "numero": 2, "element": "Feu", "nature": "Passé", "polarite": "Mâle",
        "jour": "Jeudi", "psaume": "Psaume 4", "verset": "Néhémie 8 v.10", "sceau": "2e Pentacle de Jupiter",
        "sacrifice": "Mesure de sucre, de dattes, ou un pot de miel à distribuer.",
        "plantes": "Frogofraga, N'gouna, Sérétoro (Arbres : Sana, Gounan)",
        "maisons": {
            1: "Joie, bienfaisance, réalisation des vœux et projets. Élévation et longue vie promises.",
            2: "Bon travail fructifiant, les problèmes seront résolus. Satisfaction amenée par l'argent.",
            3: "Entente cordiale entre frères et sœurs. Nouvelles réjouissantes, voyage heureux.",
            4: "Foyer agréable, famille unie. Héritage ou acquisition de biens dans la ville natale.",
            5: "Venue d'une nouvelle réjouissante. Chance d'avoir une fille. Amour heureux.",
            6: "Emploi stable amenant le bonheur. Vie familiale calme, rétablissement de la santé.",
            7: "Excellent mariage réussi. Union de bon augure. Réalisation des ambitions financières.",
            8: "Difficultés temporaires à propos de la chance, mais issue positive. Appuis occultes.",
            9: "Chance de trouver un bon travail. Voyageur agréable. Sereine élévation spirituelle.",
            10: "Victoire éclatante, obtention d'une place ou d'un statut majeur. Honneurs et paix.",
            11: "Appuis certains et grande chance. Beaucoup d'amis fidèles. Propos mielleux.",
            12: "Méchanceté sur les lieux de travail vite balayée. Victoire assurée sur les ennemis.",
            13: "Leçon tirée du passé. Changement positif, acquisition de travail près du domicile.",
            14: "Acquisition de biens importants et de richesses matérielles. Lendemain sécurisé.",
            15: "Le Juge confirme une atmosphère de soulagement général, de clarté et de sérénité.",
            16: "Bonne finalité de l'entreprise, aboutissant à des situations de chance et de triomphe."
        }
    },
    "Mahamadou / Malidjou (Caput Draconis)": {
        "code": [1, 1, 1, 2], "numero": 3, "element": "Air", "nature": "Futur", "polarite": "Femelle",
        "jour": "Jeudi", "psaume": "Psaume 128", "verset": "Exode 20 v.12", "sceau": "1er Pentacle de la Terre",
        "sacrifice": "Une mesure de céréales (mil ou maïs) à une mère de famille.",
        "plantes": "Arbres qui poussent sur colline ou toile, Djoun (Arbres : Djoulassounkalani, Sébé)",
        "maisons": {
            1: "Réalisation des vœux ou projets. Venue d'une personne étrangère. Éloquence.",
            2: "Chance et relation de parenté. Multiplication des gains, bon investissement.",
            3: "Bonheur venant d'un frère ou d'une sœur. Beau fixe pour les voyages et démarches.",
            4: "Réjouissance dans la famille, beaucoup de bonheur. Logement accueillant, héritage fructueux.",
            5: "Chance d'avoir une fille. Victoire en procès, les enfants donnent entière satisfaction.",
            6: "Maladie ou colère d'un parent de la mère. Satisfaction générale et professionnelle en fin de compte.",
            7: "Chance de se marier avec une personne apparentée. Disparition des peurs, victoire en procès.",
            8: "Changement de situation via héritage. Conjoint aisé, contrat avantageux, protection.",
            9: "L'échec ou la perte se transforme en succès. Arrivée d'un parent étranger.",
            10: "Ascension sociale ou victoire. Amitié avec une personne puissante. Sens de la justice.",
            11: "Espoirs et appuis dus à la famille ou venant de la mère. Amitié sûre et profitable.",
            12: "Méchanceté des frères/sœurs ennemis. Obstacles sans danger. Méfiez-vous de l'eau.",
            13: "Réalisation des ambitions à court délai. Changement positif dans la concession.",
            14: "Réussite à partir d'une mauvaise affaire. La chose perdue sera retrouvée. Expansion.",
            15: "Discussions ou éclaircissements à propos de la mère. Résolution finale des doutes.",
            16: "Bonne finalité, bonheur, grande réussite et élévation dans l'entreprise. Protection divine."
        }
    },
    "Idrissa (Albayaro / Albus)": {
        "code": [2, 2, 1, 2], "numero": 4, "element": "Eau", "nature": "Futur", "polarite": "Mâle",
        "jour": "Vendredi", "psaume": "Psaume 119 (Beth)", "verset": "Isaïe 1 v.18", "sceau": "2e Pentacle de Mercure",
        "sacrifice": "Offrande de lait frais, de crème ou partage d'un bélier blanc.",
        "plantes": "N'gokou, tous les arbres qui vivent sur les fleuves (Arbres : Dougalén)",
        "maisons": {
            1: "Caractère franc, tempérament mystique. Chance rapide, gains propres et clairs.",
            2: "Saine situation financière, illumination de la chance après une période noire.",
            3: "Ouverture de la chance commerciale. Relations rares mais sûres et agréables.",
            4: "Bonté venant de l'entourage. Héritage en vue, famille heureuse sans histoire.",
            5: "Chance d'avoir un enfant pour une personne dite stérile. Amour sincère et chaste.",
            6: "Petit souci de santé passager ou colère en famille. Très bon signe pour le voyageur.",
            7: "Bonne entente dans le couple, engagement et promesses respectés. Grossesse en route.",
            8: "Changement important lié au père ou au frère. Héritage ou augmentation des gains.",
            9: "Hésitations avant de prendre la route, mais voyage paisible à la fin. Sereine spiritualité.",
            10: "Situation sociale correcte, modeste et sûre. Gain venant d'une haute personnalité.",
            11: "Bonnes relations amicales et fidèles. Simple médisance sans gravité autour de vous.",
            12: "Méchanceté stérile d'ennemis du milieu artistique ou intellectuel. Attention aux yeux.",
            13: "Femme de bon augure dans la chambre. Recherche spirituelle féconde, voyage fructueux.",
            14: "Ascension, succès et acquisition de gains importants. Évolution très favorable.",
            15: "Le Juge annonce une issue pacifiée, une clarté totale et la levée des derniers doutes.",
            16: "Annonce la réussite, la clarté et le bonheur pour la finalité de l'entreprise. Consécration."
        }
    },
    "Ibrahima (Taliki / Via)": {
        "code": [1, 2, 2, 1], "numero": 5, "element": "Eau", "nature": "Présent", "polarite": "Mâle",
        "jour": "Lundi", "psaume": "Psaume 120", "verset": "Psaume 121 v.8", "sceau": "5e Pentacle de la Lune",
        "sacrifice": "Sacrifier un canard et le préparer en repas familial ou donner du riz.",
        "plantes": "Zondjè, arbres poussant au bord des sources d'eau (Arbres : Tièkala, Zongnè)",
        "maisons": {
            1: "Annonce d'une grossesse ou d'une bonne nouvelle. Projets mouvants, nervosité ou ruse.",
            2: "Chance d'avoir un garçon ou d'acquérir un gain grâce à un enfant. Transactions fluides.",
            3: "Diminution des querelles, augmentation des bons voisins. Démarches et voyage prochain.",
            4: "Annonce un nouveau voisin. Résolution d'un problème difficile. Instabilité ou déménagement.",
            5: "Chance d'un enfant bien bâti qui comblera de joie. Timides rentrées d'argent, grossesse.",
            6: "Colère ou maladie d'un enfant. Peines causées par un tyran. Voyage cher payé.",
            7: "Grossesse pour la femme mariée. Retards dans la concrétisation des projets extérieurs.",
            8: "Changement de situation, messages de l'au-delà ou difficultés liées à un héritage.",
            9: "Retour de l'enfant d'un voyage. Départ déterminant, retards possibles mais esprit créatif.",
            10: "Succès grâce à une haute personnalité. Efforts à répéter sans cesse, situation stable.",
            11: "Annonce un enfant qui comblera de joie. Appuis bienfaisants après de vives angoisses.",
            12: "Ennemis de milieux défavorisés mais persistants. Fin des ennuis matériels, prudence sur la route.",
            13: "Grande joie relative à un enfant. Stabilité familiale, voyage bénéfique et changement.",
            14: "Acquisition de richesses à venir. Nouveau dénouement et climat général positif.",
            15: "Annonce un quiproquo ou des angoisses relatives à un enfant. Dénouement sinueux.",
            16: "Bonheur dû à un enfant à l'extérieur. Réussite finale si l'on évite l'inaction."
        }
    },
    "Issa (Nabbi Issa / Amissio)": {
        "code": [2, 1, 1, 2], "numero": 6, "element": "Eau", "nature": "Passé", "polarite": "Mâle",
        "jour": "Mercredi", "psaume": "Psaume 102", "verset": "Juël 2 v.25", "sceau": "5e Pentacle de Vénus",
        "sacrifice": "Choses à plusieurs couleurs (pintade, fonio). À donner à un chanteur.",
        "plantes": "N'gagnaka, Niama, Chi (Arbres : Sourou N'tomo)",
        "maisons": {i: f"Perte matérielle, sacrifice nécessaire, détachement ou baisse d'énergie en Maison {i}." for i in range(1, 17)}
    },
    "Oumarou (Lomara / Rubeus)": {
        "code": [1, 2, 1, 1], "numero": 7, "element": "Air", "nature": "Passé", "polarite": "Femelle",
        "jour": "Mardi", "psaume": "Psaume 29", "verset": "Cantique 8 v.6", "sceau": "4e Pentacle de Mars",
        "sacrifice": "Cola rouge, bélier au cou rouge, maïs rouge.",
        "plantes": "Gaba blé, Djati tgui fa djiri (Arbres : Gabablen, Foronto, Wo)",
        "maisons": {i: f"Passion destructrice, violence verbale, danger de sang ou d'agression en Maison {i}." for i in range(1, 17)}
    },
    "Ayouba (Almangoussi / Tristitia)": {
        "code": [2, 2, 2, 1], "numero": 8, "element": "Terre", "nature": "Futur", "polarite": "Postérieur Mâle",
        "jour": "Samedi", "psaume": "Psaume 40", "verset": "Isaïe 61 v.3", "sceau": "5e Pentacle de Saturne",
        "sacrifice": "Tout ce qu'on trouve sous la terre, savon, sel. À donner aux vieux.",
        "plantes": "Herbes qui poussent sur les tombeaux, Koroni fin (Arbres : Koto, Ngokou)",
        "maisons": {i: f"Tristesse, affliction profonde, blocage matériel lourd ou enterrement d'affaire en Maison {i}." for i in range(1, 17)}
    },
    "Qala-llahou (Aboubakr Sidik / Fortuna Minor)": {
        "code": [1, 1, 2, 2], "numero": 9, "element": "Feu", "nature": "Passé", "polarite": "Mâle",
        "jour": "Dimanche", "psaume": "Psaume 121", "verset": "Psaume 46 v.2", "sceau": "4e Pentacle du Soleil",
        "sacrifice": "Cola blanc, habit blanc, bélier blanc.",
        "plantes": "Aladjon, racines d'arbres coupant la route (Arbres : Alladjô, Congo Sirani)",
        "maisons": {i: f"Petite chance, secours rapide du destin, protection divine éphémère en Maison {i}." for i in range(1, 17)}
    },
    "Solomana (Manssa Souleymane / Carcer)": {
        "code": [1, 2, 1, 2], "numero": 10, "element": "Terre", "nature": "Présent", "polarite": "Femelle",
        "jour": "Samedi", "psaume": "Psaume 142", "verset": "Isaïe 22 v.22", "sceau": "7e Pentacle de Saturne",
        "sacrifice": "Tout ce qu'on trouve sous la terre, savon, sel. À donner aux vieux.",
        "plantes": "Mandé sounsoun, Sounsoun (Arbres : Zamba, Sira/Baobab)",
        "maisons": {i: f"Enfermement, secret bien gardé, isolement nécessaire ou contrainte majeure en Maison {i}." for i in range(1, 17)}
    },
    "Badra (Badra Aliou / Conjunctio)": {
        "code": [2, 1, 1, 1], "numero": 11, "element": "Air", "nature": "Présent", "polarite": "Femelle",
        "jour": "Mercredi", "psaume": "Psaume 133", "verset": "Ruth 1 v.16", "sceau": "4e Pentacle de Mercure",
        "sacrifice": "Choses à plusieurs couleurs (pintade, fonio). À donner à un muezzin.",
        "plantes": "Guélé (Arbres : Triki, Gouélé)",
        "maisons": {i: f"Réunion, assemblée, signature de contrats, accords mutuels ou retrouvailles en Maison {i}." for i in range(1, 17)}
    },
    "Nouhou (Nouhoum / Cauda Draconis)": {
        "code": [2, 2, 1, 1], "numero": 12, "element": "Terre", "nature": "Futur", "polarite": "Femelle",
        "jour": "Dimanche", "psaume": "Psaume 59", "verset": "Psaume 68 v.2", "sceau": "6e Pentacle de Saturne",
        "sacrifice": "Cola blanc, habit blanc, bélier blanc.",
        "plantes": "Goundjè (Arbres : Koudjè, Zèguènè)",
        "maisons": {i: f"Trahison occulte, fin de cycle brutale, déception ou présence d'un piège vicieux en Maison {i}." for i in range(1, 17)}
    },
    "Laoussana (Alhoussein / Puella)": {
        "code": [2, 1, 2, 2], "numero": 13, "element": "Eau", "nature": "Passé", "polarite": "Femelle",
        "jour": "Samedi", "psaume": "Psaume 119 (Aleph)", "verset": "Cantique 4 v.7", "sceau": "2e Pentacle de Vénus",
        "sacrifice": "Tout ce qu'on trouve sous la terre, savon, sel.",
        "plantes": "Djoulasonkalani (Plantes gluantes, herbes des vieux puits)",
        "maisons": {i: f"Désirs de plaisirs, charme, présence féminine influente, frivolité ou joie passagère en Maison {i}." for i in range(1, 17)}
    },
    "Ousmane (Mory Zoumana / Acquisitio)": {
        "code": [2, 1, 2, 1], "numero": 14, "element": "Terre", "nature": "Futur", "polarite": "Mâle",
        "jour": "Jeudi", "psaume": "Psaume 23", "verset": "Psaume 23 v.1", "sceau": "3e Pentacle de Jupiter",
        "sacrifice": "Fruits secs, longs animaux. À donner à un groupe.",
        "plantes": "N'doubalé, Frogofraga (Arbres : Troubala, Dougalen)",
        "maisons": {i: f"Acquisition de biens, enrichissement matériel permanent, succès financier majeur en Maison {i}." for i in range(1, 17)}
    },
    "Younouss (Tontigui)": {
        "code": [1, 1, 1, 1], "numero": 15, "element": "Air", "nature": "Futur", "polarite": "Femelle",
        "jour": "Vendredi", "psaume": "Psaume 112", "verset": "Deutéronome 28 v.12", "sceau": "6e Pentacle de Jupiter",
        "sacrifice": "Bijoux, parures ou objets brillants. À donner aux enfants.",
        "plantes": "N'tomotigui, Zondjè (Arbres : Fogofogo)",
        "maisons": {i: f"Grande chance matérielle, succès retentissant, honneur et élévation sociale en Maison {i}." for i in range(1, 17)}
    },
    "Moussa (Djama / Populus)": {
        "code": [2, 2, 2, 2], "numero": 16, "element": "Feu", "nature": "Présent", "polarite": "Femelle",
        "jour": "Lundi", "psaume": "Psaume 47", "verset": "Genèse 22 v.17", "sceau": "1er Pentacle de la Lune",
        "sacrifice": "Fruits frais, graines, animaux féminins. À donner aux religieux.",
        "plantes": "N'tomi, N'galama (Arbres : Tomy, Sounzoufing)",
        "maisons": {i: f"Influence de la foule, rumeurs publiques, grand nombre ou dispersion d'énergie en Maison {i}." for i in range(1, 17)}
    }
}

MAISONS_NOMS = {
    1: "Maison 1 (Consultant / Âme)", 2: "Maison 2 (Chance / Biens)", 3: "Maison 3 (Entourage / Frères)", 4: "Maison 4 (Foyer / Patrimoine)",
    5: "Maison 5 (Enfants / Amours)", 6: "Maison 6 (Maladies / Obstacles)", 7: "Maison 7 (Conjoint / Associés)", 8: "Maison 8 (Blocages / Mort)",
    9: "Maison 9 (Voyages / Spiritualité)", 10: "Maison 10 (Pouvoir / Métier)", 11: "Maison 11 (Espoirs / Amis)", 12: "Maison 12 (Ennemis cachés)",
    13: "Maison 13 (Chambre / Présent)", 14: "Maison 14 (Avenir / Gains futurs)", 15: "Maison 15 (Le Juge)", 16: "Maison 16 (Sentence finale)"
}

MAPPING_SIMPLIFIE = {k: k.split(" ")[0] for k in FIGURES_DB.keys()}

# =====================================================================
# 2. LOGIQUE MATHÉMATIQUE GÉOMANTIQUE SÉCURISÉE (ANTI-CRASH)
# =====================================================================
def additionner_lignes(l1, l2):
    return 2 if l1 == l2 else 1

def copuler_figures(figA, figB):
    code_resultat = []
    for i in range(4):
        code_resultat.append(additionner_lignes(figA["code"][i], figB["code"][i]))
    for nom, data in FIGURES_DB.items():
        if data["code"] == code_resultat:
            return nom
    return list(FIGURES_DB.keys())[0]

def generer_theme_complet(m1, m2, m3, m4):
    f1, f2, f3, f4 = FIGURES_DB[m1], FIGURES_DB[m2], FIGURES_DB[m3], FIGURES_DB[m4]
    theme = {1: m1, 2: m2, 3: m3, 4: m4}
    
    # Transposition matricielle pour les Filles (M5-M8) avec Fallback de sécurité robuste
    for m, idx in [(5, 0), (6, 1), (7, 2), (8, 3)]:
        code_cherche = [f1["code"][idx], f2["code"][idx], f3["code"][idx], f4["code"][idx]]
        match = [k for k, v in FIGURES_DB.items() if v["code"] == code_cherche]
        if match:
            theme[m] = match[0]
        else:
            # Fallback automatique en cas d'imprévu
            theme[m] = list(FIGURES_DB.keys())[idx]

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
# 3. INTERFACE DE SÉCURITÉ ACCÈS
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
# 4. EXÉCUTION DE L'APPLICATION
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
# 5. DETECTEUR DE CROISEMENTS CRIMINELS/VERDICTS OMBLAUX
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
    interpretation_textuelle = FIGURES_DB[fig_analyse]["maisons"].get(maison_analyse, "Analyse absente ou en cours de rédaction dans votre livret.")
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
    st.subheader("🛠 ... Guide Opératoire Traditionnel d'Activation")
    st.markdown(f"""
    ### 1. Protocole de Récitation (Psaumes & Versets)
    * **Timing Vibratoire :** À pratiquer le **{data_f['jour']}** (Jour de la figure), idéalement à l'aube ou après minuit.
    * **Clé d'Ouverture :** Récitez d'abord le verset de verrouillage (`{data_f['verset']}`) **7, 33 ou 111 fois** consécutives.
    * **Le Corps du Rituel :** Récitez ensuite le `{data_f['psaume']}` **3 fois à voix haute**, en formulant clairement votre vœu à la fin de chaque lecture.
    
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
st.caption("SST Informatique — Version Générative complète à 16 Maisons. Tous droits réservés. Édit 2026.")
