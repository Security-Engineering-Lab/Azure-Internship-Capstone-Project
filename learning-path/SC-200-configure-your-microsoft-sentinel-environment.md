

# SC-200: Configure your Microsoft Sentinel environment

https://learn.microsoft.com/en-us/training/paths/sc-200-configure-azure-sentinel-environment/


Get started with Microsoft Sentinel by properly configuring the Microsoft Sentinel workspace. This learning path aligns with exam SC-200: Microsoft Security Operations Analyst.

#### Prerequisites
Fundamental understanding of Microsoft security, compliance, and identity products
Ability to use KQL in Microsoft Sentinel like you could learn from learning path SC-200: Create queries for Microsoft Sentinel using Kusto Query Language (KQL)


Introduction to Microsoft Sentinel
10 min remaining
Module
3 of 6 units completed
Traditional security information and event management (SIEM) systems typically take a long time to set up and configure. They're also not necessarily designed with cloud workloads in mind. Microsoft Sentinel enables you to start getting valuable security insights from your cloud and on-premises data quickly. This module helps you get started.


# 1 Introduction

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



# 2 What is Microsoft Sentinel?


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


## 3 How Microsoft Sentinel Works

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

