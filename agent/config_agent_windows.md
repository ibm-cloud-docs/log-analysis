---

copyright:
  years:  2022, 2023
lastupdated: "2022-09-19"

keywords: IBM, Log Analysis, logging, config agent, Windows

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Configuring the V2 Logging agent for Windows
{: #config_agent_windows}

The logging agent is responsible for collecting and forwarding logs to your {{site.data.keyword.la_full_notm}} instance. After you provision an instance of {{site.data.keyword.la_full}}, you must configure a logging agent for each log source that you want to monitor.
{: shortdesc}

To configure your Windows server to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install the `logdna-agent`. The logging agent reads log files from a directory defined in your Windows system and forwards the log data to your logging instance.

## Install the Chocolately package manager
{: #chocolately}

You need to install the Chocolately package manager to install the Windows agent.

From a command prompt run:

```text
powershell -command "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
```
{: codeblock}

or from PowerShell run:

```text
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```
{: codeblock}


## Installing the V2 Logging agent
{: #config_logging_agent_windows}

To configure your Windows server to forward logs to your logging instance, run the following from a Windows command prompt as an admin user:

```text
choco install logdna-agent -y
logdna-agent -k <INJESTION_KEY> # this is your unique Ingestion Key
logdna-agent -s LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com # this is your API server host
logdna-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com # this is your Log server host
:: %ALLUSERSPROFILE%\logs is monitored/added by default (recursively), optionally add more dirs with:
:: logdna-agent -d <LOCAL_WINDOWS_PATH>
:: You can configure the agent to tag your hosts with:
:: logdna-agent -t <YOUR_TAG>
nssm start logdna-agent
```
{: codeblock}

Where

`INGESTION_KEY`
:   Is the injestion key for your {{site.data.keyword.la_full_notm}} instance.

`LOCAL_WINDOWS_PATH`
:   Is the path on your Windows machine where You log data is stored.

`YOUR_TAG`
:   Is how you want your Windows logging data to be tagged in {{site.data.keyword.la_full_notm}}.

## Starting the V2 Logging agent
{: #start_logging_agent_windows}

To start the Logging agent, run the following from a Windows command prompt as an admin user:

```text
nssm start logdna-agent
```
{: codeblock}
