---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging instance, delete

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

# Rimozione di un'istanza
{: #remove}

Puoi rimuovere un'istanza del servizio {{site.data.keyword.la_full_notm}} dall'IU {{site.data.keyword.Bluemix}} o dalla riga di comando.
{:shortdesc}

Quando rimuovi un'istanza da {{site.data.keyword.cloud_notm}}, ripulisci completando le seguenti attività:

1. Annota l'elenco di origini che inoltrano metriche all'istanza {{site.data.keyword.la_full_notm}} che desideri rimuovere. Devi rimuovere l'agent LogDNA da ogni origine.
2. Rimuovi le autorizzazioni concesse agli utenti per lavorare con l'istanza. 

    Se gestisci l'accesso utilizzando gruppi di accesso dedicati per lavorare con una specifica istanza, devi rimuovere questi gruppi di accesso.

    Se gestisci l'accesso a più istanze di registrazione utilizzando i gruppi di accesso, devi rimuovere le politiche che concedono le autorizzazioni all'istanza che desideri rimuovere.
    
    Se concedi singole politiche agli utenti, devi raccogliere l'elenco di utenti che dispongono delle autorizzazioni per lavorare con tale istanza. Quindi, per ciascun utente che identifichi, devi rimuovere le politiche correlate all'istanza che desideri eliminare.


Elimina quindi l'istanza dal dashboard {{site.data.keyword.cloud_notm}}.


## Rimozione di un'istanza mediante l'IU {{site.data.keyword.cloud_notm}}
{: #remove_ui}

Per rimuovere un'istanza di {{site.data.keyword.la_full_notm}} utilizzando l'IU {{site.data.keyword.cloud_notm}}, completa la seguente procedura:

1. Accedi al tuo account {{site.data.keyword.cloud_notm}}.

    Fai clic sul [dashboard {{site.data.keyword.cloud_notm}} ![Icona link esterno](../../icons/launch-glyph.svg "Icona link esterno")](https://cloud.ibm.com/login){:new_window} per avviare il dashboard {{site.data.keyword.cloud_notm}}.

	Dopo che hai eseguito l'accesso con il tuo ID utente e la tua password, viene aperta l'IU {{site.data.keyword.cloud_notm}}.

2. Vai all'icona di menu ![icona di menu ](../../icons/icon_hamburger.svg) &gt; **Osservabilità** per accedere al dashboard *Osservabilità*.

3. Seleziona **Registrazione**. Viene visualizzato l'elenco delle istanze di registrazione.

4. Seleziona l'istanza che desideri eliminare.

5. Dal menu *Azione*, seleziona **Rimuovi**.


## Rimozione di un'istanza mediante la CLI
{: #remove_cli}

Per rimuovere un'istanza di {{site.data.keyword.la_full_notm}} mediante la riga di comando, completa la seguente procedura:

1. [Prerequisito] Installazione della CLI {{site.data.keyword.cloud_notm}}.

   Per ulteriori informazioni, vedi [Installazione della CLI {{site.data.keyword.cloud_notm}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli).

   Se la CLI è installata, continua con il passo successivo.

2. Accedi alla regione in {{site.data.keyword.cloud_notm}} dove desideri eseguire il provisioning dell'istanza. Esegui il seguente comando: [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Imposta il gruppo di risorse in cui viene eseguito il provisioning dell'istanza. Esegui il seguente comando: [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    Per impostazione predefinita, è impostato il gruppo di risorse *default*.

4. Rimuovi l'istanza. Esegui il comando [`ibmcloud resource service-instance-delete`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_delete):

    ```
    ibmcloud resource service-instance-delete NOME 
    ```
    {: codeblock}

    Dove NOME è il nome dell'istanza.

    Ad esempio, per rimuovere un'istanza, esegui questo comando:

    ```
    ibmcloud resource service-instance-delete logdna-instance-01
    ```
    {: codeblock}



