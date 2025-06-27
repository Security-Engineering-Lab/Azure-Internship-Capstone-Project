


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

