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

# 定义定制搜索查询
{:#define_search}

在“发现”页面的搜索栏中，可以使用 Lucene 查询语言来定义并保存搜索查询。对于每个搜索，可以应用过滤器来优化可供分析的条目。
{:shortdesc}

要定义定制搜索，请完成以下任务：

1. 启动 Kibana。

    对于 Cloud Foundry (CF) 应用程序，请参阅[通过 CF 应用程序的仪表板启动 Kibana](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_cf_app)。

	对于在 {{site.data.keyword.Bluemix_notm}} 管理的基础架构中运行的容器，请参阅[通过容器的仪表板启动 Kibana](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_for_containers)。
    
    对于所有云资源（例如，在 Kubernetes 集群中运行的容器），请参阅[通过浏览器启动 Kibana](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser)。 
	
	访问 Kibana 时，将应用缺省搜索。您可以看到要查询的资源实例列表的日志。可以过滤该空间中任何或全部 {{site.data.keyword.Bluemix_notm}} 资源的日志。

2. 查看“发现”页面，以确定它显示的数据子集。有关更多信息，请参阅[确定在 Kibana 的“发现”页面中显示的数据](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data)。然后，修改缺省查询以过滤条目。

    **注**：使用 Lucene 查询语言来定义定制查询。有关更多信息，请参阅 [Apache Lucene - Query Parser Syntax ![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html){: new_window}
    
    如果 Kibana 是通过 {{site.data.keyword.Bluemix_notm}} UI 启动的，要修改查询并定义多个搜索条件，可以使用逻辑项 **AND** 和 **OR**。这些运算符必须为大写。    
    
    * 要搜索关键字或关键字的一部分，请输入词语并后跟星号通配符 (*)；例如，`Java*`。 
    * 要搜索特定短语，请输入该短语并用双引号 (" ") 括起；例如，`"Java/1.8.0"`。
    * 要创建更复杂的搜索，可以使用逻辑项 AND 和 OR；例如，`"Java/1.8.0" OR "Java/1.7.0"`。
    * 要搜索特定字段内的值，请输入以下格式的搜索：*log_field_name:search_term*；例如，`instance_id:"1"`。
    * 要搜索特定日志字段内某一范围的值，请输入以下格式的搜索：*log_field_name:[start_of_range TO end_of_range]*；例如，`instance_id:["1" TO "2"]`。

     例如，对于 CF 应用程序，可以创建查询 `application_id:9d222152-8834-4bab-8685-3036cd25931a AND instance_id:["0" TO "1"]`，此查询中仅列出实例 *0* 和 *1* 的条目。 

3. 保存查询，以便将来可以复用。有关更多信息，请参阅[保存搜索](/docs/services/CloudLogAnalysis/kibana/define_search.html#save_search1)。 

**注**：如果需要删除查询，请参阅[删除搜索](/docs/services/CloudLogAnalysis/kibana/define_search.html#delete_search)。



## 删除搜索
{: #delete_search}

要删除搜索，请在“设置”页面中完成以下步骤：

1. 在“设置”页面中，选择**对象**选项卡。

2. 在**搜索**选项卡中，选择要删除的搜索。

3. 单击**删除**。


## 导出搜索
{: #export_search}

要导出搜索，请在“设置”页面中完成以下步骤：

1. 在“设置”页面中，选择**对象**选项卡。

2. 在**搜索**选项卡中，选择要导出的搜索。

3. 单击**导出**。

4. 保存文件。

 
## 导入搜索
{: #import_search}

要导入搜索，请在“设置”页面中完成以下步骤：

1. 在“设置”页面中，选择**对象**选项卡。

2. 在**搜索**选项卡中，选择**导入**。

3. 选择文件并单击**打开**。

搜索将添加到搜索列表中。

## 刷新搜索内容
{: #refresh_search}

要手动刷新搜索内容，可以单击搜索栏中可用的放大镜。 

要自动刷新“发现”页面中显示的数据，可以配置刷新时间间隔。刷新时间间隔的当前值显示在“发现”页面的菜单栏中。缺省情况下，自动刷新设置为**关闭**。

要设置刷新时间间隔，请完成以下步骤：

1. 在“发现”页面中，单击菜单栏中可用的**时间过滤器**。

2. 单击**自动刷新** ![自动刷新](images/auto_refresh_icon.jpg "自动刷新")。

3. 从列表中选择刷新时间间隔。 

**注**：启用自动刷新时间间隔后，可以通过单击“暂停”按钮 ![暂停](images/auto_refresh_pause_icon.jpg "暂停") 暂停刷新。


## 重新装入搜索
{: #reload_search1}

要装入保存的搜索，请完成以下步骤：

1. 在“发现”页面的工具栏中，单击**装入搜索**按钮 ![装入搜索](images/load_icon.jpg "装入搜索")。

2. 选择要装入的搜索。 

## 开始新搜索
{: #k4_new_search}

要开始新搜索，请单击“发现”页面工具栏中的**新建搜索**按钮 ![新建搜索](images/new_search_icon.jpg "新建搜索")。

## 保存搜索 
{: #save_search1}

请考虑以下有关在 Kibana 中保存定制搜索的信息：

* 保存搜索时，将保存搜索查询字符串和当前所选的索引模式。
* 当您在*发现*页面中打开搜索并进行修改时，您可以选择使用相同的名称来保存搜索，也可以使用不同的名称来保存修改的定制搜索。缺省情况下，所提供的搜索名称是对应于您最初打开的定制搜索的名称。

    * 要使用相同的名称保存修改的定制搜索，请单击**保存**。请注意，这会覆盖原始定制搜索。 
	
	* 要使用不同的名称保存修改的定制搜索，请在**保存搜索**字段中输入新名称，然后单击**保存**。 


要保存“发现”页面中的当前搜索，请完成以下步骤：

1. 在“发现”页面的工具栏中，单击**保存搜索**按钮 ![保存搜索](images/save_search_icon.jpg "保存搜索")。

2. 输入搜索的名称。

    **注**：单击**保存**时，不会对覆盖发出警告，因此如果您指定现有的名称，保存将会替换该版本而没有任何提示信息。

3. 单击**保存**。 
