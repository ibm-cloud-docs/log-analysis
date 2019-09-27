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

# Configuring a LogDNA agent
{: #config_agent_linux}

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


## Configuring a LogDNA agent on Linux Ubuntu or Debian
{: #config_agent_linux_steps}

To configure your Ubuntu server to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install a `logdna-agent`. The LogDNA agent reads log files from */var/log*, and forwards the log data to your LogDNA instance.

To configure your Ubuntu server to forward logs to your LogDNA instance, complete the following steps from an Ubuntu terminal:

1. Install the LogDNA agent. Run the following commands:

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

2. Set the ingestion key that the LogDNA agent must use to forward logs to the {{site.data.keyword.la_full_notm}} instance.  

    ```
    sudo logdna-agent -k INGESTION_KEY
    ```
    {: codeblock}

    Where INGESTION_KEY contains the ingestion key active for the {{site.data.keyword.la_full_notm}} instance where you are configuring to forward logs.

3. Set the authentication endpoint. The LogDNA agent uses this host to authenticate and get the token to forward logs. 

    <table>
      <caption>Commands by region</caption>
      <tr>
        <th>Location</th>
        <th>Command </th>

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
    </table>

5. Define more log paths to be monitored. Run the following command:

    ```
    sudo logdna-agent -d /path/to/log/folders
    ```
    {: codeblock}

    By default, **/var/log** is monitored.

6. Optionally, configure the LogDNA agent to tag your hosts.

7. Start the LogDNA agent.

    ```
    sudo /etc/init.d/logdna-agent start
    ```
    {: codeblock}

## Adding tags to a LogDNA agent on Linux Ubuntu or Debian
{: #config_agent-linux_tags}


Complete the following steps to add more tags to the LogDNA agent:

1. Verify the LogDNA agent is running.

2. Add one or more tags.

    ```
    sudo logdna-agent -t TAG1,TAG2
    ```
    {: codeblock}


You can also edit the LogDNA configuration file and add tags. The configuration file is located in */etc/logdna.conf*.

1. Edit the file.

    ```
    sudo update-rc.d logdna-agent defaults
    ```
    {: codeblock}

2. Add tags.

3. Restart the LogDNA agent.

    ```
    sudo /etc/init.d/logdna-agent start
    ```
    {: codeblock}
