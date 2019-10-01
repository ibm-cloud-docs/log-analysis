---

copyright:
  years:  2018, 2019
lastupdated: "2019-10-01"

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

# Configuring a LogDNA agent for a standard Kubernetes cluster
{: #config_agent_kube_cluster}

The LogDNA agent is responsible for collecting and forwarding logs to your {{site.data.keyword.la_full_notm}} instance. After you provision an instance of {{site.data.keyword.la_full}}, you must configure a LogDNA agent for each log source that you want to monitor.
{:shortdesc}


## Configuring a LogDNA agent on a standard Kubernetes cluster by using a script
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
   ibmcloud ks cluster config --cluster <cluster_name_or_ID>
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
      <tr>
        <td>`Seoul (kr-seo)`</td>
        <td>`kubectl create -f https://assets.kr-seo.logging.cloud.ibm.com/clients/logdna-agent-ds.yaml`</td>
        <td>`kubectl create -f https://assets.kr-seo.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml`</td>
      </tr>
      <tr>
        <td>`Sydney (au-syd)`</td>
        <td>`kubectl create -f https://assets.au-syd.logging.cloud.ibm.com/clients/logdna-agent-ds.yaml`</td>
        <td>`kubectl create -f https://assets.au-syd.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml`</td>
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



## Adding tags at the LogDNA agent level
{: #config_agent_kube_tags}

You can configure tags at the agent level so that all lines that are sent by this agent can be grouped automatically into a group when you filter data in a view.

You can define multiple tags. You separate tags by using commas. The maximum number of characters that you can set to define multiple tags is 80 characters.

Complete the following steps to add tags to a cluster:

1. Set up the cluster environment. Run the following commands:

    First, get the command to set the environment variable and download the Kubernetes configuration files.

    ```
    ibmcloud ks cluster config --cluster <cluster_name_or_ID>
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



## Excluding log files through the LogDNA agent
{: #config_agent_kube_exclude}

You can stop logs from being forwarded to your logging instance by modifying the LogDNA agent configuration file to exclude any files that you do not want the LogDNA agent to monitor. 

* You can exclude files that are located in any of the paths that are defined through the **logdir** parameter. 
* To define the files, you can separate multiple files by using commas. You can use glob patterns. You can also configure specific files.

Complete the following steps to configure the agent so that only application logs are forwarded and cluster logs are excluded:

1. Set up the cluster environment. Run the following commands:

    First, get the command to set the environment variable and download the Kubernetes configuration files.

    ```
    ibmcloud ks cluster config --cluster <cluster_name_or_ID>
    ```
    {: codeblock}

    When the download of the configuration files is finished, a command is displayed that you can use to set the path to the local Kubernetes configuration file as an environment variable.

    Then, copy and paste the command that is displayed in your terminal to set the KUBECONFIG environment variable.

2. Generate the configuration file of the agent by running the following command:

    ```
    kubectl get daemonset logdna-agent -o=yaml > prod-logdna-agent-ds.yaml
    ```
    {: codeblock}

2. Make changes. Add the section **LOGDNA_EXCLUDE**, and exclude all cluster logs. Add the following section to the yaml file:

    ```
    - name: LOGDNA_EXCLUDE
      value: /var/log/containers/*_kube-system_*,/var/log/containers/*ibm-observe_*,/var/log/containerd.log,/var/log/kubelet.log,/var/log/syslog,/var/log/ntpstats/*,/var/log/alb/*
    ```
    {: codeblock}

    You can also exclude logs by namespace. For example, to exclude all of the *kube-system* logs, enter:

    ```
    - name: LOGDNA_EXCLUDE
      value: /var/log/containers/*_kube-system_*
    ```
    {: codeblock}

    To exclude all non-container logs, that is, to exclude files as shown in the *All Apps* filter view, enter:

    ```
    - name: LOGDNA_EXCLUDE
      value: /var/log/!(containers)*
    ```
    {: codeblock}

    To exclude calico logs, enter:

    ```
    - name: LOGDNA_EXCLUDE
      value: /var/log/containers/calico*
    ```
    {: codeblock}

    To exclude all of the _kube-system_ logs and all non-container logs, enter:

    ```
    - name: LOGDNA_EXCLUDE
      value: /var/log/!(containers)*,/var/log/containers/*_kube-system_*
    ```
    {: codeblock}

3. Apply the configuration changes. Run the following command:

    ```
    kubectl apply -f prod-logdna-agent-ds.yaml
    ```
    {: codeblock}

4. Get the logdna-agent pods. Run the following command:

    ```
    kubectl get pods
    ```
    {: codeblock}

5. Delete all the logdna pods that are listed in the previous step.

    ```
    kubectl delete pod PodName
    ```
    {: codeblock}

6. Verify that log entries are not showing in the LogDNA web UI.


