---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, IAM, security, logging, access groups

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

 
# 管理 IAM 策略和访问组
{: #work_iam}

您可以使用 {{site.data.keyword.iamlong}} (IAM) 在 {{site.data.keyword.cloud_notm}} 中安全地认证用户，并以一致的方式控制对所有云资源的访问权。
{:shortdesc}

有关更多信息，请参阅[使用 IAM 管理用户访问权](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#iam)。


## 向用户授予许可权，使其成为 {{site.data.keyword.cloud_notm}} 帐户中服务的管理员
{: #admin_account}

作为**帐户所有者**或 **{{site.data.keyword.la_full_notm}} 服务管理员**，您必须具有运行以下操作的许可权： 

* 授予其他帐户成员使用服务的访问权
* 供应服务实例
* 删除服务实例
* 查看服务实例的详细信息
* 创建服务标识

因此，要向用户授予管理员角色来管理帐户中的服务，用户必须具有包含对 {{site.data.keyword.la_full_notm}} 服务的**管理员**平台角色的 IAM 策略。您必须为此用户分配对帐户中单个资源的访问权。 

要为用户分配对帐户中 {{site.data.keyword.la_full_notm}} 服务的管理员角色，请完成以下步骤： 

1. 在菜单栏中，单击**管理** &gt; **访问权 (IAM)**，然后选择**用户**。
2. 在要为其分配访问权的用户所在的行中，选择**操作**菜单，然后单击**分配访问权**。
3. 选择**分配对资源的访问权**。
4. 选择 **IBM Log Analysis with LogDNA**。
5. 选择**所有当前区域**。
6. 选择**所有当前服务实例**。
7. 选择**管理员**平台角色。
8. 单击“分配”。


## 向用户授予许可权，使其成为资源组中服务的管理员
{: #admin_rg}

作为 **{{site.data.keyword.la_full_notm}} 服务管理员**，您必须具有运行以下操作的许可权： 

* 授予其他帐户成员使用服务的访问权
* 供应服务实例
* 删除服务实例
* 查看服务实例的详细信息
* 创建服务标识

因此，要向用户授予管理员角色来管理帐户中资源组内的实例，用户必须在资源组上下文中具有包含对 {{site.data.keyword.la_full_notm}} 服务的**管理员**平台角色的 IAM 策略。 

要在资源组上下文中为用户分配对 {{site.data.keyword.la_full_notm}} 服务的管理员角色，请完成以下步骤： 

1. 在菜单栏中，单击**管理** &gt; **访问权 (IAM)**，然后选择**用户**。
2. 在要为其分配访问权的用户所在的行中，选择**操作**菜单，然后单击**分配访问权**。
3. 选择**在资源组中分配访问权**。
4. 选择资源组。
5. 如果尚未向用户授予针对所选资源组的角色，请为**分配对资源组的访问权**字段选择角色。 

    根据选择的角色，用户可以在其仪表板上查看资源组，编辑资源组名称或管理用户对该组的访问权。 
    
    如果希望用户仅有权访问资源组中的 {{site.data.keyword.la_full_notm}} 服务，那么可以选择**无访问权**。

6. 选择 **IBM Log Analysis with LogDNA**。
7. 选择**管理员**平台角色。
8. 单击**分配**。


## 向 DevOps 用户授予管理 {{site.data.keyword.cloud_notm}} 帐户中服务的许可权
{: #devops_account}

作为 **DevOps 用户**，您必须具有运行以下操作的许可权： 

* 供应服务实例
* 删除服务实例
* 查看服务实例的详细信息
* 创建服务标识

因此，您需要具有包含对 {{site.data.keyword.la_full_notm}} 服务的**编辑者**平台角色的 IAM 策略。

要为用户分配对帐户中 {{site.data.keyword.la_full_notm}} 服务的编辑者角色，请完成以下步骤： 

1. 在菜单栏中，单击**管理** &gt; **访问权 (IAM)**，然后选择**用户**。
2. 在要为其分配访问权的用户所在的行中，选择**操作**菜单，然后单击**分配访问权**。
3. 选择**分配对资源的访问权**。
4. 选择 **IBM Log Analysis with LogDNA**。
5. 选择**所有服务实例**。
6. 选择**编辑者**平台角色。
7. 单击“分配”。

## 向 DevOps 用户授予管理 {{site.data.keyword.cloud_notm}} 帐户中实例的许可权
{: #devops_account_instance}

要为用户分配对帐户中某个 {{site.data.keyword.la_full_notm}} 服务实例的编辑者角色，请完成以下步骤： 

1. 在菜单栏中，单击**管理** &gt; **访问权 (IAM)**，然后选择**用户**。
2. 在要为其分配访问权的用户所在的行中，选择**操作**菜单，然后单击**分配访问权**。
3. 选择**分配对资源的访问权**。
4. 选择 **IBM Log Analysis with LogDNA**。
5. 选择该实例。
6. 选择**编辑者**平台角色。
7. 单击“分配”。



## 向 DevOps 用户授予管理资源组中服务的许可权
{: #devops_rg}

作为 **DevOps 用户**，您必须具有运行以下操作的许可权： 

* 供应服务实例
* 删除服务实例
* 查看服务实例的详细信息
* 创建服务标识

因此，您需要包含对 {{site.data.keyword.la_full_notm}} 服务的**编辑者**平台角色的 IAM 策略。

要在资源组上下文中为用户分配对 {{site.data.keyword.la_full_notm}} 服务的编辑者角色，请完成以下步骤： 

1. 在菜单栏中，单击**管理** &gt; **访问权 (IAM)**，然后选择**用户**。
2. 在要为其分配访问权的用户所在的行中，选择**操作**菜单，然后单击**分配访问权**。
3. 选择**在资源组中分配访问权**。
4. 选择资源组。
5. 如果尚未向用户授予针对所选资源组的角色，请为**分配对资源组的访问权**字段选择角色。 

    根据选择的角色，用户可以在其仪表板上查看资源组，编辑资源组名称或管理用户对该组的访问权。 
    
    如果希望用户仅有权访问资源组中的 {{site.data.keyword.la_full_notm}} 服务，那么可以选择**无访问权**。

6. 选择 **IBM Log Analysis with LogDNA**。
7. 选择**编辑者**平台角色。
8. 单击**分配**。

## 授予在 LogDNA 中管理日志和配置警报的许可权
{: #admin_user_logdna}

作为 LogDNA 中的**管理员用户**，您必须具有运行以下操作的许可权： 

* 添加 LogDNA 日志源
* 查看日志
* 搜索日志
* 过滤日志
* 配置警报

因此，您需要以下策略：

* 包含对 {{site.data.keyword.la_full_notm}} 服务的**编辑者**平台角色的 IAM 策略。此策略授予通过命令行和 {{site.data.keyword.cloud_notm}} 仪表板查看服务实例详细信息的许可权。
* 包含对 {{site.data.keyword.la_full_notm}} 服务的**管理者**服务角色的 IAM 策略。此策略授予通过 LogDNA Web UI 监视、过滤和搜索日志以及定义警报的许可权。

**注：**作为服务的管理员，您向用户授予这些策略时，请考虑在资源组的上下文中进行授予。{{site.data.keyword.la_full_notm}} 实例是在资源组的上下文中进行供应的。因此，请在资源组的上下文中授予访问许可权。


要在资源组的上下文中为用户分配对 {{site.data.keyword.la_full_notm}} 服务的这两个策略，请完成以下步骤： 

1. 在菜单栏中，单击**管理** &gt; **访问权 (IAM)**，然后选择**用户**。
2. 在要为其分配访问权的用户所在的行中，选择**操作**菜单，然后单击**分配访问权**。
3. 选择**在资源组中分配访问权**。
4. 选择资源组。
5. 如果尚未向用户授予针对所选资源组的角色，请为**分配对资源组的访问权**字段选择角色。 

    根据选择的角色，用户可以在其仪表板上查看资源组，编辑资源组名称或管理用户对该组的访问权。 
    
    如果希望用户仅有权访问资源组中的 {{site.data.keyword.la_full_notm}} 服务，那么可以选择**无访问权**。

6. 选择 **IBM Log Analysis with LogDNA**。
7. 选择**编辑者**平台角色。
8. 选择**管理者**服务角色。
8. 单击**分配**。

## 向用户授予查看 LogDNA 中日志的许可权
{: #user_logdna}

作为**用户**、**审计员**或**开发者**，您可能需要运行以下操作的许可权： 

* 查看日志
* 搜索日志
* 过滤日志

因此，您需要以下策略：

* 包含对 {{site.data.keyword.la_full_notm}} 服务的**查看者**平台角色的 IAM 策略。此策略授予通过命令行和 {{site.data.keyword.cloud_notm}} 仪表板查看服务实例详细信息的许可权。
* 包含对 {{site.data.keyword.la_full_notm}} 服务的**读取者**服务角色的 IAM 策略。此策略授予通过 LogDNA Web UI 监视、过滤和搜索日志的许可权。

**注：**作为服务的管理员，您向用户授予这些策略时，请考虑在资源组的上下文中进行授予。{{site.data.keyword.la_full_notm}} 实例是在资源组的上下文中进行供应的。因此，请在资源组的上下文中向用户授予访问许可权。

要在资源组的上下文中为用户分配对 {{site.data.keyword.la_full_notm}} 服务的这两个策略，请完成以下步骤： 

1. 在菜单栏中，单击**管理** &gt; **访问权 (IAM)**，然后选择**用户**。
2. 在要为其分配访问权的用户所在的行中，选择**操作**菜单，然后单击**分配访问权**。
3. 选择**在资源组中分配访问权**。
4. 选择资源组。
5. 如果尚未向用户授予针对所选资源组的角色，请为**分配对资源组的访问权**字段选择角色。 

    根据选择的角色，用户可以在其仪表板上查看资源组，编辑资源组名称或管理用户对该组的访问权。 
    
    如果希望用户仅有权访问资源组中的 {{site.data.keyword.la_full_notm}} 服务，那么可以选择**无访问权**。

6. 选择 **IBM Log Analysis with LogDNA**。
7. 选择**查看者**平台角色。
8. 选择**读取者**服务角色。
8. 单击**分配**。

