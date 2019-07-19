---

copyright:
  years: 2019
lastupdated: "2019-07-18"

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

List of locations where {{site.data.keyword.cloud_notm}} services are enabled to send logs to {{site.data.keyword.la_full_notm}}:
{:shortdesc}


## Compute: Cloud Foundry
{: #cs_locations_platform_cfapps}

| Service                                                       | `Dallas (us-south)` | `Frankfurt (eu-de)` | `London (eu-gb)` | `Tokyo (jp-tok)` |
|---------------------------------------------------------------|---------------------|---------------------|------------------|------------------|
| Cloud Foundry (CF)                                            | `YES`               | `YES`               | `YES`            | `YES`            |
{: caption="Table 1. Cloud Foundry" caption-side="top"} 


## Platform: Database services
{: #cs_locations_database}

| Service                                                       | `Dallas (us-south)` | `Frankfurt (eu-de)` | `London (eu-gb)` | `Tokyo (jp-tok)` |
|---------------------------------------------------------------|---------------------|---------------------|------------------|------------------|
| {{site.data.keyword.databases-for-elasticsearch_full_notm}}   | `YES`               | `NO`                | `YES`            | `YES`            |
| {{site.data.keyword.databases-for-etcd_full_notm}}            | `YES`               | `NO`                | `YES`            | `YES`            |
| {{site.data.keyword.databases-for-mongodb_full_notm}}         | `YES`               | `NO`                | `YES`            | `YES`            |
| {{site.data.keyword.databases-for-postgresql_full_notm}}      | `YES`               | `NO`                | `YES`            | `YES`            |
| {{site.data.keyword.messages-for-rabbitmq_full_notm}}         | `YES`               | `NO`                | `YES`            | `YES`            |
| {{site.data.keyword.databases-for-redis_full_notm}}           | `YES`               | `NO`                | `YES`            | `YES`            |
{: caption="Table 2. Database services " caption-side="top"} 


## Platform: Security services
{: #cs_locations_security}

| Service                                                       | `Dallas (us-south)` | `Dallas (us-east)` | `Frankfurt (eu-de)` | `London (eu-gb)` | `Tokyo (jp-tok)`   | `Sydney (au-syd`)  |
|---------------------------------------------------------------|---------------------|---------------------|---------------------|------------------|--------------------|------------------|
| {{site.data.keyword.cloudcerts_full_notm}}                    | `YES`               | `NO`                | `YES`               | `NO`             | `YES`              | `NO`               |
| {{site.data.keyword.keymanagementservicelong}}                | `YES`               | `Through Dallas (us-south) instance`  | `Through Frankfurt instance`   | `YES`            | `Through Tokyo instance`   |
{: caption="Table 3. Security services " caption-side="top"} 



Tokyo has for (au-syd,jp-tok)