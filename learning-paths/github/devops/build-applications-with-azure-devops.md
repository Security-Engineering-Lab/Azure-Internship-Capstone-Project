


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

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/andy.png)
**Andy** is the development lead.

*Cartoon depiction of Amita.*

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/amita.png)
**Amita** is in QA.

*Cartoon depiction of Mara.*
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/mara.png)
**Mara** just joined as a developer and reports to Andy.

Mara has prior experience with DevOps, and is helping the team adopt a more streamlined process by using Microsoft Azure DevOps.

# 1.2 What is Azure Pipelines?

## Choose your training module development environment

Microsoft Azure Pipelines is a cloud service you can use to automatically build, test, and deploy your code project. You can also make it available to other users, and it works with just about any language or project type.

Mara is excited about replicating the team's build process on Azure Pipelines. Amita, the tester, finally has some free time and wants to catch up. Mara decides that now is a great time to tell her about her plan: setting up an automated build pipeline for the Space Game web site by using Azure Pipelines.

When she hears Mara's plan, Amita is a bit hesitant, but because Mara's plan is to replicate the build process but not replace it, she's also curious. She knows the build process could use some improvements.

**Amita:** It sounds like an interesting exercise, but you must want to prove a DevOps point!

**Mara:** You already know me so well!

**Amita:** What improvements do you expect to see, especially because you're going to do what we already do?

**Mara:** I think that just moving to Azure Pipelines will bring many benefits. Remember, Azure Pipelines is a cloud service. We can use it to automatically build and test code. And it will be available to others as well. It works with just about any language or project type.

Our build server has problems, and even keeping it up to date is hard. Because Azure Pipelines provides build servers that Microsoft hosts and maintains, it always has the latest patches and security updates. We won't have to worry about maintaining build servers.

Also, we have all kinds of scripts written by different people. We don't even understand how some of them work. Azure Pipelines comes with a catalog of tasks. A task is a packaged script or procedure that's been abstracted with a set of inputs. I'm going to try to map what our build scripts do to those tasks. At least we can standardize how things get done and increase the level of automation.

And Azure Pipelines works with many different languages and app types. If we want to expand in those directions, we won't have to retool.

**Amita:** I know it's selfish, but why do I care? One of my big problems is that I never know when a build is ready to test. Sometimes someone remembers to update the spreadsheet, but many times they forget. It seems like I'm the last person to know.

**Mara:** Right, that's something we can easily fix. We can set up the pipeline to notify you automatically, either through email or some other notification, when a build is ready. You'll never have to wait for someone to remind you again.

**Amita:** Okay, so your goal right now is to build the app and let me know when it's ready?

**Mara:** Right! Of course, I've got bigger plans. I know you're all going to love this first step, so I want to build on it to give us true continuous integration.

**Amita:** Give me the five-minute rundown on continuous integration.

**Mara:** Let me draw you a picture.

Mara moves to the whiteboard and draws the pipeline.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/2-whiteboard-pipeline-with-callouts.png)

*Screenshot of a hand-drawn illustration of a CI pipeline. The Build, Test, and Verify stages act on code. The build artifact is the output.*

**Mara:** This is my CI pipeline. CI is the process of automating the building and testing of code every time a team member commits changes to version control. I know we don't do automated testing yet, but give it time.

A pipeline defines the continuous integration process for the app. It's made up of steps called tasks. ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-01.png) You can think of it as a script that defines how your build, test, and deployment steps are run. I'm going to try to map our scripts to tasks.

The pipeline runs when you submit code changes. ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-02.png) You can configure the pipeline to run automatically, or you can run it manually. You connect your pipeline to a source repository like GitHub, Bitbucket, or Subversion. One of our tasks for this sprint is to start using GitHub, so we'll use GitHub for this project.

A build agent ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-03.png) builds or deploys the code. When your build or deployment runs, the system begins one or more jobs. An agent is an installable software that runs one build or deployment job at a time. Because we're using Azure Pipelines, we can use a Microsoft-hosted agent. With Microsoft-hosted agents, maintenance and upgrades are taken care of for us. Each time we run a pipeline, we'll get a fresh virtual machine. There are several virtual machine images to choose from, including Ubuntu 22.04, which is what we use.

The final product of the pipeline is a build artifact. ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-04.png) Think of an artifact as the smallest compiled unit that we need to test or deploy the app. For example, an artifact can be:

* A Java or .NET app packaged into a .jar or .zip file.
* A C++ or JavaScript library.
* A virtual machine, cloud, or Docker image.

