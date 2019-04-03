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

# CLI IBM Cloud Log Analysis (plugin CF)
{: #logging_cli}

La CLI {{site.data.keyword.loganalysislong}} è un plugin per gestire i log per le risorse cloud in esecuzione in uno spazio di un'organizzazione {{site.data.keyword.Bluemix}}.
{: shortdesc}

**Prerequisiti **
* Prima di eseguire i comandi di registrazione, accedi a {{site.data.keyword.Bluemix_notm}} con il comando `ibmcloud login` per generare un token di accesso {{site.data.keyword.Bluemix_short}}
 e autenticare la tua sessione. Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).

Per informazioni su come utilizzare la CLI {{site.data.keyword.loganalysisshort}}, vedi [Gestione dei log](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#log_analysis_ov).

<table>
  <caption>Comandi per la gestione dei log</caption>
  <tr>
    <th>Comando</th>
    <th>Quando utilizzarlo</th>
  </tr>
  <tr>
    <td>[ibmcloud cf logging](#base)</td>
    <td>Utilizza questo comando per ottenere le informazioni sulla CLI, come la versione o l'elenco dei comandi.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging auth](#auth)</td>
    <td>Utilizza questo comando per ottenere il token di registrazione che puoi utilizzare per inviare i log al servizio {{site.data.keyword.loganalysisshort}}.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging delete](#delete)</td>
    <td>Utilizza questo comando per eliminare i log archiviati in Raccolta dei log.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging download (Beta)](#download)</td>
    <td>Utilizza questo comando per scaricare i log dalla raccolta dei log in un file locale o per inviarli ad un altro programma come lo stack Elastic. </td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging help](#help)</td>
    <td>Utilizza questo comando per ottenere supporto su come utilizzare la CLI e per ottenere un elenco di tutti i comandi.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging option](#option)</td>
    <td>Utilizza questo comando per visualizzare o configurare il periodo di conservazione per i log disponibili in uno spazio o in un account.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging session create (Beta)](#session_create1)</td>
    <td>Utilizza questo comando per creare una nuova sessione.</td>
  <tr>
  <tr>
    <td>[ibmcloud cf logging session delete (Beta)](#session_delete1)</td>
    <td>Utilizza questo comando per eliminare una sessione.</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging session list (Beta)](#session_list1)</td>
    <td>Utilizza questo comando per elencare le sessioni attive e i rispettivi ID.</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging session show (Beta)](#session_show1)</td>
    <td>Utilizza questo comando per visualizzare lo stato di una sola sessione.</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging status](#status1)</td>
    <td>Utilizza questo comando per ottenere le informazioni sui log raccolti in uno spazio o in un account.</td>
  </tr>
  </table>


## ibmcloud cf logging
{: #base1}

Fornisce le informazioni sulla versione della CLI e su come utilizzarla.

```
ibmcloud cf logging [parametri]
```
{: codeblock}

**Parametri**

<dl>
<dt>--help, -h</dt>
<dd>Imposta questo parametro per visualizzare l'elenco dei comandi o per ottenere supporto per un comando.
</dd>

<dt>--version, -v</dt>
<dd>Imposta questo parametro per stampare la versione della CLI.</dd>
</dl>

**Esempi**

Per ottenere l'elenco dei comandi, esegui il seguente comando:

```
ibmcloud cf logging --help
```
{: codeblock}

Per ottenere la versione della CLI, esegui il seguente comando:

```
ibmcloud cf logging --version
```
{: codeblock}


## ibmcloud cf logging auth
{: #auth}

Restituisce un token di registrazione che puoi utilizzare per inviare i log al servizio {{site.data.keyword.loganalysisshort}}. 

**Nota:** il token non scade.

```
ibmcloud cf logging auth
```
{: codeblock}

**Restituisce**

<dl>
  <dt>Token di registrazione</dt>
  <dd>Ad esempio, `jec8BmipiEZc`.
  </dd>
  
  <dt>ID organizzazione</dt>
  <dd>GUID dell'organizzazione {{site.data.keyword.Bluemix_notm}} per cui hai eseguito l'accesso.
  </dd>
  
  <dt>ID spazio</dt>
  <dd>GUID dello spazio all'interno dell'organizzazione per cui hai eseguito l'accesso.
  </dd>
</dl>

## ibmcloud cf logging delete
{: #delete2}

Elimina i log archiviati in Raccolta dei log.

```
ibmcloud cf logging delete [parametri]
```
{: codeblock}

**Parametri**

<dl>
  <dt>--start value, -s value</dt>
  <dd>(Facoltativo) Imposta la data di inizio in Coordinated Universal Time (UTC): *YYYY-MM-DD*, ad esempio, `2006-01-02`. <br>Il valore predefinito viene impostato su 2 settimane fa.
  </dd>
  
  <dt>--end value, -e value</dt>
  <dd>(Facoltativo) Imposta la data di fine in Coordinated Universal Time (UTC): *YYYY-MM-DD* <br>Il formato UTC della data è **YYYY-MM-DD**, ad esempio, `2006-01-02`. <br>Il valore predefinito viene impostato sulla data corrente.
  </dd>
  
  <dt>--type value, -t value</dt>
  <dd>(Facoltativo) imposta il tipo di log. <br>Ad esempio, *syslog* è un tipo di log. <br>Il valore predefinito viene impostato su **\***. <br>Puoi specificare più tipi di log sperando ogni tipo con una virgola, ad esempio, **log_type_1,log_type_2,log_type_3*.
  </dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>(Facoltativo) imposta l'ambito delle informazioni sul log fornite al livello dell'account. <br>Se questo parametro non viene specificato, viene impostato il valore predefinito per fornire le informazioni sul log solo per lo spazio corrente.
  </dd>
</dl>

**Esempio**

Per eliminare i log di tipo *linux_syslog* per il 25 maggio 2017, esegui il seguente comando:
```
ibmcloud cf logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
```
{: codeblock}



## ibmcloud cf logging download (Beta)
{: #download4}

Scarica i log dalla raccolta dei log in un file locale o li invia a un altro programma come uno stack Elastic. 

**Nota:** per scaricare i file, devi prima creare una sessione. Una sessione definisce quali log scaricare in base all'intervallo di date, al tipo di log e al tipo di account. Scarica i log nel contesto di una sessione. Per ulteriori informazioni, vedi [ibmcloud cf logging session create (Beta)](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-logging_cli#session_create1).

```
ibmcloud cf logging download [parametri] [argomenti]
```
{: codeblock}

**Parametri**

<dl>
<dt>--output value, -o value</dt>
<dd>(Facoltativo) imposta il percorso e il nome del file per il file di output locale in cui vengono scaricati i log. <br>Il valore predefinito è un trattino (-). <br>Imposta questo parametro sul valore predefinito per inviare i log all'output standard.</dd>
</dl>

**Argomenti**

<dl>
<dt>ID_sessione</dt>
<dd>Imposta sul valore di ID sessione che ottieni quando esegui il comando `ibmcloud cf logging session create`. Questo valore indica quale sessione utilizzare quando scarichi i log. <br>**Nota:** il comando `ibmcloud cf logging session create` fornisce i parametri che controllano quali log vengono scaricati. </dd>
</dl>

**Nota:** dopo che lo scaricamento è terminato, rieseguendo lo stesso comando non succederà nulla. Per riscaricare gli stessi dati, devi utilizzare un file o una sessione differenti.

**Esempi**

In un sistema Linux, per scaricare i log in un file denominato mylogs.gz, esegui questo comando:

```
ibmcloud cf logging download -o mylogs.gz guBeZTIuYtreOPi-WMnbUg==
```
{: screen}

Per scaricare i log nel tuo proprio stack Elastic, esegui il seguente comando:

```
ibmcloud cf logging download guBeZTIuYtreOPi-WMnbUg== | gunzip | logstash -f logstash.conf
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


## ibmcloud cf logging help
{: #help1}

Fornisce le informazioni su come utilizzare un comando.

```
ibmcloud cf logging help [comando]
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
ibmcloud cf logging help status
```
{: codeblock}


## ibmcloud cf logging option
{: #option}

Visualizza o modifica il periodo di conservazione per i log disponibili in uno spazio o in un account. 

* Il periodo è impostato per numero di giorni.
* Il valore predefinito è **-1**. 

**Nota:** per impostazione predefinita sono archiviati tutti i log. Devi eliminarli manualmente utilizzando il comando **delete**. Imposta una politica di conservazione per eliminare i log automaticamente.

```
ibmcloud cf logging option [parametri]
```
{: codeblock}

**Parametri**

<dl>
<dt>--retention value, -r value</dt>
<dd>(Facoltativo) imposta il numero di giorni di conservazione. <br> Il valore predefinito è *-1* giorni.</dd>

<dt>--at-account-level, -a </dt>
  <dd>(Facoltativo) imposta l'ambito al livello dell'account. <br>Se questo parametro non viene specificato, il valore predefinito è impostato su *-1* per lo spazio corrente, che è lo spazio in cui hai effettuato l'accesso utilizzando il comando `ibmcloud cf login`.
  </dd>
</dl>

**Esempi**

Per visualizzare il periodo di conservazione corrente predefinito per lo spazio in cui hai eseguito l'accesso, esegui il seguente comando:

```
ibmcloud cf logging option
```
{: codeblock}

L'output è:

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-ibmcloud cfgh436902a3 |        -1 |
+--------------------------------------+-----------+
```
{: screen}


Per modificare il periodo di conservazione in 25 giorni per lo spazio in cui hai eseguito l'accesso, esegui il seguente comando:

```
ibmcloud cf logging option -r 25
```
{: codeblock}

L'output è:

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-ibmcloud cfgh436902a3 |        25 |
+--------------------------------------+-----------+
```
{: screen}


## ibmcloud cf logging session create (Beta)
{: #session_create1}

Crea una nuova sessione.

**Nota:** puoi avere fino a 30 sessioni simultanee in uno spazio. La sessione viene creata per un utente. Le sessioni non possono essere condivise tra gli utenti in uno spazio.

```
ibmcloud cf logging session create [parametri]
```
{: codeblock}

**Parametri**

<dl>
  <dt>--start value, -s value</dt>
  <dd>(Facoltativo) Imposta la data di inizio in Coordinated Universal Time (UTC): *YYYY-MM-DD*, ad esempio, `2006-01-02`. <br>Il valore predefinito viene impostato su 2 settimane fa.
  </dd>
  
  <dt>--end value, -e value</dt>
  <dd>(Facoltativo) Imposta la data di fine in Coordinated Universal Time (UTC): *YYYY-MM-DD*, ad esempio, `2006-01-02`. <br>Il valore predefinito viene impostato sulla data corrente.
  </dd>
  
  <dt>--type value, -t value</dt>
  <dd>(Facoltativo) imposta il tipo di log. <br>Ad esempio, *syslog* è un tipo di log. <br>Il valore predefinito è impostato su asterisco (*). <br>Puoi specificare più tipi di log separando ogni tipo con una virgola, ad esempio *log_type_1,log_type_2,log_type_3*.
  </dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>(Facoltativo) imposta l'ambito al livello dell'account. <br>Se questo parametro non viene specificato, il valore predefinito viene impostato solo sullo spazio corrente, ovvero lo spazio in cui hai effettuato l'accesso utilizzando il comando `ibmcloud cf login`.
  </dd>
</dl>

**Valori restituiti**

<dl>
<dt>Ora-Accesso</dt>
<dd>La data/ora che indica quando la sessione è stata utilizzata l'ultima volta.</dd>

<dt>Ora-Creazione</dt>
<dd>La data/ora che corrisponde alla data e all'ora in cui è stata creata la sessione.</dd>

<dt>Intervallo-Date</dt>
<dd>Indica i giorni che sono stati utilizzati per filtrare i log. Il log identificati in questo intervallo di date sono disponibili per la gestione tramite la sessione.</dd>

<dt>ID</dt>
<dd>ID sessione.</dd>

<dt>Spazio</dt>
<dd>L'ID dello spazio in cui è attiva la sessione.</dd>

<dt>Account-Tipo</dt>
<dd>I tipi di log scaricati tramite la sessione.</dd>

<dt>Nome utente</dt>
<dd>L'ID {{site.data.keyword.IBM_notm}} dell'utente che ha creato la sessione.</dd>
</dl>


**Esempio**

Per creare una sessione che include i log tra il 20 maggio 2017 e il 26 maggio 2017 per un tipo di log di *log*, esegui il seguente comando:

```
ibmcloud cf logging session create -s 2017-05-20 -e 2017-05-26 -t log
```
{: screen}


## ibmcloud cf logging session delete (Beta)
{: #session_delete1}

Elimina una sessione, specificata per ID sessione.

```
ibmcloud cf logging session delete [argomenti]
```
{: codeblock}

**Argomenti**

<dl>
<dt>ID sessione</dt>
<dd>L'ID della sessione che desideri eliminare. <br>Puoi utilizzare il comando `ibmcloud cf logging session list` per ottenere tutti gli ID delle sessioni attive.</dd>
</dl>

**Esempio**

Per eliminare una sessione con ID sessione *cI6hvAa0KR_tyhjxZZz9Uw==*, esegui il seguente comando:

```
ibmcloud cf logging session delete cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}



## ibmcloud cf logging session list (Beta)
{: #session_list1}

Elenca le sessioni attive e i rispettivi ID.

```
ibmcloud cf logging session list 
```
{: codeblock}

**Valori restituiti**

<dl>
<dt>ID</dt>
<dd>ID sessione.</dd>

<dt>SPAZIO</dt>
<dd>L'ID dello spazio in cui è attiva la sessione.</dd>

<dt>NOME UTENTE</dt>
<dd>L'ID {{site.data.keyword.IBM_notm}} dell'utente che ha creato la sessione.</dd>

<dt>ORA-CREAZIONE</dt>
<dd>La data/ora che corrisponde alla data e all'ora in cui è stata creata la sessione.</dd>

<dt>ORA-ACCESSO</dt>
<dd>La data/ora che indica quando la sessione è stata utilizzata l'ultima volta.</dd>
</dl>
 

## ibmcloud cf logging session show (Beta)
{: #session_show1}

Visualizza lo stato di una sola sessione.

```
ibmcloud cf logging session show [argomenti]
```
{: codeblock}

**Argomenti**

<dl>
<dt>ID_sessione</dt>
<dd>L'ID della sessione attiva di cui desideri ottenere le informazioni.</dd>
</dl>

**Valori restituiti**

<dl>
<dt>Ora-Accesso</dt>
<dd></dd>

<dt>Ora-Creazione</dt>
<dd>La data/ora che corrisponde alla data e all'ora in cui è stata creata la sessione.</dd>

<dt>Intervallo-Date</dt>
<dd>Indica i giorni che sono stati utilizzati per filtrare i log. Il log identificati in questo intervallo di date sono disponibili per la gestione tramite la sessione.</dd>

<dt>ID</dt>
<dd>ID sessione.</dd>

<dt>Spazio</dt>
<dd>L'ID dello spazio in cui è attiva la sessione.</dd>

<dt>Account-Tipo</dt>
<dd>I tipi di log scaricati tramite la sessione.</dd>

<dt>Nome utente</dt>
<dd>L'ID {{site.data.keyword.IBM_notm}} dell'utente che ha creato la sessione.</dd>
</dl>

**Esempio**

Per visualizzare i dettagli di una sessione con ID sessione *cI6hvAa0KR_tyhjxZZz9Uw==*, esegui il seguente comando:

```
ibmcloud cf logging session show cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}


## ibmcloud cf logging status
{: #status1}

Restituisce le informazioni sui log raccolti in uno spazio o in un account.

```
ibmcloud cf logging status [parametri]
```
{: codeblock}

**Parametri**

<dl>
  <dt>--start value, -s value</dt>
  <dd>(Facoltativo) Imposta la data di inizio in Coordinated Universal Time (UTC): *YYYY-MM-DD*, ad esempio, `2006-01-02`. <br>Il valore predefinito viene impostato su 2 settimane fa.
  </dd>
  
  <dt>--end value, -e value</dt>
  <dd>(Facoltativo) Imposta la data di fine in Coordinated Universal Time (UTC): *YYYY-MM-DD*, ad esempio, `2006-01-02`. <br>Il valore predefinito viene impostato sulla data corrente.
  </dd>
  
  <dt>--type value, -t value</dt>
  <dd>(Facoltativo) imposta il tipo di log. <br>Ad esempio, *syslog* è un tipo di log. <br>Il valore predefinito è impostato su asterisco (*). <br>Puoi specificare più tipi di log separando ogni tipo con una virgola, ad esempio *log_type_1,log_type_2,log_type_3*.
  </dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>(Facoltativo) imposta l'ambito al livello dell'account. <br> **Nota:** imposta questo valore per ottenere le informazioni sull'account. <br>Se questo parametro non viene specificato, il valore predefinito viene impostato solo sullo spazio corrente, ovvero lo spazio in cui hai effettuato l'accesso utilizzando il comando `ibmcloud cf login`.
  </dd>
  
  <dt>--list-type-detail, -l</dt>
  <dd>(Facoltativo) imposta questo parametro per elencare il totale dei tipi di log per ogni giorno.
  </dd>
</dl>

**Nota:** il comando `ibmcloud cf logging status` restituisce solo le ultime due settimane di log archiviati in Raccolta dei log quando non vengono specificate una data di inizio e di fine.


