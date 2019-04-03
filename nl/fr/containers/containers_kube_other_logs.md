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


# Activation de la collecte automatique des journaux de cluster
{: #containers_kube_other_logs}

Pour pouvoir afficher et analyser des journaux de cluster dans le service
{{site.data.keyword.loganalysisshort}}, vous devez configurer votre cluster de
sorte à transmettre ces journaux au service
{{site.data.keyword.loganalysisshort}}. 
{:shortdesc}

## Etape 1 : Vérification des droits de votre ID utilisateur
{: step1}

Votre ID utilisateur doit disposer des droits suivants pour que vous puissiez ajouter une configuration de journalisation au cluster :

* Règle IAM pour le {{site.data.keyword.containershort}} avec les droits **Afficheur**.
* Règle IAM pour l'instance de cluster avec les droits **Administrateur** ou **Opérateur**.

Afin de vérifier que votre ID utilisateur dispose de ces règles IAM, procédez comme suit :

**Remarque :** seuls le propriétaire du compte et les
utilisateurs
disposant des droits permettant d'affecter des règles peuvent effectuer cette étape.

1. Connectez vous à la console {{site.data.keyword.Bluemix_notm}}. Ouvrez un navigateur Web et lancez le tableau de bord {{site.data.keyword.Bluemix_notm}} : [http://bluemix.net ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](http://bluemix.net){:new_window}
	
	Une fois que vous êtes connecté avec votre ID utilisateur et votre mot de passe, l'interface utilisateur {{site.data.keyword.Bluemix_notm}} s'ouvre.

2. Dans la barre de menus, cliquez sur **Gérer > Compte > Utilisateurs**.  La fenêtre *Utilisateurs* affiche une liste d'utilisateurs avec leur adresse électronique et leur statut sur le compte actuellement sélectionné.
	
3. Sélectionnez l'ID utilisateur et vérifiez qu'il dispose des deux règles.




## Etape 2 : Configuration du contexte de cluster
{: #step2}

Procédez comme suit :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
    
2. Initialisez le plug-in du service
{{site.data.keyword.loganalysisshort}}.

	```
	ibmcloud ks init
	```
	{: codeblock}

3. Définissez votre cluster comme contexte du terminal.
    
	```
	ibmcloud ks cluster-config ClusterName
	```
	{: codeblock}

    La sortie de l'exécution de cette commande fournit la commande que vous devez exécuter dans votre terminal pour définir le chemin d'accès à votre fichier de configuration. Par exemple, pour un cluster nommé *MyCluster* :

	```
	export KUBECONFIG=/Users/ibm/.bluemix/plugins/container-service/clusters/MyCluster/kube-config-hou02-MyCluster.yml
	```
	{: codeblock}

4. Copiez et collez la commande afin de définir la variable d'environnement dans votre terminal, puis appuyez sur **Entrée**.



## Etape 3 : Configuration de votre cluster
{: step3}

Vous pouvez choisir les journaux de cluster à transmettre au service
{{site.data.keyword.loganalysisshort}}. 

* Pour activer la collecte et le transfert automatiques de la sortie et de l'erreur standard, voir [Activation de la collecte et du transfert automatiques des journaux de conteneur](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#containers).
* Pour activer la collecte et le transfert automatiques des journaux
d'application, voir
[Activation
de la collecte et du transfert automatiques des journaux d'application](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#apps).
* Pour activer la collecte et le transfert automatiques des journaux
d'agent, voir
[Activation
de la collecte et du transfert automatiques des journaux d'agent](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#workers).
* Pour activer la collecte et le transfert automatiques des journaux de composant système Kubernetes, voir [Activation de la collecte et du transfert automatiques des journaux de composant système Kubernetes](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#system).
* Pour activer la collecte et le transfert automatiques des journaux de
contrôleur Ingress, voir
[Activation
de la collecte et du transfert automatiques des journaux de contrôleur Ingress Kubernetes](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#controller).



## Etape 4 : Définition des droits pour le propriétaire de clé {{site.data.keyword.containershort_notm}}
{: #step4}


Le propriétaire de la clé {{site.data.keyword.containershort}} a besoin des règles IAM suivantes :

* Règle IAM pour le {{site.data.keyword.containershort}} avec le rôle **Administrateur**.
* Règle IAM pour le service {{site.data.keyword.loganalysisshort}} avec le rôle **Administrateur**.

Procédez comme suit : 

1. Connectez vous à la console {{site.data.keyword.Bluemix_notm}}. Ouvrez un navigateur Web et lancez le tableau de bord {{site.data.keyword.Bluemix_notm}} : [http://bluemix.net ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](http://bluemix.net){:new_window}
	
	Une fois que vous êtes connecté avec votre ID utilisateur et votre mot de passe, l'interface utilisateur {{site.data.keyword.Bluemix_notm}} s'ouvre.

2. Dans la barre de menus, cliquez sur **Gérer > Compte > Utilisateurs**.  La fenêtre *Utilisateurs* affiche une liste d'utilisateurs avec leur adresse électronique et leur statut sur le compte actuellement sélectionné.
	
3. Sélectionnez l'ID utilisateur pour le propriétaire de clé {{site.data.keyword.containershort_notm}} et vérifiez qu'il dispose des deux règles.


Lorsque vous transférez des journaux vers un domaine d'espace, vous devez aussi accorder des droits Cloud Foundry (CF) au propriétaire de clé {{site.data.keyword.containershort}} dans l'organisation et l'espace. Le propriétaire de clé requiert le rôle *orgManager* pour l'organisation et le rôle *SpaceManager* ou *Developer* pour l'espace.

Procédez comme suit :

1. Identifiez sur le compte l'utilisateur qui est le propriétaire de clé {{site.data.keyword.containershort}}. Depuis un terminal, exécutez la commande suivante :

    ```
    ibmcloud ks api-key-info ClusterName
    ```
    {: codeblock}
    
    où *ClusterName* est le nom du cluster.
    
2. Vérifiez que l'utilisateur identifié comme propriétaire de clé {{site.data.keyword.containershort}} possède le rôle *orgManager* pour l'organisation et les rôles *SpaceManager* et *Developer* pour l'espace.

    Connectez vous à la console {{site.data.keyword.Bluemix_notm}}. Ouvrez un navigateur Web et lancez le tableau de bord {{site.data.keyword.Bluemix_notm}} : [http://bluemix.net ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](http://bluemix.net){:new_window} Une fois que vous êtes connecté avec votre ID utilisateur et votre mot de passe, l'interface utilisateur {{site.data.keyword.Bluemix_notm}} s'ouvre.

    Dans la barre de menus, cliquez sur **Gérer > Compte > Utilisateurs**.  La fenêtre *Utilisateurs* affiche une liste d'utilisateurs avec leur adresse électronique et leur statut sur le compte actuellement sélectionné.
	
    Sélectionnez l'ID de l'utilisateur et vérifiez que l'utilisateur possède le rôle *orgManager* pour l'organisation et le rôle *SpaceManager* ou *Developer* pour l'espace.
 
3. Si l'utilisateur ne dispose pas des droits appropriés, procédez comme suit :

    1. Accordez à l'utilisateur les droits suivants : le rôle *orgManager* pour l'organisation et les rôles *SpaceManager* et *Developer* pour l'espace. Pour plus d'informations, voir [Octroi à un utilisateur des droits permettant d'afficher les journaux d'espace dans l'interface utilisateur IBM Cloud](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_space).
    
    2. Actualisez la configuration de journalisation. Exécutez la commande suivante :
    
        ```
        ibmcloud ks logging-config-refresh ClusterName
        ```
        {: codeblock}
        
        où *ClusterName* est le nom du cluster.
  




## Activation de la collecte et du transfert automatiques des journaux de conteneur 
{: #containers}

Exécutez la commande suivante pour envoyer les fichiers journaux de sortie standard (*stdout*) et d'erreur standard (*stderr*) au service {{site.data.keyword.loganalysisshort}} :

```
ibmcloud ks logging-config-create ClusterName --logsource container --namespace '*' --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

où 

* *ClusterName* est le nom du cluster.
* *EndPoint* est l'URL du service de journalisation dans la région dans laquelle le service {{site.data.keyword.loganalysisshort}} a été mis à disposition. Pour la liste des noeuds finaux, voir [Noeuds finaux](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
* *OrgName* est le nom de l'organisation dans laquelle l'espace est disponible.
* *SpaceName* est le nom de l'espace dans lequel le service {{site.data.keyword.loganalysisshort}} a été mis à disposition.


Par exemple, pour créer une configuration de journalisation qui transfère les journaux de sortie standard et d'erreur standard au domaine de compte dans la région Allemagne, exécutez la commande suivante :

```
ibmcloud ks logging-config-create MyCluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}

Pour créer une configuration de journalisation qui transfère les journaux de sortie standard et d'erreur standard à un domaine d'espace dans la région Allemagne, exécutez la commande suivante :

```
ibmcloud ks logging-config-create MyCluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org MyOrg --space MySpace
```
{: screen}



## Activation de la collecte et du transfert automatiques des journaux d'application 
{: #apps}

Exécutez la commande suivante pour envoyer les fichiers journaux
*/var/log/apps/**/.log* et */var/log/apps/*/.err*
au service {{site.data.keyword.loganalysisshort}} :

```
ibmcloud ks logging-config-create ClusterName --logsource application --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName --app-containers --app-paths
```
{: codeblock}

où 

* *ClusterName* est le nom du cluster.
* *EndPoint* est l'URL du service de journalisation dans la région dans laquelle le service {{site.data.keyword.loganalysisshort}} a été mis à disposition. Pour la liste des noeuds finaux, voir [Noeuds finaux](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
* *OrgName* est le nom de l'organisation dans laquelle l'espace est disponible.
* *SpaceName* est le nom de l'espace dans lequel le service {{site.data.keyword.loganalysisshort}} a été mis à disposition.
* *app-containers* est un paramètre facultatif que vous pouvez configurer pour définir une liste de conteneurs à surveiller. Ces conteneurs sont les seuls à partir desquels les journaux seront réacheminés vers {{site.data.keyword.loganalysisshort}}. Vous pouvez définir un ou plusieurs conteneurs en les séparant par des virgules.
* *app-paths* définit les chemins à l'intérieur des conteneurs à surveiller. Vous pouvez définir un ou plusieurs chemins en les séparant par des virgules. Les caractères génériques tels que '/var/log/*.log' sont acceptés. 

Par exemple, pour créer une configuration de journalisation qui transfère des journaux d'application à un domaine d'espace dans la région Allemagne, exécutez la commande suivante :

```
ibmcloud ks logging-config-create MyCluster --logsource application --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org MyOrg --space MySpace --app-paths /var/log/*.log
```
{: screen}

Par exemple, pour créer une configuration de journalisation qui transfère des journaux d'application à un domaine de compte dans la région Allemagne, exécutez la commande suivante :

```
ibmcloud ks logging-config-create MyCluster --logsource application --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --app-paths /var/log/*.log
```
{: screen}



## Activation de la collecte et du transfert automatiques des journaux d'agent 
{: #workers}


Exécutez la commande suivante pour envoyer les fichiers journaux
*/var/log/syslog* et */var/log/auth.log* au service
{{site.data.keyword.loganalysisshort}} :

```
ibmcloud ks logging-config-create ClusterName --logsource worker --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

où 

* *ClusterName* est le nom du cluster.
* *EndPoint* est l'URL du service de journalisation dans la région dans laquelle le service {{site.data.keyword.loganalysisshort}} a été mis à disposition. Pour la liste des noeuds finaux, voir [Noeuds finaux](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
* *OrgName* est le nom de l'organisation dans laquelle l'espace est disponible.
* *SpaceName* est le nom de l'espace dans lequel le service {{site.data.keyword.loganalysisshort}} a été mis à disposition.



Par exemple, pour créer une configuration de journalisation qui transfère des journaux d'agent à un domaine d'espace dans la région Allemagne, exécutez la commande suivante :

```
ibmcloud ks logging-config-create MyCluster --logsource worker  --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

Par exemple, pour créer une configuration de journalisation qui transfère des journaux d'agent à un domaine de compte dans la région Allemagne, exécutez la commande suivante :

```
ibmcloud ks logging-config-create MyCluster --logsource worker  --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}



## Activation de la collecte et du transfert automatiques des journaux de composant système Kubernetes
{: #system}

Exécutez la commande suivante pour envoyer les fichiers journaux
*/var/log/kubelet.log* et */var/log/kube-proxy.log* au service
{{site.data.keyword.loganalysisshort}} :

```
ibmcloud ks logging-config-create ClusterName --logsource kubernetes --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

où 

* *ClusterName* est le nom du cluster.
* *EndPoint* est l'URL du service de journalisation dans la région dans laquelle le service {{site.data.keyword.loganalysisshort}} a été mis à disposition. Pour la liste des noeuds finaux, voir [Noeuds finaux](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
* *OrgName* est le nom de l'organisation dans laquelle l'espace est disponible.
* *SpaceName* est le nom de l'espace dans lequel le service {{site.data.keyword.loganalysisshort}} a été mis à disposition.



Par exemple, pour créer une configuration de journalisation qui transfère des journaux de composant système Kubernetes à un domaine d'espace dans la région Allemagne, exécutez la commande suivante :

```
ibmcloud ks logging-config-create MyCluster --logsource kubernetes --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

Par exemple, pour créer une configuration de journalisation qui transfère des journaux de composant système Kubernetes à un domaine de compte dans la région Allemagne, exécutez la commande suivante :

```
ibmcloud ks logging-config-create MyCluster --logsource kubernetes --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}



## Activation de la collecte et du transfert automatiques des journaux de contrôleur Ingress Kubernetes
{: #controller}

Exécutez la commande suivante pour envoyer les fichiers journaux */var/log/alb/ids/.log*,
*/var/log/alb/ids/.err*, */var/log/alb/customerlogs/.log* et
/var/log/alb/customerlogs/.err* au service {{site.data.keyword.loganalysisshort}} :

```
ibmcloud ks logging-config-create ClusterName --logsource ingress --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName
```
{: codeblock}

où 

* *ClusterName* est le nom du cluster.
* *EndPoint* est l'URL du service de journalisation dans la région dans laquelle le service {{site.data.keyword.loganalysisshort}} a été mis à disposition. Pour la liste des noeuds finaux, voir [Noeuds finaux](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
* *OrgName* est le nom de l'organisation dans laquelle l'espace est disponible.
* *SpaceName* est le nom de l'espace dans lequel le service {{site.data.keyword.loganalysisshort}} a été mis à disposition.



Par exemple, pour créer une configuration de journalisation qui transfère des journaux de contrôleur Ingress à un domaine d'espace dans la région Allemagne, exécutez la commande suivante :

```
ibmcloud ks logging-config-create MyLoggingDemoCluster --logsource ingress --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

Par exemple, pour créer une configuration de journalisation qui transfère des journaux de contrôleur Ingress à un domaine de compte dans la région Allemagne, exécutez la commande suivante :

```
ibmcloud ks logging-config-create MyLoggingDemoCluster --logsource ingress --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091  
```
{: screen}



