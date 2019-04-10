---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-07"

keywords: LogDNA, IBM, Log Analysis, logging, getting started

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

# 入门教程
{: #getting-started}

使用 {{site.data.keyword.la_full}} 可向 {{site.data.keyword.cloud_notm}} 体系结构添加日志管理功能。{{site.data.keyword.la_full_notm}} 由 LogDNA 与 {{site.data.keyword.IBM_notm}} 合作运行。
{:shortdesc}


## 步骤 1. 开始之前
{: #getting-started_prereqs}

* 请阅读有关 {{site.data.keyword.la_full_notm}} 的信息。有关更多信息，请参阅[关于 {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about)。
* 检查服务在其中可用的区域。有关更多信息，请参阅[区域](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_regions)。
* 获取作为 {{site.data.keyword.cloud_notm}} 帐户的成员或所有者的用户标识。 

    要获取 {{site.data.keyword.cloud_notm}} 用户标识，请单击[注册 ![外部链接图标](../../icons/launch-glyph.svg "外部链接图标")](https://cloud.ibm.com/login){:new_window}。



## 步骤 2. 开始使用
{: #getting-started_step2}

选择要管理其日志的云资源。然后，配置此日志源，以便可以通过 {{site.data.keyword.la_full_notm}} 服务来监视其日志。日志源可以位于供应 {{site.data.keyword.la_full_notm}} 实例的同一区域中，也可以位于不同区域中。

下表列出了可以配置为使用 {{site.data.keyword.la_full_notm}} 服务来存储和管理日志的云资源的示例。完成资源的教程，以开始使用 {{site.data.keyword.loganalysisshort}} 服务：

<table>
  <caption>使用 {{site.data.keyword.la_full_notm}} 服务的入门教程</caption>
  <tr>
    <th>资源</th>
    <th>教程</th>
    <th>环境</th>
    <th>场景</th>
  </tr>
  <tr>
    <td>在 {{site.data.keyword.containershort}} 上运行的容器</td>
    <td>[使用 {{site.data.keyword.la_full_notm}} 管理 Kubernetes 集群日志](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-kube#kube)</td>
    <td>{{site.data.keyword.cloud_notm}} Public</td>
    <td>![{{site.data.keyword.containershort}} 和 {{site.data.keyword.la_full_notm}}](images/kube.png "{{site.data.keyword.containershort}} 和 {{site.data.keyword.la_full_notm}}")</td>
  </tr>
  <tr>
    <td>Linux Ubuntu 和 Linux Debian</td>
    <td>[使用 {{site.data.keyword.la_full_notm}} 管理 Linux Ubuntu 日志](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-ubuntu#ubuntu)</td>
    <td>内部部署</td>
    <td>![Ubuntu 服务器和 {{site.data.keyword.la_full_notm}}](images/ubuntu.png "Ubuntu 服务器和 {{site.data.keyword.la_full_notm}}")</td>
  </tr>
</table>



## 步骤 3. 升级套餐
{: #getting-started_step3}

启用更多日志记录功能。

将 {{site.data.keyword.la_full_notm}} 服务套餐升级到付费套餐，以便能够[过滤日志](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5)、[搜索日志](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6)、[定义视图](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7)和[配置警报](https://docs.logdna.com/docs/alerts)。有关 {{site.data.keyword.la_full_notm}} 服务套餐的更多信息，请参阅[价格套餐](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans)。

## 步骤 4. 后续步骤 
{: #getting-started_iam}

接下来，使用 IAM 管理用户访问权。

确定用户使用 {{site.data.keyword.la_full_notm}} 服务需要的 IAM 策略。

要了解有关与 {{site.data.keyword.la_full_notm}} 服务的 IAM 集成的更多信息，请参阅[使用 IAM 管理用户访问权](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#iam)。

例如，选择一个用户角色，以了解如何向该用户授予使用 {{site.data.keyword.la_full_notm}} 服务的许可权。 

|{{site.data.keyword.cloud_notm}} 中的用户角色|了解更多信息|
|-----------------------------------------------------|------------------------------------------|
|帐户所有者|[向用户授予许可权，使其成为 {{site.data.keyword.cloud_notm}} 帐户中服务的管理员](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account)|
|帐户中的平台服务管理员|[向用户授予许可权，使其成为 {{site.data.keyword.cloud_notm}} 帐户中服务的管理员](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account)|
|资源组中的平台服务管理员|[向用户授予许可权，使其成为资源组中服务的管理员](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_rg)|
|帐户中的平台 DevOps 操作员|[向 DevOps 用户授予管理 {{site.data.keyword.cloud_notm}} 帐户中服务的许可权](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#devops_account)|
|资源组中的平台 DevOps 操作员|[向 DevOps 用户授予管理资源组中服务的许可权](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#devops_rg)|
|LogDNA 中的服务管理员|[授予在 LogDNA 中管理日志和配置警报的许可权](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna)|
|用户/开发者|[向用户授予在 LogDNA 中查看和管理日志的许可权](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna)|
{: caption="表 2. {{site.data.keyword.cloud_notm}} 中的云角色" caption-side="top"}


