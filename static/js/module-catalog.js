/* Progressive enhancement: every card and detail is available without JavaScript. */
(() => {
  'use strict';
  const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  document.querySelectorAll('.module-catalog').forEach(catalog => {
    const toolbar = catalog.querySelector('.module-toolbar');
    const search = catalog.querySelector('.module-search');
    const type = catalog.querySelector('.module-type');
    const cards = Array.from(catalog.querySelectorAll('.module-card'));
    const indexed = cards.map(card => ({card, text: normalize(card.dataset.search)}));
    function update() {
      const terms = normalize(search.value).trim().split(/\s+/).filter(Boolean);
      let count = 0;
      indexed.forEach(({card, text}) => {
        const matches = (!type.value || type.value === card.dataset.type) && terms.every(term => text.includes(term));
        card.hidden = !matches;
        if (matches) count++;
      });
      catalog.querySelector('.module-count').textContent = `${count} of ${cards.length} modules`;
      catalog.querySelector('.module-empty').hidden = count !== 0;
    }
    toolbar.hidden = false;
    search.addEventListener('input', update);
    type.addEventListener('change', update);
    catalog.querySelector('.module-reset').addEventListener('click', () => {
      search.value = '';
      type.value = '';
      update();
      search.focus();
    });
    catalog.querySelectorAll('.module-logo img').forEach(img => {
      const fallback = () => { img.hidden = true; };
      img.addEventListener('error', fallback);
      if (img.complete && img.naturalWidth === 0) fallback();
    });
    update();
  });
})();
