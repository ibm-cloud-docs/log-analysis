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

# Máquinas virtuais
{: #logging_vm_ov}

Os recursos de criação de log não são ativados automaticamente para máquinas virtuais (VMs). No entanto, é possível configurar sua VM para enviar logs para a Coleção de logs. Para coletar e enviar dados de log de uma VM para o serviço {{site.data.keyword.loganalysisshort}}, deve-se configurar um Multi-Tenant Logstash Forwarder (mt-logstash-forwarder). Em seguida, será possível visualizar, filtrar e analisar logs no Kibana.
{:shortdesc}


## Ingestão de log
{: #log_ingestion2}

O serviço {{site.data.keyword.loganalysisshort}} oferece planos diferentes. Todos os planos, com a exceção do plano *Lite*, incluem a capacidade de enviar logs para a Coleção de logs. Para obter mais informações sobre os planos, veja [Planos de serviços](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).

É possível enviar logs para o {{site.data.keyword.loganalysisshort}} usando o mt-logstash-forwarder. Para obter mais informações, veja [Enviar dados do log usando um Multi-Tenant Logstash Forwarder (mt-logstash-forwarder)](/docs/services/CloudLogAnalysis/how-to/send-data?topic=cloudloganalysis-send_data_mt#send_data_mt).


## Coleta de registro
{: #log_collection2}

Por padrão, o {{site.data.keyword.Bluemix_notm}} armazena dados do log por até 3 dias:   

* Um máximo de 500 MB por espaço de dados é armazenado por dia. Qualquer log além desse valor máximo de 500 MB é descartado. As dotações de limite são reconfiguradas diariamente às 0h30 UTC.
* Até 1,5 GB de dados podem ser procurados por um máximo de 3 dias. Os dados do log são substituídos (Primeiro a entrar, Primeiro a sair) depois de atingir 1,5 GB de dados ou depois de 3 dias.

O serviço {{site.data.keyword.loganalysisshort}} fornece planos adicionais que permitem armazenar logs na Coleção de logs o tempo que for necessário. Para obter mais informações sobre o preço de cada plano, veja [Planos de serviços](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).

* É possível configurar uma política de retenção de log que possa ser usada para definir o número de dias que você deseja manter os logs na Coleção de logs. Para obter mais informações, veja [Política de retenção de log](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-manage_logs#log_retention_policy).
* É possível excluir logs manualmente usando a CLI de Coleção de logs ou a API.


## Procura de log
{: #log_search2}

Por padrão, é possível usar o Kibana para procurar até 500 MB de logs por dia no {{site.data.keyword.Bluemix_notm}}. 

O serviço {{site.data.keyword.loganalysisshort}} fornece múltiplos planos. Cada plano possui recursos de procura de log diferentes, por exemplo, o plano *Coleção de logs* permite procurar até 1 GB de dados por dia. Para obter mais informações sobre os planos, veja [Planos de serviços](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).


## Análise de Log
{: #log_analysis}

Para analisar dados do log, use o Kibana para executar tarefas analíticas avançadas. É possível usar o Kibana, uma plataforma de software livre para visualização e análise de dados, para monitorar, procurar, analisar e visualizar seus dados em uma variedade de gráficos, por exemplo, diagramas e tabelas. Para obter mais informações, veja [Analisando logs no Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analyzing_logs_Kibana#analyzing_logs_Kibana).
