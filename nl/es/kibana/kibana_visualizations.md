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

# Análisis de registros en Kibana mediante visualizaciones 
{:#kibana_visualizations}

Utilice la página *Visualizar* de Kibana para crear visualizaciones, como gráficos y tablas, que puede utilizar para analizar los datos de registro y comparara los resultados. 
{:shortdesc}

Puede utilizar una visualización de forma individual para analizar los registros. 

* Puede crear visualizaciones a partir de una búsqueda que defina y guarde en la página *Descubrir* o a partir de una nueva consulta que defina en la página *Visualizar*. La búsqueda define el subconjunto de datos que muestra una visualización.

* El tipo de visualización que elija determina cómo se visualizan los datos para su análisis.

En la tabla siguiente encontrará los distintos tipos de visualizaciones:

| Tipo de visualización | Descripción |
|-----------------------|-------------|
| Gráfico de áreas | Muestra gráficamente datos cuantitativos. Utilícelo para comparar dos o más conjuntos de datos agregados. |
| Tabla de datos | Muestra datos sin formato en formato de tabla para una agregación compuesta. |
| Gráfico de líneas | Muestra los datos que se basan en tiempo. Utilícelo para comparar dos o más conjuntos de datos agregados basados en tiempo. |
| Widget Markdown | Utilícelo para ver información de texto. |
| Métrica | Utilícelo para ver un recuento de aciertos o el promedio exacto de un campo numérico. |
| Gráfico circular | Utilícelo para ver los distintos valores de un campo. | 
| Gráfico de barras verticales | Muestra datos basados en tiempo y datos que no se basan en tiempo. Utilícelo para agrupar datos. |
{: caption="Tabla 1. Tipos de visualización" caption-side="top"}

En la página Visualizar, puede realizar cualquiera de las siguientes tareas:

| Tarea | Más información |
|------|------------------|
| [Crear una nueva visualización](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#create) | Puede crear visualizaciones a partir de una búsqueda que defina y guarde en la página *Descubrir* o a partir de una nueva consulta que defina en la página *Visualizar*. |
| [Suprimir una visualización](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#delete) | Suprima las visualizaciones que ya no necesite. |
| [Exportar una visualización](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#export) | Puede exportar una visualización como archivo JSON.  |
| [Importar una visualización](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#import1) | Puede importar una visualización como archivo JSON.  |
| [Cargar una visualización](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#reload2) | Puede cargar una visualización para actualizar sus datos, modificarlos o analizar los datos. |
| [Guardar una visualización](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#save2) | Puede guardar visualizaciones para reutilizarlas en el futuro. |
{: caption="Tabla 2. Tareas para trabajar con visualizaciones" caption-side="top"}


## Creación de visualizaciones a partir de consultas en Kibana
{: #create}

Complete los siguientes pasos para crear una visualización desde la página Visualizar:

1. Inicie Kibana y seleccione la página **Visualizar**.

2. Elija un tipo de visualización, por ejemplo *tabla*.

3. Seleccione una visualización que haya guardado anteriormente en **O, desde una búsqueda guardada**, o bien seleccione un índice en la sección **Desde una nueva búsqueda, seleccionar índice**.

4. Configure la consulta.

    * Si selecciona **O, desde una búsqueda guardada**, seleccione una consulta de búsqueda. La consulta se utiliza para recuperar los datos que se utilizan para la visualización. 
	
	    Después de seleccionar una búsqueda, se abre el programa de creación de visualizaciones y carga los datos correspondientes a la consulta seleccionada. 
		
		**Nota**: los cambios que realice en una búsqueda guardada se reflejan automáticamente en la visualización. Para inhabilitar las actualizaciones automáticas que realice en la consulta que está enlazada a esta visualización, efectúe una doble pulsación en el mensaje *Esta visualización está enlazada a una búsqueda guardada: your_search_name* 

    * Si selecciona **Desde una nueva búsqueda, seleccionar índice**, defina una consulta nueva. La consulta se utiliza para definir el subconjunto de datos que recupera y utiliza la visualización.

        Para obtener más información, consulte [Filtrado de registros mediante la definición de consultas personalizadas](/docs/services/CloudLogAnalysis/kibana/define_search.html#define_search).

Para obtener más información sobre Kibana, consulte la [Guía del usuario de Kibana ![Icono de enlace externo](../../../icons/launch-glyph.svg "Icono de enlace externo")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}.


## Supresión de una visualización
{: #delete}

Para suprimir una visualización, siga los pasos siguientes en la página **Gestión**:

1. En la página **Gestión**, seleccione **Objetos guardados**.

2. En el separador **Visualizaciones**, seleccione las visualizaciones que desea suprimir.

3. Pulse **Suprimir**.


## Exportación de una visualización
{: #export1}

Para exportar una visualización como archivo JSON, siga los pasos siguientes en la página **Gestión**:

1. En la página **Gestión**, seleccione **Objetos guardados**.

2. En el separador **Visualizaciones**, seleccione la visualización que desea exportar.

3. Pulse **Exportar**.

4. Guarde el archivo.

## Importación de una visualización
{: #import1}

Para importar una visualización como archivo JSON, siga los pasos siguientes en la página **Gestión**:

1. En la página **Gestión**, seleccione **Objetos guardados**.

2. En el separador **Visualizaciones**, seleccione **Importar**.

3. Seleccione un archivo y pulse **Abrir**.

La visualización se añade a la lista de visualizaciones.


 
## Carga de una visualización
{: #reload2}

Siga los siguientes pasos para cargar una visualización guardada:

1. En la barra de herramientas de la página Visualizar, pulse **Abrir**.

2. Seleccione la visualización que desea cargar. 


## Cómo guardar una visualización
{: #save2}

Siga los pasos siguientes para guardar una visualización en la página Visualizar:

1. En la barra de herramientas de la página Visualizar, pulse **Guardar**.

2. Escriba un nombre para la visualización.

3. Pulse Guardar. 


