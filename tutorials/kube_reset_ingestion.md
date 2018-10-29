---

copyright:
  years: 2018
lastupdated: "2018-10-29"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}


# Reseting the ingestion key used by a Kubernetes cluster to forward logs into an IBM Log Analysis with LogDNA instance
{: #kube_reset}

Use the IBM Log Analysis with LogDNA service to configure cluster-level logging on the {{site.data.keyword.Bluemix}} for Kubernetes clusters. 
{:shortdesc}


Reseting the ingestion key used by a cluster to forward logs to an IBM Log Analysis with LogDNA instance.



From the moment you provision a Kubernetes cluster in the Cloud, you want to know what is happening inside the cluster. You need to access logs to troubleshoot problems and pre-empt issues. At any time, you want to have access to different types of logs such as worker logs, pod logs, application logs, or network logs. In addition, you want to monitor different sources of log data in your Kubernetes cluster. Therefore, your ability to manage and access log records from any of these sources is critical. Your success managing and monitoring logs depends on how you configure the logging capabilities for your Kubernetes platform.

To configure cluster-level logging for a Kubernetes cluster, consider the following information:

* You must be able to store log data, system logs, and containerized application logs on separate storage from Kubernetes system components.
* You must configure every node (worker) in a cluster with a logging agent. Specifically, this agent collects and forwards logs to an external logging back-end.
* You must be able to centralize log data for analysis on an external logging back-end.


On the {{site.data.keyword.Bluemix_notm}}, to configure cluster-level logging for a Kubernetes cluster, you must complete the following steps:

1. Provision an instance of the IBM Log Analysis with LogDNA service. With this step, you configure a centralized log management system where log data is hosted on {{site.data.keyword.Bluemix_notm}}.
2. Provision a cluster on the {{site.data.keyword.containerlong_notm}}. Kubernetes v1.9+ clusters are supported.
3. Configure the LogDNA agent on every worker (node) in a cluster.

![LogDNA component overview on the {{site.data.keyword.Bluemix_notm}}](../images/kube.png "LogDNA component overview on the {{site.data.keyword.Bluemix_notm}}")

In this tutorial, you will learn how to configure cluster-level logging.

## Before you begin
{: #prereqs}

Work in the US-South region. Both resources, the IBM Log Analysis with LogDNA instance and the Kubernetes cluster must run in the same account.

Read about IBM Log Analysis with LogDNA. For more information, see [About LogDNA](/docs/services/Log-Analysis-with-LogDNA/overview.html#about).

Use a user ID that is a member or an owner of an {{site.data.keyword.Bluemix_notm}} account. To get an {{site.data.keyword.Bluemix_notm}} user ID, go to: [Registration ![External link icon](../../../icons/launch-glyph.svg "External link icon")](https://console.bluemix.net/registration/){:new_window}.

Your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources: 

| Resource                             | Scope of the access policy | Role    | Region    | Information                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Resource group **Default**           |  Resource group            | Viewer  | us-south  | This policy is required to allow the user to see service instances in the Default resource group.    |
| IBM Log Analysis with LogDNA service |  Resource group            | Editor  | us-south  | This policy is required to allow the user to provision and administer the IBM Log Analysis with LogDNA service in the Default resource group.   |
| Cluster instance                     |  Account                   | Editor  | us-south  | This policy is required to configure the LogDNA agent in the Kubernetes cluster. |
{: caption="Table 1. List of IAM policies required to complete the tutorial" caption-side="top"} 

For more information about the {{site.data.keyword.containerlong}} IAM roles, see [User access permissions](/docs/containers/cs_access_reference.html#understanding).

Install the {{site.data.keyword.Bluemix_notm}} CLI. For more information, see [Installing the {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli/index.html#overview).

Install the Kubernetes CLI plugin. For more information, see [Installing the CLI](/docs/containers/cs_cli_install.html#cs_cli_install).


## Step1: Provision an IBM Log Analysis with LogDNA instance
{: #step1}

To provision an instance of IBM Log Analysis with LogDNA through the {{site.data.keyword.Bluemix_notm}} UI, complete the following steps:

1. Log in to your {{site.data.keyword.Bluemix_notm}} account.

    The {{site.data.keyword.Bluemix_notm}} dashboard can be found at: [http://bluemix.net ![External link icon](../../icons/launch-glyph.svg "External link icon")](http://bluemix.net){:new_window}.

	After you log in with your user ID and password, the {{site.data.keyword.Bluemix_notm}} UI opens.

2. Click **Catalog**. The list of the services that are available in {{site.data.keyword.Bluemix_notm}} opens.

3. To filter the list of services that is displayed, select the **Developer Tools** category.

4. Click the **IBM Log Analysis with LogDNA** tile.

5. Enter a name for the service instance.

6. Select the **Default** resource group. 

    By default, the **Default** resource group is set.

7. Select **I understand that my data will be sent to LogDNA**. 

    **Note:** You must accept LogDNA's terms and conditions before you can provision the service in the {{site.data.keyword.Bluemix_notm}}.

8. Select the **Lite** service plan. 

    By default, the **Lite** plan is set.

    For more information about other service plans, see [Pricing plans](/docs/services/Log-Analysis-with-LogDNA/overview.html#pricing_plans).

9. To provision the IBM Log Analysis with LogDNA service in the {{site.data.keyword.Bluemix_notm}} resource group where you are logged in, click **Create**.

After you provision an instance, the IBM Log Analysis with LogDNA dashboard opens. 


**Note:** To provision an instance of LogDNA through the CLI, see [Provisioning LogDNA through the {{site.data.keyword.Bluemix_notm}} CLI](/docs/services/Log-Analysis-with-LogDNA/provision.html#logdna_provision_cli).


## Step2: Configure your Kubernetes cluster to send logs to your instance
{: #step2}

To configure your Kubernetes cluster to send logs to your IBM Log Analysis with LogDNA instance, you must install a `logdna-agent` pod on each node of your cluster. The LogDNA agent reads log files from the pod where it is installed, and forwards the log data to your LogDNA instance.

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


## Step 3: Launch the LogDNA Web UI
{: #step3}

To launch IBM the Log Analysis with LogDNA dashboard through the {{site.data.keyword.Bluemix_notm}} UI, complete the following steps:

1. Log in to your {{site.data.keyword.Bluemix_notm}} account.

    The {{site.data.keyword.Bluemix_notm}} dashboard can be found at: [http://bluemix.net ![External link icon](../../../icons/launch-glyph.svg "External link icon")](http://bluemix.net){:new_window}.

	After you log in with your user ID and password, the {{site.data.keyword.Bluemix_notm}} Dashboard opens.

2. In the navigation menu, select **Observability**. 

3. Select **Logging**. 

    The list of IBM Log Analysis with LogDNA instances that are available on {{site.data.keyword.Bluemix_notm}} is displayed.

3. Select one instance. Then, click **View logs**.

    The LogDNA Web UI opens and displays your cluster logs.


## Step 4: View your logs
{: step4}

From the LogDNA Web UI, you can view your logs as they pass through the system. You view logs by using log tailing. 

**Note:** With the **Free** service plan, you can only tail your latest logs.



## Next steps
{: #next_steps}

  If you want to [filter cluster logs](https://docs.logdna.com/docs/filters), [search cluster logs](https://docs.logdna.com/docs/search), [define views](https://docs.logdna.com/docs/views), and [configure alerts](https://docs.logdna.com/docs/alerts), you must upgrade the IBM Log Analysis with LogDNA plan to a paid plan.



