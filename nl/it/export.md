---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, export logs

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

 
# Esportazione dei log in un file locale
{: #export}

Puoi esportare i dati di log in formato JSONL da un'istanza {{site.data.keyword.la_full_notm}} in un file locale. Puoi esportare i log in modo programmatico oppure dall'IU web IBM Log Analysis. 
{:shortdesc}

Quando esporti i dati di log, tieni conto delle seguenti informazioni:
* Esporti un insieme di voci di log. Per definire l'insieme di dati che desideri esportare, puoi applicare filtri e ricerche. Puoi anche specificare l'intervallo di tempo. 
* Dall'IU web, quando esporti i log, ottieni una email che viene inviata al tuo indirizzo email con un link a un file compresso che include i dati. Per ottenere i dati, devi fare clic sul link e scaricare il file compresso.
* Quando esporti i log in modo programmatico, puoi scegliere di inviare una email o di indirizzare il flusso dei log al tuo terminale.
* Il file di log compresso che contiene i dati che desideri esportare è disponibile per un massimo di 48 ore. 
* Il numero massimo di righe che puoi esportare è 10.000.



## Esportazione dei log dall'IU web
{: #ui}

Per esportare i dati di log, completa la seguente procedura:

1. Fai clic sull'icona **Views** ![icona Configuration](images/views.png).
2. Seleziona **Everything** oppure una vista.
3. Applica un intervallo di tempo, i filtri e i criteri di ricerca fino a quando non vedi le voci di log che desideri esportare.
4. Fai clic su **Unsaved View** se stai iniziando dalla vista **Everything**. Fai clic sul nome della tua vista, se hai selezionato una vista nel passo precedente.
5. Seleziona `Export lines`. Viene visualizzata una nuova finestra.
6. Controlla l'intervallo di tempo. Se hai bisogno di modificarlo, fai clic sull'intervallo di tempo predefinito nel campo Change the *Time Range for export*.
7. Seleziona **Prefer newer lines** o **Prefer older lines** nel caso in cui la richiesta di esportazione superi il limite di righe.
8. Controlla la tua email. Ricevi una mail da **LogDNA** con un link per scaricare le righe esportate.


## Esportazione dei log in modo programmatico utilizzando l'API
{: #api}

Per esportare i log in modo programmatico, completa la seguente procedura:

1. Genera una chiave di servizio. 

    **Nota:** per completare questo passo, devi disporre del ruolo **gestore** per il servizio o l'istanza {{site.data.keyword.la_full_notm}}. Per ulteriori informazioni, vedi [Concessione delle autorizzazioni per gestire i log e configurare gli avvisi in LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna).

    1. Avvia l'IU web {{site.data.keyword.la_full_notm}}. Per ulteriori informazioni, vedi il documento relativo all'[accesso all'IU web {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

    2. Seleziona l'icona **Configuration** ![Icona Configuration](images/admin.png). Seleziona quindi **Organization**. 

    3. Seleziona **API keys**.

        Puoi visualizzare le chiavi di servizio create. 

    4. Fai clic su **Generate Service Key**.

        Una nuova chiave viene aggiunta all'elenco. Copia questa chiave.

2. Esporta i log. Esegui il seguente comando cURL:

    ```
    curl "ENDPOINT/v1/export?PARAMETRI:QUERY" -u CHIAVE_DI_SERVIZIO:
    ```
    {: codeblock}

    Dove 

    * *ENDPOINT* rappresenta il punto di ingresso del servizio. Ogni regione ha un URL differente.
    * PARAMETRI_QUERY sono i parametri che definiscono i criteri di filtro applicati alla richiesta di esportazione.
    * CHIAVE_DI_SERVIZIO è la chiave che hai creato nel passo precedente.

La seguente tabella elenca gli endpoint per ogni regione:

| Regione         | Endpoint                                             | 
|----------------|------------------------------------------------------|
| `Us-south`       | `https://api.us-south.logging.cloud.ibm.com `        |
{: caption="Endpoint per ogni regione" caption-side="top"} 


La seguente tabella elenca i parametri di query che puoi impostare:

| Parametro di query | Tipo       | Stato     | Descrizione |
|-----------|------------|------------|-------------|
| `from`      | `int32`      | Richiesto   | Ora di inizio. Imposta come data/ora UNIX in secondi o millisecondi. |
| `to`        | `int32`      | Richiesto   | Ora di fine. Imposta come data/ora UNIX in secondi o millisecondi.    |
| `size`      | `string`     | Facoltativo   | Numero di righe di log da includere nell'esportazione.  | 
| `hosts`     | `string`     | Facoltativo   | Elenco separato da virgole di host. |
| `apps`      | `string`     | Facoltativo   | Elenco separato da virgole di applicazioni. |
| `levels`    | `string`     | Facoltativo   | Elenco separato da virgole di livelli di log. |
| `query`     | `string`     | Facoltativo   | Query di ricerca. Per ulteriori informazioni, vedi [Cerca nei log](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6). |
| `prefer`    | `string`     | Facoltativo   | Definisce le righe di log che desideri esportare. I valori validi sono `head`, prime righe del log, e `tail`, ultime righe del log. Se non viene specificato, per impostazione predefinita viene utilizzato tail.  |
| `email`     | `string`     | Facoltativo   | Specifica l'email con il link scaricabile della tua esportazione. Per impostazione predefinita, le righe di log sono inviate in flusso.|
| `emailSubject` | `string`     | Facoltativo   | Utilizzalo per impostare l'oggetto della email. </br>Utilizza `%20` per rappresentare uno spazio. Un valore di esempio può essere `Export%20logs`. |
{: caption="Parametri di query" caption-side="top"} 

Ad esempio, per inviare in flusso le righe di log nel terminale, puoi eseguire questo comando:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info" -u e08c0c759663491880b0d61712346789:
```
{: screen}

Per inviare una email con il link per scaricare le righe di log specificate nell'esportazione, puoi eseguire questo comando:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=joe@ibm.com" -u e08c0c759663491880b0d61712346789:
```
{: screen}


Per inviare un'email con un oggetto personalizzato, puoi eseguire questo comando:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=lopezdsr@uk.ibm.com&emailSubject=Export%20test" -u e08c0c759663491880b0d61712346789:
```
{: screen}

