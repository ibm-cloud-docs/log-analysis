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


# Configuration d'hôtes de journaux externes
{: #thirdparty_logging}

{{site.data.keyword.Bluemix_notm}} conserve une quantité limitée d'informations de journal en mémoire. Lorsque des informations sont journalisées, les anciennes informations sont remplacées par les informations plus récentes. Pour conserver toutes les informations de journal, vous pouvez sauvegarder vos journaux d'application Cloud Foundry sur un hôte de journaux externe (par exemple, un service de gestion de journaux tiers ou un autre hôte).
{:shortdesc}

Pour acheminer vos journaux d'application CF et vos journaux système vers un hôte de journaux externe, procédez comme suit :

  1. Déterminez le noeud final de journalisation.

	 Vous pouvez envoyer des journaux à un regroupeur de journaux tiers, comme Papertrail, Splunk ou Sumologic. Vous pouvez aussi envoyer des journaux à un hôte syslog, un hôte syslog chiffré avec TLS (Transport Layer Security) ou un noeud final HTTPS POST. Les méthodes d'obtention de noeuds finaux de journalisation varient selon l'hôte de journaux.

  2. Créez une instance de service fournie par l'utilisateur.

	 Utilisez la commande `cf create-user-provided-service` (ou sa version courte `cups`) pour créer une instance de
service fournie par l'utilisateur :
	 
	 ```
	 cf create-user-provided-service <service_name> -l <logging_endpoint>
	 ```
	 {: codeblock}
	 
	 &lt;service_name&gt;

	 Nom de l'instance de service fournie par l'utilisateur.

	 &lt;logging_endpoint&gt;

	 Noeud final de journalisation auquel {{site.data.keyword.Bluemix_notm}} envoie des journaux. Reportez-vous au tableau suivant pour remplacer *noeud_final_journalisation* par la valeur appropriée :

	 <table>
	 <caption>Tableau 1. Valeurs de noeud final de journalisation</caption>
     <thead>
     <tr>
     <th>Noeud final de journalisation</th>
     <th>Commande</th>
	 <th>Remarques</th>
     </tr>
     </thead>
     <tbody>
     <tr>
     <td>hôte syslog</td>
     <td>`cf cups my-logs -l syslog://HOST:PORT`</td>
	 <td>Par exemple, pour activer la journalisation dans Papertrail, entrez `cf cups my-logs -l syslog://<papertrail-url>`. Remplacez `<papertrail-url>` par l'URL
de votre noeud final de journalisation depuis Papertrail.</td>
     </tr>
	 <tr>
     <td>hôte syslog-tls</td>
     <td>`cf cups my-logs -l syslog-tls://HOST:PORT`</td>
	 <td>Le certificat doit être considéré comme digne de confiance par une autorité de certification. N'utilisez pas de certificat autosigné.</td>
     </tr>
	 <tr>
     <td>HTTPS POST</td>
     <td>`cf cups my-logs -l https://HOST:PORT`</td>
	 <td>Ce noeud final doit se trouver sur l'Internet public et {{site.data.keyword.Bluemix_notm}} doit pouvoir y accéder.</td>
     </tr>
     </tbody>
     </table>
  3. Liez l'instance de service à votre application.

	 Utilisez la commande suivante pour lier l'instance de service à votre application :

	 ```
	 cf bind-service <appname> <service_name>
	 ```
	 {: codeblock}
	 
	 &lt;appname&gt;

	 Nom de votre application.

	 &lt;service_name&gt;

	 Nom de l'instance de service fournie par l'utilisateur.

  4. Reconstituez l'application en préproduction. Entrez `cf restage appname` pour que les modifications soient appliquées.

