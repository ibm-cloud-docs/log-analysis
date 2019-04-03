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


# 針對 Kubernetes 叢集中所部署的應用程式，在 Kibana 中分析日誌
{: #container_logs}
使用此指導教學，瞭解如何在 {{site.data.keyword.Bluemix_notm}} 中配置叢集以將日誌轉遞至 {{site.data.keyword.loganalysisshort}} 服務。
{:shortdesc}


## 目標
{: #objectives}

1. 在叢集中配置記載配置。 
2. 在 {{site.data.keyword.Bluemix_notm}} 中，搜尋及分析 Kubernetes 叢集中所部署應用程式的容器日誌。

此指導教學逐步說明讓下列完整情境在 {{site.data.keyword.Bluemix_notm}} 中運作所需的步驟：佈建叢集、在 {{site.data.keyword.Bluemix_notm}} 中配置叢集以將日誌傳送 {{site.data.keyword.loganalysisshort}} 服務、在叢集中部署應用程式，以及使用 Kibana 來檢視及過濾該叢集的容器日誌。


**附註：**若要完成此指導教學，您必須完成必要條件以及從不同步驟鏈結的指導教學。


## 必要條件
{: #prereq}

1. 成為 {{site.data.keyword.Bluemix_notm}} 帳戶的成員或擁有者，並且具有許可權可以建立 Kubernetes 標準叢集、將應用程式部署至叢集，以及查詢 {{site.data.keyword.Bluemix_notm}} 中的日誌以在 Kibana 中進行進階分析。

    {{site.data.keyword.Bluemix_notm}} 的使用者 ID 必須已指派下列原則：
    
    * {{site.data.keyword.containershort}} 的 IAM 原則與 *editor*、*operator* 或 *administrator* 許可權。
    * 使用 *developer* 許可權佈建 {{site.data.keyword.loganalysisshort}} 服務之空間的 CF 角色。
    
    如需相關資訊，請參閱[透過 IBM Cloud 使用者介面將 IAM 原則指派給使用者](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_account)及[使用 IBM Cloud 使用者介面將檢視空間日誌許可權授與使用者](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space)。

2. 具有一個終端機階段作業，您可以在其中從指令行管理 Kubernetes 叢集並部署應用程式。此指導教學中提供的範例適用於 Ubuntu Linux 系統。

3. 安裝 CLI，以在 Ubuntu 系統中使用 {{site.data.keyword.containershort}} 及 {{site.data.keyword.loganalysisshort}}。

    * 安裝 {{site.data.keyword.Bluemix_notm}} CLI。安裝 {{site.data.keyword.containershort}} CLI，以在 {{site.data.keyword.containershort}} 中建立及管理 Kubernetes 叢集，以及將容器化應用程式部署至叢集。如需相關資訊，請參閱[安裝 {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli/index.html#overview)。
    
    * 安裝 {{site.data.keyword.loganalysisshort}} CLI。如需相關資訊，請參閱[配置 Log Analysis CLI（IBM Cloud 外掛程式）](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#config_log_collection_cli)。
    
4. 在美國南部地區，有權存取帳戶中名為 **dev** 的空間。 

    將配置叢集中可用的日誌轉遞至與此空間相關聯的空間網域。 
    
    在此空間中，您將佈建 {{site.data.keyword.loganalysisshort}} 服務。
    
    您必須具有此空間中的 **developer** 許可權，才能佈建 {{site.data.keyword.loganalysisshort}} 服務。
    
    在指導教學中，所使用組織的名稱是 **MyOrg**。

    
 

## 步驟 1：佈建 Kubernetes 叢集
{: #step25}

請完成下列步驟：

1. 建立標準 Kubernetes 叢集。

   如需相關資訊，請參閱[建立叢集](/docs/containers/cs_tutorials.html#cs_cluster_tutorial)。

2. 在終端機中設定叢集環境定義。設定環境定義之後，您可以管理 Kubernetes 叢集，並在 Kubernetes 叢集中部署應用程式。

    登入 {{site.data.keyword.Bluemix_notm}} 中與您所建立叢集相關聯的地區、組織及空間。如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。

	起始設定 {{site.data.keyword.containershort}} 服務外掛程式。

	```
	ibmcloud cs init
	```
	{: codeblock}

    將終端機環境定義設為叢集。
    
	```
	ibmcloud cs cluster-config MyCluster
	```
	{: codeblock}

    此指令的執行輸出所提供的指令，就是您必須在終端機中執行以設定配置檔路徑的指令。例如：

	```
	export KUBECONFIG=/Users/ibm/.bluemix/plugins/container-service/clusters/MyCluster/kube-config-hou02-MyCluster.yml
	```
	{: codeblock}

    複製並貼上指令以在終端機中設定環境變數，然後按 **Enter** 鍵。



## 步驟 2：配置叢集以將日誌自動轉遞至 {{site.data.keyword.loganalysisshort}} 服務
{: #step26}

部署應用程式時，{{site.data.keyword.containershort}} 會自動收集日誌。不過，不會將日誌自動轉遞至 {{site.data.keyword.loganalysisshort}} 服務。您必須在叢集中建立 1 個以上的記載配置，以定義：

* 要轉遞日誌的位置。您可以將日誌轉遞至帳戶網域或空間網域。
* 將哪些日誌轉遞至 {{site.data.keyword.loganalysisshort}} 服務以進行分析。


在您定義記載配置之前，請檢查叢集中的現行記載配置定義。執行下列指令：

```
$ ibmcloud cs logging-config-get ClusterName
```
{: codeblock}

其中 *ClusterName* 是叢集的名稱。

例如，針對叢集 *mycluster* 所定義的記載配置如下： 

```
$ ibmcloud cs logging-config-get mycluster
Retrieving cluster mycluster logging configurations...
OK
Id                                     Source       Namespace   Host                                Port   Org            Space   Protocol   Paths   
13ded2c0-83f5-4cc5-8de7-1e34e1287f34   worker       -           ingest.logging.ng.bluemix.net       9091   Demo_Org       dev     ibm        /var/log/syslog,/var/log/auth.log   
ae249c04-a3a9-4c29-a890-22d8da7bd1b2   container    *           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        -   
31739fc1-42e2-4b66-ac57-6a32091c257a   ingress      -           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        /var/log/alb/ids/*.log,/var/log/alb/ids/*.err,/var/log/alb/customerlogs/*.log,/var/log/alb/customerlogs/*.err   
6b8cfe89-4959-448d-898b-c3b0584eca71   kubernetes   -           ingest-eu-fra.logging.bluemix.net   9091   Demo_Org.      dev     ibm        /var/log/kubelet.log,/var/log/kube-proxy.log   

```
{: screen}

若要查看您可定義記載配置的日誌來源清單，請參閱[日誌來源](/docs/services/CloudLogAnalysis/containers/containers_kubernetes.html#log_sources)。


### 配置叢集以將 stderr 及 stdout 日誌轉遞至 {{site.data.keyword.loganalysisshort}} 服務
{: #containerstd}


完成下列步驟，以將 stdout 及 stderr 日誌傳送至空間網域，其中，組織名稱是 *MyOrg*，而空間名稱是美國南部地區的 *dev*：

1. 確認使用者 ID 具有新增叢集配置的許可權。只有使用者具有含叢集管理許可權之 {{site.data.keyword.containershort}} 的 IAM 原則時，才能啟用此特性。需要下列任何角色：*管理者*、*操作員*

    若要檢查使用者 ID 已指派可管理叢集的 IAM 原則，請完成下列步驟：
    
    1. 登入 {{site.data.keyword.Bluemix_notm}} 主控台。開啟 Web 瀏覽器，並啟動 {{site.data.keyword.Bluemix_notm}} 儀表板：[http://bluemix.net ![外部鏈結圖示](../../../icons/launch-glyph.svg "外部鏈結圖示")](http://bluemix.net){:new_window}。使用您的使用者 ID 及密碼登入之後，{{site.data.keyword.Bluemix_notm}} 使用者介面隨即開啟。

    2. 從功能表列中，按一下**管理 > 帳戶 > 使用者**。*使用者* 視窗會顯示目前所選取帳戶的使用者及其電子郵件位址的清單。
	
    3. 選取使用者 ID，並驗證使用者 ID 具有 {{site.data.keyword.containershort}} 的原則。

    如果您需要許可權，請聯絡帳戶擁有者或帳戶管理者。只有帳戶擁有者或具有原則指派許可權的使用者才能執行此步驟。

2. 建立叢集記載配置。執行下列指令，以將 *stdout* 及 *stderr* 日誌檔傳送至 {{site.data.keyword.loganalysisshort}} 服務：

    ```
    ibmcloud cs logging-config-create ClusterName --logsource container --namespace '*' --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    其中 

    * *ClusterName* 是叢集的名稱。
    * *EndPoint* 是 {{site.data.keyword.loganalysisshort}} 服務佈建所在地區中的記載服務 URL。如需端點清單，請參閱[端點](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls)。
    * *OrgName* 是可使用空間的組織名稱。
    * *SpaceName* 是 {{site.data.keyword.loganalysisshort}} 服務佈建所在空間的名稱。


例如，若要建立記載配置以將 stdout 及 stderr 日誌轉遞至美國南部地區的空間 dev，請執行下列指令：

```
ibmcloud cs logging-config-create mycluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}




### 配置叢集以將工作者日誌轉遞至 {{site.data.keyword.loganalysisshort}} 服務
{: #workerlogs }

完成下列步驟，以將工作者日誌傳送至空間網域，其中，組織名稱是 *MyOrg*，而空間名稱是美國南部地區的 *dev*：

1. 確認使用者 ID 具有新增叢集配置的許可權。只有使用者具有含叢集管理許可權之 {{site.data.keyword.containershort}} 的 IAM 原則時，才能啟用此特性。需要下列任何角色：*管理者*、*操作員*

    若要檢查使用者 ID 已指派可管理叢集的 IAM 原則，請完成下列步驟：
    
    1. 登入 {{site.data.keyword.Bluemix_notm}} 主控台。開啟 Web 瀏覽器，並啟動 {{site.data.keyword.Bluemix_notm}} 儀表板：[http://bluemix.net ![外部鏈結圖示](../../../icons/launch-glyph.svg "外部鏈結圖示")](http://bluemix.net){:new_window}。使用您的使用者 ID 及密碼登入之後，{{site.data.keyword.Bluemix_notm}} 使用者介面隨即開啟。

    2. 從功能表列中，按一下**管理 > 帳戶 > 使用者**。*使用者* 視窗會顯示目前所選取帳戶的使用者及其電子郵件位址的清單。
	
    3. 選取使用者 ID，並驗證使用者 ID 具有 {{site.data.keyword.containershort}} 的原則。

    如果您需要許可權，請聯絡帳戶擁有者或帳戶管理者。只有帳戶擁有者或具有原則指派許可權的使用者才能執行此步驟。

2. 建立叢集記載配置。執行下列指令，以將 */var/log/syslog* 及 */var/log/auth.log* 日誌檔傳送至 {{site.data.keyword.loganalysisshort}} 服務：

    ```
    ibmcloud cs logging-config-create ClusterName --logsource worker --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    其中 

    * *ClusterName* 是叢集的名稱。
    * *EndPoint* 是 {{site.data.keyword.loganalysisshort}} 服務佈建所在地區中的記載服務 URL。如需端點清單，請參閱[端點](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls)。
    * *OrgName* 是可使用空間的組織名稱。
    * *SpaceName* 是 {{site.data.keyword.loganalysisshort}} 服務佈建所在空間的名稱。

    
例如，若要建立記載配置以將工作者日誌轉遞至美國南部地區的空間網域，請執行下列指令：

```
ibmcloud cs logging-config-create mycluster --logsource worker  --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}



## 步驟 3：將查看空間網域中日誌的許可權授與使用者
{: #step33}

若要將檢視空間中日誌的許可權授與使用者，您必須將 Cloud Foundry 角色指派給該使用者，以說明此使用者可在空間中使用 {{site.data.keyword.loganalysisshort}} 服務所執行的動作。 

請完成下列步驟，以將使用 {{site.data.keyword.loganalysisshort}} 服務的許可權授與使用者：

1. 登入 {{site.data.keyword.Bluemix_notm}} 主控台。

    開啟 Web 瀏覽器，並啟動 {{site.data.keyword.Bluemix_notm}} 儀表板：[http://bluemix.net ![外部鏈結圖示](../../../icons/launch-glyph.svg "外部鏈結圖示")](http://bluemix.net){:new_window}
	
	使用您的使用者 ID 和密碼登入之後，{{site.data.keyword.Bluemix_notm}} 使用者介面隨即開啟。

2. 從功能表列中，按一下**管理 > 帳戶 > 使用者**。 

    *使用者* 視窗會顯示目前所選取帳戶的使用者及其電子郵件位址的清單。
	
3. 如果使用者是帳戶成員，請從清單選取使用者名稱，或按一下*動作* 功能表中的**管理使用者**。

    如果使用者不是帳戶成員，請參閱[邀請使用者](/docs/iam/iamuserinv.html#iamuserinv)。

4. 選取 **Cloud Foundry 存取權**，然後選取組織。

    即會列出該組織中可用的空間清單。

5. 選擇空間。然後，從功能表動作中選取**編輯空間角色**。

    如果您看不到美國南部的空間，請先建立空間，再繼續進行。

6. 選取 *developer*。

    您可以選取 1 個以上的角色。 
    
    有效的角色為：*管理員*、*開發人員* 及*審核員*
	
7. 按一下**儲存角色**。


## 步驟 4：授與 {{site.data.keyword.containershort_notm}} 金鑰擁有者許可權
{: #step52}

對於要轉遞至空間的叢集日誌，{{site.data.keyword.containershort_notm}} 金鑰擁有者必須具有下列許可權：

* {{site.data.keyword.loganalysisshort}} 服務的 IAM 原則與 *Administrator* 許可權。
* 要轉遞日誌的組織及空間中的 Cloud Foundry (CF) 許可權。容器金鑰擁有者需要組織的 *orgManager* 角色，以及空間的 *SpaceManager* 及 *Developer*。

請完成下列步驟：

1. 識別帳戶中為 {{site.data.keyword.containershort}} 金鑰擁有者的使用者。從終端機中，執行下列指令：

    ```
    ibmcloud cs api-key-info ClusterName
    ```
    {: codeblock}
    
    其中 *ClusterName* 是叢集的名稱。

2. 驗證識別為 {{site.data.keyword.containershort}} 金鑰擁有者的使用者具有組織的 *orgManager* 角色，以及空間的 *SpaceManager* 及 *Developer*。

    登入 {{site.data.keyword.Bluemix_notm}} 主控台。開啟 Web 瀏覽器，並啟動 {{site.data.keyword.Bluemix_notm}} 儀表板：[http://bluemix.net ![外部鏈結圖示](../../../icons/launch-glyph.svg "外部鏈結圖示")](http://bluemix.net){:new_window}。使用您的使用者 ID 及密碼登入之後，{{site.data.keyword.Bluemix_notm}} 使用者介面隨即開啟。

    從功能表列中，按一下**管理 > 帳戶 > 使用者**。*使用者* 視窗會顯示目前所選取帳戶的使用者及其電子郵件位址的清單。
	
    選取使用者的 ID，並驗證使用者具有組織的 *orgManager* 角色，以及空間的 *SpaceManager* 及 *Developer*。

    如果使用者沒有正確的許可權，請將下列許可權授與使用者：組織的 *orgManager* 角色，以及空間的 *SpaceManager* 及 *Developer*。如需相關資訊，請參閱[使用 IBM Cloud 使用者介面將檢視空間日誌許可權授與使用者](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space)。
    
3. 驗證識別為 {{site.data.keyword.containershort}} 金鑰擁有者的使用者具有 {{site.data.keyword.loganalysisshort}} 服務的 IAM 原則與 *Administrator* 許可權。

    從功能表列中，按一下**管理 > 帳戶 > 使用者**。*使用者* 視窗會顯示目前所選取帳戶的使用者及其電子郵件位址的清單。
	
    選取使用者的 ID，並驗證使用者具有 IAM 原則集。 

    如果使用者沒有 IAM 原則，請參閱[透過 IBM Cloud 使用者介面將 IAM 原則指派給使用者](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_account)。

4. 重新整理記載配置。執行下列指令：
    
    ```
    ibmcloud cs logging-config-refresh ClusterName
    ```
    {: codeblock}
        
    其中 *ClusterName* 是叢集的名稱。
	



## 步驟 5：在 Kubernetes 叢集中部署範例應用程式，以產生 stdout 中的內容
{: #step53}

在 Kubernetes 叢集中部署及執行範例應用程式。完成下列指導教學中的步驟，以部署範例應用程式：[課程 1：將單一實例應用程式部署至 Kubernetes 叢集](/docs/containers/cs_tutorials_apps.html#cs_apps_tutorial_lesson1)。

應用程式是 Hello World Node.js 應用程式：

```
var express = require('express')
var app = express()

app.get('/', function(req, res) {
  res.send('Hello world! Your app is up and running in a cluster!\n')
})
app.listen(8080, function() {
  console.log('Sample app is listening on port 8080.')
})
```
{: screen}

在此範例應用程式中，當您在瀏覽器中測試應用程式時，應用程式會將下列訊息寫入 stdout：`Sample app is listening on port 8080.`






## 步驟 6：在 Kibana 中檢視日誌資料
{: #step6}

請完成下列步驟：

1. 在瀏覽器中啟動 Kibana。 

    如需如何啟動 Kibana 的相關資訊，請參閱[從 Web 瀏覽器導覽至 Kibana](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser)。

    若要分析叢集的日誌資料，您必須存取叢集建立所在之「雲端公用」地區的 Kibana。 
    
    例如，在美國南部地區中，輸入下列 URL 來啟動 Kibana：
	
	```
	https://logging.ng.bluemix.net/
	```
	{: codeblock}
	
    即會開啟 Kibana。
    
    **附註：**請驗證您在要轉遞叢集日誌的地區中啟動 Kibana。如需每個地區之 URL 的相關資訊，請參閱[記載端點](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#urls_kibana)。
    	
2. 若要檢視空間網域中可用的日誌資料，請完成下列步驟：

    1. 在 Kibana 中，按一下使用者 ID。即會開啟可設定空間的視圖。
    
    2. 選取可使用空間的帳戶。 
    
    3. 選取下列網域：**空間**
    
    4. 選取可使用空間的組織 *MyOrg*。
    
    5. 選取空間 *dev*。
    
    
3. 在**探索**頁面中，查看所顯示的事件。 
        
    在*可用欄位* 區段中，您會看到一份欄位清單，這些欄位可以用來定義新查詢，或過濾頁面上所顯示表格中列出的項目。
    
    下表列出您可在分析應用程式日誌時用來定義新搜尋查詢的一些欄位。此表格也包括範例值，這些值對應至範例應用程式所產生的事件：
 
    <table>
              <caption>表 2. 容器日誌的一般欄位</caption>
               <tr>
                <th align="center">欄位</th>
                <th align="center">說明</th>
                <th align="center">範例</th>
              </tr>
              <tr>
                <td>*ibm-containers.region_str*</td>
                <td>此欄位的值對應至日誌項目收集所在的 {{site.data.keyword.Bluemix_notm}} 地區。</td>
                <td>us-south</td>
              </tr>
			  <tr>
                <td>*ibm-containers.account_id_str*</td>
                <td>帳戶 ID</td>
                <td></td>
              </tr>
			  <tr>
                <td>*ibm-containers.cluster_id_str *</td>
                <td>叢集 ID。</td>
                <td></td>
              </tr>
              <tr>
                <td>*ibm-containers.cluster_name_str*</td>
                <td>叢集 ID</td>
                <td></td>
              </tr>
			  <tr>
                <td>*kubernetes.namespace_name_str*</td>
                <td>名稱空間名稱</td>
                <td>*default* 是預設值。</td>
              </tr>
              <tr>
                <td>*kubernetes.container_name_str*</td>
                <td>容器名稱</td>
                <td>hello-world-deployment</td>
              </tr>
              <tr>
                <td>*kubernetes.labels.label_name*</td>
                <td>標籤欄位是選用性的。您可以有 0 個以上的標籤。每一個標籤都以 `kubernetes.labels.` 字首為開頭，後面接著 *label_name*。</td>
                <td>在範例應用程式中，您可以看到 2 個標籤：<br>* *kubernetes.labels.pod-template-hash_str* = 3355293961 <br>* *kubernetes.labels.run_str* =	hello-world-deployment  </td>
              </tr>
              <tr>
                <td>*stream_str *</td>
                <td>日誌類型。</td>
                <td>*stdout*、*stderr*</td>
              </tr>
        </table>
     
如需 Kubernetes 叢集相關的其他搜尋欄位的相關資訊，請參閱[搜尋日誌](/docs/services/CloudLogAnalysis/containers/containers_kubernetes.html#log_search)。


## 步驟 7：在 Kibana 中依 Kubernetes 叢集名稱過濾資料
{: #step7}
    
在*探索* 頁面所顯示的表格中，您可以看到所有可用於分析的項目。列出的項目對應至*搜尋* 列中所顯示的搜尋查詢。使用星號 (*) 來顯示針對頁面所配置時段內的所有項目。
    
例如，若要依 Kubernetes 叢集名稱過濾資料，請修改*搜尋* 列查詢。請根據自訂欄位 *kubernetes.cluster_name_str* 來新增過濾器：
    
1. 在**可用欄位**區段中，選取 *kubernetes.cluster_name_str* 欄位。即會顯示此欄位的部分可用值。    
    
2. 選取對應至您要分析日誌之叢集的值。 
    
    在您選取值之後，會將過濾器新增至*搜尋* 列，而且表格只會顯示符合剛才所選取準則的項目。     
   

**附註：** 

如果看不到您的叢集名稱，請新增任何叢集名稱的過濾器。然後，選取過濾器的編輯符號。    
    
會顯示下列查詢：
    
```
	{
        "query": {
          "match": {
            "kubernetes.cluster_name_str": {
              "query": "cluster1",
              "type": "phrase"
            }
          }
        }
      }
```
{: screen}

請將叢集名稱 (*cluster1*) 取代為您要檢視日誌資料的叢集名稱 *mycluster*。
        
如果您看不到任何資料，請嘗試變更時間過濾器。如需相關資訊，請參閱[設定時間過濾器](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter)。

如需相關資訊，請參閱[在 Kibana 中過濾日誌](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#filter_logs)。


## {{site.data.keyword.containershort_notm}} 參照資料
{: reference}

CLI 指令：

* [ibmcloud cs api-key-info](/docs/containers/cs_cli_reference.html#cs_api_key_info)
* [ibmcloud cs logging-config-create](/docs/containers/cs_cli_reference.html#cs_logging_create)
* [ibmcloud cs logging-config-get](/docs/containers/cs_cli_reference.html#cs_logging_get)
* [ibmcloud cs logging-config-update](/docs/containers/cs_cli_reference.html#cs_logging_update)
* [ibmcloud cs logging-config-rm](/docs/containers/cs_cli_reference.html#cs_logging_rm)
* [ibmcloud cs logging-config-refresh](/docs/containers/cs_cli_reference.html#cs_logging_refresh)

