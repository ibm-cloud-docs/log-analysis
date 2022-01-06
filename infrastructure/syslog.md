---

copyright:
  years:  2018, 2022
lastupdated: "2021-04-12"

keywords: IBM, Log Analysis, logging, ingestion, python

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

 
# Logging with Syslog
{: #syslog}

You can send logs to an {{site.data.keyword.la_full_notm}} instance via Syslog. TCP and TCP+TLS are both supported.
{: shortdesc}

To use a custom port to send logs via UDP, you can open an IBM support ticket. For information about opening an IBM support ticket, or about support levels and ticket severities, see [Getting support](/docs/get-support).
{: note}

Complete the following steps to send logs:


## Before you begin
{: #syslog_prereqs}

Use a user ID that is a member or an owner of an {{site.data.keyword.cloud_notm}} account. To get an {{site.data.keyword.cloud_notm}} user ID, go to: [Registration](https://cloud.ibm.com/login){: external}.

[Your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources](/docs/log-analysis?topic=log-analysis-work_iam). For example, to work in the US-south region and in the default resource group, you need the following permissions: 

| Resource                             | Scope of the access policy | Role    | Region    | Information                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Resource group **Default**           |  Resource group            | Viewer  | us-south  | This policy is required to allow the user to see service instances in the Default resource group.    |
| {{site.data.keyword.la_full_notm}} service |  Resource group      | Editor  | us-south  | This policy is required to allow the user to provision and administer the {{site.data.keyword.la_full_notm}} service in the Default resource group.   |
{: caption="Table 1. List of IAM policies" caption-side="top"} 

## Step 1. Provision an {{site.data.keyword.la_full_notm}} instance
{: #syslog_step1}

To provision a service instance of {{site.data.keyword.la_full_notm}} through the {{site.data.keyword.cloud_notm}} console, see [Provisioning an instance](/docs/log-analysis?topic=log-analysis-provision).

## Step 2. Provision a syslog port in the logging instance
{: #syslog_step2}

1. [Launch the logging web UI.](/docs/log-analysis?topic=log-analysis-launch)

    You launch the web UI within the context of an {{site.data.keyword.la_full_notm}} instance, from the {{site.data.keyword.cloud_notm}} UI. 

2. Provision a port. From the logging web UI, complete the following steps:

    1. Open the log sources panel on the logging web UI. Select the *Install instructions icon*: ![Install instructions icon](../images/logdna_install.png "Install instructions icon")

    2. Select **Via Syslog** &gt; **Syslog**.

    3. Follow the provided instructions.

    A syslog URL for TCP streams and a URL for UDP streams is provisioned for the instance.


## Step 3. Configure syslog.conf
{: #syslog_step3}

Add the following entry to your /etc/syslog.conf:

- For TCP ingestion, add the following line:

    ```text
    *.* @syslog-a.us-south.logging.cloud.ibm.com:<PORT>
    ```
    {: codeblock}

- For UDP ingestion, add the following line:

    ```text
    *.* @syslog-u.us-south.logging.cloud.ibm.com:<PORT>
    ```
    {: codeblock}









