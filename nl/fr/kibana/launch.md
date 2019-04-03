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


# Accès au tableau de bord Kibana
{: #launch}

Vous pouvez lancer Kibana à partir du service {{site.data.keyword.loganalysisshort}}, depuis l'interface utilisateur {{site.data.keyword.Bluemix}} ou directement depuis un
navigateur Web.
{:shortdesc}

Pour les applications CF et les conteneurs Docker, vous pouvez lancer Kibana depuis l'interface utilisateur {{site.data.keyword.Bluemix_notm}} pour afficher et analyser des données dans le contexte de la ressource à partir de laquelle vous lancez Kibana. Par
exemple, vous pouvez ouvrir vos journaux d'application CK spécifiques dans Kibana, dans le contexte de cette application spécifique.
    
Pour toute ressource de cloud telle qu'un conteneur Docker qui est déployée dans une infrastructure Kubernetes, vous pouvez lancer Kibana directement depuis un lien de navigateur direct ou à partir du tableau de bord du service {{site.data.keyword.loganalysisshort}} pour afficher des données de journal agrégées depuis les services d'un espace donné. La requête utilisée pour filtrer les données affichées dans le tableau de bord extrait les entrées de journal pour un espace dans l'organisation. Les informations de journal que Kibana affiche incluent les enregistrements de toutes les ressources qui sont déployées dans l'espace de l'organisation à laquelle vous êtes connecté. 

Le tableau suivant recense certaines ressources de cloud et les méthodes de navigation prises en charge pour lancer Kibana :

<table>
<caption>Tableau 1. Liste des ressources et des méthodes de navigation prises en charge. </caption>
  <tr>
    <th>Ressource</th>
	<th>Accès au tableau de bord Kibana depuis le tableau de bord du service {{site.data.keyword.loganalysisshort}}</th>
    <th>Accès au tableau de bord Kibana depuis le tableau de bord Bluemix</th>
    <th>Accès au tableau de bord Kibana depuis un navigateur Web</th>
  </tr>
  <tr>
    <td>Application CF</td>
	<td>Oui</td>
    <td>Oui</td>
    <td>Oui</td>
  </tr>  
  <tr>
    <td>Conteneur déployé dans un cluster Kubernetes</td>
	<td>Oui</td>
    <td>Oui</td>
    <td>Oui</td>
  </tr>  
  <tr>
    <td>Conteneur déployé dans une infrastructure gérée par {{site.data.keyword.Bluemix_notm}} (déprécié)</td>
	<td>Oui</td>
    <td>Oui</td>
    <td>Oui</td>
  </tr>  
</table>

Pour plus d'informations sur Kibana, reportez-vous au manuel [Kibana User Guide ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}.
    

##  Accès à Kibana depuis le tableau de bord du service Log Analysis
{: #launch_Kibana_from_log_analysis}

La requête utilisée pour filtrer les données affichées dans Kibana extrait les entrées de journal pour cet espace dans l'organisation. 
	
Les informations de journal que Kibana affiche incluent les enregistrements de toutes les ressources qui sont déployées dans l'espace de l'organisation à laquelle vous êtes connecté.

Procédez comme suit pour lancer Kibana depuis le tableau de bord du service {{site.data.keyword.loganalysisshort}} :

1. Connectez-vous à {{site.data.keyword.Bluemix_notm}}, puis cliquez sur le service {{site.data.keyword.loganalysisshort}} dans le tableau de bord {{site.data.keyword.Bluemix_notm}}. 
    
2. Sélectionnez l'onglet **Managed** dans l'interface utilisateur {{site.data.keyword.Bluemix_notm}}.

3. Cliquez sur **LAUNCH**. Le tableau de bord Kibana s'ouvre.

Par défaut, la page **Discover** se charge avec le canevas d'index par défaut sélectionné et un filtre temporel défini sur les 15 dernières minutes. 

Si la page Discover n'affiche aucune entrée de journal, ajustez le sélecteur de période. Pour plus d'informations, voir [Définition d'un filtre temporel](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter).

	
	
##  Accès à Kibana depuis un navigateur Web
{: #launch_Kibana_from_browser}

La requête utilisée pour filtrer les données affichées dans Kibana extrait les entrées de journal pour cet espace dans l'organisation. 
	
Les informations de journal que Kibana affiche incluent les enregistrements de toutes les ressources qui sont déployées dans l'espace de l'organisation à laquelle vous êtes connecté.

Pour lancer Kibana depuis un navigateur, procédez comme suit :

1. Ouvrez un navigateur Web et lancez Kibana. Ensuite, connectez-vous à l'interface utilisateur Kibana.

    Pour afficher la liste des URL par région, voir [URL d'ouverture de Kibana](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#urls_kibana).
    
    La page Discover s'ouvre dans Kibana.
	
2. Sélectionnez le canevas d'index pour l'espace à partir duquel vous voulez afficher et analyser les données de journal.

    1. Cliquez sur **default-index**.
	
	2. Sélectionnez le canevas d'index pour l'espace. Le format du canevas d'index est le suivant :
	
	    ```
	    [logstash-Space_ID-]YYYY.MM.DD 
	    ```
        {: screen}
	
	    où *Space_ID* est l'identificateur global unique de l'espace dans lequel vous voulez afficher et analyser les données de journal. 
	
Si la page Discover n'affiche aucune entrée de journal, ajustez le sélecteur de période. Pour plus d'informations, voir [Définition d'un filtre temporel](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter).


	
##  Accès à Kibana depuis le tableau de bord d'une application CF
{: #launch_Kibana_from_cf_app}

La requête qui est utilisée pour filtrer les données qui s'affichent dans Kibana récupère les entrées de journal pour l'application CF {{site.data.keyword.Bluemix_notm}} depuis
l'endroit où vous lancez Kibana.

Pour afficher les journaux d'une application Cloud Foundry dans Kibana, procédez comme suit :

1. Connectez-vous à votre compte {{site.data.keyword.Bluemix_notm}}.

    Le tableau de bord {{site.data.keyword.Bluemix_notm}} se trouve à l'adresse suivante : [http://bluemix.net ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](http://bluemix.net){:new_window}.
    
	Une fois que vous êtes connecté avec votre ID utilisateur et votre mot de passe, l'interface utilisateur {{site.data.keyword.Bluemix_notm}} s'ouvre.

2. Cliquez sur le nom de l'application ou sur le conteneur dans le tableau de bord {{site.data.keyword.Bluemix_notm}}. 
    
3. Ouvrez l'onglet des journaux dans l'interface utilisateur {{site.data.keyword.Bluemix_notm}}.

    Pour les applications CF, cliquez sur **Journaux** dans la barre de navigation. 
    L'onglet des journaux s'affiche.  

4. Cliquez sur **Afficher dans Kibana**. Le tableau de bord Kibana s'ouvre.

    Par défaut, la page **Discover** se charge avec le canevas d'index par défaut sélectionné et un filtre temporel défini sur les 15 dernières minutes. La requête de recherche permet de rechercher toutes les entrées pour l'application CF.

    Si la page Discover n'affiche aucune entrée de journal, ajustez le sélecteur de période. Pour plus d'informations, voir [Définition d'un filtre temporel](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter).

	
	
##  Accès à Kibana depuis le tableau de bord d'un conteneur qui est déployé dans un cluster Kubernetes
{: #launch_Kibana_for_containers_kube}

La requête utilisée pour filtrer les données affichées dans Kibana extrait les entrées de journal pour le cluster depuis lequel vous lancez Kibana.

Pour afficher les journaux d'un conteneur dans Kibana, procédez comme suit :

1. Connectez-vous à votre compte {{site.data.keyword.Bluemix_notm}}.

    Le tableau de bord {{site.data.keyword.Bluemix_notm}} se trouve à l'adresse suivante : [http://bluemix.net ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](http://bluemix.net){:new_window}.
    
	Une fois que vous êtes connecté avec votre ID utilisateur et votre mot de passe, l'interface utilisateur {{site.data.keyword.Bluemix_notm}} s'ouvre.

2. Dans le menu, sélectionnez **Tableau de bord**.

3. Dans la section *Clusters*, sélectionnez le cluster.

4. Dans la section *Vue d'ensemble*, sélectionnez **Afficher les journaux**.

    Kibana s'ouvre.




##  Accès à Kibana depuis le tableau de bord d'un conteneur qui est déployé dans l'infrastructure gérée par {{site.data.keyword.Bluemix_notm}} (déprécié)
{: #launch_Kibana_for_containers}

Cette méthode s'applique uniquement aux conteneurs qui sont déployés dans l'infrastructure gérée par {{site.data.keyword.Bluemix_notm}}.

La requête qui est utilisée pour filtrer les données qui sont affichées dans Kibana extrait les entrées de journal pour le conteneur depuis lequel vous lancez Kibana.

Pour afficher les journaux d'un conteneur Docker dans Kibana, procédez comme suit :

1. Connectez-vous à {{site.data.keyword.Bluemix_notm}}, puis cliquez sur le conteneur depuis le tableau de bord {{site.data.keyword.Bluemix_notm}}. 
    
2. Ouvrez l'onglet des journaux dans l'interface utilisateur {{site.data.keyword.Bluemix_notm}}.

    Pour les conteneurs qui sont déployés dans l'infrastructure gérée par {{site.data.keyword.IBM_notm}}, sélectionnez **Surveillance et journaux** dans la barre de navigation, puis cliquez sur l'onglet **Journalisation**. 
    
    L'onglet des journaux s'affiche.  

3. Cliquez sur **Advanced view**. Le tableau de bord Kibana s'ouvre.

    Par défaut, la page **Discover** est chargée avec le canevas d'index par défaut et un filtre temporel est défini sur les 30 dernières secondes. La
requête de recherche est définie pour porter sur toutes les entrées du conteneur Docker.

    Si la page Discover n'affiche aucune entrée de journal, ajustez le sélecteur de période. Pour plus d'informations, voir [Définition d'un filtre temporel](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter).

	



