

# SC-200: Configure your Microsoft Sentinel environment

https://learn.microsoft.com/en-us/training/paths/sc-200-configure-azure-sentinel-environment/


Get started with Microsoft Sentinel by properly configuring the Microsoft Sentinel workspace. This learning path aligns with exam SC-200: Microsoft Security Operations Analyst.

#### Prerequisites
Fundamental understanding of Microsoft security, compliance, and identity products
Ability to use KQL in Microsoft Sentinel like you could learn from learning path SC-200: Create queries for Microsoft Sentinel using Kusto Query Language (KQL)


# 1 Introduction to Microsoft Sentinel

Traditional security information and event management (SIEM) systems typically take a long time to set up and configure. They're also not necessarily designed with cloud workloads in mind. Microsoft Sentinel enables you to start getting valuable security insights from your cloud and on-premises data quickly. This module helps you get started.


## 1.1 Introduction

Imagine that you work as a security operations center (SOC) analyst. Your organization wants to advance its security-management capabilities. The business already started moving some workloads to the public cloud.

You've been asked to evaluate security information and event management (SIEM) solutions that can help in both an on-premises and a multicloud environment. You've heard about Microsoft Sentinel and want to find out whether it could be the right SIEM solution for your business.

Ideally, you'd select a service that provides the features and functionality that you need, with minimal administration and a flexible pricing model.

Microsoft Sentinel offers exactly those benefits.

In this module, you'll explore Microsoft Sentinel and discover why and when to use it. You'll investigate the key features and capabilities of Microsoft Sentinel, including how and when to deploy it.

#### Learning objectives

By the end of this module, you're able to:

- Identify the various components and functionality of Microsoft Sentinel.
- Identify use cases where Microsoft Sentinel would be a good solution.

## Prerequisites
- Familiarity with security operations in an organization
- Basic experience with Azure services



## 1.2  What is Microsoft Sentinel?

Let's start with a few definitions and a look at *security information and event management* (SIEM) systems and Microsoft Sentinel.

## What is security information and event management (SIEM)?

A SIEM system is a tool that an organization uses to collect, analyze, and perform security operations on its computer systems. Those systems can be hardware appliances, applications, or both.

In its simplest form, a SIEM system allows you to:

- Collect and query logs
- Do some form of correlation or anomaly detection
- Create alerts and incidents based on your findings

A SIEM system might offer functionality such as:

- **Log management**: The ability to collect, store, and query the log data from resources within your environment
- **Alerting**: A proactive look inside the log data for potential security incidents and anomalies
- **Visualization**: Graphs and dashboards that provide visual insights into your log data
- **Incident management**: The ability to create, update, assign, and investigate incidents that have been identified
- **Querying data**: A rich query language, similar to that for log management, that you can use to query and understand your data

##  What is Microsoft Sentinel?

Microsoft Sentinel is a cloud-native SIEM system that a security operations team can use to:

- Get security insights across the enterprise by collecting data from virtually any source
- Detect and investigate threats quickly by using built-in machine learning and Microsoft threat intelligence
- Automate threat responses by using playbooks and by integrating Azure Logic Apps

Unlike with traditional SIEM solutions, you don't need to install any servers either on-premises or in the cloud to run Microsoft Sentinel. Microsoft Sentinel is a service that you deploy in Azure. You can get up and running with Sentinel in just a few minutes in the Azure portal.

Microsoft Sentinel is tightly integrated with other cloud services. Not only can you quickly ingest logs, but you can also use other cloud services natively (for example, authorization and automation).

Microsoft Sentinel helps you enable end-to-end security operations including collection, detection, investigation, and response:

Let's take a look at the key components in Microsoft Sentinel.


## 1.3 How Microsoft Sentinel Works

Microsoft Sentinel helps you enable end-to-end security operations. It starts with log ingestion and continues through to automated response to security alerts.

Here are the key features and components of Microsoft Sentinel.

## Data Connectors

The first thing to do is to have your data ingested into Microsoft Sentinel. Data connectors let you do just that. You connect Data connectors by first installing Content hub solutions. Once installed, you can add some services, such as Azure activity logs, just by selecting a button. Others, such as syslog, require more configuration. There are data connectors that cover all scenarios and sources, including but not limited to:

- syslog
- Common Event Format (CEF)
- Trusted Automated eXchange of Indicator Information (TAXII) (for threat intelligence)
- Azure Activity
- Microsoft Defender services
- Amazon Web Services (AWS) and Google Cloud Platform (GCP)

*Screenshot that shows a partial list of data connectors in the Microsoft Sentinel UI in the Azure portal.*

## Log Retention

After data is ingested into Microsoft Sentinel, the data is stored in the Log Analytics workspace. The benefits of using Log Analytics include the ability to use the Kusto Query Language (KQL) to query your data. KQL is a rich query language that gives you the power to dive into and gain insights from our data.

*Screenshot showing the Log Analytics interface in the Azure portal.*

## Workbooks

You can use workbooks to visualize your data within Microsoft Sentinel. Think of workbooks as dashboards. Each component in the dashboard is built by using an underlying KQL query of your data. You can use the built-in workbooks within Microsoft Sentinel and edit them to meet your own needs, or create your own workbooks from scratch. If you've used Azure Monitor workbooks, this feature is familiar to you, because it's Sentinel's implementation of Monitor workbooks.

*Screenshot showing an example of a workbook in Microsoft Sentinel.*

## Analytics Alerts

So far, you have your logs and some data visualization. Now it would be great to have some proactive analytics across your data, so you're notified when something suspicious occurs. You can enable built-in analytics alerts within your Sentinel workspace. There are various types of alerts, some of which you can edit to your own needs. Other alerts are built on machine-learning models that are proprietary to Microsoft. You can also create custom, scheduled alerts from scratch.

*Screenshot showing some of the built-in analytics alerts available in a Microsoft Sentinel workbook.*

## Threat Hunting

We won't dive deeply into threat hunting in this module. However, if SOC analysts need to hunt for suspicious activity, many Content hub solutions provide built-in hunting queries that they can use. Analysts can also create their own queries. Sentinel also integrates with Azure Notebooks. It provides example notebooks for advanced hunters who want to use the full power of a programming language to hunt through their data.

*Screenshot showing the threat-hunting interface in Microsoft Sentinel.*

## Incidents and Investigations

An incident is created when an alerts are triggered. In Microsoft Sentinel, you can do standard incident management tasks like changing status or assigning incidents to individuals for investigation. Microsoft Sentinel also has investigation functionality, so you can visually investigate incidents by mapping entities across log data along a timeline.

*Screenshot showing an incident-investigation graph within Microsoft Sentinel.*

## Automation Playbooks

With the ability to respond to incidents automatically, you can automate some of your security operations and make your SOC more productive. Microsoft Sentinel allows you to create automated workflows, or playbooks, in response to events. This functionality could be used for incident management, enrichment, investigation, or remediation. These capabilities are often referred to as security orchestration, automation, and response (SOAR).

