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

# Accès aux journaux d'une application Cloud Foundry
{: #launch_logs_cloud_ui_cf}

Dans l'interface utilisateur {{site.data.keyword.Bluemix}}, vous pouvez afficher, filtrer et analyser des journaux dans l'onglet des journaux qui est disponible pour chaque application Cloud Foundry ou via l'interface utilisateur du service {{site.data.keyword.loganalysisshort}}.
{:shortdesc}

Pour afficher les journaux de l'application CF, tenez compte des informations suivantes : 

<table>
  <caption>Informations sur les journaux de l'application CF dans {{site.data.keyword.Bluemix_notm}}</caption>
  <tr>
    <th>Options de l'interface utilisateur</th>
    <th>Information</th>
  </tr>
  <tr>
    <td>Onglet des journaux disponible via l'interface utilisateur de l'application CF </td>
    <td>Les journaux disponibles pour l'analyse incluent les données des dernières 24 heures.</td>
  </tr>
  <tr>
    <td>Tableau de bord {{site.data.keyword.loganalysisshort}} (Kibana)</td>
    <td>Les journaux disponibles pour l'analyse incluent les données des trois derniers jours. Vous pouvez également indiquer une période personnalisée.</td>
  </tr>
</table>


## Accès aux journaux de l'application CF via le tableau de bord de l'application CF 
{: #cfapp_ui}

Pour consulter les journaux de déploiement ou d'exécution d'une application Cloud Foundry, procédez comme suit :

1. Dans le tableau de bord Applications, cliquez sur le nom de votre application Cloud Foundry. 
    
2. Dans la page des informations d'application détaillées, cliquez sur **Journaux**.
    
    Depuis l'onglet **Journaux**, vous pouvez afficher les journaux récents de votre application ou suivre des journaux en temps réel. De plus, vous pouvez filtrer les journaux par composant (type de journal), par ID d'instance d'application et par erreur.
    
Par défaut, les journaux disponibles pour l'analyse depuis la console {{site.data.keyword.Bluemix_notm}} sont ceux des dernières 24 heures.


## Accès aux journaux de l'application CF via l'interface utilisateur {{site.data.keyword.loganalysisshort}} 
{: #cfapp_la}

Pour consulter les journaux de déploiement ou d'exécution d'une application Cloud Foundry, procédez comme suit :

1. Dans le tableau de bord Applications, cliquez sur le nom de votre application Cloud Foundry. 
    
2. Dans la page des informations d'application détaillées, cliquez sur **Journaux**.
    
3. Cliquez sur **Afficher dans Kibana**.

Par défaut, les journaux disponibles pour l'analyse incluent les données des 15 dernières minutes.

**Conseil :** pour analyser des données pour une période personnalisée, voir [Analyse de journal avancée avec Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analyzing_logs_Kibana#analyzing_logs_Kibana). 


