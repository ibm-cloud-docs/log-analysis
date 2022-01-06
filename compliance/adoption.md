---

copyright:
  years:  2018, 2022
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, regulated, highly available workloads

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Adoption guidelines for regulated and highly available workloads
{: #adoption}

For regulated and highly available workloads, consider the following adoption guidelines when using the {{site.data.keyword.la_full_notm}} service:
{: shortdesc}


## Define resources naming standards for compliance
{: #adoption_naming}

When you create resources in the {{site.data.keyword.cloud_notm}}, you can choose how to name them, what information to include in their description fields, which tags to use to group them, associate metadata, and more. 

**Define naming standards that do not include PII and other sensitive information across all resources that are created in the {{site.data.keyword.cloud_notm}}.**
{: tip}



## Define the account management strategy
{: #adoption_account}

In {{site.data.keyword.cloud_notm}}, you can have 1 or more **stand-alone** accounts. You can manage each account individually or within an **enterprise** by configuring a multitiered hierarchy of accounts. 

Within an enterprise account, you create a multitiered hierarchy of accounts, with billing and payments for all accounts managed at the enterprise level. [Learn more](/docs/account?topic=account-what-is-enterprise).  
* The root enterprise account serves as the parent account to all other accounts in the enterprise. 
* Users and access management is isolated between the enterprise and its child accounts. No access is automatically inherited between the two types of accounts.
* Resources and services within an enterprise function the same as in stand-alone accounts. Each account in an enterprise can contain resources in resource groups and services in Cloud Foundry orgs and spaces. 

Notice that an enterprise can contain up to 5 tiers of accounts and account groups. In its most basic form, an enterprise has two tiers: the enterprise account, and a single child account.

The following table highlights some of the key features per account management strategy:

| Feature                                               | Stand-alone account management                    | Enterprise account management                     |
|-------------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| `Multitiered hierarchy of accounts`                   | NO                                                | ![Checkmark icon](../images/checkmark-icon.svg) |
| `Billing and payments managed from 1 account`         | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
| `Isolation of users and access management per account`| ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
| `Isolation of resources and services per account`     | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
| `Isolation of account settings`                       | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
| `IAM enabled`                                         | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
{: caption="Table 1. Types of accounts" caption-side="top"} 


In stand-alone accounts, you control access to resources by grouping them in resource groups, and configuring IAM policies that you assign to users and service IDs directly or through access groups. These policies define the level of access to work with services in the account. For example, you might have a stand-alone account where you run your development, pre-production, and production services and applications. 

By using an enterprise management account strategy, you achieve greater isolation of resources. When you configure a multitiered hierarchy of accounts, you get the flexibility to separate your development environments into separate tiers, or isolate by Line of Business (LoB) applications and services, or a combination of both. Each account retains the features of a stand-alone account, and you can still manage billing and payments from the root enterprise account.

In addition to these benefits, when you look into logging and how it fits with any of these management strategies, consider the following facts that will be covered later on in the topic in more detail:
* Service platform logs are collected and available per location (region) through 1 single logging instance. You do not have the ability to split logs from different services running in the same region to multiple instances. If you run your development, test, and production services in a stand-alone account, all those logs will be available through the same logging instance, and any user with permissions to view logs in that instance will be able to see everything.
* You can configure other log sources in {{site.data.keyword.cloud_notm}} and on-premisses to forward logs to any logging instance in your account. 

**Define an enterprise account management strategy to add an additional layer of isolation to resources in addition to stand-alone accounts.**
{: tip}


## Configure account settings for compliance
{: #adoption_acc_settings}

Across every industry, organizations require tight controls and visibility into where their data is stored and processed. 

**Indicate to {{site.data.keyword.IBM_notm}} your compliance requirements by enabling your {{site.data.keyword.cloud_notm}} account or {{site.data.keyword.cloud_notm}} Entreprise account as HIPAA or EU supported.**
{: tip}

In the {{site.data.keyword.cloud_notm}}, you can configure your account for EU support and for HIPAA support:
* You might choose to enable the **EU Supported** setting, for example, if you use resources to process personal data for European citizens. For more information, see [Set on the EU-Supported flag in your account](/docs/account?topic=account-eu-hipaa-supported#bill_eusupported).
* You might choose to enable the **HIPAA Supported** setting if you plan to include Protected Health Information (PHI) in HIPAA-enabled services. For more information, see [Set on the HIPAA flag in your account](/docs/account?topic=account-eu-hipaa-supported#enabling-hipaa).

Notice that only the account owner can enable the account to be EU supported and HIPAA supported. 

### HIPAA
{: #adoption_acc_settings_hipaa}

If you're the account owner, you can enable your {{site.data.keyword.cloud}} account to be HIPAA supported. For example, you might choose to enable the **HIPAA Supported** setting if you plan to include Protected Health Information (PHI) in HIPAA-enabled services.

The US Health Insurance Portability and Accountability Act (HIPAA) and the Health Information Technology for Economic and Clinical Health (HITECH) Act define standards for handling electronic healthcare transactions and information. If you or your company is a covered entity as defined by HIPAA, you must enable the HIPAA supported setting if you run sensitive workloads that are regulated under HIPAA and the HITECH Act. Learn more about {{site.data.keyword.cloud_notm}} compliance in [Compliance on the {{site.data.keyword.cloud_notm}}](https://www.ibm.com/cloud/compliance){: external}.
{: tip}

When you configure your account to be HIPAA enabled, consider the following information:
* You can filter on *HIPAA Enabled* services in the catalog. Accounts that enable the **HIPAA Supported** setting still have access to the full catalog of services. 
* You indicate to {{site.data.keyword.IBM_notm}} that your account stores protected health information (PHI).
* You digitally accept the IBM Business Associate Addendum (BAA) for covered entities.

Enable this setting only if you or your company is a covered entity as defined by HIPAA. If you or your company is a business associate of a covered entity, [contact {{site.data.keyword.cloud_notm}} Sales](https://www.ibm.com/account/reg/us-en/signup?formid=MAIL-wcp){: external} to accept the applicable BAA. For more information about HIPAA definitions of covered entities and business associates, see the [US Department of Health & Human Services](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html){: external} website.
{: tip}



## Define the logging instances strategy 
{: #adoption_resource_svc}

{{site.data.keyword.la_full_notm}} collects and aggregates logs in one centralized logging system.
* Log data is hosted on the {{site.data.keyword.cloud_notm}}. 
* Data is collocated in the location where an {{site.data.keyword.la_full_notm}} instance is provisioned. 


### Locations
{: #adoption_resource_svc_location}

You can provision instances of the {{site.data.keyword.la_full_notm}} service in any of the supported locations in the {{site.data.keyword.cloud_notm}}. For more information, see [Locations](/docs/log-analysis?topic=log-analysis-regions).

Per location (region), you can provision 1 or more logging instances. 
* You can collect logs from custom applications and services that run in the {{site.data.keyword.cloud_notm}} or outside, and forward them to any logging instance in your account.
* Only 1 instance in a location can be configured to collect logs automatically from [{{site.data.keyword.cloud_notm}} enabled services](/docs/log-analysis?topic=log-analysis-cloud_services) in that {{site.data.keyword.cloud_notm}} location.
* Each location represents the geographic area where your {{site.data.keyword.la_full_notm}} requests are handled and processed for that instance, and where data is resident. 
* Each MZR location has three different data centers for redundancy. The data for each location is kept in the three data centers near that location. If all three data centers in a location fail, the {{site.data.keyword.la_full_notm}} service for that location becomes unavailable.
* Each MZR configuration can accept a single data center failure.

**When you choose the locations where you plan to provision {{site.data.keyword.la_full_notm}} instances, check the regulatory and high availability (HA) specifications of each location.**
{: tip}

For example, in Europe, only the Frankfurt region is EU-supported.

You can also check [ensure zero downtime](/docs/overview?topic=overview-zero-downtime#zero-downtime) to learn more about the high availability and disaster recovery standards in {{site.data.keyword.cloud_notm}}. 


### Platform logs
{: #adoption_account_svc_logs}

To enable automatic collection of {{site.data.keyword.cloud_notm}} enabled services, you must configure 1 instance in a location with the **platform logs** flag. [Learn more](/docs/log-analysis?topic=log-analysis-config_svc_logs). When 1 instance is enabled to collect logs in a location, data from any instance of an enabled service in that location is collected automatically.

**Define 1 instance per location with the platform logs flag enabled.**
{: tip}

If you share staging, pre-production, and production services in the same {{site.data.keyword.cloud_notm}} account, notice that users, that are granted access to view data in the logging instance with the platform logs flag in a location, can see data from any service instance provisioned in that location. To prevent users from viewing log data from all service's instances, consider moving from a  single account model to an *Enterprise account* model.

If you cannot move to an enterprise account model, try reducing the number of users that are granted permissions to view the logs. In addition, you can also define exclusion rules to hide data from showing through the web UI. Exclusion rules stop logs from counting against your data usage quota and from being stored for search. [Learn more](/docs/log-analysis?topic=log-analysis-exclusion_rules).


### Resource groups
{: #adoption_resource_svc_rg}

Resource groups are a logical container for organizing your IAM-enabled resources.
* IAM-enabled services belong to a resource group. The {{site.data.keyword.la_full_notm}} service is an IAM-enabled service.
* You assign a resource to its resource group when you create it from the catalog. 
* You can't change the resource group assignment after you set it, which is why it's important to plan and set up your resource groups.
* If you add PII information in the resource group name, you might be disclosing sensitive data to others in the same account.

**Use resource groups to organize your {{site.data.keyword.la_full_notm}} instances for access control and billing purposes.**
{: tip}

Account owners can add resources to any resource group. Other users must be granted access by using an IAM access policy to add resources to resource groups. For more information, see [Best practices for organizing resources and assigning access](/docs/account?topic=account-account_setup).

**When you define your resource groups, do not add sensitive information in the name.**
{: tip}

### Naming
{: #adoption_resource_svc_name}

If you add PII or other sensitive information in the name or the description of a service instance, you might be disclosing sensitive data to others in the same account.

**When you define your logging instances names, do not add sensitive information in the name or in the description.**
{: tip}

### Service plan
{: #adoption_resource_svc_plan}

The service plan that you choose for a logging instance determines the number of days that data is available for search. For more information, see [Service plans](/docs/log-analysis?topic=log-analysis-service_plans).

**Choose your plan based on the number of days that you need to be able to search data online through the web UI.**
{: tip}

The HIPAA plan has a maximum of 25 users. If you need to grant permissions to more than 25 users, [open a support ticket](/docs/get-support).


### Tags
{: #adoption_resource_svc_tags}

A tag is a label that you assign to a resource for easy filtering of resources in your resource list. 
* You can use tags to organize your resources and easily find them later. 
* You can also use tags to help you with identifying specific team usage or cost allocation when you view your [exported usage report](/docs/billing-usage?topic=billing-usage-viewingusage#export-csv).

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



## Define the log ingestion strategy
{: #adoption_account_ingestion}

For non-{{site.data.keyword.cloud_notm}} enabled services, you must decide the method to collect and forward logs from a log source that you want to monitor to a logging instance. 

In {{site.data.keyword.la_full_notm}}, you can collect and forward data to a logging instance by using any of the following methods:
* `logging agent`: Logging agent that automatically collects and forwards logs to 1 logging instance in your account.
* `Syslog`: Logging daemon that collects information across multiple devices and system-services, and forwards logs to 1 logging instance in your account. 
* `REST API`: API that you can use to send log data and custom metadata to 1 logging instance in your account.
* `Code libraries`: Libraries that you can use to code ingestion of logs from your apps and services to 1 logging instance. logging offer libraries for Node.JS, Python, Rails, Ruby, Go, iOS, Java, and PHP.

**For any method that you adopt, you have the flexibility to choose the logging instance where you want to send data per log source. Decide how many instances you might need to collect data from all your log sources based on who can see the data and the type of data that is collected. Avoid sending data to a logging instance that has the platform logs flag enabled.**
{: tip}

**Whenever a logging agent is available for a type of log source, configure the agent to automatically collect and forward logs from the log source to the logging instance. The agent is the preferred log collection mechanism.** 
{: tip}

The logging agent authenticates by using the logging Ingestion Key and opens a secure web socket to the {{site.data.keyword.la_full_notm}} ingestion servers; monitors all files with extension `.log`*,  and extensionless files under `/var/log/`; and can be customized to exclude data that you do not want to collect or to include custom paths that you want to monitor, and more.

For example, you can configure a Kubernetes cluster and an OpenShift cluster with a logging agent. For more information, see [Configuring a logging agent for a standard Kubernetes cluster](/docs/log-analysis?topic=log-analysis-config_agent_kube_cluster) and [Configuring a logging agent for an OpenShift Kubernetes cluster](/docs/log-analysis?topic=log-analysis-config_agent_os_cluster).

To configure a logging agent on Linux Ubuntu or Debian, see [Configuring a logging agent on Linux Ubuntu or Debian](/docs/log-analysis?topic=log-analysis-config_agent_linux).

**To send data and attach custom metadata to each log record, you can use the REST API.**
{: tip}

**Configure syslog to collect and forward logs from Cloud Foundry applications.**
{: tip}

For example, you can configure a custom user provided service (CUPS) for each Cloud Foundry (CF) app that you want to monitor through a logging instance. The CUPS service sends logs via a syslog link to a logging syslog endpoint and port. This option is only available if the CF app send logs to STDOUT and STDERR. If the CF app is configured to send logs via syslog and not to STDOUT and STDERR, this option is not supported. [Learn more](/docs/log-analysis?topic=log-analysis-monitor_cfapp_logs).



## Define the IAM strategy
{: #adoption_iam}

**Use {{site.data.keyword.iamlong}} (IAM) to securely authenticate users and service IDs, and to control access to all cloud resources and data consistently in the {{site.data.keyword.cloud_notm}}.**
{: tip}

If you add PII information in the name or description of IAM resources, you might be disclosing sensitive data to others in the same account.

**When you define your IAM resources, do not add sensitive information in their names and descriptions.**
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
| `Administrators`         | Users in this group should have permissions to fully manage the service and grant other users in the account permissions to work with the service in the {{site.data.keyword.cloud_notm}}. |
| `Managers`               | Users in this group should have permissions to fully manage the service in the {{site.data.keyword.cloud_notm}}. |
| `Advanced service users` | Users in this group should have permissions to run advanced service tasks.  |
| `Users`                  | Users in this group should have permissions to run basic tasks.  |
{: caption="Table 2. List of access groups" caption-side="top"} 

### Policies
{: #adoption_iam_policies}

A policy determines the full set of actions that a user or service ID can perform. 

**For each access group, define a policy for each resource group that defines the level of access to that resource group.** 
{: tip}

By default, the account owner is the only user in the account that can grant permissions to other users to manage and work with the {{site.data.keyword.la_full_notm}} service. 

**To allow other users or service IDs in the account to manage the service and be able to grant permissions to work with the {{site.data.keyword.la_full_notm}} service, define a policy for the {{site.data.keyword.la_full_notm}} service with the platform role *administrator*. Grant this policy to the administrators access group.** 
{: tip}

For more information, see [Granting permissions to a user to become an administrator of the service](/docs/log-analysis?topic=log-analysis-work_iam#admin_account).

Access to resources within a resource group can be granted to all resources in a group, or only selected services within a group. 

Access policies set a target, which is typically a service instance or all instances of a service in a resource group, and a role, which defines what type of access is allowed.

Roles define the actions that a user or serviceID can run. There are different types of roles in the {{site.data.keyword.cloud_notm}}:
* *Platform management roles* define permissions to work with the service at the platform level, for example, some actions are assign user access for the service, create or delete service IDs, create instances, assign policies for your service to other users, and bind instances to applications. [Learn more](/docs/log-analysis?topic=log-analysis-work_iam)
.
* *Service access roles* define permissions for calling the service's API. [Learn more](/docs/log-analysis?topic=log-analysis-work_iam)
.

**For each access group, define a policy for each resource group that specifies the permissions granted to work with the resource group, the permissions to manage instances of the {{site.data.keyword.la_full_notm}} service in that resource group, and the permissions to run {{site.data.keyword.la_full_notm}} tasks.**
{: tip}

| Access group             | Policy         |
|--------------------------|----------------|
| `Administrators`         | Grant a policy for the resource group with resource group access **administrator**. Select the {{site.data.keyword.la_full_notm}} service, and select the platform role **administrator**, and the service role **manager**. |
| `Managers`               | Grant a policy for the resource group with platform role **editor**. Select the {{site.data.keyword.la_full_notm}} service, and select the platform role **editor**, and the service role **manager**. |
| `Advanced service users` | Grant a policy for the resource group with platform role **viewer**. Select the {{site.data.keyword.la_full_notm}} service, and select the platform role **viewer**, and the service role **standard member**. |
| `Users`                  | Grant a policy for the resource group with platform role **viewer**. Select the {{site.data.keyword.la_full_notm}} service, and select the platform role **viewer**, and the service role **reader**. |
{: caption="Table 3. Roles per access group policy" caption-side="top"} 

**Every user that requires permissions to work with the {{site.data.keyword.la_full_notm}} service in your account must be assigned a resource group policy that includes the permissions for the {{site.data.keyword.la_full_notm}} service.**
{: tip}

You can assign a single policy to the access group instead of assigning the same access multiple times per individual user or service ID. 

**Add users and service IDs to an access group. Grant permissions to these users and service IDs through the access group.**
{: tip}

[Learn more](/docs/log-analysis?topic=log-analysis-work_iam).


## Configure the account settings for authentication into your account
{: #adoption_login}

Multi-factor authentication (MFA) adds an extra layer of security to your account by requiring all users to authenticate by using an additional authentication method beyond an ID and password. This is also commonly known as two-factor authentication (2FA). 

The {{site.data.keyword.cloud_notm}} account owner or administrator for the billing service can choose to require multi-factor authentication (MFA) for every user in the account or just users with non-federated IDs who do not use SSO. All users with an IBMid use a time-based one-time passcode (TOTP) MFA method, and any users with a different type of ID must be enabled to use the time-based one-time passcode authentication (TOTP), security questions, or an external authentication method separately. [Learn more](/docs/account?topic=account-enablemfa).

You can also configure MFA options such as security questions, using a time-based one-time passcode, and using an external authentication method. These types of MFA options are specific per account and are available only with former classic infrastructure accounts.

**Enable multi-factor authentication (MFA) in your {{site.data.keyword.cloud_notm}} account for all users.**
{: tip}


## Define the network strategy
{: #adoption_network}

In {{site.data.keyword.la_full_notm}}, you can use the logging agent to collect and forward logs to your {{site.data.keyword.la_full_notm}} instance. After you provision an instance of {{site.data.keyword.la_full}}, you must configure a logging agent for each log source that you want to monitor. 

You can configure the logging agent to connect to the logging instance through the public network or through the private network. 
* By default, the agent connects through the public network.
* To connect over a private network, you must have access to classic infrastructure and [enable virtual routing and forwarding (VRF)](/docs/account?topic=account-vrf-service-endpoint) and connectivity to service endpoints for your account.

The type of network defines the level of isolation and security that is configured to move workloads between cloud-based resources in your account. 

Some factors that you must consider when you must decide which network to choose are:
* Corporate requirements on how services and applications can access cloud-based services in your account
* Security on production workloads
* Industry compliance regulations

**If you require no access to Internet to connect to {{site.data.keyword.cloud_notm}} services and isolated connectivity for workloads in your account, connect the logging agent over the private network.**
{: tip}

Consider the following information when you work with private endpoints:
* Private endpoints are not accessible from the public internet. 
* All traffic is routed to the {{site.data.keyword.cloud_notm}} private network. 
* Services like {{site.data.keyword.la_full_notm}} are no longer served on an internet routable IP address.

Consider the following limitations:
* Ingestion endpoints of type `syslog-tcp (syslog-a)` and `syslog-udp (syslog-u)` are not currently supported on the Cloud Service Endpoint (CSE) network. 
* The logging web UI is not currently supported on the CSE network.


**If you have an additional firewall set up, or you have customized the firewall settings in your {{site.data.keyword.cloud_notm}} infrastructure, you must allow outgoing network traffic to the {{site.data.keyword.la_full_notm}} service on TCP port 443 and TCP port 80 in your firewall. The API endpoint is required for logging agent authentication.**
{: tip}

If you have an additional firewall set up, or you have customized the firewall settings in your {{site.data.keyword.cloud_notm}} infrastructure, and you want to configure the logging agent to connect to the logging instance through the private network, open a support ticket to request the private IP addresses that you must enable in your firewall. For information about opening an IBM support ticket, see [Getting support](/docs/get-support).
{: tip}


## Define the notification strategy 
{: #adoption_alerts}

In a logging instance, you define views to analyze the data. Then, you can configure 1 or more alerts per view to notify of an abnormal situation. [Learn more](/docs/log-analysis?topic=log-analysis-alerts).

You can choose to be notified by using an absence alert that is triggered when no data is available.

**Define an absence alert to be notified when inactivity in an application or service is identified. Notice that absence alerts require data in the view within the past 24 hours for the alert to be active.**
{: tip}

You can choose to be notified by using a presence alert that is triggered when more log lines than expected are present.  

**You will want to define a presence alert to be notified of exceptional situations in your applications and services that require immediate attention.**    
{: tip}

You can configure multiple notification channels. Valid channels are: `email`, `Slack`, `PagerDuty`, `Webhook`

| Channel      | Guidance             |
|--------------|----------------------|
| `email`      | Email is a traditional communication method that you can use to notify 1 or more users. This notification channel requires users to be monitoring proactively their emails to detect an alert. **Define an email alert to verify that the alert on a view is working, and to inform users of situations they may have requested information.** |
| `Slack`      | Slack is a collaborative tool that you can use to communicate and share information across 1 or more teams. **Define a Slack alert to inform about routine scenarios that you might want to monitor.** |
| `PagerDuty`  | PagerDuty is an incident management tool that you can use to automate incident resolution and escalation, define on-call schedules and more. **Define a PagerDuty alert to be notified immediately so that you can take action promptly.**  |
| `Webhook`    | A webhook is another method that you can configure to provide other applications information. **Define a webhook alert if you have a third party tool that you can configure with a logging instance via a webhook, and where you plan to manage notifications.** |
{: caption="Table 4. Guidance for notification channel" caption-side="top"}

**Configure PagerDuty alerts to be notified immediately so that you can take action promptly on problems and automate their resolution. In addition, configure Slack alerts to share alerts and information.**
{: tip}

In {{site.data.keyword.la_full_notm}}, you can also define a **preset**. A preset is an alert template that you can attach to any number of views.

**To reuse an alert configuration with different views and enforce notification channels across users that analyze data through that instance, configure alert presets**.
{: tip}

When you send a notification, you can include log data as part of the notification. 

**Customize the data that is included in a notification for situations where the receiver of the notification does not have access to the log data.**
{: tip}



## Define the archive strategy
{: #adoption_archive}

You might have different requirements that require archiving your data:
* Backup requirements to keep data for a period of time
* Data access requirements so that you can query the data after it is not available for search through the web UI
* Disaster recovery requirements 
* Compliance requirements

logging as a service does not backup your data. 

There are 2 types of data that you should consider archiving:
* Log data

    By default, archiving of log data is not enabled for any logging instance. 

    When you enable archiving of your log data, notice that you are responsible for checking that your archived files are not corrupted, and for the maintenance of your archived files.
    {: note}

* Web UI resource definitions such as parsing templates, exclusion rules, views, screens, and dashboards.

**You will want to archive your logging resource definitions and your log data.**
{: tip}

### Backup the resource configurations of your logging instance
{: #adoption_archive_ui}

In the logging web UI, you can define custom views, dashboards, parsing templates, screens, and exclusion rules that you can use to view and analyze data.

To reuse resource definitions that you define in your logging instance, you can export these resources from an {{site.data.keyword.la_full_notm}} instance as a JSON file. Then, you can import the definitions into other logging instances. For example, you can reuse your logging resources across different environments for your stage, pre-production, and production logging instances. [Learn more](/docs/log-analysis?topic=log-analysis-reuse_resource_definitions).

**Backup logging resource definitions into a version control system such as a git repository where you can control access to the archived files and manage versions.**
{: tip}

### Archive log data to a COS bucket
{: #adoption_archive_data}

**Enable archiving of your data from a logging instance to an {{site.data.keyword.cos_full_notm}} (COS) bucket.**
{: tip}

After you provision a logging instance, you can configure archiving to an {{site.data.keyword.cos_full_notm}} (COS) bucket. You can create different types of buckets based on your requirements. 

When you plan the bucket for a logging instance, consider the following information:

| Requirement                                            | Question to answer                                                | Information                                                                 |
|--------------------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `Type of workload` [1]                                | How often do you need to access the data?                         | [Information about storage classes](/docs/cloud-object-storage?topic=cloud-object-storage-classes#classes-about) |
| `Retention policy` [2]                                | Do you need to protect data from being deleted?                   | [Information about Immutable Object Storage](/docs/cloud-object-storage?topic=cloud-object-storage-immutable) |
| `Expiration policy` [3]                               | Do you need automatic deletion of files?                          | [Information about expiration rules](/docs/cloud-object-storage?topic=cloud-object-storage-expiry) |                            
| `Long-term retention policy` [4]                      | Do you need to keep data for a long period of time?               | [Information about archiving COS files for long term storage](/docs/cloud-object-storage?topic=cloud-object-storage-archive) |
| `Encryption of data at-rest with my own key` [5]      | Can I use my own key to encrypt data at-rest?                     | [Information about encryption of data at-rest](/docs/cloud-object-storage?topic=cloud-object-storage-encryption) |
| `Data resiliency` [6]                                 | Do you need to store the data in a specific geographical location? | [Information about resiliency](/docs/cloud-object-storage/basics?topic=cloud-object-storage-endpoints) |
{: caption="Table 5. COS bucket requirements" caption-side="top"} 

`[1]`: Data might sit untouched for long periods of time. For less active workloads, you can create buckets with different storage classes. For example, use the standard storage class for active workloads, where you need to access data at any time.

`[2]`: You can choose *Immutable Object Storage* to preserve electronic records and maintain data integrity. When you define a retention policy for a bucket, you are specifying that the data is stored in a WORM (Write-Once-Read-Many), non-erasable and non-rewritable manner. This policy is enforced until the end of a retention period and the removal of any legal holds. Notice that `Immutable Object Storage` is available in certain regions only.

`[3]`: You can use an expiration rule to delete objects automatically after a defined period from the object creation date. 

`[4]`: You can define a retention policy to retain data for a long period of time and have the data available for downloads and queries. If you do not need to query the data, and you just need to keep it for compliance, look into archiving COS files from any of the storage tiers to a long-term offline archive location or use the online *Cold Vault* option.

`[5]`: COS provides several options to encrypt your data. By default, all objects that are stored in COS are encrypted by using randomly generated keys and an all-or-nothing-transform (AONT). With COS, you can also manage your keys manually by providing your own encryption keys - referred to as Server-Side Encryption with Customer-Provided Keys (SSE-C). Alternatively, you can choose to use the integration capabilities with {{site.data.keyword.cloud}} Key Management Services like {{site.data.keyword.keymanagementservicelong}} and {{site.data.keyword.hscrypto}}. 

`[6]`: Resiliency refers to the scope and scale of the geographic area across which your data is distributed. For example, you can choose cross region resiliency to spread your data across several geographical areas, or regional resiliency to spread data across a single region. Notice that a single data center distributes data across devices within a single site only.


**Create a custom COS bucket with the storage features and the policies that you identify.** [Learn more](/docs/log-analysis?topic=log-analysis-archiving).
{: tip}

**Do not configure a long-term retention policy on a COS bucket if you need access to the data and query it with the {{site.data.keyword.sqlquery_short}} service.**
{: tip}

Use the following table to help you identify the features that you should consider when you create a bucket:

| Requirement                                  | Storage class: `Standard`[7]   | Storage class: `Vault`[8]  | Storage class: `Cold Vault`[9]  | Storage class: `Flex`[10]  |
|----------------------------------------------|---------------------------------|-----------------------------|----------------------------------|-----------------------------|
| `Type of workload`                           | `Continuous access`             | `Data isn't accessed frequently` | `Accessed every 90 days or less` | `Dynamic workloads where access patterns are difficult to predict` |
| `Data resiliency`                            | `Cross region`                  | `Cross region`             | `Cross region`                  | `Cross region`             |
| `Retention policy`                           | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
| `Expiration policy`                          | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |                         
| `Long-term retention policy`                 | `NO`                            | `NO`                        | `NO`                             | `NO`                         |
{: caption="Table 6. Disaster recovery or compliance requirements" caption-side="top"}
{: #archive-table-4}
{: tab-title="Disaster Recovery or compliance requirements"}
{: tab-group="archive"}
{: class="simple-tab-table"}
{: row-headers}

| Requirement                                  | Storage class: `Standard`[7]  | Storage class: `Vault`[8] | Storage class: `Cold Vault`[9] | Storage class: `Flex`[10] |
|----------------------------------------------|---------------------------------|-----------------------------|----------------------------------|-----------------------------|
| `Type of workload`                           | `Continuous access`             | `Data isn't accessed frequently` | `Accessed every 90 days or less` | `Dynamic workloads where access patterns are difficult to predict` |
| `Data resiliency`                            | `Cross region` or `Regional`    | `Cross region` or `Regional`    | `Cross region` or `Regional`   | `Cross region` or `Regional`   |
| `Retention policy`                           | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
| `Expiration policy`                          | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |                         
| `Long-term retention policy`                 | `NO`                            | `NO`                        | `NO`                             | `NO`                         |
{: caption="Table 7. Backup or access to data beyond the service plan days requirements" caption-side="top"}
{: #archive-table-5}
{: tab-title="Backup or access to data beyond the service plan days requirements"}
{: tab-group="archive"}
{: class="simple-tab-table"}
{: row-headers}

`[7]`: Standard is used for active workloads. No charge incurs for data that is retrieved (other than the cost of the operational request itself and public outbound bandwidth).

`[8]`: Vault is used for cool workloads where data isn't accessed frequently, but a retrieval charge applies for reading data. The service includes a threshold for object size and storage period consistent with the intended use of this service for cooler, less-active data.

`[9]`: Cold Vault is used for cold workloads where data is primarily archived (accessed every 90 days or less) - a larger retrieval charge applies for reading data. The service includes a threshold for object size and storage period consistent with the intended use of this service: storing cold, inactive data.

`[10]`:  Flex is used for dynamic workloads where access patterns are more difficult to predict. Depending on usage, if the cost of cooler storage that is combined with retrieval charges exceeds a cap value, then the storage charge increases and no any retrieval charges apply. If the data isn't accessed frequently, Flex storage can be more cost effective than Standard storage. If cooler usage patterns become more active, Flex storage is more cost effective than Vault or Cold Vault storage. No threshold object size or storage period applies to Flex buckets.

Objects that are subject to a bucket's `Immutable Object Storage` retention policy will have expiration actions deferred until the retention policy is no longer enforced. 
{: note}


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
| `Retention policy` [15]                      | `NO`                            | `NO`                        | `NO`                             | `NO`                         |
| `Expiration policy`                          | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |                         
| `Long-term retention policy`                 | `NO`                            | `NO`                        | `NO`                             | `NO`                         |
{: caption="Table 8. Use your own encryption key" caption-side="top"}

`[15]`: Currently, you cannot use your own key with a bucket that has a retention policy configured. 

 
**Use the customer-managed encryption model to manage and control the key that is used to encrypt data at-rest.**
{: tip}


[After you designate a root key in {{site.data.keyword.keymanagementserviceshort}}](/docs/key-protect?topic=key-protect-create-root-keys) and [grant access between your services](/docs/key-protect?topic=key-protect-integrate-services#grant-access), you can enable envelope encryption for a specified storage bucket by using the {{site.data.keyword.cos_full_notm}} GUI.

**To enable encryption with your custom key by using the {{site.data.keyword.keymanagementserviceshort}} service, [create a root key](/docs/key-protect?topic=key-protect-create-root-keys)  and create an [authorization](/docs/key-protect?topic=key-protect-integrate-services#grant-access) between your COS instance and the {{site.data.keyword.keymanagementserviceshort}} instance. Notice that the COS bucket and the {{site.data.keyword.keymanagementserviceshort}} instance need to be available in the same region.**
{: tip}

### Naming
{: #adoption_archive_2}

If you add PII information in the name of a bucket, you might be disclosing sensitive data to others in the same account.

**When you define your bucket name, do not add sensitive information in the name or in the description.**
{: tip}


### IAM resources to configure archiving
{: #adoption_archive_3}

To configure archiving, you need the following IAM policies:
* An IAM policy with minimum platform role **Viewer** and service role **Manager** for the {{site.data.keyword.la_full_notm}} service: This policy is required to access the logging web UI, and configure archiving of the logging instance.
* An IAM policy with minimum platform role **Administrator** and service role **Manager**  for the COS service: The administrator role is required to define the service ID, with its associated API key, that is used by the {{site.data.keyword.la_full_notm}} instance to authenticate and access the {{site.data.keyword.cos_full_notm}} instance. The manager role is required to create and configure a bucket.

You also need a service ID. A service ID identifies a service similar to how a user ID identifies a user. Service IDs are not tied to a specific user. If the user that creates the service ID leaves your organization and is deleted from the account, the service ID remains. The {{site.data.keyword.la_full_notm}} service uses an API key that is associated to a service ID that you define on your COS instance to authenticate and write files to the COS bucket.

**Create a service ID for for the COS instance with writer permissions. Restrict access to the service ID so that the API key that is associated to it can only write to the bucket that you configure in logging for archiving.**
{: tip} 

If you add PII information in the name or the description of the service ID, you might be disclosing sensitive data to others in the same account.

**When you define your service ID name, do not add sensitive information in the name or in the description.**
{: tip}

You might have a requirement to rotate API keys regularly or your API key might be compromised. 

**Rotate the API key that is associated with your service ID regularly to prevent any security breaches caused by leaked keys or to comply with security guidelines.**
{: tip}

### IAM policies to control access to the archived files
{: #adoption_archive_4}

In COS, you can define policies to control the permissions that are granted to service IDs and users to read, write, update object properties, and delete objects. [Learn more](/docs/cloud-object-storage?topic=cloud-object-storage-iam).

**You will want to restrict user access to archived files in the bucket.**
{: tip} 

### EU supported account
{: #adoption_archive_5}

When you archive logs from the Frankfurt logging instance to an {{site.data.keyword.cos_full_notm}} (COS) bucket, consider the following information:
* When you provision an instance of the COS service, this instance is a global one in your account. It is not region bound.
* You must configure a bucket that complies with the EU-Supported and GDPR regulations. For the list of COS EU-supported endpoints, see [EU-supported endpoints](/docs/cloud-object-storage?topic=cloud-object-storage-endpoints#endpoints-eu-managed).

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
For more information, see [Activity Tracker events](/docs/cloud-object-storage?topic=cloud-object-storage-at-events).

**Enable collection of COS management and data events on the bucket that you use to archive data from a logging instance. Use these events to monitor activity in your COS bucket.**
{: tip}

In {{site.data.keyword.at_full}}, you can define views, dashboard, and screens to monitor COS management and data events. You can also configure alerts on views to notify you when a specific condition occurs. On a view, you can configure an email alert, a Slack alert, a PagerDuty alert, or any combination of alerts. For more information, see [Creating custom views](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step7) and [Managing alerts](/docs/log-analysis?topic=log-analysis-alerts).

For example, you can define a view that reports when an object is archived in a bucket. On that view, you can configure an email alert to notify you when an object has been archived. You might have compliance requirements that require you to control who accesses data that is archived. You can define a view that reports access to a bucket, and define an alert to notify you when that happens.

**Define views, dashboard, screens, and alerts in {{site.data.keyword.at_full}} to investigate for abnormal activity and critical actions in your COS bucket, and to comply with regulatory audit requirements.**
{: tip}

### Archived file
{: #adoption_archive_7}

Although you define policies to manage your COS objects (logging archived files) at the bucket level, there might be situations where you need to hold on to specific files for longer for compliance and auditing purposes. In COS, you can set different attributes per object that allow you to meet this requirements.

* You can define a **legal hold** flag to an archive file. Legal holds can be applied to objects during initial uploads or after an object is written. [Learn more](/docs/cloud-object-storage?topic=cloud-object-storage-immutable#immutable-terminology-hold).
* You can define an **indefinite retention** flag to store the object indefinitely until a new retention period is applied. [Learn more](/docs/cloud-object-storage?topic=cloud-object-storage-immutable#immutable-terminology-indefinite).

**Add a *legal hold* flag or an *indefinite retention* flag to individual archived files if you need to keep a file longer than the default retention period specified at the bucket level.**
{: tip}



## Define the strategy to query archived data 
{: #adoption_query}

You can download data locally, and then use your own tools to query the data. When you download data for analysis, you are responsible for ensuring that your users comply with the regulations and compliance requirements that may be required for your organization. For example, if you must comply with GDPR, you need to control that users are following the download guidelines per GDPR rules.

You can use the {{site.data.keyword.sqlquery_short}} service to query {{site.data.keyword.la_full_notm}} archived files that are stored in a COS bucket in your account. You can run queries from the {{site.data.keyword.cloud_notm}} UI, or programmatically. 

**Avoid downloading data locally. Use the {{site.data.keyword.sqlquery_short}} service to query archived data.**
{: tip}


The {{site.data.keyword.sqlquery_short}} service provides a server-less, no-ETL solution to easily query data stored in {{site.data.keyword.cos_short}}. Underneath, SQL Query uses Apache Spark SQL as its underlying query engine. You can use the {{site.data.keyword.sqlquery_short}} to run SQL queries (that is, `SELECT` statements) to analyze, transform structured and semi-structured data, or clean up rectangular data. You cannot run actions such as `CREATE`, `DELETE`, `INSERT`, and `UPDATE`.

The {{site.data.keyword.sqlquery_short}} service can process input data that is read from CSV, JSON, ORC, Parquet, or AVRO files. Archived files from an {{site.data.keyword.at_full_notm}} instance contain data in JSON format. When you use the {{site.data.keyword.sqlquery_short}} service, each query result can be written to a `CSV`, `JSON`, `ORC`, `PARQUET`, or `AVRO` file in an {{site.data.keyword.cos_short}}instance of your choice. 

**When you query an {{site.data.keyword.at_full_notm}} archive file, you must convert the JSON formatted file into `PARQUET` format to be able to query the contents successfully.**
{: tip}

**Use the {{site.data.keyword.sqlquery_short}} user interface (UI) to develop and test your queries, and the [SQL Query REST API](#restapi) to automate them.**
{: tip}

**If you plan to use the {{site.data.keyword.sqlquery_short}} service, and you require HIPAA compliance, create a bucket for your archives that uses a custom key to encrypt the data.**
{: tip}





