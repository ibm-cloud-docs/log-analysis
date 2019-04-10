---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging instance, delete

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

# Suppression d'une instance
{: #remove}

Vous pouvez supprimer une instance du service {{site.data.keyword.la_full_notm}} depuis l'interface utilisateur {{site.data.keyword.Bluemix}} ou via la ligne de commande.
{:shortdesc}

Lorsque vous supprimez une instance d'{{site.data.keyword.cloud_notm}}, effectuez un nettoyage en procédant comme suit :

1. Notez la liste des sources qui transmettent des métriques à l'instance {{site.data.keyword.la_full_notm}} que vous voulez supprimer. Vous devez supprimer l'agent LogDNA de chaque source.
2. Supprimez les droits accordés aux utilisateurs qui leur permettant d'utiliser l'instance. 

    Si vous gérez les accès à l'aide de groupes d'accès dédiés de manière à utiliser une instance spécifique, vous devez supprimer ces groupes d'accès.

    Si vous gérez les accès à plusieurs instances de journalisation à l'aide de groupes d'accès, vous devez supprimer les règles qui accordent des droits sur l'instance que vous voulez supprimer.
    
    Si vous avez accordé des règles individuelles aux utilisateurs, vous devez dresser la liste des utilisateurs disposant de droits leur permettant d'utiliser cette instance. Puis, pour chaque utilisateur identifié, vous devez supprimer les règles associées à l'instance que vous voulez supprimer.


Ensuite, supprimez l'instance depuis le tableau de bord {{site.data.keyword.cloud_notm}}.


## Suppression d'une instance à l'aide de l'interface utilisateur {{site.data.keyword.cloud_notm}}
{: #remove_ui}

Pour supprimer une instance {{site.data.keyword.la_full_notm}} en utilisant l'interface utilisateur {{site.data.keyword.cloud_notm}}, procédez comme suit :

1. Connectez-vous à votre compte {{site.data.keyword.cloud_notm}}.

    Cliquez sur le [tableau de bord {{site.data.keyword.cloud_notm}}![Icône de lien externe](../../icons/launch-glyph.svg "Icône de lien externe")](https://cloud.ibm.com/login){:new_window} pour ouvrir le tableau de bord {{site.data.keyword.cloud_notm}}.

	Une fois connecté avec votre ID utilisateur et votre mot de passe, l'interface utilisateur {{site.data.keyword.cloud_notm}} s'ouvre.

2. Cliquez sur l'icône Menu ![Icône Menu](../../icons/icon_hamburger.svg) &gt; **Observabilité** pour accéder au tableau de bord *Observabilité*.

3. Sélectionnez **Journalisation**. La liste des instances de journalisation s'affiche.

4. Sélectionnez l'instance que vous voulez supprimer.

5. Dans le menu *Action*, sélectionnez **Retirer**.


## Suppression d'une instance à l'aide de l'interface de ligne de commande
{: #remove_cli}

Pour supprimer une instance {{site.data.keyword.la_full_notm}} via la ligne de commande, procédez comme suit :

1. [Prérequis] Installation de l'interface de ligne de commande {{site.data.keyword.cloud_notm}}.

   Pour plus d'informations, voir [Installation de l'interface de ligne de commande {{site.data.keyword.cloud_notm}}.](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli)

   Si l'interface de ligne de commande est installée, passez à l'étape suivante.

2. Connectez-vous à la région {{site.data.keyword.cloud_notm}} où vous voulez mettre l'instance à disposition. Exécutez la commande suivante : [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Définissez le groupe de ressources dans lequel l'instance est à disposition. Exécutez la commande suivante : [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    Le groupe de ressources *default* est sélectionné par défaut.

4. Supprimez l'instance. Exécutez la commande [`ibmcloud resource service-instance-delete`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_delete) command:

    ```
    ibmcloud resource service-instance-delete NAME 
    ```
    {: codeblock}

    Où NAME est le nom de l'instance.

    Par exemple, pour supprimer une instance, exécutez la commande suivante :

    ```
    ibmcloud resource service-instance-delete logdna-instance-01
    ```
    {: codeblock}



