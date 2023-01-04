---

copyright:
  years:  2018, 2023
lastupdated: "2022-02-21"

keywords: IBM, Log Analysis, logging, infrastructure

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Logging with infrastructure overview
{: #infra_logging}

In {{site.data.keyword.la_short}}, you can send infrastructure logs to an {{site.data.keyword.la_full_notm}} instance from a broad range of sources:
{: shortdesc}


## Logging with Cloud Foundry
{: #infra_logging_cf}


In {{site.data.keyword.cloud}} public, you can monitor logs from Cloud Foundry (CF) resources that run in the {{site.data.keyword.cloud_notm}} or outside the {{site.data.keyword.cloud_notm}} by using the {{site.data.keyword.la_full_notm}} service.

If your CF resources run on {{site.data.keyword.cloud_notm}} public, you can choose to automatically collect these logs and monitor them through the {{site.data.keyword.la_full_notm}} instance that is provisioned in the same region, and that is enabled to host service platform logs. Alternatively, you can choose to configure a custom user provided (CUPS) service for your app, so system and application logs are collected and streamed to a custom logging instance.

If your CF resources run on {{site.data.keyword.cloud_notm}} dedicated or outside the {{site.data.keyword.cloud_notm}}, you can configure a custom user provided (CUPS) service for your app, so system and application logs are collected and streamed to a custom logging instance.

|                          |
|--------------------------|
| ![Monitor CF resources in IBM Cloud Public](../images/components-cf-public.png "Monitor CF resources in IBM Cloud Public") |
{: caption="Methods that can be adopted to monitor CF resource logs in {{site.data.keyword.cloud_notm}} public" caption-side="top"}
{: #end-api-img-2}
{: tab-title="Monitor CF resources in IBM Cloud Public"}
{: tab-group="cf-img"}
{: class="simple-tab-table"}

|                          |
|--------------------------|
| ![Monitor CF resources in IBM Cloud Dedicated](../images/components-cf-dedicated.png "Monitor CF resources in IBM Cloud Dedicated") |
{: caption="Methods that can be adopted to monitor CF resource logs in {{site.data.keyword.cloud_notm}} dedicated" caption-side="top"}
{: #end-api-img-1}
{: tab-title="Monitor CF resources in IBM Cloud Dedicated"}
{: tab-group="cf-img"}
{: class="simple-tab-table"}

|                          |
|--------------------------|
| ![Monitor CF resources outside the IBM Cloud Public](../images/components-cf-outside-ibm-cloud.png "Monitor CF resources outside the IBM Cloud Public") |
{: caption="Methods that can be adopted to monitor CF resource logs outside the {{site.data.keyword.cloud_notm}}" caption-side="top"}
{: #end-api-img-3}
{: tab-title="Monitor CF resources outside the IBM Cloud Public"}
{: tab-group="cf-img"}
{: class="simple-tab-table"}

For more information, see [Logging with Cloud Foundry](/docs/log-analysis?topic=log-analysis-monitor_cfapp_logs).


## Logging with Kubernetes clusters
{: #infra_logging_cluster}

You can configure a logging agent to collect logs from a Kubernetes cluster and forward them to an instance of the {{site.data.keyword.la_full_notm}} service.

You can collect and monitor logs from a Kubernetes cluster that is located in the same {{site.data.keyword.cloud_notm}} region as your {{site.data.keyword.la_full_notm}} instance or in a different one. You can also collect and monitor logs from clusters that are located outside the {{site.data.keyword.cloud_notm}}.

To configure cluster-level logging for a Kubernetes cluster, you must complete the following steps:

1. Provision an instance of the {{site.data.keyword.la_full_notm}} service. With this step, you configure a centralized log management system where log data is hosted on {{site.data.keyword.cloud_notm}}.
2. Provision a cluster, for example, a standard cluster on the {{site.data.keyword.containerlong_notm}}.
3. Deploy and configure the logging agent in the cluster.

![Log Analysis component overview on the {{site.data.keyword.cloud_notm}}](../images/kube.png "Log Analysis component overview on the {{site.data.keyword.cloud_notm}}"){: caption="Log Analysis component overview on the {{site.data.keyword.cloud_notm}} for Kubernetes" caption-side="bottom"}

If you choose to send your Cloud Foundry logs by configuring a custom user provided (CUPS) service for your app, you must enable a port to send logs via syslog to your logging instance. If you are using (a) the classic syslog protocol, (b) a custom port in syslog-ng, or (c) a custom port in rsyslog, there is no authentication available and anyone with knowledge of the endpoint can submit logs to your instance. As a result, depending on your environment, your use of the classic syslog protocol or custom port configurations with `syslog-ng` or `rsyslog` may present a significant security risk.  Use these configurations at your organization's own risk.  Validate with your compliance and security teams whether this security risk is acceptable to your organization.
{: important}

For more information, see [Logging with Kubernetes clusters](/docs/log-analysis?topic=log-analysis-kube).


## Logging with Bare metal
{: #infra_logging_bm}

You can use the {{site.data.keyword.la_full}} service to monitor and manage logs from a bare metal in a centralized logging system on the {{site.data.keyword.cloud_notm}}. You can collect and monitor system and application logs.

By default, the logging agent on Linux servers monitors log files in the `/var/log` directory. For example, the Ubuntu system log (`/var/log/syslog`) is monitored by default.

On the {{site.data.keyword.cloud_notm}}, you can configure an bare metal to forward logs to an {{site.data.keyword.la_full_notm}} instance by completing the following steps:

1. Provision a bare metal running Ubuntu Linux.
2. Provision an instance of the {{site.data.keyword.la_full_notm}} service.
3. Configure the logging agent in the bare metal.
4. Optionally, add additional directories to be monitored by the agent.

![Component overview on the {{site.data.keyword.cloud_notm}}](../images/ubuntu.png "Component overview on the {{site.data.keyword.cloud_notm}}"){: caption="Log Analysis component overview on the {{site.data.keyword.cloud_notm}} for bare metal" caption-side="bottom"}

For more information, see [Logging with Bare metals](/docs/log-analysis?topic=log-analysis-ubuntu_baremetal).


## Logging with Linux VPC instances
{: #infra_logging_vpc}

You can use the {{site.data.keyword.la_full}} service to monitor and manage logs from a Linux VPC server instance in a centralized logging system on the {{site.data.keyword.cloud_notm}}. You can collect and monitor system and application logs.

By default, the logging agent for Linux VPC instances monitors log files in the `/var/log` directory. For example, the Ubuntu system log (`/var/log/syslog`) is monitored by default.

On the {{site.data.keyword.cloud_notm}}, you can configure a Linux VPC server to forward logs to an {{site.data.keyword.la_full_notm}} instance by completing the following steps:

1. Provision a VPC running Ubuntu Linux for example.
2. Provision an instance of the {{site.data.keyword.la_full_notm}} service.
3. Configure the logging agent in the Ubuntu server.
4. Optionally, add additional directories to be monitored by the agent.

![Component overview on the {{site.data.keyword.cloud_notm}}](../images/ubuntu.png "Component overview on the {{site.data.keyword.cloud_notm}}"){: caption="Log Analysis component overview on the {{site.data.keyword.cloud_notm}} for Ubuntu Linux" caption-side="bottom"}

For more information, see [Logging with Linux VPC server instances](/docs/log-analysis?topic=log-analysis-ubuntu).

## Logging with Syslog
{: #infra_logging_syslog}

You can send logs to an {{site.data.keyword.la_full_notm}} instance via Syslog. TCP and TCP+TLS are both supported.

To configure syslog, you must enable a port to send logs via syslog to your logging instance. If you are using (a) the classic syslog protocol, (b) a custom port in syslog-ng, or (c) a custom port in rsyslog, there is no authentication available and anyone with knowledge of the endpoint can submit logs to your instance.  Depending on your environment, this may present a significant security risk. Use these configurations at your organization’s own risk.  Validate with your compliance and security teams whether this security risk is acceptable to your organization.
{: important}

To use a custom port to send logs via UDP, you can open an IBM support ticket. For information about opening an IBM support ticket, or about support levels and ticket severities, see [Getting support](/docs/get-support).

For more information on using Syslog, see [Logging with Syslog](/docs/log-analysis?topic=log-analysis-syslog).

## Logging with Windows systems
{: #infra_logging_windows}

You can use the {{site.data.keyword.la_full}} service to monitor and manage logs from Windows systems.

NXLog is used to provide log files to {{site.data.keyword.la_full}}.

To configure NXLog, you must enable a port to send logs via syslog to your logging instance. If you are using (a) the classic syslog protocol, (b) a custom port in `syslog-ng`, or (c) a custom port in `rsyslog`, there is no authentication available and anyone with knowledge of the endpoint can submit logs to your instance. As a result, depending on your environment, your use of the classic syslog protocol or custom port configurations with `syslog-ng` or `rsyslog` may present a significant security risk.  Use these configurations at your organization's own risk.  Validate with your compliance and security teams whether this security risk is acceptable to your organization.
{: important}

By default, NXLog monitors log files in the `C:\\ProgramData\\logs` directory.

On the {{site.data.keyword.cloud_notm}}, configure an Windows server to forward logs to an {{site.data.keyword.la_full_notm}} instance by completing the following steps:

1. Provision an instance of the {{site.data.keyword.la_full_notm}} service.
2. Configure NXLog on the Windows server.
3. Optionally, add additional directories to be monitored by the agent.

![Component overview on the {{site.data.keyword.cloud_notm}}](../images/windows.svg "Component overview on the {{site.data.keyword.cloud_notm}}"){: caption="Log Analysis component overview on the {{site.data.keyword.cloud_notm}} for Windows" caption-side="bottom"}

For more information on logging from Windows systems, see the following:

* [Logging from a Windows client](/docs/log-analysis?topic=log-analysis-windows)
* [Logging from Windows Server systems](/docs/log-analysis?topic=log-analysis-windows_serv)
* [Logging with Windows VPC server instances](/docs/log-analysis?topic=log-analysis-windows_vpc_tutorial)
