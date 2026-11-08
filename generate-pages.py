from pathlib import Path
from learning_content import enrich_home, enrich_course, render_course_modules

out = Path(__file__).parent / 'dist'
arrow = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15M13 5l7 7-7 7"/></svg>'
instagram_url = 'https://www.instagram.com/p/DVgxQACjqm5/?utm_source=ig_web_copy_link&amp;rpxt=NTc4MTIwNjQ2YQ=='
linkedin_url = 'https://www.linkedin.com/company/dxigenius/posts/?feedView=all'
instagram_svg = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14.5 3.5H8A4.5 4.5 0 0 0 3.5 8v8A4.5 4.5 0 0 0 8 20.5h8a4.5 4.5 0 0 0 4.5-4.5V9"/><circle cx="12" cy="12" r="4"/><circle cx="19.2" cy="4.8" r="1.7" class="social-dot"/></svg>'
linkedin_svg = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="5" cy="5" r="1.8" class="social-dot"/><path d="M5 9v11M10 20V9m0 4.5a5 5 0 0 1 10 0V20"/></svg>'
map_link = 'https://share.google/lfxev3K2xydDn5Gm1'
map_embed = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3984.155314781682!2d-59.9839749!3d-3.1348123!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x926c0542387e6a7d%3A0xbcf4a7978d3807a9!2sPolo%20de%20Inova%C3%A7%C3%A3o%20IFAM!5e0!3m2!1spt-BR!2sbr!4v1700000000000!5m2!1spt-BR!2sbr'
links = [('index.html','Início'),('curso.html','Curso'),('portfolio.html','Portfólio'),('contato.html','Contato')]

def header(active):
    nav = ''.join(f'<a href="{href}"' + (' aria-current="page"' if href == active else '') + f'>{label}</a>' for href,label in links)
    return f'''<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header"><div class="header-pattern" data-lg-pattern="g" aria-hidden="true"></div><div class="wrap nav-shell">
  <a class="brand" href="index.html" aria-label="AX Academy — início"><img class="brand-light" src="assets/ax-logo.png" alt="AX Academy"><img class="brand-dark" src="assets/ax-logo-dark-red.png" alt="AX Academy"></a>
  <nav class="nav-links" id="primary-nav" aria-label="Navegação principal">{nav}</nav>
  <div class="nav-actions"><a class="social-link" href="{instagram_url}" target="_blank" rel="noopener noreferrer" aria-label="Instagram da DXI (abre em nova aba)">{instagram_svg}</a><a class="social-link" href="{linkedin_url}" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn da DXI (abre em nova aba)">{linkedin_svg}</a><button class="theme-toggle" data-theme-toggle aria-label="Alternar tema"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M4.93 4.93l1.41 1.41m11.32 11.32 1.41 1.41M19.07 4.93l-1.41 1.41M6.34 17.66l-1.41 1.41"/></svg></button><button class="menu-toggle" data-menu aria-expanded="false" aria-controls="primary-nav" aria-label="Abrir menu"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 8h16M4 16h16"/></svg></button></div>
</div></header>'''

def footer():
    nav = ''.join(f'<a href="{href}">{label}</a>' for href,label in links)
    return f'''<footer class="footer"><div class="wrap"><div class="footer-main"><div><a class="brand" href="index.html"><img class="brand-light" src="assets/ax-logo.png" alt="AX Academy"><img class="brand-dark" src="assets/ax-logo-dark-red.png" alt="AX Academy"></a><p>Conhecimento em automação para transformar ideias em soluções.</p></div><nav class="footer-nav" aria-label="Navegação do rodapé">{nav}</nav></div><div class="footer-bottom"><span><a class="footer-credit-link" href="https://messyas.github.io/meu-site-portifolio/#contato" target="_blank" rel="noopener noreferrer">Made with love by Messyas Gois França @ 2026</a></span><div><img class="footer-lg footer-lg-light" src="assets/lg.svg" alt="LG"><img class="footer-lg footer-lg-dark" src="assets/lg-light.svg" alt="LG"></div></div></div></footer>'''

