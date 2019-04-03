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


# Recuperando o proprietário da chave para um cluster
{: #containers_key_owner}

Use o comando *ibmcloud cs api-key-info* para obter o proprietário da chave do {{site.data.keyword.loganalysisshort}} para um cluster.
{:shortdesc}

Execute o comando a seguir:

```
 ibmcloud cs api-key-info ClusterName
```
{: codeblock}

em que **ClusterName** é o nome do cluster.


Por exemplo, a saída da execução do comando é a seguinte:

```
ibmcloud cs api-key-info MyDemoCluster
Getting information about the API key owner for cluster MyDemoCluster...
OK
Name           Email   
Joe Blogg      blogg@ibm.com   
```
{: screen}

O ID do espaço é o valor indicado para o campo **logSpace**.
O nome do espaço é o valor indicado para o campo **logSpaceName**.
O ID da organização é o valor indicado para o campo **logOrg**.
O nome da organização é o valor indicado para o campo **logOrgName**.

Se esses campos estiverem vazios, então, não há organização do CF e espaço associado a esse cluster.



