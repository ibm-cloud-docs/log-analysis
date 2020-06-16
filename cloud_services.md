---

copyright:
  years:  2018, 2020
lastupdated: "2020-03-27"

keywords: LogDNA, IBM, Log Analysis, logging, services

subcollection: Log-Analysis-with-LogDNA


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

You can monitor logs from CF apps and enabled services through [the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-config_svc_logs) in the location where the app or service is running. 

Notice that there is only 1 instance per location with the flag **Platform services logs**.
{: important}

## Analytics services
{: #analytics}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description |  More info about the integration with {{site.data.keyword.la_full_notm}} 
|-------------|-------------|--------------------------------------------------------------------------------------------|
| [{{site.data.keyword.iae_full_notm}}](/docs/AnalyticsEngine?topic=AnalyticsEngine-getting-started) | {{site.data.keyword.iae_full_notm}} provides a flexible framework to develop and deploy analytics applications in Apache Hadoop and Apache Spark. | [More info](/docs/AnalyticsEngine?topic=AnalyticsEngine-log-aggregation#reconfiguring-log-aggregation) | 
{: caption="Table 1. List of Blockchain services" caption-side="top"} 

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Container services](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-cloud_services_locations#cs_locations_analystics).

## Blockchain services
{: #blockchain}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description |  More info about the integration with {{site.data.keyword.la_full_notm}} 
|-------------|-------------|--------------------------------------------------------------------------------------------|
| [{{site.data.keyword.blockchainfull_notm}}](/docs/blockchain?topic=blockchain-get-started-ibp) | {{site.data.keyword.blockchainfull}} Platform provides a managed and full stack blockchain-as-a-service (BaaS) offering that allows you to deploy blockchain components in environments of your choice. | [More info](/docs/blockchain?topic=blockchain-ibp-LogDNA) | 
{: caption="Table 2. List of Blockchain services" caption-side="top"} 

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Container services](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-cloud_services_locations#cs_locations_blockchain).

## Cloud Foundry
{: #platform_cfapps}

[Cloud Foundry (CF)](/docs/cloud-foundry-public?topic=cloud-foundry-public-about-cf) logs are automatically collected and sent to {{site.data.keyword.la_full_notm}}. 

You can monitor logs from CF apps through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the app is running. 
{: note}

To see the list of {{site.data.keyword.la_full_notm}} locations where this service sends logs, see [Cloud Foundry](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-cloud_services_locations#cs_locations_platform_cfapps).

## Container services
{: #platform_container}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info about the integration with {{site.data.keyword.la_full_notm}} |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.registrylong_notm}}](/docs/Registry?topic=Registry-getting-started) | You can use {{site.data.keyword.registrylong_notm}} to provide a multi-tenant private image registry that you can use to store and share your container images with users in your {{site.data.keyword.cloud_notm}} account. | [More info](/docs/Registry?topic=Registry-registry_logs) |
| [{{site.data.keyword.containerlong}}](/docs/containers?topic=containers-getting-started) | You can use the {{site.data.keyword.containerlong_notm}} service to deploy highly available apps in Docker containers that run in Kubernetes clusters. | [More info](/docs/containers?topic=containers-health#logdna) | 
| [{{site.data.keyword.openshiftlong}}](/docs/openshift?topic=openshift-getting-started) | With {{site.data.keyword.openshiftlong}}, you can deploy apps on highly available clusters that come installed with the Red Hat OpenShift on IBM Cloud Container PlatformExternal link icon software installed on Red Hat Enterprise Linux. | [More info](/docs/openshift?topic=openshift-health) |
{: caption="Table 3. List of container services" caption-side="top"} 

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Container services](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-cloud_services_locations#cs_locations_container).

## Database services
{: #database}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description |  More info about the integration with {{site.data.keyword.la_full_notm}} | 
|-------------|-------------|--------------------------------------------------------------------------------------------|--------------|-----------------|
| [{{site.data.keyword.cloudant_short_notm}}](/docs/Cloudant?topic=cloudant-getting-started)    | {{site.data.keyword.cloudant_short_notm}} is a document-oriented database as a service (DBaaS). It stores data as documents in JSON format. | [More info](/docs/Cloudant?topic=cloudant-log-analysis-integration) | 
| [{{site.data.keyword.databases-for-elasticsearch_full_notm}}](/docs/databases-for-elasticsearch?topic=databases-for-elasticsearch-getting-started) | {{site.data.keyword.databases-for-elasticsearch_full_notm}} is a managed Elasticsearch service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/databases-for-elasticsearch?topic=cloud-databases-logging) |
| [{{site.data.keyword.databases-for-etcd_full_notm}}](/docs/databases-for-etcd?topic=databases-for-etcd-getting-started) | {{site.data.keyword.databases-for-etcd_full_notm}} is a managed etcd service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/databases-for-etcd?topic=cloud-databases-monitoring) |
| [{{site.data.keyword.databases-for-mongodb}}](/docs/databases-for-mongodb?topic=databases-for-mongodb-getting-started) | {{site.data.keyword.databases-for-mongodb}} is a managed MongoDB service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/databases-for-mongodb?topic=cloud-databases-logging) |
| [{{site.data.keyword.databases-for-postgresql_full_notm}}](/docs/databases-for-postgresql?topic=databases-for-postgresql-getting-started) | {{site.data.keyword.databases-for-postgresql_full_notm}} is a managed PostgreSQL service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/databases-for-postgresql?topic=cloud-databases-logging) |
| [{{site.data.keyword.messages-for-rabbitmq_full_notm}}](/docs/messages-for-rabbitmq?topic=messages-for-rabbitmq-getting-started)  | {{site.data.keyword.messages-for-rabbitmq_full_notm}} is a managed RabbitMQ service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services.| [More info](/docs/messages-for-rabbitmq?topic=cloud-databases-logging)|
| [{{site.data.keyword.databases-for-redis_full_notm}}](/docs/databases-for-redis?topic=databases-for-redis-getting-started) | {{site.data.keyword.databases-for-redis_full_notm}} is a managed service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services.  | [More info](/docs/databases-for-redis?topic=cloud-databases-logging)| 
| [{{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_mongodb_full}}](/docs/hyper-protect-dbaas-for-mongodb?topic=hyper-protect-dbaas-for-mongodb-gettingstarted) | {{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_mongodb_full}} is a managed highly secure MongoDB service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/hyper-protect-dbaas-for-mongodb?topic=hyper-protect-dbaas-for-mongodb-sendlogs) | 
| [{{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_postgresql_full}}](/docs/hyper-protect-dbaas-for-postgresql?topic=hyper-protect-dbaas-for-postgresql-gettingstarted) | {{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_postgresql_full}} is a managed highly secure PostgreSQL service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/hyper-protect-dbaas-for-postgresql?topic=hyper-protect-dbaas-for-postgresql-sendlogs) |
{: caption="Table 4. List of database services" caption-side="top"} 

You can monitor logs through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the service is running. 
{: note}

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Database services](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-cloud_services_locations#cs_locations_database).



## Integration services
{: #integration}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info about the integration with {{site.data.keyword.la_full_notm}} |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.appconservicefull}}](/docs/AppConnect?topic=AppConnect-getting-started) | You can use {{site.data.keyword.appconservicefull}} to connect your applications.   | [More info ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://developer.ibm.com/integration/docs/app-connect/troubleshooting/monitoring-and-managing-app-connect-logs-in-logdna/){:new_window}  |
{: caption="Table 5. List of integration Cloud services" caption-side="top"} 

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Integration services](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-cloud_services_locations#cs_locations_integration).


## Security services
{: #security}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:


| Service     | Description | More info about the integration with {{site.data.keyword.la_full_notm}} |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.cloudcerts_full_notm}}](/docs/certificate-manager?topic=certificate-manager-about-certificate-manager#about-certificate-manager) | You can use {{site.data.keyword.cloudcerts_short}} to manage the SSL certificates for your {{site.data.keyword.cloud_notm}}-based apps and services.  | [More info](/docs/certificate-manager?topic=certificate-manager-log_events) |
{: caption="Table 6. List of security Cloud services" caption-side="top"} 

You can monitor logs through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the service is running. 
{: note}

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Security services](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-cloud_services_locations#cs_locations_security).


## Networking services
{: #networking}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:


| Service     | Description | More info about the integration with {{site.data.keyword.la_full_notm}} |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.loadbalancer_full}}](/docs/loadbalancer-service?topic=loadbalancer-service-getting-started) | Use this service to improve availability of business-critical applications by distributing traffic among multiple application server instances, and by forwarding traffic to healthy instances only. | [More info](/docs/loadbalancer-service?topic=loadbalancer-service-data-logging) |
{: caption="Table 7. List of security networking services" caption-side="top"} 


