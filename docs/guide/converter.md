# Convertitore WireGuard

Incolla la tua configurazione per rimuovere i parametri Amnezia/WARP non supportati da WireGuard standard.

<div style="display: flex; flex-direction: column; gap: 15px; margin-top: 20px;">
  <div>
    <label for="fileInput"><strong>Carica un file .conf:</strong></label><br>
    <input type="file" id="fileInput" accept=".conf,.txt">
  </div>

  <div>
    <label for="inputConfig"><strong>Configurazione Input:</strong></label><br>
    <textarea id="inputConfig" style="width: 100%; height: 180px; font-family: monospace; padding: 8px; box-sizing: border-box;" placeholder="Incolla qui il contenuto del file .conf..."></textarea>
  </div>

  <div>
    <button onclick="cleanConfig()" style="background-color: #2da44e; color: white; border: none; padding: 10px 18px; border-radius: 6px; font-weight: bold; cursor: pointer;">Converti in WireGuard Standard</button>
  </div>

  <div>
    <label for="outputConfig"><strong>Configurazione Convertita:</strong></label><br>
    <textarea id="outputConfig" readonly style="width: 100%; height: 180px; font-family: monospace; padding: 8px; box-sizing: border-box;" placeholder="Il risultato apparirà qui..."></textarea>
  </div>

  <div>
    <button id="downloadBtn" onclick="downloadConf()" style="display: none; background-color: #0969da; color: white; border: none; padding: 10px 18px; border-radius: 6px; font-weight: bold; cursor: pointer;">Scarica wireguard.conf</button>
  </div>
</div>

<script>
  document.getElementById('fileInput').addEventListener('change', function(e) {
    const file = e.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = function(e) {
      document.getElementById('inputConfig').value = e.target.result;
    };
    reader.readAsText(file);
  });

  function cleanConfig() {
    const input = document.getElementById('inputConfig').value;
    const ignoredKeys = ['S1', 'S2', 'Jc', 'Jmin', 'Jmax', 'H1', 'H2', 'H3', 'H4'];
    const lines = input.split(/\r?\n/);
    const filteredLines = lines.filter(line => {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith('#') || trimmed.startsWith('[')) return true;
      const key = trimmed.split('=')[0].trim();
      return !ignoredKeys.includes(key);
    });
    const output = filteredLines.join('\n');
    document.getElementById('outputConfig').value = output;
    if (output.trim().length > 0) {
      document.getElementById('downloadBtn').style.display = 'inline-block';
    }
  }

  function downloadConf() {
    const text = document.getElementById('outputConfig').value;
    const blob = new Blob([text], { type: 'text/plain' });
    const anchor = document.createElement('a');
    anchor.download = 'wireguard.conf';
    anchor.href = window.URL.createObjectURL(blob);
    anchor.click();
    window.URL.revokeObjectURL(anchor.href);
  }
</script>