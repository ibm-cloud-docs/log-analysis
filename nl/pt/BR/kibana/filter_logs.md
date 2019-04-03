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

# Filtrando logs no Kibana
{:#filter_logs}

Na página Descobrir, é possível criar consultas de procura e aplicar filtros para restringir as
informações que são exibidas para análise.
{:shortdesc}

* É possível definir uma ou mais consultas de procura na barra de procura da página Descobrir. Uma
consulta de procura define um subconjunto de entradas de log. Use a linguagem de consulta Lucene para definir
uma consulta de procura. 

* É possível incluir filtros da *Lista de campos* ou de entradas de tabela. Um filtro define a seleção de dados incluindo ou excluindo informações. É possível ativar ou desativar um filtro, inverter a ação do filtro, ativar ou desativar o filtro ou
removê-lo completamente. 

Depois de definir uma nova procura, salve-a para que ela possa ser reutilizada para análise futura na
página Descobrir ou para criar visualizações que possam ser usadas em painéis customizados. Para obter mais
informações, consulte [Salvando uma procura](/docs/services/CloudLogAnalysis/kibana/define_search.html#save_search1).

Ao executar uma nova procura, o histograma, a tabela e a lista de Campos são atualizados automaticamente
para mostrar os resultados da procura. Para descobrir quais dados são mostrados, consulte
[Identificando os dados que são exibidos na página Descobrir](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data).

A lista a seguir descreve cenários que mostram como filtrar dados em seus logs:

* É possível criar procuras customizadas para filtrar seus logs. Para obter mais informações, consulte
[Filtrando logs definindo consultas customizadas](/docs/services/CloudLogAnalysis/kibana/define_search.html#define_search).

* É possível procurar no log por entradas que incluem um texto específico no valor de um campo. Para
obter mais informações, consulte
[Filtrando seus logs para um texto
específico em um valor de campo](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#filter_logs_spec_text).
 
* É possível procurar no log por um valor de campo específico ou excluir entradas do log para um valor
de campo específico. Para obter mais informações, consulte
[Filtrando seus logs para um
valor de campo específico](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#filter_logs_spec_field).
 
* É possível filtrar seus logs para mostrar entradas em um período de tempo. Para obter mais informações, consulte [Configurando um filtro de tempo](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter).
     

## Incluindo um filtro para um valor que não esteja relacionado na *Lista de campos*
{:#add_filter_out_value}

Para incluir um filtro para um valor que não é mostrado na *Lista de campos*, procure
por registros que incluam esse valor por meio de uma consulta. Em seguida, inclua o filtro na entrada de
tabela que está disponível na página Descobrir. 

Conclua as etapas a seguir para incluir um filtro para um valor que não está disponível na lista mostrada
na seção *Lista de campos*:

1. Consulte a página Descobrir do Kibana para ver qual subconjunto de seus dados é exibido. Para obter mais informações, consulte [Identificando os dados que são exibidos em sua página Descobrir do Kibana](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data).

2. Na página Descobrir, modifique a consulta para procurar por um valor de campo específico.

    Por exemplo, para procurar pela instância *3*, a consulta que você insere é a seguinte:
   `application_id:9d222152-8834-4bab-8685-3036cd25931a AND instance_id:"3"`
    
    Na tabela, é possível ver quaisquer registros que corresponderem à sua consulta. 
    
 3. Expanda um registro e selecione o botão de lupa ![Botão Lupa no modo inclusivo](images/include_field_icon.jpg "Botão Lupa no inclusivo") para incluir um filtro.
     
4. Verifique se o filtro foi incluído.

   


## Filtrando seus logs para um valor de campo específico
{:#filter_logs_spec_field}

É possível procurar por entradas que incluam um valor de campo específico. 

Conclua as etapas a seguir para procurar por entradas que incluem um valor de campo específico:

1. Consulte a página Descobrir do Kibana para ver qual subconjunto de seus dados é exibido. Para obter mais informações, consulte [Identificando os dados que são exibidos em sua página Descobrir do Kibana](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data).

2. Na *Lista de campos*, identifique o campo para o qual deseja definir um filtro e clique nele.

    Um máximo de 5 valores é mostrado para o campo. Cada valor possui dois botões de lupa. 
    
    Se você não conseguir ver o valor, consulte [Incluindo um filtro para um valor que não estiver relacionado na lista Campos](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#add_filter_out_value).

3. Para incluir um filtro que procure entradas com um valor de campo, escolha a lupa com um sinal de mais ![Lupa no modo inclusivo](images/include_field_icon.jpg "Botão Lupa no inclusivo") para esse valor.

    Para incluir um filtro que procure entradas que não incluam esse valor de campo, escolha a lupa com um sinal de menos ![Lupa no modo exclusivo](images/exclude_field_icon.jpg "Botão Lupa no modo exclusivo") para esse valor.

4. Escolha qualquer uma das seguintes opções para trabalhar com filtros no Kibana:

    <table>
      <caption>Tabela 1. Métodos para trabalhar com filtros</caption>
      <tbody>
        <tr>
          <th align="center">Opção</th>
          <th align="center">Descrição</th>
          <th align="center">Outras informações</th>
        </tr>
        <tr>
          <td align="left">Ativar</td>
          <td align="left">Selecione essa opção para ativar um filtro.</td>
          <td align="left">Ao incluir um filtro, ele é ativado automaticamente. <br> Se um filtro estiver desativado, clique nele para ativá-lo.</td>
        </tr>
        <tr>
          <td align="left">Desativar</td>
          <td align="left">Selecione essa opção para desativar um filtro.</td>
          <td align="left">Depois de incluir um filtro, se desejar ocultar entradas para um valor de campo, clique em **desativar**.</td>
        </tr>
        <tr>
          <td align="left">Pin</td>
          <td align="left">Selecione essa opção para persistir o filtro nas páginas do Kibana.</td>
          <td align="left">É possível fixar um filtro na página *Descobrir*, na página *Visualizar* ou na página *Painel*.</td>
        </tr>
        <tr>
          <td align="left">Comutar</td>
          <td align="left">Selecione essa opção para alternar um filtro.</td>
          <td align="left">Por padrão, as entradas que correspondem a um filtro são exibidas. Para exibir entradas que não correspondem, alterne o filtro.</td>
        </tr>
        <tr>
          <td align="left">Remover</td>
          <td align="left">Selecione essa opção para remover um filtro.</td>
          <td align="left"></td>
        </tr>
      </tbody>
    </table>

	
## Filtrando seus logs do app CF por origem
{:#filter_logs_by_source}

Conclua as etapas a seguir para procurar por entradas que incluam uma origem de log específica:

1. Consulte a página Descobrir do Kibana para ver qual subconjunto de seus dados é exibido. Para obter mais informações, consulte [Identificando os dados que são exibidos em sua página Descobrir do Kibana](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data).

2. Na *Lista de campos*, selecione o campo **source_id**.

3. Para incluir um filtro que procure entradas que incluam um source_id específico, escolha o botão de ampliação ![Botão Lupa no modo inclusivo](images/include_field_icon.jpg "Botão Lupa no inclusivo") para esse valor.

    Para obter uma lista de origens de log que estão disponíveis para apps CF, consulte
[Origens de log para apps CF](/docs/services/CloudLogAnalysis/cfapps/logging_cf_apps.html#logging_bluemix_cf_apps_log_sources).

    Para incluir um filtro que procure entradas que não incluam um source_id específico, escolha o botão de ampliação ![Botão Lupa no modo exclusivo](images/exclude_field_icon.jpg "Botão Lupa no modo exclusivo") para o valor.
    


## Filtrando seus logs por tipo de log
{:#filter_logs_by_log_type}

Conclua as etapas a seguir para procurar por entradas que incluam um tipo de log específico:

1. Consulte a página Descobrir do Kibana para ver qual subconjunto de seus dados é exibido. Para obter mais informações, consulte [Identificando os dados que são exibidos em sua página Descobrir do Kibana](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data).

2. Na *Lista de campos*, selecione o campo **tipo**.

3. Para incluir um filtro que procure um tipo de log específico, escolha o botão de ampliação ![Botão Lupa no modo inclusivo](images/include_field_icon.jpg "Botão Lupa no modo inclusivo") para o tipo de log que você deseja analisar.

    Para incluir um filtro que procure entradas que não incluam um tipo de log específico, escolha o botão de ampliação ![Botão Lupa no modo exclusivo](images/exclude_field_icon.jpg "Botão Lupa no exclusivo") para o valor.



## Filtrando seus logs por ID da instância
{:#filter_logs_by_instance_id}

Conclua as etapas a seguir para visualizar e filtrar seus logs por ID da instância no painel do Kibana:

1. Consulte a página Descobrir do Kibana para ver qual subconjunto de seus dados é exibido. Para obter mais informações, consulte [Identificando os dados que são exibidos em sua página Descobrir do Kibana](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data).

2. Na *Lista de campos*, selecione um dos campos a seguir para procurar por um ID da instância específico:

    * **instance_ID**: esse campo lista os IDs de instância diferentes que estão
disponíveis no log para um aplicativo Cloud Foundry. 
    * **instance**: esse campo lista os GUIDs diferentes de todas as instâncias
para um grupo de contêiner. 
	* **docker.container_id_str**: esse campo lista os diferentes IDs do contêiner para contêineres implementados em uma infraestrutura do Kubernetes.
   
3. Para incluir um filtro que procure um tipo de log específico, escolha o botão de ampliação ![Botão Lupa no modo inclusivo](images/include_field_icon.jpg "Botão Lupa no modo inclusivo") para o tipo de log que você deseja analisar.

    Para incluir um filtro que procure entradas que não incluam um ID de instância específico, escolha o botão de ampliação ![Botão Lupa no modo exclusivo](images/exclude_field_icon.jpg "Botão Lupa no exclusivo") para o valor.



## Filtrando seus logs do app CF por tipo de mensagem
{:#filter_cf_logs_by_msg_type}

Conclua as etapas a seguir para procurar por entradas que incluam um tipo de mensagem específico:

1. Consulte a página Descobrir do Kibana para ver qual subconjunto de seus dados é exibido. Para obter mais informações, consulte [Identificando os dados que são exibidos em sua página Descobrir do Kibana](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data).

2. Na *Lista de campos*, selecione o campo **message_type**.

    Os tipos de campo disponíveis são mostrados. 

3. Para incluir um filtro que procure entradas que incluam um *message_type* específico, escolha o botão de ampliação ![Botão Lupa no modo inclusivo](images/include_field_icon.jpg "Botão Lupa no inclusivo") para esse valor.

    Para incluir um filtro que procure entradas que não incluam um *message_type* específico, escolha o botão de ampliação ![Botão Lupa no modo exclusivo](images/exclude_field_icon.jpg "Botão Lupa no modo exclusivo") para o valor.
    
 
	

## Filtrando seus logs para um texto específico em um valor de campo
{:#filter_logs_spec_text}

Visualize e procure por entradas que incluam um texto específico no valor de um campo. 

**Nota:** só é possível executar uma procura de texto livre de campos de sequência analisados pelo analisador Elasticsearch. 
    
Quando o Elasticsearch analisa o valor de um campo de sequência, ele divide o texto em limites de
palavras, conforme definido pelo Consórcio de Unicode, remove a pontuação e coloca todas as
palavras em letras minúsculas.
    
Conclua as etapas a seguir para procurar por entradas que incluam texto específico em um valor de campo:

1. Consulte a página Descobrir do Kibana para ver qual subconjunto de seus dados é exibido. Para obter mais informações, consulte [Identificando os dados que são exibidos em sua página Descobrir do Kibana](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data).

2. Identifique os campos que são analisados no ElasticSearch por padrão.

    Para exibir a lista completa de campos analisados que estão disponíveis para procura e filtragem
de dados de log,
[recarregue a
lista de campos](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_reload_fields). Em seguida, na Lista de campos que está disponível na página Descobrir,
conclua as etapas a seguir:
    
    1. Clique no ícone de configuração o ![ícone de Configuração](images/configure_icon.jpg "ícone de configuração"). A seção **Campos selecionados**, na qual é possível
filtrar campos, é exibida.

    2. Para identificar os campos que estiverem analisados, selecione **Sim** para o
campo de procura **Analisados**.

        A lista de campos analisados é mostrada.
    
    3. Verifique se o campo no qual deseja procurar por texto livre é um campo que é analisado pelo
ElasticSearch por padrão.
    
3. Se o campo for analisado, modifique a consulta para procurar por entradas nos logs que incluam esse
texto livre como parte do valor de um campo.

    
**Exemplo**

Se você ativar o Kibana para um aplicativo Cloud Foundry (CF) na IU do
{{site.data.keyword.Bluemix}} e desejar procurar por uma mensagem específica que inclua o ID de
mensagem *CWWKT0016I:*, modifique a procura para incluir o texto livre.
    
1. Verifique a consulta de procura que é carregada e os dados que são exibidos na página Descobrir.
       
2. Para procurar o ID de mensagem *CWWKT0016I*, modifique a consulta de procura na **Barra de procura** e clique em **Enter**.
    
    Por exemplo, insira o texto a seguir na barra de Procura para um app CF com o ID *f52f6016-3aab-4b5c-aa2e-5493747cb978*:

	`<pre class="pre">application_id:f52f6016-3aab-4b5c-aa2e-5493747cb978 AND message:"CWWKT0016I:" </pre>`
        
          
A tabela mostra as entradas para seu app CF no qual o texto *CWWKT0016I* faz parte do valor
no campo *mensagem*.
    
 	
        

## Configurando um filtro de tempo
{: #set_time_filter}

Visualize e filtre logs dentro de um período configurando o *Selecionador de horário*.

É possível configurar o *Selecionador de tempo* na página Descobrir. Por padrão, ele é
configurado para os últimos 15 minutos. 

Conclua as etapas a seguir para procurar por entradas que incluam um tempo específico:

1. Na barra de menus da página Descobrir, clique no Selecionador de horário ![Selecionador de horário](images/time_picker_icon.jpg "Selecionador de horário").

2. Configure o intervalo de tempo. 

    É possível definir qualquer um dos seguintes tipos de intervalos de tempo:
    
    * Rápido: estes são os intervalos de tempo predefinidos que incluem os usos mais comuns de
intervalos de tempo Relativo e Absoluto, por exemplo, *Hoje* e *Este mês*. 
       
    * Relativo: estes são os intervalos de tempo em que é possível especificar a data e hora de início
e a data e hora de encerramento. É possível arredondar por hora.
    
    * Absoluto: estes são os intervalos de tempo entre uma data de início e uma data de encerramento.
    

Depois de configurar um intervalo de tempo, os dados mostrados no Kibana corresponderão às entradas dentro
desse intervalo de tempo.








