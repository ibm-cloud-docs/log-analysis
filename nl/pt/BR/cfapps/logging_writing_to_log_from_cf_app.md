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

# Criação de log de aplicativo de tempo de execução por meio de apps CF
{: #logging_writing_to_log_from_cf_app}

No {{site.data.keyword.Bluemix}}, para persistir dados do log para um app Cloud Foundry e seu tempo de execução, deve-se gravar seus logs para STDOUT e STDERR. 
{:shortdesc}

No {{site.data.keyword.Bluemix_notm}}, os registros de log STDOUT e STDERR são coletados automaticamente:

* O STDOUT (saída padrão) fornece informações gerais.  
* O STDERR (erro padrão) fornece informações que incluem mensagens de erro e outros avisos de diagnóstico. 

O Loggregator seleciona automaticamente os dados de saída padrão e erro padrão. O Loggregator é o componente que encaminha os logs de dentro do Cloud Foundry. 

Por exemplo, 

Para um **app Liberty Cloud Foundry**, o console.log padrão para o servidor Liberty é selecionado automaticamente pelo loggregator. 

* O console.log contém o STDOUT e o STDERR redirecionados do processo da JVM. A saída de console conterá os principais eventos e erros se você usar a configuração consoleLogLevel padrão. A saída de console também conterá quaisquer mensagens que forem gravadas nos fluxos system.out e system.err se você usar a configuração copySystemStreams padrão. A saída de console sempre contém mensagens que são gravadas diretamente pelo processo da JVM, como saída -verbose:gc. É possível ajustar o nível de criação de log do Liberty por meio do server.xml.
* O consoleLogLevel configura o nível de filtro do manipulador console.log. Ao configurar o consoleLogLevel como INFO, você configura todas as mensagens INFO, AUDIT, WARNING e ERROR para serem gravadas no arquivo console.log. **Nota:** as entradas de log FINE, FINER, FINEST são gravadas somente no arquivo trace.log.

Para obter mais informações sobre os aplicativos Liberty for Java™, veja [Perfil Liberty: criação de log e rastreio ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](http://www-01.ibm.com/support/knowledgecenter/was_beta_liberty/com.ibm.websphere.wlp.nd.multiplatform.doc/ae/rwlp_logging.html){: new_window}.

Para um **app Cloud Foundry Node.js**, é possível usar o módulo de criação de log do console integrado para configurar a criação de log para o tempo de execução no {{site.data.keyword.Bluemix}}. É possível colocar mensagens no stdout e stderr:

* O console.log('message') enviará a mensagem para o fluxo STDOUT
* O console.error('error_message') enviará o erro para o fluxo STDERR

Para obter mais informações sobre os aplicativos Node.js, veja [Como registrar no node.js ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](https://docs.nodejitsu.com/articles/intermediate/how-to-log/){: new_window}.


Para obter mais informações sobre os **aplicativos Ruby on Rails**, veja [O Criador de log ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](http://guides.rubyonrails.org/debugging_rails_applications.html#the-logger){: new_window}.

A tabela a seguir lista o mapeamento entre alguns logs de tempos de execução de aplicativo e os logs que são selecionados automaticamente pelo Loggregator:

| **Tempo de execução** |    **STDOUT**     | **STDERR** |
|-----------------|-------------------|-------------------|
| Liberty | system.out | system.err |
| Node.js | console.log, console.info | console.error, console.warn |
| Ruby | stdout| stderr |
{: caption="Tabela 1. Mapeamento entre alguns logs de tempos de execução de aplicativo e os logs que são selecionados automaticamente pelo Loggregator" caption-side="top"}

