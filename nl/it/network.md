---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-07"

keywords: LogDNA, IBM, Log Analysis, logging, network, IP addresses, port

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

 
# Gestione del traffico di rete
{: #network}

Quando hai un ulteriore firewall configurato, o hai personalizzato le impostazioni del firewall nella tua infrastruttura {{site.data.keyword.cloud_notm}}, devi consentire il traffico di rete in uscita al servizio {{site.data.keyword.la_full_notm}}. 
{:shortdesc}


## Traffico di rete per le configurazioni del firewall personalizzate nella regione US South (Stati Uniti Sud)
{: #ips_us-south}

Devi consentire il traffico in uscita sulla porta TCP 443 e sulla porta TCP 80 nel tuo firewall. Ad esempio, devi aprire la porta TCP 443 e la porta TCP 80 da ogni nodo di lavoro al servizio {{site.data.keyword.la_full_notm}}.

**Nota:** l'endpoint API è richiesto per l'autenticazione dell'agent LogDNA. L'agent LogDNA ottiene un token che puoi utilizzare per inviare i log all'endpoint di inserimento.

Le seguenti tabelle elencano gli indirizzi IP per ogni regione che devi configurare nel tuo firewall per consentire il traffico in uscita:

| Regione      | Endpoint di inserimento                          | Indirizzi IP pubblici               | Porte   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `US South`    | logs.us-south.logging.cloud.ibm.com         | 169.48.237.107 </br>169.60.166.45 </br>169.47.224.77  | TCP 443 </br>TCP 80 | 
{: caption="Tabella 1. Indirizzi IP per inviare i log" caption-side="top"}


| Regione      | Endpoint di autenticazione                     | Indirizzi IP pubblici               | Porte   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `US South`    | api.us-south.logging.cloud.ibm.com          | 169.47.224.74  </br>169.60.166.44 </br>169.48.237.109  | TCP 443 </br>TCP 80 |
{: caption="Tabella 2. Indirizzi IP utilizzati dall'agent LogDNA" caption-side="top"}



## Traffico di rete per le configurazioni del firewall personalizzate nella regione EU DE
{: #ips_eu-de}

Devi consentire il traffico in uscita sulla porta TCP 443 e sulla porta TCP 80 nel tuo firewall. Ad esempio, devi aprire la porta TCP 443 e la porta TCP 80 da ogni nodo di lavoro al servizio {{site.data.keyword.la_full_notm}}.

**Nota:** l'endpoint API è richiesto per l'autenticazione dell'agent LogDNA. L'agent LogDNA ottiene un token che puoi utilizzare per inviare i log all'endpoint di inserimento.

Le seguenti tabelle elencano gli indirizzi IP per ogni regione che devi configurare nel tuo firewall per consentire il traffico in uscita:

| Regione      | Endpoint di inserimento                          | Indirizzi IP pubblici               | Porte   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `EU DE`     | logs.eu-de.logging.cloud.ibm.com         | 161.156.89.11 </br>149.81.86.68 </br>158.177.129.36  | TCP 443 </br>TCP 80 | 
{: caption="Tabella 3. Indirizzi IP per inviare i log" caption-side="top"}


| Regione      | Endpoint di autenticazione                     | Indirizzi IP pubblici               | Porte   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `EU DE`     | api.eu-de.logging.cloud.ibm.com          | 161.156.89.12  </br>149.81.86.66 </br>158.177.129.34    | TCP 443 </br>TCP 80 |
{: caption="Tabella 4. Indirizzi IP utilizzati dall'agent LogDNA" caption-side="top"}


