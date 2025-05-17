

# Deploy and configure Azure Monitor
https://learn.microsoft.com/en-us/training/paths/deploy-configure-azure-monitor/

In this learning path, you practice implementing Azure Monitor to collect, analyze and act on monitoring telemetry from Azure environments. You learn to configure and interpret monitoring for virtual machines, networking, and web applications.

#### Prerequisites
- Understand the basic functionality of Azure Monitor and Log Analytics workspaces.


# 1 Create and configure a Log Analytics workspace

Understand how to create and configure a Log Analytics workspace, and how to configure data retention and health status alerts for the workspace.


## 1.1 Introduction

Azure Monitor collects log data and stores it in tables. Administrators use Log Analytics in the Azure portal to configure their input data sources and conduct queries for their Azure Monitor logs.

You are in IT Operations at Tailwind Traders. You're responsible for ensuring that the monitoring infrastructure that supports Tailwind Traders Azure workloads is appropriately configured. You need to configure Log Analytics workspaces so that only appropriate people have access to the workspace. You also must configure an appropriate data retention period for the workspace, and ensure that you receive notification if there's any degradation in workspace health.

#### Learning objectives
In this module, you learn how to:

- Create a Log Analytics workspace.
- Configure access to a Log Analytics workspace.
- Configure data retention for a Log Analytics workspace.
- Enable health status alerts for Log Analytics workspace.

#### Prerequisites
- Understand the basic functionality of Azure Monitor and Log Analytics workspaces.


## 1.2 Create a Log Analytics workspace

Azure Monitor Logs is a feature of Azure Monitor that collects and organizes log and performance data from monitored resources. A Log Analytics workspace is a unique environment for log data from Azure Monitor and other Azure services. Each workspace has its own data repository and configuration but might combine data from multiple services.

For example, a Log Analytics workspace allows you to collect data from:

- Azure resources in your subscription.
- Virtual machine agents.
- Application and performance usage data from Azure Monitor application insights.
- Diagnostics or log data from Azure Storage.
- All of this disparate data can be consolidated into a single workspace for analysis. A workspace has a unique workspace ID and resource ID. The workspace name must be unique for a given resource group. After you've created a workspace, configure data sources and solutions to store their data there.

To create a Log Analytics workspace, perform the following steps:

1. In the Azure portal, enter Log Analytics in the search box. As you begin typing, the list filters based on your input. Select Log Analytics workspaces.
2. Select Add.
3. Select a Subscription from the dropdown.
4. Use an existing Resource Group or create a new one.
5. Provide a name for the new Log Analytics workspace, such as DefaultLAWorkspace. This name must be unique per resource group.
6. Select an available Region.
7. Select Review + Create to review the settings. Then select Create to create the workspace. A default pricing tier of pay-as-you-go is applied. No charges will be incurred until you start collecting enough data.

Once you've configured the workspace and data is being logged, you can analyze it together using a sophisticated query language that's capable of quickly analyzing millions of records. You might start with a simple sample query that answers a common question, or perform sophisticated data analysis to identify critical patterns in your monitoring data. You can work with log queries and their results interactively using Log Analytics, use them in an alert rule to be proactively notified of issues, or visualize their results in a workbook or dashboard.


## 1.3 Configure access to Log Analytics workspaces

The data in a Log Analytics workspace that you can access is determined by a combination of the following factors:

- The settings on the workspace itself.
- The access to resources sending data to the workspace.
- The method used to access the workspace.

### Access mode
The access mode refers to how you access a Log Analytics workspace and defines the data you can access during the current session. The mode is determined according to the scope you select in Log Analytics.

There are two access modes

- Workspace-context: You can view all logs in the workspace for which you have permission. Queries in this mode are scoped to all data in tables that you have access to in the workspace. This access mode is used when logs are accessed with the workspace as the scope, such as when you select Logs on the Azure Monitor menu in the Azure portal. This mode is appropriate for administrators who need to configure data collection and users who need access to a wide variety of resources. When the workspace context is used, access is managed through Azure Role Based Access Control (RBAC).

- Resource-context: When you access the workspace for a particular resource, resource group, or subscription, such as when you select Logs from a resource menu in the Azure portal, you can view logs for only resources in all tables that you have access to. Queries in this mode are scoped to only data associated with that resource. This mode also enables granular Azure RBAC. Workspaces use a resource-context log model where every log record emitted by an Azure resource is automatically associated with this resource. This mode is appropriate for administrators of Azure resources being monitored. It allows them to focus on their resource without filtering. Records are only available in resource-context queries if they're associated with the relevant resource.

