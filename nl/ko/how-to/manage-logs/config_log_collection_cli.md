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

# Log Analysis CLI(CF 플러그인) 구성(더 이상 사용되지 않음)
{: #config_log_collection_cli1}

{{site.data.keyword.loganalysisshort}} 서비스에는 클라우드에서 로그 관리에 사용할 수 있는 명령행 인터페이스(CLI)가 포함됩니다. CF(Cloud Foundry) 플러그인을 사용하여 로그 상태를 보고 로그를 다운로드하고 로그 보존 정책을 구성할 수 있습니다. CLI는 여러 유형의 도움말을 제공합니다. CLI 및 지원되는 명령에 대해 알기 위한 일반 도움말, 명령 사용 방법을 알기 위한 명령 도움말 또는 명령의 하위 명령 사용 방법을 알기 위한 하위 명령 도움말이 있습니다.
{:shortdesc}



## Log Analysis CF 플러그인 설치
{: #install_cli1}

{{site.data.keyword.loganalysisshort}} CLI를 설치하려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}} CLI를 설치하십시오.

   자세한 정보는 [{{site.data.keyword.Bluemix_notm}} CLI 설치](/docs/cli/index.html#overview)를 참조하십시오.

2. {{site.data.keyword.loganalysisshort}} CF 플러그인을 설치하십시오.

    * Linux의 경우 [Linux에서 {{site.data.keyword.loganalysisshort}} CLI 설치](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli.html#install_cli_linux1)를 참조하십시오.
    * Windows의 경우 [Windows에서 {{site.data.keyword.loganalysisshort}} CLI 설치](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli.html#install_cli_windows1)를 참조하십시오.
    * Mac OS X의 경우 [Mac OS X에서 {{site.data.keyword.loganalysisshort}} CLI 설치](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli.html#install_cli_mac1)를 참조하십시오.
 
3. CLI 플러그인의 설치를 확인하십시오.
  
    예를 들면, 플러그인의 버전을 확인하십시오. 다음 명령을 실행하십시오.
    
    ```
    ibmcloud cf plugins
    ```
    {: codeblock}
    
    출력은 다음과 같습니다.
   
    ```
    Invoking 'cf plugins'...

    Listing Installed Plugins...
    OK

    Plugin Name           Version   Command Name   Command Help
    IBM-Logging           1.0.2     logging        IBM Logging plug-in
    ```
    {: screen}
 


## Linux에서 Log Analysis CLI 설치
{: #install_cli_linux1}

Linux에서 로그 콜렉션 CF 플러그인을 설치하려면 다음 단계를 완료하십시오.

1. 로그 콜렉션 CLI 플러그인을 설치하십시오.

    1. [{{site.data.keyword.Bluemix_notm}} CLI 페이지](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins)에서 {{site.data.keyword.loganalysisshort}} 서비스 CLI 플러그인(IBM-Logging)의 최신 릴리스를 다운로드하십시오. 
	
		플랫폼 값 **linux64**를 선택하십시오. 
		**파일 저장**을 클릭하십시오. 
    
    2. 플러그인의 압축을 푸십시오.
    
        예를 들어, Ubuntu에서 `logging-cli-linux64.gz` 플러그인을 압축 해제하려면 다음 명령을 실행하십시오.
        
        ```
        gunzip logging-cli-linux64.gz
        ```
        {: codeblock}

    3. 파일을 실행 가능하게 하십시오.
    
        예를 들어, 파일을 `logging-cli-linux64` 실행 가능하게 하려면 다음 명령을 실행하십시오.
        
        ```
        chmod a+x logging-cli-linux64
        ```
        {: codeblock}

    4. 로깅 CF 플러그인을 설치하십시오.
    
        예를 들어, 파일을 `logging-cli-linux64` 실행 가능하게 하려면 다음 명령을 실행하십시오.
        
        ```
        ibmcloud cf install-plugin -f logging-cli-linux64
        ```
        {: codeblock}

2. 환경 변수 **LANG**을 설정하십시오.

    시스템 로케일이 CF에서 지원되지 않은 경우, *LANG*를 기본값 *en_US.UTF-8*로 설정하십시오. CF 지원 로케일에 대한 자세한 정보는 [cf CLI 시작하기 ![외부 링크 아이콘](../../../../icons/launch-glyph.svg "외부 링크 아이콘")](https://docs.cloudfoundry.org/cf-cli/getting-started.html){: new_window}을 참조하십시오.
	
	Ubuntu 시스템의 경우를 예로 들면, *~/.bashrc* 파일을 편집하고 다음 행을 입력하십시오.
    
    ```
    # add entry for logging CLI
    export LANG = en_US.UTF-8
    ```
    {: codeblock}
    
    새 터미널 창을 열고 다음 명령을 실행하여 LANG 변수가 설정되었는지 확인하십시오.
    
    ```
    $echo LANG
    en_US.UTF-8
    ```
    {: screen}   
    
3. 로깅 CLI 플러그인의 설치를 확인하십시오.
  
    예를 들면, 플러그인의 버전을 확인하십시오. 다음 명령을 실행하십시오.
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    출력은 다음과 같습니다.
   
    ```
    cf logging version 1.0.2
    ```
    {: screen}


## Windows에서 Log Analysis CLI 설치
{: #install_cli_windows1}

Windows에서 로그 콜렉션 CF 플러그인을 설치하려면 다음 단계를 완료하십시오.

1. [{{site.data.keyword.Bluemix_notm}} CLI 페이지](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins)에서 {{site.data.keyword.loganalysisshort}} 서비스 CLI 플러그인(IBM-Logging)의 최신 릴리스를 다운로드하십시오. 
	
	1. 플랫폼 값 **win64**를 선택하십시오. 
	2. **파일 저장**을 클릭하십시오.  
    
2. Windows에서 로그 콜렉션 플러그인을 설치하려면 **cf install-plugin** 명령을 실행하십시오. 

    ```
	ibmcloud cf install-plugin PluginName
	```
	{: codeblock}
	
	여기서 *PluginName*은 다운로드한 파일의 이름입니다.
	
    예를 들어, 플러그인 *logging-cli-win64_v1.0.1.exe*를 설치하려면 터미널 창에서 다음 명령을 실행하십시오.
	
	```
	ibmcloud cf install-plugin logging-cli-win64_v1.0.1.exe
	```
	{: codeblock}
	
    플러그인이 설치되면 다음 메시지가 표시됩니다: `Plugin IBM-Logging 1.0.1 successfully installed.`

3. 로깅 CLI 플러그인의 설치를 확인하십시오.
  
    예를 들면, 플러그인의 버전을 확인하십시오. 다음 명령을 실행하십시오.
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    출력은 다음과 같습니다.
   
    ```
    ibmcloud cf logging version 1.0.1
    ```
    {: screen}
	

## Mac OS X에서 Log Analysis CLI 설치
{: #install_cli_mac1}

Mac OS X에서 로그 콜렉션 CF 플러그인을 설치하려면 다음 단계를 완료하십시오.

1. [{{site.data.keyword.Bluemix_notm}} CLI 페이지](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins)에서 {{site.data.keyword.loganalysisshort}} 서비스 CLI 플러그인(IBM-Logging)의 최신 릴리스를 다운로드하십시오. 
	
	1. 플랫폼 값 **osx**를 선택하십시오. 
	2. **파일 저장**을 클릭하십시오.  
    
2. Mac OS X에서 로그 콜렉션 플러그인을 설치하려면 **cf install-plugin** 명령을 실행하십시오. 

    ```
	ibmcloud cf install-plugin PluginName
	```
	{: codeblock}
	
	여기서 *PluginName*은 다운로드한 파일의 이름입니다.
	
    예를 들어, 플러그인 *logging-cli-darwin_v1.0.1*을 설치하려면 터미널에서 다음 명령을 실행하십시오.
	
	```
	ibmcloud cf install-plugin logging-cli-darwin_v1.0.1
	```
	{: codeblock}
	
    플러그인이 설치되면 다음 메시지가 표시됩니다: `Plugin IBM-Logging 1.0.1 successfully installed.`

3. 로깅 CLI 플러그인의 설치를 확인하십시오.
  
    예를 들면, 플러그인의 버전을 확인하십시오. 다음 명령을 실행하십시오.
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    출력은 다음과 같습니다.
   
    ```
    ibmcloud cf logging version 1.0.1
    ```
    {: screen}
	
	
## Log Analysis CLI 설치
{: #uninstall_cli1}

로깅 CLI를 설치 제거하려면 플러그인을 삭제하십시오.
{:shortdesc}

{{site.data.keyword.loganalysisshort}} 서비스 CLI를 설치 제거하려면 다음 단계를 완료하십시오.

1. 설치된 로깅 CLI 플러그인의 버전을 확인하십시오.
  
    예를 들면, 플러그인의 버전을 확인하십시오. 다음 명령을 실행하십시오.
    
    ```
    ibmcloud cf plugins
    ```
    {: codeblock}
    
    출력은 다음과 같습니다.
   
    ```
Listing Installed Plugins...
    OK

    Plugin Name   Version   Command Name   Command Help
    IBM-Logging   1.0.1     logging        IBM Logging plug-in
    ```
    {: screen}
    
2. 플러그인이 설치되어 있는 경우에는 `cf uninstall-plugin`을 실행하여 로깅 CLI 플러그인을 설치 제거하십시오.

    다음 명령을 실행하십시오.
        
    ```
    ibmcloud cf uninstall-plugin IBM-Logging
    ```
    {: codeblock}
  

## 일반 도움말 가져오기
{: #general_cli_help1}

CLI 및 지원되는 명령에 대한 일반적인 정보를 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
    
2. 지원되는 명령 및 CLI에 대한 정보를 나열합니다. 다음 명령을 실행하십시오.

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}
    
    

## 명령에 대한 도움말 가져오기
{: #command_cli_help1}

명령을 사용하는 방법에 대한 도움말을 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
    
2. 지원되는 명령의 목록을 가져오고 필요로 하는 명령을 식별합니다. 다음 명령을 실행하십시오.

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}

3. 명령에 대한 도움말을 가져옵니다. 다음 명령을 실행하십시오.

    ```
    ibmcloud cf logging help *Command*
    ```
    {: codeblock}
    
    여기서 *Command*는 CLI 명령의 이름입니다(예: *상태*).



## 하위 명령에 대한 도움말 가져오기
{: #subcommand_cli_help1}

명령에는 하위 명령이 있을 수 있습니다. 하위 명령에 대한 도움말을 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
    
2. 지원되는 명령의 목록을 가져오고 필요로 하는 명령을 식별하십시오. 다음 명령을 실행하십시오.

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}

3. 명령에 대한 도움말을 가져오고 지원되는 하위 명령을 식별합니다. 다음 명령을 실행하십시오.

    ```
    ibmcloud cf logging help *Command*
    ```
    {: codeblock}
    
    여기서 *Command*는 CLI 명령의 이름입니다(예: *세션*).

4. 명령에 대한 도움말을 가져오고 지원되는 하위 명령을 식별합니다. 다음 명령을 실행하십시오.

    ```
    ibmcloud cf logging *Command* help *Subcommand*
    ```
    {: codeblock}
    
    여기서 
    
    * *Command*는 CLI 명령의 이름입니다(예: *상태*).
    * *Subcommand*는 지원되는 하위 명령의 이름입니다. 예를 들면, *session* 명령의 경우 올바른 하위 명령은 *list*입니다.




