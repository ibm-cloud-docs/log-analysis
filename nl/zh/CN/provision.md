---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging instance, provision

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

# 供应实例
{: #provision}

必须先在 {{site.data.keyword.cloud_notm}} 中供应服务的实例，然后才能使用 {{site.data.keyword.la_full_notm}} 来监视和管理日志数据。
{:shortdesc}

要在公共云区域中供应 {{site.data.keyword.la_full_notm}} 实例，必须选择与该实例关联的服务套餐、在其中收集日志的区域以及用于确定日志保留期的套餐。您可以选择 7 天、14 天或 30 天保留期。

或者，{{site.data.keyword.la_full_notm}} 提供了`轻量`套餐，可用于在日志通过系统时查看日志。您可以使用日志跟踪来查看日志。还可以设计过滤器来准备升级为更长保留期的套餐。此套餐的保留期为 0 天。


## 通过“可观察性”仪表板供应实例
{: #provision_ui}

要通过 {{site.data.keyword.cloud_notm}} 中的“可观察性”仪表板来供应实例，请完成以下步骤：

1. 登录到 {{site.data.keyword.cloud_notm}} 帐户。

    {{site.data.keyword.cloud_notm}} 仪表板可以在 [{{site.data.keyword.cloud_notm}} 仪表板 ![外部链接图标](../../icons/launch-glyph.svg "外部链接图标")](https://cloud.ibm.com/login){:new_window} 中找到。

	使用用户标识和密码登录后，{{site.data.keyword.cloud_notm}} UI 即会打开。

2. 转至“菜单”图标 ![“菜单”图标](../../icons/icon_hamburger.svg)。然后，选择**可观察性**以访问*可观察性*仪表板。

3. 选择**日志记录**，然后单击**创建实例**。 

4. 输入服务实例的名称。

5. 选择资源组。 

    缺省情况下，已设置 **Default** 资源组。

    **注：**如果无法选择资源组，请检查您是否具有对要在其中供应实例的资源组的编辑许可权。

6. 选择`轻量`服务套餐。 

    缺省情况下，已设置轻量套餐。

    有关其他服务套餐的更多信息，请参阅[价格套餐](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans)。

7. 单击**创建**。

供应实例后，将打开*日志记录*仪表板。 

接下来，通过添加 LogDNA 代理程序来配置日志源。此代理程序负责收集日志并将其转发到实例。 



## 通过目录供应实例
{: #provision_catalog}

要通过 {{site.data.keyword.cloud_notm}}“目录”来供应 {{site.data.keyword.la_full_notm}} 的实例，请完成以下步骤：

1. 登录到 {{site.data.keyword.cloud_notm}} 帐户。

    单击 [{{site.data.keyword.cloud_notm}} 仪表板 ![外部链接图标](../../icons/launch-glyph.svg "外部链接图标")](https://cloud.ibm.com/login){:new_window} 以启动 {{site.data.keyword.cloud_notm}}“仪表板”。

	使用用户标识和密码登录后，{{site.data.keyword.cloud_notm}} UI 即会打开。

2. 单击**目录**。这将打开 {{site.data.keyword.cloud_notm}} 中提供的服务的列表。

3. 要过滤显示的服务列表，请选择 **Developer Tools** 类别。

4. 单击 **{{site.data.keyword.la_full_notm}}** 磁贴。 

5. 输入服务实例的名称。

6. 选择资源组。 

    缺省情况下，已设置 **Default** 资源组。

    **注：**如果无法选择资源组，请检查您是否具有对要在其中供应实例的资源组的编辑许可权。

7. 选择`轻量`服务套餐。 

    缺省情况下，已设置轻量套餐。

    有关其他服务套餐的更多信息，请参阅[价格套餐](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans)。

8. 单击**创建**。

供应实例后，将打开*日志记录*仪表板。 

接下来，通过添加 LogDNA 代理程序来配置日志源。此代理程序负责收集日志并将其转发到实例。 



## 通过 CLI 供应实例
{: #provision_cli}

要通过命令行供应 {{site.data.keyword.la_full_notm}} 的实例，请完成以下步骤：

1. [先决条件] 安装 {{site.data.keyword.cloud_notm}} CLI。

   有关更多信息，请参阅[安装 {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli)。

   如果 CLI 已安装，请继续执行下一步。

2. 在 {{site.data.keyword.cloud_notm}} 中登录到要在其中供应实例的区域。运行以下命令：[`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)。

3. 设置要在其中供应实例的资源组。运行以下命令：[`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    缺省情况下，已设置 `default` 资源组。

4. 创建实例。运行 [`ibmcloud resource service-instance-create`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_create) 命令：

    ```
    ibmcloud resource service-instance-create NAME logdna SERVICE_PLAN_NAME LOCATION
    ```
    {: codeblock}

    其中：

    NAME 是实例的名称

    值 *logdna* 是 {{site.data.keyword.cloud_notm}} 中 {{site.data.keyword.la_full_notm}} 服务的名称

    SERVICE_PLAN_NAME 是套餐的类型。有效值为 *lite*、*7-days*、*14-days* 和 *30-days*
    
    LOCATION 是在其中创建 LogDNA 实例的区域。有效值为 *us-south*

    例如，要为实例供应 7 天保留期的套餐，请运行以下命令：

    ```
    ibmcloud resource service-instance-create logdna-instance-01 logdna 7-day us-south
    ```
    {: codeblock}

5. 创建具有**管理员**许可权的服务密钥以运行实例。运行 [`ibmcloud resource service-key-create`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_key_create) 命令：

    ```
    ibmcloud resource service-key-create NAME ROLE_NAME --instance-name SERVICE_INSTANCE_NAME
    ```
    {: codeblock}

    其中：

    NAME 是 API 密钥的名称。可以像对 {{site.data.keyword.la_full_notm}} 实例一样对 API 密钥命名，以帮助您日后识别 API 密钥。

    ROLE_NAME 是用于定义启用的许可权的角色。有效值为 *editor*、*operator* 和 *administrator*

    SERVICE_INSTANCE_NAME 是 {{site.data.keyword.cloud_notm}} 中实例的名称

    例如，要在服务实例上为实例 *logdna-instance-01* 创建具有*管理员*许可权的 API 密钥，请运行以下命令：

    ```
    ibmcloud resource service-key-create logdna-instance-01 Administrator --instance-name logdna-instance-01
    ```
    {: pre}

    此命令的输出包含不同的值，如实例的 `crn` 值和 LogDNA 摄入密钥。


