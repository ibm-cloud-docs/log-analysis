---

copyright:
  years:  2018, 2019
lastupdated: "2019-10-15"

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

# Configuring a LogDNA agent for an OpenShight Kubernetes cluster
{: #config_agent_os_cluster}

The LogDNA agent is responsible for collecting and forwarding logs to your {{site.data.keyword.la_full_notm}} instance. After you provision an instance of {{site.data.keyword.la_full}}, you must configure a LogDNA agent for each log source that you want to monitor.
{:shortdesc}

To configure your Kubernetes cluster to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install a *LogDNA-agent* pod on each node of your cluster. The LogDNA agent reads log files from the pod where it is installed, and forwards the log data to your LogDNA instance.

To forward logs to your LogDNA instance, complete the following steps from the command line:

## Prereq
{: #config_agent_oscluster_prereq}

To deploy the LogDNA agent in a cluster, you must have a user ID that has the following IAM roles:
* **Viewer** platform role, and **Manager** service role to work with that cluster instance.
* **Viewer** permissions on the resource group where the cluster is available.

To configure the LogDNA agen in the cluster, you need the following CLIs:
* The {{site.data.keyword.cloud_notm}} CLI to log in to the {{site.data.keyword.cloud_notm}} by using `ibmcloud` commands, and to manage the cluster by using `ibmcloud ks` commands. [Learn more](/docs/containers?topic=containers-cs_cli_install#cs_cli_install_steps).
* The Kubernetes CLI to manage the cluster by using `kubectl` commands. [Learn more](/docs/containers?topic=containers-cs_cli_install#kubectl).
* The Openshift CLI to login to the cluster from the command line and deploy the agent. [Learn more](/docs/openshift?topic=openshift-openshift-cli).



## Step 1. Set the cluster context and log in to the cluster
{: #config_agent_oscluster_step1}

Complete the following steps:

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

3. Log in to the cluster. Run the following command and enter your IBMid userid and password.

    ```
    oc login
    ```
    {: pre}

## Step 2. Store your LogDNA ingestion key as a Kubernetes secret
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

    PROJECT is the namespace where the LogDNA pods run. Set this value to **ibm-observe**.

    SERVICEACCOUNT_NAME is the name of the service account that you use to deploy the LogDNA agent. Set this value to **logdna-agent**. Notice that if you leave the service account name blank, the default service account is used instaead of the service account that you created. 

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

    PROJECT is the namespace where the LogDNA pods run. Set this value to **ibm-observe**.

    SERVICEACCOUNT_NAME is the name of the service account that you use to deploy the LogDNA agent. Set this value to **logdna-agent**.

    ```
    oc adm policy add-scc-to-user privileged system:serviceaccount:ibm-observe:logdna-agent
    ```
    {: pre}

5. Add a secret. The secret sets the ingestion key that the LogDNA agent uses to send logs.

    ```
    oc create secret generic logdna-agent-key --from-literal=logdna-agent-key=INGESTION_KEY
    ```
    {: pre}

    Where **INGESTION_KEY** is the ingestion key for the LogDNA instance where you plan to forward and collect the cluster logs. To get the ingestion key, see [Get the ingestion key through the IBM Log Analysis with LogDNA web UI](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-ingestion_key).


## Step 3. Enable virtual routing and forwarding (VRF)
{: #config_agent_os_cluster_step3}

This step is required if you plan to use private endpoints.  

You must enable virtual routing and forwarding (VRF) and connectivity to service endpoints for your account. [Learn more](/docs/account?topic=account-vrf-service-endpoint)

## Step 4. Deploy the LogDNA agent in the cluster
{: #config_agent_os_cluster_step4}

Create a Kubernetes daemon set to deploy the LogDNA agent on every worker node of your Kubernetes cluster. 

The LogDNA agent collects logs with the extension `*.log` and extensionsless files that are stored in the `/var/log` directory of your pod. By default, logs are collected from all namespaces, including `kube-system`, and automatically forwarded to the {{site.data.keyword.la_full_notm}} service.

Choose one of the following commands:

| Location                  | Command (By using public endpoints)               | 
|--------------------------|----------------------------------------------------|
| `Dallas (us-south)`      | `oc create -f https://assets.us-south.logging.cloud.ibm.com/clients/LogDNA-agent-ds-os.yaml`       |
| `Frankfurt (eu-de)`      | `oc create -f https://assets.eu-de.logging.cloud.ibm.com/clients/LogDNA-agent-ds-os.yaml`         |
| `London (eu-gb)`         | `oc create -f https://assets.eu-gb.logging.cloud.ibm.com/clients/LogDNA-agent-ds-os.yaml`          |
| `Tokyo (jp-tok)`         | `oc create -f https://assets.jp-tok.logging.cloud.ibm.com/clients/LogDNA-agent-ds-os.yaml`       |
| `Seoul (kr-seo)`         | `oc create -f https://assets.kr-seo.logging.cloud.ibm.com/clients/LogDNA-agent-ds-os.yaml` |
| `Sydney (au-syd)`        | `oc create -f https://assets.au-syd.logging.cloud.ibm.com/clients/LogDNA-agent-ds-os.yaml`        |
{: caption="Table 1. Commands by location when you use public endpoints" caption-side="top"}
{: #end-api-table-1}
{: tab-title="Command (By using public endpoints)"}
{: tab-group="agent"}
{: class="simple-tab-table"}
{: row-headers}

| Location                  | Command (By using private endpoints)               | 
|--------------------------|----------------------------------------------------|
| `Dallas (us-south)`      | `oc create -f https://assets.us-south.logging.cloud.ibm.com/clients/LogDNA-agent-ds-os-private.yaml`      |
| `Frankfurt (eu-de)`      | `oc create -f https://assets.eu-de.logging.cloud.ibm.com/clients/LogDNA-agent-ds-os-private.yaml`          |
| `London (eu-gb)`         | `oc create -f https://assets.eu-gb.logging.cloud.ibm.com/clients/LogDNA-agent-ds-os-private.yaml`       |
| `Tokyo (jp-tok)`         | `oc create -f https://assets.jp-tok.logging.cloud.ibm.com/clients/LogDNA-agent-ds-os-private.yaml`        |
| `Seoul (kr-seo)`         | `oc create -f https://assets.kr-seo.logging.cloud.ibm.com/clients/LogDNA-agent-ds-os-private.yaml` |
| `Sydney (au-syd)`        | `oc create -f https://assets.au-syd.logging.cloud.ibm.com/clients/LogDNA-agent-ds-os-private.yaml`       |
{: caption="Table 1. Commands by location when you use private endpoints" caption-side="top"}
{: #end-api-table-1}
{: tab-title="Command (By using private endpoints)"}
{: tab-group="agent"}
{: class="simple-tab-table"}
{: row-headers}

## Step 5. Verify that the LogDNA agent is deployed successfully
{: #config_agent_os_cluster_step5}

To verify that the LogDNA agent is deployed successfully, run the following command:

1. Target the project where the LogDNA agent is deployed.

    ```
    oc project ibm-observe
    ```
    {: pre}

2. Verify the pods are running.

    ```
    oc get pods
    ```
    {: pre}


The deployment is successful when you see one or more LogDNA pods.
* **The number of LogDNA pods equals the number of worker nodes in your cluster.**
* All pods must be in a `Running` state.
* *Stdout* and *stderr* are automatically collected and forwarded from all containers. Log data includes application logs and worker logs.
* By default, the LogDNA agent pod that runs on a worker collects logs from all namespaces on that node, including kube-system logs.



