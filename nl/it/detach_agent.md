---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, detach config agent

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

# Scollegamento di un agent LogDNA da un'istanza
{: #detach_agent}

Scollega un agent LogDNA da un'istanza di registrazione per arrestare la raccolta di log.
{:shortdesc}

## Scollegamento di un agent LogDNA da un cluster Kubernetes
{: #detach_agent_kube}

Per arrestare il tuo cluster Kubernetes dall'inviare i log alla tua istanza {{site.data.keyword.la_full_notm}}, devi rimuovere l'agent LogDNA dal tuo cluster. 

Per arrestare il tuo cluster Kubernetes dall'inoltrare i log alla tua istanza LogDNA, completa la seguente procedura dalla riga di comando:

1. Apri un terminale. Quindi, [accedi a {{site.data.keyword.cloud_notm}} ![Icona link esterno](../../icons/launch-glyph.svg "Icona link esterno")](https://cloud.ibm.com/login){:new_window} e segui le istruzioni.

    Seleziona l'account in cui hai eseguito il provisioning dell'istanza {{site.data.keyword.la_full_notm}}.

2. Configura l'ambiente cluster. Esegui questi comandi:

    Innanzitutto, ottieni il comando per impostare la variabile di ambiente e scaricare i file di configurazione di Kubernetes.

    ```
    ibmcloud ks cluster-config <nome_o_ID_cluster>
    ```
    {: codeblock}

    Quando il download dei file di configurazione è terminato, viene visualizzato un comando che puoi utilizzare per impostare il percorso al file di configurazione di Kubernetes locale come una variabile di ambiente.

    Quindi, copia e incolla il comando visualizzato nel tuo terminale per impostare la variabile di ambiente `KUBECONFIG`.

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




