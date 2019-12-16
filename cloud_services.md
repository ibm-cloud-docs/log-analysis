---

copyright:
  years: 2019
lastupdated: "2019-12-16"

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

List of {{site.data.keyword.cloud}} services that send logs to {{site.data.keyword.la_full_notm}}:
{:shortdesc}

You can monitor logs from CF apps and enabled services through [the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-config_svc_logs) in the location where the app or service is running. 

Notice that there is only 1 instance per location with the flag **Platform services logs**.
{: important}

## Blockchain services
{: #blockchain}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description |  More info about the integration with {{site.data.keyword.la_full_notm}} 
|-------------|-------------|--------------------------------------------------------------------------------------------|
| [{{site.data.keyword.blockchainfull}}](/docs/services/blockchain?topic=blockchain-get-started-ibp) | {{site.data.keyword.blockchainfull}} Platform provides a managed and full stack blockchain-as-a-service (BaaS) offering that allows you to deploy blockchain components in environments of your choice. | [More info](/docs/services/blockchain?topic=blockchain-ibp-LogDNA) | 
{: caption="Table 1. List of Blockchain services" caption-side="top"} 

For the {{site.data.keyword.blockchainfull}} service, you can choose the location where you want to collect and forward logs by configuring a LogDNA agent.

## Cloud Foundry
{: #platform_cfapps}

[Cloud Foundry (CF)](/docs/cloud-foundry-public?topic=cloud-foundry-public-about-cf) logs are automatically collected and sent to {{site.data.keyword.la_full_notm}}. 

You can monitor logs from CF apps through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the app is running. 
{: note}

To see the list of {{site.data.keyword.la_full_notm}} locations where this service sends logs, see [Compute: Cloud Foundry](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services_locations#cs_locations_platform_cfapps).

## Container services
{: #platform_container}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info about the integration with {{site.data.keyword.la_full_notm}} |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.registrylong_notm}}](/docs/services/Registry?topic=registry-getting-started) | You can use {{site.data.keyword.registrylong_notm}} to provide a multi-tenant private image registry that you can use to store and share your container images with users in your {{site.data.keyword.cloud_notm}} account. | [More info](/docs/services/Registry?topic=registry-registry_logs) |
| [{{site.data.keyword.containerlong}}](/docs/containers?topic=containers-getting-started) | You can use the {{site.data.keyword.containerlong_notm}} service to deploy highly available apps in Docker containers that run in Kubernetes clusters. | [More info](/docs/containers?topic=containers-health#logdna) | 
| [{{site.data.keyword.openshiftlong}}](/docs/openshift?topic=openshift-getting-started) | With {{site.data.keyword.openshiftlong}}, you can deploy apps on highly available clusters that come installed with the Red Hat OpenShift on IBM Cloud Container PlatformExternal link icon software installed on Red Hat Enterprise Linux. | [More info](/docs/openshift?topic=openshift-health) |
{: caption="Table 2. List of container services" caption-side="top"} 

## Database services
{: #database}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description |  More info about the integration with {{site.data.keyword.la_full_notm}} | 
|-------------|-------------|--------------------------------------------------------------------------------------------|--------------|-----------------|
| [{{site.data.keyword.cloudant_short_notm}}](/docs/services/Cloudant?topic=cloudant-getting-started)    | {{site.data.keyword.cloudant_short_notm}} is a document-oriented database as a service (DBaaS). It stores data as documents in JSON format. | [More info](/docs/services/Cloudant?topic=cloudant-log-analysis-integration) | 
| [{{site.data.keyword.databases-for-elasticsearch_full_notm}}](/docs/services/databases-for-elasticsearch?topic=databases-for-elasticsearch-getting-started) | {{site.data.keyword.databases-for-elasticsearch_full_notm}} is a managed Elasticsearch service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/services/databases-for-elasticsearch?topic=cloud-databases-logging) |
| [{{site.data.keyword.databases-for-etcd_full_notm}}](/docs/services/databases-for-etcd?topic=databases-for-etcd-getting-started) | {{site.data.keyword.databases-for-etcd_full_notm}} is a managed etcd service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/services/databases-for-etcd?topic=cloud-databases-monitoring) |
| [{{site.data.keyword.databases-for-mongodb}}](/docs/services/databases-for-mongodb?topic=databases-for-mongodb-getting-started) | {{site.data.keyword.databases-for-mongodb}} is a managed MongoDB service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/services/databases-for-mongodb?topic=cloud-databases-logging) |
| [{{site.data.keyword.databases-for-postgresql_full_notm}}](/docs/services/databases-for-postgresql?topic=databases-for-postgresql-getting-started) | {{site.data.keyword.databases-for-postgresql_full_notm}} is a managed PostgreSQL service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/services/databases-for-postgresql?topic=cloud-databases-logging) |
| [{{site.data.keyword.messages-for-rabbitmq_full_notm}}](/docs/services/messages-for-rabbitmq?topic=messages-for-rabbitmq-getting-started)  | {{site.data.keyword.messages-for-rabbitmq_full_notm}} is a managed RabbitMQ service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services.| [More info](/docs/services/messages-for-rabbitmq?topic=cloud-databases-logging)|
| [{{site.data.keyword.databases-for-redis_full_notm}}](/docs/services/databases-for-redis?topic=databases-for-redis-getting-started) | {{site.data.keyword.databases-for-redis_full_notm}} is a managed service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services.  | [More info](/docs/services/databases-for-redis?topic=cloud-databases-logging)| 
| [{{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_mongodb_full}}](/docs/services/hyper-protect-dbaas-for-mongodb?topic=hyper-protect-dbaas-for-mongodb-gettingstarted) | {{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_mongodb_full}} is a managed highly secure MongoDB service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/services/hyper-protect-dbaas-for-mongodb?topic=hyper-protect-dbaas-for-mongodb-sendlogs) | 
| [{{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_postgresql_full}}](/docs/services/hyper-protect-dbaas-for-postgresql?topic=hyper-protect-dbaas-for-postgresql-gettingstarted) | {{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_postgresql_full}} is a managed highly secure PostgreSQL service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/services/hyper-protect-dbaas-for-postgresql?topic=hyper-protect-dbaas-for-postgresql-sendlogs) |
{: caption="Table 3. List of database services" caption-side="top"} 

