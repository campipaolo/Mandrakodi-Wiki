[:material-book-open-page-variant: Torna alle Guide](../guide/tutorials.md){ .md-button .md-button--primary }  [:material-home: Torna alla Home](../index.md){.md-button .md-button--primary}  [:material-face-agent: Assistenza](../ask_help.md){ .md-button .md-button--primary }

------

!!! tip "Impostazioni Kodi"
    Di seguito **settaggi consigliati** per migliori prestazioni dei vari flussi video 

------

!!! important "Players Esterni"
    A partire da Kodi 21.2 è possibile sfruttare **players esterni** (es. Ace, Vlc, Mx Player, Wuffy ecc) per riprodurre flussi video <br>Vale sia per Android/AndroidTv/Firestick che per Pc, di seguito i passaggi

!!! warning "Installare i vari player esterni"
    I players esterni (es. Mx Player, Wuffy Player) vanno **prima** installati sul dispositivo<br> [Mx Player Apk 32bit](https://) / [Mx Player Apk 64bit](https://)<br> [Wuffy Player Apk 32bit](https://) / [Wuffy Player Apk 64bit](https://)<br> 

??? info "Impostare Players Esterni con Android/AndroidTv/Firestick"
    **Avviare Kodi**

    * Entrare in Mandrakodi, sezione “**HELP ME!**”
    * Cliccare "PLAYER .XML (org.free.aceserve)"
    * Uscire da Kodi e rientrare, accedere a Mandrakodi
    * Selezionare canale (verificare se dispone di seconda pagina con link all'interno)
    * Tenere premuto sul link e selezionare voce "**riproduci con**"
    * Dall'elenco selezionare player installato

??? info "Impostare Players Esterni con Windows"
    **In Windows**

    * Scaricare [playercorefactory - windows.xml](https://raw.githubusercontent.com/mandrakodi/mandrakodi.github.io/main/pfc_win.xml) tenere premuto/tasto destro, salvare il files
    * Rinominare il file in "playercorefactory.xml" 
    * Con esplora file abilitare la visualizzazione di file e cartelle nascoste
    * Copiare il file nel percorso “C:/utenti/**tuonomeutente**/appdata/roaming/kodi/userdata”
    * Entrare in Mandrakodi
    * Selezionare canale (verificare se dispone di seconda pagina con link all'interno)
    * Tenere premuto sul link e selezionare voce "**riproduci con**"
    * Dall'elenco selezionare player esterno

 


------

!!! important "Flussi MPD"
    I link MDP sfruttano la libreria di kodi "**inputstream-adaptive**" che *regola automaticamente* la risoluzione video del flusso a seconda della propria connessione e del dispositivo <br> E' possibile sia impostare dei valori min/max sia **selezionare** una **risoluzione video** a piacimento tra quelle disponibili per ogni flusso video 

??? info "Impostazioni Flussi MPD"
    **Avviare Kodi**

    * Impostazioni, "Addon", "I miei addon" "Lettore Video Inputstream", Inputstream Adaptive" 
    * "Lettore Video Inputstream", Inputstream Adaptive", "Configura"
    * Tipo selezione del flusso: "**OSD manuale**"
    * Risoluzione massima:  "1080p"
    * Risoluzione minima:  "720p"
    * Premere "OK" per confermare

!!! warning "Come cambiare risoluzione video"
    Mentre si è in play, tasto centrale del telecomando o toccare touch smartphone <br> In basso a destra icona a forma di ingranaggio, "impostazioni video", "traccia video' <br> Si apre finestra con **elenco** delle varie risoluzioni video disponibili da poter selezionare

------

!!! important "Flussi DaddyLive"
    I canali **DaddyLive**, utilizzano il plugin **inputstream.ffmpegdirect**.
    Questo plugin, di default, utilizza la funzione **TimeShift** per permettere il **riavvolgimento** della live. <br>  Per farlo, salva dei file nella cartella di Kodi che vengono cancellati quando si ferma il video. <br>  Su device con poca memoria (esempio la FireStick), può creare problemi. 

??? info "Impostazioni Flussi DaddyLive"
    **Avviare Kodi**

    * Tenere premuto/tasto destro su icona dell'addon Mandrakodi 
    * "Impostazioni"
    * Sezione "**Personal List**" poi "**app02**"
    * All'interno scrivere "no_time_shift"
    ![daddylive_no_time_shift](../images/daddylive_no_time_shift.jpg)
    * Uscire da Kodi e rientrare

------

!!! important "Buffer/Cache"
    Kodi ha un suo sistema interno per gestire **cache con modalità buffer** per impostare una dimensione memoria per varie tipologie di flussi online/locali

??? info "Impostazioni Buffer/Cache"
    **Avviare Kodi**

    * Impostazioni, "Servizi"
    * In basso a sinistra cliccare sul pulsante "Base" fino a selezionare "Esperto"
    * Sulla sinistra compare il menu "**Cache**"
    * Modalità Buffer: selezionare "Buffer di tutti i file system internet"
    * Dimensione Memoria: "64 MB"
    * Uscire da Kodi e rientrare



!!! warning "Attenzione"
    Si ricorda che, in ogni caso, **quando il server della fonte è sovraccarico il buffering persiste comunque**.



