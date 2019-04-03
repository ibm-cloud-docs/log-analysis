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


# 擷取叢集的空間 ID
{: #containers_spaceid}

您可以在 Cloud Foundry 組織及空間環境定義內，於 {{site.data.keyword.Bluemix_notm}} 帳戶中建立叢集。
{:shortdesc}

若要尋找與叢集相關聯的空間 ID，請執行下列指令：

```
ibmcloud cs cluster-get ClusterName --json
```
{: codeblock}

其中 **ClusterName** 是叢集的名稱。


例如，這個指令的執行輸出如下：

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

空間 ID 是針對 **logSpace** 欄位所指出的值。
空間名稱是針對 **logSpaceName** 欄位所指出的值。
組織 ID 是針對 **logOrg** 欄位所指出的值。
組織名稱是針對 **logOrgName** 欄位所指出的值。

如果這些欄位是空的，則沒有與該叢集相關聯的 CF 組織及空間。



