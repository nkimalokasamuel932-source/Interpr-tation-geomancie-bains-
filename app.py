# -*- coding: utf-8 -*-
import streamlit as st

# =====================================================================
# 1. DICTIONNAIRE AUTHENTIQUE DES 16 FIGURES ET PASAAGES (Somadjely)
# =====================================================================
# La structure intègre désormais le dictionnaire 'maisons' pour l'analyse de passage.
FIGURES_DB = {
    "Youssouf (Sedjou / Puer)": {
        "numero": 1, "element": "Feu", "nature": "Passé", "polarite": "Mâle",
        "psaume": "Psaume 35", "verset": "Exode 15 v.3", "sceau": "2e Pentacle de Mars",
        "sacrifice": "Cola rouge, bélier au cou rouge, maïs rouge. À donner aux handicapés ou personnes s'étant blessées le Mardi.",
        "plantes": "Zaban, Balanzan, Poudre de fusil (Arbres : Djala, N'zèrènidjè, Djatiguifaga)",
        "maisons": {
            1: "Idées de dispute, impulsivité, colère ou force physique dominante chez le consultant.",
            2: "Gains rapides mais instables, argent acquis par la lutte ou dépensé de manière impulsive.",
            3: "Disputes ou rivalités dans l'entourage proche, démarches courageuses mais risquées.",
            4: "Tensions ou conflits dans le foyer, patrimoine exposé à des risques ou des transformations brutales.",
            5: "Passions amoureuses intenses, impulsivité avec les enfants, désirs ardents.",
            6: "Maladies subites liées au sang ou à la fièvre, accidents mineurs ou opérations.",
            7: "Rivalités dans le couple ou avec les associés, disputes ouvertes, partenaire conflictuel.",
            8: "Blocage surmonté par la force, transformation radicale, fin de situation brutale.",
            9: "Voyage rapide, recherche spirituelle axée sur la force, projets audacieux à l'étranger.",
            10: "Succès professionnel obtenu de haute lutte, autorité affirmée, poste de commandement.",
            11: "Amis fidèles mais parfois agressifs, espoirs centrés sur une action rapide.",
            12: "Ennemis déclarés et combatifs, blocages dus à la colère ou à la précipitation.",
            13: "Chambre à coucher ou lit sous tension, gain immédiat mais volatilité financière.",
            14: "Gains futurs dépendants d'un effort intense, d'un coup de poker ou d'une lutte commerciale.",
            15: "Le Juge valide une issue tranchante, rapide et sans compromis possible.",
            16: "Sentence finale : Victoire par la force ou rupture nette. Libération par le feu."
        }
    },
    "Adama (Letitia / La joie)": {
        "numero": 2, "element": "Feu", "nature": "Passé", "polarite": "Mâle",
        "psaume": "Psaume 4", "verset": "Néhémie 8 v.10", "sceau": "2e Pentacle de Jupiter",
        "sacrifice": "Fruits secs, longs animaux. À donner à plusieurs personnes (Groupe) le Jeudi.",
        "plantes": "Frogofraga, N'gouna, Sérétoro (Arbres : Sana, Gounan)",
        "maisons": {
            1: "Joie de vivre, optimisme, consultant serein, épanoui et bienveillant.",
            2: "Augmentation des revenus, gains faciles, chance matérielle et financière.",
            3: "Bonnes nouvelles de l'entourage, relations fraternelles joyeuses et harmonieuses.",
            4: "Paix au sein du foyer, embellissement de la maison, héritage ou patrimoine sécurisé.",
            5: "Amours partagés, bonheur avec les enfants, créativité débordante.",
            6: "Bonne santé, guérison rapide, les problèmes quotidiens s'allègent.",
            7: "Mariage heureux, association fructueuse, harmonie avec le partenaire.",
            8: "Héritage inattendu, fin positive d'une crise, régénération par la joie.",
            9: "Voyage agréable et profitable, chance spirituelle, hautes études réussies.",
            10: "Honneurs, promotion professionnelle, reconnaissance publique des mérites.",
            11: "Soutiens amicaux précieux, les espoirs se réalisent au-delà des attentes.",
            12: "Les ennemis deviennent inoffensifs, les blocages secrets se dissolvent dans la clarté.",
            13: "Joie présente dans l'intimité, argent disponible immédiatement pour les plaisirs.",
            14: "Avenir radieux, promesse de richesses futures et de stabilisations heureuses.",
            15: "Le Juge présage une issue joyeuse et un soulagement total des peines.",
            16: "Sentence finale : Conclusion heureuse, célébration et pleine réussite de l'affaire."
        }
    },
    # -- Les autres figures suivent exactement la même structure (M1 à M16) --
    "Mahamadou / Malidjou (Caput Draconis)": {
        "numero": 3, "element": "Air", "nature": "Futur", "polarite": "Femelle",
        "psaume": "Psaume 128", "verset": "Exode 20 v.12", "sceau": "1er Pentacle de la Terre",
        "sacrifice": "Fruits secs, longs animaux. À donner à plusieurs personnes (Groupe) le Jeudi.",
        "plantes": "Arbres qui poussent sur colline ou toile, Djoun (Arbres : Djoulassounkalani, Sébé)",
        "maisons": {i: f"Interprétation de Malidjou en Maison {i} selon le dictionnaire de votre dossier." for i in range(1, 17)}
    },
    "Idrissa (Albayaro / Albus)": {
        "numero": 4, "element": "Eau", "nature": "Futur", "polarite": "Mâle",
        "psaume": "Psaume 119 (Beth)", "verset": "Isaïe 1 v.18", "sceau": "2e Pentacle de Mercure",
        "sacrifice": "Bijoux, objets précieux, offrandes libres. À donner aux enfants le Vendredi.",
        "plantes": "N'gokou, tous les arbres qui vivent sur les fleuves (Arbres : Dougalén)",
        "maisons": {i: f"Interprétation d'Idriss en Maison {i} selon le dictionnaire de votre dossier." for i in range(1, 17)}
    },
    "Ibrahima (Taliki / Via)": {
        "numero": 5, "element": "Eau", "nature": "Présent", "polarite": "Mâle",
        "psaume": "Psaume 120", "verset": "Psaume 121 v.8", "sceau": "5e Pentacle de la Lune",
        "sacrifice": "Fruits frais, graines de céréales, animaux féminins. À donner aux religieux ou personnes s'occupant de la religion le Lundi.",
        "plantes": "Zondjè, arbres poussant au bord des sources d'eau (Arbres : Tièkala, Zongnè)",
        "maisons": {i: f"Interprétation de Bourama en Maison {i} selon le dictionnaire de votre dossier." for i in range(1, 17)}
    },
    "Issa (Nabbi Issa / Amissio)": {
        "numero": 6, "element": "Eau", "nature": "Passé", "polarite": "Mâle",
        "psaume": "Psaume 102", "verset": "Joël 2 v.25", "sceau": "5e Pentacle de Vénus",
        "sacrifice": "Choses à plusieurs couleurs (pintade, fonio, poule tachetée). À donner à un chanteur, griot ou muezzin le Mercredi.",
        "plantes": "N'gagnaka, Niama, Chi (Arbres : Sourou N'tomo)",
        "maisons": {i: f"Interprétation d'Issa en Maison {i} selon le dictionnaire de votre dossier." for i in range(1, 17)}
    },
    "Oumarou (Lomara / Rubeus)": {
        "numero": 7, "element": "Air", "nature": "Passé", "polarite": "Femelle",
        "psaume": "Psaume 29", "verset": "Cantique 8 v.6", "sceau": "4e Pentacle de Mars",
        "sacrifice": "Cola rouge, bélier au cou rouge, maïs rouge. À donner aux handicapés ou personnes s'étant blessées le Mardi.",
        "plantes": "Gaba blé, Djati tgui fa djiri (Arbres : Gabablen, Foronto, Wo)",
        "maisons": {i: f"Interprétation d'Oumar en Maison {i} selon le dictionnaire de votre dossier." for i in range(1, 17)}
    },
    "Ayouba (Almangoussi / Tristitia)": {
        "numero": 8, "element": "Terre", "nature": "Futur", "polarite": "Postérieur Mâle",
        "psaume": "Psaume 40", "verset": "Isaïe 61 v.3", "sceau": "5e Pentacle de Saturne",
        "sacrifice": "Tout ce qu'on trouve sous la terre, savon, sel. À donner aux vieilles et vieux le Samedi.",
        "plantes": "Herbes qui poussent sur les tombeaux, Koroni fin (Arbres : Koto, Ngokou)",
        "maisons": {i: f"Interprétation d'Ayouba en Maison {i} selon le dictionnaire de votre dossier." for i in range(1, 17)}
    },
    "Qala-llahou (Aboubakr Sidik / Fortuna Minor)": {
        "numero": 9, "element": "Feu", "nature": "Passé", "polarite": "Mâle",
        "psaume": "Psaume 121", "verset": "Psaume 46 v.2", "sceau": "4e Pentacle du Soleil",
        "sacrifice": "Cola blanc, habit blanc, bélier blanc. À donner aux personnages de grande renommée, chefs le Dimanche.",
        "plantes": "Aladjon, racines d'arbres coupant la route (Arbres : Alladjô, Congo Sirani)",
        "maisons": {i: f"Interprétation d'Alaou Tala en Maison {i} selon le dictionnaire de votre dossier." for i in range(1, 17)}
    },
    "Solomana (Manssa Souleymane / Carcer)": {
        "numero": 10, "element": "Terre", "nature": "Présent", "polarite": "Femelle",
        "psaume": "Psaume 142", "verset": "Isaïe 22 v.22", "sceau": "7e Pentacle de Saturne",
        "sacrifice": "Tout ce qu'on trouve sous la terre, savon, sel. À donner aux vieilles et vieux le Samedi.",
        "plantes": "Mandé sounsoun, Sounsoun (Arbres : Zamba, Sira/Baobab)",
        "maisons": {i: f"Interprétation de Solomane en Maison {i} selon le dictionnaire de votre dossier." for i in range(1, 17)}
    },
    "Badra (Badra Aliou / Conjunctio)": {
        "numero": 11, "element": "Air", "nature": "Présent", "polarite": "Femelle",
        "psaume": "Psaume 133", "verset": "Ruth 1 v.16", "sceau": "4e Pentacle de Mercure",
        "sacrifice": "Choses à plusieurs couleurs (pintade, fonio, poule). À donner à un chanteur, griot ou muezzin le Mercredi.",
        "plantes": "Guélé (Arbres : Triki, Gouélé)",
        "maisons": {i: f"Interprétation de Badra en Maison {i} selon le dictionnaire de votre dossier." for i in range(1, 17)}
    },
    "Nouhou (Nouhoum / Cauda Draconis)": {
        "numero": 12, "element": "Terre", "nature": "Futur", "polarite": "Femelle",
        "psaume": "Psaume 59", "verset": "Psaume 68 v.2", "sceau": "6e Pentacle de Saturne",
        "sacrifice": "Cola blanc, habit blanc, bélier blanc. À donner aux renommés, grands personnages le Dimanche.",
        "plantes": "Goundjè (Arbres : Koudjè, Zèguènè)",
        "maisons": {i: f"Interprétation de Nouhou en Maison {i} selon le dictionnaire de votre dossier." for i in range(1, 17)}
    },
    "Laoussana (Alhoussein / Puella)": {
        "numero": 13, "element": "Eau", "nature": "Passé", "polarite": "Femelle",
        "psaume": "Psaume 119 (Aleph)", "verset": "Cantique 4 v.7", "sceau": "2e Pentacle de Vénus",
        "sacrifice": "Tout ce qu'on trouve sous la terre, savon, sel. À donner aux vieilles et vieux le Samedi.",
        "plantes": "Djoulasonkalani (Plantes gluantes, herbes des vieux puits, ravins, rigoles)",
        "maisons": {i: f"Interprétation de Laoussana en Maison {i} selon le dictionnaire de votre dossier." for i in range(1, 17)}
    },
    "Ousmane (Mory Zoumana / Acquisitio)": {
        "numero": 14, "element": "Terre", "nature": "Futur", "polarite": "Mâle",
        "psaume": "Psaume 23", "verset": "Psaume 23 v.1", "sceau": "3e Pentacle de Jupiter",
        "sacrifice": "Fruits secs, longs animaux. À donner à plusieurs personnes (Groupe) le Jeudi.",
        "plantes": "N'doubalé, Frogofraga (Arbres : Troubala, Dougalen, Chou Toro)",
        "maisons": {i: f"Interprétation d'Ousmane en Maison {i} selon le dictionnaire de votre dossier." for i in range(1, 17)}
    },
    "Younouss (Tontigui)": {
        "numero": 15, "element": "Air", "nature": "Futur", "polarite": "Femelle",
        "psaume": "Psaume 112", "verset": "Deutéronome 28 v.12", "sceau": "6e Pentacle de Jupiter",
        "sacrifice": "Bijoux, parures ou objets brillants. À donner aux enfants le Vendredi.",
        "plantes": "N'tomotigui, Zondjè (Arbres : Fogofogo)",
        "maisons": {i: f"Interprétation de Younouss en Maison {i} selon le dictionnaire de votre dossier." for i in range(1, 17)}
    },
    "Moussa (Djama / Populus)": {
        "numero": 16, "element": "Feu", "nature": "Présent", "polarite": "Femelle",
        "psaume": "Psaume 47", "verset": "Genèse 22 v.17", "sceau": "1er Pentacle de la Lune",
        "sacrifice": "Fruits frais, graines de céréales, animaux féminins. À donner aux religieux ou gardiens du culte le Lundi.",
        "plantes": "N'tomi, N'galama (Arbres : Tomy, Sounzoufing)",
        "maisons": {i: f"Interprétation de Moussa en Maison {i} selon le dictionnaire de votre dossier." for i in range(1, 17)}
    }
}

