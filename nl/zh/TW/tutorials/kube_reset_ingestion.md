---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, kubernetes, tutorial, reset ingestion key

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


# 重設 Kubernetes 叢集用來將日誌轉遞至 {{site.data.keyword.la_full_notm}} 實例的汲取金鑰
{: #kube_reset}

如果您用來將日誌從叢集轉遞至 {{site.data.keyword.cloud_notm}} 中 {{site.data.keyword.la_full_notm}}實例的汲取金鑰已遭洩露，您必須重設金鑰，並更新 Kubernetes 叢集配置以使用新的汲取金鑰。
{:shortdesc}

## 開始之前
{: #kube_reset_prereqs}

在美國南部地區工作。這兩個資源，{{site.data.keyword.la_full_notm}} 實例及 Kubernetes 叢集必須以相同的帳戶執行。

{{site.data.keyword.la_full_notm}} 實例佈建在 **Default** 資源群組中。

閱讀 {{site.data.keyword.la_full_notm}} 的相關資訊。如需相關資訊，請參閱[關於 LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about)。

若要完成本指導教學中的步驟，您的 {{site.data.keyword.IBM_notm}} ID 必須已為下列每一個資源指派 IAM 原則： 

| 資源                             | 存取原則的範圍 | 角色    | 地區    | 資訊                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| 資源群組 **Default**           |  資源群組            | 檢視者  | 美國南部  | 需要此原則，以容許使用者查看 Default 資源群組中的服務實例。|
| {{site.data.keyword.la_full_notm}} 服務 |  資源群組            | 編輯者  </br> 管理員 | 美國南部  | 需要此原則，以容許使用者重設汲取金鑰。|
| Kubernetes 叢集實例          | 資源                             | 編輯者  | 美國南部  | 需要有此原則，才能在 Kubernetes 叢集中刪除及配置密碼和 LogDNA 代理程式。|
{: caption="表 1. 完成指導教學所需的 IAM 原則清單" caption-side="top"} 

如需 {{site.data.keyword.containerlong}} IAM 角色的相關資訊，請參閱[使用者存取權](/docs/containers?topic=containers-access_reference#access_reference)。

安裝 {{site.data.keyword.cloud_notm}} CLI 及 Kubernetes CLI 外掛程式。如需相關資訊，請參閱[安裝 {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli)。


## 步驟 1：重設汲取金鑰
{: #kube_reset_step1}

若要使用 {{site.data.keyword.la_full_notm}} Web 使用者介面更新 {{site.data.keyword.la_full_notm}} 實例的汲取金鑰，請完成下列步驟：

1. 啟動 {{site.data.keyword.la_full_notm}} Web 使用者介面。如需相關資訊，請參閱[啟動 {{site.data.keyword.la_full_notm}} Web 使用者介面](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)。

2. 選取**配置**圖示。然後，選取**組織**。 

3. 選取 **API 金鑰**。

    您可以看到已建立的汲取金鑰。 

4. 選取**產生汲取金鑰**。

    這時會在清單中新增一個新的金鑰。

5. 刪除舊的汲取金鑰。按一下**刪除**。


## 步驟 2：移除叢集中使用舊汲取金鑰的任何配置
{: #kube_reset_step2}

請完成下列步驟：

1. 開啟終端機。然後，登入 {{site.data.keyword.cloud_notm}}。執行下列指令，並遵循下列提示：

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    選取您已佈建 {{site.data.keyword.la_full_notm}} 實例的帳戶。

2. 設定叢集環境。請執行下列指令：

    首先，使用指令來設定環境變數，並下載 Kubernetes 配置檔。

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    配置檔下載完成之後，會顯示一個指令，可讓您用來將本端 Kubernetes 配置檔的路徑設為環境變數。

    然後，複製並貼上終端機中顯示的指令，以設定 KUBECONFIG 環境變數。

    **附註：**每次您登入 {{site.data.keyword.containerlong}} CLI 來使用叢集時，您必須執行這些指令，將叢集配置檔的路徑設為階段作業變數。Kubernetes CLI 會使用此變數來尋找與 {{site.data.keyword.cloud_notm}} 中的叢集連接所需的本端配置檔及憑證。

3. 從 Kubernetes 叢集移除密碼。Kubernetes 密碼包含 LogDNA 汲取金鑰。請執行下列指令：

    ```
    kubectl delete secret logdna-agent-key
    ```
    {: codeblock}

4. 在您 Kubernetes 叢集的每個工作者（節點）上移除 LogDNA 代理程式。LogDNA 代理程式負責收集及轉遞日誌。請執行下列指令：

    ```
    kubectl delete daemonset logdna-agent
    ```
    {: codeblock}

5. 驗證是否已順利刪除 LogDNA 代理程式。請執行下列指令：

    ```
    kubectl get pods
    ```
    {: codeblock}

    您應該看不到任何 LogDNA Pod。


## 步驟 3：使用新的汲取金鑰來配置您的 Kubernetes 叢集
{: #kube_reset_step3}

若要將您的 Kubernetes 叢集配置為將日誌轉遞至 LogDNA 實例，請從指令行完成下列步驟：

1. 開啟終端機。然後，登入 {{site.data.keyword.cloud_notm}}。執行下列指令，並遵循下列提示：

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    選取您已佈建 {{site.data.keyword.la_full_notm}} 實例的帳戶。

2. 設定叢集環境。請執行下列指令：

    首先，使用指令來設定環境變數，並下載 Kubernetes 配置檔。

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    配置檔下載完成之後，會顯示一個指令，可讓您用來將本端 Kubernetes 配置檔的路徑設為環境變數。

    然後，複製並貼上終端機中顯示的指令，以設定 KUBECONFIG 環境變數。

    **附註：**每次您登入 {{site.data.keyword.containerlong}} CLI 來使用叢集時，您必須執行這些指令，將叢集配置檔的路徑設為階段作業變數。Kubernetes CLI 會使用此變數來尋找與 {{site.data.keyword.cloud_notm}} 中的叢集連接所需的本端配置檔及憑證。

3. 將密碼新增至您的 Kubernetes 叢集。請執行下列指令：

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE
    ```
    {: codeblock}

    LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE 顯示實例的 LogDNA 汲取金鑰。

    Kubernetes 密碼包含 LogDNA 汲取金鑰。LogDNA 汲取金鑰用來與 {{site.data.keyword.la_full_notm}} 服務搭配使用，以鑑別記載代理程式。其用來開啟記載後端系統上汲取伺服器的安全 Web Socket。

4. 在您 Kubernetes 叢集的每個工作者（節點）上配置 LogDNA 代理程式。請執行下列指令：

    ```
    kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
    ```
    {: codeblock}

    LogDNA 代理程式負責收集及轉遞日誌。

    代理程式會自動收集副檔名為 *.log 的日誌，以及位於 /var/log 下的無副檔名檔案。依預設，會收集來自所有名稱空間中的日誌，包括 kube-system。

5. 驗證是否已順利建立 LogDNA 代理程式及其狀態。請執行下列指令：

    ```
    kubectl get pods
    ```
    {: codeblock}


## 步驟 4：啟動 LogDNA Web 使用者介面
{: #kube_reset_step4}

若要透過 {{site.data.keyword.cloud_notm}} 使用者介面來啟動 IBM Log Analysis with LogDNA 儀表板，請完成下列步驟：

1. 登入您的 {{site.data.keyword.cloud_notm}} 帳戶。

    按一下 [{{site.data.keyword.cloud_notm}} 儀表板 ![外部鏈結圖示](../../icons/launch-glyph.svg "外部鏈結圖示")](https://cloud.ibm.com/login){:new_window}，以啟動 {{site.data.keyword.cloud_notm}} 儀表板。

	使用您的使用者 ID 和密碼登入之後，即會開啟 {{site.data.keyword.cloud_notm}} 儀表板。

2. 在導覽功能表中，選取**觀察**。 

3. 選取**記載**。 

    即會顯示 {{site.data.keyword.cloud_notm}} 上可用的 {{site.data.keyword.la_full_notm}} 實例清單。

3. 選取一個實例。然後，按一下**檢視日誌**。

    即會開啟 LogDNA Web 使用者介面，並顯示您的叢集日誌。


## 步驟 5：檢視日誌
{: #kube_reset_step5}

從 LogDNA Web 使用者介面，您可以檢視通過系統的日誌。您可以使用日誌追蹤來檢視日誌。 

**附註：**如果使用**免費**服務方案，您只能追蹤最新的日誌。



## 後續步驟
{: #kube_reset_next_steps}

  如果您要[過濾叢集日誌](https://docs.logdna.com/docs/filters)、[搜尋叢集日誌](https://docs.logdna.com/docs/search)、[定義視圖](https://docs.logdna.com/docs/views)以及[配置警示](https://docs.logdna.com/docs/alerts)，則必須將 {{site.data.keyword.la_full_notm}} 方案升級至付費方案。



