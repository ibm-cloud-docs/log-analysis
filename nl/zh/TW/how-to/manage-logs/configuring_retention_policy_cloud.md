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

# 配置日誌保留原則
{: #configuring_retention_policy}

依預設，會停用保留原則，並無限期保留日誌。使用指令 **ibmcloud logging option-update** 可變更保留原則。
{:shortdesc}

您可以使用 **ibmcloud logging option-show** 指令來檢視保留原則，而此保留原則定義將日誌保留在「日誌收集」中的天數上限。 

當您設定保留原則時，在保留期間到期之後，會自動刪除日誌。


## 停用帳戶的日誌保留原則
{: #disable_retention_policy_acc}

當您停用保留原則時，會保留所有日誌。 

請完成下列步驟，以停用保留原則：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
	
2. 取得帳戶 ID。

    如需相關資訊，請參閱[如何取得帳戶的 GUID](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid)。
    
3. 將保留期間設為 **-1**，以停用保留期間。執行下列指令：

    ```
    ibmcloud logging option-update -r account -i AccountID -e RETENTION_VALUE
	```
    {: codeblock}
	
	RETENTION_VALUE 是定義天數的數值數字。
    
**範例**
    
例如，若要停用 ID 為 *12345677fgh436902a3* 的帳戶的保留期間，請執行下列指令：

```
ibmcloud logging option-update -r account -i 12345677fgh436902a3 -e -1
```
{: codeblock}


## 停用空間的日誌保留原則
{: #disable_retention_policy_space}

當您停用保留原則時，會保留所有日誌。  

請完成下列步驟，以停用保留原則：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 將保留期間設為 **-1**，以停用保留期間。執行下列指令：

    ```
    ibmcloud logging option-show -e RETENTION_VALUE
	```
    {: codeblock}
	
	RETENTION_VALUE 是定義天數的數值數字。
    
**範例**
    
例如，若要停用 ID 為 *d35da1e3-b345-475f-8502-cfgh436902a3* 的空間的保留期間，請執行下列指令：

```
ibmcloud logging option-update -e -1
```
{: codeblock}


## 檢查帳戶的日誌保留原則
{: #check_retention_policy_acc}

若要取得為帳戶所設定的保留期間，請完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。

2. 取得帳戶 ID。

    如需相關資訊，請參閱[如何取得帳戶的 GUID](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid)。
    
3. 取得保留期間。執行下列指令：

    ```
    ibmcloud logging option-show -r account -i AccountID
    ```
    {: codeblock}

    輸出如下：

    ```
    ibmcloud logging option-show -r account -i kjskdsjfksjdflkjdsfbbd06461b066
    Showing log options of resource: kjskdsjfksjdflkjdsfbbd06461b066 ...

    Resource ID                              Retention   
    a:kjskdsjfksjdflkjdsfbbd06461b066       30   
	```
    {: screen}
	
## 檢查空間的日誌保留原則
{: #check_retention_policy_space}

若要取得為空間所設定的保留期間，請完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 取得保留期間。執行下列指令：

    ```
    ibmcloud logging option-show
    ```
    {: codeblock}

    輸出如下：

    ```
    ibmcloud logging option-show
    Showing log options of resource: 12345678-1234-2edr-a9de-378620d6fab5 ...

    SpaceId                                Retention   
    12345678-1234-2edr-a9de-378620d6fab5   30   
	```
    {: screen}
    


## 設定帳戶層次日誌保留原則
{: #set_retention_policy_acc}

請完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。

2. 取得帳戶 ID。

    如需相關資訊，請參閱[如何取得帳戶的 GUID](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid)。
    
3. 設定保留期間。執行下列指令：

    ```
    ibmcloud logging option-update -r account -i AccountID -e RETENTION_VALUE
    ```
    {: codeblock}
    
    其中 *RETENTION_VALUE* 是整數，用來定義您要保留日誌的天數。 
    
    
**範例**
    
例如，若要將帳戶中的任何日誌類型僅保留 15 天，請執行下列指令：

```
ibmcloud logging option-update -r account -i AccountID -e 15
```
{: codeblock}



## 設定空間的日誌保留原則
{: #set_retention_policy_space}

若要查看空間的保留期間，請完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 設定保留期間。執行下列指令：

    ```
    ibmcloud logging option-update -e RETENTION_VALUE
    ```
    {: codeblock}
    
    其中 *RETENTION_VALUE* 是整數，用來定義您要保留日誌的天數。
    
    
**範例**
    
例如，若要將空間中可用的日誌保留一年，請執行下列指令：

```
ibmcloud logging option-update -e 365
```
{: codeblock}




