
# SC-200: Perform threat hunting in Microsoft Sentinel

https://learn.microsoft.com/en-us/training/paths/sc-200-perform-threat-hunting-azure-sentinel/


Proactively hunt for security threats using the Microsoft Sentinel powerful threat hunting tools. This learning path aligns with exam SC-200: Microsoft Security Operations Analyst.

#### Prerequisites
- Ability to use KQL in Microsoft Sentinel like you could learn from learning path SC-200: Create queries for Microsoft Sentinel using Kusto Query Language (KQL)
- Know how to create detections and perform investigations like you could learn from learning path SC-200: Create detections and perform investigations using Microsoft Sentinel


# 1 Explain threat hunting concepts in Microsoft Sentinel

Learn the threat hunting process in Microsoft Sentinel.

### Learning objectives
Upon completion of this module, the learner is able to:
- Describe threat hunting concepts for use with Microsoft Sentinel
- Define a threat hunting hypothesis for use in Microsoft Sentinel


# 1.1 Introduction

Microsoft Sentinel provides the tools to perform Threat Hunting. Before starting the hunt, it's crucial to understand the Threat Hunting process.

You're a Security Operations Analyst working at a company that implemented Microsoft Sentinel. You want to mature your Security Operations team to proactively hunt for malicious activity in your environment.

You suggest to management to create a threat hunting team. You must explain to management the benefit, processes, and tasks of a threat hunting team. You'll demonstrate how to develop a quality hypothesis for hunting.

After completing this module, you'll be able to:

* Describe threat hunting concepts for use with Microsoft Sentinel
* Define a threat hunting hypothesis for use in Microsoft Sentinel

## Prerequisites

Basic knowledge of operational concepts such as monitoring, logging, and alerting


# 1.2 Understand cybersecurity threat hunts

The term "threat hunting" is defined differently by different people. The most commonly used definition is the idea that you're proactively hunting through your environment for a threat or a set of activities that you haven't previously detected. The "not previously detected" part is what differentiates threat hunting from incident response or alert triage.

Other uses of the term hunting include searching for threats with newly obtained indicators. If a Threat Intelligence Feed provides a new IP Address considered harmful, an analyst can then take the IP Address and search the logs to find if the new indicator was seen in the past. Technically this isn't threat hunting because you're using a known bad such as an IP Address. Microsoft Sentinel already provides hunting queries to facilitate this process. Next, hunt for more evidence-based threats from a current Incident or Alert as part of an Incident Analysis process. It's vital to explore data based on evidence found in a current incident. Both Microsoft Sentinel and Microsoft Defender XDR provide this type of hunting capability.

All of these approaches have one thing in common: using KQL queries to find threats.

Microsoft Defender and Microsoft Defender Endpoint are more focused on indicator and analysis types of hunting. Microsoft Sentinel provides more features to manage the threat hunting process.

## Proactive hunts

Why do proactive hunting? As you hunt for "not previously detected" threats, the concern is that if you wait for the threat to be detected, the compromise impact could be more significant. If we don't have a known indicator, then what are we hunting? We hunt based on a Hypothesis. The Hypothesis might start with "Operational Threat Intelligence," and then list the attackers' tactics and techniques. A Hypothesis can search for a specific technique, not an indicator like an IP address. If malicious activity is identified, we might have discovered the attacker earlier in the attack process before they have an opportunity to exfiltrate data.

## Process to hunt threats

Threat hunting should be a continual process. We start at the top of our cycle with our Hypothesis. Our Hypothesis helps us plan out what we are going to hunt for, which requires us to understand where we're going to hunt and how we'll do it. This means we need to understand the data we have, the tools we have, the expertise we have, and how to work with them. The hunting cycle doesn't stop when we execute the hunt. There are still several phases we need to conduct throughout the life cycle, including responding to anomalies. Even if we don't find an active threat, there will be activities to perform.

Routine tasks should include:

* Setting up new monitoring.
* Improving our detection capabilities.

Everything done in Threat Hunting should be documented. Documentation for the hunt should include:

* What, How, and Why
* Input and Output
* How to replicate the hunt
* Next Steps


# 1.3 Develop a hypothesis

