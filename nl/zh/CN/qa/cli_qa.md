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


# 使用 IBM Cloud CLI 的常见问题及解答
{: #cli_qa}

下面是对有关使用 {{site.data.keyword.Bluemix}} CLI 与 {{site.data.keyword.loganalysisshort}} 服务的常见问题的解答。
{:shortdesc}

* [如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
* [如何安装 {{site.data.keyword.Bluemix_notm}} CLI](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#install_bmx_cli)
* [如何获取帐户的 GUID](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid)
* [如何获取组织的 GUID](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#org_guid)
* [如何获取空间的 GUID](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#space_guid)

## 如何登录到 IBM Cloud？
{: #login}

运行以下命令，以登录到 {{site.data.keyword.Bluemix_notm}} 中 {{site.data.keyword.loganalysisshort}} 服务可用的区域：

```
ibmcloud login -a Endpoint
```
{: codeblock}
	
其中，*Endpoint* 是用于登录到 {{site.data.keyword.Bluemix_notm}} 的 URL。对于每个区域，此 URL 是不同的。
	
<table>
    <caption>用于访问 {{site.data.keyword.Bluemix_notm}} 的端点的列表</caption>
	<tr>
	  <th>区域</th>
	  <th>URL</th>
	</tr>
	<tr>
	  <td>德国</td>
	  <td>api.eu-de.bluemix.net</td>
	</tr>
	<tr>
	  <td>悉尼</td>
	  <td>api.au-syd.bluemix.net</td>
	</tr>
	<tr>
	  <td>美国南部</td>
	  <td>api.ng.bluemix.net</td>
	</tr>
	<tr>
	  <td>英国</td>
	  <td>api.eu-gb.bluemix.net</td>
	</tr>
</table>

例如，要登录到美国南部区域，请运行以下命令：
	
```
ibmcloud login -a https://api.ng.bluemix.net
```
{: codeblock}

遵循指示信息进行操作。 

您还可以设置组织和空间。运行以下命令：

```
ibmcloud target -o OrgName -s SpaceName
```
{: codeblock}

其中

* OrgName 是组织的名称。
* SpaceName 是空间的名称。

	
	
## 如何安装 IBM Cloud CLI？
{: #install_bmx_cli}

请参阅[下载并安装 {{site.data.keyword.Bluemix}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)。



## 如何获取帐户的 GUID
{: #account_guid}
	
要获取帐户的 GUID，请完成以下步骤：
	
1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
	
2. 运行 `ibmcloud iam accounts` 命令以获取帐户的 GUID。

    ```
	ibmcloud iam accounts
	```
	{: codeblock} 
	
	例如，要针对用户 xxx@yyy.com 检索所有帐户及其相应的 GUID，请运行命令：
	
	
	```
	ibmcloud iam accounts
	Retrieving all accounts of xxx@yyy.com...
    OK
    Account GUID                       Name                               Type    State    Owner User ID   
    12345123451234512345123451234512   A Account                          TRIAL   ACTIVE   xxx@yyy.com   
    23456234562345622456234561234561   B Account                          TRIAL   ACTIVE   zzz@yyy.com   
	```
	{: screen}

	
## 如何获取组织的 GUID
{: #org_guid}

要获取组织的 GUID，请完成以下步骤：
	
1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。

2. 运行 `ibmcloud iam org` 命令来获取组织 GUID。 

    ```
    ibmcloud iam org NAME --guid
    ```
    {: codeblock}
	
    其中，NAME 是 {{site.data.keyword.Bluemix_notm}} 组织的名称。        
		
		
		
## 如何获取空间的 GUID
{: #space_guid2}
	
完成以下步骤，以获取空间的 GUID：
	

	
1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
	
2. 运行 `ibmcloud iam space` 命令来获取空间 GUID。 

    ```
    ibmcloud iam space NAME --guid
    ```
    {: codeblock}
	
    其中，NAME 是 {{site.data.keyword.Bluemix_notm}} 空间的名称。
	
     
	
    例如，要获取空间 *dev* 的 GUID，请运行以下命令：
	
    ```
    ibmcloud iam space dev --guid
    e03afff1-3456-4af6-1234-59treg1b0abc
    ```
    {: screen}




		
		
