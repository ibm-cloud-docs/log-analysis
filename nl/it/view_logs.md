---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, logs

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

# Visualizzazione dei log
{: #view_logs}

Dopo che hai eseguito il provisioning di un'istanza del servizio {{site.data.keyword.la_full_notm}} in {{site.data.keyword.cloud_notm}}, e hai configurato un agent LogDNA per un'origine log, puoi visualizzare, monitorare e gestire i dati di log mediante l'IU web {{site.data.keyword.la_full_notm}}.
{:shortdesc}

Quando avvii l'IU web {{site.data.keyword.la_full_notm}}, le voci di log sono visualizzate con un formato predefinito. Nella sezione **User Preferences** puoi modificare la modalità di visualizzazione delle informazioni in ciascuna riga di log. Puoi anche filtrare i log e modificare le impostazioni di ricerca e contrassegnare quindi con un segnalibro il risultato come una *vista*. Puoi collegare, o scollegare, uno o più avvisi a, o da, una vista. Puoi definire un formato personalizzato per la modalità di visualizzazione delle righe nella vista. Puoi espandere una riga di log e visualizzare i dati analizzati.


Per visualizzare i log, completa la seguente procedura:


## Passo 1. Concedi le politiche IAM a un utente per visualizzare i log
{: #view_logs_step1}

**Nota:** devi essere un amministratore del servizio {{site.data.keyword.la_full_notm}}, un amministratore dell'istanza {{site.data.keyword.la_full_notm}} o disporre delle autorizzazioni IAM dell'account per concedere politiche ad altri utenti.

La seguente tabella elenca le politiche minime di cui un utente deve disporre per poter avviare l'IU web {{site.data.keyword.la_full_notm}} e visualizzare i log:

| Servizio                        | Ruolo                      | Autorizzazione concessa            |
|--------------------------------|---------------------------|-------------------------------|  
| `{{site.data.keyword.la_full_notm}} ` | Ruolo della piattaforma: Visualizzatore     | Consente all'utente di visualizzare l'elenco di istanze del servizio nel dashboard di registrazione Osservabilità. |
| `{{site.data.keyword.la_full_notm}} ` | Ruolo del servizio: Lettore      | Consente all'utente di avviare l'IU web e di visualizzare i log nell'IU web  |
{: caption="Tabella 1. Politiche IAM" caption-side="top"} 

Per ulteriori informazioni su come configurare queste politiche per un utente, vedi [Concessione a un utente delle autorizzazioni per visualizzare i log in LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna).


## Passo 2. Vai all'IU web mediante l'IU {{site.data.keyword.cloud_notm}}
{: #view_logs_step2}

Per avviare l'IU {{site.data.keyword.la_full_notm}} mediante l'IU {{site.data.keyword.cloud_notm}}, completa la seguente procedura:

1. Accedi al tuo account {{site.data.keyword.cloud_notm}}.

    Fai clic sul [dashboard {{site.data.keyword.cloud_notm}} ![Icona link esterno](../../icons/launch-glyph.svg "Icona link esterno")](https://cloud.ibm.com/login){:new_window} per avviare il dashboard {{site.data.keyword.cloud_notm}}.

	Dopo che hai effettuato l'accesso con i tuoi ID utente e password, viene aperto il *dashboard* {{site.data.keyword.cloud_notm}}.

2. Nel menu di navigazione, seleziona **Osservabilità**. 

3. Seleziona **Registrazione**. 

    Viene visualizzato l'elenco delle istanze {{site.data.keyword.la_full_notm}} disponibili in {{site.data.keyword.cloud_notm}}.

4. Seleziona una singola istanza. Fai quindi clic su **Visualizza LogDNA**.

Viene aperta l'IU web {{site.data.keyword.la_full_notm}} che visualizza i log inoltrati a tale istanza.


## Passo 3. Personalizza la tua vista predefinita
{: #view_logs_step3}

Nella sezione **USER PREFERENCES**, puoi modificare l'ordine dei campi di dati visualizzati per ogni riga.

Per modificare il formato di una riga di log, completa la seguente procedura:

1. Seleziona l'icona **Configuration** ![Icona Configuration](images/admin.png "Icona Admin").
2. Seleziona **USER PREFERENCES**. Viene visualizzata una nuova finestra.
3. Seleziona **Log Format**.
4. Modifica la sezione *Line Format* in modo che corrisponda ai tuoi requisiti. Trascina le caselle.


## Passo 4. Esamina una riga di log
{: #view_logs_step4}

In qualsiasi momento, puoi visualizzare ogni riga di log in contesto.

Completa la seguente procedura: 

1. Fai clic sull'icona **Views** ![Icona Configuration](images/views.png "Icona Configuration").
2. Seleziona **Everything** oppure una vista.
3. Identifica una riga nel log che desideri esplorare.
4. Espandi la riga di log. 

    Vengono visualizzate le informazioni su etichette, tag e identificativi riga.

5. Fai clic su **View in Context** per visualizzare la riga di log nel contesto delle altre righe di log da tale host, applicazione o entrambi.

6. Fai clic su **Copy to clipboard** per copiare il campo del messaggio negli appunti.

Quando hai finito, chiudi la riga.


## Passo 5. Filtra i log
{: #view_logs_step5}

Puoi filtrare i log in base a origine log, applicazione e livello di log. 

* Un'origine può essere un host, un computer, una macchina virtuale o un'applicazione Heroku.
* Un'applicazione rappresenta un file di log, un programma o un contenitore.
* Esempi di livelli di log sono: INFO, DEBUG, ERROR

Per filtrare i log, completa la seguente procedura:

1. Fai clic sull'icona **Views** ![Icona Configuration](images/views.png "Icona Configuration").
2. Seleziona **Everything** oppure una vista.
3. Espandi **All Tags** per visualizzare l'elenco delle tag identificate nei log. Scegli quindi quelle che desideri.
4. Espandi **All Sources** per visualizzare l'elenco delle origini log identificate nei log. Scegli quindi quelle che desideri.
5. Espandi **All Apps** per visualizzare l'elenco delle applicazioni identificate nei log. Scegli quindi quelle che desideri.
6. Espandi **All Levels** per visualizzare l'elenco dei livelli di log identificati nei log. Scegli quindi quelli che desideri.


**Nota:** in ciascuna sezione, puoi raggruppare più opzioni in un gruppo. Raggruppa tag, origini log, applicazioni e livelli di log per riutilizzare tali raggruppamenti quando filtri i dati di log in altre viste personalizzate.

Per creare un gruppo, seleziona più valori. Fai quindi clic su **Save as group**. Immetti un nome per il gruppo e salvalo.


## Passo 6. Cerca nei log
{: #view_logs_step6}

Quando cerchi i dati di log, la ricerca applica qualsiasi filtro di log e query di tempo configurati in tale vista.

Puoi eseguire delle semplici ricerche (ricerca di stringa di un singolo termine), una ricerca composta (più termini e operatori di ricerca), ricerche di campo se la riga di log può essere analizzata e altre ancora. Per ulteriori informazioni, vedi il documento relativo alla [modalità di ricerca dei log nei documenti LogDNA ![Icona link esterno](../../icons/launch-glyph.svg "Icona link esterno")](https://docs.logdna.com/docs/search){:new_window}.

**Nota:** gli operatori AND e OR sono sensibili a maiuscole/minuscole e devono essere scritti in maiuscolo.



## Passo 7. Crea le viste
{: #view_logs_step7}


Per creare una vista, completa la seguente procedura:

1. Fai clic sull'icona **Views** ![Icona Configuration](images/views.png "Icona Configuration").
2. Seleziona **Everything** oppure una vista.
3. Filtra i dati di log e fai quindi clic su **Save as new view / alert**.

    Viene aperta la pagina *Create new view*.

4. Immetti un nome per la vista nel campo *Name*.

5. Facoltativamente, aggiungi una categoria. Immetti un nome e fai quindi clic su **Add this as new view category**.

6. Facoltativamente, collega un avviso. Viene visualizzata una nuova sezione per consentirti di configurare l'avviso.

7. Fai clic su **Save View**


