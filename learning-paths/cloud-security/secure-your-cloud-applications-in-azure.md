

# Secure your cloud applications in Azure

https://learn.microsoft.com/en-us/training/paths/secure-your-cloud-apps/


# 2 Top 5 security items to consider before pushing to production

Secure your web applications on Azure and protect your apps against the most common and dangerous web application attacks.

# 2.1 Introduction

Security is top of mind for most people working in technology, and this is especially true when it comes to software. It seems we're constantly hearing about companies and governments to which we entrusted our private data being compromised. When this happens, either maliciously or accidentally, it costs them customers and, ultimately, money.

Did you know that the most common cause of data breaches is poor security in software? It's true. This means that the pressure is on for software developers to be more diligent than ever. But where do they begin? This module is the start of your journey into the world of application security, with the top five defenses for web applications. Learn how to secure your web applications on Azure and protect your apps against the most common and dangerous web application attacks.

## Learning objectives

In this module, you will:

* Use Microsoft Defender for Cloud.
* Verify your application's inputs and outputs.
* Store your secrets into Key Vault.
* Ensure you're using the latest version of your framework, and its security features.
* Validate that your program dependencies and libraries are safe to use.



# 2.1 Microsoft Defender for Cloud

Two of the biggest problems with security are being able to see all the areas you need to protect and to find vulnerabilities before hackers do. Azure provides a service called Microsoft Defender for Cloud that makes this much easier.

## What is Microsoft Defender for Cloud?

Microsoft Defender for Cloud is a monitoring service that provides threat protection across all of your services, both in Azure and on-premises. It can:

- **Provide security recommendations** based on your configurations, resources, and networks.
- **Monitor security settings** across on-premises and cloud workloads and automatically apply required security to new services as they come online.
- **Continuously monitor** all your services and perform automatic security assessments to identify potential vulnerabilities before they can be exploited.
- **Use machine learning** to detect and block malware from being installed in your services and virtual machines. You can also allowlist applications to ensure that only the apps you validate are allowed to execute.
- **Analyze and identify** potential inbound attacks and help to investigate threats and any post-breach activity which might have occurred.
- **Enable Just-In-Time access control** for ports, reducing your attack surface by ensuring the network only allows traffic you require.

Defender for Cloud is part of the Center for Internet Security (CIS) recommendations.

## Activating Microsoft Defender for Cloud

Microsoft Defender for Cloud provides unified security management and advanced threat protection for hybrid cloud workloads, and is offered in several plans. The **Foundational Cloud Security Posture Management (CSPM)** plan, which is free and activated by default provides security policies, assessments, and recommendations. The **Defender CSPM** plan provides a robust set of features, including threat intelligence. There are also plans for Servers, App Service, and more.

Given the benefits of Defender for Cloud, your company's security team has decided to turn it on for all subscriptions at your office. You got an email this morning to turn it on for your applications, so let's look at how to do that.

> **Important**
> 
> Microsoft Defender for Cloud is not supported in the free Azure sandbox. You can perform these steps in your own subscription, or just follow along to understand how to activate Defender for Cloud.

### Steps to Activate:

1. Open the Azure portal and select **Microsoft Defender for Cloud** from the left-hand menu. If you don't see it there, you can select **All services** and find Microsoft Defender for Cloud in the security section.

2. If you've never opened Defender for Cloud, the pane starts on the **Getting started** entry, which might ask you to upgrade your subscription. Ignore that for now; select **Skip** at the bottom of the page, then select **Overview**.

3. This will display the "big security picture" across all the elements available in your subscription with tons of great information you can explore.

4. The Overview displays what subscription elements are being covered (or not covered) by Defender for Cloud. Here you can turn on Defender for Cloud for any subscription to which you have access.

5. You can activate Defender for Cloud on your subscription. Select **Azure subscriptions** at the top of the page, then select your subscription in the list. You can choose to turn plans on or off, or select **Enable all plans**.

## Foundational CSPM vs. Defender CSPM Pricing Tier

Although you can use a free Azure subscription tier with Defender for Cloud, it's limited to assessments and recommendations of Azure resources only. To really leverage Defender for Cloud, you'll need to upgrade to a Defender CSPM subscription. You can upgrade your subscription through the **Upgrade** button on the Getting Started pane in the Defender for Cloud menu, which will walk you through changing your subscription level. The pricing and features might change based on the region; you can get a full overview on the pricing page.

> **Note**
> 
> To upgrade a subscription to the Defender CSPM tier, you must be assigned the role of Subscription Owner, Subscription Contributor, or Security Admin.

> **Important**
> 
> After the 30-day trial period is over, Defender CSPM will be billed to your account.

## Turning off Microsoft Defender for Cloud

For production systems, you definitely want to keep Microsoft Defender for Cloud turned on so it can monitor all your resources for threats. However, if you're just playing with Defender for Cloud and turned it on, you'll likely want to disable it to ensure you're not charged. Let's do that now.

### Steps to Turn Off:

1. Open the Azure portal and select **Microsoft Defender for Cloud** from the left-hand menu.

