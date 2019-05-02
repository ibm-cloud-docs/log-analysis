---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging instance, delete

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

# 인스턴스 제거
{: #remove}

{{site.data.keyword.Bluemix}} UI에서 또는 명령행을 통해 {{site.data.keyword.la_full_notm}} 서비스의 인스턴스를 제거할 수 있습니다.
{:shortdesc}

{{site.data.keyword.cloud_notm}}에서 인스턴스를 제거할 때 다음 태스크를 완료하여 정리하십시오.

1. 제거할 {{site.data.keyword.la_full_notm}} 인스턴스로 메트릭을 전달하는 소스 목록을 기록하십시오. 각 소스에서 LogDNA 에이전트를 제거해야 합니다.
2. 인스턴스에 대한 작업을 수행할 수 있도록 사용자에게 부여되는 권한을 제거하십시오. 

    특정 인스턴스에 대한 작업을 수행하기 위해 전용 액세스 그룹을 사용하여 액세스를 관리하는 경우 이러한 액세스 그룹을 제거해야 합니다.

    액세스 그룹을 사용하여 다중 로깅 인스턴스에 대한 액세스를 관리하는 경우 제거할 인스턴스에 대한 권한을 부여하는 정책을 제거해야 합니다.
    
    사용자에게 개별 정책을 부여하는 경우 이 인스턴스에 대한 작업을 수행할 수 있는 권한을 가진 사용자의 목록을 수집해야 합니다. 그런 다음 식별되는 각 사용자에 대해 삭제할 인스턴스와 관련된 정책을 제거해야 합니다.


그런 다음 {{site.data.keyword.cloud_notm}} 대시보드에서 인스턴스를 삭제하십시오.


## {{site.data.keyword.cloud_notm}} UI를 통해 인스턴스 제거
{: #remove_ui}

{{site.data.keyword.cloud_notm}} UI를 사용하여 {{site.data.keyword.la_full_notm}}의 인스턴스를 제거하려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.cloud_notm}} 계정에 로그인하십시오.

    [{{site.data.keyword.cloud_notm}} 대시보드 ![외부 링크 아이콘](../../icons/launch-glyph.svg "외부 링크 아이콘")](https://cloud.ibm.com/login){:new_window}를 클릭하여 {{site.data.keyword.cloud_notm}} 대시보드를 실행하십시오.

	사용자 ID와 비밀번호로 로그인하면 {{site.data.keyword.cloud_notm}} UI가 열립니다.

2. 메뉴 아이콘 ![메뉴 아이콘](../../icons/icon_hamburger.svg) &gt; **관찰 가능성**으로 이동하여 *관찰 가능성* 대시보드에 액세스하십시오.

3. **로깅**을 선택하십시오. 로깅 인스턴스의 목록이 표시됩니다.

4. 삭제할 인스턴스를 선택하십시오.

5. *조치* 메뉴에서 **제거**를 선택하십시오.


## CLI를 통해 인스턴스 제거
{: #remove_cli}

명령행을 통해 {{site.data.keyword.la_full_notm}}의 인스턴스를 제거하려면 다음 단계를 완료하십시오.

1. [전제조건] {{site.data.keyword.cloud_notm}} CLI 설치입니다.

   자세한 정보는 [{{site.data.keyword.cloud_notm}} CLI 설치](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli)를 참조하십시오.

   CLI를 설치한 경우 다음 단계를 계속하십시오.

2. 인스턴스를 프로비저닝할 {{site.data.keyword.cloud_notm}}의 지역에 로그인하십시오. 다음 명령을 실행하십시오. [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. 인스턴스가 프로비저닝된 리소스 그룹을 설정하십시오. 다음 명령을 실행하십시오. [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    기본적으로 *기본* 리소스 그룹이 설정됩니다.

4. 인스턴스를 제거하십시오. [`ibmcloud resource service-instance-delete`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_delete) 명령을 실행하십시오.

    ```
    ibmcloud resource service-instance-delete NAME 
    ```
    {: codeblock}

    여기서 NAME은 인스턴스의 이름입니다.

    예를 들어, 인스턴스를 제거하려면 다음 명령을 실행하십시오.

    ```
    ibmcloud resource service-instance-delete logdna-instance-01
    ```
    {: codeblock}



