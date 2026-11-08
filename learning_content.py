"""Content and local technology marks shared by the home and course pages."""

from html import escape


MARKS = {
    'Python': 'python', 'FastAPI': 'fastapi', 'Docker': 'docker',
    'Google Cloud': 'googlecloud', 'TensorFlow': 'tensorflow', 'Keras': 'keras',
    'MLflow': 'mlflow', 'n8n': 'n8n', 'CrewAI': 'crewai',
    'LangChain': 'langchain', 'LangGraph': 'langgraph',
}

def technology_item(name):
    mark = MARKS.get(name)
    icon = (f'<span class="tech-logo" aria-hidden="true" '
            f'style="--tech-mark:url(\'technology/{mark}.svg\')"></span>') if mark else ''
    return f'<li>{icon}<span>{escape(name)}</span></li>'


def technology_strip(names, title, identifier):
    items = ''.join(technology_item(name) for name in names)
    return f'''<section class="tech-strip" data-tech-strip aria-label="{escape(title)}">
      <div class="tech-marquee"><div class="tech-marquee-track">
        <ul class="tech-marquee-group">{items}</ul>
        <ul class="tech-marquee-group" aria-hidden="true">{items}</ul>
      </div></div>
    </section>'''


def enrich_home(body):
    story = '''<section class="learning-story" aria-labelledby="learning-story-title">
      <div class="learning-story-intro">
        <h2 id="learning-story-title">Uma tarefa repetitiva.<br>Um novo jeito de resolver.</h2>
        <p>A AX Academy conecta automação, dados e inteligência artificial. A jornada começa nas tarefas do dia a dia e avança até a construção de fluxos que integram ferramentas, sistemas e agentes.</p>
      </div>
      <ol class="learning-journey">
        <li><h3>Entenda o desafio</h3><p>Observe o processo, reconheça etapas repetitivas e descubra onde a automação pode ajudar.</p></li>
        <li><h3>Dê forma à solução</h3><p>Crie robôs com Python, explore dados e combine serviços para transformar uma ideia em um fluxo.</p></li>
        <li><h3>Conecte com a prática</h3><p>Conheça aplicações na indústria, em suprimentos, em padrões comportamentais e na área fiscal.</p></li>
      </ol>
      <a class="learning-story-link" href="portfolio.html">Conheça Hanaro, Synergia, Vigil e Arumã</a>
    </section>'''
    technologies = technology_strip(
        ['Python', 'BotCity', 'Playwright', 'Google Cloud', 'Docker', 'FastAPI',
        'TensorFlow', 'MLflow', 'n8n', 'CrewAI', 'LangGraph', 'LangChain'],
        'Tecnologias da formação AX Academy', 'home-technologies-title')
    marker = '<section class="section home-modules">'
    if marker not in body:
        raise ValueError('The home modules section was not found.')
    return body.replace(marker, story + technologies + marker, 1)


MODULE_PRESENTATIONS = [
    {
        'tools': ['Python', 'BotCity', 'Playwright', 'PyAutoGUI', 'Google Cloud'],
        'intro': 'Da tarefa manual ao primeiro robô. Aprenda a automatizar ações no navegador e no desktop, conectando a execução a serviços que já fazem parte do trabalho.',
        'groups': [
            ('Automatizar tarefas', 'Bibliotecas Python, robôs, coleta de informações e interação com interfaces web e desktop.'),
            ('Conectar serviços', 'Integrações com Telegram, WhatsApp, Gmail e Google Cloud.'),
        ],
    },
    {
        'tools': ['Python', 'TensorFlow', 'Keras', 'MLflow'],
        'intro': 'Dos dados às decisões. Prepare informações, investigue padrões e construa modelos, acompanhando seu desempenho e as mudanças nos dados ao longo do tempo.',
        'groups': [
            ('Investigar e preparar', 'CRISP-DM, análise exploratória, limpeza de dados e pré-processamento.'),
            ('Modelar e acompanhar', 'Classificação, regressão, clusterização, NLP, redes neurais e monitoramento de modelos.'),
        ],
    },
    {
        'tools': ['Docker', 'FastAPI', 'BotCity', 'SmartOffice'],
        'intro': 'Do robô ao processo completo. Combine automações, serviços e regras de negócio para conectar etapas e acompanhar o que acontece em cada execução.',
        'groups': [
            ('Desenhar o processo', 'BPMN e integração de ferramentas para estruturar fluxos de ponta a ponta.'),
            ('Colocar em operação', 'Docker, APIs com FastAPI, SmartOffice, BotCity e logging.'),
        ],
    },
    {
        'tools': ['n8n', 'CrewAI', 'LangGraph', 'LangChain'],
        'intro': 'Dos fluxos aos agentes. Explore como conectar modelos, ferramentas e etapas de trabalho para construir sistemas com agentes inteligentes.',
        'groups': [
            ('Orquestrar fluxos', 'Conexões e automações com n8n, combinando serviços em uma mesma jornada.'),
            ('Construir com agentes', 'CrewAI, LangGraph e LangChain para organizar ferramentas e etapas de execução.'),
        ],
    },
]


def render_course_modules(modules):
    sections = []
    for index, ((name, hours, description, topics, suggestion), presentation) in enumerate(zip(modules, MODULE_PRESENTATIONS), 1):
        groups = ''.join(f'<div><h3>{escape(title)}</h3><p>{escape(text)}</p></div>' for title, text in presentation['groups'])
        topic_list = ''.join(f'<li>{escape(topic)}</li>' for topic in topics)
        tools = technology_strip(presentation['tools'], f'Tecnologias do módulo {index}', f'module-{index}-technologies')
        sections.append(f'''<section class="course-module learning-module" id="{index}" aria-labelledby="module-{index}-title">
          <div class="learning-module-heading"><span class="tag">Módulo 0{index}</span><h2 id="module-{index}-title">{escape(name)}</h2><span class="module-meta">{escape(hours)}</span></div>
          <div class="course-detail"><p class="learning-module-intro">{escape(presentation['intro'])}</p><div class="learning-outcomes">{groups}</div></div>
          {tools}
          <details class="learning-syllabus"><summary>Explorar todos os conteúdos <span>{len(topics)} tópicos</span></summary><ul>{topic_list}</ul></details>
          <p class="learning-suggestion"><strong>Conteúdos complementares sugeridos</strong>{escape(suggestion)}</p>
        </section>''')
    return ''.join(sections)


def enrich_course(body):
    # Use the existing central frame and keep all original course content.
    if 'class="home-content"' not in body:
        start = body.index('<div class="course-heading-frame">')
        body = body[start:]
        body = body.replace('<div class="course-heading-frame">', '<div class="home-content learning-course"><div class="course-heading-frame">', 1)
        body = body.replace('class="wrap course-summary"', 'class="course-summary"', 1)
        body = body.replace('<div class="wrap"><section class="course-module', '<div class="course-modules"><section class="course-module', 1)
        body += '</div>'
    else:
        body = body.replace('class="home-content"', 'class="home-content learning-course"', 1)
    return body
