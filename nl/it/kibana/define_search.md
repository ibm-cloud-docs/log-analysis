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

# Definizione di query di ricerca personalizzate
{:#define_search}

Nella barra di ricerca della pagina Rileva, puoi definire e salvare le query di ricerca utilizzando il linguaggio di query Lucene. Per ogni ricerca, puoi applicare i filtri per restringere le voci disponibili per l'analisi.
{:shortdesc}

Completa le seguenti attività per definire una ricerca personalizzata:

1. Avvia Kibana.

    Per le applicazioni CF (Cloud Foundry), vedi [avvia Kibana dal dashboard di un'applicazione CF](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_cf_app).

	Per i contenitori che vengono eseguiti nell'infrastruttura gestita da {{site.data.keyword.Bluemix_notm}}, vedi [Avvia Kibana dal dashboard di un contenitore](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_for_containers).
    
    Per tutte le risorse cloud, ad esempio i contenitori in esecuzione in un cluster Kubernetes, vedi [avvia Kibana dal browser](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser). 
	
	Quando accedi a Kibana, viene applicata la ricerca predefinita. Puoi visualizzare i log per l'elenco di istanza della risorsa di cui stai eseguendo la query. Puoi filtrare i log per ognuna delle risorse {{site.data.keyword.Bluemix_notm}} in tale spazio.

2. Guarda nella pagina Rileva per visualizzare quale sottorete dei tuoi dati viene visualizzata. Per ulteriori informazioni, vedi [Identificazione dei dati visualizzati nella tua pagina Rileva Kibana](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data). Quindi, modifica la query predefinita per filtrare le voci.

    **Nota:** utilizza il linguaggio di query Lucene per definire la tua query personalizzata. Per ulteriori informazioni, vedi [Apache Lucene - Query Parser Syntax  ![Icona link esterno](../../../icons/launch-glyph.svg "Icona link esterno")](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html){: new_window}
    
    Quando Kibana viene avviato dalla IU {{site.data.keyword.Bluemix_notm}}, per modificare la query e definire più criteri di ricerca, puoi utilizzare i termini logici **AND** e **OR**. Questi operatori devono essere maiuscoli.    
    
    * Per cercare una parola chiave, o una parte di una parola chiave, immetti una parola seguita da un asterisco (*), che è un carattere jolly, ad esempio `Java*`. 
    * Per cercare una specifica frase, immetti tale frase tra virgolette doppie (" "); ad esempio `"Java/1.8.0"`.
    * Per creare ricerche più complesse, puoi utilizzare i termini logici AND e OR, ad esempio `"Java/1.8.0" OR "Java/1.7.0"`.
    * Per cercare un valore all'interno di un determinato campo, immetti la ricerca nel seguente formato: *nome_campo_log:termine_ricerca*; ad esempio, `instance_id:"1"`.
    * Per cercare un intervallo di valori per un determinato campo di log, immetti la ricerca nel seguente formato: *nome_campo_log:[inizio_di_intervallo_ID fine_intervallo]*, ad esempio, `instance_id:["1" TO "2"]`.

     Ad esempio, per un'applicazione CF, puoi creare una query `application_id:9d222152-8834-4bab-8685-3036cd25931a AND instance_id:["0" TO "1"]` che elenca solo le voci per le istanze *0* e *1*. 

3. Salva la query in modo da poterla riutilizzare successivamente. Per maggiori informazioni, vedi [Salvataggio di una ricerca](/docs/services/CloudLogAnalysis/kibana/define_search.html#save_search1). 

**Nota:** se devi eliminare una query, vedi [Eliminazione di una ricerca](/docs/services/CloudLogAnalysis/kibana/define_search.html#delete_search).



## Eliminazione di una ricerca
{: #delete_search}

Per eliminare una ricerca, completa la seguente procedura nella pagina Impostazioni:

1. Nella pagina Impostazioni, seleziona la scheda **Oggetti**.

2. Nella scheda **Ricerche**, seleziona la ricerca che desideri eliminare.

3. Fai clic su **Elimina**.


## Esportazione di una ricerca
{: #export_search}

Per esportare una ricerca, completa la seguente procedura nella pagina Impostazioni:

1. Nella pagina Impostazioni, seleziona la scheda **Oggetti**.

2. Nella scheda **Ricerche**, seleziona la ricerca che desideri esportare.

3. Fai clic su **Esporta**.

4. Salva il file.

 
## Importazione di una ricerca
{: #import_search}

Per importare una ricerca, completa la seguente procedura nella pagina Impostazioni:

1. Nella pagina Impostazioni, seleziona la scheda **Oggetti**.

2. Nella scheda **Ricerche**, seleziona **Importa**.

3. Seleziona un file e fai clic su **Apri**.

La ricerca viene aggiunta all'elenco delle ricerche.

## Aggiornamento del contenuto di una ricerca
{: #refresh_search}

Per aggiornare manualmente il contenuto di una ricerca, puoi fare clic sulla lente di ingrandimento disponibile nella barra di ricerca. 

Per aggiornare automaticamente i dati visualizzati nella pagina Rileva, puoi configurare un intervallo di aggiornamento. Il valore corrente dell'intervallo di aggiornamento viene visualizzato nella barra del menu nella pagine Rileva. Per impostazione predefinita, l'aggiornamento automatico è impostato su **DISATTIVO**.

Completa la seguente procedura per impostare un intervallo di aggiornamento:

1. Nella pagina Rileva, fai clic sul **Filtro temporale** disponibile nella barra del menu.

2. Fai clic su **Aggiornamento automatico** ![Aggiornamento automatico](images/auto_refresh_icon.jpg "Aggiornamento automatico").

3. Scegli un intervallo di aggiornamento dall'elenco. 

**Nota**: dopo aver abilitato un intervallo di aggiornamento, puoi sospenderlo facendo clic sul pulsante di pausa![Pausa](images/auto_refresh_pause_icon.jpg "Pausa").


## Ricaricamento di una ricerca
{: #reload_search1}

Completa la seguente procedura per caricare una ricerca salvata:

1. Nella barra degli strumenti della pagina Rileva, fai clic sul pulsante **Carica ricerca** ![Carica ricerca](images/load_icon.jpg "Carica ricerca").

2. Seleziona la ricerca che desideri caricare. 

## Avvio di una nuova ricerca
{: #k4_new_search}

Per avviare una nuova ricerca, fai clic sul pulsante **Nuova ricerca** ![Nuova ricerca](images/new_search_icon.jpg "Nuova ricerca") nella barra degli strumenti della pagina Rileva.

## Salvataggio di una ricerca 
{: #save_search1}

Tieni conto delle seguenti informazioni sul salvataggio di ricerche personalizzate in Kibana:

* Quando salvi una ricerca, la stringa della query di ricerca e il modello di indice selezionato correntemente, vengono salvati.
* Quando apri una ricerca nella pagina *Rileva* e modificarla, puoi scegliere di salvarla con lo stesso nome oppure puoi salvare la ricerca personalizzata modificata con un nome differente. Per impostazione predefinita, il nome della ricerca fornito è quello che corrisponde alla ricerca personalizzata che hai aperto inizialmente.

    * Per salvare la ricerca personalizzata modificata con lo stesso nome, fai clic su **Salva**. Nota: la ricerca personalizzata originale viene sovrascritta. 
	
	* Per salvare la ricerca personalizzata modificata con un nome differente, immetti un nuovo nome nel campo **Salva ricerca** e fai quindi clic su **Salva**. 


Completa la seguente procedura per salvare la ricerca corrente nella pagina Rileva:

1. Nella barra degli strumenti della pagina Rileva, fai clic sul pulsante **Salva ricerca** ![Salva ricerca](images/save_search_icon.jpg "Salva ricerca").

2. Immetti un nome per la ricerca.

    **Nota:** quando fai clic su **Salva**, non c'è alcuna avvertenza relativa alla sovrascrittura; pertanto, se specifichi un nome esistente, il salvataggio sostituirà tale versione senza alcuna indicazione.

3. Fai clic su **Salva**. 
