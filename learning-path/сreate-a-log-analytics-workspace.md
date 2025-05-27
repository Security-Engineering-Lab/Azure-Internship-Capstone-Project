



# 1 Creating a Log Analytics Workspace for Microsoft Defender for Cloud

https://learn.microsoft.com/en-us/training/modules/create-log-analytics-workspace-microsoft-defender-cloud/

In this module, you'll discover how to create a Log Analytics workspace in the Azure portal for Microsoft Defender for Cloud, improving data collection and security analysis.

## Learning Objectives

By the end of this training module, participants will:

* Understand the importance of a centralized logging solution like Azure Log Analytics workspace for Microsoft Defender for Cloud
* Learn how to create and configure a Log Analytics workspace in Azure
* Gain insights into collecting and analyzing security data from Microsoft Defender for Cloud within the Log Analytics workspace
* Understand how to create custom queries and alerts to proactively detect security threats and incidents
* Recognize the benefits of integrating Log Analytics workspace with other Azure services and tools



# 1.1 Introduction

A Log Analytics workspace is a data store into which you can collect any type of log data from all of your Azure and non-Azure resources and applications. We recommend that you send all log data to one Log Analytics workspace, unless you have specific business needs that require you to create multiple workspaces, as described in Design a Log Analytics workspace architecture.

## Scenario

Imagine you are an Azure Security Engineer using a Log Analytics workspace to collect data from Azure and non-Azure resources, enabling centralized monitoring, custom alerts, and advanced threat detection to enhance security and compliance across a hybrid cloud environment.

## Learning Objectives

By the end of this training module, participants will:

1. Understand the importance of a centralized logging solution like Azure Log Analytics workspace for Microsoft Defender for Cloud
2. Learn how to create and configure a Log Analytics workspace in Azure
3. Gain insights into collecting and analyzing security data from Microsoft Defender for Cloud within the Log Analytics workspace
4. Understand how to create custom queries and alerts to proactively detect security threats and incidents
5. Recognize the benefits of integrating Log Analytics workspace with other Azure services and tools

## Goals

* Enable participants to create a dedicated Log Analytics workspace for Microsoft Defender for Cloud in Azure
* Enhance participants' understanding of the capabilities and benefits of a centralized logging solution
* Provide participants with hands-on experience in configuring and managing Log Analytics workspace
* Empower participants to effectively collect, analyze, and monitor security data from Microsoft Defender for Cloud
* Improve participants' ability to proactively detect and respond to security threats by leveraging custom queries and alerts
* Highlight the advantages of integrating Log Analytics workspace with other Azure services and tools for comprehensive security operations



# 1.2 Log Analytics Workspace


A Log Analytics workspace is a data store into which you can collect any type of log data from all of your Azure and non-Azure resources and applications. Workspace configuration options let you manage all of your log data in one workspace to meet the operations, analysis, and auditing needs of different personas in your organization through:

- Azure Monitor features, such as built-in insights experiences, alerts, and automatic actions
- Other Azure services, such as Microsoft Sentinel, Microsoft Defender for Cloud, and Logic Apps
- Microsoft tools, such as Power BI and Excel
- Integration with custom and third-party application

> **Important**
> 
> Microsoft Sentinel documentation uses the term Microsoft Sentinel workspace. This workspace is the same Log Analytics workspace described in this article, but it's enabled for Microsoft Sentinel. All data in the workspace is subject to Microsoft Sentinel pricing.

## Log Tables

Each Log Analytics workspace contains multiple tables in which Azure Monitor Logs stores data you collect.

Azure Monitor Logs automatically creates tables required to store monitoring data you collect from your Azure environment. You create custom tables to store data you collect from non-Azure resources and applications, based on the data model of the log data you collect and how you want to store and use the data.

Table management settings let you control access to specific tables, and manage the data model, retention, and cost of data in each table. For more information, see Manage tables in a Log Analytics workspace.

*Screenshot showing an example of a log structure.*

## Data Retention

A Log Analytics workspace retains data in two states - interactive retention and long-term retention.

During the interactive retention period, you retrieve the data from the table through queries, and the data is available for visualizations, alerts, and other features and services, based on the table plan.

Each table in your Log Analytics workspace lets you retain data up to 12 years in low-cost, long-term retention. Retrieve specific data you need from long-term retention to interactive retention using a search job. This means that you manage your log data in one place, without moving data to external storage, and you get the full analytics capabilities of Azure Monitor on older data, when you need it.

For more information, see Manage data retention in a Log Analytics workspace.

| Method | Description |
|--------|-------------|
| Search jobs | Retrieve data matching particular criteria. |
| Restore | Retrieve data from a particular time range. |

*Screenshot showing an example of a workspace plan.*

## Data Access

Permission to access data in a Log Analytics workspace is defined by the access control mode setting on each workspace. You can give users explicit access to the workspace by using a built-in or custom role. Or, you can allow access to data collected for Azure resources to users with access to those resources.

For more information, see Manage access to log data and workspaces in Azure Monitor.

