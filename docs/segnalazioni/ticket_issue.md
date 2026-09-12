<div style="max-width: 800px; margin: 0 auto; font-family: Arial, sans-serif;">

  <!-- TABELLA SEGNALAZIONI ATTIVE -->
  <h2>📋 Segnalazioni Attive</h2>
  <div style="overflow-x: auto; margin-bottom: 30px;">
    <table style="width: 100%; border-collapse: collapse; text-align: left; background: #1e1e1e; color: #fff; border-radius: 8px; overflow: hidden;">
      <thead>
        <tr style="background: #333; color: #fff;">
          <th style="padding: 10px;">Data</th>
          <th style="padding: 10px;">Sezione / Sotto-Cat.</th>
          <th style="padding: 10px;">Contenuto</th>
          <th style="padding: 10px;">Problema</th>
          <th style="padding: 10px;">Stato</th>
        </tr>
      </thead>
      <tbody id="tabella-segnalazioni">
        <tr>
          <td colspan="5" style="padding: 15px; text-align: center;">Caricamento segnalazioni in corso...</td>
        </tr>
      </tbody>
    </table>
  </div>

  <hr style="border: 0; border-top: 1px solid #444; margin: 30px 0;">

  <!-- FORM INVIO SEGNALAZIONE -->
  <h2>📌 Invia Nuova Segnalazione</h2>

  <form id="form-segnalazione" onsubmit="inviaForm(event)" style="background: #252526; padding: 20px; border-radius: 8px; color: #fff;">

    <!-- Categoria Principale -->
    <div style="margin-bottom: 15px;">
      <label for="categoria-principale"><strong>Categoria Principale (Obbligatorio):</strong></label><br>
      <select id="categoria-principale" onchange="onCategoriaChange()" required style="width: 100%; padding: 10px; margin-top: 5px; background: #333; color: #fff; border: 1px solid #555; border-radius: 4px;">
        <option value="">Caricamento categorie in corso...</option>
      </select>
    </div>
    
    <!-- Sotto-Categoria -->
    <div style="margin-bottom: 15px;">
      <label for="sotto-categoria"><strong>Sotto-Categoria (Obbligatorio):</strong></label><br>
      <select id="sotto-categoria" onchange="onSottoCategoriaChange()" required style="width: 100%; padding: 10px; margin-top: 5px; background: #333; color: #fff; border: 1px solid #555; border-radius: 4px;">
        <option value="">-- Seleziona prima Categoria Principale --</option>
      </select>
    </div>
    
    <!-- Contenuto / Lista Specifica -->
    <div style="margin-bottom: 15px;">
      <label for="contenuto-lista"><strong>Contenuto / Lista Specifica (Obbligatorio):</strong></label><br>
      <select id="contenuto-lista" name="contenuto" required style="width: 100%; padding: 10px; margin-top: 5px; background: #333; color: #fff; border: 1px solid #555; border-radius: 4px;">
        <option value="">-- Seleziona prima Sotto-Categoria --</option>
      </select>
    </div>
    
    <!-- Tipo di Problema -->
    <div style="margin-bottom: 15px;">
      <label for="problema"><strong>Tipo di Problema (Obbligatorio):</strong></label><br>
      <select id="problema" name="problema" required style="width: 100%; padding: 10px; margin-top: 5px; background: #333; color: #fff; border: 1px solid #555; border-radius: 4px;">
        <option value="INTERA sezione offline (NON singolo link)" selected>
          INTERA sezione offline (NON singolo link)
        </option>
      </select>
    </div>
    
    <!-- Piattaforma -->
    <div style="margin-bottom: 15px;">
      <label for="piattaforma"><strong>Dispositivo / Piattaforma (Obbligatorio):</strong></label><br>
      <select id="piattaforma" name="piattaforma" required style="width: 100%; padding: 10px; margin-top: 5px; background: #333; color: #fff; border: 1px solid #555; border-radius: 4px;">
        <option value="">-- Seleziona Dispositivo --</option>
        <option value="Android TV / Kodi">Android TV / Kodi</option>
        <option value="Fire TV Stick / Kodi">Fire TV Stick / Kodi</option>
        <option value="PC Windows / Linux / Kodi">PC Windows / Linux / Kodi</option>
        <option value="Smartphone / Tablet Android">Smartphone / Tablet Android</option>
        <option value="Altro">Altro</option>
      </select>
    </div>
    
    <!-- Checkbox di Consapevolezza -->
    <div style="margin-bottom: 20px; background: #3a2e12; border: 1px solid #ffa000; padding: 12px; border-radius: 6px;">
      <label style="cursor: pointer; display: flex; align-items: flex-start; gap: 10px;">
        <input type="checkbox" id="check-conferma" required style="margin-top: 3px; transform: scale(1.2);">
        <span><strong>Confermo:</strong> La segnalazione riguarda l'<strong>INTERA sezione o lista</strong> non funzionante e non un singolo canale/link temporaneamente offline.</span>
      </label>
    </div>
    
    <!-- Pulsante Invio e Messaggio Stato -->
    <button type="submit" id="btn-invia" style="width: 100%; padding: 12px; background: #107c41; color: white; border: none; border-radius: 4px; font-weight: bold; cursor: pointer; font-size: 16px;">Invia Segnalazione</button>
    
    <div id="messaggio-stato" style="margin-top: 15px; padding: 10px; border-radius: 4px; display: none; text-align: center;"></div>
  </form>

