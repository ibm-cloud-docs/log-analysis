---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

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


# Cloud services that send logs to a custom logging instance
{: #cloud_services_agent}

List of {{site.data.keyword.cloud}} services that send logs to a custom {{site.data.keyword.la_full_notm}} instance. These services require additional configuration, for example, they may require to configure a logging agent.
{:shortdesc}

You can choose the logging instance where you want to collect service logs. You can choose to send logs to the logging instance that has the **platform logs** flag, or to a custom instance in your account.



## Analytics services
{: #cloud_services_agent_analytics}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description |  More info 
|-------------|-------------|--------------------------------------------------------------------------------------------|
| [{{site.data.keyword.iae_full_notm}}](/docs/AnalyticsEngine?topic=AnalyticsEngine-getting-started) | {{site.data.keyword.iae_full_notm}} provides a flexible framework to develop and deploy analytics applications in Apache Hadoop and Apache Spark. | [More info](/docs/AnalyticsEngine?topic=AnalyticsEngine-log-aggregation#reconfiguring-log-aggregation) | 
{: caption="Table 1. List of Blockchain services" caption-side="top"} 

To see the list of {{site.data.keyword.la_full_notm}} locations where you can send logs, see [Analytics services](/docs/log-analysis?topic=log-analysis-regions).


## Blockchain services
{: #cloud_services_agent_blockchain}

The following table lists Cloud services that send logs to {{site.data.keyword.la_full_notm}}:

| Service     | Description |  More info 
|-------------|-------------|--------------------------------------------------------------------------------------------|
| [{{site.data.keyword.blockchainfull_notm}}](/docs/blockchain?topic=blockchain-get-started-ibp) | {{site.data.keyword.blockchainfull}} Platform provides a managed and full stack blockchain-as-a-service (BaaS) offering that allows you to deploy blockchain components in environments of your choice. | [More info](/docs/blockchain?topic=blockchain-ibp-LogDNA) | 
{: caption="Table 2. List of Blockchain services" caption-side="top"} 

To see the list of {{site.data.keyword.la_full_notm}} locations where you can send logs, see [Container services](/docs/log-analysis?topic=log-analysis-regions).



## Cloud Foundry
{: #cloud_services_agent_cfapps}

You can configure a Cloud Foundry app to forward logs to a custom logging instance by using Syslog drains. [Learn more](/docs/log-analysis?topic=log-analysis-monitor_cfapp_logs#monitor_cfapp_logs_drains).



