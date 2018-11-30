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
{:note .note}


# Managing Kubernetes cluster logs with IBM Log Analysis with LogDNA
{: #kube}

Use the IBM Log Analysis with LogDNA service to configure cluster-level logging in {{site.data.keyword.containerlong}}. 
{:shortdesc}

From the moment you provision a cluster with {{site.data.keyword.containerlong_notm}}, you want to know what is happening inside the cluster. You need to access logs to troubleshoot problems and pre-empt issues. At any time, you want to have access to different types of logs such as worker logs, pod logs, app logs, or network logs. In addition, you want to monitor different sources of log data in your Kubernetes cluster. Therefore, your ability to manage and access log records from any of these sources is critical. Your success managing and monitoring logs depends on how you configure the logging capabilities for your Kubernetes platform.

To configure cluster-level logging for a Kubernetes cluster, consider the following information:

* You must be able to store log data, system logs, and containerized application logs on separate storage from Kubernetes system components.
* You must deploy a logging agent to every worker node in your cluster. This agent collects and forwards logs to an external logging back-end.
* You must be able to centralize log data for analysis on an external logging back-end.

![LogDNA component overview in {{site.data.keyword.Bluemix_notm}}](../images/kube.png "LogDNA component overview in {{site.data.keyword.Bluemix_notm}}")

For more information about IBM Log Analysis with LogDNA, see [About](/docs/services/Log-Analysis-with-LogDNA/overview.html#about).


## Objectives
{: #objectives}

In this tutorial, you configure logging with LogDNA for your {{site.data.keyword.containerlong_notm}} cluster. In particular, you will:

- Provision an IBM Log Analysis with LogDNA. 
- Configure the LogDNA agent in your cluster to start sending logs to LogDNA. 
- Open the LogDNA dashboard to find your logs. 


## Prerequisites
{: #prerequisites}

To complete this tutorial, you must complete the following tasks: 

1. [Create an {{site.data.keyword.containerlong_notm}} cluster with a Kubernetes version of 1.10](/docs/containers/cs_clusters.html#clusters_ui) or higher in the US South location. IBM Log Analysis with LogDNA is supported in US South only. To configure logging for your cluster, the cluster and the IBM Log Analysis with LogDNA service must be in the same location. 
2. Make sure that your user is assigned the following IAM permissions. 
   <table>
   <caption>Table 1. List of IAM policies required to complete the tutorial</caption>
   <thead>
   <th>Resource</th>
   <th>Scope of the access policy </th>
   <th>Role</th>
   <th>Region</th>
   <th>Information</th>
   </thead>
   <tbody>
   <tr>
   <td>Resource group <strong>Default</strong></td>
   <td>Resource group</td>
   <td>Viewer</td>
   <td>us-south</td>
   <td>This policy is required to allow the user to see service instances in the <strong>Default</strong> resource group.</td>
   </tr>
   <tr>
   <td>IBM Log Analysis with LogDNA service</td>
   <td>Resource group</td>
   <td>Editor</td>
   <td>us-south</td>
   <td>This policy is required to allow the user to provision and administer the IBM Log Analysis with LogDNA service in the <strong>Default</strong> resource group.</td>
   </tr>
   <tr>
   <td>{{site.data.keyword.containerlong_notm}}</td>
   <td>Resource</td>
   <td>Editor</td>
   <td>us-south</td>
   <td>This policy is required to configure the secret and the LogDNA agent in the Kubernetes cluster.</td>
   </tr>
   </tbody>
   </table>

   For more information about {{site.data.keyword.containerlong_notm}} IAM roles, see [User access permissions](/docs/containers/cs_access_reference.html#understanding).
   
3. [Install the {{site.data.keyword.Bluemix_notm}} CLI and the {{site.data.keyword.containerlong_notm}} CLI plug-in](/docs/cli/index.html#overview). 


## Step1: Provision an IBM Log Analysis with LogDNA service instance
{: #step1}

To provision a service instance of IBM Log Analysis with LogDNA through the {{site.data.keyword.Bluemix_notm}} console, complete the following steps:

1. Log in to the [{{site.data.keyword.Bluemix_notm}} account ![External link icon](../icons/launch-glyph.svg "External link icon")](https://console.bluemix.net) where you created your Kubernetes cluster.

2. Click **Catalog**. A list of {{site.data.keyword.Bluemix_notm}} services opens.

3. To filter the list of services that is displayed, select the **Developer Tools** category.

4. Click **IBM Log Analysis with LogDNA**. The **Observability** dashboard opens.

5. Select **Create instance**. 

6. Enter a name for the service instance.

7. Select the resource group that your cluster is in. By default, the **Default** resource group is set for you. 

8. Choose a service plan for your service instance. By default, the **Lite** plan is selected for you. For more information about other service plans, see [Pricing plans](/docs/services/Log-Analysis-with-LogDNA/overview.html#pricing_plans).

9. To provision the IBM Log Analysis with LogDNA service in the {{site.data.keyword.Bluemix_notm}} resource group where you are logged in, click **Create**. The **Observability** dashboard opens and shows the details for your service. 

To provision an instance through the CLI, see [Provisioning an instance through the {{site.data.keyword.Bluemix_notm}} CLI](/docs/services/Log-Analysis-with-LogDNA/provision.html#provision_cli).
{: tip}


## Step2: Configure your Kubernetes cluster to send logs to your LogDNA instance
{: #step2}

To configure your Kubernetes cluster to send logs to your IBM Log Analysis with LogDNA instance, you must install a `logdna-agent` pod on each node of your cluster. The LogDNA agent reads log files from the pod where it is installed, and forwards the log data to your LogDNA instance.

To configure your Kubernetes cluster to forward logs to your LogDNA instance, complete the following steps from the command line:

1. Open a terminal to log in to {{site.data.keyword.Bluemix_notm}}.
   ```
   ibmcloud login -a api.ng.bluemix.net
   ```
   {: pre}

   Select the account where you have provisioned the IBM Log Analysis with LogDNA instance.

2. Set the cluster where you want to configure logging as the context for this session.
   ```
   ibmcloud ks cluster-config <cluster_name_or_ID>
   ```
   {: pre}

   When the download of the configuration files is finished, a command is displayed that you can use to set the path to the local Kubernetes configuration file as an environment variable. Copy and paste the command that is displayed in your terminal to set the `KUBECONFIG` environment variable.

   Every time you log in to the {{site.data.keyword.containerlong_notm}} CLI to work with your cluster, you must run this setup to set the path to the cluster's configuration file as a session variable. {{site.data.keyword.containerlong_notm}} uses this variable to find a local configuration file and certificates that are necessary to connect with your cluster.
   {: tip}

3. Create a Kubernetes secret to store your logDNA ingestion key for your service instance. The LogDNA ingestion key is used to open a secure web socket to the logDNA ingestion server and to authenticate the logging agent with the IBM Log Analysis with LogDNA service.
   ```
   kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<logDNA_ingestion_key>
   ```
   {: pre}

4. Create a Kubernetes daemon set to deploy the LogDNA agent on every worker node of your Kubernetes cluster. The LogDNA agent collects logs with the extension `*.log` and extensionsless files that are stored in the `/var/log` directory of your pod. By default, logs are collected from all namespaces, including `kube-system`, and automatically forwarded to the IBM Log Analysis with LogDNA service.
   ```
   kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
   ```
   {: pre}

5. Verify that the LogDNA agent is deployed successfully. 
   ```
   kubectl get pods
   ```
   {: pre}
   
   The deployment is successful when you see one or more LogDNA pods. The number of LogDNA pods equals the number of worker nodes in your cluster. All pods must be in a `Running` state.


## Step 3: Launch the LogDNA dashboard and view logs
{: #step3}

To launch the LogDNA dashboard through the {{site.data.keyword.Bluemix_notm}} console, complete the following steps:

1. Log in to your [{{site.data.keyword.Bluemix_notm}} account ![External link icon](../icons/launch-glyph.svg "External link icon")](https://console.bluemix.net).

2. From the menu ![Menu icon](../icons/icon_hamburger.svg "Menu icon"), select **Observability**.

3. Select **Logging**. The list of IBM Log Analysis with LogDNA service instances that are available on {{site.data.keyword.Bluemix_notm}} is displayed.

4. Select one instance and click **View LogDNA**. The LogDNA dashboard opens. **Note:** With the **Free** service plan, you can tail your latest logs only. For more information, see [Viewing logs](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#view_logs).

## Next steps
{: #next_steps}

- [Filter logs](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#step5)
- [Search logs](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#step6)
- [Define views](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#step7)
- [Configure alerts](https://docs.logdna.com/docs/alerts). 

To use any of these features, you must upgrade the IBM Log Analysis with LogDNA plan to a paid plan.
{: note}



