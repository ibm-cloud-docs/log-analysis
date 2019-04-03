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

# Protokollaufbewahrungsrichtlinie konfigurieren
{: #configuring_retention_policy1}

Mit dem Befehl **cf logging option** wird die Aufbewahrungsrichtlinie angezeigt und konfiguriert, die die Dauer (in Tagen) angibt, für die die Protokolle in 'Log Collection' aufbewahrt werden. Standardmäßig ist die Aufbewahrungsrichtlinie inaktiviert und die Protokolle werden unbegrenzt lange aufbewahrt. Wenn der Aufbewahrungszeitraum abgelaufen ist, werden die Protokolle automatisch gelöscht. 
{:shortdesc}

In einem Konto können verschiedene Aufbewahrungsrichtlinien definiert sein. Sie können eine globale Kontenrichtlinie und einzelne Bereichsrichtlinien haben. Die Aufbewahrungsrichtlinie, die Sie auf Kontoebene festlegen, legt die maximale Anzahl von Tagen fest, für die Protokolle aufbewahrt werden. Wenn Sie eine Bereichsaufbewahrungsrichtlinie für einen bestimmten Zeitraum festlegen, der länger als der Zeitraum auf Kontoebene ist, wird die Richtlinie angewendet, die Sie als letzte für diesen Bereich konfiguriert haben. 


## Protokollaufbewahrungsrichtlinie für einen Bereich inaktivieren
{: #disable_retention_policy_space1}

Führen Sie die folgenden Schritte aus, um eine Aufbewahrungsrichtlinie zu inaktivieren:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Legen Sie den Aufbewahrungszeitraum auf **-1** fest, um den Aufbewahrungszeitraum zu inaktivieren. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud cf logging option -r -1
    ```
    {: codeblock}
    
**Beispiel**
    
Um beispielsweise den Aufbewahrungszeitraum für einen Bereich mit der ID *d35da1e3-b345-475f-8502-cfgh436902a3* zu inaktivieren, führen Sie den folgenden Befehl aus:

```
ibmcloud cf logging option -r -1
```
{: codeblock}

Die Ausgabe sieht wie folgt aus:

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |        -1 |
+--------------------------------------+-----------+
```
{: screen} 



## Protokollaufbewahrungsrichtlinie für einen Bereich überprüfen
{: #check_retention_policy_space1}

Um die Aufbewahrungsdauer abzurufen, die für einen Bereich festgelegt ist, führen Sie die folgenden Schritte aus:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Rufen Sie den Aufbewahrungszeitraum ab. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud cf logging option
    ```
    {: codeblock}

    Die Ausgabe sieht wie folgt aus:

    ```
    +--------------------------------------+-----------+
    |               SPACEID                | RETENTION |
    +--------------------------------------+-----------+
    | d35da1e3-b345-475f-8502-cfgh436902a3 |        30 |
    +--------------------------------------+-----------+
    ```
    {: screen}
    

## Protokollaufbewahrungsrichtlinie für alle Bereiche in einem Konto überprüfen
{: #check_retention_policy_account}

Um die Aufbewahrungsdauer abzurufen, die für jeden Bereich in einem Konto festgelegt ist, führen Sie die folgenden Schritte aus:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Rufen Sie den Aufbewahrungszeitraum für jeden Bereich in dem Konto ab. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud cf logging option -a
    ```
    {: codeblock}

    Die Ausgabe sieht wie folgt aus:

    ```
    +--------------------------------------+-----------+
    |               SPACEID                | RETENTION |
    +--------------------------------------+-----------+
    | d35da1e3-b345-475f-8502-cfgh436902a3 |        30 |
    +--------------------------------------+-----------+
    | fdew45e3-b345-4365-8502-cfghrfthy5a3 |        30 |
    +--------------------------------------+-----------+
    ```
    {: screen}
    

## Protokollaufbewahrungsrichtlinie auf Kontoebene festlegen
{: #set_retention_policy_space1}

Um die Aufbewahrungsdauer für ein Konto anzuzeigen, führen Sie die folgenden Schritte aus:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Legen Sie den Aufbewahrungszeitraum fest. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud cf logging option -r *Anzahl_von_Tagen* - a
    ```
    {: codeblock}
    
    Dabei ist *Anzahl_von_Tagen* eine ganze Zahl, die die Aufbewahrungsdauer von Protokollen in Tagen angibt. 
    
    
**Beispiel**
    
Beispiel: Wenn alle Protokolltypen nur für 15 Tage in Ihrem Konto verbleiben sollen, führen Sie den folgenden Befehl aus:

```
ibmcloud cf logging option -r 15 -a
```
{: codeblock}

Die Ausgabe enthält einen Eintrag für jeden Bereich des Kontos, einschließlich Informationen zum Aufbewahrungszeitraum:

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |        15 |
+--------------------------------------+-----------+
| fdew45e3-b345-4365-8502-cfghrfthy5a3 |        30 |
+--------------------------------------+-----------+
```
{: screen}

## Protokollaufbewahrungsrichtlinie für einen Bereich festlegen
{: #set_retention_policy_account}

Um die Aufbewahrungsdauer für einen Bereich anzuzeigen, führen Sie die folgenden Schritte aus:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Legen Sie den Aufbewahrungszeitraum fest. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud cf logging option -r *Anzahl_von_Tagen*
    ```
    {: codeblock}
    
    Dabei ist *Anzahl_von_Tagen* eine ganze Zahl, die die Aufbewahrungsdauer von Protokollen in Tagen angibt.
    
    
**Beispiel**
    
Beispiel: Wenn Protokolle für ein ganzes Jahr in einem Bereich verbleiben sollen, führen Sie den folgenden Befehl aus:

```
ibmcloud cf logging option -r 365
```
{: codeblock}

Die Ausgabe sieht wie folgt aus:

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |       365 |
+--------------------------------------+-----------+
```
{: screen}


