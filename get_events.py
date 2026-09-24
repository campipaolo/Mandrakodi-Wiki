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

# Parole chiave da ignorare (menu, header, elementi statici)
IGNORE_KEYWORDS = [
    "home", "channels list", "18 plus", "embed api", "movies", 
    "live sports categories", "soccer", "cricket", "nba", "nfl", 
    "tennis", "formula 1", "motogp", "mlb", "boxing", "ufc"
]

def clean_text(text):
    return " ".join(text.split())

def is_valid_event(text):
    text_lower = text.lower()
    # Scarta se è un elemento del menu
    for ignore in IGNORE_KEYWORDS:
        if text_lower == ignore or text_lower.startswith("⚽") or text_lower.startswith("☰"):
            return False
    # Accetta solo se contiene informazioni reali (es. orari, canali o nomi di gare/sessioni)
    return len(text) > 8

def fetch_events():
    events = []

    for category, url in URLS.items():
        try:
            res = requests.get(url, headers=HEADERS, timeout=10)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                # Cerca le righe della tabella dei palinsesti o i blocchi contenenti i link ai canali
                rows = soup.select('table tr, .event-item, .schedule-item')
                
                if rows:
                    for row in rows:
                        text = clean_text(row.get_text())
                        if is_valid_event(text):
                            events.append({
                                "category": category,
                                "event": text,
                                "url": url,
                                "updated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
                            })
                else:
                    # Fallback se non ci sono tabelle: estrae solo i paragrafi o link con canali/orari
                    for item in soup.find_all(['tr', 'p', 'a']):
                        text = clean_text(item.get_text())
                        if is_valid_event(text) and any(c in text.lower() for c in ['ch', 'sky', 'channel', 'stream', '00:', '11:', '12:', '13:', '14:', '15:', '16:', '17:', '18:', '19:', '20:', '21:']):
                            events.append({
                                "category": category,
                                "event": text,
                                "url": url,
                                "updated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
                            })

        except Exception as e:
            print(f"Errore su {category}: {e}")

    # Rimuove eventuali duplicati mantenendo l'ordine
    unique_events = []
    seen = set()
    for ev in events:
        if ev['event'] not in seen:
            seen.add(ev['event'])
            unique_events.append(ev)

    return unique_events

if __name__ == "__main__":
    data = fetch_events()
    
    # Salva nella root
    with open("events.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Salva anche in docs/calendario/ se esiste la cartella
    target_dir = os.path.join("docs", "calendario")
    if os.path.exists(target_dir):
        with open(os.path.join(target_dir, "events.json"), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    print(f"Estratti {len(data)} eventi validi.")
