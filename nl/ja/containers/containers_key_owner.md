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


# クラスターのキー所有者の取得
{: #containers_key_owner}

クラスターの {{site.data.keyword.loganalysisshort}} キー所有者を取得するには、コマンド *ibmcloud cs api-key-info* を使用します。
{:shortdesc}

次のコマンドを実行します。

```
 ibmcloud cs api-key-info ClusterName
```
{: codeblock}

ここで、**ClusterName** はクラスターの名前です。


このコマンド実行の出力は、以下の例のようになります。

```
ibmcloud cs api-key-info MyDemoCluster
Getting information about the API key owner for cluster MyDemoCluster...
OK
Name           Email   
Joe Blogg      blogg@ibm.com   
```
{: screen}

スペース ID は、**logSpace** フィールドに示される値です。
スペース名は、**logSpaceName** フィールドに示される値です。
組織 ID は、**logOrg** フィールドに示される値です。
組織名は、**logOrgName** フィールドに示される値です。

これらのフィールドが空の場合、そのクラスターに関連付けられている CF 組織およびスペースはありません。



