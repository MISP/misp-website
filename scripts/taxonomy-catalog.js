(() => {
  'use strict';
  const root = document.getElementById('misp-taxonomy-catalog');
  if (!root) return;
  const cards = Array.from(root.querySelectorAll('.mt-card'));
  const grid = root.querySelector('#mt-grid');
  const search = root.querySelector('#mt-search');
  const structure = root.querySelector('#mt-structure');
  const sort = root.querySelector('#mt-sort');
  const count = root.querySelector('#mt-count');
  const empty = root.querySelector('.mt-empty');
  const fold = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const indexes = new Map(cards.map(card => [card, fold(card.dataset.search)]));
  function filter() {
    const terms = fold(search.value.trim()).split(/\s+/).filter(Boolean);
    let visible = 0;
    for (const card of cards) {
      const match = terms.every(term => indexes.get(card).includes(term))
        && (!structure.value || card.dataset.structure === structure.value);
      card.hidden = !match;
      if (match) visible++;
    }
    count.textContent = visible === cards.length
      ? `Showing all ${cards.length} taxonomies`
      : `Showing ${visible} of ${cards.length} taxonomies`;
    empty.hidden = visible > 0;
  }
  function reorder() {
    const ordered = cards.slice().sort((a, b) => {
      const difference = sort.value === 'tags' ? Number(b.dataset.tags) - Number(a.dataset.tags) : 0;
      return difference || a.dataset.namespace.localeCompare(b.dataset.namespace);
    });
    const fragment = document.createDocumentFragment();
    ordered.forEach(card => fragment.appendChild(card));
    grid.appendChild(fragment);
  }
  search.addEventListener('input', filter);
  structure.addEventListener('change', filter);
  sort.addEventListener('change', reorder);
  root.querySelector('#mt-reset').addEventListener('click', () => {
    search.value = ''; structure.value = ''; sort.value = 'name';
    reorder(); filter(); search.focus();
  });
  root.querySelector('.mt-toolbar').hidden = false;
  filter();
})();
