---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, detach config agent

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

# 從實例分離 LogDNA 代理程式
{: #detach_agent}

從記載實例分離 LogDNA 代理程式以停止收集日誌。
{:shortdesc}

## 從 Kubernetes 叢集分離 LogDNA 代理程式
{: #detach_agent_kube}

若要停止 Kubernetes 叢集繼續傳送日誌到 {{site.data.keyword.la_full_notm}} 實例，您必須從您的叢集移除 LogDNA 代理程式。 

若要停止 Kubernetes 叢集繼續將日誌轉遞到 LogDNA 實例，請從指令行完成下列步驟：

1. 開啟終端機。然後，[登入 {{site.data.keyword.cloud_notm}} ![外部鏈結圖示](../../icons/launch-glyph.svg "外部鏈結圖示")](https://cloud.ibm.com/login){:new_window}，並遵循提示。

    選取您佈建 {{site.data.keyword.la_full_notm}} 實例的帳戶。

2. 設定叢集環境。請執行下列指令：

    首先，使用指令來設定環境變數，並下載 Kubernetes 配置檔。

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    配置檔下載完成之後，會顯示一個指令，可讓您用來將本端 Kubernetes 配置檔的路徑設為環境變數。

    然後，複製並貼上終端機中顯示的指令，以設定 `KUBECONFIG` 環境變數。

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