def page(filename, title, description, body, extra=''):
    theme = "try{var t=localStorage.getItem('ax-academy-theme');document.documentElement.dataset.theme=t==='dark'||t==='light'?t:(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light')}catch(e){document.documentElement.dataset.theme='light'}"
    body_class = ' class="home-page"' if filename == 'index.html' else ''
    page_header = '' if filename == 'index.html' else header(filename)
    learning_styles = '<link rel="stylesheet" href="assets/learning.css">' if filename in ('index.html', 'curso.html') else ''
    learning_script = '<script src="assets/learning.js" defer></script>' if filename in ('index.html', 'curso.html') else ''
    contact_styles = '<link rel="stylesheet" href="assets/contact.css">' if filename == 'contato.html' else ''
    html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{description}"><title>{title} | AX Academy</title><link rel="icon" href="assets/favicon-ax.svg" type="image/svg+xml"><script>{theme}</script><link rel="stylesheet" href="assets/styles.css"><link rel="stylesheet" href="assets/lg-patterns.css">{learning_styles}{contact_styles}</head><body{body_class}>{page_header}<main id="conteudo">{body}</main>{footer()}{extra}{learning_script}<script src="assets/app.js" defer></script></body></html>'''
    (out / filename).write_text(html, encoding='utf-8')

modules = [
    ('RPA com Python', '160 horas', 'Automatize tarefas, conecte sistemas e construa robôs com Python.', ['Python', 'BotCity', 'Spiders', 'Playwright', 'PyAutoGUI', 'Bibliotecas de automação', 'Telegram', 'WhatsApp', 'Gmail', 'Google Cloud', 'APIs', 'Tratamento de erros', 'Testes', 'Versionamento']),
    ('Data Science e Machine Learning', '160 horas', 'Explore dados, desenvolva modelos e acompanhe seu desempenho ao longo do tempo.', ['Data Science', 'Data Mining', 'CRISP-DM', 'EDA', 'Limpeza de dados', 'Pré-processamento', 'Regressão linear', 'Regressão logística', 'Classificação', 'Naive Bayes', 'Árvores de decisão', 'Regularização', 'Detecção de anomalias', 'K-means', 'Clusterização', 'Redes neurais', 'TensorFlow', 'Keras', 'Transformers', 'NLP', 'Tokenização', 'Vetorização', 'Análise de sentimentos', 'Data drift', 'MLflow', 'Evidently', 'Agentic AI', 'Avaliação de modelos', 'Comunicação de resultados']),
    ('Hiperautomação', '240 horas', 'Combine processos, ferramentas e serviços para automatizar fluxos de ponta a ponta.', ['BPMN', 'Docker', 'SmartOffice', 'BotCity', 'FastAPI', 'Logging', 'Orquestração de processos', 'Integração por APIs', 'Filas', 'Monitoramento', 'Observabilidade']),
    ('Agentes inteligentes', '80 horas', 'Conheça ferramentas para criar fluxos e sistemas com agentes inteligentes.', ['n8n', 'CrewAI', 'LangGraph', 'LangChain', 'Avaliação de agentes', 'Integração com ferramentas externas']),
]

