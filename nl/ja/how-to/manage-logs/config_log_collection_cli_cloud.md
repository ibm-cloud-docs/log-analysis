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

# {{site.data.keyword.loganalysisshort}} CLI の構成
{: #config_log_collection_cli}

{{site.data.keyword.loganalysisshort}} サービスには、クラウドでログを管理するために使用できるコマンド・ライン・インターフェース (CLI) が組み込まれています。 {{site.data.keyword.Bluemix_notm}} プラグインを使用して、ログ状況の表示、ログのダウンロード、ログ保存ポリシーの構成を行うことができます。 この CLI にはいくつかの種類のヘルプがあります。一般ヘルプではこの CLI およびサポートされるコマンドについての情報が、コマンド・ヘルプではコマンドの使用方法が、サブコマンド・ヘルプではコマンドに対するサブコマンドの使用方法が提供されます。
{:shortdesc}


## {{site.data.keyword.Bluemix_notm}} リポジトリーからの {{site.data.keyword.loganalysisshort}} プラグインのインストール
{: #install_cli_repo}

{{site.data.keyword.loganalysisshort}} CLI をインストールするには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} CLI をインストールします。

   詳しくは、[『{{site.data.keyword.Bluemix_notm}}CLI のインストール』](/docs/cli/index.html#overview)を参照してください。
   
2. リポジトリー内にあるプラグインの名前を検索します。 次のコマンドを実行します。

    ```
    ibmcloud plugin repo-plugins
    ```
    {: codeblock}
    
    このプラグインの名前は **logging-cli** です。

3. {{site.data.keyword.loganalysisshort}} プラグインをインストールします。 次のコマンドを実行します。

    ```
    ibmcloud plugin install logging-cli -r Bluemix
    ```
    {: codeblock}
 
4. {{site.data.keyword.loganalysisshort}} プラグインがインストールされたことを確認します。
  
    例えば、以下のコマンドを実行して、インストール済みのプラグインのリストを表示します。
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    出力は以下のようになります。
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}


## ファイルからの {{site.data.keyword.loganalysisshort}} プラグインのインストール
{: #install_cli}

{{site.data.keyword.loganalysisshort}} CLI をインストールするには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} CLI をインストールします。

   詳しくは、[『{{site.data.keyword.Bluemix_notm}}CLI のインストール』](/docs/cli/index.html#overview)を参照してください。

2. {{site.data.keyword.loganalysisshort}} プラグインをインストールします。

    * Linux の場合、『[Linux への {{site.data.keyword.loganalysisshort}} プラグインのインストール](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_linux)』を参照してください。
    * Windows の場合、『[Windows への {{site.data.keyword.loganalysisshort}} プラグインのインストール](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_windows)』を参照してください。
    * Mac OS X の場合、『[Mac OS X への {{site.data.keyword.loganalysisshort}} プラグインのインストール](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_mac)』を参照してください。
 
3. CLI プラグインのインストールを検証します。
  
    例えば、プラグインのバージョンを確認します。 次のコマンドを実行します。
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    出力は以下のようになります。
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}
 


## Linux 上でのファイルからの Log Analysis プラグインのインストール
{: #install_cli_linux}

Linux にLog Collection プラグインをインストールするには、以下のステップを実行します。

1. プラグインをインストールします。

    最新リリースの {{site.data.keyword.loganalysisshort}} サービス CLI プラグイン (IBM-Logging) を [{{site.data.keyword.Bluemix_notm}} CLI ページ](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins)からダウンロードします。 
	
	* プラットフォーム値**「linux64」**を選択します。 
	
	* **「ファイルの保存」**をクリックします。 
    
2. プラグインをインストールします。 次のコマンドを実行します。
        
    ```
    ibmcloud plugin install -f logging-cli-linux-amd64-0.1.1
    ```
    {: codeblock}




## Windows 上でのファイルからの Log Analysis プラグインのインストール
{: #install_cli_windows}

Windows にLog Collection プラグインをインストールするには、以下のステップを実行します。

1. 最新リリースの {{site.data.keyword.loganalysisshort}} サービス CLI プラグイン (IBM-Logging) を [{{site.data.keyword.Bluemix_notm}} CLI ページ](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins)からダウンロードします。 
	
	1. プラットフォーム値**「win64」**を選択します。 
	2. **「ファイルの保存」**をクリックします。  
    
2. プラグインをインストールします。 次のコマンドを実行します。
        
    ```
    ibmcloud plugin install -f logging-cli-windows-amd64-0.1.1.exe
    ```
    {: codeblock}

	

## Mac OS X 上でのファイルからの Log Analysis プラグインのインストール
{: #install_cli_mac}

Mac OS X にLog Collection プラグインをインストールするには、以下のステップを実行します。

1. 最新リリースの {{site.data.keyword.loganalysisshort}} サービス CLI プラグイン (IBM-Logging) を [{{site.data.keyword.Bluemix_notm}} CLI ページ](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins)からダウンロードします。 
	
	1. プラットフォーム値**「osx」**を選択します。 
	2. **「ファイルの保存」**をクリックします。  
    
2. ファイルの許可を変更します。 次のコマンドを実行します。

    ```
    chmod u+x logging-cli-darwin-amd64-0.1.1
    ```
     {: codeblock}

3. プラグインをインストールします。 次のコマンドを実行します。
        
    ```
    ibmcloud plugin install -f logging-cli-darwin-amd64-0.1.1
    ```
    {: codeblock}

	
	
## Log Analysis CLI のアンインストール
{: #uninstall_cli}

ロギング CLI をアンインストールするには、プラグインを削除します。
{:shortdesc}

{{site.data.keyword.loganalysisshort}} サービス CLI をアンインストールするには、以下のステップを実行します。

1. インストールされているロギング CLI プラグインのバージョンを確認します。
  
    例えば、プラグインのバージョンを確認します。 次のコマンドを実行します。
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    出力は以下のようになります。
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}
    
2. プラグインがインストールされている場合、`ibmcloud plugin uninstall` を実行してロギング CLI プラグインをアンインストールします。

    次のコマンドを実行します。
        
    ```
    ibmcloud plugin uninstall logging-cli
    ```
    {: codeblock}
  

## リポジトリーからの Log Analysis CLI の更新
{: #update_cli}

ロギング CLI を更新するには、*ibmcloud plugin update* コマンドを実行します。
{:shortdesc}

{{site.data.keyword.loganalysisshort}} サービス CLI を更新するには、以下のステップを実行します。

1. {{site.data.keyword.loganalysisshort}} プラグインを更新します。 次のコマンドを実行します。

    ```
    ibmcloud plugin update logging-cli -r Bluemix
    ```
    {: codeblock}
 
2. CLI プラグインのインストールを検証します。
  
    例えば、プラグインのバージョンを検証します。 次のコマンドを実行します。
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    出力は以下のようになります。
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}





## 一般ヘルプの利用
{: #general_cli_help}

CLI に関する一般情報およびサポートされているコマンドについての情報を取得するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
    
2. サポートされるコマンドおよび CLI についての情報をリストします。 次のコマンドを実行します。

    ```
    ibmcloud logging help 
    ```
    {: codeblock}
    
    

## コマンドに関するヘルプの利用
{: #command_cli_help}

コマンドの使用法に関するヘルプを利用するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
    
2. サポートされるコマンドのリストを取得し、必要なコマンドを識別します。 コマンドを実行します。

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. 特定のコマンドに関するヘルプを取得します。 次のコマンドを実行します。

    ```
    ibmcloud logging help *Command*
    ```
    {: codeblock}
    
    ここで、*Command* は CLI コマンドの名前です (例: *status*)。



## サブコマンドに関するヘルプの利用
{: #subcommand_cli_help}

コマンドにはサブコマンドがある場合があります。 サブコマンドに関するヘルプを利用するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
    
2. サポートされるコマンドのリストを取得し、必要なコマンドを識別します。 コマンドを実行します。

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. 特定のコマンドに関するヘルプを取得し、サポートされるサブコマンドを識別します。 次のコマンドを実行します。

    ```
    ibmcloud logging help *Command*
    ```
    {: codeblock}
    
    ここで、*Command* は CLI コマンドの名前です (例: *session*)。

4. 特定のコマンドに関するヘルプを取得し、サポートされるサブコマンドを識別します。 次のコマンドを実行します。

    ```
    ibmcloud logging *Command* help *Subcommand*
    ```
    {: codeblock}
    
    各部分の説明: 
    
    * *Command* は CLI コマンドの名前です (例: *status*)。
    * *Subcommand* はサポートされるサブコマンドの名前です (例: コマンド *session* の有効なサブコマンドは *list* です)。


## プラグインの詳細の表示
{: #show}
  
プラグイン詳細を表示するには、「ibmcloud plugin show logging-cli」コマンドを使用します。 

```
ibmcloud plugin show logging-cli
```
{: codeblock}
    
出力は以下のようになります。
   
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

