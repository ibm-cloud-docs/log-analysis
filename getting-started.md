---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-17"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Getting started with {{site.data.keyword.la_full_notm}}
{: #getting-started}

Use {{site.data.keyword.la_full}} to add log management capabilities to your {{site.data.keyword.cloud_notm}} architecture.
{: shortdesc}

<!-- common deprecation notice -->
{{_include-segments/deprecation_notice.md}}

You can use {{site.data.keyword.la_full_notm}} to manage operating system logs, application logs, and platform logs in the {{site.data.keyword.cloud_notm}}. {{site.data.keyword.la_full_notm}} offers administrators, DevOps teams, and developers advanced features to filter, search, and tail log data, define alerts, and design custom views to monitor application and system logs.



## Step 1. Before you begin
{: #getting-started-prereqs}

1. [Check the regions where the {{site.data.keyword.la_full_notm}} service is available](/docs/log-analysis?topic=log-analysis-regions).

2. If you don't have an {{site.data.keyword.cloud_notm}} account, [register an {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}. You need an IBMid to work in {{site.data.keyword.cloud_notm}}.

## Step 2. Provision an instance
{: #getting-started-provision}

1. Log in to your {{site.data.keyword.cloud_notm}} account.

   Click [Log in to {{site.data.keyword.cloud_notm}}](https://cloud.ibm.com/login){: external} to sign in to the {{site.data.keyword.cloud_notm}}.

   After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} console opens.

2. Click **Catalog**. The list of the services that are available in {{site.data.keyword.cloud_notm}} opens.

3. To filter the list of services that is displayed, click **Services** and select the **Logging and Monitoring** category.

4. Click the **{{site.data.keyword.la_full_notm}}** tile.

5. Select a region for the service instance.

6. Select the **Lite** service plan.

   By default, the **Lite** plan is set.

   For more information about other service plans, see [Pricing plans](/docs/log-analysis?topic=log-analysis-service_plans).

7. Specify a **Service name** for your {{site.data.keyword.la_full_notm}} service instance.

8. Select the **Default** resource group.

   By default, the **Default** resource group is set.

9. To provision the {{site.data.keyword.la_full_notm}} service in the {{site.data.keyword.cloud_notm}} selected resource group, click **Create**.

After you provision an instance, the {{site.data.keyword.la_full_notm}} dashboard opens.

To provision an instance of logging through the CLI, see [Provisioning logging through the {{site.data.keyword.cloud_notm}} CLI](/docs/log-analysis?topic=log-analysis-provision#provision_cli).
{: note}

## Step 3. Choose your logging source
{: #getting-started-step2}

Choose a source for your log data. Then, complete the steps:

| Log source | Steps |
|------------|-------------|
| {{site.data.keyword.cloud_notm}} service | [Configuring {{site.data.keyword.cloud_notm}} platform logs](/docs/log-analysis?topic=log-analysis-config_svc_logs) |
| Standard Kubernetes cluster | [Collecting and analyzing logs from a Kubernetes cluster](/docs/log-analysis?topic=log-analysis-kube#kube) |
| Linux | [Collecting and analyzing logs from a Linux environment](/docs/log-analysis?topic=log-analysis-ubuntu#ubuntu) |
| Windows Server | [Collecting and analyzing logs from Windows Server systems](/docs/log-analysis?topic=log-analysis-windows_serv) |
{: caption="Table 1. Tutorials to get started working with the {{site.data.keyword.la_full_notm}} service" caption-side="top"}


## Step 3. Upgrade the plan
{: #getting-started-step3}

By upgrading your plan, you can enable additional logging features.

Upgrade the {{site.data.keyword.la_full_notm}} service plan to a paid plan to be able to [filter logs](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step5), [search logs](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step6), [define views](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step7), and [configure alerts](/docs/log-analysis?topic=log-analysis-alerts). For more information about {{site.data.keyword.la_full_notm}} service plans, see [Pricing plans](/docs/log-analysis?topic=log-analysis-service_plans).



## Step 4. Manage logs
{: #getting-started-step4}

To start managing logs, complete the following steps:

1. [Launch the logging web UI](/docs/log-analysis?topic=log-analysis-launch).

2. [View and manage your logs](/docs/log-analysis?topic=log-analysis-view_logs).


## Step 5. Next steps
{: #getting-started-step5}

Next, you can manage user access with IAM.

Identify the IAM policies that a user needs to work with the {{site.data.keyword.la_full_notm}} service.

To learn more about IAM integration with the {{site.data.keyword.la_full_notm}} service, see [Managing IAM policies and access groups](/docs/log-analysis?topic=log-analysis-work_iam).
