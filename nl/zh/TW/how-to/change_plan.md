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


# 變更方案
{: #change_plan}

您可以透過 {{site.data.keyword.Bluemix_notm}} 使用者介面，或執行 `ibmcloud service update` 指令，來變更 {{site.data.keyword.loganalysisshort}} 服務方案。您隨時可以升級或降低方案。
{:shortdesc}

## 透過使用者介面變更服務方案
{: #change_plan_ui}

若要在 {{site.data.keyword.Bluemix_notm}} 使用者介面中變更服務方案，請完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}}：[http://bluemix.net ![外部鏈結圖示](../../../icons/launch-glyph.svg "外部鏈結圖示")](http://bluemix.net){:new_window}。 

2. 選取可使用 {{site.data.keyword.loganalysisshort}} 服務的地區、組織及空間。  

3. 從 {{site.data.keyword.Bluemix_notm}} *儀表板* 中，按一下 {{site.data.keyword.loganalysisshort}} 服務實例。 
    
4. 在 {{site.data.keyword.loganalysisshort}} 儀表板中，選取**方案**標籤。

    即會顯示現行方案的相關資訊。
	
5. 選取新方案以升級或降低您的方案。 

6. 按一下**儲存**。




## 透過 CLI 變更服務方案
{: #change_plan_cli}

若要在 Bluemix 中透過 CLI 變更服務方案，請完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
	
2. 執行 `ibmcloud service list` 指令來檢查現行方案，以及從空間的可用服務清單中取得 {{site.data.keyword.loganalysisshort}} 服務名稱。 

    **name** 欄位的值就是您必須用來變更方案的值。 

    例如，
	
	```
	$ ibmcloud service list
    Invoking 'cf services'...

    Getting services in org MyOrg / space dev as xxx@ibm.com...
    OK

    name                           service                  plan             bound apps            last operation
    Log Analysis-m2                ibmLogAnalysis           premium                                update succeeded
    ```
	{: screen}
    
3. 升級或降低您的方案。執行 `ibmcloud service update` 指令。
    
	```
	ibmcloud service update service_name [-p new_plan]
	```
	{: codeblock}
	
	其中 
	
	* *service_name* 是服務的名稱。您可以執行 `ibmcloud service list` 指令來取得值。
	* *new_plan* 是方案的名稱。
	
	下表列出不同的方案及其支援的值：
	
	<table>
	  <caption>表 1. 方案清單。</caption>
	  <tr>
	    <th>方案</th>
	    <th>名稱</th>
	  </tr>
	  <tr>
	    <td>精簡</td>
	    <td>standard</td>
	  </tr>
	  <tr>
	    <td>日誌收集</td>
	    <td>premium</td>
	  </tr>
	  <tr>
	    <td>日誌收集，每天搜尋 2 GB</td>
	    <td>premiumsearch2</td>
	  </tr>
	  <tr>
	    <td>日誌收集，每天搜尋 5 GB</td>
	    <td>premiumsearch5</td>
	  </tr>
	  <tr>
	    <td>日誌收集，每天搜尋 10 GB</td>
	    <td>premiumsearch10</td>
	  </tr>
	</table>
	
	例如，若要將您的方案降低為*精簡* 方案，請執行下列指令：
	
	```
	ibmcloud service update "Log Analysis-m2" -p standard
    Updating service instance Log Analysis-m2 as xxx@ibm.com...
    OK
	```
	{: screen}

4. 驗證新的方案已變更。執行 `ibmcloud service list` 指令。

  ```
	ibmcloud service list
	```
	{: codeblock}






