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


# Analisi dei log CF dalla CLI
{: #analyzing_logs_cli}

In {{site.data.keyword.Bluemix}}, puoi visualizzare, filtrare e analizzare i log tramite l'interfaccia riga di comando (CLI). 
{:shortdesc}

Per analizzare i log dell'applicazione CF (Cloud Foundry) utilizza il seguente comando: `ibmcloud cf logs`
Per ulteriori informazioni, vedi [cf logs](/docs/cli/reference/ibmcloud?topic=cloud-cli-cf#cf_logs).


## Analisi dei log dell'applicazione CF dalla CLI
{: #analyzing_cf_logs_cli}

Utilizza il comando **cf logs** per visualizzare i log da un'applicazione Cloud Foundry e dai componenti di sistema che interagiscono con essa quando la distribuisci in {{site.data.keyword.Bluemix_notm}}. Il comando **cf logs** visualizza i flussi di log STDOUT e STDERR di un'applicazione Cloud Foundry.

Per visualizzare i log che ti interessano o per escludere i contenuti che non vuoi visualizzare, puoi utilizzare il comando **cf logs** con le opzioni di filtro come **cut** e **grep** nell'interfaccia riga di comando cf:

* Per visualizzare i log di un'applicazione Cloud Foundry, vedi [Visualizzazione dei log per un'applicazione Cloud Foundry](/docs/services/CloudLogAnalysis/cfapps?topic=cloudloganalysis-analyzing_logs_cli#full_log_cli).
* Per visualizzare i record di log più recenti di un'applicazione Cloud Foundry, vedi [Visualizzazione delle ultime voci di log per un'applicazione Cloud Foundry](/docs/services/CloudLogAnalysis/cfapps?topic=cloudloganalysis-analyzing_logs_cli#tailing_log_cli).
* Per visualizzare i record di log di un'applicazione Cloud Foundry in uno specifico intervallo di tempo, vedi [Visualizzazione di una sezione dei log](/docs/services/CloudLogAnalysis/cfapps?topic=cloudloganalysis-analyzing_logs_cli#partial_log_cli).
* Per visualizzare le voci di log di un'applicazione Cloud Foundry che contengono specifiche parole chiave, vedi [Visualizzazione di voci di log contenenti determinate parole chiave](logging_view_cli.html#partial_by_keyword_log_cli).


### Visualizzazione dei log per un'applicazione Cloud Foundry
{: #full_log_cli}

Per visualizzare tutti i log disponibili per un'applicazione Cloud Foundry, completa la seguente procedura:

1. Apri un terminale e accedi a {{site.data.keyword.Bluemix_notm}}.

2. Nella riga di comando, immetti il seguente comando per visualizzare tutti i log:

   <pre class="pre screen"><code> ibmcloud cf logs <var class="keyword varname">appname</var></code></pre>
   
   
### Visualizzazione delle ultime voci di log per un'applicazione Cloud Foundry
{: #tailing_log_cli}

Per visualizzare i log più recenti disponibili per un'applicazione Cloud Foundry, completa la seguente procedura:

1. Apri un terminale e accedi a {{site.data.keyword.Bluemix_notm}}.

2. Nella riga di comando, immetti il seguente comando per visualizzare tutti i log:

     <pre class="pre screen"><code>ibmcloud cf logs <var class="keyword varname">appname</var> --recent</code></pre>

<div class="note tip"><span class="tiptitle">Suggerimento:</span> quando esegui il comando <span class="keyword cmdname">cf push</span> o <span class="keyword cmdname">cf
start</span> in una finestra della riga di comando, puoi immettere <samp class="ph codeph">cf logs appname --recent</samp> in un'altra finestra di riga di comando per visualizzare i log in tempo reale. </div>


### Visualizzazione di una sezione di un log Cloud Foundry
{: #partial_log_cli}

Per visualizzare una parte dei log disponibili per un'applicazione Cloud Foundry all'interno di un intervallo di tempo, completa la seguente procedura:

1. Apri un terminale e accedi a {{site.data.keyword.Bluemix_notm}}.

2. Nella riga di comando, immetti il seguente comando per visualizzare tutti i log:

    <pre class="pre screen"><code>ibmcloud cf logs <var class="keyword varname">appname</var> --recent  | cut -c 29-40,46-</code></pre>
    
    Per ulteriori informazioni sull'opzione **cut**, immetti **cut --help**.


### Visualizzazione di voci di log contenenti determinate parole chiave
{: #partial_by_keyword_log_cli}

Per visualizzare le voci di log che contengono determinate parole chiave per un'applicazione Cloud Foundry, completa la seguente procedura:

1. Apri un terminale e accedi a {{site.data.keyword.Bluemix}}.

2. Nella riga di comando, immetti il seguente comando per visualizzare tutti i log:

    <pre class="pre screen"><code>ibmcloud cf logs <var class="keyword varname">appname</var> --recent | grep '<var class="keyword varname">keyword</var>'</code></pre>
    

Ad esempio, per visualizzare le voci di log che contengono la parola chiave **APP**, puoi utilizzare il seguente comando:

<pre class="pre screen"><code>ibmcloud cf logs appname --recent | grep '\[App'</code></pre>

Per ulteriori informazioni sull'opzione **grep**, immetti **grep --help**.


### Log dell'applicazione Cloud Foundry
{: #cf_app_logs_cli}

I seguenti log sono disponibili per un'applicazione Cloud Foundry dopo averla distribuita in {{site.data.keyword.Bluemix_notm}}:

**buildpack.log**

Questo file di log registra eventi informativi accurati per il debug. Puoi utilizzare il log per risolvere problemi relativi all'esecuzione dei pacchetti di build.

Per generare dei dati nel file *buildpack.log*, devi abilitare la traccia del pacchetto di build utilizzando il seguente comando: `cf set-env appname JBP_LOG_LEVEL DEBUG`
   
Per visualizzare questo log, immetti il seguente comando: `cf files appname app/.buildpack-diagnostics/buildpack.log`


**staging_task.log**

Questo file di log registra i messaggi dopo i passi principali dell'attività di preparazione. Puoi utilizzare questo log per risolvere i problemi relativi alla preparazione.

Per visualizzare questo log, immetti il seguente comando: `ibmcloud cf files appname logs/staging_task.log`




