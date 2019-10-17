---

copyright:
  years: 2019
lastupdated: "2019-10-17"

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

You can monitor logs from CF apps and enabled services through [the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-config_svc_logs) in the location where the app or service is running. 

Notice that there is only 1 instance per location with the flag **Platform services logs**.
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

| Service     | Description |  More info about the integration with {{site.data.keyword.la_full_notm}} |
|-------------|-------------|--------------------------------------------------------------------------------------------|
| [{{site.data.keyword.cloudant_short_notm}}](/docs/services/Cloudant?topic=cloudant-getting-started)    | {{site.data.keyword.cloudant_short_notm}} is a document-oriented database as a service (DBaaS). It stores data as documents in JSON format. | [More info](/docs/services/Cloudant?topic=cloudant-logging) |
| [{{site.data.keyword.databases-for-elasticsearch_full_notm}}](/docs/services/databases-for-elasticsearch?topic=databases-for-elasticsearch-about#about-databases-for-elasticsearch) | {{site.data.keyword.databases-for-elasticsearch_full_notm}} is a managed Elasticsearch service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/services/databases-for-elasticsearch?topic=cloud-databases-logging) |
| [{{site.data.keyword.databases-for-etcd_full_notm}}](/docs/services/databases-for-etcd?topic=databases-for-etcd-about#about-databases-for-etcd) | {{site.data.keyword.databases-for-etcd_full_notm}} is a managed etcd service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/services/databases-for-etcd?topic=cloud-databases-monitoring) |
| [{{site.data.keyword.databases-for-mongodb}}](/docs/services/databases-for-mongodb?topic=databases-for-mongodb-getting-started) | {{site.data.keyword.databases-for-mongodb}} is a managed MongoDB service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/services/databases-for-mongodb?topic=cloud-databases-logging) |
| [{{site.data.keyword.databases-for-postgresql_full_notm}}](/docs/services/databases-for-postgresql?topic=databases-for-postgresql-about#about) | {{site.data.keyword.databases-for-postgresql_full_notm}} is a managed PostgreSQL service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/services/databases-for-postgresql?topic=cloud-databases-logging) |
| [{{site.data.keyword.messages-for-rabbitmq_full_notm}}](/docs/services/messages-for-rabbitmq?topic=messages-for-rabbitmq-about#about-messages-for-rabbitmq)  | {{site.data.keyword.messages-for-rabbitmq_full_notm}} is a managed RabbitMQ service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services.| [More info](/docs/services/messages-for-rabbitmq?topic=cloud-databases-logging)|
| [{{site.data.keyword.databases-for-redis_full_notm}}](/docs/services/databases-for-redis?topic=databases-for-redis-about#about-databases-for-redis) | {{site.data.keyword.databases-for-redis_full_notm}} is a managed service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services.  | [More info](/docs/services/databases-for-redis?topic=cloud-databases-logging)|
| [{{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_mongodb_full}}](/docs/services/hyper-protect-dbaas-for-mongodb?topic=hyper-protect-dbaas-for-mongodb-gettingstarted) | {{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_mongodb_full}} is a managed highly secure MongoDB service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/services/hyper-protect-dbaas-for-mongodb?topic=hyper-protect-dbaas-for-mongodb-activity-tracker-events) |
| [{{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_postgresql_full}}](/docs/services/hyper-protect-dbaas-for-postgresql?topic=hyper-protect-dbaas-for-postgresql-gettingstarted) | {{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_postgresql_full}}} is a managed highly secure PostgreSQL service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/services/hyper-protect-dbaas-for-postgresql?topic=hyper-protect-dbaas-for-postgresql-activity-tracker-events) |
{: caption="List of database services" caption-side="top"} 

You can monitor logs through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the service is running. 
{: note}

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Platform: Database services](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services_locations#cs_locations_database).



## Platform: Integration services
{: #integration}

The following table lists database services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info about the integration with {{site.data.keyword.la_full_notm}} |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.appconservicefull_notm}}](/docs/services/AppConnect?topic=AppConnect-getting-started) | You can use {{site.data.keyword.appconservicefull_notm}} to connect your applications.   |  |
{: caption="List of integration Cloud services" caption-side="top"} 


## Platform: Security services
{: #security}

The following table lists security Cloud services that send logs to {{site.data.keyword.la_full_notm}}:


| Service     | Description | More info about the integration with {{site.data.keyword.la_full_notm}} |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.cloudcerts_full_notm}}](/docs/services/certificate-manager?topic=certificate-manager-about-certificate-manager#about-certificate-manager) | You can use {{site.data.keyword.cloudcerts_short}} to manage the SSL certificates for your {{site.data.keyword.cloud_notm}}-based apps and services.  | [More info](/docs/services/certificate-manager?topic=certificate-manager-log_events) |
{: caption="List of security Cloud services" caption-side="top"} 

You can monitor logs through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the service is running. 
{: note}

To see the list of {{site.data.keyword.la_full_notm}} locations where this service sends logs, see [Platform: Security services](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services_locations#cs_locations_security).