*Screenshot showing a Microsoft Sentinel Automation, with the Create options highlighted.*

As the SOC Analyst, you now start to see how Microsoft Sentinel might help you achieve your goals. For example, you could:

- Ingest data from your cloud and on-premises environments
- Perform analytics on that data
- Manage and investigate any incidents that occur
- Respond automatically by using playbooks

In other words, Microsoft Sentinel gives you an end-to-end solution for your security operations.


# 1.4 When to Use Microsoft Sentinel

Microsoft Sentinel is a solution for performing security operations on your cloud and on-premises environments.

## Use Microsoft Sentinel if you want to:

- Collect event data from various sources
- Perform security operations on that data to identify suspicious activity

Security operations could include:

- Visualization of log data
- Anomaly detection
- Threat hunting
- Security incident investigation
- Automated response to alerts and incidents

## Key Capabilities

Microsoft Sentinel offers other capabilities that could help you decide whether it's the right fit for you:

- **Cloud-native SIEM**: with no servers to provision, scaling is effortless
- **Integration with the Azure Logic Apps service** and its hundreds of connectors
- **Benefits of Microsoft research and machine learning**
- **Key log sources provided for free**
- **Support for hybrid cloud and on-premises environments**
- **SIEM and a data lake all in one**

## Decision Context

When you began investigating Microsoft Sentinel, your organization had some clear requirements:

- Support for data from multiple cloud environments
- Features and functionality required for a security operations center (SOC), without too much administrative overhead

You've found that Microsoft Sentinel could be a good fit. It offers data connectors for syslog, Amazon Web Services (AWS), and other sources, and the ability to scale effortlessly without provisioning servers. During your analysis, you also realized that your organization should make automation a key part of its SOC strategy. Automation wasn't something the organization had considered before, but now you'll look into using automation playbooks.

## Additional Considerations

If you're collecting infrastructure or application logs for performance monitoring, consider also using Azure Monitor and Log Analytics for that purpose.

And perhaps you want to understand the security posture of your environment, make sure that you're compliant with policy, and check for security misconfigurations. If so, consider also using Microsoft Defender for Cloud. You can ingest Defender for Cloud alerts as a data connector for Microsoft Sentinel.


# 1.5 Module Assessment

Choose the best response for each question.

## 1. What does Microsoft Sentinel provide?

- [ ] A solution for checking your security posture in the cloud
- [x] **An end-to-end solution for security operations**
- [ ] A solution for securely storing keys and secrets in the cloud

**Answer: An end-to-end solution for security operations**

*Explanation: Microsoft Sentinel is a cloud-native SIEM system that provides comprehensive security operations capabilities including data collection, threat detection, investigation, and automated response.*

## 2. Which language is used to query data within Microsoft Sentinel?

- [ ] SQL
- [ ] GraphQL
- [x] **KQL**

**Answer: KQL (Kusto Query Language)**

*Explanation: Microsoft Sentinel uses KQL (Kusto Query Language) to query and analyze log data stored in the Log Analytics workspace. KQL is a rich query language designed for log data analysis.*

## 3. Which Azure service stores the log data that is ingested into Microsoft Sentinel?

- [ ] Azure Data Factory
- [x] **Log Analytics**
- [ ] Azure Monitor

**Answer: Log Analytics**

*Explanation: Microsoft Sentinel stores all ingested log data in a Log Analytics workspace, which provides the underlying data storage and query capabilities using KQL.*

---

**Submit answers**

## 2 Create and manage Microsoft Sentinel workspaces

Learn about the architecture of Microsoft Sentinel workspaces to ensure you configure your system to meet your organization's security operations requirements.


# 2.1 Introduction

Deploying the Microsoft Sentinel environment involves designing a workspace configuration to meet your security and compliance requirements. The provisioning process includes creating a Log Analytics workspace and configuring the Microsoft Sentinel options.

## Scenario

You're a Security Operations Analyst working at a company that is implementing Microsoft Sentinel. You're responsible for setting up the Microsoft Sentinel environment to meet the company requirement to minimize cost, meet compliance regulations, and provide the most manageable environment for your security team to perform their daily job responsibilities.

You start by understanding the Microsoft Sentinel workspace's architecture. After you've decided on your workspace implementation options, you create your first Microsoft Sentinel workspace.

## Learning Objectives

After completing this module, you'll be able to:

- Describe Microsoft Sentinel workspace architecture
- Install Microsoft Sentinel workspace
- Manage a Microsoft Sentinel workspace


# 2.2 Plan for the Microsoft Sentinel Workspace


Before deploying Microsoft Sentinel, it's crucial to understand the workspace options. The Microsoft Sentinel solution is installed in a Log Analytics Workspace, and most implementation considerations are focused on the Log Analytics Workspace creation. The single most important option when creating a new Log Analytics Workspace is the region. The region specifies the location where the log data resides.

## The Three Implementation Options:

- Single-Tenant with a single Microsoft Sentinel Workspace
- Single-Tenant with regional Microsoft Sentinel Workspaces
- Multiple tenants

## Single-Tenant Single Workspace

The single-tenant with a single Microsoft Sentinel workspace is the central repository for logs across all resources within the same tenant.

This workspace receives logs from resources in other regions within the same tenant. Because the log data (when collected) travels across regions and stored in another region, this creates two possible concerns. First, it can incur a bandwidth cost. Second, if there's a data governance requirement to keep data in a specific region, the single workspace option wouldn't be an implementation option.

### Single-Tenants with a Single Workspace Trade-offs:

| **Pros** | **Cons** |
|----------|----------|
| Central Pane of Glass | May not meet Data Governance Requirements |
| Consolidates all security logs and information | Can incur bandwidth cost for cross region |
| Easier to query all information | |
| Azure Log Analytics RBAC to control data access | |
| Microsoft Sentinel RBAC for service RBAC | |

## Single-Tenant with Regional Microsoft Sentinel Workspaces

The single-tenant with regional Microsoft Sentinel workspaces, have multiple Microsoft Sentinel workspaces requiring the creation and configuration of multiple Microsoft Sentinel and Log Analytics workspaces.

| **Pros** | **Cons** |
|----------|----------|
| No cross-region bandwidth costs | No central pane of glass. You aren't looking in one place to see all the data. |
| May be required to meet Data Governance requirements | Analytics, Workbooks, etc. must be deployed multiple times. |
| Granular data access control | |
| Granular retention settings | |
| Split billing | |

To query data across workspaces, use the workspace() function before the table name.

```kusto
TableName
| union workspace("WorkspaceName").TableName
```

## Multiple Tenant Workspaces

If you're required to manage a Microsoft Sentinel workspace, not in your tenant, you implement Multiple tenant workspaces using Azure Lighthouse. This security configuration grants you access to the tenants. The tenant configuration within the tenant (regional or multi-regional) is the same consideration as before.

