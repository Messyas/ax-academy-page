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

  const projectContainer = document.querySelector('[data-projects]');
  if (projectContainer && window.AX_PROJECTS) {
    window.AX_PROJECTS.forEach((project, index) => {
      const article = document.createElement('article'); article.className = 'project';
      const media = document.createElement('div'); media.className = 'project-image';
      const image = document.createElement('img'); image.src = project.image; image.alt = project.imageAlt; image.loading = 'lazy'; media.append(image);
      const top = document.createElement('div'); top.className = 'project-top';
      const title = document.createElement('h2'); title.textContent = project.name;
      const number = document.createElement('span'); number.className = 'project-number'; number.textContent = String(index + 1).padStart(2, '0');
      const desc = document.createElement('p'); desc.textContent = project.description;
      top.append(title, number); article.append(media, top, desc); projectContainer.append(article);
    });
  }

  const canvas = document.querySelector('[data-pixel-art]');
  if (!canvas) return;
  const host = canvas.parentElement, ctx = canvas.getContext('2d');
  if (!ctx) return;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const cols = 68, rows = 48, mask = new Uint8Array(cols * rows);
  const image = new Image(); image.src = 'assets/ax-logo.png';
  let width = 0, height = 0, cell = 0, ox = 0, oy = 0, start = 0, frame = 0, pointer = null;
  const rand = (x, y) => { const n = Math.sin(x * 127.1 + y * 311.7) * 43758.5453; return n - Math.floor(n); };
  const clamp = n => Math.max(0, Math.min(1, n));
  const resize = () => {
    const rect = host.getBoundingClientRect(); width = rect.width; height = rect.height;
    const dpr = Math.min(devicePixelRatio || 1, 2); canvas.width = Math.round(width * dpr); canvas.height = Math.round(height * dpr); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    cell = Math.min(width / cols, height / rows); ox = (width - cols * cell) / 2; oy = (height - rows * cell) / 2;
    if (reduced.matches) draw(100);
  };
  const draw = t => {
    ctx.clearRect(0, 0, width, height);
    const dark = root.dataset.theme === 'dark';
    ctx.fillStyle = dark ? '#ffffff' : '#1a1a1a';
    for (let y = 0; y < rows; y++) for (let x = 0; x < cols; x++) {
      const px = ox + x * cell + cell / 2, py = oy + y * cell + cell / 2;
      const distance = Math.hypot(x - cols / 2, y - rows / 2);
      const local = reduced.matches ? 1 : clamp((t - distance * .026 - rand(x,y) * .2) / .5);
      if (!local) continue;
      const ease = 1 + 2.7 * Math.pow(local - 1, 3) + 1.7 * Math.pow(local - 1, 2);
      const wave = reduced.matches ? .5 : .5 + .25 * Math.sin(t * .9 + x * .19 + y * .16) + .25 * Math.sin(t * 1.3 + rand(x,y) * 6.28);
      const hover = pointer ? Math.pow(clamp(1 - Math.hypot(px - pointer.x, py - pointer.y) / (cell * 8)), 2) : 0;
      const active = mask[y * cols + x];
      const edge = cols - 2 - (y / rows) * 10;
      const edgeFade = clamp((edge - x) / 5);
      ctx.globalAlpha = clamp((active ? .10 + wave * .10 : .018 + wave * .035) + hover * .08) * edgeFade * Math.min(1, local * 1.6);
      const size = cell * (.65 + wave * .10 + hover * .12) * ease;
      ctx.fillRect(px - size / 2, py - size / 2, size, size);
    }
    ctx.globalAlpha = 1;
  };
  const tick = now => { if (!start) start = now; draw((now - start) / 1000); frame = requestAnimationFrame(tick); };
  image.onload = () => {
    const sample = document.createElement('canvas'); sample.width = cols; sample.height = rows;
    const s = sample.getContext('2d', {willReadFrequently:true});
    // A primeira parte da imagem original contém apenas o símbolo AX.
    s.drawImage(image, 0, 0, image.width * .31, image.height, 4, 7, 60, 34);
    const pixels = s.getImageData(0, 0, cols, rows).data;
    for (let i = 0; i < mask.length; i++) mask[i] = pixels[i * 4 + 3] > 75 ? 1 : 0;
    resize(); if (!reduced.matches) frame = requestAnimationFrame(tick);
  };
  const observer = new ResizeObserver(resize); observer.observe(host);
  host.addEventListener('pointermove', e => { const rect = host.getBoundingClientRect(); pointer = {x:e.clientX - rect.left,y:e.clientY - rect.top}; });
  host.addEventListener('pointerleave', () => { pointer = null; });
  new MutationObserver(() => { if (reduced.matches) draw(100); }).observe(root, {attributes:true,attributeFilter:['data-theme']});
  reduced.addEventListener('change', () => { cancelAnimationFrame(frame); frame = 0; if (reduced.matches) draw(100); else { start = 0; frame = requestAnimationFrame(tick); } });
})();
