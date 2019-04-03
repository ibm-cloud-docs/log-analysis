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

# Analisi dei log in Kibana utilizzando le visualizzazioni 
{:#kibana_visualizations}

Utilizza la pagina *Visualizza* in Kibana per creare visualizzazioni come grafici e tabelle che puoi utilizzare per analizzare i tuoi dati di log e confrontare i risultati. 
{:shortdesc}

Puoi utilizzare una visualizzazione individualmente per analizzare i tuoi log. 

* Puoi creare le visualizzazioni da una ricerca che definisci e salvi nella pagina *Rileva* o da una nuova query che definisci nella pagina *Visualizza*. La ricerca definisce la sottoserie di dati presentata da una visualizzazione.

* Il tipo di visualizzazione che scegli determina come i dati sono visualizzati per l'analisi.

La seguente tabella elenca i diversi tipi di visualizzazione:

| Tipo di visualizzazione | Descrizione |
|-----------------------|-------------|
| Grafico ad aree | Visualizza i dati quantitativi graficamente. Utilizza per confrontare due o più serie di dati aggregati. |
| Tabella dati | Visualizza i dati non elaborati in formato tabulare per un'aggregazione composta. |
| Grafico a linee | Visualizza i dati basati sul tempo. Utilizza per confrontare due o più serie di dati aggregati basati sul tempo. |
| Widget Markdown | Utilizza per visualizzare le informazioni di testo. |
| Metrica | Utilizza per visualizzare il numero di riscontri o la media esatta in un campo numerico. |
| Grafico a torta | Utilizza per visualizzare differenti valori di un campo. | 
| Grafico a barre verticali | Visualizza i dati basati sul tempo e non basati sul tempo. Utilizza per raggruppare i dati. |
{: caption="Tabella 1. Tipi di visualizzazione" caption-side="top"}

Nella pagina Visualizza, puoi eseguire tutte le seguenti attività:

| Attività | Ulteriori informazioni |
|------|------------------|
| [Creare una nuova visualizzazione](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#create) | Puoi creare le visualizzazioni da una ricerca che definisci e salvi nella pagina *Rileva* o da una nuova query che definisci nella pagina *Visualizza*. |
| [Eliminare una visualizzazione](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#delete) | Elimina le visualizzazioni non richieste. |
| [Esportare una visualizzazione](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#export) | Puoi esportare una visualizzazione come un file JSON.  |
| [Importare una visualizzazione](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#import1) | Puoi importare una visualizzazione come un file JSON.  |
| [Caricare una visualizzazione](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#reload2) | Puoi caricare una visualizzazione per aggiornarne i dati, modificarla o analizzare i dati. |
| [Salvare una visualizzazione](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#save2) | Puoi salvare le visualizzazioni per un riutilizzo successivo. |
{: caption="Tabella 2. Attività per lavorare con le visualizzazioni" caption-side="top"}


## Creazione di visualizzazioni da query in Kibana
{: #create}

Completa la seguente procedura per creare una visualizzazione dalla pagina Visualizza:

1. Avvia Kibana e seleziona la pagina **Visualizza**.

2. Scegli un tipo di visualizzazione, ad esempio, *tabella*.

3. Seleziona una visualizzazione salvata precedentemente da **O da una ricerca salvata** o seleziona un indice dalla sezione **Da una nuova ricerca, seleziona indice**.

4. Configura la query.

    * Se selezioni **O da una ricerca salvata**, seleziona una query di ricerca. La query viene utilizzata per richiamare i dati utilizzati per la visualizzazione. 
	
	    Dopo aver selezionato una ricerca, viene aperto il builder della visualizzazione e vengono caricati i dati per la query selezionata. 
		
		**Nota**: tutte le modifiche che effettui a una ricerca salvata vengono automaticamente riportate nella visualizzazione. Per disabilitare gli aggiornamenti automatici che esegui alla query collegata a questa visualizzazione, fai doppio clic sul messaggio *Questa visualizzazione è collegata a una ricerca salvata: tuo_nome_ricerca* 

    * Se selezioni **Da una nuova ricerca, seleziona indice**, definisci una nuova query. La query viene utilizzata per definire la sottorete di dati richiamati e utilizzati dalla visualizzazione.

        Per ulteriori informazioni, vedi [Filtro dei log definendo query personalizzate](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#define_search).

Per ulteriori informazioni sulle applicazioni Kibana, vedi la [ ![Icona link esterno](../../../icons/launch-glyph.svg "Icona link esterno")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}.


## Eliminazione di una visualizzazione
{: #delete}

Per eliminare una visualizzazione, completa la seguente procedura nella pagina **Gestione**:

1. Nella pagina **Gestione**, seleziona **Oggetti salvati**.

2. Nella scheda **Visualizzazioni**, seleziona le visualizzazioni che desideri eliminare.

3. Fai clic su **Elimina**.


## Esportazione di una visualizzazione
{: #export1}

Per esportare una visualizzazione come un file JSON, completa la seguente procedura nella pagina **Gestione**:

1. Nella pagina **Gestione**, seleziona **Oggetti salvati**.

2. Nella scheda **Visualizzazioni**, seleziona la visualizzazione che desideri esportare.

3. Fai clic su **Esporta**.

4. Salva il file.

## Importazione di una visualizzazione
{: #import1}

Per importare una visualizzazione come un file JSON, completa la seguente procedura nella pagina **Gestione**:

1. Nella pagina **Gestione**, seleziona **Oggetti salvati**.

2. Nella scheda **Visualizzazioni**, seleziona **Importa**.

3. Seleziona un file e fai clic su **Apri**.

La visualizzazione viene aggiunta all'elenco delle visualizzazioni.


 
## Caricamento di una visualizzazione
{: #reload2}

Completa la seguente procedura per caricare una visualizzazione salvata:

1. Nella barra degli strumenti della pagina Visualizza, fai clic su **Apri**.

2. Seleziona la visualizzazione che desideri caricare. 


## Salvataggio di una visualizzazione
{: #save2}

Completa la seguente procedura per salvare una visualizzazione nella pagina Visualizza:

1. Nella barra degli strumenti della pagina Visualizza, fai clic su **Salva**.

2. Immetti un nome per la visualizzazione.

3. Fai clic su Salva. 


