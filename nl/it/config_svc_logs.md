---

copyright:
  years:  2018, 2019
lastupdated: "2019-04-02"

keywords: LogDNA, IBM, Log Analysis, logging instance, enable, service logs

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

# Configurazione dei log del servizio {{site.data.keyword.cloud_notm}} 
{: #config_svc_logs}

Puoi avere più istanze {{site.data.keyword.la_full_notm}} in una regione. Tuttavia, solo 1 istanza in una regione può essere configurata per ricevere i log dai servizi abilitati in {{site.data.keyword.cloud_notm}}.
{:shortdesc}



## Configurazione dei servizi di piattaforma tramite il dashboard Osservabilità 
{: #config_svc_logs_ui}

Per configurare un'istanza dal dashboard Osservabilità in {{site.data.keyword.cloud_notm}}, completa la seguente procedura:

1. [Accedi al tuo account {{site.data.keyword.cloud_notm}} ![Icona link esterno](../../icons/launch-glyph.svg "Icona link esterno")](https://cloud.ibm.com/login){:new_window}.

	Dopo che hai eseguito l'accesso con il tuo ID utente e la tua password, viene aperta l'IU {{site.data.keyword.cloud_notm}}.

2. Vai all'icona di menu ![icona di menu](../../icons/icon_hamburger.svg). Seleziona quindi **Osservabilità** per accedere al dashboard *Osservabilità*.

3. Seleziona **Registrazione** e fai quindi clic su **Configura i log dei servizi di piattaforma**. 

4. Scegli quale istanza LogDNA riceverà i log dai servizi abilitati sulla piattaforma cloud.

5. Seleziona una regione. 

6. Seleziona un'istanza.

7. Fai clic su **Salva**. 

Si apre la pagina principale *Osservabilità*.

L'istanza che scegli per ricevere i log del servizio mostra l'indicatore **Log dei servizi di piattaforma**.

Per ulteriori informazioni sui servizi abilitati per inviare i log a {{site.data.keyword.la_full_notm}}, vedi [Servizi cloud](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services).

