---

copyright:
  years:  2018, 2019
lastupdated: "2019-05-01"

keywords: LogDNA, IBM, Log Analysis, logging, kubernetes, tutorial

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


# Gestione dei log di cluster Kubernetes con {{site.data.keyword.la_full_notm}}
{: #kube}

Utilizza il servizio {{site.data.keyword.la_full_notm}} per configurare la registrazione a livello di cluster in {{site.data.keyword.containerlong}}. 
{:shortdesc}

Dal momento che esegui il provisioning di un cluster con {{site.data.keyword.containerlong_notm}}, vuoi sapere cosa sta succedendo nel cluster. Devi accedere ai log per risolvere e anticipare i problemi. In qualsiasi momento, vuoi avere accesso a diversi tipi di log quali i log di nodi di lavoro, i log di pod, i log di applicazioni o i log di rete. Vuoi inoltre monitorare le diverse origini di dati di log nel tuo cluster Kubernetes. Pertanto, la tua capacità di gestire i record di log e di accedere a essi da queste origini è di importanza critica. Il tuo successo nella gestione e nel monitoraggio dei log dipende da come configuri le funzionalità di registrazione per la tua piattaforma Kubernetes.

Per configurare la registrazione a livello di cluster per un cluster Kubernetes, tieni conto delle seguenti informazioni:

* Devi poter archiviare i dati di log, i log di sistema e i log di applicazioni inserite nei contenitori su un'archiviazione separata dai componenti di sistema Kubernetes.
* Devi distribuire un agent di registrazione a ogni nodo di lavoro nel tuo cluster. Questo agent raccoglie e inoltra i log a un back-end di registrazione esterno.
* Devi potere centralizzare i dati di log per l'analisi su un back-end di registrazione esterno.


In {{site.data.keyword.cloud_notm}}, per configurare la registrazione a livello di cluster per un cluster Kubernetes, devi completare la seguente procedura:

1. Esegui il provisioning di un'istanza del servizio {{site.data.keyword.la_full_notm}}. Con questo passo, configuri un sistema di gestione dei log centralizzato in cui sono ospitati i dati di log su {{site.data.keyword.cloud_notm}}.
2. Esegui il provisioning di un cluster su {{site.data.keyword.containerlong_notm}}. Sono supportati i cluster Kubernetes v1.9+.
3. Configura l'agent LogDNA su ogni nodo di lavoro in un cluster.

![Panoramica dei componenti LogDNA su {{site.data.keyword.cloud_notm}}](../images/kube.png "Panoramica dei componenti LogDNA su {{site.data.keyword.cloud_notm}}")

In questa esercitazione, imparerai come configurare una registrazione a livello di cluster.

## Prima di iniziare
{: #kube_prereqs}

Lavora in una [regione supportata](/docs/services/Log-Analysis-with-LogDNA/tutorials?topic=LogDNA-about#overview_regions). **Nota:** è possibile inviare i dati da un cluster Kubernetes che si trova nella stessa regione o in una regione differente. 

Leggi a proposito di {{site.data.keyword.la_full_notm}}. Per ulteriori informazioni, vedi [Informazioni su ](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).

Utilizza un ID utente che sia un membro o un proprietario di un account {{site.data.keyword.cloud_notm}}. Per ottenere un ID utente {{site.data.keyword.cloud_notm}}, vai a [Registrazione![Icona link esterno](../../../icons/launch-glyph.svg "Icona link esterno")](https://cloud.ibm.com/login){:new_window}.

Al tuo ID {{site.data.keyword.IBM_notm}} devono essere assegnate le politiche IAM per ciascuna delle seguenti risorse nella regione in cui si trova la tua istanza {{site.data.keyword.la_full_notm}}:  

| Risorsa                             | Ambito della politica di accesso | Ruolo    | Informazioni                  |
|--------------------------------------|----------------------------|---------|------------------------------|
| Gruppo di risorse **Predefinito**           |  Gruppo di risorse            | Visualizzatore  | Questa politica è richiesta per consentire all'utente di visualizzare le istanze del servizio nel gruppo di risorse Predefinito.    |
| Servizio {{site.data.keyword.la_full_notm}} |  Gruppo di risorse            | Editor  | Questa politica è richiesta per consentire all'utente di eseguire il provisioning e l'amministrazione del servizio {{site.data.keyword.la_full_notm}} nel gruppo di risorse Predefinito.   |
| Istanza cluster Kubernetes          |  Risorsa                 | Editor  | Questa politica è richiesta per configurare il segreto e l'agent LogDNA nel cluster Kubernetes. |
{: caption="Tabella 1. Elenco delle politiche IAM richieste per completare l'esercitazione" caption-side="top"} 

Per ulteriori informazioni sui ruoli IAM {{site.data.keyword.containerlong}}, vedi [Autorizzazioni di accesso utente](/docs/containers?topic=containers-access_reference#access_reference).

Installa la CLI {{site.data.keyword.cloud_notm}} e il plug-in della CLI Kubernetes. Per ulteriori informazioni, vedi [Installazione della CLI {{site.data.keyword.cloud_notm}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli).


## Obiettivi
{: #kube_objectives}

In questa esercitazione, configuri la registrazione con LogDNA per il tuo cluster {{site.data.keyword.containerlong_notm}}. In particolare:

- Eseguirai il provisioning di un {{site.data.keyword.la_full_notm}}. 
- Configurerai l'agent LogDNA nel tuo cluster per iniziare a inviare i log a LogDNA. 
- Aprirai il dashboard LogDNA per trovare i tuoi log. 


## Passo 1. Provisioning di un'istanza del servizio {{site.data.keyword.la_full_notm}}
{: #kube_step1}

Per eseguire il provisioning di un'istanza del servizio di {{site.data.keyword.la_full_notm}} mediante la console {{site.data.keyword.cloud_notm}}, completa la seguente procedura:

1. Accedi all'account [{{site.data.keyword.cloud_notm}} ![Icona link esterno](../../../icons/launch-glyph.svg "Icona link esterno")](https://cloud.ibm.com/login) dove hai creato il tuo cluster Kubernetes.

2. Fai clic su **Catalogo**. Viene aperto un elenco di servizi {{site.data.keyword.cloud_notm}}.

3. Per filtrare l'elenco dei servizi che viene visualizzato, seleziona la categoria **Strumenti per gli sviluppatori**.

4. Fai clic su **{{site.data.keyword.la_full_notm}}**. Viene aperto il dashboard **Osservabilità**.

5. Seleziona **Crea istanza**. 

6. Immetti un nome per l'istanza del servizio.

7. Seleziona il gruppo di risorse in cui si trova il tuo cluster. Per impostazione predefinita, il gruppo di risorse **Predefinito** è impostato per tuo conto. 

8. Scegli un piano di servizio per la tua istanza del servizio. Per impostazione predefinita, il piano **Lite** è selezionato per tuo conto. Per ulteriori informazioni sugli altri piani di servizio, vedi [Piani di prezzo](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

9. Per eseguire il provisioning del servizio {{site.data.keyword.la_full_notm}} nel gruppo di risorse {{site.data.keyword.cloud_notm}} in cui sei collegato, fai clic su **Crea**. Viene aperto il dashboard **Osservabilità** che mostra i dettagli per il tuo servizio. 

Per eseguire il provisioning di un'istanza mediante la CLI, vedi [Provisioning di un'istanza mediante la CLI {{site.data.keyword.cloud_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-provision#provision_cli).
{: tip}

## Passo 2. Ottieni la chiave di inserimento
{: #kube_step2}

Per ottenere la chiave di inserimento, completa la seguente procedura:

1. Accedi al tuo account {{site.data.keyword.cloud_notm}}.

    Fai clic sul [dashboard {{site.data.keyword.cloud_notm}} ![Icona link esterno](../../icons/launch-glyph.svg "Icona link esterno")](https://cloud.ibm.com/login){:new_window} per avviare il dashboard {{site.data.keyword.cloud_notm}}.

	Dopo che hai eseguito l'accesso con il tuo ID utente e la tua password, viene aperta l'IU {{site.data.keyword.cloud_notm}}.

2. Nel menu di navigazione, seleziona **Osservabilità**. 

3. Seleziona **Registrazione**. Viene aperto il dashboard {{site.data.keyword.la_full_notm}}. Puoi vedere l'elenco delle istanze di registrazione disponibili in {{site.data.keyword.cloud_notm}}.

3. Identifica l'istanza per la quale desideri ottenere la chiave di inserimento e fai clic su **Visualizza chiave di inserimento**.

4. Viene visualizzata una finestra dove puoi fare clic su **Mostra** per visualizzare la chiave di inserimento.


## Passo 3: configura il tuo cluster Kubernetes per inviare i log alla tua istanza LogDNA
{: #kube_step3}

Per configurare il cluster Kubernetes per inviare i log alla tua istanza {{site.data.keyword.la_full_notm}}, devi installare un pod `logdna-agent` su ciascun nodo del tuo cluster. L'agent LogDNA legge i file di log dal pod in cui è installato e inoltra i dati di log alla tua istanza LogDNA.

Per configurare il tuo cluster Kubernetes per inoltrare i log alla tua istanza LogDNA, completa la seguente procedura dalla riga di comando:

1. Apri un terminale per accedere a {{site.data.keyword.cloud_notm}}.

   ```
   ibmcloud login -a cloud.ibm.com
   ```
   {: pre}

   Seleziona l'account dove hai eseguito il provisioning dell'istanza {{site.data.keyword.la_full_notm}}.

2. Imposta il cluster in cui desideri configurare la registrazione come contesto per questa sessione.

   ```
   ibmcloud ks cluster-config <nome_o_ID_cluster>
   ```
   {: pre}

   Quando il download dei file di configurazione è terminato, viene visualizzato un comando che puoi utilizzare per impostare il percorso al file di configurazione di Kubernetes locale come una variabile di ambiente. Copia e incolla il comando visualizzato nel tuo terminale per impostare la variabile di ambiente `KUBECONFIG`.

   Ogni volta che esegui l'accesso alla CLI {{site.data.keyword.containerlong_notm}} per lavorare con il tuo cluster, devi eseguire questa impostazione per impostare il percorso al file di configurazione del cluster come una variabile di sessione. {{site.data.keyword.containerlong_notm}} utilizza questa variabile per trovare un file di configurazione locale e i certificati necessari per stabilire una connessione al tuo cluster..
   {: tip}

3. Crea un segreto Kubernetes per archiviare la tua chiave di inserimento logDNA per la tua istanza del servizio. La chiave di inserimento LogDNA viene utilizzata per aprire un socket web sicuro al server di inserimento logDNA e per autenticare l'agent di registrazione presso il servizio {{site.data.keyword.la_full_notm}}.

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<chiave_di_inserimento_logDNA>
    ```
    {: pre}

4. Crea un insieme di daemon Kubernetes per distribuire l'agent LogDNA su ogni nodo di lavoro del tuo cluster Kubernetes. L'agent LogDNA raccoglie i log con l'estensione `*.log` e i file senza estensione che sono archiviati nella directory `/var/log` del tuo pod. Per impostazione predefinita, i log vengono raccolti da tutti gli spazi dei nomi, compreso `kube-system`, e inoltrati automaticamente al servizio {{site.data.keyword.la_full_notm}}.

   ```
   kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
   ```
   {: pre}

5. Verifica che l'agent LogDNA sia distribuito correttamente. 

   ```
   kubectl get pods
   ```
   {: pre}
   
   La distribuzione è eseguita correttamente quando vedi uno o più pod LogDNA. Il numero di pod LogDNA è uguale al numero di nodi di lavoro nel tuo cluster. Tutti i pod devono essere in uno stato `In esecuzione`.


## Passo 4: avvia il dashboard LogDNA e visualizza i log
{: #kube_step4}

Per avviare il dashboard LogDNA mediante la console {{site.data.keyword.cloud_notm}}, completa la seguente procedura:

1. Accedi al tuo account [{{site.data.keyword.cloud_notm}} ![Icona link esterno](../../../icons/launch-glyph.svg "Icona link esterno")](https://cloud.ibm.com/login).

2. Dal menu ![Icona di menu](../../../icons/icon_hamburger.svg "Icona di menu"), seleziona **Osservabilità**.

3. Seleziona **Registrazione**. Viene visualizzato l'elenco di istanze del servizio {{site.data.keyword.la_full_notm}} che sono disponibili in {{site.data.keyword.cloud_notm}}.

4. Seleziona una singola istanza e fai clic su **Visualizza LogDNA**. Viene aperto il dashboard LogDNA. **Nota:** con il piano di servizio **Gratuito**, puoi accodare solo i log più recenti. Per ulteriori informazioni, vedi [Visualizzazione dei log](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs).

## Passi successivi
{: #kube_next_steps}

- [Filtra i log](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5)
- [Cerca nei log](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6)
- [Definisci le viste](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7)
- [Configura gli avvisi](https://docs.logdna.com/docs/alerts). 

**Nota:** alcune di queste funzioni richiedono un upgrade del piano.




