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


# Messaggi di errore
{: #error_msgs}

Potresti vedere questi messaggi di errore quando utilizzi il servizio {{site.data.keyword.loganalysisshort}} su {{site.data.keyword.Bluemix}}:
{:shortdesc}

## BXNLG020001W
{: #BXNLG020001W}

**Descrizione del messaggio**

Hai raggiunto la quota giornaliera allocata allo spazio Bluemix (GUID spazio) per l'istanza {{site.data.keyword.loganalysisfull}} {GUID istanza}. La tua assegnazione giornaliera corrente è 500MB per l'archiviazione Ricerca dei log, che è conservata nell'archiviazione Ricerca dei log per un periodo di 3 giorni, durante il quale può essere cercata in Kibana. Per eseguire l'upgrade del tuo piano in modo che tu possa archiviare ulteriori dati nell'archiviazione Ricerca dei log al giorno, e conservare anche tutti i log nell'archiviazione Raccolta dei log, esegui l'upgrade al piano di servizio {{site.data.keyword.loganalysisshort}} per questo spazio. Per ulteriori informazioni su piani di servizio e su come eseguire l'upgrade del tuo piano, vedi [Piani](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).


**Spiegazione del messaggio** 

Puoi ottenere un messaggio con l'ID *BXNLG020001W* quando raggiungi la quota di archiviazione Ricerca dei log allocata per il piano del servizio Lite. Il piano Lite è il piano di servizio gratuito impostato per impostazione predefinita quando esegui il provisioning del servizio {{site.data.keyword.loganalysisshort}} in uno spazio. La tua assegnazione giornaliera corrente è 500MB per l'archiviazione Ricerca dei log, che è conservata nell'archiviazione Ricerca dei log per un periodo di 3 giorni, durante il quale può essere cercata in Kibana.

**Ripristino**

Per eseguire l'upgrade del tuo piano in modo che tu possa archiviare ulteriori dati nell'archiviazione Ricerca dei log al giorno, e conservare anche tutti i log nell'archiviazione Raccolta dei log, esegui l'upgrade al piano di servizio {{site.data.keyword.loganalysisshort}} per questo spazio. Per ulteriori informazioni su piani di servizio e su come eseguire l'upgrade del tuo piano, vedi [Piani](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).


## BXNLG020002W 
{: #BXNLG020002W}


**Descrizione del messaggio**

Hai raggiunto la quota giornaliera allocata allo spazio Bluemix (GUID spazio) per l'istanza {{site.data.keyword.loganalysisfull}} {GUID istanza}.  La tua assegnazione giornaliera corrente è XXX per l'archiviazione Ricerca dei log, che è conservata per un periodo di 3 giorni, durante il quale può essere cercata in Kibana. Questo non influenza la tua politica di conservazione dei log nell'archiviazione Raccolta dei log. Per eseguire l'upgrade del tuo piano in modo da poter archiviare ulteriori dati nell'archiviazione Ricerca dei log al giorno, esegui l'upgrade del piano di servizio {{site.data.keyword.loganalysisshort}} per questo spazio. Per ulteriori informazioni su piani di servizio e su come eseguire l'upgrade del tuo piano, vedi [Piani](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).

XXX rappresenta la dimensione dei dati ricercabili per il tuo piano corrente.

**Spiegazione del messaggio** 

Hai raggiunto la quota giornaliera allocata allo spazio (GUID spazio) per l'istanza {{site.data.keyword.loganalysisfull}} {GUID istanza}.  La tua assegnazione giornaliera corrente è 500MB, 2 GB, 5 GB o 10 GB per l'archiviazione Ricerca dei log, che viene conservata per un periodo di 3 giorni, durante il quale può essere cercata in Kibana. Questo non influenza la tua politica di conservazione dei log nell'archiviazione Raccolta dei log.

**Ripristino**

Per eseguire l'upgrade del tuo piano in modo da poter archiviare ulteriori dati nell'archiviazione Ricerca dei log al giorno, esegui l'upgrade del piano di servizio {{site.data.keyword.loganalysisshort}} per questo spazio. Per ulteriori informazioni su piani di servizio e su come eseguire l'upgrade del tuo piano, vedi [Piani](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).




