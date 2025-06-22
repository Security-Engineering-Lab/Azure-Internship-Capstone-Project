
# 🛡️ Proactive Security Monitoring for Django Web Applications in Azure

<p align="center">
  <img src="https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/project_banner.png" alt="Project Banner" width="800">
</p>

> A comprehensive security monitoring and alerting system built on Azure Monitor to detect threats and vulnerabilities in Django applications before they can be exploited.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.0+-green.svg)](https://www.djangoproject.com/)
[![Azure](https://img.shields.io/badge/Azure-Monitor-0078D4.svg)](https://azure.microsoft.com/services/monitor/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🔍 Short Introduction

This Azure Internship Capstone Project demonstrates the implementation of an advanced security monitoring system that transforms traditional application monitoring into a comprehensive threat detection platform for Django web applications deployed in Microsoft Azure.

### What This Project Does

By leveraging **Azure Monitor** and **Application Insights**, we've built an intelligent early warning system that:
- **Detects security threats in real-time** before they can compromise your application
- **Monitors for attack patterns** including SQL injection, XSS, and brute force attempts
- **Analyzes user behavior** to identify suspicious activities and anomalies
- **Automates incident response** through customized alerts and security playbooks

### Why It Matters

Traditional monitoring focuses on performance metrics, but this project addresses the critical gap in **proactive security monitoring**. It embodies the "shift security left" principle by identifying vulnerabilities and threats at the earliest possible stage, significantly reducing the attack surface and potential impact of security incidents.

### Key Innovation

Unlike standard monitoring solutions, this system uses **security-focused KQL queries** and **custom threat detection algorithms** specifically tailored for Django applications, providing security teams with actionable intelligence rather than just raw data.

### Target Audience

- **Security Engineers** implementing DevSecOps practices
- **Django Developers** building secure cloud applications  
- **Azure Architects** designing resilient monitoring systems
- **IT Security Teams** seeking proactive threat detection

This project serves as both a working implementation and a blueprint for establishing robust security monitoring in Azure-hosted Django applications, demonstrating how modern cloud platforms can be leveraged to create sophisticated security operations centers.

---

*🚀 [View Live Demo](https://msdocs-python-postgres-235-cmb4dccwfbf7emhx.westeurope-01.azurewebsites.net/) | 📁 [Explore Repository](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project)*



![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/2_workbooks.png)

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/3_dashboard.png)


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

## !!!
## Capture Web Application Logs with App Service Diagnostics Logging

Use application logs in Azure Web Apps for debugging web app code.

https://learn.microsoft.com/en-us/training/modules/capture-application-logs-app-service/2-enable-and-configure-app-service-application-logging





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


### Setting Up Azure Application Insights for Django Web Application

#### Step-by-Step Process Overview

Here's a comprehensive walkthrough of how to set up and integrate Azure Application Insights with a Django web application:

#### 1. Creating a New Application Insights Resource

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/10_AzureMonitor_ApplicationInsightsOverview_4.png)

As shown in Image 1, the process begins with creating a new Application Insights resource:

- **Navigate to**: Home > Monitor | Applications > Application Insights
- **Resource Configuration**:
  - Subscription: Azure subscription 1
  - Resource Group: msdocs-django-postgres-tutorial-1
  - Name: DjangoWebApp_ApplicationInsights (highlighted in red box)
  - Region: (Europe) West Europe
  - Log Analytics Workspace: DefaultWorkspace with unique identifier

This configuration step establishes the monitoring service that will collect and analyze your Django application's telemetry data.

#### 2. Resource Validation and Creation
![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/10_AzureMonitor_ApplicationInsightsOverview_5.png)

Image 2 shows the validation and confirmation step:

- All configuration parameters are reviewed
- The system performs validation checks (shown as "Validation passed")
- Details of the configured resource are displayed:
  - Application Insights by Microsoft
  - Resource specifications matching those entered in step 1
- To complete the setup, click the "Create" button (highlighted in red)

#### 3. Deployment Confirmation

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/10_AzureMonitor_ApplicationInsightsOverview_6.png)

Image 3 displays the deployment completion screen:

- A success message: "Your deployment is complete"
- Deployment details including:
  - Deployment name: Microsoft.AppInsights
  - Start time: 5/17/2025, 8:24:59 AM
  - Correlation ID: 2a774b94-6b1d-4eb2-bedf-9820b2011457
- Resources successfully deployed:
  - DjangoWebApp_ApplicationInsights
  - newWorkspaceTemplate
- A "Go to resource" button to access the newly created resource

#### 4. Application Insights Dashboard

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/10_AzureMonitor_ApplicationInsightsOverview_7.png)

