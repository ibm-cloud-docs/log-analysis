---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, web UI, browser

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

# 导航至 Web UI
{: #launch}

在 {{site.data.keyword.cloud_notm}} 中供应 {{site.data.keyword.la_full_notm}} 服务的实例，并为日志数据源配置了 LogDNA 代理程序后，可以通过 {{site.data.keyword.la_full_notm}} Web UI 来查看、监视和管理日志。
{:shortdesc}


## 向用户授予 IAM 策略以查看数据 
{: #step1}

**注：**您必须是 {{site.data.keyword.la_full_notm}} 服务的管理员、{{site.data.keyword.la_full_notm}} 实例的管理员，或者具有可向其他用户授予策略的帐户 IAM 许可权。

下表列出了用户必须拥有才能启动 Web UI 和查看数据的最低策略：

|服务|角色 |授予的许可权|
|--------------------------------------|---------------------------|---------------------|
| `{{site.data.keyword.la_full_notm}}` |平台角色：查看者|允许用户在“可观察性 - 日志记录”仪表板中查看服务实例的列表。|
| `{{site.data.keyword.la_full_notm}}` |服务角色：写入者|允许用户启动 Web UI，并在 Web UI 中查看日志。|
{: caption="表 1. IAM 策略" caption-side="top"} 

有关如何为用户配置这些策略的更多信息，请参阅[向用户授予查看日志的许可权](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna)。


## 通过 {{site.data.keyword.cloud_notm}} UI 启动 Web UI
{: #launch_step2}

在 {{site.data.keyword.la_full_notm}} 实例的上下文中，通过 {{site.data.keyword.cloud_notm}} UI 来启动 Web UI。 

要启动 Web UI，请完成以下步骤：

1. 登录到 {{site.data.keyword.cloud_notm}} 帐户。

    单击 [{{site.data.keyword.cloud_notm}} 仪表板 ![外部链接图标](../../icons/launch-glyph.svg "外部链接图标")](https://cloud.ibm.com/login){:new_window} 以启动 {{site.data.keyword.cloud_notm}}“仪表板”。

	使用用户标识和密码登录后，{{site.data.keyword.cloud_notm}}“仪表板”即会打开。

2. 在导航菜单中，选择**可观察性**。 

3. 选择**日志记录**。 

    这将显示 {{site.data.keyword.cloud_notm}} 上可用的实例的列表。

4. 选择一个实例。然后，单击**查看 LogDNA**。

这将打开 Web UI。


## 从 {{site.data.keyword.cloud_notm}} 获取 Web UI URL
{: #launch_get}

要获取 Web UI URL，请通过终端完成以下步骤：

1. 设置在其中供应 {{site.data.keyword.la_full_notm}} 实例的资源组。

    ```
    export logdna_rg_name=<Resource_Group_Name_Where_LogDNA_Instance_Is_Created>
    ```
    {: codeblock}

2. 设置 {{site.data.keyword.la_full_notm}} 实例名称。

    ```
    export logdna_instance_name=<Your_LogDNA_Instance_Name>
    ```
    {: codeblock}

3. 设置端点。

    ```
    export rc_endpoint=resource-controller.cloud.ibm.com
    ```
    {: codeblock}

4. 设置 IAM 令牌。

    ```
    export iam_token=$(ibmcloud iam oauth-tokens | grep IAM | grep -oP  "eyJ.*")
    ```
    {: codeblock}

    **注：**如果是在 MacOS 终端上工作，那么该命令如下所示：`export iam_token=$(ic iam oauth-tokens | grep IAM | grep -o  "eyJ.*")`

5. 设置资源组标识。

    ```
    export resource_group_id=$(ibmcloud resource groups | grep "^$logdna_rg_name" | awk '{print $2}')
    ```
    {: codeblock}

6. 在变量中设置 Web UI URL。

    ```
    export dashboard_url=$(curl -H "Accept: application/json" -H "Authorization: Bearer $iam_token" "https://$rc_endpoint/v1/resource_instances?resource_group_id=$resource_group_id&type=service_instance" | jq ".resources[] | select(.name==\"$logdna_instance_name\") | .dashboard_url")
    ```
    {: codeblock}

7. 获取 Web UI URL。

    ```
    echo $dashboard_url
    ```
    {: codeblock}

    

