---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

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

 
# Managing network traffic
{: #network}

When you have an additional firewall set up, or you have customized the firewall settings in your {{site.data.keyword.cloud_notm}} infrastructure, you need to allow outgoing network traffic to the IBM Cloud Log Analysis with LogDNA service. 
{:shortdesc}


## Network traffic for custom firewall configurations in the US South region
{: #ips_us-south}

You must allow outgoing traffic on TCP port 443 and TCP port 80 in your firewall. For example, you must open TCP port 443 and TCP port 80 from each worker to the {{site.data.keyword.la_full_notm}} service.

**Note:** The API endpoint is required for LogDNA agent authentication. The LogDNA agent gets a token that you can use to send logs to the Ingestion endpoint.

The following tables list the IP addresses per region that you must configure in your firewall to allow outgoing traffic:

| Region      | Ingestion endpoint                          | Public IP addresses               | Ports   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `US South`    | logs.us-south.logging.cloud.ibm.com         | 169.48.237.107 </br>169.60.166.45 </br>169.47.224.77  | TCP 443 </br>TCP 80 | 
{: caption="Table 1. IP addresses to send logs" caption-side="top"}


| Region      | Authentication endpoint                     | Public IP addresses               | Ports   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `US South`    | api.us-south.logging.cloud.ibm.com          | 169.47.224.74  </br>169.60.166.44 </br>169.48.237.109  | TCP 443 </br>TCP 80 |
{: caption="Table 2. IP addresses used by the LogDNA agent" caption-side="top"}



## Network traffic for custom firewall configurations in the EU DE region
{: #ips_eu-de}

You must allow outgoing traffic on TCP port 443 and TCP port 80 in your firewall. For example, you must open TCP port 443 and TCP port 80 from each worker to the {{site.data.keyword.la_full_notm}} service.

**Note:** The API endpoint is required for LogDNA agent authentication. The LogDNA agent gets a token that you can use to send logs to the Ingestion endpoint.

The following tables list the IP addresses per region that you must configure in your firewall to allow outgoing traffic:

| Region      | Ingestion endpoint                          | Public IP addresses               | Ports   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `EU DE`     | logs.eu-de.logging.cloud.ibm.com         | 161.156.89.11 </br>149.81.86.68 </br>158.177.129.36  | TCP 443 </br>TCP 80 | 
{: caption="Table 3. IP addresses to send logs" caption-side="top"}


| Region      | Authentication endpoint                     | Public IP addresses               | Ports   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `EU DE`     | api.eu-de.logging.cloud.ibm.com          | 161.156.89.12  </br>149.81.86.66 </br>158.177.129.34    | TCP 443 </br>TCP 80 |
{: caption="Table 4. IP addresses used by the LogDNA agent" caption-side="top"}


