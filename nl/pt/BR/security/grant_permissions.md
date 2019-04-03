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

# Concedendo permissões para gerenciar logs e visualizar logs de conta
{: #grant_permissions}

No {{site.data.keyword.Bluemix}}, é possível designar a um usuário uma ou mais funções do IAM. Essas funções definem quais tarefas estão ativadas para esse usuário para trabalhar com o serviço {{site.data.keyword.loganalysisshort}}.  
{:shortdesc}

Por exemplo, é possível conceder a um usuário a função de **operador** para permitir que ele gerencie logs. Se você desejar que apenas um usuário visualize logs da conta, será possível conceder ao usuário a função de **visualizador**. Para obter mais informações, veja [Funções do IAM](/docs/services/CloudLogAnalysis/security_ov.html#iam_roles).

**Nota:** 

* Para conceder permissões a um usuário para gerenciar logs ou visualizar logs da conta, deve-se ter permissões para designar políticas a outros usuários na conta ou deve-se ser o proprietário da conta. Caso você não seja o proprietário da conta, deve-se ter uma política do IAM com a função de editor, operador ou administrador.
* Para conceder permissões a um usuário para visualizar logs em um espaço, deve-se ter permissões na organização e espaço para designar ao usuário uma função do Cloud Foundry que descreva as ações que ele pode executar com o serviço {{site.data.keyword.loganalysisshort}} nesse espaço. 

## Designar uma política do IAM a um usuário por meio da UI do {{site.data.keyword.Bluemix_notm}}
{: #grant_permissions_ui_account}

Conclua as etapas a seguir para conceder a um usuário permissões para trabalhar com o serviço {{site.data.keyword.loganalysisshort}}:

1. Efetue login no console do {{site.data.keyword.Bluemix_notm}}.

    Abra um navegador da web e ative o painel do {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](http://bluemix.net){:new_window}
	
	Depois de efetuar login com seu ID de usuário e senha, a UI do {{site.data.keyword.Bluemix_notm}} é aberta.

2. Na barra de menus, clique em **Gerenciar > Conta > Usuários**. 

    A janela *Usuários* exibe uma lista de usuários com seus endereços de e-mail para a conta selecionada atualmente.
	
3. Se o usuário é um membro da conta, selecione o nome do usuário na lista ou clique em **Gerenciar usuário** no menu *Ações*.

    Se o usuário não é um membro da conta, veja [Convidando usuários](/docs/iam/iamuserinv.html#iamuserinv).

4. Na seção **Políticas de acesso**, clique em **Designar acesso** e, em seguida, selecione **Designar acesso aos recursos**.

    A janela *Designar acesso a recursos ao usuário** é aberta.

5. Insira informações sobre a política. A tabela a seguir lista os campos que são necessários para definir uma política: 

    <table>
	  <caption>Lista de campos para configurar uma política do IAM.</caption>
	  <tr>
	    <th>Campo</th>
		<th>Valor</th>
	  </tr>
	  <tr>
	    <td>Serviços</td>
		<td>*IBM Cloud Log Analysis*</td>
	  </tr>	  
	  <tr>
	    <td>Regiões</td>
		<td>É possível especificar as regiões nas quais o acesso será concedido ao usuário para trabalhar com logs. Selecione uma ou mais regiões individualmente ou selecione **Todas as regiões atuais** para conceder acesso a todas as regiões.</td>
	  </tr>
	  <tr>
	    <td>Instância de serviço</td>
		<td>Selecione *Todas as instâncias de serviço*.</td>
	  </tr>
	  <tr>
	    <td>Funções</td>
		<td>Selecione uma ou mais funções do IAM. <br>As funções válidas são: *administrador*, *operador*, *editor* e *visualizador*. <br>Para obter mais informações sobre as ações que são permitidas por função, veja [Funções do IAM](/docs/services/CloudLogAnalysis/security_ov.html#iam_roles).
		</td>
	  </tr>
     </table>
	
6. Clique em **Designar**.
	
A política que você configura é aplicável às regiões selecionadas. 


## Designar uma política do IAM a um usuário usando a linha de comandos
{: #grant_permissions_commandline}

Conclua as etapas a seguir para conceder a um usuário acesso para visualizar logs de contas usando a linha de comandos:

1. Em um terminal, efetue login na conta do {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Verifique se o usuário é um membro da conta. Execute o comando a seguir para obter a lista de usuários na conta:

    ```
	ibmcloud account users
	```
    {: codeblock}	

	Uma lista de usuários com seus GUIDs é exibida.

3. Se o usuário não for um membro da conta, entre em contato com o proprietário da conta e solicite um convite do usuário para a conta. Para obter mais informações, veja [Convidando usuários](/docs/iam/iamuserinv.html#iamuserinv).

    **Dica:** o comando para convidar um usuário para uma conta é o seguinte: `ibmcloud iam account-user-invite USER_EMAIL`
		
4. Designe uma política ao usuário. Execute o comando a seguir:

    ```
    ibmcloud iam user-policy-create USER_NAME --roles ROLE --service-name ibmloganalysis
	```
	{: codeblock}

	Em que
    * USER_NAME é o ID do {{site.data.keyword.Bluemix_notm}} do usuário.
	* ROLE é uma função do IAM. Os valores válidos são: *administrator*, *operator*, *editor* e *viewer*

5. Verifique se a política foi designada ao usuário. Execute o comando a seguir para listar todas as políticas designadas a um usuário:

    ```
    ibmcloud iam user-policies USER_NAME
	```
	{: codeblock}




## Concedendo permissões a um usuário para visualizar logs de espaço usando a UI do {{site.data.keyword.Bluemix_notm}}
{: #grant_permissions_ui_space}

Para conceder permissões a um usuário para visualizar logs em um espaço, deve-se designar ao usuário uma função do Cloud Foundry que descreva as ações que ele pode executar com o serviço {{site.data.keyword.loganalysisshort}} no espaço. 

Conclua as etapas a seguir para conceder a um usuário permissões para trabalhar com o serviço {{site.data.keyword.loganalysisshort}}:

1. Efetue login no console do {{site.data.keyword.Bluemix_notm}}.

    Abra um navegador da web e ative o painel do {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](http://bluemix.net){:new_window}
	
	Depois de efetuar login com seu ID de usuário e senha, a UI do {{site.data.keyword.Bluemix_notm}} é aberta.

2. Na barra de menus, clique em **Gerenciar > Conta > Usuários**. 

    A janela *Usuários* exibe uma lista de usuários com seus endereços de e-mail para a conta selecionada atualmente.
	
3. Se o usuário é um membro da conta, selecione o nome do usuário na lista ou clique em **Gerenciar usuário** no menu *Ações*.

    Se o usuário não é um membro da conta, veja [Convidando usuários](/docs/iam/iamuserinv.html#iamuserinv).

4. Selecione **Acesso do Cloud Foundry** e, em seguida, selecione a organização.

    Os espaços disponíveis nessa organização estão listados.

5. Escolha um espaço. Em seguida, na ação de menu, selecione **Editar função de espaço**.

6. Selecione uma ou mais funções de espaço. As funções válidas são: *Gerenciador*, *Desenvolvedor* e *Auditor*
	
7. Clique em **Salvar função**.




