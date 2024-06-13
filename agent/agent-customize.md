





# Configuring the agent

we may need  different topics 

https://github.com/logdna/logdna-agent-v2

- Configuring regex for redaction and exclusion or inclusion
- Configuring Lookback

You can define rules, using regex (regular expressions), to control what log data is collected by the agent and forwarded to LogDNA.

For example, you can identify certain types of logs that are noisy and not needed at all, and then write a regex pattern to match those lines and preclude them from collection. Conversely, you can use regex expressions to match the log lines that you do want to include, and collect only those log lines.

Additionally, you can use the environment variable LOGDNA_REDACT_REGEX to remove certain parts of a log line. Any redacted data is replaced with [REDACTED]. Redacting information is recommended when logs might contain PII (Personally Identifiable Information).

In general, using Agent-level environment variables to define what log data does not ever leave the data center or environment allows a higher level of control over sensitive data, and can also reduce any potential data egress fees.


    include only specific log lines (with LOGDNA_LINE_INCLUSION_REGEX) -> line_inclusion_regex
    exclude specific log lines (with LOGDNA_LINE_EXCLUSION_REGEX) -> line_exclusion_regex
    redact parts of a log line (with LOGDNA_REDACT_REGEX) -> line_redact_regex

Since agent 3.6, there are 3 new environment variables that can be configured to allow users to exclude or mask data before sending it to the agent. "log.line_inclusion_regex" can be used to include specific log lines. "log.line_exclusion_regex" can be configured to exclude  specific log lines. "log.line_redact_regex" can be configured to mask lines, or parts of a log line.


- Exclusion rules are applied after inclusion rules, and thus override inclusion rules. That is, for a line to be ingested, it should match all inclusion rules (if any) and not match any exclusion rule.
- Note that we use commas as separators for environment variable values, making it not possible to use the comma character (,) as a valid value. We are addressing this limitation in upcoming versions. If you need to use the comma character in a regular expression, use the unicode character reference: \u002C, for example: hello\u002C world matches hello, world.
- All regular expressions are case-sensitive by default. If you don't want to differentiate between upper and lower-case letters, use non-capturing groups with a flag: (?flags:exp), for example: (?i:my_case_insensitive_regex)


```yaml
log:
  dirs:  // add 1 line per directory (show Windows and Linux - this sample is linux)
    - "/var/log/marisa"
    - "/var/log/marisa/demo"
  include:
    glob: // "glob patterns specify sets of filenames with wildcard characters" (need to rephrase 0- I copied the definition) 
      - "*/abc*.log" // files that start abc and have extesion log
      - "*.type1" // all files with extension type1 
      - "*/demo1/a.txt" If a path is indicated, the glob expression o ly applies to that directory - only a.txt files
      - "*/abc???.txt" files named abc and 3 numbers (abc123.txt)
      - "*/abc???.*.???.json"  ? represents a digit
      - "*/demo/*.json" all json files
      - "*/demo/abc????.txt"
    regex:
      - ".*[^.]*$"  extensionless files
      - ".*/demo/[a-zA-Z0-9_\\-]+\\.type2"   only files that incl chars, numbers - _  of type2 and in the directory
      - ".*/[a-zA-Z0-9_\\-]+\\.type3"  only files that incl chars, numbers - _
      - ".*/^[a-zA-Z0-9_\\-]+\\.log" // any file that does not have extension log and  chars, numbers, _ - as part of the name (^ indicates to not valid)
  exclude:
    glob: 
      - ".*[^.]*$"  exclude extensionless files
      - "*/var/log/marisa/test/**"
      - "*.sample"
      - "*/marisa/c.txt"
    regex: [] 
  use_k8s_enrichment: ~
  log_k8s_events: ~
  lookback: start
  line_exclusion_regex: 
    - ".*(?i)debug.*" a log line that has a type debug/DEBUG is ignored and not sent (`(?i)` indicates upper or lower case matches or any combination)
    - ".*(?i)info.*" same for info
  line_redact_regex: 
    - ".*pattern.*"
    - ".*(?i)campo1.*" //redacts the line

           echo "crit 1234 campo1 sssssdf" >> abc
           Nov 23 13:12:56 crit red-hat-vsi          abc crit 1234 [REDACTED]  

    - ".*(?i)campo1" .  //masks anything in front of campo1 including campo1  
          
           echo "crit 1234 campo1 sdf" >> a.log
           `Nov 23 12:59:30 red-hat-vsi a.log         [REDACTED] sdf` 

    - "(?i)campo1"

            echo "crit 1234 campo1 sssssdf" >> abc
            Nov 23 13:15:46 crit red-hat-vsi abc crit 1234 [REDACTED] sssssdf 

# redact main level fields in a json
# use \\u002C for ,
    - "(?:message:([a-zA-Z0-9_\\-\\s]*))"
    - "(?:campo2:([a-zA-Z0-9_\\-.\\s]*)?)"
```


  line_exclusion_regex: 
    - ".*(?i)debug.*" 
    - ".*(?i)info.*"

