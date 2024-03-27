---

copyright:
  years:  2018, 2024
lastupdated: "2024-03-27"

keywords: IBM, Log Analysis, logging, agent image, container registry, icr

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Getting information about Kubernetes logging agent images
{: #log_analysis_agent_image}

Kubernetes logging agent images are public images that are available in {{site.data.keyword.cloud_notm}} through the [{{site.data.keyword.registrylong_notm}}](/docs/Registry?topic=Registry-getting-started) service.
{: shortdesc}

<!-- common deprecation notice -->
{{../_include-segments/deprecation_notice.md}}

You can access the images that are provided by {{site.data.keyword.IBM}} by using the command line.

Complete the following steps to get information about the logging agent images:

## Before you begin
{: #log_analysis_agent_image_prereqs}

Before you begin, complete the following tasks:

1. Ensure that the {{site.data.keyword.registrylong_notm}} CLI is installed, see [Installing the `container-registry` CLI plug-in](/docs/Registry?topic=Registry-registry_setup_cli_namespace#cli_namespace_registry_cli_install).

2. Log in to [{{site.data.keyword.cloud_notm}}](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login):

    ```text
    ibmcloud login
    ```
    {: pre}


## Step 1. Target the global registry
{: #log_analysis_agent_image_step1}

Run the following command:

```text
ibmcloud cr region-set global
```
{: pre}



## Step 2. List the logging agent images that are hosted in the global registry
{: #log_analysis_dna_agent_image_step2}

Run the following command:

```text
ibmcloud cr images --restrict ext/logdna-agent
```
{: codeblock}

The output of this command is the list of logging agent images. It includes information about the repository, `icr.io/ext/logdna-agent`, the image tag, the image digest, the image namespace, when the image was created, the image size, and the images security status.
