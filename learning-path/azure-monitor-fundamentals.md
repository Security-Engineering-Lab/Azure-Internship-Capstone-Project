




![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/48_7-sentinel-10.png)
![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/49_7-sentinel-11.png)
![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/50_7-sentinel-12.png)



# Azure Monitor fundamentals

https://learn.microsoft.com/en-us/training/paths/monitor-usage-performance-availability-resources-azure-monitor/


Learn how to monitor the usage, performance, and availability of resources using Azure Monitor.

### Prerequisites
- Basic knowledge of Azure services
- Basic knowledge of monitoring concepts, such as using metrics, logging, and alerting


# 1 Introduction to Azure Monitor

Learn how to use Azure Monitor to provide insights into your Azure resource performance and operations.


## 1.1 Introduction

Azure Monitor enables end-to-end monitoring of all your Azure and hybrid services and resources. This learning module gives you an overview of Azure Monitor, describes key Azure Monitor features, and helps you understand how Azure Monitor provides you with data and insights about your IT availability, performance, and health.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/0_monitoring-panel-options-small.png)

One reason for hosting workloads on Azure is the ability to scale up or scale out resources when needed, then automatically scale them back when resource needs drop off. But initially, you don't always know exactly where the capacity issues are. You can use Azure Monitor to collect metrics and logs to determine where your needs are so you can base your scaling strategy on concrete data.

Scalability isn't the only reason to host workloads on Azure, and deploying resources isn't the end of your involvement. To prove your return on investment, you need to know whether you're gaining benefits from Azure hosting. Azure Monitor can help you understand and provide the reliability, security, and performance you expect for your users and stakeholders.

#### Learning objectives

* Understand the uses and importance of monitoring.
* Learn the basics of how Azure Monitor works.
* Describe the key reasons for collecting and analyzing metrics and logs.
* Consider how Azure Monitor can support your Azure resource monitoring needs.

#### Prerequisites

Basic knowledge and understanding of the following concepts:
* Azure portal navigation and resource management
* Application and resource scaling and performance


## 1.2 Monitoring and Azure Monitor

This unit gives you an overview of monitoring and Azure Monitor. You learn about Azure Monitor capabilities that are important for the successful operation of your Azure and hybrid resources and applications.

## Introduction to monitoring

Your IT environment might contain many resources, services, networks, and other infrastructure. Monitoring tracks the state, health, behavior, and performance of your applications and IT environment. One goal of monitoring is to ensure that your applications and environment are operating optimally, securely, and reliably. Another goal is to detect and help address any issues.

Monitoring includes the following key activities:

* **Data collection**: Metrics, logs, and log traces to provide insights into the functioning and performance of monitored components.
* **Data analysis**: Understand current state, predict potential issues, identify patterns, trends, and anomalies.
* **Alerts**: Trigger when specific conditions are met, such as high CPU usage or low disk space. Helps notify administrators or trigger automated responses.
* **Visualizations**: Present collected data in user-friendly visual formats to help administrators quickly assess system and resource status.
* **Diagnostics and troubleshooting**: Help identify the root causes of problems and make informed decisions to address them.

Monitoring provides the following important benefits:

* **Performance and cost optimization**: Identifies performance bottlenecks and areas for improving resource utilization, efficiency, and costs.
* **Proactive management**: Lets you take proactive rather than reactive measures to prevent downtime, disruptions, and other problems.
* **Reliability**: Provides quick identification, troubleshooting, and recovery when problems occur.
* **Capacity planning**: Helps you analyze historical usage patterns to aid in forecasting, planning, and infrastructure scaling.
* **Security monitoring**: Detects and responds to security threats, breaches, and suspicious activities to help maintain your system's security posture.
* **Compliance and governance monitoring**: Can monitor adherence to standards, regulations, and policies.

## Overview of Azure Monitor

When you run applications built on various services and resources, a key element of monitoring is the ability to relate your applications' performance and health to the components they're built on. This observability lets you analyze and troubleshoot application issues effectively.

Azure Monitor provides features and tools for collecting, managing, and analyzing IT data from all of your Azure, other cloud, and on-premises resources. The following diagram shows a high-level architectural view of Azure Monitor.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/1_overview-simple.png)

### Data collection and storage

As soon as you add resources to an Azure subscription, Azure Monitor starts collecting data about the resources. Azure Monitor provides the following capabilities for collecting, storing, and managing monitoring data:

* Native monitoring of your entire Azure deployment.
* Tools such as data collection agents and APIs for monitoring all layers in your stack. This includes applications and infrastructure, in and outside of Azure.
* Integration with the Azure Event Hubs data streaming service.
* Data transformations during ingestion to let you filter out data you don't need.
* Configurable data retention periods, archiving, and restore options.
* Pricing tier discounts based on data volume.
* A low-cost Basic logs plan for collecting and storing high-volume verbose logs you use for debugging, troubleshooting, and auditing. However, these aren't for analytics and alerts.

### Data analysis and response

Azure Monitor offers a broad set of tools and capabilities to help you analyze and gain insights from your monitoring data. Azure Monitor includes the following features to support data analysis and response:

* An easy-to-use portal UI that lets you view, filter, and manipulate monitoring data.
* Kusto Query Language (KQL), a powerful query language that's optimized for ad-hoc queries, data exploration, and near-real time analysis of large volumes of data streamed from multiple sources.
* A range of tools for customizing your analysis, visualizations, alerting, and responses.
* Out-of-the-box recommended alerts.
* Ready-to-use monitoring experiences with advanced, built-in analysis and visualizations of your deployment.
* Autoscale to automatically add and remove resources according to the load on your application.
* Native machine learning and artificial intelligence capabilities that help you detect and respond to anomalies.

### Alerts, workbooks, and visualizations

Interactive monitoring is one way to monitor your application. Another option is to configure alerts to send text messages or email to a person or team for further investigation. You can also trigger response actions in certain situations.

Azure Monitor workbooks provide a flexible canvas for analyzing data and creating rich visual reports in the Azure portal. Workbooks can tap into multiple Azure data sources and combine them into unified interactive experiences. You can use the ready-made workbooks that Azure Monitor provides, or create your own workbooks from predefined templates.

The following image shows three types of workbooks that display logged data in different chart and table formats.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/2_workbooks.png)

You can add the visualizations you create in Azure Monitor to Azure dashboards, which let you combine different kinds of data into a single pane in the Azure portal.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/3_dashboard.png)

# 1.3 Metrics and Logs

In this unit, you learn about metrics and logs. You learn how collecting these two types of data with Azure Monitor lets you monitor the health, behavior, and performance of your Azure applications, networks, and infrastructure.

## Metrics

Metrics are quantitative measurements that show snapshots of application or resource performance. Metrics are typically numeric values that you can measure over time.

Metrics can provide you with an understanding of various aspects of an application or resource, such as resource utilization, response times, error rates, and throughput. Common examples of metrics include CPU usage, memory usage, network latency, and transaction rates.

A list of resource-specific metrics is automatically available for each resource type in your Azure subscription. You can use the Azure Monitor Metrics Explorer to interactively analyze the data in your metrics database and chart the values of multiple metrics over time.

To see the metrics for any resource in the Azure portal, select **Metrics** under **Monitoring** in the left navigation on that resource's page. Then select the metric you need from the Metric dropdown. You can pin the charts to a dashboard to view them with other visualizations.

For example, the following Requests metric line chart shows the sum aggregation of requests for the Contoso-web-sales application.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/4_web-app-metrics.png)

Azure Monitor can collect several types of metrics, including:

- **Azure platform metrics**: Azure Monitor starts collecting metrics data from Azure resources as soon as they're added to a subscription. A list of resource-specific metrics is automatically available for each Azure resource type.
- **Custom metrics**: Azure Monitor can also collect metrics from other sources, including applications and agents running on VMs. You can send custom metrics to Azure Monitor via the Azure Monitor Agent, other agents and extensions, or directly to the Azure Monitor REST API.
- **Prometheus metrics**: Azure Monitor managed service for Prometheus collects metrics from Azure Kubernetes Service (AKS) or other Kubernetes clusters. Prometheus metrics share some characteristics with platform and custom metrics, but have different features to support open-source analysis and alerting tools like PromQL and Grafana.

