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
        <li><h3>Conecte com a prática</h3><p>Conheça aplicações na indústria e em suprimentos.</p></li>
      </ol>
    </section>'''
    technologies = technology_strip(
        ['Python', 'Google Cloud', 'Docker', 'FastAPI',
        'TensorFlow', 'MLflow', 'n8n', 'CrewAI', 'LangGraph', 'LangChain'],
        'Tecnologias da formação AX Academy', 'home-technologies-title')
    marker = '<section class="section home-modules">'
    if marker not in body:
        raise ValueError('The home modules section was not found.')
    return body.replace(marker, story + technologies + marker, 1)


def render_course_modules(modules):
    sections = []
    for index, (name, hours, description, topics) in enumerate(modules, 1):
        badges = ''.join(f'<span class="chip">{escape(topic)}</span>' for topic in topics)
        sections.append(f"""<section class="course-module" id="{index}">
          <div><span class="tag">Módulo 0{index}</span><h2>{escape(name)}</h2><span class="module-meta">{escape(hours)}</span></div>
          <div class="course-detail"><p>{escape(description)}</p><div class="chips">{badges}</div></div>
        </section>""")
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
    patterns = ('<div class="closing-side closing-side-left" data-lg-pattern aria-hidden="true"></div>'
                '<div class="closing-side closing-side-right" data-lg-pattern aria-hidden="true"></div>')
    heading_start = body.index('<section class="page-heading')
    heading_end = body.index('</section>', heading_start)
    heading = body[heading_start:heading_end]
    if patterns not in heading:
        raise ValueError('The course heading patterns were not found.')
    body = body[:heading_start] + heading.replace(patterns, '', 1) + body[heading_end:]
    summary = '<div class="course-summary">'
    if summary not in body:
        raise ValueError('The course summary was not found.')
    body = body.replace(summary, '<div class="course-summary course-summary-with-pattern">' + patterns, 1)
    return body
