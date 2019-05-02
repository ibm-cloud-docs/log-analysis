---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-07"

keywords: LogDNA, IBM, Log Analysis, logging, getting started

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

# Tutoriel d'initiation
{: #getting-started}

Utilisez {{site.data.keyword.la_full}} pour ajouter des fonctionnalités de gestion des journaux à votre architecture {{site.data.keyword.cloud_notm}}. {{site.data.keyword.la_full_notm}} est exploité par LogDNA en partenariat avec {{site.data.keyword.IBM_notm}}.
{:shortdesc}


## Etape 1. Avant de commencer
{: #getting-started_prereqs}

* Documentez-vous sur {{site.data.keyword.la_full_notm}}. Pour plus d'informations, voir [About {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).
* Vérifiez les régions où le service est disponible. Pour plus d'informations, voir
[Régions](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_regions).
* Procurez-vous un ID utilisateur qui est membre ou propriétaire d'un compte {{site.data.keyword.cloud_notm}}. 

    Pour obtenir un ID utilisateur {{site.data.keyword.cloud_notm}}, cliquez sur [Inscription ![Icône de lien externe](../../icons/launch-glyph.svg "Icône de lien externe")](https://cloud.ibm.com/login){:new_window}.



## Etape 2. Mise en route
{: #getting-started_step2}

Sélectionnez une ressource de cloud dont vous voulez gérer les journaux. Ensuite, configurez cette source de journal de manière à pouvoir surveiller ses journaux via le service {{site.data.keyword.la_full_notm}}. La source de journal peut se trouver dans la région où vous mettez une instance {{site.data.keyword.la_full_notm}} à disposition ou dans une autre région.

Le tableau suivant répertorie les ressources de cloud que vous pouvez configurer pour stocker des journaux à l'aide du service {{site.data.keyword.la_full_notm}}. Suivez le tutoriel pour démarrer le service {{site.data.keyword.loganalysisshort}} pour une ressource :

<table>
  <caption>Tutoriels d'initiation à l'utilisation du service {{site.data.keyword.la_full_notm}} </caption>
  <tr>
    <th>Ressource</th>
    <th>Tutoriel</th>
    <th>Environnement</th>
    <th>Scénario</th>
  </tr>
  <tr>
    <td>Conteneurs s'exécutant sur {{site.data.keyword.containershort}}</td>
    <td>[Gestion des journaux de cluster Kubernetes avec {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-kube#kube)</td>
    <td>{{site.data.keyword.cloud_notm}} public </td>
    <td>![{{site.data.keyword.containershort}} et {{site.data.keyword.la_full_notm}}](images/kube.png "{{site.data.keyword.containershort}} et {{site.data.keyword.la_full_notm}}")</td>
  </tr>
  <tr>
    <td>Linux Ubuntu, Linux Debian</td>
    <td>[Gestion des journaux Linux Ubuntu avec {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-ubuntu#ubuntu)</td>
    <td>Sur site</td>
    <td>![serveur Ubuntu et {{site.data.keyword.la_full_notm}}](images/ubuntu.png "Serveur Ubuntu et {{site.data.keyword.la_full_notm}}")</td>
  </tr>
</table>



## Etape 3. Mise à niveau du plan
{: #getting-started_step3}

Activez d'autres fonctions de journalisation.

Mettez à niveau le plan de service {{site.data.keyword.la_full_notm}} vers un plan payant pour pouvoir [filtrer les journaux](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5), [effectuer des recherches dans les journaux](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6), [définir des vues](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7) et [configurer des alertes](https://docs.logdna.com/docs/alerts). Pour plus d'informations sur les plans de service {{site.data.keyword.la_full_notm}}, voir [Plans de tarification](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

## Etape 4. Etapes suivantes 
{: #getting-started_iam}

Ensuite, gérez les accès utilisateur avec IAM.

Identifiez les règles IAM nécessaires à un utilisateur pour utiliser le service {{site.data.keyword.la_full_notm}}.

Pour en savoir plus sur l'intégration d'IAM au service {{site.data.keyword.la_full_notm}}, voir [Gestion des accès utilisateur à l'aide d'IAM](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#iam).

Par exemple, sélectionnez un rôle utilisateur pour savoir comment accorder à cet utilisateur des droits lui permettant d'utiliser le service {{site.data.keyword.la_full_notm}}. 

| Rôle utilisateur dans {{site.data.keyword.cloud_notm}} | Pour plus d'informations                     |
|-----------------------------------------------------|------------------------------------------|
| Propriétaire de compte                                       | [Octroi à un utilisateur du droit d'administrateur du service dans le compte {{site.data.keyword.cloud_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account) |
| Administrateur de service de plateforme dans le compte       | [Octroi à un utilisateur du droit d'administrateur du service dans le compte {{site.data.keyword.cloud_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account) |
| Administrateur de service de plateforme dans un groupe de ressources  | [Octroi à un utilisateur du droit d'administrateur du service dans un groupe de ressources](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_rg) |
| Opérateur DevOps de plateforme dans le compte           | [Octroi à un utilisateur DevOps du droit de gérer le service dans le compte {{site.data.keyword.cloud_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#devops_account) |
| Opérateur DevOps de plateforme dans un groupe de ressources        | [Octroi à un utilisateur DevOps du droit de gérer le service dans un groupe de ressources](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#devops_rg) |
| Administrateur de service dans LogDNA                     | [Octroi du droit de gérer des journaux et de configurer des alertes dans LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna)              |
| Utilisateur/Développeur                                    | [Octroi à un utilisateur du droit d'afficher et de gérer des journaux dans LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna)               |
{: caption="Tableau 2. Rôles cloud dans {{site.data.keyword.cloud_notm}}" caption-side="top"}