You can view the current workspace access control mode on the Overview page for the workspace in the Log Analytics workspace menu.

Screenshot of the Overview page of a Log Analytics workspace with the Access control mode setting highlighted.

You can switch which access control mode is being used by selecting the Properties page of the Log Analytics workspace, selecting Use resource or workspace permissions, and then selecting the appropriate permission.

Screenshot of the Properties page of a Log Analytics workspace with the Access control mode setting highlighted.

### Log Analytics RBAC roles
There are two built-in Log Analytics related RBAC roles. These are:

- Log Analytics Reader
- Log Analytics Contributor

### Log Analytics Reader

You can assign the Log Analytics Reader role at a particular scope to configure access to a Log Analytics workspace. Members of the Log Analytics Reader role can view all monitoring data and monitoring settings, including the configuration of Azure diagnostics on all Azure resources.

Members of the Log Analytics Reader role can:

- View and search all monitoring data.
- View monitoring settings, including viewing the configuration of Azure diagnostics on all Azure resources.

### Log Analytics Contributor

Members of the Log Analytics Contributor role can:

- Read all monitoring data granted by the Log Analytics Reader role.
- Edit monitoring settings for Azure resources, including:
-  Adding the VM extension to VMs.
-  Configuring Azure diagnostics on all Azure resources.
- Create and configure Automation accounts. Permission must be granted at the resource group or subscription level.
- Add and remove management solutions. Permission must be granted at the resource group or subscription level.
- Read storage account keys.
- Configure the collection of logs from Azure Storage.
- Configure data export rules.
- Run a search job.
- Restore archived logs.

### Log Analytics RBAC scopes

You can configure Log Analytics role access at the following scopes:

- Subscription: Access to all workspaces in the subscription
- Resource group: Access to all workspaces in the resource group
- Resource: Access to only the specified workspace

For example, if you assign the Log Analytics Reader role at the resource group level, the user assigned the role will have Log Analytics Reader level access to all Log Analytics workspaces in that specific resource group.

To configure Azure RBAC permissions at the workspace scope, perform the following steps:

1) Navigate to Log analytics workspace in the Azure portal.
2) Select Access control (IAM).
3) Add a role assignment.
4) Select Log Analytics Reader or Log Analytics Contributor and click Next.
5) Add the security principal to which you wish to assign the role and click Next.
6) Click Save.


## 1.4 Configure Log Analytics data retention

Retention policies define when to remove or archive data in a Log Analytics workspace. Archiving lets you keep older, less used data in your workspace at a reduced cost. To configure data retention and archiving, you must have at least contributor rights on the Log Analytics workspace.

### Retention and archiving

During the interactive retention period, data is available for monitoring, troubleshooting, and analytics. When you no longer use the logs, but still need to keep the data for compliance or occasional investigation, you can archive the logs to reduce costs.

Archived data stays in the same table, alongside the data that's available for interactive queries. When you set a total retention period that's longer than the interactive retention period, Log Analytics automatically archives the relevant data immediately at the end of the retention period.

When you shorten an existing retention policy, Azure Monitor waits 30 days before removing the data, so you can revert the change and prevent data loss in the event of an error in configuration. You can purge data immediately when required.

When you increase the retention policy, the new retention period applies to all data that's already been ingested into the table and hasn't yet been purged or removed.

If you change the archive settings on a table with existing data, the relevant data in the table is also affected immediately. For example, you might have an existing table with 180 days of interactive retention and no archive period. You decide to change the retention policy to 90 days of interactive retention without changing the total retention period of 180 days. Log Analytics immediately archives any data that's older than 90 days and none of the data is deleted.

### Configuring default Log Analytics Workspace retention policy

You can set the workspace default retention policy in the Azure portal to 30, 31, 60, 90, 120, 180, 270, 365, 550, and 730 days. You can set a different policy for specific tables by configuring the retention and archive policy at the table level. If you're on the free tier, you'll need to upgrade to the paid tier to change the data retention period.

To set the default workspace retention policy:

1) From the Log Analytics workspaces menu in the Azure portal, select your workspace.
2) Select Usage and estimated costs in the left pane.
3) Select Data Retention at the top of the page.
4) Adjust the slider to increase or decrease the number of days, and then select OK.

### Configure retention and archive policies by table

