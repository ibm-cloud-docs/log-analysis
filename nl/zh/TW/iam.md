---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, iam, manage user access

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

 
# 使用 IAM 管理使用者存取權
{: #iam}

{{site.data.keyword.iamlong}} (IAM) 可讓您在 {{site.data.keyword.cloud_notm}} 中，安全地鑑別使用者以及一致地控制對所有雲端資源的存取。
{:shortdesc}

**必須將已定義 IAM 使用者角色的存取原則，指派給在您帳戶中存取 {{site.data.keyword.la_full_notm}} 服務的每位使用者。** 原則決定使用者可以在您所選服務或實例的環境定義中執行什麼動作。容許的動作是自訂的，並定義為容許對服務執行的作業。然後，這些動作會對映至 IAM 使用者角色。

*原則* 可讓您在不同層次上授與存取權。部分選項包括下列各項： 

* 對您帳戶中所有已啟用 IAM 功能之服務的存取權
* 在您帳戶的單一地區中，跨所有服務實例的存取權
* 對您帳戶中個別服務實例的存取權
* 對資源群組環境定義內所有服務實例的存取權
* 對資源群組環境定義內單一地區中所有服務實例的存取權
* 對資源群組環境定義內所有已啟用 IAM 功能之服務的存取權

*角色* 定義使用者或 serviceID 可以執行的動作。{{site.data.keyword.cloud_notm}} 中有不同類型的角色：

* *平台管理角色* 可讓使用者在平台層次對服務資源執行作業，例如，將服務的存取權指派給使用者、建立或刪除服務 ID、建立實例、將服務的原則指派給其他使用者，以及將實例連結至應用程式。
* *服務存取角色* 可將各種許可權層次指派給使用者，以呼叫服務的 API。

**若要將一組使用者及服務 ID 組織成單一實體，方便您管理 IAM 許可權，請使用*存取群組*。**您可以指派單一原則給群組，而不是針對每個個別使用者或服務 ID，多次指派相同的存取權。
{: tip}


## 透過將原則直接指派給使用者的方式來管理存取權
{: #users}

若要透過使用 IAM 原則來管理使用者的存取權或指派新存取權，您必須是帳戶擁有者、帳戶中所有服務的管理者，或特定服務或服務實例的管理者。 

選擇下列任何動作來管理 {{site.data.keyword.cloud_notm}} 中的 IAM 原則：

* 若要修改使用者的許可權，請參閱[編輯現有的存取權](/docs/iam?topic=iam-iammanidaccser#edit_existing)。
* 若要授與許可權給使用者，請參閱[指派新的存取權](/docs/iam?topic=iam-iammanidaccser#assign_new_access)。
* 若要撤銷許可權，請參閱[移除存取權](/docs/iam?topic=iam-iammanidaccser#removing_access)。
* 若要檢閱使用者的許可權，請參閱[檢閱您的已指派存取權](/docs/iam?topic=iam-iammanidaccser#review_your_access)。


## 使用存取群組來管理存取權
{: #groups}

若要使用存取群組來管理使用者的存取權或指派新存取權，您必須是帳戶擁有者、帳戶中所有已啟用「身分及存取」之服務上的管理者或編輯者，或是針對「IAM 存取群組服務」指派的管理者或編輯者。 

選擇下列任何動作來管理 {{site.data.keyword.cloud_notm}} 中的存取群組：

* [建立存取群組](/docs/iam?topic=iam-groups#create_ag)。
* [指派存取權給群組](/docs/iam?topic=iam-groups#access_ag)。



## {{site.data.keyword.cloud_notm}} 平台角色
{: #platform}

使用下表來識別平台角色，您可以在 {{site.data.keyword.cloud_notm}} 中授與使用者這些角色，以執行下列任何平台動作：

| 平台動作                                                        | {{site.data.keyword.cloud_notm}} 平台角色    | 
|-------------------------------------------------------------------------|------------------------------------------------------|
| `授與其他帳戶成員使用服務的存取權`                                      | 管理者                                   | 
| `佈建服務實例`                                                          |編輯者                     | 
| `刪除服務實例`                                                          | 管理者 </br>編輯者                     | 
| `建立服務 ID`                                                           | 管理者 </br>編輯者                     |
| `檢視服務實例的詳細資料`                                                | 管理者 </br>編輯者 </br>操作員 </br>檢視者  | 
| `檢視「觀察記載」儀表板中的服務實例`                                    | 管理者 </br>編輯者 </br>操作員 </br>檢視者  | 
{: caption="表 1. IAM 使用者角色及動作" caption-side="top"}



## {{site.data.keyword.cloud_notm}} 服務角色
{: #service}

使用下表來識別服務角色，您可以授與使用者這些角色，以執行下列任何服務動作：

| 動作                                                                 | {{site.data.keyword.cloud_notm}} 服務角色     | 
|-------------------------------------------------------------------------|------------------------------------------------------|
| `新增 LogDNA 日誌來源`                                                  | 管理員 |
| `管理汲取金鑰`                                                 | 管理員 |
| `管理服務金鑰`                                                   | 管理員 |
| `保存日誌`                                                              | 管理員 |
| `配置警示`                                                              | 管理員 </br>撰寫者 </br>讀者                      | 
| `過濾及搜尋日誌資料`                                            | 管理員 </br>撰寫者 </br>讀者                      |
| `建立視圖`                                                          | 管理員 </br>撰寫者 </br>讀者|
| `匯出日誌資料`                                                       |管理員</br>撰寫者 </br>讀者|
| `在 LogDNA Web 使用者介面配置使用者喜好設定`                                            |管理員</br>撰寫者 </br>讀者|
| `透過 LogDNA Web 使用者介面檢視日誌`                                    |管理員</br>撰寫者 </br>讀者| 
{: caption="表 3. IAM 使用者角色及動作" caption-side="top"}


**附註**：**管理員**服務角色直接對映至 LogDNA 管理者角色。






