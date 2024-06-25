---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Configuring Logging agent V3 for Red Hat Linux (WIP)
{: #config_agent_rhel3}

To configure a Red Hat Linux server to send logs to a {{site.data.keyword.la_full_notm}} instance, you must install a logging agent.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

- By default, the logging agent reads log files from */var/log*, and forwards the log data to your logging instance.
- The agent runs as a Linux daemon by using `systemd`. You can manage the agent by using `systemctl`.

These instructions are for Red Hat Linux systems but can be used for other Linux RPM-based servers.
{: note}



## Considerations when upgrading from earlier agent versions
{: #config_agent_rhel3_pereqs}

If you are upgrading from an earlier Linux agent, you might have an existing `/etc/logdna.conf` file that might need updates.

- If you have a custom `logdir` value with files or globs in an `/etc/logdna.conf` file, you will need to change those in the `/etc/logdna.conf` file. Only directories can be specifed in `logdir`.
- File patterns need to be specified as an inclusion rule.

If you are using older Linux distributions (Centos 7, Amazon Linux 2, RHEL 7), you need to make sure that the `/var/lib/logdna` directory exists since older versions of `systemd` packaged with these distributions will not automatically create the directory.

## Deploy the logging agent

Complete the following steps:

### Step 1. Install the logging agent
{: #config_agent_rhel3_step1}

Install the latest version of the logging agent. Run the following commands from a terminal:

```sh
sudo rpm --import https://assets.logdna.com/logdna.gpg
```
{: codeblock}

```sh
echo "[logdna]
name=LogDNA packages
baseurl=https://assets.logdna.com/el6/
enabled=1
gpgcheck=1
gpgkey=https://assets.logdna.com/logdna.gpg" | sudo tee /etc/yum.repos.d/logdna.repo
```
{: codeblock}

```sh
sudo yum install logdna-agent
```
{: codeblock}

### Step 2. Configure the logging agent
{: #config_agent_rhel3_step2}

To configure the agent, do the following:

1. Create the agent configuration file (`logdna.conf`) in the `/etc` directory by running  the following command:

   ```sh
   sudo touch /etc/logdna.conf
   ```
   {: pre}

   If the file does not exist, the `logdna.conf` file is created as an empty file.

2. Customize the agent.

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
    - "/var/log/"
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

Additionally, you can configure the following information:

`params.tags`
:   You can define a comma separated list of metadata that the agent includes with each log line.

`params.hostname`
:   You can include the name of the host. This information is included with each log line.

`log.dirs`
:   You can configure other directories that you want the agent to monitor for logs.

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
    - "/var/log/"
  include:
    glob:
      - "*.log"
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



### Step 3. Run the logging agent
{: #config_agent_rhel3_step3}

Start the `logdna-agent` service using the `systemctl` command:

```sh
sudo systemctl start logdna-agent
```
{: pre}

If the agent was already running when you made configuration changes, you must restart the agent for the new configuration to take effect. To restart the service run the following command:

```sh
sudo systemctl restart logdna-agent
```
{: pre}

Verify that the agent is running and log data flowing. You can verify the status of the agent by running the following command:

```sh
systemctl status logdna-agent
```
{: pre}

Run `/usr/bin/logdna-agent` to see the agent logs.
{: tip}


## Step 4. Enable the agent on boot
{: #config_agent_rhel3_step4}

To enable the agent on boot, run the following command:

```sh
sudo systemctl enable logdna-agent
```
{: pre}

