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


# 클러스터에 대한 영역 ID 검색
{: #containers_spaceid}

Cloud Foundry 조직 및 영역의 컨텍스트 내의 {{site.data.keyword.Bluemix_notm}} 계정에서 클러스터를 작성할 수 있습니다. 
{:shortdesc}

클러스터와 연관된 영역 ID를 찾으려면 다음 명령을 실행하십시오.

```
ibmcloud cs cluster-get ClusterName --json
```
{: codeblock}

여기서, **ClusterName**은 클러스터의 이름입니다.


예를 들어 이 명령 실행에 대한 출력은 다음과 같습니다.

```
{
    "id": "c213f81296db4c68b84e212c19135a99",
    "name": "MyDemoCluster",
    "region": "us-south",
    "dataCenter": "hou02",
    "location": "us-south-hou02",
    "serverURL": "https://xxx.xx.xx.xx:xxxxx",
    "state": "normal",
    "createdDate": "2017-09-26T09:00:59+0000",
    "modifiedDate": "2017-11-29T05:30:41+0000",
    "workerCount": 5,
    "isPaid": true,
    "masterKubeVersion": "1.7.4_1504",
    "targetVersion": "1.7.4_1504",
    "ingressHostname": "",
    "ingressSecretName": "",
    "logOrg": "5eab56t3-dty7-4utc-adaa-3aa5gn7r4g41",
    "logOrgName": "MyOrg",
    "logSpace": "fa277ff8-8a73-324b-9b75-0f11d54a3ae2",
    "logSpaceName": "MySpace",
    "addons": null,
    "vlans": null
}
```
{: screen}

영역 ID는 **logSpace** 필드에 대해 표시되는 값입니다.
영역 이름은 **logSpaceName** 필드에 대해 표시되는 값입니다.
조직 ID는 **logOrg** 필드에 대해 표시되는 값입니다.
조직 이름은 **logOrgName** 필드에 대해 표시되는 값입니다.

이러한 필드가 비어 있는 경우 해당 클러스터와 연관된 CF 조직 및 영역이 없습니다.



