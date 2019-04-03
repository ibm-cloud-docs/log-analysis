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


# 클러스터의 키 소유자 검색
{: #containers_key_owner}

클러스터의 {{site.data.keyword.loganalysisshort}} 키 소유자를 가져오려면 *ibmcloud cs api-key-info* 명령을 사용하십시오.
{:shortdesc}

다음 명령을 실행하십시오.

```
 ibmcloud cs api-key-info ClusterName
```
{: codeblock}

여기서, **ClusterName**은 클러스터의 이름입니다.


예를 들어 이 명령 실행에 대한 출력은 다음과 같습니다.

```
ibmcloud cs api-key-info MyDemoCluster
Getting information about the API key owner for cluster MyDemoCluster...
OK
Name           Email   
Joe Blogg      blogg@ibm.com   
```
{: screen}

영역 ID는 **logSpace** 필드에 대해 표시되는 값입니다.
영역 이름은 **logSpaceName** 필드에 대해 표시되는 값입니다.
조직 ID는 **logOrg** 필드에 대해 표시되는 값입니다.
조직 이름은 **logOrgName** 필드에 대해 표시되는 값입니다.

이러한 필드가 비어 있는 경우 해당 클러스터와 연관된 CF 조직 및 영역이 없습니다.



