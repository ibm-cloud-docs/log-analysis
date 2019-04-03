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


# 클러스터 로그의 자동 수집 사용
{: #containers_kube_other_logs}

{{site.data.keyword.loganalysisshort}} 서비스에서 클러스터를 보고 분석하려면 해당 로그를 {{site.data.keyword.loganalysisshort}} 서비스로 전달하도록 클러스터를 구성해야 합니다. 
{:shortdesc}

## 1단계: 사용자 ID의 권한 검사
{: step1}

사용자 ID에는 로깅 구성을 클러스터에 추가할 수 있도록 다음 권한이 있어야 합니다.

* **뷰어** 권한이 있는 {{site.data.keyword.containershort}}에 대한 IAM 정책
* **관리자** 또는 **운영자** 권한이 있는 클러스터 인스턴스에 대한 IAM 정책

사용자 ID에 이 IAM 정책이 있는지 확인하려면 다음 단계를 완료하십시오.

**참고:** 정책 지정 권한을 가진 계정 소유자 또는 사용자만 이 단계를 수행할 수 있습니다.

1. {{site.data.keyword.Bluemix_notm}} 콘솔에 로그인하십시오. 웹 브라우저를 열고 {{site.data.keyword.Bluemix_notm}} 대시보드를 실행하십시오. [http://bluemix.net ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](http://bluemix.net){:new_window}
	
	사용자 ID 및 비밀번호를 사용하여 로그인하면 {{site.data.keyword.Bluemix_notm}} UI가 열립니다.

2. 메뉴 표시줄에서 **관리 > 계정 > 사용자**를 클릭하십시오.  *사용자* 창에 현재 선택한 계정의 이메일 주소와 함께 사용자 목록이 표시됩니다.
	
3. 사용자 ID를 선택하고 해당 사용자 ID에 두 정책이 있는지 확인하십시오.




## 2단계: 클러스터 컨텍스트 설정
{: #step2}

다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)을 참조하십시오.
    
2. {{site.data.keyword.loganalysisshort}} 서비스 플러그인을 초기화하십시오.

	```
	ibmcloud ks init
	```
	{: codeblock}

3. 터미널 컨텍스트를 클러스터로 설정하십시오.
    
	```
	ibmcloud ks cluster-config ClusterName
	```
	{: codeblock}

    이 명령을 실행하면 출력에서 경로를 구성 파일로 설정하기 위해 터미널에서 실행해야 하는 명령을 제공합니다. 예를 들어, *MyCluster*로 이름 지정된 클러스터의 경우 다음과 같습니다.

	```
	export KUBECONFIG=/Users/ibm/.bluemix/plugins/container-service/clusters/MyCluster/kube-config-hou02-MyCluster.yml
	```
	{: codeblock}

4. 터미널에서 환경 변수를 설정하는 명령을 복사하여 붙여넣은 다음 **Enter**를 누르십시오.



## 3단계: 클러스터 구성
{: step3}

{{site.data.keyword.loganalysisshort}} 서비스로 전달하는 클러스터 로그를 선택할 수 있습니다. 

* 자동 로그 수집을 사용하고 stdout 및 stderr을 전달하려면 [자동 로그 수집 사용 및 컨테이너 로그 전달](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#containers)을 참조하십시오.
* 자동 로그 수집을 사용하고 애플리케이션 로그를 전달하려면 [자동 로그 수집 사용 및 애플리케이션 로그 전달](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#apps)을 참조하십시오.
* 자동 로그 수집을 사용하고 작업자 로그를 전달하려면 [자동 로그 수집 사용 및 작업자 로그 전달](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#workers)을 참조하십시오.
* 자동 로그 수집을 사용하고 Kubernetes 시스템 컴포넌트 로그를 전달하려면 [자동 로그 수집 사용 및 Kubernetes 시스템 컴포넌트 로그 전달](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#system)을 참조하십시오.
* 자동 로그 수집을 사용하고 Kubernetes Ingress 제어기 로그를 전달하려면 [자동 로그 수집 사용 및 Kubernetes 유입 제어기 로그 전달](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#controller)을 참조하십시오.



## 4단계: {{site.data.keyword.containershort_notm}} 키 소유자에 대한 권한 설정
{: #step4}


{{site.data.keyword.containershort}} 키 소유자는 다음 AIM 정책이 필요합니다.

* **관리자** 역할이 있는 {{site.data.keyword.containershort}}에 대한 IAM 정책
* **관리자** 역할이 있는 {{site.data.keyword.loganalysisshort}} 서비스에 대한 IAM 정책

다음 단계를 완료하십시오. 

1. {{site.data.keyword.Bluemix_notm}} 콘솔에 로그인하십시오. 웹 브라우저를 열고 {{site.data.keyword.Bluemix_notm}} 대시보드를 실행하십시오. [http://bluemix.net ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](http://bluemix.net){:new_window}
	
	사용자 ID 및 비밀번호를 사용하여 로그인하면 {{site.data.keyword.Bluemix_notm}} UI가 열립니다.

2. 메뉴 표시줄에서 **관리 > 계정 > 사용자**를 클릭하십시오.  *사용자* 창에 현재 선택한 계정의 이메일 주소와 함께 사용자 목록이 표시됩니다.
	
3. {{site.data.keyword.containershort_notm}} 키 소유자의 사용자 ID를 선택하고 해당 사용자 ID에 두 정책이 있는지 확인하십시오.


로그를 영역 도메인으로 전달하는 경우 조직 및 영역의 {{site.data.keyword.containershort}} 키 소유자에게 CF(Cloud Foundry) 권한을 부여해야 합니다. 키 소유자에는 조직에 대한 *orgManager* 역할과 영역에 대한 *SpaceManager* 또는 *개발자*가 필요합니다.

다음 단계를 완료하십시오.

1. {{site.data.keyword.containershort}} 키 소유자인 계정의 사용자를 식별하십시오. 터미널에서 다음 명령을 실행하십시오.

    ```
    ibmcloud ks api-key-info ClusterName
    ```
    {: codeblock}
    
    여기서, *ClusterName*은 클러스터의 이름입니다.
    
2. {{site.data.keyword.containershort}} 키 소유자로 식별된 사용자에게 조직에 대한 *orgManager* 역할과 영역에 대한 *SpaceManager* 및 *개발자* 역할이 있는지 확인하십시오.

    {{site.data.keyword.Bluemix_notm}} 콘솔에 로그인하십시오. 웹 브라우저를 열고 {{site.data.keyword.Bluemix_notm}} 대시보드([http://bluemix.net ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](http://bluemix.net){:new_window})를 실행하십시오. 사용자 ID 및 비밀번호를 사용하여 로그인하면 {{site.data.keyword.Bluemix_notm}} UI가 열립니다.

    메뉴 표시줄에서 **관리 > 계정 > 사용자**를 클릭하십시오.  *사용자* 창에 현재 선택한 계정의 이메일 주소와 함께 사용자 목록이 표시됩니다.
	
    사용자의 ID를 선택하고 사용자에게 조직에 대한 *orgManager* 역할과 영역에 대한 *SpaceManager* 또는 *개발자* 역할이 있는지 확인하십시오.
 
3. 사용자에게 올바른 권한이 없는 경우 다음 단계를 완료하십시오.

    1. 사용자에게 조직에 대한 *orgManager* 역할과 영역에 대한 *SpaceManager* 및 *개발자* 권한을 부여하십시오. 자세한 정보는 [IBM Cloud UI를 사용하여 사용자에게 영역 로그를 볼 수 있는 권한 부여](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_space)를 참조하십시오.
    
    2. 로깅 구성을 새로 고치십시오. 다음 명령을 실행하십시오.
    
        ```
        ibmcloud ks logging-config-refresh ClusterName
        ```
        {: codeblock}
        
        여기서, *ClusterName*은 클러스터의 이름입니다.
  




## 자동 로그 수집 사용 및 컨테이너 로그 전달 
{: #containers}

다음 명령을 실행하여 *stdout* 및 *stderr* 로그 파일을 {{site.data.keyword.loganalysisshort}} 서비스로 보내십시오.

```
ibmcloud ks logging-config-create ClusterName --logsource container --namespace '*' --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

여기서 

* *ClusterName*은 클러스터의 이름입니다.
* *EndPoint*는 {{site.data.keyword.loganalysisshort}} 서비스가 프로비저닝된 영역의 로깅 서비스에 대한 URL입니다. 엔드포인트 목록은 [엔드포인트](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls)를 참조하십시오.
* *OrgName*은 영역이 사용 가능한 조직의 이름입니다.
* *SpaceName*은 {{site.data.keyword.loganalysisshort}} 서비스가 프로비저닝된 영역의 이름입니다.


예를 들어, stdout 및 stderr 로그를 독일 지역의 계정 도메인에 전달하는 로깅 구성을 작성하려면 다음 명령을 실행하십시오.

```
ibmcloud ks logging-config-create MyCluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}

stdout 및 stderr 로그를 독일 지역의 영역 도메인에 전달하는 로깅 구성을 작성하려면 다음 명령을 실행하십시오.

```
ibmcloud ks logging-config-create MyCluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org MyOrg --space MySpace
```
{: screen}



## 자동 로그 수집 사용 및 애플리케이션 로그 전달 
{: #apps}

다음 명령을 실행하여 */var/log/apps/**/.log* 및 */var/log/apps/*/.err* 로그 파일을 {{site.data.keyword.loganalysisshort}} 서비스로 보내십시오.

```
ibmcloud ks logging-config-create ClusterName --logsource application --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName --app-containers --app-paths
```
{: codeblock}

여기서 

* *ClusterName*은 클러스터의 이름입니다.
* *EndPoint*는 {{site.data.keyword.loganalysisshort}} 서비스가 프로비저닝된 영역의 로깅 서비스에 대한 URL입니다. 엔드포인트 목록은 [엔드포인트](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls)를 참조하십시오.
* *OrgName*은 영역이 사용 가능한 조직의 이름입니다.
* *SpaceName*은 {{site.data.keyword.loganalysisshort}} 서비스가 프로비저닝된 영역의 이름입니다.
* *app-containers*는 보려는 컨테이너 목록을 정의하도록 설정할 수 있는 선택적 매개변수입니다. 컨테이너는 로그가 {{site.data.keyword.loganalysisshort}}로 전달될 유일한 항목입니다. 쉼표로 구분하여 하나 이상의 컨테이너를 설정할 수 있습니다.
* *app-paths*는 보려는 컨테이너 내부의 경로를 정의합니다. 쉼표로 구분하여 하나 이상의 경로를 설정할 수 있습니다. 와일드카드(예: '/var/log/*.log')는 사용할 수 있습니다. 

예를 들어, 애플리케이션 로그를 독일 지역의 영역 도메인에 전달하는 로깅 구성을 작성하려면 다음 명령을 실행하십시오.

```
ibmcloud ks logging-config-create MyCluster --logsource application --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org MyOrg --space MySpace --app-paths /var/log/*.log
```
{: screen}

예를 들어, 애플리케이션 로그를 독일 지역의 계정 도메인에 전달하는 로깅 구성을 작성하려면 다음 명령을 실행하십시오.

```
ibmcloud ks logging-config-create MyCluster --logsource application --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --app-paths /var/log/*.log
```
{: screen}



## 자동 로그 수집 사용 및 작업자 로그 전달 
{: #workers}


다음 명령을 실행하여 */var/log/syslog* 및 */var/log/auth.log* 로그 파일을 {{site.data.keyword.loganalysisshort}} 서비스로 보내십시오.

```
ibmcloud ks logging-config-create ClusterName --logsource worker --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

여기서 

* *ClusterName*은 클러스터의 이름입니다.
* *EndPoint*는 {{site.data.keyword.loganalysisshort}} 서비스가 프로비저닝된 영역의 로깅 서비스에 대한 URL입니다. 엔드포인트 목록은 [엔드포인트](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls)를 참조하십시오.
* *OrgName*은 영역이 사용 가능한 조직의 이름입니다.
* *SpaceName*은 {{site.data.keyword.loganalysisshort}} 서비스가 프로비저닝된 영역의 이름입니다.



예를 들어, 작업자 로그를 독일 지역의 영역 도메인에 전달하는 로깅 구성을 작성하려면 다음 명령을 실행하십시오.

```
ibmcloud ks logging-config-create MyCluster --logsource worker  --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

예를 들어, 작업자 로그를 독일 지역의 계정 도메인에 전달하는 로깅 구성을 작성하려면 다음 명령을 실행하십시오.

```
ibmcloud ks logging-config-create MyCluster --logsource worker  --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}



## 자동 로그 수집 사용 및 Kubernetes 시스템 컴포넌트 로그 전달
{: #system}

다음 명령을 사용하여 */var/log/kubelet.log* 및 */var/log/kube-proxy.log* 로그 파일을 {{site.data.keyword.loganalysisshort}} 서비스로 보내십시오.

```
ibmcloud ks logging-config-create ClusterName --logsource kubernetes --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

여기서 

* *ClusterName*은 클러스터의 이름입니다.
* *EndPoint*는 {{site.data.keyword.loganalysisshort}} 서비스가 프로비저닝된 영역의 로깅 서비스에 대한 URL입니다. 엔드포인트 목록은 [엔드포인트](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls)를 참조하십시오.
* *OrgName*은 영역이 사용 가능한 조직의 이름입니다.
* *SpaceName*은 {{site.data.keyword.loganalysisshort}} 서비스가 프로비저닝된 영역의 이름입니다.



예를 들어, Kubernetes 시스템 컴포넌트 로그를 독일 지역의 영역 도메인에 전달하는 로깅 구성을 작성하려면 다음 명령을 실행하십시오.

```
ibmcloud ks logging-config-create MyCluster --logsource kubernetes --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

예를 들어, Kubernetes 시스템 컴포넌트 로그를 독일 지역의 계정 도메인에 전달하는 로깅 구성을 작성하려면 다음 명령을 실행하십시오.

```
ibmcloud ks logging-config-create MyCluster --logsource kubernetes --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}



## 자동 로그 수집 사용 및 Kubernetes Ingress 제어기 로그 전달
{: #controller}

다음 명령을 사용하여 */var/log/alb/ids/.log*, */var/log/alb/ids/.err*, */var/log/alb/customerlogs/.log* 및 /var/log/alb/customerlogs/.err* 로그 파일을 {{site.data.keyword.loganalysisshort}} 서비스로 보내십시오.

```
ibmcloud ks logging-config-create ClusterName --logsource ingress --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName
```
{: codeblock}

여기서 

* *ClusterName*은 클러스터의 이름입니다.
* *EndPoint*는 {{site.data.keyword.loganalysisshort}} 서비스가 프로비저닝된 영역의 로깅 서비스에 대한 URL입니다. 엔드포인트 목록은 [엔드포인트](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls)를 참조하십시오.
* *OrgName*은 영역이 사용 가능한 조직의 이름입니다.
* *SpaceName*은 {{site.data.keyword.loganalysisshort}} 서비스가 프로비저닝된 영역의 이름입니다.



예를 들어, Ingress 제어기 로그를 독일 지역의 영역 도메인에 전달하는 로깅 구성을 작성하려면 다음 명령을 실행하십시오.

```
ibmcloud ks logging-config-create MyLoggingDemoCluster --logsource ingress --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

예를 들어, Ingress 제어기 로그를 독일 지역의 계정 도메인에 전달하는 로깅 구성을 작성하려면 다음 명령을 실행하십시오.

```
ibmcloud ks logging-config-create MyLoggingDemoCluster --logsource ingress --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091  
```
{: screen}



