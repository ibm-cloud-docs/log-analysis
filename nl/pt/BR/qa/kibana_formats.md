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

# Formatos de log do Kibana
{: #kibana_formats}

É possível configurar o Kibana para ser exibido nos diferentes campos da página *Descobrir* para cada entrada de log.
{:shortdesc}



## Formato de log do Kibana para aplicativos Cloud Foundry
{: #kibana_log_format_cf}

É possível configurar o Kibana para exibição, na página *Descobrir*, dos seguintes campos para cada entrada de log:

| Campo | Descrição |
|-------|-------------|
| @timestamp | `yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> O horário do evento registrado. <br> O registro de data e hora é definido até o milissegundo. |
| @version | Versão do evento. |
| ALCH_TENANT_ID | ID do espaço do {{site.data.keyword.Bluemix_notm}}. |
| \_id | O ID exclusivo para seu documento de log. |
| \_index | O índice para sua entrada de log. |
| \_type | O tipo de log; por exemplo, *syslog*. |
| app_name | O nome do aplicativo. |
| application_id | O ID exclusivo de seu aplicativo. |
| host | O nome de seu aplicativo que produziu os dados do log. |
| instance_id | O ID da instância de sua instância do aplicativo que produziu os dados do log. |
| loglevel | A severidade do evento registrado. |
| message | A mensagem que é emitida pelo componente. <br> A mensagem varia, dependendo do contexto. |
| message_type | O fluxo para o qual a mensagem de log é gravada. <br> * **OUT** refere-se ao fluxo stdout <br> * **ERR** refere-se ao fluxo stderr. |
| org_id | O ID exclusivo de sua organização do {{site.data.keyword.Bluemix_notm}} |
| org_name | O nome da organização do {{site.data.keyword.Bluemix_notm}} na qual seu app está montado. |
| origin | Componente de onde o evento foi originado. |
| source_id | O componente que produz logs. <br> A lista a seguir descreve os logs de cada componente: <br> * **API**: respostas registradas para chamadas API que solicitam uma mudança no estado do app. <br> * **APP**: respostas registradas do seu app. <br> * **CELL**: respostas registradas da célula Diego que indicam quando um aplicativo é iniciado, interrompido ou travado <br> * **LGR**: respostas registradas do loggregator que indicam problemas com o processo de criação de log. <br> * **RTR**: respostas registradas do Roteador quando ele roteia solicitações de HTTP para seu app. <br> * **SSH**: respostas registradas da célula Diego quando um usuário acessa um contêiner de app usando o comando `cf ssh`. <br> * **STG**: respostas registradas da célula Diego ou do Droplet Execution Agent quando seu app é montado ou remontado. |
| space_name | O nome do espaço do {{site.data.keyword.Bluemix_notm}} no qual seu app é montado. |
| timestamp | O horário do evento registrado. O registro de data e hora é definido até o milissegundo. |
{: caption="Tabela 1. Campos para apps CF" caption-side="top"}



## Formato de log do Kibana para contêineres do Docker que são implementados em um cluster do Kubernetes
{: #kibana_log_format_containers_kubernetes}

É possível configurar o Kibana para exibir na página *Descobrir* os campos a seguir para cada entrada de log. Esses campos são configurados por {{site.data.keyword.IBM}} e incluem seus dados da mensagem. 

| Campo | Descrição | Outras Informações |
|-------|-------------|---------------------------|
| @timestamp | `yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> O horário do evento registrado. <br> O registro de data e hora é definido até o milissegundo. | |
| @version | Versão do evento. | |
| ALCH_TENANT_ID | ID do espaço do {{site.data.keyword.Bluemix_notm}}. | |
| \_id | O ID exclusivo para seu documento de log. | |
| \_index | O índice para sua entrada de log. | |
| \_score |  |  |
| \_type | O tipo de log; por exemplo, *logs*. | |
| Crn_str | Informações sobre a origem do log. | Por padrão, esse campo é configurado pelo {{site.data.keyword.IBM_notm}}.b <br> **Nota**: se você enviar a mensagem de log no formato JSON válido e um dos campos for nomeado `crn`, o valor do campo será sobrescrito com o valor configurado na mensagem.  |  
| Docker.container_id_str | GUID do contêiner em execução em um pod. | |
| Ibm-containers.account_str | GUID do {{site.data.keyword.Bluemix_notm}} conta.  |  |
| Ibm-containers.cluster_id_str | GUID do cluster Kubernetes.  |  |
| Ibm-containers.cluster_type_str |  | O valor reservado para uso interno. {{site.data.keyword.IBM_notm}} |
| ibm-containers.region_str | Região em {{site.data.keyword.Bluemix_notm}}.  |  |
| Kubernetes.container_name_str | Nome do contêiner no qual um app é implementado.  |  |
| Kubernetes.host | Endereço IP público do trabalhador no qual o contêiner está em execução. |  |
| Kubernetes.labels.*example_label_name*\_str | Par de valores de chave que você anexa a um objeto do Kubernetes, como um pod. | Cada rótulo que você anexa a um objeto do Kubernetes é listado como um campo na entrada de log exibida no Kibana. <br> É possível ter 0 ou mais rótulos. |
| Kubernetes.namespace_name_str | O namespace do Kubernetes no qual o contêiner é implementado. |  |
| Kubernetes.pod_id_str | GUID do pod no qual o contêiner é implementado. |  |
| Kubernetes.pod_name_str | Nome do módulo. |  |
| message | Mensagem integral. | Se você enviar uma mensagem formatada JSON válida, cada campo será analisado e exibido individualmente no Kibana.  |
| Stream_str |  | O valor reservado para uso interno. {{site.data.keyword.IBM_notm}} |
|tag_str |  | O valor reservado para uso interno. {{site.data.keyword.IBM_notm}} |
{: caption="Tabela 3.  Campos para contêineres Dockar" caption-side="top"}


## Formato do log do Kibana para o {{site.data.keyword.messagehub}}
{: #kibana_log_format_messagehub}

É possível configurar o Kibana para exibição, na página *Descobrir*, dos seguintes campos para cada entrada de log:

| Campo | Descrição |
|-------|-------------|
| @timestamp | `yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> O horário do evento registrado. <br> O registro de data e hora é definido até o milissegundo. |
| @version | Versão do evento. |
| ALCH_TENANT_ID | ID do espaço do {{site.data.keyword.Bluemix_notm}}. |
| \_id | O ID exclusivo para seu documento de log. |
| \_index | O índice para sua entrada de log. |
| \_type | O tipo de log; por exemplo, *syslog*. |
| loglevel | A severidade do evento registrado, por exemplo, **Informações**. |
| Módulo | Esse campo é configurado como **MessageHub**. |
{: caption="Tabela 4. Campos para eventos do {{site.data.keyword.messagehub}}" caption-side="top"}

Exemplo de uma entrada de log:

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


