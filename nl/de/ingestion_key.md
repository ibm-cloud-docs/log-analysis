---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion key

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

# Mit Aufnahmeschlüsseln arbeiten
{: #ingestion_key}

Der Aufnahmeschlüssel ist ein Sicherheitsschlüssel, den Sie für die Konfiguration von LogDNA-Agenten und für eine erfolgreiche Weiterleitung von Protokollen an Ihre {{site.data.keyword.la_full_notm}}-Instanz in {{site.data.keyword.cloud_notm}} verwenden müssen. Sie erhalten den Aufnahmeschlüssel automatisch, wenn Sie eine Instanz bereitstellen. Sie können den Aufnahmeschlüssel auch durch die Erstellung einer Service-ID für die Instanz erhalten. 
{:shortdesc}

**Anmerkung:** 

* Damit Sie über die Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}} mit Aufnahmeschlüsseln arbeiten können, benötigen Sie eine IAM-Richtlinie mit der Plattformrolle **Anzeigeberechtigter** und der Servicerolle **Manager** für den {{site.data.keyword.la_full_notm}}-Service. 
* Damit Sie über die Benutzerschnittstelle von {{site.data.keyword.cloud_notm}} mit Aufnahmeschlüsseln arbeiten können, benötigen Sie eine IAM-Richtlinie mit der Plattformrolle **Bearbeiter** und der Servicerolle **Manager** für den {{site.data.keyword.la_full_notm}}-Service. 


## Aufnahmeschlüssel über {{site.data.keyword.cloud_notm}}-Benutzerschnittstelle abrufen
{: #ibm_cloud_ui}

Führen Sie die folgenden Schritte aus, um den Aufnahmeschlüssel für eine {{site.data.keyword.la_full_notm}}-Instanz über die {{site.data.keyword.cloud_notm}}-Benutzerschnittstelle abzurufen:

1. Melden Sie sich bei Ihrem {{site.data.keyword.cloud_notm}}-Konto an.

    Klicken Sie auf [{{site.data.keyword.cloud_notm}}-Dashboard ![Symbol für externen Link](../../icons/launch-glyph.svg "Symbol für externen Link")](https://cloud.ibm.com/login){:new_window}, um das {{site.data.keyword.cloud_notm}}-Dashboard zu starten.

	Nach der Anmeldung mit Ihrer Benutzer-ID und Ihrem Kennwort wird die Benutzerschnittstelle von {{site.data.keyword.cloud_notm}} geöffnet.

2. Wählen Sie im Navigationsmenü **Beobachtbarkeit** aus. 

3. Wählen Sie **Protokollierung** aus. Das {{site.data.keyword.la_full_notm}}-Dashboard wird geöffnet. Die Liste der in {{site.data.keyword.cloud_notm}} verfügbaren Protokollierungsinstanzen wird angezeigt.

3. Geben Sie die Instanz an, für die Sie den Aufnahmeschlüssel abrufen wollen, und klicken Sie auf **Aufnahmeschlüssel anzeigen**.

4. In dem daraufhin geöffneten Fenster können Sie auf **Anzeigen** klicken, um den Aufnahmeschlüssel anzuzeigen.


## Aufnahmeschlüssel über die Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}} abrufen
{: #logdna_ui}

Führen Sie die folgenden Schritte aus, um den Aufnahmeschlüssel für eine {{site.data.keyword.la_full_notm}}-Instanz über die Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}} abzurufen:

1. Starten Sie die Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}}. Weitere Informationen finden Sie unter [Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}} starten](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Wählen Sie das Symbol **Konfiguration** aus. Wählen Sie dann **Organisation** aus. 

3. Wählen Sie **API-Schlüssel** aus.

Die erstellten Aufnahmeschlüssel werden angezeigt. 

**Anmerkung: ** Es ist nur jeweils ein Aufnahmeschlüssel aktiv. 


## Aufnahmeschlüssel über {{site.data.keyword.cloud_notm}}-Befehlszeilenschnittstelle abrufen
{: #ibm_cloud_cli}

Führen Sie die folgenden Schritte aus, um den Aufnahmeschlüssel für eine {{site.data.keyword.la_full_notm}}-Instanz über die Befehlszeile abzurufen:

1. [Voraussetzung] Installieren Sie die Befehlszeilenschnittstelle von {{site.data.keyword.cloud_notm}}.

   Weitere Informationen finden Sie unter [{{site.data.keyword.cloud_notm}}-Befehlszeilenschnittstelle installieren](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).

   Ist die Befehlszeilenschnittstelle installiert, fahren Sie mit dem nächsten Schritt fort.

2. Melden Sie sich bei der Region in {{site.data.keyword.cloud_notm}} an, in der die Instanz ausgeführt wird. Führen Sie den folgenden Befehl aus: [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Legen Sie die Ressourcengruppe fest, in der die {{site.data.keyword.la_full_notm}}-Instanz ausgeführt wird. Führen Sie den Befehl [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target) mit der Option `-g` aus.

    Die Ressourcengruppe `Standard` ist standardmäßig festgelegt.

4. Rufen Sie den Namen des API-Schlüssels ab, der der {{site.data.keyword.la_full_notm}}-Instanz zugeordnet ist. Führen Sie den Befehl [`ibmcloud resource service-keys`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_keys) aus:

    ```
    ibmcloud resource service-keys
    ```
    {: codeblock}

    Geben Sie den Serviceschlüssel an, der Ihrer Instanz zugeordnet ist.

5. Rufen Sie den Aufnahmeschlüssel ab. Führen Sie den Befehl [`ibmcloud resource service-key`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_key) aus:

    ```
    ibmcloud resource service-key APIKEY_NAME
    ```
    {: codeblock}

    Hierbei ist APIKEY_NAME der Name des API-Schlüssels.
 
    Die Ausgabe dieses Befehls enthält das Feld **ingestion_key**, das den Aufnahmeschlüssel für die Instanz enthält.


## Aufnahmeschlüssel zurücksetzen 
{: #reset}

Wenn der Aufnahmeschlüssel beschädigt ist oder wenn eine Erneuerung des Schlüssels nach einem bestimmten Zeitraum durch eine Richtlinie festgelegt ist, können Sie einen neuen Schlüssel generieren und den alten Schlüssel löschen.

Führen Sie die folgenden Schritte aus, um den Aufnahmeschlüssel für eine {{site.data.keyword.la_full_notm}}-Instanz über die Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}} zu erneuern:

1. Starten Sie die Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}}. Weitere Informationen finden Sie unter [Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}} starten](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Wählen Sie das Symbol **Konfiguration** aus. Wählen Sie dann **Organisation** aus. 

3. Wählen Sie **API-Schlüssel** aus.

    Die erstellten Aufnahmeschlüssel werden angezeigt. 

4. Wählen Sie **Aufnahmeschlüssel generieren** aus.

    Der Liste wird ein neuer Schlüssel hinzugefügt.

5. Löschen Sie den alten Aufnahmeschlüssel. Klicken Sie auf **Löschen**.

**Anmerkung:** Nach dem Zurücksetzen des Aufnahmeschlüssels müssen Sie den Aufnahmeschlüssel für alle Protokollquellen aktualisieren, die Sie für die Weiterleitung von Protokollen an diese {{site.data.keyword.la_full_notm}}-Instanz konfiguriert haben.



