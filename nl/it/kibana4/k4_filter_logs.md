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

# Filtro dei log in Kibana
{:#k4_filter_logs}

Nella pagina Rileva, puoi creare le query di ricerca e applicare i filtri per vincolare le informazioni visualizzate per l'analisi.
{:shortdesc}

* Puoi definire una o più query di ricerca nella barra di ricerca della pagina Rileva. Una query di ricerca definisce un sottoinsieme di voci di log. Utilizza il linguaggio di query Lucene per definire la query di ricerca. 

* Puoi aggiungere filtri dall'*Elenco campi* o dalle voci della tabella. Un filtro ridefinisce la selezione dei dati includendo o escludendo informazioni. Puoi abilitare o disabilitare un filtro, invertire l'azione di filtro, attivare/disattivare il filtro o rimuoverlo completamente. 

Dopo aver definito una nuova ricerca, salvala in modo da poterla riutilizzare per analisi future nella pagina Rileva o per creare le visualizzazioni che puoi utilizzare nei dashboard personalizzati. 

Quando esegui una nuova ricerca, l'istogramma, la tabella e l'elenco dei campi vengono automaticamente aggiornati per visualizzare i risultati della ricerca. Per scoprire quali dati vengono visualizzati, vedi [Identificazione dei dati visualizzati nella pagina Rileva](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-kibana_analize_logs_interactively#k4_identify_data).

Puoi creare delle ricerche personalizzate per filtrare i tuoi log. Il seguente elenco mostra gli scenari su come filtrare i dati nei tuoi log:

* Puoi eseguire la ricerca nel tuo log per le voci che includono un testo specifico nel valore di un campo. Per maggiori informazioni, vedi [Filtro dei tuoi log per un testo specifico in un valore del campo](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-k4_filter_logs#k4_filter_logs_spec_text).
 
* Puoi eseguire la ricerca nel tuo log per un valore del campo specifico o escludere voci dal log per un valore del campo specifico. Per maggiori informazioni, vedi [Filtro dei tuoi log per un valore del campo specifico](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-k4_filter_logs#k4_filter_logs_spec_field).
 
* Puoi filtrare i tuoi log per visualizzare le voci in un periodo di tempo. Per maggiori informazioni, vedi [Configurazione di un filtro temporale](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-k4_filter_logs#set_time_filter1).
     

## Aggiunta di un filtro a un valore non elencato nell'*Elenco campi*
{:#k4_add_filter_out_value}

Per aggiungere un filtro a un valore non visualizzato nell'*Elenco campi*, ricerca i record che includono tale valore tramite una query. Quindi aggiungi il filtro dalla voce della tabella disponibile nella pagina Rileva. 

Completa la seguente procedura per aggiungere un filtro al valore che non è disponibile nell'elenco visualizzato nella sezione *Elenco campi*:

1. Guarda nella pagina Rileva Kibana per visualizzare quale sottorete dei tuoi dati viene visualizzata. Per ulteriori informazioni, vedi [Identificazione dei dati visualizzati nella tua pagina Rileva Kibana](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-kibana_analize_logs_interactively#k4_identify_data).

    Ad esempio, la seguente figura mostra i valori delle istanze per un'applicazione CF nell'*Elenco campi*. 
    
    ![Mostra valori nell'Elenco campi](images/k4_add_filter_f1.jpg "Mostra valori nell'Elenco campi")
    
    Sei interessato all'istanza numero *3* ma non è disponibile nell'elenco che puoi visualizzare.

2. Nella pagina Rileva, modifica la query per ricercare un valore di campo specifico.

    Ad esempio, per ricerca l'istanza *3*, la query che immetti è la seguente:
   `application_id:9d222152-8834-4bab-8685-3036cd25931a AND instance_id:"3"`
    
    ![Modifica query](images/k4_add_filter_f2.jpg "Modifica query")
    
    Nella tabella, puoi visualizzare tutti i record che corrispondono alla tua query. 
    
 3. Espandi un record e seleziona il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento in modalità inclusiva](images/k4_include_field_icon.jpg "Pulsante di lente di ingrandimento in modalità inclusiva") per aggiungere un filtro.
 
     Ad esempio, per aggiungere un filtro per l'ID istanza con il valore *3*, fai clic sul pulsante di lente di ingrandimento![Pulsante di lente di ingrandimento in modalità inclusiva](images/k4_include_field_icon.jpg "Pulsante di lente di ingrandimento in modalità inclusiva") accanto al campo *instance_id*.
     
     ![Mostra tabella](images/k4_add_filter_f3.jpg "Mostra tabella")
     
4. Controlla che il filtro sia stato aggiunto.

    Ad esempio, la seguente figura mostra il filtro abilitato dopo che lo hai aggiunto dalla tabella.
    
    ![Mostra filtro](images/k4_add_filter_f4.jpg "Mostra filtro")
    
    


## Filtro dei tuoi log per un valore del campo specifico
{:#k4_filter_logs_spec_field}

Puoi cercare le voci che includono un valore del campo specifico. 

Completa la seguente procedura per cercare le voci che includono un valore del campo specifico:

1. Guarda nella pagina Rileva Kibana per visualizzare quale sottorete dei tuoi dati viene visualizzata. Per ulteriori informazioni, vedi [Identificazione dei dati visualizzati nella tua pagina Rileva Kibana](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-kibana_analize_logs_interactively#k4_identify_data).

2. Nell'*Elenco campi*, identifica il campo per cui desideri definire un filtro e fai clic su di esso.

    Per il campo viene visualizzato un massimo di 5 valori. Ogni valore ha due pulsanti della lente di ingrandimento. 
    
    Se non puoi visualizzare il valore, vedi [Aggiunta di un filtro a un valore non elencato nell'Elenco campi](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-k4_filter_logs#k4_add_filter_out_value).

3. Per aggiungere un filtro che cerca le voci con un valore di campo, scegli il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento in modalità inclusiva](images/k4_include_field_icon.jpg "Pulsante di lente di ingrandimento in modalità inclusiva") per tale valore.

    ![Filtro che include il valore di campo](images/k4_add_filter_for_field.jpg "Filtro che include il valore di campo")

    Per aggiungere un filtro che cerca le voci che non includono tale valore di campo, scegli il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento in modalità inclusiva](images/k4_exclude_field_icon.jpg "Pulsante di lente di ingrandimento in modalità inclusiva") per il valore.

    ![Filtro che esclude il valore di campo](images/k4_add_filter_to_exclude_field.jpg "Filtro che esclude il valore di campo")

4. Scegli una delle seguenti opzioni per utilizzare i filtri in Kibana:

    <table>
      <caption>Tabella 1. Metodi per utilizzare i filtri</caption>
      <tbody>
        <tr>
          <th align="center">Opzione</th>
          <th align="center">Descrizione</th>
          <th align="center">Ulteriori informazioni</th>
        </tr>
        <tr>
          <td align="left">Abilita</td>
          <td align="left">Seleziona questa opzione per abilitare un filtro.</td>
          <td align="left">Quando aggiungi un filtro, viene abilitato automaticamente. <br> Se un filtro è disabilitato, fai clic su di essa per abilitarlo.</td>
        </tr>
        <tr>
          <td align="left">Disabilita</td>
          <td align="left">Seleziona questa opzione per disabilitare un filtro.</td>
          <td align="left">Dopo aver aggiunto un filtro, se desideri nascondere le voci per un valore del campo, fai clic su **disabilita**.</td>
        </tr>
        <tr>
          <td align="left">Blocca</td>
          <td align="left">Seleziona questa opzione per bloccare il filtro tra le pagine Kibana.</td>
          <td align="left">Puoi bloccare un filtro nella pagina *Ricerca*, *Visualizza* o *Dashboard*.</td>
        </tr>
        <tr>
          <td align="left">Attiva/Disattiva</td>
          <td align="left">Seleziona questa opzione per attivare/disattivare un filtro.</td>
          <td align="left">Per impostazione predefinita, le voci che corrispondono a un filtro vengono visualizzate. Per visualizzare le voci che non corrispondono, attiva/disattiva il filtro.</td>
        </tr>
        <tr>
          <td align="left">Rimuovi</td>
          <td align="left">Seleziona questa opzione per rimuovere un filtro.</td>
          <td align="left"></td>
        </tr>
      </tbody>
    </table>

## Filtro dei tuoi log dell'applicazione CF per origine
{:#k4_filter_logs_by_source}

Completa la seguente procedura per cercare le voci che includono un'origine del log specifica:

1. Guarda nella pagina Rileva Kibana per visualizzare quale sottorete dei tuoi dati viene visualizzata. Per ulteriori informazioni, vedi [Identificazione dei dati visualizzati nella tua pagina Rileva Kibana](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-kibana_analize_logs_interactively#k4_identify_data).

2. Nell'*Elenco campi*, seleziona il campo **source_id**.

    ![Elenco filtri che mostra il campo source_id](images/k4_filter_sourceid_F1.jpg "Elenco filtri che mostra il campo source_id")     

3. Per aggiungere un filtro che ricerca le voci che includono uno specifico source_id, scegli il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento nella modalità inclusiva](images/k4_include_field_icon.jpg "Pulsante di lente di ingrandimento nella modalità inclusiva") per tale valore.

    Per un elenco delle origini del log disponibili per le applicazioni CF, vedi [Origini log per le applicazioni CF](/docs/services/CloudLogAnalysis/cfapps?topic=cloudloganalysis-logging_cf_apps#cf_apps_log_sources_diego).

    Ad esempio, per aggiungere un filtro che include le voci di log relative all'avvio, all'arresto o all'arresto anomalo di un'applicazione CF, seleziona il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento in modalità inclusiva](images/k4_include_field_icon.jpg "Pulsante di lente di ingrandimento in modalità inclusiva") disponibile per il valore *CELL* nella sezione *Elenco campi*. La seguente figura mostra il filtro per il valore source_id *CELL* abilitato.
    
    ![Filtro che include il valore di campo](images/k4_filter_sourceid_F2.jpg "Filtro che include il valore di campo")

    Per aggiungere un filtro che ricerca le voci che non includono uno specifico source_id, scegli il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento in modalità esclusiva](images/k4_exclude_field_icon.jpg "Pulsante di lente di ingrandimento in modalità esclusiva") per il valore.
    
    Ad esempio, per aggiungere un filtro che esclude le voci di log relative all'avvio, all'arresto o all'arresto anomalo di un'applicazione CF, seleziona il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento in modalità inclusiva](images/k4_exclude_field_icon.jpg "Pulsante di lente di ingrandimento in modalità inclusiva") disponibile per il valore *CELL* nella sezione *Elenco campi*. La seguente figura mostra il filtro che esclude le voci per il valore source_id *CELL*.

    ![Filtro che esclude il valore di campo](images/k4_filter_sourceid_F3.jpg "Filtro che esclude il valore di campo")


## Filtro dei tuoi log per tipo di log
{:#k4_filter_logs_by_log_type}

Completa la seguente procedura per cercare le voci che includono un tipo di log specifico:

1. Guarda nella pagina Rileva Kibana per visualizzare quale sottorete dei tuoi dati viene visualizzata. Per ulteriori informazioni, vedi [Identificazione dei dati visualizzati nella tua pagina Rileva Kibana](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-kibana_analize_logs_interactively#k4_identify_data).

2. Nell'*Elenco campi*, seleziona il campo **tipo**.

    Ad esempio, nella seguente figura, è disponibile solo un singolo tipo di log: *syslog*
    
    ![Elenco filtri che mostra il campo log type](images/k4_filter_log_type_F1.jpg "Elenco filtri che mostra il campo log type")
   
3. Per aggiungere un filtro che cerca uno specifico tipo di log, scegli il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento nella modalità inclusiva](images/k4_include_field_icon.jpg "Pulsante di lente di ingrandimento nella modalità inclusiva") per il tipo di log che desideri analizzare.

    Ad esempio, per aggiungere un filtro che include le voci di log per *syslog*, seleziona il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento in modalità inclusiva](images/k4_include_field_icon.jpg "Pulsante di lente di ingrandimento in modalità inclusiva") disponibile per il valore *syslog* nella sezione *Elenco campi*. La seguente figura mostra il filtro che include le voci per il tipo di log *syslog*.

    ![Filtro che include le voci di tipo di log per syslog](images/k4_filter_log_type_F2.jpg "Filtro che include le voci di tipo di log per syslog")

    Per aggiungere un filtro che cerca le voci che non includono un tipo di log specifico, scegli il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento in modalità esclusiva](images/k4_exclude_field_icon.jpg "Pulsante di lente di ingrandimento in modalità esclusiva") per il valore.

     Ad esempio, per aggiungere un filtro che esclude le voci di log per *syslog*, seleziona il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento in modalità esclusiva](images/k4_exclude_field_icon.jpg "Pulsante di lente di ingrandimento in modalità esclusiva") disponibile per il valore *syslog* nella sezione *Elenco campi*. La seguente figura mostra il filtro che esclude le voci per il tipo di log *syslog*.
     
     ![Filtro che esclude le voci di tipo di log per syslog](images/k4_filter_log_type_F3.jpg "Filtro che esclude le voci di tipo di log per syslog")


## Filtro dei tuoi log per ID istanza
{:#k4_filter_logs_by_instance_id}

Completa le seguenti attività per visualizzare e filtrare i tuoi log per ID istanza nel dashboard Kibana:

1. Guarda nella pagina Rileva Kibana per visualizzare quale sottorete dei tuoi dati viene visualizzata. Per ulteriori informazioni, vedi [Identificazione dei dati visualizzati nella tua pagina Rileva Kibana](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-kibana_analize_logs_interactively#k4_identify_data).

2. Nell'*Elenco campi*, seleziona uno dei seguenti campi per la ricerca per un ID istanza specifico:

    * **ID_istanza**: questo campo elenca i vari ID istanza disponibili nel log per un'applicazione Cloud Foundry. 
    * **istanza**: questo campo elenca i vari GUID di tutte le istanze per un gruppo di contenitori. 

    Ad esempio, la seguente figura mostra valori differenti delle istanze per un'applicazione CF:
    
    ![Elenco filtri che mostra il campo instance_id](images/k4_filter_instanceid_f1.jpg "Elenco filtri che mostra il campo instance_id")
   
3. Per aggiungere un filtro che cerca uno specifico tipo di log, scegli il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento nella modalità inclusiva](images/k4_include_field_icon.jpg "Pulsante di lente di ingrandimento nella modalità inclusiva") per il tipo di log che desideri analizzare.

   Ad esempio, per aggiungere un filtro che include le voci per l'istanza dell'applicazione CF *2*, seleziona il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento in modalità inclusiva](images/k4_include_field_icon.jpg "Pulsante di lente di ingrandimento in modalità inclusiva") disponibile per il valore *2* nella sezione Elenco campi. La seguente figura mostra il filtro che include le voci per l'istanza *2*.
    
    ![Filtro che include le voci instance_id per l'istanza 2](images/k4_filter_instanceid_f2.jpg "Filtro che include le voci instance_id per l'istanza 2")

    Per aggiungere un filtro che cerca le voci che non includono un ID istanza specifico, scegli il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento in modalità esclusiva](images/k4_exclude_field_icon.jpg "Pulsante di lente di ingrandimento in modalità esclusiva") per il valore.

     Ad esempio, per aggiungere un filtro che esclude le voci per l'istanza dell'applicazione CF *2*, seleziona il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento in modalità esclusiva](images/k4_exclude_field_icon.jpg "Pulsante di lente di ingrandimento in modalità esclusiva") disponibile per il valore *2* nella sezione Elenco campi. La seguente figura mostra il filtro che esclude le voci per l'istanza *2*.
     
      ![Filtro che esclude le voci instance_id per l'istanza 2](images/k4_filter_instanceid_f3.jpg "Filtro che esclude le voci instance_id per l'istanza 2")


## Filtro dei tuoi log dell'applicazione CF in base al tipo di messaggio
{:#k4_filter_cf_logs_by_msg_type}

Completa la seguente procedura per cercare le voci che includono un tipo di messaggio specifico:

1. Guarda nella pagina Rileva Kibana per visualizzare quale sottorete dei tuoi dati viene visualizzata. Per ulteriori informazioni, vedi [Identificazione dei dati visualizzati nella tua pagina Rileva Kibana](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-kibana_analize_logs_interactively#k4_identify_data).

2. Nell'*Elenco campi*, seleziona il campo **message_type**.

    La seguente figura mostra i valori trovati per il campo *message_type* nei log di un'applicazione CF:
    
    ![Elenco filtri che mostra il campo message_type](images/k4_filter_by_msg_type_f1.jpg "Elenco filtri che mostra il campo message_type")     

3. Per aggiungere un filtro che cerca le voci che includono un *message_type* specifico, scegli il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento in modalità inclusiva](images/k4_include_field_icon.jpg "Pulsante di lente di ingrandimento in modalità inclusiva") per tale valore.

    Ad esempio, per aggiungere un filtro che include le voci di log che hanno un valore message_type di *OUT*, seleziona il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento in modalità inclusiva](images/k4_include_field_icon.jpg "Pulsante di lente di ingrandimento in modalità inclusiva") disponibile per il valore *OUT* nella sezione *Elenco campi*. La seguente figura mostra il filtro per il valore message_type *OUT* abilitato.
    
    ![Filtro che include il valore di campo](images/k4_filter_by_msg_type_f2.jpg "Filtro che include il valore di campo")

    Per aggiungere un filtro che cerca le voci che non includono un *message_type* specifico, scegli il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento in modalità esclusiva](images/k4_exclude_field_icon.jpg "Pulsante di lente di ingrandimento in modalità esclusiva") per il valore.
    
    Ad esempio, per aggiungere un filtro che esclude le voci di log per il message_type *OUT*, seleziona il pulsante di lente di ingrandimento ![Pulsante di lente di ingrandimento in modalità inclusiva](images/k4_exclude_field_icon.jpg "Pulsante di lente di ingrandimento in modalità inclusiva") disponibile per il valore *CELL* nella sezione *Elenco campi*. La seguente figura mostra il filtro che esclude le voci per il valore message_type *OUT*.

    ![Filtro che esclude il campo value](images/k4_filter_by_msg_type_f3.jpg "Filtro che esclude il campo value")


## Filtro dei tuoi log per un testo specifico in un valore del campo
{:#k4_filter_logs_spec_text}

Visualizza e ricerca le voci che includono un testo specifico nel valore di un campo. 

**Avviso:** puoi solo eseguire una ricerca di testo libero dei campi stringa che vengono analizzati dal programma di analisi Elasticsearch. 
    
Quando Elasticsearch analizza il valore di un campo stringa, suddivide il testo in confini di parola, come definito dal Unicode Consortium, rimuove la punteggiatura e i caratteri minuscoli da tutte le parole.
    
Completa la seguente procedura per cercare le voci che includono testo specifico in un valore del campo:

1. Guarda nella pagina Rileva Kibana per visualizzare quale sottorete dei tuoi dati viene visualizzata. Per ulteriori informazioni, vedi [Identificazione dei dati visualizzati nella tua pagina Rileva Kibana](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-kibana_analize_logs_interactively#k4_identify_data).

2. Identifica i campi analizzati in ElasticSearch per impostazione predefinita.

    Per visualizzare l'elenco completo dei campi analizzati disponibili per la ricerca e il filtro dei dati di log, [ricarica l'elenco dei campi](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-kibana_analize_logs_interactively#kibana_discover_view_reload_fields). Quindi, nell'*Elenco campi* disponibile nella pagina Rileva, completa la seguente procedura:
    
    1. Fai clic sull'icona di configurazione ![Icona di configurazione](images/k4_configure_icon.jpg "Icona di configurazione"). Viene visualizzata la sezione **Campi selezionati** in cui puoi filtrare i campi.

        ![Sezione di configurazione per visualizzare i campi con specifici attributi](images/k4_reset_filters.jpg "Sezione di configurazione per visualizzare i campi con specifici attributi")
    
    2. Per identificare i campi che vengono analizzati, seleziona **Sì** per il campo di ricerca **Analizzato**.

        ![Attributo analizzato](images/k4_reset_filters_analyze_options.jpg "Attributo analizzato")
    
        Viene visualizzato l'elenco dei campi analizzati.
    
        ![Elenco di campi analizzati](images/k4_list_analyzed_fields.jpg "Elenco di campi analizzati")
        
         
    3. Controlla se il campo in cui desideri eseguire la ricerca del testo libero sia un campo che viene analizzato da ElasticSearch per impostazione predefinita.
    
3. Se il campo viene analizzato, modifica la query per cercare le voci nei log che includono tale testo libero come parte di un valore di un campo.

    
**Esempio**

Se avvii Kibana per un'applicazione CF (Cloud Foundry) dalla IU {{site.data.keyword.Bluemix}} e desideri ricercare un messaggio specifico che include l'ID messaggio *CWWKT0016I:*, modifica la ricerca in modo che includa del testo libero.
    
1. Controlla la query di ricerca caricata e i dati visualizzati nella pagina Rileva.
       
    ![Query di ricerca predefinita](images/k4_filter_by_text_default_query.jpg "Query di ricerca predefinita")
        
2. Per cercare l'ID messaggio *CWWKT0016I*, modifica la query di ricerca e premi **Invio**:
    
    <pre class="pre">application_id:f52f6016-3aab-4b5c-aa2e-5493747cb978 AND message:"CWWKT0016I:" </pre>
        
    ![Modifica la query](images/k4_filter_by_text_modify_query.jpg "Modifica la query")
      
La tabella mostra le voci per la tua applicazione CF in cui il testo *CWWKT0016I* è parte del valore nel campo *messaggio*.
    
![Vista Nuova ricerca](images/k4_filter_by_text_result_query.jpg "Vista Nuova ricerca")     	
        

## Configurazione di un filtro temporale
{: #set_time_filter1}

Visualizza e filtra i log in un periodo di tempo configurando il *Selezionatore di tempo*.

Puoi configurare il *Selezionatore di tempo* nella pagina Rileva. Per impostazione predefinita, è impostato sugli ultimi 15 minuti. 

Completa la seguente procedura per cercare le voci che includono un tempo specifico:

1. Nella barra del menu della pagina Rileva, fai clic sul Selezionatore di tempo ![Selezionatore di tempo](images/k4_time_picker_icon.jpg "Selezionatore di tempo").

2. Configura l'intervallo di tempo 

    Puoi definire tutti i seguenti tipi di intervalli di tempo:
    
    * Veloce: questi sono gli intervalli di tempo predefiniti che includono gli utilizzi più comuni degli intervalli di tempo Assoluto e Relativo, ad esempio, *Oggi* e *Questo mese*. 
    
        ![Opzioni rapide del Selezionatore di tempo](images/k4_time_picker_quick.jpg "Opzioni rapide del Selezionatore di tempo")
    
    * Relativo: questi sono gli intervalli di tempo in cui puoi specificare la data e ora di inizio e di fine. Puoi eseguire arrotondare all'ora.
    
        ![Opzioni relative del Selezionatore di tempo](images/k4_time_picker_relative.jpg "Opzioni relative del Selezionatore di tempo")
    
    * Assoluto: questi sono gli intervalli di tempo tra una data di inizio e di fine.
    
        ![Opzioni assolute del Selezionatore di tempo](images/k4_time_picker_absolute.jpg "Opzioni assolute del Selezionatore di tempo")
      

Dopo aver configurato un intervallo di tempo, i dati visualizzati in Kibana corrispondono alle voci in quell'intervallo di tempo.








