---

copyright:
  years:  2018, 2019
lastupdated: "2019-04-02"

keywords: LogDNA, IBM, Log Analysis, logging instance, provision

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

# Instanz bereitstellen
{: #provision}

Bevor Sie Protokolldaten mit {{site.data.keyword.la_full_notm}} überwachen und verwalten können, müssen Sie zuerst eine Instanz des Service in {{site.data.keyword.cloud_notm}} bereitstellen.
{:shortdesc}

Wenn Sie eine {{site.data.keyword.la_full_notm}}-Instanz in einer Public Cloud-Region bereitstellen wollen, müssen Sie den Serviceplan, der der Instanz zugeordnet ist, die Region, in der Ihre Protokolle erfasst werden, und den Plan, der den Aufbewahrungszeitraum für Ihre Protokolle festlegt, auswählen. Sie können einen Aufbewahrungszeitraum von 7, 14 oder 30 Tagen auswählen.

Als Alternative bietet {{site.data.keyword.la_full_notm}} einen Plan `Lite` an, mit dem Sie Ihre Protokolle beim Durchlaufen des Systems anzeigen können. Sie können Protokolle mithilfe des Protokoll-Tailings (Liveanzeige der aktuellen letzten Protokollzeilen) anzeigen. Darüber hinaus können Sie zur Vorbereitung auf ein Upgrade auf einen Plan mit einem längeren Aufbewahrungszeitraum Filter entwerfen. Dieser Plan hat einen Aufbewahrungszeitraum von 0 Tagen.


## Instanz über das Dashboard 'Beobachtbarkeit' bereitstellen
{: #provision_ui}

Führen Sie die folgenden Schritte aus, um eine Instanz über das Dashboard 'Beobachtbarkeit' in {{site.data.keyword.cloud_notm}} bereitzustellen:

1. Melden Sie sich bei Ihrem {{site.data.keyword.cloud_notm}}-Konto an.

    Das {{site.data.keyword.cloud_notm}}-Dashboard finden Sie unter: [{{site.data.keyword.cloud_notm}} Dashboard ![Symbol für externen Link](../../icons/launch-glyph.svg "Symbol für externen Link")](https://cloud.ibm.com/login){:new_window}.

	Nach der Anmeldung mit Ihrer Benutzer-ID und Ihrem Kennwort wird die Benutzerschnittstelle von {{site.data.keyword.cloud_notm}} geöffnet.

2. Rufen Sie das Menüsymbol ![Menüsymbol](../../icons/icon_hamburger.svg) auf. Wählen Sie dann **Beobachtbarkeit** aus, um auf das Dashboard *Beobachtbarkeit* zuzugreifen.

3. Wählen Sie **Protokollierung** aus und klicken Sie dann auf **Instanz erstellen**. 

4. Geben Sie einen Namen für die Serviceinstanz ein.

5. Wählen Sie eine Ressourcengruppe aus. 

    Die Ressourcengruppe **Standard** ist standardmäßig festgelegt.

    **Anmerkung:** Wenn Sie keine Ressourcengruppe auswählen können, überprüfen Sie, ob Sie in der Ressourcengruppe, in der die Instanz bereitgestellt werden soll, über Berechtigungen zum Bearbeiten verfügen.

6. Wählen Sie den Serviceplan `Lite` aus. 

    Der Plan 'Lite' ist standardmäßig festgelegt.

    Weitere Informationen zu anderen Serviceplänen finden Sie in [Preisstrukturpläne](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

7. Klicken Sie auf **Erstellen**.

Nachdem Sie eine Instanz bereitgestellt haben, wird das Dashboard *Protokollierung* geöffnet. 

Als Nächstes konfigurieren Sie eine Protokollquelle, indem Sie einen LogDNA-Agenten hinzufügen. Dieser Agent ist für die Erfassung und Weiterleitung von Protokollen an Ihre Instanz zuständig. 



## Instanz über den Katalog bereitstellen
{: #provision_catalog}

Führen Sie die folgenden Schritte aus, um eine {{site.data.keyword.la_full_notm}}-Instanz über den {{site.data.keyword.cloud_notm}}-Katalog bereitzustellen:

1. Melden Sie sich bei Ihrem {{site.data.keyword.cloud_notm}}-Konto an.

    Klicken Sie auf [{{site.data.keyword.cloud_notm}}-Dashboard ![Symbol für externen Link](../../icons/launch-glyph.svg "Symbol für externen Link")](https://cloud.ibm.com/login){:new_window}, um das {{site.data.keyword.cloud_notm}}-Dashboard zu starten.

	Nach der Anmeldung mit Ihrer Benutzer-ID und Ihrem Kennwort wird die Benutzerschnittstelle von {{site.data.keyword.cloud_notm}} geöffnet.

2. Klicken Sie auf **Katalog**. Die Liste der in {{site.data.keyword.cloud_notm}} verfügbaren Services wird geöffnet.

3. Wählen Sie die Kategorie **Entwicklertools** aus, um die angezeigte Liste der Services zu filtern.

4. Klicken Sie auf die Kachel **{{site.data.keyword.la_full_notm}}**. 

5. Geben Sie einen Namen für die Serviceinstanz ein.

6. Wählen Sie eine Ressourcengruppe aus. 

    Die Ressourcengruppe **Standard** ist standardmäßig festgelegt.

    **Anmerkung:** Wenn Sie keine Ressourcengruppe auswählen können, überprüfen Sie, ob Sie in der Ressourcengruppe, in der die Instanz bereitgestellt werden soll, über Berechtigungen zum Bearbeiten verfügen.

7. Wählen Sie den Serviceplan `Lite` aus. 

    Der Plan 'Lite' ist standardmäßig festgelegt.

    Weitere Informationen zu anderen Serviceplänen finden Sie in [Preisstrukturpläne](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

8. Klicken Sie auf **Erstellen**.

Nachdem Sie eine Instanz bereitgestellt haben, wird das Dashboard *Protokollierung* geöffnet. 

Als Nächstes konfigurieren Sie eine Protokollquelle, indem Sie einen LogDNA-Agenten hinzufügen. Dieser Agent ist für die Erfassung und Weiterleitung von Protokollen an Ihre Instanz zuständig. 



## Instanz über die Befehlszeilenschnittstelle bereitstellen
{: #provision_cli}

Führen Sie die folgenden Schritte aus, um eine {{site.data.keyword.la_full_notm}}-Instanz über die Befehlszeile bereitzustellen:

1. [Voraussetzung] Installieren Sie die Befehlszeilenschnittstelle von {{site.data.keyword.cloud_notm}}.

   Weitere Informationen finden Sie in [{{site.data.keyword.cloud_notm}}-CLI installieren](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli).

   Ist die Befehlszeilenschnittstelle installiert, fahren Sie mit dem nächsten Schritt fort.

2. Melden Sie sich bei der Region in {{site.data.keyword.cloud_notm}} an, in der die Instanz bereitgestellt werden soll. Führen Sie den folgenden Befehl aus: [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Legen Sie die Ressourcengruppe fest, in der die Instanz bereitgestellt werden soll. Führen Sie den folgenden Befehl aus: [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    Die Ressourcengruppe `Standard` ist standardmäßig festgelegt.

4. Erstellen Sie die Instanz. Führen Sie den Befehl [`ibmcloud resource service-instance-create`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_create) aus:

    ```
    ibmcloud resource service-instance-create NAME logdna SERVICE_PLAN_NAME LOCATION
    ```
    {: codeblock}

    Hierbei gilt Folgendes:

    NAME ist der Name der Instanz.

    Der Wert *logdna* ist der Name des {{site.data.keyword.la_full_notm}}-Service in {{site.data.keyword.cloud_notm}}.

    SERVICE_PLAN_NAME ist der Typ des Plans. Gültige Werte sind *lite*, *7-day*, *14-day*, *30-day*.
    
    LOCATION ist die Region, in der die LogDNA-Instanz erstellt wird. Gültige Werte sind *us-south*, *eu-de*.

    Soll beispielsweise eine Instanz mit dem Plan mit einem Aufbewahrungszeitraum von 7 Tagen bereitgestellt werden, führen Sie den folgenden Befehl aus:

    ```
    ibmcloud resource service-instance-create logdna-instance-01 logdna 7-day us-south
    ```
    {: codeblock}




