---

copyright:
  years:  2018, 2020
lastupdated: "2020-05-11"

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

* You can configure a LogDNA agent to connect to an {{site.data.keyword.la_full_notm}} instance through the public network or through the private network. By default, the agent connects through the public network. To connect to {{site.data.keyword.cloud}} services over a private network, you must have access to the classic infrastructure and [enable virtual routing and forwarding (VRF)](/docs/account?topic=account-vrf-service-endpoint) and connectivity to service endpoints for your account.
* The LogDNA agent authenticates by using the LogDNA ingestion key and opens a secure web socket to the {{site.data.keyword.la_full_notm}} ingestion servers.
* The LogDNA agent for Kubernetes automatically collects STDOUT and STDERR logs.
* By default, the LogDNA agent monitors all files with extension *.log*, and extensionless files under */var/log/*.
* The LogDNA agent tails for new log data, and looks for new files that are added to the logging directories that the agent monitors.


## Connecting a LogDNA agent with a LogDNA instance 
{: #logdna_agent_connect}

The LogDNA agent is responsible for collecting and forwarding system-level, and file-based logs to your {{site.data.keyword.la_full_notm}} instance. 
* To connect your Kubernetes cluster to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install a *logdna-agent* pod on each node of your cluster. The LogDNA agent reads log files from the pod where it is installed, and forwards the log data to your LogDNA instance.
* To connect your Linux server to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install a `logdna-agent`. The LogDNA agent reads log files from */var/log*, and forwards the log data to your LogDNA instance. 


The following table outlines the LogDNA agent versions that are available and supported per platform:

