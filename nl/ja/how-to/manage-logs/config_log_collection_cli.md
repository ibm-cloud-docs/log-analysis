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

# Log Analysis CLI (CF プラグイン) の構成 (非推奨)
{: #config_log_collection_cli1}

{{site.data.keyword.loganalysisshort}} サービスには、クラウドでログを管理するために使用できるコマンド・ライン・インターフェース (CLI) が組み込まれています。 Cloud Foundry (CF) プラグインを使用して、ログ状況の表示、ログのダウンロード、ログ保存ポリシーの構成を行うことができます。 この CLI にはいくつかの種類のヘルプがあります。一般ヘルプではこの CLI およびサポートされるコマンドについての情報が、コマンド・ヘルプではコマンドの使用方法が、サブコマンド・ヘルプではコマンドに対するサブコマンドの使用方法が提供されます。
{:shortdesc}



## Log Analysis CF プラグインのインストール
{: #install_cli1}

{{site.data.keyword.loganalysisshort}} CLI をインストールするには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} CLI をインストールします。

   詳しくは、[『{{site.data.keyword.Bluemix_notm}}CLI のインストール』](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)を参照してください。

2. {{site.data.keyword.loganalysisshort}} CF プラグインをインストールします。

    * Linux の場合、『[Linux への {{site.data.keyword.loganalysisshort}} CLI のインストール](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli1#install_cli_linux1)』を参照してください。
    * Windows の場合、『[Windows への {{site.data.keyword.loganalysisshort}} CLI のインストール](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli1#install_cli_windows1)』を参照してください。
    * Mac OS X の場合、『[Mac OS X への {{site.data.keyword.loganalysisshort}} CLI のインストール](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli1#install_cli_mac1)』を参照してください。
 
3. CLI プラグインのインストールを検証します。
  
    例えば、プラグインのバージョンを確認します。 次のコマンドを実行します。
    
    ```
    ibmcloud cf plugins
    ```
    {: codeblock}
    
    出力は以下のようになります。
   
    ```
    Invoking 'cf plugins'...

    Listing Installed Plugins...
    OK

    Plugin Name           Version   Command Name   Command Help
    IBM-Logging           1.0.2     logging        IBM Logging plug-in
    ```
    {: screen}
 


## Linux への Log Analysis CLI のインストール
{: #install_cli_linux1}

Linux にLog Collection  CF プラグインをインストールするには、以下のステップを実行します。

1. Log Collection  CLI プラグインをインストールします。

    1. 最新リリースの {{site.data.keyword.loganalysisshort}} サービス CLI プラグイン (IBM-Logging) を [{{site.data.keyword.Bluemix_notm}} CLI ページ](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins)からダウンロードします。 
	
		プラットフォーム値**「linux64」**を選択します。 
		**「ファイルの保存」**をクリックします。 
    
    2. プラグインを unzip します。
    
        例えば、Ubuntu で `logging-cli-linux64.gz` プラグインを unzip するには、次のコマンドを実行します。
        
        ```
        gunzip logging-cli-linux64.gz
        ```
        {: codeblock}

    3. ファイルを実行可能にします。
    
        例えば、ファイル `logging-cli-linux64` を実行可能にするには、次のコマンドを実行します。
        
        ```
        chmod a+x logging-cli-linux64
        ```
        {: codeblock}

    4. ロギング CF プラグインをインストールします。
    
        例えば、ファイル `logging-cli-linux64` を実行可能にするには、次のコマンドを実行します。
        
        ```
        ibmcloud cf install-plugin -f logging-cli-linux64
        ```
        {: codeblock}

2. 環境変数 **LANG** を設定します。

    ご使用のシステム・ロケールが CF でサポートされていない場合は、*LANG* をデフォルト値である *en_US.UTF-8* に設定します。 CF でサポートされるロケールについては、[Getting Started with the cf CLI ![外部リンク・アイコン](../../../../icons/launch-glyph.svg "外部リンク・アイコン")](https://docs.cloudfoundry.org/cf-cli/getting-started.html){: new_window} を参照してください。
	
	例えば、Ubuntu システムでは、*~/.bashrc* ファイルを編集し、以下の行を入力します。
    
    ```
    # add entry for logging CLI
    export LANG = en_US.UTF-8
    ```
    {: codeblock}
    
    新しい端末ウィンドウを開き、次のコマンドを実行して、変数 LANG が設定されていることを検証します。
    
    ```
    $echo LANG
    en_US.UTF-8
    ```
    {: screen}   
    
3. ロギング CLI プラグインのインストールを検証します。
  
    例えば、プラグインのバージョンを確認します。 次のコマンドを実行します。
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    出力は以下のようになります。
   
    ```
    cf logging version 1.0.2
    ```
    {: screen}


## Windows への Log Analysis CLI のインストール
{: #install_cli_windows1}

Windows にLog Collection  CF プラグインをインストールするには、以下のステップを実行します。

1. 最新リリースの {{site.data.keyword.loganalysisshort}} サービス CLI プラグイン (IBM-Logging) を [{{site.data.keyword.Bluemix_notm}} CLI ページ](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins)からダウンロードします。 
	
	1. プラットフォーム値**「win64」**を選択します。 
	2. **「ファイルの保存」**をクリックします。  
    
2. **cf install-plugin** コマンドを実行して、Log Collection プラグインを Windows にインストールします。 

    ```
	ibmcloud cf install-plugin PluginName
	```
	{: codeblock}
	
	ここで、*PluginName* はダウンロードしたファイルの名前です。
	
    例えば、プラグイン「*logging-cli-win64_v1.0.1.exe*」をインストールするには、端末ウィンドウから次のコマンドを実行します。
	
	```
	ibmcloud cf install-plugin logging-cli-win64_v1.0.1.exe
	```
	{: codeblock}
	
    プラグインがインストールされたら、メッセージ「`プラグイン IBM-Logging 1.0.1 は正常にインストールされました`」が表示されます。

3. ロギング CLI プラグインのインストールを検証します。
  
    例えば、プラグインのバージョンを確認します。 次のコマンドを実行します。
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    出力は以下のようになります。
   
    ```
    ibmcloud cf logging version 1.0.1
    ```
    {: screen}
	

## Mac OS X への Log Analysis CLI のインストール
{: #install_cli_mac1}

Mac OS X にLog Collection CF プラグインをインストールするには、以下のステップを実行します。

1. 最新リリースの {{site.data.keyword.loganalysisshort}} サービス CLI プラグイン (IBM-Logging) を [{{site.data.keyword.Bluemix_notm}} CLI ページ](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins)からダウンロードします。 
	
	1. プラットフォーム値**「osx」**を選択します。 
	2. **「ファイルの保存」**をクリックします。  
    
2. **cf install-plugin** コマンドを実行して、Log Collection プラグインを Mac OS X にインストールします。 

    ```
	ibmcloud cf install-plugin PluginName
	```
	{: codeblock}
	
	ここで、*PluginName* はダウンロードしたファイルの名前です。
	
    例えば、プラグイン「*logging-cli-darwin_v1.0.1*」をインストールするには、端末から次のコマンドを実行します。
	
	```
	ibmcloud cf install-plugin logging-cli-darwin_v1.0.1
	```
	{: codeblock}
	
    プラグインがインストールされたら、メッセージ「`プラグイン IBM-Logging 1.0.1 は正常にインストールされました`」が表示されます。

3. ロギング CLI プラグインのインストールを検証します。
  
    例えば、プラグインのバージョンを確認します。 次のコマンドを実行します。
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    出力は以下のようになります。
   
    ```
    ibmcloud cf logging version 1.0.1
    ```
    {: screen}
	
	
## Log Analysis CLI のアンインストール
{: #uninstall_cli1}

ロギング CLI をアンインストールするには、プラグインを削除します。
{:shortdesc}

{{site.data.keyword.loganalysisshort}} サービス CLI をアンインストールするには、以下のステップを実行します。

1. インストールされているロギング CLI プラグインのバージョンを確認します。
  
    例えば、プラグインのバージョンを確認します。 次のコマンドを実行します。
    
    ```
    ibmcloud cf plugins
    ```
    {: codeblock}
    
    出力は以下のようになります。
   
    ```
    Listing Installed Plugins...
    OK

    Plugin Name   Version   Command Name   Command Help
    IBM-Logging   1.0.1     logging        IBM Logging plug-in
    ```
    {: screen}
    
2. プラグインがインストールされている場合、`cf uninstall-plugin` を実行してロギング CLI プラグインをアンインストールします。

    次のコマンドを実行します。
        
    ```
    ibmcloud cf uninstall-plugin IBM-Logging
    ```
    {: codeblock}
  

## 一般ヘルプの利用
{: #general_cli_help1}

CLI に関する一般情報およびサポートされているコマンドについての情報を取得するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)』を参照してください。
    
2. サポートされるコマンドおよび CLI についての情報をリストします。 次のコマンドを実行します。

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}
    
    

## コマンドに関するヘルプの利用
{: #command_cli_help1}

コマンドの使用法に関するヘルプを利用するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)』を参照してください。
    
2. サポートされるコマンドのリストを取得し、必要なコマンドを識別します。 コマンドを実行します。

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}

3. 特定のコマンドに関するヘルプを取得します。 次のコマンドを実行します。

    ```
    ibmcloud cf logging help *Command*
    ```
    {: codeblock}
    
    ここで、*Command* は CLI コマンドの名前です (例: *status*)。



## サブコマンドに関するヘルプの利用
{: #subcommand_cli_help1}

コマンドにはサブコマンドがある場合があります。 サブコマンドに関するヘルプを利用するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)』を参照してください。
    
2. サポートされるコマンドのリストを取得し、必要なコマンドを識別します。 コマンドを実行します。

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}

3. 特定のコマンドに関するヘルプを取得し、サポートされるサブコマンドを識別します。 次のコマンドを実行します。

    ```
    ibmcloud cf logging help *Command*
    ```
    {: codeblock}
    
    ここで、*Command* は CLI コマンドの名前です (例: *session*)。

4. 特定のコマンドに関するヘルプを取得し、サポートされるサブコマンドを識別します。 次のコマンドを実行します。

    ```
    ibmcloud cf logging *Command* help *Subcommand*
    ```
    {: codeblock}
    
    各部分の説明: 
    
    * *Command* は CLI コマンドの名前です (例: *status*)。
    * *Subcommand* はサポートされるサブコマンドの名前です (例: コマンド *session* の有効なサブコマンドは *list* です)。




