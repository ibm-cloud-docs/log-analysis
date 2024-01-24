---

copyright:
  years:  2018, 2024
lastupdated: "2024-01-23"

keywords: IBM, Log Analysis, logging, web UI, browser

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Navigating to the web UI
{: #launch}

After you provision an instance of the {{site.data.keyword.la_full_notm}} service in the {{site.data.keyword.cloud_notm}}, and configure a logging agent for a log data source, you can view, monitor, and manage logs through the {{site.data.keyword.la_full_notm}} web UI.
{: shortdesc}


## Granting IAM policies to a user to launch the web UI
{: #launch_iam}

Users in your account need permissions to launch the logging web UI.

You must be an administrator of the {{site.data.keyword.la_full_notm}} service, an administrator of an {{site.data.keyword.la_full_notm}} instance, or have account IAM permissions to grant other users policies.
{: note}

The following table lists the minimum policies that a user must have to be able to launch the web UI, and view data:

| Service                              | Role                      | Permission granted       |
|--------------------------------------|---------------------------|---------------------|
| `{{site.data.keyword.la_full_notm}}` | Platform role: Viewer     | Allows the user to view the list of service instances in the Observability Logging dashboard. |
| `{{site.data.keyword.la_full_notm}}` | Service role: Reader      | Allows the user to launch the Web UI and view logs in the Web UI.    |
{: caption="Table 1. IAM policies" caption-side="top"}

For more information on how to configure these policies for a user, see [Granting permissions to a user to view logs](/docs/log-analysis?topic=log-analysis-work_iam#user_logdna).


## Launching the logging web UI through the {{site.data.keyword.cloud_notm}} UI
{: #launch_cloud_ui}

You launch the logging web UI within the context of an {{site.data.keyword.la_full_notm}} instance, from the {{site.data.keyword.cloud_notm}} UI.

Complete the following steps to launch the web UI:

1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

2. Click the **Menu** icon ![Menu icon](../icons/icon_hamburger.svg) &gt; **Observability**.

3. Click **Logging**.

    The list of instances that are available on {{site.data.keyword.cloud_notm}} is displayed.

4. Select one instance. Then, click **Open dashboard**.

The Web UI opens.

## Launching the logging web UI from a browser
{: #launch_browser}

You can launch the logging web UI directly from a browser.

Complete the following steps:

1. [Get the instance ID](/docs/log-analysis?topic=log-analysis-faq#faq_9).

2. Enter the following URL in a browser.

    ```text
    https://cloud.ibm.com/observe/embedded-view/logging/<INSTANCE_ID>?q=<QUERY>&hosts=<HOSTS>&apps=<APPS>&levels=<LEVELS>&tags=<TAGS>&t=<TIMEFRAME>
    ```
    {: codeblock}

    Where

    * `<INSTANCE_ID>` indicates the instance ID.

    * `<QUERY>` represents the search query that is applied for the view, for example, `q=table%3Amangle%20reason%3A%27refresh%20timer%27`.

        Use `%3A` to represent a colon (`:`).

        Use `%20` to represent a space.

        Use `%27` to represent a quote (`'`).

    * `<HOSTS>` represents the list of hosts for which data is included in the view. Multiple hosts are separated by commas, for example,  `hosts=logging-agent-trkq9,logging-agent-trkq7`.

    * `<APPS>` represents the list of apps for which data is included in the view. Multiple apps are separated by commas, for example, `apps=autoscaler,catalog-operator`.

    * `<LEVELS>` represents the list of levels for which data is included in the view. Multiple levels are separated by commas, for example, `levels=warn,debug`.

    * `<TAGS>` represents the list of tags for which data is included in the view. Multiple tags are separated by commas, for example, `tags=agent-v2,k8s`.

    * `<TIMEFRAME>` represents the timeframe that you apply to the data that is displayed through the view. For example, look at the following samples:

        When you specify a timeframe of `July 12`, the value is `t=July%2012`.

        When you specify a timeframe of `July 12, 2020`, the value is `t=July%2012%2C%202020`.

        When you specify a timeframe of `July 12, 2020 to July 15,2020`, the value is `t=July%2012%2C%202020%20to%20July%2015%2C2020`.


You might need to log in to {{site.data.keyword.cloud_notm}} to view the data if your token has expired or you are not logged in.