![](https://learn.microsoft.com/en-us/training/advocates/top-5-security-items-to-consider/media/2-asc-menu.png)

2. Select **Environment settings** under Management in the left-hand menu.

3. Next, select the ellipses next to the subscription you want to downgrade, then select **Edit settings**.

4. A new page will appear. Toggle the **Defender CSPM** plan to **Off**.

![](https://learn.microsoft.com/en-us/training/advocates/top-5-security-items-to-consider/media/2-asc-menu.png)

5. Select the **Save** button at the top of the screen.

You've now downgraded your subscription to the free tier of Microsoft Defender for Cloud.

**Congratulations, you've taken your first (and most important) step to securing your application, data and network!**

---

## Check your knowledge

**Question:** True or false: Microsoft Defender for Cloud works for Azure resources and on-premises resources.

**Відповідь: True (Правда)**

Згідно з текстом, Microsoft Defender for Cloud є сервісом моніторингу, який забезпечує захист від загроз для всіх ваших сервісів, **як в Azure, так і в on-premises середовищі**. Це чітко зазначено на початку документа: "Microsoft Defender for Cloud is a monitoring service that provides threat protection across all of your services, both in Azure and on-premises."


# 2.3 Inputs and Outputs

The most prevalent security weakness of current applications is a failure to correctly process data received from external sources, particularly user input. You should always take a close look at any input to make sure it's been validated before it's used. Failing to analyze user input for possible attacks can result in data loss or exposure, elevation of privilege, or even execution of malicious code on other users' computers.

The tragedy in this situation is that this scenario an easy problem to solve. In this unit, we cover how to treat data when it's received, when it's displayed on the screen, and when it's stored for later use.

## Why do we need to validate our input?

Imagine that you're building an interface to allow a user to create an account on your website. Our profile data includes a name, email, and a nickname that we'll display to everyone who visits the site. What if a new user creates a profile and enters a nickname that includes some SQL commands? For example, what if a malicious user enters something like the following:

```sql
Eve'); DROP TABLE Users;--
```

If we blindly insert this value into a database, it could potentially alter the SQL statement to execute commands we absolutely don't want to run! This example is referred to as a **SQL Injection attack**, which is one of the many types of exploits that can potentially happen when you don't properly handle user input. So, what can we do to fix this situation? This unit teaches you when to validate input, how to encode output, and how to create parameterized queries (which solves the above exploit). These techniques are the three main defense techniques against malicious input being entered into your applications.

## When do I need to validate input?

The answer is **always**. You must validate every input for your application. This includes parameters in the URL, input from the user, data from the database, data from an API, and anything that's passed in the clear that a user could potentially manipulate. Always use an **allowlist approach**, which means you only accept "known good" input, instead of a blocklist (where you specifically look for bad input) because it's impossible to think of a complete list of potentially dangerous input. Do this work on the server, not the client side (or in addition to the client side), to ensure that your defenses can't be circumvented. Treat ALL data as untrusted, and you'll protect yourself from most of the common web app vulnerabilities.

If you're using ASP.NET, the framework provides great support for validating input on both the client and server side.

If you're using another web framework, there are some great techniques for doing input validation available on the **OWASP Input Validation Cheatsheet**.

## Always use parameterized queries

SQL databases are commonly used to store data; for example, your application could store user profile information in a database. You should never create inline SQL or other database queries in your code using raw user input and send it directly to the database; this behavior is a recipe for disaster, as we saw previously.

For example, don't create code like the following inline SQL example:

```csharp
string userName = Request.QueryString["username"]; // receive input from the user BEWARE!
...
string query = "SELECT *  FROM  [dbo].[users] WHERE userName = '" + userName + "'";
```

Here, we concatenate text strings together to create the query, taking the input from the user and generating a dynamic SQL query to look up the user. Again, if a malicious user realized we were doing this, or just tried different input styles to see if there was a vulnerability, we could end up with a major disaster. Instead, use parameterized SQL statements or stored procedures such as this:

```sql
-- Lookup a user
CREATE PROCEDURE sp_findUser
(
@UserName varchar(50)
)

SELECT *  FROM  [dbo].[users] WHERE userName = @UserName
```

With this method, you can invoke the procedure from your code safely, passing it the userName string without worrying about it being treated as part of the SQL statement.

## Always encode your output

Any output you present either visually or within a document should always be encoded and escaped. This can protect you in case something was missed in the sanitization pass or the code accidentally generates something that can be used maliciously. This design principle makes sure that everything is displayed as output and not inadvertently interpreted as something that should be executed, which is another common attack technique that's referred to as **Cross-Site Scripting (XSS)**.

Because XSS prevention is a common application requirement, this security technique is another area where ASP.NET does the work for you. By default, all output is already encoded. If you're using another web framework, you can verify your options for output encoding on websites with the **OWASP XSS Prevention Cheatsheet**.

## Summary

Sanitizing and validating your input is a necessary requirement to ensure your input is valid and safe to use and store. Most modern web frameworks offer built-in features that can automate some of this work. You can check your preferred framework's documentation and see what features it offers. Although web applications are the most common place where this happens, keep in mind that other types of applications can be just as vulnerable. Don't think you're safe just because your new application is a desktop app. You'll still need to properly handle user input to ensure someone doesn't use your app to corrupt your data or damage your company's reputation.

---

## Check your knowledge

### 1. Which of the following data sources need to be validated?

- Data from a third-party API
- Data from the URL parameter
- Data collected from the user via an input field
- **All of the above** ✓

**Відповідь: All of the above**

Згідно з текстом, потрібно валідувати **кожен** вхідний параметр для вашого додатку. Це включає параметри в URL, вхідні дані від користувача, дані з бази даних, дані з API та все, що передається у відкритому вигляді і може бути потенційно змінено користувачем.

### 2. Parameterized queries (stored procedures in SQL) are a secure way to talk to the database because:

- They're more organized than inline database commands, and therefore less confusing for users.
- There's a clear outline of the script in the stored procedure, ensuring better visibility.
- **Parameterized queries substitute variables before running queries, meaning it avoids the opportunity for code to be submitted in place of a variable.** ✓

**Відповідь: Parameterized queries substitute variables before running queries, meaning it avoids the opportunity for code to be submitted in place of a variable.**

Параметризовані запити безпечні тому, що вони підставляють змінні перед виконанням запитів, що уникає можливості подання коду замість змінної.

### 3. Which of the following data needs to be output encoded?

- Data saved to the database
- **Data to be output to the screen** ✓
- Data sent to a third-party API
- Data in the URL parameters

**Відповідь: Data to be output to the screen**

Згідно з текстом, будь-який вивід, який ви представляєте візуально або в документі, повинен завжди бути закодований та екранований. Це захищає від Cross-Site Scripting (XSS) атак.


# 2.4 Secrets in Key Vault

Secrets aren't secrets if they're shared with everyone. Storing confidential items like connection strings, security tokens, certificates, and passwords in your code is just inviting someone to take them and use them for something other than what you intended them for. Even storing this sort of data in your web configuration is a bad idea; you're essentially allowing anyone who has access to the source code or web server access to your private data.

Instead, you should always put these secrets into **Azure Key Vault**.

## What is Azure Key Vault?

Azure Key Vault is a *secret store*: a centralized cloud service for storing application secrets. Key Vault keeps your confidential data safe by keeping application secrets in a single central location and providing secure access, permissions control, and access logging.

Secrets are stored in individual *vaults*, each with their own configuration and security policies to control access. You can then get to your data through a REST API, or through a client SDK available for most languages.

> **Important**
> 
> **Key Vault is designed to store configuration secrets for server applications.** It's not intended for storing data belonging to your app's users, and it shouldn't be used in the client-side part of an app. This is reflected in its performance characteristics, API, and cost model.

User data should be stored elsewhere, such as in an Azure SQL database with Transparent Data Encryption, or a storage account with Storage Service Encryption. You can keep secrets your application uses to access those data stores in Key Vault.

## Why use a Key Vault for my secrets

Key management and storing secrets can be complicated and error-prone when performed manually. Rotating certificates manually means potentially going without for a few hours or days. As mentioned previously, saving your connections strings in your configuration file or code repository means someone could steal your credentials.

Key Vault allows users to store connection strings, secrets, passwords, certificates, access policies, file locks (making items in Azure read-only), and automation scripts. It also logs access and activity and allows you to monitor access control (IAM) in your subscription. It also has diagnostics, metrics, alerts, and troubleshooting tools to ensure you have the access you need.

Learn more about using an Azure Key Vault in **Manage secrets in your server apps with Azure Key Vault**.

## Summary

Credential theft, manual key rotation, and certificate renewal can be a thing of the past if you manage your secrets well by using Azure Key Vault.



# 2.5 Framework Updates

Many developers consider the frameworks and libraries they use to build their software to be primarily decided by features or personal preference. However, the framework that you choose is an important decision, not only from a design and functionality perspective, but also from a security perspective. Choosing a framework with modern security features and keeping it up to date is one of the best ways to ensure your apps are secure.

## Choose your framework carefully

The most important factor regarding security when choosing a framework is how well supported it is. The best frameworks have stated security arrangements and are supported by large communities who improve and test the framework. No software is 100% bug-free or totally secure, but when a vulnerability is identified, we want to be certain that it will be closed or have a workaround provided quickly.

Often, "well supported" is synonymous with "modern". Older frameworks tend to either be replaced or eventually fade in popularity. Even if you have significant experience with (or many apps written in) an older framework, you'll be better off choosing a modern library that has the features you need. Modern frameworks tend to build on the lessons earlier iterations learned, which makes choosing them for new apps a form of threat-surface reduction. You'll have one more app to worry about if a vulnerability is discovered in the older framework in which your legacy applications are written.

For more information on secure design and reducing threat surface, see **Microsoft Azure Well-Architected Framework - Security**.

## Keep your framework updated

Software-development frameworks (such as Java Spring and .NET Core) release updates and new versions regularly. These updates include new features, removal of old features, and often security fixes or improvements. When we allow our frameworks to become out of date, it creates technical debt. The further out of date we get, the harder and riskier it is to bring our code up to the latest version. In addition, much like the initial framework choice, staying on older versions of the framework opens you up to more security threats that have been fixed in newer releases of the framework.

As an example, from 2016-2017, more than 30 vulnerabilities were found in the Apache Struts framework. The development team quickly addressed these vulnerabilities, but some companies didn't apply the patches and paid the price in the form of a data breach. Make sure to keep your frameworks and libraries up to date.

## How do I update my framework?

Some frameworks, like Java or .NET, require an install and tend to release on a known cadence. It's a good idea to watch for new releases and plan to make a branch of your code to try it out when it's released. As an example, .NET Core maintains a release notes page you can check to find the latest versions available.

You can update more specialized libraries, such as JavaScript frameworks or .NET components, through a package manager. NPM and Webpack are popular choices for web projects, and most IDEs or build tools support them. In .NET, you can use NuGet to manage your component dependencies. Much like updating the core framework, branching your code, updating the components, and testing is a good technique to validate a new version of a dependency.

> **Note**
> 
> The dotnet command-line tool has an add package and remove package option to add or remove NuGet packages, but doesn't have a corresponding update package command. However, it turns out you can run `dotnet add package <package-name>` in your project and it will automatically upgrade the package to the latest version. This is an easy way to update dependencies without having to open the IDE.

## Take advantage of built-in security

Always check to see what security features your frameworks offer. Never roll your own security if there's a standard technique or capability built in. In addition, rely on proven algorithms and workflows, because these have often been scrutinized by many experts, critiqued, and strengthened so you can be assured they're reliable and secure.

The .NET Core framework has countless security features. Here are a few core starting places in the documentation:

- Authentication - Identity Management
- Authorization
- Data Protection
- Secure Configuration
- Security Extensibility APIs

Each of these features was written by experts in their field, then battered with tests to ensure that they work as intended and only as intended. Other frameworks offer similar features; check with the vendor that provides the framework to find out what they have in each category.

> **Warning**
> 
> Writing your own security controls, instead of using those provided by your framework, isn't only a waste of time, it's less secure.

## Microsoft Defender for Cloud

When using Azure to host your web applications, Defender for Cloud warns you if your frameworks are out of date as part of the recommendations tab. Don't forget to look there from time to time to see if there are any warnings related to your apps.

![](https://learn.microsoft.com/en-us/training/advocates/top-5-security-items-to-consider/media/5-ascframework.png)

*Screenshot of Microsoft Defender for Cloud recommending a framework upgrade.*

## Summary

Whenever possible, choose a modern framework to build your apps, always use the built-in security features, and make sure you keep it up to date. These simple rules help to ensure your application starts on a solid foundation.



# 2.6 Safe Dependencies

A large percentage of code present in modern applications is made up of the libraries and dependencies that you, the developer, choose. This is a common practice that saves time and money. However, the downside is that you're now responsible for this code—even though others wrote it—because you used it in your project. If a researcher (or worse, a hacker) discovers a vulnerability in one of these third-party libraries, the same flaw is likely also present in your app.

Using components with known vulnerabilities is a huge problem in our industry. It's so problematic that it's made the OWASP top 10 list of worst web application vulnerabilities for several years.

## Track known security vulnerabilities

The problem we have is knowing when an issue is discovered. Keeping our libraries and dependencies updated (#4 in our list!) will of course help, but it's a good idea to keep track of identified vulnerabilities that might impact your application.

> **Important**
> 
> When a system has a known vulnerability, it's much more likely also to have exploits available; code that people can use to attack those systems. If an exploit is made public, it's crucial that any affected systems are updated immediately.

**Mitre** is a non-profit organization that maintains the Common Vulnerabilities and Exposures list. This list is a publicly searchable set of known cybersecurity vulnerabilities in apps, libraries, and frameworks. **If you find a library or component in the CVE database, it has known vulnerabilities**.

The security community submits issues when a security flaw is found in a product or component. Each published issue is assigned an ID and contains the date discovered, a description of the vulnerability, and references to published workarounds or vendor statements about the issue.

## How to verify if you have known vulnerabilities in your third-party components

You could put a daily task into your phone to check this list, but luckily for us, many tools exist that allow us to verify if our dependencies are vulnerable. You can run these tools against your codebase, or better yet, add them to your CI/CD pipeline to automatically check for issues as part of the development process.

- **OWASP Dependency Check**, which has a Jenkins plugin
- **Snyk**, which is free for open-source repositories in GitHub
- **Black Duck**, which many enterprises use
- **Retire.js** a tool for verifying if your JavaScript libraries are out of date; you can use it as a plugin for various tools, including Burp Suite

You can use some tools made specifically for static code analysis for this, as well.

- Security Code Scan
- Puma Scan
- PT Application Inspector
- Apache Maven Dependency Plugin
- Sonatype
- And many more

For more information on the risks involved in using vulnerable components, visit the **OWASP page dedicated to this topic**.

## Summary

When you use libraries or other third-party components as part of your application, you're also taking on any risks they might have. The best way to reduce this risk is to ensure that you're only using components that have no known vulnerabilities associated with them.


# 2.7 Conclusion

In this module, you learned how to safeguard your applications in Azure against common attacks. We looked at several key security tips:

- Use Microsoft Defender for Cloud
- Verify your application inputs and outputs
- Store your secrets into Key Vault
- Ensure you're using the latest version of your framework, and using its security features
- Verify your program dependencies and libraries are safe to use

By following the five items in this list, you've taken leaps and strides towards ensuring that your applications are safe and that they remain that way.


# 3 Create security baselines

In this module, you learn how to create security baselines for your Azure services by ensuring that your settings meet the minimum requirements described in CIS Benchmarks for Azure v. 1.3.0.

# 3.1 Introduction

Azure doesn't monitor security or respond to security incidents within the customer's area of responsibility. Azure does provide many tools, like Microsoft Defender for Cloud and Microsoft Sentinel, that customers can use for this purpose. There's also an effort to help make every service as secure as possible by default; that is, every service comes with a baseline that is already designed to help provide security for most common use cases. Because Azure can't predict how you'll use a service, you should always review security controls to evaluate whether they adequately mitigate risks.

This module guides you through the steps of creating a security baseline for Azure services. Each unit provides a checklist of items to verify in the services you're using in your architecture.

## Learning objectives

In this module, you'll:

* Learn about Azure platform security baselines and how they were created.
* Create and validate a security baseline for the most commonly used Azure services.


# 3.2 Understand the Azure platform security baseline


The Microsoft cybersecurity group and the Center for Internet Security (CIS) have developed best practices to help establish security baselines for the Azure platform.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/cis-benchmark.png)


Microsoft initially partnered with CIS to develop an off-the-shelf hardened Azure virtual machine (VM). An initiative then began to create a CIS benchmark—a document that details CIS best practices—for Azure security services and tools to facilitate security and compliance for customer applications running on Azure services.

> **Tip**
> 
> The **CIS Microsoft Azure Foundations Security Benchmark v. 3.0.0** provides prescriptive guidance for establishing a secure baseline configuration for Azure. This guide was tested against the listed Azure services as of September 2024. The scope of this benchmark is to establish the foundational level of security for anyone who adopts Azure.

## Create a platform security baseline

Various security standards can help cloud-service customers achieve workload security when they use cloud services. The following recommended technology groupings help create secure cloud-enabled workloads. These recommendations aren't an exhaustive list of all possible security configurations and architectures. These security baseline recommendations are a starting point.

CIS has two implementation levels and several categories of recommendations:

* **Level 1**: Recommended minimum security settings
   * These settings should be configured on all systems.
   * These settings should cause little or no interruption of services or reduced functionality.
* **Level 2**: Recommendations for highly secure environments
   * These settings might result in reduced functionality.

The following table provides the categories and number of recommendations made for each category in CIS Microsoft Azure Foundations Security Benchmark v. 3.0.0:

**Expand table**

| Technology group | Description | # of recommendations |
|------------------|-------------|---------------------|
| **Identity & Access Management (IAM)** | Recommendations related to IAM policies | 30 |
| **Microsoft Defender for Cloud** | Recommendations related to the configuration and use of Microsoft Defender for Cloud | 35 |
| **Storage accounts** | Recommendations for setting storage account policies | 17 |
| **Azure SQL Database** | Recommendations for helping to secure Azure SQL databases | 22 |
| **Logging and monitoring** | Recommendations for setting logging and monitoring policies for your Azure subscriptions | 21 |
| **Networking** | Recommendations for helping to securely configure Azure networking settings and policies | 7 |
| **VMs** | Recommendations for setting security policies for Azure compute services, and specifically VMs | 11 |
| **Other** | Recommendations regarding general security and operational controls, including recommendations related to Azure Key Vault and resource locks | 13 |
| **Total recommended** | | **156** |

Let's explore each category in more detail.


# 3.3 Create an Identity & Access Management baseline

Identity and access management (IAM) is key to granting access and to the security enhancement of corporate assets. To secure and control your cloud-based assets, you must manage identity and access for your Azure administrators, application developers, and application users.

## IAM security recommendations

The following sections describe the IAM recommendations that are in CIS Microsoft Azure Foundations Security Benchmark v. 3.0.0. Included with each recommendation are the basic steps to complete in the Azure portal. You should complete these steps for your own subscription and by using your own resources to validate each security recommendation. Keep in mind that Level 2 options might restrict some features or activities, so carefully consider which security options you decide to enforce.

> **Important**
> 
> You must be an administrator for the Microsoft Entra instance to complete some of these steps.

## Restrict access to the Microsoft Entra administration portal - Level 1

Users who aren't administrators shouldn't have access to the Microsoft Entra administration portal because the data is sensitive and under the rules of least privilege.

1. Sign in to the Azure portal. Search for and select **Microsoft Entra ID**.

2. In the left menu under **Manage**, select **Users**.

3. In the left menu, select **User settings**.

4. In **User settings**, under **Administration center**, ensure that **Restrict access to Microsoft Entra administration center** is set to **Yes**. Setting this value to **Yes** prevents all non-administrators from accessing any data in the Microsoft Entra administration portal. The setting doesn't restrict access to using PowerShell or another client, such as Visual Studio.

5. If you change any settings, select **Save** in the menu bar.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/identity-access-management-azure-active-directory/restrict-access-admin-portal.png)

## Enable multifactor authentication for Microsoft Entra users

- **Enable multifactor authentication for Microsoft Entra ID privileged users - Level 1**
- **Enable multifactor authentication for Microsoft Entra non-privileged users - Level 2**

Enable multifactor authentication for all Microsoft Entra users.

1. Sign in to the Azure portal. Search for and select **Microsoft Entra ID**.

2. In the left menu under **Manage**, select **Users**.

3. In the **All users** menu bar, select **Per-user MFA**.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/identity-access-management-azure-active-directory/multifactor-authentication-option-azure-portal.png)

4. In the **Per-user multifactor authentication** window, check the box for all users, then select **Enable MFA**.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/identity-access-management-azure-active-directory/multifactor-authentication-window-enable.png)


