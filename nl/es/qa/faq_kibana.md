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


# Preguntas más comunes sobre Kibana
{: #faq_kibana}

A continuación encontrará las respuestas a preguntas comunes sobre cómo utilizar las funciones de registro de {{site.data.keyword.Bluemix}}. {:shortdesc}

* [¿Qué puedo hacer si no veo datos en la página Descubrir en Kibana](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#logging_qa_no_data_discover_kibana)
* [¿Qué puedo hacer si recibo una excepción de autenticación?](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#logging_qa_no_data_dashboard_kibana)
* [¿Por qué veo el símbolo ? en campos de la página Descubrir de Kibana?](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#logging_qa_kibana_question)
* [Recibo un error 403 cuando intento cambiar el patrón de índice predeterminado](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#error_403)
* [El URL abreviado no funciona](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#short_url)
* [¿Puedo buscar registros de mi cuenta en Bluemix?](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#acc_logs_1)


## ¿Qué puedo hacer si no veo datos en la página Descubrir en Kibana
{: #logging_qa_no_data_discover_kibana}

Hay diferentes situaciones en las que es posible que no vea datos en Kibana:

1. Cuando se inicia Kibana, es posible que no vea datos en la página Descubrir. Recibirá el mensaje siguiente: **No se han encontrado resultados.**. 
2. Si está trabajando en la página Descubrir en Kibana, es posible que, tras un breve periodo de tiempo, reciba el mensaje: **No se han encontrado resultados.** cuando intente realizar una tarea en Kibana.

Para solucionar este problema, siga estos pasos:

1. Consulte el *Selector de tiempo* definido en la página Descubrir y aumente el periodo de tiempo. 

    **Nota**: De forma predeterminada, en {{site.data.keyword.Bluemix_notm}}, el *Selector de tiempo* está definido que muestre datos correspondientes a los 15 últimos minutos.

    Para obtener más información sobre cómo definir el *Selector de tiempo*, consulte [Establecimiento de un filtro de tiempo](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter1).
       
2. Pulse la lupa que se encuentra en la barra de búsqueda de la página *Descubrir*. Los datos de la página se renuevan en función de la consulta de búsqueda predeterminada.

    Como alternativa, puede establecer un periodo de *Renovación automática*.

    **Nota**: De forma predeterminada, en {{site.data.keyword.Bluemix_notm}}, el periodo de *Renovación automática* está desactivado (**OFF**).
    
    Para obtener más información sobre cómo habilitarlo, consulte el apartado sobre [Renovación automática de los datos](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_refresh_interval).



## ¿Qué puedo hacer si recibo una excepción de autenticación?
{: #logging_qa_no_data_dashboard_kibana}

Si no puede ver datos en las visualizaciones de una página Panel de control y recibe el mensaje de error: **Error: Excepción de autorización.**, compruebe los permisos para ver los datos de cada visualización.

Tenga en cuenta la información siguiente: puede configurar una o varias visualizaciones en la página Panel de control. Si la página Panel de control realiza una solicitud para recopilar los datos que se muestran en dichas visualizaciones, solo se emite una solicitud para todas las visualizaciones. Si no tienen permisos para ver los datos de una de las visualizaciones, toda la solicitud falla.

Para solucionar este problema, siga estos pasos:

1. Identifique las visualizaciones para las que no tiene permisos.

    1. Pulse el icono de *lápiz* de una visualización en la página *Panel de control*. La visualización se abre en la página *Visualizar*. Como alternativa, en la página *Visualizar* cargue una visualización. 
    2. Verifique que puede ver datos.
    
    Repita estos pasos para cada visualización.

2. Solicite acceso para ver datos en dichas visualizaciones al administrador de la nube.

3. Cree una nueva página Panel de control que excluya las visualizaciones para los que no dispone de permisos mientras se le asigna acceso para ver los datos de las visualizaciones que causan el problema. 

    Si comparte el Panel de control, no suprima visualizaciones ya que esto afectaría a otros miembros del equipo que utilicen el mismo panel de control.



## ¿Por qué veo el símbolo ? en campos de la página Descubrir de Kibana?
{: #logging_qa_kibana_question}

Cuando abra la página Descubrir en Kibana, podría ver un signo de interrogación `?` en los campos que aparecen listados en la sección de campos disponibles en lugar del carácter `t`. Cuando vuelva a cargar la lista de campos, se analizará el tipo de los campos y el signo de interrogación `?` se sustituirá por el carácter `t`. Para obtener más información consulte [Cómo volver a cargar la lista de campos](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_reload_fields).


## Recibo un error 403 cuando intento cambiar el patrón de índice predeterminado
{: #error_403}

El patrón de índice predeterminado no se puede cambiar. 

Si intenta definir un patrón de índice diferente como nuevo predeterminado, recibirá el error siguiente: `Config: Error 403 Prohibido`

## El URL abreviado no funciona
{: #short_url}

No se da soporte a la compartición de una búsqueda, una visualización o un panel de control. Por lo tanto, el URL abreviado correspondiente a un objeto Kibana que desea compartir tampoco funciona. 

## ¿Puedo buscar registros de mi cuenta en Bluemix?
{: #acc_logs_1}

Como propietario de una cuenta, puede buscar y analizar los registros de su cuenta.

Siga estos pasos para obtener para ver los registros de su cuenta:

1. [Inicie Kibana.](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser) Por ejemplo, para la región EE.UU. sur, utilice el URL `https://logging.ng.bluemix.net`,

2. Seleccione la opción **Ver registros de la cuenta NombreCuenta** para ver los registros de la cuenta. *NombreCuenta* es el nombre de la cuenta.

