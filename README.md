
# 🛡️ Proactive Security Monitoring for Django Applications in Azure

<p align="center">
  <img src="https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/project_banner.png" alt="Project Banner" width="800">
</p>

> A comprehensive security monitoring and alerting system built on Azure Monitor to detect threats and vulnerabilities in Django applications before they can be exploited.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.0+-green.svg)](https://www.djangoproject.com/)
[![Azure](https://img.shields.io/badge/Azure-Monitor-0078D4.svg)](https://azure.microsoft.com/services/monitor/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🔍 Project Overview

This capstone project transforms standard application monitoring into a robust security monitoring system for Django applications deployed in Azure. By leveraging Azure Monitor capabilities and security engineering principles, we've created an early warning system for potential security threats and application vulnerabilities.

<p align="center">
  <img src="https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/0_AzureResources_1.png" alt="Architecture Diagram" width="700">
</p>

### 🚀 [Live Demo](https://msdocs-python-postgres-235-cmb4dccwfbf7emhx.westeurope-01.azurewebsites.net/)

## 🎯 Security Objectives

- **Threat Detection**: Real-time alerting on potentially malicious HTTP requests and injection attempts
- **Access Monitoring**: Identification of unusual access patterns and authentication anomalies
- **Vulnerability Discovery**: Early detection of application weaknesses through error rate analysis
- **Behavioral Analysis**: Creation of security baselines with alerting on suspicious deviations
- **Defense in Depth**: Implementation of multi-layered monitoring for comprehensive coverage

## 🛠️ Core Security Monitoring Components  

1. **Attack Vector Detection**: Tracking and alerting on SQL injection, XSS, and path traversal attempts
2. **Authentication Monitoring**: Identifying brute force attempts and unauthorized access patterns
3. **Security-focused KQL Queries**: Advanced threat detection using Kusto Query Language
4. **Incident Response Automation**: Configuring security playbooks for common attack scenarios
5. **Security Testing Framework**: Specialized tools to simulate attack vectors and validate defense mechanisms

### Security Value Proposition

This security monitoring solution enhances the application's security posture by:

- Providing real-time visibility into potential security incidents
- Reducing the attack surface through early vulnerability detection
- Creating an audit trail of security-relevant events for compliance
- Enabling rapid incident response through automated alerting
- Building a security knowledge base through trend analysis of attack patterns

The project serves as a security operations blueprint for Django applications in Azure, demonstrating how to transform standard application monitoring into a robust security monitoring system that aligns with the principle of "shifting security left" in the development lifecycle.

--------------------------------------------------------------------------------------------------------------------------

# Weekly Progress: Django App Monitoring in Azure 
*02/05/2025 - 09/05/2025*

## Achievements This Week

### 🚀 Django Web Application Deployment
Successfully deployed a Python Django web application with PostgreSQL in Azure:
- Configured development environment and Azure resources
- Set up PostgreSQL database and connection
- Deployed fully functional application to Azure App Service

  https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/django-postgresql-sample-app-on-azure.md

![Azure Resources Overview](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/0_AzureResources_1.png)

**Live Demo:** [msdocs-python-postgres-235](https://msdocs-python-postgres-235-cmb4dccwfbf7emhx.westeurope-01.azurewebsites.net/)

### 📊 Application Monitoring Implementation
- Integrated Application Insights SDK with Django application
- Configured comprehensive telemetry collection
- Designed custom dashboards for application metrics visualization
- Implemented HTTP error tracking and performance monitoring

### Application Insights overview

Azure Monitor Application Insights is an OpenTelemetry feature of Azure Monitor that offers application performance monitoring (APM) for live web applications. Integrating with OpenTelemetry (OTel) provides a vendor-neutral approach to collecting and analyzing telemetry data, enabling comprehensive observability of your applications.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/10_AzureMonitor_ApplicationInsightsOverview_1.png)

The logic model diagram visualizes components of Application Insights and how they interact.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/10_AzureMonitor_ApplicationInsightsOverview_2.svg)


![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/10_AzureMonitor_ApplicationInsightsOverview_4.png)
![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/10_AzureMonitor_ApplicationInsightsOverview_5.png)
![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/10_AzureMonitor_ApplicationInsightsOverview_6.png)
![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/10_AzureMonitor_ApplicationInsightsOverview_7.png)


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

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/5_AzureMonitor_.png)

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/6_AzureMonitor.png)




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

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/7_AzureMonitor.png)

2. **Available Data**:
   - Logs are dated from today (5/16/2025)
   - The most recent entry to `AppServiceHTTPLogs` was at 8:06:36.125 AM
   - Metrics (`AzureMetrics`) are collected at 1-minute intervals
   - Data is coming from an Azure subscription (ID starting with `/subscriptions/0023db84-3d8f-...`)


