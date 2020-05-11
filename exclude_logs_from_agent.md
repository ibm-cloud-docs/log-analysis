---

copyright:
  years:  2018, 2020
lastupdated: "2020-05-11"

keywords: LogDNA, IBM, Log Analysis, logging, config agent

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

# Excluding log files
{: #exclude_logs_from_agent}

Configure a LogDNA agent to exclude logs that you do not want to monitor through the LogDNA web UI. 
{:shortdesc}

* You can exclude files that are located in any of the paths that are defined through the **logdir** parameter in a Linux system or the **LOGDNA_EXCLUDE** variable in a Kubernetes cluster. 
* You can configure multiple files. You separate multiple files by using commas. 
* You can use glob patterns to define what you want to exclude. 
* You can configure specific files.



## Excluding log files for a standard Kubernetes cluster
{: #exclude_logs_from_agent_kube}


Complete the following steps to configure the agent so that only application logs are forwarded and cluster logs are excluded:

1. Open a terminal to log in to {{site.data.keyword.cloud_notm}}.

   ```
   ibmcloud login -a cloud.ibm.com
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

   When the download of the configuration files is finished, a command is displayed that you can use to set the path to the local Kubernetes configuration file as an environment variable. Copy and paste the command that is displayed in your terminal to set the `KUBECONFIG` environment variable.

5. Generate the configuration file of the agent by running the following command:

    ```
    kubectl get daemonset logdna-agent -o=yaml > prod-logdna-agent-ds.yaml
    ```
    {: codeblock}

6. Make changes. Add the section **LOGDNA_EXCLUDE**, and exclude all cluster logs. Add the following section to the yaml file:

    ```
    - name: LOGDNA_EXCLUDE
      value: /var/log/containers/*_kube-system_*,/var/log/containers/*ibm-observe_*,/var/log/containerd.log,/var/log/kubelet.log,/var/log/syslog,/var/log/ntpstats/*,/var/log/alb/*
    ```
    {: codeblock}

    You can also exclude logs by namespace. For example, to exclude all of the *kube-system* logs, enter:

    ```
    - name: LOGDNA_EXCLUDE
      value: /var/log/containers/*_kube-system_*
    ```
    {: codeblock}

    To exclude all non-container logs, that is, to exclude files as shown in the *All Apps* filter view, enter:

    ```
    - name: LOGDNA_EXCLUDE
      value: /var/log/!(containers)**
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

7. Apply the configuration changes. Run the following command:

    ```
    kubectl apply -f prod-logdna-agent-ds.yaml
    ```
    {: codeblock}

8. Get the logdna-agent pods. Run the following command:

    ```
    kubectl get pods
    ```
    {: codeblock}

9. Delete all the logdna pods that are listed in the previous step.

    ```
    kubectl delete pod PodName
    ```
    {: codeblock}

10. Verify that log entries are not showing in the LogDNA web UI.