## Use the Same Log Analytics Workspace as Microsoft Defender for Cloud

Use the same workspace for both Microsoft Sentinel and Microsoft Defender for Cloud, so that all logs collected by Microsoft Defender for Cloud can also be ingested and used by Microsoft Sentinel. The default workspace created by Microsoft Defender for Cloud won't appear as an available workspace for Microsoft Sentinel.

# 2.3 Create a Microsoft Sentinel Workspace

After designing the workspace architecture, sign-in to the Azure portal. At the search bar, search for Sentinel, then select **Microsoft Sentinel**. The Microsoft Sentinel Workspaces shows a list of the current workspaces. Select the **+ add** button to start the creation process.

> **Note**
> 
> If you choose to perform this exercise, be aware you might incur costs in your Azure Subscription. To estimate the cost, refer to **Microsoft Sentinel Pricing**. We have also included an interactive lab simulation after the exercise.

## Microsoft Sentinel Installation Prerequisites

To enable Microsoft Sentinel, you need contributor permissions to the subscription in which the Microsoft Sentinel workspace resides. To use Microsoft Sentinel, you need either contributor or reader permissions on the resource group that the workspace belongs.

## Create and Configure a Log Analytics Workspace

1. The next page, **Add Microsoft Sentinel to a workspace** will display a list of available Log Analytics workspaces to add Microsoft Sentinel. Select the **+ create a new workspace** button to start the "Create Log Analytics workspace" process.

2. The Basics tab includes the following options:

| **Option** | **Description** |
|------------|-----------------|
| Subscription | Select the Subscription |
| Resource Group | Select or create a Resource Group |
| Name | Name is the name of the Log Analytics workspace and is also the name of your Microsoft Sentinel Workspace |
| Region | The region is the location the log data is stored. |

> **Important**
> 
> The Name is the name of the Microsoft Sentinel workspace. The Microsoft Sentinel name defaults to the Log Analytics Workspace Name. The Region is the location where ingested data is stored. The data location impacts data governance requirements. Workspaces can't move from region to region; you'll need to recreate the workspace if the region option needs to be changed.

3. Select the **Review + Create** button and then select the **Create** button.

## Add Microsoft Sentinel to the Workspace

The "Add Microsoft Sentinel to Workspace" screen will now appear after you've completed the previous steps.

1. Wait for the newly created "Log Analytics Workspace" to appear in the list. This operation could take a few minutes.

2. Select the newly created Log Analytics workspace. And select the **Add** button.

The new Microsoft Sentinel workspace is now the active screen. The Microsoft Sentinel left navigation has four areas:

- General
- Threat management
- Content management
- Configuration

The Overview tab displays a standard dashboard of information about the ingested data, alerts, and incidents.

## Interactive Lab Simulation

> **Note**
> 
> Select the thumbnail image to start the lab simulation. When you're done, be sure to return to this page so you can continue learning.

## Microsoft Sentinel Sharing a Log Analytics Workspace

Considering that Microsoft Sentinel workspace uses a Log Analytics workspace, you have the option to enable the Microsoft Sentinel workspace in a Log Analytics workspace that is used by other solutions. The most common scenario is sharing the Log Analytics workspace used by Microsoft Defender for Cloud. Sharing the workspace enables one central workspace to query security data.

### Microsoft Defender for Cloud

When creating your Microsoft Sentinel workspace, you aren't allowed to use the **Default** Microsoft Defender for Cloud Log Analytics workspace. You need to manually create a Log Analytics workspace then update the Microsoft Defender for Cloud tier. Now you can select the manually created Log Analytics workspace for use with Microsoft Defender for Cloud.


# 2.4 Manage Workspaces Across Tenants Using Azure Lighthouse

If you're required to manage multiple Microsoft Sentinel workspaces, or workspaces not in your tenant, you have two options:

- Microsoft Sentinel Workspace manager
- Azure Lighthouse

## Microsoft Sentinel Workspace Manager

Microsoft Sentinel's Workspace manager enables users to centrally manage multiple Microsoft Sentinel workspaces within one or more Azure tenants. The Central workspace (with Workspace manager enabled) can consolidate content items to be published at scale to Member workspaces. Workspace manager is enabled in the `Configuration settings`.

## Azure Lighthouse

Implementing Azure Lighthouse provides the option to enable your access to the tenant. Once Azure Lighthouse is onboarded, use the directory + subscription selector on the Azure portal to select all the subscriptions containing workspaces you manage.

Azure Lighthouse allows greater flexibility to manage resources for multiple customers without having to sign in to different accounts in different tenants. For example, a service provider may have two customers with different responsibilities and access levels. By using Azure Lighthouse, authorized users can sign in to the service provider's tenant to access these resources.


## 2.5 Understand Microsoft Sentinel Permissions and Roles

Microsoft Sentinel uses Azure role-based access control (Azure RBAC) to provide built-in roles that can be assigned to users, groups, and services in Azure.

Use Azure RBAC to create and assign roles within your security operations team to grant appropriate access to Microsoft Sentinel. The different roles give you fine-grained control over what users of Microsoft Sentinel can see and do. Azure roles can be assigned in the Microsoft Sentinel workspace directly, or in a subscription or resource group that the workspace belongs to, which Microsoft Sentinel will inherit.

## Microsoft Sentinel-Specific Roles

All Microsoft Sentinel built-in roles grant read access to the data in your Microsoft Sentinel workspace:

- **Microsoft Sentinel Reader**: can view data, incidents, workbooks, and other Microsoft Sentinel resources.

- **Microsoft Sentinel Responder**: can, in addition to the above, manage incidents (assign, dismiss, etc.)

- **Microsoft Sentinel Contributor**: can, in addition to the above, create and edit workbooks, analytics rules, and other Microsoft Sentinel resources.

- **Microsoft Sentinel Automation Contributor**: allows Microsoft Sentinel to add playbooks to automation rules. It isn't meant for user accounts.

For best results, these roles should be assigned to the resource group that contains the Microsoft Sentinel workspace. The roles then apply to all the resources that deploy to support Microsoft Sentinel, if those resources are in the same resource group.

## Additional Roles and Permissions

Users with particular job requirements may need to be assigned other roles or specific permissions in order to accomplish their tasks.

### Working with Playbooks to Automate Responses to Threats

Microsoft Sentinel uses playbooks for automated threat response. Playbooks are built on Azure Logic Apps, and are a separate Azure resource. You might want to assign to specific members of your security operations team the ability to use Logic Apps for Security Orchestration, Automation, and Response (SOAR) operations. You can use the Logic App Contributor role to assign explicit permission for using playbooks.

### Giving Microsoft Sentinel Permissions to Run Playbooks

Microsoft Sentinel uses a special service account to run incident-trigger playbooks manually or to call them from automation rules. The use of this account (as opposed to your user account) increases the security level of the service.

