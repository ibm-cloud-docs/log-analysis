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

# Téléchargement des journaux
{: #downloading_logs1}

Vous pouvez télécharger des journaux vers un fichier local ou diriger des données vers un autre programme. Les journaux sont téléchargés dans le contexte d'une session. Une session
spécifie les journaux à télécharger. Si le téléchargement des journaux est interrompu, la session reprend le téléchargement là où il s'est arrêté. Une fois le téléchargement terminé, vous
devez supprimer la session.
{:shortdesc}

Procédez comme suit pour télécharger les données de journal disponibles dans un espace {{site.data.keyword.Bluemix_notm}} dans un fichier local :

## Etape 1 : Connexion à IBM Cloud

Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

## Etape 2 : Identification des journaux disponibles
{: #step31}

1. Utilisez la commande `ibmcloud cf logging status` afin d'identifier les journaux disponibles pour les deux dernières semaines. Exécutez la commande suivante :

    ```
    ibmcloud cf logging status
    ```
    {: codeblock}
    
    Par exemple, l'exécution de cette commande génère la sortie suivante :
    
    ```
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 | linux_syslog,log   |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}

    **Remarque :** le service {{site.data.keyword.loganalysisshort}} est un service global qui utilise le temps universel coordonné (TUC). Les jours sont définis
en tant que jours TUC. Afin d'obtenir des journaux pour un jour à heure locale spécifique, il peut être nécessaire de télécharger plusieurs jours TUC.


## Etape 3 : Création d'une session
{: #step32}

Une session est requise pour définir l'étendue des données de journal disponibles pour un téléchargement et pour conserver le statut du téléchargement. 

Utilisez la commande [cf logging session create](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_create1) pour créer une session. Vous pouvez également spécifier une date
de début, une date de fin et des types de journaux lorsque vous créez une session :  

* Lorsque vous spécifiez la date de début et la date de fin, la session fournit un accès aux journaux entre ces dates incluses. 
* Lorsque vous spécifiez le type de journal (**-t**), la session fournit un accès à un type de journal particulier. Cette fonction est importante lorsque vous
gérez des journaux à grande échelle car vous pouvez étendre une session à un petit sous-ensemble de journaux qui vous intéresse.

**Remarque :** pour chaque session, vous pouvez télécharger des journaux de 15 jours au maximum.

Pour créer une session pour le téléchargement des journaux de type *log*, exécutez la commande suivante :

```
ibmcloud cf logging session create -t log
```
{: codeblock}

La session renvoie les informations suivantes :

* La plage de dates à télécharger. La valeur par défaut est la date TUC en cours.
* Les types de journaux à télécharger. Par défaut, tous les types de journaux disponibles durant la période que vous spécifiez lorsque vous créez la session sont inclus. 
* Des informations indiquant si le compte entier doit être inclus, ou uniquement l'espace en cours. Par défaut, vous obtenez les journaux dans l'espace dans lequel vous êtes connecté.
* L'ID de session requis pour télécharger les journaux.

Exemple

```
$ ibmcloud cf logging session create -t log     
+--------------+--------------------------------------+
|     NAME     |                VALUE                 |
+--------------+--------------------------------------+
| Access-Time  | 2017-05-25T18:04:21.743792338Z       |
| Create-Time  | 2017-05-25T18:04:21.743792338Z       |
| Date-Range   | {                                    |
|              |  "End": "2017-05-25T00:00:00Z",      |
|              |  "Start": "2017-05-25T00:00:00Z"     |
|              | }                                    |
| Id           | -jshdjsunelsssr4566722==             |
| Space        | fdgrghg3-b090-4567-vvfg-afbc436902a3 |
| Type-Account | {                                    |
|              |  "Type": "log"                       |
|              | }                                    |
| Username     | xxx@yyy.com                          |
+--------------+--------------------------------------+
```
{: screen}

**Astuce :** pour afficher la liste des sessions actives, exécutez la commande [cf logging session list](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_list1).

## Etape 4 : Téléchargement des données de journal dans un fichier
{: #step42}

Pour télécharger les journaux qui sont spécifiés par les paramètres de session, exécutez la commande suivante :

```
ibmcloud cf logging download -o Log_File_Name Session_ID
```
{: codeblock}

où

* Log_File_Name est le nom du fichier de sortie.
* Session_ID est l'identificateur global unique de la session. Cette valeur est obtenue à l'étape précédente.

Exemple

```
ibmcloud cf logging download -o helloLogs.gz -jshdjsunelsssr4566722==
 160.00 KB / 380.33 KB [==============>------------------------]  42.07% 20.99 KB/s 10s
```
{: screen}

L'indicateur de progression se déplace de 0 à 100 % à mesure que les journaux se téléchargent.

**Remarque :** 

* Les données téléchargées sont au format JSON compressé. Si vous décompressez le fichier .gz et l'ouvrez, les données sont affichées au format JSON. 
* Le format JSON compressé est approprié pour l'ingestion par ElasticSearch ou Logstash. Si -o n'est pas indiqué, les données sont transmises à la sortie standard (stdout) afin que vous puissiez
les diriger directement vers votre propre pile ELK.
* Vous pouvez également traiter les données avec un programme pouvant analyser JSON. 

## Etape 5 : Suppression de la session
{: #step51}

Une fois que le téléchargement est terminé, vous devez supprimer la session à l'aide de la commande [cf logging session delete](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_delete1). 

Exécutez la commande suivante pour supprimer une session :

```
ibmcloud cf logging session delete Session_ID
```
{: codeblock}

où Session_ID est l'identificateur global unique de la session créée à l'étape précédente.

Exemple

```
ibmcloud cf logging session delete -jshdjsunelsssr4566722==
+---------+------------------------+
|  NAME   |         VALUE          |
+---------+------------------------+
| Message | Delete session success |
+---------+------------------------+
```
{: screen}




