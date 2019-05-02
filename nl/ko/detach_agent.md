---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, detach config agent

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

# 인스턴스에서 LogDNA 에이전트 분리
{: #detach_agent}

로그 수집을 중지하도록 로깅 인스턴스에서 LogDNA 에이전트 분리
{:shortdesc}

## Kubernetes 클러스터에서 LogDNA 에이전트 분리
{: #detach_agent_kube}

Kubernetes 클러스터가 {{site.data.keyword.la_full_notm}} 인스턴스로 로그를 전송하는 것을 중지하려면 클러스터에서 LogDNA 에이전트를 제거해야 합니다. 

Kubernetes 클러스터가 LogDNA 인스턴스로 로그를 전달하는 것을 중지하려면 명령행에서 다음 단계를 완료하십시오.

1. 터미널을 여십시오. 그런 다음 [{{site.data.keyword.cloud_notm}} ![외부 링크 아이콘](../../icons/launch-glyph.svg "외부 링크 아이콘")](https://cloud.ibm.com/login){:new_window}에 로그인하고 프롬프트에 따르십시오.

    {{site.data.keyword.la_full_notm}} 인스턴스를 프로비저닝한 계정을 선택하십시오.

2. 클러스터 환경을 설정하십시오. 다음 명령을 실행하십시오.

    먼저 명령을 가져와 환경 변수를 설정하고 Kubernetes 구성 파일을 다운로드하십시오.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    구성 파일의 다운로드가 완료되면 로컬 Kubernetes 구성 파일에 대한 경로를 환경 변수로 설정하는 데 사용할 수 있는 명령이 표시됩니다.

    그런 다음, 터미널에 표시된 명령을 복사하고 붙여넣어 `KUBECONFIG` 환경 변수를 설정하십시오.

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




