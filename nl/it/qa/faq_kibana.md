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


# Domande frequenti (FAQ) per Kibana
{: #faq_kibana}

Queste sono le risposte alle domandi comuni sull'utilizzo delle funzionalità di registrazione {{site.data.keyword.Bluemix}}. {:shortdesc}

* [Cosa posso fare se non posso visualizzare i dati nella pagina Rileva in Kibana ](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#logging_qa_no_data_discover_kibana)
* [Cosa posso fare se ricevo un'eccezione di autenticazione ](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#logging_qa_no_data_dashboard_kibana)
* [Perché vedo il simbolo ? accanto ai campi nella pagina Rileva in Kibana](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#logging_qa_kibana_question)
* [Ottengo un errore 403 quando provo a modificare il modello di indice predefinito](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#error_403)
* [L'URL breve non funziona](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#short_url)
* [Posso cercare nei log del mio account in Bluemix?](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#acc_logs_1)


## Cosa posso fare se non posso visualizzare i dati nella pagina Rileva in Kibana
{: #logging_qa_no_data_discover_kibana}

Esistono vari scenari per cui potresti non visualizzare i dati in Kibana:

1. Quando avvii Kibana, potresti non visualizzare alcun dato nella pagine Rileva. Ricevi il seguente messaggio: **Nessun risultato trovato.**. 
2. Potresti star utilizzando la pagina Rileva in Kibana. Tuttavia, dopo un breve periodo di tempo, ricevi il messaggio: **Nessun risultato trovato.** quando tenti di eseguire un'attività in Kibana.

Per risolvere questo problema, completa la seguente procedura:

1. Controlla che il *Selezionatore di tempo* sia configurato nella pagina Rileva e aumenta il periodo di tempo. 

    **Nota**: per impostazione predefinita, in {{site.data.keyword.Bluemix_notm}}, il *Selezionatore di tempo* è configurato per mostrare i dati degli ultimi 15 minuti.

    Per ulteriori informazioni su come impostare il *Selezionatore di tempo*, vedi [Configurazione di un filtro temporale](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter1).
       
2. Fai clic sulla lente di ingrandimento ubicata nella barra di ricerca della pagina *Rileva*. I dati della pagina vengono aggiornati in base alla query di ricerca predefinita.

    In alternativa, puoi impostare un periodo di *Aggiornamento automatico*.

    **Nota**: per impostazione predefinita, in {{site.data.keyword.Bluemix_notm}}, il periodo di *Aggiornamento automatico* è impostato su **DISATTIVO**.
    
    Per ulteriori informazioni su come abilitarlo, vedi [Aggiornamento automatico dei dati](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_refresh_interval).



## Cosa posso fare se ricevo un'eccezione di autenticazione
{: #logging_qa_no_data_dashboard_kibana}

Quando non puoi visualizzare i dati nelle tue visualizzazioni in una pagina Dashboard e ricevi il messaggio di errore: **Errore: Eccezione di autorizzazione.**, controlla le tue autorizzazioni per visualizzare i dati in ogni visualizzazione.

Considera le seguenti informazioni:
Puoi configurare una o più visualizzazioni in una pagina Dashboard. Quando la pagina Dashboard effettua una richiesta per raccogliere i dati visualizzati tramite queste visualizzazioni, viene emessa solo una richiesta per tutte le visualizzazioni. Se non disponi delle autorizzazioni per visualizzare i dati per una delle visualizzazioni, l'intera richiesta ha esito negativo.

Per risolvere questo problema, completa la seguente procedura:

1. Identifica le visualizzazioni per cui non disponi delle autorizzazioni.

    1. Fai clic sull'icona *matita* di una visualizzazione nella pagina *Dashboard*. Viene aperta la visualizzazione nella pagina *Visualizza*. In alternativa, nella pagina *Visualizza*, carica una visualizzazione. 
    2. Verifica di poter visualizzare i dati.
    
    Ripeti questi passi per ogni visualizzazione.

2. Richiedi l'accesso per visualizzare i dati per le visualizzazioni all'amministratore cloud.

3. Crea una nuova pagina Dashboard che esclude le visualizzazioni per cui non hai le autorizzazioni mentre hai concesso l'accesso a visualizzare i dati per le visualizzazioni che stanno provocando il problema. 

    Se condividi il Dashboard, non eliminare le visualizzazioni finché questo problema impedirà ad altri membri del team di utilizzare lo stesso dashboard.



## Perché vedo il simbolo ? accanto ai campi nella pagina Rileva in Kibana
{: #logging_qa_kibana_question}

Quando apri la pagina Rileva in Kibana, potresti vedere un punto interrogativo `?` accanto ai campi elencati nella sezione dei campi disponibili invece del carattere `t`. Quando ricarichi l'elenco di campo, il tipo di campi viene analizzato e il punto interrogativo `?` viene sostituito dal carattere `t`. Per ulteriori informazioni, vedi [Ricaricamento dell'elenco dei campi](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_reload_fields).


## Ottengo un errore 403 quando provo a modificare il modello di indice predefinito
{: #error_403}

Non è possibile modificare il modello di indice predefinito. 

Se provi a impostare un modello di indice differenze come nuovo valore predefinito, ottieni il seguente errore: `Configurazione: Errore 403 Non consentito`

## L'URL breve non funziona
{: #short_url}

La condivisione di una ricerca, di una visualizzazione o di un dashboard non è supportata. Pertanto, non funzioneranno neanche gli URL brevi per un oggetto Kibana che vuoi condividere. 

## Posso cercare nei log del mio account in Bluemix?
{: #acc_logs_1}

In qualità di proprietario di un account, puoi cercare nei log del tuo account e analizzarli.

Completa la seguente procedura per visualizzare i log del tuo account:

1. [Avvia Kibana.](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser) Ad esempio, per la regione Stati Uniti Sud, utilizza l'URL `https://logging.ng.bluemix.net`,

2. Seleziona l'opzione **Visualizza i log dell'account NomeAccount** per visualizzare i log dell'account. *NomeAccount* è il nome dell'account.

