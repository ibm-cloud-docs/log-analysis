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

# CLI Analisi dei log (plugin {{site.data.keyword.Bluemix_notm}})
{: #log_analysis_cli}

La CLI {{site.data.keyword.loganalysislong}} è un plug-in {{site.data.keyword.Bluemix_notm}} che puoi usare per gestire i log archiviati in Raccolta dei log.
{: shortdesc}

**Prerequisiti **
* Prima di eseguire i comandi di registrazione, accedi a {{site.data.keyword.Bluemix_notm}} con il comando `ibmcloud login` per generare un token di accesso e autenticare la tua sessione.

Per informazioni su come utilizzare la CLI {{site.data.keyword.loganalysisshort}}, vedi [Gestione dei log](/docs/services/CloudLogAnalysis/log_analysis_ov.html#log_analysis_ov).

<table>
  <caption>Comandi per la gestione dei log</caption>
  <tr>
    <th>Comando</th>
    <th>Quando utilizzarlo</th>
  </tr>
  <tr>
    <td>[ibmcloud logging](#base)</td>
    <td>Utilizza questo comando per ottenere informazioni sulla CLI, come l'elenco di comandi.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-delete](#delete)</td>
    <td>Utilizza questo comando per eliminare i log archiviati in Raccolta dei log.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-download](#download)</td>
    <td>Utilizza questo comando per scaricare i log dalla raccolta dei log in un file locale o per inviarli ad un altro programma come lo stack Elastic. </td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-show](#status)</td>
    <td>Utilizza questo comando per ottenere informazioni sui log raccolti in uno spazio, un'organizzazione o un account.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging help](#help)</td>
    <td>Utilizza questo comando per ottenere supporto su come utilizzare la CLI e per ottenere un elenco di tutti i comandi.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging option-show](#optionshow)</td>
    <td>Utilizza questo comando per visualizzare il periodo di conservazione per i log disponibili in uno spazio, un'organizzazione o un account.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging option-update](#optionupdate)</td>
    <td>Utilizza questo comando per impostare il periodo di conservazione per i log disponibili in uno spazio, un'organizzazione o un account.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging quota-usage-show](#quotausage)</td>
    <td>Utilizza questo comando per richiamare le informazioni sull'utilizzo della quota di uno spazio, un'organizzazione o un account. Puoi anche richiamare le informazioni sulla cronologia della quota.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging session-create](#session_create)</td>
    <td>Utilizza questo comando per creare una nuova sessione.</td>
  <tr>
  <tr>
    <td>[ibmcloud logging session-delete](#session_delete)</td>
    <td>Utilizza questo comando per eliminare una sessione.</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging sessions](#session_list)</td>
    <td>Utilizza questo comando per elencare le sessioni attive e i rispettivi ID.</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging session-show](#session_show)</td>
    <td>Utilizza questo comando per visualizzare lo stato di una sola sessione.</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging token-get](#tokenget)</td>
    <td>Utilizza questo comando per ottenere il token di registrazione e inviare i dati di log al servizio {{site.data.keyword.loganalysisshort}}.</td>
  </tr>
</table>


## ibmcloud logging
{: #base}

Fornisce informazioni generali sulla CLI.

```
ibmcloud logging 
```
{: codeblock}

**Esempi**

Per ottenere l'elenco dei comandi, esegui il seguente comando:

```
ibmcloud logging 
NAME:
   ibmcloud logging - IBM Cloud Log Analysis Service
USAGE:
   ibmcloud logging command [arguments...] [command options]

COMMANDS:
COMMANDS:
   log-delete         Delete log
   log-download       Download a log
   log-show           Show the count, size, and type of logs per day
   session-create     Create a session
   session-delete     Delete session
   sessions           List sessions info
   session-show       Show a session info
   option-show        Show the log retention
   option-update      Show the log options
   token-get          Get a logging token for sending logs
   quota-usage-show   Show quota usage info
   help             
   
Enter 'ibmcloud logging help [command]' for more information about a command.
```
{: codeblock}




## ibmcloud logging log-delete
{: #delete3}

Elimina i log archiviati in Raccolta dei log.

```
ibmcloud logging log-delete [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-f, --force ]
```
{: codeblock}

**Parametri**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facoltativo) Imposta il tipo di risorsa. I valori validi sono: *space*, *account* e *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facoltativo) Imposta questo campo sull'ID di uno spazio, un'organizzazione o un account. <br>Per impostazione predefinita, se non specifichi questo parametro, il comando usa l'ID della risorsa dove sei collegato. 
  </dd>
  
  <dt>-s, --start START_DATE</dt>
  <dd>(Facoltativo) Imposta la data di inizio in Coordinated Universal Time (UTC): *YYYY-MM-DD*, ad esempio, `2006-01-02`. <br>Il valore predefinito viene impostato su 2 settimane fa.
  </dd>
  
  <dt>-e, --end END_DATE</dt>
  <dd>(Facoltativo) Imposta la data di fine in Coordinated Universal Time (UTC): *YYYY-MM-DD*, ad esempio, `2006-01-02`. <br>Il valore predefinito viene impostato sulla data corrente.
  </dd>
  
  <dt>-f, --force </dt>
  <dd>(Facoltativo) Imposta questa opzione per eliminare i log senza dover confermare la tua azione.
  </dd>
</dl>

**Esempio**

Per eliminare i log di tipo *linux_syslog* per il 25 maggio 2017, esegui il seguente comando:
```
ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
```
{: screen}



## ibmcloud logging log-download 
{: #download3}

Scarica i log dalla raccolta dei log in un file locale o li invia a un altro programma come uno stack Elastic. 

**Nota:** per scaricare i file, devi prima creare una sessione. Una sessione definisce quali log scaricare in base all'intervallo di date, al tipo di log e al tipo di account. Scarica i log nel contesto di una sessione. Per ulteriori informazioni, vedi [ibmcloud logging session create (Beta)](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#session_create).

```
 ibmcloud logging log-download  [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-o, --output OUTPUT] SESSION_ID

```
{: codeblock}

**Parametri**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facoltativo) Imposta il tipo di risorsa. I valori validi sono: *space*, *account* e *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facoltativo) Imposta questo campo sull'ID di uno spazio, un'organizzazione o un account. <br>Per impostazione predefinita, se non specifichi questo parametro, il comando usa l'ID della risorsa dove sei collegato. 
  </dd>
 
  <dt>-o, --output OUTPUT</dt>
  <dd>(Facoltativo) imposta il percorso e il nome del file per il file di output locale in cui vengono scaricati i log. <br>Il valore predefinito è un trattino (-). <br>Imposta questo parametro sul valore predefinito per inviare i log all'output standard.</dd>

</dl>

**Argomenti**

<dl>
  <dt>SESSION_ID</dt>
  <dd>Questo valore indica l'ID della sessione che devi usare quando scarichi i log. <br>**Nota:** il comando `ibmcloud logging session-create` fornisce i parametri che controllano quali log vengono scaricati. </dd>
</dl>

**Nota:** dopo che lo scaricamento è terminato, rieseguendo lo stesso comando non succederà nulla. Per riscaricare gli stessi dati, devi utilizzare un file o una sessione differenti.

**Esempi**

In un sistema Linux, per scaricare i log in un file denominato mylogs.gz, esegui questo comando:

```
ibmcloud logging log-download -o mylogs.gz guBeZTIuYtreOPi-WMnbUg==
```
{: screen}

Per scaricare i log nel tuo proprio stack Elastic, esegui il seguente comando:

```
ibmcloud logging log-download guBeZTIuYtreOPi-WMnbUg== | gunzip | logstash -f logstash.conf
```
{: screen}

Il seguente file è un esempio di un file logstash.conf:

```
input {
  stdin {
    codec => json_lines {}
  }
}
output {
  elasticsearch {
    hosts => [ "127.0.0.1:9200" ]
  }
}
```
{: screen}


## ibmcloud logging help
{: #help}

Fornisce le informazioni su come utilizzare un comando.

```
ibmcloud logging help [comando] 
```
{: codeblock}

**Parametri**

<dl>
<dt>Comando</dt>
<dd>Imposta il nome del comando per il quale desideri ottenere supporto.
</dd>
</dl>


**Esempi**

Per ottenere supporto su come eseguire il comando per visualizzare lo stato dei log, esegui il seguente comando:

```
ibmcloud logging help log-show
NAME:
   log-show - Show the count, size, and type of logs per day

USAGE:
   ibmcloud logging log-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-l, --list-type-detail]

OPTIONS:
   -r, --resource-type     Resource type, the valid resource type is account, org, or space
   -i, --resource-id       Resource id, the target resource id
   -s, --start             Start Date, UTC time value included in format YYYY-MM-DD
   -e, --end               End Date, UTC time value included in format YYYY-MM-DD
   -t, --type              Log Type, for example "syslog"
   -l, --list-type-detail  List the detailed type

```
{: screen}


## ibmcloud logging option-show
{: #optionshow}

Visualizza il periodo di conservazione per i log disponibili in uno spazio, un'organizzazione o un account. 

* Il periodo è impostato per numero di giorni.
* Il valore predefinito è **-1**. 

**Nota:** per impostazione predefinita sono archiviati tutti i log. Devi eliminarli manualmente utilizzando il comando **delete**. Imposta una politica di conservazione per eliminare i log automaticamente.

```
ibmcloud logging option-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID]
```
{: codeblock}

**Parametri**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facoltativo) Imposta il tipo di risorsa. I valori validi sono: *space*, *account* e *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facoltativo) Imposta questo campo sull'ID di uno spazio, un'organizzazione o un account. <br>Per impostazione predefinita, se non specifichi questo parametro, il comando usa l'ID della risorsa dove sei collegato. 
  </dd>

</dl>

**Esempi**

Per visualizzare il periodo di conservazione corrente predefinito per lo spazio in cui hai eseguito l'accesso, esegui il seguente comando:

```
ibmcloud logging option-show
```
{: screen}




## ibmcloud logging option-update
{: #optionupdate}

Cambia il periodo di conservazione per i log disponibili in uno spazio, un'organizzazione o un account. 

* Il periodo è impostato per numero di giorni.
* Il valore predefinito è **-1**. 

```
ibmcloud logging option-update [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] <-e,--retention RETENTION_VALUE>
```
{: codeblock}

**Parametri**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facoltativo) Imposta il tipo di risorsa. I valori validi sono: *space*, *account* e *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facoltativo) Imposta questo campo sull'ID dello spazio, dell'organizzazione o dell'account per cui vuoi ottenere informazioni. <br>Per impostazione predefinita, se non specifichi questo parametro, il comando usa l'ID della risorsa dove sei collegato. 
  </dd>
  
  <dt>-e,--retention RETENTION_VALUE</dt>
  <dd>Imposta il numero di giorni per cui vengono conservati i log. </dd>

</dl>

**Esempio**

Per modificare il periodo di conservazione in 25 giorni per lo spazio in cui hai eseguito l'accesso, esegui il seguente comando:

```
ibmcloud logging option-update -e 25
```
{: screen}


## ibmcloud logging quota-usage-show
{: #quotausage}

Fornisce informazioni sull'utilizzo della quota di uno spazio, un'organizzazione o un account. Puoi inoltre utilizzarlo per ottenere l'utilizzo della cronologia.

* Il periodo è impostato per numero di giorni.
* Il valore predefinito è **-1**. 

```
ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s,--history]
```
{: codeblock}

**Parametri**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facoltativo) Imposta il tipo di risorsa. I valori validi sono: *space*, *account* e *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facoltativo) Imposta questo campo sull'ID di uno spazio, un'organizzazione o un account. <br>Per impostazione predefinita, se non specifichi questo parametro, il comando usa l'ID della risorsa dove sei collegato. 
  </dd>
  
  <dt>-s,--history</dt>
  <dd>(Facoltativo) Imposta questo parametro per ottenere le informazioni cronologiche sull'utilizzo della quota.</dd>

</dl>

**Esempio**

Per ottenere l'utilizzo della quota cronologico di un dominio dello spazio, immetti il seguente comando:

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744 -s
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Date         Allotmant   Usage   
2018.02.28   524288000   80405926   
2018.03.06   524288000   18955540   
2018.03.05   524288000   47262944   
2018.03.08   524288000   18311338   
2018.03.01   524288000   82416831   
2018.03.03   524288000   75045462   
2018.03.07   524288000   17386278   
2018.03.02   524288000   104316444   
2018.03.04   524288000   73125223   
```
{: screen}

## ibmcloud logging session-create
{: #session_create}

Crea una nuova sessione.

**Nota:** puoi avere fino a 30 sessioni simultanee in uno spazio. La sessione viene creata per un utente. Le sessioni non possono essere condivise tra gli utenti in uno spazio.

```
ibmcloud logging session-create [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-T, --time, LOG_TIME]
```
{: codeblock}

**Parametri**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facoltativo) Imposta il tipo di risorsa. I valori validi sono: *space*, *account* e *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facoltativo) Imposta questo campo sull'ID di uno spazio, un'organizzazione o un account. <br>Per impostazione predefinita, se non specifichi questo parametro, il comando usa l'ID della risorsa dove sei collegato. 
  </dd>
  
  <dt>-s, --start START_DATE</dt>
  <dd>(Facoltativo) Imposta la data di inizio in Coordinated Universal Time (UTC): *YYYY-MM-DD*, ad esempio, `2006-01-02`. <br>Il valore predefinito viene impostato su 2 settimane fa.
  </dd>
  
  <dt>-e, --end END_DATE</dt>
  <dd>(Facoltativo) Imposta la data di fine in Coordinated Universal Time (UTC): *YYYY-MM-DD*, ad esempio, `2006-01-02`. <br>Il valore predefinito viene impostato sulla data corrente.
  </dd>
  
  <dt>-t, --type, LOG_TYPE</dt>
  <dd>(Facoltativo) imposta il tipo di log. <br>Ad esempio, *syslog* è un tipo di log. <br>Il valore predefinito è impostato su asterisco (*). <br>Puoi specificare più tipi di log separando ogni tipo con una virgola, ad esempio *log_type_1,log_type_2,log_type_3*.
  </dd>

  <dt>-T, --time, LOG_TIME</dt>
  <dd>(Facoltativo) Imposta l'ora del giorno per cui vuoi richiamare i log di un tipo specifico. </br>I valori validi sono 0-23. </br>Dovrebbe essere utilizzato insieme a LOG_TYPE.
  </dd>

</dl>


**Valori restituiti**

<dl>

    <dt>ID</dt>
    <dd>ID sessione.</dd>
	
	<dt>Tipo di risorsa</dt>
    <dd>ID risorsa.</dd>

    <dt>AccessTime</dt>
    <dd>La data/ora che indica quando la sessione è stata utilizzata l'ultima volta.</dd>

    <dt>CreateTime</dt>
    <dd>La data/ora che corrisponde alla data e all'ora in cui è stata creata la sessione.</dd>
	
	<dt>Start</dt>
    <dd>Indica il primo giorno utilizzato per filtrare i log. </dd>

    <dt>End</dt>
    <dd>Indica l'ultimo giorno utilizzato per filtrare i log.</dd>

    <dt>Tipo</dt>
    <dd>I tipi di log scaricati tramite la sessione.</dd>

</dl>


**Esempio**

Per creare una sessione che include i log per il 13 novembre 2017, esegui questo comando:

```
ibmcloud logging session-create -s 2017-11-13 -e 2017-11-13
Creating session for xxxxx@yyy.com resource: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx ...

ID                                     Space                                  CreateTime                       AccessTime                       Start        End          Type   
1ef776d1-4d25-4297-9693-882606c725c8   xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx   2017-11-16T11:52:06.376125207Z   2017-11-16T11:52:06.376125207Z   2017-11-13   2017-11-13   ANY_TYPE   
Session: 1ef776d1-4d25-4297-9693-882606c725c8 is created
```
{: screen}


## ibmcloud logging session-delete 
{: #session_delete}

Elimina una sessione, specificata per ID sessione.

```
ibmcloud session-delete [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] SESSION_ID
```
{: codeblock}

**Parametri**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facoltativo) Imposta il tipo di risorsa. I valori validi sono: *space*, *account* e *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facoltativo) Imposta questo campo sull'ID di uno spazio, un'organizzazione o un account. <br>Per impostazione predefinita, se non specifichi questo parametro, il comando usa l'ID della risorsa dove sei collegato. 
  </dd>
 
</dl>

**Argomenti**

<dl>
  <dt>SESSION_ID</dt>
  <dd>L'ID della sessione attiva che vuoi eliminare.</dd>
</dl>

**Esempio**

Per eliminare una sessione con ID sessione *cI6hvAa0KR_tyhjxZZz9Uw==*, esegui il seguente comando:

```
ibmcloud logging session-delete cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}



