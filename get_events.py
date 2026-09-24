import os
import json
import requests
from datetime import datetime

# API originale da cui DaddyLive scarica la lista degli eventi in tempo reale
SCHEDULE_API = "https://daddylive.app/api/stream/schedule.php"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://daddylive.app/"
}

def fetch_events_from_api():
    extracted_events = []
    
    try:
        response = requests.get(SCHEDULE_API, headers=HEADERS, timeout=15)
        if response.status_code == 200:
            data = response.json()
            
            # L'API restituisce i dati organizzati per giornate/categorie
            # Struttura tipica: {"data": [{"category": "Motorsport", "events": [...]}]}
            for category_block in data if isinstance(data, list) else data.get("data", []):
                events_list = category_block.get("events", []) if isinstance(category_block, dict) else []
                
                for event in events_list:
                    title = event.get("event", "") or event.get("title", "")
                    title_upper = title.upper()
                    
                    # Filtra solo F1 e MotoGP
                    is_f1 = "F1" in title_upper or "FORMULA 1" in title_upper or "FORMULA1" in title_upper
                    is_motogp = "MOTOGP" in title_upper or "MOTO GP" in title_upper or "MOTO2" in title_upper or "MOTO3" in title_upper
                    
                    if is_f1 or is_motogp:
                        cat_label = "F1" if is_f1 else "MotoGP"
                        
                        # Estrazione dei canali associati (es. Sky Sport F1, Ch-12, ecc.)
                        channels = []
                        for ch in event.get("channels", []):
                            ch_name = ch.get("channel_name", "") or ch.get("name", "")
                            ch_id = ch.get("channel_id", "")
                            if ch_name:
                                channels.append(ch_name)
                            elif ch_id:
                                channels.append(f"Channel {ch_id}")
                        
                        channel_str = " | Canali: " + ", ".join(channels) if channels else ""
                        time_str = event.get("time", "")
                        
                        extracted_events.append({
                            "category": cat_label,
                            "time": time_str,
                            "title": title,
                            "channels": channels,
                            "event": f"{time_str} - {title}{channel_str}".strip(" -"),
                            "updated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
                        })

    except Exception as e:
        print(f"Errore durante la chiamata all'API Schedule: {e}")

    # Fallback se la schedule.php è momentaneamente offline: usa l'endpoint epg generale
    if not extracted_events:
        try:
            epg_res = requests.get("https://daddylive.app/api/stream/epg.php", headers=HEADERS, timeout=15)
            if epg_res.status_code == 200:
                epg_data = epg_res.json()
                for ch in epg_data:
                    ch_name = str(ch.get("channel_name", "")).upper()
                    if "F1" in ch_name or "MOTOGP" in ch_name:
                        cat = "F1" if "F1" in ch_name else "MotoGP"
                        extracted_events.append({
                            "category": cat,
                            "time": "Live",
                            "title": ch_name,
                            "channels": [ch_name],
                            "event": f"Diretta - {ch_name}",
                            "updated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
                        })
        except Exception as e:
            print(f"Errore Fallback EPG: {e}")

    return extracted_events

if __name__ == "__main__":
    events = fetch_events_from_api()
    
    # Salva il file JSON nella ROOT
    with open("events.json", "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=2)

    # Salva copia anche dentro docs/calendario/ se esiste la cartella
    target_dir = os.path.join("docs", "calendario")
    if os.path.exists(target_dir):
        with open(os.path.join(target_dir, "events.json"), "w", encoding="utf-8") as f:
            json.dump(events, f, ensure_ascii=False, indent=2)

    print(f"Trovati ed estratti {len(events)} eventi reali.")
