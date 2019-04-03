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


# Envoi de journaux depuis un emplacement hors de {{site.data.keyword.Bluemix_notm}}
{: #log_ingestion}

Vous pouvez envoyer des journaux depuis un emplacement hors d'{{site.data.keyword.IBM_notm}} Cloud au service {{site.data.keyword.loganalysisshort}} à l'aide de l'outil Logstash Forwarder à service partagé. 
{:shortdesc}

Cette fonction est disponible uniquement pour les plans de service autorisant l'ingestion des journaux. Pour plus d'informations, voir [Plans de service](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).

Pour envoyer des journaux depuis un emplacement hors d'{{site.data.keyword.IBM_notm}} au service {{site.data.keyword.loganalysisshort}}, vous avez besoin des ressources de cloud suivantes :

* Un {{site.data.keyword.IBM_notm}}ID pour vous connecter à {{site.data.keyword.Bluemix_notm}}. Cet ID utilisateur doit disposer des droits permettant d'utiliser le service {{site.data.keyword.loganalysisshort}} dans un espace dans {{site.data.keyword.Bluemix_notm}}. L'espace est le domaine dans {{site.data.keyword.Bluemix_notm}} dans lequel vous prévoyez d'envoyer et d'analyser les journaux.
* Un jeton de journalisation qui est généré via l'interface de ligne de commande {{site.data.keyword.loganalysisshort}} et utilisé pour authentifier votre environnement local auprès du service {{site.data.keyword.loganalysisshort}}.  

Dans votre environnement local, vous devez configurer mt-logstash-forwarder et spécifier les fichiers journaux à envoyer au service {{site.data.keyword.loganalysisshort}}.

Pour plus d'informations sur la configuration de votre environnement local pour l'envoi de journaux au service {{site.data.keyword.loganalysisshort}}, voir [Envoi de données locales dans un espace dans {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/how-to/send-data/send_data_mt.html#send_data_mt).



## URL d'ingestion
{: #log_ingestion_urls}

Le tableau suivant répertorie les URL que vous devez utiliser pour envoyer des journaux dans {{site.data.keyword.Bluemix_notm}} :

<table>
  <caption>URL d'ingestion</caption>
    <tr>
      <th>Région</th>
      <th>URL</th>
    </tr>
  <tr>
    <td>Allemagne</td>
	  <td>ingest-eu-fra.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>Sydney</td>
	  <td>ingest-au-syd.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>Royaume-Uni</td>
	  <td>ingest.logging.eu-gb.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>Sud des États-Unis</td>
	  <td>ingest.logging.ng.bluemix.net:9091</td>
  </tr>
</table>