- The resource overview page displays essential monitoring metrics
- Key information highlighted includes:
  - **Connection String** (highlighted in red): This is critical for integrating with your Django application
  - **Instrumentation Key**: 255bXXXX-XXXX-XXXX-b124-41b28399XXXX
- Dashboard panels showing:
  - Failed requests
  - Server response time
  - Server requests
  - Availability metrics
- Time range filter options (30 minutes to 30 days)


#### Implementation in Django

To integrate this Application Insights resource with Django project:

1. Copy the Connection String highlighted in Image 4
2. Add it to your Django application's environment variables:
   ```bash
   APPLICATIONINSIGHTS_CONNECTION_STRING="InstrumentationKey=255b5d65-XXXX-XXXX-XXXX-41b283997035;IngestionEndpoint=..."
   ```

3. Installing the Required Packages

```bash

# Install OpenTelemetry packages
pip install azure-monitor-opentelemetry
```

4. Modify your `wsgi.py` file to include:
   ```python
   import os
   from django.core.wsgi import get_wsgi_application
   from azure.monitor.opentelemetry import configure_azure_monitor

   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yourproject.settings')

   if os.environ.get("APPLICATIONINSIGHTS_CONNECTION_STRING"):
       configure_azure_monitor()

   application = get_wsgi_application()
   ```





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

-------------------------------------------------------------------------------------------------------------------------------------------------------------


# KQL Query Explanation

This query analyzes web application HTTP logs to detect 400 errors within the last 5 minutes. Let's break it down step by step:

## Step-by-Step Explanation

### 1. `AppServiceHTTPLogs`
- **What it does:** Selects the table containing HTTP logs from Azure App Service
- **Contains:** All HTTP requests to your web application (URLs, status codes, IP addresses, etc.)

### 2. `| where TimeGenerated >= ago(5m)`
- **What it does:** Filters records by time
- **Result:** Shows only records from the last 5 minutes
- **ago(5m)** = 5 minutes ago from current time

### 3. `| where ScStatus == 400`
- **What it does:** Filters by HTTP status code
- **Result:** Keeps only requests with 400 error (Bad Request)
- **ScStatus** = Server Status Code

### 4. `| summarize Count = count() by bin(TimeGenerated, 1m)`
- **What it does:** Groups and counts records
- **Count = count()** = counts the number of records in each group
- **bin(TimeGenerated, 1m)** = groups by minutes (each minute = one "bin")
- **Result:** Number of 400 errors for each minute

### 5. `| where Count > 0`
- **What it does:** Shows only minutes where errors occurred
- **Result:** Hides minutes with zero error count

## Example Output

| TimeGenerated | Count |
|---------------|-------|
| 2025-05-27 14:55:00 | 3 |
| 2025-05-27 14:57:00 | 1 |
| 2025-05-27 14:59:00 | 2 |

## Practical Use Cases

This query is perfect for:
- **Real-time monitoring** - detecting issues quickly
- **Alert rules** - automatic notifications when errors occur
- **Trend analysis** - understanding error frequency patterns

## Possible Modifications

**For longer time period:**
```kusto
| where TimeGenerated >= ago(1h)  // Last hour
```

