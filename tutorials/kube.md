---

copyright:
  years:  2018, 2020
lastupdated: "2020-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, kubernetes, tutorial

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


# Managing Kubernetes cluster logs with {{site.data.keyword.la_full_notm}}
{: #kube}

Use the {{site.data.keyword.la_full_notm}} service to configure cluster-level logging in {{site.data.keyword.containerlong}}. 
{:shortdesc}

From the moment you provision a cluster with {{site.data.keyword.containerlong_notm}}, you want to know what is happening inside the cluster. You need to access logs to troubleshoot problems and pre-empt issues. At any time, you want to have access to different types of logs such as worker logs, pod logs, app logs, or network logs. In addition, you want to monitor different sources of log data in your Kubernetes cluster. Therefore, your ability to manage and access log records from any of these sources is critical. Your success managing and monitoring logs depends on how you configure the logging capabilities for your Kubernetes platform.

To configure cluster-level logging for a Kubernetes cluster, consider the following information:

* You must be able to store log data, system logs, and containerized application logs on separate storage from Kubernetes system components.
* You must deploy a logging agent to every worker node in your cluster. This agent collects and forwards logs to an external logging back-end.
* You must be able to centralize log data for analysis on an external logging back-end.


On the {{site.data.keyword.cloud_notm}}, to configure cluster-level logging for a Kubernetes cluster, you must complete the following steps:

1. Provision an instance of the {{site.data.keyword.la_full_notm}} service. With this step, you configure a centralized log management system where log data is hosted on {{site.data.keyword.cloud_notm}}.
2. Provision a cluster on the {{site.data.keyword.containerlong_notm}}. Kubernetes v1.9+ clusters are supported.
3. Configure the logging agent on every worker (node) in a cluster.

![LogDNA component overview on the {{site.data.keyword.cloud_notm}}](../images/kube.png "LogDNA component overview on the {{site.data.keyword.cloud_notm}}")

In this tutorial, you will learn how to configure cluster-level logging.

## Before you begin
{: #kube_prereqs}

Work in a [supported region](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-regions). **Note:** You can send data from a Kubernetes cluster that is located in the same region or in a different region. 

Read about {{site.data.keyword.la_full_notm}}. For more information, see [About](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-getting-started#getting-started_ov).

Use a user ID that is a member or an owner of an {{site.data.keyword.cloud_notm}} account. To get an {{site.data.keyword.cloud_notm}} user ID, go to: [Registration](https://cloud.ibm.com/login){: external}.

Your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources in the region that your {{site.data.keyword.la_full_notm}} instance is in:  

| Resource                             | Scope of the access policy | Role    | Information                  |
|--------------------------------------|----------------------------|---------|------------------------------|
| Resource group **default**           |  Resource group            | Viewer  | This policy is required to allow the user to see service instances in the Default resource group.|
| {{site.data.keyword.la_full_notm}} service |  Resource group            | Editor  | This policy is required to allow the user to provision and administer the {{site.data.keyword.la_full_notm}} service in the default resource group.   |
| Kubernetes cluster instance          |  Resource                 | Editor  | This policy is required to configure the secret and the logging agent in the Kubernetes cluster. |
{: caption="Table 1. List of IAM policies required to complete the tutorial" caption-side="top"} 

For more information about the {{site.data.keyword.containerlong}} IAM roles, see [User access permissions](/docs/containers?topic=containers-access_reference#access_reference).

Install the {{site.data.keyword.cloud_notm}} CLI and the Kubernetes CLI plug-in. For more information, see [Installing the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-install-ibmcloud-cli).


## Objectives
{: #kube_objectives}

In this tutorial, you configure logging with LogDNA for your {{site.data.keyword.containerlong_notm}} cluster. In particular, you will:

- Provision an {{site.data.keyword.la_full_notm}}. 
- Configure the logging agent in your cluster to start sending logs to LogDNA. 
- Open the LogDNA dashboard to find your logs. 


## Step 1. Provision an {{site.data.keyword.la_full_notm}} service instance
{: #kube_step1}

To provision a service instance of {{site.data.keyword.la_full_notm}} through the {{site.data.keyword.cloud_notm}} console, complete the following steps:

1. Log in to the [{{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external} where you created your Kubernetes cluster.

2. Click **Catalog**. A list of {{site.data.keyword.cloud_notm}} services opens.

3. To filter the list of services that is displayed, select the **Logging and Monitoring** category.

4. Click **{{site.data.keyword.la_full_notm}}**. The **Observability** dashboard opens.

5. Select **Create instance**. 

6. Enter a name for the service instance and a location.

7. Select the resource group that your cluster is in. By default, the **Default** resource group is set for you. 

8. Choose a service plan for your service instance. By default, the **Lite** plan is selected for you. For more information about other service plans, see [Pricing plans](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-service_plans).

9. To provision the {{site.data.keyword.la_full_notm}} service in the {{site.data.keyword.cloud_notm}} resource group where you are logged in, click **Create**. The **Observability** dashboard opens and shows the details for your service. 

To provision an instance through the CLI, see [Provisioning an instance through the {{site.data.keyword.cloud_notm}} CLI](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-provision#provision_cli).
{: tip}

## Step 2. Get the ingestion key
{: #kube_step2}

Complete the following steps to get the ingestion key:

1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

	After you log in, the {{site.data.keyword.cloud_notm}} UI opens.

2. Click the **Menu** icon ![Menu icon](images/icon_hamburger.svg) &gt; **Observability** to access the *Observability* dashboard.

3. Select **Logging**. The {{site.data.keyword.la_full_notm}} dashboard opens. You can see the list of logging instances that are available on {{site.data.keyword.cloud_notm}}.

3. Identify the instance for which you want to get the ingestion key, and click **View ingestion key**.

4. A window opens where you can click **Show** to view the ingestion key.


## Step3: Configure your Kubernetes cluster to send logs to your LogDNA instance
{: #kube_step3}

To configure your Kubernetes cluster to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install a `logdna-agent` pod on each node of your cluster. The logging agent reads log files from the pod where it is installed, and forwards the log data to your LogDNA instance.

To configure your Kubernetes cluster in the `us-south` region to forward logs to your LogDNA instance, complete the following steps from the command line:

1. Open a terminal to log in to {{site.data.keyword.cloud_notm}}.

   ```
   ibmcloud login -a cloud.ibm.com
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

4. Create a Kubernetes daemon set to deploy the logging agent on every worker node of your Kubernetes cluster. The logging agent collects logs with the extension `*.log` and extensionsless files that are stored in the `/var/log` directory of your pod. By default, logs are collected from all namespaces, including `kube-system`, and automatically forwarded to the {{site.data.keyword.la_full_notm}} service.

   ```
   kubectl create -f https://assets.us-south.logging.cloud.ibm.com/clients/logdna-agent-ds.yaml
   ```
   {: pre}

5. Verify that the logging agent is deployed successfully. 

   ```
   kubectl get pods
   ```
   {: pre}
   
   The deployment is successful when you see one or more LogDNA pods. The number of LogDNA pods equals the number of worker nodes in your cluster. All pods must be in a `Running` state.


## Step 4: Launch the LogDNA dashboard and view logs
{: #kube_step4}

To launch the LogDNA dashboard through the {{site.data.keyword.cloud_notm}} console, complete the following steps:

1. Log in to your [{{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

2. From the menu ![Menu icon](../icons/icon_hamburger.svg "Menu icon"), select **Observability**.

3. Select **Logging**. The list of {{site.data.keyword.la_full_notm}} service instances that are available on {{site.data.keyword.cloud_notm}} is displayed.

4. Select one instance and click **View LogDNA**. The LogDNA dashboard opens. **Note:** With the **Free** service plan, you can tail your latest logs only. For more information, see [Viewing logs](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-view_logs#view_logs).

## Next steps
{: #kube_next_steps}

- [Filter logs](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-view_logs#view_logs_step5)
- [Search logs](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-view_logs#view_logs_step6)
- [Define views](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-view_logs#view_logs_step7)
- [Configure alerts](https://docs.logdna.com/docs/alerts). 

**Note:** Some of these features require a plan upgrade.