https://github.com/logdna/logdna-agent-v2/blob/master/docs/REGEX.md

- "\"Name\"[ :]+((?=\[)\[[^]]*\]|(?=\{)\{[^\}]*\}|\"[^"]*\")"

"name"\s?+:\s?+"?([\w+#\s]+)"?

- "\"name\"\s?+:\s?+\"?([\w+#\s]+)\"?"
- "(?:"name":")(.*?)(?:")"

"\\"campo2\\"\\s*:\\s*\\"(.*?)\\""

"{"data":[{"categories":["informationtech","business"],"url":"webshrinker.com"}]}"

(?:[{,]\s*"data"\s*:\s*\[|\G(?!\A)\s*,)\s*"([^"\\]*(?:\\.[^"\\]*)*)"


(?:[{,]\s*"message"\s*:\s*\[|\G(?!\A)\s*,)\s*"([^"\\]*(?:\\.[^"\\]*)*)"

([^"\\]
(?:s*\\"message\\"\s*:\s*(\G(?!\A)\s*)\\,$)

{"data":"1233","image":"dsfsdfsdfds","text":"hello world","name": "java"}


{"@timestamp":"2022-10-19T08:15:10.135Z","@metadata":{"beat":"filebeat","type":"doc","version":"6.4.2"},"REQUESTID":"e70c44e1-98cc-4f68-bc67-097db1d4a521","SUBSUBCANAL":"002","thread":"[ACTIVE] ExecuteThread: '5' for queue: 'weblogic.kernel.Default (self-tuning)'","message":"getValue(applicationId): no ha sido posible generar el contexto para la aplicacion 'SCARecursoOperativa', clave 'CA.OFI.Home' y gestor 'controlaccesoManager'","level":"DEBUG","source":"/mnt/log/arch-distributed-cache-client.TST.EXC01_0301.json","prospector":{"type":"log"},"threadId":98,"input":{"type":"log"},"loggerName":"es.lacaixa.absis.arch.configman.distributedcache.client.impl.hazelcast.AbstractArchManager","instant":{"nanoOfSecond":675000000,"epochSecond":1666010595},"timestamp":"2022-10-17 14:43:15.675","loggerFqcn":"org.apache.logging.log4j.jcl.Log4jLog","log_type":"ARQABS_CACHECLIENT_JSON","threadPriority":5,"INSTANCIA":"EXC01_0301","endOfBatch":false,"entorno":"dev","SUBCANAL":"001","USUARIO":"U0187224","THREAD":"98","CANAL":"001","clase":"cacheclient","host":{"name":"6dca6d2cc869"},"beat":{"name":"6dca6d2cc869","hostname":"6dca6d2cc869","version":"6.4.2"},"offset":0}

{"@timestamp":"2022-12-01T12:23:25.210+00:00","@version":"1","message":"{\n \"SCA_MENSAJE\" : \"[SCA-PLUGIN] Autorizado - permiso de scope\",\n \"SCA_ROL\" : \"SCA_SCOPE_ATM\",\n \"USER\" : \"00086\",\n \"SCA_AUTORIZADO\" : \"AUTORIZADO\",\n \"SCA_TIPO_RECURSO\" : \"SRV.MS\",\n \"SCA_MODO\" : \"SIMULACION\",\n \"SCA_RECURSO\" : \"SRV.MS.atmOperationsManagement-micro\",\n \"SCA_RECURSO_ENDPOINT\" : \"/channelSpecific/atm/home\",\n \"CRIT\" : \"Authorized by user role and resource\",\n \"CHANNEL\" : \"002\",\n \"SUB_CHANNEL\" : \"001\",\n \"SUB_SUB_CHANNEL\" : \"001\",\n \"OFFICE_ID\" : \"02400\",\n \"OPERATION_ID\" : \"home\",\n \"ROLE_LIST\" : \"[SCA_SCOPE_ATM, SCA.CANAL_EXTERNO]\"\n}","logger_name":"com.caixabank.absis.arch.sca.service.ScaPluginService","thread_name":"http-nio-8080-exec-3","level":"CRIT","level_value":20000,"channel":"002","ABSIS_APP_VERSION":"1","ABSIS_ENVIRONMENT":"tst","serviceEndpoint":"/channelSpecific/atm/home","httpMethod":"POST","info.rollout-type":"devops","ABSIS_APP_DOMAIN":"architecture","requestId":"2c0c9a07-05f2-4d4e-acd7-55f9f1f62aba","subChannel":"001","applicationName":"service-manager-micro-server","absisLayer":"BUSINESS_PLUGIN","subSubChannel":"001","canaryRoute":"stable","serviceOperation":"home","ipAddress":"127.0.0.1","messageId":"9def372b-5f6a-4634-8b7b-aa7e0bbbceaa","executionMode":"NORMAL","principalName":"00086","serviceName":"SRV.MS.atmOperationsManagement-micro","absis.service-manager.integration":"REMOTE","actor":"ATM","ABSIS_APP_SUBDOMAIN":"NO_SUBDOMAIN","ABSIS_APP_COMPANY":"CORP","stage":"BEFORE","plugin":"sca","mainframeTest":"IMSEPPI1","ABSIS_APP_TYPE":"ARQ.MIA","n3Key":"02XCA00086 0092022328132321630C120223281323210860000086 00103","coreVersion":"1.21.0","principalType":"ATM","serviceMethod":"sca","clase":"generic"}

{"@timestamp":"2022-12-01T12:30:25.210+00:00","@version":"1","message":"hello"}
{"a":"1","@version":"1","message":"hello"}


{"thread":"[ACTIVE] ExecuteThread: '0' for queue: 'weblogic.kernel.Default (self-tuning)'","level":"CRIT","loggerName":"es.lacaixa.absis.arch20.service.as.IntegrationServiceAdvice","message":"Enviamos a la cola de fraude antes de llamar al SI. Escenario2: false, Relanzamiento: false","endOfBatch":false,"loggerFqcn":"org.apache.logging.log4j.jcl.Log4jLog","instant":{"epochSecond":1669279191,"nanoOfSecond":855000000},"threadId":16,"threadPriority":5,"timestamp":"2022-11-24 09:39:51.855","INSTANCIA":"SRV11_0101","REQUESTID":"ad9e619c-cbd0-43c5-bce3-6576be0d93a3","USUARIO":"U0180365","ACTOR":"","LTERM":"T01H5YDI","OFICINA":"06161","CANAL":"001","SUBCANAL":"001","SUBSUBCANAL":"004","APPID":"ABSIS_CO_EXT"}
{"thread":"[ACTIVE] ExecuteThread: '0' for queue: 'weblogic.kernel.Default (self-tuning)'","level":"DEBUG","loggerName":"es.lacaixa.absis.arch20.service.as.IntegrationServiceAdvice","message":"methodName actual: consPersonas","endOfBatch":false,"loggerFqcn":"org.apache.logging.log4j.jcl.Log4jLog","instant":{"epochSecond":1669279191,"nanoOfSecond":855000000},"threadId":16,"threadPriority":5,"timestamp":"2022-11-24 09:39:51.855","INSTANCIA":"SRV11_0101","REQUESTID":"ad9e619c-cbd0-43c5-bce3-6576be0d93a3","USUARIO":"U0180365","ACTOR":"","LTERM":"T01H5YDI","OFICINA":"06161","CANAL":"001","SUBCANAL":"001","SUBSUBCANAL":"004","APPID":"ABSIS_CO_EXT"}

architecture.TST.SRV11_0101.json

".*/,\"message\"[:]+[a-zA-Z0-9_\\-\\"],"

- "\"Name\"[ :]+((?=\[)\[[^]]*\]|(?=\{)\{[^\}]*\}|\"[^"]*\")"

(?<=^|,)1(?=,|$)

((?=\S)[^,]+)

(?<=,)[^,\n]+(?=,)



(?=\S)(?:"[^"\\]*(?:\\[\s\S][^"\\]*)*"|[^",])

    (?=\S) - next char must be a non-whitespace char
    (?:"[^"]*"|[^",])+ - one or more occurrences (+) of the pattern sequence defined in a non-capturing group ((?:...)):
        "[^"]*" - either ", then 0 or more chars other than " and then a "
        | - or
        [^",] - any char other than " and ,.






[2022-11-25T09:27:20Z ERROR logdna_agent::_main] line regex is invalid: regex parse error:
        (?<=, )message .+?(?=,)
        ^^^^
    error: look-around, including look-ahead and look-behind, is not supported
Error: regex parse error:
    (?<=, )message .+?(?=,)
    ^^^^
error: look-around, including look-ahead and look-behind, is not supported



[2022-11-25T12:23:37Z ERROR logdna_agent::_main] line regex is invalid: regex parse error:
        (?:(?!target:)(?[a-zA-Z0-9_\-\s/\{\}:]*))
           ^^^
    error: look-around, including look-ahead and look-behind, is not supported
Error: regex parse error:
    (?:(?!target:)(?[a-zA-Z0-9_\-\s/\{\}:]*))
       ^^^
error: look-around, including look-ahead and look-behind, is not supported
[root@red-hat-vsi marisa]# 