In order for an automation rule to run a playbook, this account must be granted explicit permissions to the resource group where the playbook resides. At that point, any automation rule will be able to run any playbook in that resource group. To grant these permissions to this service account, your account must have Owner permissions on the resource groups containing the playbooks.

### Connecting Data Sources to Microsoft Sentinel

For a user to add data connectors, you must assign the user write permissions on the Microsoft Sentinel workspace. Also, note the required other permissions for each connector, as listed on the relevant connector page.

### Guest Users Assigning Incidents

If a guest user needs to be able to assign incidents, then in addition to the Microsoft Sentinel Responder role, the user will also need to be assigned the role of Directory Reader. This role isn't an Azure role but a Microsoft Entra role, and that regular (non-guest) users have this role assigned by default.

### Creating and Deleting Workbooks

To create and delete a Microsoft Sentinel workbook, the user requires either the Microsoft Sentinel Contributor role or a lesser Microsoft Sentinel role plus the Azure Monitor role of Workbook Contributor. This role isn't necessary for using workbooks, but only for creating and deleting.

## Azure Roles and Azure Monitor Log Analytics Roles

In addition to Microsoft Sentinel-dedicated Azure RBAC roles, other Azure and Log Analytics Azure RBAC roles can grant a wider set of permissions. These roles include access to your Microsoft Sentinel workspace and other resources.

Azure roles grant access across all your Azure resources. They include Log Analytics workspaces and Microsoft Sentinel resources:

- Owner
- Contributor
- Reader

Log Analytics roles grant access across all your Log Analytics workspaces:

- Log Analytics Contributor
- Log Analytics Reader

For example, a user who is assigned with the Microsoft Sentinel Reader and Azure Contributor (not Microsoft Sentinel Contributor) roles can edit data in Microsoft Sentinel. If you want to only grant permissions to Microsoft Sentinel, you should carefully remove the user's prior permissions. Make sure you don't break any needed permission role for another resource.

## Microsoft Sentinel Roles and Allowed Actions

The following table summarizes the roles and allowed actions in Microsoft Sentinel.

| **Roles** | **Create and run playbooks** | **Create and edit workbooks, analytic rules, and other Microsoft Sentinel resources** | **Manage incidents such as dismissing and assigning** | **View data incidents, workbooks, and other Microsoft Sentinel resources** |
|-----------|-------------------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------|----------------------------------------------------------------------------|
| Microsoft Sentinel Reader | No | No | No | Yes |
| Microsoft Sentinel Responder | No | No | Yes | Yes |
| Microsoft Sentinel Contributor | No | Yes | Yes | Yes |
| Microsoft Sentinel Contributor and Logic App Contributor | Yes | Yes | Yes | Yes |

## Custom Roles and Advanced Azure RBAC

If the built-in Azure roles don't meet the specific needs of your organization, you can create your own custom roles. Just like built-in roles, you can assign custom roles to users, groups, and service principals for management-group, subscription, and resource-group scopes.


## 2.6 Manage Microsoft Sentinel Settings

Microsoft Sentinel Environment Settings are managed in two areas. In Microsoft Sentinel and in the Log Analytics workspace where Microsoft Sentinel resides. In Microsoft Sentinel, the left navigation has an option for Settings. The Settings includes tabs for Pricing, Settings, and Workspace Settings—the Settings changes over time based on the current and in-preview feature set. Most Microsoft Sentinel Environment settings are managed in the Log Analytics workspace. Other areas within the Microsoft Sentinel portal will transfer you to the Log Analytics portal. An example would be specific data connector configurations that are performed in the log analytics workspace.

## Configure Log Retention

Data retention at the workspace level can be configured from 30 to 730 days (two years) for all workspaces unless they're using the legacy Free pricing tier. To adjust the retention days, select the workspace settings in the Microsoft Sentinel Settings area. The next screen is in the Log Analytics portal. Select the "Usage and estimated costs" tab. At the top of the page, select the "Retention" button. A window will open, allowing for the adjustment of the retention days.

# 2.7 Configure Logs

There are three primary log types in Microsoft Sentinel:

- Analytics Logs
- Basic Logs
- Auxiliary Logs (Preview)

Data in each table in a Log Analytics workspace is retained for a specified period of time after which it's either removed or archived with a reduced retention fee. Set the retention time to balance your requirement for having data available with reducing your cost for data retention.

To access archived data, you must first retrieve data from it in an Analytics Logs table using one of the following methods:

- Search Jobs
- Restore

*Diagram of different Workspace Log Types.*

## Analytical Logs

By default, all tables in a workspace are of type Analytics Logs, which are available to all features of a Log Analytics workspace and any other services that use the workspace.

## Basic Logs

You can configure certain tables as Basic Logs to reduce the cost of storing high-volume verbose logs you use for debugging, troubleshooting and auditing, but not for analytics and alerts. Tables configured for Basic Logs have a lower ingestion cost in exchange for reduced features. Basic logs are only retained for 8 days.

## Auxiliary Logs (Preview)

Auxiliary Logs are suited for low-touch data, such as verbose logs, and data required for auditing and compliance. This plan offers low-cost ingestion and unoptimized single-table queries for 30 days.

## KQL Language Limits

Queries against Basic Logs are optimized for simple data retrieval using a subset of KQL language, including the following operators:

- where
- extend
- project
- project-away
- project-keep
- project-rename
- project-reorder
- parse
- parse-where

The following KQL isn't supported:

- join
- union
- aggregates (summarize)

## Table Support Basic Logs

All tables in your Log Analytics are Analytics tables, by default. You can configure particular tables to use Basic Logs. You can't configure a table for Basic Logs if Azure Monitor relies on that table for specific features.

You can currently configure the following tables for Basic Logs:

- All tables created with the Data Collection Rule (DCR)-based custom logs API
- ContainerLogV2, which Container Insights uses and which include verbose text-based log records
- AppTraces, which contain freeform log records for application traces in Application Insights

## Configure Log Type

To adjust the log type for an eligible table, select the workspace settings in the Microsoft Sentinel Settings area.

The next screen is in the Log Analytics portal.

1. Select the "Tables" tab
2. Select the table then ... at the end of the row
3. Select Manage table
4. Change the Table plan
5. Select Save

## Long-Term Retention

By default, all tables in a Log Analytics workspace retain data for 30 days, except for log tables with 90-day default retention. During this period - the interactive retention period - you can retrieve the data from the table through queries, and the data is available for visualizations, alerts, and other features and services, based on the table plan.

You can extend the interactive retention period of tables with the Analytics plan to up to two years. The Basic and Auxiliary plans have a fixed interactive retention period of 30 days.

*Diagram of the Retention archive process.*

To retain data in the same table beyond the interactive retention period, extend the table's total retention to up to 12 years. At the end of the interactive retention period, the data stays in the table for the remainder of the total retention period you configure. During this period - the long-term retention period - run a search job to retrieve the specific data you need from the table and make it available for interactive queries in a search results table.

## Configure Table Retention

