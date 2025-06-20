
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


# 1.2 Exercise - Detect threats with Microsoft Sentinel analytics

The Threat detection with Microsoft Sentinel Analytics exercise in this module is an optional unit. However, if you want to perform this exercise, you need access to an Azure subscription where you can create Azure resources. If you don't have an Azure subscription, create a free account before you begin.

To deploy the prerequisites for the exercise, perform the following tasks.

**Note**

If you choose to perform the exercise in this module, be aware you might incur costs in your Azure Subscription. To estimate the cost, refer to Microsoft Sentinel Pricing.

## Task 1: Deploy Microsoft Sentinel using ARM template

1. Select the following link:

   Deploy To Azure.

https://aka.ms/deploytoazurebutton

   You're prompted to sign in to Azure. The Custom deployment pane appears.

3. On the **Basics** tab, enter the following values for each setting.

   | Setting | Value |
   |---------|-------|
   | **Project details** | |
   | Subscription | Select your Azure subscription. |
   | Resource group | Select **Create new**, and provide a name for the resource group, such as **azure-sentinel-rg**. |
   | **Instance details** | |
   | Region | From the dropdown list, select the location where you want to deploy the Microsoft Sentinel. |
   | Workspace Name | Provide a unique name for the Microsoft Sentinel Workspace such as **<yourName>-sentinel**, where **<yourName>** represents the workspace name that you chose in the previous task. |
   | Location | Accept the default value of **[resourceGroup().location]**. |
   | Simplevm Name | Accept the default value of **simple-vm**. |
   | Simplevm Windows OS Version | Accept the default value of **2022-Datacenter**. |


