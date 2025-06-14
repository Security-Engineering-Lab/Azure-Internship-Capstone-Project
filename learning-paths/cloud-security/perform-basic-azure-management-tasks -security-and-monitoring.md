

# Perform basic Azure Management Tasks (Security and Monitoring)

https://learn.microsoft.com/en-us/training/paths/perform-basic-azure-management-tasks/




# 2 Configure and manage secrets in Azure Key Vault

Storing and handling secrets, encryption keys, and certificates directly is risky. Every usage introduces the possibility of unintentional data exposure. Azure Key Vault provides a secure storage area for managing all your app secrets so you can properly encrypt your data in transit or while it's being stored.

# 2.1 Introduction

PetDash is an online pet food delivery company that provides store-to-door service for all their customer's pet needs. They take online orders, store credit cards and personal details in their SQL database, and have a secure website running on Azure App Service to interact with customers. They've been in business a little over a year. Steve, one of the website admins, noticed that their website certificate for the **petdash.com** domain has expired. Steve quickly renews the certificate, gets it installed on the server, and begins to explore ways to ensure that this problem never happens again. The investigation reveals that Azure Key Vault supports certificate management. Even better, Key Vault can communicate with App Service to provide the certification *and* renew it automatically if necessary.

**Azure Key Vault** helps safeguard cryptographic keys and secrets that cloud applications and services use. Key Vault streamlines the key management process and enables you to maintain control of keys that access and encrypt your data. Developers can create keys for development and testing in minutes, and then migrate them to production keys. Security administrators can grant (and revoke) permission to keys, as needed.

## Learning objectives

In this module, you will:

- Explore proper usage of Azure Key Vault.
- Manage access to an Azure Key Vault.
- Explore certificate management with Azure Key Vault.
- Configure a Hardware Security Module Key-generation solution.

# 2.2 Guidelines for using Azure Key Vault

Azure Key Vault is a centralized cloud service for storing application secrets such as encryption keys, certificates, and server-side tokens. Key Vault helps you control your applications' secrets by keeping them in a single central location and providing secure access, permissions control, and access logging.

There are three primary concepts used in an Azure Key Vault: vaults, keys, and secrets.

## Vaults

You use Azure Key Vault to create multiple secure containers, called vaults. Vaults help reduce the chances of accidental loss of security information by centralizing application secrets storage. Organizations have several key vaults. Each key vault is a collection of cryptographic keys and cryptographically protected data (call them "secrets") managed by one or more responsible individuals within your organization. These key vaults represent the logical groups of keys and secrets for your organization that you want to manage together. They are like folders in the file system. Key vaults also control and log the access to anything stored in them.

You can create and manage vaults using command line tools such as Azure PowerShell or the Azure CLI, using the REST API, or through the Azure portal.

For example, here's a sample Azure CLI command line to create a new vault in a resource group:

**Azure CLI**
```bash
az keyvault create \
    --resource-group <resource-group> \
    --name <your-unique-vault-name>
```

Here's the same command using Azure PowerShell:

**PowerShell**
```powershell
New-AzKeyVault -Name <your-unique-vault-name> -ResourceGroupName <resource-group>
```

## Keys

Keys are the central actor in the Azure Key Vault service. A given key in a key vault is a cryptographic asset destined for a particular use. Examples are, the asymmetric master key of Microsoft Azure RMS, or the asymmetric keys used for SQL Server TDE (Transparent Data Encryption), CLE (Column Level Encryption), and Encrypted backup.

Microsoft and your apps don't have access to the stored keys directly once a key is created or added to a key vault. Applications must use your keys by calling cryptography methods on the Key Vault service. The Key Vault service performs the requested operation within its hardened boundary. The application never has direct access to the keys.

Keys can be single instanced (only one key exists) or be versioned. In the versioned case, a key is an object with a primary (active) key, and a collection of zero, one, or more secondary (archived) keys created when keys are rolled (renewed). Key Vault supports asymmetric keys (RSA 2048). Your applications may use these keys for encryption or digital signatures.

There are two variations on keys in Key Vault: hardware-protected and software-protected.

### Hardware-protected keys

The Key Vault service supports using hardware security modules (HSMs) that provide a hardened, tamper-resistant environment for cryptographic processing and key generation. Azure has dedicated HSMs validated to FIPS 140-2 Level 2 that Key Vault uses to generate or store keys. These HSM-backed keys are always locked to the boundary of the HSM. When you query the Key Vault service to decrypt or sign with a key, the operation is performed inside an HSM.

