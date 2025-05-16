
# Azure Internship Capstone Project

## Task: Create Demo Project on Alerts in Azure Monitor for Django Web Application


### Alerts Monitoring
Alerts proactively notify you when issues are found with your infrastructure or application using your monitoring data in Azure Monitor. They allow you to identify and address issues before the users of your system notice them.

--------------------------------------------------------------------------------------------------------------------------

# Weekly Progress: Django App Monitoring in Azure 
*02/05/2025 - 09/05/2025*

## Achievements This Week

### 🚀 Django Web Application Deployment
Successfully deployed a Python Django web application with PostgreSQL in Azure:
- Configured development environment and Azure resources
- Set up PostgreSQL database and connection
- Deployed fully functional application to Azure App Service

![Azure Resources Overview](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/0_AzureResources_1.png)

**Live Demo:** [msdocs-python-postgres-235](https://msdocs-python-postgres-235-cmb4dccwfbf7emhx.westeurope-01.azurewebsites.net/)

### 📊 Application Monitoring Implementation
- Integrated Application Insights SDK with Django application
- Configured comprehensive telemetry collection
- Designed custom dashboards for application metrics visualization
- Implemented HTTP error tracking and performance monitoring

### 🔔 Alert System Configuration (50% Complete)
Configured multiple alert types in Azure Monitor:
- Availability monitoring for critical endpoints
- Performance thresholds for response times
- Resource utilization warnings for database and app service
- HTTP 4xx error rate tracking

### 🧪 Testing Framework Development
Created a sophisticated testing utility to validate monitoring setup:

https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/generate_400_errors.py

```python
# Test your application's error handling with a single command
python generate_400_errors.py https://your-app.azurewebsites.net --iterations 200 --concurrency 10
```

#### HTTP 400 Error Simulator Features:
- **Multi-vector Testing:** Generates diverse malformed requests including invalid parameters, malformed headers, invalid HTTP methods, and unsafe URLs
- **Concurrent Execution:** Simulates realistic user patterns with configurable parallel requests
- **Detailed Analytics:** Provides real-time statistics on error generation and application responses
- **Security Probing:** Tests application resilience against common attack patterns

## Skills Development

- ✅ Completed 100% of "Data Analysis with Kusto Query Language" course
  - Applied KQL to analyze application logs and create custom monitoring queries
  
- ✅ Progressed through 50% of "Developing a Site Reliability Engineering (SRE) Strategy" learning path
  - Implemented SRE best practices in monitoring configuration
  - Applied SLA-based alerting thresholds

## Next Steps

- Complete the preparation of a full Azure Monitor alert demo for a Django web application, including all alert types (metrics, logs, availability, errors, anomalies).
- Prepare a presentation script with a step-by-step demonstration of all aspects of working with alerts - from creating rules to responding to incidents.
- Develop a comprehensive monitoring system for a Django application using custom metrics and KQL queries to identify non-trivial performance issues.


---

![Azure Resource Configuration](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/0_AzureResources_2.png)

> **Project Repository:** [Azure-Internship-Capstone-Project](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project)


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Weekly Report: 12/05/2025 - 16/05/2025

##  Setting Up Alerts in Azure Monitor

## Key Steps for Alert Configuration

### 1. Accessing Alert Creation
- Open Azure Monitor

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/1_AzureMonitor.png)
  
- Navigate to the "Alerts" section

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/2_AzureMonitor.png)
  
- Click "Add new alert rule"

### 2. Defining the Target Resource (Scope)
- Select the resource(s) you want to monitor

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/3_AzureMonitor.png)

- Available signals depend on the chosen scope:
  * At subscription level - activity log signals are available
  * At VM level - metric and activity log signals are available
  * For Log Analytics workspace - log signals are available
- Multi-resource metric alert rules are supported for specific resource types

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/4_AzureMonitor.png)

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/5_AzureMonitor.png)





### 3. Configuring Alert Conditions
Azure offers three main types of alerts:

#### a) Metric Alerts
- Based on time series data emitted by Azure resources
- You need to select:
  * A specific metric of interest
  * Aggregation type
  * Threshold value for triggering

