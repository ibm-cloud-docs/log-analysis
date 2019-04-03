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

# 在 Kibana 中通过仪表板分析日志
{:#analize_logs_dashboard}

使用 Kibana 中的*仪表板*页面可显示按仪表板分组的可视化项集合。使用仪表板可分析日志数据并比较结果。
{:shortdesc}

在 {{site.data.keyword.Bluemix}} 中，可以定义和定制不同类型的仪表板来对数据进行可视化和分析。例如，下表列出了一些常用的仪表板类型：

|仪表板类型|描述
|
|-------------------|-------------|
|单 CF 应用程序仪表板|此仪表板用于显示单个 Cloud Foundry 应用程序的信息。|
|单容器仪表板|此仪表板用于显示单个容器的信息。|
|容器组仪表板|此仪表板用于显示特定容器组的信息。|
|多 CF 应用程序仪表板|此仪表板用于显示同一空间内部署的所有 Cloud Foundry 应用程序的信息。| 
|多容器仪表板|此仪表板用于显示同一空间内部署的所有容器的信息。|
|空间仪表板|此仪表板用于显示空间中可用的日志记录数据。| 
{: caption="表 1. 仪表板类型的样本" caption-side="top"}

要在仪表板中将数据可视化，可以配置面板。Kibana 包含可用于分析信息的不同可视化项，如表、趋势和直方图。将可视化项作为面板添加到仪表板。可以在仪表板中添加、除去和重新排列面板。每个面板的用途各不相同。一些面板组织成行，用于提供一个或多个查询的结果。另一些面板则显示文档或定制信息。每个面板基于一个搜索。搜索用于定义面板显示的数据子集。例如，可以配置条形图、饼图或表来对数据进行可视化表示和分析。  

下表列出了可在“仪表板”页面中执行的不同任务：

|任务|更多信息|
|------|------------------|
|[添加可视化项](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#add_visualization)|可以向仪表板添加现有可视化项或搜索。|
|[新建仪表板](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#new)|可以创建多个仪表板。每个仪表板可以设计为包含不同的搜索、可视化项和不同的日志数据子集。|
|[删除仪表板](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#delete)|删除不需要的仪表板。|
|[导出仪表板](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#export)|可以将仪表板导出为 JSON 文件。|
|[导入仪表板](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#import)|可以将仪表板作为 JSON 文件导入。|
|[装入仪表板](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#reload3)|可以上传仪表板以更新其数据，修改仪表板或分析数据。|
|[保存仪表板](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#save)|可以保存仪表板以供日后复用。|
{: caption="表 2. 使用仪表板的任务" caption-side="top"}

有关 Kibana 的更多信息，请参阅 [Kibana User Guide ![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}。


## 添加新的搜索或可视化项
{: #add_visualization}

要添加现有可视化项或搜索，请完成以下步骤：

1. 在“仪表板”页面的工具栏中，单击**添加**。 

    **注**：可以添加可视化项和搜索。 

2. 选择**可视化项**选项卡以添加可视化项，或者选择**搜索**选项卡以添加搜索。

3. 单击要添加的搜索或可视化项。

    该搜索或可视化项的面板会添加到仪表板。

	
## 新建 Kibana 仪表板
{: #new}

要创建新的仪表板，请完成以下步骤：

1. 在“仪表板”页面的工具栏中，单击**添加**。 

2. 添加一个或多个搜索和可视化项。有关更多信息，请参阅[添加新的搜索或可视化项](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#add_visualization)。

    添加搜索或可视化项时，将在仪表板中添加面板。

3. 将面板拖放到仪表板中您希望将其定位到的部分。
 
4. 保存仪表板以供未来复用。有关更多信息，请参阅[保存 Kibana 仪表板](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#save)。


## 删除 Kibana 仪表板
{: #delete1}

要删除仪表板，请在**管理**页面中完成以下步骤：

1. 在**管理**页面中，选择**保存的对象**。

2. 在**仪表板**选项卡中，选择要删除的仪表板。

3. 单击**删除**。

## 导出 Kibana 仪表板
{: #export}

要将仪表板导出为 JSON 文件，请在**管理**页面中完成以下步骤：

1. 在**管理**页面中，选择**保存的对象**。

2. 在**仪表板**选项卡中，选择要导出的仪表板。

3. 单击**导出**。

4. 保存文件。

## 导入 Kibana 仪表板
{: #import}

要将仪表板作为 JSON 文件导入，请在**管理**页面中完成以下步骤：

1. 在**管理**页面中，选择**保存的对象**。

2. 在**仪表板**选项卡中，选择**导入**。

3. 选择文件并单击**打开**。

仪表板将添加到仪表板列表中。

## 装入 Kibana 仪表板
{: #reload3}

要装入保存的仪表板，请完成以下步骤：

1. 在“仪表板”页面的工具栏中，单击**打开**。

2. 从*名称*字段下显示的可用仪表板列表中选择仪表板。

还可以通过搜索栏来搜索仪表板。

## 保存 Kibana 仪表板
{: #save}

要保存定制后的 Kibana 仪表板，请完成以下步骤：

1. 在工具栏中，单击**保存**。

2. 输入仪表板的名称。

    **注**：此名称不能包含空格。

3. 单击**保存**。