To adjust the retention days for a table, select the workspace settings in the Microsoft Sentinel Settings area.

The next screen is in the Log Analytics portal.

1. Select the "Tables" tab
2. Select the table then ... at the end of the row
3. Select Manage table
4. Change the Total retention period
5. Select Save


# 2.8 Module Assessment

Choose the best response for each question.

*AI-generated content: The question and answer choices in this module assessment were created with AI.*

**Provide feedback**

## 1. Your organization needs granular data access control and split billing across different departments. Which Microsoft Sentinel workspace architecture option best supports these requirements?

- [ ] Single-tenant with a single Microsoft Sentinel workspace
- [x] **Single-tenant with regional Microsoft Sentinel workspaces**
- [ ] Multiple tenants using Azure Lighthouse

**Answer: Single-tenant with regional Microsoft Sentinel workspaces**

*Explanation: Regional workspaces provide granular data access control and split billing capabilities, which are ideal for departmental separation.*

## 2. Which permission level is required to enable Microsoft Sentinel on a workspace?

- [ ] Reader permissions on the resource group
- [ ] Owner permissions on the Log Analytics workspace
- [x] **Contributor permissions on the subscription**

**Answer: Contributor permissions on the subscription**

*Explanation: To enable Microsoft Sentinel, you need contributor permissions to the subscription in which the Microsoft Sentinel workspace resides.*

## 3. What is a potential disadvantage of using a single-tenant single Microsoft Sentinel workspace?

- [ ] Granular data access control
- [x] **May incur bandwidth costs for cross-region data transfer**
- [ ] Split billing across multiple workspaces

**Answer: May incur bandwidth costs for cross-region data transfer**

*Explanation: When log data travels across regions to be stored in a single workspace, it can incur bandwidth costs and may not meet data governance requirements.*

## 4. A user needs to be able to view incidents and manage playbooks within Microsoft Sentinel. Which combination of roles should be assigned to fulfill this requirement?

- [x] **Microsoft Sentinel Reader and Logic App Contributor**
- [ ] Microsoft Sentinel Responder and Microsoft Sentinel Automation Contributor
- [ ] Microsoft Sentinel Contributor and Microsoft Sentinel Responder

**Answer: Microsoft Sentinel Reader and Logic App Contributor**

*Explanation: Microsoft Sentinel Reader provides viewing capabilities, while Logic App Contributor enables playbook management.*

## 5. Your company requires that data ingested by Microsoft Sentinel be stored in a specific region due to compliance regulations. What is the most important consideration when creating a new Log Analytics workspace?

- [ ] Selecting the appropriate resource group
- [ ] Ensuring contributor permissions on the subscription
- [x] **Choosing the correct region for the Log Analytics workspace**

**Answer: Choosing the correct region for the Log Analytics workspace**

*Explanation: The region specifies where log data is stored and impacts data governance requirements. Workspaces cannot be moved between regions.*

## 6. Your company needs to manage multiple Microsoft Sentinel workspaces across different Azure tenants. Which tool should you use to achieve effective management?

- [ ] Single-tenant with regional Microsoft Sentinel workspaces
- [ ] Microsoft Sentinel Workspace manager
- [x] **Azure Lighthouse**

**Answer: Azure Lighthouse**

*Explanation: Azure Lighthouse enables cross-tenant access and management capabilities for multiple customer tenants.*

## 7. While setting up Microsoft Sentinel, you need a user to have the ability to view incidents and workbooks but not to edit them. Which role should be assigned?

- [x] **Microsoft Sentinel Reader**
- [ ] Microsoft Sentinel Responder
- [ ] Microsoft Sentinel Contributor

**Answer: Microsoft Sentinel Reader**

*Explanation: Microsoft Sentinel Reader provides read-only access to view data, incidents, workbooks, and other Microsoft Sentinel resources.*

## 8. If a security operations team member needs to create and manage analytics rules in Microsoft Sentinel, which role should be assigned?

- [ ] Microsoft Sentinel Reader
- [x] **Microsoft Sentinel Contributor**
- [ ] Microsoft Sentinel Responder

**Answer: Microsoft Sentinel Contributor**

*Explanation: Microsoft Sentinel Contributor can create and edit workbooks, analytics rules, and other Microsoft Sentinel resources.*

## 9. What is the role of Azure Lighthouse in managing Microsoft Sentinel workspaces?

- [x] **It provides cross-tenant access and management capabilities**
- [ ] It enables data governance within a single tenant
- [ ] It restricts access to Microsoft Sentinel resources

**Answer: It provides cross-tenant access and management capabilities**

*Explanation: Azure Lighthouse allows service providers to manage resources across multiple customer tenants without signing into different accounts.*


# 2.9 Summary and Resources

You should have learned how the Microsoft Sentinel provisioning process includes creating a Log Analytics workspace and configuring the Microsoft Sentinel options.

## Learning Outcomes

You should now be able to:

- Describe Microsoft Sentinel workspace architecture
- Provision a Microsoft Sentinel workspace
- Manage a Microsoft Sentinel workspace

## Learn More

You can learn more by reviewing the following:

- Become a Microsoft Sentinel Ninja
- Microsoft Tech Community Security Webinars



# 3 Query logs in Microsoft Sentinel

As a Security Operations Analyst, you must understand the tables, fields, and data ingested in your workspace. Learn how to query the most used data tables in Microsoft Sentinel.

# 3.1 Introduction

Microsoft Sentinel collects log data that is stored in tables. The Logs page in Microsoft Sentinel provides a user interface to build and view query results using the Kusto Query Language (KQL). KQL is the query language used to perform data analysis to create analytics, workbooks, and perform hunting with Microsoft Sentinel.

## Scenario

You're a Security Operations Analyst working at a company that is implementing Microsoft Sentinel. You must explore the tables available in your workspace. The Logs page using Microsoft Sentinel allows you to write Kusto Query Language (KQL) statements to view data stored in the tables. When you connect log data to the Microsoft Sentinel workspace, the connectors will write data to specific tables.

You need to have a basic understanding of the provided tables and their intended purpose. For example, the "SecurityEvents" table is designed for Windows Security Event log data. With this knowledge, you'll be able to query the required tables to use in your search for malicious activity.

## Learning Objectives

After completing this module, you'll be able to:

- Use the Logs page to view data tables with Microsoft Sentinel
- Query the most used tables using Microsoft Sentinel

## Prerequisites

Basic knowledge of operational concepts such as monitoring, logging, and alerting


# 3.2 Query Logs in the Logs Page

KQL is the language used to query the log data in the Log Analytics workspace. In Microsoft Sentinel, the Logs page provides access to the query window. The query window allows you to run queries, save queries, run saved queries, create a new alert rule, and export. The left side provides a list of tables and related table fields. To run a query, enter the query text and press the run button. Query results appear in the bottom section of the form.

# 3.3 Understand Microsoft Sentinel Tables

