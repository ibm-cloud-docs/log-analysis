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

# Sécurité
{: #security_ov}

Pour contrôler les actions {{site.data.keyword.loganalysisshort}} qu'un utilisateur peut effectuer, vous pouvez affecter un ou plusieurs rôles à un utilisateur.
s 
{:shortdesc}

Pour utiliser l'API de service {{site.data.keyword.loganalysisshort}}, vous devez utiliser un jeton UAA ou un jeton IAM. Pour pouvoir envoyer des journaux au service {{site.data.keyword.loganalysisshort}}, vous avez besoin d'un jeton de journalisation.


## Modèles d'authentification
{: #auth1}

Pour pouvoir utiliser le service {{site.data.keyword.loganalysisshort}} via l'interface de ligne de commande ou l'API, vous avez besoin d'un jeton d'authentification.

Le service {{site.data.keyword.loganalysisshort}} prend en charge les modèles d'authentification suivants :

* [Authentification UAA](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa)

    Vous pouvez utiliser l'interface de ligne de commande pour gérer les jetons UAA.
	
* [Authentification IAM](/docs/services/CloudLogAnalysis/security/auth_iam.html#auth_iam1)

    Le modèle d'authentification IAM offre des fonctions d'interface utilisateur, d'interface de ligne de commande ou de gestion d'API. 

**Remarque :** les jetons UAA et IAM arrivent à expiration au bout d'un certain temps. 

## Rôles
{: #roles3}

Dans {{site.data.keyword.Bluemix_notm}}, il existe deux types de rôle qui contrôlent les actions que les utilisateurs peuvent effectuer lorsqu'ils utilisent le service {{site.data.keyword.loganalysisshort}} :

* Rôles Cloud Foundry (CF) : vous contrôlez les actions {{site.data.keyword.loganalysisshort}} qu'un utilisateur peut effectuer en affectant un ou plusieurs rôles CF. Avec ces rôles, vous contrôlez les droits qui permettent à l'utilisateur d'afficher et de gérer les journaux dans un espace ou une organisation.
* Rôles IAM : vous contrôlez les actions {{site.data.keyword.loganalysisshort}} qu'un utilisateur peut effectuer en affectant un ou plusieurs rôles IAM. Avec ces rôles, vous contrôlez les droits qui permettent à l'utilisateur d'afficher et de gérer les journaux de compte. 


Le tableau suivant répertorie les types de rôle et le domaine dans {{site.data.keyword.Bluemix_notm}} qu'ils contrôlent :

<table>
  <caption>Tableau 1. Type de rôles contrôlant les actions par domaine</caption>
  <tr>
    <th></th>
	<th align="right">Compte</th>
    <th align="right">Organisation</th>
    <th align="right">Espace</th>	
  </tr>
  <tr>
    <td align="left">Rôles CF</td>
	<td align="center">Non</td>
	<td align="center">Oui</td>
	<td align="center">Oui</td>
  </tr>
  <tr>
    <td align="left">Rôles IAM</td>
	<td align="center">Oui</td>
	<td align="center">Non</td>
	<td align="center">Non</td>
  </tr>
</table>


## Rôles CF
{: #bmx_roles}

Le tableau suivant répertorie les privilèges de chaque rôle CF permettant d'utiliser le service {{site.data.keyword.loganalysisshort}} :

<table>
  <caption>Tableau 2. Rôle et privilèges Cloud Foundry permettant d'utiliser le service {{site.data.keyword.loganalysisshort}}</caption>
  <tr>
    <th>Rôle</th>
	<th>Domaine</th>
	<th>Privilèges d'accès</th>
  </tr>
  <tr>
    <td>Responsable</td>
	<td>Organisation <br>Espace</td>
	<td>Toutes les API RESTful</td>
  </tr>
  <tr>
    <td>Développeur</td>
	<td>Espace</td>
	<td>Toutes les API RESTful</td>
  </tr>
  <tr>
    <td>Auditeur</td>
	<td>Organisation <br>Espace</td>
	<td>Seules les API RESTful qui effectuent des opérations en lecture seule, comme interroger des journaux.</td>
  </tr>
</table>


## Rôles IAM
{: #iam_roles}

Le tableau suivant répertorie les privilèges de chaque rôle IAM permettant d'utiliser le service {{site.data.keyword.loganalysisshort}} :

<table>
  <caption>Tableau 3. Rôles et privilèges IAM permettant d'utiliser le service {{site.data.keyword.loganalysisshort}}</caption>
  <tr>
    <th>Rôle</th>
	<th>Privilèges</th>
  </tr>
  <tr>
    <td>Administrateur</td>
	  <td>Afficher des informations sur les journaux dans un espace ou au niveau du compte. <br>Télécharger les journaux dans un fichier local ou diriger les journaux vers un autre programme tel qu'Elastic Stack. <br>Affiche la durée de conservation des journaux qui sont disponibles dans un espace ou un compte. <br>Met à jour la durée de conservation des journaux qui sont disponibles dans un espace ou un compte. <br>Affiche la liste des sessions actives et leurs ID. <br>Créer une session que vous pouvez utiliser pour télécharger des journaux. <br>Supprimer une session, spécifiée par l'ID de session. <br>Affiche le statut d'une session unique. <br>Supprimer les journaux. </td>
  </tr>
  <tr>
    <td>Editeur</td>
	  <td>Afficher des informations sur les journaux dans un espace ou au niveau du compte. <br>Télécharger les journaux dans un fichier local ou diriger les journaux vers un autre programme tel qu'Elastic Stack. <br>Affiche la durée de conservation des journaux qui sont disponibles dans un espace ou un compte. <br>Met à jour la durée de conservation des journaux qui sont disponibles dans un espace ou un compte. <br>Affiche la liste des sessions actives et leurs ID. <br>Créer une session que vous pouvez utiliser pour télécharger des journaux. <br>Supprimer une session, spécifiée par l'ID de session. <br>Affiche le statut d'une session unique. <br>Supprimer les journaux.  </td>
  </tr>
  <tr>
    <td>Opérateur</td>
	  <td>Afficher des informations sur les journaux dans un espace ou au niveau du compte. <br>Affiche la durée de conservation des journaux qui sont disponibles dans un espace ou un compte. <br>Affiche la liste des sessions actives et leurs ID. <br>Affiche le statut d'une session unique. <br>Télécharger les journaux dans un fichier local ou diriger les journaux vers un autre programme tel qu'Elastic Stack.  <br>Créer une session que vous pouvez utiliser pour télécharger des journaux. <br>Supprimer une session, spécifiée par l'ID de session. </td>
  </tr>
  <tr>
    <td>Afficheur</td>
	  <td>Afficher des informations sur les journaux dans un espace ou au niveau du compte. <br>Affiche la durée de conservation des journaux qui sont disponibles dans un espace ou un compte. <br>Affiche la liste des sessions actives et leurs ID. <br>Affiche le statut d'une session unique. </td>
  </tr>
</table>

Le tableau ci-dessous répertorie la relation entre l'API, une action de service et un rôle IAM qui est utilisé par le service {{site.data.keyword.loganalysisshort}}.

<table>
  <caption>Tableau 4. Relation entre l'API, une action de service et un rôle IAM </caption>
  <tr>
    <th>API</th>
	<th>Action</th>
	<th>Rôle IAM</th>
	<th>Description</th>
  </tr>
  <tr>
    <td>DELETE /v1/logging/logs</td>
    <td>ibmcloud-log-analysis.domain.log_delete</td>
	<td>Administrateur, Editeur</td>
	<td>Supprimer les journaux.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs</td>
    <td>ibmcloud-log-analysis.domain.log_read</td>
	<td>Administrateur, Editeur, Afficheur</td>
	<td>Afficher des informations sur les journaux dans un espace {{site.data.keyword.Bluemix_notm}} ou au niveau du compte.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs/download</td>
    <td>ibmcloud-log-analysis.domain.log_download</td>
	<td>Administrateur, Editeur</td>
	<td>Télécharger les journaux dans un fichier local ou diriger les journaux vers un autre programme tel qu'Elastic Stack.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs/retention</td>
    <td>ibmcloud-log-analysis.domain.policy_read</td>
    <td>Administrateur, Editeur, Afficheur</td>
    <td>Affiche la durée de conservation des journaux qui sont disponibles dans un espace {{site.data.keyword.Bluemix_notm}} ou un compte.</td>
  </tr>
  <tr>
    <td>PUT /v1/logging/logs/retention</td>
    <td>ibmcloud-log-analysis.domain.policy_write</td>
    <td>Administrateur, Editeur</td>
    <td>Met à jour la durée de conservation des journaux qui sont disponibles dans un espace {{site.data.keyword.Bluemix_notm}} ou un compte.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/sessions</td>
    <td>ibmcloud-log-analysis.domain.session_read</td>
    <td>Administrateur, Editeur, Afficheur</td>
    <td>Affiche la liste des sessions actives et leurs ID.</td>
  </tr>
  <tr>
    <td>POST /v1/logging/sessions</td>
    <td>ibmcloud-log-analysis.domain.session_write</td>
    <td>Administrateur, Editeur</td>
    <td>Créer une session que vous pouvez utiliser pour télécharger des journaux.</td>
  </tr>
  <tr>
    <td>DELETE /v1/logging/sessions/{id}</td>
    <td>ibmcloud-log-analysis.domain.session_delete</td>
    <td>Administrateur, Editeur</td>
    <td>Supprimer une session, spécifiée par l'ID de session.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/sessions/{id}</td>
    <td>ibmcloud-log-analysis.domain.session_read</td>
    <td>Administrateur, Editeur, Afficheur</td>
    <td>Affiche le statut d'une session unique.</td>
  </tr>
</table>

## Obtention d'un jeton d'authentification pour gérer les journaux à l'aide de l'API
{: #get_token}

Pour gérer les journaux à l'aide de l'API {{site.data.keyword.loganalysisshort}}, vous devez utiliser un jeton d'authentification. 

**Utilisation des journaux qui sont disponibles dans le domaine d'espace**

* Utilisez l'interface de ligne de commande {{site.data.keyword.loganalysisshort}} pour obtenir le jeton UAA. 
* Le jeton possède un délai d'expiration. 

Pour plus d'informations, voir [Obtention du jeton UAA](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa).

**Utilisation des journaux qui sont disponibles dans le domaine de compte**

* Utilisez l'interface de ligne de commande {{{site.data.keyword.Bluemix_notm}} pour obtenir le jeton IAM. 
* Le jeton possède un délai d'expiration. 

Pour plus d'informations, voir [Obtention du jeton IAM](/docs/services/CloudLogAnalysis/security/auth_iam.html#auth_iam1).


## Obtention du jeton de journalisation pour envoyer des journaux à Log Analysis
{: #get_logging_token}

Pour pouvoir envoyer des journaux au service {{site.data.keyword.loganalysisshort}}, vous avez besoin d'un jeton de journalisation. 

Pour envoyer des journaux dans un domaine d'espace, choisissez l'une des méthodes suivantes :

* [Obtention du jeton de journalisation pour envoyer des journaux dans un espace à l'aide de la commande {{site.data.keyword.Bluemix_notm}} ibmcloud service](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_cloud_cli)
* [Obtention du jeton de journalisation pour envoyer des journaux dans un espace via l'interface de ligne de commande Log Analysis](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_la_cloud_cli)
* [Obtention du jeton de journalisation pour envoyer des journaux dans un espace via l'API Log Analysis](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_api)


## Octroi de droits à un utilisateur pour l'utilisation des journaux
{: #grant_permissions1}

Pour qu'un utilisateur puisse gérer les journaux ou les afficher, il doit disposer de droits dans {{site.data.keyword.Bluemix_notm}} permettant d'utiliser le service {{site.data.keyword.loganalysisshort}}.

* Pour des informations sur les droits requis pour gérer les journaux, voir [Rôles requis par un utilisateur pour gérer les journaux](/docs/services/CloudLogAnalysis/manage_logs.html#roles1).
* Pour des informations sur les droits requis pour afficher les journaux, voir [Rôles requis par un utilisateur pour afficher les journaux](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#roles).

Pour plus d'informations sur l'octroi de droits, voir :

* [Affectation d'une règle IAM à un utilisateur dans l'interface utilisateur {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions).
* [Affectation d'une règle IAM à un utilisateur via la ligne de commande](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_commandline).
* [Octroi à un utilisateur des droits permettant d'afficher les journaux d'espace dans l'interface utilisateur {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space).


