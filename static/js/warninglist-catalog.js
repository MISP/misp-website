/* Progressive enhancement: every list and detail is available without JavaScript. */
(() => {
  'use strict';
  const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  document.querySelectorAll('.warninglist-catalog').forEach(catalog => {
    const search = catalog.querySelector('.warninglist-search');
    const type = catalog.querySelector('.warninglist-type');
    const attribute = catalog.querySelector('.warninglist-attribute');
    const cards = Array.from(catalog.querySelectorAll('.warninglist-card'));
    const indexed = cards.map(card => ({card, text: normalize(card.dataset.search), attributes: JSON.parse(card.dataset.attributes)}));
    function update() {
      const terms = normalize(search.value).trim().split(/\s+/).filter(Boolean);
      let count = 0;
      indexed.forEach(({card, text, attributes}) => {
        const matches = (!type.value || type.value === card.dataset.type) &&
          (!attribute.value || attributes.includes(attribute.value) || attributes.includes('ALL')) &&
          terms.every(term => text.includes(term));
        card.hidden = !matches;
        if (matches) count++;
      });
      catalog.querySelector('.warninglist-count').textContent = `${count} of ${cards.length} warning lists`;
      catalog.querySelector('.warninglist-empty').hidden = count !== 0;
    }
    catalog.querySelector('.warninglist-toolbar').hidden = false;
    search.addEventListener('input', update);
    type.addEventListener('change', update);
    attribute.addEventListener('change', update);
    catalog.querySelector('.warninglist-reset').addEventListener('click', () => {
      search.value = '';
      type.value = '';
      attribute.value = '';
      update();
      search.focus();
    });
    update();
  });
})();
