---

copyright:
  years: 2019
lastupdated: "2019-08-27"

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

The following table shows the locations where automatic collection of Cloud Foundry (CF) logs is enabled. You can monitor these logs through the {{site.data.keyword.la_full_notm}}  instance that is configured with the **service platform logs** in the same location where the CF resource is available.

| Service                                                       | `Dallas (us-south)` |
|---------------------------------------------------------------|:--------------------:|
| Cloud Foundry (CF)                                            | ![Checkmark icon](../../icons/checkmark-icon.svg)              |
{: caption="Table 1. Cloud Foundry in America" caption-side="top"}
{: #cs-cfapps-table-1}
{: tab-title="America"}
{: tab-group="cs_cfapps"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                       | `Tokyo (jp-tok)`                                  | `Sydney (au-syd)` |
|---------------------------------------------------------------|:-------------------------------------------------:|:------------------|
| Cloud Foundry (CF)                                            | ![Checkmark icon](../../icons/checkmark-icon.svg) | `Logs are available through the Log Analysis Tokyo instance` |
{: caption="Table 2. Cloud Foundry in Asia Pacific" caption-side="top"}
{: #cs-cfapps-table-2}
{: tab-title="Asia Pacific"}
{: tab-group="cs_cfapps"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                       | `Frankfurt (eu-de)` | `London (eu-gb)` |
|---------------------------------------------------------------|:-------------------:|:----------------:|
| Cloud Foundry (CF)                                            | ![Checkmark icon](../../icons/checkmark-icon.svg) | ![Checkmark icon](../../icons/checkmark-icon.svg)  |
{: caption="Table 3. Cloud Foundry in Europe" caption-side="top"}
{: #cs-cfapps-table-3}
{: tab-title="Europe"}
{: tab-group="cs_cfapps"}
{: class="simple-tab-table"}
{: row-headers}



## Platform: Database services
{: #cs_locations_database}

The following tables list the locations where automatic collection of database service logs is enabled. You can monitor logs through the Log Analysis instance that is available in the same location as your database resources, if you enable 1 instance in this location to host service platform logs. For locations where you can provision a service instance but the {{site.data.keyword.la_full_notm}} service is not available, specific detail about the location where you can monitor those logs is provided in each case.

| Service                                                         | `Dallas (us-south)` | `Washington (us-east)`  |
|-----------------------------------------------------------------|:-------------------:|:-------------------:|
| {{site.data.keyword.cloudant_short_notm}}                       | ![Checkmark icon](../../icons/checkmark-icon.svg) `(beta)`        | `NO`                |
| {{site.data.keyword.databases-for-elasticsearch_full_notm}}     | ![Checkmark icon](../../icons/checkmark-icon.svg)               | `NO`                |
| {{site.data.keyword.databases-for-etcd_full_notm}}              | ![Checkmark icon](../../icons/checkmark-icon.svg)               | `NO`                |
| {{site.data.keyword.databases-for-mongodb_full_notm}}           | ![Checkmark icon](../../icons/checkmark-icon.svg)               | `NO`                |
| {{site.data.keyword.databases-for-postgresql_full_notm}}        | ![Checkmark icon](../../icons/checkmark-icon.svg)`               | `NO`                |
| {{site.data.keyword.messages-for-rabbitmq_full_notm}}           | ![Checkmark icon](../../icons/checkmark-icon.svg)               | `NO`                |
| {{site.data.keyword.databases-for-redis_full_notm}}             | ![Checkmark icon](../../icons/checkmark-icon.svg)               | `NO`                |
| {{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_mongodb_full}}             | ![Checkmark icon](../../icons/checkmark-icon.svg)               | `NO`                |
| {{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_postgresql_full}}             | ![Checkmark icon](../../icons/checkmark-icon.svg)               | `NO`                |
{: caption="Table 4. Database services integration in America's locations" caption-side="top"}
{: #cs-dbs-table-1}
{: tab-title="America"}
{: tab-group="cs_dbs"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                         | `Tokyo (jp-tok)`   |`Sydney (au-syd)` | `Seoul 01 (seo01)`       | `Chennai 01 (che01)`     |
|-----------------------------------------------------------------|:------------------:|:----------------:|:-------------------------|:-------------------------|
| {{site.data.keyword.cloudant_short_notm}}                       | `NO`               | `NO`             | `NO`                     | `NO`                     |
| {{site.data.keyword.databases-for-elasticsearch_full_notm}}     | ![Checkmark icon](../../icons/checkmark-icon.svg)   | `NO`             | `Logs are available through the Log Analysis Tokyo instance` | `Logs are available through the Log Analysis Tokyo instance` |
| {{site.data.keyword.databases-for-etcd_full_notm}}              | ![Checkmark icon](../../icons/checkmark-icon.svg)   | `NO`             | `Logs are available through the Log Analysis Tokyo instance` | `Logs are available through the Log Analysis Tokyo instance` |
| {{site.data.keyword.databases-for-mongodb_full_notm}}           | ![Checkmark icon](../../icons/checkmark-icon.svg)    | `NO`             | `Logs are available through the Log Analysis Tokyo instance` | `Logs are available through the Log Analysis Tokyo instance` |
| {{site.data.keyword.databases-for-postgresql_full_notm}}        | ![Checkmark icon](../../icons/checkmark-icon.svg)    | `NO`             | `Logs are available through the Log Analysis Tokyo instance` | `Logs are available through the Log Analysis Tokyo instance` |
| {{site.data.keyword.messages-for-rabbitmq_full_notm}}           | ![Checkmark icon](../../icons/checkmark-icon.svg)    | `NO`             | `Logs are available through the Log Analysis Tokyo instance` | `Logs are available through the Log Analysis Tokyo instance` |
| {{site.data.keyword.databases-for-redis_full_notm}}             | ![Checkmark icon](../../icons/checkmark-icon.svg)    | `NO`             | `Logs are available through the Log Analysis Tokyo instance` | `Logs are available through the Log Analysis Tokyo instance` |
{: caption="Table 5. Database services integration in AP locations" caption-side="top"}
{: #cs-dbs-table-2}
{: tab-title="Asia Pacific"}
{: tab-group="cs_dbs"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                       |`Frankfurt (eu-de)`  | `London (eu-gb)` | `Oslo 01 (osl01)`         |
|---------------------------------------------------------------|:-------------------:|:----------------:|:--------------------------|
| {{site.data.keyword.cloudant_short_notm}}                     | `NO`                | `NO`             | `NO`                      |
| {{site.data.keyword.databases-for-elasticsearch_full_notm}}   | `NO`                | ![Checkmark icon](../../icons/checkmark-icon.svg)            | `Logs are available through the Log Analysis London instance` |
| {{site.data.keyword.databases-for-etcd_full_notm}}            | `NO`                | ![Checkmark icon](../../icons/checkmark-icon.svg)            | `Logs are available through the Log Analysis London instance` |
| {{site.data.keyword.databases-for-mongodb_full_notm}}         | `NO`                | ![Checkmark icon](../../icons/checkmark-icon.svg)            | `Logs are available through the Log Analysis London instance` |
| {{site.data.keyword.databases-for-postgresql_full_notm}}      | `NO`                | ![Checkmark icon](../../icons/checkmark-icon.svg)            | `Logs are available through the Log Analysis London instance` |
| {{site.data.keyword.messages-for-rabbitmq_full_notm}}         | `NO`                | ![Checkmark icon](../../icons/checkmark-icon.svg)            | `Logs are available through the Log Analysis London instance` |
| {{site.data.keyword.databases-for-redis_full_notm}}           | `NO`                | ![Checkmark icon](../../icons/checkmark-icon.svg)            | `Logs are available through the Log Analysis London instance` |
{: caption="Table 6. Database services integration in Europe locations" caption-side="top"}
{: #cs-dbs-table-3}
{: tab-title="Europe"}
{: tab-group="cs_dbs"}
{: class="simple-tab-table"}
{: row-headers}


## Platform: Security services
{: #cs_locations_security}

The following tables list the locations where automatic collection of security service logs is enabled. You can monitor logs through the Log Analysis instance that is available in the same location as your security resources, if you enable 1 instance in this location to host service platform logs. For locations where you can provision a service instance but the {{site.data.keyword.la_full_notm}} service is not available, specific detail about the location where you can monitor those logs is provided in each case.


| Service                                                         | `Dallas (us-south)` | `Washington (us-east)`                   |
|-----------------------------------------------------------------|---------------------|--------------------------------------|
| {{site.data.keyword.cloudcerts_full_notm}}                      | ![Checkmark icon](../../icons/checkmark-icon.svg)               | `NO`                                 |            
{: caption="Table 7. Security services integration in America's locations" caption-side="top"}
{: #cs-sec-table-1}
{: tab-title="America"}
{: tab-group="cs_sec"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                         | `Tokyo (jp-tok)` |`Sydney (au-syd)`           |
|-----------------------------------------------------------------|:----------------:|:---------------------------|
| {{site.data.keyword.cloudcerts_full_notm}}                      | ![Checkmark icon](../../icons/checkmark-icon.svg)            | `NO`                       |
{: caption="Table 8. Security services integration in AP locations" caption-side="top"}
{: #cs-sec-table-2}
{: tab-title="Asia Pacific"}
{: tab-group="cs_sec"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                       |`Frankfurt (eu-de)`  | `London (eu-gb)` |
|---------------------------------------------------------------|:-------------------:|:----------------:|
| {{site.data.keyword.cloudcerts_full_notm}}                    | ![Checkmark icon](../../icons/checkmark-icon.svg)               | `NO`             |
{: caption="Table 9. Security services  integration in Europe locations" caption-side="top"}
{: #cs-sec-table-3}
{: tab-title="Europe"}
{: tab-group="cs_sec"}
{: class="simple-tab-table"}
{: row-headers}
