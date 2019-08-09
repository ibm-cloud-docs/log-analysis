---

copyright:
  years: 2019
lastupdated: "2019-08-09"

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


# Cloud services by location
{: #cloud_services_locations}

List of locations where {{site.data.keyword.cloud_notm}} services are enabled to send logs to {{site.data.keyword.la_full_notm}}. [Learn more about enabling service platform logs](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-config_svc_logs).
{:shortdesc}


## Compute: Cloud Foundry
{: #cs_locations_platform_cfapps}

The following table lists the locations where automatic collection of Cloud Foundry (CF) logs is enabled. You can monitor these logs through the {{site.data.keyword.la_full_notm}}  instance that is configured with the **service platform logs** in the same location where the CF resource is available.

| Service                                                       | `Dallas (us-south)` | `Frankfurt (eu-de)` | `London (eu-gb)` | `Tokyo (jp-tok)` |
|---------------------------------------------------------------|---------------------|---------------------|------------------|------------------|
| Cloud Foundry (CF)                                            | `YES`               | `YES`               | `YES`            | `YES`            |
{: caption="Cloud Foundry" caption-side="top"} 


## Platform: Database services
{: #cs_locations_database}

The following tables list the locations where automatic collection of database service logs is enabled. You can monitor logs through the Log Analysis instance that is available in the same location as your database resources, if you enable 1 instance in this location to host service platform logs. For locations where you can provision a service instance but the {{site.data.keyword.la_full_notm}} service is not available, specific detail about the location where you can monitor those logs is specified in each case.

### Americas
{: #am1}

| Service                                                         | `Dallas (us-south)` | `Dallas (us-east)`  |
|-----------------------------------------------------------------|---------------------|---------------------|
| {{site.data.keyword.cloudant_short_notm}}                       | `Yes (beta)`        | `NO`                |
| {{site.data.keyword.databases-for-elasticsearch_full_notm}}     | `YES`               | `NO`                | 
| {{site.data.keyword.databases-for-etcd_full_notm}}              | `YES`               | `NO`                |
| {{site.data.keyword.databases-for-mongodb_full_notm}}           | `YES`               | `NO`                |
| {{site.data.keyword.databases-for-postgresql_full_notm}}        | `YES`               | `NO`                |
| {{site.data.keyword.messages-for-rabbitmq_full_notm}}           | `YES`               | `NO`                |
| {{site.data.keyword.databases-for-redis_full_notm}}             | `YES`               | `NO`                |
{: caption="Database services integration in America's locations" caption-side="top"} 


### Asia Pacific (AP)
{: #ap1}


| Service                                                         | `Tokyo (jp-tok)` |`Sydney (au-syd)` | `Seoul 01 (seo01)`       | `Chennai 01 (che01)`     |
|-----------------------------------------------------------------|------------------|------------------|--------------------------|--------------------------|
| {{site.data.keyword.cloudant_short_notm}}                       | `NO`             | `NO`             | `NO`                     | `NO`                     |
| {{site.data.keyword.databases-for-elasticsearch_full_notm}}     | `YES`            | `NO`             | `Logs are available through the Log Analysis Tokyo instance` | `Logs are available through the Log Analysis Tokyo instance` |
| {{site.data.keyword.databases-for-etcd_full_notm}}              | `YES`            | `NO`             | `Logs are available through the Log Analysis Tokyo instance` | `Logs are available through the Log Analysis Tokyo instance` |
| {{site.data.keyword.databases-for-mongodb_full_notm}}           | `YES`            | `NO`             | `Logs are available through the Log Analysis Tokyo instance` | `Logs are available through the Log Analysis Tokyo instance` |
| {{site.data.keyword.databases-for-postgresql_full_notm}}        | `YES`            | `NO`             | `Logs are available through the Log Analysis Tokyo instance` | `Logs are available through the Log Analysis Tokyo instance` |
| {{site.data.keyword.messages-for-rabbitmq_full_notm}}           | `YES`            | `NO`             | `Logs are available through the Log Analysis Tokyo instance` | `Logs are available through the Log Analysis Tokyo instance` |
| {{site.data.keyword.databases-for-redis_full_notm}}             | `YES`            | `NO`             | `Logs are available through the Log Analysis Tokyo instance` | `Logs are available through the Log Analysis Tokyo instance` |
{: caption="Database services integration in AP locations" caption-side="top"} 


### Europe (EU)
{: #eu1}

| Service                                                       |`Frankfurt (eu-de)`  | `London (eu-gb)` | `Oslo 01 (osl01)`         |
|---------------------------------------------------------------|---------------------|------------------|---------------------------|
| {{site.data.keyword.cloudant_short_notm}}                     | `NO`                | `NO`             | `NO`                      |
| {{site.data.keyword.databases-for-elasticsearch_full_notm}}   | `NO`                | `YES`            | `Logs are available through the Log Analysis London instance` |
| {{site.data.keyword.databases-for-etcd_full_notm}}            | `NO`                | `YES`            | `Logs are available through the Log Analysis London instance` |
| {{site.data.keyword.databases-for-mongodb_full_notm}}         | `NO`                | `YES`            | `Logs are available through the Log Analysis London instance` | 
| {{site.data.keyword.databases-for-postgresql_full_notm}}      | `NO`                | `YES`            | `Logs are available through the Log Analysis London instance` |
| {{site.data.keyword.messages-for-rabbitmq_full_notm}}         | `NO`                | `YES`            | `Logs are available through the Log Analysis London instance` |
| {{site.data.keyword.databases-for-redis_full_notm}}           | `NO`                | `YES`            | `Logs are available through the Log Analysis London instance` |
{: caption="Database services integration in Europe locations" caption-side="top"} 



## Platform: Security services
{: #cs_locations_security}

The following tables list the locations where automatic collection of security service logs is enabled. You can monitor logs through the Log Analysis instance that is available in the same location as your security resources, if you enable 1 instance in this location to host service platform logs. For locations where you can provision a service instance but the {{site.data.keyword.la_full_notm}} service is not available, specific detail about the location where you can monitor those logs is specified in each case.


### Americas
{: #am1}

| Service                                                         | `Dallas (us-south)` | `Dallas (us-east)`                   |
|-----------------------------------------------------------------|---------------------|--------------------------------------|
| {{site.data.keyword.cloudcerts_full_notm}}                      | `YES`               | `NO`                                 |            
| {{site.data.keyword.keymanagementservicelong}}                  | `YES`               | `Logs are available through the Log Analysis Dallas (us-south) instance` |
{: caption="Security services integration in America's locations" caption-side="top"} 



### Asia Pacific (AP)
{: #ap2}


| Service                                                         | `Tokyo (jp-tok)` |`Sydney (au-syd)`           |
|-----------------------------------------------------------------|------------------|----------------------------|
| {{site.data.keyword.cloudcerts_full_notm}}                      | `YES`            | `NO`                       |
| {{site.data.keyword.keymanagementservicelong}}                  | `YES`            | `Logs are available through the Log Analysis Tokyo instance`   |
{: caption="Security services integration in AP locations" caption-side="top"} 


### Europe (EU)
{: #eu2}

| Service                                                       |`Frankfurt (eu-de)`  | `London (eu-gb)` | 
|---------------------------------------------------------------|---------------------|------------------|
| {{site.data.keyword.cloudcerts_full_notm}}                    | `YES`               | `NO`             |
| {{site.data.keyword.keymanagementservicelong}}                | `YES`               | `NO`             |
{: caption="Security services  integration in Europe locations" caption-side="top"} 



