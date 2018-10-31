---

copyright:
  years:  2018
lastupdated: "2018-11-02"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}

 
# Configuring network traffic
{: #network}

When you have an additional firewall set up, or you have customized the firewall settings in your {{site.data.keyword.Bluemix_notm}} infrastructure (SoftLayer), you need to allow outgoing network traffic to the IBM Cloud Log Analysis with LogDNA service. 
{:shortdesc}


## Network traffic for custom firewall configurations in the {{site.data.keyword.Bluemix_notm}}
{: #ips}

The following table list the IP addresses per region that you must configure in your custom firewall to allow outgoing traffic:

| Region      | Ingestion URL                                     | Public IP addresses               |
|-------------|---------------------------------------------|-----------------------------------|
| US South    | To send logs: logs.us-south.logging.cloud.ibm.com  </br>Using the collector:  api.us-south.logging.cloud.ibm.com             | 169.60.166.43 </br>169.48.237.108 |
{: caption="Table 1. IP addresses" caption-side="top"}


You must allow outgoing traffic on TCP port 443 and TCP port 80 in your firewall. For example, you must open TCP port 443 and TCP port 80 from each worker to the IBM Log Analysis with LogDNA service.