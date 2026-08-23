document.documentElement.classList.add('js');

document.querySelectorAll('.site-menu').forEach((menu) => {
  const button = menu.querySelector('.menu-toggle');
  const navigation = menu.querySelector('.nav-links');

  if (!button || !navigation) return;

  const setOpen = (open) => {
    menu.classList.toggle('is-open', open);
    button.setAttribute('aria-expanded', String(open));
    button.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
  };

  button.addEventListener('click', () => {
    setOpen(button.getAttribute('aria-expanded') !== 'true');
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') setOpen(false);
  });

  document.addEventListener('click', (event) => {
    if (!menu.contains(event.target)) setOpen(false);
  });
});