| Platform                       | How to install and configure |
|--------------------------------|------------------------------|
| `Standard Kubernetes cluster`  | [Configuring a LogDNA agent for a standard Kubernetes cluster](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-config_agent_kube_cluster) |
| `OpenShift Kubernetes cluster` | `N/A` |
| `Linux Ubuntu or Debian`       | `N/A` |
{: caption="Table 2. LogDNA agent version 2" caption-side="top"}
{: #agent-table-3}
{: tab-title="LogDNA agent V2"}
{: tab-group="version"}
{: class="simple-tab-table"}
{: row-headers}

| Platform                       | How to install and configure |
|--------------------------------|------------------------------|
| `Standard Kubernetes cluster`  | [Configuring a LogDNA agent for a standard Kubernetes cluster](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-config_agent_kube_cluster) |
| `OpenShift Kubernetes cluster` | [Configuring a LogDNA agent for an OpenShift Kubernetes cluster](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-config_agent_os_cluster) |
| `Linux Ubuntu or Debian`       | [Configuring a LogDNA agent on Linux Ubuntu or Debian](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-config_agent_linux) |
{: caption="Table 3. LogDNA agent version 1" caption-side="top"}
{: #agent-table-3}
{: tab-title="LogDNA agent V1"}
{: tab-group="version"}
{: class="simple-tab-table"}
{: row-headers}

The LogDNA Agent v2 is available only for Kubernetes 1.9+.
{: important}



## Configuring a LogDNA agent
{: #logdna_agent_configure}

You can configure the following parameters through the LogDNA agent:
Configuration options for the LogDNA agent V1
Configuration is done through environment variables which are found in the env section of your LogDNA Agent's Kubernetes YAML.

| Parameter | Description | LogDNA agent V1 | LogDNA agent V2 |
|-----------|-------------|-----------------|-----------------|
| `tags`    | Define tags to group hosts automatically into dynamic groups. | ![Checkmark icon](../../icons/checkmark-icon.svg)  | `N/A`|
| `logdir`  | Define custom paths that you want the agent to monitor. </br>Separate multiple paths by using commas. You can use glob patterns. You can configure specific files. Enter glob patterns by using double quotation marks. | ![Checkmark icon](../../icons/checkmark-icon.svg)  | `N/A`|
| `exclude` | Define the files that you do not want the LogDNA agent to monitor. **Note:** These files can be located in any of the paths that are defined through the logdir parameter. </br>Separate multiple files by using commas. You can use glob patterns. You can configure specific files. | ![Checkmark icon](../../icons/checkmark-icon.svg)  | `N/A`|
| `exclude_regex` | Define regex patterns to filter out any lines that match the pattern. Do not include leading and trailing `/`. | ![Checkmark icon](../../icons/checkmark-icon.svg)  | `N/A`|
| `hostname` | Define the hostname. This value overrides the operating system hostname. | ![Checkmark icon](../../icons/checkmark-icon.svg)  | `N/A`|
| `autoupdate` | Set to `1` to update the agent automatically when the public repo agent definition is updated. Set to `0` to disable this feature. |   ![Checkmark icon](../../icons/checkmark-icon.svg)  | `N/A`|
{: caption="Table 4. Configuration options for the LogDNA agent V1" caption-side="top"}
{: #agent-table-4}
{: tab-title="Linux"}
{: tab-group="tags"}
{: class="simple-tab-table"}
{: row-headers}

| Parameter | Description | Sample value                     | LogDNA agent V1 | LogDNA agent V2 |
|-----------|-------------|----------------------------------|-----------------|-----------------|
| `LOGDNA_HOST` | LogDNA instance name. </br> The default value is `logs.logdna.com`.  | `MyLogDNAinstance` | `N/A` | ![Checkmark icon](../../icons/checkmark-icon.svg)  |
| `LOGDNA_HOSTNAME` | Log Source name.  | `MyCluster` | `N/A` | ![Checkmark icon](../../icons/checkmark-icon.svg)  |
| `LOGDNA_ENDPOINT` | Ingestion endpoint where the agent sends logs. </br>The default value is `/logs/ingest/` | `https://logs.us-south.logging.cloud.ibm.com`  | `N/A` | ![Checkmark icon](../../icons/checkmark-icon.svg)  |
| `LOGDNA_INGESTION_KEY` | LogDNA ingestion key.  | | `N/A` | ![Checkmark icon](../../icons/checkmark-icon.svg)  |
| `LOGDNA_LOG_DIRS` | Defines custom paths that you want the agent to monitor. </br>Separate multiple paths by using commas. </br>You can use glob patterns. Use double quotation marks to add a globe pattern. </br>By default, everything under `/var/log` is sent to the LogDNA instance.  | `/output/,/mylogs/myapplogs/` | `N/A` | ![Checkmark icon](../../icons/checkmark-icon.svg)  |
| `LOGDNA_INCLUSION_RULES` | Custom rules that you can define to configure what log files to monitor. </br>These files can be located in any of the paths that are defined through the logdir parameter. </br>You can use glob patterns. For more information, see [Glober rules ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://github.com/CJP10/globber){:new_window}   | `*.json,*.test` | `N/A` | ![Checkmark icon](../../icons/checkmark-icon.svg)  |
| `LOGDNA_INCLUSION_REGEX_RULES` | Regex custom rules that you can define to configure what log files to monitor. For more information, see [regex syntax ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://docs.rs/regex/1.2.1/regex/#syntax){:new_window} </br>These files can be located in any of the paths that are defined through the logdir parameter.  |  | `N/A` | ![Checkmark icon](../../icons/checkmark-icon.svg)  |
| `LOGDNA_EXCLUDE` | Custom rules that you can define to configure what log files to exclude from being monitored. </br>These files can be located in any of the paths that are defined through the logdir parameter. </br>Separate multiple files by using commas. You can use glob patterns. You can configure specific files. | | ![Checkmark icon](../../icons/checkmark-icon.svg)  | `Deprecated`  |
| `LOGDNA_EXCLUSION_RULES` | Custom rules that you can define to configure what log files to exclude from being monitored. </br>You can use glob patterns. For more information, see [Glober rules ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://github.com/CJP10/globber){:new_window}  | | `N/A` | ![Checkmark icon](../../icons/checkmark-icon.svg)  |
| `LOGDNA_EXCLUSION_REGEX_RULES` | Regex custom rules that you can define to configure what log files to exclude from being monitored. | `/var/log/containers/**,/var/log/pods/**`  | `N/A` | ![Checkmark icon](../../icons/checkmark-icon.svg)  |
| `LOGDNA_IP` | IP of the cluster. | `127.0.0.1`  | `N/A` | ![Checkmark icon](../../icons/checkmark-icon.svg)  |
| `LOGDNA_MAC` | MAC address of the device. |   | `N/A` | ![Checkmark icon](../../icons/checkmark-icon.svg)  | 
| `LOGDNA_USE_SSL`  | Boolean that defines whether TLS 1.2 should be used when the agent sends logs to the LogDNA instance. </br>The default value is set to `true`. |  | `N/A` | ![Checkmark icon](../../icons/checkmark-icon.svg)  |
| `LOGDNA_USE_COMPRESSION` | Boolean that defines whether compression is enabled when the agent sends logs to the LogDNA instance. </br> The default value is set to `true`. | | `N/A` | ![Checkmark icon](../../icons/checkmark-icon.svg)  |
| `LOGDNA_GZIP_LEVEL` | Compression level for gzip. </br>Valid values are: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` </br>When you set this variable to `1`, you are configuring the agent to use the fastest compression speed but at a lower ratio. When you set this variable to `9`, you are configuring the agent to use the highest compression ratio but at a lower speed. </br> The default value is set to `6`, that offers higher compression over speed. | `N/A` | ![Checkmark icon](../../icons/checkmark-icon.svg)  |
| `LOGDNA_TAGS` | Define tags to group hosts automatically into dynamic groups. | ![Checkmark icon](../../icons/checkmark-icon.svg)  | ![Checkmark icon](../../icons/checkmark-icon.svg)  |
{: caption="Table 5. Tags that are available for the LogDNA agent V2" caption-side="top"}
{: #agent-table-5}
{: tab-title="Standard Kubernetes clusters"}
{: tab-group="tags"}
{: class="simple-tab-table"}
{: row-headers}



### Adding tags
{: #logdna_agent_tags}

You can configure tags at the agent level so that all lines that are sent by this agent can be grouped automatically into a group when you filter data in a view.

* You can define multiple tags. 
* You separate tags by using commas. 
* The maximum number of characters that you can set to define multiple tags is 80 characters.

| Platform                       | How to install and configure |
|--------------------------------|------------------------------|
| `Standard Kubernetes cluster`  | [Adding tags to logs from a Kubernetes cluster](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-adding_tags#adding_tags_kube) |
| `OpenShift Kubernetes cluster` | [Configuring a LogDNA agent for an OpenShift Kubernetes cluster]() |
| `Linux Ubuntu or Debian`       | [Adding tags to logs from Linux Ubuntu or Debian](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-adding_tags#adding_tags_linux) |
{: caption="Table 6. Adding tags" caption-side="top"}


### Excluding log files
{: #logdna_agent_exclude}

You can configure a LogDNA agent to exclude logs that you do not want to monitor through the LogDNA web UI. 

* You can exclude files that are located in any of the paths that are defined through the **logdir** parameter in a Linux system or the **LOGDNA_EXCLUDE** variable in a Kubernetes cluster. 
* You can configure multiple files. You separate multiple files by using commas. 
* You can use glob patterns to define what you want to exclude. 
* You can configure specific files.

For more information, see [Excluding log files through the LogDNA agent](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-exclude_logs_from_agent).



## Detaching a LogDNA agent from a cluster
{: #logdna_agent_detach}

To stop your Kubernetes cluster from sending logs to your {{site.data.keyword.la_full_notm}} instance, you must remove the LogDNA agent from your cluster. [Learn more](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-detach_agent).

| Platform                       | How to install and configure |
|--------------------------------|------------------------------|
| `Standard Kubernetes cluster`  | [Detaching a LogDNA agent from a standard Kubernetes cluster](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-detach_agent#detach_agent_kube) |
| `OpenShift Kubernetes cluster` | [Detaching a LogDNA agent from an Openshift Kubernetes cluster](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-detach_agent#detach_agent_os) |
| `Linux Ubuntu or Debian`       | [Detaching a LogDNA agent from Linux Ubuntu or Debian]() |
{: caption="Table 7. Detaching a LogDNA agent from a cluster" caption-side="top"}


## LogDNA agent image
{: #logdna_agent_image_ov}

When you use the {{site.data.keyword.la_full}}, LogDNA agent images are public images that are available in {{site.data.keyword.cloud_notm}} through the [{{site.data.keyword.registrylong_notm}}](/docs/Registry?topic=registry-getting-started) service.

The LogDNA agent images are hosted in the {{site.data.keyword.registrylong_notm}} global repository `icr.io/ext/logdna-agent`.

To get details about the LogDNA agent images, see [Getting information about LogDNA agent images ]().

