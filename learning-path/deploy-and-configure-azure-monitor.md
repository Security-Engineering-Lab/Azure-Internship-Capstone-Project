
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


### Module Assessment Answers

### Question 1
**Which of the following types of platform log would store an event related to a secret key being retrieved from Azure Key Vault by an application?**

The correct answer is: **Activity logs**

Activity logs in Azure record all operations performed on resources at the control plane level, including retrieval of secrets from Key Vault. They track "who did what and when" for operations that affect Azure resources, including authentication events and secret access operations.

### Question 2
**Which of the following Application Insights log-based metrics should be chosen for the best performance at query time?**

The correct answer is: **Standard metrics**

Standard metrics in Application Insights offer the best query performance because they're pre-aggregated during collection, optimized for storage and retrieval, and don't require complex query processing at runtime. This makes them significantly faster than log-based metrics, especially for large datasets.

### Question 3
**Which of the following Application Insights sampling methods reduces the volume of telemetry sent from the server and user's browsers?**

The correct answer is: **Adaptive sampling**

Adaptive sampling dynamically adjusts the amount of telemetry collected based on the current volume, reducing data sent from both the server and users' browsers. It maintains statistically representative sampling while intelligently reducing traffic during high-volume periods, unlike fixed-rate sampling (which uses a constant percentage) or ingestion sampling (which only filters data after it has already been sent to Application Insights).


## 2.7 Summary

In this module, you learned how to monitor the performance of your applications and how to collect and analyze the appropriate telemetry to improve application performance. You learned how to create an Application Insights resource, and how to configure data sampling rate, anomaly detection, diagnostic and Azure SQL Insights.

You can learn more by reviewing the following documents:

- Sampling in Application Insights, https://learn.microsoft.com/en-us/previous-versions/azure/azure-monitor/app/sampling
- Monitor app performance, https://learn.microsoft.com/en-us/training/modules/monitor-app-performance/
- Monitor your SQL deployments with SQL Insights, https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-insights-overview?view=azuresql
- Overview of Azure platform logs, https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/data-sources
- Azure resource log, https://learn.microsoft.com/en-us/azure/azure-monitor/platform/resource-logs
- Diagnostic settings in Azure Monitor, https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings


# 3 Configure monitoring for virtual machines

Understand how to deploy and configure Azure Monitor Agent on IaaS VMs and how to enable VM Insights and Data Collection Rules to monitor performance and application telemetry.


## 3.1 Introduction

You are in IT Operations at Tailwind Traders. You're responsible for managing and monitoring a fleet of IaaS VMs deployed in Azure running a mixture of Windows Server and Linux operating systems. You want to ensure that the performance and applications of these virtual machines are tracked and visible in the Azure Portal.

### Learning objectives
In this module, you learn how to:

- Describe how the Azure Monitor Agent can be deployed to IaaS Virtual Machines.
- Explain VM Insights and how to use it to monitor IaaS VM performance.
- Enable data collection rules to collect operating system and application logs.

#### Prerequisites:
- Understand the basic functionality of Azure Monitor and Log Analytics workspaces.


## 3.2 Deploy Azure Monitor Agent to IaaS Virtual Machines

Azure Monitor for VMs enables you to monitor Virtual Machines that are hosted in Azure or server operating systems connected through Azure Arc. Azure Monitor for VMs supports the following operating systems:

- Windows Server 2012 R2 and later
- Windows Server 2008 R2 SP1 and later
- Ubuntu 14.04 LTS and later
- SUSE Linux Enterprise Server 12 SP2 and later
- Red Hat Enterprise Linux 6.7 and later

To collect logs and performance data from the guest operating system of the virtual machine, though, you must install the Azure Monitor Agent and have deployed a Log Analytics workspace.

###  Azure Monitor Agent

Azure Monitor Agent (AMA) collects monitoring data from the guest operating system of Azure and hybrid virtual machines and delivers it to Azure Monitor for use by features, insights, and other services, such as Microsoft Sentinel and Microsoft Defender for Cloud. Azure Monitor Agent replaces all of Azure Monitor's legacy monitoring agents including:

- Log Analytics Agent: Sends data to a Log Analytics workspace and supports monitoring solutions. This is fully consolidated into Azure Monitor agent.
- Telegraf agent: Sends data to Azure Monitor Metrics (Linux only). Only basic Telegraf plugins are supported today in Azure Monitor agent.
- Diagnostics extension: Sends data to Azure Monitor Metrics (Windows only), Azure Event Hubs, and Azure Storage. This is not consolidated yet.

### Installing the Azure Monitor Agent
Azure Monitor Agent is implemented as an Azure VM extension. The following prerequisites must be met prior to installing Azure Monitor Agent.

