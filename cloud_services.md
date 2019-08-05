---

copyright:
  years: 2019
lastupdated: "2019-08-05"

keywords: LogDNA, IBM, Log Analysis, logging, services

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


# Cloud services
{: #cloud_services}

List of {{site.data.keyword.cloud_notm}} services that send logs to {{site.data.keyword.la_full_notm}}:
{:shortdesc}

You can monitor logs from CF apps and enabled services through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the app or service is running. Notice that there is only 1 instance per location with the flag **Platform services logs**.
{: important}

## Compute: Cloud Foundry
{: #platform_cfapps}

[Cloud Foundry (CF)](/docs/cloud-foundry-public?topic=cloud-foundry-public-about-cf) logs are automatically collected and sent to {{site.data.keyword.la_full_notm}}. 

You can monitor logs from CF apps through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the app is running. 
{: note}

To see the list of {{site.data.keyword.la_full_notm}} locations where this service sends logs, see [Compute: Cloud Foundry](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services_locations#cs_locations_platform_cfapps).


## Platform: Database services
{: #database}

The following table lists database services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | 
|-------------|-------------|
| [{{site.data.keyword.databases-for-elasticsearch_full_notm}}](/docs/services/databases-for-elasticsearch?topic=databases-for-elasticsearch-about#about-databases-for-elasticsearch) | {{site.data.keyword.databases-for-elasticsearch_full_notm}} is a managed Elasticsearch service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. |
| [{{site.data.keyword.databases-for-etcd_full_notm}}](/docs/services/databases-for-etcd?topic=databases-for-etcd-about#about-databases-for-etcd) | {{site.data.keyword.databases-for-etcd_full_notm}} is a managed etcd service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. |
| [{{site.data.keyword.databases-for-mongodb}}](/docs/services/databases-for-mongodb?topic=databases-for-mongodb-getting-started) | {{site.data.keyword.databases-for-mongodb}} is a managed MongoDB service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. |  
| [{{site.data.keyword.databases-for-postgresql_full_notm}}](/docs/services/databases-for-postgresql?topic=databases-for-postgresql-about#about) | {{site.data.keyword.databases-for-postgresql_full_notm}} is a managed PostgreSQL service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. |
| [{{site.data.keyword.messages-for-rabbitmq_full_notm}}](/docs/services/messages-for-rabbitmq?topic=messages-for-rabbitmq-about#about-messages-for-rabbitmq)  | {{site.data.keyword.messages-for-rabbitmq_full_notm}} is a managed RabbitMQ service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services.|
| [{{site.data.keyword.databases-for-redis_full_notm}}](/docs/services/databases-for-redis?topic=databases-for-redis-about#about-databases-for-redis) | {{site.data.keyword.databases-for-redis_full_notm}} is a managed service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services.  |
{: caption="List of database services" caption-side="top"} 

You can monitor logs through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the service is running. 
{: note}

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Platform: Database services](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services_locations#cs_locations_database).



## Platform: Security services
{: #security}

The following table lists security Cloud services that send logs to {{site.data.keyword.la_full_notm}}:


| Service     | Description | 
|-------------|-------------|
| [{{site.data.keyword.cloudcerts_full_notm}}](/docs/services/certificate-manager?topic=certificate-manager-about-certificate-manager#about-certificate-manager) | You can use {{site.data.keyword.cloudcerts_short}} to manage the SSL certificates for your {{site.data.keyword.cloud_notm}}-based apps and services.  | 
{: caption="List of security Cloud services" caption-side="top"} 

You can monitor logs through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the service is running. 
{: note}

To see the list of {{site.data.keyword.la_full_notm}} locations where this service sends logs, see [Platform: Security services](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services_locations#cs_locations_security).


