(() => {
  const projectSlugs = ['eit-tactile-sensing','food-handling-humanoid','multi-layer-tactile-skins','ei-conference','anthropomorphic-robot-hand','roboscientist-falling-paper','agri-food-robotics','physical-robot-evolution','cambridge-arm','thermoplastic-robotics','energy-efficient-locomotion','climbing-robots','clutch-actuators','posture-support','compass-gait','underactuated-locomotion','biped-locomotion','body-dynamics-sensing','underwater-locomotion','puppy','stumpy','bio-inspired-navigation','non-verbal-face-robot'];
  const search = document.querySelector('#archive-search');
  const items = [...document.querySelectorAll('.archive-item')];
  const filters = [...document.querySelectorAll('[data-filter]')];
  const count = document.querySelector('#result-count');
  const countLabel = document.querySelector('#result-label');
  const noResults = document.querySelector('.no-results');
  const showMore = document.querySelector('.archive-more');
  const isFullArchive = document.body.classList.contains('archive-page');
  const isJapanese = document.documentElement.lang === 'ja';
  const mobileQuery = window.matchMedia('(max-width: 760px)');
  let activeFilter = 'all';
  let expanded = false;

  const updateArchive = () => {
    if (!items.length) return;
    const query = (search?.value || '').trim().toLocaleLowerCase();
    const matching = items.filter((item) => {
      const aliases = {embodied:['embodied','systems'], interaction:['interaction','systems']};
      const categoryMatch = activeFilter === 'all' || item.dataset.category === activeFilter || (aliases[activeFilter] || []).includes(item.dataset.category);
      const haystack = `${item.dataset.search || ''} ${item.textContent}`.toLocaleLowerCase();
      return categoryMatch && (!query || haystack.includes(query));
    });
    const collapsed = mobileQuery.matches && !isFullArchive && !expanded && !query && activeFilter === 'all';
    items.forEach((item) => { item.hidden = !matching.includes(item) || (collapsed && matching.indexOf(item) >= 9); });
    if (count) count.textContent = String(matching.length);
    if (countLabel) countLabel.textContent = isJapanese ? '件のプロジェクト' : matching.length === 1 ? 'project' : 'projects';
    if (noResults) noResults.hidden = matching.length !== 0;
    if (showMore) {
      showMore.hidden = isFullArchive || !mobileQuery.matches || query !== '' || activeFilter !== 'all' || matching.length <= 9;
      showMore.textContent = expanded ? (isJapanese ? '表示を戻す' : 'Show fewer') : (isJapanese ? 'さらに表示' : 'Show more');
      showMore.setAttribute('aria-expanded', String(expanded));
    }
  };

  search?.addEventListener('input', updateArchive);
  filters.forEach((button) => button.addEventListener('click', () => {
    activeFilter = button.dataset.filter || 'all';
    filters.forEach((filter) => {
      const active = filter === button;
      filter.classList.toggle('is-active', active);
      filter.setAttribute('aria-pressed', String(active));
    });
    updateArchive();
  }));
  showMore?.addEventListener('click', () => { expanded = !expanded; updateArchive(); });
  mobileQuery.addEventListener?.('change', updateArchive);
  filters.forEach((filter) => filter.setAttribute('aria-pressed', String(filter.dataset.filter === activeFilter)));

  items.forEach((item, index) => {
    const slug = item.id || item.dataset.slug || projectSlugs[index];
    if (!slug) return;
    if (!item.id && isFullArchive) item.id = slug;
    const destination = item.dataset.href || `${isJapanese ? 'projects-jp.html' : 'projects.html'}#${slug}`;
    const title = item.querySelector('h3')?.textContent || (isJapanese ? 'プロジェクト' : 'project');
    item.classList.add('is-linked');
    item.setAttribute('role', 'link');
    item.setAttribute('tabindex', '0');
    item.setAttribute('aria-label', `${title} — ${isJapanese ? 'プロジェクト詳細を開く' : 'open project details'}`);
    const openProject = () => { window.location.href = destination; };
    item.addEventListener('click', openProject);
    item.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); openProject(); }
    });
  });
  updateArchive();

  document.querySelectorAll('.language-switch a').forEach((link) => link.addEventListener('click', () => {
    const target = new URL(link.href, window.location.href);
    if (!target.hash && window.location.hash) target.hash = window.location.hash;
    link.href = target.href;
  }));

  const dialog = document.querySelector('.lightbox');
  const dialogImage = dialog?.querySelector('img');
  const dialogCaption = dialog?.querySelector('p');
  document.querySelectorAll('.gallery-item').forEach((item) => item.addEventListener('click', () => {
    const source = item.querySelector('img');
    if (!dialog || !dialogImage || !dialogCaption || !source) return;
    dialogImage.src = source.currentSrc || source.src;
    dialogImage.alt = source.alt;
    dialogCaption.textContent = item.dataset.caption || source.alt;
    dialog.showModal();
  }));
  dialog?.querySelector('.lightbox-close')?.addEventListener('click', () => dialog.close());
  dialog?.addEventListener('click', (event) => { if (event.target === dialog) dialog.close(); });
})();
