[:material-book-open-page-variant: Torna alle Guide](../guide/tutorials.md){ .md-button .md-button--primary }  [:material-home: Torna alla Home](../index.md){.md-button .md-button--primary} [:material-face-agent: Assistenza](../ask_help.md){ .md-button .md-button--primary }

------

!!! tip "Players Esterni"
    A partire da Kodi 21.2 per riprodurre flussi video è possibile sfruttare **players esterni** (es. Ace, Vlc, Mx Player, Wuffy Player, ecc)  più stabili del player interno di kodi molto "sensibile" ai flussi streaming <br>Vale sia per *Android* su Smartphone/Tablet/Chiavette/Tv/Box/Firestick che per *Pc* Windows, di seguito i passaggi 

!!! warning "Installare i vari players esterni"
    I players esterni (es. Ace, Mx Player, Wuffy Player,  ecc) vanno **prima** installati sul dispositivo

    * <a href="https://github.com/campipaolo/Mandrakodi-Wiki/releases/download/Files/mx-player-32bit.apk" target="_blank">Mx Player (Android)</a>  Tv/Chiavette/Box/Firestick<br>
    * <a href="https://github.com/campipaolo/Mandrakodi-Wiki/releases/download/Files/mx-player-64bit.apk" target="_blank">Mx Player (Android)</a>  Smartphone/Tablet<br>
    * <a href="https://github.com/campipaolo/Mandrakodi-Wiki/releases/download/Files/wuffy-player-32bit.apk" target="_blank">Wuffy Player (Android)</a>  Tv/Chiavette/Box/Firestick<br>
    * <a href="https://github.com/campipaolo/Mandrakodi-Wiki/releases/download/Files/wuffy-player-64bit.apk" target="_blank">Wuffy Player (Android)</a>  Smartphone/Tablet<br>
    * <a href="https://github.com/campipaolo/Mandrakodi-Wiki/releases/download/Files/wuffy-player-64bit.apk" target="_blank">Wuffy Player (Android)</a>  Smartphone/Tablet<br>
    * Acestream [Guida Installazione](../guide/acestream.md/)<br>

------

!!! important "Localsend (invio apk  a dispositivo no touch)"
    **Inviare** apk a Chiavette/Tv/Box/Firestick

    * Installare "Localsend" su **entrambi** i dispositivi "mittente" e "ricevente"
    * <a href="https://localsend.org/it/download" target="_blank">Loalsend</a>  Windows/macOS/Linux/Android/iOS/Chiavette/Tv/Box/Firestick<br>
    * Firestick con **Fire OS 5.x.x.x**: [LocalSend Android 5](https://github.com/campipaolo/Mandrakodi-Wiki/releases/download/Files/LocalSend_1_8_0_Android5.apk)<br>
    * Avviare Localsend **prima** sul dispositivo "ricevente" e **poi** su quello "mittente"
    * Sul dispositivo "mittente" premere "Invia" e poi "File" 
    * Selezionare files da inviare
    * Selezionare dispositivo "ricevente"
    * Sul dispositivo "ricevente" dare conferma per ricevere  
    * N.B.: la cartella "**Download**" è quella di default per la ricezione dei files
    * Sul dispositivo "ricevente" in alto a destra l'icona a fianco alla “i” elenca la cronologia

------

??? info "Impostare Players Esterni su Android Smartphone/Tablet/Chiavette/Tv/Box/Firestick"
    **Avviare Kodi**

    * Entrare in Mandrakodi, sezione “**HELP ME!**”
    * Cliccare "PLAYER .XML (org.free.aceserve)" e confermare
    * Uscire da Kodi e rientrare, accedere a Mandrakodi
    * Selezionare canale (verificare se dispone di seconda pagina con link all'interno)
    * Tenere premuto sul link e selezionare voce "**riproduci con**" [(Foto)](../images/kodi_riproduci_con.png){ target="_blank" }
    * Dall'elenco selezionare player installato

------

??? info "Impostare Players Esterni su Pc Windows"
    **In Windows**

    * Scaricare <a href="https://github.com/campipaolo/Mandrakodi-Wiki/releases/download/Files/playercorefactory_windows.xml" target="_blank">playercorefactory_windows.xml</a> tasto destro/tenere prenuto sul link e salvare
    * **Rinominare** il file in "playercorefactory.xml" 
    * Con esplora file **abilitare** la visualizzazione di file e cartelle nascoste
    * Copiare il file nel percorso “C:/utenti/**tuonomeutente**/appdata/roaming/kodi/userdata”
    * Entrare in Mandrakodi
    * Selezionare canale (verificare se dispone di seconda pagina con link all'interno)
    * Tenere premuto sul link e selezionare voce "**riproduci con**" [(Foto)](../images/kodi_riproduci_con.png){ target="_blank" }
    * Dall'elenco selezionare player esterno

------

??? info "Impostare Players Esterni su Pc Linux"
    **In Linux** con Kodi Flatpak

    * Scaricare <a href="https://github.com/campipaolo/Mandrakodi-Wiki/releases/download/Files/playercorefactory_linux.xml" target="_blank">playercorefactory_linux.xml</a> tasto destro/tenere prenuto sul link e salvare
    * **Rinominare** il file in "playercorefactory.xml" 
    * Con file manager **abilitare** la visualizzazione di file e cartelle nascoste
    * Nella propria Home Copiare il file nel percorso “.var/app/tv.kodi.Kodi/data/userdata”
    * Aprire il terminale e digitare:<br>
    ```bash
    sudo flatpak override tv.kodi.Kodi --talk-name=org.freedesktop.Flatpak 
    sudo flatpak override tv.kodi.Kodi --filesystem=host
    ```
    * Entrare in Mandrakodi
    * Selezionare canale (verificare se dispone di seconda pagina con link all'interno)
    * Tenere premuto sul link e selezionare voce "**riproduci con**" [(Foto)](../images/kodi_riproduci_con.png){ target="_blank" }
    * Dall'elenco selezionare player esterno
    * N.B.: chi utilizza player in formato Flatpak deve modificare nel playercorefactory.xml inserendo nome pacchetto come di seguito<br>
    --host flatpak run org.videolan.VLC "{1}"

