---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Logging agent for Linux
{: #agent_linux}

The Linux logging agent collects and forwards Linux logs to your {{site.data.keyword.la_full_notm}} instance. After you provision an {{site.data.keyword.la_full}} instance, you must configure a logging agent for each log source that you want to monitor.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

By default, the logging agent monitors all files with extension *.log*, and extensionless files under */var/log/*.

The logging agent tails for new log data, and looks for new files that are added to the logging directories that the agent monitors.

Before you begin, understand the [agent storage requirements.](/docs/log-analysis?topic=log-analysis-agent_storage)


## Linux image versions
{: #log_analysis_dna_agent_image_linux_versions}

Logging agent images for Linux are public images that are available in the logging repo `https://assets.logdna.com`.

The following table outlines the agent versions that are available:

| Linux                                 | Logging agent V1 | Logging agent V2  | Logging agent V3 |
|---------------------------------------|------------------|-------------------|------------------|
| `Linux`   | ![Checkmark icon](../images/checkmark-icon.svg)  | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
{: caption="Table 3. Logging agent versions for Linux" caption-side="top"}



## Connecting a logging agent with a logging instance
{: #log_analysis_agent_image_linux_connect}

The logging agent is responsible for collecting and forwarding system-level, and file-based logs to your {{site.data.keyword.la_full_notm}} instance.

To connect your Linux server to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install a *logging-agent*.

- The logging agent reads log files from */var/log*, and forwards the log data to your logging instance.

To connect an agent to a Linux platform, choose 1 of the following options:
- [Configuring a Logging agent for Linux Ubuntu or Debian](/docs/log-analysis?topic=log-analysis-config_agent_linux).
- [Configuring a Logging agent for a Linux RPM](/docs/log-analysis?topic=log-analysis-config_agent_linux_rpm)

## Configuration the agent
{: #linux_agent_config}

You can customize a logging agent by [configuring parameters](/docs/log-analysis?topic=log-analysis-log_analysis_agent_configure) for Linux agents.