Metrics are well-suited for real-time monitoring. You can use metrics to trigger alerts when defined thresholds are reached.

## Logs

Logs are textual records of events, actions, and messages that occur in a resource or application. While metrics are numeric, logs can include the following data:

- **Text**: Human-readable text entries that provide context, details, and descriptions of events.
- **Unstructured data**: Log entries in various formats that don't fit neatly into predefined numerical values.
- **Contextual information**: Insights into the context surrounding an event, which is invaluable for root cause analysis.

Logs can capture information about errors, warnings, user actions, and application state changes. Logs provide detailed narratives of events in a given context. This makes them crucial for troubleshooting, debugging, and understanding event sequences that lead to issues. Logs are essential for retrospective analysis of issues, helping to reconstruct the chain of events that led up to a problem.

Azure Monitor Logs is a feature of Azure Monitor that lets you store, manage, and analyze log and performance data from monitored resources. To collect and analyze all your data, you set up a common workspace called a Log Analytics workspace. You configure your resources to send their data to that workspace.

Once you configure the workspace and start logging data, you can use Azure Monitor Logs to explore and analyze the data. You can work with log queries and their results interactively in the Log Analytics user interface.

You can use log queries in the following scenarios:

- Use a basic query to answer a common question.
- Do complex data analysis to identify critical patterns in your monitoring data.
- Use queries in alert rules to be proactively notified of issues.
- Visualize query results in a workbook or dashboard.


## 1.4 Azure Monitor Insights, visualizations, and actions

This unit describes how Azure Monitor Insights, visualizations, and dashboards can consume and transmit monitoring information about your web application. You can also use alerts and automated actions to proactively respond to and sometimes correct application issues.

### Insights

Some Azure resource providers have created visualizations that provide a customized monitoring experience and require minimal configuration. Insights are large, scalable, curated visualizations.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/5_insights-box.svg)

Azure Monitor includes many types of Insights. In the Azure portal, select **Insights Hub** in the Azure Monitor navigation to list and access all the available types of Insights.

The following sections describe some of the largest, most common Azure Monitor Insights.

### Application Insights

The Application Insights feature of Azure Monitor provides application performance monitoring (APM) from app development, through test, and into production. You can proactively monitor to see how well an application is performing, and reactively review application execution data to find the cause of an incident.

Along with collecting metrics and telemetry data that describe application activities and health, you can use Application Insights to collect and store application trace logging data. The log trace is associated with other telemetry to give a detailed view of activity. To add trace logging to existing applications, you only need to provide a destination for the logs. You seldom need to change the logging framework.

Application Insights supports distributed tracing, which is also known as distributed component correlation. This feature allows searching for and visualizing the end-to-end flow of a specific execution or transaction. The ability to trace activity from end to end is important for applications built as distributed components or microservices.

Application Insights also includes the following features:

- **Live metrics**: Observe activity from your deployed application in real time with no effect on the host environment.
- **Availability monitoring**: Also known as synthetic transaction monitoring, probes the external endpoints of your applications to test overall availability and responsiveness over time.
- **Usage monitoring**: Helps you understand which features are popular with users and how users interact and use your application.
- **Smart detection**: Detects failures and anomalies automatically through proactive telemetry analysis.
- **Application Map**: A high-level, top-down view of your application architecture with at-a-glance visual references to component health and responsiveness.

#### Container Insights

Container Insights gives you performance visibility into containerized workloads deployed to Azure Kubernetes Service (AKS) or Azure Container Instances. Container Insights collects container logs and metrics from controllers, nodes, and containers that are available through the Metrics API. After you enable monitoring from AKS clusters, these metrics and logs are automatically collected for you through a containerized version of the Log Analytics agent.

### VM Insights

VM Insights monitors and analyzes the performance and health of your Azure Windows and Linux VMs, including VMs hosted on-premises or in another cloud. VM Insights identifies VM processes, application dependencies, and interconnected dependencies on external processes.

### Network Insights

Network Insights provides a comprehensive visual representation of health and metrics for all deployed network resources through topologies, without requiring any configuration. Network Insights also provides access to network monitoring capabilities like Connection Monitor, flow logging for network security groups (NSGs), Traffic Analytics, and other diagnostic features.

### Visualizations

Visualizations such as charts and tables are effective tools for summarizing monitoring data and presenting it to audiences. Azure Monitor has its own features for visualizing monitoring data, and uses other Azure services for publishing data to different audiences. Power BI and Grafana aren't officially part of Azure Monitor, but are core integrations to tell the monitoring story.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/6_visualize-box.svg)

The following sections describe some Azure Monitor and external tools for visualizing and presenting monitoring data.

### Workbooks

Workbooks provide a flexible canvas for analyzing data and creating rich visual reports in the Azure portal. Workbooks can query data from multiple data sources and combine and correlate data from multiple data sets in one visualization, giving you easy visual representation of your system. Workbooks are interactive, with data updating in real time, and can be shared across teams.

You can use the workbooks that Azure Monitor Insights provide, use the workbook template library, or create your own workbooks. In the Azure portal, select **Workbooks** in the Azure Monitor left navigation to see and access the available workbooks and templates.

### Dashboards

Dashboards let you combine different kinds of data into a single pane in the Azure portal. You can add the output of any log query or metrics chart to an Azure dashboard, and optionally share the dashboard with other Azure users. For example, you could create a dashboard that shows a graph of metrics, a table of activity logs, and a usage chart from Application Insights.

### Power BI

Power BI is a business analytics service that provides interactive visualizations across various data sources. You can configure Power BI to automatically import log data from Azure Monitor to take advantage of these visualizations. Power BI is an effective way to make data available to other people within and outside your organization.

### Grafana

Grafana is an open platform for operational dashboards. Grafana includes the Azure Monitor data source plugin to visualize Azure Monitor metrics and logs. Azure Managed Grafana optimizes this experience for Azure-native data stores such as Azure Monitor and Azure Data Explorer.

Grafana also has popular plugins and dashboard templates for non-Microsoft application performance monitoring tools such as Dynatrace, New Relic, and AppDynamics. Grafana includes AWS CloudWatch and GCP BigQuery plugins for multicloud monitoring in a single pane of glass. You can use these resources to visualize Azure Monitor data alongside other metrics that these other tools collect.

## Actions

An effective monitoring solution proactively responds to critical events without the need for an individual or team to notice the issue. The response could be a text or email to an administrator, or an automated process that attempts to correct an error condition.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/7_respond-box.svg)

Azure Monitor works with the following types of automated alerting and responses.

### Artificial Intelligence for IT Operations (AIOps)

AIOps describes the application of artificial intelligence and machine learning techniques to enhance and automate aspects of IT operations and infrastructure management. Azure Monitor provides features that use machine learning and artificial intelligence to automate data-driven tasks, predict capacity usage, identify performance issues, and detect anomalies.

These features simplify IT monitoring and operations without requiring machine learning expertise. If you have machine learning expertise, you can apply more machine learning to the data Azure Monitor collects by using Azure Machine Learning services.

### Azure Monitor alerts

Alerts notify you of critical conditions and can take corrective action. Alert rules can be based on metric or log data. Metric alert rules provide near-real time alerts based on collected metrics. Log alert rules based on log data allow for complex logic across data from multiple sources.

Alert rules use action groups, which can take actions such as sending email or SMS notifications. Action groups can send notifications using webhooks to trigger external processes or to integrate with IT service management tools. You can share action groups, actions, and sets of recipients across multiple rules.

### Autoscale

Autoscale lets you dynamically adjust the number of resources running to handle the load on your applications. To save money or increase performance, you can create rules that use Azure Monitor metrics to determine when to automatically add or remove resources. You can specify a minimum and maximum number of instances and the logic for when to increase or decrease resources.


# 1.5 Module assessment

## 1.
**What action do you need to take for Azure Monitor to start recording metrics on your resources?**

- **None. Azure Monitor begins recording as soon as you create resources.**
- You must configure at least one rule.
- You must associate the resources with a Log Analytics workspace.

## 2.
**What are Azure Monitor Insights?**

- Quantitative measurements of application or resource performance.
- **Curated visualizations that provide a customized monitoring experience.**
- Textual records of events that occur in a resource or application.

