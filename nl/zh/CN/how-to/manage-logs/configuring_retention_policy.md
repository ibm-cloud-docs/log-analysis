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
{: #configuring_retention_policy1}

使用 **cf logging option** 命令可查看和配置保留时间策略，此策略用于定义日志在“日志收集”中保留的最长天数。缺省情况下，会禁用保留时间策略，且日志会无限期保留。在保留期到期后，会自动删除日志。
{:shortdesc}

您可在帐户中定义不同的保留时间策略。您可以有一个全局帐户策略和单独的空间策略。在帐户级别设置的保留时间策略用于设置可以保留日志的最长天数。如果设置空间保留时间策略时使用的时间段长于帐户级别的时间段，那么应用的策略是为该空间配置的最后一个策略。 


## 禁用空间的日志保留时间策略
{: #disable_retention_policy_space1}

要禁用保留时间策略，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 将保留期设置为 **-1** 以禁用保留期。运行以下命令：

    ```
    ibmcloud cf logging option -r -1
    ```
    {: codeblock}
    
**示例**
    
例如，要禁用标识为 *d35da1e3-b345-475f-8502-cfgh436902a3* 的空间的保留期，请运行以下命令：

```
ibmcloud cf logging option -r -1
```
{: codeblock}

输出为：

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |        -1 |
+--------------------------------------+-----------+
```
{: screen} 



## 检查空间的日志保留时间策略
{: #check_retention_policy_space1}

要获取为空间设置的保留期，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 获取保留期。运行以下命令：

    ```
    ibmcloud cf logging option
    ```
    {: codeblock}

    输出为：

    ```
    +--------------------------------------+-----------+
    |               SPACEID                | RETENTION |
    +--------------------------------------+-----------+
    | d35da1e3-b345-475f-8502-cfgh436902a3 |        30 |
    +--------------------------------------+-----------+
    ```
    {: screen}
    

## 检查帐户中所有空间的日志保留时间策略
{: #check_retention_policy_account}

要获取为帐户中每个空间设置的保留期，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 获取帐户中每个空间的保留期。运行以下命令：

    ```
    ibmcloud cf logging option -a
    ```
    {: codeblock}

    输出为：

    ```
    +--------------------------------------+-----------+
    |               SPACEID                | RETENTION |
    +--------------------------------------+-----------+
    | d35da1e3-b345-475f-8502-cfgh436902a3 |        30 |
    +--------------------------------------+-----------+
    | fdew45e3-b345-4365-8502-cfghrfthy5a3 |        30 |
    +--------------------------------------+-----------+
    ```
    {: screen}
    

## 设置帐户级别的日志保留时间策略
{: #set_retention_policy_space1}

要查看帐户的保留期，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 设置保留期。运行以下命令：

    ```
    ibmcloud cf logging option -r *Number_of_days* - a
    ```
    {: codeblock}
    
    其中，*Number_of_days* 是整数，用于定义要保留日志的天数。 
    
    
**示例**
    
例如，要使帐户中任何类型的日志仅保留 15 天，请运行以下命令：

```
ibmcloud cf logging option -r 15 -a
```
{: codeblock}

输出列出了帐户中每个空间的条目，包括有关保留期的信息：

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |        15 |
+--------------------------------------+-----------+
| fdew45e3-b345-4365-8502-cfghrfthy5a3 |        30 |
+--------------------------------------+-----------+
```
{: screen}

## 设置空间的日志保留时间策略
{: #set_retention_policy_account}

要查看空间的保留期，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 设置保留期。运行以下命令：

    ```
    ibmcloud cf logging option -r *Number_of_days*
    ```
    {: codeblock}
    
    其中，*Number_of_days* 是整数，用于定义要保留日志的天数。
    
    
**示例**
    
例如，要使空间中可用的日志保留 1 年，请运行以下命令：

```
ibmcloud cf logging option -r 365
```
{: codeblock}

输出为：

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |       365 |
+--------------------------------------+-----------+
```
{: screen}


