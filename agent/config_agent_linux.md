---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, config agent

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Connecting a logging agent to a Linux Ubuntu or Debian
{: #config_agent_linux}

The logging agent is responsible for collecting and forwarding logs to your {{site.data.keyword.la_full_notm}} instance. After you provision an instance of {{site.data.keyword.la_full}}, you must configure a logging agent for each log source that you want to monitor.
{: shortdesc}


## Configuring a logging agent on Linux Ubuntu or Debian
{: #config_agent_linux_steps}

To configure your Ubuntu server to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install a `logging-agent`. The logging agent reads log files from */var/log*, and forwards the log data to your logging instance.

To configure your Ubuntu server to forward logs to your logging instance, complete the following steps from an Ubuntu terminal:

1. Install the logging agent. Run the following commands:

    ```
    echo "deb https://repo.logdna.com stable main" | sudo tee /etc/apt/sources.list.d/logdna.list
    ```
    {: codeblock}

    ```
    wget -O- https://repo.logdna.com/logdna.gpg | sudo apt-key add -
    ```
    {: codeblock}

    ```
    sudo apt-get update
    ```
    {: codeblock}

    ```
    sudo apt-get install logdna-agent < "/dev/null"
    ```
    {: codeblock}

2. Set the ingestion key that the logging agent must use to forward logs to the {{site.data.keyword.la_full_notm}} instance.  

    ```
    sudo logdna-agent -k INGESTION_KEY
    ```
    {: codeblock}

    Where INGESTION_KEY contains the ingestion key active for the {{site.data.keyword.la_full_notm}} instance where you are configuring to forward logs.

3. Set the authentication endpoint. The logging agent uses this host to authenticate and get the token to forward logs. 

| Location               | Command                                                                         |
|------------------------|---------------------------------------------------------------------------------|
| `Chennai (in-che)`     | `sudo logdna-agent -s export LOGDNA_APIHOST=api.in-che.logging.cloud.ibm.com`   |
| `Dallas (us-south)`    | `sudo logdna-agent -s export LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com` |
| `Frankfurt (eu-de)`    | `sudo logdna-agent -s export LOGDNA_APIHOST=api.eu-de.logging.cloud.ibm.com`    |
| `London (eu-gb)`       | `sudo logdna-agent -s export LOGDNA_APIHOST=api.eu-gb.logging.cloud.ibm.com`    |
| `Tokyo (jp-tok)`       | `sudo logdna-agent -s export LOGDNA_APIHOST=api.jp-tok.logging.cloud.ibm.com`   |
| `Seoul (kr-seo)`       | `sudo logdna-agent -s export LOGDNA_APIHOST=api.kr-seo.logging.cloud.ibm.com`   |
| `Sydney (au-syd)`      | `sudo logdna-agent -s export LOGDNA_APIHOST=api.au-syd.logging.cloud.ibm.com`   |
| `Washington (us-east)` | `sudo logdna-agent -s export LOGDNA_APIHOST=api.us-east.logging.cloud.ibm.com`  |
{: caption="Commands by region" caption-side="top"}


4. Set the ingestion endpoint. Choose the public or the private endpoint in a location.

| Location               | Command (By using public endpoints)                                       | Command (By using private endpoints)                                                                                                                     |
|------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Chennai (in-che)`     | `sudo logdna-agent -s LOGDNA_LOGHOST=logs.in-che.logging.cloud.ibm.com`   | `sudo logdna-agent -s LOGDNA_LOGHOST=logs.private.in-che.logging.cloud.ibm.com`  \n  \n `export LDLOGHOST=logs.private.in-che.logging.cloud.ibm.com`     |
| `Dallas (us-south)`    | `sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com` | `sudo logdna-agent -s LOGDNA_LOGHOST=logs.private.us-south.logging.cloud.ibm.com`  \n  \n `export LDLOGHOST=logs.private.us-south.logging.cloud.ibm.com` |
| `Frankfurt (eu-de)`    | `sudo logdna-agent -s LOGDNA_LOGHOST=logs.eu-de.logging.cloud.ibm.com`    | `sudo logdna-agent -s LOGDNA_LOGHOST=logs.private.eu-de.logging.cloud.ibm.com`  \n  \n `export LDLOGHOST=logs.private.eu-de.logging.cloud.ibm.com`       |
| `London (eu-gb)`       | `sudo logdna-agent -s LOGDNA_LOGHOST=logs.eu-gb.logging.cloud.ibm.com`    | `sudo logdna-agent -s LOGDNA_LOGHOST=logs.private.eu-gb.logging.cloud.ibm.com`  \n  \n `export LDLOGHOST=logs.private.eu-gb.logging.cloud.ibm.com`       |
| `Tokyo (jp-tok)`       | `sudo logdna-agent -s LOGDNA_LOGHOST=logs.jp-tok.logging.cloud.ibm.com`   | `sudo logdna-agent -s LOGDNA_LOGHOST=logs.private.jp-tok.logging.cloud.ibm.com`  \n  \n `export LDLOGHOST=logs.private.jp-tok.logging.cloud.ibm.com`     |
| `Seoul (kr-seo)`       | `sudo logdna-agent -s LOGDNA_LOGHOST=logs.kr-seo.logging.cloud.ibm.com`   | `sudo logdna-agent -s LOGDNA_LOGHOST=logs.private.kr-seo.logging.cloud.ibm.com`  \n  \n `export LDLOGHOST=logs.private.kr-seo.logging.cloud.ibm.com`     |
| `Sydney (au-syd)`      | `sudo logdna-agent -s LOGDNA_LOGHOST=logs.au-syd.logging.cloud.ibm.com`   | `sudo logdna-agent -s LOGDNA_LOGHOST=logs.private.au-syd.logging.cloud.ibm.com`  \n  \n `export LDLOGHOST=logs.private.au-syd.logging.cloud.ibm.com`     |
| `Washington (us-east)` | `sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-east.logging.cloud.ibm.com`  | `sudo logdna-agent -s LOGDNA_LOGHOST=logs.private.us-east.logging.cloud.ibm.com`  \n  \n `export LDLOGHOST=logs.private.us-east.logging.cloud.ibm.com`   |
{: caption="Commands by region" caption-side="top"}

5. Define more log paths to be monitored. Run the following command:

    ```
    sudo logdna-agent -d /path/to/log/folders
    ```
    {: codeblock}

    By default, **/var/log** is monitored.

6. Optionally, configure the logging agent to tag your hosts.

7. Start the logging agent.

    ```
    sudo /etc/init.d/logdna-agent start
    ```
    {: codeblock}

