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
{: #deleting_logs1}

請使用 [ibmcloud cf logging delete](/docs/services/CloudLogAnalysis/reference/logging_cli.html#status1) 指令，以從「日誌收集」中刪除日誌。
{:shortdesc}

* 您可以刪除特定時間範圍內的日誌。
* 您可以依類型刪除日誌。請注意，每一個日誌檔都只有一種類型的日誌項目。
* 您可以刪除空間或帳戶網域中的日誌。


## 刪除特定一段時間內的日誌
{: #fix_period}

請完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
    
2. 執行 *status* 指令，以查看「日誌收集」中可用的日誌。

    ```
    ibmcloud cf logging status
    ```
    {: codeblock}
    
    例如，
    
    ```
    $ ibmcloud cf logging status
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 | linux_syslog,log   |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}
	
3. 刪除特定日期所儲存的日誌。

    ```
	ibmcloud cf logging delete -s StartDate -e EndDate
	```
	{: codeblock}
	
	其中
	
	* *-s* 設定「世界標準時間 (UTC)」格式的開始日期：YYYY-MM-DD（例如，2006-01-02）。
    * *-e* 設定「世界標準時間 (UTC)」格式的結束日期：YYYY-MM-DD
    	
	例如，若要刪除 2017 年 5 月 25 日的日誌，請執行下列指令：
	
	```
	ibmcloud cf logging delete -s 2017-05-25 -e 2017-05-25
	```
	{: screen}

	
## 依日誌類型刪除特定一段時間內的日誌 
{: #log_type1}

請完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
    
2. 執行 *status* 指令，以查看「日誌收集」中可用的日誌。

    ```
    ibmcloud cf logging status
    ```
    {: codeblock}
    
    例如，
    
    ```
    $ ibmcloud cf logging status
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 | linux_syslog,log   |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}
	
3. 刪除特定日期所儲存的日誌。

    ```
	ibmcloud cf logging delete -s StartDate -e EndDate -t LogType
	```
	{: codeblock}
	
	其中
	
	* *-s* 設定「世界標準時間 (UTC)」格式的開始日期：YYYY-MM-DD（例如，2006-01-02）。
    * *-e* 設定「世界標準時間 (UTC)」格式的結束日期：YYYY-MM-DD
	* *-t* 設定日誌類型。
    	
	例如，若要刪除 2017 年 5 月 25 日類型為 linux_syslog 的日誌，請執行下列指令：
	
	```
	ibmcloud cf logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
	```
	{: screen}

		
	
## 依日誌類型刪除特定一段時間內的帳戶日誌 
{: #acc_log_type}

請完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
    
2. 執行 *status* 指令，以查看「日誌收集」中帳戶層次的可用日誌。

    ```
    ibmcloud cf logging status  -a
    ```
    {: codeblock}
    
    例如，
    
    ```
    $ ibmcloud cf logging status -a
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 | linux_syslog,log   |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}
	
3. 刪除特定日期所儲存的日誌。

    ```
	ibmcloud cf logging delete -s StartDate -e EndDate -t LogType -a
	```
	{: codeblock}
	
	其中
	
	* *-s* 設定「世界標準時間 (UTC)」格式的開始日期：YYYY-MM-DD（例如，2006-01-02）。
    * *-e* 設定「世界標準時間 (UTC)」格式的結束日期：YYYY-MM-DD
	* *-t* 設定日誌類型。
    	
	例如，若要刪除 2017 年 5 月 25 日類型為 linux_syslog 且儲存在「日誌收集」中帳戶層次的日誌，請執行下列指令：
	
	```
	ibmcloud cf logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog -a
	```
	{: screen}
	












