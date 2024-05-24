---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, config agent

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Reusing definitions of logging resources
{: #reuse_resource_definitions}

To avoid recreating definitions of views, boards, parsing templates, and exclusion rules, you can export these resources from a {{site.data.keyword.la_full_notm}} instance as a JSON file. Then, you can import the definitions into other logging instances.
{: shortdesc}

<!-- common deprecation notice -->
{{../_include-segments/deprecation_notice.md}}

## Export the configuration of resources in a logging instance
{: #export_config_res}

Complete the following steps to export the configuration of your resources:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step2).

2. Click the **Settings** icon ![Configuration icon](../images/admin.png "Configuration icon"). Then select **Organization**.

3. Click **Export Config**.

4. In the *Export Configuration* section, select the types of resources that you want to export.

    Notice that options are disabled if you do not have definitions of this type of resource in your logging instance.

    You can export views and alerts, boards, parsing templates, and exclusion rules.

5. Select **Export** and save the file.

Do not edit the exported JSON file. If the JSON file is edited it will be corrupted and cannot be imported into another logging instance.
{: attention}

## Import the configuration of resources into a logging instance
{: #import_config}


Complete the following steps to import the configuration of your resources:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step2).

2. Click the **Settings** icon ![Configuration icon](../images/admin.png "Configuration icon"). Then select **Organization**.

3. Select **Import config**.

4. In the *Import Configuration* section, drop the JSON config file that inclides the resource definitions, or click to upload a file.

5. Choose **Add to existing configuration** or **Replace existing configuration**.

    When you choose the **add** option, you add assets to the exisiting ones.

    When you choose the **replace** option, you remove all assets, and new ones are created.

6. Select  **Import**.
