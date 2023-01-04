---
copyright:
  years: 2018, 2023
lastupdated: "2022-08-17"

keywords: IBM, Log Analysis, logging, disaster recovery, ha, high availability, redundancy

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}


# Recovering from a regional disaster
{: #ha_dr_steps}

{{site.data.keyword.la_full_notm}} is a highly available, multi-tenant, regional service. In this topic, you can learn more about {{site.data.keyword.la_short}}'s availability and disaster recovery strategies, what you need to plan for, and what you need to do if you need to recover from a regional disaster.
{: shortdesc}


## Prereqs
{: #ha_dr_steps_prereqs}

- Learn about your responsibilities in the event of a disaster. See [Disaster and recovery](/docs/log-analysis?topic=log-analysis-shared-responsibilities#disaster-recovery).
- Learn about disaster recovery (DR). See [Overview](#ha_dr_steps_ov).

## Planning for a DR scenario
{: #ha_dr_steps_plan}

The steps in this section assume that you have a list of all {{site.data.keyword.la_full_notm}} instances that are provisioned in a region per resource group; access reports for each instance; a current export of the logging configuration resources per instance; and a list of log sources per region that include information on the logging instance where logs are sent and how those logs are sent, for example, by configuring an agent. You should keep track of any agent versions too and any custom logging resources such as views, boards, screens, parsing templates that might be required to manage those logs.
{: important}

Consider using access groups to manage permissions to work with logging instances. In the event of a DR situation, you can quickly add permissions for users and service IDs per access group and accelerate recovery time.
{: tip}

- To get the access report for an instance, go to the Observability UI, and in the **Logging** section, select 1 instance. Select the 3 dots icon and click **Access report**. Then, save it in a version control tool.

    The report includes a list of users, access groups, and service IDs that have access to the selected resource. You must have the `Administrator` role on the selected resource to view the report.

    You can download the report as CSV or as JSON.

    Generate an access report everytime permissions to work with logging instances change in the account.

    You can use terraform to manage IAM permissions. Consider keeping the terraform script up to date with details of all the IAM resources so that you can recover faster in the event of a DR. For more information on using terraform to provision a logging instance, see [IBM Cloud Provider - Identity and Access Management (IAM)](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs).
    {: tip}

- To get the list of instances including all the details, you can run the following command:

    ```
    ibmcloud resource service-instances --all-resource-groups --output JSON > instances.json
    ```
    {: pre}

    Get current details everytime a change or a new logging instance is created in the account. Then, save the file you saved (`instances.json`) in a version control tool.

    Once the export file is generated, do not modify it. Any change to that file will corrupt the file and you will not be able to import it. For more information, see [Export the configuration of resources in a logging instance](/docs/log-analysis?topic=log-analysis-reuse_resource_definitions).

    You can use terraform to provision logging instances. Consider keeping the terraform script up to date with details of all the instances so that you can recover faster in the event of a DR. For more information on using terraform to provision a logging instance, see [Provisioning an instance by using Terraforms](/docs/log-analysis?topic=log-analysis-terraform-setup).
    {: tip}

- To get the logging agent configuration information, including its version, export the logging agent yaml file for each agent that you have deployed and save it in a version control tool.

    For example, you can run the command to get the yaml file:

    ```
    kubectl get daemonset logdna-agent -o=yaml > prod-logdna-agent-ds.yaml -n ibm-observe
    ```
    {: pre}

## Steps to recover a regional disaster
{: #ha_dr_steps_region}


Complete the following steps to recover {{site.data.keyword.la_full_notm}} from a regional disaster:

1. Decide the region where you plan to recover activity.

    It is best to choose the same recovery region that you choose for the rest of your services that are also impacted in the region that is down.

    Why? Some of those services might generate platform logs.

    Make sure that the region that you choose is a supported region for the {{site.data.keyword.la_full_notm}} service. For more information on supported egions, see [Locations](/docs/log-analysis?topic=log-analysis-regions).
    {: note}

2. Identify the list of instances that are affected in the regional disaster. Then, provision new instances in the new region.

    Use the latest report to know how many instances to create. You can also use your terraform script. Notice that you must edit the script and change the `region` where the instance is to be provisioned.

    If you have an instance that collects IBM Cloud platform logs in the recovery region, make sure you do not define a new instance with the platform logs flag. You should use the existing logging instance in the new region that has the `platform logs` flag to also manage platform logs from services that you restore in the new region.
    {: important}

    If the new region does not have an instance with the flag to collect platform logs, but the region that was down had one, you must configure 1 of the new instances to collect platform logs. For more information, see [Configuring IBM Cloud platform logs](/docs/log-analysis?topic=log-analysis-config_svc_logs).

3. Grant permissions to users, service IDs, and access groups to work with the new logging instances. Use the latest access report to map permissions per instance.

    Use the latest report to map permissions in the new region. You can also use your terraform script.

    If you use access groups, add new policies for the new instances. The users and service IDs within an access group will inherit those new policies.

    If you define permissions by users and service IDs, you must update permissions for each use and for each service ID.

4. Per instance, you must import the logging configuration so any views, parsing templates, boards and screens are uploaded into the new instance. For more information, see [Import the configuration of resources into a logging instance](/docs/log-analysis?topic=log-analysis-reuse_resource_definitions#import_config).

5. For each log source that was affected by the disaster, you must reconfigure the log source to send logs to a logging instance in the new region.

    When you reconfigure an agent, check the region and the ingestion key are the ones for an instance in the new region.

    For example, for Kubernetes clusters, make sure that you reconfigure the logging agent to a new instance. If you have custom views, boards or screens to manage logs from that source, make sure the instance that you reconfigue includes them.

    Other instructions on how to configure log sources:

    - [Connecting a logging agent to a standard Kubernetes cluster](/docs/log-analysis?topic=log-analysis-config_agent_kube_cluster)

    - [Managing a logging agent deployed in an OpenShift cluster](/docs/log-analysis?topic=log-analysis-config_agent_os_cluster)

    - [Configuring a Logging agent for Linux Ubuntu or Debian](/docs/log-analysis?topic=log-analysis-config_agent_linux)

    - [Configuring a Logging agent for a Linux RPM-based](/docs/log-analysis?topic=log-analysis-config_agent_linux_rpm)



If you recover IBM Cloud services and logging instances across different regions, consider streaming logs to 1 or more logging instances so that you can group logs for troubleshooting and analysis that otherwise would be distributed and not collected in the same way as the region that went down. For more information, see [Configuring streaming to a Log Analysis instance](/docs/log-analysis?topic=log-analysis-streaming-configure-l2l).
{: note}




## Overview
{: #ha_dr_steps_ov}

Disaster recovery is about surviving a catastrophic failure or loss of availability in a single location.

{{site.data.keyword.la_short}} is a regional service, there is no automatic cross-regional failover or cross-regional disaster recovery. If all of the availability zones in a region fail, {{site.data.keyword.la_short}} becomes unavailable in that location.

### Availability zones
{: #ha_dr_steps_locations}

The following table lists the high-availability (HA) status for the regions (locations) where the {{site.data.keyword.at_full_notm}} hosted event search service is available:

| Geography             | Region                   | EU-Supported | HA Status |
|-----------------------|--------------------------|--------------|-----------|
| `Asia Pacific`        | `Tokyo (jp-tok)`         | `N/A`        | `MZR`     |
| `Asia Pacific`        | `Osaka (jp-osa)`         | `N/A`        | `MZR`     |
| `Asia Pacific`        | `Seoul (kr-seo)`         | `N/A`        | `SZR`     |
| `Asia Pacific`        | `Chennai (in-che)`       | `N/A`        | `SZR`     |
| `Asia Pacific`        | `Sydney (au-syd)`        | `N/A`        | `MZR`     |
| `Europe`              | `Frankfurt (eu-de)`      | `YES`        | `MZR`     |
| `Europe`              | `London (eu-gb)`         | `NO`         | `MZR`     |
| `North America`       | `Dallas (us-south)`      | `N/A`        | `MZR`     |
| `North America`       | `Washington (us-east)`   | `N/A`        | `MZR`     |
| `North America`       | `Toronto (ca-tor)`       | `N/A`        | `MZR`     |
| `South America`     | `Sao Paulo (br-sao)`       | `N/A`        | `MZR` |
{: caption="Table 1. List of locations where the service is available" caption-side="top"}


Where
* A *geography* is a geographic area or larger political body that contains one or more regions.
* A *region* is a defined geographic territory.

    A region could be a specific postal code area, a town, a city, a state, a group of states, or even a group of countries.

    A region contains [multiple availability zones](https://www.ibm.com/cloud/data-centers/) to meet local access, low latency, and security requirements for the region.

* `N/A` means feature that is not applicable to that geography.
* `MZR` means multi-zone region. [Learn more](/docs/overview?topic=overview-locations#mzr-table).
* `SZR` means single-zone region. [Learn more](/docs/overview?topic=overview-locations#szr-table).



### DR recovery time
{: #ha_dr_steps_recovery_time}

The following table indicates the estimated recovery times in the event of a DR situation:

| Recovery objective for DR | Estimated time |
|---------------------------|----------------|
| Maximum Tolerable Downtime (MTD) / Recovery Time Objective (RTO)  | Less than 24 hours |
| Recovery Point Objective (RPO) | Less than 4 hours |
{: caption="Table 4. Recovery objectives for DR" caption-side="top"}


### MZR
{: #ha_dr_steps_mzr}

A multizone region (MZR) consist of 3 or more availability zones that are independent from each other to ensure that single failure events affect only a single zone. By default, {{site.data.keyword.la_short}} hosted event search is deployed across 3 zones, one primary zone and two secondary zones:
* Each zone is located in a different data center in the region.
* The data in your primary zone is automatically replicated to the secondary zones with low latency. You don't need to do anything to enable the replication.
* The service is designed to withstand a single zone failure with no interruption.

The MZR architecture offers automatic failover between zones within the region, and high availability for a auditing instance withing a region.

### SZR
{: #ha_dr_steps_mzr}

The SZR architecture offers failover across 3 distinct systems within the single datacenter so that you get high availability from a system failure, but not from a datacenter failure.


### Data availability for {{site.data.keyword.at_short}} hosted event search offerings
{: #ha_dr_steps_data_availability}

When you provision an auditing instance, you select the location where the instance is created. The region determines where the auditing data is processed and the data is hosted.

### Considerations
{: #ha_dr_steps_res}

{{site.data.keyword.la_full_notm}} follows {{site.data.keyword.cloud_notm}} requirements for [planning and recovering from disaster events](/docs/overview?topic=overview-zero-downtime#disaster-recovery).
{: note}

When a regional disaster occurs, consider the following information:
* Data and the auditing metadata such as dashboards, alerts, views, screens, templates are backed up every 24 hours. In the event of an un-recoverable disaster, up to 24 hours of data and metadata changes to the auditing instance in the failure region can be lost.
* The estimated recovery time for rebuilding the regional site and restoring the service at another location is 24 hours.
* Due to the large volume of data, older data might not be available at the time the service is restored, as this process requires additional time to recover data from the backups.
* When the auditing instance in the DR region is available in the new location, you will be able to use it while the data is restored into the newly constructed region.