## 3.
**What's a good way to combine metrics and other types of data into a single view?**

(Question appears to be incomplete, but based on the material covered, the answer would likely be "Azure Dashboards" or "Azure Monitor Workbooks", as these both allow combining different types of data into unified views)


# 1.6 Summary

This module presented an overview of monitoring, Azure Monitor, and Azure Monitor capabilities that are important to the success of your Azure deployments. You learned about Azure Monitor Metrics and Azure Monitor Logs, two key ways to monitor the health, behavior, and performance of Azure applications and infrastructure.

You also saw how you can consume and transmit monitoring information with Azure Monitor Insights, visualizations, and dashboards. You learned about alerts and automated actions that can proactively respond to and sometimes correct application issues.

Azure Monitor is a comprehensive solution for collecting, analyzing, and acting on telemetry from your cloud and on-premises environments. Azure Monitor helps you evaluate performance and proactively identify issues to maximize the availability and performance of your Azure resources.

## Learn more

Learn more about the Azure Monitor concepts and processes this overview introduced.

**Azure Monitor:**
* [Azure Monitor documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/)
* [Azure Monitor overview](https://learn.microsoft.com/en-us/azure/azure-monitor/overview)
* [Monitor Azure resources with Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/monitor-azure-resource)

**Data collection:**
* [Azure Monitor data sources and data collection methods](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-collection)
* [Data collection rules (DCRs) in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-collection-rule-overview)
* [Azure Monitor Agent overview](https://learn.microsoft.com/en-us/azure/azure-monitor/agents/agents-overview)
* [Monitor Kubernetes clusters using Azure services and cloud native tools](https://learn.microsoft.com/en-us/azure/architecture/operator-guides/aks/monitor-kubernetes)

**Azure Monitor Metrics:**
* [Azure Monitor Metrics overview](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-platform-metrics)
* [Custom metrics in Azure Monitor (preview)](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/metrics-custom-overview)
* [Azure Monitor and Prometheus](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview)
* [Live Metrics: Monitor and diagnose with 1-second latency](https://learn.microsoft.com/en-us/azure/azure-monitor/app/live-stream)
* [Analyze metrics with Azure Monitor metrics explorer](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/metrics-getting-started)

**Azure Monitor Logs:**
* [Azure Monitor Logs overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-platform-logs)
* [Send Azure resource logs to Log Analytics workspaces, Event Hubs, or Azure Storage](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/resource-logs)

**Insights and visualizations:**
* [Azure Monitor Insights overview](https://learn.microsoft.com/en-us/azure/azure-monitor/insights/insights-overview)
* [Application Insights overview](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)
* [Azure Monitor features for Kubernetes monitoring](https://learn.microsoft.com/en-us/azure/azure-monitor/containers/container-insights-overview)
* [VM Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/vm/vminsights-overview)
* [Network Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/insights/network-insights-overview)
* [Azure Workbooks](https://learn.microsoft.com/en-us/azure/azure-monitor/visualize/workbooks-overview)

**Automated actions:**
* [What are Azure Monitor alerts?](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview)
* [Overview of autoscale in Azure](https://learn.microsoft.com/en-us/azure/azure-monitor/autoscale/autoscale-overview)
* [Detect and mitigate potential issues using AIOps and machine learning in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/smart-analytics)



## 2 Design a full-stack monitoring strategy on Azure

Use monitoring services on Azure to help bring operational excellence and security to your applications and infrastructure.

# 2.1 Introduction

Suppose you work for a financial organization that's moving its systems to Azure, with a mixture of infrastructure-as-a-service (IaaS) and platform-as-a-service (PaaS) services. The organization's previous on-premises environment experienced instances of degraded application performance or unavailable systems, with extended delays before the issues were identified and resolved. Customers' inability to access their accounts decreased their satisfaction.

To quickly identify and minimize poor performance and system failures in the future, the organization wants to implement a full-stack monitoring strategy across all its technology solutions. This strategy should offer insights and alerting into collected data.

In this learning module, you explore the monitoring solutions available in Azure. You learn how to use Azure Monitor and its features, such as Application Insights and Azure Monitor Logs, to analyze infrastructure and application performance and availability. You also explore how to use Microsoft Defender for Cloud and Microsoft Sentinel for security monitoring.

After you complete this module, you can use Azure tools to design and implement a full-stack monitoring strategy for your infrastructure and applications.

## Learning objectives

* Select the appropriate monitoring solutions based on use cases.
* Choose a combination of monitoring solutions to create a unified full-stack monitoring strategy.

## Prerequisites

* Basic knowledge of Azure application, virtualization, and container services
* Basic knowledge of operational concepts like monitoring, logging, and alerting


# 2.2 Full-stack monitoring in Azure

Your organization is moving all its systems from an on-premises location to Azure, and wants you to design a monitoring strategy. This unit explains how a full-stack monitoring strategy can improve customer experience by providing the ability to identify and mitigate issues across all the layers of your applications and infrastructure.

## Use full-stack monitoring

Full-stack monitoring is a complete approach to monitoring, triaging, and diagnosing application, infrastructure, and security issues. Full-stack monitoring includes telemetry collection, tracking key performance indicators, isolating problems, and analyzing root causes.

Your applications and infrastructure might face different kinds of potentially damaging issues, such as poor response times, changing usage rates, exceptions, and security risks. Your response must be appropriate to the issue type. You might respond by scaling up capacity to meet increased load, or by changing your application or infrastructure to improve performance and reduce errors.

With the right tools, you can:

- Monitor your infrastructure and application performance.
- Monitor for security risks and suspicious activity.
- Collect information on issues as soon as they arise.
- Analyze and respond to the information you collect.

By monitoring your applications and infrastructure with a full-stack approach, you respond to changes and issues quickly and appropriately. This strategy can help your organization become more productive, cost-effective, secure, and competitive.

## Monitor your applications

Monitor your application for issues while you develop it to prevent errors and exceptions later in production. To improve your development lifecycle, ensure that your code gets pushed to the next stage of the development cycle only if it successfully passes the necessary checks.

Also monitor your application when it's live and in use. You might be faced with failing requests, high server response times, or availability issues. By monitoring for live issues, you identify these types of problems and risks promptly, and can respond effectively to keep your application healthy.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/8_2-full-stack-monitoring-01.png)

To improve your applications' health and build better applications in future, configure alerts and automated responses to help you deal with application issues.

## Monitor your infrastructure

Different kinds of issues can affect your infrastructure. You might have to deal with performance issues or problems that could render your services unreachable or the entire infrastructure unavailable. Any of these issues can result in decreased productivity, financial loss, or damage to your organization's reputation.

To deal with any issues that arise in a timely and effective way, you can configure alerts to monitor your infrastructure for various issues. For example, you can configure alerts for:

- Your infrastructure's resource utilization.
- Your infrastructure's availability and health.
- A specific event occurring at the operating-system level.

You can configure alerts to start a process that notifies a person or team to take appropriate action. You can also trigger automated responses to alerts with playbooks and webhooks.

You can also use infrastructure monitoring data for operational analysis and capacity planning. You can collect performance data from virtual machine (VM) guest operating systems into charts for comparison and trending purposes to inform decision making.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/9_2-full-stack-monitoring-02.png)


## Monitor Azure platform resources

In addition to monitoring your deployed applications and infrastructure, you can use Azure's built-in capabilities to monitor your other Azure platform resources. Azure resources such as Storage Accounts, Key Vaults, and Azure Cosmos DB databases have performance metrics and resource logs that you can view and analyze to track performance and availability.

These and other Azure resource types offer dedicated insights that provide predefined monitoring experiences across subscriptions, resource groups, and other resources. The following screenshot shows the Azure Monitor storage insight displaying usage and latency for multiple storage accounts across two subscriptions.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/9_2-full-stack-monitoring-03.png)

You can also view and collect logs related to Active Directory for your Azure tenant, and Service Health and activity logs for Azure subscriptions. A full-stack monitoring solution includes visibility into the Azure platform resources your application and infrastructure depend on.

## Monitor security

It's also essential to monitor the security of your applications and infrastructure to ensure that they always remain protected and available. You should monitor and alert on data exfiltration and on any risks to your infrastructure's security, such as suspicious user accounts or malicious IP addresses. Your security monitoring solution should include strong, automated anomaly detection and event management to combine multiple related events into a single actionable alert.

## Summary

Taking a full-stack approach to monitoring your applications and infrastructure helps you respond appropriately and more effectively to issues. You can strengthen your protection and build improved applications and infrastructure. The full-stack approach also helps you gain situational awareness, and you learn from the issues that affect your environment.

## Check your knowledge

1. At what point should DevOps teams implement application monitoring for optimal application health and performance?

   - During development only
   - In production only
   - **During development and while in production**

2. What's the term for a monitoring strategy that takes a complete approach to monitoring, triaging, and diagnosing application, infrastructure, and security issues?

   - **Full-stack monitoring**
   - Insights
   - Platform monitoring


# 2.3 Monitoring options in Azure

Your organization's reputation depends on its systems' performance, reliability, and security. For example, if your payment system is unable to process user transactions during a high-volume holiday sales period, your customers might lose confidence in your business.

It's critical to monitor your systems closely to identify any performance problems or attacks before they can affect users. This unit describes the Azure solutions that help you monitor your organization's services.

## Azure Monitor

Azure Monitor is a service for collecting, analyzing, and acting on telemetry from your cloud and on-premises environments. You can analyze metrics and logs from monitored resources.

Azure Monitor helps you maximize the availability and performance of your applications and services by detecting and diagnosing application, infrastructure, and platform issues. Azure Monitor also supports operational workflows with alerts and automated actions, and lets you create visualizations such as dashboards and reports.


![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/10_overview-simple-20230707-opt.svg)

Azure Monitor collects telemetry directly from Azure platform resources, and you can also ingest custom data by using APIs. Azure Monitor can also collect application-layer data and infrastructure-performance data from containers and VM guest operating systems.

Azure Monitor stores the collected data in centralized and fully managed data stores: Azure Monitor Metrics for numerical time-series values and Azure Monitor Log Analytics workspaces for resource logs. Azure Monitor automatically collects and stores metrics for most Azure resources, but user configuration is required to send and store resource logs. You can choose how to consume, analyze, and respond to the collected data.

In most cases, you should start with insights, which are guided monitoring and troubleshooting experiences for Azure resources. For example, you can use Azure Monitor container insights for your Kubernetes workloads.

You can also visualize the data yourself with Azure dashboards in the Azure portal, create business views with Power BI, or create interactive reports by using workbooks. Use Azure Monitor for a detailed view of your applications' and infrastructure's health on a single screen.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/10_3-azure-monitoring-options-02.png)


You can further analyze collected data by using Metrics Explorer for charting and visual correlation, and Log Analytics for queries, trending, and pattern recognition. Azure Monitor lets you manage and create alerts, notifications, and actions such as runbooks and autoscale based on metrics and logs. You can also integrate Azure Monitor with other tools by using Azure Event Hubs to export data or APIs for ingestion and export.

## Microsoft Defender for Cloud

Microsoft Defender for Cloud is a service that manages your infrastructure's security from a centralized location. You can use Defender for Cloud to monitor the security of your workloads, whether they're on-premises or in the cloud.

Attacks are becoming more intelligent, and the number of people with the right security skills is low. Defender for Cloud helps you deal with these challenges by providing you with tools that improve your protection against security threats. Use Defender for Cloud to monitor your resources' health and implement recommendations.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/10_3-azure-monitoring-options-03.png)

Defender for Cloud helps streamline your security configuration. Defender for Cloud is natively integrated with other Azure PaaS services like Azure SQL Database. For IaaS services, you can enable automatic provisioning in Defender for Cloud.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/11_3-azure-monitoring-options-04.png)

Defender for Cloud creates an agent on each supported VM when the VM is created. Defender then automatically starts collecting data from the machine. This Defender for Cloud capability reduces the complexity of configuring security.

## Microsoft Sentinel

Microsoft Sentinel is a cloud-native security information and event management (SIEM) system that collects data on devices, users, infrastructure, and applications across your enterprise. You can use Microsoft Sentinel to proactively hunt for threats and anomalies, and respond by using orchestration and automation. Microsoft Sentinel has built-in threat intelligence for detection and investigation that can help reduce false positives.

You can connect your data sources to Microsoft Sentinel. Data sources include Microsoft services such as Microsoft 365 and Defender for Cloud, and can also include external solutions such as AWS CloudTrail or on-premises sources. The Microsoft Sentinel dashboard shows detailed information collected from your sources.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/12_3-azure-monitoring-options-05.png)

Incidents help you group and combine related alerts. You can use incidents to reduce the noise generated because of the scale of the data. Incidents also help you to further investigate anomalous activities or threats that raise alerts.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/13_3-azure-monitoring-options-06.png)

You can use hunting queries to look for threats across your enterprise before alerts are raised. Microsoft security researchers maintain built-in hunting queries that act as bases for you to build your own queries.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/14_3-azure-monitoring-options-08.png)

Notebooks can consist of investigation or hunting steps that you reuse or share with others. Use Microsoft Sentinel Notebooks to develop and run your notebooks. For example, you might use the Guided hunting - Anomalous Office365 Exchange Sessions notebook to hunt for anomalous activities in Microsoft 365 across your enterprise.

## Log Analytics workspaces

Microsoft Sentinel and Microsoft Defender for Cloud use Azure Monitor Logs as their underlying logging data platform, and store their data in Log Analytics workspaces. Log Analytics workspaces are central storage and management locations that collect and aggregate your application, infrastructure, and security logs for analysis, troubleshooting, and auditing.

This centralized approach lets you use a single user interface and query language to correlate and investigate across application performance, infrastructure performance, and security logs within the same data analytics service. It's best to use as few workspaces as possible, and manage user and team access to subsets of log data by using resource or workspace permissions. For more information, see [Design a Log Analytics workspace architecture](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/workspace-design).

## Check your knowledge

1. Which Azure service incorporates threat intelligence for detection and investigation in enterprise environments?

   - Azure Monitor
   - **Microsoft Sentinel**
   - Application Insights

2. What's the shared underlying logging data platform for Microsoft Sentinel and Microsoft Defender for Cloud?

   - Azure Monitor Metrics
   - **Azure Monitor Logs**
   - Azure Event Hubs



# 2.4 Monitor applications by using Application Insights

When issues arise on your financial organization's application, customers can't access their accounts. If the application issues aren't resolved quickly, customer satisfaction is negatively affected. Your organization wants to avoid these issues as it moves to Azure.

This unit describes how to integrate Azure Monitor Application Insights with your applications. You can use Application Insights to check the health of applications and resolve issues faster.

Use Application Insights to:

- Analyze and address issues and problems that affect your application's health and performance.
- Improve your application's development lifecycle.
- Assess your user experience and analyze users' behavior.

## Integrate Application Insights with your applications

To integrate Application Insights with your applications, you can enable Application Insights in the Azure portal or instrument your application with Application Insights. Instrumentation refers to enabling the collection of monitoring data from your app by using an agent or an SDK. The approach to instrumentation varies depending on your application's language and platform.

In many cases, you can implement instrumentation without access to application source code by using codeless attach in the Azure portal or by using an agent. For example, for your .NET and .NET Core applications hosted on Azure App Services, you can enable the collection of monitoring data with Application Insights by using a toggle in the Azure portal.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/15-application-insights-01.png)

