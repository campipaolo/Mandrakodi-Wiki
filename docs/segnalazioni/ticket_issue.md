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

<!-- RICHIAMO DELLO SCRIPT ESTERNO -->
<script src="script_ticket.js"></script>