Microsoft Sentinel has Analytic Rules that generate Alerts and Incidents based on querying the tables within Log Analytics. The primary tables to manage alerts and incidents are SecurityAlert and SecurityIncident. Microsoft Sentinel provides tables to be a repository of indicators and watchlists.

> **Note**
> 
> Some of the Sentinel Data Connectors ingest alerts directly.

The table below is the Microsoft Sentinel feature related tables.

| **Table** | **Description** |
|-----------|-----------------|
| `SecurityAlert` | Contains Alerts Generated from Sentinel Analytical Rules. Also, it could include Alerts created directly from a Sentinel Data Connector |
| `SecurityIncident` | Alerts can generate Incidents. Incidents are related to Alert(s). |
| `ThreatIntelligenceIndicator` | Contains user-created or data connector ingested Indicators such as File Hashes, IP Addresses, Domains |
| `Watchlist` | A Microsoft Sentinel watchlist contains imported data. |


## 3.4 Understand Common Tables

When Sentinel ingests data from the Data Connectors, the following table lists the most commonly used tables.

| **Table** | **Description** |
|-----------|-----------------|
| AzureActivity | Entries from the Azure Activity log that provides insight into any subscription-level or management group level events that have occurred in Azure. |
| AzureDiagnostics | Stores resource logs for Azure services that use Azure Diagnostics mode. Resource logs describe the internal operation of Azure resources. |
| AuditLogs | Audit log for Microsoft Entra ID. Includes system activity information about user and group management, managed applications, and directory activities. |
| CommonSecurityLog | Syslog messages using the Common Event Format (CEF). |
| McasShadowItReporting | Microsoft Defender for Cloud Apps logs |
| OfficeActivity | Audit logs for Office 365 tenants collected by Microsoft Sentinel. Including Exchange, SharePoint and Teams logs. |
| SecurityEvent | Security events collected from windows machines by Azure Security Center or Microsoft Sentinel |
| SigninLogs | Azure Activity Directory Sign-in logs |
| Syslog | Syslog events on Linux computers using the Log Analytics agent. |
| Event | Sysmon Events collected from a Windows host. |
| WindowsFirewall | Windows Firewall Events |



## 3.5 Understand Microsoft Defender XDR Tables

The Microsoft Defender XDR Sentinel Data Connector can populate tables with raw data collected from the Microsoft Defender XDR solutions.

| **Table Name** | **Description** |
|----------------|-----------------|
| AlertEvidence | Files, IP addresses, URLs, users, or devices associated with alerts |
| CloudAppEvents | Events involving accounts and objects in Office 365 and other cloud apps and services |
| DeviceEvents | Multiple event types, including events triggered by security controls such as Windows Defender Antivirus and exploit protection |
| DeviceFileCertificateInfo | Certificate information of signed files obtained from certificate verification events on endpoints |
| DeviceFileEvents | File creation, modification, and other file system events |
| DeviceImageLoadEvents | DLL loading events |
| DeviceInfo | Machine information, including OS information |
| DeviceLogonEvents | Sign-ins and other authentication events on devices |
| DeviceNetworkEvents | Network connection and related events |
| DeviceNetworkInfo | Network properties of devices, including physical adapters, IP and MAC addresses, as well as connected networks and domains |
| DeviceProcessEvents | Process creation and related events |
| DeviceRegistryEvents | Creation and modification of registry entries |
| EmailEvents | Microsoft 365 email events, including email delivery and blocking events |
| EmailPostDeliveryEvents | Security events that occur post-delivery, after Microsoft 365 has delivered the emails to the recipient mailbox |
| EmailUrlInfo | Information about URLs on emails |
| EmailAttachmentInfo | Information about files attached to Office 365 emails |
| IdentityDirectoryEvents | Events involving an on-premises domain controller running Active Directory (AD). This table covers a range of identity-related events and system events on the domain controller. |
| IdentityLogonEvents | Authentication events on Active Directory and Microsoft online services |
| IdentityQueryEvents | Queries for Active Directory objects, such as users, groups, devices, and domains |



## 3.6 Module Assessment

Choose the best response for each of the questions below.

## Check Your Knowledge

### 1. Which table stores Defender for Endpoint logon events?

- [x] **DeviceLogonEvents**
- [ ] OfficeActivity
- [ ] SigninLogs

**Answer: DeviceLogonEvents**

*Explanation: DeviceLogonEvents contains sign-ins and other authentication events on devices from Microsoft Defender for Endpoint.*

### 2. What table contains logs from Windows hosts collected directly to Microsoft Sentinel?

- [x] **SecurityEvent**
- [ ] AuditLogs
- [ ] SecurityAlert

**Answer: SecurityEvent**

*Explanation: SecurityEvent table contains security events collected from Windows machines by Azure Security Center or Microsoft Sentinel.*

### 3. Which table stores Alerts from Microsoft Defender for Endpoint?

- [ ] SecurityIncident
- [ ] DeviceEvents
- [x] **SecurityAlert**

**Answer: SecurityAlert**

*Explanation: SecurityAlert table contains alerts generated from Sentinel Analytical Rules and can also include alerts created directly from Sentinel Data Connectors, including Microsoft Defender for Endpoint.*


# 3.7 Summary and Resources


You should have a basic understanding of the provided tables and their intended purpose in Microsoft Sentinel.

## Learning Outcomes

You should now be able to:

- Use the Logs page to view tables with Microsoft Sentinel
- Query the most used tables with Microsoft Sentinel

## Learn More

You can learn more by reviewing the following:

- Become a Microsoft Sentinel Ninja
- Microsoft Tech Community Security Webinars



# 4 Use watchlists in Microsoft Sentinel

Learn how to create Microsoft Sentinel watchlists that are a named list of imported data. Once created, you can easily use the named watchlist in KQL queries.


# 4.1 Introduction

Microsoft Sentinel provides a table to store list data accessible to Kusto Query Language (KQL) queries. The Watchlists page in Microsoft Sentinel provides the management options to maintain the lists.

## Scenario

You're a Security Operations Analyst working at a company that deployed Microsoft Sentinel. The Security Operations team members need to prioritize alerts that are impacting high-value target servers.

You must import a list of server names into Microsoft Sentinel, which is used by detection queries to set a priority field. You import a list of servers into the Watchlist page of Microsoft Sentinel. Once created, you instruct the Security Operations team to use the watch list in their KQL queries.

## Learning Objectives

After completing this module, you'll be able to:

- Create a watchlist with Microsoft Sentinel
- Use KQL to access the watchlist with Microsoft Sentinel

## Prerequisites

 - None


# 4.2 Plan for Watchlists

Microsoft Sentinel watchlists enable collecting data from external data sources for correlation with the events in your Microsoft Sentinel environment. Once created, you can use watchlists in your search, detection rules, threat hunting, and response playbooks. Watchlists are stored in your Microsoft Sentinel workspace as name-value pairs and are cached for optimal query performance and low latency.

## Common Scenarios for Using Watchlists

