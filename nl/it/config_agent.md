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

# Configurazione di un agent LogDNA
{: #config_agent}

L'agent LogDNA è responsabile della raccolta e dell'inoltro dei log alla tua istanza {{site.data.keyword.la_full_notm}}. Dopo che hai eseguito il provisioning di un'istanza di {{site.data.keyword.la_full}}, devi configurare un agent LogDNA per ciascuna origine log che desideri monitorare.
{:shortdesc}

* L'agent LogDNA esegue l'autenticazione utilizzando la chiave di inserimento LogDNA e apre un socket web sicuro ai server di inserimento {{site.data.keyword.la_full_notm}}. 
* Per impostazione predefinita, l'agent monitora tutti i file con l'estensione *.log* e i file senza estensione in */var/log/*.
* l'agent esegue l'accodamento per i nuovi dati di log e cerca i nuovi file aggiunti alle directory di registrazione monitorate dall'agent.

Puoi configurare i seguenti parametri mediante l'agent LogDNA: 

| Parametro | Descrizione |
|-----------|-------------|
| `tags`    | Definisci le tag per raggruppare gli host automaticamente in gruppi dinamici. |
| `logdir`  | Definisci i percorsi personalizzati che desideri siano monitorati dall'agent. </br>Separa più percorsi utilizzando le virgole. Puoi utilizzare i pattern globali. Puoi configurare file specifici. Immetti i pattern globali utilizzando le virgolette doppie. |
| `exclude` | Definisci i file che non desideri vengano monitorati dall'agent LogDNA. **Nota:** questi file possono essere ubicati in uno qualsiasi dei percorsi definiti mediante il parametro logdir. </br>Separa più file utilizzando le virgole. Puoi utilizzare i pattern globali. Puoi configurare file specifici. |
| `exclude_regex` | Definisci i pattern di espressione regolare (regex) per escludere mediante filtro le righe che corrispondono al pattern. Non includere `/` di inizio e fine. |
| `hostname` | Definisci il nome host. Questo valore sovrascrive il nome host del sistema operativo. |
| `autoupdate` | Imposta su `1` per aggiornare automaticamente l'agent quando viene aggiornata la definizione dell'agent di repository pubblico. Imposta su `0` per disabilitare questa funzione. |  
{: caption="Tabella 1. Parametri per personalizzare un agent LogDNA" caption-side="top"} 



## Configurazione di un agent LogDNA su un cluster Kubernetes utilizzando uno script
{: #config_agent_kube_script}

Per configurare il cluster Kubernetes per inviare i log alla tua istanza {{site.data.keyword.la_full_notm}}, devi installare un pod *logdna-agent* su ciascun nodo del tuo cluster. L'agent LogDNA legge i file di log dal pod in cui è installato e inoltra i dati di log alla tua istanza LogDNA.

Per configurare il tuo cluster Kubernetes per inoltrare i log alla tua istanza LogDNA, completa la seguente procedura dalla riga di comando:

1. Apri un terminale per accedere a {{site.data.keyword.cloud_notm}}.

   ```
   ibmcloud login -a cloud.ibm.com
   ```
   {: pre}

   Seleziona l'account in cui hai eseguito il provisioning dell'istanza {{site.data.keyword.la_full_notm}}.

2. Imposta il cluster in cui desideri configurare la registrazione come contesto per questa sessione.

   ```
   ibmcloud ks cluster-config <nome_o_ID_cluster>
   ```
   {: pre}

   Quando il download dei file di configurazione è terminato, viene visualizzato un comando che puoi utilizzare per impostare il percorso al file di configurazione di Kubernetes locale come una variabile di ambiente. Copia e incolla il comando visualizzato nel tuo terminale per impostare la variabile di ambiente `KUBECONFIG`.

3. Crea un segreto Kubernetes per archiviare la tua chiave di inserimento logDNA per la tua istanza del servizio. La chiave di inserimento LogDNA viene utilizzata per aprire un socket web sicuro al server di inserimento logDNA e per autenticare l'agent di registrazione presso il servizio {{site.data.keyword.la_full_notm}}.

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<chiave_di_inserimento_logDNA>
    ```
    {: pre}

4. Crea un insieme di daemon Kubernetes per distribuire l'agent LogDNA su ogni nodo di lavoro del tuo cluster Kubernetes. L'agent LogDNA raccoglie i log con l'estensione `*.log` e i file senza estensione che sono archiviati nella directory `/var/log` del tuo pod. Per impostazione predefinita, i log vengono raccolti da tutti gli spazi dei nomi, compreso `kube-system`, e inoltrati automaticamente al servizio {{site.data.keyword.la_full_notm}}.

    <table>
      <caption>Comandi per regione</caption>
      <tr>
        <th>Ubicazione</th>
        <th>Comando</th>
      </tr>
      <tr>
        <td>`US-South`</td>
        <td>`   kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
   `</td>
      </tr>
      <tr>
        <td>`EU-DE`</td>
        <td>`kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-eu-de.yaml`</td>
      </tr>
    </table>

5. Verifica che l'agent LogDNA sia distribuito correttamente. 

   ```
   kubectl get pods
   ```
   {: pre}
   

La distribuzione è eseguita correttamente quando vedi uno o più pod LogDNA.
* **Il numero di pod LogDNA è uguale al numero di nodi di lavoro nel tuo cluster.** 
* Tutti i pod devono essere in uno stato `In esecuzione`.
* *stdout* e *stderr* vengono raccolti e inoltrati automaticamente da tutti i contenitori. I dati di log includono i log delle applicazioni e i log dei nodi di lavoro. 
* Per impostazione predefinita, il pod dell'agent LogDNA che viene eseguito su un nodo di lavoro raccoglie i log da tutti gli spazi dei nomi su quel nodo, inclusi i log kube-system.



## Aggiunta di tag a un agent LogDNA su un cluster Kubernetes
{: #config_agent_kube_tags}

Completa la seguente procedura per aggiungere le tag:

1. Configura l'ambiente cluster. Esegui questi comandi:

    Innanzitutto, ottieni il comando per impostare la variabile di ambiente e scaricare i file di configurazione di Kubernetes.

    ```
    ibmcloud ks cluster-config <nome_o_ID_cluster>
    ```
    {: codeblock}

    Quando il download dei file di configurazione è terminato, viene visualizzato un comando che puoi utilizzare per impostare il percorso al file di configurazione di Kubernetes locale come una variabile di ambiente.

    Quindi, copia e incolla il comando visualizzato nel tuo terminale per impostare la variabile di ambiente KUBECONFIG.

2. Controlla la strategia di aggiornamento dell'insieme di daemon (DaemonSet). Scegli quindi se utilizzare *kubectl apply* o *kubectl edit* per modificare il file di configurazione per l'agent.

    Per controllare la strategia di aggiornamento, esegui il seguente comando:

    ```
    kubectl get ds/logdna-agent -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'
    ```
    {: pre}

    Se la strategia di aggiornamento è impostata su *OnDelete* oppure se hai un file di configurazione gestito mediante un sistema di controllo delle versioni, aggiorna il tuo file di configurazione locale e applica le modifiche all'agent LogDNA utilizzando *kubectl apply*.

    Se la strategia di aggiornamento è impostata su *RollingUpdate*, puoi aggiornare e applicare modifiche all'agent LogDNA utilizzando *kubectl edit*.

3. Modifica il file `logdna-agent-configmap.yaml`. 

    Aggiorna il file di configurazione modificando la copia locale. **Nota:** puoi anche generare il file di configurazione dell'agent eseguendo questo comando:

    ```
    kubectl get daemonset logdna-agent -o=yaml > prod-logdna-agent-ds.yaml
    ```
    {: codeblock}

    In alternativa, aggiorna il file di configurazione utilizzando *kubectl edit*.

    ```
    kubectl edit daemonset logdna-agent
    ```
    {: codeblock}

4. Apporta le modifiche. Aggiungi la sezione **LOGDNA_TAGS**.

    ```
    - name: LOGDNA_TAGS
        value: tag1,tag2,tag3
    ```
    {: codeblock}

    Ad esempio, la seguente sezione mostra dove aggiungere le tag nel file di configurazione:

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

5. Applica le modifiche della configurazione se modifichi il file in locale. 

    ```
    kubectl apply -f prod-logdna-agent-ds.yaml
    ```
    {: codeblock}
    
    **Nota:** se utilizzi *kubectl edit*, le variazioni vengono applicate automaticamente quando salvi le tue modifiche.


## Configurazione di un agent LogDNA su Linux Ubuntu o Debian
{: #config_agent_linux}

Per configurare il tuo server Ubuntu per inviare i log alla tua istanza {{site.data.keyword.la_full_notm}}, devi installare un `logdna-agent`. L'agent LogDNA legge i file di log da */var/log*, e inoltra i dati di log alla tua istanza LogDNA.

Per configurare il tuo server Ubuntu per inoltrare i log alla tua istanza LogDNA, completa la seguente procedura da un terminale Ubuntu:

1. Installa l'agent LogDNA. Esegui questi comandi:

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

2. Imposta la chiave di inserimento che l'agent LogDNA deve utilizzare per inoltrare i log all'istanza {{site.data.keyword.la_full_notm}}.  

    ```
    sudo logdna-agent -k CHIAVE_DI_INSERIMENTO
    ```
    {: codeblock}

    Dove CHIAVE_DI_INSERIMENTO contiene la chiave di inserimento attiva per l'istanza {{site.data.keyword.la_full_notm}} dove stai configurando l'inoltro dei log.

3. Imposta l'endpoint di autenticazione. L'agent LogDNA utilizza questo host per autenticare e ottenere il token per inoltrare i log.

    <table>
      <caption>Comandi per regione</caption>
      <tr>
        <th>Ubicazione</th>
        <th>Comando</th>
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

4. Imposta l'endpoint di inserimento.

    <table>
      <caption>Comandi per regione</caption>
      <tr>
        <th>Ubicazione</th>
        <th>Comando</th>
      </tr>
      <tr>
        <td>`US-South`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`EU-DE`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.eu-de.logging.cloud.ibm.com`</td>
      </tr>
    </table>

5. Definisci più percorsi di log da monitorare. Esegui il seguente comando: 

    ```
    sudo logdna-agent -d /path/to/log/folders
    ```
    {: codeblock}

    Per impostazione predefinita, viene monitorato **/var/log**.

6. Facoltativamente, configura l'agent LogDNA per contrassegnare con delle tag i tuoi host. 


## Aggiunta di tag a un agent LogDNA su Linux Ubuntu o Debian
{: #config_agent-linux_tags}
 

Completa la seguente procedura per aggiungere ulteriori tag all'agent LogDNA:

1. Verifica che l'agent LogDNA sia in esecuzione.

2. Aggiungi una o più tag.

    ```
    sudo logdna-agent -t TAG1,TAG2 
    ```
    {: codeblock}


Puoi anche modificare il file di configurazione LogDNA e aggiungere le tag. Il file di configurazione si trova in */etc/logdna.conf*.

1. Modifica il file.

    ```
    sudo update-rc.d logdna-agent defaults
    ```
    {: codeblock}

2. Aggiungi le tag.

3. Riavvia l'agent LogDNA.

    ``` 
    sudo /etc/init.d/logdna-agent start
    ```
    {: codeblock}














