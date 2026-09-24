import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

URLS = {
    "F1": "https://daddylive.app/formula1",
    "MotoGP": "https://daddylive.app/motogp"
}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

all_events = []

for category, url in URLS.items():
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Cerca le righe o i blocchi contenenti eventi e canali
            # (Adatta i selettori CSS in base alla struttura HTML esatta della pagina)
            for item in soup.select('div.event, tr, li'):
                text = item.get_text(strip=True)
                if text and len(text) > 5:
                    all_events.append({
                        "category": category,
                        "raw_event": text,
                        "url": url,
                        "updated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
                    })
    except Exception as e:
        print(f"Errore durante l'estrazione da {category}: {e}")

# Salva i dati estratti nel file JSON
with output_file = open("events.json", "w", encoding="utf-8"):
    json.dump(all_events, output_file, ensure_ascii=False, indent=2)

print(f"Salvati {len(all_events)} eventi in events.json")
