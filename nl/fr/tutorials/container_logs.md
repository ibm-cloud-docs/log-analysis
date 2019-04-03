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


# Analyse dans Kibana des journaux d'une application déployée dans un cluster Kubernetes
{: #container_logs}
Suivez ce tutoriel pour apprendre à configurer un cluster afin de transférer des journaux au service {{site.data.keyword.loganalysisshort}} dans {{site.data.keyword.Bluemix_notm}}.
{:shortdesc}


## Objectifs
{: #objectives}

1. Définir des configurations de journalisation dans un cluster. 
2. Rechercher et analyser des journaux de conteneur pour une application déployée dans un cluster Kubernetes dans {{site.data.keyword.Bluemix_notm}}.

Ce tutoriel vous guide tout au long des étapes à suivre pour le scénario de bout en bout suivant dans {{site.data.keyword.Bluemix_notm}} : mettre à disposition un cluster, configurer le cluster pour l'envoi de journaux au service {{site.data.keyword.loganalysisshort}} dans {{site.data.keyword.Bluemix_notm}}, déployer une application dans le cluster, et utiliser Kibana pour afficher et filtrer les journaux de conteneur pour ce cluster.


**Remarque :** pour pouvoir suivre ce tutoriel, vous devez remplir les conditions requises et avoir suivi les tutoriels liés aux différentes étapes.


## Conditions requises
{: #prereq}

1. Etre membre ou propriétaire d'un compte {{site.data.keyword.Bluemix_notm}} et disposer des droits permettant de créer des clusters Kubernetes, de déployer des applications dans des clusters, et d'interroger les journaux dans {{site.data.keyword.Bluemix_notm}} pour l'analyse avancée dans Kibana.

    Votre ID utilisateur pour {{site.data.keyword.Bluemix_notm}} doit être associé aux règles suivantes :
    
    * Une règle IAM pour {{site.data.keyword.containershort}} avec les droits *Editeur*, *Opérateur* ou *Administrateur*.
    * Un rôle CF pour l'espace dans lequel le service {{site.data.keyword.loganalysisshort}} a été mis à disposition avec les droits *Développeur*.
    
    Pour plus d'informations, voir [Affectation d'une règle IAM à un utilisateur dans l'interface utilisateur IBM Cloud](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_account) et [Octroi à un utilisateur des droits permettant d'afficher les journaux d'espace dans l'interface utilisateur IBM Cloud](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space).

2. Disposer d'une session de terminal depuis laquelle vous pouvez gérer le cluster Kubernetes et déployer des applications à partir de la ligne de commande. Les exemples dans ce tutoriel sont valables pour un système Ubuntu Linux.

3. Installer les interfaces de ligne de commande pour pouvoir utiliser {{site.data.keyword.containershort}} et {{site.data.keyword.loganalysisshort}} sur votre système Ubuntu.

    * Installer l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}. Installer l'interface de ligne de commande {{site.data.keyword.containershort}} pour pouvoir créer et gérer vos clusters Kubernetes dans {{site.data.keyword.containershort}}, et pour pouvoir déployer des applications conteneurisées dans votre cluster. Pour plus d'informations, voir [Installation de l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}.](/docs/cli/index.html#overview)
    
    * Installer l'interface de ligne de commande {{site.data.keyword.loganalysisshort}}. Pour plus d'informations, voir [Configuration de l'interface de ligne de commande Log Analysis (plug-in IBM Cloud)](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#config_log_collection_cli).
    
4. Disposer d'un accès à un espace nommé **dev** sur votre compte dans la région Sud des Etats-Unis. 

    Les journaux disponibles dans le cluster seront configurés en vue de leur transfert au domaine d'espace associé à cet espace. 
    
    Vous allez mettre à disposition le service {{site.data.keyword.loganalysisshort}} dans cet espace.
    
    Vous devez disposer des droits **Développeur** dans cet espace pour pouvoir mettre à disposition le service {{site.data.keyword.loganalysisshort}}.
    
    Dans ce tutoriel, le nom de l'organisation est **MyOrg**.

    
 

## Etape 1 : Mise à disposition d'un cluster Kubernetes
{: #step25}

Procédez comme suit :

1. Créez un cluster Kubernetes standard.

   Pour plus d'informations, voir [Création de clusters](/docs/containers/cs_tutorials.html#cs_cluster_tutorial).

2. Configurez le contexte de cluster dans un terminal. Une fois le contexte défini, vous pouvez gérer le cluster Kubernetes et y déployer l'application.

    Connectez-vous à la région, l'organisation et l'espace dans l'environnement {{site.data.keyword.Bluemix_notm}} associé au cluster que vous avez créé. Pour plus d'informations, voir
[Comment se connecter
à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

	Initialisez le plug-in du service
{{site.data.keyword.containershort}}.

	```
	ibmcloud cs init
	```
	{: codeblock}

    Définissez votre cluster comme contexte du terminal.
    
	```
	ibmcloud cs cluster-config MyCluster
	```
	{: codeblock}

    La sortie de l'exécution de cette commande fournit la commande que vous devez exécuter dans votre terminal pour définir le chemin d'accès à votre fichier de configuration. Exemple :

	```
	export KUBECONFIG=/Users/ibm/.bluemix/plugins/container-service/clusters/MyCluster/kube-config-hou02-MyCluster.yml
	```
	{: codeblock}

    Copiez et collez la commande afin de définir la variable d'environnement dans votre terminal, puis appuyez sur **Entrée**.



## Etape 2 : Configuration de votre cluster en vue du transfert automatique des journaux au service {{site.data.keyword.loganalysisshort}}
{: #step26}

Lorsque l'application est déployée, les journaux sont collectés automatiquement par {{site.data.keyword.containershort}}. Toutefois, ils ne sont pas transférés automatiquement au service {{site.data.keyword.loganalysisshort}}. Vous devez créer dans votre cluster une ou plusieurs configurations de journalisation, qui définissent :

* L'emplacement auquel les journaux sont transférés. Vous pouvez transférer les journaux dans le domaine de compte ou dans un domaine d'espace.
* Quels sont les journaux qui sont transférés au service {{site.data.keyword.loganalysisshort}} en vue de leur analyse.


Avant de définir des configurations de journalisation, vérifiez vos définitions de configuration de journalisation existantes dans le cluster. Exécutez la commande suivante :

```
$ ibmcloud cs logging-config-get ClusterName
```
{: codeblock}

où *ClusterName* est le nom de votre cluster.

Par exemple, les configurations de journalisation qui sont définies pour le cluster *mycluster* sont les suivantes : 

```
$ ibmcloud cs logging-config-get mycluster
Retrieving cluster mycluster logging configurations...
OK
Id                                     Source       Namespace   Host                                Port   Org            Space   Protocol   Paths   
13ded2c0-83f5-4cc5-8de7-1e34e1287f34   worker       -           ingest.logging.ng.bluemix.net       9091   Demo_Org       dev     ibm        /var/log/syslog,/var/log/auth.log   
ae249c04-a3a9-4c29-a890-22d8da7bd1b2   container    *           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        -   
31739fc1-42e2-4b66-ac57-6a32091c257a   ingress      -           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        /var/log/alb/ids/*.log,/var/log/alb/ids/*.err,/var/log/alb/customerlogs/*.log,/var/log/alb/customerlogs/*.err   
6b8cfe89-4959-448d-898b-c3b0584eca71   kubernetes   -           ingest-eu-fra.logging.bluemix.net   9091   Demo_Org.      dev     ibm        /var/log/kubelet.log,/var/log/kube-proxy.log   

```
{: screen}

Pour afficher la liste des sources de journal pour lesquelles vous pouvez définir une configuration de journalisation, voir [Sources de journal](/docs/services/CloudLogAnalysis/containers/containers_kubernetes.html#log_sources).


### Configuration de votre cluster en vue du transfert des journaux d'erreur standard et de sortie standard au service {{site.data.keyword.loganalysisshort}}.
{: #containerstd}


Procédez comme suit pour envoyer les journaux de sortie standard et d'erreur standard à un domaine d'espace, où le nom d'organisation est *MyOrg* et le nom d'espace est *dev* dans la région Sud des Etats-Unis :

1. Vérifiez que votre ID utilisateur disposer des droits permettant d'ajouter une configuration de cluster. Seuls les utilisateurs associés à une règle IAM pour
{{site.data.keyword.containershort}} et disposant des droits permettant de gérer
les clusters peuvent activer cette fonction. L'un des rôles suivants est requis : *Administrateur*,
*Opérateur*.

    Afin de vérifier que votre ID utilisateur est associé à une règle IAM pour la
gestion des clusters, procédez comme suit :
    
    1. Connectez vous à la console {{site.data.keyword.Bluemix_notm}}. Ouvrez un navigateur Web et lancez le tableau de bord {{site.data.keyword.Bluemix_notm}} : [http://bluemix.net ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](http://bluemix.net){:new_window} Une fois que vous êtes connecté avec votre ID utilisateur et votre mot de passe, l'interface utilisateur {{site.data.keyword.Bluemix_notm}} s'ouvre.

    2. Dans la barre de menus, cliquez sur **Gérer > Compte > Utilisateurs**.  La fenêtre *Utilisateurs* affiche une liste d'utilisateurs avec leur adresse électronique et leur statut sur le compte actuellement sélectionné.
	
    3. Sélectionnez l'ID utilisateur et vérifiez qu'il est associé à une règle pour {{site.data.keyword.containershort}}.

    Si vous avez besoin de droits, prenez contact avec le propriétaire du compte ou un administrateur de compte. Seuls le propriétaire du compte et les utilisateurs qui disposent des droits permettant d'affecter des règles peuvent effectuer cette étape.

2. Créez une configuration de journalisation de cluster. Exécutez la commande suivante pour envoyer les fichiers journaux de sortie standard (*stdout*) et d'erreur standard (*stderr*) au service {{site.data.keyword.loganalysisshort}} :

    ```
    ibmcloud cs logging-config-create ClusterName --logsource container --namespace '*' --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    où 

    * *ClusterName* est le nom du cluster.
    * *EndPoint* est l'URL du service de journalisation dans la région dans laquelle le service {{site.data.keyword.loganalysisshort}} a été mis à disposition. Pour la liste des noeuds finaux, voir [Noeuds finaux](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls).
    * *OrgName* est le nom de l'organisation dans laquelle l'espace est disponible.
    * *SpaceName* est le nom de l'espace dans lequel le service {{site.data.keyword.loganalysisshort}} a été mis à disposition.


Par exemple, pour créer une configuration de journalisation qui transfère les journaux de sortie standard et d'erreur standard au développeur de l'espace dans la région Sud des Etats-Unis, exécutez la commande suivante :

```
ibmcloud cs logging-config-create mycluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}




### Configuration de votre cluster pour le transfert des journaux d'agent au service {{site.data.keyword.loganalysisshort}}
{: #workerlogs }

Procédez comme suit pour envoyer les journaux d'agent à un domaine d'espace, où le nom d'organisation est *MyOrg* et le nom d'espace est *dev* dans la région Sud des Etats-Unis :

1. Vérifiez que votre ID utilisateur disposer des droits permettant d'ajouter une configuration de cluster. Seuls les utilisateurs associés à une règle IAM pour
{{site.data.keyword.containershort}} et disposant des droits permettant de gérer
les clusters peuvent activer cette fonction. L'un des rôles suivants est requis : *Administrateur*,
*Opérateur*.

    Afin de vérifier que votre ID utilisateur est associé à une règle IAM pour la
gestion des clusters, procédez comme suit :
    
    1. Connectez vous à la console {{site.data.keyword.Bluemix_notm}}. Ouvrez un navigateur Web et lancez le tableau de bord {{site.data.keyword.Bluemix_notm}} : [http://bluemix.net ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](http://bluemix.net){:new_window} Une fois que vous êtes connecté avec votre ID utilisateur et votre mot de passe, l'interface utilisateur {{site.data.keyword.Bluemix_notm}} s'ouvre.

    2. Dans la barre de menus, cliquez sur **Gérer > Compte > Utilisateurs**.  La fenêtre *Utilisateurs* affiche une liste d'utilisateurs avec leur adresse électronique et leur statut sur le compte actuellement sélectionné.
	
    3. Sélectionnez l'ID utilisateur et vérifiez qu'il est associé à une règle pour {{site.data.keyword.containershort}}.

    Si vous avez besoin de droits, prenez contact avec le propriétaire du compte ou un administrateur de compte. Seuls le propriétaire du compte et les utilisateurs qui disposent des droits permettant d'affecter des règles peuvent effectuer cette étape.

2. Créez une configuration de journalisation de cluster. Exécutez la commande suivante pour envoyer les fichiers journaux
*/var/log/syslog* et */var/log/auth.log* au service
{{site.data.keyword.loganalysisshort}} :

    ```
    ibmcloud cs logging-config-create ClusterName --logsource worker --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    où 

    * *ClusterName* est le nom du cluster.
    * *EndPoint* est l'URL du service de journalisation dans la région dans laquelle le service {{site.data.keyword.loganalysisshort}} a été mis à disposition. Pour la liste des noeuds finaux, voir [Noeuds finaux](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls).
    * *OrgName* est le nom de l'organisation dans laquelle l'espace est disponible.
    * *SpaceName* est le nom de l'espace dans lequel le service {{site.data.keyword.loganalysisshort}} a été mis à disposition.

    
Par exemple, pour créer une configuration de journalisation qui transfère des journaux d'agent à un domaine d'espace dans la région Sud des Etats-Unis, exécutez la commande suivante :

```
ibmcloud cs logging-config-create mycluster --logsource worker  --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}



## Etape 3 : Octroi de droits à votre utilisateur pour l'affichage des journaux dans un domaine d'espace
{: #step33}

Afin d'accorder des droits à un utilisateur pour qu'il puisse afficher les journaux dans un espace, vous devez lui attribuer un rôle Cloud Foundry qui décrit les actions qu'il peut effectuer avec le service {{site.data.keyword.loganalysisshort}} dans l'espace. 

Pour accorder à un utilisateur des droits permettant d'utiliser le service {{site.data.keyword.loganalysisshort}}, procédez comme suit :

1. Connectez vous à la console {{site.data.keyword.Bluemix_notm}}.

    Ouvrez un navigateur Web et lancez le tableau de bord {{site.data.keyword.Bluemix_notm}} : [http://bluemix.net ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](http://bluemix.net){:new_window}
	
	Une fois que vous êtes connecté avec votre ID utilisateur et votre mot de passe, l'interface utilisateur {{site.data.keyword.Bluemix_notm}} s'ouvre.

2. Dans la barre de menus, cliquez sur **Gérer > Compte > Utilisateurs**. 

    La fenêtre *Utilisateurs* affiche une liste d'utilisateurs avec leur adresse électronique et leur statut sur le compte actuellement sélectionné.
	
3. Si l'utilisateur est membre du compte, sélectionnez le nom de l'utilisateur dans la liste ou cliquez sur **Gérer un utilisateur** dans le menu *Actions*.

    Si l'utilisateur n'est pas membre du compte, voir [Invitation d'utilisateurs](/docs/iam/iamuserinv.html#iamuserinv).

4. Sélectionnez **Accès Cloud Foundry**, puis sélectionnez l'organisation.

    La liste des espaces disponibles dans cette organisation est affichée.

5. Choisissez l'espace. Ensuite, dans le menu d'actions, sélectionnez **Editer un rôle d'espace**.

    Si l'espace n'apparaît pas pour la région Sud des Etats-Unis, créez-le avant de continuer.

6. Sélectionnez *Développeur*.

    Vous pouvez sélectionner un ou plusieurs rôles. 
    
    Les rôles valides sont : *Responsable*, *Développeur* et *Auditeur*.
	
7. Cliquez sur **Sauvegarder le rôle**.


## Etape 4 : Octroi de droits au propriétaire de clé {{site.data.keyword.containershort_notm}}
{: #step52}

Pour que les journaux de cluster soient transférés vers un espace, le propriétaire de clé {{site.data.keyword.containershort_notm}} doit disposer des droits suivants :

* Règle IAM pour le service {{site.data.keyword.loganalysisshort}} avec des droits *Administrateur*.
* Droits Cloud Foundry (CF) dans l'organisation et l'espace où les journaux doivent être transférés. Le propriétaire de clé du conteneur requiert le rôle *orgManager* pour l'organisation et les rôles *SpaceManager* et *Developer* pour l'espace.

Procédez comme suit :

1. Identifiez sur le compte l'utilisateur qui est le propriétaire de clé {{site.data.keyword.containershort}}. Depuis un terminal, exécutez la commande suivante :

    ```
    ibmcloud cs api-key-info ClusterName
    ```
    {: codeblock}
    
    où *ClusterName* est le nom du cluster.

2. Vérifiez que l'utilisateur identifié comme propriétaire de clé {{site.data.keyword.containershort}} possède le rôle *orgManager* pour l'organisation et les rôles *SpaceManager* et *Developer* pour l'espace.

    Connectez vous à la console {{site.data.keyword.Bluemix_notm}}. Ouvrez un navigateur Web et lancez le tableau de bord {{site.data.keyword.Bluemix_notm}} : [http://bluemix.net ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](http://bluemix.net){:new_window} Une fois que vous êtes connecté avec votre ID utilisateur et votre mot de passe, l'interface utilisateur {{site.data.keyword.Bluemix_notm}} s'ouvre.

    Dans la barre de menus, cliquez sur **Gérer > Compte > Utilisateurs**.  La fenêtre *Utilisateurs* affiche une liste d'utilisateurs avec leur adresse électronique et leur statut sur le compte actuellement sélectionné.
	
    Sélectionnez l'ID de l'utilisateur et vérifiez que l'utilisateur possède le rôle *orgManager* pour l'organisation et les rôles *SpaceManager* et *Developer* pour l'espace.

    Si l'utilisateur ne dispose pas des droits appropriés, accordez à l'utilisateur les droits suivants : le rôle *orgManager* pour l'organisation et les rôles *SpaceManager* et *Developer* pour l'espace. Pour plus d'informations, voir [Octroi à un utilisateur des droits permettant d'afficher les journaux d'espace dans l'interface utilisateur IBM Cloud](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space).
    
3. Vérifiez que l'utilisateur identifié comme propriétaire de clé {{site.data.keyword.containershort}} dispose d'une règle IAM pour le service {{site.data.keyword.loganalysisshort}} avec les droits *Administrateur*.

    Dans la barre de menus, cliquez sur **Gérer > Compte > Utilisateurs**.  La fenêtre *Utilisateurs* affiche une liste d'utilisateurs avec leur adresse électronique et leur statut sur le compte actuellement sélectionné.
	
    Sélectionnez l'ID de l'utilisateur et vérifiez que l'utilisateur dispose de l'ensemble de règles IAM. 

    Si l'utilisateur ne dispose pas de la règle IAM, voir [Affectation d'une règle IAM à un utilisateur dans l'interface utilisateur IBM Cloud](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_account).

4. Actualisez la configuration de journalisation. Exécutez la commande suivante :
    
    ```
    ibmcloud cs logging-config-refresh ClusterName
    ```
    {: codeblock}
        
    où *ClusterName* est le nom du cluster.
	



## Etape 5 : Déploiement d'un exemple d'application dans le cluster Kubernetes pour générer un contenu dans la sortie standard
{: #step53}

Déployez et exécutez un exemple d'application dans le cluster Kubernetes. Effectuez les étapes du tutoriel suivant pour déployer l'exemple d'application : [Leçon 1 : Déploiement d'applications avec instance unique dans des clusters Kubernetes](/docs/containers/cs_tutorials_apps.html#cs_apps_tutorial_lesson1).

L'application est une application Hello World Node.js :

```
var express = require('express')
var app = express()

app.get('/', function(req, res) {
  res.send('Hello world! Your app is up and running in a cluster!\n')
})
app.listen(8080, function() {
  console.log('Sample app is listening on port 8080.')
})
```
{: screen}

Dans cet exemple d'application, lorsque vous testez votre application dans un navigateur, l'application consigne dans stdout le message suivant : `L'exemple d'application est à l'écoute sur le port 8080.`






## Etape 6 : Affichage des données de journal dans Kibana
{: #step6}

Procédez comme suit :

1. Lancez Kibana dans un navigateur. 

    Pour plus d'informations sur le lancement de Kibana, voir [Accès à Kibana depuis un navigateur Web](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser).

    Afin d'analyser les données de journal pour un cluster, vous devez accéder à Kibana dans la région de cloud publique dans laquelle le cluster a été créé. 
    
    Par exemple, dans la région Sud des Etats-Unis, entrez l'URL suivante pour lancer Kibana :
	
	```
	https://logging.ng.bluemix.net/ 
	```
	{: codeblock}
	
    Kibana s'ouvre.
    
    **REMARQUE :** assurez-vous de lancer Kibana dans la région dans laquelle vous transférez vos journaux de cluster. Pour des informations sur les URL par région, voir [Noeuds finaux de journalisation](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#urls_kibana).
    	
2. Pour afficher les données de journal qui sont disponibles dans le domaine d'espace, procédez comme suit :

    1. Dans Kibana, cliquez sur votre ID utilisateur. La vue permettant de définir l'espace s'ouvre.
    
    2. Sélectionnez le compte sur lequel l'espace est disponible. 
    
    3. Sélectionnez le domaine suivant : **space**
    
    4. Sélectionnez l'organisation *MyOrg* dans laquelle l'espace est disponible.
    
    5. Sélectionnez l'espace *dev*.
    
    
3. Dans la page **Discover**, examinez les événements qui sont affichés. 
        
    La section *Available fields* affiche la liste des zones que vous pouvez utiliser pour définir de nouvelles requêtes ou pour filtrer les entrées dans le tableau affiché dans la page.
    
    Le tableau ci-dessous répertorie certaines des zones que vous pouvez utiliser pour définir de nouvelles requêtes de recherche lors de l'analyse des journaux d'application. Il comprend également des exemples de valeur correspondant à l'événement généré par l'exemple d'application :
 
    <table>
              <caption>Tableau 2. Zones communes aux journaux de conteneur </caption>
               <tr>
                <th align="center">Zone</th>
                <th align="center">Description</th>
                <th align="center">Exemple</th>
              </tr>
              <tr>
                <td>*ibm-containers.region_str*</td>
                <td>La valeur de cette zone correspond à la région {{site.data.keyword.Bluemix_notm}} dans laquelle l'entrée de journal est collectée.</td>
                <td>us-south</td>
              </tr>
			  <tr>
                <td>*ibm-containers.account_id_str*</td>
                <td>ID de compte</td>
                <td></td>
              </tr>
			  <tr>
                <td>*ibm-containers.cluster_id_str *</td>
                <td>ID de cluster.</td>
                <td></td>
              </tr>
              <tr>
                <td>*ibm-containers.cluster_name_str*</td>
                <td>ID de cluster</td>
                <td></td>
              </tr>
			  <tr>
                <td>*kubernetes.namespace_name_str*</td>
                <td>Nom de l'espace de nom</td>
                <td>*default* est la valeur par défaut.</td>
              </tr>
              <tr>
                <td>*kubernetes.container_name_str*</td>
                <td>Nom du conteneur</td>
                <td>hello-world-deployment</td>
              </tr>
              <tr>
                <td>*kubernetes.labels.label_name*</td>
                <td>Les zones de libellé sont facultatives. Vous pouvez ne pas les utiliser ou en utiliser plusieurs. Chaque libellé commence par le préfixe `kubernetes.labels.`, suivi du nom de libellé (*label_name*). </td>
                <td>Dans l'exemple d'application, vous pouvez observer 2 libellés : <br>* *kubernetes.labels.pod-template-hash_str* = 3355293961 <br>* *kubernetes.labels.run_str* =	hello-world-deployment  </td>
              </tr>
              <tr>
                <td>*stream_str *</td>
                <td>Type de journal.</td>
                <td>*stdout*, *stderr*</td>
              </tr>
        </table>
     
Pour plus d'informations sur les autres zones de recherche pertinentes pour les clusters Kubernetes, voir [Recherche des journaux](/docs/services/CloudLogAnalysis/containers/containers_kubernetes.html#log_search).


## Etape 7 : Filtrage des données par nom de cluster Kubernetes dans Kibana
{: #step7}
    
Le tableau affiché dans la page *Discover* répertorie toutes les entrées disponibles pour l'analyse. Les entrées répertoriées correspondent à la requête de recherche affichée dans la barre *Rechercher*. Utilisez un astérisque (*) afin d'afficher toutes les entrées pour la période configurée pour la page.
    
Par exemple, pour filtrer les données par nom de cluster Kubernetes, modifiez la requête dans la barre *Rechercher*. Ajoutez un filtre reposant sur la zone personnalisée *kubernetes.cluster_name_str* :
    
1. Dans la section **Available fields**, sélectionnez la zone *kubernetes.cluster_name_str*. Un sous-ensemble des valeurs disponibles pour la zone est affiché.    
    
2. Sélectionnez la valeur qui correspond au cluster pour lequel analyser les journaux. 
    
    Une fois que vous avez sélectionné la valeur, un filtre est ajouté à la *barre de recherche* et le tableau n'affiche plus que les entrées correspondant aux critères que vous venez de sélectionner.     
   

**Remarque :** 

Si votre nom de cluster n'apparaît pas, ajoutez un filtre pour le nom de cluster de votre choix. Ensuite, cliquez sur le symbole d'édition du filtre.    
    
La requête suivante est affichée :
    
```
	{
        "query": {
          "match": {
            "kubernetes.cluster_name_str": {
              "query": "cluster1",
              "type": "phrase"
            }
          }
        }
      }
```
{: screen}

Remplacez le nom du cluster (*cluster1*) par le nom de cluster *mycluster* pour lequel afficher les données de journal.
        
Si aucune donnée ne s'affiche, essayez de changer le filtre temporel. Pour plus d'informations, voir [Définition d'un filtre temporel](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter).

Pour plus d'informations, voir [Filtrage des journaux dans Kibana](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#filter_logs).


## Documents de référence pour {{site.data.keyword.containershort_notm}}
{: reference}

Commandes de l'interface de ligne de commande :

* [ibmcloud cs api-key-info](/docs/containers/cs_cli_reference.html#cs_api_key_info)
* [ibmcloud cs logging-config-create](/docs/containers/cs_cli_reference.html#cs_logging_create)
* [ibmcloud cs logging-config-get](/docs/containers/cs_cli_reference.html#cs_logging_get)
* [ibmcloud cs logging-config-update](/docs/containers/cs_cli_reference.html#cs_logging_update)
* [ibmcloud cs logging-config-rm](/docs/containers/cs_cli_reference.html#cs_logging_rm)
* [ibmcloud cs logging-config-refresh](/docs/containers/cs_cli_reference.html#cs_logging_refresh)

