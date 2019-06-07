---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, logs

subcollection: LogDNA

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

# 檢視日誌
{: #view_logs}

在 {{site.data.keyword.cloud_notm}} 中佈建 {{site.data.keyword.la_full_notm}} 服務的實例，並為日誌來源配置 LogDNA 代理程式之後，即可透過 {{site.data.keyword.la_full_notm}} Web 使用者介面，來檢視、監視及管理日誌資料。
{:shortdesc}

當您啟動 {{site.data.keyword.la_full_notm}} Web 使用者介面時，會以預先定義的格式來顯示日誌項目。您可以在**使用者喜好設定**區段中，修改每個日誌行中資訊的顯示方式。您也可以過濾日誌並修改搜尋設定，然後將結果加入書籤，作為*視圖*。您可以將一個以上的警示連接至視圖，以及將其取消連接。您可以定義一個自訂格式，指定您的行顯示在視圖中的格式。您可以展開日誌行，並查看已剖析的資料。


請完成下列步驟來檢視日誌：


## 步驟 1. 將 IAM 原則授與使用者以檢視日誌
{: #view_logs_step1}

**附註：**您必須是 {{site.data.keyword.la_full_notm}} 服務的管理者、{{site.data.keyword.la_full_notm}} 實例的管理者，或者具有帳戶 IAM 許可權，才能將原則授與其他使用者。

下表列出使用者必須擁有才能夠啟動 {{site.data.keyword.la_full_notm}} Web 使用者介面及檢視日誌的最低原則：

| 服務                              | 角色                      | 授與的許可權       |
|--------------------------------|---------------------------|-------------------------------|  
| `{{site.data.keyword.la_full_notm}} ` | 平台角色：檢視者     | 容許使用者檢視「觀察記載」儀表板中的服務實例清單。|
| `{{site.data.keyword.la_full_notm}} ` | 服務角色：讀者      | 容許使用者啟動 Web 使用者介面，以及在 Web 使用者介面中檢視日誌。|
{: caption="表 1. IAM 原則" caption-side="top"} 

如需如何為使用者配置這些原則的相關資訊，請參閱[將許可權授與使用者以在 LogDNA 中檢視日誌](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna)。


## 步驟 2. 透過 {{site.data.keyword.cloud_notm}} 使用者介面導覽至 Web 使用者介面
{: #view_logs_step2}

若要透過 {{site.data.keyword.cloud_notm}} 使用者介面來啟動 {{site.data.keyword.la_full_notm}} 使用者介面，請完成下列步驟：

1. 登入您的 {{site.data.keyword.cloud_notm}} 帳戶。

    按一下 [{{site.data.keyword.cloud_notm}} 儀表板 ![外部鏈結圖示](../../icons/launch-glyph.svg "外部鏈結圖示")](https://cloud.ibm.com/login){:new_window}，以啟動 {{site.data.keyword.cloud_notm}} 儀表板。

	使用您的使用者 ID 和密碼登入之後，即會開啟 {{site.data.keyword.cloud_notm}} *儀表板*。

2. 在導覽功能表中，選取**觀察**。 

3. 選取**記載**。 

    即會顯示 {{site.data.keyword.cloud_notm}} 上可用的 {{site.data.keyword.la_full_notm}} 實例清單。

4. 選取一個實例。然後，按一下**檢視 LogDNA**。

即會開啟 {{site.data.keyword.la_full_notm}} Web 使用者介面，並顯示已轉遞至該實例的日誌。


## 步驟 3. 自訂預設視圖
{: #view_logs_step3}

在**使用者喜好設定**區段中，您可以修改每行顯示的資料欄位順序。

請完成下列步驟來修改日誌行的格式：

1. 選取**配置**圖示 ![配置圖示](images/admin.png "管理圖示")。
2. 選取**使用者喜好設定**。即會開啟一個新視窗。
3. 選取**日誌格式**。
4. 修改*行格式* 區段，以符合您的需求。拖曳方框。


## 步驟 4. 查看日誌行
{: #view_logs_step4}

您可以隨時檢視環境定義中的每個日誌行。

請完成下列步驟： 

1. 按一下**視圖**圖示 ![配置圖示](images/views.png "配置圖示")。
2. 選取**所有項目**或視圖。
3. 識別日誌中您要瀏覽的行。
4. 展開日誌行。 

    即會顯示有關行 ID、標籤及標示的相關資訊。

5. 按一下**環境定義中的視圖**，以在該主機及/或應用程式中其他日誌行的環境定義中，查看日誌行。

6. 按一下**複製到剪貼簿**，將訊息欄位複製到剪貼簿。

完成時，請關閉這一行。


## 步驟 5. 過濾日誌
{: #view_logs_step5}

您可以依日誌來源、應用程式及記載層次來過濾日誌。 

* 來源可為主機、電腦、虛擬機器或 Heroku 應用程式。
* 應用程式代表日誌檔、程式或儲存器。
* 記載層次的範例為：INFO、DEBUG、ERROR

請完成下列步驟來過濾日誌：

1. 按一下**視圖**圖示 ![配置圖示](images/views.png "配置圖示")。
2. 選取**所有項目**或視圖。
3. 展開**所有標籤**，以查看日誌中所識別的標籤清單。然後，選擇您要的選項。
4. 展開**所有來源**，以查看日誌中所識別的日誌來源清單。然後，選擇您要的選項。
5. 展開**所有應用程式**，以查看日誌中所識別的應用程式清單。然後，選擇您要的選項。
6. 展開**所有層次**，以查看日誌中所識別的記載層次清單。然後，選擇您要的選項。


**附註：**在每一個區段中，您可以將多個選項分組成一個群組。將標籤、日誌來源、應用程式及記載層次分組，即可在您於其他自訂視圖中過濾日誌資料時，重複使用這些分組。

若要建立群組，請選取多個值。然後，按一下**另存為群組**。輸入群組的名稱，然後儲存。


## 步驟 6. 搜尋日誌
{: #view_logs_step6}

當您搜尋日誌資料時，搜尋會套用該視圖中所配置的任何日誌過濾器及時間查詢。

您可以執行簡式搜尋（單一詞彙字串搜尋）、複合搜尋（多個搜尋詞彙和運算子）、欄位搜尋（如果日誌行可以剖析），以及其他搜尋。如需相關資訊，請參閱[如何在 LogDNA 中搜尋日誌文件 ![外部鏈結圖示](../../icons/launch-glyph.svg "外部鏈結圖示")](https://docs.logdna.com/docs/search){:new_window}。

**附註：**AND 和 OR 運算子會區分大小寫，且必須大寫。



## 步驟 7. 建立視圖
{: #view_logs_step7}


請完成下列步驟來建立視圖：

1. 按一下**視圖**圖示 ![配置圖示](images/views.png "配置圖示")。
2. 選取**所有項目**或視圖。
3. 過濾日誌資料，然後按一下**另存為新視圖 / 警示**。

    即會開啟*建立新視圖* 頁面。

4. 在*名稱* 欄位中，輸入視圖的名稱。

5. 選擇性地新增種類。輸入名稱，然後按一下**將此新增為新的視圖種類**。

6. 選擇性地連接警示。這時會顯示一個新區段，供您配置警示。

7. 按一下**儲存視圖**
