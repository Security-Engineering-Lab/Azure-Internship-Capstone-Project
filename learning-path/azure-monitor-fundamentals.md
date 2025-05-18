
![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/0_monitoring-panel-options-small.png)
![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/1_overview-simple.png)
![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/2_workbooks.png)
![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/3_dashboard.png)
![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/4_web-app-metrics.png)
![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/5_insights-box.svg)
![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/6_visualize-box.svg)
![](https://github.com/Security-Engineering-Lab/Azure-Internship-Capstone-Project/blob/main/learning-path/images/azure-monitor-fundamentals/7_respond-box.svg)



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

![Diagram that shows an overview of Azure Monitor with data sources and features that use the collected data.](https://learn.microsoft.com/en-us/training/wwl-azure/introduction-to-azure-monitor/media/azure-monitor-overview.png)

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

![Screenshots of three workbooks displaying logged data in various chart and table formats.](https://learn.microsoft.com/en-us/training/wwl-azure/introduction-to-azure-monitor/media/azure-monitor-workbooks.png)

You can add the visualizations you create in Azure Monitor to Azure dashboards, which let you combine different kinds of data into a single pane in the Azure portal.

![Screenshot of an Azure dashboard that displays metrics in graph format for application performance metrics at left and security incidents at right.](https://learn.microsoft.com/en-us/training/wwl-azure/introduction-to-azure-monitor/media/azure-monitor-dashboard.png)


# 1.3 Metrics and Logs

In this unit, you learn about metrics and logs. You learn how collecting these two types of data with Azure Monitor lets you monitor the health, behavior, and performance of your Azure applications, networks, and infrastructure.

## Metrics

Metrics are quantitative measurements that show snapshots of application or resource performance. Metrics are typically numeric values that you can measure over time.

Metrics can provide you with an understanding of various aspects of an application or resource, such as resource utilization, response times, error rates, and throughput. Common examples of metrics include CPU usage, memory usage, network latency, and transaction rates.

A list of resource-specific metrics is automatically available for each resource type in your Azure subscription. You can use the Azure Monitor Metrics Explorer to interactively analyze the data in your metrics database and chart the values of multiple metrics over time.

To see the metrics for any resource in the Azure portal, select **Metrics** under **Monitoring** in the left navigation on that resource's page. Then select the metric you need from the Metric dropdown. You can pin the charts to a dashboard to view them with other visualizations.

For example, the following Requests metric line chart shows the sum aggregation of requests for the Contoso-web-sales application.

![Screenshot of the Monitoring option selected in the Azure portal for a web app, showing chart of requests for the web app.](https://learn.microsoft.com/en-us/training/wwl-azure/introduction-to-azure-monitor/media/azure-monitor-metrics.png)

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

![Diagram that shows the Insights part of Azure Monitor.](https://learn.microsoft.com/en-us/training/wwl-azure/monitor-app-performance/media/azure-monitor-insights.png)

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

![Diagram that shows the Visualize part of Azure Monitor.](https://learn.microsoft.com/en-us/training/wwl-azure/monitor-app-performance/media/azure-monitor-visualize.png)

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

![Diagram that shows the Respond part of the Consumption section of the Azure Monitor system.](https://learn.microsoft.com/en-us/training/wwl-azure/monitor-app-performance/media/azure-monitor-respond.png)

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





