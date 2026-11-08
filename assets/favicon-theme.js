(() => {
  const icon = document.querySelector('link[rel="icon"]');
  if (!icon) return;
  const browserTheme = window.matchMedia('(prefers-color-scheme: dark)');
  const update = () => { icon.href = browserTheme.matches ? 'assets/favicon-dark.png' : 'assets/favicon-light.png'; };
  update();
  if (browserTheme.addEventListener) browserTheme.addEventListener('change', update);
  else if (browserTheme.addListener) browserTheme.addListener(update);
})();
