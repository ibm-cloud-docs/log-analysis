---

copyright:
  years: 2018, 2021
lastupdated: "2021-03-28"

keywords: IBM Cloud, Log Analysis, logging, customer responsibilities, IBM responsibilities, terms and conditions

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Understanding your responsibilities when using {{site.data.keyword.la_full_notm}}
{: #shared-responsibilities}

Learn about the management responsibilities and terms and conditions that you have when you use {{site.data.keyword.la_full}}. For a high-level view of the service types in {{site.data.keyword.cloud_notm}} and the breakdown of responsibilities between the customer and {{site.data.keyword.IBM_notm}} for each type, see [Shared responsibilities for {{site.data.keyword.cloud_notm}} offerings](/docs/overview?topic=overview-shared-responsibilities).
{: shortdesc}

Review the following sections for the specific responsibilities for you and for {{site.data.keyword.IBM_notm}} when you use {{site.data.keyword.la_full_notm}}. For the overall terms of use, see [{{site.data.keyword.cloud_notm}} Terms and Notices](/docs/overview/terms-of-use?topic=overview-terms).

  
## Incident and operations management
{: #incident-and-ops}


| Task              | {{site.data.keyword.IBM_notm}} Responsibilities | Your Responsibilities |
|-------------------|-------------------------------------------------|-----------------------|
| `Incident and operations management` | Maintain {{site.data.keyword.la_full_notm}} service instances and infrastructure workloads. | Maintain incident and operations management of your data. |
| `Monitor incidents`  | Provide notifications for planned maintenance, security bulletins, or unplanned outages. | Set preferences to [receive emails about platform notifications](/docs/overview?topic=overview-ui#email-prefsl).  \n Monitor the [IBM Cloud status page](https://{DomainName}/status?selected=announcement) for general announcements. |
| `Maintain {{site.data.keyword.cloud_notm}} high availability SLA`  | Provide Cloud Service across availability zones in a Multi-Zone Region (MZR).  \n  Provide Cloud Service across hosts in a Single-Zone Region (SZR).  \n Provides replication, fail-over features, and infrastructure maintenance and updates. | Use the [list of available regions](/docs/log-analysis?topic=log-analysis-regions) to plan for and create new instances of the service. |
| `Monitor platform logs`  | [Participating Cloud services](/docs/log-analysis?topic=log-analysis-cloud_services) publish relevant log data to their subscribing clients. {{site.data.keyword.la_full_notm}} provides clients with the ability to receive the logs once the client configures their instance. | [Create an {{site.data.keyword.la_full_notm}} instance](/docs/log-analysis?topic=log-analysis-provision) in each region where Cloud service subscriptions publish logs.  \n [Configure 1 instance in each of those regions to received the published logs](/docs/log-analysis?topic=log-analysis-config_svc_logs). |
| `Monitor logs collected by logging agents`   | Provide images and instructions for how to install logging agents in environments that you want to monitor, such as Kubernetes, Linux, Openshift. | [Install and configure logging agents](/docs/log-analysis?topic=log-analysis-config_agent_kube_cluster).  \n Monitor that the agents are running in your environment. |
| `Archive logs`  | Provide the ablity to archive to a client configured Cloud Object Storage (COS) location and archive data hourly or daily. | [Configure Cloud Object Storage per your requirements.](/docs/log-analysis?topic=log-analysis-archiving#archiving_step3)  \n [Enable archiving of the logging instance.](/docs/log-analysis?topic=log-analysis-archiving) |
{: caption="Table 1. Responsibilities for incident and operations" caption-side="top"}


		


## Change management
{: #change-management}


| Task                                                    | {{site.data.keyword.IBM_notm}} Responsibilities | Your Responsibilities |
|---------------------------------------------------------|-----------------------|--------|
| `Update the {{site.data.keyword.la_full_notm}} service` | Provide major, minor, and patch version updates for {{site.data.keyword.la_full_notm}} interfaces.  \n Document changes in the [logging release notes](https://logdna.zendesk.com/hc/en-us/categories/360001626492-Release-Notes.htm){: external} | Ensure that any logging agents that you have deployed are kept current. |
| `Track versions of custom views, dashboards, screens, parsing templates, and alerts`    | `N/A` | Use your own change management process to control versions of logging resources such as views, dashboards, screens, parsing templates, and alerts`.  \n To learn how to export metadata, see [Export the configuration of resources in a logging instance](/docs/log-analysis?topic=log-analysis-reuse_resource_definitions#export_config_res).| 
{: caption="Table 2. Responsibilities for change management" caption-side="top"}


## Identity and access management
{: #iam-responsibilities}


| Task                           | {{site.data.keyword.IBM_notm}} Responsibilities | Your Responsibilities |
|--------------------------------|-------------------------------------------------|-----------------------|
| `Manage permissions`           | Provide the ability to restrict access to resouces.  \n {{site.data.keyword.IBM_notm}} is responsible for the security and compliance of {{site.data.keyword.la_full_notm}}. | Restrict access to resources by using Cloud IAM access policies by defining IAM policies to control which users within your account have access to the logging data.  \n [Learn more about controlling access through IAM](/docs/log-analysis?topic=log-analysis-work_iam)
. | 
{: caption="Table 3. Responsibilities for identity and access management" caption-side="top"}





## Security and regulation compliance
{: #security-compliance}


| Task                                       | {{site.data.keyword.IBM_notm}} Responsibilities | Your Responsibilities |
|--------------------------------------------|-------------------------------------------------|-----------------------|
| `Encrypt data`  | Operate the Cloud Service encrypting data in motion and at rest per compliance specifications. | Ensure encryption of archived data by configuring a COS bucket that has full control over the data encryption keys that are used. [{{site.data.keyword.cos_full}} provides several options to encrypt your data.](/docs/cloud-object-storage?topic=cloud-object-storage-encryption) |
| `Meet security and compliance objectives`  | Maintain controls that are commensurate to various industry compliance standards such as SOC2, PCI, HIPAA and Privacy Shield. | Set up and maintain security and regulation compliance for your apps and data.  This includes:  \n [Defining the account management strategy](/docs/log-analysis?topic=log-analysis-adoption#adoption_account)  \n [Configuring the accounts settings for compliance](/docs/log-analysis?topic=log-analysis-adoption#adoption_acc_settings)  \n Define IAM Strategy  \n [Define the notification strategy](/docs/log-analysis?topic=log-analysis-adoption#adoption_alerts) |
{: caption="Table 4. Responsibilities for security and regulation compliance" caption-side="top"}


## Disaster recovery
{: #disaster-recovery}


| Task                                                            | {{site.data.keyword.IBM_notm}} Responsibilities | Your Responsibilities |
|-----------------------------------------------------------------|-------------------------------------------------|-----------------------|
| `Restore the service` `[*]`      |Automatically recover and restart service components after any disaster event.  | `N/A` |
| `Backup the {{site.data.keyword.la_full_notm}} key resources that are provided by the service`        | Daily backup of the {{site.data.keyword.la_full_notm}} infrastructure and components. | `N/A` |
| `Backup logging agents`                                          | `N/A`  | Backup each logging agent YAML file that is deployed in your organization. |
| `Recovery of logging agents`                                     | `N/A` | [Reinstall](/docs/log-analysis?topic=log-analysis-logdna_agent#logdna_agent_configure) the logging agent in the event of any disaster event that impacts the agent runtime. |
| `Backup the metadata of a logging instance`                          | Backup metadata that is used by the service.  | [Backup the metadata such as views, dashboards, screens, parsing templates, and alerts for each logging instance.](/docs/log-analysis?topic=log-analysis-reuse_resource_definitions#export_config_res) |
| `Restore the metadata of a logging instance`                         | Restore metadata that is used by the service. | [Restore the metadata such as views, dashboards, screens, parsing templates, and alerts for each logging instance.](/docs/log-analysis?topic=log-analysis-reuse_resource_definitions#import_config) |
| `Backup of the data` | `N/A` | [Configure archiving to retain a backup copy of the data.](/docs/log-analysis?topic=log-analysis-archiving) |
{: caption="Table 5. Responsibilities for disaster recovery" caption-side="top"}


`[*]` Recovered and restarted service components will not have customer data reloaded.
{: note}


