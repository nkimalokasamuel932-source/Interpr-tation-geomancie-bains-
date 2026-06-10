# -*- coding: utf-8 -*-
import streamlit as st
# Base de données Théurgique et Africaine Pro
# Enrichie avec les textes intégraux des versets de Salomon pour les bains

DATA_THEURGIQUE = {
    "Bila (ou Sira)": {
        "nom_latin": "VIA (La Voie)",
        "psaume": "Psaume 23",
        "verset_reference": "Verset 3",
        "verset_texte": "Il restaure mon âme, il me conduit dans les sentiers de la justice, à cause de son nom.",
        "huile": "Menthe Poivrée",
        "moment_bain": "Matin (Lever du soleil)",
        "usage": "Ouvrir les routes, débloquer les voies sans issue, accélérer la chance."
    },
    "Tontigui (ou Gariya)": {
        "nom_latin": "POPULUS / POPA CAS (Le Peuple)",
        "psaume": "Psaume 91",
        "verset_reference": "Verset 11",
        "verset_texte": "Car il ordonnera à ses anges de te garder dans toutes tes voies.",
        "huile": "Arbre à Thé (Tea Tree)",
        "moment_bain": "Matin ou Soir (Protection continue)",
        "usage": "Protection blindée contre les complots de la foule, les jalousies et le public."
    },
    "Allou Badra (ou Aliou Badra)": {
        "nom_latin": "PUER (Le Garçon)",
        "psaume": "Psaume 144",
        "verset_reference": "Verset 1",
        "verset_texte": "Béni soit l'Éternel, mon rocher, qui exerce mes mains au combat, mes doigts à la bataille !",
        "huile": "Gingembre",
        "moment_bain": "Matin (Action / Dynamisme)",
        "usage": "Force, courage, victoire éclatante lors d'un conflit, d'une rivalité ou d'un procès."
    },
    "Massa Solomane": {
        "nom_latin": "PUELLA (La Fille)",
        "psaume": "Psaume 45",
        "verset_reference": "Verset 2",
        "verset_texte": "Des paroles pleines de charme bouillonnent dans mon cœur. Je dis : Mon œuvre est pour le roi ! Que ma langue soit comme la plume d'un habile écrivain !",
        "huile": "Géranium ou Rose de Damas",
        "moment_bain": "Matin ou avant une sortie",
        "usage": "Harmonie familiale, retour d'affection, séduction, charisme commercial et paix."
    },
    "Mavour (ou Inzan)": {
        "nom_latin": "ALBUS (Le Blanc)",
        "psaume": "Psaume 119",
        "verset_reference": "Verset 105",
        "verset_texte": "Ta parole est une lampe à mes pieds, et une lumière sur mon sentier.",
        "huile": "Encens d'Oliban",
        "moment_bain": "Soir (Méditation et clarté)",
        "usage": "Clarté mentale, intuition pour les affaires, haute protection et sagesse spirituelle."
    },
    "Lomara Blen": {
        "nom_latin": "RUBEUS (Le Rouge)",
        "psaume": "Psaume 35",
        "verset_reference": "Verset 1",
        "verset_texte": "Éternel ! Attaque ceux qui m'attaquent, combats ceux qui me combattent !",
        "huile": "Cannelle (Écorce)",
        "moment_bain": "Soir (Coucher, ne pas s'essuyer)",
        "usage": "Retour à l'envoyeur puissant, briser les mauvais sorts immédiatement (Bain de choc)."
    },
    "Goundo (ou Tchebissaba)": {
        "nom_latin": "AMISSIO (La Perte)",
        "psaume": "Psaume 51",
        "verset_reference": "Verset 12",
        "verset_texte": "Ô Dieu ! crée en moi un cœur pur, renouvelle en moi un esprit bien disposé.",
        "huile": "Lavande Vraie",
        "moment_bain": "Soir (Purification)",
        "usage": "Purification des blocages internes, détachement des erreurs du passé, effacement des dettes."
    },
    "Kalalahou": {
        "nom_latin": "CONIUNCTIO (L'Union)",
        "psaume": "Psaume 133",
        "verset_reference": "Verset 1",
        "verset_texte": "Voici, qu'il est agréable, qu'il est doux pour des frères de demeurer ensemble !",
        "huile": "Ylang-Ylang",
        "moment_bain": "Matin (Alliances et contrats)",
        "usage": "Sceller des contrats de partenariat, accords commerciaux solides, unions ou mariages."
    },
    "Yousouf (ou Asidika)": {
        "nom_latin": "FORTUNA MAJOR (La Grande Fortune)",
        "psaume": "Psaume 20",
        "verset_reference": "Verset 5",
        "verset_texte": "Qu'il te donne ce que ton cœur désire, et qu'il accomplisse tous tes desseins !",
        "huile": "Laurier Noble",
        "moment_bain": "Matin (Bain de Royauté)",
        "usage": "Bain de Royauté. Grande chance financière, succès total aux examens, jeux et concours."
    },
    "Mahamadou (ou Moussa)": {
        "nom_latin": "FORTUNA MINOR (La Petite Fortune)",
        "psaume": "Psaume 4",
        "verset_reference": "Verset 7",
        "verset_texte": "Plusieurs disent : Qui nous fera voir le bonheur ? Fais lever sur nous la lumière de ta face, ô Éternel !",
        "huile": "Orange Douce ou Bergamote",
        "moment_bain": "Matin",
        "usage": "Succès rapide et brillant, protection discrète au quotidien, dynamisme."
    },
    "Idrissa": {
        "nom_latin": "ACQUISITIO / ARQUISITIO (Le Gain)",
        "psaume": "Psaume 112",
        "verset_reference": "Verset 3",
        "verset_texte": "Il a dans sa maison bien-être et richesse, et sa justice subsiste à jamais.",
        "huile": "Patchouli",
        "moment_bain": "Matin (Attraction commerciale)",
        "usage": "Attraction financière magnétique, prospérité dans le commerce et rentrées d'argent."
    },
    "Mangossi": {
        "nom_latin": "CARCER (La Prison)",
        "psaume": "Psaume 142",
        "verset_reference": "Verset 8",
        "verset_texte": "Tire mon âme de sa prison, afin que je célèbre ton nom ! Les justes viendront m'entourer, quand tu m'auras fait du bien.",
        "huile": "Cyprès de Provence",
        "moment_bain": "Soir (Libération)",
        "usage": "Sortir des dettes étouffantes, clore définitivement un problème, briser les blocages juridiques."
    },
    "Nouhou-Koro": {
        "nom_latin": "TRISTITIA / PRISTITIA (La Tristesse)",
        "psaume": "Psaume 30",
        "verset_reference": "Verset 12",
        "verset_texte": "Tu as changé mon deuil en allégresse, tu as délié mon sac, et tu m'as ceint de joie.",
        "huile": "Citronnelle ou Eucalyptus",
        "moment_bain": "Soir (Déracinement / Consolidation)",
        "usage": "Bain de consolidation des acquis, ancrage spirituel, protection de la maison et déracinement des tristesses."
    },
    "Mori-Zoumana": {
        "nom_latin": "LAETITIA (La Joie)",
        "psaume": "Psaume 100",
        "verset_reference": "Verset 2",
        "verset_texte": "Servez l'Éternel avec joie, venez avec allégresse en sa présence !",
        "huile": "Pamplemousse",
        "moment_bain": "Matin (Ouverture sociale)",
        "usage": "Attirer la bonne humeur, la fête, les faveurs des personnes influentes et la chance spontanée."
    },
    "Adama": {
        "nom_latin": "CAPUT DRACONIS (La Tête de Dragon)",
        "psaume": "Psaume 8",
        "verset_reference": "Verset 6",
        "verset_texte": "Tu lui as donné l'empire sur les œuvres de tes mains, tu as tout mis sous ses pieds.",
        "huile": "Cèdre de l'Atlas",
        "moment_bain": "Matin (Élévation / Autorité)",
        "usage": "Élévation sociale, prise de poste de direction, charisme de leader et initiation spirituelle."
    },
    "Adama-Lomara": {
        "nom_latin": "CAUDA DRACONIS (La Queue de Dragon)",
        "psaume": "Psaume 18",
        "verset_reference": "Verset 38",
        "verset_texte": "Je les brise, et ils ne peuvent se relever ; ils tombent sous mes pieds.",
        "huile": "Clou de Girofle",
        "moment_bain": "Soir (Coupure nette, ne pas s'essuyer)",
        "usage": "Bain de coupure radicale. Nettoyage karmique, chasser un ennemi tenace et finir un cycle négatif."
    }
}

