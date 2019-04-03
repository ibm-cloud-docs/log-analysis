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

# Interface de ligne de commande Log Analysis (plug-in {{site.data.keyword.Bluemix_notm}})
{: #log_analysis_cli}

L'interface de ligne de commande {{site.data.keyword.loganalysislong}} est un plug-in {{site.data.keyword.Bluemix_notm}} que vous pouvez utiliser pour gérer les journaux qui sont stockés dans le composant Log Collection.
{: shortdesc}

**Prérequis**
* Avant d'exécuter les commandes de journalisation, connectez-vous à {{site.data.keyword.Bluemix_notm}} avec la commande `ibmcloud login` pour générer un jeton d'accès et authentifier votre session.

Pour savoir comment utiliser l'interface de ligne de commande {{site.data.keyword.loganalysisshort}},
voir [Gestion des journaux](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#log_analysis_ov).

<table>
  <caption>Commandes de gestion des journaux</caption>
  <tr>
    <th>Commande</th>
    <th>Quant l'utiliser</th>
  </tr>
  <tr>
    <td>[ibmcloud logging](#base)</td>
    <td>Utilisez cette commande pour obtenir des informations sur l'interface de ligne de commande, comme la liste des commandes.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-delete](#delete)</td>
    <td>Utilisez cette commande pour supprimer des journaux stockés dans le composant Log Collection.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-download](#download)</td>
    <td>Utilisez cette commande pour télécharger des journaux depuis le composant Log Collection dans un fichier local ou pour diriger les journaux vers un autre programme tel qu'Elastic Stack. </td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-show](#status)</td>
    <td>Utilisez cette commande pour obtenir des informations sur les journaux qui sont collectés dans un espace, une organisation ou un compte.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging help](#help)</td>
    <td>Utilisez cette commande pour obtenir de l'aide au sujet de l'utilisation de l'interface de ligne de commande ainsi que la liste de toutes les commandes.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging option-show](#optionshow)</td>
    <td>Utilisez cette commande pour afficher la durée de conservation des journaux qui sont disponibles dans un espace, une organisation ou un compte.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging option-update](#optionupdate)</td>
    <td>Utilisez cette commande pour définir la durée de conservation pour les journaux qui sont disponibles dans un espace, une organisation ou un compte.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging quota-usage-show](#quotausage)</td>
    <td>Utilisez cette commande pour obtenir les informations d'utilisation de quota pour un espace, une organisation ou un compte. Vous pouvez également obtenir l'historique du quota.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging session-create](#session_create)</td>
    <td>Utilisez cette commande pour créer une session.</td>
  <tr>
  <tr>
    <td>[ibmcloud logging session-delete](#session_delete)</td>
    <td>Utilisez cette commande pour supprimer une session.</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging sessions](#session_list)</td>
    <td>Utilisez cette commande pour afficher la liste des sessions actives et leurs ID.</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging session-show](#session_show)</td>
    <td>Utilisez cette commande pour afficher le statut d'une session unique.</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging token-get](#tokenget)</td>
    <td>Utilisez cette commande pour obtenir le jeton de journalisation qui permet d'envoyer des données de journal au service {{site.data.keyword.loganalysisshort}}.</td>
  </tr>
</table>


## ibmcloud logging
{: #base}

Fournit des informations générales sur l'interface de ligne de commande.

```
ibmcloud logging 
```
{: codeblock}

**Exemples**

Pour obtenir la liste des commandes, exécutez la commande suivante :

```
ibmcloud logging 
NAME:
   ibmcloud logging - IBM Cloud Log Analysis Service
USAGE:
   ibmcloud logging command [arguments...] [command options]

COMMANDS:
COMMANDS:
   log-delete         Delete log
   log-download       Download a log
   log-show           Show the count, size, and type of logs per day
   session-create     Create a session
   session-delete     Delete session
   sessions           List sessions info
   session-show       Show a session info
   option-show        Show the log retention
   option-update      Show the log options
   token-get          Get a logging token for sending logs
   quota-usage-show   Show quota usage info
   help             
   
Enter 'ibmcloud logging help [command]' for more information about a command.
```
{: codeblock}




## ibmcloud logging log-delete
{: #delete3}

Supprime les journaux stockés dans le composant Log Collection.

```
ibmcloud logging log-delete [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-f, --force ]
```
{: codeblock}

**Paramètres**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facultatif) Définit le type de ressource. Les valeurs admises sont *space*, *account* et *org*.
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facultatif) Pour cette zone, définissez l'ID d'un espace, d'une organisation ou d'un compte. <br>Par défaut, si vous ne spécifiez pas ce paramètre, la commande utilise l'ID de la ressource à laquelle vous êtes connecté. 
  </dd>
  
  <dt>-s, --start START_DATE</dt>
  <dd>(Facultatif) Définit la date de début en temps universel coordonné (TUC) : *AAAA-MM-JJ*, par exemple `2006-01-02`. <br>La valeur par défaut correspond aux
deux semaines précédant la date du jour.
  </dd>
  
  <dt>-e, --end END_DATE</dt>
  <dd>(Facultatif) Définit la date de fin en temps universel coordonné (TUC) : *AAAA-MM-JJ*, par exemple `2006-01-02`. <br>La valeur par défaut est la
date en cours.
  </dd>
  
  <dt>-f, --force </dt>
  <dd>(Facultatif) Définissez cette option pour supprimer les journaux sans avoir à confirmer votre action.
  </dd>
</dl>

**Exemple**

Afin de supprimer les journaux du type *linux_syslog* du 25 mai 2017, exécutez la commande suivante :
```
ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
```
{: screen}



## ibmcloud logging log-download 
{: #download3}

Télécharge les journaux depuis le composant Log Collection vers un fichier local ou dirige les journaux vers un autre programme, tel qu'Elastic Stack. 

**Remarque :** pour télécharger les fichiers, vous devez d'abord créer une session. Une session définit quels journaux doivent être téléchargés en fonction de la plage
de dates, du type de journal et du type de compte. Les journaux sont téléchargés dans le contexte d'une session. Pour plus d'informations, voir [ibmcloud logging session create (bêta)](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#session_create).

```
 ibmcloud logging log-download  [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-o, --output OUTPUT] SESSION_ID

```
{: codeblock}

**Paramètres**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facultatif) Définit le type de ressource. Les valeurs admises sont *space*, *account* et *org*.
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facultatif) Pour cette zone, définissez l'ID d'un espace, d'une organisation ou d'un compte. <br>Par défaut, si vous ne spécifiez pas ce paramètre, la commande utilise l'ID de la ressource à laquelle vous êtes connecté. 
  </dd>
 
  <dt>-o, --output OUTPUT</dt>
  <dd>(Facultatif) Définit le chemin et le nom du fichier de sortie local où les journaux sont téléchargés. <br>La valeur par défaut est un trait d'union (-). <br>Définissez ce
paramètre sur la valeur par défaut pour que les journaux soient générés dans la sortie standard.</dd>

</dl>

**Arguments**

<dl>
  <dt>SESSION_ID</dt>
  <dd>Cette valeur indique l'ID de la session que vous devez utiliser lors du téléchargement des journaux. <br>**Remarque :** la commande `ibmcloud logging session-create` fournit les paramètres qui déterminent quels sont les journaux qui sont téléchargés. </dd>
</dl>

**Remarque :** si vous exécutez à nouveau la même commande une fois que le téléchargement est terminé, cela n'aura aucun effet. Pour télécharger à nouveau les mêmes
données, vous devez utiliser un fichier différent ou une session différente.

**Exemples**

Sur un système Linux, pour télécharger les journaux dans un fichier appelé mylogs.gz, exécutez la commande suivante :

```
ibmcloud logging log-download -o mylogs.gz guBeZTIuYtreOPi-WMnbUg==
```
{: screen}

Pour télécharger des journaux dans Elastic Stack, exécutez la commande suivante :

```
ibmcloud logging log-download guBeZTIuYtreOPi-WMnbUg== | gunzip | logstash -f logstash.conf
```
{: screen}

Le fichier suivant est un exemple de fichier logstash.conf :

```
input {
  stdin {
    codec => json_lines {}
  }
}
output {
  elasticsearch {
    hosts => [ "127.0.0.1:9200" ]
  }
}
```
{: screen}


## ibmcloud logging help
{: #help}

Fournit des informations sur le mode d'utilisation d'une commande.

```
ibmcloud logging help [command] 
```
{: codeblock}

**Paramètres**

<dl>
<dt>Commande</dt>
<dd>Définissez le nom de la commande pour laquelle vous souhaitez obtenir de l'aide.
</dd>
</dl>


**Exemples**

Pour obtenir de l'aide sur la façon dont vous pouvez exécuter la commande pour afficher le statut des journaux, exécutez la commande suivante :

```
ibmcloud logging help log-show
NAME:
   log-show - Show the count, size, and type of logs per day

USAGE:
   ibmcloud logging log-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-l, --list-type-detail]

OPTIONS:
   -r, --resource-type     Resource type, the valid resource type is account, org, or space
   -i, --resource-id       Resource id, the target resource id
   -s, --start             Start Date, UTC time value included in format YYYY-MM-DD
   -e, --end               End Date, UTC time value included in format YYYY-MM-DD
   -t, --type              Log Type, for example "syslog"
   -l, --list-type-detail  List the detailed type

```
{: screen}


## ibmcloud logging option-show
{: #optionshow}

Affiche la durée de conservation pour les journaux qui sont disponibles dans un espace, une organisation ou un compte. 

* La durée est définie en nombre de jours.
* La valeur par défaut est **-1**. 

**Remarque :** par défaut, tous les journaux sont stockés. Vous devez les supprimer manuellement à l'aide de la commande **delete**. Définissez une règle de conservation pour supprimer les journaux automatiquement.

```
ibmcloud logging option-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID]
```
{: codeblock}

**Paramètres**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facultatif) Définit le type de ressource. Les valeurs admises sont *space*, *account* et *org*.
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facultatif) Pour cette zone, définissez l'ID d'un espace, d'une organisation ou d'un compte. <br>Par défaut, si vous ne spécifiez pas ce paramètre, la commande utilise l'ID de la ressource à laquelle vous êtes connecté. 
  </dd>

</dl>

**Exemples**

Afin d'afficher la durée de conservation en cours par défaut pour l'espace auquel vous êtes connecté, exécutez la commande suivante :

```
ibmcloud logging option-show
```
{: screen}




## ibmcloud logging option-update
{: #optionupdate}

Change la durée de conservation des journaux qui sont disponibles dans un espace, une organisation ou un compte. 

* La durée est définie en nombre de jours.
* La valeur par défaut est **-1**. 

```
ibmcloud logging option-update [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] <-e,--retention RETENTION_VALUE>
```
{: codeblock}

**Paramètres**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facultatif) Définit le type de ressource. Les valeurs admises sont *space*, *account* et *org*.
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facultatif) Pour cette zone, définissez l'ID de l'espace, de l'organisation ou du compte pour lequel obtenir des informations. <br>Par défaut, si vous ne spécifiez pas ce paramètre, la commande utilise l'ID de la ressource à laquelle vous êtes connecté. 
  </dd>
  
  <dt>-e,--retention RETENTION_VALUE</dt>
  <dd>Définit le nombre de jours pendant lequel les journaux sont conservés. </dd>

</dl>

**Exemple**

Afin de modifier la durée de conservation à 25 jours pour l'espace auquel vous êtes connecté, exécutez la commande suivante :

```
ibmcloud logging option-update -e 25
```
{: screen}


## ibmcloud logging quota-usage-show
{: #quotausage}

Fournit des informations sur l'utilisation du quota d'un espace, d'une organisation ou d'un compte. Vous pouvez également l'utiliser pour obtenir l'utilisation de l'historique.

* La durée est définie en nombre de jours.
* La valeur par défaut est **-1**. 

```
ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s,--history]
```
{: codeblock}

**Paramètres**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facultatif) Définit le type de ressource. Les valeurs admises sont *space*, *account* et *org*.
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facultatif) Pour cette zone, définissez l'ID d'un espace, d'une organisation ou d'un compte. <br>Par défaut, si vous ne spécifiez pas ce paramètre, la commande utilise l'ID de la ressource à laquelle vous êtes connecté. 
  </dd>
  
  <dt>-s,--history</dt>
  <dd>(Facultatif) Définissez ce paramètre pour obtenir les informations d'historique relatives à l'utilisation du quota.</dd>

</dl>

**Exemple**

Pour obtenir l'historique de l'utilisation du quota d'un domaine d'espace, exécutez la commande suivante :

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744 -s
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Date         Allotmant   Usage   
2018.02.28   524288000   80405926   
2018.03.06   524288000   18955540   
2018.03.05   524288000   47262944   
2018.03.08   524288000   18311338   
2018.03.01   524288000   82416831   
2018.03.03   524288000   75045462   
2018.03.07   524288000   17386278   
2018.03.02   524288000   104316444   
2018.03.04   524288000   73125223   
```
{: screen}

## ibmcloud logging session-create
{: #session_create}

Crée une session.

**Remarque :** vous pouvez avoir jusqu'à 30 sessions simultanées dans un espace. La session est créée pour un utilisateur. Les sessions ne peuvent pas être partagées
entre les utilisateurs dans un espace.

```
ibmcloud logging session-create [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-T, --time, LOG_TIME]
```
{: codeblock}

**Paramètres**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facultatif) Définit le type de ressource. Les valeurs admises sont *space*, *account* et *org*.
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facultatif) Pour cette zone, définissez l'ID d'un espace, d'une organisation ou d'un compte. <br>Par défaut, si vous ne spécifiez pas ce paramètre, la commande utilise l'ID de la ressource à laquelle vous êtes connecté. 
  </dd>
  
  <dt>-s, --start START_DATE</dt>
  <dd>(Facultatif) Définit la date de début en temps universel coordonné (TUC) : *AAAA-MM-JJ*, par exemple `2006-01-02`. <br>La valeur par défaut correspond aux
deux semaines précédant la date du jour.
  </dd>
  
  <dt>-e, --end END_DATE</dt>
  <dd>(Facultatif) Définit la date de fin en temps universel coordonné (TUC) : *AAAA-MM-JJ*, par exemple `2006-01-02`. <br>La valeur par défaut est la
date en cours.
  </dd>
  
  <dt>-t, --type, LOG_TYPE</dt>
  <dd>(Facultatif) Définit le type de journal. <br>Par exemple, *syslog* est un type de journal. <br>La valeur par défaut est un astérisque (*). <br>Vous pouvez spécifier plusieurs types de journaux en séparant chacun d'eux par une virgule, par exemple *log_type_1,log_type_2,log_type_3*.
  </dd>

  <dt>-T, --time, LOG_TIME</dt>
  <dd>(Facultatif) Définit l'heure à laquelle vous souhaitez obtenir les journaux pour un type spécifique. </br>Les valeurs valides sont comprises entre 0 et 23. </br>Doit être combinée avec LOG_TYPE.
  </dd>

</dl>


**Valeurs renvoyées**

<dl>

    <dt>ID</dt>
    <dd>ID de session.</dd>
	
	<dt>Resource type</dt>
    <dd>ID de ressource.</dd>

    <dt>AccessTime</dt>
    <dd>Horodatage indiquant quand la session a été utilisée pour la dernière fois.</dd>

    <dt>CreateTime</dt>
    <dd>Horodatage correspondant à la date et à l'heure de création de la session.</dd>
	
	<dt>Start</dt>
    <dd>Indique le premier jour utilisé pour filtrer les journaux. </dd>

    <dt>End</dt>
    <dd>Indique le dernier jour utilisé pour filtrer les journaux.</dd>

    <dt>Type</dt>
    <dd>Types de journaux qui sont téléchargés via la session.</dd>

</dl>


**Exemple**

Afin de créer une session qui inclut les journaux du 13 novembre 2017, exécutez la commande suivante :

```
ibmcloud logging session-create -s 2017-11-13 -e 2017-11-13
Creating session for xxxxx@yyy.com resource: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx ...

ID                                     Space                                  CreateTime                       AccessTime                       Start        End          Type   
1ef776d1-4d25-4297-9693-882606c725c8   xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx   2017-11-16T11:52:06.376125207Z   2017-11-16T11:52:06.376125207Z   2017-11-13   2017-11-13   ANY_TYPE   
Session: 1ef776d1-4d25-4297-9693-882606c725c8 is created
```
{: screen}


## ibmcloud logging session-delete 
{: #session_delete}

Supprime une session, spécifiée par l'ID de session.

```
ibmcloud session-delete [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] SESSION_ID
```
{: codeblock}

**Paramètres**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facultatif) Définit le type de ressource. Les valeurs admises sont *space*, *account* et *org*.
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facultatif) Pour cette zone, définissez l'ID d'un espace, d'une organisation ou d'un compte. <br>Par défaut, si vous ne spécifiez pas ce paramètre, la commande utilise l'ID de la ressource à laquelle vous êtes connecté. 
  </dd>
 
</dl>

**Arguments**

<dl>
  <dt>SESSION_ID</dt>
  <dd>ID de la session active à supprimer.</dd>
</dl>

**Exemple**

Pour supprimer une session dont l'ID de session est *cI6hvAa0KR_tyhjxZZz9Uw==*, exécutez la commande suivante :

```
ibmcloud logging session-delete cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}



## ibmcloud logging sessions
{: #session_list}

Affiche la liste des sessions actives et leurs ID.

```
ibmcloud logging sessions [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID]
```
{: codeblock}

**Paramètres**

<dl>

  <dt>-r,--resource-type RESOURCE_TYPE</dt>
      <dd>(Facultatif) Définit le type de ressource. Les valeurs admises sont *space*, *account* et *org*. </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
      <dd>(Facultatif) Pour cette zone, définissez l'ID d'un espace, d'une organisation ou d'un compte. <br>Par défaut, si vous ne spécifiez pas ce paramètre, la commande utilise l'ID de la ressource à laquelle vous êtes connecté.  </dd>
</dl>

**Valeurs renvoyées**

<dl>	
    <dt>SESSION_ID</dt>
    <dd>ID de la session active.</dd>
	   
    <dt>ID de ressource</dt>
    <dd>ID de la ressource pour laquelle la session est valide.</dd>

    <dt>CreateTime</dt>
    <dd>Horodatage correspondant à la date et à l'heure de création de la session.</dd>

    <dt>AccessTime</dt>
    <dd>Horodatage indiquant quand la session a été utilisée pour la dernière fois.</dd>
</dl>
 
**Exemple**

```
ibmcloud logging sessions
Listing sessions of resource: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx ...

ID                                     Space                                  CreateTime                       AccessTime   
1ef776d1-4d25-4297-9693-882606c725c8   xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx   2017-11-16T11:52:06.376125207Z   2017-11-16T11:52:06.376125207Z   
Listed the sessions of resource xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 
```
:{ screen}


## ibmcloud logging session-show
{: #session_show}

Affiche le statut d'une session unique.

```
ibmcloud logging session-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] SESSION_ID

```
{: codeblock}

**Paramètres**

<dl>
   <dt>-r,--resource-type RESOURCE_TYPE</dt>
      <dd>(Facultatif) Définit le type de ressource. Les valeurs admises sont *space*, *account* et *org*. </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
      <dd>(Facultatif) Pour cette zone, définissez l'ID d'un espace, d'une organisation ou d'un compte. <br>Par défaut, si vous ne spécifiez pas ce paramètre, la commande utilise l'ID de la ressource à laquelle vous êtes connecté.  </dd>
</dl>

**Arguments**

<dl>
   <dt>SESSION_ID</dt>
   <dd>ID de la session active sur laquelle vous souhaitez obtenir des informations.</dd>
</dl>

**Exemple**

Pour afficher les détails d'une session avec l'ID de session *cI6hvAa0KR_tyhjxZZz9Uw==*, exécutez la commande suivante :

```
ibmcloud logging session-show cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}

## ibmcloud logging token-get
{: #tokenget}

Renvoie le jeton de journalisation qui est requis pour l'envoi des données de journal à {{site.data.keyword.loganalysisshort}}.

```
ibmcloud logging token-get [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID]
```
{: codeblock}

**Paramètres**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facultatif) Définit le type de ressource vers lequel vous prévoyez d'envoyer les données de journal. Les valeurs admises sont *space*, *account* et *org*.
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facultatif) Pour cette zone, définissez l'ID d'un espace, d'une organisation ou d'un compte. <br>Par défaut, si vous ne spécifiez pas ce paramètre, la commande utilise l'ID de la ressource à laquelle vous êtes connecté. 
  </dd>
</dl>


**Exemple**

```
ibmcloud logging token-get -r space -i js7ydf98-8682-430d-bav4-36b712341744
Getting log token of resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Tenant Id                              Logging Token   
js7ydf98-8682-430d-bav4-36b712341744   xxxxxxxxxx   
```
{: screen}


## ibmcloud logging log-show
{: #status}

Renvoie des informations sur les journaux qui sont collectés dans un compte ou dans un espace {{site.data.keyword.Bluemix_notm}}.

```
ibmcloud logging log-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-l, --list-type-detail]
```
{: codeblock}

* Lorsque le type de ressource n'est pas spécifié, la commande renvoie les détails de la ressource à laquelle vous êtes connecté.
* Si vous spécifiez un type de ressource, vous devez spécifier l'ID de ressource.
* La commande ne renvoie des informations que pour les deux dernières semaines de journaux qui sont stockés dans le composant Log Collection lorsque les dates de début et de fin ne sont pas spécifiées.

**Paramètres**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(Facultatif) Définit le type de ressource. Les valeurs admises sont *space*, *account* et *org*.
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(Facultatif) Pour cette zone, définissez l'ID d'un espace, d'une organisation ou d'un compte. <br>Par défaut, si vous ne spécifiez pas ce paramètre, la commande utilise l'ID de la ressource à laquelle vous êtes connecté. 
  </dd>
  
  <dt>-s, --start START_DATE</dt>
  <dd>(Facultatif) Définit la date de début en temps universel coordonné (TUC) : *AAAA-MM-JJ*, par exemple `2006-01-02`. <br>La valeur par défaut correspond aux
deux semaines précédant la date du jour.
  </dd>
  
  <dt>-e, --end END_DATE</dt>
  <dd>(Facultatif) Définit la date de fin en temps universel coordonné (TUC) : *AAAA-MM-JJ*, par exemple `2006-01-02`. <br>La valeur par défaut est la
date en cours.
  </dd>
  
  <dt>-t, --type, LOG_TYPE</dt>
  <dd>(Facultatif) Définit le type de journal. <br>Par exemple, *syslog* est un type de journal. <br>La valeur par défaut est un astérisque (*). <br>Vous pouvez spécifier plusieurs types de journaux en séparant chacun d'eux par une virgule, par exemple *log_type_1,log_type_2,log_type_3*.
  </dd>
  
  <dt>-l, --list-type-detail</dt>
  <dd>(Facultatif) Définissez ce paramètre pour répertorier chaque type de journal individuellement.
  </dd>
</dl>


**Exemple**

```
ibmcloud logging log-show
Showing log status of resource: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx ...

Date         Size        Count    Searchable   Types   
2017-11-07   1878197     1333     None         default   
2017-11-13   201653512   179391   All          default,linux_syslog   
2017-11-14   32134119    30425    All          default,linux_syslog   
2017-11-15   303901156   269689   All          linux_syslog,default   
2017-11-16   107253679   96648    All          default,linux_syslog   
```
{: screen}

```
 ibmcloud logging log-show -l
Showing log status of resource: cedc73c5-6d55-4193-a9de-378620d6fab5 ...

Date         Size        Count    Searchable   Type   
2017-11-14   30146764    26611    true         default   
2017-11-14   1987355     3814     true         linux_syslog   
2017-11-15   303004895   267890   true         default   
2017-11-15   896261      1799     true         linux_syslog   
2017-11-16   107918249   96278    true         default   
2017-11-16   912890      1794     true         linux_syslog   
```
{: screen}
