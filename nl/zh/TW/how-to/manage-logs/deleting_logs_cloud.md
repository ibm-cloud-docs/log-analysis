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

# 刪除日誌
{: #deleting_logs}

請使用 [ibmcloud logging log-delete](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#delete) 指令，以從「日誌收集」中刪除日誌。
{:shortdesc}

* 您可以刪除特定時間範圍內的日誌。
* 您可以依類型刪除日誌。請注意，每一個日誌檔都只有一種類型的日誌項目。
* 您可以刪除空間、組織或帳戶網域中的日誌。


## 刪除特定一段時間內的所有日誌
{: #time_range}

請完成下列步驟，以刪除空間網域中特定一段時間內所儲存的所有日誌：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
    
2. 執行下列指令，以查看「日誌收集」中可用的日誌。

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    例如，
    
    ```
    $ ibmcloud logging log-show
    Showing log status of resource: 12345678-abcd-4193-aere-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    None                default
	2017-05-25   1224       76115   All                 linux_syslog,log
    2017-05-26   19663113   17639   All                 default,linux_syslog  
    ```
    {: screen}
	
3. 刪除特定日期所儲存的日誌。

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate
	```
	{: codeblock}
	
	其中
	
	* *-s* 設定「世界標準時間 (UTC)」格式的開始日期：YYYY-MM-DD（例如，2006-01-02）。
    * *-e* 設定「世界標準時間 (UTC)」格式的結束日期：YYYY-MM-DD
    	
	例如，若要刪除 2017 年 5 月 25 日的日誌，請執行下列指令：
	
	```
	ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25
	```
	{: screen}

	
## 依日誌類型刪除特定一段時間內的日誌 
{: #log_type}

請完成下列步驟，以依日誌類型刪除空間網域中特定一段時間內所儲存的日誌：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
    
2. 執行下列指令，以查看「日誌收集」中可用的日誌。

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    例如，
    
    ```
    $ ibmcloud logging log-show
    Showing log status of resource: 12345678-1234-2edr-a9de-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    None                default
	2017-05-25   1224       76115   All                 linux_syslog,log
    2017-05-26   19663113   17639   All                 default,linux_syslog  
    ```
    {: screen}
	
3. 刪除特定日期所儲存的日誌。

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate -t LogType
	```
	{: codeblock}
	
	其中
	
	* *-s* 設定「世界標準時間 (UTC)」格式的開始日期：YYYY-MM-DD（例如，2006-01-02）。
    * *-e* 設定「世界標準時間 (UTC)」格式的結束日期：YYYY-MM-DD
	* *-t* 設定日誌類型。
    	
	例如，若要刪除 2017 年 5 月 25 日類型為 linux_syslog 的日誌，請執行下列指令：
	
	```
	ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
	```
	{: screen}

		
	
## 依日誌類型刪除特定一段時間內的帳戶日誌 
{: #time_range_acc}

請完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
	
2. 取得帳戶 ID。

    如需相關資訊，請參閱[如何取得帳戶的 GUID](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid)。
    
3. 執行下列指令，以查看「日誌收集」中帳戶層次的可用日誌。

    ```
    ibmcloud logging log-show  -r account -i AccountID
    ```
    {: codeblock}
    
    例如，
    
    ```
    $ ibmcloud logging log-show -r account -i 123456789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: 123456789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    All                 default
	2017-05-25   2000       76115   All                 linux_syslog,log
    2017-05-26   195678     17639   All                 default,linux_syslog    
    Logs of resource 123456789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}
	
4. 刪除特定日期所儲存的日誌。

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate -t LogType -r account -i AccountID
	```
	{: codeblock}
	
	其中
	
	* *-s* 設定「世界標準時間 (UTC)」格式的開始日期：YYYY-MM-DD（例如，2006-01-02）。
    * *-e* 設定「世界標準時間 (UTC)」格式的結束日期：YYYY-MM-DD
	* *-t* 設定日誌類型。
    	
	例如，若要刪除 2017 年 5 月 25 日類型為 linux_syslog 且儲存在「日誌收集」中帳戶層次的日誌，請執行下列指令：
	
	```
	ibmcloud logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog -r account -i 123456789123456789567c9c8de6dece
	```
	{: screen}
	












