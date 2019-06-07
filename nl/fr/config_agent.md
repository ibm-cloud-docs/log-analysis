---

copyright:
  years:  2018, 2019
lastupdated: "2019-05-01"

keywords: LogDNA, IBM, Log Analysis, logging, config agent

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

# Configuration d'un agent LogDNA
{: #config_agent}

L'agent LogDNA est chargé de la collecte et du transfert des journaux vers votre instance {{site.data.keyword.la_full_notm}}. Après avoir mis à disposition une instance {{site.data.keyword.la_full}}, vous devez configurer un agent LogDNA pour chaque source de journal que vous voulez surveiller.
{:shortdesc}

* L'agent LogDNA s'authentifie à l'aide de la clé d'ingestion LogDNA et ouvre un socket sécurisé Web sur les serveurs d'ingestion {{site.data.keyword.la_full_notm}}. 
* Par défaut, l'agent surveille tous les fichiers ayant l'extension *.log* et les fichiers sans extension qui se trouvent dans */var/log/*.
* L'agent suit les nouvelles données de journal et recherche les nouveaux fichiers ajoutés aux répertoires de journalisation qu'il surveille.

Vous pouvez configurer les paramètres suivants pour l'agent LogDNA : 

| Paramètre | Description |
|-----------|-------------|
| `tags`    | Définit des étiquettes afin de regrouper automatiquement des hôtes en groupes dynamiques. |
| `logdir`  | Définit des chemins d'accès personnalisés que vous voulez que l'agent surveille. </br>Séparez les différents chemins par des virgules. Vous pouvez utiliser des modèles glob. Vous pouvez configurer des fichiers spécifiques. Entrez des modèles glob en utilisant des guillemets. |
| `exclude` | Définit les fichiers que vous ne voulez pas que l'agent LogDNA surveille. **Remarque :** ces fichiers peuvent se trouver dans n'importe lequel des chemins définis à l'aide du paramètre logdir. </br>Séparez les différents fichiers par des virgules. Vous pouvez utiliser des modèles glob. Vous pouvez configurer des fichiers spécifiques. |
| `exclude_regex` | Définit des modèles d'expression régulière pour filtrer toutes les lignes qui correspondent au modèle. N'incluez aucune barre oblique (`/`) de début ni de fin. |
| `hostname` | Définit le nom d'hôte. Cette valeur se substitue au nom d'hôte du système d'exploitation. |
| `autoupdate` | Défini sur `1` pour mettre l'agent automatiquement à jour lorsque la définition de l'agent du référentiel public est mise à jour. Défini sur `0` pour désactiver cette fonction. |  
{: caption="Tableau 1. Paramètres de personnalisation d'un agent LogDNA" caption-side="top"} 



## Configuration d'un agent LogDNA sur un cluster Kubernetes à l'aide d'un script
{: #config_agent_kube_script}

Pour configurer votre cluster Kubernetes de manière à envoyer des journaux à votre instance {{site.data.keyword.la_full_notm}}, vous devez installer un pod *logdna-agent* sur chaque noeud de votre cluster. L'agent LogDNA lit les fichiers journaux depuis le pod où il est installé et envoie les données des journaux à votre instance LogDNA.

Pour configure votre cluster Kubernetes de manière à envoyer les journaux à votre instance LogDNA, procédez comme suit à partir de la ligne de commande :

1. Ouvrez un terminal pour vous connecter à {{site.data.keyword.cloud_notm}}.

   ```
   ibmcloud login -a cloud.ibm.com
   ```
   {: pre}

   Sélectionnez le compte où vous avez mis l'instance {{site.data.keyword.la_full_notm}} à disposition.

2. Définissez le cluster où vous voulez configurer la journalisation en tant que contexte pour cette session.

   ```
   ibmcloud ks cluster-config <cluster_name_or_ID>
   ```
   {: pre}

   Une fois les fichiers de configuration téléchargés, une commande, qui permet de définir le chemin vers le fichier de configuration Kubernetes local en tant que variable d'environnement s'affiche. Copiez et collez la commande qui s'affiche sur votre terminal pour définir la variable d'environnement `KUBECONFIG`.

3. Créez une valeur confidentielle (secret) Kubernetes pour stocker votre clé d'ingestion logDNA pour votre instance de service. La clé d'ingestion LogDNA permet d'ouvrir un socket Web sécurisé sur le serveur d'ingestion logDNA et d'authentifier l'agent de journalisation auprès du service {{site.data.keyword.la_full_notm}}.

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<logDNA_ingestion_key>
    ```
    {: pre}

4. Créez un ensemble de démons Kubernetes pour déployer l'agent LogDNA sur chaque noeud worker de votre cluster Kubernetes. L'agent LogDNA collecte les journaux ayant l'extension `*.log` et les fichiers sans extension stockés dans le répertoire `/var/log` de votre pod. Par défaut, les journaux sont collectés à partir de tous les espaces de nom, y compris `kube-system`, et automatiquement envoyés au service {{site.data.keyword.la_full_notm}}.

    <table>
      <caption>Commandes par région</caption>
      <tr>
        <th>Emplacement</th>
        <th>Commande</th>
      </tr>
      <tr>
        <td>`US-South`</td>
        <td>`kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml`</td>
      </tr>
      <tr>
        <td>`EU-DE`</td>
        <td>`kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-eu-de.yaml`</td>
      </tr>
    </table>

5. Vérifiez que l'agent LogDNA est correctement déployé. 

   ```
   kubectl get pods
   ```
   {: pre}
   

Le déploiement a abouti si vous voyez un ou plusieurs pods LogDNA.
* **Le nombre de pods LogDNA est égal au nombre de noeuds worker dans votre cluster.** 
* Tous les pods doivent être à l'état `Running`.
* *Stdout* et *stderr* sont automatiquement collectés et envoyés à partir de tous les conteneurs. Les données de journal incluent les journaux d'application et les journaux d'agent. 
* Par défaut, le pod d'agent LogDNA qui s'exécute sur un noeud worker collecte les journaux à partir de tous les espaces de noms sur ce noeud, y compris les journaux kube-system.



## Ajout d'étiquettes à un agent LogDNA sur un cluster Kubernetes
{: #config_agent_kube_tags}

Pour ajouter des étiquettes, procédez comme suit :

1. Configurez l'environnement de cluster. Exécutez les commandes suivantes :

    Commencez par vous procurer la commande de définition de la variable d'environnement et téléchargez les fichiers de configuration Kubernetes.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    Une fois les fichiers de configuration téléchargés, une commande s'affiche ; elle vous permet de définir le chemin vers le fichier de configuration Kubernetes local en tant que variable d'environnement.

    Ensuite, copiez et collez la commande affichée sur votre terminal pour définir la variable d'environnement KUBECONFIG.

2. Vérifiez la stratégie de mise à jour du DaemonSet. Puis déterminez si vous voulez utiliser *kubectl apply* ou *kubectl edit* pour modifier le fichier de configuration de l'agent.

    Pour vérifier la stratégie de mise à jour, exécutez la commande suivante :

    ```
    kubectl get ds/logdna-agent -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'
    ```
    {: pre}

    Si la stratégie de mise à jour est définie sur *OnDelete* ou si le fichier de configuration est géré par l'intermédiaire d'un système de contrôle de version, mettez à jour votre fichier de configuration local et appliquez les modifications à l'agent LogDNA à l'ide de *kubectl apply*.

    Si la stratégie de mise à jour est définie sur *RollingUpdate*, vous pouvez mettre à jour et appliquer les modifications à l'agent LogDNA à l'aide de *kubectl edit*.

3. Editez le fichier `logdna-agent-configmap.yaml`. 

    Mettez à jour le fichier de configuration en modifiant la copie locale. **Remarque :** vous pouvez également générer le fichier de configuration de l'agent en exécutant la commande suivante :

    ```
    kubectl get daemonset logdna-agent -o=yaml > prod-logdna-agent-ds.yaml
    ```
    {: codeblock}

    Sinon, mettez à jour le fichier de configuration à l'aide de *kubectl edit*.

    ```
    kubectl edit daemonset logdna-agent
    ```
    {: codeblock}

4. Effectuez les modifications. Ajoutez la section **LOGDNA_TAGS**.

    ```
    - name: LOGDNA_TAGS
        value: tag1,tag2,tag3
    ```
    {: codeblock}

    Par exemple, la section suivante montre où ajouter les étiquettes dans le fichier de configuration :

    ```
    apiVersion: extensions/v1beta1
    kind: DaemonSet
    metadata:
      name: logdna-agent
    spec:
      template:
        metadata:
          labels:
            app: logdna-agent
        spec:
          containers:
          - name: logdna-agent
            image: logdna/logdna-agent:latest
            imagePullPolicy: Always
            env:
            - name: LOGDNA_AGENT_KEY
              valueFrom:
                 secretKeyRef:
                  name: logdna-agent-key
                  key: logdna-agent-key
            - name: LDAPIHOST
              value: api.us-south.logging.cloud.ibm.com
            - name: LDLOGHOST
              value: logs.us-south.logging.cloud.ibm.com
            - name: LOGDNA_PLATFORM
              value: k8s
            - name: LOGDNA_TAGS
              value: tag1,tag2,tag3
    ```
    {: screen}

5. Appliquez les modifications de configuration si vous éditez le fichier en local. 

    ```
    kubectl apply -f prod-logdna-agent-ds.yaml
    ```
    {: codeblock}
    
    **Remarque :** si vous utilisez *kubectl edit*, les modifications sont appliquées automatiquement lorsque vous les sauvegardez.


## Configuration d'un agent LogDNA sur Linux Ubuntu ou Debian
{: #config_agent_linux}

Pour configurer votre serveur Ubuntu de manière à envoyer des journaux à votre instance {{site.data.keyword.la_full_notm}}, vous devez installer un agent `logdna-agent`. L'agent LogDNA lit les fichiers journaux depuis */var/log* et envoie les données des journaux à votre instance LogDNA.

Pour configurer votre serveur Ubuntu de manière à envoyer des journaux à votre instance LogDNA, procédez comme suit à partir d'un terminal Ubuntu :

1. Installez l'agent LogDNA. Exécutez les commandes suivantes :

    ```
    echo "deb https://repo.logdna.com stable main" | sudo tee /etc/apt/sources.list.d/logdna.list 
    ```
    {: codeblock}

    ```
    wget -O- https://repo.logdna.com/logdna.gpg | sudo apt-key add - 
    ```
    {: codeblock}

    ```
    sudo apt-get update
    ```
    {: codeblock}

    ```
    sudo apt-get install logdna-agent < "/dev/null"
    ```
    {: codeblock}

2. Définissez la clé d'ingestion que doit utiliser l'agent LogDNA pour envoyer les journaux à l'instance {{site.data.keyword.la_full_notm}}.  

    ```
    sudo logdna-agent -k INGESTION_KEY
    ```
    {: codeblock}

    Où INGESTION_KEY contient la clé d'ingestion active pour l'instance {{site.data.keyword.la_full_notm}} où vous configurez le réacheminement des journaux.

3. Définissez le noeud final d'authentification. L'agent LogDNA utilise cet hôte pour s'authentifier et obtenir le jeton pour réacheminer les journaux.

    <table>
      <caption>Commandes par région</caption>
      <tr>
        <th>Emplacement</th>
        <th>Commande</th>
      </tr>
      <tr>
        <td>`US-South`</td>
        <td>`    sudo logdna-agent -s LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com
    `</td>
      </tr>
      <tr>
        <td>`EU-DE`</td>
        <td>`sudo logdna-agent -s LOGDNA_APIHOST=api.eu-de.logging.cloud.ibm.com`</td>
      </tr>
    </table>

4. Définissez le noeud final d'ingestion.

    <table>
      <caption>Commandes par région</caption>
      <tr>
        <th>Emplacement</th>
        <th>Commande</th>
      </tr>
      <tr>
        <td>`US-South`</td>
        <td>`    sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com
    `</td>
      </tr>
      <tr>
        <td>`EU-DE`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.eu-de.logging.cloud.ibm.com`</td>
      </tr>
    </table>

5. Définissez d'autre chemin d'accès aux journaux à surveiller. Exécutez la commande suivante : 

    ```
    sudo logdna-agent -d /path/to/log/folders
    ```
    {: codeblock}

    Par défaut, **/var/log** est surveillé.

6. Configurez éventuellement l'agent LogDNA pour marquer vos hôtes. 


## Ajout d'étiquettes à un agent LogDNA sur Linux Ubuntu ou Debian
{: #config_agent-linux_tags}
 

Pour ajouter d'autres étiquettes à l'agent LogDNA, procédez comme suit :

1. Vérifiez que l'agent LogDNA s'exécute.

2. Ajoutez une ou plusieurs étiquettes.

    ```
    sudo logdna-agent -t TAG1,TAG2 
    ```
    {: codeblock}


Vous pouvez également éditer le fichier de configuration de LogDNA et ajouter des étiquettes. Le fichier de configuration se trouve dans */etc/logdna.conf*.

1. Editez le fichier.

    ```
    sudo update-rc.d logdna-agent defaults
    ```
    {: codeblock}

2. Ajoutez des étiquettes.

3. Redémarrez l'agent LogDNA.

    ``` 
    sudo /etc/init.d/logdna-agent start
    ```
    {: codeblock}