By default, all tables in your workspace inherit the workspace's interactive retention setting and have no archive policy. You can modify the retention and archive policies of individual tables, except for workspaces in the legacy Free Trial pricing tier. The Analytics log data plan includes 30 days of interactive retention. You can increase the interactive retention period to up to 730 days though this will increase costs.

To set the retention and archive duration for a table in the Azure portal:

1) From the Log Analytics workspaces menu, select Tables. The Tables screen lists all the tables in the workspace.
2) Select the context menu for the table you want to configure and select Manage table.
3) Configure the retention and archive duration in the Data retention settings section of the table configuration screen.


## 1.5 Configure Log Analytics health status alerts

Azure Service Health monitors the health of your cloud resources, including Log Analytics workspaces. When a Log Analytics workspace is healthy, data you collect from resources in your IT environment is available for querying and analysis in a relatively short period of time, measured as latency. When Azure Service Health detects average latency in your Log Analytics workspace, the workspace resource health status is Available.

To enable recommended alert rules:

1) In the Azure portal, navigate to the Log Analytics workspace. Under Monitoring, select the Alerts section and then under Enable recommended alert rules click View + enable.
2) This will bring up the Enable recommended alert rules page.
Screenshot of the Properties page of the Enable recommended alert rules page in a Log Analytics workspace.

3) In the Alert me if section, select all the rules you want to enable.
4) In the Notify me by section, select the way you want to be notified if an alert is triggered.
5) Select Use an existing action group, and enter the details of the existing action group if you want to use an action group that already exists.
6) Select Enable.

If you want to create a new action group, you will perform the following steps before setting up the alert rules:

1) In the Azure portal, navigate to the Azure Monitor page.
2) In the navigation menu, select Alerts.
3) In the toolbar, select Action groups.
4) Select +Create.
5) Step through the Create action group wizard.
6) On the Notifications page, set the Notification type to Email/SMS message/Push/Voice and set Email to alerts@contoso.com.

If you want to create a new alert rule, perform the following steps:

1) In the Azure portal, navigate to the Log Analytics workspace. Under Monitoring, select the Alerts section. On the menu bar click the Create drop down and then click Alert rule.
2) On the Condition page select Resource Health and then click Apply. Once you select Resource Health, the rule triggers alerts for all status changes in all Log Analytics workspaces in the subscription by default. If necessary, you can edit and modify the scope and condition at this stage.
3) On the Actions page either select an existing action group or create a new action group.
4) On the Details page, specify the Resource Group, Alert rule name, and a description.
5) Click Review and Create.


## 1.6 Module assessment

Answer the following questions

Choose the best response for each of the following questions.


1. Which Log Analytics workspace mode should be chosen in order to allow security principals to only view logs in the workspace to which they have permission irrespective of whether that log belongs to an IaaS Virtual Machine, Azure Web App, or Azure Storage?

- Workspace context
- Resource context
- Access control mode

2. An Azure subscription contains multiple Log Analytics workspace in a resource group named LogStores. Which Log Analytics RBAC role should be assigned in order to allow a security principal to be able to restore archived Log Analytics Workspace logs?

- Backup Operator
- Log Analytics Reader
- Log Analytics Contributor

3. What is the maximum value that can be configured for a default Log Analytics Workspace retention policy?

- 550 Days
- 730 Days
- 900 Days

## Module Assessment Answers

### Question 1
**Which Log Analytics workspace mode should be chosen in order to allow security principals to only view logs in the workspace to which they have permission irrespective of whether that log belongs to an IaaS Virtual Machine, Azure Web App, or Azure Storage?**

The correct answer is: **Resource context**

Resource context mode enables granular permission control, allowing security principals to view only logs for resources they have specific permissions to access, regardless of whether those resources are VMs, Web Apps, or Storage accounts.

### Question 2
**An Azure subscription contains multiple Log Analytics workspace in a resource group named LogStores. Which Log Analytics RBAC role should be assigned in order to allow a security principal to be able to restore archived Log Analytics Workspace logs?**

The correct answer is: **Log Analytics Contributor**

The Log Analytics Contributor role provides the necessary permissions to manage Log Analytics workspaces, including the ability to restore archived logs. Neither Backup Operator nor Log Analytics Reader roles have sufficient permissions for this task.

### Question 3
**What is the maximum value that can be configured for a default Log Analytics Workspace retention policy?**

The correct answer is: **730 Days**

Azure Log Analytics allows data retention policies to be configured for up to 730 days (2 years) for the default retention policy. The 550 and 900 days options are incorrect.



## 1.7 Summary

