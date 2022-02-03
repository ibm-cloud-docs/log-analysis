---

copyright:
  years:  2018, 2022
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, config agent

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Grouping data by using tags
{: #adding_tags}

Configure a logging agent to associate tags to all log records that it collects so that you can identify the agent's data quicker in the logging UI.
{: shortdesc}

* You can define multiple tags per logging agent. 
* You separate tags by using commas. 
* The maximum number of characters that you can set to define multiple tags is 80 characters.
* You can view the tags per log record.
* You can filter data by using one or more tags through the *All Tags* menu in the logging UI.


## Adding tags to logs from a Kubernetes cluster
{: #adding_tags_kube}


Complete the following steps to add tags to a cluster:

1. Set up the cluster environment. Run the following commands:

    1. Get the command to set the environment variable and download the Kubernetes configuration files.

       ```text
       ibmcloud ks cluster config --cluster <cluster_name_or_ID>
       ```
       {: codeblock}

       When the download of the configuration files is finished, a command is displayed that you can use to set the path to the local Kubernetes configuration file as an environment variable.

    2. Copy and paste the command that is displayed in your terminal to set the KUBECONFIG environment variable.

2. Check the update strategy of the DaemonSet and choose whether to use *kubectl apply* or *kubectl edit* to modify the configuration file for the agent.

    To check the update strategy, run the following command:

    ```text
    kubectl get ds/logdna-agent -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'
    ```
    {: pre}

    If the update strategy is set to *OnDelete* or if you have the configuration file that is managed through a version control system, update your local configuration file and apply changes to the logging agent by using *kubectl apply*.

    If the update strategy is set to *RollingUpdate*, you can update and apply changes to the logging agent by using *kubectl edit*.

3. Edit the `logdna-agent-configmap.yaml` file.

    Update the configuration file by modifying the local copy. **Note:** You can also generate the configuration file of the agent by running the following command:

    ```text
    kubectl get daemonset logdna-agent -o=yaml > prod-logdna-agent-ds.yaml
    ```
    {: codeblock}

    Alternatively, update the configuration file by using *kubectl edit*.

    ```text
    kubectl edit daemonset logdna-agent
    ```
    {: codeblock}

4. Add a **LOGDNA_TAGS** section.

    ```yaml
    - name: LOGDNA_TAGS
        value: tag1,tag2,tag3
    ```
    {: codeblock}

    For example, the following shows the tags in a sample configuration file:

    ```yaml
    apiVersion: extensions/v1beta1
    kind: DaemonSet
    metadata:
      name: logdna-agent
    spec:
      template:
        metadata:
          labels:
            app: logdna-agent
        spec:
          containers:
          - name: logdna-agent
            image: logdna/logdna-agent:latest
            imagePullPolicy: Always
            env:
            - name: LOGDNA_AGENT_KEY
              valueFrom:
                 secretKeyRef:
                  name: logdna-agent-key
                  key: logdna-agent-key
            - name: LDAPIHOST
              value: api.us-south.logging.cloud.ibm.com
            - name: LDLOGHOST
              value: logs.us-south.logging.cloud.ibm.com
            - name: LOGDNA_PLATFORM
              value: k8s
            - name: LOGDNA_TAGS
              value: tag1,tag2,tag3
    ```
    {: codeblock}

5. Apply configuration changes if you edit the file locally.

    ```text
    kubectl apply -f prod-logdna-agent-ds.yaml
    ```
    {: codeblock}

    **Note:** If you use *kubectl edit*, changes are applied automatically when you save your modifications.



## Adding tags to logs from Linux Ubuntu or Debian
{: #adding_tags_linux}

These instructions are for Ubuntu or Debian Linux systems but can be used for other Linux systems.
{: note}

Complete the following steps to add more tags to the logging agent:

1. Verify the logging agent is running.

2. Add one or more tags.

    ```text
    sudo logdna-agent -t TAG1,TAG2
    ```
    {: codeblock}


You can also edit the agent configuration file and add tags. The configuration file is located in */etc/logdna.conf*.

1. Edit the file.

    ```text
    sudo update-rc.d logdna-agent defaults
    ```
    {: codeblock}

2. Add tags.

3. Restart the logging agent.

    ```text
    sudo /etc/init.d/logdna-agent start
    ```
    {: codeblock}