## VPC infrastructure
{: #vpc_infrastructure}

You can provision a Virtual Private Cloud (VPC) in the {{site.data.keyword.cloud_notm}} to run an isolated environment within the public cloud. VPC gives you the security of a private cloud, with the agility and ease of a public cloud. For more information, see [About Virtual Private Cloud](/docs/vpc-on-classic?topic=vpc-on-classic-about).

There are 2 types of VPC infrastructure that you can provision in your account:
* [Virtual Private Cloud classic Gen 1](/docs/vpc-on-classic?topic=vpc-on-classic-getting-started)
* [{{site.data.keyword.vpc_full}} Gen 2](/docs/vpc?topic=vpc-getting-started)

The following tables lists VPC infrastructure services that send metrics to {{site.data.keyword.at_full_notm}}:

## VPC infrastructure Gen 1 (classic)
{: #vpc_infrastructure_gen1}


| Service     | Description |Events             |
|-------------|-------------|-------------------|
| `VPN`| Use this service to connect private networks in a secure fashion. You can use VPN to set up an IPsec site-to-site tunnel between your VPC and your on-premise private network or another VPC. | [More info](/docs/vpc?topic=vpc-using-logdna-to-view-vpn-logs) |
{: caption="Table 8. List of VPC infrastructure services (generation 2)" caption-side="top"} 

## VPC infrastructure Gen 2
{: #vpc_infrastructure_gen2}

| Service     | Description |Events             |
|-------------|-------------|-------------------|
| [VPN](/docs/vpc-on-classic-network?topic=vpc-on-classic-network---using-vpn-with-your-vpc)| Use this service to connect private networks in a secure fashion. You can use VPN to set up an IPsec site-to-site tunnel between your VPC and your on-premise private network or another VPC. | [More info](/docs/vpc-on-classic-network?topic=vpc-on-classic-network-using-logdna-to-view-vpn-logs) |
{: caption="Table 9. List of VPC infrastructure services (generation 1)" caption-side="top"} 




## Watson AI services
{: #watson_ai}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info about the integration with {{site.data.keyword.la_full_notm}} |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.iva_full_notm}} ](/docs/voice-agent?topic=voice-agent-getting-started) | You can {{site.data.keyword.iva_full_notm}} to integrate a set of orchestrated Watson services with the telephone network by using the Session Initiation Protocol (SIP).   | [More info](/docs/voice-agent?topic=voice-agent-log-analysis-integration) |
{: caption="Table 10. List of Watson AI Cloud services" caption-side="top"} 

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Watson AI services](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-cloud_services_locations#cloud_services_locations_watson_ai).

