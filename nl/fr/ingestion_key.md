---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion key

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

# Utilisation des clés d'ingestion
{: #ingestion_key}

La clé d'ingestion est une clé de sécurité que vous devez utiliser pour configurer des agents LogDNA et pouvoir envoyer des journaux à votre instance {{site.data.keyword.la_full_notm}} dans {{site.data.keyword.cloud_notm}}. Vous obtenez automatiquement la clé d'ingestion lorsque vous mettez une instance à disposition. Sinon, vous pouvez obtenir la clé d'ingestion en créant un ID de service pour l'instance. 
{:shortdesc}

**Remarque :** 

* Pour utiliser des clés d'ingestion via l'interface utilisateur Web {{site.data.keyword.la_full_notm}}, vous devez disposer d'une règle IAM avec le rôle de plateforme **Afficheur** et le rôle de service **Responsable** pour le service {{site.data.keyword.la_full_notm}}. 
* Pour utiliser des clés d'ingestion via l'interface utilisateur {{site.data.keyword.cloud_notm}}, vous devez disposer d'une règle IAM avec le rôle de plateforme **Editeur** et le rôle de service **Responsable** pour le service {{site.data.keyword.la_full_notm}}. 


## Obtention de la clé d'ingestion via l'interface utilisateur {{site.data.keyword.cloud_notm}}
{: #ibm_cloud_ui}

Pour obtenir la clé d'ingestion pour une instance {{site.data.keyword.la_full_notm}} en utilisant l'interface utilisateur {{site.data.keyword.cloud_notm}}, procédez comme suit :

1. Connectez-vous à votre compte {{site.data.keyword.cloud_notm}}.

    Cliquez sur le [tableau de bord {{site.data.keyword.cloud_notm}}![Icône de lien externe](../../icons/launch-glyph.svg "Icône de lien externe")](https://cloud.ibm.com/login){:new_window} pour ouvrir le tableau de bord {{site.data.keyword.cloud_notm}}.

	Une fois connecté avec votre ID utilisateur et votre mot de passe, l'interface utilisateur {{site.data.keyword.cloud_notm}} s'ouvre.

2. Dans le menu de navigation, sélectionnez **Observabilité**. 

3. Sélectionnez **Journalisation**. Le tableau de bord {{site.data.keyword.la_full_notm}} s'ouvre. Il affiche la liste des instances de journalisation disponibles sur {{site.data.keyword.cloud_notm}}.

3. Identifiez l'instance pour laquelle vous voulez obtenir la clé d'ingestion, puis cliquez sur **Afficher la clé d'ingestion**.

4. Une fenêtre dans laquelle vous pouvez cliquer sur **Afficher** pour afficher la clé d'ingestion s'affiche.


## Obtention de la clé d'ingestion via l'interface utilisateur Web {{site.data.keyword.la_full_notm}}
{: #logdna_ui}

Pour obtenir la clé d'ingestion pour une instance {{site.data.keyword.la_full_notm}} en utilisant l'interface utilisateur Web {{site.data.keyword.la_full_notm}}, procédez comme suit :

1. Ouvrez l'interface utilisateur Web {{site.data.keyword.la_full_notm}}. Pour plus d'informations, voir [Démarrage de l'interface utilisateur Web {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Cliquez sur l'icône **Configuration**. Puis sélectionnez **Organisation**. 

3. Sélectionnez **Clés d'API**.

La clé d'ingestion créée s'affiche. 

**Remarque :** une seule clé d'ingestion est active à la fois. 


## Obtention de la clé d'ingestion via l'interface de ligne de commande {{site.data.keyword.cloud_notm}}
{: #ibm_cloud_cli}

Pour obtenir la clé d'ingestion pour une instance {{site.data.keyword.la_full_notm}} en utilisant la ligne de commande, procédez comme suit :

1. [Prérequis] Installez l'interface de ligne de commande {{site.data.keyword.cloud_notm}}.

   Pour plus d'informations, voir [Installation de l'interface de ligne de commande {{site.data.keyword.cloud_notm}}.](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about)

   Si l'interface de ligne de commande est installée, passez à l'étape suivante.

2. Connectez-vous à la région {{site.data.keyword.cloud_notm}} où l'instance s'exécute. Exécutez la commande suivante : [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Définissez le groupe de ressources dans lequel l'instance {{site.data.keyword.la_full_notm}} s'exécute. Exécutez la commande suivante : [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target) avec l'option `-g`.

    Le groupe de ressources `default` est sélectionné par défaut.

4. Obtenez le nom de la clé d'API associée à l'instance {{site.data.keyword.la_full_notm}}. Exécutez la commande [`ibmcloud resource service-keys`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_keys):

    ```
    ibmcloud resource service-keys
    ```
    {: codeblock}

    Identifiez la clé de service associée à votre instance.

5. Obtenez la clé d'ingestion. Exécutez la commande [`ibmcloud resource service-key`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_key) :

    ```
    ibmcloud resource service-key APIKEY_NAME
    ```
    {: codeblock}

    Où APIKEY_NAME est le nom de la clé d'API.
 
    La sortie de la commande inclut la zone **ingestion_key** qui contient la clé d'ingestion pour l'instance.


## Réinitialisation de la clé d'ingestion 
{: #reset}

Si la clé d'ingestion est compromise ou si une règle impose de renouveler la clé après un certain nombre de jours, vous pouvez générer une nouvelle clé et supprimer l'ancienne.

Pour renouveler la clé d'ingestion pour une instance {{site.data.keyword.la_full_notm}} à l'aide de l'interface utilisateur Web {{site.data.keyword.la_full_notm}}, procédez comme suit :

1. Ouvrez l'interface utilisateur Web {{site.data.keyword.la_full_notm}}. Pour plus d'informations, voir [Démarrage de l'interface utilisateur Web {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Cliquez sur l'icône **Configuration**. Puis sélectionnez **Organisation**. 

3. Sélectionnez **Clés d'API**.

    La clé d'ingestion créée s'affiche. 

4. Sélectionnez **Generate Ingestion Key**.

    Une nouvelle clé est ajoutée à la liste.

5. Supprimez l'ancienne clé d'ingestion. Cliquez sur **Supprimer**.

**Remarque :** après voir réinitialisé la clé d'ingestion, vous devez mettre à jour la clé d'ingestion pour toutes les sources de journal configurées pour envoyer des journaux à cette instance {{site.data.keyword.la_full_notm}}.



