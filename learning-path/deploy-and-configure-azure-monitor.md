

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