## Don't remember multifactor authentication on trusted devices - Level 2

Remembering the multifactor authentication feature for devices and browsers that are trusted by the user is a free feature for all multifactor authentication users. Users can bypass subsequent verifications for a specified number of days after they've successfully signed in to a device by using multifactor authentication.

If an account or device is compromised, remembering multifactor authentication for trusted devices can negatively affect security. A security recommendation is to turn off remembering multifactor authentication for trusted devices.

1. Sign in to the Azure portal. Search for and select **Microsoft Entra ID**.

2. In the left menu under **Manage**, select **Users**.

3. In the **All users** menu bar, select **Per-user MFA**.

4. In the **Per-user multifactor authentication** window, select a user. Select the **User MFA settings** button.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/identity-access-management-azure-active-directory/multifactor-authentication-window.png)

5. Select the **Restore multifactor authentication on all remembered devices** checkbox, and then select **Save**.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/identity-access-management-azure-active-directory/multifactor-authentication-user-settings.png)

## Ensure guest users are reviewed on a regular basis - Level 1

Ensure that no guest users exist, or alternatively, if the business requires guest users, ensure that guest permissions are limited.

1. Sign in to the Azure portal. Search for and select **Microsoft Entra ID**.

2. In the left menu under **Manage**, select **Users**.

3. Select the **Add filters** button.

4. For **Filters**, select **User type**. For **Value**, select **Guest**. Select **Apply** to verify that no guest users exist.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/identity-access-management-azure-active-directory/guest-users-verification.png)

5. If you change any settings, select **Save** in the menu bar.

## Password options

### Notify users on password resets - Level 1
### Notify all admins when other admins reset passwords - Level 2
### Require two methods to reset passwords - Level 1

With multifactor authentication set, an attacker would have to compromise both identity authentication forms before they could maliciously reset a user's password. Ensure that password reset requires two forms of identity authentication.

1. Sign in to the Azure portal. Search for and select **Microsoft Entra ID**.

2. In the left menu under **Manage**, select **Password reset**.

3. In the left menu under **Manage**, select **Authentication methods**.

4. Set the **Number of methods required to reset** to **2**.

5. If you change any settings, select **Save** in the menu bar.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/identity-access-management-azure-active-directory/require-two-authentication-methods.png)

## Establish an interval for reconfirming user authentication methods - Level 1

If authentication reconfirmation is turned off, registered users aren't prompted to reconfirm their authentication information. The more secure option is to turn on authentication reconfirmation for a set interval.

1. Sign in to the Azure portal. Search for and select **Microsoft Entra ID**.

2. In the left menu under **Manage**, select **Password reset**.

3. In the left menu under **Manage**, select **Registration**.

4. Ensure that **Number of days before users are asked to re-confirm their authentication information** is not set to **0**. The default is **180 days**.

5. If you change any settings, select **Save** in the menu bar.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/identity-access-management-azure-active-directory/days-until-reconfirm.png)

## Guest invite setting - Level 2

Only administrators should be able to invite guest users. Restricting invitations to administrators ensures that only authorized accounts have access to Azure resources.

1. Sign in to the Azure portal. Search for and select **Microsoft Entra ID**.

2. In the left menu under **Manage**, select **Users**.

3. In the left menu, select **User settings**.

4. In the **User settings** pane, under **External users**, select **Manage external collaboration settings**.

5. In **External collaboration settings**, under **Guest invite settings**, select **Only users assigned to specific admin roles can invite guest users**.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/identity-access-management-azure-active-directory/members-invite-guests.png)

6. If you change any settings, select **Save** in the menu bar.

## Users can create and manage security groups - Level 2

When this feature is enabled, all users in Microsoft Entra ID can create new security groups. You should restrict security group creation to administrators.

1. Sign in to the Azure portal. Search for and select **Microsoft Entra ID**.

2. In the left menu under **Manage**, select **Groups**.

3. In the **All groups** pane, in the left menu under **Settings**, select **General**.

4. For **Security Groups**, ensure that **Users can create security groups in Azure portals, API or PowerShell** is set to **No**.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/identity-access-management-azure-active-directory/security-group-settings.png)

5. If you change any settings, select **Save** in the menu bar.

## Self-service group management enabled - Level 2

Unless your business requires delegating self-service group management to various users, we recommend disabling this feature as a safety precaution.

1. Sign in to the Azure portal. Search for and select **Microsoft Entra ID**.

2. In the left menu under **Manage**, select **Groups**.

3. In the **All groups** pane, in the left menu under **Settings**, select **General**.

4. Under **Self Service Group Management**, ensure that all options are set to **No**.

5. If you change any settings, select **Save** in the menu bar.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/identity-access-management-azure-active-directory/self-service-groups.png)

## Application options - Allow users to register apps - Level 2

Require administrators to register custom applications.

1. Sign in to the Azure portal. Search for and select **Microsoft Entra ID**.

2. In the left menu under **Manage**, select **Users**.

3. In the left menu, select **User settings**.

4. In the **User settings** pane, ensure that **App registrations** is set to **No**.

5. If you change any settings, select **Save** in the menu bar.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/identity-access-management-azure-active-directory/app-registrations.png)




# 3.4 Create a Microsoft Defender for Cloud baseline

Microsoft Defender for Cloud provides unified security management and advanced threat protection for workloads that run in Azure, on-premises, and in other clouds. The following Defender for Cloud recommendations, if followed, will set various security policies on an Azure subscription. These policies define the set of controls that are recommended for your resources with an Azure subscription.

## Microsoft Defender for Cloud security recommendations

The following sections describe the Microsoft Defender for Cloud recommendations that are in CIS Microsoft Azure Foundations Security Benchmark v. 3.0.0. Included with each recommendation are the basic steps to complete in the Azure portal. You should complete these steps for your own subscription and by using your own resources to validate each security recommendation. Keep in mind that Level 2 options might restrict some features or activity, so carefully consider which security options you decide to enforce.

## View Microsoft Defender for Cloud built-in security policies

To see the Microsoft Defender for Cloud security policies for your Azure subscription:

1. Sign in to the Azure portal. Search for and select **Microsoft Defender for Cloud**.

2. In the left menu under **Management**, select **Environment settings**.

3. Select the subscription to open the **Policy settings** pane.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/microsoft-defender-for-cloud/environment-settings.png)

The enabled policies define the Microsoft Defender for Cloud recommendations, as shown in the following example:

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/microsoft-defender-for-cloud/policy-settings.png)

## Enable System Updates - Level 1

Microsoft Defender for Cloud daily monitors Windows and Linux VMs and computers for missing operating system updates. Defender for Cloud retrieves a list of available security and critical updates from Windows Update or Windows Server Update Services (WSUS). Which updates are on the list depends on which service you configure on a Windows computer. Defender for Cloud also checks for the latest updates on Linux systems. If your VM or computer is missing a system update, Defender for Cloud recommends that you apply system updates.

1. Sign in to the Azure portal. Search for and select **Microsoft Defender for Cloud**.

2. In the left menu under **Management**, select **Environment settings**.

3. Select the subscription.

4. In the left menu, select **Security policy**.

5. Under **Default initiative**, select a subscription or management group.

6. Select the **Parameters** tab.

7. Ensure that the **Only show parameters that need input or review** box is cleared.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/microsoft-defender-for-cloud/security-policies-parameters.png)

8. Ensure that **System updates should be installed on your machines** is one of the policies listed.

In the following example, the Microsoft Defender for Cloud agent hasn't been deployed to a VM or physical machine, so the message **AuditIfNotExists** appears. **AuditIfNotExists** enables auditing on resources that match the if condition. If the resource isn't deployed, **NotExists** appears.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/microsoft-defender-for-cloud/parameters-system-updates.png)

If **System updates should be installed on your machines** is enabled, **Audit** appears. If deployed but disabled, **Disabled** appears.

9. If you change any settings, select the **Review + Save** tab, and then select **Save**.

## Enable Security Configurations - Level 1

Microsoft Defender for Cloud monitors security configurations by applying a set of more than 150 recommended rules for hardening the OS. These rules are related to firewalls, auditing, password policies, and more. If a machine is found to have a vulnerable configuration, Defender for Cloud generates a security recommendation.

1. Sign in to the Azure portal. Search for and select **Microsoft Defender for Cloud**.

2. In the left menu under **Management**, select **Environment settings**.

3. Select the subscription.

