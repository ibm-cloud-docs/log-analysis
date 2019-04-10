---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, logs

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

# Affichage des journaux
{: #view_logs}

Après avoir mis une instance à disposition dans le service {{site.data.keyword.la_full_notm}} dans {{site.data.keyword.cloud_notm}}, et configuré un agent LogDNA pour une source de journal, vous pouvez afficher, surveiller et gérer les données de journal via l'interface utilisateur Web {{site.data.keyword.la_full_notm}}.
{:shortdesc}

Lorsque vous démarrez l'interface utilisateur Web {{site.data.keyword.la_full_notm}}, les entrées de journal s'affichent dans un format prédéfini. Dans la section **Préférences utilisateur**, vous pouvez modifier la façon dont les informations s'affichent sur chaque ligne de journal. Vous pouvez également filtrer les journaux et modifier les paramètres de recherche, puis ajouter un signet au résultat en tant que *vue*. Vous pouvez associer une ou plusieurs alertes à une vue ou en supprimer. Vous pouvez définir un format personnalisé qui détermine comment vos lignes se présentent dans la vue. Vous pouvez développer une ligne de journal et voir les données analysées.


Pour afficher des journaux, procédez comme suit :


## Etape 1. Accord à un utilisateur de règles IAM pour l'affichage de journaux
{: #view_logs_step1}

**Remarque :** vous devez être administrateur du service {{site.data.keyword.la_full_notm}}, administrateur de l'instance {{site.data.keyword.la_full_notm}} ou disposer de droits IAM sur le compte pour accorder des règles à d'autres utilisateurs.

Le tableau suivant répertorie les règles minimales dont doit disposer un utilisateur pour pouvoir démarrer l'interface utilisateur Web {{site.data.keyword.la_full_notm}} et afficher des journaux :

| Service                        | Rôle                      | Droits accordés            |
|--------------------------------|---------------------------|-------------------------------|  
| `{{site.data.keyword.la_full_notm}} ` | Rôle de plateforme : Afficheur     | Autorise l'utilisateur à afficher la liste des instances de service dans le tableau de bord de journalisation d’observabilité. |
| `{{site.data.keyword.la_full_notm}} ` | Rôle de service : Lecteur      | Autorise l'utilisateur à démarrer l'interface utilisateur Web et à afficher des journaux dans cette interface.  |
{: caption="Tableau 1. Règles IAM" caption-side="top"} 

Pour plus d'informations sur la manière de configurer ces règles pour un utilisateur, voir [Octroi à un utilisateur du droit d'afficher des journaux dans LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna).


## Etape 2. Accès à l'interface utilisateur Web via l'interface utilisateur {{site.data.keyword.cloud_notm}}
{: #view_logs_step2}

Pour démarrer l'interface utilisateur {{site.data.keyword.la_full_notm}} via l'interface utilisateur {{site.data.keyword.cloud_notm}}, procédez comme suit :

1. Connectez-vous à votre compte {{site.data.keyword.cloud_notm}}.

    Cliquez sur le [tableau de bord {{site.data.keyword.cloud_notm}}![Icône de lien externe](../../icons/launch-glyph.svg "Icône de lien externe")](https://cloud.ibm.com/login){:new_window} pour ouvrir le tableau de bord {{site.data.keyword.cloud_notm}}.

	Une fois connecté avec votre ID utilisateur et votre mot de passe, le *tableau de bord* {{site.data.keyword.cloud_notm}} s'ouvre.

2. Dans le menu de navigation, sélectionnez **Observabilité**. 

3. Sélectionnez **Journalisation**. 

    La liste des instances {{site.data.keyword.la_full_notm}} disponibles sur {{site.data.keyword.cloud_notm}} s'affiche.

4. Sélectionnez une instance. Ensuite, cliquez sur **Afficher LogDNA**.

L'interface utilisateur Web {{site.data.keyword.la_full_notm}} s'ouvre et affiche les journaux envoyés à cette instance.


## Etape 3. Personnalisation de votre vue par défaut
{: #view_logs_step3}

Dans la section **Préférences utilisateur**, vous pouvez modifier l'ordre des zones de données qui s'affichent pour chaque ligne.

Pour modifier le format d'une ligne de journal, procédez comme suit :

1. Cliquez sur l'icône **Configuration** ![Icône Configuration](images/admin.png "Icône Admin").
2. Sélectionnez **Préférences utilisateur**. Une nouvelle fenêtre s'ouvre.
3. Sélectionnez **Format de journal**.
4. Modifiez la section *Format de ligne* de manière à répondre à vos exigences. Faites glisser les zones.


## Etape 4. Examen d'une ligne de journal
{: #view_logs_step4}

Vous pouvez à tout moment visualiser chaque ligne de journal en contexte.

Pour ce faire, procédez comme suit : 

1. Cliquez sur l'icône **Vues** ![Icône Configuration](images/views.png "Icône Configuration").
2. Sélectionnez **Tout** ou bien une vue.
3. Identifiez dans le journal une ligne que vous voulez examiner.
4. Développez la ligne de journal. 

    Des informations relatives aux identificateurs, aux étiquettes et aux libellés de la ligne s'affichent.

5. Cliquez sur **View in Context** pour afficher la ligne de journal dans le contexte des autres lignes de journal de cet hôte, de cette application, ou les deux.

6. Cliquez sur **Copier dans le presse-papiers** pour copier la zone de message dans le presse-papiers.

Lorsque vous avez terminé, refermez la ligne.


## Etape 5. Filtrage de journaux
{: #view_logs_step5}

Vous pouvez filtrer les journaux par source de journal, application et niveau de journalisation. 

* Une source peut être un hôte, un ordinateur, une machine virtuelle ou une application Heroku.
* Une application représente un fichier journal, un programme ou un conteneur.
* Exemples de niveau de journalisation : INFO, DEBUG, ERROR

Pour filtrer des journaux, procédez comme suit :

1. Cliquez sur l'icône **Vues** ![Icône Configuration](images/views.png "Icône Configuration").
2. Sélectionnez **Tout** ou bien une vue.
3. Développez **All Tags** pour visualiser la liste des étiquettes identifiées dans les journaux. Puis sélectionnez celles qui vous intéressent.
4. Développez **All Sources** pour visualiser la liste des sources de journal identifiées dans les journaux. Puis sélectionnez celles qui vous intéressent.
5. Développez **Toutes les applications** pour visualiser la liste des applications identifiées dans les journaux. Puis sélectionnez celles qui vous intéressent.
6. Développez **All Levels** pour visualiser la liste des niveaux identifiés dans les journaux. Puis sélectionnez ceux qui vous intéressent.


**Remarque :** dans chaque section, vous pouvez regrouper plusieurs options dans un groupe. Regroupez des étiquettes, des sources de journal, des applications et des niveaux de journalisation afin de réutiliser ces regroupements lorsque vous filtrez des données de journal dans d'autres vues personnalisées.

Pour créer un groupe, sélectionnez plusieurs valeurs. Puis cliquez sur **Sauvegarder en tant que groupe**. Entrez un nom pour le groupe, puis sauvegardez-le.


## Etape 6. Recherche dans les journaux
{: #view_logs_step6}

Lorsque vous recherchez des données de journal, la recherche applique tous les filtres de journal et requêtes temporelles configurés dans cette vue.

Vous pouvez effectuer des recherches simples (recherche de chaîne d'un seul terme), des recherches composées (plusieurs opérateurs et termes de recherche), des recherches de zone si la ligne de journal peut être analysée, et d'autres types de recherche. Pour plus d'informations, voir [comment effectuer des recherches dans les journaux dans la documentation LogDNA![Icône de lien externe](../../icons/launch-glyph.svg "Icône de lien externe")](https://docs.logdna.com/docs/search){:new_window}.

**Remarque :** les opérateurs AND et OR sont sensibles à la casse et doivent être indiqués en majuscules.



## Etape 7. Création de vue
{: #view_logs_step7}


Pour créer une vue, procédez comme suit :

1. Cliquez sur l'icône **Vues** ![Icône Configuration](images/views.png "Icône Configuration").
2. Sélectionnez **Tout** ou bien une vue.
3. Filtrez les données de journal, puis cliquez sur **Save as new view / alert**.

    La page *Créer une nouvelle vue* s'ouvre.

4. Dans la zone *Name*, entrez un nom pour la vue.

5. Vous pouvez éventuellement ajouter une catégorie. Entrez un nom, puis cliquez sur **Add this as new view category**.

6. Vous pouvez éventuellement associer une alerte. Une nouvelle section permettant de configurer l'alerte s'affiche.

7. Cliquez sur **Sauvegarder la vue**