**For other errors:**
```kusto
| where ScStatus >= 400 and ScStatus < 500  // All client errors
```


-------------------------------------------------------------------------------------------------------------------------------------------

## Email Nofification

## Azure Monitor Alert - HTTP 400 Errors Description

**Alert Overview:**
This is a Severity 3 (Sev3) Azure Monitor alert that fired on May 27, 2025 at 8:06:30 AM UTC, indicating HTTP 400 errors detected in a Django web application.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/11_Azure%20Monitor%20Alert%20HTTP400-Alerts%20on%20djangowebapp_01.png)
![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/images/11_Azure%20Monitor%20Alert%20HTTP400-Alerts%20on%20djangowebapp%20_02.png)

**Technical Details:**
- **Alert Name:** HTTP400-Alerts
- **Affected Resource:** djangowebapp
- **Resource Type:** microsoft.operationalinsights/workspaces
- **Resource Group:** msdocs-django-postgres-tutorial-1
- **Monitoring Service:** Log Alerts V2
- **Signal Type:** Log-based alert

**Alert Configuration:**
- **Monitor Condition:** Fired (alert threshold exceeded)
- **Description:** HTTP 400 Errors Detected in DjangoWebApp
- **Alert ID:** 0eefbe32-0b2a-283e-ed86-cc234bc3000e
- **Alert Rule Location:** Azure portal with specific subscription and resource group path

**Incident Summary:**
This alert indicates that the Django web application is experiencing HTTP 400 (Bad Request) errors, which typically occur when the server cannot process a request due to client-side issues such as malformed syntax, invalid request message framing, or deceptive request routing. The alert is configured to monitor application logs and trigger when the threshold for 400-level errors is exceeded.

**Recommended Actions:**
1. Click "View the alert in Azure Monitor" to access detailed logs
2. Use "Investigate" button for deeper analysis
3. Review application logs for specific error patterns
4. Check recent deployments or configuration changes
5. Verify client request formats and API endpoints

-------------------------------------------------------------------------------------------------------------------------------------------


# Weekly Standup Report
**Reporting Period:** [Week of Date]  
**Team Member:** [Your Name]

## What I Accomplished This Week

### **Completed Learning Modules**
- ✅ **Finished SC-200: Create Queries for Microsoft Sentinel using KQL** 
  - Successfully completed 5.5-hour learning path with 100% achievement
  - Mastered advanced KQL syntax for security data analysis
  - Developed proficiency in threat hunting and incident investigation queries

- ✅ **Finished SC-200: Configure Microsoft Sentinel Environment**
  - Completed 5.5-hour comprehensive configuration training
  - Gained expertise in workspace setup, data connectors, and analytics rules
  - Learned automation and SOC optimization best practices

### **Project Development Progress**
- 🔄 **Azure Internship Capstone Project: Advanced 20 hours of development**
  - Continued work on "Proactive Security Monitoring for Django Web Applications in Azure"
  - Implemented custom threat detection algorithms using learned KQL skills
  - Integrated Application Insights with Django application for comprehensive monitoring
  - Developed automated alerting system and incident response workflows

### **Professional Development Activities**
- 🔄 **Onboarding Activities: Progressed 4 hours**
  - Completed team integration sessions and process familiarization
  - Established stakeholder communication protocols
  - Aligned project deliverables with organizational objectives

- 🔄 **Updated Professional Profile: 80% completion (4 hours invested)**
  - Enhanced work experience documentation in Telescope platform
  - Updated skills matrix and achievement tracking
  - Refined career progression planning

## What I'm Working on Next Week

### **Primary Focus Areas**
1. **Azure Monitor Practical Implementation**
   - Create new alert rules based on learned KQL techniques
   - Implement advanced monitoring scenarios for production environments
   - Practice hands-on configuration and optimization

