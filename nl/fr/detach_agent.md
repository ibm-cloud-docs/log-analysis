---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, detach config agent

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

# Déconnexion d'un agent LogDNA d'une instance
{: #detach_agent}

Déconnectez un agent LogDNA d'une instance de journalisation afin d'arrêter la collecte des journaux.
{:shortdesc}

## Déconnexion d'un agent LogDNA d'un cluster Kubernetes
{: #detach_agent_kube}

Pour que le cluster Kubernetes cesse d'envoyer des journaux à votre instance {{site.data.keyword.la_full_notm}}, vous devez supprimer l'agent LogDNA de votre cluster. 

Pour que le cluster Kubernetes cesse d'envoyer des journaux à votre instance LogDNA, procédez comme suit à partir de la ligne de commande :

1. Ouvrez un terminal. Ensuite, [connectez-vous à {{site.data.keyword.cloud_notm}} ![Icône de lien externe](../../icons/launch-glyph.svg "Icône de lien externe")](https://cloud.ibm.com/login){:new_window} et suivez les invites.

    Sélectionnez le compte où vous avez mis l'instance {{site.data.keyword.la_full_notm}} à disposition.

2. Configurez l'environnement de cluster. Exécutez les commandes suivantes :

    Commencez par vous procurer la commande de définition de la variable d'environnement et téléchargez les fichiers de configuration Kubernetes.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    Une fois les fichiers de configuration téléchargés, une commande s'affiche ; elle vous permet de définir le chemin vers le fichier de configuration Kubernetes local en tant que variable d'environnement.

    Ensuite, copiez et collez la commande affichée sur votre terminal pour définir la variable d'environnement `KUBECONFIG`.

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




