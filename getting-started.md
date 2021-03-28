---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: LogDNA, IBM, Log Analysis, logging, getting started

subcollection: Log-Analysis-with-LogDNA

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
{:external: target="_blank" .external}

# Getting started tutorial
{: #getting-started}

Use {{site.data.keyword.la_full}} to add log management capabilities to your {{site.data.keyword.cloud_notm}} architecture. {{site.data.keyword.la_full_notm}} is operated by logging in partnership with {{site.data.keyword.IBM_notm}}.
{:shortdesc}

You can use {{site.data.keyword.la_full_notm}} to manage system and application logs in the {{site.data.keyword.cloud_notm}}.

{{site.data.keyword.la_full_notm}} offers administrators, DevOps teams, and developers advanced features to filter, search, and tail log data, define alerts, and design custom views to monitor application and system logs.

## Features
{: #getting-started_features}

{{site.data.keyword.la_full_notm}} provides the following features.

### Troubleshooting logs in real time to diagnose issues and identify problems

By using the *live streaming tail* feature, developers and DevOps teams can diagnose issues, analyze stack traces and exceptions, identify the source of errors, and monitor different log sources through a single view. 

### Issuing alerts to be notified of important actions
 
DevOps teams can configure the system so critical or warning alert notifications are sent to email, Slack, webHook, or PagerDuty.  This helps DevOps teams to act promptly on important application and services events.

### Exporting logs to a local file for analysis or to an archive service to meet auditing requirements

You can export specific log lines to a local copy or archive logs from {{site.data.keyword.la_full_notm}} to {{site.data.keyword.cloud}} Object Storage.
Log lines are exported in JSON line format. Logs are archived in JSON format with the metadata that is associated with each line. 

### Controlling logging infrastructure costs by customizing {{site.data.keyword.la_full_notm}} managed logs

You can control the cost of your {{site.data.keyword.cloud_notm}} logging infrastructure by configuring the log sources that are collecting and managing logs. 


## Overview
{: #getting-started_ov}

{{site.data.keyword.la_full_notm}} is a service hosted on the {{site.data.keyword.cloud_notm}} and operated by LogDNA.  The log data is stored on the {{site.data.keyword.cloud_notm}}.

Because {{site.data.keyword.la_full_notm}} is part of the {{site.data.keyword.cloud_notm}} users must have the following permissions:

* Your users must have platform permissions to create, view, and delete an instance of a service in the {{site.data.keyword.cloud_notm}}.
* Your users must have platform permissions to create resources within the context of the resource group where the logging instance is provisioned.

To add logging features with logging in the {{site.data.keyword.cloud_notm}}, you must provision an instance of {{site.data.keyword.la_full_notm}}.

An {{site.data.keyword.la_full_notm}} instance is provisioned within the context of a resource group. Your services are organized for access control and billing purposes by using resource groups. You can provision the instance in the *default* resource group or in a custom resource group.

After provisioning an instance of {{site.data.keyword.la_full_notm}}, an account is created in LogDNA, and you receive the ingestion key for your account.

After you have your ingestion key, you can configure your log sources:

* You can enable a logging instance per region to host logs from enabled {{site.data.keyword.cloud_notm}} services. For example, to collect logs from an {{site.data.keyword.ibmcf_notm}} app, you can enable the *service platform logs* flag. [Learn more](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-config_svc_logs). When this feature is enabled, logs are collected automatically.
* You can configure a logging agent for a log source. A log source is a Cloud or on-prem resource that generates logs. For example, a log source can be a Kubernetes cluster. You use the ingestion key to configure the logging agent that is responsible for collecting and forwarding logs to your {{site.data.keyword.la_full_notm}} instance. After the logging agent is deployed in a log source, logs are collected and forwarded automatically to the {{site.data.keyword.la_full_notm}} instance. [Learn more](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-logdna_agent).

You can launch the {{site.data.keyword.la_full_notm}} Web UI to view, monitor, and manage your logs from the {{site.data.keyword.cloud_notm}} Menu ![Navigation Menu](images/icon_hamburger.svg) &gt; **Observability** &gt; **Logging** page.

The following figure shows the components comprising the {{site.data.keyword.la_full_notm}} service that is running on {{site.data.keyword.cloud_notm}}:

![{{site.data.keyword.la_full_notm}}](images/Logging-arch.png "{{site.data.keyword.la_full_notm}} high level architecture")



## Step 1. Before you begin
{: #getting-started_prereqs}

1. [Check the regions where the {{site.data.keyword.la_full_notm}} service is available](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-regions).

2. If you don't have an {{site.data.keyword.cloud_notm}} account, [register an {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}. You need an IBMid to work in {{site.data.keyword.cloud_notm}}.

## Step 2. Get started
{: #getting-started_step2}

Choose a log resource. Then, complete the get started section:

| Log source | Get started | 
|------------|-------------|
| {{site.data.keyword.cloud_notm}} service | [Collecting and analyzing logs from {{site.data.keyword.cloud_notm}} service logs in your account](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-config_svc_logs) |
| Standard Kubernetes cluster | [Collecting and analyzing logs from a Kubernetes cluster](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-kube#kube) |
| Linux Ubuntu </br>Linux Debian | [Collecting and analyzing logs from a Linux environment](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-ubuntu#ubuntu) |
| Cloud Foundry `[1]` | [Collecting and analyzing logs from CF resources](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-monitor_cfapp_logs) |
{: caption="Table 1. Tutorials to get started working with the {{site.data.keyword.la_full_notm}} service" caption-side="top"}

`[1]` If your CF resources run on {{site.data.keyword.cloud_notm}} public, you can choose to automatically collect these logs and monitor them through the {{site.data.keyword.la_full_notm}} instance that is provisioned in the same region, and that is enabled to host platform logs. Alternatively, you can choose to configure a custom user provided (CUPS) service for your app, so system and application logs are collected and streamed to a custom logging instance.


## Step 3. Upgrade the plan
{: #getting-started_step3}

Enable more logging features.

Upgrade the {{site.data.keyword.la_full_notm}} service plan to a paid plan to be able to [filter logs](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-view_logs#view_logs_step5), [search logs](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-view_logs#view_logs_step6), [define views](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-view_logs#view_logs_step7), and [configure alerts](https://docs.logdna.com/docs/alerts). For more information about {{site.data.keyword.la_full_notm}} service plans, see [Pricing plans](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-service_plans).



## Step 4. Manage logs
{: #getting-started_step4}

Complete the following steps:

1. [Launch the logging web UI](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-launch).

2. [Manage logs](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-view_logs).


## Step 5. Next steps 
{: #getting-started_step5}

Next, you can manage user access with IAM.

Identify the IAM policies that a user needs to work with the {{site.data.keyword.la_full_notm}} service.

To learn more about IAM integration with the {{site.data.keyword.la_full_notm}} service, see [Managing IAM policies and access groups](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-work_iam).

For example, choose one user role to learn how to grant permissions to that user to work with the {{site.data.keyword.la_full_notm}} service. 

| User role in the {{site.data.keyword.cloud_notm}} | For more information                     |
|-----------------------------------------------------|------------------------------------------|
| Account owner                                       | [Granting permissions to a user to become an administrator of the service in the {{site.data.keyword.cloud_notm}} account](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-work_iam#admin_account) |
| Platform service administrator in the account       | [Granting permissions to a user to become an administrator of the service in the {{site.data.keyword.cloud_notm}} account](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-work_iam#admin_account) |
| Platform service administrator in a resource group  | [Granting permissions to a user to become an administrator of the service within a resource group](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-work_iam#admin_rg) |
| Platform DevOps operator in the account           | [Granting permissions to a DevOps user to manage the service in the {{site.data.keyword.cloud_notm}} account](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-work_iam#devops_account) |
| Platform DevOps operator in a resource group        | [Granting permissions to a DevOps user to manage the service within a resource group](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-work_iam#devops_rg) |
| Service administrator in logging                     | [Granting permissions to manage logs and configure alerts in LogDNA](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-work_iam#admin_user_logdna)              |
| User / Developer                                    | [Granting permissions to a user to view and manage logs in LogDNA](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-work_iam#user_logdna)               |
{: caption="Table 2. Cloud roles in the {{site.data.keyword.cloud_notm}}" caption-side="top"}


