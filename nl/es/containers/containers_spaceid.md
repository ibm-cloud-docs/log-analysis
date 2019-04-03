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


# Recuperación del ID de espacio de un clúster
{: #containers_spaceid}

Puede crear un clúster en una cuenta de {{site.data.keyword.Bluemix_notm}} en el contexto de una organización y de un espacio de Cloud Foundry. 
{:shortdesc}

Para encontrar el ID de espacio asociado con un clúster, ejecute el mandato siguiente:

```
ibmcloud cs cluster-get ClusterName --json
```
{: codeblock}

donde **ClusterName** es el nombre del clúster.


Por ejemplo, el resultado de ejecutar el mandato es el siguiente:

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

El ID de espacio es el valor indicado para el campo **logSpace**.
El nombre de espacio es el valor indicado para el campo **logSpaceName**.
El ID de organización es el valor indicado para el campo **logOrg**.
El nombre de la organización es el valor indicado para el campo **logOrgName**.

Si estos campos están vacíos, no habrá ninguna organización ni espacio de CF asociados con dicho clúster.



