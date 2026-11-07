from pathlib import Path

out = Path(__file__).parent / 'dist'
arrow = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15M13 5l7 7-7 7"/></svg>'
links = [('index.html','Início'),('curso.html','Curso'),('portfolio.html','Portfólio'),('contato.html','Contato')]

def header(active):
    nav = ''.join(f'<a href="{href}"' + (' aria-current="page"' if href == active else '') + f'>{label}</a>' for href,label in links)
    return f'''<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header"><div class="wrap nav-shell">
  <a class="brand" href="index.html" aria-label="AX Academy — início"><img class="brand-light" src="assets/ax-logo.png" alt="AX Academy"><img class="brand-dark" src="assets/ax-logo-white.png" alt="AX Academy"></a>
  <nav class="nav-links" id="primary-nav" aria-label="Navegação principal">{nav}</nav>
  <div class="nav-actions"><button class="theme-toggle" data-theme-toggle aria-label="Alternar tema"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M4.93 4.93l1.41 1.41m11.32 11.32 1.41 1.41M19.07 4.93l-1.41 1.41M6.34 17.66l-1.41 1.41"/></svg></button><button class="menu-toggle" data-menu aria-expanded="false" aria-controls="primary-nav" aria-label="Abrir menu"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 8h16M4 16h16"/></svg></button></div>
</div></header>'''

def footer():
    nav = ''.join(f'<a href="{href}">{label}</a>' for href,label in links)
    return f'''<footer class="footer"><div class="wrap"><div class="footer-main"><div><a class="brand" href="index.html"><img class="brand-light" src="assets/ax-logo.png" alt="AX Academy"><img class="brand-dark" src="assets/ax-logo-white.png" alt="AX Academy"></a><p>Conhecimento em automação para transformar ideias em soluções.</p></div><nav class="footer-nav" aria-label="Navegação do rodapé">{nav}</nav></div><div class="footer-bottom"><span>AX Academy · Formação em automação</span><div><img class="footer-lg footer-lg-light" src="assets/lg.svg" alt="LG"><img class="footer-lg footer-lg-dark" src="assets/lg-light.svg" alt="LG"></div></div></div></footer>'''

def page(filename, title, description, body, extra=''):
    theme = "try{var t=localStorage.getItem('ax-academy-theme');document.documentElement.dataset.theme=t==='dark'||t==='light'?t:(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light')}catch(e){document.documentElement.dataset.theme='light'}"
    body_class = ' class="home-page"' if filename == 'index.html' else ''
    html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{description}"><title>{title} | AX Academy</title><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><script>{theme}</script><link rel="stylesheet" href="assets/styles.css"><link rel="stylesheet" href="assets/lg-patterns.css"></head><body{body_class}>{header(filename)}<main id="conteudo">{body}</main>{footer()}{extra}<script src="assets/app.js" defer></script></body></html>'''
    (out / filename).write_text(html, encoding='utf-8')

modules = [
    ('RPA com Python', '160 horas', 'Automatize tarefas, conecte sistemas e construa robôs com Python.', ['Python','BotCity','Spiders','Playwright','PyAutoGUI','Bibliotecas de automação','Telegram','WhatsApp','Gmail','Google Cloud'], 'APIs, tratamento de erros, testes e versionamento.'),
    ('Data Science e Machine Learning', '160 horas', 'Explore dados, desenvolva modelos e acompanhe seu desempenho ao longo do tempo.', ['Data Science','Data Mining','CRISP-DM','EDA','Limpeza de dados','Pré-processamento','Regressão linear','Regressão logística','Classificação','Naive Bayes','Árvores de decisão','Regularização','Detecção de anomalias','K-means','Clusterização','Redes neurais','TensorFlow','Keras','Transformers','NLP','Tokenização','Vetorização','Análise de sentimentos','Data drift','MLflow','Evidently','Agentic AI'], 'Avaliação de modelos e comunicação de resultados.'),
    ('Hiperautomação', '240 horas', 'Combine processos, ferramentas e serviços para automatizar fluxos de ponta a ponta.', ['BPMN','Docker','SmartOffice','BotCity','FastAPI','Logging'], 'Orquestração de processos, integração por APIs, filas, monitoramento e observabilidade.'),
    ('Agentes inteligentes', '80 horas', 'Conheça ferramentas para criar fluxos e sistemas com agentes inteligentes.', ['n8n','CrewAI','LangGraph','LangChain'], 'Avaliação de agentes e integração com ferramentas externas.')
]

