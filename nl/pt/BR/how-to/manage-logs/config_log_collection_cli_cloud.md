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

# Configurando o {{site.data.keyword.loganalysisshort}} CLI
{: #config_log_collection_cli}

O serviço {{site.data.keyword.loganalysisshort}} inclui uma interface da linha de comandos (CLI) que pode ser usada para gerenciar logs na nuvem. É possível usar o plug-in {{site.data.keyword.Bluemix_notm}} para visualizar o status do log, fazer download de logs e configurar a política de retenção de log. A CLI oferece diferentes tipos de ajuda: ajuda geral para aprender sobre a CLI e os comandos suportados, ajuda de comando para aprender como usar um comando ou ajuda de subcomando para aprender como usar um subcomando para um comando.
{:shortdesc}


## Instalando o plug-in {{site.data.keyword.loganalysisshort}} por meio do repositório do {{site.data.keyword.Bluemix_notm}}
{: #install_cli_repo}

Para instalar a CLI do {{site.data.keyword.loganalysisshort}}, conclua as etapas a seguir:

1. Instale a CLI do {{site.data.keyword.Bluemix_notm}}.

   Para obter mais informações, veja [Instalando a CLI do {{site.data.keyword.Bluemix_notm}}](/docs/cli/index.html#overview).
   
2. Descubra o nome do plug-in no repositório. Execute o comando a seguir:

    ```
    ibmcloud plugin repo-plugins
    ```
    {: codeblock}
    
    O nome do plug-in é **logging-cli**.

3. Instale o plug-in {{site.data.keyword.loganalysisshort}}. Execute o comando a seguir:

    ```
    ibmcloud plugin install logging-cli -r Bluemix
    ```
    {: codeblock}
 
4. Verifique se o plug-in do {{site.data.keyword.loganalysisshort}} está instalado.
  
    Por exemplo, execute o comando a seguir para ver a lista de plug-ins que estão instalados:
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    A saída é semelhante ao seguinte:
   
    ```
    ibmcloud plugin list Listing installed plug-ins...

    Plugin Name Version   
    logging-cli 0.1.1   
    ```
    {: screen}


## Instalando o plug-in {{site.data.keyword.loganalysisshort}} por meio de um arquivo
{: #install_cli}

Para instalar a CLI do {{site.data.keyword.loganalysisshort}}, conclua as etapas a seguir:

1. Instale a CLI do {{site.data.keyword.Bluemix_notm}}.

   Para obter mais informações, veja [Instalando a CLI do {{site.data.keyword.Bluemix_notm}}](/docs/cli/index.html#overview).

2. Instale o plug-in {{site.data.keyword.loganalysisshort}}.

    * Para Linux, veja [Instalando o plug-in {{site.data.keyword.loganalysisshort}} no Linux](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_linux).
    * Para Windows, veja [Instalando o plug-in {{site.data.keyword.loganalysisshort}} no Windows](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_windows).
    * Para Mac OS X, veja [Instalando o plug-in {{site.data.keyword.loganalysisshort}} no Mac OS X](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_mac).
 
3. Verifique a instalação do plug-in da CLI.
  
    Por exemplo, verifique a versão do plug-in. Execute o comando a seguir:
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    A saída é semelhante ao seguinte:
   
    ```
    ibmcloud plugin list Listing installed plug-ins...

    Plugin Name Version   
    logging-cli 0.1.1   
    ```
    {: screen}
 


## Instalando o plug-in Log Analysis no Linux por meio de um arquivo
{: #install_cli_linux}

Conclua as etapas a seguir para instalar o plug-in Coleção de logs no Linux:

1. Instale o plug-in.

    Faça download da liberação mais recente do plug-in da CLI do serviço {{site.data.keyword.loganalysisshort}} (IBM-Logging) na [página CLI do {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins). 
	
	* Selecione o valor de plataforma: **linux64**. 
	
	* Clique em **Salvar arquivo**. 
    
2. Instale o plug-in. Execute o comando a seguir:
        
    ```
    ibmcloud plugin install -f logging-cli-linux-amd64-0.1.1
    ```
    {: codeblock}




## Instalando o plug-in Log Analysis no Windows por meio de um arquivo
{: #install_cli_windows}

Conclua as etapas a seguir para instalar o plug-in Coleção de logs no Windows:

1. Faça download da liberação mais recente do plug-in da CLI do serviço {{site.data.keyword.loganalysisshort}} (IBM-Logging) na [página CLI do {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins). 
	
	1. Selecione o valor de plataforma: **win64**. 
	2. Clique em **Salvar arquivo**.  
    
2. Instale o plug-in. Execute o comando a seguir:
        
    ```
    ibmcloud plugin install -f logging-cli-windows-amd64-0.1.1.exe
    ```
    {: codeblock}

	

## Instalando o plug-in Log Analysis no Mac OS X por meio de um arquivo
{: #install_cli_mac}

Conclua as etapas a seguir para instalar o plug-in Coleção de logs no Mac OS X:

1. Faça download da liberação mais recente do plug-in da CLI do serviço {{site.data.keyword.loganalysisshort}} (IBM-Logging) na [página CLI do {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins). 
	
	1. Selecione o valor de plataforma: **osx**. 
	2. Clique em **Salvar arquivo**.  
    
2. Altere as permissões do arquivo. Execute o comando a seguir:

    ```
    Chmod u + x logging-cli-darwin-amd64-0.1.1
    ```
     {: codeblock}

3. Instale o plug-in. Execute o comando a seguir:
        
    ```
    ibmcloud plugin install -f logging-cli-darwin-amd64-0.1.1
    ```
    {: codeblock}

	
	
## Desinstalando a CLI de Análise do log
{: #uninstall_cli}

Para desinstalar a CLI de criação de log, exclua o plug-in.
{:shortdesc}

Conclua as etapas a seguir para desinstalar a CLI do serviço {{site.data.keyword.loganalysisshort}}:

1. Verifique a versão do plug-in da CLI de criação de log que está instalada.
  
    Por exemplo, verifique a versão do plug-in. Execute o comando a seguir:
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    A saída é semelhante ao seguinte:
   
    ```
    ibmcloud plugin list Listing installed plug-ins...

    Plugin Name Version   
    logging-cli 0.1.1   
    ```
    {: screen}
    
2. Se o plug-in estiver instalado, execute `ibmcloud plugin uninstall` para desinstalar o plug-in da CLI de criação de log.

    Execute o comando a seguir:
        
    ```
    ibmcloud plugin uninstall logging-cli
    ```
    {: codeblock}
  

## Atualizando a CLI do Log Analysis por meio do repositório
{: #update_cli}

Para atualizar a CLI de criação de log, execute o comando *ibmcloud plugin update*.
{:shortdesc}

Conclua as etapas a seguir para atualizar a CLI de serviço do {{site.data.keyword.loganalysisshort}}:

1. Atualize o plug-in do {{site.data.keyword.loganalysisshort}}. Execute o comando a seguir:

    ```
    ibmcloud plugin update update logging-cli -r Bluemix
    ```
    {: codeblock}
 
2. Verifique a instalação do plug-in da CLI.
  
    Por exemplo, verifique a versão do plug-in. Execute o comando a seguir:
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    A saída é semelhante ao seguinte:
   
    ```
    ibmcloud plugin list Listing installed plug-ins...

    Plugin Name Version   
    logging-cli 0.1.1   
    ```
    {: screen}





## Obtendo ajuda geral
{: #general_cli_help}

Para obter informações gerais sobre a CLI e quais comandos são suportados, conclua as etapas a seguir:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Liste informações sobre os comandos suportados e a CLI. Execute o comando a seguir:

    ```
    ibmcloud logging help 
    ```
    {: codeblock}
    
    

## Obtendo ajuda sobre um comando
{: #command_cli_help}

Para obter ajuda sobre como usar um comando, conclua as etapas a seguir:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Obtenha a lista de comandos suportados e identifique aquele que você precisa. Execute o comando:

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. Obter ajuda sobre o comando. Execute o comando a seguir:

    ```
    ibmcloud logging help *Command*
    ```
    {: codeblock}
    
    em que *Command* é o nome de um comando da CLI, por exemplo, *status*.



## Obtendo ajuda sobre um subcomando
{: #subcommand_cli_help}

Um comando pode ter subcomandos. Para obter ajuda sobre subcomandos, conclua as etapas a seguir:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Obtenha a lista de comandos suportados e identifique aquele que você precisa. Execute o comando:

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. Obtenha ajuda sobre o comando e identifique os subcomandos suportados. Execute o comando a seguir:

    ```
    ibmcloud logging help *Command*
    ```
    {: codeblock}
    
    em que *Command* é o nome de um comando da CLI, por exemplo, *session*.

4. Obtenha ajuda sobre o comando e identifique os subcomandos suportados. Execute o comando a seguir:

    ```
    ibmcloud logging *Command* help *Subcommand*
    ```
    {: codeblock}
    
    Em que 
    
    * *Command* é o nome de um comando da CLI, por exemplo, *status*.
    * *Subcommand* é o nome de um subcomando suportado, por exemplo, para o comando *session*, um subcomando válido é *list*.


## Mostrar os detalhes do plug-in
{: #show}
  
Use o comando 'ibmcloud plugin show logging-cli' para mostrar os detalhes do plug-in. 

```
ibmcloud plugin logging-cli-log-cli
```
{: codeblock}
    
A saída é semelhante ao seguinte:
   
```
ibmcloud plugin logging-cli-log-cli
                                  
Plug-in                        logging-cli
Versão                         0.1.1
Versão mínima da CLI necessária 0.5.0
Comandos
                               logging log-delete       Excluir log
                               logging log-download     Fazer download de um log
                               logging log-show         Mostrar a contagem, o tamanho e o tipo de logs por dia
                               logging session-create   Criar uma sessão
                               logging session-delete   Excluir sessão
                               logging sessions         Listar informações de sessões
                               logging session-show     Mostrar informações de sessão
                               logging option-show      Mostrar a retenção de log
                               logging option-update    Mostrar as opções de log    
```
{: screen}

