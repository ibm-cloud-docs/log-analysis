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


# Analizza i log in Kibana per un'applicazione distribuita in un cluster Kubernetes
{: #container_logs}
Utilizza questa esercitazione per imparare la modalità di configurazione di un cluster per inoltrare i log al servizio {{site.data.keyword.loganalysisshort}} in {{site.data.keyword.Bluemix_notm}}.
{:shortdesc}


## Obbiettivi
{: #objectives}

1. Configurare le configurazioni di registrazione in un cluster. 
2. Ricercare e analizzare i log del contenitore per un'applicazione distribuita in un cluster Kubernetes in {{site.data.keyword.Bluemix_notm}}.

Questa esercitazione illustra in modo dettagliato i passi necessari per rendere operativo il seguente scenario end-to-end in {{site.data.keyword.Bluemix_notm}}: provisioning di un cluster, configurazione del cluster per inviare i log al servizio {{site.data.keyword.loganalysisshort}} in {{site.data.keyword.Bluemix_notm}}, distribuzione di un'applicazione nel cluster e utilizzo di Kibana per visualizzare e filtrare i log del contenitore per tale cluster.


**Nota:** per completare questa esercitazione, devi completare le esercitazioni che sono collegate dai diversi passi.


## Prerequisiti
{: #prereq}

1. Essere un membro o un proprietario di un account {{site.data.keyword.Bluemix_notm}} con autorizzazioni per creare i cluster standard Kubernetes, distribuire le applicazioni nei cluster ed eseguire query dei log in {{site.data.keyword.Bluemix_notm}} per l'analisi avanzata in Kibana.

    Al tuo ID utente per {{site.data.keyword.Bluemix_notm}} devono essere assegnate le seguenti politiche:
    
    * Una politica IAM per il {{site.data.keyword.containershort}} con le autorizzazioni *editor*, *operatore* o *amministratore*.
    * Un ruolo CF per lo spazio in cui viene eseguito il provisioning del servizio {{site.data.keyword.loganalysisshort}} con le autorizzazioni *sviluppatore*.
    
    Per ulteriori informazioni, vedi [Assegnazione di una politica IAM a un utente tramite la IU Cloud](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_account) e [Concessione delle autorizzazioni a un utente per visualizzare i log dello spazio utilizzando la IU IBM Cloud](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_space).

2. Avere una sessione terminale dalla quale poter gestire il cluster Kubernetes e distribuire le applicazioni dalla riga di comando. Gli esempi in questa esercitazione vengono forniti per un sistema Linux Ubuntu.

3. Installare le CLI per gestire il {{site.data.keyword.containershort}} e {{site.data.keyword.loganalysisshort}} nel tuo sistema Ubuntu.

    * Installa la CLI {{site.data.keyword.Bluemix_notm}}. Installa la CLI {{site.data.keyword.containershort}} per creare e gestire i tuoi cluster Kubernetes in {{site.data.keyword.containershort}} e per distribuire le applicazioni inserite nel contenitore al tuo cluster. Per ulteriori informazioni, vedi [Installazione della CLI {{site.data.keyword.Bluemix_notm}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview).
    
    * Installa la CLI {{site.data.keyword.loganalysisshort}}. Per ulteriori informazioni, vedi [Configurazione della CLI Analisi dei log (plugin IBM Cloud)](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli#config_log_collection_cli).
    
4. Disporre dell'accesso a uno spazio denominato **dev** nel tuo account nella regione Stati Uniti Sud. 

    I log disponibili nel cluster saranno configurati per essere inoltrati al dominio di spazio associato a questo spazio. 
    
    In questo spazio, eseguirai il provisioning del servizio {{site.data.keyword.loganalysisshort}}.
    
    Devi disporre delle autorizzazioni **sviluppatore** in questo spazio in modo da poter eseguire il provisioning del servizio {{site.data.keyword.loganalysisshort}}.
    
    In questa esercitazione, il nome dell'organizzazione utilizzato è **MyOrg**.

    
 

## Passo 1: esegui il provisioning di un cluster Kubernetes
{: #step25}

Completa la seguente procedura:

1. Crea un cluster standard Kubernetes.

   Per ulteriori informazioni, consulta [Creazione dei cluster](/docs/containers?topic=containers-cs_cluster_tutorial#cs_cluster_tutorial).

2. Configura il contesto del cluster in un terminale. Dopo che il contesto è stato impostato, puoi gestire il cluster Kubernetes e distribuire l'applicazione nel cluster Kubernetes.

    Accedi alla regione, all'organizzazione e allo spazio in {{site.data.keyword.Bluemix_notm}} che è associato al cluster che hai creato. Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).

	Inizializza il plug-in del servizio {{site.data.keyword.containershort}}.

	```
	ibmcloud cs init
	```
	{: codeblock}

    Imposta il contesto di terminale sul tuo cluster.
    
	```
	ibmcloud cs cluster-config MyCluster
	```
	{: codeblock}

    L'output dell'esecuzione di questo comando fornisce il comando che devi eseguire nel tuo terminale per impostare il percorso sul tuo file di configurazione. Ad esempio:

	```
	export KUBECONFIG=/Users/ibm/.bluemix/plugins/container-service/clusters/MyCluster/kube-config-hou02-MyCluster.yml
	```
	{: codeblock}

    Copia e incolla il comando per impostare la variabile di ambiente nel tuo terminale e premi quindi **Invio**.



## Passo 2: configura il tuo cluster per inoltrare i log automaticamente al servizio {{site.data.keyword.loganalysisshort}}
{: #step26}

Quando viene distribuita l'applicazione, i log vengono raccolti automaticamente dal {{site.data.keyword.containershort}}. Tuttavia, i log non vengono inoltrati automaticamente al servizio {{site.data.keyword.loganalysisshort}}. Devi creare 1 o più configurazioni di registrazione nel tuo cluster che definiscono:

* Dove vengono inoltrati i log. Puoi inoltrare i log al dominio dell'account o a un dominio dello spazio.
* Quali log sono inoltrati al servizio {{site.data.keyword.loganalysisshort}} per l'analisi.


Prima di definire le configurazioni di registrazione, controlla le tue definizioni di configurazione di registrazione correnti nel cluster. Esegui il seguente comando:

```
$ ibmcloud cs logging-config-get ClusterName
```
{: codeblock}

dove *ClusterName* è il nome del tuo cluster.

Ad esempio, le configurazioni di registrazione definite per il cluster *mycluster* sono le seguenti: 

```
$ ibmcloud cs logging-config-get mycluster
Retrieving cluster mycluster logging configurations...
OK
Id                                     Source       Namespace   Host                                Port   Org            Space   Protocol   Paths   
13ded2c0-83f5-4cc5-8de7-1e34e1287f34   worker       -           ingest.logging.ng.bluemix.net       9091   Demo_Org       dev     ibm        /var/log/syslog,/var/log/auth.log   
ae249c04-a3a9-4c29-a890-22d8da7bd1b2   container    *           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        -
31739fc1-42e2-4b66-ac57-6a32091c257a   ingress      -           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        /var/log/alb/ids/*.log,/var/log/alb/ids/*.err,/var/log/alb/customerlogs/*.log,/var/log/alb/customerlogs/*.err
6b8cfe89-4959-448d-898b-c3b0584eca71   kubernetes   -           ingest-eu-fra.logging.bluemix.net   9091   Demo_Org.      dev     ibm        /var/log/kubelet.log,/var/log/kube-proxy.log   

```
{: screen}

Per visualizzare un elenco delle origini log per cui puoi definire una configurazione di registrazione, vedi [Origini log](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kubernetes#log_sources).


### Configura il tuo cluster per inoltrare i log stderr e stdout al servizio {{site.data.keyword.loganalysisshort}}
{: #containerstd}


Completa la seguente procedura per inviare i log stdout e stderr a un dominio di spazio, dove il nome organizzazione è *MyOrg* e il nome spazio è *dev* nella regione Stati Uniti Sud:

1. Controlla che il tuo ID utente disponga delle autorizzazioni ad aggiungere una configurazione del cluster. Solo gli utenti con una politica IAM per {{site.data.keyword.containershort}} con le autorizzazioni per gestire i cluster possono abilitare questa funzione. È richiesto uno qualsiasi dei seguenti ruoli: *Amministratore*, *Operatore*

    Per controllare che il tuo ID utente abbia una politica IAM assegnata per gestire i cluster, completa questa procedura:
    
    1. Accedi alla console {{site.data.keyword.Bluemix_notm}}. Apri un browser web e avvia il dashboard {{site.data.keyword.Bluemix_notm}}; [http://bluemix.net ![Icona link esterno](../../../icons/launch-glyph.svg "Icona link esterno")](http://bluemix.net){:new_window} Dopo che hai eseguito l'accesso con i tuoi ID utente e password, viene aperta la IU {{site.data.keyword.Bluemix_notm}}.

    2. Dalla barra dei menu, fai clic su **Gestisci > Account > Utenti**.  La finestra *Utenti* visualizza un elenco di utenti con i loro indirizzi email per l'account attualmente selezionato.
	
    3. Seleziona l'ID utente e verifica che abbia una politica per il {{site.data.keyword.containershort}}.

    Se hai bisogno delle autorizzazioni, contatta il proprietario o l'amministratore dell'account. Solo il proprietario dell'account o gli utenti con le autorizzazioni ad assegnare le politiche possono eseguire questo passo.

2. Crea una configurazione di registrazione del cluster. Esegui questo comando per inviare i file di log *stdout* e *stderr* al servizio {{site.data.keyword.loganalysisshort}}:

    ```
    ibmcloud cs logging-config-create ClusterName --logsource container --namespace '*' --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    dove 

    * *ClusterName* è il nome del cluster.
    * *EndPoint* è l'URL del servizio di registrazione nella regione in cui viene eseguito il provisioning del servizio {{site.data.keyword.loganalysisshort}}. Per un elenco degli endpoint, vedi [Endpoint](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
    * *OrgName* è il nome dell'organizzazione in cui è disponibile lo spazio.
    * *SpaceName* è il nome dello spazio in cui viene eseguito il provisioning del servizio {{site.data.keyword.loganalysisshort}}.


Ad esempio, per creare una configurazione di registrazione che inoltra i log stdout e stderr allo spazio dev nella regione Stati Uniti Sud, esegui questo comando:

```
ibmcloud cs logging-config-create mycluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}




### Configura il tuo cluster per inoltrare i log worker al servizio {{site.data.keyword.loganalysisshort}}
{: #workerlogs }

Completa la seguente procedura per inviare i log worker a un dominio di spazio, dove il nome organizzazione è *MyOrg* e il nome spazio è *dev* nella regione Stati Uniti Sud:

1. Controlla che il tuo ID utente disponga delle autorizzazioni ad aggiungere una configurazione del cluster. Solo gli utenti con una politica IAM per {{site.data.keyword.containershort}} con le autorizzazioni per gestire i cluster possono abilitare questa funzione. È richiesto uno qualsiasi dei seguenti ruoli: *Amministratore*, *Operatore*

    Per controllare che il tuo ID utente abbia una politica IAM assegnata per gestire i cluster, completa questa procedura:
    
    1. Accedi alla console {{site.data.keyword.Bluemix_notm}}. Apri un browser web e avvia il dashboard {{site.data.keyword.Bluemix_notm}}; [http://bluemix.net ![Icona link esterno](../../../icons/launch-glyph.svg "Icona link esterno")](http://bluemix.net){:new_window} Dopo che hai eseguito l'accesso con i tuoi ID utente e password, viene aperta la IU {{site.data.keyword.Bluemix_notm}}.

    2. Dalla barra dei menu, fai clic su **Gestisci > Account > Utenti**.  La finestra *Utenti* visualizza un elenco di utenti con i loro indirizzi email per l'account attualmente selezionato.
	
    3. Seleziona l'ID utente e verifica che abbia una politica per il {{site.data.keyword.containershort}}.

    Se hai bisogno delle autorizzazioni, contatta il proprietario o l'amministratore dell'account. Solo il proprietario dell'account o gli utenti con le autorizzazioni ad assegnare le politiche possono eseguire questo passo.

2. Crea una configurazione di registrazione del cluster. Esegui questo comando per inviare i file di log */var/log/syslog* e */var/log/auth.log* al servizio {{site.data.keyword.loganalysisshort}}:

    ```
    ibmcloud cs logging-config-create ClusterName --logsource worker --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    dove 

    * *ClusterName* è il nome del cluster.
    * *EndPoint* è l'URL del servizio di registrazione nella regione in cui viene eseguito il provisioning del servizio {{site.data.keyword.loganalysisshort}}. Per un elenco degli endpoint, vedi [Endpoint](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
    * *OrgName* è il nome dell'organizzazione in cui è disponibile lo spazio.
    * *SpaceName* è il nome dello spazio in cui viene eseguito il provisioning del servizio {{site.data.keyword.loganalysisshort}}.

    
Ad esempio, per creare una configurazione di registrazione che inoltra i log di lavoro al dominio dello spazio nella regione Stati Uniti Sud, esegui questo comando:

```
ibmcloud cs logging-config-create mycluster --logsource worker  --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}



## Passo 3: concedi le tue autorizzazioni utente per visualizzare i log in un dominio dello spazio
{: #step33}

Per concedere a un utente le autorizzazioni a visualizzare i log in uno spazio, devi assegnare a tale utente un ruolo Cloud Foundry che descrive le azioni che questo utente può eseguire con il servizio {{site.data.keyword.loganalysisshort}} nello spazio. 

Completa la seguente procedura per concedere a un utente le autorizzazioni a lavorare con il servizio {{site.data.keyword.loganalysisshort}}:

1. Accedi alla console {{site.data.keyword.Bluemix_notm}}.

    Apri un browser web e avvia il dashboard {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Icona di link esterno](../../../icons/launch-glyph.svg "Icona di link esterno")](http://bluemix.net){:new_window}
	
	Dopo che hai eseguito l'accesso con il tuo ID utente e la tua password, viene aperta la IU {{site.data.keyword.Bluemix_notm}}.

2. Dalla barra dei menu, fai clic su **Gestisci > Account > Utenti**. 

    La finestra *Utenti* visualizza un elenco di utenti con i loro indirizzi email per l'account attualmente selezionato.
	
3. Se l'utente è un membro dell'account, seleziona il suo nome dall'elenco o fai clic su **Gestisci utente** dal menu *Azioni*.

    Se l'utente non è un membro dell'account, vedi [Invito di utenti](/docs/iam?topic=iam-iamuserinv#iamuserinv).

4. Seleziona **Accesso Cloud Foundry** e seleziona quindi l'organizzazione.

    Viene presentato l'elenco di spazi disponibili in tale organizzazione.

5. Scegli lo spazio. Quindi, dal menu delle azioni, seleziona **Modifica ruolo spazio**.

    Se non puoi visualizzare lo spazio per Stati Uniti Sud, crea lo spazio prima di procedere.

6. Seleziona *sviluppatore*.

    Puoi selezionare 1 o più ruoli. 
    
    I ruoli validi sono: *Gestore*, *Sviluppatore * e *Revisore*
	
7. Fai clic su **Salva ruolo**.


## Passo 4: concedere le autorizzazioni al proprietario della chiave {{site.data.keyword.containershort_notm}}
{: #step52}

In modo che i log del cluster siano inoltrati a uno spazio, il proprietario della chiave {{site.data.keyword.containershort_notm}} deve avere le seguenti autorizzazioni:

* Politica IAM per il servizio {{site.data.keyword.loganalysisshort}} con le autorizzazioni di *Amministratore*.
* Le autorizzazioni Cloud Foundry (CF) nell'organizzazione e nello spazio in cui stanno venendo inoltrati i log. Il proprietario della chiave del contenitore ha bisogno del ruolo *orgManager* (Gestore organizzazione) per l'organizzazione e *SpaceManager* (Gestore spazio) e *Developer* (Sviluppatore) per lo spazio.

Completa la seguente procedura:

1. Identifica l'utente nell'account che è il proprietario della chiave {{site.data.keyword.containershort}}. Da un terminale, esegui questo comando:

    ```
    ibmcloud cs api-key-info ClusterName
    ```
    {: codeblock}
    
    dove *ClusterName* è il nome del cluster.

2. Verifica che l'utente che è identificato come proprietario della chiave {{site.data.keyword.containershort}} abbia il ruolo *orgManager* (Gestore organizzazione) per l'organizzazione e *SpaceManager* (Gestore spazio) e *Developer* (Sviluppatore) per lo spazio.

    Accedi alla console {{site.data.keyword.Bluemix_notm}}. Apri un browser web e avvia il dashboard {{site.data.keyword.Bluemix_notm}}; [http://bluemix.net ![Icona link esterno](../../../icons/launch-glyph.svg "Icona link esterno")](http://bluemix.net){:new_window} Dopo che hai eseguito l'accesso con i tuoi ID utente e password, viene aperta la IU {{site.data.keyword.Bluemix_notm}}.

    Dalla barra dei menu, fai clic su **Gestisci > Account > Utenti**.  La finestra *Utenti* visualizza un elenco di utenti con i loro indirizzi email per l'account attualmente selezionato.
	
    Seleziona l'ID dell'utente e verifica che l'utente abbia il ruolo *orgManager* (Gestore organizzazione) per l'organizzazione e *SpaceManager* (Gestore spazio) e *Developer* (Sviluppatore) per lo spazio.

    Se l'utente non ha le autorizzazioni corrette, concedi all'utente le seguenti autorizzazioni: *orgManager* (Gestore organizzazione) per l'organizzazione e *SpaceManager* (Gestore spazio) e *Developer* (Sviluppatore) per lo spazio. Per ulteriori informazioni, vedi [Concessione delle autorizzazioni a un utente per visualizzare i log dello spazio utilizzando la IU IBM Cloud](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_space).
    
3. Verifica che l'utente che è identificato come proprietario della chiave {{site.data.keyword.containershort}} abbia una politica IAM per il servizio {{site.data.keyword.loganalysisshort}} con le autorizzazioni *Amministratore*.

    Dalla barra dei menu, fai clic su **Gestisci > Account > Utenti**.  La finestra *Utenti* visualizza un elenco di utenti con i loro indirizzi email per l'account attualmente selezionato.
	
    Seleziona l'ID dell'utente e verifica che l'utente abbia la politica IAM configurata. 

    Se l'utente non dispone della politica IAM, vedi [Assegna una politica IAM a un utente tramite la IU IBM Cloud](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_account).

4. Aggiorna la configurazione della registrazione. Esegui il seguente comando:
    
    ```
    ibmcloud cs logging-config-refresh ClusterName
    ```
    {: codeblock}
        
    dove *ClusterName* è il nome del cluster.
	



## Passo 5: distribuisci un'applicazione di esempio nel cluster Kubernetes per generare il contenuto in stdout
{: #step53}

Distribuisci ed esegui un'applicazione di esempio nel cluster Kubernetes. Completa la procedura in questa esercitazione per distribuire l'applicazione di esempio:[Lezione 1: distribuzione di singole applicazioni dell'istanza ai cluster Kubernetes](/docs/containers?topic=containers-cs_apps_tutorial#cs_apps_tutorial_lesson1).

L'applicazione è un'applicazione Node.js Hello World:

```
var express = require('express')
var app = express()

app.get('/', function(req, res) {
  res.send('Hello world! Your app is up and running in a cluster!\n')
})
app.listen(8080, function() {
  console.log('Sample app is listening on port 8080.')
})
```
{: screen}

In questa applicazione di esempio, quando verifichi la tua applicazione in un browser, l'applicazione scrive in stdout il seguente messaggio: `Sample app is listening on port 8080.`






## Passo 6: visualizza i dati di log in Kibana
{: #step6}

Completa la seguente procedura:

1. Avvia Kibana in un browser. 

    Per ulteriori informazioni su come avviare Kibana, vedi [Passaggio a Kibana da un browser web](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-launch#launch_Kibana_from_browser).

    Per analizzare i dati di log per un cluster, devi accedere a Kibana nella regione di cloud pubblico dove viene creato il cluster. 
    
    Ad esempio, nella regione Stati Uniti Sud, immetti il seguente URL per avviare Kibana:
	
	```
	https://logging.ng.bluemix.net/ 
	```
	{: codeblock}
	
    Viene aperto Kibana.
    
    **NOTA:** verifica che avvii Kibana nella regione in cui stai inoltrando i tuoi log di cluster. Per informazioni sugli URL per regione, vedi [Endpoint di registrazione](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analyzing_logs_Kibana#urls_kibana).
    	
2. Per visualizzare i dati di log disponibili nel dominio dello spazio, completa la seguente procedura:

    1. In Kibana, fai clic sul tuo ID utente. Viene aperta la vista per impostare lo spazio.
    
    2. Seleziona l'account in cui è disponibile lo spazio. 
    
    3. Seleziona il seguente dominio: **space**
    
    4. Seleziona l'organizzazione *MyOrg* in cui è disponibile lo spazio.
    
    5. Seleziona lo spazio *dev*.
    
    
3. Nella pagina **Rileva**, guarda gli eventi visualizzati. 
        
    Nella sezione *Campi disponibili*, puoi vedere l'elenco di campi che puoi utilizzare per definire nuove query o filtrare le voci elencate nella tabella visualizzata nella pagina.
    
    La seguente tabella elenca alcuni dei campi che puoi usare per definire nuove query di ricerca quando analizzi i log dell'applicazione. La tabella include anche dei valori di esempio che corrispondono all'evento generato dall'applicazione di esempio:
 
    <table>
              <caption>Tabella 2. Campi comuni per i log del contenitore </caption>
               <tr>
                <th align="center">Campo</th>
                <th align="center">Descrizione</th>
                <th align="center">Esempio</th>
              </tr>
              <tr>
                <td>*ibm-containers.region_str *</td>
                <td>l valore di questo campo corrisponde alla regione {{site.data.keyword.Bluemix_notm}} dove viene raccolta la voce di log.</td>
                <td>us-south</td>
              </tr>
			  <tr>
                <td>*ibm-containers.account_id_str*</td>
                <td>ID account</td>
                <td></td>
              </tr>
			  <tr>
                <td>*ibm-containers.cluster_id_str *</td>
                <td>L'ID cluster.</td>
                <td></td>
              </tr>
              <tr>
                <td>*ibm-containers.cluster_name_str*</td>
                <td>ID cluster</td>
                <td></td>
              </tr>
			  <tr>
                <td>*kubernetes.namespace_name_str *</td>
                <td>Nome dello spazio dei nomi</td>
                <td>*default* è il valore predefinito.</td>
              </tr>
              <tr>
                <td>*kubernetes.container_name_str *</td>
                <td>Il nome del contenitore</td>
                <td>hello-world-deployment</td>
              </tr>
              <tr>
                <td>*kubernetes.labels.label_name*</td>
                <td>I campi di etichetta sono facoltativi. Puoi avere 0 o più etichette. Ciascuna etichetta inizia con il prefisso `kubernetes.labels.` seguito dal *nome_etichetta*. </td>
                <td>Nell'applicazione di esempio, puoi vedere 2 etichette: <br>* *kubernetes.labels.pod-template-hash_str* = 3355293961 <br>* *kubernetes.labels.run_str* =	hello-world-deployment  </td>
              </tr>
              <tr>
                <td>*stream_str *</td>
                <td>Il tipo di log.</td>
                <td>*stdout*, *stderr*</td>
              </tr>
        </table>
     
Per ulteriori informazioni sugli altri campi di ricerca pertinenti ai cluster Kubernetes, vedi [Ricerca dei log](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kubernetes#log_search).


## Passo 7: filtra i dati in base al nome cluster Kubernetes in Kibana
{: #step7}
    
Nella tabella visualizzata nella pagina *Individuazione*, puoi vedere tutte le voci disponibili per l'analisi. Le voci elencate corrispondono alla query di ricerca visualizzata nella barra *Ricerca*. Utilizza un asterisco (*) per visualizzare tutte le voci nel periodo di tempo configurato per la pagina.
    
Ad esempio, per filtrare i dati in base al nome cluster Kubernetes, modifica la query della barra *Ricerca*. Aggiungi un filtro basato sul campo personalizzato *kubernetes.cluster_name_str*:
    
1. Nella sezione **Campi disponibili**, seleziona il campo *kubernetes.cluster_name_str*. Viene visualizzato un sottoinsieme dei valori disponibili per il campo.    
    
2. Seleziona il valore che corrisponde al cluster per cui vuoi analizzare i log. 
    
    Dopo che hai selezionato il valore, alla *Barra di ricerca* viene aggiunto un filtro e la tabella visualizza solo le voci che corrispondono ai criteri che hai appena selezionato.     
   

**Nota:** 

se non puoi vedere il tuo nome cluster, aggiungi un filtro per qualsiasi nome cluster. Seleziona quindi il simbolo di modifica del filtro.    
    
Viene visualizzata la seguente query:
    
```
	{
        "query": {
          "match": {
            "kubernetes.cluster_name_str": {
              "query": "cluster1",
              "type": "phrase"
            }
          }
        }
      }
```
{: screen}

Sostituisci il nome del cluster (*cluster1*) con il nome del cluster *mycluster* per cui vuoi visualizzare i dati di log.
        
Se non riesci a vedere alcun dato, prova a modificare il filtro temporale. Per maggiori informazioni, vedi [Configurazione di un filtro temporale](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter).

Per maggiori informazioni, vedi [Filtro dei log in Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#filter_logs).


## Materiale di riferimento di {{site.data.keyword.containershort_notm}}
{: reference}

Comandi CLI:

* [ibmcloud cs api-key-info](/docs/containers?topic=containers-cs_cli_reference#cs_api_key_info)
* [ibmcloud cs logging-config-create](/docs/containers?topic=containers-cs_cli_reference#cs_logging_create)
* [ibmcloud cs logging-config-get](/docs/containers?topic=containers-cs_cli_reference#cs_logging_get)
* [ibmcloud cs logging-config-update](/docs/containers?topic=containers-cs_cli_reference#cs_logging_update)
* [ibmcloud cs logging-config-rm](/docs/containers?topic=containers-cs_cli_reference#cs_logging_rm)
* [ibmcloud cs logging-config-refresh](/docs/containers?topic=containers-cs_cli_reference#cs_logging_refresh)

