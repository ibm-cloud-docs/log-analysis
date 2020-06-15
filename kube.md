---

copyright:
  years:  2018, 2020
lastupdated: "2020-06-01"

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


# Collecting, configuring, and analyzing logs from Kubernetes clusters (cluster-level logging)
{: #kube}

You can configure a LogDNA agent to collect logs from a Kubernetes cluster and forward them to an instance of the {{site.data.keyword.la_full_notm}} service.
{:shortdesc}

You can collect and monitor logs from a Kubernetes cluster that is located in the same {{site.data.keyword.cloud_notm}} region as your {{site.data.keyword.la_full_notm}} instance or in a different one. You can also collect and monitor logs from clusters that are located outside the {{site.data.keyword.cloud_notm}}.
{: note}


From the moment you provision a cluster with {{site.data.keyword.containerlong_notm}}, you want to know what is happening inside the cluster. You need to access logs to troubleshoot problems and pre-empt issues. At any time, you want to have access to different types of logs such as worker logs, pod logs, app logs, or network logs. In addition, you want to monitor different sources of log data in your Kubernetes cluster. Therefore, your ability to manage and access log records from any of these sources is critical. Your success managing and monitoring logs depends on how you configure the logging capabilities for your Kubernetes platform.

To configure cluster-level logging for a Kubernetes cluster, consider the following information:

* You must be able to store log data, system logs, and containerized application logs on separate storage from Kubernetes system components.
* You must deploy a logging agent to every worker node in your cluster. This agent collects and forwards logs to an external logging back-end.
* You must be able to centralize log data for analysis on an external logging back-end.


To configure cluster-level logging for a Kubernetes cluster, you must complete the following steps:

1. Provision an instance of the {{site.data.keyword.la_full_notm}} service. With this step, you configure a centralized log management system where log data is hosted on {{site.data.keyword.cloud_notm}}.
2. Provision a cluster, for example, a standard cluster on the {{site.data.keyword.containerlong_notm}}.
3. Deploy and configure the LogDNA agent in the cluster.

![LogDNA component overview on the {{site.data.keyword.cloud_notm}}](../images/kube.png "LogDNA component overview on the {{site.data.keyword.cloud_notm}}")



## Before you begin
{: #kube_prereqs}

Complete the following tasks:

1. [Read about {{site.data.keyword.la_full_notm}}](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-getting-started).

2. [Check the {{site.data.keyword.la_full_notm}} regions that are supported](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-regions). 

3. [Install the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli).

4. Use an {{site.data.keyword.IBM_notm}} ID that is a member or an owner of an {{site.data.keyword.cloud_notm}} account. 

    To get an {{site.data.keyword.cloud_notm}} user ID, go to: [Registration ![External link icon](../../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window}.

5. Provision an {{site.data.keyword.la_full_notm}} instance. Choose any of the following methods:  

    [Provisioning an instance through the Observability dashboard](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-provision#provision_ui)

    [Provisioning an instance through the CLI](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-provision#provision_cli)

6. Get the ingestion key for the {{site.data.keyword.la_full_notm}} instance where you want to monitor your cluster logs. Choose any of the following methods:

    [Get the ingestion key through the IBM Cloud UI](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-ingestion_key#ibm_cloud_ui).

    [Get the ingestion key through the CLI](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-ingestion_key#ingestion_key_cli).

7. Check that you have permissions and access to the cluster. 

    For more information about the {{site.data.keyword.containerlong}} IAM roles, see [User access permissions](/docs/containers?topic=containers-access_reference#access_reference).




Your IBMid must have assigned IAM policies for each of the following resources in the region that your {{site.data.keyword.la_full_notm}} instance is in:  

| Resource                             | Scope of the access policy | Role    | Information                  |
|--------------------------------------|----------------------------|---------|------------------------------|
| Resource group **default**           |  Resource group            | Viewer  | This policy is required to allow the user to see service instances in the Default resource group.|
| {{site.data.keyword.la_full_notm}} service |  Resource group            | Editor  | This policy is required to allow the user to provision and administer the {{site.data.keyword.la_full_notm}} service in the default resource group.   |
| Kubernetes cluster instance          |  Resource                 | Editor  | This policy is required to configure the secret and the LogDNA agent in the Kubernetes cluster. |
{: caption="Table 1. List of IAM policies required to complete the tutorial" caption-side="top"} 


## Step 1. Configure your Kubernetes cluster to send logs to your LogDNA instance
{: #kube_step1}

To configure your Kubernetes cluster to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install the LogDNA agent in the cluster. 

* The LogDNA agent automatically collects STDOUT and STDERR logs.
* By default, the LogDNA agent monitors all files with extension *.log*, and extensionless files under */var/log/*.

Choose one of the following options to deploy and configure the LogDNA agent in your cluster, and connect the agent with your {{site.data.keyword.la_full_notm}} instance:

* [Connect a standard Kubernetes cluster to an {{site.data.keyword.la_full_notm}} instance by using a LogDNA agent](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-config_agent_kube_cluster).

* [Connect an OpenShift Kubernetes cluster to an {{site.data.keyword.la_full_notm}} instance by using a LogDNA agent](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-config_agent_os_cluster).



## [Optional] Step 2. Configure a cluster to forward API audit logs to LogDNA
{: #kube_step2}

If you want to analyze the cluster's API audit logs through the IBM Log Analysis with LogDNA instance, you must configure your cluster:






## Step 3. Launch the LogDNA dashboard to view and analyze logs
{: #kube_step3}

To analyze logs and generate alerts, you might need to upgrade your service plan. [Learn more about service plans](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-service_plans).
{: important}


Complete the following steps:

1. [Navigate to the web UI](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-launch).

2. Analyze your logs:

    - [Filter logs](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-view_logs#view_logs_step5)
    
    - [Search logs](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-view_logs#view_logs_step6)

    - [Define views](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-view_logs#view_logs_step7)

    - [Configure alerts](https://docs.logdna.com/docs/alerts). 


## [Optional] Step 4. Remove duplicate logs by defining exclusion rules
{: #kube_step4}





## Next steps
{: #kube_next_steps}