![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/8_AzureMonitor.png)
![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/9_AzureMonitor.png)




# References:

1) What Is a Capstone Project?, https://www.nu.edu/blog/what-is-a-capstone-project/
2) How to configure an Alert Rule with Azure Monitor, https://www.youtube.com/watch?v=ps4iasnS7Qs&t=64s
3) Introduction to Microsoft Azure Application Insights, https://www.youtube.com/watch?v=FPRo0hnHl7M
4) Introduction to Application Insights - OpenTelemetry observability, https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview
5) Monitoring Django App with Azure Application Insights, https://blog.jcharistech.com/2022/10/31/monitoring-django-app-with-azure-application-insights/
6) Using Azure Application Insights in a dockerized Django, https://django.fun/qa/425698/
7) ApplicationInsightsMiddleware Class, https://learn.microsoft.com/en-us/python/api/botbuilder-applicationinsights/botbuilder.applicationinsights.django.applicationinsightsmiddleware?view=botbuilder-py-latest
8) Django, Flask, FastAPI and Azure OpenTelemetry, https://www.youtube.com/watch?v=K_fn6nXHa0s
9) How to send Python logs to Applications Insights (Azure Monitor), https://www.youtube.com/watch?v=EimFeRKuVb8
10) Python Metrics in Azure Application Insights, https://www.youtube.com/watch?app=desktop&v=ZEeVpRR25S4&t=0s
11) Unlock the Power of Azure Monitor & Application Insights, https://www.youtube.com/watch?v=lBpWvqI-3PI
12) SDE Bootcamp 10: Monitor your application with Zero code in Azure with Azure App insights, https://www.youtube.com/watch?v=yW8Zgp5Vy64
   
   

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


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 1. Attack Vector Detection System

```kusto
// SQL Injection Detection
AppServiceHTTPLogs
| where CsUriStem contains "SELECT" or CsUriStem contains "UNION" or CsUriStem contains "DROP"
| project TimeGenerated, CsUriStem, CsMethod, ScStatus, CIp
| order by TimeGenerated desc
```

### 2. Authentication Security Monitoring

Tracks authentication patterns and detects potential brute force attacks using custom metrics and KQL queries.

### 3. Security-focused KQL Query Library

Repository of specialized Kusto Query Language scripts for threat detection and security analysis.

### 4. Incident Response Automation

<p align="center">
  <img src="https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/alert_workflow.png" alt="Alert Workflow" width="600">
</p>

### 5. Security Testing Framework

```bash
# Generate simulated attack patterns to test detection capabilities
python generate_400_errors.py https://your-app.azurewebsites.net --iterations 200 --concurrency 10 --types param,url
```

## 📊 Security Value Proposition

- **Visibility**: Real-time dashboard of security-relevant events and potential threats
- **Proactive Defense**: Early detection of vulnerabilities before exploitation
- **Compliance**: Comprehensive audit trail for security events and responses
- **Efficiency**: Automated alerting and incident response procedures
- **Intelligence**: Trend analysis of attack patterns for continuous improvement

## 🚀 Getting Started

1. Clone this repository
2. Deploy the Django application to Azure App Service
3. Configure Application Insights for your application
4. Import alert templates and KQL queries
5. Run the security testing framework to validate configurations

## 📚 Documentation

- [Setup Guide](docs/setup.md)
- [Alert Configuration](docs/alerts.md)
- [KQL Query Library](docs/kql-library.md)
- [Testing Framework](docs/testing.md)
- [Security Best Practices](docs/best-practices.md)

## 🔗 Azure Resources

<p align="center">
  <img src="https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/0_AzureResources_2.png" alt="Azure Resources" width="700">
</p>

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Microsoft Azure Documentation
- Django Security Team
- Azure Security Center Guidelines

---

<p align="center">
  <i>Developed as part of the Azure Internship Capstone Project</i><br>
  <i>© 2025 Security Engineering Lab</i>
</p>



---------------------------------------------
# Azure Internship Capstone Project

## Proactive Security Monitoring for Django Applications in Azure

## (Previos: Create Demo Project on Alerts in Azure Monitor for Django Web Application)

### Project Overview

This project implements a security-focused monitoring and alerting system for Django web applications deployed in Azure. By combining Azure Monitor capabilities with security engineering principles, we've created an early warning system that detects potential security threats, anomalous behavior, and application vulnerabilities before they can be exploited.

### Security Objectives

- Detect and alert on potentially malicious HTTP requests and injection attempts
- Monitor for unusual access patterns and authentication anomalies
- Identify application vulnerabilities through error rate analysis
- Create security baselines and detect deviations in application behavior
- Implement defense-in-depth through multi-layer monitoring





