---

copyright:
  years:  2018, 2020
lastupdated: "2020-07-01"

keywords: LogDNA, IBM, Log Analysis, logging, detach config agent

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

# Disconnecting a LogDNA agent
{: #detach_agent}

Detach a LogDNA agent from a logging instance to stop collecting logs.
{:shortdesc}

## Detaching a LogDNA agent from a standard Kubernetes cluster
{: #detach_agent_kube}

To stop your Kubernetes cluster from sending logs to your {{site.data.keyword.la_full_notm}} instance, you must remove the LogDNA agent from your cluster. 

### Detaching a LogDNA agent from a standard Kubernetes cluster by using kubectl commands
{: #detach_agent_kube_kubectl}


To stop your Kubernetes cluster from forwarding logs to your LogDNA instance, complete the following steps from the command line:

1. Open a terminal. Then, [log in to the {{site.data.keyword.cloud_notm}}](https://cloud.ibm.com/login){: external}, and follow the prompts.

    Select the account where you provisioned the {{site.data.keyword.la_full_notm}} instance.

2. Set up the cluster environment. Run the following commands:

    First, get the command to set the environment variable and download the Kubernetes configuration files.

    ```
    ibmcloud ks cluster config --cluster <cluster_name_or_ID>
    ```
    {: codeblock}

3. Remove the secret from your Kubernetes cluster. The Kubernetes secret contains the LogDNA ingestion key. Run the following command:

    ```
    kubectl delete secret logdna-agent-key -n ibm-observe
    ```
    {: codeblock}

4. Remove the LogDNA agent on every worker(node) of your Kubernetes cluster. The LogDNA agent is responsible for collecting and forwarding your logs. Run the following command:

    ```
    kubectl delete daemonset logdna-agent -n ibm-observe
    ```
    {: codeblock}

5. Verify that the LogDNA agent is deleted successfully. Run the following command:

    ```
    kubectl get pods -n ibm-observe
    ```
    {: codeblock}

    You should not see any LogDNA pods.



### Detaching a LogDNA agent from a standard Kubernetes cluster from the cluster console
{: #detach_agent_os_console}

Complete the following steps from the [{{site.data.keyword.containerlong_notm}} console](https://cloud.ibm.com/kubernetes/clusters){: external}:

1. Select the cluster for which you want to create a LogDNA logging configuration.

2. On the cluster **Overview** page, in the *Logging* section, click **Disconnect**.





### Detaching a LogDNA agent from a standard Kubernetes cluster by using ob commands
{: #detach_agent_os_console_ob}

Complete the following steps:


1. Set the cluster context.

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

2. Detach the LogDNA agent by using the `ob` CLI. Run the following command:

    ```
    ibmcloud ob logging config delete --cluster <cluster_name_or_ID> --instance <LogDNA_instance_name_or_ID>  [--force]
    ```
    {: pre}

    Where

    * `<cluster_name_or_ID>` is the name or the ID of the cluster.

    * `<LogDNA_instance_name_or_ID>` is the name or the ID of the LogDNA instance where you want to forward the cluster logs for analysis.

    * ` [--force]`  is used to force the command to run with no user prompts.






## Detaching a LogDNA agent from an Openshift Kubernetes cluster
{: #detach_agent_os}

To stop your OpenShift cluster from sending logs to your {{site.data.keyword.la_full_notm}} instance, you must remove the LogDNA agent from your cluster. 

### Detaching a LogDNA agent from an Openshift Kubernetes cluster by using kubectl commands
{: #detach_agent_os_kube_kubectl}

Complete the following steps from the command line:

1. Open a terminal to log in to {{site.data.keyword.cloud_notm}}.

   ```
   ibmcloud login -a cloud.ibm.com
   ```
   {: pre}

   Select the account where you provisioned the {{site.data.keyword.la_full_notm}} instance.

2. Set the cluster where you want to configure logging as the context for this session.

   ```
   ibmcloud cs cluster config --cluster <cluster_name_or_ID>
   ```
   {: pre}

3. Log in to the cluster. Choose a method to login to an OpenShift cluster. [Learn more about the methods to login](/docs/openshift?topic=openshift-access_cluster#access_automation).

4. Delete the LogDNA agent serviceaccount.

    ```
    oc delete serviceaccount logdna-agent -n ibm-observe
    ```
    {: pre}

4. Remove the LogDNA secrets from your cluster. Each secret contains the LogDNA ingestion key. Run the following commands:

    List secrets.

    ```
    oc get secrets -n PROJECT
    ```
    {: pre}

    Then, run the following command for each secret: 
    
    ```
    oc delete secret logdna-agent-key -n PROJECT
    ```
    {: pre}

    Where *PROJECT* is the namespace where the LogDNA pods run. Set this value to **ibm-observe**.

5. Remove the LogDNA agent on every worker(node) of your Kubernetes cluster. The LogDNA agent is responsible for collecting and forwarding your logs. Run the following command:

    ```
    oc delete daemonset logdna-agent -n PROJECT
    ```
    {: codeblock}

    Where *PROJECT* is the namespace where the LogDNA pods run. Set this value to **ibm-observe**.

5. Verify that the LogDNA agent is deleted successfully. Run the following command to verify that LogDNA agent pods are not running:

    ```
    oc get pods -n PROJECT
    ```
    {: codeblock}




### Detaching a LogDNA agent from an Openshift Kubernetes cluster from the OpenShift console
{: #detach_agent_os_console}

Complete the following steps from the [OpenShift console](https://cloud.ibm.com/kubernetes/clusters?platformType=openshift){: external}:

1. Select the cluster for which you want to create a LogDNA logging configuration.

2. On the cluster **Overview** page, in the *Logging* section, click **Disconnect**.





### Detaching a LogDNA agent from an Openshift Kubernetes cluster by using ob commands
{: #detach_agent_os_console_ob}

Complete the following steps:


1. Set the cluster context.

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

2. Detach the LogDNA agent by using the `ob` CLI. Run the following command:

    ```
    ibmcloud ob logging config delete --cluster <cluster_name_or_ID> --instance <LogDNA_instance_name_or_ID>  [--force]
    ```
    {: pre}

    Where

    * `<cluster_name_or_ID>` is the name or the ID of the cluster.

    * `<LogDNA_instance_name_or_ID>` is the name or the ID of the LogDNA instance where you want to forward the cluster logs for analysis.

    * ` [--force]`  is used to force the command to run with no user prompts.





