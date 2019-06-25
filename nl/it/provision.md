---

copyright:
  years:  2018, 2019
lastupdated: "2019-04-02"

keywords: LogDNA, IBM, Log Analysis, logging instance, provision

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

# Provisioning di un'istanza
{: #provision}

Prima di poter monitorare e gestire i dati di log con {{site.data.keyword.la_full_notm}} devi eseguire il provisioning di un'istanza del servizio in {{site.data.keyword.cloud_notm}}.
{:shortdesc}

Per eseguire il provisioning di un'istanza {{site.data.keyword.la_full_notm}} in una regione cloud pubblico, devi selezionare il piano di servizio associato all'istanza, la regione in cui vengono raccolti i log e il piano che determina il periodo di conservazione per i tuoi log. Puoi scegliere da periodi di conservazione di 7, 14 o 30 giorni.

In alternativa, {{site.data.keyword.la_full_notm}} offre un piano `Lite` che puoi utilizzare per visualizzare i tuoi log quando transitano per il sistema. Puoi visualizzare i log utilizzando l'accodamento di log. Puoi anche progettare dei filtri per la preparazione all'upgrade a un piano con un periodo di conservazione più lungo. Questo piano ha un periodo di conservazione di 0 giorni.


## Provisioning di un'istanza mediante il dashboard Osservabilità
{: #provision_ui}

Per eseguire il provisioning di un'istanza dal dashboard Osservabilità in {{site.data.keyword.cloud_notm}}, completa la seguente procedura:

1. Accedi al tuo account {{site.data.keyword.cloud_notm}}.

    Il dashboard {{site.data.keyword.cloud_notm}} è disponibile in: [dashboard {{site.data.keyword.cloud_notm}} ![Icona link esterno](../../icons/launch-glyph.svg "Icona link esterno")](https://cloud.ibm.com/login){:new_window}.

	Dopo che hai eseguito l'accesso con il tuo ID utente e la tua password, viene aperta l'IU {{site.data.keyword.cloud_notm}}.

2. Vai all'icona di menu ![icona di menu](../../icons/icon_hamburger.svg). Seleziona quindi **Osservabilità** per accedere al dashboard *Osservabilità*.

3. Seleziona **Registrazione** e fai quindi clic su **Crea istanza**. 

4. Immetti un nome per l'istanza del servizio.

5. Seleziona un gruppo di risorse. 

    Per impostazione predefinita, è impostato il gruppo di risorse **Predefinito**.

    **Nota:** se non sei in grado di selezionare un gruppo di risorse, controlla di disporre delle autorizzazioni di modifica sul gruppo di risorse dove desideri eseguire il provisioning dell'istanza.

6. Seleziona il piano di servizio `Lite`. 

    Per impostazione predefinita, è impostato il piano Lite.

    Per ulteriori informazioni sugli altri piani di servizio, vedi [Piani di prezzo](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

7. Fai clic su **Crea**.

Dopo che hai eseguito il provisioning di un'istanza, viene aperto il dashboard *Registrazione*. 

Configura quindi un'origine log aggiungendo un agent LogDNA. Questo agent è responsabile della raccolta e dell'inoltro dei log alla tua istanza. 



## Provisioning di un'istanza mediante il catalogo
{: #provision_catalog}

Per eseguire il provisioning di un'istanza di {{site.data.keyword.la_full_notm}} mediante il catalogo {{site.data.keyword.cloud_notm}}, completa la seguente procedura:

1. Accedi al tuo account {{site.data.keyword.cloud_notm}}.

    Fai clic sul [dashboard {{site.data.keyword.cloud_notm}} ![Icona link esterno](../../icons/launch-glyph.svg "Icona link esterno")](https://cloud.ibm.com/login){:new_window} per avviare il dashboard {{site.data.keyword.cloud_notm}}.

	Dopo che hai eseguito l'accesso con il tuo ID utente e la tua password, viene aperta l'IU {{site.data.keyword.cloud_notm}}.

2. Fai clic su **Catalogo**. Viene aperto l'elenco dei servizi disponibili in {{site.data.keyword.cloud_notm}}.

3. Per filtrare l'elenco dei servizi che viene visualizzato, seleziona la categoria **Strumenti per gli sviluppatori**.

4. Fai clic sul tile **{{site.data.keyword.la_full_notm}}**. 

5. Immetti un nome per l'istanza del servizio.

6. Seleziona un gruppo di risorse. 

    Per impostazione predefinita, è impostato il gruppo di risorse **Predefinito**.

    **Nota:** se non sei in grado di selezionare un gruppo di risorse, controlla di disporre delle autorizzazioni di modifica sul gruppo di risorse dove desideri eseguire il provisioning dell'istanza.

7. Seleziona il piano di servizio `Lite`. 

    Per impostazione predefinita, è impostato il piano Lite.

    Per ulteriori informazioni sugli altri piani di servizio, vedi [Piani di prezzo](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

8. Fai clic su **Crea**.

Dopo che hai eseguito il provisioning di un'istanza, viene aperto il dashboard *Registrazione*. 

Configura quindi un'origine log aggiungendo un agent LogDNA. Questo agent è responsabile della raccolta e dell'inoltro dei log alla tua istanza. 



## Provisioning di un'istanza mediante la CLI
{: #provision_cli}

Per eseguire il provisioning di un'istanza di {{site.data.keyword.la_full_notm}} mediante la riga di comando, completa la seguente procedura:

1. [Prerequisito] Installazione della CLI {{site.data.keyword.cloud_notm}}.

   Per ulteriori informazioni, vedi [Installazione della CLI {{site.data.keyword.cloud_notm}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli).

   Se la CLI è installata, continua con il passo successivo.

2. Accedi alla regione in {{site.data.keyword.cloud_notm}} dove desideri eseguire il provisioning dell'istanza. Esegui il seguente comando: [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Imposta il gruppo di risorse in cui desideri eseguire il provisioning dell'istanza. Esegui il seguente comando: [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    Per impostazione predefinita, è impostato il gruppo di risorse `default`.

4. Crea l'istanza. Esegui il comando [`ibmcloud resource service-instance-create`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_create):

    ```
    ibmcloud resource service-instance-create NAME logdna NOME_PIANO_SERVIZIO UBICAZIONE
    ```
    {: codeblock}

    Dove

    NOME è il nome dell'istanza.

    Il valore di *logdna* è il nome del servizio {{site.data.keyword.la_full_notm}} in {{site.data.keyword.cloud_notm}}.

    NOME_PIANO_SERVIZIO è il tipo di piano. I valori validi sono *lite*, *7-days*, *14-days*, *30-days*.
    
    UBICAZIONE è la regione in cui viene creata l'istanza LogDNA. I valori validi sono *us-south*, *eu-de*.

    Ad esempio, per eseguire il provisioning di un'istanza con il piano di conservazione di 7 giorni, esegui questo comando:

    ```
    ibmcloud resource service-instance-create logdna-instance-01 logdna 7-day us-south
    ```
    {: codeblock}