### Investigating Threats and Incident Response
- **Rapid threat investigation** with quick import of IP addresses, file hashes, and other data from CSV files
- **Enhanced detection capabilities** using watchlist name-value pairs for joins and filters in alert rules, threat hunting, workbooks, notebooks, and general queries

### Business Data Integration
- **Privileged user monitoring** by importing user lists with privileged system access
- **Terminated employee tracking** to create allowlists and blocklists for detecting or preventing unauthorized access attempts
- **Access control enforcement** using watchlists to monitor and control user network access

### Alert Optimization
- **Reducing alert fatigue** by creating allowlists to suppress alerts from authorized users
- **Filtering legitimate activities** from users at authorized IP addresses that perform tasks that would normally trigger alerts
- **Preventing false positives** by ensuring benign events don't become unnecessary alerts

### Data Enrichment
- **Enhanced event analysis** by enriching event data with name-value combinations derived from external data sources
- **Contextual information** adding business context to security events for better analysis and decision-making




# 4.3 Create a Watchlist

To create a watchlist from the Azure portal perform these steps:

## Step-by-Step Process

### 1. Navigate to Watchlist Section
Go to **Microsoft Sentinel > Configuration > Watchlist** and select **Add new**.

### 2. Configure General Settings
On the General page, provide the name, description, and alias for the watchlist, then select **Next**.

### 3. Upload Data Source
On the Source page, select the dataset type, upload a file, then select **Next**.

> **Note**
> 
> File uploads are currently limited to files of up to 3.8 MB in size.

### 4. Review and Create
Review the information, and verify that it's correct. Then select **Create**. A notification appears once the watchlist is ready.

## Using Watchlist in KQL

To use the watchlist data in KQL, use the KQL function `_GetWatchlist('watchlist name')`.

```kusto
_GetWatchlist('HighValueMachines')
```

# 4.4 Manage Watchlists

We recommend you edit an existing watchlist instead of deleting and recreating a watchlist. Log analytics has a five-minute SLA (Service Level Agreement) for data ingestion. If you delete and recreate a watchlist, you might see both the deleted and recreated entries in Log Analytics during this five-minute window. If you see these duplicate entries in Log Analytics for a longer period of time, submit a support ticket.

## Edit a Watchlist Item

Edit a watchlist to edit or add an item to the watchlist.

### Steps to Edit Items

1. In the Azure portal, go to Microsoft Sentinel and select the appropriate workspace.
2. Under Configuration, select **Watchlist**.
3. Select the watchlist you want to edit.
4. On the details pane, select **Update watchlist > Edit watchlist items**.

### To Edit an Existing Watchlist Item

1. Select the checkbox of that watchlist item.
2. Edit the item.
3. Select Save.
4. Select Yes at the confirmation prompt.

### To Add a New Item to Your Watchlist

1. Select Add new.
2. Fill in the fields in the Add watchlist item panel.
3. At the bottom of that panel, select Add.

## Bulk Update a Watchlist

When you have many items to add to a watchlist, use bulk update. A bulk update of a watchlist appends items to the existing watchlist. Then, it deduplicates the items in the watchlist where all the value in each column match.

> **Important Notes:**
> - If you deleted an item from your watchlist file and upload it, bulk update won't delete the item in the existing watchlist. Delete the watchlist item individually. Or, when you have many deletions, delete and recreate the watchlist.
> - The updated watchlist file you upload must contain the search key field used by the watchlist with no blank values.

### Steps for Bulk Update

1. In the Azure portal, go to Microsoft Sentinel and select the appropriate workspace.
2. Under Configuration, select **Watchlist**.
3. Select the watchlist you want to edit.
4. On the details pane, select **Update watchlist > Bulk update**.
5. Under Upload file, drag and drop or browse to the file to upload.
6. If you get an error, fix the issue in the file. Then select Reset and try the file upload again.
7. Select **Next: Review and update > Update**.



# 4.5 Module Assessment

Choose the best response for each of the questions below.

## Check Your Knowledge

### 1. Which of the following operations is a typical scenario for using a Microsoft Sentinel watchlist?

- [ ] Creating more alerts to help identify issues.
- [ ] Export business data as a watchlist.
- [x] **Responding to incidents quickly with the rapid import of IP addresses.**

**Answer: Responding to incidents quickly with the rapid import of IP addresses.**

*Explanation: Watchlists are commonly used for rapid threat investigation by importing IP addresses, file hashes, and other data from CSV files to correlate with security events.*

### 2. How do you access a new watchlist named MyList in KQL?

- [ ] _Watchlist('MyList ')
- [x] **_GetWatchlist('MyList')**
- [ ] _Getlist('MyList ')

**Answer: _GetWatchlist('MyList')**

*Explanation: The correct KQL function to access watchlist data is `_GetWatchlist('watchlist name')` where you specify the name of your watchlist.*

---

## Summary

You have learned how to:

- **Create watchlists** in Microsoft Sentinel for storing external data sources
- **Plan watchlist implementation** for common security scenarios including threat investigation, business data integration, alert optimization, and data enrichment
- **Manage watchlists** through editing individual items and bulk updates
- **Access watchlist data** in KQL queries using the `_GetWatchlist()` function

Watchlists provide a powerful way to enrich security analysis by incorporating external data sources and reducing false positives through allowlists and blocklists.


# 4.6 Summary and Resources

You learned how Microsoft Sentinel provides a table to store list data accessible to Kusto Query Language (KQL) queries. And that the Watchlists page in Microsoft Sentinel provides the management options to maintain the lists.

## Learning Outcomes

You should now be able to:

- Create a watchlist with Microsoft Sentinel
- Use KQL to access the watchlist with Microsoft Sentinel

## Learn More

You can learn more by reviewing the following:

- Become a Microsoft Sentinel Ninja
- Microsoft Tech Community Security Webinars




# 5 Utilize threat intelligence in Microsoft Sentinel

Learn how the Microsoft Sentinel Threat Intelligence page enables you to manage threat indicators.


# 5.1 Introduction

Microsoft Sentinel provides a table to store indicator data accessible to Kusto Query Language (KQL) queries. The Threat intelligence page in Microsoft Sentinel provides the management options to maintain the indicators.

## Scenario

You're a Security Operations Analyst working at a company that implemented Microsoft Sentinel. You receive threat indicators from threat intelligence providers and your threat hunting team. The Indicators include IP addresses, domains, and file hashes that can be utilized by many components within Microsoft Sentinel.

The indicators from the threat intelligence providers are automatically imported into the workspace using connectors. You're tasked with adding the indicators from the threat hunting team. You use the Threat Intelligence page to add the indicators for use by the detection KQL queries.

## Learning Objectives

After completing this module, you'll be able to:

- Manage threat indicators in Microsoft Sentinel
- Use KQL to access threat indicators in Microsoft Sentinel

## Prerequisites

Basic knowledge of operational concepts such as monitoring, logging, and alerting.


