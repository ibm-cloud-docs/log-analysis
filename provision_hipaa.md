---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, overview

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}


# Provisioning a HIPAA compliance instance
{: #provision_hipaa}

Across every industry, organizations require tighter controls and visibility into where their data is stored and processed in the {{site.data.keyword.cloud}}. To manage logs for HIPAA resources by using the {{site.data.keyword.la_full_notm}} service, consider the following information:
{: shortdesc}


{{_include-segments/deprecation_notice.md}}

HIPAA compliance is a shared responsibility. {{site.data.keyword.IBM_notm}} only provides the security and the tools to ensure its cloud platform can be used without violating HIPAA rules. It is the responsibility of HIPAA-covered entities to ensure that cloud-based infrastructure and applications are not misconfigured, and that stored files are appropriately secured.
{: important}

## Step 1. Enable the HIPAA supported settings in your account
{: #compliance_hipaa_supported}

If you're the account owner, you can enable your {{site.data.keyword.cloud}} account to be HIPAA supported. You might choose to enable the **HIPAA Supported setting** if you plan to include Protected Health Information (PHI) in HIPAA-enabled services.

The US Health Insurance Portability and Accountability Act (HIPAA) and the Health Information Technology for Economic and Clinical Health (HITECH) Act define standards for handling electronic healthcare transactions and information. If you or your company is a covered entity as defined by HIPAA, you must enable the HIPAA Supported setting if you run sensitive workloads that are regulated under HIPAA and the HITECH Act. Learn more about {{site.data.keyword.cloud_notm}} compliance in [Compliance on the {{site.data.keyword.cloud_notm}}.](https://www.ibm.com/cloud/compliance){: external}

Enabling this setting has the following effects:

* Enables you to filter on HIPAA Enabled services in the catalog
* Indicates to IBM that your account stores protected health information (PHI)
* Digitally accepts the IBM Business Associate Addendum (BAA) for covered entities

Enable this setting only if you or your company is a covered entity as defined by HIPAA. If you or your company is a business associate of a covered entity, [contact {{site.data.keyword.cloud_notm}} Sales](https://www.ibm.com/account/reg/us-en/signup?formid=MAIL-wcp){: external} to accept the applicable BAA. For more information about HIPAA definitions of covered entities and business associates, see the [US Department of Health & Human Services](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html){: external} website.
{: important}

Accounts that enable the **HIPAA Supported setting** still have access to the full catalog of services.


## Step 2. Provision your {{site.data.keyword.la_full_notm}} instances with the HIPAA service plan
{: #compliance_hipaa_provision}

The HIPAA plan allows a maximum of 25 team members per instance. If you need to grant permissions to more than 25 users, [open a support ticket](/docs/get-support).
{: note}


Choose any of the following methods to provision an instance of the {{site.data.keyword.la_full_notm}} service:
[Provisioning an instance through the Observability dashboard](/docs/log-analysis?topic=log-analysis-provision#provision_ui)
[Provisioning an instance through the catalog](/docs/log-analysis?topic=log-analysis-provision#provision_catalog)
[Provisioning an instance through the CLI](/docs/log-analysis?topic=log-analysis-provision#provision_cli)

Make sure that your naming convention for {{site.data.keyword.la_full_notm}} instances does not include PII information. Choose the **HIPAA service plan** for your logging instances.
{: important}


### Step 3. Label your service (optional)
{: #compliance_hipaa_provision_tag}

Set the tag **HIPAA** to the {{site.data.keyword.la_full_notm}} instances that you provision in your account.

Complete the following steps:

1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.
2. Click the **Menu** icon ![Menu icon](../icons/icon_hamburger.svg) &gt; **Resource List** to view your list of resources.
3. In the *Services* section, identify the instance that you want to tag.
4. Click the **Actions** icon ![Actions icon](../icons/action-menu-icon.svg). Select **Add tags** or **Edit tags**.
5. Enter the tag **HIPAA**.
6. Click **Save**.

## Next steps
{: #compliance_hipaa_iam}

Restrict access to manage and view the data. [Learn more](/docs/log-analysis?topic=log-analysis-work_iam)
.
