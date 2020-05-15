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

# Connecting a LogDNA agent to a standard Kubernetes cluster
{: #config_agent_kube_cluster}

The LogDNA agent is responsible for collecting and forwarding logs to your {{site.data.keyword.la_full_notm}} instance. After you provision an instance of {{site.data.keyword.la_full}}, you must configure a LogDNA agent for each log source that you want to monitor.
{:shortdesc}

To configure your Kubernetes cluster to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install a *logdna-agent* pod on each node of your cluster. The LogDNA agent reads log files from the pod where it is installed, and forwards the log data to your LogDNA instance.

Complete the following steps from the command line to configure your Kubernetes cluster to forward logs to your LogDNA instance:


## Prereq
{: #config_agent_kube_cluster_prereq}

To deploy the LogDNA agent in a cluster, you must have a user ID that has the following IAM roles:
* **Viewer** platform role, and **Writer** or **Manager** service role to work with that cluster instance.
* **Viewer** permissions on the resource group where the cluster is available.

To configure the LogDNA agen in the cluster, you need the following CLIs:
* The {{site.data.keyword.cloud_notm}} CLI to log in to the {{site.data.keyword.cloud_notm}} by using `ibmcloud` commands, and to manage the cluster by using `ibmcloud ks` commands. [Learn more](/docs/containers?topic=containers-cs_cli_install#cs_cli_install_steps).
* The Kubernetes CLI to manage the cluster by using `kubectl` commands. [Learn more](/docs/containers?topic=containers-cs_cli_install#kubectl).

## Step 1. Set the cluster context
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



## Step 2. Store your logDNA ingestion key as a Kubernetes secret
{: #config_agent_kube_cluster_step2}

Create a Kubernetes secret to store your logDNA ingestion key for your service instance. 

The LogDNA ingestion key is used to open a secure web socket to the logDNA ingestion server and to authenticate the logging agent with the {{site.data.keyword.la_full_notm}} service.

Run the following command:

```
kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<logDNA_ingestion_key> -n ibm-observe
```
{: pre}

To get the ingestion key, see [Get the ingestion key through the IBM Log Analysis with LogDNA web UI](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-ingestion_key).

## Step 3. Enable virtual routing and forwarding (VRF)
{: #config_agent_kube_cluster_step3}

This step is required if you plan to use private endpoints.  

You must enable virtual routing and forwarding (VRF) and connectivity to service endpoints for your account. [Learn more](/docs/account?topic=account-vrf-service-endpoint)

## Step 4. Deploy the LogDNA agent in the cluster
{: #config_agent_kube_cluster_step4}

Create a Kubernetes daemonset to deploy the LogDNA agent on every worker node of your Kubernetes cluster. 

The LogDNA agent collects STDOUT, STDERR, logs with the extension `*.log`, and extensionsless files that are stored in the `/var/log` directory of your pod. By default, logs are collected from all namespaces, including `kube-system`, and automatically forwarded to the {{site.data.keyword.la_full_notm}} service.

Choose any of the following options to deploy the LogDNA agent:
* Option 1: Get up and running by using the LogDNA agent V1. For example, you can use this option for proofs of concept, and development environments.
* Option 2: Deploy and configure the LogDNA agent V1 for production, regulated, and highly available workloads.

### Option 1. Get up and running by using the LogDNA agent V1
{: #config_agent_kube_cluster_step4_opt1_V1}

Choose one of the following commands to install and configure the LogDNA agent version 1:

| Location                  | Command (By using public endpoints)               | 
|--------------------------|----------------------------------------------------|
| `Chennai (in-che)`       | `kubectl create -f https://assets.in-che.logging.cloud.ibm.com/clients/logdna-agent-ds.yaml -n ibm-observe`       |
| `Dallas (us-south)`      | `kubectl create -f https://assets.us-south.logging.cloud.ibm.com/clients/logdna-agent-ds.yaml -n ibm-observe`       |
| `Frankfurt (eu-de)`      | `kubectl create -f https://assets.eu-de.logging.cloud.ibm.com/clients/logdna-agent-ds.yaml -n ibm-observe`         |
| `London (eu-gb)`         | `kubectl create -f https://assets.eu-gb.logging.cloud.ibm.com/clients/logdna-agent-ds.yaml -n ibm-observe`          |
| `Tokyo (jp-tok)`         | `kubectl create -f https://assets.jp-tok.logging.cloud.ibm.com/clients/logdna-agent-ds.yaml -n ibm-observe`       |
| `Seoul (kr-seo)`         | `kubectl create -f https://assets.kr-seo.logging.cloud.ibm.com/clients/logdna-agent-ds.yaml -n ibm-observe` |
| `Sydney (au-syd)`        | `kubectl create -f https://assets.au-syd.logging.cloud.ibm.com/clients/logdna-agent-ds.yaml -n ibm-observe`        |
| `Washington (us-east)`   | `kubectl create -f https://assets.us-east.logging.cloud.ibm.com/clients/logdna-agent-ds.yaml -n ibm-observe`       |
{: caption="Table 1. Commands by location when you use public endpoints" caption-side="top"}
{: #end-api-table-1}
{: tab-title="Command (By using public endpoints)"}
{: tab-group="agent"}
{: class="simple-tab-table"}
{: row-headers}

| Location                  | Command (By using private endpoints)               | 
|--------------------------|----------------------------------------------------|
| `Chennai (in-che)`       | `kubectl create -f https://assets.in-che.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe`       |
| `Dallas (us-south)`      | `kubectl create -f https://assets.us-south.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe`      |
| `Frankfurt (eu-de)`      | `kubectl create -f https://assets.eu-de.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe`          |
| `London (eu-gb)`         | `kubectl create -f https://assets.eu-gb.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe`       |
| `Tokyo (jp-tok)`         | `kubectl create -f https://assets.jp-tok.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe`        |
| `Seoul (kr-seo)`         | `kubectl create -f https://assets.kr-seo.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe` |
| `Sydney (au-syd)`        | `kubectl create -f https://assets.au-syd.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe`       |
| `Washington (us-east)`   | `kubectl create -f https://assets.us-east.logging.cloud.ibm.com/clients/logdna-agent-ds-private.yaml -n ibm-observe`      |
{: caption="Table 2. Commands by location when you use private endpoints" caption-side="top"}
{: #end-api-table-2}
{: tab-title="Command (By using private endpoints)"}
{: tab-group="agent"}
{: class="simple-tab-table"}
{: row-headers}

### Option 2. LogDNA agent V1: Regulated and highly available workloads
{: #config_agent_kube_cluster_step4_opt2_V1}











## Step 5. Verify that the LogDNA agent is deployed successfully
{: #config_agent_kube_cluster_step5}

To verify that the LogDNA agent is deployed successfully, run the following command:

```
kubectl get pods
```
{: pre}


The deployment is successful when you see one or more LogDNA pods.
* **The number of LogDNA pods equals the number of worker nodes in your cluster.**
* All pods must be in a `Running` state.
* *Stdout* and *stderr* are automatically collected and forwarded from all containers. Log data includes application logs and worker logs.
* By default, the LogDNA agent pod that runs on a worker collects logs from all namespaces on that node, including kube-system logs.



