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


# Ativando a coleta automática de logs de cluster
{: #containers_kube_other_logs}

Para ser capaz de visualizar e analisar os logs de cluster no serviço {{site.data.keyword.loganalysisshort}}, deve-se configurar seu cluster para encaminhar os logs para o serviço {{site.data.keyword.loganalysisshort}}. 
{:shortdesc}

## Etapa 1: Verificar permissões para seu ID do usuário
{: step1}

Seu ID do usuário deve ter as permissões a seguir para que você possa incluir uma configuração de criação de log no cluster:

* Política IAM para o {{site.data.keyword.containershort}} com permissões de **Visualizador**.
* Política IAM para a instância de cluster com permissões de **Administrador** ou **Operador**.

Para verificar se o seu ID de usuário tem essas políticas do IAM, conclua as etapas a seguir:

**Nota:** somente o proprietário da conta ou usuários com permissões para designar políticas podem executar esta etapa.

1. Efetue login no console do {{site.data.keyword.Bluemix_notm}}. Abra um navegador da web e ative o painel do {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](http://bluemix.net){:new_window}
	
	Depois de efetuar login com seu ID de usuário e senha, a UI do {{site.data.keyword.Bluemix_notm}} é aberta.

2. Na barra de menus, clique em **Gerenciar > Conta > Usuários**.  A janela *Usuários* exibe uma lista de usuários com seus endereços de e-mail para a conta selecionada atualmente.
	
3. Selecione o userID e verifique se o ID do usuário tem ambas as políticas.




## Etapa 2: configurar o contexto do cluster.
{: #step2}

Conclua as etapas a seguir:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Inicialize o plug-in do serviço {{site.data.keyword.loganalysisshort}}.

	```
	ibmcloud ks init
	```
	{: codeblock}

3. Configure seu contexto de terminal para o cluster.
    
	```
	ibmcloud ks cluster-config ClusterName
	```
	{: codeblock}

    A saída de execução desse comando fornece o comando que deve ser executado no terminal para configurar o caminho para o arquivo de configuração. Por exemplo, para um cluster chamado *MyCluster*:

	```
	export KUBECONFIG=/Users/ibm/.bluemix/plugins/container-service/clusters/MyCluster/kube-config-hou02-MyCluster.yml
	```
	{: codeblock}

4. Copie e cole o comando para configurar a variável de ambiente em seu terminal e, em seguida, pressione **Enter**.



## Etapa 3: configurar seu cluster
{: step3}

É possível escolher quais logs de cluster serão encaminhados para o serviço {{site.data.keyword.loganalysisshort}}. 

* Para ativar a coleção de logs automática e encaminhar stdout e stderr, veja [Ativando a coleção de logs automática e encaminhando logs do contêiner](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#containers).
* Para ativar a coleção automática de logs e o encaminhamento de logs do aplicativo, veja [Ativando a coleção automática de logs e o encaminhamento de logs do aplicativo](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#apps).
* Para ativar a coleção automática de logs e o encaminhamento de logs do trabalhador, veja [Ativando a coleção automática de logs e o encaminhamento de logs do trabalhador](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#workers).
* Para ativar a coleção automática de logs e o encaminhamento dos logs do componente do sistema do Kubernetes, veja [Ativando a coleção automática de logs e o encaminhamento dos logs do componente do sistema do Kubernetes](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#system).
* Para ativar a coleção automática de logs e o encaminhamento dos logs de controlador de ingresso do Kubernetes, veja [Ativando a coleção automática de logs e o encaminhamento dos logs de controlador de ingresso do Kubernetes](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#controller).



## Etapa 4: Configurar permissões para o proprietário da chave do {{site.data.keyword.containershort_notm}}
{: #step4}


O proprietário da chave do {{site.data.keyword.containershort}} precisa das políticas do IAM a seguir:

* Política IAM para o {{site.data.keyword.containershort}} com a função de **Administrador**.
* Política IAM para o serviço {{site.data.keyword.loganalysisshort}} com a função de **Administrador**.

Conclua as etapas a seguir: 

1. Efetue login no console do {{site.data.keyword.Bluemix_notm}}. Abra um navegador da web e ative o painel do {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](http://bluemix.net){:new_window}
	
	Depois de efetuar login com seu ID de usuário e senha, a UI do {{site.data.keyword.Bluemix_notm}} é aberta.

2. Na barra de menus, clique em **Gerenciar > Conta > Usuários**.  A janela *Usuários* exibe uma lista de usuários com seus endereços de e-mail para a conta selecionada atualmente.
	
3. Selecione o userID para o proprietário da chave do {{site.data.keyword.containershort_notm}} e verifique se o ID do usuário tem ambas as políticas.


Quando você encaminha logs para um domínio de espaço, deve-se também conceder permissões do Cloud Foundry (CF) para o proprietário da chave do {{site.data.keyword.containershort}} na organização e no espaço. O proprietário da chave precisa da função *orgManager* para a organização e *SpaceManager* ou *Developer* para o espaço.

Conclua as etapas a seguir:

1. Identifique o usuário na conta que é o proprietário da chave do {{site.data.keyword.containershort}}. Em um terminal, execute o comando a seguir:

    ```
    ibmcloud ks api-key-info ClusterName
    ```
    {: codeblock}
    
    em que *ClusterName* é o nome do cluster.
    
2. Verifique se o usuário que é identificado como o dono da chave do {{site.data.keyword.containershort}} tem a função *orgManager* para a organização e *SpaceManager* e *Developer* para o espaço.

    Efetue login no console do {{site.data.keyword.Bluemix_notm}}. Abra um navegador da web e ative o painel do {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](http://bluemix.net){:new_window} Após você efetuar login com seu ID do usuário e senha, a UI do {{site.data.keyword.Bluemix_notm}} será aberta.

    Na barra de menus, clique em **Gerenciar > Conta > Usuários**.  A janela *Usuários* exibe uma lista de usuários com seus endereços de e-mail para a conta selecionada atualmente.
	
    Selecione o ID do usuário e verifique se o usuário tem a função *orgManager* para a organização e *SpaceManager* ou *Developer* para o espaço.
 
3. Se o usuário não tiver as permissões corretas, conclua as etapas a seguir:

    1. Conceda ao usuário as permissões a seguir: função *orgManager* para a organização e *SpaceManager* e *Developer* para o espaço. Para obter mais informações, veja [Concedendo a um usuário permissões para visualizar logs de espaço usando a UI do IBM Cloud](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_space).
    
    2. Atualize a configuração de criação de log. Execute o comando a seguir:
    
        ```
        ibmcloud ks logging-config-refresh ClusterName
        ```
        {: codeblock}
        
        em que *ClusterName* é o nome do cluster.
  




## Ativando a coleção automática de logs e o encaminhamento de logs do contêiner 
{: #containers}

Execute o comando a seguir para enviar arquivos de log*stdout* e *stderr* para o serviço do {{site.data.keyword.loganalysisshort}}:

```
ibmcloud ks logging-config-create ClusterName --logsource container --namespace '*' --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

Em que 

* *ClusterName* é o nome do cluster.
* *EndPoint* é a URL para o serviço de criação de log na região na qual o serviço do {{site.data.keyword.loganalysisshort}} é provisionado. Para obter uma lista de terminais, veja [Terminais](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
* *OrgName* é o nome da organização na qual o espaço está disponível.
* *SpaceName* é o nome do espaço no qual o serviço é provisionado. {{site.data.keyword.loganalysisshort}}


Por exemplo, para criar uma configuração de criação de log que encaminhe logs stdout e stderr para o domínio de contas na região alemã, execute o comando a seguir:

```
ibmcloud ks logging-config-create MyCluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}

Para criar uma configuração de criação de log que encaminhe logs stdout e stderr para um domínio de espaço na região alemã, execute o comando a seguir:

```
ibmcloud ks logging-config-create MyCluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org MyOrg --space MySpace
```
{: screen}



## Ativando a coleção automática de logs e o encaminhamento de logs do aplicativo 
{: #apps}

Execute o comando a seguir para enviar os arquivos de log */var/log/apps/**/.log* e */var/log/apps/*/.err* para o serviço {{site.data.keyword.loganalysisshort}}:

```
ibmcloud ks logging-config-create ClusterName --logsource application --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName --app-containers --app-paths
```
{: codeblock}

Em que 

* *ClusterName* é o nome do cluster.
* *EndPoint* é a URL para o serviço de criação de log na região na qual o serviço do {{site.data.keyword.loganalysisshort}} é provisionado. Para obter uma lista de terminais, veja [Terminais](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
* *OrgName* é o nome da organização na qual o espaço está disponível.
* *SpaceName* é o nome do espaço no qual o serviço é provisionado. {{site.data.keyword.loganalysisshort}}
* *app-containers* é um parâmetro opcional que pode ser configurado para definir uma lista de contêineres que você deseja observar. Esses contêineres são os únicos de onde os logs serão encaminhados para o {{site.data.keyword.loganalysisshort}}. É possível configurar um ou mais contêineres separando-os com vírgulas.
* *app-paths* define os caminhos dentro de contêineres que você deseja observar. É possível configurar um ou mais caminhos separando-os com vírgulas. Os caracteres curinga como '/var/log/* .log' são aceitos. 

Por exemplo, para criar uma configuração de criação de log que encaminhe logs do aplicativo para um domínio de espaço na região alemã, execute o comando a seguir:

```
ibmcloud ks logging-config-create MyCluster --logsource application --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org MyOrg --space MySpace --app-paths /var/log/*.log
```
{: screen}

Por exemplo, para criar uma configuração de criação de log que encaminhe logs do aplicativo para o domínio de contas na região alemã, execute o comando a seguir:

```
ibmcloud ks logging-config-create MyCluster --logsource application --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --app-paths /var/log/*.log
```
{: screen}



## Ativando a coleção automática de logs e o encaminhamento de logs de trabalhador 
{: #workers}


Execute o comando a seguir para enviar os arquivos de log */var/log/syslog* e */var/log/auth.log* para o serviço {{site.data.keyword.loganalysisshort}}:

```
ibmcloud ks logging-config-create ClusterName --logsource worker --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

Em que 

* *ClusterName* é o nome do cluster.
* *EndPoint* é a URL para o serviço de criação de log na região na qual o serviço do {{site.data.keyword.loganalysisshort}} é provisionado. Para obter uma lista de terminais, veja [Terminais](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
* *OrgName* é o nome da organização na qual o espaço está disponível.
* *SpaceName* é o nome do espaço no qual o serviço é provisionado. {{site.data.keyword.loganalysisshort}}



Por exemplo, para criar uma configuração de criação de log que encaminhe logs do trabalhador para um domínio de espaço na região alemã, execute o comando a seguir:

```
ibmcloud ks logging-config-create MyCluster --logsource worker  --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

Por exemplo, para criar uma configuração de criação de log que encaminhe logs do trabalhador para o domínio de contas na região alemã, execute o comando a seguir:

```
ibmcloud ks logging-config-create MyCluster --logsource worker  --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}



## Ativando a coleção automática de logs e o encaminhamento dos logs de componente do sistema do Kubernetes
{: #system}

Execute o comando a seguir para enviar os arquivos de log */var/log/kubelet.log* e */var/log/kube-proxy.log* para o serviço {{site.data.keyword.loganalysisshort}}:

```
ibmcloud ks logging-config-create ClusterName --logsource kubernetes --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

Em que 

* *ClusterName* é o nome do cluster.
* *EndPoint* é a URL para o serviço de criação de log na região na qual o serviço do {{site.data.keyword.loganalysisshort}} é provisionado. Para obter uma lista de terminais, veja [Terminais](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
* *OrgName* é o nome da organização na qual o espaço está disponível.
* *SpaceName* é o nome do espaço no qual o serviço é provisionado. {{site.data.keyword.loganalysisshort}}



Por exemplo, para criar uma configuração de criação de log que encaminhe logs de componente do sistema do Kubernetes para um domínio de espaço na região alemã, execute o comando a seguir:

```
ibmcloud ks logging-config-create MyCluster --logsource kubernetes --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

Por exemplo, para criar uma configuração de criação de log que encaminhe logs de componente do sistema do Kubernetes para o domínio de contas na região alemã, execute o comando a seguir:

```
ibmcloud ks logging-config-create MyCluster --logsource kubernetes --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}



## Ativando a coleção automática de logs e o encaminhamento dos logs de controlador de ingresso do Kubernetes
{: #controller}

Execute o comando a seguir para enviar os arquivos de log */var/log/alb/ids/.log*, */var/log/alb/ids/.err*, */var/log/alb/customerlogs/.log* e /var/log/alb/customerlogs/.err* para o serviço {{site.data.keyword.loganalysisshort}}:

```
ibmcloud ks logging-config-create ClusterName --logsource ingress --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName
```
{: codeblock}

Em que 

* *ClusterName* é o nome do cluster.
* *EndPoint* é a URL para o serviço de criação de log na região na qual o serviço do {{site.data.keyword.loganalysisshort}} é provisionado. Para obter uma lista de terminais, veja [Terminais](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
* *OrgName* é o nome da organização na qual o espaço está disponível.
* *SpaceName* é o nome do espaço no qual o serviço é provisionado. {{site.data.keyword.loganalysisshort}}



Por exemplo, para criar uma configuração de criação de log que encaminhe logs do controlador de ingresso para um domínio de espaço na região alemã, execute o comando a seguir:

```
ibmcloud ks logging-config-create MyLoggingDemoCluster --logsource ingress --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

Por exemplo, para criar uma configuração de criação de log que encaminhe logs do controlador de ingresso para o domínio de contas na região alemã, execute o comando a seguir:

```
ibmcloud ks logging-config-create MyLoggingDemoCluster --logsource ingress --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091  
```
{: screen}



