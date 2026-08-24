[:material-book-open-page-variant: Torna alle Guide](../guide/tutorials.md){ .md-button .md-button--primary }  [:material-home: Torna alla Home](../index.md){.md-button .md-button--primary} [:material-face-agent: Assistenza](../ask_help.md){ .md-button .md-button--primary }

------

!!! tip "Links "WARP""
    I links con dicitura "**WARP**" richiedono l'utilizzo dei seguenti  Software/App  <br>    - **Warp** (Windows/macOS/Linux/Android/iOS) *[si installa da qui](https://one.one.one.one)*, **non richiede** alcuna configurazione <br>    - **Amnezia Vpn** (AndroidTv/Firestick) una volta installato **necessita** del file ".conf" per funzionare correttamente 

!!! warning "Attenzione"
    File ".conf" è utilizzabile su *più dispositivi contemporaneamente* da stessa rete e tra reti diverse <br> **Sconsigliamo** di **condividere** il proprio file .conf **con più utenti**, ad esagerare finisce che Cloudlfare poi impone un   file diverso per ogni dispositivo e pure per ogni tipologia di rete....

------

!!! important "Fase 1 - creare file configurazione per Amnesia Vpn"
    Creare file ".conf" (**senza scadenza**) da utilizzare in Amnesia Vpn su AndroidTv/Firestick

??? info "Sito Config Generator"
       **Generare file ".conf" senza scadenza**

    **N.B.: qualora app "Dowloader" non funzionasse, usare smartphone/tablet/pc<br>
      Il file scaricato poi si invia a AndroidTv/Firestick seguendo i passaggi della "Fase 3"**<br>
      
    * [Config Generator](https://warp-generator.vercel.app)<br>
      (c'è scritto "WARP" ma va bene ugualmente)
    * Premere il pulsante "Generate"
    * Premere il pulsante "Download Config"
    * N.B.: verificare che il file salvato abbia l'estensione "**.conf**" (se necessario **rinominarlo**)

------

!!! important "Fase 2 - Amnezia Vpn"
    **Apk per AndroidTv/Firestick** 

??? info "Amnezia Vpn"
    **AndroidTv/Firestick**

    **N.B.: qualora app "Dowloader" non funzionasse, usare smartphone/tablet/pc<br>
      Il file scaricato poi si invia a AndroidTv/Firestick seguendo i passaggi della "Fase 3"**<br>
      
    * [AndroidTv/Firestick](https://github.com/amnezia-vpn/amneziawg-android/releases/latest): Scaricare "AmneziaWG-x.x.xxxxxxxxx.apk"

------

!!! important "Fase 3 - Localsend"
    **Inviare** a AndroidTv/Firestick file ".conf" e Apk Amnezia Vpn

??? info "Localsend"
    **Windows/macOS/Linux/Android/AndroidTv/iOS/Firestick**

    * Installare "Localsend" su entrambi i dispositivi "mittente" e "ricevente"
    * [Loalsend Windows/macOS/Linux/Android/AndroidTv/iOS](https://localsend.org/it/download)
    * Utenti **Firestick**: provare una o più fonti<br>
    [F-Droid](https://f-droid.org/packages/org.localsend.localsend_app/): scaricare apk versione "armeabi-v7a"<br>
    [Github](https://github.com/localsend/localsend/releases): scaricare apk "LocalSend-x.xx.x-android-arm32v7.apk"<br>
    * Avviare Localsend **prima** sul dispositivo "ricevente" e **poi** su quello "mittente"
    * Sul dispositivo "mittente" premere "Invia" e poi "File" 
    * Selezionare files da inviare
    * Selezionare dispositivo "ricevente"
    * Sul dispositivo "ricevente" dare conferma per ricevere  
    * N.B.: la cartella "**Download**" è quella di default per la ricezione dei files
    * Sul dispositivo "ricevente" in alto a destra l'icona a fianco alla “i” elenca la cronologia

------

!!! important "Fase 4 - Installare Amnezia Vpn  su  AndroidTv/Firestick"
    **Installazione** Apk Amnezia Vpn su **AndroidTv/Firestick**

??? info "Amnezia Vpn  per AndroidTv/Firestick"
    **AndroidTv/Firestick**


    **N.B.: chi ha scaricato apk con Downloader, ha già installato l'app, diversamente l'apk è presente nella cartella "Download"**<br> 
    
    * In "Localsend" sul dispositivo "ricevente" in alto a destra l'icona a fianco alla “**i**” elenca la cronologia dei file ricevuti
    * Cliccare apk Amnezia Vpn 
    * Consentire installazione delle app da Localsend (se richiesto) e installarlo
    * Alla prima apertura, Amnezia Vpn potrebbe chiedere il permesso di accedere ai file
    * Concedere l'autorizzazione, se non appare richiesta, uscire e rientrare

------

!!! important " Fase 5 - Configurare Amnezia Vpn"
    **Impostare** Amnezia Vpn su AndroidTv/Firestick

??? info "Amnezia Vpn"
    **AndroidTv/Firestick**


    * Aprire Amnezia Vpn, premere il pulsante "+", poi "File with connection settings"
    * Importare il file ".conf", sarà quindi presente nella schermata principale
    * Cliccare l'interruttore "Connect" per attivare/disattivare
    * Al primo avvio verrà chiesta conferma di attivazione
    * N.B.: qualora non fosse possibile selezionare il file ".conf" durante l'importazione, installare dallo Store **file manager** come "x-plore " o simili