And that's it. I know we can do this.

**Amita:** It sounds great. Let's see what you have to do to get it to work and how long it takes you. You can give us all a demo.

**Mara:** Will do!

## Manage build agents

Now that you and the team are familiar with Azure Pipelines, let's talk a bit more about build agents. A build agent is a piece of installable software that runs one build or deployment job at a time. To build your code or deploy your software, you need at least one agent. As you add more code and people, you'll eventually need more than one agent. There are two main categories of agents.

**Microsoft-hosted agents** are agents that Microsoft manages, so maintenance and upgrades are taken care of for you. Each time you run a pipeline, you get a new agent for each job in the pipeline. In this module, when you choose Local development environment using a Microsoft-hosted agent, you're running your pipeline on a Microsoft-hosted agent. To run pipelines on a Microsoft-hosted agent, your organization must have at least one Microsoft-hosted parallel job. Check your Microsoft-hosted parallel jobs count to ensure that you have at least one Microsoft-hosted parallel job. If your Microsoft-hosted parallel jobs count is zero (new Azure DevOps organizations typically have zero parallel jobs), you can request a free grant. The approval process for the free grant typically takes two to three business days.

**Self-hosted agents** are agents that you manage. You configure the virtual machines or containers by installing the agent software and desired tools, and register the agents with Azure DevOps. In this module, when you choose GitHub Codespaces development environment using a self-hosted agent, you're using a self-hosted agent running in your GitHub Codespaces container. Self-hosting the agent on a GitHub Codespaces container isn't a typical production scenario, but it does provide an environment for completing this training module.

## Check your knowledge

**1. Which of these is an example of a build artifact?**

The code compiler used to build the application.
A Windows Installer (.msi) file that contains a C++ desktop application. ✅
An email that summarizes the build run.


# 1.3 Exercise - Get the sample application

## Choose your training module development environment

Get ready to start building a CI pipeline with Microsoft Azure Pipelines. The first step is to build and run the Space Game web app. Understanding how to build software manually, prepares you to repeat the process in the pipeline.

Mara is going to do exactly that, and by following the procedures, you can do the same thing.

## Create an Azure DevOps personal access token

1. Sign in to your organization (https://dev.azure.com/{yourorganization}). If you don't already have an Azure DevOps organization, create a free organization before you begin. After you sign in, if you have more than one organization, choose Azure DevOps and go to the organization that you plan to use to complete this module. In this example, the name of the organization is fabrikam.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/3-choose-organization.png)

   *Screenshot of choosing your Azure DevOps organization.*

2. From your home page, open user settings and select **Personal access tokens**.

3. Select **+ New Token**.

4. Name your token using any name that you prefer. The token is used when the Codespace registers its agent with your Azure DevOps organization, so you can keep the default expiration.

5. Choose **Custom defined** and choose **Show all scopes**.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/3-show-all-scopes.png)
   
   *Screenshot of viewing all scopes for a personal access token.*

6. Select the following scope: **Agent Pools (Read & manage)**, and choose **Create**.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/3-agent-pools-read-and-manage.png)

   *Screenshot of selecting agent pool permissions for a personal access token.*

7. When you're done, copy the token and store it in a secure location. For your security, it won't be shown again.

> **Warning**
> 
> Treat and use a PAT like your password and keep it secret.

## Create a fork

The first step to using a project in Git is to create a fork so you can work with and modify the source files. A fork is a copy of a GitHub repository. The copy exists in your account and lets you make any changes you want without affecting the original project.

Although you can propose changes to the original project, in this lesson, you work with the Space Game web project as though it was the original project owned by Mara and the team.

> **Note**
> 
> If you have previously forked this repository, for example if you have previously completed this module or another Tailspin Toys training module, we recommend that you delete your fork and create a new fork using the following steps. If you don't want to delete your fork, ensure that you sync your fork.

Let's fork the Space Game web project into your GitHub account:

1. In a web browser, go to GitHub and sign in.

2. Go to the Space Game web project.

3. Select **Fork**:

![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/3-github-fork-button.png)

   *Screenshot of GitHub showing the location of the Fork button.*

4. To fork the repository into your account, follow the instructions.

## Set up secrets for self-hosted agent

Before you create your Codespace, you create several secrets that help your self-hosted Azure DevOps agent run. In production, you wouldn't want to use a self-hosted agent in GitHub Codespaces. However, because your team is using Codespaces for testing, it's a good temporary solution to use it when you're building your pipelines.