## ibmcloud logging sessions
{: #session_list}

Elenca le sessioni attive e i rispettivi ID.

```
ibmcloud logging sessions [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID]
```
{: codeblock}

**Parametri**

<dl>

  <dt>-r,--resource-type RESOURCE_TYPE</dt>
      <dd>(Facoltativo) Imposta il tipo di risorsa. I valori validi sono: *space*, *account* e *org* </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
      <dd>(Facoltativo) Imposta questo campo sull'ID di uno spazio, un'organizzazione o un account. <br>Per impostazione predefinita, se non specifichi questo parametro, il comando usa l'ID della risorsa dove sei collegato.  </dd>
</dl>

**Valori restituiti**

<dl>	
    <dt>SESSION_ID</dt>
    <dd>L'ID della sessione attiva.</dd>
	   
    <dt>Resource ID</dt>
    <dd>L'ID della risorsa per cui è valida la sessione.</dd>

    <dt>CreateTime</dt>
    <dd>La data/ora che corrisponde alla data e all'ora in cui è stata creata la sessione.</dd>

    <dt>AccessTime</dt>
    <dd>La data/ora che indica quando la sessione è stata utilizzata l'ultima volta.</dd>
</dl>
 
**Esempio**

```
ibmcloud logging sessions
Listing sessions of resource: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx ...

ID                                     Space                                  CreateTime                       AccessTime   
1ef776d1-4d25-4297-9693-882606c725c8   xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx   2017-11-16T11:52:06.376125207Z   2017-11-16T11:52:06.376125207Z   
Listed the sessions of resource xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 
```
:{ screen}


## ibmcloud logging session-show
{: #session_show}

Visualizza lo stato di una sola sessione.

```
ibmcloud logging session-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] SESSION_ID

```
{: codeblock}

**Parametri**

<dl>
   <dt>-r,--resource-type RESOURCE_TYPE</dt>
      <dd>(Facoltativo) Imposta il tipo di risorsa. I valori validi sono: *space*, *account* e *org* </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
      <dd>(Facoltativo) Imposta questo campo sull'ID di uno spazio, un'organizzazione o un account. <br>Per impostazione predefinita, se non specifichi questo parametro, il comando usa l'ID della risorsa dove sei collegato.  </dd>
</dl>

**Argomenti**

<dl>
   <dt>SESSION_ID</dt>
   <dd>L'ID della sessione attiva di cui desideri ottenere le informazioni.</dd>
</dl>

**Esempio**

Per visualizzare i dettagli di una sessione con ID sessione *cI6hvAa0KR_tyhjxZZz9Uw==*, esegui il seguente comando:

```
ibmcloud logging session-show cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}

## ibmcloud logging token-get
{: #tokenget}

Restituisce il token di registrazione necessario per inviare i dati di log a {{site.data.keyword.loganalysisshort}}.

```
ibmcloud logging token-get [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID]
```
{: codeblock}

**Parametri**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facoltativo) Imposta il tipo di risorsa a cui pensi di inviare i dati di log. I valori validi sono: *space*, *account* e *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facoltativo) Imposta questo campo sull'ID di uno spazio, un'organizzazione o un account. <br>Per impostazione predefinita, se non specifichi questo parametro, il comando usa l'ID della risorsa dove sei collegato. 
  </dd>
</dl>


**Esempio**

```
ibmcloud logging token-get -r space -i js7ydf98-8682-430d-bav4-36b712341744
Getting log token of resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Tenant Id                              Logging Token   
js7ydf98-8682-430d-bav4-36b712341744   xxxxxxxxxx   
```
{: screen}


## ibmcloud logging log-show
{: #status}

Restituisce le informazioni sui log raccolti in uno spazio o in un account {{site.data.keyword.Bluemix_notm}}.

```
ibmcloud logging log-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-l, --list-type-detail]
```
{: codeblock}

* Quando il tipo di risorsa non viene specificato, il comando restituisce i dettagli della risorsa dove sei collegato.
* Se specifichi un tipo di risorsa, devi specificare l'ID risorsa.
* Il comando segnala solo le informazioni sulle ultime 2 settimane di log archiviati in Raccolta dei log quando non vengono specificate date di inizio e fine.

**Parametri**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facoltativo) Imposta il tipo di risorsa. I valori validi sono: *space*, *account* e *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facoltativo) Imposta questo campo sull'ID di uno spazio, un'organizzazione o un account. <br>Per impostazione predefinita, se non specifichi questo parametro, il comando usa l'ID della risorsa dove sei collegato. 
  </dd>
  
  <dt>-s, --start START_DATE</dt>
  <dd>(Facoltativo) Imposta la data di inizio in Coordinated Universal Time (UTC): *YYYY-MM-DD*, ad esempio, `2006-01-02`. <br>Il valore predefinito viene impostato su 2 settimane fa.
  </dd>
  
  <dt>-e, --end END_DATE</dt>
  <dd>(Facoltativo) Imposta la data di fine in Coordinated Universal Time (UTC): *YYYY-MM-DD*, ad esempio, `2006-01-02`. <br>Il valore predefinito viene impostato sulla data corrente.
  </dd>
  
  <dt>-t, --type, LOG_TYPE</dt>
  <dd>(Facoltativo) imposta il tipo di log. <br>Ad esempio, *syslog* è un tipo di log. <br>Il valore predefinito è impostato su asterisco (*). <br>Puoi specificare più tipi di log separando ogni tipo con una virgola, ad esempio *log_type_1,log_type_2,log_type_3*.
  </dd>
  
  <dt>-l, --list-type-detail</dt>
  <dd>(Facoltativo) Imposta questo parametro per elencare ciascun tipo di log singolarmente.
  </dd>
</dl>


**Esempio**

```
ibmcloud logging log-show
Showing log status of resource: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx ...

Date         Size        Count    Searchable   Types   
2017-11-07   1878197     1333     None         default   
2017-11-13   201653512   179391   All          default,linux_syslog   
2017-11-14   32134119    30425    All          default,linux_syslog   
2017-11-15   303901156   269689   All          linux_syslog,default   
2017-11-16   107253679   96648    All          default,linux_syslog   
```
{: screen}

```
 ibmcloud logging log-show -l
Showing log status of resource: cedc73c5-6d55-4193-a9de-378620d6fab5 ...

Date         Size        Count    Searchable   Type
2017-11-14   30146764    26611    true         default
2017-11-14   1987355     3814     true         linux_syslog
2017-11-15   303004895   267890   true         default
2017-11-15   896261      1799     true         linux_syslog
2017-11-16   107918249   96278    true         default
2017-11-16   912890      1794     true         linux_syslog   
```
{: screen}