You can import keys from your own HSMs, and transfer them to Key Vault without leaving the HSM boundary. This scenario is often referred to as bring your own key or BYOK. More details about generating your own HSM-protected key and then transferring it to Azure Key Vault is available in the summary of this module. You can also use these Azure HSMs directly through the Microsoft Azure Dedicated Hardware Security Module (HSM) service if you need to migrate HSM-protected apps or maintain a high security compliance requirement.

### Software-protected keys

Key Vault can also generate and protect keys using software-based RSA and ECC algorithms. In general, software-protected keys offer most of the features as HSM-protected keys except the FIPS 140-2 Level 2 assurance:

- Your key is still isolated from the application (and Microsoft) in a container that you manage.
- It's stored at rest encrypted with HSMs.
- You can monitor usage using Key Vault logs.

The primary difference (besides price) with a software-protected key is that cryptographic operations are performed in software using Azure compute services. With HSM-protected keys, the cryptographic operations are performed within the HSM.

> **Tip**
> 
> For production use, it's recommended to use HSM-protected keys and use software-protected keys in only test/pilot scenarios. There's an additional charge for HSM-backed keys per-month if the key is used in that month. The summary page has a link to the pricing details for Azure Key Vault.

You determine the key generation type when you create the key. For example, the Azure PowerShell command Add-AzureKeyVaultKey has a Destination parameter that can be set to either Software or HSM:

**PowerShell**
```powershell
$key = Add-AzureKeyVaultKey -VaultName 'contoso' -Name 'MyFirstKey' -Destination 'HSM'
```

## Secrets

Secrets are small (less than 10K) data blobs protected by a HSM-generated key created with the Key Vault. Secrets exist to simplify the process of persisting sensitive settings that almost every application has: storage account keys, .PFX files, SQL connection strings, data encryption keys, etc.

## Key vault uses

With these three elements, an Azure Key Vault helps address the following issues:

**Secrets management:** Azure Key Vault can securely store (with HSMs) and tightly control access to tokens, passwords, certificates, API keys, and other secrets.

**Key management:** Azure Key Vault is a cloud-based key management solution, making it easier to create and control the encryption keys used to encrypt your data. Azure services such as App Service integrate directly with Azure Key Vault and can decrypt secrets without knowledge of the encryption keys.

**Certificate management:** Azure Key Vault is also a service that lets you easily provision, manage, and deploy public and private SSL/TLS certificates for use with Azure and your internal connected resources. It can also request and renew TLS certificates through partnerships with certificate authorities, providing a robust solution for certificate lifecycle management.

> **Important**
> 
> Key Vault is designed to store configuration secrets for server applications. It's not intended for storing data belonging to your app's users, and it shouldn't be used in the client-side part of an app. This is reflected in its performance characteristics, API, and cost model.
> 
> User data should be stored elsewhere, such as in an Azure SQL database with Transparent Data Encryption, or a storage account with Storage Service Encryption. Secrets used by your application to access those data stores can be kept in Key Vault.

## Best practices

Here are some security best practices for using Azure Key Vault.

| Best practice | Solution |
|---|---|
| Grant access to users, groups, and applications at a specific scope. | Use RBAC's predefined roles. For example, to grant access to a user to manage key vaults, you would assign the predefined role Key Vault Contributor to this user at a specific scope. The scope, in this case, would be a subscription, a resource group, or just a specific key vault. If the predefined roles don't fit your needs, you can define your own roles. |
| Control what users have access to. | Access to a key vault is controlled through two separate interfaces: management plane and data plane. The management plane and data plane access controls work independently. Use RBAC to control what users have access to. For example, if you want to grant an application the rights to use keys in a key vault, you only need to grant data plane access permissions using key vault access policies. No management plane access is needed for this application. Conversely, if you want a user to be able to read vault properties and tags but not have any access to keys, secrets, or certificates. You can use RBAC to grant read access to the management plane. No access to the data plane is required. |
| Store certificates in your key vault. | Azure Resource Manager can securely deploy certificates stored in Azure Key Vault to Azure VMs when the VMs are deployed. By setting appropriate access policies for the key vault, you also control who gets access to your certificate. Another benefit is that you manage all your certificates in one place in Azure Key Vault. |
| Ensure that you can recover a deletion of key vaults or key vault objects. | Deletion of key vaults or key vault objects can be either inadvertent or malicious. Enable the soft delete and purge protection features of Key Vault, particularly for keys that are used to encrypt data at rest. Deletion of these keys is equivalent to data loss, so you can recover deleted vaults and vault objects if needed. Practice Key Vault recovery operations regularly. |

