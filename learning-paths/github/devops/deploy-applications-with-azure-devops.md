
# Deploy applications with Azure DevOps
https://learn.microsoft.com/en-us/training/paths/deploy-applications-with-azure-devops/

Azure DevOps enables you to build, test, and deploy any application to any cloud or on premises. Learn how to configure release pipelines that continuously build, test, and deploy your applications.

This learning path is part of a series. You can choose the topics you're most interested in or progress through each of them. Here are the learning paths in this series:

The trophy for the Get started with Azure DevOps learning path.

- Part 1: Get started with Azure DevOps. 
- Part 2: Build applications with Azure DevOps. 
- Part 3: Deploy applications with Azure DevOps

In this learning path, you will:
- Create a basic release pipeline that deploys a web application to Azure App Service.
- Build a more complete pipeline that deploys to multiple development and testing stages.
- Run functional and non-functional tests that verify your application's behavior and performance.
- Choose and implement an appropriate deployment pattern to smoothly roll out new features to your users.
- Extend pipelines to add support for different deployment targets, such as Azure Functions.
- Automate Docker and multi-container Kubernetes deployments with Azure Pipelines.

#### Prerequisites
- Get started with Azure DevOps
- Build applications with Azure DevOps
- An Azure subscription


# 1 Create a release pipeline in Azure Pipelines

Set up a continuous delivery (CD) pipeline that automates the process of deploying your application.

#### Learning objectives
After completing this module, you'll be able to:
- Define what continuous delivery is, why it's important, and what tools you can use.
- Create a basic release pipeline in Azure Pipelines that deploys a web application to Azure App Service.
- Examine pipeline analytics to understand the health and history of your releases.
#### Prerequisites
- An Azure subscription
- An Azure DevOps organization with access to parallel jobs
- Visual Studio Code
- .NET 8.0 SDK
- Git
- A GitHub account

# 1.1 **Introduction**

In the **Build applications with Azure DevOps** learning path, you helped the Tailspin Toys team use Azure DevOps to plan and build a continuous integration (CI) pipeline to build their *Space Game* website.

The Tailspin team's big release is approaching. The team can use Azure DevOps to build and test their code, but how can they quickly deploy the application to an environment that's available to their users?

In this module, you'll continue your journey with the Tailspin team as they set up a continuous delivery (CD) pipeline to deploy their *Space Game* website.

## **Learning objectives**

After completing this module, you'll be able to:

* Define what continuous delivery is, why it's important, and what tools you can use.
* Create a basic release pipeline in Azure Pipelines that deploys a web application to Azure App Service.
* Examine pipeline analytics to understand the health and history of your releases.

## **Prerequisites**

The modules in this learning path and previous learning paths form a progression.

If you want to start with this learning path, set up a development environment on your Windows, macOS, or Linux system. You'll need:

* An Azure DevOps organization with access to parallel jobs. If your organization does not have access to parallel jobs, you can request parallel jobs for free for public or private projects using [this form](https://aka.ms/azpipelines-parallelism-request). Your request takes 2-3 business days.
* An Azure subscription
* A GitHub account
* Visual Studio Code with the Azure Pipelines for VS Code extension.
* .NET 8.0 SDK
* Git

To follow the progression from the beginning, complete the following learning paths:

* **Get started with Azure DevOps**
* **Build applications with Azure DevOps**

You can get started with Azure and Azure DevOps for free. You don't need an Azure subscription to work with Azure DevOps, but here you'll use Azure DevOps to deploy to Azure resources in your Azure subscription.

> **Note**
> 
> Azure Pipelines support a vast array of **languages and application types**. In this module, you'll be working with a .NET application but you can apply the patterns you learn here to your own projects that use your favorite programming languages and frameworks.

## **Meet the team**

You met the *Space Game* web team at Tailspin Toys in previous modules. As a refresher, here's who you'll work with in this module:

**Andy** is the development lead.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/andy.png)

**Amita** is in QA.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/amita.png)

**Tim** is in operations.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/tim.png)

**Mara** just joined as a developer and reports to Andy.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/mara.png)

**Irwin** is the product manager.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/irwin.png)

Mara has prior experience with DevOps. She's helping the team adopt a streamlined process by using Azure DevOps.
