



FAQ logging


An ingestion key can only be reset or new ones created in the LogDNA web UI. You can have a maximum of 10 ingestion keys active at the same time in a LogDNA instance.
In IBM Cloud - Observability - Logging UI, you can only see 1 ingestion key that is active for a LogDNA instance.
When you provision a LogDNA instance via the UI, 2 things happen: 1) an instance is provisioned, and 2) a service  key is created for the instance. This service key includes information about the ingestion key that you can see via the UI.
If you provision an instance thorugh the CLI, you must manually create the service key to retrieve the ingestion key so you can see it from the IBM Cloud UI. (https://cloud.ibm.com/docs/Log-Analysis-with-LogDNA?topic=LogDNA-provision#provision_cli_2)
When the service key is not available, in the UI you get the option to "Create Key" because the ingestion key is not available for display. The option should be "Retrieve the key" since you are not generating a new ingestion key but retrieving one that is already active in the LogDNA instance.   The UI team is looking into making it more clear.
If you need to reset the ingestion key (for example, if you need to rotate or if the key is compromissed) , you need to do it from the LogDNA web UI. You must create a new ingestion key and delete the old one.

