---

copyright:
  years:  2018, 2019
lastupdated: "2019-08-12"

keywords: LogDNA, IBM, Log Analysis, logging, overview

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

# HIPAA compliance
{: #compliance_hipaa}

Across every industry, organizations require tighter controls and visibility into where their data is stored and processed in the {{site.data.keyword.cloud}}. To manage logs for HIPAA resources by using the {{site.data.keyword.la_full_notm}} service, consider the following information:
{:shortdesc}

HIPAA compliance is a shared responsibility. {{site.data.keyword.IBM_notm}} only provides the security and the tools to ensure its cloud platform can be used without violating HIPAA rules. It is the responsibility of HIPAA-covered entities to ensure that cloud-based infrastructure and applications are not misconfigured, and that stored files are appropriately secured.
{: important}

## Enable the HIPAA supported settings in your account
{: #compliance_hipaa_supported}

If you're the account owner, you can enable your {{site.data.keyword.cloud}} account to be HIPAA supported. You might choose to enable the **HIPAA Supported setting** if you plan to include Protected Health Information (PHI) in HIPAA-enabled services.

The US Health Insurance Portability and Accountability Act (HIPAA) and the Health Information Technology for Economic and Clinical Health (HITECH) Act define standards for handling electronic healthcare transactions and information. If you or your company is a covered entity as defined by HIPAA, you must enable the HIPAA Supported setting if you run sensitive workloads that are regulated under HIPAA and the HITECH Act. Learn more about {{site.data.keyword.cloud_notm}} compliance in [Compliance on the {{site.data.keyword.cloud_notm}}](https://www.ibm.com/cloud/compliance){: new_window} ![External link icon](../icons/launch-glyph.svg "External link icon").

Enabling this setting has the following effects:

* Enables you to filter on HIPAA Enabled services in the catalog
* Indicates to IBM that your account stores protected health information (PHI)
* Digitally accepts the IBM Business Associate Addendum (BAA) for covered entities

Enable this setting only if you or your company is a covered entity as defined by HIPAA. If you or your company is a business associate of a covered entity, [contact {{site.data.keyword.cloud_notm}} Sales](https://www.ibm.com/account/reg/us-en/signup?formid=MAIL-wcp){: new_window} ![External link icon](../icons/launch-glyph.svg "External link icon") to accept the applicable BAA. For more information about HIPAA definitions of covered entities and business associates, see the [US Department of Health & Human Services](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html){: new_window} ![External link icon](../icons/launch-glyph.svg "External link icon") website.
{: important}

Accounts that enable the **HIPAA Supported setting** still have access to the full catalog of services. 


## Provision your {{site.data.keyword.la_full_notm}} instances with the HIPAA service plan
{: #compliance_hipaa_provision}


### Step 1. Enable the HIPAA plan in your account
{: #compliance_hipaa_provision_plan}

To have access to the HIPAA plan in your account, you must contact {{site.data.keyword.IBM_notm}}. [Open a support ticket](/docs/get-support?topic=get-support-getting-customer-support#getting-customer-support). You need to accept a BAA with LogDNA prior to having access to this plan.

### Step 2. Provision instances of the service in your account
{: #compliance_hipaa_provision_provision}

Choose any of the following methods to provision an instance of the {{site.data.keyword.la_full_notm}} service:
[Provisioning an instance through the Observability dashboard](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-provision#provision_ui)
[Provisioning an instance through the catalog](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-provision#provision_catalog)
[Provisioning an instance through the CLI](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-provision#provision_cli)

Make sure that your naming convention for {{site.data.keyword.la_full_notm}} instances does not include PII information. Choose the **HIPAA service plan** for your logging instances.
{: important}


### Step 3. Label your service
{: #compliance_hipaa_provision_tag}

Set the tag **HIPAA** to the {{site.data.keyword.la_full_notm}} instances that you provision in your account.

Complete the following steps:

1. [Log in to your {{site.data.keyword.cloud_notm}} account ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window}.
2. Go to the menu icon ![menu icon](../../icons/icon_hamburger.svg) &gt; **Resource list**.
3. In the *Services* section, identify the instance that you want to tag.
4. Go to the action menu icon ![action menu icon](../../icons/icon_hamburger.svg). Select **Add tags** or **Edit tags**.
5. Enter the tag **HIPAA**.
6. Click **Save**.

 
## Restrict access to manage and view the data
{: #compliance_hipaa_iam}

The HIPAA plan allows a maximum of 25 team members per instance.
{: important}


### Step 1. Define access groups
{: #adoption_iam_access_groups}

You can assign permissions to work with the {{site.data.keyword.la_full_notm}} service within the context of the service, a resource group, or an access group. You can create multiple access groups. Define multiple access groups to organize users and service IDs into a single entity that makes it easy for you to manage IAM permissions.

When you define your access groups, consider the following information:

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

By default, the account owner is the only user in the account that can grant permissions to other users to manage and work with the {{site.data.keyword.la_full_notm}} service. To allow other users or service IDs in the account to manage the service and be able to grant permisisons to work with the {{site.data.keyword.la_full_notm}} service, define a policy for the {{site.data.keyword.la_full_notm}} service with the platform role **administrator**. Grant this policy to the administrators access group. For more information, see [Granting permissions to a user to become an administrator of the service](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account).

Access to resources within a resource group can be granted to all resources in a group, or only selected services within a group. Policies set a target, which is typically a service instance or all instances of a service in a resource group, and a role, which defines what type of access is allowed. Roles define the actions that a user or serviceID can run. 

There are different types of roles in the {{site.data.keyword.cloud_notm}}:
* *Platform management roles* define permissions to work with the service at the platform level, for example, some actions are assign user access for the service, create or delete service IDs, create instances, assign policies for your service to other users, and bind instances to applications. [Learn more](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#platform).
* *Service access roles* define permissions for calling the service's API. [Learn more](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#service).

For each access group, define a policy for each resource group that specifies the permissions granted to work with the resource group, the permissions to manage instances of the {{site.data.keyword.la_full_notm}} service in that resource group, and the permissions to run {{site.data.keyword.la_full_notm}} tasks.**
{: note}

| Access group             | Policy         |
|--------------------------|----------------|
| `Administrators`         | Grant a policy for the resource group with resource group access **administrator**. Select the {{site.data.keyword.la_full_notm}} service, and select the platform role **administrator**, and the service role **manager**. |
| `Managers`               | Grant a policy for the resource group with platform role **editor**. Select the {{site.data.keyword.la_full_notm}} service, and select the platform role **editor**, and the service role **manager**. |
| `Advanced service users` | Grant a policy for the resource group with platform role **viewer**. Select the {{site.data.keyword.la_full_notm}} service, and select the platform role **viewer**, and the service role **standard member**. |
| `Users`                  | Grant a policy for the resource group with platform role **viewer**. Select the {{site.data.keyword.la_full_notm}} service, and select the platform role **viewer**, and the service role **reader**. |
{: caption="Table 2. Roles per access group policy" caption-side="top"} 

**Every user that requires permissions to work with the {{site.data.keyword.la_full_notm}} service in your account must be assigned a resource group policy that includes the permissions for the {{site.data.keyword.la_full_notm}} service.**
{: note}

You can assign a single policy to the access group instead of assigning the same access multiple times per individual user or service ID. 

**Add users and service IDs to an access group. Grant permissions to these users and service IDs through the access group.**
{: note}

[Learn more](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam).



## Restrict access to manage and view the data
{: #compliance_hipaa_archive}





