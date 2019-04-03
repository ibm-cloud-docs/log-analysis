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
{: #viewing_log_status}

使用 [cf logging status](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-logging_cli#status1) 指令，以取得「日誌收集」中所收集及儲存之日誌的相關資訊。
{:shortdesc}

## 取得一段時間內的日誌相關資訊
{: #viewing_logs1}

使用 `cf logging status` 指令，以查看「日誌收集」中所儲存日誌的大小、計數和日誌類型，以及是否可在 Kibana 中分析日誌。 

使用 `cf logging status` 指令與 **-s** 選項搭配來設定開始日期，與 **-e** 選項搭配來設定結束日期。例如：

* `cf logging status` 提供過去 2 週的資訊。
* `cf logging status -s 2017-05-03` 提供從 2017 年 5 月 3 日到現行日期的資訊。
* `cf logging status -s 2017-05-03 -e 2017-05-08` 提供 2017 年 5 月 3 日與 2017 年 5 月 8 日之間的資訊。 

請完成下列步驟，以取得日誌的相關資訊：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 執行 *status* 指令。

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


## 取得一段時間內的某類型日誌相關資訊
{: #viewing_logs_by_log_type1}

若要取得一段時間內的某類型日誌相關資訊，請使用 `cf logging status` 指令與 **-t** 選項搭配來指定日誌類型、與 **-s** 選項搭配來設定開始日期，以及與 **-e** 選項搭配來設定結束日期。例如，

* `cf logging status -t syslog` 提供類型為 *syslog* 之日誌過去 2 週的相關資訊。
* `cf logging status -s 2017-05-03 -t syslog` 提供類型為 *syslog* 之日誌從 2017 年 5 月 3 日到現行日期的相關資訊。
* `cf logging status -s 2017-05-03 -e 2017-05-08 -t syslog` 提供類型為 *syslog* 之日誌在 2017 年 5 月 3 日與 2017 年 5 月 8 日之間的相關資訊。 

請完成下列步驟，以取得一段時間內某類型日誌的相關資訊：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 執行 *status* 指令。

    ```
    ibmcloud cf logging status -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    其中
    
    * *-s* 用來設定「世界標準時間 (UTC)」格式的開始日期：*YYYY-MM-DD*
    * *-e* 用來設定「世界標準時間 (UTC)」格式的結束日期：*YYYY-MM-DD*
    * *-t* 用來設定日誌類型。
    
    您可以指定多種日誌類型，作法是使用逗點來區隔每一種類型，例如，**log_type_1,log_type_2,log_type_3**。 
    
    例如，
    
    ```
    $ ibmcloud cf logging status -s 2017-05-24 -e 2017-05-25 -t log
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 |        log         |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}



## 取得有關日誌的帳戶資訊
{: #viewing_logs_account1}

若要取得 {{site.data.keyword.Bluemix_notm}} 帳戶一段時間內的日誌相關資訊，請使用 `cf logging status` 指令與 **-a** 選項搭配。您也可以指定 **-t** 選項來指定日誌類型、指定 **-s** 選項來設定開始日期，以及指定 **-e** 選項來設定結束日期。 

請完成下列步驟，以取得日誌的相關帳戶資訊：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 執行 *status* 指令。

    ```
    ibmcloud cf logging status -a -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    其中
    
    * *-a* 用來指定帳戶層次資訊
    * *-s* 用來設定「世界標準時間 (UTC)」格式的開始日期：*YYYY-MM-DD*
    * *-e* 用來設定「世界標準時間 (UTC)」格式的結束日期：*YYYY-MM-DD*
    * *-t* 用來設定日誌類型。
    

    您可以指定多種日誌類型，作法是使用逗點來區隔每一種類型，例如，**log_type_1,log_type_2,log_type_3**。 
 
    例如，
    
    ```
    $ ibmcloud cf logging status -s 2017-05-24 -e 2017-05-25 -t log -a
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 |        log         |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}














