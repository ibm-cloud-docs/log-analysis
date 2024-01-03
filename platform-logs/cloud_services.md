---

copyright:
  years:  2018, 2024
lastupdated: "2024-01-03"

keywords:

subcollection: log-analysis


---

{{site.data.keyword.attribute-definition-list}}


# {{site.data.keyword.cloud_notm}} services that generate platform logs
{: #cloud_services}

List of {{site.data.keyword.cloud}} services that send logs to {{site.data.keyword.la_full_notm}}:
{: shortdesc}

You can define only 1 instance per region where {{site.data.keyword.la_full_notm}} is supported with the flag **Platform logs**.
{: important}

## Analytics services
{: #analytics}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info |
|-------------|-------------|-------------------|
| [{{site.data.keyword.PA_SaaS_notm}}](/docs/planning-analytics?topic=planning-analytics-about) | {{site.data.keyword.PA_SaaS_notm}} is a fully-managed and collaborative service that provides enterprise-level budgeting, planning, modeling, and reporting solutions. | [More info](/docs/planning-analytics?topic=planning-analytics-logging) |
{: caption="Table 1. List of analytics services" caption-side="top"}

You can monitor logs through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the service is running.
{: note}

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Security services](/docs/log-analysis?topic=log-analysis-cloud_services_locations#cs_locations_analytics).

## Compute serverless services
{: #serverless}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info |
|-------------|-------------|-------------------|
| [{{site.data.keyword.codeenginefull}}](/docs/codeengine?topic=codeengine-getting-started)| Code Engine is a fully managed, serverless platform that runs your containerized workloads, including web apps, micro-services, event-driven functions, or batch jobs  | [More info](/docs/codeengine?topic=codeengine-view-logs). |
{: caption="Table 2. List of serverless compute services" caption-side="top"}


## Container services
{: #platform_container}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.registrylong_notm}}](/docs/Registry?topic=Registry-getting-started) | You can use {{site.data.keyword.registrylong_notm}} to provide a multi-tenant private image registry that you can use to store and share your container images with users in your {{site.data.keyword.cloud_notm}} account. | [More info](/docs/Registry?topic=Registry-registry_logs) |
| [{{site.data.keyword.containerlong}}](/docs/containers?topic=containers-getting-started) | You can use the {{site.data.keyword.containerlong_notm}} service to deploy highly available apps in Docker containers that run in Kubernetes clusters. | [More info](/docs/containers?topic=containers-health#logdna) |
| [{{site.data.keyword.openshiftlong}}](/docs/openshift?topic=openshift-getting-started) | With {{site.data.keyword.openshiftlong_notm}}, you can deploy apps on highly available clusters that come installed with the Red Hat OpenShift on IBM Cloud Container Platform software installed on Red Hat Enterprise Linux. | [More info](/docs/openshift?topic=openshift-health) |
| [{{site.data.keyword.satellitelong}}](/docs/satellite?topic=satellite-getting-started) | With {{site.data.keyword.satellitelong_notm}}, you can bring your own compute infrastructure to run {{site.data.keyword.cloud_notm}} services and consistently deploy, manage, and control your app workloads. | [More info](/docs/satellite?topic=satellite-health) |
{: caption="Table 3. List of container services" caption-side="top"}

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Container services](/docs/log-analysis?topic=log-analysis-cloud_services_locations#cs_locations_container).

## Carbon Calculator services
{: #carbon-calculator}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info |
|-------------|-------------|-------------------------------------------------------------------------|
| [IBM Cloud Carbon Calculator](/docs/billing-usage?topic=billing-usage-what-is-cloud-calc) | The IBM Cloud Carbon Calculator displays the carbon emissions for your {{site.data.keyword.cloud_notm}} account which enables you to track and reduce your carbon footprint over time. | [More info](/docs/billing-usage?topic=billing-usage-what-is-cloud-calc) |
{: caption="Table 4. List of carbon calculator services" caption-side="top"}

## Database services
{: #database}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description |  More info |
|-------------|-------------|--------------------------------------------------------------------------------------------|
| [{{site.data.keyword.cloudant_short_notm}}](/docs/Cloudant?topic=Cloudant-getting-started-with-cloudant)    | {{site.data.keyword.cloudant_short_notm}} is a document-oriented database as a service (DBaaS). It stores data as documents in JSON format. | [More info](/docs/Cloudant?topic=Cloudant-log-analysis-integration) |
| [{{site.data.keyword.databases-for-elasticsearch_full_notm}}](/docs/databases-for-elasticsearch?topic=databases-for-elasticsearch-getting-started) | {{site.data.keyword.databases-for-elasticsearch_full_notm}} is a managed Elasticsearch service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/databases-for-elasticsearch?topic=cloud-databases-logging) |
| [{{site.data.keyword.databases-for-enterprisedb_full}}](/docs/databases-for-enterprisedb?topic=databases-for-enterprisedb-getting-started) | {{site.data.keyword.databases-for-enterprisedb}} is a database engine that optimizes the built-in features of PostgreSQL. | [More info](/docs/databases-for-enterprisedb?topic=cloud-databases-logging) |
| [{{site.data.keyword.databases-for-etcd_full_notm}}](/docs/databases-for-etcd?topic=databases-for-etcd-getting-started) | {{site.data.keyword.databases-for-etcd_full_notm}} is a managed etcd service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/databases-for-etcd?topic=cloud-databases-logging) |
| [{{site.data.keyword.databases-for-mongodb}}](/docs/databases-for-mongodb?topic=databases-for-mongodb-getting-started) | {{site.data.keyword.databases-for-mongodb}} is a managed MongoDB service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/databases-for-mongodb?topic=cloud-databases-logging) |
| [{{site.data.keyword.databases-for-mysql_full}}](/docs/databases-for-mysql) | `databases-for-mysql-group` | ![Checkmark](/images/checkmark-icon.svg "Checkmark")|  [Location-based events](/docs/databases-for-mysql?topic=cloud-databases-activity-tracker-integration) |
| [{{site.data.keyword.databases-for-postgresql_full_notm}}](/docs/databases-for-postgresql?topic=databases-for-postgresql-getting-started) | {{site.data.keyword.databases-for-postgresql_full_notm}} is a managed PostgreSQL service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/databases-for-postgresql?topic=cloud-databases-logging) |
| [{{site.data.keyword.messages-for-rabbitmq_full_notm}}](/docs/messages-for-rabbitmq?topic=messages-for-rabbitmq-getting-started)  | {{site.data.keyword.messages-for-rabbitmq_full_notm}} is a managed RabbitMQ service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services.| [More info](/docs/messages-for-rabbitmq?topic=cloud-databases-logging)|
| [{{site.data.keyword.databases-for-redis_full_notm}}](/docs/databases-for-redis?topic=databases-for-redis-getting-started) | {{site.data.keyword.databases-for-redis_full_notm}} is a managed service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services.  | [More info](/docs/databases-for-redis?topic=cloud-databases-logging)|
| [{{site.data.keyword.Db2_on_Cloud_long}}](/docs/Db2onCloud?topic=Db2onCloud-getting-started) | {{site.data.keyword.Db2_on_Cloud_long}} is a managed Db2 service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/Db2onCloud?topic=Db2onCloud-auditing-events-for-db2-on-cloud) |
| [{{site.data.keyword.dashdblong_notm}}](/docs/Db2whc?topic=Db2whc-about) | {{site.data.keyword.dashdblong_notm}} is a managed Db2 Warehouse service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](/docs/Db2whc?topic=Db2whc-logg_mon) |
| [{{site.data.keyword.dv_short}}](/docs/data-virtualization?topic=data-virtualization-getting-started) | {{site.data.keyword.dv_short}} is a data management service that is hosted in the {{site.data.keyword.cloud_notm}} and integrated with other {{site.data.keyword.cloud_notm}} services. | [More info](https://dataplatform.cloud.ibm.com/docs/content/wsj/admin/at-events.html?audience=wdp&context=cpdaas#dv){: external} |
{: caption="Table 5. List of database services" caption-side="top"}

You can monitor logs through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the service is running.
{: note}

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Database services](/docs/log-analysis?topic=log-analysis-cloud_services_locations#cs_locations_database).


## Developer tools
{: #developer_tools}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info |
|-------------|-------------|-----------|
| [{{site.data.keyword.en_full}}](/docs/event-notifications?topic=event-notifications-getting-started) | {{site.data.keyword.en_short}} is a routing service that tells you about critical events that occur in your {{site.data.keyword.cloud}} account. You can filter and route event notifications from {{site.data.keyword.cloud_notm}} services like Monitoring, Security and Compliance Center, and Secrets Manager to communication channels like email, SMS, push notifications, webhook, slack, and Microsoft&trade; Teams.  | [More info](/docs/event-notifications?topic=event-notifications-logging)  |
{: caption="Table 6. List of Developer tools services" caption-side="top"}

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Developer tools](/docs/log-analysis?topic=log-analysis-cloud_services_locations#cs_locations_developer_tools).


## Integration services
{: #integration}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.mq_short}}](/docs/mqcloud?topic=mqcloud-mqoc_getting_started) | MQ on IBM Cloud enables you to quickly and easily deploy queue managers in the cloud and connect your applications to them, for reliable data transfer between different parts of your enterprise application landscape. | [More info](/docs/mqcloud?topic=mqcloud-logdna_logs) |
{: caption="Table 7. List of integration Cloud services" caption-side="top"}

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Integration services](/docs/log-analysis?topic=log-analysis-cloud_services_locations#cs_locations_integration).


## VPC services
{: #vpc}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:


| Service          | Description | More info         | Message IDs |
|------------------|-------------|-------------------|-------------|
| [Dedicated host](/docs/vpc?topic=vpc-creating-dedicated-hosts-instances) | You can create a dedicated host to carve out a single-tenant compute node, free from users outside of your organization.  | [More info](/docs/vpc?topic=vpc-logging) | [Message IDs](/docs/vpc?topic=vpc-logging#dedicated-host) |
| [Flow Log Collector](/docs/vpc?topic=vpc-flow-logs)| This service is used to collect and store information regarding the Internet Protocol (IP) traffic going to and from network interfaces within your Virtual Private Cloud (VPC) | [Viewing flow log objects](/docs/vpc?topic=vpc-fl-analyze) | [Message IDs](/docs/vpc?topic=vpc-logging#logging-flow-log-collector_msgs) |
| [VPN](/docs/vpc?topic=vpc-using-vpn) | Use this service to connect private networks in a secure fashion. You can use VPN to set up an IPsec site-to-site tunnel between your VPC and your on-premise private network or another VPC. | [More info](/docs/vpc?topic=vpc-using-log-analysis-to-view-vpn-logs) | |
{: caption="Table 8. List of IBM Cloud VPC services" caption-side="top"}

## Classic Infrastructure services
{: #classic-infrastructure}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:


| Service          | Description | More info         | Message IDs |
|------------------|-------------|-------------------|-------------|
| [{{site.data.keyword.loadbalancer_full}}](/docs/loadbalancer-service?topic=loadbalancer-service-getting-started) | Use this service to improve availability of business-critical applications by distributing traffic among multiple application server instances, and by forwarding traffic to healthy instances only. | [More info](/docs/loadbalancer-service?topic=loadbalancer-service-data-logging) | |
{: caption="Table 9. List of Classic Infrastructure services" caption-side="top"}


## Security services
{: #security}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:


| Service     | Description | More info |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.secrets-manager_full}}](/docs/secrets-manager?topic=secrets-manager-getting-started) | With {{site.data.keyword.secrets-manager_full_notm}}, you can create, lease, and centrally manage secrets that are used in {{site.data.keyword.cloud_notm}} services or your custom-built applications. | [More info](/docs/secrets-manager?topic=secrets-manager-service-logs) |
{: caption="Table 10. List of security Cloud services" caption-side="top"}

You can monitor logs through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs in the location where the service is running.
{: note}

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Security services](/docs/log-analysis?topic=log-analysis-cloud_services_locations#cs_locations_security).
