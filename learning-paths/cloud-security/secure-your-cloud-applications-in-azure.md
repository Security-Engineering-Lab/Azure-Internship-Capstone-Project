

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
