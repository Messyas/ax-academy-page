(() => {
  const strips = document.querySelectorAll('[data-tech-strip]');
  if (!strips.length) return;
  const visibility = 'IntersectionObserver' in window
    ? new IntersectionObserver(entries => entries.forEach(({ target, isIntersecting }) => {
      target.dataset.inView = String(isIntersecting);
    })) : null;
  strips.forEach(strip => {
    strip.dataset.enhanced = 'true';
    if (visibility) visibility.observe(strip);
    else strip.dataset.inView = 'true';
  });
})();
