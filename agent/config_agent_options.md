---

copyright:
  years:  2022, 2024
lastupdated: "2024-05-24"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Logging agent options (WIP)
{: #config_agent_options}

The logging agent can be configured to include or exclude specific log files and lines forwarded to your {{site.data.keyword.la_full_notm}} instance. This configuration is done using a configuration file.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

How the `logdna.conf` is provided to the agent depends on where the agent is run.  See the appropriate configuration topic for your operating system for details.

## Configuration file
{: #logdna_conf}

A `logdna.conf` file is similar to the following.

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
  params:
    tags: "TAG1, TAG2, TAG3"
    hostname: "MYHOST"
log:
  dirs:
    - "LOG_DIRECTORY"
  include:
    glob:
      - "*.log"
    regex: []
  exclude:
    glob: []
    regex: []
  use_k8s_enrichment: ~
  log_k8s_events: ~
  lookback: start
  line_exclusion_regex:
journald: {}
startup: {}
```
{: codeblock}

Configure the following information in your `logdna.conf` file:

`host`
:   Set to the endpoint of the location where the logging instance is available. For example, for a logging instance in the US South region, set the value to `logs.us-south.logging.cloud.ibm.com`. For more information, see [Endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_ingestion).

`ingestion_key`
:   Set to an ingestion key that is enabled in the logging instance.

`params.tags`
:   You can define a comma separated list of metadata that the agent includes with each log line.

    You can use the `tags` values to search logs.
    {: tip}

`params.hostname`
:   You can include the name of the host. This information is included with each log line.

    You can use the `hostname` value to search logs.
    {: tip}

`log.dirs`
:   You can configure directories that you want the agent to monitor for logs. Each directory must be specified on a separate line.

    For example, the following indicate to forward logs in the `/var/log/myhost` and `/var/log/myhost/demo` directories:

    ```yaml
    dirs:
    - "/var/log/myhost"
    - "/var/log/myhost/demo"
    ```
    {: codeblock}

    [Windows]{: tag-windows} You must specify two backslashes (`\\`) when specifying the directory. For example, `C:\\ProgramData\\logs`.
    {: important}

    If you specify a directory that does not exist, the agent will successfully start, but data will not be processed.
    {: note}

`log.include.glob`
:   You can configure glob patterns to define the types of log files that the agent processes.

    For example:

    `"*/abc*.log"`
    :   Forwards all files in the configured directories with file names beginning with `abc` and have the file extension `.log`.

    `"*.json"`
    :   Forwards all files with the file extension `.json`.

    `"*/demo/a.txt"`
    :   Forward only the specific file in the specified directory. In this example only the `a.txt` file in the `demo` directory is forwarded.

    `"*/abc???.txt"`

    :   A `?` can be used to match numbers. This example forwards any files beginning with `abc` followed by 3 numbers with the file extension `.txt`.

`log.include.regex`
:   You can configure regex patterns to define the types of log files that the agent processes.

    For example:

    `".*[^.]*$"`
    :   Forwards all log files without a file extension.

    `".*/[a-zA-Z0-9_\\-]+\\.txt"`
    :   Forwards all log files with a file extension of `.txt` that only includes alphanumeric characters in the file name.

    `".*/demo/[a-zA-Z0-9_\\-]+\\.json"`
    :   Forwards all log files in the `demo` directory with a file extension of `.json` that only includes alphanumeric characters in the file name.

    `".*/^[a-zA-Z0-9_\\-]+\\.log"`
    :   Forwards any file that *does not* have the `.log` file extension and alphanumeric characters in the file name. The use of the `^` indicates the "not" condition.

`log.exclude.glob`
:   You can configure glob patterns to define the types of log files that the agent does not process and are ignored. Patterns similar to `log.include.glob` can be used.

`log.exclude.regex`
:   You can configure regex patterns to define the types of log files that the agent does not process and are ignored. Patterns similar to `log.include.regex` can be used.

`lookback`
:   Set this field to indicate how the logging agent handles files. Valid values are: `none`, `smallfiles`, and `start`.

    Set to `none` when you want the agent to process new lines, and ignore existing log lines that were not processed when the agent is restarted.

    Set to `start` so that the agent checks the agent state file and uses the last recorded state to continue processing. If the file is not present, the agent processes data in the file from the beginning.

    Set to `smallfiles` so that the agent checks the agent state file and uses the last recorded state to continue processing. If the file is not present, the agent processes data in the file from the beginning when the file is less than 8 KB, and processes data from the end when the file is larger than 8 KB.

`line_exclusion_regex:`
:   Set this field to exclude specific lines within the forwarded log files.

    For example:

    `".*(?i)debug.*"`
    :   Exclude any log line containing the string `debug`. Specifying `(?i)` indicates a case insensitive match. In this example logs with the string `debug` or `DEBUG` would be excluded.

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
