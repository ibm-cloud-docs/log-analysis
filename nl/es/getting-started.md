---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-07"

keywords: LogDNA, IBM, Log Analysis, logging, getting started

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

# Guía de aprendizaje de iniciación
{: #getting-started}

Utilice {{site.data.keyword.la_full}} para añadir funciones de gestión de registros a la arquitectura de {{site.data.keyword.cloud_notm}}. Se trabaja con {{site.data.keyword.la_full_notm}} mediante LogDNA en asociación con {{site.data.keyword.IBM_notm}}.
{:shortdesc}


## Paso 1. Antes de empezar
{: #getting-started_prereqs}

* Obtenga más información sobre {{site.data.keyword.la_full_notm}}. Encontrará detalles en la sección [Acerca de {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).
* Compruebe las regiones en las que está disponible el servicio. Para obtener más información, consulte [Regiones](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_regions).
* Obtenga un ID de usuario que sea miembro o propietario de una cuenta de {{site.data.keyword.cloud_notm}}. 

    Para obtener un ID de usuario de {{site.data.keyword.cloud_notm}}, pulse [Registro ![Icono de enlace externo](../../icons/launch-glyph.svg "Icono de enlace externo")](https://cloud.ibm.com/login){:new_window}.



## Paso 2. Iniciación
{: #getting-started_step2}

Elija un recurso de nube para el que desee gestionar registros. A continuación, configure este origen de registro para que pueda supervisar sus registros a través del servicio {{site.data.keyword.la_full_notm}}. El origen de registro puede estar en la misma región donde suministre una instancia de {{site.data.keyword.la_full_notm}} o en una región distinta.

En la tabla siguiente se muestran ejemplos de recursos de nube que puede configurar para almacenar y gestionar registros utilizando el servicio {{site.data.keyword.la_full_notm}}. Complete la guía de aprendizaje para un recurso para iniciarse en el servicio {{site.data.keyword.loganalysisshort}}:

<table>
  <caption>Guías de aprendizaje para empezar a trabajar con el servicio {{site.data.keyword.la_full_notm}} </caption>
  <tr>
    <th>Recurso</th>
    <th>Guía de aprendizaje</th>
    <th>Entorno</th>
    <th>Escenario</th>
  </tr>
  <tr>
    <td>Contenedores que se ejecutan en {{site.data.keyword.containershort}}</td>
    <td>[Gestión de registros de clúster de Kubernetes con {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-kube#kube)</td>
    <td>{{site.data.keyword.cloud_notm}} público </td>
    <td>![{{site.data.keyword.containershort}} e {{site.data.keyword.la_full_notm}}](images/kube.png "{{site.data.keyword.containershort}} e {{site.data.keyword.la_full_notm}}")</td>
  </tr>
  <tr>
    <td>Linux Ubuntu, Linux Debian</td>
    <td>[Gestión de registros de Linux Ubuntu con {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-ubuntu#ubuntu)</td>
    <td>Local</td>
    <td>![Servidor Ubuntu e {{site.data.keyword.la_full_notm}}](images/ubuntu.png "Servidor Ubuntu e {{site.data.keyword.la_full_notm}}")</td>
  </tr>
</table>



## Paso 3. Actualizar el plan
{: #getting-started_step3}

Habilite más características de registro.

Actualice el plan del servicio {{site.data.keyword.la_full_notm}} a un plan de pago para poder [filtrar registros](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5), [buscar en registros](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6), [definir vistas](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7) y [configurar alertas](https://docs.logdna.com/docs/alerts). Para obtener más información sobre los planes de servicio de {{site.data.keyword.la_full_notm}}, consulte [Planes de tarifas](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

## Paso 4. Próximos pasos 
{: #getting-started_iam}

A continuación, gestione el acceso de usuario con IAM.

Identifique las políticas de IAM que necesita un usuario para trabajar con el servicio {{site.data.keyword.la_full_notm}}.

Para obtener más información sobre la integración de IAM con el servicio {{site.data.keyword.la_full_notm}}, consulte [Gestión del acceso de usuario con IAM](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#iam).

Por ejemplo, elija un rol de usuario para obtener información sobre cómo otorgar permisos a dicho usuario para que pueda trabajar con el servicio {{site.data.keyword.la_full_notm}}. 

| Rol de usuario en {{site.data.keyword.cloud_notm}} | Para obtener más información                     |
|-----------------------------------------------------|------------------------------------------|
| Propietario de la cuenta                                       | [Cómo otorgar permisos a un usuario para que se convierta en administrador del servicio en la cuenta de {{site.data.keyword.cloud_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account) |
| Administrador de servicios de plataforma en la cuenta       | [Cómo otorgar permisos a un usuario para que se convierta en administrador del servicio en la cuenta de {{site.data.keyword.cloud_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account) |
| Administrador de servicios de plataforma en un grupo de recursos  | [Cómo otorgar permisos a un usuario para que se convierta en administrador del servicio dentro de un grupo de recursos](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_rg) |
| Operador de DevOps de la plataforma en la cuenta           | [Cómo otorgar permisos a un usuario de DevOps para gestionar el servicio en la cuenta de {{site.data.keyword.cloud_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#devops_account) |
| Operador de DevOps de la plataforma en un grupo de recursos        | [Cómo otorgar permisos a un usuario de DevOps para gestionar el servicio dentro de un grupo de recursos](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#devops_rg) |
| Administrador de servicios en LogDNA                     | [Cómo otorgar permisos para gestionar registros y configurar alertas en LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna)              |
| Usuario / Desarrollador                                    | [Cómo otorgar permisos a un usuario para ver y gestionar registros en LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna)               |
{: caption="Tabla 2. Roles de Cloud en {{site.data.keyword.cloud_notm}}" caption-side="top"}


