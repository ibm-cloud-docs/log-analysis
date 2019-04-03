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

# CLI do IBM Cloud Log Analysis (plug-in do CF)
{: #logging_cli}

A CLI do {{site.data.keyword.loganalysislong}} é um plug-in para gerenciar os logs para recursos em nuvem em execução em um espaço de uma organização do {{site.data.keyword.Bluemix}}.
{: shortdesc}

**Pré-requisitos**
* Antes de executar os comandos de criação de log, efetue login no {{site.data.keyword.Bluemix_notm}} com o comando `ibmcloud login` para gerar um token de acesso do {{site.data.keyword.Bluemix_short}}
e autenticar sua sessão. Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).

Para descobrir sobre como usar a CLI do {{site.data.keyword.loganalysisshort}}, veja [Gerenciando logs](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#log_analysis_ov).

<table>
  <caption>Comandos para gerenciar os logs</caption>
  <tr>
    <th></th>
    <th>Quando utilizá-lo</th>
  </tr>
  <tr>
    <td>[ ibmcloud cf logging ](#base)</td>
    <td>Use esse comando para obter informações sobre a CLI, como versão ou a lista de comandos.</td>
  </tr>
  <tr>
    <td>[ ibmcloud cf logging auth ](#auth)</td>
    <td>Use esse comando para obter o token de criação de log que pode ser usado para enviar logs para o serviço {{site.data.keyword.loganalysisshort}}.</td>
  </tr>
  <tr>
    <td>[ ibmcloud cf logging delete ](#delete)</td>
    <td>Use esse comando para excluir logs armazenados na Coleção de logs.</td>
  </tr>
  <tr>
    <td>[ ibmcloud cf logging download (Beta) ](#download)</td>
    <td>Use este comando para fazer download de logs da Coleção de logs para um arquivo local ou canalizar os logs para outro programa, como Elastic Stack. </td>
  </tr>
  <tr>
    <td>[ ibmcloud cf logging help ](#help)</td>
    <td>Use esse comando para obter ajuda sobre como usar a CLI, além de uma lista de todos os comandos.</td>
  </tr>
  <tr>
    <td>[ Opção de criação de log ibmcloud cf ](#option)</td>
    <td>Use esse comando para visualizar ou configurar o período de retenção para logs que estão disponíveis em um espaço ou conta.</td>
  </tr>
  <tr>
    <td>[ ibmcloud cf logging session create (Beta) ](#session_create1)</td>
    <td>Use esse comando para criar uma nova sessão.</td>
  <tr>
  <tr>
    <td>[ibmcloud cf logging session delete (Beta)](#session_delete1)</td>
    <td>Use esse comando para excluir uma sessão.</td>
  <tr>  
  <tr>
    <td>[ ibmcloud cf logging session list (Beta) ](#session_list1)</td>
    <td>Use esse comando para listar sessões ativas e seus IDs.</td>
  <tr>  
  <tr>
    <td>[ ibmcloud cf logging session show (Beta) ](#session_show1)</td>
    <td>Use esse comando para mostrar o status de uma única sessão.</td>
  <tr>  
  <tr>
    <td>[    ibmcloud cf logging status
    ](#status1)</td>
    <td>Use esse comando para obter informações sobre os logs que são coletados em um espaço ou conta.</td>
  </tr>
  </table>


## ibmcloud cf logging
{: #base1}

Fornece informações sobre a versão da CLI e como usar a CLI.

```
ibmcloud cf logging [ parameters ]
```
{: codeblock}

**Parameters**

<dl>
<dt>-- help, -h</dt>
<dd>Configure esse parâmetro para mostrar a lista de comandos ou para obter ajuda para um comando.
</dd>

<dt>-- versão, -v</dt>
<dd>Configure esse parâmetro para imprimir a versão da CLI.</dd>
</dl>

**Exemplos**

Para obter a lista de comandos, execute o comando a seguir:

```
ibmcloud cf logging -- help
```
{: codeblock}

Para obter a versão da CLI, execute o comando a seguir:

```
ibmcloud cf logging -- version
```
{: codeblock}


## ibmcloud cf logging auth
{: #auth}

Retorna um token de criação de log que pode ser usado para enviar logs para o serviço {{site.data.keyword.loganalysisshort}}. 

**Nota:** O token não expire.

```
ibmcloud cf logging auth
```
{: codeblock}

**Retornos**

<dl>
  <dt>Criação de Token</dt>
  <dd>Por exemplo, `jec8BmipiEZc`.
  </dd>
  
  <dt>ID da Organização</dt>
  <dd>GUID da organização do {{site.data.keyword.Bluemix_notm}} à qual você está conectado.
  </dd>
  
  <dt>ID do espaço</dt>
  <dd>GUID do espaço dentro da organização à qual você está conectado.
  </dd>
</dl>

## ibmcloud cf logging delete
{: #delete2}

Exclui logs armazenados na Coleção de logs.

```
ibmcloud cf logging delete [ parameters ]
```
{: codeblock}

**Parameters**

<dl>
  <dt>--start value, -s value</dt>
  <dd>(Opcional) Configura a data de início em Hora Universal Coordenada (UTC): *AAAA-MM-DD*, por exemplo, `2006-01-02`. <br>O valor padrão é configurado como 2 semanas atrás.
  </dd>
  
  <dt>--end value, -e value</dt>
  <dd>(Opcional) Configura a data de encerramento na Hora Universal Coordenada (UTC): *AAAA-MM-DD* <br>O formato UTC da data é **AAAA-MM-DD**, por exemplo, `2006-01-02`. <br>O valor padrão é configurado como a data atual.
  </dd>
  
  <dt>--type value, -t value</dt>
  <dd>(Opcional) Configura o tipo de log. <br>Por exemplo, *syslog* é um tipo de log. <br>O valor padrão é configurado como **\***. <br>É possível especificar múltiplos tipos de log separando cada tipo com uma vírgula, por exemplo, **log_type_1,log_type_2,log_type_3*.
  </dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>(Opcional) Configura o escopo da informação de log fornecida para o nível de conta. <br>Se esse parâmetro não for especificado, o valor padrão será configurado para fornecer informações de log sobre o espaço atual apenas.
  </dd>
</dl>

**Exemplo**

Para excluir os logs do tipo *linux_syslog* em 25 de maio de 2017, execute o comando a seguir:
```
ibmcloud cf logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
```
{: codeblock}



## ibmcloud cf logging download (Beta)
{: #download4}

Faz download de logs da Coleção de logs em um arquivo local ou canaliza logs para outro programa, como um Elastic Stack. 

**Nota:** para fazer download de arquivos, será necessário criar uma sessão primeiro. Uma sessão define de quais logs fazer download com base no intervalo de data, no tipo de log e no tipo de conta. O download de logs é feito dentro do contexto de uma sessão. Para obter mais informações, veja [ibmcloud cf logging session create (Beta)](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-logging_cli#session_create1).

```
ibmcloud cf logging download [ parameters ] [ arguments ]
```
{: codeblock}

**Parameters**

<dl>
<dt>-- output valor, -o valor</dt>
<dd>(Opcional) Configura o caminho e o nome do arquivo para o arquivo de saída local no qual os logs são transferidos por download. <br>O valor padrão é um hífen (-). <br>Configure esse parâmetro como o valor padrão para logs de saída para a saída padrão.</dd>
</dl>

**Argumentos**

<dl>
<dt>Session_ID</dt>
<dd>Configure com o valor de ID de sessão obtido ao executar o comando `ibmcloud cf logging session create`. Esse valor indica qual sessão usar ao fazer download de logs. <br>**Nota:** o comando `ibmcloud cf logging session create` fornece os parâmetros que controlam quais logs são transferidos por download. </dd>
</dl>

**Nota:** após a conclusão do download, a execução do mesmo comando novamente recusará a realização de qualquer coisa. Para fazer download dos mesmos dados novamente, deve-se usar um arquivo diferente ou uma sessão diferente.

**Exemplos**

Em um sistema Linux, para fazer download de logs em um arquivo chamado mylogs.gz, execute o comando a seguir:

```
ibmcloud cf logging download -o mylogs.gz guBeZTIuYtreOPi-WMnbUg==
```
{: screen}

Para fazer download de logs em seu próprio Elastic Stack, execute o comando a seguir:

```
ibmcloud cf logging download guBeZTIuYtreOPi-WMnbUg== | gunzip | logstash -f logstash.conf
```
{: screen}

O arquivo a seguir é um exemplo de um arquivo logstash.conf:

```
input {
  stdin {
    Codec = > json_lines {
  }
} { {
  Elasticsearch {
    Hosts = > [ "127.0.0.1:9200" ]
  }
}
```
{: screen}


## ibmcloud cf logging help
{: #help1}

Fornece informações sobre como usar um comando.

```
ibmcloud cf logging help [ command ]
```
{: codeblock}

**Parameters**

<dl>
<dt></dt>
<dd>Configure o nome do comando para o qual você deseja obter ajuda.
</dd>
</dl>


**Exemplos**

Para obter ajuda sobre como executar o comando para visualizar o status de logs, execute o comando a seguir:

```
ibmcloud cf logging help status
```
{: codeblock}


## ibmcloud cf logging option
{: #option}

Exibe ou muda o período de retenção para logs que estão disponíveis em um espaço ou conta. 

* O período é configurado em número de dias.
* O valor padrão é **-1**. 

**Nota:** por padrão, todos os logs são armazenados. Deve-se excluí-los manualmente usando o comando **delete**. Configure uma política de retenção para excluir os logs automaticamente.

```
ibmcloud cf logging option [ parameters ]
```
{: codeblock}

**Parameters**

<dl>
<dt>--retention value, -r value</dt>
<dd>(Opcional) Configura o número de dias de retenção. <br> O valor padrão é *-1* dias.</dd>

<dt>--at-account-level, -a </dt>
  <dd>(Opcional) Configura o escopo como nível de conta. <br>Se esse parâmetro não for especificado, o valor padrão será configurado como *-1* para o espaço atual, que é o espaço no qual você efetuou login usando o comando `ibmcloud cf login`.
  </dd>
</dl>

**Exemplos**

Para ver o período de retenção atual padrão para o espaço no qual você efetuou login, execute o comando a seguir:

```
ibmcloud cf logging option
```
{: codeblock}

A saída é:

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-ibmcloud cfgh436902a3 |        -1 |
+--------------------------------------+-----------+
```
{: screen}


Para mudar o período de retenção para 25 dias do espaço ao qual você está conectado, execute o comando a seguir:

```
ibmcloud cf logging option -r 25
```
{: codeblock}

A saída é:

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-ibmcloud cfgh436902a3 |        25 |
+--------------------------------------+-----------+
```
{: screen}


## ibmcloud cf logging session create (Beta)
{: #session_create1}

Cria uma nova sessão.

**Nota:** é possível ter até 30 sessões simultâneas em um espaço. A sessão é criada para um usuário. As sessões não podem ser compartilhadas entre usuários em um espaço.

```
ibmcloud cf logging session create [ parameters ]
```
{: codeblock}

**Parameters**

<dl>
  <dt>--start value, -s value</dt>
  <dd>(Opcional) Configura a data de início em Hora Universal Coordenada (UTC): *AAAA-MM-DD*, por exemplo, `2006-01-02`. <br>O valor padrão é configurado como 2 semanas atrás.
  </dd>
  
  <dt>--end value, -e value</dt>
  <dd>(Opcional) Configura a data de encerramento em Hora Universal Coordenada (UTC): *AAAA-MM-DD*, por exemplo, `2006-01-02`. <br>O valor padrão é configurado como a data atual.
  </dd>
  
  <dt>--type value, -t value</dt>
  <dd>(Opcional) Configura o tipo de log. <br>Por exemplo, *syslog* é um tipo de log. <br>O valor padrão é configurado como asterisco (*). <br>É possível especificar múltiplos tipos de log separando cada tipo com uma vírgula, por exemplo, *log_type_1,log_type_2,log_type_3*.
  </dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>(Opcional) Configura o escopo como nível de conta. <br>Se esse parâmetro não for especificado, o valor padrão será definido somente para o espaço atual,
ou seja, o espaço no qual você efetuou login usando o comando `ibmcloud cf login`.
  </dd>
</dl>

**Valores Retornados**

<dl>
<dt>Tempo de acesso</dt>
<dd>Registro de data e hora que indica quando a sessão foi usada pela última vez.</dd>

<dt>Horário da criação</dt>
<dd>O registro de data e hora que corresponde à data e hora em que a sessão foi criada.</dd>

<dt>Data-Intervalo</dt>
<dd>Indica os dias usados para filtrar logs. Os logs identificados neste intervalo de data ficam disponíveis para gerenciamento por meio da sessão.</dd>

<dt>ID</dt>
<dd>ID de sessão.</dd>

<dt>Espaço</dt>
<dd>O ID do espaço no qual a sessão está ativa.</dd>

<dt>Tipo de Conta</dt>
<dd>Os tipos de log que são transferidos por download por meio da sessão.</dd>

<dt>Nome de Usuário</dt>
<dd>ID da {{site.data.keyword.IBM_notm}} do usuário que criou a sessão.</dd>
</dl>


**Exemplo**

Para criar uma sessão que inclua logs entre 20 e 26 de maio de 2017 para um tipo de log de *log*, execute o comando a seguir:

```
ibmcloud cf logging session create -s 2017-05-20 -e 2017-05-26 -t log
```
{: screen}


## ibmcloud cf logging session delete (Beta)
{: #session_delete1}

Exclui uma sessão, especificada pelo ID de sessão.

```
ibmcloud cf logging delete delete [ arguments ]
```
{: codeblock}

**Argumentos**

<dl>
<dt>ID de
sessão</dt>
<dd>ID da sessão que você deseja excluir. <br>É possível usar o comando `ibmcloud cf logging session list` para obter todos os IDs de sessão ativos.</dd>
</dl>

**Exemplo**

Para excluir uma sessão com o ID de sessão *cI6hvAa0KR_tyhjxZZz9Uw==*, execute o comando a seguir:

```
ibmcloud cf logging session delete cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}



## ibmcloud cf logging session list (Beta)
{: #session_list1}

Lista as sessões ativas e seus IDs.

```
ibmcloud cf logging session list 
```
{: codeblock}

**Valores Retornados**

<dl>
<dt>ID</dt>
<dd>ID de sessão.</dd>

<dt>SPACE</dt>
<dd>O ID do espaço no qual a sessão está ativa.</dd>

<dt>USERNAME</dt>
<dd>ID da {{site.data.keyword.IBM_notm}} do usuário que criou a sessão.</dd>

<dt>CREATE-TIME</dt>
<dd>O registro de data e hora que corresponde à data e hora em que a sessão foi criada.</dd>

<dt>ACCESS-TIME</dt>
<dd>O registro de data e hora que indica quando a sessão foi usada pela última vez.</dd>
</dl>
 

## ibmcloud cf logging session show (Beta)
{: #session_show1}

Mostra o status de uma sessão única.

```
ibmcloud cf logging session show [ arguments ]
```
{: codeblock}

**Argumentos**

<dl>
<dt>Session_ID</dt>
<dd>ID da sessão ativa da qual você deseja obter informações.</dd>
</dl>

**Valores Retornados**

<dl>
<dt>Tempo de acesso</dt>
<dd></dd>

<dt>Horário da criação</dt>
<dd>O registro de data e hora que corresponde à data e hora em que a sessão foi criada.</dd>

<dt>Data-Intervalo</dt>
<dd>Indica os dias usados para filtrar logs. Os logs identificados neste intervalo de data ficam disponíveis para gerenciamento por meio da sessão.</dd>

<dt>ID</dt>
<dd>ID de sessão.</dd>

<dt>Espaço</dt>
<dd>O ID do espaço no qual a sessão está ativa.</dd>

<dt>Tipo de Conta</dt>
<dd>Os tipos de log que são transferidos por download por meio da sessão.</dd>

<dt>Nome de Usuário</dt>
<dd>ID da {{site.data.keyword.IBM_notm}} do usuário que criou a sessão.</dd>
</dl>

**Exemplo**

Para mostrar detalhes de uma sessão com ID de sessão *cI6hvAa0KR_tyhjxZZz9Uw==*, execute o comando a seguir:

```
ibmcloud cf logging session show cI6hvAa0KR_tyhjxZZz9Uw ==
```
{: screen}


## ibmcloud cf logging status
{: #status1}

Retorna informações sobre os logs que são coletados em um espaço ou conta.

```
ibmcloud cf logging status [ parameters ]
```
{: codeblock}

**Parameters**

<dl>
  <dt>--start value, -s value</dt>
  <dd>(Opcional) Configura a data de início em Hora Universal Coordenada (UTC): *AAAA-MM-DD*, por exemplo, `2006-01-02`. <br>O valor padrão é configurado como 2 semanas atrás.
  </dd>
  
  <dt>--end value, -e value</dt>
  <dd>(Opcional) Configura a data de encerramento em Hora Universal Coordenada (UTC): *AAAA-MM-DD*, por exemplo, `2006-01-02`. <br>O valor padrão é configurado como a data atual.
  </dd>
  
  <dt>--type value, -t value</dt>
  <dd>(Opcional) Configura o tipo de log. <br>Por exemplo, *syslog* é um tipo de log. <br>O valor padrão é configurado como asterisco (*). <br>É possível especificar múltiplos tipos de log separando cada tipo com uma vírgula, por exemplo, *log_type_1,log_type_2,log_type_3*.
  </dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>(Opcional) Configura o escopo como nível de conta. <br> **Nota:** configure esse valor para obter dados da conta. <br>Se esse parâmetro não for especificado, o valor padrão será definido somente para o espaço atual,
ou seja, o espaço no qual você efetuou login usando o comando `ibmcloud cf login`.
  </dd>
  
  <dt>-- list-type-detalhes, -l</dt>
  <dd>(Opcional) Configure esse parâmetro para listar o subtotal de tipos de log de cada dia.
  </dd>
</dl>

**Nota:** o comando `ibmcloud cf logging status` relata apenas as duas últimas semanas de logs armazenados na Coleção de logs quando nenhuma data de início e de encerramento é especificada.


