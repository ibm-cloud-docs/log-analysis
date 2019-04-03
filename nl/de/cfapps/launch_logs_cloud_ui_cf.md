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

# Zu den Protokollen einer Cloud Foundry-App navigieren
{: #launch_logs_cloud_ui_cf}

Sie können in der {{site.data.keyword.Bluemix}}-Benutzerschnittstelle Protolokke über eine Protokollregisterkarte, die in jeder Cloud Foundry-App oder in der Benutzerschnittstelle des {{site.data.keyword.loganalysisshort}}-Services verfügbar ist, anzeigen, filtern und analysieren.
{:shortdesc}

Berücksichtigen Sie bei der Anzeige von CF-App-Protokollen die folgenden Informationen: 

<table>
  <caption>Informationen zu CF-App-Protokollen in {{site.data.keyword.Bluemix_notm}}</caption>
  <tr>
    <th>Benutzerschnittstellenoptionen</th>
    <th>Informationen</th>
  </tr>
  <tr>
    <td>Über die CF-App-Benutzerschnittstelle verfügbare Protokollregisterkarte </td>
    <td>Die Protokolle, die für eine Analyse verfügbar sind, enthalten Daten der letzten 24 Stunden.</td>
  </tr>
  <tr>
    <td>{{site.data.keyword.loganalysisshort}}-Dashboard (Kibana)</td>
    <td>Die Protokolle, die für eine Analyse verfügbar sind, enthalten Daten der letzten 3 Tage. Sie können auch einen benutzerdefinierten Zeitraum angeben.</td>
  </tr>
</table>


## Mit dem CF-App-Dashboard zu den CF-App-Protokollen navigieren 
{: #cfapp_ui}

Führen Sie die folgenden Schritte aus, um die Bereitstellungs- oder Laufzeitprotokolle einer Cloud Foundry-App anzuzeigen:

1. Klicken Sie im Dashboard 'Apps' auf den Namen Ihrer Cloud Foundry-App. 
    
2. Klicken Sie auf der Seite 'App-Details' auf **Protokolle**.
    
    Auf der Registerkarte **Protokolle** können Sie die neuesten Protokolle für Ihre App anzeigen oder die Protokolle per Tailing in Echtzeit verfolgen. Darüber hinaus können Sie Protokolle nach Komponente (Protokolltyp), nach App-Instanz-ID und nach Fehler filtern.
    
Standardmäßig enthalten die Protokolle, die für die Analyse über die {{site.data.keyword.Bluemix_notm}}-Konsole zur Verfügung stehen, Daten für die letzten 24 Stunden.


## Mit der {{site.data.keyword.loganalysisshort}}-Benutzerschnittstelle zu den CF-App-Protokollen navigieren 
{: #cfapp_la}

Führen Sie die folgenden Schritte aus, um die Bereitstellungs- oder Laufzeitprotokolle einer Cloud Foundry-App anzuzeigen:

1. Klicken Sie im Dashboard 'Apps' auf den Namen Ihrer Cloud Foundry-App. 
    
2. Klicken Sie auf der Seite 'App-Details' auf **Protokolle**.
    
3. Klicken Sie auf die Option zur Anzeige in Kibana.

Die Protokolle, die für eine Analyse verfügbar sind, enthalten standardmäßig Daten der letzten 15 Minuten.

**Tipp:** Informationen zur Analyse von Daten für einen angepassten Zeitraum, finden Sie unter [Erweiterte Protokollanalyse mit Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analyzing_logs_Kibana#analyzing_logs_Kibana). 