2. **Capstone Project Completion**
   - Finalize security monitoring framework documentation
   - Complete testing and validation of threat detection algorithms
   - Prepare project presentation and deliverables

3. **Continue Security Compliance Learning**
   - Advance through "Secure Azure Services with Microsoft Defenders" learning path
   - Focus on regulatory compliance controls and governance frameworks

## Blockers & Support Needed

### **Current Challenges**
- No significant blockers at this time
- Azure subscription credits expired - resolved through account upgrade
- Need additional time allocation for hands-on Azure Monitor practice

### **Support Requests**
- **Resource Access:** Confirmation of continued Azure environment access for practical exercises
- **Project Review:** Schedule review session for capstone project milestone assessment
- **Learning Path Priority:** Guidance on prioritizing between AZ-500 preparation and current compliance learning track

## Key Metrics & Progress Indicators

- **Learning Completion Rate:** 100% on structured modules (11 total hours completed)
- **Project Investment:** 20+ hours dedicated to hands-on implementation
- **Overall Status:** 🟢 **ON TRACK** - Meeting all scheduled milestones
- **Skill Development:** Successfully applying learned KQL skills in practical project scenarios

## Next Week's Commitments

1. **Complete Azure Monitor alert rule implementation** (Target: 6 hours)
2. **Advance capstone project to 75% completion** (Target: 15 hours)  
3. **Finish regulatory compliance learning module** (Target: 2 hours)
4. **Prepare mid-week project status update** for stakeholder review

---

**Overall Assessment:** Strong momentum maintained across all development tracks. Successfully bridging theoretical learning with practical implementation. Ready to accelerate project completion in upcoming week.


---------------------------------------------------------------------------------------------

# Weekly Standup Report
**Reporting Period:** 02.06.2025 - 06.06.2025   
**Team Member:** [Your Name]

## What I Accomplished This Week

## What I Accomplished This Week

This week I focused on expanding my GitHub expertise by completing two comprehensive Learning Paths that covered both foundational and advanced GitHub concepts.

### Completed Learning Paths:

**1. GitHub Foundations Part 1 of 2**
- URL: https://learn.microsoft.com/en-us/training/paths/github-foundations/
- **Key Areas Covered:**
  - InnerSource fundamentals and program management
  - Repository security and supply chain protection
  - GitHub administration and organizational structure
  - Authentication and authorization strategies

**2. GitHub Foundations Part 2 of 2** 
- URL: https://learn.microsoft.com/en-us/training/paths/github-foundations-2/
- **Key Areas Covered:**
  - Advanced authentication methods (SAML SSO, 2FA)
  - Team synchronization with identity providers
  - Pull request workflows and collaboration
  - Enterprise-level access management

### Specific Technical Focus Areas:

**GitHub Security Integration:**
- Studied how to secure GitHub repositories as part of Azure internship capstone project
- Learned repository security best practices including dependency scanning, secret scanning, and code scanning
- Explored automated security features and vulnerability management

**Azure Entra ID Integration:**
- Deep dive into synchronizing GitHub with Azure Entra ID (formerly Active Directory)
- Learned SAML SSO configuration and enforcement strategies
- Studied team synchronization capabilities between Azure AD groups and GitHub teams
- Explored SCIM provisioning for automated user lifecycle management

### Practical Applications:

- **Enterprise Security:** Understanding how to implement organization-wide security policies
- **Identity Management:** Learned to centralize authentication through Azure Entra ID
- **Access Control:** Studied fine-grained permission models and repository access management
- **Automation:** Explored automated user provisioning/deprovisioning workflows

## Key Takeaways for Reporting:

This learning directly supports enterprise-level GitHub implementations and provides crucial knowledge for:
- Securing organizational repositories and sensitive code
- Implementing proper authentication and authorization controls
- Managing large-scale user access through identity provider integration
- Establishing governance frameworks for development teams