1. Go to your forked GitHub repository and select **Settings > Secrets and variables > Codespaces**.

   *Screenshot of GitHub Codespaces secrets.*

![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/3-add-codespaces-secret.png)

2. Create the following Codespaces Repository secrets.

   | Name | Value |
   |------|-------|
   | ADO_ORG | Name of the Azure DevOps organization you're using to complete this module. In this example, fabrikam is the name of the organization. This organization name must be the same one you used when you created your PAT in the previous step. |
   | ADO_PAT | The Personal Access Token that you created in the previous step. |

> **Tip**
> 
> In this training module, your agent is assigned to the Default agent pool. If don't want to run your agent in the Default pool (for example, you're running this training module using your production Azure DevOps environment and you have other agents in the Default pool), you can create a secret named ADO_POOL_NAME and specify the name of the agent pool to use. If this secret isn't specified, the Default pool is used.

## Set up Codespaces

Next, you set up Codespaces so that you can build the website, work with source files, and run your pipeline using a self-hosted agent.

1. In your forked GitHub repository, select **Code**, select **Code** again, choose the **Codespaces** tab, and choose **+** to create a new Codespace.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/3-create-new-options-codespaces.png)
   *Screenshot of create a new Codespace with options.*

2. Wait for your Codespace to build. This build can take a few moments, but you only have to do it once in this step of the training module.

3. When the build completes, you're redirected to an online version of Visual Studio Code. Your Codespace comes with a fresh installation of Visual Studio Code, similar to a fresh installation of Visual Studio Code on your local machine. When the Codespace first starts, Visual Studio Code online might prompt you to provide certain configurations or ask you about preferences. You can choose the preferences that suit your Visual Studio Code usage style.

## Set the upstream remote

A remote is a Git repository where team members collaborate (similar to a repository on GitHub). Let's list your remotes and add a remote that points to Microsoft's copy of the repository so you can get the latest sample code.

1. In the Visual Studio Code online editor, go to the terminal window and choose **bash** from the right-hand side.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/3-terminal-window.png)
   
   *Screenshot of terminal window in Visual Studio Code online editor.*

2. To list your remotes, run the `git remote` command:

   ```bash
   git remote -v
   ```

   You have both fetch (download) and push (upload) access to your repository:

   ```
   origin  https://github.com/username/mslearn-tailspin-spacegame-web.git (fetch)
   origin  https://github.com/username/mslearn-tailspin-spacegame-web.git (push)
   ```

   Origin specifies your repository on GitHub. When you fork code from another repository, it's common to name the original remote (the one you forked from) upstream.

3. To create a remote named upstream that points to the Microsoft repository, run this `git remote add` command:

   ```bash
   git remote add upstream https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web.git
   ```

4. Run `git remote` a second time to see the changes:

   ```bash
   git remote -v
   ```

   You see that you still have both fetch (download) and push (upload) access to your repository. You also now have fetch and push access to the Microsoft repository:

   ```
   origin  https://github.com/username/mslearn-tailspin-spacegame-web.git (fetch)
   origin  https://github.com/username/mslearn-tailspin-spacegame-web.git (push)
   upstream        https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web.git (fetch)
   upstream        https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web.git (push)
   ```

## Build and run the web app

1. In the Visual Studio Code online editor, navigate to the terminal window, and to build the app, run this `dotnet build` command:

   ```bash
   dotnet build --configuration Release
   ```

2. From the terminal window, to run the app, run this `dotnet run` command:

   ```bash
   dotnet run --configuration Release --no-build --project Tailspin.SpaceGame.Web
   ```

   .NET solution files can contain more than one project. The `--project` argument specifies the project for the Space Game web app.

## Verify the application is running

1. In development mode, the Space Game website is configured to run on port 5000.

2. You see a new message in the Visual Studio editor. Your application running on port 5000 is available. Select **Open in Browser** to go to the running app.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/3-port-forwarding-message.png)

   *Screenshot of port forwarding Codespaces message.*

3. In the new browser window, you should see the Space Game web site:

![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/3-space-game-top.png)

   *Screenshot of a web browser showing the Space Game web site.*

4. You can interact with the page, including the leaderboard. When you select a player's name, you see details about that player:

![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/3-space-game-leaderboard-profile.png)

   *Screenshot of a web browser showing the Space Game leaderboard.*

5. When you're finished, return to the terminal window, and to stop the running app, select **Ctrl + C**.



