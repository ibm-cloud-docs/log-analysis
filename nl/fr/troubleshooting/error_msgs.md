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


# Messages d'erreur
{: #error_msgs}

Il se peut que les messages d'erreur suivants s'affichent lorsque vous utilisez le service {{site.data.keyword.loganalysisshort}} dans {{site.data.keyword.Bluemix}} :
{:shortdesc}

## BXNLG020001W
{: #BXNLG020001W}

**Description du message**

Vous avez atteint le quota journalier alloué à l'espace Bluemix {Space GUID} pour l'instance {{site.data.keyword.loganalysisfull}} {Instance GUID}. Votre allocation journalière est actuellement de 500 Mo pour le stockage Log Search, et elle est conservée pendant une période de 3 jours au cours de laquelle elle peut faire l'objet de recherches dans Kibana. Pour mettre à niveau votre plan afin de pouvoir stocker davantage de données dans le stockage Log Search chaque jour, et aussi pour conserver tous les journaux dans le stockage Log Collection, mettez à niveau le plan de service {{site.data.keyword.loganalysisshort}} pour cet espace. Pour plus d'informations sur les plans de service et pour savoir comment effectuer la mise à niveau de votre plan, voir [Plans](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).


**Explication du message** 

Il se peut qu'un message *BXNLG020001W* s'affiche lorsque vous atteignez le quota de stockage Log Search alloué pour le plan de service Lite. Le plan Lite est le plan de service gratuit défini par défaut lorsque vous mettez à disposition le service {{site.data.keyword.loganalysisshort}} dans un espace. Votre allocation journalière est actuellement de 500 Mo pour le stockage Log Search, et elle est conservée pendant une période de 3 jours au cours de laquelle elle peut faire l'objet de recherches dans Kibana.

**Que faire**

Pour mettre à niveau votre plan afin de pouvoir stocker davantage de données dans le stockage Log Search chaque jour, et aussi pour conserver tous les journaux dans le stockage Log Collection, mettez à niveau le plan de service {{site.data.keyword.loganalysisshort}} pour cet espace. Pour plus d'informations sur les plans de service et pour savoir comment effectuer la mise à niveau de votre plan, voir [Plans](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).


## BXNLG020002W 
{: #BXNLG020002W}


**Description du message**

Vous avez atteint le quota journalier alloué à l'espace Bluemix {Space GUID} pour l'instance {{site.data.keyword.loganalysisfull}} {Instance GUID}.  Votre allocation journalière est actuellement de XXX pour le stockage Log Search, et elle est conservée pendant une période de 3 jours au cours de laquelle elle peut faire l'objet de recherches dans Kibana. Cela n'affecte pas la règle de conservation de journaux définie dans le stockage Log Collection. Pour mettre à niveau votre plan afin de pouvoir stocker davantage de données dans le stockage Log Search chaque jour, mettez à niveau le plan de service {{site.data.keyword.loganalysisshort}} pour cet espace. Pour plus d'informations sur les plans de service et pour savoir comment effectuer la mise à niveau de votre plan, voir [Plans](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).

XXX représente la taille des données pouvant faire l'objet d'une recherche pour votre plan en cours.

**Explication du message** 

Vous avez atteint le quota journalier alloué à l'espace {Space GUID} pour l'instance {{site.data.keyword.loganalysisfull}} {Instance GUID}.  Votre allocation journalière est actuellement de 500 Mo, 2 Go, 5 Go ou 10 Go pour le stockage Log Search, et elle est conservée pendant une période de 3 jours au cours de laquelle elle peut faire l'objet de recherches dans Kibana. Cela n'affecte pas la règle de conservation de journaux définie dans le stockage Log Collection.

**Que faire**

Pour mettre à niveau votre plan afin de pouvoir stocker davantage de données dans le stockage Log Search chaque jour, mettez à niveau le plan de service {{site.data.keyword.loganalysisshort}} pour cet espace. Pour plus d'informations sur les plans de service et pour savoir comment effectuer la mise à niveau de votre plan, voir [Plans](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).




