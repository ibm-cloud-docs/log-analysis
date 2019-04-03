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

# Laufzeitanwendungsprotokollierung durch CF-Apps
{: #logging_writing_to_log_from_cf_app}

Wenn Sie in {{site.data.keyword.Bluemix}} Protokolldaten für eine Cloud Foundry-App und ihre Laufzeitumgebung speichern möchten, müssen Sie Ihre Protokolle in die Standardausgabe (STDOUT) und Standardfehlerausgabe (STDERR) schreiben. 
{:shortdesc}

In {{site.data.keyword.Bluemix_notm}} werden STDOUT- und STDERR-Protokolleinträge automatisch erfasst:

* STDOUT (Standardausgabe) stellt allgemeine Informationen zur Verfügung.  
* STDERR (Standardfehlerausgabe) stellt Informationen zur Verfügung, die Fehlernachrichten und andere Warnungen zur Diagnose enthalten. 

Loggregator ruft Daten in der Standardausgabe und Standardfehlerausgabe automatisch ab. Loggregator ist die Komponente, die Protokolle aus Cloud Foundry heraus weiterleitet. 

Beispiel: 

Für eine **Liberty Cloud Foundry-App** wird das Standardkonsolenprotokoll (console.log) für den Liberty-Server automatisch von Loggregator erfasst. 

* Das Konsolenprotokoll enthält die umgeleiteten STDOUT- und STDERR-Daten aus dem JVM-Prozess. Die Konsolenausgabe enthält wichtige Ereignisse und Fehler, wenn Sie die Standardkonfiguration "consoleLogLevel" verwenden. Die Konsolenausgabe enthält außerdem alle Nachrichten, die an die Datenströme "system.out" und "system.err" geschrieben werden, wenn Sie die Standardkonfiguration "copySystemStreams" verwenden. Die Konsolenausgabe enthält immer Nachrichten, die direkt vom JVM-Prozess geschrieben werden, wie zum Beispiel Ausgaben mit der Option "-verbose:gc". Sie können die Protokollstufe von Liberty über die Datei "server.xml" anpassen.
* Die Konfiguration "consoleLogLevel" legt die Filterebene des Konsolenprotokollhandlers fest. Wenn Sie "consoleLogLevel" auf den Wert INFO setzen, konfigurieren Sie dadurch, dass alle Nachrichten der Protokollstufen INFO, AUDIT, WARNING und ERROR in die Datei "console.log" geschrieben werden. **Hinweis:** Protokolleinträge der Stufen FINE, FINER und FINEST werden nur in die Datei "trace.log" geschrieben.

Weitere Informationen zu Liberty for Java™-Anwendungen finden Sie unter
[Liberty Profile: Protokollierung und Trace ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](http://www-01.ibm.com/support/knowledgecenter/was_beta_liberty/com.ibm.websphere.wlp.nd.multiplatform.doc/ae/rwlp_logging.html){: new_window}.

Für eine **Node.js-Cloud Foundry-App** können Sie das Protokollierungsmodul "Built in Console" zur Konfiguration der Protokollierung für die Laufzeit in {{site.data.keyword.Bluemix}} verwenden. Sie können Nachrichten an die Standardausgabe (STDOUT) und die Standardfehlerausgabe (STDERR) leiten:

* console.log ('message') sendet die Nachricht an den STDOUT-Datenstrom.
* console.error ('error_message') sendet die Fehlernachricht an den STDERR-Datenstrom.

Weitere Informationen zu Node.js-Anwendungen finden Sie unter [Protokollierung in Node.js![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](https://docs.nodejitsu.com/articles/intermediate/how-to-log/){: new_window}.


Weitere Informationen zu **Ruby on Rails-Anwendungen** finden Sie unter [The Logger ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](http://guides.rubyonrails.org/debugging_rails_applications.html#the-logger){: new_window}.

In der folgenden Tabelle wird die Zuordnung zwischen den Protokollen einiger Anwendungslaufzeiten und den Protokollen, die automatisch von Loggregator erfasst werden, dargestellt:

| **Laufzeit** |    **STDOUT**     | **STDERR** |
|-----------------|-------------------|-------------------|
| Liberty | system.out | system.err |
| Node.js | console.log, console.info | console.error, console.warn |
| Ruby | stdout| stderr |
{: caption="Tabelle 1. Zuordnung zwischen den Protokollen einiger Anwendungslaufzeiten und den Protokollen, die automatisch von Loggregator erfasst werden" caption-side="top"}

