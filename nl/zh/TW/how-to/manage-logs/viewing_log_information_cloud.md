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

# 檢視日誌資訊
{: #viewing_log_status1}

請使用 [ibmcloud logging log-show](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#status) 指令，以取得「日誌收集」中所收集及儲存之日誌的相關資訊。您可以取得下列相關資訊：大小、記錄數目、日誌類型，以及日誌是否可用於 Kibana 分析。
{:shortdesc}

## 取得一段時間內的日誌相關資訊
{: #viewing_logs}

請使用 `ibmcloud logging log-show` 指令與 **-s** 選項搭配來設定開始日期，與 **-e** 選項搭配來設定結束日期。例如：

* `ibmcloud logging log-show` 提供過去 2 週的資訊。
* `ibmcloud logging log-show -s 2017-05-03` 提供從 2017 年 5 月 3 日到現行日期的資訊。
* `ibmcloud logging log-show -s 2017-05-03 -e 2017-05-08` 提供 2017 年 5 月 3 日與 2017 年 5 月 8 日之間的資訊。 

請完成下列步驟，以取得空間中所儲存日誌的相關資訊：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
    
2. 執行下列指令：

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    例如，
    
    ```
    $ ibmcloud logging log-show -s 2017-11-17 -e 2017-11-17
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size     Count   Searchable   Types   
    2017-11-17   794008   706     All          default   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}


## 取得一段時間內的某類型日誌相關資訊
{: #viewing_logs_by_log_type}

若要取得一段時間內某類型日誌的相關資訊，請使用 `ibmcloud logging log-show` 指令與 **-t** 選項搭配來指定日誌類型、與 **-s** 選項搭配來設定開始日期，以及與 **-e** 選項搭配來設定結束日期。例如，

* `ibmcloud logging log-show -t syslog` 提供類型為 *syslog* 之日誌過去 2 週的相關資訊。
* `ibmcloud logging log-show -s 2017-05-03 -t syslog` 提供類型為 *syslog* 之日誌從 2017 年 5 月 3 日到現行日期的相關資訊。
* `ibmcloud logging log-show -s 2017-05-03 -e 2017-05-08 -t syslog` 提供類型為 *syslog* 之日誌在 2017 年 5 月 3 日與 2017 年 5 月 8 日之間的相關資訊。 

請完成下列步驟，以取得一段時間內某類型日誌的相關資訊：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
    
2. 執行下列指令：

    ```
    ibmcloud logging log-show -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    其中
    
    * *-s* 用來設定「世界標準時間 (UTC)」格式的開始日期：*YYYY-MM-DD*
    * *-e* 用來設定「世界標準時間 (UTC)」格式的結束日期：*YYYY-MM-DD*
    * *-t* 用來設定日誌類型。
    
    您可以指定多種日誌類型，作法是使用逗點來區隔每一種類型，例如，**log_type_1,log_type_2,log_type_3**。 
    
    例如，
    
    ```
    $ ibmcloud logging log-show -s 2017-05-24 -e 2017-05-25 -t syslog
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size     Count   Searchable   Types   
    2017-11-17   794008   706     All          syslog   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}



## 取得帳戶層次之日誌的相關資訊
{: #viewing_logs_account}

若要取得帳戶層次上一段時間內可用日誌的相關資訊，請使用 `ibmcloud logging log-show` 指令與 **-r account** 及 **-i** 選項搭配來設定帳戶的 ID。您也可以指定 **-t** 選項來指定日誌類型、指定 **-s** 選項來設定開始日期，以及指定 **-e** 選項來設定結束日期。 

請完成下列步驟，以取得日誌的相關帳戶資訊：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
	
2. 取得帳戶 ID。

    如需相關資訊，請參閱[如何取得帳戶的 GUID](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid)。
    
3. 執行下列指令：

    ```
    ibmcloud logging log-show -r account -i AccountID -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    其中
    
    * *-r account* 是用來設定您要取得日誌相關資訊的網域。
    * *-i AccountID* 是用來設定帳戶的 ID。
    * *-s* 用來設定「世界標準時間 (UTC)」格式的開始日期：*YYYY-MM-DD*
    * *-e* 用來設定「世界標準時間 (UTC)」格式的結束日期：*YYYY-MM-DD*
    * *-t* 用來設定日誌類型。

    您可以指定多種日誌類型，作法是使用逗點來區隔每一種類型，例如，**log_type_1,log_type_2,log_type_3**。 
 
    例如，若要顯示帳戶 *123456789123456789567c9c8de6dece* 之帳戶網域上針對 2017 年 11 月 17 日所儲存日誌的相關資訊，請執行下列指令：
    
    ```
    $ ibmcloud logging log-show -r account -i 123456789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: 123456789123456789567c9c8de6dece ...

    Date         Size      Count   Searchable   Types   
	2017-11-17   794008    200     All          syslog  
    Logs of resource 123456789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}


## 取得組織層次之日誌的相關資訊
{: #viewing_logs_org}

若要取得組識層次上一段時間內可用日誌的相關資訊，請使用 `ibmcloud logging log-show` 指令與 **-r org** 及 **-i** 選項搭配來設定組織的 ID。您也可以指定 **-t** 選項來指定日誌類型、指定 **-s** 選項來設定開始日期，以及指定 **-e** 選項來設定結束日期。 

請完成下列步驟，以取得日誌的相關帳戶資訊：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
	
2. 取得帳戶 ID。

    如需相關資訊，請參閱[如何取得組織的 GUID](/docs/services/CloudLogAnalysis/qa/cli_qa.html#org_guid)。
    
3. 執行下列指令：

    ```
    ibmcloud logging log-show -r org -i OrgID -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    其中
    
    * *-r org* 是用來設定您要取得日誌相關資訊的網域。
    * *-i OrgID* 是用來設定組織的 ID。
    * *-s* 用來設定「世界標準時間 (UTC)」格式的開始日期：*YYYY-MM-DD*
    * *-e* 用來設定「世界標準時間 (UTC)」格式的結束日期：*YYYY-MM-DD*
    * *-t* 用來設定日誌類型。
    
    您可以指定多種日誌類型，作法是使用逗點來區隔每一種類型，例如，**log_type_1,log_type_2,log_type_3**。 
 
    例如，若要顯示 ID 為 *abcd56789123456789567c9c8de6dece* 之組織的組織網域上針對 2017 年 11 月 17 日所儲存日誌的相關資訊，請執行下列指令：
    
    ```
    $ ibmcloud logging log-show -r org -i abcd56789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: abcd56789123456789567c9c8de6dece ...

    Date         Size      Count   Searchable   Types   
	2017-11-17   794008    200     All          syslog  
    Logs of resource abcd56789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}








