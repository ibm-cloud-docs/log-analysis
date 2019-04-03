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

# IBM Cloud Log Analysis CLI（CF 插件）
{: #logging_cli}

{{site.data.keyword.loganalysislong}} CLI 是一个插件，用于管理在 {{site.data.keyword.Bluemix}} 组织内空间中运行的云资源的日志。
{: shortdesc}

**先决条件**
* 运行 logging 命令之前，请先使用 `ibmcloud login` 命令登录到 {{site.data.keyword.Bluemix_notm}}，以生成 {{site.data.keyword.Bluemix_short}} 访问令牌并对会话进行认证。有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。

要了解如何使用 {{site.data.keyword.loganalysisshort}} CLI，请参阅[管理日志](/docs/services/CloudLogAnalysis/log_analysis_ov.html#log_analysis_ov)。

<table>
  <caption>用于管理日志的命令</caption>
  <tr>
    <th>命令</th>
    <th>何时使用</th>
  </tr>
  <tr>
    <td>[ibmcloud cf logging](#base)</td>
    <td>使用此命令可获取有关 CLI 的信息，例如版本或命令列表。</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging auth](#auth)</td>
    <td>使用此命令可获取日志记录令牌，此令牌可用于将日志发送到 {{site.data.keyword.loganalysisshort}} 服务。</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging delete](#delete)</td>
    <td>使用此命令可删除存储在“日志收集”中的日志。</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging download (Beta)](#download)</td>
    <td>使用此命令可将“日志收集”中的日志下载到本地文件，或者通过管道将日志传递到其他程序，例如 Elastic 堆栈。</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging help](#help)</td>
    <td>使用此命令可获取有关如何使用 CLI 的帮助以及所有命令的列表。</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging option](#option)</td>
    <td>使用此命令可查看或设置空间或帐户中可用的日志的保留期。</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging session create (Beta)](#session_create1)</td>
    <td>使用此命令可创建新会话。</td>
  <tr>
  <tr>
    <td>[ibmcloud cf logging session delete (Beta)](#session_delete1)</td>
    <td>使用此命令可删除会话。</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging session list (Beta)](#session_list1)</td>
    <td>使用此命令可列出活动会话及其标识。</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging session show (Beta)](#session_show1)</td>
    <td>使用此命令可显示单个会话的状态。</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging status](#status1)</td>
    <td>使用此命令可获取有关在空间或帐户中收集的日志的信息。</td>
  </tr>
  </table>


## ibmcloud cf logging
{: #base1}

提供有关 CLI 版本以及如何使用 CLI 的信息。

```
ibmcloud cf logging [parameters]
```
{: codeblock}

**参数**

<dl>
<dt>--help, -h</dt>
<dd>设置此参数可显示命令列表或获取某个命令的帮助。
</dd>

<dt>--version, -v</dt>
<dd>设置此参数可显示 CLI 的版本。</dd>
</dl>

**示例**

要获取命令的列表，请运行以下命令：

```
ibmcloud cf logging --help
```
{: codeblock}

要获取 CLI 的版本，请运行以下命令：

```
ibmcloud cf logging --version
```
{: codeblock}


## ibmcloud cf logging auth
{: #auth}

获取日志记录令牌，此令牌可用于将日志发送到 {{site.data.keyword.loganalysisshort}} 服务。 

**注**：此令牌不会到期。

```
ibmcloud cf logging auth
```
{: codeblock}

**返回**

<dl>
  <dt>日志记录令牌</dt>
  <dd>例如，`jec8BmipiEZc`。</dd>
  
  <dt>组织标识</dt>
  <dd>您所登录到的 {{site.data.keyword.Bluemix_notm}} 组织的 GUID。</dd>
  
  <dt>空间标识</dt>
  <dd>您所登录到的组织内空间的 GUID。</dd>
</dl>

## ibmcloud cf logging delete
{: #delete2}

删除存储在“日志收集”中的日志。

```
ibmcloud cf logging delete [parameters]
```
{: codeblock}

**参数**

<dl>
  <dt>--start value, -s value</dt>
  <dd>（可选）设置开始日期，格式为全球标准时间 (UTC)：*YYYY-MM-DD*，例如 `2006-01-02`。<br>缺省值设置为 2 周前。</dd>
  
  <dt>--end value, -e value</dt>
  <dd>（可选）设置结束日期，格式为全球标准时间 (UTC)：*YYYY-MM-DD*。<br>日期的 UTC 格式为 **YYYY-MM-DD**，例如 `2006-01-02`。<br>缺省值设置为当前日期。</dd>
  
  <dt>--type value, -t value</dt>
  <dd>（可选）设置日志类型。<br>例如，*syslog* 是一种日志类型。<br>缺省值设置为 **\***。<br>可以通过用逗号分隔各个类型来指定多种日志类型，例如 **log_type_1,log_type_2,log_type_3*。</dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>（可选）将提供的日志信息的作用域设置为帐户级别。<br>如果未指定此参数，那么缺省值会设置为仅提供有关当前空间的日志信息。</dd>
</dl>

**示例**

要删除 2017 年 5 月 25 日类型为 *linux_syslog* 的日志，请运行以下命令：
```
ibmcloud cf logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
```
{: codeblock}



## ibmcloud cf logging download (Beta)
{: #download4}

将“日志收集”中的日志下载到本地文件，或者通过管道将日志传递到其他程序，例如 Elastic 堆栈。 

**注**：要下载文件，需要首先创建会话。会话会根据日期范围、日志类型和帐户类型来定义要下载的日志。您将在会话上下文中下载日志。有关更多信息，请参阅 [ibmcloud cf logging session create (Beta)](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_create1)。

```
ibmcloud cf logging download [parameters] [arguments]
```
{: codeblock}

**参数**

<dl>
<dt>--output value, -o value</dt>
<dd>（可选）设置日志下载到其中的本地输出文件的路径和文件名。<br>缺省值为连字符 (-)。<br>将此参数设置为缺省值会将日志输出到标准输出。</dd>
</dl>

**自变量**

<dl>
<dt>session_ID</dt>
<dd>设置为运行 `ibmcloud cf logging session create` 命令时获得的会话标识值。此值指示下载日志时要使用的会话。<br>**注**：`ibmcloud cf logging session create` 命令提供用于控制下载哪些日志的参数。</dd>
</dl>

**注**：下载完成后，再次运行相同的命令将拒绝执行任何操作。要重新下载相同的数据，必须使用其他文件或其他会话。

**示例**

在 Linux 系统中，要将日志下载到名为 mylogs.gz 的文件中，请运行以下命令：

```
ibmcloud cf logging download -o mylogs.gz guBeZTIuYtreOPi-WMnbUg==
```
{: screen}

要将日志下载到自己的 Elastic 堆栈，请运行以下命令：

```
ibmcloud cf logging download guBeZTIuYtreOPi-WMnbUg== | gunzip | logstash -f logstash.conf
```
{: screen}

以下文件是 logstash.conf 文件的示例：

```
input {
  stdin {
    codec => json_lines {}
  }
}
output {
  elasticsearch {
    hosts => [ "127.0.0.1:9200" ]
  }
}
```
{: screen}


## ibmcloud cf logging help
{: #help1}

提供有关如何使用命令的信息。

```
ibmcloud cf logging help [command]
```
{: codeblock}

**参数**

<dl>
<dt>命令</dt>
<dd>设置要获取其帮助的命令名。
</dd>
</dl>


**示例**

要获取有关如何运行命令来查看日志状态的帮助，请运行以下命令：

```
ibmcloud cf logging help status
```
{: codeblock}


## ibmcloud cf logging option
{: #option}

显示或更改空间或帐户中可用的日志的保留期。 

* 保留期以天数为单位进行设置。
* 缺省值为 **-1**。 

**注**：缺省情况下，将存储所有日志。日志必须使用 **delete** 命令手动删除。设置保留时间策略可自动删除日志。

```
ibmcloud cf logging option [parameters]
```
{: codeblock}

**参数**

<dl>
<dt>--retention value, -r value</dt>
<dd>（可选）设置保留天数。<br> 缺省值为 *-1* 天。</dd>

<dt>--at-account-level, -a </dt>
  <dd>（可选）将作用域设置为帐户级别。<br>如果未指定此参数，那么对于当前空间（即，使用 `ibmcloud cf login` 命令登录到的空间），缺省值会设置为 *-1*。</dd>
</dl>

**示例**

要查看所登录到的空间的缺省当前保留期，请运行以下命令：

```
ibmcloud cf logging option
```
{: codeblock}

输出为：

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-ibmcloud cfgh436902a3 |        -1 |
+--------------------------------------+-----------+
```
{: screen}


要将所登录到的空间的保留期更改为 25 天，请运行以下命令：

```
ibmcloud cf logging option -r 25
```
{: codeblock}

输出为：

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-ibmcloud cfgh436902a3 |        25 |
+--------------------------------------+-----------+
```
{: screen}


## ibmcloud cf logging session create (Beta)
{: #session_create1}

创建新的会话。

**注**：一个空间中最多可以有 30 个并发会话。会话是为用户创建的。因此，空间中的不同用户之间不能共享会话。

```
ibmcloud cf logging session create [parameters]
```
{: codeblock}

**参数**

<dl>
  <dt>--start value, -s value</dt>
  <dd>（可选）设置开始日期，格式为全球标准时间 (UTC)：*YYYY-MM-DD*，例如 `2006-01-02`。<br>缺省值设置为 2 周前。</dd>
  
  <dt>--end value, -e value</dt>
  <dd>（可选）设置结束日期，格式为全球标准时间 (UTC)：*YYYY-MM-DD*，例如 `2006-01-02`。<br>缺省值设置为当前日期。</dd>
  
  <dt>--type value, -t value</dt>
  <dd>（可选）设置日志类型。<br>例如，*syslog* 是一种日志类型。<br>缺省值设置为星号 (*)。<br>可以指定多种日志类型并使用逗号分隔各个类型，例如 *log_type_1,log_type_2,log_type_3*。</dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>（可选）将作用域设置为帐户级别。<br>如果未指定此参数，那么仅会对当前空间（即，使用 `ibmcloud cf login` 命令登录到的空间）设置缺省值。</dd>
</dl>

**返回值**

<dl>
<dt>Access-Time</dt>
<dd>指示最后一次使用会话时的时间戳记。</dd>

<dt>Create-Time</dt>
<dd>对应于创建会话时的日期和时间的时间戳记。</dd>

<dt>Date-Range</dt>
<dd>指示用于过滤日志的日期。在此日期范围中识别到的日志可通过会话进行管理。</dd>

<dt>ID</dt>
<dd>会话标识。</dd>

<dt>空间</dt>
<dd>会话在其中处于活动状态的空间的标识。</dd>

<dt>Type-Account</dt>
<dd>通过会话下载的日志类型。</dd>

<dt>用户名</dt>
<dd>创建会话的用户的 {{site.data.keyword.IBM_notm}} 标识。</dd>
</dl>


**示例**

要创建会话以包含 2017 年 5 月 20 日到 2017 年 5 月 26 日之间日志类型为 *log* 的日志，请运行以下命令：

```
ibmcloud cf logging session create -s 2017-05-20 -e 2017-05-26 -t log
```
{: screen}


## ibmcloud cf logging session delete (Beta)
{: #session_delete1}

删除会话标识指定的会话。

```
ibmcloud cf logging session delete [arguments]
```
{: codeblock}

**自变量**

<dl>
<dt>session ID</dt>
<dd>要删除的会话的标识。<br>可以使用 `ibmcloud cf logging session list` 命令来获取所有活动会话标识。</dd>
</dl>

**示例**

要删除会话标识为 *cI6hvAa0KR_tyhjxZZz9Uw==* 的会话，请运行以下命令：

```
ibmcloud cf logging session delete cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}



## ibmcloud cf logging session list (Beta)
{: #session_list1}

列出活动会话及其标识。

```
ibmcloud cf logging session list 
```
{: codeblock}

**返回值**

<dl>
<dt>ID</dt>
<dd>会话标识。</dd>

<dt>SPACE</dt>
<dd>会话在其中处于活动状态的空间的标识。</dd>

<dt>USERNAME</dt>
<dd>创建会话的用户的 {{site.data.keyword.IBM_notm}} 标识。</dd>

<dt>CREATE-TIME</dt>
<dd>对应于创建会话时的日期和时间的时间戳记。</dd>

<dt>ACCESS-TIME</dt>
<dd>指示最后一次使用会话的时间的时间戳记。</dd>
</dl>
 

## ibmcloud cf logging session show (Beta)
{: #session_show1}

显示单个会话的状态。

```
ibmcloud cf logging session show [arguments]
```
{: codeblock}

**自变量**

<dl>
<dt>session_ID</dt>
<dd>要获取其信息的活动会话的标识。</dd>
</dl>

**返回值**

<dl>
<dt>Access-Time</dt>
<dd></dd>

<dt>Create-Time</dt>
<dd>对应于创建会话时的日期和时间的时间戳记。</dd>

<dt>Date-Range</dt>
<dd>指示用于过滤日志的日期。在此日期范围中识别到的日志可通过会话进行管理。</dd>

<dt>ID</dt>
<dd>会话标识。</dd>

<dt>空间</dt>
<dd>会话在其中处于活动状态的空间的标识。</dd>

<dt>Type-Account</dt>
<dd>通过会话下载的日志类型。</dd>

<dt>用户名</dt>
<dd>创建会话的用户的 {{site.data.keyword.IBM_notm}} 标识。</dd>
</dl>

**示例**

要显示会话标识为 *cI6hvAa0KR_tyhjxZZz9Uw==* 的会话的详细信息，请运行以下命令：

```
ibmcloud cf logging session show cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}


## ibmcloud cf logging status
{: #status1}

返回有关在空间或帐户中收集的日志的信息。

```
ibmcloud cf logging status [parameters]
```
{: codeblock}

**参数**

<dl>
  <dt>--start value, -s value</dt>
  <dd>（可选）设置开始日期，格式为全球标准时间 (UTC)：*YYYY-MM-DD*，例如 `2006-01-02`。<br>缺省值设置为 2 周前。</dd>
  
  <dt>--end value, -e value</dt>
  <dd>（可选）设置结束日期，格式为全球标准时间 (UTC)：*YYYY-MM-DD*，例如 `2006-01-02`。<br>缺省值设置为当前日期。</dd>
  
  <dt>--type value, -t value</dt>
  <dd>（可选）设置日志类型。<br>例如，*syslog* 是一种日志类型。<br>缺省值设置为星号 (*)。<br>可以指定多种日志类型并使用逗号分隔各个类型，例如 *log_type_1,log_type_2,log_type_3*。</dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>（可选）将作用域设置为帐户级别。<br> **注**：设置此值可获取帐户信息。<br>如果未指定此参数，那么仅会对当前空间（即，使用 `ibmcloud cf login` 命令登录到的空间）设置缺省值。</dd>
  
  <dt>--list-type-detail, -l</dt>
  <dd>（可选）设置此参数可列出每天各日志类型的小计。</dd>
</dl>

**注**：如果未指定开始日期和结束日期，`ibmcloud cf logging status` 命令将仅报告存储在“日志收集”中的最近 2 周的日志。


