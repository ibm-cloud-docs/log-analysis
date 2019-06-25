---

copyright:
  years:  2018, 2019
lastupdated: "2019-04-02"

keywords: LogDNA, IBM, Log Analysis, logging instance, enable, service logs

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

# 配置 {{site.data.keyword.cloud_notm}} 服务日志
{: #config_svc_logs}

在一个区域中可以拥有多个 {{site.data.keyword.la_full_notm}} 实例。然而，只能在一个区域中配置一个实例，以便从 {{site.data.keyword.cloud_notm}} 中的已启用服务接收日志。
{:shortdesc}



## 通过“可观察性”仪表板配置平台服务日志
{: #config_svc_logs_ui}

要通过 {{site.data.keyword.cloud_notm}} 中的“可观察性”仪表板来配置实例，请完成以下步骤：

1. [登录到 {{site.data.keyword.cloud_notm}} 账户 ![外部链接图标](../../icons/launch-glyph.svg "外部链接图标")](https://cloud.ibm.com/login){:new_window}。

	使用用户标识和密码登录后，{{site.data.keyword.cloud_notm}} UI 即会打开。

2. 转至“菜单”图标 ![“菜单”图标](../../icons/icon_hamburger.svg)。然后，选择**可观察性**以访问*可观察性*仪表板。

3. 选择**日志记录**，然后单击**配置平台服务日志**。 

4. 选择 LogDNA 实例以从云平台启用的服务中接收日志。

5. 选择区域。 

6. 选择实例。

7. 单击**保存**。 

这将打开*可观察性*主页面。

选择接收服务日志的实例显示标志**平台服务日志**。

有关启用将日志发送到 {{site.data.keyword.la_full_notm}} 的服务的更多信息，请参阅[云服务](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services)。

