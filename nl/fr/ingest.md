---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion 

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

 
# Envoi de journaux
{: #ingest}

Vous pouvez envoyer des données de journal à une instance {{site.data.keyword.la_full_notm}}. 
{:shortdesc}

Pour envoyer des journaux à l'aide d'un programme, procédez comme suit :

## Etape 1. Obtention de la clé d'API d'ingestion 
{: #ingest_step1}

**Remarque :** vous devez avoir le rôle **responsable** sur l'instance {{site.data.keyword.la_full_notm}} ou le service pour effectuer cette étape. Pour plus d'informations, voir [Octroi du droit de gérer des journaux et de configurer des alertes dans LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna).

Pour obtenir la clé d'ingestion, procédez comme suit :
    
1. Ouvrez l'interface utilisateur Web {{site.data.keyword.la_full_notm}}. Pour plus d'informations, voir [Accès à l'interface utilisateur Web {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Cliquez sur l'icône **Configuration** ![Icône Configuration](images/admin.png). Puis sélectionnez **Organisation**. 

3. Sélectionnez **Clés d'API**.

    La clé d'ingestion créée s'affiche. 

4. Utilisez une clé d'ingestion existante ou cliquez sur **Generate Ingestion Key** pour en créer une nouvelle.

    Une nouvelle clé est ajoutée à la liste. Copiez la clé.


## Etape 2. Envoi de journaux
{: #ingest_step2}

Pour envoyer des journaux, exécutez la commande cURL suivante :

```
curl "ENDPOINT/logs/ingest?QUERY_PARAMETERS" -u INGESTION_KEY: --header "Content-Type: application/json; charset=UTF-8" -d "LOG_LINES"
```
{: codeblock}

Où 

* ENDPOINT représente le point d'entrée du service. Chaque région a une adresse URL différente.
* QUERY_PARAMETERS sont les paramètres qui définissent les critères de filtrage appliqués à la demande d'ingestion.
* LOG_LINES décrit l'ensemble de lignes de journal que vous voulez envoyer. Il est défini en tant que tableau d'objets.
* INGESTION_KEY est la clé que vous avez créée à l'étape précédente.

Le tableau suivant répertorie les noeuds finaux par région :

| Région         | Noeud final                                             | 
|----------------|------------------------------------------------------|
| `Us-south`       | `https://logs.us-south.logging.cloud.ibm.com`        |
{: caption="Noeuds finaux par région" caption-side="top"} 


Le tableau suivant répertorie les paramètres de requête :

| Paramètre de requête | Type       | Statut     | Description |
|-----------------|------------|------------|-------------|
| `hostname`      | `chaîne`     | obligatoire   | Nom d'hôte de la source. |
| `mac`           | `chaîne`     | facultatif   | Adresse MAC de réseau de l'ordinateur hôte.    |
| `ip`            | `chaîne`     | facultatif   | Adresse IP locale de l'ordinateur hôte.  | 
| `now`           | `date-heure`  | facultatif   | Horodatage UNIX de la source en millisecondes au moment de la demande. Utilisée pour calculer le décalage de temps.|
| `tags`          | `chaîne`     | facultatif   | Etiquettes utilisées pour regrouper des hôtes de manière dynamique. |
{: caption="Paramètres de requête" caption-side="top"} 



Le tableau suivant répertorie les données nécessaires par ligne de journal :

| Paramètres     | Type       | Description                                   |
|----------------|------------|-----------------------------------------------|
| `timestamp`      |            | Horodatage UNIX, avec les millisecondes, du moment où l'entrée de journal a été enregistrée.       | 
| `line`           | `chaîne`     | Texte de la ligne de journal.                                     |
| `app`            | `chaîne`     | Nom de l'application qui génère la ligne de journal.  |
| `level`          | `chaîne`     | Entrez une valeur pour indiquer le niveau. Par exemple, `INFO`, `AVERTISSEMENT` ou `ERREUR`. |
| `meta`           |            | Cette zone est réservée aux informations personnalisées qui sont associées à une ligne de journal. Pour ajouter des métadonnées à un appel API, spécifiez la zone meta sous les objets "line". Les métadonnées peuvent être affichées dans ce contexte de ligne.                      |
{: caption="Zones des objets ligne" caption-side="top"} 

Par exemple, voici le JSON pour une ligne de journal que vous voulez ingérer :

```
{ 
  "lines": [ 
    { 
      "timestamp": 2018-11-02T10:53:06+00:00, 
      "line":"This is my first log line.", 
      "app":"myapp",
      "level": "INFO",
      "meta": {
        "customfield": {"nestedfield": "nestedvalue"}
      }
    }
  ] 
}
```
{: screen}


## Exemple
{: #ingest_example}

L'exemple suivant illustre la commande cURL d'envoi d'une seule ligne de journal au service {{site.data.keyword.la_full_notm}} : 

```
curl "https://logs.us-south.logging.cloud.ibm.com/logs/ingest?hostname=MYHOST&now=$(date +%s)000" -u xxxxxxxxxxxxxxxxxxxxxxx: --header "Content-Type: application/json; charset=UTF-8" -d "{\"lines\":[{\"line\":\"This is a sample test log statement\",\"timestamp\":\"2018-11-02T10:53:06+00:00\",\"level\":\"INFO\",\"app\":\"myapp\"}]}"
```
{: screen}

