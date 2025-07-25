


# Курс "Основи моделювання загроз" (Threat Modeling Fundamentals)

## 📖 Загальний опис курсу

Цей курс від Microsoft Learn присвячений **моделюванню загроз** - систематичному підходу до виявлення, оцінки та пом'якшення потенційних загроз безпеці в системах та додатках.

## 🎯 Що таке моделювання загроз?

**Моделювання загроз** - це структурований процес, який допомагає:
- Виявити потенційні вразливості в системі на етапі проектування
- Зрозуміти, як зловмисники можуть атакувати систему
- Розробити контрзаходи для захисту від загроз
- Покращити загальну безпеку продукту

## 📚 Структура курсу

Курс складається з кількох модулів:

### 1. **Вступ до моделювання загроз**
- Основні концепції та принципи
- Навіщо потрібне моделювання загроз
- Місце в циклі розробки ПЗ

### 2. **Методології моделювання загроз**
- **STRIDE** (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege)
- **PASTA** (Process for Attack Simulation and Threat Analysis)
- **DREAD** (Damage, Reproducibility, Exploitability, Affected Users, Discoverability)

### 3. **Практичний процес**
- Створення діаграм архітектури системи
- Ідентифікація активів та точок входу
- Аналіз потоків даних
- Визначення меж довіри (trust boundaries)

### 4. **Інструменти та техніки**
- Microsoft Threat Modeling Tool
- Діаграми потоків даних (DFD)
- Дерева атак (Attack Trees)
- Матриці ризиків

## 🏆 Навички, які ви отримаєте

### **Технічні навички:**
- Створення моделей загроз для різних типів систем
- Використання STRIDE методології
- Робота з діаграмами архітектури
- Аналіз потоків даних та меж довіри

### **Аналітичні навички:**
- Системне мислення з точки зору безпеки
- Оцінка ризиків та їх пріоритизація
- Розробка стратегій пом'якшення загроз

### **Практичні навички:**
- Інтеграція моделювання загроз у процес розробки
- Співпрацю з командами розробників
- Документування результатів аналізу

## 👥 Для кого цей курс?

### **Основна аудиторія:**
- **Security Engineers** та архітектори безпеки
- **Software Architects** та системні аналітики
- **DevSecOps Engineers**
- **Product Security** спеціалісти

### **Додаткова аудиторія:**
- Розробники, які хочуть покращити безпеку свого коду
- IT-менеджери, відповідальні за безпеку продуктів
- Консультанти з кібербезпеки

## 🛠️ Практичні застосування

### **В розробці ПЗ:**
- Безпечне проектування архітектури
- Раннє виявлення вразливостей
- Зменшення витрат на виправлення помилок безпеки

### **В корпоративному середовищі:**
- Аналіз безпеки існуючих систем
- Планування модернізації з урахуванням безпеки
- Відповідність регуляторним вимогам

### **В хмарних рішеннях:**
- Безпека мікросервісів
- Захист API та інтеграцій
- Моделювання загроз для Azure/AWS/GCP

## 📈 Кар'єрні можливості

Після завершення курсу ви зможете працювати на позиціях:
- **Threat Modeling Specialist**
- **Security Architect**
- **Application Security Engineer**
- **Product Security Manager**
- **Cybersecurity Consultant**

## 🎓 Сертифікація та визнання

- Курс є частиною Microsoft Learn платформи
- Дає фундаментальні знання для подальшої сертифікації з безпеки
- Визнається в індустрії як якісна освітня програма

## 💡 Чому варто пройти цей курс?

### **Актуальність:**
- Моделювання загроз стає обов'язковою практикою у великих компаніях
- Регуляторні вимоги все частіше вимагають формального аналізу безпеки
- "Security by Design" - це тренд сучасної розробки

### **Практичність:**
- Навички можна застосувати відразу в поточній роботі
- Курс базується на реальних кейсах та прикладах
- Інструменти та методології активно використовуються в індустрії

### **Кар'єрний розвиток:**
- Високий попит на спеціалістів з моделювання загроз
- Можливість працювати в провідних IT-компаніях
- Гарна база для подальшого розвитку в кібербезпеці

## 🚀 Рекомендації для успішного проходження

1. **Підготовка:** Базові знання архітектури ПЗ та принципів безпеки
2. **Практика:** Обов'язково виконуйте всі практичні завдання
3. **Застосування:** Спробуйте застосувати знання до реального проекту
4. **Спільнота:** Приєднуйтесь до професійних груп з моделювання загроз

Цей курс дасть вам міцну основу для роботи в сфері безпеки та допоможе розвинути системне мислення щодо захисту інформаційних систем.



--------------------------------------------------------------------------------------------


# Threat Modeling Security Fundamentals

https://learn.microsoft.com/en-us/training/paths/tm-threat-modeling-fundamentals/


This learning path takes you through the four main phases of threat modeling, explains the differences between each data-flow diagram element, walks you through the threat modeling framework, recommends different tools and gives you a step-by-step guide on creating proper data-flow diagrams.

#### Prerequisites
- None

# 1. Introduction to threat modeling

