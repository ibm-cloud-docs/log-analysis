---

copyright:
  years: 2015, 2022

lastupdated: "2021-11-10"

keywords: 

subcollection: log-analysis

content-type: conref

---

{{site.data.keyword.attribute-definition-list}}

# Content references for log-analysis subcollection
{: #conref-log-analysis}

<!----------------------------------------------------->

## Install NXLog 
{: #nxlog_install}

Follow these steps to install NXLog.

You will need to run as a Windows Administrator for all command prompt or PowerShell steps.
{: important}

1. The [Chocolately package manager](https://chocolatey.org/){: external} is used to install NXLog.  Run one of the following if you do not have the package manager already installed.

    From a Windows command prompt (`cmd.exe`):

    ```text
    powershell -command "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
    ```
    {: pre}

    From a PowerShell prompt:

    ```text
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
    ```
    {: pre}


2. Run the following command in PowerShell to install NXLog Community Edition.

    ```text
    choco install -y nxlog
    ```
    {: pre}


## Configure NXLog
{: #nxlog_config}

1. Provision a syslog port for NXLog. 

    To get the required port value, do the following:

    1. Access the [{{site.data.keyword.la_full_notm}} UI.](/docs/log-analysis?topic=log-analysis-launch#launch_cloud_ui)
    2. Click the ![question mark icon](../images/question_mark.png "question mark icon") to access install instructions.
    3. Click **NXLog**.
    4. The syslog port you need to provision in Windows will be displayed.  For example, `syslog-a.us-south.logging.cloud.ibm.com:63980`.

    Then, in Windows, do the following:

    1. From the Control Panel access **System and Security** > **Windows Defender Firewall**.
    2. Click **Advanced settings**.
    3. Click **Inbound Rules**.
    4. Click **New Rule**.
    5. Select **Port**. 
    6. Click **Next**.
    7. For **Specific local ports:** enter `63980`.
    8. Click **Next**.
    9. Select **Allow the connection**.
    10. Click **Next**.
    11. Select where the rule should apply.
    12. Click **Next**.
    13. Name the rule.  For example, `syslog-a.us-south.logging.cloud.ibm.com:63980`.
    14. Click **Finish**.

2. Create your `nxlog.conf` file.

    1. Get the provided `nxlog.conf` file:

        1. Access the [{{site.data.keyword.la_full_notm}} UI.](/docs/log-analysis?topic=log-analysis-launch#launch_cloud_ui)
        2. Click the ![question mark icon](../images/question_mark.png "question mark icon") to access install instructions.
        3. Click **NXLog**.
        4. Click **Download the file** to download a copy of the provided `nxlog.conf` file.

    2. Customize the `nxlog.conf` to meet your needs.

       * The `<Input eventlog>` section specifies the logging channels to be captured.  To enable a logging channel, uncomment the desired lines.  To disable a logging channel, comment out those lines.

       * `LOGFOLDER` specifies the folder to stream logs from.  Check that the `File '%LOGFOLDER%\\*.log'` value is correct for your system as well.

       * Input, processor, and output channels are connected in the `<Route>` block.  Comment out this block to remove the route and disable logging from this channel.  Add new input modules with unique names to enable logging from new sources.

    3. Copy the `nxlog.conf` file as `<NXLOGDIR>\conf\nxlog.conf` where `<NXLOGDIR>` is the directory where you installed NXLog.  For example, `C:\Program Files (x86)\nxlog\` 

3. Download the LogDNA SSL Certificate Authority file.  This can be done in one of the following ways.

   * Run the following PowerShell script where `<NXLOGDIR>` is the directory where you installed NXLog.

      ```text
      $url = "https://assets.us-south.logging.cloud.ibm.com/rootca/ld-root-ca.crt"
      $output = "<NXLOGDIR>\cert\ca.pem"
      (New-Object System.Net.WebClient).DownloadFile($url, $output) 
      ```
      {: pre}

   * Use the link in the installation information to download and install the Root CA Certificate.

        1. Access the [{{site.data.keyword.la_full_notm}} UI.](/docs/log-analysis?topic=log-analysis-launch#launch_cloud_ui)
        2. Click the ![question mark icon](../images/question_mark.png "question mark icon") to access install instructions.
        3. Click **NXLog**.
        4. Click **Download Root CA Certificate** to download a copy of the certificate.  
        5. Copy the certificate to `<NXLOGDIR>\cert\ca.pem`, where `<NXLOGDIR>` is directory nxlog is installed.

<!----------------------------------------------------->

## Run NXLog
{: #nxlog_run}

Run the following in PowerShell from the directory where you installed NXLog.

```text
.\nxlog.exe
```
{: pre}

Run the following in PowerShell from the directory where you installed NXLog to stop the service.

```text
.\nxlog.exe --stop
```
{: pre}

<!----------------------------------------------------->

## Before you begin
{: #windows_prereqs}

Before you begin, make sure you have an {{site.data.keyword.la_full_notm}} instance configured.

### Make sure you have an ID with the proper permissions
{: #windows_id}

Use a user ID that is a member or an owner of an {{site.data.keyword.cloud_notm}} account. To get an {{site.data.keyword.cloud_notm}} user ID, go to: [Registration](https://cloud.ibm.com/login){: external}.

[Your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources](/docs/log-analysis?topic=log-analysis-work_iam). For example, to work in the US-south region and in the default resource group, you need the following permissions: 

| Resource                             | Scope of the access policy | Role    | Region    | Information                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Resource group **Default**           |  Resource group            | Viewer  | us-south  | This policy is required to allow the user to see service instances in the Default resource group.    |
| {{site.data.keyword.la_full_notm}} service |  Resource group      | Editor  | us-south  | This policy is required to allow the user to provision and administer the {{site.data.keyword.la_full_notm}} service in the Default resource group.   |
{: caption="Table 1. List of IAM policies" caption-side="top"} 

### Provision an {{site.data.keyword.la_full_notm}} instance
{: #windows_provision_la}

To provision a service instance of {{site.data.keyword.la_full_notm}} through the {{site.data.keyword.cloud_notm}} console, see [Provisioning an instance](/docs/log-analysis?topic=log-analysis-provision).