These skills are particularly relevant for organizations looking to adopt GitHub Enterprise while maintaining security compliance and operational efficiency.

## Next Steps:

I plan to apply this knowledge to the Azure capstone project and explore practical implementation scenarios for GitHub-Azure Entra ID integration in enterprise environments.

--------------------------------------------------------------------------------------------


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
13) 𝗘𝗡𝗗-𝗧𝗢-𝗘𝗡𝗗 𝗔𝗭𝗨𝗥𝗘 𝗗𝗘𝗩𝗢𝗣𝗦 𝗣𝗥𝗢𝗝𝗘𝗖𝗧 𝗔𝗨𝗧𝗢𝗠𝗔𝗧𝗜𝗢𝗡, https://medium.com/@capukvelu/-036f4dd73011
14) Understanding Azure DevOps Pipeline — A CI/CD Blueprint for Modern Cloud Deployments, https://medium.com/@capukvelu/understanding-azure-devops-pipeline-a-ci-cd-blueprint-for-modern-cloud-deployments-f3ce1069dd8f
15) How Azure DevOps Works, https://medium.com/@capukvelu/how-azure-devops-works-ba1b53579ab3
16) Top 10 Terraform tips for Infrastructure Automation, https://medium.com/@devops4solutions/top-10-terraform-tips-for-infrastructure-automation-9f85e8c4e60d
17) Deploying an AWS EKS Cluster Using Terraform and GitHub Actions, https://medium.com/@devops4solutions/deploying-an-aws-eks-cluster-using-terraform-and-github-actions-eaad8d80e6e1
18) 
    
   
   

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


## 🔍 Project Overview

This capstone project transforms standard application monitoring into a robust security monitoring system for Django applications deployed in Azure. By leveraging Azure Monitor capabilities and security engineering principles, we've created an early warning system for potential security threats and application vulnerabilities.

### !!!!
#### Full-stack monitoring in Azure
#### Monitor web (Django) applications
#### Monitor your infrastructure
#### Monitor Azure platform resources
#### Monitor security



# Cybersecurity Roles

- These Cybersecurity Roles Are the Future: How to Thrive in the Age of AI, https://medium.com/aws-in-plain-english/these-cybersecurity-roles-are-the-future-how-to-thrive-in-the-age-of-ai-94b39a75b788
- CERTIFICATIONS THAT ARE REQUIRED IN CYBERSECURITY, https://medium.com/devsecops-ai/certifications-that-are-required-in-cybersecurity-ac987d3eed70

  

- Anomalous Behavior Detection for SOC: Advanced Monitoring Techniques with UEBA, https://medium.com/@esrakyhn/anomalous-behavior-detection-for-soc-advanced-monitoring-techniques-with-ueba-aa47d4ca647d
- AI-Based Threat Hunting, https://medium.com/@esrakyhn/ai-based-threat-hunting-9150633cb30e
- Example Alert Rules in Wazuh, https://medium.com/@esrakyhn/example-alert-rules-in-wazuh-bfdc027020f9
- CI/CD Pipeline Security: DevSecOps Best Practices for 2025, https://medium.com/@rizqimulkisrc/ci-cd-pipeline-security-devsecops-best-practices-for-2025-6cc1946f3f13
- From Recon to Report: Automate Your Pentesting Workflow With Python, https://medium.com/the-first-digit/from-recon-to-report-automate-your-pentesting-workflow-with-python-fe0721ff66c9
- How to Implement a Zero Trust Architecture in Your Network, https://medium.com/infosecmatrix/how-to-implement-a-zero-trust-architecture-in-your-network-6cba1ff54845
- How to Build a Scalable Network Security Architecture for Enterprises, https://medium.com/infosecmatrix/how-to-build-a-scalable-network-security-architecture-for-enterprises-ac21d52fc469
- Top 20 Automation Scripts for Ethical Hackers and Security Analysts, https://medium.com/the-first-digit/top-20-automation-scripts-for-ethical-hackers-and-security-analysts-1f5a0954d481
- Anomalous Behavior Detection for SOC: Advanced Monitoring Techniques with UEBA, https://medium.com/@esrakyhn/anomalous-behavior-detection-for-soc-advanced-monitoring-techniques-with-ueba-aa47d4ca647d
- PentestGPT: The Future of Automated Penetration Testing with AI, https://medium.com/@Ekenejoseph/pentestgpt-the-future-of-automated-penetration-testing-with-ai-256799a378ae
- Kali GPT: The Future of AI-Driven Cybersecurity Tools in Kali Linux, https://medium.com/@Ekenejoseph/kali-gpt-the-future-of-ai-driven-cybersecurity-tools-in-kali-linux-544824b878ea
- Detect Vulnerabilities With Nuclei AI, https://medium.com/@loyalonlytoday/detect-bugs-with-nuclei-ai-59105992e798