rows = ''.join(f'<a class="module-row" href="curso.html#{i}"><span class="index">{i}</span><div><h3>{name}</h3><p>{description}</p></div><span class="module-meta">{duration}</span></a>' for i,(name,duration,description,topics) in enumerate(modules,1))
side_patterns = '<div class="closing-side closing-side-left" data-lg-pattern aria-hidden="true"></div><div class="closing-side closing-side-right" data-lg-pattern aria-hidden="true"></div>'
home = f'''<div class="intro-scene" data-intro-scene><div class="intro-sticky">{header('index.html')}<section class="hero"><div class="hero-art" aria-hidden="true"><canvas data-pixel-art></canvas></div><div class="hero-copy"><h1>Ideias em movimento.<br><em>Futuro em construção.</em></h1><p class="lead">Na AX Academy, tecnologia e aprendizado se encontram para transformar desafios em soluções inteligentes.</p><div class="hero-actions"><a class="button" href="curso.html">Conheça o curso</a><a class="button button-outline" href="portfolio.html">Explore os projetos</a></div></div></section></div></div>
<div class="home-content"><div class="home-band" aria-hidden="true"></div><div class="ribbon"><div class="ribbon-inner"><strong>Da automação à inteligência artificial.</strong><div class="ribbon-list"><span>Python & RPA</span><span>Ciência de dados</span><span>Hiperautomação</span><span>Agentes inteligentes</span></div></div></div>
<section class="section home-modules"><div class="section-head"><h2>Quatro módulos.<br>Um mundo de possibilidades.</h2><p>Uma jornada que conecta ferramentas, dados e processos para criar soluções com propósito.</p></div><div class="module-list">{rows}</div><p class="module-cta"><a class="formation-cta" href="curso.html"><span>Conheça a formação completa</span><i aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></i></a></p></section>
<div class="home-band" aria-hidden="true"></div><section class="closing">{side_patterns}<div class="closing-inner"><div><h2>Conheça o que estamos construindo.</h2><p>Explore projetos que aplicam automação e inteligência a desafios reais.</p></div><a class="button" href="portfolio.html">Ver portfólio</a></div></section><div class="home-band" aria-hidden="true"></div><section class="supporters" id="apoiadores" aria-labelledby="supporters-title"><h2 id="supporters-title">Apoiadores</h2><div class="supporters-logos"><div class="supporter"><img class="supporter-ifam" src="assets/ifam-logo.png" alt=""><span class="supporter-ifam-label">IFAM</span></div><div class="supporter"><img class="supporter-lg supporter-lg-light" src="assets/lg.svg" alt="LG"><img class="supporter-lg supporter-lg-dark" src="assets/lg-mosaic.png" alt="LG"></div></div></section><div class="home-band" aria-hidden="true"></div></div>'''
home = f'<div class="intro-scene" data-intro-scene><div class="intro-sticky">{header("index.html")}<section class="hero"><div class="hero-art" aria-hidden="true"><canvas data-pixel-art></canvas></div><div class="hero-copy"><h1>Ideias em movimento.<br><em>Futuro em construção.</em></h1><p class="lead">Na AX Academy, tecnologia e aprendizado se encontram para transformar desafios em soluções inteligentes.</p><div class="hero-actions"><a class="button" href="curso.html">Conheça o curso</a><a class="button button-outline" href="portfolio.html">Explore os projetos</a></div></div></section></div></div>\n<div class="home-content"><div class="home-band" aria-hidden="true"></div><div class="ribbon"><div class="ribbon-inner"><strong>Da automação à inteligência artificial.</strong><div class="ribbon-list"><span>Python & RPA</span><span>Ciência de dados</span><span>Hiperautomação</span><span>Agentes inteligentes</span></div></div></div>\n<section class="section home-modules"><div class="section-head"><h2>Quatro módulos.<br>Um mundo de possibilidades.</h2><p>Uma jornada que conecta ferramentas, dados e processos para criar soluções com propósito.</p></div><div class="module-list">{rows}</div><p class="module-cta"><a class="formation-cta" href="curso.html"><span>Conheça a formação completa</span><i aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></i></a></p></section>\n<div class="home-band" aria-hidden="true"></div><section class="closing"><div class="closing-side closing-side-left" data-lg-pattern aria-hidden="true"></div><div class="closing-side closing-side-right" data-lg-pattern aria-hidden="true"></div><div class="closing-inner"><div><h2>Conheça o que estamos construindo.</h2><p>Explore projetos que aplicam automação e inteligência a desafios reais.</p></div><a class="button" href="portfolio.html">Ver portfólio</a></div></section><div class="home-band" aria-hidden="true"></div><section class="supporters" id="apoiadores" aria-labelledby="supporters-title"><h2 id="supporters-title">Apoiadores</h2><div class="supporters-logos"><div class="supporter"><img class="supporter-ifam" src="assets/ifam-logo.png" alt=""><span class="supporter-ifam-label">IFAM</span></div><div class="supporter"><img class="supporter-lg supporter-lg-light" src="assets/lg.svg" alt="LG"><img class="supporter-lg supporter-lg-dark" src="assets/lg-mosaic.png" alt="LG"></div></div></section><div class="home-band" aria-hidden="true"></div></div>'
home = enrich_home(home)
page('index.html','Início','Conheça a AX Academy e sua formação em automação.',home)

course_sections = render_course_modules(modules)
course = f'''<div class="course-heading-frame"><div class="home-band" aria-hidden="true"></div><section class="page-heading heading-with-pattern">{side_patterns}<span class="tag">A jornada AX</span><h1>Aprender para automatizar. Criar para transformar.</h1><p class="lead">Uma formação que percorre automação, ciência de dados e inteligência artificial, com ferramentas aplicadas a diferentes desafios.</p></section></div><div class="wrap course-summary"><div class="summary-item"><strong>04</strong><span>módulos</span></div><div class="summary-item"><strong>640 horas</strong><span>de conteúdo</span></div></div><div class="wrap">{course_sections}</div><section class="section wrap"><div class="section-head"><h2>Conhecimento que ganha forma.</h2><p>Veja como a tecnologia se conecta a diferentes contextos no portfólio da AX Academy.</p></div><a class="button" href="portfolio.html">Explorar projetos</a></section>'''
course = f'<div class="home-content"><div class="home-band" aria-hidden="true"></div><section class="page-heading heading-with-pattern"><div class="closing-side closing-side-left" data-lg-pattern aria-hidden="true"></div><div class="closing-side closing-side-right" data-lg-pattern aria-hidden="true"></div><span class="tag">A jornada AX</span><h1>Aprender para automatizar. Criar para transformar.</h1><p class="lead">Uma formação que percorre automação, ciência de dados e inteligência artificial, com ferramentas aplicadas a diferentes desafios.</p></section><div class="course-summary"><div class="summary-item"><strong>04</strong><span>módulos</span></div><div class="summary-item"><strong>640 horas</strong><span>de conteúdo</span></div></div><div class="home-band" aria-hidden="true"></div><div class="course-modules">{course_sections}</div><div class="home-band" aria-hidden="true"></div><section class="closing"><div class="closing-side closing-side-left" data-lg-pattern aria-hidden="true"></div><div class="closing-side closing-side-right" data-lg-pattern aria-hidden="true"></div><div class="closing-inner"><div><h2>Conhecimento que ganha forma.</h2><p>Veja como a tecnologia se conecta a diferentes contextos no portfólio da AX Academy.</p></div><a class="button" href="portfolio.html">Explorar projetos</a></div></section><div class="home-band" aria-hidden="true"></div></div>'
course = enrich_course(course)
page('curso.html','Curso','Conheça os módulos e conteúdos da formação em automação da AX Academy.',course)

