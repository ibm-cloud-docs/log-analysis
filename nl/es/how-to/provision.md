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


# Suministro del servicio de análisis de registros
{: #provision}

Puede suministrar el servicio {{site.data.keyword.loganalysisshort}} desde la interfaz de usuario de {{site.data.keyword.Bluemix}} o desde la línea de mandatos.
{:shortdesc}


## Suministro desde la interfaz de usuario
{: #ui}

Siga estos pasos para suministrar una instancia del servicio {{site.data.keyword.loganalysisshort}} en {{site.data.keyword.Bluemix_notm}}:

1. Inicie una sesión en su cuenta de {{site.data.keyword.Bluemix_notm}}.

    El panel de control de {{site.data.keyword.Bluemix_notm}} se puede encontrar en: [http://bluemix.net ![Icono de enlace externo](../../../icons/launch-glyph.svg "Icono de enlace externo")](http://bluemix.net){:new_window}.
    
	Cuando inicia sesión con su ID de usuario y su contraseña, se abre la interfaz de usuario de {{site.data.keyword.Bluemix_notm}}.

2. Pulse **Catálogo**. Se abrirá la lista de servicios disponibles en {{site.data.keyword.Bluemix_notm}}.

3. Seleccione la categoría **Herramientas de desarrollador** para filtrar la lista de servicios mostrados.

4. Pulse el mosaico **Análisis de registros**.

5. Seleccione un plan de servicio. De forma predeterminada, se establece el plan **Lite**.

    Para obtener más información sobre los planes de servicio, consulte [Planes de servicio](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).
	
6. Pulse **Crear** para suministrar el servicio {{site.data.keyword.loganalysisshort}} en el espacio de {{site.data.keyword.Bluemix_notm}} en el que ha iniciado sesión.
  
 

## Suministro desde la CLI
{: #cli}

Siga estos pasos para suministrar una instancia del servicio {{site.data.keyword.loganalysisshort}} en {{site.data.keyword.Bluemix_notm}} mediante la línea de mandatos:

1. [Requisito previo] Instale la CLI de {{site.data.keyword.Bluemix_notm}}.

   Para obtener más información, consulte [Instalación de la CLI de {{site.data.keyword.Bluemix_notm}}](/docs/cli/index.html#overview).
   
   Si la CLI está instalada, continúe en el paso siguiente.
    
2. Inicie la sesión en la región, organización o espacio en {{site.data.keyword.Bluemix_notm}} donde desea suministrar el servicio. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
3. Ejecute el mandato `ibmcloud service create` para suministrar una instancia.

    ```
	ibmcloud service create service_name service_plan service_instance_name
	```
	{: codeblock}
	
	Donde
	
	* service_name es el nombre del servicio, que es **ibmLogAnalysis**.
	* service_plan es el nombre del plan de servicio. Para obtener una lista de planes, consulte [Planes de servicio](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).
	* service_instance_name es el nombre que desea utilizar para la nueva instancia de servicio que cree.

	Por ejemplo, para crear una instancia del servicio {{site.data.keyword.loganalysisshort}} con el plan Lite, ejecute este mandato:
	
	```
	ibmcloud service create ibmLogAnalysis standard my_logging_svc
	```
	{: codeblock}
	
4. Verifique que el servicio se ha creado correctamente. Ejecute el mandato siguiente:

    ```	
	ibmcloud service list
	```
	{: codeblock}
	
	El resultado de la ejecución del mandato tiene este aspecto:
	
	```
    Getting services in org MyOrg / space MySpace as xxx@yyy.com...
    OK
    
    name                           service                  plan                   bound apps              last operation
    my_logging_svc                ibmLogAnalysis           standard                                        create succeeded
	```
	{: screen}

	