#  Bug bounty
- Find your bug bounty target hidden directories, https://medium.com/@loyalonlytoday/find-your-bug-bounty-target-hidden-directories-f132f70bafe1
- A Hacker's Notebook: Real Techniques from the World of Bug Bounty (2025 Edition), https://medium.com/@verylazytech/a-hackers-notebook-real-techniques-from-the-world-of-bug-bounty-2025-edition-b7272595e681
- New Bug Bounty Platform for AI/ML, https://medium.com/meetcyber/huntr-bug-bounty-platform-for-ai-ml-c0e4413a7bec
- BI.ZONE Bug Bounty Platform, https://medium.com/@abhirupkonwar04/bi-zone-bug-bounty-platform-c1c3a6619696
-  

# OSINT
- Analyze any website with this awesome Osint tool, https://medium.com/the-first-digit/analyze-any-website-with-this-awesome-osint-tool-c11901629cc6
- Phone Number Investigation Tools For OSINT Investigators, https://medium.com/@loyalonlytoday/phone-number-investigation-tools-for-osint-investigators-52571c4d82bc
- A list of datasets for OSINT Investigators, https://medium.com/@loyalonlytoday/a-list-of-datasets-for-osint-investigators-8521490a7f5e
- Telegram bots for OSINT, https://medium.com/the-first-digit/telegram-bots-for-osint-fd74575e8ff3
- Find the digital footprints of a person, https://medium.com/the-first-digit/find-the-digital-footprints-of-a-person-bcb30b11dd40
- AI Detection Tools For OSINT Investigators, https://medium.com/@loyalonlytoday/ai-detection-tools-for-osint-investigators-7f08d46c196b
- Free Social Media Intelligence(SOCMINT) Tools, https://medium.com/@loyalonlytoday/free-social-media-intelligence-socmint-tools-5c695ed644ec
- How to Find Info on Anyone Online (Even Without Hacking!), https://medium.com/@hartarto/how-to-find-info-on-anyone-online-even-without-hacking-e46623de7154
- A list of Paste sites for OSINT investigators, https://medium.com/@loyalonlytoday/a-list-of-paste-sites-for-osint-investigators-dc8cb7465067
- OSINT Data Analysis: Pyvis and Networkx, https://medium.com/@CyberRaya/osint-data-analysis-pyvis-and-networkx-24b00544e212
- X-OSINT: All in One OSINT tool, https://medium.com/the-first-digit/x-osint-all-in-one-osint-tool-9ef483d1d017


# LLM
- LLM Prompt Ideas for Red Teamers, https://medium.com/system-weakness/llm-prompt-ideas-for-red-teamers-4cf7837a3511
- ScrapeGraphAI: Automate Web Scraping With LLM, https://medium.com/@CyberRaya/scrapegraphai-automate-web-scraping-with-llm-1b8751130edd



# AI

