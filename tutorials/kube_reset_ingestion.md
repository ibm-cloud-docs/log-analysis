---

copyright:
  years:  2018, 2020
lastupdated: "2020-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, kubernetes, tutorial, reset ingestion key

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


# Resetting the ingestion key used by a Kubernetes cluster to forward logs to an {{site.data.keyword.la_full_notm}} instance
{: #kube_reset}

If the ingestion key that you use to forward logs from a cluster to an {{site.data.keyword.la_full_notm}} instance in the {{site.data.keyword.cloud_notm}} is compromised, you must reset the key and update the Kubernetes cluster configuration to use the new ingestion key. 
{:shortdesc}

## Before you begin
{: #kube_reset_prereqs}

Work in a [supported region](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-regions). **Note:** You can work with a Kubernetes cluster that is located in the same region or in a different region. 

Read about {{site.data.keyword.la_full_notm}}. For more information, see [About](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-getting-started#getting-started_ov).

Use a user ID that is a member or an owner of an {{site.data.keyword.cloud_notm}} account. To get an {{site.data.keyword.cloud_notm}} user ID, go to: [Registration ![External link icon](../../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window}.

The {{site.data.keyword.la_full_notm}} instance is provisioned in the **default** resource group.

To complete the steps in this tutorial, your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources: 

| Resource                             | Scope of the access policy | Roles    | Region    | Information                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Resource group **Default**           |  Resource group            | Viewer  | us-south  | This policy is required to allow the user to see service instances in the Default resource group.    |
| {{site.data.keyword.la_full_notm}} service |  Resource group            | Editor </br>Manager  | us-south  | This policy is required to allow the user to reset the ingestion key.   |
| Kubernetes cluster instance          |  Resource                  | Editor  | us-south  | This policy is required to delete and configure the secret and the LogDNA agent in the Kubernetes cluster. |
{: caption="Table 1. List of IAM policies required to complete the tutorial" caption-side="top"} 

For more information about the {{site.data.keyword.containerlong}} IAM roles, see [User access permissions](/docs/containers?topic=containers-access_reference#access_reference).

Install the {{site.data.keyword.cloud_notm}} CLI and the Kubernetes CLI plug-in. For more information, see [Installing the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli).


## Step 1: Reset the ingestion key
{: #kube_reset_step1}

To renew the ingestion key for an {{site.data.keyword.la_full_notm}} instance by using the {{site.data.keyword.la_full_notm}} Web UI, complete the following steps:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Select the **Configuration** icon. Then select **Organization**. 

3. Select **API keys**.

    You can see the ingestion keys that have been created. 

4. Select **Generate Ingestion Key**.

    A new key is added to the list.

5. Delete the old ingestion key. Click **delete**.


## Step 2: Remove any configuration in the cluster that uses the old ingestion key
{: #kube_reset_step2}

Complete the following steps:

1. Open a terminal. Then, log in to the {{site.data.keyword.cloud_notm}}. Run the following command and follow the prompts:

    ```
    ibmcloud login -a cloud.ibm.com
    ```
    {: codeblock}

    Select the account where you have provisioned the {{site.data.keyword.la_full_notm}} instance.

2. Set up the cluster environment. Run the following commands:

    First, get the command to set the environment variable and download the Kubernetes configuration files.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    When the download of the configuration files is finished, a command is displayed that you can use to set the path to the local Kubernetes configuration file as an environment variable.

    Then, copy and paste the command that is displayed in your terminal to set the KUBECONFIG environment variable.

    **Note:** Every time you log in to the {{site.data.keyword.containerlong}} CLI to work with clusters, you must run these commands to set the path to the cluster's configuration file as a session variable. The Kubernetes CLI uses this variable to find a local configuration file and certificates that are necessary to connect with the cluster in {{site.data.keyword.cloud_notm}}.

3. Remove the secret from your Kubernetes cluster. The Kubernetes secret contains the LogDNA ingestion key. Run the following command:

    ```
    kubectl delete secret logdna-agent-key
    ```
    {: codeblock}

4. Remove the LogDNA agent on every worker(node) of your Kubernetes cluster. The LogDNA agent is responsible for collecting and forwarding your logs. Run the following command:

    ```
    kubectl delete daemonset logdna-agent
    ```
    {: codeblock}

5. Verify that the LogDNA agent is deleted successfully. Run the following command:

    ```
    kubectl get pods
    ```
    {: codeblock}

    You should not see any LogDNA pods.


## Step 3: Configure your Kubernetes cluster with the new ingestion key
{: #kube_reset_step3}

To configure your Kubernetes cluster in the `us-south` region to forward logs to your LogDNA instance, complete the following steps from the command line:

1. Open a terminal. Then, log in to the {{site.data.keyword.cloud_notm}}. Run the following command and follow the prompts:

    ```
    ibmcloud login -a cloud.ibm.com
    ```
    {: codeblock}

    Select the account where you have provisioned the {{site.data.keyword.la_full_notm}} instance.

2. Set up the cluster environment. Run the following commands:

    First, get the command to set the environment variable and download the Kubernetes configuration files.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    When the download of the configuration files is finished, a command is displayed that you can use to set the path to the local Kubernetes configuration file as an environment variable.

    Then, copy and paste the command that is displayed in your terminal to set the KUBECONFIG environment variable.

    **Note:** Every time you log in to the {{site.data.keyword.containerlong}} CLI to work with clusters, you must run these commands to set the path to the cluster's configuration file as a session variable. The Kubernetes CLI uses this variable to find a local configuration file and certificates that are necessary to connect with the cluster in {{site.data.keyword.cloud_notm}}.

3. Add a secret to your Kubernetes cluster. Run the following command:

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE
    ```
    {: codeblock}

    The LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE shows the LogDNA ingestion key for your instance.

    The Kubernetes secret contains the LogDNA ingestion key. The LogDNA ingestion key is used to authenticate the logging agent with the {{site.data.keyword.la_full_notm}} service. It is used to open a secure web socket to the ingestion server on the logging back-end system.

4. Configure the LogDNA agent on every worker(node) of your Kubernetes cluster. Run the following command:

    ```
    kubectl create -f https://assets.us-south.logging.cloud.ibm.com/clients/logdna-agent-ds.yaml
    ```
    {: codeblock}

    The LogDNA agent is responsible for collecting and forwarding your logs.

    The agent collects automatically logs with extension *.log and extensionless files that are located under /var/log. By default, logs are collected from all namespaces, including the kube-system.

5. Verify that the LogDNA agent is created successfully and its status. Run the following command:

    ```
    kubectl get pods
    ```
    {: codeblock}


## Step 4: Launch the LogDNA web UI
{: #kube_reset_step4}

You launch the web UI from the {{site.data.keyword.cloud_notm}} Observability dashboard. 

Complete the following steps to launch the web UI:

1. [Log in to your {{site.data.keyword.cloud_notm}} account ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window}.

2. Click the **Menu** icon ![Menu icon](../../../icons/icon_hamburger.svg) &gt; **Observability** to launch the Observability dashboard. 

3. Select **Logging**. 

    The list of {{site.data.keyword.la_full_notm}} instances that are available on {{site.data.keyword.cloud_notm}} is displayed.

3. Select one instance. Then, click **View logs**.

    The LogDNA web UI opens and displays your cluster logs.


## Step 5: View your logs
{: #kube_reset_step5}

From the LogDNA web UI, you can view your logs as they pass through the system. You view logs by using log tailing. 

With the **Lite - Free** service plan, you can only tail your latest logs.
{: note}


## Next steps
{: #kube_reset_next_steps}

  If you want to [filter cluster logs](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5), [search cluster logs](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6), [define views](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7), and [configure alerts](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-alerts), you must upgrade the {{site.data.keyword.la_full_notm}} plan to a paid plan.



