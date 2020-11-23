---

copyright:
  years:  2018, 2020
lastupdated: "2020-05-11"

keywords: LogDNA, IBM, Log Analysis, logging, update LogDNA agent

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

# Upgrading from LogDNA agent version 1 to LogDNA agent version 2
{: #upgrade_logdna_agent_2}

If your Kubernetes cluster version is 1.9+, you can upgrade the LogDNA agent to version 2.
{:shortdesc}

Complete the following steps from the command line to upgrade the LogDNA agent version that is deployed in your Kubernetes cluster:


## Step 1. Set the cluster context
{: #upgrade_agent_kube_cluster_step1}


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


## Step 2. Backup the yaml file of the LogDNA agent that is deployed in the cluster
{: #upgrade_agent_kube_cluster_step2}

Run the following command to backup the yaml file of the LogDNA agent that is currently deployed in your cluster:

```
kubectl get ds logdna-agent -o yaml > logdna-agent-<clusterName>-<date>.yaml
```
{: pre}

Where

* `clusterName` is the name of your cluster
* `date` is the current date


## Step 3. Create the namespace ibm-observe
{: #upgrade_agent_kube_cluster_step3}

This step is only required if you installed the LogDNA agent version 1 in a namespace that is different to `ibm-observe`.
{: note}

To check if the namespace exists, run the following command:

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


## Step 4. Delete the existing agent
{: #upgrade_agent_kube_cluster_step4}

Run the following command to delete the LogDNA agent version 1:

```
kubectl delete daemonset logdna-agent -n NAMESPACE
```
{: pre}

Where `NAMESPACE` is the namespace in your cluster where the LogDNA agent version 1 is deployed.



## Step 4. Deploy the LogDNA agent version 2 in the cluster
{: #upgrade_agent_kube_cluster_step4}

Choose one of the following commands to install and configure the LogDNA agent:

| Location                  | Command (By using public endpoints)               | 
|--------------------------|----------------------------------------------------|
| `Chennai (in-che)`       | `kubectl apply -f https://assets.in-che.logging.cloud.ibm.com/clients/agent-resources.yaml`       |
| `Dallas (us-south)`      | `kubectl apply -f https://assets.us-south.logging.cloud.ibm.com/clients/agent-resources.yaml`       |
| `Frankfurt (eu-de)`      | `kubectl apply -f https://assets.eu-de.logging.cloud.ibm.com/clients/agent-resources.yaml`         |
| `London (eu-gb)`         | `kubectl apply -f https://assets.eu-gb.logging.cloud.ibm.com/clients/agent-resources.yaml`          |
| `Tokyo (jp-tok)`         | `kubectl apply -f https://assets.jp-tok.logging.cloud.ibm.com/clients/agent-resources.yaml`       |
| `Seoul (kr-seo)`         | `kubectl apply -f https://assets.kr-seo.logging.cloud.ibm.com/clients/agent-resources.yaml` |
| `Sydney (au-syd)`        | `kubectl apply -f https://assets.au-syd.logging.cloud.ibm.com/clients/agent-resources.yaml`        |
| `Washington (us-east)`   | `kubectl apply -f https://assets.us-east.logging.cloud.ibm.com/clients/agent-resources.yaml`       |
{: caption="Table 3. Commands by location when you use public endpoints" caption-side="top"}
{: #agent-table-3}
{: tab-title="Command (By using public endpoints)"}
{: tab-group="agent1"}
{: class="simple-tab-table"}
{: row-headers}

| Location                  | Command (By using private endpoints)               | 
|--------------------------|----------------------------------------------------|
| `Chennai (in-che)`       | `kubectl apply -f https://assets.in-che.logging.cloud.ibm.com/clients/agent-resources-private.yaml`   |
| `Dallas (us-south)`      | `kubectl apply -f https://assets.us-south.logging.cloud.ibm.com/clients/agent-resources-private.yaml` |
| `Frankfurt (eu-de)`      | `kubectl apply -f https://assets.eu-de.logging.cloud.ibm.com/clients/agent-resources-private.yaml`    |
| `London (eu-gb)`         | `kubectl apply -f https://assets.eu-gb.logging.cloud.ibm.com/clients/agent-resources-private.yaml`    |
| `Tokyo (jp-tok)`         | `kubectl apply -f https://assets.jp-tok.logging.cloud.ibm.com/clients/agent-resources-private.yaml`   |
| `Seoul (kr-seo)`         | `kubectl apply -f https://assets.kr-seo.logging.cloud.ibm.com/clients/agent-resources-private.yaml`   |
| `Sydney (au-syd)`        | `kubectl apply -f https://assets.au-syd.logging.cloud.ibm.com/clients/agent-resources-private.yaml`   |
| `Washington (us-east)`   | `kubectl apply -f https://assets.us-east.logging.cloud.ibm.com/clients/agent-resources-private.yaml`  |
{: caption="Table 4. Commands by location when you use private endpoints" caption-side="top"}
{: #agent-table-4}
{: tab-title="Command (By using private endpoints)"}
{: tab-group="agent1"}
{: class="simple-tab-table"}
{: row-headers}

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



