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


# Extraction de l'ID d'espace pour un cluster
{: #containers_spaceid}

Vous pouvez créer un cluster sur un compte {{site.data.keyword.Bluemix_notm}} dans le contexte d'une organisation et d'un espace Cloud Foundry. 
{:shortdesc}

Pour identifier l'ID d'espace qui est associé à un cluster, exécutez la commande suivante :

```
ibmcloud cs cluster-get ClusterName --json
```
{: codeblock}

où **ClusterName** est le nom du cluster.


Par exemple, la sortie de l'exécution de la commande est la suivante :

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

L'ID d'espace est la valeur indiquée dans la zone **logSpace**.
Le nom d'espace est la valeur indiquée dans la zone **logSpaceName**.
L'ID d'organisation est la valeur indiquée dans la zone **logOrg**.
Le nom d'organisation est la valeur indiquée dans la zone **logOrgName**.

Si ces zones sont vides, cela signifie qu'aucun espace ni organisation CF n'est associé à ce cluster.



