---

copyright:
  years:  2018, 2019
lastupdated: "2019-11-15"

keywords: LogDNA, IBM, Log Analysis, logging, config agent

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


# Adoption guidelines for regulated and highly available workloads
{: #adoption}

In {{site.data.keyword.la_full_notm}}, 
{:shortdesc}



## 1. Define your account settings
{: #adoption_acc_settings}

Across every industry, organizations require tighter controls and visibility into where their data is stored and processed in the {{site.data.keyword.cloud}}. 

**Enable your {{site.data.keyword.cloud_notm}} account to be EU supported and HIPAA supported.**
{: important}

Notice that only the account owner can enable the account to be EU supported and HIPAA supported. 

You might choose to enable the EU Supported setting, for example, if you use resources to process personal data for European citizens. For more information, see [Set on the EU-Supported flag in your account](/docs/account?topic=account-eu-hipaa-supported#bill_eusupported).

You might choose to enable the HIPAA Supported setting if you plan to include Protected Health Information (PHI) in HIPAA-enabled services. For more information, see [Set on the HIPAA flag in your account](/docs/account?topic=account-eu-hipaa-supported#enabling-hipaa).


## 2. Define the service strategy 
{: #adoption_resource}

{{site.data.keyword.la_full_notm}} collects and aggregates logs in one centralized logging system.
* Log data is hosted on the {{site.data.keyword.cloud_notm}}. The {{site.data.keyword.la_full_notm}} service is operated by LogDNA.
* Data is collocated in the location where an {{site.data.keyword.la_full_notm}} instance is provisioned. 


### Locations
{: #adoption_resource_location}

You can provision {{site.data.keyword.la_full_notm}} instances in different {{site.data.keyword.cloud_notm}} locations. 
* Each location represents the geographic area where your {{site.data.keyword.la_full_notm}} requests are handled and processed for that instance, and where data is resident. 
* Each MZR location has three different data centers for redundancy. The data for each location is kept in the three data centers near that location. If all three data centers in a location fail, the {{site.data.keyword.la_full_notm}} service for that location becomes unavailable.

**When you choose the locations where you plan to provision {{site.data.keyword.la_full_notm}} instances, check the regulatory and high availability (HA) specifications of each location. For more information, see [Locations](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-regions).**
{: note}

For example, in Europe, only the Frankfurt region is EU-supported.

You can also check [ensure zero downtime](/docs/overview?topic=overview-zero-downtime#zero-downtime) to learn more about the high availability and disaster recovery standards in {{site.data.keyword.cloud_notm}}. 


### Resource groups

Resource groups are a logical container for organizing your IAM-enabled resources.
* IAM-enabled services belong to a resource group. The {{site.data.keyword.la_full_notm}} service is an IAM-enabled service.
* You assign a resource to its resource group when you create it from the catalog. 
* You can't change the resource group assignment after you set it, which is why it's important to plan and set up your resource groups.

**Use resource groups to organize your {{site.data.keyword.la_full_notm}} instances for access control and billing purposes.**
{: note}

Account owners can add resources to any resource group. Other users must be granted access by using an IAM access policy to add resources to resource groups. 

For more information, see [Best practices for organizing resources in a resource group](/docs/resources?topic=resources-bp_resourcegroups).



### Tags
{: #tags}

A tag is a label that you assign to a resource for easy filtering of resources in your resource list. 
* You can use tags to organize your resources and easily find them later. 
* You can also use tags to help you with identifying specific team usage or cost allocation when you view your [exported usage report](/docs/billing-usage?topic=billing-usage-viewingusage#export-csv).

**Use tags to organize your resources and track usage costs.**
{: note}

Tags are case-sensitive, and the maximum length of a tag is 128 characters. 
* The characters that are permitted to name tags are A-Z, 0-9, spaces, underscore, hyphen, period, and colon. 
* Colons turn the tag into a string where you can isolate two logical parts, like a `key:value` pair. You can't use a colon in a tag without creating this pairing. 
* A comma separates tags and can't be used within the tag name itself.

**When you define your tags, do not store information in tags that might disclose sensitive information to others in the same account.**
{: note}

Tags are visible to all members of an account. 

**To control tag visibility, circulate tagging guidelines, and let users know that tags are visible account-wide.**
{: note}



## 3. Define the IAM strategy
{: #adoption_iam}

**Use {{site.data.keyword.iamlong}} (IAM) to securely authenticate users and service IDs, and to control access to all cloud resources and data consistently in the {{site.data.keyword.cloud_notm}}.**
{: important}



### Access groups
{: #adoption_iam_access_groups}

You can assign permissions to work with the {{site.data.keyword.la_full_notm}} service within the context of the service, a resource group, or an access group. 

**Use access groups to organize a set of users and service IDs into a single entity that makes it easy for you to manage IAM permissions.**
{: note}

You can create multiple access groups.

Define a minimum of 4 access groups:

| Access group             | Description |
|--------------------------|-------------|
| `Administrators`         | Users in this group should have permissions to fully manage the service and grant other users in the account permisisons to work with the service in the {{site.data.keyword.cloud_notm}}. |
| `Managers`               | Users in this group should have permissions to fully manage the service in the {{site.data.keyword.cloud_notm}}. |
| `Advanced service users` | Users in this group should have permissions to run advanced tasks.  |
| `Users`                  | Users in this group should have permissions to run basic tasks.  |
{: caption="Table 1. List of access groups" caption-side="top"} 

### Policies
{: #adoption_iam_policies}

A policy determines the full set of actions that a user or service ID can perform. 

**For each access group, define a policy for each resource group that defines the level of access to that resource group.** 
{: note}

By default, the account owner is the only user in the account that can grant permissions to other users to manage and work with the {{site.data.keyword.la_full_notm}} service. 

**To allow other users or service IDs in the account to manage the service and be able to grant permisisons to work with the {{site.data.keyword.la_full_notm}} service, define a policy for the {{site.data.keyword.la_full_notm}} service with the platform role **administrator**. Grant this policy to the administrators access group.** 
{: note}

For more information, see [Granting permissions to a user to become an administrator of the service](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account).

Access to resources within a resource group can be granted to all resources in a group, or only selected services within a group. 

Access policies set a target, which is typically a service instance or all instances of a service in a resource group, and a role, which defines what type of access is allowed.

Roles define the actions that a user or serviceID can run. There are different types of roles in the {{site.data.keyword.cloud_notm}}:
* *Platform management roles* define permissions to work with the service at the platform level, for example, some actions are assign user access for the service, create or delete service IDs, create instances, assign policies for your service to other users, and bind instances to applications. [Learn more](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#platform).
* *Service access roles* define permissions for calling the service's API. [Learn more](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#service).

**For each access group, define a policy for each resource group that specifies the permissions granted to work with the resource group, the permissions to manage instances of the {{site.data.keyword.la_full_notm}} service in that resource group, and the permissions to run {{site.data.keyword.la_full_notm}} tasks.**
{: note}

| Access group             | Policy         |
|--------------------------|----------------|
| `Administrators`         | Grant a policy for the resource group with resource group access **administrator**. Select the {{site.data.keyword.la_full_notm}} service, and select the platform role **administrator**, and the service role **manager**. |
| `Managers`               | Grant a policy for the resource group with platform role **editor**. Select the {{site.data.keyword.la_full_notm}} service, and select the platform role **editor**, and the service role **manager**. |
| `Advanced service users` | Grant a policy for the resource group with platform role **viewer**. Select the {{site.data.keyword.la_full_notm}} service, and select the platform role **viewer**, and the service role **standard member**. |
| `Users`                  | Grant a policy for the resource group with platform role **viewer**. Select the {{site.data.keyword.la_full_notm}} service, and select the platform role **viewer**, and the service role **reader**. |
{: caption="Table 2. Roles per access group policy" caption-side="top"} 

**Every user that requires permissions to work with the {{site.data.keyword.la_full_notm}} service in your account must be assigned a resource group policy that inclides the permissions for the {{site.data.keyword.la_full_notm}} service.**
{: note}

You can assign a single policy to the access group instead of assigning the same access multiple times per individual user or service ID. 

**Add users and service IDs to an access group. Grant permissions to these users and service IDs through the access group.**
{: note}

[Learn more](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam).


## 4. Define the notification strategy 
{: #adoption_alerts}

HIPAA
PCI

Notify in the event of an exception 

Setup absence alerting

Follow these steps:
Setup alert
Configure it for absence alerting

bsence alerting tests for the absence of data flowing into your service instance.  If data is not flowing into the system it may indicate an issue in the application or environment.  Absence duration is unique to workload and can be customized within the UI.



## 5. Define the archive strategy





Disaster Recovy

Follow these steps.

Archive, when sent to the properly configured COS account may provide your application or environment the necessary backup of data.  


LogDNA as a service does not store an independent backup copy of your data. 


When LogDNA is setup to archive to IBM COS, setup archive to a COS bucket which does not have preconfigured retention policies.



### Cloud Object Storage 

HIPAA
PCI
Business Continuity
Disaster Recovery


Services that are hosted globally create resources that operate across multiple locations. For example, with IBM Cloud Object Storage, you can choose to deploy data in a single data center, or even a combination of locations by selecting the endpoint where your application sends REST API requests.


Review and identify the right COS configuration for your business needs.  Set this up to prepare for service archive.


LogDNA can archive to a client configured COS bucket.  There are many COS configurations helping clients meet a variety of needs.  Data may need to be replicated across Regions to meet business and regulated requirements.  Alternatively data may need to be restricted to certain locations to meet data locality requirements.  Learn more about COS configurations here.


## Network strategy

 VRF