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

# Kibana 리소스를 다시 사용하여 {{site.data.keyword.Bluemix_notm}} 로그 분석
{:#k4_reuse_resource}

검색, 시각화 또는 대시보드를 한 {{site.data.keyword.Bluemix}} 영역에서 다른 영역으로 복사하려면 Kibana에서 사용할 수 있는 내보내기 및 가져오기 기능을 사용하십시오. Kibana에서 리소스를 개별적으로 복사하거나 모든 리소스를 내보낼 수 있습니다.
{:shortdesc}

|태스크 |설명 |
|------|-------------|
|[검색 복사](/docs/services/CloudLogAnalysis/kibana4/k4_reuse_resource.html#k4_reuse_search) |영역 간에 검색 복사 |
|[시각화 복사](/docs/services/CloudLogAnalysis/kibana4/k4_reuse_resource.html#k4_reuse_visualization) |영역 간에 시각화 복사 |

검색, 시각화 또는 대시보드 재사용에 대해서는 {{site.data.keyword.Bluemix_notm}}에서 다음 시나리오를 고려하십시오. 

* 동일한 조직의 영역 간에 리소스를 복사하십시오.

    예를 들어 시각화를 개발 영역에서 스테이징 영역으로 복사하려고 할 수 있습니다.
    
* 동일한 계정에서 다른 조직의 영역 간에 리소스를 복사하십시오.

    예를 들어 시각화를 개발 조직의 영역에서 스테이징 조직의 영역으로 복사하려고 할 수 있습니다.

* 동일한 조직이지만 다른 공용 지역에 있는 영역 간에 리소스를 복사하십시오.

    예를 들어 시각화를 공용 지역 미국 남부에 있는 {{site.data.keyword.Bluemix_notm}} 조직 A의 영역에서 공용 지역 영국에 있는 조직 A의 영역으로 복사하려고 할 수 있습니다.



## 검색 복사
{:#k4_reuse_search}

{{site.data.keyword.Bluemix_notm}}의 영역 간에 검색을 복사하려면 다음 단계를 완료하십시오.

1. 복사하려는 검색을 사용할 수 있는 Kibana를 실행하십시오. 

    * {{site.data.keyword.Bluemix_notm}} UI에서 Kibana를 실행하십시오. 내보낼 수 있는 JSON 검색 파일에는 다음 필드가 포함되어 있습니다. *영역 ID* 및 CF(Cloud Foundry)의 *애플리케이션 ID* 또는 컨테이너의 *인스턴스 ID*. 자세한 정보는 [{{site.data.keyword.Bluemix_notm}} 대시보드에서 Kibana 대시보드로 이동](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-k4_launch#launch_Kibana_from_bluemix)을 참조하십시오.
    
    * 브라우저에서 Kibana를 실행하십시오. 내보낼 수 있는 JSON 검색 파일에는 *영역 ID* 필드가 포함되어 있습니다. 자세한 정보는 [브라우저에서 Kibana 대시보드로 이동](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-k4_launch#launch_Kibana_from_browser1)을 참조하십시오.

2. *설정* 페이지에서 **오브젝트** 및 **검색** 탭을 선택하십시오. 그런 다음 검색을 선택하고 다음 정보를 복사하십시오.

    <table>
      <tbody>
        <tr>
          <th align="center">검색 필드</th>
          <th align="center">설명</th>
        </tr>
        <tr>
          <td align="left">그룹</td>
          <td align="left"> 데이터를 필터링하기 위해 검색이 적용되는 영역 ID입니다.</td>
        </tr>
        <tr>
          <td align="left">제목</td>
          <td align="left">검색의 이름입니다.</td>
        </tr>
        <tr>
          <td align="left">버전</td>
          <td align="left">검색의 버전입니다.</td>
        </tr>
      </tbody>
    </table>
   
3. 검색을 내보내십시오.

    1. 설정 페이지에서 **오브젝트** 탭을 선택하십시오.
    2. **검색** 탭에서 내보내려는 검색을 선택하십시오.
    3. **내보내기**를 클릭하십시오.
    4. JSON 파일을 저장하십시오.

4. {{site.data.keyword.Bluemix_notm}} UI에서 검색을 복사할 대상 영역으로 이동한 후 CF 애플리케이션 또는 컨테이너가 사용 가능하고 실행 중인지 확인하십시오.
    
5. 검색을 가져오려는 {{site.data.keyword.Bluemix_notm}} 영역의 Kibana를 실행한 후 다음 정보를 가져오십시오.

    [Bluemix UI](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-k4_launch#launch_Kibana_from_bluemix)에서 다음을 가져오십시오.
    
    <table>
      <tbody>
        <tr>
          <th align="center">검색 필드</th>
          <th align="center">설명</th>
        </tr>
        <tr>
          <td align="left">영역 ID</td>
          <td align="left"> <ol><li> *설정* 페이지에서 *인덱스* 탭을 선택하십시오.</li> <br> <li>영역 ID는 인덱스 패턴에 임베드되어 있습니다. 색인 패턴의 형식은 다음과 같습니다. `[logstash-3d8d2eae-SpaceID-]YYYY.MM.DD` 여기서, *SpaceID*는 영역의 ID입니다. 영역 ID를 복사하십시오.</li></ol></td>
        </tr>
        <tr>
          <td align="left">애플리케이션 ID 또는 인스턴스 ID</td>
          <td align="left"><ul><li>{{site.data.keyword.Bluemix_notm}} UI에서 Kibana를 실행하면 기본적으로 *검색* 페이지가 열립니다. *검색* 페이지의 검색줄에서 애플리케이션 ID 또는 인스턴스 ID를 가져오십시오. 예: `application_id:d88d1f16-e9d9-4623-bce7-0348c88f5133`.</li> <br> <li>브라우저에서 Kibana를 실행하는 경우 검색 페이지의 필드 목록에서 필드 application_id 또는 instance_id를 선택하십시오.</li></ul></td>
        </tr>
      </tbody>
    </table>

6. 이전 단계에서 내보낸 검색 JSON 검색 파일을 수정하십시오. 애플리케이션 ID 값을 바꾸십시오. 

    예를 들어 다음 JSON은 검색 JSON 파일의 예입니다. 
 
    <pre class="pre">
    [
  {
    "_id": "52edf6e6-5386-4235-8fb8-598de3b80f41_Dev",
    "_type": "search",
    "_source": {
      "columns": [
        "application_id",
        "source_id",
        "instance_id"
      ],
      "description": "",
      "group": "52edf6e6-5386-4235-8fb8-598de3b80f41",
      "hits": 0,
      "kibanaSavedObjectMeta": {
        "searchSourceJSON": "{\"index\":\"[logstash-52edf6e6-5386-4235-8fb8-598de3b80f41-]YYYY.MM.DD\",\"query\":{\"query_string\":{\"analyze_wildcard\":true,\"query\":\"application_id:4ae73dcd-1fc4-48f0-9dc7-425839040436\"}},\"highlight\":{\"pre_tags\":[\"@kibana-highlighted-field@\"],\"post_tags\":[\"@/kibana-highlighted-field@\"],\"fields\":{\"*\":{}},\"fragment_size\":2147483647},\"filter\":[{\"meta\":{\"negate\":false,\"index\":\"[logstash-52edf6e6-5386-4235-8fb8-598de3b80f41-]YYYY.MM.DD\",\"key\":\"application_id\",\"value\":\"4ae73dcd-1fc4-48f0-9dc7-425839040436\",\"disabled\":false},\"query\":{\"match\":{\"application_id\":{\"query\":\"4ae73dcd-1fc4-48f0-9dc7-425839040436\",\"type\":\"phrase\"}}}}]}"
      },
      "sort": [
        "@timestamp",
        "desc"
      ],
      "title": "Dev",
      "version": 1
    }
  }
]
    </pre>
    
    이 샘플 JSON 파일에서 새 영역의 정보로 다음 변수를 수정할 수 있습니다. 
    
    * SPACEID: 이 변수를 새 영역의 영역 ID로 바꾸십시오.
    * NAME: 새 영역에서 검색 이름을 변경하려는 경우 이 변수를 바꾸십시오. 동일한 이름을 유지하려면 이 값을 변경하지 마십시오.
    * APPID: 이 변수를 새 영역에 있는 CF 앱의 application_id 값 또는 새 영역에 있는 컨테이너의 인스턴스 ID로 바꾸십시오.
    
   <pre class="pre">
   [
  {
    "_id": "SPACEID_NAME",
    "_type": "search",
    "_source": {
      "columns": [
        "application_id",
        "source_id",
        "instance_id"
      ],
      "description": "",
      "group": "SPACEID",
      "hits": 0,
      "kibanaSavedObjectMeta": {
        "searchSourceJSON": "{\"index\":\"[logstash-SPACEID-]YYYY.MM.DD\",\"query\":{\"query_string\":{\"analyze_wildcard\":true,\"query\":\"application_id:APPID\"}},\"highlight\":{\"pre_tags\":[\"@kibana-highlighted-field@\"],\"post_tags\":[\"@/kibana-highlighted-field@\"],\"fields\":{\"*\":{}},\"fragment_size\":2147483647},\"filter\":[{\"meta\":{\"negate\":false,\"index\":\"[logstash-SPACEID-]YYYY.MM.DD\",\"key\":\"application_id\",\"value\":\"APPID\",\"disabled\":false},\"query\":{\"match\":{\"application_id\":{\"query\":\"APPID\",\"type\":\"phrase\"}}}}]}"
      },
      "sort": [
        "@timestamp",
        "desc"
      ],
      "title": "Dev",
      "version": 1
    }
  }
]
    </pre>

6. 검색 JSON 파일을 새 영역의 Kibana로 가져오십시오.

    1. 설정 페이지에서 **오브젝트** 탭을 선택하십시오.
    2. **검색** 탭에서 가져오려는 검색 JSON 파일을 선택하십시오.
    3. **가져오기**를 클릭하십시오.

Kibana에서 검색을 사용하여 새 영역의 애플리케이션에 사용할 수 있는 데이터를 모니터할 수 있습니다.


    
## 시각화 복사
{:#k4_reuse_visualization}

영역의 애플리케이션 데이터를 분석하는 데 사용하는 시각화를 다른 영역으로 복사하려면 다음 단계를 완료하십시오.

1. 복사하려는 시각화를 사용할 수 있는 영역의 Kibana를 실행하십시오. 

    * {{site.data.keyword.Bluemix_notm}} UI에서 Kibana를 실행하십시오. 내보낼 수 있는 JSON 검색 파일에는 다음 필드가 포함되어 있습니다. *영역 ID* 및 CF(Cloud Foundry)의 *애플리케이션 ID* 또는 컨테이너의 *인스턴스 ID*. 자세한 정보는 [{{site.data.keyword.Bluemix_notm}} 대시보드에서 Kibana 대시보드로 이동](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-k4_launch#launch_Kibana_from_bluemix)을 참조하십시오.
    
    * 브라우저에서 Kibana를 실행하십시오. 내보낼 수 있는 JSON 검색 파일에는 *영역 ID* 필드가 포함되어 있습니다. 자세한 정보는 [브라우저에서 Kibana 대시보드로 이동](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-k4_launch#launch_Kibana_from_browser1)을 참조하십시오.
    
2. 시각화와 연관된 검색을 영역 간에 복사하십시오. 자세한 정보는 [Bluemix 영역 간에 검색 복사](/docs/services/CloudLogAnalysis/kibana4/k4_reuse_resource.html#k4_reuse_search)를 참조하십시오.

    시각화는 검색을 사용하여 표시되는 데이터를 필터링합니다. 시각화가 검색에 연결된 경우 검색에 대한 모든 업데이트가 자동으로 업데이트되며 검색에 연결되지 않은 경우 분석에 사용 가능한 데이터는 시각화 작성 시 표시되는 데이터입니다.

    시각화를 복사하는 경우 검색에 대한 연결 상태와 상관없이 시각화와 연관된 검색도 복사해야 합니다. **참고:** 시각화를 새 영역으로 가져오면 새 시각화가 새 영역의 검색에 연결됩니다.
    
3. *설정* 페이지에서 **오브젝트** 및 **시각화** 탭을 선택하십시오. 그런 다음 시각화를 선택하고 다음 정보를 가져오십시오. 

    <table>
      <tbody>
        <tr>
          <th align="center">시각화 필드</th>
          <th align="center">설명</th>
        </tr>
        <tr>
          <td align="left">그룹</td>
          <td align="left"> 시각화를 사용하여 데이터를 분석하는 영역 ID 값입니다.</td>
        </tr>
        <tr>
          <td align="left">제목</td>
          <td align="left">시각화의 이름입니다.</td>
        </tr>
        <tr>
          <td align="left">버전</td>
          <td align="left">시각화의 버전입니다.</td>
        </tr>
        <tr>
          <td align="left">savedSearchID</td>
          <td align="left">시각화를 통해 표시되는 데이터를 필터링하는 데 사용되는 검색 ID입니다. <br> 이 값의 형식은 다음과 같습니다. `SpaceID_SearchTitle` 여기서 SearchTitle은 검색의 *제목* 필드 값입니다. </td>
        </tr>
      </tbody>
    </table>
   

4. 시각화를 내보내십시오.

    1. 설정 페이지에서 **오브젝트** 탭을 선택하십시오.
    2. **시각화** 탭에서 내보내려는 시각화를 선택하십시오.
    3. **내보내기**를 클릭하십시오.
    4. JSON 파일을 저장하십시오.
    
5. {{site.data.keyword.Bluemix_notm}} UI에서 시각화를 복사할 대상 영역으로 이동한 후 CF 애플리케이션 또는 컨테이너가 사용 가능하고 실행 중인지 확인하십시오.
    
6.  이전 단계에서 내보낸 검색 JSON 시각화 파일을 수정하십시오. 영역 ID 및 검색 ID 값을 바꾸십시오. 

    예를 들어 다음 JSON은 시각화 JSON 파일의 예입니다. 

    <pre class="pre">
    [
  {
    "_id": "3d8d2eae-f3f0-44f6-9717-126113a00b51_test",
    "_type": "visualization",
    "_source": {
      "description": "",
      "group": "3d8d2eae-f3f0-44f6-9717-126113a00b51",
      "kibanaSavedObjectMeta": {
        "searchSourceJSON": "{\"filter\":[]}"
      },
      "savedSearchId": "3d8d2eae-f3f0-44f6-9717-126113a00b51_Default_9d222152-8834-4bab-8685-3036cd25931a",
      "title": "test",
      "version": 1,
      "visState": "{\"type\":\"line\",\"params\":{\"shareYAxis\":true,\"addTooltip\":true,\"addLegend\":true,\"showCircles\":true,\"smoothLines\":false,\"interpolate\":\"linear\",\"scale\":\"linear\",\"drawLinesBetweenPoints\":true,\"radiusRatio\":9,\"times\":[],\"addTimeMarker\":false,\"defaultYExtents\":false,\"setYExtents\":false,\"yAxis\":{}},\"aggs\":[{\"id\":\"1\",\"type\":\"count\",\"schema\":\"metric\",\"params\":{}}],\"listeners\":{}}"
    }
    }
    ]
    </pre>
    
    이 샘플 JSON 파일에서 다음 변수를 수정할 수 있습니다. 
    
    * SPACEID: 이 변수를 새 영역의 영역 ID로 바꾸십시오.
    * NAME: 새 영역에서 시각화 이름을 변경하려는 경우 이 변수를 바꾸십시오.
    * SEARCHID: 이 변수를 새 영역의 검색 ID로 바꾸십시오. 이는 시각화를 통해 표시되는 데이터를 필터링하는 데 사용되는 조회 ID입니다.
    
       <pre class="pre">
    [
  {
    "_id": "SPACEID_NAME",
    "_type": "visualization",
    "_source": {
      "description": "",
      "group": "SPACEID",
      "kibanaSavedObjectMeta": {
        "searchSourceJSON": "{\"filter\":[]}"
      },
      "savedSearchId": "SPACEID_SEARCHID",
      "title": "NAME",
      "version": 1,
      "visState": "{\"type\":\"line\",\"params\":{\"shareYAxis\":true,\"addTooltip\":true,\"addLegend\":true,\"showCircles\":true,\"smoothLines\":false,\"interpolate\":\"linear\",\"scale\":\"linear\",\"drawLinesBetweenPoints\":true,\"radiusRatio\":9,\"times\":[],\"addTimeMarker\":false,\"defaultYExtents\":false,\"setYExtents\":false,\"yAxis\":{}},\"aggs\":[{\"id\":\"1\",\"type\":\"count\",\"schema\":\"metric\",\"params\":{}}],\"listeners\":{}}"
    }
    }
    ]
    </pre>

8. 시각화를 가져오십시오.

    1. 설정 페이지에서 **오브젝트** 탭을 선택하십시오.
    2. **시각화** 탭에서 가져오려는 시각화 JSON 파일을 선택하십시오.
    3. **가져오기**를 클릭하십시오.


Kibana에서 시각화를 사용하여 새 영역의 애플리케이션에 사용할 수 있는 데이터를 모니터할 수 있습니다.
    
