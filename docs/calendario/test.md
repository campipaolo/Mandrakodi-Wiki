# Calendario F1 e MotoGP

<div id="events-container">Caricamento in corso...</div>

<script>
async function loadEvents() {
  const container = document.getElementById('events-container');

  // Prova prima a leggere il file nella stessa cartella, poi risale alla root
  const paths = ['./events.json', '../../events.json', '/events.json'];
  let data = null;

  for (const path of paths) {
    try {
      const res = await fetch(path);
      if (res.ok) {
        data = await res.json();
        break;
      }
    } catch (e) {
      continue;
    }
  }

  if (!data || data.length === 0) {
    container.innerHTML = '<p>Nessun evento trovato al momento.</p>';
    return;
  }

  let html = '<ul style="list-style-type: none; padding: 0;">';
  data.forEach(item => {
    html += `<li style="margin-bottom: 8px; padding: 8px; border-bottom: 1px solid #ccc;">
      <strong>[${item.category}]</strong> ${item.event}
    </li>`;
  });
  html += '</ul>';

  container.innerHTML = html;
}

loadEvents();
</script>