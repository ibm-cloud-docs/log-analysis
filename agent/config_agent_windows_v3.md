---

copyright:
  years:  2022, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, config agent, Windows

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Configuring the V3 Logging agent for Windows
{: #config_agent_windows_v3}

The logging agent is responsible for collecting and forwarding logs to your {{site.data.keyword.la_full_notm}} instance. After you provision an instance of {{site.data.keyword.la_full}}, you must configure a logging agent for each log source that you want to monitor.
{: shortdesc}

<!-- common deprecation notice -->
{{../_include-segments/deprecation_notice.md}}

To configure your Windows server to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install the `logdna-agent`. The logging agent reads log files from a directory defined in your Windows system and forwards the log data to your logging instance.




## Before you begin
{: #config_agent_windows_v3_prereqs}

Currently, you cannot collect Windows Event server logs with this agent. [Configure NXlog](/docs/log-analysis?topic=log-analysis-windows_serv) to send Event logs to the logging instance.
{: note}


## Step 1. Install the agent
{: #config_agent_windows_v3_install}

You can install the agent by using MSI or Chocolatey.

### Option 1: Install by using Chocolatey
{: #config_agent_windows_v3_install_1}

Run the following command to deploy the agent:

```text
choco install mezmo-agent
```
{: codeblock}


### Option 2: Install by using MSI
{: #config_agent_windows_v3_install_2}

Complete the following steps to deploy the agent:

1. [Download the current Windows agent `msi` package.](https://github.com/logdna/logdna-agent-v2/blob/3.6/docs/WINDOWS.md){: external}


2. Run the following from a Windows command prompt as an admin user in the directory where you downloaded the agent package:

   ```text
   msiexec /i "mezmo-agent.msi" /qn KEY=<INGESTION_KEY>
   ```
   {: codeblock}

   Where

   `INGESTION_KEY`
   :   Is the ingestion key for your {{site.data.keyword.la_full_notm}} instance.

After the agent is installed it is started and log entries are written to `c:\ProgramData\logs`.

## Step 2. Configure the agent
{: #config_agent_windows_v3_config}

After you install the agent, check that you have the following directories and files:

`C:\Program Files\Mezmo`
:   This is the directory containing the installed files.

`C:\ProgramData\logdna\logdna.conf`
:   This is the file you will use to configure the agent.

`C:\ProgramData\logdna\agent_state.db`
:   This is the file used to track log offsets.

`C:\ProgramData\logs`
:   This is the default directory that the agent automatically monitors for log files. Only `*.log` files are processed automatically with the configuration installed by default.

Then, customize the agent by configuring the `logdna.conf` file.

The following is a sample of the default `logdna.conf` file:

```yaml
http:
  host: logs....
  endpoint: /logs/agent
  use_ssl: true
  timeout: 10000
  use_compression: true
  gzip_level: 2
  body_size: 2097152
  ingestion_key: INGESTION_KEY
log:
  dirs:
    - "C:\\ProgramData\\logs"
  include:
    glob:
      - "*.log"
    regex: []
  exclude:
    glob: []
    regex: []
  use_k8s_enrichment: ~
  log_k8s_events: ~
journald: {}
startup: {}
```
{: codeblock}

Configure the following information:

`host`
:   Set to the endpoint of the location where the logging instance is available. For example, for a logging instance in the US South region, set the value to `logs.us-south.logging.cloud.ibm.com`. For more information, see [Endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_ingestion).

`ingestion_key`
:   Set to an ingestion key that is enabled in the logging instance.

`params.tags`
:   You can define a comma separated list of metadata that the agent includes with each log line.

`params.hostname`
:   You can include the name of the host. This information is included with each log line.

`log.dirs`
:   You can configure directories that you want the agent to monitor for logs.

    You must specify two backslashes (`\\`) when specifying the directory. For example, `C:\\ProgramData\\logs`.
    {: important}

    If you specify a directory that does not exist, the agent will successfully start, but data will not be processed.
    {: note}

`log.include.glob`
:   You can configure glob patterns to define the types of log files that the agent processes.

    For example:

    Specify `*.log` to process any log with extension `.log`.

    Specify `*.txt` to process any log with extension `.txt`.

`log.include.regex`
:   You can configure regex patterns to define the types of log files that the agent processes.

    For example:

    Specify `^[^.]*$` to process a log file without a file extension.

`log.exclude.glob`
:   You can configure glob patterns to define the types of log files that the agent does not process and are ignored.

`log.exclude.regex`
:   You can configure regex patterns to define the types of log files that the agent does not process and are ignored.

`lookback`
:   Set this field to indicate how the logging agent handles files. Valid values are: `none`, `smallfiles`, and `start`.

    Set to `none` when you want the agent to process new lines, and ignore non-processed existing log lines when the agent is restarted.

    Set to `start` so that the agent checks the agent state file and uses the last recorded state to continue processing. If the file is not present, the agent processes data in the file from the beginning.

    Set to `smallfiles` so that the agent checks the agent state file and uses the last recorded state to continue processing. If the file is not present, the agent processes data in the file from the beginning when the file is less than 8 KB, and processes data from the end when the file is larger than 8 KB.

You can use `hostname` and `tags` values to search logs.
{: tip}

The following is an example `logdna.conf` file:

```yaml
http:
  host: logs.us-south.logging.cloud.ibm.com
  endpoint: /logs/agent
  use_ssl: true
  timeout: 10000
  use_compression: true
  gzip_level: 2
  body_size: 2097152
  ingestion_key: INGESTION_KEY
  params:
    tags: "demo"
    hostname: "MYHOST"
log:
  dirs:
    - "C:\\ProgramData\\logs"
    - "C:\\ProgramData\\otherlogs"
  include:
    glob:
      - "*.log"
      - "*.txt"
    regex:
      - "^[^.]*$"
  exclude:
    glob: []
    regex: []
  use_k8s_enrichment: ~
  log_k8s_events: ~
  lookback: start
journald: {}
startup: {}
```
{: codeblock}


## Starting and stopping the logging agent
{: #config_agent_windows_v3_config_manage}

When you install the agent, the agent is automatically started. However, there are times when you need to stop, start, or restart the agent.

Whenever you change the `logdna.conf` file you must restart the agent to pick up the configuration changes.
{: important}

1. Click Start, enter "Services" and open the "Services" app.

2. Find `Mezmo Agent` in the list.

3. Right-click `Mezmo Agent` and select the action you want to run:

   Start
   :   Start the agent. This option is only available when the agent is not running.

   Stop
   :   Stop the agent when it is running.

   Restart
   :   Stop and restart a running agent.

If the agent does not start, or restart, check the `c:\ProgramData\logs\logdna-agent-svc_rCURRENT.log` for messages to help you resolve any configuration errors.
{: tip}
