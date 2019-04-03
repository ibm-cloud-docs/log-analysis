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


# 取得 IAM 記號
{: #auth_iam1}

若要使用 {{site.data.keyword.loganalysisshort}} API 來管理帳戶網域中的可用日誌，您必須使用鑑別記號。使用 {{site.data.keyword.cloud_notm}} CLI 來取得 IAM 記號。記號具有有效期限。
{:shortdesc}


## 取得 IAM 記號
{: #iam_token_cli}

若要使用 {{site.data.keyword.cloud_notm}} CLI 來取得授權記號，請從終端機完成下列步驟：

1. 安裝 {{site.data.keyword.cloud_notm}} CLI。

   如需相關資訊，請參閱[下載並安裝 {{site.data.keyword.Bluemix}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)。
   
   如果已安裝 CLI，請繼續進行下一步。
    
2. 登入 {{site.data.keyword.cloud_notm}} 中的地區。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.cloud_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
	
3. 執行 `ibmcloud iam oauth-tokens` 指令來取得 IAM 記號。

    ```
	ibmcloud iam oauth-tokens
	```
	{: codeblock}
	
	此輸出會傳回必要的 IAM 記號，以用來在該空間及組織中鑑別使用者 ID。您可以將 IAM 記號匯出至 Shell 變數（例如 `$iam_token`）。



**附註：**當您使用記號時，請從您傳入 API 呼叫的記號值中移除 *Bearer*。

