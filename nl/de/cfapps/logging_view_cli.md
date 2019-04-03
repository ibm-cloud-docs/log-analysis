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


# CF-Protokolle über die Befehlszeilenschnittstelle analysieren
{: #analyzing_logs_cli}

In {{site.data.keyword.Bluemix}} können Sie Protokolle über die Befehlszeilenschnittstelle (CLI) anzeigen. 
{:shortdesc}

Verwenden Sie zur Analyse von Cloud Foundry-Anwendungsprotokollen den folgenden Befehl: `ibmcloud cf logs`
Weitere Informationen finden Sie unter [cf logs](/docs/cli/reference/ibmcloud?topic=cloud-cli-cf#cf_logs).


## CF-App-Protokolle über die Befehlszeilenschnittstelle analysieren
{: #analyzing_cf_logs_cli}

Verwenden Sie den Befehl **cf logs**, um Protokolle über eine Cloud Foundry-App und die Systemkomponenten anzuzeigen, die mit ihr interagieren, wenn Sie die App in {{site.data.keyword.Bluemix_notm}} bereitstellen. Der Befehl **cf logs** zeigt die Protokolldatenströme STDOUT und STDERR einer Cloud Foundry-Anwendung an.

Um die Protokolle anzuzeigen, an denen Sie interessiert sind, oder um Inhalte auszuschließen, die Sie nicht anzeigen möchten, können Sie den Befehl **cf logs** mit Filteroptionen wie **cut** und **grep** in der 'cf'-Befehlszeilenschnittstelle verwenden:

* Informationen zum Anzeigen der Protokolle für eine Cloud Foundry-App finden Sie unter [Protokoll für eine Cloud Foundry-App anzeigen](/docs/services/CloudLogAnalysis/cfapps?topic=cloudloganalysis-analyzing_logs_cli#full_log_cli).
* Informationen zum Anzeigen der neuesten Protokolldatensätze für eine Cloud Foundry-App finden Sie unter [Neueste Protokolleinträge für eine Cloud Foundry-App anzeigen](/docs/services/CloudLogAnalysis/cfapps?topic=cloudloganalysis-analyzing_logs_cli#tailing_log_cli).
* Informationen zum Anzeigen der Protokolldatensätze für eine Cloud Foundry-App in einem bestimmten Zeitbereich finden Sie unter [Abschnitt eines Cloud Foundry-Protokolls anzeigen](/docs/services/CloudLogAnalysis/cfapps?topic=cloudloganalysis-analyzing_logs_cli#partial_log_cli).
* Informationen zum Anzeigen von Einträgen in den Protokollen für eine Cloud Foundry-App, die bestimmte Schlüsselwörter enthalten, finden Sie unter [Protokolleinträge anzeigen, die bestimmte Schlüsselwörter enthalten](logging_view_cli.html#partial_by_keyword_log_cli).


### Protokoll für eine Cloud Foundry-App anzeigen
{: #full_log_cli}

Führen Sie die folgenden Schritte aus, um alle für eine Cloud Foundry-App verfügbaren Protokolle anzuzeigen:

1. Öffnen Sie ein Terminal und melden Sie sich bei {{site.data.keyword.Bluemix_notm}} an.

2. Führen Sie den folgenden Befehl von der Befehlszeile aus, um alle Protokolle anzuzeigen:

   <pre class="pre screen"><code> ibmcloud cf logs <var class="keyword varname">App-Name</var></code></pre>
   
   
### Neueste Protokolleinträge für eine Cloud Foundry-App anzeigen
{: #tailing_log_cli}

Führen Sie die folgenden Schritte aus, um die neuesten für eine Cloud Foundry-App verfügbaren Protokolle anzuzeigen:

1. Öffnen Sie ein Terminal und melden Sie sich bei {{site.data.keyword.Bluemix_notm}} an.

2. Führen Sie den folgenden Befehl von der Befehlszeile aus, um alle Protokolle anzuzeigen:

     <pre class="pre screen"><code>ibmcloud cf logs <var class="keyword varname">App-Name</var> --recent</code></pre>

<div class="note tip"><span class="tiptitle">Tipp:</span> Wenn Sie den Befehl <span class="keyword cmdname">cf push</span> oder <span class="keyword cmdname">cf start</span> in einem Befehlszeilenfenster ausführen, können Sie <samp class="ph codeph">cf logs appname --recent</samp> in einem anderen Befehlszeilenfenster eingeben, um die Protokolle in Echtzeit zu sehen. </div>


### Abschnitt eines Cloud Foundry-Protokolls anzeigen
{: #partial_log_cli}

Führen Sie die folgenden Schritte aus, um einen Teil der für eine Cloud Foundry-App verfügbaren Protokolle in einem bestimmten Zeitbereich anzuzeigen:

1. Öffnen Sie ein Terminal und melden Sie sich bei {{site.data.keyword.Bluemix_notm}} an.

2. Führen Sie den folgenden Befehl von der Befehlszeile aus, um alle Protokolle anzuzeigen:

    <pre class="pre screen"><code>ibmcloud cf logs <var class="keyword varname">App-Name</var> --recent  | cut -c 29-40,46-</code></pre>
    
    Weitere Informationen zur Option **cut** können Sie durch Eingabe von **cut --help** abrufen.


### Protokolleinträge anzeigen, die bestimmte Schlüsselwörter enthalten
{: #partial_by_keyword_log_cli}

Führen Sie die folgenden Schritte aus, um Protokolleinträge anzuzeigen, die bestimmte Schlüsselwörter für eine Cloud Foundry-App enthalten:

1. Öffnen Sie ein Terminal und melden Sie sich bei {{site.data.keyword.Bluemix}} an.

2. Führen Sie den folgenden Befehl von der Befehlszeile aus, um alle Protokolle anzuzeigen:

    <pre class="pre screen"><code>ibmcloud cf logs <var class="keyword varname">App-Name</var> --recent | grep '<var class="keyword varname">Schlüsselwort</var>'</code></pre>
    

Beispiel: Um Protokolleinträge anzuzeigen, die das Schlüsselwort **APP** enthalten, können Sie den folgenden Befehl verwenden:

<pre class="pre screen"><code>ibmcloud cf logs appname --recent | grep '\[App'</code></pre>

Weitere Informationen zur Option **grep** können Sie durch Eingabe von **grep --help** abrufen.


### Cloud Foundry-Anwendungsprotokolle
{: #cf_app_logs_cli}

Die folgenden Protokolle sind für eine Cloud Foundry-Anwendung verfügbar, nachdem Sie sie in {{site.data.keyword.Bluemix_notm}} bereitgestellt haben:

**buildpack.log**

Diese Protokolldatei zeichnet differenzierte Informationsereignisse für das Debugging auf. Mithilfe dieses Protokolls können Sie Probleme bei der Buildpack-Ausführung beheben.

Um Daten für die Datei *buildpack.log* zu generieren, müssen Sie das Buildpack-Tracing aktivieren, indem Sie folgenden Befehl eingeben: `cf set-env appname JBP_LOG_LEVEL DEBUG`
   
Um dieses Protokoll anzuzeigen, geben Sie den folgenden Befehl ein: `cf files appname app/.buildpack-diagnostics/buildpack.log`


**staging_task.log**

Diese Protokolldatei zeichnet Nachrichten nach den Hauptschritten der Staging-Task auf. Mithilfe dieses Protokolls können Sie Staging-Probleme beheben.

Um dieses Protokoll anzuzeigen, geben Sie den folgenden Befehl ein: `ibmcloud cf files appname logs/staging_task.log`