# --- TEXTES TEXTES SALOMONIQUES BIBLIQUES DE CONSÉCRATION ---
# À utiliser pour consacrer et réveiller l'eau du bain avant d'y ajouter les huiles et les versets spécifiques.

TEXTES_SALOMONIQUES = {
    "Sagesse_Et_Appel_De_Salomon": (
        "1 Rois 3:9 - 'Accorde donc à ton serviteur un cœur intelligent pour juger ton peuple, "
        "pour discerner le bien du mal ! Car qui pourrait juger ton peuple, ce peuple si nombreux ?' "
        "[Utilisé pour activer l'intelligence et la direction divine avant le bain]."
    ),
    "Priere_Royale_De_Salomon": (
        "2 Chroniques 1:12 - 'La sagesse et l'intelligence te sont accordées. "
        "Je te donnerai en outre des richesses, des biens et de la gloire, "
        "comme n'en a jamais eu aucun roi avant toi, et comme n'en aura aucun après toi.' "
        "[Idéal pour oindre et charger les bains de type Yousouf, Idrissa ou Adama]."
    ),
    "Consecration_De_L_Eau": (
        "Psaume 29:3-4 - 'La voix de l'Éternel retentit sur les eaux, "
        "Le Dieu de gloire fait tonner le tonnerre, L'Éternel est sur les grandes eaux. "
        "La voix de l'Éternel est puissante, La voix de l'Éternel est majestueuse.' "
        "[À réciter en remuant l'eau du bain 3 fois avec la main droite pour l'allumer spirituellement]."
    )
}
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
    # ==============================================================================
