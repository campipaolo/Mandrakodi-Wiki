# Calendario F1 e MotoGP

<div id="events-container">Caricamento in corso...</div>

<script>
async function loadEvents() {
  const container = document.getElementById('events-container');

  // Costruisce i percorsi corretti tenendo conto del baseurl di GitHub Pages (/Mandrakodi-Wiki/)
  const baseUrl = window.location.pathname.split('/docs/')[0].split('/calendario/')[0].replace(/\/$/, '');

  const possiblePaths = [
    './events.json',
    '../events.json',
    '../../events.json',
    `${baseUrl}/events.json`,
    `${baseUrl}/calendario/events.json`,
    `${baseUrl}/docs/calendario/events.json`
  ];

  let data = null;

  for (const path of possiblePaths) {
    try {
      const res = await fetch(path);
      if (res.ok) {
        data = await res.json();
        console.log(`[EPG Success] File caricato con successo da: ${path}`);
        break;
      }
    } catch (e) {
      // Prova il percorso successivo
    }
  }

  if (!data || data.length === 0) {
    container.innerHTML = '<p>Nessun evento disponibile o file JSON non ancora generato.</p>';
    return;
  }

  let html = '<ul style="list-style-type: none; padding: 0;">';
  data.forEach(item => {
    html += `<li style="margin-bottom: 8px; padding: 10px; border-bottom: 1px solid #444; background: rgba(255,255,255,0.05); border-radius: 4px;">
      <strong style="color: #ff4757;">[${item.category}]</strong> ${item.event}
    </li>`;
  });
  html += '</ul>';

  container.innerHTML = html;
}

loadEvents();
</script>

