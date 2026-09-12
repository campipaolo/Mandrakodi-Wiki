var menuData = {}; // Conterrà la mappa inviata da Apps Script

// 1. Carica la struttura dei menu al caricamento della pagina
function loadMenu() {
  fetch(SCRIPT_URL + "?action=getMenu", { method: "GET", redirect: "follow" })
    .then(function(res) { return res.json(); })
    .then(function(data) {
      menuData = data;
      popolaCategoriePrincipali();
    })
    .catch(function(err) {
      console.error("Errore caricamento menu:", err);
    });
}

// 2. Popola il primo menu: Categoria Principale
function popolaCategoriePrincipali() {
  var catSelect = document.getElementById("categoria-principale");
  catSelect.innerHTML = '<option value="">-- Seleziona Categoria --</option>';

  // Mappa delle Categorie Principali in base alle intestazioni del foglio
  var categorie = [
    { label: menuData["A"] ? menuData["A"][0] : "SPORT", key: "A" },
    { label: menuData["I"] ? menuData["I"][0] : "LIVE", key: "I" },
    { label: menuData["K"] ? menuData["K"][0] : "ONDEMAND", key: "K" },
    { label: menuData["M"] ? menuData["M"][0] : "RADIO", key: "M" }
  ];

  categorie.forEach(function(cat) {
    if (cat.label) {
      var opt = document.createElement("option");
      opt.value = cat.key;
      opt.textContent = cat.label;
      catSelect.appendChild(opt);
    }
  });
}

// 3. Gestore cambio Categoria Principale -> Popola Sotto-Categoria
function onCategoriaChange() {
  var catKey = document.getElementById("categoria-principale").value;
  var subSelect = document.getElementById("sotto-categoria");
  var contentSelect = document.getElementById("contenuto-lista");

  subSelect.innerHTML = '<option value="">-- Seleziona Sotto-Categoria --</option>';
  contentSelect.innerHTML = '<option value="">-- Seleziona Contenuto --</option>';

  if (!catKey) return;

  if (catKey === "A") {
    // SPORT: ha 4 sotto-categorie (A1, A2, A3, A4)
    var subSport = [
      { code: "A1", label: menuData["B"] ? menuData["B"][0] : "Liste Eventi" },
      { code: "A2", label: menuData["D"] ? menuData["D"][0] : "Liste Canali" },
      { code: "A3", label: menuData["F"] ? menuData["F"][0] : "Roja Tube" },
      { code: "A4", label: menuData["G"] ? menuData["G"][0] : "Sport Replay" }
    ];
    subSport.forEach(function(item) {
      if (item.label) {
        var opt = document.createElement("option");
        opt.value = item.code;
        opt.textContent = item.label;
        subSelect.appendChild(opt);
      }
    });
  } else if (catKey === "I") {
    // LIVE: le sotto-categorie sono in B1 (Colonna J)
    var itemsB1 = menuData["B1"] || [];
    itemsB1.forEach(function(item) {
      var opt = document.createElement("option");
      opt.value = "B1:" + item;
      opt.textContent = item;
      subSelect.appendChild(opt);
    });
  } else if (catKey === "K") {
    // ONDEMAND: le sotto-categorie sono in C1 (Colonna L)
    var itemsC1 = menuData["C1"] || [];
    itemsC1.forEach(function(item) {
      var opt = document.createElement("option");
      opt.value = "C1:" + item;
      opt.textContent = item;
      subSelect.appendChild(opt);
    });
  } else if (catKey === "M") {
    // RADIO: non ha sotto-categorie, seleziona in automatico Generale
    var opt = document.createElement("option");
    opt.value = "M_GEN";
    opt.textContent = "Generale";
    opt.selected = true;
    subSelect.appendChild(opt);
    onSottoCategoriaChange(); // Popola direttamente i contenuti
  }
}

// 4. Gestore cambio Sotto-Categoria -> Popola Contenuto / Lista Specifica
function onSottoCategoriaChange() {
  var catKey = document.getElementById("categoria-principale").value;
  var subValue = document.getElementById("sotto-categoria").value;
  var contentSelect = document.getElementById("contenuto-lista");

  contentSelect.innerHTML = '<option value="">-- Seleziona Contenuto --</option>';

  if (!subValue) return;

  var list = [];

  if (subValue === "A1") {
    list = menuData["C"] || []; // Colonna C (A1A - Liste Eventi)
  } else if (subValue === "A2") {
    list = menuData["E"] || []; // Colonna E (A2A - Liste Canali)
  } else if (subValue === "A3") {
    list = ["Roja Tube"]; // Selezione singola
  } else if (subValue === "A4") {
    list = menuData["H"] || []; // Colonna H (A4A - Sport Replay)
  } else if (subValue.indexOf("B1:") === 0 || subValue.indexOf("C1:") === 0) {
    // Per LIVE e ONDEMAND la sotto-categoria è già lo specifico canale/sezione
    list = [subValue.split(":")[1]];
  } else if (catKey === "M") {
    list = menuData["M"] ? menuData["M"].slice(1) : []; // Colonna Radio
  }

  list.forEach(function(item) {
    var opt = document.createElement("option");
    opt.value = item;
    opt.textContent = item;
    contentSelect.appendChild(opt);
  });

  // Se c'è solo un elemento, selezionalo automaticamente
  if (list.length === 1) {
    contentSelect.selectedIndex = 1;
  }
}

// Inizializza i menu all'apertura
document.addEventListener("DOMContentLoaded", loadMenu);