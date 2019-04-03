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

# Definindo consultas de procura customizada
{:#define_search}

Na barra de procura da página Descobrir, é possível definir e salvar consultas de procura usando a
linguagem de consulta Lucene. Para cada procura, é possível aplicar filtros para refinar as
entradas que estiverem disponíveis para análise.
{:shortdesc}

Conclua as tarefas a seguir para definir uma procura customizada:

1. Ativar Kibana.

    Para apps Cloud Foundry (CF), veja [ativar o Kibana por meio do painel de um app CF](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-launch#launch_Kibana_from_cf_app).

	Para contêineres que são executados na infraestrutura gerenciada pelo {{site.data.keyword.Bluemix_notm}}, veja [ativar o Kibana no painel de um contêiner](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-launch#launch_Kibana_for_containers).
    
    Para todos os recursos em nuvem, por exemplo, contêineres executados em um cluster do Kubernetes, veja [ativar o Kibana por meio do navegador](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-launch#launch_Kibana_from_browser). 
	
	Ao acessar o Kibana, a procura padrão é aplicada. É possível ver os logs da lista de instâncias do recurso que está sendo consultado. É possível filtrar os logs para quaisquer ou todos os
recursos do {{site.data.keyword.Bluemix_notm}} nesse espaço.

2. Consulte a página Descobrir para ver qual subconjunto de seus dados é exibido. Para obter mais informações, consulte [Identificando os dados que são exibidos em sua página Descobrir do Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data). Em seguida, modifique a consulta padrão para
filtrar entradas.

    **Nota:** use a linguagem de consulta Lucene para definir sua consulta
customizada. Para obter mais informações, veja [Apache Lucene - Sintaxe do analisador sintático de consulta ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html){: new_window}
    
    Quando o Kibana é ativado na UI do {{site.data.keyword.Bluemix_notm}}, para modificar a consulta e definir múltiplos critérios de procura, é possível usar os termos lógicos **AND** e **OR**. Esses operadores devem estar em maiúsculas.    
    
    * Para procurar uma palavra-chave ou parte de uma palavra-chave, insira uma palavra seguida de um asterisco (*), que é um curinga; por exemplo, `Java*`. 
    * Para procurar uma frase específica, insira essa frase entre aspas duplas (" "); por exemplo, `"Java/1.8.0"`.
    * Para criar procuras mais complexas, é possível usar os termos lógicos AND e OR; por exemplo, `"Java/1.8.0" OR "Java/1.7.0"`.
    * Para procurar por um valor em um campo específico, insira sua procura no formato a seguir:
*log_field_name:search_term*; por exemplo, `instance_id:"1"`.
    * Para procurar por um intervalo de valores para um campo de log específico, insira sua procura no
formato a seguir: *log_field_name:[start_of_range TO end_of_range]*; por exemplo,
`instance_id:["1" TO "2"]`.

     Por exemplo, para um app CF, é possível criar uma consulta `application_id:9d222152-8834-4bab-8685-3036cd25931a AND instance_id:["0" TO "1"]` que liste entradas para as instâncias *0* e *1* somente. 

3. Salve a consulta para poder reutilizá-la posteriormente. Para obter mais
informações, consulte [Salvando uma procura](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#save_search1). 

**Nota:** se precisar excluir uma consulta, consulte
[Excluindo uma procura](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#delete_search).



## Excluindo uma Procura
{: #delete_search}

Para excluir uma procura, conclua as etapas a seguir na página Configurações:

1. Na página Configurações, selecione a guia **Objetos**.

2. Na guia **Procuras**, selecione a procura que deseja excluir.

3. Clique em **Excluir**.


## Exportando uma procura
{: #export_search}

Para exportar uma procura, conclua as etapas a seguir na página Configurações:

1. Na página Configurações, selecione a guia **Objetos**.

2. Na guia **Procuras**, selecione a procura que deseja exportar.

3. Clique em **Exportar**.

4. Salve o arquivo.

 
## Importando uma procura
{: #import_search}

Para importar uma procura, conclua as etapas a seguir na página Configurações:

1. Na página Configurações, selecione a guia **Objetos**.

2. Na guia **Procuras**, selecione **Importar**.

3. Selecione um arquivo e clique em **Abrir**.

A procura é incluída na lista de procuras.

## Atualizando o conteúdo de uma procura
{: #refresh_search}

Para atualizar manualmente o conteúdo de uma procura, é possível clicar na lupa que está disponível na
barra de procura. 

Para atualizar automaticamente os dados que são mostrados na página Descobrir, é possível configurar um
intervalo de atualização. O valor atual do intervalo de atualização é exibido na barra de menus da página
Descobrir. Por padrão, a atualização automática é configurada como **OFF**.

Conclua as etapas a seguir para configurar um intervalo de atualização:

1. Na página Descobrir, clique no **Filtro de tempo** que está disponível na barra
de menus.

2. Clique em **Atualização automática** ![Atualização automática](images/auto_refresh_icon.jpg "Atualização automática").

3. Escolha um intervalo de atualização na lista. 

**Nota**: após a ativação de um intervalo de atualização automática, será possível pausá-lo clicando no botão de pausa ![Pausa](images/auto_refresh_pause_icon.jpg "Pausa").


## Recarregando uma procura
{: #reload_search1}

Conclua as etapas a seguir para carregar uma procura salva:

1. Na barra de ferramentas da página Descobrir, clique no botão **Carregar procura** ![Carregar procura](images/load_icon.jpg "Carregar procura").

2. Selecione a procura que deseja carregar. 

## Iniciando uma nova procura
{: #k4_new_search}

Para iniciar uma nova procura, clique no botão **Nova procura** ![Nova procura](images/new_search_icon.jpg "Nova procura") na barra de ferramentas da página Descobrir.

## Salvando uma Procura 
{: #save_search1}

Considere as informações a seguir sobre como salvar procuras customizadas no Kibana:

* Ao salvar uma procura, a sequência de consultas de procura e o padrão de
índice selecionado atualmente são salvos.
* Ao abrir uma procura na página *Descobrir* e modificá-la, é possível escolher salvá-la com o mesmo nome ou salvar a procura customizada modificada com um nome diferente. Por padrão, o nome da procura fornecido é aquele que corresponde à procura customizada que você abriu inicialmente.

    * Para salvar a procura customizada modificada com o mesmo nome, clique em **Salvar**. Observe que a procura customizada original é sobrescrita. 
	
	* Para salvar a procura customizada modificada com um nome diferente, insira um novo nome no campo **Salvar procura** e, em seguida, clique em **Salvar**. 


Conclua as etapas a seguir para salvar uma procura atual na página Descobrir:

1. Na barra de ferramentas da página Descobrir, clique no botão **Salvar procura** ![Salvar procura](images/save_search_icon.jpg "Salvar procura").

2. Digite um nome para a procura.

    **Nota:** ao clicar em **Salvar**, não há nenhum aviso sobre sobrescrever, portanto, se você especifica um nome existente, o salvamento substitui essa versão sem nenhuma indicação.

3. Clique em **Salvar**. 
