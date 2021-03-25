---

copyright:
  years:  2018, 2020
lastupdated: "2020-07-16"

keywords: LogDNA, IBM, Log Analysis, logging, web UI, browser

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

# Navigating to the web UI
{: #launch}

After you provision an instance of the {{site.data.keyword.la_full_notm}} service in the {{site.data.keyword.cloud_notm}}, and configure a logging agent for a log data source, you can view, monitor, and manage logs through the {{site.data.keyword.la_full_notm}} web UI.
{:shortdesc}


## Granting IAM policies to a user to launch the web UI
{: #launch_iam}

Users in your account need permissions to launch the logging UI.

You must be an administrator of the {{site.data.keyword.la_full_notm}} service, an administrator of an {{site.data.keyword.la_full_notm}} instance, or have account IAM permissions to grant other users policies.
{: note}

The following table lists the minimum policies that a user must have to be able to launch the web UI, and view data:

| Service                              | Role                      | Permission granted       |
|--------------------------------------|---------------------------|---------------------|
| `{{site.data.keyword.la_full_notm}}` | Platform role: Viewer     | Allows the user to view the list of service instances in the Observability Logging dashboard. |
| `{{site.data.keyword.la_full_notm}}` | Service role: Reader      | Allows the user to launch the Web UI and view logs in the Web UI.    |
{: caption="Table 1. IAM policies" caption-side="top"} 

For more information on how to configure these policies for a user, see [Granting permissions to a user to view logs](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-work_iam#user_logdna).


## Launching the logging UI through the {{site.data.keyword.cloud_notm}} UI
{: #launch_cloud_ui}

You launch the logging UI within the context of an {{site.data.keyword.la_full_notm}} instance, from the {{site.data.keyword.cloud_notm}} UI. 

Complete the following steps to launch the web UI:

1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

2. Click the **Menu** icon ![Menu icon](../icons/icon_hamburger.svg) &gt; **Observability**. 

3. Select **Logging**. 

    The list of instances that are available on {{site.data.keyword.cloud_notm}} is displayed.

4. Select one instance. Then, click **View LogDNA**.

The Web UI opens.


## Launching the logging UI from a browser
{: #launch_browser}

You can launch the logging UI directly from a browser. 

Complete the following steps:

1. [Get the logging UI URL](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-get_logdna_web_url).

    For example, a logging UI looks like `https://app.eu-gb.logging.cloud.ibm.com/ext/ibm-sso/xxxxxxxxxx`.

2. Enter the dashboard URL in a browser and log in to {{site.data.keyword.cloud_notm}.

3. [Optional] You can also pass query parameters to refine the view that is displayed.

    ```
    https://<ENDPOINT>/ext/ibm-sso/LOGDNA_ID?q=<QUERY>&hosts=<HOSTS>&apps=<APPS>&levels=<LEVELS>&tags=<TAGS>&t=<TIMEFRAME>
    ```
    {: codeblock}

    Where

    * `<ENDPOINT>` represents the dashboard URL in the region where the instance is available. See [logging UI endpoints](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-endpoints#endpoints_logdna_ui).

    * `<QUERY>` represents the search query that is applied for the view, for example, `q=table%3Amangle%20reason%3A%27refresh%20timer%27`. 

        Use `%3A` to represent a colon (`:`).

        Use `%20` to represent a space.

        Use `%27` to represent a quote (`'`).

    * `<HOSTS>` represents the list of hosts for which data is included in the view. Multiple hosts are separated by commas, for example,  `hosts=logdna-agent-trkq9,logdna-agent-trkq7`.

    * `<APPS>` represents the list of apps for which data is included in the view. Multiple apps are separated by commas, for example, `apps=autoscaler,catalog-operator`.

    * `<LEVELS>` represents the list of levels for which data is included in the view. Multiple levels are separated by commas, for example, `levels=warn,debug`.

    * `<TAGS>` represents the list of tags for which data is included in the view. Multiple tags are separated by commas, for example, `tags=agent-v2,k8s`.

    * `<TIMEFRAME>` represents the timeframe that you apply to the data that is displayed through the view. For example, look at the following samples:
    
        When you specify a timeframe of `July 12`, the value is `t=July%2012`. 
        
        When you specify a timeframe of `July 12, 2020`, the value is `t=July%2012%2C%202020`. 

        When you specify a timeframe of `July 12, 2020 to July 15,2020`, the value is `t=July%2012%2C%202020%20to%20July%2015%2C2020`.






    

