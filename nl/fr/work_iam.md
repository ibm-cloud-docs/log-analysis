---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, IAM, security, logging, access groups

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

 
# Gestion des groupes d'accès et des règles IAM
{: #work_iam}

Vous pouvez utiliser {{site.data.keyword.iamlong}} (IAM) pour authentifier de manière sécurisée les utilisateurs et contrôler de manière cohérente l'accès à toutes les ressources de cloud dans {{site.data.keyword.cloud_notm}}. 
{:shortdesc}

Pour plus d'informations, voir [Gestion des accès utilisateur à l'aide d'IAM](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#iam).


## Octroi à un utilisateur du droit d'administrateur du service dans le compte {{site.data.keyword.cloud_notm}}
{: #admin_account}

Un **propriétaire de compte** ou un **administrateur du service {{site.data.keyword.la_full_notm}}** est autorisé à exécuter les actions suivantes : 

* Accorder à d'autres membres du compte un accès leur permettant d'utiliser le service
* Mettre à disposition une instance de service
* Supprimer une instance de service
* Afficher les détails d'une instance de service
* Créer un ID de service

Par conséquent, pour accorder à un utilisateur le rôle d'administrateur afin qu'il puisse gérer le service dans le compte, cet utilisateur doit disposer d'une règle IAM pour le service {{site.data.keyword.la_full_notm}} avec le rôle de plateforme **Administrateur**. Vous devez affecter à cet utilisateur un accès à une ressource individuelle du compte. 

Pour affecter à un utilisateur le rôle d'administrateur sur le service {{site.data.keyword.la_full_notm}} dans le compte, procédez comme suit : 

1. Dans la barre de menus, cliquez sur **Gérer** &gt; **Accès (IAM)** puis sélectionnez **Utilisateurs**.
2. Sur la ligne de l'utilisateur auquel vous voulez affecter un accès, sélectionnez le menu **Actions**, puis cliquez sur **Affecter un accès**.
3. Sélectionnez **Affecter l'accès aux ressources**.
4. Sélectionnez **IBM Log Analysis avec LogDNA**.
5. Sélectionnez **Toutes les régions en cours**.
6. Sélectionnez **Toutes les instances de service en cours**.
7. Sélectionnez le rôle de plateforme **Administrateur**.
8. Cliquez sur Affecter.


## Octroi à un utilisateur du droit d'administrateur du service dans un groupe de ressources
{: #admin_rg}

Un **administrateur du service {{site.data.keyword.la_full_notm}}** est autorisé à exécuter les actions suivantes : 

* Accorder à d'autres membres du compte un accès leur permettant d'utiliser le service
* Mettre à disposition une instance de service
* Supprimer une instance de service
* Afficher les détails d'une instance de service
* Créer un ID de service

Par conséquent, pour accorder à un utilisateur le rôle d'administrateur afin qu'il puisse gérer des instances dans un groupe de ressources du compte, cet utilisateur doit disposer d'une règle IAM pour le service {{site.data.keyword.la_full_notm}} avec le rôle de plateforme **Administrateur** dans le contexte du groupe de ressources. 

Pour affecter à un utilisateur le rôle d'administrateur sur le service {{site.data.keyword.la_full_notm}} dans le contexte d'un groupe de ressources, procédez comme suit : 

1. Dans la barre de menus, cliquez sur **Gérer** &gt; **Accès (IAM)** puis sélectionnez **Utilisateurs**.
2. Sur la ligne de l'utilisateur auquel vous voulez affecter un accès, sélectionnez le menu **Actions**, puis cliquez sur **Affecter un accès**.
3. Sélectionnez **Affecter l'accès au sein d'un groupe de ressources**.
4. Sélectionnez un groupe de ressources.
5. Si aucun rôle n'a encore été accordé à l'utilisateur pour le groupe de ressources concerné, sélectionnez un rôle pour la zone **Affecter l'accès à un groupe de ressources**. 

    En fonction du rôle sélectionné, l'utilisateur peut afficher le groupe de ressources sur son tableau de bord, modifier le nom du groupe de ressources ou gérer les accès utilisateur au groupe. 
    
    Vous pouvez sélectionner **Aucun accès** si vous voulez que l'utilisateur puisse uniquement accéder au service {{site.data.keyword.la_full_notm}} dans le groupe de ressources.

6. Sélectionnez **IBM Log Analysis avec LogDNA**.
7. Sélectionnez le rôle de plateforme **Administrateur**.
8. Cliquez sur **Affecter**.


## Octroi à un utilisateur DevOps du droit de gérer le service dans le compte {{site.data.keyword.cloud_notm}}
{: #devops_account}

Un **utilisateur DevOps** est autorisé à exécuter les actions suivantes : 

* Mettre à disposition une instance de service
* Supprimer une instance de service
* Afficher les détails d'une instance de service
* Créer un ID de service

Par conséquent, vous devez disposer d'une règle IAM pour le service {{site.data.keyword.la_full_notm}} avec le rôle de plateforme **Editeur**.

Pour affecter à un utilisateur le rôle d'éditeur sur le service {{site.data.keyword.la_full_notm}} dans le compte, procédez comme suit : 

1. Dans la barre de menus, cliquez sur **Gérer** &gt; **Accès (IAM)** puis sélectionnez **Utilisateurs**.
2. Sur la ligne de l'utilisateur auquel vous voulez affecter un accès, sélectionnez le menu **Actions**, puis cliquez sur **Affecter un accès**.
3. Sélectionnez **Affecter l'accès aux ressources**.
4. Sélectionnez **IBM Log Analysis avec LogDNA**.
5. Sélectionnez **Toutes les instances de service**.
6. Sélectionnez le rôle de plateforme **Editeur**.
7. Cliquez sur Affecter.

## Octroi à un utilisateur DevOps du droit de gérer une instance dans le compte {{site.data.keyword.cloud_notm}}
{: #devops_account_instance}

Pour affecter à un utilisateur le rôle d'éditeur sur une instance du service {{site.data.keyword.la_full_notm}} dans le compte, procédez comme suit : 

1. Dans la barre de menus, cliquez sur **Gérer** &gt; **Accès (IAM)** puis sélectionnez **Utilisateurs**.
2. Sur la ligne de l'utilisateur auquel vous voulez affecter un accès, sélectionnez le menu **Actions**, puis cliquez sur **Affecter un accès**.
3. Sélectionnez **Affecter l'accès aux ressources**.
4. Sélectionnez **IBM Log Analysis avec LogDNA**.
5. Sélectionnez l'instance.
6. Sélectionnez le rôle de plateforme **Editeur**.
7. Cliquez sur Affecter.



## Octroi à un utilisateur DevOps du droit de gérer le service dans un groupe de ressources
{: #devops_rg}

Un **utilisateur DevOps** est autorisé à exécuter les actions suivantes : 

* Mettre à disposition une instance de service
* Supprimer une instance de service
* Afficher les détails d'une instance de service
* Créer un ID de service

Par conséquent, vous devez disposer d'une règle IAM pour service {{site.data.keyword.la_full_notm}} avec le rôle de plateforme **éditeur**.

Pour affecter à un utilisateur le rôle d'éditeur sur le service {{site.data.keyword.la_full_notm}} dans le contexte d'un groupe de ressources, procédez comme suit : 

1. Dans la barre de menus, cliquez sur **Gérer** &gt; **Accès (IAM)** puis sélectionnez **Utilisateurs**.
2. Sur la ligne de l'utilisateur auquel vous voulez affecter un accès, sélectionnez le menu **Actions**, puis cliquez sur **Affecter un accès**.
3. Sélectionnez **Affecter l'accès au sein d'un groupe de ressources**.
4. Sélectionnez un groupe de ressources.
5. Si aucun rôle n'a encore été accordé à l'utilisateur pour le groupe de ressources concerné, sélectionnez un rôle pour la zone **Affecter l'accès à un groupe de ressources**. 

    En fonction du rôle sélectionné, l'utilisateur peut afficher le groupe de ressources sur son tableau de bord, modifier le nom du groupe de ressources ou gérer les accès utilisateur au groupe. 
    
    Vous pouvez sélectionner **Aucun accès** si vous voulez que l'utilisateur puisse uniquement accéder au service {{site.data.keyword.la_full_notm}} dans le groupe de ressources.

6. Sélectionnez **IBM Log Analysis avec LogDNA**.
7. Sélectionnez le rôle de plateforme **Editeur**.
8. Cliquez sur **Affecter**.

## Octroi du droit de gérer des journaux et de configurer des alertes dans LogDNA
{: #admin_user_logdna}

Un **utilisateur administrateur** dans LogDNA est autorisé à exécuter les actions suivantes : 

* Ajouter des sources de journal LogDNA
* Afficher les journaux
* Rechercher dans les journaux
* Filtrer les journaux
* Configurer des alertes

Par conséquent, vous devez disposer des règles suivantes :

* Une règle IAM pour le service {{site.data.keyword.la_full_notm}} avec le rôle de plateforme **Editeur**. Cette règle accorde le droit d'afficher les détails d'une instance de service via la ligne de commande et dans le tableau de bord {{site.data.keyword.cloud_notm}}.
* Une règle IAM pour le service {{site.data.keyword.la_full_notm}} avec le rôle de service **Responsable**. Cette règle accorde le droit de surveiller, filtrer et effectuer des recherche dans un journal et de définir des alertes via l'interface utilisateur Web de LogDNA.

**Remarque :** en tant qu'administrateur du service, lorsque vous affectez ces règles à un utilisateur, envisagez de le faire dans le contexte d'un groupe de ressources. Une instance {{site.data.keyword.la_full_notm}} est mise à disposition dans le contexte d'un groupe de ressources. Par conséquent, accordez les droits d'accès dans le contexte du groupe de ressources.


Pour affecter les deux règles à un utilisateur pour le service {{site.data.keyword.la_full_notm}} dans le contexte d'un groupe de ressources, procédez comme suit : 

1. Dans la barre de menus, cliquez sur **Gérer** &gt; **Accès (IAM)** puis sélectionnez **Utilisateurs**.
2. Sur la ligne de l'utilisateur auquel vous voulez affecter un accès, sélectionnez le menu **Actions**, puis cliquez sur **Affecter un accès**.
3. Sélectionnez **Affecter l'accès au sein d'un groupe de ressources**.
4. Sélectionnez un groupe de ressources.
5. Si aucun rôle n'a encore été accordé à l'utilisateur pour le groupe de ressources concerné, sélectionnez un rôle pour la zone **Affecter l'accès à un groupe de ressources**. 

    En fonction du rôle sélectionné, l'utilisateur peut afficher le groupe de ressources sur son tableau de bord, modifier le nom du groupe de ressources ou gérer les accès utilisateur au groupe. 
    
    Vous pouvez sélectionner **Aucun accès** si vous voulez que l'utilisateur puisse uniquement accéder au service {{site.data.keyword.la_full_notm}} dans le groupe de ressources.

6. Sélectionnez **IBM Log Analysis avec LogDNA**.
7. Sélectionnez le rôle de plateforme **Editeur**.
8. Sélectionnez le rôle de service **Responsable**.
8. Cliquez sur **Affecter**.

## Octroi à un utilisateur du droit d'afficher des journaux dans LogDNA
{: #user_logdna}

Un **utilisateur**, un **auditeur** ou un **développeur** peut avoir besoin de droits pour exécuter les actions suivantes : 

* Afficher les journaux
* Rechercher dans les journaux
* Filtrer les journaux

Par conséquent, vous devez disposer des règles suivantes :

* Une règle IAM pour le service {{site.data.keyword.la_full_notm}} avec le rôle de plateforme **Afficheur**. Cette règle accorde le droit d'afficher les détails d'une instance de service via la ligne de commande et dans le tableau de bord {{site.data.keyword.cloud_notm}}.
* Une règle IAM pour le service {{site.data.keyword.la_full_notm}} avec le rôle de service **Lecteur**. Cette règle accorde le droit d'afficher, de filtrer et d'effectuer des recherches dans les journaux via l'interface utilisateur Web de LogDNA.

**Remarque :** en tant qu'administrateur du service, lorsque vous affectez ces règles à un utilisateur, envisagez de le faire dans le contexte d'un groupe de ressources. Une instance {{site.data.keyword.la_full_notm}} est mise à disposition dans le contexte d'un groupe de ressources. Par conséquent, accordez les droits d'accès aux utilisateurs dans le contexte du groupe de ressources.

Pour affecter les deux règles à un utilisateur pour le service {{site.data.keyword.la_full_notm}} dans le contexte d'un groupe de ressources, procédez comme suit : 

1. Dans la barre de menus, cliquez sur **Gérer** &gt; **Accès (IAM)** puis sélectionnez **Utilisateurs**.
2. Sur la ligne de l'utilisateur auquel vous voulez affecter un accès, sélectionnez le menu **Actions**, puis cliquez sur **Affecter un accès**.
3. Sélectionnez **Affecter l'accès au sein d'un groupe de ressources**.
4. Sélectionnez un groupe de ressources.
5. Si aucun rôle n'a encore été accordé à l'utilisateur pour le groupe de ressources concerné, sélectionnez un rôle pour la zone **Affecter l'accès à un groupe de ressources**. 

    En fonction du rôle sélectionné, l'utilisateur peut afficher le groupe de ressources sur son tableau de bord, modifier le nom du groupe de ressources ou gérer les accès utilisateur au groupe. 
    
    Vous pouvez sélectionner **Aucun accès** si vous voulez que l'utilisateur puisse uniquement accéder au service {{site.data.keyword.la_full_notm}} dans le groupe de ressources.

6. Sélectionnez **IBM Log Analysis avec LogDNA**.
7. Sélectionnez le rôle de plateforme **Afficheur**.
8. Sélectionnez le rôle de service **Lecteur**.
8. Cliquez sur **Affecter**.

