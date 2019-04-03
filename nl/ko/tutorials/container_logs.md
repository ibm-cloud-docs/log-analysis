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


# Kubernetes 클러스터에 배치된 앱에 대한 Kibana에서 로그 분석
{: #container_logs}
이 튜토리얼을 사용하여 {{site.data.keyword.Bluemix_notm}}의 {{site.data.keyword.loganalysisshort}} 서비스로 로그를 전달하도록 클러스터를 구성하는 방법을 학습할 수 있습니다.
{:shortdesc}


## 목표
{: #objectives}

1. 클러스터에서 로깅 구성을 구성합니다. 
2. {{site.data.keyword.Bluemix_notm}}에서 Kubernetes 클러스터에 배치된 앱에 대한 컨테이너 로그를 검색하고 분석합니다.

이 튜토리얼은 {{site.data.keyword.Bluemix_notm}}에서 클러스터 프로비저닝, {{site.data.keyword.Bluemix_notm}}에서 {{site.data.keyword.loganalysisshort}} 서비스로 로그를 보내도록 클러스터 구성, 클러스터에서 앱 배치, Kibana를 사용하여 해당 클러스터에 대한 컨테이너 로그 보기 및 필터링과 같은 엔드 투 엔드 시나리오 작업을 수행하는 데 필요한 단계를 안내합니다.


**참고:** 이 튜토리얼을 완료하려면 여러 단계에서 링크된 튜토리얼 및 전제조건을 완료해야 합니다.


## 전제조건
{: #prereq}

1. Kubernetes 표준 클러스터를 작성하고, 클러스터에 앱을 배치하고, Kibana에서 고급 분석을 위해 {{site.data.keyword.Bluemix_notm}}에서 로그를 조회할 수 있는 권한이 있는 {{site.data.keyword.Bluemix_notm}} 계정의 소유자이거나 구성원입니다.

    {{site.data.keyword.Bluemix_notm}} 사용자 ID에 다음 정책이 지정되어 있어야 합니다.
    
    * *편집자*, *운영자* 또는 *관리자* 권한이 있는 {{site.data.keyword.containershort}}에 대한 IAM 정책
    * {{site.data.keyword.loganalysisshort}} 서비스가 *개발자* 권한으로 프로비저닝된 영역에 대한 CF 역할
    
    자세한 정보는 [IBM Cloud UI를 통해 사용자에게 IAM 정책 지정](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_account) 및 [IBM Cloud UI를 사용하여 사용자에게 영역 로그를 볼 수 있는 권한 부여](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_space)를 참조하십시오.

2. Kubernetes 클러스터를 관리할 수 있는 터미널 세션이 있고 명령행에서 앱을 배치합니다. 이 튜토리얼에 소개되는 예는 Ubuntu Linux 시스템에 대해 제공됩니다.

3. Ubuntu 시스템에서 {{site.data.keyword.containershort}} 및 {{site.data.keyword.loganalysisshort}}에 대해 작업하기 위한 CLI를 설치하십시오.

    * {{site.data.keyword.Bluemix_notm}} CLI를 설치하십시오. {{site.data.keyword.containershort}}에서 Kubernetes 클러스터를 작성 및 관리하고 컨테이너식 앱을 클러스터에 배치하기 위한 {{site.data.keyword.containershort}} CLI를 설치하십시오. 자세한 정보는 [{{site.data.keyword.Bluemix_notm}} CLI 설치](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)를 참조하십시오.
    
    * {{site.data.keyword.loganalysisshort}} CLI를 설치하십시오. 자세한 정보는 [Log Analysis CLI(IBM Cloud 플러그인) 구성](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli#config_log_collection_cli)을 참조하십시오.
    
4. 미국 남부 지역의 계정에서 **dev**라는 영역에 액세스할 수 있도록 하십시오. 

    클러스터에서 사용 가능한 로그가 이 영역과 연관된 영역 도메인에 전달되도록 구성됩니다. 
    
    이 영역에서 {{site.data.keyword.loganalysisshort}} 서비스를 프로비저닝합니다.
    
    {{site.data.keyword.loganalysisshort}} 서비스를 프로비저닝할 수 있도록 이 영역의 **개발자** 권한이 있어야 합니다.
    
    튜토리얼에서 사용되는 조직의 이름은 **MyOrg**입니다.

    
 

## 1단계: Kubernetes 클러스터 프로비저닝
{: #step25}

다음 단계를 완료하십시오.

1. 표준 Kubernetes 클러스터를 작성하십시오.

   자세한 정보는 [클러스터 작성](/docs/containers?topic=containers-cs_cluster_tutorial#cs_cluster_tutorial)을 참조하십시오.

2. 터미널에서 클러스터 컨텍스트를 설정하십시오. 컨텍스트가 설정된 후에 Kubernetes 클러스터를 관리하고, Kubernetes 클러스터에서 애플리케이션을 배치할 수 있습니다.

    작성한 클러스터와 연관된 {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)을 참조하십시오.

	{{site.data.keyword.containershort}} 서비스 플러그인을 초기화하십시오.

	```
	ibmcloud cs init
	```
	{: codeblock}

    터미널 컨텍스트를 클러스터로 설정하십시오.
    
	```
	ibmcloud cs cluster-config MyCluster
	```
	{: codeblock}

    이 명령을 실행하면 출력에서 경로를 구성 파일로 설정하기 위해 터미널에서 실행해야 하는 명령을 제공합니다. 예:

	```
	export KUBECONFIG=/Users/ibm/.bluemix/plugins/container-service/clusters/MyCluster/kube-config-hou02-MyCluster.yml
	```
	{: codeblock}

    터미널에서 환경 변수를 설정하는 명령을 복사하여 붙여넣은 다음 **Enter**를 누르십시오.



## 2단계: 자동으로 로그를 {{site.data.keyword.loganalysisshort}} 서비스로 전달하도록 클러스터 구성
{: #step26}

앱이 배치될 때 {{site.data.keyword.containershort}}가 자동으로 로그를 수집합니다. 그러나 자동으로 로그가 {{site.data.keyword.loganalysisshort}} 서비스로 전달되지 않습니다. 클러스터에서 다음을 정의하는 하나 이상의 로깅 구성을 작성해야 합니다.

* 로그가 전달될 위치. 로그를 계정 도메인 또는 영역 도메인으로 전달할 수 있습니다.
* 분석을 위해 {{site.data.keyword.loganalysisshort}} 서비스에 전달되는 로그


로깅 구성을 정의하기 전에 클러스터의 현재 로깅 구성 정의를 확인하십시오. 다음 명령을 실행하십시오.

```
$ ibmcloud cs logging-config-get ClusterName
```
{: codeblock}

여기서 *ClusterName*은 클러스터의 이름입니다.

예를 들어, *mycluster* 클러스터에 대해 정의된 로깅 구성은 다음과 같습니다. 

```
$ ibmcloud cs logging-config-get mycluster
Retrieving cluster mycluster logging configurations...
OK
Id                                     Source       Namespace   Host                                Port   Org            Space   Protocol   Paths   
13ded2c0-83f5-4cc5-8de7-1e34e1287f34   worker       -           ingest.logging.ng.bluemix.net       9091   Demo_Org       dev     ibm        /var/log/syslog,/var/log/auth.log   
ae249c04-a3a9-4c29-a890-22d8da7bd1b2   container    *           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        -   
31739fc1-42e2-4b66-ac57-6a32091c257a   ingress      -           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        /var/log/alb/ids/*.log,/var/log/alb/ids/*.err,/var/log/alb/customerlogs/*.log,/var/log/alb/customerlogs/*.err   
6b8cfe89-4959-448d-898b-c3b0584eca71   kubernetes   -           ingest-eu-fra.logging.bluemix.net   9091   Demo_Org.      dev     ibm        /var/log/kubelet.log,/var/log/kube-proxy.log   

```
{: screen}

로깅 구성을 정의할 수 있는 로그 소스의 목록을 보려면 [로그 소스](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kubernetes#log_sources)를 참조하십시오.


### stderr 및 stdout 로그를 {{site.data.keyword.loganalysisshort}} 서비스에 전달하도록 클러스터 구성
{: #containerstd}


stdout 및 stderr 로그를 영역 도메인으로 보내려면 다음 단계를 완료하십시오. 여기서 조직 이름은 *MyOrg*이고 영역 이름은 미국 남부 지역의 *dev*입니다.

1. 사용자 ID에 클러스터 구성 추가 권한이 있는지 확인하십시오. 클러스터 관리 권한이 있는 {{site.data.keyword.containershort}}에 대한 IAM 정책을 가진 사용자만 이 기능을 사용할 수 있습니다. 다음 역할이 필요합니다. *관리자*, *운영자*

    사용자 ID에 클러스터 관리를 위해 지정된 IAM 정책이 있는지 확인하려면 다음 단계를 완료하십시오.
    
    1. {{site.data.keyword.Bluemix_notm}} 콘솔에 로그인하십시오. 웹 브라우저를 열고 {{site.data.keyword.Bluemix_notm}} 대시보드([http://bluemix.net ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](http://bluemix.net){:new_window})를 실행하십시오. 사용자 ID 및 비밀번호를 사용하여 로그인하면 {{site.data.keyword.Bluemix_notm}} UI가 열립니다.

    2. 메뉴 표시줄에서 **관리 > 계정 > 사용자**를 클릭하십시오.  *사용자* 창에 현재 선택한 계정의 이메일 주소와 함께 사용자 목록이 표시됩니다.
	
    3. 사용자 ID를 선택하고 해당 사용자 ID에 {{site.data.keyword.containershort}}에 대한 정책이 있는지 확인하십시오.

    권한이 필요한 경우 계정 소유자 또는 계정 관리자에게 문의하십시오. 정책 지정 권한이 있는 계정 소유자 또는 사용자만 이 단계를 수행할 수 있습니다.

2. 클러스터 로깅 구성을 작성하십시오. 다음 명령을 실행하여 *stdout* 및 *stderr* 로그 파일을 {{site.data.keyword.loganalysisshort}} 서비스로 보내십시오.

    ```
    ibmcloud cs logging-config-create ClusterName --logsource container --namespace '*' --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    여기서 

    * *ClusterName*은 클러스터의 이름입니다.
    * *EndPoint*는 {{site.data.keyword.loganalysisshort}} 서비스가 프로비저닝된 영역의 로깅 서비스에 대한 URL입니다. 엔드포인트 목록은 [엔드포인트](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls)를 참조하십시오.
    * *OrgName*은 영역이 사용 가능한 조직의 이름입니다.
    * *SpaceName*은 {{site.data.keyword.loganalysisshort}} 서비스가 프로비저닝된 영역의 이름입니다.


예를 들어, stdout 및 stderr 로그를 미국 남부 지역의 영역 개발자에게 전달하는 로깅 구성을 작성하려면 다음 명령을 실행하십시오.

```
ibmcloud cs logging-config-create mycluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}




### 작업자 로그를 {{site.data.keyword.loganalysisshort}} 서비스에 전달하도록 클러스터 구성
{: #workerlogs }

작업자 로그를 영역 도메인으로 보내려면 다음 단계를 완료하십시오. 여기서 조직 이름은 *MyOrg*이고 영역 이름은 미국 남부 지역의 *dev*입니다.

1. 사용자 ID에 클러스터 구성 추가 권한이 있는지 확인하십시오. 클러스터 관리 권한이 있는 {{site.data.keyword.containershort}}에 대한 IAM 정책을 가진 사용자만 이 기능을 사용할 수 있습니다. 다음 역할이 필요합니다. *관리자*, *운영자*

    사용자 ID에 클러스터 관리를 위해 지정된 IAM 정책이 있는지 확인하려면 다음 단계를 완료하십시오.
    
    1. {{site.data.keyword.Bluemix_notm}} 콘솔에 로그인하십시오. 웹 브라우저를 열고 {{site.data.keyword.Bluemix_notm}} 대시보드([http://bluemix.net ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](http://bluemix.net){:new_window})를 실행하십시오. 사용자 ID 및 비밀번호를 사용하여 로그인하면 {{site.data.keyword.Bluemix_notm}} UI가 열립니다.

    2. 메뉴 표시줄에서 **관리 > 계정 > 사용자**를 클릭하십시오.  *사용자* 창에 현재 선택한 계정의 이메일 주소와 함께 사용자 목록이 표시됩니다.
	
    3. 사용자 ID를 선택하고 해당 사용자 ID에 {{site.data.keyword.containershort}}에 대한 정책이 있는지 확인하십시오.

    권한이 필요한 경우 계정 소유자 또는 계정 관리자에게 문의하십시오. 정책 지정 권한이 있는 계정 소유자 또는 사용자만 이 단계를 수행할 수 있습니다.

2. 클러스터 로깅 구성을 작성하십시오. 다음 명령을 실행하여 */var/log/syslog* 및 */var/log/auth.log* 로그 파일을 {{site.data.keyword.loganalysisshort}} 서비스로 보내십시오.

    ```
    ibmcloud cs logging-config-create ClusterName --logsource worker --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    여기서 

    * *ClusterName*은 클러스터의 이름입니다.
    * *EndPoint*는 {{site.data.keyword.loganalysisshort}} 서비스가 프로비저닝된 영역의 로깅 서비스에 대한 URL입니다. 엔드포인트 목록은 [엔드포인트](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls)를 참조하십시오.
    * *OrgName*은 영역이 사용 가능한 조직의 이름입니다.
    * *SpaceName*은 {{site.data.keyword.loganalysisshort}} 서비스가 프로비저닝된 영역의 이름입니다.

    
예를 들어, 작업자 로그를 미국 남부 지역의 영역 도메인에 전달하는 로깅 구성을 작성하려면 다음 명령을 실행하십시오.

```
ibmcloud cs logging-config-create mycluster --logsource worker  --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}



## 3단계: 사용자에게 영역 도메인의 로그를 볼 수 있는 권한 부여
{: #step33}

사용자에게 영역의 로그를 볼 수 있는 권한을 부여하려면 해당 사용자에게 이 사용자가 영역에서 {{site.data.keyword.loganalysisshort}} 서비스에 대해 수행할 수 있는 조치를 설명하는 Cloud Foundry 역할을 지정해야 합니다. 

{{site.data.keyword.loganalysisshort}} 서비스에 대한 작업을 수행할 권한을 사용자에게 부여하려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}} 콘솔에 로그인하십시오.

    웹 브라우저를 열고 {{site.data.keyword.Bluemix_notm}} 대시보드를 실행하십시오. [http://bluemix.net ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](http://bluemix.net){:new_window}
	
	사용자 ID 및 비밀번호를 사용하여 로그인하면 {{site.data.keyword.Bluemix_notm}} UI가 열립니다.

2. 메뉴 표시줄에서 **관리 > 계정 > 사용자**를 클릭하십시오. 

    *사용자* 창에 현재 선택한 계정의 이메일 주소와 함께 사용자 목록이 표시됩니다.
	
3. 사용자가 계정의 구성원인 경우 목록에서 사용자 이름을 선택하거나 *조치* 메뉴에서 **사용자 관리**를 클릭하십시오.

    사용자가 계정의 구성원이 아닌 경우 [사용자 초대](/docs/iam?topic=iam-iamuserinv#iamuserinv)를 참조하십시오.

4. **Cloud Foundry 액세스**를 선택한 후 조직을 선택하십시오.

    해당 조직에서 사용 가능한 영역의 목록이 나열됩니다.

5. 영역을 선택하십시오. 그런 다음 메뉴 조치에서 **영역 역할 편집**을 선택하십시오.

    미국 남부에 대한 영역을 볼 수 없는 경우 진행하기 전에 영역을 작성하십시오.

6. *개발자*를 선택하십시오.

    하나 이상의 역할을 선택할 수 있습니다. 
    
    올바른 역할은 *관리자*, *개발자* 및 *감사자*입니다.
	
7. **역할 저장**을 클릭하십시오.


## 4단계: {{site.data.keyword.containershort_notm}} 키 소유자 권한 부여
{: #step52}

영역으로 전달될 클러스터 로그의 경우 {{site.data.keyword.containershort_notm}} 키 소유자에는 다음 권한이 있어야 합니다.

* *관리자* 권한이 있는 {{site.data.keyword.loganalysisshort}} 서비스에 대한 IAM 정책
* 로그가 전달될 조직 및 영역의 CF(Cloud Foundry) 권한. 컨테이너 키 소유자에는 조직에 대한 *orgManager* 역할과 영역에 대한 *SpaceManager* 및 *개발자*가 필요합니다.

다음 단계를 완료하십시오.

1. {{site.data.keyword.containershort}} 키 소유자인 계정의 사용자를 식별하십시오. 터미널에서 다음 명령을 실행하십시오.

    ```
    ibmcloud cs api-key-info ClusterName
    ```
    {: codeblock}
    
    여기서, *ClusterName*은 클러스터의 이름입니다.

2. {{site.data.keyword.containershort}} 키 소유자로 식별된 사용자에게 조직에 대한 *orgManager* 역할과 영역에 대한 *SpaceManager* 및 *개발자* 역할이 있는지 확인하십시오.

    {{site.data.keyword.Bluemix_notm}} 콘솔에 로그인하십시오. 웹 브라우저를 열고 {{site.data.keyword.Bluemix_notm}} 대시보드([http://bluemix.net ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](http://bluemix.net){:new_window})를 실행하십시오. 사용자 ID 및 비밀번호를 사용하여 로그인하면 {{site.data.keyword.Bluemix_notm}} UI가 열립니다.

    메뉴 표시줄에서 **관리 > 계정 > 사용자**를 클릭하십시오.  *사용자* 창에 현재 선택한 계정의 이메일 주소와 함께 사용자 목록이 표시됩니다.
	
    사용자의 ID를 선택하고 사용자에게 조직에 대한 *orgManager* 역할과 영역에 대한 *SpaceManager* 및 *개발자* 역할이 있는지 확인하십시오.

    사용자에게 올바른 권한이 없는 경우 사용자에게 조직에 대한 *orgManager* 역할과 영역에 대한 *SpaceManager* 및 *개발자* 권한을 부여하십시오. 자세한 정보는 [IBM Cloud UI를 사용하여 사용자에게 영역 로그를 볼 수 있는 권한 부여](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_space)를 참조하십시오.
    
3. {{site.data.keyword.containershort}} 키 소유자로 식별된 사용자에게 *관리자* 권한이 있는 {{site.data.keyword.loganalysisshort}} 서비스에 대한 IAM 정책이 있는지 확인하십시오.

    메뉴 표시줄에서 **관리 > 계정 > 사용자**를 클릭하십시오.  *사용자* 창에 현재 선택한 계정의 이메일 주소와 함께 사용자 목록이 표시됩니다.
	
    사용자의 ID를 선택하고 사용자에게 IAM 정책 세트가 있는지 확인하십시오. 

    사용자에게 IAM 정책이 없는 경우 [IBM Cloud UI를 통해 사용자에게 IAM 정책 지정](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_account)을 참조하십시오.

4. 로깅 구성을 새로 고치십시오. 다음 명령을 실행하십시오.
    
    ```
    ibmcloud cs logging-config-refresh ClusterName
    ```
    {: codeblock}
        
    여기서, *ClusterName*은 클러스터의 이름입니다.
	



## 5단계: Kubernetes 클러스터에서 샘플 앱을 배치하여 stdout에 컨텐츠 생성
{: #step53}

Kubernetes 클러스터에서 샘플 앱을 배치하고 실행하십시오. [학습 1: Kubernetes 클러스터에 단일 인스턴스 앱 배치](/docs/containers?topic=containers-cs_apps_tutorial#cs_apps_tutorial_lesson1) 튜토리얼의 단계를 완료하여 샘플 앱을 배치하십시오.

앱은 Hello World Node.js 앱입니다.

```
var express = require('express')
var app = express()

app.get('/', function(req, res) {
  res.send('Hello world! Your app is up and running in a cluster!\n')
})
app.listen(8080, function() {
  console.log('Sample app is listening on port 8080.')
})
```
{: screen}

이 샘플 앱에서는 앱을 브라우저에서 테스트하면 앱이 `Sample app is listening on port 8080.` 메시지를 stdout에 작성합니다.






## 6단계: Kibana에서 로그 데이터 보기
{: #step6}

다음 단계를 완료하십시오.

1. 브라우저에서 Kibana를 실행하십시오. 

    Kibana 실행 방법에 대한 자세한 정보는 [웹 브라우저에서 Kibana로 이동](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-launch#launch_Kibana_from_browser)을 참조하십시오.

    클러스터에 대한 로그 데이터를 분석하려면 클러스터가 작성된 클라우드 공용 지역에서 Kibana에 액세스해야 합니다. 
    
    예를 들어, 미국 남부 지역에서 Kibana를 실행하려면 다음 URL을 입력하십시오.
	
	```
	https://logging.ng.bluemix.net/ 
	```
	{: codeblock}
	
    Kibana가 열립니다.
    
    **참고:** 클러스터 로그를 전달할 지역에서 Kibana를 실행하는지 확인하십시오. 지역별 URL에 대한 정보는 [로깅 엔드포인트](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analyzing_logs_Kibana#urls_kibana)를 참조하십시오.
    	
2. 영역 도메인에서 사용 가능한 로그 데이터를 보려면 다음 단계를 완료하십시오.

    1. Kibana에서 사용자 ID를 클릭하십시오. 영역을 설정하기 위한 보기가 열립니다.
    
    2. 영역이 사용 가능한 계정을 선택하십시오. 
    
    3. **space** 도메인을 선택하십시오.
    
    4. 영역이 사용 가능한 *MyOrg* 조직을 선택하십시오.
    
    5. *dev* 영역을 선택하십시오.
    
    
3. **검색** 페이지에서 표시된 이벤트를 보십시오. 
        
    *사용 가능한 필드* 섹션에서는 페이지에 표시된 표에 나열된 항목을 필터링하거나 새 조회를 정의하는 데 사용할 수 있는 필드 목록을 볼 수 있습니다.
    
    다음 표는 애플리케이션 로그를 분석할 때 새 검색 조회를 정의하는 데 사용할 수 있는 일부 필드를 나열합니다. 표에는 샘플 앱에서 생성된 이벤트에 해당하는 샘플 값이 포함되어 있습니다.
 
    <table>
              <caption>표 2. 컨테이너 로그를 위한 공통 필드 </caption>
               <tr>
                <th align="center">필드</th>
                <th align="center">설명</th>
                <th align="center">예</th>
              </tr>
              <tr>
                <td>*ibm-containers.region_str*</td>
                <td>이 필드의 값은 로그 항목이 수집된 {{site.data.keyword.Bluemix_notm}} 지역에 해당합니다.</td>
                <td>us-south</td>
              </tr>
			  <tr>
                <td>*ibm-containers.account_id_str*</td>
                <td>계정 ID</td>
                <td></td>
              </tr>
			  <tr>
                <td>*ibm-containers.cluster_id_str *</td>
                <td>클러스터 ID.</td>
                <td></td>
              </tr>
              <tr>
                <td>*ibm-containers.cluster_name_str*</td>
                <td>클러스터 ID</td>
                <td></td>
              </tr>
			  <tr>
                <td>*kubernetes.namespace_name_str*</td>
                <td>네임스페이스 이름</td>
                <td>*default*는 기본값입니다.</td>
              </tr>
              <tr>
                <td>*kubernetes.container_name_str*</td>
                <td>컨테이너 이름.</td>
                <td>hello-world-deployment</td>
              </tr>
              <tr>
                <td>*kubernetes.labels.label_name*</td>
                <td>레이블 필드는 선택 사항입니다. 0 이상의 레이블이 있습니다. 각 레이블은 접두부 `kubernetes.labels.`으로 시작하고 그 뒤에 *label_name*이 옵니다. </td>
                <td>샘플 앱에서는 2개의 레이블을 볼 수 있습니다. <br>* *kubernetes.labels.pod-template-hash_str* = 3355293961 <br>* *kubernetes.labels.run_str* =	hello-world-deployment  </td>
              </tr>
              <tr>
                <td>*stream_str *</td>
                <td>로그 유형.</td>
                <td>*stdout*, *stderr*</td>
              </tr>
        </table>
     
Kubernetes 클러스터와 관련된 다른 검색 필드에 대한 자세한 정보는 [로그 검색](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kubernetes#log_search)을 참조하십시오.


## 7단계: Kibana에서 Kubernetes 클러스터 이름별로 데이터 필터링
{: #step7}
    
*검색* 페이지에 표시되는 표에서 분석할 수 있는 모든 항목을 볼 수 있습니다. 나열된 항목은 *검색* 표시줄에 표시된 검색 조회에 해당합니다. 별표(*)를 사용하여 페이지에 구성된 기간 내의 모든 항목을 표시하십시오.
    
예를 들어, Kubernetes 클러스터 이름별로 데이터를 필터링하려면 *검색* 표시줄 조회를 수정하십시오. 사용자 정의 필드 *kubernetes.cluster_name_str*을 기반으로 필터를 추가하십시오.
    
1. **사용 가능한 필드** 섹션에서 *kubernetes.cluster_name_str* 필드를 선택하십시오. 필드에 사용 가능한 값의 서브세트가 표시됩니다.    
    
2. 로그를 분석할 클러스터에 해당하는 값을 선택하십시오. 
    
    값을 선택한 후에 필터가 *검색 표시줄*에 추가되고 방금 선택한 기준과 일치하는 항목만 표에 표시됩니다.     
   

**참고:** 

클러스터 이름을 볼 수 없는 경우 클러스터 이름에 대한 필터를 추가하십시오. 그런 다음 필터의 편집 기호를 선택하십시오.    
    
다음과 같은 조회가 표시됩니다.
    
```
	{
        "query": {
          "match": {
            "kubernetes.cluster_name_str": {
              "query": "cluster1",
              "type": "phrase"
            }
          }
        }
      }
```
{: screen}

클러스터의 이름(*cluster1*)을 로그 데이터를 보려는 클러스터의 이름(*mycluster*)으로 바꾸십시오.
        
데이터를 볼 수 없는 경우 시간 필터를 변경해보십시오. 자세한 정보는 [시간 필터 설정](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter)을 참조하십시오.

자세한 정보는 [Kibana에서 로그 필터링](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#filter_logs)을 참조하십시오.


## {{site.data.keyword.containershort_notm}} 참조 자료
{: reference}

CLI 명령:

* [ibmcloud cs api-key-info](/docs/containers?topic=containers-cs_cli_reference#cs_api_key_info)
* [ibmcloud cs logging-config-create](/docs/containers?topic=containers-cs_cli_reference#cs_logging_create)
* [ibmcloud cs logging-config-get](/docs/containers?topic=containers-cs_cli_reference#cs_logging_get)
* [ibmcloud cs logging-config-update](/docs/containers?topic=containers-cs_cli_reference#cs_logging_update)
* [ibmcloud cs logging-config-rm](/docs/containers?topic=containers-cs_cli_reference#cs_logging_rm)
* [ibmcloud cs logging-config-refresh](/docs/containers?topic=containers-cs_cli_reference#cs_logging_refresh)