![](https://learn.microsoft.com/en-us/training/wwl-sci/analyze-data-in-sentinel/media/02-custom-deployment.png)

4. Select the **Review + create**. When validation passes, select **Create**.

   Screenshot of the Custom Deployment page.

**Note**

Wait for the deployment to complete. The deployment should take less than five minutes.

## Task 2: Check the resources created

1. In the Azure portal, search for **Resource groups**.

2. Select **azure-sentinel-rg**.

3. Sort the list of resources by **Type**.

The resource group should contain the resources listed in the following table.

| Name | Type | Description |
|------|------|-------------|
| **<yourName>-sentinel** | Log Analytics workspace | Log Analytics workspace used by Microsoft Sentinel, where **<yourName>** represents the workspace name that you chose in the previous task. |
| **simple-vmNetworkInterface** | Network interface | Network interface for the VM. |
| **SecurityInsights(<yourName>-sentinel)** | Solution | Security insights for Microsoft Sentinel. |
| **simple-vm** | Virtual machine | Virtual machine (VM) used in the demonstration. |
| **st1<xxxxx>** | Storage account | Storage account used by the VM, where **<xxxxx>** represents a random string generated to create a unique storage account name. |
| **vnet1** | Virtual network | Virtual network for the VM. |

**Note**

The resources deployed and configuration steps completed in this exercise are required in the next exercise. If you intended to complete the next exercise, don't delete the resources from this exercise.

## Task 3: Configure Microsoft Sentinel Data connectors

In this task, you deploy a Microsoft Sentinel Data connector to detect Azure Activity.

1. In the Azure portal, select **Home**, and then search for and select **Microsoft Sentinel**.

2. In the list of Sentinel workspace names, select the Microsoft Sentinel workspace you created in Task 2. The **Overview** pane for your Sentinel workspace appears.

3. In the menu pane, under **Content management**, select **Content hub**. The **Content hub** pane appears.

4. In the **Search** box, search for and select the **Azure Activity** Solution. On the **Azure Activity** details pane, select **Install**.

5. Wait for the install to complete and then select **Manage**.

6. In the **Search** box, search for and select the **Azure Activity** Data connector.

7. On the **Azure Activity** details pane, select **Open connector page**.

8. In the **Instructions** tab, **Configuration** area, scroll down and under "2. Connect your subscriptions..." select **Launch Azure Policy Assignment Wizard>**.

9. In the **Basics** tab, select the ellipsis button (...) under **Scope** and select your "Azure subscription" from the drop-down list and select **Select**.

10. Select the **Parameters** tab, choose your **yourName-sentinel** workspace from the **Primary Log Analytics workspace** drop-down list.

11. Select the **Remediation** tab and select the **Create a remediation task** checkbox. This action applies the subscription configuration to send the information to the Log Analytics workspace.

**Note**

To apply the policy to your existing resources, you need to create a remediation task.

12. Select the **Review + Create** button to review the configuration.

13. Select **Create** to finish.

14. Once the deployment is complete, you see the **Connected** status (green bar) for the Azure Activity connector in the **Configuration/Data connectors** pane.

    Screenshot of the Microsoft Sentinel connector

![](https://learn.microsoft.com/en-us/training/wwl-sci/analyze-data-in-sentinel/media/07-azure-sentinel-connector.png)

**Note**

The connector for Azure Activity could take 15 minutes to show Connected in Microsoft Sentinel. You can proceed with rest of the steps and with other units of this module.


# 1.3 What is Microsoft Sentinel Analytics?

Microsoft Sentinel Analytics helps you detect, investigate, and remediate cybersecurity threats. The Contoso SOC team can use Microsoft Sentinel Analytics to set up analytics rules and queries to detect issues in your environment.

## What is Microsoft Sentinel Analytics?

Microsoft Sentinel Analytics provides several functionalities that you can use to implement security for the data and resources at Contoso.

You can analyze historical data collected from your workstations, servers, networking devices, firewalls, intrusion prevention, sensors, and so on. Microsoft Sentinel Analytics analyzes data from various sources to identify correlations and anomalies.

By using analytics rules, you can trigger alerts based on the attack techniques that are used by known malicious actors. You can set up these rules to help ensure your SOC is alerted to potential security incidents in your environment in a timely fashion.

## Why use analytics rules for security operations?

Although some of the other products that Contoso implemented can help you identify threats, Microsoft Sentinel Analytics plays an important part in the overall detection of the security threat by correlating and matching the signals that impact the presence of a cybersecurity threat. With the proper analytics rule, you can get insights into where an attack originated from, what resources were compromised, potential data lost, along with the timeline for the incident.

Common security analytics use cases include:

- Identification of compromised accounts
- User behavior analysis to detect potentially suspicious patterns
- Network traffic analysis to locate trends indicating potential attacks
- Detection of data exfiltration by attackers
- Detection of insider threats
- Investigation of incidents
- Threat hunting

You might not be able to detect some of the threats by using conventional protection tools, such as firewalls or anti-malware solutions. Certain threats can go undetected for months. Combining data, gathered by multiple tools and products, with the power of threat intelligence can help you to detect, analyze, and mitigate insider threats.

You can also use analytics rules to create custom alerts that use indicators of attack. These indicators can identify potential attacks that are in progress in real time.

Analytics helps the Contoso SOC team to improve the efficiency of their complex investigation and detect threats faster.

## Exploring the Analytics home page

You can create analytics rules from the Analytics home page. You can access the Analytics page in Microsoft Sentinel from the navigation pane.

Screenshot of the Analytics rules and rule details page.

The Analytics home page has three main parts:

- The header bar contains information on the number of the rules that are currently in use.
- The list of rules and templates contains all the rule templates that Microsoft has preloaded from the Microsoft Sentinel GitHub repository.
- The details pane contains additional information that explains each template and rule that you can use in detection.

## Filter the rule templates

Currently Microsoft has preloaded over 150 template rules from the Microsoft Sentinel GitHub repository. To search these templates and to access the appropriate rule, you need to apply filters. For example, you might want to review only template rules that detect threats with a high severity level or rules from specific data sources.

To use filters, in the header bar, select the filters you want to use.

Screenshot of filtering the Analytics home page.

The Analytics home page provides the following filters:

- **Severity.** Use to filter the rules by levels of severity.
- **Rule Type.** There are currently seven types of rules: Scheduled, NRT (near real time), Fusion, Microsoft Security, ML (machine learning) Behavior Analytics, and Threat Intelligence.
- **Tactics.** Use to filter the rules based on 14 specific methodologies in ATT&CK model.
- **Data Sources.** Use to filter the rules by the data source connector that generates the alert.

**Note**

MITRE ATT&CK is a globally accessible knowledge base of adversary tactics and techniques based on real-world observations. The ATT&CK knowledge base is used as a foundation for the development of specific threat models and methodologies in the private sector, in government, and in the cybersecurity product and service community.

## Check your knowledge

### 1. Which of the following aren't common use cases of analytics rules?

- Identifying compromised accounts.
- Detecting insider threats.
- **Visualizing data from Microsoft Sentinel Connectors.**

### 2. You want to find additional information that explains the analytics template and the rule that is used in detection of the threats. Which section in the analytics rules page provides that information?

- **Details pane**
- Header bar
- Rules and templates section

---

## Відповіді:

1. **Visualizing data from Microsoft Sentinel Connectors** - Візуалізація даних не є типовим використанням аналітичних правил. Аналітичні правила призначені для виявлення загроз, а не для візуалізації даних.

2. **Details pane** - Панель деталей містить додаткову інформацію, яка пояснює кожен шаблон та правило, що можна використовувати для виявлення загроз, як зазначено в тексті: "The details pane contains additional information that explains each template and rule that you can use in detection."



# 1.4 Types of analytics rules


By using Microsoft Sentinel Analytics rules, you can configure notification and alerts based on data coming from the sources that are connected to Microsoft Sentinel. These alerts help ensure that the Contoso SOC team knows when a threat occurs, and the team can then appropriately react to prevent the threat from reaching your corporate assets.

## Types of analytics rules

You can search for potential threats by using the built-in analytics rules that Microsoft Sentinel Analytics provides, including the following types:

- Anomaly
- Fusion
- Microsoft security
- Machine learning (ML) behavior analytics
- Scheduled alerts
- NRT (Near Real Time) rules
- Threat Intelligence

Screenshot of rule templates in the Analytics home page.

![](https://learn.microsoft.com/en-us/training/wwl-sci/analyze-data-in-sentinel/media/03-rule-templates.png)

## Anomaly

Anomaly alerts are informational and identify anomalous behaviors.

## Fusion

Microsoft Sentinel uses the Fusion correlation engine, with its scalable machine learning algorithms, to detect advanced multistage attacks. The engine correlates many low-fidelity alerts and events across multiple products into high-fidelity and actionable incidents. Fusion is enabled by default. Because the logic is hidden and therefore not customizable, you can only create one rule with this template.

The Fusion engine can also correlate alerts from scheduled analytics rules with alerts from other systems, producing high-fidelity incidents as a result.

By default, Fusion detection is enabled in Microsoft Sentinel. Microsoft is constantly updating Fusion detection scenarios for threat detection. At the time of writing this article, for Anomaly and Fusion detection, you must configure the following data connectors:

**Out-of-the-box anomaly detections**

**Alerts from Microsoft Products**
- Microsoft Entra ID Protection
- Microsoft Defender for Cloud
- Microsoft Defender for IoT
- Microsoft Defender XDR
- Microsoft Defender for Cloud Apps
- Microsoft Defender for Endpoint
- Microsoft Defender for Identity
- Microsoft Defender for Office 365

**Alerts from scheduled analytics rules**, both built-in and created by your security analysts. Analytics rules must contain kill-chain (tactics) and entity mapping information in order to be used by Fusion

Some of the common attack detection scenarios that Fusion alerts identify include:

**Data exfiltration.** Suspicious activity detected, such as suspicious forwarding rule in Microsoft 365 mailbox, after a suspicious sign-in to Microsoft Entra account can indicate compromised user account.

**Data destruction.** Anomalous number of unique files that were deleted after a suspicious sign-in to Microsoft Entra account can signal that a compromised user account was used to destroy data.

**Denial of service.** Significant number of Azure virtual machines (VMs) deleted after a suspicious sign-in to Microsoft Entra account can signal a compromised user account that can be used to destroy the organization's assets.

**Lateral movement.** Significant number of impersonation actions that occur after a suspicious sign-in to Microsoft Entra account can indicate a compromised user account that was used for malicious purposes.

**Ransomware.** After a suspicious sign-in to a Microsoft Entra account, unusual user behavior used to encrypt data can trigger a ransomware execution alert.

**Note**

For more information on the Fusion technology in Microsoft Sentinel, see Advanced multistage attack detection in Microsoft Sentinel

## Microsoft security

You can configure Microsoft security solutions that are connected to Microsoft Sentinel to automatically create incidents from all alerts generated in the connected service.

For example, you can configure for Contoso to be alerted when a user who is categorized as a high-risk threat attempts to sign in and access corporate resources.

You can configure the following security solutions to pass their alerts to Microsoft Sentinel:

- Microsoft Defender for Cloud Apps
- Microsoft Defender for Server
- Microsoft Defender for IoT
- Microsoft Defender for Identity
- Microsoft Defender for Office 365
- Microsoft Entra ID Protection
- Microsoft Defender for Endpoint

**Note**

Microsoft unifies security information and event management (SIEM) and extended detection and response (XDR) terminology across their security products.

You can filter these alerts by severity and by specific text that is contained in the alert name.

## ML behavior analytics

Microsoft Sentinel Analytics includes built-in machine learning behavior analytics rules. You can't edit these built-in rules or review the rule settings. These rules use Microsoft machine learning algorithms to detect suspicious activity. Machine Learning algorithms correlate several low-fidelity incidents into a high-fidelity security incident. This correlation saves hours that you might otherwise spend manually analyzing numerous alerts from different products and correlating them. Machine learning algorithms that analytics rules use also help reduce the noise around alerts by quickly ingesting and connecting important data.

For example, by using a machine learning behavior analytics rule, you can detect an anomalous secure shell protocol (SSH) sign-in or remote desktop protocol (RDP) sign-in activity.

## Scheduled alerts

Scheduled alerts analytics rules provide you with the highest level of customization. You can define your own expression using Kusto Query Language (KQL) to filter the security events, and you can set up a schedule for the rule to run.

## Check your knowledge

### 1. Which one of the analytics rules can you customize with your own query rules?

- Fusion
- Machine learning behavior analytics
- **Scheduled analytic rules**

### 2. Which type of the template rules can create incidents based on all alerts generated in Microsoft Defender for Cloud?

- Machine learning behavioral analytics
- Fusion
- **Microsoft security**

---

## Відповіді:

1. **Scheduled analytic rules** - Згідно з текстом: "Scheduled alerts analytics rules provide you with the highest level of customization. You can define your own expression using Kusto Query Language (KQL) to filter the security events, and you can set up a schedule for the rule to run."

2. **Microsoft security** - У тексті зазначено: "You can configure Microsoft security solutions that are connected to Microsoft Sentinel to automatically create incidents from all alerts generated in the connected service" і Microsoft Defender for Cloud входить до списку підтримуваних рішень безпеки Microsoft.


# 1.5 Create an analytics rule from templates

The Analytics section in Microsoft Sentinel contains rule templates that are preloaded from the Microsoft Sentinel GitHub repository. You can use these templates to create a rule to detect security threats.

## Exploring the existing rule templates

You can use some of the existing rule templates to create a single rule and others to create multiple rules with different customization options. Templates in use display the **IN USE** label on the template page as displayed in the following screenshot.

Screenshot of the template in use.

By selecting one of the rules on the **Rule Templates** tab, you can observe the properties of the rule. For each rule, you can review:

**Severity level.** This indicates the importance of the alert. There are four severity levels:

- High
- Medium
- Low
- Informational

**Name of the rule.** This provides a meaningful name for the alert rule.

**Rule type.** This defines the type of the rule, which can be one of the following types:

- Anomaly
- Fusion
- Microsoft Security
- ML Behavior Analytics
- Scheduled
- NRT (Near Real Time)

**Data Source.** This specifies the data source connector that generated the alert.

**Tactics.** This specifies methodologies in MITRE ATT&CK model used by different kinds of malware.

**Note**

MITRE ATT&CK is a globally accessible knowledge base of adversary tactics and techniques based on real-world observations. The ATT&CK knowledge base provides a foundation for the development of specific threat models and methodologies in the private sector, in government, and in the cybersecurity product and service community.

When you select a rule from the list on either the **Active rules** tab or the **Rule templates** tab, the details pane provides more information for the selected rule.

## Creating an analytic rule from a rule template

When you select a predefined rule template, the details pane may display filters that can be used to define how that rule behaves. For Fusion and ML behavior analytics rules, Microsoft doesn't provide any editable information. However, for scheduled rules and Microsoft Security, you can view or edit the query, filters, and includes and excludes used in the threat detection. By selecting the **Create rule** button, you can define the analytics rule logic using a wizard that helps you customize a rule from the selected template.

For Fusion and ML behavior analytics templates, you can only enable or disable them as active rules.

A rule that you create from a Microsoft security template consists of the following elements:

## General tab

The following table lists the inputs on the **General** tab.

| Field | Description |
|-------|-------------|
| Name | This is prepopulated from the name of the rule template. |
| Description | Provide more details about the creation of the alerts. |
| Status | This indicates whether the analytics rule is enabled or disabled. |
| Microsoft security service | This indicates the source of the alert from one of the Microsoft security services. |
| Filter by severity | Use to tune alerts from a source based on the severity level; if you select custom, you can specify High, Medium, Low, or Informational. |
| Include specific alerts | Add one or more words to include results of alerts that contain specific text in their name. |
| Exclude specific alerts | Add one or more words to exclude results of alerts that contain specific text in their name. |

## Automated response

On the **Automated response** tab, you can define automation rules. If you select **Add new**, the **Create new automation rule** pane opens. The following fields are inputs:

| Field | Description |
|-------|-------------|
| Automation rule name | Choose a name that uniquely describes this automation rule |
| Trigger | Predefined value that can't be changed. |
| Conditions | Typical query filter construct that can be edited and sorted. |
| Actions | Selection list of actions; select which action you want to be performed if the query filter conditions are met. |
| Rule expiration | Date and time for rule to be disabled. Default is indefinite. |
| Order | If multiple rules are created, select sequential numbers to reorder the incident automation rules in the left pane. |

**Note**

When you implement filters to include or exclude specific alerts based on a text string, these alerts will not appear in Microsoft Sentinel.

The following screenshot presents an example of creating an incident from alerts generated by the Microsoft Defender for Cloud.

Screenshot of the wizard used to create analytics rules from templates.

For instructions on how to create an analytics rule from a scheduled rule type template, see Create an analytics rule from a scheduled rule template in next unit (Unit 6).

**Note**

For certain rule templates, the **Create rule** button might be disabled, which indicates that you can't create a rule from selected template because of a missing data source.

## Check your knowledge

### 1. Which one of the template types should you use to create an incident based on all alerts generated in Microsoft Defender for Cloud?

- Fusion
- Machine learning behavior analytics
- **Microsoft Security**

### 2. Which one of the following template rules are precreated in Microsoft Sentinel Analytics?

- Scheduled template rules
- **Fusion**
- Machine learning behavior analytics templates

---

## Відповіді:

1. **Microsoft Security** - Згідно з текстом, Microsoft Security правила дозволяють створювати інциденти на основі всіх алертів, згенерованих підключеними службами безпеки Microsoft, включаючи Microsoft Defender for Cloud.

2. **Fusion** - У тексті зазначено, що Fusion правила є попередньо створеними в Microsoft Sentinel Analytics: "Fusion is enabled by default" і "you can only create one rule with this template", що вказує на те, що це попередньо створене правило.
