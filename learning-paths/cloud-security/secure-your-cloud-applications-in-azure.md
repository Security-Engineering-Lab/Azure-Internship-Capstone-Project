

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
