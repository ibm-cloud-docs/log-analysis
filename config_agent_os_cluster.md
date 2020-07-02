---

copyright:
  years:  2018, 2020
lastupdated: "2020-05-11"

keywords: LogDNA, IBM, Log Analysis, logging, config agent

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
{:external: target="_blank" .external}

# Connecting a LogDNA agent to an OpenShift cluster
{: #config_agent_os_cluster}

The LogDNA agent is responsible for collecting and forwarding logs to your {{site.data.keyword.la_full_notm}} instance. After you provision an instance of {{site.data.keyword.la_full}}, you must configure a LogDNA agent for each log source that you want to monitor.
{:shortdesc}

To configure your Kubernetes cluster to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install a *LogDNA-agent* pod on each node of your cluster. The LogDNA agent reads log files from the pod where it is installed, and forwards the log data to your LogDNA instance.



## Deploy the LogDNA agent by using kubectl commands
{: #config_agent_os_kubectl}

Complete the following steps from the command line to configure your OpenShift cluster to forward logs to your LogDNA instance by using the default yaml file:


### Prereq
{: #config_agent_oscluster_prereq}

To deploy the LogDNA agent in a cluster, you must have a user ID that has the following IAM roles:
* **Viewer** platform role, and **Manager** service role to work with that cluster instance.
* **Viewer** permissions on the resource group where the cluster is available.

To configure the LogDNA agent in the cluster, you need the following CLIs:
* The {{site.data.keyword.cloud_notm}} CLI to log in to the {{site.data.keyword.cloud_notm}} by using `ibmcloud` commands, and to manage the cluster by using `ibmcloud ks` commands. [Learn more](/docs/containers?topic=containers-cs_cli_install#cs_cli_install_steps).
* The Kubernetes CLI to manage the cluster by using `kubectl` commands. [Learn more](/docs/containers?topic=containers-cs_cli_install#kubectl).
* The Openshift CLI to login to the cluster from the command line and deploy the agent. [Learn more](/docs/openshift?topic=openshift-openshift-cli).



### Step 1. Set the cluster context and log in to the cluster
{: #config_agent_oscluster_step1}

Complete the following steps:

1. Open a terminal to log in to {{site.data.keyword.cloud_notm}}.

   ```
   ibmcloud login -a cloud.ibm.com
   ```
   {: pre}

   Select the account where you provisioned the {{site.data.keyword.la_full_notm}} instance.

2. List the clusters to find out in which region and resource group the cluster is available.

    ```
    ibmcloud oc clusters
    ```
    {: pre}

3. Set the resource group and region.

    ```
    ibmcloud target -g RESOURCE_GROUP -r REGION
    ```
    {: pre}

    Where 
    
    `RESOURCE_GROUP` is the name of the resource group where the cluster is available, for example, `default`.
    
    `REGION` is the region where the cluster is available, for example, `us-south`.

4. Set the cluster context in your session.

    ```
    ibmcloud oc cluster config --cluster <cluster_name_or_ID>
    ```
    {: pre}

    When the download of the configuration files is finished, a command is displayed that you can use to set the path to the local Kubernetes configuration file as an environment variable. Copy and paste the command that is displayed in your terminal to set the KUBECONFIG environment variable.

5. Log in to the cluster. Choose a method to login to an OpenShift cluster. [Learn more about the methods to login](/docs/openshift?topic=openshift-access_cluster#access_automation).


### Step 2. Store your LogDNA ingestion key as a Kubernetes secret
{: #config_agent_os_cluster_step2}

You must create a Kubernetes secret to store your LogDNA ingestion key for your service instance. The LogDNA ingestion key is used to open a secure web socket to the LogDNA ingestion server and to authenticate the logging agent with the {{site.data.keyword.la_full_notm}} service.

1. Create a project. A project is a namespace in a cluster.

    ```
    oc adm new-project --node-selector='' ibm-observe
    ```
    {: pre}

    Set `--node-selector=''` to disable the default project-wide node selector in your namespace and avoid pod recreates on the nodes that got unselected by the merged node selector.

2. Create the service account **logdna-agent** in the cluster namespace **ibm-observe**. A service account is in Openshift what a service ID is in {{site.data.keyword.cloud_notm}}. Run the following command:

    ```
    oc create serviceaccount SERVICEACCOUNT_NAME -n PROJECT
    ```
    {: pre}

    Where

    `PROJECT` is the namespace where the LogDNA pods run. Set this value to **ibm-observe**.

    `SERVICEACCOUNT_NAME` is the name of the service account that you use to deploy the LogDNA agent. Set this value to **logdna-agent**. Notice that if you leave the service account name blank, the default service account is used instead of the service account that you created. 

    ```
    oc create serviceaccount logdna-agent -n ibm-observe
    ```
    {: pre}

4. Grant the serviceaccount access to the **Privileged SCC** so the service account has permissions to create priviledged LogDNA pods. Run the following command:

    ```
    oc adm policy add-scc-to-user privileged system:serviceaccount:PROJECT:SERVICEACCOUNT_NAME
    ```
    {: pre}

    Where

    `PROJECT` is the namespace where the LogDNA pods run. Set this value to **ibm-observe**.

    `SERVICEACCOUNT_NAME` is the name of the service account that you use to deploy the LogDNA agent. Set this value to **logdna-agent**.

    ```
    oc adm policy add-scc-to-user privileged system:serviceaccount:ibm-observe:logdna-agent
    ```
    {: pre}

5. Add a secret. The secret sets the ingestion key that the LogDNA agent uses to send logs.

    ```
    oc create secret generic logdna-agent-key --from-literal=logdna-agent-key=INGESTION_KEY -n PROJECT 
    ```
    {: pre}

    Where 
    
    `PROJECT` is the namespace where the LogDNA pods run. Set this value to **ibm-observe**.
    
    `INGESTION_KEY` is the ingestion key for the LogDNA instance where you plan to forward and collect the cluster logs. To get the ingestion key, see [Get the ingestion key through the IBM Log Analysis with LogDNA web UI](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-ingestion_key).


### Step 3. Enable virtual routing and forwarding (VRF)
{: #config_agent_os_cluster_step3}

This step is required if you plan to use private endpoints.  

You must enable virtual routing and forwarding (VRF) and connectivity to service endpoints for your account. [Learn more](/docs/account?topic=account-vrf-service-endpoint)

### Step 4. Deploy the LogDNA agent in the cluster
{: #config_agent_os_cluster_step4}

Create a Kubernetes daemon set to deploy the LogDNA agent on every worker node of your Kubernetes cluster. 

The LogDNA agent collects logs with the extension `*.log` and extensionsless files that are stored in the `/var/log` directory of your pod. By default, logs are collected from all namespaces, including `kube-system`, and automatically forwarded to the {{site.data.keyword.la_full_notm}} service.

Choose one of the following commands to install and configure the LogDNA agent version 1:

| Location                  | Command (By using public endpoints)               | 
|--------------------------|----------------------------------------------------|
| `Chennai (in-che)`       | `kubectl create -f https://assets.in-che.logging.cloud.ibm.com/clients/logdna-agent-ds-os.yaml -n ibm-observe`       |
| `Dallas (us-south)`      | `kubectl create -f https://assets.us-south.logging.cloud.ibm.com/clients/logdna-agent-ds-os.yaml -n ibm-observe`       |
| `Frankfurt (eu-de)`      | `kubectl create -f https://assets.eu-de.logging.cloud.ibm.com/clients/logdna-agent-ds-os.yaml -n ibm-observe`         |
| `London (eu-gb)`         | `kubectl create -f https://assets.eu-gb.logging.cloud.ibm.com/clients/logdna-agent-ds-os.yaml -n ibm-observe`          |
| `Tokyo (jp-tok)`         | `kubectl create -f https://assets.jp-tok.logging.cloud.ibm.com/clients/logdna-agent-ds-os.yaml -n ibm-observe`       |
| `Seoul (kr-seo)`         | `kubectl create -f https://assets.kr-seo.logging.cloud.ibm.com/clients/logdna-agent-ds-os.yaml -n ibm-observe` |
| `Sydney (au-syd)`        | `kubectl create -f https://assets.au-syd.logging.cloud.ibm.com/clients/logdna-agent-ds-os.yaml -n ibm-observe`        |
| `Washington (us-east)`   | `kubectl create -f https://assets.us-east.logging.cloud.ibm.com/clients/logdna-agent-ds-os.yaml -n ibm-observe`       |
{: caption="Table 1. Commands by location when you use public endpoints" caption-side="top"}
{: #end-api-table-1}
{: tab-title="Command (By using public endpoints)"}
{: tab-group="agent"}
{: class="simple-tab-table"}
{: row-headers}

| Location                  | Command (By using private endpoints)               | 
|--------------------------|----------------------------------------------------|
| `Chennai (in-che)`       | `kubectl create -f https://assets.in-che.logging.cloud.ibm.com/clients/logdna-agent-ds-os-private.yaml -n ibm-observe`       |
| `Dallas (us-south)`      | `kubectl create -f https://assets.us-south.logging.cloud.ibm.com/clients/logdna-agent-ds-os-private.yaml -n ibm-observe`      |
| `Frankfurt (eu-de)`      | `kubectl create -f https://assets.eu-de.logging.cloud.ibm.com/clients/logdna-agent-ds-os-private.yaml -n ibm-observe`          |
| `London (eu-gb)`         | `kubectl create -f https://assets.eu-gb.logging.cloud.ibm.com/clients/logdna-agent-ds-os-private.yaml -n ibm-observe`       |
| `Tokyo (jp-tok)`         | `kubectl create -f https://assets.jp-tok.logging.cloud.ibm.com/clients/logdna-agent-ds-os-private.yaml -n ibm-observe`        |
| `Seoul (kr-seo)`         | `kubectl create -f https://assets.kr-seo.logging.cloud.ibm.com/clients/logdna-agent-ds-os-private.yaml -n ibm-observe` |
| `Sydney (au-syd)`        | `kubectl create -f https://assets.au-syd.logging.cloud.ibm.com/clients/logdna-agent-ds-os-private.yaml -n ibm-observe`       |
| `Washington (us-east)`   | `kubectl create -f https://assets.us-east.logging.cloud.ibm.com/clients/logdna-agent-ds-os-private.yaml -n ibm-observe`      |
{: caption="Table 2. Commands by location when you use private endpoints" caption-side="top"}
{: #end-api-table-2}
{: tab-title="Command (By using private endpoints)"}
{: tab-group="agent"}
{: class="simple-tab-table"}
{: row-headers}


### Step 5. Verify that the LogDNA agent is deployed successfully
{: #config_agent_os_cluster_step5}

To verify that the LogDNA agent is deployed successfully, run the following command:

1. Target the project where the LogDNA agent is deployed.

    ```
    oc project ibm-observe
    ```
    {: pre}

2. Verify that the `logdna-agent` pods on each node are in a **Running** status.

    ```
    oc get pods -n PROJECT_NAME
    ```
    {: pre}

    For example, the following command lists all the pods in the namespace *ibm-observe*.

    ```
    oc get pods -n ibm-observe
    ```
    {: pre}


The deployment is successful when you see one or more LogDNA pods.
* **The number of LogDNA pods equals the number of worker nodes in your cluster.**
* All pods must be in a `Running` state.
* *Stdout* and *stderr* are automatically collected and forwarded from all containers. Log data includes application logs and worker logs.
* By default, the LogDNA agent pod that runs on a worker collects logs from all namespaces on that node.

After the agent is configured, you should start seeing logs from this cluster in the LogDNA web UI. If after a period of time you cannot see logs, check the agent logs.

To check the logs that are generated by a LogDNA agent, run the following command:

```
oc logs logdna-agent-<ID>
```
{: pre}

Where *ID* is the ID for a LogDNA agent pod. 

For example, 

```
oc logs logdna-agent-xxxkz
```
{: pre}


Next, launch the LogDNA web UI to verify that logs from the cluster are available through the UI. See [Navigating to the web UI](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-launch) and [Viewing logs](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-view_logs).





## Deploy the LogDNA agent within the context of the cluster
{: #config_agent_os_ob}

When you deploy and connect a LogDNA agent within the context of the cluster, consider the following information:
* You can launch the LogDNA web UI from the OpenShift cluster UI in {{site.data.keyword.cloud_notm}}. 
* The view that opens displays logs for your cluster. 
* The agent is deployed in the `ibm-observe` namespace.
* A tag that informs about the cluster name is associated to each log line as metadata.
* A tag that informs about the version of the agent is associated to each log line as metadata.
* The LogDNA instance must be available in the same {{site.data.keyword.cloud_notm}} account where the cluster is provisioned. 
* The LogDNA instance can be in a different resource group and {{site.data.keyword.cloud_notm}} region than your cluster.


Before you can deploy the LogDNA agent in a cluster, verify that you are assigned the following IAM roles: 
* **Viewer** permissions on the resource group where the cluster is available.
* **Viewer** permissions on the resource group where the LogDNA instance is available.
* **Viewer** platform role and **Writer** or **Manager** service role for the OpenShift service to configure the LogDNA agent.
* **Viewer** platform role, and **Reader** service role for the {{site.data.keyword.la_full_notm}} instance to launch the LogDNA UI, and analyze logs through the LogDNA web UI.

The minimum persmissions that a user must have to launch the LogDNA web UI from the cluster UI, and analyze cluster logs are the following:
* **Viewer** permissions on the resource group where the cluster is available.
* **Viewer** permissions on the resource group where the LogDNA instance is available.
* **Viewer** platform role and **Reader** service role for the OpenShift service to see the cluster and open the cluster's UI.
* **Viewer** platform role, and **Reader** service role for the {{site.data.keyword.la_full_notm}} instance to launch the LogDNA web UI, and analyze logs through the LogDNA web UI.

### Deploy the LogDNA agent from the OpenShift console
{: #config_agent_os_ob_ui}


Complete the following steps from the [OpenShift console](https://cloud.ibm.com/kubernetes/clusters?platformType=openshift){: external}:

1. Select the cluster for which you want to create a LogDNA logging configuration.

2. On the cluster **Overview** page, in the *Logging* section, click **Connect**.

    The page `Connect an existing IBM Log Analysis with LogDNA instance` opens.

3. Select the region where the LogDNA instance is provisioned.

4. Select the {{site.data.keyword.la_full_notm}} instance that you want to use to analyze your logs.

5. If your account is VRF-enabled, check the box **Use private endpoint** to keep all network traffic to your service instance on the private network.

    Your cluster must be set up with a private service endpoint to use this option. To enable the private service endpoint, use the cluster Overview page.
    {: note}

    To check if your account is VRF-enabled, run the following command:

    ```
    ibmcloud account show
    ```
    {: pre}

6. Click **Connect**.


### Deploy the LogDNA agent by using ob commands
{: #config_agent_os_ob_cli}


To configure the LogDNA agent in a cluster, complete the following steps:


1. [Pre-req] Install the OpenShift observability CLI plug-in (ibmcloud ob).

    ```
    ibmcloud plugin install observe-service
    ```
   {: pre}

2. Set the cluster context.

    Open a terminal to log in to {{site.data.keyword.cloud_notm}}.

    ```
    ibmcloud login -a cloud.ibm.com
    ```
    {: pre}

    Select the account where you provisioned the {{site.data.keyword.la_full_notm}} instance.

    List the clusters to find out in which region and resource group the cluster is available.

    ```
    ibmcloud ks clusters
    ```
    {: pre}

    Set the resource group and region.

    ```
    ibmcloud target -g RESOURCE_GROUP -r REGION
    ```
    {: pre}

    Where 
    
    `RESOURCE_GROUP` is the name of the resource group where the cluster is available, for example, `default`.
    
    `REGION` is the region where the cluster is available, for example, `us-south`.

    Set the cluster where you want to configure logging as the context for this session.

    ```
    ibmcloud oc cluster config --cluster <cluster_name_or_ID>
    ```
    {: pre}

3. Deploy the LogDNA agent by using the `ob` CLI. Run the following command:

    ```
    ibmcloud ob logging config create --cluster <cluster_name_or_ID> --instance <LogDNA_instance_name_or_ID> [--LogDNA-ingestion-key <Ingestion_Key>] [--private-endpoint]
    ```
    {: pre}

    Where

    * `<cluster_name_or_ID>` is the name or the ID of the cluster.

    * `<LogDNA_instance_name_or_ID>` is the name or the ID of the LogDNA instance where you want to forward the cluster logs for analysis.

    * `<Ingestion_Key>` is the ingestion key that you want to use to connect the LogDNA agent with the LogDNA instance.

    * `[--private-endpoint]` is optional. Add this option to connect to your LogDNA instance by using private service endpoints.











