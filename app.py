import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page Streamlit
st.set_page_config(page_title="Théurgie Somadjely - Présentation", layout="wide")

# Contenu HTML des slides
presentation_html = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Théurgie Somadjely - Présentation</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Merriweather:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        /* CONFIGURATION DE BASE */
        * { box-sizing: border-box; }
        body { margin: 0; padding: 20px; background-color: #f1f5f9; font-family: 'DM Sans', sans-serif; display: flex; flex-direction: column; align-items: center; gap: 40px; }
        
        .slide-container {
            width: 1280px; height: 720px; background-color: #fff; border-radius: 12px; overflow: hidden;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1); position: relative; display: flex; flex-direction: column;
            padding: 60px; z-index: 1;
        }

        /* THÈME SOMADJELY : BLEU ACADÉMIQUE ET CRÈME */
        .academic-theme { background-color: #003366; color: #f3f0df; }
        .academic-theme h1, .academic-theme h2, .academic-theme h3 { color: #f3f0df; font-family: 'Merriweather', serif; }
        .academic-theme p, .academic-theme li { color: #d1d5db; }

        .light-theme { background-color: #fdfbf4; color: #003366; border: 1px solid #e2e8f0; }
        .light-theme h2, .light-theme h3 { color: #003366; font-family: 'Merriweather', serif; }
        .light-theme .slide-title { font-size: 48px; border-bottom: 3px solid #003366; display: inline-block; margin-bottom: 40px; }

        /* LAYOUTS */
        .title-layout { text-align: center; justify-content: center; height: 100%; }
        .title-layout h1 { font-size: 80px; margin-bottom: 20px; }
        .title-layout .subtitle { font-size: 28px; font-weight: 400; }

        .content-area { flex-grow: 1; display: flex; align-items: center; width: 100%; }
        .two-column { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; width: 100%; }

        .tiled-content { display: flex; gap: 30px; width: 100%; }
        .tile { flex: 1; background: #004080; padding: 30px; border-radius: 15px; text-align: center; }
        .tile .icon { font-size: 40px; margin-bottom: 20px; color: #11caa0; }

        .image-wrapper { border-radius: 15px; overflow: hidden; width: 100%; height: 400px; border: 2px solid #003366; }
        .image-wrapper img { width: 100%; height: 100%; object-fit: cover; }

        .rounded-image { border-radius: 50%; height: 350px; width: 350px; border: 5px solid #003366; }

        .quote-layout { text-align: center; max-width: 900px; margin: auto; }
        .quote-layout blockquote { font-size: 42px; font-family: 'Merriweather', serif; font-style: italic; position: relative; padding: 40px; }
        .quote-layout blockquote::before { content: '"'; font-size: 100px; position: absolute; left: -20px; top: -10px; opacity: 0.2; }

        .highlight-numbers { display: flex; align-items: center; justify-content: space-around; width: 100%; }
        .number-box { text-align: center; }
        .number-box .val { font-size: 120px; font-weight: 700; color: #11caa0; }
        .number-box .label { font-size: 24px; text-transform: uppercase; }

        .bleed-image-layout { display: grid; grid-template-columns: 1fr 1fr; padding: 0; align-items: stretch; }
        .bleed-text { padding: 60px; display: flex; flex-direction: column; justify-content: center; }
        .bleed-img { height: 720px; width: 100%; object-fit: cover; }

        /* DESIGN ELEMENTS */
        .bg-shapes { position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; opacity: 0.1; }
    </style>
</head>
<body>

<div class="slide-container academic-theme" id="slide1">
    <div class="title-layout">
        <i class="fa-solid fa-scroll" style="font-size: 60px; color: #11caa0; margin-bottom: 20px;"></i>
        <h1>La Théurgie du Maître Somadjely</h1>
        <p class="subtitle">Géomancie Sacrée, Botanique et Remèdes Bibliques</p>
    </div>
</div>

<div class="slide-container light-theme" id="slide2">
    <div class="title-layout">
        <h2 style="font-size: 64px;">Principes Fondamentaux</h2>
        <div style="height: 5px; width: 150px; background: #003366; margin: 20px auto;"></div>
        <p style="font-size: 24px; max-width: 800px; margin: 0 auto;">L'alliance de la terre et du ciel : Utiliser la vibration des plantes et la puissance des Psaumes pour transformer le destin.</p>
    </div>
</div>

<div class="slide-container light-theme" id="slide3">
    <h2 class="slide-title">Les 16 Figures Sacrées</h2>
    <div class="content-area">
        <div class="two-column">
            <div style="background: #eef2ff; padding: 30px; border-radius: 12px;">
                <h3 style="margin-top:0">Matrice Binaire</h3>
                <p>Chaque figure est une signature énergétique composée de quatre strates (Tête, Poitrine, Ventre, Pied).</p>
                <ul>
                    <li><strong>1 point :</strong> Energie Impaire (Mouvement)</li>
                    <li><strong>2 points :</strong> Energie Paire (Stabilité)</li>
                </ul>
            </div>
            <div class="image-wrapper">
                <img src="http://googleusercontent.com/image_collection/image_retrieval/3976605460248458434" alt="Manuscrit Géomantique">
            </div>
        </div>
    </div>
</div>

<div class="slide-container academic-theme" id="slide4">
    <h2 class="slide-title">La Vision Somadjely</h2>
    <div class="content-area">
        <div class="two-column" style="align-items: center;">
            <img src="https://placehold.co/400x400/004080/f3f0df?text=L'Art+Sacré" class="rounded-image">
            <div>
                <h3>Une Théurgie sans sacrifice</h3>
                <p style="font-size: 22px;">Le Maître préconise une approche pure : le "Nassi" chrétien. Pas de sang, mais l'infusion de plantes sacrées et la récitation de paroles de puissance.</p>
            </div>
        </div>
    </div>
</div>

<div class="slide-container light-theme" id="slide5">
    <h2 class="slide-title">Botanique Sacrée</h2>
    <div class="content-area">
        <div class="two-column">
            <div>
                <p>Chaque plante correspond à une figure et un élément cosmique :</p>
                <ul style="font-size: 20px; line-height: 2;">
                    <li><i class="fa-solid fa-leaf" style="color:#11caa0"></i> <strong>Laurier Noble :</strong> Victoire (Youssouf)</li>
                    <li><i class="fa-solid fa-leaf" style="color:#11caa0"></i> <strong>Hysope :</strong> Purification (Ibrahima)</li>
                    <li><i class="fa-solid fa-leaf" style="color:#11caa0"></i> <strong>Menthe Blanche :</strong> Paix (Idrissa)</li>
                </ul>
            </div>
            <div class="image-wrapper">
                <img src="http://googleusercontent.com/image_collection/image_retrieval/9778828959196244537" alt="Plantes Sacrées">
            </div>
        </div>
    </div>
</div>

<div class="slide-container bleed-image-layout academic-theme" id="slide6">
    <div class="bleed-text">
        <h2 style="font-size: 56px;">Face au Nord</h2>
        <p style="font-size: 24px;">L'orientation est la clé. Le Nord représente l'axe polaire, le point fixe de la sagesse éternelle d'où descendent les bénédictions.</p>
    </div>
    <img src="http://googleusercontent.com/image_collection/image_retrieval/15884405325664246470" class="bleed-img" alt="Boussole Nord">
</div>

<div class="slide-container light-theme" id="slide7">
    <h2 class="slide-title">Le Protocole du Rituel</h2>
    <div class="content-area">
        <div class="tiled-content">
            <div class="tile" style="background:#003366">
                <div class="icon"><i class="fa-solid fa-pen-nib"></i></div>
                <h3>Calligraphie</h3>
                <p>Dessiner la figure et le verset 7 fois.</p>
            </div>
            <div class="tile" style="background:#004080">
                <div class="icon"><i class="fa-solid fa-fire-burner"></i></div>
                <h3>Infusion</h3>
                <p>Bouillir la plante durant 10 minutes.</p>
            </div>
            <div class="tile" style="background:#0050a0">
                <div class="icon"><i class="fa-solid fa-droplet"></i></div>
                <h3>Le Bain</h3>
                <p>Application du Nassi après la douche.</p>
            </div>
        </div>
    </div>
</div>

<div class="slide-container academic-theme" id="slide8">
    <div class="quote-layout">
        <blockquote>"Purifie-moi avec l'hysope, et je serai pur ; lave-moi, et je serai plus blanc que la neige."</blockquote>
        <cite style="font-size: 24px; color: #11caa0;">— Psaume 51:7</cite>
    </div>
</div>

<div class="slide-container light-theme" id="slide9">
    <h2 class="slide-title">Cycle Temporel</h2>
    <div class="content-area">
        <div class="highlight-numbers">
            <div class="number-box">
                <div class="val">3</div>
                <div class="label">Jours (Présent)</div>
            </div>
            <div class="number-box">
                <div class
