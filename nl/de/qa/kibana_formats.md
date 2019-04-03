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

# Kibana-Protokollformate
{: #kibana_formats}

Sie können Kibana so konfigurieren, dass auf der Seite *Discover* verschiedene Felder für jeden Protokolleintrag angezeigt werden.
{:shortdesc}



## Kibana-Protokollformat für Cloud Foundry-Anwendungen
{: #kibana_log_format_cf}

Sie können Kibana so konfigurieren, dass auf der Seite *Discover* die folgenden Felder für jeden Protokolleintrag angezeigt werden:

| Feld | Beschreibung |
|-------|-------------|
| @timestamp | `yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> Die Zeit des protokollierten Ereignisses. <br> Die Zeitmarke wird millisekundengenau definiert. |
| @version | Die Version des Ereignisses. |
| ALCH_TENANT_ID | ID des {{site.data.keyword.Bluemix_notm}}-Bereichs. |
| \_id | Die eindeutige ID für Ihr Protokolldokument. |
| \_index | Der Index für Ihren Protokolleintrag. |
| \_type | Der Typ des Protokolls, z. B. *syslog*. |
| app_name | Der Name der Anwendung. |
| application_id | Die eindeutige ID der Anwendung. |
| host | Der Name Ihrer Anwendung, von der die Protokolldaten stammen. |
| instance_id | Die Instanz-ID Ihrer Anwendungsinstanz, von der die Protokolldaten stammen. |
| loglevel | Die Wertigkeit des protokollierten Ereignisses. |
| message | Die Nachricht, die von der Komponente ausgegeben wird. <br> Die Nachricht variiert abhängig vom Kontext. |
| message_type | Der Datenstrom, in den die Protokollnachricht geschrieben wird. <br> * **OUT** bezieht sich auf den Datenstrom 'stdout'. <br> * **ERR** bezieht sich auf den Datenstrom 'stderr'. |
| org_id | Die eindeutige ID Ihrer {{site.data.keyword.Bluemix_notm}}-Organisation. |
| org_name | Der Name der {{site.data.keyword.Bluemix_notm}}-Organisation, in der das Staging Ihrer App erfolgt. |
| origin | Die Komponente, von der das Ereignis stammt. |
| source_id | Die Komponente, die die Protokolle erstellt. <br> Die folgende Liste beschreibt die Protokolle von jeder Komponente: <br> * **API**: Protokollierte Antworten auf API-Aufrufe, die eine Änderung an Ihrem App-Status anfordern. <br> * **APP**: Protokollierte Antworten von Ihrer App. <br> * **CELL**: Protokollierte Antworten von der Diego-Zelle, die den Zeitpunkt des Startens, Stoppens oder Ausfalls einer App angeben. <br> * **LGR**: Protokollierte Antworten vom Loggregator, die auf Probleme beim Protokollierungsprozess hinweisen. <br> * **RTR**: Protokollierte Antworten vom Router, wenn er HTTP-Anforderungen an Ihre App weiterleitet. <br> * **SSH**: Protokollierte Antworten von der Diego-Zelle, wenn ein Benutzer mit dem Befehl `cf ssh` auf einen App-Container zugreift. <br> * **STG**: Protokollierte Antworten von der Diego-Zelle oder vom Droplet Execution Agent, wenn für Ihre Anwendung ein Staging oder erneutes Staging durchgeführt wird. |
| space_name | Der Name des {{site.data.keyword.Bluemix_notm}}-Bereichs, in dem das Staging Ihrer App erfolgt. |
| timestamp | Die Zeit des protokollierten Ereignisses. Die Zeitmarke wird millisekundengenau definiert. |
{: caption="Tabelle 1. Felder für CF-Apps" caption-side="top"}



## Kibana-Protokollformat für Docker-Container, die in einem Kubernetes-Cluster bereitgestellt sind
{: #kibana_log_format_containers_kubernetes}

Sie können Kibana so konfigurieren, dass auf der Seite *Discover* die folgenden Felder für jeden Protokolleintrag angezeigt werden. Diese Felder werden von {{site.data.keyword.IBM}} festgelegt und beinhalten Ihre Nachrichtendaten. 

| Feld | Beschreibung | Weitere Informationen |
|-------|-------------|---------------------------|
| @timestamp | `yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> Die Zeit des protokollierten Ereignisses. <br> Die Zeitmarke wird millisekundengenau definiert. | |
| @version | Die Version des Ereignisses. | |
| ALCH_TENANT_ID | Die ID des {{site.data.keyword.Bluemix_notm}}-Bereichs. | |
| \_id | Die eindeutige ID für Ihr Protokolldokument. | |
| \_index | Der Index für Ihren Protokolleintrag. | |
| \_score |  |  |
| \_type | Der Typ des Protokolls, z. B. *logs*. | |
| crn_str | Informationen über die Quelle des Protokolls. | Standardmäßig wird dieses Feld von {{site.data.keyword.IBM_notm}} festgelegt. <br> **Anmerkung:** Wenn Sie die Protokollnachricht in einem gültigen JSON-Format senden und eines der Felder hat den Namen `crn`, wird der Wert des Felds mit dem Wert in der Nachricht überschrieben.  |  
| docker.container_id_str | GUID des Containers, der in einem Pod ausgeführt wird. | |
| ibm-containers.account_str | GUID des {{site.data.keyword.Bluemix_notm}}-Kontos.  |  |
| ibm-containers.cluster_id_str | GUID des Kubernetes-Clusters.  |  |
| ibm-containers.cluster_type_str |  | Der Wert ist für die interne Verwendung durch {{site.data.keyword.IBM_notm}} reserviert. |
| ibm-containers.region_str | Die Region in {{site.data.keyword.Bluemix_notm}}.  |  |
| kubernetes.container_name_str | Der Name des Containers, in dem eine App bereitgestellt ist.  |  |
| kubernetes.host | Öffentliche IP-Adresse des Workers, bei dem der Container ausgeführt wird. |  |
| kubernetes.labels.*Beispielbezeichnung*\_str | Schlüssel-Wert-Paar, das Sie einem Kubernetes-Objekt (z. B. einem Pod) zuordnen. | Jede Bezeichnung, die Sie einem Kubernetes-Objekt zuordnen, wird als Feld in dem in Kibana angezeigten Protokolleintrag aufgelistet. <br> Sie können 0 oder mehrere Bezeichnungen ("labels") haben. |
| kubernetes.namespace_name_str | Kubernetes-Namensbereich, in dem der Container bereitgestellt ist. |  |
| kubernetes.pod_id_str | GUID des Pod, in dem der Container bereitgestellt ist. |  |
| kubernetes.pod_name_str | Name des Pod. |  |
| message | Vollständige Nachricht. | Wenn Sie eine gültige JSON-formatierte Nachricht senden, wird jedes Feld einzeln analysiert und in Kibana angezeigt.  |
| stream_str |  | Der Wert ist für die interne Verwendung durch {{site.data.keyword.IBM_notm}} reserviert. |
|tag_str |  | Der Wert ist für die interne Verwendung durch {{site.data.keyword.IBM_notm}} reserviert. |
{: caption="Tabelle 3. Felder für Docker-Container" caption-side="top"}


## Kibana-Protokollformat für {{site.data.keyword.messagehub}}
{: #kibana_log_format_messagehub}

Sie können Kibana so konfigurieren, dass auf der Seite *Discover* die folgenden Felder für jeden Protokolleintrag angezeigt werden:

| Feld | Beschreibung |
|-------|-------------|
| @timestamp | `yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> Die Zeit des protokollierten Ereignisses. <br> Die Zeitmarke wird millisekundengenau definiert. |
| @version | Die Version des Ereignisses. |
| ALCH_TENANT_ID | Die ID des {{site.data.keyword.Bluemix_notm}}-Bereichs. |
| \_id | Die eindeutige ID für Ihr Protokolldokument. |
| \_index | Der Index für Ihren Protokolleintrag. |
| \_type | Der Typ des Protokolls, z. B. *syslog*. |
| loglevel | Die Wertigkeit des protokollierten Ereignisses, z. B. **Info**. |
| module | Dieses Feld wird auf **MessageHub** eingestellt. |
{: caption="Tabelle 4. Felder für {{site.data.keyword.messagehub}}-Ereignisse" caption-side="top"}

Beispiel für einen Protokolleintrag:

```
March 8th 2017, 17:15:16.454	

message:
    Creating topic ABC
@version:
    1
@timestamp:
    March 8th 2017, 17:15:16.454
loglevel:
    Info
module:
    MessageHub
ALCH_TENANT_ID:
    3d8d2eae-f3f0-44f6-9717-126113a00b51
&#95;id:
    AVqu6vJl1zcfr8KYMI95
&#95;type:
    logs
&#95;index:
    logstash-2017.03.08
```
{: screen}


