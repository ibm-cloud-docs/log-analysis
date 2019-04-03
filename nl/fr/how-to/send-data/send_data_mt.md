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

# Envoi de données locales dans un espace dans IBM Cloud
{: #send_data_mt}

Pour envoyer des données de journal au service {{site.data.keyword.loganalysisshort}}, vous pouvez configurer un réexpéditeur Logstash à service partagé (mt-logstash-forwarder). 
{: shortdesc}

Procédez comme suit pour envoyer des données de journal dans un espace dans {{site.data.keyword.Bluemix_notm}} :

## Configuration requise
{: #prereqs1}

* Un {{site.data.keyword.Bluemix_notm}}ID pour la connexion à {{site.data.keyword.Bluemix_notm}}.
* Un ID utilisateur qui dispose de droits permettant d'utiliser le service {{site.data.keyword.loganalysisshort}} dans un espace. Pour plus d'informations, voir [Sécurité](/docs/services/CloudLogAnalysis/security_ov.html#security_ov).
* L'interface de ligne de commande {{site.data.keyword.loganalysisshort}} installée dans votre environnement local.
* Le service {{site.data.keyword.loganalysisshort}} mis à disposition dans un espace de votre compte avec un plan autorisant l'ingestion de journaux.


## Etape 1 : Obtention du jeton de journalisation
{: #get_logging_auth_token}

Effectuez les étapes suivantes depuis une session de terminal dans laquelle l'interface de ligne de commande {{site.data.keyword.loganalysisshort}} est installée :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Exécutez la commande `ibmcloud logging token-get`. 

    ```
    ibmcloud logging token-get
    ```
    {: codeblock}

    La commande renvoie le jeton de journalisation.
    
    Exemple

    ```
    ibmcloud logging token-get
    Getting log token of resource: 93f54jh6-b5f5-46c9-9f0e-kfeutpldnbcf ...
    OK

    Tenant Id                              Logging Token   
    93f54jh6-b5f5-46c9-9f0e-kfeutpldnbcf   oT98_abcdefz   
    ```
    {: screen}

    où *Tenant Id* est l'identificateur global unique de l'espace où vous prévoyez d'envoyer les journaux.


## Etape 2 : Configuration de mt-logstash-forwarder
{: #configure_mt_logstash_forwarder}

Procédez comme suit pour configurer mt-logstash-forwarder dans l'environnement depuis lequel vous prévoyez d'envoyer des journaux au service {{site.data.keyword.loganalysisshort}} :

1.	Connectez-vous en tant que superutilisateur. 

    ```
    sudo -s
    ```
    {: codeblock}
    
2.	Installez le package NTP (Network Time Protocol) pour synchroniser l'heure des journaux. 

    Par exemple, pour un système Ubuntu, vérifiez si `timedatectl status` affiche *Network time on: yes*. Si tel est le cas, votre système Ubuntu est déjà configuré pour utiliser ntp et vous pouvez ignorer cette étape.
    
    ```
    # timedatectl status
    Local time: Mon 2017-06-12 03:01:22 PDT
    Universal time: Mon 2017-06-12 10:01:22 UTC
    RTC time: Mon 2017-06-12 10:01:22
    Time zone: America/Los_Angeles (PDT, -0700)
    Network time on: yes
    NTP synchronized: yes
    RTC in local TZ: no
    ```
    {: screen}
    
    Effectuez les étapes suivantes pour installer ntp sur un système Ubuntu :

    1.	Exécutez la commande suivante pour mettre à jour les packages : 

        ```
        apt-get update
        ```
        {: codeblock}
        
    2.	Exécutez la commande suivante pour installer le package ntp : 

        ```
        apt-get install ntp
        ```
        {: codeblock}
        
    3.	Exécutez la commande suivante pour installer le package ntpdate : 
    
        ```
        apt-get install ntpdate
        ```
        {: codeblock}
        
    4.	Exécutez la commande suivante pour arrêter le service : 
        
        ```
        service ntp stop
        ```
        {: codeblock}
        
    5.	Exécutez la commande suivante pour synchroniser l'horloge système : 
    
        ```
        ntpdate -u 0.ubuntu.pool.ntp.org
        ```
        {: codeblock}
        
        Le résultat confirme que l'heure est réglée, par exemple :
        
        ```
        4 May 19:02:17 ntpdate[5732]: adjust time server 50.116.55.65 offset 0.000685 sec
        ```
        {: screen}
        
    6.	Exécutez la commande suivante pour démarrer ntpd à nouveau : 
    
        ```
        service ntp start
        ```
        {: codeblock}
    
        Le résultat confirme que le service démarre.

    7.	Exécutez la commande suivante afin d'activer le service ntpd pour démarrer automatiquement après une panne ou un réamorçage : 
    
        ```
        service ntp enable
        ```
        {: codeblock}
        
        Le résultat qui s'affiche est une liste de commandes qui peuvent être utilisées pour gérer le service ntpd, par exemple :
        
        ```
        Usage: /etc/init.d/ntpd {start|stop|status|restart|try-restart|force-reload}
        ```
        {: screen}

3. Ajoutez le référentiel du service {{site.data.keyword.loganalysisshort}} dans le gestionnaire de package du système. Exécutez la commande suivante :

    ```
    wget -O - https://downloads.opvis.bluemix.net/client/IBM_Logmet_repo_install.sh | bash
    ```
    {: codeblock}

4. Installez et configurez mt-logstash-forwarder pour envoyer des journaux de votre environnement à Log Collection. 

    1. Exécutez la commande suivante pour installer mt-logstash-forwarder :
    
        ```
        apt-get install mt-logstash-forwarder 
        ```
        {: codeblock}
        
    2. Créez le fichier de configuration mt-logstash-forwarder pour votre environnement. Ce fichier inclut des variables qui sont utilisées pour configurer mt logstash forwarder pour que le réexpéditeur pointe sur le service {{site.data.keyword.loganalysisshort}}.
    
       Editez le fichier `/etc/mt-logstash-forwarder/mt-lsf-config.sh`. Par exemple, vous pouvez utiliser l'éditeur vi :
               
       ```
       vi /etc/mt-logstash-forwarder/mt-lsf-config.sh
       ```
       {: codeblock}
        
       Pour que le réexpéditeur pointe sur le service {{site.data.keyword.loganalysisshort}}, ajoutez les variables suivantes au fichier **mt-lsf-config.sh** : 
         
       <table>
          <caption>Tableau 1. Liste des variables requises pour que le réexpéditeur pointe sur le service {{site.data.keyword.loganalysisshort}} sur une machine virtuelle </caption>
          <tr>
            <th>Nom de la variable</th>
            <th>Description</th>
          </tr>
          <tr>
            <td>LSF_INSTANCE_ID</td>
            <td>ID de votre machine virtuelle, par exemple *MyTestVM*. </td>
          </tr>
          <tr>
            <td>LSF_TARGET</td>
            <td>URL cible. Pour la liste des URL d'ingestion, voir [URL d'ingestion](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls). Par exemple, définissez la valeur **ingest.logging.ng.bluemix.net:9091** pour envoyer des journaux dans la région Sud des Etats-Unis. </td>
          </tr>
          <tr>
            <td>LSF_TENANT_ID</td>
            <td>ID de l'espace dans lequel le service {{site.data.keyword.loganalysisshort}} est prêt à collecter les journaux que vous envoyez dans {{site.data.keyword.Bluemix_notm}}. <br>Utilisez la valeur obtenue à l'étape 1.</td>
          </tr>
          <tr>
            <td>LSF_PASSWORD</td>
            <td>Jeton de journalisation. <br>Utilisez la valeur obtenue à l'étape 1.</td>
          </tr>
          <tr>
            <td>LSF_GROUP_ID</td>
            <td>Définissez une balise personnalisée permettant de regrouper des journaux connexes.</td>
          </tr>
       </table>
        
       Par exemple, recherchez dans l'exemple de fichier suivant un espace ayant l'ID *7d576e3b-170b-4fc2-a6c6-b7166fd57912* dans la région Royaume-Uni :
        
       ```
       # more mt-lsf-config.sh 
       LSF_INSTANCE_ID="myhelloapp"
       LSF_TARGET="ingest.logging.ng.bluemix.net:9091"
       LSF_TENANT_ID="7d576e3b-170b-4fc2-a6c6-b7166fd57912"
       LSF_PASSWORD="oT98_abcdefz"
       LSF_GROUP_ID="Group1"
       ```
       {: screen}
        
    3. Démarrez mt-logstash-forwarder. 
    
       ```
       service mt-logstash-forwarder start
       ```
       {: codeblock}
                
Par défaut, le réexpéditeur surveille uniquement syslog. Vos journaux sont disponibles dans Kibana pour l'analyse.
        

## Etape 3 : Spécification de fichiers journaux additionnels
{: #add_logs}

Par défaut, seul le fichier /var/log/syslog est contrôlé par le réexpéditeur. Vous pouvez ajouter des fichiers de configuration supplémentaires dans le répertoire `/etc/mt-logstash-forwarder/conf.d/syslog.conf/` afin que le réexpéditeur les contrôle également. 

Exécutez les étapes suivantes afin d'ajouter un fichier de configuration pour une application qui s'exécute dans votre environnement :

1.	Copiez le fichier `/etc/mt-logstash-forwarder/conf.d/syslog.conf`. 

    **Astuce :** n'éditez pas le fichier syslog.conf pour ajouter des fichiers journaux.
    
    Par exemple, sur un système Ubuntu, exécutez la commande suivante :
    
    ```
    cp /etc/mt-logstash-forwarder/conf.d/syslog.conf /etc/mt-logstash-forwarder/conf.d/myapp.conf
    ```
    {: codeblock}
        
2.	Editez le fichier *myapp.conf* dans un éditeur de texte et mettez le à jour pour inclure les journaux d'application à contrôler. Incluez le type de journal de chaque journal d'application. Supprimez les exemples qui ne sont pas utilisés.

3.	Redémarrez mt-logstash-forwarder. 

     Redémarrez le service mt-logstash-forwarder. Exécutez la commande suivante :
    
    ```
    service mt-logstash-forwarder restart
    ```
    {: codeblock}

**Exemple**

Pour inclure le flux de sortie standard (stdout) ou d'erreur standard (stderr) d'une application hello, redirigez le flux de sortie standard (stdout) ou d'erreur standard (stderr) dans un fichier journal. Créez un fichier de configuration de réexpéditeur pour l'application. Ensuite, redémarrez mt-logstash-forwarder.

1.	Copiez le fichier `/etc/mt-logstash-forwarder/conf.d/syslog.conf`. 

    ```
    cp /etc/mt-logstash-forwarder/conf.d/syslog.conf /etc/mt-logstash-forwarder/conf.d/myapp.conf
    ```
    {: codeblock}
    
2. Editez le fichier de configuration *myapp.conf*.

    Pour pouvoir effectuer une recherche par zone JSON dans Kibana lors de l'ingestion d'un journal, activez l'analyse syntaxique JSON. Associez `is_json` à la valeur true dans le fichier de configuration pour des chemins de fichier spécifiques. Pour les fichiers journaux configurés ainsi, les lignes du journal doivent respecter le format de blocs JSON et être séparées par un retour chariot. Le service mt-logstash-forwarder consomme alors ces zones JSON en tant que zones de recherche Kibana. Les noms de zone JSON incluent un suffixe basé sur le type de la zone.
    
    ```
    {
    "files": [
         # other file configurations omitted...
            {
            "paths": [ "/var/log/myhelloapp.log" ],
            "fields": { "type": "helloapplog" },
            "is_json": true
            }
         ]
     }
     ```
     {: screen}
