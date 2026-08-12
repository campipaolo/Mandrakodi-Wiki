[Tornaa alle guide](../guide/tutorials.md){.md-button .md-button--primary} [Torna alla Home](../index.md){.md-button .md-button--primary} 

------

!!! warning "DNS: Obbligatori al giorno d'oggi!"
❓ Cosa c'entra con KODI/MANDRAKODI?

La maggior parte dei siti di streaming italiani non ha server in Italia: la magistratura, non potendo chiuderli, chiede a tutti i provider Internet di oscurarli, ossia di cancellare i record dei siti dal loro database
In questo modo, chiunque usi i loro DNS (tutti in pratica) non riuscirà a raggiungerli.
Siccome il mio addon, come anche altri, non fa altro che visitare i vari siti per estrapolarne il contenuto, anch'esso non sarà in grado di contattarli.
Alcuni siti cercano di contrastare questi continui oscuramenti cambiando dominio di frequente (pertanto a volte potrebbero andare, a volte no), altri invece hanno proprio rinunciato a modificarlo.
Per provare se il vostro problema sia davvero legato ai DNS basta visitare con un browser lo stesso sito (esempio https://1.dlhd.sx). 
Se la pagina non si apre, o se vi compare la scritta che il sito è sotto sequestro, avete i DNS di default.

❓ Come posso RISOLVERE?
Basta cambiare server DNS, impostandone uno che non oscura.

------

??? info "DNS  rete fissa"
    **Elenco DNS**

    * Opendns 
    - formato IPV4
      dns primario: 208.67.222.222
      dns secondario: 208.67.220.220
      - formato IPV6
      dns primario: 2620:119:35::35 
      dns secondario: 2620:119:53::53
    * Cloudflare 
    - formato IPV4
      dns primario: 1.1.1.1
      dns secondario: 1.0.0.1
      - formato IPV6
      dns primario: 2606:4700:4700::1111 
      dns secondario: 2606:4700:4700::1001

??? info "DNS  rete mobile"
    **Elenco DNS**

    * Opendns
      dns.opendns.com
    * Cloudflare 
      1dot1dot1dot1.cloudflare-dns.com 

------

!!! important "Guide per router di rete fissa"
    Di seguito guide per impostare i DNS sui router dei principali Internet Service Provider Italiani

??? info "Vodafone"
    **Vodafone Station FTTC e FTTH**

    * Con un browser (Chrome, Firefox, ecc.) da un dispositivo connesso alla Station 
    * Digitare nella barra degli indirizzi: http://vodafone.station/ 
    * Inserire le credenziali di accesso. 
      Se non sono state cambiate, si trovano sull'etichetta posta sotto / lato della Station 
    * Nell'angolo in alto a destra un menu a tendina,  o un pulsante che mostri la modalità  attuale (es. "Modalità base"), selezionare “Modalità Utente Esperto” 
    * Nel menu a sinistra o in alto, cliccare su "Internet" 
    * All'interno di questa sezione, cliccare la voce "DNS" 
    * Nella sezione “DNS Sicuro”, selezionare “Manuale” 
    * Appena sotto attivare opzione “Configura il DNS per tutti i tuoi dispositivi” 
    * Inserire i dns sia in formato IPV4 che IPV6 
    * Salvare i cambiamenti premendo il pulsante “Applica” 
    * Riavviare Vodafine Station 
    * Eseguire [test dns](https://dnsleaktest.com)
    * Selezionare "Extended test" e attendere, deve segnare ISP con nome dei dns impostati



??? info "Iliad"
    **IliadBox FTTH**

    * Con un browser (Chrome, Firefox, ecc.) da un dispositivo connesso alla Station 
    * Digitare nella barra degli indirizzi: 192.168.1.254 
    * Effettuare l’accesso al pannello di gestione dell’iliadbox inserendo la password scelta
    * Doppio clic sull’icona Parametri della iliadbox
    * Cliccare su Modalità avanzata 
    * Doppio clic su DHCP 
    * Selezionare scheda Server DHCP 
    * Inserire dns primario e secondario in formato IPV4 
    * Cliccare su Salva e poi su OK 
    * Doppio clic su Configurazione IPv6 
    * Selezionare scheda DNS IPv6 
    * Spuntare la voce Forza l’uso di server DNS IPv6 personalizzati 
    * Inserire dns primario e secondario in formato IPV6 
    * Eseguire [test dns](https://dnsleaktest.com)
    * Selezionare "Extended test" e attendere, deve segnare ISP con nome dei dns impostati



??? info "Fastweb"
    **Fastweb FTTH**

    * Con un browser (Chrome, Firefox, ecc.) da un dispositivo connesso alla Station 
    * Digitare nella barra degli indirizzi: 192.168.1.254
    * Nell'angolo in alto a destra un menu a tendina,  o un pulsante che mostri la modalità attuale (es. "Modalità base"), selezionare “Modalità Utente Esperto” 
    * Cliccare sulla scheda “Internet”
    * Nella sezione “DNS & DDNS”  disabilitare “DNS protetto”
    * Salvare le modifiche 
    * Sui vari dispositivi ricreare connessione alla rete Fastweb in modalità avanzata 
    * Sui vari dispositivi impostare manualmente i Dns 
    * Eseguire [test dns](https://dnsleaktest.com)
    * Selezionare "Extended test" e attendere, deve segnare ISP con nome dei dns impostati



??? info "Poste"
    **Poste FTTH**

    * Con un browser (Chrome, Firefox, ecc.) da un dispositivo connesso alla Station 
    * Digitare l'indirizzo IP del router ed inserire le credenziali, indicate nell'etichetta sul router
    * In alto premere su “Rete Locale”
    * Sulla sinistra premere su ”LAN”
    *  destra selezionare “Server DHCP” 
    * Nella sezione “ISP DNS” premere “Off” 
    * Inserire i  Dns in formato IPV4 
    * Salvare le modifiche
    * Eseguire [test dns](https://dnsleaktest.com)
    * Selezionare "Extended test" e attendere, deve segnare ISP con nome dei dns impostati



??? info "WINDTRE"
    **WINDTRE FTTC e FTTH**

    * Verificare se attivo il servizio “Più Sicuri Casa & Ufficio controlla” 
    * Da browser digitare l’indirizzo https://test.sicurezzaw3.it 
    * Se attivo disattivarlo da app windtre / area clienti / servizio clienti
    * Con un browser (Chrome, Firefox, ecc.) da un dispositivo connesso al Router
    * Digitare l'indirizzo IP del router ed inserire le credenziali, indicate nell'etichetta sul router 
    * Accedere  al menu di configurazione tramite il pulsante (tre linee in alto a destra) 
    * Selezionare  sezione “Network”  e poi  “Rete Locale LAN”
    * Scorrere le impostazioni fino alla sezione “Valori DNS” impostare DNS su “DNS statico” 
    * nserire i dns in formato IPV4
    * Salvare la configurazione cliccando sul tasto “Applica” 
    * Eseguire [test dns](https://dnsleaktest.com)
    * Selezionare "Extended test" e attendere, deve segnare ISP con nome dei dns impostati



??? info "Tim"
    **Tim FTTC e FTTH**

    * Dns non si possono inserire sul router dell’operatore 
    * Inserirli manualmente sul dispositivo (vedi sezione più sotto)




??? info "SKY Wifi"
    **SKY Wifi  FTTH**

    * Dns non si possono inserire né sul router dell’operatore  né sul singolo dispositivo, poiché non vengono comunque accettati
    * 




??? info "Eolo"
    **Eolo 5G**

    * Dns non si possono inserire né sul router dell’operatore  né sul singolo dispositivo, poiché non vengono comunque accettati
    * E' possibile richiedere solo IP Pubblico Statico a €4,90 al mese




??? info "Aruba"
    **Aruba  FTTH**

    * Dns non si possono inserire né sul router dell’operatore  né sul singolo dispositivo, poiché non vengono comunque accettati
    * E' possibile richiedere solo IP Pubblico Dinamico con una tantum €10




??? info "Enel"
    **Aruba  FTTC e FTTH**

    * Dns non si possono inserire né sul router dell’operatore  né sul singolo dispositivo, poiché non vengono comunque accettati
    * E' possibile solo con router di proprietà

------

!!! important "DNS su singolo dipositivo"
    Di seguito guide per impostare i DNS sui singolo dispositivo ove router non disponga di opzione per inserirli al suo interno

??? info "Rete fissa"
    **Rete fissa/AndroiTv/Firestick**

    * ** Smartphone Android: (passaggi indicativi a seconda versione Android e UI del modello)**
      1. Impostazioni, rete e internet
    
      2. Selezionare la propria connessione wifi
    
      3. A fianco della connessione premere su icona a forma di ingranaggio (proprietà connessione)
    
      4. In alto a destra premere su icona a forma di matita (modifica impostazioni)
    
      5. Nella sezione “Impostazioni IP” selezionare “IP Statico”
    
      6. Nella sezione “Gateway” inserire ip del proprio router (es. 192.168.1.1)
    
      7. Nella sezione “Lunghezza prefisso rete” inserire “24”
    
      8. Nella sezione “Indirizzo IP” inserire ip diverso da Gateway (es. 192.168.1.10)
    
      9. Eseguire [test dns](https://dnsleaktest.com)
      
      10. Selezionare "Extended test" e attendere, deve segnare ISP con nome dei dns impostati
      
    * ** Android Tv: (passaggi indicativi a seconda versione Android) **
      1. Impostazioni (icona a forma di ingranaggio in alto a destra)
    
      2. Rete Internet
    
      3. Selezionare la propria connessione wifi
    
      4. Nella sezione “Impostazioni IP” e selezionare “Statico”
    
      5. Nella sezione “Indirizzo IP” inserire ip diverso da quello del proprio router
    
      6. Nella sezione “Gateway” inserire ip del proprio router (es. 192.168.1.1)
    
      7. Nella sezione “Lunghezza prefisso rete” inserire “24”
    
      8. Nelle sezioni “DNS 1” e “DNS 2” inserire Dns primario e secondario formato IPV4
    
      9. Eseguire [test dns](https://dnsleaktest.com)
      
      10. Selezionare "Extended test" e attendere, deve segnare ISP con nome dei dns impostati
    
    * ** Firestick **
      1. Cliccare  su "Impostazioni"
    
      2. Selezionare "Sistemi"
    
      3. Selezionare "WI-FI"
    
      4. Selezionare la tua rete WI-FI e dimentica la rete WI-FI premendo il pulsante con 3 linee
    
      5. Nella sezione “Indirizzo IP” inserire ip diverso da quello del proprio router
    
      6. Premere il pulsante di selezione
    
      7. Selezionare la propria rete WI-FI
    
      8. Immettere la psw WI-FI e fare clic su "Avanzate"
    
      9. Inserire ip diverso da quello del proprio router
      
      10. Per il “Gateway” predefinito, inserire ip del proprio router (es. 192.168.1.1)
      
      11. Inserire '24' per 'Lunghezza prefisso di rete' e fare clic su 'Avanti'
      
      12. Nelle sezioni “DNS 1” e “DNS 2” inserire Dns primario e secondario formato IPV4
      
      13. Cliccare su connetti
      
      14. Eseguire [test dns](https://dnsleaktest.com)
      
      15. Selezionare "Extended test" e attendere, deve segnare ISP con nome dei dns impostati
      

??? info "Rete mobile"
    **Smartphone/Tablet Android**

    * Impostazioni, rete e internet
    * Selezionare “DNS Privato”
    * Selezionare “Nome host del provider DNS Privato”
    * Inserire DNS per rete mobile



