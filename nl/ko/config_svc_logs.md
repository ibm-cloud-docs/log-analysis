---

copyright:
  years:  2018, 2019
lastupdated: "2019-04-02"

keywords: LogDNA, IBM, Log Analysis, logging instance, enable, service logs

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

# {{site.data.keyword.cloud_notm}} 서비스 로그 구성
{: #config_svc_logs}

한 지역에 여러 {{site.data.keyword.la_full_notm}} 인스턴스가 있을 수 있습니다. 그러나 한 지역에서 하나의 인스턴스만 {{site.data.keyword.cloud_notm}}의 사용 설정된 서비스에서 로그를 수신하도록 구성할 수 있습니다.
{:shortdesc}



## 관찰 가능성 대시보드를 통해 플랫폼 서비스 로그 구성
{: #config_svc_logs_ui}

{{site.data.keyword.cloud_notm}}의 관찰 가능성 대시보드에서 인스턴스를 구성하려면 다음 단계를 완료하십시오.

1. [{{site.data.keyword.cloud_notm}} 계정 ![외부 링크 아이콘](../../icons/launch-glyph.svg "외부 링크 아이콘")에 로그인하십시오](https://cloud.ibm.com/login){:new_window}.

	사용자 ID와 비밀번호로 로그인하면 {{site.data.keyword.cloud_notm}} UI가 열립니다.

2. 메뉴 아이콘(![메뉴 아이콘](../../icons/icon_hamburger.svg))으로 이동하십시오. 그런 다음 **관찰 가능성**을 선택하여 *관찰 가능성* 대시보드에 액세스하십시오.

3. **로깅**을 선택한 후 **플랫폼 서비스 로그 구성**을 클릭하십시오. 

4. 클라우드 플랫폼의 사용 설정된 서비스에서 로그를 수신할 LogDNA 인스턴스를 선택하십시오.

5. 지역을 선택하십시오. 

6. 인스턴스를 선택하십시오.

7. **저장**을 클릭하십시오. 

기본 *관찰 가능성* 페이지가 열립니다.

서비스 로그를 수신하도록 선택하는 인스턴스에는 **플랫폼 서비스 로그** 플래그가 표시됩니다.

{{site.data.keyword.la_full_notm}}에 로그를 전송할 수 있도록 설정된 서비스에 대한 자세한 정보는 [클라우드 서비스](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services)를 참조하십시오.

