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

# Kibana 로그 형식
{: #kibana_formats}

*검색* 페이지에서 각 로그 항목에 여러 가지 필드를 표시하도록 Kibana를 구성할 수 있습니다.
{:shortdesc}



## Cloud Foundry 애플리케이션의 Kibana 로그 형식
{: #kibana_log_format_cf}

*검색* 페이지에서 각 로그 항목에 다음과 같은 필드를 표시하도록 Kibana를 구성할 수 있습니다.

|필드 |설명 |
|-------|-------------|
|@timestamp |`yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> 로그된 이벤트의 시간입니다. <br> 시간소인은 밀리초 단위까지 정의됩니다. |
|@version |이벤트의 버전입니다. |
|ALCH_TENANT_ID |{{site.data.keyword.Bluemix_notm}} 영역의 ID입니다. |
|\_id |로그 문서에 대한 고유 ID입니다. |
|\_index |로그 항목에 대한 색인입니다. |
|\_type |로그의 유형입니다(예: *syslog*). |
|app_name |애플리케이션의 이름입니다. |
|application_id |애플리케이션의 고유 ID입니다. |
|host |로그 데이터를 생성한 애플리케이션의 이름입니다. |
|instance_id |로그 데이터를 생성한 애플리케이션 인스턴스의 인스턴스 ID입니다. |
|loglevel |로그된 이벤트의 심각도입니다. |
|message |컴포넌트에서 발행하는 메시지입니다. <br> 메시지는 컨텍스트에 따라 달라집니다. |
|message_type |로그 메시지가 기록되는 스트림입니다. <br> * **OUT** - stdout 스트림을 참조합니다. <br> * **ERR** - stderr 스트림을 참조합니다. |
|org_id |{{site.data.keyword.Bluemix_notm}} 조직의 고유 ID입니다. |
|org_name |사용자의 앱이 스테이징된 {{site.data.keyword.Bluemix_notm}} 조직의 이름입니다. |
|origin |이벤트가 생성된 컴포넌트입니다. |
|source_id |로그를 생성하는 컴포넌트입니다. <br> 다음 목록에서는 각 컴포넌트의 로그에 대해 설명합니다. <br> * **API**: 사용자의 앱 상태에 변경을 요청하는 API 호출에 로그된 응답. <br> * **APP**: 사용자의 앱에서 로그된 응답. <br> * **CELL**: 앱이 시작, 중지 또는 충돌할 때 표시하는 Diego 셀에서 로그된 응답. <br> * **LGR**: 로깅 프로세스와 함께 문제점을 표시하는 Loggregator에서 로그된 응답. <br> * **RTR**: 사용자의 앱에 HTTP 요청을 라우트할 때 라우터에서 로그된 응답. <br> * **SSH**: `cf ssh` 명령을 사용하여 사용자가 앱 컨테이너에 액세스할 때 Diego 셀에서 로그된 응답. <br> * **STG**: 앱을 스테이징하거나 다시 스테이징할 때 Diego 셀 또는 DEA(Droplet Execution Agent)에서 로그된 응답. |
|space_name |사용자의 앱이 스테이징된 {{site.data.keyword.Bluemix_notm}} 영역의 이름입니다. |
|timestamp |로그된 이벤트의 시간입니다. 시간소인은 밀리초 단위까지 정의됩니다. |
{: caption="표 1. CF 앱의 필드" caption-side="top"}



## Kubernetes 클러스터에 배치된 Docker 컨테이너에 대한 Kibana 로그 형식
{: #kibana_log_format_containers_kubernetes}

*검색* 페이지에서 각 로그 항목에 다음과 같은 필드를 표시하도록 Kibana를 구성할 수 있습니다. 이러한 필드는 {{site.data.keyword.IBM}}에 의해 설정되며 메시지 데이터가 포함됩니다. 

|필드 |설명 |기타 정보 |
|-------|-------------|---------------------------|
|@timestamp |`yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> 로그된 이벤트의 시간입니다. <br> 시간소인은 밀리초 단위까지 정의됩니다. | |
|@version |이벤트의 버전입니다. | |
|ALCH_TENANT_ID |{{site.data.keyword.Bluemix_notm}} 영역의 ID입니다. | |
|\_id |로그 문서에 대한 고유 ID입니다. | |
|\_index |로그 항목에 대한 색인입니다. | |
|\_score |  |  |
|\_type |로그의 유형입니다(예: *logs*). | |
|crn_str |로그의 소스에 대한 정보입니다. |기본적으로 이 필드는 {{site.data.keyword.IBM_notm}}에 의해 설정됩니다. <br> **참고**: 올바른 JSON 형식으로 로그 메시지를 전송하고 필드 중 하나가 `crn`으로 이름 지정된 경우, 필드의 값을 메시지에 설정된 값으로 겹쳐씁니다.  |  
|docker.container_id_str |포드에서 실행 중인 컨테이너의 GUID입니다. | |
|ibm-containers.account_str |{{site.data.keyword.Bluemix_notm}} 계정의 GUID입니다.  |  |
|ibm-containers.cluster_id_str |Kubernetes 클러스터의 GUID입니다.  |  |
|ibm-containers.cluster_type_str |  |{{site.data.keyword.IBM_notm}} 내부 사용에 예약된 값입니다. |
|ibm-containers.region_str |{{site.data.keyword.Bluemix_notm}}의 지역입니다.  |  |
|kubernetes.container_name_str |앱이 배치된 컨테이너의 이름입니다.  |  |
|kubernetes.host |컨테이너가 실행 중인 작업자의 공용 IP 주소입니다. |  |
|kubernetes.labels.*example_label_name*\_str |포드와 같은 Kubernetes 오브젝트에 첨부하는 키-값 쌍입니다. |Kubernetes 오브젝트에 첨부하는 각 레이블은 Kibana에 표시되는 로그 항목에서 필드로 나열됩니다. <br> 0 이상의 레이블이 있습니다. |
|kubernetes.namespace_name_str |컨테이너가 배치된 Kubernetes 네임스페이스입니다. |  |
|kubernetes.pod_id_str |컨테이너가 배치된 포드의 GUID입니다. |  |
|kubernetes.pod_name_str |포드의 이름입니다. |  |
|message |전체 메시지입니다. |올바른 JSON 형식화된 메시지를 전송하는 경우, 각 필드는 개별적으로 구문 분석되며 Kibana에 표시됩니다.  |
|stream_str |  |{{site.data.keyword.IBM_notm}} 내부 사용에 예약된 값입니다. |
|tag_str |  |{{site.data.keyword.IBM_notm}} 내부 사용에 예약된 값입니다. |
{: caption="표 3. Docker 컨테이너의 필드" caption-side="top"}


## {{site.data.keyword.messagehub}}의 Kibana 로그 형식
{: #kibana_log_format_messagehub}

*검색* 페이지에서 각 로그 항목에 다음과 같은 필드를 표시하도록 Kibana를 구성할 수 있습니다.

|필드 |설명 |
|-------|-------------|
|@timestamp |`yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> 로그된 이벤트의 시간입니다. <br> 시간소인은 밀리초 단위까지 정의됩니다. |
|@version |이벤트의 버전입니다. |
|ALCH_TENANT_ID |{{site.data.keyword.Bluemix_notm}} 영역의 ID입니다. |
|\_id |로그 문서에 대한 고유 ID입니다. |
|\_index |로그 항목에 대한 색인입니다. |
|\_type |로그의 유형입니다(예: *syslog*). |
|loglevel |로그된 이벤트의 심각도입니다(예: **정보**). |
|module |이 필드는 **MessageHub**로 설정됩니다. |
{: caption="표 4. {{site.data.keyword.messagehub}} 이벤트의 필드" caption-side="top"}

로그 항목의 예:

```
March 8th 2017, 17:15:16.454	

message:
    Creating topic ABC
@version:
    1
@timestamp:
    March 8th 2017, 17:15:16.454
loglevel:
    Info
module:
    MessageHub
ALCH_TENANT_ID:
    3d8d2eae-f3f0-44f6-9717-126113a00b51
&#95;id:
    AVqu6vJl1zcfr8KYMI95
&#95;type:
    logs
&#95;index:
    logstash-2017.03.08
```
{: screen}