> **Note**
> 
> If a user has contributor permissions (RBAC) to a key vault management plane, they can grant themselves access to the data plane by setting a key vault access policy. It's recommended that you tightly control who has contributor access to your key vaults, to ensure that only authorized persons can access and manage your key vaults, keys, secrets, and certificates.


# 2.3 Manage access to secrets, certificates, and keys

Key Vault access has two facets: the management of the Key Vault itself, and accessing the data contained in the Key Vault. Documentation refers to these facets as the *management plane* and the *data plane*.

These two areas are separated because the creation of the Key Vault is a management operation, while storing and retrieving a secret stored in the Key Vault is a different type of role. To access a key vault all users or apps must have proper *authentication* to identify the caller and *authorization* to determine the operations the caller can perform.

## Authentication

Azure Key Vault uses Microsoft Entra ID to authenticate users and apps that try to access a vault. Authentication is always performed by associating the request with the Microsoft Entra tenant of the subscription that the Key Vault is part of. Every user or app making a request must be known to Microsoft Entra ID. There's no support for anonymous access to a Key Vault.

## Authorization

Management operations (creating a new Azure Key Vault) use role-based access control (RBAC). There's a built-in role **Key Vault Contributor** that provides access to management features of key vaults, but it doesn't allow access to the key vault data. This role is the recommended role to use. There's also a **Contributor** role that includes full administration rights - including the ability to grant access to the data plane.

Reading and writing data in the Key Vault uses a separate Key Vault *access policy*. A Key Vault access policy is a permission set assigned to a user or managed identity to read, write, and/or delete secrets and keys. You can create an access policy using the CLI, REST API, or Azure portal as follows.

