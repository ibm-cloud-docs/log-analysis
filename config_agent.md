---

copyright:
  years:  2018, 2019
lastupdated: "2019-02-28"

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
* The agent tails for new log data, and looks for new files that have been added to the logging directories that the agent monitors.

There are different parameters that you can configure to customize the LogDNA agent: 

| Parameter | Description |
|-----------|-------------|
| `tags`    | Define tags to group hosts automatically into dynamic groups. |
| `logdir`  | Define custom paths that you want the agent to monitor. </br>Separate multiple paths by using commas. You can use glob patterns. You can configure specific files. Enter glob patterns by using double quotes. |
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
   ibmcloud login -a api.ng.bluemix.net
   ```
   {: pre}

   Select the account where you have provisioned the {{site.data.keyword.la_full_notm}} instance.

2. Set the cluster where you want to configure logging as the context for this session.

   ```
   ibmcloud ks cluster-config <cluster_name_or_ID>
   ```
   {: pre}

   When the download of the configuration files is finished, a command is displayed that you can use to set the path to the local Kubernetes configuration file as an environment variable. Copy and paste the command that is displayed in your terminal to set the `KUBECONFIG` environment variable.

   Every time you log in to the {{site.data.keyword.containerlong_notm}} CLI to work with your cluster, you must run this setup to set the path to the cluster's configuration file as a session variable. {{site.data.keyword.containerlong_notm}} uses this variable to find a local configuration file and certificates that are necessary to connect with your cluster.
   {: tip}

3. Create a Kubernetes secret to store your logDNA ingestion key for your service instance. The LogDNA ingestion key is used to open a secure web socket to the logDNA ingestion server and to authenticate the logging agent with the {{site.data.keyword.la_full_notm}} service.

   ```
   kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<logDNA_ingestion_key>
   ```
   {: pre}

4. Create a Kubernetes daemon set to deploy the LogDNA agent on every worker node of your Kubernetes cluster. The LogDNA agent collects logs with the extension `*.log` and extensionsless files that are stored in the `/var/log` directory of your pod. By default, logs are collected from all namespaces, including `kube-system`, and automatically forwarded to the {{site.data.keyword.la_full_notm}} service.

   ```
   kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
   ```
   {: pre}

5. Verify that the LogDNA agent is deployed successfully. 

   ```
   kubectl get pods
   ```
   {: pre}
   

The deployment is successful when you see one or more LogDNA pods.
* **The number of LogDNA pods equals the number of worker nodes in your cluster.** 
* All pods must be in a `Running` state.
* *Stdout* and *stderr* is automaticaly collected and forwarded from all containers. Log data include application logs and worker logs. 
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

    **Note:** Every time you log in to the {{site.data.keyword.containerlong}} CLI to work with clusters, you must run these commands to set the path to the cluster's configuration file as a session variable. The Kubernetes CLI uses this variable to find a local configuration file and certificates that are necessary to connect with the cluster in {{site.data.keyword.cloud_notm}}.

2. Check the update strategy of the DaemonSet. Then, choose whether to use *kubectl apply* or *kubectl edit* to modify the configuration file for the agent.

    To check the update strategy, run the following command:

    ```
    kubectl get ds/logdna-agent -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'
    ```
    {: pre}

    Option 1: If the update strategy is set to *OnDelete* or if you have the configuration file managed through a version control system, update your local configuration file. Then, apply those changes to the LogDNA agent by using *kubectl apply*.

    Option 2: If the update strategy is set to *RollingUpdate*, you can update and apply changes to the LogDNA agent by using *kubectl edit*.

3. Edit the *logdna-agent-configmap.yaml* file. 

    Option 1: Update the configuration file by modifying the local copy. **Note:** You can also generate the configuration file of the agent by running the following command:

    ```
    kubectl get configmap logdna-agent -o=yaml > prod-logdna-agent-configmap.yaml
    ```
    {: codeblock}

    Option 2: Update the configuration file by using *kubectl edit*:

    ```
    kubectl edit configmap logdna-agent
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
    kubectl apply -f logdna-agent-configmap.yaml
    ```
    {: codeblock}
    
    **Note:** If you use *kubectl edit*, changes are applied automatically when you save your modifications.


## Configuring a LogDNA agent on Linux Ubuntu/Debian
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

    where INGESTION_KEY contains the ingestion key active for the {{site.data.keyword.la_full_notm}} instance where you are configuring to forward logs.

3. Set the authentication endpoint. The LogDNA agent uses this host to authenticate and get the token to forward logs.

    ```
    sudo logdna-agent -s LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com
    ```
    {: codeblock}

4. Set the ingestion endpoint.

    ```
    sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com
    ```
    {: codeblock}

5. Define more log paths to be monitored. Run the following command: 

    ```
    sudo logdna-agent -d /path/to/log/folders
    ```
    {: codeblock}

    By default, **/var/log** is monitored.

6. Optionally, configure the LogDNA agent to tag your hosts. 


## Adding tags to a LogDNA agent on Linux Ubuntu/Debian
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









