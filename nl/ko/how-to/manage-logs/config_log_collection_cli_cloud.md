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

# {{site.data.keyword.loganalysisshort}} CLI 구성
{: #config_log_collection_cli}

{{site.data.keyword.loganalysisshort}} 서비스에는 클라우드에서 로그 관리에 사용할 수 있는 명령행 인터페이스(CLI)가 포함됩니다. {{site.data.keyword.Bluemix_notm}} 플러그인을 사용하여 로그 상태를 보고 로그를 다운로드하고 로그 보존 정책을 구성할 수 있습니다. CLI는 여러 유형의 도움말을 제공합니다. CLI 및 지원되는 명령에 대해 알기 위한 일반 도움말, 명령 사용 방법을 알기 위한 명령 도움말 또는 명령의 하위 명령 사용 방법을 알기 위한 하위 명령 도움말이 있습니다.
{:shortdesc}


## {{site.data.keyword.Bluemix_notm}} 저장소에서 {{site.data.keyword.loganalysisshort}} 플러그인 설치
{: #install_cli_repo}

{{site.data.keyword.loganalysisshort}} CLI를 설치하려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}} CLI를 설치하십시오.

   자세한 정보는 [{{site.data.keyword.Bluemix_notm}} CLI 설치](/docs/cli/index.html#overview)를 참조하십시오.
   
2. 저장소에서 플러그인의 이름을 찾으십시오. 다음 명령을 실행하십시오.

    ```
    ibmcloud plugin repo-plugins
    ```
    {: codeblock}
    
    플러그인의 이름은 **logging-cli**입니다.

3. {{site.data.keyword.loganalysisshort}} 플러그인을 설치하십시오. 다음 명령을 실행하십시오.

    ```
    ibmcloud plugin install logging-cli -r Bluemix
    ```
    {: codeblock}
 
4. {{site.data.keyword.loganalysisshort}} 플러그인이 설치되었는지 확인하십시오.
  
    예를 들어, 다음 명령을 실행하여 설치된 플러그인의 목록을 확인하십시오.
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    출력은 다음과 같습니다.
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}


## 파일에서 {{site.data.keyword.loganalysisshort}} 플러그인 설치
{: #install_cli}

{{site.data.keyword.loganalysisshort}} CLI를 설치하려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}} CLI를 설치하십시오.

   자세한 정보는 [{{site.data.keyword.Bluemix_notm}} CLI 설치](/docs/cli/index.html#overview)를 참조하십시오.

2. {{site.data.keyword.loganalysisshort}} 플러그인을 설치하십시오.

    * Linux의 경우 [Linux에서 {{site.data.keyword.loganalysisshort}} 플러그인 설치](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_linux)를 참조하십시오.
    * Windows의 경우 [Windows에서 {{site.data.keyword.loganalysisshort}} 플러그인 설치](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_windows)를 참조하십시오.
    * Mac OS X의 경우 [Mac OS X에서 {{site.data.keyword.loganalysisshort}} 플러그인 설치](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_mac)를 참조하십시오.
 
3. CLI 플러그인의 설치를 확인하십시오.
  
    예를 들면, 플러그인의 버전을 확인하십시오. 다음 명령을 실행하십시오.
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    출력은 다음과 같습니다.
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}
 


