---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion key

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

# Gestione delle chiavi di inserimento
{: #ingestion_key}

La chiave di inserimento è una chiave di sicurezza che devi utilizzare per configurare gli agent LogDNA e inoltrare correttamente i log alla tua istanza {{site.data.keyword.la_full_notm}} in {{site.data.keyword.cloud_notm}}. Ottieni automaticamente la chiave di inserimento quando esegui il provisioning di un'istanza. In alternativa, puoi anche ottenere la chiave di inserimento creando un ID servizio per l'istanza.. 
{:shortdesc}

**Nota:** 

* Per gestire le chiavi di inserimento mediante l'IU web {{site.data.keyword.la_full_notm}}, devi disporre di una politica IAM con il ruolo della piattaforma **Visualizzatore** e il ruolo del servizio **Gestore** per il servizio {{site.data.keyword.la_full_notm}}. 
* Per gestire le chiavi di inserimento mediante l'IU {{site.data.keyword.cloud_notm}}, devi disporre di una politica IAM con il ruolo della piattaforma **Editor** e il ruolo del servizio **Gestore** per il servizio {{site.data.keyword.la_full_notm}}. 


## Ottieni la chiave di inserimento mediante l'IU {{site.data.keyword.cloud_notm}}
{: #ibm_cloud_ui}

Per ottenere la chiave di inserimento da un'istanza {{site.data.keyword.la_full_notm}} utilizzando l'IU {{site.data.keyword.cloud_notm}}, completa la seguente procedura:

1. Accedi al tuo account {{site.data.keyword.cloud_notm}}.

    Fai clic sul [dashboard {{site.data.keyword.cloud_notm}} ![Icona link esterno](../../icons/launch-glyph.svg "Icona link esterno")](https://cloud.ibm.com/login){:new_window} per avviare il dashboard {{site.data.keyword.cloud_notm}}.

	Dopo che hai eseguito l'accesso con il tuo ID utente e la tua password, viene aperta l'IU {{site.data.keyword.cloud_notm}}.

2. Nel menu di navigazione, seleziona **Osservabilità**. 

3. Seleziona **Registrazione**. Viene aperto il dashboard {{site.data.keyword.la_full_notm}}. Puoi vedere l'elenco delle istanze di registrazione disponibili in {{site.data.keyword.cloud_notm}}.

3. Identifica l'istanza per la quale desideri ottenere la chiave di inserimento e fai clic su **Visualizza chiave di inserimento**.

4. Viene visualizzata una finestra dove puoi fare clic su **Mostra** per visualizzare la chiave di inserimento.


## Ottieni la chiave di inserimento mediante l'IU web {{site.data.keyword.la_full_notm}}
{: #logdna_ui}

Per ottenere la chiave di inserimento per un'istanza {{site.data.keyword.la_full_notm}} utilizzando l'IU web {{site.data.keyword.la_full_notm}}, completa la seguente procedura:

1. Avvia l'IU web {{site.data.keyword.la_full_notm}}. Per ulteriori informazioni, vedi [Avvio dell'IU web {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Seleziona l'icona **Configuration**. Seleziona quindi **Organization**. 

3. Seleziona **API keys**.

Puoi visualizzare le chiavi di inserimento che sono state create. 

**Nota:** è attiva solo una singola chiave di inserimento per volta. 


## Ottieni la chiave di inserimento mediante la CLI {{site.data.keyword.cloud_notm}}
{: #ibm_cloud_cli}

Per ottenere la chiave di inserimento per un'istanza {{site.data.keyword.la_full_notm}} mediante la riga di comando, completa la seguente procedura:

1. [Pre-requisito] Installa la CLI {{site.data.keyword.cloud_notm}}.

   Per ulteriori informazioni, vedi [Installazione della CLI {{site.data.keyword.cloud_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).

   Se la CLI è installata, continua con il passo successivo.

2. Accedi alla regione in {{site.data.keyword.cloud_notm}} dove l'istanza è in esecuzione. Esegui il seguente comando: [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Imposta il gruppo di risorse in cui l'istanza {{site.data.keyword.la_full_notm}} è in esecuzione. Esegui il seguente comando: [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target) con l'opzione `-g`.

    Per impostazione predefinita, è impostato il gruppo di risorse `default`.

4. Ottieni il nome della chiave API associata all'istanza {{site.data.keyword.la_full_notm}}. Esegui il comando [`ibmcloud resource service-keys`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_keys):

    ```
    ibmcloud resource service-keys
    ```
    {: codeblock}

    Identifica la chiave di servizio associata alla tua istanza.

5. Ottieni la chiave di inserimento. Esegui il comando [`ibmcloud resource service-key`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_key):

    ```
    ibmcloud resource service-key NOME_CHIAVEAPI
    ```
    {: codeblock}

    Dove NOME_CHIAVEAPI è il nome della chiave API
 
    L'output da questo comando include il campo **ingestion_key** che contiene la chiave di inserimento per l'istanza.


## Reimposta la chiave di inserimento 
{: #reset}

Se la chiave di inserimento è danneggiata oppure hai una politica di rinnovarla dopo un certo numero di giorni, puoi generare una nuova chiave ed eliminare quella vecchia.

Per rinnovare la chiave di inserimento per un'istanza {{site.data.keyword.la_full_notm}} utilizzando l'IU web {{site.data.keyword.la_full_notm}}, completa la seguente procedura:

1. Avvia l'IU web {{site.data.keyword.la_full_notm}}. Per ulteriori informazioni, vedi [Avvio dell'IU web {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Seleziona l'icona **Configuration**. Seleziona quindi **Organization**. 

3. Seleziona **API keys**.

    Puoi visualizzare le chiavi di inserimento che sono state create. 

4. Seleziona **Generate Ingestion Key**.

    Una nuova chiave viene aggiunta all'elenco.

5. Elimina la vecchia chiave di inserimento. Fai clic su **delete**.

**Nota:** dopo che hai reimpostato la chiave di inserimento, devi aggiornare la chiave di inserimento per le eventuali origini log che hai configurato per inoltrare i log a questa istanza {{site.data.keyword.la_full_notm}}.



