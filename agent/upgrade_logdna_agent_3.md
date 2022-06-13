---

copyright:
  years:  2021, 2022
lastupdated: "2021-07-30"

keywords: IBM, Log Analysis, logging, update logging agent

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Upgrading from logging agent version 2 to logging agent version 3
{: #upgrade_log_analysis_agent_3}

If your Kubernetes cluster version is 1.9+ or Red Hat OpenShift 4.5+, you can upgrade the logging agent to version 3 and run the agent as non-root.
{: shortdesc}

Version 3 of the logging agent includes a number of features and enhancements, depending on the release level, including:

* Running as a non-root user.
* Configuring how existing files are handled on startup.  For example, whether they are read from the beginning or end of the file.
* The ability to monitor `journald` log files.
* Logging Kubernetes events.
* Enhancement of log file metadata with Kubernetes labels.
* Enhanced log inclusion and exclusion rules using regex patterns.
* Redaction of log lines using regex patterns.

When you upgrade the version of the agent, some logs may not be collected or duplicated depending on the period of time that you take to delete the current logging agent and deploy a new version of the logging agent in the cluster.
{: important}

Complete the following steps from the command line to upgrade the logging agent version that is deployed in your Kubernetes cluster:


## Step 1. Determine the latest available version of the agent
{: #upgrade_log_analysis_agent_3_step1}

To see all the currently installed agent versions, run the following commands:

```text
ibmcloud cr login
ibmcloud cr region-set global
ibmcloud cr images --restrict ext/logdna-agent
```
{: codeblock}

Make note of the image you want to update.  The image will be named similar to `3.2.0-20210629.b52135aba711`.  You will need this information for [Step 6](#upgrade_log_analysis_agent_3_step6).

Do not use the `latest` or `stable` versions.
{: note}

The [LogDNA release notes](https://logdna.zendesk.com/hc/en-us/categories/360001626492-Release-Notes.htm){: external} lists all LogDNA enhancements and fixes, including enhancements and fixes to the LogDNA Agent.

## Step 2. Set the cluster context
{: #upgrade_log_analysis_agent_3_step2}

1. Open a terminal to log in to {{site.data.keyword.cloud_notm}}.

   ```text
   ibmcloud login -a cloud.ibm.com
   ```
   {: pre}

2. List the clusters to find out in which region and resource group the cluster is available.

    ```text
    ibmcloud ks clusters
    ```
    {: pre}

3. Set the resource group and region.

    ```text
    ibmcloud target -g RESOURCE_GROUP -r REGION
    ```
    {: pre}

    Where 
    
    `RESOURCE_GROUP` is the name of the resource group where the cluster is available, for example, `default`.
    
    `REGION` is the region where the cluster is available, for example, `us-south`.

4. Set the cluster where you want to configure logging as the context for this session.

   ```text
   ibmcloud ks cluster config --cluster <cluster_name_or_ID>
   ```
   {: pre}


## Step 3. Backup the YAML file of the logging agent that is deployed in the cluster
{: #upgrade_log_analysis_agent_3_step3}

Run the following command to backup the YAML file of the logging agent that is currently deployed in your cluster:

```text
kubectl get ds logdna-agent -o yaml --namespace=<namespace> > logdna-agent-<clusterName>-<date>.yaml
```
{: pre}

Where

* `clusterName` is the name of your cluster
* `date` is the current date
* `namespace` is the namespace where you deployed your agent.  This is normally `ibm-observe`.


## Step 4. Create the namespace ibm-observe
{: #upgrade_log_analysis_agent_3_step4}

This step is only required if you installed the prior logging agent in a namespace that is different from `ibm-observe`.
{: note}

To check if the namespace exists, run the following command:

```text
kubectl get namespaces
```
{: pre}

Verify the `ibm-observe` namespace is active.

If you need to create the namespace, run the following command:

```text
kubectl create namespace ibm-observe
```
{: pre}


## Step 5. Delete the logging agent version 2
{: #upgrade_log_analysis_agent_3_step5}

If you are running the logging agent 2.0 or earlier, do the following:

1. Delete the old agent by running the following command:

   ```text
   kubectl delete daemonset.apps/logdna-agent
   ```
   {: pre}

2. Delete the secret in the default namespace by running the following command:

   ```text
   kubectl delete secret logdna-agent-key
   ```
   {: pre}

   Make sure you change to the default context before running this command.
   {: important}

If you are running the logging agent 2.1 or later, delete the old agent by running the following command:

```text
kubectl delete -f <YOUR_FILE_NAME>
```
{: pre}

Where `YOUR_FILE_NAME` is the name of the `yaml` file you used to deploy the old agent.  This is the file you obtained in [Step 3](# upgrade_log_analysis_agent_3_step3).


## Step 6. Preparing the version 3 yaml file to run the agent as non-root
{: #upgrade_log_analysis_agent_3_step6}

When you deploy a logging agent version 3 by using the yaml that is provided, you configure the agent with the feature `stateful lookback` enabled. This feature helps avoid log loss or duplication of data when the agent restarts. Stateful lookback requires the logging agent to run as root.

If you run in a secured environment or a highly regulated environment, the logging agent should run as non-root. To do this, you must edit the yaml you must edit the yaml file that is provided. Running as non-root requires additional configuration on the init container.

Complete the following steps to modify the yaml so that the logging agent runs as non-root:


1. Download the new version 3 `yaml` file.  Starting with version 3, `yaml` files are stored in a version-specific directory.  

    For Kubernetes clusters, get the `yaml` file from the following location: 

    Public endpoint: `https://assets.<REGION>.logging.cloud.ibm.com/clients/logdna-agent/<VERSION>/agent-resources.yaml` 

    Private endpoint: `https://assets.<REGION>.logging.cloud.ibm.com/clients/logdna-agent/<VERSION>/agent-resources-private.yaml`

    For OpenShift clusters, get the `yaml` file from the following location:

    Public endpoint: `https://assets.<REGION>.logging.cloud.ibm.com/clients/logdna-agent/<VERSION>/agent-resources-openshift.yaml` 

    Private endpoint: `https://assets.<REGION>.logging.cloud.ibm.com/clients/logdna-agent/<VERSION>/agent-resources-openshift-private.yaml`

    Where

    `<REGION>` indicates the region where the logging instance is available. For more information about regions, see [Locations](/docs/log-analysis?topic=log-analysis-regions).

    `<VERSION>` indicates the version of the agent that you want to deploy. For more information on versions, see [Getting information about Kubernetes logging agent images](/docs/log-analysis?topic=log-analysis-log_analysis_agent_image).

    For example:

    ```text
    wget https://assets.us-south.logging.cloud.ibm.com/clients/logdna-agent/3.2.0/agent-resources-private.yaml -o agent-resources-private.yaml
    ```
    {: pre}

    You cannot use a version 1 or 2 `yaml` file.  If you do, the agent will not run and you will get the following error in the agent log: `kc logs logdna-agent-5sxhb -n ibm-observe standard_init_linux.go:211: exec user process caused "operation not permitted"`.
    {: important}

2. Edit the downloaded `yaml` file and make the following changes:

   - Change the `image` tag to specify the image you obtained in [Step 1](#upgrade_log_analysis_agent_3_step1). For example:

      ```yaml
      image: icr.io/ext/logdna-agent:3.2.0-20210629.b52135aba711
      ```
      {: codeblock}

      Do not change any other instances of the version number in the `yaml` file.
      {: important}

   - In the `securityContext` section, add the following lines to run the agent as non-root:

      ```yaml
      securityContext:
            # Add these 2 lines to run as non-root
            runAsUser: 5000
            runAsGroup: 5000
      ```
      {: codeblock}

      This section needs to be in the `spec/containers/name` branch at the same indentation level as `capabilities`.
      {: important}

   - Add any custom tags from your version 2 `yaml` file to the `LOGDNA_TAGS`.

   - Save the updated `yaml` file as `logging-agent-resources-private.yaml`.


## Step 7. Deploy the logging agent version 3 in the cluster
{: #upgrade_log_analysis_agent_3_step7}

Create the secret in the ibm-observe namespace by running the following command with your ingestion key:

```text
kubectl create secret generic logdna-agent-key -n ibm-observe --from-literal=logdna-agent-key=<ingestion_key>
```
{: pre}
   
Install the agent by running the following command:

```text
kubectl create -f <logging-agent-resources yaml file>
```
{: pre}

For example:

```text
kubectl create -f logging-agent-resources-private.yaml
```
{: pre}


## Step 8. Verify that the logging agent is deployed successfully
{: #upgrade_log_analysis_agent_3_step8}

To verify that the logging agent is deployed successfully, run the following command:

```text
kubectl get pod -n ibm-observe
```
{: pre}

The deployment is successful when you see one or more logging pods.
* **The number of logging pods equals the number of worker nodes in your cluster.**
* All pods must be in a `Running` state.


