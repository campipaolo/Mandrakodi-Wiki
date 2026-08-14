[Tornaa alle guide](../guide/tutorials.md){.md-button .md-button--primary} [Torna alla Home](../index.md){.md-button .md-button--primary} 

------

!!! tip "Acestream, flussi P2P ad alta qualità"
    Sono link che sfruttano un protocollo basato sulla condivisione di flussi streaming audiovisivi tramite rete **p2p** (peer to peer) il che vuol dire creare interconnessioni tra più utenti e il server proprio come accadeva anni or sono con eMule/Torrent. <br>Questo significa che “chi guarda in streaming, trasmette anche agli altri utenti, ovvero più utenti guardano e condividono a loro volta ad altri , meno blocchi ci sono durante la visione”: **questo avviene esclusivamente solo se sul proprio router viene aperta la porta 8621 udp**

!!! warning "Lingua contenuti"
    I link acestream sono **praticamente totalmente stranieri**, in quentoin Italia poco utilizzati per mancanza della coltura di condivisione alla base di tutti i sistemi P2P come appunto Acestream, Emule, Torrent ecc

------

!!! important "Fase 1 - Installazione"
    Installare sul proprio dispositivo  

??? info "Acestream per Windows"
    **Installer per Windows**

    * [Download Windows](https://download.acestream.media/products/acestream-full/win/latest) 
    * Avviare Acestream

??? info "AceServe per Android/AndroidTv/Firestick"
    **Installer MOD per Android/AndroidTv/Firestick**

    * [Download Android ARMV8A 64bit](https://www.dropbox.com/scl/fi/uz8q15arnixvo47e9odbm/Aceserve-1.5.5-32bit.apk?rlkey=lhvtazx8sfqmrbd4qdsfsw1l9&st=nzwzt76l&dl=1)
    * [Download Android ARMV7A 32bit](https://)
    * Avviare AceServe una prima volta per dargli i permessi
    * Tornare alla home page col tasto dedicato per  lasciarlo aperto in background

??? info "Acestream per Linux"
    **Pacchetti per Linux**

    * Installare Acestream a seconda della propria distribuzione in formato "Snap" o "Flatpak"
    * Avviare Acestream



------

!!! important "Fase 2 - Player interno Kodi / Player esterno (es. Vlc)"
    - "ENGINE":   sfrutta motore di AceServe **rimanendo all'interno di Kodi**  usando il suo **player interno** <br>                           (richieste più risorse hardware, solo per device con 2Gb Ram)
    - "DIRETTO":   sfrutta motore di AceServe ma **esce da Kodi** usando un **player esterno** (es. Vlc) <br>                           (richieste meno risorse hardware, per dispositivi con 1,5Gb Ram)  

??? info "Opzione ENGINE"
    **Play all'interno di Kodi**

    * Avviare Kodi
    * In Mandrakodi avviare un link Ace
    * Usare opzione "ENGINE"

??? info "Opzione DIRETTO"
    **Play con player esterno (es. Vlc)**

    * Avviare Kodi
    * In Mandrakodi avviare un link Ace
    * Usare opzione "DIRETTO"
    * Selezionare "org.free.aceserve"
    * Selezionare player esterno (es. Vlc)

!!! warning "ATTENZIONE"
    Prima eseguire passaggi inerenti ai "Players Esterni" nella sezione Installazione >>> Impostazioni Kodi (se non precedentemente eseguita)

------

!!! important "EXTRA - AceServe con dispositivi poco performanti"
    Con dispositivi poco performanti  (tv/chiavetta con 1Gb/1,5Gb Ram e 8Gb storage) è consigliabile eseguire AceServe su **altro dispositivo** (generalmente smartphone) **purché connesso alla medesima rete,**  sfruttando maggiori risorse per cache disco e ram 

??? info "Kodi Tv/Chiavetta + AceServe Smartphone"
    **Eseguire AceServe su dispositivo terzo**

    * Installare AcesServe sullo smartphone
    * Avviare AcesServe sullo smartphone
    * Avviare Kodi su Tv/Chiavetta, dalla pagina principale, scorrere su addon
    * Tenere premuto sull'icona di Mandrakodi, poi "Impostazioni"
    * Nella scheda "Personal List", poi "Appo1", copiare come da foto inserendo IP smartphone
      ![acestream_app01](../images/acestream_app01.jpg)
    * N.B.: IP smartphone è visibile dalle proprietà della connessione Wifi
    * In Mandrakodi provare un qualunque link ace sempre e solo con opzione “ENGINE”

