---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, export logs

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

 
# Exportation de journaux vers un fichier local
{: #export}

Vous pouvez exporter des données de journal au format JSONL depuis une instance {{site.data.keyword.la_full_notm}} vers un fichier local. L'exportation des journaux peut être effectuée à l'aide d'un programme ou depuis l'interface utilisateur Web IBM Log Analysis. 
{:shortdesc}

Lorsque vous exportez des données de journal, tenez compte des informations suivantes :
* Vous exportez un ensemble d'entrées de journal. Pour définir l'ensemble de données à exporter, vous pouvez appliquer des filtres et des critères de recherche. Vous pouvez également indiquer une plage horaire. 
* A partir de l'interface utilisateur Web, lorsque vous exportez des journaux, vous recevez à votre adresse électronique un courrier électronique avec un lien vers un fichier compressé qui contient les données. Pour obtenir les données, vous devez cliquer sur le lien et télécharger le fichier compressé.
* Lorsque vous exportez des journaux à l'aide d'un programme, vous pouvez choisir d'envoyer un courrier électronique ou de diffuser les journaux sur votre terminal.
* Le fichier journal compressé qui contient les données à exporter est disponible pendant 48 heures au maximum. 
* Vous pouvez exporter un maximum de 10 000 lignes.



## Exportation de journaux à partir de l'interface utilisateur Web
{: #ui}

Pour exporter des données de journal, procédez comme suit :

1. Cliquez sur l'icône **Vues** ![Icône Configuration](images/views.png).
2. Sélectionnez **Tout** ou bien une vue.
3. Appliquez une plage horaire, des filtres et des critères de recherche jusqu'à obtenir les entrées de journal que vous voulez exporter.
4. Cliquez sur **Unsaved View** si vous commencez par la vue **Tout**. Cliquez sur le nom de la vue si vous avez sélectionné une vue à l'étape précédente.
5. Sélectionnez `Export lines`. Une nouvelle fenêtre s'ouvre.
6. Vérifiez la plage horaire. Si vous devez la modifier, cliquez sur la plage horaire prédéfinie dans la zone *Change the Time Range for export*.
7. Sélectionner **Prefer newer lines** ou **Prefer older lines** pour le cas où l'exportation dépasse la limite de lignes.
8. Consultez votre courrier électronique. Vous recevez de **LogDNA** un courrier électronique qui contient un lien pour télécharger les lignes exportées.


## Exportation de journaux à l'aide d'un programme en utilisant l'API
{: #api}

Pour exporter des journaux à l'aide d'un programme, procédez comme suit :

1. Générez une clé de service. 

    **Remarque :** vous devez avoir le rôle **responsable** sur l'instance {{site.data.keyword.la_full_notm}} ou le service pour effectuer cette étape. Pour plus d'informations, voir [Octroi du droit de gérer des journaux et de configurer des alertes dans LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna).

    1. Ouvrez l'interface utilisateur Web {{site.data.keyword.la_full_notm}}. Pour plus d'informations, voir [Accès à l'interface utilisateur Web {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

    2. Cliquez sur l'icône **Configuration** ![Icône Configuration](images/admin.png). Puis sélectionnez **Organisation**. 

    3. Sélectionnez **Clés d'API**.

        Les clés de service créées s'affichent. 

    4. Cliquez sur **Générer une clé de service**.

        Une nouvelle clé est ajoutée à la liste. Copiez cette clé.

2. Exportez les journaux. Exécutez la commande cURL suivante :

    ```
    curl "ENDPOINT/v1/export?QUERY_PARAMETERS" -u SERVICE_KEY:
    ```
    {: codeblock}

    Où 

    * ENDPOINT représente le point d'entrée vers le service. Chaque région a une adresse URL différente.
    * QUERY_PARAMETERS sont les paramètres qui définissent les critères de filtrage appliqués à la demande d'exportation.
    * SERVICE_KEY est la clé de service créée à l'étape précédente.

Le tableau suivant répertorie les noeuds finaux par région :

| Région         | Noeud final                                             | 
|----------------|------------------------------------------------------|
| `Us-south`       | `https://api.us-south.logging.cloud.ibm.com `        |
{: caption="Noeuds finaux par région" caption-side="top"} 


Le tableau suivant répertorie les paramètres de requête que vous pouvez définir :

| Paramètre de requête | Type       | Statut     | Description |
|-----------|------------|------------|-------------|
| `from`      | `int32`      | Obligatoire   | Heure de début. Défini en tant qu'horodatage UNIX en secondes ou millisecondes. |
| `to`        | `int32`      | Obligatoire   | Heure de fin. Défini en tant qu'horodatage UNIX en secondes ou millisecondes.    |
| `size`      | `chaîne`     | Facultatif   | Nombre de lignes de journal à inclure dans l'exportation.  | 
| `hosts`     | `chaîne`     | Facultatif   | Liste d'hôtes séparés par des virgules. |
| `apps`      | `chaîne`     | Facultatif   | Liste d'applications séparées par des virgules. |
| `levels`    | `chaîne`     | Facultatif   | Liste de niveaux de journalisation séparés par des virgules. |
| `query`     | `chaîne`     | Facultatif   | Requête de recherche. Pour plus d'informations, voir [Recherche dans les journaux](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6). |
| `prefer`    | `chaîne`     | Facultatif   | Définit les lignes de journal à exporter. Les valeurs admises sont `head`, premières lignes de journal et `tail`, dernières lignes de journal. La valeur par défaut est tail.  |
| `email`     | `chaîne`     | Facultatif   | Indique le courrier électronique avec le lien de téléchargement de l'exportation. Par défaut, les lignes de journal sont diffusées.|
| `emailSubject` | `chaîne`     | Facultatif   | Permet de définir la ligne Objet du courrier électronique. </br>Utilisez `%20` pour représenter un espace. Par exemple, `Exporter%20journaux`. |
{: caption="Paramètres de requête" caption-side="top"} 

Par exemple, pour diffuser des lignes de journal sur le terminal, vous pouvez exécuter la commande suivante :

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info" -u e08c0c759663491880b0d61712346789:
```
{: screen}

Pour envoyer un courrier électronique contenant le lien permettant de télécharger les lignes de journal désignées pour exportation, vous pouvez exécuter la commande suivante :

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=joe@ibm.com" -u e08c0c759663491880b0d61712346789:
```
{: screen}


Pour envoyer un courrier électronique dont l'objet est personnalisé, vous pouvez exécuter la commande suivante :

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=lopezdsr@uk.ibm.com&emailSubject=Export%20test" -u e08c0c759663491880b0d61712346789:
```
{: screen}

