---

copyright:
  years:  2018, 2019
lastupdated: "2019-05-01"

keywords: LogDNA, IBM, Log Analysis, logging, iam, manage user access

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

 
# Gestion des accès utilisateur à l'aide d'IAM
{: #iam}

{{site.data.keyword.iamlong}} (IAM) vous permet d'authentifier de manière sécurisée les utilisateurs et de contrôler de manière cohérente l'accès à toutes les ressources de cloud dans {{site.data.keyword.cloud_notm}}. 
{:shortdesc}

**Une règle d'accès avec un rôle utilisateur IAM doit être affectée à chaque utilisateur disposant d'un accès au service {{site.data.keyword.la_full_notm}}.** La règle détermine les actions que l'utilisateur peut exécuter dans le contexte du service ou de l'instance que vous sélectionnez. Les actions autorisées sont personnalisées et définies en tant qu'opérations pouvant être effectuées sur le service. Les actions sont ensuite mappées à des rôles utilisateur IAM.

Les *règles* activent l'accès à accorder à différents niveaux. Certaines des options sont les suivantes : 

* Accès à tous les services activés par IAM dans votre compte
* Accès à toutes les instances du service dans une seule région dans votre compte
* Accès à une instance de service individuelle de votre compte
* Accès à toutes les instances du service dans le contexte d'un groupe de ressources
* Accès à toutes les instances du service dans une seule région dans le contexte d'un groupe de ressources
* Accès à tous les services activés par IAM dans le contexte d'un groupe de ressources

Les *rôles* définissent les actions qu'un utilisateur ou un ID de service peut exécuter. Il existe différents types de rôle dans {{site.data.keyword.cloud_notm}} :

* Les *rôles de gestion de plateformes* qui permettent aux utilisateurs d'effectuer des tâches sur des ressources de service au niveau de la plateforme, par exemple affecter des accès utilisateur au service, créer ou supprimer des ID de service, créer des instances, affecter à d'autres utilisateurs des règles concernant votre service et lier des instances à des applications.
* Les *rôles d'accès au service* qui permettent d'affecter à des utilisateurs différents niveaux de droits pour l'appel de l'API du service.

**Pour organiser un ensemble d'utilisateurs et d'ID de service en une même entité afin de faciliter la gestion des droits IAM, utilisez des *groupes d'accès*.** Vous pouvez affecter une seule règle au groupe au lieu d'affecter individuellement le même accès plusieurs fois pour chaque utilisateur ou ID de service.
{: tip}


## Gestion des accès à l'aide de groupes d'accès
{: #groups}

Pour gérer les droits d'accès ou en accorder de nouveaux à des utilisateurs en utilisant des groupes d'accès, vous devez être le propriétaire du compte, l'administrateur ou l'éditeur de tous les services activés avec IAM dans le compte ou l'administrateur ou éditeur désigné pour le service Groupes d'accès IAM. 

Sélectionnez l'une des actions suivantes pour gérer les groupes d'accès dans {{site.data.keyword.cloud_notm}}:

* [Création d'un groupe d'accès](/docs/iam?topic=iam-groups#create_ag).
* [Affectation d'accès à un groupe](/docs/iam?topic=iam-groups#access_ag).


## Gestion des accès par affectation de règles directement aux utilisateurs
{: #users}

Pour gérer les droits d'accès ou en accorder de nouveaux à des utilisateurs en utilisant des règles IAM, vous devez être le propriétaire du compte, l'administrateur de tous les services du compte ou l'administrateur affecté au service ou à l'instance de service spécifique. 

Sélectionnez l'une des actions suivantes pour gérer les règles IAM dans {{site.data.keyword.cloud_notm}} :

* Pour modifier les droits d'un utilisateur, voir [Edition d'accès existants](/docs/iam?topic=iam-iammanidaccser#edit_existing).
* Pour accorder des droits à un utilisateur, voir [Affectation de nouveaux accès](/docs/iam?topic=iam-iammanidaccser#assign_new_access).
* Pour révoquer des droits, voir [Retrait d'accès](/docs/iam?topic=iam-iammanidaccser#removing_access).
* Pour réviser les droits d'un utilisateur, voir [Révision des accès affectés](/docs/iam?topic=iam-iammanidaccser#review_your_access).




## Rôles de plateforme {{site.data.keyword.cloud_notm}}
{: #platform}

Le tableau suivant vous permet d'identifier le rôle de plateforme que vous pouvez accorder à un utilisateur dans {{site.data.keyword.cloud_notm}} pour exécuter les actions de plateforme suivantes :

| Action de plateforme                                                         | Rôles de plateforme {{site.data.keyword.cloud_notm}}    | 
|--------------------------------------------------------------------------|------------------------------------------------------|
| `Accorder à d'autres membres du compte un accès leur permettant d'utiliser le service`            | Administrateur                                        | 
| `Mettre à disposition une instance de service`                                           | Editeur                            | 
| `Supprimer une instance de service`                                              | Administrateur </br>Editeur                            | 
| `Créer un service ID`                                                    | Administrateur </br>Editeur                            |
| `Afficher les détails d'une instance de service`                                     | Administrateur </br>Editeur </br>Opérateur </br>Afficheur  | 
| `Afficher des instances de service dans le tableau de bord de journalisation d'observabilité`          | Administrateur </br>Editeur </br>Opérateur </br>Afficheur  | 
| `Afficher la clé d'ingestion sur la console {{site.data.keyword.cloud_notm}}` | Administrateur                                        | 
{: caption="Tableau 1. Actions et rôles utilisateur IAM" caption-side="top"}



## Rôles de service {{site.data.keyword.cloud_notm}}
{: #service}

Utilisez le tableau suivant pour identifier le rôle de service que vous pouvez accorder à un utilisateur pour exécuter les actions de service suivantes :

| Actions                                                                 | Rôles de service {{site.data.keyword.cloud_notm}}     | 
|-------------------------------------------------------------------------|------------------------------------------------------|
| `Ajouter des sources de journal LogDNA`                                                | Responsable                                              |
| `Gérer des clés d'ingestion via l'interface utilisateur Web LogDNA`                       | Responsable                                              |
| `Gérer des clés de service`                                                   | Responsable                                              |
| `Archiver des journaux`                                                          | Responsable                                              |
| `Gérer l'analyse syntaxique`                                                        | Responsable                                              |
| `Configurer des alertes`                                                      | Responsable </br>Auteur </br>Lecteur                      | 
| `Filtrer et effectuer des recherche dans des données de journal`                                            | Responsable </br>Auteur </br>Lecteur                      |
| `Créer des vues`                                                          | Responsable </br>Auteur </br>Lecteur                      |
| `Gérer des vues`                                                          | Responsable </br>Auteur </br>Lecteur                      |
| `Exporter des données de journal`                                                       | Responsable </br>Auteur </br>Lecteur                      |
| `Configurer des préférences utilisateur dans l'interface utilisateur Web LogDNA`                       | Responsable </br>Auteur </br>Lecteur                      |
| `Afficher les journaux via l'interface utilisateur Web LogDNA`                                   | Responsable </br>Auteur </br>Lecteur                      | 
{: caption="Tableau 2. Actions et rôles utilisateur IAM" caption-side="top"}


**Remarque :** le rôle de service **responsable** est automatiquement associé au rôle d'administrateur LogDNA.






