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


# Kibana 常见问题
{: #faq_kibana}

下面是对有关使用 {{site.data.keyword.Bluemix}} 日志记录功能的常见问题的解答。
{:shortdesc}

* [如果在 Kibana 的“发现”页面中看不到数据该怎么办](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-faq_kibana#logging_qa_no_data_discover_kibana)
* [如果获得认证异常该怎么办](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-faq_kibana#logging_qa_no_data_dashboard_kibana)
* [为什么在 Kibana 的“发现”页面中会看到字段旁边有符号 ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-faq_kibana#logging_qa_kibana_question)
* [尝试更改缺省索引模式时，收到 403 错误](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-faq_kibana#error_403)
* [简短 URL 不起作用](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-faq_kibana#short_url)
* [可以在 Bluemix 中搜索帐户日志吗？](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-faq_kibana#acc_logs_1)


## 如果在 Kibana 的“发现”页面中看不到数据该怎么办
{: #logging_qa_no_data_discover_kibana}

有多种不同的场景可能会导致在 Kibana 中看不到数据：

1. 启动 Kibana 时，可能在“发现”页面中看不到任何数据。您会收到以下消息：**找不到任何结果。** 
2. 您可能正在 Kibana 的“发现”页面中工作。但是，您在短时间内收到消息：**找不到任何结果。**

要解决此问题，请完成以下步骤：

1. 检查在“发现”页面中设置的*时间选取器*，并增大时间段。 

    **注**：缺省情况下，在 {{site.data.keyword.Bluemix_notm}} 中，*时间选取器*设置为显示最近 15 分钟的数据。

    有关如何设置*时间选取器*的更多信息，请参阅[设置时间过滤器](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter1)。
       
2. 单击*发现*页面搜索栏中的放大镜。页面数据会基于缺省搜索查询进行刷新。

    或者，可以设置*自动刷新*时间段。

    **注**：缺省情况下，在 {{site.data.keyword.Bluemix_notm}} 中，*自动刷新*时间段设置为**关闭**。
    
    有关如何将其启用的更多信息，请参阅[自动刷新数据](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_view_refresh_interval)。



## 如果获得认证异常该怎么办
{: #logging_qa_no_data_dashboard_kibana}

如果在“仪表板”页面看不到可视化项中显示的数据，并且系统显示错误消息：**错误：授权异常。**，请检查您是否有权查看每个可视化项中的数据。

请考虑以下信息：
可以在“仪表板”页面中配置一个或多个可视化项。“仪表板”页面发起请求以收集通过这些可视化项显示的数据时，对于所有可视化项只会发起一个请求。如果您无权查看其中一个可视化项的数据，那么整个请求会失败。

要解决此问题，请完成以下步骤：

1. 确定您无权查看的可视化项。

    1. 单击*仪表板*页面中可视化项的*画笔*图标。该可视化项会在*可视化*页面中打开。或者，在*可视化*页面中，装入一个可视化项。 
    2. 验证是否可以看到数据。
    
    对每个可视化项重复上述步骤。

2. 向云管理员请求访问权以查看这些可视化项中的数据。

3. 在您等待授予访问权以查看导致此问题的可视化项中的数据期间，创建新的“仪表板”页面，将您无权查看的可视化项排除在外。 

    如果共享了仪表板，请勿删除这些可视化项，否则会影响使用同一仪表板的其他团队成员。



## 为什么在 Kibana 的“发现”页面中会看到字段旁边有符号 ?
{: #logging_qa_kibana_question}

在 Kibana 中打开“发现”页面时，您可能会在“可用字段”部分中所列出的字段旁边看到问号 `?` 而非字符 `t`。重新装入字段列表时，系统会分析字段的类型，而问号 `?` 会替换为字符 `t`。有关更多信息，请参阅[重新装入字段列表](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_view_reload_fields)。


## 尝试更改缺省索引模式时，收到 403 错误
{: #error_403}

无法更改缺省索引模式。 

如果尝试将其他索引模式设置为新的缺省索引模式，那么会收到以下错误：`配置：错误 403 已禁止`

## 简短 URL 不起作用
{: #short_url}

不支持共享搜索、可视化或仪表板。因此，您要共享的 Kibana 对象的任何简短 URL 也不会起作用。 

## 可以在 Bluemix 中搜索帐户日志吗？
{: #acc_logs_1}

作为帐户所有者，可以搜索并分析帐户日志。

要查看帐户日志，请完成以下步骤：

1. [启动 Kibana。](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-launch#launch_Kibana_from_browser)例如，对于美国南部区域，请使用 URL `https://logging.ng.bluemix.net`。

2. 选择选项**查看 AccountName 帐户日志**以显示帐户日志。*AccountName* 是帐户的名称。

