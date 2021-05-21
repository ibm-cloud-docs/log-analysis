---

copyright:
  years:  2018, 2021
lastupdated: "2021-05-21"

keywords: IBM, Log Analysis, logging, config agent

subcollection: log-analysis

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

# Connecting a logging agent to a standard Kubernetes cluster
{: #config_agent_kube_cluster}

The logging agent is responsible for collecting and forwarding logs to your {{site.data.keyword.la_full_notm}} instance. After you provision an instance of {{site.data.keyword.la_full}}, you must configure a logging agent for each log source that you want to monitor.
{:shortdesc}

To configure your Kubernetes cluster to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install the logging agent in your cluster. 
* The agent deploys a a logdna-agent pod on each node of your cluster. 
* The logging agent reads log files from the pod where it is installed, and forwards the log data to your logging instance.


## Deploy the logging agent by using kubectl commands
{: #config_agent_kube_kubectl}

Complete the following steps from the command line to configure your Kubernetes cluster to forward logs to your logging instance by using the default YAML file:


### Prereq
{: #config_agent_kube_cluster_prereq}

To deploy the logging agent in a cluster, you must have a user ID that has the following IAM roles:
* **Viewer** platform role, and **Writer** or **Manager** service role to work with that cluster instance.
* **Viewer** permissions on the resource group where the cluster is available.

To configure the logging agent in the cluster, you need the following CLIs:
* The {{site.data.keyword.cloud_notm}} CLI to log in to the {{site.data.keyword.cloud_notm}} by using `ibmcloud` commands, and to manage the cluster by using `ibmcloud ks` commands. [Learn more](/docs/containers?topic=containers-cs_cli_install#cs_cli_install_steps).
* The Kubernetes CLI to manage the cluster by using `kubectl` commands. [Learn more](/docs/containers?topic=containers-cs_cli_install#kubectl).

### Step 1. Set the cluster context
{: #config_agent_kube_cluster_step1}


1. Open a terminal to log in to {{site.data.keyword.cloud_notm}}.

   ```
   ibmcloud login -a cloud.ibm.com
   ```
   {: pre}

   Select the account where you provisioned the {{site.data.keyword.la_full_notm}} instance.

2. List the clusters to find out in which region and resource group the cluster is available.

    ```
    ibmcloud ks clusters
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

4. Set the cluster where you want to configure logging as the context for this session.

   ```
   ibmcloud ks cluster config --cluster <cluster_name_or_ID>
   ```
   {: pre}

### Step 2. Create the ibm-observe namespace
{: #config_agent_kube_cluster_step2}

Observability services are deployed in the `ibm-observe` namespace. 
{: note}

First, check if the namespace exists. Run the following command:

```
kubectl get namespaces
```
{: pre}

Verify the `ibm-observe` namespace is active.

If you need to create the namespace, run the following command:

```
kubectl create namespace ibm-observe
```
{: pre}


### Step 3. Store your logging ingestion key as a Kubernetes secret
{: #config_agent_kube_cluster_step3}

Create a Kubernetes secret to store your logging ingestion key for your service instance. 

The logging ingestion key is used to open a secure web socket to the logging ingestion server and to authenticate the logging agent with the {{site.data.keyword.la_full_notm}} service.

Run the following command:

```
kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<LogDNA_ingestion_key> -n ibm-observe
```
{: pre}

To get the ingestion key, see [Get the ingestion key through the logging UI](/docs/log-analysis?topic=log-analysis-ingestion_key).

### Step 4. Enable virtual routing and forwarding (VRF)
{: #config_agent_kube_cluster_step4}

This step is required if you plan to use private endpoints.  

You must enable virtual routing and forwarding (VRF) and connectivity to service endpoints for your account. [Learn more](/docs/account?topic=account-vrf-service-endpoint)

### Step 5. Deploy the logging agent in the cluster
{: #config_agent_kube_cluster_step5}

Create a Kubernetes daemonset to deploy the logging agent on every worker node of your Kubernetes cluster. 

The logging agent collects the following logs:
- STDOUT and STDERR
- Logs with the extension `*.log`, and extensionsless files that are stored in the `/var/log` directory of your pod. 
By default, logs are collected from all namespaces, including `kube-system`, and automatically forwarded to the {{site.data.keyword.la_full_notm}} service.


#### Logging agent V2 and V3
{: #config_agent_kube_cluster_step5-vx}

The logging agent version 2 and version 3 are supported for Kubernetes 1.9+ and later.
{: note}

To configure the logging agent by using `kubectl` commands, run the following command:

| Type of endpoint | Command |
|------------------|---------|
| Public endpoint  | `kubectl apply -f https://assets.<REGION>.logging.cloud.ibm.com/clients/logdna-agent/<VERSION>/agent-resources.yaml` |
| Private endpoint | `kubectl apply -f https://assets.<REGION>.logging.cloud.ibm.com/clients/logdna-agent/<VERSION>/agent-resources-private.yaml` |

Where

- `<REGION>` indicates the region where the logging instance is available. For more information about regions, see [Locations](/docs/log-analysis?topic=log-analysis-regions).
- `<VERSION>` indicates the version of the agent that you want to deploy. You must use a version that has a tag with the following format: `X.Y.Z`. 

If you need to use a version that has a tag with any of the following formats: `X.Y.Z-<date>.[hash]`, `X`, or `X.Y`, you must download the agent yaml file and modify it. Replace the version for all entries `app.kubernetes.io/version` in the file with the one that you want to use. You must download the yaml file that has the format `X.Y.Z`. Then, after you make the version changes, you can run `kubectl apply -f <CUSTOM_YAML_FILE>` to deploy the agent.
{: important}

For more information about the agent tags, see [Understanding image tags](/docs/log-analysis?topic=log-analysis-log_analysis_agent#log_analysis_agent_image_kube_tags).

For more information about the versions that are available, see [Getting information about Kubernetes logging agent images](/docs/log-analysis?topic=log-analysis-log-analysis_agent_image).

For example, to configure an agent that sends data to a logging instance in Dallas, you must run the following command:

```
kubectl apply -f https://assets.us-south.logging.cloud.ibm.com/clients/logdna-agent/3.1.0/agent-resources.yaml
```
{: screen}


#### Logging agent V1
{: #config_agent_kube_cluster_step5-v1}


The logging agent version 1 is supported for Kubernetes 1.2 to 1.8 only.
{: important}

Choose one of the following commands to install and configure the logging agent version 2 by using `kubectl` commands:


| Location                 | Command (By using public endpoints)               | 
|--------------------------|----------------------------------------------------|
| `Chennai (in-che)`       | `kubectl create -f https://assets.in-che.logging.cloud.ibm.com/clients/logdna-agent-ds-k8s-v1.8.yaml -n ibm-observe`       |
| `Tokyo (jp-tok)`         | `kubectl create -f https://assets.jp-tok.logging.cloud.ibm.com/clients/logdna-agent-ds-k8s-v1.8.yaml -n ibm-observe`       |
| `Seoul (kr-seo)`         | `kubectl create -f https://assets.kr-seo.logging.cloud.ibm.com/clients/logdna-agent-ds-k8s-v1.8.yaml -n ibm-observe` |
| `Sydney (au-syd)`        | `kubectl create -f https://assets.au-syd.logging.cloud.ibm.com/clients/logdna-agent-ds-k8s-v1.8.yaml -n ibm-observe`        |
| `Osaka (jp-osa)`         | `kubectl create -f https://assets.jp-osa.logging.cloud.ibm.com/clients/logdna-agent-ds-k8s-v1.8.yaml -n ibm-observe`        |
| `Frankfurt (eu-de)`      | `kubectl create -f https://assets.eu-de.logging.cloud.ibm.com/clients/logdna-agent-ds-k8s-v1.8.yaml -n ibm-observe`         |
| `London (eu-gb)`         | `kubectl create -f https://assets.eu-gb.logging.cloud.ibm.com/clients/logdna-agent-ds-k8s-v1.8.yaml -n ibm-observe`          |
| `Toronto (ca-tor)`       | `kubectl create -f https://assets.ca-tor.logging.cloud.ibm.com/clients/logdna-agent-ds-k8s-v1.8.yaml -n ibm-observe`       |
| `Dallas (us-south)`      | `kubectl create -f https://assets.us-south.logging.cloud.ibm.com/clients/logdna-agent-ds-k8s-v1.8.yaml -n ibm-observe`       |
| `Washington (us-east)`   | `kubectl create -f https://assets.us-east.logging.cloud.ibm.com/clients/logdna-agent-ds-k8s-v1.8.yaml -n ibm-observe`       |
{: caption="Table 1. Commands by location when you use public endpoints" caption-side="top"}
{: #end-api-table-1}
{: tab-title="Command (By using public endpoints)"}
{: tab-group="agent"}
{: class="simple-tab-table"}
{: row-headers}

| Location                  | Command (By using private endpoints)               | 
|--------------------------|----------------------------------------------------|
| `Chennai (in-che)`       | `kubectl create -f https://assets.in-che.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe`       |
| `Tokyo (jp-tok)`         | `kubectl create -f https://assets.jp-tok.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe`        |
| `Seoul (kr-seo)`         | `kubectl create -f https://assets.kr-seo.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe` |
| `Sydney (au-syd)`        | `kubectl create -f https://assets.au-syd.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe`       |
| `Osaka (jp-osa)`         | `kubectl create -f https://assets.jp-osa.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe`       |
| `Frankfurt (eu-de)`      | `kubectl create -f https://assets.eu-de.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe`          |
| `London (eu-gb)`         | `kubectl create -f https://assets.eu-gb.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe`       |
| `Toronto (ca-tor)`       | `kubectl create -f https://assets.ca-tor.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe`      |
| `Dallas (us-south)`      | `kubectl create -f https://assets.us-south.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe`      |
| `Washington (us-east)`   | `kubectl create -f https://assets.us-east.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe`      |
{: caption="Table 2. Commands by location when you use private endpoints" caption-side="top"}
{: #end-api-table-2}
{: tab-title="Command (By using private endpoints)"}
{: tab-group="agent"}
{: class="simple-tab-table"}
{: row-headers}




### Step 6. Verify that the logging agent is deployed successfully
{: #config_agent_kube_cluster_step6}

To verify that the logging agent is deployed successfully, run any of the following commands:

```
kubectl get all -n ibm-observe
```
{: pre}

```
kubectl get pods -n ibm-observe
```
{: pre}


The deployment is successful when you see one or more logging pods.
* **The number of logging pods equals the number of worker nodes in your cluster.**
* All pods must be in a `Running` state.
* *Stdout* and *stderr* are automatically collected and forwarded from all containers. Log data includes application logs and worker logs.
* By default, the logging agent pod that runs on a worker collects logs from all namespaces on that node, including kube-system logs.

To get a copy of the logging agent configuration that is deployed, you can run the following command: 

```
 kubectl get daemonset logdna-agent -o=yaml > prod-logdna-agent-ds.yaml -n ibm-observe
```
{: pre}




## Deploy the logging agent within the context of the cluster
{: #config_agent_kube_ob}

When you deploy and connect a logging agent within the context of the cluster, consider the following information:
* You can launch the logging UI from the Kubernetes cluster UI in {{site.data.keyword.cloud_notm}}. 
* The view that opens displays logs for your cluster. 
* The agent is deployed in the `ibm-observe` namespace.
* A tag that informs about the cluster name is associated to each log line as metadata.
* A tag that informs about the version of the agent is associated to each log line as metadata.
* The logging instance must be available in the same {{site.data.keyword.cloud_notm}} account where the cluster is provisioned. 
* The logging instance can be in a different resource group and {{site.data.keyword.cloud_notm}} region than your cluster.


Before you can deploy the logging agent in a cluster, verify that you are assigned the following IAM roles: 
* **Viewer** permissions on the resource group where the cluster is available.
* **Viewer** permissions on the resource group where the logging instance is available.
* **Viewer** platform role and **Writer** or **Manager** service role for the {{site.data.keyword.containerlong_notm}} service to configure the logging agent.
* **Viewer** platform role, and **Reader** service role for the {{site.data.keyword.la_full_notm}} instance to launch the logging UI, and analyze logs through the logging UI.

The minimum persmissions that a user must have to launch the logging UI from the cluster UI, and analyze cluster logs are the following:
* **Viewer** permissions on the resource group where the cluster is available.
* **Viewer** permissions on the resource group where the logging instance is available.
* **Viewer** platform role and **Reader** service role for the {{site.data.keyword.containerlong_notm}} service to see the cluster and open the cluster's UI.
* **Viewer** platform role, and **Reader** service role for the {{site.data.keyword.la_full_notm}} instance to launch the logging UI, and analyze logs through the logging UI.

### Deploy the logging agent from the {{site.data.keyword.containerlong_notm}} console
{: #config_agent_kube_ob_ui}


Complete the following steps from the [{{site.data.keyword.containerlong_notm}} console](https://cloud.ibm.com/kubernetes/clusters){: external}:

1. Select the cluster for which you want to create a logging logging configuration.

2. On the cluster **Overview** page, in the *Logging* section, click **Connect**.

    The page `Connect an existing IBM Log Analysis with logging instance` opens.

3. Select the region where the logging instance is provisioned.

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


### Deploy the logging agent by using ob commands
{: #config_agent_kube_ob_cli}


To configure the logging agent in a cluster, complete the following steps:


1. [Pre-req] Install the {{site.data.keyword.containerlong_notm}} observability CLI plug-in (ibmcloud ob).

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
    ibmcloud ks cluster config --cluster <cluster_name_or_ID>
    ```
    {: pre}

3. Deploy the logging agent by using the `ob` CLI. Run the following command:

    ```
    ibmcloud ob logging config create --cluster <cluster_name_or_ID> --instance <instance_name_or_ID> [--LogDNA-ingestion-key <Ingestion_Key>] [--private-endpoint]
    ```
    {: pre}

    Where

    * `<cluster_name_or_ID>` is the name or the ID of the cluster.

    * `<instance_name_or_ID>` is the name or the ID of the logging instance where you want to forward the cluster logs for analysis.

    * `<Ingestion_Key>` is the ingestion key that you want to use to connect the logging agent with the logging instance.

    * `[--private-endpoint]` is optional. Add this option to connect to your logging instance by using private service endpoints.





