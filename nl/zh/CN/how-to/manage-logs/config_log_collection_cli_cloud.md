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

{{site.data.keyword.loganalysisshort}} 服务包含可用于在云中管理日志的命令行界面 (CLI)。可以使用 {{site.data.keyword.Bluemix_notm}} 插件来查看日志的状态、下载日志以及配置日志保留时间策略。该 CLI 提供了以下不同类型的帮助：了解 CLI 和受支持命令的一般帮助、了解如何使用命令的命令帮助，以及了解如何使用某个命令的子命令的子命令帮助。
{:shortdesc}


## 通过 {{site.data.keyword.Bluemix_notm}} 存储库安装 {{site.data.keyword.loganalysisshort}} 插件
{: #install_cli_repo}

要安装 {{site.data.keyword.loganalysisshort}} CLI，请完成以下步骤：

1. 安装 {{site.data.keyword.Bluemix_notm}} CLI。

   有关更多信息，请参阅[安装 {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli/index.html#overview)。
   
2. 在存储库中查找插件的名称。运行以下命令：

    ```
    ibmcloud plugin repo-plugins
    ```
    {: codeblock}
    
    插件的名称为 **logging-cli**。

3. 安装 {{site.data.keyword.loganalysisshort}} 插件。运行以下命令：

    ```
    ibmcloud plugin install logging-cli -r Bluemix
    ```
    {: codeblock}
 
4. 验证 {{site.data.keyword.loganalysisshort}} 插件是否已安装。
  
    例如，运行以下命令以查看安装的插件列表：
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    输出如下所示：
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}


## 通过文件安装 {{site.data.keyword.loganalysisshort}} 插件
{: #install_cli}

要安装 {{site.data.keyword.loganalysisshort}} CLI，请完成以下步骤：

1. 安装 {{site.data.keyword.Bluemix_notm}} CLI。

   有关更多信息，请参阅[安装 {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli/index.html#overview)。

2. 安装 {{site.data.keyword.loganalysisshort}} 插件。

    * 对于 Linux，请参阅[在 Linux 上安装 {{site.data.keyword.loganalysisshort}} 插件](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_linux)。
    * 对于 Windows，请参阅[在 Windows 上安装 {{site.data.keyword.loganalysisshort}} 插件](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_windows)。
    * 对于 Mac OS X，请参阅[在 Mac OS X 上安装 {{site.data.keyword.loganalysisshort}} 插件](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_mac)。
 
3. 验证 CLI 插件的安装情况。
  
    例如，检查该插件的版本。运行以下命令：
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    输出如下所示：
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}
 


## 在 Linux 上通过文件安装 Log Analysis 插件
{: #install_cli_linux}

要在 Linux 上安装 Log Analysis 插件，请完成以下步骤：

1. 安装插件。

    从 [{{site.data.keyword.Bluemix_notm}} CLI 页面](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins)下载 {{site.data.keyword.loganalysisshort}} 服务 CLI 插件 (IBM-Logging) 的最新发行版。 
	
	* 选择平台值：**linux64**。 
	
	* 单击**保存文件**。 
    
2. 安装插件。运行以下命令：
        
    ```
    ibmcloud plugin install -f logging-cli-linux-amd64-0.1.1
    ```
    {: codeblock}




## 在 Windows 上通过文件安装 Log Analysis 插件
{: #install_cli_windows}

要在 Windows 上安装 Log Analysis 插件，请完成以下步骤：

1. 从 [{{site.data.keyword.Bluemix_notm}} CLI 页面](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins)下载 {{site.data.keyword.loganalysisshort}} 服务 CLI 插件 (IBM-Logging) 的最新发行版。 
	
	1. 选择平台值：**win64**。 
	2. 单击**保存文件**。  
    
2. 安装插件。运行以下命令：
        
    ```
    ibmcloud plugin install -f logging-cli-windows-amd64-0.1.1.exe
    ```
    {: codeblock}

	

## 在 Mac OS X 上通过文件安装 Log Analysis 插件
{: #install_cli_mac}

要在 Mac OS X 上安装 Log Analysis 插件，请完成以下步骤：

1. 从 [{{site.data.keyword.Bluemix_notm}} CLI 页面](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins)下载 {{site.data.keyword.loganalysisshort}} 服务 CLI 插件 (IBM-Logging) 的最新发行版。 
	
	1. 选择平台值：**osx**。 
	2. 单击**保存文件**。  
    
2. 更改文件的许可权。运行以下命令：

    ```
chmod u+x logging-cli-darwin-amd64-0.1.1
    ```
     {: codeblock}

3. 安装插件。运行以下命令：
        
    ```
    ibmcloud plugin install -f logging-cli-darwin-amd64-0.1.1
    ```
    {: codeblock}

	
	
## 卸载 Log Analysis CLI
{: #uninstall_cli}

要卸载日志记录 CLI，请删除该插件。
{:shortdesc}

要卸载 {{site.data.keyword.loganalysisshort}} 服务 CLI，请完成以下步骤：

1. 验证安装的日志记录 CLI 插件的版本。
  
    例如，检查该插件的版本。运行以下命令：
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    输出如下所示：
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}
    
2. 如果日志记录 CLI 插件已安装，请运行 `ibmcloud plugin uninstall` 来卸载该插件。

    运行以下命令：
        
    ```
    ibmcloud plugin uninstall logging-cli
    ```
    {: codeblock}
  

## 更新存储库中的 Log Analysis CLI
{: #update_cli}

要更新日志记录 CLI，请运行 *ibmcloud plugin update* 命令。
{:shortdesc}

要更新 {{site.data.keyword.loganalysisshort}} 服务 CLI，请完成以下步骤：

1. 更新 {{site.data.keyword.loganalysisshort}} 插件。运行以下命令：

    ```
    ibmcloud plugin update logging-cli -r Bluemix
    ```
    {: codeblock}
 
2. 验证 CLI 插件的安装情况。
  
    例如，验证插件的版本。运行以下命令：
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    输出如下所示：
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}





## 获取一般帮助
{: #general_cli_help}

要获取有关 CLI 以及受支持命令的常规信息，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
    
2. 列出有关受支持命令和 CLI 的信息。运行以下命令：

    ```
    ibmcloud logging help 
    ```
    {: codeblock}
    
    

## 获取有关命令的帮助
{: #command_cli_help}

要获取有关如何使用命令的帮助，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
    
2. 获取受支持命令的列表，并确定您需要的命令。运行以下命令：

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. 获取有关命令的帮助。运行以下命令：

    ```
    ibmcloud logging help *Command*
    ```
    {: codeblock}
    
    其中，*Command* 是 CLI 命令的名称，例如 *status*。



## 获取有关子命令的帮助
{: #subcommand_cli_help}

一个命令可能具有子命令。要获取有关子命令的帮助，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
    
2. 获取受支持命令的列表，并确定您需要的命令。运行以下命令：

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. 获取有关命令的帮助并确定受支持的子命令。运行以下命令：

    ```
    ibmcloud logging help *Command*
    ```
    {: codeblock}
    
    其中，*Command* 是 CLI 命令的名称，例如 *session*。

4. 获取有关命令的帮助并确定受支持的子命令。运行以下命令：

    ```
    ibmcloud logging *Command* help *Subcommand*
    ```
    {: codeblock}
    
    其中 
    
    * *Command* 是 CLI 命令的名称，例如 *status*。
    * *Subcommand* 是受支持子命令的名称，例如，对于 *session* 命令，有效的子命令是 *list*。


## 显示插件的详细信息
{: #show}
  
使用“ibmcloud plugin show logging-cli”命令显示插件详细信息。 

```
ibmcloud plugin show logging-cli
```
{: codeblock}
    
输出如下所示：
   
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

