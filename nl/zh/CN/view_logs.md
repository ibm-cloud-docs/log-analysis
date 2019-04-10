---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, logs

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

# 查看日志
{: #view_logs}

在 {{site.data.keyword.cloud_notm}} 中供应 {{site.data.keyword.la_full_notm}} 服务的实例，并为日志源配置了 LogDNA 代理程序后，可以通过 {{site.data.keyword.la_full_notm}} Web UI 来查看、监视和管理日志数据。
{:shortdesc}

启动 {{site.data.keyword.la_full_notm}} Web UI 时，将显示具有预定义格式的日志条目。可以在**用户首选项**部分中修改每个日志行中信息的显示方式。还可以过滤日志并修改搜索设置，然后将结果作为*视图*添加书签。您可以将一个或多个警报连接到视图，也可以从视图拆离一个或多个警报。可以为视图中行的显示方式定义定制格式。还可以展开日志行并查看已解析的数据。


要查看日志，请完成以下步骤：


## 步骤 1. 向用户授予 IAM 策略以查看日志
{: #view_logs_step1}

**注：**您必须是 {{site.data.keyword.la_full_notm}} 服务的管理员、{{site.data.keyword.la_full_notm}} 实例的管理员，或者具有可向其他用户授予策略的帐户 IAM 许可权。

下表列出了用户必须拥有才能启动 {{site.data.keyword.la_full_notm}} Web UI 和查看日志的最低策略：

|服务|角色 |授予的许可权|
|--------------------------------|---------------------------|-------------------------------|  
| `{{site.data.keyword.la_full_notm}} ` |平台角色：查看者|允许用户在“可观察性 - 日志记录”仪表板中查看服务实例的列表。|
| `{{site.data.keyword.la_full_notm}} ` |服务角色：读取者|允许用户启动 Web UI，并在 Web UI 中查看日志。|
{: caption="表 1. IAM 策略" caption-side="top"} 

有关如何为用户配置这些策略的更多信息，请参阅[向用户授予查看 LogDNA 中日志的许可权](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna)。


## 步骤 2. 通过 {{site.data.keyword.cloud_notm}} UI 导航至 Web UI
{: #view_logs_step2}

要通过 {{site.data.keyword.cloud_notm}} UI 启动 {{site.data.keyword.la_full_notm}} UI，请完成以下步骤：

1. 登录到 {{site.data.keyword.cloud_notm}} 帐户。

    单击 [{{site.data.keyword.cloud_notm}} 仪表板 ![外部链接图标](../../icons/launch-glyph.svg "外部链接图标")](https://cloud.ibm.com/login){:new_window} 以启动 {{site.data.keyword.cloud_notm}}“仪表板”。

	使用用户标识和密码登录后，{{site.data.keyword.cloud_notm}} *仪表板*即会打开。

2. 在导航菜单中，选择**可观察性**。 

3. 选择**日志记录**。 

    这将显示 {{site.data.keyword.cloud_notm}} 上可用的 {{site.data.keyword.la_full_notm}} 实例的列表。

4. 选择一个实例。然后，单击**查看 LogDNA**。

{{site.data.keyword.la_full_notm}} Web UI 将打开并显示转发到该实例的日志。


## 步骤 3. 定制缺省视图
{: #view_logs_step3}

在**用户首选项**部分中，可以修改每行显示的数据字段的顺序。

要修改日志行的格式，请完成以下步骤：

1. 选择**配置**图标 ![“配置”图标](images/admin.png "“管理员”图标")。
2. 选择**用户首选项**。这将打开一个新窗口。
3. 选择**日志格式**。
4. 修改*行格式*部分以匹配您的需求。拖动各个框。


## 步骤 4. 查看日志行
{: #view_logs_step4}

您可以随时查看上下文中的每个日志行。

完成以下步骤： 

1. 单击**视图**图标 ![“配置”图标](images/views.png "“配置”图标")。
2. 选择**全部内容**或视图。
3. 确定日志中要探索的行。
4. 展开该日志行。 

    这将显示有关行标识、标记和标签的信息。

5. 单击**在上下文中查看**以在该主机和/或应用程序的其他日志行的上下文中查看该日志行。

6. 单击**复制到剪贴板**以将消息字段复制到剪贴板。

完成后，请关闭该行。


## 步骤 5. 过滤日志
{: #view_logs_step5}

可以按日志源、应用程序和日志级别过滤日志。 

* 源可以是主机、计算机、虚拟机或 Heroku 应用程序。
* 应用程序表示日志文件、程序或容器。
* 日志级别的示例包括：INFO、DEBUG、ERROR

要过滤日志，请完成以下步骤：

1. 单击**视图**图标 ![“配置”图标](images/views.png "“配置”图标")。
2. 选择**全部内容**或视图。
3. 展开**所有标记**以查看在日志中识别到的标记的列表。然后，选择所需的标记。
4. 展开**所有源**以查看日志中识别到的日志源的列表。然后，选择所需的日志源。
5. 展开**所有应用程序**以查看在日志中识别到的应用程序的列表。然后，选择所需的应用程序。
6. 展开**所有级别**以查看在日志中识别到的日志级别的列表。然后，选择所需的日志级别。


**注：**在每个部分中，可以将多个选项分组到一个组中。对标记、日志源、应用程序和日志级别分组后，可在其他定制视图中过滤日志数据时复用这些分组。

要创建组，请选择多个值。然后，单击**另存为组**。输入组的名称，然后保存该组。


## 步骤 6. 搜索日志
{: #view_logs_step6}

搜索日志数据时，搜索将应用在该视图中配置的任何日志过滤器和时间查询。

可以执行简单搜索（单个搜索项字符串搜索）、复合搜索（多个搜索项和运算符）、字段搜索（如果可以解析日志行）等。有关更多信息，请参阅 LogDNA 文档中的 [How to Search Logs ![外部链接图标](../../icons/launch-glyph.svg "外部链接图标")](https://docs.logdna.com/docs/search){:new_window}。

**注：**AND 和 OR 运算符区分大小写，并且必须大写。



## 步骤 7. 创建视图
{: #view_logs_step7}


要创建视图，请完成以下步骤：

1. 单击**视图**图标 ![“配置”图标](images/views.png "“配置”图标")。
2. 选择**全部内容**或视图。
3. 过滤日志数据，然后单击**另存为新视图/警报**。

    这将打开*新建视图*页面。

4. 在*名称*字段中输入视图的名称。

5. （可选）添加类别。输入名称，然后单击**将此名称添加为新视图类别**。

6. （可选）连接警报。这将显示一个新部分，用于配置警报。

7. 单击**保存视图**。


