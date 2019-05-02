---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging instance, provision

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

# Mise à disposition d'une instance
{: #provision}

Pour pouvoir surveiller et gérer des données de journal avec {{site.data.keyword.la_full_notm}}, vous devez commencer par mettre à disposition une instance du service dans {{site.data.keyword.cloud_notm}}.
{:shortdesc}

Pour mettre une instance {{site.data.keyword.la_full_notm}} à disposition dans une région de cloud public, vous devez sélectionner le plan de service associé à l'instance, la région dans laquelle vos journaux sont collectés et le plan qui détermine la durée de conservation de vos journaux. Vous avez le choix entre 7, 14 ou 30 jours de conservation.

Sinon, {{site.data.keyword.la_full_notm}} propose un plan `Lite` qui permet d'afficher vos journaux lorsqu'ils passent par le système. Vous pouvez afficher les journaux à l'aide de la fonction de mise à la queue (tailing) des journaux. Vous pouvez également concevoir des filtres afin de préparer une mise à niveau vers un plan avec une durée de conservation plus longue. Ce plan a une durée de conservation de 0 jour.


## Mise à disposition d'une instance via le tableau de bord Observabilité
{: #provision_ui}

Pour mettre à disposition une instance à partir du tableau de bord Observabilité dans {{site.data.keyword.cloud_notm}}, procédez comme suit :

1. Connectez-vous à votre compte {{site.data.keyword.cloud_notm}}.

    Le tableau de bord {{site.data.keyword.cloud_notm}} est accessible via [Tableau de bord {{site.data.keyword.cloud_notm}}![Icône de lien externe](../../icons/launch-glyph.svg "Icône de lien externe")](https://cloud.ibm.com/login){:new_window}.

	Une fois connecté avec votre ID utilisateur et votre mot de passe, l'interface utilisateur {{site.data.keyword.cloud_notm}} s'ouvre.

2. Cliquez sur l'icône Menu ![Icône Menu](../../icons/icon_hamburger.svg). Ensuite, sélectionnez **Observabilité** pour accéder au tableau de bord *Observabilité*.

3. Sélectionnez **Journalisation**, puis cliquez sur **Create instance**. 

4. Entrez un nom pour l'instance de service.

5. Sélectionnez un groupe de ressources. 

    Le groupe de ressources **Default** est sélectionné par défaut.

    **Remarque :** si vous n'arrivez pas à sélectionner un groupe de ressources, vérifiez que vous disposez du droit d'édition sur le groupe de ressources où vous voulez mettre l'instance à disposition.

6. Sélectionnez le plan de service `Lite`. 

    Le plan Lite est sélectionné par défaut.

    Pour plus d'informations sur les autres plans de service, voir [Plans de tarification](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

7. Cliquez sur **Créer**.

Une fois l'instance mise à disposition, le tableau de bord *Journalisation* s'ouvre. 

Ensuite, configurez une source de journal en ajoutant un agent LogDNA. Cet agent est chargé de la collecte et du transfert des journaux vers votre instance. 



## Mise à disposition d'une instance via le catalogue
{: #provision_catalog}

Pour mettre à disposition une instance {{site.data.keyword.la_full_notm}} via le catalogue {{site.data.keyword.cloud_notm}}, procédez comme suit :

1. Connectez-vous à votre compte {{site.data.keyword.cloud_notm}}.

    Cliquez sur le [tableau de bord {{site.data.keyword.cloud_notm}}![Icône de lien externe](../../icons/launch-glyph.svg "Icône de lien externe")](https://cloud.ibm.com/login){:new_window} pour ouvrir le tableau de bord {{site.data.keyword.cloud_notm}}.

	Une fois connecté avec votre ID utilisateur et votre mot de passe, l'interface utilisateur {{site.data.keyword.cloud_notm}} s'ouvre.

2. Cliquez sur **Catalogue**. La liste des services disponibles dans {{site.data.keyword.cloud_notm}} s'affiche.

3. Pour filtrer la liste des services affichés, sélectionnez la catégorie **Developer Tools**.

4. Cliquez sur la vignette **{{site.data.keyword.la_full_notm}}**. 

5. Entrez un nom pour l'instance de service.

6. Sélectionnez un groupe de ressources. 

    Le groupe de ressources **Default** est sélectionné par défaut.

    **Remarque :** si vous n'arrivez pas à sélectionner un groupe de ressources, vérifiez que vous disposez du droit d'édition sur le groupe de ressources où vous voulez mettre l'instance à disposition.

7. Sélectionnez le plan de service `Lite`. 

    Le plan Lite est sélectionné par défaut.

    Pour plus d'informations sur les autres plans de service, voir [Plans de tarification](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

8. Cliquez sur **Créer**.

Une fois l'instance mise à disposition, le tableau de bord *Journalisation* s'ouvre. 

Ensuite, configurez une source de journal en ajoutant un agent LogDNA. Cet agent est chargé de la collecte et du transfert des journaux vers votre instance. 



## Mise à disposition d'une instance via l'interface de ligne de commande
{: #provision_cli}

Pour mettre à disposition une instance {{site.data.keyword.la_full_notm}} via la ligne de commande, procédez comme suit :

1. [Prérequis] Installation de l'interface de ligne de commande {{site.data.keyword.cloud_notm}}.

   Pour plus d'informations, voir [Installation de l'interface de ligne de commande {{site.data.keyword.cloud_notm}}.](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli)

   Si l'interface de ligne de commande est installée, passez à l'étape suivante.

2. Connectez-vous à la région {{site.data.keyword.cloud_notm}} où vous voulez mettre l'instance à disposition. Exécutez la commande suivante : [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Définissez le groupe de ressources dans lequel vous voulez mettre l'instance à disposition. Exécutez la commande suivante : [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    Le groupe de ressources `default` est sélectionné par défaut.

4. Créez l'instance. Exécutez la commande [`ibmcloud resource service-instance-create`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_create) :

    ```
    ibmcloud resource service-instance-create NAME logdna SERVICE_PLAN_NAME LOCATION
    ```
    {: codeblock}

    Où

    NAME est le nom de l'instance

    La valeur *logdna* est le nom du service {{site.data.keyword.la_full_notm}} dans {{site.data.keyword.cloud_notm}}

    SERVICE_PLAN_NAME est le type de plan. Les valeurs admises sont *Lite*, *7-days*, *14-days* et *30-days*
    
    LOCATION est la région où l'instance LogDNA est créée. La valeur admise est *us-south*

    Par exemple, pour mettre une instance à disposition avec un plan de conservation de 7 jours, exécutez la commande suivante :

    ```
    ibmcloud resource service-instance-create logdna-instance-01 logdna 7-day us-south
    ```
    {: codeblock}

5. Créez une clé de service avec les droits **administrateur** sur l'instance. Exécutez la commande [`ibmcloud resource service-key-create`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_key_create) :

    ```
    ibmcloud resource service-key-create NAME ROLE_NAME --instance-name SERVICE_INSTANCE_NAME
    ```
    {: codeblock}

    Où

    NAME est le nom de la clé d'API. Vous pouvez attribuer à la clé d'API le même nom qu'à l'instance {{site.data.keyword.la_full_notm}} pour l'identifier plus facilement par la suite.

    ROLE_NAME est le rôle qui définit les droits accordés. Les valeurs admises sont *éditeur*, *opérateur* et *administrateur*

    SERVICE_INSTANCE_NAME est le nom de l'instance dans {{site.data.keyword.cloud_notm}}

    Par exemple, pour créer une clé d'API pour l'instance *logdna-instance-01* avec les droits *administrateur* sur l'instance de service, exécutez la commande suivante :

    ```
    ibmcloud resource service-key-create logdna-instance-01 Administrator --instance-name logdna-instance-01
    ```
    {: pre}

    La sortie de cette commande inclut différentes valeurs telles que le nom de ressource de cloud (`crn`) de l'instance et la clé d'ingestion LogDNA.


