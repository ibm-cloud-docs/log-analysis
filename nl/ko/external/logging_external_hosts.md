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


# 외부 로그 호스트 구성
{: #thirdparty_logging}

{{site.data.keyword.Bluemix_notm}}는 메모리에 제한된 양의 로그 정보를 보관합니다. 정보가 로그되면 이전 정보는 새 정보로 대체됩니다. 모든 로그 정보를 보관하기 위해 Cloud Foundry 애플리케이션 로그를 외부 로그 호스트(예: 서드파티 로그 관리 서비스 또는 다른 호스트)에 저장할 수 있습니다.
{:shortdesc}

외부 로그 호스트에 CF 앱 및 시스템의 로그를 스트림하려면 다음 단계를 완료하십시오.

  1. 로깅 엔드포인트를 판별하십시오.

	 Papertrail, Splunk 또는 Sumologic과 같은 서드파티 로그 집계기에 로그를 전송할 수 있습니다. 또한 syslog 호스트, TLS(Transport Layer Security)로 암호화된 syslog 호스트 또는 HTTPS POST 엔드포인트에 로그를 전송할 수 있습니다. 로깅 엔드포인트를 얻기 위한 방법은 여러 가지 로그 호스트에 따라 다릅니다.

  2. 사용자 제공 서비스 인스턴스를 작성하십시오.

	 사용자 제공 서비스 인스턴스를 작성하려면 `cf create-user-provided-service` 명령(또는 명령의 짧은 버전인 `cups`)을 사용하십시오.
	 
	 ```
	 cf create-user-provided-service <service_name> -l <logging_endpoint>
	 ```
	 {: codeblock}
	 
	 &lt;service_name&gt;

	 사용자 제공 서비스 인스턴스의 이름입니다.

	 &lt;logging_endpoint&gt;

	 {{site.data.keyword.Bluemix_notm}}에서 로그를 전송하는 로깅 엔드포인트입니다. *logging_endpoint*를 사용자의 값으로 바꾸려면 다음 표를 참조하십시오.

	 <table>
	 <caption>표 1. 로깅 엔드포인트 값</caption>
     <thead>
     <tr>
     <th>로깅 엔드포인트</th>
     <th>명령</th>
	 <th>참고</th>
     </tr>
     </thead>
     <tbody>
     <tr>
     <td>syslog 호스트</td>
     <td>`cf cups my-logs -l syslog://HOST:PORT`</td>
	 <td>예를 들어, Papertrail에 로깅을 사용하려면 `cf cups my-logs -l syslog://<papertrail-url>`을 입력하십시오. `<papertrail-url>`을 Papertrail에서 로깅 엔드포인트의 URL로 바꾸십시오.</td>
     </tr>
	 <tr>
     <td>syslog-tls 호스트</td>
     <td>`cf cups my-logs -l syslog-tls://HOST:PORT`</td>
	 <td>인증서는 인증 기관에서 신뢰해야 합니다. 자체 서명 인증서를 사용하지 마십시오.</td>
     </tr>
	 <tr>
     <td>HTTPS POST</td>
     <td>`cf cups my-logs -l https://HOST:PORT`</td>
	 <td>이 엔드포인트는 공용 인터넷에 있어야 하며 {{site.data.keyword.Bluemix_notm}}에서 액세스할 수 있어야 합니다.</td>
     </tr>
     </tbody>
     </table>
  3. 서비스 인스턴스를 앱에 바인드하십시오.

	 다음 명령을 사용하여 서비스 인스턴스를 앱에 바인드하십시오.

	 ```
	 cf bind-service <appname> <service_name>
	 ```
	 {: codeblock}
	 
	 &lt;appname&gt;

	 앱의 이름입니다.

	 &lt;service_name&gt;

	 사용자 제공 서비스 인스턴스의 이름입니다.

  4. 앱을 다시 스테이징하십시오.
     변경사항을 적용하려면 `cf restage appname`을 입력하십시오.

