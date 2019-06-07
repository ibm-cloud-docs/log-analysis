---

copyright:
  years:  2018, 2019
lastupdated: "2019-05-01"

keywords: LogDNA, IBM, Log Analysis, logging, kubernetes, tutorial, reset ingestion key

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


# Réinitialisation de la clé d'ingestion utilisée par un cluster Kubernetes pour envoyer des journaux à une instance {{site.data.keyword.la_full_notm}}
{: #kube_reset}

Si la clé d'ingestion que vous utilisez pour envoyer des journaux depuis un cluster vers une instance {{site.data.keyword.la_full_notm}} dans {{site.data.keyword.cloud_notm}} est compromise, vous devez réinitialiser la clé et mettre à jour la configuration du cluster Kubernetes afin d'utiliser la nouvelle clé d'ingestion. 
{:shortdesc}

## Avant de commencer
{: #kube_reset_prereqs}

Opérez dans la région Sud des Etats-Unis. Les deux ressources, l'instance {{site.data.keyword.la_full_notm}} et le cluster Kubernetes doivent s'exécuter dans le même compte.

L'instance {{site.data.keyword.la_full_notm}} est mise à disposition dans le groupe de ressources **Default**.

Documentez-vous sur {{site.data.keyword.la_full_notm}}. Pour plus d'informations, voir [A propos de LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).

Pour pouvoir effectuer les étapes de ce tutoriel, des règles IAM doivent avoir été affectées à votre {{site.data.keyword.IBM_notm}}ID pour chacune des ressources suivantes : 

| Ressource                             | Portée de la règle d'accès | Rôles    | Région    | Informations                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Groupe de ressources **Default**           |  Groupe de ressources            | Afficheur  | us-south  | Cette règle est requise pour autoriser l'utilisateur à visualiser des instances de service dans le groupe de ressources par défaut.    |
| Service {{site.data.keyword.la_full_notm}} |  Groupe de ressources            | Editeur </br>Responsable  | us-south  | Cette règle est requise pour autoriser l'utilisateur à réinitialiser la clé d'ingestion.   |
| Instance de cluster Kubernetes          |  Ressource                  | Editeur  | us-south  | Cette règle est requise pour supprimer et configurer la valeur confidentielle (secret) et l'agent LogDNA dans le cluster Kubernetes. |
{: caption="Tableau 1. Liste des règles IAM requises pour suivre ce tutoriel" caption-side="top"} 

Pour plus d'informations sur les rôles IAM d'{{site.data.keyword.containerlong}}, voir [User access permissions](/docs/containers?topic=containers-access_reference#access_reference).

Installez l'interface de ligne de commande {{site.data.keyword.cloud_notm}} et le plug-in d'interface de ligne de commande Kubernetes. Pour plus d'informations, voir [Installation de l'interface de ligne de commande {{site.data.keyword.cloud_notm}}.](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli)


## Etape 1: Réinitialisation de la clé d'ingestion
{: #kube_reset_step1}

Pour renouveler la clé d'ingestion pour une instance {{site.data.keyword.la_full_notm}} à l'aide de l'interface utilisateur Web {{site.data.keyword.la_full_notm}}, procédez comme suit :

1. Ouvrez l'interface utilisateur Web {{site.data.keyword.la_full_notm}}. Pour plus d'informations, voir [Démarrage de l'interface utilisateur Web {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Cliquez sur l'icône **Configuration**. Puis sélectionnez **Organisation**. 

3. Sélectionnez **Clés d'API**.

    La clé d'ingestion créée s'affiche. 

4. Sélectionnez **Generate Ingestion Key**.

    Une nouvelle clé est ajoutée à la liste.

5. Supprimez l'ancienne clé d'ingestion. Cliquez sur **Supprimer**.


## Etape 2: Suppression et configuration dans le cluster qui utilise l'ancienne clé d'ingestion
{: #kube_reset_step2}

Pour ce faire, procédez comme suit :

1. Ouvrez un terminal. Puis connectez-vous à {{site.data.keyword.cloud_notm}}. Exécutez la commande suivante et suivez les invites :

    ```
    ibmcloud login -a cloud.ibm.com
    ```
    {: codeblock}

    Sélectionnez le compte où vous avez mis l'instance {{site.data.keyword.la_full_notm}} à disposition.

2. Configurez l'environnement de cluster. Exécutez les commandes suivantes :

    Commencez par vous procurer la commande de définition de la variable d'environnement et téléchargez les fichiers de configuration Kubernetes.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    Une fois les fichiers de configuration téléchargés, une commande s'affiche ; elle vous permet de définir le chemin vers le fichier de configuration Kubernetes local en tant que variable d'environnement.

    Ensuite, copiez et collez la commande affichée sur votre terminal pour définir la variable d'environnement KUBECONFIG.

    **Remarque :** chaque fois que vous vous connectez à l'interface de ligne de commande {{site.data.keyword.containerlong}} pour travailler avec des clusters, vous devez exécuter ces commandes définir le chemin d'accès au fichier de configuration des clusters sous forme de variable de session. L'interface de ligne de commande Kubernetes utilise cette variable pour localiser un fichier de configuration local et les certificats requis pour la connexion au cluster dans {{site.data.keyword.cloud_notm}}.

3. Supprimez la valeur confidentielle (secret) de votre cluster Kubernetes. Le secret Kubernetes contient la clé d'ingestion LogDNA. Exécutez la commande suivante :

    ```
    kubectl delete secret logdna-agent-key
    ```
    {: codeblock}

4. Supprimez l'agent LogDNA sur chaque noeud worker de votre cluster Kubernetes. L'agent LogDNA est chargé de la collecte et du transfert de vos journaux. Exécutez la commande suivante :

    ```
    kubectl delete daemonset logdna-agent
    ```
    {: codeblock}

5. Vérifiez que l'agent LogDNA a bien été supprimé. Exécutez la commande suivante :

    ```
    kubectl get pods
    ```
    {: codeblock}

    Vous ne devez voir aucun pod LogDNA.


## Etape 3: Configuration de votre cluster Kubernetes avec la nouvelle clé d'ingestion
{: #kube_reset_step3}

Pour configure votre cluster Kubernetes de manière à envoyer les journaux à votre instance LogDNA, procédez comme suit à partir de la ligne de commande :

1. Ouvrez un terminal. Puis connectez-vous à {{site.data.keyword.cloud_notm}}. Exécutez la commande suivante et suivez les invites :

    ```
    ibmcloud login -a cloud.ibm.com
    ```
    {: codeblock}

    Sélectionnez le compte où vous avez mis l'instance {{site.data.keyword.la_full_notm}} à disposition.

2. Configurez l'environnement de cluster. Exécutez les commandes suivantes :

    Commencez par vous procurer la commande de définition de la variable d'environnement et téléchargez les fichiers de configuration Kubernetes.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    Une fois les fichiers de configuration téléchargés, une commande s'affiche ; elle vous permet de définir le chemin vers le fichier de configuration Kubernetes local en tant que variable d'environnement.

    Ensuite, copiez et collez la commande affichée sur votre terminal pour définir la variable d'environnement KUBECONFIG.

    **Remarque :** chaque fois que vous vous connectez à l'interface de ligne de commande {{site.data.keyword.containerlong}} pour travailler avec des clusters, vous devez exécuter ces commandes définir le chemin d'accès au fichier de configuration des clusters sous forme de variable de session. L'interface de ligne de commande Kubernetes utilise cette variable pour localiser un fichier de configuration local et les certificats requis pour la connexion au cluster dans {{site.data.keyword.cloud_notm}}.

3. Ajoutez une valeur confidentielle (secret) à votre cluster Kubernetes. Exécutez la commande suivante :

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE
    ```
    {: codeblock}

    LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE affiche la clé d'ingestion LogDNA de votre instance.

    Le secret Kubernetes contient la clé d'ingestion LogDNA. La clé d'ingestion LogDNA est utilisée pour authentifier l'agent de journalisation auprès du service {{site.data.keyword.la_full_notm}}. Elle est utilisée pour ouvrir un socket Web sécurisé sur le serveur d'ingestion sur le système de back end de journalisation.

4. Configurez l'agent LogDNA sur chaque noeud worker de votre cluster Kubernetes. Exécutez la commande suivante :

    ```
    kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
    ```
    {: codeblock}

    L'agent LogDNA est chargé de la collecte et du transfert de vos journaux.

    L'agent collecte automatiquement les journaux ayant l'extension *.log et les fichiers sans extension qui se trouvent dans /var/log. Par défaut, les journaux sont collectés à partir de tous les espaces de nom, y compris kube-system.

5. Vérifiez que l'agent LogDNA a été créé et vérifiez son statut. Exécutez la commande suivante :

    ```
    kubectl get pods
    ```
    {: codeblock}


## Etape 4: Démarrage de l'interface utilisateur Web LogDNA
{: #kube_reset_step4}

Pour ouvrir le tableau de bord IBM Log Analysis avec LogDNA via l'interface utilisateur {{site.data.keyword.cloud_notm}}, procédez comme suit :

1. Connectez-vous à votre compte {{site.data.keyword.cloud_notm}}.

    Cliquez sur le [tableau de bord {{site.data.keyword.cloud_notm}}![Icône de lien externe](../../icons/launch-glyph.svg "Icône de lien externe")](https://cloud.ibm.com/login){:new_window} pour ouvrir le tableau de bord {{site.data.keyword.cloud_notm}}.

	Une fois connecté avec votre ID utilisateur et votre mot de passe, le tableau de bord {{site.data.keyword.cloud_notm}} s'ouvre.

2. Dans le menu de navigation, sélectionnez **Observabilité**. 

3. Sélectionnez **Journalisation**. 

    La liste des instances {{site.data.keyword.la_full_notm}} disponibles sur {{site.data.keyword.cloud_notm}} s'affiche.

3. Sélectionnez une instance. Puis cliquez sur **Afficher les journaux**.

    L'interface utilisateur Web LogDNA qui affiche les journaux de votre cluster s'ouvre.


## Etape 5: Affichage de vos journaux
{: #kube_reset_step5}

Depuis l'interface utilisateur Web LogDNA, vous pouvez afficher vos journaux lorsqu'ils passent par le système. Vous affichez les journaux selon un processus de mise à la queue (tailing) des journaux. 

**Remarque :** avec le plan de service **Free**, vous ne pouvez mettre à la queue (tailing) que vos journaux les plus récents.



## Etapes suivantes
{: #kube_reset_next_steps}

  Si vous voulez [filtrer les journaux de cluster](https://docs.logdna.com/docs/filters), [effectuer des recherches dans les journaux de cluster](https://docs.logdna.com/docs/search), [définir des vues](https://docs.logdna.com/docs/views) et [configurer des alertes](https://docs.logdna.com/docs/alerts), vous devez effectuer une mise à niveau du plan {{site.data.keyword.la_full_notm}} vers un plan payant.



