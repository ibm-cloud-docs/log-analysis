---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Configuring a logging agent
{: #log_analysis_agent_configure}

You can customize a logging agent by configuring parameters for Linux agents, or environment variables for Kubernetes agents.
{: shortdesc}

<!-- common deprecation notice -->
{{../_include-segments/deprecation_notice.md}}


## Environment variables for the V3 logging agent
{: #log_analysis_agent_configure_v3}


| Environment variable     | YAML path name | Description   |  Default value                         | Sample value          |
|--------------------------|---------------|---------------|----------------------------------------|-----------------------|
| `LOGDNA_CONFIG_FILE`      | | Default configuration file.   | `/etc/logdna/config.yaml`              |                       |
| `LOGDNA_DB_PATH` | `log.db_path` | The directory where the agent stores status information. \n  The directory must be on a persistent volume. \n The agent must have write access to the directory. | `/var/lib/logdna-agent/` | |
| `LOGDNA_INGESTION_KEY`   | `http.ingestion_key` | Reference to the logging ingestion key.                | secretKeyRef                           |                       |
| `LOGDNA_HOST`            | `http.host` | {{site.data.keyword.la_full_notm}} ingestion endpoint.                            |                                        | `logs.us-south.logging.cloud.ibm.com` |
| `LOGDNA_ENDPOINT`        | `http.endpoint` | Ingestion log path.                                   | `/logs/agent/`                         |                       |
| `LOGDNA_HOSTNAME`        | `http.params.hostname` | Log Source name.  | Machine's default OS hostname.     | `MyCluster`  |
| `LOGDNA_IP` | `http.params.ip` | IP address that is included as metadata to log lines that are forwarded from the agent. |  | |
| `LOGDNA_JOURNALD_PATHS` | `journald.paths[]` | List of journald paths that you want to monitor. |   | `/var/log/journal`, `/run/systemd/journal` |
| `LOGDNA_LOG_DIRS`        | `log.dirs[]` | Defines custom paths that you want the agent to monitor.  \n Separate multiple paths by using commas.  \n You can use glob patterns. Use double quotation marks to add a globe pattern.   | `/var/log/`   | `/output/,/mylogs/myapplogs/` |
| `LOGDNA_REDACT_REGEX` | `log.line_redact_regex` | Regex custom rules that you can define to mask sensitive information before the agent sends the log line. | | |
| `LOGDNA_LINE_INCLUSION_REGEX` | `log.line_inclusion_regex[]` | Regex custom rules that you can define to configure what log lines to monitor. \n When you set this field, the agent sends only log lines that match any of the patterns. | | |
| `LOGDNA_INCLUSION_RULES` | `log.include.glob[]` | Custom rules that you can define to configure what log files to monitor.  \n These files can be located in any of the paths that are defined through the logdir parameter.  \n You can use glob patterns. For more information, see [Glober rules](https://github.com/CJP10/globber){: external}   |  | `*.json,*.test` |
| `LOGDNA_LINE_EXCLUSION_REGEX` | `log.line_exclusion_regex[]` | Regex custom rules that you can define to configure what log files to exclude from monitoring. For more information, see [regex syntax](https://docs.rs/regex/1.2.1/regex/#syntax){: external}  \n These files can be located in any of the paths that are defined through the logdir parameter.  |  |  |
| `LOGDNA_EXCLUSION_RULES` | `log.exclude.glob[]` | Custom rules that you can define to configure what log files to exclude from being monitored.  \n You can use glob patterns. For more information, see [Glober rules](https://github.com/CJP10/globber){: external}  | | |
| `LOGDNA_EXCLUSION_REGEX_RULES` | `log.exclude.regex[]` | Regex custom rules that you can define to configure what log files to exclude from being monitored. |  | `/var/log/containers/**,/var/log/pods/**`  |
| `LOGDNA_USE_SSL`          | `http.use_ssl` | Boolean that defines whether TLS 1.2 should be used when the agent sends logs to the logging instance.  \n The default value is set to `true`.  | `true` | Valid values are `true` and `false`. |
| `LOGDNA_USE_COMPRESSION`  | `http.use_compression` | Boolean that defines whether compression is enabled when the agent sends logs to the logging instance.  \n  The default value is set to `true`. | `true` | `true` |
| `LOGDNA_GZIP_LEVEL`       | `http.gzip_level` | Compression level for gzip.  \n Valid values are: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`  \n When you set this variable to `1`, you are configuring the agent to use the fastest compression speed but at a lower ratio. When you set this variable to `9`, you are configuring the agent to use the highest compression ratio but at a lower speed.  | `2` | `6` |
| `LOGDNA_TAGS` | `http.params.tags` | Define tags to group hosts automatically into dynamic groups. |  | `prod,appA` |
| `LOGDNA_MAC` | `http.params.mac` | MAC address that is attached as metadata to log lines. |  |  |
| `LOGDNA_LOOKBACK` | `log.lookback` | Defines the lookback strategy on startup of the agent. | `smallfiles` | Valid values are: `smallfiles`, `start` or `none` |
| `LOGDNA_METRICS_PORT` | `log.metrics_port` | Port number to expose Prometheus metrics for the agent. |  |  |
| `LOGDNA_LOG_K8S_EVENTS` |  | Boolean that defines if Kubernetes resource events are logged. | | |
| `LOGDNA_USE_K8S_LOG_ENRICHMENT` |  | Set to enrich log lines from other pods by allowing the agent to query the K8s API. | `always` | Valid values are: `always`, `never` |
{: caption="Table 4. Tags that are available for the logging agent V2" caption-side="top"}


## Environment variables for the V2 logging agent
{: #log_analysis_agent_configure_v2}


| Environment variable     | Description   |  Default value                         | Sample value          |
|--------------------------|---------------|----------------------------------------|-----------------------|
| `DEFAULT_CONF_FILE`      | Default configuration file.                           | `/etc/logdna/config.yaml`              |                       |
| `LOGDNA_PLATFORM`        | Log source type.                                      | `k8s`                                  |                       |
| `LOGDNA_INGESTION_KEY`   | Reference to the logging ingestion key.                | secretKeyRef                           |                       |
| `LOGDNA_HOST`            | {{site.data.keyword.la_full_notm}} ingestion endpoint.                            |                                        | `logs.us-south.logging.cloud.ibm.com` |
| `LOGDNA_API_HOST`        | {{site.data.keyword.la_full_notm}} API ingestion endpoint.                        |                                        | `api.us-south.logging.cloud.ibm.com`   |
| `LOGDNA_ENDPOINT`        | Ingestion log path.                                   | `/logs/agent/`                         |                       |
| `LOGDNA_HOSTNAME`        | Log Source name.                                      |                                        | `MyCluster`                            |
| `LOGDNA_LOG_DIRS`        | Defines custom paths that you want the agent to monitor.  \n Separate multiple paths by using commas.  \n You can use glob patterns. Use double quotation marks to add a globe pattern.   | `/var/log/`   | `/output/,/mylogs/myapplogs/` |
| `LOGDNA_INCLUSION_RULES` | Custom rules that you can define to configure what log files to monitor.  \n These files can be located in any of the paths that are defined through the logdir parameter.  \n You can use glob patterns. For more information, see [Glober rules](https://github.com/CJP10/globber){: external}   |  | `*.json,*.test` |
| `LOGDNA_INCLUSION_REGEX_RULES` | Regex custom rules that you can define to configure what log files to monitor. For more information, see [regex syntax](https://docs.rs/regex/1.2.1/regex/#syntax){: external}  \n These files can be located in any of the paths that are defined through the logdir parameter.  |  |  |
| `LOGDNA_EXCLUSION_RULES` | Custom rules that you can define to configure what log files to exclude from being monitored.  \n You can use glob patterns. For more information, see [Glober rules](https://github.com/CJP10/globber){: external}  | | |
| `LOGDNA_EXCLUSION_REGEX_RULES` | Regex custom rules that you can define to configure what log files to exclude from being monitored. |  | `/var/log/containers/**,/var/log/pods/**`  |
| `LOGDNA_USE_SSL`          | Boolean that defines whether TLS 1.2 should be used when the agent sends logs to the logging instance.  \n The default value is set to `true`.  | `true` | `true` |
| `LOGDNA_USE_COMPRESSION`  | Boolean that defines whether compression is enabled when the agent sends logs to the logging instance.  \n  The default value is set to `true`. | `true` | `true` |
| `LOGDNA_GZIP_LEVEL`       | Compression level for gzip.  \n Valid values are: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`  \n When you set this variable to `1`, you are configuring the agent to use the fastest compression speed but at a lower ratio. When you set this variable to `9`, you are configuring the agent to use the highest compression ratio but at a lower speed.  | `2` | `6` |
| `LOGDNA_TAGS` | Define tags to group hosts automatically into dynamic groups. |  | `production,serviceA` |
{: caption="Table 5. Tags that are available for the logging agent V2" caption-side="top"}

## Standard Kubernetes clusters: environment variables for the V1 logging agent
{: #log_analysis_dna_agent_configure_std_kube_v1}

| Environment variable     | Description                                           | Default value                          | Sample value          |
|--------------------------|-------------------------------------------------------|----------------------------------------|-----------------------|
| `DEFAULT_CONF_FILE`      | Default configuration file.                           | `/etc/logdna/config.yaml`              |                       |
| `LOGDNA_PLATFORM`        | Log source type.                                      | `k8s`                                  |                       |
| `LOGDNA_INGESTION_KEY`   | Reference to the logging ingestion key.                | secretKeyRef                           |                       |
| `LDLOGHOST`              | {{site.data.keyword.la_full_notm}} ingestion endpoint.                            |                                        | `logs.us-south.logging.cloud.ibm.com` |
| `LDAPIHOST`              | {{site.data.keyword.la_full_notm}} API ingestion endpoint.                        |                                        | `api.us-south.logging.cloud.ibm.com`   |
| `LDLOGPATH`              | Ingestion log path.                                   | `/logs/agent/`                         |                       |
| `LOGDNA_HOSTNAME`        | Log Source name.                                      |                                        | `MyCluster`                            |
| `LOG_DIRS`            | Defines custom paths that you want the agent to monitor.  \n Separate multiple paths by using commas.  \n You can use glob patterns. Use double quotation marks to add a globe pattern.  | `var/log` | `/output/,/mylogs/myapplogs/` |
| `LOGDNA_INCLUDE`     | Custom rules that you can define to configure what log files to monitor.  \n These files can be located in any of the paths that are defined through the logdir parameter.  \n You can use glob patterns. For more information, see [Glober rules](https://github.com/CJP10/globber){: external}  |  | `*.json,*.test` |
| `LOGDNA_INCLUDE_REGEX` | Regex custom rules that you can define to configure what log files to monitor. For more information, see [regex syntax](https://docs.rs/regex/1.2.1/regex/#syntax){: external}  \n These files can be located in any of the paths that are defined through the logdir parameter.  | | |
| `LOGDNA_EXCLUDE`     | Custom rules that you can define to configure what log files to exclude from being monitored.  \n These files can be located in any of the paths that are defined through the logdir parameter.  \n Separate multiple files by using commas. You can use glob patterns. You can configure specific files. | | |
| `LOGDNA_EXCLUDE_REGEX` | Regex custom rules that you can define to configure what log files to exclude from being monitored. | | `/var/log/containers/*,/var/log/pods/*`  |
| `LDLOGSSL` | Boolean that defines whether TLS 1.2 should be used when the agent sends logs to the logging instance.  \n The default value is set to `true`. | `true` | `true` |
| `COMPRESS` | Boolean that defines whether compression is enabled when the agent sends logs to the logging instance.  \n  The default value is set to `true`. | `true` | `true` |
| `GZIP_COMPRESS_LEVEL` | Compression level for gzip.  \n Valid values are: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`  \n When you set this variable to `1`, you are configuring the agent to use the fastest compression speed but at a lower ratio. When you set this variable to `9`, you are configuring the agent to use the highest compression ratio but at a lower speed.  | `2` | `6` |
| `LOGDNA_TAGS` | Define tags to group hosts automatically into dynamic groups. |  | `production,serviceA`  |
{: caption="Table 6. Tags that are available for the logging agent V2" caption-side="top"}

### Linux: configuration parameters for V1 logging agent
{: #log_analysis_agent_configure_linux_v1}

| Parameter | Description                                          |
|-----------|------------------------------------------------------|
| `tags`    | Define tags to group hosts automatically into dynamic groups. |
| `logdir`  | Define custom paths that you want the agent to monitor.  \n Separate multiple paths by using commas. You can use glob patterns. You can configure specific files. Enter glob patterns by using double quotation marks. |
| `exclude` | Define the files that you do not want the logging agent to monitor. **Note:** These files can be located in any of the paths that are defined through the logdir parameter.  \n Separate multiple files by using commas. You can use glob patterns. You can configure specific files. |
| `exclude_regex` | Define regex patterns to filter out any lines that match the pattern. Do not include leading and trailing `/`. |
| `hostname` | Define the hostname. This value overrides the operating system hostname. |
| `autoupdate` | Set to `1` to update the agent automatically when the public repo agent definition is updated. Set to `0` to disable this feature. |
{: caption="Table 7. Configuration options for the logging agent V1" caption-side="top"}


## Configuring tags to group data
{: #log_analysis_dna_agent_tags}

You can configure tags at the agent level so that all lines that are sent by this agent can be grouped automatically into a group when you filter data in a view.

* You can define multiple tags.
* You separate tags by using commas.
* The maximum number of characters that you can set to define multiple tags is 80 characters.

| Platform                       | How to install and configure |
|--------------------------------|------------------------------|
| `Kubernetes cluster`           | [Adding tags to logs from a Kubernetes cluster](/docs/log-analysis?topic=log-analysis-adding_tags#adding_tags_kube) |
| `Linux Ubuntu or Debian`       | [Adding tags to logs from Linux Ubuntu or Debian](/docs/log-analysis?topic=log-analysis-adding_tags#adding_tags_linux) |
{: caption="Table 8. Adding tags" caption-side="top"}


### Exclude log files that are monitored by the agent
{: #log_analysis_agent_exclude}

You can configure a logging agent to exclude logs that you do not want to monitor through the logging UI.

* You can exclude files that are located in any of the paths that are defined through the **logdir** parameter in a Linux system or the **LOGDNA_EXCLUDE** variable in a Kubernetes cluster.
* You can configure multiple files. You separate multiple files by using commas.
* You can use glob patterns to define what you want to exclude.
* You can configure specific files.

For more information, see [Excluding log files through the logging agent](/docs/log-analysis?topic=log-analysis-exclude_logs_from_agent).
