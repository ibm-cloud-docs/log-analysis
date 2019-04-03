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


# Mensajes de error
{: #error_msgs}

Puede que vea estos mensajes de error al utilizar el servicio {{site.data.keyword.loganalysisshort}} en {{site.data.keyword.Bluemix}}:
{:shortdesc}

## BXNLG020001W
{: #BXNLG020001W}

**Descripción del mensaje**

Ha alcanzado la cuota diaria asignada al espacio de Bluemix {GUID del espacio} para la instancia de {{site.data.keyword.loganalysisfull}} {GUID de la instancia}. Su asignación diaria actual es de 500 MB para el almacenamiento de búsqueda de registros, que se retienen en el almacenamiento de recopilación de registros durante un periodo de 3 días, durante los cuales se pueden buscar en Kibana. Para actualizar su plan para poder almacenar más datos al día en el almacenamiento de búsqueda de registros, y retener todos los registros en el almacenamiento de recopilación de registros, actualice el plan de servicio {{site.data.keyword.loganalysisshort}} para este espacio. Para obtener más información sobre los planes de servicio y sobre cómo actualizar su plan, consulte [Planes](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).


**Explicación del mensaje** 

Puede recibir un mensaje con el ID *BXNLG020001W* cuando alcanza la cuota de almacenamiento de búsqueda de registros asignada al plan de servicio Lite. El plan Lite es un plan de servicio complementario que se establece de forma predeterminada cuando se suministra el servicio {{site.data.keyword.loganalysisshort}} en un espacio. Su asignación diaria actual es de 500 MB para el almacenamiento de búsqueda de registros, que se retienen en el almacenamiento de recopilación de registros durante un periodo de 3 días, durante los cuales se pueden buscar en Kibana.

**Recuperación**

Para actualizar su plan para poder almacenar más datos al día en el almacenamiento de búsqueda de registros, y retener todos los registros en el almacenamiento de recopilación de registros, actualice el plan de servicio {{site.data.keyword.loganalysisshort}} para este espacio. Para obtener más información sobre los planes de servicio y sobre cómo actualizar su plan, consulte [Planes](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).


## BXNLG020002W 
{: #BXNLG020002W}


**Descripción del mensaje**

Ha alcanzado la cuota diaria asignada al espacio de Bluemix {GUID del espacio} para la instancia de {{site.data.keyword.loganalysisfull}} {GUID de la instancia}.  Su asignación diaria actual es de XXX para el almacenamiento de búsqueda de registros, que se retienen durante un periodo de 3 días, durante los cuales se pueden buscar en Kibana. Esto no afecta a la política de retención de registros en el almacenamiento de recopilación de registros. Para actualizar su plan para poder almacenar más datos al día en el almacenamiento de búsqueda de registros, actualice el plan de servicio {{site.data.keyword.loganalysisshort}} para este espacio. Para obtener más información sobre los planes de servicio y sobre cómo actualizar su plan, consulte [Planes](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).

XXX representa el tamaño de los datos que se pueden buscar en su plan actual.

**Explicación del mensaje** 

Ha alcanzado la cuota diaria asignada al espacio {GUID del espacio} para la instancia de {{site.data.keyword.loganalysisfull}} {GUID de la instancia}.  Su asignación diaria actual es de 500 MB, 2 GB, 5 GB o 10 GB para el almacenamiento de búsqueda de registros, que se retienen durante un periodo de 3 días, durante los cuales se pueden buscar en Kibana. Esto no afecta a la política de retención de registros en el almacenamiento de recopilación de registros.

**Recuperación**

Para actualizar su plan para poder almacenar más datos al día en el almacenamiento de búsqueda de registros, actualice el plan de servicio {{site.data.keyword.loganalysisshort}} para este espacio. Para obtener más información sobre los planes de servicio y sobre cómo actualizar su plan, consulte [Planes](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).




