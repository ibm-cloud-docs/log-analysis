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

# Berechtigungen zum Verwalten von Protokollen und zum Anzeigen von Kontoprotokollen erteilen
{: #grant_permissions}

In {{site.data.keyword.Bluemix}} können Sie einem Benutzer eine oder mehrere IAM-Rollen zuweisen. Diese Rollen definieren, welche Tasks für diesen Benutzer für die Arbeit mit dem {{site.data.keyword.loganalysisshort}}-Service aktiviert sind.  
{:shortdesc}

Sie können einem Benutzer beispielsweise die Rolle **operator** erteilen, um ihm die Verwaltung von Protokollen zu ermöglichen. Wenn Sie einem Benutzer nur das Anzeigen von Protokollen ermöglichen möchten, können Sie diesem Benutzer die Rolle **viewer** erteilen. Weitere Informationen finden Sie unter [IAM-Rollen](/docs/services/CloudLogAnalysis/security_ov.html#iam_roles).

**Hinweis:** 

* Um einem Benutzer Berechtigungen zum Verwalten von Protokollen oder zum Anzeigen von Kontoprotokollen zu erteilen, müssen Sie über Berechtigungen zum Zuweisen von Richtlinien für andere Benutzer im Konto verfügen oder Sie müssen der Kontoinhaber sein. Wenn Sie nicht der Kontoinhaber sind, benötigen Sie eine IAM-Richtlinie mit einer Rolle als Editor, Operator oder Administrator.
* Um einem Benutzer Berechtigungen zum Anzeigen von Protokollen in einem Bereich zu erteilen, müssen Sie über Berechtigungen in der Organisation und im Bereich verfügen, um dem Benutzer eine Cloud Foundry-Rolle zuzuweisen, die die Aktionen beschreibt, die dieser Benutzer mit dem {{site.data.keyword.loganalysisshort}}-Service in diesem Bereich ausführen kann. 

## Einem Benutzer über die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle eine IAM-Richtlinie zuweisen
{: #grant_permissions_ui_account}

Führen Sie die folgenden Schritte aus, um einem Benutzer Berechtigungen für die Arbeit mit dem {{site.data.keyword.loganalysisshort}}-Service zu erteilen:

1. Melden Sie sich bei der {{site.data.keyword.Bluemix_notm}}-Konsole an.

    Öffnen Sie einen Web-Browser und starten Sie das {{site.data.keyword.Bluemix_notm}}-Dashboard: [http://bluemix.net ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](http://bluemix.net){:new_window}
	
	Nach der Anmeldung mit Ihrer Benutzer-ID und Ihrem Kennwort wird die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle geöffnet.

2. Klicken Sie in der Menüleiste auf **Verwalten > Konto > Benutzer**. 

    Im Fenster *Benutzer* wird eine Liste mit Benutzern und den entsprechenden E-Mail-Adressen für das aktuell ausgewählte Konto angezeigt.
	
3. Wenn der Benutzer ein Mitglied des Kontos ist, wählen Sie den Benutzernamen aus der Liste aus oder klicken Sie im Menü *Aktionen* auf **Benutzer verwalten**.

    Wenn der Benutzer kein Mitglied des Kontos ist, finden Sie unter [Benutzer einladen](/docs/iam/iamuserinv.html#iamuserinv) Informationen zum entsprechenden Vorgehen in diesem Fall.

4. Klicken Sie im Abschnitt **Zugriffsrichtlinien** auf **Zugriff zuweisen** und wählen Sie anschließend **Zugriff auf Ressourcen zuweisen**.

    Das Fenster *Ressourcenzugriff an Benutzer zuweisen** wird geöffnet.

5. Geben Sie Informationen zu der Richtlinie ein. In der folgenden Tabelle sind die Felder aufgeführt, die zum Definieren einer Richtlinie erforderlich sind: 

    <table>
	  <caption>Liste von Feldern für die Konfiguration einer IAM-Richtlinie.</caption>
	  <tr>
	    <th>Feld</th>
		<th>Wert</th>
	  </tr>
	  <tr>
	    <td>Services</td>
		<td>*IBM Cloud Log Analysis*</td>
	  </tr>	  
	  <tr>
	    <td>Regionen</td>
		<td>Sie können die Regionen angeben, für die der Benutzer Zugriff für die Arbeit mit Protokollen erhält. Wählen Sie nacheinander eine oder mehrere Regionen aus oder wählen Sie **Alle aktuellen Regionen** aus, um Zugriff auf alle Regionen zu erteilen.</td>
	  </tr>
	  <tr>
	    <td>Serviceinstanz</td>
		<td>Wählen Sie *Alle Serviceinstanzen* aus.</td>
	  </tr>
	  <tr>
	    <td>Rollen</td>
		<td>Wählen Sie eine oder mehrere IAM-Rollen aus. <br>Gültige Rollen sind: *Administrator*, *Operator*, *Editor* und *Anzeigeberechtigter*. <br>Weitere Informationen zu den Aktionen, die pro Rolle zulässig sind, finden Sie unter [IAM-Rollen](/docs/services/CloudLogAnalysis/security_ov.html#iam_roles).
		</td>
	  </tr>
     </table>
	
6. Klicken Sie auf **Zuweisen**.
	
Die von Ihnen konfigurierte Richtlinie gilt für die ausgewählten Regionen. 


## Einem Benutzer über die Befehlszeile eine IAM-Richtlinie zuweisen
{: #grant_permissions_commandline}

Führen Sie die folgenden Schritte aus, um einem Benutzer über die Befehlszeile Zugriff zum Anzeigen von Kontoprotokollen zu erteilen:

1. Meldne Sie sich über ein Terminal beim {{site.data.keyword.Bluemix_notm}}-Konto an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Überprüfen Sie, ob der Benutzer ein Mitglied für das Konto ist. Führen Sie den folgenden Befehl aus, um die Liste der Benutzer im Konto abzurufen:

    ```
	ibmcloud account users
	```
    {: codeblock}	

	Es wird eine Liste von Benutzern mit ihren jeweiligen GUIDs angezeigt.

3. Wenn der Benutzer kein Mitglied des Kontos ist, wenden Sie sich an den Kontoeigner und fordern Sie eine Einladung dieses Benutzers für das Konto an. Weitere Informationen finden Sie in [Benutzer einladen](/docs/iam/iamuserinv.html#iamuserinv).

    **Tipp:** Der Befehl zum Einladen eines Benutzers zu einem Konto lautet wie folgt: `ibmcloud iam account-user-invite USER_EMAIL`
		
4. Weisen Sie dem Benutzer eine Richtlinie zu. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud iam user-policy-create USER_NAME --roles ROLE --service-name ibmloganalysis
	```
	{: codeblock}

	Dabei gilt:
    * USER_NAME ist die {{site.data.keyword.Bluemix_notm}}-ID des Benutzers.
	* ROLE ist eine IAM-Rolle. Gültige Werte sind: *Administrator*, *Operator*, *Editor* und *Anzeigeberechtigter*.

5. Überprüfen Sie, ob die Richtlinie dem Benutzer zugewiesen wurde. Führen Sie den folgenden Befehl aus, um alle einem Benutzer zugewiesenen Richtlinien aufzulisten:

    ```
    ibmcloud iam user-policies USER_NAME
	```
	{: codeblock}




## Einem Benutzer über die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle Berechtigungen zum Anzeigen von Bereichsprotokollen erteilen
{: #grant_permissions_ui_space}

Um einem Benutzer Berechtigungen zum Anzeigen von Protokollen in einem Bereich zu erteilen, müssen Sie dem Benutzer eine Cloud Foundry-Rolle zuweisen, die die Aktionen beschreibt, die dieser Benutzer mit dem {{site.data.keyword.loganalysisshort}}-Service im Bereich ausführen kann. 

Führen Sie die folgenden Schritte aus, um einem Benutzer Berechtigungen für die Arbeit mit dem {{site.data.keyword.loganalysisshort}}-Service zu erteilen:

1. Melden Sie sich bei der {{site.data.keyword.Bluemix_notm}}-Konsole an.

    Öffnen Sie einen Web-Browser und starten Sie das {{site.data.keyword.Bluemix_notm}}-Dashboard: [http://bluemix.net ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](http://bluemix.net){:new_window}
	
	Nach der Anmeldung mit Ihrer Benutzer-ID und Ihrem Kennwort wird die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle geöffnet.

2. Klicken Sie in der Menüleiste auf **Verwalten > Konto > Benutzer**. 

    Im Fenster *Benutzer* wird eine Liste mit Benutzern und den entsprechenden E-Mail-Adressen für das aktuell ausgewählte Konto angezeigt.
	
3. Wenn der Benutzer ein Mitglied des Kontos ist, wählen Sie den Benutzernamen aus der Liste aus oder klicken Sie im Menü *Aktionen* auf **Benutzer verwalten**.

    Wenn der Benutzer kein Mitglied des Kontos ist, finden Sie unter [Benutzer einladen](/docs/iam/iamuserinv.html#iamuserinv) Informationen zum entsprechenden Vorgehen in diesem Fall.

4. Wählen Sie **Cloud Foundry-Zugriff** und anschließend die Organisation aus.

    Die in dieser Organisation verfügbaren Bereiche werden aufgelistet.

5. Wählen Sie nur einen Bereich aus. Anschließend wählen Sie aus der Menüaktion **Bereichsrolle bearbeiten** aus.

6. Wählen Sie mindestens eine Bereichsrolle aus. Gültige Rollen sind: *Manager*, *Entwickler* und *Prüfer*
	
7. Klicken Sie auf **Rolle speichern**.