MAISONS_NOMS = {
    1: "Maison 1 (L'Âme, le Consultant)",
    2: "Maison 2 (La Chance, les Gains)",
    3: "Maison 3 (L'Entourage, les Frères)",
    4: "Maison 4 (Le Foyer, le Patrimoine)",
    5: "Maison 5 (Les Enfants, les Amours)",
    6: "Maison 6 (Les Maladies, les Obstacles)",
    7: "Maison 7 (Le Conjoint, les Associés)",
    8: "Maison 8 (Les Blocages, les Pertes)",
    9: "Maison 9 (Les Voyages, la Spiritualité)",
    10: "Maison 10 (Le Pouvoir, le Métier)",
    11: "Maison 11 (Les Espoirs, les Amis)",
    12: "Maison 12 (Les Ennemis cachés)",
    13: "Maison 13 (La Chambre, l'Argent présent)",
    14: "Maison 14 (L'Avenir, les Gains futurs)",
    15: "Maison 15 (Le Juge du thème)",
    16: "Maison 16 (La Sentence finale)"
}

MAPPING_SIMPLIFIE = {
    "Youssouf (Sedjou / Puer)": "Youssouf", "Adama (Letitia / La joie)": "Adama",
    "Mahamadou / Malidjou (Caput Draconis)": "Maldjou", "Idrissa (Albayaro / Albus)": "Idriss",
    "Ibrahima (Taliki / Via)": "Bourama", "Issa (Nabbi Issa / Amissio)": "Issa",
    "Oumarou (Lomara / Rubeus)": "Oumar", "Ayouba (Almangoussi / Tristitia)": "Ayouba",
    "Qala-llahou (Aboubakr Sidik / Fortuna Minor)": "Alaou Tala", "Solomana (Manssa Souleymane / Carcer)": "Solomane",
    "Badra (Badra Aliou / Conjunctio)": "Badra", "Nouhou (Nouhoum / Cauda Draconis)": "Nouhou",
    "Laoussana (Alhoussein / Puella)": "Laoussana", "Ousmane (Mory Zoumana / Acquisitio)": "Ousmane",
    "Younouss (Tontigui)": "Younouss", "Moussa (Djama / Populus)": "Moussa"
}