## View Log Analytics Workspace Insights

Log Analytics Workspace Insights helps you manage and optimize your Log Analytics workspaces with a comprehensive view of your workspace usage, performance, health, ingestion, queries, and change log.

## Transform Data You Ingest into Your Log Analytics Workspace

Data collection rules (DCRs) that define data coming into Azure Monitor can include transformations that allow you to filter and transform data before it's ingested into the workspace. Since all data sources don't yet support DCRs, each workspace can have a workspace transformation DCR.

Transformations in the workspace transformation DCR are defined for each table in a workspace and apply to all data sent to that table, even if sent from multiple sources. These transformations only apply to workflows that don't already use a DCR. For example, Azure Monitor agent uses a DCR to define data collected from virtual machines. This data won't be subject to any ingestion-time transformations defined in the workspace.

For example, you might have diagnostic settings that send resource logs for different Azure resources to your workspace. You can create a transformation for the table that collects the resource logs that filters this data for only records that you want. This method saves you the ingestion cost for records you don't need. You might also want to extract important data from certain columns and store it in other columns in the workspace to support simpler queries.

## Cost

There's no direct cost for creating or maintaining a workspace. You're charged for the data you ingest into the workspace and for data retention, based on each table's table plan.

For information on pricing, see Azure Monitor pricing. For guidance on how to reduce your costs, see Azure Monitor best practices - Cost management. If you're using your Log Analytics workspace with services other than Azure Monitor, see the documentation for those services for pricing information.


# 1.3 Exercise - Create a Log Analytics Workspace

In this lab, learn how to create a Log Analytics workspace to collect data from Azure resources in your subscription, on-premises computers monitored by System Center Operations Manager, device collections from Configuration Manager, diagnostics or log data from Azure Storage.

> **Note**
> 
> To complete this lab, you will need an **Azure subscription**.

Launch the exercise and follow the instructions.

> **Tip**
> 
> To continue your learning journey, open the exercise in a new browser tab or window while staying on this page. To do this, right-click the Launch Exercise button and select Open link in new tab or Open link in new window.


# 1.4 Module Assessment

Choose the best response for each question.

## Check Your Knowledge

### 1. What is the purpose of creating a Log Analytics workspace for Microsoft Defender for Cloud?

- [ ] To store and analyze security logs and telemetry data ✅
- [ ] To manage virtual machine resources in Azure
- [ ] To deploy and manage virtual networks in Azure

**Answer: To store and analyze security logs and telemetry data**

*Explanation: A Log Analytics workspace serves as a centralized data store for collecting, storing, and analyzing security logs and telemetry data from Microsoft Defender for Cloud and other Azure resources.*

### 2. Which service is used to create a Log Analytics workspace in Azure?

- [ ] Defender for Cloud
- [ ] Azure Log Analytics
- [ ] Azure Monitor ✅

**Answer: Azure Monitor**

*Explanation: Log Analytics workspaces are created and managed through Azure Monitor, which is the comprehensive monitoring service in Azure that includes Log Analytics functionality.*

### 3. What type of data can be collected and analyzed in a Log Analytics workspace?

- [ ] Virtual machine performance metrics ✅
- [ ] Security event logs ✅
- [ ] Application code repositories

**Answer: Both Virtual machine performance metrics and Security event logs**

*Explanation: Log Analytics workspaces can collect and analyze various types of data including performance metrics, security event logs, application logs, and telemetry data. However, it doesn't store application code repositories.*

### 4. How can organizations access and query data stored in a Log Analytics workspace?

- [ ] Through the Azure portal only
- [ ] Using the Log Analytics Query Language (KQL) ✅
- [ ] By exporting data to external storage

**Answer: Using the Log Analytics Query Language (KQL)**

*Explanation: While data can be accessed through the Azure portal, the primary method for querying and analyzing data in Log Analytics is through KQL (Kusto Query Language), which provides powerful query capabilities for log data analysis.*


# Summary


In this module, you learned to create and configure an Azure Log Analytics workspace for Microsoft Defender for Cloud, enabling centralized logging, data analysis, custom queries, alerts, and integration with other Azure services for enhanced threat detection.

## Key Takeaways

Throughout this module, you have gained knowledge and skills in:

- **Creating Log Analytics workspaces** - Understanding how to set up a centralized data store for security logs and telemetry
- **Configuring data collection** - Learning to collect data from Azure and non-Azure resources for comprehensive monitoring
- **Writing custom queries** - Using KQL (Kusto Query Language) to analyze security data and extract meaningful insights
- **Setting up alerts** - Creating proactive monitoring and alerting mechanisms for threat detection
- **Service integration** - Connecting Log Analytics with Microsoft Defender for Cloud and other Azure services for enhanced security operations

These capabilities enable organizations to implement robust security monitoring, improve incident response times, and maintain better visibility across their hybrid cloud environments.




#### References:

- Design a Log Analytics workspace architecture, https://learn.microsoft.com/en-us/azure/azure-monitor/logs/workspace-design
- 

