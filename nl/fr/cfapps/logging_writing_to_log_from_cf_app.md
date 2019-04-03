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

# Journalisation des applications de contexte d'exécution via des applications CF
{: #logging_writing_to_log_from_cf_app}

Dans {{site.data.keyword.Bluemix}}, pour conserver les données de journal pour une application Cloud Foundry et son contexte d'exécution, vous devez écrire vos journaux dans des enregistrements de sortie standard et d'erreur standard. 
{:shortdesc}

Dans {{site.data.keyword.Bluemix_notm}}, les enregistrements de journal de la sortie standard (STDOUT) et de l'erreur standard (STDERR) sont collectés automatiquement :

* STDOUT (sortie standard) fournit des informations générales.  
* STDERR (erreur standard) fournit des informations incluant des messages d'erreur et d'autres avertissements de diagnostic. 

Le composant Loggregator prélève automatiquement des données de sortie standard et d'erreur standard. Loggregator est le composant qui réachemine les journaux depuis Cloud Foundry. 

Exemple 

Pour une **application Cloud Foundry Liberty**, le fichier console.log par défaut du serveur Liberty est prélevé automatiquement par le composant Loggregator. 

* Le fichier console.log contient l'enregistrement de sortie standard et l'enregistrement d'erreur standard réacheminés à partir du processus de machine virtuelle Java. La sortie de la console contient les événements et les erreurs principaux si vous utilisez la configuration consoleLogLevel par défaut. La sortie de la console contient également les messages écrits dans les flux system.out et system.err si vous utilisez la configuration copySystemStreams par défaut. La sortie de la console contient toujours les messages écrits directement par le processus de machine virtuelle Java, par exemple, -verbose:gc output. Vous pouvez ajuster le niveau de journalisation de Liberty via le fichier server.xml.
* La configuration consoleLogLevel définit le niveau de filtre du gestionnaire console.log. Lorsque vous affectez la valeur INFO à consoleLogLevel, vous configurez l'écriture de tous les messages INFO, AUDIT, WARNING et ERROR dans le fichier console.log. **Remarque :** les entrées de journal FINE, FINER, FINEST ne sont écrites que dans le fichier trace.log.

Pour plus d'informations sur les applications Liberty for Java™, voir [Liberty Profile: Logging and Trace ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](http://www-01.ibm.com/support/knowledgecenter/was_beta_liberty/com.ibm.websphere.wlp.nd.multiplatform.doc/ae/rwlp_logging.html){: new_window}.

Pour une **application Cloud Foundry Node.js**, vous pouvez utiliser le module de journalisation de la console intégré afin de configurer la journalisation pour l'exécution dans {{site.data.keyword.Bluemix}}. Vous pouvez placer les messages dans les fichiers de sortie standard et d'erreur standard :

* console.log('message') envoie le message dans le flux de sortie standard
* console.error('error_message') envoie l'erreur dans le flux d'erreur standard

Pour plus d'informations sur les applications Node.js, voir [How to log in node.js ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](https://docs.nodejitsu.com/articles/intermediate/how-to-log/){: new_window}.


Pour plus d'informations sur les **applications Ruby on Rails**, voir [The Logger ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](http://guides.rubyonrails.org/debugging_rails_applications.html#the-logger){: new_window}.

Le tableau suivant présente le mappage entre certains journaux d'exécution d'application et les journaux prélevés automatiquement par Loggregator :

| **Runtime** |    **STDOUT**     | **STDERR** |
|-----------------|-------------------|-------------------|
| Liberty | system.out | system.err |
| Node.js | console.log, console.info | console.error, console.warn |
| Ruby | stdout| stderr |
{: caption="Tableau 1. Mappage entre certains journaux d'exécution d'application et les journaux prélevés automatiquement par Loggregator" caption-side="top"}

