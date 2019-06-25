---

copyright:
  years:  2018, 2019
lastupdated: "2019-04-02"

keywords: LogDNA, IBM, Log Analysis, logging instance, enable, service logs

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

# Configuración de los registros de servicio de {{site.data.keyword.cloud_notm}}
{: #config_svc_logs}

Puede tener varias instancias de {{site.data.keyword.la_full_notm}} en una región. Sin embargo, solo se puede configurar 1 instancia en una región para que reciba registros de los servicios habilitados en {{site.data.keyword.cloud_notm}}.
{:shortdesc}



## Configuración de los registros de servicios de plataforma mediante el panel de control Observabilidad
{: #config_svc_logs_ui}

Para configurar una instancia desde el panel de control Observabilidad en {{site.data.keyword.cloud_notm}}, realice los pasos siguientes:

1. [Inicie una sesión en su cuenta de {{site.data.keyword.cloud_notm}} ![Icono de enlace externo](../../icons/launch-glyph.svg "Icono de enlace externo")](https://cloud.ibm.com/login){:new_window}.

	Cuando inicia una sesión con su ID de usuario y su contraseña, se abre la interfaz de usuario de {{site.data.keyword.cloud_notm}}.

2. Vaya al icono de menú ![icono de menú](../../icons/icon_hamburger.svg). A continuación, seleccione **Observabilidad** para acceder al panel de control *Observabilidad*.

3. Seleccione **Registro** y, a continuación, pulse **Configurar registros de servicios de plataforma**. 

4. Elija la instancia de LogDNA que recibirá los registros de los servicios habilitados en la plataforma en la nube.

5. Seleccione una región. 

6. Seleccione una instancia.

7. Pulse **Guardar**. 

Se abre la página principal *Observabilidad*.

La instancia que ha seleccionado para recibir los registros de servicio muestra el distintivo **Registros de servicios de plataforma**.

Para obtener más información sobre los servicios que están habilitados para enviar registros a {{site.data.keyword.la_full_notm}}, consulte [Servicios en la nube](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services).

