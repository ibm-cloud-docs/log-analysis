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

# 在 Kibana 中使用可视化项分析日志 
{:#kibana_visualizations}

使用 Kibana 中的*可视化*页面创建可视化项（例如，图形和表），用于分析日志数据并比较结果。
{:shortdesc}

可以单独使用可视化项来分析日志。 

* 通过在*发现*页面中定义并保存的搜索，或通过在*可视化*页面中定义的新查询，可以创建可视化项。搜索会定义可视化项显示的数据子集。

* 选择的可视化项类型确定了如何显示数据以供分析。

下表列出了不同的可视化项类型：

|可视化项类型|描述
|
|-----------------------|-------------|
|面积图|以图形方式显示量化数据。用于比较两组或更多组聚集的数据。|
|数据表|以表格形式显示组合聚集的原始数据。|
|折线图|显示基于时间的数据。用于比较两组或更多组基于时间的聚集数据。|
|Markdown 窗口小部件|用于显示文本信息。|
|度量值|用于显示命中计数或数字字段的准确平均值。|
|饼图|用于显示字段的不同值。| 
|垂直条形图|显示基于时间的数据和非基于时间的数据。用于对数据分组。|
{: caption="表 1. 可视化项类型" caption-side="top"}

在“可视化”页面中，可以执行以下任一任务：

|任务|更多信息|
|------|------------------|
|[新建可视化项](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#create)|通过在*发现*页面中定义并保存的搜索，或通过在*可视化*页面中定义的新查询，可以创建可视化项。|
|[删除可视化项](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#delete)|删除不需要的可视化项。|
|[导出可视化项](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#export)|可以将可视化项导出为 JSON 文件。|
|[导入可视化项](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#import1)|可以将可视化项作为 JSON 文件导入。|
|[装入可视化项](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#reload2)|可以上传可视化项以更新其数据，修改可视化项或分析数据。|
|[保存可视化项](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#save2)|可以保存可视化项以供未来复用。|
{: caption="表 2. 使用可视化项的任务" caption-side="top"}


## 在 Kibana 中通过查询创建可视化项
{: #create}

要在“可视化”页面中创建可视化项，请完成以下步骤：

1. 启动 Kibana，然后选择**可视化**页面。

2. 选择可视化项的类型，例如*表*。

3. 在**或者，通过保存的搜索选择**中选择早先保存的可视化项，或在**通过新搜索选择索引**部分中选择索引。

4. 配置查询。

    * 如果选择**或者，通过保存的搜索选择**，请选择搜索查询。该查询用于检索供可视化项使用的数据。 
	
	    选择搜索后，可视化项构建器会打开，并装入所选查询的数据。 
		
		**注**：对保存的搜索进行的任何更改都会自动反映在可视化项中。要禁用对链接到此可视化项的查询进行的自动更新，请双击消息：*此可视化项已链接到保存的搜索：your_search_name* 

    * 如果选择**通过新搜索选择索引**，请定义新查询。该查询用于定义由可视化项检索并使用的数据子集。

        有关更多信息，请参阅[通过定义定制查询来过滤日志](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#define_search)。

有关 Kibana 的更多信息，请参阅 [Kibana User Guide ![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}。


## 删除可视化项
{: #delete}

要删除可视化项，请在**管理**页面中完成以下步骤：

1. 在**管理**页面中，选择**保存的对象**。

2. 在**可视化项**选项卡中，选择要删除的可视化项。

3. 单击**删除**。


## 导出可视化项
{: #export1}

要将可视化项导出为 JSON 文件，请在**管理**页面中完成以下步骤：

1. 在**管理**页面中，选择**保存的对象**。

2. 在**可视化项**选项卡中，选择要导出的可视化项。

3. 单击**导出**。

4. 保存文件。

## 导入可视化项
{: #import1}

要将可视化项作为 JSON 文件导入，请在**管理**页面中完成以下步骤：

1. 在**管理**页面中，选择**保存的对象**。

2. 在**可视化项**选项卡中，选择**导入**。

3. 选择文件并单击**打开**。

该可视化项将添加到可视化项列表中。


 
## 装入可视化项
{: #reload2}

要装入保存的可视化项，请完成以下步骤：

1. 在“可视化”页面的工具栏中，单击**打开**。

2. 选择要装入的可视化项。 


## 保存可视化项
{: #save2}

要在“可视化”页面中保存可视化项，请完成以下步骤：

1. 在“可视化”页面的工具栏中，单击**保存**。

2. 输入可视化项的名称。

3. 单击“保存”。 


