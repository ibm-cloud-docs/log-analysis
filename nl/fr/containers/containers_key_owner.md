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


# Extraction du propriétaire de clé pour un cluster
{: #containers_key_owner}

Utilisez la commande *ibmcloud cs api-key-info* afin d'obtenir le propriétaire de clé {{site.data.keyword.loganalysisshort}} pour un cluster.
{:shortdesc}

Exécutez la commande suivante :

```
 ibmcloud cs api-key-info ClusterName
```
{: codeblock}

où **ClusterName** est le nom du cluster.


Par exemple, la sortie de l'exécution de la commande est la suivante :

```
ibmcloud cs api-key-info MyDemoCluster
Getting information about the API key owner for cluster MyDemoCluster...
OK
Name           Email   
Joe Blogg      blogg@ibm.com   
```
{: screen}

L'ID d'espace est la valeur indiquée dans la zone **logSpace**.
Le nom d'espace est la valeur indiquée dans la zone **logSpaceName**.
L'ID d'organisation est la valeur indiquée dans la zone **logOrg**.
Le nom d'organisation est la valeur indiquée dans la zone **logOrgName**.

Si ces zones sont vides, cela signifie qu'aucun espace ni organisation CF n'est associé à ce cluster.



