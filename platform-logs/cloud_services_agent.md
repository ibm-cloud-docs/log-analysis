---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords:

subcollection: log-analysis


---

{{site.data.keyword.attribute-definition-list}}


# Cloud services that send logs to a custom logging instance
{: #cloud_services_agent}

List of {{site.data.keyword.cloud}} services that send logs to a custom {{site.data.keyword.la_full_notm}} instance. These services require additional configuration, for example, they may require to configure a logging agent.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

You can choose the logging instance where you want to collect service logs. You can choose to send logs to the logging instance that has the **platform logs** flag, or to a custom instance in your account.



## Analytics services
{: #cloud_services_agent_analytics}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description |  More info
|-------------|-------------|--------------------------------------------------------------------------------------------|
| [{{site.data.keyword.iae_full_notm}}](/docs/AnalyticsEngine?topic=AnalyticsEngine-getting-started) | {{site.data.keyword.iae_full_notm}} provides a flexible framework to develop and deploy analytics applications in Apache Hadoop and Apache Spark. | [More info](/docs/AnalyticsEngine?topic=AnalyticsEngine-viewing-logs) |
{: caption="Table 1. List of Analytics services" caption-side="top"}

To see the list of {{site.data.keyword.la_full_notm}} locations where you can send logs, see [Analytics services](/docs/log-analysis?topic=log-analysis-regions).


## Blockchain services
{: #cloud_services_agent_blockchain}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description |  More info
|-------------|-------------|--------------------------------------------------------------------------------------------|
| [{{site.data.keyword.blockchainfull_notm}}](/docs/blockchain?topic=blockchain-get-started-ibp) | {{site.data.keyword.blockchainfull}} Platform provides a managed and full stack blockchain-as-a-service (BaaS) offering that allows you to deploy blockchain components in environments of your choice. | [More info](/docs/blockchain?topic=blockchain-ibp-tracking) |
{: caption="Table 2. List of Blockchain services" caption-side="top"}

To see the list of {{site.data.keyword.la_full_notm}} locations where you can send logs, see [Container services](/docs/log-analysis?topic=log-analysis-regions).


## Container services
{: #cloud_services_agent_container}

The following table lists services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description | More info |
|-------------|-------------|-------------------------------------------------------------------------|
| [{{site.data.keyword.containerlong}}](/docs/containers?topic=containers-getting-started) | You can use the {{site.data.keyword.containerlong_notm}} service to deploy highly available apps in Docker containers that run in Kubernetes clusters. | [More info](/docs/containers?topic=containers-health) |
| [{{site.data.keyword.openshiftlong}}](/docs/openshift?topic=openshift-getting-started) | With {{site.data.keyword.openshiftlong_notm}}, you can deploy apps on highly available clusters that come installed with the Red Hat OpenShift on IBM Cloud Container Platform software installed on Red Hat Enterprise Linux. | [More info](/docs/openshift?topic=openshift-health) |
| [{{site.data.keyword.satellitelong}}](/docs/satellite?topic=satellite-getting-started) | With {{site.data.keyword.satellitelong_notm}}, you can bring your own compute infrastructure to run {{site.data.keyword.cloud_notm}} services and consistently deploy, manage, and control your app workloads. | [More info](/docs/satellite?topic=satellite-health) |
{: caption="Table 3. List of container services" caption-side="top"}

To see the list of {{site.data.keyword.la_full_notm}} locations where these services send logs, see [Container services](/docs/log-analysis?topic=log-analysis-cloud_services_locations#cs_locations_container).
