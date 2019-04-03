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

# Visualizando e analisando logs (Kibana)
{:#analyzing_logs_Kibana}

É possível usar o Kibana 5.1 Use o Kibana para executar tarefas analíticas avançadas.
{:shortdesc}

O Kibana é uma interface baseada em navegador na qual é possível analisar dados interativamente e customizar painéis que podem ser usados para analisar dados do log e executar tarefas de gerenciamento avançado. Para obter mais informações, veja [Guia do Usuário do Kibana ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}.

Os dados que a página do Kibana exibe são restritos por uma procura. O conjunto de dados padrão é definido pelo padrão de índice pré-configurado. Para filtrar as informações, é possível incluir novas consultas de procura e aplicar filtros no conjunto de dados padrão. Em seguida, é possível salvar a procura para reutilização futura. 

O Kibana inclui páginas diferentes que podem ser usadas para analisar seus logs:

| Página do Kibana | Descrição |
|-------------|-------------|
| Descobrir | Use essa página para definir procuras e analisar seus logs interativamente por meio de uma tabela e um histograma. |
| Visualizar | Use esta página para criar visualizações, como gráficos e tabelas, que podem ser usadas para analisar seus dados do log e comparar resultados.  |
| Painel | Use essa página para analisar seus logs por meio de coleções de visualizações e procuras salvas.  |
{: caption="Tabela 1. Páginas do Kibana" caption-side="top"}

**Nota:** só é possível analisar 1 dia completo de cada vez por meio da página Visualizar ou da página Painel, ainda que seja possível voltar 3 dias. Os dados do log são armazenados por 3 dias por padrão. 

| Página do Kibana | Informações de período de tempo |
|-------------|-------------------------|
| Descobrir | Analisar dados por um máximo de 3 dias. |
| Visualizar | Analisa dados para um período de 24 horas. <br> É possível filtrar dados do log para um período customizado que decorra 24 horas.  |
| Painel | Analisa dados para um período de 24 horas. <br> É possível filtrar dados do log para um período customizado que decorra 24 horas. <br> O selecionador de tempo que você configurar é aplicado a todas as visualizações que estiverem incluídas no painel. |
{: caption="Tabela 2. Informações de período" caption-side="top"}

Por exemplo, é desse modo que o Kibana pode ser usado para mostrar informações sobre um aplicativo ou contêiner CF em seu espaço por meio de diferentes páginas:

## Navegar para o painel do Kibana
{: #launch_Kibana}

É possível ativar o Kibana de qualquer uma das maneiras a seguir:

* No {{site.data.keyword.loganalysisshort}} painel de serviço

    É possível ativar o Kibana para que os dados que você vê agreguem logs de serviços em um espaço fornecido.
	
	Para obter mais informações, veja [Navegando para o Kibana por meio do painel do serviço Log Analysis](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_log_analysis).

* No {{site.data.keyword.Bluemix_notm}}

    É possível ativar seus logs específicos do app CF no Kibana dentro do contexto desse App específico. Para obter mais informações, veja [Navegando para o Kibana por meio do painel de um app CF](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_cf_app).
    
    É possível ativar seus logs específicos do contêiner do Docker dentro do contexto desse contêiner específico. Esse recurso se aplica somente aos contêineres que são implementados na infraestrutura gerenciada pelo {{site.data.keyword.Bluemix_notm}}. Para obter mais informações, veja [Navegando para o Kibana por meio do painel de um contêiner](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_for_containers).
    
    Para apps CF, a consulta que é usada para filtrar os dados que estão disponíveis para análise no Kibana recupera entradas de log para o aplicativo Cloud Foundry. As informações de log que o Kibana exibe estão todas relacionadas a um único aplicativo Cloud Foundry e a todas as suas instâncias. 
    
    Para contêineres, a consulta que é usada para filtrar os dados que estão disponíveis para análise no Kibana recupera entradas de log para todas as instâncias do contêiner. As informações de log que o Kibana exibe por padrão estão todas relacionadas a um único contêiner ou a um grupo de contêiner e a todas as suas instâncias. 
    
    

* Em um link direto do navegador

    Você pode desejar ativar o Kibana para que os dados vistos agreguem logs de serviços em um espaço fornecido.
    
    A consulta que é usada para filtrar os dados que são exibidos no painel recupera entradas de log para um espaço na organização do
    {{site.data.keyword.Bluemix_notm}}. As informações de log que o Kibana exibe incluem registros para todos os recursos que estiverem implementados no espaço da organização do {{site.data.keyword.Bluemix_notm}} na qual você estiver com login efetuado. 
    
    Para obter mais informações, veja [Navegando para o painel do Kibana de um navegador da web](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser).
    
    

## Analisar dados interativamente
{: #analyze_discover}

Na página Descobrir, é possível definir novas consultas de procura e aplicar filtros por consulta. Os dados do log são exibidos por meio de uma tabela e de um histograma. É possível usar essas visualizações para analisar os dados interativamente. Para obter mais informações, consulte [Analisando logs interativamente no Kibana](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#analize_logs_interactively).

Também é possível configurar filtros de campos de log, por exemplo, message_type e instance_ID, e configurar um período de tempo. É possível ativar ou desativar dinamicamente esses filtros. A tabela e o histograma exibirão as entradas de log que atenderem aos critérios de consulta e de filtragem que você ativar. Para obter mais informações, consulte [Filtrando logs no Kibana](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#filter_logs).

## Analisar dados por meio de uma visualização
{: #analyze_visualize}
    
Na página Visualizar, é possível definir novas consultas de procura e visualizações. Também é possível abrir visualizações salvas ou salvar uma visualização.

Para analisar os dados, é possível criar visualizações com base em uma procura nova ou existente. O Kibana inclui diferentes tipos de visualizações, como tabela, tendências e histograma, que podem ser usados para analisar as informações. O objetivo de cada visualização varia. Algumas visualizações são organizadas em linhas que fornecem os resultados de uma ou mais consultas. Outras visualizações exibem documentos ou informações customizadas. Os dados em uma visualização poderão ser corrigidos ou mudados, se uma consulta de procura for atualizada. É possível integrar a visualização em uma página da web ou compartilhá-la. 

Para obter mais informações, consulte [Analisando logs usando visualizações](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#kibana_visualizations).

## Analisar dados em um painel
{: #analyze_dashboard}

Na página Painel, é possível customizar, salvar e compartilhar múltiplas visualizações e procuras simultaneamente. 

É possível incluir, remover e reorganizar as visualizações no painel. Para obter mais informações, consulte [Analisando logs no Kibana por meio de um painel](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#analize_logs_dashboard).
    
Depois de customizar um painel do Kibana, é possível analisar os dados por meio de suas visualizações e salvá-los para reutilização futura. Para obter mais informações, veja [Salvando um painel do Kibana](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#save).

## Customizar o Kibana
{: #analyze_management}

Também é possível configurar e gerenciar recursos do Kibana na página **Gerenciamento**. 

É possível concluir uma das tarefas a seguir:

* Salvar, excluir, exportar e importar procuras. 
* Salvar, excluir, exportar e importar visualizações.
* Salvar, excluir, exportar e importar painéis.
* [Atualizar a lista de campos.](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_reload_fields)

## Limitações
{: #limitations}

No Kibana, é possível compartilhar uma Visualização ou um Painel somente com membros da mesma organização ou conta.

Os recursos do Kibana a seguir não são suportados:

* Compartilhando uma procura.
* Criando novos padrões de índice. 


## Funções que são requeridas por um usuário para visualizar logs
{: #roles}

No {{site.data.keyword.Bluemix_notm}}, é possível designar uma ou mais funções para os usuários. Essas funções definem quais tarefas estão ativadas para esse usuário para trabalhar com o serviço {{site.data.keyword.loganalysisshort}}. 

As tabelas a seguir listam as funções que um usuário deve ter para visualizar logs:

<table>
  <caption>Permissões requeridas por um **proprietário da conta** para ver logs</caption>
  <tr>
    <th>Ação</th>
	<th>Funções de espaço do CF</th>
	<th>Funções de organização do CF</th>
	<th>Funções IAM</th>
  </tr>
  <tr>
    <td>Visualizar logs em um domínio de espaço</td>
	<td>*Funcionamento* </br>*Desenvolvedor * </br>*Auditor*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>Visualizar logs no domínio de contas</td>
	<td></td>
	<td></td>
	<td>*Administrador*</td>
  </tr>
  <tr>
    <td>Visualizar logs em um domínio da organização</td>
	<td></td>
	<td>*Funcionamento* </br>*Gerenciador de faturamento *  </br>*Auditor*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>Permissões requeridas por um **auditor** para ver logs</caption>
  <tr>
    <th>Ação</th>
	<th>Funções de espaço do CF</th>
	<th>Funções de organização do CF</th>
	<th>Funções IAM</th>
  </tr>
  <tr>
    <td>Visualizar logs em um domínio de espaço</td>
	<td>*Auditor*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>Visualizar logs no domínio de contas</td>
	<td></td>
	<td></td>
	<td>*Visualizador*</td>
  </tr>
  <tr>
    <td>Visualizar logs em um domínio da organização</td>
	<td></td>
	<td>*Auditor*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>Permissões requeridas por um **administrador** para ver logs</caption>
  <tr>
    <th>Ação</th>
	<th>Funções de espaço do CF</th>
	<th>Funções de organização do CF</th>
	<th>Funções IAM</th>
  </tr>
  <tr>
    <td>Visualizar logs em um domínio de espaço</td>
	<td>*Desenvolvedor *</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>Visualizar logs no domínio de contas</td>
	<td></td>
	<td></td>
	<td>*Visualizador*</td>
  </tr>
  <tr>
    <td>Visualizar logs em um domínio da organização</td>
	<td></td>
	<td>*Funcionamento*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>Permissões requeridas por um **desenvolvedor** para ver logs</caption>
  <tr>
    <th>Ação</th>
	<th>Funções de espaço do CF</th>
	<th>Funções de organização do CF</th>
	<th>Funções IAM</th>
  </tr>
  <tr>
    <td>Visualizar logs em um domínio de espaço</td>
	<td>*Desenvolvedor *</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>Visualizar logs no domínio de contas</td>
	<td></td>
	<td></td>
	<td>*Visualizador*</td>
  </tr>
  <tr>
    <td>Visualizar logs em um domínio da organização</td>
	<td></td>
	<td>*Auditor*</td>
	<td></td>
  </tr>
</table>



## URLs para ativar o Kibana
{: #urls_kibana}

A tabela a seguir lista as URLs para ativar o Kibana e as versões do Kibana por região:

<table>
    <caption>URLs para ativar o Kibana</caption>
    <tr>
      <th>Region</th>
      <th>URL</th>
      <th>Versão do Kibana</th>
    </tr>
	<tr>
      <td>Frankfurt</td>
	  <td>[https://logging.eu-fra.bluemix.net](https://logging.eu-fra.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
	<tr>
      <td>Sydney</td>
	  <td>[https://logging.au-syd.bluemix.net](https://logging.au-syd.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
	<tr>
      <td></td>
	  <td>[https://logging.eu-gb.bluemix.net](https://logging.eu-gb.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
    <tr>
      <td>Sul dos Estados Unidos</td>
      <td>[Https://logging.ng.bluemix.net](https://logging.ng.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
</table>




