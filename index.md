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


# Getting started with IBM Log Analysis with LogDNA
{: #getting-started}

Use IBM Log Analysis with LogDNA to add log management capabilities to your {{site.data.keyword.Bluemix}} architecture. IBM Log Analysis with LogDNA is operated by LogDNA in partnership with {{site.data.keyword.IBM_notm}}.
{:shortdesc}


## [Step1] Before you begin
{: #prereqs}

* Read about IBM Log Analysis with LogDNA. For more information, see [About IBM Log Analysis with LogDNA](/docs/services/Log-Analysis-with-LogDNA/overview.html#about).
* Check the regions where the service is available. For more information, see [Regions](/docs/services/Log-Analysis-with-LogDNA/overview.html#regions).
* Get a user ID that is a member or an owner of an {{site.data.keyword.Bluemix_notm}} account. 

    To get an {{site.data.keyword.Bluemix_notm}} user ID, go to: [Registration ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://console.bluemix.net/registration/){:new_window}.

* Install the {{site.data.keyword.Bluemix_notm}} CLI. 

    For more information, see [Installing the {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli/index.html#overview).


## [Step2] Get started
{: #getstarted}

Choose a cloud resource for which you want to manage logs. Then, configure this log source so that you can monitor its logs through the IBM Log Analysis with LogDNA service.

The following table lists cloud resources that you can configure to store and manage logs by using the IBM Log Analysis with LogDNA service. Complete the tutorial for a resource to get started working with the {{site.data.keyword.loganalysisshort}} service:

<table>
  <caption>Tutorials to get started working with the IBM Log Analysis with LogDNA service </caption>
  <tr>
    <th>Resource</th>
    <th>Tutorial</th>
    <th>Cloud environment</th>
    <th>Scenario</th>
  </tr>
  <tr>
    <td>Containers running on the {{site.data.keyword.containershort}}</td>
    <td>[Managing Kubernetes cluster logs with IBM Log Analysis with LogDNA]()</td>
    <td>Public </td>
    <td>![{{site.data.keyword.containershort}} and the IBM Log Analysis with LogDNA](images/kube.png "{{site.data.keyword.containershort}} and the IBM Log Analysis with LogDNA")</td>
  </tr>
  <tr>
    <td>Linux Ubuntu Debian</td>
    <td>[Managing Linux Ubuntu logs with IBM Log Analysis with LogDNA]()</td>
    <td>Public</td>
    <td></td>
  </tr>
</table>

**Note:** The Cloud resource for which you want to manage logs and the IBM Log Analysis with LogDNA instance that you must use to manage those logs must run in the same account and in the same region.


## [Step3] Upgrade the plan
{: #upgrade}

Enable additional logging features.

Upgrade the IBM Log Analysis with LogDNA service plan to a paid plan to be able to [filter logs](https://docs.logdna.com/docs/filters), [search logs](https://docs.logdna.com/docs/search), [define views](https://docs.logdna.com/docs/views), and [configure alerts](https://docs.logdna.com/docs/alerts). For more information about IBM Log Analysis with LogDNA service plans, see [Pricing plans](/docs/services/Log-Analysis-with-LogDNA/overview.html#pricing_plans).

## [Step4] Manage user access with IAM: Identify the IAM policies that a user needs to work with the IBM Log Analysis with LogDNA service
{: #iam}

Learn more about IAM integration with the IBM Log Analysis with LogDNA service. For more information, see:

| User role in the {{site.data.keyword.Bluemix_notm}} | For more information                     |
|-----------------------------------------------------|------------------------------------------|
| Account owner                                       | [Granting permissions to a user to become an administrator of the service in the {{site.data.keyword.Bluemix_notm}} account](/docs/services/Log-Analysis-with-LogDNA/iam.html#admin_account) |
| Platform service administrator in the account       | [Granting permissions to a user to become an administrator of the service in the {{site.data.keyword.Bluemix_notm}} account](/docs/services/Log-Analysis-with-LogDNA/iam.html#admin_account) |
| Platform service administrator in a resource group  | [Granting permissions to a user to become an administrator of the service within a resource group](/docs/services/Log-Analysis-with-LogDNA/iam.html#admin_rg) |
| Platform Devops operator in the account           | [Granting permissions to a Devops user to manage the service in the {{site.data.keyword.Bluemix_notm}} account](/docs/services/Log-Analysis-with-LogDNA/iam.html#devops_account) |
| Platform Devops operator in a resource group        | [Granting permissions to a Devops user to manage the service within a resource group](/docs/services/Log-Analysis-with-LogDNA/iam.html#devops_rg) |
| Service administrator in LogDNA                     | [Granting permissions to manage logs and configure alerts in LogDNA](/docs/services/Log-Analysis-with-LogDNA/iam.html#admin_user_logdna)              |
| User / developer                                    | [Granting permissions to a user to view and manage logs in LogDNA](/docs/services/Log-Analysis-with-LogDNA/iam.html#user_logdna)               |
{: caption="Table 1. Cloud roles in the {{site.data.keyword.Bluemix_notm}}" caption-side="top"}


