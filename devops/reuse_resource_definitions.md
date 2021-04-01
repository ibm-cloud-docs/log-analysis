---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, config agent

subcollection: log-analysis

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

# Reusing definitions of logging resources
{: #reuse_resource_definitions}

To avoid recreating definitions of views, boards, parsing templates, and exclusion rules, you can export these resources from a {{site.data.keyword.la_full_notm}} instance as a JSON file. Then, you can import the definitions into other logging instances.
{:shortdesc}



## Export the configuration of resources in a logging instance
{: #export_config_res}

Complete the following steps to export the configuration of your resources:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step2).

2. Select the **Settings** icon ![Configuration icon](../images/admin.png "Configuration icon"). Then select **Organization**. 

3. Select **Account config**.

4. In the *Export configuration* section, select the types of resources that you want to export.

    Notice that options are disabled if you do not have definitions of this type of resource in your logging instance. 

    You can export views and alerts, boards, parsing templates, and exclusion rules. 

5. Select **Export configuration** and save the file.


## Import the configuration of resources into a logging instance
{: #import_config}


Complete the following steps to import the configuration of your resources:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step2).

2. Select the **Settings** icon ![Configuration icon](../images/admin.png "Configuration icon"). Then select **Organization**. 

3. Select **Account config**.

4. In the *Import configuration* section, drop the JSON config file that inclides the resource definitions, or click to upload a file.

5. Choose **Add to existing views, alerts, and boards** or **Replace existing views, alerts, and boards**.

    When you choose the **add** option, you add assets to the exisiting ones.

    When you choose the **replace** option, you remove all assets, and new ones are created.

6. Select  **Import configuration**.


