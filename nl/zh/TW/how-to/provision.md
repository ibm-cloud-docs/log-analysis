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


# 佈建 Log Analysis 服務
{: #provision}

您可以從 {{site.data.keyword.Bluemix}} 使用者介面或從指令行佈建 {{site.data.keyword.loganalysisshort}} 服務。
{:shortdesc}


## 從使用者介面佈建
{: #ui}

請完成下列步驟，以在 {{site.data.keyword.Bluemix_notm}} 中佈建 {{site.data.keyword.loganalysisshort}} 服務的實例：

1. 登入 {{site.data.keyword.Bluemix_notm}} 帳戶。

    {{site.data.keyword.Bluemix_notm}} 儀表板可以在下列網址找到：[http://bluemix.net ![外部鏈結圖示](../../../icons/launch-glyph.svg "外部鏈結圖示")](http://bluemix.net){:new_window}。
    
	使用您的使用者 ID 和密碼登入之後，{{site.data.keyword.Bluemix_notm}} 使用者介面隨即開啟。

2. 按一下**型錄**。{{site.data.keyword.Bluemix_notm}} 上可用的服務清單隨即開啟。

3. 選取**開發人員工具**種類，以過濾所顯示的服務清單。

4. 按一下 **Log Analysis** 磚。

5. 選取服務方案。依預設，會設定**精簡**方案。

    如需服務方案的相關資訊，請參閱[服務方案](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans)。
	
6. 按一下**建立**，以在所登入的 {{site.data.keyword.Bluemix_notm}} 空間中佈建 {{site.data.keyword.loganalysisshort}} 服務。
  
 

## 從 CLI 佈建
{: #cli}

請完成下列步驟，以透過指令行在 {{site.data.keyword.Bluemix_notm}} 中佈建 {{site.data.keyword.loganalysisshort}} 服務的實例：

1. [必要條件] 安裝 {{site.data.keyword.Bluemix_notm}} CLI。

   如需相關資訊，請參閱[安裝 {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)。
   
   如果已安裝 CLI，請繼續進行下一步。
    
2. 登入 {{site.data.keyword.Bluemix_notm}} 中您要佈建服務的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
	
3. 執行 `ibmcloud service create` 指令，以佈建實例。

    ```
	ibmcloud service create service_name service_plan service_instance_name
	```
	{: codeblock}
	
	其中
	
	* service_name 是服務的名稱，亦即 **ibmLogAnalysis**。
	* service_plan 是服務方案名稱。如需方案的清單，請參閱[服務方案](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans)。
	* service_instance_name 是您要用於所建立之新服務實例的名稱。

	例如，若要使用精簡方案建立 {{site.data.keyword.loganalysisshort}} 服務的實例，請執行下列指令：
	
	```
	ibmcloud service create ibmLogAnalysis standard my_logging_svc
	```
	{: codeblock}
	
4. 驗證已順利建立服務。執行下列指令：

    ```	
	ibmcloud service list
	```
	{: codeblock}
	
	執行指令的輸出看起來如下：
	
	```
Getting services in org MyOrg / space MySpace as xxx@yyy.com...
    OK
    
    name                           service                  plan                   bound apps              last operation
    my_logging_svc                ibmLogAnalysis           standard                                        create succeeded
	```
	{: screen}

	



