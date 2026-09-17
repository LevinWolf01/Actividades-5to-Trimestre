from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from .import views
urlpatterns = [
    path('admin/',admin.site.urls),
    path('', lambda request: HttpResponse("""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WaySmart: IA y Logística Avanzada</title>
    
    <style>
        /* =========================================
           Variables de Alto Contraste y Colores Vivos
           ========================================= */
        :root {
            --electric-blue: #0055FF;
            --neon-cyan: #00E5FF;
            --deep-navy: #040B16;
            --vibrant-purple: #8A2BE2;
            --pure-white: #FFFFFF;
            --flashy-yellow: #CCFF00;
            --card-bg: #0A1428;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background-color: var(--deep-navy);
            color: var(--pure-white);
            line-height: 1.5;
            display: grid;
            grid-template-areas:
                "nav"
                "header"
                "main"
                "footer";
            grid-template-columns: 1fr;
        }

        /* =========================================
           Navegación Flotante (Glassmorphism)
           ========================================= */
        .main-nav {
            grid-area: nav;
            position: sticky;
            top: 0;
            z-index: 100;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 5%;
            background: rgba(4, 11, 22, 0.8);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .nav-brand {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .logo-icon {
            background: linear-gradient(45deg, var(--electric-blue), var(--neon-cyan));
            color: var(--pure-white);
            font-weight: 900;
            font-size: 1.2rem;
            width: 45px; height: 45px;
            display: flex; align-items: center; justify-content: center;
            border-radius: 14px;
            box-shadow: 0 0 20px rgba(0, 229, 255, 0.4);
        }

        .nav-brand h2 { font-weight: 800; font-size: 1.8rem; letter-spacing: -1px; }

        .nav-links {
            display: flex; gap: 25px; list-style: none; align-items: center;
        }

        .nav-links a {
            text-decoration: none;
            color: rgba(255, 255, 255, 0.8);
            font-weight: 600;
            font-size: 0.95rem;
            transition: color 0.3s, text-shadow 0.3s;
            position: relative;
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            width: 0%; height: 3px;
            bottom: -5px; left: 0;
            background: var(--neon-cyan);
            transition: width 0.3s ease;
            border-radius: 2px;
        }

        .nav-links a:hover {
            color: var(--neon-cyan);
            text-shadow: 0 0 10px rgba(0, 229, 255, 0.5);
        }
        .nav-links a:hover::after { width: 100%; }

        .nav-actions {
            display: flex;
            gap: 12px;
        }

        .btn-secondary {
            background: transparent;
            color: var(--neon-cyan);
            border: 2px solid var(--neon-cyan);
            padding: 8px 18px;
            border-radius: 50px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
        }

        .btn-secondary:hover {
            background: rgba(0, 229, 255, 0.15);
            box-shadow: 0 0 15px rgba(0, 229, 255, 0.3);
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--electric-blue), var(--neon-cyan));
            color: var(--pure-white);
            padding: 10px 22px;
            border-radius: 50px;
            font-weight: 800;
            border: none;
            cursor: pointer;
            text-transform: uppercase;
            font-size: 0.85rem;
            letter-spacing: 1px;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .btn-primary:hover {
            transform: translateY(-3px) scale(1.03);
            box-shadow: 0 10px 20px rgba(0, 85, 255, 0.4);
        }

        /* =========================================
           Hero Section (Header)
           ========================================= */
        @keyframes gradientAnimation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .site-header {
            grid-area: header;
            position: relative;
            min-height: 80vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 20px;
            overflow: hidden;
            background: linear-gradient(-45deg, var(--deep-navy), var(--electric-blue), var(--vibrant-purple), #000814);
            background-size: 300% 300%;
            animation: gradientAnimation 12s ease infinite;
        }

        .header-content {
            position: relative;
            z-index: 10;
            max-width: 900px;
        }

        .badge-neon {
            display: inline-block;
            padding: 8px 20px;
            background: rgba(0, 229, 255, 0.1);
            color: var(--neon-cyan);
            border: 1px solid var(--neon-cyan);
            border-radius: 30px;
            font-weight: 600;
            margin-bottom: 25px;
            text-transform: uppercase;
            letter-spacing: 2px;
            box-shadow: 0 0 15px rgba(0, 229, 255, 0.3);
        }

        .header-content h1 {
            font-size: 4.5rem;
            font-weight: 900;
            line-height: 1.1;
            margin-bottom: 20px;
            text-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        .header-content h1 span {
            background: linear-gradient(to right, var(--flashy-yellow), var(--neon-cyan));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .header-content p {
            font-size: 1.3rem;
            color: rgba(255,255,255,0.9);
            max-width: 700px;
            margin: 0 auto;
        }

        .blob {
            position: absolute;
            border-radius: 50%;
            filter: blur(80px);
            z-index: 1;
            opacity: 0.6;
        }
        .blob-1 { top: -100px; left: -100px; width: 400px; height: 400px; background: var(--neon-cyan); }
        .blob-2 { bottom: -150px; right: 10%; width: 500px; height: 500px; background: var(--electric-blue); }

        /* =========================================
           Bento Box Grid Main
           ========================================= */
        .grid-main {
            grid-area: main;
            padding: 5% 5%;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            grid-auto-rows: minmax(300px, auto);
            gap: 25px;
            max-width: 1400px;
            margin: 0 auto;
        }

        .research-section {
            border-radius: 35px;
            overflow: hidden;
            position: relative;
            background: var(--card-bg);
            border: 1px solid rgba(255, 255, 255, 0.05);
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease;
        }

        .research-section:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(0, 85, 255, 0.25);
        }

        .bento-hero { grid-column: span 4; min-height: 420px; }
        .bento-solid { grid-column: span 2; padding: 40px; }
        .bento-wide { grid-column: span 4; padding: 30px; }
        .bento-full { grid-column: span 4; padding: 45px; }

        /* Tarjeta con imagen de fondo */
        .has-bg-image { display: flex; align-items: flex-end; }
        .bg-img {
            position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: 1;
            transition: transform 0.7s ease;
        }
        .research-section:hover .bg-img { transform: scale(1.08); }
        .content-overlay {
            position: relative; z-index: 3; padding: 40px; width: 100%;
            background: linear-gradient(to top, rgba(4,11,22,0.95) 0%, rgba(4,11,22,0.7) 50%, transparent 100%);
        }
        .content-overlay h3 { font-size: 2.5rem; font-weight: 800; margin-bottom: 8px; }
        .content-overlay p { font-size: 1.1rem; color: #ccc; }

        .neon-blue-bg { background: var(--electric-blue); display: flex; flex-direction: column; justify-content: center; }
        .icon-big { font-size: 3.5rem; margin-bottom: 15px; }
        .neon-blue-bg h3 { font-size: 2rem; font-weight: 800; margin-bottom: 12px; }

        .dark-bg { background: #0A1428; }
        .outline-glow::before {
            content: ''; position: absolute; inset: 0; border: 2px solid rgba(0, 229, 255, 0.2);
            border-radius: 35px; pointer-events: none; transition: border-color 0.3s;
        }
        .outline-glow:hover::before { border-color: var(--neon-cyan); }
        .gradient-text {
            font-size: 2rem; font-weight: 800;
            background: linear-gradient(45deg, var(--neon-cyan), #fff);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            margin-bottom: 12px;
        }
        .tech-tags { margin-top: 25px; display: flex; gap: 10px; }
        .tech-tags span {
            background: rgba(0, 229, 255, 0.1); color: var(--neon-cyan);
            padding: 6px 14px; border-radius: 10px; font-weight: 600; font-size: 0.85rem;
        }

        /* =========================================
           NUEVA TARJETA: Video Local
           ========================================= */
        .video-card {
            background: linear-gradient(135deg, #0A1428, #101F3C);
        }
        .video-container-grid {
            display: flex;
            align-items: center;
            gap: 30px;
        }
        .video-info { flex: 1; }
        .video-info h3 { font-size: 2rem; font-weight: 800; margin-bottom: 12px; color: var(--neon-cyan); }
        .video-info p { color: rgba(255,255,255,0.8); margin-bottom: 15px; font-size: 1.05rem; }
        .video-badge {
            display: inline-block; background: rgba(204, 255, 0, 0.15); color: var(--flashy-yellow);
            padding: 6px 14px; border-radius: 20px; font-size: 0.85rem; font-weight: 700;
        }
        .video-wrapper {
            flex: 1.2; border-radius: 20px; overflow: hidden; box-shadow: 0 15px 35px rgba(0,0,0,0.5);
            border: 2px solid rgba(0, 229, 255, 0.3);
        }
        .video-wrapper video {
            width: 100%; display: block; height: 260px; object-fit: cover;
        }

        /* =========================================
           NUEVA TARJETA: Estadísticas con CSS Puro
           ========================================= */
        .stats-card {
            background: #070E1B;
            border: 1px solid rgba(0, 229, 255, 0.15);
        }
        .stats-header { text-align: center; margin-bottom: 35px; }
        .stats-header h3 { font-size: 2.2rem; font-weight: 800; color: var(--pure-white); }
        .stats-header p { color: rgba(255,255,255,0.6); font-size: 1rem; margin-top: 5px; }

        .stats-grid-container {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 40px;
        }

        .chart-box {
            background: rgba(10, 20, 40, 0.7);
            padding: 30px;
            border-radius: 25px;
            border: 1px solid rgba(255,255,255,0.05);
        }
        .chart-box h4 { font-size: 1.2rem; font-weight: 700; margin-bottom: 25px; color: var(--neon-cyan); text-align: center; }

        /* Gráfico de barras hecho con degradados CSS */
        .css-bar-chart {
            display: flex;
            justify-content: space-around;
            align-items: flex-end;
            height: 180px;
            padding-top: 20px;
            border-bottom: 2px solid rgba(255,255,255,0.1);
        }
        .bar-group {
            display: flex; flex-direction: column; align-items: center; height: 100%; justify-content: flex-end;
            gap: 8px; width: 30%;
        }
        .bar-value { font-size: 0.85rem; font-weight: 700; color: var(--pure-white); }
        .bar {
            width: 100%; border-radius: 8px 8px 0 0;
            transition: height 1s ease;
        }
        .bar.traditional { background: linear-gradient(to top, #FF4B2B, #FF416C); }
        .bar.waysmart { background: linear-gradient(to top, var(--electric-blue), var(--neon-cyan)); }
        .bar.optimized { background: linear-gradient(to top, #11998e, #38ef7d); }
        .bar-label { font-size: 0.8rem; color: rgba(255,255,255,0.7); text-align: center; }

        /* Gráfico de pastel / rosquilla simulado con CSS Conic-Gradient */
        .css-pie-container {
            display: flex;
            align-items: center;
            justify-content: space-around;
            height: 180px;
        }
        .pie-chart-mock {
            width: 130px; height: 130px;
            border-radius: 50%;
            background: conic-gradient(
                var(--neon-cyan) 0% 45%,
                var(--electric-blue) 45% 80%,
                var(--flashy-yellow) 80% 100%
            );
            position: relative;
            display: flex; align-items: center; justify-content: center;
            box-shadow: 0 0 20px rgba(0, 229, 255, 0.2);
        }
        .pie-hole {
            width: 80px; height: 80px; background: #0A1428; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
        }
        .pie-center-text { font-weight: 800; font-size: 0.95rem; color: var(--pure-white); }
        .pie-legend { list-style: none; display: flex; flex-direction: column; gap: 10px; font-size: 0.85rem; }
        .pie-legend li { display: flex; align-items: center; gap: 8px; color: rgba(255,255,255,0.8); }
        .dot { width: 12px; height: 12px; border-radius: 4px; }
        .dot.d1 { background: var(--neon-cyan); }
        .dot.d2 { background: var(--electric-blue); }
        .dot.d3 { background: var(--flashy-yellow); }

        /* =========================================
           NUEVA TARJETA: Preguntas Frecuentes (FAQ)
           ========================================= */
        .faq-card {
            background: #0A1428;
        }
        .faq-header { text-align: center; margin-bottom: 35px; }
        .faq-header h3 { font-size: 2.2rem; font-weight: 800; }
        .faq-header p { color: rgba(255,255,255,0.6); }

        .faq-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 25px;
        }
        .faq-item {
            background: rgba(255, 255, 255, 0.03);
            padding: 25px;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.05);
            transition: border-color 0.3s;
        }
        .faq-item:hover { border-color: var(--neon-cyan); }
        .faq-item h4 { font-size: 1.1rem; color: var(--neon-cyan); margin-bottom: 10px; font-weight: 700; }
        .faq-item p { font-size: 0.95rem; color: rgba(255, 255, 255, 0.7); }

        /* =========================================
           Footer
           ========================================= */
        .site-footer {
            grid-area: footer;
            text-align: center;
            padding: 50px;
            background-color: #030810;
        }
        .site-footer h2 {
            font-weight: 900; font-size: 2rem;
            background: linear-gradient(45deg, var(--electric-blue), var(--neon-cyan));
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }
        .site-footer p { color: rgba(255,255,255,0.5); font-weight: 500; }

        /* =========================================
           ESTILOS DE VENTANAS MODALES (Mini Ventanas)
           ========================================= */
        .modal-overlay {
            position: fixed; inset: 0; background: rgba(0, 0, 0, 0.75);
            backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
            display: flex; align-items: center; justify-content: center;
            z-index: 1000;
            opacity: 0; pointer-events: none;
            transition: opacity 0.3s ease;
        }
        .modal-overlay.active { opacity: 1; pointer-events: auto; }

        .modal-content {
            background: #0E1A33;
            width: 100%; max-width: 450px;
            padding: 40px; border-radius: 30px;
            border: 1px solid rgba(0, 229, 255, 0.3);
            box-shadow: 0 25px 50px rgba(0,0,0,0.6);
            position: relative;
            transform: translateY(20px);
            transition: transform 0.3s ease;
        }
        .modal-overlay.active .modal-content { transform: translateY(0); }

        .close-btn {
            position: absolute; top: 20px; right: 20px;
            background: transparent; border: none; color: rgba(255,255,255,0.6);
            font-size: 1.8rem; cursor: pointer; transition: color 0.2s;
        }
        .close-btn:hover { color: var(--pure-white); }

        .modal-header h2 { font-size: 1.8rem; font-weight: 800; margin-bottom: 5px; color: var(--neon-cyan); }
        .modal-header p { font-size: 0.9rem; color: rgba(255,255,255,0.6); margin-bottom: 25px; }

        .modal-form { display: flex; flex-direction: column; gap: 18px; }
        .form-group { display: flex; flex-direction: column; gap: 6px; }
        .form-group label { font-size: 0.85rem; font-weight: 600; color: rgba(255,255,255,0.8); }
        .form-group input, .form-group select {
            background: rgba(4, 11, 22, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 12px 16px; border-radius: 12px; color: var(--pure-white);
            font-family: 'Poppins', sans-serif; font-size: 0.95rem;
            outline: none; transition: border-color 0.3s;
        }
        .form-group input:focus, .form-group select:focus { border-color: var(--neon-cyan); }
        .form-group select option { background: #0E1A33; color: var(--pure-white); }

        .btn-submit {
            background: linear-gradient(135deg, var(--electric-blue), var(--neon-cyan));
            color: var(--pure-white); border: none; padding: 14px; border-radius: 12px;
            font-weight: 800; font-size: 0.95rem; cursor: pointer; text-transform: uppercase;
            letter-spacing: 1px; margin-top: 10px; transition: transform 0.2s, box-shadow 0.2s;
        }
        .btn-submit:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(0,85,255,0.4); }
        .form-hint { font-size: 0.75rem; text-align: center; color: rgba(255,255,255,0.4); margin-top: 5px; }

        /* =========================================
           Responsive General
           ========================================= */
        @media (max-width: 1024px) {
            .grid-main { grid-template-columns: repeat(2, 1fr); }
            .bento-hero, .bento-wide, .bento-full { grid-column: span 2; }
            .video-container-grid, .stats-grid-container, .faq-grid { flex-direction: column; grid-template-columns: 1fr; }
        }

        @media (max-width: 768px) {
            .header-content h1 { font-size: 3rem; }
            .grid-main { grid-template-columns: 1fr; }
            .bento-hero, .bento-solid, .bento-wide, .bento-full { grid-column: 1 / -1; }
            .nav-links { display: none; }
        }
    </style>
    <!-- Fuente moderna e impactante -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800;900&display=swap" rel="stylesheet">
</head>
<body>

    <!-- Navegación Flotante con Botones de Acceso (Modals/Triggers) -->
    <nav class="main-nav">
        <div class="nav-brand">
            <div class="logo-icon">WS</div>
            <h2>WaySmart</h2>
        </div>
        <ul class="nav-links">
            <li><a href="#intro">Inicio</a></li>
            <li><a href="#solucion">IA Generativa</a></li>
            <li><a href="#video-section">Demo</a></li>
            <li><a href="#estadisticas">Métricas</a></li>
            <li><a href="#faq">FAQ</a></li>
        </ul>
        <div class="nav-actions">
            <button class="btn-secondary" id="openLogin">Iniciar Sesión</button>
            <button class="btn-primary" id="openRegister">Registrarse</button>
        </div>
    </nav>

    <!-- Header / Hero Section con Degradado Animado -->
    <header class="site-header">
        <div class="header-content">
            <span class="badge-neon">v 2.0.0 - Fase de Prueba</span>
            <h1>Logística Urbana<br>Reinventada con <span>IA</span></h1>
            <p>WaySmart optimiza rutas en milisegundos, empoderando a los repartidores con tecnología predictiva de última generación.</p>
        </div>
        <div class="blob blob-1"></div>
        <div class="blob blob-2"></div>
    </header>

    <!-- Contenedor Principal: Bento Grid Moderno Expandido -->
    <main class="grid-main">

        <!-- Card 1: Intro (Imagen de fondo gigante) -->
        <article id="intro" class="research-section bento-hero has-bg-image">
            <img src="https://images.unsplash.com/photo-1617469165786-8007eda3caa7?auto=format&fit=crop&q=80&w=1200" alt="Repartidor velocidad" class="bg-img">
            <div class="content-overlay">
                <h3>El Futuro del Reparto</h3>
                <p>Nuestra plataforma conecta la inmediatez humana con la inteligencia de datos a gran escala.</p>
            </div>
        </article>

        <!-- Card 2: Problema -->
        <article id="problem" class="research-section bento-solid neon-blue-bg">
            <div class="content">
                <div class="icon-big">🚧</div>
                <h3>El Caos del Tráfico</h3>
                <p>Rutas superpuestas y embotellamientos destruyen los márgenes de ganancia y el tiempo de los repartidores. Es hora de evolucionar.</p>
            </div>
        </article>

        <!-- Card 3: Solución (IA Generativa) -->
        <article id="solucion" class="research-section bento-solid dark-bg outline-glow">
            <div class="content">
                <h3 class="gradient-text">Motor IA Generativo</h3>
                <p>Nuestros algoritmos generan cientos de escenarios de rutas por segundo, seleccionando la óptima basándose en datos históricos y eventos en curso.</p>
                <div class="tech-tags">
                    <span>Machine Learning</span>
                    <span>Redes Neuronales</span>
                </div>
            </div>
        </article>

        <!-- Card NUEVA: Video Ilustrativo Local -->
        <article id="video-section" class="research-section bento-wide video-card">
            <div class="video-container-grid">
                <div class="video-info">
                    <h3>Demostración en Acción</h3>
                    <p>Observa cómo nuestra IA recalcula rutas urbanas en tiempo real ante imprevistos viales, reduciendo drásticamente los tiempos muertos del repartidor.</p>
                    <span class="video-badge">▶ Video Local Integrado</span>
                </div>
                <div class="video-wrapper">
                    <!-- Configurado para tu video local llamado 'waysmart-demo.mp4' -->
                    <video controls autoplay loop>
                        <source src="./src/video/WaySmart ALPHA.mp4" type="video/mp4">
                        Tu navegador no soporta la reproducción de videos locales.
                    </video>
                </div>
            </div>
        </article>

        <!-- Card NUEVA: Estadísticas de Repartidores (Gráficos puros con CSS) -->
        <article id="estadisticas" class="research-section bento-full stats-card">
            <div class="stats-header">
                <h3>Rendimiento y Tiempos de Repartidores</h3>
                <p>Comparativa de eficiencia operativa antes y después de implementar WaySmart (Minutos por entrega)</p>
            </div>
            <div class="stats-grid-container">
                <!-- Gráfico de Barras CSS -->
                <div class="chart-box">
                    <h4>Tiempo Promedio por Ruta (Min)</h4>
                    <div class="css-bar-chart">
                        <div class="bar-group">
                            <span class="bar-value">45m</span>
                            <div class="bar traditional" style="height: 90%;"></div>
                            <span class="bar-label">Tradicional</span>
                        </div>
                        <div class="bar-group">
                            <span class="bar-value">32m</span>
                            <div class="bar waysmart" style="height: 64%;"></div>
                            <span class="bar-label">WaySmart IA</span>
                        </div>
                        <div class="bar-group">
                            <span class="bar-value">25m</span>
                            <div class="bar optimized" style="height: 50%;"></div>
                            <span class="bar-label">IA + Tráfico Real</span>
                        </div>
                    </div>
                </div>

                <!-- Gráfico de Pastel / Progreso CSS -->
                <div class="chart-box">
                    <h4>Distribución de Tiempo Ahorrado</h4>
                    <div class="css-pie-container">
                        <div class="pie-chart-mock">
                            <div class="pie-slice slice-1"></div>
                            <div class="pie-slice slice-2"></div>
                            <div class="pie-slice slice-3"></div>
                            <div class="pie-hole">
                                <span class="pie-center-text">100%</span>
                            </div>
                        </div>
                        <ul class="pie-legend">
                            <li><span class="dot d1"></span> Tráfico Evitado (45%)</li>
                            <li><span class="dot d2"></span> Optimización de Destinos (35%)</li>
                            <li><span class="dot d3"></span> Tiempos de Espera (20%)</li>
                        </ul>
                    </div>
                </div>
            </div>
        </article>

        <!-- Card NUEVA: Preguntas Frecuentes (FAQ) -->
        <article id="faq" class="research-section bento-full faq-card">
            <div class="faq-header">
                <h3>Preguntas Frecuentes</h3>
                <p>Todo lo que necesitas saber sobre la plataforma y su funcionamiento.</p>
            </div>
            <div class="faq-grid">
                <div class="faq-item">
                    <h4>¿Cómo funciona la IA Generativa en WaySmart?</h4>
                    <p>La IA analiza patrones masivos de tráfico urbano y congestión en tiempo real para generar múltiples alternativas de rutas en segundos, eligiendo la de menor fricción.</p>
                </div>
                <div class="faq-item">
                    <h4>¿Qué necesito para registrarme como Conductor?</h4>
                    <p>Solo requieres registrarte mediante el botón superior, completar tus datos de vehículo y comenzar a recibir rutas dinámicas desde tu teléfono móvil.</p>
                </div>
                <div class="faq-item">
                    <h4>¿Es compatible con cualquier dispositivo GPS?</h4>
                    <p>Sí, WaySmart cuenta con geolocalización nativa integrada adaptable a cualquier smartphone sin requerir hardware externo costoso.</p>
                </div>
                <div class="faq-item">
                    <h4>¿Qué pasa si no tengo conexión a internet estable?</h4>
                    <p>La plataforma cuenta con caché predictivo local que almacena los tramos críticos de la ruta generada ante breves cortes de red.</p>
                </div>
            </div>
        </article>

    </main>

    <!-- Footer -->
    <footer class="site-footer">
        <h2>WaySmart</h2>
        <p>Rompiendo los límites de la logística. ⚡ 2026</p>
    </footer>

    <!-- ==========================================
       VENTANAS MODALES (Mini Ventanas Flotantes)
       ========================================== -->

    <!-- Modal de Iniciar Sesión (Con roles y datos fijos simulados) -->
    <div id="loginModal" class="modal-overlay">
        <div class="modal-content">
            <button class="close-btn" id="closeLogin">&times;</button>
            <div class="modal-header">
                <h2>Iniciar Sesión</h2>
                <p>Selecciona tu rol e ingresa tus credenciales preconfiguradas.</p>
            </div>
            <form id="loginForm" class="modal-form">
                <div class="form-group">
                    <label for="loginRole">Rol de Usuario</label>
                    <select id="loginRole" required>
                        <option value="conductor">Conductor (Ej: conductor@waysmart.com)</option>
                        <option value="representante">Representante (Ej: rep@waysmart.com)</option>
                        <option value="admin">Administrador (Ej: admin@waysmart.com)</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="loginUser">Usuario / Correo</label>
                    <input type="text" id="loginUser" value="conductor@waysmart.com" required>
                </div>
                <div class="form-group">
                    <label for="loginPass">Contraseña (Fija: 1234)</label>
                    <input type="password" id="loginPass" value="1234" required>
                </div>
                <button type="submit" class="btn-submit">Entrar al Sistema</button>
                <p class="form-hint">Simulación de acceso seguro local con valores predefinidos.</p>
            </form>
        </div>
    </div>

    <!-- Modal de Registro -->
    <div id="registerModal" class="modal-overlay">
        <div class="modal-content">
            <button class="close-btn" id="closeRegister">&times;</button>
            <div class="modal-header">
                <h2>Registro de Cuenta</h2>
                <p>Crea tu perfil para unirte a la red logística inteligente.</p>
            </div>
            <form id="registerForm" class="modal-form">
                <div class="form-group">
                    <label for="regName">Nombre Completo</label>
                    <input type="text" id="regName" placeholder="Ej. Carlos Mendoza" required>
                </div>
                <div class="form-group">
                    <label for="regEmail">Correo Electrónico</label>
                    <input type="email" id="regEmail" placeholder="carlos@correo.com" required>
                </div>
                <div class="form-group">
                    <label for="regRole">Tipo de Perfil</label>
                    <select id="regRole">
                        <option value="conductor">Repartidor / Conductor</option>
                        <option value="representante">Representante Logístico</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="regPass">Contraseña</label>
                    <input type="password" id="regPass" placeholder="••••••••" required>
                </div>
                <button type="submit" class="btn-submit">Completar Registro</button>
            </form>
        </div>
    </div>

    <!-- Script JavaScript para controlar las modales y el inicio de sesión simulado -->
    <script>
        // Referencias elementos Modal Login
        const loginModal = document.getElementById('loginModal');
        const openLogin = document.getElementById('openLogin');
        const closeLogin = document.getElementById('closeLogin');

        // Referencias elementos Modal Register
        const registerModal = document.getElementById('registerModal');
        const openRegister = document.getElementById('openRegister');
        const closeRegister = document.getElementById('closeRegister');

        // Abrir / Cerrar Login
        openLogin.addEventListener('click', () => loginModal.classList.add('active'));
        closeLogin.addEventListener('click', () => loginModal.classList.remove('active'));

        // Abrir / Cerrar Registro
        openRegister.addEventListener('click', () => registerModal.classList.add('active'));
        closeRegister.addEventListener('click', () => registerModal.classList.remove('active'));

        // Cerrar al hacer clic fuera del contenido modal
        window.addEventListener('click', (e) => {
            if (e.target === loginModal) loginModal.classList.remove('active');
            if (e.target === registerModal) registerModal.classList.remove('active');
        });

        // Simulación de Inicio de Sesión y redirección a otra página (programa funcionando)
        const loginForm = document.getElementById('loginForm');
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const pass = document.getElementById('loginPass').value;
            
            // Verificación de valor fijo de contraseña establecida
            if (pass === '1234') {
                alert('¡Inicio de sesión exitoso! Redirigiendo al programa en funcionamiento...');
                // Redirección simulada a la página interna de la aplicación (crearás 'app.html' posteriormente)
                window.location.href = 'app.html';
            } else {
                alert('Contraseña incorrecta. Utiliza la contraseña fija: 1234');
            }
        });

        // Simulación de Registro
        const registerForm = document.getElementById('registerForm');
        registerForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('¡Registro simulado completado con éxito! Ahora puedes Iniciar Sesión.');
            registerModal.classList.remove('active');
        });
    </script>
</body>
</html>
                                
""")), 
 
    path('variante-1', lambda request: HttpResponse("""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WaySmart.com - Popayán</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        body { font-family: 'Inter', system-ui, sans-serif; }
        
        .map-container {
            height: 620px;
            border-radius: 24px;
            overflow: hidden;
            box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25);
        }
    </style>
</head>
<body class="bg-zinc-50 dark:bg-zinc-950 text-zinc-900 dark:text-white transition-all">

    <!-- LOGIN -->
    <div id="login-screen" class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-zinc-900 dark:to-blue-950">
        <div class="max-w-md w-full mx-4">
            <div class="bg-white dark:bg-zinc-900 rounded-3xl p-12 shadow-2xl border border-zinc-200 dark:border-white/10">
                <div class="flex justify-center mb-10">
                    <div class="flex items-center gap-4">
                        <div class="w-16 h-16 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-3xl flex items-center justify-center text-white font-black text-5xl shadow-inner">W</div>
                        <div>
                            <h1 class="text-5xl font-bold tracking-tighter">WaySmart</h1>
                            <p class="text-blue-600 dark:text-blue-400 text-lg">Popayán</p>
                        </div>
                    </div>
                </div>
                <h2 class="text-center text-2xl font-medium mb-10 text-gray-700 dark:text-gray-300">Inicia sesión para gestionar tus rutas y entregas</h2>
                
                <form onsubmit="login(event)">
                    <input type="email" value="fernando.g@waysmart.co" class="w-full px-6 py-5 bg-zinc-100 dark:bg-zinc-800 border border-zinc-300 dark:border-white/20 rounded-2xl focus:border-blue-500 outline-none mb-4">
                    <input type="password" value="demo123" class="w-full px-6 py-5 bg-zinc-100 dark:bg-zinc-800 border border-zinc-300 dark:border-white/20 rounded-2xl focus:border-blue-500 outline-none mb-6">
                    <button type="submit" class="w-full bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-5 rounded-2xl text-xl font-semibold hover:brightness-110 transition">Iniciar Sesión</button>
                </form>
            </div>
        </div>
    </div>

    <!-- DASHBOARD -->
    <div id="dashboard" class="hidden min-h-screen">
        <!-- Navbar -->
        <nav class="bg-white dark:bg-zinc-900 border-b border-zinc-200 dark:border-white/10 sticky top-0 z-50">
            <div class="max-w-screen-2xl mx-auto px-8 py-5 flex items-center justify-between">
                <div class="flex items-center gap-4">
                    <div class="w-11 h-11 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-2xl flex items-center justify-center text-white font-black text-4xl">W</div>
                    <div>
                        <h1 class="text-3xl font-bold">WaySmart</h1>
                        <p class="text-xs text-blue-600 dark:text-blue-400">Popayán • Tiempo real</p>
                    </div>
                </div>
                
                <div class="flex items-center gap-4">
                    <div class="relative w-80">
                        <i class="fa-solid fa-magnifying-glass absolute left-4 top-1/2 -translate-y-1/2 text-zinc-400"></i>
                        <input id="address-input" 
                               type="text" 
                               placeholder="Buscar dirección en Popayán (ej: Parque Caldas)" 
                               class="w-full bg-white dark:bg-zinc-800 border border-zinc-300 dark:border-white/20 pl-11 py-3 rounded-2xl focus:border-blue-500 outline-none text-sm">
                    </div>
                    <button onclick="searchAddress()" 
                            class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-2xl font-medium transition">
                        Agregar
                    </button>
                </div>

                <div class="flex items-center gap-4">
                    <button onclick="toggleTheme()" class="p-3 rounded-2xl hover:bg-zinc-100 dark:hover:bg-zinc-800 transition">
                        <i id="theme-icon" class="fa-solid fa-moon text-2xl"></i>
                    </button>
                    <button onclick="newRoute()" class="flex items-center gap-3 bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-2xl font-medium transition">
                        <i class="fa-solid fa-plus"></i> Nueva Ruta
                    </button>
                    <button onclick="optimizeRoute()" class="flex items-center gap-3 bg-emerald-600 hover:bg-emerald-700 text-white px-6 py-3 rounded-2xl font-medium transition">
                        <i class="fa-solid fa-brain"></i> Optimizar IA
                    </button>
                    <button onclick="logout()" class="flex items-center gap-3 bg-red-600 hover:bg-red-700 text-white px-6 py-3 rounded-2xl font-medium transition">
                        <i class="fa-solid fa-right-from-bracket"></i> Salir
                    </button>
                </div>
            </div>
        </nav>

        <div class="max-w-screen-2xl mx-auto px-8 py-8">
            <div class="grid grid-cols-12 gap-8">
                <!-- MAPA -->
                <div class="col-span-12 lg:col-span-8">
                    <div class="flex justify-between items-center mb-4">
                        <h2 class="text-3xl font-bold">Mapa de Popayán</h2>
                        <div id="route-status" class="px-5 py-2 bg-white dark:bg-zinc-800 rounded-2xl text-sm font-medium shadow flex items-center gap-2"></div>
                    </div>
                    <div id="map" class="map-container"></div>
                </div>

                <!-- Sidebar -->
                <div class="col-span-12 lg:col-span-4 space-y-6">
                    <div class="bg-white dark:bg-zinc-900 rounded-3xl p-7 border border-zinc-200 dark:border-white/10">
                        <h3 class="font-bold text-xl mb-6 flex items-center gap-3"><i class="fa-solid fa-truck"></i> Pedidos Activos</h3>
                        <div id="active-orders" class="space-y-6"></div>
                    </div>

                    <div class="bg-white dark:bg-zinc-900 rounded-3xl p-7 border border-zinc-200 dark:border-white/10">
                        <h3 class="font-bold text-xl mb-5">Notificaciones</h3>
                        <div class="space-y-5 text-sm">
                            <div class="flex gap-4"><i class="fa-solid fa-message text-blue-500 mt-1"></i><div>Nuevo mensaje del Soporte</div></div>
                            <div class="flex gap-4"><i class="fa-solid fa-triangle-exclamation text-amber-500 mt-1"></i><div>Tráfico en Carrera 7</div></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        let map, currentRoute = null, waypoints = [];
        let isDark = true;

        function toggleTheme() {
            isDark = !isDark;
            document.documentElement.classList.toggle('dark', isDark);
            document.getElementById('theme-icon').classList.toggle('fa-moon', isDark);
            document.getElementById('theme-icon').classList.toggle('fa-sun', !isDark);
        }

        function initMap() {
            map = L.map('map', { zoomControl: true }).setView([2.45, -76.61], 15);
            
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

            map.on('click', function(e) {
                addMarker(e.latlng);
            });
        }

        function addMarker(latlng, popupText = "Punto de ruta") {
            const marker = L.marker(latlng, { draggable: true }).addTo(map);
            marker.bindPopup(popupText).openPopup();
            marker.on('dragend', updateRoute);
            waypoints.push({ latlng: latlng, marker: marker });
            updateRoute();
        }

        function updateRoute() {
            if (currentRoute) map.removeLayer(currentRoute);
            if (waypoints.length < 2) return;

            const coords = waypoints.map(w => w.latlng);
            currentRoute = L.polyline(coords, { 
                color: '#3b82f6', 
                weight: 7.5, 
                opacity: 0.92,
                lineJoin: 'round'
            }).addTo(map);
        }

        async function searchAddress() {
            const input = document.getElementById('address-input');
            const query = input.value.trim();
            if (!query) return alert("Escribe una dirección en Popayán");

            try {
                const res = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query + ", Popayán, Colombia")}`);
                const data = await res.json();

                if (data.length > 0) {
                    const lat = parseFloat(data[0].lat);
                    const lon = parseFloat(data[0].lon);
                    map.flyTo([lat, lon], 16, { duration: 1.5 });
                    addMarker([lat, lon], data[0].display_name.split(',')[0]);
                    input.value = "";
                } else {
                    alert("No se encontró la dirección. Intenta con: Parque Caldas, Carrera 7, Universidad del Cauca, etc.");
                }
            } catch (e) {
                alert("Error al buscar dirección");
            }
        }

        function newRoute() {
            clearMap();
            document.getElementById('route-status').innerHTML = `🗺️ <span class="text-blue-600">Haz clic o busca direcciones</span>`;
        }

        function optimizeRoute() {
            clearMap();
            
            // Ruta más realista y fluida por Popayán
            const routePoints = [
                [2.4558, -76.6148], // Parque Caldas
                [2.4532, -76.6121],
                [2.4515, -76.6095], // Calle 5
                [2.4498, -76.6078],
                [2.4479, -76.6092], // Carrera 6
                [2.4462, -76.6128],
                [2.4481, -76.6159], // Centro Histórico
                [2.4510, -76.6184]  // Barrio Belén
            ];
            
            routePoints.forEach((pos, i) => {
                const popup = i === 0 ? "Inicio - Parque Caldas" : 
                             (i === routePoints.length-1 ? "Destino Final" : `Parada ${i}`);
                addMarker(pos, popup);
            });
            
            currentRoute = L.polyline(routePoints, { 
                color: '#10b981', 
                weight: 8, 
                opacity: 0.95 
            }).addTo(map);
            
            document.getElementById('route-status').innerHTML = `✨ <span class="text-emerald-600">Ruta optimizada por IA</span> • 41 min`;
        }

        function clearMap() {
            if (currentRoute) map.removeLayer(currentRoute);
            waypoints.forEach(w => map.removeLayer(w.marker));
            waypoints = [];
        }

        function login(e) {
            e.preventDefault();
            document.getElementById('login-screen').classList.add('hidden');
            document.getElementById('dashboard').classList.remove('hidden');
            setTimeout(() => {
                initMap();
                loadDemoData();
            }, 300);
        }

        function logout() {
            if (confirm("¿Cerrar sesión?")) {
                clearMap();
                document.getElementById('dashboard').classList.add('hidden');
                document.getElementById('login-screen').classList.remove('hidden');
            }
        }

        function loadDemoData() {
            document.getElementById('active-orders').innerHTML = `
                <div class="flex gap-5 border-l-4 border-blue-500 pl-4">
                    <div class="flex-1">
                        <p class="font-semibold">#WS-2024-007</p>
                        <p class="text-sm text-zinc-500">Parque Caldas → Centro Histórico</p>
                        <p class="text-emerald-600 text-sm">ETA: 10:42 AM</p>
                    </div>
                </div>
            `;
        }
    </script>
</body>
</html>

""")),   
]