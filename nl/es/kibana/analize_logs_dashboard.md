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

# Análisis de registro en Kibana mediante un panel de control
{:#analize_logs_dashboard}

Utilice el *Panel de control* de Kibana para visualizar recopilaciones de visualizaciones agrupadas en los paneles de control. Utilice los paneles de control para analizar los datos de registro y comparar resultados.
{:shortdesc}

En {{site.data.keyword.Bluemix}} hay diferentes tipos de paneles de control que puede definir y personalizar para visualizar y analizar los datos. Por ejemplo, en la siguiente tabla se muestran algunos de los tipos de paneles de control más comunes:

| Tipo de panel de control | Descripción |
|-------------------|-------------|
| Panel de control Single-cf-app | Es un panel de control que muestra información correspondiente a una sola aplicación Cloud Foundry. |
| Panel de control Contenedor único  | Es un panel de control que muestra información correspondiente a un solo contenedor.  |
| Panel de control Grupo de contenedores  | Es un panel de control que muestra información correspondiente a un determinado grupo de contenedores.  |
| Panel de control Multi-cf-app | Es un panel de control que muestra información correspondiente a todas las aplicaciones Cloud Foundry desplegadas en el mismo espacio.  | 
| Panel de control multicontenedor | Es un panel de control que muestra información correspondiente a todos los contenedores desplegados en el mismo espacio.  |
| Panel de control Espacio | Este es un panel de control que muestra datos de registro disponibles en un espacio.  | 
{: caption="Tabla 1. Ejemplos de tipos de paneles de control" caption-side="top"}

Para visualizar los datos de un panel de control, puede configurar paneles. Kibana incluye distintas visualizaciones, como tabla, tendencias e histograma, que puede utilizar para analizar la información. Una visualización se añade como un panel a un panel de control. Puede añadir, eliminar y cambiar la disposición de los paneles del panel de control. El objetivo de cada panel varía. Algunos paneles se organizan en filas que proporcionan los resultados de una o varias consultas. Otros paneles muestran documentos o información personalizada. Cada panel se basa en una búsqueda. La búsqueda define el subconjunto de datos que muestra el panel. Por ejemplo, puede configurar un diagrama de barras, un diagrama circular o una tabla para visualizar los datos y analizarlos.  

En la tabla siguiente se muestran las diferentes tareas que puede llevar a cabo en la página Panel de control:

| Tarea | Más información |
|------|------------------|
| [Añadir una visualización](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#add_visualization) | Puede añadir una visualización existente o una búsqueda a un panel de control.|
| [Crear un nuevo panel de control](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#new) | Puede crear varios paneles de control. Cada panel de control se puede diseñar de modo que incluya distintas búsquedas, visualizaciones y un subconjunto diferente de datos de registro.  |
| [Suprimir un panel de control](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#delete) | Suprima los paneles de control que ya no necesite. |
| [Exportar un panel de control](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#export) | Puede exportar un panel de control como archivo JSON. |
| [Importar un panel de control](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#import) | Puede importar un panel de control como archivo JSON. |
| [Cargar un panel de control](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#reload3) | Puede cargar un panel de control para actualizar sus datos, modificarlo o analizar los datos. |
| [Guardar un panel de control](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#save) | Puede guardar un panel de control para reutilizarlo en el futuro. |
{: caption="Tabla 2. Tareas para trabajar con paneles de control" caption-side="top"}

Para obtener más información sobre Kibana, consulte la [Guía del usuario de Kibana ![Icono de enlace externo](../../../icons/launch-glyph.svg "Icono de enlace externo")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}.


## Adición de una nueva búsqueda o visualización
{: #add_visualization}

Siga estos pasos para añadir una visualización o búsqueda existente:

1. En la barra de herramientas de la página Panel de control, pulse **Añadir**. 

    **Nota**: Puede añadir visualizaciones y búsquedas. 

2. Seleccione el separador **Visualizaciones** para añadir una visualización o seleccione el separador **Búsquedas** para añadir una búsqueda.

3. Pulse sobre la búsqueda o visualización que desee añadir.

    Se añade al panel de control un panel correspondiente a la búsqueda o visualización.

	
## Creación de un nuevo panel de control de Kibana
{: #new}

Siga los siguientes pasos para crear un nuevo panel de control:

1. En la barra de herramientas de la página Panel de control, pulse **Añadir**. 

2. Añada una o varias búsquedas y visualizaciones. Para obtener más información, consulte [Adición de una nueva búsqueda o visualización](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#add_visualization).

    Cuando añade una búsqueda o una visualización, se añade un panel al panel de control.

3. Arrastre un panel y suéltelo en la parte del panel de control en el que lo desea colocar.
 
4. Guarde el panel de control para su reutilización en el futuro. Para obtener más información, consulte [Cómo guardar un panel de control de Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#save).


## Supresión de un panel de control de Kibana
{: #delete1}

Para suprimir un panel de control, siga los pasos siguientes en la página **Gestión**:

1. En la página **Gestión**, seleccione **Objetos guardados**.

2. En el separador **Paneles de control**, seleccione el panel de control que desea suprimir.

3. Pulse **Suprimir**.

## Exportación de un panel de control de Kibana
{: #export}

Para exportar un panel de control como archivo JSON, siga los pasos siguientes en la página **Gestión**:

1. En la página **Gestión**, seleccione **Objetos guardados**.

2. En el separador **Panel de control**, seleccione el panel de control que desea exportar.

3. Pulse **Exportar**.

4. Guarde el archivo.

## Importación de un panel de control de Kibana
{: #import}

Para importar un panel de control como archivo JSON, siga los pasos siguientes en la página **Gestión**:

1. En la página **Gestión**, seleccione **Objetos guardados**.

2. En el separador **Panel de control**, seleccione **Importar**.

3. Seleccione un archivo y pulse **Abrir**.

El panel de control se añade a la lista de paneles de control.

## Carga de un panel de control de Kibana
{: #reload3}

Siga los siguientes pasos para cargar un nuevo panel de control guardado:

1. En la barra de herramientas de la página Panel de control, pulse **Abrir**.

2. Seleccione un panel de control de la lista de paneles de control disponibles que se muestra en el campo *Nombre*.

También puede buscar un panel de control desde la barra de búsqueda.

## Cómo guardar un panel de control de Kibana
{: #save}

Siga los pasos siguientes para guardar un panel de control de Kibana después de personalizarlo:

1. En la barra de herramientas, pulse **Guardar**.

2. Escriba un nombre para el panel de control.

    **Nota:** el nombre no debe incluir espacios.

3. Pulse **Guardar**.




