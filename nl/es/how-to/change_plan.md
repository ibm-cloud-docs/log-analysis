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


# Cambio del plan
{: #change_plan}

Puede cambiar el plan de servicio de {{site.data.keyword.loganalysisshort}} mediante la IU de {{site.data.keyword.Bluemix_notm}} o mediante la ejecución del mandato `ibmcloud service update`. Puede actualizar o reducir el plan siempre que lo desee.
{:shortdesc}

## Cambio del plan de servicio a través de la interfaz de usuario
{: #change_plan_ui}

Para cambiar el plan de servicio en la IU de {{site.data.keyword.Bluemix_notm}}, siga los pasos siguientes:

1. Inicie sesión en {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Icono de enlace externo](../../../icons/launch-glyph.svg "Icono de enlace externo")](http://bluemix.net){:new_window}. 

2. Seleccione la región, la organización y el espacio donde está disponible el servicio de {{site.data.keyword.loganalysisshort}}.  

3. Pulse la instancia de servicio de {{site.data.keyword.loganalysisshort}} desde el *Panel de control* de {{site.data.keyword.Bluemix_notm}}. 
    
4. Seleccione el separador **Plan** en el panel de control de {{site.data.keyword.loganalysisshort}}.

    Se muestra información sobre el plan actual.
	
5. Seleccione un plan nuevo para actualizar o reducir su plan. 

6. Pulse **Guardar**.




## Cambio del plan de servicio a través de la CLI
{: #change_plan_cli}

Para cambiar el plan de servicio en Bluemix a través de la CLI, siga los pasos siguientes:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
	
2. Ejecute el mandato `ibmcloud service list` para comprobar su plan actual y para obtener el nombre de servicio {{site.data.keyword.loganalysisshort}} de la lista de servicios disponibles en el espacio. 

    El valor del campo **name** es el que debe utilizar para cambiar el plan. 

    Por ejemplo,
	
	```
	$ ibmcloud service list
    Invoking 'cf services'...

    Getting services in org MyOrg / space dev as xxx@ibm.com...
    OK

    name                           service                  plan             bound apps            last operation
    Log Analysis-m2                ibmLogAnalysis           premium                                update succeeded
    ```
	{: screen}
    
3. Actualice o reduzca su plan. Ejecute el mandato `ibmcloud service update`.
    
	```
	ibmcloud service update service_name [-p new_plan]
	```
	{: codeblock}
	
	donde 
	
	* *service_name* es el nombre del servicio. Puede ejecutar el mandato `ibmcloud service list` para obtener el valor.
	* *new_plan* es el nombre del plan.
	
	En la tabla siguiente encontrará los distintos planes y sus valores admitidos:
	
	<table>
	  <caption>Tabla 1. Lista de planes.</caption>
	  <tr>
	    <th>Plan</th>
	    <th>Nombre</th>
	  </tr>
	  <tr>
	    <td>Lite</td>
	    <td>estándar</td>
	  </tr>
	  <tr>
	    <td>Recopilación de registros</td>
	    <td>premium</td>
	  </tr>
	  <tr>
	    <td>Recopilación de registros con búsqueda de 2 GB/día</td>
	    <td>premiumsearch2</td>
	  </tr>
	  <tr>
	    <td>Recopilación de registros con búsqueda de 5 GB/día</td>
	    <td>premiumsearch5</td>
	  </tr>
	  <tr>
	    <td>Recopilación de registros con búsqueda de 10 GB/día</td>
	    <td>premiumsearch10</td>
	  </tr>
	</table>
	
	Por ejemplo, para reducir su plan al plan *Lite*, ejecute el siguiente mandato:
	
	```
	ibmcloud service update "Log Analysis-m2" -p standard
    Updating service instance Log Analysis-m2 as xxx@ibm.com...
    OK
	```
	{: screen}

4. Compruebe que el nuevo plan se haya cambiado. Ejecute el mandato `ibmcloud service list`.

  ```
	ibmcloud service list
	```
	{: codeblock}






