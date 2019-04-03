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

# 配置 Log Analysis CLI（CF 插件）（已弃用）
{: #config_log_collection_cli1}

{{site.data.keyword.loganalysisshort}} 服务包含可用于在云中管理日志的命令行界面 (CLI)。可以使用 Cloud Foundry (CF) 插件来查看日志的状态，下载日志以及配置日志保留时间策略。该 CLI 提供了以下不同类型的帮助：了解 CLI 和受支持命令的一般帮助、了解如何使用命令的命令帮助，以及了解如何使用某个命令的子命令的子命令帮助。
{:shortdesc}



## 安装 Log Analysis CF 插件
{: #install_cli1}

要安装 {{site.data.keyword.loganalysisshort}} CLI，请完成以下步骤：

1. 安装 {{site.data.keyword.Bluemix_notm}} CLI。

   有关更多信息，请参阅[安装 {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli/index.html#overview)。

2. 安装 {{site.data.keyword.loganalysisshort}} CF 插件。

    * 对于 Linux，请参阅[在 Linux 上安装 {{site.data.keyword.loganalysisshort}} CLI](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli.html#install_cli_linux1)。
    * 对于 Windows，请参阅[在 Windows 上安装 {{site.data.keyword.loganalysisshort}} CLI](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli.html#install_cli_windows1)。
    * 对于 Mac OS X，请参阅[在 Mac OS X 上安装 {{site.data.keyword.loganalysisshort}} CLI](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli.html#install_cli_mac1)。
 
3. 验证 CLI 插件的安装情况。
  
    例如，检查该插件的版本。运行以下命令：
    
    ```
    ibmcloud cf plugins
    ```
    {: codeblock}
    
    输出如下所示：
   
    ```
    Invoking 'cf plugins'...

    

        Listing Installed Plugins...
    OK

    Plugin Name           Version   Command Name   Command Help
    IBM-Logging           1.0.2     logging        IBM Logging plug-in
    ```
    {: screen}
 


## 在 Linux 上安装 Log Analysis CLI
{: #install_cli_linux1}

要在 Linux 上安装“日志收集”CF 插件，请完成以下步骤：

1. 安装“日志收集”CLI 插件。

    1. 从 [{{site.data.keyword.Bluemix_notm}} CLI 页面](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins)下载 {{site.data.keyword.loganalysisshort}} 服务 CLI 插件 (IBM-Logging) 的最新发行版。 
	
		选择平台值：**linux64**。单击**保存文件**。 
    
    2. 解压缩该插件。
    
        例如，要在 Ubuntu 中解压缩 `logging-cli-linux64.gz` 插件，请运行以下命令：
        
        ```
        gunzip logging-cli-linux64.gz
        ```
        {: codeblock}

    3. 使该文件成为可执行文件。
    
        例如，要使 `logging-cli-linux64` 文件成为可执行文件，请运行以下命令：
        
        ```
        chmod a+x logging-cli-linux64
        ```
        {: codeblock}

    4. 安装日志记录 CF 插件。
    
        例如，要使 `logging-cli-linux64` 文件成为可执行文件，请运行以下命令：
        
        ```
        ibmcloud cf install-plugin -f logging-cli-linux64
        ```
        {: codeblock}

2. 设置环境变量 **LANG**。

    如果 CF 不支持系统语言环境，请将 *LANG* 设置为缺省值 *en_US.UTF-8*。有关 CF 支持的语言环境的信息，请参阅 [cf CLI 入门 ![外部链接图标](../../../../icons/launch-glyph.svg "外部链接图标")](https://docs.cloudfoundry.org/cf-cli/getting-started.html){: new_window}
	
	例如，在 Ubuntu 系统中，编辑 *~/.bashrc* 文件并输入以下行：
    
    ```
    # add entry for logging CLI
    export LANG = en_US.UTF-8
    ```
    {: codeblock}
    
    打开新的终端窗口，然后运行以下命令来验证是否已设置 LANG 变量：
    
    ```
    $echo LANG
    en_US.UTF-8
    ```
    {: screen}   
    
3. 验证日志记录 CLI 插件的安装情况。
  
    例如，检查该插件的版本。运行以下命令：
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    输出如下所示：
   
    ```
    cf logging version 1.0.2
    ```
    {: screen}


## 在 Windows 上安装 Log Analysis CLI
{: #install_cli_windows1}

要在 Windows 上安装“日志收集”CF 插件，请完成以下步骤：

1. 从 [{{site.data.keyword.Bluemix_notm}} CLI 页面](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins)下载 {{site.data.keyword.loganalysisshort}} 服务 CLI 插件 (IBM-Logging) 的最新发行版。 
	
	1. 选择平台值：**win64**。 
	2. 单击**保存文件**。  
    
2. 运行 **cf install-plugin** 命令以在 Windows 上安装“日志收集”插件。 

    ```
	ibmcloud cf install-plugin PluginName
	```
	{: codeblock}
	
	其中，*PluginName* 是所下载文件的名称。
	
    例如，要安装 *logging-cli-win64_v1.0.1.exe* 插件，请在终端窗口中运行以下命令：
	
	```
	ibmcloud cf install-plugin logging-cli-win64_v1.0.1.exe
	```
	{: codeblock}
	
    当插件安装完成时，您会收到以下消息：`IBM-Logging 1.0.1 插件已成功安装。`

3. 验证日志记录 CLI 插件的安装情况。
  
    例如，检查该插件的版本。运行以下命令：
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    输出如下所示：
   
    ```
    ibmcloud cf logging version 1.0.1
    ```
    {: screen}
	

## 在 Mac OS X 上安装 Log Analysis CLI
{: #install_cli_mac1}

要在 Mac OS X 上安装“日志收集”CF 插件，请完成以下步骤：

1. 从 [{{site.data.keyword.Bluemix_notm}} CLI 页面](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins)下载 {{site.data.keyword.loganalysisshort}} 服务 CLI 插件 (IBM-Logging) 的最新发行版。 
	
	1. 选择平台值：**osx**。 
	2. 单击**保存文件**。  
    
2. 运行 **cf install-plugin** 命令，以在 Mac OS X 上安装“日志收集”插件。 

    ```
	ibmcloud cf install-plugin PluginName
	```
	{: codeblock}
	
	其中，*PluginName* 是所下载文件的名称。
	
    例如，要安装 *logging-cli-darwin_v1.0.1* 插件，请在终端上运行以下命令：
	
	```
	ibmcloud cf install-plugin logging-cli-darwin_v1.0.1
	```
	{: codeblock}
	
    当插件安装完成时，您会收到以下消息：`IBM-Logging 1.0.1 插件已成功安装。`

3. 验证日志记录 CLI 插件的安装情况。
  
    例如，检查该插件的版本。运行以下命令：
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    输出如下所示：
   
    ```
    ibmcloud cf logging version 1.0.1
    ```
    {: screen}
	
	
## 卸载 Log Analysis CLI
{: #uninstall_cli1}

要卸载日志记录 CLI，请删除该插件。
{:shortdesc}

要卸载 {{site.data.keyword.loganalysisshort}} 服务 CLI，请完成以下步骤：

1. 验证安装的日志记录 CLI 插件的版本。
  
    例如，检查该插件的版本。运行以下命令：
    
    ```
    ibmcloud cf plugins
    ```
    {: codeblock}
    
    输出如下所示：
   
    ```
    Listing Installed Plugins...
    OK

    Plugin Name   Version   Command Name   Command Help
    IBM-Logging   1.0.1     logging        IBM Logging plug-in
    ```
    {: screen}
    
2. 如果已安装该插件，请运行 `cf uninstall-plugin` 来卸载该日志记录 CLI 插件。

    运行以下命令：
        
    ```
    ibmcloud cf uninstall-plugin IBM-Logging
    ```
    {: codeblock}
  

## 获取一般帮助
{: #general_cli_help1}

要获取有关 CLI 以及受支持命令的常规信息，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
    
2. 列出有关受支持命令和 CLI 的信息。运行以下命令：

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}
    
    

## 获取有关命令的帮助
{: #command_cli_help1}

要获取有关如何使用命令的帮助，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
    
2. 获取受支持命令的列表，并确定您需要的命令。运行以下命令：

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}

3. 获取有关命令的帮助。运行以下命令：

    ```
    ibmcloud cf logging help *Command*
    ```
    {: codeblock}
    
    其中，*Command* 是 CLI 命令的名称，例如 *status*。



## 获取有关子命令的帮助
{: #subcommand_cli_help1}

一个命令可能具有子命令。要获取有关子命令的帮助，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
    
2. 获取受支持命令的列表，并确定您需要的命令。运行以下命令：

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}

3. 获取有关命令的帮助并确定受支持的子命令。运行以下命令：

    ```
    ibmcloud cf logging help *Command*
    ```
    {: codeblock}
    
    其中，*Command* 是 CLI 命令的名称，例如 *session*。

4. 获取有关命令的帮助并确定受支持的子命令。运行以下命令：

    ```
    ibmcloud cf logging *Command* help *Subcommand*
    ```
    {: codeblock}
    
    其中 
    
    * *Command* 是 CLI 命令的名称，例如 *status*。
    * *Subcommand* 是受支持子命令的名称，例如，对于 *session* 命令，有效的子命令是 *list*。




