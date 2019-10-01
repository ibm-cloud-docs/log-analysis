---

copyright:
  years:  2018, 2019
lastupdated: "2019-10-01"

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

# Excluding log files through the LogDNA agent
{: #config_agent_kube_exclude}

You can stop logs from being forwarded to your logging instance by modifying the LogDNA agent configuration file to exclude any files that you do not want the LogDNA agent to monitor. 
{:shortdesc}


* You can exclude files that are located in any of the paths that are defined through the **logdir** parameter. 
* To define the files, you can separate multiple files by using commas. You can use glob patterns. You can also configure specific files.

Complete the following steps to configure the agent so that only application logs are forwarded and cluster logs are excluded:

1. Set up the cluster environment. Run the following commands:

    First, get the command to set the environment variable and download the Kubernetes configuration files.

    ```
    ibmcloud ks cluster config --cluster <cluster_name_or_ID>
    ```
    {: codeblock}

    When the download of the configuration files is finished, a command is displayed that you can use to set the path to the local Kubernetes configuration file as an environment variable.

    Then, copy and paste the command that is displayed in your terminal to set the KUBECONFIG environment variable.

2. Generate the configuration file of the agent by running the following command:

    ```
    kubectl get daemonset logdna-agent -o=yaml > prod-logdna-agent-ds.yaml
    ```
    {: codeblock}

2. Make changes. Add the section **LOGDNA_EXCLUDE**, and exclude all cluster logs. Add the following section to the yaml file:

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
      value: /var/log/!(containers)*
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
      value: /var/log/!(containers)*,/var/log/containers/*_kube-system_*
    ```
    {: codeblock}

3. Apply the configuration changes. Run the following command:

    ```
    kubectl apply -f prod-logdna-agent-ds.yaml
    ```
    {: codeblock}

4. Get the logdna-agent pods. Run the following command:

    ```
    kubectl get pods
    ```
    {: codeblock}

5. Delete all the logdna pods that are listed in the previous step.

    ```
    kubectl delete pod PodName
    ```
    {: codeblock}

6. Verify that log entries are not showing in the LogDNA web UI.


