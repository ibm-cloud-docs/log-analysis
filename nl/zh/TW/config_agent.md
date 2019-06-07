---

copyright:
  years:  2018, 2019
lastupdated: "2019-05-01"

keywords: LogDNA, IBM, Log Analysis, logging, config agent

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

# 配置 LogDNA 代理程式
{: #config_agent}

LogDNA 代理程式負責收集日誌並將其轉遞至您的 {{site.data.keyword.la_full_notm}} 實例。佈建 {{site.data.keyword.la_full}} 的實例之後，您必須為您要監視的每個日誌來源，配置 LogDNA 代理程式。
{:shortdesc}

* LogDNA 代理程式使用「LogDNA 汲取金鑰」來進行鑑別，並開啟 {{site.data.keyword.la_full_notm}} 汲取伺服器的安全 Web Socket。 
* 依預設，代理程式會監視副檔名為 *.log* 的所有檔案，以及 */var/log/* 下的無副檔名檔案。
* 代理程式會追蹤新的日誌資料，並尋找新增至代理程式所監視之記載目錄的新檔案。

您可以透過 LogDNA 代理程式來配置下列參數： 

| 參數 | 說明 |
|-----------|-------------|
| `tags`    | 定義標籤，以自動將主機分組為動態群組。|
| `logdir`  | 定義您希望代理程式監視的自訂路徑。</br>使用逗點區隔多個路徑。您可以使用 glob 型樣。您可以配置特定的檔案。使用雙引號來輸入 glob 型樣。|
| `exclude` | 定義您不希望 LogDNA 代理程式監視的檔案。**附註：**這些檔案可以位於透過 logdir 參數所定義的任何路徑中。</br>使用逗點區隔多個檔案。您可以使用 glob 型樣。您可以配置特定的檔案。|
| `exclude_regex` | 定義正規表示式型樣，以過濾出符合型樣的任何行。請勿包括前導及尾端 `/`。|
| `hostname` | 定義主機名稱。此值會置換作業系統主機名稱。|
| `autoupdate` | 設為 `1`，可在更新公用儲存庫代理程式定義時自動更新代理程式。設為 `0`，可停用此特性。|  
{: caption="表 1. 用來自訂 LogDNA 代理程式的參數" caption-side="top"} 



## 使用 Script 配置 Kubernetes 叢集上的 LogDNA 代理程式
{: #config_agent_kube_script}

若要將您的 Kubernetes 叢集配置為傳送日誌到您的 {{site.data.keyword.la_full_notm}} 實例，您必須在叢集的每個節點上安裝 *logdna-agent* Pod。LogDNA 代理程式會從安裝它的 Pod 中讀取日誌檔，並將日誌資料轉遞至 LogDNA 實例。

若要將您的 Kubernetes 叢集配置為將日誌轉遞至 LogDNA 實例，請從指令行完成下列步驟：

1. 開啟終端機，以登入 {{site.data.keyword.cloud_notm}}。

   ```
   ibmcloud login -a cloud.ibm.com
   ```
   {: pre}

   選取您佈建 {{site.data.keyword.la_full_notm}} 實例的帳戶。

2. 將您要配置記載的叢集設為此階段作業的環境定義。

   ```
   ibmcloud ks cluster-config <cluster_name_or_ID>
   ```
   {: pre}

   配置檔下載完成之後，會顯示一個指令，可讓您用來將本端 Kubernetes 配置檔的路徑設為環境變數。複製並貼上終端機中顯示的指令，以設定 `KUBECONFIG` 環境變數。

3. 建立 Kubernetes 密碼來儲存您服務實例的 logDNA 汲取金鑰。LogDNA 汲取金鑰用來開啟 logDNA 汲取伺服器的安全 Web Socket，以及與 {{site.data.keyword.la_full_notm}} 服務搭配使用，以鑑別記載代理程式。

    ```
   kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<logDNA_ingestion_key>
   ```
    {: pre}

4. 建立 Kubernetes 常駐程式集，以在 Kubernetes 叢集的每個工作者節點上，部署 LogDNA 代理程式。LogDNA 代理程式會收集副檔名為 `*.log` 的日誌，以及儲存在您 Pod 之 `/var/log` 目錄中的無副檔名檔案。依預設，會收集來自所有名稱空間中的日誌，包括 `kube-system`，並會自動轉遞至 {{site.data.keyword.la_full_notm}} 服務。

    <table>
      <caption>依地區的指令</caption>
      <tr>
        <th> 位置  </th>
        <th>指令</th>
      </tr>
      <tr>
        <td>`US-South`</td>
        <td>`   kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
   `</td>
      </tr>
      <tr>
        <td>`EU-DE`</td>
        <td>`kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-eu-de.yaml`</td>
      </tr>
    </table>

5. 驗證是否已順利部署 LogDNA 代理程式。 

   ```
   kubectl get pods
   ```
   {: pre}
   

當您看到一個以上的 LogDNA Pod 時，表示已成功部署。
* **LogDNA Pod 的數量等於您叢集中的工作者節點數量。** 
* 所有 Pod 都必須處於`執行中`狀態。
* 會自動從所有儲存器收集 *Stdout* 及 *stderr*，並進行轉遞。日誌資料包括應用程式日誌以及工作者節點日誌。 
* 依預設，在工作者節點上執行的 LogDNA 代理程式 Pod 會收集來自該節點上所有名稱空間的日誌，包括 kube-system 日誌。



## 將標籤新增至 Kubernetes 叢集上的 LogDNA 代理程式
{: #config_agent_kube_tags}

請完成下列步驟來新增標籤：

1. 設定叢集環境。請執行下列指令：

    首先，使用指令來設定環境變數，並下載 Kubernetes 配置檔。

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    配置檔下載完成之後，會顯示一個指令，可讓您用來將本端 Kubernetes 配置檔的路徑設為環境變數。

    然後，複製並貼上終端機中顯示的指令，以設定 KUBECONFIG 環境變數。

2. 檢查 DaemonSet 的更新策略。然後，選擇要使用 *kubectl apply* 或 *kubectl edit* 來修改代理程式的配置檔。

    若要檢查更新策略，請執行下列指令：

    ```
    kubectl get ds/logdna-agent -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'
    ```
    {: pre}

    如果更新策略設為 *OnDelete*，或如果您的配置檔是透過版本控制系統來管理，請更新本端配置檔，並使用 *kubectl apply*，將變更套用至 LogDNA 代理程式。

    如果更新策略設為 *RollingUpdate*，則您可以使用 *kibectl edit* 來更新及套用對 LogDNA代理程式所做的變更。

3. 編輯 `logdna-agent-configmap.yaml` 檔。 

    透過修改本端副本來更新配置檔。**附註：**您也可以執行下列指令，來產生代理程式的配置檔：

    ```
    kubectl get daemonset logdna-agent -o=yaml > prod-logdna-agent-ds.yaml
    ```
    {: codeblock}

    或者，使用 *kubectl edit* 來更新配置檔。

    ```
    kubectl edit daemonset logdna-agent
    ```
    {: codeblock}

4. 進行變更。新增 **LOGDNA_TAGS** 區段。

    ```
    - name: LOGDNA_TAGS
        value: tag1,tag2,tag3
    ```
    {: codeblock}

    例如，下列區段顯示在配置檔中新增標籤的位置：

    ```
    apiVersion: extensions/v1beta1
    kind: DaemonSet
    metadata:
      name: logdna-agent
    spec:
      template:
        metadata:
          labels:
            app: logdna-agent
        spec:
          containers:
          - name: logdna-agent
            image: logdna/logdna-agent:latest
            imagePullPolicy: Always
            env:
            - name: LOGDNA_AGENT_KEY
              valueFrom:
                 secretKeyRef:
                  name: logdna-agent-key
                  key: logdna-agent-key
            - name: LDAPIHOST
              value: api.us-south.logging.cloud.ibm.com
            - name: LDLOGHOST
              value: logs.us-south.logging.cloud.ibm.com
            - name: LOGDNA_PLATFORM
              value: k8s
            - name: LOGDNA_TAGS
              value: tag1,tag2,tag3
    ```
    {: screen}

5. 如果您在本端編輯檔案，請套用配置變更。 

    ```
    kubectl apply -f prod-logdna-agent-ds.yaml
    ```
    {: codeblock}
    
    **附註：**如果您使用 *kibectl edit*，當您儲存修改內容時，會自動套用變更。


## 在 Linux Ubuntu 或 Debian 上配置 LogDNA 代理程式
{: #config_agent_linux}

若要將您的 Ubuntu 伺服器配置為傳送日誌到您的 {{site.data.keyword.la_full_notm}} 實例，您必須安裝 `logdna-agent`。LogDNA 代理程式會讀取 */var/log* 中的日誌檔，並將日誌資料轉遞至 LogDNA 實例。

若要將您的 Ubuntu 伺服器配置為將日誌轉遞至 LogDNA 實例，請從 Ubuntu 終端機完成下列步驟：

1. 安裝 LogDNA 代理程式。請執行下列指令：

    ```
    echo "deb https://repo.logdna.com stable main" | sudo tee /etc/apt/sources.list.d/logdna.list 
    ```
    {: codeblock}

    ```
    wget -O- https://repo.logdna.com/logdna.gpg | sudo apt-key add - 
    ```
    {: codeblock}

    ```
    sudo apt-get update
    ```
    {: codeblock}

    ```
    sudo apt-get install logdna-agent < "/dev/null"
    ```
    {: codeblock}

2. 設定汲取金鑰，LogDNA 代理程式必須使用該金鑰才能將日誌轉遞至 {{site.data.keyword.la_full_notm}} 實例。  

    ```
    sudo logdna-agent -k INGESTION_KEY
    ```
    {: codeblock}

    其中，INGESTION_KEY 包含對您配置要轉遞日誌的 {{site.data.keyword.la_full_notm}} 實例有效的汲取金鑰。

3. 設定鑑別端點。LogDNA 代理程式會使用此主機進行鑑別，並使用記號轉遞日誌。

    <table>
      <caption>依地區的指令</caption>
      <tr>
        <th> 位置  </th>
        <th>指令</th>
      </tr>
      <tr>
        <td>`US-South`</td>
        <td>`    sudo logdna-agent -s LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com
    `</td>
      </tr>
      <tr>
        <td>`EU-DE`</td>
        <td>`sudo logdna-agent -s LOGDNA_APIHOST=api.eu-de.logging.cloud.ibm.com`</td>
      </tr>
    </table>

4. 設定汲取端點。

    <table>
      <caption>依地區的指令</caption>
      <tr>
        <th> 位置  </th>
        <th>指令</th>
      </tr>
      <tr>
        <td>`US-South`</td>
        <td>`    sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com
    `</td>
      </tr>
      <tr>
        <td>`EU-DE`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.eu-de.logging.cloud.ibm.com`</td>
      </tr>
    </table>

5. 定義更多要監視的日誌路徑。請執行下列指令： 

    ```
    sudo logdna-agent -d /path/to/log/folders
    ```
    {: codeblock}

    依預設，會監視 **/var/log**。

6. 選擇性地配置 LogDNA 代理程式，以標記您的主機。 


## 在 Linux Ubuntu 或 Debian 上新增標籤至 LogDNA 代理程式
{: #config_agent-linux_tags}
 

請完成下列步驟，以將其他標籤新增至 LogDNA 代理程式：

1. 驗證 LogDNA 代理程式是否正在執行中。

2. 新增一個以上的標籤。

    ```
    sudo logdna-agent -t TAG1,TAG2 
    ```
    {: codeblock}


您也可以編輯 LogDNA 配置檔，並新增標籤。配置檔位於 */etc/logdna.conf*。

1. 編輯檔案。

    ```
    sudo update-rc.d logdna-agent defaults
    ```
    {: codeblock}

2. 新增標籤。

3. 重新啟動 LogDNA 代理程式。

    ``` 
    sudo /etc/init.d/logdna-agent start
    ```
    {: codeblock}














