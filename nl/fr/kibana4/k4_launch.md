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
{: #k4_launch}

Vous pouvez lancer Kibana depuis l'interface utilisateur {{site.data.keyword.Bluemix}} ou directement depuis un navigateur Web.
{:shortdesc}

Lancez Kibana depuis {{site.data.keyword.Bluemix_notm}} pour afficher et analyser des données en contexte sur la ressource à partir de laquelle vous lancez Kibana. Par exemple, vous pouvez ouvrir vos journaux d'application CK spécifiques dans Kibana,
dans le contexte de cette application spécifique.

Le tableau suivant recense les ressources et la méthode de navigation prise en charge pour lancer Kibana :

<table>
<caption>Tableau 1. Liste des ressources et des méthodes de navigation prises en charge </caption>
  <tr>
    <th>Ressource</th>
    <th>Accès au tableau de bord Kibana depuis le tableau de bord Bluemix</th>
    <th>Accès au tableau de bord Kibana depuis un navigateur Web</th>
  <tr>
  <tr>
    <td>Application CF</td>
    <td>Oui</td>
    <td>Oui</td>
  <tr>  
  <tr>
    <td>Conteneur déployé dans un cluster Kubernetes</td>
    <td>Oui</td>
    <td>Oui</td>
  <tr>  
</table>

Pour plus d'informations sur Kibana, reportez-vous au manuel [Kibana User Guide ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](https://www.elastic.co/guide/en/kibana/4.1/index.html){: new_window}.
    

##  Accès au tableau de bord Kibana depuis le tableau de bord Bluemix
{: #launch_Kibana_from_bluemix}

La requête utilisée pour filtrer les données affichées dans Kibana extrait les entrées de journal pour l'application CF ou le conteneur {{site.data.keyword.Bluemix_notm}} depuis laquelle ou lequel vous lancez Kibana.

Pour consulter les journaux d'une application Cloud Foundry ou d'un conteneur Docker dans Kibana, procédez comme suit :

1. Connectez-vous à {{site.data.keyword.Bluemix_notm}}, puis cliquez sur le nom de l'application ou le conteneur dans le tableau de bord {{site.data.keyword.Bluemix_notm}}. 
    
2. Ouvrez l'onglet des journaux dans l'interface utilisateur {{site.data.keyword.Bluemix_notm}}.

    * Pour les applications CF, cliquez sur **Journaux** dans la barre de navigation. 
    * Pour les conteneurs qui sont déployés dans l'infrastructure gérée par {{site.data.keyword.Bluemix_notm}}, sélectionnez **Surveillance et journaux** dans la barre de navigation, puis cliquez sur l'onglet **Journalisation**. 
    
        L'onglet Journaux s'affiche.  

3. Cliquez sur **Vue avancée**. Le tableau de bord Kibana s'ouvre.

    Par défaut, la page **Discover** est chargée avec le canevas d'index par défaut et un filtre temporel est défini pour les 30 dernières secondes. La requête de recherche est configurée pour rechercher toutes les entrées concernant votre application CF ou votre conteneur Docker.

    Si la page Discover n'affiche aucune entrée de journal, ajustez le sélecteur de période. 


##  Accès au tableau de bord Kibana depuis un navigateur Web
{: #launch_Kibana_from_browser1}

La requête utilisée pour filtrer les données affichées dans Kibana extrait les entrées de journal pour un espace dans l'organisation {{site.data.keyword.Bluemix_notm}}. Les informations de journal affichées par Kibana incluent des enregistrements pour toutes les ressources déployées dans l'espace de l'organisation {{site.data.keyword.Bluemix_notm}} à laquelle vous êtes connecté.

Procédez comme suit pour lancer Kibana depuis un navigateur :

1. Lancez l'interface utilisateur Kibana.
    
    Exemple 
      
        <table>
          <caption>Tableau 1. URL d'ouverture de Kibana  </caption>
           <tr>
            <th>Région</th>
            <th>URL</th>
          </tr>
          <tr>
            <td>Sud des Etats-Unis</td>
            <td>https://logging.ng.bluemix.net/ </td>
          </tr>
          <tr>
            <td>Royaume-Uni</td>
            <td>https://logging.eu-gb.bluemix.net/ </td>
          </tr>
        </table>

    Si la page Discover n'affiche aucune entrée de journal, ajustez le sélecteur de période. 

