---

copyright:
  years:  2018, 2020
lastupdated: "2020-05-11"

keywords: LogDNA, IBM, Log Analysis, logging, detach config agent

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

# Disconnecting a LogDNA agent
{: #detach_agent}

Detach a LogDNA agent from a logging instance to stop collecting logs.
{:shortdesc}

## Detaching a LogDNA agent from a standard Kubernetes cluster
{: #detach_agent_kube}

To stop your Kubernetes cluster from sending logs to your {{site.data.keyword.la_full_notm}} instance, you must remove the LogDNA agent from your cluster. 

To stop your Kubernetes cluster from forwarding logs to your LogDNA instance, complete the following steps from the command line:

1. Open a terminal. Then, [log in to the {{site.data.keyword.cloud_notm}} ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window}, and follow the prompts.

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


## Detaching a LogDNA agent from an Openshift Kubernetes cluster
{: #detach_agent_os}

To stop your Kubernetes cluster from sending logs to your {{site.data.keyword.la_full_notm}} instance, you must remove the LogDNA agent from your cluster. 

To stop your Kubernetes cluster from forwarding logs to your LogDNA instance, complete the following steps from the command line:

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

3. Log in to the cluster. Run one of the following commands and enter valid credentials.

    There are different methods to login to an OpenShift cluster. [Learn more](/docs/openshift?topic=openshift-access_cluster#access_automation).

    For example, you can create an {{site.data.keyword.cloud_notm}} IAM API key, and then use the API key to log in to an OpenShift cluster. 

    Create an {{site.data.keyword.cloud_notm}} API key.<p class="important">Save your API key in a secure location. You cannot retrieve the API key again. If you want to export the output to a file on your local machine, include the `--file <path>/<file_name>` flag.</p>

    ```
    ibmcloud iam api-key-create <name>
    ```
    {: pre}

    Then, use the API key to login:

    ```
    oc login -u apikey -p <API_key>
    ```
    {: pre}

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






