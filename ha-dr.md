---
copyright:
  years: 2018, 2020
lastupdated: "2020-08-14"

keywords: LogDNA, IBM, Log Analysis, logging, disaster recovery, ha, high availability, redundancy

subcollection: Log-Analysis-with-LogDNA

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:external: target="_blank" .external}
{:codeblock: .codeblock}
{:tip: .tip}
{:note: .note}
{:important: .important}

# High availability and disaster recovery
{: #ha-dr}

{{site.data.keyword.la_full}} is a highly available, multi-tenant, regional service for analyzing logs from your applications, platform resources and infrastructure. In this topic, you can learn more about {{site.data.keyword.la_full_notm}}'s availability and disaster recovery strategies.
{: shortdesc}



## Availability zones
{: #ha-dr_locations}

An availability zone is a logically and physically isolated location within an {{site.data.keyword.cloud_notm}} region where your data is processed and hosted. 
* An availability zone has independent power, cooling, and network infrastructures that are isolated from other zones to strengthen fault tolerance by avoiding single points of failure between zones.
* An availability zone offers high bandwidth and low inter-zone latency within a region.

A region (location) is a geographically and physically separate group of one or more availability zones with independent electrical and network infrastructures isolated from other regions. 
* Regions are designed to remove shared single points of failure with other regions and guarantee low inter-zone latency within the region.
* Each region has 3 different data centers (DC) for redundancy.

The following table lists the high-availability (HA) status for the regions (locations) where the {{site.data.keyword.la_full_notm}} service is available:

| Geography             | Region                   | EU-Supported | HA Status |
|-----------------------|--------------------------|--------------|-----------|
| `Asia Pacific`        |	`Chennai (in-che)`       | `N/A`        | `SZR`     |
| `Asia Pacific`        | `Tokyo (jp-tok)`         | `N/A`        | `MZR`     |
| `Asia Pacific`        | `Seoul (kr-seo)`         | `N/A`        | `SZR`     |
| `Asia Pacific`        | `Sydney (au-syd)`        | `N/A`        | `MZR`     |
| `Europe`              | `Frankfurt (eu-de) (*)`  | `YES`        | `MZR`     |
| `Europe`              | `London (eu-gb)`         | `NO`         | `MZR`     |
| `North America`       | `Dallas (us-south)`      | `N/A`        | `MZR`     |
| `North America`       | `Washington (us-east)`   | `N/A`        | `MZR`     |
{: caption="Table 1. List of locations where the service is available" caption-side="top"}


Where
* A *geography* is a geographic area or larger political body that contains one or more regions.
* A *region* is a defined geographic territory. 

    A region could be a specific postal code area, a town, a city, a state, a group of states, or even a group of countries. 

    A region contains [multiple availability zones](https://www.ibm.com/cloud/data-centers/) to meet local access, low latency, and security requirements for the region.

* `N/A` means feature that is not applicable to that geography.
* `MZR` means multi-zone region. [Learn more](/docs/overview?topic=overview-locations#mzr-table).
* `SZR` means single-zone region. [Learn more](/docs/overview?topic=overview-locations#szr-table).




## Availability of a logging instance
{: #ha-dr-region}

When you provision a logging instance, you select the location where the instance is created. The region determines where the logging data is processed and the data is hosted. 

A multizone region (MZR) consist of 3 or more availability zones that are independent from each other to ensure that single failure events affect only a single zone.

By default, each logging instance consist of 3 zones, one primary zone and two secondary zones: 
* Each zone is located in a different data center in the region.
* The data in your primary zone is automatically replicated to the secondary zones with low latency. You don't need to do anything to enable the replication. 
* When the primary zone fails, a secondary zone is elected as the primary to prevent your service instance from being affected. 
* If 2 zones fail at the same time, the service is down.

The MZR architecture offers automatic failover between 2 zones, and high availability for a logging instance withing a region.

The SZR architecture offers failover across 3 distinct systems within the single datacenter so that you get high availability from a system failure, but not from a datacenter failure.

## Disaster recovery (DR) of the logging service in a region
{: #dr}

Disaster recovery is about surviving a catastrophic failure or loss of availability in a single location. 

{{site.data.keyword.la_full_notm}} follows {{site.data.keyword.cloud_notm}} requirements for [planning and recovering from disaster events](/docs/overview?topic=overview-zero-downtime#disaster-recovery).

If a regional disaster occurs, consider the following information:
* Log data and the logging metadata such as dashboards, alerts, views, screens, templates are backed up every 24 hours. In the event of an un-recoverable disaster, up to 24 hours of data and metadata changes to the logging instance in the failure region can be lost.
* The estimated recovery time for rebuilding the regional site and restoring the service at another location is 24 hours.
* Older data will not be available when the service is restored. If you need access to older data, you can access your archive data directly in {{site.data.keyword.cos_full_notm}} or use the {{site.data.keyword.sqlquery_short}} service to access it.  
* You might have 1 or more logging instances in the region. When these service instances are available in the new location, you will be able to use them while the data is restored into the newly constructed region.
* You will have to update the endpoints of applications and LogDNA agents to point to the ingestion endpoint in the new location. 




### Manual recovery of the service
{: #dr-rebuilt}

If a regional disaster occurs, the recovery time of the service depends on the recovery time for the region. To minimize the downtime of the service and impact to your business, you could implement a manual failover to switch to another region while the region is being restored. To reduce the time to get up and running in a new location, consider using access groups to manage permissions working with the service, and backup the logging metadata of each instance. You should backup your views, alerts, dashboards, screens, and templates definitions on a regular basis.

How to continue working while a DR site is rebuilt?

If the applications and services that you are logging through a logging instance are all co-located in the same region, then you must wait for the region to be available again for business.

If you have deployed LogDNA agents on your systems, and those systems are not impacted by the regional failure, you may choose to redirect logs to other instances of LogDNA in a different region. To redirect data, complete the following steps:
1. [Provision a LogDNA instance](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-provision)
2. Reconfigure the LogDNA agent of each system: Change the ingestion key and ingestion endpoints in the agent configuration. [Learn more](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-logdna_agent).
3. Define IAM permissions to work with the new logging instance.

    Using access groups to manage permissions to work with a LogDNA logging instance, reduces the amount of work that you might have to do to set the correct policies and users to work with a new instance. Information about access groups is global and not region based.
    {: tip}

4. Launch the LogDNA instance and import the views, alerts, dashboards, screens, templates, and exclusion rules.