# BASE DE DONNÉES THÉURGIQUE & GÉOMANTIQUE ALIGNÉE (SYNCHRONISATION DES SIGNIFICATIONS)
# ==============================================================================

DATA_THEURGIQUE = {
    "Adama": {
        "nom_africain_synonyme": "Mahadi",
        "nom_latin": "CAPUT DRACONIS (La Tête de Dragon)",
        "nature": "Bénéfique",
        "signification": "Succès, prospérité, accomplissement",
        "domaines": "Argent, carrière, projets aboutis",
        "psaume": "Psaume 8",
        "verset_reference": "Verset 6",
        "verset_texte": "Tu lui as donné l'empire sur les œuvres de tes mains, tu as tout mis sous ses pieds.",
        "huile": "Cèdre de l'Atlas",
        "moment_bain": "Matin (Élévation / Autorité)",
        "usage": "Élévation sociale, prise de poste de direction, charisme de leader et initiation spirituelle."
    },
    "Mori-Zoumana": {
        "nom_africain_synonyme": "Talki",
        "nom_latin": "LAETITIA (La Joie)",
        "nature": "Bénéfique",
        "signification": "Chance, bénédiction, bonheur futur",
        "domaines": "Spiritualité, destin, événements heureux",
        "psaume": "Psaume 100",
        "verset_reference": "Verset 2",
        "verset_texte": "Servez l'Éternel avec joie, venez avec allégresse en sa présence !",
        "huile": "Pamplemousse",
        "moment_bain": "Matin (Ouverture sociale)",
        "usage": "Attirer la bonne humeur, la fête, les faveurs des personnes influentes et la chance spontanée."
    },
    "Massa Solomane": {
        "nom_africain_synonyme": "Faventina",
        "nom_latin": "PUELLA (La Fille)",
        "nature": "Bénéfique",
        "signification": "Espoir, amour, faveur sociale",
        "domaines": "Relations, diplomatie, réputation",
        "psaume": "Psaume 45",
        "verset_reference": "Verset 2",
        "verset_texte": "Des paroles pleines de charme bouillonnent dans mon cœur. Je dis : Mon œuvre est pour le roi ! Que ma langue soit comme la plume d'un habile écrivain !",
        "huile": "Géranium ou Rose de Damas",
        "moment_bain": "Matin ou avant une sortie",
        "usage": "Harmonie familiale, retour d'affection, séduction, charisme commercial et paix."
    },
    "Allou Badra (ou Aliou Badra)": {
        "nom_africain_synonyme": "Diafan_Almamy",
        "nom_latin": "PUER (Le Garçon)",
        "nature": "Plutôt Bénéfique (ambivalent)",
        "signification": "Jeunesse, énergie, courage, action",
        "domaines": "Action, aventure, compétition, défense",
        "psaume": "Psaume 144",
        "verset_reference": "Verset 1",
        "verset_texte": "Béni soit l'Éternel, mon rocher, qui exerce mes mains au combat, mes doigts à la bataille !",
        "huile": "Gingembre",
        "moment_bain": "Matin (Action / Dynamisme)",
        "usage": "Force, courage, victoire éclatante lors d'un conflit, d'une rivalité ou d'un procès."
    },
    "Idrissa": {
        "nom_africain_synonyme": "Soumana",
        "nom_latin": "ACQUISITIO / ARQUISITIO (Le Gain)",
        "nature": "Bénéfique (surtout matériel)",
        "signification": "Gain, acquisition, réussite matérielle",
        "domaines": "Finance, commerce, possession",
        "psaume": "Psaume 112",
        "verset_reference": "Verset 3",
        "verset_texte": "Il a dans sa maison bien-être et richesse, et sa justice subsiste à jamais.",
        "huile": "Patchouli",
        "moment_bain": "Matin (Attraction commerciale)",
        "usage": "Attraction financière magnétique, prospérité dans le commerce et rentrées d'argent."
    },
    "Mahamadou (ou Moussa)": {
        "nom_africain_synonyme": "Moussa",
        "nom_latin": "FORTUNA MINOR (La Petite Fortune)",
        "nature": "Neutre",
        "signification": "Soutien collectif, attente, popularité",
        "domaines": "Opinions publiques, soutien social, élections",
        "psaume": "Psaume 4",
        "verset_reference": "Verset 7",
        "verset_texte": "Plusieurs disent : Qui nous fera voir le bonheur ? Fais lever sur nous la lumière de ta face, ô Éternel !",
        "huile": "Orange Douce ou Bergamote",
        "moment_bain": "Matin",
        "usage": "Succès rapide et brillant, protection discrète au quotidien, dynamisme."
    },
    "Kalalahou": {
        "nom_africain_synonyme": "Ali_Badara",
        "nom_latin": "CONIUNCTIO (L'Union)",
        "nature": "Neutre à Bénéfique",
        "signification": "Réunion, rencontre, coopération",
        "domaines": "Relations, partenariats, collaborations",
        "psaume": "Psaume 133",
        "verset_reference": "Verset 1",
        "verset_texte": "Voici, qu'il est agréable, qu'il est doux pour des frères de demeurer ensemble !",
        "huile": "Ylang-Ylang",
        "moment_bain": "Matin (Alliances et contrats)",
        "usage": "Sceller des contrats de partenariat, accords commerciaux solides, unions ou mariages."
    },
    "Mavour (ou Inzan)": {
        "nom_africain_synonyme": "Bayada",
        "nom_latin": "ALBUS (Le Blanc)",
        "nature": "Neutre à Bénéfique",
        "signification": "Sagesse, paix, clarté mentale",
        "domaines": "Négociations, calme, gestion raisonnable",
        "psaume": "Psaume 119",
        "verset_reference": "Verset 105",
        "verset_texte": "Ta parole est une lampe à mes pieds, et une lumière sur mon sentier.",
        "huile": "Encens d'Oliban",
        "moment_bain": "Soir (Méditation et clarté)",
        "usage": "Clarté mentale, intuition pour les affaires, haute protection et sagesse spirituelle."
    },
    "Tontigui (ou Gariya)": {
        "nom_africain_synonyme": "Tontigui",
        "nom_latin": "POPULUS / POPA CAS (Le Peuple)",
        "nature": "Neutre à Bénéfique",
        "signification": "Douceur, harmonie, séduction",
        "domaines": "Relations amoureuses, diplomatie, art",
        "psaume": "Psaume 91",
        "verset_reference": "Verset 11",
        "verset_texte": "Car il ordonnera à ses anges de te garder dans toutes tes voies.",
        "huile": "Arbre à Thé (Tea Tree)",
        "moment_bain": "Matin ou Soir (Protection continue)",
        "usage": "Protection blindée contre les complots de la foule, les jalousies et le public."
    },
    "Yousouf (ou Asidika)": {
        "nom_africain_synonyme": "Nouhou",
        "nom_latin": "FORTUNA MAJOR (La Grande Fortune)",
        "nature": "Bénéfique",
        "signification": "Grande chance, succès durable",
        "domaines": "Opportunités, destin, réussite stable",
        "psaume": "Psaume 20",
        "verset_reference": "Verset 5",
        "verset_texte": "Qu'il te donne ce que ton cœur désire, et qu'il accomplisse tous tes desseins !",
        "huile": "Laurier Noble",
        "moment_bain": "Matin (Bain de Royauté)",
        "usage": "Bain de Royauté. Grande chance financière, succès total aux examens, jeux et concours."
    },
    "Bila (ou Sira)": {
        "nom_africain_synonyme": "Allahou_Tallah",
        "nom_latin": "VIA (La Voie)",
        "nature": "Neutre à Mauvais",
        "signification": "Petite chance, voyage, opportunité fugace",
        "domaines": "Voyages, opportunités passagères",
        "psaume": "Psaume 23",
        "verset_reference": "Verset 3",
        "verset_texte": "Il restaure mon âme, il me conduit dans les sentiers de la justice, à cause de son nom.",
        "huile": "Menthe Poivrée",
        "moment_bain": "Matin (Lever du soleil)",
        "usage": "Ouvrir les routes, débloquer les voies sans issue, accélérer la chance."
    },
    "Mangossi": {
        "nom_africain_synonyme": "Massa_Solo",
        "nom_latin": "CARCER (La Prison)",
        "nature": "Mauvais",
        "signification": "Enfermement, isolement, blocage",
        "domaines": "Contrainte, procédure juridique, stagnation",
        "psaume": "Psaume 142",
        "verset_reference": "Verset 8",
        "verset_texte": "Tire mon âme de sa prison, afin que je célèbre ton nom ! Les justes viendront m'entourer, quand tu m'auras fait du bien.",
        "huile": "Cyprès de Provence",
        "moment_bain": "Soir (Libération)",
        "usage": "Sortir des dettes étouffantes, clore définitivement un problème, briser les blocages juridiques."
    },
    "Goundo (ou Tchebissaba)": {
        "nom_africain_synonyme": "Ngansa",
        "nom_latin": "AMISSIO (La Perte)",
        "nature": "Mauvais",
        "signification": "Perte, manque, séparation",
        "domaines": "Argent, amour, possession",
        "psaume": "Psaume 51",
        "verset_reference": "Verset 12",
        "verset_texte": "Ô Dieu ! crée en moi un cœur pur, renouvelle en moi un esprit bien disposé.",
        "huile": "Lavande Vraie",
        "moment_bain": "Soir (Purification)",
        "usage": "Purification des blocages internes, détachement des erreurs du passé, effacement des dettes."
    },
    "Nouhou-Koro": {
        "nom_africain_synonyme": "Mangoussi",
        "nom_latin": "TRISTITIA / PRISTITIA (La Tristesse)",
        "nature": "Mauvais",
        "signification": "Tristesse, chagrin, obstacles",
        "domaines": "Santé mentale, projets bloqués, mauvaises nouvelles",
        "psaume": "Psaume 30",
        "verset_reference": "Verset 12",
        "verset_texte": "Tu as changé mon deuil en allégresse, tu as délié mon sac, et tu m'as ceint de joie.",
        "huile": "Citronnelle ou Eucalyptus",
        "moment_bain": "Soir (Déracinement / Consolidation)",
        "usage": "Bain de consolidation des acquis, ancrage spirituel, protection de la maison et déracinement des tristesses."
    },
    "Adama-Lomara": {
        "nom_africain_synonyme": "Lahoussana",
        "nom_latin": "CAUDA DRACONIS (La Queue de Dragon)",
        "nature": "Très Mauvais",
        "signification": "Fin tragique, abandon, conclusion négative",
        "domaines": "Projets avortés, ruptures, fin dramatique",
        "psaume": "Psaume 18",
        "verset_reference": "Verset 38",
        "verset_texte": "Je les brise, et ils ne peuvent se relever ; ils tombent sous mes pieds.",
        "huile": "Clou de Girofle",
        "moment_bain": "Soir (Coupure nette, ne pas s'essuyer)",
        "usage": "Bain de coupure radicale. Nettoyage karmique, chasser un ennemi tenace et finir un cycle négatif."
    },
    "Lomara Blen": {
        "nom_africain_synonyme": "Lomara",
        "nom_latin": "RUBEUS (Le Rouge)",
        "nature": "Mauvais",
        "signification": "Violence, conflit direct, destruction par le feu",
        "domaines": "Guerre, litiges, blocages physiques violents",
        "psaume": "Psaume 35",
        "verset_reference": "Verset 1",
        "verset_texte": "Éternel ! Attaque ceux qui m'attaquent, combats ceux qui me combattent !",
        "huile": "Cannelle (Écorce)",
        "moment_bain": "Soir (Coucher, ne pas s'essuyer)",
        "usage": "Retour à l'envoyeur puissant, briser les mauvais sorts immédiatement (Bain de choc)."
    }
}

