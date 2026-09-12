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

    <!-- LIVELLO 1: MACRO CATEGORIA -->
    <label>Categoria Principale (Obbligatorio):</label><br>
    <select id="cat_principale" required onchange="aggiornaSubCat()" style="width:100%; padding: 8px; margin: 8px 0; background: #1e1e2e; color: #fff; border: 1px solid #555;">
      <option value="">-- Seleziona Categoria --</option>
      <option value="SPORT">SPORT</option>
      <option value="LIVE">LIVE</option>
      <option value="ONDEMAND">ONDEMAND</option>
      <option value="RADIO">RADIO</option>
    </select><br>
    
    <!-- LIVELLO 2: SOTTO CATEGORIA -->
    <label>Sotto-Categoria (Obbligatorio):</label><br>
    <select id="cat_secondaria" required disabled onchange="aggiornaContenuti()" style="width:100%; padding: 8px; margin: 8px 0; background: #1e1e2e; color: #fff; border: 1px solid #555;">
      <option value="">-- Prima seleziona la Categoria --</option>
    </select><br>
    
    <!-- LIVELLO 3: CONTENUTO SPECIFICO -->
    <label>Contenuto / Lista Specifica (Obbligatorio):</label><br>
    <select id="contenuto_specifico" required disabled style="width:100%; padding: 8px; margin: 8px 0; background: #1e1e2e; color: #fff; border: 1px solid #555;">
      <option value="">-- Prima seleziona la Sotto-Categoria --</option>
    </select><br>
    
    <div id="duplicate-warning" style="display:none; background: #d32f2f; color: white; padding: 10px; border-radius: 4px; margin: 8px 0;">
      ❌ <strong>Attenzione:</strong> Risulta già una segnalazione attiva per questo specifico contenuto!
    </div>
    
    <!-- PROBLEMA -->
    <label>Tipo di Problema (Obbligatorio):</label><br>
    <select id="problema" required style="width:100%; padding: 8px; margin: 8px 0; background: #1e1e2e; color: #fff; border: 1px solid #555;">
      <option value="">-- Seleziona Problema --</option>
      <option value="Link non funzionante / No Stream">Link non funzionante / No Stream</option>
      <option value="Buffering continuo">Buffering continuo</option>
      <option value="Audio/Video fuori sincro">Audio/Video fuori sincro</option>
      <option value="Traccia audio errata">Traccia audio errata</option>
      <option value="Canale/Lista offline">Canale/Lista offline</option>
    </select><br>
    
    <!-- PIATTAFORMA -->
    <label>Dispositivo / Sistema (Obbligatorio):</label><br>
    <select id="piattaforma" required style="width:100%; padding: 8px; margin: 8px 0; background: #1e1e2e; color: #fff; border: 1px solid #555;">
      <option value="">-- Seleziona Piattaforma --</option>
      <option value="Android TV / Firestick">Android TV / Firestick</option>
      <option value="Windows">Windows</option>
      <option value="Linux / CoreELEC">Linux / CoreELEC</option>
      <option value="Altro">Altro</option>
    </select><br><br>
    
    <button type="submit" id="btnSubmit" style="background: #2196F3; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-weight: bold;">Invia Segnalazione</button>
  </form>
</div>

<script>
  var SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxBf2aK5ILmULSlcuuGR6K47vsuJbdwj1b1jEtBwl8qMEzXCZRr0QKG5wc4ZAoVnj4/exec";

  var datiStruttura = {
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

  function aggiornaSubCat() {
    var cat = document.getElementById('cat_principale').value;
    var subSelect = document.getElementById('cat_secondaria');
    var itemSelect = document.getElementById('contenuto_specifico');

    subSelect.innerHTML = '<option value="">-- Seleziona Sotto-Categoria --</option>';
    itemSelect.innerHTML = '<option value="">-- Prima seleziona la Sotto-Categoria --</option>';
    itemSelect.disabled = true;
    
    if (cat && datiStruttura[cat]) {
      subSelect.disabled = false;
      for (var sub in datiStruttura[cat]) {
        var opt = document.createElement('option');
        opt.value = sub;
        opt.text = sub;
        subSelect.appendChild(opt);
      }
    } else {
      subSelect.disabled = true;
    }
  }

  function aggiornaContenuti() {
    var cat = document.getElementById('cat_principale').value;
    var sub = document.getElementById('cat_secondaria').value;
    var itemSelect = document.getElementById('contenuto_specifico');

    itemSelect.innerHTML = '<option value="">-- Seleziona Contenuto/Lista --</option>';
    
    if (cat && sub && datiStruttura[cat] && datiStruttura[cat][sub]) {
      itemSelect.disabled = false;
      var lista = datiStruttura[cat][sub];
      for (var i = 0; i < lista.length; i++) {
        var opt = document.createElement('option');
        opt.value = lista[i];
        opt.text = lista[i];
        itemSelect.appendChild(opt);
      }
    } else {
      itemSelect.disabled = true;
    }
  }

  // Carica la tabella segnalazioni aperte
  function loadReports() {
    fetch(SCRIPT_URL + "?action=getOpen")
      .then(function(res) { return res.json(); })
      .then(function(data) {
        var tbody = document.getElementById('tabella-segnalazioni');
        tbody.innerHTML = '';
        if (!data || data.length === 0) {
          tbody.innerHTML = '<tr><td colspan="5">Nessuna segnalazione attiva al momento.</td></tr>';
          return;
        }
        data.forEach(function(item) {
          tbody.innerHTML += '<tr style="border-bottom: 1px solid #444;">' +
            '<td>' + item.data + '</td>' +
            '<td><span style="background: #333; padding: 2px 6px; border-radius: 4px;">' + item.sezione + '</span></td>' +
            '<td><strong>' + item.contenuto + '</strong></td>' +
            '<td>' + item.problema + '</td>' +
            '<td><span style="background: #ff9800; padding: 2px 6px; border-radius: 4px; font-size: 12px; color: #000;">' + item.stato + '</span></td>' +
          '</tr>';
        });
      })
      .catch(function(err) { console.error("Errore caricamento:", err); });
  }

  // Invio Form
  document.getElementById('reportForm').addEventListener('submit', function(e) {
    e.preventDefault();
    var btn = document.getElementById('btnSubmit');
    btn.innerText = "Invio in corso...";
    btn.disabled = true;

    var macro = document.getElementById('cat_principale').value;
    var sub = document.getElementById('cat_secondaria').value;
    var item = document.getElementById('contenuto_specifico').value;
    
    var payload = {
      sezione: macro,
      contenuto: macro + ' > ' + sub + ' > ' + item,
      problema: document.getElementById('problema').value,
      piattaforma: document.getElementById('piattaforma').value
    };
    
    fetch(SCRIPT_URL, {
      method: 'POST',
      mode: 'no-cors',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    .then(function() {
      alert('Segnalazione inviata con successo!');
      document.getElementById('reportForm').reset();
      document.getElementById('cat_secondaria').disabled = true;
      document.getElementById('contenuto_specifico').disabled = true;
      btn.innerText = "Invia Segnalazione";
      btn.disabled = false;
      setTimeout(loadReports, 1500);
    })
    .catch(function(err) {
      alert('Errore invio!');
      btn.innerText = "Invia Segnalazione";
      btn.disabled = false;
    });
  });

  loadReports();
</script>