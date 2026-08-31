[:material-book-open-page-variant: Torna alle Guide](../guide/tutorials.md){ .md-button .md-button--primary }  [:material-home: Torna alla Home](../index.md){.md-button .md-button--primary} [:material-face-agent: Assistenza](../ask_help.md){ .md-button .md-button--primary }

------

!!! tip "WARP"
    I links con dicitura "**WARP**" *esigono* l'utilizzo dei seguenti  Software/App  <br>    - **Warp** è per *Pc Windows/macOS/Linux & Smartphone-Tablet Android/iOS*, **non richiede** alcuna configurazione <a href="https://one.one.one.one/" target="_blank">(*si installa da qui*)</a><br>    - **Wireguard** è per *Chiavette/Tv/Box/Firestick*, **necessita** del file ".conf" per funzionare correttamente (di seguito passaggi per configurazione e installazione) 

!!! warning "Attenzione"
    File ".conf" è utilizzabile su *più dispositivi contemporaneamente* da stessa rete e tra reti diverse <br> **Sconsigliamo** di **condividere** il proprio file .conf **con più utenti**, ad esagerare finisce che Cloudlfare poi impone un   file diverso per ogni dispositivo e pure per ogni tipologia di rete....

------

!!! important "Fase 1 - creare file configurazione per Wireguard"
    Creare file ".conf" **senza scadenza** da utilizzare in Wireguard su Chiavette/Tv/Box/Firestick

??? info "Web Config Generator + Web Convertitore per Wireguard"
       **Generare file ".conf" senza scadenza** (*non usare app Dowmloader*)

    * <a href="https://warp-generator.vercel.app" target="_blank">Config Generator</a>
    * Premere il pulsante "**Generate**" per generare la configurazione
    * Premere il pulsante "**Copy**" per copiare negli appunti la configurazione
    * <a href="https://campipaolo.github.io/Mandrakodi-Wiki/guide/converter.html" target="_blank">Convertitore per Wireguard</a>
    * Nel box di testo "Input" **incollare** la configurazione
    * Premere il pulsante "**Converti**" per generare configurazione nel box di testo "Ouput"
    * Premere il pulsante "**Scarica file**" per salvare file ".conf"
    * N.B.: verificare che il file "wireguard" salvato abbia l'estensione "**.conf**" (se diversa, **rinominare** correggendo)

------

!!! important "Fase 2 - Wireguard per Chiavette/Tv/Box/Firestick"
    Play Store Chiavette/Tv/Box - Apk **Firestick** 

??? info "Wireguard"
    **Chiavette/Tv/Box - Firestick**

    * **Chiavette/Tv/Box**: installare Wireguard dal Google Play Store
    * **Firestick**: scaricare apk Wireguard <a href="https://download.wireguard.com/android-client/" target="_blank">"com.wireguard.android-x.x.xxxxxxxx.apk"</a>
    Firestick vecchia con **Android 5**<br>
      <a href="../files/WireGuard_1_0_20210924_Android5.apk" target="_blank">Wireguard</a>

------

!!! important "Fase 3 - Localsend"
    **Inviare** file ".conf" a Chiavette/Tv/Box/Firestick (ed eventuale Apk Wireguard per Firestick)

??? info "Localsend"
    **Windows/macOS/Linux/Android/iOS/Chiavette/Tv/Box/Firestick**

    * Installare "Localsend" su **entrambi** i dispositivi "mittente" e "ricevente"
    * <a href="https://localsend.org/it/download" target="_blank">Sito Web</a> Loalsend Windows/macOS/Linux/Android/iOS/Chiavette/Tv/Box/Firestick<br>
    * Firestick vecchia con **Android 5**<br>
      <a href="../files/LocalSend_1_8_0_Android5.apk" target="_blank"> Localsend</a>Localsend<br>
    * Avviare Localsend **prima** sul dispositivo "ricevente" e **poi** su quello "mittente"
    * Sul dispositivo "mittente" premere "Invia" e poi "File" 
    * Selezionare files da inviare
    * Selezionare dispositivo "ricevente"
    * Sul dispositivo "ricevente" dare conferma per ricevere  
    * N.B.: la cartella "**Download**" è quella di default per la ricezione dei files
    * Sul dispositivo "ricevente" in alto a destra l'icona a fianco alla “i” elenca la cronologia

------

!!! important "Fase 4 - Installare Wireguard  su  Firestick"
    **Installazione** Wireguard su **Firestick**

??? info "Wireguard su Firestick"
    **Firestick**


    * In "**Localsend**" sul dispositivo "**ricevente**" in alto a destra l'icona a fianco alla “**i**” elenca la cronologia dei file ricevuti
    * Cliccare apk Wireguard 
    * Consentire installazione delle app da Localsend (se richiesto) e installarlo
    * Alla prima apertura, Wireguard potrebbe chiedere il permesso di accedere ai file
    * Concedere l'autorizzazione, se non appare richiesta, uscire e rientrare

------

!!! important " Fase 5 - Configurare Wireguard"
    **Impostare** Wireguard su Chiavette/Tv/Box/Firestick

??? info "Wireguard"
    **Chiavette/Tv/Box/Firestick**


    * Aprire Wireguard, premere il pulsante "**+**", poi "**Importa da file o archivio**"
    * Importare il file ".conf", sarà quindi presente nella schermata principale
    * Cliccare l'**interruttore** in corrispondenza a destra per attivare/disattivare
    * Al primo avvio verrà chiesta conferma di attivazione
    * N.B.: qualora non fosse possibile selezionare il file ".conf" durante l'importazione, installare dallo Store **file manager** come "x-plore " o simili

------

!!! important " EXTRA - WG Tunnel (sempre con file ".conf")"
    Installare **alternativa** "WG Tunnel" su Windows/Linux/Android/Chiavette/Tv/Box/Firestick

??? info "WG Tunnel"
    **Windows/Linux/Android/Chiavette/Tv/Box/Firestick**


    * Installare WG Tunnel
    * <a href="https://github.com/wgtunnel/android/releases/latest" target="_blank">Chiavette/Tv/Box/Firestick 32bit</a> (wgtunnel-standalone-vx.x.x-armv7.apk)
    * <a href="https://github.com/wgtunnel/android/releases/latest" target="_blank">Smartphone/Tablet 64bit</a> (wgtunnel-standalone-vx.x.x-armv64.apk)
    * <a href="https://github.com/wgtunnel/desktop/releases/latest" target="_blank">Windows 64bit</a></a> (wgtunnel-x.x.x.x64.msix)
    * <a href="https://github.com/wgtunnel/desktop/releases/latest" target="_blank">Linux 64bit</a> (wgtunnel_x.x.x_amd64.deb)
    * Avviare WG Tunnel
    * Alla prima apertura, WG Tunnel potrebbe chiedere il permesso di accedere ai file
    * Aperto WG Tunnel, premere il pulsante "**+**" e selezionare l'opzione "**importa da file**
    * Importato il file ".conf", sarà presente nella schermata principale 
    * Cliccare l'interruttore in corrispondeza sulla destra per attivare/disattivare 
    * Al primo avvio verrà chiesta conferma di attivazione 

------

