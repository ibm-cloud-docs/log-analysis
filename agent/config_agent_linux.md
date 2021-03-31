---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, config agent

subcollection: Log-Analysis-with-LogDNA

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

# Connecting a logging agent to a Linux Ubuntu or Debian
{: #config_agent_linux}

The logging agent is responsible for collecting and forwarding logs to your {{site.data.keyword.la_full_notm}} instance. After you provision an instance of {{site.data.keyword.la_full}}, you must configure a logging agent for each log source that you want to monitor.
{:shortdesc}


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

    <table>
      <caption>Commands by region</caption>
      <tr>
        <th>Location</th>
        <th>Command </th>

      </tr>
      <tr>
        <td>`Chennai (in-che)`</td>
        <td>`sudo logdna-agent -s export LOGDNA_APIHOST=api.in-che.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`Dallas (us-south)`</td>
        <td>`sudo logdna-agent -s export LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`Frankfurt (eu-de)`</td>
        <td>`sudo logdna-agent -s export LOGDNA_APIHOST=api.eu-de.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`London (eu-gb)`</td>
        <td>`sudo logdna-agent -s export LOGDNA_APIHOST=api.eu-gb.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`Tokyo (jp-tok)`</td>
        <td>`sudo logdna-agent -s export LOGDNA_APIHOST=api.jp-tok.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`Seoul (kr-seo)`</td>
        <td>`sudo logdna-agent -s export LOGDNA_APIHOST=api.kr-seo.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`Sydney (au-syd)`</td>
        <td>`sudo logdna-agent -s export LOGDNA_APIHOST=api.au-syd.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`Washington (us-east)`</td>
        <td>`sudo logdna-agent -s export LOGDNA_APIHOST=api.us-east.logging.cloud.ibm.com`</td>
      </tr>
    </table>

4. Set the ingestion endpoint. Choose the public or the private endpoint in a location.

    <table>
      <caption>Commands by region </caption>
      <tr>
        <th>Location</th>
        <th>Command (By using public endpoints)</th>
        <th>Command (By using private endpoints)</th>
      </tr>
      <tr>
        <td>`Chennai (in-che)`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.in-che.logging.cloud.ibm.com`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.private.in-che.logging.cloud.ibm.com` </br></br>`export LDLOGHOST=logs.private.in-che.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`Dallas (us-south)`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.private.us-south.logging.cloud.ibm.com` </br></br>`export LDLOGHOST=logs.private.us-south.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`Frankfurt (eu-de)`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.eu-de.logging.cloud.ibm.com`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.private.eu-de.logging.cloud.ibm.com` </br></br>`export LDLOGHOST=logs.private.eu-de.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`London (eu-gb)`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.eu-gb.logging.cloud.ibm.com`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.private.eu-gb.logging.cloud.ibm.com` </br></br>`export LDLOGHOST=logs.private.eu-gb.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`Tokyo (jp-tok)`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.jp-tok.logging.cloud.ibm.com`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.private.jp-tok.logging.cloud.ibm.com` </br></br>`export LDLOGHOST=logs.private.jp-tok.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`Seoul (kr-seo)`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.kr-seo.logging.cloud.ibm.com`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.private.kr-seo.logging.cloud.ibm.com` </br></br>`export LDLOGHOST=logs.private.kr-seo.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`Sydney (au-syd)`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.au-syd.logging.cloud.ibm.com`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.private.au-syd.logging.cloud.ibm.com` </br></br>`export LDLOGHOST=logs.private.au-syd.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`Washington (us-east)`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-east.logging.cloud.ibm.com`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.private.us-east.logging.cloud.ibm.com` </br></br>`export LDLOGHOST=logs.private.us-east.logging.cloud.ibm.com`</td>
      </tr>
    </table>

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

