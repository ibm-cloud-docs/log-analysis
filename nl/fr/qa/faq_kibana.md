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


# Foire aux questions concernant Kibana
{: #faq_kibana}

Ci-après figurent des réponses aux questions fréquentes concernant l'utilisation des fonctions de journalisation de {{site.data.keyword.Bluemix}}. {:shortdesc}

* [Comment procéder si je ne vois pas de données dans la page Discover de Kibana ?](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#logging_qa_no_data_discover_kibana)
* [Que faire en cas de renvoi d'une exception d'authentification ?](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#logging_qa_no_data_dashboard_kibana)
* [Pourquoi le symbole ? s'affiche-t-il en regard de zones dans la page Kibana Discover ?](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#logging_qa_kibana_question)
* [Une erreur 403 s'affiche lorsque j'essaie de modifier le canevas d'index par défaut](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#error_403)
* [L'URL abrégée ne fonctionne pas](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#short_url)
* [Puis-je effectuer des recherches dans mes journaux de compte dans Bluemix ?](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#acc_logs_1)


## Comment procéder si je ne vois pas de données dans la page Discover de Kibana ?
{: #logging_qa_no_data_discover_kibana}

Il se peut qu'aucune donnée ne s'affiche dans Kibana dans différentes situations :

1. Lorsque vous lancez Kibana, aucune donnée ne s'affiche dans la page Discover. Vous recevez alors le message suivant : **No results found.**. 
2. Vous vous trouvez dans la page Discover dans Kibana. Toutefois, après un bref délai, vous recevez le message : **No results found.** lorsque vous essayez d'effectuer une tâche dans Kibana.

Pour résoudre ce problème, procédez comme suit :

1. Vérifiez le *sélecteur de période* configuré dans la page Discover et rallongez la période. 

    **Remarque** : par défaut dans {{site.data.keyword.Bluemix_notm}}, le *sélecteur de période* est configuré pour afficher les données des 15 dernières minutes.

    Pour plus d'informations sur la configuration du *sélecteur de période*, voir [Définition d'un sélecteur de période](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter1).
       
2. Cliquez sur la loupe située dans la barre de recherche de la page *Discover*. Les données de la page sont actualisées en fonction de la requête de recherche par défaut.

    Vous pouvez également définir une période d'*actualisation automatique*.

    **Remarque** : par défaut dans {{site.data.keyword.Bluemix_notm}}, la période d'*actualisation automatique* est **désactivée**.
    
    Pour plus d'informations sur son activation, voir [Actualisation automatique des données](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_refresh_interval).



## Que faire en cas de renvoi d'une exception d'authentification ?
{: #logging_qa_no_data_dashboard_kibana}

Lorsqu'aucune donnée ne s'affiche dans vos visualisations dans une page du tableau de bord et que vous rencontrez le message d'erreur : **Error: Authorization Exception.**, vérifiez que vous disposez des droits permettant d'afficher les données dans chaque visualisation.

Prenez en compte les informations suivantes : vous pouvez configurer une ou plusieurs visualisations dans une page du tableau de bord. Lorsque la page du tableau de bord demande de collecter les données affichées via ces visualisations, une seule demande est émise pour toutes les visualisations. Si vous n'êtes pas autorisé à examiner les données de l'une de ces visualisations, la demande complète échoue.

Pour résoudre ce problème, procédez comme suit :

1. Identifiez les visualisations pour lesquelles vous ne disposez pas des droits appropriés.

    1. Cliquez sur l'icône représentant un *crayon* d'une visualisation dans la page *Tableau de bord*. La visualisation s'ouvre dans la page *Visualize*. Vous pouvez aussi charger une visualisation dans la page *Visualize*. 
    2. Vérifiez que vous pouvez voir des données.
    
    Répétez ces étapes pour chaque visualisation.

2. Demandez à votre administrateur de cloud de vous accorder l'accès aux données de ces visualisations.

3. Créez une page de tableau de bord excluant les visualisations à l'origine du problème, pour lesquelles vous ne disposez pas de l'accès permettant d'afficher les données. 

    Si vous partagez le tableau de bord, ne supprimez pas de visualisation car cette opération affecterait d'autres membres de l'équipe qui utilisent le même tableau de bord.



## Pourquoi le symbole ? s'affiche-t-il dans la page Kibana Discover ?
{: #logging_qa_kibana_question}

Lorsque vous ouvrez la page Discover dans Kibana, un point d'interrogation (`?`) peut être affiché en regard de zones répertoriées comme disponibles au lieu du caractère `t`. Lorsque vous rechargez la liste des zones, le type des zones est analysé et le point d'interrogation `?` est remplacé par le caractère `t`. Pour plus d'informations, voir [Rechargement de la liste de zones](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_reload_fields).


## Une erreur 403 s'affiche lorsque j'essaie de modifier le canevas d'index par défaut
{: #error_403}

Le canevas d'index par défaut ne peut pas être modifié. 

Si vous essayez de définir un autre canevas d'index comme nouveau canevas par défaut, l'erreur suivante s'affiche : `Config: Error 403 Forbidden`

## L'URL abrégée ne fonctionne pas
{: #short_url}

Le partage d'une recherche, d'une visualisation ou d'un tableau de bord n'est pas pris en charge. Par conséquent, les URL abrégées pour un objet Kibana que vous voulez partager ne fonctionnent pas non plus. 

## Puis-je effectuer des recherches dans mes journaux de compte dans Bluemix ?
{: #acc_logs_1}

En tant que propriétaire de compte, vous pouvez effectuer des recherches dans vos journaux de compte et les analyser.

Procédez comme suit pour afficher vos journaux de compte :

1. [Lancez Kibana.](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser) Par exemple, pour la région Sud des Etats-Unis, utilisez l'URL `https://logging.ng.bluemix.net`,

2. Sélectionnez l'option **View AccountName account Logs** pour afficher les journaux de compte. *AccountName* est le nom du compte.