Azure Monitor collects log data and stores it in tables. Administrators use Log Analytics in the Azure portal to configure their input data sources and conduct queries for their Azure Monitor logs. In this module you learned how to create a Log analytics workspace, how to configure access to the workspace including the details of the built-in Log Analytics RBAC roles, how to configure data retention for a Log Analytics workspace as well as how to configure Health Status Alerts for a Log Analytics Workspace.

### Learn more
You can learn more by reviewing the following documents:

- Log Analytics workspace overview, https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview?source=recommendations
- Create a Log Analytics workspace, https://learn.microsoft.com/en-us/azure/azure-monitor/logs/quick-create-workspace?tabs=azure-portal
- Manage access to Log Analytics workspaces, https://learn.microsoft.com/en-us/azure/azure-monitor/logs/manage-access?tabs=portal
- Configure data retention and archive policies in Azure Monitor Logs, https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-retention-configure?tabs=portal-3%2Cportal-1%2Cportal-2
- Set daily cap on Log Analytics workspace, https://learn.microsoft.com/en-us/azure/azure-monitor/logs/daily-cap
- Monitor Log Analytics workspace health, https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-health



# 2 Configure monitoring for applications

Understand how to monitor the performance of your applications and how to collect and analyze the appropriate telemetry to improve application performance.


# 2.1 Introduction

Azure Monitor is a service in Azure that provides performance and availability monitoring for applications and services in Azure, other cloud environments, or on-premises environments. You are in IT Operations at Tailwind Traders. Part of your responsibilities include collaborating with the application developers in your organization. You need to be able to collect the appropriate log, performance, and error data generated by running their applications. As Tailwind Traders already has Azure Monitor in place, you decide that enabling Application Insights would be an ideal solution because it allows you to detect performance anomalies in those applications. Additionally, Application Insights provides you with powerful analytics tools so that you can more easily diagnose issues and better understand how your applications are used.

#### Learning objectives

In this module you learn how to:

- Describe how Application Insights is used to monitor application performance.
- Distinguish between the different Application Insights sampling rates.
- Describe Azure diagnostic settings and resource logs.
- Leverage Azure SQL Insights to improve performance of Azure SQL database applications.

#### Prerequisites
- Understand the basic functionality of Azure Monitor and Log Analytics workspaces.



## 2.2 Understand Application Insights

Application Insights is an extension of Azure Monitor and provides Application Performance Monitoring (also known as APM) features. APM tools are useful for monitoring applications from development, through test, and into production in the following ways:

- Proactively understand how an application is performing.
- Reactively review application execution data to determine the cause of an incident.

In addition to collecting metrics and application telemetry data, which describe application activities and health, Application Insights can also be used to collect and store application trace logging data.

The log trace is associated with other telemetry to give a detailed view of the activity. Adding trace logging to existing apps only requires providing a destination for the logs; the logging framework rarely needs to be changed.

Screenshot of the Application Insights dashboard, displaying categories of metrics collected for web app usage.

## What Application Insights monitors

Application Insights collects metrics and application telemetry data, which describe application activities and health, as well as trace logging data.

- Request rates, response times, and failure rates – Identify which pages are most popular, at what times of day, and where your users are. See which pages perform best. If your response times and failure rates go high when there are more requests, then you may have a resourcing problem.
- Dependency rates, response times, and failure rates – Determine whether external services are slowing you down.
- Exceptions – Analyze the aggregated statistics, or pick specific instances and drill into the stack trace and related requests. Both server and browser exceptions are reported.
- Page views and load performance – reported by your users' browsers.
- AJAX calls from web pages – rates, response times, and failure rates.
- User and session counts.
- Performance counters from your Windows or Linux server machines, such as CPU, memory, and network usage.
- Host diagnostics from Docker or Azure.
- Diagnostic trace logs from your app – so that you can correlate trace events with requests.
- Custom events and metrics that you write yourself in the client or server code, to track business events such as items sold, or games won.

There are several ways to get started monitoring and analyzing app performance:

- At run time – instrument your web app on the server. Ideal for applications already deployed. Avoids any update to the code.
- At development time – add Application Insights to your code. Allows you to customize telemetry collection and send more telemetry.
- Instrument your web pages for page view, AJAX, and other client-side telemetry.
- Analyze mobile app usage by integrating with Visual Studio App Center.
- Availability tests - ping your website regularly from our servers.

### Metric types
Application Insights log-based metrics let you analyze the health of your monitored apps, create powerful dashboards, and configure alerts. There are two kinds of metrics:

- Log-based metrics behind the scene are translated into Kusto queries from stored events.
- Standard metrics are stored as pre-aggregated time series.

Since standard metrics are pre-aggregated during collection, they have better performance at query time. Standard metrics are a better choice for dashboarding and in real-time alerting. The log-based metrics have more dimensions, which makes them the superior option for data analysis and ad-hoc diagnostics. Use the namespace selector to switch between log-based and standard metrics in metrics explorer.

### Log-based metrics
Developers can use the SDK to send events manually (by writing code that explicitly invokes the SDK) or they can rely on the automatic collection of events from auto-instrumentation. In either case, the Application Insights backend stores all collected events as logs, and the Application Insights blades in the Azure portal act as an analytical and diagnostic tool for visualizing event-based data from logs.

Using logs to retain a complete set of events can bring great analytical and diagnostic value. For example, you can get an exact count of requests to a particular URL with the number of distinct users who made these calls. Or you can get detailed diagnostic traces, including exceptions and dependency calls for any user session. Having this type of information can significantly improve visibility into the application health and usage, allowing to cut down the time necessary to diagnose issues with an app.

At the same time, collecting a complete set of events may be impractical (or even impossible) for applications that generate a large volume of telemetry. For situations when the volume of events is too high, Application Insights implements several telemetry volume reduction techniques, such as sampling and filtering that reduces the number of collected and stored events. Unfortunately, lowering the number of stored events also lowers the accuracy of the metrics that, behind the scenes, must perform query-time aggregations of the events stored in logs.

### Pre-aggregated metrics
Pre-aggregated metrics aren't stored as individual events with lots of properties. Instead, they're stored as pre-aggregated time series, and only with key dimensions. This makes the new metrics superior at query time: retrieving data happens faster and requires less compute power. This enables new scenarios such as near real-time alerting on dimensions of metrics, more responsive dashboards, and more.

The current SDKs (Application Insights 2.7 SDK or later for .NET) pre-aggregate metrics during collection. This applies to standard metrics sent by default, so the accuracy isn't affected by sampling or filtering. It also applies to custom metrics sent using GetMetric resulting in less data ingestion and lower cost.

For the SDKs that don't implement pre-aggregation the Application Insights backend still populates the new metrics by aggregating the events received by the Application Insights event collection endpoint. While you will not benefit from the reduced volume of data transmitted over the wire, you can still use the pre-aggregated metrics and experience better performance and support of the near real-time dimensional alerting with SDKs that don't pre-aggregate metrics during collection.

It's worth mentioning that the collection endpoint pre-aggregates events before ingestion sampling, which means that ingestion sampling will never impact the accuracy of pre-aggregated metrics, regardless of the SDK version you use with your application.



### 2.3 Application Insights sampling

Sampling is a feature in Application Insights that allows you to reduce telemetry traffic, data costs, and storage costs, while preserving a statistically correct analysis of application data. Sampling also helps you avoid Application Insights throttling your telemetry. The sampling filter selects items that are related, so that you can navigate between items when you're doing diagnostic investigations.

In general, for most small and medium size applications you don't need sampling. The most useful diagnostic information and most accurate statistics are obtained by collecting data on all your user activities.

The main advantages of sampling are:

- Application Insights service drops ("throttles") data points when your app sends a high rate of telemetry in a short time interval. Sampling reduces the likelihood that your application sees throttling occur.
- Allows you to keep within the quota of data points for your pricing tier.
- Allows you to reduce network traffic from the collection of telemetry.

### How sampling works

The sampling algorithm decides which telemetry items to drop, and which ones to keep. It is true whether sampling is done by the SDK or in the Application Insights service. The sampling decision is based on several rules that aim to preserve all interrelated data points intact, maintaining a diagnostic experience in Application Insights that is actionable and reliable even with a reduced data set. For example, if your app has a failed request included in a sample, the extra telemetry items (such as exception and traces logged for this request) are retained. Sampling either keeps or drops them all together. As a result, when you look at the request details in Application Insights, you can always see the request along with its associated telemetry items.

The sampling decision is based on the operation ID of the request, which means that all telemetry items belonging to a particular operation are either preserved or dropped. For the telemetry items that don't have an operation ID set (such as telemetry items reported from asynchronous threads with no HTTP context) sampling simply captures a percentage of telemetry items of each type.

When presenting telemetry back to you, the Application Insights service adjusts the metrics by the same sampling percentage that was used at the time of collection, to compensate for the missing data points. So, when looking at the telemetry in Application Insights, the users are seeing statistically correct approximations that are close to the real numbers.