projects_data = [
    {
        'num': '01',
        'name': 'Hanaro',
        'category': 'Automação Industrial',
        'code_lang': 'Python',
        'mesh': 'mesh-blue',
        'mockup_header': 'HANARO · MONITORAMENTO INDUSTRIAL',
        'chips': [
            ('Linha SMD', True),
            ('Desperdício 0%', True),
            ('Otimização contínua', False),
            ('Visão computacional', False)
        ],
        'progress_label': 'TAXA DE REDUÇÃO DE PERDAS',
        'progress_val': '-24.8%',
        'progress_pct': '82%',
        'footer': '→ FLUXO PRODUTIVO OTIMIZADO',
        'description': 'Automação da análise de casos de desperdício que acontecem no processo produtivo.',
        'tags': ['Python', 'BotCity', 'Computer Vision', 'Pandas', 'Docker', 'RPA']
    },
    {
        'num': '02',
        'name': 'Synergia',
        'category': 'Supply Chain',
        'code_lang': 'Python · SQL',
        'mesh': 'mesh-green',
        'mockup_header': 'SYNERGIA · GESTÃO DE SUPRIMENTOS',
        'stats': [
            ('ENTREGAS', 'filled-emerald', 8, 10, '84%'),
            ('ESTOQUE', 'filled-cyan', 10, 10, '100% OK'),
            ('PENDÊNCIAS', 'filled-violet', 2, 10, 'BAIXO')
        ],
        'footer': '▲ ERP SAP SINCRONIZADO',
        'description': 'Consolidação de dados e acompanhamento de pendências de suprimentos.',
        'tags': ['Python', 'FastAPI', 'ETL', 'PostgreSQL', 'Dashboards', 'SAP']
    },
    {
        'num': '03',
        'name': 'Vigil',
        'category': 'Machine Learning',
        'code_lang': 'Machine Learning',
        'mesh': 'mesh-purple',
        'mockup_header': 'VIGIL · PADRÕES COMPORTAMENTAIS',
        'chips': [
            ('Cluster #04', True),
            ('Desvio < 0.05', True),
            ('Padrão regular', False),
            ('Detecção anomalia', False)
        ],
        'stats': [
            ('CONFIANÇA', 'filled-pink', 9, 10, '98.4%')
        ],
        'footer': '● INFERÊNCIA EM TEMPO REAL',
        'description': 'Identificação de parâmetros para classificação de padrões comportamentais.',
        'tags': ['Python', 'TensorFlow', 'Scikit-learn', 'Clusterização', 'Análise Preditiva']
    },
    {
        'num': '04',
        'name': 'Arumã',
        'category': 'Comex & Fiscal',
        'code_lang': 'Hiperautomação',
        'mesh': 'mesh-amber',
        'mockup_header': 'ARUMÃ · FISCAL & COMÉRCIO EXTERIOR',
        'stats': [
            ('DU-E / DI', 'filled-amber', 9, 10, '92%'),
            ('RECEITA', 'filled-emerald', 10, 10, 'VALIDADO'),
            ('AUDITORIA', 'filled-cyan', 10, 10, 'APROVADO')
        ],
        'footer': '✓ DESEMBARAÇO AUTOMATIZADO',
        'description': 'Automação de processos voltados à área fiscal de comércio exterior.',
        'tags': ['Python', 'Playwright', 'FastAPI', 'OCR', 'Docker', 'Comex']
    }
]

