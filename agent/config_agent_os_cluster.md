---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, config agent

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Managing a logging agent deployed in an OpenShift cluster
{: #config_agent_os_cluster}

The logging agent is responsible for collecting and forwarding logs to your {{site.data.keyword.la_full_notm}} instance. After you provision an instance of {{site.data.keyword.la_full}}, you must configure a logging agent for each log source that you want to monitor.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

To configure your Kubernetes cluster to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install a *logging-agent* pod on each node of your cluster. The logging agent reads log files from the pod where it is installed, and forwards the log data to your logging instance.



## Deploy the logging agent by using kubectl commands
{: #config_agent_os_kubectl}

Complete the following steps from the command line to configure your OpenShift cluster to forward logs to your logging instance by using the default YAML file:

You can use an existing YAML file if you are configuring a newer logging agent version. Change the `image` value in your existing YAML file to match the version you are configuring.
{: note}

### Prereq
{: #config_agent_oscluster_prereq}

To deploy the logging agent in a cluster, you must have a user ID that has the following IAM roles:
* **Viewer** platform role, and **Manager** service role to work with that cluster instance.
* **Viewer** permissions on the resource group where the cluster is available.

To configure the logging agent in the cluster, you need the following CLIs:
* The {{site.data.keyword.cloud_notm}} CLI to log in to the {{site.data.keyword.cloud_notm}} by using `ibmcloud` commands, and to manage the cluster by using `ibmcloud ks` commands. [Learn more](/docs/containers?topic=containers-cs_cli_install#cs_cli_install_steps).
* The Kubernetes CLI to manage the cluster by using `kubectl` commands. [Learn more](/docs/containers?topic=containers-cs_cli_install#kubectl).
* The Openshift CLI to login to the cluster from the command line and deploy the agent. [Learn more](/docs/openshift?topic=openshift-openshift-cli).



### Step 1. Set the cluster context and log in to the cluster
{: #config_agent_oscluster_step1}

Complete the following steps:

1. Open a terminal to log in to {{site.data.keyword.cloud_notm}}.

   ```text
   ibmcloud login -a cloud.ibm.com
   ```
   {: pre}

   Select the account where you provisioned the {{site.data.keyword.la_full_notm}} instance.

2. List the clusters to find out in which region and resource group the cluster is available.

    ```text
    ibmcloud oc clusters
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

4. Set the cluster context in your session.

    ```text
    ibmcloud oc cluster config --cluster <cluster_name_or_ID>
    ```
    {: pre}

    When the download of the configuration files is finished, a command is displayed that you can use to set the path to the local Kubernetes configuration file as an environment variable. Copy and paste the command that is displayed in your terminal to set the KUBECONFIG environment variable.

5. Log in to the cluster. Choose a method to login to an OpenShift cluster. [Learn more about the methods to login](/docs/openshift?topic=openshift-access_cluster#access_automation).


### Step 2. Store your logging ingestion key as a Kubernetes secret
{: #config_agent_os_cluster_step2}

You must create a Kubernetes secret to store your logging ingestion key for your service instance. The logging ingestion key is used to open a secure web socket to the logging ingestion server and to authenticate the logging agent with the {{site.data.keyword.la_full_notm}} service.

1. Create a project. A project is a namespace in a cluster.

    ```text
    oc adm new-project --node-selector='' ibm-observe
    ```
    {: pre}

    Set `--node-selector=''` to disable the default project-wide node selector in your namespace and avoid pod recreates on the nodes that got unselected by the merged node selector.

2. Create the service account **logging-agent** in the cluster namespace **ibm-observe**. A service account is in Openshift what a service ID is in {{site.data.keyword.cloud_notm}}. Run the following command:

    ```text
    oc create serviceaccount SERVICEACCOUNT_NAME -n PROJECT
    ```
    {: pre}

    Where

    `PROJECT` is the namespace where the logging pods run. Set this value to **ibm-observe**.

    `SERVICEACCOUNT_NAME` is the name of the service account that you use to deploy the logging agent. Set this value to **logging-agent**. Notice that if you leave the service account name blank, the default service account is used instead of the service account that you created.

    ```text
    oc create serviceaccount logging-agent -n ibm-observe
    ```
    {: pre}

3. Grant the serviceaccount access to the **Privileged SCC** so the service account has permissions to create priviledged logging pods. Run the following command:

    ```text
    oc adm policy add-scc-to-user privileged system:serviceaccount:PROJECT:SERVICEACCOUNT_NAME
    ```
    {: pre}

    Where

    `PROJECT` is the namespace where the logging pods run. Set this value to **ibm-observe**.

    `SERVICEACCOUNT_NAME` is the name of the service account that you use to deploy the logging agent. Set this value to **logging-agent**.

    ```text
    oc adm policy add-scc-to-user privileged system:serviceaccount:ibm-observe:logging-agent
    ```
    {: pre}

4. Add a secret. The secret sets the ingestion key that the logging agent uses to send logs.

    ```text
    oc create secret generic logdna-agent-key --from-literal=logdna-agent-key=INGESTION_KEY -n PROJECT
    ```
    {: pre}

    Where

    `PROJECT` is the namespace where the logging pods run. Set this value to **ibm-observe**.

    `INGESTION_KEY` is the ingestion key for the logging instance where you plan to forward and collect the cluster logs. To get the ingestion key, see [Get the ingestion key through the IBM Log Analysis with logging UI](/docs/log-analysis?topic=log-analysis-ingestion_key).


### Step 3. Enable virtual routing and forwarding (VRF)
{: #config_agent_os_cluster_step3}

This step is required if you plan to use private endpoints.

You must enable virtual routing and forwarding (VRF) and connectivity to service endpoints for your account. [Learn more](/docs/account?topic=account-vrf-service-endpoint)

### Step 4. Deploy the logging agent in the cluster
{: #config_agent_os_cluster_step4}

Create a Kubernetes daemonset to deploy the logging agent on every worker node of your Kubernetes cluster.

The logging agent collects the following logs:

- STDOUT and STDERR
- Logs with the extension `*.log`, and extensionsless files that are stored in the `/var/log` directory of your pod.

By default, logs are collected from all namespaces, including `kube-system`, and automatically forwarded to the {{site.data.keyword.la_full_notm}} service.


#### Logging agent V2 and V3
{: #config_agent_os_cluster_step4_vx}

The logging agent version 2 and version 3 are supported for Red Hat OpenShift (version 4.5 or later).
{: important}

To configure the logging agent by using `kubectl` commands, run the following command:

| Type of endpoint | Command |
|------------------|---------|
| Public endpoint  | `kubectl apply -f https://assets.<REGION>.logging.cloud.ibm.com/clients/logdna-agent/<VERSION>/agent-resources-openshift.yaml` |
| Private endpoint | `kubectl apply -f https://assets.<REGION>.logging.cloud.ibm.com/clients/logdna-agent/<VERSION>/agent-resources-openshift-private.yaml` |
{: caption="Commands by endpoint type" caption-side="top"}

Where

- `<REGION>` indicates the region where the logging instance is available. For more information about regions, see [Locations](/docs/log-analysis?topic=log-analysis-regions).
- `<VERSION>` indicates the version of the agent that you want to deploy. You must use a version that has a tag with the following format: `X.Y.Z`.

If you need to use a version that has a tag with any of the following formats: `X.Y.Z-<date>.[hash]`, `X`, or `X.Y`, you must download the agent yaml file and modify it. Replace the version for all entries `app.kubernetes.io/version` in the file with the one that you want to use. You must download the yaml file that has the format `X.Y.Z`. Then, after you make the version changes, you can run `kubectl apply -f <CUSTOM_YAML_FILE>` to deploy the agent.
{: important}

For more information about the agent tags, see [Understanding image tags](/docs/log-analysis?topic=log-analysis-log_analysis_agent#log_analysis_agent_image_kube_tags).

For more information about the versions that are available, see [Getting information about Kubernetes logging agent images](/docs/log-analysis?topic=log-analysis-log_analysis_agent_image).

For example, to configure an agent that sends data to a logging instance in Dallas, you must run the following command:

```text
kubectl apply -f https://assets.us-south.logging.cloud.ibm.com/clients/logdna-agent/2.2.0/agent-resources-openshift.yaml
```
{: screen}


#### Logging agent V1
{: #config_agent_os_cluster_step4_v1}

Choose one of the following commands to install and configure the logging agent version 1 by using `kubectl` commands::

| Location                  | Command (By using public endpoints)               |
|--------------------------|----------------------------------------------------|
| `Chennai (in-che)`       | `kubectl apply -f https://assets.in-che.logging.cloud.ibm.com/clients/logdna-agent-ds-os.yaml -n ibm-observe`       |
| `Tokyo (jp-tok)`         | `kubectl apply -f https://assets.jp-tok.logging.cloud.ibm.com/clients/logdna-agent-ds-os.yaml -n ibm-observe`       |
| `Sydney (au-syd)`        | `kubectl apply -f https://assets.au-syd.logging.cloud.ibm.com/clients/logdna-agent-ds-os.yaml -n ibm-observe`        |
| `Osaka (jp-osa)`         | `kubectl apply -f https://assets.jp-osa.logging.cloud.ibm.com/clients/logdna-agent-ds-os.yaml -n ibm-observe`        |
| `Frankfurt (eu-de)`      | `kubectl apply -f https://assets.eu-de.logging.cloud.ibm.com/clients/logdna-agent-ds-os.yaml -n ibm-observe`         |
| `London (eu-gb)`         | `kubectl apply -f https://assets.eu-gb.logging.cloud.ibm.com/clients/logdna-agent-ds-os.yaml -n ibm-observe`          |
| `Toronto (ca-tor)`       | `kubectl apply -f https://assets.ca-tor.logging.cloud.ibm.com/clients/logdna-agent-ds-os.yaml -n ibm-observe`       |
| `Dallas (us-south)`      | `kubectl apply -f https://assets.us-south.logging.cloud.ibm.com/clients/logdna-agent-ds-os.yaml -n ibm-observe`       |
| `Washington (us-east)`   | `kubectl apply -f https://assets.us-east.logging.cloud.ibm.com/clients/logdna-agent-ds-os.yaml -n ibm-observe`       |
{: caption="Commands by location when you use public endpoints" caption-side="top"}
{: #end-api-table-1}
{: tab-title="Command (By using public endpoints)"}
{: tab-group="agent"}
{: class="simple-tab-table"}
{: row-headers}

| Location                  | Command (By using private endpoints)               |
|--------------------------|----------------------------------------------------|
| `Chennai (in-che)`       | `kubectl apply -f https://assets.in-che.logging.cloud.ibm.com/clients/logdna-agent-ds-os-private.yaml -n ibm-observe`       |
| `Tokyo (jp-tok)`         | `kubectl apply -f https://assets.jp-tok.logging.cloud.ibm.com/clients/logdna-agent-ds-os-private.yaml -n ibm-observe`        |
| `Sydney (au-syd)`        | `kubectl apply -f https://assets.au-syd.logging.cloud.ibm.com/clients/logdna-agent-ds-os-private.yaml -n ibm-observe`       |
| `Osaka (jp-osa)`         | `kubectl apply -f https://assets.jp-osa.logging.cloud.ibm.com/clients/logdna-agent-ds-os-private.yaml -n ibm-observe`      |
| `Frankfurt (eu-de)`      | `kubectl apply -f https://assets.eu-de.logging.cloud.ibm.com/clients/logdna-agent-ds-os-private.yaml -n ibm-observe`          |
| `London (eu-gb)`         | `kubectl apply -f https://assets.eu-gb.logging.cloud.ibm.com/clients/logdna-agent-ds-os-private.yaml -n ibm-observe`       |
| `Toronto (ca-tor)`       | `kubectl apply -f https://assets.ca-tor.logging.cloud.ibm.com/clients/logdna-agent-ds-os-private.yaml -n ibm-observe`      |
| `Dallas (us-south)`      | `kubectl apply -f https://assets.us-south.logging.cloud.ibm.com/clients/logdna-agent-ds-os-private.yaml -n ibm-observe`      |
| `Washington (us-east)`   | `kubectl apply -f https://assets.us-east.logging.cloud.ibm.com/clients/logdna-agent-ds-os-private.yaml -n ibm-observe`      |
{: caption="Commands by location when you use private endpoints" caption-side="top"}
{: #end-api-table-2}
{: tab-title="Command (By using private endpoints)"}
{: tab-group="agent"}
{: class="simple-tab-table"}
{: row-headers}

### Step 5. Forward your API audit logs
{: #config_agent_os_cluster_step5}

Follow the [forwarding Kubernetes API audit logs steps](/docs/openshift?topic=openshift-health-audit#audit-api-server-la) to configure the system to collect and forward events from your Kubernetes API server to {{site.data.keyword.la_full}}.

### Step 6. Verify that the logging agent is deployed successfully
{: #config_agent_os_cluster_step6}

To verify that the logging agent is deployed successfully, run the following command:

1. Target the project where the logging agent is deployed.

    ```text
    oc project ibm-observe
    ```
    {: pre}

2. Verify that the pods on each node are in a **Running** status.

    ```text
    oc get pods -n PROJECT_NAME
    ```
    {: pre}

    For example, the following command lists all the pods in the namespace *ibm-observe*.

    ```text
    oc get pods -n ibm-observe
    ```
    {: pre}


The deployment is successful when you see one or more logging pods.
* **The number of logging pods equals the number of worker nodes in your cluster.**
* All pods must be in a `Running` state.
* *Stdout* and *stderr* are automatically collected and forwarded from all containers. Log data includes application logs and worker logs.
* By default, the logging agent pod that runs on a worker collects logs from all namespaces on that node.

After the agent is configured, you should start seeing logs from this cluster in the logging UI. If after a period of time you cannot see logs, check the agent logs.

To check the logs that are generated by a logging agent, run the following command:

```text
oc logs logdna-agent-<ID>
```
{: pre}

Where *ID* is the ID for a logging agent pod.

For example,

```text
oc logs logdna-agent-xxxkz
```
{: pre}


Next, launch the logging UI to verify that logs from the cluster are available through the UI. See [Navigating to the web UI](/docs/log-analysis?topic=log-analysis-launch) and [Viewing logs](/docs/log-analysis?topic=log-analysis-view_logs).





## Deploy the logging agent within the context of the cluster
{: #config_agent_os_ob}

When you deploy and connect a logging agent within the context of the cluster, consider the following information:
* You can launch the logging UI from the OpenShift cluster UI in {{site.data.keyword.cloud_notm}}.
* The view that opens displays logs for your cluster.
* The agent is deployed in the `ibm-observe` namespace.
* A tag that informs about the cluster name is associated to each log line as metadata.
* A tag that informs about the version of the agent is associated to each log line as metadata.
* The logging instance must be available in the same {{site.data.keyword.cloud_notm}} account where the cluster is provisioned.
* The logging instance can be in a different resource group and {{site.data.keyword.cloud_notm}} region than your cluster.


Before you can deploy the logging agent in a cluster, verify that you are assigned the following IAM roles:
* **Viewer** permissions on the resource group where the cluster is available.
* **Viewer** permissions on the resource group where the logging instance is available.
* **Viewer** platform role and **Writer** or **Manager** service role for the OpenShift service to configure the logging agent.
* **Viewer** platform role, and **Reader** service role for the {{site.data.keyword.la_full_notm}} instance to launch the logging UI, and analyze logs through the logging UI.

The minimum persmissions that a user must have to launch the logging UI from the cluster UI, and analyze cluster logs are the following:
* **Viewer** permissions on the resource group where the cluster is available.
* **Viewer** permissions on the resource group where the logging instance is available.
* **Viewer** platform role and **Reader** service role for the OpenShift service to see the cluster and open the cluster's UI.
* **Viewer** platform role, and **Reader** service role for the {{site.data.keyword.la_full_notm}} instance to launch the logging UI, and analyze logs through the logging UI.

### Deploy the logging agent from the OpenShift console
{: #config_agent_os_ob_ui}


Complete the following steps from the [OpenShift console](https://cloud.ibm.com/kubernetes/clusters?platformType=openshift){: external}:

1. Select the cluster for which you want to create a logging logging configuration.

2. On the cluster **Overview** page, in the *Logging* section, click **Connect**.

    The page `Connect an existing IBM Log Analysis with logging instance` opens.

3. Select the region where the logging instance is provisioned.

4. Select the {{site.data.keyword.la_full_notm}} instance that you want to use to analyze your logs.

5. If your account is VRF-enabled, check the box **Use private endpoint** to keep all network traffic to your service instance on the private network.

    Your cluster must be set up with a private service endpoint to use this option. To enable the private service endpoint, use the cluster Overview page.
    {: note}

    To check if your account is VRF-enabled, run the following command:

    ```text
    ibmcloud account show
    ```
    {: pre}

6. Click **Connect**.


### Deploy the logging agent by using ob commands
{: #config_agent_os_ob_cli}


To configure the logging agent in a cluster, complete the following steps:


1. [Pre-req] Install the OpenShift observability CLI plug-in (ibmcloud ob).

    ```text
    ibmcloud plugin install observe-service
    ```
   {: pre}

2. Set the cluster context.

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

3. Deploy the logging agent by using the `ob` CLI. Run the following command:

    ```text
    ibmcloud ob logging config create --cluster <cluster_name_or_ID> --instance <instance_name_or_ID> [--LogDNA-ingestion-key <Ingestion_Key>] [--private-endpoint]
    ```
    {: pre}

    Where

    * `<cluster_name_or_ID>` is the name or the ID of the cluster.

    * `<instance_name_or_ID>` is the name or the ID of the logging instance where you want to forward the cluster logs for analysis.

    * `<Ingestion_Key>` is the ingestion key that you want to use to connect the logging agent with the logging instance.

    * `[--private-endpoint]` is optional. Add this option to connect to your logging instance by using private service endpoints.
