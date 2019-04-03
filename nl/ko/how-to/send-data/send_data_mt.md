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

# IBM Cloud의 영역에 온프레미스 데이터 전송
{: #send_data_mt}

{{site.data.keyword.loganalysisshort}} 서비스로 로그 데이터를 전송하도록 다중 테넌트 Logstash 포워더(mt-logstash-forwarder)를 구성할 수 있습니다. 
{: shortdesc}

로그 데이터를 {{site.data.keyword.Bluemix_notm}}의 영역으로 보내려면 다음 단계를 완료하십시오.

## 전제조건
{: #prereqs1}

* {{site.data.keyword.Bluemix_notm}}에 로그인할 {{site.data.keyword.Bluemix_notm}} ID.
* 영역에서 {{site.data.keyword.loganalysisshort}} 서비스에 대한 작업을 수행할 수 있는 권한이 있는 사용자 ID. 자세한 정보는 [보안](/docs/services/CloudLogAnalysis/security_ov.html#security_ov)을 참조하십시오.
* 로컬 환경에 설치된 {{site.data.keyword.loganalysisshort}} CLI.
* 로그 수집을 허용하는 플랜과 함께 계정의 영역에 프로비저닝된 {{site.data.keyword.loganalysisshort}} 서비스.


## 1단계: 로깅 토큰 가져오기
{: #get_logging_auth_token}

{{site.data.keyword.loganalysisshort}} CLI가 설치된 터미널 세션에서 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
    
2. `ibmcloud logging token-get` 명령을 실행하십시오. 

    ```
    ibmcloud logging token-get
    ```
    {: codeblock}

    명령은 로깅 토큰을 리턴합니다.
    
    예:

    ```
    ibmcloud logging token-get
    Getting log token of resource: 93f54jh6-b5f5-46c9-9f0e-kfeutpldnbcf ...
    OK

    Tenant Id                              Logging Token   
    93f54jh6-b5f5-46c9-9f0e-kfeutpldnbcf   oT98_abcdefz   
    ```
    {: screen}

    여기서 *Tenant Id*는 로그를 전송할 계획인 영역의 GUID입니다.


## 2단계: mt-logstash-forwarder 구성
{: #configure_mt_logstash_forwarder}

{{site.data.keyword.loganalysisshort}} 서비스에 로그를 전송할 계획인 환경에서 mt-logstash-forwarder를 구성하려면 다음 단계를 완료하십시오.

1.	루트 사용자로 로그인하십시오. 

    ```
    sudo -s
    ```
    {: codeblock}
    
2.	로그의 시간을 동기화하려면 NTP(Network Time Protocol) 패키지를 설치하십시오. 

    예를 들어, Ubunutu 시스템의 경우 `timedatectl status`에 *Network time on: yes*가 표시되는지 확인하십시오. 표시가 되면 Ubuntu 시스템이 이미 ntp를 사용하도록 구성되어 있어서 이 단계를 건너뛸 수 있습니다.
    
    ```
    # timedatectl status
    Local time: Mon 2017-06-12 03:01:22 PDT
    Universal time: Mon 2017-06-12 10:01:22 UTC
    RTC time: Mon 2017-06-12 10:01:22
    Time zone: America/Los_Angeles (PDT, -0700)
    Network time on: yes
    NTP synchronized: yes
    RTC in local TZ: no
    ```
    {: screen}
    
    Ubuntu 시스템에서 ntp를 설치하려면 다음 단계를 완료하십시오.

    1.	다음 명령을 실행하여 패키지를 업데이트하십시오. 

        ```
        apt-get update
        ```
        {: codeblock}
        
    2.	다음 명령을 실행하여 ntp 패키지를 설치하십시오. 

        ```
        apt-get install ntp
        ```
        {: codeblock}
        
    3.	다음 명령을 실행하여 ntpdate 패키지를 설치하십시오. 
    
        ```
        apt-get install ntpdate
        ```
        {: codeblock}
        
    4.	다음 명령을 실행하여 서비스를 중지하십시오. 
        
        ```
        service ntp stop
        ```
        {: codeblock}
        
    5.	다음 명령을 실행하여 시스템 시계를 동기화하십시오. 
    
        ```
        ntpdate -u 0.ubuntu.pool.ntp.org
        ```
        {: codeblock}
        
        결과를 통해 시간이 조정되었음을 확인합니다. 예:
        
        ```
        4 May 19:02:17 ntpdate[5732]: adjust time server 50.116.55.65 offset 0.000685 sec
        ```
        {: screen}
        
    6.	다음 명령을 실행하여 ntpd를 다시 시작하십시오. 
    
        ```
        service ntp start
        ```
        {: codeblock}
    
        결과를 통해 서비스가 시작 중임을 확인합니다.

    7.	다음 명령을 실행하여 충돌 또는 다시 부팅 후 자동으로 시작하도록 ntpd 서비스를 사용으로 설정하십시오. 
    
        ```
        service ntp enable
        ```
        {: codeblock}
        
        표시되는 결과는 ntpd 서비스 관리에 사용할 수 있는 명령의 목록입니다. 예:
        
        ```
        Usage: /etc/init.d/ntpd {start|stop|status|restart|try-restart|force-reload}
        ```
        {: screen}

3. 시스템의 패키지 관리자에서 {{site.data.keyword.loganalysisshort}} 서비스에 대한 저장소를 추가하십시오. 다음 명령을 실행하십시오.

    ```
    wget -O - https://downloads.opvis.bluemix.net/client/IBM_Logmet_repo_install.sh | bash
    ```
    {: codeblock}

4. 사용자의 환경에서 로그를 로그 콜렉션으로 전송하려면 mt-logstash-forwarder를 설치하고 구성하십시오. 

    1. mt-logstash-forwarder를 설치하려면 다음 명령을 실행하십시오.
    
        ```
        apt-get install mt-logstash-forwarder 
        ```
        {: codeblock}
        
    2. 사용자의 환경에 대한 mt-logstash-forwarder 구성 파일을 작성하십시오. 이 파일에는 포워더가 {{site.data.keyword.loganalysisshort}} 서비스를 가리키도록 mt logstash forwarder를 구성하는 데 사용되는 변수가 포함되어 있습니다.
    
       `/etc/mt-logstash-forwarder/mt-lsf-config.sh` 파일을 편집하십시오. 예를 들면, vi 편집기를 사용할 수 있습니다.
               
       ```
       vi /etc/mt-logstash-forwarder/mt-lsf-config.sh
       ```
       {: codeblock}
        
       포워더가 {{site.data.keyword.loganalysisshort}} 서비스를 가리키도록 다음 변수를 **mt-lsf-config.sh** 파일에 추가하십시오. 
         
       <table>
          <caption>표 1. VM에서 포워더가 {{site.data.keyword.loganalysisshort}} 서비스를 가리키도록 하는 데 필요한 변수의 목록 </caption>
          <tr>
            <th>변수 이름</th>
            <th>설명</th>
          </tr>
          <tr>
            <td>LSF_INSTANCE_ID</td>
            <td>VM에 대한 ID입니다. 예: *MyTestVM*. </td>
          </tr>
          <tr>
            <td>LSF_TARGET</td>
            <td>대상 URL입니다. 수집 URL 목록을 가져오려면 [수집 URL](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls)을 참조하십시오. 예를 들어 미국 남부 지역의 로그를 보내려면 값을 **ingest.logging.ng.bluemix.net:9091**로 설정하십시오. </td>
          </tr>
          <tr>
            <td>LSF_TENANT_ID</td>
            <td>{{site.data.keyword.loganalysisshort}} 서비스가 {{site.data.keyword.Bluemix_notm}}로 전송하는 로그를 수집할 준비가 되어 있는 영역 ID입니다. <br>1단계에서 얻은 값을 사용하십시오.</td>
          </tr>
          <tr>
            <td>LSF_PASSWORD</td>
            <td>로깅 토큰입니다. <br>1단계에서 얻은 값을 사용하십시오.</td>
          </tr>
          <tr>
            <td>LSF_GROUP_ID</td>
            <td>관련 로그를 그룹화하기 위해 정의할 수 있는 사용자 정의 태그에 이 값을 설정하십시오.</td>
          </tr>
       </table>
        
       예를 들면, 영국 지역에서 ID *7d576e3b-170b-4fc2-a6c6-b7166fd57912*가 있는 영역에 대한 다음 샘플 파일을 보십시오.
        
       ```
       # more mt-lsf-config.sh 
       LSF_INSTANCE_ID="myhelloapp"
       LSF_TARGET="ingest.logging.ng.bluemix.net:9091"
       LSF_TENANT_ID="7d576e3b-170b-4fc2-a6c6-b7166fd57912"
       LSF_PASSWORD="oT98_abcdefz"
       LSF_GROUP_ID="Group1"
       ```
       {: screen}
        
    3. mt-logstash-forwarder를 시작하십시오. 
    
       ```
       service mt-logstash-forwarder start
       ```
       {: codeblock}
                
기본적으로 포워더는 syslog만 감시합니다. 사용자의 로그는 Kibana에서 분석용으로만 사용 가능합니다.
        

## 3단계: 추가 로그 파일 지정
{: #add_logs}

기본적으로 /var/log/syslog 파일만 포워더에서 모니터합니다. 포워더가 모니터하도록 `/etc/mt-logstash-forwarder/conf.d/syslog.conf/` 디렉토리에 구성 파일을 더 추가할 수 있습니다. 

사용자의 환경에서 실행되는 앱에 대한 구성 파일을 추가하려면 다음 단계를 완료하십시오.

1.	`/etc/mt-logstash-forwarder/conf.d/syslog.conf` 파일을 복사하십시오. 

    **팁:** 로그 파일을 추가하기 위해 syslog.conf 파일을 편집하지 마십시오.
    
    예를 들어, Ubuntu 시스템에서는 다음 명령을 실행하십시오.
    
    ```
    cp /etc/mt-logstash-forwarder/conf.d/syslog.conf /etc/mt-logstash-forwarder/conf.d/myapp.conf
    ```
    {: codeblock}
        
2.	텍스트 편집기를 사용하여 *myapp.conf* 파일을 편집하고 모니터하려는 애플리케이션 로그를 포함하도록 파일을 업데이트하십시오. 각 앱 로그에 대한 로그 유형을 포함하십시오. 사용되지 않는 예는 삭제하십시오.

3.	mt-logstash-forwarder를 다시 시작하십시오. 

     mt-logstash-forwarder 서비스를 다시 시작하십시오. 다음 명령을 실행하십시오.
    
    ```
    service mt-logstash-forwarder restart
    ```
    {: codeblock}

**예**

hello 앱에서 stdout 또는 stderr을 포함하도록 stdout 또는 stderr을 로그 파일로 경로 재지정하십시오. 앱에 대한 포워더 구성 파일을 작성하십시오. 그런 다음에 mt-logstash-forwarder를 다시 시작하십시오.

1.	`/etc/mt-logstash-forwarder/conf.d/syslog.conf` 파일을 복사하십시오. 

    ```
    cp /etc/mt-logstash-forwarder/conf.d/syslog.conf /etc/mt-logstash-forwarder/conf.d/myapp.conf
    ```
    {: codeblock}
    
2. 구성 파일 *myapp.conf*를 편집하십시오.

    로그를 수집할 때 Kibana에서 JSON 필드를 사용하여 검색할 수 있도록 하려면 JSON 구문 분석을 사용으로 설정하십시오. 특정 파일 경로의 구성 파일에서 `is_json`을 true로 설정하십시오. 이 방식으로 구성된 로그 파일의 경우 로그 행이 캐리지 리턴으로 구분된 JSON 블록으로 형식화되어야 합니다. 그러면 mt-logstash-forwarder가 이러한 모든 JSON 필드를 각각의 Kibana 검색 가능 필드로 사용합니다. JSON 필드 이름에는 유형을 기반으로 한 접미부가 포함됩니다.
    
    ```
    {
    "files": [
         # other file configurations omitted...
            {
            "paths": [ "/var/log/myhelloapp.log" ],
            "fields": { "type": "helloapplog" },
            "is_json": true
            }
         ]
     }
     ```
     {: screen}
