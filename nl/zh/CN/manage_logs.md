---

copyright:
  years: 2017, 2019

lastupdated: "2019-03-06"

keywords: IBM Cloud, logging

subcollection: cloudloganalysis

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


# 管理日志
{: #manage_logs}

您可以使用 {{site.data.keyword.loganalysisshort}} CLI 和 {{site.data.keyword.loganalysisshort}} API 来管理存储在“日志收集”中的日志。
{:shortdesc}

要管理日志，请考虑以下信息：

1. 用户标识必须在 {{site.data.keyword.Bluemix_notm}} 中分配有策略，具有许可权的 {{site.data.keyword.loganalysisshort}} 才能管理日志。 

    有关 IAM 角色和每种角色的任务的列表，请参阅 [IAM 角色](/docs/services/CloudLogAnalysis/security_ov.html#iam_roles)。 
	
	有关如何分配策略的更多信息，请参阅[通过 {{site.data.keyword.Bluemix_notm}} UI 将 IAM 策略分配给用户](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_account)。
	
2. 此功能仅可用于允许日志保留的服务套餐。 

    有关服务套餐的更多信息，请参阅[服务套餐](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)。

{{site.data.keyword.loganalysisshort}} 服务提供两个 CLI，您可用于管理日志：

* {{site.data.keyword.loganalysisshort}} {{site.data.keyword.Bluemix_notm}} 插件。有关 CLI 的更多信息，请参阅 [{{site.data.keyword.loganalysisshort}} CLI（{{site.data.keyword.Bluemix_notm}} 插件）](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#log_analysis_cli)。
* {{site.data.keyword.loganalysisshort}} CF 插件（已弃用）。有关 CLI 的更多信息，请参阅[配置 Log Analysis CLI（CF 插件）](/docs/services/CloudLogAnalysis/reference/logging_cli.html#logging_cli)。


## 配置日志保留时间策略
{: #log_retention_policy}

可以使用 {{site.data.keyword.loganalysisshort}} CLI 来查看和配置日志保留时间策略。此策略指定日志在“日志收集”中的保留天数。 

* 缺省情况下，当您选择付费套餐时，日志会收集并保留在“日志收集”中。 
* 如果设置了保留期，那么在保留期到期后，会自动从“日志收集”中删除日志，并且无法恢复这些日志。
* 可以为帐户指定保留期。保留期会自动针对该帐户中的所有空间进行配置。 
* 可以为空间指定保留期。
* 可以随时更改保留时间策略。
* 可以通过将该策略的值设置为 *-1* 以禁用该策略。 

**注**：禁用日志保留时间策略时，必须将日志保留在“日志收集”中。可以使用 CLI 命令 [cf logging delete](/docs/services/CloudLogAnalysis/reference/logging_cli.html#delete4) 来删除旧日志。

要获取更多信息，请参阅：

* [使用 {{site.data.keyword.Bluemix_notm}} 插件查看和配置日志保留时间策略](/docs/services/CloudLogAnalysis/how-to/manage-logs/configuring_retention_policy_cloud.html#configuring_retention_policy)。
* [使用 CF 插件查看和配置日志保留时间策略](/docs/services/CloudLogAnalysis/how-to/manage-logs/configuring_retention_policy.html#configuring_retention_policy)。


## 删除日志
{: #log_deletion}

存储在“日志搜索”中的日志会在 3 天后删除。

除非您配置了保留时间策略或手动将日志删除，否则会保留在“日志收集”中存储的日志。 

* 可以配置日志保留时间策略，以定义希望日志在“日志收集”中保留的天数。有关更多信息，请参阅[使用 {{site.data.keyword.Bluemix_notm}} 插件查看和配置日志保留时间策略](/docs/services/CloudLogAnalysis/how-to/manage-logs/configuring_retention_policy_cloud.html#configuring_retention_policy)。

* 您可以使用[日志收集 API](https://console.bluemix.net/apidocs/948-ibm-cloud-log-collection-api?&language=node&env_id=ibm%3Ayp%3Aus-south#introduction){: new_window} 或[日志收集 CLI](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#log_analysis_cli){: new_window} 从“日志收集”中手动删除日志。 

* 您可以使用 CLI。有关通过 CLI 手动删除日志的更多信息，请参阅[使用 {{site.data.keyword.Bluemix_notm}} 插件运行 ibmcloud logging log-delete](/docs/services/CloudLogAnalysis/how-to/manage-logs/deleting_logs_cloud.html#deleting_logs)。
    


## 下载日志
{: #download_logs2}

可以在 Kibana 中搜索最近 3 天的日志。为了能够分析更早的日志数据，可以将日志下载到本地文件，也可以通过管道将这些日志传递到其他程序，例如本地 Elastic 堆栈。 

要获取更多信息，请参阅：

* [使用 {{site.data.keyword.Bluemix_notm}} 插件下载日志](/docs/services/CloudLogAnalysis/how-to/manage-logs/downloading_logs_cloud.html#downloading_logs)。
* [使用 CF 插件下载日志](/docs/services/CloudLogAnalysis/how-to/manage-logs/downloading_logs.html#downloading_logs1)。



## 获取日志的信息
{: #info_about_logs}

要获取有关日志的常规信息，请使用 `ibmcloud logging log-show` 或 `cf logging status` 命令。要获取更多信息，请参阅：

* [使用 {{site.data.keyword.Bluemix_notm}} 插件查看日志信息](/docs/services/CloudLogAnalysis/how-to/manage-logs/viewing_log_information_cloud.html#viewing_log_status1)
* [使用 CF 插件查看日志信息](/docs/services/CloudLogAnalysis/how-to/manage-logs/viewing_log_information.html#viewing_log_status1)。

例如，为了控制成本，您可能希望监视应用程序日志在一段时间内的大小。例如，您可能希望知道 {{site.data.keyword.Bluemix_notm}} 空间的每种日志类型在一周内的大小，以确定任何应用程序或服务生成的日志是否超过期望数量。要检查日志的大小，请使用 `ibmcloud logging log-show` 或 `cf logging status` 命令。

您可以查看存储在空间域、组织域或帐户域的日志的信息。



## 安装 {{site.data.keyword.loganalysisshort_notm}} CLI（{{site.data.keyword.Bluemix_notm}} 插件）
{: #install_cli2}

要了解如何安装 CLI，请参阅[安装日志记录 CLI](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#config_log_collection_cli)。

要检查 CLI 的版本，请运行 `ibmcloud plugin list` 命令。

要获取有关如何运行命令的帮助，请参阅[获取命令行帮助以运行命令](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#command_cli_help)。


## 日志记录端点
{: #endpoints}

下表列出每个区域的日志记录 URL：

<table>
    <caption>每个区域的端点</caption>
    <tr>
      <th>区域</th>
      <th>URL</th>
    </tr>
	<tr>
      <td>法兰克福</td>
	  <td>[https://logging.eu-fra.bluemix.net](https://logging.eu-fra.bluemix.net)</td>
    </tr>
	<tr>
      <td>悉尼</td>
	  <td>[https://logging.au-syd.bluemix.net](https://logging.au-syd.bluemix.net)</td>
    </tr>
	<tr>
      <td>英国</td>
	  <td>[https://logging.eu-gb.bluemix.net](https://logging.eu-gb.bluemix.net)</td>
    </tr>
    <tr>
      <td>美国南部</td>
      <td>[https://logging.ng.bluemix.net](https://logging.ng.bluemix.net)</td>
    </tr>
</table>

## 用户管理日志所需的角色
{: #roles1}

在 {{site.data.keyword.Bluemix_notm}} 中，您可以将一个或多个角色分配给用户。这些角色可定义要启用什么任务以便该用户能够使用 {{site.data.keyword.loganalysisshort}} 服务。
 

下表列出用户管理日志时必须具有的角色：

<table>
  <caption>**帐户所有者**管理日志所需的许可权</caption>
  <tr>
	<th>IAM 角色</th>
	<th>操作</th>
  </tr>
  <tr>
    <td>*管理员*</td>
    <td>检查日志的状态</br>下载日志</br>删除日志</br>更改日志保留时间策略</br>管理会话</td>
</table>

<table>
  <caption>**审计员**管理日志所需的许可权</caption>
  <tr>
	<th>IAM 角色</th>
	<th>操作</th>
  </tr>
  <tr>
    <td>*查看者*</td>
    <td>获取在“日志收集”中托管的日志的信息。</br>获取配置的日志保留时间策略的信息。</td>
</table>

<table>
  <caption>**管理员**管理日志所需的许可权</caption>
  <tr>
	<th>IAM 角色</th>
	<th>操作</th>
  </tr>
  <tr>
    <td>*管理员*</td>
    <td>检查日志的状态</br>下载日志</br>删除日志</br>更改日志保留时间策略</br>管理会话</td>
</table>

<table>
  <caption>**开发者**管理日志所需的许可权。</caption>
  <tr>
	<th>IAM 角色</th>
	<th>操作</th>
  </tr>
  <tr>
    <td>*编辑者*</td>
    <td>检查日志的状态</br>下载日志</br>删除日志</br>更改日志保留时间策略</br>管理会话</td>
</table>

