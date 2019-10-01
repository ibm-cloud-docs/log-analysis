---

copyright:
  years:  2018, 2019
lastupdated: "2019-09-27"

keywords: LogDNA, IBM, Log Analysis, logging, config agent

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

# LogDNA agent
{: #logdna_agent}


The LogDNA agent is responsible for collecting and forwarding logs to your {{site.data.keyword.la_full_notm}} instance. After you provision an instance of {{site.data.keyword.la_full}}, you must configure a LogDNA agent for each log source that you want to monitor.
{:shortdesc}

* The LogDNA agent authenticates by using the LogDNA Ingestion Key and opens a secure web socket to the {{site.data.keyword.la_full_notm}} ingestion servers.
* By default, the agent monitors all files with extension *.log*,  and extensionless files under */var/log/*.
* The agent tails for new log data, and looks for new files that are added to the logging directories that the agent monitors.
* To connect to {{site.data.keyword.cloud}} services over a private network, you must have access to classic infrastructure and [enable virtual routing and forwarding (VRF)](/docs/account?topic=account-vrf-service-endpoint) and connectivity to service endpoints for your account.

You can configure the following parameters through the LogDNA agent:

| Parameter | Description |
|-----------|-------------|
| `tags`    | Define tags to group hosts automatically into dynamic groups. |
| `logdir`  | Define custom paths that you want the agent to monitor. </br>Separate multiple paths by using commas. You can use glob patterns. You can configure specific files. Enter glob patterns by using double quotation marks. |
| `exclude` | Define the files that you do not want the LogDNA agent to monitor. **Note:** These files can be located in any of the paths that are defined through the logdir parameter. </br>Separate multiple files by using commas. You can use glob patterns. You can configure specific files. |
| `exclude_regex` | Define regex patterns to filter out any lines that match the pattern. Do not include leading and trailing `/`. |
| `hostname` | Define the hostname. This value overrides the operating system hostname. |
| `autoupdate` | Set to `1` to update the agent automatically when the public repo agent definition is updated. Set to `0` to disable this feature. |  
{: caption="Table 1. Parameters to customize a LogDNA agent" caption-side="top"}


## Adding tags at the LogDNA agent level
{: #logdna_agent_tags}

You can configure tags at the agent level so that all lines that are sent by this agent can be grouped automatically into a group when you filter data in a view.

* You can define multiple tags. 
* You separate tags by using commas. 
* The maximum number of characters that you can set to define multiple tags is 80 characters.

For example, choose any of the following options to find out how to configure tags:
* [Adding tags to logs from a Kubernetes cluster](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-adding_tags#adding_tags_kube)
* [Adding tags to logs from Linux Ubuntu or Debian](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-adding_tags#adding_tags_linux)


## Excluding log files through the LogDNA agent
{: #logdna_agent_exclude}

You can stop logs from being forwarded to your logging instance by modifying the LogDNA agent configuration file to exclude any files that you do not want the LogDNA agent to monitor. 

* You can exclude files that are located in any of the paths that are defined through the **logdir** parameter. 
* To define the files, you can separate multiple files by using commas. You can use glob patterns. You can also configure specific files.

For example, see [Excluding log files through the LogDNA agent](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-exclude_logs_from_agent).


