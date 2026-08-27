[:material-book-open-page-variant: Torna alle Guide](../guide/tutorials.md){ .md-button .md-button--primary }  [:material-home: Torna alla Home](../index.md){.md-button .md-button--primary} [:material-face-agent: Assistenza](../ask_help.md){ .md-button .md-button--primary }

------

!!! tip "WARP"
    I links con dicitura "**WARP**" *esigono* l'utilizzo dei seguenti  Software/App  <br>    - **Warp** (Windows/macOS/Linux/Android/iOS) *[si installa da qui](https://one.one.one.one)*, **non richiede** alcuna configurazione<br>    - **Wireguard** (*AndroidTv/Firestick*) una volta installato **necessita** del file ".conf" per funzionare correttamente 

!!! warning "Attenzione"
    File ".conf" è utilizzabile su *più dispositivi contemporaneamente* da stessa rete e tra reti diverse <br> **Sconsigliamo** di **condividere** il proprio file .conf **con più utenti**, ad esagerare finisce che Cloudlfare poi impone un   file diverso per ogni dispositivo e pure per ogni tipologia di rete....

------

!!! important "Fase 1 - creare file configurazione per Wireguard"
    Creare file ".conf" **senza scadenza** da utilizzare in Wireguard su AndroidTv/Firestick

??? info "Web Config Generator + Web Convertitore per Wireguard"
       **Generare file ".conf" senza scadenza**

    * <a href="https://warp-generator.vercel.app" target="_blank">Config Generator</a>
    * Premere il pulsante "Generate" per generare la configurazione
    * Premere il pulsante "Copy" per copiare negli appunti la configurazione
    * <a href="https://campipaolo.github.io/Mandrakodi-Wiki/guide/converter.html" target="_blank">Convertitore per Wireguard</a>
    * Nel box di testo "Input" incollare la configurazione
    * Premere il pulsante "Converti" per generare configurazione nel box di testo "Ouput"
    * Premere il pulsante "Scarica file" per salvare file ".conf"
    * N.B.: verificare che il file "wireguard" salvato abbia l'estensione "**.conf**" (se diversa, **rinominare** correggendo)

------

!!! important "Fase 2 - Wireguard per AdroidTv/Firestick"
    Apk per **AndroidTv/Firestick** 

??? info "Wireguard"
    **AndroidTv/Firestick**

    * <a href="https://download.wireguard.com/android-client/" target="_blank">Wireguard</a>
    * AndroidTv: installare con link "Google Play Store"
    * Firestick: scaricare apk "com.wireguard.android-x.x.xxxxxxxx.apk"

------

!!! important "Fase 3 - Localsend"
    **Inviare** a AndroidTv/Firestick file ".conf" ed eventuale Apk Firestick

??? info "Localsend"
    **Windows/macOS/Linux/Android/AndroidTv/iOS/Firestick**

    **N.B.: Sito supporta app "Downloader" per scaricare Apk**<br>
    
    * Installare "Localsend" su entrambi i dispositivi "mittente" e "ricevente"
    * <a href="https://localsend.org/it/download" target="_blank">Sito Web</a> Loalsend Windows/macOS/Linux/Android/AndroidTv/iOS<br>
    * Utenti **Firestick**: provare una o più fonti<br>
      <a href="https://f-droid.org/packages/org.localsend.localsend_app/" target="_blank"> F-Droid</a> scaricare apk "LocalSend-x.xx.x-android-arm32v7.apk"<br>
      <a href="https://github.com/localsend/localsend/releases/latest" target="_blank">Github</a> scaricare apk "LocalSend-x.xx.x-android-arm32v7.apk"<br>
    * Avviare Localsend **prima** sul dispositivo "ricevente" e **poi** su quello "mittente"
    * Sul dispositivo "mittente" premere "Invia" e poi "File" 
    * Selezionare files da inviare
    * Selezionare dispositivo "ricevente"
    * Sul dispositivo "ricevente" dare conferma per ricevere  
    * N.B.: la cartella "**Download**" è quella di default per la ricezione dei files
    * Sul dispositivo "ricevente" in alto a destra l'icona a fianco alla “i” elenca la cronologia

------

!!! important "Fase 4 - Installare Wireguard  su  AndroidTv/Firestick"
    **Installazione** Wireguard Vpn su **AndroidTv/Firestick**

??? info "Wireguard  per AndroidTv/Firestick"
    **AndroidTv/Firestick**


    **N.B.: chi ha scaricato apk con Downloader, ha già installato l'app, diversamente l'apk è presente nella cartella "Download"**<br> 
    
    * In "Localsend" sul dispositivo "ricevente" in alto a destra l'icona a fianco alla “**i**” elenca la cronologia dei file ricevuti
    * Cliccare apk Wireguard 
    * Consentire installazione delle app da Localsend (se richiesto) e installarlo
    * Alla prima apertura, Wireguard potrebbe chiedere il permesso di accedere ai file
    * Concedere l'autorizzazione, se non appare richiesta, uscire e rientrare

------

!!! important " Fase 5 - Configurare Wireguard"
    **Impostare** Wireguard su AndroidTv/Firestick

??? info "Wireguard"
    **AndroidTv/Firestick**


    * Aprire Wireguard, premere il pulsante "+", poi "Importa da file o archivio"
    * Importare il file ".conf", sarà quindi presente nella schermata principale
    * Cliccare l'interruttore in coorispondenza a destra per attivare/disattivare
    * Al primo avvio verrà chiesta conferma di attivazione
    * N.B.: qualora non fosse possibile selezionare il file ".conf" durante l'importazione, installare dallo Store **file manager** come "x-plore " o simili