# 5.2 Define Threat Intelligence

Cyber threat intelligence (CTI) can come from many sources. Sources include open-source data feeds, threat intelligence-sharing communities, paid intelligence feeds, and security investigations within organizations. CTI can range from written reports on a threat actor's motivations, infrastructure, and techniques, to specific observations of IP addresses, domains, and file hashes. CTI provides essential context for unusual activity, so security personnel can act quickly to protect people and assets.

## Threat Indicators and IoCs

The most utilized CTI in SIEM solutions like Microsoft Sentinel is threat indicator data, sometimes called Indicators of Compromise (IoCs). Threat indicators associate URLs, file hashes, IP addresses, and other data with known threat activity like phishing, botnets, or malware. This form of threat intelligence is often called tactical threat intelligence, because security products and automation can use it in large scale to protect and detect potential threats. Microsoft Sentinel can help detect, respond to, and provide CTI context for malicious cyber activity.

## Integrating Threat Intelligence with Microsoft Sentinel

You can integrate threat intelligence (TI) into Microsoft Sentinel through the following activities:

- **Use Data connectors** to various TI platforms to import threat intelligence into Microsoft Sentinel
- **View and manage** the imported threat intelligence in Logs and the new Threat Intelligence area of Microsoft Sentinel
- **Use built-in Analytics rule templates** to generate security alerts and incidents using your imported threat intelligence
- **Visualize critical information** about your threat intelligence in Microsoft Sentinel with the Threat Intelligence workbook
- **Perform threat hunting** with your imported threat intelligence

# 5.3 Manage Your Threat Indicators

With the Threat Intelligence area, accessible from the Microsoft Sentinel menu, you can also view, sort, filter, and search your imported threat indicators without even writing a Logs query. This area also allows you to create threat indicators directly within the Microsoft Sentinel interface and perform everyday threat intelligence administrative tasks. These tasks include indicator tagging and creating new indicators related to security investigations. Let's look at two of the most common tasks, creating new threat indicators and tagging indicators for easy grouping and reference.

## Accessing Threat Intelligence

### Navigation Options
- Defender portal
- Azure portal

### Steps to Access Threat Intelligence

1. Open the Defender portal and navigate to Microsoft Sentinel.
2. From the **Threat management** section of the Microsoft Sentinel menu, select **Threat intelligence**.
3. If you see the *This page has a new home* message. Select the **Open Intel management** button.
4. You're redirected to the *Intel management* page under the *Threat Intelligence* section of the Defender portal navigation menu.

> **Tip**
> 
> As the *Threat intelligence* capabilities in Microsoft Sentinel are being consolidated into the Defender portals *Threat intelligence* section, you can go directly to *Intel management* from there.

## Creating New Threat Indicators

5. Select the **Add new** button from the top menu of the page.
6. Choose the indicator type, then complete the required fields marked with a red asterisk (*) on the New indicator panel. Select **Apply**.

## Tagging Threat Indicators

Tagging threat indicators is an easy way to group them to make them easier to find. Typically, you might apply a tag to indicators related to a particular incident or indicators representing threats from a known actor or a well-known attack campaign. You can tag threat indicators individually or multi-select indicators and tag them all at once. Since tagging is free-form, a recommended practice is to create standard naming conventions for threat indicator tags. You can apply multiple tags to each indicator.

# 5.4 View Your Threat Indicators with KQL

The indicators reside in the *ThreatIntelligenceIndicator* table. This table is the basis for queries performed by other Microsoft Sentinel features such as Analytics and Workbooks. Here's how to find and view your threat indicators in the ThreatIntelligenceIndicator table.

## Accessing Threat Indicators with KQL

To view your threat indicators with KQL. Select **Logs** from the General section of the Microsoft Sentinel menu. Then run a query on the ThreatIntelligenceIndicator table.

```kusto
ThreatIntelligenceIndicator
```

## Important Update - New Tables

> **Important**
> 
> On April 3, 2025, we publicly previewed two new tables to support STIX indicator and object schemas: `ThreatIntelIndicators` and `ThreatIntelObjects`. Microsoft Sentinel will ingest all threat intelligence into these new tables, while continuing to ingest the same data into the legacy `ThreatIntelligenceIndicator` table until July 31, 2025. 
> 
> **Be sure to update your custom queries, analytics and detection rules, workbooks, and automation to use the new tables by July 31, 2025.** After this date, Microsoft Sentinel will stop ingesting data to the legacy `ThreatIntelligenceIndicator` table. 
> 
> We're updating all out-of-the-box threat intelligence solutions in Content hub to leverage the new tables. For more information about the new table schemas, see **ThreatIntelIndicators** and **ThreatIntelObjects**.


# 5.5 Module Assessment

Choose the best response for each of the questions below.

## Check Your Knowledge

### 1. In Threat Intelligence, indicators are considered as which of the following?

- [ ] Strategic
- [ ] Operational
- [x] **Tactical**

**Answer: Tactical**

*Explanation: Threat indicators are considered tactical threat intelligence because security products and automation can use them at large scale to protect and detect potential threats in real-time operations.*

### 2. Which of these items is an example of a Threat indicator?

- [ ] Threat Actor Name
- [x] **Domain Name**
- [ ] Threat Campaign

**Answer: Domain Name**

*Explanation: Domain names, along with IP addresses, file hashes, and URLs, are examples of threat indicators (IoCs - Indicators of Compromise) that can be directly used in detection systems.*

### 3. What table do you query in KQL to view your indicators?

- [ ] Indicator
- [ ] TI Indicator
- [x] **ThreatIntelligenceIndicator**

**Answer: ThreatIntelligenceIndicator**

*Explanation: The ThreatIntelligenceIndicator table is where threat indicators reside in Microsoft Sentinel and is the table used for KQL queries (though new tables ThreatIntelIndicators and ThreatIntelObjects are being introduced).*

---

**Submit answers**


# 5.6 Summary and Resources

You should have learned how Microsoft Sentinel provides a table to store indicator data accessible to Kusto Query Language (KQL) queries. And how the Threat intelligence page in Microsoft Sentinel provides the management options to maintain the indicators.

## Learning Outcomes

You should now be able to:

- Manage threat indicators in Microsoft Sentinel
- Use KQL to access threat indicators in Microsoft Sentinel

## Key Takeaways

Throughout this module, you have gained knowledge about:

- **Threat Intelligence Concepts** - Understanding cyber threat intelligence (CTI) sources and tactical threat intelligence
- **Indicator Management** - Creating, tagging, and organizing threat indicators through the Microsoft Sentinel interface
- **KQL Integration** - Querying threat indicators using the ThreatIntelligenceIndicator table
- **Future Updates** - Awareness of new tables (ThreatIntelIndicators and ThreatIntelObjects) replacing legacy systems

This knowledge enables you to effectively integrate and manage threat intelligence data within your security operations center, enhancing your organization's ability to detect and respond to cyber threats.



