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


# Richiamo dell'ID spazio per un cluster
{: #containers_spaceid}

Puoi creare un cluster in un account {{site.data.keyword.Bluemix_notm}} nel contesto di un'organizzazione e uno spazio Cloud Foundry. 
{:shortdesc}

Per trovare l'ID spazio associato a un cluster, esegui questo comando:

```
ibmcloud cs cluster-get ClusterName --json
```
{: codeblock}

dove **ClusterName** è il nome del cluster.


Ad esempio, l'output di esecuzione del comando è il seguente:

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

L'ID spazio è il valore indicato per il campo **logSpace**.
Il nome spazio è il valore indicato per il campo **logSpaceName**.
L'ID organizzazione è il valore indicato per il campo **logOrg**.
Il nome organizzazione è il valore indicato per il campo **logOrgName**.

Se questi campi sono vuoti, non ci sono spazi e organizzazioni CF associati a tale cluster.