# =====================================================================
# 2. LOGIQUE D'ANALYSE MATRICIELLE DES ÉLÉMENTS
# =====================================================================
def interpreter_importance_element(element_str):
    if "Feu" in element_str:
        return {"icone": "🔥", "titre": "Élément FEU", "analyse": "Résolution tranchante et immédiate.", "conseil": "Agissez promptement."}
    elif "Air" in element_str:
        return {"icone": "💨", "titre": "Élément AIR", "analyse": "Situation mobile dépendante de paroles ou écrits.", "conseil": "Misez sur la communication."}
    elif "Eau" in element_str:
        return {"icone": "💧", "titre": "Élément EAU", "analyse": "Fluidité, purification et dénouement naturel.", "conseil": "Privilégiez les bains (Nassi)."}
    elif "Terre" in element_str:
        return {"icone": "🌱", "titre": "Élément TERRE", "analyse": "Ancrage solide mais soumis aux retards du temps.", "conseil": "Soyez patient."}
    return {"icone": "✨", "titre": "Équilibré", "analyse": "Forces stables.", "conseil": "Suivez le protocole."}

# =====================================================================
# 3. INTERFACE DE SÉCURITÉ
# =====================================================================
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_login():
    if st.session_state["username"] == "admin" and st.session_state["password"] == "Somadjely2026":
        st.session_state["authenticated"] = True
    else:
        st.error("❌ Accès refusé.")

