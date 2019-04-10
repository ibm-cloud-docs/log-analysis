---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, alerts

subcollection: LogDNA

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

 
# Cómo trabajar con alertas
{: #alerts}

Puede adjuntar una o más alertas a una vista. Puede definir varios canales de notificación para una alerta. Puede silenciar alertas. Puede desvincular alertas de una vista.
{:shortdesc}

Puede configurar cualquiera de las condiciones siguientes para una alerta:

* *Frecuencia*: especifique la frecuencia con la que se desencadena una alerta. Los valores válidos son: 30 segundos, 1 minuto, 5 minutos, 15 minutos, 30 minutos, 1 hora, 6 horas, 12 horas, 24 horas
* *Contador de líneas de registro*: especifique el número de líneas de registro que coinciden con los criterios de filtrado y búsqueda de la vista. Cuando se alcanza el número de líneas de registro, se desencadena una alerta.

Puede decidir si deben comprobarse ambas condiciones o solo una de ellas. Si se establecen ambas condiciones, se desencadena una alerta cuando se alcanza cualquiera de los umbrales. 

Por ejemplo, puede configurar una alerta que se desencadene después de 30 segundos, o cuando se recopilen 100 líneas de registro que coincidan con los criterios de filtrado y de búsqueda de la vista.

Puede configurar varios canales de notificación. Los valores válidos son: `email`, `Slack`, `PagerDuty`, `Webhook`, `OpsGenie`, `Datadog`, `AppOptics`, `VictorOps`

También puede definir un **valor preestablecido**. Un valor preestablecido es una plantilla de alerta que puede adjuntar a cualquier número de vistas. 

Para reutilizar una configuración de alerta con distintas vistas, configure un **valor preestablecido de alerta**.
{: tip}

Se mostrará un icono de campana con la vista para indicar que esta vista tiene una alerta añadida.



## Configurar un valor preestablecido (plantilla de alerta)
{: #config_preset}

Realice los pasos siguientes para configurar un valor preestablecido:

1. Seleccione el icono **Configuración** ![Icono Configuración](images/admin.png "Icono Administración").
2. Seleccione **Alertas**.
3. Seleccione **Añadir un valor preestablecido de alerta**.
4. Elija un canal de notificación. 
5. Defina las condiciones de umbral.

    1. Seleccione la frecuencia. Por ejemplo, 12 horas.

    2. Especifique el número de líneas de registro tras el cual desea que se desencadene la alerta.

    3. Seleccione si desea que se comprueben ambas condiciones o solo una de ellas.

6. Añada los detalles del canal de notificación que ha elegido.

    Por ejemplo, para el canal de notificación por correo electrónico, añada uno o más destinatarios y, de manera opcional, un huso horario.

7. Pulse **Guardar alerta**.



## Configurar una alerta utilizando un valor preestablecido
{: #config_alert_preset}

Realice los pasos siguientes para añadir un valor preestablecido a una vista:

1. Pulse el icono **Vistas** ![Icono Configuración](images/views.png).
2. Cree una vista. 

    Aplique un marco de tiempo, filtros y criterios de búsqueda para filtrar las líneas de registro que se deben mostrar en la vista. 

    Para obtener más información, consulte [Creación de vistas](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7).

3. Pulse el nombre de la vista. A continuación, seleccione **Adjuntar una alerta**.

4. Elija un valor preestablecido para reutilizar una definición de alerta. 

5. Pulse **Guardar alerta**. 




## Configurar una alerta específica de una vista
{: #config_alert_view}

Realice los pasos siguientes para añadir una alerta a una vista:

1. Pulse el icono **Vistas** ![Icono Configuración](images/views.png).
2. Cree una vista. 

    Aplique un marco de tiempo, filtros y criterios de búsqueda para filtrar las líneas de registro que se deben mostrar en la vista. 

    Para obtener más información, consulte [Creación de vistas](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7).

3. Pulse el nombre de la vista. A continuación, seleccione **Adjuntar una alerta**.

4. Elija **Alerta específica de vista**.

5. Elija un canal de notificación. 

6. Defina las condiciones de umbral.

    1. Seleccione la frecuencia. Por ejemplo, 12 horas.

    2. Especifique el número de líneas de registro tras el cual desea que se desencadene la alerta.

    3. Seleccione si desea que se comprueben ambas condiciones o solo una de ellas.

7. Añada los detalles del canal de notificación que ha elegido.

    Por ejemplo, para el canal de notificación por correo electrónico, añada uno o más destinatarios y, de manera opcional, un huso horario.

8. Pulse **Guardar alerta**.



## Suprimir un valor preestablecido (plantilla de alerta)
{: #delete_preset}

Realice los pasos siguientes para suprimir un valor preestablecido:

1. Seleccione el icono **Configuración** ![Icono Configuración](images/admin.png "Icono Administración").
2. Seleccione **Alertas**.
3. Pase el puntero del ratón sobre el botón *Editar* del valor preestablecido que desee suprimir. Aparecerá la opción *Suprimir*.
4. Seleccione **Suprimir**.
5. Confirme que desea suprimir el valor preestablecido. Pulse **Suprimir**.

## Desvincular una alerta específica de vista de una vista
{: #delete_alert}

Realice los pasos siguientes para desvincular un valor preestablecido:

1. Seleccione el icono **Configuración** ![Icono Configuración](images/admin.png "Icono Administración").
2. Seleccione **Alertas**.
3. Pase el puntero del ratón sobre el botón *Editar* de la alerta que desee suprimir. Aparecerá la opción *Suprimir*.
4. Seleccione **Desvincular**.
5. Confirme que desea suprimir la alerta. Pulse **Desvincular**.



## Canales de notificación
{: #channels}

En la tabla siguiente se muestran los canales de notificación que puede configurar cuando se desencadena una alerta:

| Canal           | Detalles de configuración | 
|-------------------|-----------------------|
| `email`             | Puede configurar una o más direcciones de correo electrónico.  | 
| `Slack`             | Puede configurar un canal de slack. |
| `Webhook`           | Puede configurar un URL de webhook. |
| `PagerDuty`         | Puede configurar detalles de conexión de su sistema PagerDuty y seleccionar un servicio.|
| `OpsGenie`          | Puede configurar la clave de API para conectarse a su sistema OpsGenie. |
| `Datadog`           | Puede configurar la clave de API para conectarse a su sistema `Datadog`. |
| `AppOptics/Librato` | Puede configurar la clave de API para conectarse a su sistema AppOptics/Librato. |
| `VictorOps`         | Puede configurar el URL al que se notificará cuando se desencadene una alerta, la clave de direccionamiento y un tipo de alerta. Los tipos de alerta válidos son: `info`, `warning`, `critical` |
{: caption="Canales de notificación" caption-side="top"} 


