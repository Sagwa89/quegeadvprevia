html_code = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Richart Advogados - Layout Personalizado</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700;800&display=swap" rel="stylesheet">
    
    <style>
        /* ==================== DESIGN SYSTEM & VARIAVEIS ==================== */
        :root {
            --bg-dark: #121214;
            --bg-light: #EBEBEB;
            --accent-gold: #D4AF37;
            --text-white: #FFFFFF;
            --text-muted: #9CA3AF;
            --text-dark: #18181B;
            --font-main: 'Montserrat', sans-serif;
            --transition-smooth: all 0.6s cubic-bezier(0.25, 1, 0.5, 1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* RESET DE BORDAS/MARGENS PARA EVITAR "BORDAS GROSSAS" */
        html, body {
            width: 100%;
            overflow-x: hidden;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: var(--font-main);
            background-color: var(--bg-dark);
            color: var(--text-white);
            -webkit-font-smoothing: antialiased;
        }

        img {
            max-width: 100%;
            display: block;
        }

        /* Container centralizador */
        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
        }

        /* ==================== ANIMAÇÕES ==================== */
        .reveal {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.8s ease-out, transform 0.8s ease-out;
        }
        
        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }
        .delay-1 { transition-delay: 0.1s; }
        .delay-2 { transition-delay: 0.2s; }

        /* ==================== HERO SECTION ==================== */
        .hero {
            position: relative;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            background: linear-gradient(rgba(18, 18, 20, 0.6), rgba(18, 18, 20, 0.95)), 
                        url('https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1920&q=80') top center/cover no-repeat;
            padding: 0 5%;
        }

        .hero h1 {
            font-size: clamp(2rem, 4vw, 3.5rem);
            font-weight: 800;
            letter-spacing: -0.02em;
            line-height: 1.2;
            text-transform: uppercase;
            max-width: 1000px;
        }

        /* ==================== ABOUT SECTION ==================== */
        .about {
            background-color: var(--bg-light);
            color: var(--text-dark);
            padding: 100px 5%;
            text-align: center;
        }

        .about h2 {
            font-size: clamp(2rem, 3vw, 2.5rem);
            font-weight: 800;
            margin-bottom: 2rem;
            color: var(--text-dark);
        }

        .about p {
            font-size: 1.15rem;
            line-height: 1.8;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
        }

        /* ==================== ÁREAS DE ATUAÇÃO ==================== */
        .practice-areas {
            background-color: var(--bg-dark);
            padding: 100px 5%;
        }

        .practice-areas .header {
            text-align: center;
            margin-bottom: 4rem;
        }

        .practice-areas h2 {
            font-size: clamp(2rem, 3vw, 2.5rem);
            font-weight: 800;
            color: var(--accent-gold);
            margin-bottom: 1rem;
        }

        .practice-areas p {
            font-size: 1.1rem;
            color: var(--text-muted);
            max-width: 700px;
            margin: 0 auto;
        }

        .areas-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
        }

        .area-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(212, 175, 55, 0.1);
            padding: 2.5rem 2rem;
            border-radius: 4px;
            transition: var(--transition-smooth);
            text-align: center;
        }

        .area-card:hover {
            border-color: var(--accent-gold);
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.05);
        }

        .area-card h3 {
            font-size: 1.2rem;
            color: var(--text-white);
        }

        /* ==================== EXPERIÊNCIA (AVALIAÇÕES) ==================== */
        .experience {
            background-color: #0D0D0F;
            padding: 100px 5%;
        }
        
        .experience h2 {
            font-size: clamp(2rem, 3vw, 2.5rem);
            font-weight: 800;
            margin-bottom: 3rem;
            text-align: center;
        }

        .reviews-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .review-card {
            background: rgba(255,255,255,0.02);
            padding: 2.5rem;
            border-left: 3px solid var(--accent-gold);
            position: relative;
        }

        .review-card::before {
            content: '"';
            position: absolute;
            top: 10px;
            left: 20px;
            font-size: 4rem;
            color: rgba(212, 175, 55, 0.2);
            font-family: serif;
            line-height: 1;
        }

        .review-text {
            font-size: 1rem;
            line-height: 1.7;
            color: #d1d5db;
            margin-bottom: 1.5rem;
            position: relative;
            z-index: 1;
        }

        .review-author {
            color: var(--accent-gold);
            font-weight: 700;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        /* ==================== ADVOGADOS (APENAS 2) ==================== */
        .team {
            background-color: var(--bg-dark);
            padding: 100px 5%;
        }

        .team h2 {
            font-size: clamp(2rem, 3vw, 2.5rem);
            font-weight: 800;
            text-align: center;
            margin-bottom: 4rem;
            color: var(--accent-gold);
        }

        .team-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 3rem;
            max-width: 800px;
            margin: 0 auto;
        }

        .member-photo {
            aspect-ratio: 3/4;
            background-color: #1A1A1C;
            overflow: hidden;
            margin-bottom: 1.5rem;
        }

        .member-photo img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: contrast(1.05) brightness(0.9);
            transition: var(--transition-smooth);
        }

        .team-member:hover .member-photo img {
            transform: scale(1.03);
            filter: contrast(1) brightness(1.1);
        }

        .team-member {
            text-align: center;
        }

        .member-name {
            font-size: 1.3rem;
            font-weight: 700;
            margin-bottom: 0.3rem;
        }
        
        .member-role {
            font-size: 0.9rem;
            color: var(--text-muted);
        }

        /* ==================== CONTEÚDO ==================== */
        .content-section {
            background-color: var(--bg-light);
            color: var(--text-dark);
            padding: 100px 5%;
        }

        .content-header {
            text-align: center;
            margin-bottom: 4rem;
        }

        .content-header h2 {
            font-size: clamp(2rem, 3vw, 2.5rem);
            font-weight: 800;
            margin-bottom: 1rem;
        }

        .content-header p {
            font-size: 1.1rem;
            color: #444;
            max-width: 700px;
            margin: 0 auto;
            line-height: 1.6;
        }

        .authors-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 2rem;
            max-width: 600px;
            margin: 0 auto;
        }

        .author-card {
            display: flex;
            align-items: center;
            gap: 1rem;
            background: #fff;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }

        .author-photo {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            overflow: hidden;
        }

        .author-photo img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .author-info h4 {
            font-size: 1rem;
            font-weight: 700;
            color: var(--text-dark);
        }

        .author-info span {
            font-size: 0.8rem;
            color: #666;
        }

        /* ==================== FOOTER / CTA ==================== */
        .footer-cta {
            background: linear-gradient(rgba(18, 18, 20, 0.85), rgba(18, 18, 20, 0.95)), 
                        url('https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1920&q=80') center/cover fixed;
            padding: 120px 5%;
            text-align: center;
            border-top: 2px solid var(--accent-gold);
        }

        .footer-cta h2 {
            font-size: clamp(1.8rem, 4vw, 3rem);
            font-weight: 800;
            color: var(--text-white);
            max-width: 900px;
            margin: 0 auto 2rem auto;
            line-height: 1.3;
        }

        .cta-btn {
            display: inline-block;
            background-color: var(--accent-gold);
            color: #000;
            padding: 1rem 2.5rem;
            font-size: 1.1rem;
            font-weight: 700;
            text-decoration: none;
            border-radius: 4px;
            transition: var(--transition-smooth);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .cta-btn:hover {
            background-color: #e6c24a;
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(212, 175, 55, 0.2);
        }

        /* ==================== RESPONSIVO ==================== */
        @media (max-width: 768px) {
            .team-grid, .authors-grid { grid-template-columns: 1fr; }
            section { padding: 70px 5%; }
            .author-card { flex-direction: column; text-align: center; }
        }
    </style>
</head>
<body>

    <!-- HERO SECTION -->
    <section class="hero">
        <div class="container reveal">
            <h1>COMPROMETIDOS COM A<br>EXCELÊNCIA JURÍDICA<br>E EMPRESARIAL</h1>
        </div>
    </section>

    <!-- ABOUT SECTION -->
    <section class="about">
        <div class="container reveal">
            <h2>Tradição e Inovação na Advocacia Empresarial</h2>
            <p>Fundado em 2002, o Richart Advogados Empresarial consolidou sua reputação a partir de uma atuação pautada pela ética, excelência técnica e segurança jurídica. Com presença estratégica nas áreas do Direito Empresarial, Trabalhista Empresarial, Tributário e Recuperação de Crédito, o escritório dispõe de estrutura física contemporânea e cuidadosamente planejada, que reflete seu padrão de atendimento, discrição e eficiência.</p>
        </div>
    </section>

    <!-- ÁREAS DE ATUAÇÃO -->
    <section class="practice-areas">
        <div class="container">
            <div class="header reveal">
                <h2>Áreas de atuação</h2>
                <p>O Direito como vetor de segurança, estratégia e soluções para a dinâmica empresarial.</p>
            </div>
            
            <div class="areas-grid reveal delay-1">
                <div class="area-card">
                    <h3>Direito Empresarial</h3>
                </div>
                <div class="area-card">
                    <h3>Trabalhista Empresarial</h3>
                </div>
                <div class="area-card">
                    <h3>Tributário</h3>
                </div>
                <div class="area-card">
                    <h3>Recuperação de Crédito</h3>
                </div>
            </div>
        </div>
    </section>

    <!-- EXPERIÊNCIA (AVALIAÇÕES) -->
    <section class="experience">
        <div class="container">
            <h2 class="reveal">Experiência</h2>
            <div class="reviews-grid reveal delay-1">
                <div class="review-card">
                    <p class="review-text">A atuação estratégica e preventiva do escritório foi fundamental para a reestruturação societária do nosso grupo. Segurança e precisão em cada detalhe.</p>
                    <span class="review-author">Diretoria - Setor Industrial</span>
                </div>
                <div class="review-card">
                    <p class="review-text">Atendimento ágil e soluções jurídicas que realmente compreendem a dinâmica e velocidade que o mercado exige atualmente.</p>
                    <span class="review-author">CEO - Tecnologia e Logística</span>
                </div>
                <div class="review-card">
                    <p class="review-text">Parceiros indispensáveis no nosso dia a dia tributário. A excelência técnica da equipe reflete diretamente na nossa segurança financeira.</p>
                    <span class="review-author">CFO - Comércio Varejista</span>
                </div>
            </div>
        </div>
    </section>

    <!-- TEAM (2 ADVOGADOS) -->
    <section class="team">
        <div class="container">
            <h2 class="reveal">Sócios Fundadores</h2>
            <div class="team-grid">
                <div class="team-member reveal delay-1">
                    <div class="member-photo"><img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=600&q=80" alt="Paulo Richart"></div>
                    <div class="member-name">Paulo Richart</div>
                    <div class="member-role">Sócio Administrador</div>
                </div>
                <div class="team-member reveal delay-2">
                    <div class="member-photo"><img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=600&q=80" alt="Ana Clara"></div>
                    <div class="member-name">Ana Clara Silva</div>
                    <div class="member-role">Sócia</div>
                </div>
            </div>
        </div>
    </section>

    <!-- CONTEÚDO E PERFIS -->
    <section class="content-section">
        <div class="container">
            <div class="content-header reveal">
                <h2>Conteúdo</h2>
                <p>Dia a dia, publicações institucionais voltadas à atualização jurídica e à prática empresarial. Nos acompanhe</p>
            </div>
            
            <div class="authors-grid reveal delay-1">
                <div class="author-card">
                    <div class="author-photo">
                        <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=150&q=80" alt="Advogado 1">
                    </div>
                    <div class="author-info">
                        <h4>Paulo Richart</h4>
                        <span>Artigos sobre Direito Societário</span>
                    </div>
                </div>
                <div class="author-card">
                    <div class="author-photo">
                        <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=150&q=80" alt="Advogado 2">
                    </div>
                    <div class="author-info">
                        <h4>Ana Clara Silva</h4>
                        <span>Atualizações Tributárias</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- FOOTER CTA -->
    <footer class="footer-cta">
        <div class="container reveal">
            <h2>Venha nos visitar e conversar sobre o futuro da sua empresa.</h2>
            <a href="#" class="cta-btn">Agendar Reunião</a>
        </div>
    </footer>

    <!-- SCRIPT DE ANIMAÇÕES -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const observerOptions = {
                root: null,
                rootMargin: '0px',
                threshold: 0.1
            };

            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('active');
                        observer.unobserve(entry.target);
                    }
                });
            }, observerOptions);

            const revealElements = document.querySelectorAll('.reveal');
            revealElements.forEach(el => observer.observe(el));
        });
    </script>
</body>
</html>
"""

with open("index_customizado.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("HTML customizado gerado.")