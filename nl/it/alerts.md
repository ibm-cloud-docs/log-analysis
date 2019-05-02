---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, alerts

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

 
# Gestione degli avvisi
{: #alerts}

Puoi collegare uno o più avvisi a una vista. Puoi definire più canali di notifica per un avviso. Puoi disattivare la notifica degli avvisi. Puoi scollegare gli avvisi da una vista.
{:shortdesc}

Puoi configurare le seguenti condizioni per un avviso:

* *Frequenza temporale*: specifica la frequenza con cui attivare un avviso. I valori validi sono: 30 secondi, 1 minuto, 5 minuti, 15 minuti, 30 minuti, 1 ora, 6 ore, 12 ore, 24 ore
* *Contatore delle righe di log*: specifica il numero di righe di log corrispondenti ai criteri di filtro e ricerca della vista. Quando il numero di righe di log viene raggiunto, viene attivato un avviso.

Puoi decidere se vengono controllate entrambe le condizioni oppure solo una. Se sono impostate entrambe le condizioni, viene attivato un avviso quando viene raggiunta una qualsiasi delle soglie. 

Ad esempio, puoi configurare un avviso che viene attivato dopo 30 secondi o quando vengono raccolte 100 righe di log che corrispondono ai criteri di ricerca e filtro della vista.

Puoi configurare più canali di notifica. I canali validi sono: `email`, `Slack`, `PagerDuty`, `Webhook`, `OpsGenie`, `Datadog`, `AppOptics`, `VictorOps`

Puoi anche definire una **preimpostazione**. Una preimpostazione è un template di avviso che puoi collegare a qualsiasi numero di viste. 

Per riutilizzare una configurazione di avviso con altre viste, configura una **preimpostazione di avviso**.
{: tip}

Con la vista viene visualizzata un'icona a forma di campana per indicare che a questa vista è collegato un avviso.



## Configura una preimpostazione (template di avviso)
{: #config_preset}

Per configurare una preimpostazione, completa la seguente procedura:

1. Seleziona l'icona **Configuration** ![Icona Configuration](images/admin.png "Icona Admin").
2. Seleziona **Alerts**.
3. Seleziona **Add a preset alert**.
4. Scegli un canale di notifica. 
5. Definisci le condizioni di soglia.

    1. Seleziona una frequenza temporale. Ad esempio, 12 ore.

    2. Immetti il numero di righe di log dopo le quali desideri che venga attivato l'avviso.

    3. Seleziona se desideri che entrambe le condizioni vengano controllate o solo una.

6. Aggiungi i dettagli per il canale di notifica che hai scelto.

    Ad esempio, per il canale di notifica email, aggiungi uno o più destinatari e, facoltativamente, un fuso orario.

7. Fai clic su **Save alert**.



## Configura un avviso utilizzando una preimpostazione
{: #config_alert_preset}

Per collegare una preimpostazione a una vista, completa la seguente procedura:

1. Fai clic sull'icona **Views** ![icona Configuration](images/views.png).
2. Crea una vista. 

    Applica un intervallo di tempo e dei criteri di filtro e ricerca per filtrare le righe di log che vengono visualizzate mediante la vista. 

    Per ulteriori informazioni, vedi il documento relativo alla [creazione di viste](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7).

3. Fai clic sul nome della vista. Seleziona quindi **Attach an alert**.

4. Scegli una preimpostazione per riutilizzare una definizione di avviso. 

5. Fai clic su **Save alert**. 




## Configura un avviso specifico per la vista
{: #config_alert_view}

Per collegare un avviso a una vista, completa la seguente procedura:

1. Fai clic sull'icona **Views** ![icona Configuration](images/views.png).
2. Crea una vista. 

    Applica un intervallo di tempo e dei criteri di filtro e ricerca per filtrare le righe di log che vengono visualizzate mediante la vista. 

    Per ulteriori informazioni, vedi il documento relativo alla [creazione di viste](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7).

3. Fai clic sul nome della vista. Seleziona quindi **Attach an alert**.

4. Scegli **view-specific alert**.

5. Scegli un canale di notifica. 

6. Definisci le condizioni di soglia.

    1. Seleziona una frequenza temporale. Ad esempio, 12 ore.

    2. Immetti il numero di righe di log dopo le quali desideri che venga attivato l'avviso.

    3. Seleziona se desideri che entrambe le condizioni vengano controllate o solo una.

7. Aggiungi i dettagli per il canale di notifica che hai scelto.

    Ad esempio, per il canale di notifica email, aggiungi uno o più destinatari e, facoltativamente, un fuso orario.

8. Fai clic su **Save alert**.



## Elimina una preimpostazione (template di avviso)
{: #delete_preset}

Per eliminare una preimpostazione, completa la seguente procedura:

1. Seleziona l'icona **Configuration** ![Icona Configuration](images/admin.png "Icona Admin").
2. Seleziona **Alerts**.
3. Passa il puntatore del mouse sul pulsante *edit* della preimpostazione che desideri eliminare. Viene visualizzata l'opzione *delete*.
4. Seleziona **Delete**.
5. Conferma che desideri eliminare la preimpostazione. Fai clic su **Delete**.

## Scollega un avviso specifico per la vista da una vista
{: #delete_alert}

Per scollegare una preimpostazione, completa la seguente procedura:

1. Seleziona l'icona **Configuration** ![Icona Configuration](images/admin.png "Icona Admin").
2. Seleziona **Alerts**.
3. Passa il puntatore del mouse sul pulsante *edit* dell'avviso che desideri eliminare. Viene visualizzata l'opzione *delete*.
4. Seleziona **Detach**.
5. Conferma che desideri eliminare l'avviso. Fai clic su **Detach**.



## Canali di notifica
{: #channels}

La seguente tabella elenca i canali di notifica che puoi configurare quando viene attivato un avviso:

| Canale           | Dettagli della configurazione | 
|-------------------|-----------------------|
| `email`             | Puoi configurare uno o più indirizzi email.  | 
| `Slack`             | Puoi configurare un canale slack. |
| `Webhook`           | Puoi configurare un URL webhook. |
| `PagerDuty`         | Puoi configurare i dettagli di connessione per il tuo sistema PagerDuty e selezionare un servizio.|
| `OpsGenie`          | Puoi configurare la chiave API per la connessione al tuo sistema OpsGenie. |
| `Datadog`           | Puoi configurare la chiave API per la connessione al tuo sistema `Datadog`. |
| `AppOptics/Librato` | Puoi configurare la chiave API per la connessione al tuo sistema AppOptics/Librato. |
| `VictorOps`         | Puoi configurare l'URL per la notifica quando viene attivato un avviso, la chiave di instradamento e un tipo di avviso. I tipi di avviso validi sono: `info`, `warning`, `critical` |
{: caption="Canali di notifica" caption-side="top"} 


