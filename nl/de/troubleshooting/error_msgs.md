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


# Fehlernachrichten
{: #error_msgs}

Die folgenden Fehlernachrichten können angezeigt werden, wenn Sie den {{site.data.keyword.loganalysisshort}}-Service in {{site.data.keyword.Bluemix}} verwenden:
{:shortdesc}

## BXNLG020001W
{: #BXNLG020001W}

**Nachrichtenbeschreibung**

Sie haben das täglich Kontingent erreicht, das dem Bluemix-Bereich {Bereichs-GUID} für die {{site.data.keyword.loganalysisfull}}-Instanz {Instanz-GUID} zugewiesen ist. Die aktuelle tägliche Zuteilung beträgt 500 MB für den Log Search-Speicher; diese Daten werden im Log Search-Speicher für einen Zeitraum von drei Tagen aufbewahrt und können in dieser Zeit in Kibana durchsucht werden. Wenn Sie ein Upgrade durchführen möchten, um mehr Daten pro Tag im Log Search-Speicher speichern und auch alle Protokolle im Speicher 'Log Collection' aufbewahren zu können, führen Sie für den {{site.data.keyword.loganalysisshort}}-Serviceplan für diesen Bereich ein Upgrade durch. Weitere Informationen zu Serviceplänen und zum Upgrade Ihres Serviceplans finden Sie unter [Pläne](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).


**Nachrichtenerläuterung** 

Es kann eine Nachricht mit der ID *BXNLG020001W* angezeigt werden, wenn Sie das Kontingent für den Log Search-Speicher erreichen, das dem Lite-Serviceplan zugewiesen ist. Der Lite-Plan ist der ergänzende Serviceplan, der standardmäßig festgelegt ist, wenn Sie den {{site.data.keyword.loganalysisshort}}-Service in einem Bereich bereitstellen. Die aktuelle tägliche Zuteilung beträgt 500 MB für den Log Search-Speicher; diese Daten werden im Log Search-Speicher für einen Zeitraum von drei Tagen aufbewahrt und können in dieser Zeit in Kibana durchsucht werden.

**Wiederherstellung**

Wenn Sie ein Upgrade durchführen möchten, um mehr Daten pro Tag im Log Search-Speicher speichern und auch alle Protokolle im Speicher 'Log Collection' aufbewahren zu können, führen Sie für den {{site.data.keyword.loganalysisshort}}-Serviceplan für diesen Bereich ein Upgrade durch. Weitere Informationen zu Serviceplänen und zum Upgrade Ihres Serviceplans finden Sie unter [Pläne](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).


## BXNLG020002W 
{: #BXNLG020002W}


**Nachrichtenbeschreibung**

Sie haben das täglich Kontingent erreicht, das dem Bluemix-Bereich {Bereichs-GUID} für die {{site.data.keyword.loganalysisfull}}-Instanz {Instanz-GUID} zugewiesen ist.  Die aktuelle tägliche Zuteilung beträgt XXX für den Log Search-Speicher; diese Daten werden für einen Zeitraum von drei Tagen aufbewahrt und können in dieser Zeit in Kibana durchsucht werden. Dies hat keine Auswirkungen auf die Protokollspeicherungsrichtlinie im Log Collection-Speicher. Wenn Sie ein Upgrade durchführen möchten, um mehr Daten pro Tag im Log Search-Speicher speichern zu können, führen Sie für den {{site.data.keyword.loganalysisshort}}-Serviceplan für diesen Bereich ein Upgrade durch. Weitere Informationen zu Serviceplänen und zum Upgrade Ihres Serviceplans finden Sie unter [Pläne](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).

XXX steht für die Größe der durchsuchbaren Daten für den aktuellen Plan.

**Nachrichtenerläuterung** 

Sie haben das tägliche Kontingent erreicht, das dem Bereich {der Bereichs-GUID} für die {{site.data.keyword.loganalysisfull}}-Instanz {Instanz-GUID} zugewiesen ist.  Die aktuelle tägliche Zuteilung beträgt eine Datenmenge von 500 MB, 2 GB, 5 GB oder 10 GB für den Log Search-Speicher, die für einen Zeitraum von drei Tagen aufbewahrt wird und in dieser Zeit in Kibana durchsucht werden kann. Dies hat keine Auswirkungen auf die Protokollspeicherungsrichtlinie im Log Collection-Speicher.

**Wiederherstellung**

Wenn Sie ein Upgrade durchführen möchten, um mehr Daten pro Tag im Log Search-Speicher speichern zu können, führen Sie für den {{site.data.keyword.loganalysisshort}}-Serviceplan für diesen Bereich ein Upgrade durch. Weitere Informationen zu Serviceplänen und zum Upgrade Ihres Serviceplans finden Sie unter [Pläne](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).




