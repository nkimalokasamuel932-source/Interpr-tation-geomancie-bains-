# -*- coding: utf-8 -*-
import streamlit as st

# =====================================================================
# 1. DICTIONNAIRE UNIQUE ET INTEGRAL DES 16 FIGURES (CODES ET MAISONS COMPLETS)
# =====================================================================
# Strates : [Tête, Poitrine, Ventre, Pied] | 1 = Impair (un point), 2 = Pair (deux points)
FIGURES_DB = {
    "Youssouf (Sedjou / Puer)": {
        "code": [1, 1, 2, 1], "numero": 1, "element": "Feu", "nature": "Passé", "polarite": "Comté Mâle",
        "jour": "Mardi", "psaume": "Psaume 35", "verset": "Exode 15 v.3", "sceau": "2e Pentacle de Mars",
        "sacrifice": "Donner 10 pièces d'argent ou 10 cauris ; ou un coq 'Manan dounoun' ; ou quelque chose de rouge (poulet, colas).",
        "plantes": "Zaban, Balanzan, Poudre de fusil (Arbres : Djala, N'zèrènidjè, Djatiguifaga)",
        "maisons": {
            1: "Beaucoup de bonheur en vue ; Personne aimée dans son milieu ; Trahison dans l'affaire en cours.",
            2: "Perte de richesses (argent...) ; Difficultés dans la chance.",
            3: "Brouilles dans les affaires ; Trahison ou mésentente en vue dans la maison ou entre frères ou/sœurs.",
            4: "Avarice pure entre eaux ; Perte de richesse (argent...) ; Procès difficile en vue ; Trahison dans la maison paternelle ; Avarice entre frères.",
            5: "Chance d'avoir un enfant ; Nouvelle mensongère ; Perte de nouvelle.",
            6: "Survenue d'une maladie difficile ou d'une colère ; Augmentation de la douleur ou de la colère ; La chose perdue ne sera plus retrouvée.",
            7: "Difficulté d'avoir satisfaction dans une entreprise ou une union ; Difficulté ou/et trahison dans l'union.",
            8: "Annonce la mort de quelqu'un ou de quelque chose, d'une idée ; Annonce l'emprisonnement ou la fermeture.",
            9: "Voyage désagréable pour cause de trahison.",
            10: "Acquisition du pouvoir pour le chercheur. Sinon : annonce une trahison ou des propos malveillants chez les personnes haut placées.",
            11: "Déception ou traitrise causées par un ou des ami(s).",
            12: "Prolifération des ennemis et leur trahison ; Perte ou destruction.",
            13: "Difficulté de déplacement pour le voyageur ; Trahison de l'entourage immédiat ; Annonce une femme amoureuse d'un homme.",
            14: "Annonce un gain d'argent ; Annonce qu'on va retrouver quelque chose qui était perdue ou retirée ; Avantages venant des femmes.",
            15: "Interdiction classique de mouvement de M1 vers M7/M15 pour cette figure. Trahison latente dans le résultat.",
            16: "Annonce la guérison du malade ; Pour une autre affaire : trahison au bout de l'affaire."
        }
    },
    "Adama (Letitia / La joie)": {
        "code": [1, 2, 2, 2], "numero": 2, "element": "Feu", "nature": "Passé", "polarite": "Comté Mâle",
        "jour": "Jeudi", "psaume": "Psaume 4", "verset": "Néhémie 8 v.10", "sceau": "2e Pentacle de Jupiter",
        "sacrifice": "Donner 100 colas blanches avec la viande d'un mouton 'dadiè sagadjigui' ou 12 colas ou une paire de chaussures.",
        "plantes": "Frogofraga, N'gouna, Sérétoro (Arbres : Sana, Gounan)",
        "maisons": {
            1: "Réalisation des vœux et des projets ; Libéralisme d'idées ; Acquisition de chance en vue, élévation promise ; Longue vie.",
            2: "Bon travail fructifiant, chance ; Problèmes bientôt résolus ; Bien en péril sauvé ; Satisfaction amenée par l'argent.",
            3: "Entente cordiale entre frères et sœurs ('badénya diya') ; Chance grâce à un proche ; Nouvelles réjouissantes.",
            4: "Foyer agréable, famille unie ; Acquisition de bien (argent...) avec un parent ou dans la famille paternelle ; Beaux héritages.",
            5: "Nouvelle réjouissante ; Chance d'avoir une fille ; Chance grâce à un enfant ; Amour heureux, coup de foudre.",
            6: "Emploi peu important mais amenant le bonheur ; Bonne santé ; Colère due à une difficulté passagère mais joie finale.",
            7: "Excellent mariage réussi ; Union de bon augure ; Réalisation rapide des ambitions financières malgré un léger retard.",
            8: "Difficultés initiales à propos de la chance financière mais réalisation après de grosses épreuves ; Gain suite à une rupture.",
            9: "Chance de trouver un bon travail ; Arrivée d'une nouvelle chance ; Voyage agréable ; Spiritualité favorisée.",
            10: "Chance, victoire (surtout pour une personne haut placée) ; Réussite professionnelle (commerce) ; Élévation sociale, paix.",
            11: "Appuis certains ('jigimafa') ; Amis intéressés par les arts ; Mariage précoce ; Propos mielleux.",
            12: "Méchanceté sur les lieux de travail ; Colère due à la malchance, mais la fin est heureuse ; Victoire assurée sur les ennemis.",
            13: "Leçon apprise du passé ; Changement positif ; Voyage bénéfique ; Acquisition de travail dans les environs.",
            14: "Acquisition de biens ; Les espoirs et les vœux ont toutes les chances de se réaliser.",
            15: "Synthèse et dénouement très positifs. Harmonie retrouvée dans l'ensemble de la consultation.",
            16: "Bonne finalité de l'entreprise, aboutissant à des situations de chance et de bonheur seulement."
        }
    },
    "Mahamadou / Malidjou (Caput Draconis)": {
        "code": [2, 1, 1, 1], "numero": 3, "element": "Air", "nature": "Futur", "polarite": "Femelle",
        "jour": "Jeudi", "psaume": "Psaume 128", "verset": "Exode 20 v.12", "sceau": "1er Pentacle de la Terre",
        "sacrifice": "Sacrifier et donner 7 tas d'arachides, des céréales, ou du cola blessé ('moroudatô woro').",
        "plantes": "Arbres qui poussent sur colline ou toile, Djoun (Arbres : Djoulassounkalani, Sébé)",
        "maisons": {
            1: "Réalisation des vœux ; Venue d'une personne étrangère (belle-famille ou femme) ; Ambition, éloquence.",
            2: "Chance et relation de parenté ; Acquisition d'un bon travail avec la mère ou un parent ; Multiplication des gains.",
            3: "Bonheur venant d'un frère/sœur ou belle-famille ; Idée juste ; Beau fixe pour les voyages.",
            4: "Réjouissance dans la famille ; Chance d'avoir un garçon ; Logement accueillant, stabilité ; Héritage.",
            5: "Chance d'avoir une fille ; Victoire en procès ; Fiancé/Amour ; Enfants satisfaisants.",
            6: "Maladie ou colère de la mère ou de sa famille ; Abandon temporaire de travail ; Petit souci de santé.",
            7: "Mariage avec une personne apparentée (bonheur) ; Fin des peurs ; Accord positif ; Victoire en procès.",
            8: "Mort ou emprisonnement d'un proche maternel ; Conjoint aisé ; Contrat avantageux.",
            9: "L'échec se transforme en succès ; Arrivée de la mère ; Initiation ou engagement communautaire.",
            10: "Ascension sociale, prestige ; Amitié avec un haut placé ; Sens aigu de la justice.",
            11: "Espoirs et appuis dus à un parent ou venant de la mère ; Amitié sûre et profitable.",
            12: "Méfiez-vous de l'eau (risque d'amnésie, méningite) ; Méchanceté des germains ('fadénmaw') ; Ennemis sans danger.",
            13: "Réalisation dans un court délai ; Venue de la mère/sœur dans la chambre ; Changement positif.",
            14: "Réussite à partir d'une mauvaise affaire ; Le bien détruit sera sauvé ; Enrichissement général.",
            15: "Résolution intermédiaire guidée par l'influence et le conseil des parents maternels.",
            16: "Bonne finalité, bonheur, élévation et stabilisation de la position demandée."
        }
    },
    "Idrissa (Albayaro / Albus)": {
        "code": [2, 2, 1, 2], "numero": 4, "element": "Eau", "nature": "Futur", "polarite": "Comté Mâle",
        "jour": "Vendredi", "psaume": "Psaume 119 (Beth)", "verset": "Isaïe 1 v.18", "sceau": "2e Pentacle de Mercure",
        "sacrifice": "Du poisson frais à manger en mixité ; ou du lait frais + 1 cola blanche à croquer.",
        "plantes": "N'gokou, tous les arbres qui vivent sur les fleuves (Arbres : Dougalén)",
        "maisons": {
            1: "Caractère franc, naïveté ; Tempérament calme, mystique ; Chance rapide d'argent propre.",
            2: "Saine situation financière ; Illumination de la chance après une période noire ; Bénéfices honnêtes.",
            3: "Ouverture de la chance commerciale ; Entente entre germains de même mère ; Voyages décevants.",
            4: "Bonté venant des ennemis ; Biens d'héritage en vue ; Retour d'une ancienne maladie ; Habitation paisible.",
            5: "Chance d'avoir un enfant pour personne dite 'stérile' ; Risque d'avortement si grossesse ; Liaison chaste.",
            6: "Maladie ou malade en famille ; Personne en colère ; Bon pour le voyageur ; Emploi stable.",
            7: "Bonne entente de couple ; Femme enceinte ; Attention aux ingérences extérieures ; Bon mariage.",
            8: "Mort ou emprisonnement du père ou du frère ; Association extérieure intéressante ; Augmentation de gain.",
            9: "Hésitations à prendre la route, voyage paisible ; Risque de pluie ; Opinions sereines.",
            10: "Situation sociale correcte, modeste et sûre ; Bon pour l'ascension ; Problèmes pour la mère.",
            11: "Relations amicales fidèles mais instables ; Acquisition de charme ; Simple médisance.",
            12: "Méchanceté des ennemis (penseurs/artistes) ; Procès persistant ; Risque d'accident/maladie des yeux.",
            13: "Femme de bon augure au foyer ; Parent étranger installé confortablement ; Recherche spirituelle.",
            14: "Ascension, succès et gains importants ; Évolution hautement favorable pour l'avenir.",
            15: "Résolution lucide et paisible, éclaircissement spirituel de la situation obscure.",
            16: "Annonce la réussite, la paix intérieure et le bonheur pour la finalité de l'entreprise."
        }
    },
    "Ibrahima (Taliki / Via)": {
        "code": [1, 1, 1, 1], "numero": 5, "element": "Eau", "nature": "Présent", "polarite": "Comté Mâle",
        "jour": "Lundi", "psaume": "Psaume 120", "verset": "Psaume 121 v.8", "sceau": "5e Pentacle de la Lune",
        "sacrifice": "Un mouton 'lolosaga' ou 'kirikêsaga' ; ou de la viande de bœuf de brousse ; ou 4 colas blanches.",
        "plantes": "Zondjè, arbres poussant au bord des sources d'eau (Arbres : Tièkala, Zongnè)",
        "maisons": {
            1: "Annonce enfant (grossesse) ; Projets et espoirs ; L'intérêt s'estompe vite ; Nervosité.",
            2: "Chance d'avoir un garçon ; Gain grâce à un enfant ; Vente, achat, dépenses ; Désillusions.",
            3: "Diminution des 'balimaw' ; Augmentation des bons voisins ; Longue vie ; Démarches d'affaires.",
            4: "Nouveau voisin ; Résolution d'un problème difficile ; Déménagement, instabilité.",
            5: "Chance d'un enfant bien bâti qui comblera de joie ; Timides rentrées d'argent ; Liaison instable.",
            6: "Colère ou maladie d'un enfant ; Peines causées par un tyran ; Serpent ou danger sur la route ; Voyage forcé sans profit.",
            7: "Grossesse pour femme mariée ; Mauvais augure pour le mariage ou le choix du partenaire ; Retards.",
            8: "Mort d'un enfant ; Changement négatif de situation ; Difficulté d'héritage ; Signe de l'au-delà.",
            9: "Venue de l'enfant d'un voyage ; Nouvelle sûre ; Départ déterminant ; Curiosité.",
            10: "Succès grâce à une haute personnalité ; Mauvais pour l'ascension brute ; Effort à répéter.",
            11: "Enfant comblant de joie ; Appuis bienfaisants après angoisses ; Amis sans grands moyens.",
            12: "L'enfant devient l'ennemi ; Ennemis de milieux défavorisés ; Fin des ennuis matériels ; Risque d'accident.",
            13: "Grande joie relative à l'enfant ; Stabilité de l'enfant dans la famille ; Voyage bénéfique.",
            14: "Enfant et beaucoup de richesses ; Nouveau richard ; Climat financier positif.",
            15: "Quiproquo relatif à un enfant ; Peurs et angoisses ; Dénouement promis malgré les embûches.",
            16: "Bonheur dû à un enfant à l'extérieur ; Risque de fin humiliante si on croise les bras."
        }
    },
    "Issa (Nabbi Issa / Amissio)": {
        "code": [1, 2, 1, 2], "numero": 6, "element": "Eau", "nature": "Passé", "polarite": "Comté Mâle",
        "jour": "Mercredi", "psaume": "Psaume 102", "verset": "Joël 2 v.25", "sceau": "5e Pentacle de Vénus",
        "sacrifice": "Un foulard 'dissa' + 6 colas blanches ; ou une pintade tachetée à une personne 'diminto' ; ou du fonio.",
        "plantes": "N'gagnaka, Niama, Chi (Arbres : Sourou N'tomo)",
        "maisons": {
            1: "Mauvaise augure, échec et mat ; Personne malade ou en colère ; Durée courte ; Fatigue morale et physique.",
            2: "Perte d'argent, dépenses injustifiées ; Pauvreté, perte de travail ; Difficultés croissantes.",
            3: "Trahison, affaire néfaste ; Escroc parmi les proches ; Amitié qui disparaît ; Courrier égaré.",
            4: "Maladie, colère ou dureté (karôgèlèya) du père ; Désunion, adultère désastreux ; Dilapidation.",
            5: "Maladie de l'enfant ou du rival ; Avortement ; Rupture amoureuse ; Transactions non rentables.",
            6: "Souffrance pour le malade (sans mort obligatoire) ; Menace de chômage ; Perte d'animaux.",
            7: "Maladie ou colère du conjoint ou de l'associé ; Mariage qui périclite ; Divorce, procès perdu.",
            8: "Très mauvais augure pour le malade ; Perte d'héritage ; Veuvage, longue détention.",
            9: "Venue d'un malade ou d'une colère ; Mauvais voyage, perte au loin ; Régression.",
            10: "Échec, mauvais procès chez les chefs (famaw) ; Ruine, perte de situation ; Danger pour la mère.",
            11: "Maladie d'un ami ou appui ; Abandon des entreprises ; Mauvais conseils provoquant des pertes.",
            12: "Maladie ou chute des ennemis ; Risque d'emprisonnement ; Fatigue mentale ; Accident au visage.",
            13: "Maladie ou malade dans la chambre/concession ; Colère, peur, malchance, indolence.",
            14: "Perte de biens, maladie d'animaux ; Grosses difficultés pour obtenir satisfaction.",
            15: "Malheur dans la famille ; Échec des projets, querelles, bruits et revers structurels.",
            16: "Mauvaise finalité : échec, maladie grave, amertume et déception profonde."
        }
    },
    "Oumarou (Lomara / Rubeus)": {
        "code": [2, 1, 2, 2], "numero": 7, "element": "Air", "nature": "Passé", "polarite": "Femelle",
        "jour": "Mardi", "psaume": "Psaume 29", "verset": "Cantique 8 v.6", "sceau": "4e Pentacle de Mars",
        "sacrifice": "Un bouc rouge avec un chapeau rouge ; ou un poulet 'dakissê siè' + 70 colas ; ou de la viande rouge.",
        "plantes": "Gaba blé, Djati tgui fa djiri (Arbres : Gabablen, Foronto, Wo)",
        "maisons": {
            1: "Annonce clairement un mariage ; Relation houleuse, brutalité, querelles, sang ou regrets.",
            2: "Chance d'avoir un mariage ; Beaucoup de viande à manger ; Risque de perte sans sacrifice ; Impatience.",
            3: "Mariage ou malheur d'un parent dans la famille maternelle ; Paroles agressives ; Danger en déplacement.",
            4: "Brouille, fausses mauvaises nouvelles dans la famille paternelle ; Dilapidation ; Vente de mobilier.",
            5: "Mariage ou malheur de l'enfant ; Fille/grossesse ; Passion fougueuse et brutale, adultère.",
            6: "Maladie ou colère du conjoint ; Associé peu coopératif, chômage, vols, risques de congestion.",
            7: "Réalisation rapide d'un mariage ou association triste ; Contestation, adultère, procès perdu.",
            8: "Divorce, mort ou emprisonnement du partenaire ; Accidents (brûlures), désaccord d'héritage.",
            9: "Sérieux périls en voyage ; Arrivée d'une femme de teint clair ou de viande ; Fanatisme.",
            10: "Mauvaise réputation ; Élévation soudaine par la violence ; Colère des chefs (sang versé).",
            11: "Espoir de mariage (si M7 est bonne, aura lieu ; si mauvaise, sera raté) ; Discorde amicale.",
            12: "Méchanceté face au mariage ; Ennemis dangereux ; Scandales, congestion ; Risque à la tête.",
            13: "Nouvelle de mariage au foyer ; Personne en colère ou mécontentement dans la chambre.",
            14: "Perte de bien, pauvreté ; Gain obtenu uniquement par la violence ou via un objet rouge.",
            15: "Analyse d'un blocage violent ou d'une crise passionnelle menaçant l'équilibre du thème.",
            16: "Achèvement du mariage ou fin malheureuse (sang versé, échec agressif)."
        }
    },
    "Ayouba (Almangoussi / Tristitia)": {
        "code": [2, 2, 2, 1], "numero": 8, "element": "Terre", "nature": "Futur", "polarite": "Postérieur Mâle",
        "jour": "Samedi", "psaume": "Psaume 40", "verset": "Isaïe 61 v.3", "sceau": "5e Pentacle de Saturne",
        "sacrifice": "Habit complet (chapeau + boubou + pantalon) ; ou un mouton 'wéléwélé saga' + 111 colas blanches.",
        "plantes": "Herbes qui poussent sur les tombeaux, Koroni fin (Arbres : Koto, Ngokou)",
        "maisons": {
            1: "Mauvaises pensées, pessimisme, dépression, querelle, maladie ; Grand travail de réflexion.",
            2: "Mauvaise ambiance de travail, perte d'emploi ; Soucis d'argent, ruine ou petits déficits.",
            3: "Mauvaise entente ou mort d'un proche dans la famille maternelle ; Tristes nouvelles ; Voyage désagréable.",
            4: "Mort du père ou d'un parent ; Mauvaise ambiance entre germains ('fadénmaw') ; Solitude, père avare.",
            5: "Malchance, mort ou emprisonnement de l'enfant ou du rival ; Amour qui s'achève ; Rapports tendus.",
            6: "Aggravation de la maladie ou de la colère ; Métier non stimulant, dépression ; Perte d'animaux.",
            7: "Divorce, fin d'alliance ou mort d'un conjoint (veuvage) ; Malheureux mariage ; Perte de procès.",
            8: "Maladie chronique, chagrins ; Mort bouleversante d'une vieille personne ; Longue détention ; Ruine.",
            9: "De gros ennuis en vue, très mauvais pour le voyage ; Retards massifs et blocages à l'étranger.",
            10: "Chute sociale, destitution, ruine des projets de pouvoir, destitution de cadres.",
            11: "Espérances déçues, blocage systématique des projets d'avenir et défection des soutiens.",
            12: "Ennemis cachés puissants, destructeurs, sournois ; Complots ourdis dans l'ombre.",
            13: "Tristesse au foyer, blocage sur place, maladie à domicile ou ambiance sépulcrale.",
            14: "Pauvreté ou blocage total des gains financiers ; Les ressources s'épuisent.",
            15: "Témoin de blocage absolu ou fin définitive des choses et des espoirs formulés.",
            16: "Finalité extrêmement difficile ou issue totalement hermétique, ruine morale."
        }
    },
    "Qala-llahou (Aboubakr Sidik / Fortuna Minor)": {
        "code": [1, 1, 2, 2], "numero": 9, "element": "Feu", "nature": "Passé", "polarite": "Comté Mâle",
        "jour": "Dimanche", "psaume": "Psaume 121", "verset": "Psaume 46 v.2", "sceau": "4e Pentacle du Soleil",
        "sacrifice": "6 colas 'kôlô woro' ; ou 6 mètres de tissu blanc ; ou un poulet blanc à un malade ('dimintô').",
        "plantes": "Aladjon, racines d'arbres coupant la route (Arbres : Alladjô, Congo Sirani)",
        "maisons": {
            1: "Ambition, route libre et ouverte ; Réussites, projets heureux et profitables mais de courte durée ; Bon voyage.",
            2: "Gains rapides et instables ; L'argent rentre facilement mais repart aussitôt ; Risque de dépenses imprévues.",
            3: "Démarches rapides ; Nouvelles imminentes et plutôt satisfaisantes ; Entente de courte durée avec l'entourage.",
            4: "Changement de résidence ou modification dans le foyer ; Ambiance passagère ; Biens mobiles.",
            5: "Nouvelles d'un plaisir ou d'un succès éphémère ; Liaison amoureuse rapide ; Joie passagère liée à un enfant.",
            6: "Maladie ou colère en cours de route pour le voyageur ; Humiliation, orgueil mal placé ; Instabilité professionnelle.",
            7: "Démarches pour un mariage ou une union (prendra du temps) ; Goût du libertinage pour le conjoint ; Union peu durable.",
            8: "Très mauvais augure : peines et inquiétudes, emprisonnement ou mort ; Héritage vite dilapidé.",
            9: "Activité au loin ; Réalisation du voyage et réussite ; Arrivée d'un voyageur ; L'absent se fera attendre.",
            10: "Succès professionnel brillant mais instable ; Changement de poste en vue ; Autorité temporaire.",
            11: "Espoirs centrés sur de multiples projets ; Amis versatiles mais de bonne compagnie.",
            12: "Obstacles passagers créés par l'orgueil ; Ennemis sans grande consistance, feintes faciles.",
            13: "Changement ou agitation dans la chambre ou la concession ; Arrivée subite d'un visiteur.",
            14: "Rentré d'argent immédiate mais qui ne restera pas ; Flux financier très fluctuant.",
            15: "Présage d'un mouvement ou d'un voyage imminent, instabilité globale du verdict.",
            16: "Finalité rapide ; L'issue finale dépendra uniquement de la rapidité de vos actions."
        }
    },
    "Solomana (Manssa Souleymane / Carcer)": {
        "code": [1, 2, 2, 1], "numero": 10, "element": "Terre", "nature": "Présent", "polarite": "Femelle",
        "jour": "Samedi", "psaume": "Psaume 142", "verset": "Isaïe 22 v.22", "sceau": "7e Pentacle de Saturne",
        "sacrifice": "Un poulet 'sièlanka' qui a commencé à pondre ; ou beaucoup de colas distribuées ; ou du riz aux pauvres.",
        "plantes": "Mandé sounsoun, Sounsoun (Arbres : Zamba, Sira/Baobab)",
        "maisons": {
            1: "Esprit concentré, secret, repli sur soi ; Isolement volontaire ou involontaire ; Blocage initial.",
            2: "Gains bloqués ou épargne forcée ; L'argent est thésaurisé ou difficile d'accès ; Retards financiers.",
            3: "Grosses tensions, brouille entre les 'balimaw' ; Les ennemis grimpent ; Voyage compromis ; Démarche cachée.",
            4: "Habitation triste, mauvaise ambiance ; Grosses tensions entre les 'fadénmaw' ; Péril pour le père (prison).",
            5: "Secret concernant un enfant ou une grossesse ; Amour secret ou bloqué ; Pas de communication extérieure.",
            6: "Maladie chronique ou de longue durée ; Confinement, hospitalisation ; Contraintes professionnelles lourdes.",
            7: "Union secrète, mariage bloqué ou difficile à rompre ; Partenaire austère, froid ou fermé.",
            8: "Mort à la suite d'une longue maladie ou en prison ; Secret d'un héritage bloqué ; Sentiment d'étouffement.",
            9: "Voyage annulé ou empêché ; Esprit dogmatique ou profondément ésotérique ; Blocage au loin.",
            10: "Pouvoir acquis tardivement ou autorité stricte ; Chute ou enfermement pour les dirigeants actuels.",
            11: "Amis rares, secrets et fidèles ; Espoirs bloqués pour le moment ; Soutiens occultes cachés.",
            12: "Ennemis cachés et puissants ; Risque d'incarcération ou de mise à l'écart prolongée.",
            13: "Inertie, indolence, passé triste ; On voit la vie en noir, impression d'être marabouté ('siri').",
            14: "Perte de biens due aux 'famaw' (chefs) ; Parcours semé d'embûches amenant difficultés et souffrances.",
            15: "L'affaire est sous secret (chefferie) ; Il vaut mieux ne rien envisager et attendre ou changer de cap.",
            16: "Longue et difficile réalisation de l'ambition ; Celui qui cherche le pouvoir l'aura finalement après épreuves."
        }
    },
    "Badra (Badra Aliou / Conjunctio)": {
        "code": [2, 1, 1, 2], "numero": 11, "element": "Air", "nature": "Présent", "polarite": "Femelle",
        "jour": "Mercredi", "psaume": "Psaume 133", "verset": "Ruth 1 v.16", "sceau": "4e Pentacle de Mercure",
        "sacrifice": "Un bouc à égorger (viande partagée) ; ou un poulet à donner à un misérable (aveugle, lépreux) ; du poisson.",
        "plantes": "Guélé (Arbres : Triki, Gouélé)",
        "maisons": {
            1: "Présage favorable, idées prometteuses ; Association en vue, bonheur, affabilité ; Retard infime.",
            2: "Chance d'acquérir un bien par un ami ou associé (argent, engin, bétail) ; Obtention de ce qui est désiré.",
            3: "Espoirs comblés au niveau de la famille maternelle, avec un frère, sœur ou la belle-famille.",
            4: "Paix au foyer ; Climat familial sain, serein et équilibré ; Acquisition de biens immobiliers propres.",
            5: "Annonce de joies saines, clarté avec les enfants ; Sentiments purs, sincères et partagés.",
            6: "Bonne santé, rétablissement rapide ; Climat de confiance absolue au travail.",
            7: "Mariage heureux, alliance claire et sincère ; Succès dans les signatures de contrats.",
            8: "Transformation positive ; Fin définitive des ennuis ; Gains par des moyens légaux et clairs.",
            9: "Voyage paisible, études ou quête spirituelle couronnée de succès ; Grande sagesse.",
            10: "Honneurs, reconnaissance méritée, situation sociale limpide, respectée et stable.",
            11: "Amitiés fidèles et hautement protectrices ; Les espoirs secrets se réalisent sereinement.",
            12: "Les ennemis capitulent ou s'effacent devant la vérité ; Clarté face aux derniers obstacles.",
            13: "Sérénité dans la chambre à coucher, discussions très constructives et saines en famille.",
            14: "Gains financiers honnêtes, consolidés et sécurisés ; Excellente protection matérielle.",
            15: "Résolution juste, pacifique et définitive de la situation litigieuse ou recherchée.",
            16: "Excellente finalité : la paix, le droit, l'alliance et la clarté triomphent sur toute la ligne."
        }
    },
    "Nouhou (Nouhoum / Cauda Draconis)": {
        "code": [1, 1, 2, 1], "numero": 12, "element": "Terre", "nature": "Futur", "polarite": "Femelle",
        "jour": "Dimanche", "psaume": "Psaume 59", "verset": "Psaume 68 v.2", "sceau": "6e Pentacle de Saturne",
        "sacrifice": "Un bélier blanc à attacher pendant 6 jours à la maison. Lui faire boire un Nassi de 100 Manssa Souleymane.",
        "plantes": "Goundjè (Arbres : Koudjè, Zèguènè)",
        "maisons": {
            1: "Esprit lourd, tristesse, sévérité, rancœur ; Projets ralentis ou bloqués par le passé ou des dettes.",
            2: "Difficultés financières chroniques ; Rares gains obtenus au prix d'efforts pénibles et harassants.",
            3: "Mésentente larvée entre proches ; Nouvelles attristantes ou très retardées ; Voyages pénibles.",
            4: "Foyer austère, rigueur paternelle excessive ; Soucis profonds liés aux structures ou à la terre.",
            5: "Inquiétudes face à un enfant ; Relations amoureuses froides, distantes ou bloquées.",
            6: "Maladie liée aux os, à la fatigue ou à la vieillesse ; Travail subordonné, ingrat et difficile.",
            7: "Union tardive, mariage de raison ou marqué par l'austérité et le manque de communication.",
            8: "Héritage ancestral ou de longue date ; Fin d'une situation difficile après de longs mois d'attente.",
            9: "Voyage reporté ; Profondes réflexions philosophiques ou religieuses traditionnelles.",
            10: "Position sociale stable mais acquise par un labeur acharné ; Responsabilités lourdes à porter.",
            11: "Amis âgés ou conservateurs ; Espoirs limités par la dure réalité du moment.",
            12: "Ennemis tenaces qui agissent sur la longue durée ; Obstacles administratifs ou structurels.",
            13: "Atmosphère pesante ou silencieuse dans la chambre ; Réflexion solitaire et nocturne.",
            14: "Ressources limitées, nécessité d'une gestion prudente, austère et très économe.",
            15: "Persistance des blocages hérités du passé ; Le Juge invite à assainir les dettes.",
            16: "Issue lente mais stable, demandant une persévérance et une endurance à toute épreuve."
        }
    },
    "Laoussana (Alhoussein / Puella)": {
        "code": [1, 2, 1, 2], "numero": 13, "element": "Eau", "nature": "Passé", "polarite": "Femelle",
        "jour": "Samedi", "psaume": "Psaume 119 (Aleph)", "verset": "Cantique 4 v.7", "sceau": "2e Pentacle de Vénus",
        "sacrifice": "Tout ce qu'on trouve sous la terre (igname, carotte), savon blanc, sel de gemme à offrir aux vieilles.",
        "plantes": "Djoulasonkalani (Plantes gluantes, herbes des vieux puits)",
        "maisons": {
            1: "Sentiment de perte, détachement, générosité excessive au détriment de soi ; Fatigue physique.",
            2: "Sortie d'argent massive, mauvaise affaire, investissement hasardeux, perte financière sèche.",
            3: "Éloignement d'un proche, rupture définitive de communication, voyage infructueux.",
            4: "Dépréciation des biens immobiliers, dépenses lourdes et imprévues pour le foyer familial.",
            5: "Chagrin d'amour, rupture sentimentale ; Soucis financiers liés aux loisirs ou aux caprices des enfants.",
            6: "Bainte d'énergie, fatigue physique latente ; Risque de perte d'emploi ou baisse d'activité.",
            7: "Séparation, divorce, rupture de contrat ou d'association ; Procès coûteux et épuisant.",
            8: "Dépenses importantes liées à une succession ; Perte définitive d'une ancienne situation avantageuse.",
            9: "Voyage gâché, annulé ou très coûteux ; Crise de foi ou égarement intellectuel passager.",
            10: "Destitution, perte de statut social ou d'influence professionnelle ; Échec à un examen.",
            11: "Éloignement ou perte d'un ami fidèle ; Espoirs déçus ou projets s'effondrant.",
            12: "Les ennemis s'affaiblissent ou perdent leurs moyens et leurs alliés (aspect positif de la perte).",
            13: "Disparition d'un objet précieux ou départ soudain d'un habitant de la chambre ou concession.",
            14: "Diminution nette des gains financiers ; Période de vaches maigres demandant de la retenue.",
            15: "Effritement ou disparition progressive des acquis matériels ou relationnels mis en cause.",
            16: "Finalité menant à un renoncement nécessaire ou à une perte s'il n'y a pas de réaction immédiate."
        }
    },
    "Ousmane (Mory Zoumana / Acquisitio)": {
        "code": [2, 1, 2, 1], "numero": 14, "element": "Terre", "nature": "Futur", "polarite": "Comté Mâle",
        "jour": "Jeudi", "psaume": "Psaume 23", "verset": "Psaume 23 v.1", "sceau": "3e Pentacle de Jupiter",
        "sacrifice": "Fruits secs, dattes, raisins, ou longs animaux (caprins). À donner à un groupe réuni le Jeudi.",
        "plantes": "N'doubalé, Frogofraga (Arbres : Troubala, Dougalen)",
        "maisons": {
            1: "Esprit tourné vers le profit, l'expansion et les affaires ; Confiance en soi, opportunisme positif.",
            2: "Accroissement majeur des richesses, excellente rentrée d'argent, investissement très rentable.",
            3: "Transactions commerciales fructueuses ; Démarches payantes ; Nouvelles financières enrichissantes.",
            4: "Enrichissement du patrimoine familial ; Prospérité matérielle et confort accru au foyer.",
            5: "Investissements chanceux ; Enfants apportant réussite, fierté et honneur ; Bonheur matériel.",
            6: "Augmentation de l'activité professionnelle, promotion interne ; Bonne et robuste constitution physique.",
            7: "Mariage financièrement avantageux, association commerciale ou industrielle très lucrative.",
            8: "Héritage important, retours sur investissements majeurs ; Crises surmontées avec un gros profit.",
            9: "Voyages d'affaires très profitables ; Élargissement des horizons commerciaux ou géographiques.",
            10: "Ascension sociale majeure, réussite politique ou commerciale éclatante, pouvoir financier établi.",
            11: "Relations influentes, riches et fortunées ; Les vœux de richesse se réalisent concrètement.",
            12: "Capacité financière et relationnelle à racheter ou à neutraliser ses ennemis par les biens.",
            13: "Entrée massive de biens matériels, de cadeaux ou de capitaux directement dans la maison.",
            14: "Multiplication exponentielle des profits financiers ; Prospérité continue à moyen terme.",
            15: "Confirmation absolue d'un enrichissement à venir ou d'un succès total sur l'objectif.",
            16: "Finalité excellente débouchant sur une immense réussite financière, matérielle et sociale."
        }
    },
    "Younouss (Tontigui / Puella)": {
        "code": [1, 2, 1, 1], "numero": 15, "element": "Air", "nature": "Futur", "polarite": "Femelle",
        "jour": "Vendredi", "psaume": "Psaume 112", "verset": "Deutéronome 28 v.12", "sceau": "6e Pentacle de Jupiter",
        "sacrifice": "Bijoux, parures, objets brillants, ou miroirs. À donner aux jeunes enfants le Vendredi.",
        "plantes": "N'tomotigui, Zondjè (Arbres : Fogofogo)",
        "maisons": {
            1: "Recherche d'harmonie, coquetterie, indécision ; Importance accordée au regard de l'autre.",
            2: "Gains liés à la beauté, aux arts ou provenant de femmes ; Dépenses de plaisir et de luxe.",
            3: "Discussions futiles mais agréables ; Entente facile avec les sœurs, tantes ou voisines proches.",
            4: "Décoration agréable du foyer ; Recherche de confort, d'esthétique et d'harmonie en famille.",
            5: "Amours volages ou passionnées ; Chance d'avoir une fille ; Plaisirs, fêtes et sorties.",
            6: "Petits soucis de santé bénins (esthétiques ou circulatoires légers) ; Emploi agréable.",
            7: "Union romantique, mariage basé sur l'attraction mutuelle ; Association d'affaires plaisante.",
            8: "Succession sans heurts ni conflits ; Fin douce et naturelle d'une situation tendue.",
            9: "Voyages d'agrément, de tourisme ou de loisir ; Curiosité artistique développée.",
            10: "Succès dans les métiers publics, de communication ou artistiques ; Grande popularité.",
            11: "Amies nombreuses, élégantes et bienveillantes ; Souhaits orientés vers le confort de vie.",
            12: "Rivalités amoureuses ou jalousies superficielles vite balayées par votre charme.",
            13: "Ambiance intime, douce et feutrée dans la chambre ; Présence féminine réconfortante.",
            14: "Aisance matérielle facilitée par les relations de charme ; Confort financier assuré.",
            15: "Dénouement sous le signe de la conciliation, de la diplomatie et de l'entente cordiale.",
            16: "Finalité heureuse, agréable, légère et pleinement satisfaisante pour l'harmonie personnelle."
        }
    },
    "Moussa (Djama / Populus)": {
        "code": [2, 2, 2, 2], "numero": 16, "element": "Feu", "nature": "Présent", "polarite": "Femelle",
        "jour": "Lundi", "psaume": "Psaume 47", "verset": "Genèse 22 v.17", "sceau": "1er Pentacle de la Lune",
        "sacrifice": "Fruits frais, bananes, graines, riz blanc. À donner aux guides religieux ou imams le Lundi.",
        "plantes": "N'tomi, N'galama (Arbres : Tomy, Sounzoufing)",
        "maisons": {
            1: "Influence de l'entourage, indécision personnelle, esprit grégaire ; Suivre la masse.",
            2: "Gains dépendants directement du public, des clients ou de la foule ; Revenus multiples.",
            3: "Nombreux déplacements, réunions de quartier ou de famille ; Flux massif d'informations.",
            4: "Maison ouverte, beaucoup de passage au foyer ; Manque cruel d'intimité familiale.",
            5: "Famille nombreuse ou beaucoup d'enfants autour de soi ; Amours multiples ou instables.",
            6: "Maladies contagieuses ou épidémiques ; Métiers en contact direct avec le grand public.",
            7: "Mariage exposé au public, vie sociale intense du couple ; Nombreux associés ou rivaux.",
            8: "Affaires publiques ou d'intérêt collectif ; Transformations influencées par l'extérieur.",
            9: "Grands rassemblements, pèlerinages ou voyages collectifs ; Idées influencées par la masse.",
            10: "Célébrité, vie publique, poste électif ou dépendant entièrement du choix de la foule.",
            11: "Réseau d'amis très vaste ; Les espoirs dépendent de l'appui du plus grand nombre.",
            12: "Les ennemis agissent en groupe ou publiquement (rumeurs, opinion publique hostile).",
            13: "Beaucoup de monde réuni dans la concession ou la chambre ; Réunions, assemblées.",
            14: "Ressources fluctuantes selon les tendances de la collectivité ou du marché public.",
            15: "Le Juge indique que la situation implique une collectivité ou est désormais connue de tous.",
            16: "Finalité dépendante de l'environnement extérieur et de l'approbation générale du groupe."
        }
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
# 2. LOGIQUE MATHEMATIQUE GEOMANTIQUE DE COPULATION SANS FAILLE
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
    
    # Transposition matricielle rigoureuse pour l'engendrement des Filles (M5-M8)
    try:
        theme[5] = next(k for k, v in FIGURES_DB.items() if v["code"] == [f1["code"][0], f2["code"][0], f3["code"][0], f4["code"][0]])
        theme[6] = next(k for k, v in FIGURES_DB.items() if v["code"] == [f1["code"][1], f2["code"][1], f3["code"][1], f4["code"][1]])
        theme[7] = next(k for k, v in FIGURES_DB.items() if v["code"] == [f1["code"][2], f2["code"][2], f3["code"][2], f4["code"][2]])
        theme[8] = next(k for k, v in FIGURES_DB.items() if v["code"] == [f1["code"][3], f2["code"][3], f3["code"][3], f4["code"][3]])
    except StopIteration:
        st.error("🚨 Une asymétrie critique est détectée dans la matrice. Réinitialisation sur les valeurs fondamentales.")
        theme[5], theme[6], theme[7], theme[8] = m1, m2, m3, m4

    # Calcul du reste du Tribunal Géomantique
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
# 3. INTERFACE DE SECURITE STREAMLIT
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
# 4. EXÉCUTION DE L'APPLICATION ET DESIGN GRAPHIQUE
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
# 5. DÉTECTION DES RÈGLES DE COPULATION DE FIN DE THÈME (M15 + M1)
# =====================================================================
st.header("🧬 Analyse Statistique Spécifique des Copulations")
parent_detecte_A = theme_calcule[15]
parent_detecte_B = theme_calcule[1]
nameA, nameB = MAPPING_SIMPLIFIE[parent_detecte_A], MAPPING_SIMPLIFIE[parent_detecte_B]
set_parents = {nameA, nameB}

details_engendre = "Les flux d'accouplement suivent le cours naturel des éléments du thème."
if set_parents == {"Youssouf", "Laoussana"}: details_engendre = "⚠️ **MÉCHANCETÉ À CAUSE D'ENFANT**"
elif set_parents == {"Adama", "Laoussana"}: details_engendre = "🔴 **SACRIFICE ROUGE REQUIS**"
elif set_parents == {"Mahamadou", "Ayouba"}: details_engendre = "❌ **DIFFICULTÉ POUR AVOIR DES ENFANTS (BLOCAGE MATERNEL)**"
elif set_parents == {"Idrissa", "Oumarou"}: details_engendre = "💨 **TEMPÊTE, UN GRAND VENT VIOLENT QUI FAIT DES DÉGÂTS**"
elif set_parents == {"Ibrahima", "Solomana"}: details_engendre = "👶 **LA GROSSESSE EN ATTEINTE**"
elif set_parents == {"Nouhou", "Ousmane"}: details_engendre = "👑 **LA GRANDEUR ET L'HONNEUR ASSURÉS**"
elif set_parents == {"Qala-llahou", "Issa"}: details_engendre = "🚨 **UNE TRÈS GRAVE DIFFICULTÉ EN RÉSULTAT**"
elif set_parents == {"Moussa", "Badra"}: details_engendre = "⚔️ **DESTIN DE GUERRIER, DE SOLDAT OU D'ÉLÈVES COUPEURS**"

with st.expander("🔍 Résultat du Croisement de Fin de Thème (M15 + M1)", expanded=True):
    st.write(f"**Parents Détectés :** {parent_detecte_A} ✖️ {parent_detecte_B}")
    st.warning(f"✨ **Verdict Ombral :** {details_engendre}")

st.markdown("---")

# =====================================================================
# 6. EXPLORATEUR DYNAMIQUE INTERPRÉTATIF DES 16 MAISONS
# =====================================================================
st.header("🏠 Analyse Spécifique du Passage d'une Figure en Maison")
col_ex1, col_ex2 = st.columns(2)
with col_ex1: fig_analyse = st.selectbox("Figure à étudier :", options=list(FIGURES_DB.keys()), key="expl_fig")
with col_ex2: maison_analyse = st.selectbox("Maison de destination :", options=list(MAISONS_NOMS.keys()), format_func=lambda x: MAISONS_NOMS[x], key="expl_mai")

if fig_analyse and maison_analyse:
    interpretation_textuelle = FIGURES_DB[fig_analyse]["maisons"].get(maison_analyse, "Analyse absente dans les manuscrits de base.")
    st.success(f"📋 **Interprétation Référentielle du Passage :**\n\n> {interpretation_textuelle}")

st.markdown("---")

# =====================================================================
# 7. ORDONNANCE THÉURGIQUE INTÉGRALE & PROTOCOLES PRATIQUES (MAISON 16)
# =====================================================================
st.header("📊 Protocole Théurgique Intégral : Focus Maison 16")
figure_finale = theme_calcule[16]
st.info(f"Figure souveraine de fermeture et d'aboutissement (M16) : **{figure_finale}**")

data_f = FIGURES_DB[figure_finale]

tab_s1, tab_s2, tab_s3, tab_s4 = st.tabs([
    "🐑 1. Sacrifices Correctifs (Saraka)", 
    "✝️ 2. Alignements & Textes Sacrés", 
    "🌿 3. Ingrédients Botaniques",
    "📜 4. Protocoles d'Utilisation (Nassi, Bains, Récitation)"
])

with tab_s1:
    st.markdown(f"**Aumône prescriptive traditionnelle :** {data_f['sacrifice']}")

with tab_s2:
    st.markdown(f"* **Psaume de traçage et de purification :** `{data_f['psaume']}`")
    st.markdown(f"* **Verset d'activation d'autorité :** `{data_f['verset']}`")
    st.markdown(f"* **Sceau Sceau Vibratoire de Salomon :** `{data_f['sceau']}`")
    st.markdown(f"* **Jour Planétaire Sacré de Trait :** **{data_f['jour']}**")

with tab_s3:
    st.markdown(f"**Plantes, poudres et composants magiques associés :** {data_f['plantes']}")

with tab_s4:
    st.subheader("🛠️ Guide Opératoire Traditionnel d'Activation")
    
    st.markdown(f"""
    ### 1. Protocole de Récitation (Psaumes & Versets)
    * **Timing Vibratoire :** À pratiquer impérativement le **{data_f['jour']}** (Jour de la figure), idéalement à l'aube ou après minuit.
    * **Clé d'Ouverture :** Récitez d'abord le verset d'activation (`{data_f['verset']}`) **7, 33 ou 111 fois** consécutives selon l'urgence.
    * **Le Corps du Rituel :** Récitez ensuite le `{data_f['psaume']}` **3 fois à voix haute**, en formulant clairement votre vœu de déblocage ou d'acquisition à la fin de chaque lecture.
    
    ---
    ### 2. Guide de Préparation du Nassi (Eau Sacrée)
    * **Support d'écriture :** Utilisez une tablette traditionnelle en bois (*Alo*) ou une assiette blanche en porcelaine neuve sans aucun motif.
    * **Encre Sacrée :** Utilisez une encre soluble traditionnelle saine (mélange de safran, eau de rose et charbon de bois pulvérisé). Tracez la figure géomantique **{MAPPING_SIMPLIFIE[figure_finale]}** entourée du `{data_f['verset']}`.
    * **Lavage :** Rincez délicatement la surface avec de l'eau pure (eau de source ou eau de pluie) pour dissoudre l'encre. Recueillez le précieux liquide dans un flacon propre.
    * **Usage :** Buvez-en une gorgée chaque matin à jeun pendant **3, 7 ou 9 jours**, ou appliquez-en sur votre visage et vos mains avant vos démarches critiques.
    
    ---
    ### 3. Protocole des Bains Sacrés (Plantes & Décoctions)
    * **Préparation :** Faites bouillir les plantes spécifiques indiquées (`{data_f['plantes']}`) dans une grande marmite d'eau pure pendant 15 à 30 minutes.
    * **L'Alliance Mystique :** Filtrez la décoction, versez-la dans votre seau et ajoutez-y **un demi-verre de votre Nassi** préparé précédemment.
    * **Le Bain :** Lavez-vous d'abord normalement avec votre savon habituel. À la fin, versez l'eau de plantes tiède de la tête aux pieds en récitant le verset d'activation.
    * **Le Secret du Séchage :** **Ne vous essuyez pas.** Laissez l'eau sacrée sécher d'elle-même sur votre peau afin de sceller l'enveloppe astrale. *Évitez tout rapport intime pendant la durée du traitement (3 ou 7 jours).*
    """)

st.markdown("---")
st.caption("SST Informatique — Version Générative complète à 16 Maisons. Tous droits réservés.")
