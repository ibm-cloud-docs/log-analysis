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


# 擷取叢集的金鑰擁有者
{: #containers_key_owner}

使用 *ibmcloud cs api-key-info* 指令，以取得叢集的 {{site.data.keyword.loganalysisshort}} 金鑰擁有者。
{:shortdesc}

執行下列指令：

```
 ibmcloud cs api-key-info ClusterName
```
{: codeblock}

其中 **ClusterName** 是叢集的名稱。


例如，這個指令的執行輸出如下：

```
ibmcloud cs api-key-info MyDemoCluster
Getting information about the API key owner for cluster MyDemoCluster...
OK
Name           Email   
Joe Blogg      blogg@ibm.com   
```
{: screen}

空間 ID 是針對 **logSpace** 欄位所指出的值。
空間名稱是針對 **logSpaceName** 欄位所指出的值。
組織 ID 是針對 **logOrg** 欄位所指出的值。
組織名稱是針對 **logOrgName** 欄位所指出的值。

如果這些欄位是空的，則沒有與該叢集相關聯的 CF 組織及空間。



