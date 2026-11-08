(() => {
  const root = document.documentElement;
  const key = 'ax-academy-theme';
  const button = document.querySelector('[data-theme-toggle]');
  const updateLabel = () => { if (button) button.setAttribute('aria-label', root.dataset.theme === 'dark' ? 'Ativar tema claro' : 'Ativar tema escuro'); };
  updateLabel();
  button?.addEventListener('click', () => {
    const theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = theme;
    try { localStorage.setItem(key, theme); } catch {}
    updateLabel();
  });
  const menu = document.querySelector('[data-menu]');
  const nav = document.querySelector('#primary-nav');
  menu?.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('open', open);
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menu?.getAttribute('aria-expanded') === 'true') {
      menu.setAttribute('aria-expanded', 'false'); nav.classList.remove('open'); menu.focus();
    }
  });

  const fitPattern = element => {
    const { width, height } = element.getBoundingClientRect();
    if (width < 1 || height < 1) return;
    if (element.dataset.lgPattern === 'g') {
      const rows = Math.max(3, Math.round(height / 27));
      const size = height / rows;
      let columns = Math.max(2, Math.ceil(width / size));
      if (columns % 2 !== 0) columns += 1;
      element.style.setProperty('--pattern-columns', columns);
      element.style.setProperty('--pattern-rows', rows);
      element.style.setProperty('--motif-size', `${size}px`);
      if (element.dataset.patternGrid === `${columns}:${rows}`) return;
      element.dataset.patternGrid = `${columns}:${rows}`;
      const marks = document.createDocumentFragment();
      for (let row = 0; row < rows; row++) for (let column = 0; column < columns; column++) {
        const mark = document.createElement('i');
        mark.className = 'lg-g-pattern-mark';
        mark.style.setProperty('--turn', `${[[90, 0], [270, 180]][row % 2][column % 2]}deg`);
        mark.style.setProperty('--flip', column % 2 === 0 ? '-1' : '1');
        marks.append(mark);
      }
      element.replaceChildren(marks);
      return;
    }
    const columns = Math.max(1, Math.round(width / 40));
    const rows = Math.max(1, Math.round(height / 40));
    element.style.setProperty('--pattern-columns', columns);
    element.style.setProperty('--pattern-rows', rows);
    element.style.setProperty('--motif-size', `${Math.min(width / columns, height / rows)}px`);
    if (element.dataset.patternGrid === `${columns}:${rows}`) return;
    element.dataset.patternGrid = `${columns}:${rows}`;
    const marks = document.createDocumentFragment();
    for (let row = 0; row < rows; row++) for (let column = 0; column < columns; column++) {
      const mark = document.createElement('i');
      mark.className = 'lg-pattern-mark';
      mark.style.setProperty('--turn', `${[[0, 90], [270, 180]][row % 2][column % 2]}deg`);
      const g = document.createElement('span'); g.className = 'lg-pattern-g';
      mark.append(g); marks.append(mark);
    }
    element.replaceChildren(marks);
  };
  const patternObserver = new ResizeObserver(entries => entries.forEach(entry => fitPattern(entry.target)));
  document.querySelectorAll('[data-lg-pattern]').forEach(element => patternObserver.observe(element));

  const projectContainer = document.querySelector('[data-projects]');
  if (projectContainer && window.AX_PROJECTS && projectContainer.children.length === 0) {
    window.AX_PROJECTS.forEach(project => {
      const article = document.createElement('article');
      article.className = `project ${project.meshTheme || 'mesh-blue'}`;

      const preview = document.createElement('div');
      preview.className = 'project-preview';

      const codeBadge = document.createElement('div');
      codeBadge.className = 'project-code-badge';
      codeBadge.innerHTML = `<span class="code-bracket">&lt;&gt;</span> ${project.codeLang || 'Python'}`;
      preview.appendChild(codeBadge);

      const mockup = document.createElement('div');
      mockup.className = 'project-mockup';

      const header = document.createElement('div');
      header.className = 'mockup-header';
      header.textContent = project.mockupTitle || project.name;
      mockup.appendChild(header);

      if (project.chips && project.chips.length) {
        const chipsWrap = document.createElement('div');
        chipsWrap.className = 'mockup-chips';
        project.chips.forEach(c => {
          const chip = document.createElement('span');
          chip.className = `mockup-chip ${c.solid ? 'solid' : 'outline'}`;
          chip.textContent = c.text;
          chipsWrap.appendChild(chip);
        });
        mockup.appendChild(chipsWrap);
      }

      if (project.stats && project.stats.length) {
        project.stats.forEach(s => {
          const row = document.createElement('div');
          row.className = 'mockup-stat-row';
          const label = document.createElement('span');
          label.className = 'mockup-stat-label';
          label.textContent = s.label;
          const segments = document.createElement('div');
          segments.className = 'mockup-stat-segments';
          for (let i = 0; i < (s.total || 10); i++) {
            const seg = document.createElement('span');
            seg.className = `mockup-stat-segment ${i < s.count ? s.color : ''}`;
            segments.appendChild(seg);
          }
          const val = document.createElement('span');
          val.className = 'mockup-stat-val';
          val.textContent = s.val;
          row.append(label, segments, val);
          mockup.appendChild(row);
        });
      }

      if (project.progress) {
        const prog = document.createElement('div');
        prog.className = 'mockup-progress';
        prog.innerHTML = `
          <div class="mockup-progress-label">
            <span>${project.progress.label}</span>
            <span>${project.progress.valText}</span>
          </div>
          <div class="mockup-progress-track">
            <div class="mockup-progress-bar" style="width: ${project.progress.percent}%;"></div>
          </div>
        `;
        mockup.appendChild(prog);
      }

      if (project.footer) {
        const foot = document.createElement('div');
        foot.className = 'mockup-footer';
        foot.textContent = project.footer;
        mockup.appendChild(foot);
      }

      preview.appendChild(mockup);

      const content = document.createElement('div');
      content.className = 'project-content';

      const titleRow = document.createElement('div');
      titleRow.className = 'project-title-row';

      const title = document.createElement('h2');
      title.className = 'project-title';
      title.textContent = project.name;

      const badge = document.createElement('span');
      badge.className = 'project-badge';
      badge.innerHTML = `<span class="project-badge-num">${project.num || ''}</span> ${project.category || ''}`;

      titleRow.append(title, badge);

      const desc = document.createElement('p');
      desc.className = 'project-desc';
      desc.textContent = project.description;

      const tagsWrap = document.createElement('div');
      tagsWrap.className = 'project-tags';
      (project.tags || []).forEach(t => {
        const tag = document.createElement('span');
        tag.className = 'project-tag';
        tag.textContent = t;
        tagsWrap.appendChild(tag);
      });

      content.append(titleRow, desc, tagsWrap);
      article.append(preview, content);
      projectContainer.appendChild(article);
    });
  }

  const canvas = document.querySelector('[data-pixel-art]');
  if (!canvas) return;
  const host = canvas.parentElement, ctx = canvas.getContext('2d');
  if (!ctx) return;
  const scene = document.querySelector('[data-intro-scene]');
  const copy = document.querySelector('.hero-copy');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const cols = 68, rows = 48, mask = new Uint8Array(cols * rows);
  const ifam = new Uint8Array(cols * rows), lg = new Uint8Array(cols * rows);
  let width = 0, height = 0, cell = 0, ox = 0, oy = 0, start = 0, frame = 0, pointer = null;
  let progress = 0, imageReady = false, sceneVisible = true, scrollFrame = 0;
  const rand = (x, y) => { const n = Math.sin(x * 127.1 + y * 311.7) * 43758.5453; return n - Math.floor(n); };
  const clamp = n => Math.max(0, Math.min(1, n));
  const mix = (a, b, t) => a + (b - a) * t;
  const smooth = (a, b, n) => { const t = clamp((n - a) / (b - a)); return t * t * (3 - 2 * t); };
  const updateProgress = () => {
    scrollFrame = 0;
    if (!scene || reduced.matches || !imageReady) progress = 0;
    else {
      const bounds = scene.getBoundingClientRect();
      progress = clamp(-bounds.top / Math.max(1, bounds.height - window.innerHeight));
    }
    const fade = smooth(.10, .25, progress);
    if (copy) {
      copy.style.setProperty('--intro-copy-opacity', String(1 - fade));
      copy.style.setProperty('--intro-copy-offset', `${-18 * fade}px`);
      copy.inert = fade > .98;
      if (fade > .98) copy.setAttribute('aria-hidden', 'true');
      else copy.removeAttribute('aria-hidden');
    }
    host.style.setProperty('--intro-overlay-opacity', String(1 - smooth(.10, .30, progress)));
  };
  const queueProgress = () => { if (!scrollFrame) scrollFrame = requestAnimationFrame(updateProgress); };
  const resize = () => {
    const rect = host.getBoundingClientRect(); width = rect.width; height = rect.height;
    const dpr = Math.min(devicePixelRatio || 1, 2); canvas.width = Math.round(width * dpr); canvas.height = Math.round(height * dpr); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const mobile = width <= 720;
    cell = Math.max(width / (mobile ? 58 : 84), height / 34);
    ox = width * (mobile ? .30 : .27) - (cols * cell) / 2;
    oy = (height - rows * cell) / 2;
    if (reduced.matches) draw(100);
  };
  const draw = t => {
    ctx.clearRect(0, 0, width, height);
    const dark = root.dataset.theme === 'dark';
    ctx.fillStyle = dark ? '#ffffff' : '#1a1a1a';
    const center = smooth(.10, .29, progress);
    const centeredCell = Math.min(width / (width <= 720 ? 55 : 70), height / 50);
    const drawCell = mix(cell, centeredCell, center);
    const drawX = mix(ox, (width - cols * centeredCell) / 2, center);
    const rise = height * .11 * smooth(0, .2, progress) * (1 - center);
    const drawY = mix(oy - rise, (height - rows * centeredCell) / 2, center);
    const firstColumn = Math.floor(-drawX / drawCell) - 1;
    const lastColumn = Math.ceil((width - drawX) / drawCell) + 1;
    const firstRow = Math.floor(-drawY / drawCell) - 1;
    const lastRow = Math.ceil((height - drawY) / drawCell) + 1;
    for (let y = firstRow; y < lastRow; y++) for (let x = firstColumn; x < lastColumn; x++) {
      const px = drawX + x * drawCell + drawCell / 2, py = drawY + y * drawCell + drawCell / 2;
      const distance = Math.hypot(x - cols / 2, y - rows / 2);
      const local = reduced.matches ? 1 : Math.max(clamp((t - distance * .026 - rand(x,y) * .2) / .5), smooth(0, .08, progress));
      if (!local) continue;
      const ease = 1 + 2.7 * Math.pow(local - 1, 3) + 1.7 * Math.pow(local - 1, 2);
      const wave = reduced.matches ? .5 : .5 + .25 * Math.sin(t * .9 + x * .19 + y * .16) + .25 * Math.sin(t * 1.3 + rand(x,y) * 6.28);
      const hover = pointer ? Math.pow(clamp(1 - Math.hypot(px - pointer.x, py - pointer.y) / (drawCell * 8)), 2) : 0;
      const inside = x >= 0 && x < cols && y >= 0 && y < rows;
      const index = y * cols + x;
      const delay = rand(x, y) * .025 + clamp(distance / 48) * .02;
      const ifamMix = smooth(.22 + delay, .37 + delay, progress);
      const lgMix = smooth(.46 + delay, .76 + delay, progress);
      const active = inside ? mix(mix(mask[index], ifam[index], ifamMix), lg[index], lgMix) : 0;
      const edge = cols - 2 - (y / rows) * 10;
      const edgeFade = mix(clamp((edge - x) / 5), 1, center);
      const base = .018 + wave * .035;
      ctx.globalAlpha = clamp(base + active * (.10 + wave * .10 + center * .08) + hover * .08) * edgeFade * Math.min(1, local * 1.6);
      const size = drawCell * (.65 + wave * .10 + hover * .12) * ease;
      ctx.fillRect(px - size / 2, py - size / 2, size, size);
    }
    ctx.globalAlpha = 1;
  };
  const tick = now => { if (!start) start = now; draw((now - start) / 1000); frame = requestAnimationFrame(tick); };
  const startAnimation = () => {
    if (!frame && imageReady && sceneVisible && !reduced.matches && !document.hidden) frame = requestAnimationFrame(tick);
  };
  const syncMotion = () => {
    cancelAnimationFrame(frame); frame = 0;
    root.classList.toggle('has-scroll-intro', imageReady && !reduced.matches);
    updateProgress(); resize();
    if (reduced.matches) draw(100);
    else startAnimation();
  };
  const loadImage = src => new Promise(resolve => {
    const image = new Image();
    image.onload = () => resolve(image);
    image.onerror = () => resolve(null);
    image.src = src;
  });
  Promise.all([
    loadImage('assets/ax-logo.png'),
    loadImage('assets/ifam-logo.png'),
    loadImage('assets/lg-mosaic.png'),
  ]).then(([axImage, ifamImage, lgImage]) => {
    if (!axImage) return;
    const sample = document.createElement('canvas'); sample.width = cols; sample.height = rows;
    const s = sample.getContext('2d', {willReadFrequently:true});
    // A primeira parte da imagem original contém apenas o símbolo AX.
    s.drawImage(axImage, 0, 0, axImage.width * .31, axImage.height, 4, 7, 60, 34);
    const readMask = (target, lightOnly = false) => {
      const pixels = s.getImageData(0, 0, cols, rows).data;
      for (let i = 0; i < target.length; i++) {
        const offset = i * 4;
        target[i] = pixels[offset + 3] > 75 && (!lightOnly || pixels[offset] + pixels[offset + 1] + pixels[offset + 2] > 360) ? 1 : 0;
      }
      s.clearRect(0, 0, cols, rows);
    };
    readMask(mask);
    if (ifamImage) { s.drawImage(ifamImage, 14, 4, 40, 40); readMask(ifam); }
    else ifam.set(mask);
    if (lgImage) { s.drawImage(lgImage, 3, 7, 62, 34); readMask(lg, true); }
    else lg.set(ifam);
    imageReady = true;
    syncMotion();
  });
  const observer = new ResizeObserver(resize); observer.observe(host);
  window.addEventListener('scroll', updateProgress, { passive: true });
  window.addEventListener('resize', queueProgress, { passive: true });
  host.addEventListener('pointermove', e => { const rect = host.getBoundingClientRect(); pointer = {x:e.clientX - rect.left,y:e.clientY - rect.top}; });
  host.addEventListener('pointerleave', () => { pointer = null; });
  new MutationObserver(() => { if (reduced.matches) draw(100); }).observe(root, {attributes:true,attributeFilter:['data-theme']});
  reduced.addEventListener('change', syncMotion);
  if (scene && 'IntersectionObserver' in window) {
    new IntersectionObserver(entries => {
      sceneVisible = entries[0].isIntersecting;
      if (sceneVisible) startAnimation();
      else { cancelAnimationFrame(frame); frame = 0; }
    }).observe(scene);
  }
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) { cancelAnimationFrame(frame); frame = 0; }
    else startAnimation();
  });
})();