The accuracy of the approximation largely depends on the configured sampling percentage. Also, the accuracy increases for applications that handle a large volume of similar requests from lots of users. On the other hand, for applications that don't work with a significant load, sampling isn't needed as these applications can usually send all their telemetry while staying within the quota, without causing data loss from throttling.

When metric counts are presented in the portal, they're renormalized to take into account sampling. Doing so minimizes any effect on the statistics.

### Sampling types

There are three different sampling methods:

- Adaptive sampling automatically adjusts the volume of telemetry sent from the SDK in your ASP.NET/ASP.NET Core app, and from Azure Functions. This is the default sampling when you use the ASP.NET or ASP.NET Core SDK. Adaptive sampling is currently only available for ASP.NET/ASP.NET Core server-side telemetry, and for Azure Functions.
- Fixed-rate sampling reduces the volume of telemetry sent from both your ASP.NET or ASP.NET Core or Java server and from your users' browsers. You set the rate. The client and server will synchronize their sampling so that, in Search, you can navigate between related page views and requests.
- Ingestion sampling happens at the Application Insights service endpoint. It discards some of the telemetry that arrives from your app, at a sampling rate that you set. It doesn't reduce telemetry traffic sent from your app, but helps you keep within your monthly quota. The main advantage of ingestion sampling is that you can set the sampling rate without redeploying your app. Ingestion sampling works uniformly for all servers and clients, but it doesn't apply when any other types of sampling are in operation.

If adaptive or fixed rate sampling methods are enabled for a telemetry type, ingestion sampling is disabled for that telemetry. However, telemetry types that are excluded from sampling at the SDK level will still be subject to ingestion sampling at the rate set in the portal.



## 2.4 Diagnostic settings and resource logs

Platform logs provide detailed diagnostic and auditing information for Azure resources and the Azure platform they depend on. Platform logs are automatically generated.

The following platform logs are available within Azure:

- Resource logs. Resource logs provide an insight into operations that were performed within an Azure resource. This is known as the data plane. Examples include getting a secret from a key vault, or making a request to a database. The contents of resource logs varies according to the Azure service and resource type. Resource logs were previously referred to as diagnostic logs.
- Activity logs. Activity logs provide an insight into the operations performed on each Azure resource in the subscription from the outside, known as the management plane, in addition to updates on Service Health events. Use the Activity log to determine what, who, and when for any write operation (PUT, POST, DELETE) executed on the resources in your subscription. There's a single activity log for each Azure subscription.
- Microsoft Entra ID logs. Entra ID logs contain the history of sign-in activity and an audit trail of changes made in Entra ID for a particular tenant. (Previously termed the Azure Active Directory logs.)

### Viewing platform logs
There are different options for viewing and analyzing the different Azure platform logs:

- View the activity log using the Azure portal and access events from PowerShell and the Azure CLI. See View the activity log for details.
- View Azure AD security and activity reports in the Azure portal. See What are Azure AD reports? for details.
- Resource logs are automatically generated by supported Azure resources. You must create a diagnostic setting for the resource to store and view the log.

### Diagnostic settings
Resource logs must have a diagnostic setting to be viewed. Create a diagnostic setting to send platform logs to one of the following destinations for analysis or other purposes.

- Log Analytics workspace. Analyze the logs of all your Azure resources together and take advantage of all the features available to Azure Monitor Logs including log queries and log alerts. Pin the results of a log query to an Azure dashboard or include it in a workbook as part of an interactive report.
- Event hub. Send platform log data outside of Azure, for example, to a third-party SIEM or custom telemetry platform via Event hubs.
- Azure Storage. Archive the logs to Azure storage for audit or backup.

Platform metrics are sent automatically to Azure Monitor Metrics by default and without configuration. Platform logs provide detailed diagnostic and auditing information for Azure resources and the Azure platform they depend on:

- Resource logs aren't collected until they're routed to a destination.
- Activity logs exist on their own but can be routed to other locations.

Each Azure resource requires its own diagnostic setting, which defines the following criteria:

- Sources: The type of metric and log data to send to the destinations defined in the setting. The available types vary by resource type.
- Destinations: One or more destinations to send to.

A single diagnostic setting can define no more than one of each of the destinations. If you want to send data to more than one of a particular destination type (for example, two different Log Analytics workspaces), create multiple settings. Each resource can have up to five diagnostic settings.