Application Insights automatically collects data about your application's performance and health, and displays this data in the Azure portal. You can select **Failures** in the Application Insights left navigation to get a list of all failures collected for your app and drill into each one.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/16-application-insights-02.png)

To continue your investigation into the root cause of the error or exception, you can drill into the problematic transaction for a detailed end-to-end transaction view that includes dependencies and exception details.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/17-application-insights-03.png)

Application Insights also automatically detects app dependencies to support distributed tracing and create application topology views. You can see this topology by selecting **Application map** in the Application Insights left navigation.

You can view more details of each component in the map by selecting it. For example, you can view the slowest requests for an instance and investigate performance further. These detailed analytics help you understand the application better and respond to its requirements.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/18-application-insights-04.png)

## Monitor your applications' performance

You can further investigate slow transactions to identify slow requests and server-side dependencies. Drill down by selecting **Investigate performance** from the application map, or by selecting **Performance** from the Application Insights left navigation.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/19-application-insights-05.png)

On the Performance screen, you can isolate slow transactions by selecting the time range, operation name, and durations of interest. You're also prompted with automatically identified anomalies and commonalities across transactions. From here, you can drill into an individual transaction for an end-to-end view of transaction details with a Gantt chart of dependencies.

If you instrument your web pages with Application Insights, you can also gain visibility into page views and browser operations and dependencies. Collecting this browser data requires adding a script to your web pages. After you add the script, you can access page views and their associated performance metrics by selecting the **Browser** toggle.

