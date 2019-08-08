---

copyright:
  years:  2018, 2019
lastupdated: "2019-06-03"

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

 
# Managing network connectivity
{: #network}

You can configure the LogDNA agent to connect to the logging instance through the public network or through the private network. In addition, when you have an additional firewall set up, or you have customized the firewall settings in your {{site.data.keyword.cloud_notm}} infrastructure, you need to allow outgoing network traffic to the {{site.data.keyword.la_full_notm}} service.
{:shortdesc}



## Choosing a network endpoint
{: #network_endpoints}

You can configure a LogDNA agent to connect to an {{site.data.keyword.la_full_notm}} instance through the public network or through the private network. By default, the agent connects through the public network.

The type of network defines the level of isolation and security that is configured to move workloads between cloud-based resources in your account. 

Some factors that you must consider when you must decide which network to choose are:
* Corporate requirements on how services and applications can access cloud-based services in your account
* Security on production workloads
* Industry compliance regulations

For example, you might have the following requirements when you are working in the {{site.data.keyword.cloud_notm}}:
* No access to Internet to connect to {{site.data.keyword.cloud_notm}} services
* Isolated connectivity for workloads in your account

When you have these requirements, you should move from the public network to the private network. You should consider connecting the LogDNA agent over the private network. 

You can enable virtual routing and forwarding (VRF) to move IP routing for your account and all of its resources into a separate routing table. If VRF is enabled, you can then enable {{site.data.keyword.cloud_notm}} service endpoints to connect directly to resources without using the public network. To configure an agent to send logs by using a private endpoint, you must [enable virtual routing and forwarding (VRF)](/docs/account?topic=account-vrf-service-endpoint) for your account. Once the account is VRF and service endpoint enabled, the LogDNA agent can be configured to use the private network by using the [Private Endpoint](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-endpoints) as the ingestion URL.
* Private endpoints are not accessible from the public internet. 
* All traffic is routed to the {{site.data.keyword.cloud_notm}} private network. 
* Services like {{site.data.keyword.la_full_notm}} are no longer served on an internet routable IP address.

Notice that when you configure the agent to send logs through the public network, the environment where the agent is running requires internet access to use the public endpoint.



### Limitations
{: #network_endpoints_limitations}

Consider the following limitations:
* Ingestion endpoints of type `syslog-a` and `syslog-u` are not currently supported on the Cloud Service Endpoint (CSE) network. 
* The LogDNA web UI is not currently supported on the CSE network.




## Allowing outgoing network traffic
{: #network_outgoing_traffic}

When you have an additional firewall set up, or you have customized the firewall settings in your {{site.data.keyword.cloud_notm}} infrastructure, you need to allow outgoing network traffic to the {{site.data.keyword.la_full_notm}} service. 

You must allow outgoing traffic on TCP port 443 and TCP port 80 in your firewall. For example, you must open TCP port 443 and TCP port 80 from each worker to the {{site.data.keyword.la_full_notm}} service.

The API endpoint is required for LogDNA agent authentication. The LogDNA agent gets a token that you can use to send logs to the ingestion endpoint.

If you configure the LogDNA agent to connect to the logging instance through the private network, open a support ticket to request the private IP addresses that you must enable in your firewall. For information about opening an IBM support ticket, see [Getting support](/docs/get-support?topic=get-support-getting-customer-support#getting-customer-support).
{: important}



### Ingestion IP addresses for public endpoints
{: #ips_ingestion}


The following tables list the IP addresses per region that you must configure in your firewall to allow outgoing traffic:

| Region                 | Ingestion endpoint                          | Public IP addresses                                   | Ports               |
|------------------------|---------------------------------------------|-------------------------------------------------------|---------------------|
| `Dallas (us-south)`    | `logs.us-south.logging.cloud.ibm.com`       | 169.48.237.107 </br>169.60.166.45 </br>169.47.224.77  | TCP 443 </br>TCP 80 | 
| `Frankfurt (eu-de)`    | `logs.eu-de.logging.cloud.ibm.com`          | 161.156.89.11 </br>149.81.86.68 </br>158.177.129.36   | TCP 443 </br>TCP 80 | 
| `London (eu-gb)`       | `logs.eu-gb.logging.cloud.ibm.com`          | 158.175.125.165 </br>158.176.135.133 </br>141.125.78.186  | TCP 443 </br>TCP 80 | 
| `Tokyo (jp-tok)`       | `logs.jp-tok.logging.cloud.ibm.com`         | 165.192.69.122 </br>161.202.93.253 </br>128.168.70.51 | TCP 443 </br>TCP 80 | 
{: caption="Table 1. IP addresses to send logs" caption-side="top"}



### API IP addresses for public endpoints
{: #ips_api}


| Region                | Authentication endpoint                     | Public IP addresses                                    | Ports               |
|-----------------------|---------------------------------------------|--------------------------------------------------------|---------------------|
| `Dallas (us-south)`   | `api.us-south.logging.cloud.ibm.com`        | 169.47.224.74  </br>169.60.166.44 </br>169.48.237.109  | TCP 443 </br>TCP 80 |
| `Frankfurt (eu-de)`   | `api.eu-de.logging.cloud.ibm.com`           | 149.81.86.66  </br>161.156.89.12 </br>158.177.129.34   | TCP 443 </br>TCP 80 |
| `London (eu-gb)`      | `api.eu-gb.logging.cloud.ibm.com`           | 158.176.135.132 </br>158.175.82.238 </br>141.125.78.213 | TCP 443 </br>TCP 80 |
| `Tokyo (jp-tok)`      | `api.jp-tok.logging.cloud.ibm.com`          | 165.192.71.226 </br>128.168.70.53 </br>161.202.67.2    | TCP 443 </br>TCP 80 | 
{: caption="Table 2. IP addresses used by the LogDNA agent" caption-side="top"}





