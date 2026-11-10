const projectDetails = {
  Hanaro: {
    context: 'Antes do Hanaro, a equipe extraía dados manualmente e cruzava planilhas para acompanhar perdas da Linha Final. Esse trabalho recorrente dificultava a análise de todas as linhas e gerava divergências nos indicadores.',
    solution: 'O sistema centraliza os registros de scrap e o acompanhamento do IF Cost. Um painel compara o realizado com as metas, enquanto o assistente de IA sugere ações de contenção, correção e prevenção para avaliação do analista.',
    team: [['André Filipe Aloise', 'P.O. · Scrum Master'], ['Messyas Gois França', 'Full Stack Developer + AI'], ['Gustavo Almada', 'Full Stack Developer'], ['Teodório Neto', 'Front-end Developer']], image: 'hanaro'
  },
  Synergia: {
    context: 'Os dados de Suprimentos estavam distribuídos em relatórios de diferentes sistemas e planilhas, exigindo consolidação manual para acompanhar a operação.',
    solution: 'O Synergia importa, valida e consolida dados operacionais, conectando informações de Workorders, lotes e seriais à sua origem. Painéis e registros de execução ajudam a equipe a acompanhar os indicadores e investigar ocorrências.',
    team: [['Gabriel Fernandes', 'P.O. · Fullstack'], ['Rebecca Xavier', 'Frontend e UX/UI'], ['Marcelo Uchôa', 'DevOps e QA'], ['Carlos Eduardo', 'RPA e Integrações'], ['Gustavo Nunes', 'Backend']], image: 'synergia'
  },
  Vigil: {
    context: 'O acompanhamento de jornadas, horas extras e absenteísmo dependia do cruzamento manual de dados em planilhas. Os desvios muitas vezes eram identificados apenas depois de acontecer.',
    solution: 'O Vigil importa e valida dados de jornada, acompanha limites e envia alertas preventivos aos gestores. Também registra justificativas e oferece relatórios para apoiar a auditoria da operação.',
    team: [['Ítalo Henrique', 'P.O. · Fullstack e DevOps'], ['Ana Carolina', 'Backend'], ['Fabrício Coelho', 'QA'], ['Luiz Gustavo', 'Front-end'], ['Raquel Andrade', 'Designer']], image: 'vigil'
  },
  'Arumã': {
    context: 'A rotina fiscal recebe diariamente documentos de importação que precisam ser registrados, conferidos e acompanhados. As tarefas repetitivas e as informações dispersas tornam mais difícil identificar e tratar ocorrências.',
    solution: 'O Arumã organiza lotes e documentos em um fluxo de acompanhamento, dando visibilidade ao que foi recebido e ao que precisa de análise. Um assistente de IA apoia consultas às informações em linguagem natural.',
    team: [['José Santarém', 'P.O. · DevOps'], ['Mariane Oliveira', 'Analista de Qualidade'], ['Mouriem Pacheco', 'Front-end'], ['Victor Breno', 'Back-end'], ['Victor Lima', 'Fullstack · Dev RPA']], image: 'aruma'
  }
};

const projectGrid = document.querySelector('[data-projects]');
if (projectGrid) {
  const dialog = document.createElement('dialog');
  dialog.className = 'project-dialog';
  dialog.setAttribute('aria-labelledby', 'project-dialog-title');
  dialog.innerHTML = `<div class="project-dialog-inner"><button class="project-dialog-close" type="button" aria-label="Fechar detalhes do projeto"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19"/></svg></button><div class="project-dialog-heading"><div class="header-pattern project-dialog-pattern" data-lg-pattern="g" aria-hidden="true"></div><span>Projeto AX Academy</span><h2 id="project-dialog-title"></h2></div><div class="project-dialog-body"><section><h3>O desafio</h3><p data-context></p></section><section><h3>A solução</h3><p data-solution></p></section><section class="project-team"><h3>Equipe do projeto</h3><div class="project-team-list"></div></section></div></div>`;
  document.body.append(dialog);
  const dialogPattern = dialog.querySelector('.project-dialog-pattern');
  const resizeDialogPattern = new ResizeObserver(() => {
    const { width, height } = dialogPattern.getBoundingClientRect();
    if (width < 1 || height < 1) return;
    const rows = Math.max(2, Math.round(height / 36));
    const motifSize = height / rows;
    let columns = Math.max(2, Math.ceil(width / motifSize));
    if (columns % 2 !== 0) columns += 1;
    dialogPattern.style.setProperty('--pattern-columns', columns);
    dialogPattern.style.setProperty('--pattern-rows', rows);
    dialogPattern.style.setProperty('--motif-size', `${motifSize}px`);
    if (dialogPattern.dataset.patternGrid === `${columns}:${rows}`) return;
    dialogPattern.dataset.patternGrid = `${columns}:${rows}`;
    const marks = document.createDocumentFragment();
    for (let row = 0; row < rows; row++) for (let column = 0; column < columns; column++) {
      const mark = document.createElement('i');
      mark.className = 'lg-g-pattern-mark';
      mark.style.setProperty('--turn', `${[[90, 0], [270, 180]][row % 2][column % 2]}deg`);
      mark.style.setProperty('--flip', column % 2 === 0 ? '-1' : '1');
      marks.append(mark);
    }
    dialogPattern.replaceChildren(marks);
  });
  resizeDialogPattern.observe(dialogPattern);
  let opener;
  const close = dialog.querySelector('.project-dialog-close');
  close.addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener('close', () => { document.body.classList.remove('project-dialog-open'); opener?.focus(); });
  projectGrid.querySelectorAll('.project').forEach(card => {
    const name = card.querySelector('.project-title').textContent.trim();
    const details = projectDetails[name];
    if (!details) return;
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'project-open';
    button.setAttribute('aria-label', `Ver mais sobre o projeto ${name}`);
    button.textContent = 'Ver mais';
    card.querySelector('.project-content').append(button);
    button.addEventListener('click', () => {
      opener = button;
      dialog.querySelector('#project-dialog-title').textContent = name;
      dialog.querySelector('[data-context]').textContent = details.context;
      dialog.querySelector('[data-solution]').textContent = details.solution;
      const list = dialog.querySelector('.project-team-list');
      list.replaceChildren(...details.team.map(([person, role], index) => {
        const member = document.createElement('div');
        member.className = 'project-member';
        const photo = document.createElement('img');
        photo.src = `assets/team/${details.image}-${index + 1}.jpg${details.image === 'synergia' && index === 3 ? '?v=3' : ''}`;
        photo.alt = '';
        const info = document.createElement('div');
        const memberName = document.createElement('strong');
        memberName.textContent = person;
        const memberRole = document.createElement('span');
        memberRole.textContent = role;
        info.append(memberName, memberRole);
        member.append(photo, info);
        return member;
      }));
      document.body.classList.add('project-dialog-open');
      dialog.showModal();
      close.focus();
    });
  });
}
