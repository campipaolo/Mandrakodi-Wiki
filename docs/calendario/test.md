# Programmazione F1 e MotoGP

<div id="events-container">Caricamento eventi in corso...</div>

<script>
async function loadEvents() {
  try {
    const response = await fetch('../../events.json');
    const events = await response.json();
    const container = document.getElementById('events-container');

    if (events.length === 0) {
      container.innerHTML = '<p>Nessun evento disponibile al momento.</p>';
      return;
    }
    
    let html = '<ul>';
    events.forEach(ev => {
      html += `<li><strong>[${ev.category}]</strong> ${ev.raw_event}</li>`;
    });
    html += '</ul>';
    
    container.innerHTML = html;
  } catch (err) {
    document.getElementById('events-container').innerHTML = '<p>Errore nel caricamento del file JSON.</p>';
  }
}

loadEvents();
</script>