4. In the left menu, select **Security policy**.

5. Under **Default initiative**, select a subscription or management group.

6. Select the **Parameters** tab.

7. Ensure that **Vulnerabilities in security configuration on your virtual machine scale sets should be remediated** is one of the policies.

8. If you change any settings, select the **Review + Save** tab, and then select **Save**.

> **Note**
> 
> All of the following policy categories that have a (*) in their title are on the Parameters tab. In some cases, there are several options in each category.

## Enable endpoint protection (*) - Level 1
Endpoint protection is recommended for all VMs.

## Enable disk encryption (*) - Level 1
Microsoft Defender for Cloud recommends that you use Azure Disk Encryption if you have Windows or Linux VM disks. Disk encryption lets you encrypt your Windows and Linux infrastructure as a service (IaaS) VM disks. Encryption is recommended for both the OS and the data volumes on your VM.

## Enable Network Security Groups (*) - Level 1
Microsoft Defender for Cloud recommends that you enable a network security group (NSG). NSGs contain a list of Access Control List (ACL) rules that allow or deny network traffic to your VM instances in a virtual network. NSGs can be associated either with subnets or with individual VM instances within that subnet. When an NSG is associated with a subnet, the ACL rules apply to all the VM instances in that subnet. In addition, traffic to an individual VM can be restricted further by associating an NSG directly with that VM.

## Enable a web application firewall (*) - Level 1
Microsoft Defender for Cloud might recommend that you add a web application firewall (WAF) from a Microsoft partner to secure your web applications.

## Enable vulnerability assessment (*) - Level 1
The vulnerability assessment in Microsoft Defender for Cloud is part of the Defender for Cloud VM recommendations. If Defender for Cloud doesn't find a vulnerability assessment solution installed on your VM, it recommends that you install one. A partner agent, after being deployed, starts reporting vulnerability data to the partner's management platform. In turn, the partner's management platform provides vulnerability and health monitoring data back to Defender for Cloud.

## Enable storage encryption (*) - Level 1
When storage encryption is enabled, any new data in Azure Blob Storage and Azure Files is encrypted.

## Enable JIT network access (*) - Level 1
Just-in-time (JIT) network access can be used to lock down inbound traffic to your Azure VMs. JIT network access reduces exposure to attacks while providing easy access to connect to VMs when needed.

## Enable adaptive application control (*) - Level 1
Adaptive application control is an intelligent, automated end-to-end approved application listing solution from Microsoft Defender for Cloud. It helps you control which applications can run on your Azure and non-Azure VMs (Windows and Linux), which, among other benefits, helps harden your VMs against malware. Defender for Cloud uses machine learning to analyze the applications running on your VMs. It helps you apply the specific approval rules by using adaptive application control intelligence. The capability greatly simplifies the process of configuring and maintaining approved application policies.

## Enable SQL auditing and threat detection (*) - Level 1
Microsoft Defender for Cloud recommends that you turn on auditing and threat detection for all databases on your servers that run Azure SQL. Auditing and threat detection can help you maintain regulatory compliance, understand database activity, and gain insight into discrepancies and anomalies that might alert you to business concerns or suspected security violations.

## Enable SQL encryption (*) - Level 1
Microsoft Defender for Cloud recommends that you enable Transparent Data Encryption (TDE) on SQL databases running in Azure. TDE protects your data and helps you meet compliance requirements by encrypting your database, associated backups, and transaction log files at rest. Enabling TDE doesn't require making changes to your applications.

## Set security contact email and phone number - Level 1

Microsoft Defender for Cloud recommends that you provide security contact details for your Azure subscription. Microsoft uses this information to contact you if the Microsoft Security Response Center finds that your customer data has been accessed by an unauthorized party. The Microsoft Security Response Center performs select security monitoring of the Azure network and infrastructure and receives threat intelligence and abuse complaints from third parties.

1. Sign in to the Azure portal. Search for and select **Cost Management + Billing**. Depending on your subscriptions, you'll either see the **Overview** pane or the **Billing scopes** pane.

2. If you see the **Overview** pane, continue to the next step.
   If you see the **Billing scopes** pane, select your subscription to go to the **Overview** pane.

3. In the **Overview** pane, in the left menu under **Settings**, select **Properties**.

4. Validate the contact information that appears. If you need to update the contact information, select the **Update sold to** link and enter the new information.

5. If you change any settings, select **Save**.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/microsoft-defender-for-cloud/update-contact-information.png)

## Enable Send me emails about alerts - Level 1

Microsoft Defender for Cloud recommends that you provide security contact details for your Azure subscription.

1. Sign in to the Azure portal. Search for and select **Microsoft Defender for Cloud**.

2. In the left menu under **Management**, select **Environment settings**.

3. Select the subscription.

4. In the left menu under **Settings**, select **Email notifications**.

5. In the **All users with the following roles** dropdown, select your role or, in **Additional email addresses (separated by commas)**, enter your email address.

6. Select the **Notify about alerts with the following severity** checkbox, select an alert severity, and then select **Save**.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/microsoft-defender-for-cloud/email-notifications-settings.png)

## Enable Send email also to subscription owners - Level 1

Microsoft Defender for Cloud recommends that you provide security contact details for your Azure subscription.

In the **Email notifications** pane described in the preceding section, you can add more email addresses separated by commas.

If you change any settings, in the menu bar, select **Save**.


# 3.5 Create an Azure storage accounts baseline

An Azure Storage account provides a unique namespace where you can store and access your Azure Storage data objects.

## Azure Storage account security recommendations

The following sections describe the Azure Storage recommendations that are in CIS Microsoft Azure Foundations Security Benchmark v. 3.0.0. Included with each recommendation are the basic steps to complete in the Azure portal. You should complete these steps for your own subscription and by using your own resources to validate each security recommendation. Keep in mind that Level 2 options might restrict some features or activity, so carefully consider which security options you decide to enforce.

## Require security-enhanced transfers - Level 1

This is a step you should take to ensure the security of your Azure Storage data is to encrypt the data between the client and Azure Storage. The first recommendation is to always use the HTTPS protocol. Using HTTPS ensures secure communication over the public internet. To enforce the use of HTTPS when you call REST APIs to access objects in storage accounts, turn on the **Secure transfer required** option for the storage account. After you turn on this control, connections that use HTTP are refused. Complete the following steps for each storage account in your subscription.

1. Sign in to the Azure portal. Search for and select **Storage accounts**.

2. In the **Storage accounts** pane, select a storage account.

3. In the left menu under **Settings**, select **Configuration**.

4. In the **Configuration** pane, ensure that **Secure transfer required** is set to **Enabled**.

5. If you change any settings, select **Save** in the menu bar.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/azure-storage-accounts/secure-transfer.png)

## Enable binary large object (blob) encryption - Level 1

Azure Blob Storage is the Microsoft object storage solution for the cloud. Blob Storage is optimized to store massive amounts of unstructured data. Unstructured data is data that doesn't adhere to a specific data model or definition. Examples of unstructured data include text and binary data. Storage service encryption protects your data at rest. Azure Storage encrypts your data as it's written in its datacenters, and it automatically decrypts it for you as you access it.

1. Sign in to the Azure portal. Search for and select **Storage accounts**.

2. In the **Storage accounts** pane, select a storage account.

3. In the left menu under **Security + networking**, select **Encryption**.

4. In the **Encryption** pane, note that Azure Storage encryption is enabled for all new and existing storage accounts and that it can't be disabled.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/azure-storage-accounts/encryption.png)

## Periodically regenerate access keys - Level 1

When you create a storage account in Azure, Azure generates two 512-bit storage access keys. These keys are used for authentication when the storage account is accessed. Rotating these keys periodically ensures that any inadvertent access to or exposure of these keys is limited by time. Complete the following steps for each storage account in your Azure subscription.

1. Sign in to the Azure portal. Search for and select **Storage accounts**.

2. In the **Storage accounts** pane, select a storage account.

3. In the left menu, select **Security + networking**, then select **Access keys**.

4. Review the **Last rotated** date for each key.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/azure-storage-accounts/activity-log-timespan.png)

5. If you aren't using Azure Key Vault with key rotation, you can select the **Rotate key** button to manually rotate your access keys.

## Require shared access signature tokens to expire within an hour - Level 1

A shared access signature is a URI that grants restricted access rights to Azure Storage resources. You can provide a shared access signature to clients that shouldn't be trusted with your storage account key, but to whom you want to delegate access to certain storage account resources. By distributing a shared access signature URI to these clients, you can grant them access to a resource for a specified period of time, with a specified set of permissions.

> **Note**
> 
> For the recommendations in CIS Microsoft Azure Foundations Security Benchmark v. 3.0.0, shared access signature token expiry times can't be automatically verified. The recommendation requires manual verification.

## Require shared access signature tokens to be shared only via HTTPS - Level 1

Shared access signature tokens should be allowed only over HTTPS protocol. Complete the following steps for each storage account in your Azure subscription.

1. Sign in to the Azure portal. Search for and select **Storage accounts**.

2. In the **Storage accounts** pane, select a storage account.

3. In the menu under **Security + networking**, select **Shared access signature**.

4. In the **Shared access signature** pane, under **Start and expiry date/time**, set the **Start** and **End** dates and times.

5. Under **Allowed protocols**, select **HTTPS only**.

6. If you change any settings, select the **Generate SAS and connection string** button at the bottom of the screen.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/azure-storage-accounts/shared-access-signature.png)

Configure shared access signature features in the next sections.

## Enable Azure Files encryption - Level 1

Azure Disk Encryption encrypts the OS and data disks in IaaS VMs. Client-side encryption and server-side encryption (SSE) are both used to encrypt data in Azure Storage. Complete the following steps for each storage account in your Azure subscription.

1. Sign in to the Azure portal. Search for and select **Storage accounts**.

2. In the **Storage accounts** pane, select a storage account.

3. In the left menu under **Security + networking**, select **Encryption**.

4. In the **Encryption** pane, note that Azure Storage encryption is enabled for all new and existing blob storage and file storage, and that it can't be disabled.

![Screenshot that shows encryption is automatically enabled for all blobs and files in storage accounts.](screenshot-placeholder)

## Require only private access to blob containers - Level 1

You can enable anonymous, public-read access to a container and its blobs in Azure Blob Storage. By turning on anonymous, public-read access, you can grant read-only access to these resources without sharing your account key, and without requiring a shared access signature. By default, a container and any blobs within it might be accessed only by a user that has been given appropriate permissions. To grant anonymous users read access to a container and its blobs, you can set the container access level to public.

However, if you grant public access to a container, anonymous users can read blobs within a publicly accessible container without the request being authorized. A security recommendation is to instead set access to storage containers to private. Complete the following steps for each storage account in your Azure subscription.

1. Sign in to the Azure portal. Search for and select **Storage accounts**.

2. In the **Storage accounts** pane, select a storage account.

3. In the left menu under **Data storage**, select **Containers**.

4. In the **Containers** pane, ensure that **Public access level** is set to **Private**.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/azure-storage-accounts/container-private-access-setting.png)



# 3.6 Create an Azure SQL Database baseline

Azure SQL Database is a cloud-based relational database family of products that support many of the same features offered in Microsoft SQL Server. Azure SQL Database provides an easy transition from an on-premises database to a cloud-based database that has built-in diagnostics, redundancy, security, and scalability.

## Azure SQL Database security recommendations

