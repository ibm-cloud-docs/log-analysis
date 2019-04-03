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

# 配置日志保留时间策略
{: #configuring_retention_policy}

缺省情况下，会禁用保留时间策略，且日志会无限期保留。使用 **ibmcloud logging option-update** 命令更改保留时间策略。
{:shortdesc}

可以使用 **ibmcloud logging option-show** 命令来查看保留时间策略，此策略用于定义日志在“日志收集”中保留的最长天数。 

如果设置了保留时间策略，那么在保留期到期后，会自动删除日志。


## 禁用帐户的日志保留时间策略
{: #disable_retention_policy_acc}

禁用保留时间策略时，会保留所有日志。 

要禁用保留时间策略，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
	
2. 获取帐户标识。

    有关更多信息，请参阅[如何获取帐户的 GUID](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid)。
    
3. 将保留期设置为 **-1** 以禁用保留期。运行以下命令：

    ```
    ibmcloud logging option-update -r account -i AccountID -e RETENTION_VALUE
	```
    {: codeblock}
	
	RETENTION_VALUE 是用于定义天数的数字。


    
**示例**
    
例如，要禁用标识为 *12345677fgh436902a3* 的帐户的保留期，请运行以下命令：

```
ibmcloud logging option-update -r account -i 12345677fgh436902a3 -e -1
```
{: codeblock}


## 禁用空间的日志保留时间策略
{: #disable_retention_policy_space}

禁用保留时间策略时，会保留所有日志。  

要禁用保留时间策略，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 将保留期设置为 **-1** 以禁用保留期。运行以下命令：

    ```
    ibmcloud logging option-show -e RETENTION_VALUE
	```
    {: codeblock}
	
	RETENTION_VALUE 是用于定义天数的数字。


    
**示例**
    
例如，要禁用标识为 *d35da1e3-b345-475f-8502-cfgh436902a3* 的空间的保留期，请运行以下命令：

```
ibmcloud logging option-update -e -1
```
{: codeblock}


## 检查帐户的日志保留时间策略
{: #check_retention_policy_acc}

要获取为帐户设置的保留期，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。

2. 获取帐户标识。

    有关更多信息，请参阅[如何获取帐户的 GUID](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid)。
    
3. 获取保留期。运行以下命令：

    ```
    ibmcloud logging option-show -r account -i AccountID
    ```
    {: codeblock}

    输出为：

    ```
    ibmcloud logging option-show -r account -i kjskdsjfksjdflkjdsfbbd06461b066
    Showing log options of resource: kjskdsjfksjdflkjdsfbbd06461b066 ...

    Resource ID                              Retention   
    a:kjskdsjfksjdflkjdsfbbd06461b066       30   
	```
    {: screen}
	
## 检查空间的日志保留时间策略
{: #check_retention_policy_space}

要获取为空间设置的保留期，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 获取保留期。运行以下命令：

    ```
    ibmcloud logging option-show
    ```
    {: codeblock}

    输出为：

    ```
    ibmcloud logging option-show
    Showing log options of resource: 12345678-1234-2edr-a9de-378620d6fab5 ...

    SpaceId                                Retention   
    12345678-1234-2edr-a9de-378620d6fab5   30   
	```
    {: screen}
    


## 设置帐户级别的日志保留时间策略
{: #set_retention_policy_acc}

请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。

2. 获取帐户标识。

    有关更多信息，请参阅[如何获取帐户的 GUID](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid)。
    
3. 设置保留期。运行以下命令：

    ```
    ibmcloud logging option-update -r account -i AccountID -e RETENTION_VALUE
    ```
    {: codeblock}
    
    其中，*RETENTION_VALUE* 是整数，用于定义要保留日志的天数。 
    
    
**示例**
    
例如，要使帐户中任何类型的日志仅保留 15 天，请运行以下命令：

```
ibmcloud logging option-update -r account -i AccountID -e 15
```
{: codeblock}



## 设置空间的日志保留时间策略
{: #set_retention_policy_space}

要查看空间的保留期，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 设置保留期。运行以下命令：

    ```
    ibmcloud logging option-update -e RETENTION_VALUE
    ```
    {: codeblock}
    
    其中，*RETENTION_VALUE* 是整数，用于定义要保留日志的天数。
    
    
**示例**
    
例如，要使空间中可用的日志保留 1 年，请运行以下命令：

```
ibmcloud logging option-update -e 365
```
{: codeblock}




