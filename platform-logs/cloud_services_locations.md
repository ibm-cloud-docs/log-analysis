---

copyright:
  years:  2018, 2020
lastupdated: "2020-12-02"

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


# Cloud services by location
{: #cloud_services_locations}

List of locations where {{site.data.keyword.cloud_notm}} services are enabled to send logs to {{site.data.keyword.la_full_notm}}. You monitor these logs that you monitor through the {{site.data.keyword.la_short}} instance that is configured to receive platform services logs. [Learn more about enabling service platform logs](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-config_svc_logs).
{:shortdesc}


## Cloud Foundry
{: #cs_locations_platform_cfapps}

The following table shows the locations where automatic collection of Cloud Foundry (CF) logs is enabled. You can monitor these logs through the {{site.data.keyword.la_full_notm}}  instance that is configured with the **service platform logs** in the same location where the CF resource is available.

| Service                                                       | `Dallas (us-south)` |
|---------------------------------------------------------------|--------------------|
| Cloud Foundry (CF)                                            | ![Checkmark icon](../images/checkmark-icon.svg)            |
{: caption="Table 1. Cloud Foundry in America" caption-side="top"}
{: #cs-cfapps-table-1}
{: tab-title="America"}
{: tab-group="cs_cfapps"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                       | `Tokyo (jp-tok)`                                  | `Sydney (au-syd)` |
|---------------------------------------------------------------|-------------------------------------------------|------------------|
| Cloud Foundry (CF)                                            | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
{: caption="Table 2. Cloud Foundry in Asia Pacific" caption-side="top"}
{: #cs-cfapps-table-2}
{: tab-title="Asia Pacific"}
{: tab-group="cs_cfapps"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                       | `Frankfurt (eu-de)` | `London (eu-gb)` |
|---------------------------------------------------------------|-------------------|----------------|
| Cloud Foundry (CF)                                            | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg)|
{: caption="Table 3. Cloud Foundry in Europe" caption-side="top"}
{: #cs-cfapps-table-3}
{: tab-title="Europe"}
{: tab-group="cs_cfapps"}
{: class="simple-tab-table"}
{: row-headers}


## Container services
{: #cs_locations_container}

You can choose the LogDNA instance where you want to collect {{site.data.keyword.containerlong}} service logs.

You can choose the LogDNA instance where you want to collect {{site.data.keyword.openshiftlong}} service logs.

You can choose the LogDNA instance where you want to collect {{site.data.keyword.satellitelong}} service logs.

The following tables list the locations where automatic collection of registry service logs is enabled. You can monitor logs through the Log Analysis instance that is available in the same location as your database resources, if you enable 1 instance in this location to host service platform logs. For locations where you can provision a service instance but the {{site.data.keyword.la_full_notm}} service is not available, specific detail about the location where you can monitor those logs is provided in each case.

| Service                                                         | `Dallas (us-south)` | `Washington (us-east)`                   |
|-----------------------------------------------------------------|---------------------|--------------------------------------|
| {{site.data.keyword.registrylong_notm}}                      | ![Checkmark icon](../images/checkmark-icon.svg)             |                                 |            
{: caption="Table 4. Container services" caption-side="top"}
{: #cs-con-table-1}
{: tab-title="America"}
{: tab-group="cs_con"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                         | `Tokyo (jp-tok)` |`Sydney (au-syd)`           |
|-----------------------------------------------------------------|----------------|---------------------------|
| {{site.data.keyword.registrylong_notm}}                         | ![Checkmark icon](../images/checkmark-icon.svg)  | `Logs are available through the Log Analysis Tokyo instance`  |
{: caption="Table 5. Container services" caption-side="top"}
{: #cs-con-table-2}
{: tab-title="Asia Pacific"}
{: tab-group="cs_con"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                       |`Frankfurt (eu-de)`  | `London (eu-gb)` |
|---------------------------------------------------------------|-------------------|----------------|
| {{site.data.keyword.registrylong_notm}}                    |  ![Checkmark icon](../images/checkmark-icon.svg)            | ![Checkmark icon](../images/checkmark-icon.svg)|
{: caption="Table 6. Container services" caption-side="top"}
{: #cs-con-table-3}
{: tab-title="Europe"}
{: tab-group="cs_con"}
{: class="simple-tab-table"}
{: row-headers}


## Database services
{: #cs_locations_database}

The following tables list the locations where automatic collection of database service logs is enabled. You can monitor logs through the Log Analysis instance that is available in the same location as your database resources, if you enable 1 instance in this location to host service platform logs. For locations where you can provision a service instance but the {{site.data.keyword.la_full_notm}} service is not available, specific detail about the location where you can monitor those logs is provided in each case.

| Service                                                         | `Dallas (us-south)` | `Washington (us-east)`  |
|-----------------------------------------------------------------|-------------------|-------------------|
| {{site.data.keyword.cloudant_short_notm}}                       | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg)  |
| {{site.data.keyword.databases-for-enterprisedb_full_notm}}      | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
| {{site.data.keyword.databases-for-cassandra_full_notm}}         | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
| {{site.data.keyword.databases-for-elasticsearch_full_notm}}     | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
| {{site.data.keyword.databases-for-etcd_full_notm}}              | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
| {{site.data.keyword.databases-for-mongodb_full_notm}}           | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
| {{site.data.keyword.databases-for-postgresql_full_notm}}        | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
| {{site.data.keyword.messages-for-rabbitmq_full_notm}}           | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
| {{site.data.keyword.databases-for-redis_full_notm}}             | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
| {{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_mongodb_full}}     | ![Checkmark icon](../images/checkmark-icon.svg)             |                |
| {{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_postgresql_full}}      | ![Checkmark icon](../images/checkmark-icon.svg)        |                |
{: caption="Table 7. Database services" caption-side="top"}
{: #cs-dbs-table-1}
{: tab-title="America"}
{: tab-group="cs_dbs"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                         | `Tokyo (jp-tok)`   |`Sydney (au-syd)` | `Seoul 01 (seo01)`       | `Chennai 01 (che01)`     |`Seoul (kr-seo)` | 
|-----------------------------------------------------------------|--------------------|------------------|--------------------------|--------------------------|------------------|
| {{site.data.keyword.cloudant_short_notm}}                       | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |     | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg)  |
| {{site.data.keyword.databases-for-enterprisedb_full_notm}}      | ![Checkmark icon](../images/checkmark-icon.svg) |![Checkmark icon](../images/checkmark-icon.svg) | `Logs are available through the Tokyo instance` | ![Checkmark icon](../images/checkmark-icon.svg) |             | 
| {{site.data.keyword.databases-for-cassandra_full_notm}}         | ![Checkmark icon](../images/checkmark-icon.svg) |![Checkmark icon](../images/checkmark-icon.svg) | `Logs are available through the Tokyo instance` | ![Checkmark icon](../images/checkmark-icon.svg) |             |
| {{site.data.keyword.databases-for-elasticsearch_full_notm}}     | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) | `Logs are available through the Log Analysis Tokyo instance` | ![Checkmark icon](../images/checkmark-icon.svg) |                      |
| {{site.data.keyword.databases-for-etcd_full_notm}}              | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg)| `Logs are available through the Log Analysis Tokyo instance` | ![Checkmark icon](../images/checkmark-icon.svg) |                      |
| {{site.data.keyword.databases-for-mongodb_full_notm}}           | ![Checkmark icon](../images/checkmark-icon.svg)  | ![Checkmark icon](../images/checkmark-icon.svg) | `Logs are available through the Log Analysis Tokyo instance` | ![Checkmark icon](../images/checkmark-icon.svg) |                      |
| {{site.data.keyword.databases-for-postgresql_full_notm}}        | ![Checkmark icon](../images/checkmark-icon.svg)  | ![Checkmark icon](../images/checkmark-icon.svg) | `Logs are available through the Log Analysis Tokyo instance` | ![Checkmark icon](../images/checkmark-icon.svg) |                      |
| {{site.data.keyword.messages-for-rabbitmq_full_notm}}           | ![Checkmark icon](../images/checkmark-icon.svg)  | ![Checkmark icon](../images/checkmark-icon.svg) | `Logs are available through the Log Analysis Tokyo instance` | ![Checkmark icon](../images/checkmark-icon.svg) |                      |
| {{site.data.keyword.databases-for-redis_full_notm}}             | ![Checkmark icon](../images/checkmark-icon.svg)  | ![Checkmark icon](../images/checkmark-icon.svg) | `Logs are available through the Log Analysis Tokyo instance` | ![Checkmark icon](../images/checkmark-icon.svg) |                      |
| {{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_mongodb_full}}             |    | `Logs are available through the Log Analysis Dallas instance`        |   |   |    |
| {{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_postgresql_full}}     |    | `Logs are available through the Log Analysis Dallas instance`        |   |   |   |
{: caption="Table 8. Database services" caption-side="top"}
{: #cs-dbs-table-2}
{: tab-title="Asia Pacific"}
{: tab-group="cs_dbs"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                       |`Frankfurt (eu-de)`  | `London (eu-gb)` | `Oslo 01 (osl01)`         |
|---------------------------------------------------------------|-------------------|----------------|--------------------------|
| {{site.data.keyword.cloudant_short_notm}}                     | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |                      |
| {{site.data.keyword.databases-for-elasticsearch_full_notm}}   | ![Checkmark icon](../images/checkmark-icon.svg)| ![Checkmark icon](../images/checkmark-icon.svg)          | `Logs are available through the Log Analysis London instance` |
| {{site.data.keyword.databases-for-etcd_full_notm}}            | ![Checkmark icon](../images/checkmark-icon.svg)| ![Checkmark icon](../images/checkmark-icon.svg)          | `Logs are available through the Log Analysis London instance` |
| {{site.data.keyword.databases-for-mongodb_full_notm}}         | ![Checkmark icon](../images/checkmark-icon.svg)| ![Checkmark icon](../images/checkmark-icon.svg)          | `Logs are available through the Log Analysis London instance` |
| {{site.data.keyword.databases-for-postgresql_full_notm}}      | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg)          | `Logs are available through the Log Analysis London instance` |
| {{site.data.keyword.messages-for-rabbitmq_full_notm}}         | ![Checkmark icon](../images/checkmark-icon.svg)| ![Checkmark icon](../images/checkmark-icon.svg)          | `Logs are available through the Log Analysis London instance` |
| {{site.data.keyword.databases-for-redis_full_notm}}           | ![Checkmark icon](../images/checkmark-icon.svg)| ![Checkmark icon](../images/checkmark-icon.svg)          | `Logs are available through the Log Analysis London instance` |
| {{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_mongodb_full}}           | ![Checkmark icon](../images/checkmark-icon.svg)              |           |        |
| {{site.data.keyword.cloud_notm}} {{site.data.keyword.ihsdbaas_postgresql_full}}           | ![Checkmark icon](../images/checkmark-icon.svg)              |           |        |
{: caption="Table 9. Database services" caption-side="top"}
{: #cs-dbs-table-3}
{: tab-title="Europe"}
{: tab-group="cs_dbs"}
{: class="simple-tab-table"}
{: row-headers}



## Integration services
{: #cs_locations_integration}

| Service                                         | `Dallas (us-south)`                          | `Washington (us-east)`            |
|-------------------------------------------------|----------------------------------------------|-----------------------------------|
| {{site.data.keyword.appconservicefull}}         | ![Checkmark icon](../images/checkmark-icon.svg) |                              |
| {{site.data.keyword.mq_short}}                  | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |            
{: caption="Table 10. Integration services" caption-side="top"}
{: #cs-int-table-10}
{: tab-title="America"}
{: tab-group="cs_int"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                         | `Tokyo (jp-tok)` |`Sydney (au-syd)`           |
|-----------------------------------------------------------------|----------------|---------------------------|
| {{site.data.keyword.appconservicefull}}                      |    | ![Checkmark icon](../images/checkmark-icon.svg)|
| {{site.data.keyword.mq_short}}                               |     | ![Checkmark icon](../images/checkmark-icon.svg)|
{: caption="Table 11. Integration services" caption-side="top"}
{: #cs-int-table-11}
{: tab-title="Asia Pacific"}
{: tab-group="cs_int"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                       |`Frankfurt (eu-de)`  | `London (eu-gb)` |
|---------------------------------------------------------------|-------------------|----------------|
| {{site.data.keyword.appconservicefull}}                    |               | ![Checkmark icon](../images/checkmark-icon.svg)|
| {{site.data.keyword.mq_short}}                  | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
{: caption="Table 12. Integration services" caption-side="top"}
{: #cs-int-table-12}
{: tab-title="Europe"}
{: tab-group="cs_int"}
{: class="simple-tab-table"}
{: row-headers}



## Networking services
{: #cs_locations_networking}

| Service                                                         | `Dallas (us-south)` | `Washington (us-east)`                   |
|-----------------------------------------------------------------|---------------------|--------------------------------------|
| {{site.data.keyword.loadbalancer_full}} `[1]`                | ![Checkmark icon](../images/checkmark-icon.svg)             |                                 |            
{: caption="Table 13. Networking services" caption-side="top"}
{: #cs-net-table-13}
{: tab-title="America"}
{: tab-group="cs_net"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                         | `Tokyo (jp-tok)` |`Sydney (au-syd)`           |
|-----------------------------------------------------------------|----------------|---------------------------|
| {{site.data.keyword.loadbalancer_full}} `[1]`                  |    |  |
{: caption="Table 14. Networking services" caption-side="top"}
{: #cs-net-table-14}
{: tab-title="Asia Pacific"}
{: tab-group="cs_net"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                       |`Frankfurt (eu-de)`  | `London (eu-gb)` |
|---------------------------------------------------------------|-------------------|----------------|
| {{site.data.keyword.loadbalancer_full}} `[1]`               |               |  |
{: caption="Table 15. Networking services" caption-side="top"}
{: #cs-net-table-15}
{: tab-title="Europe"}
{: tab-group="cs_net"}
{: class="simple-tab-table"}
{: row-headers}

`[1]` Data logs are only sent if your Softlayer and {{site.data.keyword.cloud}} accounts are linked.

## Security services
{: #cs_locations_security}

The following tables list the locations where automatic collection of security service logs is enabled. You can monitor logs through the Log Analysis instance that is available in the same location as your security resources, if you enable 1 instance in this location to host service platform logs. For locations where you can provision a service instance but the {{site.data.keyword.la_full_notm}} service is not available, specific detail about the location where you can monitor those logs is provided in each case.


| Service                                                         | `Dallas (us-south)` | `Washington (us-east)`                   |
|-----------------------------------------------------------------|---------------------|--------------------------------------|
| {{site.data.keyword.cloudcerts_full_notm}}                      | ![Checkmark icon](../images/checkmark-icon.svg)             |                                 |            
{: caption="Table 16. Security services" caption-side="top"}
{: #cs-sec-table-16}
{: tab-title="America"}
{: tab-group="cs_sec"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                         | `Tokyo (jp-tok)` |`Sydney (au-syd)`           |
|-----------------------------------------------------------------|----------------|---------------------------|
| {{site.data.keyword.cloudcerts_full_notm}}                      | ![Checkmark icon](../images/checkmark-icon.svg)          | ![Checkmark icon](../images/checkmark-icon.svg) |
{: caption="Table 17. Security services" caption-side="top"}
{: #cs-sec-table-17}
{: tab-title="Asia Pacific"}
{: tab-group="cs_sec"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                       |`Frankfurt (eu-de)`  | `London (eu-gb)` |
|---------------------------------------------------------------|-------------------|----------------|
| {{site.data.keyword.cloudcerts_full_notm}}                    | ![Checkmark icon](../images/checkmark-icon.svg)             | ![Checkmark icon](../images/checkmark-icon.svg) |
{: caption="Table 18. Security services" caption-side="top"}
{: #cs-sec-table-18}
{: tab-title="Europe"}
{: tab-group="cs_sec"}
{: class="simple-tab-table"}
{: row-headers}



## VPC infrastructure services
{: #cloud_services_locations_vpc_infrastructure}

The followinf locations are valid for VPC Gen 1 and VPC Gen 2:

| Service                                | `Dallas (us-south)`                                | `Washington (us-east)`               |
|----------------------------------------|----------------------------------------------------|--------------------------------------|
| VPN                                    | ![Checkmark icon](../images/checkmark-icon.svg) | `Logs are available through the LogDNA US-South instance` |
{: caption="Table 19. VPC events in America's locations" caption-side="top"}
{: #cs-vpc-table-19}
{: tab-title="America"}
{: tab-group="cs_vpc"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                         | `Tokyo (jp-tok)` |`Sydney (au-syd)`           |
|-----------------------------------------------------------------|------------------|----------------------------|
| VPN                                              | ![Checkmark icon](../images/checkmark-icon.svg)             | ![Checkmark icon](../images/checkmark-icon.svg) |      
{: caption="Table 20. VPC events in AP locations" caption-side="top"}
{: #cs-vpc-table-20}
{: tab-title="Asia Pacific"}
{: tab-group="cs_vpc"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                       |`Frankfurt (eu-de)`  | `London (eu-gb)` |
|---------------------------------------------------------------|---------------------|------------------|
| VPN                                                           | ![Checkmark icon](../images/checkmark-icon.svg)  | ![Checkmark icon](../images/checkmark-icon.svg) |           
{: caption="Table 21. VPC events in Europe locations" caption-side="top"}
{: #cs-vpc-table-21}
{: tab-title="Europe"}
{: tab-group="cs_vpc"}
{: class="simple-tab-table"}
{: row-headers}



## Watson AI
{: #cloud_services_locations_watson_ai}


| Service                                                         | `Dallas (us-south)` | `Washington (us-east)`                   |
|-----------------------------------------------------------------|---------------------|--------------------------------------|
| {{site.data.keyword.iva_full_notm}}                                  | ![Checkmark icon](../images/checkmark-icon.svg)             | `Logs are available through the Log Analysis Dallas instance` |  
{: caption="Table 22. Watson AI in America's locations" caption-side="top"}
{: #cs-wat-table-22}
{: tab-title="America"}
{: tab-group="cs_sec"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                         | `Tokyo (jp-tok)` |`Sydney (au-syd)`           |
|-----------------------------------------------------------------|----------------|---------------------------|
| {{site.data.keyword.iva_full_notm}}                                                |            |   |
{: caption="Table 23. Watson AI in AP locations" caption-side="top"}
{: #cs-wat-table-23}
{: tab-title="Asia Pacific"}
{: tab-group="cs_sec"}
{: class="simple-tab-table"}
{: row-headers}

| Service                                                       |`Frankfurt (eu-de)`  | `London (eu-gb)` |
|---------------------------------------------------------------|-------------------|----------------|
| {{site.data.keyword.iva_full_notm}}                           |  |    |
{: caption="Table 24. Watson AI in Europe locations" caption-side="top"}
{: #cs-wat-table-24}
{: tab-title="Europe"}
{: tab-group="cs_sec"}
{: class="simple-tab-table"}
{: row-headers}



