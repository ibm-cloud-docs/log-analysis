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


# 计算搜索配额和每日使用情况
{: #quota}

要获取 {{site.data.keyword.loganalysisshort}} 服务的日志域配额和当前每日使用情况，您可以运行 cURL 命令。
{:shortdesc}

## 使用 CLI 计算搜索配额和每日使用情况
{: #quota_cli}

请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}}。

    例如，要登录到美国南部，请运行以下命令：

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。

2. 运行 `ibmcloud logging quota-usage-show` CLI 命令。 

    ```
    ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE][-i,--resource-id RESOURCE_ID]
    ```
    {: codeblock}

    其中 

    * 有效的 RESOURCE_TYPE 值如下：space 和 account
    * RESOURCE_ID 是要获取其配额使用情况的帐户或空间的 GUID。


例如，要显示帐户的配额使用情况，请运行以下命令：

```
 ibmcloud logging quota-usage-show -r account -i 475693845023932019c6567c9c8de6dece
Showing quota usage for resource: 475693845023932019c6567c9c8de6dece ...
OK

Daily Allotmant   Current Usage   
524288000         0   
```
{: screen}

要显示空间的配额使用情况，请运行以下命令：

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Daily Allotmant   Current Usage   
524288000         6774014   
```
{: screen}


## 使用 CLI 获取搜索配额历史记录
{: #quota_history_cli}


请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}}。

    例如，要登录到美国南部，请运行以下命令：

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。

2. 运行带有 `-s` 参数的 `ibmcloud logging quota-usage-show` CLI 命令。 

    ```
    ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE][-i,--resource-id RESOURCE_ID] [-s,--history]
    ```
    {: codeblock}

    其中 

    * 有效的 RESOURCE_TYPE 值如下：space 和 account
    * RESOURCE_ID 是要获取其配额使用情况的帐户或空间的 GUID。

例如：

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744 -s
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Date         Allotmant   Usage   
2018.02.28   524288000   80405926   
2018.03.06   524288000   18955540   
2018.03.05   524288000   47262944   
2018.03.08   524288000   18311338   
2018.03.01   524288000   82416831   
2018.03.03   524288000   75045462   
2018.03.07   524288000   17386278   
2018.03.02   524288000   104316444   
2018.03.04   524288000   73125223   
```
{: screen}



## 使用 API 计算帐户的搜索配额和每日使用情况
{: #account}

请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}}。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。

2. 获取帐户的标识。运行以下命令：

    ```
	ibmcloud iam accounts
	```
    {: codeblock}	

	这将显示帐户及其 GUID 的列表。
	
	将帐户标识导出到 shell 变量。例如：
	
	```
	export AccountID="1234567891234567812341234123412"
	```
	{: screen}

3. 获取 UAA 令牌。 

    有关更多信息，请参阅[获取 UAA 令牌](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-auth_uaa#auth_uaa)。

    将 UAA 令牌导出到 shell 变量。请不要包含 `Bearer`。例如：
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. 获取域的配额和当前使用情况。运行以下命令：

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	其中，*ENDPOINT* 对于每个区域来说是不同的。有关每个区域的端点列表，请参阅[日志记录端点](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-manage_logs#endpoints)。
	
	例如，运行 cURL 命令以获取美国南部区域中帐户的配额：
	
	
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	结果包含每日配额和使用情况的相关信息。
	
	
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET https://logging.ng.bluemix.net/quota/usage
    HTTP/1.1 200 OK
    Server: nginx/1.10.3 (Ubuntu)
    Date: Wed, 29 Nov 2017 13:18:20 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 52
    Connection: keep-alive



   {
      "usage": {
        "dailyallotment": 524288000,
        "current": 2115811531
       }
    }
    ```
    {: screen}

	
## 使用 API 计算空间的搜索配额和每日使用情况
{: #space1}

请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}}。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。

2. 获取空间的标识。

    有关更多信息，请参阅[如何获取空间的 GUID](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#space_guid)。
	
	将空间标识导出到 shell 变量。例如：
	
	```
	export SpaceID="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

3. 获取 UAA 令牌。 

    有关更多信息，请参阅[获取 UAA 令牌](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-auth_uaa#auth_uaa)。

    将 UAA 令牌导出到 shell 变量。请不要包含 `Bearer`。例如：
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. 获取域的配额和当前使用情况。运行以下命令：

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	其中，*ENDPOINT* 对于每个区域来说是不同的。有关每个区域的端点列表，请参阅[日志记录端点](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-manage_logs#endpoints)。

    例如，运行以下 cURL 命令以获取美国南部区域中空间域的配额和使用情况：
	
    
	
    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	结果包含每日配额和使用情况的相关信息。
	
	
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET https://logging.ng.bluemix.net/quota/usage
    HTTP/1.1 200 OK
    Server: nginx/1.10.3 (Ubuntu)
    Date: Wed, 29 Nov 2017 13:18:20 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 52
    Connection: keep-alive

   {
      "usage": {
        "dailyallotment": 524288000,
        "current": 2115811531
       }
    }
    ```
    {: screen}



