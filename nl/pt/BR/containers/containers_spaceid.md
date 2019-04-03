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


# Recuperando o ID de espaço para um cluster
{: #containers_spaceid}

É possível criar um cluster em uma conta do {{site.data.keyword.Bluemix_notm}} no contexto de uma organização e um espaço do Cloud Foundry. 
{:shortdesc}

Para localizar o ID do espaço que está associado a um cluster, execute o comando a seguir:

```
ibmcloud cs cluster-get ClusterName -- json
```
{: codeblock}

em que **ClusterName** é o nome do cluster.


Por exemplo, a saída da execução do comando é a seguinte:

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

O ID do espaço é o valor indicado para o campo **logSpace**.
O nome do espaço é o valor indicado para o campo **logSpaceName**.
O ID da organização é o valor indicado para o campo **logOrg**.
O nome da organização é o valor indicado para o campo **logOrgName**.

Se esses campos estiverem vazios, então, não há organização do CF e espaço associado a esse cluster.