The following sections describe the Azure SQL Database recommendations that are in CIS Microsoft Azure Foundations Security Benchmark v. 3.0.0. Included with each recommendation are the basic steps to complete in the Azure portal. You should complete these steps for your own subscription and by using your own resources to validate each security recommendation.

## Enable auditing - Level 1

Auditing for Azure SQL Database and Azure Synapse Analytics tracks database events and writes them to an audit log in your Azure storage account, Azure Log Analytics workspace, or in Azure Event Hubs. Auditing also:

* Helps you maintain regulatory compliance, understand database activity, and gain insight into discrepancies and anomalies that might alert you to business concerns or suspected security violations.
* Enables and facilitates adherence to compliance standards, although it doesn't guarantee compliance.

To turn on auditing, complete the following steps for each database in your Azure subscription.

1. Sign in to the Azure portal. Search for and select **SQL databases**.

2. In the left menu under **Security**, select **Auditing**.

3. In the **Auditing** pane, enable **Enable Azure SQL Auditing**, and then select at least one audit log destination.

4. If you change any settings, select **Save** in the menu bar.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/azure-sql-database/auditing-enable.png)

For more information about auditing, see Auditing for Azure SQL Database and Azure Synapse Analytics.

## Enable SQL protections in Microsoft Defender for Cloud - Level 1

Microsoft Defender for Cloud detects anomalous activities that indicate unusual and potentially harmful attempts to access or exploit databases. Defender for Cloud can identify:

* Potential SQL injection.
* Access from an unusual location or datacenter.
* Access from an unfamiliar principal or from a potentially harmful application.
* Brute-force SQL credentials.

You can access and manage SQL threats in the Defender for Cloud menu.

1. Sign in to the Azure portal. Search for and select **Microsoft Defender for Cloud**.

2. In the left menu under **Management**, select **Environment settings**.

3. Select your subscription.

4. In the **Defender plans** pane, select **Select types** in the **Databases** row, then set **Azure SQL Databases** to **On**.

5. Select **Continue**.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/azure-sql-database/defender-for-cloud-plans-azure-sql-database.png)

6. Return to Azure **Home**. Search for and select **SQL databases**, then select the database you want to view.

7. For each database instance, in the left menu under **Security**, select **Microsoft Defender for Cloud**. View security recommendations, alerts, and vulnerability assessment findings for your SQL Database instance.

## Configure audit retention for more than 90 days - Level 1

Audit logs should be preserved for security and discovery, and to meet legal and regulatory compliance requirements. Complete the following steps for each Azure SQL Database instance in your Azure subscription.

1. Sign in to the Azure portal. Search for and select **SQL databases**, then select a database.

2. In the left menu under **Security**, select **Auditing**.

3. Select your **Audit log destination**, and then expand **Advanced properties**.

4. Ensure that **Retention (Days)** is *greater than 90 days*.

5. If you change any settings, select **Save** in the menu bar.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/azure-sql-database/auditing-retention.png)



# 3.7 Create a logging and monitoring baseline

Logging and monitoring are critical requirements when you try to identify, detect, and mitigate security threats. A proper logging policy can ensure that you can determine when a security violation has occurred. The policy also can potentially identify who is responsible. Azure activity logs provide data about external access to a resource, and they provide diagnostic logs, so you have information about the operation of a specific resource.

> **Note**
> 
> An Azure activity log is a subscription log that provides insight into subscription-level events that occurred in Azure. By using the activity log, you can determine the what, who, and when for any write operations that occurred on the resources in your subscription.

## Logging policy recommendations

The following sections describe the security recommendations in CIS Microsoft Azure Foundations Security Benchmark v. 3.0.0 to set logging and monitoring policies on your Azure subscriptions. Included with each recommendation are the basic steps to complete in the Azure portal. You should complete these steps for your own subscription and by using your own resources to validate each security recommendation. Keep in mind that Level 2 options might restrict some features or activity, so carefully consider which security options you decide to enforce.

## Ensure that a diagnostic setting exists - Level 1

The Azure activity log provides insight into subscription-level events that occurred in Azure. This log includes a range of data, from Azure Resource Manager operational data to updates on Azure Service Health events. The activity log previously was called an audit log or an operational log. The Administrative category reports control-plane events for your subscriptions.

Each Azure subscription has a single activity log. The log provides data about resource operations that originated outside Azure.

Diagnostic logs are emitted by a resource. Diagnostic logs provide information about the operation of the resource. You must enable diagnostic settings for each resource.

1. Sign in to the Azure portal. Search for and select **Monitor**.

2. In the left menu, select **Activity log**.

3. In the **Activity log** menu bar, select **Export activity logs**.

4. If no settings are shown, select your subscription, and then select **Add diagnostic setting**.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/azure-logging-monitoring/add-diagnostic-setting.png)

5. Enter a name for your diagnostic setting, and then select log categories and destination details.

6. In the menu bar, select **Save**.

Here's an example of how to create a diagnostic setting:

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/azure-logging-monitoring/configure-diagnostic-setting.png)

## Create an activity log alert for creating a policy assignment - Level 1

If you monitor policies that are created, you can see which users can create policies. The information might help you detect a breach or misconfiguration of your Azure resources or subscription.

1. Sign in to the Azure portal. Search for and select **Monitor**.

2. In the left menu, select **Alerts**.

3. In the **Alerts** menu bar, select the **Create** dropdown, and then select **Alert rule**.

4. In the **Create an alert rule** pane, select **Select scope**.

5. In the **Select a resource** pane, in the **Filter by resource type** dropdown, select **Policy assignment (policyAssignments)**.

6. Select a resource to monitor.

7. Select **Done**.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/azure-logging-monitoring/add-alert-resource.png)

8. To finish creating the alert, complete the steps that are described in Create an alert rule from the Azure Monitor Alerts pane.

## Create an activity log alert for creating, updating, or deleting a network security group - Level 1

By default, no monitoring alerts are created when NSGs are created, updated, or deleted. Changing or deleting a security group can allow internal resources to be accessed from improper sources or for unexpected outbound network traffic.

1. Sign in to the Azure portal. Search for and select **Monitor**.

2. In the left menu, select **Alerts**.

3. In the **Alerts** menu bar, select the **Create** dropdown, and then select **Alert rule**.

4. In the **Create an alert rule** pane, select **Select scope**.

5. In the **Select a resource** pane, in the **Filter by resource type** dropdown, select **Network security groups**.

6. Select **Done**.

7. To finish creating the alert, complete the steps that are described in Create an alert rule from the Azure Monitor Alerts pane.

## Create an activity log alert for creating or updating a SQL Server firewall rule - Level 1

Monitoring for events that create or update a SQL Server firewall rule provides insight into network access changes, and it might reduce the time it takes to detect suspicious activity.

1. Sign in to the Azure portal. Search for and select **Monitor**.

2. In the left menu, select **Alerts**.

3. In the **Alerts** menu bar, select the **Create** dropdown, and then select **Alert rule**.

4. In the **Create alert rule** pane, select **Select scope**.

5. In the **Select a resource** pane, in the **Filter by resource type** dropdown, select **SQL servers**.

6. Select **Done**.

7. To finish creating the alert, complete the steps that are described in Create an alert rule from the Azure Monitor Alerts pane.




# 8 Create a Networking baseline

By design, Azure networking services maximize flexibility, availability, resiliency, security, and integrity. Network connectivity is possible between resources that are located in Azure, between on-premises and Azure-hosted resources, and to and from the internet and Azure.

## Azure networking security recommendations

The following sections describe the Azure networking recommendations that are in CIS Microsoft Azure Foundations Security Benchmark v. 3.0.0. Included with each recommendation are the basic steps to complete in the Azure portal. You should complete these steps for your own subscription and by using your own resources to validate each security recommendation. Keep in mind that Level 2 options might restrict some features or activity, so carefully consider which security options you decide to enforce.

## Restrict RDP and SSH access from the internet - Level 1

You can reach Azure VMs by using Remote Desktop Protocol (RDP) and the Secure Shell (SSH) protocol. You can use these protocols to manage VMs from remote locations. The protocols are standard in datacenter computing.

The potential security problem with using RDP and SSH over the internet is that attackers can use brute-force techniques to gain access to Azure VMs. After the attackers gain access, they can use your VM as a launching pad to compromise other machines on your virtual network, or even attack networked devices outside Azure.

We recommended that you disable direct RDP and SSH access from the internet for your Azure VMs. Complete the following steps for each VM in your Azure subscription.

1. Sign in to the Azure portal. Search for and select **Virtual machines**.

2. Select a virtual machine.

3. In the left menu under **Networking**, select **Network settings**.

4. Verify that the **Inbound port rules** section doesn't have a rule for RDP, for example: port=3389, protocol = TCP, Source = Any or Internet. You can use the **Delete** icon to remove the rule.

5. Verify that the **Inbound port rules** section doesn't have a rule for SSH, for example: port=22, protocol = TCP, Source = Any or Internet. You can use the **Delete** icon to remove the rule.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/azure-networking/rdp.png)

When direct RDP and SSH access from the internet are disabled, you have other options that you can use to access these VMs for remote management:

- Point-to-site VPN
- Site-to-site VPN
- Azure ExpressRoute
- Azure Bastion Host

## Restrict SQL Server access from the internet - Level 1

Firewall systems help prevent unauthorized access to computer resources. If a firewall is turned on but isn't correctly configured, attempts to connect to SQL Server might be blocked.

To access an instance of SQL Server through a firewall, you must configure the firewall on the computer that's running SQL Server. Allowing ingress for the IP range 0.0.0.0/0 (Start IP of 0.0.0.0 and End IP of 0.0.0.0) allows open access to any and all traffic, potentially making the SQL Server database vulnerable to attacks. Ensure that no SQL Server databases allow ingress from the internet. Complete the following steps for each SQL Server instance.

1. Sign in to the Azure portal. Search for and select **SQL servers**.

2. In the menu pane under **Security**, select **Networking**.

3. In the **Networking** pane, on the **Public access** tab, ensure that a firewall rule exists. Ensure that no rule has a Start IP of **0.0.0.0** and End IP of **0.0.0.0** or another combination that allows access to wider public IP ranges.

4. If you change any settings, select **Save**.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/azure-networking/firewall.png)

## Enable Network Watcher - Level 1

NSG flow logs are an Azure Network Watcher feature that gives you information about IP ingress and egress traffic through an NSG. Flow logs are written in JSON format and show:

- Outbound and inbound flows on a per-rule basis.
- The network interface (NIC) the flow applies to.
- 5-tuple information about the flow: source and destination IP addresses, source and destination ports, and the protocol that was used.
- Whether the traffic was allowed or denied.
- In version 2, throughput information like bytes and packets.

1. Sign in to the Azure portal. Search for and select **Network Watcher**.

2. Select **Network Watcher** for your subscription and location.

3. If no NSG flow logs exist for your subscription, create an NSG flow log.

## Set NSG flow log retention period to more than 90 days - Level 2

When you create or update a virtual network in your subscription, Network Watcher is automatically enabled in your virtual network's region. Your resources aren't affected and no charge is assessed when Network Watcher is automatically enabled.

You can use NSG flow logs to check for anomalies and to gain insight into suspected breaches.

1. Sign in to the Azure portal. Search for and select **Network Watcher**.

2. In the left menu under **Logs**, select **NSG flow logs**.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/azure-networking/nsg-flow.png)

3. Select an NSG flow log.

4. Ensure that **Retention (days)** is greater than **90 days**.

5. If you change any settings, select **Save** in the menu bar.