You can monitor logs through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the service is running. 
{: note}

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Platform: Database services](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services_locations#cs_locations_database).



## Integration services
{: #integration}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info about the integration with {{site.data.keyword.la_full_notm}} |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.appconservicefull}}](/docs/services/AppConnect?topic=AppConnect-getting-started) | You can use {{site.data.keyword.appconservicefull}} to connect your applications.   | More info [ ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://developer.ibm.com/integration/docs/app-connect/troubleshooting/monitoring-and-managing-app-connect-logs-in-logdna/){:new_window}  |
{: caption="Table 4. List of integration Cloud services" caption-side="top"} 


## Security services
{: #security}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:


| Service     | Description | More info about the integration with {{site.data.keyword.la_full_notm}} |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.cloudcerts_full_notm}}](/docs/services/certificate-manager?topic=certificate-manager-about-certificate-manager#about-certificate-manager) | You can use {{site.data.keyword.cloudcerts_short}} to manage the SSL certificates for your {{site.data.keyword.cloud_notm}}-based apps and services.  | [More info](/docs/services/certificate-manager?topic=certificate-manager-log_events) |
{: caption="Table 5. List of security Cloud services" caption-side="top"} 

You can monitor logs through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the service is running. 
{: note}

To see the list of {{site.data.keyword.la_full_notm}} locations where this service sends logs, see [Platform: Security services](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services_locations#cs_locations_security).



## Watson AI services
{: #watson_ai}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info about the integration with {{site.data.keyword.la_full_notm}} |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.iva_full}} ](/docs/services/voice-agent?topic=voice-agent-getting-started) |   | [More info](/docs/services/voice-agent?topic=voice-agent-log-analysis-integration) |
{: caption="Table 6. List of Watson AI Cloud services" caption-side="top"} 