if not st.session_state["authenticated"]:
    st.title("🔒 Interface Sécurisée SST")
    with st.form("login_form"):
        st.text_input("👤 Identifiant", key="username")
        st.text_input("🔑 Mot de passe", type="password", key="password")
        st.form_submit_button("Se connecter", on_click=check_login)
    st.stop()

# =====================================================================
# 4. APPLICATION PRINCIPALE
# =====================================================================
st.title("🔮 Système Informatique de Géomancie — Enseignement Somadjely")

# --- SIDEBAR : CALCULATEUR DES COPULATIONS ---
st.sidebar.header("📥 Analyse des Copulations")
parentA = st.sidebar.selectbox("Figure Parente A :", options=list(FIGURES_DB.keys()), index=0)
parentB = st.sidebar.selectbox("Figure Parente B :", options=list(FIGURES_DB.keys()), index=12)

nameA = MAPPING_SIMPLIFIE[parentA]
nameB = MAPPING_SIMPLIFIE[parentB]
set_parents = {nameA, nameB}

signe_engendre = "Aucun"
details_engendre = "Pas de rencontre secrète configurée."

# Implémentation des règles de copulation Nouhou & Badra
if set_parents == {"Youssouf", "Laoussana"}:
    signe_engendre, details_engendre = "Nouhou", "⚠️ **MÉCHANCETÉ À CAUSE D'ENFANT**"
