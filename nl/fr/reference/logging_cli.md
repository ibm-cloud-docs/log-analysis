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

# Interface de ligne de commande d'IBM Cloud Log Analysis (plug-in CF)
{: #logging_cli}

L'interface de ligne de commande {{site.data.keyword.loganalysislong}} est un plug-in qui permet de gérer les journaux des ressources de cloud s'exécutant dans un espace d'une
organisation {{site.data.keyword.Bluemix}}.
{: shortdesc}

**Prérequis**
* Avant d'exécuter les commandes de journalisation, connectez-vous à {{site.data.keyword.Bluemix_notm}} avec la commande `ibmcloud login` pour générer un jeton d'accès {{site.data.keyword.Bluemix_short}} et authentifier votre session. Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

Pour savoir comment utiliser l'interface de ligne de commande {{site.data.keyword.loganalysisshort}},
voir [Gestion des journaux](/docs/services/CloudLogAnalysis/log_analysis_ov.html#log_analysis_ov).

<table>
  <caption>Commandes de gestion des journaux</caption>
  <tr>
    <th>Commande</th>
    <th>Quant l'utiliser</th>
  </tr>
  <tr>
    <td>[ibmcloud cf logging](#base)</td>
    <td>Utilisez cette commande pour obtenir des informations sur l'interface de ligne de commande, comme la version ou la liste des commandes.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging auth](#auth)</td>
    <td>Utilisez cette commande pour obtenir le jeton de journalisation que vous pouvez utiliser pour envoyer des journaux au service {{site.data.keyword.loganalysisshort}}.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging delete](#delete)</td>
    <td>Utilisez cette commande pour supprimer des journaux stockés dans la collecte des journaux.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging download (bêta)](#download)</td>
    <td>Utilisez cette commande pour télécharger des journaux depuis le composant Log Collection dans un fichier local ou pour diriger les journaux vers un autre programme tel qu'Elastic Stack. </td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging help](#help)</td>
    <td>Utilisez cette commande pour obtenir de l'aide au sujet de l'utilisation de l'interface de ligne de commande ainsi que la liste de toutes les commandes.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging option](#option)</td>
    <td>Utilisez cette commande pour afficher ou définir la durée de conservation des journaux qui sont disponibles dans un espace ou sur un compte.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging session create (bêta)](#session_create1)</td>
    <td>Utilisez cette commande pour créer une nouvelle session.</td>
  <tr>
  <tr>
    <td>[ibmcloud cf logging session delete (bêta)](#session_delete1)</td>
    <td>Utilisez cette commande pour supprimer une session.</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging session list (bêta)](#session_list1)</td>
    <td>Utilisez cette commande pour afficher la liste des sessions actives et leurs ID.</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging session show (bêta)](#session_show1)</td>
    <td>Utilisez cette commande pour afficher le statut d'une session unique.</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging status](#status1)</td>
    <td>Utilisez cette commande pour obtenir des informations sur les journaux qui sont collectés dans un espace ou sur un compte.</td>
  </tr>
  </table>


## ibmcloud cf logging
{: #base1}

Fournit des informations sur la version de l'interface de ligne de commande et sur son mode d'utilisation.

```
ibmcloud cf logging [parameters]
```
{: codeblock}

**Paramètres**

<dl>
<dt>--help, -h</dt>
<dd>Définissez ce paramètre pour afficher la liste des commandes ou pour obtenir de l'aide sur une commande.
</dd>

<dt>--version, -v</dt>
<dd>Définissez ce paramètre pour imprimer la version de l'interface de ligne de commande.</dd>
</dl>

**Exemples**

Pour obtenir la liste des commandes, exécutez la commande suivante :

```
ibmcloud cf logging --help
```
{: codeblock}

Pour obtenir la version de l'interface de ligne de commande, exécutez la commande suivante :

```
ibmcloud cf logging --version
```
{: codeblock}


## ibmcloud cf logging auth
{: #auth}

Renvoie un jeton de journalisation que vous pouvez utiliser pour envoyer des journaux au service {{site.data.keyword.loganalysisshort}}. 

**Remarque :** le jeton n'expire pas.

```
ibmcloud cf logging auth
```
{: codeblock}

**renvoie**

<dl>
  <dt>Un jeton de journalisation</dt>
  <dd>Par exemple, `jec8BmipiEZc`.
  </dd>
  
  <dt>L'ID d'organisation</dt>
  <dd>Identificateur global unique de l'organisation {{site.data.keyword.Bluemix_notm}} où vous êtes connecté.
  </dd>
  
  <dt>L'ID d'espace</dt>
  <dd>Identificateur global unique de l'espace dans l'organisation où vous êtes connecté.
  </dd>
</dl>

## ibmcloud cf logging delete
{: #delete2}

Supprime les journaux stockés dans Log Collection.

```
ibmcloud cf logging delete [parameters]
```
{: codeblock}

**Paramètres**

<dl>
  <dt>--start value, -s value</dt>
  <dd>(Facultatif) Définit la date de début en temps universel coordonné (TUC) : *AAAA-MM-JJ*, par exemple `2006-01-02`. <br>La valeur par défaut correspond aux
deux semaines précédant la date du jour.
  </dd>
  
  <dt>--end value, -e value</dt>
  <dd>(Facultatif) Définit la date de fin en temps universel coordonné (TUC) : *AAAA-MM-JJ*. <br>Le format TUC de la date est **AAAA-MM-JJ**,
par exemple `2006-01-02`. <br>La valeur par défaut est la date en cours.
  </dd>
  
  <dt>--type value, -t value</dt>
  <dd>(Facultatif) Définit le type de journal. <br>Par exemple, *syslog* est un type de journal. <br>La valeur par défaut est **\***. <br>Vous
pouvez spécifier plusieurs types de journaux en les séparant par une virgule, par exemple **log_type_1,log_type_2,log_type_3*.
  </dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>(Facultatif) Définit l'étendue des informations de journal fournies au niveau du compte. <br>Si ce paramètre n'est pas spécifié, la valeur par défaut est définie pour fournir des
informations de journal sur l'espace en cours uniquement.
  </dd>
</dl>

**Exemple**

Pour supprimer les journaux du type *linux_syslog* pour le 25 mai 2017, exécutez la commande suivante :
```
ibmcloud cf logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
```
{: codeblock}



## ibmcloud cf logging download (bêta)
{: #download4}

Télécharge les journaux de Log Collection vers un fichier local ou dirige les journaux vers un autre programme, tel qu'Elastic Stack. 

**Remarque :** pour télécharger les fichiers, vous devez d'abord créer une session. Une session définit quels journaux doivent être téléchargés en fonction de la plage
de dates, du type de journal et du type de compte. Les journaux sont téléchargés dans le contexte d'une session. Pour plus d'informations, voir [ibmcloud cf logging session create (bêta)](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_create1).

```
ibmcloud cf logging download [parameters] [arguments]
```
{: codeblock}

**Paramètres**

<dl>
<dt>--output value, -o value</dt>
<dd>(Facultatif) Définit le chemin et le nom du fichier de sortie local où les journaux sont téléchargés. <br>La valeur par défaut est un trait d'union (-). <br>Pour ce paramètre, définissez la valeur par défaut pour que les journaux soient générés dans la sortie standard.</dd>
</dl>

**Arguments**

<dl>
<dt>session_ID</dt>
<dd>Associez cet argument à la valeur d'ID de session que vous obtenez lorsque vous exécutez la commande `ibmcloud cf logging session create`. Cette valeur indique quelle session utiliser lors du
téléchargement des journaux. <br>**Remarque :** la commande `ibmcloud cf logging session create` fournit les paramètres qui contrôlent quels sont les journaux qui sont téléchargés. </dd>
</dl>

**Remarque :** si vous exécutez à nouveau la même commande une fois que le téléchargement est terminé, cela n'aura aucun effet. Pour télécharger à nouveau les mêmes
données, vous devez utiliser un fichier différent ou une session différente.

**Exemples**

Sur un système Linux, pour télécharger les journaux dans un fichier appelé mylogs.gz, exécutez la commande suivante :

```
ibmcloud cf logging download -o mylogs.gz guBeZTIuYtreOPi-WMnbUg==
```
{: screen}

Pour télécharger des journaux dans Elastic Stack, exécutez la commande suivante :

```
ibmcloud cf logging download guBeZTIuYtreOPi-WMnbUg== | gunzip | logstash -f logstash.conf
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


## ibmcloud cf logging help
{: #help1}

Fournit des informations sur le mode d'utilisation d'une commande.

```
ibmcloud cf logging help [command]
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
ibmcloud cf logging help status
```
{: codeblock}


## ibmcloud cf logging option
{: #option}

Affiche ou change la durée de conservation pour les journaux qui sont disponibles dans un espace ou sur un compte. 

* La durée est définie en nombre de jours.
* La valeur par défaut est **-1**. 

**Remarque :** par défaut, tous les journaux sont stockés. Vous devez les supprimer manuellement à l'aide de la commande **delete**. Définissez une règle de conservation pour supprimer les journaux automatiquement.

```
ibmcloud cf logging option [parameters]
```
{: codeblock}

**Paramètres**

<dl>
<dt>--retention value, -r value</dt>
<dd>(Facultatif) Définit le nombre de jours de conservation. <br> La valeur par défaut est *-1* jour.</dd>

<dt>--at-account-level, -a </dt>
  <dd>(Facultatif) Définit le niveau de compte comme portée. <br>Si ce paramètre n'est pas spécifié, la valeur par défaut est *-1* pour l'espace en cours, c'est-à-dire l'espace auquel vous vous êtes connecté avec la commande `ibmcloud cf login`.
  </dd>
</dl>

**Exemples**

Afin d'afficher la durée de conservation en cours par défaut pour l'espace auquel vous êtes connecté, exécutez la commande suivante :

```
ibmcloud cf logging option
```
{: codeblock}

La sortie est :

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-ibmcloud cfgh436902a3 |        -1 |
+--------------------------------------+-----------+
```
{: screen}


Pour modifier la durée de conservation à 25 jours pour l'espace auquel vous êtes connecté, exécutez la commande suivante :

```
ibmcloud cf logging option -r 25
```
{: codeblock}

La sortie est :

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-ibmcloud cfgh436902a3 |        25 |
+--------------------------------------+-----------+
```
{: screen}


## ibmcloud cf logging session create (bêta)
{: #session_create1}

Crée une session.

**Remarque :** vous pouvez avoir jusqu'à 30 sessions simultanées dans un espace. La session est créée pour un utilisateur. Les sessions ne peuvent pas être partagées
entre les utilisateurs dans un espace.

```
ibmcloud cf logging session create [parameters]
```
{: codeblock}

**Paramètres**

<dl>
  <dt>--start value, -s value</dt>
  <dd>(Facultatif) Définit la date de début en temps universel coordonné (TUC) : *AAAA-MM-JJ*, par exemple `2006-01-02`. <br>La valeur par défaut correspond aux
deux semaines précédant la date du jour.
  </dd>
  
  <dt>--end value, -e value</dt>
  <dd>(Facultatif) Définit la date de fin en temps universel coordonné (TUC) : *AAAA-MM-JJ*, par exemple `2006-01-02`. <br>La valeur par défaut est la date en cours.
  </dd>
  
  <dt>--type value, -t value</dt>
  <dd>(Facultatif) Définit le type de journal. <br>Par exemple, *syslog* est un type de journal. <br>La valeur par défaut est un astérisque (*). <br>Vous pouvez spécifier plusieurs types de journaux en séparant chacun d'eux par une virgule, par exemple *log_type_1,log_type_2,log_type_3*.
  </dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>(Facultatif) Définit le niveau de compte comme portée. <br>Si ce paramètre n'est pas spécifié, la valeur par défaut est l'espace en cours uniquement, c'est-à-dire l'espace auquel vous vous êtes connecté avec la commande `ibmcloud cf login`.
  </dd>
</dl>

**Valeurs renvoyées**

<dl>
<dt>Access-Time</dt>
<dd>Horodatage indiquant quand la session a été utilisée pour la dernière fois.</dd>

<dt>Create-Time</dt>
<dd>Horodatage correspondant à la date et à l'heure de création de la session.</dd>

<dt>Date-Range</dt>
<dd>Indique les dates utilisées pour filtrer les journaux. Les journaux identifiés dans cette plage de dates peuvent être gérés via la session.</dd>

<dt>ID</dt>
<dd>ID de session.</dd>

<dt>Espace</dt>
<dd>ID de l'espace dans lequel la session est active.</dd>

<dt>Type-Account</dt>
<dd>Types de journaux qui sont téléchargés via la session.</dd>

<dt>Username</dt>
<dd>ID {{site.data.keyword.IBM_notm}} de l'utilisateur qui a créé la session.</dd>
</dl>


**Exemple**

Pour créer une session incluant les journaux compris entre le 20 mai 2017 et le 26 mai 2017 pour un type de journal *log*, exécutez la commande suivante :

```
ibmcloud cf logging session create -s 2017-05-20 -e 2017-05-26 -t log
```
{: screen}


## ibmcloud cf logging session delete (bêta)
{: #session_delete1}

Supprime une session, spécifiée par l'ID de session.

```
ibmcloud cf logging session delete [arguments]
```
{: codeblock}

**Arguments**

<dl>
<dt>session ID</dt>
<dd>ID de la session à supprimer. <br>Vous pouvez utiliser la commande `ibmcloud cf logging session list` pour obtenir tous les ID de session active.</dd>
</dl>

**Exemple**

Pour supprimer une session dont l'ID de session est *cI6hvAa0KR_tyhjxZZz9Uw==*, exécutez la commande suivante :

```
ibmcloud cf logging session delete cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}



## ibmcloud cf logging session list (bêta)
{: #session_list1}

Affiche la liste des sessions actives et leurs ID.

```
ibmcloud cf logging session list 
```
{: codeblock}

**Valeurs renvoyées**

<dl>
<dt>ID</dt>
<dd>ID de session.</dd>

<dt>SPACE</dt>
<dd>ID de l'espace dans lequel la session est active.</dd>

<dt>USERNAME</dt>
<dd>ID {{site.data.keyword.IBM_notm}} de l'utilisateur qui a créé la session.</dd>

<dt>CREATE-TIME</dt>
<dd>Horodatage correspondant à la date et à l'heure de création de la session.</dd>

<dt>ACCESS-TIME</dt>
<dd>Horodatage indiquant quand la session a été utilisée pour la dernière fois.</dd>
</dl>
 

## ibmcloud cf logging session show (bêta)
{: #session_show1}

Affiche le statut d'une session unique.

```
ibmcloud cf logging session show [arguments]
```
{: codeblock}

**Arguments**

<dl>
<dt>session_ID</dt>
<dd>ID de la session active sur laquelle vous souhaitez obtenir des informations.</dd>
</dl>

**Valeurs renvoyées**

<dl>
<dt>Access-Time</dt>
<dd></dd>

<dt>Create-Time</dt>
<dd>Horodatage correspondant à la date et à l'heure de création de la session.</dd>

<dt>Date-Range</dt>
<dd>Indique les dates utilisées pour filtrer les journaux. Les journaux identifiés dans cette plage de dates peuvent être gérés via la session.</dd>

<dt>ID</dt>
<dd>ID de session.</dd>

<dt>Espace</dt>
<dd>ID de l'espace dans lequel la session est active.</dd>

<dt>Type-Account</dt>
<dd>Types de journaux qui sont téléchargés via la session.</dd>

<dt>Username</dt>
<dd>ID {{site.data.keyword.IBM_notm}} de l'utilisateur qui a créé la session.</dd>
</dl>

**Exemple**

Pour afficher les détails d'une session dont l'ID est *cI6hvAa0KR_tyhjxZZz9Uw==*, exécutez la commande suivante :

```
ibmcloud cf logging session show cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}


## ibmcloud cf logging status
{: #status1}

Renvoie des informations sur les journaux qui sont collectés dans un espace ou sur un compte.

```
ibmcloud cf logging status [parameters]
```
{: codeblock}

**Paramètres**

<dl>
  <dt>--start value, -s value</dt>
  <dd>(Facultatif) Définit la date de début en temps universel coordonné (TUC) : *AAAA-MM-JJ*, par exemple `2006-01-02`. <br>La valeur par défaut correspond aux
deux semaines précédant la date du jour.
  </dd>
  
  <dt>--end value, -e value</dt>
  <dd>(Facultatif) Définit la date de fin en temps universel coordonné (TUC) : *AAAA-MM-JJ*, par exemple `2006-01-02`. <br>La valeur par défaut est la date en cours.
  </dd>
  
  <dt>--type value, -t value</dt>
  <dd>(Facultatif) Définit le type de journal. <br>Par exemple, *syslog* est un type de journal. <br>La valeur par défaut est un astérisque (*). <br>Vous pouvez spécifier plusieurs types de journaux en séparant chacun d'eux par une virgule, par exemple *log_type_1,log_type_2,log_type_3*.
  </dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>(Facultatif) Définit le niveau de compte comme portée. <br> **Remarque :** définissez cette valeur pour obtenir des informations relatives à un compte. <br>Si ce paramètre n'est pas spécifié, la valeur par défaut est l'espace en cours uniquement, c'est-à-dire l'espace auquel vous vous êtes connecté avec la commande `ibmcloud cf login`.
  </dd>
  
  <dt>--list-type-detail, -l</dt>
  <dd>(Facultatif) Définissez ce paramètre pour afficher le sous-total des types de journaux pour chaque jour.
  </dd>
</dl>

**Remarque :** la commande `ibmcloud cf logging status` ne renvoie des informations que pour les deux dernières semaines de journaux qui sont stockés dans Log Collection lorsque les dates de début et de fin ne sont pas spécifiées.


