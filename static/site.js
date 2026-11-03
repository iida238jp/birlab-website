/* Progressive enhancements. All page content and language links work without JS. */
'use strict';
document.documentElement.classList.add('js');
const filters = document.querySelector('#publication-filters');
if (filters) {
  const search = document.querySelector('#publication-search');
  const year = document.querySelector('#publication-year');
  const type = document.querySelector('#publication-type');
  const rows = Array.from(document.querySelectorAll('.publication')).map(element => ({
    element,
    text: element.querySelector('p').textContent.normalize('NFKC').toLocaleLowerCase(),
    year: element.dataset.year,
    type: element.dataset.type,
  }));
  function applyFilters() {
    const terms = search.value.trim().normalize('NFKC').toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let shown = 0;
    rows.forEach(row => {
      const matches = (!year.value || row.year === year.value)
        && (!type.value || row.type === type.value)
        && terms.every(term => row.text.includes(term));
      row.element.hidden = !matches;
      if (matches) shown++;
    });
    document.querySelector('#result-count').textContent = String(shown);
    document.querySelector('#no-results').hidden = shown > 0;
  }
  filters.addEventListener('submit', event => event.preventDefault());
  filters.addEventListener('input', applyFilters);
  filters.addEventListener('change', applyFilters);
  filters.addEventListener('reset', () => {
    search.value = '';
    year.value = '';
    type.value = '';
    applyFilters();
  });
}