elif set_parents == {"Adama", "Younouss"}:
    signe_engendre, details_engendre = "Nouhou", "⚠️ **MÉCHANCETÉ À CAUSE D'HÉRITAGE**"
elif set_parents == {"Bourama", "Alaou Tala"}:
    signe_engendre, details_engendre = "Nouhou", "⚠️ **MÉCHANCETÉ POUR ENFANT**"
elif set_parents == {"Oumar", "Maldjou"}:
    signe_engendre, details_engendre = "Nouhou", "⚠️ **MÉCHANCETÉ À CAUSE DE FEMME**"
elif set_parents == {"Issa", "Solomane"}:
    signe_engendre, details_engendre = "Nouhou", "⚠️ **MÉCHANCETÉ D'UN CHEF**"
elif set_parents == {"Ayouba", "Idriss"}:
    signe_engendre, details_engendre = "Nouhou", "⚠️ **MÉCHANCETÉ DANS LA FAMILLE OU FOYER**"
elif set_parents == {"Badra", "Ousmane"}:
    signe_engendre, details_engendre = "Nouhou", "⚠️ **MÉCHANCETÉ FAITE PAR UN MARABOUT OU GÉOMANCIEN**"
elif set_parents == {"Moussa", "Nouhou"}:
    signe_engendre, details_engendre = "Nouhou", "⚠️ **MÉCHANCETÉ FAITE PAR UN GROUPE DE PERSONNES**"
