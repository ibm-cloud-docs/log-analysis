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


# Protokolle verwalten
{: #manage_logs}

Sie können in 'Log Collection' gespeicherte Protokolle über die {{site.data.keyword.loganalysisshort}}-Befehlszeilenschnittstelle und die {{site.data.keyword.loganalysisshort}}-API verwalten.
{:shortdesc}

Berücksichtigen Sie bei der Verwaltung von Protokollen die folgenden Informationen:

1. Der Benutzer-ID muss eine Richtlinie in {{site.data.keyword.Bluemix_notm}} für {{site.data.keyword.loganalysisshort}} zugewiesen sein, die Berechtigungen zum Verwalten von Protokollen enthält. 

    Eine Liste der IAM-Rollen und den entsprechenden Tasks pro Rolle finden Sie unter [IAM-Rollen](/docs/services/CloudLogAnalysis/security_ov.html#iam_roles). 
	
	Weitere Informationen zum Zuweisen einer Richtlinie finden Sie unter [Benutzern eine IAM-Richtlinie über die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle zuweisen](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_account).
	
2. Diese Funktion ist nur für Servicepläne zur Verfügung, die eine Protokollaufbewahrung zulassen. 

    Weitere Informationen zu Serviceplänen finden Sie unter [Servicepläne](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).

Der {{site.data.keyword.loganalysisshort}}-Service bietet zwei Befehlszeilenschnittstellen, über die Protokolle verwaltet werden können:

* Ein {{site.data.keyword.Bluemix_notm}}-Plug-in für {{site.data.keyword.loganalysisshort}}. Weitere Informationen zu dieser Befehlszeilenschnittstelle finden Sie unter [{{site.data.keyword.loganalysisshort}}-Befehlszeilenschnittstelle ({{site.data.keyword.Bluemix_notm}}-Plug-in)](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#log_analysis_cli).
* Ein CF-Plug-in für {{site.data.keyword.loganalysisshort}} (veraltet). Weitere Informationen zu dieser Befehlszeilenschnittstelle finden Sie unter [Log Analysis-Befehlszeilenschnittstelle (CF-Plug-in) konfigurieren](/docs/services/CloudLogAnalysis/reference/logging_cli.html#logging_cli).


## Protokollaufbewahrungsrichtlinie konfigurieren
{: #log_retention_policy}

Sie können die Befehlszeilenschnittstelle von {{site.data.keyword.loganalysisshort}} verwenden, um eine Protokollaufbewahrungsrichtlinie zu konfigurieren. Die Richtlinie gibt die Dauer (in Tagen) an, für die die Protokolle in 'Log Collection' aufbewahrt werden. 

* Standardmäßig werden bei der Auswahl eines kostenpflichtigen Plans Protokolle in 'Log Collection' erfasst und aufbewahrt. 
* Wenn ein Aufbewahrungszeitraum festgelegt wurde und dieser abgelaufen ist, werden die Protokolle automatisch aus 'Log Collection' gelöscht und können nicht wiederhergestellt werden.
* Sie können einen Aufbewahrungszeitraum für ein Konto angeben. Der Aufbewahrungszeitraum wird automatisch für alle Bereiche in diesem Konto konfiguriert. 
* Sie können einen Aufbewahrungszeitraum für einen Bereich angeben.
* Sie können die Aufbewahrungsrichtlinie jederzeit ändern.
* Sie können die Richtlinie inaktivieren, indem Sie ihren Wert auf *-1* einstellen. 

**Hinweis:** Wenn Sie die Protokollaufbewahrungsrichtlinie inaktivieren, müssen Sie die Protokolle in 'Log Collection' selbst verwalten. Sie können den CLI-Befehl [cf logging delete](/docs/services/CloudLogAnalysis/reference/logging_cli.html#delete4) verwenden, um alte Protokolle zu löschen.

Weitere Informationen finden Sie in den folgenden Abschnitten:

* [Protokollaufbewahrungsrichtlinie mithilfe des {{site.data.keyword.Bluemix_notm}}-Plug-ins anzeigen und konfigurieren](/docs/services/CloudLogAnalysis/how-to/manage-logs/configuring_retention_policy_cloud.html#configuring_retention_policy).
* [Protokollaufbewahrungsrichtlinie mithilfe des CF-Plug-ins anzeigen und konfigurieren](/docs/services/CloudLogAnalysis/how-to/manage-logs/configuring_retention_policy.html#configuring_retention_policy).


## Protokolle löschen
{: #log_deletion}

Protokolle, die in 'Log Search' gespeichert sind, werden nach drei Tagen gelöscht.

Protokolle, die in 'Log Collection' gespeichert sind, werden so lange aufbewahrt, bis Sie entweder eine Aufbewahrungsrichtlinie konfigurieren oder sie manuell löschen. 

* Sie können eine Protokollaufbewahrungsrichtlinie konfigurieren, die die Anzahl Tage definiert, für die Protokolle in 'Log Collection' aufbewahrt werden. Weitere Informationen finden Sie in [Protokollaufbewahrungsrichtlinie mithilfe des {{site.data.keyword.Bluemix_notm}}-Plug-ins anzeigen und konfigurieren](/docs/services/CloudLogAnalysis/how-to/manage-logs/configuring_retention_policy_cloud.html#configuring_retention_policy).

* Sie können die ['Log Collection'-API](https://console.bluemix.net/apidocs/948-ibm-cloud-log-collection-api?&language=node&env_id=ibm%3Ayp%3Aus-south#introduction){: new_window} oder die ['Log Collection'-Befehlszeilenschnittstelle](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#log_analysis_cli){: new_window} verwenden, um Protokolle manuell aus 'Log Collection' zu löschen. 

* Sie können die Befehlszeilenschnittstelle verwenden. Weitere Informationen zum manuellen Löschen von Protokollen über die Befehlszeilenschnittstelle finden Sie in [ibmcloud logging log-delete durch Nutzung des {{site.data.keyword.Bluemix_notm}}-Plug-ins](/docs/services/CloudLogAnalysis/how-to/manage-logs/deleting_logs_cloud.html#deleting_logs).
    


## Protokolle herunterladen
{: #download_logs2}

In Kibana können Sie Protokolle für die letzten 3 Tage durchsuchen. Wenn Sie ältere Protokolldaten analysieren möchten, können Sie die betreffenden Protokolle in eine lokale Datei herunterladen oder Sie können diese Protokolle an andere Programme (zum Beispiel eine lokale Elastic Stack-Instanz) umleiten. 

Weitere Informationen finden Sie in den folgenden Abschnitten:

* [Protokolle mithilfe des {{site.data.keyword.Bluemix_notm}}-Plug-ins herunterladen](/docs/services/CloudLogAnalysis/how-to/manage-logs/downloading_logs_cloud.html#downloading_logs).
* [Protokolle mithilfe des CF-Plug-ins herunterladen](/docs/services/CloudLogAnalysis/how-to/manage-logs/downloading_logs.html#downloading_logs1).



## Informationen zu den Protokollen abrufen
{: #info_about_logs}

Allgemeine Informationen zu Ihren Protokollen können Sie über die Befehle `ibmcloud logging log-show` oder `cf logging status` abrufen. Weitere Informationen finden Sie in den folgenden Abschnitten:

* [Protokollinformationen mithilfe des {{site.data.keyword.Bluemix_notm}}-Plug-ins anzeigen](/docs/services/CloudLogAnalysis/how-to/manage-logs/viewing_log_information_cloud.html#viewing_log_status1)
* [Protokollinformationen mithilfe des CF-Plug-ins anzeigen](/docs/services/CloudLogAnalysis/how-to/manage-logs/viewing_log_information.html#viewing_log_status1).

Zur Kostenkontrolle können Sie unter anderem die Größe der Protokolle Ihrer Apps über einen bestimmten Zeitraum überwachen. Sie können sich beispielsweise über die Größe der einzelnen Protokolltypen für einen {{site.data.keyword.Bluemix_notm}}-Bereich innerhalb einer Woche informieren, um zu ermitteln, ob eine App oder ein Service mehr Protokolle erstellt als erwartet. Um die Größe Ihrer Protokolle zu überprüfen, können Sie die Befehle `ibmcloud logging log-show` oder `cf logging status` verwenden.

Sie können Informationen zu Protokollen anzeigen, die in einer Bereichsdomäne, einer Organisationsdomäne oder ein Kontodomäne gespeichert sind.



## {{site.data.keyword.loganalysisshort_notm}}-Befehlszeilenschnittstelle ({{site.data.keyword.Bluemix_notm}}-Plug-in) installieren
{: #install_cli2}

Informationen zur Installation der Befehlszeilenschnittstelle (CLI) finden Sie unter [Befehlszeilenschnittstelle für Protokollierung installieren](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#config_log_collection_cli).

Um die Version der Befehlszeilenschnittstelle zu prüfen, führen Sie den Befehl `ibmcloud plugin list` aus.

Hilfeinformationen zur Befehlsausführung finden Sie unter [Befehlszeilenhilfe für die Befehlsausführung abrufen](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#command_cli_help).


## Protokollierungsendpunkte
{: #endpoints}

In der folgenden Tabelle sind die Protokollierungs-URLs nach Region aufgeführt:

<table>
    <caption>Endpunkte nach Region</caption>
    <tr>
      <th>Region</th>
      <th>URL</th>
    </tr>
	<tr>
      <td>Frankfurt</td>
	  <td>[https://logging.eu-fra.bluemix.net](https://logging.eu-fra.bluemix.net)</td>
    </tr>
	<tr>
      <td>Sydney</td>
	  <td>[https://logging.au-syd.bluemix.net](https://logging.au-syd.bluemix.net)</td>
    </tr>
	<tr>
      <td>Vereinigtes Königreich</td>
	  <td>[https://logging.eu-gb.bluemix.net](https://logging.eu-gb.bluemix.net)</td>
    </tr>
    <tr>
      <td>USA (Süden)</td>
      <td>[https://logging.ng.bluemix.net](https://logging.ng.bluemix.net)</td>
    </tr>
</table>

## Benutzerrollen für die Verwaltung von Protokollen
{: #roles1}

In {{site.data.keyword.Bluemix_notm}} können Sie Benutzern eine oder mehrere Rollen zuweisen. Diese Rollen definieren, welche Tasks für diesen Benutzer für die Arbeit mit dem {{site.data.keyword.loganalysisshort}}-Service aktiviert sind. 

In der folgenden Tabelle sind die Rollen aufgeführt, die einem Benutzer für die Verwaltung von Protokollen zugewiesen sein müssen:

<table>
  <caption>Für einen **Kontoeigner** erforderliche Berechtigungen für die Verwaltung von Protokollen</caption>
  <tr>
	<th>IAM-Rolle</th>
	<th>Aktionen</th>
  </tr>
  <tr>
    <td>*Administrator*</td>
    <td>Status der Protokolle überprüfen </br>Protokolle herunterladen </br>Protokolle löschen </br>Protokollaufbewahrungsrichtlinie ändern </br>Sitzungen verwalten </td>
</table>

<table>
  <caption>Für einen **Prüfer** erforderliche Berechtigungen für die Verwaltung von Protokollen</caption>
  <tr>
	<th>IAM-Rolle</th>
	<th>Aktionen</th>
  </tr>
  <tr>
    <td>*Anzeigeberechtigter*</td>
    <td>Informationen zu Protokollen abrufen, die in 'Log Collection' gehostet sind </br>Informationen zur konfigurierten Protokollaufbewahrungsrichtlinie abrufen </td>
</table>

<table>
  <caption>Für einen **Administrator** erforderliche Berechtigungen für die Verwaltung von Protokollen</caption>
  <tr>
	<th>IAM-Rolle</th>
	<th>Aktionen</th>
  </tr>
  <tr>
    <td>*Administrator*</td>
    <td>Status der Protokolle überprüfen </br>Protokolle herunterladen </br>Protokolle löschen </br>Protokollaufbewahrungsrichtlinie ändern </br>Sitzungen verwalten </td>
</table>

<table>
  <caption>Für einen **Entwickler** erforderliche Berechtigungen für die Verwaltung von Protokollen</caption>
  <tr>
	<th>IAM-Rolle</th>
	<th>Aktionen</th>
  </tr>
  <tr>
    <td>*Editor*</td>
    <td>Status der Protokolle überprüfen </br>Protokolle herunterladen </br>Protokolle löschen </br>Protokollaufbewahrungsrichtlinie ändern </br>Sitzungen verwalten</td>
</table>

