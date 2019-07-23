---

copyright:
  years:  2018, 2019
lastupdated: "2019-07-17"

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
{: #config_agent}

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



## Configuring a LogDNA agent on a Kubernetes cluster by using a script
{: #config_agent_kube_script}

To configure your Kubernetes cluster to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install a *logdna-agent* pod on each node of your cluster. The LogDNA agent reads log files from the pod where it is installed, and forwards the log data to your LogDNA instance.

To configure your Kubernetes cluster to forward logs to your LogDNA instance, complete the following steps from the command line:

1. Open a terminal to log in to {{site.data.keyword.cloud_notm}}.

   ```
   ibmcloud login -a cloud.ibm.com
   ```
   {: pre}

   Select the account where you provisioned the {{site.data.keyword.la_full_notm}} instance.

2. Set the cluster where you want to configure logging as the context for this session.

   ```
   ibmcloud ks cluster-config <cluster_name_or_ID>
   ```
   {: pre}

   When the download of the configuration files is finished, a command is displayed that you can use to set the path to the local Kubernetes configuration file as an environment variable. Copy and paste the command that is displayed in your terminal to set the `KUBECONFIG` environment variable.

3. Create a Kubernetes secret to store your logDNA ingestion key for your service instance. The LogDNA ingestion key is used to open a secure web socket to the logDNA ingestion server and to authenticate the logging agent with the {{site.data.keyword.la_full_notm}} service.

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<logDNA_ingestion_key>
    ```
    {: pre}

4. [Required if you plan to use private endpoints] [Enable virtual routing and forwarding (VRF)](/docs/account?topic=account-vrf-service-endpoint) and connectivity to service endpoints for your account.

5. Create a Kubernetes daemon set to deploy the LogDNA agent on every worker node of your Kubernetes cluster. The LogDNA agent collects logs with the extension `*.log` and extensionsless files that are stored in the `/var/log` directory of your pod. By default, logs are collected from all namespaces, including `kube-system`, and automatically forwarded to the {{site.data.keyword.la_full_notm}} service.

    <table>
      <caption>Commands by location</caption>
      <tr>
        <th>Location</th>
        <th>Command (By using public endpoints)</th>
        <th>Command (By using private endpoints)</th>
      </tr>
      <tr>
        <td>`Dallas (us-south)`</td>
        <td>`kubectl create -f https://assets.us-south.logging.cloud.ibm.com/clients/logdna-agent-ds.yaml`</td>
        <td>`kubectl create -f https://assets.us-south.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml`</td>
      </tr>
      <tr>
        <td>`Frankfurt (eu-de)`</td>
        <td>`kubectl create -f https://assets.eu-de.logging.cloud.ibm.com/clients/logdna-agent-ds.yaml`</td>
        <td>`kubectl create -f https://assets.eu-de.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml`</td>
      </tr>
      <tr>
        <td>`London (eu-gb)`</td>
        <td>`kubectl create -f https://assets.eu-gb.logging.cloud.ibm.com/clients/logdna-agent-ds.yaml`</td>
        <td>`kubectl create -f https://assets.eu-gb.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml`</td>
      </tr>
      <tr>
        <td>`Tokyo (jp-tok)`</td>
        <td>`kubectl create -f https://assets.jp-tok.logging.cloud.ibm.com/clients/logdna-agent-ds.yaml`</td>
        <td>`kubectl create -f https://assets.jp-tok.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml`</td>
      </tr>
    </table>

6. Verify that the LogDNA agent is deployed successfully.

   ```
   kubectl get pods
   ```
   {: pre}


The deployment is successful when you see one or more LogDNA pods.
* **The number of LogDNA pods equals the number of worker nodes in your cluster.**
* All pods must be in a `Running` state.
* *Stdout* and *stderr* are automatically collected and forwarded from all containers. Log data includes application logs and worker logs.
* By default, the LogDNA agent pod that runs on a worker collects logs from all namespaces on that node, including kube-system logs.



## Adding tags to a LogDNA agent on a Kubernetes cluster
{: #config_agent_kube_tags}

Complete the following steps to add tags:

1. Set up the cluster environment. Run the following commands:

    First, get the command to set the environment variable and download the Kubernetes configuration files.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    When the download of the configuration files is finished, a command is displayed that you can use to set the path to the local Kubernetes configuration file as an environment variable.

    Then, copy and paste the command that is displayed in your terminal to set the KUBECONFIG environment variable.

2. Check the update strategy of the DaemonSet. Then, choose whether to use *kubectl apply* or *kubectl edit* to modify the configuration file for the agent.

    To check the update strategy, run the following command:

    ```
    kubectl get ds/logdna-agent -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'
    ```
    {: pre}

    If the update strategy is set to *OnDelete* or if you have the configuration file that is managed through a version control system, update your local configuration file and apply changes to the LogDNA agent by using *kubectl apply*.

    If the update strategy is set to *RollingUpdate*, you can update and apply changes to the LogDNA agent by using *kubectl edit*.

3. Edit the `logdna-agent-configmap.yaml` file.

    Update the configuration file by modifying the local copy. **Note:** You can also generate the configuration file of the agent by running the following command:

    ```
    kubectl get daemonset logdna-agent -o=yaml > prod-logdna-agent-ds.yaml
    ```
    {: codeblock}

    Alternatively, update the configuration file by using *kubectl edit*.

    ```
    kubectl edit daemonset logdna-agent
    ```
    {: codeblock}

4. Make changes. Add the section **LOGDNA_TAGS**.

    ```
    - name: LOGDNA_TAGS
        value: tag1,tag2,tag3
    ```
    {: codeblock}

    For example, the following section shows where to add tags in the configuration file:

    ```
    apiVersion: extensions/v1beta1
    kind: DaemonSet
    metadata:
      name: logdna-agent
    spec:
      template:
        metadata:
          labels:
            app: logdna-agent
        spec:
          containers:
          - name: logdna-agent
            image: logdna/logdna-agent:latest
            imagePullPolicy: Always
            env:
            - name: LOGDNA_AGENT_KEY
              valueFrom:
                 secretKeyRef:
                  name: logdna-agent-key
                  key: logdna-agent-key
            - name: LDAPIHOST
              value: api.us-south.logging.cloud.ibm.com
            - name: LDLOGHOST
              value: logs.us-south.logging.cloud.ibm.com
            - name: LOGDNA_PLATFORM
              value: k8s
            - name: LOGDNA_TAGS
              value: tag1,tag2,tag3
    ```
    {: screen}

5. Apply configuration changes if you edit the file locally.

    ```
    kubectl apply -f prod-logdna-agent-ds.yaml
    ```
    {: codeblock}

    **Note:** If you use *kubectl edit*, changes are applied automatically when you save your modifications.


## Configuring a LogDNA agent on Linux Ubuntu or Debian
{: #config_agent_linux}

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

3. Set the authentication endpoint. The LogDNA agent uses this host to authenticate and get the token to forward logs. Choose the public or the private endpoint in a location.

    <table>
      <caption>Commands by region</caption>
      <tr>
        <th>Location</th>
        <th>Command (By using public endpoints)</th>
        <th>Command (By using private endpoints)</th>
      </tr>
      <tr>
        <td>`Dallas (us-south)`</td>
        <td>`sudo logdna-agent` </br> `export LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com`</td>
        <td>`sudo logdna-agent` </br> `export LOGDNA_APIHOST=api.private.us-south.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`Frankfurt (eu-de)`</td>
        <td>`sudo logdna-agent` </br> `export LOGDNA_APIHOST=api.eu-de.logging.cloud.ibm.com`</td>
        <td>`sudo logdna-agent` </br> `export LOGDNA_APIHOST=api.private.eu-de.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`London (eu-gb)`</td>
        <td>`sudo logdna-agent` </br> `export LOGDNA_APIHOST=api.eu-gb.logging.cloud.ibm.com`</td>
        <td>`sudo logdna-agent` </br> `export LOGDNA_APIHOST=api.private.eu-gb.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`Tokyo (jp-tok)`</td>
        <td>`sudo logdna-agent` </br> `export LOGDNA_APIHOST=api.jp-tok.logging.cloud.ibm.com`</td>
        <td>`sudo logdna-agent` </br> `export LOGDNA_APIHOST=api.private.jp-tok.logging.cloud.ibm.com`</td>
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
        <td>`sudo logdna-agent` </br> `export LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com`</td>
        <td>`sudo logdna-agent` </br> `export LOGDNA_LOGHOST=logs.private.us-south.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`Frankfurt (eu-de)`</td>
        <td>`sudo logdna-agent` </br> `export LOGDNA_LOGHOST=logs.eu-de.logging.cloud.ibm.com`</td>
        <td>`sudo logdna-agent` </br> `export LOGDNA_LOGHOST=logs.private.eu-de.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`London (eu-gb)`</td>
        <td>`sudo logdna-agent` </br> `export LOGDNA_LOGHOST=logs.eu-gb.logging.cloud.ibm.com`</td>
        <td>`sudo logdna-agent` </br> `export LOGDNA_LOGHOST=logs.private.eu-gb.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`Tokyo (jp-tok)`</td>
        <td>`sudo logdna-agent` </br> `export LOGDNA_LOGHOST=logs.jp-tok.logging.cloud.ibm.com`</td>
        <td>`sudo logdna-agent` </br> `export LOGDNA_LOGHOST=logs.private.jp-tok.logging.cloud.ibm.com`</td>
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
