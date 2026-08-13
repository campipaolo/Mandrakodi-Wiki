[Tornaa alle guide](../guide/tutorials.md){.md-button .md-button--primary} [Torna alla Home](../index.md){.md-button .md-button--primary} 

------

!!! tip "Warp / Wireguard"
    Sono richiesti per alcuni link iinseriti in Mandrakodi contrassegnati con dicitura  **"WARP"**  <br>    Warp (WIndows/macOS/Linux/Android/Ios) una volta installato non richiede altre configurazioni <br>    Wireguard (AndroidTv/Firestick) una volta installato richiede file ".conf" per funzionare correttamente 

!!! warning "Attenzione"
    File ".conf" è utilizzabile su più dispositivi contemporaneamente da stessa rete e tra reti diverse <br> **Sconsigliamo** di **condividere** il proprio file .conf **con più utenti**, ad esagerare finisce che Cloudlfare poi impone un   file diverso per ogni dispositivo e pure per ogni tipologia di rete....

------

!!! important " Fase 1"
    Esistono più metodi per creare file ".conf" da utilizare in WIreguard su AndroidTv/Firestick <br>    - Con sito Config Generator (scadenza 90gg) <br>    - Con Pc desktop (Windows) con "WGCF" (nessuna scadenza) <br>    - Con Smartphone Android con app "Termux" (nessuna scadenza)

??? info "Sito Config Generator"
    ** Scadenza 90gg **

    * [Config Generator](https://lanrat.github.io/wireguard-warp-generator/) 
    * Premere il pulsante "Generate Warp Config"
    * Premere bottone "Download warp.conf"
    * Il file così creato, ha una durata di 90 giorni trascorsi i quali va rigenerato
      ![wireguard_config_online](../images/wireguard_config_online.jpg)
    * N.B.: verificare che il file salvato abbia l'estensione ".conf"

??? info "Pc con WGCF"
    ** Nessuna scadenza **

    * [WGCG](https://github.com/ViRb3/wgcf/releases) 
    * Scorrere fino alla sezione "Assets" (premere "Show All" per espandere l'elenco)
    * Windows 64bit: wgcf_x.x.x_windows_amd64.exe	Windows ARM: wgcf_2.2.32_windows_arm64.exe 
    * Copiare il file scaricato sul Desktop
    * Rinominarlo in "wgcf.exe"
    * Premere il tasto Windows, scrivere "cmd" e premere invio
    * Digitare "cd desktop" e premere invio
    * Digitare "wgcf.exe register" e premere invio
    * Quando richiesto andare su "Yes" e premere invio
    * Sul desktop saranno presenti due file, l'unico da conservare è "wgcf-profile.conf"

??? info "Smartphone Android con app Termux"
    ** Nessuna scadenza **

    * [Termux Play Store](https://play.google.com/store/apps/details?id=com.termux&hl=it) 
    * Installare ed avviare 
    * N.B.: di seguito comandi da copiaree poi incollare in termux, uno alla volta (quando richiesto premere invio alla domanda "Y" o scrivere Yes per confermare) 
    * termux-setup-storage (abilitare permesso scrittura  su dispositivo)
    * pkg install wget
    * pkg install git 
    * git clone https://github.com/ViRb3/wgcf
    * cd wgcf
    * pkg install golang
    * go mod download
    * go build -o wgcf
    * chmod +x wgcf
    * ./wgcf register
    * ./wgcf generate
    * ./wgcf status
    * ls
    * cp wgcf-profile.conf ~/storage/downloads
    * exit
    * N.B.: il file ".conf"  sarà reperibile nella cartella Download del prprio device

