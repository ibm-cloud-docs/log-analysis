---

copyright:
  years: 2017, 2019

lastupdated: "2019-03-06"

keywords: IBM Cloud, logging

subcollection: cloudloganalysis

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}
{:important: .important}
{:note: .note}

# Invio di dati in loco a un spazio in IBM Cloud
{: #send_data_mt}

Per inviare i dati di log nel servizio {{site.data.keyword.loganalysisshort}}, puoi configurare un Logstash Forwarder a più tenant (mt-logstash-forwarder). 
{: shortdesc}

Completa la seguente procedura per inviare i dati di log a uno spazio in {{site.data.keyword.Bluemix_notm}}:

## Prerequisiti
{: #prereqs1}

* Un ID {{site.data.keyword.Bluemix_notm}} per accedere a {{site.data.keyword.Bluemix_notm}}.
* Un ID utente che dispone delle autorizzazioni per lavorare in uno spazio con il servizio {{site.data.keyword.loganalysisshort}}. Per ulteriori informazioni, vedi [Sicurezza](/docs/services/CloudLogAnalysis/security_ov.html#security_ov).
* La CLI {{site.data.keyword.loganalysisshort}} installata nel tuo ambiente locale.
* Il servizio {{site.data.keyword.loganalysisshort}} di cui è stato eseguito il provisioning in uno spazio nel tuo account con un piano che consente l'inserimento dei log.


## Fase 1: Ottieni il token di registrazione
{: #get_logging_auth_token}

Completa la seguente procedura da una sessione terminale in cui è installata la CLI {{site.data.keyword.loganalysisshort}}:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Esegui il comando `ibmcloud logging token-get`. 

    ```
    ibmcloud logging token-get
    ```
    {: codeblock}

    Il comando restituisce il token di registrazione.
    
    Ad esempio,

    ```
    ibmcloud logging token-get
    Getting log token of resource: 93f54jh6-b5f5-46c9-9f0e-kfeutpldnbcf ...
    OK

    Tenant Id                              Logging Token   
    93f54jh6-b5f5-46c9-9f0e-kfeutpldnbcf   oT98_abcdefz   
    ```
    {: screen}

    dove *Tenant Id* è il GUID dello spazio a cui vuoi inviare i log.


## Fase 2: Configura mt-logstash-forwarder
{: #configure_mt_logstash_forwarder}

Completa la seguente procedura per configurare mt-logstash-forwarder nell'ambiente da cui pianifichi di inviare i log nel servizio {{site.data.keyword.loganalysisshort}}:

1.	Accedi come utente root. 

    ```
    sudo -s
    ```
    {: codeblock}
    
2.	Installa il pacchetto NTP (Network Time Protocol) per sincronizzare l'ora dei log. 

    Ad esempio, per un sistema Ubuntu, controlla se `timedatectl status` mostra *Network time on: yes*. Se lo visualizza, il tuo sistema Ubuntu è già configurato ad utilizzare ntp e puoi saltare questo passo.
    
    ```
    # timedatectl status
    Local time: Mon 2017-06-12 03:01:22 PDT
    Universal time: Mon 2017-06-12 10:01:22 UTC
    RTC time: Mon 2017-06-12 10:01:22
    Time zone: America/Los_Angeles (PDT, -0700)
    Network time on: yes
    NTP synchronized: yes
    RTC in local TZ: no
    ```
    {: screen}
    
    Completa la seguente procedura per installare ntp in un sistema Ubuntu:

    1.	Esegui il seguente comando per aggiornare i pacchetti. 

        ```
        apt-get update
        ```
        {: codeblock}
        
    2.	Esegui il seguente comando per installare il pacchetto ntp. 

        ```
        apt-get install ntp
        ```
        {: codeblock}
        
    3.	Esegui il seguente comando per installare il pacchetto ntpdate. 
    
        ```
        apt-get install ntpdate
        ```
        {: codeblock}
        
    4.	Esegui il seguente comando per arrestare il servizio. 
        
        ```
        service ntp stop
        ```
        {: codeblock}
        
    5.	Esegui il seguente comando per sincronizzare l'orologio di sistema. 
    
        ```
        ntpdate -u 0.ubuntu.pool.ntp.org
        ```
        {: codeblock}
        
        Il risultato conferma che l'ora è stata modificata, ad esempio:
        
        ```
        4 May 19:02:17 ntpdate[5732]: adjust time server 50.116.55.65 offset 0.000685 sec
        ```
        {: screen}
        
    6.	Esegui il seguente comando per avviare nuovamente ntpd. 
    
        ```
        service ntp start
        ```
        {: codeblock}
    
        Il risultato conferma che il servizio è in fase di avvio.

    7.	Esegui il seguente comando per abilitare l'avvio automatico del servizio ntpd dopo un arresto anomalo o un riavvio. 
    
        ```
        service ntp enable
        ```
        {: codeblock}
        
        Il risultato che viene visualizzato è un elenco di comandi che possono essere utilizzati per gestire il servizio ntpd, ad esempio:
        
        ```
        Usage: /etc/init.d/ntpd {start|stop|status|restart|try-restart|force-reload}
        ```
        {: screen}

3. Aggiungi il repository per il servizio {{site.data.keyword.loganalysisshort}} nel gestore pacchetti del sistema. Esegui il seguente comando:

    ```
    wget -O - https://downloads.opvis.bluemix.net/client/IBM_Logmet_repo_install.sh | bash
    ```
    {: codeblock}

4. Installa e configura mt-logstash-forwarder per inviare i log dal tuo ambiente nella raccolta dati. 

    1. Esegui il seguente comando per installare mt-logstash-forwarder:
    
        ```
        apt-get install mt-logstash-forwarder 
        ```
        {: codeblock}
        
    2. Crea il file di configurazione mt-logstash-forwarder per il tuo ambiente. Questo file include le variabili che vengono utilizzate per configurare il logstash forwarder mt per far puntare il forwarder al servizio {{site.data.keyword.loganalysisshort}}.
    
       Modifica il file `/etc/mt-logstash-forwarder/mt-lsf-config.sh`. Ad esempio, puoi utilizzare l'editor vi:
               
       ```
       vi /etc/mt-logstash-forwarder/mt-lsf-config.sh
       ```
       {: codeblock}
        
       Per far puntare il forwarder al servizio {{site.data.keyword.loganalysisshort}}, aggiungi le seguenti variabili al file **mt-lsf-config.sh**: 
         
       <table>
          <caption>Tabella 1. Elenco di variabili obbligatorie per far puntare il forwarder in una VM al servizio {{site.data.keyword.loganalysisshort}} </caption>
          <tr>
            <th>Nome Variabile</th>
            <th>Descrizione</th>
          </tr>
          <tr>
            <td>LSF_INSTANCE_ID</td>
            <td>ID della tua VM, ad esempio. *MyTestVM*. </td>
          </tr>
          <tr>
            <td>LSF_TARGET</td>
            <td>URL di destinazione. Per ottenere l'elenco di URL di inserimento, vedi [URL di inserimento](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls). Ad esempio, imposta il valore su **ingest.logging.ng.bluemix.net:9091** per inviare i log nella regione Stati Uniti Sud. </td>
          </tr>
          <tr>
            <td>LSF_TENANT_ID</td>
            <td>ID dello spazio in cui il servizio {{site.data.keyword.loganalysisshort}} è pronto a raccogliere i log che invii in {{site.data.keyword.Bluemix_notm}}. <br>Utilizza il valore che hai ottenuto nel passo 1.</td>
          </tr>
          <tr>
            <td>LSF_PASSWORD</td>
            <td>Token di registrazione. <br>Utilizza il valore che hai ottenuto nel passo 1.</td>
          </tr>
          <tr>
            <td>LSF_GROUP_ID</td>
            <td>Imposta questo valore su una tag personalizzata che puoi definire per raggruppare i log correlati.</td>
          </tr>
       </table>
        
       Ad esempio, ricerca il seguente file di esempio per uno spazio con l'ID *7d576e3b-170b-4fc2-a6c6-b7166fd57912* nella regione del regno unito:
        
       ```
       # more mt-lsf-config.sh
       LSF_INSTANCE_ID="myhelloapp"
       LSF_TARGET="ingest.logging.ng.bluemix.net:9091"
       LSF_TENANT_ID="7d576e3b-170b-4fc2-a6c6-b7166fd57912"
       LSF_PASSWORD="oT98_abcdefz"
       LSF_GROUP_ID="Group1"
       ```
       {: screen}
        
    3. Avvia mt-logstash-forwarder. 
    
       ```
       service mt-logstash-forwarder start
       ```
       {: codeblock}
                
Per impostazione predefinita, il forwarder controlla solo il syslog. I tuoi log sono disponibili in Kibana per l'analisi.
        

## Passo 3: Specifica più file di log
{: #add_logs}

Per impostazione predefinita, viene monitorato solo il file /var/log/syslog dal forwarder. Puoi aggiungere ulteriori file di configurazione nella seguente directory `/etc/mt-logstash-forwarder/conf.d/syslog.conf/` in modo che il forwarder li monitori. 

Completa la seguente procedura per aggiungere un file di configurazione a un'applicazione in esecuzione nel tuo ambiente

1.	Copia il file `/etc/mt-logstash-forwarder/conf.d/syslog.conf`. 

    **Suggerimento:** non modificare il file syslog.conf per aggiungere file di log.
    
    Ad esempio, in un sistema Ubuntu, esegui il seguente comando:
    
    ```
    cp /etc/mt-logstash-forwarder/conf.d/syslog.conf /etc/mt-logstash-forwarder/conf.d/myapp.conf
    ```
    {: codeblock}
        
2.	Con un editor di testo, modifica il file *myapp.conf* e aggiornalo per includere i log dell'applicazione che desideri monitorare: Includi il tipo di log per ogni log dell'applicazione. Elimina ogni esempio che non viene utilizzato.

3.	Riavvia mt-logstash-forwarder. 

     Riavvia il servizio mt-logstash-forwarder. Esegui il seguente comando:
    
    ```
    service mt-logstash-forwarder restart
    ```
    {: codeblock}

**Esempio**

Per includere stdout o stderr da un'applicazione hello, reindirizza stdout o stderr a un file di log. Crea un fil di configurazione forwarder per l'applicazione. Quindi, riavvia mt-logstash-forwarder.

1.	Copia il file `/etc/mt-logstash-forwarder/conf.d/syslog.conf`. 

    ```
    cp /etc/mt-logstash-forwarder/conf.d/syslog.conf /etc/mt-logstash-forwarder/conf.d/myapp.conf
    ```
    {: codeblock}
    
2. Modifica il file di configurazione *myapp.conf*.

    Per poter eseguire una ricerca in base a un campo JSON in Kibana quando inserisci un log, abilita l'analisi JSON. Imposta `is_json` su true nel file di configurazione per specifici percorsi file. Per i file di log configurati in questo modo, le righe di log devono essere formattate come blocchi JSON, separati da ritorni a capo. mt-logstash-forwarder utilizzerà quindi tutti questi campi JSON come singoli campi ricercabili da Kibana. I nomi campo JSON includono un suffisso basato sul tipo.
    
    ```
    {
    "files": [
         # other file configurations omitted...
            {
            "paths": [ "/var/log/myhelloapp.log" ],
            "fields": { "type": "helloapplog" },
            "is_json": true
            }
         ]
     }
     ```
     {: screen}
