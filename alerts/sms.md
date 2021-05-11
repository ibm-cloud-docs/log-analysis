---

copyright:
  years:  2021
lastupdated: "2021-05-11"

keywords: IBM, Log Analysis, PagerDuty

subcollection: log-analysis

---

{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}
{:important: .important}
{:note: .note}
{:external: target="_blank" .external}

# Sending an SMS notification
{: #sms}

You can send SMS alerts to notify on log data hosted in a {{site.data.keyword.la_short}} instance.
{:shortdesc}

To send an SMS alert, you can choose 1 of the following options:
- Integrate with the {{site.data.keyword.mon_full_notm}} service to send SMS alerts.

    Use this option when you need alerts on log data alongside system health metrics.

- Integrate with PagerDuty to send SMS alerts.

    Use this option when you require call times and escalation management processes.


## Send an SMS notification by using the {{site.data.keyword.mon_full_notm}} service
{: #sms-mon}

When the {{site.data.keyword.la_short}} service sends a notification to the {{site.data.keyword.mon_full_notm}} service, an event is created in the the {{site.data.keyword.mon_short}} instance. You can then configure the {{site.data.keyword.mon_full_notm}} service to send an SMS. 

Complete the following steps to get an SMS notification when an alert in the {{site.data.keyword.la_short}} service is triggered:

1. In the {{site.data.keyword.la_short}} web UI, [configure a {{site.data.keyword.mon_short}} alert](/docs/log-analysis?topic=log-analysis-monitoring). 

    You manage alerts through the Events view section in the {{site.data.keyword.mon_short}} UI.

2. In the the {{site.data.keyword.mon_short}} UI, configure [sending SMS alerts using PagerDuty](/docs/monitoring?topic=monitoring-pd_sms).



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





