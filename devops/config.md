---

copyright:
  years: 2019, 2021
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, config, ui

subcollection: Log-Analysis-with-LogDNA

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
{:external: target="_blank" .external}


# Customizing the web UI
{: #config}

You can configure your web UI to work with UTC timestamps, change the log line format, change the background color and more.
{:shortdesc}


## Configure UTC timestamps 
{: #config_utc}

By default, the web UI is configured to use local timestamps in views and searches.

To display timestamps in UTC and do timeframe searches relative to UTC instead of local time, complete the following steps:

1. In the web UI, click the **Settings** icon ![Settings icon](images/admin.png "Admin icon") &gt; **User preferences**.
2. Select **Viewer options**.
3. Click **Show time as UTC** to enable UTC timestamps.



## Configure the background color
{: #config_color}

Complete the following steps:

1. In the web UI, click the **Settings** icon ![Settings icon](images/admin.png "Admin icon") &gt; **User preferences**.
2. Select **Viewer style**.
3. Choose the default contrast. 

    Choose *Light mode* to have a light background. 
    
    Choose *Dark mode** to have a black background.




## Configure the log line format
{: #config_line_format}

Complete the following steps to display a log line that includes the timestamp and message of an event:

1. In the web UI, click the **Settings** icon ![Settings icon](images/admin.png "Admin icon") &gt; **User preferences**.
2. Select **Log format**.

    By default, the log format is configured in the following way:
    
    ```
    %time('MMM D HH:mm:ss') %source %app %level %line
    ```
    {: screen}

3. Remove source, app, and level by dragging them out.

    The log line changes to the following format:

    ```
    %time('MMM D HH:mm:ss') %line
    ```
    {: screen}


