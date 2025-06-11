


# Build applications with Azure DevOps
https://learn.microsoft.com/en-us/training/paths/build-applications-with-azure-devops/

Azure DevOps enables you to build, test, and deploy any application to any cloud or on premises. Learn how to configure build pipelines that continuously build, test, and verify your applications.

This learning path is part of a series. You can choose the topics you're most interested in or progress through each of them. Here are the learning paths in this series:

**Part 1:** Get started with Azure DevOps

**Part 2:** Build applications with Azure DevOps

**Part 3:** Deploy applications with Azure DevOps

In this learning path, you will:

* Collaborate with others to build your applications using Azure Pipelines and GitHub
* Run automated tests in your pipeline to validate code quality
* Scan your source code and third-party components for potential vulnerabilities
* Define multiple pipelines that work together to build your application
* Build applications using both Microsoft-hosted agents and your own build agents

## Prerequisites

* Evolve your DevOps practices



# 1 Create a build pipeline with Azure Pipelines

In this module, you'll learn to set up a continuous integration (CI) pipeline that automates the process of building your application.


# 1.1 Introduction

## Choose your training module development environment

In the Get started with Azure DevOps learning path, you helped the Tailspin team start their DevOps journey by evaluating their current processes and technologies, then planning their initial set of tasks on Azure Boards.

In this module, you'll help the team with their first task: setting up a continuous integration (CI) pipeline for their app.

### Choose your training module development environment

This training module provides two options for running the pipeline that you create while completing the module.

**Choose Local development environment using a Microsoft-hosted agent** if you want to use a Microsoft-hosted agent to run your pipeline. To run pipelines on a Microsoft-hosted agent, your Azure DevOps organization must have at least one Microsoft-hosted parallel job. Check your Microsoft-hosted parallel jobs count, and if you don't have any:

* **Request a free grant of parallel jobs.** The approval process for the free grant typically takes two to three business days. You can apply for the grant and return to complete the module when your request is approved.
* **Pay for a parallel job.** If you want to use a Microsoft-hosted agent and don't want to wait two to three business days for the free grant, you can purchase a parallel job and complete the training using the paid job.

**Choose GitHub Codespaces development environment using a self-hosted agent** if you don't have any parallel jobs and you don't want to wait two to three business days for the free grant in order to use a Microsoft-hosted agent. This module's GitHub Codespaces environment includes the required development tools and provides a self-hosted agent that runs the pipeline that you create in the training module. This isn't a typical production scenario, but it does provide an environment for completing this training module. GitHub Codespaces provides a free tier of included usage hours and storage (charges might apply if you exceed the free tier, so check your usage).

> **Note**
> 
> If you decide to change between Local development environment using a Microsoft-hosted agent and GitHub Codespaces development environment using a self-hosted agent after starting the training module, you should restart the module and follow the steps from the beginning.

## Training module scenario

The Tailspin web team is being pulled in many directions. Andy, the lead dev, is running from one meeting to another and never has any time. Amita, the QA person, is helping a tester on another team. Tim, who's in Ops, is upgrading his servers and hasn't been seen for days. Mara's dream of a true DevOps team is stalled (again).

She isn't giving up, though. She remembers that she and the team used Azure Boards to create a backlog of issues with the build process:

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/build-all-tasks.png)

*Screenshot of Azure Boards showing a backlog of issues.*

She also remembers that they picked three of the issues to fix within the next two weeks. (Of course, everyone else has forgotten about them.)

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/build-initial-tasks.png)

*Screenshot of Azure Boards showing the initial three tasks.*

Mara decides to take an initial pass on the biggest issue, **Stabilize the build server**, herself. She won't try to fix everything. Instead, she's going to see if she can use Microsoft Azure Pipelines to replicate the current build process. She's convinced that Azure Pipelines provides enough benefits to improve the process. If she's right, she'll show her version to the team to see if she can make them more enthusiastic.

## Learning objectives

After completing this module, you'll be able to:

* Create a build pipeline in Azure Pipelines.
* Map manual build steps to automated build tasks.
* Publish your builds so others can access them.
* Use templates to build multiple configurations.

## Configure your environment

The modules in this learning path and previous learning path form a progression.

To follow the progression from the beginning, be sure to first complete the Get started with Azure DevOps learning path.

To complete this training module using a self-hosted agent with GitHub Codespaces, you must have:

* An Azure DevOps organization. If you don't already have an Azure DevOps organization, create a free organization before you begin. If you have completed the Get started with Azure DevOps learning path prerequisite, use that Azure DevOps organization.
* A GitHub account

If your company's policy doesn't allow you to create an Azure DevOps project in your existing company Azure DevOps organization, you can create your own personal Azure DevOps organization. You can get started with Azure DevOps for free.

This Azure DevOps environment lets you complete the exercises in this and future modules. You can also use it to apply your new skills to your own projects.

> **Note**
> 
> Azure Pipelines support a vast array of languages and application types. In this module, you'll be working with a .NET application but you can apply the patterns you learn here to your own projects that use your favorite programming languages and frameworks.

## Meet the team

You met the Space Game web team at Tailspin Toys in previous modules. As a refresher, here's who you'll work with in this module:

*Cartoon depiction of Andy.*

**Andy** is the development lead.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/andy.png)
*Cartoon depiction of Amita.*

**Amita** is in QA.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/amita.png)
*Cartoon depiction of Mara.*

**Mara** just joined as a developer and reports to Andy.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/mara.png)
Mara has prior experience with DevOps, and is helping the team adopt a more streamlined process by using Microsoft Azure DevOps.
