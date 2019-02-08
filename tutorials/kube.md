---

copyright:
  years: 2018, 2019
lastupdated: "2019-01-08"

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


# Managing Kubernetes cluster logs with {{site.data.keyword.la_full_notm}}
{: #kube}

Use the {{site.data.keyword.la_full_notm}} service to configure cluster-level logging in {{site.data.keyword.containerlong}}. 
{:shortdesc}

From the moment you provision a cluster with {{site.data.keyword.containerlong_notm}}, you want to know what is happening inside the cluster. You need to access logs to troubleshoot problems and pre-empt issues. At any time, you want to have access to different types of logs such as worker logs, pod logs, app logs, or network logs. In addition, you want to monitor different sources of log data in your Kubernetes cluster. Therefore, your ability to manage and access log records from any of these sources is critical. Your success managing and monitoring logs depends on how you configure the logging capabilities for your Kubernetes platform.

To configure cluster-level logging for a Kubernetes cluster, consider the following information:

* You must be able to store log data, system logs, and containerized application logs on separate storage from Kubernetes system components.
* You must deploy a logging agent to every worker node in your cluster. This agent collects and forwards logs to an external logging back-end.
* You must be able to centralize log data for analysis on an external logging back-end.


On the {{site.data.keyword.Bluemix_notm}}, to configure cluster-level logging for a Kubernetes cluster, you must complete the following steps:

1. Provision an instance of the {{site.data.keyword.la_full_notm}} service. With this step, you configure a centralized log management system where log data is hosted on {{site.data.keyword.Bluemix_notm}}.
2. Provision a cluster on the {{site.data.keyword.containerlong_notm}}. Kubernetes v1.9+ clusters are supported.
3. Configure the LogDNA agent on every worker (node) in a cluster.

![LogDNA component overview on the {{site.data.keyword.Bluemix_notm}}](../images/kube.png "LogDNA component overview on the {{site.data.keyword.Bluemix_notm}}")

In this tutorial, you will learn how to configure cluster-level logging.

## Before you begin
{: #prereqs}

Work in the US-South region. The {{site.data.keyword.la_full_notm}} is currently available in the US South region. **Note:** You can send data from a Kubernetes cluster that is located in the same region or in a different region. 

Read about {{site.data.keyword.la_full_notm}}. For more information, see [About](/docs/services/Log-Analysis-with-LogDNA/overview.html#about).

Use a user ID that is a member or an owner of an {{site.data.keyword.Bluemix_notm}} account. To get an {{site.data.keyword.Bluemix_notm}} user ID, go to: [Registration ![External link icon](../../../icons/launch-glyph.svg "External link icon")](http://cloud.ibm.com /registration/){:new_window}.

Your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources: 

| Resource                             | Scope of the access policy | Role    | Region    | Information                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Resource group **Default**           |  Resource group            | Viewer  | us-south  | This policy is required to allow the user to see service instances in the Default resource group.    |
| {{site.data.keyword.la_full_notm}} service |  Resource group            | Editor  | us-south  | This policy is required to allow the user to provision and administer the {{site.data.keyword.la_full_notm}} service in the Default resource group.   |
| Kubernetes cluster instance          |  Resource                 | Editor  | us-south  | This policy is required to configure the secret and the LogDNA agent in the Kubernetes cluster. |
{: caption="Table 1. List of IAM policies required to complete the tutorial" caption-side="top"} 

For more information about the {{site.data.keyword.containerlong}} IAM roles, see [User access permissions](/docs/containers/cs_access_reference.html#understanding).

Install the {{site.data.keyword.Bluemix_notm}} CLI. For more information, see [Installing the {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli/index.html#overview).

Install the Kubernetes CLI plug-in. For more information, see [Installing the CLI](/docs/containers/cs_cli_install.html#cs_cli_install).


## Objectives
{: #objectives}

In this tutorial, you configure logging with LogDNA for your {{site.data.keyword.containerlong_notm}} cluster. In particular, you will:

- Provision an {{site.data.keyword.la_full_notm}}. 
- Configure the LogDNA agent in your cluster to start sending logs to LogDNA. 
- Open the LogDNA dashboard to find your logs. 


## Prerequisites
{: #prerequisites}

To complete this tutorial, you must complete the following tasks: 

1. [Create an {{site.data.keyword.containerlong_notm}} cluster with a Kubernetes version of 1.10](/docs/containers/cs_clusters.html#clusters_ui) or higher in the US South location. {{site.data.keyword.la_full_notm}} is supported in US South only. To configure logging for your cluster, the cluster and the {{site.data.keyword.la_full_notm}} service must be in the same location. 
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
   <td>{{site.data.keyword.la_full_notm}} service</td>
   <td>Resource group</td>
   <td>Editor</td>
   <td>us-south</td>
   <td>This policy is required to allow the user to provision and administer the {{site.data.keyword.la_full_notm}} service in the <strong>Default</strong> resource group.</td>
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


## Step1: Provision an {{site.data.keyword.la_full_notm}} service instance
{: #step1}

To provision a service instance of {{site.data.keyword.la_full_notm}} through the {{site.data.keyword.Bluemix_notm}} console, complete the following steps:

1. Log in to the [{{site.data.keyword.Bluemix_notm}} account ![External link icon](../../../icons/launch-glyph.svg "External link icon")](http://cloud.ibm.com ) where you created your Kubernetes cluster.

2. Click **Catalog**. A list of {{site.data.keyword.Bluemix_notm}} services opens.

3. To filter the list of services that is displayed, select the **Developer Tools** category.

4. Click **{{site.data.keyword.la_full_notm}}**. The **Observability** dashboard opens.

5. Select **Create instance**. 

6. Enter a name for the service instance.

7. Select the resource group that your cluster is in. By default, the **Default** resource group is set for you. 

8. Choose a service plan for your service instance. By default, the **Lite** plan is selected for you. For more information about other service plans, see [Pricing plans](/docs/services/Log-Analysis-with-LogDNA/overview.html#pricing_plans).

9. To provision the {{site.data.keyword.la_full_notm}} service in the {{site.data.keyword.Bluemix_notm}} resource group where you are logged in, click **Create**. The **Observability** dashboard opens and shows the details for your service. 

To provision an instance through the CLI, see [Provisioning an instance through the {{site.data.keyword.Bluemix_notm}} CLI](/docs/services/Log-Analysis-with-LogDNA/provision.html#provision_cli).
{: tip}


## Step2: Configure your Kubernetes cluster to send logs to your LogDNA instance
{: #step2}

To configure your Kubernetes cluster to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install a `logdna-agent` pod on each node of your cluster. The LogDNA agent reads log files from the pod where it is installed, and forwards the log data to your LogDNA instance.

To configure your Kubernetes cluster to forward logs to your LogDNA instance, complete the following steps from the command line:

1. Open a terminal to log in to {{site.data.keyword.Bluemix_notm}}.

   ```
   ibmcloud login -a api.ng.bluemix.net
   ```
   {: pre}

   Select the account where you have provisioned the {{site.data.keyword.la_full_notm}} instance.

2. Set the cluster where you want to configure logging as the context for this session.

   ```
   ibmcloud ks cluster-config <cluster_name_or_ID>
   ```
   {: pre}

   When the download of the configuration files is finished, a command is displayed that you can use to set the path to the local Kubernetes configuration file as an environment variable. Copy and paste the command that is displayed in your terminal to set the `KUBECONFIG` environment variable.

   Every time you log in to the {{site.data.keyword.containerlong_notm}} CLI to work with your cluster, you must run this setup to set the path to the cluster's configuration file as a session variable. {{site.data.keyword.containerlong_notm}} uses this variable to find a local configuration file and certificates that are necessary to connect with your cluster.
   {: tip}

3. Create a Kubernetes secret to store your logDNA ingestion key for your service instance. The LogDNA ingestion key is used to open a secure web socket to the logDNA ingestion server and to authenticate the logging agent with the {{site.data.keyword.la_full_notm}} service.

   ```
   kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<logDNA_ingestion_key>
   ```
   {: pre}

4. Create a Kubernetes daemon set to deploy the LogDNA agent on every worker node of your Kubernetes cluster. The LogDNA agent collects logs with the extension `*.log` and extensionsless files that are stored in the `/var/log` directory of your pod. By default, logs are collected from all namespaces, including `kube-system`, and automatically forwarded to the {{site.data.keyword.la_full_notm}} service.

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

1. Log in to your [{{site.data.keyword.Bluemix_notm}} account ![External link icon](../../../icons/launch-glyph.svg "External link icon")](http://cloud.ibm.com ).

2. From the menu ![Menu icon](../icons/icon_hamburger.svg "Menu icon"), select **Observability**.

3. Select **Logging**. The list of {{site.data.keyword.la_full_notm}} service instances that are available on {{site.data.keyword.Bluemix_notm}} is displayed.

4. Select one instance and click **View LogDNA**. The LogDNA dashboard opens. **Note:** With the **Free** service plan, you can tail your latest logs only. For more information, see [Viewing logs](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#view_logs).

## Next steps
{: #next_steps}

- [Filter logs](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#step5)
- [Search logs](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#step6)
- [Define views](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#step7)
- [Configure alerts](https://docs.logdna.com/docs/alerts). 

**Note:** Some of these features require a plan upgrade.




