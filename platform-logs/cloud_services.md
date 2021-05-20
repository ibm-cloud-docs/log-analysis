---

copyright:
  years:  2018, 2021
lastupdated: "2021-05-18"

keywords: IBM, Log Analysis, logging, services

subcollection: log-analysis


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
{:external: target="_blank" .external}


# Cloud services
{: #cloud_services}

List of {{site.data.keyword.cloud}} services that send logs to {{site.data.keyword.la_full_notm}}:
{:shortdesc}

You can monitor logs from CF apps and enabled services through [the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs](/docs/log-analysis?topic=log-analysis-config_svc_logs) in the location where the app or service is running. 

Notice that there is only 1 instance per location with the flag **Platform logs**.
{: important}


## Cloud Foundry
{: #platform_cfapps}

[Cloud Foundry (CF)](/docs/cloud-foundry-public?topic=cloud-foundry-public-getting-started) logs are automatically collected and sent to {{site.data.keyword.la_full_notm}}. 

You can monitor logs from CF apps through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the app is running. 
{: note}

To see the list of {{site.data.keyword.la_full_notm}} locations where this service sends logs, see [Cloud Foundry](/docs/log-analysis?topic=log-analysis-cloud_services_locations#cs_locations_platform_cfapps).



## Compute serverless services
{: #serverless}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info |
|-------------|-------------|-------------------|
| [{{site.data.keyword.openwhisk}}](/docs/openwhisk?topic=openwhisk-getting-started) | {{site.data.keyword.openwhisk_short}} is a polyglot Functions-as-a-Service (FaaS) programming platform based on Apache OpenWhisk that you can use to write lightweight `code called actions`. | [More info](/docs/openwhisk?topic=openwhisk-logs) |
| [{{site.data.keyword.codeenginefull}}](/docs/codeengine?topic=codeengine-getting-started)| Code Engine is a fully managed, serverless platform that runs your containerized workloads, including web apps, micro-services, event-driven functions, or batch jobs  | [More info](/docs/codeengine?topic=codeengine-view-logs). |
{: caption="Table 1. List of serverless compute services" caption-side="top"} 


## Container services
{: #platform_container}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.registrylong_notm}}](/docs/Registry?topic=Registry-getting-started) | You can use {{site.data.keyword.registrylong_notm}} to provide a multi-tenant private image registry that you can use to store and share your container images with users in your {{site.data.keyword.cloud_notm}} account. | [More info](/docs/Registry?topic=Registry-registry_logs) |
| [{{site.data.keyword.containerlong}}](/docs/containers?topic=containers-getting-started) | You can use the {{site.data.keyword.containerlong_notm}} service to deploy highly available apps in Docker containers that run in Kubernetes clusters. | [More info](/docs/containers?topic=containers-health#logdna) | 
| [{{site.data.keyword.openshiftlong}}](/docs/openshift?topic=openshift-getting-started) | With {{site.data.keyword.openshiftlong_notm}}, you can deploy apps on highly available clusters that come installed with the Red Hat OpenShift on IBM Cloud Container Platform software installed on Red Hat Enterprise Linux. | [More info](/docs/openshift?topic=openshift-health) |
| [{{site.data.keyword.satellitelong}}](/docs/satellite?topic=satellite-getting-started) | With {{site.data.keyword.satellitelong_notm}}, you can bring your own compute infrastructure to run {{site.data.keyword.cloud_notm}} services and consistently deploy, manage, and control your app workloads. | [More info](/docs/satellite?topic=satellite-health) |
{: caption="Table 2. List of container services" caption-side="top"} 

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Container services](/docs/log-analysis?topic=log-analysis-cloud_services_locations#cs_locations_container).

## Database services
{: #database}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description |  More info | 
|-------------|-------------|--------------------------------------------------------------------------------------------|--------------|-----------------|
| [{{site.data.keyword.cloudant_short_notm}}](/docs/Cloudant?topic=Cloudant-getting-started-with-cloudant)    | {{site.data.keyword.cloudant_short_notm}} is a document-oriented database as a service (DBaaS). It stores data as documents in JSON format. | [More info](/docs/Cloudant?topic=Cloudant-log-analysis-integration) | 
| [{{site.data.keyword.databases-for-elasticsearch_full_notm}}](/docs/databases-for-elasticsearch?topic=databases-for-elasticsearch-getting-started) | {{site.data.keyword.databases-for-elasticsearch_full_notm}} is a managed Elasticsearch service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/databases-for-elasticsearch?topic=cloud-databases-logging) |
| [{{site.data.keyword.databases-for-enterprisedb_full}}](/docs/databases-for-enterprisedb?topic=databases-for-enterprisedb-getting-started) | {{site.data.keyword.databases-for-enterprisedb}} is a database engine that optimizes the built-in features of PostgreSQL. | [More info](/docs/databases-for-enterprisedb?topic=cloud-databases-logging) | 
| [{{site.data.keyword.databases-for-cassandra_full}}](/docs/databases-for-cassandra?topic=databases-for-cassandra-getting-started) | {{site.data.keyword.databases-for-cassandra_full}} is a scale-out NoSQL database that is built on Apache Cassandra. It’s designed to power real-time applications with high availability and massive scalability. | [More info](/docs/databases-for-cassandra?topic=cloud-databases-logging) | 
| [{{site.data.keyword.databases-for-etcd_full_notm}}](/docs/databases-for-etcd?topic=databases-for-etcd-getting-started) | {{site.data.keyword.databases-for-etcd_full_notm}} is a managed etcd service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/databases-for-etcd?topic=cloud-databases-logging) |
| [{{site.data.keyword.databases-for-mongodb}}](/docs/databases-for-mongodb?topic=databases-for-mongodb-getting-started) | {{site.data.keyword.databases-for-mongodb}} is a managed MongoDB service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/databases-for-mongodb?topic=cloud-databases-logging) |
| [{{site.data.keyword.databases-for-postgresql_full_notm}}](/docs/databases-for-postgresql?topic=databases-for-postgresql-getting-started) | {{site.data.keyword.databases-for-postgresql_full_notm}} is a managed PostgreSQL service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/databases-for-postgresql?topic=cloud-databases-logging) |
| [{{site.data.keyword.messages-for-rabbitmq_full_notm}}](/docs/messages-for-rabbitmq?topic=messages-for-rabbitmq-getting-started)  | {{site.data.keyword.messages-for-rabbitmq_full_notm}} is a managed RabbitMQ service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services.| [More info](/docs/messages-for-rabbitmq?topic=cloud-databases-logging)|
| [{{site.data.keyword.databases-for-redis_full_notm}}](/docs/databases-for-redis?topic=databases-for-redis-getting-started) | {{site.data.keyword.databases-for-redis_full_notm}} is a managed service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services.  | [More info](/docs/databases-for-redis?topic=cloud-databases-logging)| 
| [{{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_mongodb_full}}](/docs/hyper-protect-dbaas-for-mongodb?topic=hyper-protect-dbaas-for-mongodb-gettingstarted) | {{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_mongodb_full}} is a managed highly secure MongoDB service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/hyper-protect-dbaas-for-mongodb?topic=hyper-protect-dbaas-for-mongodb-sendlogs) | 
| [{{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_postgresql_full}}](/docs/hyper-protect-dbaas-for-postgresql?topic=hyper-protect-dbaas-for-postgresql-gettingstarted) | {{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_postgresql_full}} is a managed highly secure PostgreSQL service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/hyper-protect-dbaas-for-postgresql?topic=hyper-protect-dbaas-for-postgresql-sendlogs) |
{: caption="Table 3. List of database services" caption-side="top"} 

You can monitor logs through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the service is running. 
{: note}

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Database services](/docs/log-analysis?topic=log-analysis-cloud_services_locations#cs_locations_database).



## Integration services
{: #integration}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.appconservicefull}}](/docs/AppConnect?topic=AppConnect-getting-started) | You can use {{site.data.keyword.appconservicefull}} to connect your applications.   | [More info](https://developer.ibm.com/integration/docs/app-connect/troubleshooting/monitoring-and-managing-app-connect-logs-in-logdna/){: external}  |
| [{{site.data.keyword.mq_short}}](/docs/mqcloud?topic=mqcloud-mqoc_getting_started) | MQ on IBM Cloud enables you to quickly and easily deploy queue managers in the cloud and connect your applications to them, for reliable data transfer between different parts of your enterprise application landscape. | [More info ](/docs/mqcloud?topic=mqcloud-logdna_logs) |
{: caption="Table 4. List of integration Cloud services" caption-side="top"} 

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Integration services](/docs/log-analysis?topic=log-analysis-cloud_services_locations#cs_locations_integration).


## Networking services
{: #networking}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:


| Service          | Description | More info         | Message IDs |
|------------------|-------------|-------------------|-------------|
| [Dedicated host](/docs/vpc?topic=vpc-creating-dedicated-hosts-instances) | You can create a dedicated host to carve out a single-tenant compute node, free from users outside of your organization.  | [More info](/docs/vpc?topic=vpc-logging) | [Message IDs](/docs/vpc?topic=vpc-logging#dedicated-host) |
| [Flow Log Collector](/docs/vpc?topic=vpc-flow-logs)| This service is used to collect and store information regarding the Internet Protocol (IP) traffic going to and from network interfaces within your Virtual Private Cloud (VPC) | [Viewing flow log objects](/docs/vpc?topic=vpc-fl-analyze) | [Message IDs](/docs/vpc?topic=vpc-logging#logging-flow-log-collector_msgs) |
| [VPN](/docs/vpc?topic=vpc-using-vpn) | Use this service to connect private networks in a secure fashion. You can use VPN to set up an IPsec site-to-site tunnel between your VPC and your on-premise private network or another VPC. | [More info](/docs/vpc?topic=vpc-using-log-analysis-to-view-vpn-logs) | |
| [{{site.data.keyword.loadbalancer_full}}](/docs/loadbalancer-service?topic=loadbalancer-service-getting-started) | Use this service to improve availability of business-critical applications by distributing traffic among multiple application server instances, and by forwarding traffic to healthy instances only. | [More info](/docs/loadbalancer-service?topic=loadbalancer-service-data-logging) | |
{: caption="Table 6. List of security networking services" caption-side="top"} 




## Security services
{: #security}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:


| Service     | Description | More info |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.cloudcerts_full_notm}}](/docs/certificate-manager?topic=certificate-manager-about-certificate-manager#about-certificate-manager) | You can use {{site.data.keyword.cloudcerts_short}} to manage the SSL certificates for your {{site.data.keyword.cloud_notm}}-based apps and services.  | [More info](/docs/certificate-manager?topic=certificate-manager-log_events) |
| [{{site.data.keyword.secrets-manager_full}}](/docs/secrets-manager?topic=secrets-manager-getting-started) | With {{site.data.keyword.secrets-manager_full_notm}}, you can create, lease, and centrally manage secrets that are used in {{site.data.keyword.cloud_notm}} services or your custom-built applications. | [More info](/docs/secrets-manager?topic=secrets-manager-service-logs) |
{: caption="Table 5. List of security Cloud services" caption-side="top"} 

You can monitor logs through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the service is running. 
{: note}

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Security services](/docs/log-analysis?topic=log-analysis-cloud_services_locations#cs_locations_security).



## Watson AI services
{: #watson_ai}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.iva_full_notm}}](/docs/voice-agent?topic=voice-agent-getting-started) | You can {{site.data.keyword.iva_full_notm}} to integrate a set of orchestrated Watson services with the telephone network by using the Session Initiation Protocol (SIP).   | [More info](/docs/voice-agent?topic=voice-agent-log-analysis-integration) |
{: caption="Table 8. List of Watson AI Cloud services" caption-side="top"} 

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Watson AI services](/docs/log-analysis?topic=log-analysis-cloud_services_locations#cloud_services_locations_watson_ai).

