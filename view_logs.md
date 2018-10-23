---

copyright:
  years: 2018
lastupdated: "2018-10-22"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}

# Viewing logs through the IBM Log Analysis with LogDNA Web UI
{: #view_logs}

After you provision an instance of the IBM Log Analysis with LogDNA service in the {{site.data.keyword.Bluemix}}, and configure a LogDNA agent for a log source, you can view, monitor, and manage log data through the IBM Log Analysis with LogDNA Web UI.
{:shortdesc}



## Grant IAM policies to a user to view logs
{: #iam}

The following table lists the minimum policies that a user must have to be able to launch the IBM Log Analysis with LogDNA Web UI, and view logs:

| Service                        | Role                      | Permission granted                                                                            | 
|--------------------------------|---------------------------|-----------------------------------------------------------------------------------------------|       
| `IBM Log Analysis with LogDNA` | Platform role: Viewer     | Allows the user to view the list of service instances in the Observability Logging dashboard. |
| `IBM Log Analysis with LogDNA` | Service role: Reader      | Allows the user to launch the Web UI and view logs in the Web UI.                             |
{: caption="Table 1. IAM policies" caption-side="top"} 

For more information on how to configire these policies for a user, see [Granting permissions to a user to view logs in LogDNA](/docs/services/Log-Analysis-with-LogDNA/iam.html#user_logdna).


## Launch the Web UI through the {{site.data.keyword.Bluemix_notm}} UI
{: #launch_web_ui}

To launch IBM the Log Analysis with LogDNA UI through the {{site.data.keyword.Bluemix_notm}} UI, complete the following steps:

1. Log in to your {{site.data.keyword.Bluemix_notm}} account.

    The {{site.data.keyword.Bluemix_notm}} dashboard can be found at: [http://bluemix.net ![External link icon](../../../icons/launch-glyph.svg "External link icon")](http://bluemix.net){:new_window}.

	After you log in with your user ID and password, the {{site.data.keyword.Bluemix_notm}} Dashboard opens.

2. In the navigation menu, select **Observability**. 

3. Select **Logging**. 

    The list of IBM Log Analysis with LogDNA instances that are available on {{site.data.keyword.Bluemix_notm}} is displayed.

4. Select one instance. Then, click **View LogDNA**.

The IBM Log Analysis with LogDNA Web UI opens and displays logs forwarded to that instance.


