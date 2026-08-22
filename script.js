(() => {
  const search = document.querySelector('#archive-search');
  const items = [...document.querySelectorAll('.archive-item')];
  const filters = [...document.querySelectorAll('[data-filter]')];
  const count = document.querySelector('#result-count');
  const noResults = document.querySelector('.no-results');
  let activeFilter = 'all';

  const updateArchive = () => {
    const query = (search?.value || '').trim().toLocaleLowerCase();
    let visible = 0;
    items.forEach((item) => {
      const categoryMatch = activeFilter === 'all' || item.dataset.category === activeFilter;
      const queryMatch = !query || item.dataset.search.toLocaleLowerCase().includes(query) || item.textContent.toLocaleLowerCase().includes(query);
      item.hidden = !(categoryMatch && queryMatch);
      if (!item.hidden) visible += 1;
    });
    if (count) count.textContent = String(visible);
    if (noResults) noResults.hidden = visible !== 0;
  };

  search?.addEventListener('input', updateArchive);
  filters.forEach((button) => {
    button.addEventListener('click', () => {
      activeFilter = button.dataset.filter;
      filters.forEach((filter) => filter.classList.toggle('is-active', filter === button));
      updateArchive();
    });
  });

  items.forEach((item) => {
    const destination = item.dataset.href || 'https://birlab.org/research/';
    const title = item.querySelector('h3')?.textContent || 'project';
    item.classList.add('is-linked');
    item.setAttribute('role', 'link');
    item.setAttribute('tabindex', '0');
    item.setAttribute('aria-label', `${title} — open project archive`);
    const openProject = () => window.open(destination, '_blank', 'noopener');
    item.addEventListener('click', openProject);
    item.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        openProject();
      }
    });
  });

  const dialog = document.querySelector('.lightbox');
  const dialogImage = dialog?.querySelector('img');
  const dialogCaption = dialog?.querySelector('p');
  document.querySelectorAll('.gallery-item').forEach((item) => {
    item.addEventListener('click', () => {
      const source = item.querySelector('img');
      if (!dialog || !dialogImage || !dialogCaption || !source) return;
      dialogImage.src = source.src;
      dialogImage.alt = source.alt;
      dialogCaption.textContent = item.dataset.caption || source.alt;
      dialog.showModal();
    });
  });
  dialog?.querySelector('.lightbox-close')?.addEventListener('click', () => dialog.close());
  dialog?.addEventListener('click', (event) => {
    if (event.target === dialog) dialog.close();
  });
})();
