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
{: #launch}

É possível ativar o Kibana do serviço {{site.data.keyword.loganalysisshort}} por meio da UI do {{site.data.keyword.Bluemix}} ou diretamente de um navegador da web.
{:shortdesc}

Para apps CF e contêineres do Docker, é possível ativar o Kibana na UI do {{site.data.keyword.Bluemix_notm}} para visualizar e analisar dados no contexto para o recurso no qual você ativa o Kibana. Por exemplo, é possível ativar seus logs específicos do app CF no Kibana dentro do contexto para esse App específico.
    
Para qualquer recurso em nuvem, como um contêiner do Docker que é implementado em uma infraestrutura do Kubernetes, é possível ativar o Kibana por meio de um link direto do navegador ou do painel de serviço do {{site.data.keyword.loganalysisshort}} para ver os dados agregados do log de serviços em um espaço fornecido. A consulta que é usada para filtrar os dados exibidos no painel recupera entradas de log para um espaço na organização. A informação de log que o Kibana exibe inclui registros para todos os recursos que são implementados dentro do espaço da organização no qual você efetuou login. 

A tabela a seguir lista alguns recursos em nuvem e os métodos de navegação suportados para ativar o Kibana:

<table>
<caption>Tabela 1. Lista de recursos e métodos de navegação suportados. </caption>
  <tr>
    <th>Recursos</th>
	<th>Navegue para o painel do Kibana do painel de serviço do {{site.data.keyword.loganalysisshort}}</th>
    <th>Navegue para o painel do Kibana do painel do Bluemix</th>
    <th>Navegue para o painel do Kibana de um navegador da web</th>
  </tr>
  <tr>
    <td>Aplicativo CF</td>
	<td>Sim</td>
    <td>Sim</td>
    <td>Sim</td>
  </tr>  
  <tr>
    <td>Contêiner implementado em um cluster Kubernetes</td>
	<td>Sim</td>
    <td>Sim</td>
    <td>Sim</td>
  </tr>  
  <tr>
    <td>Contêiner implementado em uma infraestrutura gerenciada pelo {{site.data.keyword.Bluemix_notm}}(descontinuado)</td>
	<td>Sim</td>
    <td>Sim</td>
    <td>Sim</td>
  </tr>  
</table>

Para obter mais informações sobre Kibana, veja o [Guia do Usuário do Kibana ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}.
    

##  Navegando para o Kibana por meio do painel do serviço Log Analysis
{: #launch_Kibana_from_log_analysis}

A consulta que é usada para filtrar os dados exibidos no Kibana recupera entradas de log para esse espaço na organização. 
	
A informação de log que o Kibana exibe inclui registros para todos os recursos que são implementados dentro do espaço da organização no qual você efetuou login.

Conclua as etapas a seguir para ativar o Kibana por meio do painel do serviço {{site.data.keyword.loganalysisshort}}:

1. Efetue login no {{site.data.keyword.Bluemix_notm}} e, em seguida, clique no serviço {{site.data.keyword.loganalysisshort}} no painel do {{site.data.keyword.Bluemix_notm}}. 
    
2. Selecione a guia **Gerenciado** na UI do {{site.data.keyword.Bluemix_notm}}.

3. Clique em **ATIVAR**. O painel Kibana é aberto.

Por padrão, a página **Descobrir** é carregada com o padrão de índice padrão selecionado e um filtro de tempo configurado para os últimos 15 minutos. 

Se a página Descobrir não mostrar nenhuma entrada de log, ajuste o selecionador de tempo. Para obter mais informações, consulte [Configurando um filtro de tempo](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter).

	
	
##  Navegando para o Kibana por meio de um navegador da web
{: #launch_Kibana_from_browser}

A consulta que é usada para filtrar os dados exibidos no Kibana recupera entradas de log para esse espaço na organização. 
	
A informação de log que o Kibana exibe inclui registros para todos os recursos que são implementados dentro do espaço da organização no qual você efetuou login.

Conclua as etapas a seguir para ativar o Kibana em um navegador:

1. Abra um navegador da web e ative o Kibana. Em seguida, efetue login na interface com o usuário do Kibana.

    Para ver a lista de URLs por região, veja [URLs para ativar o Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analyzing_logs_Kibana#urls_kibana).
    
    A página Descobrir no Kibana é aberto.
	
2. Selecione o padrão de índice para o espaço no qual você deseja visualizar e analisar os dados do log.

    1. Clique em **default-index**.
	
	2. Selecione o padrão de índice do espaço. O formato do padrão de índice é o seguinte:
	
	    ```
	    [logstash-Space_ID-]YYYY.MM.DD 
	    ```
        {: screen}
	
	    em que *Space_ID* é o GUID do espaço no qual você deseja visualizar e analisar dados do log. 
	
Se a página Descobrir não mostrar nenhuma entrada de log, ajuste o selecionador de tempo. Para obter mais informações, consulte [Configurando um filtro de tempo](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter).


	
##  Navegando para o Kibana por meio do painel de um app CF
{: #launch_Kibana_from_cf_app}

A consulta usada para filtrar os dados exibidos no Kibana recupera entradas de log para o app CF do {{site.data.keyword.Bluemix_notm}} do qual o Kibana é ativado.

Para ver os logs de um aplicativo Cloud Foundry no Kibana, conclua as etapas a seguir:

1. Efetue login em sua conta do {{site.data.keyword.Bluemix_notm}}.

    O painel do {{site.data.keyword.Bluemix_notm}} pode ser localizado em: [http://bluemix.net ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](http://bluemix.net){:new_window}.
    
	Depois de efetuar login com seu ID de usuário e senha, a UI do {{site.data.keyword.Bluemix_notm}} é aberta.

2. Clique no nome do app ou contêiner no painel do {{site.data.keyword.Bluemix_notm}}. 
    
3. Abra a guia de log na IU do {{site.data.keyword.Bluemix_notm}}.

    Para apps CF, clique em **Logs** na barra de navegação. 
    A guia de logs é aberta.  

4. Clique em **Visualizar no Kibana**. O painel Kibana é aberto.

    Por padrão, a página **Descobrir** é carregada com o padrão de índice padrão selecionado e um filtro de tempo configurado para os últimos 15 minutos. A consulta de procura é configurada para corresponder todas as entradas para o app CF.

    Se a página Descobrir não mostrar nenhuma entrada de log, ajuste o selecionador de tempo. Para obter mais informações, consulte [Configurando um filtro de tempo](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter).

	
	
##  Navegando para o Kibana por meio do painel de um contêiner que é implementado em um cluster do Kubernetes
{: #launch_Kibana_for_containers_kube}

A consulta que é usada para filtrar os dados que são exibidos no Kibana recupera entradas de log para o cluster no qual você ativa o Kibana.

Para ver os logs de um contêiner no Kibana, conclua as etapas a seguir:

1. Efetue login em sua conta do {{site.data.keyword.Bluemix_notm}}.

    O painel do {{site.data.keyword.Bluemix_notm}} pode ser localizado em: [http://bluemix.net ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](http://bluemix.net){:new_window}.
    
	Depois de efetuar login com seu ID de usuário e senha, a UI do {{site.data.keyword.Bluemix_notm}} é aberta.

2. No menu, selecione **Painel**.

3. Na seção *Clusters*, selecione o cluster.

4. Na seção *Visão geral*, selecione **Visualizar logs**.

    O Kibana é aberto.




##  Navegando para o Kibana do painel de um contêiner que é implementado na infraestrutura gerenciada pelo {{site.data.keyword.Bluemix_notm}} (descontinuado)
{: #launch_Kibana_for_containers}

Esse método se aplica somente aos contêineres que são implementados na infraestrutura gerenciada pelo {{site.data.keyword.Bluemix_notm}}.

A consulta usada para filtrar os dados exibidos no Kibana recupera entradas de log para o contêiner de onde o Kibana é ativado.

Para ver os logs de um contêiner do Docker no Kibana, conclua as etapas a seguir:

1. Efetue login no {{site.data.keyword.Bluemix_notm}} e, em seguida, clique no contêiner por meio do painel do {{site.data.keyword.Bluemix_notm}}. 
    
2. Abra a guia de log na IU do {{site.data.keyword.Bluemix_notm}}.

    Para contêineres que são implementados na infraestrutura gerenciada pelo {{site.data.keyword.IBM_notm}}, selecione **Monitoramento e logs** na barra de navegação e, em seguida, clique na guia **Criação de log**. 
    
    A guia de logs é aberta.  

3. Clique em **Visualização avançada**. O painel Kibana é aberto.

    Por padrão, a página **Descobrir** é carregada com o modelo de índice padrão selecionado e com um filtro de tempo configurado para os últimos 30 segundos. A consulta de procura é configurada para corresponder todas as entradas do contêiner do Docker.

    Se a página Descobrir não mostrar nenhuma entrada de log, ajuste o selecionador de tempo. Para obter mais informações, consulte [Configurando um filtro de tempo](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter).

	



