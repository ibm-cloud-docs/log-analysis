---

copyright:
  years: 2018, 2021
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, security, connection

subcollection: Log-Analysis-with-LogDNA

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:codeblock: .codeblock}
{:tip: .tip}
{:note: .note}
{:important: .important}
{:deprecated: .deprecated}
{:download: .download}
{:preview: .preview}


# Securing your connection
{: #service-connection}

To ensure that you have enhanced control and security over your data when you use {{site.data.keyword.la_full}}, you have the option that use private routes to {{site.data.keyword.cloud_notm}} service endpoints. Private routes are not accessible or reachable over the internet. By using the {{site.data.keyword.cloud_notm}} Private service endpoints feature, you can protect your data from threats from the public network and logically extend your private network.
{: shortdesc}


## Before you begin
{: #prereq-service-endpoint}

Consider the following factors when you must decide which network to choose:
* Corporate requirements on how services and applications can access cloud-based services in your account.
* Security on production workloads.
* Industry compliance regulations.

For example, you might have the following requirements when you are working in the {{site.data.keyword.cloud_notm}}:
* No access to Internet to connect to {{site.data.keyword.cloud_notm}} services.
* Isolated connectivity for workloads in your account.

When you have these requirements, consider moving from the public network to the private network.

You can configure a logging agent to connect to an {{site.data.keyword.la_full_notm}} instance through the public network or through the private network. By default, the agent connects through the public network.
{: note}

The type of network defines the level of isolation and security that is configured to move workloads between cloud-based resources in your account. Consider connecting the logging agent over the private network.
{: tip}


## Setting up private service endpoints for {{site.data.keyword.la_full_notm}}
{: #endpoint-setup}

Private network endpoints support routing services over the {{site.data.keyword.cloud_notm}} Private network instead of the public network. 

* A private network endpoint provides a unique IP address that is accessible to you without a VPN connection.
* Private endpoints work between regions offering a global network. You can run your applications and services in Dallas, and connect to a logging instance in Sydney with a private endpoint.



### Step 1. Enabling your account
{: #endpoint-setup-step1}

To use private network endpoints, the following account features must be enabled for your account:
* Virtual routing and forwarding (VRF)
* Service endpoints

    Enabling service endpoints means that all users in the account can connect to private network endpoints.
    {: note}

You must first enable virtual routing and forwarding in your account, and then you can enable the use of IBM Cloud private service endpoints. 
* To enable VRF, you create a support case. 
* To enable service endpoints, you use the {{site.data.keyword.cloud_notm}} CLI. For more information about how to enable your account, see [Enabling VRF and service endpoints](/docs/account?topic=account-vrf-service-endpoint).


### Step 2. Setting a private endpoint
{: #endpoint-setup-step2}

After your account is enabled for VRF and service endpoints, you can configure a logging agent to connect to an {{site.data.keyword.la_full_notm}} instance through the private network. 

A service instance can have a private network endpoint, a public network endpoint, or both.
* A public network endpoint is a service endpoint on the {{site.data.keyword.cloud_notm}} public network.
* A private network endpoint is a service endpoint that is accessible only on the {{site.data.keyword.cloud_notm}} Private network.


The {{site.data.keyword.la_full_notm}} service offers the following private endpoints:


| Region                   | Private Endpoint                                       | Ports and private IP addresses for the default log data endpoint| Ports and private IP addresses for the TCP syslog data endpoint| Ports and private IP addresses for the UDP syslog data endpoint|
|--------------------------|--------------------------------------------------------|--------------------------------------------------------|
| `Chennai (in-che)`      | `https://api.private.in-che.logging.cloud.ibm.com`   | TCP 443, TCP 80 for 166.9.40.2, 166.9.40.3, 166.9.42.3, 166.9.42.4, 166.9.46.5, 166.9.46.6, 166.9.60.6, 166.9.60.7 | TCP 514, TCP 6514 for 166.9.40.23, 166.9.42.26, 166.9.46.8, 166.9.60.9 | UDP 514 for 166.9.40.24, 166.9.42.27, 166.9.46.9, 166.9.60.10 |
| `Dallas (us-south)`      | `https://api.private.us-south.logging.cloud.ibm.com`   | TCP 443, TCP 80 for 166.9.12.12, 166.9.12.13, 166.9.14.2, 166.9.14.3, 166.9.16.11, 166.9.16.12 | TCP 514, TCP 6514 for 166.9.12.15, 166.9.14.5, 166.9.16.14 | UDP 514 for 166.9.12.16, 166.9.14.6, 166.9.16.15  |
| `Frankfurt (eu-de)`      | `https://api.private.eu-de.logging.cloud.ibm.com`      | TCP 443, TCP 80 for 166.9.28.2, 166.9.28.3, 166.9.32.21, 166.9.32.7 | TCP 514, TCP 6514 for 166.9.28.5, 166.9.32.23 | UDP 514 for 166.9.28.7, 166.9.32.24 |
| `London (eu-gb)`         | `https://api.private.eu-gb.logging.cloud.ibm.com`      | TCP 443, TCP 80 for 166.9.34.2, 166.9.34.4, 166.9.36.2, 166.9.36.3, 166.9.38.4, 166.9.38.5 | TCP 514, TCP 6514 for 166.9.34.18, 166.9.36.5, 166.9.38.20 | UDP 514 for 166.9.34.19, 166.9.36.6, 166.9.38.21 |
| `Tokyo (jp-tok)`         | `https://api.private.jp-tok.logging.cloud.ibm.com`     | TCP 443, TCP 80 for 166.9.40.2, 166.9.40.3, 166.9.42.3, 166.9.42.4, 166.9.46.5, 166.9.46.6, 166.9.60.6, 166.9.60.7 | TCP 514, TCP 6514 for 166.9.40.23, 166.9.42.26, 166.9.46.8, 166.9.60.9 | UDP 514 for 166.9.40.24, 166.9.42.27, 166.9.46.9, 166.9.60.10 |
| `Seoul (kr-seo)`         | `https://api.private.kr-seo.logging.cloud.ibm.com`     | TCP 443, TCP 80 for 166.9.40.2, 166.9.40.3, 166.9.42.3, 166.9.42.4, 166.9.46.5, 166.9.46.6, 166.9.60.6, 166.9.60.7 | TCP 514, TCP 6514 for 166.9.40.23, 166.9.42.26, 166.9.46.8, 166.9.60.9 | UDP 514 for 166.9.40.24, 166.9.42.27, 166.9.46.9, 166.9.60.10 |
| `Sydney (au-syd)`        | `https://api.private.au-syd.logging.cloud.ibm.com`     | TCP 443, TCP 80 for 166.9.52.5, 166.9.52.2, 166.9.56.3, 166.9.56.20 | TCP 514, TCP 6514 for 166.9.56.22, 166.9.52.8 | UDP 514 for 166.9.56.23, 166.9.52.9 |
| `Washington (us-east)`   | `https://api.private.us-east.logging.cloud.ibm.com`     | TCP 443, TCP 80 for 166.9.20.72, 166.9.20.73, 166.9.22.35, 166.9.22.36 | TCP 514, TCP 6514 for 166.9.20.76, 166.9.22.38 | UDP 514 for 166.9.20.77, 166.9.22.39 |
{: caption="Table 1. Lists of private API endpoints for interacting with {{site.data.keyword.la_full_notm}}." caption-side="top"}

### Step 3. Configure your logging agent
{: #endpoint-setup-step3}

You can [configure the logging agent](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-logdna_agent) to use the private network by using a private endpoint as the ingestion URL.

What happens when you configure the logging agent to use a private endpoint?
* Private endpoints are not accessible from the public internet. 
* All traffic is routed to the {{site.data.keyword.cloud_notm}} Private network. 
* Services like {{site.data.keyword.la_full_notm}} are no longer served on an internet routable IP address.




## Limitations that use private endpoints
{: #network_endpoints_limitations}

Consider the following limitations:
* Ingestion endpoints of type `syslog-tcp (syslog-a)` and `syslog-udp (syslog-u)` are not currently supported on the Cloud Service Endpoint (CSE) network. 
* The logging web UI is not currently supported on the private network.



## Allowing outgoing network traffic
{: #network_outgoing_traffic}

When you have an extra firewall set up, or you customize the firewall settings in your {{site.data.keyword.cloud_notm}} infrastructure, you need to allow outgoing network traffic to the {{site.data.keyword.la_full_notm}} service. 

You must allow outgoing traffic on TCP port 443 and TCP port 80 in your firewall. For example, you must open TCP port 443 and TCP port 80 from each worker to the {{site.data.keyword.la_full_notm}} service.

The API endpoint is required for logging agent authentication. The logging agent gets a token that you can use to send logs to the ingestion endpoint.

If you configure the logging agent to connect to the logging instance through the **private network**, open a support ticket to request the private IP addresses that you must enable in your firewall. For more information about opening an IBM support ticket, see [Getting support](/docs/get-support).
{: important}



### Ingestion IP addresses for public endpoints
{: #ips_ingestion}


The following tables list the IP addresses per region that you must configure in your firewall to allow outgoing traffic:

| Region                 | Ingestion endpoint                          | Public IP addresses                                   | Ports               |
|------------------------|---------------------------------------------|-------------------------------------------------------|---------------------|
| `Chennai (in-che)`     | `logs.in-che.logging.cloud.ibm.com`         | 169.38.128.164                                        | TCP 443 </br>TCP 80 |
| `Dallas (us-south)`    | `logs.us-south.logging.cloud.ibm.com`       | 169.48.237.107 </br>169.60.166.45 </br>169.47.224.77  | TCP 443 </br>TCP 80 | 
| `Frankfurt (eu-de)`    | `logs.eu-de.logging.cloud.ibm.com`          | 161.156.89.11 </br>149.81.86.68 </br>158.177.129.36   | TCP 443 </br>TCP 80 | 
| `London (eu-gb)`       | `logs.eu-gb.logging.cloud.ibm.com`          | 158.175.125.165 </br>158.176.135.133 </br>141.125.78.186  | TCP 443 </br>TCP 80 | 
| `Seoul (kr-seo)`       | `logs.kr-seo.logging.cloud.ibm.com`         | 169.56.70.98                                          | TCP 443 </br>TCP 80 |
| `Sydney (au-syd)`      | `logs.au-syd.logging.cloud.ibm.com`         | 130.198.89.45 </br>135.90.67.187 </br>168.1.38.92     | TCP 443 </br>TCP 80 |
| `Tokyo (jp-tok)`       | `logs.jp-tok.logging.cloud.ibm.com`         | 165.192.69.122 </br>161.202.93.253 </br>128.168.70.51 | TCP 443 </br>TCP 80 | 
| `Washington (us-east)` | `logs.us-east.logging.cloud.ibm.com`        | 169.61.65.235 </br>169.63.163.51 </br>169.47.52.83    | TCP 443 </br>TCP 80 | 
{: caption="Table 2. IP addresses to send logs." caption-side="top"}



### API IP addresses for public endpoints
{: #ips_api}


| Region                | Authentication endpoint                     | Public IP addresses                                    | Ports               |
|-----------------------|---------------------------------------------|--------------------------------------------------------|---------------------|
| `Chennai (in-che)`    | `api.in-che.logging.cloud.ibm.com`          | 169.38.82.170                                          | TCP 443 </br>TCP 80 |
| `Dallas (us-south)`   | `api.us-south.logging.cloud.ibm.com`        | 169.47.224.74  </br>169.60.166.44 </br>169.48.237.109  | TCP 443 </br>TCP 80 |
| `Frankfurt (eu-de)`   | `api.eu-de.logging.cloud.ibm.com`           | 149.81.86.66  </br>161.156.89.12 </br>158.177.129.34   | TCP 443 </br>TCP 80 |
| `London (eu-gb)`      | `api.eu-gb.logging.cloud.ibm.com`           | 158.176.135.132 </br>158.175.82.238 </br>141.125.78.213 | TCP 443 </br>TCP 80 |
| `Seoul (kr-seo)`      | `api.kr-seo.logging.cloud.ibm.com`          | 169.56.70.102                                          | TCP 443 </br>TCP 80 |
| `Sydney (au-syd)`     | `api.au-syd.logging.cloud.ibm.com`          | 130.198.89.43 </br>135.90.70.75 </br>168.1.38.90       | TCP 443 </br>TCP 80 |
| `Tokyo (jp-tok)`      | `api.jp-tok.logging.cloud.ibm.com`          | 165.192.71.226 </br>128.168.70.53 </br>161.202.67.2    | TCP 443 </br>TCP 80 | 
| `Washington (us-east)`| `api.us-east.logging.cloud.ibm.com`         | 169.47.43.67 </br>169.62.55.212 </br>169.60.95.75      | TCP 443 </br>TCP 80 |
{: caption="Table 3. IP addresses used by the logging agent." caption-side="top"}
