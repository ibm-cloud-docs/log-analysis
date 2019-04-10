---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, config agent

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

# LogDNA 에이전트 구성
{: #config_agent}

LogDNA 에이전트는 로그를 수집하고 {{site.data.keyword.la_full_notm}} 인스턴스로 로그를 전달합니다. {{site.data.keyword.la_full}}의 인스턴스를 프로비저닝한 후 모니터할 각 로그 소스에 대해 LogDNA 에이전트를 구성해야 합니다.
{:shortdesc}

* LogDNA 에이전트는 LogDNA 수집 키를 사용하여 인증하고 {{site.data.keyword.la_full_notm}} 수집 서버에 보안 웹 소켓을 엽니다. 
* 기본적으로 에이전트는 확장자가 *.log*인 모든 파일과 */var/log/* 아래에 있는 확장자 없는 파일을 모니터합니다.
* 에이전트는 새 로그 데이터를 추적하고, 에이전트가 모니터하는 로깅 디렉토리에 추가된 새 파일을 찾습니다.

LogDNA 에이전트를 통해 다음 매개변수를 구성할 수 있습니다. 

|매개변수 |설명 |
|-----------|-------------|
| `tags`    | 호스트를 자동으로 동적 그룹으로 그룹화하도록 태그를 정의합니다. |
| `logdir`  | 에이전트가 모니터할 사용자 정의 경로를 정의합니다. </br>쉼표를 사용하여 여러 경로를 구분하십시오. 글로브 패턴을 사용할 수 있습니다. 특정 파일을 구성할 수 있습니다. 큰따옴표를 사용하여 글로브 패턴을 입력하십시오. |
| `exclude` | LogDNA 에이전트가 모니터하지 않을 파일을 정의합니다. **참고:** 이러한 파일은 logdir 매개변수를 통해 정의된 경로에 있을 수 있습니다. </br>쉼표를 사용하여 여러 파일을 구분합니다. 글로브 패턴을 사용할 수 있습니다. 특정 파일을 구성할 수 있습니다. |
| `exclude_regex` | 패턴과 일치하는 행을 필터링하기 위해 regex 패턴을 정의합니다. 선행 및 후행 `/`를 포함하지 않습니다. |
| `hostname` | 호스트 이름을 정의합니다. 이 값은 운영 체제 호스트 이름을 대체합니다. |
| `autoupdate` | 공용 저장소 에이전트 정의가 업데이트된 후 자동으로 에이전트를 업데이트하려면 `1`로 설정합니다. 이 기능을 사용하지 않으려면 `0`으로 설정합니다. |  
{: caption="표 1. LogDNA 에이전트를 사용자 정의하기 위한 매개변수" caption-side="top"} 



## 스크립트를 사용하여 Kubernetes 클러스터에서 LogDNA 에이전트 구성
{: #config_agent_kube_script}

{{site.data.keyword.la_full_notm}} 인스턴스로 로그를 보내도록 Kubernetes 클러스터를 구성하려면 클러스터의 각 노드에 *logdna-agent* 팟(Pod)을 설치해야 합니다. LogDNA 에이전트가 이 에이전트가 설치된 팟(Pod)에서 로그 파일을 읽고 로그 데이터를 LogDNA 인스턴스로 전달합니다.

LogDNA 인스턴스로 로그를 전달하도록 Kubernetes 클러스터를 구성하려면 명령행에서 다음 단계를 완료하십시오.

1. 터미널을 열어 {{site.data.keyword.cloud_notm}}에 로그인하십시오.

   ```
   ibmcloud login -a api.ng.bluemix.net
   ```
   {: pre}

   {{site.data.keyword.la_full_notm}} 인스턴스를 프로비저닝한 계정을 선택하십시오.

2. 이 세션에 대한 컨텍스트로 로깅을 구성할 클러스터를 설정하십시오.

   ```
   ibmcloud ks cluster-config <cluster_name_or_ID>
   ```
   {: pre}

   구성 파일의 다운로드가 완료되면 로컬 Kubernetes 구성 파일에 대한 경로를 환경 변수로 설정하는 데 사용할 수 있는 명령이 표시됩니다. 터미널에 표시된 명령을 복사하고 붙여넣어 `KUBECONFIG` 환경 변수를 설정하십시오.

3. Kubernetes 시크릿을 작성하여 서비스 인스턴스에 대한 logDNA 수집 키를 저장하십시오. LogDNA 수집 키는 logDNA 수집 서버에 대한 보안 웹 소켓을 열고 {{site.data.keyword.la_full_notm}} 서비스로 로깅 에이전트를 인증하는 데 사용됩니다.

   ```
   kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<logDNA_ingestion_key>
   ```
   {: pre}

4. Kubernetes 디먼 세트를 작성하여 Kubernetes 클러스터의 모든 작업자 노드에 LogDNA 에이전트를 배치하십시오. LogDNA 에이전트는 확장자가 `*.log`인 로그 및 팟(Pod)의 `/var/log` 디렉토리에 저장된 확장자 없는 파일을 수집합니다. 기본적으로 로그는 `kube-system`을 포함해 모든 네임스페이스에서 수집되며 자동으로 {{site.data.keyword.la_full_notm}} 서비스에 전달됩니다.

   ```
   kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
   ```
   {: pre}

5. LogDNA 에이전트가 배치되었는지 확인하십시오. 

   ```
   kubectl get pods
   ```
   {: pre}
   

하나 이상의 LogDNA 팟(Pod)이 표시되면 배치가 성공한 것입니다.
* **LogDNA 팟(Pod)의 수가 클러스터의 작업자 노드 수와 같습니다.** 
* 모든 팟(Pod)은 `실행 중` 상태여야 합니다.
* *Stdout* 및 *stderr*은 모든 컨테이너에서 자동으로 수집되고 전달됩니다. 로그 데이터에는 애플리케이션 로그 및 작업자 로그가 포함됩니다. 
* 기본적으로 작업자에서 실행되는 LogDNA 에이전트 팟(Pod)은 kube-system 로그를 포함해 해당 노드의 모든 네임스페이스에서 로그를 수집합니다.



## Kubernetes 클러스터의 LogDNA 에이전트에 태그 추가
{: #config_agent_kube_tags}

태그를 추가하려면 다음 단계를 완료하십시오.

1. 클러스터 환경을 설정하십시오. 다음 명령을 실행하십시오.

    먼저 명령을 가져와 환경 변수를 설정하고 Kubernetes 구성 파일을 다운로드하십시오.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    구성 파일의 다운로드가 완료되면 로컬 Kubernetes 구성 파일에 대한 경로를 환경 변수로 설정하는 데 사용할 수 있는 명령이 표시됩니다.

    그런 다음, 터미널에 표시된 명령을 복사하고 붙여넣어 KUBECONFIG 환경 변수를 설정하십시오.

2. 디먼 세트의 업데이트 전략을 확인하십시오. 그런 다음 *kubectl apply*를 사용할지 아니면 *kubectl edit*를 사용할지 선택하여 에이전트에 대한 구성 파일을 수정하십시오.

    업데이트 전략을 확인하려면 다음 명령을 실행하십시오.

    ```
    kubectl get ds/logdna-agent -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'
    ```
    {: pre}

    업데이트 전략을 *OnDelete*로 설정했거나 버전 제어 시스템을 통해 관리되는 구성 파일이 있는 경우, 로컬 구성 파일을 업데이트하고 *kubectl apply*를 사용하여 LogDNA 에이전트에 변경사항을 적용하십시오.

    업데이트 전략을 *RollingUpdate*로 설정한 경우, *kubectl edit*를 사용하여 변경사항을 업데이트하고 LogDNA 에이전트에 적용하십시오.

3. `logdna-agent-configmap.yaml` 파일을 편집하십시오. 

    로컬 사본을 수정하여 구성 파일을 업데이트하십시오. **참고:** 또한 다음 명령을 실행하여 에이전트의 구성 파일을 생성할 수 있습니다.

    ```
    kubectl get configmap logdna-agent -o=yaml > prod-logdna-agent-configmap.yaml
    ```
    {: codeblock}

    또는 *kubectl edit*를 사용하여 구성 파일을 업데이트하십시오.

    ```
    kubectl edit configmap logdna-agent
    ```
    {: codeblock}

4. 변경을 수행하십시오. **LOGDNA_TAGS** 섹션을 추가하십시오.

    ```
    - name: LOGDNA_TAGS
        value: tag1,tag2,tag3
    ```
    {: codeblock}

    예를 들어, 다음 섹션에는 구성 파일에 태그를 추가할 위치가 표시됩니다.

    ```
    apiVersion: extensions/v1beta1
    kind: DaemonSet
    metadata:
      name: logdna-agent
    spec:
      template:
        metadata:
          labels:
            app: logdna-agent
        spec:
          containers:
          - name: logdna-agent
            image: logdna/logdna-agent:latest
            imagePullPolicy: Always
            env:
            - name: LOGDNA_AGENT_KEY
              valueFrom:
                 secretKeyRef:
                  name: logdna-agent-key
                  key: logdna-agent-key
            - name: LDAPIHOST
              value: api.us-south.logging.cloud.ibm.com
            - name: LDLOGHOST
              value: logs.us-south.logging.cloud.ibm.com
            - name: LOGDNA_PLATFORM
              value: k8s
            - name: LOGDNA_TAGS
              value: tag1,tag2,tag3
    ```
    {: screen}

5. 로컬로 파일을 편집하는 경우 구성 변경사항을 적용하십시오. 

    ```
    kubectl apply -f logdna-agent-configmap.yaml
    ```
    {: codeblock}
    
    **참고:** *kubectl edit*를 사용하는 경우, 수정사항을 저장하면 변경사항이 자동으로 적용됩니다.


## Linux Ubuntu 또는 Debian에서 LogDNA 에이전트 구성
{: #config_agent_linux}

{{site.data.keyword.la_full_notm}} 인스턴스로 로그를 보내도록 Ubuntu 서버를 구성하려면 `logdna-agent`를 설치해야 합니다. LogDNA 에이전트가 */var/log*에서 로그 파일을 읽고 로그 데이터를 LogDNA 인스턴스로 전달합니다.

LogDNA 인스턴스로 로그를 전달하도록 Ubuntu 서버를 구성하려면 Ubuntu 터미널에서 다음 단계를 완료하십시오.

1. LogDNA 에이전트를 설치하십시오. 다음 명령을 실행하십시오.

    ```
    echo "deb https://repo.logdna.com stable main" | sudo tee /etc/apt/sources.list.d/logdna.list 
    ```
    {: codeblock}

    ```
    wget -O- https://repo.logdna.com/logdna.gpg | sudo apt-key add - 
    ```
    {: codeblock}

    ```
    sudo apt-get update
    ```
    {: codeblock}

    ```
    sudo apt-get install logdna-agent < "/dev/null"
    ```
    {: codeblock}

2. LogDNA 에이전트가 로그를 {{site.data.keyword.la_full_notm}} 인스턴스로 전달하는 데 사용해야 하는 수집 키를 설정하십시오.  

    ```
    sudo logdna-agent -k INGESTION_KEY
    ```
    {: codeblock}

    여기서 INGESTION_KEY에는 로그를 전달하도록 구성하는 {{site.data.keyword.la_full_notm}} 인스턴스에 대해 활성 상태인 수집 키가 포함됩니다.

3. 인증 엔드포인트를 설정하십시오. LogDNA 에이전트는 이 호스트를 사용하여 토큰을 인증하고 가져와 로그를 전달합니다.

    ```
    sudo logdna-agent -s LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com
    ```
    {: codeblock}

4. 수집 엔드포인트를 설정하십시오.

    ```
    sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com
    ```
    {: codeblock}

5. 모니터할 추가 로그 경로를 정의하십시오. 다음 명령을 실행하십시오. 

    ```
    sudo logdna-agent -d /path/to/log/folders
    ```
    {: codeblock}

    기본적으로 **/var/log**가 모니터됩니다.

6. 선택적으로 호스트를 태그하도록 LogDNA 에이전트를 구성하십시오. 


## Linux Ubuntu 또는 Debian의 LogDNA 에이전트에 태그 추가
{: #config_agent-linux_tags}
 

LogDNA 에이전트에 태그를 추가하려면 다음 단계를 완료하십시오.

1. LogDNA 에이전트가 실행 중인지 확인하십시오.

2. 하나 이상의 태그를 추가하십시오.

    ```
    sudo logdna-agent -t TAG1,TAG2 
    ```
    {: codeblock}


또한 LogDNA 구성 파일을 편집하고 태그를 추가할 수 있습니다. 구성 파일은 */etc/logdna.conf*에 있습니다.

1. 파일을 편집하십시오.

    ```
    sudo update-rc.d logdna-agent defaults
    ```
    {: codeblock}

2. 태그를 추가하십시오.

3. LogDNA 에이전트를 다시 시작하십시오.

    ``` 
    sudo /etc/init.d/logdna-agent start
    ```
    {: codeblock}














