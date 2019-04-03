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


# Schlüsseleigner für einen Cluster abrufen
{: #containers_key_owner}

Verwenden Sie den Befehl *ibmcloud cs api-key-info*, um den {{site.data.keyword.loganalysisshort}}-Schlüsseleigner für einen Cluster abzurufen.
{:shortdesc}

Führen Sie den folgenden Befehl aus:

```
 ibmcloud cs api-key-info ClusterName
```
{: codeblock}

Dabei ist **ClusterName** der Name des Clusters.


Die Ausgabe kann nach dem Ausführen des Befehls beispielsweise folgendermaßen aussehen:

```
ibmcloud cs api-key-info MyDemoCluster
Getting information about the API key owner for cluster MyDemoCluster...
OK
Name           Email   
Joe Blogg      blogg@ibm.com   
```
{: screen}

Die Bereichs-ID ist der Wert, der für das Feld **logSpace** angegeben ist.
Der Bereichsname ist der Wert, der für das Feld **logSpaceName** angegeben ist.
Die Organisations-ID ist der Wert, der für das Feld **logOrg** angegeben ist.
Der Organisationsname ist der Wert, der für das Feld **logOrgName** angegeben ist.

Wenn diese Felder leer sind, ist diesem Cluster keine CF-Organisation und kein CF-Bereich zugeordnet.