SIGNIFICATION_MAISONS = {
    1: "Maison de l'Auteur (Le Consultant, son état présent, ses pensées)",
    2: "Maison des Biens (Finances, commerce, possessions matérielles)",
    3: "Maison de l'Entourage (Proches, frères, petites démarches, nouvelles)",
    4: "Maison du Patrimoine (Foyer, le père, la maison, dénouement des affaires)",
    5: "Maison des Enfants (Amours, plaisirs, chance pure, créativité)",
    6: "Maison des Malaises (Santé, obstacles subis, travail quotidien)",
    7: "Maison de l'Union (Conjoint, partenariats, contrats, adversaire connu)",
    8: "Maison de la Mort (Transformations, crises, héritages, capitaux externes)",
    9: "Maison des Voyages (Spiritualité, l'étranger, études, grands projets)",
    10: "Maison du Pouvoir (Carrière, honneurs, position sociale, autorité)",
    11: "Maison des Appuis (Soutiens, amis fidèles, espoirs secrets)",
    12: "Maison des Obstacles (Ennemis cachés, épreuves secrètes, blocages occultes)",
    13: "Maison du Résultat (Conclusion directe, ce qui se matérialise)",
    14: "Maison des Conséquences (Le futur proche, ce qui se développe après)",
    15: "Maison de la Clarté (Le Témoin du thème, l'ambiance générale)",
    16: "Maison de la Sentence (Le Décret final de la consultation)"
}


