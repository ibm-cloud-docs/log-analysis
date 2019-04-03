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

# Concessione di autorizzazioni per gestire i log e visualizzare i log dell'account
{: #grant_permissions}

In {{site.data.keyword.Bluemix}}, puoi assegnare a un utente uno o più ruoli IAM. Questi ruoli definiscono quali attività sono abilitate per tale utente per lavorare con il servizio {{site.data.keyword.loganalysisshort}}.  
{:shortdesc}

Ad esempio, puoi concedere a un utente il ruolo **operatore** per consentirgli di gestire i log. Se vuoi che l'utente visualizzi solo i log dell'account, puoi concedergli il ruolo di **visualizzatore**. Per ulteriori informazioni, vedi [Ruoli IAM](/docs/services/CloudLogAnalysis/security_ov.html#iam_roles).

**Nota:** 

* Per concedere a un utente le autorizzazioni per gestire i log o per visualizzare i log dell'account, devi disporre delle autorizzazioni per assegnare le politiche ad altri utenti nell'account o devi essere il proprietario dell'account. Se non sei il proprietario dell'account, devi avere una politica IAM con il ruolo di editor, operatore o amministratore.
* Per concedere a un utente le autorizzazioni per visualizzare i log in uno spazio, devi disporre delle autorizzazioni nell'organizzazione e nello spazio per assegnare all'utente un ruolo Cloud Foundry che descrive le azioni che tale utente può effettuare con il servizio {{site.data.keyword.loganalysisshort}} in tale spazio. 

## Assegna una politica IAM a un utente tramite la IU {{site.data.keyword.Bluemix_notm}}
{: #grant_permissions_ui_account}

Completa la seguente procedura per concedere a un utente le autorizzazioni a lavorare con il servizio {{site.data.keyword.loganalysisshort}}:

1. Accedi alla console {{site.data.keyword.Bluemix_notm}}.

    Apri un browser web e avvia il dashboard {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Icona di link esterno](../../../icons/launch-glyph.svg "Icona di link esterno")](http://bluemix.net){:new_window}
	
	Dopo che hai eseguito l'accesso con il tuo ID utente e la tua password, viene aperta la IU {{site.data.keyword.Bluemix_notm}}.

2. Dalla barra dei menu, fai clic su **Gestisci > Account > Utenti**. 

    La finestra *Utenti* visualizza un elenco di utenti con i loro indirizzi email per l'account attualmente selezionato.
	
3. Se l'utente è un membro dell'account, seleziona il suo nome dall'elenco o fai clic su **Gestisci utente** dal menu *Azioni*.

    Se l'utente non è un membro dell'account, vedi [Invito di utenti](/docs/iam/iamuserinv.html#iamuserinv).

4. Nella sezione **Politiche di accesso**, fai clic su **Assegna accesso** e seleziona quindi **Assegna l'accesso alle risorse**.

    Viene visualizzata la finestra *Assegna l'accesso alla risorsa a (utente)**.

5. Immetti le informazioni sulla politica. La seguente tabella elenca i campi obbligatori per definire una politica: 

    <table>
	  <caption>Elenco di campi per configurare una politica IAM.</caption>
	  <tr>
	    <th>Campo</th>
		<th>Valore</th>
	  </tr>
	  <tr>
	    <td>Servizi</td>
		<td>*IBM Cloud Log Analysis*</td>
	  </tr>	  
	  <tr>
	    <td>Regioni</td>
		<td>Puoi specificare le regioni a cui all'utente verrà concesso l'accesso per lavorare con i log. Seleziona una o più regioni singolarmente oppure seleziona **Tutte le regioni correnti** per concedere l'accesso a tutte le regioni.</td>
	  </tr>
	  <tr>
	    <td>Istanza di servizio</td>
		<td>Seleziona *Tutte le istanze del servizio*.</td>
	  </tr>
	  <tr>
	    <td>Ruoli</td>
		<td>Seleziona uno o più ruoli IAM. <br>I ruoli validi sono: *amministratore*, *operatore*, *editor* e *visualizzatore*. <br>Per ulteriori informazioni sulle azioni consentite per ogni ruolo, vedi [Ruoli IAM](/docs/services/CloudLogAnalysis/security_ov.html#iam_roles).
		</td>
	  </tr>
     </table>
	
6. Fai clic su **Assegna**.
	
La politica che configuri è applicabile alle regioni selezionate. 


## Assegna una politica IAM a un utente utilizzando la riga di comando
{: #grant_permissions_commandline}

Completa la seguente procedura per concedere a un utente l'accesso per visualizzare i log dell'account utilizzando la riga di comando:

1. Da un terminale, accedi all'account {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Controlla che l'utente sia un membro dell'account. Esegui il seguente comando per ottenere l'elenco degli utenti nell'account:

    ```
	ibmcloud account users
	```
    {: codeblock}	

	Viene visualizzato un elenco di utenti con i relativi GUID.

3. Se l'utente non è un membro dell'account, contatta il proprietario dell'account e richiedi un invito per tale utente nell'account. Per ulteriori informazioni, vedi [Invito di utenti](/docs/iam/iamuserinv.html#iamuserinv).

    **Suggerimento:** il comando per invitare un utente in un account è il seguente: `ibmcloud iam account-user-invite USER_EMAIL`
		
4. Assegna una politica all'utente. Esegui il seguente comando:

    ```
    ibmcloud iam user-policy-create USER_NAME --roles ROLE --service-name ibmloganalysis
	```
	{: codeblock}

	dove
    * USER_NAME è l'ID {{site.data.keyword.Bluemix_notm}} dell'utente.
	* ROLE è un ruolo IAM. I valori validi sono: *amministratore*, *operatore*, *editor* e *visualizzatore*

5. Verifica che la politica sia assegnata all'utente. Immetti il seguente comando per elencare tutte le politiche assegnate a un utente:

    ```
    ibmcloud iam user-policies USER_NAME
	```
	{: codeblock}




## Concessione delle autorizzazioni a un utente per visualizzare i log dello spazio utilizzando la IU {{site.data.keyword.Bluemix_notm}}
{: #grant_permissions_ui_space}

Per concedere a un utente le autorizzazioni per visualizzare i log in uno spazio, devi assegnare all'utente un ruolo Cloud Foundry che descriva le azioni che questo utente può eseguire con il servizio {{site.data.keyword.loganalysisshort}} nello spazio. 

Completa la seguente procedura per concedere a un utente le autorizzazioni a lavorare con il servizio {{site.data.keyword.loganalysisshort}}:

1. Accedi alla console {{site.data.keyword.Bluemix_notm}}.

    Apri un browser web e avvia il dashboard {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Icona di link esterno](../../../icons/launch-glyph.svg "Icona di link esterno")](http://bluemix.net){:new_window}
	
	Dopo che hai eseguito l'accesso con il tuo ID utente e la tua password, viene aperta la IU {{site.data.keyword.Bluemix_notm}}.

2. Dalla barra dei menu, fai clic su **Gestisci > Account > Utenti**. 

    La finestra *Utenti* visualizza un elenco di utenti con i loro indirizzi email per l'account attualmente selezionato.
	
3. Se l'utente è un membro dell'account, seleziona il suo nome dall'elenco o fai clic su **Gestisci utente** dal menu *Azioni*.

    Se l'utente non è un membro dell'account, vedi [Invito di utenti](/docs/iam/iamuserinv.html#iamuserinv).

4. Seleziona **Accesso Cloud Foundry** e seleziona quindi l'organizzazione.

    Viene presentato l'elenco di spazi disponibili in tale organizzazione.

5. Scegli uno spazio. Quindi, dal menu delle azioni, seleziona **Modifica ruolo spazio**.

6. Seleziona 1 o più ruoli spazio. I ruoli validi sono: *Gestore*, *Sviluppatore * e *Revisore*
	
7. Fai clic su **Salva ruolo**.




