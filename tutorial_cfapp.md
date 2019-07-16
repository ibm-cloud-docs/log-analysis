---

copyright:
  years: 2019
lastupdated: "2019-06-24"

keywords: LogDNA, IBM, Log Analysis, logging, cf, tutorial

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


# Monitoring logs from a CF app
{: #tutorial_cfapp}

List of {{site.data.keyword.cloud_notm}} services that send logs to {{site.data.keyword.la_full_notm}}:
{:shortdesc}




## Prereqs
{: #tutorial_iam_prereqs}

1. You need a user ID that is a member or an owner of an {{site.data.keyword.cloud_notm}} account. To get an {{site.data.keyword.cloud_notm}} user ID, go to: [Registration ![External link icon](../../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window}.

2. To work with the command-line, you must install the {{site.data.keyword.cloud_notm}} CLI. For more information, see [Installing the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli).

3. You need an {{site.data.keyword.at_full_notm}} instance provisioned in Frankfurt with a 7-day, 14-day, or 30-day plan. [Learn more](/docs/services/Activity-Tracker-with-LogDNA?topic=logdnaat-provision).

4. Your user ID must have assigned an IAM policy to work in the {{site.data.keyword.cloud_notm}} with {{site.data.keyword.at_full_notm}} service. [Learn more](/docs/iam?topic=iam-iammanidaccser#access_to_resources).

    ![Policy for working as a viewer with the {{site.data.keyword.at_short}} service](images/viewer_at_policy_in_rg.png "Policy for working as a viewer with the {{site.data.keyword.at_short}} service") 


## Step 1. Launch the web UI in Frankfurt
{: #tutorial_iam_step1}

1. [Log in to your {{site.data.keyword.cloud_notm}} account ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window}.

	After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} dashboard opens.

2. Click the **Menu** icon ![Menu icon](../icons/icon_hamburger.svg) &gt; **Observability**. 

3. Select **Activity Tracker**. 

    The list of instances that are available on {{site.data.keyword.cloud_notm}} is displayed.

4. Select the instance whose region is set to **Frankfurt**. Then, click **View LogDNA**. The Web UI opens.




    A logDNA instance
    You need to configure this LogDNA instance for platform service logs: https://cloud.ibm.com/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-config_svc_logs
    Apps in the same account that are actually sending logs. They will show up automatically.



