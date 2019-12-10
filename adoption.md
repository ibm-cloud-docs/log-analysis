---

copyright:
  years:  2018, 2019
lastupdated: "2019-12-06"

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

For regulated and highly available workloads, consider the following adoption guidelines when using the {{site.data.keyword.la_full_notm}} service:
{:shortdesc}


## 1. Define naming stardards for compliance
{: #adoption_acc_settings}

When you create resources in the {{site.data.keyword.cloud_notm}}, you can choose how to name them. 

Define naming standards that do not include PII information across all resources that are created in the {{site.data.keyword.cloud_notm}}.
{: important}

## 2. Configure the account settings for compliance
{: #adoption_acc_settings}

Across every industry, organizations require tighter controls and visibility into where their data is stored and processed. 

**Indicate to {{site.data.keyword.IBM_notm}} your compliance requirements by enabling your {{site.data.keyword.cloud_notm}} account as HIPAA or EU supported.**
{: important}

In the {{site.data.keyword.cloud}}, you can configure your account for EU support and for HIPAA support:
* You might choose to enable the **EU Supported** setting, for example, if you use resources to process personal data for European citizens. For more information, see [Set on the EU-Supported flag in your account](/docs/account?topic=account-eu-hipaa-supported#bill_eusupported).
* You might choose to enable the **HIPAA** Supported setting if you plan to include Protected Health Information (PHI) in HIPAA-enabled services. For more information, see [Set on the HIPAA flag in your account](/docs/account?topic=account-eu-hipaa-supported#enabling-hipaa).

Notice that only the account owner can enable the account to be EU supported and HIPAA supported. 

### HIPAA
{: #adoption_acc_settings_hipaa}

If you're the account owner, you can enable your {{site.data.keyword.cloud}} account to be HIPAA supported. For example, you might choose to enable the **HIPAA Supported setting** if you plan to include Protected Health Information (PHI) in HIPAA-enabled services.

The US Health Insurance Portability and Accountability Act (HIPAA) and the Health Information Technology for Economic and Clinical Health (HITECH) Act define standards for handling electronic healthcare transactions and information. If you or your company is a covered entity as defined by HIPAA, you must enable the HIPAA Supported setting if you run sensitive workloads that are regulated under HIPAA and the HITECH Act. Learn more about {{site.data.keyword.cloud_notm}} compliance in [Compliance on the {{site.data.keyword.cloud_notm}}](https://www.ibm.com/cloud/compliance){: new_window} ![External link icon](../icons/launch-glyph.svg "External link icon").
{: tip}

When you configure your account to be HIPAA enabled, consider the following information:
* You can filter on *HIPAA Enabled* services in the catalog. Accounts that enable the **HIPAA Supported setting** still have access to the full catalog of services. 
* You indicate to {{site.data.keyword.IBM_notm}} that your account stores protected health information (PHI).
* You digitally accept the IBM Business Associate Addendum (BAA) for covered entities.

Enable this setting only if you or your company is a covered entity as defined by HIPAA. If you or your company is a business associate of a covered entity, [contact {{site.data.keyword.cloud_notm}} Sales](https://www.ibm.com/account/reg/us-en/signup?formid=MAIL-wcp){: new_window} ![External link icon](../icons/launch-glyph.svg "External link icon") to accept the applicable BAA. For more information about HIPAA definitions of covered entities and business associates, see the [US Department of Health & Human Services](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html){: new_window} ![External link icon](../icons/launch-glyph.svg "External link icon") website.
{: important}

In addition, for logging instances that you provision in a HIPAA enabled account, LogDNA requires that you **accept a Business Associate Addendum (BAA) with LogDNA** prior to having access to this plan. Contact {{site.data.keyword.IBM_notm}} and [open a support ticket](/docs/get-support?topic=get-support-getting-customer-support#getting-customer-support).
{: important}


## 3. Define the service strategy 
{: #adoption_resource_svc}

{{site.data.keyword.la_full_notm}} collects and aggregates logs in one centralized logging system.
* Log data is hosted on the {{site.data.keyword.cloud_notm}}. The {{site.data.keyword.la_full_notm}} service is operated by LogDNA.
* Data is collocated in the location where an {{site.data.keyword.la_full_notm}} instance is provisioned. 


### Locations
{: #adoption_resource_svc_location}

You can provision {{site.data.keyword.la_full_notm}} instances in different {{site.data.keyword.cloud_notm}} locations. 
* Each location represents the geographic area where your {{site.data.keyword.la_full_notm}} requests are handled and processed for that instance, and where data is resident. 
* Each MZR location has three different data centers for redundancy. The data for each location is kept in the three data centers near that location. If all three data centers in a location fail, the {{site.data.keyword.la_full_notm}} service for that location becomes unavailable.
* Each MZR configuration can accept a single data center failure.

**When you choose the locations where you plan to provision {{site.data.keyword.la_full_notm}} instances, check the regulatory and high availability (HA) specifications of each location. For more information, see [Locations](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-regions).**
{: tip}

For example, in Europe, only the Frankfurt region is EU-supported.

You can also check [ensure zero downtime](/docs/overview?topic=overview-zero-downtime#zero-downtime) to learn more about the high availability and disaster recovery standards in {{site.data.keyword.cloud_notm}}. 


### Resource groups
{: #adoption_resource_svc_rg}

Resource groups are a logical container for organizing your IAM-enabled resources.
* IAM-enabled services belong to a resource group. The {{site.data.keyword.la_full_notm}} service is an IAM-enabled service.
* You assign a resource to its resource group when you create it from the catalog. 
* You can't change the resource group assignment after you set it, which is why it's important to plan and set up your resource groups.

**Use resource groups to organize your {{site.data.keyword.la_full_notm}} instances for access control and billing purposes.**
{: tip}

Account owners can add resources to any resource group. Other users must be granted access by using an IAM access policy to add resources to resource groups. 

For more information, see [Best practices for organizing resources in a resource group](/docs/resources?topic=resources-bp_resourcegroups).

If you add PII information in the resource group name, you might be disclosing sensitive data to others in the same account.

**When you define your resource groups, do not add sensitive information in the tag name.**
{: tip}

### Naming
{: #adoption_resource_svc_name}

If you add PII information in the name or the description of a service, you might be disclosing sensitive data to others in the same account.

**When you define your service name, do not add sensitive information in the name or in the description.**
{: tip}

### Service plan
{: #adoption_resource_svc_plan}

The service plan that you choose for a LogDNA instance determines the number of days that data is available for search. For more information, see [Service plans](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-service_plans).

**Choose your plan based on the number of days that you need to be able to search data online through the web UI.**
{: tip}

The HIPAA plan has a maximum of 25 users. If you need to grant permissions to more than 25 users, [open a support ticket](/docs/get-support?topic=get-support-getting-customer-support#getting-customer-support).


### Tags
{: #adoption_resource_svc_tags}

A tag is a label that you assign to a resource for easy filtering of resources in your resource list. 
* You can use tags to organize your resources and easily find them later. 
* You can also use tags to help you with identifying specific team usage or cost allocation when you view your [exported usage report](/docs/billing-usage?topic=billing-usage-viewingusage#export-csv).

**Use tags to organize your resources and track usage costs.**
{: tip}

Tags are case-sensitive, and the maximum length of a tag is 128 characters. 
* The characters that are permitted to name tags are A-Z, 0-9, spaces, underscore, hyphen, period, and colon. 
* Colons turn the tag into a string where you can isolate two logical parts, like a `key:value` pair. You can't use a colon in a tag without creating this pairing. 
* A comma separates tags and can't be used within the tag name itself.

If you add PII information in the name, you might be disclosing sensitive data to others in the same account.

**When you define your tags, do not add sensitive information in the tag name.**
{: tip}

Tags are visible to all members of an account. 

**To control tag visibility, circulate tagging guidelines, and let users know that tags are visible account-wide.**
{: tip}



## 4. Define the IAM strategy
{: #adoption_iam}

**Use {{site.data.keyword.iamlong}} (IAM) to securely authenticate users and service IDs, and to control access to all cloud resources and data consistently in the {{site.data.keyword.cloud_notm}}.**
{: important}

If you add PII information in the name or description of IAM resources, you might be disclosing sensitive data to others in the same account.

**When you define your IAM reosurces, do not add sensitive information in the tag name.**
{: tip}


### Access groups
{: #adoption_iam_access_groups}

You can assign permissions to work with the {{site.data.keyword.la_full_notm}} service within the context of the service, a resource group, or an access group. 

**Use access groups to organize a set of users and service IDs into a single entity that makes it easy for you to manage IAM permissions.**
{: tip}

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
{: tip}

By default, the account owner is the only user in the account that can grant permissions to other users to manage and work with the {{site.data.keyword.la_full_notm}} service. 

**To allow other users or service IDs in the account to manage the service and be able to grant permisisons to work with the {{site.data.keyword.la_full_notm}} service, define a policy for the {{site.data.keyword.la_full_notm}} service with the platform role **administrator**. Grant this policy to the administrators access group.** 
{: tip}

For more information, see [Granting permissions to a user to become an administrator of the service](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account).

Access to resources within a resource group can be granted to all resources in a group, or only selected services within a group. 

Access policies set a target, which is typically a service instance or all instances of a service in a resource group, and a role, which defines what type of access is allowed.

Roles define the actions that a user or serviceID can run. There are different types of roles in the {{site.data.keyword.cloud_notm}}:
* *Platform management roles* define permissions to work with the service at the platform level, for example, some actions are assign user access for the service, create or delete service IDs, create instances, assign policies for your service to other users, and bind instances to applications. [Learn more](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#platform).
* *Service access roles* define permissions for calling the service's API. [Learn more](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#service).

**For each access group, define a policy for each resource group that specifies the permissions granted to work with the resource group, the permissions to manage instances of the {{site.data.keyword.la_full_notm}} service in that resource group, and the permissions to run {{site.data.keyword.la_full_notm}} tasks.**
{: tip}

| Access group             | Policy         |
|--------------------------|----------------|
| `Administrators`         | Grant a policy for the resource group with resource group access **administrator**. Select the {{site.data.keyword.la_full_notm}} service, and select the platform role **administrator**, and the service role **manager**. |
| `Managers`               | Grant a policy for the resource group with platform role **editor**. Select the {{site.data.keyword.la_full_notm}} service, and select the platform role **editor**, and the service role **manager**. |
| `Advanced service users` | Grant a policy for the resource group with platform role **viewer**. Select the {{site.data.keyword.la_full_notm}} service, and select the platform role **viewer**, and the service role **standard member**. |
| `Users`                  | Grant a policy for the resource group with platform role **viewer**. Select the {{site.data.keyword.la_full_notm}} service, and select the platform role **viewer**, and the service role **reader**. |
{: caption="Table 2. Roles per access group policy" caption-side="top"} 

**Every user that requires permissions to work with the {{site.data.keyword.la_full_notm}} service in your account must be assigned a resource group policy that includes the permissions for the {{site.data.keyword.la_full_notm}} service.**
{: tip}

You can assign a single policy to the access group instead of assigning the same access multiple times per individual user or service ID. 

**Add users and service IDs to an access group. Grant permissions to these users and service IDs through the access group.**
{: tip}

[Learn more](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam).


## 5. Configure the account settings for authentication into your account
{: #adoption_login}

Multifactor authentication (MFA) adds an extra layer of security to your account by requiring all users to authenticate by using an additional authentication method beyond an ID and password. This is also commonly known as two-factor authentication (2FA). 

The {{site.data.keyword.cloud_notm}} account owner or administrator for the billing service can choose to require multifactor authentication (MFA) for every user in the account or just users with non-federated IDs who do not use SSO. All users with an IBMid use a time-based one-time passcode (TOTP) MFA method, and any users with a different type of ID must be enabled to use the time-based one-time passcode authentication (TOTP), security questions, or an external authentication method separately. [Learn more](/docs/iam?topic=iam-enablemfa).

You can also configure MFA options such as security questions, using a time-based one-time passcode, and using an external authentication method. These types of MFA options are specific per account and are available only with former classic infrastructure accounts.

**Enable multifactor authentication (MFA) in your {{site.data.keyword.cloud_notm}} account for all users.**
{: important}



## 6. Define the archive strategy
{: #adoption_archive}

You might have different requirements that require archiving your data:
* Backup requirements to keep data for a period of time
* Data access requirements so that you can query the data after it is not available for search through the web UI
* Disaster recovery requirements 
* Compliance requirements

LogDNA as a service does not backup your data. 

There are 2 types of data that you should consider archiving:
* Log data

    By default, archiving of log data is not enabled for any LogDNA instance. 

    When you enable archiving of your log data, notice that you are responsible for checking that your archived files are not corrupted, and for the maintenance of your archived files.
    {: note}

* Web UI resource definitions such as parsing templates, exclusion rules, views, and dashboards.

**Archive your LogDNA resource definitions and your log data.**
{: important}

### Backup the resource configurations of your LogDNA instance
{: #adoption_archive_ui}

In the LogDNA web UI, you can define custom views, dashboards, parsing templates, and exclusion rules that you can use to view and analyze data.

To reuse resource definitions that you define in your LogDNA instance, you can export these resources from {an {{site.data.keyword.la_full_notm}} instance as a JSON file. Then, you can import the definitions into other LogDNA instances. For example, you can reuse your LogDNA resources across different environments for your stage, pre-production, and production logging instances. [Learn more](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-reuse_resource_definitions).

**Backup LogDNA resource definitions into a version control system such as a git repository where you can control access to the archived files and manage versions.**
{: tip}

### Archive log data to a COS bucket
{: #adoption_archive_data}

**Enable archiving of your data from a LogDNA instance to {an {{site.data.keyword.cos_full_notm}} (COS) bucket.**
{: tip}

After you provision a LogDNA instance, you can configure archiving to an {{site.data.keyword.cos_full_notm}} (COS) bucket. You can create different types of buckets based on your requirements. 

When you plan the bucket for a LogDNA instance, consider the following information:

| Requirement                                            | Question to answer                                                | Information                                                                 |
|--------------------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `Type of workload` [^1]                                | How often do you need to access the data?                         | [Information about storage classes](/docs/services/cloud-object-storage?topic=cloud-object-storage-classes#classes-about) |
| `Retention policy` [^2]                                | Do you need to protect data from being deleted?                   | [Information about Immutable Object Storage](/docs/services/cloud-object-storage?topic=cloud-object-storage-immutable) |
| `Expiration policy` [^3]                               | Do you need automatic deletion of files?                          | [Information about expiration rules](/docs/services/cloud-object-storage?topic=cloud-object-storage-expiry) |                            
| `Long-term retention policy` [^4]                      | Do you need to keep data for a long period of time?               | [Information about archiving COS files for long term storage](/docs/services/cloud-object-storage?topic=cloud-object-storage-archive) |
| `Encryption of data at-rest with my own key` [^5]      | Can I use my own key to encrypt data at-rest?                     | [Information about encryption of data at-rest](/docs/services/cloud-object-storage?topic=cloud-object-storage-encryption) |
| `Data resiliency` [^6]                                 | Do you need to store the data in a specific geographical location? | [Information about resiliency](/docs/services/cloud-object-storage/basics?topic=cloud-object-storage-endpoints) |
{: caption="Table 3. COS bucket requirements" caption-side="top"} 

`[1]`: Data might sit untouched for long periods of time. For less active workloads, you can create buckets with different storage classes. For example, use the standard storage class for active workloads, where you need to access data at any time.

`[2]`: You can choose *Immutable Object Storage* to preserve electronic records and maintain data integrity. When you define a retention policy for a bucket, you are specifying that the data is stored in a WORM (Write-Once-Read-Many), non-erasable and non-rewritable manner. This policy is enforced until the end of a retention period and the removal of any legal holds. Notice that `Immutable Object Storage` is available in certain regions only.

`[3]`: You can use an expiration rule to delete objects automatically after a defined period from the object creation date. 

`[4]`: You can define a retention policy to retain data for a long period of time and have the data available for downloads and queries. If you do not need to query the data, and you just need to keep it for compliance, look into archiving COS files from any of the storage tiers to a long-term offline archive location or use the online *Cold Vault* option.

`[5]`: COS provides several options to encrypt your data. By default, all objects that are stored in COS are encrypted by using randomly generated keys and an all-or-nothing-transform (AONT). With COS, you can also manage your keys manually by providing your own encryption keys - referred to as Server-Side Encryption with Customer-Provided Keys (SSE-C). Alternatively, you can choose to use the integration capabilities with {{site.data.keyword.cloud}} Key Management Services like {{site.data.keyword.keymanagementservicelong}} and {{site.data.keyword.hscrypto}}. 

`[6]`: Resiliency refers to the scope and scale of the geographic area across which your data is distributed. For example, you can choose cross region resiliency to spread your data across several geographical areas, or regional resiliency to spread data across a single region. Notice that a single data center distributes data across devices within a single site only.


**Create a custom COS bucket with the storage features and the policies that you identify.** [Learn more](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-archiving).
{: tip}

**Do not configure a long-term retention policy on a COS bucket if you need access to the data and query it with the {{site.data.keyword.sqlquery_short}} service.**
{: tip}

Use the following table to help you identify the features that you should consider when you create a bucket:

| Requirement                                  | Storage class: `Standard`[^7]   | Storage class: `Vault`[^8]  | Storage class: `Cold Vault`[^9]  | Storage class: `Flex`[^10]  |
|----------------------------------------------|---------------------------------|-----------------------------|----------------------------------|-----------------------------|
| `Type of workload`                           | `Continuous access`             | `Data isn't accessed frequently` | `Accessed every 90 days or less` | `Dynamic workloads where access patterns are difficult to predict` |
| `Data resiliency`                            | `Cross region`                  | `Cross region`             | `Cross region`                  | `Cross region`             |
| `Retention policy`                           | ![Checkmark icon](../../icons/checkmark-icon.svg) | ![Checkmark icon](../../icons/checkmark-icon.svg) | ![Checkmark icon](../../icons/checkmark-icon.svg) | ![Checkmark icon](../../icons/checkmark-icon.svg) |
| `Expiration policy`                          | ![Checkmark icon](../../icons/checkmark-icon.svg) | ![Checkmark icon](../../icons/checkmark-icon.svg) | ![Checkmark icon](../../icons/checkmark-icon.svg) | ![Checkmark icon](../../icons/checkmark-icon.svg) |                         
| `Long-term retention policy`                 | `NO`                            | `NO`                        | `NO`                             | `NO`                         |
{: caption="Table 4. Disaster recovery or compliance requirements" caption-side="top"}
{: #archive-table-4}
{: tab-title="Disaster Recovery"}
{: tab-group="archive"}
{: class="simple-tab-table"}
{: row-headers}

| Requirement                                  | Storage class: `Standard`[^7]  | Storage class: `Vault`[^8] | Storage class: `Cold Vault`[^9] | Storage class: `Flex`[^10] |
|----------------------------------------------|---------------------------------|-----------------------------|----------------------------------|-----------------------------|
| `Type of workload`                           | `Continuous access`             | `Data isn't accessed frequently` | `Accessed every 90 days or less` | `Dynamic workloads where access patterns are difficult to predict` |
| `Data resiliency`                            | `Cross region` or `Regional`    | `Cross region` or `Regional`    | `Cross region` or `Regional`   | `Cross region` or `Regional`   |
| `Retention policy`                           | ![Checkmark icon](../../icons/checkmark-icon.svg) | ![Checkmark icon](../../icons/checkmark-icon.svg) | ![Checkmark icon](../../icons/checkmark-icon.svg) | ![Checkmark icon](../../icons/checkmark-icon.svg) |
| `Expiration policy`                          | ![Checkmark icon](../../icons/checkmark-icon.svg) | ![Checkmark icon](../../icons/checkmark-icon.svg) | ![Checkmark icon](../../icons/checkmark-icon.svg) | ![Checkmark icon](../../icons/checkmark-icon.svg) |                         
| `Long-term retention policy`                 | `NO`                            | `NO`                        | `NO`                             | `NO`                         |
{: caption="Table 5. Backup or access to data beyond the service plan days requirements" caption-side="top"}
{: #archive-table-5}
{: tab-title="Backup"}
{: tab-group="archive"}
{: class="simple-tab-table"}
{: row-headers}

`[7]`: Standard is used for active workloads. No charge incurs for data that is retrieved (other than the cost of the operational request itself and public outbound bandwidth).

`[8]`: Vault is used for cool workloads where data isn't accessed frequently, but a retrieval charge applies for reading data. The service includes a threshold for object size and storage period consistent with the intended use of this service for cooler, less-active data.

`[9]`: Cold Vault is used for cold workloads where data is primarily archived (accessed every 90 days or less) - a larger retrieval charge applies for reading data. The service includes a threshold for object size and storage period consistent with the intended use of this service: storing cold, inactive data.

`[10]`:  Flex is used for dynamic workloads where access patterns are more difficult to predict. Depending on usage, if the lower cost of cooler storage that is combined with retrieval charges exceeds a cap value, then the storage charge increases and no any retrieval charges apply. If the data isn't accessed frequently, Flex storage can be more cost effective than Standard storage. If cooler usage patterns become more active, Flex storage is more cost effective than Vault or Cold Vault storage. No threshold object size or storage period applies to Flex buckets.

Objects that are subject to a bucket's `Immutable Object Storage` retention policy will have expiration actions deferred until the retention policy is no longer enforced. 
{: tip}


### Encrypt data with your own key
{: #adoption_archive_1}

By default, all objects that are stored in COS are encrypted by using randomly generated keys and an all-or-nothing-transform (AONT). When you archive data into your COS instance, your objects are automatically encrypted with data encryption keys (DEKs). When you need to access a bucket, the service checks your user permissions and decrypts the objects within the bucket for you. This encryption model is called *provider-managed encryption*.

While this default encryption model provides at-rest security, some workloads need full control over the data encryption keys used. 

COS provides several options to encrypt your data. This encryption model is called *customer-managed encryption*:
* You can manage your keys manually by providing your own encryption keys - referred to as Server-Side Encryption with Customer-Provided Keys (SSE-C). 
* You can choose to use the integration capabilities with {{site.data.keyword.cloud}} Key Management Services like {{site.data.keyword.keymanagementservicelong}} and {{site.data.keyword.hscrypto}}. 

    You can use {{site.data.keyword.keymanagementservicelong}} to provision encrypted keys for apps across {{site.data.keyword.cloud_notm}} services. As you manage the lifecycle of your keys, you can benefit from knowing that your keys are secured by FIPS 140-2 Level 3 certified cloud-based hardware security modules (HSMs) that protect against the theft of information. When you integrate COS with the {{site.data.keyword.keymanagementserviceshort}} service, you can add envelope encryption to your DEKs. In {{site.data.keyword.keymanagementserviceshort}}, you can provision highly secure root keys, which serve as a master keys that you control in the service. When you create a bucket, you can configure envelope encryption for the bucket at its creation. This added protection wraps (or encrypts) the DEKs associated with the bucket by using a root key that you manage in {{site.data.keyword.keymanagementserviceshort}}. The practice, called *key wrapping*, uses multiple AES algorithms to protect the privacy and the integrity of your DEKs, so only you control access to their associated data.

    Hyper Protect Crypto Services is a single-tenant, dedicated HSM that is controlled by you. The service is built on FIPS 140-2 Level 4-certified hardware, the highest offered by any cloud provider in the industry.


If you need to use your own key to encrypt the data at-rest in a bucket, use the following table to help you identify the features that you should consider when you create a bucket:

| Requirement                                  | Storage class: `Standard`       | Storage class: `Vault`      | Storage class: `Cold Vault`      | Storage class: `Flex`       |
|----------------------------------------------|---------------------------------|-----------------------------|----------------------------------|-----------------------------|
| `Type of workload`                           | `Continuous access`             | `Data isn't accessed frequently` | `Accessed every 90 days or less` | `Dynamic workloads where access patterns are difficult to predict` |
| `Data resiliency`                            | `Regional`                      | `Regional`                   | `Regional`                      | `Regional`                   |
| `Retention policy`  [^15]                    | `NO`                            | `NO`                        | `NO`                             | `NO`                         |
| `Expiration policy`                          | ![Checkmark icon](../../icons/checkmark-icon.svg) | ![Checkmark icon](../../icons/checkmark-icon.svg) | ![Checkmark icon](../../icons/checkmark-icon.svg) | ![Checkmark icon](../../icons/checkmark-icon.svg) |                         
| `Long-term retention policy`                 | `NO`                            | `NO`                        | `NO`                             | `NO`                         |
{: caption="Table 6. Use your own encryption key" caption-side="top"}

`[15]`: Currently, you cannot use your own key with a bucket that has a retention policy configured. 

 
**Use the customer-managed encryption model to manage and control the key that is used to encrypt data at-rest.**
{: tip}


[After you designate a root key in {{site.data.keyword.keymanagementserviceshort}}](/docs/services/key-protect?topic=key-protect-create-root-keys) and [grant access between your services](/docs/services/key-protect?topic=key-protect-integrate-services#grant-access), you can enable envelope encryption for a specified storage bucket by using the {{site.data.keyword.cos_full_notm}} GUI.

**To enable encryption with your custom key by using the {{site.data.keyword.keymanagementserviceshort}} service, [create a root key](/docs/services/key-protect?topic=key-protect-create-root-keys)  and create an [authorization](/docs/services/key-protect?topic=key-protect-integrate-services#grant-access) between your COS instance and the {{site.data.keyword.keymanagementserviceshort}} instance. Notice that the COS bucket and the {{site.data.keyword.keymanagementserviceshort}} instance need to be in the available in the same region.**
{: tip}

### Naming
{: #adoption_archive_2}

If you add PII information in the name of a bucket, you might be disclosing sensitive data to others in the same account.

**When you define your bucket name, do not add sensitive information in the name or in the description.**
{: tip}


### IAM resources to configure archiving
{: #adoption_archive_3}

To configure archiving, you need the following IAM policies:
* An IAM policy with minimum platform role **Viewer** and service role **Manager** for the {{site.data.keyword.la_full_notm}} service: This policy is required to access the web UI, and configure archiving of the LogDNA instance.
* An IAM policy with minimum platform role **Administrator** and service role **Manager**  for the COS service: The administrator role is required to define the service ID, with its associated API key, that is used by the {{site.data.keyword.la_full_notm}} instance to authenticate and access the {{site.data.keyword.cos_full_notm}} instance. The manager role is required to create and configure a bucket.

You also need a service ID. A service ID identifies a service similar to how a user ID identifies a user. Service IDs are not tied to a specific user. If the user that creates the service ID leaves your organization and is deleted from the account, the service ID remains. The {{site.data.keyword.la_full_notm}} service uses an API key that is associated to a service ID that you define on your COS instance to authenticate and write files to the COS bucket.

**Create a service ID for for the COS instance with writer permissions. Restrict access to the service ID so that the API key that is associated to it can only write to the bucket that you configure in LogDNA for archiving.**
{: tip} 

If you add PII information in the name or the description of the service ID, you might be disclosing sensitive data to others in the same account.

**When you define your service ID name, do not add sensitive information in the name or in the description.**
{: tip}

You might have a requirement to rotate API keys regularly or your API key might be compromissed. 

**Rotate the API key that is associated with your service ID regularly to prevent any security breaches caused by leaked keys or to comply with security guidelines.**
{: tip}

### IAM policies to control access to the archived files
{: #adoption_archive_4}

In COS, you can define policies to control the permissions that are granted to service IDs and users to read, write, update object properties, and delete objects. [Learn more](/docs/services/cloud-object-storage?topic=cloud-object-storage-iam).

**Restrict user access to archived files in the bucket.**
{: tip} 

### EU supported account
{: #adoption_archive_5}

When you archive logs from the Frankfurt LogDNA instance to {an {{site.data.keyword.cos_full_notm}} (COS) bucket, consider the following information:
* When you provision an instance of the COS service, this instance is a global one in your account. It is not region bound.
* You must configure a bucket that complies with the EU-Supported and GDPR regulations. For the list of COS EU-supported endpoints, see [EU-supported endpoints](/docs/services/cloud-object-storage?topic=cloud-object-storage-endpoints#endpoints-eu-managed).

    For example, consider the following scenarios:

    * For a bucket with **regional** resiliency, you can create the bucket in the `EU-DE` location to keep the data in Frankfurt.

    * For a bucket with **cross region** resiliency, you can create the bucket in the `eu-geo` location. Data is kept within the EU geography across datacenters that are located in Milan, Amsterdam, and Frankfurt.

* You must restrict user access to manage archived log files in these buckets.  
* Users are responsible for downloading files to EU-supported locations.

### Monitor archiving through Activity Tracker
{: #adoption_archive_6}

You can use the {{site.data.keyword.at_full}} service to monitor the activity of your {{site.data.keyword.cloud_notm}} account. You can use this service to investigate for abnormal activity and critical actions, and comply with regulatory audit requirements. In addition, you can be alerted on actions as they happen. The events that are collected comply with the Cloud Auditing Data Federation (CADF) standard.

In COS, you can track management and data events. 
* By default, these events are not enabled. 
* Management events report actions that change the state of resource configurations, bucket properties, and object properties.
* Data events report actions on buckets, objects, and multi-part objects such as creation, deletion, and access.
* You must configure each bucket to enable management events, or management and data events. Notice that you cannot enable data events only for a bucket. 
For more information, see [Activity Tracker events](/docs/services/cloud-object-storage?topic=cloud-object-storage-at-events).

**Enable collection of COS management and data events on the bucket that you use to archive data from a LogDNA instance. Use these events to monitor activity in your COS bucket.**
{: tip}

In {{site.data.keyword.at_full}}, you can define views, dashboard, and screens to monitor COS management and data events. You can also configure alerts on views to notify you when a specific condition occurs. On a view, you can configure an email alert, a Slack alert, a PagerDuty alert, or any combination of the above. For more information, see [Creating custom views](/docs/services/Activity-Tracker-with-LogDNA?topic=logdnaat-views) and [Managing alerts](/docs/services/Activity-Tracker-with-LogDNA?topic=logdnaat-alerts).

For example, you can define a view that reports when an object is archived in a bucket. On that view, you can configure an email alert to notify you when an object has been archived. You might have compliance requirements that require you to control who accesses data that is archived. You can define a view that reports access to a bucket, and define an alert to notify you when that happens.

**Define views, dashboard, screens, and alerts in {{site.data.keyword.at_full}} to investigate for abnormal activity and critical actions in your COS bucket, and to comply with regulatory audit requirements.**
{: tip}

### Archived file
{: #adoption_archive_7}

Whether you define policies to manage your COS objects (LogDNA archived files) at the bucket level, there might be situatiosn where you need to hold on to specific files for longer for compliance and auditing purposes. In COS, you can set different attributes per object that allow you to meet this requirements.

* You can define a **legal hold** flag to an archive file. Legal holds can be applied to objects during initial uploads or after an object is written. [Learn more](/docs/services/cloud-object-storage?topic=cloud-object-storage-immutable#immutable-terminology-hold).
* You can define an **indefinite retention** flag to store the object indefinitely until a new retention period is applied. [Learn more](/docs/services/cloud-object-storage?topic=cloud-object-storage-immutable#immutable-terminology-indefinite).

**Add a *legal hold* flag or an *indefinite retention* flag to individual archived files if you need to keep a file longer than the default retention period specified at the bucket level.**
{: tip}



## 7. Query archived data 
{: #adoption_query}

You can download data locally, and then use your own tools to query the data. When you download data for analysis, you are responsible for ensuring that your users comply with the regulations and compliance requirements that may be required for your organization. For example, if you must comply with GDPR, you need to control that users are following the download guidelines per GDPR rules.

You can use the {{site.data.keyword.sqlquery_short}} service to query {{site.data.keyword.la_full_notm}} archived files that are stored in a COS bucket in your account. You can run queries from the {{site.data.keyword.cloud_notm}} UI, or programmatically. 

**Avoid downloading data locally. Use the {{site.data.keyword.sqlquery_short}} service to query archived data.**
{: tip}


The {{site.data.keyword.sqlquery_short}} service provides a serverless, no-ETL solution to easily query data stored in {{site.data.keyword.cos_short}}. Underneath, SQL Query uses Apache Spark SQL as its underlying query engine. You can use the {{site.data.keyword.sqlquery_short}} to run SQL queries (that is, `SELECT` statements) to analyze, transform structured and semi-structured data, or clean up rectangular data. You cannot run actions such as `CREATE`, `DELETE`, `INSERT`, and `UPDATE`.

The {{site.data.keyword.sqlquery_short}} service can process input data that is read from CSV, JSON, ORC, Parquet, or AVRO files. Archived files from an {{site.data.keyword.at_full_notm}} instance contain data in JSON format. When you use the {{site.data.keyword.sqlquery_short}} service, each query result can be written to a `CSV`, `JSON`, `ORC`, `PARQUET`, or `AVRO` file in {an {{site.data.keyword.cos_short}}instance of your choice. 

**When you query an {{site.data.keyword.at_full_notm}} archive file, you must convert the JSON formatted file into `PARQUET` format to be able to query the contents successfully.**
{: tip}

**Use the {{site.data.keyword.sqlquery_short}} user interface (UI) to develop and test your queries, and the [SQL Query REST API](#restapi) to automate them.**
{: tip}

**If you plan to use the {{site.data.keyword.sqlquery_short}} service, and you require HIPAA compliance, create a bucket for your archives that uses a custom key to encrypt the data.**
{: important}


## 8. Define the notification strategy 
{: #adoption_alerts}

In a LogDNA instance, you define views to analyze the data. Then, you can configure 1 or more alerts per view to notify of an abnormal situation. [Learn more](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-alerts).
* You can configure multiple notification channels. Valid channels are: `email`, `Slack`, `PagerDuty`, `Webhook`
* You can choose to be notified by using a presence alert where you are alerted if more log lines than expected are present or to be notified by using an absence alert that is triggered when no data is available. 

**Define an absence alert to be notified when inactivity in an application or service is identified. Notice that absence alerts require data going through the view in the past 24 hours to be active.**
{: tip}

**Define a presence alert to be notified of exceptional situations in your applications and services that require your inmediate attention.**    
{: tip}


You can also define a **preset**. A preset is an alert template that you can attach to any number of views. 

To reuse an alert configuration with different views, configure an **alert preset**.
{: tip}

For compliance, define present alerts that notify


## 9. Network strategy
{: #adoption_network}

 VRF




## 10. Sending logs to a LogDNA instance
{: #adoption_ingestion}


## Exporting logs from a LogDNA instance
{: #adoption_export}


## Service platform logs
{: #adoption_svc_logs}


