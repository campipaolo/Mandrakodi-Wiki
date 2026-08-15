[Torna alla Home](../index.md){.md-button .md-button--primary}

------

[ :material-arrow-right-bold: Impostazioni Kodi](kodi_settings.md){.md-button .md-button--primary}  [ :material-arrow-right-bold: Assistenza ](ask_help.md){.md-button .md-button--primary} 

------

!!! warning "Importante"
    Qualora Kodi fosse **pre installato** senza essere sicuri se installato con installer preso da sito, disinstallare e procedere seguendo istruzioni di seguito a seconda del Sistema Operativo 

!!! important "Attenzione"
    Per un pieno funzionamento di Kodi con tutte le sue dipendenze corrette, **scaricare Kodi dal proprio sito** per i vari Sistemi Operativi seguendo i passaggi sotto riportati

------

!!! tip "Fase 1 - Installazione"
    Installare Kodi sul proprio dispositivo

??? info "Kodi per Windows"
    **Installer per Windows**

    * [Download Windows](https://kodi.tv/download/windows/) 
    * Selezionare sezione "Recommended"
    * Scaricare Installer 32bit o 64bit (NON Windows Store)

??? info "Kodi per Android / Android TV"
    **Installer per Android / Android TV**

    * [Download Android/AndroidTv](https://kodi.tv/download/android/)
    * Selezionare sezione "Recommended"
    * Scaricare Installer ARMV7A 32bit (Android TV fino v12) o ARMV8A 64bit (Smartphone/Tablet/Android TV >14)

??? info "Kodi per macOS"
    **Installer per macOS**

    * [Download macOS](https://kodi.tv/download/macos/)
    * Selezionare sezione "Recommended"
    * Scaricare Installer Intel (x86_64) o ARM64

??? info "Kodi per iOS"
    **Guida con Esign**

    1. **Installare il profilo DNS**
       1. Apri Safari sull’iPhone.
       2. Vai al sito https://www.applejr.xyz/?m=1
       3. Clicca su AppleJrDNS.
       4. Scarica il profilo.
       5. Quando iOS segnala che è stato scaricato un profilo, apri Impostazioni.
       6. Tocca Profilo scaricato.
       7. Controlla attentamente il nome dell’organizzazione e ciò che il profilo vuole configurare.
       8. Se sei sicuro della provenienza, procedi con l’installazione.
       9. In alternativa, puoi trovare il profilo da **Impostazioni** → **Generali** → **VPN e gestione dispositivo**.
    
    2. **Installare ESign**
       Dopo aver configurato il DNS:
       1. Vai alla pagina https://api.khoindvn.eu.org/fSfJEA
       2. Apri la sezione Esign.
       3. Scegli una delle installazioni ESign disponibili.
       4. Tocca Install.
       5. Attendi che iOS completi l’installazione.
    
       Dopo l’installazione, potrebbe essere necessario autorizzare il certificato aziendale da:
       **Impostazioni** → **Generali** → **VPN e gestione dispositivo**
    
    3. **Autorizzare l’app**
       Se iOS non permette di aprire ESign:
       1. Vai in Impostazioni.
       2. Apri Generali.
       3. Vai in VPN e gestione dispositivo.
       4. Seleziona il profilo/certificato relativo all’app.
       5. Verifica attentamente l’organizzazione indicata.
       6. Se riconosci e ti fidi del certificato, puoi procedere con l’autorizzazione.
    
       Se compare un messaggio come *“Impossibile verificare l’integrità dell’app”*, non cercare semplicemente di aggirarlo installando certificati casuali: il certificato potrebbe essere stato revocato o non essere più valido.
    
    4. **Installare un file IPA**
       Una volta configurato ESign:
       1. Scarica il file `.ipa` di Kodi da qui: https://kodiipa.com
       2. Apri ESign.
       3. Tocca i tre puntini.
       4. Seleziona Import.
       5. Cerca il file IPA nell’app File.
       6. Tocca il file.
       7. Conferma l’importazione.
    
       Il file dovrebbe comparire nella lista di ESign.
    
    5. **Firmare l’IPA**
       1. Tocca il file IPA importato.
       2. Seleziona Signature.
       3. Apri More Settings.
       4. Se disponibile, abilita **Remove mobileprovision after signing**.
       5. Tocca Signature.
       6. Al termine della firma, tocca Install.
       7. Attendi il completamento dell’installazione.
    
    6. **Dopo l’installazione**
       Una volta terminata l’installazione:
       - L’app dovrebbe comparire sulla schermata Home.
       - Puoi provare ad aprirla.
       - Se iOS non la avvia, controlla **Impostazioni** → **Generali** → **VPN e gestione dispositivo**.
       - Se il certificato è stato revocato, l’app potrebbe smettere di funzionare.
    
    7. **Problemi comuni**
       - **“Integrity could not be verified”**
         Di solito significa che iOS non riesce a verificare correttamente la firma dell’app.
         *Possibili cause:*
         - Certificato revocato;
         - Firma non valida;
         - Profilo/certificato non configurato correttamente;
         - IPA modificato o danneggiato.
    
       - **ESign non si installa**
         Controlla:
         1. Che il profilo DNS sia stato installato correttamente;
         2. Che il certificato utilizzato sia ancora valido;
         3. Che l’installazione non sia stata bloccata da iOS.
    
       - **L’app si installa ma non si apre**
         Il certificato potrebbe essere stato revocato oppure l’IPA potrebbe essere incompatibile con il dispositivo/iOS.
    
       - **ESign smette improvvisamente di funzionare**
         È possibile che il certificato utilizzato sia stato revocato. Il sito stesso segnala che gli utenti ESign possono incontrare problemi di verifica e revoca.
    
    8. **La cosa più importante: sicurezza**
       ESign può essere utile, ma il rischio principale non è necessariamente ESign in sé: sono soprattutto i file IPA, i profili di configurazione e i certificati scaricati da fonti non ufficiali.
    
       *Prima di installare qualcosa:*
       - Evita IPA provenienti da fonti sconosciute;
       - Controlla sempre cosa stai installando;
       - Non inserire il tuo Apple ID o la password in siti che promettono certificati;
       - Non installare profili DNS che non riconosci;
       - Non autorizzare certificati Enterprise di organizzazioni sconosciute;
       - Per app importanti, preferisci App Store o metodi ufficiali Apple.





??? info "Kodi per Linux"
    **Installer Flatpak**

    * [Download Linux](https://flathub.org/en/apps/tv.kodi.Kodi)
    * Premere pulsante "Install" o installare dal proprio Store
    * Da terminale digitare:
    
      ```bash
      sudo flatpak install flathub tv.kodi.Kodi
      ```

------

!!! tip "Fase 2 - Installazione addon"
    Installare l'addon Mandrakodi

??? info "Mandrakodi"
    **Guida all'installazione**

    * **Fase 1: Inserimento Sorgente**
      1. Cliccare sulla rotellina delle impostazioni:
    
         ![kodi_settings](../images/kodi_settings.jpg)
    
      2. Cliccare su **File**:
    
         ![kodi_settings](../images/kodi_file.jpg)
    
      3. Nella maschera che compare (Gestore File), cliccare su **Aggiungi sorgente**:
    
         ![kodi_source_add](../images/kodi_source_add.jpg)
    
      4. Nella maschera, cliccare su **Nessuno**:
    
         ![kodi_source_boxurl](../images/kodi_source_boxurl.jpg)
    
      5. Nella nuova maschera, inserire l'URL `https://mandrakodi.github.io` e poi premere **OK**:
    
         ![kodi_source_url](../images/kodi_source_url.jpg)
    
      6. Nella maschera cliccare nello spazio vuoto sotto *"Inserisci un nome per questa sorgente elementi"*:
    
         ![kodi_source_boxname](../images/kodi_source_boxname.png)
    
      7. Inserire un nome qualunque e premere **OK**:
    
         ![kodi_source_boxname](../images/kodi_source_boxname.jpg)
    
      8. Nella maschera, a questo punto, si è attivato il pulsante **OK** per aggiungere la sorgente. Cliccatelo:
    
         ![kodi_source_confirm1](../images/kodi_source_confirm1.jpg)
    
      9. Adesso, nella maschera Gestore File, vi comparirà il nome che avete scelto:
    
         ![kodi_source_select](../images/kodi_source_select.jpg)
    
    * **Fase 2: Installazione Add-on**
      *Pre-requisito: Installare dal Repository Ufficiale l'add-on YouTube (questo passaggio scaricherà dei componenti aggiuntivi necessari per MandraKodi)*
    
      1. Cliccare sulla rotellina delle impostazioni:
    
         ![kodi_settings](../images/kodi_settings.jpg)
    
      2. Nella maschera che compare, cliccare su **Add-on**:
    
         ![kodi_addon](../images/kodi_addon.jpg)
    
      3. Nella nuova maschera, selezionare **Installa da file zip**:
    
         ![kodi_install_fromzip](../images/kodi_install_fromzip.jpg)
    
         * **A.** Se è la prima volta che installate un add-on non ufficiale, vi comparirà questa maschera:
    
           ![kodi_addon_allert](../images/kodi_addon_allert.jpg)
    
         * **B.** Cliccare su **Impostazioni** e, nella nuova maschera, attivare **Sorgenti sconosciute**:
    
           ![kodi_source_unknow](../images/kodi_source_unknow.jpg)
    
         * **C.** Comparirà un altro avviso dove bisogna rispondere **SÌ**:
    
           ![kodi_source_external](../images/kodi_source_external.jpg)
    
      4. Se avete già attivato le "Sorgenti sconosciute", comparirà questo avviso. Cliccare su **SÌ**:
    
         ![kodi_source_confirm2](../images/kodi_source_confirm2.jpg)
    
      5. Nella maschera selezionare il nome della sorgente di MandraKodi:
    
         ![kodi_install_selectsource](../images/kodi_install_selectsource.jpg)
    
      6. Nell'elenco che compare, selezionare il file `plugin.video.mandrakodi-2.2.1a.zip` (o la versione attualmente disponibile):
    
         ![kodi_install_selectzip](../images/kodi_install_selectzip.jpg)
    
      7. Attendere fino a quando non compare il messaggio *"Add-on installato"*:
    
         ![kodi_mandra_installed](../images/kodi_mandra_installed.jpg)
    
    * **Fase 3: Installazione script aggiuntivi**
    
    **A) Script.module.resolveurl**
    * Ripetere i passaggi 1 – 5 fatti per l'installazione dell'add-on MandraKodi.
    * Nell'elenco che compare, selezionare il file `script.module.resolveurl-5.1.92.zip` (o la versione attualmente disponibile):
    
    ![kodi_resolverurl_select](../images/kodi_resolverurl_select.jpg)
    
    * Attendere fino a quando non compare il messaggio *"Add-on installato"*:
    
    ![kodi_resolverurl_installed](../images/kodi_resolverurl_installed.jpg)
    
    **B) Script.module.resolveurl.xxx**
    * Ripetere i passaggi 1 – 5 fatti per l'installazione dell'add-on MandraKodi.
    * Nell'elenco che compare, selezionare il file `script.module.resolveurl.xxx-2.1.35.zip` (o la versione attualmente disponibile):
    
    ![kodi_resolverxxx_select](../images/kodi_resolverxxx_select.jpg)
    
    * Attendere fino a quando non compare il messaggio *"Add-on installato"*:
    
    ![kodi_resolverurl_installed](../images/kodi_resolverurl_installed.jpg)
    
    * **Fase 4: Configurazione addon**
      1. Cliccare sulla rotellina delle impostazioni:
    
         ![kodi_settings](../images/kodi_settings.jpg)
    
      2. Nella maschera che compare, cliccare su **Add-on**:
    
         ![kodi_addon](../images/kodi_addon.jpg)
    
      3. Nella nuova maschera, selezionare **I miei Add-on**:
    
         ![kodi_myaddons](../images/kodi_myaddons.jpg)
    
      4. Nella nuova maschera, selezionare **Addon video**:
    
         ![kodi_addonvideo](../images/kodi_addonvideo.jpg)
    
      5. Selezionare l'add-on **MandraKodi**:
    
         ![kodi_mandra_select](../images/kodi_mandra_select.jpg)
    
      6. Nella maschera dell'add-on, selezionare **Configura**:
    
         ![kodi_mandra_settings1](../images/kodi_mandra_settings1.jpg)
    
      7. Nella maschera inserire l'URL preso dal bot `@mandrakodibot` e premere **OK**:
    
         ![kodi_mandra_settings2](../images/kodi_mandra_settings2.jpg)
