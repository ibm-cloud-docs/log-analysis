---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-07"

keywords: LogDNA, IBM, Log Analysis, logging, getting started

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

# Esercitazione introduttiva
{: #getting-started}

Utilizza {{site.data.keyword.la_full}} per aggiungere funzionalità di gestione dei log alla tua architettura di {{site.data.keyword.cloud_notm}}. {{site.data.keyword.la_full_notm}} è gestito da LogDNA in collaborazione con {{site.data.keyword.IBM_notm}}.
{:shortdesc}


## Passo 1. Prima di iniziare
{: #getting-started_prereqs}

* Leggi a proposito di {{site.data.keyword.la_full_notm}}. Per ulteriori informazioni, vedi [Informazioni su {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).
* Controlla le regioni in cui è disponibile il servizio. Per ulteriori informazioni, vedi [Regioni](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_regions).
* Ottieni un ID utente che sia un membro o un proprietario di un account {{site.data.keyword.cloud_notm}}. 

    Per ottenere un ID utente {{site.data.keyword.cloud_notm}}, fai clic su [Registrazione ![Icona link esterno](../../icons/launch-glyph.svg "Icona link esterno")](https://cloud.ibm.com/login){:new_window}.



## Passo 2. Inizia a lavorare
{: #getting-started_step2}

Scegli una risorsa cloud per cui desideri gestire i log. Configura quindi questa origine log in modo da poterne monitorare i log mediante il servizio {{site.data.keyword.la_full_notm}}. L'origine log può trovarsi nella stessa regione in cui esegui il provisioning di un'istanza {{site.data.keyword.la_full_notm}} oppure in una regione differente.

La seguente tabella elenca degli esempi di risorse cloud che puoi configurare per archiviare e gestire i log utilizzando il servizio {{site.data.keyword.la_full_notm}}. Completa l'esercitazione per una risorsa per iniziare a lavorare con il servizio {{site.data.keyword.loganalysisshort}}:

<table>
  <caption>Esercitazioni per iniziare a lavorare con il servizio {{site.data.keyword.la_full_notm}} </caption>
  <tr>
    <th>Risorsa</th>
    <th>Esercitazione</th>
    <th>Ambiente</th>
    <th>Scenario</th>
  </tr>
  <tr>
    <td>Contenitori in esecuzione in {{site.data.keyword.containershort}}</td>
    <td>[Gestione dei log di cluster Kubernetes con {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-kube#kube)</td>
    <td>{{site.data.keyword.cloud_notm}} pubblico </td>
    <td>![{{site.data.keyword.containershort}} e {{site.data.keyword.la_full_notm}}](images/kube.png "{{site.data.keyword.containershort}} e {{site.data.keyword.la_full_notm}}")</td>
  </tr>
  <tr>
    <td>Linux Ubuntu, Linux Debian</td>
    <td>[Gestione dei log Linux Ubuntu con {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-ubuntu#ubuntu)</td>
    <td>In loco</td>
    <td>![Server Ubuntu e {{site.data.keyword.la_full_notm}}](images/ubuntu.png "Server Ubuntu e {{site.data.keyword.la_full_notm}}")</td>
  </tr>
</table>



## Passo 3. Esegui l'upgrade del piano
{: #getting-started_step3}

Abilita ulteriori funzioni di registrazione.

Esegui l'upgrade del piano di servizio {{site.data.keyword.la_full_notm}} a un piano a pagamento per poter [filtrare i log](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5), [cercare nei log](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6), [definire le viste](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7) e [configurare gli avvisi](https://docs.logdna.com/docs/alerts). Per ulteriori informazioni sui piani di servizio {{site.data.keyword.la_full_notm}}, vedi [Piani di prezzo](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

## Passo 4. Passi successivi 
{: #getting-started_iam}

Gestisci quindi l'accesso utente con IAM.

Identifica le politiche IAM di cui un utente ha bisogno per lavorare con il servizio {{site.data.keyword.la_full_notm}}.

Per ulteriori informazioni sull'integrazione IAM con il servizio {{site.data.keyword.la_full_notm}}, vedi [Gestione dell'accesso utente con IAM](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#iam).

Ad esempio, scegli un singolo ruolo utente per imparare come concedere autorizzazioni a tale utente per lavorare con il servizio {{site.data.keyword.la_full_notm}}, 

| Ruolo utente in {{site.data.keyword.cloud_notm}} | Per ulteriori informazioni                     |
|-----------------------------------------------------|------------------------------------------|
| Proprietario dell'account                                       | [Concessione delle autorizzazioni a un utente per diventare un amministratore del servizio nell'account {{site.data.keyword.cloud_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account) |
| Amministratore del servizio della piattaforma nell'account       | [Concessione delle autorizzazioni a un utente per diventare un amministratore del servizio nell'account {{site.data.keyword.cloud_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account) |
| Amministratore del servizio della piattaforma in un gruppo di risorse  | [Concessione delle autorizzazioni a un utente per diventare un amministratore del servizio in un gruppo di risorse](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_rg) |
| Operatore DevOps della piattaforma nell'account           | [Concessione delle autorizzazioni a un utente DevOps per gestire il servizio nell'account {{site.data.keyword.cloud_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#devops_account) |
| Operatore DevOps della piattaforma in un gruppo di risorse        | [Concessione delle autorizzazioni a un utente DevOps per gestire il servizio in un gruppo di risorse](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#devops_rg) |
| Amministratore del servizio in LogDNA                     | [Concessione delle autorizzazioni per gestire i log e configurare gli avvisi in LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna)              |
| Utente / Sviluppatore                                    | [Concessione delle autorizzazioni a un utente per visualizzare e gestire i log in LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna)               |
{: caption="Tabella 2. Ruoli cloud in {{site.data.keyword.cloud_notm}}" caption-side="top"}


