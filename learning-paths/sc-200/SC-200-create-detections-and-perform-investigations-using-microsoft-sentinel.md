
# SC-200: Create detections and perform investigations using Microsoft Sentinel
https://learn.microsoft.com/en-us/training/paths/sc-200-create-detections-perform-investigations-azure-sentinel/

Detect previously uncovered threats and rapidly remediate threats with built-in orchestration and automation in Microsoft Sentinel. This learning path aligns with Exam SC-200: Security Operation Analyst.

#### Prerequisites

- Understand how to use KQL in Microsoft Sentinel like you could learn from learning path SC-200: Create queries for Microsoft Sentinel using Kusto Query Language (KQL)
- Understand how data is connected to Microsoft Sentinel like you could learn from learning path SC-200: Connect logs to Microsoft Sentinel



# 1 Threat detection with Microsoft Sentinel analytics

In this module, you learned how Microsoft Sentinel Analytics can help the SecOps team identify and stop cyber attacks.

# 1.1 Introduction

Microsoft Sentinel Analytics provides an intelligent solution that you can use to detect potential threats and vulnerabilities in your organizations.

Imagine that you work as Security Operations Center (SOC) analyst in Contoso, Ltd. Contoso is a midsize financial services company in London with a New York branch office. Contoso uses several Microsoft products and services to implement data security and threat protection for its resources. These products are:

* Microsoft 365
* Microsoft Entra ID
* Microsoft Entra ID Protection
* Microsoft Defender for Cloud Apps
* Microsoft Defender for Identity
* Microsoft Defender for Endpoint
* Microsoft Defender for Office 365
* System Center Endpoint Protection
* Microsoft Azure Information Protection

Contoso provides threat protection for its Azure-based and on-premises resources by using the paid version of Microsoft Defender for Cloud. The company also monitors and protects other non-Microsoft assets. Security analysts at Contoso face a huge triage burden. They deal with a high volume of alerts from multiple products. They correlate alerts in the following ways:

* Manually from different project dashboards
* By using a traditional correlation engine

Additionally, the time spent to set up and maintain IT infrastructure takes the SOC team away from its security tasks.

The IT director believes that Microsoft Sentinel Analytics will help the security analysts perform complex investigations faster and improve their Security Operations Center (SOC). As Contoso's lead system engineer and Azure administrator, you've been asked to set up analytics rules in Microsoft Sentinel so that the SecOps team can identify and analyze attacks to Contoso's resources.

In this module, you'll understand the importance of using Microsoft Sentinel Analytics, create, and implement analytics rules from existing templates, create new rules and queries using the wizard, and manage rules with modifications.

By the end of this module, you'll be able to set up analytics rules in Microsoft Sentinel to help the SecOps team identify and stop cyberattacks.

## Learning objectives

* Explain the importance of Microsoft Sentinel Analytics.
* Explain different types of analytics rules.
* Create rules from templates.
* Create new analytics rules and queries using the analytics rule wizard.
* Manage rules with modifications.

## Prerequisites

* Basic knowledge of Azure services
* Basic knowledge of operational concepts, such as monitoring, logging, and alerting
* Azure subscription
* Microsoft Sentinel instance in your Azure subscription

**Note**

If you choose to perform the exercise in this module, be aware you might incur costs in your Azure Subscription. To estimate the cost refer to **Microsoft Sentinel Pricing**
