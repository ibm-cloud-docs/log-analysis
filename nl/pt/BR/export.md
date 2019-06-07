---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, export logs

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

 
# Exportando logs para o arquivo local
{: #export}

É possível exportar dados do log no formato JSONL de uma instância do {{site.data.keyword.la_full_notm}} para um arquivo local. É possível exportar logs programaticamente ou por meio da IU da web do IBM Log Analysis. 
{:shortdesc}

Considere as informações a seguir ao exportar dados do log:
* Exporte um conjunto de entradas de log. Para definir o conjunto de dados que você deseja exportar, é possível aplicar filtros e procuras. Também é possível especificar o intervalo de tempo. 
* Ao exportar os logs por meio da IU da web, um e-mail é enviado para o seu endereço de e-mail, com um link para um arquivo compactado que inclui os dados. Para obter os dados, deve-se clicar no link e fazer download do arquivo compactado.
* Ao exportar os logs programaticamente, é possível optar por enviar um e-mail ou transmitir os logs para o seu terminal.
* O arquivo de log compactado que contém os dados que você deseja exportar está disponível por 48 horas, no máximo. 
* O número máximo de linhas que podem ser exportadas é 10.000.



## Exportando Logs da UI da Web
{: #ui}

Conclua as etapas a seguir para exportar os dados do log:

1. Clique no ícone  ** Visualizações **   ![Configuration icon](images/views.png).
2. Selecione  ** Tudo **  ou uma visualização.
3. Aplique um prazo, filtros e critérios de procura até que você veja as entradas de log que deseja exportar.
4. Clique em **Visualização não salva** se você estiver iniciando por meio da visualização **Tudo**. Clique em seu nome de visualização se você selecionou uma visualização na etapa anterior.
5. Selecione  ` Exportar linhas `. Uma nova janela é aberta.
6. Verifique o intervalo de tempo. Se for necessário mudá-lo, clique no intervalo de tempo predefinido no campo *Mudar intervalo de tempo para a exportação*.
7. Selecione **Preferir linhas mais novas** ou **Preferir linhas mais antigas** no caso de a solicitação de exportação exceder o limite de linha.
8. Verifique seu e-mail. Você recebe um e-mail do **LogDNA** com um link para fazer download de suas linhas exportadas.


## Exportando logs programaticamente usando a API
{: #api}

Conclua as etapas a seguir para exportar os logs programaticamente:

1. Gere uma chave de serviço. 

    **Nota:** deve-se ter a função de **gerenciador** para a instância ou o serviço do {{site.data.keyword.la_full_notm}} para concluir essa etapa. Para obter mais informações, consulte [Concedendo permissões para gerenciar logs e configurar alertas no LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna).

    1. Ative a IU da web do {{site.data.keyword.la_full_notm}}. Para obter mais informações, consulte [Acesse a IU da web do {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

    2. Selecione o ícone  ** Configuração **   ![Configuration icon](images/admin.png). Em seguida, selecione  ** Organização **. 

    3. Selecione  ** Chaves API **.

        É possível ver as chaves de serviço que foram criadas. 

    4. Clique em  ** Gerar chave de serviço **.

        Uma nova chave é incluída na lista. Copie essa chave.

2. Exportar logs. Execute o comando cURL a seguir:

    ```
    curl "ENDPOINT/v1/export?QUERY_PARAMETERS" -u SERVICE_KEY:
    ```
    {: codeblock}

    Em que 

    * ENDPOINT representa o ponto de entrada para o serviço. Cada região tem uma URL diferente.
    * QUERY_PARAMETERS são parâmetros que definem os critérios de filtragem que são aplicados à solicitação de exportação.
    * SERVICE_KEY é a chave de serviço que você criou na etapa anterior.

A tabela a seguir lista os terminais por região:

| Região         | Nó de Extrem                                             | 
|----------------|------------------------------------------------------|
| `Us-south`       | `https://api.us-south.logging.cloud.ibm.com `        |
{: caption="Terminais por região" caption-side="top"} 


A tabela a seguir lista os parâmetros de consulta que podem ser configurados:

| Parâmetro de consulta | Digite       | Status     | Descrição |
|-----------|------------|------------|-------------|
| `from`      | `int32`      | Necessário   | Horário de início. Configure como registro de data e hora do UNIX em segundos ou milissegundos. |
| `to`        | `int32`      | Necessário   | Horário de encerramento. Configure como registro de data e hora do UNIX em segundos ou milissegundos.    |
| `size`      | `string`     | Opcional   | Número de linhas de log a serem incluídas na exportação.  | 
| `hosts`     | `string`     | Opcional   | Lista separada por vírgulas de hosts. |
| `apps`      | `string`     | Opcional   | Lista separada por vírgulas de aplicativos. |
| `levels`    | `string`     | Opcional   | Lista separada por vírgulas de níveis de log. |
| `query`     | `string`     | Opcional   | Procurar consulta. Para obter mais informações, consulte  [ Logs de procura ](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6). |
| `prefer`    | `string`     | Opcional   | Define as linhas de log que você deseja exportar. Os valores válidos são `head`, as primeiras linhas do log, e `tail`, as últimas linhas do log. Se não especificado, o padrão será padronizado.  |
| `email`     | `string`     | Opcional   | Especifica o e-mail com o link transferível por download de sua exportação. Por padrão, as linhas do log são transmitidas.|
| `emailSubject` | `string`     | Opcional   | Use para configurar o assunto do e-mail. </br>Use `%20` para representar um espaço. Por exemplo, um valor de amostra é `Export%20logs`. |
{: caption="Parâmetros de consulta" caption-side="top"} 

Por exemplo, para transmitir linhas de log para o terminal, é possível executar o comando a seguir:

```
curl "https: //api.us-south.logging.cloud.ibm.com/v1/export?to=$ (date + %s) 000 &from=$ ((($(date + %s) -86400)) 000 &levels=info" -u e08c0c759663491880b0d61712346789:
```
{: screen}

Para enviar um e-mail com o link para fazer download das linhas de log especificadas na exportação, é possível executar o comando a seguir:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=joe@ibm.com" -u e08c0c759663491880b0d61712346789:
```
{: screen}


Para enviar um e-mail com um assunto customizado, é possível executar o comando a seguir:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=lopezdsr@uk.ibm.com&emailSubject=Export%20test" -u e08c0c759663491880b0d61712346789:
```
{: screen}

