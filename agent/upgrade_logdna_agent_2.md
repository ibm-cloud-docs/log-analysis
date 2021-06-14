---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, update logging agent

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


# Upgrading from logging agent version 1 to logging agent version 2
{: #upgrade_log_analysis_agent_2}

If your Kubernetes cluster version is 1.9+, you can upgrade the logging agent to version 2.
{:shortdesc}

When you upgrade the version of the agent, some logs may not be collected or duplicated depending on the period of time that you take to delete the current logging agent and deploy a new version of the logging agent in the cluster.
{: important}

Complete the following steps from the command line to upgrade the logging agent version that is deployed in your Kubernetes cluster:


## Step 1. Set the cluster context
{: #upgrade_log_analysis_agent_2_step1}


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


## Step 2. Backup the YAML file of the logging agent that is deployed in the cluster
{: #upgrade_log_analysis_agent_2_step2}

Run the following command to backup the YAML file of the logging agent that is currently deployed in your cluster:

```
kubectl get ds logdna-agent -o yaml > logdna-agent-<clusterName>-<date>.yaml
```
{: pre}

Where

* `clusterName` is the name of your cluster
* `date` is the current date


## Step 3. Create the namespace ibm-observe
{: #upgrade_log_analysis_agent_2_step3}

This step is only required if you installed the logging agent version 1 in a namespace that is different to `ibm-observe`.
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


## Step 4. Delete the logging agent version 1
{: #upgrade_log_analysis_agent_2_step4}

Run the following command to delete the logging agent version 1:

```
kubectl delete daemonset logdna-agent -n NAMESPACE
```
{: pre}

Where `NAMESPACE` is the namespace in your cluster where the logging agent version 1 is deployed.



## Step 5. Deploy the logging agent version 2 in the cluster
{: #upgrade_log_analysis_agent_2_step5}

Choose one of the following commands to install and configure the logging agent:

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

## Step 6. Verify that the logging agent is deployed successfully
{: #upgrade_log_analysis_agent_2_step6}

To verify that the logging agent is deployed successfully, run the following command:

```
kubectl get pods
```
{: pre}


The deployment is successful when you see one or more logging pods.
* **The number of logging pods equals the number of worker nodes in your cluster.**
* All pods must be in a `Running` state.


