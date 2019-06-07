---

copyright:
  years:  2018, 2019
lastupdated: "2019-04-02"

keywords: LogDNA, IBM, Log Analysis, logging instance, enable, service logs

subcollection: LogDNA

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

# Configuration des journaux de maintenance {{site.data.keyword.cloud_notm}} 
{: #config_svc_logs}

Vous pouvez posséder plusieurs instances {{site.data.keyword.la_full_notm}} dans une région. Toutefois, une seul instance par région peut être configurée pour recevoir des journaux des services activés dans {{site.data.keyword.cloud_notm}}.
{:shortdesc}



## Configuration de journaux de maintenance de plateforme via le tableau de bord Observabilité 
{: #config_svc_logs_ui}

Pour configurer une instance depuis le tableau de bord Observabilité dans {{site.data.keyword.cloud_notm}}, procédez comme suit : 

1. [Connectez-vous à votre compte {{site.data.keyword.cloud_notm}} ![Icône de lien externe](../../icons/launch-glyph.svg "Icône de lien externe")](https://cloud.ibm.com/login){:new_window}.

	Une fois connecté avec votre ID utilisateur et votre mot de passe, l'interface utilisateur {{site.data.keyword.cloud_notm}} s'ouvre.

2. Cliquez sur l'icône Menu ![Icône Menu](../../icons/icon_hamburger.svg). Ensuite, sélectionnez **Observabilité** pour accéder au tableau de bord *Observabilité*.

3. Sélectionnez **Journalisation** puis cliquez sur **Configurer les journaux de maintenance de plateforme**. 

4. Indiquez quelle instance LogDNA recevra des journaux des services activés sur la plateforme cloud.

5. Sélectionnez une région. 

6. Sélectionnez une instance.

7. Cliquez sur **Sauvegarder**. 

La page *Observabilité* principale s'ouvre. 

L'instance qui doit recevoir les journaux de maintenance affiche l'indicateur **Journaux de maintenance de plateforme**.

Pour plus d'informations sur les services activés pour envoyer des journaux à {{site.data.keyword.la_full_notm}}, voir [Services cloud](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services).