Hunting starts with a Hypothesis. The idea of what we are going to hunt. Getting this right is critical because it drives our focuses on what we are going to do. What makes a good Hypothesis?

There are many factors, but here are the key ones:

**Keep it achievable**. Don't perform a hunt where you know you have no hope of finding results. It could be that you don't have the data available, or have insufficient knowledge about the threat to understand how to find it.

**Keep the scope narrow**. Avoid broad a hypothesis such as "I'm going to hunt for strange log-ons." Such a hypothesis fails to define what the results could mean.

**Keep it time-bound**. Are you looking for any sign-ins since the beginning of your logs? Are you looking for last week? The last day? The time-bounded also is used in documentation. You'll want Threat Hunting to be a continual process. If you don't time-bound your hunts, there's a chance that you'll end up just repeating the same hunt on the same dataset. You'll be able to say, "I did this hunt, at this time, covering this period." With this documented, your team members will know what period was hunted for with this Hypothesis.

**Keep it useful and efficient**. You want to target threats that maybe you don't have adequate coverage for in your detections. These might be things that you know that you've previously missed or that you haven't detected. A good SOC team typically has a good idea about where their coverage is good and where it may be weaker and needs improvement. You also want to make sure it relates to realistic threats. There's no point in hunting for an advanced threat that targets an industry you're not in or a platform you aren't using.

**Keep it related to the threat model that  you are defending against**. Otherwise, you may spend much time threat hunting for things that you'll never find and which aren't a threat.

Don't start your Threat Hunting journey going after the most advanced threats. Start with the basics and incrementally mature your organization's Threat Hunting capabilities. Start with a simple Hunt Hypothesis. An example hypothesis could be that we have Threat Intel that a Threat Actor, has automated attacks that use the cmd.exe process.

Another Hypothesis could be; We want to check for the last day in which accounts have run cmd.exe, but that have not run cmd.exe during the past week.



# 1.4Explore MITRE ATT&CK

MITRE ATT&CK is a publicly accessible knowledge base of tactics, techniques, and procedures (TTP) that are commonly used by attackers, and is created and maintained by observing real-world observations. Many organizations use the MITRE ATT&CK knowledge base to develop specific threat models and methodologies that are used to verify security status in their environments.

Microsoft Sentinel analyzes ingested data, not only to detect threats and help you investigate, but also to visualize the nature and coverage of your organization's security status.

When developing a threat hunting hypothesis, it's critical to understand the tactics (why), techniques (how), and procedures (implementations) you're searching for. The MITRE ATT&CK framework is used throughout Microsoft Sentinel.

Use the MITRE ATT&CK selection under Threat Management in Microsoft Sentinel to view the detections already active in your workspace, and those available for you to configure, to understand your organization's security coverage, based on the tactics and techniques from the MITRE ATT&CK® framework.

## View current MITRE coverage

**Defender portal**
**Azure portal**

In Microsoft Sentinel, in the Defender portal, select the Threat management section of the navigation menu, select MITRE ATT&CK. By default, Active scheduled query, Active near real-time (NRT) rules, and Active anomaly query rules are indicated in the coverage matrix.

Use the legend at the top-right to understand how many detections are currently active in your workspace for specific technique.

Use the search bar at the top right to search for a specific technique in the matrix, using the technique name or ID, to view your organization's security status for the selected technique.

Select a specific technique in the top row of the matrix to view in the details pane on the right. There, use the links to jump to any of the following locations:

Select View full tactic or technique details links for more information in the MITRE ATT&CK framework knowledge base.

Select links to any of the Active coverage rules to jump to the relevant area in Microsoft Sentinel.

View MITRE by threat scenarios to view the coverage matrix by threat scenarios:

Drag the View MITRE by threat scenarios slider to the right to view the coverage matrix by threat scenarios. The matrix is filtered to show only the techniques that are relevant to the selected scenario.

Screenshot of the MITRE ATT&CK threat scenarios drop down menu.

