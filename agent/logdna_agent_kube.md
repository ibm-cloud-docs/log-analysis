---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Logging agent for Kubernetes
{: #agent_kube}

The Kubernetes logging agent collects and forwards logs to your {{site.data.keyword.la_full_notm}} instance. After you provision an {{site.data.keyword.la_full}} instance, you must configure a logging agent for each log source that you want to monitor.
{: shortdesc}

<!-- common deprecation notice -->
{{../_include-segments/deprecation_notice.md}}

The logging agent for Kubernetes automatically collects STDOUT and STDERR logs.

The logging agent tails for new log data, and looks for new files that are added to the logging directories that the agent monitors.

Before you begin, understand the [agent storage requirements.](/docs/log-analysis?topic=log-analysis-agent_storage)


## Logging agent images
{: #log_analysis_agent_image_kube}

Logging agent images for Kubernetes clusters are public images that are available in {{site.data.keyword.cloud_notm}} through the [{{site.data.keyword.registrylong_notm}}](/docs/Registry?topic=Registry-getting-started) service.

* The logging agent images are hosted in the {{site.data.keyword.registrylong_notm}} global repository `icr.io/ext/logdna-agent`.

* {{site.data.keyword.registrylong_notm}} provides a multi-tenant, highly available, scalable, and encrypted private image registry that is hosted and managed by {{site.data.keyword.IBM_notm}}.

* The {{site.data.keyword.registrylong_notm}} includes *Vulnerability Advisor* features that scan for potential security issues and vulnerabilities. Vulnerability Advisor checks for vulnerable packages in specific Docker base images, and known vulnerabilities in app configuration settings. When vulnerabilities are found, information about the vulnerability is provided. You can use this information to resolve security issues so that containers are not deployed from vulnerable images.

To get details about the logging agent images, see [Getting information about logging agent images](/docs/log-analysis?topic=log-analysis-log_analysis_agent_image).

## Resource Limits for agents deployed on Kubernetes
{: #kube_resource_limits}

The agent is deployed as a Kubernetes DaemonSet, creating one pod for each node selected. The agent collects logs of all the pods in the node. The resource requirements of the agent are in direct relation to the number of pods for each node and the amount of logs produced for each pod.

The agent requires at least 128 MB and no more than 512 MB of memory. It requires at least twenty millicpu (20m).

Different features can also increase resource utilization. When line exclusion, inclusion or redaction rules are specified, you can expect additional CPU consumption for each line and regex rule defined. When Kubernetes event logging is enabled (disabled by default), additional CPU usage will occur on the oldest agent pod.

Placing traffic shaping or CPU limits on the agent is not recommended to ensure data can be sent to the log ingestion service.



## Understanding image tags
{: #log_analysis_agent_image_kube_tags}

The tag that is associated to a logging image indicates whether the logging agent is automatically updated.
{: important}

A tag consists of multiple parts:

```text
X.Y.Z-<date>.[hash]
```
{: codeblock}

Where

- `X` represents the major version of an image.
- `Y` represents the minor version of an image.
- `Z` represents an incremental ID that determines the latest patched minor version.
- `<date>` represents the date that the image is built and available. The format is `YYYYMMDD`.
- `[hash]` represents the digest (manifest) of the container image. It is a unique `SHA-256` hash.


The following table outlines the tagging convention adopted and the agent update behavior:

| Tag | Logging agent auto-update enabled | More info |
|-----|----------------------------------|-----------|
| `X` |  YES  | The logging agent auto-updates when a new minor version releases.  \n The logging agent does not update to a new major version, as these updates may require configuration changes. |
| `X.Y`  | YES | The logging agent auto-updates when a new patch version is released. |
| `X.Y.Z` | YES | The logging agent auto-updates when a new vulnerability fix is released. The agent code does not change, but the included libraries have vulnerability fixes. |
| `X.Y.Z-<date>.[hash]` | NO | The logging agent never updates. If you use this tag, make sure you are watching for new agent releases that have vulnerability fixes. |
{: caption="Table 1. logging agent tags explained" caption-side="top"}

Depending on the tag that you use, you must consider upgrading the logging agent image in your DevOps maintenance plan, to resolve vulnerabilities and apply agent enhancements and agent bug fixes. For example:
- In a development environment, you can use a tag `X` and let auto-updates happen as new minor versions are released.
- In a staging environment, you might consider using a tag `X.Y` so auto-updates happen when a new patch is released.
- In a production environment, you can use the tag `X.Y.Z` so that auto-updates happen when a new vulnerability fix is released.
- For highly regulated environments, you should use the tag `X.Y.Z-<date>.[hash]`. Notice that you will have to check periodically for vulnerability fixes, patches, and minor version releases to keep the agent free of issues.

The logging agent auto-updates happen when you restart the logging pod. It is your responsibility to restart the pods periodically in order for agent updates to occur within the scope specified by the tag.
{: important}


## Stable and latest tags
{: #log_analysis_agent_image_tags_1}

[Deprecated]{: tag-deprecated}

For the `V1` and `V2` agent versions, you can also find the tags `stable` and `latest`. When you use any of these tags to configure the logging agent, notice that the logging agent will automatically update to the latest version of the agent.

- The tag `latest` refers to the most recent logging agent 1.Y image.
- The tag `stable` refers to the most recent logging agent 2.Y image.

The tags `stable` and `latest` were deprecated in June 2021.
{: important}



## Image versions
{: #log_analysis_agent_image_kube_versions}


The following table outlines the logging agent versions that are available to configure for a Kubernetes cluster:

| Kubernetes cluster             | logging agent V3             | logging agent V2      | logging agent V1     |
|--------------------------------|-----------------------------|-----------------------|----------------------------------------------|
| `Standard Kubernetes cluster`  | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) |
| `OpenShift Kubernetes cluster` | ![Checkmark icon](../images/checkmark-icon.svg) | ![Checkmark icon](../images/checkmark-icon.svg) | `Not available`                              |
{: caption="Table 2. logging agent versions for Kubernetes clusters" caption-side="top"}


The logging agent v2 is available only for Kubernetes 1.9+.
{: important}


## Choosing a version
{: #log_analysis_agent_image_kube_choose_version}

When you configure the logging agent, you can choose any of the following options:
- You can use the default YAML file that is provided. Choose by region and by type of account. The default configuration pulls the image `icr.io/ext/logdna-agent:stable`.
- You can use an existing YAML file and change the `image:tag` value in your existing YAML file to pull a specific image from the registry.

If you have a highly regulated environment, you can customize the YAML file. You can modify the YAML file so that it pulls from the {{site.data.keyword.registrylong_notm}} global repository `icr.io/ext/` the image that you specify, for example, `image: icr.io/ext/logdna-agent:X.Y.Z-<date>.[hash]`. Consider keeping a copy of the customized YAML file in a version control system.
{: important}


## Connecting a logging agent with a logging instance
{: #log_analysis_agent_image_kube_connect}

The logging agent is responsible for collecting and forwarding system-level, and file-based logs to your {{site.data.keyword.la_full_notm}} instance.

To connect your Kubernetes cluster to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install a *logging-agent* pod on each node of your cluster.

- The logging agent reads log files from the pod where it is installed, and forwards the log data to your logging instance.

- The logging agent collects STDOUT, STDERR, logs with the extension `*.log`, and extensionsless files that are stored in the `/var/log` directory of your pod. By default, logs are collected from all namespaces, including `kube-system`, and automatically forwarded to the {{site.data.keyword.la_full_notm}} service.

- To connect an agent to a standard Kubernetes cluster, see [Connecting a logging agent for a standard Kubernetes cluster](/docs/log-analysis?topic=log-analysis-config_agent_kube_cluster).

- To connect an agent to an OpenShift Kubernetes cluster, see [Connecting a logging agent for an OpenShift Kubernetes cluster](/docs/log-analysis?topic=log-analysis-config_agent_os_cluster).



## Detaching a logging agent from a cluster
{: #log_analysis_agent_detach}

To stop your Kubernetes cluster from sending logs to your {{site.data.keyword.la_full_notm}} instance, you must remove the logging agent from your cluster. [Learn more](/docs/log-analysis?topic=log-analysis-detach_agent).

| Platform                       | How to install and configure |
|--------------------------------|------------------------------|
| `Standard Kubernetes cluster`  | [Detaching a logging agent from a standard Kubernetes cluster](/docs/log-analysis?topic=log-analysis-detach_agent#detach_agent_kube) |
| `OpenShift Kubernetes cluster` | [Detaching a logging agent from an Openshift Kubernetes cluster](/docs/log-analysis?topic=log-analysis-detach_agent#detach_agent_os) |
{: caption="Table 10. Detaching a logging agent from a cluster" caption-side="top"}

## Running the agent as non-root
{: #log_analysis_agent_image_kube_non-root}

The default YAML files to configure a logging agent do not include running the agent as non-root.

To run the agent as non-root, see [Preparing the version 3 yaml file to run the agent as non-root](/docs/log-analysis?topic=log-analysis-upgrade_log_analysis_agent_3#upgrade_log_analysis_agent_3_step6).


## Configuration the agent
{: #kube_agent_config}

You can customize a logging agent by [configuring the environment variables](/docs/log-analysis?topic=log-analysis-log_analysis_agent_configure) for Kubernetes agents.
