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


{{../_include-segments/deprecation_notice.md}}

## Export the configuration of resources in a logging instance
{: #export_config_res}
{: ui}

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
{: ui}


Complete the following steps to import the configuration of your resources:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step2).

2. Click the **Settings** icon ![Configuration icon](../images/admin.png "Configuration icon"). Then select **Organization**.

3. Select **Import config**.

4. In the *Import Configuration* section, drop the JSON config file that inclides the resource definitions, or click to upload a file.

5. Choose **Add to existing configuration** or **Replace existing configuration**.

    When you choose the **add** option, you add assets to the exisiting ones.

    When you choose the **replace** option, you remove all assets, and new ones are created.

6. Select  **Import**.

## Exporting configuration values using the API
{: #export_config_api}
{: api}

You can export configuration values using the API.

The following configuration settings can be obtained using the API:

| Configuration | Method |
| -------------- | -------------- |
| View | [`GET /v1/config/view/{viewId}`](https://cloud.ibm.com/apidocs/log-analysis#get-view){: external} |
| Preset alert | [`GET /v1/presetalert/{presetId}`](https://cloud.ibm.com/apidocs/log-analysis#get-alert){: external} |
| Category | [`GET /v1/config/categories/{type}/{id}`](https://cloud.ibm.com/apidocs/log-analysis#get-category){: external} |
{: caption="Table 1. GET API configuration methods" caption-side="bottom"}

The JSON returned by these methods can be used or modified to create new configurations or update existing configurations.


## Creating and updating configurations using exported API values
{: #create_config_api}
{: api}

You can use values obtained by [API calls](#export_config_api) to create new configurations in existing or new logging instances. The JSON can also be used to update existing configurations.

| Configuration | Method |
| -------------- | -------------- |
| View | [`POST /v1/config/view`](https://cloud.ibm.com/apidocs/log-analysis#create-view){: external} |
| Preset alert | [`POST /v1/presetalert`](https://cloud.ibm.com/apidocs/log-analysis#create-alert){: external} |
| Category | [`POST /v1/config/categories/{type}`](https://cloud.ibm.com/apidocs/log-analysis#create-category{: external} |
{: caption="Table 2. POST (create) API configuration methods" caption-side="bottom"}

| Configuration | Method |
| -------------- | -------------- |
| View | [`PUT /v1/config/view/{viewId}`](https://cloud.ibm.com/apidocs/log-analysis#update-view){: external} |
| Preset alert | [`PUT /v1/presetalert/{presetId}`](https://cloud.ibm.com/apidocs/log-analysis#update-preset){: external} |
| Category | [`PUT /v1/config/categories/{type}/{id}`](https://cloud.ibm.com/apidocs/log-analysis#update-category{: external} |
{: caption="Table 3. PUT (update) API configuration methods" caption-side="bottom"}
