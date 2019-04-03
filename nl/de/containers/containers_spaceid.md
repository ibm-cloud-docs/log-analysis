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


# Bereichs-ID für einen Cluster abrufen
{: #containers_spaceid}

Sie können einen Cluster in einem {{site.data.keyword.Bluemix_notm}}-Konto im Kontext einer Organisation und eines Bereichs von Cloud Foundry erstellen. 
{:shortdesc}

Führen Sie den folgenden Befehl aus, um nach der Bereichs-ID zu suchen, die einem Cluster zugeordnet ist:

```
ibmcloud cs cluster-get ClusterName --json
```
{: codeblock}

Dabei ist **ClusterName** der Name des Clusters.


Die Ausgabe kann nach dem Ausführen des Befehls beispielsweise folgendermaßen aussehen:

```
{
    "id": "c213f81296db4c68b84e212c19135a99",
    "name": "MyDemoCluster",
    "region": "us-south",
    "dataCenter": "hou02",
    "location": "us-south-hou02",
    "serverURL": "https://xxx.xx.xx.xx:xxxxx",
    "state": "normal",
    "createdDate": "2017-09-26T09:00:59+0000",
    "modifiedDate": "2017-11-29T05:30:41+0000",
    "workerCount": 5,
    "isPaid": true,
    "masterKubeVersion": "1.7.4_1504",
    "targetVersion": "1.7.4_1504",
    "ingressHostname": "",
    "ingressSecretName": "",
    "logOrg": "5eab56t3-dty7-4utc-adaa-3aa5gn7r4g41",
    "logOrgName": "MyOrg",
    "logSpace": "fa277ff8-8a73-324b-9b75-0f11d54a3ae2",
    "logSpaceName": "MySpace",
    "addons": null,
    "vlans": null
}
```
{: screen}

Die Bereichs-ID ist der Wert, der für das Feld **logSpace** angegeben ist.
Der Bereichsname ist der Wert, der für das Feld **logSpaceName** angegeben ist.
Die Organisations-ID ist der Wert, der für das Feld **logOrg** angegeben ist.
Der Organisationsname ist der Wert, der für das Feld **logOrgName** angegeben ist.

Wenn diese Felder leer sind, ist diesem Cluster keine CF-Organisation und kein CF-Bereich zugeordnet.



