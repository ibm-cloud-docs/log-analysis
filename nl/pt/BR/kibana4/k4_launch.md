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


# Navegando para o painel do Kibana
{: #k4_launch}

É possível ativar o Kibana da UI do {{site.data.keyword.Bluemix}} ou diretamente de um navegador da web.
{:shortdesc}

Ative o Kibana no {{site.data.keyword.Bluemix_notm}} para visualizar e analisar dados no contexto para o recurso no qual você ativa o Kibana. Por exemplo, é possível ativar seus logs específicos do app CF no Kibana dentro do contexto para esse App específico.

A tabela a seguir lista os recursos e o método de navegação suportado para ativar o Kibana:

<table>
<caption>Tabela 1. Lista de recursos e métodos de navegação suportados. </caption>
  <tr>
    <th>Recursos</th>
    <th>Navegando para o painel do Kibana por meio do painel do Bluemix</th>
    <th>Navegando para o painel do Kibana por meio de um navegador da web</th>
  <tr>
  <tr>
    <td>Aplicativo CF</td>
    <td>Sim</td>
    <td>Sim</td>
  <tr>  
  <tr>
    <td>Contêiner implementado em um cluster Kubernetes</td>
    <td>Sim</td>
    <td>Sim</td>
  <tr>  
</table>

Para obter mais informações sobre Kibana, veja o [Guia do Usuário do Kibana ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](https://www.elastic.co/guide/en/kibana/4.1/index.html){: new_window}.
    

##  Navegando para o painel do Kibana por meio do painel do Bluemix
{: #launch_Kibana_from_bluemix}

A consulta que é usada para filtrar os dados que são exibidos no Kibana recupera entradas de log para o app ou contêiner CF do {{site.data.keyword.Bluemix_notm}} no local em que o Kibana é ativado.

Para ver os logs de um aplicativo Cloud Foundry ou contêiner do Docker no Kibana, conclua as etapas a seguir:

1. Efetue login no {{site.data.keyword.Bluemix_notm}} e, em seguida, clique no nome do app ou contêiner no painel do {{site.data.keyword.Bluemix_notm}}. 
    
2. Abra a guia de log na IU do {{site.data.keyword.Bluemix_notm}}.

    * Para apps CF, clique em **Logs** na barra de navegação. 
    * Para os contêineres implementados na infraestrutura gerenciada pelo {{site.data.keyword.Bluemix_notm}}, selecione **Monitoramento e logs** na barra de navegação e, em seguida, clique na guia **Criação de log**. 
    
        A guia de logs é aberta.  

3. Clique em **Visualização avançada**. O painel Kibana é aberto.

    Por padrão, a página **Descobrir** é carregada com o modelo de índice padrão selecionado e com um filtro de tempo configurado para os últimos 30 segundos. A consulta de procura é configurada para corresponder todas as entradas para o seu app CF ou contêiner do Docker.

    Se a página Descobrir não mostrar nenhuma entrada de log, ajuste o selecionador de tempo. 


##  Navegando para o painel do Kibana por meio de um navegador da web
{: #launch_Kibana_from_browser1}

A consulta que é usada para filtrar os dados que são exibidos no Kibana recupera entradas de log para um espaço na organização do {{site.data.keyword.Bluemix_notm}}. As informações de log que o Kibana exibe incluem registros para todos os recursos que estiverem implementados no espaço da organização do {{site.data.keyword.Bluemix_notm}} na qual você estiver com login efetuado.

Conclua a etapa a seguir para ativar o Kibana por meio de um navegador:

1. Ative a interface com o usuário do Kibana.
    
    Por exemplo, 
      
        <table>
          <caption>Tabela 1.  URLs para ativar Kibana  </caption>
           <tr>
            <th>Region</th>
            <th>URL</th>
          </tr>
          <tr>
            <td>Sul dos Estados Unidos</td>
            <td>Https://logging.ng.bluemix.net/ </td>
          </tr>
          <tr>
            <td></td>
            <td>Https://logging.eu-gb.bluemix.net/ </td>
          </tr>
        </table>

    Se a página Descobrir não mostrar nenhuma entrada de log, ajuste o selecionador de tempo. 

