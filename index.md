---

copyright:
  years: 2018
lastupdated: "2018-10-15"

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

## Before you begin
{: #prereqs}

Choose a region. Currently, the service is only availab le in the **us-south**, therefore, you will be working in the US-South region. 

The Cloud resource and the IBM Log Analysis with LogDNA instance must be running in the same account, and in the same region.

Read about IBM Log Analysis with LogDNA. For more information, see [About LogDNA](/docs/services/Log-Analysis-with-LogDNA/overview.html#about).

You must have a user ID that is a member or an owner of an {{site.data.keyword.Bluemix_notm}} account. To get an {{site.data.keyword.Bluemix_notm}} user ID, go to: [Registration ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://console.bluemix.net/registration/){:new_window}.

Install the {{site.data.keyword.Bluemix_notm}} CLI. For more information, see [Installing the {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli/index.html#overview).


## Step1: Choose a cloud resource for which you want to see logs
{: #step1}

To view and manage logs in the {{site.data.keyword.Bluemix_notm}}, the resource needs to be configured to send logs to LogDNA by using the IBM Log Analysis with LogDNA.

The following table lists cloud resources that you can configure to store and manage logs by using the IBM Log Analysis with LogDNA. Complete the tutorial for a resource to get started working with the {{site.data.keyword.loganalysisshort}} service:

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
    <td>![{{site.data.keyword.containershort}} and the IBM Log Analysis with LogDNA](images/components.png "{{site.data.keyword.containershort}} and the IBM Log Analysis with LogDNA")</td>
  </tr>
  <tr>
    <td>Linux Ubuntu Debian</td>
    <td>[Managing Linux Ubuntu logs with IBM Log Analysis with LogDNA]()</td>
    <td>Public</td>
    <td></td>
  </tr>
</table>

## Step2: Identify the IAM policies that you need for different types of users
{: #step2}

For account administrators

For service administrators

For service operators

For viewers

## Next steps
{: #next_steps}

Upgrade the IBM Log Analysis with LogDNA service plan to a paid plan to be able to [filter logs](https://docs.logdna.com/docs/filters), [search logs](https://docs.logdna.com/docs/search), [define views](https://docs.logdna.com/docs/views), and [configure alerts](https://docs.logdna.com/docs/alerts).

For more information about IBM Log Analysis with LogDNA service plans, see [Pricing plans](/docs/services/Log-Analysis-with-LogDNA/overview.html#pricing_plans).