## Analyze user behavior

Instrumenting your web pages with Application Insights collects usage information to augment the server-side monitoring capabilities. The same browser-side JavaScript instrumentation provides usage data including number of users, sessions, events, browser version, OS version, and locations. This usage data shows which pages of your app are the most popular, where users drop out, and the conversion and retention rates for specific pages.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/20-application-insights-06.png)

The preceding example shows the most popular browsers and versions. You can use this type of information to inform decisions for allocating functional and performance-testing resources.

## Monitor your application's availability

You can use the Application Insights Availability page to continuously monitor your application health and check application health from different geographic locations.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/21-application-insights-07.png)

After you create an availability test, you can use the Availability page to see how your application is doing across different locations. Each dot on the Scatter Plot graph represents a test that was run. A red dot means that the test failed.

Select a red dot to see a detailed breakdown of the test failure, including information on what might have caused it. You can use the information to respond appropriately.

When you create an availability test, you can specify details like frequency, the URL of your application, and locations from which to test the app. The following example shows the configuration of a test that sends a request to an application every five minutes from five geographic locations.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/22-application-insights-08.png)

## Get notifications and take action

You can configure Application Insights alert rules to monitor your application's performance and availability. You can specify the conditions that should trigger an alert and dictate how to handle the alert. For example, Application Insights can send an alert if a specified number of locations are unavailable, or if a certain number of exceptions occur.

You can also specify who to notify about the alert. Application Insights can send notifications through email or text message, or use runbooks and webhooks to respond to alerts through automation.

## Check your knowledge

1. Which aspects of application performance can Application Insights monitor?

   - Key Vault requests and latency
   - **User behavior and usage patterns**
   - Types of network delay

2. How can you continuously monitor your applications from different geographic locations?

   - **Create availability tests.**
   - Use an instrumentation script.
   - View the Performance screen in Application Insights.
  




# 2.5 Monitor VMs and containers by using insights

Your organization migrated several applications from on-premises to Azure virtual machines (VMs) and Azure Kubernetes Service (AKS). Several hundred Azure resources are now deployed across several Azure subscriptions.

You must track resource usage to ensure that cloud resources are adequately provisioned and their performance meets business requirements. You need a monitoring approach that provides broad visibility and the capability to triage and isolate problems quickly.

This unit explains how to use Azure Monitor insights and other tools for an at-scale monitoring view across all your virtual machine (VM) and container resources. You also learn how to drill into specific nodes and containers for troubleshooting.

## Azure Monitor insights

You can use Azure Monitor insights to monitor resource utilization and performance at scale with guided troubleshooting to triage and isolate issues. This unit focuses on VM insights and container insights, but insights exist for other Azure resources, including networks, storage accounts, and Azure Cosmos DB databases. For a complete list of available insights, select **Insights Hub** in the Azure Monitor left navigation.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/23-analyze-resource-utilization-08.png)


## Azure Monitor VM insights

The Azure Monitor feature VM insights helps you get started monitoring your VM clients by collecting a set of commonly used metrics and sending them to a Log Analytics workspace. You can use Azure Monitor VM insights to:

- View your VMs' health and performance.
- Monitor your VMs at scale across multiple subscriptions and resource groups.
- Get a topology view that shows the processes and network connection details of your VMs and virtual machine scale sets.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/24-analyze-resource-utilization-01.png)

To enable Azure Monitor VM insights, select **Virtual Machines** from the Azure Monitor left navigation, and then select **Configure Insights** on the **Get started** tab. In the **Not monitored** section of the **Overview** tab, select the VMs and virtual machine scale sets to monitor, and then select **Enable**.

Enabling VM insights adds extensions and configuration to your VMs and virtual machine scale sets that collect, store, and display a predetermined set of usage and performance measurements.

## Monitor your VMs at scale

Once enabled, VM insights monitors VM and virtual machine scale set usage and performance. Select the VM insights **Performance** tab to see the Top N Charts and Top N List that show VM resource usage.

These charts allow you to quickly identify outliers and hot spots where the allocated resources might be insufficient to support the existing load. From the Top N List, you can select a VM to access more details, such as its properties, links to other workbooks, collected logs, and alerts.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/25_machine-log-events.png)

You can drill down into Azure Monitor Logs by selecting an event type from the list in **Log Events**. The relevant Log Analytics workspace opens with the appropriate table and filter applied.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/26-analyze-resource-utilization-03.png)

The Azure Monitor VM insights **Map** tab shows network connections for an entire resource group, virtual machine scale set, or individual VM. To select the resources of interest, use the filters at the top of the view.

You can expand the number of processes for a complete list and to view the network connections per process. Select the arrow representing the connection for network usage and performance details.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/27-analyze-resource-utilization-04.png)

## Azure Monitor container insights

Container insights is a feature of Azure Monitor that monitors the performance and health of container workloads deployed to Azure, including AKS. The Container insights feature collects memory and processor metrics from controllers, nodes, and containers, and gathers container logs. You can use Azure Monitor container insights to:

- View your Kubernetes workloads' health and performance at scale across multiple subscriptions and resource groups.
- Get visibility into memory and processor performance metrics from controllers, nodes, and containers.
- View and store container logs for real-time and historical analysis.

You can enable Azure Monitor container insights when you create an AKS cluster, or by selecting **Containers** in the Azure Monitor left navigation and then selecting the **Unmonitored clusters** tab.

## Monitor Kubernetes clusters at scale

After you enable container insights, you can view your Kubernetes workloads' performance and resource utilization on the container insights page by Cluster, Node, Controller, or Container. For example, you can:

- Investigate an overutilized node.
- View the state of pods by controller.
- Look at the number of restarts and CPU or memory utilization of a specific container.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/28_container.png)

The **Monitored clusters** tab shows an at-scale view of the health and status of all your clusters, nodes, system pods, and user pods. You can filter this view by namespace and use it as a starting point to drill into problem areas. You can also use container insights to access logs and enable recommended alerts.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/29-analyze-resource-utilization-05.png)


## Azure Monitor managed service for Prometheus

Prometheus is an open-source monitoring system designed specifically for containers and microservices. Prometheus focuses on distributed applications, making it a popular tool for monitoring Kubernetes, distributed services, and containerized microservices.

Azure Monitor managed service for Prometheus is a component of Azure Monitor Metrics that supports open-source querying and visualization tools like PromQL and Grafana. Azure Monitor managed service for Prometheus can collect data from AKS or from any Kubernetes cluster that runs self-managed Prometheus using remote-write. To enable Azure Monitor managed service for Prometheus, you create an Azure Monitor workspace to store the Prometheus metrics.

## Integrate with Azure Managed Grafana

Grafana is an open-source visualization and dashboarding platform that's the primary method for visualizing Prometheus metrics. You can connect your Azure Monitor workspace to a Grafana workspace to use your Prometheus metrics data as a data source in a Grafana dashboard.

Azure Managed Grafana is a fully managed implementation of Grafana that offers multiple predefined Grafana dashboards for monitoring Kubernetes and doing full-stack troubleshooting. You can import prebuilt Grafana dashboards that use Prometheus metrics, or you can create custom dashboards. The following screenshot shows an Azure Managed Grafana dashboard that uses AKS monitoring data.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/30_managed-grafana.png)


## Azure Monitor alerts

Some types of Azure Monitor insights include recommended alert templates, but you can also specify conditions to trigger an alert in your particular environment. You can configure alert rules to monitor your infrastructure's performance and availability, and use alert rules and action rules to dictate how to handle alerts.

You can base Azure Monitor alerts on the same metrics or log data used to populate insights. For example, Azure Monitor can send an alert if a VM exceeds a utilization threshold, or if a specified number of container restarts occur.

