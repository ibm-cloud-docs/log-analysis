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

# Analisi dei log in Kibana tramite un dashboard
{:#analize_logs_dashboard}

Utilizza la pagina *Dashboard* in Kibana per visualizzare le raccolte di visualizzazioni raggruppate nei dashboard. Utilizza i dashboard per analizzare i tuoi dati di log e confrontare i risultati.
{:shortdesc}

In {{site.data.keyword.Bluemix}}, ci sono diversi tipi di dashboard che puoi definire e personalizzare per visualizzare e analizzare i dati. Ad esempio, la seguente tabella elenca alcuni tipi di dashboard comuni:

| Tipo di dashboard | Descrizione |
|-------------------|-------------|
| Dashboard a singola applicazione cf | Questo è un dashboard che mostra le informazioni per una singola applicazione Cloud Foundry. |
| Dashboard a singolo contenitore  | Questo è un dashboard che mostra le informazioni per un singolo contenitore.  |
| Dashboard del gruppo di contenitori  | Questo è un dashboard che mostra le informazioni per un gruppo di contenitori specifico.  |
| Dashboard a più applicazioni cf | Questo è un dashboard che mostra informazioni per tutte le applicazioni Cloud Foundry distribuite nello stesso spazio.  | 
| Dashboard a più contenitori | Questo è un dashboard che mostra informazioni per tutti i contenitori distribuiti nello stesso spazio.  |
| Dashboard spazio | Questo è un dashboard che mostra la registrazione dei dati disponibile in uno spazio.  | 
{: caption="Tabella 1. Esempi di tipi di dashboard" caption-side="top"}

Per visualizzare i dati in un dashboard, configura i pannelli. Kibana include diverse visualizzazioni, come tabella, tendenze e istogramma, che puoi utilizzare per analizzare le informazioni. Una visualizzazione viene aggiunta come un pannello a un dashboard. Puoi aggiungere, rimuovere e riorganizzare i pannelli nel dashboard. Ogni pannello ha un obiettivo diverso. Alcuni pannelli sono organizzati in righe che forniscono i risultati di una o più query. Altri pannelli visualizzano documenti o informazioni personalizzate. Ogni pannello si basa su una ricerca. La ricerca definisce la sottoserie di dati che visualizza il pannello. Ad esempio, puoi configurare un grafico a barre, un grafico a torta o una tabella per visualizzare i dati e analizzarli.  

La seguente tabella elenca diverse attività che puoi eseguire nella pagina Dashboard:

| Attività | Ulteriori informazioni |
|------|------------------|
| [Aggiungere una visualizzazione](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#add_visualization) | Puoi aggiungere una ricerca o una visualizzazione esistente a un dashboard.|
| [Creare un nuovo dashboard](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#new) | Puoi creare più dashboard. Ogni dashboard può essere progettato per includere diverse ricerche, visualizzazioni e una sottorete di dati di log differente.  |
| [Eliminare un dashboard](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#delete) | Eliminare i dashboard che non sono richiesti. |
| [Esportare un dashboard](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#export) | Puoi esportare un dashboard come un file JSON. |
| [Importare un dashboard](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#import) | Puoi importare un dashboard come un file JSON. |
| [Caricare un dashboard](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#reload3) | Puoi caricare un dashboard per aggiornarne i dati, modificarlo o analizzare i dati. |
| [Salvare un dashboard](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#save) | Puoi salvare un dashboard per un riutilizzo successivo. |
{: caption="Tabella 2. Attività per lavorare con i dashboard" caption-side="top"}

Per ulteriori informazioni sulle applicazioni Kibana, vedi la [ ![Icona link esterno](../../../icons/launch-glyph.svg "Icona link esterno")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}.


## Aggiunta di una nuova ricerca o visualizzazione
{: #add_visualization}

Completa la seguente procedura per aggiungere una ricerca o una visualizzazione esistente:

1. Nella barra degli strumenti della pagina Dashboard, fai clic su **Aggiungi**. 

    **Nota**: puoi aggiungere visualizzazioni e ricerche. 

2. Seleziona la scheda **Visualizzazioni** per aggiungere una visualizzazione o seleziona la scheda **Ricerche** per aggiungere una ricerca.

3. Fai clic sulla ricerca o visualizzazione che desideri aggiungere.

    Viene aggiunto un pannello per questa ricerca o visualizzazione al dashboard.

	
## Creazione di un nuovo dashboard Kibana
{: #new}

Per creare un nuovo dashboard completa la seguente procedura:

1. Nella barra degli strumenti della pagina Dashboard, fai clic su **Aggiungi**. 

2. Aggiungi una o più ricerche o visualizzazioni. Per ulteriori informazioni, vedi [Aggiunta di una nuova ricerca o visualizzazione](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#add_visualization).

    Dopo aver aggiunto una ricerca o una visualizzazione, viene aggiunto un pannello al dashboard.

3. Trascina e rilascia un pannello nella parte del dashboard in cui desideri posizionarlo.
 
4. Salva il dashboard per un riutilizzo successivo. Per maggiori informazioni, vedi [Salvataggio di un dashboard Kibana ](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#save).


## Eliminazione di un dashboard Kibana
{: #delete1}

Per eliminare un dashboard, completa le seguenti istruzioni nella pagina **Gestione**:

1. Nella pagina **Gestione**, seleziona **Oggetti salvati**.

2. Nella scheda **Dashboard**, seleziona il dashboard che desideri eliminare.

3. Fai clic su **Elimina**.

## Esportazione di un dashboard Kibana
{: #export}

Per esportare un dashboard come un file JSON, completa la seguente procedura nella pagina **Gestione**:

1. Nella pagina **Gestione**, seleziona **Oggetti salvati**.

2. Nella scheda **Dashboard**, seleziona il dashboard che desideri esportare.

3. Fai clic su **Esporta**.

4. Salva il file.

## Importazione di un dashboard Kibana
{: #import}

Per importare un dashboard come un file JSON, completa la seguente procedura nella pagina **Gestione**:

1. Nella pagina **Gestione**, seleziona **Oggetti salvati**.

2. Nella scheda **Dashboard**, seleziona **Importa**.

3. Seleziona un file e fai clic su **Apri**.

Il dashboard viene aggiunto all'elenco dei dashboard.

## Caricamento di un dashboard Kibana
{: #reload3}

Completa la seguente procedura per caricare un dashboard salvato:

1. Nella barra degli strumenti della pagina Dashboard, fai clic su **Apri**.

2. Seleziona un dashboard dell'elenco dei dashboard disponibili visualizzato nel campo *Nome*.

Puoi anche ricercare un dashboard dalla barra di ricerca.

## Salvataggio di un dashboard Kibana
{: #save}

Completa la seguente procedura per salvare un dashboard Kibana dopo averlo personalizzato:

1. Nella barra degli strumenti, fai clic su **Salva**.

2. Immetti un nome per il dashboard.

    **Nota:** il nome non deve contenere spazi.

3. Fai clic su **Salva**.