- Permissions: For methods other than using the Azure portal, you must have the following role assignments to install the agent:
Virtual Machine Contributor
Azure Connected Machine Resource Administrator
Any role that includes the action Microsoft.Resources/deployments/* (for example, Log Analytics Contributor.)
- Non-Azure: To install the agent on physical servers and virtual machines hosted outside of Azure (that is, on-premises) or in other clouds, you must install the Azure Arc Connected Machine agent.
Authentication: Managed identity must be enabled on Azure virtual machines. Both user-assigned and system-assigned managed identities are supported.
- Networking: If you use network firewalls, the Azure Resource Manager service tag must be enabled on the virtual network for the virtual machine. The virtual machine must also have access to the following HTTPS endpoints:
global.handler.control.monitor.azure.com
<virtual-machine-region-name>.handler.control.monitor.azure.com (example: westus.handler.control.monitor.azure.com)
<log-analytics-workspace-id>.ods.opinsights.azure.com (example: 12345a01-b1cd-1234-e1f2-1234567g8h99.ods.opinsights.azure.com)


It is important to note that once the agent is installed that Azure Monitor Agents don’t function without being associated with data collection rules. Those can be created manually or through using VM Insights.

You can install Azure Monitor Agent on Azure virtual machines using the az vm extension set –name AzureMonitorWindowsAgent or az vm extension set AzureMonitorLinuxAgent commands.

For example, to install Azure Monitor Agent using the system-assigned managed identity on a Windows Server IaaS VM use the command:

az vm extension set --name AzureMonitorWindowsAgent --publisher Microsoft.Azure.Monitor --ids <vm-resource-id> --enable-auto-upgrade true

To install Azure Monitor Agent using the system-assigned managed identity on a Linux IaaS VM use the command:

az vm extension set --name AzureMonitorLinuxAgent --publisher Microsoft.Azure.Monitor --ids <vm-resource-id> --enable-auto-upgrade true

Creating a data collection rule through the Azure portal automatically deploys the Azure Monitor Agent on an IaaS VM if it is not already deployed.

Microsoft recommends you enable Automatic Extension Upgrade when deploying the Azure Monitor Agent. You can enable Azure Policy to automatically deploy the Azure Monitor Agent and associate it with a data collection rule each time you deploy a new IaaS VM.



## 3.3 Monitor Performance with VM insights

VM insights provides a quick and easy method for getting started monitoring the client workloads on your virtual machines and virtual machine scale sets. It displays an inventory of your existing VMs and provides a guided experience to enable base monitoring for them. It also monitors the performance and health of your virtual machines and virtual machine scale sets by collecting data on their running processes and dependencies on other resources. VM insights monitors key operating system performance indicators related to processor, memory, network adapter, and disk utilization.

VM insights provides a set of predefined workbooks that allow you to view trending of collected performance data over time. You can view this data in a single VM from the virtual machine directly, or you can use Azure Monitor to deliver an aggregated view of multiple VMs.

VM insights includes a set of performance charts that target several key performance indicators to help you determine how well a virtual machine is performing. The charts show resource utilization over a period of time. You can use them to identify bottlenecks and anomalies. You can also switch to a perspective that lists each machine to view resource utilization based on the metric selected.

VM insights provides the following benefits beyond other features for monitoring VMs in Azure Monitor:

- Simplified onboarding of the Azure Monitor agent and the Dependency agent, so that you can monitor a virtual machine guest operating system and workloads.
- Pre-defined data collection rules that collect the most common set of performance data.
- Pre-defined trending performance charts and workbooks, so that you can analyze core performance metrics from the virtual machine's guest operating system.
- The Dependency map, which displays processes that run on each virtual machine and the interconnected components with other machines and external sources.
Screenshot showing Performance tab in VM Insights displaying data for a VM and the processes Dependency map for that VM.

### Enable VM insights

To enable VM Insights, select Insights from your virtual machine's menu in the Azure portal. If VM insights isn't enabled, you see a short description of it and an option to enable it.

Select Enable to open the Monitoring configuration pane. Leave the default option of Azure Monitor agent.

Enabling VM insights creates a default data collection rule that doesn't include collection of processes and dependencies. To enable this collection, select Create New to create a new data collection rule.

You will be asked to provide a Data collection rule name and then select Enable processes and dependencies (Map). You can't disable collection of guest performance because it's required for VM insights.

You can use the default Log Analytics workspace for the subscription unless you have another workspace that you want to use.

1) Select Create to create the new data collection rule.
2) Select Configure to start VM insights configuration.

### View VM performance

When the deployment completes, you see views on the Performance tab in VM insights with performance data for the machine. This data shows you the values of key guest metrics over time.

By default, the charts show the last 24 hours. By using the TimeRange selector, you can query for historical time ranges of up to 30 days to show past performance.

The following capacity utilization charts are available:

- CPU Utilization %: Defaults show the average and top 95th percentile.
- Available Memory: Defaults show the average, top 5th, and 10th percentile.
- Logical Disk Space Used %: Defaults show the average and 95th percentile.
- Logical Disk IOPS: Defaults show the average and 95th percentile.
- Logical Disk MB/s: Defaults show the average and 95th percentile.
- Max Logical Disk Used %: Defaults show the average and 95th percentile.
- Bytes Sent Rate: Defaults show the average bytes sent.
- Bytes Receive Rate: Defaults show the average bytes received.

Screenshot of the Performance tab in VM insights, displaying performance data for disk, CPU, memory, and disk IOPS.

# View dependencies

In VM insights, you can view discovered application components on Windows and Linux virtual machines (VMs) that run in Azure or your environment. You can view a map directly from a VM. You can also view a map from Azure Monitor to see the components across groups of VMs. This unit helps you to understand these two viewing methods and how to use the Map feature.

The Map feature visualizes the VM dependencies by discovering running processes that have:

- Active network connections between servers.
- Inbound and outbound connection latency.
- Ports across any TCP-connected architecture over a specified time range.

To access VM insights map directly from a VM:

1) In the Azure portal, select Virtual Machines.
2) From the list, select a VM. In the Monitoring section, select Insights.
3) Select the Map tab.

The map visualizes the VM's dependencies by discovering running process groups and processes that have active network connections over a specified time range.

By default, the map shows the last 30 minutes. If you want to see how dependencies looked in the past, you can query for historical time ranges of up to one hour. To run the query, use the TimeRange selector in the upper-left corner. You might run a query, for example, during an incident or to see the status before a change.

Screenshot of Map tab in VM Insights showing a visual representation of ContosoVM1's dependencies between running process groups and processes.

In Azure Monitor, the Map feature provides a global view of your VMs and their dependencies. To access the Map feature in Azure Monitor:

1) In the Azure portal, select Monitor.
2) In the Insights section, select Virtual Machines.
3) Select the Map tab.

If you have more than one Log Analytics workspace, choose the workspace that's enabled with the solution and that has VMs reporting to it.

The Group selector returns subscriptions, resource groups, computer groups, and virtual machine scale sets of computers that are related to the selected workspace. Your selection applies only to the Map feature and doesn't carry over to Performance or Health.



## 3.4 Configure data collection rules for IaaS VM logs

If you enable VM insights, the Azure Monitor agent is installed and starts sending a predefined set of performance data to Azure Monitor Logs. You can create additional data collection rules to collect events and other performance data.

Data collection rules (DCRs) define the data collection process in Azure Monitor. DCRs specify what data should be collected, how to transform that data, and where to send that data. Some DCRs will be created and managed by Azure Monitor to collect a specific set of data to enable insights and visualizations. You might also create your own DCRs to define the set of data required for other scenarios.

You can define a data collection rule to send data from multiple machines to multiple Log Analytics workspaces, including workspaces in a different region or tenant. Create the data collection rule in the same region as your Log Analytics workspace. You can send Windows event and Syslog data to Azure Monitor Logs only. You can send performance counters to both Azure Monitor Metrics and Azure Monitor Logs.

### Collect events and performance logs
To collect events and performance data, perform the following steps:

1) In the Azure portal, navigate to Azure Monitor.
2) On the Monitor menu, select Data Collection Rules.
3) Select Create to create a new data collection rule and associations.
4) Enter a Rule name and specify a Subscription, Resource Group, Region, and Platform Type:
- Region specifies where the DCR will be created. The virtual machines and their associations can be in any subscription or resource group in the tenant.
- Platform Type specifies the type of resources this rule can apply to. The Custom option allows for both Windows and Linux types.
5) On the Resources tab:
- Select + Add resources and associate resources to the data collection rule. Resources can be virtual machines, Virtual Machine Scale Sets, and Azure Arc for servers.
- Select Enable Data Collection Endpoints.
- Select a data collection endpoint for each of the resources and associate to the data collection rule.
6) On the Collect and deliver tab, select Add data source to add a data source and set a destination.
7) Select a Data source type.
8) Select which data you want to collect. For performance counters, you can select from a predefined set of objects and their sampling rate. For events, you can select from a set of logs and severity levels.
9) Select Custom to collect logs and performance counters that aren't currently supported data sources, or to filter events by using XPath queries. You can then specify an XPath to collect any specific values.
10) On the Destination tab, add one or more destinations for the data source. You can select multiple destinations of the same or different types. For instance, you can select multiple Log Analytics workspaces, which is also known as multihoming. You can send Windows event and Syslog data sources to Azure Monitor Logs only. You can send performance counters to both Azure Monitor Metrics and Azure Monitor Logs.
Select Add data source and then select Review + create to review the details of the data collection rule and association with the set of virtual machines.
Collect IIS logs
11) To create the data collection rule to collect IIS logs from a Windows Server VM in the Azure portal perform the steps outlined in the collect events and performance section, except when choosing your data source, specify IIS Logs.

Screenshot of the Add data source dialog in Create Data Collection Rule, showing IIS Logs selected and highlighted.

### Collect Syslog data
Syslog is an event logging protocol that's common to Linux. You can use the Syslog daemon that's built into Linux devices and appliances to collect local events of the types you specify. You can then have it send those events to a Log Analytics workspace. Applications send messages that might be stored on the local machine or delivered to a Syslog collector.

When the Azure Monitor agent for Linux is installed, it configures the local Syslog daemon to forward messages to the agent when Syslog collection is enabled in data collection rules (DCRs). Azure Monitor Agent then sends the messages to an Azure Monitor or Log Analytics workspace where a corresponding Syslog record is created in a Syslog table.

The following facilities are supported with the Syslog collector:

- auth
- authpriv
- cron
- daemon
- mark
- kern
- lpr
- mail
- news
- syslog
- user
- uucp
- local0-local7

The Azure Monitor Agent for Linux only collects events with the facilities and severities that are specified in its configuration. You can configure Syslog through the Azure portal or by managing configuration files on your Linux agents.

Configure Syslog collection from the Data Collection Rules menu of Azure Monitor. This configuration is delivered to the configuration file on each Linux agent. Follow the procedure outlined earlier in the unit for events and performance logs, but when selecting Add data source, ensure that for the data source type you select Linux syslog.

You can collect Syslog events with a different log level for each facility. By default, all Syslog facility types are collected. If you don't want to collect, for example, events of auth type, select NONE in the Minimum log level list box for auth facility and save the changes. If you need to change the default log level for Syslog events and collect only events with a log level starting at NOTICE or a higher priority, select LOG_NOTICE in the Minimum log level list box.



## 3.5 Module assessment

Answer the following questions
Choose the best response for each of the following questions.

1. Which of the following role assignments includes the necessary permissions to install the Azure Monitor Agent?
- Virtual Machine Reader
- Virtual Machine Contributor
- Log Analytics Reader

2. What is the maximum amount of time performance data can be viewed over in a VM Insights performance chart on IaaS VM CPU utilization?
- 7 days
- 30 days
- 21 days

3. When configuring a data collection rule, which of the following items can be sent to both Azure Monitor Metrics and Azure Monitor Logs?
- Windows Event log data
- Syslog
- Performance counter data

#№ Module Assessment Answers

## Question 1
**Which of the following role assignments includes the necessary permissions to install the Azure Monitor Agent?**

The correct answer is: **Virtual Machine Contributor**

The Virtual Machine Contributor role provides comprehensive management permissions for virtual machines, including the ability to install and configure agents such as the Azure Monitor Agent. This role grants the necessary access to modify VM configurations while Virtual Machine Reader is read-only, and Log Analytics Reader only provides access to view log data but not to modify VM configurations.

## Question 2
**What is the maximum amount of time performance data can be viewed over in a VM Insights performance chart on IaaS VM CPU utilization?**

The correct answer is: **30 days**

VM Insights performance charts allow you to view performance data for up to 30 days. This provides a comprehensive historical view of CPU utilization trends while balancing performance and storage considerations. The other options (7 days and 21 days) represent shorter time frames than what is actually available.

## Question 3
**When configuring a data collection rule, which of the following items can be sent to both Azure Monitor Metrics and Azure Monitor Logs?**

The correct answer is: **Performance counter data**

Performance counter data is the only option that can be sent to both Azure Monitor Metrics and Azure Monitor Logs. This flexibility allows performance data to be used both for real-time dashboards and alerting (Metrics) as well as for detailed analysis and querying (Logs). Windows Event log data and Syslog are text-based logs that can only be sent to Azure Monitor Logs, not to Metrics which requires numerical data.


## 3.6 Summary

In this module, you learned how to deploy and configure Azure Monitor Agent on IaaS VMs. You also learned how to enable VM Insights and Data Collection Rules to monitor performance and application telemetry.

#### Learn more
You can learn more by reviewing the following documents:

- Azure Monitor Agent overview, https://learn.microsoft.com/en-us/azure/azure-monitor/agents/azure-monitor-agent-overview
- Manage Azure Monitor Agent, https://learn.microsoft.com/en-us/azure/azure-monitor/agents/azure-monitor-agent-manage?tabs=azure-portal
- Use the Map feature of VM insights to understand application component, https://learn.microsoft.com/en-us/azure/azure-monitor/vm/vminsights-maps
- Chart performance with VM insights, https://learn.microsoft.com/en-us/azure/azure-monitor/vm/vminsights-performance
- Collect events and performance counters from virtual machines with Azure Monitor Agent, https://learn.microsoft.com/en-us/azure/azure-monitor/vm/data-collection
- Collect IIS logs with Azure Monitor Agent, https://learn.microsoft.com/en-us/azure/azure-monitor/vm/data-collection-iis
- Collect text logs with Azure Monitor Agent, https://learn.microsoft.com/en-us/azure/azure-monitor/vm/data-collection-log-text
- Collect Syslog events with Azure Monitor Agent, https://learn.microsoft.com/en-us/azure/azure-monitor/vm/data-collection-syslog



### 4. Configure monitoring for virtual networks

Understand how to use Azure Network Watcher Connection Monitor, flow logs, NSG diagnostics, and packet capture to monitor connectivity across your Azure IaaS network resources.

## 4.1 Introduction

Azure Network Watcher provides a suite of tools to monitor, diagnose, view metrics, and enable or disable logs for Azure IaaS (Infrastructure-as-a-Service) resources. Network Watcher enables you to monitor and diagnose the network health of IaaS products like virtual machines (VMs), virtual networks (VNets), application gateways, and load balancers. You can use Network Watcher to monitor the connections of these IaaS products to resources in Azure such as service endpoints as well as on-premises and other resources.

You are in IT Operations at Tailwind Traders. You're responsible for managing and monitoring the health of the Azure IaaS resources in your network environment. You need to be able to monitor, diagnose, view metrics, and enable or disable logs for those resources. Having investigated Azure Network Watcher, you decide that it has the tools you need to monitor and repair the network health of your network resources.

### Learning objectives
In this module, you learn how to use the following Azure Network Watcher functionality to monitor and diagnose Azure networks:

- Azure Network Watcher topology
- Connection Monitor
- IP flow verify and NSG diagnostics
- Packet capture


## 4.2 Topology

Azure Network Watcher’s Topology functionality provides a visualization of the entire network for understanding network configuration. It provides an interactive interface to view resources and their relationships in Azure spanning across multiple subscriptions, resource groups, and locations. You can also drill down to a resource view for resources to view their component level visualization.

The following are the resource types supported by topology:

- Application gateways
- Azure Bastion hosts
- Azure Front Door profiles
- ExpressRoute circuits
- Load balancers
- Network interfaces
- Network security groups
- Private endpoints
- Private Link services
- Public IP addresses
- Virtual machines
- Virtual network gateways
- Virtual networks

To view a topology, follow these steps:

1) In the search box at the top of the Azure portal, enter Monitor. Select Monitor from the search results.
2) Under Insights, select Networks.
3) In Networks, select Topology.
4)Select Scope to define the scope of the Topology.
5) In the Select scope pane, select the list of Subscriptions, Resource groups, and Locations of the resources for which you want to view the topology. Select Save.
6) Select the Resource type that you want to include in the topology and select Apply.

Screenshot displaying Azure Network's Topology view of a network and its configuration.

To drill down to the basic unit of each network, select the plus sign on each resource. When you hover on the resource, you can see the details of that resource. Selecting a resource displays a pane on the right with a summary of the resource. When you drill down to a VM within the topology, you can see details about the VM in the summary tab.

Screenshot of the summary tab in Topology, displaying details for a specific VM.

The Next hop capability of Network Watcher checks if the destination IP address is reachable from the source VM. Azure Network Watcher next hop gives you the Next hop type, IP address, and Route table ID of a specific destination IP address. Knowing the next hop helps you determine if traffic is being directed to the intended destination, or whether the traffic is being sent nowhere. An improper configuration of routes, where traffic is directed to an on-premises location, or a network virtual appliance, can lead to connectivity issues. If the route is defined using a user-defined route, the route table that has the route is returned. Otherwise, next hop returns System Route as the route table. The result shows the Next hop type and route table used to route traffic from the VM.

Screenshot of the Next hop details in Topology, showing the Next hop type and route table used to route traffic from the VM.



## 4.3 Connection Monitor

Connection Monitor provides unified, end-to-end connection monitoring in Azure Network Watcher. The Connection Monitor feature supports hybrid and Azure cloud deployments. Network Watcher provides tools to monitor, diagnose, and view connectivity-related metrics for your Azure deployments.

You can use Connection Monitor in the following scenarios:

- You can check network connectivity between the two VMs in a two-tier application to ensure that the front-end web server virtual machine (VM) is able to communicate with a VM hosting a database server VM.
- You want to calculate cross-region latencies between VMs deployed in different regions, for example, VMs in the Australia Southeast region with VMs deployed in the Central US region.
- You want to compare the latencies for branch office sites for Microsoft 365 URLs.
- You want to compare the latencies of an on-premises site with the latencies of an Azure application in terms of a connection to an Azure storage account endpoint.
- You want to check the connectivity between your on-premises setups and the Azure VMs that host your cloud application.
- You want to check the connectivity from multiple instances of an Azure Virtual Machine Scale Set to your Non-Azure multi-tier application.

### Diagnosing network issues

Connection Monitor helps you diagnose issues in your connection monitor and your network. Issues in your hybrid network are detected by the Log Analytics agents that you installed earlier. Issues in Azure are detected by the Network Watcher extension.

For networks whose sources are on-premises VMs, the following issues can be detected:

- Request timed out.
- Endpoint not resolved by DNS – temporary or persistent. URL invalid.
- No hosts found.
- Source unable to connect to destination. Target not reachable through ICMP.
- Certificate-related issues including:
Client certificate required to authenticate agent.
Certificate revocation list isn't accessible.
Host name of the endpoint doesn't match the certificate's subject or subject alternate name.
Root certificate is missing in source's Local Computer Trusted Certification Authorities store.
SSL certificate is expired, invalid, revoked, or incompatible.

For networks whose sources are Azure VMs, the following issues can be detected:

- Agent issues including:
- Agent stopped
Failed DNS resolution
No application or listener listening on the destination port and Socket could not be opened.
- VM state issues including:
Starting
Stopping
Stopped
Deallocating
Deallocated
Rebooting
Not allocated
- ARP table entry is missing.
- Traffic was blocked because of local firewall issues or NSG rules.
- Virtual network gateway issues including:
Missing routes
The tunnel between two gateways is disconnected or missing.
The second gateway wasn't found by the tunnel.
No peering info was found.
The route was missing in Microsoft Edge.
Traffic stopped because of system routes or user-defined route (UDR).
Border Gateway Protocol (BGP) isn't enabled on the gateway connection.
The dynamic IP address (DIP) probe is down at the load balancer.

### Configuring Connection Monitor
To use Connection Monitor to measure a specific scenario, you need to perform the following general steps:

1) Install monitoring agents.
2) Create a connection monitor.
3) Analyze monitoring data and set alerts.
4) Diagnose issues in your network.

### Install monitoring agents

Connection Monitor relies on lightweight executable files to run connectivity checks. It supports connectivity checks from both Azure environments and on-premises environments. The executable file that you use depends on whether your VM is hosted on Azure or on-premises.

Connection Monitor can use your Azure VMs or virtual machine scale sets as monitoring sources if the Network Watcher Agent virtual machine extension is installed on them. This extension is also known as the Network Watcher extension. This extension allows end-to-end monitoring and other advanced functionality.

Rules for a network security group (NSG) or firewall can block communication between the source and destination. Connection Monitor detects this issue and shows it as a diagnostics message in the topology. To enable connection monitoring, ensure that the NSG and firewall rules allow packets over TCP or ICMP between the source and destination.

To make Connection Monitor recognize your on-premises machines as sources for monitoring, install the Log Analytics agent on the machines. Then, enable the Network Performance Monitor solution. These agents are linked to Log Analytics workspaces, so you need to set up the workspace ID and primary key before the agents can start monitoring.

### Create a connection monitor

In connection monitors that you create in Connection Monitor, you can add both on-premises machines and Azure VMs/ scale sets as sources. These connection monitors can also monitor connectivity to endpoints. The endpoints can be on Azure or any other URL or IP address.

Connection Monitor includes the following entities:

- Connection monitor resource: A region-specific Azure resource. All the following entities are properties of a connection monitor resource.
- Endpoint: A source or destination that participates in connectivity checks. Examples of endpoints include Azure VMs/ scale sets, on-premises agents, URLs, and IP addresses.
- Test configuration: A protocol-specific configuration for a test. Based on the protocol you select, you can define the port, thresholds, test frequency, and other properties.
- Test group: The group that contains source endpoints, destination endpoints, and test configurations. A connection monitor can contain more than one test group.
- Test: The combination of a source endpoint, destination endpoint, and test configuration. A test is the most granular level at which monitoring data is available. The monitoring data includes the percentage of checks that failed and the round-trip time (RTT).

To create a connection monitor, perform the following steps:

1) In the Azure portal, go to Network Watcher.
2) On the left pane, in the Monitoring section, select Connection monitor.
3) On the Connection Monitor dashboard, select Create.
4) On the Basics pane, enter the following details:
Connection Monitor Name: Enter a name for your connection monitor. Use the standard naming rules for Azure resources.
Subscription: Select a subscription for your connection monitor.
Region: Select a region for your connection monitor. You can select only the source VMs that are created in this region.
Workspace configuration: Choose a custom workspace or the default workspace. Your workspace holds your monitoring data. To choose a custom workspace, clear the default workspace checkbox, and then select the subscription and region for your custom workspace.
5) Select Next:
6) On the Test groups page, either select an existing test group or create a new one. To create a test group, provide the following information:
Test group Name: Enter the name of your test group.
Sources: Select Add sources to specify both Azure VMs and on-premises machines as sources if agents are installed on them.
When you select a virtual network, subnet, a single VM, or a virtual machine scale set, the corresponding resource ID is set as the endpoint. By default, all VMs in the selected virtual network or subnet participate in monitoring. To reduce the scope, either select specific subnets or agents or change the value of the scope property.
To choose on-premises agents, select the Non–Azure endpoints tab. Select from a list of on-premises hosts with a Log Analytics agent installed. Select Arc Endpoint as the Type and select the subscriptions from the Subscription dropdown list. The list of hosts that have the Azure Arc endpoint extension and the Azure Monitor Agent extension enabled are displayed.
To choose public endpoints as destinations, select the External Addresses tab. The list of endpoints includes Office 365 test URLs and Dynamics 365 test URLs, grouped by name. You also can choose endpoints that were created in other test groups in the same connection monitor.
To add an endpoint, at the upper right, select Add Endpoint, and then provide an endpoint name and URL, IP, or FQDN.
7) The next step is to configure Alerts. Alerts allow you to be notified if tests are failing. When you create an alert, you need to specify which connection monitor test failure will trigger the alert. Specify an action group to determine what happens when the alert triggers.
8) At the bottom of the pane, select Next: Review + create.


### Analyze monitoring data
While monitoring endpoints, Connection Monitor re-evaluates the status of endpoints once every 24 hours. So, in case a VM gets deallocated or is turned-off during a 24-hour cycle, Connection Monitor would report an indeterminate state due to absence of data in the network path till the end of the 24-hour cycle before re-evaluating the status of the VM and reporting the VM status as deallocated.

Depending on the data that the checks return, tests can have the following states:

- Pass: Actual values for the percentage of failed checks and round-trip time (RTT) are within the specified thresholds.
- Fail: Actual values for the percentage of failed checks or RTT exceeded the specified thresholds. If no threshold is specified, a test reaches the Fail state when the percentage of failed checks is 100.
- Warning:
If a threshold is specified and Connection Monitor observes a checks-failed percentage that's more than 80 percent of the threshold, the test is marked as Warning.
In the absence of specified thresholds, Connection Monitor automatically assigns a threshold. When that threshold is exceeded, the test status changes to Warning. For RTT in TCP or ICMP tests, the threshold is 750 milliseconds (ms). For the checks-failed percentage, the threshold is 10 percent.
- Indeterminate: No data in the Log Analytics workspace. Check the metrics.
- Not Running: Disabled by disabling the test group.
The data that Connection Monitor collects is stored in the Log Analytics workspace. You set up this workspace when you created the connection monitor.

Monitoring data is also available in Azure Monitor Metrics. You can use Log Analytics to keep your monitoring data for as long as you want. Azure Monitor stores metrics for only 30 days by default.


## 4.4 IP flow verify and NSG diagnostics

Both IP flow verify and NSG diagnostics allow you to diagnose how networking configuration might be restricting network traffic.

### IP flow verify
IP flow verify checks if a packet is allowed or denied to or from a virtual machine. The information consists of direction, protocol, local IP, remote IP, local port, and a remote port. If the packet is denied by a security group, the name of the rule that denied the packet is returned. While any source or destination IP can be chosen, IP flow verify helps administrators quickly diagnose connectivity issues from or to the internet and from or to the on-premises environment.

IP flow verify looks at the rules for all Network Security Groups (NSGs) applied to the network interface, such as a subnet or virtual machine NIC. Traffic flow is then verified based on the configured settings to or from that network interface. IP flow verify is useful in confirming if a rule in a Network Security Group is blocking ingress or egress traffic to or from a virtual machine. Now along with the NSG rules evaluation, the Azure Virtual Network Manager rules will also be evaluated.

Azure Virtual Network Manager (AVNM) is a management service that enables users to group, configure, deploy, and manage Virtual Networks globally across subscriptions. AVNM security configuration allows users to define a collection of rules that can be applied to one or more network groups at the global level. These security rules have a higher priority than network security group (NSG) rules. An important difference to note here is that admin rules are a resource delivered by AVNM in a central location controlled by governance and security teams, which bubble down to each VNet. NSGs are a resource controlled by the VNet owners, which apply at each subnet or NIC level.

An instance of Network Watcher needs to be created in all regions where you plan to run IP flow verify. Network Watcher is a regional service and can only be run against resources in the same region. The instance used does not affect the results of IP flow verify, as any route associated with the NIC or subnet is still returned.

### NSG diagnostics

The NSG (Network Security Group) diagnostics is an Azure Network Watcher tool that helps you understand which network traffic is allowed or denied in your Azure virtual network along with detailed information for debugging. NSG diagnostics can help you verify that your network security group rules are set up properly. NSG diagnostics shares some functionality with IP flow verify.

The NSG diagnostics tool can simulate a given flow based on the source and destination you provide. It returns whether the flow is allowed or denied with detailed information about the security rule allowing or denying the flow.

To run diagnostics against an NSG, perform the following steps:

1) In the search box at the top of the portal, search for and select Network Watcher.
2) Under Network diagnostic tools, select NSG diagnostics.
3) On the NSG diagnostics page, enter or select the following values:
Target resource
Target resource type. Select the resource you are diagnosing the connection to.
Virtual machine. Select the VM you want to run the diagnostics from.
Traffic details
Protocol. Select TCP, UDP and/or ICMP.
Direction. Select Inbound or Outbound.
Source type. Select IPv4 address/CIDR or Service Tag.
Ipv4 address/CIDR. Acceptable values are: single IP address, multiple IP addresses, single IP prefix, and multiple IP prefixes.
Destination IP address. Acceptable values are: single IP address, multiple IP addresses, single IP prefix, multiple IP prefixes.
Destination port. Enter * to include all ports.
4) Select Run NSG diagnostics to run the test. Once NSG diagnostics completes checking all security rules, it displays the result. This result will indicate which rules an NSG has, and which rule is denying traffic.



## 4.5 Packet capture

Azure Network Watcher packet capture allows you to create packet capture sessions to track traffic to and from a virtual machine (VM) or a scale set. Packet capture helps to diagnose network anomalies both reactively and proactively. Other uses include gathering network statistics, gaining information on network intrusions, to debug client-server communications and much more.

Packet capture is an extension that is remotely started through Network Watcher. This capability eases the burden of running a packet capture manually on the desired virtual machine or virtual machine scale set instance(s), which saves valuable time. Packet capture can be triggered through the portal, PowerShell, Azure CLI, or REST API. One example of how packet capture can be triggered is with virtual machine alerts. Filters are provided for the capture session to ensure you capture traffic you want to monitor. Filters are based on 5-tuple (protocol, local IP address, remote IP address, local port, and remote port) information. The captured data can be stored in the local disk or a storage blob. Packet capture requires a virtual machine extension.

To implement a packet capture, perform the following steps:

1) In the search box at the top of the Azure portal, enter Network Watcher and in the search results, select Network Watcher.
2) Select Packet capture under Network diagnostic tools. Any existing packet captures are listed, regardless of their status.
3) Select + Add to create a packet capture. In Add packet capture, enter or select values for the following settings in the Basic Details page:
Subscription. Select the Azure subscription of the virtual machine.
Resource group. Select the resource group of the virtual machine.
Target type. Select Virtual machine.
Target instance. Select the virtual machine.
Packet capture name. Enter a name or leave the default name.
4) Enter or select values for the following settings in the Packet capture configuration page:
Capture location. Select Storage account, File, or Both.
Storage account. Select your Standard storage account. This option is available if you selected Storage account or Both.
Local file path. Enter a valid local file path where you want the capture to be saved in the target virtual machine. If you're using a Linux machine, the path must start with /var/captures.
Maximum bytes per packet. Enter the maximum number of bytes to be captured per each packet. All bytes are captured if left blank or 0 entered.
Maximum bytes per session. Enter the total number of bytes that are captured. Once the value is reached the packet capture stops. Up to 1 GB is captured if left blank.
Time limit (seconds). Enter the time limit of the packet capture session in seconds. Once the value is reached the packet capture stops. Up to 5 hours (18,000 seconds) is captured if left blank.
5) You can optionally configure the following filtering settings.
Protocol. Filters the packet capture based on the selected protocol. Available values are TCP, UDP, or Any.
Local IP address. Filters the packet capture for packets where the local IP address matches this value.
Local port. Filters the packet capture for packets where the local port matches this value.
Remote IP address. Filters the packet capture for packets where the remote IP address matches this value.
Remote port. Filters the packet capture for packets where the remote port matches this value.
6) Select Start packet capture. Once the time limit set on the packet capture is reached, the packet capture stops and can be reviewed.


## 4.6 Module assessment

Answer the following questions
Choose the best response for each of the following questions.

1. Which functionality in Topology should be used to determine the path that is being taken from the VM to the external data source?
- Next Hop
- VNet Configuration
- DNS Settings

2. What must be installed on on-premises computers in order to use Connection Monitor to diagnose latency between those computers and an Azure storage endpoint?
- Azure Network Adapter
- SNMP Agent
- Log Analytics Agent

4. A Connection Monitor is created between an Azure Arc enabled server in an on-premises location and an Azure storage endpoint. No warning threshold is specified so Connection Monitor uses default values for its tests. Which of the following results triggers a warning result?
- Ten percent of results over 500 milliseconds
- Five percent of results over 750 milliseconds
- Ten percent of results over 750 milliseconds


### Module Assessment Answers

#### Question 1
**Which functionality in Topology should be used to determine the path that is being taken from the VM to the external data source?**

The correct answer is: **Next Hop**

The Next Hop functionality in Network Watcher's Topology view allows you to trace the routing path from a virtual machine to a destination. It shows each network hop along the route, helping identify the exact path that network traffic takes when traveling from the VM to an external data source. This is essential for diagnosing routing issues, unexpected network paths, or connectivity problems.

#### Question 2
**What must be installed on on-premises computers in order to use Connection Monitor to diagnose latency between those computers and an Azure storage endpoint?**

The correct answer is: **Log Analytics Agent**

The Log Analytics Agent (also known as Microsoft Monitoring Agent) must be installed on on-premises computers to enable Connection Monitor functionality for diagnosing latency to Azure resources. This agent allows the on-premises system to report monitoring data to Azure and participate in Connection Monitor tests. Neither the Azure Network Adapter (which doesn't exist as a product) nor the SNMP Agent provides the necessary capabilities for Connection Monitor integration.

#### Question 3
**A Connection Monitor is created between an Azure Arc enabled server in an on-premises location and an Azure storage endpoint. No warning threshold is specified so Connection Monitor uses default values for its tests. Which of the following results triggers a warning result?**

The correct answer is: **Ten percent of results over 750 milliseconds**

By default, Connection Monitor will trigger a warning when 10% of test results exceed 750 milliseconds of latency. This threshold represents a balance between sensitivity to potential issues and tolerance for normal network variations. The other options either specify an incorrect percentage threshold or an incorrect latency value compared to the default Connection Monitor configuration.


## 4.7 Summary

In this module, you learned how to monitor connectivity across your Azure IaaS network resources. You learned how to create an Azure Network Watcher Connection Monitor to monitor, diagnose, and view connectivity-related metrics for your Azure deployments. You also learned how to create and configure flow logs, run diagnostics against NSGs, and use packet capture sessions to track traffic to and from a virtual machine (VM) or a scale set.

#### Learn more

- What is Azure Network Watcher?, https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-overview
- Azure Network Watcher connection monitor, https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview
- Flow logging for network security groups, https://learn.microsoft.com/en-us/azure/network-watcher/nsg-flow-logs-overview?tabs=Americas
- NSG diagnostics overview, https://learn.microsoft.com/en-us/azure/network-watcher/nsg-diagnostics-overview



# 5 Configure alerts and responses

Understand how to configure and manage alerts and responses in order to proactively manage notifications about potential issues before those issues become problems for your users.

# 5.1 Introduction

The purpose of Azure Monitoring alerts is to notify you proactively when Azure Monitor data indicates there might be a problem. Alerts can notify you of problems with your infrastructure or applications before a problem becomes one for your users.

You are in IT Operations at Tailwind Traders. As part of your job, you want to ensure you’re using the best tools to stay informed about issues that may affect your applications and infrastructure before those issues occur. You decide that Azure Monitor alerts and responses would give you the means to successfully accomplish this.

#### Learning objectives

In this module, you learn how to:

- Describe the purpose of and identify the different types of alerts.
- Explain how action groups are used to notify users about alerts.
- Configure and manage alert rules.
- Configure alert processing rules to modify triggered alerts.
- Describe how Change Analysis provides insight into changes made to Azure resources.
- 
#### Prerequisites:
- Understand the basic functionality of Azure Monitor and Log Analytics workspaces.


## 5.2 Azure Monitor alerts

Azure Monitor Alerts help you detect and address issues before users notice them by proactively notifying you when Azure Monitor data indicates there might be a problem with your infrastructure or application. You can alert on any metric or log data source in the Azure Monitor data platform.

Azure Monitor supports the following types of alert:

- Metric alerts. Metric alerts evaluate resource metrics at regular intervals. Metrics can be platform metrics, custom metrics, logs from Azure Monitor converted to metrics, or Application Insights metrics. Metric alerts can also apply multiple conditions and dynamic thresholds.
Log alerts. Log alerts allow users to use a Log Analytics query to evaluate resource logs at a predefined frequency.
- Activity log alerts. Activity log alerts are triggered when a new activity log event occurs that matches defined conditions. Resource Health alerts and Service Health alerts are activity log alerts that report on your service and resource health.
- Smart detection alerts. Smart detection on an Application Insights resource automatically warns you of potential performance problems and failure anomalies in your web application. You can migrate smart detection on your Application Insights resource to create alert rules for the different smart detection modules.
- Prometheus alerts. Prometheus alerts are used for alerting on Prometheus metrics stored in Azure Monitor managed services for Prometheus. The alert rules are based on the PromQL open-source query language.
If you don't have alert rules defined for the selected resource, you can enable recommended out-of-the-box alert rules in the Azure portal.

The system compiles a list of recommended alert rules based on:

- The resource provider’s knowledge of important signals and thresholds for monitoring the resource.
- Data that tells us what customers commonly alert on for this resource.

Recommended alert rules are available for:

- Virtual machines
- AKS resources
- Log Analytics workspaces

### Alert RBAC permissions

You can only access, create, or manage alerts for resources for which you have permissions. To create an alert rule, you must have:

- Read permission on the target resource of the alert rule.
- Write permission on the resource group in which the alert rule is created. If you're creating the alert rule from the Azure portal, the alert rule is created by default in the same resource group in which the target resource resides.
- Read permission on any action group associated with the alert rule, if applicable.

These built-in Azure roles, supported at all Azure Resource Manager scopes, have permissions to and can access alerts information and create alert rules:

- Monitoring contributor: A contributor can create alerts and use resources within their scope.
- Monitoring reader: A reader can view alerts and read resources within their scope.

### Alert state
You can configure whether log or metric alerts are stateful or stateless. Activity log alerts are stateless.

- Stateless alerts fire each time the condition is met, even if fired previously.
- Stateful alerts fire when the condition is met. They don't fire again or trigger any more actions until the conditions are resolved.


## 5.3 Action groups

When Azure Monitor data indicates that there might be a problem with your infrastructure or application, an alert is triggered. Alerts can contain action groups, which are a collection of notification preferences. Azure Monitor, Azure Service Health, and Azure Advisor use action groups to notify users about the alert and take an action.

Each action is made up of:

- Type: The notification that's sent or action that's performed. Examples include sending a voice call, SMS, or email. You can also trigger various types of automated actions.
- Name: A unique identifier within the action group.
- Details: The corresponding details that vary by type.
In general, an action group is a global service. Global requests from clients can be processed by action group services in any region. If one region of the action group service is down, the traffic is automatically routed and processed in other regions. As a global service, an action group helps provide a disaster recovery solution.

### Action group properties
Action groups have the following properties:

- You can add up to five action groups to an alert rule.
- Action groups are executed concurrently, in no specific order.
- Multiple alert rules can use the same action group.

When creating an Action group, you must choose a region option. The two options are as follows:

- Global. The action groups service decides where to store the action group. The action group is persisted in at least two regions to ensure regional resiliency. Processing of actions may be done in any geographic region. Voice, SMS, and email actions performed as the result of service health alerts are resilient to Azure live-site incidents.
- Regional. The action group is stored within the selected region. The action group is zone-redundant. Use this option if you want to ensure that the processing of your action group is performed within a specific geographic boundary.

### Action group notification
Action groups support the following notification options:

- Email Azure Resource Manager role. Send an email to the subscription members, based on their role. A notification email is sent only to the primary email address configured for the Azure AD user. The email is only sent to Azure Active Directory user members of the selected role, not to Azure AD groups or service principals.
- Email. Send an email to a specific address. Ensure that your email filtering and any malware/spam prevention services are configured appropriately. Emails are sent from the following email addresses:
azure-noreply@microsoft.com
azureemail-noreply@microsoft.com
alerts-noreply@mail.windowsazure.com
SMS. SMS notifications support bi-directional communication. The recipient of an SMS is able to unsubscribe to SMS alerts, resubscribe, or request help. You must enter the country code and phone number of the recipient. The SMS contains the following information:
Shortname of the action group this alert was sent to
The title of the alert.
- Azure app Push notifications. Send notifications to the Azure mobile app. In the Azure account email field, enter the email address that you use as your account ID when you configure the Azure mobile app.
- Voice. Voice notification. Enter the Country code and the Phone number for the recipient of the notification.

### Action types
Action groups allow the following actions to be triggered:

- Automation Runbook. Allows an automation runbook to be run.
- Event hubs. An Event Hubs action publishes notifications to Event Hubs. You can subscribe to the alert notification stream from your event receiver.
- Functions. Calls an existing HTTP trigger endpoint in functions. When you define the function action, the function's HTTP trigger endpoint and access key are saved in the action definition. If you change the access key for the function, you must remove and re-create the function action in the action group. In addition to this your endpoint must support the HTTP POST method and the function must have access to the storage account.
- ITSM. Allows you to create work items in your ITSM (IT Service Management) tool based on your Azure metric alerts, activity log alerts, and Log Analytics alerts.
- Logic apps. You can use Azure Logic Apps to build and customize workflows for integration and to customize your alert notifications.
- Secure webhook. When you use a secure webhook action, you must use Azure AD to secure the connection between your action group and your endpoint, which is a protected web API. Secure webhook doesn't support basic authentication.
- Webhook. If you use the webhook action, your target webhook endpoint must be able to process the various JSON payloads that different alert sources emit. You can't pass security certificates through a webhook action. To use basic authentication, you must pass your credentials through the URI. If the webhook endpoint expects a specific schema, for example, the Microsoft Teams schema, use the Logic Apps action type to manipulate the alert schema to meet the target webhook's expectations.

### Common alert schema
The common alert schema standardizes the consumption of Azure Monitor alert notifications. Historically, activity log, metric, and log alerts each had their own email templates and webhook schemas. The common alert schema provides one standardized schema for all alert notifications.

The common alert schema provides a consistent structure for:

- Email templates: Use the detailed email template to diagnose issues at a glance. Embedded links to the alert instance on the portal and to the affected resource ensure that you can quickly jump into the remediation process.
- JSON structure: Use the consistent JSON structure to build integrations for all alert types using:
Azure Logic Apps
Azure Functions
Azure Automation runbook

Alerts generated by VM insights do not support the common schema. Smart detection alerts use the common schema by default. However, you don't have to enable the common schema for smart detection alerts.

### Create an action group
To create an action group, perform the following steps:

1) In the Azure portal search for and select Monitor.
2) In the Monitor page, select Alerts, and then select Action groups and select Create.
3) Configure the basic action group settings. In the Project details section:
Select values for Subscription and Resource group.
Select the region. Choose between Global and Regional.
4) In the Instance details section, enter values for Action group name and Display name. The display name is used in place of a full action group name when the group is used to send notifications.
5) Configure notifications. Select Next: Notifications or select the Notifications tab at the top of the page.
6) Define a list of notifications to send when an alert is triggered. You can choose between the following options described earlier:
Email Azure Resource Manager role
Email
SMS
Azure app Push notifications
Voice
7) Select if you want to enable the Common alert schema and choose Next.
8) Configure actions. Select Next: Actions. or select the Actions tab at the top of the page. Define a list of actions to trigger when an alert is triggered. Select an action type and enter a name for each action. You can choose from the following actions:
- Automation Runbook.
- Event hubs.
- Functions.
- ITSM.
- Logic apps.
- Secure webhook.
- Webhook.

9) If you'd like to assign a key-value pair to the action group to categorize your Azure resources, select Next: Tags or the Tags tab. Otherwise, skip this step.
10) Select Review + create to review your settings. This step quickly checks your inputs to make sure you've entered all required information. If there are issues, they're reported here. After you've reviewed the settings, select Create to create the action group.



## 5.4 Alert rules

An alert rule monitors your data and captures a signal that indicates something is happening on the specified resource. The alert rule captures the signal and checks to see if the signal meets the criteria of the condition. If the conditions are met, an alert is triggered, which initiates the associated action group and updates the state of the alert.

You create an alert rule by combining:
- The resources to be monitored.
- The signal or data from the resource.
- Conditions.

You then define these elements for the alert actions:
- Action groups
- Alert processing rules

Alerts triggered by these alert rules contain a payload that uses the common alert schema.

### Create an alert rule
To create a new alert rule from the portal home page:

1) In the portal, select Monitor > Alerts.
2) Open the + Create menu and select Alert rule.
3) On the Select a resource pane, set the scope for your alert rule. You can filter by subscription, resource type, or resource location. Select Apply. Select Next: Condition at the bottom of the page.
4) On the Condition tab, when you select the Signal name field, the most commonly used signals are displayed in the drop-down list. Select one of these popular signals or select See all signals if you want to choose a different signal for the condition. If you chose to See all signals in the previous step, use the Select a signal pane to search for the signal name or filter the list of signals. Filter by:
Signal type. The type of alert rule you're creating.
Signal source. The service sending the signal. The list is prepopulated based on the type of alert rule you selected.
5) The next step depends on the type of alert that you are creating:
Metric alert. Provide time range and time series, a threshold, operator, aggregation, and when to evaluate.
Log alert. Write a query that returns the log events for which you want to create an alert. The condition tab will be populated based on your log query. Select threshold values to trigger the alert.
Activity log alert. Select the chart period and values for the event level, status, and event initiated by related to the activity.
Resource health alert. Provide details for the Event status, Current resource status, Previous resource status and reason type fields.
Service health alert. Provide details for the following fields: Azure services, Azure regions, event types.
6) On the Actions tab, select or create the required action groups.
7) On the Alert Rule Details page, specify the subscription and resource group that will host the alert. Also provide an alert name, description and severity.

### Manage alert rules
You manage alert rules from the Alerts page in the Azure portal.

Screenshot of Azure Monitor alerts.

You can filter the list of Alert rules using the available filters:
- Subscription
- Alert condition
- Severity
- User response
- Monitor service
- Signal type
- Resource group
- Target resource type
- Resource name
- Suppression status

If you select a single alert rule, you can edit, disable, duplicate, or delete the rule in the alert rule pane. If you select multiple alert rules, you can enable or disable the selected rules. Selecting multiple rules can be useful when you want to perform maintenance on specific resources.




### 5.5 Alert processing rules

You can use alert processing rules to make modifications to triggered alerts as they're being fired. You can use alert processing rules to add or suppress action groups, apply filters, or have the rule processed on a predefined schedule. Alert processing rules are different from alert rules. Alert rules generate new alerts, while alert processing rules modify the fired alerts as they're being fired.

You can use alert processing rules to add action groups or remove (suppress) action groups from your fired alerts. You can apply alert processing rules to different resource scopes, from a single resource, or to an entire subscription. You can also use them to apply various filters or have the rule work on a predefined schedule.

Common uses for alert processing rules include:

- Suppress notifications during planned maintenance.
- Management at scale.
- Add action groups to all alert types.

You can control when an alert processing rule will apply. The alert processing rule is always active, by default. You can select a one-time window for this rule to apply, or you can have a recurring window, such as a weekly recurrence.

### Suppressing notifications during planned maintenance
Many customers set up a planned maintenance time for their resources, either on a one-time basis or on a regular schedule. The planned maintenance might cover a single resource, like a virtual machine, or multiple resources, like all virtual machines in a resource group. So, you might want to stop receiving alert notifications for those resources during the maintenance window. Alert processing rules allow you to do that.

You could suppress alert notifications by disabling the alert rules themselves at the beginning of the maintenance window, and reenable them after the maintenance is over. In that case, the alerts won't fire in the first place. That approach has several limitations:

- This approach is only practical if the scope of the alert rule is exactly the scope of the resources under maintenance. For example, a single alert rule might cover multiple resources, but only a few of those resources are going through maintenance. So, if you disable the alert rule, you won't be alerted when the remaining resources covered by that rule run into issues.
- You might have many alert rules that cover the resource. Updating all of them is time consuming and error prone.
- You might have some alerts that aren't created by an alert rule at all, like alerts from Azure Backup.

In all these cases, an alert processing rule provides an easy way to suppress notifications.

### Management at scale

Most customers tend to define a few action groups that are used repeatedly in their alert rules. For example, they might want to call a specific action group whenever any high-severity alert is fired. As their number of alert rules grows, manually making sure that each alert rule has the right set of action groups is becoming harder.

Alert processing rules allow you to specify that logic in a single rule, instead of having to set it consistently in all your alert rules. They also cover alert types that aren't generated by an alert rule.

### Add action groups to all alert types
Azure Monitor alert rules let you select which action groups will be triggered when their alerts are fired. However, not all Azure alert sources let you specify action groups. Some examples of such alerts include Azure Backup alerts, VM Insights guest health alerts, Azure Stack Edge, and Azure Stack Hub. For those alert types, you can use alert processing rules to add action groups.

### Alert processing rules filters and scope
Each alert processing rule has a scope. A scope is a list of one or more specific Azure resources, a specific resource group, or an entire subscription. The alert processing rule applies to alerts that fired on resources within that scope.

You can also define filters to narrow down which specific subset of alerts are affected within the scope.

You can figure the following filters:

- Alert context (payload). The rule applies only to alerts that contain any of the filter's strings within the alert context section of the alert. This section includes fields specific to each alert type.
- Alert rule ID. The rule applies only to alerts from a specific alert rule. The value should be the full resource ID. To locate the alert rule ID, open a specific alert rule in the portal, select Properties, and copy the Resource ID value.
- Alert rule name. The rule applies only to alerts with this alert rule name. It can also be useful with a Contains operator.
- Description. The rule applies only to alerts that contain the specified string within the alert rule description field.
- Monitor condition. The rule applies only to alerts with the specified monitor condition, either Fired or Resolved.
- Monitor service. The rule applies only to alerts from any of the specified monitoring services that are sending the signal. Different services are available depending on the type of signal.
- Resource. The rule applies only to alerts from the specified Azure resource. For example, you can use this filter with Does not equal to exclude one or more resources when the rule's scope is a subscription.
- Resource group. The rule applies only to alerts from the specified resource groups. For example, you can use this filter with Does not equal to exclude one or more resource groups when the rule's scope is a subscription.
- Resource type. The rule applies only to alerts on resources from the specified resource types, such as virtual machines. You can use Equals to match one or more specific resources. You can also use Contains to match a resource type and all its child resources.
- Severity. The rule applies only to alerts with the selected severities.

If you define multiple filters in a rule, all the rules apply. There's a logical AND between all filters.

### Alert processing rules actions
Alert processing rules can perform one of the following actions:

- Suppression: This action removes all the action groups from the affected fired alerts. So, the fired alerts won't invoke any of their action groups, not even at the end of the maintenance window. Those fired alerts will still be visible when you list your alerts in the portal, Azure Resource Graph, API, or PowerShell. The suppression action has a higher priority over the Apply action groups action. If a single fired alert is affected by different alert processing rules of both types, the action groups of that alert will be suppressed.
- Apply action groups: This action adds one or more action groups to the affected fired alerts.

### Create an alert processing rule
To create an alert processing rule, perform the following steps:

1) In the Alerts page of the Azure portal select Create > Alert processing rules to open the new alert processing rule wizard.
2) On the Scope tab, you select which fired alerts are covered by this rule. Pick the scope of resources whose alerts will be covered. You can choose multiple resources and resource groups, or an entire subscription. You can also optionally add filters.
3) On the Rule settings tab, you select which action to apply on the affected alerts. Choose between Suppress notifications or Apply action group. If you choose Apply action group, you can select existing action groups by selecting Add action groups. You can also create a new action group.
4) On the Scheduling tab, you select an optional schedule for the rule. By default, the rule works all the time, unless you disable it. You can set it to work On a specific time, or you can set up a Recurring schedule.
5) On the Details tab, you give this rule a name, pick where it will be stored, and optionally add a description for your reference.
6) On the Tags tab, you can optionally add tags to the rule.
7) On the Review + create tab, you can review and create the alert processing rule.


## 5.6 Azure Monitor change analysis

Change Analysis detects various types of changes, from the infrastructure layer through application deployment. Using Azure Resource Graph, Change Analysis provides a historical record of how the Azure resources that host your application have changed over time. Change Analysis is a subscription-level Azure resource provider that:

- Checks resource changes in the subscription.
- Provides data for various diagnostic tools to help users understand what changes might have caused issues.
Azure Monitor's Change Analysis queries for:

- Azure Resource Manager resource properties.
- Resource configuration changes.
- App Service Function and Web App in-guest changes.

Change Analysis also tracks resource dependency changes to diagnose and monitor an application end-to-end.

Azure Monitor Change Analysis service supports resource property level changes in all Azure resource types, including common resources like:

- Virtual Machine
- Virtual machine scale set
- App Service
- Azure Kubernetes Service (AKS)
- Azure Function
- Networking resources:
Network Security Group
Virtual Network
Application Gateway, etc.
- Data services:
Storage
SQL
Redis Cache
Azure Cosmos DB, etc.

To enable Azure Monitor Change Analysis, register the Microsoft.ChangeAnalysis resource provider with an Azure Resource Manager subscription to make the resource properties and configuration change data available. The Microsoft.ChangeAnalysis resource provider is automatically registered as you either:

- Enter any UI entry point, like the Web App Diagnose and Solve Problems tool, or
- Bring up the Change Analysis standalone tab.


## 5.7 Module assessment

Answer the following questions
Choose the best response for each of the following questions.

1. How many action groups can be added to an alert rule?
- Five
- Ten
- Twenty
2. A set of action groups need to be suppressed from sending notifications during maintenance at scale on resources in Azure. Which of the following items should be configured?
- Alert state
- Action group
- Alert processing rule
3. An alert processing rule is configured with three filters. How many of the filters apply at any time to the rule?
- One
- Two
- Three

### Module Assessment Answers

#### Question 1
**How many action groups can be added to an alert rule?**

The correct answer is: **Five**

An alert rule in Azure can have a maximum of five action groups associated with it. This limitation is designed to maintain manageability and performance when alerts are triggered. Each action group can contain multiple notification methods (email, SMS, webhook, etc.), but the total number of action groups per alert rule is capped at five.

#### Question 2
**A set of action groups need to be suppressed from sending notifications during maintenance at scale on resources in Azure. Which of the following items should be configured?**

The correct answer is: **Alert processing rule**

Alert processing rules are specifically designed to manage alerts at scale, including the ability to temporarily suppress notifications from action groups during planned maintenance periods. Alert processing rules can be configured to apply across multiple resources, resource groups, or subscriptions, making them ideal for coordinating maintenance activities. Neither Alert state nor Action group provides the capability to suppress notifications at scale during maintenance windows.

#### Question 3
**An alert processing rule is configured with three filters. How many of the filters apply at any time to the rule?**

The correct answer is: **Three**

When an alert processing rule has multiple filters configured, all of them apply simultaneously. The rule processes incoming alerts against all three filters, and the alert must match all filter criteria to have the rule's actions applied to it. This creates an "AND" condition between filters, not an "OR" condition, meaning all three filters are actively evaluating alerts at the same time.


## 5.8 Summary

In this module, you learned how to configure and manage alerts and responses to proactively manage notifications about potential issues with your applications and infrastructure.

#### Learn more
You can learn more by reviewing the following documents:

- Action groups, https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups
- Create or edit an alert rule, https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-metric-alert-rule
- Manage your alert rule, https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-manage-alert-rules
- Alert processing rules, https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules?tabs=portal
- Use Change Analysis in Azure Monitor, https://learn.microsoft.com/en-us/azure/azure-monitor/change/change-analysis


## 6 Guided Project – Deploy and configure Azure Monitor

Understand how to configure monitoring of various workloads and infrastructure services using Azure Monitor.

## 6.1 Introduction

Welcome to this interactive skills validation experience. Completing this module helps you prepare for the **Deploy and configure Azure Monitor assessment**.

In this module, you practice configuring monitoring of various workloads and infrastructure services using Azure Monitor. The lab combines both learning and hands-on practice. The skills validated include:

* Deploying and configuring Log Analytics
* Configuring monitoring for Web apps
* Monitoring compute and networking services
* Configuring alerts

By the end of this guided exercise, you gain hands-on experience in creating and configuring these services in Azure.

> **Note**: This is a guided project module where you complete an end-to-end project by following step-by-step instructions.

## Skills Breakdown

| Skilling area | Skilling task |
|---------------|---------------|
| **Deploy Log Analytics** | • Create a Log Analytics workspace<br>• Configure Log Analytics data retention and archive policies<br>• Enable access to a Log Analytics workspace |
| **Monitor web apps** | • Enable Application Insights<br>• Disable logging for .NET core snapshot debugger<br>• Configure Web apps to be written to a Log Analytics workspace<br>• Enable file and configuration tracking for web apps |
| **Configure monitoring for compute services** | • Create a data collection endpoint<br>• Create a data collection rule<br>• Add an IIS log collection to an existing data collection rule<br>• Configure Network Connection Monitor for a Linux IaaS virtual machine |
| **Configure alerts** | • Create an action group to send an email<br>• Create an alert for VM CPU utilization |


## 6.2 Exercise - Prepare your Azure environment

You must first complete the following exercise to prepare your Azure environment before you begin the lab exercises.

### Tasks:
* Create a Log Analytics workspace.
* Configure Log Analytics data retention and archive policies.
* Enable access to a Log Analytics workspace.

Launch the exercise and follow the instructions. When you're done, be sure to return to this page so you can continue learning.

> **Note**: To complete this lab you will need an **Azure subscription**.

## 6.3 Exercise - Deploy Log Analytics

This guided project consists of the four exercises:
* **Exercise 1: Deploy Log Analytics**
* Exercise 2: Monitor web apps
* Exercise 3: Configure monitoring for compute services
* Exercise 4: Configure alerts

In Exercise 1, you deploy and configure a Log Analytics workspace:
* Task 1: Create a Log Analytics workspace.
* Task 2: Configure Log Analytics data retention and archive policies.
* Task 3: Enable access to a Log Analytics workspace.

Launch the exercise and follow the instructions. When you're done, be sure to return to this page so you can continue learning.

> **Note**: To complete this lab you will need an **Azure subscription**.
>

## 6.4 Exercise - Monitor web apps

This guided project consists of the four exercises:
* Exercise 1: Deploy Log Analytics
* **Exercise 2: Monitor web apps**
* Exercise 3: Configure monitoring for compute services
* Exercise 4: Configure alerts

In Exercise 2, you configure monitoring for web applications.
* Task 1: Enable Application Insights.
* Task 2: Disable logging for .NET core snapshot debugger.
* Task 3: Configure web app HTTP logs to be written to a Log Analytics workspace.
* Task 4: Configure SQL Insights data to be written to a Log Analytics workspace.
* Task 5: Enable file and configuration change tracking for web apps.

Launch the exercise and follow the instructions. When you're done, be sure to return to this page so you can continue learning.

> **Note**: To complete this lab you will need an **Azure subscription**.


## 6.5 Exercise - Configure monitoring for compute services

This guided project consists of the four exercises:
* Exercise 1: Deploy Log Analytics
* Exercise 2: Monitor web apps
* **Exercise 3: Configure monitoring for compute services**
* Exercise 4: Configure alerts

In Exercise 3, you configure monitoring for compute services and perform tasks related to integrating IaaS virtual machines with Azure Monitor. You create a data collection endpoint and a data collection rule to collect Windows Event logs. You then add an existing IIS log collection to the data collection rule. Finally, you configure Network Connection Monitor for a Linux IaaS virtual machine.

* Task 1: Create a data collection endpoint.
* Task 2: Create a data collection rule.
* Task 3: Add an IIS log collection to an existing data collection rule.
* Task 4: Configure Network Connection Monitor for a Linux IaaS virtual machine.

> **Note**: To complete this lab you will need an **Azure subscription**.

## 6.6 Exercise - Configure alerts

This guided project consists of the four exercises:
* Exercise 1: Deploy Log Analytics
* Exercise 2: Monitor web apps
* Exercise 3: Configure monitoring for compute services
* **Exercise 4: Configure alerts**

In Exercise 4, you configure two specific alerts: an action group to send an email, and an alert for virtual machine CPU utilization.
* Task 1: Create an action group to send an email.
* Task 2: Create an alert for virtual machine CPU utilization.

> **Note**: To complete this lab you will need an **Azure subscription**.

## 7 Module assessment

## Answer the following questions

Choose the best response for each of the following questions.

### 1.
**Tailwind Traders has a subscription that contains multiple Log Analytics workspaces across multiple resource groups. The administrator needs to assign the Log Analytics Reader role to a new user. Which scope should the role assignment be configured to allow the user access to all the Log Analytics workspaces in a specific resource group?**

- Subscription
- **Resource group**
- Resource

### 2.
**Tailwind Traders needs to collect information about all HTTP requests and responses that occur on their web server. An IT staff member decides to create a data collection rule that collects this information from virtual machines that are monitored with Azure Monitor Agent. When configuring the data collection rule, which data source should the staff member specify?**

- Performance counters
- Windows event logs
- **IIS logs**

### 3.
**Tailwind Traders needs to set up an Azure Resource Health alert that notifies them of any changes in the health status of any resources due to a restart or a shutdown. Which type of alert should be used?**

- **Activity log alert**
- Metric alert
- Log alert



