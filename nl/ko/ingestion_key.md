---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion key

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

# 수집 키에 대한 작업
{: #ingestion_key}

수집 키는 LogDNA 에이전트를 구성하고 {{site.data.keyword.cloud_notm}}의 {{site.data.keyword.la_full_notm}} 인스턴스로 로그를 전달하는 데 사용해야 하는 보안 키입니다. 인스턴스를 프로비저닝할 때 자동으로 수집 키를 가져옵니다. 또는 인스턴스에 대한 서비스 ID를 작성하여 수집 키를 얻을 수도 있습니다. 
{:shortdesc}

**참고:** 

* {{site.data.keyword.la_full_notm}} Web UI를 통해 수집 키에 대한 작업을 수행하려면 {{site.data.keyword.la_full_notm}} 서비스에 대한 플랫폼 역할이 **뷰어**이고 서비스 역할이 **관리자**인 IAM 정책을 사용해야 합니다. 
* {{site.data.keyword.cloud_notm}} UI를 통해 수집 키에 대한 작업을 수행하려면 {{site.data.keyword.la_full_notm}} 서비스에 대한 플랫폼 역할이 **편집자**이고 서비스 역할이 **관리자**인 IAM 정책을 사용해야 합니다. 


## {{site.data.keyword.cloud_notm}} UI를 통해 수집 키 가져오기
{: #ibm_cloud_ui}

{{site.data.keyword.cloud_notm}} UI를 사용하여 {{site.data.keyword.la_full_notm}} 인스턴스에 대한 수집 키를 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.cloud_notm}} 계정에 로그인하십시오.

    [{{site.data.keyword.cloud_notm}} 대시보드 ![외부 링크 아이콘](../../icons/launch-glyph.svg "외부 링크 아이콘")](https://cloud.ibm.com/login){:new_window}를 클릭하여 {{site.data.keyword.cloud_notm}} 대시보드를 실행하십시오.

	사용자 ID와 비밀번호로 로그인하면 {{site.data.keyword.cloud_notm}} UI가 열립니다.

2. 탐색 메뉴에서 **관찰 가능성**을 선택하십시오. 

3. **로깅**을 선택하십시오. {{site.data.keyword.la_full_notm}} 대시보드가 열립니다. {{site.data.keyword.cloud_notm}}에서 사용 가능한 로깅 인스턴스의 목록을 볼 수 있습니다.

3. 수집 키를 가져올 인스턴스를 식별하고 **수집 키 보기**를 클릭하십시오.

4. **표시**를 클릭하여 수집 키를 볼 수 있는 창이 열립니다.


## {{site.data.keyword.la_full_notm}} Web UI를 통해 수집 키 가져오기
{: #logdna_ui}

{{site.data.keyword.la_full_notm}} Web UI를 사용하여 {{site.data.keyword.la_full_notm}} 인스턴스에 대한 수집 키를 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.la_full_notm}} Web UI를 실행하십시오. 자세한 정보는 [{{site.data.keyword.la_full_notm}} Web UI 실행](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)을 참조하십시오.

2. **구성** 아이콘을 선택하십시오. 그런 다음 **조직**을 선택하십시오. 

3. **API 키**를 선택하십시오.

작성된 수집 키를 볼 수 있습니다. 

**참고:** 한 번에 하나의 수집 키만 활성 상태입니다. 


## {{site.data.keyword.cloud_notm}} CLI를 통해 수집 키 가져오기
{: #ibm_cloud_cli}

명령행을 통해 {{site.data.keyword.la_full_notm}} 인스턴스에 대한 수집 키를 가져오려면 다음 단계를 완료하십시오.

1. [전제조건] {{site.data.keyword.cloud_notm}} CLI를 설치하십시오.

   자세한 정보는 [{{site.data.keyword.cloud_notm}} CLI 설치](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about)를 참조하십시오.

   CLI를 설치한 경우 다음 단계를 계속하십시오.

2. 인스턴스가 실행 중인 {{site.data.keyword.cloud_notm}}의 지역에 로그인하십시오. 다음 명령을 실행하십시오. [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. {{site.data.keyword.la_full_notm}} 인스턴스가 실행 중인 리소스 그룹을 설정하십시오. 다음 명령을 실행하십시오. [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)(옵션 `-g` 포함).

    기본적으로 `기본` 리소스 그룹이 설정됩니다.

4. {{site.data.keyword.la_full_notm}} 인스턴스와 연관된 API 키의 이름을 가져오십시오. [`ibmcloud resource service-keys`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_keys) 명령을 실행하십시오.

    ```
    ibmcloud resource service-keys
    ```
    {: codeblock}

    인스턴스와 연관된 서비스 키를 식별하십시오.

5. 수집 키를 가져오십시오. [`ibmcloud resource service-key`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_key) 명령을 실행하십시오.

    ```
    ibmcloud resource service-key APIKEY_NAME
    ```
    {: codeblock}

    여기서 APIKEY_NAME은 API 키의 이름입니다.
 
    이 명령의 출력에는 인스턴스에 대한 수집 키가 포함된 **ingestion_key** 필드가 있습니다.


## 수집 키 재설정 
{: #reset}

수집 키가 손상되었거나 여러 일 후에 정책을 갱신하는 경우, 새 키를 생성하고 이전 키를 삭제할 수 있습니다.

{{site.data.keyword.la_full_notm}} Web UI를 사용하여 {{site.data.keyword.la_full_notm}} 인스턴스에 대한 수집 키를 갱신하려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.la_full_notm}} Web UI를 실행하십시오. 자세한 정보는 [{{site.data.keyword.la_full_notm}} Web UI 실행](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)을 참조하십시오.

2. **구성** 아이콘을 선택하십시오. 그런 다음 **조직**을 선택하십시오. 

3. **API 키**를 선택하십시오.

    작성된 수집 키를 볼 수 있습니다. 

4. **수집 키 생성**을 선택하십시오.

    새 키가 목록에 추가됩니다.

5. 이전 수집 키를 삭제하십시오. **삭제**를 클릭하십시오.

**참고:** 수집 키를 재설정한 후 이 {{site.data.keyword.la_full_notm}} 인스턴스로 로그를 전달하도록 구성한 로그 소스에 대한 수집 키를 업데이트해야 합니다.