You can also specify who should be notified. Insights can send notifications through email or text message, or use runbooks and webhooks to automatically respond to alerts.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/31-analyze-resource-utilization-07.png)

## Check your knowledge

1. Where can you see a topology view with network connection details of your VMs and virtual machine scale sets?

   - Log Analytics
   - Metrics Explorer
   - **VM insights Map tab**

2. What open-source monitoring system is designed specifically for containers and microservices?

   - **Prometheus**
   - VM insights
   - Grafana
  
# 2.6 Manage infrastructure security by using Defender for Cloud


Because your company is a financial organization, it needs to meet the highest standards for security. Each customer or partner transaction must be protected completely from threats, and you must also respond effectively to potential threats. For example, if a virtual machine (VM) is compromised, you must act rapidly to address the issue.

This unit describes how to protect resources and respond to threats by using Microsoft Defender for Cloud. Defender for Cloud helps you ensure that the security configuration of your infrastructure is as secure as possible.

You can use Defender for Cloud to:

- Understand your architecture's security posture.
- Identify and address risks and threats to your infrastructure.
- Secure a complex infrastructure by using traditional in-house skills and capital.
- Secure an infrastructure that consists of on-premises and cloud resources.

## Understand your security posture

You must understand your architecture's security posture to help you build and maintain better infrastructures. Defender for Cloud helps you understand the security of your architecture by giving you detailed analyses of different components of your environment, including:

- Data security
- Network security
- Identity and access
- Application security

Defender for Cloud uses Azure Monitor Logs to collect data from your VMs to monitor for security vulnerabilities and threats. An agent reads various security-related configurations and event logs from the VM and copies the data to your Log Analytics workspace for analysis.

Defender for Cloud recommends ways to address the issues and risks that it uncovers. You can use recommendations to improve the security and compliance of your architecture.


![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/32-security-center-update-02.png)

## Protect against threats

You can use Defender for Cloud just-in-time (JIT) VM access and adaptive application controls to help block suspicious activity and protect your resources. To access these controls, select **Workload protections** in the Cloud Security section of the Defender for Cloud left navigation.

### JIT VM access

You can protect your VMs by using the just-in-time (JIT) VM access feature to block persistent VM access. Your VMs can be accessed based only on audited access that you configure.

To enable JIT, select **Just-in-time VM access** on the Workload protections screen under Advanced protection. On the Just-in-time VM access page, select the checkboxes next to one or more VMs on the Not Configured list, and then select **Enable JIT on (number) VM(s)** to configure JIT for the VMs.

Defender for Cloud shows you a list of default ports that JIT targets, or you can configure your own ports.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/33-security-center-update-03.png)

### Adaptive application controls

You can use adaptive application controls to control which applications are allowed to run on your VMs. Defender for Cloud uses machine learning to look at the processes running on your VMs, create exception rules for each resource group that holds your VMs, and give recommendations.

To configure adaptive controls, select **Adaptive application control** on the Workload protections screen under Advanced protection. The Adaptive application controls screen shows a list of resource groups that contain your VMs. The **Recommended** tab lists the resource groups that Defender for Cloud recommends for adaptive application controls.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/34-security-center-update-04.png)


When you select a resource group, it opens **Configure application control rules**. On this screen, use the options to target VMs and applications that should have the control rules applied.

## Respond to threats

Defender for Cloud gives you a centralized view of all your security alerts, ranked by their severity. You can view your security alerts by selecting **Security alerts** in the Defender for Cloud left navigation.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/35-security-center-update-01.png)

Defender for Cloud combines related alerts into a single security incident as much as possible. Select an incident to see the specific security alerts that the incident holds.

Drill down into an alert by selecting the alert and then selecting **View full details**.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/36-security-center-update-06.png)

Defender for Cloud can help you respond to threats faster and in an automated way by taking actions. Select **Next: Take Action** to take action on the alert.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/37-security-center-update-08.png)

Expand any of the following sections to take action on the alert:

- **Inspect resource context** to examine the resource logs around the time of the alert.
- **Mitigate the threat** to see suggestions for minimizing or remediating the threat.
- **Prevent future attacks** to implement security recommendations.
- **Trigger automated response** to trigger a logic app as an automated response to this security alert.
- **Suppress similar alerts** by creating a suppression rule with predefined conditions.
- **Configure email notification settings** to select who to notify about the alert and under what conditions.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/38-security-center-update-10.png)

In the alert details, you should dismiss alerts if no action is required, for example if there are false positives. You should act to address known attacks, for example by blocking known malicious IP addresses, and you should decide which alerts require further investigation.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/39-security-center-update-09.png)

## Check your knowledge

1. How can you use Defender for Cloud to prevent persistent access to your virtual machines?

   - Use Azure Logic Apps.
   - **Use just-in-time (JIT) access.**
   - Use adaptive application controls.

2. How can you automate responses to Defender for Cloud alerts?

   - Use just-in-time (JIT) access.
   - Use adaptive application controls.
   - **Use Azure Logic Apps.**
  
# 2.7 Manage enterprise security by using Microsoft Sentinel

Your financial organization constantly deals with customers and partners across different regions in the world. Many transactions happen every day, and each transaction must be monitored and protected regardless of its type or the devices and users involved. Your organization's security and monitoring strategy must focus on enterprise-wide security and monitoring.

This unit describes how Microsoft Sentinel helps monitor and respond to security threats across an enterprise-level organization. You can use Microsoft Sentinel to:

- Get a detailed overview of your enterprise, potentially across multiple clouds and on-premises locations.
- Avoid reliance on complex and disparate tools.
- Identify and handle threats across your organization by using enterprise-grade AI, built by experts.

## Connect your data sources to Microsoft Sentinel

To implement Microsoft Sentinel, you need a Log Analytics workspace. When you create a Microsoft Sentinel resource in the Azure portal, you can create a new Log Analytics workspace or connect an existing workspace.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/40_7-sentinel-01.png)

After you create the Microsoft Sentinel resource and connect it to a workspace, you need to connect data sources for your enterprise. Install solutions with data connectors from the content hub. Microsoft Sentinel integrates with Microsoft solutions, including Microsoft Entra ID and Microsoft 365, through connectors.

You can see all of your available data connectors by selecting **Data connectors** under Configuration in the Microsoft Sentinel left navigation.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/41_7-sentinel-02.png)

Select the appropriate data connector for your data source, read the information about the connector, and select **Open connector page** to look at the prerequisites for your connector. Make sure you address all the prerequisites to successfully connect your data source.

When you connect the data source, your logs are synced to Microsoft Sentinel. You see a summary of collected data in the Data received graph for your connector. You can also see the different data types that are collected for the source. For example, the Azure Storage Account connector can collect Blob, Queue, File, or Table log data.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/42_7-sentinel-03.png)

Once you connect your data sources, Microsoft Sentinel begins to monitor your enterprise.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/43_7-sentinel-04.png)


## Use alerts to monitor your enterprise

You can configure alert rules to investigate anomalies and threats more intelligently. Alert rules specify the threats and activities that should raise alerts. You can respond manually or by using playbooks for automated responses.

Select **Analytics** in the Microsoft Sentinel left navigation under Configuration to view all the rules you have in place and create new rules.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/44_7-sentinel-05.png)

When you create a rule, you specify whether it should be enabled or disabled, and the severity of the alert. In the **Rule query** field of the **Set rule logic** tab, enter a rule query.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/45_7-sentinel-06.png)

For example, the following query can determine if a suspicious number of Azure VMs are created or updated, or a suspicious number of resource deployments occur.

```kusto
AzureActivity
 | where OperationName == "Create or Update Virtual Machine" or OperationName == "Create Deployment"
 | where ActivityStatus == "Succeeded"
 | make-series dcount(ResourceId)  default=0 on EventSubmissionTimestamp in range(ago(7d), now(), 1d) by Caller
```

In the **Query scheduling** section, you can set how often the query should run and which period of data to look up. In the **Alert threshold** section, you can specify the level at which to raise an alert.

## Investigate incidents

Microsoft Sentinel combines generated alerts into incidents for further investigation. Select **Incidents** in the Microsoft Sentinel left navigation under Threat management to see details about all your incidents, such as how many incidents are closed, how many remain open, when the incidents happened, and their severity.

