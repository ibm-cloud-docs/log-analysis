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


# Analisar logs no Kibana para um app que é implementado em um cluster do Kubernetes
{: #container_logs}
Use esse tutorial para aprender como configurar um cluster para encaminhar logs para o serviço {{site.data.keyword.loganalysisshort}} no {{site.data.keyword.Bluemix_notm}}.
{:shortdesc}


## Objetivos
{: #objectives}

1. Configurar as configurações de criação de log em um cluster. 
2. Procurar e analisar logs do contêiner para um app implementado em um cluster do Kubernetes no {{site.data.keyword.Bluemix_notm}}.

Esse tutorial percorre as etapas necessárias para obter o seguinte cenário de ponta a ponta funcionando no {{site.data.keyword.Bluemix_notm}}: provisionando um cluster, configurando o cluster para enviar logs para o serviço {{site.data.keyword.loganalysisshort}} no {{site.data.keyword.Bluemix_notm}}, implementando um app no cluster e usando o Kibana para visualizar e filtrar logs do contêiner para esse cluster.


**Nota:** para concluir esse tutorial, deve-se concluir os pré-requisitos e os tutoriais vinculados nas diferentes etapas.


## Pré-requisitos
{: #prereq}

1. Seja um membro ou um proprietário de uma conta do {{site.data.keyword.Bluemix_notm}} com permissões para criar clusters padrão do Kubernetes, implementar apps nos clusters e consultar os logs no {{site.data.keyword.Bluemix_notm}} para análise avançada no Kibana.

    Seu ID de usuário do {{site.data.keyword.Bluemix_notm}} deve ter as seguintes políticas designadas:
    
    * Uma política do IAM para o {{site.data.keyword.containershort}} com permissões de *editor*, *operador* ou *administrador*.
    * Uma função do CF para o espaço no qual o serviço {{site.data.keyword.loganalysisshort}} é provisionado com permissões de *desenvolvedor*.
    
    Para obter mais informações, veja [Designar uma política do IAM a um usuário por meio da UI do IBM Cloud](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_account) e [Concedendo a um usuário permissões para visualizar logs de espaço usando a UI do IBM Cloud](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space).

2. Tenha uma sessão de terminal da qual seja possível gerenciar o cluster do Kubernetes e implementar apps por meio da linha de comandos. Os exemplos neste tutorial são fornecidos para um sistema Ubuntu Linux.

3. Instale as CLIs para que funcionem com o {{site.data.keyword.containershort}} e o {{site.data.keyword.loganalysisshort}} no sistema Ubuntu.

    * Instale a CLI do {{site.data.keyword.Bluemix_notm}}. Instale a CLI do {{site.data.keyword.containershort}} para criar e gerenciar os clusters do Kubernetes no {{site.data.keyword.containershort}} e implementar apps conteinerizados no cluster. Para obter mais informações, veja [Instalando a CLI do {{site.data.keyword.Bluemix_notm}}](/docs/cli/index.html#overview).
    
    * Instale a CLI do {{site.data.keyword.loganalysisshort}}. Para obter mais informações, veja [Configurando a CLI do Log Analysis (plug-in do IBM Cloud)](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#config_log_collection_cli).
    
4. Tenha acesso a um espaço chamado **dev** em sua conta na região sul dos EUA. 

    Os logs disponíveis no cluster serão configurados para serem encaminhados para o domínio de espaço associado a este espaço. 
    
    Nesse espaço, você provisionará o serviço {{site.data.keyword.loganalysisshort}}.
    
    Deve-se ter permissões de **desenvolvedor** nesse espaço para que seja possível provisionar o serviço {{site.data.keyword.loganalysisshort}}.
    
    No tutorial, o nome da organização usado é **MyOrg**.

    
 

## Etapa 1: Provisionar um cluster do Kubernetes
{: #step25}

Conclua as etapas a seguir:

1. Crie um cluster padrão do Kubernetes.

   Para obter mais informações, consulte [Criando Clusters](/docs/containers/cs_tutorials.html#cs_cluster_tutorial).

2. Configure o contexto do cluster em um terminal. Após o contexto ser configurado, é possível gerenciar o cluster do Kubernetes e implementar o aplicativo no cluster do Kubernetes.

    Efetue login na região, na organização e no espaço no {{site.data.keyword.Bluemix_notm}} que está associado ao cluster criado. Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

	Inicialize o plug-in do serviço {{site.data.keyword.containershort}}.

	```
	ibmcloud cs init
	```
	{: codeblock}

    Configure seu contexto de terminal para o cluster.
    
	```
	ibmcloud cs cluster-config MyCluster
	```
	{: codeblock}

    A saída de execução desse comando fornece o comando que deve ser executado no terminal para configurar o caminho para o arquivo de configuração. Por exemplo:

	```
	export KUBECONFIG=/Users/ibm/.bluemix/plugins/container-service/clusters/MyCluster/kube-config-hou02-MyCluster.yml
	```
	{: codeblock}

    Copie e cole o comando para configurar a variável de ambiente em seu terminal e, em seguida, pressione **Enter**.



## Etapa 2: Configurar seu cluster para encaminhar logs automaticamente para o serviço {{site.data.keyword.loganalysisshort}}
{: #step26}

Quando o app é implementado, os logs são coletados automaticamente pelo {{site.data.keyword.containershort}}. No entanto, os logs não são encaminhados automaticamente para o serviço {{site.data.keyword.loganalysisshort}}. Deve-se criar 1 ou mais configurações de criação de log em seu cluster que definam:

* Para onde os logs devem ser encaminhados. É possível encaminhar logs para o domínio de contas ou para um domínio de espaço.
* Quais logs são encaminhados para o serviço {{site.data.keyword.loganalysisshort}} para análise.


Antes de definir as configurações de criação de log, verifique suas definições de configuração de criação de log atuais no cluster. Execute o comando a seguir:

```
$ibmcloud cs logging-config-get ClusterName
```
{: codeblock}

em que *ClusterName* é o nome de seu cluster.

Por exemplo, as configurações de criação de log definidas para o cluster *mycluster* são as seguintes: 

```
$ ibmcloud cs logging-config-get mycluster
Retrieving cluster mycluster logging configurations...
OK
Id                                     Source       Namespace   Host                                Port   Org            Space   Protocol   Paths   
13ded2c0-83f5-4cc5-8de7-1e34e1287f34   worker       -           ingest.logging.ng.bluemix.net       9091   Demo_Org       dev     ibm        /var/log/syslog,/var/log/auth.log   
ae249c04-a3a9-4c29-a890-22d8da7bd1b2   container    *           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        -   
31739fc1-42e2-4b66-ac57-6a32091c257a   ingress      -           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        /var/log/alb/ids/*.log,/var/log/alb/ids/*.err,/var/log/alb/customerlogs/*.log,/var/log/alb/customerlogs/*.err   
6b8cfe89-4959-448d-898b-c3b0584eca71   kubernetes   -           ingest-eu-fra.logging.bluemix.net   9091   Demo_Org.      dev     ibm        /var/log/kubelet.log,/var/log/kube-proxy.log   

```
{: screen}

Para ver a lista de origens de log para as quais é possível definir uma configuração de criação de log, veja [Origens de log](/docs/services/CloudLogAnalysis/containers/containers_kubernetes.html#log_sources).


### Configurar seu cluster para encaminhar logs stderr e stdout para o serviço {{site.data.keyword.loganalysisshort}}
{: #containerstd}


Conclua as etapas a seguir para enviar logs stdout e stderr para um domínio de espaço, em que o nome da organização é *MyOrg* e o nome do espaço é *dev* na região sul dos EUA:

1. Verifique se o seu ID do usuário tem permissões para incluir uma configuração de cluster. Somente usuários com uma política do IAM para o {{site.data.keyword.containershort}} com permissões para gerenciar clusters podem ativar esse recurso. Qualquer uma das funções a seguir é necessária: *Administrador*, *Operador*

    Para verificar se o seu ID do usuário tem uma política do IAM designada para gerenciar clusters, conclua as etapas a seguir:
    
    1. Efetue login no console do {{site.data.keyword.Bluemix_notm}}. Abra um navegador da web e ative o painel do {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](http://bluemix.net){:new_window} Após você efetuar login com seu ID do usuário e senha, a UI do {{site.data.keyword.Bluemix_notm}} será aberta.

    2. Na barra de menus, clique em **Gerenciar > Conta > Usuários**.  A janela *Usuários* exibe uma lista de usuários com seus endereços de e-mail para a conta selecionada atualmente.
	
    3. Selecione o userID e verifique se o ID do usuário tem uma política para o {{site.data.keyword.containershort}}.

    Se você precisar de permissões, entre em contato com o proprietário da conta ou um administrador de conta. Somente o proprietário da conta ou usuários com permissões para designar políticas podem executar esta etapa.

2. Crie uma configuração de criação de log de cluster. Execute o comando a seguir para enviar arquivos de log*stdout* e *stderr* para o serviço do {{site.data.keyword.loganalysisshort}}:

    ```
    ibmcloud cs logging-config-create ClusterName --logsource container --namespace '*' --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    Em que 

    * *ClusterName* é o nome do cluster.
    * *EndPoint* é a URL para o serviço de criação de log na região na qual o serviço do {{site.data.keyword.loganalysisshort}} é provisionado. Para obter uma lista de terminais, veja [Terminais](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls).
    * *OrgName* é o nome da organização na qual o espaço está disponível.
    * *SpaceName* é o nome do espaço no qual o serviço é provisionado. {{site.data.keyword.loganalysisshort}}


Por exemplo, para criar uma configuração de criação de log que encaminhe logs stdout e stderr para o espaço dev na região sul dos EUA, execute o comando a seguir:

```
ibmcloud cs logging-config-create mycluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}




### Configurar seu cluster para encaminhar logs do trabalhador para o serviço {{site.data.keyword.loganalysisshort}}
{: #workerlogs }

Conclua as etapas a seguir para enviar logs do trabalhador para um domínio de espaço, em que o nome da organização é *MyOrg* e o nome do espaço é *dev* na região sul dos EUA:

1. Verifique se o seu ID do usuário tem permissões para incluir uma configuração de cluster. Somente usuários com uma política do IAM para o {{site.data.keyword.containershort}} com permissões para gerenciar clusters podem ativar esse recurso. Qualquer uma das funções a seguir é necessária: *Administrador*, *Operador*

    Para verificar se o seu ID do usuário tem uma política do IAM designada para gerenciar clusters, conclua as etapas a seguir:
    
    1. Efetue login no console do {{site.data.keyword.Bluemix_notm}}. Abra um navegador da web e ative o painel do {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](http://bluemix.net){:new_window} Após você efetuar login com seu ID do usuário e senha, a UI do {{site.data.keyword.Bluemix_notm}} será aberta.

    2. Na barra de menus, clique em **Gerenciar > Conta > Usuários**.  A janela *Usuários* exibe uma lista de usuários com seus endereços de e-mail para a conta selecionada atualmente.
	
    3. Selecione o userID e verifique se o ID do usuário tem uma política para o {{site.data.keyword.containershort}}.

    Se você precisar de permissões, entre em contato com o proprietário da conta ou um administrador de conta. Somente o proprietário da conta ou usuários com permissões para designar políticas podem executar esta etapa.

2. Crie uma configuração de criação de log de cluster. Execute o comando a seguir para enviar os arquivos de log */var/log/syslog* e */var/log/auth.log* para o serviço {{site.data.keyword.loganalysisshort}}:

    ```
    ibmcloud cs logging-config-create ClusterName --logsource worker --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    Em que 

    * *ClusterName* é o nome do cluster.
    * *EndPoint* é a URL para o serviço de criação de log na região na qual o serviço do {{site.data.keyword.loganalysisshort}} é provisionado. Para obter uma lista de terminais, veja [Terminais](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls).
    * *OrgName* é o nome da organização na qual o espaço está disponível.
    * *SpaceName* é o nome do espaço no qual o serviço é provisionado. {{site.data.keyword.loganalysisshort}}

    
Por exemplo, para criar uma configuração de criação de log que encaminhe logs do trabalhador para o domínio de espaço na região sul dos EUA, execute o comando a seguir:

```
ibmcloud cs logging-config-create mycluster --logsource worker  --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}



## Etapa 3: Conceder permissões ao usuário para ver logs em um domínio de espaço
{: #step33}

Para conceder a um usuário permissões para visualizar logs em um espaço, deve-se designar a esse usuário uma função do Cloud Foundry que descreva as ações que esse usuário pode executar com o serviço {{site.data.keyword.loganalysisshort}} no espaço. 

Conclua as etapas a seguir para conceder a um usuário permissões para trabalhar com o serviço {{site.data.keyword.loganalysisshort}}:

1. Efetue login no console do {{site.data.keyword.Bluemix_notm}}.

    Abra um navegador da web e ative o painel do {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](http://bluemix.net){:new_window}
	
	Depois de efetuar login com seu ID de usuário e senha, a UI do {{site.data.keyword.Bluemix_notm}} é aberta.

2. Na barra de menus, clique em **Gerenciar > Conta > Usuários**. 

    A janela *Usuários* exibe uma lista de usuários com seus endereços de e-mail para a conta selecionada atualmente.
	
3. Se o usuário é um membro da conta, selecione o nome do usuário na lista ou clique em **Gerenciar usuário** no menu *Ações*.

    Se o usuário não é um membro da conta, veja [Convidando usuários](/docs/iam/iamuserinv.html#iamuserinv).

4. Selecione **Acesso do Cloud Foundry** e, em seguida, selecione a organização.

    Os espaços disponíveis nessa organização estão listados.

5. Escolha o espaço. Em seguida, na ação de menu, selecione **Editar função de espaço**.

    Se não for possível ver o espaço para sul dos EUA, crie o espaço antes de continuar.

6. Selecione *desenvolvedor*.

    É possível selecionar 1 ou mais funções. 
    
    As funções válidas são: *Gerenciador*, *Desenvolvedor* e *Auditor*
	
7. Clique em **Salvar função**.


## Etapa 4: Conceder ao {{site.data.keyword.containershort_notm}} permissões de proprietário da chave
{: #step52}

Para que os logs do cluster sejam encaminhados para um espaço, o proprietário da chave do {{site.data.keyword.containershort_notm}} deve ter as permissões a seguir:

* Política do IAM para o serviço {{site.data.keyword.loganalysisshort}} com permissões de *Administrador*.
* Permissões do Cloud Foundry (CF) na organização e no espaço nos quais os logs devem ser encaminhados. O proprietário da chave do contêiner precisa da função *orgManager* para a organização e *SpaceManager* e *Developer* para o espaço.

Conclua as etapas a seguir:

1. Identifique o usuário na conta que é o proprietário da chave do {{site.data.keyword.containershort}}. Em um terminal, execute o comando a seguir:

    ```
    ibmcloud cs api-key-info ClusterName
    ```
    {: codeblock}
    
    em que *ClusterName* é o nome do cluster.

2. Verifique se o usuário que é identificado como o dono da chave do {{site.data.keyword.containershort}} tem a função *orgManager* para a organização e *SpaceManager* e *Developer* para o espaço.

    Efetue login no console do {{site.data.keyword.Bluemix_notm}}. Abra um navegador da web e ative o painel do {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](http://bluemix.net){:new_window} Após você efetuar login com seu ID do usuário e senha, a UI do {{site.data.keyword.Bluemix_notm}} será aberta.

    Na barra de menus, clique em **Gerenciar > Conta > Usuários**.  A janela *Usuários* exibe uma lista de usuários com seus endereços de e-mail para a conta selecionada atualmente.
	
    Selecione o ID do usuário e verifique se o usuário tem a função *orgManager* para a organização e *SpaceManager* e *Developer* para o espaço.

    Se o usuário não tiver as permissões corretas, conceda a ele as permissões a seguir: a função *orgManager* para a organização e *SpaceManager* e *Developer* para o espaço. Para obter mais informações, veja [Concedendo a um usuário permissões para visualizar logs de espaço usando a UI do IBM Cloud](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space).
    
3. Verifique se o usuário identificado como o proprietário da chave do {{site.data.keyword.containershort}} tem uma política do IAM para o serviço {{site.data.keyword.loganalysisshort}} com permissões de *Administrador*.

    Na barra de menus, clique em **Gerenciar > Conta > Usuários**.  A janela *Usuários* exibe uma lista de usuários com seus endereços de e-mail para a conta selecionada atualmente.
	
    Selecione o ID do usuário e verifique se ele tem o conjunto de políticas do IAM. 

    Se o usuário não tiver a política do IAM, veja [Designar uma política do IAM a um usuário por meio da UI do IBM Cloud](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_account).

4. Atualize a configuração de criação de log. Execute o comando a seguir:
    
    ```
    ibmcloud cs logging-config-refresh ClusterName
    ```
    {: codeblock}
        
    em que *ClusterName* é o nome do cluster.
	



## Etapa 5: Implementar um app de amostra no cluster do Kubernetes para gerar conteúdo em stdout
{: #step53}

Implemente e execute um aplicativo de amostra no cluster do Kubernetes. Conclua as etapas no tutorial a seguir para implementar o app de amostra: [Lição 1: Implementando apps de instância única em clusters do Kubernetes](/docs/containers/cs_tutorials_apps.html#cs_apps_tutorial_lesson1).

O app é Hello World Node.js:

```
var express = require('express')
var app = express()

app.get('/', function(req, res) {
  Res.send (' Hello world! Your app is up and running in a cluster!\n')
})
App.listen (8080, function () {
  console.log('Sample app is listening on port 8080.')
})
```
{: screen}

Nesse aplicativo de amostra, quando você testa seu app em um navegador, o app grava no stdout a mensagem a seguir: `Sample app is listening on port 8080.`






## Etapa 6: Visualizar dados do log no Kibana
{: #step6}

Conclua as etapas a seguir:

1. Ative o Kibana em um navegador. 

    Para obter mais informações sobre como ativar o Kibana, veja [Navegando para o Kibana de um navegador da web](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser).

    Para analisar dados do log para um cluster, deve-se acessar o Kibana na região Pública de nuvem na qual o cluster é criado. 
    
    Por exemplo, na região sul dos EUA, insira a URL a seguir para ativar o Kibana:
	
	```
	Https://logging.ng.bluemix.net/ 
	```
	{: codeblock}
	
    O Kibana é aberto.
    
    **NOTA:** verifique se você ativa o Kibana na região na qual está encaminhando os logs do cluster. Para obter informações sobre as URLs por região, veja [Registrando terminais](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#urls_kibana).
    	
2. Para visualizar dados do log que estão disponíveis no domínio de espaço, conclua as etapas a seguir:

    1. No Kibana, clique em seu ID do usuário. A visualização para configurar o espaço é aberta.
    
    2. Selecione a conta na qual o espaço está disponível. 
    
    3. Selecione o domínio a seguir: **espaço**
    
    4. Selecione a organização *MyOrg* na qual o espaço está disponível.
    
    5. Selecione o espaço *dev*.
    
    
3. Na página **Descobrir**, consulte os eventos que são exibidos. 
        
    Na seção *Campos disponíveis*, é possível ver a lista de campos que podem ser usados para definir novas consultas ou filtrar as entradas listadas na tabela exibida na página.
    
    A tabela a seguir lista alguns dos campos que podem ser usados para definir novas consultas de procura ao analisar logs de aplicativo. A tabela também inclui valores de amostra que correspondem ao evento que é gerado pelo aplicativo de amostra:
 
    <table>
              <caption>Tabela 2. Campos comuns para logs do contêiner </caption>
               <tr>
                <th align="center">Campo</th>
                <th align="center">descrição</th>
                <th align="center">Exemplo</th>
              </tr>
              <tr>
                <td>*ibm-containers.region_str*</td>
                <td>O valor desse campo corresponde à região do {{site.data.keyword.Bluemix_notm}} na qual a entrada de log é coletada.</td>
                <td>Us-south</td>
              </tr>
			  <tr>
                <td>*ibm-containers.account_id_str*</td>
                <td>ID da conta</td>
                <td></td>
              </tr>
			  <tr>
                <td>*Ibm-containers.cluster_id_str *</td>
                <td>ID do cluster.</td>
                <td></td>
              </tr>
              <tr>
                <td>*ibm-containers.cluster_name_str*</td>
                <td>ID do cluster</td>
                <td></td>
              </tr>
			  <tr>
                <td>*Kubernetes.namespace_name_str*</td>
                <td>Nome do namespace</td>
                <td>*default* é o valor padrão.</td>
              </tr>
              <tr>
                <td>*kubernetes.container_name_str*</td>
                <td>Nome do contêiner</td>
                <td>Olá a implementação mundial</td>
              </tr>
              <tr>
                <td>*kubernetes.labels.label_name*</td>
                <td>Os campos Rótulo são opcionais. É possível ter 0 ou mais rótulos. Cada rótulo inicia com o prefixo `kubernetes.labels.` Seguido pelo *label_name*. </td>
                <td>No app de amostra, é possível ver 2 rótulos: <br>* *kubernetes.labels.pod-template-hash_str* = 3355293961 <br>* *kubernetes.labels.run_str* =	hello-world-deployment  </td>
              </tr>
              <tr>
                <td>*Stream_str *</td>
                <td>Tipo de log.</td>
                <td>*stdout*, *stderr*</td>
              </tr>
        </table>
     
Para obter mais informações sobre outros campos de procura que sejam relevantes aos clusters do Kubernetes, veja [Procurando logs](/docs/services/CloudLogAnalysis/containers/containers_kubernetes.html#log_search).


## Etapa 7: Filtrar dados pelo nome do cluster do Kubernetes no Kibana
{: #step7}
    
Na tabela exibida na página *Descoberta*, é possível ver todas as entradas que estão disponíveis para análise. As entradas que estão listados correspondem à consulta de procura que é exibida na barra *Procurar*. Use um asterisco (*) para exibir todas as entradas dentro do período de tempo configurado para a página.
    
Por exemplo, para filtrar os dados pelo nome do cluster do Kubernetes, modifique a consulta da barra de *Procura*. Inclua um filtro com base no campo customizado *kubernetes.cluster_name_str*:
    
1. Na seção **Campos disponíveis**, selecione o campo *kubernetes.cluster_name_str*. Um subconjunto de valores disponíveis para o campo é exibido.    
    
2. Selecione o valor que corresponde ao cluster para o qual você deseja analisar logs. 
    
    Depois de selecionar o valor, um filtro é incluído na *Barra de procura* e a tabela exibe somente as entradas que correspondem aos critérios que você acabou de selecionar.     
   

**Nota:** 

Se não puder ver o nome do cluster, inclua um filtro para qualquer nome de cluster. Em seguida, selecione o símbolo de edição do filtro.    
    
A consulta a seguir exibe:
    
```
	{
        "query": {
          "Corresponder": {
            "kubernetes.cluster_name_str": {
              "query": "cluster1",
              "type": "phrase"
            }
          }
        }
      }
```
{: screen}

Substitua o nome do cluster (*cluster1*) pelo nome do cluster *mycluster* para o qual você deseja visualizar dados do log.
        
Se não for possível ver nenhum dado, tente mudar o filtro de tempo. Para obter mais informações, consulte [Configurando um filtro de tempo](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter).

Para obter mais informações, consulte [Filtrando logs no Kibana](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#filter_logs).


## Material de referência do {{site.data.keyword.containershort_notm}}
{: reference}

Comandos da CLI:

* [ ibmcloud cs api-key-info ](/docs/containers/cs_cli_reference.html#cs_api_key_info)
* [ ibmcloud cs logging-config-create ](/docs/containers/cs_cli_reference.html#cs_logging_create)
* [ ibmcloud cs logging-config-get ](/docs/containers/cs_cli_reference.html#cs_logging_get)
* [ibmcloud cs logging-config-update](/docs/containers/cs_cli_reference.html#cs_logging_update)
* [ ibmcloud cs logging-config-rm ](/docs/containers/cs_cli_reference.html#cs_logging_rm)
* [ ibmcloud cs logging-config-refresh ](/docs/containers/cs_cli_reference.html#cs_logging_refresh)