#### b) Log Alerts
- Based on queries against logs stored in a Log Analytics workspace
- Allow you to define complex scenarios for alerting
- Utilize the Log Analytics query language (KQL)

#### c) Activity Log Alerts
- Based on events from the activity log
- Notify you when specific events occur in your Azure environment

### 4. Defining Actions When Alert Triggers
- You can choose an existing Action Group or create a new one
- To create a new Action Group:
  * Provide a name for the Action Group
  * Input the name of the action
  * Select the action type (email, SMS, webhook, etc.)
  * Enter relevant details for the chosen action type

#### Additional Configuration for Webhooks:
- Enter your webhook URL to receive notifications
- It's recommended to enable the "Common Alert Schema" for standardized alert formats
- This simplifies automation of responses through webhooks, Logic Apps, or runbooks

### 5. Finalizing Settings
- Specify the alert name and description
- Define the severity level
- Click "Create alert rule" to complete



# Analysis of Azure Monitor Log Query Results

Based on the search results, the following is evident:

1. **Available Data Tables**:
   - The following tables are currently available in Azure Monitor:
     - `AppServiceHTTPLogs` - HTTP request logs from App Service
     - `AzureMetrics` - standard Azure metrics

2. **Available Data**:
   - Logs are dated from today (5/16/2025)
   - The most recent entry to `AppServiceHTTPLogs` was at 8:06:36.125 AM
   - Metrics (`AzureMetrics`) are collected at 1-minute intervals
   - Data is coming from an Azure subscription (ID starting with `/subscriptions/0023db84-3d8f-...`)





# References:

1) What Is a Capstone Project?, https://www.nu.edu/blog/what-is-a-capstone-project/
2) How to configure an Alert Rule with Azure Monitor, https://www.youtube.com/watch?v=ps4iasnS7Qs&t=64s

### Onboarding
3) Create, view, and manage metric alerts in Azure Monitor,  https://learn.microsoft.com/ru-ru/azure/azure-monitor/alerts/alerts-create-metric-alert-rule?wt.mc_id=monitor_inproduct_overview_alerts_o
4) Create, view, and manage log alerts using Azure Monitor, https://learn.microsoft.com/ru-ru/azure/azure-monitor/alerts/alerts-create-log-alert-rule?wt.mc_id=monitor_inproduct_overview_alerts_o
5) Create, view, and manage activity log alerts by using Azure Monitor,  https://learn.microsoft.com/ru-ru/azure/azure-monitor/alerts/alerts-create-activity-log-alert-rule?wt.mc_id=monitor_inproduct_overview_alerts_o&tabs=activity-log

### Tutorials
6) Improve incident response with alerting on Azure, https://learn.microsoft.com/ru-ru/training/modules/incident-response-with-alerting-on-azure/?wt.mc_id=monitor_inproduct_overview_alerts_t

### Scenario Guidance
7) Configure actions, https://learn.microsoft.com/ru-ru/azure/azure-monitor/alerts/action-groups?wt.mc_id=monitor_inproduct_overview_alerts_s  
8) Suppress alerts and configure actions at-scale, https://learn.microsoft.com/ru-ru/azure/azure-monitor/alerts/alerts-processing-rules?wt.mc_id=monitor_inproduct_overview_alerts_s&tabs=portal 


### Learning paths
9)   Discover data analysis, https://learn.microsoft.com/en-us/training/modules/data-analytics-microsoft/
10)  Data analysis with Kusto Query Language, https://learn.microsoft.com/en-us/training/paths/kusto-query-language/
11)  Data analysis with Kusto Query Language, https://learn.microsoft.com/en-us/training/paths/kusto-query-language/
12)  Analyze monitoring data with Kusto Query Language, https://learn.microsoft.com/en-us/training/paths/analyze-monitoring-data-with-kql/
13) Data analysis in Azure Data Explorer with Kusto Query Language, https://learn.microsoft.com/en-us/training/paths/data-analysis-data-explorer-kusto-query-language/







