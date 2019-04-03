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

# Configurando a CLI do Log Analysis (plug-in CF) Descontinuado
{: #config_log_collection_cli1}

O serviço {{site.data.keyword.loganalysisshort}} inclui uma interface da linha de comandos (CLI) que pode ser usada para gerenciar os logs na nuvem. É possível usar o plug-in Cloud Foundry (CF) para visualizar o status do log, fazer download de logs e configurar a política de retenção de log. A CLI oferece diferentes tipos de ajuda: ajuda geral para aprender sobre a CLI e os comandos suportados, ajuda de comando para aprender como usar um comando ou ajuda de subcomando para aprender como usar um subcomando para um comando.
{:shortdesc}



## Instalando o plug-in do CF do Log Analysis
{: #install_cli1}

Para instalar a CLI do {{site.data.keyword.loganalysisshort}}, conclua as etapas a seguir:

1. Instale a CLI do {{site.data.keyword.Bluemix_notm}}.

   Para obter mais informações, veja [Instalando a CLI do {{site.data.keyword.Bluemix_notm}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview).

2. Instale o plug-in CF do {{site.data.keyword.loganalysisshort}}.

    * Para Linux, veja [Instalando a CLI do {{site.data.keyword.loganalysisshort}} no Linux](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli1#install_cli_linux1).
    * Para Windows, veja [Instalando a CLI do {{site.data.keyword.loganalysisshort}} no Windows](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli1#install_cli_windows1).
    * Para Mac OS X, veja [Instalando a CLI do {{site.data.keyword.loganalysisshort}} no Mac OS X](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli1#install_cli_mac1).
 
3. Verifique a instalação do plug-in da CLI.
  
    Por exemplo, verifique a versão do plug-in. Execute o comando a seguir:
    
    ```
    ibmcloud cf plugins
    ```
    {: codeblock}
    
    A saída é semelhante ao seguinte:
   
    ```
    Chamando 'cf plugins'...

    Listing Installed Plugins...
    OK

    Plugin Name           Version   Command Name   Command Help
    IBM-Logging           1.0.2     logging        IBM Logging plug-in
    ```
    {: screen}
 


## Instalando a CLI do Log Analysis no Linux
{: #install_cli_linux1}

Conclua as etapas a seguir para instalar o plug-in CF da Coleção de logs no Linux:

1. Instale o plug-in da CLI da Coleção de logs.

    1. Faça download da liberação mais recente do plug-in da CLI do serviço {{site.data.keyword.loganalysisshort}} (IBM-Logging) na [página da CLI do {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins). 
	
		Selecione o valor de plataforma: **linux64**. 
		Clique em **Salvar arquivo**. 
    
    2. Descompacte o plug-in.
    
        Por exemplo, para descompactar o arquivo ZIP do plug-in `logging-cli-linux64.gz` no Ubuntu, execute o comando a seguir:
        
        ```
        Gunzip log-cli-linux64.gz
        ```
        {: codeblock}

    3. Torne o arquivo executável.
    
        Por exemplo, para tornar o arquivo `logging-cli-linux64` executável, execute o comando a seguir:
        
        ```
        Chmod a + x log-cli-linux64
        ```
        {: codeblock}

    4. Instale o plug-in CF de log.
    
        Por exemplo, para tornar o arquivo `logging-cli-linux64` executável, execute o comando a seguir:
        
        ```
        ibmcloud cf install-plugin -f logging-cli-linux64
        ```
        {: codeblock}

2. Configure a variável de ambiente **LANG**.

    Configure *LANG* para o valor padrão *en_US.UTF-8* se o seu código de idioma do sistema não for suportado pelo CF. Para obter informações sobre códigos de idioma CF suportados, veja [Introdução à CLI do cf ![Ícone de link externo](../../../../icons/launch-glyph.svg "Ícone de link externo")](https://docs.cloudfoundry.org/cf-cli/getting-started.html){: new_window}
	
	Por exemplo, em um sistema Ubuntu, edite o arquivo *~/.bashrc* e insira as linhas a seguir:
    
    ```
    # add entry for logging CLI
    export LANG = en_US.UTF-8
    ```
    {: codeblock}
    
    Abra uma nova janela do terminal e execute o comando a seguir para verificar se a variável LANG está configurada:
    
    ```
    $echo LANG
    en_US.UTF-8
    ```
    {: screen}   
    
3. Verifique a instalação do plug-in da CLI de criação de log.
  
    Por exemplo, verifique a versão do plug-in. Execute o comando a seguir:
    
    ```
    ibmcloud cf logging -- version
    ```
    {: codeblock}
    
    A saída é semelhante ao seguinte:
   
    ```
    cf logging version 1.0.2
    ```
    {: screen}


## Instalando a CLI do Log Analysis no Windows
{: #install_cli_windows1}

Conclua as etapas a seguir para instalar o plug-in do CF Log Analysis no Windows:

1. Faça download da liberação mais recente do plug-in da CLI do serviço {{site.data.keyword.loganalysisshort}} (IBM-Logging) na [página da CLI do {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins). 
	
	1. Selecione o valor de plataforma: **win64**. 
	2. Clique em **Salvar arquivo**.  
    
2. Execute o comando **cf install-plugin** para instalar o plug-in Coleção de logs no Windows. 

    ```
	ibmcloud cf install-plugin PluginName
	```
	{: codeblock}
	
	em que *PluginName* é o nome do arquivo que foi transferido por download.
	
    Por exemplo, para instalar o plug-in *logging-cli-win64_v1.0.1.exe*, execute o comando a seguir de uma janela do terminal:
	
	```
	ibmcloud cf install-plugin logging-cli-win64_v1.0.1.exe
	```
	{: codeblock}
	
    Quando o plug-in está instalado, você obtém a mensagem a seguir: `Plugin IBM-Logging 1.0.1 successfully installed.`

3. Verifique a instalação do plug-in da CLI de criação de log.
  
    Por exemplo, verifique a versão do plug-in. Execute o comando a seguir:
    
    ```
    ibmcloud cf logging -- version
    ```
    {: codeblock}
    
    A saída é semelhante ao seguinte:
   
    ```
    ibmcloud cf logging version 1.0.1
    ```
    {: screen}
	

## Instalando a CLI do Log Analysis no Mac OS X
{: #install_cli_mac1}

Conclua as etapas a seguir para instalar o plug-in do CF da Coleção de logs no Mac OS X:

1. Faça download da liberação mais recente do plug-in da CLI do serviço {{site.data.keyword.loganalysisshort}} (IBM-Logging) na [página da CLI do {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins). 
	
	1. Selecione o valor de plataforma: **osx**. 
	2. Clique em **Salvar arquivo**.  
    
2. Execute o comando **cf install-plugin** para install instalar o plug-in da Coleção de logs no Mac OS X. 

    ```
	ibmcloud cf install-plugin PluginName
	```
	{: codeblock}
	
	em que *PluginName* é o nome do arquivo que foi transferido por download.
	
    Por exemplo, para instalar o plug-in *logging-cli-darwin_v1.0.1*, execute o comando a seguir em um terminal:
	
	```
	ibmcloud cf install-plugin logging-cli-darwin_v1.0.1
	```
	{: codeblock}
	
    Quando o plug-in está instalado, você obtém a mensagem a seguir: `Plugin IBM-Logging 1.0.1 successfully installed.`

3. Verifique a instalação do plug-in da CLI de criação de log.
  
    Por exemplo, verifique a versão do plug-in. Execute o comando a seguir:
    
    ```
    ibmcloud cf logging -- version
    ```
    {: codeblock}
    
    A saída é semelhante ao seguinte:
   
    ```
    ibmcloud cf logging version 1.0.1
    ```
    {: screen}
	
	
## Desinstalando a CLI de Análise do log
{: #uninstall_cli1}

Para desinstalar a CLI de criação de log, exclua o plug-in.
{:shortdesc}

Conclua as etapas a seguir para desinstalar a CLI do serviço {{site.data.keyword.loganalysisshort}}:

1. Verifique a versão do plug-in da CLI de criação de log que está instalada.
  
    Por exemplo, verifique a versão do plug-in. Execute o comando a seguir:
    
    ```
    ibmcloud cf plugins
    ```
    {: codeblock}
    
    A saída é semelhante ao seguinte:
   
    ```
    Listing Installed Plugins...
    OK

    Plugin Name   Version   Command Name   Command Help
    IBM-Logging   1.0.1     logging        IBM Logging plug-in
    ```
    {: screen}
    
2. Se o plug-in estiver instalado, execute o `cf uninstall-plugin` para desinstalar o plug-in da CLI de criação de log.

    Execute o comando a seguir:
        
    ```
    ibmcloud cf uninstall-plugin IBM-Logging
    ```
    {: codeblock}
  

## Obtendo ajuda geral
{: #general_cli_help1}

Para obter informações gerais sobre a CLI e quais comandos são suportados, conclua as etapas a seguir:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Liste informações sobre os comandos suportados e a CLI. Execute o comando a seguir:

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}
    
    

## Obtendo ajuda sobre um comando
{: #command_cli_help1}

Para obter ajuda sobre como usar um comando, conclua as etapas a seguir:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Obtenha a lista de comandos suportados e identifique aquele que você precisa. Execute o comando:

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}

3. Obter ajuda sobre o comando. Execute o comando a seguir:

    ```
    ibmcloud cf logging help *Command*
    ```
    {: codeblock}
    
    em que *Command* é o nome de um comando da CLI, por exemplo, *status*.



## Obtendo ajuda sobre um subcomando
{: #subcommand_cli_help1}

Um comando pode ter subcomandos. Para obter ajuda sobre subcomandos, conclua as etapas a seguir:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Obtenha a lista de comandos suportados e identifique aquele que você precisa. Execute o comando:

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}

3. Obtenha ajuda sobre o comando e identifique os subcomandos suportados. Execute o comando a seguir:

    ```
    ibmcloud cf logging help *Command*
    ```
    {: codeblock}
    
    em que *Command* é o nome de um comando da CLI, por exemplo, *session*.

4. Obtenha ajuda sobre o comando e identifique os subcomandos suportados. Execute o comando a seguir:

    ```
    ibmcloud cf logging *Command* help *Subcommand*
    ```
    {: codeblock}
    
    Em que 
    
    * *Command* é o nome de um comando da CLI, por exemplo, *status*.
    * *Subcommand* é o nome de um subcomando suportado, por exemplo, para o comando *session*, um subcomando válido é *list*.




