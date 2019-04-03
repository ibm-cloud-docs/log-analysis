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


# Kibana FAQ
{: #faq_kibana}

{{site.data.keyword.Bluemix}} 로깅 기능 사용에 대한 일반적인 질문에 대한 답변입니다. {:shortdesc}

* [Kibana의 검색 페이지에서 데이터를 볼 수 없는 경우 처리 방법](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#logging_qa_no_data_discover_kibana)
* [인증 예외가 발생하는 경우 처리 방법](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#logging_qa_no_data_dashboard_kibana)
* [Kibana 검색 페이지에서 필드 옆에 ? 기호가 표시되는 이유](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#logging_qa_kibana_question)
* [기본 인덱스 패턴 변경 시 403 오류 표시](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#error_403)
* [단축 URL이 작동하지 않음](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#short_url)
* [Bluemix에서 내 계정 로그를 검색할 수 있습니까?](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#acc_logs_1)


## Kibana의 검색 페이지에서 데이터를 볼 수 없는 경우 처리 방법
{: #logging_qa_no_data_discover_kibana}

Kibana에서 데이터를 볼 수 없게 되는 다른 시나리오가 있습니다.

1. Kibana를 실행했을 때 검색 페이지에서 데이터를 전혀 볼 수 없습니다. **결과를 찾을 수 없음**이라는 메시지를 수신합니다. 
2. Kibana의 검색 페이지에서 작업할 수 있습니다. 그러나 Kibana에서 태스크를 수행하려고 할 때 잠시 후 **결과를 찾을 수 없음**이라는 메시지를 수신합니다.

이 문제를 해결하려면 다음 단계를 완료하십시오.

1. 검색 페이지에 설정된 *시간 선택도구*를 선택하고 기간을 늘리십시오. 

    **참고**: 기본적으로 {{site.data.keyword.Bluemix_notm}}에서 *시간 선택도구*는 최근 15분 동안의 데이터를 표시하도록 설정됩니다.

    *시간 선택도구* 설정 방법에 대한 자세한 정보는 [시간 필터 설정](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter1)을 참조하십시오.
       
2. *검색* 페이지 검색 표시줄에 있는 돋보기를 클릭하십시오. 페이지 데이터는 기본 검색 조회를 기반으로 새로 고쳐집니다.

    또는 *자동으로 새로 고치기* 기간을 설정할 수 있습니다.

    **참고**: 기본적으로 {{site.data.keyword.Bluemix_notm}}에서 *자동으로 새로 고치기* 기간은 **OFF**로 설정됩니다.
    
    사용 가능하게 설정하는 방법에 대한 자세한 정보는 [자동으로 데이터 새로 고치기](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_refresh_interval)를 참조하십시오.



## 인증 예외가 발생하는 경우 처리 방법
{: #logging_qa_no_data_dashboard_kibana}

대시보드 페이지에서 시각화에 표시되는 데이트를 볼 수 없으며 **오류: 권한 부여 예외** 오류 메시지를 수신하는 경우, 각 시각화에서 데이터를 볼 수 있도록 권한을 확인하십시오.

다음과 같은 정보를 고려하십시오.
대시보드 페이지에서 하나 이상의 시각화를 구성할 수 있습니다. 대시보드 페이지에서 해당 시각화를 통해 표시되는 데이터를 수집하는 요청을 하면 모든 시각화에 대해 하나의 요청만 발행됩니다. 시각화 중 하나에서 데이터를 볼 수 있는 권한이 없어도 전체 요청이 실패합니다.

이 문제를 해결하려면 다음 단계를 완료하십시오.

1. 사용자가 권한이 없는 시각화를 식별하십시오.

    1. *대시보드* 페이지에서 시각화의 *연필* 아이콘을 클릭하십시오. 시각화가 *시각화* 페이지에 열립니다. 또는 *시각화* 페이지에서 하나의 시각화를 로드하십시오. 
    2. 데이터를 볼 수 있는지 확인하십시오.
    
    각 시각화에 이러한 단계를 반복하십시오.

2. 클라우드 관리자에게 해당 시각화에서 데이터를 볼 수 있는 액세스 권한을 요청하십시오.

3. 문제점을 일으키는 시각화에서 데이터를 볼 수 있는 액세스 권한이 부여되는 동안에 권한이 없는 시각화를 제외한 새 대시보드 페이지를 작성하십시오. 

    대시보드를 공유하는 경우, 같은 대시보드를 사용하는 다른 팀 구성원들에게 영향이 있으므로 시각화를 삭제하지 마십시오.



## Kibana 검색 페이지에서 필드 옆에 ? 기호가 표시되는 이유
{: #logging_qa_kibana_question}

Kibana에서 검색 페이지를 열 때 사용 가능한 필드 섹션에 나열된 필드 옆에 문자 `t` 대신에 물음표 `?`가 표시될 수 있습니다. 필드의 목록을 다시 로드하면 필드의 유형이 분석되고 물음표 `?`가 `t`로 대체됩니다. 자세한 정보는[필드의 목록 다시 로드](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_reload_fields)를 참조하십시오.


## 기본 인덱스 패턴 변경 시 403 오류 표시
{: #error_403}

기본 인덱스 패턴을 변경할 수 없습니다. 

새 기본 인덱스 패턴으로 다른 인덱스 패턴을 설정하려는 경우 `구성: 오류 403 금지됨` 오류 메시지가 표시됩니다.

## 단축 URL이 작동하지 않음
{: #short_url}

검색, 시각화 또는 대시보드 공유가 지원되지 않습니다. 따라서 공유하려는 Kibana 오브젝트에 대한 단축 URL이 작동하지 않습니다. 

## Bluemix에서 내 계정 로그를 검색할 수 있습니까?
{: #acc_logs_1}

계정 소유자로서 계정 로그를 검색하고 분석할 수 있습니다.

계정 로그를 보려면 다음 단계를 완료하십시오.

1. [Kibana를 실행](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser)하십시오. 예를 들어 미국 남부 지역의 경우 `https://logging.ng.bluemix.net` URL을 사용하십시오,

2. **AccountName 계정 로그 보기** 옵션을 선택하여 계정 로그를 표시하십시오. *AccountName*은 계정의 이름입니다.

