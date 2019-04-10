---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-23"

keywords: LogDNA, IBM, Log Analysis, logging, overview

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

# Informazioni su {{site.data.keyword.la_full_notm}}
{: #about}

{{site.data.keyword.la_full}} è un servizio di terze parti che puoi includere come parte della tua architettura {{site.data.keyword.cloud_notm}} per aggiungere funzionalità di gestione dei log. {{site.data.keyword.la_full_notm}} è gestito da LogDNA in collaborazione con {{site.data.keyword.IBM_notm}}.
{:shortdesc}

Puoi utilizzare {{site.data.keyword.la_full_notm}} per gestire i log di applicazione e sistema in {{site.data.keyword.cloud_notm}}.

{{site.data.keyword.la_full_notm}} offre ad amministratori, team DevOps e sviluppatori delle funzioni avanzate per filtrare, cercare, accodare dati di log, definire avvisi e progettare viste personalizzate per monitorare i log di applicazione e sistema.


## Panoramica
{: #ov}

Per aggiungere funzioni di registrazione con LogDNA in {{site.data.keyword.cloud_notm}}, devi eseguire il provisioning di un'istanza di {{site.data.keyword.la_full_notm}}.

Prima di eseguire il provisioning di un'istanza di {{site.data.keyword.la_full_notm}}, valuta le seguenti informazioni:
* I dati di log sono ospitati in {{site.data.keyword.cloud_notm}}.
* I dati di log sono inviati a una terza parte.
* I tuoi utenti devono disporre delle autorizzazioni della piattaforma per creare, visualizzare ed eliminare un'istanza di un servizio in {{site.data.keyword.cloud_notm}}.
* I tuoi utenti devono disporre delle autorizzazioni della piattaforma per creare risorse nel contesto del gruppo di istanze dove intendi eseguire il provisioning dell'istanza LogDNA.

Esegui il provisioning di un'istanza {{site.data.keyword.la_full_notm}} nel contesto di un gruppo di risorse. Organizzi i tuoi servizi per scopi di controllo dell'accesso e di fatturazione utilizzando i gruppi di risorse. Puoi eseguire il provisioning dell'istanza nel gruppo di risorse *predefinito* oppure in un gruppo di risorse personalizzato.

Dopo che hai eseguito il provisioning di un'istanza di {{site.data.keyword.la_full_notm}}, viene creato un account in LogDNA e ricevi la chiave di inserimento per il tuo account.

Devi quindi configurare un agent LogDNA per ogni origine log. Un'origine log è una risorsa Cloud oppure in loco che genera dei log. Ad esempio, un'origine log può essere un cluster Kubernetes. Utilizzi la chiave di inserimento per configurare l'agent LogDNA responsabile della raccolta e dell'inoltro dei log alla tua istanza {{site.data.keyword.la_full_notm}}.

Dopo la distribuzione dell'agent LogDNA in un'origine log, la raccolta e l'inoltro dei log all'istanza {{site.data.keyword.la_full_notm}} sono automatici.

Puoi avviare l'IU web {{site.data.keyword.la_full_notm}} per visualizzare, monitorare e gestire i tuoi log.

La seguente figura mostra la panoramica dei componenti per il servizio {{site.data.keyword.la_full_notm}} in esecuzione su {{site.data.keyword.cloud_notm}}:

![{{site.data.keyword.la_full_notm}} - panoramica dei componenti su {{site.data.keyword.cloud_notm}}](images/components.png "{{site.data.keyword.la_full_notm}} - panoramica dei componenti su {{site.data.keyword.cloud_notm}}")


## Dati di log
{: #overview_data}

{{site.data.keyword.la_full_notm}} raccoglie e aggrega i log in un sistema di registrazione centralizzato.

* I dati di log sono ospitati in {{site.data.keyword.cloud_notm}}.
* I dati sono co-locati nella regione dove viene eseguito il provisioning dell'istanza {{site.data.keyword.la_full_notm}}. Ad esempio, i dati di log per un'istanza di cui viene eseguito il provisioning in Stati Uniti Sud sono ospitati nella regione Stati Uniti Sud.

Il piano del servizio che scegli per un'istanza {{site.data.keyword.la_full_notm}} definisce il numero di giorni di archiviazione e conservazione dei dati in LogDNA. Ad esempio, se scegli il piano *Gratuito*, i dati non vengono archiviati affatto. Tuttavia, se scegli il piano di 7 giorni, i dati vengono archiviati per 7 giorni e hai accesso ad essi tramite l'IU web LogDNA.

Quando elimini un'istanza di {{site.data.keyword.la_full_notm}} da {{site.data.keyword.cloud_notm}}, vengono eliminati tutti i dati.



## Funzioni
{: #overview_features}

**Risolvi i problemi con i log in tempo reale per diagnosticare e identificare i problemi.**

Utilizzando la funzione *live streaming tail*, gli sviluppatori e i team DevOps possono diagnosticare i problemi, analizzare le eccezioni e le tracce di stack, identificare l'origine degli errori e monitorare diverse origini di log mediante una singola vista. Questa funzione è disponibile mediante la riga di comando e mediante l'interfaccia web.

**Emetti gli avvisi per ricevere una notifica delle azioni importanti.**
 
Per intervenire tempestivamente sugli eventi relativi ad applicazioni e servizi che identifichi come critici o di avvertenza, i team DevOps possono configurare delle integrazioni di notifica degli avvisi ai seguenti sistemi: email, Slack, HipChat, webHook, PagerDuty e OpsGenie.

**Esporta i log in un file locale per l'analisi oppure a un servizio di archiviazione per soddisfare requisiti di controllo.**

Esporta specifiche righe di log in una copia locale oppure archivia i log da {{site.data.keyword.la_full_notm}} a IBM Cloud Object Storage.
Le righe di log sono esportate in formato di riga JSON. I log sono archiviati in formato JSON e mantengono i metadati associati a ciascuna riga.

**Controlla i costi dell'infrastruttura di registrazione personalizzando quali log gestire mediante {{site.data.keyword.la_full_notm}}.**

Controlla il costo della tua infrastruttura di registrazione in IBM Cloud configurando le origini di log per cui desideri raccogliere e gestire i log.


## Piani di prezzo
{: #overview_pricing_plans}

Sono disponibili diversi piani di prezzo che puoi scegliere per un'istanza {{site.data.keyword.la_full_notm}}. Ogni piano definisce il numero di giorni per cui i dati vengono conservati per la ricerca, il numero di utenti a cui è consentito gestire i dati e le funzioni LogDNA abilitate.

| Piano                     | 
|--------------------------|
| `30 days log search`  |
| `14 days log search`  |
| `7-day log search`   |
| `Lite`                  |
{: caption="Tabella 1. Elenco dei piani di servizio" caption-side="top"} 

{{site.data.keyword.la_full_notm}} offre un piano `Lite` che puoi utilizzare per visualizzare i tuoi log quando transitano per il sistema. Puoi visualizzare i log utilizzando l'accodamento di log. Puoi anche progettare dei filtri per la preparazione all'upgrade a un piano con un periodo di conservazione più lungo. Questo piano ha un periodo di conservazione di 0 giorni.

Le seguenti tabelle descrivono le diverse funzioni che sono incluse in ogni piano di servizio:

| Funzione                          | Piano `30 day log search` | Piano `14 days log search`    | Piano `7 days log search     | Piano `Lite` | 
|----------------------------------|-------------------------|-------------------------------|-----------------------------|--------------|
| `Logs are stored and searchable` | Sì - per 30 giorni       | Sì - per 14 giorni             | Sì - per 7 giorni            | No           |
| `Live streaming tail`            | Sì                     | Sì                           | Sì                         | Sì          |
| `Archiving`                      | Sì                     | Sì                           | Sì                         | No           |
| `Multi-channel Alerting`         | Sì                     | Sì                           | Sì                         | No           | 
{: caption="Tabella 2. Elenco delle funzioni disponibili per ogni piano di servizio" caption-side="top"} 



## Regioni
{: #overview_regions}

La registrazione con {{site.data.keyword.la_full_notm}} è disponibile nelle seguenti regioni:

| Regione                | Ubicazione  |
|-----------------------|-----------|
| **Stati Uniti Sud**          | Dallas    |
| **EU-DE**             | Francoforte | 
{: caption="Tabella 3. Elenco delle regioni in cui il servizio è disponibile" caption-side="top"} 

Attualmente, l'ubicazione **Francoforte** **non** è gestita dall'UE. Per ulteriori informazioni, vedi [Abilitazione dell'impostazione Supportato UE](/docs/account?topic=account-eu-hipaa-supported#bill_eusupported).
{: important}