## 파일에서 Linux에 Log Analysis 플러그인 설치
{: #install_cli_linux}

Linux에서 로그 콜렉션 플러그인을 설치하려면 다음 단계를 완료하십시오.

1. 플러그인을 설치하십시오.

    [{{site.data.keyword.Bluemix_notm}} CLI 페이지](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins)에서 {{site.data.keyword.loganalysisshort}} 서비스 CLI 플러그인(IBM-Logging)의 최신 릴리스를 다운로드하십시오. 
	
	* 플랫폼 값 **linux64**를 선택하십시오. 
	
	* **파일 저장**을 클릭하십시오. 
    
2. 플러그인을 설치하십시오. 다음 명령을 실행하십시오.
        
    ```
    ibmcloud plugin install -f logging-cli-linux-amd64-0.1.1
    ```
    {: codeblock}




## 파일에서 Windows에 Log Analysis 플러그인 설치
{: #install_cli_windows}

Windows에서 로그 콜렉션 플러그인을 설치하려면 다음 단계를 완료하십시오.

1. [{{site.data.keyword.Bluemix_notm}} CLI 페이지](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins)에서 {{site.data.keyword.loganalysisshort}} 서비스 CLI 플러그인(IBM-Logging)의 최신 릴리스를 다운로드하십시오. 
	
	1. 플랫폼 값 **win64**를 선택하십시오. 
	2. **파일 저장**을 클릭하십시오.  
    
2. 플러그인을 설치하십시오. 다음 명령을 실행하십시오.
        
    ```
    ibmcloud plugin install -f logging-cli-windows-amd64-0.1.1.exe
    ```
    {: codeblock}

	

## 파일에서 Mac OS X에 Log Analysis 플러그인 설치
{: #install_cli_mac}

Mac OS X에서 로그 콜렉션 플러그인을 설치하려면 다음 단계를 완료하십시오.

1. [{{site.data.keyword.Bluemix_notm}} CLI 페이지](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins)에서 {{site.data.keyword.loganalysisshort}} 서비스 CLI 플러그인(IBM-Logging)의 최신 릴리스를 다운로드하십시오. 
	
	1. 플랫폼 값 **osx**를 선택하십시오. 
	2. **파일 저장**을 클릭하십시오.  
    
2. 파일의 권한을 변경하십시오. 다음 명령을 실행하십시오.

    ```
    chmod u+x logging-cli-darwin-amd64-0.1.1
    ```
     {: codeblock}

3. 플러그인을 설치하십시오. 다음 명령을 실행하십시오.
        
    ```
    ibmcloud plugin install -f logging-cli-darwin-amd64-0.1.1
    ```
    {: codeblock}

	
	
## Log Analysis CLI 설치
{: #uninstall_cli}

로깅 CLI를 설치 제거하려면 플러그인을 삭제하십시오.
{:shortdesc}

{{site.data.keyword.loganalysisshort}} 서비스 CLI를 설치 제거하려면 다음 단계를 완료하십시오.

1. 설치된 로깅 CLI 플러그인의 버전을 확인하십시오.
  
    예를 들면, 플러그인의 버전을 확인하십시오. 다음 명령을 실행하십시오.
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    출력은 다음과 같습니다.
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}
    
2. 플러그인이 설치되어 있는 경우에는 `ibmcloud plugin uninstall`을 실행하여 로깅 CLI 플러그인을 설치 제거하십시오.

    다음 명령을 실행하십시오.
        
    ```
    ibmcloud plugin uninstall logging-cli
    ```
    {: codeblock}
  

## 저장소에서 Log Analysis CLI 업데이트
{: #update_cli}

로깅 CLI를 업데이트하려면 *ibmcloud plugin update* 명령을 실행하십시오.
{:shortdesc}

{{site.data.keyword.loganalysisshort}} 서비스 CLI를 업데이트하려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.loganalysisshort}} 플러그인을 업데이트하십시오. 다음 명령을 실행하십시오.

    ```
    ibmcloud plugin update logging-cli -r Bluemix
    ```
    {: codeblock}
 
2. CLI 플러그인의 설치를 확인하십시오.
  
    예를 들어, 플러그인의 버전을 확인하십시오. 다음 명령을 실행하십시오.
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    출력은 다음과 같습니다.
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}





## 일반 도움말 가져오기
{: #general_cli_help}

CLI 및 지원되는 명령에 대한 일반적인 정보를 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
    
2. 지원되는 명령 및 CLI에 대한 정보를 나열합니다. 다음 명령을 실행하십시오.

    ```
    ibmcloud logging help 
    ```
    {: codeblock}
    
    

## 명령에 대한 도움말 가져오기
{: #command_cli_help}

명령을 사용하는 방법에 대한 도움말을 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
    
2. 지원되는 명령의 목록을 가져오고 필요로 하는 명령을 식별합니다. 다음 명령을 실행하십시오.

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. 명령에 대한 도움말을 가져옵니다. 다음 명령을 실행하십시오.

    ```
    ibmcloud logging help *Command*
    ```
    {: codeblock}
    
    여기서 *Command*는 CLI 명령의 이름입니다(예: *상태*).



## 하위 명령에 대한 도움말 가져오기
{: #subcommand_cli_help}

명령에는 하위 명령이 있을 수 있습니다. 하위 명령에 대한 도움말을 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
    
2. 지원되는 명령의 목록을 가져오고 필요로 하는 명령을 식별합니다. 다음 명령을 실행하십시오.

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. 명령에 대한 도움말을 가져오고 지원되는 하위 명령을 식별합니다. 다음 명령을 실행하십시오.

    ```
    ibmcloud logging help *Command*
    ```
    {: codeblock}
    
    여기서 *Command*는 CLI 명령의 이름입니다(예: *세션*).

4. 명령에 대한 도움말을 가져오고 지원되는 하위 명령을 식별합니다. 다음 명령을 실행하십시오.

    ```
    ibmcloud logging *Command* help *Subcommand*
    ```
    {: codeblock}
    
    여기서 
    
    * *Command*는 CLI 명령의 이름입니다(예: *상태*).
    * *Subcommand*는 지원되는 하위 명령의 이름입니다. 예를 들면, *session* 명령의 경우 올바른 하위 명령은 *list*입니다.


## 플러그인의 세부사항 표시
{: #show}
  
플러그인 세부사항을 표시하려면 'ibmcloud plugin show logging-cli' 명령을 사용하십시오. 

```
ibmcloud plugin show logging-cli
```
{: codeblock}
    
출력은 다음과 같습니다.
   
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

