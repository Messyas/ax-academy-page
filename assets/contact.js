(() => {
  const dialog = document.querySelector('[data-contact-dialog]');
  const openButton = document.querySelector('[data-contact-open]');
  const form = document.querySelector('[data-contact-form]');
  if (!dialog || !openButton || !form) return;

  const select = dialog.querySelector('[data-contact-select]');
  const trigger = select?.querySelector('[data-select-trigger]');
  const valueInput = select?.querySelector('[data-select-value]');
  const valueLabel = select?.querySelector('[data-select-label]');
  const listbox = select?.querySelector('[role="listbox"]');
  const options = [...(select?.querySelectorAll('[role="option"]') || [])];
  const error = dialog.querySelector('#contact-subject-error');
  let activeIndex = -1;

  const setActive = index => {
    activeIndex = (index + options.length) % options.length;
    options.forEach((option, i) => option.dataset.active = String(i === activeIndex));
    trigger.setAttribute('aria-activedescendant', options[activeIndex].id);
  };
  const closeSelect = ({ focus = false } = {}) => {
    if (!trigger || !listbox) return;
    listbox.hidden = true;
    trigger.setAttribute('aria-expanded', 'false');
    trigger.removeAttribute('aria-activedescendant');
    options.forEach(option => delete option.dataset.active);
    activeIndex = -1;
    if (focus) trigger.focus();
  };
  const openSelect = () => {
    listbox.hidden = false;
    trigger.setAttribute('aria-expanded', 'true');
    const selected = options.findIndex(option => option.dataset.value === valueInput.value);
    setActive(selected >= 0 ? selected : 0);
  };
  const chooseOption = option => {
    valueInput.value = option.dataset.value;
    valueLabel.textContent = option.dataset.value;
    options.forEach(item => item.setAttribute('aria-selected', String(item === option)));
    trigger.removeAttribute('aria-invalid');
    error.hidden = true;
    closeSelect({ focus: true });
  };

  if (trigger && listbox && valueInput && valueLabel) {
    trigger.addEventListener('click', () => {
      if (trigger.getAttribute('aria-expanded') === 'true') closeSelect();
      else openSelect();
    });
    trigger.addEventListener('keydown', event => {
      const expanded = trigger.getAttribute('aria-expanded') === 'true';
      if (event.key === 'ArrowDown' || event.key === 'ArrowUp') {
        event.preventDefault();
        if (!expanded) openSelect();
        else setActive(activeIndex + (event.key === 'ArrowDown' ? 1 : -1));
      } else if ((event.key === 'Enter' || event.key === ' ') && expanded) {
        event.preventDefault();
        chooseOption(options[activeIndex]);
      } else if (event.key === 'Home' && expanded) {
        event.preventDefault(); setActive(0);
      } else if (event.key === 'End' && expanded) {
        event.preventDefault(); setActive(options.length - 1);
      } else if (event.key === 'Escape' && expanded) {
        event.preventDefault(); event.stopPropagation(); closeSelect();
      } else if (event.key === 'Tab' && expanded) {
        closeSelect();
      }
    });
    options.forEach(option => {
      option.addEventListener('pointerenter', () => setActive(options.indexOf(option)));
      option.addEventListener('click', () => chooseOption(option));
    });
    document.addEventListener('pointerdown', event => {
      if (!select.contains(event.target)) closeSelect();
    });
    form.addEventListener('reset', () => {
      valueInput.value = '';
      valueLabel.textContent = 'Selecione um assunto';
      options.forEach(option => option.setAttribute('aria-selected', 'false'));
      trigger.removeAttribute('aria-invalid');
      error.hidden = true;
      closeSelect();
    });
  }

  openButton.addEventListener('click', () => dialog.showModal());
  dialog.querySelectorAll('[data-contact-close]').forEach(button => {
    button.addEventListener('click', () => dialog.close());
  });
  dialog.addEventListener('click', event => {
    if (event.target === dialog) dialog.close();
  });
  dialog.addEventListener('close', () => openButton.focus());
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!valueInput.value) {
      trigger.setAttribute('aria-invalid', 'true');
      error.hidden = false;
      trigger.focus();
      return;
    }
    if (!form.reportValidity()) return;

    const fields = new FormData(form);
    const subject = `AX Academy | ${fields.get('subject')}`;
    const body = `E-mail para resposta: ${fields.get('email')}\n\nMensagem:\n${fields.get('message')}`;
    const recipient = dialog.dataset.recipient;
    window.location.href = `mailto:${recipient}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  });
})();
