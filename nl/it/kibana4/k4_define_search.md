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
{:#k4_define_search}

Nella barra di ricerca della pagina Rileva, puoi definire e salvare le query di ricerca utilizzando il linguaggio di query Lucene. Per ogni ricerca, puoi applicare i filtri per restringere le voci disponibili per l'analisi.
{:shortdesc}

Completa le seguenti attività per definire una ricerca personalizzata:

1. Avvia Kibana.

    Per i contenitori o le applicazioni CF (Cloud Foundry) eseguiti nell'infrastruttura cloud gestita da {{site.data.keyword.Bluemix}}, completa la seguente procedura:
    
    1. Accedi alla scheda **Log** del tuo contenitore o della tua applicazione CF (Cloud Foundry). 

        Fai clic sul nome dell'applicazione o sul contenitore nel dashboard {{site.data.keyword.Bluemix_notm}}. Quindi, per le applicazioni CF, fai clic sulla scheda **Log**; per i contenitori, fai clic su **Monitoraggio e log** e seleziona quindi la scheda **Registrazione**. Vengono visualizzati i log.

    2. Accedi a Kibana. Fai clic su **Vista avanzata** ![Link Vista avanzata](images/logging_advanced_view.jpg "Link Vista avanzata"). Viene visualizzato il dashboard Kibana.
    
    Per i contenitori eseguiti in un cluster Kubernetes, [avvia Kibana dal browser](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-k4_launch#launch_Kibana_from_browser1). 
    
    Quando accedi a Kibana, viene applicata la ricerca predefinita. Puoi visualizzare i log per l'elenco di istanze delle risorse per cui hai avviato Kibana. Puoi filtrare i log per ognuna delle risorse {{site.data.keyword.Bluemix_notm}} in tale spazio.

2. Guarda nella pagina Rileva per visualizzare quale sottorete dei tuoi dati viene visualizzata. Per ulteriori informazioni, vedi [Identificazione dei dati visualizzati nella tua pagina Rileva Kibana](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-kibana_analize_logs_interactively#k4_identify_data). Quindi, modifica la query predefinita per filtrare le voci.

    **Nota:** utilizza il linguaggio di query Lucene per definire la tua query personalizzata. Per ulteriori informazioni, vedi [Apache Lucene - Query Parser Syntax  ![Icona link esterno](../../../icons/launch-glyph.svg "Icona link esterno")](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html){: new_window}
    
    Quando Kibana viene avviato da {{site.data.keyword.Bluemix_notm}}, per modificare la query e definire più criteri di ricerca, puoi utilizzare i termini logici **AND** e **OR**. Questi operatori devono essere maiuscoli.    
    
    * Per cercare una parola chiave, o parte di una parola chiave, immetti una parola seguita da un simbolo jolly \*, ad esempio `Java*`. 
    * Per cercare una frase particolare, immetti tale frase tra virgolette doppie, ad esempio `"Java/1.8.0"`.
    * Per creare ricerche più complesse, puoi utilizzare i termini logici AND e OR, ad esempio `"Java/1.8.0" OR "Java/1.7.0"`.
    * Per cercare un valore all'interno di un determinato campo, immetti la ricerca nel seguente formato: *nome_campo_log:termine_ricerca*; ad esempio, `instance_id:"1"`.
    * Per cercare un intervallo di valori per un determinato campo di log, immetti la ricerca nel seguente formato: *nome_campo_log:[inizio_di_intervallo_ID fine_intervallo]*, ad esempio, `instance_id:["1" TO "2"]`.

     Ad esempio, per un'applicazione CF, puoi creare una query `application_id:9d222152-8834-4bab-8685-3036cd25931a AND instance_id:["0" TO "1"]` che elenca solo le voci per le istanze *0* e *1*. 

3. Salva la query in modo da poterla riutilizzare successivamente. 




## Eliminazione di una ricerca
{: #k4_delete_search}

Per eliminare una ricerca, completa la seguente procedura nella pagina Impostazioni:

1. Nella pagina Impostazioni, seleziona la scheda **Oggetti**.

2. Nella scheda **Ricerche**, seleziona la ricerca che desideri eliminare.

3. Fai clic su **Elimina**.


## Esportazione di una ricerca
{: #k4_export_search}

Per esportare una ricerca, completa la seguente procedura nella pagina Impostazioni:

1. Nella pagina Impostazioni, seleziona la scheda **Oggetti**.

2. Nella scheda **Ricerche**, seleziona la ricerca che desideri esportare.

3. Fai clic su **Esporta**.

4. Salva il file.

 
## Importazione di una ricerca
{: #k4_import_search}

Per importare una ricerca, completa la seguente procedura nella pagina Impostazioni:

1. Nella pagina Impostazioni, seleziona la scheda **Oggetti**.

2. Nella scheda **Ricerche**, seleziona **Importa**.

3. Seleziona un file e fai clic su **Apri**.

La ricerca viene aggiunta all'elenco delle ricerche.

## Aggiornamento del contenuto di una ricerca
{: #k4_refresh_search}

Per aggiornare manualmente il contenuto di una ricerca, puoi fare clic sulla lente di ingrandimento disponibile nella barra di ricerca. 

Per aggiornare automaticamente i dati visualizzati nella pagina Rileva, puoi configurare un intervallo di aggiornamento. Il valore corrente dell'intervallo di aggiornamento viene visualizzato nella barra del menu nella pagine Rileva. Per impostazione predefinita, l'aggiornamento automatico è impostato su **DISATTIVO**.

Completa la seguente procedura per impostare un intervallo di aggiornamento:

1. Nella pagina Rileva, fai clic sul **Filtro temporale** disponibile nella barra del menu.

2. Fai clic su **Aggiornamento automatico** ![Aggiornamento automatico](images/k4_auto_refresh_icon.jpg "Aggiornamento automatico").

3. Scegli un intervallo di aggiornamento dall'elenco. 

    ![Opzioni di intervallo di aggiornamento](images/k4_change_autorefresh.jpg "Opzioni di intervallo di aggiornamento")


**Nota**: dopo aver abilitato un intervallo di aggiornamento, puoi sospenderlo facendo clic sul pulsante di pausa![Pausa](images/k4_auto_refresh_pause_icon.jpg "Pausa").


## Ricaricamento di una ricerca
{: #k4_reload_search}

Completa la seguente procedura per caricare una ricerca salvata:

1. Nella barra degli strumenti della pagina Rileva, fai clic sul pulsante **Carica ricerca** ![Carica ricerca](images/k4_load_icon.jpg "Carica ricerca").

2. Seleziona la ricerca che desideri caricare. 

## Avvio di una nuova ricerca
{: #k4_new_search1}

Per avviare una nuova ricerca, fai clic sul pulsante **Nuova ricerca** ![Nuova ricerca](images/k4_new_search_icon.jpg "Nuova ricerca") nella barra degli strumenti della pagina Rileva.

## Salvataggio di una ricerca 
{: #k4_save_search}

Quando salvi una ricerca, la stringa della query di ricerca e il modello di indice selezionato correntemente, vengono salvati.

Completa la seguente procedura per salvare la ricerca corrente nella pagina Rileva:

1. Nella barra degli strumenti della pagina Rileva, fai clic sul pulsante **Salva ricerca** ![Salva ricerca](images/k4_save_search_icon.jpg "Salva ricerca").

2. Immetti un nome per la ricerca.

3. Fai clic su Salva. 