# 3.9 Create an Azure VM baseline

Azure Policy is an Azure service you can use to create, assign, and manage policies. The policies you create enforce different rules and effects over your resources so that those resources stay compliant with your corporate standards and service-level agreements. Azure Policy meets this need by evaluating your resources for noncompliance with assigned policies. For example, you can have a policy to allow only a certain SKU size of VM in your environment. After this policy is implemented, new and existing resources are evaluated for compliance. With the right type of policy, you can bring existing resources into compliance.

## Azure VM security recommendations

The following sections describe the Azure VM security recommendations that are in CIS Microsoft Azure Foundations Security Benchmark v. 3.0.0. Included with each recommendation are the basic steps to complete in the Azure portal. You should complete these steps for your own subscription and by using your own resources to validate each security recommendation. Keep in mind that Level 2 options might restrict some features or activity, so carefully consider which security options you decide to enforce.

## Ensure that OS disks are encrypted - Level 1

Azure Disk Encryption helps protect and safeguard your data to meet your organization's security and compliance commitments. Azure Disk Encryption:

- Uses the BitLocker feature of Windows and the DM-Crypt feature of Linux to provide volume encryption for the OS and data disks of Azure VMs.
- Integrates with Azure Key Vault to help you control and manage disk encryption keys and secrets.
- Ensures that all data on the VM disks is encrypted at rest when it is in Azure storage.

Azure Disk Encryption for Windows and Linux VMs is in General Availability in all Azure public regions and Azure Government regions for Standard VMs and VMs with Azure Premium Storage.

If you use Microsoft Defender for Cloud (recommended), you're alerted if you have VMs that aren't encrypted. Complete the following steps for each VM in your Azure subscription.

1. Sign in to the Azure portal. Search for and select **Virtual machines**.

2. Select a virtual machine.

3. In the left menu under **Settings**, select **Disks**.

4. Under **OS disk**, ensure that the OS disk has an encryption type set.

5. Under **Data disks**, ensure that each disk has an encryption type set.

6. If you change any settings, select **Save** in the menu bar.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/azure-virtual-machines/disk-encryption.png)

## Ensure that only approved VM extensions are installed - Level 1

Azure VM extensions are small applications that provide post-deployment configuration and automation tasks on Azure VMs. For example, if a VM requires software installation or antivirus protection or if the VM needs to run a script, you can use a VM extension. You can run an Azure VM extension by using the Azure CLI, PowerShell, an Azure Resource Manager template, or the Azure portal. You can bundle extensions with a new VM deployment or run them against any existing system. To use the Azure portal to ensure that only approved extensions are installed on your VMs, complete the following steps for each VM in your Azure subscription.

1. Sign in to the Azure portal. Search for and select **Virtual machines**.

2. Select a virtual machine.

3. In the left menu under **Settings**, select **Extensions + applications**.

4. In the **Extensions + applications** pane, ensure that the extensions that are listed are approved for use.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/azure-virtual-machines/extensions.png)

## Ensure that the OS patches for the VMs are applied - Level 1

Microsoft Defender for Cloud monitors Windows and Linux VMs and computers daily for missing operating system updates. Defender for Cloud retrieves a list of available security and critical updates from Windows Update or Windows Server Update Services (WSUS). The updates you receive depend on which service you configure on the Windows computer. Defender for Cloud also checks for the latest updates in Linux systems. If your VM or computer is missing a system update, Defender for Cloud recommends that you apply system updates.

1. Sign in to the Azure portal. Search for and select **Microsoft Defender for Cloud**.

2. In the left menu under **General**, select **Recommendations**.

3. In **Recommendations**, ensure that there are no recommendations for **Apply system updates**.

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/azure-virtual-machines/defender-for-cloud-recommend.png)

## Ensure that VMs have an endpoint protection solution installed and running - Level 1

Microsoft Defender for Cloud monitors the status of antimalware protection. It reports this status in the **Endpoint protection issues** pane. Defender for Cloud highlights issues like detected threats and insufficient protection, which can make your VMs and computers vulnerable to antimalware threats. By using the information in **Endpoint protection issues**, you can begin to create a plan to address any issues that are identified.

Use the same process as described in the preceding recommendation.



# 3.10 Other baseline security considerations

You should follow a few more security recommendations to set general security and operational controls on your Azure subscription.

## More security recommendations

The following sections describe additional recommendations that are in CIS Microsoft Azure Foundations Security Benchmark v. 3.0.0. Included with each recommendation are the basic steps to complete in the Azure portal. You should complete these steps for your own subscription and by using your own resources to validate each security recommendation. Keep in mind that Level 2 options might restrict some features or activity, so carefully consider which security options you decide to enforce.

## Set an expiration date on all keys in Azure Key Vault - Level 1

In addition to the key, the following attributes might be specified for a key in Azure Key Vault. In a JSON request, an attribute's keyword and braces { } are required, even if no attribute is specified. For example, for the optional IntDate attribute, the default value is forever. The exp (expiration time) attribute identifies the expiration time at or after which the key must not be used for a cryptographic operation, except for certain operation types under specific conditions. Processing the exp attribute requires that the current date and time are before the expiration date and time set in the exp value.

We recommend that you rotate your keys in your key vault and set an explicit expiry time for each key. This process ensures that keys can't be used beyond their assigned lifetimes. Key Vault stores and manages secrets as sequences of 8-bit bytes called octets, with a maximum size of 25 KB each for each key. For highly sensitive data, clients should consider more layers of protection for data. One example is to encrypt data by using a separate protection key prior to storage in Key Vault. Complete the following steps for all keys in each of your key vaults.

1. Sign in to the Azure portal. Search for and select **Key vaults**.

2. Select a key vault.

3. In the left menu under **Objects**, select **Keys**.

4. In the **Keys** pane for the key vault, ensure that each key in the vault has **Expiration date** set as appropriate.

5. If you change any settings, select **Save** in the menu bar.

## Set an expiration date on all secrets in Azure Key Vault - Level 1

Securely store and tightly control access to tokens, passwords, certificates, API keys, and other secrets. Ensure that an expiration time is set for all secrets in Azure Key Vault. Complete the following steps for all secrets in each of your key vaults.

1. Sign in to the Azure portal. Search for and select **Key vaults**.

2. In the left menu under **Objects**, select **Secrets**.

3. In the **Secrets** pane for the key vault, ensure that each secret in the vault has **Expiration date** set as appropriate.

The following screenshot illustrates setting an expiration date on a password:

![](https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/other-security-considerations/key-vault-set-secret-expiration-date.png)

4. If you change any settings, select **Save** in the menu bar.

## Set resource locks for mission-critical Azure resources - Level 2

As an administrator, you might need to lock a subscription, resource group, or resource to prevent other users from accidentally deleting or modifying a critical resource. In the Azure portal, the lock levels are **Read-only** and **Delete**. Unlike role-based access control, you use management locks to apply a restriction to all users and roles. Azure Resource Manager locks apply only to operations that happen in the management plane, which consists of operations sent to https://management.azure.com. The locks don't restrict how resources perform their own functions. Resource changes are restricted, but resource operations aren't restricted.

> **Tip**
> 
> For example, a Read-only lock on an instance of Azure SQL Database prevents you from deleting or modifying the database. It doesn't prevent you from creating, updating, or deleting data in the database. Data transactions are permitted because those operations aren't sent to https://management.azure.com.

Complete the following steps for all mission-critical resources in your Azure subscription.

1. Sign in to the Azure portal. Search for and select **All resources**.

2. Select a resource, resource group, or subscription that you want to lock.

3. In the menu under **Settings**, select **Locks**.

4. In the **Locks** pane, in the menu bar, select **Add**.

5. In the **Add lock** pane, enter a name for the lock and select a lock level. Optionally, you can add notes that describe the lock.

6. Select **OK**.

