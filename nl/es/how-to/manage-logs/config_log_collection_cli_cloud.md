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

# Configuración de la CLI de {{site.data.keyword.loganalysisshort}}
{: #config_log_collection_cli}

El servicio {{site.data.keyword.loganalysisshort}} incluye una interfaz de línea de mandatos (CLI) que puede utilizar para gestionar registros en la nube. Puede utilizar el plugin de {{site.data.keyword.Bluemix_notm}} para ver el estado del registro, para descargar registros y para configurar la política de retención de registros. La CLI ofrece distintos tipos de ayuda: ayuda general para obtener información sobre la CLI y los mandatos soportados, ayuda sobre mandatos para ver cómo se utiliza un mandato o ayuda sobre submandatos para aprender a utilizar un submandato de un mandato.
{:shortdesc}


## Instalación del plugin de {{site.data.keyword.loganalysisshort}} desde el repositorio de {{site.data.keyword.Bluemix_notm}}
{: #install_cli_repo}

Para instalar la CLI de {{site.data.keyword.loganalysisshort}},
siga estos pasos:

1. Instale la CLI de {{site.data.keyword.Bluemix_notm}}.

   Para obtener más información, consulte [Instalación de la CLI de {{site.data.keyword.Bluemix_notm}}](/docs/cli/index.html#overview).
   
2. Obtenga el nombre del plugin en el repositorio. Ejecute el mandato siguiente:

    ```
    ibmcloud plugin repo-plugins
    ```
    {: codeblock}
    
    El nombre del plugin es **logging-cli**.

3. Instale el plugin de {{site.data.keyword.loganalysisshort}}. Ejecute el mandato siguiente:

    ```
    ibmcloud plugin install logging-cli -r Bluemix
    ```
    {: codeblock}
 
4. Compruebe que el plugin de {{site.data.keyword.loganalysisshort}} esté instalado.
  
    Por ejemplo, ejecute el siguiente mandato para ver la lista de plugins instalados:
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    La salida tiene el aspecto siguiente:
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}


## Instalación del plugin de {{site.data.keyword.loganalysisshort}} desde un archivo
{: #install_cli}

Para instalar la CLI de {{site.data.keyword.loganalysisshort}},
siga estos pasos:

1. Instale la CLI de {{site.data.keyword.Bluemix_notm}}.

   Para obtener más información, consulte [Instalación de la CLI de {{site.data.keyword.Bluemix_notm}}](/docs/cli/index.html#overview).

2. Instale el plugin de {{site.data.keyword.loganalysisshort}}.

    * Para Linux, consulte [Instalación del plugin de {{site.data.keyword.loganalysisshort}} en Linux](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_linux).
    * Para Windows, consulte [Instalación del plugin de {{site.data.keyword.loganalysisshort}} en Windows](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_windows).
    * Para Mac OS X, consulte [Instalación del plugin de {{site.data.keyword.loganalysisshort}} en Mac OS X](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_mac).
 
3. Verifique la instalación del plugin de la CLI.
  
    Por ejemplo, compruebe la versión del plugin. Ejecute el mandato siguiente:
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    La salida tiene el aspecto siguiente:
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}
 


## Instalación del plugin de Log Analysis en Linux desde un archivo
{: #install_cli_linux}

Siga estos pasos para instalar el plugin de recopilación de registros en Linux:

1. Instale el plugin.

    Descargue el último release del plugin de la CLI del servicio {{site.data.keyword.loganalysisshort}} (IBM-Logging) de [la página de la CLI de {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins). 
	
	* Seleccione el valor de plataforma: **linux64**. 
	
	* Pulse **Guardar archivo**. 
    
2. Instale el plugin. Ejecute el mandato siguiente:
        
    ```
    ibmcloud plugin install -f logging-cli-linux-amd64-0.1.1
    ```
    {: codeblock}




## Instalación del plugin de Log Analysis en Windows desde un archivo
{: #install_cli_windows}

Siga estos pasos para instalar el plugin de recopilación de registros en Windows:

1. Descargue el último release del plugin de la CLI del servicio {{site.data.keyword.loganalysisshort}} (IBM-Logging) de [la página de la CLI de {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins). 
	
	1. Seleccione el valor de plataforma: **win64**. 
	2. Pulse **Guardar archivo**.  
    
2. Instale el plugin. Ejecute el mandato siguiente:
        
    ```
    ibmcloud plugin install -f logging-cli-windows-amd64-0.1.1.exe
    ```
    {: codeblock}

	

## Instalación del plugin de Log Analysis en Mac OS X desde un archivo
{: #install_cli_mac}

Siga estos pasos para instalar el plugin de recopilación de registros en Mac OS X:

1. Descargue el último release del plugin de la CLI del servicio {{site.data.keyword.loganalysisshort}} (IBM-Logging) de [la página de la CLI de {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins). 
	
	1. Seleccione el valor de plataforma: **osx**. 
	2. Pulse **Guardar archivo**.  
    
2. Cambie los permisos del archivo. Ejecute el mandato siguiente:

    ```
    chmod u+x logging-cli-darwin-amd64-0.1.1
    ```
     {: codeblock}

3. Instale el plugin. Ejecute el mandato siguiente:
        
    ```
    ibmcloud plugin install -f logging-cli-darwin-amd64-0.1.1
    ```
    {: codeblock}

	
	
## Desinstalación de la CLI de Log Analysis
{: #uninstall_cli}

Para desinstalar la CLI de registro, suprima el plugin.
{:shortdesc}

Siga estos pasos para desinstalar la CLI del servicio {{site.data.keyword.loganalysisshort}}:

1. Verifique la versión del plugin de la CLI de registro que se ha instalado.
  
    Por ejemplo, compruebe la versión del plugin. Ejecute el mandato siguiente:
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    La salida tiene el aspecto siguiente:
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}
    
2. Si el plugin está instalado, ejecute `ibmcloud plugin uninstall` para desinstalar el plugin de la CLI de registro.

    Ejecute el mandato siguiente:
        
    ```
    ibmcloud plugin uninstall logging-cli
    ```
    {: codeblock}
  

## Actualización de la CLI de Log Analysis desde el repositorio
{: #update_cli}

Para actualizar la CLI de registro, ejecute el mandato *ibmcloud plugin update*.
{:shortdesc}

Siga estos pasos para actualizar la CLI de servicio de {{site.data.keyword.loganalysisshort}}:

1. Actualice el plugin de {{site.data.keyword.loganalysisshort}}. Ejecute el mandato siguiente:

    ```
    ibmcloud plugin update logging-cli -r Bluemix
    ```
    {: codeblock}
 
2. Verifique la instalación del plugin de la CLI.
  
    Por ejemplo, compruebe la versión del plugin. Ejecute el mandato siguiente:
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    La salida tiene el aspecto siguiente:
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}





## Obtención de ayuda general
{: #general_cli_help}

Para obtener información general sobre la CLI y los mandatos soportados, siga los pasos siguientes:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Obtenga información sobre los mandatos soportados y sobre la CLI. Ejecute el mandato siguiente:

    ```
    ibmcloud logging help 
    ```
    {: codeblock}
    
    

## Obtención de ayuda sobre un mandato
{: #command_cli_help}

Para obtener ayuda sobre cómo utilizar un mandato, siga los pasos siguientes:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Obtenga la lista de mandatos soportados e identifique el que necesita. Ejecute el mandato:

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. Obtenga ayuda sobre el mandato. Ejecute el mandato siguiente:

    ```
    ibmcloud logging help *Command*
    ```
    {: codeblock}
    
    donde *Mandato* es el nombre de un mandato de la CLI, como por ejemplo *status*.



## Obtención de ayuda sobre un submandato
{: #subcommand_cli_help}

Un mandato puede tener submandatos. Para obtener ayuda sobre los submandatos, siga los pasos siguientes:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Obtenga la lista de mandatos soportados e identifique el que necesita. Ejecute el mandato:

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. Obtenga ayuda sobre el mandato e identifique los submandatos soportados. Ejecute el mandato siguiente:

    ```
    ibmcloud logging help *Command*
    ```
    {: codeblock}
    
    donde *Mandato* es el nombre de un mandato de la CLI, como por ejemplo *session*.

4. Obtenga ayuda sobre el mandato e identifique los submandatos soportados. Ejecute el mandato siguiente:

    ```
    ibmcloud logging *Command* help *Subcommand*
    ```
    {: codeblock}
    
    donde 
    
    * *Mandato* es el nombre de un mandato de la CLI, como por ejemplo *status*.
    * *Submandato* es el nombre de un submandato soportado, como por ejemplo, para el mandato *session*, un submandato válido es *list*.


## Mostrar los detalles del plugin
{: #show}
  
Utilice el mandato 'ibmcloud plugin show logging-cli' para ver los detalles del plugin. 

```
ibmcloud plugin show logging-cli
```
{: codeblock}
    
La salida tiene el aspecto siguiente:
   
```
ibmcloud plugin show logging-cli
                                  
Plugin                         logging-cli
Version                        0.1.1
Minimal CLI version required   0.5.0
Commands
                               logging log-delete       Delete log
                               logging log-download     Download a log
                               logging log-show         Show the count, size, and type of logs per day
                               logging session-create   Create a session
                               logging session-delete   Delete session
                               logging sessions         List sessions info
                               logging session-show     Show a session info
                               logging option-show      Show the log retention
                               logging option-update    Show the log options    
```
{: screen}