There are three sources for diagnostic information:
- Metrics
- Resource Logs
- Activity logs
The AllMetrics setting routes a resource's platform metrics to other destinations. This option might not be present for all resource providers.

### Resource logs
With logs, you can select the log categories you want to route individually or choose a category group. You can use category groups to dynamically collect resource logs based on predefined groupings instead of selecting individual log categories. Microsoft defines the groupings to help monitor specific use cases across all Azure services. Category groups don't apply to all metric resource providers.

You can use category groups to dynamically collect resource logs based on predefined groupings instead of selecting individual log categories. Use these groupings to help monitor specific use cases across all Azure services.

When you use category groups, you can no longer:
- Select individual resource logs based on individual category types.
- Apply retention settings to logs sent to Azure Storage.
There are two category groups:

- All. Every resource log offered by the resource.
- Audit. All resource logs that record customer interactions with data or the settings of the service. Audit logs are an attempt by each resource provider to provide the most relevant audit data, but may not be considered sufficient from an auditing standards perspective.

The Audit category is a subset of All, but the Azure portal and REST API consider them separate settings. Selecting All does collect all audit logs regardless of if the Audit category is also selected.

## Activity log

The Azure Monitor activity log is a platform log in Azure that provides insight into subscription-level events. The activity log includes information like when a resource is modified, or a virtual machine is started. You can view the activity log in the Azure portal or retrieve entries with PowerShell and the Azure CLI.

For more functionality, create a diagnostic setting to send the activity log to one or more of these locations for the following reasons:

- Azure Monitor Logs – for more complex querying and alerting and for longer retention, up to two years.
- Azure Event Hubs – to forward outside of Azure.
- Azure Storage – for cheaper, long-term archiving.

You can access the activity log from most menus in the Azure portal. The menu that you open it from determines its initial filter. If you open it from the Monitor menu, the only filter is on the subscription. If you open it from a resource's menu, the filter is set to that resource. You can always change the filter to view all other entries. Activity log events are retained in Azure for 90 days and then deleted.

You can send the activity log to a Log Analytics workspace to enable the Azure Monitor Logs feature, where you:

- Correlate activity log data with other monitoring data collected by Azure Monitor.
- Consolidate log entries from multiple Azure subscriptions and tenants into one location for analysis together.
- Use log queries to perform complex analysis and gain deep insights on activity log entries.
- Use log alerts with Activity entries for more complex alerting logic.
- Store activity log entries for longer than the activity log retention period.

To send the activity log to a Log Analytics workspace select Export Activity Logs from the Activity Logs page. You can send the activity log from any single subscription to up to five workspaces. Activity log data in a Log Analytics workspace is stored in a table called AzureActivity that you can retrieve with a log query in Log Analytics. The structure of this table varies depending on the category of the log entry.

Send the activity log to an Azure Storage account if you want to retain your log data longer than 90 days for audit, static analysis, or back up. When you send the activity log to Azure, a storage container is created in the storage account as soon as an event occurs.


## 2.5 Azure SQL Insights

SQL Insights allows you to analyze your queries, and tune performance of any product in the Azure SQL family. SQL Insights allows you to customize telemetry collection and frequency. SQL Insights also allows you to combine data from multiple sources into a single monitoring experience.

SQL Insights performs all monitoring remotely. Monitoring agents are hosted on dedicated virtual machines that connect to your SQL resources to remotely gather data. SQL Insights remote data collection leverages Azure SQL dynamic management views. Data gathered by SQL Insights is stored in Azure Monitor Logs to enable easy aggregation, filtering, and trend analysis. You can view the collected data from the SQL Insights workbook template, or you can delve directly into the data by using log queries.

SQL Insights is built on top of the Azure Monitor platform, which provides native alerting and out-of-the-box visualizations. This also allows you to retain a set of metrics over time so you can investigate performance issues that you may have encountered in the past.

SQL Insights allows you to configure which telemetry data to collect, the frequency of collection, and how long you want to store that data. Database activity and the settings that you've set in your monitoring profiles determine the amount of data being collected, which impacts the cost of the service.

### Azure SQL Insights and Azure SQL Analytics

Both Azure SQL Insights, Azure SQL Analytics, and Azure diagnostic telemetry provide information on how your Azure SQL databases function.

