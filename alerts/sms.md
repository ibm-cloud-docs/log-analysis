---

copyright:
  years:  2021, 2023
lastupdated: "2021-07-12"

keywords: IBM, Log Analysis, PagerDuty

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Sending an SMS notification
{: #sms}

You can send SMS alerts to notify on log data hosted in a {{site.data.keyword.la_short}} instance.
{: shortdesc}

To send an SMS alert, you can choose 1 of the following options:
- Integrate with the {{site.data.keyword.mon_full_notm}} service to send SMS alerts.

    Use this option when you need alerts on log data alongside system health metrics.

- Integrate with PagerDuty to send SMS alerts.

    Use this option when you require call times and escalation management processes.


## Send an SMS notification by using the {{site.data.keyword.en_full_notm}} service
{: #sms-mon}

When the {{site.data.keyword.la_short}} service sends a notification to the {{site.data.keyword.mon_full_notm}} service, an alert is triggered in the {{site.data.keyword.mon_full_notm}} instance. In the *Events* view section, you can then configure an event for that type of alert to send an SMS through the {{site.data.keyword.en_full_notm}} service.

Complete the following steps to get an SMS notification when an alert in the {{site.data.keyword.la_short}} service is triggered:

### Step 1. Configure an alert in {{site.data.keyword.la_full_notm}}
{: #sms-mon-step1}

In the {{site.data.keyword.la_short}} web UI, [configure a {{site.data.keyword.mon_short}} alert](/docs/log-analysis?topic=log-analysis-monitoring).

When an alert is triggered, a notification is sent to the {{site.data.keyword.mon_short}} instance that you have configured. Then, you manage alerts through the *Events* view section in the {{site.data.keyword.mon_short}} UI.

### Step 2. Configure the {{site.data.keyword.mon_short}} instance
{: #sms-mon-step2}

Complete the following steps:
1. [Define an {{site.data.keyword.en_full_notm}} notification channel in your {{site.data.keyword.mon_short}} instance](/docs/log-analysis?topic=log-analysis-monitoring#monitoring-config).
2. Define an alert from the event that triggers the {{site.data.keyword.la_full_notm}} alert.

      In the *Events* section of the {{site.data.keyword.mon_short}} UI, configure an event that send an SMS notification based on the alert that youd defined previously:

      1. Select an alert. Then select **Create Alert from Event**.

      2. Enter a name, a description, a group, and the severity level. The group **default** is set unless you specify a custom one.

      3. Define the condition that triggers the SMS notification.

          Specify events that match the alerts being sent to {{site.data.keyword.mon_short}} from {{site.data.keyword.la_short}}. For example, you can indicate **LogDNA** or the name of the alert.

          Set the **Scope** to `everywhere`.

          If you want {{site.data.keyword.mon_short}} to send alerts to {{site.data.keyword.en_full_notm}} to be sent on as SMS message as soon as possible, specify **Trigger** values in the {{site.data.keyword.mon_short}} alert definition to be as low as possible.

      4. Select 1 or more notification channels. Make sure you select the {{site.data.keyword.en_full_notm}} channel that you configured to notify thorugh the {{site.data.keyword.en_full_notm}} service.



### Step 3. Configure the {{site.data.keyword.en_full_notm}} service
{: #sms-mon-step3}

Complete the following steps:

1. [Provision an {{site.data.keyword.en_full_notm}} instance](/docs/monitoring?topic=monitoring-eventnotif_sms#eventnotif_sms_step1).
2. [Configure an authorization that grants {{site.data.keyword.mon_full_notm}} access to {{site.data.keyword.en_full_notm}}](/docs/monitoring?topic=monitoring-eventnotif_sms#eventnotif_sms_step2).
3. [Configure the {{site.data.keyword.en_full_notm}} instance](/docs/monitoring?topic=monitoring-eventnotif_sms#eventnotif_sms_step3).






## Send an SMS notification by using the PagerDuty On Call Service
{: #sms-pd}

When the {{site.data.keyword.la_short}} service sends a notification (event) to PagerDuty, an alert incident is created in PagerDuty and an SMS is sent if the escalation policy and on-call responder details include the rule to send to an SMS number.
- An incident is the issue that needs to be resolved. It can have 3 states: `triggered`, `acknowledged`, and `resolved`
- An incident triggers a PagerDuty service that generates 1 or more notifications to go out to on-call responders according to the service's escalation policy. SMS is a type of notification. You must configure a service so that it includes the escalation policy that indicates how to connect a service to individual users and schedules.

    A service includes information about the {{site.data.keyword.la_short}} service as an inbound integration that sends notifications to PagerDuty.

    A service profile provides information such as collaboration across teams, who owns the service, who’s on-call, how to contact the Team responsible for the service and more.

- A User Profile includes information about on-call responders such as the phone number, SMS number, and email address. The information is used to contact the user when an incident is assigned to the user. You must configure the user profiles and check that the SMS details are correct.

- An SMS provides basic information about the alert. The alert can include 1 or more incidents. When multiple incidents are triggered and assigned to a user, the SMS notification bundles all notifications for the user into 1 SMS. You can click on an incident link to see more details. You can acknowledge or resolve the incident with a text reply.

    The maximum number of characters in a text message is 160. Any text message that has more than 160 characters is truncated.
    {: note}

- PagerDuty publishes the SMS number list so a user can easily validate the sender of the SMS. For more information, see [Notification Phone Numbers](https://support.pagerduty.com/docs/notification-phone-numbers){: external}.

Complete the following steps to get an SMS notification when an alert in the {{site.data.keyword.la_short}} service is triggered:

1. [Create a PagerDuty service](https://support.pagerduty.com/docs/services-and-integrations#create-a-new-service){: external}.

2. [Configure the support user in PagerDuty who will receive SMS alert messages](https://support.pagerduty.com/docs/configuring-a-user-profile){: external}.

   Make sure a valid mobile number is provided for **SMS** in the user's **Contact Information** and that the **Notification Rules** for the user indicates that an SMS is to be sent to the mobile number. If these items are not configured correctly, the user will not receive SMS messages.
   {: important}

3. [Configure a PagerDuty Escalation Policy](https://support.pagerduty.com/docs/escalation-policies#section-create-an-escalation-policy){: external} and for **Notify** specify the support user.

4. In the {{site.data.keyword.la_short}} UI, [configure a PagerDuty alert](/docs/log-analysis?topic=log-analysis-pagerduty).