Threat modeling is an effective way to help secure your systems, applications, networks, and services. It's an engineering technique that identifies potential threats and offers recommendations to help reduce risk and meet security objectives earlier in the development lifecycle.

# Learning objectives
In this module, you will:
- Understand the importance of capturing requirements and assumptions when creating a data-flow diagram.
- Read about the framework that helps you find security issues in a system.
- Learn about the security control categories that help you reduce or eliminate potential threats.
- Highlight the importance of verifying assumptions, requirements, and fixes before deployment.


# 1.1 Introduction

Threat modeling is an effective technique to help secure your systems, applications, networks, and services. It helps you identify potential threats and risk reduction strategies earlier in the development lifecycle.

Threat modeling uses a data-flow diagram that graphically shows how the system works. It then applies a framework to help you find and fix security issues.

Systems released without first being threat modeled place your customers and organization at risk.

> **Note**  
> To make things easier, this learning path refer to systems, applications, and services as just *systems*.

## When to use threat modeling

Use threat modeling whenever you design new systems or update existing ones. Examples include:

* Creating a new Azure micro-service that reports on your organization's cloud resource usage for budgeting purposes.
* Designing a public API to provide customers access to your data.
* Adding a new feature to an existing application.

## Who can threat model

Anyone with a working knowledge of the system and a basic understanding of security can work with threat modeling. This technique can be applied across any:

* Software delivery approach, for example, Agile or Waterfall.
* Deployment cadence, such as hourly, monthly, or annually.

## Learning objectives

In this module, you explore the four high-level steps of threat modeling so that you can:

* Understand the importance of capturing requirements and assumptions when creating a data-flow diagram.
* Read about the framework that helps you find security issues in a system.
* Learn about the security-control categories that help you reduce or eliminate potential threats.
* Highlight the importance of verifying assumptions, requirements, and fixes before deployment.

## Prerequisites
* None




# 1.2 Threat Modeling Phases

Threat modeling is a technique used by anyone who knows how their system works and has a working knowledge of information security.

The technique is broken down into four different phases. Each phase contains important steps to help you create a data-flow diagram and analyze it for potential threats.