# ==============================================================================
# ESPACE DE SAISIE DU THÈME EN MOUVEMENT (LIÉ À VOTRE TIRAGE)
# ==============================================================================

THEME_DYNAMIQUE = {
    1: "Adama",          # Mahadi bouge en M1
    2: "Idrissa",        # Soumana bouge en M2
    3: "Mahamadou",      # Moussa bouge en M3
    4: "Tontigui",       # Tontigui bouge en M4
    5: "Bila",           # Allahou_Tallah bouge en M5
    6: "Mavour",         # Bayada bouge en M6
    7: "Lomara Blen",    # Lomara bouge en M7
    8: "Yousouf",        # Nouhou bouge en M8
    9: "Massa Solomane", # Faventina bouge en M9
    10: "Idrissa",       # Soumana bouge en M10
    11: "Kalalahou",     # Ali_Badara bouge en M11
    12: "Mangossi",      # Massa_Solo bouge en M12
    13: "Mori-Zoumana",  # Talki bouge en M13
    14: "Adama-Lomara",  # Lahoussana bouge en M14
    15: "Goundo",        # Ngansa bouge en M15
    16: "Nouhou-Koro"    # Mangoussi bouge en M16
}


# ==============================================================================
# MOTEUR D'INTERPRÉTATION STRICTE BASÉ SUR VOS SIGNIFICATIONS
# ==============================================================================

