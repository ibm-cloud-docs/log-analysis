---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, web UI, browser

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

# Accesso all'IU web
{: #launch}

Dopo che hai eseguito il provisioning di un'istanza del servizio {{site.data.keyword.la_full_notm}} in {{site.data.keyword.cloud_notm}}, e hai configurato un agent LogDNA per un'origine dati di log, puoi visualizzare, monitorare e gestire i log mediante l'IU web {{site.data.keyword.la_full_notm}}.
{:shortdesc}


## Concessione di politiche IAM a un utente per visualizzare i dati 
{: #step1}

**Nota:** devi essere un amministratore del servizio {{site.data.keyword.la_full_notm}}, un amministratore di un'istanza {{site.data.keyword.la_full_notm}} o disporre delle autorizzazioni IAM dell'account per concedere politiche ad altri utenti.

La seguente tabella elenca le politiche minime di cui un utente deve disporre per potere avviare l'IU web e visualizzare i dati:

| Servizio                              | Ruolo                      | Autorizzazione concessa       |
|--------------------------------------|---------------------------|---------------------|
| `{{site.data.keyword.la_full_notm}}` | Ruolo della piattaforma: Visualizzatore     | Consente all'utente di visualizzare l'elenco di istanze del servizio nel dashboard di registrazione Osservabilità. |
| `{{site.data.keyword.la_full_notm}}` | Ruolo del servizio: Scrittore      | Consente all'utente di avviare l'IU web e di visualizzare i log nell'IU web    |
{: caption="Tabella 1. Politiche IAM" caption-side="top"} 

Per ulteriori informazioni su come configurare queste politiche per un utente, vedi [Concessione di autorizzazioni a un utente per visualizzare i log](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna).


## Avvio dell'IU web mediante l'IU {{site.data.keyword.cloud_notm}}
{: #launch_step2}

Avvii l'IU web nel contesto di un'istanza {{site.data.keyword.la_full_notm}}, dall'IU {{site.data.keyword.cloud_notm}}. 

Per avviare l'IU web, completa la seguente procedura:

1. Accedi al tuo account {{site.data.keyword.cloud_notm}}.

    Fai clic sul [dashboard {{site.data.keyword.cloud_notm}} ![Icona link esterno](../../icons/launch-glyph.svg "Icona link esterno")](https://cloud.ibm.com/login){:new_window} per avviare il dashboard {{site.data.keyword.cloud_notm}}.

	Dopo che hai effettuato l'accesso con i tuoi ID utente e password, viene aperto il dashboard {{site.data.keyword.cloud_notm}}.

2. Nel menu di navigazione, seleziona **Osservabilità**. 

3. Seleziona **Registrazione**. 

    Viene visualizzato l'elenco delle istanze disponibili in {{site.data.keyword.cloud_notm}}.

4. Seleziona una singola istanza. Fai quindi clic su **Visualizza LogDNA**.

L'IU web viene aperta.


## Ottenimento dell'URL dell'IU web da {{site.data.keyword.cloud_notm}}
{: #launch_get}

Per ottenere l'URL dell'IU web, completa la seguente procedura da un terminale:

1. Imposta il gruppo di risorse dove viene eseguito il provisioning dell'istanza {{site.data.keyword.la_full_notm}}.

    ```
    export logdna_rg_name=<nome_del_gruppo_di_risorse_dove_viene_creata_la_istanza_logDNA>
    ```
    {: codeblock}

2. Imposta il nome dell'istanza {{site.data.keyword.la_full_notm}}.

    ```
    export logdna_instance_name=<il_tuo_nome_della_istanza_LogDNA>
    ```
    {: codeblock}

3. Imposta l'endpoint.

    ```
    export rc_endpoint=resource-controller.cloud.ibm.com
    ```
    {: codeblock}

4. Imposta il token IAM.

    ```
    export iam_token=$(ibmcloud iam oauth-tokens | grep IAM | grep -oP  "eyJ.*")
    ```
    {: codeblock}

    **Nota:** se stai lavorando su un terminale MacOS, il comando è il seguente: `export iam_token=$(ic iam oauth-tokens | grep IAM | grep -o  "eyJ.*")`

5. Imposta l'ID del gruppo di risorse.

    ```
    export resource_group_id=$(ibmcloud resource groups | grep "^$logdna_rg_name" | awk '{print $2}')
    ```
    {: codeblock}

6. Imposta l'URL dell'IU web in una variabile.

    ```
    export dashboard_url=$(curl -H "Accept: application/json" -H "Authorization: Bearer $iam_token" "https://$rc_endpoint/v1/resource_instances?resource_group_id=$resource_group_id&type=service_instance" | jq ".resources[] | select(.name==\"$logdna_instance_name\") | .dashboard_url")
    ```
    {: codeblock}

7. Ottieni l'URL dell'IU web.

    ```
    echo $dashboard_url
    ```
    {: codeblock}

    

