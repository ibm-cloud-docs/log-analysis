---

copyright:
  years: 2018
lastupdated: "2018-11-15"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}


# Resetting the ingestion key used by a Kubernetes cluster to forward logs to an IBM Log Analysis with LogDNA instance
{: #kube_reset}

If the ingestion key that you use to forward logs from a cluster to an IBM Log Analysis with LogDNA instance in the {{site.data.keyword.Bluemix}} is compromised, you must reset the key and update the Kubernetes cluster configuration to use the new ingestion key. 
{:shortdesc}

## Before you begin
{: #prereqs}

Work in the US-South region. Both resources, the IBM Log Analysis with LogDNA instance and the Kubernetes cluster must run in the same account.

The IBM Log Analysis with LogDNA instance is provisioned in the **Default** resource group.

Read about IBM Log Analysis with LogDNA. For more information, see [About LogDNA](/docs/services/Log-Analysis-with-LogDNA/overview.html#about).

To complete the steps in this tutorial, your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources: 

| Resource                             | Scope of the access policy | Roles    | Region    | Information                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Resource group **Default**           |  Resource group            | Viewer  | us-south  | This policy is required to allow the user to see service instances in the Default resource group.    |
| IBM Log Analysis with LogDNA service |  Resource group            | Editor </br>Manager  | us-south  | This policy is required to allow the user to reset the ingestion key.   |
| Kubernetes cluster instance          |  Resource                  | Editor  | us-south  | This policy is required to delete and configure the secret and the LogDNA agent in the Kubernetes cluster. |
{: caption="Table 1. List of IAM policies required to complete the tutorial" caption-side="top"} 

For more information about the {{site.data.keyword.containerlong}} IAM roles, see [User access permissions](/docs/containers/cs_access_reference.html#understanding).

Install the {{site.data.keyword.Bluemix_notm}} CLI. For more information, see [Installing the {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli/index.html#overview).

Install the Kubernetes CLI plug-in. For more information, see [Installing the CLI](/docs/containers/cs_cli_install.html#cs_cli_install).


## Step 1: Reset the ingestion key
{: #step1}

To renew the ingestion key for an IBM Log Analysis with LogDNA instance by using the IBM Log Analysis with LogDNA Web UI, complete the following steps:

1. Launch the IBM Log Analysis with LogDNA web UI. For more information, see [Launching the IBM Log Analysis with LogDNA Web UI](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#step2).

2. Select the **Configuration** icon. Then select **Organization**. 

3. Select **API keys**.

    You can see the ingestion keys that have been created. 

4. Select **Generate Ingestion Key**.

    A new key is added to the list.

5. Delete the old ingestion key. Click **delete**.


## Step 2: Remove any configuration in the cluster that uses the old ingestion key
{: #step2}

Complete the following steps:

1. Open a terminal. Then, log in to the {{site.data.keyword.Bluemix_notm}}. Run the following command and follow the prompts:

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    Select the account where you have provisioned the IBM Log Analysis with LogDNA instance.

2. Set up the cluster environment. Run the following commands:

    First, get the command to set the environment variable and download the Kubernetes configuration files.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    When the download of the configuration files is finished, a command is displayed that you can use to set the path to the local Kubernetes configuration file as an environment variable.

    Then, copy and paste the command that is displayed in your terminal to set the KUBECONFIG environment variable.

    **Note:** Every time you log in to the {{site.data.keyword.containerlong}} CLI to work with clusters, you must run these commands to set the path to the cluster's configuration file as a session variable. The Kubernetes CLI uses this variable to find a local configuration file and certificates that are necessary to connect with the cluster in {{site.data.keyword.Bluemix_notm}}.

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
{: #step3}

To configure your Kubernetes cluster to forward logs to your LogDNA instance, complete the following steps from the command line:

1. Open a terminal. Then, log in to the {{site.data.keyword.Bluemix_notm}}. Run the following command and follow the prompts:

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    Select the account where you have provisioned the IBM Log Analysis with LogDNA instance.

2. Set up the cluster environment. Run the following commands:

    First, get the command to set the environment variable and download the Kubernetes configuration files.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    When the download of the configuration files is finished, a command is displayed that you can use to set the path to the local Kubernetes configuration file as an environment variable.

    Then, copy and paste the command that is displayed in your terminal to set the KUBECONFIG environment variable.

    **Note:** Every time you log in to the {{site.data.keyword.containerlong}} CLI to work with clusters, you must run these commands to set the path to the cluster's configuration file as a session variable. The Kubernetes CLI uses this variable to find a local configuration file and certificates that are necessary to connect with the cluster in {{site.data.keyword.Bluemix_notm}}.

3. Add a secret to your Kubernetes cluster. Run the following command:

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE
    ```
    {: codeblock}

    The LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE shows the LogDNA ingestion key for your instance.

    The Kubernetes secret contains the LogDNA ingestion key. The LogDNA ingestion key is used to authenticate the logging agent with the IBM Log Analysis with LogDNA service. It is used to open a secure web socket to the ingestion server on the logging back-end system.

4. Configure the LogDNA agent on every worker(node) of your Kubernetes cluster. Run the following command:

    ```
    kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
    ```
    {: codeblock}

    The LogDNA agent is responsible for collecting and forwarding your logs.

    The agent collects automatically logs with extension *.log and extensionless files that are located under /var/log. By default, logs are collected from all namespaces, including the kube-system.

5. Verify that the LogDNA agent is created successfully and its status. Run the following command:

    ```
    kubectl get pods
    ```
    {: codeblock}


## Step 4: Launch the LogDNA Web UI
{: #step4}

To launch IBM the Log Analysis with LogDNA dashboard through the {{site.data.keyword.Bluemix_notm}} UI, complete the following steps:

1. Log in to your {{site.data.keyword.Bluemix_notm}} account.

    The {{site.data.keyword.Bluemix_notm}} dashboard can be found at: [http://bluemix.net ![External link icon](../../../icons/launch-glyph.svg "External link icon")](http://bluemix.net){:new_window}.

	After you log in with your user ID and password, the {{site.data.keyword.Bluemix_notm}} Dashboard opens.

2. In the navigation menu, select **Observability**. 

3. Select **Logging**. 

    The list of IBM Log Analysis with LogDNA instances that are available on {{site.data.keyword.Bluemix_notm}} is displayed.

3. Select one instance. Then, click **View logs**.

    The LogDNA Web UI opens and displays your cluster logs.


## Step 5: View your logs
{: step5}

From the LogDNA Web UI, you can view your logs as they pass through the system. You view logs by using log tailing. 

**Note:** With the **Free** service plan, you can only tail your latest logs.



## Next steps
{: #next_steps}

  If you want to [filter cluster logs](https://docs.logdna.com/docs/filters), [search cluster logs](https://docs.logdna.com/docs/search), [define views](https://docs.logdna.com/docs/views), and [configure alerts](https://docs.logdna.com/docs/alerts), you must upgrade the IBM Log Analysis with LogDNA plan to a paid plan.



