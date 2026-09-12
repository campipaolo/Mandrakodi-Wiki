<!-- TABELLA SEGNALAZIONI APERTE -->
<div id="lista-segnalazioni-box" style="background: #1e1e2e; color: #fff; padding: 15px; border-radius: 8px; margin-bottom: 25px;">
  <h3 style="margin-top:0; color: #ffab00;">⚠️ Segnalazioni Attive / Non Funzionanti</h3>
  <table style="width:100%; border-collapse: collapse; color: #fff;">
    <thead>
      <tr style="border-bottom: 2px solid #444; text-align: left;">
        <th>Data</th>
        <th>Sezione</th>
        <th>Contenuto/Canale</th>
        <th>Problema</th>
        <th>Stato</th>
      </tr>
    </thead>
    <tbody id="tabella-segnalazioni">
      <tr><td colspan="5">Caricamento segnalazioni...</td></tr>
    </tbody>
  </table>
</div>

<!-- FORM DI SEGNALAZIONE -->
<div style="background: #2a2a3c; padding: 20px; border-radius: 8px; color: #fff;">
  <h3>Segnala un contenuto non funzionante</h3>
  <form id="reportForm">
    <label>Sezione (Obbligatorio):</label><br>
    <select id="sezione" required style="width:100%; padding: 8px; margin: 8px 0;">
      <option value="">-- Seleziona Sezione --</option>
      <option value="Film">Film</option>
      <option value="Serie TV">Serie TV</option>
      <option value="Canali Live">Canali Live</option>
      <option value="Sports">Sports</option>
    </select><br>

    <label>Nome Contenuto / Canale (Obbligatorio):</label><br>
    <input type="text" id="contenuto" required placeholder="Es. Sky Sport Uno oppure Nome Film" style="width:100%; padding: 8px; margin: 8px 0;"><br>
    
    <div id="duplicate-warning" style="display:none; background: #d32f2f; color: white; padding: 10px; border-radius: 4px; margin: 8px 0;">
      ❌ <strong>Attenzione:</strong> Risulta già una segnalazione attiva per questo contenuto!
    </div>
    
    <label>Tipo di Problema (Obbligatorio):</label><br>
    <select id="problema" required style="width:100%; padding: 8px; margin: 8px 0;">
      <option value="">-- Seleziona Problema --</option>
      <option value="Link non funzionante / No Stream">Link non funzionante / No Stream</option>
      <option value="Buffering continuo">Buffering continuo</option>
      <option value="Audio/Video fuori sincro">Audio/Video fuori sincro</option>
      <option value="Traccia audio errata">Traccia audio errata</option>
    </select><br>
    
    <label>Dispositivo (Obbligatorio):</label><br>
    <select id="piattaforma" required style="width:100%; padding: 8px; margin: 8px 0;">
      <option value="">-- Seleziona Piattaforma --</option>
      <option value="Android TV / Firestick">Android TV / Firestick</option>
      <option value="Windows">Windows</option>
      <option value="Linux / CoreELEC">Linux / CoreELEC</option>
      <option value="Altro">Altro</option>
    </select><br><br>
    
    <button type="submit" id="btnSubmit" style="background: #2196F3; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer;">Invia Segnalazione</button>
  </form>
</div>

<script>
  // INCOLLA QUI L'URL DI GOOGLE APPS SCRIPT
  const SCRIPT_URL = "https://script.google.com/macros/s/TUO_SCRIPT_ID/exec";

  // Carica segnalazioni all'avvio
  async function loadReports() {
    try {
      const res = await fetch(`${SCRIPT_URL}?action=getOpen`);
      const data = await res.json();
      const tbody = document.getElementById('tabella-segnalazioni');
      tbody.innerHTML = '';

      if (data.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5">Nessuna segnalazione attiva al momento.</td></tr>';
        return;
      }
    
      data.forEach(item => {
        tbody.innerHTML += `
          <tr style="border-bottom: 1px solid #444;">
            <td>${item.data}</td>
            <td>${item.sezione}</td>
            <td><strong>${item.contenuto}</strong></td>
            <td>${item.problema}</td>
            <td><span style="background: #ff9800; padding: 2px 6px; border-radius: 4px; font-size: 12px; color: #000;">${item.stato}</span></td>
          </tr>
        `;
      });
    } catch (e) {
      console.error(e);
    }
  }

  // Controllo duplicati al cambio del nome contenuto o sezione
  const contenutoInput = document.getElementById('contenuto');
  const sezioneSelect = document.getElementById('sezione');
  const warningDiv = document.getElementById('duplicate-warning');
  const btnSubmit = document.getElementById('btnSubmit');

  async function checkDuplicate() {
    const sezione = sezioneSelect.value;
    const contenuto = contenutoInput.value;

    if (sezione && contenuto.length > 2) {
      const res = await fetch(`${SCRIPT_URL}?action=checkDuplicate&sezione=${encodeURIComponent(sezione)}&contenuto=${encodeURIComponent(contenuto)}`);
      const result = await res.json();
    
      if (result.duplicate) {
        warningDiv.style.display = 'block';
        btnSubmit.disabled = true;
        btnSubmit.style.opacity = '0.5';
      } else {
        warningDiv.style.display = 'none';
        btnSubmit.disabled = false;
        btnSubmit.style.opacity = '1';
      }
    }
  }

  contenutoInput.addEventListener('blur', checkDuplicate);
  sezioneSelect.addEventListener('change', checkDuplicate);

  // Invio Form
  document.getElementById('reportForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    btnSubmit.innerText = "Invio in corso...";
    btnSubmit.disabled = true;

    const payload = {
      sezione: document.getElementById('sezione').value,
      contenuto: document.getElementById('contenuto').value,
      problema: document.getElementById('problema').value,
      piattaforma: document.getElementById('piattaforma').value
    };
    
    await fetch(SCRIPT_URL, {
      method: 'POST',
      body: JSON.stringify(payload)
    });
    
    alert('Segnalazione inviata con successo!');
    document.getElementById('reportForm').reset();
    btnSubmit.innerText = "Invia Segnalazione";
    btnSubmit.disabled = false;
    loadReports();
  });

  loadReports();
</script>