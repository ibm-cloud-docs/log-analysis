---

copyright:
  years:  2018, 2024
lastupdated: "2024-10-29"

keywords: IBM, Log Analysis, logging, ingestion, python

subcollection: log-analysis

content-type: tutorial
account-plan: lite
completion-time: 1h

---

{{site.data.keyword.attribute-definition-list}}


# Logging with Syslog
{: #syslog}
{: toc-content-type="tutorial"}
{: toc-completion-time="1h"}

You can send logs to an {{site.data.keyword.la_full_notm}} instance via Syslog. TCP and TCP+TLS are both supported.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

To use a custom port to send logs via UDP, you can open an IBM support ticket. For information about opening an IBM support ticket, or about support levels and ticket severities, see [Creating support cases](/docs/account?topic=account-open-case&interface=ui).
{: note}

To configure syslog, you may need to enable a port to send logs via syslog to your logging instance. If you are using (a) the classic syslog protocol, (b) a custom port in `syslog-ng`, or (c) a custom port in `rsyslog`, there is no authentication available and anyone with knowledge of the endpoint can submit logs to your instance. As a result, depending on your environment, your use of the classic syslog protocol or custom port configurations with `syslog-ng` or `rsyslog` may present a significant security risk.  Use these configurations at your organization's own risk.  Validate with your compliance and security teams whether this security risk is acceptable to your organization.
{: important}

## Before you begin
{: #syslog_prereqs}

Use a user ID that is a member or an owner of an {{site.data.keyword.cloud_notm}} account. To get an {{site.data.keyword.cloud_notm}} user ID, go to: [Registration](https://cloud.ibm.com/login){: external}.

[Your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources](/docs/log-analysis?topic=log-analysis-work_iam). For example, to work in the US-south region and in the default resource group, you need the following permissions:

| Resource                             | Scope of the access policy | Role    | Region    | Information                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Resource group **Default**           |  Resource group            | Viewer  | us-south  | This policy is required to allow the user to see service instances in the Default resource group.    |
| {{site.data.keyword.la_full_notm}} service |  Resource group      | Editor  | us-south  | This policy is required to allow the user to provision and administer the {{site.data.keyword.la_full_notm}} service in the Default resource group.   |
{: caption="List of IAM policies" caption-side="top"}

## Provision an {{site.data.keyword.la_full_notm}} instance
{: #syslog_step1}
{: step}

To provision a service instance of {{site.data.keyword.la_full_notm}} through the {{site.data.keyword.cloud_notm}} console, see [Provisioning an instance](/docs/log-analysis?topic=log-analysis-provision).

## Provision a syslog port in the logging instance
{: #syslog_step2}
{: step}

1. [Launch the logging web UI.](/docs/log-analysis?topic=log-analysis-launch)

    You launch the web UI within the context of an {{site.data.keyword.la_full_notm}} instance, from the {{site.data.keyword.cloud_notm}} UI.

2. Provision a port. From the logging web UI, complete the following steps:

    1. Open the log sources panel on the logging web UI. Select the *Install instructions icon*: ![Install instructions icon](../images/logdna_install.png "Install instructions icon")

    2. Select **Via Syslog** &gt; **Syslog**.

    3. Follow the provided instructions.

    A syslog URL for TCP streams and a URL for UDP streams is provisioned for the instance.


## Configure syslog.conf
{: #syslog_step3}
{: step}

Add the following entry to your `/etc/syslog.conf` file:

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
