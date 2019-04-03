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


# クラスターのスペース ID の取得
{: #containers_spaceid}

Cloud Foundry 組織およびスペースのコンテキスト内で {{site.data.keyword.Bluemix_notm}} アカウントにクラスターを作成できます。 
{:shortdesc}

クラスターに関連付けられているスペース ID を見つけるには、以下のコマンドを実行します。

```
ibmcloud cs cluster-get ClusterName --json
```
{: codeblock}

ここで、**ClusterName** はクラスターの名前です。


このコマンド実行の出力は、以下の例のようになります。

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

スペース ID は、**logSpace** フィールドに示される値です。
スペース名は、**logSpaceName** フィールドに示される値です。
組織 ID は、**logOrg** フィールドに示される値です。
組織名は、**logOrgName** フィールドに示される値です。

これらのフィールドが空の場合、そのクラスターに関連付けられている CF 組織およびスペースはありません。



