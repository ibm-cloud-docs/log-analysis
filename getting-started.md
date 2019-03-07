---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-07"

keywords: LogDNA, IBM, Log Analysis, logging, getting started

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

# Getting started tutorial
{: #getting-started}

Use {{site.data.keyword.la_full}} to add log management capabilities to your {{site.data.keyword.cloud_notm}} architecture. {{site.data.keyword.la_full_notm}} is operated by LogDNA in partnership with {{site.data.keyword.IBM_notm}}.
{:shortdesc}


## Step 1. Before you begin
{: #getting-started_prereqs}

* Read about {{site.data.keyword.la_full_notm}}. For more information, see [About {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).
* Check the regions where the service is available. For more information, see [Regions](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_regions).
* Get a user ID that is a member or an owner of an {{site.data.keyword.cloud_notm}} account. 

    To get an {{site.data.keyword.cloud_notm}} user ID, click [Registration ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window}.



## Step 2. Get started
{: #getting-started_step2}

Choose a cloud resource for which you want to manage logs. Then, configure this log source so that you can monitor its logs through the {{site.data.keyword.la_full_notm}} service. The log source can be located in the same region where you provision an {{site.data.keyword.la_full_notm}} instance or in a different region.

The following table lists examples of cloud resources that you can configure to store and manage logs by using the {{site.data.keyword.la_full_notm}} service. Complete the tutorial for a resource to get started with the {{site.data.keyword.loganalysisshort}} service:

<table>
  <caption>Tutorials to get started working with the {{site.data.keyword.la_full_notm}} service </caption>
  <tr>
    <th>Resource</th>
    <th>Tutorial</th>
    <th>Environment</th>
    <th>Scenario</th>
  </tr>
  <tr>
    <td>Containers running on the {{site.data.keyword.containershort}}</td>
    <td>[Managing Kubernetes cluster logs with {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-kube#kube)</td>
    <td>{{site.data.keyword.cloud_notm}} Public </td>
    <td>![{{site.data.keyword.containershort}} and the {{site.data.keyword.la_full_notm}}](images/kube.png "{{site.data.keyword.containershort}} and the {{site.data.keyword.la_full_notm}}")</td>
  </tr>
  <tr>
    <td>Linux Ubuntu, Linux Debian</td>
    <td>[Managing Linux Ubuntu logs with {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-ubuntu#ubuntu)</td>
    <td>On premisses</td>
    <td>![Ubuntu server and the {{site.data.keyword.la_full_notm}}](images/ubuntu.png "Ubuntu server and the {{site.data.keyword.la_full_notm}}")</td>
  </tr>
</table>



## Step 3. Upgrade the plan
{: #getting-started_step3}

Enable more logging features.

Upgrade the {{site.data.keyword.la_full_notm}} service plan to a paid plan to be able to [filter logs](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5), [search logs](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6), [define views](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7), and [configure alerts](https://docs.logdna.com/docs/alerts). For more information about {{site.data.keyword.la_full_notm}} service plans, see [Pricing plans](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

## Step 4. Next steps 
{: #getting-started_iam}

Next, manage user access with IAM.

Identify the IAM policies that a user needs to work with the {{site.data.keyword.la_full_notm}} service.

To learn more about IAM integration with the {{site.data.keyword.la_full_notm}} service, see [Managing user access with IAM](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#iam).

For example, choose one user role to learn how to grant permissions to that user to work with the {{site.data.keyword.la_full_notm}} service. 

| User role in the {{site.data.keyword.cloud_notm}} | For more information                     |
|-----------------------------------------------------|------------------------------------------|
| Account owner                                       | [Granting permissions to a user to become an administrator of the service in the {{site.data.keyword.cloud_notm}} account](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account) |
| Platform service administrator in the account       | [Granting permissions to a user to become an administrator of the service in the {{site.data.keyword.cloud_notm}} account](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account) |
| Platform service administrator in a resource group  | [Granting permissions to a user to become an administrator of the service within a resource group](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_rg) |
| Platform DevOps operator in the account           | [Granting permissions to a DevOps user to manage the service in the {{site.data.keyword.cloud_notm}} account](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#devops_account) |
| Platform DevOps operator in a resource group        | [Granting permissions to a DevOps user to manage the service within a resource group](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#devops_rg) |
| Service administrator in LogDNA                     | [Granting permissions to manage logs and configure alerts in LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna)              |
| User / Developer                                    | [Granting permissions to a user to view and manage logs in LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna)               |
{: caption="Table 2. Cloud roles in the {{site.data.keyword.cloud_notm}}" caption-side="top"}


