---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, detach config agent

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Disconnecting a logging agent
{: #detach_agent}

Detach a logging agent from a logging instance to stop collecting logs.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

## Detaching a logging agent  from a standard Kubernetes cluster
{: #detach_agent_kube}

To stop your Kubernetes cluster from sending logs to your {{site.data.keyword.la_full_notm}} instance, you must remove the logging agent from your cluster.


### Detaching a logging agent by using the agent yaml file
{: #detach_agent_kube_kubectl_v2}

To stop your Kubernetes cluster from forwarding logs to your logging instance, complete the following steps from the command line:

1. Open a terminal. Then, [log in to the {{site.data.keyword.cloud_notm}}](https://cloud.ibm.com/login){: external}, and follow the prompts.

    Select the account where you provisioned the {{site.data.keyword.la_full_notm}} instance.

2. Set up the cluster environment. Run the following commands:

    First, get the command to set the environment variable and download the Kubernetes configuration files.

    ```text
    ibmcloud ks cluster config --cluster <cluster_name_or_ID>
    ```
    {: codeblock}

3. Remove the secret from your Kubernetes cluster. The Kubernetes secret contains the logging ingestion key. Run the following command:

    ```text
    kubectl delete secret logdna-agent-key -n ibm-observe
    ```
    {: codeblock}

4. Remove the logging agent on every worker(node) of your Kubernetes cluster. Run the following command:

    | Type of endpoint | Command |
    |------------------|---------|
    | Public endpoint  | `kubectl delete -f https://assets.<REGION>.logging.cloud.ibm.com/clients/logdna-agent/<VERSION>/agent-resources.yaml` |
    | Private endpoint | `kubectl delete -f https://assets.<REGION>.logging.cloud.ibm.com/clients/logdna-agent/<VERSION>/agent-resources-private.yaml` |

    Where

    - `<REGION>` indicates the region where the logging instance is available. For more information about regions, see [Locations](/docs/log-analysis?topic=log-analysis-regions).
    - `<VERSION>` indicates the version of the agent that you have deployed. You must use a version that has a tag with the following format: `X.Y.Z` or use your custom yaml file.

5. To verify that the logging agent is deleted successfully, run the following command:

    ```text
    kubectl get pods -n ibm-observe
    ```
    {: codeblock}

    You should not see any logging pods.

### Detaching a logging agent by using kubectl commands
{: #detach_agent_kube_kubectl_v1}

To stop your Kubernetes cluster from forwarding logs to your logging instance, complete the following steps from the command line:

1. Open a terminal. Then, [log in to the {{site.data.keyword.cloud_notm}}](https://cloud.ibm.com/login){: external}, and follow the prompts.

    Select the account where you provisioned the {{site.data.keyword.la_full_notm}} instance.

2. Set up the cluster environment. Run the following commands:

    First, get the command to set the environment variable and download the Kubernetes configuration files.

    ```text
    ibmcloud ks cluster config --cluster <cluster_name_or_ID>
    ```
    {: codeblock}

3. Remove the secret from your Kubernetes cluster. The Kubernetes secret contains the logging ingestion key. Run the following command:

    ```text
    kubectl delete secret logdna-agent-key -n ibm-observe
    ```
    {: codeblock}

4. Remove the logging agent on every worker(node) of your Kubernetes cluster. The logging agent is responsible for collecting and forwarding your logs. Run the following command:

    ```text
    kubectl delete daemonset logdna-agent -n ibm-observe
    ```
    {: codeblock}

5. To verify that the logging agent is deleted successfully, run the following command:

    ```text
    kubectl get pods -n ibm-observe
    ```
    {: codeblock}

    You should not see any logging pods.



### Detaching a logging agent from the cluster console
{: #detach_agent_kube_console}

This option is only valid when you deploy the logging agent from the {{site.data.keyword.containerlong_notm}} console.
{: note}

Complete the following steps from the [{{site.data.keyword.containerlong_notm}} console](https://cloud.ibm.com/kubernetes/clusters){: external}:

1. Select the cluster for which you want to create a logging logging configuration.

2. On the cluster **Overview** page, in the *Logging* section, click **Disconnect**.





### Detaching a logging agent by using ob commands
{: #detach_agent_kube_console_ob}

This option is only valid when you deploy the logging agent by using ob commands.
{: note}

Complete the following steps:

1. Set the cluster context.

    Open a terminal to log in to {{site.data.keyword.cloud_notm}}.

    ```text
    ibmcloud login -a cloud.ibm.com
    ```
    {: pre}

    Select the account where you provisioned the {{site.data.keyword.la_full_notm}} instance.

    List the clusters to find out in which region and resource group the cluster is available.

    ```text
    ibmcloud ks clusters
    ```
    {: pre}

    Set the resource group and region.

    ```text
    ibmcloud target -g RESOURCE_GROUP -r REGION
    ```
    {: pre}

    Where

    `RESOURCE_GROUP` is the name of the resource group where the cluster is available, for example, `default`.

    `REGION` is the region where the cluster is available, for example, `us-south`.

    Set the cluster where you want to configure logging as the context for this session.

    ```text
    ibmcloud ks cluster config --cluster <cluster_name_or_ID>
    ```
    {: pre}

2. Detach the logging agent by using the `ob` CLI. Run the following command:

    ```text
    ibmcloud ob logging config delete --cluster <cluster_name_or_ID> --instance <LogDNA_instance_name_or_ID>  [--force]
    ```
    {: pre}

    Where

    * `<cluster_name_or_ID>` is the name or the ID of the cluster.

    * `<LogDNA_instance_name_or_ID>` is the name or the ID of the logging instance where you want to forward the cluster logs for analysis.

    * `[--force]`  is used to force the command to run with no user prompts.






## Detaching a logging agent from an Openshift Kubernetes cluster
{: #detach_agent_os}

To stop your OpenShift cluster from sending logs to your {{site.data.keyword.la_full_notm}} instance, you must remove the logging agent from your cluster.

### Detaching a logging agent by using kubectl commands
{: #detach_agent_os_kube_kubectl}

Complete the following steps from the command line:

1. Open a terminal to log in to {{site.data.keyword.cloud_notm}}.

   ```text
   ibmcloud login -a cloud.ibm.com
   ```
   {: pre}

   Select the account where you provisioned the {{site.data.keyword.la_full_notm}} instance.

2. Set the cluster where you want to configure logging as the context for this session.

   ```text
   ibmcloud cs cluster config --cluster <cluster_name_or_ID>
   ```
   {: pre}

3. Log in to the cluster. Choose a method to login to an OpenShift cluster. [Learn more about the methods to login](/docs/openshift?topic=openshift-access_cluster#access_automation).

4. Delete the logging agent serviceaccount.

    ```text
    oc delete serviceaccount logdna-agent -n ibm-observe
    ```
    {: pre}

5. Remove the logging secrets from your cluster. Each secret contains the logging ingestion key. Run the following commands:

    List secrets.

    ```text
    oc get secrets -n ibm-observe
    ```
    {: pre}

    Then, run the following command for each secret:

    ```text
    oc delete secret logdna-agent-key -n ibm-observe
    ```
    {: pre}

6. Remove the logging agent on every worker(node) of your Kubernetes cluster. The logging agent is responsible for collecting and forwarding your logs. Run the following command:

    ```text
    kubectl delete -f https://<ENDPOINT>/clients/logdna-agent-ds-os.yaml -n ibm-observe
    ```
    {: codeblock}

    Where `<ENDPOINT>` is the [endpoint where the agent was installed.](/docs/log-analysis?topic=log-analysis-config_agent_os_cluster#config_agent_os_cluster_step4_v1)

7. Verify that the logging agent is deleted successfully. Run the following command to verify that logging agent pods are not running:

    ```text
    oc get pods -n ibm-observe
    ```
    {: codeblock}




### Detaching a logging agent from the OpenShift console
{: #detach_agent_os_console}

This option is only valid when you deploy the logging agent from the OpenShift console.
{: note}

Complete the following steps from the [OpenShift console](https://cloud.ibm.com/kubernetes/clusters?platformType=openshift){: external}:

1. Select the cluster for which you want to create a logging logging configuration.

2. On the cluster **Overview** page, in the *Logging* section, click **Disconnect**.





### Detaching a logging agent by using ob commands
{: #detach_agent_os_console_ob}

This option is only valid when you deploy the logging agent by using ob commands.
{: note}

Complete the following steps:

1. Set the cluster context.

    Open a terminal to log in to {{site.data.keyword.cloud_notm}}.

    ```text
    ibmcloud login -a cloud.ibm.com
    ```
    {: pre}

    Select the account where you provisioned the {{site.data.keyword.la_full_notm}} instance.

    List the clusters to find out in which region and resource group the cluster is available.

    ```text
    ibmcloud ks clusters
    ```
    {: pre}

    Set the resource group and region.

    ```text
    ibmcloud target -g RESOURCE_GROUP -r REGION
    ```
    {: pre}

    Where

    `RESOURCE_GROUP` is the name of the resource group where the cluster is available, for example, `default`.

    `REGION` is the region where the cluster is available, for example, `us-south`.

    Set the cluster where you want to configure logging as the context for this session.

    ```text
    ibmcloud oc cluster config --cluster <cluster_name_or_ID>
    ```
    {: pre}

2. Detach the logging agent by using the `ob` CLI. Run the following command:

    ```text
    ibmcloud ob logging config delete --cluster <cluster_name_or_ID> --instance <LogDNA_instance_name_or_ID>  [--force]
    ```
    {: pre}

    Where

    * `<cluster_name_or_ID>` is the name or the ID of the cluster.

    * `<LogDNA_instance_name_or_ID>` is the name or the ID of the logging instance where you want to forward the cluster logs for analysis.

    * `[--force]`  is used to force the command to run with no user prompts.
