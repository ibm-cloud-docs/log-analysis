---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, applications

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Logging with applications overview
{: #app_logging}

You can use the Ingestion REST API and libraries to send application logs to an {{site.data.keyword.la_full}} instance.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

In an application log, you can find information that you can use to troubleshoot and monitor your application.

In {{site.data.keyword.la_short}}, you can choose any of the following options to send application logs to an {{site.data.keyword.la_full_notm}} instance:


## REST API
{: #app_logging_api}

You can send log data to an {{site.data.keyword.la_full_notm}} instance by using the Ingestion REST API. For more information, see [Sending logs by using the REST API](/docs/log-analysis?topic=log-analysis-ingest).


## Code library
{: #app_logging_code}


You can add code to an application to manage application logs through an {{site.data.keyword.la_full}} instance.


The following table lists libraries that you can use to send application logs to an {{site.data.keyword.la_full_notm}} instance:

![Code libraries](/images/app_logging_img1.png "Code libraries")

| Library | Git Repo | More info |
|---------|----------|-----------|
| `Python` | [Python](https://github.com/logdna/python){: external} | [Sending logs by using Python](/docs/log-analysis?topic=log-analysis-ingest_python). |
| `Node`   | [Node](https://github.com/logdna/nodejs){: external} | You can send logs from your Node.js and JavaScript applications to an {{site.data.keyword.la_full_notm}} instance by using the Node.js library and adding a transport.  \n  \n Valid transports are Winston and Bunyan.
| `Ruby and Ruby on Rails` | [Ruby](https://github.com/logdna/ruby){: external} |  |
{: caption="Table 1. Code libraries" caption-side="top"}
