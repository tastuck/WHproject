document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('orderForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const guests = [...document.querySelectorAll('.seat-form')].map(block => {
      return {
        waffles: {
          flavor: block.querySelector('.waffle-flavor')?.value || '',
          qty: parseInt(block.querySelector('.waffle-qty')?.value || '0')
        },
        eggs: block.querySelector('[name="eggs"]')?.value || '',
        meat: block.querySelector('[name="meat"]')?.value || '',
        toast: block.querySelector('[name="toast"]')?.value || '',
        hashbrowns: block.querySelector('[name="hashbrowns"]')?.value || '',
        hashbrownMods: [...block.querySelectorAll('.hashbrown-mods input[type="checkbox"]:checked')].map(cb => cb.value),
        gritsBowl: block.querySelector('[name="grits_bowl"]')?.value || '',
        sandwich: block.querySelector('[name="sandwich"]')?.value || '',
        beverage: block.querySelector('[name="drink"]')?.value || ''
      };
    });

    const response = await fetch('/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ guests })
    });

    const data = await response.json();

    document.getElementById('result').innerText = `
PULL: ${data.pull.join(', ')}
DROP: ${data.drop.join(', ')}
MARK: ${data.mark.join('\n')}
TOTAL: $${data.total.toFixed(2)}
    `;
  });
});

