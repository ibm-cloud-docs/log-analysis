---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, kubernetes, tutorial

subcollection: LogDNA

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


# {{site.data.keyword.la_full_notm}}를 사용하여 Kubernetes 클러스터 로그 관리
{: #kube}

{{site.data.keyword.containerlong}}에서 클러스터 레벨 로깅을 구성하려면 {{site.data.keyword.la_full_notm}} 서비스를 사용하십시오. 
{:shortdesc}

{{site.data.keyword.containerlong_notm}}를 사용하여 클러스터를 프로비저닝할 때부터 클러스터 내부의 상황을 알고 싶을 것입니다. 문제점을 해결하고 문제를 방지하려면 로그에 액세스해야 합니다. 언제든지 작업자 로그, 팟(Pod) 로그, 앱 로그 또는 네트워크 로그와 같은 여러 로그 유형에 액세스할 수 있습니다. 또한 Kubernetes 클러스터에서 로그 데이터의 여러 소스를 모니터할 수 있습니다. 따라서 이러한 소스에서 로그 레코드를 관리하고 액세스하는 기능이 중요합니다. 로그에 대한 성공적인 관리 및 모니터링은 Kubernetes 플랫폼에 대한 로깅 기능을 구성하는 방법에 따라 다릅니다.

Kubernetes 클러스터에 대한 클러스터 레벨 로깅을 구성하려면 다음 정보를 고려하십시오.

* Kubernetes 시스템 컴포넌트의 개별 스토리지에 로그 데이터, 시스템 로그 및 컨테이너형 애플리케이션 로그를 저장해야 합니다.
* 클러스터의 모든 작업자 노드에 로깅 에이전트를 배치해야 합니다. 이 에이전트는 로그를 수집하여 외부 로깅 백엔드로 전달합니다.
* 외부 로깅 백엔드에 대한 분석을 위해 로그 데이터를 중앙화해야 합니다.


{{site.data.keyword.cloud_notm}}에서 Kubernetes 클러스터에 대한 클러스터 레벨 로깅을 구성하려면 다음 단계를 완료해야 합니다.

1. {{site.data.keyword.la_full_notm}} 서비스의 인스턴스를 프로비저닝하십시오. 이 단계에서는 {{site.data.keyword.cloud_notm}}에서 로그 데이터가 호스팅되는 중앙화된 로그 관리 시스템을 구성합니다.
2. {{site.data.keyword.containerlong_notm}}에서 클러스터를 프로비저닝하십시오. Kubernetes v1.9+ 클러스터가 지원됩니다.
3. 클러스터의 모든 작업자(노드)에서 LogDNA 에이전트를 구성하십시오.

![{{site.data.keyword.cloud_notm}}의 LogDNA 컴포넌트 개요](../images/kube.png "{{site.data.keyword.cloud_notm}}의 LogDNA 컴포넌트 개요")

이 튜토리얼에서는 클러스터 레벨 로깅을 구성하는 방법에 대해 알아봅니다.

## 시작하기 전에
{: #kube_prereqs}

미국 남부 지역에서 작업합니다. {{site.data.keyword.la_full_notm}}는 현재 미국 남부 지역에서 사용 가능합니다. **참고:** 같은 지역 또는 서로 다른 지역에 있는 Kubernetes 클러스터에서 데이터를 전송할 수 있습니다. 

{{site.data.keyword.la_full_notm}}에 대해 읽으십시오. 자세한 정보는 [제품 정보](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about)를 참조하십시오.

{{site.data.keyword.cloud_notm}} 계정의 소유자 또는 구성원인 사용자 ID를 사용하십시오. {{site.data.keyword.cloud_notm}} 사용자 ID를 가져오려면 [등록 ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](https://cloud.ibm.com/login){:new_window}으로 이동하십시오.

{{site.data.keyword.IBM_notm}} ID에는 다음 각 리소스에 대한 IAM 정책이 지정되어 있어야 합니다. 

| 리소스                             | 액세스 정책 범위 | 역할    | 지역    | 정보                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| 리소스 그룹 **기본값**           |  리소스 그룹            | 뷰어  | 미국 남부  | 사용자가 기본 리소스 그룹에서 서비스 인스턴스를 보려면 이 정책이 필요합니다.    |
| {{site.data.keyword.la_full_notm}} 서비스 |  리소스 그룹            |편집자  | 미국 남부  | 사용자가 기본 리소스 그룹에서 {{site.data.keyword.la_full_notm}} 서비스를 프로비저닝하고 관리하려면 이 정책이 필요합니다.   |
| Kubernetes 클러스터 인스턴스          |  리소스                 | 편집자  | 미국 남부  | 이 정책은 Kubernetes 클러스터에서 시크릿 및 LogDNA 에이전트를 구성하는 데 필요합니다. |
{: caption="표 1. 튜토리얼을 완료하는 데 필요한 IAM 정책 목록" caption-side="top"} 

{{site.data.keyword.containerlong}} IAM 역할에 대한 자세한 정보는 [사용자 액세스 권한](/docs/containers?topic=containers-access_reference#access_reference)을 참조하십시오.

{{site.data.keyword.cloud_notm}} CLI 및 Kubernetes CLI 플러그인을 설치하십시오. 자세한 정보는 [{{site.data.keyword.cloud_notm}} CLI 설치](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli)를 참조하십시오.


## 목표
{: #kube_objectives}

이 튜토리얼에서는 {{site.data.keyword.containerlong_notm}} 클러스터에 대한 LogDNA로 로깅을 구성합니다. 특히 다음을 수행합니다.

- {{site.data.keyword.la_full_notm}}를 프로비저닝합니다. 
- LogDNA로 로그 전송을 시작하도록 클러스터에서 LogDNA 에이전트를 구성합니다. 
- LogDNA 대시보드를 열어 로그를 찾습니다. 


## 1단계. {{site.data.keyword.la_full_notm}} 서비스 인스턴스 프로비저닝
{: #kube_step1}

{{site.data.keyword.cloud_notm}} 콘솔을 통해 {{site.data.keyword.la_full_notm}}의 서비스 인스턴스를 프로비저닝하려면 다음 단계를 완료하십시오.

1. Kubernetes 클러스터를 작성한 [{{site.data.keyword.cloud_notm}} 계정 ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](https://cloud.ibm.com/login)에 로그인하십시오.

2. **카탈로그**를 클릭하십시오. {{site.data.keyword.cloud_notm}} 서비스 목록이 열립니다.

3. 표시된 서비스 목록을 필터링하려면 **개발자 도구** 카테고리를 선택하십시오.

4. **{{site.data.keyword.la_full_notm}}**를 클릭하십시오. **관찰 가능성** 대시보드가 열립니다.

5. **인스턴스 작성**을 선택하십시오. 

6. 서비스 인스턴스의 이름을 입력하십시오.

7. 클러스터가 있는 리소스 그룹을 선택하십시오. 기본적으로 **기본** 리소스 그룹이 설정됩니다. 

8. 서비스 인스턴스에 대한 서비스 플랜을 선택하십시오. 기본적으로 **Lite** 플랜이 선택됩니다. 다른 서비스 플랜에 대한 자세한 정보는 [가격 플랜](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans)을 참조하십시오.

9. 로그인한 {{site.data.keyword.cloud_notm}} 리소스 그룹에서 {{site.data.keyword.la_full_notm}} 서비스를 프로비저닝하려면 **작성**을 클릭하십시오. **관찰 가능성** 대시보드가 열리고 서비스에 대한 세부사항이 표시됩니다. 

CLI를 통해 인스턴스를 프로비저닝하려면 [{{site.data.keyword.cloud_notm}} CLI를 통해 인스턴스 프로비저닝](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-provision#provision_cli)을 참조하십시오.
{: tip}

## 2단계. 수집 키 가져오기
{: #kube_step2}

수집 키를 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.cloud_notm}} 계정에 로그인하십시오.

    [{{site.data.keyword.cloud_notm}} 대시보드 ![외부 링크 아이콘](../../icons/launch-glyph.svg "외부 링크 아이콘")](https://cloud.ibm.com/login){:new_window}를 클릭하여 {{site.data.keyword.cloud_notm}} 대시보드를 실행하십시오.

	사용자 ID와 비밀번호로 로그인하면 {{site.data.keyword.cloud_notm}} UI가 열립니다.

2. 탐색 메뉴에서 **관찰 가능성**을 선택하십시오. 

3. **로깅**을 선택하십시오. {{site.data.keyword.la_full_notm}} 대시보드가 열립니다. {{site.data.keyword.cloud_notm}}에서 사용 가능한 로깅 인스턴스의 목록을 볼 수 있습니다.

3. 수집 키를 가져올 인스턴스를 식별하고 **수집 키 보기**를 클릭하십시오.

4. **표시**를 클릭하여 수집 키를 볼 수 있는 창이 열립니다.


## 3단계: LogDNA 인스턴스로 로그를 전송하도록 Kubernetes 클러스터 구성
{: #kube_step3}

{{site.data.keyword.la_full_notm}} 인스턴스로 로그를 보내도록 Kubernetes 클러스터를 구성하려면 클러스터의 각 노드에 `logdna-agent` 팟(Pod)을 설치해야 합니다. LogDNA 에이전트가 이 에이전트가 설치된 팟(Pod)에서 로그 파일을 읽고 로그 데이터를 LogDNA 인스턴스로 전달합니다.

LogDNA 인스턴스로 로그를 전달하도록 Kubernetes 클러스터를 구성하려면 명령행에서 다음 단계를 완료하십시오.

1. 터미널을 열어 {{site.data.keyword.cloud_notm}}에 로그인하십시오.

   ```
   ibmcloud login -a api.ng.bluemix.net
   ```
   {: pre}

   {{site.data.keyword.la_full_notm}} 인스턴스를 프로비저닝한 계정을 선택하십시오.

2. 이 세션에 대한 컨텍스트로 로깅을 구성할 클러스터를 설정하십시오.

   ```
   ibmcloud ks cluster-config <cluster_name_or_ID>
   ```
   {: pre}

   구성 파일의 다운로드가 완료되면 로컬 Kubernetes 구성 파일에 대한 경로를 환경 변수로 설정하는 데 사용할 수 있는 명령이 표시됩니다. 터미널에 표시된 명령을 복사하고 붙여넣어 `KUBECONFIG` 환경 변수를 설정하십시오.

   클러스터에 대한 작업을 수행하기 위해 {{site.data.keyword.containerlong_notm}} CLI에 로그인할 때마다 이 설정을 실행하여 클러스터의 구성 파일에 대한 경로를 세션 변수로 설정해야 합니다. {{site.data.keyword.containerlong_notm}}는 이 변수를 사용하여 클러스터와 연결하는 데 필요한 로컬 구성 파일과 인증서를 찾습니다.
   {: tip}

3. Kubernetes 시크릿을 작성하여 서비스 인스턴스에 대한 logDNA 수집 키를 저장하십시오. LogDNA 수집 키는 logDNA 수집 서버에 대한 보안 웹 소켓을 열고 {{site.data.keyword.la_full_notm}} 서비스로 로깅 에이전트를 인증하는 데 사용됩니다.

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<logDNA_ingestion_key>
    ```
    {: pre}

4. Kubernetes 디먼 세트를 작성하여 Kubernetes 클러스터의 모든 작업자 노드에 LogDNA 에이전트를 배치하십시오. LogDNA 에이전트는 확장자가 `*.log`인 로그 및 팟(Pod)의 `/var/log` 디렉토리에 저장된 확장자 없는 파일을 수집합니다. 기본적으로 로그는 `kube-system`을 포함해 모든 네임스페이스에서 수집되며 자동으로 {{site.data.keyword.la_full_notm}} 서비스에 전달됩니다.

   ```
   kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
   ```
   {: pre}

5. LogDNA 에이전트가 배치되었는지 확인하십시오. 

   ```
   kubectl get pods
   ```
   {: pre}
   
   하나 이상의 LogDNA 팟(Pod)이 표시되면 배치가 성공한 것입니다. LogDNA 팟(Pod)의 수가 클러스터의 작업자 노드 수와 같습니다. 모든 팟(Pod)은 `실행 중` 상태여야 합니다.


## 4단계: LogDNA 대시보드 실행 및 로그 보기
{: #kube_step4}

{{site.data.keyword.cloud_notm}} 콘솔을 통해 LogDNA 대시보드를 실행하려면 다음 단계를 완료하십시오.

1. [{{site.data.keyword.cloud_notm}} 계정 ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](https://cloud.ibm.com/login)에 로그인하십시오.

2. 메뉴 ![메뉴 아이콘](../../../icons/icon_hamburger.svg "메뉴 아이콘")에서 **관찰 가능성**을 선택하십시오.

3. **로깅**을 선택하십시오. {{site.data.keyword.cloud_notm}}에서 사용 가능한 {{site.data.keyword.la_full_notm}} 서비스 인스턴스의 목록이 표시됩니다.

4. 하나의 인스턴스를 선택하고 **LogDNA 보기**를 클릭하십시오. LogDNA 대시보드가 열립니다. **참고:** **무료** 서비스 플랜을 사용하면 최근 로그만 추적할 수 있습니다. 자세한 정보는 [로그 보기](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs)를 참조하십시오.

## 다음 단계
{: #kube_next_steps}

- [로그 필터링](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5)
- [로그 검색](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6)
- [보기 정의](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7)
- [경보 구성](https://docs.logdna.com/docs/alerts). 

**참고:** 일부 기능에는 플랜 업그레이드가 필요합니다.




