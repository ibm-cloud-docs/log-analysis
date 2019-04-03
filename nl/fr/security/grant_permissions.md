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

# Octroi de droits permettant de gérer des journaux et d'afficher des journaux de compte
{: #grant_permissions}

Dans {{site.data.keyword.Bluemix}}, vous pouvez affecter un ou plusieurs rôles IAM à un utilisateur. Ces rôles définissent quelles tâches sont activées pour que cet utilisateur puisse utiliser le service {{site.data.keyword.loganalysisshort}}.  
{:shortdesc}

Par exemple, vous pouvez octroyer à un utilisateur le rôle **Opérateur** afin de lui permettre de gérer des journaux. Pour qu'un utilisateur puisse uniquement afficher des journaux de compte, vous pouvez lui octroyer le rôle **Afficheur**. Pour plus d'informations, voir [Rôles IAM](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-security_ov#iam_roles).

**Remarque :** 

* Pour accorder à un utilisateur des droits qui lui permettent de gérer des journaux ou d'afficher des journaux de compte, vous devez être autorisé à affecter des règles à d'autres utilisateurs dans le compte, ou vous devez être le propriétaire du compte. Si vous n'êtes pas le propriétaire du compte, vous devez disposer d'une règle IAM dotée du rôle Editeur, Opérateur ou Administrateur.
* Afin d'accorder des droits à un utilisateur pour qu'il puisse afficher les journaux dans un espace, vous devez disposer de droits dans l'organisation et l'espace qui permettent d'attribuer à l'utilisateur un rôle Cloud Foundry qui décrit les actions qu'il peut effectuer avec le service {{site.data.keyword.loganalysisshort}} dans cet espace. 

## Affectation d'une règle IAM à un utilisateur dans l'interface utilisateur {{site.data.keyword.Bluemix_notm}}
{: #grant_permissions_ui_account}

Pour accorder à un utilisateur des droits permettant d'utiliser le service {{site.data.keyword.loganalysisshort}}, procédez comme suit :

1. Connectez vous à la console {{site.data.keyword.Bluemix_notm}}.

    Ouvrez un navigateur Web et lancez le tableau de bord {{site.data.keyword.Bluemix_notm}} : [http://bluemix.net ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](http://bluemix.net){:new_window}
	
	Une fois que vous êtes connecté avec votre ID utilisateur et votre mot de passe, l'interface utilisateur {{site.data.keyword.Bluemix_notm}} s'ouvre.

2. Dans la barre de menus, cliquez sur **Gérer > Compte > Utilisateurs**. 

    La fenêtre *Utilisateurs* affiche une liste d'utilisateurs avec leur adresse électronique et leur statut sur le compte actuellement sélectionné.
	
3. Si l'utilisateur est membre du compte, sélectionnez le nom de l'utilisateur dans la liste ou cliquez sur **Gérer un utilisateur** dans le menu *Actions*.

    Si l'utilisateur n'est pas membre du compte, voir [Invitation d'utilisateurs](/docs/iam?topic=iam-iamuserinv#iamuserinv).

4. Dans la section **Règles d'accès**, cliquez sur **Affecter un accès**, puis cliquez sur **Affecter l'accès aux ressources**.

    La fenêtre *Affecter l'accès à la ressource à** s'ouvre.

5. Entrez les informations concernant la règle. Le tableau ci-dessous répertorie les zones requises pour définir une règle. 

    <table>
	  <caption>Liste des zones de configuration d'une règle IAM.</caption>
	  <tr>
	    <th>Zone</th>
		<th>Valeur</th>
	  </tr>
	  <tr>
	    <td>Services</td>
		<td>*IBM Cloud Log Analysis*</td>
	  </tr>	  
	  <tr>
	    <td>Régions</td>
		<td>Vous pouvez spécifier les régions dans lesquelles l'utilisateur disposera des droits permettant d'utiliser les journaux. Sélectionnez ou une plusieurs régions individuellement, ou sélectionnez **Toutes les régions en cours** pour accorder l'accès à toutes les régions.</td>
	  </tr>
	  <tr>
	    <td>Instance de service</td>
		<td>Sélectionnez *Toutes les instances de service*.</td>
	  </tr>
	  <tr>
	    <td>Rôles</td>
		<td>Sélectionnez un ou plusieurs rôles IAM. <br>Les rôles valides sont *administrateur*, *opérateur*, *éditeur* et *afficheur*. <br>Pour plus d'informations sur les actions autorisées pour chaque rôle, voir [Rôle IAM](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-security_ov#iam_roles).
		</td>
	  </tr>
     </table>
	
6. Cliquez sur **Affecter**.
	
La règle que vous configurez est applicable aux régions sélectionnées. 


## Affectation d'une règle IAM à un utilisateur via la ligne de commande
{: #grant_permissions_commandline}

Procédez comme suit pour accorder à un utilisateur le droit permettant d'afficher les journaux de compte via la ligne de commande :

1. A partir d'un terminal, connectez-vous au compte {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)

2. Vérifiez que l'utilisateur est membre du compte. Exécutez la commande suivante pour obtenir la liste des utilisateurs du compte :

    ```
	ibmcloud account users
	```
    {: codeblock}	

	La liste des utilisateurs avec leur identificateur global unique s'affiche.

3. Si l'utilisateur n'est pas membre du compte, contactez le propriétaire de compte et demandez une invitation autorisant l'utilisateur à accéder au compte. Pour plus d'informations, voir [Invitation d'utilisateurs](/docs/iam?topic=iam-iamuserinv#iamuserinv).

    **Astuce :** la commande permettant d'inviter un utilisateur à accéder à un compte est la suivante : `ibmcloud iam account-user-invite USER_EMAIL`
		
4. Affectez une règle à l'utilisateur. Exécutez la commande suivante :

    ```
    ibmcloud iam user-policy-create USER_NAME --roles ROLE --service-name ibmloganalysis
	```
	{: codeblock}

	où
    * USER_NAME est l'ID {{site.data.keyword.Bluemix_notm}} de l'utilisateur.
	* ROLE est un rôle IAM. Les valeurs admises sont : *administrator*, *operator*, *editor* et *viewer*

5. Vérifiez que la règle est affectée à l'utilisateur. Exécutez la commande suivante pour répertorier toutes les règles affectées à un utilisateur :

    ```
    ibmcloud iam user-policies USER_NAME
	```
	{: codeblock}




## Octroi à un utilisateur des droits permettant d'afficher les journaux d'espace dans l'interface utilisateur {{site.data.keyword.Bluemix_notm}}
{: #grant_permissions_ui_space}

Afin d'accorder des droits à un utilisateur pour qu'il puisse afficher les journaux dans un espace, vous devez lui attribuer un rôle Cloud Foundry qui décrit les actions qu'il peut effectuer avec le service {{site.data.keyword.loganalysisshort}} dans l'espace. 

Pour accorder à un utilisateur des droits permettant d'utiliser le service {{site.data.keyword.loganalysisshort}}, procédez comme suit :

1. Connectez vous à la console {{site.data.keyword.Bluemix_notm}}.

    Ouvrez un navigateur Web et lancez le tableau de bord {{site.data.keyword.Bluemix_notm}} : [http://bluemix.net ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](http://bluemix.net){:new_window}
	
	Une fois que vous êtes connecté avec votre ID utilisateur et votre mot de passe, l'interface utilisateur {{site.data.keyword.Bluemix_notm}} s'ouvre.

2. Dans la barre de menus, cliquez sur **Gérer > Compte > Utilisateurs**. 

    La fenêtre *Utilisateurs* affiche une liste d'utilisateurs avec leur adresse électronique et leur statut sur le compte actuellement sélectionné.
	
3. Si l'utilisateur est membre du compte, sélectionnez le nom de l'utilisateur dans la liste ou cliquez sur **Gérer un utilisateur** dans le menu *Actions*.

    Si l'utilisateur n'est pas membre du compte, voir [Invitation d'utilisateurs](/docs/iam?topic=iam-iamuserinv#iamuserinv).

4. Sélectionnez **Accès Cloud Foundry**, puis sélectionnez l'organisation.

    La liste des espaces disponibles dans cette organisation est affichée.

5. Choisissez un espace. Ensuite, dans le menu d'actions, sélectionnez **Editer un rôle d'espace**.

6. Sélectionnez un ou plusieurs rôles d'espace. Les rôles valides sont : *Responsable*, *Développeur* et *Auditeur*.
	
7. Cliquez sur **Sauvegarder le rôle**.




