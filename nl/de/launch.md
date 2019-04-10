---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, web UI, browser

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

# Zur Webbenutzerschnittstelle navigieren
{: #launch}

Nach der Bereitstellung einer Instanz des {{site.data.keyword.la_full_notm}}-Service in {{site.data.keyword.cloud_notm}} und der Konfiguration eines LogDNA-Agenten für eine Protokolldatenquelle können Sie Protokolle über die Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}} anzeigen, überwachen und verwalten.
{:shortdesc}


## Einem Benutzer IAM-Richtlinien zum Anzeigen von Daten gewähren 
{: #step1}

**Anmerkung:** Sie müssen Administrator des {{site.data.keyword.la_full_notm}}-Service oder einer {{site.data.keyword.la_full_notm}}-Instanz sein oder im Konto über IAM-Berechtigungen verfügen, anderen Benutzern Richtlinien zu gewähren.

Die folgende Tabelle enthält eine Auflistung der Richtlinien, die ein Benutzer mindestens benötigt, um die Webbenutzerschnittstelle starten und Daten anzeigen zu können:

| Service                              | Rolle                      | Erteilte Berechtigung       |
|--------------------------------------|---------------------------|---------------------|
| `{{site.data.keyword.la_full_notm}}` | Plattformrolle: Anzeigeberechtigter     | Der Benutzer kann die Liste der Serviceinstanzen im Dashboard Beobachtbarkeit - Protokollierung anzeigen. |
| `{{site.data.keyword.la_full_notm}}` | Servicerolle: Schreibberechtigter      | Der Benutzer kann die Webbenutzerschnittstelle starten und Protokolle in der Webbenutzerschnittstelle anzeigen.    |
{: caption="Tabelle 1. IAM-Richtlinien" caption-side="top"} 

Weitere Informationen zur Konfiguration dieser Richtlinien für einen Benutzer finden Sie in [Benutzer Berechtigungen zum Anzeigen von Protokollen in LogDNA erteilen](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna).


## Webbenutzerschnittstelle über die {{site.data.keyword.cloud_notm}}-Benutzerschnittstelle starten
{: #launch_step2}

Sie starten die Webbenutzerschnittstelle im Kontext einer {{site.data.keyword.la_full_notm}}-Instanz über die {{site.data.keyword.cloud_notm}}-Benutzerschnittstelle. 

Führen Sie die folgenden Schritte aus, um die Webbenutzerschnittstelle zu starten:

1. Melden Sie sich bei Ihrem {{site.data.keyword.cloud_notm}}-Konto an.

    Klicken Sie auf [{{site.data.keyword.cloud_notm}}-Dashboard ![Symbol für externen Link](../../icons/launch-glyph.svg "Symbol für externen Link")](https://cloud.ibm.com/login){:new_window}, um das {{site.data.keyword.cloud_notm}}-Dashboard zu starten.

	Nach der Anmeldung mit Ihrer Benutzer-ID und Ihrem Kennwort wird das {{site.data.keyword.cloud_notm}}-Dashboard geöffnet.

2. Wählen Sie im Navigationsmenü **Beobachtbarkeit** aus. 

3. Wählen Sie **Protokollierung** aus. 

    Die Liste der in {{site.data.keyword.cloud_notm}} verfügbaren Instanzen wird angezeigt.

4. Wählen Sie eine Instanz aus. Klicken Sie dann auf **LogDNA anzeigen**.

Die Webbenutzerschnittstelle wird geöffnet.


## URL der Webbenutzerschnittstelle aus {{site.data.keyword.cloud_notm}} abrufen
{: #launch_get}

Führen Sie die folgenden Schritte von einem Terminal aus, um die URL der Webbenutzerschnittstelle abzurufen:

1. Legen Sie die Ressourcengruppe fest, in der die {{site.data.keyword.la_full_notm}}-Instanz bereitgestellt wird.

    ```
    export logdna_rg_name=<Name_der_Ressourcengruppen_in_der_LogDNA-Instanz_erstellt_wird>
    ```
    {: codeblock}

2. Legen Sie den Namen der {{site.data.keyword.la_full_notm}}-Instanz fest.

    ```
    export logdna_instance_name=<Ihr_LogDNA-Instanzname>
    ```
    {: codeblock}

3. Legen Sie den Endpunkt fest.

    ```
    export rc_endpoint=resource-controller.cloud.ibm.com
    ```
    {: codeblock}

4. Legen Sie das IAM-Token fest.

    ```
    export iam_token=$(ibmcloud iam oauth-tokens | grep IAM | grep -oP  "eyJ.*")
    ```
    {: codeblock}

    **Anmerkung:** Wenn Sie an einem MacOS-Terminal arbeiten, lautet der Befehl wie folgt: `export iam_token=$(ic iam oauth-tokens | grep IAM | grep -o  "eyJ.*")`

5. Legen Sie die ID der Ressourcengruppe fest.

    ```
    export resource_group_id=$(ibmcloud resource groups | grep "^$logdna_rg_name" | awk '{print $2}')
    ```
    {: codeblock}

6. Legen Sie die URL der Webbenutzerschnittstelle in einer Variablen fest.

    ```
    export dashboard_url=$(curl -H "Accept: application/json" -H "Authorization: Bearer $iam_token" "https://$rc_endpoint/v1/resource_instances?resource_group_id=$resource_group_id&type=service_instance" | jq ".resources[] | select(.name==\"$logdna_instance_name\") | .dashboard_url")
    ```
    {: codeblock}

7. Rufen Sie die URL der Webbenutzerschnittstelle ab.

    ```
    echo $dashboard_url
    ```
    {: codeblock}

    

