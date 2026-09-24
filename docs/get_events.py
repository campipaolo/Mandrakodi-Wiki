import os
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

URLS = {
    "F1": "https://daddylive.app/formula1",
    "MotoGP": "https://daddylive.app/motogp"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_events():
    events = []
    
    # 1. Scraping diretto dalle pagine F1 e MotoGP
    for category, url in URLS.items():
        try:
            res = requests.get(url, headers=HEADERS, timeout=10)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                # Estrae le righe di testo contenenti eventi/canali
                for element in soup.find_all(['p', 'div', 'li', 'tr']):
                    text = element.get_text(strip=True)
                    if any(kw in text.lower() for kw in ['f1', 'formula', 'motogp', 'ch2', 'ch1', 'sky', 'channel']):
                        if len(text) > 10 and len(text) < 200:
                            events.append({
                                "category": category,
                                "event": text,
                                "url": url,
                                "updated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
                            })
        except Exception as e:
            print(f"Errore su {category}: {e}")

    # Fallback API in caso di pagina vuota
    if not events:
        try:
            api_res = requests.get("https://daddylive.app/api/stream/epg.php", headers=HEADERS, timeout=10)
            if api_res.status_code == 200:
                data = api_res.json()
                for item in data:
                    name = str(item.get("channel_name", "")).upper()
                    if "F1" in name or "MOTOGP" in name:
                        events.append({
                            "category": "F1" if "F1" in name else "MotoGP",
                            "event": f"{name} - {item.get('title', 'Evento in diretta')}",
                            "url": "https://daddylive.app",
                            "updated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
                        })
        except Exception as e:
            print(f"Errore API fallback: {e}")

    return events

if __name__ == "__main__":
    data = fetch_events()
    
    # Salva il file nella root
    with open("events.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Salvato events.json nella root.")

    # Salva una copia direttamente dentro docs/calendario/ per evitare qualsiasi errore 404
    target_dir = os.path.join("docs", "calendario")
    if os.path.exists(target_dir):
        with open(os.path.join(target_dir, "events.json"), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Salvato events.json anche in docs/calendario/.")
