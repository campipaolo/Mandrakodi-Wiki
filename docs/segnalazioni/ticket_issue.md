<script>
  var SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxBf2aK5ILmULSlcuuGR6K47vsuJbdwj1b1jEtBwl8qMEzXCZRr0QKG5wc4ZAoVnj4/exec";

  var rawMenuData = {};

  document.addEventListener("DOMContentLoaded", function() {
    loadReports();
    loadMenu();
  });

  function loadReports() {
    fetch(SCRIPT_URL + "?action=getOpen", { method: "GET", redirect: "follow" })
      .then(function(res) { return res.json(); })
      .then(function(data) {
        var tbody = document.getElementById('tabella-segnalazioni');
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

  // GESTIONE CATEGORIA PRINCIPALE
  function onCategoriaChange() {
    var catValue = document.getElementById("categoria-principale").value;
    var subSelect = document.getElementById("sotto-categoria");
    var contentSelect = document.getElementById("contenuto-lista");

    subSelect.innerHTML = '<option value="">-- Seleziona Sotto-Categoria --</option>';
    contentSelect.innerHTML = '<option value="">-- Seleziona Contenuto --</option>';
    
    if (!catValue) return;
    
    if (catValue === "SPORT") {
      // Sport legge SOLO le sotto-categorie reali B, D, F, G dal tuo foglio
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
      // LIVE legge la colonna J (B1)
      var listJ = rawMenuData["J"] || rawMenuData["B1"] || [];
      listJ.forEach(function(item) {
        var opt = document.createElement("option");
        opt.value = item;
        opt.textContent = item;
        subSelect.appendChild(opt);
      });
    
    } else if (catValue === "ONDEMAND") {
      // ONDEMAND legge la colonna L (C1)
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

  // GESTIONE SOTTO-CATEGORIA E POPOLAMENTO CONTENUTO
  function onSottoCategoriaChange() {
    var catValue = document.getElementById("categoria-principale").value;
    var subSelect = document.getElementById("sotto-categoria");
    var subValue = subSelect.value;
    var subText = subSelect.options[subSelect.selectedIndex] ? subSelect.options[subSelect.selectedIndex].text : "";
    var contentSelect = document.getElementById("contenuto-lista");

    contentSelect.innerHTML = '<option value="">-- Seleziona Contenuto --</option>';
    
    if (!subValue) return;
    
    if (catValue === "SPORT") {
      if (subValue === "F") { // Roja Tube
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
      // Per LIVE e ONDEMAND il contenuto coincide esattamente con la sotto-categoria (es. Ita Epg)
      // Si autocompila senza mostrare doppioni!
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
    
    var catMainText = document.getElementById("categoria-principale").options[document.getElementById("categoria-principale").selectedIndex].text;
    var subCatText = document.getElementById("sotto-categoria").options[document.getElementById("sotto-categoria").selectedIndex].text;
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