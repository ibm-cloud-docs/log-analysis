---

copyright:
  years:  2018, 2019
lastupdated: "2019-05-01"

keywords: LogDNA, IBM, Log Analysis, logging, iam, manage user access

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

 
# Gestione dell'accesso utente con IAM
{: #iam}

IAM ({{site.data.keyword.iamlong}}) ti consente di autenticare in modo sicuro gli utenti e di controllare l'accesso a tutte le risorse cloud in modo congruente in {{site.data.keyword.cloud_notm}}. 
{:shortdesc}

**A ogni utente che accede al servizio {{site.data.keyword.la_full_notm}} nel tuo account deve essere assegnata una politica di accesso con un ruolo utente IAM definito.** La politica determina quali azioni possono essere eseguite dall'utente nel contesto del servizio o dell'istanza che selezioni. Le azioni consentite sono personalizzate e definite come operazioni di cui è consentita l'esecuzione sul servizio. Le azioni vengono quindi associate ai ruoli utente IAM.

Le *politiche* abilitano la concessione dell'accesso a diversi livelli. Alcune delle opzioni includono quanto segue: 

* Accesso a tutti i servizi abilitati a IAM nel tuo account
* Accesso a tutte le istanze del servizio in una singola regione nel tuo account
* Accesso a una singola istanza del servizio nel tuo account
* Accesso a tutte le istanze del servizio nel contesto di un gruppo di risorse
* Accesso a tutte le istanze del servizio in una singola regione nel contesto di un gruppo di risorse
* Accesso a tutti i servizi abilitati a IAM nel contesto di un gruppo di risorse

I *ruoli* definiscono le azioni che possono essere eseguite da un utente o un ID servizio. Ci sono diversi tipi di ruoli in {{site.data.keyword.cloud_notm}}:

* I *ruoli di gestione della piattaforma* consentono agli utenti di eseguire azioni sulle risorse di servizio a livello della piattaforma, ad esempio assegnare all'utente l'accesso per il servizio, creare o eliminare gli ID servizio, creare istanze, assegnare politiche per il tuo servizio ad altri utenti e associare mediante bind le istanze alle applicazioni.
* I *ruoli di accesso al servizio* consentono l'assegnazione agli utenti di diversi livelli di autorizzazione per il richiamo dell'API del servizio.

**Per organizzare un insieme di utenti e ID servizio in una singola entità che ti facilita la gestione delle autorizzazioni IAM, utilizza i *gruppi di accesso*.** Puoi assegnare una sola politica al gruppo invece di assegnare lo stesso accesso più volte per ogni utente o ID servizio.
{: tip}


## Gestione dell'accesso utilizzando i gruppi di accesso
{: #groups}

Per gestire l'accesso o assegnare del nuovo accesso per gli utenti utilizzando i gruppi di accesso, devi essere il proprietario dell'account, l'amministratore o l'editor su tutti i servizi abilitati per l'accesso e l'identità nell'account oppure un amministratore o un editor assegnati per il servizio Gruppi di accesso IAM. 

Scegli una qualsiasi delle seguenti azioni per gestire i gruppi di accesso in {{site.data.keyword.cloud_notm}}:

* [Creazione di un gruppo di accesso](/docs/iam?topic=iam-groups#create_ag).
* [Assegnazione dell'accesso a un gruppo](/docs/iam?topic=iam-groups#access_ag).


## Gestione dell'accesso assegnando le politiche direttamente agli utenti
{: #users}

Per gestire l'accesso o assegnare del nuovo accesso per gli utenti utilizzando le politiche IAM, devi essere il proprietario dell'account, l'amministratore di tutti i servizi nell'account oppure un amministratore per il servizio o l'istanza del servizio specifici. 

Scegli una qualsiasi delle seguenti azioni per gestire le politiche IAM in {{site.data.keyword.cloud_notm}}:

* Per modificare le autorizzazioni di un utente, vedi [Modifica dell'accesso esistente](/docs/iam?topic=iam-iammanidaccser#edit_existing).
* Per concedere le autorizzazioni a un utente, vedi [Assegna nuovo accesso](/docs/iam?topic=iam-iammanidaccser#assign_new_access).
* Per revocare le autorizzazioni, vedi [Rimozione dell'accesso](/docs/iam?topic=iam-iammanidaccser#removing_access).
* Per controllare le autorizzazioni di un utente, vedi [Controllo del tuo accesso assegnato](/docs/iam?topic=iam-iammanidaccser#review_your_access).




## Ruoli della piattaforma {{site.data.keyword.cloud_notm}}
{: #platform}

Utilizza la seguente tabella per identificare il ruolo della piattaforma che desideri concedere a un utente in {{site.data.keyword.cloud_notm}} per eseguire una qualsiasi delle seguenti azioni della piattaforma:

| Azioni della piattaforma                                                         | Ruoli della piattaforma {{site.data.keyword.cloud_notm}}    | 
|--------------------------------------------------------------------------|------------------------------------------------------|
| `Grant other account members access to work with the service`            | Amministratore                                        | 
| `Provision a service instance`                                           | Editor                            | 
| `Delete a service instance`                                              | Amministratore </br>Editor                            | 
| `Create a service ID`                                                    | Amministratore </br>Editor                            |
| `View details of a service instance`                                     | Amministratore </br>Editor </br>Operatore </br>Visualizzatore  | 
| `View service instances in the Observability Logging dashboard`          | Amministratore </br>Editor </br>Operatore </br>Visualizzatore  | 
| `View the ingestion key in the {{site.data.keyword.cloud_notm}} console` | Amministratore                                        | 
{: caption="Tabella 1. Azioni e ruoli utente IAM" caption-side="top"}



## Ruoli del servizio {{site.data.keyword.cloud_notm}}
{: #service}

Utilizza la seguente tabella per identificare i ruoli del servizio che puoi concedere a un utente per eseguire le seguenti azioni di servizio:

| Azioni                                                                 | Ruoli del servizio {{site.data.keyword.cloud_notm}}     | 
|-------------------------------------------------------------------------|------------------------------------------------------|
| `Add LogDNA log sources`                                                | Gestore                                              |
| `Manage ingestion keys through the LogDNA web UI`                       | Gestore                                              |
| `Manage service keys`                                                   | Gestore                                              |
| `Archive logs`                                                          | Gestore                                              |
| `Manage parsing`                                                        | Gestore                                              |
| `Configure alerts`                                                      | Gestore </br>Scrittore </br>Lettore                      | 
| `Filter and search log data`                                            | Gestore </br>Scrittore </br>Lettore                      |
| `Create views`                                                          | Gestore </br>Scrittore </br>Lettore                      |
| `Manage views`                                                          | Gestore </br>Scrittore </br>Lettore                      |
| `Export log data`                                                       | Gestore </br>Scrittore </br>Lettore                      |
| `Configure user preferences in the LogDNA web UI`                       | Gestore </br>Scrittore </br>Lettore                      |
| `View logs through the LogDNA web UI`                                   | Gestore </br>Scrittore </br>Lettore                      | 
{: caption="Tabella 2. Azioni e ruoli utente IAM" caption-side="top"}


**Nota:** il ruolo del servizio **gestore** è associato direttamente al ruolo di amministratore di LogDNA.






