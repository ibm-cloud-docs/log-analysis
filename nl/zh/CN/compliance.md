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


# 合规性
{: #compliance}

[{{site.data.keyword.Bluemix}} 提供了依照 IBM 严格安全标准构建的云平台和服务。](/docs/security/compliance.html#compliance){{site.data.keyword.loganalysislong}} 服务是专为 {{site.data.keyword.Bluemix_notm}} 而构建的 DevOps 服务。
{:shortdesc}


## 一般数据保护条例

一般数据保护条例 (GDPR) 力求在整个欧盟范围内建立一个统一的数据保护法律框架，目的是让公民重新拥有对其个人数据的控制权，同时对全球任意位置托管和“处理”此类数据的相关方施加严格的规则。该条例还引入了与欧盟境内和境外个人数据自由流通相关的规则。 

**免责声明**：{{site.data.keyword.loganalysisshort}} 服务会存储和显示在您 {{site.data.keyword.Bluemix_notm}} 帐户中运行的云资源的日志记录，以及您可能从 {{site.data.keyword.Bluemix_notm}} 外部发送的日志的日志记录。在 {{site.data.keyword.loganalysisshort}} 中存储的任何日志条目中不得包含个人信息 (PI)，因为您企业内的其他用户有权访问这些条目，而且 {{site.data.keyword.IBM_notm}} 也会使用这些条目来为云服务提供支持。

### 区域
{: #regions}

{{site.data.keyword.loganalysisshort}} 服务在其所在 {{site.data.keyword.Bluemix_notm}} Public 区域中遵从 GDPR。


### 数据保留
{: #data_retention}

{{site.data.keyword.loganalysisshort}} 服务包含 2 个可用于存储数据的数据存储库： 

* 日志搜索，用于托管可通过 Kibana 进行分析的日志数据。
* 日志收集，用于托管长期存储的日志数据。

数据是单独存储在“日志搜索”中，还是同时存储在“日志搜索”和“日志收集”中，取决于 {{site.data.keyword.loganalysisshort}} 服务套餐。标准套餐或轻量套餐仅在“日志搜索”中存储数据。其余套餐会将数据同时存储在“日志搜索”和“日志收集”中。

* 存储在“日志搜索”中的日志会保留 3 天。
* 除非您配置了保留时间策略或手动将日志删除，否则会保留在“日志收集”中存储的日志。缺省情况下，“日志收集”中的日志会无限期保留。



### 数据删除
{: #data_deletion}

请考虑以下信息：

* 存储在“日志搜索”中的日志会在 3 天后删除。

* “日志收集”中存储的日志会在您配置的保留时间策略中指定的天数后删除，您也可以手动删除这些日志。 

    可以配置日志保留时间策略，以定义希望日志在“日志收集”中保留的天数。有关更多信息，请参阅[使用 {{site.data.keyword.Bluemix_notm}} 插件查看和配置日志保留时间策略](/docs/services/CloudLogAnalysis/how-to/manage-logs/configuring_retention_policy_cloud.html#configuring_retention_policy)。

    您可以使用[日志收集 API](https://console.bluemix.net/apidocs/948-ibm-cloud-log-collection-api?&language=node&env_id=ibm%3Ayp%3Aus-south#introduction){: new_window} 或[日志收集 CLI](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#log_analysis_cli){: new_window} 从“日志收集”中手动删除日志。 

    您可以使用 CLI 从“日志收集”中手动删除日志。有关更多信息，请参阅[使用 {{site.data.keyword.Bluemix_notm}} 插件运行 ibmcloud logging log-delete](/docs/services/CloudLogAnalysis/how-to/manage-logs/deleting_logs_cloud.html#deleting_logs)。


如果从付费套餐更改为标准套餐或轻量套餐，那么“日志收集”中的日志将会在大约一天后删除。

您可以随时开具支持凭单，请求从“日志搜索”和“日志收集”中删除您的所有数据。有关开具 IBM 支持凭单的信息，请参阅[联系支持人员](/docs/get-support/howtogetsupport.html#getting-customer-support)。



### 更多信息
{: #info}

要获取更多信息，请参阅：

[{{site.data.keyword.Bluemix_notm}} 安全合规性](/docs/security/compliance.html#compliance)

[GDPR - {{site.data.keyword.IBM_notm}} 官方页面](https://www.ibm.com/data-responsibility/gdpr/)