</div>

<script>
  var SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxBf2aK5ILmULSlcuuGR6K47vsuJbdwj1b1jEtBwl8qMEzXCZRr0QKG5wc4ZAoVnj4/exec";
  var rawMenuData = {};

  function initPage() {
    loadReports();
    loadMenu();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initPage);
  } else {
    initPage();
  }

  function loadReports() {
    var tbody = document.getElementById('tabella-segnalazioni');
    if (!tbody) return;

    fetch(SCRIPT_URL + "?action=getOpen", { method: "GET", redirect: "follow" })
      .then(function(res) { return res.json(); })
      .then(function(data) {
        tbody.innerHTML = '';
        if (!data || data.length === 0) {
          tbody.innerHTML = '<tr><td colspan="5" style="padding: 15px; text-align: center;">Nessuna segnalazione attiva al momento.</td></tr>';
          return;
        }
        data.forEach(function(item) {
          tbody.innerHTML += '<tr style="border-bottom: 1px solid #333;">' +
            '<td style="padding: 10px;">' + (item.data || '') + '</td>' +
            '<td style="padding: 10px;"><span style="background: #444; padding: 3px 8px; border-radius: 4px;">' + (item.sezione || '') + '</span></td>' +
            '<td style="padding: 10px;"><strong>' + (item.contenuto || '') + '</strong></td>' +
            '<td style="padding: 10px;">' + (item.problema || '') + '</td>' +
            '<td style="padding: 10px;"><span style="background: #ff9800; color: #000; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 12px;">' + (item.stato || '') + '</span></td>' +
          '</tr>';
        });
      })
      .catch(function(err) { console.error("Errore tabella:", err); });
  }

  function loadMenu() {
    fetch(SCRIPT_URL + "?action=getMenu", { method: "GET", redirect: "follow" })
      .then(function(res) { return res.json(); })
      .then(function(data) {
        rawMenuData = data;
        popolaCategoriePrincipali();
      })
      .catch(function(err) { console.error("Errore recupero menu:", err); });
  }

  function popolaCategoriePrincipali() {
    var mainSelect = document.getElementById("categoria-principale");
    if (!mainSelect) return;

    mainSelect.innerHTML = '<option value="">-- Seleziona Categoria --</option>';
    
    var categorie = [
      { key: "SPORT", label: "SPORT" },
      { key: "LIVE", label: "LIVE" },
      { key: "ONDEMAND", label: "ONDEMAND" },
      { key: "RADIO", label: "RADIO" }
    ];
    
    categorie.forEach(function(cat) {
      var opt = document.createElement("option");
      opt.value = cat.key;
      opt.textContent = cat.label;
      mainSelect.appendChild(opt);
    });
  }

  function onCategoriaChange() {
    var mainSelect = document.getElementById("categoria-principale");
    var subSelect = document.getElementById("sotto-categoria");
    var contentSelect = document.getElementById("contenuto-lista");

    if (!mainSelect || !subSelect || !contentSelect) return;
    
    var catValue = mainSelect.value;
    subSelect.innerHTML = '<option value="">-- Seleziona Sotto-Categoria --</option>';
    contentSelect.innerHTML = '<option value="">-- Seleziona Contenuto --</option>';
    
    if (!catValue) return;
    
    if (catValue === "SPORT") {
      var sportOptions = [
        { value: "C", label: rawMenuData["B"] ? rawMenuData["B"][0] : "Liste Eventi" },
        { value: "E", label: rawMenuData["D"] ? rawMenuData["D"][0] : "Liste Canali" },
        { value: "F", label: "Roja Tube" },
        { value: "H", label: rawMenuData["G"] ? rawMenuData["G"][0] : "Sport Replay" }
      ];
    
      sportOptions.forEach(function(item) {
        var opt = document.createElement("option");
        opt.value = item.value;
        opt.textContent = item.label;
        subSelect.appendChild(opt);
      });
    
    } else if (catValue === "LIVE") {
      var listJ = rawMenuData["J"] || rawMenuData["B1"] || [];
      listJ.forEach(function(item) {
        var opt = document.createElement("option");
        opt.value = item;
        opt.textContent = item;
        subSelect.appendChild(opt);
      });
    
    } else if (catValue === "ONDEMAND") {
      var listL = rawMenuData["L"] || rawMenuData["C1"] || [];
      listL.forEach(function(item) {
        var opt = document.createElement("option");
        opt.value = item;
        opt.textContent = item;
        subSelect.appendChild(opt);
      });
    
    } else if (catValue === "RADIO") {
      var opt = document.createElement("option");
      opt.value = "Generale";
      opt.textContent = "Generale";
      opt.selected = true;
      subSelect.appendChild(opt);
      onSottoCategoriaChange();
    }
  }

  function onSottoCategoriaChange() {
    var mainSelect = document.getElementById("categoria-principale");
    var subSelect = document.getElementById("sotto-categoria");
    var contentSelect = document.getElementById("contenuto-lista");

    if (!mainSelect || !subSelect || !contentSelect) return;
    
    var catValue = mainSelect.value;
    var subValue = subSelect.value;
    var subText = subSelect.options[subSelect.selectedIndex] ? subSelect.options[subSelect.selectedIndex].text : "";
    
    contentSelect.innerHTML = '<option value="">-- Seleziona Contenuto --</option>';
    
    if (!subValue) return;
    
    if (catValue === "SPORT") {
      if (subValue === "F") {
        var opt = document.createElement("option");
        opt.value = "Roja Tube";
        opt.textContent = "Roja Tube";
        opt.selected = true;
        contentSelect.appendChild(opt);
      } else {
        var items = rawMenuData[subValue] || [];
        items.forEach(function(item) {
          var opt = document.createElement("option");
          opt.value = item;
          opt.textContent = item;
          contentSelect.appendChild(opt);
        });
      }
    } else if (catValue === "LIVE" || catValue === "ONDEMAND") {
      var opt = document.createElement("option");
      opt.value = subText;
      opt.textContent = subText;
      opt.selected = true;
      contentSelect.appendChild(opt);
    
    } else if (catValue === "RADIO") {
      var radioItems = rawMenuData["N"] || rawMenuData["D"] || [];
      radioItems.forEach(function(item) {
        if (item.toUpperCase() !== "RADIO") {
          var opt = document.createElement("option");
          opt.value = item;
          opt.textContent = item;
          contentSelect.appendChild(opt);
        }
      });
    }
  }

  function inviaForm(e) {
    e.preventDefault();
    var btn = document.getElementById("btn-invia");
    var msg = document.getElementById("messaggio-stato");
    var mainSelect = document.getElementById("categoria-principale");
    var subSelect = document.getElementById("sotto-categoria");
    
    var catMainText = mainSelect.options[mainSelect.selectedIndex].text;
    var subCatText = subSelect.options[subSelect.selectedIndex].text;
    var contenutoVal = document.getElementById("contenuto-lista").value;
    var problemaVal = document.getElementById("problema").value;
    var piattaformaVal = document.getElementById("piattaforma").value;
    
    var sezioneCompleta = catMainText + " > " + subCatText;
    
    var payload = {
      sezione: sezioneCompleta,
      contenuto: contenutoVal,
      problema: problemaVal,
      piattaforma: piattaformaVal
    };
    
    btn.disabled = true;
    btn.textContent = "Invio in corso...";
    msg.style.display = "none";
    
    fetch(SCRIPT_URL, {
      method: "POST",
      redirect: "follow",
      headers: { "Content-Type": "text/plain;charset=utf-8" },
      body: JSON.stringify(payload)
    })
    .then(function(res) { return res.json(); })
    .then(function(data) {
      btn.disabled = false;
      btn.textContent = "Invia Segnalazione";
      msg.style.display = "block";
    
      if (data.result === "success") {
        msg.style.background = "#1b5e20";
        msg.style.color = "#fff";
        msg.innerHTML = "✅ Segnalazione inviata con successo!";
        document.getElementById("form-segnalazione").reset();
        onCategoriaChange();
        loadReports();
      } else if (data.result === "duplicate") {
        msg.style.background = "#b71c1c";
        msg.style.color = "#fff";
        msg.innerHTML = "⚠️ Attenzione: Risulta già una segnalazione attiva per questo contenuto.";
      } else {
        msg.style.background = "#b71c1c";
        msg.style.color = "#fff";
        msg.innerHTML = "❌ Si è verificato un errore durante l'invio.";
      }
    })
    .catch(function(err) {
      btn.disabled = false;
      btn.textContent = "Invia Segnalazione";
      msg.style.display = "block";
      msg.style.background = "#b71c1c";
      msg.style.color = "#fff";
      msg.innerHTML = "❌ Errore di connessione al server.";
    });
  }
</script>