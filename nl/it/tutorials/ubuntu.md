---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ubuntu, tutorial

subcollection: LogDNA

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


# Gestione dei log Ubuntu con {{site.data.keyword.la_full_notm}}
{: #ubuntu}

Utilizza il servizio {{site.data.keyword.la_full}} per monitorare e gestire i log Ubuntu in un sistema di registrazione centralizzato su {{site.data.keyword.cloud_notm}}. 
{:shortdesc}

Puoi raccogliere e monitorare i log di sistema e delle applicazioni. 

Per impostazione predefinita, l'agent LogDNA per Ubuntu monitora i file di log nella directory **/var/log**. Ad esempio, il log di sistema Ubuntu (*/var/log/syslog*) viene monitorato per impostazione predefinita.

In {{site.data.keyword.cloud_notm}}, per configurare un server Ubuntu per inoltrare i log ad un'istanza {{site.data.keyword.la_full_notm}}, devi completare la seguente procedura:

1. Esegui il provisioning di un'istanza del servizio {{site.data.keyword.la_full_notm}}. 
2. Configura l'agent LogDNA nel server Ubuntu.
3. Facoltativamente, aggiungi ulteriori directory per il monitoraggio da parte dell'agent.

![Panoramica dei componenti su {{site.data.keyword.cloud_notm}}](../images/ubuntu.png "Panoramica dei componenti su {{site.data.keyword.cloud_notm}}")

In questa esercitazione, imparerai come configurare un server Ubuntu per inoltrare i log a un'istanza {{site.data.keyword.la_full_notm}}.

## Prima di iniziare
{: #ubuntu_prereqs}

Leggi a proposito di {{site.data.keyword.la_full_notm}}. Per ulteriori informazioni, vedi [Informazioni su LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).

Lavoro nella regione US-South. {{site.data.keyword.la_full_notm}} è attualmente disponibile nella regione Stati Uniti Sud. **Nota:** puoi inviare dati da un server Ubuntu che si trova nella stessa regione o in una regione differente. 

Utilizza un ID utente che sia un membro o un proprietario di un account {{site.data.keyword.cloud_notm}}. Per ottenere un ID utente {{site.data.keyword.cloud_notm}}, vai a [Registrazione![Icona link esterno](../../../icons/launch-glyph.svg "Icona link esterno")](https://cloud.ibm.com/login){:new_window}.

Al tuo ID {{site.data.keyword.IBM_notm}} devono essere assegnate le politiche IAM per ciascuna delle seguenti risorse: 

| Risorsa                             | Ambito della politica di accesso | Ruolo    | Regione    | Informazioni                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Gruppo di risorse **Predefinito**           |  Gruppo di risorse            | Visualizzatore  | us-south  | Questa politica è richiesta per consentire all'utente di visualizzare le istanze del servizio nel gruppo di risorse Predefinito.    |
| Servizio {{site.data.keyword.la_full_notm}} |  Gruppo di risorse            | Editor  | us-south  | Questa politica è richiesta per consentire all'utente di eseguire il provisioning e l'amministrazione del servizio {{site.data.keyword.la_full_notm}} nel gruppo di risorse Predefinito.   |
{: caption="Tabella 1. Elenco delle politiche IAM richieste per completare l'esercitazione" caption-side="top"} 

Installa la CLI {{site.data.keyword.cloud_notm}}. Per ulteriori informazioni, vedi [Installazione della CLI {{site.data.keyword.cloud_notm}}](/docs/cli/index.html#overview).



## Passo 1. Provisioning di un'istanza {{site.data.keyword.la_full_notm}}
{: #ubuntu_step1}

per eseguire il provisioning di un'istanza di {{site.data.keyword.la_full_notm}} mediante l'IU {{site.data.keyword.cloud_notm}}, completa la seguente procedura:

1. Accedi al tuo account {{site.data.keyword.cloud_notm}}.

    Fai clic sul [dashboard {{site.data.keyword.cloud_notm}} ![Icona link esterno](../../icons/launch-glyph.svg "Icona link esterno")](https://cloud.ibm.com/login){:new_window} per avviare il dashboard {{site.data.keyword.cloud_notm}}.

	Dopo che hai eseguito l'accesso con il tuo ID utente e la tua password, viene aperta l'IU {{site.data.keyword.cloud_notm}}.

2. Fai clic su **Catalogo**. Viene aperto l'elenco dei servizi disponibili in {{site.data.keyword.cloud_notm}}.

3. Per filtrare l'elenco dei servizi che viene visualizzato, seleziona la categoria **Strumenti per gli sviluppatori**.

4. Fai clic sul tile **{{site.data.keyword.la_full_notm}}**.

5. Immetti un nome per l'istanza del servizio.

6. Seleziona il gruppo di risorse **Predefinito**. 

    Per impostazione predefinita, è impostato il gruppo di risorse **Predefinito**.

7. Seleziona il piano di servizio **Lite**. 

    Per impostazione predefinita, è impostato il piano **Lite**.

    Per ulteriori informazioni sugli altri piani di servizio, vedi [Piani di prezzo](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

8. Per eseguire il provisioning del servizio {{site.data.keyword.la_full_notm}} nel gruppo di risorse {{site.data.keyword.cloud_notm}} in cui sei collegato, fai clic su **Crea**.

Dopo che hai eseguito il provisioning di un'istanza, viene aperto il dashboard {{site.data.keyword.la_full_notm}}. 


**Nota:** per eseguire il provisioning di un'istanza di LogDNA mediante la CLI, vedi [Provisioning di LogDNA mediante la CLI {{site.data.keyword.cloud_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-provision#provision_cli).


## Passo 2. Configura il tuo server Ubuntu per inviare i log alla tua istanza
{: #ubuntu_step2}

Per configurare il tuo server Ubuntu per inviare i log alla tua istanza {{site.data.keyword.la_full_notm}}, devi installare un `logdna-agent`. L'agent LogDNA legge i file di log da */var/log*, e inoltra i dati di log alla tua istanza LogDNA.

Per configurare il tuo server Ubuntu per inoltrare i log alla tua istanza LogDNA, completa la seguente procedura da un terminale Ubuntu:

1. Installa l'agent LogDNA. Esegui questi comandi:

    ```
    echo "deb https://repo.logdna.com stable main" | sudo tee /etc/apt/sources.list.d/logdna.list 
    ```
    {: codeblock}

    ```
    wget -O- https://repo.logdna.com/logdna.gpg | sudo apt-key add - 
    ```
    {: codeblock}

    ```
    sudo apt-get update
    ```
    {: codeblock}

    ```
    sudo apt-get install logdna-agent < "/dev/null"
    ```
    {: codeblock}

2. Imposta la chiave di inserimento che l'agent LogDNA deve utilizzare per inoltrare i log all'istanza {{site.data.keyword.la_full_notm}}.  

    ```
    sudo logdna-agent -k CHIAVE_DI_INSERIMENTO
    ```
    {: codeblock}

    dove CHIAVE_DI_INSERIMENTO contiene la chiave di inserimento attiva per l'istanza {{site.data.keyword.la_full_notm}} dove stai configurando l'inoltro dei log.

3. Imposta l'endpoint di autenticazione. L'agent LogDNA utilizza questo host per autenticare e ottenere il token per inoltrare i log.

    ```
    sudo logdna-agent -s LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com
    ```
    {: codeblock}

4. Imposta l'endpoint di inserimento.

    ```
    sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com
    ```
    {: codeblock}

5. Definisci più percorsi di log da monitorare. Esegui il seguente comando: 

    ```
    sudo logdna-agent -d /path/to/log/folders
    ```
    {: codeblock}

    Per impostazione predefinita, viene monitorato **/var/log**.

6. Facoltativamente, configura l'agent LogDNA per contrassegnare con delle tag i tuoi host. Esegui questi comandi:

    ```
    sudo logdna-agent -t TAG1,TAG2 
    ```
    {: codeblock}

    ```
    sudo update-rc.d logdna-agent defaults
    ```
    {: codeblock}

    ``` 
    sudo /etc/init.d/logdna-agent start
    ```
    {: codeblock}


## Passo 3. Avvia l'IU web LogDNA
{: #ubuntu_step3}

Per avviare il dashboard IBM Log Analysis con LogDNA mediante l'IU {{site.data.keyword.cloud_notm}}, completa la seguente procedura:

1. Accedi al tuo account {{site.data.keyword.cloud_notm}}.

    Fai clic sul [dashboard {{site.data.keyword.cloud_notm}} ![Icona link esterno](../../icons/launch-glyph.svg "Icona link esterno")](https://cloud.ibm.com/login){:new_window} per avviare il dashboard {{site.data.keyword.cloud_notm}}.

	Dopo che hai effettuato l'accesso con i tuoi ID utente e password, viene aperto il dashboard {{site.data.keyword.cloud_notm}}.

2. Nel menu di navigazione, seleziona **Osservabilità**. 

3. Seleziona **Registrazione**. 

    Viene visualizzato l'elenco delle istanze {{site.data.keyword.la_full_notm}} disponibili in {{site.data.keyword.cloud_notm}}.

3. Seleziona una singola istanza. Fai quindi clic su **Visualizza LogDNA**.

    Viene aperta l'IU web LogDNA, che visualizza i tuoi log del cluster.


## Passo 4. Visualizza i tuoi log
{: #ubuntu_step4}

Dall'IU web LogDNA, puoi visualizzare i tuoi log quando transitano per il sistema. Visualizzi i log utilizzando l'accodamento di log. 

**Nota:** con il piano di servizio **Gratuito**, puoi accodare solo i tuoi log più recenti.

Per ulteriori informazioni, vedi [Visualizzazione dei log](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs).


## Passi successivi
{: #ubuntu_next_steps}

[Filtra i log](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5), [ricerca nei log](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6), [definisci le viste](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7) e [configura gli avvisi](https://docs.logdna.com/docs/alerts). 

**Nota:** per utilizzare queste funzioni, devi eseguire l'upgrade del piano {{site.data.keyword.la_full_notm}} a un piano a pagamento.

