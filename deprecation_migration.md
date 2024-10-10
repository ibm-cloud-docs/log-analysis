---

copyright:
  years:  2018, 2024
lastupdated: "2024-09-25"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Migrating from {{site.data.keyword.la_full_notm}} or {{site.data.keyword.at_full_notm}} to {{site.data.keyword.logs_full_notm}}
{: #deprecation_migration}

The {{site.data.keyword.logs_full}} migration tool is a command line tool that you can use to migrate your {{site.data.keyword.la_full_notm}} or {{site.data.keyword.at_full_notm}} instance configuration to {{site.data.keyword.logs_full_notm}}.
{: shortdesc}

For full details about the migration process and tooling, see the [{{site.data.keyword.logs_full_notm}} documentation](/docs/cloud-logs), especially the topics in these sections:

* [Migrating to {{site.data.keyword.logs_full_notm}}](/docs/cloud-logs?topic=cloud-logs-migration-intro) and the planning templates.
* [Migration tool](/docs/cloud-logs?topic=cloud-logs-migration-tool).
* The migrating topics required for your environment. For example, [Migrating instances](/docs/cloud-logs?topic=cloud-logs-migration-instance).


{{_include-segments/deprecation_notice.md}}

If you plan to migrate using the migration tool, you must do so before {{site.data.keyword.la_full}} and {{site.data.keyword.at_full_notm}} are de-provisioned and deleted on 30 March 2025.
{: important}

![Overview of migrating to {{site.data.keyword.logs_full_notm}}](/images/migration-tool.png "Overview of migrating to {{site.data.keyword.logs_full_notm}}"){: caption="Overview of migrating to {{site.data.keyword.logs_full_notm}}" caption-side="bottom"}

The tool requires minimal user interaction. {{site.data.keyword.iamshort}} authentication and APIs are used to get the details about your current {{site.data.keyword.la_full_notm}} or {{site.data.keyword.at_full_notm}} instance.

The migration tool migrates only configuration information. No data is migrated from {{site.data.keyword.la_full_notm}} or {{site.data.keyword.at_full_notm}} to {{site.data.keyword.logs_full_notm}}.
{: important}

You can use the tool to:

* Migrate {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} instance configurations.

* Migrate {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} resources such as views, dashboards, alerts, exclusion rules, archiving configuration and more.

* Migrate {{site.data.keyword.cloud_notm}} associated resources such as {{site.data.keyword.iamshort}} permissions.

* Migrate the archiving configuration that is enabled in an {{site.data.keyword.la_full_notm}} or {{site.data.keyword.at_full_notm}} instance.

The tool generates exception reports that indicate items that cannot be migrated automatically and require more migration steps. Exceptions can include:

* Resources requiring user validation before migration. Examples of these include custom catalogs and IAM permissions.

* Migrated resources that require more user tasks, such as regenerating API keys for new {{site.data.keyword.logs_full_notm}} resources.

* Resources that are not part of the migration tool, such as configuring a cross-account {{site.data.keyword.cos_full_notm}} bucket or bucket outside of {{site.data.keyword.cloud_notm}}.

Terraform artifacts can be created that can be used to create new {{site.data.keyword.logs_full_notm}} instances. Terraform on {{site.data.keyword.cloud_notm}} enables predictable and consistent creation of {{site.data.keyword.cloud_notm}} services so that you can rapidly build complex, multitier cloud environments by following Infrastructure as Code (IaC) principles. Similar to using the {{site.data.keyword.cloud_notm}} CLI or API and SDKs, you can automate the creation, update, and deletion of your {{site.data.keyword.logs_full_notm}} instances by using the HashiCorp Configuration Language (HCL).

For details about migration and the migration tool, see [Migrating to {{site.data.keyword.logs_full_notm}}](/docs/cloud-logs?topic=cloud-logs-migration-intro).
{: tip}