elif set_parents == {"Youssouf", "Younouss"}:
    signe_engendre, details_engendre = "Badra Alou", "💰 **UNE FEMME QUI A DE BON ESPOIR DE RICEHSSE**"
elif set_parents == {"Adama", "Laoussana"}:
    signe_engendre, details_engendre = "Badra Alou", "🔴 **SACRIFICE ROUGE REQUIS**"
elif set_parents == {"Maldjou", "Ayouba"}:
    signe_engendre, details_engendre = "Badra Alou", "❌ **DIFFICULTÉ POUR AVOIR DES ENFANTS (BLOCAGE)**"
elif set_parents == {"Idriss", "Oumar"}:
    signe_engendre, details_engendre = "Badra Alou", "💨 **TEMPÊTE, UN GRAND VENT VIOLENT**"
elif set_parents == {"Bourama", "Solomane"}:
    signe_engendre, details_engendre = "Badra Alou", "👶 **LA GROSSESSE**"
elif set_parents == {"Nouhou", "Ousmane"}:
    signe_engendre, details_engendre = "Badra Alou", "👑 **LA GRANDEUR ET L'HONNEUR**"
elif set_parents == {"Alaou Tala", "Issa"}:
    signe_engendre, details_engendre = "Badra Alou", "🚨 **UNE TRÈS GRAVE DIFFICULTÉ**"
elif set_parents == {"Moussa", "Badra"}:
    signe_engendre, details_engendre = "Badra Alou", "⚔️ **DESTIN DE GUERRIER, DE SOLDAT OU D'ÉLÈVES**"

st.header("🧬 Résultat de la Copulation Courante")
st.warning(f"Croisement : {nameA} ✖️ {nameB} ➡️ Enfant généré : **{signe_engendre}**\n\n*Signplication : {details_engendre}*")

st.markdown("---")

# --- NOUVEAU BLOC : CALCULATEUR DE PASSAGE DANS LES MAISONS ---
st.header("🏠 Explorateur Statistique : Passage d'une Figure en Maison")
st.write("Choisissez une figure et la maison dans laquelle elle se trouve pour extraire son interprétation textuelle.")

col_p1, col_p2 = st.columns(2)
with col_p1:
    fig_passage = st.selectbox("Sélectionnez la figure à analyser :", options=list(FIGURES_DB.keys()), key="fig_pass")
with col_p2:
    maison_passage = st.selectbox("Sélectionnez la Maison de destination :", options=list(MAISONS_NOMS.keys()), format_func=lambda x: MAISONS_NOMS[x], key="maison_pass")

if fig_passage and maison_passage:
    texte_interpretation = FIGURES_DB[fig_passage]["maisons"].get(maison_passage, "Interprétation non documentée pour cette maison.")
    st.info(f"📋 **Interprétation officielle (Enseignement PDF) :**\n\n> {texte_interpretation}")

st.markdown("---")

# --- SPÉCIFIQUE MAISON 16 ---
st.header("📊 Focus & Remèdes : Maison 16")
figure_choisie = st.selectbox("Sélectionnez la figure finale du thème (M16) :", options=list(FIGURES_DB.keys()), key="m16_box")

if figure_choisie:
    data = FIGURES_DB[figure_choisie]
    info_element = interpreter_importance_element(data['element'])
    
    tab1, tab2, tab3 = st.tabs(["🐑 Sacrifices", "✝️ Théurgie (Psaumes/Versets)", "🌿 Pharmacopée"])
    with tab1: st.write(data['sacrifice'])
    with tab2:
        st.write(f"**Psaume :** {data['psaume']}")
        st.write(f"**Verset de Verrouillage :** {data['verset']}")
        st.write(f"**Sceau Planétaire :** {data['sceau']}")
    with tab3: st.write(data['plantes'])
