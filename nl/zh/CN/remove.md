---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging instance, delete

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

# 除去实例
{: #remove}

您可以通过 {{site.data.keyword.Bluemix}} UI 或命令行来除去 {{site.data.keyword.la_full_notm}} 服务的实例。
{:shortdesc}

从 {{site.data.keyword.cloud_notm}} 中除去实例时，请通过完成以下任务来执行清除操作：

1. 记下将度量值转发到要除去的 {{site.data.keyword.la_full_notm}} 实例的源的列表。必须从每个源中除去 LogDNA 代理程序。
2. 除去向用户授予的使用该实例的许可权。 

    如果是使用专用访问组来管理使用特定实例的访问权，那么必须除去这些访问组。

    如果是使用访问组来管理对多个日志记录实例的访问权，那么必须除去对要除去的实例授予许可权的策略。
    
    如果向用户授予了个别策略，那么必须收集有权使用该实例的用户的列表。然后，对于识别到的每个用户，必须除去与要删除的实例相关的策略。


接下来，在 {{site.data.keyword.cloud_notm}}“仪表板”中删除实例。


## 通过 {{site.data.keyword.cloud_notm}} UI 除去实例
{: #remove_ui}

要使用 {{site.data.keyword.cloud_notm}} UI 来除去 {{site.data.keyword.la_full_notm}} 的实例，请完成以下步骤：

1. 登录到 {{site.data.keyword.cloud_notm}} 帐户。

    单击 [{{site.data.keyword.cloud_notm}} 仪表板 ![外部链接图标](../../icons/launch-glyph.svg "外部链接图标")](https://cloud.ibm.com/login){:new_window} 以启动 {{site.data.keyword.cloud_notm}}“仪表板”。

	使用用户标识和密码登录后，{{site.data.keyword.cloud_notm}} UI 即会打开。

2. 转至“菜单”图标 ![“菜单”图标](../../icons/icon_hamburger.svg) &gt; **可观察性**以访问*可观察性*仪表板。

3. 选择**日志记录**。这将显示日志记录实例的列表。

4. 选择要删除的实例。

5. 从*操作*菜单中，选择**除去**。


## 通过 CLI 除去实例
{: #remove_cli}

要通过命令行除去 {{site.data.keyword.la_full_notm}} 的实例，请完成以下步骤：

1. [先决条件] 安装 {{site.data.keyword.cloud_notm}} CLI。

   有关更多信息，请参阅[安装 {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli)。

   如果 CLI 已安装，请继续执行下一步。

2. 在 {{site.data.keyword.cloud_notm}} 中登录到要在其中供应实例的区域。运行以下命令：[`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)。

3. 设置在其中供应实例的资源组。运行以下命令：[`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    缺省情况下，已设置 *default* 资源组。

4. 除去实例。运行 [`ibmcloud resource service-instance-delete`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_delete) 命令：

    ```
    ibmcloud resource service-instance-delete NAME 
    ```
    {: codeblock}

    其中，NAME 是实例的名称。

    例如，要除去实例，请运行以下命令：

    ```
    ibmcloud resource service-instance-delete logdna-instance-01
    ```
    {: codeblock}