![](https://learn.microsoft.com/en-us/training/wwl-sci/what-is-threat-hunting-azure-sentinel/media/mitre-threat-hunting-scenario.png)

## Simulate possible rules coverage

In the MITRE matrix, simulated coverage refers to detections that are available, but not currently configured, in your Microsoft Sentinel workspace. View your simulated coverage to understand your organization's possible security status, were you to configure all detections available to you.

**Important**

If you have the View MITRE by threat scenarios slider enabled, and have selected a scenario, the Simulated rules (Product simulation) will be disabled.

From the Microsoft Defender navigation menu, expand the Microsoft Sentinel section, and select Threat management, then select MITRE ATT&CK.

Select items in the Simulated rules drop-down menu to simulate your organization's possible security status.

For example, select Hunting queries, and then select Hunting queries View link to jump to the Microsoft Sentinel Hunting page. There, you see a filtered list of the hunting queries that are associated with the selected technique, and available for you to configure in your workspace.

![](https://learn.microsoft.com/en-us/training/wwl-sci/what-is-threat-hunting-azure-sentinel/media/mitre-simulated-rules.png)


## Use the MITRE ATT&CK framework in analytics rules and incidents

Having a scheduled analytical rule with MITRE techniques applied running regularly in your Microsoft Sentinel workspace enhances the security status shown for your organization in the MITRE coverage matrix.

**Analytics rules:**

When configuring analytics rules, select specific MITRE techniques to apply to your rule.

When searching for analytics rules, filter the rules displayed by technique to find your rules quicker.

![](https://learn.microsoft.com/en-us/training/wwl-sci/what-is-threat-hunting-azure-sentinel/media/mitre-analytic-rule-technique.png)

Screenshot of the MITRE ATT&CK analytics rules configuration.

**Incidents:**

When incidents are created for alerts that are surfaced by rules with MITRE techniques configured, the techniques are also added to the incidents.

**Threat hunting:**

When creating a new hunting query, select the specific tactics and techniques to apply to your query.

When searching for active hunting queries, filter the queries displayed by tactics by selecting an item from the list above the grid. Select a query to see tactic and technique details on the right.

When creating bookmarks, either use the technique mapping inherited from the hunting query, or create your own mapping.


# 1.5 Module assessment

Choose the best response for each of the questions below.

## Check your knowledge

### 1.
**Which of the following best describes a good Hypothesis?**

- **is Time-bound**
- focuses on known Indicators
- focuses on all current threats

### 2.
**Threat Hunting is considered which of the following?**

- Retroactive.
- Reactive.
- **Proactive.**

### 3.
**"We want to check which accounts have run cmd.exe." Why is this hypothesis poor?**

- Cmd.exe isn't a program.
- Accounts aren't associated with the running of cmd.exe
- **The scope is too broad.**

---

## Відповіді:

1. **is Time-bound** - Хороша гіпотеза повинна бути обмежена в часі. Це один з ключових факторів, згаданих у модулі як критичний для розробки якісної гіпотези для полювання на загрози.

2. **Proactive** - Threat Hunting є проактивним процесом. Це основна характеристика полювання на загрози - проактивний пошук загроз, які ще не були виявлені, на відміну від реактивного реагування на інциденти.

3. **The scope is too broad** - Ця гіпотеза має занадто широкий обсяг. У модулі зазначається, що потрібно "Keep the scope narrow" (тримати обсяг вузьким) і уникати широких гіпотез, які не визначають, що можуть означати результати.






# 2 Threat hunting with Microsoft Sentinel

In this module, you'll learn to proactively identify threat behaviors by using Microsoft Sentinel queries. You'll also learn to use bookmarks and livestream to hunt threats.

### Learning objectives
In this module, you will:

Use queries to hunt for threats.
Save key findings with bookmarks.
Observe threats over time with livestream.
#### Prerequisites
- Familiarity with security operations in an organization.
- Basic experience with Azure services.
- Basic knowledge of operational concepts such as monitoring, logging, and alerting.
- Basic Microsoft Sentinel functionality.
- Access to a Microsoft Azure subscription for exercise tasks.


# 2.1 Introduction

Use Microsoft Sentinel to hunt for security threats across on-premises and cloud environments by using interactive queries and other tools.

This module imagines a midsize financial services company called Contoso, Ltd., based in London with a New York branch office. Contoso uses Microsoft 365, Microsoft Entra ID, Microsoft Entra ID Protection, Microsoft Defender for Cloud Apps, Microsoft Defender for Identity, Microsoft Defender for Endpoint, Microsoft Defender for Office 365, Endpoint Protection, and Azure Information Protection.

As part of the Security Operations Center team, you've been tasked with using Microsoft Sentinel to identify security threats within Contoso's Azure environment.

By the end of this module, you'll be able to hunt for threats by using the tools available in Microsoft Sentinel. Specifically, you'll be able to proactively identify threat behaviors by using Microsoft Sentinel queries. You'll also be able to use bookmarks and livestream to identify specific account usage patterns for Contoso's Azure environment.

## Learning objectives

After completing this module, you'll be able to:

* Use queries to hunt for threats.
* Save key findings with bookmarks.
* Observe threats over time with livestream.

## Prerequisites

To get the best learning experience from this module, you should have the following:

* Familiarity with security operations in an organization.
* Basic experience with configuring Azure services, specifically Azure Policy.
* Basic knowledge of operational concepts such as monitoring, logging, and alerting.
* Basic Microsoft Sentinel functionality.
* Access to a Microsoft Azure subscription for exercise tasks.

# 2.2 Exercise setup

To complete this optional exercise, you need access to an Azure subscription to create Azure resources. If you don't have an Azure subscription, create a free account before you begin.

**Note**

If you perform the exercises in this module, you might incur costs in your Azure subscription. To estimate the costs, see **Microsoft Sentinel pricing**.

To deploy the prerequisites for the exercise, perform the following tasks.

## Deploy the Azure Resource Manager template for the exercise environment

1. Select the following link:

You're prompted to sign in to Azure.

2. On the **Custom deployment** page, provide the following information:

**Expand table**

| Name | Description |
|------|-------------|
| **Subscription** | Select your Azure subscription. |
| **Resource Group** | Select **Create new** and provide a name for the resource group, such as `azure-sentinel-rg`. |
| **Region** | Select an Azure region. |
| **Workspace name** | Provide a unique name for the Microsoft Sentinel workspace, such as `<yourName>-sentinel`, where *<yourName>* represents the workspace name that you chose in the previous task. |
| **Location** | Accept the default value **[resourceGroup().location]**. |
| **Simplevm Name** | Accept the default value **simple-vm**. |
| **Simplevm Windows OS Version** | Accept the default value **2022-Datacenter**. |

3. Select **Review + create**, and then select **Create**.

![](https://learn.microsoft.com/en-us/training/wwl-sci/hunt-threats-sentinel/media/02-custom-deployment.png)

**Note**

Wait for the deployment to finish. The deployment should take less than five minutes.

## Check created resources

1. In the Azure portal, search for **Resource groups**.
2. Select your resource group.
3. Sort the list of resources by **Type**.
4. The resource group should contain the resources displayed in this table:

**Expand table**

| Name | Type | Description |
|------|------|-------------|
| `<yourName>-sentinel` | Log Analytics workspace | Log Analytics workspace used by Microsoft Sentinel, where *<yourName>* represents the workspace name that you chose in the previous task. |
| `simple-vmNetworkInterface` | Network interface | Network interface for the virtual machine (VM). |
| `SecurityInsights(<yourName>-sentinel)` | Solution | Security insights for Microsoft Sentinel. |
| `simple-vm` | Virtual machine | VM used in the demonstration. |
| `st1<xxxxx>` | Storage account | Storage account used by the VM, where *<xxxxx>* represents a random string generated to create a unique storage account name. |
| `vnet1` | Virtual network | Virtual network for the VM. |

## Configure Microsoft Sentinel connectors

In this task, you deploy a Microsoft Sentinel connector to Azure Activity.

1. In the Azure portal, search for and select **Microsoft Sentinel**, and then select the previously created Microsoft Sentinel workspace.
2. On the **Microsoft Sentinel** page, on the menu bar, in the **Configuration** section, select **Data connectors**.
3. On the **Data connectors** pane, search for and select **Azure Activity**. On the details pane, select **Open connector page**.
4. Review the **Prerequisites**. You need to have the owner role assigned for Azure Policy assignment scopes.
5. If you have a subscription connected with the *legacy method*, you're directed to disconnect it using the **Configuration** instructions for "1. Disconnect your subscriptions from the legacy method".
6. If you didn't have the connector configured with the legacy method, proceed to "2. Connect your subscriptions..." in the **Configuration** area.
7. Select **Launch Azure Policy Assignment Wizard>**.
8. In the **Basics** tab, select the ellipsis button (...) under **Scope** and choose your subscription from the drop-down list. Then choose **Select**.
9. Select the **Parameters** tab, choose your *uniquename-sentinel* workspace from the **Primary Log Analytics workspace** drop-down list.
10. Select the **Remediation** tab and check the **Create a remediation task** box.
11. Select the **Review + Create** button to review the configuration.
12. Select **Create** to finish.

**Note**

The connector for Azure Activity uses policy assignments, so it might take 15 to 30 minutes to display a status of **Connected**.




# 5.3 Explore creation and management of threat-hunting queries

Microsoft Sentinel contains powerful query tools that can help you, as part of the Security Operations Center team, find and isolate security threats and unwanted activity in Contoso's environment.

## Hunt by using built-in queries

You can use the search and query tools in Microsoft Sentinel to hunt for security threats and tactics throughout your environment. These tools let you filter through large amounts of events and security data sources to identify potential threats or track down known or expected threats.

The Hunting page in Microsoft Sentinel has built-in queries that can guide your hunting process and help you pursue the appropriate hunting paths to uncover issues in your environment. Hunting queries can expose issues that aren't significant enough on their own to generate an alert but have happened often enough over time to warrant investigation.


![](https://learn.microsoft.com/en-us/training/wwl-sci/hunt-threats-sentinel/media/3-hunting-page.png)

Screenshot that shows the Hunting page in Microsoft Sentinel.

The Hunting page provides a list all hunting queries. You can filter and sort queries by name, provider, data source, results, and tactics. You can save queries by selecting the Favorites star icon for the query in the list.

**Tip**

When a query is selected as a favorite, it runs automatically each time you open the Hunting page.

## Manage hunting queries

When you select a query from the list, the query details appear on a new pane that contains a description, code, and other information about the query. That information includes related entities and identified tactics. You can run a query interactively by selecting Run Query on the details pane.

## Hunt for threats by using the MITRE ATT&CK framework

Microsoft Sentinel uses the MITRE ATT&CK framework to categorize and order queries by tactics. ATT&CK is a knowledge base of tactics and techniques that are used and observed in the global threat landscape. You can use MITRE ATT&CK to develop and inform your threat-hunting models and methods in Microsoft Sentinel. When you're threat hunting in Microsoft Sentinel, you can use the ATT&CK framework to categorize and run queries by using the MITRE ATT&CK tactics timeline.

**Note**

You can select individual MITRE ATT&CK tactics from the timeline on the Hunting page.

![](https://learn.microsoft.com/en-us/training/wwl-sci/hunt-threats-sentinel/media/3-attack-timeline.png)

Selecting any tactic filters the available queries by the selected tactic. The following Hunting tactics are from the ATT&CK Enterprise and ICS (Industrial Control Systems) matrices:

**Reconnaissance.** Tactics that the adversary uses to find information they can use to plan future operations.

**Resource development.** Tactics that the adversary uses to establish resources they can use to support operations. Resources include infrastructure, accounts, or capabilities.

**Initial access.** Tactics that the adversary uses to gain entry to a network, by exploiting vulnerabilities or configuration weaknesses in public-facing systems. An example is targeted spear-phishing.

**Execution.** Tactics that result in an adversary running their code on a target system. For example, a malicious hacker might run a PowerShell script to download more attacker tools and/or scan other systems.

**Persistence.** Tactics that allow an adversary to maintain access to a target system, even after restarts and credential changes. An example of a persistence technique is an attacker who creates a scheduled task that runs their code at a specific time or on restart.

**Privilege escalation.** Tactics that an adversary uses to gain higher-level privileges on a system, such as local administrator or root.

**Defense evasion.** Tactics that attackers use to avoid detection. Evasion tactics include hiding malicious code within trusted processes and folders, encrypting or obfuscating adversary code, or disabling security software.

**Credential access.** Tactics deployed on systems and networks to steal usernames and credentials for reuse.

**Discovery.** Tactics that adversaries use to obtain information about systems and networks that they want to exploit or use for their tactical advantage.

**Lateral movement.** Tactics that allow an attacker to move from one system to another within a network. Common techniques include pass-the-hash methods of authenticating users and abuse of the Remote Desktop Protocol.

**Collection.** Tactics that an adversary uses to gather and consolidate the information they were targeting as part of their objectives.

**Command and control.** Tactics that an attacker uses to communicate with a system under their control. One example is an attacker communicating with a system over an uncommon or high-numbered port to evade detection by security appliances or proxies.

**Exfiltration.** Tactics used to move data from the compromised network to a system or network that's fully under control of the attacker.

**Impact.** Tactics that an attacker uses to affect the availability of systems, networks, and data. Methods in this category include denial-of-service attacks and disk-wiping or data-wiping software.

**Impair Process Control.** Tactics the adversary uses to manipulate, disable, or damage physical control processes.

**Inhibit Response Function.** Tactics the adversary uses to prevent your safety, protection, quality assurance, and operator intervention functions from responding to a failure, hazard, or unsafe state.

**None.**

## Create custom queries to refine threat hunting

All Microsoft Sentinel hunting queries use Kusto Query Language (KQL) syntax used in Log Analytics. You can modify a query in the details pane and run the new query. Or you can save it as a new query that can be reused in your Microsoft Sentinel workspace.

You can also create your own custom queries by using KQL code to hunt for threats.

![](https://learn.microsoft.com/en-us/training/wwl-sci/hunt-threats-sentinel/media/3-create-custom-query-page.png)

Screenshot that shows the page for creating a custom query in Microsoft Sentinel.

Custom queries allow you to define the following:

| Query parameter | Description |
|-----------------|-------------|
| Name | Provide a name for the custom query. |
| Description | Provide a description of your query's functionality. |
| Custom query | Your KQL hunting query. |
| Entity mapping | Map entity types to columns from your query result to populate your query results with more actionable information. You can also map entities by using code in your KQL query. |
| Tactics & techniques | Specify the tactics that your query is designed to expose. |

Custom queries are listed alongside built-in queries for management.

## 5.4 Explore Microsoft Sentinel on GitHub

The Microsoft Sentinel repository contains out-of-the-box detections, exploration queries, hunting queries, workbooks, playbooks, and more to help you secure your environment and hunt for threats. Microsoft and the Microsoft Sentinel community contribute to this repo.

The repo contains folders with contributed content for several areas of Microsoft Sentinel functionality, including hunting queries. You can use the code from these queries to create custom queries in your Microsoft Sentinel workspace.

Choose the best response for the following question.

## Check your knowledge

### 1. Which code syntax is used for Microsoft Sentinel hunting queries?

- T-SQL (Transact-SQL)
- Kusto Query Language (KQL)
- JavaScript Object Notation (JSON)


# Save key findings with bookmarks

To hunt for threats to Contoso's environment, you have to review large amounts of log data for evidence of malicious behavior. During this process, you might find events that you want to remember, revisit, and analyze as part of validating potential hypotheses and understanding the full story of a compromise.

## Hunt by using bookmarks

Bookmarks in Microsoft Sentinel can help you hunt for threats by preserving the queries you already ran, along with the query results that you deem relevant. You can also record your contextual observations and reference your findings by adding notes and tags. Bookmarked data is visible to you and your teammates for easy collaboration.

You can revisit your bookmarked data at any time on the **Bookmarks** tab of the **Hunting** page. You can use filtering and search options to quickly find specific data for your current investigation. Alternatively, you can review your bookmarked data directly in the **HuntingBookmark** table in your Log Analytics workspace.

**Note**

Bookmarked events contain standard event information but can be used in different ways throughout the Microsoft Sentinel interface.

## Create or add to incidents by using bookmarks

You can use bookmarks to create a new incident or add bookmarked query results to existing incidents. The **Incident actions** button on the *Hunt* toolbar enables you to perform either of these tasks when a bookmark is selected.

![](https://learn.microsoft.com/en-us/training/wwl-sci/hunt-threats-sentinel/media/4-incident-actions.png)

Incidents that you create from bookmarks can be managed from the **Incidents** page alongside other incidents created in Microsoft Sentinel.

## Use the investigation graph to explore bookmarks

You can investigate bookmarks in the same way that you'd investigate incidents in Microsoft Sentinel. From the **Hunting** page, select your *Hunt* with a *Bookmark* from the **Hunts (Preview)** tab. In the *Hunt* details pane select **Bookmarks** (or select any *Related incidents*), select a specific *Bookmark* and then select the **Investigate** button to open the investigation graph for the incident. The investigation graph is a visual tool that helps to identify entities involved in the attack and the relationships between those entities. If the incident involves multiple alerts over time, you can also review the alert timeline and correlations between alerts.

![](https://learn.microsoft.com/en-us/training/wwl-sci/hunt-threats-sentinel/media/4-investigation-graph.png)

## Review entity details

You can select each entity on the graph to observe complete contextual information about it. This information includes relationships to other entities, account usage, and data flow information. For each information area, you can go to the related events in Log Analytics and add the related alert data into the graph.

## Review bookmark details

You can select the bookmark item on the graph to observe important bookmark metadata related to the bookmark's security and environment context.

Choose the best response for the following question.

## Check your knowledge

### 1.
**How do bookmarks aid in the threat-hunting process?**

- **They enable the hunter to save query results for later reference.**
- They enable the hunter to track incident status and resolution.
- They enable the hunter to create workbooks from query results.

---

## Відповідь:

**They enable the hunter to save query results for later reference.** - Закладки в Microsoft Sentinel допомагають у процесі полювання на загрози, зберігаючи запити та їх результати, які вважаються релевантними. Вони дозволяють аналітикам записувати контекстуальні спостереження, додавати нотатки та теги, а також легко повертатися до збережених даних для подальшого аналізу та співпраці з командою.



# 5.5 Observe threats over time with livestream

You can use the hunting livestream to test queries against live events as they occur. Livestream provides interactive sessions that can notify you when Microsoft Sentinel finds matching events for your query.

A livestream is always based on a query. Typically, you use the query to narrow down streaming log events, so only the events that are related to your threat-hunting efforts appear. You can use a livestream to:

* Test new queries against live events.
* Generate notifications for threats.
* Launch investigations.

Livestream queries refresh every 30 seconds and generate Azure notifications of any new results from the query.

## Create a livestream

To create a livestream from the **Hunting** page in Microsoft Sentinel, select the **Livestream** tab and then select **New livestream** from the toolbar.

![](https://learn.microsoft.com/en-us/training/wwl-sci/hunt-threats-sentinel/media/5-new-livestream.png)

**Note**

Livestream queries run continuously against your live environment, so you can't use time parameters in a livestream query.

## View a livestream

On the new **Livestream** page, specify a name for the livestream session and the query that provides results for the session. Notifications for livestream events appear in your Azure portal notifications.

## Manage a livestream

You can play the livestream to review results or save the livestream for later reference. Saved livestream sessions can be viewed from the **Livestream** tab on the **Hunting** page. You can also elevate events from a livestream session to an alert by selecting the events and then selecting **Elevate to alert** from the command bar.

You might use a livestream to track baseline activities for Azure resource deletion, and identify other Azure resources that should be tracked. For example, the following query returns any Azure Activity events that recorded a deleted resource:

```kusto
AzureActivity
| where OperationName has 'delete'
| where ActivityStatus == 'Accepted'
| extend AccountCustomEntity = Caller
| extend IPCustomEntity = CallerIpAddress
```

## Use a livestream query to create an analytics rule

If the query returns significant results, you can select **Create analytics rule** from the command bar to create an analytics rule based on the query. After the rule refines the query to identify the specific resources, it can generate alerts or incidents when the resources are deleted.

Choose the best response for the following question.

## Check your knowledge

### 1.
**Which of the following can't be used in a livestream query?**

- **Time parameters**
- Alert data parameters
- Event entities

---

## Відповідь:

**Time parameters** - Параметри часу не можуть використовуватися в livestream запитах, оскільки livestream запити виконуються безперервно проти живого середовища в реальному часі. Це зазначено в тексті: "Livestream queries run continuously against your live environment, so you can't use time parameters in a livestream query."


# 5.6 Exercise - Hunt for threats by using Microsoft Sentinel

As a security engineer working for Contoso, you recently noticed that a significant number of virtual machines (VMs) were deleted from your Azure subscription. You want to simulate a deleted VM, analyze this occurrence, and understand the key elements of the potential threat in Microsoft Sentinel.

In this exercise, you delete a VM, manage threat-hunting queries, and save key findings with bookmarks.

**Note**

To complete this exercise, you need to have completed the setup exercise earlier in the module. If you haven't done that, please do it now.

## Delete a VM

In this task, you delete a VM to test rule detection and incident creation.

1. In the Azure portal, search for and select **Virtual machines**.
2. On the **Virtual machines** page, select the check box beside the virtual machine labeled **simple-vm**, and then select **Delete** from the toolbar.
3. In the **Delete Resources** pane, confirm the deletion and then select **Delete**.

## Manage Microsoft Sentinel threat-hunting queries

In this task, you create and manage threat-hunting queries to review events related to deleting the VM in the previous task. It might take up to 5 minutes for the event to appear in Microsoft Sentinel after you delete the VM.

1. In the Azure portal, search for and select **Microsoft Sentinel**, and then select the previously created Sentinel workspace.

2. On the **Microsoft Sentinel** page, on the menu bar, in the **Threat management** section, select **Hunting**.

3. On the **Hunting** page, select the **Queries** tab. Then choose **New Query**.

4. On the **Create custom query** page, provide the following inputs, and then select **Create**.

   - **Name**: Enter **Deleted VMs**.
   - **Description**: Enter a detailed description that helps other security analysts understand what the rule does.
   - **Custom query**: Enter the following code.

```kusto
AzureActivity
| where OperationName == 'Delete Virtual Machine'
| where ActivityStatus == 'Accepted'
| extend AccountCustomEntity = Caller
| extend IPCustomEntity = CallerIpAddress
```

   - **Tactics**: Select **Impact**.

5. On the **Hunting** page, on the **Queries** tab, enter **Deleted VMs** in the **Search queries** field.

6. In the list of queries, select the star icon beside **Deleted VMs** to mark the query as a favorite.

7. Select the **Deleted VMs** query. In the details pane, select **View Results**.

**Note**

It might take up to 15 minutes for the deleted VM event to be sent to Microsoft Sentinel. You can periodically choose to run the query on the **Results** tab if the VM deletion event doesn't appear.

8. On the **Logs** page, in the **Results** section, select the listed event. It should have **"action": "Microsoft.Compute/virtualMachines/delete"** in the **Authorization** column. This is the event from the Azure Activity log that indicates that the VM was deleted.

9. Remain on this page for the next task.

## Save key findings with bookmarks

In this task, you use bookmarks to save events and do more hunting.

1. On the **Logs** page, in the **Results** section, select the check box beside the listed event. Then select **Add bookmark**.
2. On the **Add bookmark** pane, select **Create**.
3. At the top of the page, select **Microsoft Sentinel** on the breadcrumb trail.
4. On the **Hunting** page, select the **Bookmarks** tab.
5. In the list of bookmarks, select the bookmark that begins with **Deleted VMs**.
6. On the details page, select **Investigate**.
7. On the **Investigation** page, select **Deleted VMs** and observe the details of the incident.
8. On the **Investigation** page, select the entity on the graph that represents a user. This is your user account, which indicates that you deleted the VM.

## Results

In this exercise, you deleted a VM, managed threat-hunting queries, and saved key findings with bookmarks.

## Clean up Azure resources

After you finish using the Azure resources that you created in this exercise, delete them to avoid incurring costs:

1. In the Azure portal, search for **Resource groups**.
2. Select your resource group.
3. In the header bar, select **Delete resource group**.
4. In the **TYPE THE RESOURCE GROUP NAME** field, enter the name of the resource group and select **Delete**.



# 5.7 Summary

As part of the Security Operations Center team, you need to protect Contoso's environment. To accomplish this goal, you first need to detect any threats to the environment.

In this module, you learned how to hunt for threats by using the tools available in Microsoft Sentinel. That activity included proactively identifying threat behaviors by using Microsoft Sentinel queries. You also learned to continue the hunt by using bookmarks and livestream to identify specific account-usage patterns for Contoso's Azure environment.

Now, you can lead your team in using Microsoft Sentinel to help protect Contoso's environment through threat detection.






