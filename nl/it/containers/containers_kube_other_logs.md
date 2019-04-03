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


# Abilitazione della raccolta automatica dei log di cluster
{: #containers_kube_other_logs}

Per poter visualizzare e analizzare i log di cluster nel servizio {{site.data.keyword.loganalysisshort}}, devi configurare il cluster per inoltrare tali log al servizio {{site.data.keyword.loganalysisshort}}. 
{:shortdesc}

## Passo 1: controlla le autorizzazioni del tuo ID utente
{: step1}

Il tuo ID utente deve avere le seguenti autorizzazioni per poter aggiungere una configurazione di registrazione al cluster:

* Politica IAM per {{site.data.keyword.containershort}} con le autorizzazioni di **Visualizzatore**.
* Politica IAM per l'istanza del cluster con le autorizzazioni di **Amministratore** o **Operatore**.

Per controllare che il tuo ID utente abbia queste politiche IAM, completa la seguente procedura:

**Nota:** solo il proprietario dell'account o gli utenti con le autorizzazioni ad assegnare le politiche possono eseguire questo passo.

1. Accedi alla console {{site.data.keyword.Bluemix_notm}}. Apri un browser web e avvia il dashboard {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Icona di link esterno](../../../icons/launch-glyph.svg "Icona di link esterno")](http://bluemix.net){:new_window}
	
	Dopo che hai eseguito l'accesso con il tuo ID utente e la tua password, viene aperta la IU {{site.data.keyword.Bluemix_notm}}.

2. Dalla barra dei menu, fai clic su **Gestisci > Account > Utenti**.  La finestra *Utenti* visualizza un elenco di utenti con i loro indirizzi email per l'account attualmente selezionato.
	
3. Seleziona l'ID utente e verifica che abbia entrambe le politiche.




## Passo 2: configura il contesto del cluster.
{: #step2}

Completa la seguente procedura:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Inizializza il plug-in del servizio {{site.data.keyword.loganalysisshort}}.

	```
	ibmcloud ks init
	```
	{: codeblock}

3. Imposta il contesto di terminale sul tuo cluster.
    
	```
	ibmcloud ks cluster-config ClusterName
	```
	{: codeblock}

    L'output dell'esecuzione di questo comando fornisce il comando che devi eseguire nel tuo terminale per impostare il percorso sul tuo file di configurazione. Ad esempio, per un cluster denominato *MyCluster*:

	```
	export KUBECONFIG=/Users/ibm/.bluemix/plugins/container-service/clusters/MyCluster/kube-config-hou02-MyCluster.yml
	```
	{: codeblock}

4. Copia e incolla il comando per impostare la variabile di ambiente nel tuo terminale e premi quindi **Invio**.



## Passo 3: configura il tuo cluster
{: step3}

Puoi scegliere quali log di cluster inoltrare al servizio {{site.data.keyword.loganalysisshort}}. 

* Per abilitare la raccolta di log automatica e l'inoltro di stdout e stderr, vedi [Abilitazione della raccolta di log automatica e dell'inoltro dei log del contenitore](/docs/services/CloudLogAnalysis/containers/containers_kube_other_logs.html#containers).
* Per abilitare la raccolta di log automatica e l'inoltro dei log di applicazione, vedi [Abilitazione della raccolta di log automatica e inoltro di log di applicazione](/docs/services/CloudLogAnalysis/containers/containers_kube_other_logs.html#apps).
* Per abilitare la raccolta di log automatica e l'inoltro di log di lavoro, vedi [Abilitazione della raccolta di log automatica e inoltro di log di lavoro](/docs/services/CloudLogAnalysis/containers/containers_kube_other_logs.html#workers).
* Per abilitare la raccolta di log automatica e l'inoltro dei log di componente di sistema Kubernetes, vedi [Abilitazione della raccolta di log automatica e inoltro dei log di componente di sistema Kubernetes](/docs/services/CloudLogAnalysis/containers/containers_kube_other_logs.html#system).
* Per abilitare la raccolta di log automatica e l'inoltro dei log di controller Ingress Kubernetes, vedi [Abilitazione della raccolta di log automatica e inoltro dei log di controller Ingress Kubernetes](/docs/services/CloudLogAnalysis/containers/containers_kube_other_logs.html#controller).



## Passo 4: imposta le autorizzazioni per il proprietario della chiave {{site.data.keyword.containershort_notm}}
{: #step4}


Il proprietario della chiave {{site.data.keyword.containershort}} ha bisogno delle seguenti politiche IAM:

* Politica IAM per {{site.data.keyword.containershort}} con il ruolo di **Amministratore**.
* Politica IAM per il servizio {{site.data.keyword.loganalysisshort}} con il ruolo di **Amministratore**.

Completa la seguente procedura: 

1. Accedi alla console {{site.data.keyword.Bluemix_notm}}. Apri un browser web e avvia il dashboard {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Icona di link esterno](../../../icons/launch-glyph.svg "Icona di link esterno")](http://bluemix.net){:new_window}
	
	Dopo che hai eseguito l'accesso con il tuo ID utente e la tua password, viene aperta la IU {{site.data.keyword.Bluemix_notm}}.

2. Dalla barra dei menu, fai clic su **Gestisci > Account > Utenti**.  La finestra *Utenti* visualizza un elenco di utenti con i loro indirizzi email per l'account attualmente selezionato.
	
3. Seleziona l'ID utente del proprietario della chiave {{site.data.keyword.containershort_notm}} e verifica che abbia entrambe le politiche.


Quando inoltri i log a un dominio dello spazio, devi anche concedere le autorizzazioni CF (Cloud Foundry) al proprietario della chiave {{site.data.keyword.containershort}} nell'organizzazione e nello spazio. Il proprietario della chiave ha bisogno del ruolo *orgManager* (Gestore organizzazione) per l'organizzazione e *SpaceManager* (Gestore spazio) o *Developer* (Sviluppatore) per lo spazio.

Completa la seguente procedura:

1. Identifica l'utente nell'account che è il proprietario della chiave {{site.data.keyword.containershort}}. Da un terminale, esegui questo comando:

    ```
    ibmcloud ks api-key-info ClusterName
    ```
    {: codeblock}
    
    dove *ClusterName* è il nome del cluster.
    
2. Verifica che l'utente che è identificato come proprietario della chiave {{site.data.keyword.containershort}} abbia il ruolo *orgManager* (Gestore organizzazione) per l'organizzazione e *SpaceManager* (Gestore spazio) e *Developer* (Sviluppatore) per lo spazio.

    Accedi alla console {{site.data.keyword.Bluemix_notm}}. Apri un browser web e avvia il dashboard {{site.data.keyword.Bluemix_notm}}; [http://bluemix.net ![Icona link esterno](../../../icons/launch-glyph.svg "Icona link esterno")](http://bluemix.net){:new_window} Dopo che hai eseguito l'accesso con i tuoi ID utente e password, viene aperta la IU {{site.data.keyword.Bluemix_notm}}.

    Dalla barra dei menu, fai clic su **Gestisci > Account > Utenti**.  La finestra *Utenti* visualizza un elenco di utenti con i loro indirizzi email per l'account attualmente selezionato.
	
    Seleziona l'ID dell'utente e verifica che l'utente abbia il ruolo *orgManager* (Gestore organizzazione) per l'organizzazione e *SpaceManager* (Gestore spazio) o *Developer* (Sviluppatore) per lo spazio.
 
3. Se l'utente non dispone delle autorizzazioni corrette, completa la seguente procedura:

    1. Concedi all'utente le seguenti autorizzazioni: *orgManager* (Gestore organizzazione) per l'organizzazione e *SpaceManager* (Gestore spazio) e *Developer* (Sviluppatore) per lo spazio. Per ulteriori informazioni, vedi [Concessione delle autorizzazioni a un utente per visualizzare i log dello spazio utilizzando la IU IBM Cloud](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space).
    
    2. Aggiorna la configurazione della registrazione. Esegui il seguente comando:
    
        ```
        ibmcloud ks logging-config-refresh ClusterName
        ```
        {: codeblock}
        
        dove *ClusterName* è il nome del cluster.
  




## Abilitazione della raccolta di log automatica e inoltro dei log del contenitore 
{: #containers}

Esegui questo comando per inviare i file di log *stdout* e *stderr* al servizio {{site.data.keyword.loganalysisshort}}:

```
ibmcloud ks logging-config-create ClusterName --logsource container --namespace '*' --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

dove 

* *ClusterName* è il nome del cluster.
* *EndPoint* è l'URL del servizio di registrazione nella regione in cui viene eseguito il provisioning del servizio {{site.data.keyword.loganalysisshort}}. Per un elenco degli endpoint, vedi [Endpoint](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls).
* *OrgName* è il nome dell'organizzazione in cui è disponibile lo spazio.
* *SpaceName* è il nome dello spazio in cui viene eseguito il provisioning del servizio {{site.data.keyword.loganalysisshort}}.


Ad esempio, per creare una configurazione della registrazione che inoltra i log stdout e stderr al dominio dell'account nella regione Germania, esegui questo comando:

```
ibmcloud ks logging-config-create MyCluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}

Per creare una configurazione della registrazione che invia i log stdout e stderr a un dominio dello spazio nella regione Germania, esegui questo comando:

```
ibmcloud ks logging-config-create MyCluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org MyOrg --space MySpace
```
{: screen}



## Abilitazione della raccolta di log automatica e inoltro dei log di applicazione 
{: #apps}

Esegui questo comando per inviare i file di log */var/log/apps/**/.log* e */var/log/apps/*/.err* al servizio {{site.data.keyword.loganalysisshort}}:

```
ibmcloud ks logging-config-create ClusterName --logsource application --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName --app-containers --app-paths
```
{: codeblock}

dove 

* *ClusterName* è il nome del cluster.
* *EndPoint* è l'URL del servizio di registrazione nella regione in cui viene eseguito il provisioning del servizio {{site.data.keyword.loganalysisshort}}. Per un elenco degli endpoint, vedi [Endpoint](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls).
* *OrgName* è il nome dell'organizzazione in cui è disponibile lo spazio.
* *SpaceName* è il nome dello spazio in cui viene eseguito il provisioning del servizio {{site.data.keyword.loganalysisshort}}.
* *app-containers* è un parametro facoltativo che puoi impostare per definire un elenco di contenitori che vuoi visualizzare. Questi contenitori sono gli unici da cui i log saranno instradati a {{site.data.keyword.loganalysisshort}}. Puoi impostare uno o più contenitori separandoli da virgole.
* *app-paths* definisce i percorsi nei contenitori che vuoi visualizzare. Puoi impostare uno o più percorsi separandoli da virgole. I caratteri jolly come '/var/log/*.log' sono accettati. 

Ad esempio, per creare una configurazione della registrazione che inoltra i log dell'applicazione a un dominio dello spazio nella regione Germania, esegui questo comando:

```
ibmcloud ks logging-config-create MyCluster --logsource application --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org MyOrg --space MySpace --app-paths /var/log/*.log
```
{: screen}

Ad esempio, per creare una configurazione della registrazione che inoltra i log dell'applicazione al dominio dell'account nella regione Germania, esegui questo comando:

```
ibmcloud ks logging-config-create MyCluster --logsource application --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --app-paths /var/log/*.log
```
{: screen}



## Abilitazione della raccolta di log automatica e inoltro dei log di lavoro 
{: #workers}


Esegui questo comando per inviare i file di log */var/log/syslog* e */var/log/auth.log* al servizio {{site.data.keyword.loganalysisshort}}:

```
ibmcloud ks logging-config-create ClusterName --logsource worker --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

dove 

* *ClusterName* è il nome del cluster.
* *EndPoint* è l'URL del servizio di registrazione nella regione in cui viene eseguito il provisioning del servizio {{site.data.keyword.loganalysisshort}}. Per un elenco degli endpoint, vedi [Endpoint](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls).
* *OrgName* è il nome dell'organizzazione in cui è disponibile lo spazio.
* *SpaceName* è il nome dello spazio in cui viene eseguito il provisioning del servizio {{site.data.keyword.loganalysisshort}}.



Ad esempio, per creare una configurazione della registrazione che inoltra i log di lavoro a un dominio dello spazio nella regione Germania, esegui questo comando:

```
ibmcloud ks logging-config-create MyCluster --logsource worker  --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

Ad esempio, per creare una configurazione della registrazione che inoltra i log di lavoro al dominio dell'account nella regione Germania, esegui questo comando:

```
ibmcloud ks logging-config-create MyCluster --logsource worker  --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}



## Abilitazione della raccolta di log automatica e inoltro dei log di componente di sistema Kubernetes
{: #system}

Esegui questo comando per inviare i file di log */var/log/kubelet.log* e */var/log/kube-proxy.log* al servizio {{site.data.keyword.loganalysisshort}}:

```
ibmcloud ks logging-config-create ClusterName --logsource kubernetes --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

dove 

* *ClusterName* è il nome del cluster.
* *EndPoint* è l'URL del servizio di registrazione nella regione in cui viene eseguito il provisioning del servizio {{site.data.keyword.loganalysisshort}}. Per un elenco degli endpoint, vedi [Endpoint](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls).
* *OrgName* è il nome dell'organizzazione in cui è disponibile lo spazio.
* *SpaceName* è il nome dello spazio in cui viene eseguito il provisioning del servizio {{site.data.keyword.loganalysisshort}}.



Ad esempio, per creare una configurazione della registrazione che inoltra i log di componente di sistema Kubernetes a un dominio dello spazio nella regione Germania, esegui questo comando:

```
ibmcloud ks logging-config-create MyCluster --logsource kubernetes --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

Ad esempio, per creare una configurazione della registrazione che inoltra i log di componente di sistema Kubernetes al dominio dell'account nella regione Germania, esegui questo comando:

```
ibmcloud ks logging-config-create MyCluster --logsource kubernetes --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}



## Abilitazione della raccolta di log automatica e inoltro dei log di controller Ingress Kubernetes
{: #controller}

Esegui questo comando per inviare i file di log */var/log/alb/ids/.log*, */var/log/alb/ids/.err*, */var/log/alb/customerlogs/.log* e /var/log/alb/customerlogs/.err* al servizio {{site.data.keyword.loganalysisshort}}:

```
ibmcloud ks logging-config-create ClusterName --logsource ingress --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName
```
{: codeblock}

dove 

* *ClusterName* è il nome del cluster.
* *EndPoint* è l'URL del servizio di registrazione nella regione in cui viene eseguito il provisioning del servizio {{site.data.keyword.loganalysisshort}}. Per un elenco degli endpoint, vedi [Endpoint](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls).
* *OrgName* è il nome dell'organizzazione in cui è disponibile lo spazio.
* *SpaceName* è il nome dello spazio in cui viene eseguito il provisioning del servizio {{site.data.keyword.loganalysisshort}}.



Ad esempio, per creare una configurazione della registrazione che inoltra i log di controller Ingress a un dominio dello spazio nella regione Germania, esegui questo comando:

```
ibmcloud ks logging-config-create MyLoggingDemoCluster --logsource ingress --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

Ad esempio, per creare una configurazione della registrazione che inoltra i log di controller Ingress al dominio dell'account nella regione Germania, esegui questo comando:

```
ibmcloud ks logging-config-create MyLoggingDemoCluster --logsource ingress --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091  
```
{: screen}