def interpreter_mouvement_geomantique(theme):
    print("=" * 90)
    print(" 🔮 RAPPORT DIVINATOIRE STRUCTURÉ SUR VOS SIGNIFICATIONS GÉOMANTIQUES")
    print("=" * 90)
    
    for maison, nom_fig in theme.items():
        clef_exacte = None
        for clef in DATA_THEURGIQUE.keys():
            if nom_fig.lower() in clef.lower():
                clef_exacte = clef
                break
                
        if not clef_exacte:
            continue
            
        f_data = DATA_THEURGIQUE[clef_exacte]
        desc_maison = SIGNIFICATION_MAISONS[maison]
        
        print(f"\n🏠 MAISON {maison} : {desc_maison}")
        print(f"   ▶ Figure   : {clef_exacte} (Nom géomantique : {f_data['nom_africain_synonyme']})")
        print(f"   ▶ Nature   : [{f_data['nature'].upper()}]")
        print(f"   ▶ Message  : {f_data['signification']} -> S'applique directement au domaine : {f_data['domaines']}")
        
        # Application théurgique corrective
        if "Mauvais" in f_data["nature"]:
            print(f"   ❌ IMPACT  : Blocage identifié. Cette figure altère la maison.")
            print(f"   🛁 SOLUTION: Faire le bain avec l'huile de {f_data['huile']} ({f_data['moment_bain']}).")
            print(f"   📜 VERSET  : {f_data['psaume']}, {f_data['verset_reference']} : \"{f_data['verset_texte']}\"")
        else:
            print(f"   ✨ IMPACT  : Courant d'ouverture. Énergie constructive présente.")
            print(f"   🛁 SCELLAGE: Soutenir le mouvement avec le bain vibratoire : {f_data['usage']}")
            print(f"   📜 VERSET  : \"{f_data['verset_texte']}\"")
        print("-" * 90)

if __name__ == "__main__":
    interpreter_mouvement_geomantique(THEME_DYNAMIQUE)

st.markdown("---")
st.caption("SST Informatique — Version Générative complète à 16 Maisons. Tous droits réservés. Édit 2026.")
