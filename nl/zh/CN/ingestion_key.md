---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion key

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

# 使用摄入密钥
{: #ingestion_key}

摄入密钥是一种安全密钥，必须使用该密钥来配置 LogDNA 代理程序，并成功地将日志转发到 {{site.data.keyword.cloud_notm}} 中的 {{site.data.keyword.la_full_notm}} 实例。供应实例时，您会自动获得摄入密钥。或者，您还可以通过为实例创建服务标识来获取摄入密钥。
{:shortdesc}

**注：** 

* 要通过 {{site.data.keyword.la_full_notm}} Web UI 使用摄入密钥，您必须具有包含对 {{site.data.keyword.la_full_notm}} 服务的**查看者**平台角色和**管理者**服务角色的 IAM 策略。 
* 要通过 {{site.data.keyword.cloud_notm}} UI 使用摄入密钥，您必须具有包含对 {{site.data.keyword.la_full_notm}} 服务的**编辑者**平台角色和**管理者**服务角色的 IAM 策略。 


## 通过 {{site.data.keyword.cloud_notm}} UI 获取摄入密钥
{: #ibm_cloud_ui}

要使用 {{site.data.keyword.cloud_notm}} UI 来获取 {{site.data.keyword.la_full_notm}} 实例的摄入密钥，请完成以下步骤：

1. 登录到 {{site.data.keyword.cloud_notm}} 帐户。

    单击 [{{site.data.keyword.cloud_notm}} 仪表板 ![外部链接图标](../../icons/launch-glyph.svg "外部链接图标")](https://cloud.ibm.com/login){:new_window} 以启动 {{site.data.keyword.cloud_notm}}“仪表板”。

	使用用户标识和密码登录后，{{site.data.keyword.cloud_notm}} UI 即会打开。

2. 在导航菜单中，选择**可观察性**。 

3. 选择**日志记录**。这将打开 {{site.data.keyword.la_full_notm}} 仪表板。您可以查看 {{site.data.keyword.cloud_notm}} 上可用的日志记录实例的列表。

3. 确定要获取其摄入密钥的实例，然后单击**查看摄入密钥**。

4. 这将打开一个窗口，在其中可以单击**显示**以查看摄入密钥。


## 通过 {{site.data.keyword.la_full_notm}} Web UI 获取摄入密钥
{: #logdna_ui}

要使用 {{site.data.keyword.la_full_notm}} Web UI 来获取 {{site.data.keyword.la_full_notm}} 实例的摄入密钥，请完成以下步骤：

1. 启动 {{site.data.keyword.la_full_notm}} Web UI。有关更多信息，请参阅[启动 {{site.data.keyword.la_full_notm}} Web UI](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)。

2. 选择**配置**图标。然后，选择**组织**。 

3. 选择 **API 密钥**。

您可以看到已创建的摄入密钥。 

**注：**同一时间只有一个摄入密钥处于活动状态。 


## 通过 {{site.data.keyword.cloud_notm}} CLI 获取摄入密钥
{: #ibm_cloud_cli}

要通过命令行获取 {{site.data.keyword.la_full_notm}} 实例的摄入密钥，请完成以下步骤：

1. [先决条件] 安装 {{site.data.keyword.cloud_notm}} CLI。

   有关更多信息，请参阅[安装 {{site.data.keyword.cloud_notm}} CLI](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about)。

   如果 CLI 已安装，请继续执行下一步。

2. 在 {{site.data.keyword.cloud_notm}} 中登录到要运行实例的区域。运行以下命令：[`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)。

3. 设置要运行 {{site.data.keyword.la_full_notm}} 实例的资源组。运行带 `-g` 选项的以下命令：[`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)。

    缺省情况下，已设置 `default` 资源组。

4. 获取与 {{site.data.keyword.la_full_notm}} 实例关联的 API 密钥的名称。运行 [`ibmcloud resource service-keys`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_keys) 命令：

    ```
    ibmcloud resource service-keys
    ```
    {: codeblock}

    确定与实例关联的服务密钥。

5. 获取摄入密钥。运行 [`ibmcloud resource service-key`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_key) 命令：

    ```
    ibmcloud resource service-key APIKEY_NAME
    ```
    {: codeblock}

    其中，APIKEY_NAME 是 API 密钥的名称
 
    此命令的输出包含 **ingestion_key** 字段，其中含有实例的摄入密钥。


## 重置摄入密钥 
{: #reset}

如果摄入密钥泄露，或者您有用于在一定天数后更新摄入密钥的策略，那么可以生成新密钥并删除旧密钥。

要使用 {{site.data.keyword.la_full_notm}} Web UI 来更新 {{site.data.keyword.la_full_notm}} 实例的摄入密钥，请完成以下步骤：

1. 启动 {{site.data.keyword.la_full_notm}} Web UI。有关更多信息，请参阅[启动 {{site.data.keyword.la_full_notm}} Web UI](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)。

2. 选择**配置**图标。然后，选择**组织**。 

3. 选择 **API 密钥**。

    您可以看到已创建的摄入密钥。 

4. 选择**生成摄入密钥**。

    新的密钥会添加到列表中。

5. 删除旧的摄入密钥。单击**删除**。

**注：**重置摄入密钥后，必须更新已配置为将日志转发到此 {{site.data.keyword.la_full_notm}} 实例的任何日志源的摄入密钥。



