<!-- TABELLA SEGNALAZIONI APERTE -->
<div id="lista-segnalazioni-box" style="background: #1e1e2e; color: #fff; padding: 15px; border-radius: 8px; margin-bottom: 25px;">
  <h3 style="margin-top:0; color: #ffab00;">⚠️ Segnalazioni Attive / Non Funzionanti</h3>
  <table style="width:100%; border-collapse: collapse; color: #fff;">
    <thead>
      <tr style="border-bottom: 2px solid #444; text-align: left;">
        <th>Data</th>
        <th>Categoria</th>
        <th>Sotto-Categoria / Contenuto</th>
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

    <!-- LIVALLO 1: MACRO CATEGORIA -->
    <label>Categoria Principale (Obbligatorio):</label><br>
    <select id="cat_principale" required style="width:100%; padding: 8px; margin: 8px 0;">
      <option value="">-- Seleziona Categoria --</option>
      <option value="SPORT">SPORT</option>
      <option value="LIVE">LIVE</option>
      <option value="ONDEMAND">ONDEMAND</option>
      <option value="RADIO">RADIO</option>
    </select><br>
    
    <!-- LIVELLO 2: SOTTO CATEGORIA -->
    <label>Sotto-Categoria (Obbligatorio):</label><br>
    <select id="cat_secondaria" required disabled style="width:100%; padding: 8px; margin: 8px 0;">
      <option value="">-- Prima seleziona la Categoria --</option>
    </select><br>
    
    <!-- LIVELLO 3: CONTENUTO SPECIFICO -->
    <label>Contenuto / Lista Specifica (Obbligatorio):</label><br>
    <select id="contenuto_specifico" required disabled style="width:100%; padding: 8px; margin: 8px 0;">
      <option value="">-- Prima seleziona la Sotto-Categoria --</option>
    </select><br>
    
    <div id="duplicate-warning" style="display:none; background: #d32f2f; color: white; padding: 10px; border-radius: 4px; margin: 8px 0;">
      ❌ <strong>Attenzione:</strong> Risulta già una segnalazione attiva per questo specifico contenuto!
    </div>
    
    <!-- PROBLEMA -->
    <label>Tipo di Problema (Obbligatorio):</label><br>
    <select id="problema" required style="width:100%; padding: 8px; margin: 8px 0;">
      <option value="">-- Seleziona Problema --</option>
      <option value="Link non funzionante / No Stream">Link non funzionante / No Stream</option>
      <option value="Buffering continuo">Buffering continuo</option>
      <option value="Audio/Video fuori sincro">Audio/Video fuori sincro</option>
      <option value="Traccia audio errata">Traccia audio errata</option>
      <option value="Canale/Lista offline">Canale/Lista offline</option>
    </select><br>
    
    <!-- PIATTAFORMA -->
    <label>Dispositivo / Sistema (Obbligatorio):</label><br>
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
  // INCOLLA QUI L'URL DELLA TUA WEB APP GOOGLE APPS SCRIPT
  const SCRIPT_URL = "https://script.google.com/macros/s/TUO_SCRIPT_ID/exec";

  // ALBERO DEI DATI GERARCHICO
  const datiStruttura = {
    "SPORT": {
      "Liste Eventi": [
        "Lista 1 (Daddy)",
        "Lista 2 (Platin - Ace)",
        "Lista 3 (Sportzonline)",
        "Lista 4 (SportzX)",
        "Lista 5 (CDN)",
        "Lista 6 (Fitlibre)"
      ],
      "Liste Canali": [
        "MPD (Nazioni)",
        "MPD (All)",
        "Sky",
        "Sky 2",
        "Lista Ace 1",
        "Free Live Sport",
        "Mediahosting Channel",
        "Lista 1 (Github 1)",
        "Lista 2 (Github 2)",
        "Lista 3 (Rocktalk)",
        "Lista 4 (Partite)",
        "Lista 5 (Sportsonline)",
        "Lista 6 (Sports99)",
        "Lista 7 (Rustinco Tv)",
        "Lista 8 (Daddy)"
      ],
      "Roja Tube": [
        "Roja Tube"
      ],
      "Sport Replay": [
        "Soccer Replay",
        "Motor Sport Replay",
        "NBA Replay",
        "WNBA Replay",
        "Eurolegue Replay",
        "NFL Condensed Replay",
        "UFC Replay",
        "Tennis Replay",
        "WWE Replay"
      ]
    },
    "LIVE": {
      "Generale": ["Tutti i canali LIVE"]
    },
    "ONDEMAND": {
      "Generale": ["Tutti i contenuti ONDEMAND"]
    },
    "RADIO": {
      "Generale": ["Tutte le stazioni RADIO"]
    }
  };

  const catPrincipale = document.getElementById('cat_principale');
  const catSecondaria = document.getElementById('cat_secondaria');
  const contenutoSpecifico = document.getElementById('contenuto_specifico');
  const warningDiv = document.getElementById('duplicate-warning');
  const btnSubmit = document.getElementById('btnSubmit');

  // Gestione Cambio Categoria Principale
  catPrincipale.addEventListener('change', () => {
    const val = catPrincipale.value;
    catSecondaria.innerHTML = '<option value="">-- Seleziona Sotto-Categoria --</option>';
    contenutoSpecifico.innerHTML = '<option value="">-- Prima seleziona la Sotto-Categoria --</option>';
    contenutoSpecifico.disabled = true;

    if (val && datiStruttura[val]) {
      catSecondaria.disabled = false;
      Object.keys(datiStruttura[val]).forEach(subCat => {
        catSecondaria.innerHTML += `<option value="${subCat}">${subCat}</option>`;
      });
    } else {
      catSecondaria.disabled = true;
    }
    checkDuplicate();
  });

  // Gestione Cambio Sotto-Categoria
  catSecondaria.addEventListener('change', () => {
    const macro = catPrincipale.value;
    const sub = catSecondaria.value;
    contenutoSpecifico.innerHTML = '<option value="">-- Seleziona Contenuto/Lista --</option>';

    if (macro && sub && datiStruttura[macro][sub]) {
      contenutoSpecifico.disabled = false;
      datiStruttura[macro][sub].forEach(item => {
        contenutoSpecifico.innerHTML += `<option value="${item}">${item}</option>`;
      });
    } else {
      contenutoSpecifico.disabled = true;
    }
    checkDuplicate();
  });

  contenutoSpecifico.addEventListener('change', checkDuplicate);

  // Controllo Duplicati via API
  async function checkDuplicate() {
    const macro = catPrincipale.value;
    const sub = catSecondaria.value;
    const item = contenutoSpecifico.value;

    if (macro && sub && item) {
      const nomeCompleto = `${macro} > ${sub} > ${item}`;
      try {
        const res = await fetch(`${SCRIPT_URL}?action=checkDuplicate&sezione=${encodeURIComponent(macro)}&contenuto=${encodeURIComponent(nomeCompleto)}`);
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
      } catch (e) {
        console.error("Errore verifica duplicato", e);
      }
    }
  }

  // Caricamento segnalazioni aperte in testata
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
            <td><span style="background: #333; padding: 2px 6px; border-radius: 4px;">${item.sezione}</span></td>
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

 // Invio Form Corretto con gestione CORS
  document.getElementById('reportForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    btnSubmit.innerText = "Invio in corso...";
    btnSubmit.disabled = true;

    const macro = catPrincipale.value;
    const sub = catSecondaria.value;
    const item = contenutoSpecifico.value;
    
    const payload = {
      sezione: macro,
      contenuto: `${macro} > ${sub} > ${item}`,
      problema: document.getElementById('problema').value,
      piattaforma: document.getElementById('piattaforma').value
    };
    
    try {
      await fetch(SCRIPT_URL, {
        method: 'POST',
        mode: 'no-cors', // Evita il blocco CORS su Google Apps Script
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });
    
      alert('Segnalazione inviata con successo!');
      document.getElementById('reportForm').reset();
      catSecondaria.disabled = true;
      catSecondaria.innerHTML = '<option value="">-- Prima seleziona la Categoria --</option>';
      contenutoSpecifico.disabled = true;
      contenutoSpecifico.innerHTML = '<option value="">-- Prima seleziona la Sotto-Categoria --</option>';
      
      // Ricarica la lista dopo un piccolo ritardo per dare tempo allo script di aggiornare il foglio
      setTimeout(loadReports, 1500);
    
    } catch (error) {
      console.error('Errore durante l invio:', error);
      alert('Si è verificato un errore durante l invio. Riprova.');
    } finally {
      btnSubmit.innerText = "Invia Segnalazione";
      btnSubmit.disabled = false;
    }
  });