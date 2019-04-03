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

# Fazendo download de logs
{: #downloading_logs1}

É possível fazer download de logs em um arquivo local ou canalizar dados em outro programa. É possível fazer download de logs dentro do contexto de uma sessão. Uma sessão especifica quais logs serão transferidos por download. Se o download dos logs é interrompido, a sessão permite continuar o download de onde parou. Após a conclusão do download, deve-se excluir a sessão.
{:shortdesc}

Conclua as etapas a seguir para fazer download de dados do log que estão disponíveis em um espaço do {{site.data.keyword.Bluemix_notm}} em um arquivo local:

## Etapa 1: efetuar login no IBM Cloud

Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

## Etapa 2: identificar quais logs estão disponíveis
{: #step31}

1. Use o comando `ibmcloud cf logging status` para ver quais logs estão disponíveis para as duas últimas semanas. Execute o comando a seguir:

    ```
    ibmcloud cf logging status
    ```
    {: codeblock}
    
    Por exemplo, a saída da execução desse comando é:
    
    ```
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 | linux_syslog,log   |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}

    **Nota:** o serviço {{site.data.keyword.loganalysisshort}} é um serviço global que usa a Hora Universal Coordenada (UTC). Dias são definir como dias UTC. Para obter logs para um horário local específico do dia, talvez seja necessário fazer download de vários dias UTC.


## Etapa 3: criar uma sessão
{: #step32}

É necessária uma sessão para definir o escopo de dados do log que estão disponíveis para um download e para manter o status do download. 

Use o comando [cf logging session create](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_create1) para criar uma sessão. Opcionalmente, é possível especificar a data de início, a data de encerramento e os tipos de logs quando você cria uma sessão:  

* Quando você especificar a data de início e a data de encerramento, a sessão fornecerá acesso aos logs entre essas datas inclusivas. 
* Quando você especificar o tipo de log (**-t**), a sessão fornecerá acesso a um tipo específico de log. Esse é um recurso importante ao gerenciar logs em escala, porque é possível definir o escopo de uma sessão para apenas um pequeno subconjunto de logs nos quais você estiver interessado.

**Nota:** para cada sessão, é possível fazer download de logs por até 15 dias.

Para criar uma sessão que seja usada para fazer download de logs do tipo *log*, execute o comando a seguir:

```
ibmcloud cf logging session create -t log
```
{: codeblock}

A sessão retorna as seguintes informações:

* O intervalo de data a ser transferido por download. O padrão é a data UTC atual.
* Os tipos de log a ser transferido por download. Por padrão, inclui todos os tipos de log que estão disponíveis para o período de tempo que você especifica ao criar a sessão. 
* Informações sobre se a conta inteira ou apenas o espaço atual deve ser incluído. Por padrão, você obtém logs no espaço ao qual está conectado.
* O ID de sessão, que é necessário para fazer download de logs.

Por
exemplo,

```
$ ibmcloud cf logging session create -t log     
+--------------+--------------------------------------+
|     NAME     |                VALUE                 |
+--------------+--------------------------------------+
| Access-Time  | 2017-05-25T18:04:21.743792338Z       |
| Create-Time  | 2017-05-25T18:04:21.743792338Z       |
| Date-Range   | {                                    |
|              |  "End": "2017-05-25T00:00:00Z",      |
|              |  "Start": "2017-05-25T00:00:00Z"     |
|              | }                                    |
| Id           | -jshdjsunelsssr4566722==             |
| Space        | fdgrghg3-b090-4567-vvfg-afbc436902a3 |
| Type-Account | {                                    |
|              |  "Type": "log"                       |
|              | }                                    |
| Username     | xxx@yyy.com                          |
+--------------+--------------------------------------+
```
{: screen}

**Dica:** para ver a lista de sessões ativas, execute o comando [cf logging session list](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_list1).

## Etapa 4: fazer download de dados do log em um arquivo
{: #step42}

Para fazer download dos logs especificados pelos parâmetros de sessão, execute o comando a seguir:

```
ibmcloud cf logging download -o Log_File_Name Session_ID
```
{: codeblock}

Em que

* Log_File_Name é o nome do arquivo de saída.
* Session_ID é o GUID da sessão. Você obtém esse valor na etapa anterior.

Por
exemplo,

```
ibmcloud cf logging download -o helloLogs.gz -jshdjsunelsssr4566722==
 160.00 KB / 380.33 KB [==============>------------------------]  42.07% 20.99 KB/s 10s
```
{: screen}

O indicador de progresso move-se de 0 para 100% conforme o download dos logs é feito.

**Nota:** 

* O formato dos dados transferidos por download é compactado como JSON. Se você descompactar o arquivo ZIP .gz e abri-lo, será possível ver os dados no formato JSON. 
* O JSON compactado é adequado para ingestão pelo ElasticSearch ou pelo Logstash. Se -o não for fornecido, os dados serão transmitidos para stdout para que você possa canalizá-los diretamente em sua própria pilha ELK.
* Também é possível processar os dados com qualquer programa que possa analisar JSON. 

## Etapa 5: excluir a sessão
{: #step51}

Após a conclusão do download, deve-se excluir a sessão usando o comando [cf logging session delete](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_delete1). 

Execute o comando a seguir para excluir uma sessão:

```
ibmcloud cf logging session delete Session_ID
```
{: codeblock}

Em que Session_ID é o GUID da sessão que você criou em uma etapa anterior.

Por
exemplo,

```
ibmcloud cf logging session delete -jshdjsunelsssr4566722==
+---------+------------------------+
|  NAME   |         VALUE          |
+---------+------------------------+
| Message | Delete session success |
+---------+------------------------+
```
{: screen}




