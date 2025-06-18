
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
