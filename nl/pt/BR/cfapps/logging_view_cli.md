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


# Analisando logs do CF por meio da CLI
{: #analyzing_logs_cli}

No {{site.data.keyword.Bluemix}}, é possível visualizar, filtrar e analisar logs por meio da interface da linha de comandos. 
{:shortdesc}

Para analisar os logs do aplicativo Cloud Foundry (CF), use o comando a seguir: `ibmcloud cf logs`
Para obter mais informações, veja [cf logs](/docs/cli/reference/ibmcloud?topic=cloud-cli-cf#cf_logs).


## Analisando logs do app CF na CLI
{: #analyzing_cf_logs_cli}

Use o comando **cf logs** para exibir logs de um app Cloud Foundry e dos componentes do sistema que interagem com ele quando você implementa o app no {{site.data.keyword.Bluemix_notm}}. O comando **cf logs** exibe os fluxos de logs STDOUT e STDERR de um aplicativo Cloud Foundry.

Para visualizar os logs de seu interesse ou excluir o conteúdo que você não deseja visualizar, é possível usar o comando **cf logs** com opções de filtragem, como **cut** e **grep**, na interface da linha de comandos cf.

* Para visualizar os logs para um app Cloud Foundry, veja [Visualizando o log para um app Cloud Foundry](/docs/services/CloudLogAnalysis/cfapps?topic=cloudloganalysis-analyzing_logs_cli#full_log_cli).
* Para visualizar os registros de log mais recentes para um app Cloud Foundry, veja [Visualizando as entradas de log mais recentes para um app Cloud Foundry](/docs/services/CloudLogAnalysis/cfapps?topic=cloudloganalysis-analyzing_logs_cli#tailing_log_cli).
* Para visualizar os registros de log para um app Cloud Foundry em um intervalo de tempo específico, veja [Visualizando uma seção dos logs](/docs/services/CloudLogAnalysis/cfapps?topic=cloudloganalysis-analyzing_logs_cli#partial_log_cli).
* Para visualizar as entradas nos logs para um app Cloud Foundry que contenham palavras-chave específicas, veja [Visualizando entradas de log que contenham determinadas palavras-chave](logging_view_cli.html#partial_by_keyword_log_cli).


### Visualizando o log para um app Cloud Foundry
{: #full_log_cli}

Para ver todos os logs disponíveis para um app Cloud Foundry, conclua as etapas a seguir:

1. Abra um terminal e efetue login no {{site.data.keyword.Bluemix_notm}}.

2. Na linha de comandos, execute o comando a seguir para exibir todos os logs:

   <pre class="pre screen"><code>  ibmcloud cf logs  <var class="keyword varname"> appname </var> </code></pre>
   
   
### Visualizando as entradas de log mais recentes para um app Cloud Foundry
{: #tailing_log_cli}

Para ver os logs mais recentes que estão disponíveis para um app Cloud Foundry, conclua as etapas a seguir:

1. Abra um terminal e efetue login no {{site.data.keyword.Bluemix_notm}}.

2. Na linha de comandos, execute o comando a seguir para exibir todos os logs:

     <pre class="pre screen"><code> ibmcloud cf logs  <var class="keyword varname"> appname </var>  -- recente </code></pre>

<div class="note tip"><span class="tiptitle">Dica:</span> ao executar o comando <span class="keyword cmdname">cf push</span> ou <span class="keyword cmdname">cf
start</span> em uma janela de linha de comandos, é possível inserir <samp class="ph codeph">cf
logs appname --recent</samp> em outra janela de linha de comandos para ver
os logs em tempo real. </div>


### Visualizando uma seção de um log do Cloud Foundry
{: #partial_log_cli}

Para visualizar uma parte dos logs que estão disponíveis para um app Cloud Foundry dentro de um intervalo de tempo, conclua as etapas a seguir:

1. Abra um terminal e efetue login no {{site.data.keyword.Bluemix_notm}}.

2. Na linha de comandos, execute o comando a seguir para exibir todos os logs:

    <pre class="pre screen"><code>ibmcloud cf logs <var class="keyword varname">appname</var> --recent  | cut -c 29-40,46-</code></pre>
    
    Para obter mais informações sobre a opção **cut**, insira **cut --help**.


### Visualizando entradas de log que contêm determinadas palavras-chave
{: #partial_by_keyword_log_cli}

Para exibir entradas de log que contenham determinadas palavras-chave para um app Cloud Foundry, conclua as etapas a seguir:

1. Abra um terminal e efetue login no {{site.data.keyword.Bluemix}}.

2. Na linha de comandos, execute o comando a seguir para exibir todos os logs:

    <pre class="pre screen"><code>ibmcloud cf logs <var class="keyword varname">appname</var> --recent | grep '<var class="keyword varname">keyword</var>'</code></pre>
    

Por exemplo, para exibir entradas de log que contenham a palavra-chave **APP**, é possível usar o comando a seguir:

<pre class="pre screen"><code>ibmcloud cf logs appname --recent | grep '\[App'</code></pre>

Para obter mais informações sobre a opção **grep**, digite **grep --help**.


### Logs do aplicativo Cloud Foundry
{: #cf_app_logs_cli}

Os logs a seguir estão disponíveis para um aplicativo Cloud Foundry depois de implementá-lo no {{site.data.keyword.Bluemix_notm}}:

**buildpack.log**

Esse arquivo de log registra eventos informativos de baixa granularidade para
depuração. É possível usar esse log para solucionar problemas de
execução de buildpack.

Para gerar dados para o arquivo *buildpack.log*, deve-se ativar o rastreio do buildpack
usando o comando a seguir: `cf set-env appname JBP_LOG_LEVEL DEBUG`
   
Para visualizar esse log, insira o comando a seguir: `cf files appname
app/.buildpack-diagnostics/buildpack.log`


**staging_task.log**

Esse arquivo de log registra mensagens depois das principais etapas da
tarefa de preparação. É possível usar esse log para solucionar problemas de preparação.

Para visualizar esse log, insira o comando a seguir: `ibmcloud cf files appname logs/staging_task.log`




