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


# 計算搜尋配額及每日用量
{: #quota}

若要取得 {{site.data.keyword.loganalysisshort}} 服務之日誌網域的配額及現行每日用量，您可以執行 cURL 指令。
{:shortdesc}

## 使用 CLI 計算搜尋配額及每日用量
{: #quota_cli}

請完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}}。

    例如，若要登入「美國南部」，請執行以下指令：

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。

2. 執行 `ibmcloud logging quota-usage-show` CLI 指令。 

    ```
    ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE][-i,--resource-id RESOURCE_ID]
    ```
    {: codeblock}

    其中 

    * 有效的 RESOURCE_TYPE 值如下：space、account
    * RESOURCE_ID 是您要取得配額用量的帳戶或空間的 GUID。


例如，若要顯示帳戶的配額用量，請執行下列指令：

```
 ibmcloud logging quota-usage-show -r account -i 475693845023932019c6567c9c8de6dece
Showing quota usage for resource: 475693845023932019c6567c9c8de6dece ...
OK

Daily Allotmant   Current Usage   
524288000         0   
```
{: screen}

若要顯示空間的配額用量，請執行下列指令：

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Daily Allotmant   Current Usage   
524288000         6774014   
```
{: screen}


## 使用 CLI 取得搜尋配額歷程
{: #quota_history_cli}


請完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}}。

    例如，若要登入「美國南部」，請執行以下指令：

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。

2. 執行 `ibmcloud logging quota-usage-show` CLI 指令，並搭配參數 `-s`。 

    ```
    ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE][-i,--resource-id RESOURCE_ID] [-s,--history]
    ```
    {: codeblock}

    其中 

    * 有效的 RESOURCE_TYPE 值如下：space、account
    * RESOURCE_ID 是您要取得配額用量的帳戶或空間的 GUID。

例如，

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



## 使用 API 計算帳戶的搜尋配額及每日用量
{: #account}

請完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}}。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。

2. 取得帳戶的 ID。執行下列指令：

    ```
	ibmcloud iam accounts
	```
    {: codeblock}	

	即會顯示帳戶及其 GUID 的清單。
	
	將帳戶 ID 匯出至 Shell 變數。例如：
	
	```
	export AccountID="1234567891234567812341234123412"
	```
	{: screen}

3. 取得 UAA 記號。 

    如需相關資訊，請參閱[取得 UAA 記號](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa)。

    將 UAA 記號匯出至 Shell 變數。請不要包括 `Bearer`。例如：
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. 取得網域的配額及現行用量。執行下列指令：

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	其中，每個地區的 *ENDPOINT* 都不同。如需每個地區的端點清單，請參閱[記載端點](/docs/services/CloudLogAnalysis/manage_logs.html#endpoints)。
	
	例如，執行 cURL 指令，以取得美國南部地區中帳戶的配額：
	
	```
curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	此結果會包括每日配額及用量的相關資訊。
	
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

	
## 使用 API 計算空間的搜尋配額及每日用量
{: #space1}

請完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}}。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。

2. 取得空間的 ID。

    如需相關資訊，請參閱[如何取得空間的 GUID](/docs/services/CloudLogAnalysis/qa/cli_qa.html#space_guid)。
	
	將空間 ID 匯出至 Shell 變數。例如：
	
	```
	export SpaceID="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

3. 取得 UAA 記號。 

    如需相關資訊，請參閱[取得 UAA 記號](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa)。

    將 UAA 記號匯出至 Shell 變數。請不要包括 `Bearer`。例如：
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. 取得網域的配額及現行用量。執行下列指令：

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	其中，每個地區的 *ENDPOINT* 都不同。如需每個地區的端點清單，請參閱[記載端點](/docs/services/CloudLogAnalysis/manage_logs.html#endpoints)。

    例如，執行下列 cURL 指令，以取得美國南部地區中空間網域的配額及用量：
	
    ```
curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	此結果會包括每日配額及用量的相關資訊。
	
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