![](https://learn.microsoft.com/en-us/training/modules/configure-and-manage-azure-key-vault/media/3-add-key-vault-policy.png)

The system has a list of predefined management options that define the permissions allowed for this policy. Here we've selected **Key, Secret, & Certificate Management**, which is appropriate to manage secrets in the Key Vault. You can then customize the permissions as desired by changing the **Key permissions** entries. For example, we could adjust the permissions to only allow *read* operations:

![](https://learn.microsoft.com/en-us/training/modules/configure-and-manage-azure-key-vault/media/3-permissions.png)

Developers only need `Get` and `List` permissions to a development-environment vault. A lead or senior developer needs full permissions to the vault to change and add secrets when necessary. Full permissions to production-environment vaults are typically reserved for senior operations staff. Apps only require `Get` permissions as they often only need to retrieve secrets.

## Restrict network access

Another point to consider with Azure Key Vault is what services in your network can access the vault. In most cases, the network endpoints don't need to be open to the Internet. You should determine the minimum network access required. For example, you can restrict Key Vault endpoints to specific Azure Virtual Network subnets, specific IP addresses, or trusted Microsoft services. Services include Azure SQL, Azure App Service, and various data and storage services that use encryption keys.

![](https://learn.microsoft.com/en-us/training/modules/configure-and-manage-azure-key-vault/media/3-network-rules.png)


# 2.4 Exercise - store secrets in Azure Key Vault

## Verify your account

To get some quick experience with Azure Key Vault, let's create a new Key Vault and do the most basic operation available: store a secret. Creating a vault in the Azure portal requires no initial configuration. Your signed-in user identity is automatically granted the full set of secret management permissions, and you can start adding secrets immediately. Once you have a vault, adding and managing secrets can be done from any Azure administrative interface, including the Azure portal, the Azure CLI, and Azure PowerShell.

## Create a new Azure Key Vault

Let's start by creating a new Key Vault in the Azure portal.

1. Sign in to the Azure portal using the same credentials you used to activate the Azure Sandbox.

2. Select **Create a resource**. The Create a resource pane appears.

3. In the **Search services and marketplace**, search for and select **Key Vault** to find the Azure Key Vault service. The Key Vault pane appears.


4. Select **Create**. The Create key vault pane appears.

5. On the **Basics** tab, enter the following values for each setting.

| Setting | Value |
|---------|-------|
| **Project details** | |
| Subscription | From the dropdown, select **Concierge Subscription**. |
| Resource group | From the dropdown, select **[sandbox resource group name]**. |
| **Instance details** | |
| Key vault name | Enter a globally unique name for the new vault. Vault names must be 3-24 characters long and contain only alphanumeric characters and dashes. The exercise uses the example name of **VaultamortDiary** for the new vault. |
| Region | Accept default. |
| Pricing tier | Accept default. |

6. Select **Review + create**.

7. After validation passes, select **Create** to create the Azure Key Vault.

8. After the deployment is complete, select **Go to resource**. Your Key vault pane appears.

## Add a secret

Next, add a new secret to the vault.

1. In the left menu pane, under **Objects**, select **Secrets**. The Secrets pane appears for your key vault.

2. In the top menu bar, select **Generate/Import**. The Create a secret pane appears.

3. Enter a name, value, and (optional) content type. An example follows.

   *Screenshot showing the Create a secret pane in the Azure portal for Azure Key Vault.*

![](https://learn.microsoft.com/en-us/training/modules/configure-and-manage-azure-key-vault/media/1-create-secret.png)
   

5. Select **Create** to add the secret. The Secrets pane reappears.

## Show the secret

Finally, verify that the secret value has been set.

1. Select your secret from the list. The Versions pane appears for your secret.

2. Select the **CURRENT VERSION** of the secret. The Secret Version pane appears.

3. Select **Show Secret Value** to see the value assigned to the secret.

   *Screenshot showing the secret value in the Azure portal.*

   ![](https://learn.microsoft.com/en-us/training/modules/configure-and-manage-azure-key-vault/media/1-show-secret.png)

## Other ways to consume the secret

You can create and retrieve secrets from the Azure Key Vault as long as you're authenticated with Microsoft Entra ID using the REST API, native SDKs, Azure CLI, or Azure PowerShell. For example, here's the same process using Azure PowerShell.

**PowerShell**
```powershell
Get-AzKeyVault
```

This command returns the created vault with the name VaultamortDiary.

**Output**
```
Vault Name          : VaultamortDiary
Resource Group Name : Learn-4f01665a-1272-46a8-9c16-83bbf146494e
Region              : northcentralus
Resource ID         : /subscriptions/xyz/providers/Microsoft.KeyVault/vaults/VaultamortDiary
```

With the name of the vault and the key, you can retrieve the secret value:

**PowerShell**
```powershell
Get-AzKeyVaultSecret -VaultName 'VaultamortDiary' -Name 'HiddenLocation'
```

This command returns our set value:

**Output**
```
Vault Name   : vaultamortdiary
Name         : VaultamortDiary
Version      : ff4b23af35bf4ba9a5c8792227d00ff6
Id           : https://vaultamortdiary1972.vault.azure.net:44
               3/secrets/VaultamortDiary/ff4b23af35bf4ba9
               a5c8792227d00ff6
Enabled      : True
Expires      :
Not Before   :
Created      : 12/17/2020 7:54:03 PM
Updated      : 12/17/2020 7:54:03 PM
Content Type : text
Tags         :
```

> **Note**
> 
> The module **Manage secrets in your server apps with Azure Key Vault** shows how to use the Azure CLI and various programming languages to create Key Vaults, set, and retrieve secrets.



# 2.6 Manage certificates

Securely managing certificates is a challenge for every organization. You must ensure that the private key is kept safe. As Steve from PetDash found out, certificates have an expiration date and have to be renewed periodically to ensure your website traffic is secure.

## Add certificates to a Key Vault

Azure Key Vault manages X.509 based certificates that can come from several sources.

First, you can create self-signed certificates directly in the Azure portal. This process creates a public/private key pair and signs the certificate with its own key. These certificates can be used for testing and development.

Second, you can create an X.509 certificate signing request (CSR). This process creates a public/private key pair in Key Vault along with a CSR you can pass over to your certification authority (CA). The signed X.509 certificate can then be merged with the held key pair to finalize the certificate in Key Vault as shown in the following diagram.

*Diagram showing the process to create a certificate with your own certificate authority.*

![](https://learn.microsoft.com/en-us/training/modules/configure-and-manage-azure-key-vault/media/5-certificate-authority-1.png)

In the previous diagram, your application is creating a certificate, which internally begins by creating a key in your Azure Key Vault.

1. Key Vault returns a Certificate Signing Request (CSR) to your application.
2. Your application passes the CSR to your chosen CA.
3. Your chosen CA responds with an X.509 Certificate.
4. Your application completes the new certificate creation with a merger of the X.509 Certificate from your CA.

This approach works with any certificate issuer and provides better security than handling the CSR directly. The process is more secure because the private key is created and secured in Azure Key Vault and never revealed.

Third, you can connect your Key Vault with a trusted certificate issuer (referred to as an integrated CA) and create the certificate directly in Azure Key Vault. This approach requires a one-time setup to connect the certificate authority. You can then request to create a certificate, and the Key Vault interacts directly with the CA to fulfill the request in a similar process to the manual CSR creation process shown previously. The full details of this process are presented in the following diagram.

*Diagram showing the process to create a certificate with an integrated certificate authority.*

![](https://learn.microsoft.com/en-us/training/modules/configure-and-manage-azure-key-vault/media/5-certificate-authority-2.png)

In the previous diagram, your application is creating a certificate, which begins internally by creating a key in your key vault.

1. Key Vault sends an SSL Certificate Request to the CA.
2. Your application polls, in a loop and wait process, for your Key Vault for certificate completion. The certificate creation is complete when Key Vault receives the CA's response with x509 certificate.
3. The CA responds to Key Vault's SSL Certificate Request with an X509 SSL Certificate.
4. Your new certificate creation completes with the merger of the X509 Certificate for the CA.

This approach has several distinct advantages. Because the Key Vault is connected to the issuing CA, it can manage and monitor the lifecycle of the certificate. That means it can automatically renew the certificate, notify you about expiration, and monitor events such as whether the certificate has been revoked.

Finally, you can import existing certificates - importing allows you to add certificates to the Key Vault that you're already using. The imported certificate can be in either PFX or PEM format and must contain the private key. For example, here's a PowerShell script to upload a certificate:

**PowerShell**
```powershell
$pfxFilePath = "C:\WebsitePrivateCertificate.pfx"
$pwd = "password-goes-here"
$flag = [System.Security.Cryptography.X509Certificates.X509KeyStorageFlags]::Exportable
$pkcs12ContentType = [System.Security.Cryptography.X509Certificates.X509ContentType]::Pkcs12

$collection = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2Collection  
$collection.Import($pfxFilePath, $pwd, $flag)

$clearBytes = $collection.Export($pkcs12ContentType)
$fileContentEncoded = [System.Convert]::ToBase64String($clearBytes)
$secret = ConvertTo-SecureString -String $fileContentEncoded -AsPlainText –Force
$secretContentType = 'application/x-pkcs12'

# Replace the following <vault-name> and <key-name>.
Set-AzKeyVaultSecret -VaultName <vault-name> -Name <key-name> -SecretValue $secret -ContentType $secretContentType
```

## Retrieve certificates from a Key Vault

Once a certificate is stored in your Azure Key Vault, you can use the Azure portal to explore the certificate properties and enable or disable a certificate to make it unavailable to clients.

*Screenshot showing the certificate properties in the Azure portal.*

![](https://learn.microsoft.com/en-us/training/modules/configure-and-manage-azure-key-vault/media/5-certificate-properties.png)

## Azure App Service integration

Once you have a public/private key pair certificate in your Azure Key Vault, you can easily associate it to your web app through the Azure portal.

1. Select **TLS/SSL settings** under **Settings**.

2. Select the **Private Key Certificate (.pfx)** tab.

3. Select **Import Key Vault Certificate** as shown in the following screenshot.

*Screenshot of the Azure portal where you can load a Key Vault certificate to an Azure App Service web app.*

![](https://learn.microsoft.com/en-us/training/modules/configure-and-manage-azure-key-vault/media/5-add-cert-to-webapp.png)

You can then select the vault, which must be in the same subscription, and the secret containing the certificate.

The certificate must be an X.509 cert with a content type of application/x-pkcs12 and can't have a password.

Finally, once the certificate is in place, you want to set up a custom domain. There's already a built-in certificate for *.azurewebsites.net. You can then associate your custom domain with the certificate you've assigned so the server uses your certificate to secure the connection to the browser.

# 2.7 Summary

After you have a key vault, you can start using it to store keys and secrets. Your applications no longer need to persist this confidential data but can request them from the vault as needed. A key vault allows you to update keys and secrets without affecting the behavior of your application, which opens up a breadth of possibilities for your key, secret, and certificate management.

In this module, you've learned about several security benefits of AKV:

- You can create a segmentation of security roles – no one person has the keys to the kingdom.
- The service is monitored and access is logged – giving you the capability to track user activity and prevent, detect, and minimize a security incident.
- You can avoid mistakes – other than the creation of the vault, the services can be automated.
- AKV cloud services are available, accessible, and distributed to ensure high reliability for your services.

## Further reading

Continue learning about Azure Key Vault in the Microsoft Learn module **Manage secrets in your server apps with Azure Key Vault**.

Read Azure Key Vault documentation about subjects we covered in this module:

- What is Azure Key Vault?
- Azure Key Vault pricing
- About Azure Key Vault certificates
- Implementing bring your own key (BYOK) for Azure Key Vault





