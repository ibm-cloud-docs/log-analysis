---

copyright:
  years:  2018, 2022
lastupdated: "2021-10-06"

keywords: IBM, Log Analysis, logging, config agent

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Configuring a Logging agent for a Linux RPM-based
{: #config_agent_linux_rpm}

The logging agent is responsible for collecting and forwarding logs to your {{site.data.keyword.la_full}} instance. After you provision an instance of {{site.data.keyword.la_full_notm}}, you must configure a logging agent for each log source that you want to monitor.
{: shortdesc}

The logging agent reads log files from */var/log*, and forwards the log data to your logging instance.

The agent runs as a Linux daemon by using `systemd`. You can manage the agent by using `systemctl`.


To configure your Linux RPM-based server to forward logs to your logging instance, complete the following steps from a terminal:

## Step 1. Add the logdna repository to your package manager
{: #config_agent_linux_rpm_step1}

Add the logdna repository to your package manager, open a host terminal and run the following commands:

1. List the versions of the agent that are available in the repo.

    ```text
    yum --showduplicates list logdna-agent | expand
    ```
    {: codeblock}

2. Add the logdna repository to your package manager.

    ```text
    sudo rpm --import https://assets.logdna.com/logdna.gpg
    echo "[logdna]
    name=LogDNA packages
    baseurl=https://assets.logdna.com/el6/
    enabled=1
    gpgcheck=1
    gpgkey=https://assets.logdna.com/logdna.gpg" | sudo tee /etc/yum.repos.d/logdna.repo
    ```
   {: codeblock}

3. Install the agent.

    ```text
    sudo yum -y install logdna-agent-VERSION.x86_64
    ```
    {: codeblock}

    Where `VERSION` is set to the agent version that you want to configure.

    For example, to install the logging agent version `2.1.2-1`, you can use the following command: 
    
    ```text
    sudo yum -y install logdna-agent-2.1.2-1.x86_64
    ```
    {: codeblock}

If you get the error `failed loading '/etc/yum.repos.d/logdna.repo'`, check that the `/etc/yum.repos.d/logdna.repo` file is set as follows:

```text
[logdna]
name=LogDNA packages
baseurl=https://assets.logdna.com/el6/
enabled=1
gpgcheck=1
gpgkey=https://assets.logdna.com/logdna.gpg
```
{: codeblock}

## Step 2. Create the configuration file
{: #config_agent_linux_rpm_step2}

Create the configuration file that includes information about the {{site.data.keyword.la_full_notm}} instance where you are configuring your system to forward logs.

Complete the following steps:

1. Create the configuration file `logdna.env` in the `/etc` directory, by using the following command:

    ```text
    sudo touch /etc/logdna.env
    ```
    {: codeblock}

    The logdna.env file is initialized as an empty file and stores environment variables as key-value pairs.

2. Edit the `/etc/logdna.env` file and set the following information:

    ```text
    LOGDNA_HOST=ENDPOINT
    LOGDNA_ENDPOINT=/logs/agent
    LOGDNA_INGESTION_KEY=INGESTION_KEY
    LOGDNA_LOG_DIRS=OTHER_LOG_PATHS
    LOGDNA_HOSTNAME=NAME_OF_SOURCE
    LOGDNA_TAGS=TAGS
    ```
    {: codeblock}

    Where

    - `INGESTION_KEY` contains the ingestion key active for the {{site.data.keyword.la_full_notm}} instance where you are configuring to forward logs.

    - `ENDPOINT` is the authentication endpoint. The logging agent uses this host to authenticate and get the token to forward logs. You can set a public endpoint `logs.REGION.logging.cloud.ibm.com` or a private endpoint `logs.private.REGION.logging.cloud.ibm.com`. Replace `REGION` with the location of the {{site.data.keyword.la_full_notm}} instance where you are configuring to forward logs.

    - `NAME_OF_SOURCE` contains a human-readable name for the source where you are collecting logs, such as the name of a vsi, for example.

    - `OTHER_LOG_PATHS` define more log paths to be monitored, for example, `/path/to/log/folders`. By default, **/var/log** is monitored. 

    - `TAGS` define a comma-separated list of tags that you want to attach as metadata to each log record.



## Step 3. Start the logging agent
{: #config_agent_linux_rpm_step3}

### Agent V2
{: #config_agent_linux_rpm_step3_v2}

Complete the following steps to start the logging agent:

1. Set the ingestion key.

    ```text
    logdna-agent -k INGESTION_KEY
    ```
    {: codeblock}

2. Start the logdna-agent service by running the following command:

    ```text
    sudo service logdna-agent start
    ```
    {: codeblock}

Next, verify that the agent is running.

```text
sudo service logdna-agent status
```
{: codeblock}


## Appendix. Commands to manage the agent
{: #config_agent_linux_rpm_cmd} 


### Get the agent version
{: #config_agent_linux_rpm_cmd0}

```text
logdna-agent --version
```
{: codeblock}

### Enable the agent on boot
{: #config_agent_linux_rpm_cmd1} 

```text
sudo systemctl enable logdna-agent
```
{: codeblock}

### Check the status of the agent
{: #config_agent_linux_rpm_cmd2}

```text
systemctl status logdna-agent
```
{: codeblock}


### Start the agent
{: #config_agent_linux_rpm_cmd3}

```text
sudo systemctl start logdna-agent
```
{: codeblock}



### Stop the agent
{: #config_agent_linux_rpm_cmd4}

```text
sudo systemctl stop logdna-agent
```
{: codeblock}

### Get a log trace from the agent
{: #config_agent_linux_rpm_cmd5}

```text
journalctl _SYSTEMD_INVOCATION_ID=`systemctl show -p InvocationID --value logdna-agent.service`
```
{: codeblock}

### Delete the agent
{: #config_agent_linux_rpm_cmd5}

```text
yum remove logdna-agent
```
{: codeblock}

