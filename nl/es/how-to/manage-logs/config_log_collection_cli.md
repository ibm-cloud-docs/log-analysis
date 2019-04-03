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

# Configuración de la CLI de Log Analysis (plugin CF) en desuso
{: #config_log_collection_cli1}

El servicio {{site.data.keyword.loganalysisshort}} incluye una interfaz de línea de mandatos (CLI) que puede utilizar para gestionar los registros en la nube. Puede utilizar el plugin de Cloud Foundry (CF) para ver el estado del registro, para descargar registros y para configurar la política de retención de registros. La CLI ofrece distintos tipos de ayuda: ayuda general para obtener información sobre la CLI y los mandatos soportados, ayuda sobre mandatos para ver cómo se utiliza un mandato o ayuda sobre submandatos para aprender a utilizar un submandato de un mandato.
{:shortdesc}



## Instalación del plugin CF de Log Analysis
{: #install_cli1}

Para instalar la CLI de {{site.data.keyword.loganalysisshort}},
siga estos pasos:

1. Instale la CLI de {{site.data.keyword.Bluemix_notm}}.

   Para obtener más información, consulte [Instalación de la CLI de {{site.data.keyword.Bluemix_notm}}](/docs/cli/index.html#overview).

2. Instale el plugin de {{site.data.keyword.loganalysisshort}} CF.

    * Para Linux, consulte [Instalación de la CLI de {{site.data.keyword.loganalysisshort}} en Linux](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli.html#install_cli_linux1).
    * Para Windows, consulte [Instalación de la CLI de {{site.data.keyword.loganalysisshort}} en Windows](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli.html#install_cli_windows1).
    * Para Mac OS X, consulte [Instalación de la CLI de {{site.data.keyword.loganalysisshort}} en Mac OS X](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli.html#install_cli_mac1).
 
3. Verifique la instalación del plugin de la CLI.
  
    Por ejemplo, compruebe la versión del plugin. Ejecute el mandato siguiente:
    
    ```
    ibmcloud cf plugins
    ```
    {: codeblock}
    
    La salida tiene el aspecto siguiente:
   
    ```
    Invoking 'cf plugins'...

    Listing Installed Plugins...
    OK

    Plugin Name           Version   Command Name   Command Help
    IBM-Logging           1.0.2     logging        IBM Logging plug-in
    ```
    {: screen}
 


## Instalación de la CLI de Log Analysis en Linux
{: #install_cli_linux1}

Siga estos pasos para instalar el plugin de Log Collection CF en Linux:

1. Instale el plugin de la CLI de recopilación de registros.

    1. Descargue el último release del plugin de la CLI del servicio {{site.data.keyword.loganalysisshort}} (IBM-Logging) de [la página de la CLI de {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins). 
	
		Seleccione el valor de plataforma: **linux64**. 
		Pulse **Guardar archivo**. 
    
    2. Descomprima el plugin.
    
        Por ejemplo, para descomprimir el plugin `logging-cli-linux64.gz` en Ubuntu, ejecute el siguiente mandato:
        
        ```
        gunzip logging-cli-linux64.gz
        ```
        {: codeblock}

    3. Convierta el archivo en ejecutable.
    
        Por ejemplo, para convertir el archivo `logging-cli-linux64` en ejecutable, ejecute el siguiente mandato:
        
        ```
        chmod a+x logging-cli-linux64
        ```
        {: codeblock}

    4. Instale el plugin de CF de registro.
    
        Por ejemplo, para convertir el archivo `logging-cli-linux64` en ejecutable, ejecute el siguiente mandato:
        
        ```
        ibmcloud cf install-plugin -f logging-cli-linux64
        ```
        {: codeblock}

2. Defina la variable de entorno **LANG**.

    Establezca *LANG* en el valor predeterminado *en_US.UTF-8* si el entorno local del sistema no recibe soporte de CF. Para obtener información sobre los entornos locales soportados de CF, consulte [Iniciación a la CLI de cf ![Icono de enlace externo](../../../../icons/launch-glyph.svg "Icono de enlace externo")](https://docs.cloudfoundry.org/cf-cli/getting-started.html){: new_window}
	
	Por ejemplo, en un sistema Ubuntu, edite el archivo *~/.bashrc* y especifique las siguientes líneas:
    
    ```
    # add entry for logging CLI
    export LANG = en_US.UTF-8
    ```
    {: codeblock}
    
    Abra una nueva ventana de terminal y ejecute el mandato siguiente para verificar que la variable LANG esté establecida:
    
    ```
    $echo LANG
    en_US.UTF-8
    ```
    {: screen}   
    
3. Verifique la instalación del plugin de la CLI de registro.
  
    Por ejemplo, compruebe la versión del plugin. Ejecute el mandato siguiente:
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    La salida tiene el aspecto siguiente:
   
    ```
    cf logging version 1.0.2
    ```
    {: screen}


## Instalación de la CLI de Log Analysis en Windows
{: #install_cli_windows1}

Siga estos pasos para instalar el plugin Log Collection CF en Windows:

1. Descargue el último release del plugin de la CLI del servicio {{site.data.keyword.loganalysisshort}} (IBM-Logging) de [la página de la CLI de {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins). 
	
	1. Seleccione el valor de plataforma: **win64**. 
	2. Pulse **Guardar archivo**.  
    
2. Ejecute el mandato **cf install-plugin** para instalar el plugin de recopilación de registros en Windows. 

    ```
	ibmcloud cf install-plugin PluginName
	```
	{: codeblock}
	
	donde *PluginName* es el nombre del archivo que ha descargado.
	
    Por ejemplo, para instalar el plugin *logging-cli-win64_v1.0.1.exe*, ejecute el mandato siguiente desde una ventana de terminal:
	
	```
	ibmcloud cf install-plugin logging-cli-win64_v1.0.1.exe
	```
	{: codeblock}
	
    Cuando el plugin esté instalado, recibirá el mensaje siguiente: `Plugin IBM-Logging 1.0.1 successfully installed.`

3. Verifique la instalación del plugin de la CLI de registro.
  
    Por ejemplo, compruebe la versión del plugin. Ejecute el mandato siguiente:
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    La salida tiene el aspecto siguiente:
   
    ```
    ibmcloud cf logging version 1.0.1
    ```
    {: screen}
	

## Instalación de la CLI de Log Analysis en Mac OS X
{: #install_cli_mac1}

Siga estos pasos para instalar el plugin Log Collection CF en Mac OS X:

1. Descargue el último release del plugin de la CLI del servicio {{site.data.keyword.loganalysisshort}} (IBM-Logging) de [la página de la CLI de {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins). 
	
	1. Seleccione el valor de plataforma: **osx**. 
	2. Pulse **Guardar archivo**.  
    
2. Ejecute el mandato **cf install-plugin** para instalar el plugin de recopilación de registros en Mac OS X. 

    ```
	ibmcloud cf install-plugin PluginName
	```
	{: codeblock}
	
	donde *PluginName* es el nombre del archivo que ha descargado.
	
    Por ejemplo, para instalar el plugin *logging-cli-darwin_v1.0.1*, ejecute el mandato siguiente desde un terminal:
	
	```
	ibmcloud cf install-plugin logging-cli-darwin_v1.0.1
	```
	{: codeblock}
	
    Cuando el plugin esté instalado, recibirá el mensaje siguiente: `Plugin IBM-Logging 1.0.1 successfully installed.`

3. Verifique la instalación del plugin de la CLI de registro.
  
    Por ejemplo, compruebe la versión del plugin. Ejecute el mandato siguiente:
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    La salida tiene el aspecto siguiente:
   
    ```
    ibmcloud cf logging version 1.0.1
    ```
    {: screen}
	
	
## Desinstalación de la CLI de Log Analysis
{: #uninstall_cli1}

Para desinstalar la CLI de registro, suprima el plugin.
{:shortdesc}

Siga estos pasos para desinstalar la CLI del servicio {{site.data.keyword.loganalysisshort}}:

1. Verifique la versión del plugin de la CLI de registro que se ha instalado.
  
    Por ejemplo, compruebe la versión del plugin. Ejecute el mandato siguiente:
    
    ```
    ibmcloud cf plugins
    ```
    {: codeblock}
    
    La salida tiene el aspecto siguiente:
   
    ```
    Listing Installed Plugins...
    OK

    Plugin Name   Version   Command Name   Command Help
    IBM-Logging   1.0.1     logging        IBM Logging plug-in
    ```
    {: screen}
    
2. Si el plugin está instalado, ejecute `cf uninstall-plugin` para desinstalar el plugin de la CLI de registro.

    Ejecute el mandato siguiente:
        
    ```
    ibmcloud cf uninstall-plugin IBM-Logging
    ```
    {: codeblock}
  

## Obtención de ayuda general
{: #general_cli_help1}

Para obtener información general sobre la CLI y los mandatos soportados, siga los pasos siguientes:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Obtenga información sobre los mandatos soportados y sobre la CLI. Ejecute el mandato siguiente:

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}
    
    

## Obtención de ayuda sobre un mandato
{: #command_cli_help1}

Para obtener ayuda sobre cómo utilizar un mandato, siga los pasos siguientes:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Obtenga la lista de mandatos soportados e identifique el que necesita. Ejecute el mandato:

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}

3. Obtenga ayuda sobre el mandato. Ejecute el mandato siguiente:

    ```
    ibmcloud cf logging help *Command*
    ```
    {: codeblock}
    
    donde *Mandato* es el nombre de un mandato de la CLI, como por ejemplo *status*.



## Obtención de ayuda sobre un submandato
{: #subcommand_cli_help1}

Un mandato puede tener submandatos. Para obtener ayuda sobre los submandatos, siga los pasos siguientes:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Obtenga la lista de mandatos soportados e identifique el que necesita. Ejecute el mandato:

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}

3. Obtenga ayuda sobre el mandato e identifique los submandatos soportados. Ejecute el mandato siguiente:

    ```
    ibmcloud cf logging help *Command*
    ```
    {: codeblock}
    
    donde *Mandato* es el nombre de un mandato de la CLI, como por ejemplo *session*.

4. Obtenga ayuda sobre el mandato e identifique los submandatos soportados. Ejecute el mandato siguiente:

    ```
    ibmcloud cf logging *Command* help *Subcommand*
    ```
    {: codeblock}
    
    donde 
    
    * *Mandato* es el nombre de un mandato de la CLI, como por ejemplo *status*.
    * *Submandato* es el nombre de un submandato soportado, como por ejemplo, para el mandato *session*, un submandato válido es *list*.