![https://learn.microsoft.com/en-us/training/modules/create-security-baselines/media/other-security-considerations/lock-resource.png]



# 3.11 Summary

We've covered many things in this module to create a baseline security checklist for commonly used Azure services. Let's quickly recap what we've gone through:

* **Turn on Microsoft Defender for Cloud - it's free**. Upgrade your Azure subscription to turn on Microsoft Defender for Cloud. Defender for Cloud's enhanced security features help you:
   * Find and fix security vulnerabilities.
   * Apply access and application controls to block malicious activity.
   * Detect threats by using analytics and intelligence.
   * Respond quickly when under attack.
* **Adopt Center for Internet Security (CIS) Benchmarks**. Apply the benchmarks to existing tenants.
* **Use CIS VMs for new workloads**. Get CIS hardened VM images in Azure Marketplace.
* **Store your keys and secrets in Azure Key Vault** (not in your source code). Key Vault is designed to support any type of secret, including passwords, database credentials, API keys, and certificates.
* **Install a web application firewall**. A web application firewall (WAF) is a feature of Azure Application Gateway that provides centralized protection of your web applications from common exploits and vulnerabilities. Third parties also offered Azure-supported WAFs.
* **Enforce multifactor verification for users, especially for your administrator accounts**. Multifactor authentication for Microsoft Entra users helps administrators protect their organizations and users by requiring more than one authentication method.
* **Encrypt your virtual hard disk files**. Encryption helps protect your boot volume and data volumes at rest in storage, along with your encryption keys and secrets.
* **Connect Azure VMs and appliances to other networked devices by placing them in Azure virtual networks**. VMs that are connected to an Azure virtual network can connect to devices that are on the same virtual network, on different virtual networks, on the internet, or on your own on-premises networks.

## Strong operational security practices to implement

Implement these strong operational security practices every day:

* **Manage your VM updates**. Azure VMs, like all on-premises VMs, are meant to be user-managed. Azure doesn't push Windows updates to these VMs. Ensure that you have solid processes in place for important operations like patch management and backup.
* **Enable password management**. Use appropriate security policies to prevent abuse.
* **Review your workload protection dashboard regularly**. Get a central view of the security state of all of your Azure resources, and take action on the recommendations regularly.

## Further reading

To explore the topics presented in this module in more detail, see CIS Microsoft Azure Foundations Security Benchmark.



# 5 Control access to your APIs with Azure API Management

Discover how to protect your APIs from unauthorized use with API keys and client certificate authentication.

# 5.1 Introduction

Azure API Management allows you to carefully identify and control who can access the data published by your APIs.

Suppose you work for a meteorological company, which has an API that customers use to access weather data for forecasts and research. There's proprietary information in this data, and you'd like to ensure that only paying customers have access. You want to use **Azure API Management** to properly secure this API from unauthorized use.

In this module, you'll use two basic methods to secure access to an API in Azure API Management:

- Subscriptions
- Client certificates

By the end of this module, you'll be able to ensure that only people with the right credentials can access the information in your API. You'll also be ready to explore more advanced options to secure access to an API.

## Learning objectives

In this module, you will:

- Create an Azure API gateway.
- Import a RESTful API into the gateway.
- Implement policies to secure the API from unauthorized use.
- Call an API to test the applied policies.

## Prerequisites

- Familiarity with basic concepts of web APIs, such as operations and endpoints
- Familiarity with certificates
- You need an Azure subscription to complete the exercises. If you don't have an Azure subscription, create a free account and add a subscription before you begin. If you're a student, you can take advantage of the Azure for students offer.



# 5.2 What is API Management?

Azure API Management helps organizations unlock the potential of their data and services by publishing APIs to external partners and internal developers. Businesses are extending their operations as a digital platform by creating new channels, finding new customers, and driving deeper engagement with existing ones. API Management provides the core competencies to ensure a successful API program through developer engagement, business insights, analytics, security, and protection. You can use API Management to take any backend and launch a full-fledged API program based on it.

To use API Management, administrators define *APIs* in the portal. Each API consists of one or more operations and can be added to one or more products. To use an API, developers subscribe to a product that contains that API, then call the API's operations, subject to any usage policies that might be in effect. Common scenarios include:

- Securing mobile infrastructure by gating access with API keys, preventing distributed denial of service (DDoS) attacks by using throttling, or using advanced security policies like JSON web token (JWT) validation.
- Offering fast partner onboarding through the developer portal to independent software vendor (ISV) partner ecosystems, enabling them to build an API facade to decouple from internal implementations that aren't ready for partner consumption.
- Running an internal API program that offers a centralized location for the organization to communicate between the API gateway and the backend. Communications about the availability and latest changes to APIs would be on a secured channel with gated access based on organizational accounts.

## Components of API Management

API Management is made up of the following components:

**API gateway**

The API gateway is the endpoint that:

- Accepts API calls and routes them to the backend.
- Verifies API keys, JWT tokens, certificates, and other credentials.
- Enforces usage quotas and rate limits.
- Transforms your API on the fly without code modifications.
- Caches backend responses, where the capability is set up.
- Logs call metadata for analytics purposes.

**Azure portal**

The Azure portal is the administrative interface where you set up your API program. You can also use it to:

- Define or import API schema.
- Package APIs into products.
- Set up policies such as quotas or transformations on the APIs.
- Get insights from analytics.
- Manage users.

**Developer portal**

The developer portal serves as the main web presence for developers. From here, they can:

- Read API documentation.
- Try out an API via the interactive console.
- Create an account and subscribe to get API keys.
- Access analytics on their own usage.


# 5.3 Create subscriptions in Azure API Management

When you publish an API with API Management, you define who can access the API through the gateway.

For your meteorological app, you want to ensure that only customers who are subscribed to your service can access the API and use your forecast data. You accomplish this access control by issuing subscription keys.

> **Important**
> 
> Subscriptions in this context are not related to Azure subscriptions used for managing your Azure account.

Here, you'll learn how to use subscription keys to secure your APIs.

## Subscriptions and keys

You can choose to make your APIs and the information they contain freely available. But usually, you want to restrict access to users who have paid or organizations with which you have a working relationship. One way to control access to your APIs is by using subscriptions. Subscriptions are used to segment user access to an API.

Subscription keys form the authorization to enable access to these subscriptions. Whenever a client makes a request to a protected API, a valid subscription key must be included in the HTTP request; otherwise, the call will be rejected.

A subscription key is a unique, autogenerated key that can be passed as part of an API call. The key is directly related to a subscription, which can be scoped to different areas. Subscriptions give you granular control over permissions and policies.

The three main subscription scopes are:

| Scope | Details |
|-------|---------|
| All APIs | Applies to every API accessible from the gateway. |
| Single API | Applies to a single imported API and all of its endpoints. |
| Product | A product is a collection of one or more APIs that you configure in API Management. You can assign APIs to more than one product. Products can have different access rules, usage quotas, and terms of use. So, if you want your partners and suppliers to have different access rights to your WeatherData API, assign the API to a product, and then use the Azure portal to associate APIs with a product. |

Applications that call a protected API must include a subscription key in every request.

You can regenerate these subscription keys at any time; for example, if you suspect that a key has been shared with unauthorized users, you can create a new one.

*Screenshot of subscription keys in the Azure portal.*

![](https://learn.microsoft.com/en-us/training/modules/control-authentication-with-apim/media/2-subscription-keys.png)

Every subscription has two keys: a primary key and a secondary key. Having two keys makes it easier when you do need to regenerate a key. For example, if you want to change the primary key and avoid downtime, use the secondary key in your apps.

For products in which subscriptions are enabled, clients must supply a key when making calls to APIs in that product. Developers can obtain a key by submitting a subscription request. If you approve the request, you must send them the subscription key securely; for example, in an encrypted message. This step is a core part of the API Management workflow.

## Call an API with the subscription key

Applications must include a valid key in all HTTP requests that make calls to API endpoints that are protected by a subscription. Keys can be passed in the request header or as a query string parameter in the URL.

The default subscription key header name is `Ocp-Apim-Subscription-Key`, and the default query string name is `subscription-key`.

To test out your API calls, you can use a test console in the Azure portal, or the developer portal, or command-line tools such as curl. Here's an example of a GET request using the developer portal, which shows the subscription key header:

*Screenshot that shows how to call your API from developer portal.*

![](https://learn.microsoft.com/en-us/training/modules/control-authentication-with-apim/media/2-key-header-portal.png)

Here's an example of how you'd pass a key in a request header using curl:

```bash
curl --header "Ocp-Apim-Subscription-Key: <key string>" https://<apim gateway>.azure-api.net/api/path
```

Here's an example of how you'd use a curl command to pass a key as a query string in a URL:

```bash
curl https://<apim gateway>.azure-api.net/api/path?subscription-key=<key string>
```

If a required key isn't passed in the header, or as a query string in the URL, you'll get a 401 Access Denied response from the API gateway.


# 5.4 Exercise - Create subscriptions in Azure API Management

You can use the Azure API Management user interface in the Azure portal to create subscriptions and obtain subscription keys for use in client apps.

Suppose your weather company decided to make its meteorological data available to clients who subscribe and pay for this service. The critical requirement is to only allow access to clients who are allocated a key. As lead developer, you need to create an API gateway. You'll use the gateway to publish a RESTful Weather API that exposes an OpenAPI endpoint. You'll then secure the endpoint and allocate a client key.

In this unit, you'll:

- Publish a RESTful Weather API.
- Deploy an API Management gateway.
- Expose the Weather API through the gateway endpoint.
- Restrict access based on a subscription key.

> **Important**
> 
> You need your own Azure subscription to run this exercise, and you might incur charges. If you don't already have an Azure subscription, create a free account before you begin.

## Deploy the Weather Web API

You've developed a .NET Core app that returns weather information. The app includes Swashbuckle to generate OpenAPI documentation.

To save time, let's start by running a script to host our API in Azure. The script performs the following steps:

- Create an Azure App Service plan in the free tier
- Create a Web API within an Azure App Service, configured for Git deployment from a local repo
- Set account-level deployment credentials for our app
- Configure Git locally
- Deploy our Web API to our App Service instance

1. Sign in to the Azure portal.

2. In the Azure taskbar, select the Cloud Shell icon to open Azure Cloud Shell.

   *Screenshot of Cloud Shell icon in taskbar.*

3. Run the following git clone command in Azure Cloud Shell to clone the repo that contains the source for our app, and our setup script from GitHub.

   ```bash
   git clone https://github.com/MicrosoftDocs/mslearn-control-authentication-with-apim.git
   ```

4. Go to the repo folder directory locally by running the following cd command.

   ```bash
   cd mslearn-control-authentication-with-apim
   ```

5. As its name suggests, setup.sh is the script you'll run to create our API. It will generate a public web app that exposes an OpenAPI interface.

   ```bash
   bash setup.sh
   ```

   The script has seven parts and takes about a minute to run. Observe that, during deployment, all dependencies needed for our app to run are automatically installed on the remote App Service.

6. When the script has finished, it outputs two URLS: a Swagger URL and an Example URL. You can use these URLs to test the app deployment.

7. To test that our app deployed correctly, copy and paste the Swagger URL from Azure Cloud Shell output into your favorite browser. The browser should display the Swagger UI for our app and declare the following RESTful endpoints:

   - `api/weather/{latitude}/{longitude}`, which returns meteorological data for the current day given the specified latitude and longitude (double values).
   - `api/weather/{date}/{latitude}/{longitude}`, which returns meteorological data for the specified day (date value) at the specified latitude and longitude (double values).

   *Screenshot of the app Swagger view.*

![](https://learn.microsoft.com/en-us/training/modules/control-authentication-with-apim/media/3-swagger.png)

8. Finally, copy and save the Example URL from Azure Cloud Shell output. This location is the Swagger JSON URL. You'll need it later in this exercise.

## Deploy an API gateway

The next step in this exercise is to create an API gateway in the Azure portal. In the next exercise, you'll use this gateway to publish your API.

1. Sign into the Azure portal.

2. On the Azure resource menu or from the Home page, under Azure services, select **Create a resource**. The Create a resource pane appears.

3. In the resource menu, search for and select **API Management**. Select **Create**. The Install API Management gateway pane appears.

4. On the **Basics** tab, enter the following values for each setting.

   | Setting | Value |
   |---------|-------|
   | **Project details** | |
   | Subscription | Select your subscription. |
   | Resource group | Select a new or existing resource group. A resource group is a logical container that holds related resources for an Azure solution. |
   | **Instance details** | |
   | Region | Select an available region. |
   | Resource name | Enter `apim-WeatherDataXXXX`; replace the XXXX with a random number to ensure that the name is globally unique. Make a note of this resource name; it will be the API gateway name that you'll need it later in this exercise. |
   | Organization name | Enter `Weather-Company`. |
   | Administrator email | The email address to receive all system notifications. |
   | **Pricing tier** | |
   | Pricing tier | From the dropdown list, select **Consumption**. |

5. Select **Review + create**, and after validation passes, select **Create**.

   > **Note**
   > 
   > The Consumption tier provides fast deployment for testing and has a pay-for-use pricing model. The overall API management experience is similar to the other pricing tiers.

6. You can view the progress of the deployment, along with the resources that are being created.

## Import the API

After deployment has completed, import the Weather API into the API Management gateway by using the following procedure.

1. Select **Go to resource**. The Overview pane of the API Management service for your resource appears.

2. In the left menu pane, under **APIs**, select **APIs**. The APIs pane for your API Management service appears, with template selections for creating/displaying an API.

3. Under **Create from definition**, select **OpenAPI**. The Create from OpenAPI specification dialog box appears.

4. In the **OpenAPI specification** field, paste the Swagger JSON URL that you saved earlier in the exercise. When you press Enter or select a different area of the dialog box, other fields will be populated for you. This data is imported from the OpenAPI specification that Swagger created.

5. Accept the defaults for all the other settings, and then select **Create**.

   *Screenshot of dialog box with swagger.json url highlighted.*

![](https://learn.microsoft.com/en-us/training/modules/control-authentication-with-apim/media/3-import-the-api.png)

6. The **Design** tab of the Weather Data API displays all operations, which consists of two GET operations.

## Add a subscription key to access the Weather API

The final step is to add a subscription key for the Weather Data API.

1. In the left menu pane, under **APIs**, select **Subscriptions**. The Subscriptions pane for your API Management service appears.

2. On the top menu bar, select **Add subscription**. The New subscription pane appears.

![](https://learn.microsoft.com/en-us/training/modules/control-authentication-with-apim/media/3-cloud-shell-icon.png)
  
   *Screenshot showing how to add a new subscription.*

3. Enter the following values for each setting.

   | Setting | Value |
   |---------|-------|
   | Name | `weather-data-subscription` |
   | Display name | `Weather Data Subscription` |
   | Allow tracing | No checkmark |
   | Scope | From the dropdown list, select **API**. |
   | API | From the dropdown list, select **Weather Data**. |

4. Select **Create**. The Subscriptions pane lists two subscriptions, Built-in all-access subscription and your Weather Data Subscription.

5. At the end of the Weather Data Subscription row, select the ellipsis, and in the context menu select **Show/hide keys**. The Primary and Secondary key values show.

6. Copy the Primary key from Weather Data Subscription to your clipboard and save it in something like Notepad. You'll need this key in the next step.



## Test the subscription key

The API is secured with a key. Now, we'll test the API without and with the key to demonstrate secure access.

1. Make a request without passing a subscription key. In Azure Cloud Shell, run the following cURL command. Substitute the `[Name Of Gateway]` placeholder with the resource name for the API gateway (`apim-WeatherDataNNNN`) that you created in the previous task.

   ```bash
   curl -X GET https://[Name Of Gateway].azure-api.net/api/Weather/53/-1
   ```

   This command has no subscription key and should return a 401 Access Denied error, similar to the following.

   ```json
   { "statusCode": 401, "message": "Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API." }
   ```

2. Now, run the following command. Substitute the `Name Of Gateway` placeholder with the resource name for the API gateway (`apim-WeatherDataNNNN`). Also, substitute the `Primary Key` placeholder with the primary key you copied from the show/hide step.

   ```bash
   curl -X GET https://[Name Of Gateway].azure-api.net/api/Weather/53/-1 \
     -H 'Ocp-Apim-Subscription-Key: [Primary Key]'
   ```

   If you included the closing quote, this command should result in a successful response similar to the following code.

   ```json
   {"mainOutlook":{"temperature":32,"humidity":34},"wind":{"speed":11,"direction":239.0},"date":"2019-05-16T00:00:00+00:00","latitude":53.0,"longitude":-1.0}
   ```

# 5.5 Use client certificates to secure access to an API

Certificates can be used to provide TLS mutual authentication between the client and the API gateway. You can configure the API Management gateway to allow only requests with certificates containing a specific thumbprint. The authorization at the gateway level is handled through inbound policies.

For your meteorological app, you have some customers who have client certificates issued by a certificate authority (CA) that you both trust. You want to allow those customers to authenticate by passing those certificates.

Here, you'll learn how to configure API Management to accept client certificates.

## TLS client authentication

With TLS client authentication, the API Management gateway can inspect the certificate contained within the client request and check for properties like:

| Property | Reason |
|----------|--------|
| Certificate Authority (CA) | Only allow certificates signed by a particular CA. |
| Thumbprint | Allow certificates containing a specified thumbprint. |
| Subject | Only allow certificates with a specified subject. |
| Expiration Date | Only allow certificates that haven't expired. |

These properties aren't mutually exclusive, and you can combine them to form your own policy requirements. For example, you can specify that the certificate passed in the request hasn't expired, and has been signed by a particular certificate authority.

Client certificates are signed to ensure that they aren't tampered with. When a partner sends you a certificate, verify that it comes from them and not an imposter. There are two common ways to verify a certificate:

- Check who issued the certificate. If the issuer was a certificate authority that you trust, you can use the certificate. You can configure the trusted certificate authorities in the Azure portal to automate this process.

- If the certificate is issued by a partner, verify that it came from them. For example, if they deliver the certificate in person, you can be sure of its authenticity. These certificates are known as self-signed certificates.

## Accept client certificates in the Consumption tier

The Consumption tier in API Management is designed to conform with serverless design principles. If you build your APIs from serverless technologies, such as Azure Functions, this tier is a good fit. In the Consumption tier, you must explicitly enable the use of client certificates, which you can do on the Custom domains pane. This step isn't necessary in other tiers.

*Screenshot showing configuring the gateway to request certificates.*

![](https://learn.microsoft.com/en-us/training/modules/control-authentication-with-apim/media/5-config-request-certificates.png)

## Create certificate authorization policies

Create these policies in the inbound processing policy file within the API Management gateway.

*Screenshot showing the inbound processing policy button.*

![](https://learn.microsoft.com/en-us/training/modules/control-authentication-with-apim/media/5-inbound-policy.png)


### Check the thumbprint of a client certificate

Every client certificate includes a thumbprint, which is a hash calculated from other certificate properties. The thumbprint ensures that the values in the certificate haven't been altered since the certificate was issued by the certificate authority. You can check the thumbprint in your policy. The following example checks the thumbprint of the certificate passed in the request.

```xml
<choose>
    <when condition="@(context.Request.Certificate == null || context.Request.Certificate.Thumbprint != "desired-thumbprint")" >
        <return-response>
            <set-status code="403" reason="Invalid client certificate" />
        </return-response>
    </when>
</choose>
```

### Check the thumbprint against certificates uploaded to API Management

In the previous example, only one thumbprint would work, so only one certificate would be validated. Usually, each customer or partner company would pass a different certificate with a different thumbprint. To support this scenario, obtain the certificates from your partners, and use the Client certificates pane in the Azure portal to upload them to the API Management resource. Then, add this code to your policy.

```xml
<choose>
    <when condition="@(context.Request.Certificate == null || !context.Request.Certificate.Verify()  || !context.Deployment.Certificates.Any(c => c.Value.Thumbprint == context.Request.Certificate.Thumbprint))" >
        <return-response>
            <set-status code="403" reason="Invalid client certificate" />
        </return-response>
    </when>
</choose>
```

### Check the issuer and subject of a client certificate

The following example checks the issuer and subject of the certificate passed in the request.

```xml
<choose>
    <when condition="@(context.Request.Certificate == null || context.Request.Certificate.Issuer != "trusted-issuer" || context.Request.Certificate.SubjectName.Name != "expected-subject-name")" >
        <return-response>
            <set-status code="403" reason="Invalid client certificate" />
        </return-response>
    </when>
</choose>
```



# 5.6 Exercise - Use client certificates to secure access to an API

You configure API Management to accept client certificates by using inbound policies.

Suppose your weather company has decided to secure its API through certificate authentication for certain clients who already use certificate authentication in other systems. This setup will allow those clients to use existing certificates to authenticate themselves against the API Management gateway.

In this exercise, you'll:

- Create a self-signed certificate.
- Configure the gateway to request client certificates.
- Get the thumbprint for the certificate.
- Edit the inbound policy to allow only clients with the specified certificate in their request.
- Call the API Management gateway and pass the certificate by using curl.

> **Note**
> 
> This exercise uses the resources that you set up in the previous exercise.

## Create self-signed certificate

First, use Cloud Shell to create a self-signed certificate, which you'll then use for authentication between the client and the API Management gateway.

1. To create the private key and the certificate, run the following commands in Cloud Shell.

   ```bash
   pwd='<Enter a secure password here>'
   pfxFilePath='selfsigncert.pfx'
   openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout privateKey.key -out selfsigncert.crt -subj /CN=localhost
   ```

   To make this example easy to follow, the preceding commands include the password used to secure the private key. Whenever you generate a private key for your own use, make sure you generate a secure password and control access to it appropriately.

2. Now, convert the certificate to PEM format, which the curl tool can use, by running these commands:

   ```bash
   openssl pkcs12 -export -out $pfxFilePath -inkey privateKey.key -in selfsigncert.crt -password pass:$pwd
   openssl pkcs12 -in selfsigncert.pfx -out selfsigncert.pem -nodes
   ```

   When you're prompted, enter your secure password, and then press Enter.

## Configure the gateway to request client certificates

Because you're using the Consumption tier for API Management, you must configure the gateway to accept client certificates. Follow these steps.

1. From the Azure portal that is already open, select your API Management service (`apim-WeatherDataNNNN`).

2. In the left menu pane, under **Deployment and infrastructure**, select **Custom domains**. The Custom domains pane for your API Management service appears.

3. For **Request client certificate**, select **Yes**, and on the top menu bar, select **Save**.

   *Screenshot of configuring the gateway to request certificates.*

![](https://learn.microsoft.com/en-us/training/modules/control-authentication-with-apim/media/5-config-request-certificates.png)

## Get the thumbprint for the certificate

In this section, you'll configure API Management to accept a request only if it has a certificate with a certain thumbprint (fingerprint). Let's get that thumbprint from the certificate.

> **Note**
> 
> An SSL certificate thumbprint is also known as an SSL certificate fingerprint.

1. In Cloud Shell, run the following code.

   ```bash
   Fingerprint="$(openssl x509 -in selfsigncert.pem -noout -fingerprint)"
   Fingerprint="${Fingerprint//:}"
   echo ${Fingerprint#*=}
   ```

2. Copy the complete output (a hexadecimal string) and paste this fingerprint value into a text file.

## Edit inbound policy to only allow requests with a valid certificate

Now, create the authentication policy in the API Management gateway.

1. In the Azure portal, select your API Management service. If necessary, in the Azure resource menu, or from the home page, select **All resources**, and then select your API Management service.

2. In the left menu pane, under **APIs**, select **APIs**. The APIs pane for your API Management service appears.

3. In the secondary menu, select **Weather Data**.

4. In the **Inbound processing** box, select the **</>** icon to open Policies code editor. The HTML code for the policies node displays.

   *Screenshot of the inbound processing policy button.*

![](https://learn.microsoft.com/en-us/training/modules/control-authentication-with-apim/media/5-inbound-policy.png)

5. Replace the `<inbound>` node of the policy file with the following XML, substituting the fingerprint you copied earlier for the `desired-fingerprint` placeholder:

   ```xml
   <inbound>
       <choose>
           <when condition="@(context.Request.Certificate == null || context.Request.Certificate.Thumbprint != "desired-fingerprint")" >
               <return-response>
                   <set-status code="403" reason="Invalid client certificate" />
               </return-response>
           </when>
       </choose>
       <base />
   </inbound>
   ```

6. Select **Save**.

## Call the gateway and pass the client certificate

You can now test the new authentication policy with and without the certificate.

1. To test the API without the certificate, run the following command in Cloud Shell, replacing the placeholder values with your API gateway name and subscription key.

   ```bash
   curl -X -v GET https://[api-gateway-name].azure-api.net/api/Weather/53/-1 \
     -H 'Ocp-Apim-Subscription-Key: [Subscription Key]' 
   ```

   This command should return a 403 Client certificate error, and no data will be returned.

2. In Cloud Shell, to test the API with the certificate, copy and paste the following cURL command, using the primary subscription key from the first exercise (you can also obtain this primary key from the Subscriptions pane for your WeatherData API Management service). Remember to include your API gateway name.

   ```bash
   curl -X GET https://[api-gateway-name].azure-api.net/api/Weather/53/-1 \
     -H 'Ocp-Apim-Subscription-Key: [subscription-key]' \
     --cert-type pem \
     --cert selfsigncert.pem
   ```

   This command should result in a successful response displaying weather data similar to the following.

   ```json
   {"mainOutlook":{"temperature":32,"humidity":34},"wind":{"speed":11,"direction":239.0},"date":"2019-05-16T00:00:00+00:00","latitude":53.0,"longitude":-1.0}
   ```

# 5.6 Summary

In this module, you've learned about API management and how you can control authentication through subscriptions and certificate authentication. You've also learned how the authentication models can be divided into granular levels of restrictions, offering different authorization mechanisms to different clients.

> **Important**
> 
> In this module you created resources using your Azure subscription. You want to clean up these resources so that you will not continue to be charged for them. You can delete resources individually or delete the resource group to delete the entire set of resources.

## Learn more

- API Management documentation
- Subscriptions in Azure API Management
- How to secure back-end services using client certificate authentication in Azure API Management
- Authentication and authorization to APIs in API Management





### Reference:
1) CIS Microsoft Azure Benchmarks, https://www.cisecurity.org/benchmark/azure
2) 




