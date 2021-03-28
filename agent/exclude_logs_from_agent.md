---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: LogDNA, IBM, Log Analysis, logging, config agent

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

# Excluding log files
{: #exclude_logs_from_agent}

Configure a logging agent to exclude logs that you do not want to monitor through the logging UI. 
{:shortdesc}

* You can exclude files that are located in any of the paths that are defined through the **logdir** parameter in a Linux system or the **LOGDNA_EXCLUDE** variable in a Kubernetes cluster. 
* You can configure multiple files. You separate multiple files by using commas. 
* You can use glob patterns to define what you want to exclude. 
* You can configure specific files.



## Excluding log files for a standard Kubernetes cluster
{: #exclude_logs_from_agent_kube}


Complete the following steps to configure the agent so that only application logs are forwarded and cluster logs are excluded:

### Step 1. Set the context of the cluster
{: #exclude_logs_from_agent_kube_1}

Complete the following steps:

1. Open a terminal to log in to {{site.data.keyword.cloud_notm}}.

    ```
    ibmcloud login -a cloud.ibm.com --sso
    ```
    {: pre}

    Select the account where you provisioned the {{site.data.keyword.la_full_notm}} instance.

2. List the clusters to find out in which region and resource group the cluster is available.

    ```
    ibmcloud ks clusters
    ```
    {: pre}

3. Set the resource group and region.

    ```
    ibmcloud target -g RESOURCE_GROUP -r REGION
    ```
    {: pre}

    Where 
    
    `RESOURCE_GROUP` is the name of the resource group where the cluster is available, for example, `default`.
    
    `REGION` is the region where the cluster is available, for example, `us-south`.

4. Set the cluster where you want to configure logging as the context for this session.

    ```
    ibmcloud ks cluster config --cluster <cluster_name_or_ID>
    ```
    {: pre}

    Where `<cluster_name_or_ID>` is the name or the ID of the cluster.


### Step 2. Modify the logging agent YAML file
{: #exclude_logs_from_agent_kube_2}

Complete the following steps:

1. Generate the configuration file of the agent by running the following command:

    ```
    kubectl get daemonset logdna-agent -o=yaml > prod-logdna-agent-ds.yaml -n ibm-observe
    ```
    {: codeblock}

2. Make changes. Add the section **LOGDNA_EXCLUDE** to the YAML file. 


To exclude all cluster logs, you can enter:

```
- name: LOGDNA_EXCLUDE
  value: /var/log/containers/*_kube-system_*,/var/log/containers/*ibm-observe_*,/var/log/containerd.log,/var/log/kubelet.log,/var/log/syslog,/var/log/ntpstats/*,/var/log/alb/*
```
{: codeblock}

To exclude logs by namespace, for example, to exclude all of the *kube-system* logs, enter:

```
- name: LOGDNA_EXCLUDE
  value: /var/log/containers/*_kube-system_*
```
{: codeblock}

To exclude all non-container logs, that is, to exclude files as shown in the *All Apps* filter view, enter:

```
- name: LOGDNA_EXCLUDE
  value: /var/log/!(containers)/**
```
{: codeblock}

To exclude calico logs, enter:

```
- name: LOGDNA_EXCLUDE
  value: /var/log/containers/calico*
```
{: codeblock}

To exclude all of the _kube-system_ logs and all non-container logs, enter:

```
- name: LOGDNA_EXCLUDE
  value: /var/log/!(containers)**,/var/log/containers/*_kube-system_*
```
{: codeblock}


### Step 3. Apply the changes to the logging agent
{: #exclude_logs_from_agent_kube_3}

To apply the configuration changes, run the following command:

```
kubectl apply -f prod-logdna-agent-ds.yaml -n ibm-observe
```
{: codeblock}

### Step 4. Verify the changes
{: #exclude_logs_from_agent_kube_4}

Complete the following steps:

1. Get the logdna-agent pods and check that pods have restarted. Run the following command:

    ```
    kubectl get pods -n ibm-observe
    ```
    {: codeblock}

2. If pods are not restarted, delete all the logging pods.

    ```
    kubectl delete pod PodName -n ibm-observe
    ```
    {: codeblock}

3. [Launch the logging UI](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-launch), and verify that log entries are not showing in the logging UI.


