---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, alerts

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

 
# Utilisation des alertes
{: #alerts}

Vous pouvez associer une ou plusieurs alertes à une vue. Vous pouvez définir plusieurs canaux de notification pour une alerte. Vous pouvez désactiver le son d'une alerte. Vous pouvez dissocier des alertes d'une vue.
{:shortdesc}

Vous pouvez configurer l'une des conditions suivantes pour une alerte :

* *Time frequency* : Fréquence à laquelle déclencher une alerte. Les valeurs admises sont : 30 secondes, 1 minute, 5 minutes, 15 minutes, 30 minutes, 1 heure, 6 heures, 12 heures et 24 heures.
* *Log lines counter* : Nombre de lignes de journal qui répondent aux critères de recherche et de filtrage de la vue. Lorsque ce nombre de lignes de journal est atteint, une alerte est déclenchée.

Vous pouvez décider si les deux conditions doivent être remplies ou une seule uniquement. Si les deux conditions sont définies, une alerte est déclenchée lorsque l'un des seuils est atteint. 

Par exemple, vous pouvez configurer une alerte déclenchée au bout de 30 secondes ou lorsque 100 lignes de journal qui répondent aux critères de recherche et de filtrage de la vue ont été collectées.

Vous pouvez configurer plusieurs canaux de notification. Les canaux admis sont `email`, `Slack`, `PagerDuty`, `Webhook`, `OpsGenie`, `Datadog`, `AppOptics` et `VictorOps`

Vous pouvez également définir un **préréglage**. Un préréglage est un modèle d'alerte que vous pouvez associer à un nombre illimité de vues. 

Pour réutiliser une configuration d'alerte avec différentes vues, configurez un **préréglage d'alerte**.
{: tip}

Une icône en forme de cloche s'affiche avec la vue pour indiquer qu'une alerte est associée à cette vue.



## Configuration d'un préréglage (modèle d'alerte)
{: #config_preset}

Pour configurer un préréglage, procédez comme suit :

1. Cliquez sur l'icône **Configuration** ![Icône Configuration](images/admin.png "Icône Admin").
2. Sélectionnez **Alerts**.
3. Sélectionnez **Add a preset alert**.
4. Sélectionnez un canal de notification. 
5. Définissez des conditions de seuil.

    1. Sélectionnez une fréquence. Par exemple, 12 heures.

    2. Indiquez le nombre de lignes de journal après lequel l'alerte doit être déclenchée.

    3. Indiquez si vous voulez que les deux conditions soient remplies ou une seule uniquement.

6. Ajoutez des détails concernant le canal de notification que vous avez sélectionné.

    Par exemple, pour le canal de notification par courrier électronique, ajoutez un ou plusieurs destinataires et éventuellement un fuseau horaire.

7. Cliquez sur **Save alert**.



## Configuration d'une alerte à l'aide d'un préréglage
{: #config_alert_preset}

Pour associer un préréglage à une vue, procédez comme suit :

1. Cliquez sur l'icône **Vues** ![Icône Configuration](images/views.png).
2. Créez une vue. 

    Appliquez une plage horaire, des filtres et des critères de recherche pour filtrer les lignes de journal qui s'affichent dans la vue. 

    Pour plus d'informations, voir [Création de vues](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7).

3. Cliquez sur le nom de la vue. Puis sélectionnez **Attach an alert**.

4. Sélectionnez un préréglage pour réutiliser une définition d'alerte. 

5. Cliquez sur **Save alert**. 




## Configuration d'une alerte spécifique à une vue
{: #config_alert_view}

Pour associer une alerte à une vue, procédez comme suit :

1. Cliquez sur l'icône **Vues** ![Icône Configuration](images/views.png).
2. Créez une vue. 

    Appliquez une plage horaire, des filtres et des critères de recherche pour filtrer les lignes de journal qui s'affichent dans la vue. 

    Pour plus d'informations, voir [Création de vues](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7).

3. Cliquez sur le nom de la vue. Puis sélectionnez **Attach an alert**.

4. Sélectionnez **view-specific alert**.

5. Sélectionnez un canal de notification. 

6. Définissez des conditions de seuil.

    1. Sélectionnez une fréquence. Par exemple, 12 heures.

    2. Indiquez le nombre de lignes de journal après lequel l'alerte doit être déclenchée.

    3. Indiquez si vous voulez que les deux conditions soient remplies ou une seule uniquement.

7. Ajoutez des détails concernant le canal de notification que vous avez sélectionné.

    Par exemple, pour le canal de notification par courrier électronique, ajoutez un ou plusieurs destinataires et éventuellement un fuseau horaire.

8. Cliquez sur **Save alert**.



## Suppression d'un préréglage (modèle d'alerte)
{: #delete_preset}

Pour supprimer un préréglage, procédez comme suit :

1. Cliquez sur l'icône **Configuration** ![Icône Configuration](images/admin.png "Icône Admin").
2. Sélectionnez **Alerts**.
3. Survolez avec la souris le bouton *Editer* du préréglage que vous voulez supprimer. L'option *Supprimer* s'affiche.
4. Sélectionner **Supprimer**.
5. Confirmez la suppression du préréglage. Cliquez sur **Supprimer**.

## Dissociation d'une vue d'une alerte spécifique à une vue
{: #delete_alert}

Pour dissocier un préréglage, procédez comme suit :

1. Cliquez sur l'icône **Configuration** ![Icône Configuration](images/admin.png "Icône Admin").
2. Sélectionnez **Alerts**.
3. Survolez avec la souris le bouton *Editer* de l'alerte que vous voulez supprimer. L'option *Supprimer* s'affiche.
4. Sélectionner **Detach**.
5. Confirmez la suppression de l'alerte. Cliquez sur **Detach**.



## Canaux de notification
{: #channels}

Le tableau suivant répertorie les canaux de notification que vous pouvez configurer pour une alerte déclenchée :

| Canal           | Détails de configuration | 
|-------------------|-----------------------|
| `email`             | Vous pouvez configurer une ou plusieurs adresses de courrier électronique.  | 
| `Slack`             | Vous pouvez configurer un canal Slack. |
| `Webhook`           | Vous pouvez configurer une adresse URL de point d'ancrage Web. |
| `PagerDuty`         | Vous pouvez configurer des détails de connexion dans votre système PagerDuty et sélectionner un service.|
| `OpsGenie`          | Vous pouvez configurer la clé d'API pour la connexion à votre système OpsGenie. |
| `Datadog`           | Vous pouvez configurer la clé d'API pour la connexion à votre système `Datadog`. |
| `AppOptics/Librato` | Vous pouvez configurer la clé d'API pour la connexion à votre système AppOptics/Librato. |
| `VictorOps`         | Vous pouvez configurer l'adresse URL de notification lorsqu'une alerte est déclenchée, la clé de routage et le type d'alerte. Les types d'alerte admis sont : `info`, `avertissement` et `critique` |
{: caption="Canaux de notification" caption-side="top"} 


