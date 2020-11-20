---
copyright:
  years: 2018, 2020
lastupdated: "2020-11-20"

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
* If 2 zones fail at the same time, the service is down.

The MZR architecture offers automatic failover between 2 zones, and high availability for a logging instance withing a region.

The SZR architecture offers failover across 3 distinct systems within the single datacenter so that you get high availability from a system failure, but not from a datacenter failure.

## Disaster recovery (DR) of the logging service in a region
{: #dr}

Disaster recovery is about surviving a catastrophic failure or loss of availability in a single location. 

{{site.data.keyword.la_full_notm}} follows {{site.data.keyword.cloud_notm}} requirements for [planning and recovering from disaster events](/docs/overview?topic=overview-zero-downtime#disaster-recovery).

If a regional disaster occurs, consider the following information:
* The estimated recovery time for rebuilding the regional site and restoring the service at another location is 24 hours.
* Older data will not be available when the service is restored. Services that are restored will be available to receive data buffered at end points during course of the outage and future ingested data.  Data previously retained is available through your archives and is not reloaded into your service instance. You can access your archive data directly in {{site.data.keyword.cos_full_notm}} or use the {{site.data.keyword.sqlquery_short}} service to access it.  
* You might have 1 or more logging instances in the region. When these service instances are available in the new location, you will be able to use them. However, you will have to update the endpoints of applications and LogDNA agents to point to the ingestion endpoint in the new location. 

