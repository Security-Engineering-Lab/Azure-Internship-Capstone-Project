


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




# Step 1 - Design

**200 XP**  
*6 minutes*

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
| **Process** | ![Process shape: circle](circle) | Task that receives, modifies, or redirects input to output, like a web service. |
| **Data store** | ![Data store shape: two parallel horizontal lines](parallel-lines) | Permanent and temporary data storage, like a web cache and Azure-managed databases. |
| **External entity** | ![External entity shape: square](square) | Task, entity, or data store outside of your direct control, like users and third-party APIs. |
| **Data-flow** | ![Data-flow shape: two parallel diagonal arrows](arrows) | Data movement between processes, data stores, and external entities, like connection strings and payloads. |
| **Trust boundary** | ![Trust boundary: dashed square/line](dashed-line) | Trust-zone changes as data flows through the system, like users using the internet to access a secured corporate network. |

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
