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

# 授與許可權以管理日誌以及檢視帳戶日誌
{: #grant_permissions}

在 {{site.data.keyword.Bluemix}} 中，您可以將一個以上的 IAM 角色指派給使用者。這些角色定義針對該使用者啟用以使用 {{site.data.keyword.loganalysisshort}} 服務的作業。  
{:shortdesc}

例如，您可以將**操作員**角色授與使用者，以容許他管理日誌。如果您只想要使用者檢視帳戶日誌，則可以將**檢視者**角色授與使用者。如需相關資訊，請參閱 [IAM 角色](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-security_ov#iam_roles)。

**附註：** 

* 若要將管理日誌或檢視帳戶日誌的許可權授與使用者，您必須有權可將原則指派給帳戶中的其他使用者，或者您必須是帳戶擁有者。如果您不是帳戶擁有者，則必須具有 IAM 原則與編輯器、操作員或管理者角色。
* 若要將檢視空間中日誌的許可權授與使用者，您必須具有組織及空間的權限來將 Cloud Foundry 角色指派給使用者，以說明此使用者可在該空間中使用 {{site.data.keyword.loganalysisshort}} 服務所執行的動作。 

## 透過 {{site.data.keyword.Bluemix_notm}} 使用者介面將 IAM 原則指派給使用者
{: #grant_permissions_ui_account}

請完成下列步驟，以將使用 {{site.data.keyword.loganalysisshort}} 服務的許可權授與使用者：

1. 登入 {{site.data.keyword.Bluemix_notm}} 主控台。

    開啟 Web 瀏覽器，並啟動 {{site.data.keyword.Bluemix_notm}} 儀表板：[http://bluemix.net ![外部鏈結圖示](../../../icons/launch-glyph.svg "外部鏈結圖示")](http://bluemix.net){:new_window}
	
	使用您的使用者 ID 和密碼登入之後，{{site.data.keyword.Bluemix_notm}} 使用者介面隨即開啟。

2. 從功能表列中，按一下**管理 > 帳戶 > 使用者**。 

    *使用者* 視窗會顯示目前所選取帳戶的使用者及其電子郵件位址的清單。
	
3. 如果使用者是帳戶成員，請從清單選取使用者名稱，或按一下*動作* 功能表中的**管理使用者**。

    如果使用者不是帳戶成員，請參閱[邀請使用者](/docs/iam?topic=iam-iamuserinv#iamuserinv)。

4. 在**存取原則**區段中，按一下**指派存取權**，然後選取**指派資源的存取權**。

    即會開啟*將資源存取權指派給使用者* 視窗。

5. 輸入原則的相關資訊。下表列出可定義原則的必要欄位： 

    <table>
	  <caption>可配置 IAM 原則的欄位清單。</caption>
	  <tr>
	    <th>欄位</th>
		<th>值</th>
	  </tr>
	  <tr>
	    <td>服務</td>
		<td>*IBM Cloud Log Analysis*</td>
	  </tr>	  
	  <tr>
	    <td>地區</td>
		<td>您可以指定使用者將獲授與日誌使用存取權的地區。個別選取一個以上的地區，或選取**所有現行地區**以將存取權授與所有地區。</td>
	  </tr>
	  <tr>
	    <td>服務實例</td>
		<td>選取*所有服務實例*。</td>
	  </tr>
	  <tr>
	    <td>角色</td>
		<td>選取一個以上的 IAM 角色。<br>有效的角色為：*管理者*、*操作員*、*編輯者* 及*檢視者*。<br>如需每個角色所容許動作的相關資訊，請參閱 [IAM 角色](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-security_ov#iam_roles)。</td>
	  </tr>
     </table>
	
6. 按一下**指派**。
	
您配置的原則即適用於選取的地區。 


## 使用指令行將 IAM 原則指派給使用者
{: #grant_permissions_commandline}

請完成下列步驟，以使用指令行將檢視帳戶日誌存取權授與使用者：

1. 從終端機中，登入 {{site.data.keyword.Bluemix_notm}} 帳戶。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。

2. 確認使用者是帳戶成員。執行下列指令，以取得帳戶中的使用者清單：

    ```
	ibmcloud account users
	```
    {: codeblock}	

	即會顯示使用者及其 GUID 的清單。

3. 如果使用者不是帳戶成員，請聯絡帳戶擁有者，並提出邀請使用者加入帳戶的要求。如需相關資訊，請參閱[邀請使用者](/docs/iam?topic=iam-iamuserinv#iamuserinv)。

    **提示：**邀請使用者加入帳戶的指令如下：`ibmcloud iam account-user-invite USER_EMAIL`
		
4. 將原則指派給使用者。執行下列指令：

    ```
    ibmcloud iam user-policy-create USER_NAME --roles ROLE --service-name ibmloganalysis
	```
	{: codeblock}

	其中
    * USER_NAME 是使用者的 {{site.data.keyword.Bluemix_notm}} ID。
	* ROLE 是 IAM 角色。有效值為：*administrator*、*operator*、*editor* 及 *viewer*

5. 驗證已將原則指派給使用者。執行下列指令，以列出已指派給使用者的所有原則：

    ```
    ibmcloud iam user-policies USER_NAME
	```
	{: codeblock}




## 使用 {{site.data.keyword.Bluemix_notm}} 使用者介面將檢視空間日誌許可權授與使用者
{: #grant_permissions_ui_space}

若要將檢視空間中日誌的許可權授與使用者，您必須將 Cloud Foundry 角色指派給使用者，以說明此使用者可在空間中使用 {{site.data.keyword.loganalysisshort}} 服務所執行的動作。 

請完成下列步驟，以將使用 {{site.data.keyword.loganalysisshort}} 服務的許可權授與使用者：

1. 登入 {{site.data.keyword.Bluemix_notm}} 主控台。

    開啟 Web 瀏覽器，並啟動 {{site.data.keyword.Bluemix_notm}} 儀表板：[http://bluemix.net ![外部鏈結圖示](../../../icons/launch-glyph.svg "外部鏈結圖示")](http://bluemix.net){:new_window}
	
	使用您的使用者 ID 和密碼登入之後，{{site.data.keyword.Bluemix_notm}} 使用者介面隨即開啟。

2. 從功能表列中，按一下**管理 > 帳戶 > 使用者**。 

    *使用者* 視窗會顯示目前所選取帳戶的使用者及其電子郵件位址的清單。
	
3. 如果使用者是帳戶成員，請從清單選取使用者名稱，或按一下*動作* 功能表中的**管理使用者**。

    如果使用者不是帳戶成員，請參閱[邀請使用者](/docs/iam?topic=iam-iamuserinv#iamuserinv)。

4. 選取 **Cloud Foundry 存取權**，然後選取組織。

    即會列出該組織中可用的空間清單。

5. 選擇一個空間。然後，從功能表動作中選取**編輯空間角色**。

6. 選取 1 個以上的空間角色。有效的角色為：*管理員*、*開發人員* 及*審核員*
	
7. 按一下**儲存角色**。




