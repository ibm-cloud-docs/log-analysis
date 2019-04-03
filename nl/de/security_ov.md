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

# Sicherheit
{: #security_ov}

Um die Aktionen in {{site.data.keyword.loganalysisshort}} zu steuern, die ein Benutzer durchführen darf, können Sie einem Benutzer eine oder mehrere Rollen zuweisen. 
{:shortdesc}

Um die API des {{site.data.keyword.loganalysisshort}}-Service verwenden zu können, benötigen Sie ein UAA- oder ein IAM-Token. Zum Senden von Protokollen an den {{site.data.keyword.loganalysisshort}}-Service benötigen Sie ein Protokollierungstoken.


## Authentifizierungsmodelle
{: #auth1}

Um den {{site.data.keyword.loganalysisshort}}-Service über die Befehlszeilenschnittstelle oder die API verwenden zu können, ist ein Authentifizierungstoken erforderlich.

Der {{site.data.keyword.loganalysisshort}}-Service unterstützt die folgenden Authentifizierungsmodelle:

* [UAA-Authentifizierung](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa)

    UAA-Token können nur über die Befehlszeilenschnittstelle verwaltet werden.
	
* [IAM-Authentifizierung](/docs/services/CloudLogAnalysis/security/auth_iam.html#auth_iam1)

    Das IAM-Authentifizierungsmodell bietet Managementfunktionalität für die Benutzerschnittstelle, Befehlszeilenschnittstelle oder API. 

**Hinweis:** Ein UAA-Token und ein IAM-Token laufen nach einem bestimmten Zeitraum ab. 

## Rollen
{: #roles3}

In {{site.data.keyword.Bluemix_notm}} gibt es zwei Typen von Rollen, die die Aktionen steuern, die Benutzer bei der Arbeit mit dem {{site.data.keyword.loganalysisshort}}-Service ausführen können:

* Cloud Foundry-Rollen (CF-Rollen): Sie steuern, welche {{site.data.keyword.loganalysisshort}}-Aktionen ein Benutzer ausführen kann, indem ihm eine oder mehrere CF-Rollen zuweisen. Mit diesen Rollen steuern Sie die Berechtigungen des Benutzers zum Anzeigen und Verwalten von Protokollen in einem Bereich oder einer Organisation.
* IAM-Rollen: Sie steuern, welche {{site.data.keyword.loganalysisshort}}-Aktionen ein Benutzer ausführen kann, indem ihm eine oder mehrere IAM-Rollen zuweisen. Mit diesen Rollen steuern Sie die Berechtigungen des Benutzers zum Anzeigen und Verwalten von Kontoprotokollen. 


In der folgenden Tabelle sind die Typen von Rollen und die entsprechende Domäne in {{site.data.keyword.Bluemix_notm}} aufgeführt, die mit diesen Rollen gesteuert werden kann:

<table>
  <caption>Tabelle 1. Typen von Rollen zum Steuern von Aktionen nach Domäne</caption>
  <tr>
    <th></th>
	<th align="right">Konto</th>
    <th align="right">Organisation</th>
    <th align="right">Bereich</th>	
  </tr>
  <tr>
    <td align="left">CF-Rollen</td>
	<td align="center">Nein</td>
	<td align="center">Ja</td>
	<td align="center">Ja</td>
  </tr>
  <tr>
    <td align="left">IAM-Rollen</td>
	<td align="center">Ja</td>
	<td align="center">Nein</td>
	<td align="center">Nein</td>
  </tr>
</table>


## CF-Rollen
{: #bmx_roles}

In der folgenden Tabelle sind die Berechtigungen der einzelnen CF-Rollen für die Verwendung des {{site.data.keyword.loganalysisshort}}-Service aufgeführt:

<table>
  <caption>Tabelle 2. Cloud Foundry-Rollen und Berechtigungen für die Verwendung des {{site.data.keyword.loganalysisshort}}-Service.</caption>
  <tr>
    <th>Rolle</th>
	<th>Domäne</th>
	<th>Zugriffsberechtigungen</th>
  </tr>
  <tr>
    <td>Manager</td>
	<td>Organisation <br>Bereich</td>
	<td>Alle REST-konformen APIs</td>
  </tr>
  <tr>
    <td>Entwickler</td>
	<td>Bereich</td>
	<td>Alle REST-konformen APIs</td>
  </tr>
  <tr>
    <td>Prüfer</td>
	<td>Organisation <br>Bereich</td>
	<td>Nur REST-konforme APIs, mit denen schreibgeschützte Operationen, wie Abfrageprotokolle, durchgeführt werden.</td>
  </tr>
</table>


## IAM-Rollen
{: #iam_roles}

In der folgenden Tabelle sind die Berechtigungen der einzelnen IAM-Rollen für die Verwendung des {{site.data.keyword.loganalysisshort}}-Service aufgeführt:

<table>
  <caption>Tabelle 3. IAM-Rollen und Berechtigungen für die Verwendung des {{site.data.keyword.loganalysisshort}}-Service.</caption>
  <tr>
    <th>Rolle</th>
	<th>Berechtigungen</th>
  </tr>
  <tr>
    <td>Administrator</td>
	  <td>Informationen zu den Protokollen in einem Bereich oder auf Kontoebene anzeigen. <br>Protokolle in eine lokale Datei herunterladen oder Protokolle an ein anderes Programm (zum Beispiel Elastic Stack) umleiten. <br>Aufbewahrungszeitraum für Protokolle anzeigen, die in einem Bereich oder einem Konto verfügbar sind. <br>Aufbewahrungszeitraum für Protokolle aktualisieren, die in einem Bereich oder einem Konto verfügbar sind. <br>Aktive Sitzungen und ihre IDs auflisten. <br>Sitzungen erstellen, mit denen Protokolle heruntergeladen werden können. <br>Sitzungen löschen, die durch die Sitzungs-ID angegeben sind. <br>Status einer einzelnen Sitzung anzeigen. <br>Protokolle löschen. </td>
  </tr>
  <tr>
    <td>Bearbeiter</td>
	  <td>Informationen zu den Protokollen in einem Bereich oder auf Kontoebene anzeigen. <br>Protokolle in eine lokale Datei herunterladen oder Protokolle an ein anderes Programm (zum Beispiel Elastic Stack) umleiten. <br>Aufbewahrungszeitraum für Protokolle anzeigen, die in einem Bereich oder einem Konto verfügbar sind. <br>Aufbewahrungszeitraum für Protokolle aktualisieren, die in einem Bereich oder einem Konto verfügbar sind. <br>Aktive Sitzungen und ihre IDs auflisten. <br>Sitzungen erstellen, mit denen Protokolle heruntergeladen werden können. <br>Sitzungen löschen, die durch die Sitzungs-ID angegeben sind. <br>Status einer einzelnen Sitzung anzeigen. <br>Protokolle löschen.  </td>
  </tr>
  <tr>
    <td>Operator</td>
	  <td>Informationen zu den Protokollen in einem Bereich oder auf Kontoebene anzeigen. <br>Aufbewahrungszeitraum für Protokolle anzeigen, die in einem Bereich oder einem Konto verfügbar sind. <br>Aktive Sitzungen und ihre IDs auflisten. <br>Status einer einzelnen Sitzung anzeigen. <br>Protokolle in eine lokale Datei herunterladen oder Protokolle an ein anderes Programm (zum Beispiel Elastic Stack) umleiten.  <br>Sitzungen erstellen, mit denen Protokolle heruntergeladen werden können. <br>Sitzungen löschen, die durch die Sitzungs-ID angegeben sind. </td>
  </tr>
  <tr>
    <td>Anzeigeberechtigter</td>
	  <td>Informationen zu den Protokollen in einem Bereich oder auf Kontoebene anzeigen. <br>Aufbewahrungszeitraum für Protokolle anzeigen, die in einem Bereich oder einem Konto verfügbar sind. <br>Aktive Sitzungen und ihre IDs auflisten. <br>Status einer einzelnen Sitzung anzeigen. </td>
  </tr>
</table>

In der folgenden Tabelle ist die Beziehung zwischen der API, einer Serviceaktion und einer IAM-Rolle aufgeführt, die vom {{site.data.keyword.loganalysisshort}}-Service verwendet wird.

<table>
  <caption>Tabelle 4. Beziehung zwischen der API, einer Serviceaktion und einer IAM-Rolle. </caption>
  <tr>
    <th>API</th>
	<th>Aktion</th>
	<th>IAM-Rolle</th>
	<th>Beschreibung</th>
  </tr>
  <tr>
    <td>DELETE /v1/logging/logs</td>
    <td>ibmcloud-log-analysis.domain.log_delete</td>
	<td>Administrator, Bearbeiter</td>
	<td>Protokolle löschen.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs</td>
    <td>ibmcloud-log-analysis.domain.log_read</td>
	<td>Administrator, Bearbeiter, Anzeigeberechtigter</td>
	<td>Informationen zu den Protokollen in einem {{site.data.keyword.Bluemix_notm}}-Bereich oder auf Kontoebene anzeigen.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs/download</td>
    <td>ibmcloud-log-analysis.domain.log_download</td>
	<td>Administrator, Bearbeiter</td>
	<td>Protokolle in eine lokale Datei herunterladen oder Protokolle an ein anderes Programm (zum Beispiel Elastic Stack) umleiten.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs/retention</td>
    <td>ibmcloud-log-analysis.domain.policy_read</td>
    <td>Administrator, Bearbeiter, Anzeigeberechtigter</td>
    <td>Aufbewahrungszeitraum für Protokolle anzeigen, die in einem {{site.data.keyword.Bluemix_notm}}-Bereich oder einem Konto verfügbar sind.</td>
  </tr>
  <tr>
    <td>PUT /v1/logging/logs/retention</td>
    <td>ibmcloud-log-analysis.domain.policy_write</td>
    <td>Administrator, Bearbeiter</td>
    <td>Aufbewahrungszeitraum für Protokolle aktualisieren, die in einem {{site.data.keyword.Bluemix_notm}}-Bereich oder einem Konto verfügbar sind.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/sessions</td>
    <td>ibmcloud-log-analysis.domain.session_read</td>
    <td>Administrator, Bearbeiter, Anzeigeberechtigter</td>
    <td>Aktive Sitzungen und ihre IDs auflisten.</td>
  </tr>
  <tr>
    <td>POST /v1/logging/sessions</td>
    <td>ibmcloud-log-analysis.domain.session_write</td>
    <td>Administrator, Bearbeiter</td>
    <td>Sitzungen erstellen, mit denen Protokolle heruntergeladen werden können.</td>
  </tr>
  <tr>
    <td>DELETE /v1/logging/sessions/{id}</td>
    <td>ibmcloud-log-analysis.domain.session_delete</td>
    <td>Administrator, Bearbeiter</td>
    <td>Sitzungen löschen, die durch die Sitzungs-ID angegeben sind.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/sessions/{id}</td>
    <td>ibmcloud-log-analysis.domain.session_read</td>
    <td>Administrator, Bearbeiter, Anzeigeberechtigter</td>
    <td>Status einer einzelnen Sitzung anzeigen.</td>
  </tr>
</table>

## Authentifizierungstoken zum Verwalten von Protokollen über die API abrufen
{: #get_token}

Zum Verwalten von Protokollen über die {{site.data.keyword.loganalysisshort}}-API müssen Sie ein Authentifizierungstoken verwenden. 

**Arbeiten mit Protokollen, die in der Bereichsdomäne verfügbar sind**

* Sie können die Befehlszeilenschnittstelle von {{site.data.keyword.loganalysisshort}} verwenden, um das UAA-Token abzurufen. 
* Das Token hat eine Ablaufzeit. 

Weitere Informationen finden Sie unter [UAA-Token abrufen](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa).

**Arbeiten mit Protokollen, die in der Kontodomäne verfügbar sind**

* Sie können die Befehlszeilenschnittstelle von {{{site.data.keyword.Bluemix_notm}} verwenden, um das IAM-Token abzurufen. 
* Das Token hat eine Ablaufzeit. 

Weitere Informationen finden Sie unter [IAM-Token abrufen](/docs/services/CloudLogAnalysis/security/auth_iam.html#auth_iam1).


## Protokollierungstoken zum Senden von Protokollen an Log Analysis abrufen
{: #get_logging_token}

Zum Senden von Protokollen an den {{site.data.keyword.loganalysisshort}}-Service benötigen Sie ein Protokollierungstoken. 

Wählen Sie eine der folgenden Methoden aus, um Protokolle an eine Bereichsdomäne zu senden:

* [Protokollierungstoken zum Senden von Protokollen an einen Bereich mit dem {{site.data.keyword.Bluemix_notm}}-Befehl 'ibmcloud service' abrufen](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_cloud_cli)
* [Protokollierungstoken zum Senden von Protokollen an einen Bereich über die Log Analysis-Befehlszeilenschnittstelle abrufen](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_la_cloud_cli)
* [Protokollierungstoken zum Senden von Protokollen an einen Bereich über die Log Analysis-API abrufen](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_api)


## Benutzern Berechtigungen zum Arbeiten mit Protokollen erteilen
{: #grant_permissions1}

Damit ein Benutzer Protokolle verwalten oder Protokolle anzeigen kann, müssen ihm in {{site.data.keyword.Bluemix_notm}} Berechtigungen für die Arbeit mit {{site.data.keyword.loganalysisshort}}-Service erteilt werden.

* Informationen zu Berechtigungen für die Verwaltung von Protokollen finden Sie unter [Rollen für die Verwaltung von Protokollen](/docs/services/CloudLogAnalysis/manage_logs.html#roles1).
* Informationen zu Berechtigungen für das Anzeigen von Protokollen finden Sie unter [Rollen zum Anzeigen von Protokollen](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#roles).

Weitere Informationen zum Erteilen von Berechtigungen finden Sie in den folgenden Abschnitten:

* [Einem Benutzer über die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle eine IAM-Richtlinie zuweisen](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions).
* [Einem Benutzer über die Befehlszeile eine IAM-Richtlinie zuweisen](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_commandline).
* [Einem Benutzer über die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle Berechtigungen zum Anzeigen von Bereichsprotokollen erteilen](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space).


