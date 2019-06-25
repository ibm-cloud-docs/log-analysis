---

copyright:
  years:  2018, 2019
lastupdated: "2019-05-01"

keywords: LogDNA, IBM, Log Analysis, logging, kubernetes, tutorial, reset ingestion key

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


# Reimpostazione della chiave di inserimento utilizzata da un cluster Kubernetes per inoltrare i log a un'istanza {{site.data.keyword.la_full_notm}}
{: #kube_reset}

Se la chiave di inserimento che utilizzi per inoltrare i log da un cluster a un'istanza {{site.data.keyword.la_full_notm}} in {{site.data.keyword.cloud_notm}} è danneggiata, devi reimpostare la chiave e aggiornare la configurazione del cluster Kubernetes per utilizzare la nuova chiave di inserimento. 
{:shortdesc}

## Prima di iniziare
{: #kube_reset_prereqs}

Lavoro nella regione US-South. Entrambe le risorse, l'istanza {{site.data.keyword.la_full_notm}} e il cluster Kubernetes, devono essere eseguite nello stesso account.

Il provisioning dell'istanza {{site.data.keyword.la_full_notm}} viene eseguito nel gruppo di risorse **Default**.

Leggi a proposito di {{site.data.keyword.la_full_notm}}. Per ulteriori informazioni, vedi [Informazioni su LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).

Per completare la procedura in questa esercitazione, al tuo ID {{site.data.keyword.IBM_notm}} devono essere assegnate le politiche IAM per ciascuna delle seguenti risorse: 

| Risorsa                             | Ambito della politica di accesso | Ruoli    | Regione    | Informazioni                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Gruppo di risorse **Predefinito**           |  Gruppo di risorse            | Visualizzatore  | us-south  | Questa politica è richiesta per consentire all'utente di visualizzare le istanze del servizio nel gruppo di risorse Predefinito.    |
| Servizio {{site.data.keyword.la_full_notm}} |  Gruppo di risorse            | Editor </br>Gestore  | us-south  | Questa politica è richiesta per consentire all'utente di reimpostare la chiave di inserimento.   |
| Istanza cluster Kubernetes          |  Risorsa                  | Editor  | us-south  | Questa politica è richiesta per eliminare e configurare il segreto e l'agent LogDNA nel cluster Kubernetes. |
{: caption="Tabella 1. Elenco delle politiche IAM richieste per completare l'esercitazione" caption-side="top"} 

Per ulteriori informazioni sui ruoli IAM {{site.data.keyword.containerlong}}, vedi [Autorizzazioni di accesso utente](/docs/containers?topic=containers-access_reference#access_reference).

Installa la CLI {{site.data.keyword.cloud_notm}} e il plug-in della CLI Kubernetes. Per ulteriori informazioni, vedi [Installazione della CLI {{site.data.keyword.cloud_notm}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli).


## Passo 1: reimposta la chiave di inserimento
{: #kube_reset_step1}

Per rinnovare la chiave di inserimento per un'istanza {{site.data.keyword.la_full_notm}} utilizzando l'IU web {{site.data.keyword.la_full_notm}}, completa la seguente procedura:

1. Avvia l'IU web {{site.data.keyword.la_full_notm}}. Per ulteriori informazioni, vedi [Avvio dell'IU web {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Seleziona l'icona **Configuration**. Seleziona quindi **Organization**. 

3. Seleziona **API keys**.

    Puoi visualizzare le chiavi di inserimento che sono state create. 

4. Seleziona **Generate Ingestion Key**.

    Una nuova chiave viene aggiunta all'elenco.

5. Elimina la vecchia chiave di inserimento. Fai clic su **delete**.


## Passo 2: rimuovi qualsiasi configurazione nel cluster che utilizza la vecchia chiave di inserimento
{: #kube_reset_step2}

Completa la seguente procedura:

1. Apri un terminale. Accedi quindi a {{site.data.keyword.cloud_notm}}. Esegui il seguente comando e segui i prompt:

    ```
    ibmcloud login -a cloud.ibm.com
    ```
    {: codeblock}

    Seleziona l'account dove hai eseguito il provisioning dell'istanza {{site.data.keyword.la_full_notm}}.

2. Configura l'ambiente cluster. Esegui questi comandi:

    Innanzitutto, ottieni il comando per impostare la variabile di ambiente e scaricare i file di configurazione di Kubernetes.

    ```
    ibmcloud ks cluster-config <nome_o_ID_cluster>
    ```
    {: codeblock}

    Quando il download dei file di configurazione è terminato, viene visualizzato un comando che puoi utilizzare per impostare il percorso al file di configurazione di Kubernetes locale come una variabile di ambiente.

    Quindi, copia e incolla il comando visualizzato nel tuo terminale per impostare la variabile di ambiente KUBECONFIG.

    **Nota:** ogni volta che accedi alla CLI {{site.data.keyword.containerlong}} per lavorare con i cluster, devi eseguire questi comandi per impostare il percorso al file di configurazione del cluster come una variabile di sessione. La CLI Kubernetes utilizza questa variabile per trovare i certificati e un file di configurazione locale necessari per il collegamento con il cluster in {{site.data.keyword.cloud_notm}}.

3. Rimuovi il segreto dal tuo cluster Kubernetes. Il segreto Kubernetes contiene la chiave di inserimento LogDNA. Esegui il seguente comando:

    ```
    kubectl delete secret logdna-agent-key
    ```
    {: codeblock}

4. Rimuovi l'agent LogDNA su qualsiasi nodo di lavoro del tuo cluster Kubernetes. L'agent LogDNA è responsabile della raccolta e dell'inoltro dei tuoi log. Esegui il seguente comando:

    ```
    kubectl delete daemonset logdna-agent
    ```
    {: codeblock}

5. Verifica che l'agent LogDNA sia eliminato correttamente. Esegui il seguente comando:

    ```
    kubectl get pods
    ```
    {: codeblock}

    Non dovresti vedere alcun pod LogDNA.


## Passo 3: configura il tuo cluster Kubernetes con la nuova chiave di inserimento
{: #kube_reset_step3}

Per configurare il tuo cluster Kubernetes per inoltrare i log alla tua istanza LogDNA, completa la seguente procedura dalla riga di comando:

1. Apri un terminale. Accedi quindi a {{site.data.keyword.cloud_notm}}. Esegui il seguente comando e segui i prompt:

    ```
    ibmcloud login -a cloud.ibm.com
    ```
    {: codeblock}

    Seleziona l'account dove hai eseguito il provisioning dell'istanza {{site.data.keyword.la_full_notm}}.

2. Configura l'ambiente cluster. Esegui questi comandi:

    Innanzitutto, ottieni il comando per impostare la variabile di ambiente e scaricare i file di configurazione di Kubernetes.

    ```
    ibmcloud ks cluster-config <nome_o_ID_cluster>
    ```
    {: codeblock}

    Quando il download dei file di configurazione è terminato, viene visualizzato un comando che puoi utilizzare per impostare il percorso al file di configurazione di Kubernetes locale come una variabile di ambiente.

    Quindi, copia e incolla il comando visualizzato nel tuo terminale per impostare la variabile di ambiente KUBECONFIG.

    **Nota:** ogni volta che accedi alla CLI {{site.data.keyword.containerlong}} per lavorare con i cluster, devi eseguire questi comandi per impostare il percorso al file di configurazione del cluster come una variabile di sessione. La CLI Kubernetes utilizza questa variabile per trovare i certificati e un file di configurazione locale necessari per il collegamento con il cluster in {{site.data.keyword.cloud_notm}}.

3. Aggiungi un segreto al tuo cluster Kubernetes. Esegui il seguente comando:

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=CHIAVE_DI_INSERIMENTO_LOGDNA_PER_LA_TUA_ISTANZA
    ```
    {: codeblock}

    La CHIAVE_DI_INSERIMENTO_LOGDNA_PER_LA_TUA_ISTANZA mostra la chiave di inserimento LogDNA per la tua istanza.

    Il segreto Kubernetes contiene la chiave di inserimento LogDNA. La chiave di inserimento LogDNA viene utilizzata per eseguire l'autenticazione dell'agent di registrazione presso il servizio {{site.data.keyword.la_full_notm}}. Viene utilizzata per aprire un socket web sicuro al server di inserimento sul sistema di back-end di registrazione.

4. Configura l'agent LogDNA su qualsiasi nodo di lavoro del tuo cluster Kubernetes. Esegui il seguente comando:

    ```
    kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
    ```
    {: codeblock}

    L'agent LogDNA è responsabile della raccolta e dell'inoltro dei tuoi log.

    L'agent raccoglie automaticamente i log con l'estensione *.log e i file senza estensione che si trovano in /var/log. Per impostazione predefinita, i log vengono raccolti da tutti gli spazi dei nomi, compreso il kube-system.

5. Verifica che l'agent LogDNA sia creato correttamente e verificane lo stato. Esegui il seguente comando:

    ```
    kubectl get pods
    ```
    {: codeblock}


## Passo 4: avvia l'IU web LogDNA
{: #kube_reset_step4}

Per avviare il dashboard IBM Log Analysis con LogDNA mediante l'IU {{site.data.keyword.cloud_notm}}, completa la seguente procedura:

1. Accedi al tuo account {{site.data.keyword.cloud_notm}}.

    Fai clic sul [dashboard {{site.data.keyword.cloud_notm}} ![Icona link esterno](../../icons/launch-glyph.svg "Icona link esterno")](https://cloud.ibm.com/login){:new_window} per avviare il dashboard {{site.data.keyword.cloud_notm}}.

	Dopo che hai effettuato l'accesso con i tuoi ID utente e password, viene aperto il dashboard {{site.data.keyword.cloud_notm}}.

2. Nel menu di navigazione, seleziona **Osservabilità**. 

3. Seleziona **Registrazione**. 

    Viene visualizzato l'elenco delle istanze {{site.data.keyword.la_full_notm}} disponibili in {{site.data.keyword.cloud_notm}}.

3. Seleziona una singola istanza. Fai quindi clic su **Visualizza log**.

    Viene aperta l'IU web LogDNA, che visualizza i tuoi log del cluster.


## Passo 5: visualizza i tuoi log
{: #kube_reset_step5}

Dall'IU web LogDNA, puoi visualizzare i tuoi log quando transitano per il sistema. Visualizzi i log utilizzando l'accodamento di log. 

**Nota:** con il piano di servizio **Gratuito**, puoi accodare solo i tuoi log più recenti.



## Passi successivi
{: #kube_reset_next_steps}

  Se desideri [filtrare i log del cluster](https://docs.logdna.com/docs/filters), [cercare nei log del cluster](https://docs.logdna.com/docs/search), [definire le viste](https://docs.logdna.com/docs/views) e [configurare gli avvisi](https://docs.logdna.com/docs/alerts), devi eseguire l'upgrade del piano {{site.data.keyword.la_full_notm}} a un piano a pagamento.