![](https://learn.microsoft.com/en-us/training/modules/tm-introduction-to-threat-modeling/media/threat-modeling-steps.png)

| Phase | Title | Description |
|-------|--------|-------------|
| 1 | Design | Capture all requirements for your system and create a data-flow diagram. |
| 2 | Break | Apply a threat-modeling framework to the data-flow diagram and find potential security issues. |
| 3 | Fix | Decide how to approach each issue with the right combination of security controls. |
| 4 | Verify | Verify requirements are met, issues are found, and security controls are implemented. |

This module discusses each phase in the next units.

> **Important**
> 
> The units in this module introduce important threat-modeling concepts at a high level. The Threat Modeling Fundamentals learning path discusses the concepts in detail.




# 1.3 Step 1 - Design


The design phase is the starting ground for your threat modeling activities. Gather as much data as possible about what you're building and what you're using to build it.

## Goals

- Develop a clear picture of how your system works
- List every service consumed by your system
- Enumerate all the assumptions about the environment and default security configurations
- Create a data-flow diagram that uses the right context depth level

> **Important**
> 
> If you don't complete this phase, you might overlook important security-design considerations for your system, which can put your customers at risk.

## Ask questions about your system

Ask as many questions as possible about your system. Here are a few questions to consider:

| Area | Questions |
|------|-----------|
| **System description** | What does the system do? What are the business processes handled by the service? Are they clearly defined? |
| **System environment** | Will the system be built on the cloud or on-premises? On which operating system is it built? Does it use containers? Is the system an application, service, or something entirely different? |
| **Scenarios** | How will the system be used? How will it not be used? |
| **Permissions** | Does the system have script-execution, data, or hardware-access requirements? If so, what are they? |
| **Cloud provider** | Which cloud provider does the system use? What default security configuration options does the provider offer? How do these options affect the system security requirements? |
| **Operating system** | Which Operating System will the system use? What default security configuration options does the operating system offer? How do these options affect the system security requirements? |
| **First- and third-party** | Which first- and third-party services will the system use? What default security configuration options do they offer? How do these options affect the system security requirements? |
| **Accounts** | What are the account types that the system uses, like users and administrators? Are these accounts be local or cloud-enabled? What access do they need and why? |
| **Identity & access control** | How does the system help secure those accounts? Does it rely on Microsoft Entra ID? Does it use features like Access Control Lists (ACL), multifactor authentication (MFA), and Session control? |
| **Tokens & sessions** | Will the system process requests like SOAP or REST APIs? How does it handle different sessions? |
| **Bypass** | Will the system use or require back doors? If so, how does that bypass work? |
| **Logging, monitoring and backing up** | What are the mechanisms the system uses to log security events, monitor for anomalies, and back up system data? Which event types does capture? |
| **Network** | What are all the intrusion, detection, and protection systems that will be used? How is communication encrypted? |
| **Data** | What type of data will the system create or handle? What will the data classification type be? How does the system trust data sources? How does it parse data? What are the expected input and output behaviors? How is validation handled? How is data encrypted across all states? |
| **Secrets management** | How does the system handle keys, certificates, and credentials? |

> **Important**
> 
> This list is extensive, but not exhaustive. Speak with your colleagues and security team to capture all relevant context for the system.

> **Note**
> 
> If you have a dedicated security team, schedule a whiteboarding session with them to go over the initial design. This contact can save you a considerable amount of time.

## Create a data-flow diagram

Use the answers to create a data-flow diagram. Your diagram shows data across each stage in the data lifecycle, and includes changes in trust zones. Examples include:

- Human users sign into your web application hosted in Azure to access data
- Administrators change default security configurations for elastic resources used by the web application
- Automated daily scripts monitor activity logs for the web application and notify administrators of any anomalies

Microsoft engineering teams submit data-flow diagrams as part of their security-compliance requirements. These diagrams make it easier to conduct security conversations.

### Diagraming tools

Microsoft engineers recommend using one of two tools available today:

- Threat Modeling Tool
- Visio

### Diagram elements

A data-flow diagram shows the flow of data in a given system. It usually starts with requests from users or data stores and ends with data stores or Analytics Services. The data-flow diagram uses distinct shapes to indicate the elements they represent.

| Element | Shape | Definition |
|---------|--------|------------|
| **Process** | ![Process shape: circle](https://learn.microsoft.com/en-us/training/modules/tm-introduction-to-threat-modeling/media/process50.png) | Task that receives, modifies, or redirects input to output, like a web service. |
| **Data store** | ![Data store shape: two parallel horizontal lines](https://learn.microsoft.com/en-us/training/modules/tm-introduction-to-threat-modeling/media/data-store50.png) | Permanent and temporary data storage, like a web cache and Azure-managed databases. |
| **External entity** | ![External entity shape: square](https://learn.microsoft.com/en-us/training/modules/tm-introduction-to-threat-modeling/media/external-entity50.png) | Task, entity, or data store outside of your direct control, like users and third-party APIs. |
| **Data-flow** | ![Data-flow shape: two parallel diagonal arrows](https://learn.microsoft.com/en-us/training/modules/tm-introduction-to-threat-modeling/media/data-flow50.png) | Data movement between processes, data stores, and external entities, like connection strings and payloads. |
| **Trust boundary** | ![Trust boundary: dashed square/line](https://learn.microsoft.com/en-us/training/modules/tm-introduction-to-threat-modeling/media/trust-boundary-box50.png) | Trust-zone changes as data flows through the system, like users using the internet to access a secured corporate network. |

Data-flow diagram elements also need context to help anyone understand how they're used and secured in the system.

### Information to include in the data-flow diagram

The amount of information to include in the data-flow diagram depends on a few key factors:

| Factor | Explanation |
|--------|-------------|
| **Type of system you're building** | Systems that don't handle sensitive data or are used only internally might not need as much context as an externally facing system |
| **Required context from your security team** | Security teams are precise with what they look for in threat models. Speak with your security team to confirm the required depth layer |

Failure to include the right context leads to incomplete security reviews and potentially vulnerable systems.

### Diagram layers

To help you understand how much information to include, choose between these four context depth layers:

| Depth layer | Title | Description |
|-------------|-------|-------------|
| **0** | **System** | Starting point for any system. Data-flow diagram contains major system parts with enough context to help you understand how they work and interact with each other. |
| **1** | **Process** | Focus on data-flow diagrams for each part of the system by using other data-flow diagrams. Use this layer for every system, especially if it handles sensitive data. The context at this layer helps you identify threats and ways to reduce or eliminate risks more efficiently. |
| **2** | **Subprocess** | Focus on data-flow diagrams for each subpart of a system part. Used for systems considered critical. Examples include systems for secured environments, systems that handle highly sensitive data, or systems that contain a high risk rating. |
| **3** | **Lower-Level** | Focus on highly critical and kernel-level systems. Data-flow diagrams describe each subprocess in minute detail. |

> **Note**
> 
> Most data-flow diagrams should contain both Layers 0 and 1 depth layers. Speak with your security team to confirm the required layer depth.

---

## Check your knowledge

**1. What happens at the Design Phase?**

**Correct Answer:** You know how the system works or will work. You can also identify security requirements, guarantees, or gaps inherited from cloud providers and integrated services.

**Explanation:** The Design Phase is about gathering comprehensive information about your system - understanding how it works, what services it uses, what assumptions you're making about the environment, and creating a detailed data-flow diagram. This includes identifying security requirements, guarantees, and gaps that come from cloud providers and integrated services. The other options are incorrect because:

- Option 2 is wrong - you DO need to research security guarantees, assumptions, and gaps during the Design phase
- Option 3 is wrong - identifying and resolving security issues happens in later phases (Break and Fix), not during Design



# 1.4 Step 2 - Break


The break phase is where you use the data-flow diagram to find potential threats against your system. The process uses a threat-modeling framework to help you find the most common threats and ways to protect against them.

## Goals

- Choose between *protecting the system* and *understanding the attacker* focused approaches
- Use the STRIDE framework to identify common threats

> **Important**
> 
> If you don't complete this phase, you won't find potential threats in your system, which can lead to future breaches.

## Focus your approach

Start by choosing whether you want to find ways to protect your system, or you want to understand all you can about an attacker and their motives. Examples include:

| Focus | Example of what you can find |
|-------|------------------------------|
| **System** | You find an issue with an unencrypted connection between the user and the system. |
| **Attacker** | You find out more about means, motivation, and ways to harden the system entry points. |
| **Asset** | You identify critical assets based on things like classified data handling, and focus mostly on protecting those assets. |

> **Note**
> 
> Microsoft product engineers mostly focus on protecting the system. Penetration testing teams focus on both.

## Select a threat framework

Next, select a framework to help generate potential threats in your system. Microsoft traditionally uses STRIDE, an acronym for the six main threat categories to provide an extensive—but not exhaustive—list of threats.

The framework helps you ask a few important questions about your system:

| Threat | Definition | Question | Threat example |
|--------|------------|----------|----------------|
| **Spoofing** | Attacker pretends to be someone or something else | Are both sides of the communication authenticated? | Sending an email to users from an account that seems legitimate with malicious links and attachments to capture their credentials, data, and device access |
| **Tampering** | Attacker changes data without authorization | How do I know someone can't change data in transit, in use, or at rest? | Modifying memory through weak API call handling to cause crashes and disclosure of sensitive error messages |
| **Repudiation** | Attacker claims to not have done something | Can every action be tied to an identity? | Claiming to not have deleted database records |
| **Information Disclosure** | Attacker sees data they aren't supposed to see | How do I know someone can't see data in transit, in use, or at rest? | Accessing unauthorized documents and folders with weak security controls |
| **Denial of Service** | Attacker brings your system down | Are there areas in the system where resource is limited? | Flooding the network with requests |
| **Elevation of Privilege** | Attacker has unauthorized access to data | How do I know someone is allowed to take this action? | Extracting data by exploiting weaknesses in input-handling logic or memory |

---

## Check your knowledge

**1. What happens at the Break Phase?**

**Correct Answer:** You select a focus area with an associated framework to systematically identify potential threats in your system.

**Explanation:** The Break Phase is specifically about identifying potential threats in your system using a systematic approach. You choose a focus area (system, attacker, or asset-focused) and then apply a threat modeling framework like STRIDE to systematically find potential threats. The other options are incorrect because:

- Option 2 is wrong - the Break phase is about identifying threats, not solutions (solutions come in the Fix phase)
- Option 3 is wrong - while meeting with the security team can be helpful, it's not a requirement of the Break phase itself




# 1.5 Step 3 - Fix

The fix phase is where the fate of all threats is decided. Each STRIDE threat maps to one or more security controls, which offer different functions and types to choose from.

## Goals
- Measure each threat against a prioritization framework or security bug bar
- Track each threat as a task or work item in a bug-management service
- Generate security control recommendations that are mapped to STRIDE threats
- Address each threat by selecting one or more security control types and functions
- Resolve tasks

> **Important**
> 
> If you don't complete this phase, you won't find the security controls to help reduce risk or track each threat properly.

## Set up a threat tracking workflow
Set up a threat tracking workflow that prioritizes threats and creates tasks to address them.

### Prioritize threats
Start by measuring each threat against a prioritization framework or security bug bar. This process helps you arrange resources to fix issues deemed most important to your organization.

The process uses three key variables:

| Variable | Description |
|----------|-------------|
| Impact | Uses STRIDE categories to assign impact |
| Severity | Uses internal bug bar or prioritization framework to assign severity using worst-case scenarios |
| Risk | Uses a calculation of security control effectiveness and implementation cost |

> **Tip**
> 
> Microsoft engineers use an internal security bug bar that assigns threats with a Critical, Important, Moderate, Low, or Information severity rating. Check with your security team to confirm how to prioritize your issues.

### Create tasks
Next, add each threat in a bug-management solution like Azure DevOps Services. Some of the benefits include:

- Reinforces issue ownership
- Effectively tracks history
- Gives you the ability to use standardized templates for priority and resolution exercises

## Rate security control effectiveness and cost
Visit each security control recommendation mapped to STRIDE threats. Write down the ones that are most effective and least expensive to implement. Here are a few examples:

| Threat | Security Control | Security Control Example |
|--------|------------------|--------------------------|
| Spoofing | Authentication | Ensure message integrity and authenticate origin by sending and receiving messages signed with digital signatures |
| Tampering | Integrity | Validate input to prevent the processing of malicious payloads and mishandling of unexpected behavior |
| Repudiation | Nonrepudiation | Create and protect security logs that contain user actions and timestamps |
| Information disclosure | Confidentiality | Apply access control lists to ensure the right users can access the right data |
| Denial of service | Availability | Use elastic resources to manage the growing or shrinking usage |
| Elevation of privilege | Authorization | Run the service using the least possible amount of access |

> **Tip**
> 
> You might come across security controls that reduce or completely eliminate multiple threats at once. As an example, using SSL/TLS creates secure transmission channels to help prevent malicious data modification or disclosure.

## Security control types and functions
Security controls have different types and functions. When combined, they help secure your system and create multiple layers of security, also known as defense-in-depth.

You can choose one or more security control types:

- **Physical**, like cameras
- **Technical**, like encryption
- **Administrative**, like policies

These types have one or more security control functions:

| Function | Description |
|----------|-------------|
| Preventive | Reduces the probability or impact of a threat, like firewalls |
| Detective | Identifies attacks as they happen, like surveillance |
| Corrective | Controls how the system responds to an ongoing attack, like system patches |
| Recovery | Recovers system from an attack, like backups |
| Deterrent | Keeps attackers away from the system, like least privilege |

## Add security control details to each issue
Add the details to each issue in the bug management solution, then resolve each issue with one of the following resolutions. They vary slightly from organization to organization:

| Resolution | Description |
|------------|-------------|
| Reduce | Use bug fixes or redesign to reduce or eliminate threat impact and severity |
| Transfer | Assign issue to another system or team |
| Avoid | Cut the part of the system that contains the issue |
| Accept | Risk is accepted without a resolution. This resolution requires approval of an authorized risk decision maker. The decision might be based on threat severity. Critical severity threats might require approval from senior leadership, while a defense-in-depth risk might require approval by a senior engineer. Speak with your team for strategic guidance |

---

## Check your knowledge

**Question:** What happens at the Fix Phase?

**Варіанти відповідей:**
1. It's when all fixes are verified before the system is deployed.
2. It's when you generate, validate, and prioritize a list of security controls to reduce or eliminate risk.
3. It's when a framework is selected to help generate potential threats.

**Правильна відповідь:** **Варіант 2** - It's when you generate, validate, and prioritize a list of security controls to reduce or eliminate risk.

**Пояснення:** На етапі Fix основна мета - це створення, валідація та пріоритизація списку засобів безпеки (security controls) для зменшення або усунення ризиків. Це включає оцінку загроз, створення завдань для їх вирішення, вибір відповідних типів та функцій засобів безпеки, а також вирішення кожної загрози через один із запропонованих методів (зменшення, передача, уникнення або прийняття ризику).



# 1.6 Step 4 - Verify

The verify phase is the last step of the threat-modeling process, which often happens before the system is deployed. It involves ensuring requirements are met, assumptions are validated, and security controls are in place.

## Goals
- Confirm that the system satisfies all previous and new security requirements
- Configure cloud provider, operating system, and components to meet security requirements
- Ensure that all issues are addressed with the right security controls
- Take the system through manual and automated verification before deployment

> **Important**
> 
> If you don't complete this phase, you won't be able to verify the security work was successfully completed.

## Verify requirements and set defaults

Start by verifying that all requirements created in the first phase are met.

**Examples:**
- Network security plans
- Secrets-management solution implementation
- Logging and monitoring systems
- Identity and access controls

Then make sure to change all the default configuration settings from the cloud provider, operating system, and components so you can meet all security requirements.

**Examples:**
- Enable Azure SQL Database transparent data encryption to protect data on disk
- Use role-based access control to assign permissions to users, groups, and applications
- Enable Windows Firewall across all profiles

You should resolve all issues logged in the bug-management solution. Verify all fixes.

## Run verification

The last part involves running both manual and automated verification. At Microsoft, systems are subject to a verification process before deployment. The process might include automated scanners, code reviews, and penetration tests. The process can be enforced before each deployment or across time intervals, like every **6-12 months**.

If you answer **yes** to any of the following questions, you might want to have shorter verification cadences:

- Is my system used externally?
- Does my system handle confidential data?
- Do I have to comply with regulations?
- Does my organization require extra security processes such as privacy implications, operational risk, or development requirements?

---

## Check your knowledge

**Question:** What happens at the Verify Phase?

**Варіанти відповідей:**
1. You implement the list of applicable security controls that reduces or eliminates risk.
2. Code is reviewed manually before being pushed to the staging branch for deployment.
3. System is verified manually or automatically against previously generated threats to verify security controls reduced or eliminated risk.

**Правильна відповідь:** **Варіант 3** - System is verified manually or automatically against previously generated threats to verify security controls reduced or eliminated risk.

**Пояснення:** На етапі Verify основна мета - це перевірка системи (як ручна, так і автоматична) відповідно до раніше ідентифікованих загроз, щоб переконатися, що впроваджені засоби безпеки дійсно зменшили або усунули ризики. Це заключний етап процесу моделювання загроз, який включає:

- Підтвердження виконання всіх вимог безпеки
- Налаштування системних компонентів згідно з вимогами
- Запуск процесів верифікації (сканери, code review, penetration testing)
- Перевірку ефективності впроваджених security controls

Етап Verify відрізняється від етапу Fix тим, що тут ми не впроваджуємо нові засоби захисту, а перевіряємо ефективність уже впроваджених.


# 1.7 Summary

Threat modeling is an effective way to help secure your systems, applications, networks, and services. It identifies potential threats and recommends risk-reduction strategies to help you meet security goals early in the development lifecycle.

In this module, you:
- Understood the importance of capturing requirements and assumptions to help create a data-flow diagram
- Read about the framework that helps you find security issues in a system
- Learned about the security control categories that help you reduce or eliminate potential threats
- Highlighted the importance of verifying assumptions, requirements, and fixes before deployment

## What's next

In the next few modules of this learning path, you learn about each concept introduced in the four phases in detail:

| Module | Title | Description |
|--------|-------|-------------|
| 2 | Create a threat model using data-flow diagram elements | Learn about each element in a data-flow diagram, including when to use them and what context to include |
| 3 | Provide context with the right depth layer | Learn the differences between each context-depth layer and when to use them before you create a data-flow diagram |
| 4 | Approach your data-flow diagram with the right threat model focus | Learn about the different ways to focus your threat-modeling activities |
| 5 | Use a framework to identify threats and find ways to reduce or eliminate risk | Deep-dive into STRIDE and learn more about what's at risk and how to protect your system |
| 6 | Prioritize your issues and apply security controls | Learn to prioritize threats and understand the different types and functions of security controls for your system |
| 7 | Use recommended tools to create a data-flow diagram | Check out some of the tools you can use for threat modeling |

## Learn more
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/en-us/securityengineering/sdl/)




# 2 Create a threat model using data-flow diagram elements

Data-flow diagrams are graphical representations of your system and should specify each element, their interactions, and helpful context.

# 2.1 Introduction

Data-flow diagrams are made up of elements represented as shapes and lines. They graphically represent every major part of your system.

Examples include:
* An Azure DB used to store customer data.
* A web service that handles a user request.
* A user interacting with your system.
* Data flow crossing a trust-zone level change.

We use elements and their interactions in threat modeling to help identify threats and reduce system risk. The process helps engineers collaborate more efficiently while securing their systems against the most common threats.

In this module, you explore each element of a data-flow diagram. These elements have distinct shapes and functions and require specific context.

> **Note**
> 
> We might also refer to elements as *Stencils* throughout this learning path.

## When to use elements

Use elements whenever you create a data-flow diagram. The diagram shows how data is created, manipulated, stored, and removed from your system. Let's build on the examples from the first module:

* **Azure micro-service**: Add elements to specify users, authentication processes, data storage, data-request processes, and response-handling processes.
  * Don't forget to specify trust-zone level changes.
* **Public API**: Add elements to specify users, data storage, logging and monitoring processes, and other parts of the system.
* **New feature on existing application**: Add elements to represent existing and new parts of the system.

## Learning objectives

In this module, you learn how to:
* Distinguish between the shape and function of each element.
* Include the right context for an element when creating a data-flow diagram.

## Prerequisites

* None


# 2.2 Data-flow diagram elements

Data-flow diagrams are made up of shapes that create graphical representations of your system. Each shape represents a unique function. Each interaction is analyzed to help you identify potential threats and ways to reduce risk.

Using shapes correctly helps you receive better input from colleagues and security teams. They allow everyone to understand how the system works. It can also help everyone avoid going through countless design documents and development plans to get them up and running.

> **Note**
> 
> If you fail to properly account for all the parts of a system in the data-flow diagram, you'll risk deploying the system with potential vulnerabilities.

| Element | Shape | Definition | Example |
|---------|-------|------------|---------|
| Process | ![](https://learn.microsoft.com/en-us/training/modules/tm-create-a-threat-model-using-foundational-data-flow-diagram-elements/media/process50.png) | Task that receives, modifies, or redirects input to output | Web service |
| Data store | ![](https://learn.microsoft.com/en-us/training/modules/tm-create-a-threat-model-using-foundational-data-flow-diagram-elements/media/data-store50.png) | Permanent and temporary data storage | Web cache and Azure DB |
| External entity |![](https://learn.microsoft.com/en-us/training/modules/tm-create-a-threat-model-using-foundational-data-flow-diagram-elements/media/external-entity50.png) | Task, entity, or data store outside of your direct control | Users and third-party APIs |
| Data-flow | ![](https://learn.microsoft.com/en-us/training/modules/tm-create-a-threat-model-using-foundational-data-flow-diagram-elements/media/data-flow50.png) | Data movement between processes, data stores, and external entities | Connection strings and payloads |
| Trust boundary | ![](https://learn.microsoft.com/en-us/training/modules/tm-create-a-threat-model-using-foundational-data-flow-diagram-elements/media/trust-boundary-box50.png) | Trust zone changes as data flows through the system | Users connecting to a secured corporate network over the internet |

In the next few units, we discuss each of the elements.


# 2.3 Process - The task element

![](https://learn.microsoft.com/en-us/training/modules/tm-create-a-threat-model-using-foundational-data-flow-diagram-elements/media/process.png)

The **process element** is depicted as a circle. It represents activities that can modify or redirect received input to their proper outputs.

Examples include:
* A microservice that receives an API call request and forwards it to an API handling service.
* Code that validates data input before it writes to a data store.

## When to use the process element

Add a process element between:
* **Data stores**: Processes handle all communication between data stores.
* **External entities with other elements**: Processes handle all tasks and communication.
* **Processes**: Processes handle all tasks.

Depending on the information-depth level required for a data-flow diagram, you may use the process element to represent a few distinct use cases:

| Use case | Description |
|----------|-------------|
| Stubs | Using the process element as a "stub" on a higher-level data-flow diagram is a good way to help keep things clean. It involves creating a separate data-flow diagram for a specific process and mapping it back to the higher-level diagram. It works like a "zoom-in" feature, where the in-depth data-flow diagram is available when you "zoom-in" on that process. |
| Multiple tasks | This use case applies when a process handles more than one task. This context is important because it allows anyone looking at the data-flow diagram to apply the proper security controls for each task. |

## Include context

Include the following context with each process element:

| Context | Questions |
|---------|-----------|
| Code | Is this process running in C#, C++, Objective C, Java, or a scripting language? |
| Permission level | Does this process need kernel, local, or administration-level permissions to run? |
| Service isolation | Is the process running in a sandbox? |
| Input | Can this process accept input from everyone, local accounts, or just administrators? |
| Validation | How does the process parse, handle, and accept input? |
| Authentication | Does the process rely on Microsoft Entra ID for authentication? If not, on what does it rely? |
| Authorization | Does it rely on Access Control Lists (ACL) for authorization? If not, on what does it rely? |

## Check your knowledge

**1.**
**Which one of these actions best describes a process?**

A. A web portal asks a user for their credentials.  
B. A cache stores service-related cookies for a user.  
C. A third-party API sends requested data to its requestor.

**Відповідь на запитання:**

**Правильна відповідь: A. A web portal asks a user for their credentials.**

**Пояснення:**

- **A. A web portal asks a user for their credentials** - це **процес**, оскільки веб-портал активно обробляє дії (запитує дані, валідує їх, перенаправляє). Це відповідає визначенню процесу як активності, що модифікує або перенаправляє вхідні дані на вихідні.

- **B. A cache stores service-related cookies** - це **сховище даних** (data store), оскільки кеш пасивно зберігає інформацію.

- **C. A third-party API sends requested data** - це **зовнішня сутність** (external entity), оскільки API третьої сторони знаходиться поза вашим прямим контролем.

**Ключ до розуміння:** Процес завжди виконує активні дії - обробляє, валідує, трансформує, або перенаправляє дані між іншими елементами системи.



# 2.4 Data store - The storage element

![](https://learn.microsoft.com/en-us/training/modules/tm-create-a-threat-model-using-foundational-data-flow-diagram-elements/media/data-store.png)

The **data store element** is depicted as parallel lines. This element represents data stored on a temporary or permanent basis.

Examples include:
* Using the browser cache to store user session-related data.
* Adding a security log event to a database.

## When to use the data store element

* Whenever you're storing data somewhere, like Azure DB or a local cache.
* If you're establishing communication between two data stores, don't forget to add a process between them.
* Data stores and external entities start the data flow, so verify you have either one in place.
* Make sure to include any post-processing of data, such as analytics services like Azure Analytics. This process is often missed.

## Include context

Include the following context with each data store element:

| Context | Questions |
|---------|-----------|
| Type | Does the system use Azure SQL, cookies, local, or some other type of storage? If so, what is it? |
| Function | How is the storage used? Is it used to share data, store backups, security logs, credentials, or secrets? |
| Permission level | How is access control implemented? Who has read and write permissions? |
| Additional controls | Is data encrypted? What about the disk? Are digital signatures used? |

## Check your knowledge

**1.**
**Which one of these actions best describes a data store?**

A. A web portal asks a user for their credentials.  
B. A cache stores service-related cookies for a user.  
C. A third-party API sends requested data to its requestor.


**Відповідь на запитання:**

**Правильна відповідь: B. A cache stores service-related cookies for a user.**

**Пояснення:**

- **A. A web portal asks a user for their credentials** - це **процес** (process), оскільки веб-портал активно виконує дію запиту та обробки даних.

- **B. A cache stores service-related cookies for a user** - це **сховище даних** (data store), оскільки кеш пасивно зберігає дані (cookies) на тимчасовій або постійній основі. Це точно відповідає визначенню data store як елемента, що представляє збережені дані.

- **C. A third-party API sends requested data to its requestor** - це **зовнішня сутність** (external entity), оскільки API третьої сторони знаходиться поза вашим прямим контролем.

**Ключ до розуміння:** Data store завжди пасивно зберігає дані (тимчасово або постійно), не виконуючи активних дій з їх обробки. У цьому випадку кеш саме зберігає cookies користувача.



# 2.5 External entity - The no control element

![](https://learn.microsoft.com/en-us/training/modules/tm-create-a-threat-model-using-foundational-data-flow-diagram-elements/media/external-entity.png)

The **external entity element** is depicted as a square. The external entity can be a process, data store, or even a full-fledged system outside of your direct control.

Examples include:
* A user interacting with your service.
* Tight integration with a third-party authentication service.
* Services created by other teams within your organization.

## When to use the external entity element

* When representing an entity that you can't directly modify.
* Data stores and external entities start the data flow, so verify you have either one in place.

## Include context

Include the following context with each external entity element:

| Context | Questions |
|---------|-----------|
| Source | Is the entity internal or external? |
| Type | Is the entity human, a service provider, or web service? |
| Authentication | Does the process rely on Microsoft Entra ID for authentication? If not, on what does it rely? |
| Authorization | Does it rely on Access Control Lists (ACL) for authorization? If not, on what does it rely? |

## Check your knowledge

**1.**
**Which one of these actions best describes an external entity?**

A. A web portal asks a user for their credentials.  
B. A cache stores service-related cookies for a user.  
C. A third-party API sends requested data to its requestor.

**Відповідь на запитання:**

**Правильна відповідь: C. A third-party API sends requested data to its requestor.**

**Пояснення:**

- **A. A web portal asks a user for their credentials** - це **процес** (process), оскільки веб-портал активно обробляє дані та виконує дії всередині вашої системи.

- **B. A cache stores service-related cookies for a user** - це **сховище даних** (data store), оскільки кеш пасивно зберігає дані.

- **C. A third-party API sends requested data to its requestor** - це **зовнішня сутність** (external entity), оскільки API третьої сторони знаходиться поза вашим прямим контролем. Ви не можете модифікувати його код, логіку роботи, або безпосередньо керувати ним.

**Ключ до розуміння:** External entity завжди представляє сутність (людину, сервіс, систему), яку ви **не можете безпосередньо контролювати або модифікувати**. API третьої сторони є класичним прикладом такої сутності - ви можете з нею взаємодіяти, але не можете змінювати її внутрішню логіку роботи.


# 2.6 Data-flow - The data in transit element

![](https://learn.microsoft.com/en-us/training/modules/tm-create-a-threat-model-using-foundational-data-flow-diagram-elements/media/data-flow.png)

The **data-flow element** is depicted as directional arrows. This element represents data movement between elements. The directional arrows indicate communication between the data source and destination.

Examples include:
* Credentials submitted by a user to access your service.
* A request from a process to add an entry to your data store.

## When to use the data-flow element

* Between each element interaction.
* To call out the data type being transmitted, and include how you're transmitting it.
* In most cases, include responses to each request.

## Include context

Include the following context with each data-flow element:

| Context | Questions |
|---------|-----------|
| Description | Is the data flow passing a session token, SQL string, or user credentials? If not, what's it passing? |
| Protocol | Does the flow use HTTPS or SOAP? If not, what does it use? |
| Flow sequence | Is the data flow enumerated to make it easier to follow the flow sequence? |
| Type | What type of data is in the data flow? Cookies? XML? SOAP payload? REST payload? JSON payload? |
| Additional controls | Does the data flow have forgery protection enabled? Other security flags enabled? |
| Authentication | Does the process rely on Microsoft Entra ID for authentication? If not, on what does it rely? |
| Authorization | Does it rely on Access Control Lists (ACL) for authorization? If not, on what does it rely? |

## Check your knowledge

**1.**
**Which one of these actions best describes a data-flow?**

User credentials being transmitted from a process to an authentication service provider.  
Session tokens being stored for later use.  
A third-party API handling service analyzing a request.




# 2.7 Trust boundary - The trust zone change element

Trust boundary box

![](https://learn.microsoft.com/en-us/training/modules/tm-create-a-threat-model-using-foundational-data-flow-diagram-elements/media/trust-boundary-box.png)

Trust boundary line

![](https://learn.microsoft.com/en-us/training/modules/tm-create-a-threat-model-using-foundational-data-flow-diagram-elements/media/trust-boundary-line.png)

The **trust boundary element** is represented by dotted lines or squares. Trust boundaries are used to describe data flow as it crosses different trust zone levels.

Examples include:
* Firewalls
* Connections to third-party services
* Parts of your system only available to administrators

Areas with changing trust zones are the most targeted by attackers and should be carefully designed.

Microsoft has predefined trust-zone requirements for engineers to use internally. It takes the guesswork out of which boundaries to apply. If you work at Microsoft, contact your security team to learn more.

## When to use the trust boundary element

Here are a few important points to remember about trust boundaries:
* Include trust boundaries to handle data flow as it crosses different trust zones.
* Trust boundary **lines** represent data flow as it crosses large environments, like the internet.
* Trust boundary **boxes** represent smaller environments, like sandbox environments and corporate networks.

## Include context

Include the following context with each trust boundary element:

| Context | Questions |
|---------|-----------|
| Description | Is it a corporate network boundary? Internet? Azure subscription? |

## Check your knowledge

**1.**
**Which one of these actions best describes data crossing a trust boundary?**

Data sent from the user to a web service hosted on Azure.  
Data sent from the web service to the data store on Azure under the same Azure subscription.  
Data sent from the data store to a process on Azure under the same tenant.


# 3.8 Summary

Data-flow diagrams are graphical representations of your system and should contain each applicable process, data-store, external entity, data-flow, and trust boundary.

In this module, you:
* Distinguished between the shape and function of each element.
* Learned about the right context for an element when creating a data-flow diagram.

## Get started with Azure

Choose the Azure account that's right for you. Pay as you go or try Azure free for up to 30 days. Sign up.

