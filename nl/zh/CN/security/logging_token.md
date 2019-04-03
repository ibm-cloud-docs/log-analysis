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


# 获取日志记录令牌
{: #logging_token}

获取日志记录令牌以将日志发送到 {{site.data.keyword.loganalysisshort}} 服务。
{:shortdesc}


## 使用 {{site.data.keyword.loganalysisshort}} CLI 获取日志记录令牌以向空间发送日志 
{: #logging_token_la_cloud_cli}

要获取您可用于向 {{site.data.keyword.loganalysisshort}} 服务发送日志的日志记录令牌，请完成以下步骤：

1. 安装 {{site.data.keyword.Bluemix_notm}} CLI。

   有关更多信息，请参阅[下载并安装 {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)。
   
   如果 CLI 已安装，请继续执行下一步。
    
2. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
	
3. 运行以下命令：

    ```
	ibmcloud logging token-get
	```
	{: codeblock}

输出会返回日志记录令牌。


## 使用 {{site.data.keyword.Bluemix_notm}} CLI 获取日志记录令牌以向空间发送日志 
{: #logging_token_cloud_cli}

要获取您可用于向 {{site.data.keyword.loganalysisshort}} 服务发送日志的日志记录令牌，请完成以下步骤：

1. 安装 {{site.data.keyword.Bluemix_notm}} CLI。

   有关更多信息，请参阅[下载并安装 {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)。
   
   如果 CLI 已安装，请继续执行下一步。
    
2. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
	
3. 在供应 {{site.data.keyword.loganalysisshort}} 服务的空间中创建服务密钥。运行以下命令：

    

    列出服务以获取空间中 {{site.data.keyword.loganalysisshort}} 实例的名称：
	
    ```
	ibmcloud service list
	```
	{: codeblock}
	
	例如：
	
	```
	ibmcloud service list
    Invoking 'cf services'...

    Getting services in org lopezdsr_org / space dev as xxx@yyyy...
    OK

    

    name              service          plan       bound apps   last operation
    Log Analysis-vg   ibmloganalysis   standard                create succeeded
    ```
	{: screen}
	
	创建密钥。对 servicename 使用 **name** 值并输入您密钥的名称。
	
	```
	ibmcloud service key-create servicename KeyName 
	```
	{: codeblock}
	
	例如：
	
	```
	ibmcloud service key-create "Log Analysis-vg" mykey2
    Invoking 'cf create-service-key Log Analysis-vg mykey2'...

    Creating service key mykey2 for service instance Log Analysis-vg as xxx@yyyy...
    OK
    ```
	{: screen}
	
4. 获取日志记录令牌。运行以下命令：
	
	```
	ibmcloud service key-show name Keyname
	```
	{: codeblock}
	
	例如： 
	
	```
	ibmcloud service key-show "Log Analysis-vg" "mykey2" 
    Invoking 'cf service-key Log Analysis-vg mykey2'...

    Getting key mykey2 for service instance Log Analysis-vg as xxx@yyyy...

    {
     "LOG_INGESTION_MTLJ_URL": "https://ingest-eu-fra.logging.bluemix.net:9091",
     "logging_token": "sdtghyrtfde4",
     "space_id": "12345678-avfg-erft-b1f2-2efrtgcb1744"
    }
    ```
	{: screen}
	
	要获取日志记录令牌，您可以运行以下命令：
	
	```
	ibmcloud service key-show "Log Analysis-vg" "mykey2" | tail -n +4 | jq -r .logging_token
    sdtghyrtfde4
	```
	{: screen}


	
## 使用 Log Analysis API 获取日志记录令牌以向空间发送日志
{: #logging_token_api}


要获取您可用于向 {{site.data.keyword.loganalysisshort}} 服务发送日志的日志记录令牌，请完成以下步骤：

1. 安装 {{site.data.keyword.Bluemix_notm}} CLI。

   有关更多信息，请参阅[下载并安装 {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)。
   
   如果 CLI 已安装，请继续执行下一步。
    
2. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
	
3. 获取 [UAA 令牌](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-auth_uaa#uaa_cli)。

    例如，运行 `ibmcloud cf oauth-token` 命令以获取 UAA 令牌。

    ```
	ibmcloud cf oauth-token
	```
	{: codeblock}
	
	输出返回您在该空间和组织中认证用户标识时必须使用的 UAA 令牌。



4. 获取空间的 GUID。

   有关更多信息，请参阅[如何获取空间的 GUID](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#space_guid2)。  
	
5. 导出以下变量：TOKEN 和 SPACEID。

    * *TOKEN* 是上一步中获取的 oauth 令牌（不包含 Bearer）。
	
	* *SPACEID* 是上一步中获取的空间 GUID。 
		
	例如：
	
	```
	export TOKEN="eyJhbGciOiJI....cGFzc3dvcmQiLCJjZiIsInVhYSIsIm9wZW5pZCJdfQ.JaoaVudG4jqjeXz6q3JQL_SJJfoIFvY8m-rGlxryWS8"
	export SPACEID="667fb895-abcd-defg-aaaa-cf4587341095"
	```
	{: screen}
	
6. 获取日志记录令牌。运行以下命令：
 
    ```
	curl -k -X GET  --header "X-Auth-Token: ${TOKEN}"  --header "X-Auth-Project-Id: s-${SPACEID}"  LOGGING_ENDPOINT/token
    ```
    {: codeblock}	
	
	其中
	* SPACEID 是服务运行所在空间的 GUID。
	* TOKEN 是上一步中获取的 UAA 令牌，不带 Bearer 前缀。
	* LOGGING_ENDPOINT 是组织和空间所在的 {{site.data.keyword.Bluemix_notm}} 区域的 {{site.data.keyword.loganalysisshort}} 端点。每个区域的 LOGGING_ENDPOINT 不同。要查看不同端点的 URL，请参阅[端点](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-manage_logs#endpoints)。
	
    该命令返回您向该空间发送日志时必须使用的日志记录令牌。 	

	
