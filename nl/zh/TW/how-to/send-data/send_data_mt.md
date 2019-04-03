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

# 將內部部署資料傳送至 IBM Cloud 中的空間
{: #send_data_mt}

若要將日誌資料傳送至 {{site.data.keyword.loganalysisshort}} 服務，您可以配置「多方承租戶 Logstash 轉遞程式 (mt-logstash-forwarder)」。
{: shortdesc}

請完成下列步驟，以在 {{site.data.keyword.Bluemix_notm}} 中將日誌資料傳送至空間：

## 必要條件
{: #prereqs1}

* 用來登入 {{site.data.keyword.Bluemix_notm}} 的 {{site.data.keyword.Bluemix_notm}} ID。
* 有權使用 {{site.data.keyword.loganalysisshort}} 服務處理空間的使用者 ID。如需相關資訊，請參閱[安全](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-security_ov#security_ov)。
* 本端環境中已安裝的 {{site.data.keyword.loganalysisshort}} CLI。
* 以容許日誌汲取的方案將 {{site.data.keyword.loganalysisshort}} 服務佈建在您帳戶的空間中。


## 步驟 1：取得記載記號
{: #get_logging_auth_token}

請從已安裝 {{site.data.keyword.loganalysisshort}} CLI 的終端機階段作業中，完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 執行 `ibmcloud logging token-get` 指令。 

    ```
    ibmcloud logging token-get
    ```
    {: codeblock}

    這個指令會傳回記載記號。
    
    例如，

    ```
    ibmcloud logging token-get
    Getting log token of resource: 93f54jh6-b5f5-46c9-9f0e-kfeutpldnbcf ...
    OK

    Tenant Id                              Logging Token   
    93f54jh6-b5f5-46c9-9f0e-kfeutpldnbcf   oT98_abcdefz   
    ```
    {: screen}

    其中 *Tenant Id* 是您計劃要傳送日誌之空間的 GUID。


## 步驟 2：配置 mt-logstash-forwarder
{: #configure_mt_logstash_forwarder}

請完成下列步驟，以在您計劃要將日誌傳送至 {{site.data.keyword.loganalysisshort}} 服務的環境中配置 mt-logstash-forwarder：

1.	以 root 使用者身分登入。 

    ```
    sudo -s
    ```
    {: codeblock}
    
2.	安裝「網路時間通訊協定 (NTP)」套件，以同步化日誌的時間。 

    例如，針對 Ubunutu 系統，檢查 `timedatectl status` 是否顯示 *Network time on: yes*。如果是，Ubuntu 系統即已配置成使用 NTP，而且您可以跳過此步驟。
    
    ```
    # timedatectl status
    Local time: Mon 2017-06-12 03:01:22 PDT
    Universal time: Mon 2017-06-12 10:01:22 UTC
    RTC time: Mon 2017-06-12 10:01:22
    Time zone: America/Los_Angeles (PDT, -0700)
    Network time on: yes
    NTP synchronized: yes
    RTC in local TZ: no
    ```
    {: screen}
    
    請完成下列步驟，以在 Ubuntu 系統中安裝 NTP：

    1.	執行下列指令，以更新套件。 

        ```
        apt-get update
        ```
        {: codeblock}
        
    2.	執行下列指令，以安裝 ntp 套件。 

        ```
        apt-get install ntp
        ```
        {: codeblock}
        
    3.	執行下列指令，以安裝 ntpdate 套件。 
    
        ```
        apt-get install ntpdate
        ```
        {: codeblock}
        
    4.	執行下列指令，以停止服務。 
        
        ```
        service ntp stop
        ```
        {: codeblock}
        
    5.	執行下列指令，以同步化系統時鐘。 
    
        ```
        ntpdate -u 0.ubuntu.pool.ntp.org
        ```
        {: codeblock}
        
        結果會確認時間已調整，例如：
        
        ```
4 May 19:02:17 ntpdate[5732]: adjust time server 50.116.55.65 offset 0.000685 sec
        ```
        {: screen}
        
    6.	執行下列指令，以重新啟動 ntpd。 
    
        ```
        service ntp start
        ```
        {: codeblock}
    
        結果會確認服務正在啟動。

    7.	執行下列指令，讓 ntpd 服務在當機或重新開機之後自動啟動。 
    
        ```
        service ntp enable
        ```
        {: codeblock}
        
        顯示的結果是可用來管理 ntpd 服務的指令清單，例如：
        
        ```
        Usage: /etc/init.d/ntpd {start|stop|status|restart|try-restart|force-reload}
        ```
        {: screen}

3. 在系統的套件管理程式中，新增 {{site.data.keyword.loganalysisshort}} 服務的儲存庫。執行下列指令：

    ```
    wget -O - https://downloads.opvis.bluemix.net/client/IBM_Logmet_repo_install.sh | bash
    ```
    {: codeblock}

4. 安裝及配置 mt-logstash-forwarder，以將日誌從您的環境傳送至「日誌收集」。 

    1. 執行下列指令，以安裝 mt-logstash-forwarder：
    
        ```
        apt-get install mt-logstash-forwarder 
        ```
        {: codeblock}
        
    2. 建立您環境的 mt-logstash-forwarder 配置檔。此檔案包括的變數可用來配置 mt-logstash-forwarder，以將轉遞程式指向 {{site.data.keyword.loganalysisshort}} 服務。
    
       編輯檔案 `/etc/mt-logstash-forwarder/mt-lsf-config.sh`。例如，您可以使用 vi 編輯器：
               
       ```
       vi /etc/mt-logstash-forwarder/mt-lsf-config.sh
       ```
       {: codeblock}
        
       若要將轉遞程式指向 {{site.data.keyword.loganalysisshort}} 服務，請將下列變數新增至 **mt-lsf-config.sh** 檔案： 
         
       <table>
          <caption>表 1. 將 VM 中的轉遞程式指向 {{site.data.keyword.loganalysisshort}} 服務所需的變數清單</caption>
          <tr>
            <th>變數名稱</th>
            <th>說明</th>
          </tr>
          <tr>
            <td>LSF_INSTANCE_ID</td>
            <td>VM 的 ID。例如，*MyTestVM*。</td>
          </tr>
          <tr>
            <td>LSF_TARGET</td>
            <td>目標 URL。若要取得汲取 URL 清單，請參閱[汲取 URL](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls)。例如，將值設為 **ingest.logging.ng.bluemix.net:9091**，以傳送美國南部地區中的日誌。</td>
          </tr>
          <tr>
            <td>LSF_TENANT_ID</td>
            <td>{{site.data.keyword.loganalysisshort}} 服務已備妥可收集您傳送至 {{site.data.keyword.Bluemix_notm}} 之日誌的空間 ID。<br>請使用您在步驟 1 中取得的值。</td>
          </tr>
          <tr>
            <td>LSF_PASSWORD</td>
            <td>記載記號。<br>請使用您在步驟 1 中取得的值。</td>
          </tr>
          <tr>
            <td>LSF_GROUP_ID</td>
            <td>將此值設為您可定義以分組相關日誌的自訂標籤。</td>
          </tr>
       </table>
        
       例如，請查看下列範例檔案，尋找英國地區中 ID 為 *7d576e3b-170b-4fc2-a6c6-b7166fd57912* 的空間：
        
       ```
       # more mt-lsf-config.sh 
       LSF_INSTANCE_ID="myhelloapp"
       LSF_TARGET="ingest.logging.ng.bluemix.net:9091"
       LSF_TENANT_ID="7d576e3b-170b-4fc2-a6c6-b7166fd57912"
       LSF_PASSWORD="oT98_abcdefz"
       LSF_GROUP_ID="Group1"
       ```
       {: screen}
        
    3. 啟動 mt-logstash-forwarder。 
    
       ```
       service mt-logstash-forwarder start
       ```
       {: codeblock}
                
依預設，轉遞程式只會監看 syslog。在 Kibana 中，可以使用您的日誌來進行分析。
        

## 步驟 3：指定其他日誌檔
{: #add_logs}

依預設，轉遞程式只會監視 /var/log/syslog 檔案。您可以將其他配置檔新增至下列目錄 `/etc/mt-logstash-forwarder/conf.d/syslog.conf/`，讓轉遞程式一併監視它們。 

請完成下列步驟，以新增您環境中所執行應用程式的配置檔：

1.	複製 `/etc/mt-logstash-forwarder/conf.d/syslog.conf` 檔案。 

    **提示：**請不要編輯 syslog.conf 檔案來新增日誌檔。
    
    例如，在 Ubuntu 系統中，執行下列指令：
    
    ```
    cp /etc/mt-logstash-forwarder/conf.d/syslog.conf /etc/mt-logstash-forwarder/conf.d/myapp.conf
    ```
    {: codeblock}
        
2.	使用文字編輯器，編輯 *myapp.conf* 檔案，並將檔案更新成包括您要監視的應用程式日誌。包括每一個應用程式日誌的日誌類型。刪除任何未使用的範例。

3.	重新啟動 mt-logstash-forwarder。 

     重新啟動 mt-logstash-forwarder 服務。執行下列指令：
    
    ```
    service mt-logstash-forwarder restart
    ```
    {: codeblock}

**範例**

若要包括來自 hello 應用程式的 stdout 或 stderr，請將 stdout 或 stderr 重新導向至日誌檔。建立應用程式的轉遞程式配置檔。然後，重新啟動 mt-logstash-forwarder。

1.	複製 `/etc/mt-logstash-forwarder/conf.d/syslog.conf` 檔案。 

    ```
    cp /etc/mt-logstash-forwarder/conf.d/syslog.conf /etc/mt-logstash-forwarder/conf.d/myapp.conf
    ```
    {: codeblock}
    
2. 編輯配置檔 *myapp.conf*。

    若要能夠在汲取日誌時於 Kibana 中依 JSON 欄位搜尋，請啟用 JSON 剖析。將配置檔中特定檔案路徑的 `is_json` 設為 true。對於透過此方式配置的日誌檔，日誌行應該格式化為 JSON 區塊（以換行字元區隔）。mt-logstash-forwarder 接著會使用所有這些 JSON 欄位作為個別 Kibana 可搜尋欄位。JSON 欄位名稱包括根據類型的字尾。
    
    ```
    {
    "files": [
         # other file configurations omitted...
            {
            "paths": [ "/var/log/myhelloapp.log" ],
            "fields": { "type": "helloapplog" },
            "is_json": true
            }
         ]
     }
     ```
     {: screen}