rows = ''.join(f'<a class="module-row" href="curso.html#{i}"><span class="index">0{i}</span><div><h3>{name}</h3><p>{description}</p></div><span class="module-meta">{duration}</span><span class="module-arrow" aria-hidden="true">↗</span></a>' for i,(name,duration,description,topics,suggestion) in enumerate(modules,1))
home = f'''<section class="hero"><div class="hero-art" aria-hidden="true"><canvas data-pixel-art></canvas></div><div class="hero-copy"><h1>Ideias em movimento.<br><em>Futuro em construção.</em></h1><p class="lead">Na AX Academy, tecnologia e aprendizado se encontram para transformar desafios em soluções inteligentes.</p><div class="hero-actions"><a class="button" href="curso.html">Conheça o curso</a><a class="button button-outline" href="portfolio.html">Explore os projetos</a></div></div></section>
<div class="home-content"><div class="home-band pattern-left" aria-hidden="true"></div><div class="ribbon"><div class="ribbon-inner"><strong>Da automação à inteligência artificial.</strong><div class="ribbon-list"><span>Python & RPA</span><span>Ciência de dados</span><span>Hiperautomação</span><span>Agentes inteligentes</span></div></div></div>
<section class="section home-modules"><div class="section-head"><h2>Quatro módulos.<br>Um mundo de possibilidades.</h2><p>Uma jornada que conecta ferramentas, dados e processos para criar soluções com propósito.</p></div><div class="module-list">{rows}</div><p class="module-cta"><a class="text-link" href="curso.html">Conheça a formação completa {arrow}</a></p></section>
<div class="home-band pattern-right" aria-hidden="true"></div><section class="closing"><div class="closing-inner"><div><h2>Conheça o que estamos construindo.</h2><p>Explore projetos que aplicam automação e inteligência a desafios reais.</p></div><a class="button" href="portfolio.html">Ver portfólio</a></div></section><div class="home-band pattern-left" aria-hidden="true"></div></div>'''
page('index.html','Início','Conheça a AX Academy e sua formação em automação.',home)

course_sections = ''.join(f'''<section class="course-module" id="{i}"><div><span class="tag">Módulo 0{i}</span><h2>{name}</h2><span class="module-meta">{duration}</span></div><div class="course-detail"><p>{description}</p><div class="chips">{''.join(f'<span class="chip">{topic}</span>' for topic in topics)}</div><div class="suggestion"><strong>Conteúdos complementares sugeridos:</strong> {suggestion}</div></div></section>''' for i,(name,duration,description,topics,suggestion) in enumerate(modules,1))
course = f'''<section class="wrap page-heading"><span class="tag">A jornada AX</span><h1>Aprender para automatizar. Criar para transformar.</h1><p class="lead">Uma formação que percorre automação, ciência de dados e inteligência artificial, com ferramentas aplicadas a diferentes desafios.</p></section><div class="wrap course-summary"><div class="summary-item"><strong>04</strong><span>módulos</span></div><div class="summary-item"><strong>640 horas</strong><span>de conteúdo</span></div></div><div class="wrap">{course_sections}</div><section class="section wrap"><div class="section-head"><h2>Conhecimento que ganha forma.</h2><p>Veja como a tecnologia se conecta a diferentes contextos no portfólio da AX Academy.</p></div><a class="button" href="portfolio.html">Explorar projetos</a></section>'''
page('curso.html','Curso','Conheça os módulos e conteúdos da formação em automação da AX Academy.',course)

portfolio = '''<section class="wrap page-heading"><span class="tag">Portfólio</span><h1>Ideias que se tornam soluções.</h1><p class="lead">Conheça projetos que exploram automação e dados em diferentes contextos.</p></section><section class="section wrap"><div class="portfolio-grid" data-projects></div><p class="project-note">As imagens dos projetos são provisórias e serão atualizadas.</p><noscript><p>Hanaro: automação da análise de desperdícios no processo produtivo. Synergia: consolidação de dados e pendências de suprimentos. Vigil: classificação de padrões comportamentais. Arumã: automação fiscal de comércio exterior.</p></noscript></section>'''
page('portfolio.html','Portfólio','Conheça os projetos Hanaro, Synergia, Vigil e Arumã.',portfolio,'<script src="assets/projects.js" defer></script>')

contact = '''<section class="wrap page-heading"><span class="tag">Contato</span><h1>Vamos conversar?</h1><p class="lead">Entre em contato para saber mais sobre a AX Academy e sua formação em automação.</p></section><section class="section wrap"><div class="contact-layout"><article class="contact-card"><h2>E-mail</h2><span class="contact-value">contato@exemplo.com</span><p>Canal de contato da AX Academy.</p><span class="notice">E-mail de exemplo · será atualizado</span></article><article class="contact-card"><h2>Onde estamos</h2><span class="contact-value">Polo de Inovação do IFAM</span><p>Campus Distrito Industrial (CMDI)</p></article></div></section>'''
page('contato.html','Contato','Entre em contato com a AX Academy.',contact)
