---

copyright:
  years: 2018
lastupdated: "2018-10-22"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}


# Managing Kubernetes cluster logs with IBM Log Analysis with LogDNA
{: #kube}

To manage cluster logs with the IBM Log Analysis with LogDNA service, you must provision an instance
{:shortdesc}

## Before you begin
{: #prereqs}

You will be working in the US-South region. Both resources, the IBM Log Analysis with LogDNA instance and the Kubernetes cluster are running in the same account.

Read about IBM Log Analysis with LogDNA. For more information, see [About LogDNA](/docs/services/Log-Analysis-with-LogDNA/overview.html#about).

You must have a user ID that is a member or an owner of an {{site.data.keyword.Bluemix_notm}} account. To get an {{site.data.keyword.Bluemix_notm}} user ID, go to: [Registration ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://console.bluemix.net/registration/){:new_window}.

Your {{site.data.keyword.IBM_notm}}ID has `editor` role for the `Default` resource group for . 

Your {{site.data.keyword.IBM_notm}}ID has `editor` service role for the IBM Log Analysis with LogDNA service. 

Your {{site.data.keyword.IBM_notm}}ID has `editor` permissions for the Kubernetes Cloud service to work with a standard cluster in the US-South region.

Your {{site.data.keyword.IBM_notm}}ID has `editor` permissions for the Cluster instance in the US-South region. For more information, see [User access permissions](/docs/containers/cs_access_reference.html#understanding).

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

8. Select the **Free** service plan. 

    By default, the **Free** plan is set.

    For more information about other service plans, see [Pricing plans](/docs/services/Log-Analysis-with-LogDNA/overview.html#pricing_plans).

9. To provision the IBM Log Analysis with LogDNA service in the {{site.data.keyword.Bluemix_notm}} resource group where you are logged in, click **Create**.

After you provision an instance, the IBM Log Analysis with LogDNA dashboard opens. 


**Note:** To provision an instance of LogDNA through the CLI, see [Provisioning LogDNA through the {{site.data.keyword.Bluemix_notm}} CLI]().


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

2. Add a secret to your Kubernetes cluster. Run the following command:

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE
    {: pre}

    The LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE shows the LogDNA ingestion key for your instance.

    The Kubernetes secret contains the LogDNA ingestion key. The LogDNA ingestion key is used to authenticate the logging agent with the IBM Log Analysis with LogDNA service. It is used to open a secure web socket to the ingestion server on the logging back-end system.

3. Configure the LogDNA agent on every worker(node) of your Kubernetes cluster. Run the following command:

    ```
    kubectl create -f https://raw.github.ibm.com/alchemy-logging/vendor-config/master/logdna-agent-ibm-staging-ds.yaml
    ```
    {: pre}

    The LogDNA agent is responsible for collecting and forwarding your logs.

    The agent collects automatically logs with extension *.log and extensionless files that are located under /var/log. By default, logs are collected from all namespaces, including the kube-system.


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