- Building a Team of AI Agents in n8n, https://medium.com/towards-artificial-intelligence/building-a-team-of-ai-agents-in-n8n-a3b988500dd2
- n8n: The Future of Workflow Automation, https://medium.com/towards-artificial-intelligence/n8n-the-future-of-workflow-automation-3b6da1e6506b
- BlueTeamGPT: The AI Defender Every Security Team Needs, https://medium.com/@Ekenejoseph/blueteamgpt-the-ai-defender-every-security-team-needs-77389b061f10


# Azure Sentinel
- MSTICPy v1.0.0 and Jupyter Notebooks for CyberSec, https://medium.com/@msticpy/msticpy-v1-0-0-and-jupyter-notebooks-in-azure-sentinel-an-update-ac2f6df61f9e
- Writing a Data Provider for MSTICPy, https://medium.com/@msticpy/writing-a-data-provider-for-msticpy-a7c237775c6
- msticpy 0.9.0 — Pivot Functions, https://medium.com/@msticpy/msticpy-0-9-0-pivot-functions-2be851ae2001
- MSTICPy 0.8.8 Release, https://medium.com/@msticpy/msticpy-0-8-8-release-5e8fe28a77d6
- MSTICpy 0.7.0/1 Release, https://medium.com/@msticpy/msticpy-0-7-0-1-release-758c5cbbf06d
- Azure Sentinel Notebooks, https://github.com/Azure/Azure-Sentinel-Notebooks
- Unlock the Power of Azure’s Sentinel: The Ultimate Guard for Your Digital Fortress!, https://medium.com/data-analytics-magazine/unlock-the-power-of-azures-sentinel-the-ultimate-guard-for-your-digital-fortress-d20cf4a45964
- Microsoft Azure Sentinel 101: Linux Command Line Logging and Auditing Activity for Threats or Compromise using Snoopy, https://medium.com/@truvis.thornton/microsoft-azure-sentinel-101-linux-command-line-logging-and-auditing-activity-for-threats-or-34f0c6a5c522
- Microsoft Azure Sentinel 101: Timechart with week/month over week/month overlay — find changes in log ingestion, https://medium.com/@truvis.thornton/microsoft-azure-sentinel-101-timechart-with-week-month-over-week-month-overlay-find-changes-in-e25405fc973f
- Microsoft Azure Sentinel 101: Forwarding OpnSense logs to LogStash and parsing with Geo IP info before sending to Azure Sentinel, https://medium.com/@truvis.thornton/microsoft-azure-sentinel-101-forwarding-opnsense-logs-to-logstash-and-parsing-with-geo-ip-info-7a516c69eef2
- Microsoft Azure Sentinel 101: Log Source, Data Table & End Point Monitoring — Be alerted when a source goes down or stops responding, https://medium.com/@truvis.thornton/microsoft-azure-sentinel-101-log-source-dataable-end-point-monitoring-be-alerted-when-a-1ff4fae77892


# DevSecOps

- 10 Shell Scripts to Automate DevSecOps Workflows, https://medium.com/devsecops-ai/10-shell-scripts-to-automate-devsecops-workflows-a3bbd716775d
- 

# SOC 

- Build Your Own AI SOC — Part 1: Why the Future of Cyber Defense Is Automated, https://medium.com/@corytat/build-your-own-ai-soc-part-1-why-the-future-of-cyber-defense-is-automated-054340393077
- Build Your Own AI SOC — Part 2, https://medium.com/@corytat/build-your-own-ai-soc-part-2-7edf9a84282f
- Build Your Own AI SOC — Part 3 Phishing Detection With Gmail, VirusTotal, and GPT, https://medium.com/devsecops-ai/build-your-own-ai-soc-part-3-phishing-detection-with-gmail-virustotal-and-gpt-7ed4d4a8b3b2
- Build Your Own AI SOC — Final Post: What You’ve Built and Where to Go Next, https://medium.com/@corytat/build-your-own-ai-soc-final-post-what-youve-built-and-where-to-go-next-5526183318ac


