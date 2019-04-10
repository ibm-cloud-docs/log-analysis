---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging instance, provision

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

# 인스턴스 프로비저닝
{: #provision}

{{site.data.keyword.la_full_notm}}를 사용하여 로그 데이터를 모니터하고 관리하려면 먼저 {{site.data.keyword.cloud_notm}}에서 서비스의 인스턴스를 프로비저닝해야 합니다.
{:shortdesc}

퍼블릭 클라우드 지역에서 {{site.data.keyword.la_full_notm}} 인스턴스를 프로비저닝하려면 인스턴스와 연관된 서비스 플랜, 로그를 수집한 지역 및 로그에 대한 보존 기간을 판별하는 플랜을 선택해야 합니다. 7, 14 또는 30일 보존 기간 중에서 선택할 수 있습니다.

또는 {{site.data.keyword.la_full_notm}}가 시스템을 통과할 때 로그를 보는 데 사용할 수 있는 `Lite` 플랜을 제공합니다. 로그 추적을 사용하여 로그를 볼 수 있습니다. 또한 장기 보존 기간 플랜으로 업그레이드를 준비하기 위해 필터를 디자인할 수 있습니다. 이 플랜에는 0일의 보존 기간이 있습니다.


## 관찰 가능성 대시보드를 통해 인스턴스 프로비저닝
{: #provision_ui}

{{site.data.keyword.cloud_notm}}의 관찰 가능성 대시보드에서 인스턴스를 프로비저닝하려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.cloud_notm}} 계정에 로그인하십시오.

    {{site.data.keyword.cloud_notm}} 대시보드는 [{{site.data.keyword.cloud_notm}} 대시보드 ![외부 링크 아이콘](../../icons/launch-glyph.svg "외부 링크 아이콘")](https://cloud.ibm.com/login){:new_window}에 있습니다.

	사용자 ID와 비밀번호로 로그인하면 {{site.data.keyword.cloud_notm}} UI가 열립니다.

2. 메뉴 아이콘(![메뉴 아이콘](../../icons/icon_hamburger.svg))으로 이동하십시오. 그런 다음 **관찰 가능성**을 선택하여 *관찰 가능성* 대시보드에 액세스하십시오.

3. **로깅**을 선택한 다음 **인스턴스 작성**을 클릭하십시오. 

4. 서비스 인스턴스의 이름을 입력하십시오.

5. 리소스 그룹을 선택하십시오. 

    기본적으로 **기본** 리소스 그룹이 설정됩니다.

    **참고:** 리소스 그룹을 선택할 수 없는 경우 인스턴스를 프로비저닝할 리소스 그룹에 대한 편집 권한이 있는지 확인하십시오.

6. `Lite` 서비스 플랜을 선택하십시오. 

    기본적으로 Lite 플랜이 설정됩니다.

    다른 서비스 플랜에 대한 자세한 정보는 [가격 플랜](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans)을 참조하십시오.

7. **작성**을 클릭하십시오.

인스턴스를 프로비저닝하면 *로깅* 대시보드가 열립니다. 

그 다음 LogDNA 에이전트를 추가하여 로그 소스를 구성하십시오. 이 에이전트는 로그를 수집하고 인스턴스로 로그를 전달합니다. 



## 카탈로그를 통해 인스턴스 프로비저닝
{: #provision_catalog}

{{site.data.keyword.cloud_notm}} 카탈로그를 통해 {{site.data.keyword.la_full_notm}}의 인스턴스를 프로비저닝하려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.cloud_notm}} 계정에 로그인하십시오.

    [{{site.data.keyword.cloud_notm}} 대시보드 ![외부 링크 아이콘](../../icons/launch-glyph.svg "외부 링크 아이콘")](https://cloud.ibm.com/login){:new_window}를 클릭하여 {{site.data.keyword.cloud_notm}} 대시보드를 실행하십시오.

	사용자 ID와 비밀번호로 로그인하면 {{site.data.keyword.cloud_notm}} UI가 열립니다.

2. **카탈로그**를 클릭하십시오. {{site.data.keyword.cloud_notm}}에서 사용 가능한 서비스 목록이 열립니다.

3. 표시된 서비스 목록을 필터링하려면 **개발자 도구** 카테고리를 선택하십시오.

4. **{{site.data.keyword.la_full_notm}}** 타일을 클릭하십시오. 

5. 서비스 인스턴스의 이름을 입력하십시오.

6. 리소스 그룹을 선택하십시오. 

    기본적으로 **기본** 리소스 그룹이 설정됩니다.

    **참고:** 리소스 그룹을 선택할 수 없는 경우 인스턴스를 프로비저닝할 리소스 그룹에 대한 편집 권한이 있는지 확인하십시오.

7. `Lite` 서비스 플랜을 선택하십시오. 

    기본적으로 Lite 플랜이 설정됩니다.

    다른 서비스 플랜에 대한 자세한 정보는 [가격 플랜](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans)을 참조하십시오.

8. **작성**을 클릭하십시오.

인스턴스를 프로비저닝하면 *로깅* 대시보드가 열립니다. 

그 다음 LogDNA 에이전트를 추가하여 로그 소스를 구성하십시오. 이 에이전트는 로그를 수집하고 인스턴스로 로그를 전달합니다. 



## CLI를 통해 인스턴스 프로비저닝
{: #provision_cli}

명령행을 통해 {{site.data.keyword.la_full_notm}}의 인스턴스를 프로비저닝하려면 다음 단계를 완료하십시오.

1. [전제조건] {{site.data.keyword.cloud_notm}} CLI 설치입니다.

   자세한 정보는 [{{site.data.keyword.cloud_notm}} CLI 설치](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli)를 참조하십시오.

   CLI를 설치한 경우 다음 단계를 계속하십시오.

2. 인스턴스를 프로비저닝할 {{site.data.keyword.cloud_notm}}의 지역에 로그인하십시오. 다음 명령을 실행하십시오. [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. 인스턴스를 프로비저닝할 리소스 그룹을 설정하십시오. 다음 명령을 실행하십시오. [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    기본적으로 `기본` 리소스 그룹이 설정됩니다.

4. 인스턴스를 작성하십시오. [`ibmcloud resource service-instance-create`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_create) 명령을 실행하십시오.

    ```
    ibmcloud resource service-instance-create NAME logdna SERVICE_PLAN_NAME LOCATION
    ```
    {: codeblock}

    여기서,

    NAME은 인스턴스의 이름입니다.

    *logdna* 값은 {{site.data.keyword.cloud_notm}}에 있는 {{site.data.keyword.la_full_notm}} 서비스의 이름입니다.

    SERVICE_PLAN_NAME은 플랜 유형입니다. 올바른 값은 *lite*, *7-days*, *14-days*, *30-days*입니다.
    
    LOCATION은 LogDNA 인스턴스가 작성된 지역입니다. 올바른 값은 *us-south*입니다.

    예를 들어, 7일의 보존 플랜이 있는 인스턴스를 프로비저닝하려면 다음 명령을 실행하십시오.

    ```
    ibmcloud resource service-instance-create logdna-instance-01 logdna 7-day us-south
    ```
    {: codeblock}

5. 인스턴스를 조작할 수 있는 **관리자** 권한으로 서비스 키를 작성하십시오. [`ibmcloud resource service-key-create`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_key_create) 명령을 실행하십시오.

    ```
    ibmcloud resource service-key-create NAME ROLE_NAME --instance-name SERVICE_INSTANCE_NAME
    ```
    {: codeblock}

    여기서,

    NAME은 API 키의 이름입니다. 나중에 API 키를 식별하는 데 도움이 되도록 {{site.data.keyword.la_full_notm}} 인스턴스와 같은 API 키에 이름을 지정할 수 있습니다.

    ROLE_NAME은 사용 가능한 권한을 정의하는 역할입니다. 올바른 값은 *editor*, *operator*, *administrator*입니다.

    SERVICE_INSTANCE_NAME은 {{site.data.keyword.cloud_notm}}의 인스턴스 이름입니다.

    예를 들어, 서비스 인스턴스에서 *관리자* 권한으로 *logdna-instance-01* 인스턴스에 대한 API 키를 작성하려면 다음 명령을 실행하십시오.

    ```
    ibmcloud resource service-key-create logdna-instance-01 Administrator --instance-name logdna-instance-01
    ```
    {: pre}

    이 명령의 출력에는 LogDNA 수집 키 및 인스턴스의 `crn` 값과 같이 여러 값이 포함됩니다.


