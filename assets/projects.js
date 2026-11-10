// Configuração detalhada dos projetos da AX Academy inspirada no modelo escuro com pré-visualização, chips e tags.
window.AX_PROJECTS = [
  {
    num: '01',
    name: 'Hanaro',
    image: 'assets/hanaro-placeholder.png',
    category: 'Automação Industrial',
    codeLang: 'Python',
    description: 'Automação da análise de casos de desperdício que acontecem no processo produtivo.',
    meshTheme: 'mesh-blue',
    mockupType: 'chips_progress',
    mockupTitle: 'HANARO · MONITORAMENTO INDUSTRIAL',
    chips: [
      { text: 'Linha SMD', solid: true },
      { text: 'Desperdício 0%', solid: true },
      { text: 'Otimização contínua', solid: false },
      { text: 'Visão computacional', solid: false }
    ],
    progress: { label: 'TAXA DE REDUÇÃO DE PERDAS', valText: '-24.8%', percent: 82 },
    footer: '→ FLUXO PRODUTIVO OTIMIZADO',
    tags: ['Python', 'BotCity', 'Computer Vision', 'Pandas', 'Docker', 'RPA']
  },
  {
    num: '02',
    name: 'Synergia',
    image: 'assets/synergia-logo.png',
    category: 'Supply Chain',
    codeLang: 'Python · SQL',
    description: 'Consolidação de dados e acompanhamento de pendências de suprimentos.',
    meshTheme: 'mesh-green',
    mockupType: 'stats',
    mockupTitle: 'SYNERGIA · GESTÃO DE SUPRIMENTOS',
    stats: [
      { label: 'ENTREGAS', color: 'filled-emerald', count: 8, total: 10, val: '84%' },
      { label: 'ESTOQUE', color: 'filled-cyan', count: 10, total: 10, val: '100% OK' },
      { label: 'PENDÊNCIAS', color: 'filled-violet', count: 2, total: 10, val: 'BAIXO' }
    ],
    footer: '▲ ERP SAP SINCRONIZADO',
    tags: ['Python', 'FastAPI', 'ETL', 'PostgreSQL', 'Dashboards', 'SAP']
  },
  {
    num: '03',
    name: 'Vigil',
    image: 'assets/vigil-logo.png',
    category: 'Machine Learning',
    codeLang: 'Machine Learning',
    description: 'Identificação de parâmetros para classificação de padrões comportamentais.',
    meshTheme: 'mesh-purple',
    mockupType: 'chips_stat',
    mockupTitle: 'VIGIL · PADRÕES COMPORTAMENTAIS',
    chips: [
      { text: 'Cluster #04', solid: true },
      { text: 'Desvio < 0.05', solid: true },
      { text: 'Padrão regular', solid: false },
      { text: 'Detecção anomalia', solid: false }
    ],
    stats: [
      { label: 'CONFIANÇA', color: 'filled-pink', count: 9, total: 10, val: '98.4%' }
    ],
    footer: '● INFERÊNCIA EM TEMPO REAL',
    tags: ['Python', 'TensorFlow', 'Scikit-learn', 'Clusterização', 'Análise Preditiva']
  },
  {
    num: '04',
    name: 'Arumã',
    image: 'assets/aruma-logo.png',
    category: 'Comex & Fiscal',
    codeLang: 'Hiperautomação',
    description: 'Automação de processos voltados à área fiscal de comércio exterior.',
    meshTheme: 'mesh-amber',
    mockupType: 'stats',
    mockupTitle: 'ARUMÃ · FISCAL & COMÉRCIO EXTERIOR',
    stats: [
      { label: 'DU-E / DI', color: 'filled-amber', count: 9, total: 10, val: '92%' },
      { label: 'RECEITA', color: 'filled-emerald', count: 10, total: 10, val: 'VALIDADO' },
      { label: 'AUDITORIA', color: 'filled-cyan', count: 10, total: 10, val: 'APROVADO' }
    ],
    footer: '✓ DESEMBARAÇO AUTOMATIZADO',
    tags: ['Python', 'Playwright', 'FastAPI', 'OCR', 'Docker', 'Comex']
  }
];
