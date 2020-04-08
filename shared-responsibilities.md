---

copyright:
  years: 2018, 2020
lastupdated: "2020-03-25"

keywords: LogDNA, IBM Cloud, Log Analysis, logging, customer responsibilities, IBM responsibilities, terms and conditions

subcollection: LogDNA

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:codeblock: .codeblock}
{:tip: .tip}
{:note: .note}
{:important: .important}
{:deprecated: .deprecated}
{:download: .download}
{:preview: .preview}

# Understanding your responsibilities when using {{site.data.keyword.la_full_notm}}
{: #shared-responsibilities}

Learn about the management responsibilities and terms and conditions that you have when you use {{site.data.keyword.la_full}}. For a high-level view of the service types in {{site.data.keyword.cloud_notm}} and the breakdown of responsibilities between the customer and {{site.data.keyword.IBM_notm}} for each type, see [Shared responsibilities for {{site.data.keyword.cloud_notm}} offerings](/docs/overview?topic=overview-shared-responsibilities).
{:shortdesc}

Review the following sections for the specific responsibilities for you and for {{site.data.keyword.IBM_notm}} when you use {{site.data.keyword.la_full_notm}}. For the overall terms of use, see [{{site.data.keyword.cloud_notm}} Terms and Notices](/docs/overview/terms-of-use?topic=overview-terms).

  
## Incident and operations management
{: #incident-and-ops}

You and {{site.data.keyword.IBM_notm}} share responsibilities for the set up and maintenance of your {{site.data.keyword.la_full_notm}} service instance and infrastructure workloads. You are responsible for incident and operations management of your data.
{: note}

| Task              | {{site.data.keyword.IBM_notm}} Responsibilities | Your Responsibilities |
|-------------------|-------------------------------------------------|-----------------------|
| `Monitor incidents`  | Provide notifications for planned maintenance, security bulletins, or unplanned outages. | Set preferences to [receive emails about platform notifications](/docs/overview?topic=overview-ui#email-prefsl). </br>Monitor the [IBM Cloud status page](https://{DomainName}/status?selected=announcement) for general announcements. |
| `Availability`  | Provide Cloud Service across availability zones in a Multi-Zone Region (MZR). </br> Provide Cloud Service across hosts in a Single-Zone Region (SZR). </br>Provides replication, fail-over features, and infrastructure maintenance and updates. | Use the list of available regions to plan for and create new instances of the service. |
| `Monitoring platform logs`  | Participating Cloud services publish relevant log data to their subscribing clients. {{site.data.keyword.la_full_notm}} provides clients with the ability to receive the logs once the client configures their instance. | Create an {{site.data.keyword.la_full_notm}} instance in each region where Cloud service subscriptions publish logs. </br>Configure 1 instance in each of those regions to received the published events. |
| `Monitor logs collected by LogDNA agents`   | Provide images and instructions for how to install LogDNA agents in environments that you want to monitor, such as Kubernetes, Linux, Openshift. | Install and configure LogDNA agents. </br>Monitor that the agents are running in your environment. |
| `Archive logs`  | Provide the ablity to archive to a client configured Cloud Object Storage (COS) location and archive data hourly or daily. | Configure Cloud Object Storage per your requirements. </br>Enable archiving of the logging instance. |
{: caption="Table 1. Responsibilities for incident and operations" caption-side="top"}


		


## Change management
{: #change-management}

You and {{site.data.keyword.IBM_notm}} share responsibilities for keeping {{site.data.keyword.la_full_notm}} service components at the latest version. You are responsible for change management of your LogDNA agents, dashboards, screens, views, and alert definitions.
{: note}

| Task                                                    | {{site.data.keyword.IBM_notm}} Responsibilities | Your Responsibilities |
|---------------------------------------------------------|-----------------------|--------|
| `Application` | Provide major, minor, and patch version updates for {{site.data.keyword.la_full_notm}} interfaces. </br>Document changes in the [LogDNA release notes](https://logdna.zendesk.com/hc/en-us/categories/360001626492-Release-Notes) | Ensure that any LogDNA agents that you have deployed are kept current. |
{: caption="Table 2. Responsibilities for change management" caption-side="top"}


## Identity and access management
{: #iam-responsibilities}

{{site.data.keyword.IBM_notm}} is responsible for the security and compliance of {{site.data.keyword.la_full_notm}}. You are responsible for defining the {{site.data.keyword.cloud_notm}} Identity and Access Management (IAM) policies to control which users within your account have access to the logging data.
{: note}

| Task                           | {{site.data.keyword.IBM_notm}} Responsibilities | Your Responsibilities |
|--------------------------------|-------------------------------------------------|-----------------------|
| `Applications`  | Provide the ability to restrict access to resouces. | Depending on your needs, restrict access to resources by using Cloud IAM access policies and access settings within the LogDNA UI interface. | 
{: caption="Table 3. Responsibilities for identity and access management" caption-side="top"}

[Learn more about controlling access through IAM](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-iam).




## Security and regulation compliance
{: #security-compliance}

{{site.data.keyword.IBM_notm}} is responsible for the security and compliance of {{site.data.keyword.la_full_notm}}. You are responsible for ensuring that logs, that contain regulated data, are not provided to the {{site.data.keyword.la_full_notm}} service.
{: note}

| Task                                       | {{site.data.keyword.IBM_notm}} Responsibilities | Your Responsibilities |
|--------------------------------------------|-------------------------------------------------|-----------------------|
| `Encryption`  | Operate the Cloud Service encrypting data in motion and at rest per compliance specifications. | Ensure encryption of archived data. |
| `Applications` | Maintain controls that are commensurate to various industry compliance standards such as SOC2, PCI, HIPAA and Privacy Shield. | Set up and maintain security and regulation compliance for your apps and data.  This includes: </br>Defining the account management strategy </br>Configuring the accounts settings for compliance </br>Define IAM Strategy </br>Define the notification strategy |
{: caption="Table 4. Responsibilities for security and regulation compliance" caption-side="top"}


## Disaster recovery
{: #disaster-recovery}

{{site.data.keyword.IBM_notm}} is responsible for the recovery of {{site.data.keyword.la_full_notm}} components in case of disaster. You are responsible for the recovery of the LogDNA agents running in your environment should they be impacted by a disaster, and the resources to manage data like views, dashboards, screens, parsing templates, and alerts`.
{: note}

| Task                                                            | {{site.data.keyword.IBM_notm}} Responsibilities | Your Responsibilities |
|-----------------------------------------------------------------|-------------------------------------------------|-----------------------|
| `Applications` |Automatically recover and restart service components after any disaster event. | Enable archiving and check archive data is valid. |
{: caption="Table 5. Responsibilities for disaster recovery" caption-side="top"}