To start to investigate an incident, select the incident. You get information about the incident in the right pane. Select **View full details** to get more information.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/46_7-sentinel-07.png)

To investigate the incident, update its status from **New** to **Active**, assign it to an owner, and select **Investigate**.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/47_7-sentinel-08.png)

The investigation map helps you understand what caused an incident and the affected scope. You can also use the map to correlate data surrounding an incident.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/47_7-sentinel-08.png)

The investigation map lets you drill down into an incident. Multiple entities, including users, devices, and appliances, can be mapped to an incident. For example, you can get details about a user identified as part of the incident.

![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/48_7-sentinel-10.png)

If you hover over an entity, you see a list of exploration queries designed by Microsoft security analysts and experts. You can use the exploration queries to investigate more effectively.

![Screenshot of exploration queries.](https://learn.microsoft.com/en-us/training/wwl-azure/design-monitoring-strategy-for-azure-solutions/media/microsoft-sentinel-exploration-queries.png)

The investigation map also gives you a timeline that helps you understand which event occurred at a particular time. Use the timeline feature to understand the path that a threat might take over time.

![Screenshot of timeline.](https://learn.microsoft.com/en-us/training/wwl-azure/design-monitoring-strategy-for-azure-solutions/media/microsoft-sentinel-timeline.png)

## Check your knowledge

1. Why do you use Microsoft Sentinel?

   - To improve the development lifecycle for an application.
   - **To detect and respond to security threats across multiple clouds.**
   - To cross-query data collected from multiple on-premises and cloud data sources.

2. How can you use the Microsoft Sentinel investigation map to determine which users an incident affected?

   - Use exploration queries.
   - **Use entities.**
   - Use the timeline.
  


## 2.8 Summary

Your organization asked you to design a monitoring strategy to cover all of its technology solutions. The strategy needed to be able to quickly identify and minimize problems and failures, and to provide insights and alerts for collected log and metrics data.

This learning module showed you how to use Azure Monitor features like Application Insights and Virtual machine (VM) insights to monitor the health and performance of your applications and infrastructure. You also saw how to use Microsoft Defender for Cloud and Microsoft Sentinel to monitor the security of your infrastructure and enterprise.

* Azure Monitor lets you analyze and address environment health and performance issues, and query to analyze data in a single location.
* Defender for Cloud helps you identify and address risks to your security posture.
* Microsoft Sentinel gives you security incident management, investigation, and response capabilities.

These Azure services give you a full-stack approach to monitoring applications and infrastructure. Because you can address issues faster and more effectively, your organization is more secure, productive, cost-effective, and competitive.

## Other resources

To learn more about monitoring solutions on Azure, see the following resources:

* [Azure Monitor overview](https://learn.microsoft.com/en-us/azure/azure-monitor/overview)
* [Application Insights overview](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)
* [Availability standard test](https://learn.microsoft.com/en-us/azure/azure-monitor/app/availability-standard-tests)
* [Monitor virtual machines](https://learn.microsoft.com/en-us/azure/azure-monitor/vm/vminsights-overview)
* [Container insights overview](https://learn.microsoft.com/en-us/azure/azure-monitor/containers/container-insights-overview)
* [Monitor Kubernetes clusters using Azure services and cloud native tools](https://learn.microsoft.com/en-us/azure/architecture/operator-guides/aks/monitor-kubernetes)
* [Azure Monitor managed service for Prometheus](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview)
* [Azure Managed Grafana](https://learn.microsoft.com/en-us/azure/managed-grafana/overview)
* [What is Microsoft Sentinel?](https://learn.microsoft.com/en-us/azure/sentinel/overview)
* [Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)


# 3 Monitor app performance

Learn how to use the tools offered in Application Insights to enhance the performance and stability of your applications.

# 3.1 Introduction

Instrumenting and monitoring your apps helps you maximize their availability and performance.

After completing this module, you'll be able to:

* Describe how Application Insights works and how it collects events and metrics.
* Instrument an app for monitoring, and perform availability tests.
* Use Application Map to help you monitor performance and troubleshoot issues.

## 3.2 Explore Application Insights

Application Insights is an extension of Azure Monitor and provides Application Performance Monitoring (APM) features. APM tools are useful to monitor applications from development, through test, and into production in the following ways:

- Proactively understand how an application is performing.
- Reactively review application execution data to determine the cause of an incident.

In addition to collecting metrics and application telemetry data, which describe application activities and health, Application Insights can also be used to collect and store application trace logging data.

The log trace is associated with other telemetry to give a detailed view of the activity. Adding trace logging to existing apps only requires providing a destination for the logs; the logging framework rarely needs to be changed.

### Application Insights feature overview

Features include, but not limited to:

| Feature | Description |
|---------|-------------|
| Live Metrics | Observe activity from your deployed application in real time with no effect on the host environment. |
| Availability | Also known as Synthetic Transaction Monitoring, probe your applications external endpoints to test the overall availability and responsiveness over time. |
| GitHub or Azure DevOps integration | Create GitHub or Azure DevOps work items in context of Application Insights data. |
| Usage | Understand which features are popular with users and how users interact and use your application |
| Smart Detection | Automatic failure and anomaly detection through proactive telemetry analysis. |
| Application Map | A high level top-down view of the application architecture and at-a-glance visual references to component health and responsiveness. |
| Distributed Tracing | Search and visualize an end-to-end flow of a given execution or transaction. |

### What Application Insights monitors

Application Insights collects Metrics and application Telemetry data, which describe application activities and health, as well as trace logging data.

- **Request rates, response times, and failure rates** - Find out which pages are most popular, at what times of day, and where your users are. See which pages perform best. If your response times and failure rates go high when there are more requests, then perhaps you have a resourcing problem.
- **Dependency rates, response times, and failure rates** - Find out whether external services are slowing you down.
- **Exceptions** - Analyze the aggregated statistics, or pick specific instances and drill into the stack trace and related requests. Both server and browser exceptions are reported.
- **Page views and load performance** - reported by your users' browsers.
- **AJAX calls from web pages** - rates, response times, and failure rates.
- **User and session counts**.
- **Performance counters** from your Windows or Linux server machines, such as CPU, memory, and network usage.
- **Host diagnostics** from Docker or Azure.
- **Diagnostic trace logs** from your app - so that you can correlate trace events with requests.
- **Custom events and metrics** that you write yourself in the client or server code, to track business events such as items sold or games won.

### Getting started with Application Insights

Application Insights is one of the many services hosted within Microsoft Azure, and telemetry is sent there for analysis and presentation. It's free to sign up, and if you choose the basic pricing plan of Application Insights, there's no charge until your application has grown to have substantial usage.

There are several ways to get started monitoring and analyzing app performance:

- **At run time**: instrument your web app on the server. Ideal for applications already deployed. Avoids any update to the code.
- **At development time**: add Application Insights to your code. Allows you to customize telemetry collection and send more telemetry.
- **Instrument your web pages** for page view, AJAX, and other client-side telemetry.
- **Analyze mobile app usage** by integrating with Visual Studio App Center.
- **Availability tests** - ping your website regularly from our servers.


## 3.3 Discover log-based metrics


Application Insights log-based metrics let you analyze the health of your monitored apps, create powerful dashboards, and configure alerts. There are two kinds of metrics:

- **Log-based metrics** behind the scene are translated into Kusto queries from stored events.
- **Standard metrics** are stored as preaggregated time series.

Since standard metrics are preaggregated during collection, they have better performance at query time. Standard metrics are a better choice for dashboarding and in real-time alerting. The log-based metrics have more dimensions, which makes them the superior option for data analysis and ad-hoc diagnostics. Use the namespace selector to switch between log-based and standard metrics in metrics explorer.

### Log-based metrics

Developers can use the SDK to send events manually (by writing code that explicitly invokes the SDK) or they can rely on the automatic collection of events from autoinstrumentation. In either case, the Application Insights backend stores all collected events as logs, and the Application Insights blades in the Azure portal act as an analytical and diagnostic tool for visualizing event-based data from logs.

Using logs to retain a complete set of events can bring great analytical and diagnostic value. For example, you can get an exact count of requests to a particular URL with the number of distinct users who made these calls. Or you can get detailed diagnostic traces, including exceptions and dependency calls for any user session. Having this type of information can significantly improve visibility into the application health and usage, allowing to cut down the time necessary to diagnose issues with an app.

At the same time, collecting a complete set of events may be impractical (or even impossible) for applications that generate a large volume of telemetry. For situations when the volume of events is too high, Application Insights implements several telemetry volume reduction techniques, such as sampling and filtering that reduces the number of collected and stored events. Unfortunately, lowering the number of stored events also lowers the accuracy of the metrics that, behind the scenes, must perform query-time aggregations of the events stored in logs.

### Preaggregated metrics

The preaggregated metrics aren't stored as individual events with lots of properties. Instead, they're stored as preaggregated time series, and only with key dimensions. This makes the new metrics superior at query time: retrieving data happens faster and requires less compute power. This enables new scenarios such as near real-time alerting on dimensions of metrics, more responsive dashboards, and more.

> **Important**
>
> Both, log-based and pre-aggregated metrics coexist in Application Insights. To differentiate the two, in the Application Insights UX the pre-aggregated metrics are now called "Standard metrics (preview)", while the traditional metrics from the events were renamed to "Log-based metrics".

The newer SDKs (Application Insights 2.7 SDK or later for .NET) preaggregate metrics during collection. This applies to standard metrics sent by default so the accuracy isn't affected by sampling or filtering. It also applies to custom metrics sent using GetMetric resulting in less data ingestion and lower cost.

For the SDKs that don't implement preaggregation the Application Insights backend still populates the new metrics by aggregating the events received by the Application Insights event collection endpoint. While you don't benefit from the reduced volume of data transmitted over the wire, you can still use the preaggregated metrics and experience better performance and support of the near real-time dimensional alerting with SDKs that don't preaggregate metrics during collection.

It's worth mentioning that the collection endpoint preaggregates events before ingestion sampling, which means that ingestion sampling will never impact the accuracy of preaggregated metrics, regardless of the SDK version you use with your application.



# 3.4 Instrument an app for monitoring

At a basic level, "instrumenting" is simply enabling an application to capture telemetry. There are two methods to instrument your application:
* Automatic instrumentation (autoinstrumentation)
* Manual instrumentation

**Autoinstrumentation** enables telemetry collection through configuration without touching the application's code. Although it's more convenient, it tends to be less configurable. It's also not available in all languages. See Autoinstrumentation supported environments and languages. When autoinstrumentation is available, it's the easiest way to enable Azure Monitor Application Insights.

**Manual instrumentation** is coding against the Application Insights or OpenTelemetry API. In the context of a user, it typically refers to installing a language-specific SDK in an application. This means that you have to manage the updates to the latest package version by yourself. You can use this option if you need to make custom dependency calls or API calls that are not captured by default with autoinstrumentation. There are two options for manual instrumentation:
* Application Insights SDKs
* Azure Monitor OpenTelemetry Distros.

## Enabling via Application Insights SDKs

You only need to install the Application Insights SDK in the following circumstances:
* You require custom events and metrics
* You require control over the flow of telemetry
* Auto-Instrumentation isn't available (typically due to language or platform limitations)

To use the SDK, you install a small instrumentation package in your app and then instrument the web app, any background components, and JavaScript within the web pages. The app and its components don't have to be hosted in Azure. The instrumentation monitors your app and directs the telemetry data to an Application Insights resource by using a unique token.

A list of SDK versions and names is hosted on GitHub. For more information, visit SDK Version.

## Enable via OpenTelemetry

Microsoft worked with project stakeholders from two previously popular open-source telemetry projects, OpenCensus and OpenTracing. Together, we helped to create a single project, OpenTelemetry. OpenTelemetry includes contributions from all major cloud and Application Performance Management (APM) vendors and lives within the Cloud Native Computing Foundation (CNCF). Microsoft is a Platinum Member of the CNCF.

Some legacy terms in Application Insights are confusing because of the industry convergence on OpenTelemetry. The following table highlights these differences. OpenTelemetry terms are replacing Application Insights terms.

| Application Insights | OpenTelemetry |
|----------------------|---------------|
| Autocollectors | Instrumentation libraries |
| Channel | Exporter |
| Codeless / Agent-based | Autoinstrumentation |
| Traces | Logs |
| Requests | Server Spans |
| Dependencies | Other Span Types (Client, Internal, etc.) |
| Operation ID | Trace ID |
| ID or Operation Parent ID | Span ID |



# 3.5 Select an availability test

After you deploy your web app or website, you can set up recurring tests to monitor availability and responsiveness. Application Insights sends web requests to your application at regular intervals from points around the world. It can alert you if your application isn't responding or responds too slowly. You can create up to 100 availability tests per Application Insights resource.

Availability tests don't require any changes to the website you're testing and work for any HTTP or HTTPS endpoint that's accessible from the public internet. You can also test the availability of a REST API that your service depends on.

You can create up to 100 availability tests per Application Insights resource, and there are three types of availability tests:

* **Standard test:** This is a type of availability test that checks the availability of a website by sending a single request, similar to the deprecated URL ping test. In addition to validating whether an endpoint is responding and measuring the performance, Standard tests also include TLS/SSL certificate validity, proactive lifetime check, HTTP request verb (for example, `GET`,`HEAD`, and `POST`), custom headers, and custom data associated with your HTTP request.

* **Custom TrackAvailability test:** If you decide to create a custom application to run availability tests, you can use the TrackAvailability() method to send the results to Application Insights.

* **URL ping test (classic):** You can create this test through the portal to validate whether an endpoint is responding and measure performance associated with that response. You can also set custom success criteria coupled with more advanced features, like parsing dependent requests and allowing for retries.

> **Important**
> 
> **URL ping tests:** On September 30, 2026, URL ping tests in Application Insights will be retired. Existing URL ping tests will be removed from your resources. Review the **pricing** for standard tests and **transition** to using them before September 30, 2026 to ensure you can continue to run single-step availability tests in your Application Insights resources.

# 3.7 Troubleshoot app performance by using Application Map

Application Map helps you spot performance bottlenecks or failure hotspots across all components of your distributed application. Each node on the map represents an application component or its dependencies; and has health key performance indicator and alerts status. You can select through from any component to more detailed diagnostics, such as Application Insights events. If your app uses Azure services, you can also select through to Azure diagnostics, such as SQL Database Advisor recommendations.

Components are independently deployable parts of your distributed/microservices application. Developers and operations teams have code-level visibility or access to telemetry generated by these application components.

* Components are different from "observed" external dependencies such as SQL, Event Hubs, etc. which your team/organization may not have access to (code or telemetry).
* Components run on any number of server/role/container instances.
* Components can be separate Application Insights instrumentation keys (even if subscriptions are different) or different roles reporting to a single Application Insights instrumentation key. The preview map experience shows the components regardless of their configuration.

You can see the full application topology across multiple levels of related application components. Components could be different Application Insights resources, or different roles in a single resource. The app map finds components by following HTTP dependency calls made between servers with the Application Insights SDK installed.

This experience starts with progressive discovery of the components. When you first load the application map, a set of queries is triggered to discover the components related to this component. A button at the top-left corner updates with the number of components in your application as they're discovered.

Selecting **Update map components** refreshes with all components discovered until that point. Depending on the complexity of your application, this may take a minute to load.

If all of the components are roles within a single Application Insights resource, then this discovery step isn't required. The initial load for such an application has all its components.

One of the key objectives with this experience is to be able to visualize complex topologies with hundreds of components. Click on any component to see related insights and go to the performance and failure triage experience for that component.

Application Map uses the cloud role name property to identify the components on the map. You can manually set or override the cloud role name and change what gets displayed on the Application Map.


## 3.8 Module assessment

## Check your knowledge

### 1.
**Which of the following availability tests is recommended for authentication tests?**
- URL ping
- Standard
- **Custom TrackAvailability**

### 2.
**Which of the following metric collection types provides near real-time querying and alerting on dimensions of metrics, and more responsive dashboards?**
- Log-based
- **Pre-aggregated**
- Azure Service Bus



# 3.9 Summary

In this module, you learned how to:

* Describe how Application Insights works and how it collects events and metrics.
* Instrument an app for monitoring, and perform availability tests.
* Use Application Map to help you monitor performance and troubleshoot issues.