def render_project_card(p):
    # Replace each project image here when its final artwork is available.
    image = p.get('image', 'assets/hanaro-placeholder.png')
    preview = f'<div class="project-preview"><img src="{image}" alt="" loading="lazy"></div>'
    tags_html = ''.join(f'<span class="project-tag">{t}</span>' for t in p['tags'])
    content = f'<div class="project-content"><div class="project-title-row"><h2 class="project-title">{p["name"]}</h2></div><p class="project-desc">{p["description"]}</p><div class="project-tags">{tags_html}</div></div>'
    return f'<article class="project">{preview}{content}</article>'

project_cards_html = ''.join(render_project_card(p) for p in projects_data)
portfolio = f'''<div class="home-content"><div class="home-band" aria-hidden="true"></div><section class="page-heading heading-with-pattern">{side_patterns}<span class="tag">Portfólio</span><h1>Ideias que se tornam soluções.</h1><p class="lead">Conheça projetos que exploram automação e dados em diferentes contextos.</p></section><div class="home-band" aria-hidden="true"></div><section class="section portfolio-section"><div class="portfolio-grid" data-projects>{project_cards_html}</div><p class="project-note">Projetos desenvolvidos no ecossistema de formação tecnológica da AX Academy.</p><noscript><p>Hanaro: automação da análise de desperdícios no processo produtivo. Synergia: consolidação de dados e pendências de suprimentos. Vigil: classificação de padrões comportamentais. Arumã: automação fiscal de comércio exterior.</p></noscript></section><div class="home-band" aria-hidden="true"></div><section class="closing">{side_patterns}<div class="closing-inner"><div><h2>Transforme desafios em soluções.</h2><p>Conheça a estrutura completa da formação em automação da AX Academy.</p></div><a class="button" href="curso.html">Ver o curso</a></div></section><div class="home-band" aria-hidden="true"></div></div>'''
page('portfolio.html','Portfólio','Conheça os projetos Hanaro, Synergia, Vigil e Arumã.',portfolio,'<script src="assets/projects.js" defer></script>')

contact = f'''<div class="home-content contact-page-content"><div class="home-band" aria-hidden="true"></div><section class="page-heading heading-with-pattern">{side_patterns}<span class="tag">Contato</span><h1>Vamos conversar?</h1><p class="lead">Entre em contato para saber mais sobre a AX Academy, parcerias e nossa formação em tecnologia e automação.</p></section><div class="home-band" aria-hidden="true"></div><div class="contact-grid"><div class="contact-col"><div class="contact-block"><span class="contact-kicker">E-mail</span><a class="contact-value-link" href="mailto:contato@exemplo.com">contato@exemplo.com</a><p class="contact-desc">Canal de contato da formação para dúvidas gerais e atendimento.</p><span class="notice">E-mail de exemplo</span></div></div><div class="contact-col"><div class="contact-block"><span class="contact-kicker">Redes Sociais</span><p class="contact-desc">Acompanhe nossas atualizações, projetos e novidades institucionais.</p><div class="contact-social-list"><a class="contact-social-row" href="{instagram_url}" target="_blank" rel="noopener noreferrer" aria-label="Instagram da DXI (abre em nova aba)"><span class="social-icon">{instagram_svg}</span><span class="social-name">Instagram <small>@dxigenius</small></span></a><a class="contact-social-row" href="{linkedin_url}" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn da DXI (abre em nova aba)"><span class="social-icon">{linkedin_svg}</span><span class="social-name">LinkedIn <small>DXI Genius</small></span></a></div></div></div></div><div class="home-band" aria-hidden="true"></div><section class="contact-map-section"><div class="contact-map-header"><div><span class="tag">Localização</span><h2>Polo de Inovação no mapa</h2></div><a class="text-link" href="{map_link}" target="_blank" rel="noopener noreferrer">Ver no Google Maps</a></div><div class="contact-map-frame"><iframe src="{map_embed}" title="Localização do Polo de Inovação do IFAM no Google Maps" width="100%" height="380" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div><div class="contact-map-footer"><span>Av. Gov. Danilo de Matos Areosa, 1672 · Distrito Industrial I, Manaus - AM</span><a href="{map_link}" target="_blank" rel="noopener noreferrer">Como chegar</a></div></section><div class="home-band" aria-hidden="true"></div><section class="closing">{side_patterns}<div class="closing-inner"><div><h2>Conheça de perto a formação.</h2><p>Explore os módulos e projetos que estão transformando ideias em soluções inteligentes.</p></div><a class="button" href="curso.html">Conheça o curso</a></div></section><div class="home-band" aria-hidden="true"></div></div>'''
page('contato.html','Contato','Entre em contato com a AX Academy.',contact)