- Azure SQL Insights is a project inside Azure Monitor that can provide advanced insights into Azure SQL database activity. It's deployed via a customer-managed VM using Telegraf as a collection agent that connects to SQL sources, collects data, and moves data into Log Analytics.
- Azure SQL Analytics also requires Log Analytics to provide advanced insights into Azure SQL database activity.
- Azure diagnostic telemetry is a separate, streaming source of data for Azure SQL Database and Azure SQL Managed Instance. Separate from Azure SQL Insights, SQLInsights is a log inside Intelligent Insights, and is one of several packages of telemetry emitted by Azure diagnostic settings. Diagnostic settings are a feature that contains Resource Log categories (formerly known as Diagnostic Logs).
Azure SQL Analytics consumes the resource logs coming from the diagnostic telemetry (configurable under Diagnostic Settings in the Azure portal), while Azure SQL Insights uses a different pipeline to collect Azure SQL telemetry.

The following diagram details all the database engine, platform metrics, resource logs, and Azure activity logs generated by Azure SQL products, how they're processed, and how they can be surfaced for analysis.

Diagram showing how SQL Insights is used in conjunction with Azure SQL Analytics to collect and analyze data.

You can quickly monitor various Azure SQL related resource metrics in the Azure portal in the Metrics view. These metrics enable you to see if a database is approaching the limits of CPU, memory, IO, or storage resources. High DTU, CPU or IO utilization may indicate that your workload needs more resources. It might also indicate that queries need to be optimized.

### Database advisors
Azure SQL Database provides several Database Advisors to provide intelligent performance tuning recommendations and automatic tuning options to improve performance.

The Query Performance Insight page shows you details about the queries responsible for the most CPU and IO usage for single and pooled databases.

Query Performance Insight is available in the Azure portal in the Overview pane of your Azure SQL Database under "Intelligent Performance." Use the automatically collected information to identify queries and begin optimizing your workload performance.
You can also configure automatic tuning to implement these recommendations automatically, such as forcing a query execution plan to prevent regression, or creating and dropping nonclustered indexes based on workload patterns. Automatic tuning is also available in the Azure portal in the Overview pane of your Azure SQL Database under "Intelligent Performance."


## 2.6 Module assessment

Answer the following questions
Choose the best response for each of the following questions.


1. Which of the following types of platform log would store an event related to a secret key being retrieved from Azure Key Vault by an application?
- Resource Logs
- Activity logs
- Microsoft Entra ID logs

2. Which of the following Application Insights log-based metrics should be chosen for the best performance at query time?
- Log-based metrics
- Standard metrics
- Platform metrics

3. Which of the following Application Insights sampling methods reduces the volume of telemetry sent from the server and user's browsers?
- Adaptive sampling
- Ingestion sampling
- Fixed-rate sampling


# Module Assessment Answers

## Question 1
**Which of the following types of platform log would store an event related to a secret key being retrieved from Azure Key Vault by an application?**

The correct answer is: **Activity logs**

Activity logs in Azure record all operations performed on resources at the control plane level, including retrieval of secrets from Key Vault. They track "who did what and when" for operations that affect Azure resources, including authentication events and secret access operations.

## Question 2
**Which of the following Application Insights log-based metrics should be chosen for the best performance at query time?**

The correct answer is: **Standard metrics**

Standard metrics in Application Insights offer the best query performance because they're pre-aggregated during collection, optimized for storage and retrieval, and don't require complex query processing at runtime. This makes them significantly faster than log-based metrics, especially for large datasets.

## Question 3
**Which of the following Application Insights sampling methods reduces the volume of telemetry sent from the server and user's browsers?**

The correct answer is: **Adaptive sampling**

Adaptive sampling dynamically adjusts the amount of telemetry collected based on the current volume, reducing data sent from both the server and users' browsers. It maintains statistically representative sampling while intelligently reducing traffic during high-volume periods, unlike fixed-rate sampling (which uses a constant percentage) or ingestion sampling (which only filters data after it has already been sent to Application Insights).


## 2.7 Summary

In this module, you learned how to monitor the performance of your applications and how to collect and analyze the appropriate telemetry to improve application performance. You learned how to create an Application Insights resource, and how to configure data sampling rate, anomaly detection, diagnostic and Azure SQL Insights.

You can learn more by reviewing the following documents:

- Sampling in Application Insights, https://learn.microsoft.com/en-us/previous-versions/azure/azure-monitor/app/sampling
- Monitor app performance, https://learn.microsoft.com/en-us/training/modules/monitor-app-performance/
- Monitor your SQL deployments with SQL Insights,
- Overview of Azure platform logs
- Azure resource log
- Diagnostic settings in Azure Monitor
