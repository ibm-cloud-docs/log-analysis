---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion 

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

 
# Enviando logs
{: #ingest}

É possível enviar dados do log para uma instância do {{site.data.keyword.la_full_notm}}. 
{:shortdesc}

Conclua as etapas a seguir para enviar os logs programaticamente:

## Etapa 1. Obter a chave de API de ingestão 
{: #ingest_step1}

**Nota:** deve-se ter a função de **gerenciador** para a instância ou o serviço do {{site.data.keyword.la_full_notm}} para concluir essa etapa. Para obter mais informações, consulte [Concedendo permissões para gerenciar logs e configurar alertas no LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna).

Conclua as etapas a seguir para obter a chave de ingestão:
    
1. Ative a IU da web do {{site.data.keyword.la_full_notm}}. Para obter mais informações, consulte [Acesse a IU da web do {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Selecione o ícone  ** Configuração **   ![Configuration icon](images/admin.png). Em seguida, selecione  ** Organização **. 

3. Selecione  ** Chaves API **.

    É possível ver as chaves de ingestão que foram criadas. 

4. Use uma chave de ingestão existente ou clique em **Gerar chave de ingestão** para criar uma nova.

    Uma nova chave é incluída na lista. Copie a chave.


## Etapa 2. Enviar logs
{: #ingest_step2}

Para enviar logs, execute o comando cURL a seguir:

```
curl "ENDPOINT/logs/ingest?QUERY_PARAMETERS" -u INGESTION_KEY: --header "Content-Type: application/json; charset=UTF-8" -d "LOG_LINES"
```
{: codeblock}

Em que 

* ENDPOINT representa o ponto de entrada para o serviço. Cada região tem uma URL diferente.
* QUERY_PARAMETERS são parâmetros que definem os critérios de filtragem que são aplicados à solicitação de ingestão.
* LOG_LINES descrevem o conjunto de linha de logs que você deseja enviar. Ele é definido como uma matriz de objetos.
* INGESTION_KEY é a chave que você criou na etapa anterior.

A tabela a seguir lista os terminais por região:

| Região         | Nó de Extrem                                             | 
|----------------|------------------------------------------------------|
| `Us-south`       | `https://logs.us-south.logging.cloud.ibm.com`        |
{: caption="Terminais por região" caption-side="top"} 


A tabela a seguir lista os parâmetros de consulta:

| Parâmetro de consulta | Digite       | Status     | Descrição |
|-----------------|------------|------------|-------------|
| `hostname`      | `string`     | Necessário   | Nome do host da origem. |
| `mac`           | `string`     | opcional   | O endereço mac de rede do computador host.    |
| `ip`            | `string`     | opcional   | O endereço IP local do computador host.  | 
| `now`           | `date-time`  | opcional   | O registro de data e hora do UNIX de origem em milissegundos no momento da solicitação. Usado para calcular o desvio de tempo.|
| `tags`          | `string`     | opcional   | Tags que são usadas para agrupar hosts dinamicamente. |
{: caption="Parâmetros de consulta" caption-side="top"} 



A tabela a seguir lista os dados necessários por linha de log:

| Parameters     | Digite       | Descrição                                   |
|----------------|------------|-----------------------------------------------|
| `timestamp`      |            | Registro de data e hora do UNIX, incluindo milissegundos, quando a entrada de log foi registrada.       | 
| `line`           | `string`     | Texto da linha de log.                                     |
| `app`            | `string`     | Nome do aplicativo que gera a linha de log.  |
| `level`          | `string`     | Configure um valor para o nível. Por exemplo, os valores de amostra para esse parâmetro são `INFO`, `WARNING` e `ERROR`. |
| `meta`           |            | Esse campo é reservado para informações customizadas que estão associadas a uma linha de log. Para incluir metadados em uma chamada API, especifique o campo de metadados sob o objeto de linhas. Os metadados podem ser visualizados dentro do contexto dessa linha.                      |
{: caption="Campos de objeto de linha" caption-side="top"} 

Por exemplo, a amostra a seguir mostra o JSON para uma linha de log que você deseja alimentar:

```
{ 
  "lines": [ 
    { 
      "timestamp": 2018-11-02T10:53:06+00:00, 
      "line":"This is my first log line.", 
      "app":"myapp",
      "level": "INFO",
      "meta": {
        "customfield": {"nestedfield": "nestedvalue"}
      }
    }
  ] 
}
```
{: screen}


## Exemplo:
{: #ingest_example}

A amostra a seguir mostra o comando cURL para enviar 1 linha de log para uma instância do serviço {{site.data.keyword.la_full_notm}}: 

```
curl "https://logs.us-south.logging.cloud.ibm.com/logs/ingest?hostname=MYHOST&now=$(date +%s)000" -u xxxxxxxxxxxxxxxxxxxxxxx: --header "Content-Type: application/json; charset=UTF-8" -d "{\"lines\":[{\"line\":\"This is a sample test log statement\",\"timestamp\":\"2018-11-02T10:53:06+00:00\",\"level\":\"INFO\",\"app\":\"myapp\"}]}"
```
{: screen}

