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

 
# Netzverkehr verwalten
{: #network}

Wenn eine zusätzliche Firewall eingerichtet ist oder wenn Sie die Firewalleinstellungen in Ihrer {{site.data.keyword.cloud_notm}}-Infrastruktur angepasst haben, müssen Sie ausgehenden Netzverkehr an den {{site.data.keyword.la_full_notm}}-Service zulassen. 
{:shortdesc}


## Netzverkehr für angepasste Firewallkonfigurationen in der Region US South
{: #ips_us-south}

Sie müssen ausgehenden Datenverkehr an TCP-Port 443 und TCP-Port 80 in Ihrer Firewall zulassen. Sie müssen z. B. TCP-Port 443 und TCP-Port 80 auf jedem Workerknoten zum {{site.data.keyword.la_full_notm}}-Service öffnen.

**Anmerkung:** Der API-Endpunkt ist für die Authentifizierung des LogDNA-Agenten erforderlich. Der LogDNA-Agent ruft ein Token ab, das Sie zum Senden von Protokollen an den Aufnahmeendpunkt verwenden können.

Die folgenden Tabellen enthalten eine Auflistung der IP-Adressen nach Region, die Sie in Ihrer Firewall konfigurieren müssen, damit ausgehender Datenverkehr möglich ist.

| Region      | Aufnahmeendpunkt                          | Öffentliche IP-Adressen               | Ports   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `US South`    | logs.us-south.logging.cloud.ibm.com         | 169.48.237.107 </br>169.60.166.45 </br>169.47.224.77  | TCP 443 </br>TCP 80 | 
{: caption="Tabelle 1. IP-Adressen zum Senden von Protokollen" caption-side="top"}


| Region      | Authentifizierungsendpunkt                     | Öffentliche IP-Adressen               | Ports   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `US South`    | api.us-south.logging.cloud.ibm.com          | 169.47.224.74  </br>169.60.166.44 </br>169.48.237.109  | TCP 443 </br>TCP 80 |
{: caption="Tabelle 2. Vom LogDNA-Agenten verwendete IP-Adressen" caption-side="top"}



## Netzverkehr für angepasste Firewallkonfigurationen in der Region EU DE
{: #ips_eu-de}

Sie müssen ausgehenden Datenverkehr an TCP-Port 443 und TCP-Port 80 in Ihrer Firewall zulassen. Sie müssen z. B. TCP-Port 443 und TCP-Port 80 auf jedem Workerknoten zum {{site.data.keyword.la_full_notm}}-Service öffnen.

**Anmerkung:** Der API-Endpunkt ist für die Authentifizierung des LogDNA-Agenten erforderlich. Der LogDNA-Agent ruft ein Token ab, das Sie zum Senden von Protokollen an den Aufnahmeendpunkt verwenden können.

Die folgenden Tabellen enthalten eine Auflistung der IP-Adressen nach Region, die Sie in Ihrer Firewall konfigurieren müssen, damit ausgehender Datenverkehr möglich ist.

| Region      | Aufnahmeendpunkt                          | Öffentliche IP-Adressen               | Ports   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `EU DE`     | logs.eu-de.logging.cloud.ibm.com         | 161.156.89.11 </br>149.81.86.68 </br>158.177.129.36  | TCP 443 </br>TCP 80 | 
{: caption="Tabelle 3. IP-Adressen zum Senden von Protokollen" caption-side="top"}


| Region      | Authentifizierungsendpunkt                     | Öffentliche IP-Adressen               | Ports   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `EU DE`     | api.eu-de.logging.cloud.ibm.com          | 161.156.89.12  </br>149.81.86.66 </br>158.177.129.34    | TCP 443 </br>TCP 80 |
{: caption="Tabelle 4. Vom LogDNA-Agenten verwendete IP-Adressen" caption-side="top"}


