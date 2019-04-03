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

# 配置 {{site.data.keyword.loganalysisshort}} CLI
{: #config_log_collection_cli}

{{site.data.keyword.loganalysisshort}} 服務包括指令行介面 (CLI)，可用來管理雲端中的日誌。您可以使用 {{site.data.keyword.Bluemix_notm}} 外掛程式來檢視日誌的狀態、下載日誌，以及配置日誌保留原則。CLI 提供不同類型的說明：瞭解 CLI 及所支援指令的一般說明、瞭解如何使用指令的指令說明，或瞭解如何使用指令之次指令的次指令說明。
{:shortdesc}


## 從 {{site.data.keyword.Bluemix_notm}} 儲存庫中安裝 {{site.data.keyword.loganalysisshort}} 外掛程式
{: #install_cli_repo}

若要安裝 {{site.data.keyword.loganalysisshort}} CLI，請完成下列步驟：

1. 安裝 {{site.data.keyword.Bluemix_notm}} CLI。

   如需相關資訊，請參閱[安裝 {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)。
   
2. 在儲存庫中，找出外掛程式的名稱。執行下列指令：

    ```
    ibmcloud plugin repo-plugins
    ```
    {: codeblock}
    
    外掛程式的名稱是 **logging-cli**。

3. 安裝 {{site.data.keyword.loganalysisshort}} 外掛程式。執行下列指令：

    ```
    ibmcloud plugin install logging-cli -r Bluemix
    ```
    {: codeblock}
 
4. 驗證已安裝 {{site.data.keyword.loganalysisshort}} 外掛程式。
  
    例如，執行下列指令，以查看已安裝的外掛程式清單：
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    輸出如下所示：
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}


## 從檔案中安裝 {{site.data.keyword.loganalysisshort}} 外掛程式
{: #install_cli}

若要安裝 {{site.data.keyword.loganalysisshort}} CLI，請完成下列步驟：

1. 安裝 {{site.data.keyword.Bluemix_notm}} CLI。

   如需相關資訊，請參閱[安裝 {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)。

2. 安裝 {{site.data.keyword.loganalysisshort}} 外掛程式。

    * 若為 Linux，請參閱[在 Linux 上安裝 {{site.data.keyword.loganalysisshort}} 外掛程式](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli#install_cli_linux)。
    * 若為 Windows，請參閱[在 Windows 上安裝 {{site.data.keyword.loganalysisshort}} 外掛程式](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli#install_cli_windows)。
    * 若為 Mac OS X，請參閱[在 Mac OS X 上安裝 {{site.data.keyword.loganalysisshort}} 外掛程式](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli#install_cli_mac)。
 
3. 驗證 CLI 外掛程式的安裝。
  
    例如，檢查外掛程式的版本。執行下列指令：
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    輸出如下所示：
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}
 


## 在 Linux 上從檔案中安裝 Log Analysis 外掛程式
{: #install_cli_linux}

請完成下列步驟，以在 Linux 上安裝日誌收集外掛程式：

1. 安裝外掛程式。

    從 [{{site.data.keyword.Bluemix_notm}} CLI 頁面](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins)中，下載 {{site.data.keyword.loganalysisshort}} 服務 CLI 外掛程式 (IBM-Logging) 的最新版本。 
	
	* 選取平台值：**linux64**。 
	
	* 按一下**儲存檔案**。 
    
2. 安裝外掛程式。執行下列指令：
        
    ```
    ibmcloud plugin install -f logging-cli-linux-amd64-0.1.1
    ```
    {: codeblock}




## 在 Windows 上從檔案中安裝 Log Analysis 外掛程式
{: #install_cli_windows}

請完成下列步驟，以在 Windows 上安裝日誌收集外掛程式：

1. 從 [{{site.data.keyword.Bluemix_notm}} CLI 頁面](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins)中，下載 {{site.data.keyword.loganalysisshort}} 服務 CLI 外掛程式 (IBM-Logging) 的最新版本。 
	
	1. 選取平台值：**win64**。 
	2. 按一下**儲存檔案**。  
    
2. 安裝外掛程式。執行下列指令：
        
    ```
    ibmcloud plugin install -f logging-cli-windows-amd64-0.1.1.exe
    ```
    {: codeblock}

	

## 在 Mac OS X 上從檔案中安裝 Log Analysis 外掛程式
{: #install_cli_mac}

請完成下列步驟，以在 Mac OS X 上安裝日誌收集外掛程式：

1. 從 [{{site.data.keyword.Bluemix_notm}} CLI 頁面](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins)中，下載 {{site.data.keyword.loganalysisshort}} 服務 CLI 外掛程式 (IBM-Logging) 的最新版本。 
	
	1. 選取平台值：**osx**。 
	2. 按一下**儲存檔案**。  
    
2. 變更檔案的許可權。執行下列指令：

    ```
chmod u+x logging-cli-darwin-amd64-0.1.1
    ```
     {: codeblock}

3. 安裝外掛程式。執行下列指令：
        
    ```
    ibmcloud plugin install -f logging-cli-darwin-amd64-0.1.1
    ```
    {: codeblock}

	
	
## 解除安裝 Log Analysis CLI
{: #uninstall_cli}

若要解除安裝記載 CLI，請刪除外掛程式。
{:shortdesc}

請完成下列步驟，以解除安裝 {{site.data.keyword.loganalysisshort}} 服務 CLI：

1. 驗證所安裝之記載 CLI 外掛程式的版本。
  
    例如，檢查外掛程式的版本。執行下列指令：
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    輸出如下所示：
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}
    
2. 如果已安裝外掛程式，請執行 `ibmcloud plugin uninstall` 來解除安裝記載 CLI 外掛程式。

    執行下列指令：
        
    ```
    ibmcloud plugin uninstall logging-cli
    ```
    {: codeblock}
  

## 從儲存庫中更新 Log Analysis CLI
{: #update_cli}

若要更新記載 CLI，請執行 *ibmcloud plugin update* 指令。
{:shortdesc}

請完成下列步驟，以更新 {{site.data.keyword.loganalysisshort}} 服務 CLI：

1. 更新 {{site.data.keyword.loganalysisshort}} 外掛程式。執行下列指令：

    ```
    ibmcloud plugin update logging-cli -r Bluemix
    ```
    {: codeblock}
 
2. 驗證 CLI 外掛程式的安裝。
  
    例如，驗證外掛程式的版本。執行下列指令：
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    輸出如下所示：
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}





## 取得一般說明
{: #general_cli_help}

若要取得 CLI 的一般資訊及支援的指令，請完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 列出所支援指令及 CLI 的相關資訊。執行下列指令：

    ```
    ibmcloud logging help 
    ```
    {: codeblock}
    
    

## 取得指令的說明
{: #command_cli_help}

若要取得如何使用指令的說明，請完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 取得所支援指令的清單，並識別您需要的指令。執行下列指令：

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. 取得指令的說明。執行下列指令：

    ```
    ibmcloud logging help *Command*
    ```
    {: codeblock}
    
    其中 *Command* 是 CLI 指令的名稱，例如，*status*。



## 取得次指令的說明
{: #subcommand_cli_help}

指令可以有次指令。若要取得次指令的說明，請完成下列步驟：

1. 登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

    如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 取得所支援指令的清單，並識別您需要的指令。執行下列指令：

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. 取得指令的說明，並識別所支援的次指令。執行下列指令：

    ```
    ibmcloud logging help *Command*
    ```
    {: codeblock}
    
    其中 *Command* 是 CLI 指令的名稱，例如，*session*。

4. 取得指令的說明，並識別所支援的次指令。執行下列指令：

    ```
    ibmcloud logging *Command* help *Subcommand*
    ```
    {: codeblock}
    
    其中 
    
    * *Command* 是 CLI 指令的名稱，例如，*status*。
    * *Subcommand* 是所支援次指令的名稱，例如，指令 *session* 的有效次指令是 *list*。


## 顯示外掛程式的詳細資料
{: #show}
  
請使用 'ibmcloud plugin show logging-cli' 指令，以顯示外掛程式詳細資料。 

```
ibmcloud plugin show logging-cli
```
{: codeblock}
    
輸出如下所示：
   
```
ibmcloud plugin show logging-cli
                                  
Plugin                         logging-cli   
Version                        0.1.1   
Minimal CLI version required   0.5.0   
Commands                                                      
                               logging log-delete       Delete log      
                               logging log-download     Download a log      
                               logging log-show         Show the count, size, and type of logs per day      
                               logging session-create   Create a session      
                               logging session-delete   Delete session      
                               logging sessions         List sessions info      
                               logging session-show     Show a session info      
                               logging option-show      Show the log retention      
                               logging option-update    Show the log options    
```
{: screen}

