---

copyright:
  years: 2019
lastupdated: "2019-08-12"

keywords: IBM Cloud, LogDNA, Activity Tracker, endpoints

subcollection: logdnaat

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

# Endpoints
{: #endpoints}

Review the connectivity options for interacting with {{site.data.keyword.la_full}}.
{:shortdesc}



## Connectivity options
{: #connectivity-options}

{{site.data.keyword.la_full_notm}} offers two connectivity options:

<dl>
    <dt>Public endpoints</dt>
        <dd>By default, you can connect to resources in your account over the {{site.data.keyword.cloud_notm}} public network. Your data is encrypted in transit by using the Transport Security Layer (TLS) 1.2 protocol.
        </dd>
    <dt>Private endpoints</dt>
        <dd>For added benefits, you can also enable <a href="/docs/account?topic=account-vrf-service-endpoint#vrf" target="_blank" class="external"> virtual routing and forwarding (VRF)</a> and <a href="/docs/account?topic=account-vrf-service-endpoint" target="_blank" class="external"> service endpoints</a> for your infrastructure account. When you enable VRF for your account, you can connect to {{site.data.keyword.la_full_notm}} by using a private IP that is accessible only through the {{site.data.keyword.cloud_notm}} private network. To learn more about VRF, see <a href="/docs/resources?topic=direct-link-overview-of-virtual-routing-and-forwarding-vrf-on-ibm-cloud" target="_blank" class="external">Virtual routing and forwarding on {{site.data.keyword.cloud_notm}}</a>. To learn how to connect to {{site.data.keyword.la_full_notm}} by using a private endpoint, see <a href="/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-network#network_endpoints">Choosing a service endpoint</a>.
        </dd>
</dl>

[Learn more.](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-network)

## API endpoints
{: #endpoints_api}

The following table shows the API endpoints:

| Region                   |  Public Endpoint                                   |
|--------------------------|----------------------------------------------------|
| `Dallas (us-south)`      | `https://api.us-south.logging.cloud.ibm.com`       |
| `Frankfurt (eu-de)`      | `https://api.eu-de.logging.cloud.ibm.com`          |
| `London (eu-gb)`         | `https://api.eu-gb.logging.cloud.ibm.com`          |
| `Tokyo (jp-tok)`         | `https://api.jp-tok.logging.cloud.ibm.com`         |
{: caption="Table 1. Lists of public API endpoints for interacting with {{site.data.keyword.la_full_notm}} over {{site.data.keyword.cloud_notm}}'s public network" caption-side="top"}
{: #end-api-table-1}
{: tab-title="Public"}
{: tab-group="end-api"}
{: class="simple-tab-table"}
{: row-headers}

| Region                   | Private Endpoint                                       |
|--------------------------|--------------------------------------------------------|
| `Dallas (us-south)`      | `https://api.private.us-south.logging.cloud.ibm.com`   |
| `Frankfurt (eu-de)`      | `https://api.private.eu-de.logging.cloud.ibm.com`      |
| `London (eu-gb)`         | `https://api.private.eu-gb.logging.cloud.ibm.com`      |
| `Tokyo (jp-tok)`         | `https://api.private.jp-tok.logging.cloud.ibm.com`     |
{: caption="Table 2. Lists of private API endpoints for interacting with {{site.data.keyword.la_full_notm}} over {{site.data.keyword.cloud_notm}}'s private network" caption-side="top"}
{: #end-api-table-2}
{: tab-title="Private"}
{: tab-group="end-api"}
{: class="simple-tab-table"}
{: row-headers}




## Ingestion endpoints
{: #endpoints_ingestion}

The following table shows the ingestion endpoints:

| Region                   |   Public Endpoint                                   |
|--------------------------|-----------------------------------------------------|
| `Dallas (us-south)`      | `https://logs.us-south.logging.cloud.ibm.com`       |
| `Frankfurt (eu-de)`      | `https://logs.eu-de.logging.cloud.ibm.com`          |
| `London (eu-gb)`         | `https://logs.eu-gb.logging.cloud.ibm.com`          |
| `Tokyo (jp-tok)`         | `https://logs.jp-tok.logging.cloud.ibm.com`         |
{: caption="Table 3. Lists of public ingestion endpoints for interacting with {{site.data.keyword.la_full_notm}} over {{site.data.keyword.cloud_notm}}'s public network" caption-side="top"}
{: #end-ing-table-3}
{: tab-title="Public"}
{: tab-group="end-ing"}
{: class="simple-tab-table"}
{: row-headers}

| Region                   | Private Endpoint                                       |
|--------------------------|--------------------------------------------------------|
| `Dallas (us-south)`      | `https://logs.private.us-south.logging.cloud.ibm.com`  |
| `Frankfurt (eu-de)`      | `https://logs.private.eu-de.logging.cloud.ibm.com`     |
| `London (eu-gb)`         | `https://logs.private.eu-gb.logging.cloud.ibm.com`     |
| `Tokyo (jp-tok)`         | `https://logs.private.jp-tok.logging.cloud.ibm.com`    |
{: caption="Table 4. Lists of private ingestion endpoints for interacting with {{site.data.keyword.la_full_notm}} over {{site.data.keyword.cloud_notm}}'s private network" caption-side="top"}
{: #end-ing-table-4}
{: tab-title="Private"}
{: tab-group="end-ing"}
{: class="simple-tab-table"}
{: row-headers}




