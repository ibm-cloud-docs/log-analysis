---

copyright:
  years:  2018, 2019
lastupdated: "2019-05-01"

keywords: LogDNA, IBM, Log Analysis, logging, kubernetes, tutorial, reset ingestion key

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


# {{site.data.keyword.la_full_notm}} 인스턴스로 로그를 전달하도록 Kubernetes 클러스터에서 사용되는 수집 키 재설정
{: #kube_reset}

클러스터에서 {{site.data.keyword.cloud_notm}}의 {{site.data.keyword.la_full_notm}} 인스턴스로 로그를 전달하는 데 사용하는 수집 키가 손상되면, 키를 재설정하고 Kubernetes 클러스터 구성을 업데이트하여 새 수집 키를 사용해야 합니다. 
{:shortdesc}

## 시작하기 전에
{: #kube_reset_prereqs}

미국 남부 지역에서 작업합니다. 두 리소스, 즉 {{site.data.keyword.la_full_notm}} 인스턴스와 Kubernetes 클러스터 모두 동일한 계정에서 실행되어야 합니다.

{{site.data.keyword.la_full_notm}} 인스턴스는 **기본** 리소스 그룹에 프로비저닝됩니다.

{{site.data.keyword.la_full_notm}}에 대해 읽으십시오. 자세한 정보는 [LogDNA 정보](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about)를 참조하십시오.

이 튜토리얼에서 단계를 완료하려면 {{site.data.keyword.IBM_notm}} ID에 다음 각 리소스에 대해 IAM 정책을 지정해야 합니다. 

| 리소스                             | 액세스 정책 범위 | 역할    | 지역    | 정보                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| 리소스 그룹 **기본값**           |  리소스 그룹            | 뷰어  | 미국 남부  | 사용자가 기본 리소스 그룹에서 서비스 인스턴스를 보려면 이 정책이 필요합니다.    |
| {{site.data.keyword.la_full_notm}} 서비스 |  리소스 그룹            | 편집자 </br>관리자 | 미국 남부  | 사용자가 수집 키를 재설정하려면 이 정책이 필요합니다.   |
| Kubernetes 클러스터 인스턴스          |  리소스                  | 편집자  | 미국 남부  | 이 정책은 Kubernetes 클러스터에서 시크릿 및 LogDNA 에이전트를 삭제하고 구성하는 데 필요합니다. |
{: caption="표 1. 튜토리얼을 완료하는 데 필요한 IAM 정책 목록" caption-side="top"} 

{{site.data.keyword.containerlong}} IAM 역할에 대한 자세한 정보는 [사용자 액세스 권한](/docs/containers?topic=containers-access_reference#access_reference)을 참조하십시오.

{{site.data.keyword.cloud_notm}} CLI 및 Kubernetes CLI 플러그인을 설치하십시오. 자세한 정보는 [{{site.data.keyword.cloud_notm}} CLI 설치](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli)를 참조하십시오.


## 1단계: 수집 키 재설정
{: #kube_reset_step1}

{{site.data.keyword.la_full_notm}} Web UI를 사용하여 {{site.data.keyword.la_full_notm}} 인스턴스에 대한 수집 키를 갱신하려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.la_full_notm}} Web UI를 실행하십시오. 자세한 정보는 [{{site.data.keyword.la_full_notm}} Web UI 실행](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)을 참조하십시오.

2. **구성** 아이콘을 선택하십시오. 그런 다음 **조직**을 선택하십시오. 

3. **API 키**를 선택하십시오.

    작성된 수집 키를 볼 수 있습니다. 

4. **수집 키 생성**을 선택하십시오.

    새 키가 목록에 추가됩니다.

5. 이전 수집 키를 삭제하십시오. **삭제**를 클릭하십시오.


## 2단계: 이전 수집 키를 사용하는 클러스터에서 구성 제거
{: #kube_reset_step2}

다음 단계를 완료하십시오.

1. 터미널을 여십시오. 그런 다음 {{site.data.keyword.cloud_notm}}에 로그인하십시오. 다음 명령을 실행하고 프롬프트를 따르십시오.

    ```
    ibmcloud login -a cloud.ibm.com
    ```
    {: codeblock}

    {{site.data.keyword.la_full_notm}} 인스턴스를 프로비저닝한 계정을 선택하십시오.

2. 클러스터 환경을 설정하십시오. 다음 명령을 실행하십시오.

    먼저 명령을 가져와 환경 변수를 설정하고 Kubernetes 구성 파일을 다운로드하십시오.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    구성 파일의 다운로드가 완료되면 로컬 Kubernetes 구성 파일에 대한 경로를 환경 변수로 설정하는 데 사용할 수 있는 명령이 표시됩니다.

    그런 다음, 터미널에 표시된 명령을 복사하고 붙여넣어 KUBECONFIG 환경 변수를 설정하십시오.

    **참고:** 클러스터에 대한 작업을 수행하기 위해 {{site.data.keyword.containerlong}} CLI에 로그인할 때마다 이러한 명령을 실행하여 클러스터의 구성 파일에 대한 경로를 세션 변수로 설정해야 합니다. Kubernetes CLI는 이 변수를 사용하여 {{site.data.keyword.cloud_notm}}의 클러스터와 연결하는 데 필요한 로컬 구성 파일 및 인증서를 찾습니다.

3. Kubernetes 클러스터에서 시크릿을 제거하십시오. Kubernetes 시크릿에는 LogDNA 수집 키가 포함됩니다. 다음 명령을 실행하십시오.

    ```
    kubectl delete secret logdna-agent-key
    ```
    {: codeblock}

4. Kubernetes 클러스터의 모든 작업자(노드)에서 LogDNA 에이전트를 제거하십시오. LogDNA 에이전트는 로그를 수집하고 전달합니다. 다음 명령을 실행하십시오.

    ```
    kubectl delete daemonset logdna-agent
    ```
    {: codeblock}

5. LogDNA 에이전트가 삭제되었는지 확인하십시오. 다음 명령을 실행하십시오.

    ```
    kubectl get pods
    ```
    {: codeblock}

    LogDNA 팟(Pod)이 표시되지 않아야 합니다.


## 3단계: 새 수집 키를 사용하여 Kubernetes 클러스터 구성
{: #kube_reset_step3}

LogDNA 인스턴스로 로그를 전달하도록 Kubernetes 클러스터를 구성하려면 명령행에서 다음 단계를 완료하십시오.

1. 터미널을 여십시오. 그런 다음 {{site.data.keyword.cloud_notm}}에 로그인하십시오. 다음 명령을 실행하고 프롬프트를 따르십시오.

    ```
    ibmcloud login -a cloud.ibm.com
    ```
    {: codeblock}

    {{site.data.keyword.la_full_notm}} 인스턴스를 프로비저닝한 계정을 선택하십시오.

2. 클러스터 환경을 설정하십시오. 다음 명령을 실행하십시오.

    먼저 명령을 가져와 환경 변수를 설정하고 Kubernetes 구성 파일을 다운로드하십시오.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    구성 파일의 다운로드가 완료되면 로컬 Kubernetes 구성 파일에 대한 경로를 환경 변수로 설정하는 데 사용할 수 있는 명령이 표시됩니다.

    그런 다음, 터미널에 표시된 명령을 복사하고 붙여넣어 KUBECONFIG 환경 변수를 설정하십시오.

    **참고:** 클러스터에 대한 작업을 수행하기 위해 {{site.data.keyword.containerlong}} CLI에 로그인할 때마다 이러한 명령을 실행하여 클러스터의 구성 파일에 대한 경로를 세션 변수로 설정해야 합니다. Kubernetes CLI는 이 변수를 사용하여 {{site.data.keyword.cloud_notm}}의 클러스터와 연결하는 데 필요한 로컬 구성 파일 및 인증서를 찾습니다.

3. Kubernetes 클러스터에 시크릿을 추가하십시오. 다음 명령을 실행하십시오.

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE
    ```
    {: codeblock}

    LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE는 인스턴스에 대한 LogDNA 수집 키를 표시합니다.

    Kubernetes 시크릿에는 LogDNA 수집 키가 포함됩니다. LogDNA 수집 키는 {{site.data.keyword.la_full_notm}} 서비스로 로깅 에이전트를 인증하는 데 사용됩니다. 이는 로깅 백엔드 시스템에서 수집 서버에 대한 보안 웹 소켓을 여는 데 사용됩니다.

4. Kubernetes 클러스터의 모든 작업자(노드)에서 LogDNA 에이전트를 구성하십시오. 다음 명령을 실행하십시오.

    ```
    kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
    ```
    {: codeblock}

    LogDNA 에이전트는 로그를 수집하고 전달합니다.

    에이전트는 /var/log에 있는 확장자 없는 파일과 확장자가 *.log인 로그를 자동으로 수집합니다. 기본적으로 로그는 kube-system을 포함해 모든 네임스페이스에서 수집됩니다.

5. LogDNA 에이전트가 작성되었는지 확인하고 해당 상태를 확인하십시오. 다음 명령을 실행하십시오.

    ```
    kubectl get pods
    ```
    {: codeblock}


## 4단계: LogDNA Web UI 실행
{: #kube_reset_step4}

{{site.data.keyword.cloud_notm}} UI를 통해 IBM Log Analysis with LogDNA 대시보드를 실행하려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.cloud_notm}} 계정에 로그인하십시오.

    [{{site.data.keyword.cloud_notm}} 대시보드 ![외부 링크 아이콘](../../icons/launch-glyph.svg "외부 링크 아이콘")](https://cloud.ibm.com/login){:new_window}를 클릭하여 {{site.data.keyword.cloud_notm}} 대시보드를 실행하십시오.

	사용자 ID와 비밀번호로 로그인하면 {{site.data.keyword.cloud_notm}} 대시보드가 열립니다.

2. 탐색 메뉴에서 **관찰 가능성**을 선택하십시오. 

3. **로깅**을 선택하십시오. 

    {{site.data.keyword.cloud_notm}}에서 사용 가능한 {{site.data.keyword.la_full_notm}} 인스턴스의 목록이 표시됩니다.

3. 하나의 인스턴스를 선택하십시오. 그런 다음 **로그 보기**를 클릭하십시오.

    LogDNA Web UI가 열리고 클러스터 로그가 표시됩니다.


## 5단계: 로그 보기
{: #kube_reset_step5}

LogDNA Web UI에서 시스템을 통과할 때 로그를 볼 수 있습니다. 로그 추적을 사용하여 로그를 봅니다. 

**참고:** **무료** 서비스 플랜을 사용하면 최근 로그만 추적할 수 있습니다.



## 다음 단계
{: #kube_reset_next_steps}

  [클러스터 로그를 필터링](https://docs.logdna.com/docs/filters)하고, [클러스터 로그를 검색](https://docs.logdna.com/docs/search)하고, [보기를 정의](https://docs.logdna.com/docs/views)하고, [경보를 구성](https://docs.logdna.com/docs/alerts)하려면, {{site.data.keyword.la_full_notm}} 플랜을 유료 플랜으로 업그레이드해야 합니다.



