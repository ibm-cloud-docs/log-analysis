---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, IAM, security, logging, access groups

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

 
# Gestione dei gruppi di accesso e delle politiche IAM
{: #work_iam}

Puoi utilizzare IAM ({{site.data.keyword.iamlong}}) per autenticare in modo sicuro gli utenti e controllare l'accesso a tutte le risorse cloud in modo congruente in {{site.data.keyword.cloud_notm}}. 
{:shortdesc}

Per ulteriori informazioni, vedi [Gestione dell'accesso utente con IAM](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#iam).


## Concessione delle autorizzazioni a un utente per diventare un amministratore del servizio nell'account {{site.data.keyword.cloud_notm}}
{: #admin_account}

In qualità di **proprietario dell'account** o di **amministratore del servizio {{site.data.keyword.la_full_notm}}**, devi disporre delle autorizzazioni per eseguire queste azioni: 

* Concedere ad altri membri dell'account l'accesso per gestire il servizio
* Eseguire il provisioning di un'istanza del servizio
* Eliminare un'istanza del servizio
* Visualizzare i dettagli di un'istanza del servizio
* Creare un ID servizio

Pertanto, per concedere a un utente il ruolo di amministratore per gestire il servizio nell'account, l'utente deve disporre di una politica IAM per il servizio {{site.data.keyword.la_full_notm}} con il ruolo della piattaforma **Amministratore**. Devi assegnare a questo utente l'accesso a una singola risorsa nell'account. 

Completa la seguente procedura per assegnare a un utente il ruolo di amministratore per il servizio {{site.data.keyword.la_full_notm}} nell'account: 

1. Dalla barra dei menu, fai clic su **Gestisci** &gt; **Accesso (IAM)** e seleziona **Utenti**.
2. Dalla riga per l'utente a cui desideri assegnare l'accesso, seleziona il menu **Azioni** e fai quindi clic su **Assegna accesso**.
3. Seleziona **Assegna l'accesso alle risorse**.
4. Seleziona **IBM Log Analysis con LogDNA**.
5. Seleziona **Tutte le regioni correnti**.
6. Seleziona **Tutte le istanze del servizio correnti**.
7. Seleziona il ruolo della piattaforma **Amministratore**.
8. Fai clic su Assegna.


## Concessione delle autorizzazioni a un utente per diventare un amministratore del servizio in un gruppo di risorse
{: #admin_rg}

In qualità di **amministratore del servizio {{site.data.keyword.la_full_notm}}**, devi disporre delle autorizzazioni per eseguire queste azioni: 

* Concedere ad altri membri dell'account l'accesso per gestire il servizio
* Eseguire il provisioning di un'istanza del servizio
* Eliminare un'istanza del servizio
* Visualizzare i dettagli di un'istanza del servizio
* Creare un ID servizio

Pertanto, per concedere a un utente il ruolo di amministratore per gestire le istanze in un gruppo di risorse nell'account, l'utente deve disporre di una politica IAM per il servizio {{site.data.keyword.la_full_notm}} con il ruolo della piattaforma **Amministratore** nel contesto del gruppo di risorse. 

Completa la seguente procedura per assegnare a un utente il ruolo di amministratore per il servizio {{site.data.keyword.la_full_notm}} nel contesto di un gruppo di risorse: 

1. Dalla barra dei menu, fai clic su **Gestisci** &gt; **Accesso (IAM)** e seleziona **Utenti**.
2. Dalla riga per l'utente a cui desideri assegnare l'accesso, seleziona il menu **Azioni** e fai quindi clic su **Assegna accesso**.
3. Seleziona **Assegna l'accesso in un gruppo di risorse**.
4. Seleziona un gruppo di risorse.
5. Se all'utente non è stato già concesso un ruolo per il gruppo di risorse selezionato, scegli un ruolo per il campo **Assegna accesso a un gruppo di risorse**. 

    A seconda del ruolo che selezioni, l'utente può visualizzare il gruppo di risorse nel suo dashboard, modificarne il nome o gestire l'accesso degli utenti ad esso. 
    
    Puoi selezionare **Nessun accesso** se desideri che l'utente abbia accesso solo al servizio {{site.data.keyword.la_full_notm}} nel gruppo di risorse.

6. Seleziona **IBM Log Analysis con LogDNA**.
7. Seleziona il ruolo della piattaforma **Amministratore**.
8. Fai clic su **Assegna**.


## Concessione delle autorizzazioni a un utente DevOps per gestire il servizio nell'account {{site.data.keyword.cloud_notm}}
{: #devops_account}

In qualità di **utente DevOps**, devi disporre delle autorizzazioni per eseguire queste azioni: 

* Eseguire il provisioning di un'istanza del servizio
* Eliminare un'istanza del servizio
* Visualizzare i dettagli di un'istanza del servizio
* Creare un ID servizio

Devi pertanto disporre di una politica IAM per il servizio {{site.data.keyword.la_full_notm}} con il ruolo della piattaforma **Editor**.

Completa la seguente procedura per assegnare a un utente il ruolo di editor per il servizio {{site.data.keyword.la_full_notm}} nell'account: 

1. Dalla barra dei menu, fai clic su **Gestisci** &gt; **Accesso (IAM)** e seleziona **Utenti**.
2. Dalla riga per l'utente a cui desideri assegnare l'accesso, seleziona il menu **Azioni** e fai quindi clic su **Assegna accesso**.
3. Seleziona **Assegna l'accesso alle risorse**.
4. Seleziona **IBM Log Analysis con LogDNA**.
5. Seleziona **Tutte le istanze del servizio**.
6. Seleziona il ruolo della piattaforma **Editor**.
7. Fai clic su Assegna.

## Concessione delle autorizzazioni a un utente DevOps per gestire un'istanza nell'account {{site.data.keyword.cloud_notm}}
{: #devops_account_instance}

Completa la seguente procedura per assegnare a un utente il ruolo di editor su un'istanza del servizio {{site.data.keyword.la_full_notm}} nell'account: 

1. Dalla barra dei menu, fai clic su **Gestisci** &gt; **Accesso (IAM)** e seleziona **Utenti**.
2. Dalla riga per l'utente a cui desideri assegnare l'accesso, seleziona il menu **Azioni** e fai quindi clic su **Assegna accesso**.
3. Seleziona **Assegna l'accesso alle risorse**.
4. Seleziona **IBM Log Analysis con LogDNA**.
5. Seleziona l'istanza.
6. Seleziona il ruolo della piattaforma **Editor**.
7. Fai clic su Assegna.



## Concessione delle autorizzazioni a un utente DevOps per gestire il servizio in un gruppo di risorse
{: #devops_rg}

In qualità di **utente DevOps**, devi disporre delle autorizzazioni per eseguire queste azioni: 

* Eseguire il provisioning di un'istanza del servizio
* Eliminare un'istanza del servizio
* Visualizzare i dettagli di un'istanza del servizio
* Creare un ID servizio

Hai bisogno pertanto di una politica IAM per il servizio {{site.data.keyword.la_full_notm}} con il ruolo della piattaforma **Editor**.

Completa la seguente procedura per assegnare all'utente il ruolo di editor per il servizio {{site.data.keyword.la_full_notm}} nel contesto di un gruppo di risorse: 

1. Dalla barra dei menu, fai clic su **Gestisci** &gt; **Accesso (IAM)** e seleziona **Utenti**.
2. Dalla riga per l'utente a cui desideri assegnare l'accesso, seleziona il menu **Azioni** e fai quindi clic su **Assegna accesso**.
3. Seleziona **Assegna l'accesso in un gruppo di risorse**.
4. Seleziona un gruppo di risorse.
5. Se all'utente non è stato già concesso un ruolo per il gruppo di risorse selezionato, scegli un ruolo per il campo **Assegna accesso a un gruppo di risorse**. 

    A seconda del ruolo che selezioni, l'utente può visualizzare il gruppo di risorse nel suo dashboard, modificarne il nome o gestire l'accesso degli utenti ad esso. 
    
    Puoi selezionare **Nessun accesso** se desideri che l'utente abbia accesso solo al servizio {{site.data.keyword.la_full_notm}} nel gruppo di risorse.

6. Seleziona **IBM Log Analysis con LogDNA**.
7. Seleziona il ruolo della piattaforma **Editor**.
8. Fai clic su **Assegna**.

## Concessione delle autorizzazioni per gestire i log e configurare gli avvisi in LogDNA
{: #admin_user_logdna}

In qualità di **utente amministratore** in LogDNA, devi disporre delle autorizzazioni per eseguire queste azioni: 

* Aggiungere origini log LogDNA
* Visualizzare i log
* Cercare nei log
* Filtrare i log
* Configurare gli avvisi

Hai pertanto bisogno delle seguenti politiche:

* Una politica IAM per il servizio {{site.data.keyword.la_full_notm}} con il ruolo della piattaforma **Editor**. Questa politica concede le autorizzazioni per visualizzare i dettagli dell'istanza del servizio mediante la riga di comando e nel dashboard {{site.data.keyword.cloud_notm}}.
* Una politica IAM per il servizio {{site.data.keyword.la_full_notm}} con il ruolo del servizio **Gestore**. Questa politica concede le autorizzazioni per monitorare, filtrare e cercare nei log e per definire gli avvisi mediante l'IU web LogDNA.

**Nota:** in qualità di amministratore del servizio, quando concedi a un utente tali politiche, considera l'esecuzione di tale operazione nel contesto di un gruppo di risorse. Il provisioning di un'istanza {{site.data.keyword.la_full_notm}} viene eseguito nel contesto di un gruppo di risorse. Concedi, pertanto, le autorizzazioni di accesso nel contesto del gruppo di risorse.


Completa la seguente procedura per assegnare a un utente entrambe le politiche per il servizio {{site.data.keyword.la_full_notm}} nel contesto di un gruppo di risorse: 

1. Dalla barra dei menu, fai clic su **Gestisci** &gt; **Accesso (IAM)** e seleziona **Utenti**.
2. Dalla riga per l'utente a cui desideri assegnare l'accesso, seleziona il menu **Azioni** e fai quindi clic su **Assegna accesso**.
3. Seleziona **Assegna l'accesso in un gruppo di risorse**.
4. Seleziona un gruppo di risorse.
5. Se all'utente non è stato già concesso un ruolo per il gruppo di risorse selezionato, scegli un ruolo per il campo **Assegna accesso a un gruppo di risorse**. 

    A seconda del ruolo che selezioni, l'utente può visualizzare il gruppo di risorse nel suo dashboard, modificarne il nome o gestire l'accesso degli utenti ad esso. 
    
    Puoi selezionare **Nessun accesso** se desideri che l'utente abbia accesso solo al servizio {{site.data.keyword.la_full_notm}} nel gruppo di risorse.

6. Seleziona **IBM Log Analysis con LogDNA**.
7. Seleziona il ruolo della piattaforma **Editor**.
8. Seleziona il ruolo del servizio **Gestore**.
8. Fai clic su **Assegna**.

## Concessione delle autorizzazioni a un utente per visualizzare i log in LogDNA
{: #user_logdna}

In qualità di **utente**, **revisore** o **sviluppatore**, potresti aver bisogno delle autorizzazioni per eseguire queste azioni: 

* Visualizzare i log
* Cercare nei log
* Filtrare i log

Hai pertanto bisogno delle seguenti politiche:

* Una politica IAM per il servizio {{site.data.keyword.la_full_notm}} con il ruolo della piattaforma **Visualizzatore**. Questa politica concede le autorizzazioni per visualizzare i dettagli dell'istanza del servizio mediante la riga di comando e nel dashboard {{site.data.keyword.cloud_notm}}.
* Una politica IAM per il servizio {{site.data.keyword.la_full_notm}} con il ruolo del servizio **Lettore**. Questa politica concede le autorizzazioni per visualizzare, filtrare e cercare nei log mediante l'IU web LogDNA.

**Nota:** in qualità di amministratore del servizio, quando concedi a un utente tali politiche, considera l'esecuzione di tale operazione nel contesto di un gruppo di risorse. Il provisioning di un'istanza {{site.data.keyword.la_full_notm}} viene eseguito nel contesto di un gruppo di risorse. Concedi, pertanto, le autorizzazioni di accesso agli utenti nel contesto del gruppo di risorse.

Completa la seguente procedura per assegnare a un utente entrambe le politiche per il servizio {{site.data.keyword.la_full_notm}} nel contesto di un gruppo di risorse: 

1. Dalla barra dei menu, fai clic su **Gestisci** &gt; **Accesso (IAM)** e seleziona **Utenti**.
2. Dalla riga per l'utente a cui desideri assegnare l'accesso, seleziona il menu **Azioni** e fai quindi clic su **Assegna accesso**.
3. Seleziona **Assegna l'accesso in un gruppo di risorse**.
4. Seleziona un gruppo di risorse.
5. Se all'utente non è stato già concesso un ruolo per il gruppo di risorse selezionato, scegli un ruolo per il campo **Assegna accesso a un gruppo di risorse**. 

    A seconda del ruolo che selezioni, l'utente può visualizzare il gruppo di risorse nel suo dashboard, modificarne il nome o gestire l'accesso degli utenti ad esso. 
    
    Puoi selezionare **Nessun accesso** se desideri che l'utente abbia accesso solo al servizio {{site.data.keyword.la_full_notm}} nel gruppo di risorse.

6. Seleziona **IBM Log Analysis con LogDNA**.
7. Seleziona il ruolo della piattaforma **Visualizzatore**.
8. Seleziona il ruolo del servizio **Lettore**.
8. Fai clic su **Assegna**.

