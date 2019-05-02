---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging instance, delete

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

# Instanz entfernen
{: #remove}

Sie können eine Instanz des {{site.data.keyword.la_full_notm}}-Service über die {{site.data.keyword.Bluemix}}-Benutzerschnittstelle oder über die Befehlszeile entfernen.
{:shortdesc}

Wenn Sie eine Instanz aus {{site.data.keyword.cloud_notm}} entfernen, führen Sie eine Bereinigung wie folgt durch:

1. Notieren Sie die Liste der Quellen, die Metriken an die {{site.data.keyword.la_full_notm}}-Instanz weiterleiten, die Sie entfernen wollen. Sie müssen den LogDNA-Agenten aus jeder Quelle entfernen.
2. Entfernen Sie die Berechtigungen, die Benutzern für die Arbeit mit der Instanz erteilt wurden. 

    Wenn Sie den Zugriff mit dedizierten Zugriffsgruppen für die Arbeit mit einer bestimmten Instanz verwalten, müssen Sie diese Zugriffsgruppen entfernen.

    Wenn Sie den Zugriff auf mehrere Protokollierungsinstanzen mithilfe von Zugriffsgruppen verwalten, müssen Sie die Richtlinien entfernen, die der zu entfernenden Instanz Berechtigungen erteilen.
    
    Wenn Sie Benutzern einzelne Richtlinien zuweisen, müssen Sie die Liste der Benutzer zusammenstellen, die über Berechtigungen zum Arbeiten mit dieser Instanz verfügen. Dann müssen Sie für jeden identifizierten Benutzer die Richtlinien entfernen, die sich auf die zu löschende Instanz beziehen.


Löschen Sie anschließend die Instanz aus dem {{site.data.keyword.cloud_notm}}-Dashboard.


## Instanz über die {{site.data.keyword.cloud_notm}}-Benutzerschnittstelle entfernen
{: #remove_ui}

Führen Sie die folgenden Schritte aus, um eine {{site.data.keyword.la_full_notm}}-Instanz über die {{site.data.keyword.cloud_notm}}-Benutzerschnittstelle zu entfernen:

1. Melden Sie sich bei Ihrem {{site.data.keyword.cloud_notm}}-Konto an.

    Klicken Sie auf [{{site.data.keyword.cloud_notm}}-Dashboard ![Symbol für externen Link](../../icons/launch-glyph.svg "Symbol für externen Link")](https://cloud.ibm.com/login){:new_window}, um das {{site.data.keyword.cloud_notm}}-Dashboard zu starten.

	Nach der Anmeldung mit Ihrer Benutzer-ID und Ihrem Kennwort wird die Benutzerschnittstelle von {{site.data.keyword.cloud_notm}} geöffnet.

2. Rufen Sie das Menüsymbol ![Menüsymbol](../../icons/icon_hamburger.svg) &gt; **Beobachtbarkeit** auf, um auf das Dashboard *Beobachtbarkeit* zuzugreifen.

3. Wählen Sie **Protokollierung** aus. Die Liste der Protokollierungsinstanzen wird angezeigt.

4. Wählen Sie die Instanz aus, die Sie löschen wollen.

5. Wählen Sie **Entfernen** im Menü *Aktion* aus.


## Instanz über die Befehlszeilenschnittstelle entfernen
{: #remove_cli}

Führen Sie die folgenden Schritte aus, um eine {{site.data.keyword.la_full_notm}}-Instanz über die Befehlszeile zu entfernen:

1. [Voraussetzung] Installieren Sie die Befehlszeilenschnittstelle von {{site.data.keyword.cloud_notm}}.

   Weitere Informationen finden Sie in [{{site.data.keyword.cloud_notm}}-CLI installieren](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli).

   Ist die Befehlszeilenschnittstelle installiert, fahren Sie mit dem nächsten Schritt fort.

2. Melden Sie sich bei der Region in {{site.data.keyword.cloud_notm}} an, in der die Instanz bereitgestellt werden soll. Führen Sie den folgenden Befehl aus: [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Legen Sie die Ressourcengruppe fest, in der die Instanz bereitgestellt wird. Führen Sie den folgenden Befehl aus: [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    Die Ressourcengruppe *Standard* ist standardmäßig festgelegt.

4. Entfernen Sie die Instanz. Führen Sie den Befehl [`ibmcloud resource service-instance-delete`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_delete) aus:

    ```
    ibmcloud resource service-instance-delete NAME 
    ```
    {: codeblock}

    Hierbei ist NAME der Name der Instanz.

    Führen Sie beispielsweise den folgenden Befehl aus, um eine Instanz zu entfernen:

    ```
    ibmcloud resource service-instance-delete logdna-instance-01
    ```
    {: codeblock}



