


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



# 1.4 Plan your build tasks

## Choose your training module development environment

Mara now has a copy of the Space Game code. She's going to build it using Microsoft Azure Pipelines instead of the existing Ubuntu 22.04 build server. Before she can do that, she needs to think about the existing build scripts. Follow along as she maps the existing scripts to Azure Pipelines tasks. Think about how you can do the same with your own build process.

Here are some notes that Mara collected when she talked to Andy, the dev lead:

* The build machine is running Ubuntu 22.04.
* The build machine includes build tools like:
  * npm, the package manager for Node.js
  * NuGet, the package manager for .NET
  * .NET SDK
* The project uses Syntactically Awesome Style Sheets (Sass) to make it easier to author cascading style sheets (CSS) files.
* The project uses the gulp toolkit to minify JavaScript and CSS files.
* A minified asset excludes unneeded data (like whitespace) and shortens variable names to help it download faster.

Here are the steps that happen during the build process:

1. To install the Node.js packages defined in package.json, run `npm install`.
2. To convert Sass (.scss) files to CSS (.css) files, run `node-sass`.
3. To minify JavaScript and CSS files, run `gulp`.
4. To help the QA team identify the build number and date, print build information to the wwwroot directory.
5. To install the project's dependencies, run `dotnet restore`.
6. To build the app under both Debug and Release configurations, run `dotnet build`.
7. To package the application as a .zip file and copy the results to a network share for the QA team to pick up, run `dotnet publish`.

Mara builds a shell script that performs the tasks she's identified. She runs it on her laptop.

> **Note**
> 
> You don't need to run this script or completely understand what it does. It's here to illustrate what a typical build script might do.

```bash
#!/bin/bash

# Install Node.js modules as defined in package.json.
npm install --quiet

# Compile Sass (.scss) files to standard CSS (.css).
node-sass Tailspin.SpaceGame.Web/wwwroot

# Minify JavaScript and CSS files.
gulp

# Print the date to wwwroot/buildinfo.txt.
echo `date` > Tailspin.SpaceGame.Web/wwwroot/buildinfo.txt

# Install the latest .NET packages the app depends on.
dotnet restore

# Build the app under the Debug configuration.
dotnet build --configuration Debug

# Publish the build to the /tmp directory.
dotnet publish --no-build --configuration Debug --output /tmp/Debug

# Build the app under the Release configuration.
dotnet build --configuration Release

# Publish the build to the /tmp directory.
dotnet publish --no-build --configuration Release --output /tmp/Release
```

The /tmp directory mimics the team's network share.

After she runs the script, Mara realizes that it's incomplete. For example, it doesn't deal with errors. It doesn't notify anyone if build errors occur. Even when there are errors, it keeps running. It also doesn't install the tools each step requires.

## What are Azure Pipelines tasks?

In Azure Pipelines, a task is a packaged script or procedure that's been abstracted with a set of inputs.

An Azure Pipelines task abstracts away the underlying details. This abstraction makes it easier to run common build functions, like downloading build tools or packages your app depends on, or to build your project, running Visual Studio or Xcode.

To build a C# project that targets .NET, here's an example that uses the DotNetCoreCLI@2 task:

```yml
task: DotNetCoreCLI@2
  displayName: 'Build the project'
  inputs:
    command: 'build'
    arguments: '--no-restore --configuration Release'
    projects: '**/*.csproj'
```

The pipeline might translate this task to this command:

```bash
dotnet build MyProject.csproj --no-restore --configuration Release
```

Let's break this task down a bit more:

* The **DotNetCoreCLI@2** task maps to the `dotnet` command.
* **displayName** defines the task name that's shown in the user interface. You'll see this in action soon.
* **inputs** defines arguments that are passed to the command.
* **command** specifies to run the `dotnet build` subcommand.
* **arguments** specifies additional arguments to pass to the command.
* **projects** specifies which projects to build. This example uses the wildcard pattern `**/*.csproj`. Both `**` and `*.csproj` are examples of what are called glob patterns. The `**` part specifies to search the current directory and all child directories. The `*.csproj` part specifies any .csproj file. Wildcards let you act on multiple files without specifying each one. If you need to act on a specific file only, you can specify that file instead of using wildcards.

The "@" in the task name—for example, **DotNetCoreCLI@2**—refers to the task's version. As new task versions become available, you can gradually migrate to the latest version to take advantage of new features.

## How are tasks used in a pipeline?

Next, Mara's going to map the existing script commands to Azure Pipelines tasks. A Pipeline is created using a YAML file, which is a compact format that makes it easy to structure the kind of data that's in configuration files. Pipeline YAML files are typically maintained directly with your app's source code.

Mara used YAML previously to define similar build tasks and configurations. She also likes the idea of maintaining the build definition as code, just as she would any other part of her project.

To define her build, Mara chooses to use Visual Studio Code to create a YAML file. In it, she enters all the Azure Pipelines tasks that she'll use to replace the existing script commands.

## Map script commands to Azure Pipelines tasks

Now, you'll follow along as Mara maps commands from her script to Azure Pipelines tasks.

To map each command, Mara refers to the reference documentation. The documentation categorizes tasks by function, like build or deploy.

For example, the .NET Core CLI task **DotNetCoreCLI@2** helps you run dotnet commands.

This table associates the script commands with the new Azure Pipelines tasks:

| Script command | Azure Pipelines task |
|----------------|----------------------|
| npm install | Npm@1 |
| node-sass | CmdLine@2 (or script) |
| gulp | gulp@1 |
| echo `date` | CmdLine@2 (or script) |
| dotnet restore | DotNetCoreCLI@2 |
| dotnet build | DotNetCoreCLI@2 |
| dotnet publish | DotNetCoreCLI@2 |

There's no built-in task type that runs node-sass or prints the date to a file. For those, Mara uses the **CmdLine@2** task, which lets her run any command that she wants. More commonly, you'll see the **script** task, which is a shortcut for **CmdLine@2**. For more information about the other common task shortcuts, see YAML scheme reference for Azure Pipelines - steps.

You'll soon create a YAML file of your own that uses these tasks.

## Check your knowledge

**1. A build task:**

Defines how a test, build, or deployment step is run. ✅
Is the same as the make utility.
Is run on the build agent when the build completes to clean up the system.


# 1.5 Exercise - Set up your Azure DevOps environment

## Choose your training module development environment

**Local development environment using a Microsoft-hosted agent** | **GitHub Codespaces development environment using a self-hosted agent**

In this section, you'll ensure that your Microsoft Azure DevOps organization is set up to complete the rest of this module.

The modules in this learning path form a progression, in which you follow the Tailspin web team through its DevOps journey.

This learning path also builds on the Get started with Azure DevOps learning path. There, you used the basic process to set up your Azure DevOps organization and created a task backlog on Azure Boards.

## Get the Azure DevOps project

Here, you ensure that your Azure DevOps organization is set up to complete the rest of this module. You do this by running a template that creates a project for you in Azure DevOps.

For learning purposes, each module has an associated Azure DevOps project, so you can start each module even if you haven't completed the previous modules.

### Run the template

Run a template that sets up your Azure DevOps organization.

1. Get and run the ADOGenerator project in Visual Studio or the IDE of your choice.

2. When prompted to **Enter the template number from the list of templates**, enter **22** for **Create a build pipeline with Azure Pipelines**, then press **Enter**.

3. Choose your authentication method. You can set up and use a Personal Access Token (PAT) or use device login.

   > **Note**
   > 
   > If you set up a PAT, make sure to authorize the necessary **scopes**. For this module, you can use **Full access**, but in a real-world situation, you should ensure you grant only the necessary scopes.

4. Enter your Azure DevOps organization name, then press **Enter**.

5. If prompted, enter your Azure DevOps PAT, then press **Enter**.

6. Enter a project name such as *Space Game - web - Pipeline*, then press **Enter**.

7. Once your project is created, go to your Azure DevOps organization in your browser (at `https://dev.azure.com/<your-organization-name>/`) and select the project.

## Fork the repository

If you haven't already, create a fork of the **mslearn-tailspin-spacegame-web** repository.

1. On GitHub, go to the mslearn-tailspin-spacegame-web repository.

2. Select **Fork** at the top-right of the screen.

3. Choose your GitHub account as the **Owner**, then select **Create fork**.

> **Important**
> 
> The **Clean up your Azure DevOps environment** unit at the end of this module provides important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes for Microsoft-hosted agents (**check your usage**), or GitHub Codespaces **included usage hours and storage** (**charges might apply if you exceed the free tier, so check your usage**). Be sure to do the cleanup steps even if you don't complete this module.



# 1.6 Exercise - Create the pipeline

## Choose your training module development environment

At this point, Mara has defined a build configuration for the Space Game website. Now, it's your turn; you're going to create a pipeline and produce your first build artifact.

As you saw, Mara used a YAML file to define the build. When you create a pipeline, the process prompts you for your YAML file. The project doesn't have this file yet.

When you don't provide an initial YAML file for your project, Azure Pipelines can create one for you based on your app type. Here, you'll build an ASP.NET Core app, but Azure Pipelines also provides starter build configurations for other project types, including Java, Go, and more.

## Create the pipeline

1. In Azure DevOps, go to your project.

2. Either from the project page or from the left pane, select **Pipelines**.

3. Select **Create Pipeline** (or **New pipeline** if this isn't the first pipeline in the project).

4. On the **Connect** tab, select **GitHub**.

5. When prompted, enter your GitHub credentials.

6. On the **Select** tab, select your **mslearn-tailspin-spacegame-web** repository.

7. To install the Azure Pipelines app, you might be redirected to GitHub. If so, scroll to the bottom, and select **Approve & Install**.

8. On the **Configure** tab, select **ASP.NET Core**.

   > **Note**
   > 
   > If you don't see this option, select **Show more**. Don't select **ASP.NET Core (.NET Framework)**.

   *Screenshot of locating ASP.NET Core from the list of provided application types.*

   ![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/6-configure-app-type.png)

   > **Note**
   > 
   > If your repository has an azure-pipelines.yml file at the root level, Azure DevOps may skip the Configure step. To resolve this issue, remove or rename the file.

10. On the **Review** tab, note the initial build configuration.

   *Screenshot of Azure Pipelines showing the initial build configuration.*

   ![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/6-initial-pipeline-yml.png)

   This is a very basic configuration that Azure DevOps provides for you based on your app type, ASP.NET Core. The default configuration uses a Microsoft-hosted agent.

11. Replace the text `vmImage: ubuntu-latest` with `name: Default` (or the name of your agent pool if you specified a different pool when setting up the Codespaces Repository secrets).

12. On the **Review** tab, select **Save and run**. To commit your changes to GitHub and start the pipeline, choose **Commit directly to the main branch** and select **Save and run** a second time. If you're prompted to grant permission with a message like **This pipeline needs permission to access a resource before this run can continue**, choose **View** and follow the prompts to permit access.

## Watch the pipeline run

1. Under **Jobs**, select **Job**. Next, trace the build process through each of the steps. To see the job output as a text file when the build completes, you can also select **View raw log**.

   If your pipeline doesn't start quickly, verify that Codespaces is still running. Codespaces will shut down after 30 minutes and may need to be restarted.

2. Here, you see the steps that the build definition created. It prepares the VM, fetches the latest source code from GitHub, and then builds the app.

   *Screenshot of Azure Pipelines showing output from the initial build configuration.*

 ![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/6-initial-build.png)

   This configuration is a great start, because now you have a place to add build tasks. You still need to update it to meet the needs of the Tailspin team, such as to minify JavaScript and CSS files.

> **Tip**
> 
> Check your email. You might have already received a build notification with the results of your run. You can use these notifications to let your team members know when builds complete, and whether each build passed or failed.

## Add build tasks

Now that you have a working build process, you can start to add build tasks.

Remember that you're working from the main branch. To hold your work, you'll now create a branch named **build-pipeline**. The branch gives you a place to experiment and get your build working completely without affecting the rest of the team.

You can add build tasks to azure-pipelines.yml directly from Azure Pipelines. Azure Pipelines commits your changes directly to your branch. Here, you'll change azure-pipelines.yml locally and push—or upload—your changes to GitHub. Doing it this way lets you practice your Git skills. Watch the pipeline automatically build the app when you push up changes.

In practice, you might add build tasks one at a time, push your changes, and watch the build run. Here, you'll add all the build tasks we identified earlier at one time.

> **Note**
> 
> You're about to run a few Git commands. Don't worry if you're new to Git. We'll show you what to do. We'll also go into more detail about Git in future modules.

1. In Visual Studio Code, go to the integrated terminal. Ensure you go to the main branch in your repo and then go through the steps.

2. To fetch the latest changes from GitHub and update your main branch, run this `git pull` command.

   ```bash
   git pull origin main
   ```

   You'll see from the output that Git fetches a file named azure-pipelines.yml. This is the starter pipeline configuration that Azure Pipelines created for you. When you set up the pipeline, Azure Pipelines adds this file to your GitHub repository.

3. To create a branch named **build-pipeline**, run this `git checkout` command:

   ```bash
   git checkout -B build-pipeline
   ```

4. In Visual Studio Code, change azure-pipelines.yml as you see here:

   ```yml
   trigger:
   - '*'

   pool:
     name: 'Default' # Replace Default with the name of your agent pool if you used a different pool

   variables:
     buildConfiguration: 'Release'

   steps:
   - task: UseDotNet@2
     displayName: 'Use .NET SDK 6.x'
     inputs:
       packageType: sdk
       version: '6.x'

   - task: Npm@1
     displayName: 'Run npm install'
     inputs:
       verbose: false

   - script: './node_modules/.bin/node-sass Tailspin.SpaceGame.Web/wwwroot --output Tailspin.SpaceGame.Web/wwwroot'
     displayName: 'Compile Sass assets'

   - task: gulp@1
     displayName: 'Run gulp tasks'

   - script: 'echo "$(Build.DefinitionName), $(Build.BuildId), $(Build.BuildNumber)" > buildinfo.txt'
     displayName: 'Write build info'
     workingDirectory: Tailspin.SpaceGame.Web/wwwroot

   - task: DotNetCoreCLI@2
     displayName: 'Restore project dependencies'
     inputs:
       command: 'restore'
       projects: '**/*.csproj'

   - task: DotNetCoreCLI@2
     displayName: 'Build the project - Release'
     inputs:
       command: 'build'
       arguments: '--no-restore --configuration Release'
       projects: '**/*.csproj'
   ```

   Under the **steps** section, you see the build tasks that map to each of the script commands that we identified earlier.

   Azure Pipelines provides built-in build tasks that map to many common build activities. For example, the **DotNetCoreCLI@2** task maps to the dotnet command-line utility. The pipeline uses **DotNetCoreCLI@2** two times: one time to restore, or install, the project's dependencies, and one time to build the project.

   Remember that not all build activities map to a built-in task. For example, there's no built-in task that runs the node-Sass utility, or writes build info to a text file. To run general system commands, you use the **CmdLine@2** or **script** task. The pipeline uses the **script** task because it's a common shortcut for **CmdLine@2**.

   In the build step that writes information about the build to a file, notice these elements:

   - `$(Build.DefinitionName)`
   - `$(Build.BuildId)`
   - `$(Build.BuildNumber)`

   These elements are built-in variables that the system provides for use in your pipelines:

   - `$(Build.DefinitionName)` is the name of the build pipeline. For example, "SpaceGame-Web-CI."
   - `$(Build.BuildId)` is a numeric identifier for the completed build, like 115.
   - `$(Build.BuildNumber)` is the name of the completed build. You can configure the format, but by default, the build number includes the current date followed by the build number for that day. An example build number is "20190329.1."

   You can also define your own variables, which you'll do soon.

   You might have also noticed the **UseDotNet@2** task, which is the first build step. Mara remembered that the build script didn't install the required build tools. Although the build agent comes with several .NET SDK versions, this task lets the pipeline author easily specify the version they need to use on the build agent.

5. From the integrated terminal, run the following Git commands to add azure-pipelines.yml to the index, commit the change, and push the change to GitHub. These steps are similar to the steps you performed earlier.

   > **Tip**
   > 
   > Before you run these Git commands, remember to save azure-pipelines.yml.

   ```bash
   git add azure-pipelines.yml
   git commit -m "Add build tasks"
   git push origin build-pipeline
   ```

   This time, you push the **build-pipeline** branch, not the main branch, to GitHub.

   Pushing the branch to GitHub triggers the build process in Azure Pipelines.

6. In Azure Pipelines, go to your build. To do so, on the side of the page, select **Pipelines**, then select your pipeline. You'll see your commit message and that the build is running using the code from the **build-pipeline** branch.

   *Screenshot of Azure Pipelines showing the run history, including the branch you recently pushed to GitHub.*

   ![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/6-build-history.png)

   > **Tip**
   > 
   > If you don't see the build right away, wait a few moments or refresh the page.

7. Select your build and choose **Jobs** and trace the build tasks as they run.

   For example, here's what happens when the **gulp@1** task runs to perform the gulp tasks that minify JavaScript and CSS assets:

   *Screenshot of tracing the gulp tasks in Azure Pipelines.*

   ![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/6-gulp-task.png)

   If any step fails, you'll see the error in the output so you can diagnose and fix the failure.

9. Earlier, you ran a more minimal build configuration. This time, when the build completes, you see a more complete set of tasks needed to build the app.

   *Screenshot of Azure Pipelines showing the complete list of build tasks.*

   ![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/6-add-build-tasks.png)

11. After your build completes, select any of the steps to see the overall progression of the build. From there, you can jump to the build logs or the associated change on GitHub.

   *Screenshot of Azure Pipelines showing the complete list of build tasks. The Run gulp task is selected.*

![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/6-build-summary.png)



# 1.7 Exercise - Publish the result to the pipeline

## Choose your training module development environment

At this point, you can build the Space Game web project through the pipeline.

But where do the build results go? Right now, the build output remains on the temporary build server. Mara needs a way to hand off this build to Amita so she can begin testing.

You can store build artifacts in Azure Pipelines so that they're available to others on your team after the build completes, which is what you'll do here. As a bonus, you'll also refactor the build configuration to use variables to make the configuration easier to read and keep up to date.

> **Note**
> 
> Azure Pipelines lets you automatically deploy the built app to a testing or production environment running in the cloud or in your datacenter. For now, Mara's goal is only to produce builds that she can hand off to QA by using their existing processes.

## Publish the build to the pipeline

In .NET, you can package your app as a .zip file. You can then use the built-in **PublishBuildArtifacts@1** task to publish the .zip file to Azure Pipelines.

1. In Visual Studio Code, change azure-pipelines.yml as you see here:

   ```yml
   trigger:
   - '*'

   pool:
     name: 'Default' #replace if needed with name of your agent pool

   steps:
   - task: UseDotNet@2
     displayName: 'Use .NET SDK 6.x'
     inputs:
       version: '6.x'

   - task: Npm@1
     displayName: 'Run npm install'
     inputs:
       verbose: false

   - script: './node_modules/.bin/node-sass Tailspin.SpaceGame.Web/wwwroot --output Tailspin.SpaceGame.Web/wwwroot'
     displayName: 'Compile Sass assets'

   - task: gulp@1
     displayName: 'Run gulp tasks'

   - script: 'echo "$(Build.DefinitionName), $(Build.BuildId), $(Build.BuildNumber)" > buildinfo.txt'
     displayName: 'Write build info'
     workingDirectory: Tailspin.SpaceGame.Web/wwwroot

   - task: DotNetCoreCLI@2
     displayName: 'Restore project dependencies'
     inputs:
       command: 'restore'
       projects: '**/*.csproj'

   - task: DotNetCoreCLI@2
     displayName: 'Build the project - Release'
     inputs:
       command: 'build'
       arguments: '--no-restore --configuration Release'
       projects: '**/*.csproj'

   - task: DotNetCoreCLI@2
     displayName: 'Publish the project - Release'
     inputs:
       command: 'publish'
       projects: '**/*.csproj'
       publishWebProjects: false
       arguments: '--no-build --configuration Release --output $(Build.ArtifactStagingDirectory)/Release'
       zipAfterPublish: true

   - task: PublishBuildArtifacts@1
     displayName: 'Publish Artifact: drop'
     condition: succeeded()
   ```

   This version of azure-pipelines.yml looks like the previous version, but it adds two additional tasks.

   The first task uses the **DotNetCoreCLI@2** task to publish or package the app's build results (including its dependencies) into a folder. The **zipAfterPublish** argument specifies to add the built results to a .zip file.

   The second task uses the **PublishBuildArtifacts@1** task to publish the .zip file to Azure Pipelines. The **condition** argument specifies to run the task only when the previous task succeeds. **succeeded()** is the default condition, so you don't need to specify it, but we show it here to show its use.

2. From the integrated terminal, add azure-pipelines.yml to the index, commit the change, and push the change to GitHub.

   > **Tip**
   > 
   > Before you run these Git commands, remember to save azure-pipelines.yml.

   ```bash
   git add azure-pipelines.yml
   git commit -m "Add publish tasks"
   git push origin build-pipeline
   ```

3. As you did earlier, from Azure Pipelines, trace the build through each of the steps.

4. When the pipeline completes, go back to the build summary.

   Under **Related**, there's **1 published**.

   *Screenshot of the build summary. Details include the repository and version, the time started and elapsed, and a link to the published build artifact.*

5. Select the artifact.

6. Expand the **drop** folder.

   You'll see a .zip file that contains your built app and its dependencies:

   *Screenshot of the packaged web application in the Artifacts explorer.*

   If you want to try an optional exercise, you can download this .zip file to your computer and explore its contents.

## Define variables to enhance readability

Mara steps back to examine her work. The build configuration does what she needs, but she wants to ensure Andy and others can easily help keep it up to date and extend it.

Variables allow you to define values once and refer to those values throughout your pipeline. Azure Pipelines replaces each variable with its current value when the pipeline runs.

Just like in other programming languages, variables let you do things like:

* Define values that might change between runs of your pipeline.
* Store information that's repeated throughout your pipeline, like a version number or a file path, in one place. That way, you don't need to update all occurrences when yours need to change.

Azure Pipelines provides many built-in variables. These variables describe aspects of the build process, like the build identifier and the directory names where your software is built and staged.

You can also define your own variables. Here's an example that shows a variable named **buildConfiguration** that defines the Release build configuration:

```yml
variables:
  buildConfiguration: 'Release'
```

Use variables when you repeat the same value multiple times or when a value, like a dependency version, might change.

You don't need to create a variable for every piece of your build configuration. In fact, too many variables can make your pipeline code harder for others to read and understand.

Take a moment to examine azure-pipelines.yml. Notice that these values are repeated:

* **Build configuration**: Release.
* **Location of the wwwroot directory**: Tailspin.SpaceGame.Web/wwwroot.
* **.NET SDK version**: 6.x.

You now use variables to define these values one time. You then reference the variables throughout the pipeline.

1. In Visual Studio Code, change azure-pipelines.yml as you see here:

   ```yml
   trigger:
   - '*'

   pool:
     name: 'Default' #replace if needed with name of your agent pool

   variables:
     buildConfiguration: 'Release'
     wwwrootDir: 'Tailspin.SpaceGame.Web/wwwroot'
     dotnetSdkVersion: '6.x'

   steps:
   - task: UseDotNet@2
     displayName: 'Use .NET SDK $(dotnetSdkVersion)'
     inputs:
       version: '$(dotnetSdkVersion)'

   - task: Npm@1
     displayName: 'Run npm install'
     inputs:
       verbose: false

   - script: './node_modules/.bin/node-sass $(wwwrootDir) --output $(wwwrootDir)'
     displayName: 'Compile Sass assets'

   - task: gulp@1
     displayName: 'Run gulp tasks'

   - script: 'echo "$(Build.DefinitionName), $(Build.BuildId), $(Build.BuildNumber)" > buildinfo.txt'
     displayName: 'Write build info'
     workingDirectory: $(wwwrootDir)

   - task: DotNetCoreCLI@2
     displayName: 'Restore project dependencies'
     inputs:
       command: 'restore'
       projects: '**/*.csproj'

   - task: DotNetCoreCLI@2
     displayName: 'Build the project - $(buildConfiguration)'
     inputs:
       command: 'build'
       arguments: '--no-restore --configuration $(buildConfiguration)'
       projects: '**/*.csproj'

   - task: DotNetCoreCLI@2
     displayName: 'Publish the project - $(buildConfiguration)'
     inputs:
       command: 'publish'
       projects: '**/*.csproj'
       publishWebProjects: false
       arguments: '--no-build --configuration $(buildConfiguration) --output $(Build.ArtifactStagingDirectory)/$(buildConfiguration)'
       zipAfterPublish: true

   - task: PublishBuildArtifacts@1
     displayName: 'Publish Artifact: drop'
     condition: succeeded()
   ```

   Notice the **variables** section, which defines these variables:

   * **buildConfiguration**: Specifies the build configuration.
   * **wwwrootDir**: Specifies the path to the wwwroot directory.
   * **dotnetSdkVersion**: Specifies the .NET SDK version to use.

   To reference these variables, use the **$()** syntax just as you do for built-in variables. Here's the step that runs node-Sass to convert Sass files to CSS. To get the path to the wwwroot directory, it references the **wwwrootDir** variable.

   ```yml
   - script: './node_modules/.bin/node-sass $(wwwrootDir) --output $(wwwrootDir)'
     displayName: 'Compile Sass assets'
   ```

   The script command uses the variable to define both the source directory for Sass files and the directory in which to write CSS files. It also uses the variable to define the task name that's shown in the user interface.

2. From the integrated terminal, add azure-pipelines.yml to the index, commit the change, and push the change to GitHub.

   ```bash
   git add azure-pipelines.yml
   git commit -m "Refactor common variables"
   git push origin build-pipeline
   ```

3. From Azure Pipelines, trace the build through each of the steps.

   You'll see that the variables are replaced with their values when the build runs. For example, here's the **UseDotNet@2** task that sets the .NET SDK version to use.

   *Screenshot of Azure Pipelines showing the .NET SDK task running in the pipeline.*

4. As before, to see the artifact when the build completes, you can navigate to the build summary.

Congratulations! You've successfully used Azure Pipelines and created your first build artifact.


# 1.8 Exercise - Build multiple configurations by using templates

## Choose your training module development environment

In the previous exercises, you implemented a pipeline that builds the Space Game website. You started with a script that performed each build action and mapped each action to its corresponding pipeline task. The pipeline's output is a .zip file that contains the compiled web app.

In this exercise, you'll use a template to define build tasks that can build any configuration defined in the project file. Templates let you define your logic one time and then reuse it several times. Templates combine the content of multiple YAML files into a single pipeline.

> **Tip**
> 
> This step in the module is optional. If you don't want to learn about templates at this time, proceed to the next step, Clean up your Azure DevOps environment. For more information about templates, see Template types & usage.

Let's begin by checking in with Mara and Amita.

## The demo

Mara, excited to share her results, tracks down Amita to show her the build pipeline.

**Amita:** I'm impressed you got this working so quickly! In fact, I was just coming to see you because I got an email telling me the build was ready. Thank you! I see that the pipeline builds only the Release configuration. We also use Debug builds so we can capture additional information if the app crashes. Can we add that?

**Mara:** Absolutely. I forgot to consider Debug builds when I set this up. How about we sit down together and add it?

**Amita:** You showed me the YAML file that defines the build steps, but I'm not sure I know how to modify it.

**Mara:** That's OK. You can watch while I type. We can think through it together.

## How might you define both build configurations?

Consider the following tasks that build and publish the Space Game web project's Release configuration. (Don't add this code to your azure-pipelines.yml file.)

```yml
- task: DotNetCoreCLI@2
  displayName: 'Build the project - Release'
  inputs:
    command: 'build'
    arguments: '--no-restore --configuration Release'
    projects: '**/*.csproj'

- task: DotNetCoreCLI@2
  displayName: 'Publish the project - Release'
  inputs:
    command: 'publish'
    projects: '**/*.csproj'
    publishWebProjects: false
    arguments: '--no-build --configuration Release --output $(Build.ArtifactStagingDirectory)/Release'
    zipAfterPublish: true
```

To build the Debug configuration, you might repeat these two tasks, but replace Release with Debug.

Doing so would give you the result you're looking for, but what happens when your build becomes more complex or your requirements change? You'd need to manually locate and change both variations of each build task. After you added the additional build requirements, you'd also need to create two tasks, one for the Debug configuration and one for Release, to satisfy those requirements.

A better solution is to use a template.

## What are templates?

A template lets you define common build tasks once and reuse those tasks multiple times.

You'll call a template from the parent pipeline as a build step. You can pass parameters into a template from the parent pipeline.

Mara can define tasks to build and publish the app as a template, and then apply that template to each configuration she needs.

## Define the template

Remember that a template lets you define common build tasks one time and reuse those tasks multiple times. You call a template from its parent template as a build step and pass parameters into a template from the parent pipeline.

You'll now create a template that can build any configuration that's defined in the project file.

1. From the Visual Studio Code integrated console, at the root of your project, create a **templates** directory.

   ```bash
   mkdir templates
   ```

   In practice, you can put a template file in any location. You don't need to put them in the templates directory.

2. In Visual Studio Code, select **File > New File**. Next, to save the blank file as **build.yml** in your project's **templates** directory, select **File > Save**. An example would be ~/mslearn-tailspin-spacegame-web/templates.

   > **Important**
   > 
   > As before, in Windows, in the **Save as type** list, select **YAML**.

3. In Visual Studio Code, add this code to build.yml:

   ```yml
   parameters:
     buildConfiguration: 'Release'

   steps:
   - task: DotNetCoreCLI@2
     displayName: 'Build the project - ${{ parameters.buildConfiguration }}'
     inputs:
       command: 'build'
       arguments: '--no-restore --configuration ${{ parameters.buildConfiguration }}'
       projects: '**/*.csproj'

   - task: DotNetCoreCLI@2
     displayName: 'Publish the project - ${{ parameters.buildConfiguration }}'
     inputs:
       command: 'publish'
       projects: '**/*.csproj'
       publishWebProjects: false
       arguments: '--no-build --configuration ${{ parameters.buildConfiguration }} --output $(Build.ArtifactStagingDirectory)/${{ parameters.buildConfiguration }}'
       zipAfterPublish: true
   ```

   These tasks look like the ones you defined earlier to build and publish the app; but in a template, you work with input parameters differently than you work with normal variables. Here are two differences:

   * In a template file, use the **parameters** section instead of **variables** to define inputs.
   * In a template file, use **${{ }}** syntax instead of **$()** to read a parameter's value. When you read a parameter's value, you'll include the **parameters** section in its name. For example, **${{ parameters.buildConfiguration }}**.

## Call the template from the pipeline

You'll now call the template that you just built from the pipeline. You'll do so one time for the Debug configuration, then repeat the process for the Release configuration.

1. In Visual Studio Code, modify azure-pipelines.yml as you see here:

   ```yml
   trigger:
   - '*'

   pool:
     name: 'Default' #replace if needed with name of your agent pool

   variables:
     buildConfiguration: 'Release'
     wwwrootDir: 'Tailspin.SpaceGame.Web/wwwroot'
     dotnetSdkVersion: '6.x'

   steps:
   - task: UseDotNet@2
     displayName: 'Use .NET SDK $(dotnetSdkVersion)'
     inputs:
       version: '$(dotnetSdkVersion)'

   - task: Npm@1
     displayName: 'Run npm install'
     inputs:
       verbose: false

   - script: './node_modules/.bin/node-sass $(wwwrootDir) --output $(wwwrootDir)'
     displayName: 'Compile Sass assets'

   - task: gulp@1
     displayName: 'Run gulp tasks'

   - script: 'echo "$(Build.DefinitionName), $(Build.BuildId), $(Build.BuildNumber)" > buildinfo.txt'
     displayName: 'Write build info'
     workingDirectory: $(wwwrootDir)

   - task: DotNetCoreCLI@2
     displayName: 'Restore project dependencies'
     inputs:
       command: 'restore'
       projects: '**/*.csproj'

   - template: templates/build.yml
     parameters:
       buildConfiguration: 'Debug'

   - template: templates/build.yml
     parameters:
       buildConfiguration: 'Release'

   - task: PublishBuildArtifacts@1
     displayName: 'Publish Artifact: drop'
     condition: succeeded()
   ```

   This file looks like the original, except that it replaces the build and publish tasks with calls to the template that does the same tasks.

   You'll see that the template is called one time for each configuration. To pass the configuration name to the template, each template task uses the **parameters** argument.

## Run the pipeline

You'll now push your changes to GitHub and see the pipeline run.

1. From the integrated terminal, add azure-pipelines.yml and templates/build.yml to the index, commit the changes, and push the changes up to GitHub.

   ```bash
   git add azure-pipelines.yml templates/build.yml
   git commit -m "Support build configurations"
   git push origin build-pipeline
   ```

2. From Azure Pipelines, trace the build through each of the steps as you did earlier.

   As the pipeline runs, you'll see that the process expands the tasks within the template. The tasks that build and publish the project are run two times, once for each build configuration.

   *Screenshot of Azure Pipelines showing the expanded template tasks. Included are build and publish tasks for both the Debug and Release configurations.*

   ![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/8-template-tasks.png)

4. When the build completes, go back to the summary page and select the published artifact as you did before. Expand the **drop** folder.

   You'll see that the pipeline produces a .zip file for both the Debug configuration and the Release configuration.

   *Screenshot of Azure Pipelines showing the packaged application for both Debug and Release configurations.*

![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/8-artifacts-explorer.png)


# 1.9  Exercise - Clean up your Azure DevOps environment


## Choose your training module development environment

**Local development environment using a Microsoft-hosted agent** | **GitHub Codespaces development environment using a self-hosted agent**

You're all done with the tasks for this module. You'll now clean up your Azure DevOps environment.

> **Important**
> 
> This page has important cleanup steps. Cleaning up helps ensure that you don't run out of free GitHub Codespaces **included usage hours and storage** (**charges may apply if you exceed the free tier - check your usage**). Be sure to do the cleanup steps even if you don't complete this module.

## Disable the pipeline or delete your project

To create a clean environment for the duration of the module, each module in this learning path provides a template that you can run.

Running multiple templates gives you multiple Azure Pipelines projects, each pointing to the same GitHub repository. This can trigger multiple pipelines to run each time you push a change to your GitHub repository, which can cause you to run out of free build minutes on our hosted agents. That's why it's important that you disable or delete your pipeline before moving on to the next module.

Select one of the following options:

### Option 1: Delete the Azure DevOps project

This option deletes your Azure DevOps project, including what's on Azure Boards and your build pipeline. In future modules, you'll be able to run another template that brings up a new project in a state where this one leaves off. Select this option if you don't need your Azure DevOps project for future reference.

> **Tip**
> 
> This project isn't needed for subsequent training modules, as each module includes a template that creates a new project that includes the required steps from previous modules.

To delete the project:

1. In Azure DevOps, go to your project. Earlier, we recommended that you name the project *Space Game - web - Pipeline*.

2. Select **Project settings** in the bottom left corner.

3. In the **Project details** area, scroll to the bottom, and select **Delete**.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-delete-project.png)

4. In the window that appears, enter the project name, and select **Delete** a second time.

Your project is now deleted.

### Option 2: Disable the pipeline

This option disables the pipeline so that it doesn't process further build requests. You can re-enable the build pipeline later if you want to. Select this option if you want to keep your Azure DevOps project and your build pipeline for future reference.

To disable the pipeline:

1. In Azure Pipelines, navigate to your pipeline.

2. From the dropdown, select **Settings**.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-pipelines-settings-button.png)

3. Under **Processing of new run requests**, select **Disabled**, then select **Save**.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-a-build-pipeline/media/9-delete-codespace.png)


Your pipeline will no longer process build requests.

## Delete your GitHub Codespace

1. In your forked GitHub repository, select **Code**.

2. Select the **Codespaces** tab.

3. Select **...** by your Codespace, and choose **Delete**.

4. Select **Delete** again to confirm deletion.



# 1.10 Summary

## Choose your training module development environment

**Local development environment using a Microsoft-hosted agent** | **GitHub Codespaces development environment using a self-hosted agent**

Great work! You covered a lot of ground in this module. You and the team have come a long way in creating an automated pipeline. You learned how to map script commands on a build server to automated pipeline tasks that run when you push code to GitHub. The result of the pipeline is a *.zip* file that contains the built *Space Game* web app.

Along the way, you learned how to use variables to simplify your code.

You also learned how to use templates to encapsulate sets of tasks that you can repeat throughout your build process. You used a template to build the app's Debug and Release configurations.

Lastly, you practiced your Git skills by pushing commits to a branch and building from that branch. Working from a branch lets you work in isolation from the main code base. That helps you experiment and try new things without affecting the main development branch, `main`.

Keep in mind that this build configuration focuses on building a .NET app. The tasks you choose will depend on the kind of app you're building, the tools you use to build it, and the programming language in which it's written.

When you approach your own builds, it's a good idea to start by making sure you can build the app from scratch from the terminal or from a Bash or PowerShell script. From there, you can map each command to a pipeline task that accomplishes the same thing.

When you create your own pipeline, you have two choices: the visual designer or YAML files. If you choose the visual designer to get started, you can switch to the YAML version of your configuration to learn how each task is structured.

> **Note**
> 
> At this point, you have a build artifact that you could deploy to a QA or production environment. For the rest of this learning path, you'll focus on using Azure Pipelines to build and test your software. You'll learn how to use Azure Pipelines to deploy your apps in a future learning path.

## Additional resources

To further your understanding, see the following additional resources:

If you're looking for a more academic approach, *Continuous Delivery* by Jez Humble and David Farley is a great starting point.

### Learn YAML

If you're interested in learning YAML, check out Learn YAML in Y minutes. You can then review the Azure Pipelines YAML schema reference to get a better sense of how pipelines are structured.

### Explore the documentation

We provide complete reference documentation that goes deeper into the concepts and tasks we described here. The documentation also provides starter guides for many app types, like Java, C++, and Node.js.

The Build and release tasks section can help you map your existing build commands to built-in tasks.

### Create your own build pipeline

In this module, you created the pipeline from Azure DevOps. You can repeat a similar process to create your own pipeline. You can also create a pipeline from the GitHub Marketplace app.


# 2 Implement a code workflow in your build pipeline by using Git and GitHub

Collaborate with others and merge only the highest quality code.


# 2.1 Introduction

In **Create a build pipeline with Azure Pipelines**, you created a basic but complete build configuration for an ASP.NET Core web application.

In this module, you'll extend this build configuration by implementing a code-collaboration strategy that uses Git and GitHub.

Collaboration is a key DevOps value. Developers need a way to work with source code and share their code revisions with others. A source-control system facilitates cooperation among developers and more frequent deployments to improve the product.

Azure DevOps works with different kinds of source control, but many Azure DevOps organizations choose to use Git. Git is a distributed system in which all contributors have their own copy of the work. In this module, you'll use the branching and merging capabilities of Git to more efficiently work with other developers. You'll also use GitHub, a central location for teams to host their projects and share their work.

## Learning objectives

After completing this module, you'll be able to:

* Collaborate with others by choosing an appropriate branching and merging strategy.
* Add a badge to your GitHub repository to show the status of the latest build.
* Add a dashboard widget to help visualize your build history.
* Set up a rule on your GitHub repository to require a review.

## Prerequisites

The modules in this learning path form a progression. Information in one module is the basis for further learning in the next module.

To follow the progression from the beginning, first complete the **Get started with Azure DevOps** learning path.

We also recommend you start at the beginning of this learning path, **Build applications with Azure DevOps**.

If you want to complete only this module, you need to set up a development environment on your Windows, macOS, or Linux system. You'll need these prerequisites:

* An Azure DevOps organization
* A GitHub account
* Visual Studio Code
* .NET 6.0 SDK
* Git

You can get started with Azure DevOps for free.

This environment lets you complete the exercises in this and future modules. You can also use it to apply your new skills to your own projects.

**Note:** Azure Pipelines support a vast array of **languages and application types**. In this module, you'll be working with a .NET application but you can apply the patterns you learn here to your own projects that use your favorite programming languages and frameworks.

## Meet the team

In earlier modules, you met the *Space Game* web team at Tailspin Toys. The *Space Game* web team is here again to work with you in this module:

**Andy** is the development lead.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/andy.png)

**Amita** is in QA.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/amita.png)

**Mara** just joined as a developer and reports to Andy.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/mara.png)

Mara has prior experience with DevOps and is helping the team adopt a more streamlined process that uses Azure DevOps.



# 2.2 Choose a code-flow strategy

It's important to choose a code-flow strategy that fits the way your team works. You have several strategies to consider. At the end of the module, you can explore options. The Tailspin web team decides to develop a code-flow strategy that's based on Git and GitHub.

When Mara set up Azure Boards, she and the team identified a few initial tasks to address. One task was to create a Git-based workflow.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/build-initial-tasks.png)

Let's listen in on the team as they work out a better way to collaborate. Currently, they're using a centralized version-control system, but the plan is to move to Git, a distributed system.

Mara is diligently working on her assigned features when Andy walks in.

**Andy:** Hi Mara. In the leadership meeting this morning, it was brought up that our team and the game-development team are using different version-control systems. To streamline how we share resources between teams, we've been asked to move to a distributed version-control system that can better handle the collaboration.

**Mara:** That's good to know. If you remember, we put it on our board. Currently, we're using a centralized version-control system. It works great for us now, but I agree that a distributed version-control system is a better choice when we start to share between teams and our team gets bigger. It's also a task on our board to increase visibility so that all the stakeholders know what everyone is doing. I think a distributed source-control system like Git would also help.

**Andy:** I've been wanting to try Git for a while. I never seem to have the time. Is it difficult to learn or set up? If it seems reasonable, maybe we could work on it now. I'm tired of always putting things off. And it would be nice to be able to see what everyone is doing and to have access to the entire repository. OK, what's it all about?

**Mara:** Let me explain it, and then you can decide if it sounds like something we want to implement right away.

Mara and Andy move to the whiteboard for a discussion on version control.

## What is Git and distributed version control?

![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/2-whiteboard-centralized-vs-distributed-drawing.png)

**Mara:** The drawing on the left is centralized version control, like what we're using now. We have a central version of the code base ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-01.png) in Team Foundation Version Control (TFVC) that everyone uses. We each work on the files we need to change and then merge them back into the main repository when we're finished with them.

**Andy:** Yes, and that's working for us. Well, except when I was blocked that time when a breaking change got merged into the central repo.

**Mara:** Right! You were blocked. ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-02.png) We could use a branching strategy with TFVC to solve the blocking issue, but in our current configuration, merging might get a bit more complicated. And when we had that breaking change ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-03.png), no one could get any work done until we got that resolved. That problem is always lurking, because we're all using the same copy of the code.

On the right is a drawing of distributed version control. We still have a central repository ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-04.png) that's the stable version of the code base, but each developer has their own copy of it from which to work. This frees us up to experiment and try various approaches without affecting the central repository.

Distributed version control also ensures that only the working code ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-05.png) is merged into the central repository. We could even set it up so that code can't be merged until it's reviewed.

What's cool about Azure DevOps is that it works well both with centralized version-control systems and distributed version-control systems.

**Andy:** What happens when more than one person changes the same file?

**Mara:** Often, Git can merge multiple changes automatically. Of course, we want to always make sure that the combination of changes results in code that works. When Git can't automatically merge changes, it marks the conflicts directly in the files so that a human can choose which changes to accept.

**Andy:** Right now, our code is stored on our own server. If we move to using distributed version control, where will the code be stored?

**Mara:** I'm glad you asked. That's where hosting comes in.

## Where can I host my repository?

**Mara:** When we're deciding where to host our repositories, we have a few options. For example, we can host them on a local server, in Bitbucket, or in GitHub. Bitbucket and GitHub are web-based hosting solutions. We can access them from anywhere.

**Andy:** Have you used either of them?

**Mara:** I've used GitHub in the past. It has features that are important to developers, like easy access to change logs and version-control features from either the command line or the online portal.

**Andy:** So how does Git work?

## How do I work with Git?

**Mara:** Like I mentioned before, with distributed systems, developers are free to access any file they need without affecting other developers' work because they have their own copy of the repository. A clone is your local copy of a repository.

When we work on a feature or a bug fix, we usually want to try out different approaches until we find the best solution. However, trying out code on your copy of the main code base isn't a good idea, because you might not want to keep the first few tries.

To give you a better option, Git has a feature called branching, where you can maintain as many copies as you want and merge back only the one you want to keep. This keeps the main branch stable.

**Andy:** I get the concepts so far. How do I check in my code?

## How do my local changes get up to the main code base?

**Mara:** In Git, the default branch, or trunk, is typically called main.

When you feel your code is ready to be merged into the main branch in the central repository that's shared by all developers, you create what's called a pull request. When you create a pull request, you're telling the other developers that you have code ready to review, and you want it merged into the main branch. When your pull request is approved and then merged, it becomes part of the central code base.

## What does a branching workflow look like?

**Step 1:** When you begin to work on a new feature or bug fix, the first thing you want to do is ensure that you're starting with the latest stable code base. To do this, you can synchronize your local copy of the main branch with the server's copy. This pulls into your local copy all other developer changes that were pushed to the main branch on the server since your last sync.

![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/2-github-paths-1.png)

**Step 2:** To ensure that you're working only on your copy of the code, you create a new branch just for that feature or bug fix. As you can imagine, having many branches for all the things you're doing might get hard to remember, so using a good naming convention is critical.

Before you make changes to a file, you check out a new branch so that you know you're working on the files from that branch and not from a different branch. You can switch branches anytime by checking out that branch.

![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/2-github-paths-2.png)

**Step 3:** You're now safe to make whatever changes you want because these changes are only in your branch. As you work, you can commit your changes to your branch to ensure that you don't lose any work. This also provides a way to roll back any changes you've made to earlier versions. Before you can commit changes, you need to stage your files so that Git knows which ones you're ready to commit.

![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/2-github-paths-3.png)

**Step 4:** The next step is to push, or upload, your local branch up to the remote repository (such as GitHub) so that others can see what you're working on. Don't worry, this won't merge your changes yet. You can push up your work as often as you'd like. In fact, that's a good way to back up your work or allow yourself to work from multiple computers.

![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/2-github-paths-4.png)

**Step 5:** This step is a common one but not required. When you're satisfied that your code is working as you want it to, you can pull, or merge, the remote main branch back into your local main branch. Changes have been taking place there that your local main branch doesn't have yet. After you've synchronized the remote main branch with yours, merge your local main branch into your working branch and test your build again.

This process helps ensure that your feature works with the latest code. It also helps ensure that your work will integrate smoothly when you submit your pull request.

![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/2-github-paths-5.png)

**Step 6:** Your local code now needs to be committed and pushed up to the hosted repository. This is the same as steps 3 and 4.

![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/2-github-paths-6.png)

**Step 7:** You're finally ready to propose your changes to the remote main branch. To do this, you begin a pull request. When configured in Azure Pipelines or another CI/CD system, this step triggers the build process, and you can watch your changes move through the pipeline. After the build succeeds and others approve your pull request, your code can be merged into the remote main branch. (It's still up to a human to merge the changes.)

![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/2-github-paths-7.png)

**Andy:** This all looks complicated and hard to learn.

**Mara:** Git can seem intimidating because it's so powerful, but after you get the hang of the flow, it starts to feel natural.

You'll use only a few commands daily. Here's a summary:

| Category | To perform this task | Use this command |
|----------|---------------------|------------------|
| Repository management | Create a Git repository | `git init` |
| | Download a remote repository | `git clone` |
| Branch | Create a branch | `git checkout` |
| Stage and commit changes | See which files have been changed | `git status` |
| | Stage files to commit | `git add` |
| | Commit files to your branch | `git commit` |
| Remote synchronization | Download a branch from a remote repository | `git pull` |
| | Upload a branch to a remote repository | `git push` |

**Andy:** That sounds like a great starting point. I can definitely handle that. I can learn more advanced commands as I need them.

---

## Check your knowledge

### 1. Which type of version control enables you to work from your own copy of the main repository?

- [ ] Centralized version control
- [ ] Team Foundation Version Control
- [x] **Distributed version control**

### 2. A Git branch is used to:

- [ ] Copy only the part of the repository that you want to work with.
- [x] **Make changes and experiment with the codebase without affecting other developers' work.**
- [ ] Create an entirely new repository that's not connected to the main repository.

### 3. The git pull command:

- [ ] Uploads changes from your local repository to the remote repository.
- [x] **Downloads and merges the latest changes from the remote repository into your local repository.**

---

## Відповіді на запитання:

**1. Правильна відповідь: Distributed version control**
Розподілена система контролю версій дозволяє кожному розробнику мати власну повну копію репозиторію, з якою можна працювати незалежно від інших.

**2. Правильна відповідь: Make changes and experiment with the codebase without affecting other developers' work.**
Git гілки створюються для ізоляції змін і експериментів від основної кодової бази та роботи інших розробників.

**3. Правильна відповідь: Downloads and merges the latest changes from the remote repository into your local repository.**
Команда `git pull` завантажує та об'єднує останні зміни з віддаленого репозиторію в локальний репозиторій.


# 2.3 Exercise - Set up your Azure DevOps environment

In this unit, you'll ensure that your Microsoft Azure DevOps organization is set up to complete the rest of this module.

To do this, you'll:

* Set up an Azure DevOps project for this module.
* Move the work item for this module on Azure Boards to the Doing column.
* Ensure that your project is set up locally so that you can push changes to the pipeline.

## Get the Azure DevOps project

Here, you'll ensure that your Azure DevOps organization is set up to complete the rest of this module. You do this by running a template that creates a project for you in Azure DevOps.

The modules in this learning path form a progression, where you follow the Tailspin web team through their DevOps journey. For learning purposes, each module has an associated Azure DevOps project.

### Run the template

Run a template that sets up your Azure DevOps organization.

1. Get and run the ADOGenerator project in Visual Studio or the IDE of your choice.

2. When prompted to **Enter the template number from the list of templates**, enter **23** for **Implement a code workflow in your build pipeline using Git and GitHub**, then press Enter.

3. Choose your authentication method. You can set up and use a Personal Access Token (PAT) or use device login.

   **Note:** If you set up a PAT, make sure to authorize the necessary scopes. For this module, you can use Full access, but in a real-world situation, you should ensure you grant only the necessary scopes.

4. Enter your Azure DevOps organization name, then press Enter.

5. If prompted, enter your Azure DevOps PAT, then press Enter.

6. Enter a project name such as **Space Game - web - Workflow**, then press Enter.

7. Once your project is created, go to your Azure DevOps organization in your browser (at `https://dev.azure.com/<your-organization-name>/`) and select the project.

**Important:** The **Clean up your Azure DevOps environment** page in this module contains important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes. Be sure to perform the cleanup steps even if you don't complete this module.

### Fork the repository

If you haven't already, fork the mslearn-tailspin-spacegame-web repository.

1. On GitHub, go to the **mslearn-tailspin-spacegame-web** repository.

2. Select **Fork** at the top-right of the screen.

3. Choose your GitHub account as the Owner, then select **Create fork**.

### Set your project's visibility

Initially, your fork of the Space Game repository on GitHub is set to public while the project created by the Azure DevOps template is set to private. A public repository on GitHub can be accessed by anyone, while a private repository is only accessible to you and the people you choose to share it with. Similarly, on Azure DevOps, public projects provide read-only access to non-authenticated users, while private projects require users to be granted access and authenticated to access the services.

At the moment, it is not necessary to modify any of these settings for the purposes of this module. However, for your personal projects, you must determine the visibility and access you wish to grant to others. For instance, if your project is open source, you may choose to make both your GitHub repository and your Azure DevOps project public. If your project is proprietary, you would typically make both your GitHub repository and your Azure DevOps project private.

Later on, you may find the following resources helpful in determining which option is best for your project:

* Use private and public projects
* Change project visibility to public or private
* Setting repository visibility

## Move the work item to Doing

In this section, you'll assign yourself a work item that relates to this module on Azure Boards. You'll also move the work item to the **Doing** state. In practice, you and your team would create work items at the start of each sprint or work iteration.

Assigning work in this way gives you a checklist from which to work. It gives others on your team visibility into what you're working on and how much work is left. It also helps the team enforce work in process (WIP) limits so that the team doesn't take on too much work at one time.

Recall that the team settled on these seven top issues:

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/build-all-tasks.png)

**Note:** Within an Azure DevOps organization, work items are numbered sequentially. In your project, the number that's assigned to each work item might not match what you see here.

Here, you'll move the second item, **Create a Git-based workflow**, to the **Doing** column and assign yourself to the work item.

Recall that **Create a Git-based workflow** relates to moving to a code workflow that enables better collaboration among team members.

![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/3-work-item-details.png)

To set up the work item:

1. In Azure DevOps, select **Boards** in the left pane, then select **Boards**.

  ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-boards-menu.png)

2. In the **Create a Git-based workflow** work item, select the **To Do** down arrow, and then assign the work item to yourself.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-boards-down-chevron.png)

4. Drag the work item from the **To Do** column to the **Doing** column.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/3-azure-boards-wi2-doing.png)

At the end of this module, after you've completed the task, you'll move the item to the **Done** column.

## Set up the project locally

Here, you load the Space Game project in Visual Studio Code, configure Git, clone your repository locally, and set the upstream remote so that you can download the starter code.

**Note:** If you're already set up with the mslearn-tailspin-spacegame-web project locally, you can move to the next section.

### Open the integrated terminal

Visual Studio Code comes with an integrated terminal, so you can edit files and work from the command line all in one place.

1. Start Visual Studio Code.

2. On the **View** menu, select **Terminal**.

3. In the dropdown list, select **bash**. If you're familiar with another Unix shell that you prefer to use, such as Zsh, select that shell instead.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/vscode-terminal-bash.png)

The terminal window lets you choose any shell that's installed on your system, like Bash, Zsh, and PowerShell.

Here you'll use Bash. Git for Windows provides Git Bash, which makes it easy to run Git commands.

**Note:** On Windows, if you don't see Git Bash listed as an option, make sure you've installed Git, and then restart Visual Studio Code.

4. Run the `cd` command to navigate to the directory you want to work from, like your home directory (`~`). You can choose a different directory if you want.

   ```bash
   cd ~
   ```

### Configure Git

If you're new to Git and GitHub, you first need to run a few commands to associate your identity with Git and authenticate with GitHub.

**Set up Git** explains the process in greater detail.

At a minimum, you'll need to complete the following steps. Run these commands from the integrated terminal:

1. Set your username.
2. Set your commit email address.
3. Cache your GitHub password.

**Note:** If you're already using two-factor authentication with GitHub, create a personal access token and use your token in place of your password when prompted later.

Treat your access token like you would a password. Keep it in a safe place.

### Set up your project in Visual Studio Code

In this part, you clone your fork locally so that you can make changes and build out your pipeline configuration.

**Note:** If you receive any errors about filenames being too long when you clone your repository, try cloning the repository in a folder that doesn't have a long name or is deeply nested.

#### Clone your fork locally

You now have a copy of the Space Game web project in your GitHub account. Now you'll download, or clone, a copy to your computer so you can work with it.

A clone, just like a fork, is a copy of a repository. When you clone a repository, you can make changes, verify they work as you expect, and then upload those changes back to GitHub. You can also synchronize your local copy with changes other authenticated users have made to GitHub's copy of your repository.

To clone the Space Game web project to your computer:

1. Go to your fork of the Space Game web project (mslearn-tailspin-spacegame-web) on GitHub.

2. Select **Code**. Then, from the **HTTPS** tab, select the button next to the URL that's shown to copy the URL to your clipboard.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/github-clone-button.png)

4. In Visual Studio Code, go to the terminal window.

5. In the terminal, move to the directory you want to work from, like your home directory (`~`). You can choose a different directory if you want.

   ```bash
   cd ~
   ```

6. Run the `git clone` command. Replace the URL that's shown here with the contents of your clipboard:

   ```bash
   git clone https://github.com/your-name/mslearn-tailspin-spacegame-web.git
   ```

7. Move to the mslearn-tailspin-spacegame-web directory. This is the root directory of your repository.

   ```bash
   cd mslearn-tailspin-spacegame-web
   ```

#### Set the upstream remote

A remote is a Git repository where team members collaborate (like a repository on GitHub). Here you list your remotes and add a remote that points to Microsoft's copy of the repository so that you can get the latest sample code.

1. Run this `git remote` command to list your remotes:

   ```bash
   git remote -v
   ```

   You see that you have both fetch (download) and push (upload) access to your repository:

   ```
   origin  https://github.com/username/mslearn-tailspin-spacegame-web.git (fetch)
   origin  https://github.com/username/mslearn-tailspin-spacegame-web.git (push)
   ```

   Origin specifies your repository on GitHub. When you fork code from another repository, it's common to name the original remote (the one you forked from) as upstream.

2. Run this `git remote add` command to create a remote named upstream that points to the Microsoft repository:

   ```bash
   git remote add upstream https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web.git
   ```

3. Run `git remote` a second time to see the changes:

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

#### Open the project in the file explorer

In Visual Studio Code, your terminal window points to the root directory of the Space Game web project. To view its structure and work with files, from the file explorer, you'll now open the project.

The easiest way to open the project is to reopen Visual Studio Code in the current directory. To do so, run the following command from the integrated terminal:

```bash
code -r .
```

You see the directory and file tree in the file explorer.

Reopen the integrated terminal. The terminal places you at the root of your web project.

If the `code` command fails, you need to add Visual Studio Code to your system PATH. To do so:

1. In Visual Studio Code, select **F1** or select **View > Command Palette** to access the command palette.
2. In the command palette, enter **Shell Command: Install 'code' command in PATH**.
3. Repeat the previous procedure to open the project in the file explorer.

You're now set up to work with the Space Game source code and your Azure Pipelines configuration from your local development environment.



# 2.4 Exercise - Create a pull request

In this unit, you'll practice the process of submitting a pull request and merging your changes into the main branch so that everyone can benefit from your work.

In **Create a build pipeline with Azure Pipelines**, you created a Git branch named **build-pipeline**, where you defined a basic build pipeline for the Space Game website. Recall that your build definition is in a file named **azure-pipelines.yml**.

Although your branch produces a build artifact, that work exists only on the **build-pipeline** branch. You need to merge your branch into the **main** branch.

Recall that a pull request tells the other developers that you have code ready to review, if necessary, and you want your changes merged into another branch, such as the **main** branch.

Before we start, let's check in with Mara and Andy.

**Andy:** Hi, Mara. I know you've got a build pipeline running on Azure. I'm adding a feature to the website, and I want to see the build process for myself. Are we ready to do that?

**Mara:** Absolutely. I created the pipeline on a branch. Why don't we create a pull request and get it merged into main so you can use the pipeline, too?

**Andy:** Sounds great. Let's take a look.

## Create a branch and add starter code

Although you could use the build pipeline you built in the previous module, let's create a new branch named **code-workflow**. This branch is based on **main**, so you can practice the process from the beginning.

1. In Visual Studio Code, open the integrated terminal.

2. Switch to the **main** branch:

   ```bash
   git checkout main
   ```

3. Ensure that you have the latest version of the code from GitHub:

   ```bash
   git pull origin main
   ```

4. Create a branch named **code-workflow**:

   ```bash
   git checkout -B code-workflow
   ```

   The **-b** argument specifies to create a new branch if it doesn't exist. Omit the **-b** argument when you want to switch to an existing branch.

   By default, your new branch builds on the previous branch from where you ran the **git checkout** command. Here, the parent branch is **main**, but the parent branch can be another one, such as a feature branch someone else started that you want to build on or experiment with.

   It's now safe to make whatever changes you need, because you're on your own local branch. If you want to see which branch you're on, run **git branch -v**.

5. From the file explorer, open **azure-pipelines.yml** and replace its contents with this:

   ```yml
   trigger:
   - '*'

   pool:
     vmImage: 'ubuntu-20.04'
     demands:
     - npm

   variables:
     buildConfiguration: 'Release'
     wwwrootDir: 'Tailspin.SpaceGame.Web/wwwroot'
     dotnetSdkVersion: '6.x'

   steps:
   - task: UseDotNet@2
     displayName: 'Use .NET SDK $(dotnetSdkVersion)'
     inputs:
       version: '$(dotnetSdkVersion)'

   - task: Npm@1
     displayName: 'Run npm install'
     inputs:
       verbose: false

   - script: './node_modules/.bin/node-sass $(wwwrootDir) --output $(wwwrootDir)'
     displayName: 'Compile Sass assets'

   - task: gulp@1
     displayName: 'Run gulp tasks'

   - script: 'echo "$(Build.DefinitionName), $(Build.BuildId), $(Build.BuildNumber)" > buildinfo.txt'
     displayName: 'Write build info'
     workingDirectory: $(wwwrootDir)

   - task: DotNetCoreCLI@2
     displayName: 'Restore project dependencies'
     inputs:
       command: 'restore'
       projects: '**/*.csproj'

   - task: DotNetCoreCLI@2
     displayName: 'Build the project - $(buildConfiguration)'
     inputs:
       command: 'build'
       arguments: '--no-restore --configuration $(buildConfiguration)'
       projects: '**/*.csproj'

   - task: DotNetCoreCLI@2
     displayName: 'Publish the project - $(buildConfiguration)'
     inputs:
       command: 'publish'
       projects: '**/*.csproj'
       publishWebProjects: false
       arguments: '--no-build --configuration $(buildConfiguration) --output $(Build.ArtifactStagingDirectory)/$(buildConfiguration)'
       zipAfterPublish: true

   - task: PublishBuildArtifacts@1
     displayName: 'Publish Artifact: drop'
     condition: succeeded()
   ```

   This configuration resembles the basic one you created in the previous module. For brevity, it builds only your project's Release configuration.

## Push your branch to GitHub

Here, you'll push your **code-workflow** branch to GitHub and watch Azure Pipelines build the application.

1. In the terminal, run **git status** to see what uncommitted work exists on your branch:

   ```bash
   git status
   ```

   You'll see that **azure-pipelines.yml** has been modified. You'll commit that to your branch shortly, but you first need to ensure that Git is tracking this file which is called staging the file.

   Only staged changes are committed when you run **git commit**. Next, you run the **git add** command to add **azure-pipelines.yml** to the staging area, or index.

2. Run the following **git add** command to add **azure-pipelines.yml** to the staging area:

   ```bash
   git add azure-pipelines.yml
   ```

3. Run the following **git commit** command to commit your staged file to the **code-workflow** branch:

   ```bash
   git commit -m "Add the build configuration"
   ```

   The **-m** argument specifies the commit message. The commit message becomes part of a changed file's history. It helps reviewers understand the change, and it helps future maintainers understand how the file changed over time.

   **Tip:** The best commit messages complete the sentence, "If you apply this commit, you will ..."

   If you omit the **-m** argument, Git brings up a text editor where you can detail the change. This option is useful when you want to specify a commit message that spans multiple lines. The text up to the first blank line specifies the commit title.

4. Run this **git push** command to push, or upload, the **code-workflow** branch to your repository on GitHub:

   ```bash
   git push origin code-workflow
   ```

5. As an optional step, go to your project in Azure Pipelines and trace the build as it runs.

   This build is called a CI build. Your pipeline configuration uses what's called a trigger to control which branches participate in the build process. Here, "*" specifies all branches.

   ```yml
   trigger:
   - '*'
   ```

   Later, you'll see how to control your pipeline configuration to build from only the branches that you need.

   You'll see that the build completes successfully and produces an artifact that contains the built web application.

## Create a pull request

Here, you'll create a pull request for your branch:

1. In a browser, sign in to GitHub.

2. Go to your **mslearn-tailspin-spacegame-web** repository.

3. In the **Branch** drop-down list, select your **code-workflow** branch.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/4-github-select-branch.png)

5. To start your pull request, select **Contribute** and then **Open pull request**.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/4-github-new-pr.png)

6. Ensure that the base specifies your forked repository and not the Microsoft repository.

   Your selection looks like this:

   ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/4-github-set-base.png)

   **Important:** This step is important because you can't merge your changes into the Microsoft repository. Ensure that the base repository points to your GitHub account and not MicrosoftDocs.

   If you end up with a pull request against MicrosoftDocs, close the pull request and repeat these steps.

   This process involves an extra step because you're working from a forked repository. When you work directly with your own repository, and not a fork, your **main** branch is selected by default.

8. Enter a title and description for your pull request.

   **Title:**
   ```
   Configure Azure Pipelines
   ```

   **Description:**
   ```
   This pipeline configuration builds the application and produces a build for the Release configuration.
   ```

9. To complete your pull request, select **Create pull request**.

   This step doesn't merge any code. It tells others that you have proposed changes to be merged into the **main** branch.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/4-github-pr-details.png)

   The pull request window is displayed. You can see that the build status in Azure Pipelines is configured to appear as part of the pull request. That way, you and others can view the status of the build as it's running.


   ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/4-github-build-pending.png)

   Just like when you push a branch to GitHub, a pull request, by default, triggers Microsoft Azure Pipelines to build your application.

   **Tip:** If you don't see the build status appear right away, wait a few moments or refresh the page.

11. Optionally, select the **Details** link, and then trace the build as it moves through the pipeline.

   You can hand off your build to the next step in the process, such as QA. Later, you can configure the pipeline to push your change all the way out to your QA lab or production.

11. Go back to your pull request on GitHub.

12. Wait for the build to complete. You're now ready to merge your pull request.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/4-github-build-succeeded.png)

13. Select **Merge pull request**, and then select **Confirm merge**.

14. To delete the **code-workflow** branch from GitHub, select **Delete branch**.

    ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/4-github-delete-branch.png)

    It's completely safe to delete a branch from GitHub after you've merged your pull request. In fact, it's a common practice, because the branch is no longer needed. The changes are merged, and you can still find the details about the changes on GitHub or from the command line. Deleting a merged branch also helps others see only the work that's currently active.

    Git branches are meant to be short-lived. After you merge a branch, you don't push additional commits onto it or merge it a second time. In most cases, every time you start on a new feature or bug fix, you start with a clean branch that's based on the **main** branch.

    Deleting a branch on GitHub doesn't delete that branch from your local system. To do that, you would pass the **-d** switch to the **git branch** command.

## How many times is a change built?

The answer depends on how your build configuration is defined. Azure Pipelines enables you to define triggers that specify which events cause builds to happen. You can control which branches get built or even which files trigger the build.

As an example, let's say that you want a build to happen when a change is pushed to GitHub on any Git branch. But you don't want the build to happen when the only changes are to files in your project's **docs** folder. You might want to include this trigger section in your build configuration:

```yml
trigger:
  branches:
    include:
    - '*'     # build all branches
  paths:
    exclude:
    - docs/*  # exclude the docs folder
```

By default, a build is triggered when a change is pushed to any file on any branch.

A **continuous integration (CI) build** is a build that runs when you push a change to a branch.

A **pull request (PR) build** is a build that runs when you open a pull request or when you push additional changes to an existing pull request.

The changes you make through the **code-workflow** branch are built under three conditions:

1. A CI build happens when you push changes to the **code-workflow** branch.
2. A PR build happens when you open a pull request on the **code-workflow** branch against the **main** branch.
3. A final CI build happens after the pull request is merged to the **main** branch.

PR builds help you verify that your proposed changes will work correctly after they're merged to **main** or another target branch.

The final CI build verifies that the changes are still good after the PR was merged.

As an optional step, go to Azure Pipelines and watch the final CI build happen on the **main** branch.



# 2.5 Exercise - Push a change through the pipeline

In this unit, you'll practice the complete code workflow by pushing a small change to the Space Game website to GitHub.

Mara has been given the task of changing some text on the home page of the website, **Index.cshtml**. In this unit, you'll follow along.

Let's briefly review the steps to follow to complete the task:

1. Synchronize your local repository with the latest **main** branch on GitHub.
2. Create a branch to hold your changes.
3. Make the code changes you need, and verify them locally.
4. Push your branch to GitHub.
5. Merge any recent changes from the **main** branch on GitHub into your local working branch, and verify that your changes still work.
6. Push up any remaining changes, watch Azure Pipelines build the application, and submit your pull request.

## Fetch the latest main branch

In the previous unit, you created a pull request and merged your **code-workflow** branch into the **main** branch on GitHub. Now you need to pull the changes to **main** back to your local branch.

The **git pull** command fetches the latest code from the remote repository and merges it into your local repository. This way, you know you're working with the latest code base.

1. In your terminal, run **git checkout main** to switch to the **main** branch:

   ```bash
   git checkout main
   ```

2. To pull down the latest changes, run this **git pull** command:

   ```bash
   git pull origin main
   ```

   You can view the list of files that were changed. As an optional step, you can open the **azure-pipelines.yml** file to verify that it contains your complete build configuration.

   Recall that a Git repository where team members collaborate (such as on GitHub) is called a remote. Here, **origin** specifies your repository on GitHub.

   Later, you'll fetch starter code from the Microsoft GitHub repository, known as **upstream**.

## Build and run the web application

To ensure that you have a working copy to start your changes, build and run the web application locally.

1. In Visual Studio Code, go to the terminal window and run the following **dotnet build** command to build the application:

   ```bash
   dotnet build --configuration Release
   ```

2. Run the following **dotnet run** command to run the application:

   ```bash
   dotnet run --configuration Release --no-build --project Tailspin.SpaceGame.Web
   ```

   **Tip:** If you see an error in your browser that's related to a privacy or certificate error, select **Ctrl+C** from your terminal to stop the running application.

   Then run **dotnet dev-certs https --trust** and select **Yes** when prompted, or see this blog post for more information.

   After your computer trusts your local SSL certificate, run the **dotnet run** command a second time and go to **http://localhost:5000** from a new browser tab to see the running application.

## Verify that the application is running

In development mode, the Space Game website is configured to run on port 5000.

1. In a new browser tab, navigate to **http://localhost:5000** to see the running application.

   You should see this:

   ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/3-space-game-top.png)


   You can interact with the page, including the leaderboard. When you select a player's name, you see details about that player.

3. When you're finished, return to the terminal window, and select **Ctrl+C** to stop the running application.

## Create a feature branch

In this section, you'll create a Git branch so that you can work on files without affecting anyone else. No one will even know you're working on those files until you push them to the remote repository.

To create a branch, you use the **git checkout** command and give your branch a name, just like you did in the previous part.

Before you create a branch, it's a good idea to adhere to a naming convention. For example, if your branch is for working on a new feature, you might use **feature/<branch-name>**. For a bug fix, you could use **bugfix/<bug-number>**. In this example, your branch name will be **feature/home-page-text**.

In your terminal, run the following **git checkout** command:

```bash
git checkout -B feature/home-page-text
```

Like before, the **feature/home-page-text** is based on the **main** branch.

## Make changes and test it locally

1. In Visual Studio Code, open **Index.cshtml** in the **Tailspin.SpaceGame.Web/Views/Home** directory.

2. Look for this text near the top of the page:

   ```html
   <p>An example site for learning</p>
   ```

   **Tip:** Visual Studio Code also provides an easy way to search for text in files. To access the search pane, select the magnifying glass icon in the side pane.

3. Replace the text in the previous step with the following "mistyped" text, and then save the file:

   ```html
   <p>Welcome to the oficial Space Game site!</p>
   ```

   Note that the word "oficial" is intentionally mistyped. We'll address that error later in this module.

4. In your terminal, run the following **dotnet build** command to build the application:

   ```bash
   dotnet build --configuration Release
   ```

5. Run the following **dotnet run** command to run the application:

   ```bash
   dotnet run --configuration Release --no-build --project Tailspin.SpaceGame.Web
   ```

6. On a new browser tab, go to **http://localhost:5000** to see the running application.

   You can see that the home page contains the updated text.

    ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/5-web-site-revised-text.png)

8. When you're finished, return to the terminal window, and then press **Ctrl+C** to stop the running application.

## Commit and push your branch

Here you'll stage your changes to **Index.cshtml**, commit the change to your branch, and push your branch up to GitHub.

1. Run **git status** to check and see whether there are uncommitted changes on your branch:

   ```bash
   git status
   ```

   You'll see that **Index.cshtml** has been modified. Like before, the next step is to make sure that Git is tracking this file, which is called staging the file.

2. Run the following **git add** command to stage **Index.cshtml**:

   ```bash
   git add Tailspin.SpaceGame.Web/Views/Home/Index.cshtml
   ```

3. Run the following **git commit** command to commit your staged file to the **feature/home-page-text** branch:

   ```bash
   git commit -m "Improve the text at the top of the home page"
   ```

4. Run this **git push** command to push, or upload, the **feature/home-page-text** branch to your repository on GitHub:

   ```bash
   git push origin feature/home-page-text
   ```

   Just as before, you can locate your branch on GitHub from the branch drop-down box.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/5-github-recently-pushed.png)

## Watch Azure Pipelines build the application

Just as you did previously, Azure Pipelines automatically queues the build when you push changes to GitHub.

As an optional step, trace the build as it moves through the pipeline, and verify that the build succeeds.

## Synchronize any changes to the main branch

While you were busy working on your feature, changes might have been made to the remote **main** branch. Before you create a pull request, it's common practice to get the latest from the remote **main** branch.

To do this, first check out, or switch to, the **main** branch. Then, merge the remote **main** branch with your local **main** branch.

Next, check out your feature branch, and then merge your feature branch with the **main** branch.

Let's try the process now.

1. In your terminal, run this **git checkout** command to check out the **main** branch:

   ```bash
   git checkout main
   ```

2. To download the latest changes to the remote **main** branch and merge those changes into your local **main** branch, run this **git pull** command:

   ```bash
   git pull origin main
   ```

   Because no one actually made any changes to your **main** branch, the following command tells you that everything is already up to date.

   ```
   From https://github.com/username/mslearn-tailspin-spacegame-web
    * branch            main     -> FETCH_HEAD
   Already up to date.
   ```

3. To check out your feature branch, run **git checkout**:

   ```bash
   git checkout feature/home-page-text
   ```

4. Merge your feature branch with **main**:

   ```bash
   git merge main
   ```

   Again, because no one actually made any changes to your **main** branch, you see that everything is still up to date.

   ```
   Already up to date.
   ```

   If you did incorporate any changes, you would want to test your application again to ensure that everything is still working.

## Push your local branch again

When you incorporate changes from the remote repository into your local feature branch, you need to push your local branch back to the remote repository a second time.

Although you didn't incorporate any changes from the remote repository, let's practice the process to see what happens.

Run this **git push** command to push your changes to GitHub:

```bash
git push origin feature/home-page-text
```

Once again, the response says that you're already up to date since no changes were made.

```
Everything up-to-date
```

## Submit a pull request

In this section, you submit a pull request just as you did previously.

1. In a browser, sign in to GitHub.

2. Go to your **mslearn-tailspin-spacegame-web** repository.

3. In the drop-down list, select your **feature/home-page-text** branch.

4. To start your pull request, select **Contribute** and then **Open pull request**.

5. Ensure that the **base** drop-down list specifies your repository and not the Microsoft repository.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/5-github-set-base.png)

   **Important:** Again, this step is important because you can't merge your changes into the Microsoft repository.

   When you work directly with your own repository, and not a fork, your **main** branch is selected by default.

7. Enter a title and a description for your pull request.
   * **Title**: *Improve the text at the top of the home page*
   * **Description**: *Received the latest home page text from the product team.*

8. To complete your pull request, select **Create pull request**.

   This step doesn't merge any code. It tells others that you have changes that you're proposing to merge.

   The pull request window is displayed. As before, a pull request triggers Azure Pipelines to build your application by default.

9. Optionally, select the **Details** link or go to your project on Azure DevOps and watch the pipeline run.

10. When the build is finished, go back to your pull request on GitHub.

11. Select **Merge pull request**, and then select **Confirm merge**.

12. Select **Delete branch** to delete the **feature/home-page-text** branch from GitHub.




# 2.6 Exercise - Add a build badge

It's important for team members to know the build status. An easy way to quickly determine the build status is to add a build badge to the **README.md** file on GitHub. Let's check in on the team to see how it's done.

Andy is at his desk sifting through his emails. He's answering the third email that's related to the build status for the Space Game website.

**Andy:** There has to be some way to automate a status message. We have the pipeline, so we should be able to put a status somewhere. Maybe Mara knows how we can do it.

Andy finds Mara talking with Amita in the break room.

**Andy:** Hi, Amita. Mind if I borrow Mara for a second?

**Amita:** I have to get to a meeting anyway. Borrow away.

**Mara:** Hi Andy. What's up?

**Andy:** I really like the changes we've made to our build pipeline by using Azure Pipelines, and Git is a great version-control system. I was wondering, is there a way to let people know the build status?

**Mara:** Yes, actually. We can use a build badge.

## What is a build badge?

A badge is part of Microsoft Azure Pipelines. It has methods you can use to add an SVG image that shows the status of the build on your GitHub repository.

Most GitHub repositories include a file named **README.md**, which is a Markdown file that includes essential details and documentation about your project. GitHub renders this file on your project's home page.

Here's an example build badge:


![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/6-final-build-badge.png)

For this exercise, you make your build badge visible to everyone. This might not be a good idea for your private projects, because your build information will be made available to the public.

To check that your build badge is visible:

1. In Azure DevOps, navigate to your organization.

2. Select **Organization settings** from the bottom corner.

3. Under **Pipelines**, select **Settings**.

4. Turn off **Disable anonymous access to badges**.

 ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/6-devops-disable-anonymous-badge-access.png)

You need to make a similar change to your project:

1. Go to your project.
2. Navigate to **Project settings** from the bottom corner.
3. Under **Pipelines**, select **Settings**.
4. Turn off **Disable anonymous access to badges**.

## Add the build badge

Up until now, you created Git branches locally to make changes to the Space Game project. You can also propose changes directly through GitHub. In this section, you do that to set up your status badge.

1. In Azure DevOps, in the left pane, select **Pipelines**, then select your pipeline.

2. Select the ellipsis (**...**) in the upper right, then select **Status badge**.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/6-pipeline-options-menu.png)

4. Under **Sample Markdown**, select the **Copy** button to copy the Markdown code to the clipboard.

5. In GitHub, go to your project.

6. Make sure you're on the **main** branch. In the files area, open the **README.md** file.

7. Select **Edit this file** (the pencil icon) to open the file in the editor.

8. At the top of the page, add a blank line, and then paste the contents of the clipboard.

9. Select the **Preview** tab to see your proposed changes.

   GitHub renders the Markdown file and shows you the build badge.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/6-github-preview-changes.png)

## Commit your changes to main

In this section, you commit your changes to the **main** branch on GitHub.

1. Select **Commit changes**.

2. In the **Commit message** area, specify a commit message, such as "Add build badge".

   ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/6-github-commit-changes.png)

4. Leave the **Commit directly to the main branch** option selected, then select **Commit changes** to commit your changes to the **main** branch.

Your badge is displayed on the **README.md** page.

![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/6-final-build-badge.png)

This process is a more basic way to merge code into GitHub. Instead of committing directly, you could have created a pull request with your changes for others to review.

In practice, you'd switch to the **main** branch and pull the latest changes from GitHub the next time you need to add a feature or address a bug.

**Andy:** Mara, you just made a change directly to main. Why didn't you use the flow you taught me? You know, with the feature branches.

**Mara:** We could've done that. But sometimes when people are changing only the README file or other documentation files, they commit to main right then. Plus, you and I were able to verify the work together before we merged the change.

But this brings up a good point. If we can all just commit to main when we want to, we could be letting problems in the code slip into our main branch.

**Andy:** I've been meaning to talk to you about that.

Andy and Mara continue this conversation while walking back to their offices.


# 2.7 Exercise - Track your build history

An easy way to track important events in your Microsoft Azure DevOps project is to create a dashboard. A dashboard allows team members and observers to understand and track build trends at a glance.

In this unit, you'll set up a dashboard and add widgets to track your build history.

Andy is putting together a report of the progress the team is making. He's in the middle of searching through all the build reports and pull requests to try to get the big picture when Mara walks in.

**Mara:** Hi Andy, I have a question on a feature I'm working on. Do you have a minute?

**Andy:** Sure! I could use a break. There has to be an easier way to sum up the builds and see whether there are patterns of failure.

**Mara:** Actually, there's an easier way. We can set up a dashboard.

**Andy:** So I can have a summary of the information I need in one place? I'm all ears.

## What's the dashboard?

The dashboard is a customizable area in Azure DevOps where you can add widgets and extensions to help you visualize areas of your DevOps solution. For example, you can add a widget to:

* Show the history of your builds over time.
* Give you a *burn down* view of the work in progress.
* Show you the current pull requests.

## Add a build history widget to the dashboard

1. In Azure DevOps, select **Overview**, then select **Dashboards**.

2. Select **Add a widget**.

3. In the **Add widget** pane, search for **Build History**.

4. Drag the **Build History** tile to the canvas.

5. Select the **Gear** icon to configure the widget.
   1. Keep the **Build History** title.
   2. In the **Pipeline** drop-down list, select your pipeline.
   3. Keep **All branches** selected.

6. Select **Save**.

7. Select **Done Editing**.

   The **Build History** widget is displayed on the dashboard.

8. Hover over each build to view the build number, when the build was completed, and the elapsed build time.

   Each build succeeded, so the bars on the widget are all green. If the build had failed, it would appear in red.

9. Select one of the bars to drill down into that build.

To display more widgets, select the **Extension Gallery** link at the bottom of the **Add Widget** pane.



# 2.8 Exercise - Add a rule to require a review


In this unit, you'll set up a rule on GitHub that requires a reviewer to approve changes before they can be merged into the main branch. As a bonus, you'll also fix the typing error on the Space Game website's home page.

Currently, the team allows anyone who makes a pull request to merge the code into the main branch. Because no review is required, it's possible for incorrect or unstable code to find its way in.

Andy decides that he wants to add a check to the pull request in the form of another pair of eyes. He wants to set up GitHub to require someone other than the pull request author to review the code before it's merged. Let's see how to do this.

Andy heads off to find Mara and spots her at her desk working away, her head bobbing to the music in her earbuds.

**Andy:** Mara, I've been meaning to talk to you about something.

Mara looks up.

**Mara:** What can I help you with?

**Andy:** Several small mistakes are making it through the build. Just today, a typing error showed up on the home page. Amita is spending too much time on these things. We need to stop them before they make it to the main branch. We need another pair of eyes on the code before the pull request is approved.

**Mara:** I can set that up. In GitHub, there's a way to make sure that no pull request is merged before someone else reviews and approves it.

## Set up approvals

In this section, you'll set up a rule on GitHub that requires at least one reviewer to approve a pull request before it can be merged into the main branch. You'll then verify that the rule works by pushing up a fix to the typing error that Mara made earlier.

### Add the rule

1. In GitHub, go to your Space Game project repository.
2. Select the **Settings** tab near the top of the page.
3. On the left menu, select **Branches**.
4. Make sure that **main** is selected as your default branch.
5. Select **Add classic branch protection rule**.
6. Under **Branch name pattern**, enter **main**.
7. Select the **Require a pull request before merging** check box.
8. Select the **Require approvals** check box.
9. Keep the **Required approving reviews** value at **1**.
10. Select **Create**.
11. Select **Save changes**.

**Note:** At the bottom of the list of choices is an option named **Include Administrators**. This option requires repository administrators to follow the rule. You don't set that, because you're an administrator of your repository and there isn't another reviewer. In this unit, for learning purposes, you review and approve your own pull requests.

### Submit the fix

In this section, you submit a fix to the typing error on the home page. Remember that the word "official" is mistyped as "oficial."

![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/5-web-site-revised-text.png)

1. In Visual Studio Code, go to the terminal.

2. To check out the **main** branch, run **git checkout**:

   ```bash
   git checkout main
   ```

3. To pull down the latest changes to the **main** branch from GitHub, run **git pull**:

   ```bash
   git pull origin main
   ```

   You can see that two files are updated:

   - **README.md**: Contains the Markdown code for displaying the build badge.
   - **Index.cshtml**: Contains the updated home page text, which includes the typing error.

4. To fix the error, create and check out a branch:

   ```bash
   git checkout -B bugfix/home-page-typo
   ```

5. In File Explorer, open **Index.cshtml**.

6. Locate the error:

   ```html
   <p>Welcome to the oficial Space Game site!</p>
   ```

7. Change the line to correct the error:

   ```html
   <p>Welcome to the official Space Game site!</p>
   ```

8. Save the file.

9. In the terminal, stage and commit the change:

   ```bash
   git status
   git add Tailspin.SpaceGame.Web/Views/Home/Index.cshtml
   git commit -m "Fix typing error on the home page"
   ```

   In practice, you'd ordinarily build and run the site locally to verify the change. In this unit, for the sake of brevity, let's skip that step.

10. Push the branch to GitHub.

    ```bash
    git push origin bugfix/home-page-typo
    ```

### Test the rule

1. In GitHub, locate and select the **bugfix/home-page-typo** branch.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/8-github-recent-branch.png)

3. To start your pull request, select **Contribute** and then **Open pull request**.

4. Set your forked repository as the base repository.

    ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/8-github-review-required.png)

6. Select **Create pull request**.

   You can see that a human review is required before you can merge the change.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/8-github-review-required.png)

   In practice, you'd assign a team member to review your change. In this unit, you can merge your own pull request for learning purposes.

8. Select the **Merge without waiting for requirements to be met (bypass branch protections)** check box, and then select **Merge pull request**.

9. Select **Confirm merge**.

   Your change is merged.

10. To delete the **bugfix/home-page-typo** branch, select **Delete branch**.


# 2.9 Exercise - Clean up your Azure DevOps environment

You're all done with the tasks for this module. In this unit, you'll move the work item to the **Done** state on Azure Boards and clean up your Azure DevOps environment.

**Important**

This page contains important cleanup instructions. Cleaning up your resources helps ensure that you don't run out of free build minutes. Be sure to perform the cleanup if you ran the template earlier in this module.

## Move the work item to Done

In this section, you move the work item that you previously assigned to yourself, **Create a Git-based workflow**, to the **Done** column.

In practice, the definition of "Done" often means that working software is in the hands of your users. In this unit, for learning purposes, you'll mark this work as complete because you and the Tailspin team have started an improved code workflow that uses Git and GitHub.

At the end of each sprint, or work iteration, you and your team might hold a retrospective meeting in which you share the work you completed, what went well in the sprint, and what could be improved.

To complete the work item:

1. In Microsoft Azure DevOps, select **Boards** on the left menu, then select **Boards**.
2. Drag the **Create a Git-based workflow** work item from the **Doing** column to the **Done** column.

![](https://learn.microsoft.com/en-us/training/azure-devops/implement-code-workflow/media/9-azure-boards-wi2-done.png)

## Disable the pipeline or delete your project

Each module in this learning path provides a template that you can run to create a clean environment for the duration of the module.

Running multiple templates creates multiple Microsoft Azure Pipelines projects, each pointing to the same GitHub repository. This action can cause multiple pipelines to run each time you push a change to your GitHub repository. This action, in turn, can cause you to run out of free build minutes on our hosted agents. Therefore, it's important to disable or delete your pipeline before you move on to the next module.

Choose either of the next two options.

### Option 1: Disable the pipeline

This option disables the pipeline so that it doesn't process further build requests. You can reenable the build pipeline later if you want to. Choose this option if you want to keep your DevOps project and your build pipeline for future reference.

To disable the pipeline:

1. In Azure Pipelines, navigate to your pipeline.
2. Select the ellipsis (**...**), then select **Settings**:

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-pipelines-settings-button.png)

4. Under **Processing of new run requests**, select **Disabled**, and then select **Save**.

Your pipeline will no longer process build requests.

### Option 2: Delete the Azure DevOps project and GitHub repository

This option deletes your Azure DevOps project, including what's on Azure Boards and your build pipeline, and your GitHub repository. In future modules, you'll be able to run another template that brings up a new project in a state where this one leaves off. Choose this option if you don't need your DevOps project for future reference.

To delete the project:

1. In Azure DevOps, go to your project. Earlier, we recommended that you name this project *Space Game - web - Workflow*.
2. Select **Project settings** in the lower-left corner.
3. In the **Project details** area, scroll to the bottom and select **Delete**.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-delete-project.png)
   
5. In the window that appears, enter the project name and select **Delete** a second time.

Your project is now deleted.

To delete the repository:

1. In GitHub, go to your repository, `https://github.com/username/mslearn-tailspin-spacegame-web`.
2. Select the **Settings** tab, then select **General** in the left menu.
3. Scroll down and select **Delete this repository**.
4. Select **I want to delete this repository**.
5. Select **I have read and understand these effects**.
6. Type the repository name, then select **Delete this repository**.



# 2.10 Summary

In this module, you learned how to collaborate with others by using Git and GitHub.

Andy and Mara are well on their way to implementing a system that will allow them to better collaborate as a team and help ensure that only quality code is merged to the `main` branch.

A build badge and dashboard widgets help the team and others understand the latest build state and track the build history over time.

Although Andy and Mara are the primary code contributors, setting up a rule on GitHub to require a review is a good way to enforce a disciplined code review practice. Even minor errors can cause a build to break. As an example, you watched a typing error make its way through the build and into the hands of the QA team.

## Learn more

### Explore tools that simplify the Git and GitHub workflow

In this module, you made basic changes to the *Space Game* website. In practice, your changes will likely be much more complex. Although you can do everything you need from the command line, there are many tools you can use to simplify the workflow. Here are two that we recommend:

* **Visual Studio Code** includes Git support in-the-box. Here are resources where you can learn more:
   * Using Git source control in VS Code
   * Working with GitHub in VS Code
* **GitHub Desktop** is another great way to branch, commit, and visually compare and commit your changes.

### Learn more about Git

Although you can learn Git with just a few commands, full mastery will let you perform more complex types of merges and understand the history of your code base.

**git-scm.com** and the book **Pro Git** are two excellent resources for learning more about Git.

### Define your workflow

The workflow you used in this module is a standard way to get started. Your team can refine it to suit your needs. You'll find many resources and perspectives on the web from various teams with varying needs.

**Understanding the GitHub flow** introduces an approach that's similar to what you saw in this module, and it includes tips that you can apply to your own workflow.

**A successful Git branching model** proposes a more advanced branching and merging strategy.

**How to Split Pull Requests** describes how to split large pull requests into smaller ones to help others more easily understand your changes.

**How to Write a Git Commit Message** teaches you how to be a better collaborator by writing effective commit messages.

**Specify events that trigger pipelines** explains how triggers enable you to control which files or Git branches cause a build to occur.




# 3 Run quality tests in your build pipeline by using Azure Pipelines

Set up automated testing in your pipeline to improve code quality.

# Learning objectives
After completing this module, you'll be able to:
- Explain the benefits of automated testing and the kinds of testing you can use.
- Run unit tests locally and then in Azure Pipelines.
- Add dashboard widgets to visualize test runs over time.
- Perform code coverage testing to see how much of your code is covered by unit tests.
- Fix and verify test failures in your build pipeline.


# 3.1 Introduction

As you add a feature to your app, how do you *know* whether the feature will work correctly, given all possible interactions? How do you know that the feature works well with and doesn't break other features? How do you know that your code is maintainable and easily understandable by others?

You could run the app locally and try a few inputs, but that takes time and doesn't cover all cases. Plus, repeatedly testing existing features gets tedious and time consuming as you add new features.

In this module, you're a developer at Tailspin Toys, working with your team on a game called *Space Game*. This module demonstrates how to set up automated testing to help ensure that your latest feature works and that you haven't broken anything along the way.

After completing this module, you'll be able to:

* Explain the benefits of automated testing and the kinds of testing you can use.
* Run unit tests locally and then in Azure Pipelines.
* Add dashboard widgets to visualize test runs over time.
* Perform code coverage testing to see how much of your code is covered by unit tests.
* Fix and verify test failures in your build pipeline.

## Prerequisites

The modules in this learning path form a progression.

To follow the progression from the beginning, be sure to first complete the **Get started with Azure DevOps** learning path.

We also recommend you start at the beginning of this learning path, **Build applications with Azure DevOps**.

If you want to go through just this module, you need to set up a development environment on your Windows, macOS, or Linux system. You need:

* An Azure DevOps organization with access to parallel jobs. If your organization does not have access to parallel jobs, you can request parallel jobs for free for public or private projects using [this form](). Your request takes 2-3 business days.
* An Azure subscription
* A GitHub account
* Visual Studio Code with the Azure Pipelines for VS Code extension.
* .NET 8.0 SDK
* Git

You can get started with Microsoft Azure DevOps for free.

This environment lets you complete the exercises in this and future modules. You can also use it to apply your new skills to your own projects.

> **Note**
> 
> Azure Pipelines support a vast array of **languages and application types**. In this module, you'll be working with a .NET application but you can apply the patterns you learn here to your own projects that use your favorite programming languages and frameworks.


# 3.2 What is automated testing?

In this unit, you'll learn about the benefits of automated testing and the kinds of testing you can perform. You'll also learn what makes a good test and be introduced to some of the testing tools that are available to you.

## What is automated testing?

Automated testing uses software to execute your code and compare the actual results with the results you expect. Compare this with exploratory or manual testing, where a human typically follows instructions in a test plan to verify that software functions as expected.

Manual testing has its benefits. But as your code base grows in size, testing all features manually (including edge cases) can become repetitive, tedious, and error prone. Automated testing can help eliminate some of this burden and enable manual testers to focus on what they do best: ensuring that your users will have a positive experience with your software.

## The test pyramid

When we think about automated testing, it's common to separate tests into layers. Mike Cohn proposes this concept, known as the test pyramid, in his book *Succeeding with Agile*.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/2-test-pyramid.png)

Although this is a simplistic version of Cohn's model, the concept illustrates that you focus most of your effort on writing tests that verify the foundational levels of your software (callout 1 in the pyramid), such as functions, classes, and methods. You focus progressively less effort as features are combined, such as at the user interface (UI) layer (callout 2 in the pyramid). The idea is that if you can verify that each lower-level component works as expected in isolation, tests at the higher levels need only verify that multiple components work together to get the expected result.

## When should I write tests?

The answer mainly depends on your needs and experience in writing tests.

It's never too late to start adding tests for code you've already written and deployed. This is especially true for features that often break or require the most effort from your test team.

When you relate testing to continuous integration and continuous delivery pipelines, two concepts you'll hear about are **continuous testing** and **shifting left**.

**Continuous testing** means tests are run early in the development process as every change moves through the pipeline. **Shifting left** means considering software quality and testing earlier in the development process.

For example, developers often add test cases as they develop their feature and run the entire suite of tests before they submit the change to the pipeline. This approach helps ensure that the feature they're building behaves as expected and that it doesn't break existing features.

Here's a short video where Abel Wang, Cloud Advocate at Microsoft, explains how to ensure you maintain quality in your DevOps plan.

### Ask Abel

Shifting left often requires testers to get involved in the design process, even before any code for the feature is written. Compare this to the "handoff" model, where the test team is presented with new features to test only after the software is designed and written. A bug discovered late in the process can affect the team's delivery schedule, and bugs might be discovered weeks or even months after the developer originally built the feature.

https://videoencodingpublic-hgeaeyeba8gycee3.b01.azurefd.net/public-90341df2-dc15-406f-af3f-52afc0d4ca76/thumbnail_w1120.jpeg

## The tradeoff

With automated testing, there's a tradeoff. Although automated testing allows testers to focus their time verifying the end-user experience, developers might need to dedicate more time to writing and maintaining their test code.

However, the point of automated testing is to help ensure that testers receive only the highest quality code, code that's been proven to function as expected. Therefore, developers can reclaim some of their time by having to handle fewer bugs or avoiding code rewrites because of an edge case they hadn't originally considered.

## Added benefits

Documentation and the ability to refactor your code more easily are two added benefits of automated testing.

### Documentation

Manual test plans can serve as a type of documentation as to how software should behave and why certain features exist.

Automated tests can serve the same purpose. Automated test code often uses a human-readable format. The set of inputs you provide represents values your users might enter. Each associated output specifies the result your users should expect.

In fact, many developers follow the **test-driven development (TDD)** method by writing their test code before implementing a new feature. The idea is to write a set of tests, often called specs, that initially fail. Then, the developer incrementally writes code to implement the feature until all tests pass. Not only do the specs document the requirements, but the TDD process helps ensure that only the necessary amount of code is written to implement the feature.

### Refactoring

Say you have a large code base that you want to refactor to make certain parts run faster. How do you know that your refactoring efforts won't cause parts of your application to break?

Automated tests serve as a type of contract. That is, you specify the inputs and the expected results. When you have a set of passing tests, you're better able to experiment and refactor your code. When you make a change, all you need to do is run your tests and verify that they continue to pass. After you've met your refactoring goals, you can submit your change to the build pipeline so that everyone can benefit, but with a lower risk of something breaking.

## What types of automated testing are there?

There are many types of automated testing. Each test serves a separate purpose. For example, you might run security tests to help verify that only authorized users can access a piece of software or one of its features.

When we mention continuous integration and the build pipeline, we're typically referring to **development testing**. Development testing refers to tests you can run before you deploy the application to a test or production environment.

For example, **lint testing**, a form of static-code analysis, checks your source code to determine whether it conforms to your team's style guide. Code that's formatted consistently is easier for everyone to read and maintain.

In this module, you'll work with **unit testing** and **code-coverage testing**.

**Unit testing** verifies the most fundamental components of your program or library, such as an individual function or method. You specify one or more inputs along with the expected results. The test runner performs each test and checks to see whether the actual and expected results match.

As an example, let's say you have a function that performs an arithmetic operation that includes division. You might specify a few values that you expect your users to enter along with edge-case values such as 0 and -1. If a certain input produces an error or exception, you can verify that the function produces the same error.

**Code-coverage testing** computes the percentage of your code that's covered by your unit tests. Code-coverage testing can include conditional branches in your code to ensure that a function is covered.

The greater your code coverage percentage, the more confident you can be that you won't later discover a bug in code that wasn't fully tested. You don't need to reach 100 percent code coverage. In fact, when you start, you'll likely find that you have a low percentage, but that gives you a starting point from which you can add additional tests that cover problematic or frequently used code.

## Keep unit tests isolated

When you're learning about unit testing, you might hear terms such as **mocks**, **stubs**, and **dependency injection**.

Recall that a unit test should verify an individual function or method, and not how multiple components interact. But if you have a function that calls a database or web server, how do you handle that?

Not only does a call to an external service break isolation, but it can slow things down. If the database or web server goes down or is otherwise unavailable, the call can also disrupt your test run.

By using techniques such as mocking and dependency injection, you can create components that mimic this external functionality. You'll get an example later in this module.

Later, you can run integration tests to verify that your application works correctly with a real database or web server.

## What makes a good test?

You'll be better able to identify a good test as you gain experience writing your own tests and reading tests written by others. Here are some guidelines for getting started:

* **Don't test for the sake of testing**: Your tests should serve a purpose beyond being a checklist item to cross off. Write tests that verify that your critical code works as intended and doesn't break existing functionality.
* **Keep your tests short**: Tests should finish as quickly as possible, especially those that happen during the development and build phases. When tests are run as each change moves through the pipeline, you don't want them to be the bottleneck.
* **Ensure that your tests are repeatable**: Test runs should produce the same results each time, whether you run them on your computer, a coworker's computer, or in the build pipeline.
* **Keep your tests focused**: A common misconception is that tests are meant to cover code written by others. Ordinarily, your tests should cover only your code. For example, if you're using an open-source graphics library in your project, you don't need to test that library.
* **Choose the right granularity**: For example, if you're performing unit testing, an individual test shouldn't combine or test multiple functions or methods. Test each function separately and later write integration tests that verify that multiple components interact properly.

## What types of testing tools are available?

The testing tools you use depend on the type of application you're building and the type of testing you want to perform. For example, you can use Selenium to perform UI testing on many types of web browsers and operating systems.

No matter what language your application is written in, many test tools are available to you to use.

For example, for Java applications, you might choose Checkstyle to perform lint testing and JUnit to perform unit testing.

In this module, we'll use **NUnit** for unit testing because it's popular in the .NET community.

---

## Check your knowledge

### 1. According to the test pyramid, where should you spend most of your time running tests?

- [ ] Running unit tests on your classes and methods.
- [ ] Running integration tests between your web server and your database.
- [ ] Running manual tests on your user interface.

### 2. Shifting left refers to:

- [ ] Fixing all known bugs before adding new features.
- [ ] Considering software quality and testing earlier in the development process.
- [ ] Testing for undiscovered bugs in a test or pre-production environment.

### 3. Which of the following demonstrates the best testing practices?

- [ ] Tests run quickly and focus on the most-used code paths.
- [ ] A comprehensive suite of unit and integration tests is run during each stage of the build process.
- [ ] Tests cover both the team's application code and all open-source libraries the application uses.

---

## Відповіді на запитання:

**1. According to the test pyramid, where should you spend most of your time running tests?**
✅ **Running unit tests on your classes and methods.**

Згідно з пірамідою тестування, найбільшу увагу слід приділяти тестуванню фундаментальних компонентів програмного забезпечення (functions, classes, methods), які знаходяться в основі піраміди.

**2. Shifting left refers to:**
✅ **Considering software quality and testing earlier in the development process.**

"Shifting left" означає розгляд якості програмного забезпечення та тестування на більш ранніх етапах процесу розробки, а не після завершення написання коду.

**3. Which of the following demonstrates the best testing practices?**
✅ **Tests run quickly and focus on the most-used code paths.**

Найкращі практики тестування включають швидке виконання тестів та фокус на найбільш використовуваних шляхах коду, що забезпечує ефективність та практичність тестування.




# 3.3 Exercise - Set up your Azure DevOps environment

In this unit, you'll ensure that your Microsoft Azure DevOps organization is set up to complete the rest of this module.

To do this, you:

* Set up an Azure DevOps project for this module.
* Move the work item for this module on Azure Boards to the Doing column.
* Make sure your project is set up locally so that you can push changes to the pipeline.

## Get the Azure DevOps project

Here, you'll make sure that your Azure DevOps organization is set up to complete the rest of this module. You'll do this by running a template that creates a project for you in Azure DevOps.

### Run the template

Run a template that sets up your Azure DevOps organization.

1. Get and run the ADOGenerator project in Visual Studio or the IDE of your choice.

2. When prompted to **Enter the template number from the list of templates**, enter **24** for **Run quality tests in your build pipeline using Azure Pipelines**, then press **Enter**.

3. Choose your authentication method. You can set up and use a Personal Access Token (PAT) or use device login.

   > **Note**
   > 
   > If you set up a PAT, make sure to authorize the necessary scopes. For this module, you can use **Full access**, but in a real-world situation, you should ensure you grant only the necessary scopes.

4. Enter your Azure DevOps organization name, then press **Enter**.

5. If prompted, enter your Azure DevOps PAT, then press **Enter**.

6. Enter a project name such as **Space Game - web - Tests**, then press **Enter**.

7. Once your project is created, go to your Azure DevOps organization in your browser (at `https://dev.azure.com/<your-organization-name>/`) and select the project.

### Fork the repository

If you haven't already, create a fork of the `mslearn-tailspin-spacegame-web` repository.

1. On GitHub, go to the [mslearn-tailspin-spacegame-web](https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web) repository.

2. Select **Fork** at the top-right of the screen.

3. Choose your GitHub account as the **Owner**, then select **Create fork**.

> **Important**
> 
> The **Clean up your Azure DevOps environment** page in this module contains important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes. Be sure to perform the cleanup steps even if you don't complete this module.

### Set your project's visibility

Initially, your fork of the Space Game repository on GitHub is set to public while the project created by the Azure DevOps template is set to private. A public repository on GitHub can be accessed by anyone, while a private repository is only accessible to you and the people you choose to share it with. Similarly, on Azure DevOps, public projects provide read-only access to non-authenticated users, while private projects require users to be granted access and authenticated to access the services.

At the moment, it is not necessary to modify any of these settings for the purposes of this module. However, for your personal projects, you must determine the visibility and access you wish to grant to others. For instance, if your project is open source, you may choose to make both your GitHub repository and your Azure DevOps project public. If your project is proprietary, you would typically make both your GitHub repository and your Azure DevOps project private.

Later on, you may find the following resources helpful in determining which option is best for your project:

* [Use private and public projects](https://docs.microsoft.com/azure/devops/organizations/projects/about-projects)
* [Change project visibility to public or private](https://docs.microsoft.com/azure/devops/organizations/projects/make-project-public)
* [Setting repository visibility](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)

## Set up the project locally

Here, you load the Space Game project in Visual Studio Code, configure Git, clone your repository locally, and set the upstream remote so that you can download the starter code.

> **Note**
> 
> If you're already set up with the `mslearn-tailspin-spacegame-web` project locally, you can move to the next section.

### Open the integrated terminal

Visual Studio Code comes with an integrated terminal, so you can edit files and work from the command line all in one place.

1. Start Visual Studio Code.

2. On the **View** menu, select **Terminal**.

3. In the dropdown list, select **bash**. If you're familiar with another Unix shell that you prefer to use, such as Zsh, select that shell instead.


![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/vscode-terminal-bash.png)

The terminal window lets you choose any shell that's installed on your system, like Bash, Zsh, and PowerShell.

Here you'll use Bash. Git for Windows provides Git Bash, which makes it easy to run Git commands.

> **Note**
> 
> On Windows, if you don't see Git Bash listed as an option, make sure you've installed Git, and then restart Visual Studio Code.

4. Run the `cd` command to navigate to the directory you want to work from, like your home directory (`~`). You can choose a different directory if you want.

```bash
cd ~
```

### Configure Git

If you're new to Git and GitHub, you first need to run a few commands to associate your identity with Git and authenticate with GitHub.

[Set up Git](https://docs.github.com/get-started/quickstart/set-up-git) explains the process in greater detail.

At a minimum, you'll need to complete the following steps. Run these commands from the integrated terminal:

1. Set your username.
2. Set your commit email address.
3. Cache your GitHub password.

> **Note**
> 
> If you're already using two-factor authentication with GitHub, create a personal access token and use your token in place of your password when prompted later.
> 
> Treat your access token like you would a password. Keep it in a safe place.

## Set up your project in Visual Studio Code

In this part, you clone your fork locally so that you can make changes and build out your pipeline configuration.

> **Note**
> 
> If you receive any errors about filenames being too long when you clone your repository, try cloning the repository in a folder that doesn't have a long name or is deeply nested.

### Clone your fork locally

You now have a copy of the Space Game web project in your GitHub account. Now you'll download, or clone, a copy to your computer so you can work with it.

A clone, just like a fork, is a copy of a repository. When you clone a repository, you can make changes, verify they work as you expect, and then upload those changes back to GitHub. You can also synchronize your local copy with changes other authenticated users have made to GitHub's copy of your repository.

To clone the Space Game web project to your computer:

1. Go to your fork of the Space Game web project (`mslearn-tailspin-spacegame-web`) on GitHub.

2. Select **Code**. Then, from the **HTTPS** tab, select the button next to the URL that's shown to copy the URL to your clipboard.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/github-clone-button.png)

3. In Visual Studio Code, go to the terminal window.

4. In the terminal, move to the directory you want to work from, like your home directory (`~`). You can choose a different directory if you want.

```bash
cd ~
```

5. Run the `git clone` command. Replace the URL that's shown here with the contents of your clipboard:

```bash
git clone https://github.com/your-name/mslearn-tailspin-spacegame-web.git
```

6. Move to the `mslearn-tailspin-spacegame-web` directory. This is the root directory of your repository.

```bash
cd mslearn-tailspin-spacegame-web
```

### Set the upstream remote

A remote is a Git repository where team members collaborate (like a repository on GitHub). Here you list your remotes and add a remote that points to Microsoft's copy of the repository so that you can get the latest sample code.

1. Run this `git remote` command to list your remotes:

```bash
git remote -v
```

You see that you have both fetch (download) and push (upload) access to your repository:

```
origin  https://github.com/username/mslearn-tailspin-spacegame-web.git (fetch)
origin  https://github.com/username/mslearn-tailspin-spacegame-web.git (push)
```

**Origin** specifies your repository on GitHub. When you fork code from another repository, it's common to name the original remote (the one you forked from) as **upstream**.

2. Run this `git remote add` command to create a remote named **upstream** that points to the Microsoft repository:

```bash
git remote add upstream https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web.git
```

3. Run `git remote` a second time to see the changes:

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

### Open the project in the file explorer

In Visual Studio Code, your terminal window points to the root directory of the Space Game web project. To view its structure and work with files, from the file explorer, you'll now open the project.

The easiest way to open the project is to reopen Visual Studio Code in the current directory. To do so, run the following command from the integrated terminal:

```bash
code -r .
```

You see the directory and file tree in the file explorer.

Reopen the integrated terminal. The terminal places you at the root of your web project.

If the `code` command fails, you need to add Visual Studio Code to your system PATH. To do so:

1. In Visual Studio Code, select **F1** or select **View > Command Palette** to access the command palette.
2. In the command palette, enter **Shell Command: Install 'code' command in PATH**.
3. Repeat the previous procedure to open the project in the file explorer.

You're now set up to work with the Space Game source code and your Azure Pipelines configuration from your local development environment.


# 3.4 Exercise - Add unit tests to your application

In this unit, we'll add unit tests to the automated build that we created with Microsoft Azure Pipelines. Regression bugs are creeping into your team's code and breaking the leaderboard's filtering functionality. Specifically, the wrong game mode keeps appearing.

The following image illustrates the problem. When a user selects "Milky Way" to show only scores from that game map, they get results from other game maps, such as Andromeda.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/4-leaderboard-bug.png)

The team wants to catch the error before it reaches the testers. Unit tests are a great way to automatically test for regression bugs.

Adding the unit tests at this point in the process will give the team a head start as they improve the Space Game web app. The application uses a document database to store high scores and player profiles. Right now, it uses local test data. Later, they plan to connect the app to a live database.

Many unit test frameworks are available for C# applications. We'll use **NUnit** because it's popular with the community.

Here's the unit test you're working with:

```csharp
[TestCase("Milky Way")]
[TestCase("Andromeda")]
[TestCase("Pinwheel")]
[TestCase("NGC 1300")]
[TestCase("Messier 82")]
public void FetchOnlyRequestedGameRegion(string gameRegion)
{
    const int PAGE = 0; // take the first page of results
    const int MAX_RESULTS = 10; // sample up to 10 results

    // Form the query predicate.
    // This expression selects all scores for the provided game region.
    Expression<Func<Score, bool>> queryPredicate = score => (score.GameRegion == gameRegion);

    // Fetch the scores.
    Task<IEnumerable<Score>> scoresTask = _scoreRepository.GetItemsAsync(
        queryPredicate, // the predicate defined above
        score => 1, // we don't care about the order
        PAGE,
        MAX_RESULTS
    );
    IEnumerable<Score> scores = scoresTask.Result;

    // Verify that each score's game region matches the provided game region.
    Assert.That(scores, Is.All.Matches<Score>(score => score.GameRegion == gameRegion));
}
```

You can filter the leaderboard by any combination of game type and game map.

This test queries the leaderboard for high scores and verifies that each result matches the provided game map.

In an NUnit test method, `TestCase` provides inline data to use to test that method. Here, NUnit calls the `FetchOnlyRequestedGameRegion` unit test method, as follows:

```csharp
FetchOnlyRequestedGameRegion("Milky Way");
FetchOnlyRequestedGameRegion("Andromeda");
FetchOnlyRequestedGameRegion("Pinwheel");
FetchOnlyRequestedGameRegion("NGC 1300");
FetchOnlyRequestedGameRegion("Messier 82");
```

Notice the call to the `Assert.That` method at the end of the test. An assertion is a condition or statement that you declare to be true. If the condition turns out to be false, that could indicate a bug in your code. NUnit runs each test method using the inline data you specify and records the result as a passing or failing test.

Many unit test frameworks provide verification methods that resemble natural language. These methods help make tests easy to read and help you map the tests to the application's requirements.

Consider the assertion made in this example:

```csharp
Assert.That(scores, Is.All.Matches<Score>(score => score.GameRegion == gameRegion));
```

You might read this line as:

*Assert that the game region of each returned score matches the provided game region.*

Here's the process to follow:

1. Fetch a branch from the GitHub repository that contains the unit tests.
2. Run the tests locally to verify that they pass.
3. Add tasks to your pipeline configuration to run the tests and collect the results.
4. Push the branch to your GitHub repository.
5. Watch your Azure Pipelines project automatically build the application and run the tests.

## Fetch the branch from GitHub

Here, you'll fetch the `unit-tests` branch from GitHub and check out, or switch to, that branch.

This branch contains the Space Game project that you worked with in the previous modules and an Azure Pipelines configuration to start with.

1. In Visual Studio Code, open the integrated terminal.

2. Run the following git commands to fetch a branch named `unit-tests` from the Microsoft repository, and then switch to that branch.

```bash
git fetch upstream unit-tests
git checkout -B unit-tests upstream/unit-tests
```

The format of this command enables you to get starter code from the Microsoft GitHub repository, known as `upstream`. Shortly, you'll push this branch to your GitHub repository, known as `origin`.

3. As an optional step, open the `azure-pipelines.yml` file in Visual Studio Code and familiarize yourself with the initial configuration. The configuration resembles the basic one you created in the **Create a build pipeline with Azure Pipelines** module. It builds only the application's Release configuration.

## Run the tests locally

It's a good idea to run all tests locally before you submit any tests to the pipeline. You'll do that here.

1. In Visual Studio Code, open the integrated terminal.

2. Run `dotnet build` to build each project in the solution.

```bash
dotnet build --configuration Release
```

3. Run the following `dotnet test` command to run the unit tests:

```bash
dotnet test --configuration Release --no-build
```

The `--no-build` flag specifies not to build the project before running it. You don't need to build the project because you built it in the previous step.

You should see that all five tests pass.

```
Starting test execution, please wait...
A total of 1 test files matched the specified pattern.

Passed!  - Failed:     0, Passed:     5, Skipped:     0, Total:     5, Duration: 57 ms
```

In this example, the tests took less than one second to run.

Notice that there were five total tests. Although we defined just one test method, `FetchOnlyRequestedGameRegion`, that test is run five times, once for each game map as specified in the `TestCase` inline data.

4. Run the tests a second time. This time, provide the `--logger` option to write the results to a log file.

```bash
dotnet test Tailspin.SpaceGame.Web.Tests --configuration Release --no-build --logger trx
```

You see from the output that a TRX file is created in the `TestResults` directory.

A TRX file is an XML document that contains the results of a test run. It's a popular format for test results because Visual Studio and other tools can help you visualize the results.

Later, you'll see how Azure Pipelines can help you visualize and track your test results as they run through the pipeline.

> **Note**
> 
> TRX files are not meant to be included in source control. A `.gitignore` file allows you to specify which temporary and other files you want Git to ignore. The project's `.gitignore` file is already set up to ignore anything in the `TestResults` directory.

5. As an optional step, in Visual Studio Code, open the `DocumentDBRepository_GetItemsAsyncShould.cs` file from the `Tailspin.SpaceGame.Web.Tests` folder and examine the test code. Even if you're not interested in building .NET apps specifically, you might find the test code useful because it resembles code you might see in other unit test frameworks.

## Add tasks to your pipeline configuration

Here, you'll configure the build pipeline to run your unit tests and collect the results.

1. In Visual Studio Code, modify `azure-pipelines.yml` as follows:

```yaml
trigger:
- '*'

pool:
  vmImage: 'ubuntu-20.04'
  demands:
  - npm

variables:
  buildConfiguration: 'Release'
  wwwrootDir: 'Tailspin.SpaceGame.Web/wwwroot'
  dotnetSdkVersion: '6.x'

steps:
- task: UseDotNet@2
  displayName: 'Use .NET SDK $(dotnetSdkVersion)'
  inputs:
    version: '$(dotnetSdkVersion)'

- task: Npm@1
  displayName: 'Run npm install'
  inputs:
    verbose: false

- script: './node_modules/.bin/node-sass $(wwwrootDir) --output $(wwwrootDir)'
  displayName: 'Compile Sass assets'

- task: gulp@1
  displayName: 'Run gulp tasks'

- script: 'echo "$(Build.DefinitionName), $(Build.BuildId), $(Build.BuildNumber)" > buildinfo.txt'
  displayName: 'Write build info'
  workingDirectory: $(wwwrootDir)

- task: DotNetCoreCLI@2
  displayName: 'Restore project dependencies'
  inputs:
    command: 'restore'
    projects: '**/*.csproj'

- task: DotNetCoreCLI@2
  displayName: 'Build the project - $(buildConfiguration)'
  inputs:
    command: 'build'
    arguments: '--no-restore --configuration $(buildConfiguration)'
    projects: '**/*.csproj'

- task: DotNetCoreCLI@2
  displayName: 'Run unit tests - $(buildConfiguration)'
  inputs:
    command: 'test'
    arguments: '--no-build --configuration $(buildConfiguration)'
    publishTestResults: true
    projects: '**/*.Tests.csproj'

- task: DotNetCoreCLI@2
  displayName: 'Publish the project - $(buildConfiguration)'
  inputs:
    command: 'publish'
    projects: '**/*.csproj'
    publishWebProjects: false
    arguments: '--no-build --configuration $(buildConfiguration) --output $(Build.ArtifactStagingDirectory)/$(buildConfiguration)'
    zipAfterPublish: true

- task: PublishBuildArtifacts@1
  displayName: 'Publish Artifact: drop'
  condition: succeeded()
```

This version introduces this `DotNetCoreCLI@2` build task.

```yaml
- task: DotNetCoreCLI@2
  displayName: 'Run unit tests - $(buildConfiguration)'
  inputs:
    command: 'test'
    arguments: '--no-build --configuration $(buildConfiguration)'
    publishTestResults: true
    projects: '**/*.Tests.csproj'
```

This build task runs the `dotnet test` command.

Notice that this task doesn't specify the `--logger trx` argument that you used when you ran the tests manually. The `publishTestResults` argument adds that for you. This argument tells the pipeline to generate the TRX file to a temporary directory, accessible through the `$(Agent.TempDirectory)` built-in variable. It also publishes the task results to the pipeline.

The `projects` argument specifies all C# projects that match `"**/*.Tests.csproj."` The `"**"` part matches all directories, and the `"*.Tests.csproj"` part matches all projects whose file name ends with `".Tests.csproj."` The `unit-tests` branch contains just one unit test project, `Tailspin.SpaceGame.Web.Tests.csproj`. By specifying a pattern, you can run more test projects without the need to modify your build configuration.

## Push the branch to GitHub

Here, you'll push your changes to GitHub and see the pipeline run. Recall that you're currently on the `unit-tests` branch.

1. In the integrated terminal, add `azure-pipelines.yml` to the index, commit the changes, and push the branch up to GitHub.

```bash
git add azure-pipelines.yml
git commit -m "Run and publish unit tests"
git push origin unit-tests
```

## Watch Azure Pipelines run the tests

Here you see the tests run in the pipeline and then visualize the results from Microsoft Azure Test Plans. Azure Test Plans provides all the tools you need to successfully test your applications. You can create and run manual test plans, generate automated tests, and collect feedback from stakeholders.

1. In Azure Pipelines, trace the build through each of the steps.

You see that the **Run unit tests - Release** task runs the unit tests just as you did manually from the command line.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/4-pipeline-task.png)

2. Navigate back to the pipeline summary.

3. Move to the **Tests** tab.

You see a summary of the test run. All five tests have passed.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/4-test-tab-summary.png)

4. In Azure DevOps, select **Test Plans**, and then select **Runs**.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/4-test-plans-runs.png)

You see the most recent test runs, including the one you just ran.

5. Double-click the most recent test run.

You see a summary of the results.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/4-test-run-results.png)

In this example, all five tests have passed. If any tests failed, you can go to the build task to get more details.

You can also download the TRX file to examine it through Visual Studio or another visualization tool.

Although you only added one test, it's a good start and it fixes the immediate problem. Now, the team has a place to add more tests and run them as they improve their process.

## Merge your branch into main

In a real-world scenario, if you were happy with the results, you might merge the `unit-tests` branch to `main`, but for brevity, we'll skip that process for now.



# 3.5 Exercise - Add a testing widget to your dashboard


In this unit, you'll add a widget to your dashboard to help visualize your test runs over time.

## Add the widget to the dashboard

1. In your Azure DevOps project, select **Overview**, and then select **Dashboards**.

   > **Note**
   > 
   > If you ran the template to create the Azure DevOps project, you won't see the dashboard widgets you set up in previous modules.

2. Select **Add a widget**.

3. In the **Add Widget** pane, search for **Test Results Trend**.

4. Drag **Test Results Trend** to the canvas.

5. Select the **Gear** icon to configure the widget.
   a. Under **Build pipeline**, select your pipeline.
   b. Keep the other default settings.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/5-test-results-trend-widget.png)

6. Select **Save**.

7. Select **Done Editing**.

Although the widget displays only one test run, you now have a way to visualize and track test runs over time. Here's an example that shows a few successful test runs.

If you begin to see test failures, you can select a point on the graph to navigate directly to that build.


# 3.6 Exercise - Perform code coverage testing


Much like the tool you use for unit testing, the tool you use for code coverage depends on the programming language and application framework.

When you target .NET applications to run on Linux, **coverlet** is a popular option. Coverlet is a cross-platform, code-coverage library for .NET.

## How is code coverage done in .NET?

The way you collect code coverage depends on what programming language and frameworks you're using, and what code coverage tools are available.

In our Tailspin scenario, we find that:

- Visual Studio on Windows provides a way to perform code coverage.
- However, because we're building on Linux, we can use **coverlet**, a cross-platform code coverage library for .NET.
- The unit test project requires the **coverlet.msbuild** NuGet package.
- Code coverage results are written to an XML file so that they can be processed by another tool. Azure Pipelines supports **Cobertura** and **JaCoCo** coverage result formats.
- For this module, we're using **Cobertura**.
- To convert Cobertura coverage results to a format that's human-readable, we can use a tool called **ReportGenerator**.
- ReportGenerator provides many formats, including HTML. The HTML formats create detailed reports for each class in a .NET project.
- Specifically, there's an HTML format called **HtmlInline_AzurePipelines**, which provides a visual appearance that matches Azure Pipelines.

## How can I manage .NET tools?

A .NET tool such as ReportGenerator is a special NuGet package that contains a console application. You can manage a .NET tool as a global tool or as a local tool.

A **global tool** is installed in a centralized location and can be called from any directory. One version of a global tool is used for all directories on the machine.

A **local tool** is a more isolated copy of a .NET tool that's scoped to a specific directory. Scope enables different directories to contain different versions of the same tool.

You use a manifest file to manage local tools for a given directory. This file is in JSON format and is typically named **dotnet-tools.json**. A manifest file allows you to describe the specific tool versions that you need to build or run your application.

When you include the manifest file in source control and your application sources, developers and build systems can run the `dotnet tool restore` command to install all of the tools listed in the manifest file. When you need a newer version of a local tool, you simply update the version in the manifest file.

To keep things more isolated, you'll work with local tools in this module. You'll create a tool manifest that includes the ReportGenerator Tool. You'll also modify your build pipeline to install the ReportGenerator Tool to convert code coverage results to a human-readable format.

## Run code coverage locally

Before you write any pipeline code, you can try things manually to verify the process.

1. In Visual Studio Code, open the integrated terminal.

2. Run the following `dotnet new` command to create a local tool manifest file.

```bash
dotnet new tool-manifest
```

The command creates a file named `.config/dotnet-tools.json`.

3. Run the following `dotnet tool install` command to install ReportGenerator:

```bash
dotnet tool install dotnet-reportgenerator-globaltool
```

This command installs the latest version of ReportGenerator and adds an entry to the tool manifest file.

4. Run the following `dotnet add package` command to add the **coverlet.msbuild** package to the `Tailspin.SpaceGame.Web.Tests` project:

```bash
dotnet add Tailspin.SpaceGame.Web.Tests package coverlet.msbuild
```

5. Run the following `dotnet test` command to run your unit tests and collect code coverage:

> **Note**
> 
> If you're using the PowerShell terminal in Visual Studio, the line continuation character is a backtick (`), so use that character in place of the backslash character (\) for multi-line commands.

```bash
dotnet test --no-build \
  --configuration Release \
  /p:CollectCoverage=true \
  /p:CoverletOutputFormat=cobertura \
  /p:CoverletOutput=./TestResults/Coverage/
```

If the command fails, try running it as follows:

```bash
MSYS2_ARG_CONV_EXCL="*" dotnet test --no-build \
  --configuration Release \
  /p:CollectCoverage=true \
  /p:CoverletOutputFormat=cobertura \
  /p:CoverletOutput=./TestResults/Coverage/
```

This command resembles the one you ran previously. The `/p:` flags tell coverlet which code coverage format to use and where to place the results.

6. Run the following `dotnet tool run` command to use ReportGenerator to convert the Cobertura file to HTML:

```bash
dotnet tool run reportgenerator \
  -reports:./Tailspin.SpaceGame.Web.Tests/TestResults/Coverage/coverage.cobertura.xml \
  -targetdir:./CodeCoverage \
  -reporttypes:HtmlInline_AzurePipelines
```

Many HTML files will appear in the **CodeCoverage** folder at the root of the project.

7. In Visual Studio Code, expand the **CodeCoverage** folder, right-click **index.htm**, and then select **Reveal in File Explorer** (**Reveal in Finder** on macOS or **Open Containing Folder** on Linux).

8. In Windows Explorer (Finder on macOS), double-click **index.htm** to open it in a web browser.

You'll see the coverage report summary.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/6-coverage-report-summary.png)

9. Scroll to the bottom of the page to see a coverage breakdown by class type.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/6-coverage-class-summary.png)

10. Select the link to **TailSpin.SpaceGame.Web.LocalDocumentDBRepository<T>** to view further details.

Notice that the **GetItemsAsync** method is covered by unit tests, but the **CountItemsAsync** method has no coverage.


![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/6-coverage-class-details.png)

This makes sense, because the `FetchOnlyRequestedGameRegion` test method calls the `GetItemsAsync` method, but doesn't call the `CountItemsAsync` method. (To review the test code, look at the **DocumentDBRepository_GetItemsAsyncShould.cs** file.)

## Create a branch

Now that you can build a code coverage report locally, you're ready to add tasks to your build pipeline, which performs the same tasks.

In this section, you'll create a branch named **code-coverage**, based on the **unit-tests** branch, to hold your work. In practice, you'd ordinarily create this branch from the **main** branch.

1. In Visual Studio Code, open the integrated terminal.

2. In the terminal, run the following `git checkout` command to create a branch named **code-coverage**:

```bash
git checkout -B code-coverage
```

## Add build tasks

In this section, you'll add tasks that measure code coverage to your build pipeline.

1. In Visual Studio Code, modify `azure-pipelines.yml` as follows:

```yaml
trigger:
- '*'

pool:
  vmImage: 'ubuntu-20.04'
  demands:
  - npm

variables:
  buildConfiguration: 'Release'
  wwwrootDir: 'Tailspin.SpaceGame.Web/wwwroot'
  dotnetSdkVersion: '6.x'

steps:
- task: UseDotNet@2
  displayName: 'Use .NET SDK $(dotnetSdkVersion)'
  inputs:
    version: '$(dotnetSdkVersion)'

- task: Npm@1
  displayName: 'Run npm install'
  inputs:
    verbose: false

- script: './node_modules/.bin/node-sass $(wwwrootDir) --output $(wwwrootDir)'
  displayName: 'Compile Sass assets'

- task: gulp@1
  displayName: 'Run gulp tasks'

- script: 'echo "$(Build.DefinitionName), $(Build.BuildId), $(Build.BuildNumber)" > buildinfo.txt'
  displayName: 'Write build info'
  workingDirectory: $(wwwrootDir)

- task: DotNetCoreCLI@2
  displayName: 'Restore project dependencies'
  inputs:
    command: 'restore'
    projects: '**/*.csproj'

- task: DotNetCoreCLI@2
  displayName: 'Build the project - $(buildConfiguration)'
  inputs:
    command: 'build'
    arguments: '--no-restore --configuration $(buildConfiguration)'
    projects: '**/*.csproj'

- task: DotNetCoreCLI@2
  displayName: 'Install .NET tools from local manifest'
  inputs:
    command: custom
    custom: tool
    arguments: 'restore'

- task: DotNetCoreCLI@2
  displayName: 'Run unit tests - $(buildConfiguration)'
  inputs:
    command: 'test'
    arguments: '--no-build --configuration $(buildConfiguration) /p:CollectCoverage=true /p:CoverletOutputFormat=cobertura /p:CoverletOutput=$(Build.SourcesDirectory)/TestResults/Coverage/'
    publishTestResults: true
    projects: '**/*.Tests.csproj'

- task: DotNetCoreCLI@2
  displayName: 'Create code coverage report'
  inputs:
    command: custom
    custom: tool
    arguments: 'run reportgenerator -reports:$(Build.SourcesDirectory)/**/coverage.cobertura.xml -targetdir:$(Build.SourcesDirectory)/CodeCoverage -reporttypes:HtmlInline_AzurePipelines'

- task: PublishCodeCoverageResults@1
  displayName: 'Publish code coverage report'
  inputs:
    codeCoverageTool: 'cobertura'
    summaryFileLocation: '$(Build.SourcesDirectory)/**/coverage.cobertura.xml'

- task: DotNetCoreCLI@2
  displayName: 'Publish the project - $(buildConfiguration)'
  inputs:
    command: 'publish'
    projects: '**/*.csproj'
    publishWebProjects: false
    arguments: '--no-build --configuration $(buildConfiguration) --output $(Build.ArtifactStagingDirectory)/$(buildConfiguration)'
    zipAfterPublish: true

- task: PublishBuildArtifacts@1
  displayName: 'Publish Artifact: drop'
  condition: succeeded()
```

This version builds upon your existing configuration. Here's a summary of what's new:

| Azure Pipelines task | Display name | Description |
|---|---|---|
| DotNetCoreCLI@2 | Install .NET tools from local manifest | Installs tools listed in the manifest file, dotnet-tools.json |
| DotNetCoreCLI@2 | Run unit tests - $(buildConfiguration) | Runs unit tests and also collects code coverage in Cobertura format |
| DotNetCoreCLI@2 | Create code coverage report | Converts Cobertura output to HTML |
| PublishCodeCoverageResults@1 | Publish code coverage report | Publishes the report to the pipeline |

## Commit your changes and push the branch to GitHub

Here you push your changes to GitHub and see the pipeline run. Recall that you're currently in the **code-coverage** branch.

Although not required, here you'll add and commit each file separately so that each change is associated with a descriptive commit message.

1. In Visual Studio Code, go to the terminal.

2. Add and commit the **Tailspin.SpaceGame.Web.Tests.csproj** file, which now contains a reference to the **coverlet.msbuild** package:

```bash
git add Tailspin.SpaceGame.Web.Tests/Tailspin.SpaceGame.Web.Tests.csproj
git commit -m "Add coverlet.msbuild package"
```

3. Add and commit the tool manifest file, **dotnet-tools.json**:

```bash
git add .config/dotnet-tools.json
git commit -m "Add code coverage"
```

4. Add and commit **azure-pipelines.yml**, which contains your updated build configuration:

```bash
git add azure-pipelines.yml
git commit -m "Add code coverage"
```

5. Push the **code-coverage** branch to GitHub.

```bash
git push origin code-coverage
```

## Watch Azure Pipelines run the tests

Here, you'll see the tests run in the pipeline and then visualize the results from Azure Test Plans.

1. In Azure Pipelines, trace the build through each of the steps.

2. When the build finishes, go back to the **Summary** page and select the **Code Coverage** tab.

You view the same results that you did when you ran the tests locally.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/6-coverage-report-pipeline.png)

3. As an optional step, you can explore the results from Azure Pipelines.

## Add the dashboard widget

In the previous section, you added the **Test Results Trend** widget to your dashboard, which lets others quickly review test result trends over time.

Here, you'll add a second widget that summarizes code coverage.

1. In a new browser tab, go to [marketplace.visualstudio.com](https://marketplace.visualstudio.com).

2. On the **Azure DevOps** tab, search for **code coverage**.

3. Select **Code Coverage Widgets** (published by Shane Davis).

4. Select **Get it free**.

5. In the drop-down list, select your Azure DevOps organization.

6. Select **Install**.

7. Go back to Azure DevOps.

8. Go to **Overview > Dashboards**.

9. Select **Edit**.

10. Search for **Code Coverage**, and then select **Code Coverage**.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/6-add-code-coverage-widget.png)

11. Drag **Code Coverage** to the canvas.

12. Select the **Gear** icon to configure the widget.

13. Keep all the default settings, except for:
    - **Width**: Enter **2**
    - **Build definition**: Select your pipeline
    - **Coverage measurement**: select **Lines**

14. Select **Save**.

15. Select **Done Editing**.

The widget shows the percentage of code your unit tests cover.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/6-dashboard-widget.png)

You now have code coverage set up in your pipeline. Although your existing code coverage is low, you have a baseline that you can improve over time.

Later, you can configure coverlet to check to see whether your tests provide a minimum threshold of coverage. Your threshold might be 30 percent, 50 percent, or 80 percent coverage, depending on your requirements. The build will fail if your tests cover less than this amount.

## Remove code coverage files

Recall that when you ran Reportgenerator earlier, many HTML files appeared in the **CodeCoverage** folder at the root of the project.

These HTML files aren't intended to be included in source control, and you no longer need them. Although the project's `.gitignore` file is already set up to ignore anything in the **CodeCoverage** directory, it's a good idea to delete these files so that they're not added to your Git repository in future modules.

1. In Visual Studio Code, go to the terminal window, and then, in your project's root directory, run this command:

```bash
rm -rf CodeCoverage/
```



# 3.7 Exercise - Fix a failed test

At this point, you have a way to run unit tests as changes move through the build pipeline. You also have a way to measure the amount of code that's covered by your tests.

It's always a good idea to run your tests locally before you submit changes to the pipeline. But what happens when someone forgets and submits a change that breaks the build?

In this unit, you'll fix a broken build that's caused by a failing unit test. Here, you will:

1. Get starter code from GitHub.
2. Add code coverage tools to your project.
3. Push the code up to your repository.
4. Watch the pipeline automatically run and the unit tests fail.
5. Reproduce the failure locally.
6. Analyze and fix the failure.
7. Push up a fix and watch the build succeed.

## Review the new unit test

The team's latest feature involves the leaderboard. We need to get the number of scores from the database, so we can write a unit test to verify the `IDocumentDBRepository<T>.GetItemsAsync` method.

Here's what the test looks like. You don't need to add any code yet.

```csharp
[TestCase(0, ExpectedResult=0)]
[TestCase(1, ExpectedResult=1)]
[TestCase(10, ExpectedResult=10)]
public int ReturnRequestedCount(int count)
{
    const int PAGE = 0; // take the first page of results

    // Fetch the scores.
    Task<IEnumerable<Score>> scoresTask = _scoreRepository.GetItemsAsync(
        score => true, // return all scores
        score => 1, // we don't care about the order
        PAGE,
        count // fetch this number of results
    );
    IEnumerable<Score> scores = scoresTask.Result;

    // Verify that we received the specified number of items.
    return scores.Count();
}
```

Recall that in an NUnit test, `TestCase` provides inline data to use to test that method. NUnit calls the `ReturnRequestedCount` unit test method like this:

```csharp
ReturnRequestedCount(0);
ReturnRequestedCount(1);
ReturnRequestedCount(10);
```

This test also uses the `ExpectedResult` property to simplify the test code and help make its intention clear. NUnit automatically compares the return value against the value of this property, removing the need to explicitly call the assertion.

We'll choose a few values that represent typical queries. We'll also include 0 to cover that edge case.

## Fetch the branch from GitHub

As you did earlier, fetch the `failed-test` branch from GitHub and check out (or switch to) that branch.

1. In Visual Studio Code, open the integrated terminal.

2. Run the following `git fetch` and `git checkout` commands to download a branch named `failed-test` from the Microsoft repository and switch to that branch:

```bash
git fetch upstream failed-test
git checkout -B failed-test upstream/failed-test
```

We named the branch `failed-test` for learning purposes. In practice, you'd name a branch after its purpose or feature.

3. Run these commands to create a local tool manifest file, install the ReportGenerator tool, and add the `coverlet.msbuild` package to your tests project:

```bash
dotnet new tool-manifest
dotnet tool install dotnet-reportgenerator-globaltool
dotnet add Tailspin.SpaceGame.Web.Tests package coverlet.msbuild
```

You need this step because the `failed-test` branch doesn't contain the work you added to the `unit-tests` branch.

4. Add your test project file and your tool manifest file to the staging index and commit your changes.

```bash
git add Tailspin.SpaceGame.Web.Tests/Tailspin.SpaceGame.Web.Tests.csproj
git add .config/dotnet-tools.json
git commit -m "Configure code coverage tests"
```

5. Run the following `git push` command to upload the `failed-test` branch to your GitHub repository:

```bash
git push origin failed-test
```

## See the test failure in the pipeline

Let's say that you were in a hurry and pushed up your work without running the tests one final time. Luckily, the pipeline can help you catch issues early when there are unit tests. You can see that here.

1. In Azure Pipelines, trace the build as it runs through the pipeline.

2. Expand the **Run unit tests - Release** task as it runs.

You see that the `ReturnRequestedCount` test method fails.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/7-pipeline-test-failure.png)

The test passes when the input value is 0, but it fails when the input value is 1 or 10.

The build is published to the pipeline only when the previous task succeeds. Here, the build wasn't published because the unit tests failed. This prevents others from accidentally obtaining a broken build.

In practice, you won't always manually trace the build as it runs. Here are a few ways you might discover the failure:

**An email notification from Azure DevOps**

You can configure Azure DevOps to send you an email notification when the build is complete. The subject line starts with "[Build failed]" when the build fails.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/7-email-notification.png)

**Azure Test Plans**

In Azure DevOps, select **Test Plans**, and then select **Runs**. You see the recent test runs, including the one that just ran. Select the latest completed test. You see that two of the eight tests failed.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/7-test-run-outcome.png)

**The dashboard**

In Azure DevOps, select **Overview**, and then select **Dashboards**. You see the failure appear in the **Test Results Trend** widget. The **Code Coverage** widget is blank, which indicates that code coverage wasn't run.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/7-dashboard-failed-test.png)


**The build badge**

Although the `failed-test` branch doesn't include the build badge in the README.md file, here's what you would see on GitHub when the build fails:

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/7-badge-failed.png)

## Analyze the test failure

When unit tests fail, you ordinarily have two choices, depending on the nature of the failure:

1. If the test reveals a defect in the code, fix the code and rerun the tests.
2. If the functionality changes, adjust the test to match the new requirements.

### Reproduce the failure locally

In this section, you'll reproduce the failure locally.

1. In Visual Studio Code, open the integrated terminal.

2. In the terminal, run this `dotnet build` command to build the application:

```bash
dotnet build --configuration Release
```

3. In the terminal, run this `dotnet test` command to run the unit tests:

```bash
dotnet test --no-build --configuration Release
```

You should see the same errors that you saw in the pipeline. Here's part of the output:

```
Starting test execution, please wait...
A total of 1 test files matched the specified pattern.
  Failed ReturnRequestedCount(1) [33 ms]
  Error Message:
     Expected: 1
  But was:  0

  Stack Trace:
     at NUnit.Framework.Internal.Commands.TestMethodCommand.Execute(TestExecutionContext context)
   at NUnit.Framework.Internal.Commands.BeforeAndAfterTestCommand.<>c__DisplayClass1_0.<Execute>b__0()
   at NUnit.Framework.Internal.Commands.BeforeAndAfterTestCommand.RunTestMethodInThreadAbortSafeZone(TestExecutionContext context, Action action)

  Failed ReturnRequestedCount(10) [1 ms]
  Error Message:
     Expected: 10
  But was:  9

  Stack Trace:
     at NUnit.Framework.Internal.Commands.TestMethodCommand.Execute(TestExecutionContext context)
   at NUnit.Framework.Internal.Commands.BeforeAndAfterTestCommand.<>c__DisplayClass1_0.<Execute>b__0()
   at NUnit.Framework.Internal.Commands.BeforeAndAfterTestCommand.RunTestMethodInThreadAbortSafeZone(TestExecutionContext context, Action action)


Failed!  - Failed:     2, Passed:     6, Skipped:     0, Total:     8, Duration: 98 ms
```

### Find the cause of the error

You notice that each failed test produces a result that's off by one. For example, when 10 is expected, the test returns 9.

Take a look at the source code for the method that's being tested, `LocalDocumentDBRepository<T>.GetItemsAsync`. You should see this:

```csharp
public Task<IEnumerable<T>> GetItemsAsync(
    Func<T, bool> queryPredicate,
    Func<T, int> orderDescendingPredicate,
    int page = 1, int pageSize = 10
)
{
    var result = _items
        .Where(queryPredicate) // filter
        .OrderByDescending(orderDescendingPredicate) // sort
        .Skip(page * pageSize) // find page
        .Take(pageSize - 1); // take items

    return Task<IEnumerable<T>>.FromResult(result);
}
```

In this scenario, you could check GitHub to see if the file was recently changed.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/7-github-diff.png)

You suspect that `pageSize - 1` is returning one fewer result and that this should be just `pageSize`. In our scenario, this is an error you made when you pushed work without testing, but in a real-world scenario, you could check with the developer who changed the file on GitHub to determine the reason for the change.

> **Tip**
> 
> Discussion and collaboration can also happen on GitHub. You can comment on a pull request or open an issue.

## Fix the error

In this section, you'll fix the error by changing the code back to its original state and running the tests to verify the fix.

1. In Visual Studio Code, open **Tailspin.SpaceGame.Web/LocalDocumentDBRepository.cs** from the file explorer.

2. Modify the `GetItemsAsync` method as shown here:

```csharp
public Task<IEnumerable<T>> GetItemsAsync(
    Func<T, bool> queryPredicate,
    Func<T, int> orderDescendingPredicate,
    int page = 1, int pageSize = 10
)
{
    var result = _items
        .Where(queryPredicate) // filter
        .OrderByDescending(orderDescendingPredicate) // sort
        .Skip(page * pageSize) // find page
        .Take(pageSize); // take items

    return Task<IEnumerable<T>>.FromResult(result);
}
```

This version changes `pageSize - 1` to `pageSize`.

3. Save the file.

4. In the integrated terminal, build the application.

```bash
dotnet build --configuration Release
```

You should see that the build succeeds.

In practice, you might run the app and briefly try it out. For learning purposes, we'll skip that for now.

5. In the terminal, run the unit tests.

```bash
dotnet test --no-build --configuration Release
```

You see that the tests pass.

```
Starting test execution, please wait...
A total of 1 test files matched the specified pattern.

Passed!  - Failed:     0, Passed:     8, Skipped:     0, Total:     8, Duration: 69 ms
```

6. In the integrated terminal, add each modified file to the index, commit the changes, and push the branch up to GitHub.

```bash
git add .
git commit -m "Return correct number of items"
git push origin failed-test
```

> **Tip**
> 
> The dot (.) in this `git add` example is a wildcard character. It matches all unstaged files in the current directory and all subdirectories.
> 
> Before you use this wildcard character, it's a good practice to run `git status` before you commit to ensure that you're staging the files you intend to stage.

7. Return to Azure Pipelines. Watch the change move through the pipeline. The tests pass, and the overall build succeeds.

8. Optionally, to verify the test results, you can select the **Tests** and **Code Coverage** tabs when the build completes.

You can also check out the dashboard to view the updated results trend.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-quality-tests-build-pipeline/media/7-dashboard-passing-test.png)

Great! You've fixed the build. Next, you'll learn how to clean up your Azure DevOps environment.



# 3.8 **Exercise - Clean up your Azure DevOps environment**

You're all done with the tasks for this module. You can now move the work item to the **Done** state on Microsoft Azure Boards and clean up your Microsoft Azure DevOps environment.

## **Important**
This page contains important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes. Be sure to perform the cleanup steps if you ran the template earlier in this module.

## **Disable the pipeline or delete your project**

Each module in this learning path provides a template that you can run to create a clean environment for the duration of the module.

Running multiple templates gives you multiple Azure Pipelines projects, each pointing to the same GitHub repository. This can trigger multiple pipelines to run each time you push a change to your GitHub repository, which can cause you to run out of free build minutes on our hosted agents. Therefore, it's important that you disable or delete your pipeline before you move on to the next module.

Choose one of the following options.

### **Option 1: Disable the pipeline**

This option disables the pipeline so that it doesn't process further build requests. You can reenable the build pipeline later if you want to. Choose this option if you want to keep your Azure DevOps project and your build pipeline for future reference.

**To disable the pipeline:**

1. In Azure Pipelines, navigate to your pipeline.
2. From the drop-down menu, select **Settings**:

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-pipelines-settings-button.png)

3. Under **Processing of new run requests**, select **Disabled**, then select **Save**.

Your pipeline will no longer process build requests.

### **Option 2: Delete the Azure DevOps project**

This option deletes your Azure DevOps project, including what's on Azure Boards and your build pipeline. In future modules, you'll be able to run another template that brings up a new project in a state where this one leaves off. Choose this option to delete your Azure DevOps project if you don't need it for future reference.

**To delete the project:**

1. In Azure DevOps, go to your project. Earlier, we recommended that you name this project **Space Game - web - Tests**.
2. Select **Project settings** in the lower-left corner of the Azure DevOps page.
3. In the **Project details** area, scroll down, and then select **Delete**.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-delete-project.png)

4. In the window that appears, enter the project name, and then select **Delete** a second time.

Your project is now deleted.


# 3.9 **Summary**

Great work. In this module, you added unit tests and code coverage to the build pipeline. You set up dashboard widgets so that others can easily track your improvements. You also fixed a build break before it could reach anyone else.

Defining build tasks locally first helps you understand and verify the process before you add build tasks to your pipeline.

Remember, the process you followed was specific to .NET applications. The tools and tasks that you use depend on the programming language and frameworks that you use to build your applications.

## **Learn more**

In this module, you used the `DotNetCoreCLI@2` task to run unit tests through the `dotnet test` command. If you use Visual Studio to run your tests, you can use the Visual Studio Test task in your build pipeline.

If you're interested in unit testing .NET applications, here are some more resources:

* [Unit test your code](https://docs.microsoft.com/en-us/visualstudio/test/unit-test-your-code)
* [Unit testing C# with NUnit and .NET Core](https://docs.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-nunit)
* [Build, test, and deploy .NET Core apps](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core)

Here's more information about how to analyze your test results:

* [Configure the Test Results Trend (Advanced) widget](https://docs.microsoft.com/en-us/azure/devops/report/dashboards/configure-test-results-trend)
* [Analyze test results](https://docs.microsoft.com/en-us/azure/devops/pipelines/test/review-continuous-test-results-after-build)




# 4 Manage build dependencies with Azure Artifacts

Manage your application and the packages it uses across build Pipelines.

#### Learning objectives
After completing this module, you'll be able to:
- Create and share packages that multiple applications can use.
- Create a build pipeline for your package and publish your package to Azure Artifacts.
- Connect an application to your package and build the application in Azure Pipelines.
- Push changes to your package and update your application to use them.




# 4.1 **Introduction**


In this module, you create a build pipeline that produces a package that multiple apps can use.

It's likely that you used open-source or other partner components in your software. Using components that are popular in the community and have already been built and tested is often the fastest way to get things done.

You might also have your own app code that you can move into a library or package so that others can use it. This code might be an open-source project, or software that only your team can access.

There are many ways to build and host your packages. The right solution depends both on the kinds of programming languages and frameworks you use and who you want to access your packages. Here, you continue your work with the Tailspin web team by creating a NuGet package for .NET that Azure Artifacts hosts.

After you complete this module, you'll be able to:

* Create and share packages that multiple applications can use.
* Create a build pipeline for your package and publish your package to Azure Artifacts.
* Connect an application to your package and build the application in Azure Pipelines.
* Push changes to your package and update your application to use them.

## **Prerequisites**

The modules in this learning path form a progression.

To follow the progression from the beginning, first complete the **Get started with Azure DevOps** learning path.

We also recommend you start at the beginning of this learning path, **Build applications with Azure DevOps**.

If you want to go through just this module, you need to set up a development environment on your Windows, macOS, or Linux system. You need:

* An Azure DevOps organization with access to parallel jobs. If your organization does not have access to parallel jobs, you can request parallel jobs for free for public or private projects using [this form](https://aka.ms/azpipelines-parallelism-request). Your request takes 2-3 business days.
* An Azure subscription
* A GitHub account
* Visual Studio Code with the Azure Pipelines for VS Code extension.
* .NET 8.0 SDK
* Git

You can get started with Azure DevOps for free.

This environment lets you complete the exercises in this and future modules. You can also use it to apply your new skills to your own projects.

> **Note**
> 
> Azure Pipelines support a vast array of **languages and application types**. In this module, you'll be working with a .NET application but you can apply the patterns you learn here to your own projects that use your favorite programming languages and frameworks.

## **Meet the team**

You met the *Space Game* web team at Tailspin Toys in previous modules. As a refresher, here's who you work with in this module.

**Andy** is the development lead.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/andy.png)

**Amita** is in QA.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/amita.png)

**Tim** is in operations.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/tim.png)

**Mara** just joined as a developer and reports to Andy.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/mara.png)


Mara has prior experience with DevOps, and is helping the team adopt a more streamlined process by using Azure DevOps.



# 4.2 **Plan build dependencies for your pipeline**

In this unit, you learn about packaging code to make it easier to share. You discover why you should make packages, the kinds of packages you can create, where you can host the packages, and how you can access them when they're hosted. You also learn about package versioning.

Codebases are always growing larger and more complex. It's unusual for a team to write all the code that their app uses. Instead, the team includes existing code written by other developers. There can be many of these packages, or dependencies, in an app. It's important to actively manage dependencies to be able to maintain them properly and make sure they meet security requirements.

Check in and see how the team is doing. Andy called the team together to talk about a potential change to their code that would help out another team.

## **Team meeting**

**Andy:** Hi everyone. I was chatting with the team that's working on the back end system for Space Game. They could use the models we use for the website in a back-end app they plan to write.

**Amita:** What do you mean by models?

**Andy:** As you know, the Space Game website is an ASP.NET Core application. It uses the Model-View-Controller—or MVC—pattern to separate data from how that data is displayed in the user interface. I was thinking we could create a package that contains our model classes so that any app can use them.

**Amita:** What exactly is the goal?

**Andy:** Both of our teams will share the same database. The game sends the database high scores; we read these scores to display on the leaderboard.

**Amita:** That makes sense. How will we create this package?

**Andy:** That's why I wanted to chat with you. We have a few options, and I'm looking for ideas.

**Tim:** I'd love to help, but first I have some questions. I'm new to this and I want to understand how it all works.

## **What is a package?**

A package contains reusable code that other developers can use in their own projects, even though they didn't write it.

For compiled languages, a package typically contains the compiled binary code, such as .dll files in .NET or .class files in Java. For languages that are interpreted instead of compiled, such as JavaScript or Python, a package might include source code.

Either way, packages are typically compressed to ZIP or a similar format. Package systems often define a unique file extension, such as .nupkg or .jar, to make the package's use clear. Compression can help reduce download time and also produce a single file to simplify management.

Packages also often contain one or more files that provide metadata, or information about the package. This metadata might describe what the package does, specify its license terms, the author's contact information, and the package version.

## **Why should I build a package?**

There are advantages to building a package as opposed to duplicating the code.

One reason to create a package instead of duplicating code is to prevent drift. When code is duplicated, each copy can quickly diverge to satisfy the requirements of a particular app. It becomes difficult to migrate changes from one copy to the others. In other words, you lose the ability to improve the code in ways that benefit everyone.

Packages also group related functionality into one reusable component. Depending on the programming language, a package can provide apps with access to certain types and functions, while restricting access to their implementation details.

Another reason to build a package is to provide a consistent way to build and test the functionality of that package. When code is duplicated, each app might build and test that code in different ways. One set of tests might include checks from which another set could benefit.

One tradeoff is that you have another codebase to test and maintain with a package. You must also be careful when adding features. Generally speaking, a package should contain features that benefit many kinds of apps. For example, Json.NET is a popular NuGet package for .NET that allows you to work with JSON files. Json.NET is open source, so the community can propose improvements and report issues.

When multiple apps can benefit from the same code, the advantages far outweigh the disadvantages. You have just one codebase, just one set of tests, and just one build process to manage.

## **How can I identify dependencies?**

If the goal is to reorganize your code into separate components, you need to identify those pieces of your app that can be removed, packaged to be made reusable, stored in a central location, and versioned. You might even want to replace your own code with partner components that are either open source or that you license.

There are many ways to identify the potential dependencies in your codebase. These approaches include scanning your code for patterns of reuse, and analyzing the architecture of your solution. Here are some ways to identify dependencies:

**Duplicate code.**

If certain pieces of code appear in several places, that's a good indication that you can reuse the code. Centralize these duplicate pieces of code and repackage them appropriately.

**High cohesion and low coupling.**

A second approach is to look for code elements that have a high cohesion to each other and low coupling with other parts of the code. In essence, high cohesion means keeping parts of a codebase that are related to each other in a single place. Low coupling, at the same time, is about separating unrelated parts of the code base as much as possible.

**Individual lifecycle.**

Look for parts of the code that have a similar lifecycle that you can deploy and release individually. If a separate team can maintain this code, it's a good indication you can package it as a component outside of the solution.

**Stable parts.**

Some parts of your codebase might be stable and change infrequently. Check your code repository to find code with a low change frequency.

**Independent code and components.**

Whenever code and components are independent and unrelated to other parts of the system, you can potentially isolate them into separate dependencies.

You can use various tools to assist you in scanning and examining your codebase. Examples range from tools that scan for duplicate code and draw solution dependency graphs to tools that can compute metrics for coupling and cohesion.

## **What kinds of packages are there?**

Each programming language or framework provides its own way to build packages. Popular package systems provide documentation about how the process works.

You might already be familiar with these popular package systems:

* **NuGet:** packages .NET libraries
* **NPM:** packages JavaScript libraries
* **Maven:** packages Java libraries
* **Docker:** packages software in isolated units called containers

## **Where are packages hosted?**

You can host packages on your own network, or you can use a hosting service. A hosting service is often called a package repository or package registry. Many of these services provide free hosting for open-source projects.

Here are some popular hosting services for the package types we just described:

### **NuGet Gallery**

NuGet packages are used for .NET code artifacts. These artifacts include .NET assemblies and related files, tooling and, sometimes, metadata. NuGet defines the way packages are created, stored, and consumed. A NuGet package is essentially a compressed folder structure with files in the ZIP format and has the .nupkg extension.

### **NPM**

An NPM package is used for JavaScript. An NPM package is a file or folder that contains JavaScript files and a package.json file that describes the metadata of the package. For node.js, the package usually contains one or more modules that can be loaded after the package is consumed.

### **Maven Central Repository**

Maven is used for Java-based projects. Each package has a Project Object Model file that describes the metadata of the project, and is the basic unit for defining a package and working with it.

### **Docker Hub**

Docker packages are called images, and contain complete, self-contained deployments. Most commonly, a Docker image represents a software component that can be hosted and run by itself, without any dependencies on other images. Docker images are layered and might be dependent on other images.

A package feed refers to your package repository server. This server can be on the internet or behind your firewall on your network. For example, you can host your own NuGet feeds by using hosting products such as Azure Artifacts and MyGet. You can also host packages on a file share.

When you host packages behind the firewall, you can include feeds to your own packages. You can also cache packages that you trust on your network when your systems can't connect to the internet.

## **What elements make up a good dependency management strategy?**

A good dependency management strategy depends on these three elements:

**Standardization.**

Standardize how you declare and resolve dependencies helps your automated release process remain repeatable and predictable.

**Packaging formats and sources.**

Each dependency should be packaged using the applicable format and stored in a central location.

**Versioning.**

You need to keep track of the changes that occur over time in dependencies just as you do with your own code. This means that dependencies should be versioned.

## **Who can access packages?**

Many package feeds provide unrestricted access to packages. For example, you can download Json.NET from nuget.org, without the need to sign in or authenticate.

Other package feeds require authentication. You can authenticate access to feeds in a few ways. For example, some feeds require a username and password. Other feeds require an access token, which is typically a long series of characters that identifies who you are and to what resources you have access. You can set access tokens to expire after a given period.

## **How are packages versioned?**

The versioning scheme depends on the packaging system you use.

For example, NuGet packages use Semantic Versioning.

Semantic Versioning is a popular versioning scheme. Here's the format:

**Major.Minor.Patch[-Suffix]**

Here's what each of these parameters means:

* A new **Major** version introduces breaking changes. Apps typically need to update how they use the package to work with a new major version.
* A new **Minor** version introduces new features, but is backward-compatible with earlier versions.
* A new **Patch** introduces backward-compatible bug fixes, but not new features.
* The **-Suffix** part is optional and identifies the package as a prerelease version. For example, 1.0.0-beta1 might identify the package as the first beta prerelease build for the 1.0.0 release.

When you reference a package, you do so by version number.

Here's an example of installing a package by using PowerShell and a specific version number:

```powershell
Install-Package Newtonsoft.Json -Version 13.0.1
```

## **What happens when the package changes?**

When you reference a package from your app, you typically pin, or specify, the version of that package you want to use.

Many frameworks let you specify allowable ranges of package versions to install. Some also allow you to specify wildcards, which we call a floating version.

For example, in NuGet, version "1.0" means the first version that's equal to or greater than 1.0. "[1.0]" specifies to install version 1.0 only, and not a newer version.

Here are a few other examples:

| This notation: | Selects: |
|---------------|----------|
| (1.0,) | The first version that's greater than 1. |
| [1.0,2.0] | The first version that's greater than or equal to 1.0, and less than or equal to 2.0 |
| (1.0,2.0) | The first version that's greater than 1.0 and less than 2.0 |
| [1.0,2.0) | The first version that's greater than or equal to 1.0, and less than 2.0 |

As each maintainer releases a new package version, you can evaluate what's changed and test your app against it. When you're ready, you can update the package's version number in your configuration and submit the change to your build pipeline.

Here's an example of how you might include the Newtonsoft.Json package in your C# application's project (.csproj) file. This example specifies version 13.0.1 of that package:

```xml
<ItemGroup>
  <PackageReference Include="Newtonsoft.Json" Version="13.0.1" />
</ItemGroup>
```

## **Check your knowledge**

### **1. What is a package?**

**✅ Reusable code that other developers can use in their own projects.**

❌ A Git construct for moving a repository.

❌ A preview version of your library.

### **2. Say you've built a package that you want to share publicly. What's the easiest way to do that?**

**✅ A public hosting service, such as NuGet.**

❌ On a public network file share.

❌ Behind your firewall.

---

## **Відповіді на запитання:**

**Запитання 1:** Що таке пакет?
**Правильна відповідь:** Багаторазовий код, який інші розробники можуть використовувати у своїх власних проектах.

**Запитання 2:** Припустимо, ви створили пакет, яким хочете поділитися публічно. Який найпростіший спосіб це зробити?
**Правильна відповідь:** Публічний хостинг-сервіс, такий як NuGet.



# 4.3 **What is Azure Artifacts?**

In this unit, you get an overview about how you can use Azure Artifacts to securely create and manage packages that your apps can consume.

Check back in with the team as they decide whether Azure Artifacts is the appropriate way to host their .NET package.

**Mara:** It seems to me that it would make sense for us to host the new Models package in Azure Artifacts. We're all part of the Microsoft Azure DevOps organization already, so authentication would be easier than trying to set it up on a different package manager.

**Andy:** I looked into that before the meeting and it seems straightforward to me. I agree with Mara.

**Amita:** What's Azure Artifacts?

**Andy:** Azure Artifacts is a repository in your Azure DevOps organization where you can manage the dependencies for your codebase. Azure Artifacts can store your artifacts and your binaries. It provides a container, called a feed, for groups of dependencies. Developers who have access to the feed can easily consume or publish packages.

## **How do I create a package and use it in the pipeline?**

**Tim:** So, if I'm understanding right, the app code uses packages from NuGet already. We're going to create our own package and host it in Azure Artifacts. Can you draw out the pieces and how they'll work together? I'm having a hard time picturing the whole process.

**Andy:** Sure. Let's go over the process of creating a package and using it in our Azure DevOps pipeline.

Andy moves to the whiteboard.

*Illustration of a whiteboard diagram showing the steps to create and use a package.*

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-build-dependencies/media/2-azure-artifacts-whiteboard.png)

### **Create the package**

First, create a project in Azure Artifacts. We can create a project from Azure DevOps.

Then, create a pipeline in Azure Pipelines that connects to the GitHub repo for the package code. The pipeline builds the code, packages it, and pushes the package to Azure Artifacts.

You need to update the app that consumes this package to point to the Azure Artifacts feed that we created.

After that, update the pipeline that creates our app. The update allows us to use our Azure Artifacts feed to pull the new package dependency and build as normal.

### **Update the package**

**Tim:** What if someone updates the package?

**Andy:** When you update the package with a new feature or bug fix and run tests to make sure it works correctly, bump up the version number of the package. Then, commit the change. The package pipeline sees the commit and creates a new artifact in Azure Artifacts with the new version number. Don't worry, the old package with the lower version number is still there for apps that depend on that version. This is why you don't typically unlist a package.

Our app might want to use this newer version of the package. In that case, we update the app to reference the newer version and run the tests locally to make sure this new version works with our app. When we're satisfied that everything works, we submit the app change to the pipeline. It builds with the new version of the package dependency.

**Amita:** This sounds like a good plan, and it will help the other team too. It will also keep the code from drifting, as you put it. That will help QA as well.

## **Include a versioning strategy in your build pipeline**

When you use a build pipeline, packages need versions before they can be consumed and tested. However, only after you test the package can you know its quality. Because package versions should never be changed, it becomes challenging to choose a certain version beforehand.

Azure Artifacts associates a quality level with each package in its feeds, and distinguishes between prerelease and release versions. Azure Artifacts offers different views on the list of packages and their versions, which separate them based on their quality level. This approach works well with semantic versioning, which is useful for predicting the intent of a particular version. Azure Artifacts also uses a descriptor to include more metadata from the Azure Artifacts feed. A common use for views is to share package versions that have been tested, validated, or deployed, but hold back packages still under development and not ready for public consumption.

Feeds in Azure Artifacts have three different views by default. These views are added at the moment a new feed is created. The three views are:

* **Release:** The @release view contains all packages that are considered official releases.
* **Prerelease:** The @prerelease view contains all packages that have a label in their version number.
* **Local:** The @local view contains all release and prerelease packages and the packages downloaded from upstream sources.

You can use views to help package-feed consumers to filter between released and unreleased versions of packages. Views allow a consumer to make a conscious decision to choose from released packages, or opt in to prereleases of a certain quality level.

## **Package security in Azure Artifacts**

Ensuring the security of your packages is as important as ensuring the security of the rest of your code. One aspect of package security is securing access to the package feeds. A feed, in Azure Artifacts, is where you store packages. Setting permissions on the feed allows you to share your packages with as many or as few people as your scenario requires.

### **Feed permissions**

Feeds have four levels of access: Owners, Contributors, Collaborators, and Readers. Each level of access has a certain set of permissions. For example, Owners can add any type of identity—individuals, teams, and groups—to any access level. By default, the Project Collection Build Service is a Collaborator and your project team is a Reader.

### **Configure the pipeline to access security and license ratings**

There are several tools available from third parties to help you assess the security and license rating of the software packages you use.

Some of these tools scan the packages as they're included in the build or CD pipeline. During the build process, the tool scans the packages and gives instantaneous feedback. During the CD process, the tool uses the build artifacts and performs scans. Two examples of such tools are Mend Bolt and Black Duck. With Azure DevOps, you use build tasks to incorporate scanning into your pipeline.



# 4.4 **Exercise - Set up your Azure DevOps environment**


In this unit, you ensure that your Microsoft Azure DevOps organization is set up to complete the rest of this module.

To do this configuration, you:

* Set up an Azure DevOps project for this module.
* On Azure Boards, move the work item for this module to the Doing column.
* Make sure your project is set up locally so that you can push changes to the pipeline.

## **Get the Azure DevOps project**

Here, you make sure that your Azure DevOps organization is set up to complete the rest of this module. You do this set up by running a template that creates a project for you in Azure DevOps.

The modules in this learning path form a progression, where you follow the Tailspin web team through their DevOps journey. For learning purposes, each module has an associated Azure DevOps project.

### **Run the template**

Run a template that sets up your Azure DevOps organization.

1. Get and run the ADOGenerator project in Visual Studio or the IDE of your choice.

2. When prompted to **Enter the template number from the list of templates**, enter **27** for **Manage build dependencies with Azure Artifacts**, then press Enter.

3. Choose your authentication method. You can set up and use a Personal Access Token (PAT) or use device sign-in.

> **Note**
> 
> If you set up a PAT, make sure to authorize the necessary scopes. For this module, you can use Full access, but in a real-world situation, you should ensure you grant only the necessary scopes.

4. Enter your Azure DevOps organization name, then press Enter.

5. If prompted, enter your Azure DevOps PAT, then press Enter.

6. Enter a project name such as **Space Game - web - Dependencies**, then press Enter.

After you create your project, go to your Azure DevOps organization in your browser at https://dev.azure.com/<your-organization-name>/ and select the project.

### **Fork the repository**

If you haven't already, create a fork of the mslearn-tailspin-spacegame-web repository.

1. On GitHub, go to the [mslearn-tailspin-spacegame-web](https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web) repository.

2. Select **Fork** at the top-right of the screen.

3. Choose your GitHub account as the Owner, then select **Create fork**.

> **Important**
> 
> The **Clean up your Azure DevOps environment** page in this module contains important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes. Be sure to perform the cleanup steps even if you don't complete this module.

### **Set your project's visibility**

Initially, your fork of the Space Game repository on GitHub is set to public while the project created by the Azure DevOps template is set to private. A public repository on GitHub can be accessed by anyone, while a private repository is only accessible to you and the people you choose to share it with. Similarly, on Azure DevOps, public projects provide read-only access to non-authenticated users, while private projects require users to be granted access and authenticated to access the services.

At the moment, it is not necessary to modify any of these settings for the purposes of this module. However, for your personal projects, you must determine the visibility and access you wish to grant to others. For instance, if your project is open source, you may choose to make both your GitHub repository and your Azure DevOps project public. If your project is proprietary, you would typically make both your GitHub repository and your Azure DevOps project private.

Later on, you may find the following resources helpful in determining which option is best for your project:

* [Use private and public projects](https://docs.microsoft.com/azure/devops/organizations/public/about-public-projects)
* [Change project visibility to public or private](https://docs.microsoft.com/azure/devops/organizations/public/make-project-public)
* [Setting repository visibility](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)

## **Move the work item to Doing**

In this section, you assign a work item to yourself that relates to this module on Azure Boards. You also move the work item to the **Doing** state. In practice, you and your team would create work items at the start of each sprint, or work iteration.

Assigning work in this way gives you a checklist from which to work. It gives others on your team visibility into what you're working on and how much work is left. It also helps the team enforce work-in-progress limits so that the team doesn't take on too much work at one time.

Recall that the team settled on these seven top issues:

*A screenshot of Azure Boards showing a backlog of issues.*

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/build-all-tasks.png)

> **Note**
> 
> Within an Azure DevOps organization, work items are numbered sequentially. In your project, the number assigned to each work item might not match what you see here.

Here, you move the sixth item, **Move model data to its own package** to the **Doing** column, and assign yourself to the work item.

Recall that **Move model data to its own package** relates to moving reusable code to its own NuGet package, so that package can be shared among multiple apps.

*A screenshot of Azure Boards showing work item details for the Move model data to its own package issue.*

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-build-dependencies/media/3-work-item-details.png)

To set up the work item:

1. From Azure DevOps, go to **Boards**, and select **Boards** from the menu.

*A screenshot of Azure DevOps showing the location of the Boards menu.*

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-boards-menu.png)

2. From the **Move model data to its own package** work item, select the down arrow at the bottom of the card, then assign the work item to yourself.

*A screenshot of Azure Boards showing the location of the down arrow.*

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-boards-down-chevron.png)

3. Move the work item from the **To Do** to the **Doing** column.

*A screenshot of Azure Boards, showing the card in the Doing column.*

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-build-dependencies/media/3-azure-boards-wi6-doing.png)

At the end of this module, after you complete the task, you move the card to the **Done** column.

## **Set up the project locally**

Here, you load the Space Game project in Visual Studio Code, configure Git, clone your repository locally, and set the upstream remote so that you can download the starter code.

> **Note**
> 
> If you're already set up with the mslearn-tailspin-spacegame-web project locally, you can move to the next section.

### **Open the integrated terminal**

Visual Studio Code comes with an integrated terminal, so you can edit files and work from the command line all in one place.

1. Start Visual Studio Code.

2. On the **View** menu, select **Terminal**.

3. In the dropdown list, select **bash**. If you're familiar with another Unix shell that you prefer to use, such as Zsh, select that shell instead.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/vscode-terminal-bash.png)

*A screenshot of Visual Studio Code showing the location of the Bash shell.*

The terminal window lets you choose any shell that's installed on your system, like Bash, Zsh, and PowerShell.

Here you'll use Bash. Git for Windows provides Git Bash, which makes it easy to run Git commands.

> **Note**
> 
> On Windows, if you don't see Git Bash listed as an option, make sure you've installed Git, and then restart Visual Studio Code.

4. Run the `cd` command to navigate to the directory you want to work from, like your home directory (`~`). You can choose a different directory if you want.

```bash
cd ~
```

### **Configure Git**

If you're new to Git and GitHub, you first need to run a few commands to associate your identity with Git and authenticate with GitHub.

[Set up Git](https://docs.github.com/get-started/quickstart/set-up-git) explains the process in greater detail.

At a minimum, you'll need to complete the following steps. Run these commands from the integrated terminal:

* Set your username.
* Set your commit email address.
* Cache your GitHub password.

> **Note**
> 
> If you're already using two-factor authentication with GitHub, create a personal access token and use your token in place of your password when prompted later.
> 
> Treat your access token like you would a password. Keep it in a safe place.

### **Set up your project in Visual Studio Code**

In this part, you clone your fork locally so that you can make changes and build out your pipeline configuration.

> **Note**
> 
> If you receive any errors about filenames being too long when you clone your repository, try cloning the repository in a folder that doesn't have a long name or is deeply nested.

### **Clone your fork locally**

You now have a copy of the Space Game web project in your GitHub account. Now you'll download, or clone, a copy to your computer so you can work with it.

A clone, just like a fork, is a copy of a repository. When you clone a repository, you can make changes, verify they work as you expect, and then upload those changes back to GitHub. You can also synchronize your local copy with changes other authenticated users have made to GitHub's copy of your repository.

To clone the Space Game web project to your computer:

1. Go to your fork of the Space Game web project (mslearn-tailspin-spacegame-web) on GitHub.

2. Select **Code**. Then, from the **HTTPS** tab, select the button next to the URL that's shown to copy the URL to your clipboard.

*Locating the URL and copy button from the GitHub repository.*

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/github-clone-button.png)

3. In Visual Studio Code, go to the terminal window.

4. In the terminal, move to the directory you want to work from, like your home directory (`~`). You can choose a different directory if you want.

```bash
cd ~
```

5. Run the `git clone` command. Replace the URL that's shown here with the contents of your clipboard:

```bash
git clone https://github.com/your-name/mslearn-tailspin-spacegame-web.git
```

6. Move to the mslearn-tailspin-spacegame-web directory. This is the root directory of your repository.

```bash
cd mslearn-tailspin-spacegame-web
```

### **Set the upstream remote**

A remote is a Git repository where team members collaborate (like a repository on GitHub). Here you list your remotes and add a remote that points to Microsoft's copy of the repository so that you can get the latest sample code.

1. Run this `git remote` command to list your remotes:

```bash
git remote -v
```

You see that you have both fetch (download) and push (upload) access to your repository:

```
origin  https://github.com/username/mslearn-tailspin-spacegame-web.git (fetch)
origin  https://github.com/username/mslearn-tailspin-spacegame-web.git (push)
```

Origin specifies your repository on GitHub. When you fork code from another repository, it's common to name the original remote (the one you forked from) as upstream.

2. Run this `git remote add` command to create a remote named upstream that points to the Microsoft repository:

```bash
git remote add upstream https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web.git
```

3. Run `git remote` a second time to see the changes:

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

### **Open the project in the file explorer**

In Visual Studio Code, your terminal window points to the root directory of the Space Game web project. To view its structure and work with files, from the file explorer, you'll now open the project.

The easiest way to open the project is to reopen Visual Studio Code in the current directory. To do so, run the following command from the integrated terminal:

```bash
code -r .
```

You see the directory and file tree in the file explorer.

Reopen the integrated terminal. The terminal places you at the root of your web project.

If the `code` command fails, you need to add Visual Studio Code to your system PATH. To do so:

1. In Visual Studio Code, select **F1** or select **View > Command Palette** to access the command palette.
2. In the command palette, enter **Shell Command: Install 'code' command in PATH**.
3. Repeat the previous procedure to open the project in the file explorer.

You're now set up to work with the Space Game source code and your Azure Pipelines configuration from your local development environment.



# 4.5 **Exercise - Create a package feed in Azure Artifacts**


In this unit, you set up Azure Artifacts and create a new feed. You use this feed later to store your new Models package and to consume the package in your app pipeline.

## **Set up Azure Artifacts**

1. From Azure DevOps, go to the **Artifacts** tab, and then select **+ Create feed**.

   1. Name the feed *Tailspin.SpaceGame.Web.Models*.
   2. Under **Visibility**, select **Members of (your organization name)**.
   3. Under **Upstream sources**, unselect **Include packages from common public sources**.

The other choice, to use public sources, is if you want to create an *upstream* from this feed, meaning you can access your packages and packages from public package managers like NuGet or npmjs from this feed.

   4. Under **Scope**, leave the **Project** option selected.
   5. Select **Create**.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-build-dependencies/media/4-setup-azure-artifacts-feed.png)

2. Select **Connect to feed**.

This option has a list of links, commands, and a credential provider you could use if you wanted to run this process locally by using Visual Studio.

> **Note**
> 
> In practice, you'd connect your application to the feed so that you can pull down packages and include them when you build and run your application locally. For brevity, we skip this part.

**Andy:** I've got Azure Artifacts set up. Now, we need to create a pipeline that creates the new package there.



# 4.6 **Exercise - Create a pipeline for your package**

Here, you get the team's new code for the Tailspin.SpaceGame.Web.Models project that's now separate from the Tailspin.SpaceGame.Web project. You create an Azure Pipelines project for the Models project and see the artifact in Azure Artifacts with a version number of 1.0.0 in your feed.

## **What changes were made to the project?**

Recall that the Space Game website is an ASP.NET Core app. It uses the Model-View-Controller (MVC) pattern to separate data from how that data is displayed in the user interface. Andy and Mara want to move the model classes to a separate library so that multiple projects can use those classes.

To do that, they create a new C# project called Tailspin.SpaceGame.Web.Models that contains only the model classes. At the same time, they remove the model classes from their existing project, Tailspin.SpaceGame.Web. They replace the model classes in their existing project with a reference to the Tailspin.SpaceGame.Web.Models project.

To build these projects, Andy and Mara use two pipelines, one for each project. You already have the first project and its associated Azure Pipelines configuration. Here, you fork the second project on GitHub and create an Azure Pipelines configuration to build it. Publish the resulting package to Azure Artifacts.

## **Prepare Visual Studio Code**

Previously, you set up Visual Studio Code to work with the Tailspin.SpaceGame.Web project. Here, you open a second instance of Visual Studio Code so you can work with the Tailspin.SpaceGame.Web.Models project.

1. Open a second instance of Visual Studio Code.

2. From Visual Studio Code, open the integrated terminal.

3. Navigate to the parent directory from where your mslearn-tailspin-spacegame-web project is located. Here's an example that moves to your home directory:

```bash
cd ~
```

## **Get the source code**

Get the source code for the Tailspin.SpaceGame.Web.Models project from GitHub and set up Visual Studio Code so you can work with the files.

### **Create a fork**

The first step is to fork the mslearn-tailspin-spacegame-web-models repository so you can work with and modify the source files. Recall that Mara put the Models directory in a new project and removed it from the web project.

To fork the mslearn-tailspin-spacegame-web-models project into your GitHub account:

1. From a web browser, go to GitHub, and sign in.
2. Go to the [mslearn-tailspin-spacegame-web-models](https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web-models) project.
3. Select **Fork**.
4. To fork the repository into your account, follow the instructions.

### **Clone your fork locally**

To clone the mslearn-tailspin-spacegame-web-models projects to your computer:

1. On GitHub, go to your fork of the mslearn-tailspin-spacegame-web-models project.

2. Select **Code**. Then, from the **HTTPS** tab, select the button next to the URL to copy the URL to your clipboard.

*Screenshot showing the URL and copy button from the GitHub repository.*

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/github-clone-button.png)


3. From Visual Studio Code, go to the terminal window, and run this `git clone` command. Replace the URL with the contents of your clipboard.

```bash
git clone https://github.com/your-name/mslearn-tailspin-spacegame-web-models.git
```

4. Move to the mslearn-tailspin-spacegame-web-models directory. This location is the root directory of your repository.

```bash
cd mslearn-tailspin-spacegame-web-models
```

### **Open the project and examine the configuration**

In Visual Studio Code, your terminal window points to the root directory of the mslearn-tailspin-spacegame-web-models project. Open the project from the file explorer so that you can view its structure and work with files.

The easiest way to open the project is to reopen Visual Studio Code in the current directory. To do so, run the following command from the integrated terminal:

```bash
code -r .
```

You see the directory and file tree in the file explorer.

Reopen the integrated terminal. The terminal places you at the root of your web project.

Open the azure-pipelines.yml file.

You see the steps where the package is built, the version is set, and the package is added to Azure Artifacts.

This `DotNetCoreCLI@2` task builds the project:

```yml
- task: DotNetCoreCLI@2
  displayName: 'Build the project - $(buildConfiguration)'
  inputs:
    command: 'build'
    arguments: '--no-restore --configuration $(buildConfiguration)'
    projects: '**/*.csproj'
```

This `DotNetCoreCLI@2` task packages the project with a version of 1.0.0:

```yml
- task: DotNetCoreCLI@2
  displayName: 'Pack the project - $(buildConfiguration)'
  inputs:
    command: 'pack'
    projects: '**/*.csproj'
    arguments: '--no-build --configuration $(buildConfiguration)'
    versioningScheme: byPrereleaseNumber
    majorVersion: '1'
    minorVersion: '0'
    patchVersion: '0'
```

When developing your package, it's common to use the `byPrereleaseNumber` versioning scheme. This approach appends a unique prerelease suffix such as `-CI-20190621-042647` to the end of the version number. Following this example, the complete version number would be `1.0.0-CI-20190621-042647`.

This `NuGetCommand@2` task pushes the package to your Tailspin.SpaceGame.Web.Models Azure Artifacts feed:

```yml
- task: NuGetCommand@2
  displayName: 'Publish NuGet package'
  inputs:
    command: push
    feedPublish: '$(System.TeamProject)/Tailspin.SpaceGame.Web.Models'
    allowPackageConflicts: true
  condition: succeeded()
```

`feedPublish` specifies the name of the feed to publish to. The format of the name is `<projectName>/<feedName>`, where:

* `$(System.TeamProject)` is a predefined variable that refers to your project name, for example, "Space Game - web - Dependencies".
* `Tailspin.SpaceGame.Web.Models` is the feed name that you provided in the previous exercise.

## **Set permissions**

Before you can set up and run your pipeline, you need to give the Build service the correct permissions.

1. Go to your project in Azure DevOps.
2. Select **Artifacts** from the menu on the left.
3. Select the **Settings** icon at the top-right of the screen, then select the **Permissions** tab.
4. Select the **Add users/groups** button.
5. In the **Users/Groups** field, enter **Space Game - web - Dependencies Build Service**, select the **Contributor** role, and select **Save**.

## **Create the pipeline in Azure Pipelines**

You learned how to set up Azure Pipelines in an earlier module. If you need a refresher, head over to [Create a build pipeline with Azure Pipelines](https://docs.microsoft.com/learn/modules/create-a-build-pipeline/).

Here's how to set up a second pipeline to build the package, and upload that package to Azure Artifacts.

1. From Azure DevOps, go to the **Space Game - web - Dependencies** project.

2. From the menu on the left, select **Pipelines**.

3. Select **New Pipeline**.

4. From the **Connect** tab, select **GitHub**.

5. From the **Select** tab, select **mslearn-tailspin-spacegame-web-models**.

6. If prompted, enter your GitHub credentials. From the page that appears, scroll to the bottom, and select **Approve and install**.

7. From the **Review** tab, you see the new pipeline's azure-pipelines.yml file.

8. Select **Run**.

9. Watch the pipeline run.

10. Go to the **Artifacts** tab.

11. From the dropdown at the top, select **Tailspin.SpaceGame.Web.Models**.

*A screenshot showing the location of the package from the dropdown.*

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-build-dependencies/media/5-feed-dropdown.png)

You see the resulting package, **Tailspin.SpaceGame.Web.Models**, in Azure Artifacts.

*A screenshot of the package in Azure Artifacts, showing version 1.0 of the package.*

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-build-dependencies/media/5-artifacts-package.png)

12. Select the package to go to the details page. Then, copy the version number to a location where you can access it later.

*A screenshot of Azure Artifacts showing package details. Highlighted is the version number for the package.*

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-build-dependencies/media/5-package-details.png)

Use this version number in the next unit.


# 4.7 **Exercise - Reference the package from the application**

In this unit, you get the new Tailspin.SpaceGame.Web code that has the model classes removed. Instead of referencing the models directly, the code references them from the package you created in the previous unit.

Here's a list of the steps:

* Get the new code from a branch of the original Tailspin.SpaceGame.Web repository.
* Reference the new Models package, version 1.0.0.
* To look for this package in your Azure Artifacts feed, change the build pipeline.
* Watch the pipeline successfully build the app.

## **Fetch the branch from GitHub**

Fetch the models-package branch from GitHub and check out, or switch to, that branch.

This branch contains the Space Game project you worked with in the previous modules, but the Models directory has been removed.

1. Switch to your copy of Visual Studio Code that shows the Tailspin.SpaceGame.Web project.

2. From the terminal, to fetch a branch named models-package from the Microsoft repository, run the following git commands. Then, switch to that branch.

```bash
git fetch upstream models-package
git checkout -B models-package upstream/models-package
```

The format of these commands allows you to get starter code from the Microsoft repository on GitHub, known as upstream. Shortly, you'll push this branch up to your GitHub repository, known as origin.

3. As an optional step, verify that the Models directory no longer exists in the file explorer. Instead, you should have Controllers, Views, and other directories.

## **Reference the Models package**

1. Open the Tailspin.SpaceGame.Web.csproj file and add the following ItemGroup:

```xml
<ItemGroup>
  <PackageReference Include="Tailspin.SpaceGame.Web.Models" Version="1.0.0" />
</ItemGroup>
```

Be sure to place the ItemGroup inside the Project node. Your file should resemble this example:

```xml
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net6.0</TargetFramework>
    <ProjectGuid>{A0C4E31E-AC75-4F39-9F59-0AA19D9B8F46}</ProjectGuid>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Tailspin.SpaceGame.Web.Models" Version="1.0.0" />
  </ItemGroup>

  <ItemGroup>
    <Folder Include="wwwroot\images\avatars\" />
  </ItemGroup>
</Project>
```

2. Modify the version, 1.0.0, to include the prerelease prefix that was generated during the build process. Here's an example:

```xml
<PackageReference Include="Tailspin.SpaceGame.Web.Models" Version="1.0.0-CI-20200610-165738" />
```

This entry references the Tailspin.SpaceGame.Web.Models package that you created in Azure Artifacts. Notice the version number, 1.0.0, plus the prerelease suffix. This value matches the initial version that you published to Azure Artifacts in the previous unit.

3. Save the file.

> **Note**
> 
> When you save the file, Visual Studio Code might ask you to restore dependencies. Select the **Restore** button to restore the dependencies.

## **Modify the pipeline configuration**

The models-package branch provides an initial azure-pipelines.yml file. Here, you modify the pipeline configuration to pull the Tailspin.SpaceGame.Web.Models package from Azure Artifacts.

1. From Visual Studio Code, open azure-pipelines.yml.

2. Modify azure-pipelines.yml as shown here:

```yml
trigger:
- '*'

pool:
  vmImage: 'ubuntu-20.04'
  demands:
  - npm

variables:
  buildConfiguration: 'Release'
  wwwrootDir: 'Tailspin.SpaceGame.Web/wwwroot'
  dotnetSdkVersion: '6.x'

steps:
- task: UseDotNet@2
  displayName: 'Use .NET SDK $(dotnetSdkVersion)'
  inputs:
    version: '$(dotnetSdkVersion)'

- task: NuGetToolInstaller@0
  inputs:
    versionSpec: '5.9.1'

- task: Npm@1
  displayName: 'Run npm install'
  inputs:
    verbose: false

- script: './node_modules/.bin/node-sass $(wwwrootDir) --output $(wwwrootDir)'
  displayName: 'Compile Sass assets'

- task: gulp@1
  displayName: 'Run gulp tasks'

- script: 'echo "$(Build.DefinitionName), $(Build.BuildId), $(Build.BuildNumber)" > buildinfo.txt'
  displayName: 'Write build info'
  workingDirectory: $(wwwrootDir)

- task: NuGetCommand@2
  displayName: 'Restore project dependencies'
  inputs:
    command: 'restore'
    restoreSolution: '**/*.sln'
    feedsToUse: 'select'
    vstsFeed: '$(System.TeamProject)/Tailspin.SpaceGame.Web.Models'

- task: DotNetCoreCLI@2
  displayName: 'Build the project - $(buildConfiguration)'
  inputs:
    command: 'build'
    arguments: '--no-restore --configuration $(buildConfiguration)'
    projects: '**/*.csproj'

- task: DotNetCoreCLI@2
  displayName: 'Publish the project - $(buildConfiguration)'
  inputs:
    command: 'publish'
    projects: '**/*.csproj'
    publishWebProjects: false
    arguments: '--no-build --configuration $(buildConfiguration) --output $(Build.ArtifactStagingDirectory)/$(buildConfiguration)'
    zipAfterPublish: true

- task: PublishBuildArtifacts@1
  displayName: 'Publish Artifact: drop'
  condition: succeeded()
```

The highlighted code shows where the pipeline restores dependencies, and looks in your Azure Artifacts feed for the dependencies that might be there.

3. Stage, commit, and push your changes to GitHub.

```bash
git add .
git commit -m "Add reference to Models package"
git push origin models-package
```

4. Go to Azure Pipelines and watch the build run. The build picks up your Models package from Azure Artifacts and builds the project successfully.


# 4.8 **Exercise - Push a change to your package**

At this point, you have two pipelines. One publishes the Models package to Azure Artifacts. The other one is for the Space Game web app. The build configuration for the web app references the Models package so that it can access the model classes.

Here, you practice updating the Models package and consuming that change from the web app.

To do that, start by adding a property to one of the model classes and then bump the package version. Then, submit the change to GitHub so that the pipeline can build the package and publish it to Azure Artifacts.

Then update the web app to reference the newer version number of the Models package so that it can use the added property.

## **Create a branch**

Start by creating a branch that holds your work. Create a branch named add-game-style, which is based off the main branch.

At this point, you have two copies of Visual Studio Code open, one for the Tailspin.SpaceGame.Web.Models project and one for the Space Game web app project, Tailspin.SpaceGame.Web. Work from the copy for the Tailspin.SpaceGame.Web.Models project.

1. From Visual Studio Code, open the integrated terminal.

2. To create a branch named add-game-style, run the following git checkout command in the terminal.

```bash
git checkout -B add-game-style
```

## **Add a property to the Models package**

Add a property named Score to one of the model classes, which provides the game style, or difficulty, with which the score is associated.

Work from the copy of Visual Studio Code for the Tailspin.SpaceGame.Web.Models project.

1. From Visual Studio Code, open Tailspin.SpaceGame.Web.Models/Models/Score.cs. Add the following highlighted property to the list of properties already there.

```csharp
using System.Text.Json.Serialization;

namespace TailSpin.SpaceGame.Web.Models
{
    public class Score : Model
    {
        // The ID of the player profile associated with this score.
        [JsonPropertyName("profileId")]
        public string ProfileId { get; set; }

        // The score value.
        [JsonPropertyName("score")]
        public int HighScore { get; set; }

        // The game mode the score is associated with.
        [JsonPropertyName("gameMode")]
        public string GameMode { get; set; }

        // The game region (map) the score is associated with.
        [JsonPropertyName("gameRegion")]
        public string GameRegion { get; set; }

        // The game style (difficulty) the score is associated with.
        [JsonPropertyName("gameStyle")]
        public string GameStyle { get; set; }
    }
}
```

> **Note**
> 
> You're making a change to a file in the project to demonstrate where you bump up the version number. However, don't update the web app to use the new property.

2. Save the file.

3. To verify your work, build the project:

```bash
dotnet build --configuration Release
```

In practice, you might perform more verification steps, such as running tests or testing the new package with an app that uses it.

## **Build and publish the package**

Now that you added the new property to the Score class and verified the project builds successfully, you can update the package version. You can then push your change to GitHub so that Azure Pipelines can build and publish the updated package.

1. Open azure-pipelines.yml, change the minorVersion from 0 to 1, and save the file.

```yml
minorVersion: '1'
```

Here, you bump the version from 1.0.0 to 1.1.0 to make the change clear. In practice, you'd follow the versioning scheme for the kind of package you're working with.

For example, according to Semantic Versioning, bumping the minor version to 1 (1.1.0) tells others that the package is backward compatible with apps that use version 1.0.0 of that package. The ones who use the package might then modify their app to make use of new features.

Popular open-source projects provide documentation in the form of a changelog that explains the changes made in each version and how to migrate from one major version to the next.

2. Stage, commit, and push your changes:

```bash
git add .
git commit -m "Add GameStyle property"
git push origin add-game-style
```

3. From Microsoft Azure Pipelines, go to the Tailspin.SpaceGame.Web.Models project, and watch the build run.

4. Open the **Artifacts** tab and note the new version. Don't worry; your old version is still there for any projects that still reference it.

*A screenshot of the package in Azure Artifacts, showing version 1.1 of the package.*

As you did previously, write down the new version for the next unit.

## **Reference the new version of the Models package**

Now, change the Tailspin.SpaceGame.Web project to use the new version of the Tailspin.SpaceGame.Web.Models package.

Here, work from the copy of Visual Studio Code for the Space Game web app project, Tailspin.SpaceGame.Web.

1. From Visual Studio Code, open Tailspin.SpaceGame.Web.csproj, and change PackageReference to the version number of the Tailspin.SpaceGame.Web.Models package you created in Azure Artifacts. Then, save the file.

Here's an example:

```xml
<PackageReference Include="Tailspin.SpaceGame.Web.Models" Version="1.1.0-CI-20210528-202436" />
```

If Visual Studio Code asks you to restore packages, you can safely ignore that message. For brevity, we don't build the web app locally.

2. From the terminal, stage, commit, and push the changes.

```bash
git add .
git commit -m "Bump Models package to 1.1.0"
git push origin models-package
```

3. From Azure Pipelines, go to the mslearn-tailspin-spacegame-web project, and watch the build run.

You see from the build output that it gets the latest dependency, builds the app, and publishes the artifact for the web app.



# 4.9 **Exercise - Clean up your Azure DevOps environment**

You're all done with the tasks for this module. Here, you move the work item to the **Done** state on Azure Boards and clean up your Microsoft Azure DevOps environment.

## **Important**

This page contains important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes. Be sure to perform the cleanup steps if you ran the template earlier in this module.

## **Move the work item to Done**

Move the work item you assigned to yourself earlier in this module, "Move model data to its own package," to the **Done** column.

In practice, the definition of "Done" often means having working software in the hands of your users. Here, for learning purposes, mark this work as complete because you set up a build pipeline that publishes NuGet packages to Azure Artifacts.

At the end of each sprint, or work iteration, you and your team might hold a retrospective meeting. You share the work you completed, what went well in the sprint, and what could be improved.

To complete the work item:

1. From Azure DevOps, go to **Boards**, and from the menu, select **Boards**.
2. Move the **Move model data to its own package** work item from the **Doing** column to the **Done** column.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-build-dependencies/media/8-azure-boards-wi6-done.png)

## **Disable the pipeline or delete your project**

Each module in this learning path provides a template you can run to create a clean environment during the module.

Running multiple templates gives you multiple Azure Pipelines projects, each pointing to the same GitHub repository. This approach can trigger multiple pipelines to run each time you push a change to your GitHub repository, which can cause you to run out of free build minutes on our hosted agents. Therefore, it's important that you disable or delete your pipeline before moving on to the next module.

Choose one of the following options.

### **Option 1: Disable the pipeline**

This option disables the pipeline so that it doesn't process further build requests. You can re-enable the build pipeline later if you want to. Select this option if you want to keep your Azure DevOps project and your build pipeline for future reference.

To disable the pipeline:

1. In Azure Pipelines, navigate to your pipeline.
2. From the dropdown, select **Settings**.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-pipelines-settings-button.png)

3. Under **Processing of new run requests**, select **Disabled**, and then select **Save**.

Your pipeline no longer processes build requests.

4. Repeat the process for the second pipeline.

### **Option 2: Delete the Azure DevOps project**

This option deletes your Azure DevOps project, including what's on Azure Boards and your build pipeline. In future modules, you can run another template that creates a new project in a state where this one leaves off. Select this option if you don't need your Azure DevOps project for future reference.

To delete the project:

1. From Azure DevOps, go to your project. Earlier, we recommended that you name this project **Space Game - web - Dependencies**.
2. Select **Project settings** in the lower-left corner.
3. From the **Project details** area, scroll to the bottom, and select **Delete**.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-delete-project.png)


4. From the window that appears, enter the project name and select **Delete** a second time.

Your project is now deleted.


# 4.10 **Summary**

The team has really come a long way. They know how to use Azure Pipelines and Azure Artifacts to create packages and store them in a place where other teams in the company can use them. Azure DevOps is all about sharing and collaboration. Creating reusable code and making it available to others is a great way to foster those values.

Most modern apps have dependencies that need to be managed during the build process. There are many package repositories from which to choose when you're looking for packages to use, or when you're deciding where to store your packages. You can also host your own repository or use a file share.

Sharing code between and among teams helps to reduce development time, because you're not writing the same code more than once. It also reduces testing time, because only one codebase needs to be tested. Any improvements made to the shared code benefit everyone who uses it.

## **Learn more**

Deciding where to host your package depends on many factors. For example:

* Will it be public or private?
* Does the host have the features you need?
* Will you need to authenticate access to the package?
* Are there reasons it needs to be hosted on-premises?

You might need to consider the package's language and the process for accessing it. Here are some resources to check out when you're deciding where to host your packages:

* [Azure Artifacts overview](https://docs.microsoft.com/azure/devops/artifacts/overview)
* [NuGet](https://www.nuget.org/)
* [NPM](https://www.npmjs.com/)
* [Maven](https://maven.apache.org/)
* [Docker](https://www.docker.com/)

To learn more about how to configure secure access to package feeds, see [Manage permissions](https://docs.microsoft.com/azure/devops/artifacts/feeds/feed-permissions).



# 5 Host your own build agent in Azure Pipelines

Learn how to use your own build agent when Microsoft-hosted agents don't meet your needs.

#### Learning objectives
After completing this module, you'll be able to:
- Choose when to use Microsoft-hosted build agents and when to host your own.
- Describe the options you have when you're managing your own build agents.
- Bring up and configure your own agent to work with Azure Pipelines.
- Connect your agent to a pipeline and build your application.
#### Prerequisites
- An Azure DevOps organization
- An Azure subscription
- Visual Studio Code
- .NET 8.0 SDK
- Git
- A GitHub account



# 5.1 **Introduction**

In this module, you'll set up your own build agent running on a Microsoft Azure virtual machine.

Imagine you work for a company called Tailspin Toys, and your team is developing an application called *Space Game*. Up until now, you used a Microsoft-hosted agent that runs Ubuntu to build the *Space Game* web application. Most of the time, a Microsoft-hosted agent can do everything you need.

However, you occasionally need additional processing power, disk space, or time to build your applications. In this module, you'll learn how to set up your own build agent, which can run either in the cloud or on-premises.

## **Learning objectives**

After completing this module, you'll be able to:

* Choose when to use Microsoft-hosted build agents and when to host your own.
* Describe the options you have when you're managing your own build agents.
* Bring up and configure your own agent to work with Azure Pipelines.
* Connect your agent to a pipeline and build your application.

## **Prerequisites**

The modules in this learning path form a progression.

To follow the progression from the beginning, be sure to first complete the **Get started with Azure DevOps** learning path.

We also recommend you start at the beginning of this learning path, **Build applications with Azure DevOps**.

If you want to go through just this module, you need to set up a development environment on your Windows, macOS, or Linux system. You need:

* An Azure DevOps organization
* An Azure subscription
* A GitHub account
* Visual Studio Code
* .NET 8.0 SDK
* Git

You can get started with Azure DevOps for free.

This environment lets you complete the exercises in this and future modules. You can also use it to apply your new skills to your own projects.

> **Note**
> 
> Azure Pipelines support a vast array of **languages and application types**. In this module, you'll be working with a .NET application but you can apply the patterns you learn here to your own projects that use your favorite programming languages and frameworks.


# 5.2 **Choose a Microsoft-hosted or self-hosted build agent**


In this unit, you'll learn about some of the factors to consider when you're choosing a build agent. You'll learn about some of the benefits and limitations of using a Microsoft-hosted agent, and what's involved when you set up your own private build agent.

## **What are build agents and agent pools?**

A build agent is a system that performs build tasks. Think of it as a dedicated server that runs your build process.

Imagine that you have an Azure Pipelines project that receives build requests many times per day, or perhaps you have multiple projects that can each use the same type of build agent. You can organize build agents into agent pools to help ensure that there's a server ready to process each build request.

When a build is triggered, Azure Pipelines selects an available build agent from the pool. If all agents are busy, the process waits for one to become available.

When you use a Microsoft-hosted agent, you specify the VM image to use from the pool. Here's an example from your existing build configuration that uses an Ubuntu 20.04 build agent:

```yml
pool:
  vmImage: 'ubuntu-20.04'
  demands:
  - npm
```

When you use a Microsoft-hosted agent, you use `vmImage` to specify which type of system you need. Microsoft provides many types of VM images, including ones that run Windows, macOS, and various flavors of Linux.

The `demands` section specifies which software or capabilities you require the build machine to have.

When you use a build agent from your own pool, also known as a private pool, you specify the name of your pool. Here's an example:

```yml
pool:
  name: 'MyAgentPool'
  demands:
  - npm
```

When you don't require a `demands` section, you can shorten the syntax like this:

```yml
pool: 'MyAgentPool'
```

You'll create a build agent and add it to a pool later in this module.

## **What kind of agents can I use?**

When you're choosing a build agent, there are two factors to consider:

* The operating system on which you want to build
* Whether you can use a Microsoft-hosted agent or you need to provide your own agent

Azure Pipelines supports these operating systems:

* Windows
* macOS
* Linux

The build agent you choose depends mainly on what tools you use to build your code. For example, if you use Xcode to build your applications, you might choose a macOS agent. If you need Visual Studio, you'd likely choose a Windows agent.

Your existing build configuration uses a Microsoft-hosted agent. Hosted agents run on infrastructure that Microsoft provides for you.

A private agent uses infrastructure that you provide. Your agent can be a system that runs in the cloud or in your datacenter. Either system works, as long as the agent meets your requirements and can connect to Azure Pipelines. In this module, you'll use a VM that runs on Azure, which we provide.

## **When should I use my own build agent?**

For many build tasks, a Microsoft-hosted agent does everything you need. It's the easiest way to get started.

Microsoft takes care of all the security and other operating system updates for you. All you need to do is define the build configuration that you want to run.

Hosted agents also contain software for building many common types of applications. You can add any other software you need during the build process.

Microsoft-hosted agents have a few limitations, which include:

* **Build duration:** A build job can run for up to six hours.
* **Disk space:** Hosted agents provide a fixed amount of storage for your sources and your build outputs. This may not be enough storage.
* **CPU, memory, and network:** Hosted agents run on Microsoft Azure general purpose VMs. Standard_DS2_v2 describes the CPU, memory, and network characteristics you can expect.
* **Interactivity:** You can't sign in to a hosted agent.
* **File shares:** You can't drop build artifacts to Universal Naming Convention (UNC) file shares.

Although hosted agents are relatively easy to set up, there are some benefits to using your own build agents, keeping aside the limitations we just described.

For example, when you use hosted agents, you're sharing infrastructure with other Azure DevOps users. Although it ordinarily takes just seconds to start your build, it can take longer depending on the load on the Microsoft system.

Also, when you use hosted agents, you get a clean system with each build. When you bring your own build agent, you can decide whether to perform a clean build each time or perform an incremental build. With an incremental build, you build upon existing build tools and compiled code. An incremental build can take less time to complete, because the system already has many of the build tools and dependent components installed.

As a tradeoff, because the build infrastructure is yours, it's your responsibility to ensure that your build agents contain the latest software and security patches.

## **How do you set up a private build agent?**

A private build agent contains the software that's required to build your applications. It also contains agent software, which enables the system to connect to Azure Pipelines and receive build jobs.

When you set up a private agent, you provide the infrastructure on which the builds run. This gives you flexibility in how you bring up and maintain your agents.

For example, you can:

**Set up the build agent manually:** You bring up the system, sign in, and interactively install your build tools and the agent software.

**Automate the process:** You bring up the system and run a script or tool to install your build tools and the agent software. You can configure the agent after the system comes online or during the provisioning process.

For example, when you run build agents on Azure, you can use an Azure Resource Manager template (ARM template) or Bicep to bring up the system and configure it to act as a build agent, all in one step. Terraform by HashiCorp is another way to automate the process. Terraform works with many types of infrastructure, including Azure.

**Create an image:** You create an image—or snapshot—of a configured environment. You then use the image to create as many identical systems as you need in your pool.

Manual configuration is a good way to get started, because it allows you to understand the process. It's also the fastest way to get set up when you need just one build agent.

Automation is useful when you need many build agents, or you need to bring up and tear down build infrastructure on a regular basis. You can move from a manual process to an automated process when you need multiple agents.

Images are a form of automation. They can help save time, because all the software is preconfigured. As a tradeoff, you might need to periodically rebuild your images to incorporate the latest OS patches and build tools. Packer by HashiCorp is a popular tool for creating images.

For your Space Game scenario, you decide to use a private build agent.

## **Check your knowledge**

### **1. Let's say you're building a video game. The build process takes two hours to run and uses 18 GB to 20 GB of disk space to compile the game assets. What kind of build agent might you use?**

❌ A Microsoft-hosted agent

✅ **A self-hosted agent**

### **2. Let's say you're building an application that runs on macOS, Linux, and Windows. How might you build the app for each platform you target?**

✅ **Create a build pipeline for each platform.**

✅ **Configure one pipeline to build on each platform.**

❌ Build for one platform and trust that the results run on all platforms.

### **3. A self-hosted build agent:**

❌ Must run on Azure.

✅ **Can run anywhere, including Azure, another cloud, or on-premises.**

❌ Must run on Linux. Use a Microsoft-hosted agent to build Windows applications.



# 5.3 **Exercise - Set up your Azure DevOps environment**

In this unit, you'll ensure that your Microsoft Azure DevOps organization is set up to complete the rest of this module.

To do this, you'll:

* Set up an Azure DevOps project for this module.
* Make sure your project is set up locally so that you can push changes to the pipeline.

## **Get the Azure DevOps project**

Here, you'll make sure that your Azure DevOps organization is set up to complete the rest of this module by running a template that creates a project for you in Azure DevOps.

The modules in this learning path form a progression, where you follow the Tailspin web team through their DevOps journey. For learning purposes, each module has an associated Azure DevOps project.

### **Run the template**

Run a template that sets up your Azure DevOps organization.

1. Get and run the ADOGenerator project in Visual Studio or the IDE of your choice.

2. When prompted to **Enter the template number from the list of templates**, enter **28** for **Host your own build agent in Azure Pipelines**, then press Enter.

3. Choose your authentication method. You can set up and use a Personal Access Token (PAT) or use device login.

> **Note**
> 
> If you set up a PAT, make sure to authorize the necessary scopes. For this module, you can use Full access, but in a real-world situation, you should ensure you grant only the necessary scopes.

4. Enter your Azure DevOps organization name, then press Enter.

5. If prompted, enter your Azure DevOps PAT, then press Enter.

6. Enter a project name such as **Space Game - web - Agent**, then press Enter.

Once your project is created, go to your Azure DevOps organization in your browser (at https://dev.azure.com/<your-organization-name>/) and select the project.

### **Fork the repository**

If you haven't already, create a fork of the mslearn-tailspin-spacegame-web repository.

1. On GitHub, go to the [mslearn-tailspin-spacegame-web](https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web) repository.

2. Select **Fork** at the top-right of the screen.

3. Choose your GitHub account as the Owner, then select **Create fork**.

> **Important**
> 
> The **Clean up your Azure DevOps environment** page in this module contains important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes. Be sure to perform the cleanup steps even if you don't complete this module.

## **Set up the project locally**

Here, you load the Space Game project in Visual Studio Code, configure Git, clone your repository locally, and set the upstream remote so that you can download the starter code.

> **Note**
> 
> If you're already set up with the mslearn-tailspin-spacegame-web project locally, you can move to the next section.

### **Open the integrated terminal**

Visual Studio Code comes with an integrated terminal, so you can edit files and work from the command line all in one place.

1. Start Visual Studio Code.

2. On the **View** menu, select **Terminal**.

3. In the dropdown list, select **bash**. If you're familiar with another Unix shell that you prefer to use, such as Zsh, select that shell instead.

*A screenshot of Visual Studio Code showing the location of the Bash shell.*

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/vscode-terminal-bash.png)

The terminal window lets you choose any shell that's installed on your system, like Bash, Zsh, and PowerShell.

Here you'll use Bash. Git for Windows provides Git Bash, which makes it easy to run Git commands.

> **Note**
> 
> On Windows, if you don't see Git Bash listed as an option, make sure you've installed Git, and then restart Visual Studio Code.

4. Run the `cd` command to navigate to the directory you want to work from, like your home directory (`~`). You can choose a different directory if you want.

```bash
cd ~
```

### **Configure Git**

If you're new to Git and GitHub, you first need to run a few commands to associate your identity with Git and authenticate with GitHub.

[Set up Git](https://docs.github.com/get-started/quickstart/set-up-git) explains the process in greater detail.

At a minimum, you'll need to complete the following steps. Run these commands from the integrated terminal:

* Set your username.
* Set your commit email address.
* Cache your GitHub password.

> **Note**
> 
> If you're already using two-factor authentication with GitHub, create a personal access token and use your token in place of your password when prompted later.
> 
> Treat your access token like you would a password. Keep it in a safe place.

### **Set up your project in Visual Studio Code**

In this part, you clone your fork locally so that you can make changes and build out your pipeline configuration.

> **Note**
> 
> If you receive any errors about filenames being too long when you clone your repository, try cloning the repository in a folder that doesn't have a long name or is deeply nested.

### **Clone your fork locally**

You now have a copy of the Space Game web project in your GitHub account. Now you'll download, or clone, a copy to your computer so you can work with it.

A clone, just like a fork, is a copy of a repository. When you clone a repository, you can make changes, verify they work as you expect, and then upload those changes back to GitHub. You can also synchronize your local copy with changes other authenticated users have made to GitHub's copy of your repository.

To clone the Space Game web project to your computer:

1. Go to your fork of the Space Game web project (mslearn-tailspin-spacegame-web) on GitHub.

2. Select **Code**. Then, from the **HTTPS** tab, select the button next to the URL that's shown to copy the URL to your clipboard.

*Locating the URL and copy button from the GitHub repository.*

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/github-clone-button.png)

3. In Visual Studio Code, go to the terminal window.

4. In the terminal, move to the directory you want to work from, like your home directory (`~`). You can choose a different directory if you want.

```bash
cd ~
```

5. Run the `git clone` command. Replace the URL that's shown here with the contents of your clipboard:

```bash
git clone https://github.com/your-name/mslearn-tailspin-spacegame-web.git
```

6. Move to the mslearn-tailspin-spacegame-web directory. This is the root directory of your repository.

```bash
cd mslearn-tailspin-spacegame-web
```

### **Set the upstream remote**

A remote is a Git repository where team members collaborate (like a repository on GitHub). Here you list your remotes and add a remote that points to Microsoft's copy of the repository so that you can get the latest sample code.

1. Run this `git remote` command to list your remotes:

```bash
git remote -v
```

You see that you have both fetch (download) and push (upload) access to your repository:

```
origin  https://github.com/username/mslearn-tailspin-spacegame-web.git (fetch)
origin  https://github.com/username/mslearn-tailspin-spacegame-web.git (push)
```

Origin specifies your repository on GitHub. When you fork code from another repository, it's common to name the original remote (the one you forked from) as upstream.

2. Run this `git remote add` command to create a remote named upstream that points to the Microsoft repository:

```bash
git remote add upstream https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web.git
```

3. Run `git remote` a second time to see the changes:

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

### **Open the project in the file explorer**

In Visual Studio Code, your terminal window points to the root directory of the Space Game web project. To view its structure and work with files, from the file explorer, you'll now open the project.

The easiest way to open the project is to reopen Visual Studio Code in the current directory. To do so, run the following command from the integrated terminal:

```bash
code -r .
```

You see the directory and file tree in the file explorer.

Reopen the integrated terminal. The terminal places you at the root of your web project.

If the `code` command fails, you need to add Visual Studio Code to your system PATH. To do so:

1. In Visual Studio Code, select **F1** or select **View > Command Palette** to access the command palette.
2. In the command palette, enter **Shell Command: Install 'code' command in PATH**.
3. Repeat the previous procedure to open the project in the file explorer.

You're now set up to work with the Space Game source code and your Azure Pipelines configuration from your local development environment.



# 5.4 **Exercise - Create a build agent that runs on Azure**

In this unit, you'll use a virtual machine that runs on Microsoft Azure to configure a build agent that you can use in Microsoft Azure Pipelines. We provide a virtual machine that you can use for the duration of this module.

In this unit, you will:

* Create an Ubuntu virtual machine on Azure to serve as your build agent.
* Create an agent pool in Microsoft Azure DevOps.
* Create an access token to authenticate your agent with Azure DevOps.
* Configure your agent with the software that's required to build the Space Game website.
* Configure your agent to connect to Azure DevOps so that it can receive build jobs.
* Verify that the agent is connected to Azure DevOps and ready to receive build jobs.

There are many ways to create a virtual machine on Azure. In this unit, you'll create an Ubuntu virtual machine by using an interactive terminal called Cloud Shell.

To configure your VM, you have several choices:

* For a Linux VM, you can connect directly over SSH and interactively configure your system.
* You can automate the deployment by using an ARM template, Bicep, or other automated provisioning tool.
* If you need to deploy many build agents, you can create a VM image that has all the software pre-installed.

Configuring a system interactively is a good way to get started, because it helps you understand the process and what's needed. To simplify the process, connect to your Ubuntu VM over SSH and run shell scripts to set up your build agent.

> **Note**
> 
> If you're unfamiliar with connecting to or configuring Linux systems, just follow along. You can apply the same concepts to Windows build agents.

## **Create a Linux virtual machine**

In this section, you create a VM that's running Ubuntu 20.04, which will serve as your build agent. The VM isn't yet set up to be a build agent or have any of the tools that are required to build the Space Game web application. You'll set that up shortly.

### **Bring up Cloud Shell through the Azure portal**

> **Important**
> 
> To complete the exercises in this module, you need your own Azure subscription.

1. Go to the [Azure portal](https://portal.azure.com) and sign in.

2. From the menu, select **Cloud Shell**. When prompted, select the **Bash** experience.

*A screenshot of the Azure portal showing the location of the Cloud Shell menu item.*

> **Note**
> 
> Cloud Shell requires an Azure storage resource to persist any files that you create in the Cloud Shell. When you first open the Cloud Shell, you're prompted to create a resource group, storage account, and Azure Files share. This setup is automatically used for all future Cloud Shell sessions.

### **Select an Azure region**

A region is one or more Azure datacenters within a geographic location. East US, West US, and North Europe are examples of regions. Every Azure resource, including an Azure VM, is assigned a region.

To make commands easier to run, start by selecting a default region. After you specify the default region, later commands use that region unless you specify a different region.

1. From the Cloud Shell, to list the regions that are available from your Azure subscription, run the following `az account list-locations` command:

```bash
az account list-locations \
  --query "[].{Name: name, DisplayName: displayName}" \
  --output table
```

2. From the **Name** column in the output, select a region that's close to you. For example, choose **eastasia** or **westus2**.

3. Run `az configure` to set your default region. Replace `<REGION>` with the name of the region you selected:

```bash
az configure --defaults location=<REGION>
```

This example sets **westus2** as the default region:

```bash
az configure --defaults location=westus2
```

### **Create a resource group**

Create a resource group to contain the resources used in this training module.

To create a resource group that's named **tailspin-space-game-rg**, run the following `az group create` command:

```bash
az group create --name tailspin-space-game-rg
```

### **Create the VM**

To create your VM, run the following `az vm create` command:

```bash
az vm create \
    --name MyLinuxAgent \
    --resource-group tailspin-space-game-rg \
    --image canonical:ubuntu-24_04-lts:server:latest \
    --size Standard_DS2_v2 \
    --admin-username azureuser \
    --generate-ssh-keys
```

Your VM will take a few minutes to come up.

**Standard_DS2_v2** specifies the VM's size. A VM's size defines its processor speed, amount of memory, initial amount of storage, and expected network bandwidth. This is the same size that's provided by Microsoft-hosted agents. In practice, you can choose a size that provides more computing power or additional capabilities, such as graphics processing.

The `--resource-group` argument specifies the resource group that holds all the things that we need to create. A resource group allows you to administer all the VMs, disks, network interfaces, and other elements that make up our solution as a unit.

## **Create the agent pool**

Recall that an agent pool organizes build agents. In this section, you'll create the agent pool in Azure DevOps. Later, you'll specify the name of the agent pool when you configure your agent so that it can register itself to the correct pool.

1. In Azure DevOps, go to the **Space Game - web - Agent** project.

2. Select **Project settings**.

3. Under **Pipelines**, select **Agent pools**.

*A screenshot of the project settings in Azure DevOps showing the location of the Agent pools menu item.*

![](https://learn.microsoft.com/en-us/training/azure-devops/host-build-agent/media/4-project-settings-agent-pools.png)


4. Select **Add pool**.

5. In the **Add pool** window:

   * Under **Pool to link**, select **New**.
   * Under **Pool type**, select **Self-hosted**.
   * Under **Name**, enter **MyAgentPool**.

In practice, you'd choose a more descriptive name for your pool.

6. Select **Create**. The new agent pool appears in the list.

## **Create a personal access token**

For your build agent to register itself with Azure DevOps, you need a way for it to authenticate itself.

To do that, you can create a personal access token. A personal access token—or PAT—is an alternative to a password. You can use the PAT to authenticate with services such as Azure DevOps.

> **Important**
> 
> As you would with a password, be sure to keep your access token in a safe place. In this section, you'll store your access token as an environment variable so that it doesn't appear in your shell script.

1. In Azure DevOps, open your profile settings, and then select **Personal access tokens**.

*A screenshot of Azure DevOps showing the location of the Personal access tokens menu item.*

![](https://learn.microsoft.com/en-us/training/azure-devops/host-build-agent/media/4-personal-access-token.png)

2. Select **New Token**.

3. Enter a name for your token, such as **Build agent**.

4. Under **Scopes**, select the **Show all scopes** link at the bottom.

5. Look for **Agent Pools**, then select **Read & manage**.

6. Select **Create**.

7. Copy the token to a safe place.

Shortly, you'll use your token to enable your build agent to authenticate access to Azure Pipelines.

## **Connect to your VM**

In this section, you'll connect to your Linux VM over SSH so that you can configure it.

Recall that you can't interactively sign in to a Microsoft-hosted agent. Because a private build agent is your own, you can sign in to and configure it however you'd like.

The ability to connect to your build agent lets you configure it with the tools you need to build your software. It also allows you to troubleshoot issues as you build out your pipeline configuration.

1. To get your VM's IP address, run `az vm show` in Cloud Shell:

```bash
IPADDRESS=$(az vm show \
  --name MyLinuxAgent \
  --resource-group tailspin-space-game-rg \
  --show-details \
  --query [publicIps] \
  --output tsv)
```

This command stores the IP address in a Bash variable named **IPADDRESS**.

2. Print the VM's IP address to the console:

```bash
echo $IPADDRESS
```

3. Create an SSH connection to your VM. In place of `$IPADDRESS`, enter the IP address you received in the previous step. At the prompt, enter **yes** to continue connecting.

```bash
ssh azureuser@$IPADDRESS
```

You're now connected to your VM over SSH.

This command works because you provided the `--generate-ssh-keys` option when you ran `az vm create` earlier. This option creates an SSH key pair, which enables you to sign in to the VM.

## **Install build tools on your VM**

In this section, you'll configure your VM with the tools that are required to build the Space Game website.

Recall that your existing build process uses these tools:

* .NET SDK, which is used to build the application
* Node.js, which is used to perform build tasks
* npm, the package manager for Node.js
* gulp, a Node.js package that's used to minify JavaScript and CSS files

These are the primary tools that the build process requires. To install them, you'll download and run a shell script from GitHub.

> **Note**
> 
> The build process uses other tools, such as node-sass, to convert Sass (.scss) files to CSS (.css) files. However, Node.js installs these tools when the build runs.

Let's start by updating the Ubuntu package manager, named apt. This action fetches the latest information from the package repositories and is ordinarily the first thing you do when you set up a new Ubuntu system.

1. In your SSH connection, update the apt package manager cache:

```bash
sudo apt-get update
```

`sudo` runs the command with administrator, or root, privileges.

2. To download a shell script named `build-tools.sh` from GitHub, run the following `curl` command:

```bash
curl https://raw.githubusercontent.com/MicrosoftDocs/mslearn-tailspin-spacegame-web/main/.agent-tools/build-tools.sh > build-tools.sh
```

3. Print the script to the terminal so that you can examine its contents:

```bash
cat build-tools.sh
```

The following result is displayed:

```bash
#!/bin/bash
set -e

# Select a default .NET version if one is not specified
if [ -z "$DOTNET_VERSION" ]; then
  DOTNET_VERSION=6.0.300
fi

# Add the Node.js PPA so that we can install the latest version
curl -sL https://deb.nodesource.com/setup_16.x | bash -

# Install Node.js and jq
apt-get install -y nodejs

apt-get install -y jq

# Install gulp
npm install -g gulp

# Change ownership of the .npm directory to the sudo (non-root) user
chown -R $SUDO_USER ~/.npm

# Install .NET as the sudo (non-root) user
sudo -i -u $SUDO_USER bash << EOF
curl -sSL https://dot.net/v1/dotnet-install.sh | bash /dev/stdin -c LTS -v $DOTNET_VERSION
EOF
```

The script installs Node.js, npm, gulp, and .NET Core.

By setting the `DOTNET_VERSION` environment variable, you can specify the .NET version to install. If you don't set this variable, the script installs the version that your existing build configuration uses. For learning purposes, you don't set this variable. You allow the script to use the default version.

4. Make the script executable, then run the script:

```bash
chmod u+x build-tools.sh
sudo ./build-tools.sh
```

The script takes a few minutes to run.

In practice, you could now run commands to verify that each software component was successfully installed.

## **Install agent software on your VM**

Now it's time to install the agent software on your VM. This software enables the VM to act as a build agent and receive build jobs from Azure Pipelines.

The registration process checks for installed software before it registers the agent with Azure Pipelines. Therefore, it's important to set up the agent after you install all other software. In practice, you can register the agent a second time if you need to install additional software.

The [documentation](https://docs.microsoft.com/azure/devops/pipelines/agents/v2-linux) explains how to manually set up self-hosted Linux agents as well as macOS and Windows agents. You run a shell script to configure your agent in much the same way you set up build tools in the preceding section.

> **Important**
> 
> The script that you run here is for learning purposes. In practice, you should first understand how each command in the scripts you build affects the overall system. At the end of the module, we'll point to documentation that more completely describes your options.

1. To download a shell script named `build-agent.sh` from GitHub, run the following `curl` command:

```bash
curl https://raw.githubusercontent.com/MicrosoftDocs/mslearn-tailspin-spacegame-web/main/.agent-tools/build-agent.sh > build-agent.sh
```

2. Print the script to the terminal so that you can examine its contents:

```bash
cat build-agent.sh
```

The following result is displayed:

```bash
#!/bin/bash
set -e

# Select a default agent version if one is not specified
if [ -z "$AZP_AGENT_VERSION" ]; then
  AZP_AGENT_VERSION=2.187.2
fi

# Verify Azure Pipelines token is set
if [ -z "$AZP_TOKEN" ]; then
  echo 1>&2 "error: missing AZP_TOKEN environment variable"
  exit 1
fi

# Verify Azure DevOps URL is set
if [ -z "$AZP_URL" ]; then
  echo 1>&2 "error: missing AZP_URL environment variable"
  exit 1
fi

# If a working directory was specified, create that directory
if [ -n "$AZP_WORK" ]; then
  mkdir -p "$AZP_WORK"
fi

# Create the Downloads directory under the user's home directory
if [ -n "$HOME/Downloads" ]; then
  mkdir -p "$HOME/Downloads"
fi

# Download the agent package
curl https://vstsagentpackage.azureedge.net/agent/$AZP_AGENT_VERSION/vsts-agent-linux-x64-$AZP_AGENT_VERSION.tar.gz > $HOME/Downloads/vsts-agent-linux-x64-$AZP_AGENT_VERSION.tar.gz

# Create the working directory for the agent service to run jobs under
if [ -n "$AZP_WORK" ]; then
  mkdir -p "$AZP_WORK"
fi

# Create a working directory to extract the agent package to
mkdir -p $HOME/azp/agent

# Move to the working directory
cd $HOME/azp/agent

# Extract the agent package to the working directory
tar zxvf $HOME/Downloads/vsts-agent-linux-x64-$AZP_AGENT_VERSION.tar.gz

# Install the agent software
./bin/installdependencies.sh

# Configure the agent as the sudo (non-root) user
chown $SUDO_USER $HOME/azp/agent
sudo -u $SUDO_USER ./config.sh --unattended \
  --agent "${AZP_AGENT_NAME:-$(hostname)}" \
  --url "$AZP_URL" \
  --auth PAT \
  --token "$AZP_TOKEN" \
  --pool "${AZP_POOL:-Default}" \
  --work "${AZP_WORK:-_work}" \
  --replace \
  --acceptTeeEula

# Install and start the agent service
./svc.sh install
./svc.sh start
```

You don't need to understand how each line works, but here's a brief summary of what this script does:

1. It downloads the agent package as a .tar.gz file and extracts its contents.
2. In the extracted files, the script:
   * Runs a shell script named `installdependencies.sh` to install the agent software.
   * Runs a shell script named `config.sh` to configure the agent and register the agent with Azure Pipelines.
   * Runs a shell script named `svc.sh` to install and start the agent service.

The script uses environment variables to enable you to provide details about your Azure DevOps organization. Here's a summary:

| Bash variable | Description | Default |
|---------------|-------------|---------|
| AZP_AGENT_VERSION | The version of the agent software to install | The version we last used to test this module |
| AZP_URL | The URL of your Azure DevOps organization | (None) |
| AZP_TOKEN | Your personal access token | (None) |
| AZP_AGENT_NAME | Your agent's name as it appears in Azure DevOps | The system's hostname |
| AZP_POOL | The name of your agent pool | Default |
| AZP_WORK | The working directory for the agent to perform build tasks | _work |

If the script doesn't provide a default value for a variable that's not set, the script prints an error message and immediately exits.

In the steps that follow, set these environment variables:

* AZP_AGENT_VERSION
* AZP_URL
* AZP_TOKEN
* AZP_AGENT_NAME
* AZP_POOL

For now, we recommend that you leave the other variables unset.

3. Set the `AZP_AGENT_NAME` environment variable to specify your agent's name. We recommend **MyLinuxAgent**.

```bash
export AZP_AGENT_NAME=MyLinuxAgent
```

4. Set the `AZP_URL` environment variable to specify the URL to your Azure DevOps organization.

Replace `<organization>` with yours. You can get the name from the browser tab that displays Azure DevOps.

```bash
export AZP_URL=https://dev.azure.com/organization
```

5. Set the `AZP_TOKEN` environment variable to specify your personal access token (the long token value that you copied earlier in this unit).

Replace `<token>` with your token.

```bash
export AZP_TOKEN=token
```

6. Set the `AZP_POOL` environment variable to specify the name of your agent pool. Earlier, you created a pool named **MyAgentPool**.

```bash
export AZP_POOL=MyAgentPool
```

7. Set the `AZP_AGENT_VERSION` environment variable to specify the latest version of the agent.

```bash
export AZP_AGENT_VERSION=$(curl -s https://api.github.com/repos/microsoft/azure-pipelines-agent/releases | jq -r '.[0].tag_name' | cut -d "v" -f 2)
```

A YAML pipeline on a Linux machine must be using the latest version of the agent, even if it's pre-release. The agent software is constantly updated, so you curl the version information from the GitHub repo. The command uses `jq` to read the latest version from the JSON string that's returned.

8. Print the agent version to the console. Optionally, check to make sure this is the latest version.

```bash
echo $AZP_AGENT_VERSION
```

9. Make the script executable, then run it:

```bash
chmod u+x build-agent.sh
sudo -E ./build-agent.sh
```

`sudo` enables the script to run as the root user. The `-E` argument preserves the current environment variables, including the ones you set, so that they're available to the script.

As the script runs, you can see the agent connect to Azure DevOps, see it added to the agent pool, and see the agent connection be tested.

## **Verify that the agent is running**

You've successfully installed the build tools and the agent software on your VM. As a verification step, go to Azure DevOps and see your agent in the agent pool.

1. In Azure DevOps, go to the **Space Game - web - Agent** project.

2. Select **Project settings**.

3. Under **Pipelines**, select **Agent pools**.

4. Select **MyAgentPool**.

5. Select the **Agents** tab.

You can see that your agent is online and ready to accept build jobs.

*A screenshot of Azure DevOps showing the status of the private agent. The agent shows as online, idle, and enabled.*

![](https://learn.microsoft.com/en-us/training/azure-devops/host-build-agent/media/4-project-settings-agent-details.png)

> **Tip**
> 
> If your build agent shows as **Offline**, try waiting a few moments and then refreshing the page.

6. Select your agent, **MyLinuxAgent**.

7. Select the **Capabilities** tab.

During setup, the configuration process scanned your build agent for tool capabilities. You see that **npm** is listed as one of them. Recall that your original build configuration specified that npm must be installed on the agent.

*A screenshot of Azure DevOps showing a few of the agent's capabilities. The npm capability is highlighted.*

![](https://learn.microsoft.com/en-us/training/azure-devops/host-build-agent/media/4-project-settings-agent-capabilities.png)

When you specify which agent pool to use, you can include any of these entries in your `demands` section. Including them ensures that Azure Pipelines chooses a build agent that has the software you need to build your application. It also enables you to create agent pools with various software configurations. Azure Pipelines will select the correct configuration based on your requirements.



# 5.5 **Exercise - Build the application using your agent**

Now that your build agent is running and ready to receive build jobs, let's see it in action. In this unit, you'll modify a basic build configuration that we provide to build the Space Game website by using your agent and not the Microsoft-hosted agent.

> **Note**
> 
> Run the following steps immediately after performing the steps in the previous module **Create a build agent that runs on Azure**.

At the end of this unit, as an optional step, you can remove the agent pool from your Microsoft Azure DevOps organization.

## **Fetch the branch from GitHub**

In this section, you'll fetch the build-agent branch from GitHub and check out, or switch to, that branch.

This branch contains the Space Game project that you worked with in previous modules and an Azure Pipelines configuration to start with.

1. In Visual Studio Code, open the integrated terminal.

2. To download a branch named build-agent from the Microsoft repository and switch to that branch, run the following `git fetch` and `git checkout` commands:

```bash
git fetch upstream build-agent
git checkout -B build-agent upstream/build-agent
```

Recall that `upstream` refers to the Microsoft GitHub repository. Your project's Git configuration understands the upstream remote, because you set up that relationship when you forked the project from the Microsoft repository and cloned it locally.

Shortly, you'll push this branch up to your GitHub repository, known as `origin`.

3. Optionally, in Visual Studio Code, open the azure-pipelines.yml file and familiarize yourself with the initial configuration.

The configuration resembles the basic one that you created in the **Create a build pipeline with Azure Pipelines** module. It builds only the application's release configuration.

## **Modify the build configuration**

In this section, you'll modify the build configuration to switch from using a Microsoft-hosted agent to using the agent from your build pool.

1. In Visual Studio Code, open the azure-pipelines.yml file, then look for the `pool` section.

```yml
pool:
  vmImage: 'ubuntu-20.04'
  demands:
  - npm
```

2. Modify the `pool` section as shown here:

```yml
pool:
  name: 'MyAgentPool'
  demands:
  - npm
```

This version uses `name` to specify your agent pool, **MyAgentPool**. It maintains the `demands` section to specify that the build agent must have npm, the Node.js package manager, installed.

3. In the integrated terminal, add azure-pipelines.yml to the index, commit the changes, and push the branch up to GitHub.

```bash
git add azure-pipelines.yml
git commit -m "Use private agent pool"
git push origin build-agent
```

## **Watch Azure Pipelines use your build agent**

Watch the build run in the pipeline by using your build agent.

1. In Azure DevOps, go to the **Space Game - web - Agent** project.

2. On the project page or in the left pane, select **Pipelines**.

3. Select your pipeline from **Recently run pipelines**, and choose the most recent run (that was started when you updated the pipeline to use the MyAgentPool pool).

4. Choose **Job** and trace the run through each of the steps.

From the **Initialize job** task, you see that the build uses your build agent.

*A screenshot of Azure Pipelines running the build. The Initialize job task shows that it's running the build on the private agent named MyLinxuAgent.*

![](https://learn.microsoft.com/en-us/training/azure-devops/host-build-agent/media/5-build-results-private-pool.png)

## **Optional: Remove your build pool**

For future reference, you can keep the build pool configuration in your Azure DevOps organization, but keep in mind that the VM that hosts the agent will no longer be available to you after you perform the cleanup steps at the end of this module.

In fact, Azure DevOps will detect that the agent is offline. Azure Pipelines will check for an available agent the next time a build is queued by using the MyAgentPool pool.

*A screenshot of the agent pool in Azure DevOps showing that the build agent is offline.*

![](https://learn.microsoft.com/en-us/training/azure-devops/host-build-agent/media/5-agent-pools-offline-agent.png)

As an optional step, you can remove the build pool configuration from Azure DevOps. Here's how:

1. In Azure DevOps, go to the **Space Game - web - Agent** project.

2. Select **Project settings**.

3. Under **Pipelines**, select **Agent pools**.

*A screenshot of the project settings in Azure DevOps showing the location of the Agent pools menu item.*

![](https://learn.microsoft.com/en-us/training/azure-devops/host-build-agent/media/4-project-settings-agent-pools.png)

4. Under **MyAgentPool**, select the trash can icon, then select **Delete**.

*A screenshot of Azure DevOps showing the location of where to remove the agent from the agent pool.*

![](https://learn.microsoft.com/en-us/training/azure-devops/host-build-agent/media/5-agent-pools-delete-agent.png)




# 5.6 **Exercise - Clean up your Azure DevOps environment**

You're all done with the tasks for this module. In this unit, we'll help you clean up your Microsoft Azure DevOps environment.

## **Important**

This page contains important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes. Be sure to perform the cleanup steps if you ran the template earlier in this module.

## **Clean up Azure resources**

Here, you'll delete your Azure VM. The easiest way to delete resources is to delete their parent resource group. When you delete a resource group, you delete all resources in that group.

In the **Create a release pipeline with Azure Pipelines** module, you managed Azure resources through the Azure portal. Here, you'll tear down your deployment by using the Azure CLI through Azure Cloud Shell. The steps are similar to the steps that you used when you created the resources.

To clean up your resource group:

1. Go to the [Azure portal](https://portal.azure.com), and sign in.

2. From the menu bar, select **Cloud Shell**. When prompted, select the **Bash** experience.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-portal-menu-cloud-shell.png)

3. To delete the resource group that you used, `tailspin-space-game-rg`, run the following `az group delete` command:

```bash
az group delete --name tailspin-space-game-rg
```

When prompted, to confirm the operation, enter `y`.

> **Note**
> 
> If you're still signed in to SSH in Cloud Shell window from the previous step, run the `exit` command to exit SSH, then run the `az group delete` command.

4. As an optional step, after the previous command finishes, run the following `az group list` command:

```bash
az group list --output table
```

You should see that the resource group `tailspin-space-game-rg` no longer exists.

## **Disable the pipeline or delete your project**

Each module in this learning path provides a template that you can run to create a clean environment for the duration of the module.

Running multiple templates creates multiple Azure Pipelines projects, each pointing to the same GitHub repository. This action can cause multiple pipelines to run each time you push a change to your GitHub repository. This action, in turn, can cause you to run out of free build minutes on your hosted agents. Therefore, it's important to disable or delete your pipeline before you move on to the next module.

Choose either of the next two options.

### **Option 1: Disable the pipeline**

This option disables the pipeline so that it doesn't process further build requests. You can reenable the build pipeline later if you want to. Choose this option if you want to keep your DevOps project and your build pipeline for future reference.

To disable the pipeline:

1. In Azure Pipelines, go to your pipeline.

2. From the **More actions** menu (**...**), select **Settings**.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-pipelines-settings-button.png)

4. Under **Processing of new run requests**, select **Disabled**, then select **Save**.

Your pipeline will no longer process build requests.

### **Option 2: Delete the Azure DevOps project**

This option deletes your Azure DevOps project, including what's on Azure Boards and your build pipeline. In future modules, you'll be able to run another template that brings up a new project in a state where this one leaves off. Choose this option if you don't need your DevOps project for future reference.

To delete the project:

1. In Azure DevOps, go to your project. Earlier, we recommended that you name this project **Space Game - web - Agent**.

2. Select **Project settings** in the lower-left corner of the Azure DevOps page.

3. In the **Project details** area, scroll down and select **Delete**.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-delete-project.png)

4. In the window that appears, enter the project name, then select **Delete** a second time.

Your project is now deleted.


# 5.7 **Summary**


In this module, you set up your own private build agent by using a virtual machine that runs on Microsoft Azure.

Although a Microsoft-hosted agent often does everything you need, there are times when you might consider using your own build agent.

There are a few factors to consider when you decide to use a Microsoft-hosted agent rather than use your own. These factors include how much compute power and disk space you need and how much time is required for your builds to run.

When you configure a private build agent, it's yours to configure however you want. As a tradeoff, you also need to keep your system updated with the latest security patches and build tools.

## **Learning path summary**

Congratulations. You've completed the final module in the *Build applications with Azure DevOps* learning path. In this learning path, you accomplished a lot, including:

* Setting up a project in Azure Pipelines and publishing build artifacts to the pipeline.
* Implementing a code workflow for the team members that uses Git and GitHub.
* Running automated tests, such as unit and code coverage tests, when the pipeline runs.
* Managing your own packages in the pipeline and connecting them to your applications.
* Using your own build agents when Microsoft-hosted agents don't meet your needs.

The focus of this learning path is on building applications and receiving build artifacts that you can hand off to your QA or operations teams.

## **Learn more**

For more self-paced, hands-on learning around Azure DevOps, check out [Azure DevOps Labs](https://azuredevopslabs.com/).

To learn more about build agents and agent pools, see the following articles:

* [Azure Pipelines agents](https://docs.microsoft.com/azure/devops/pipelines/agents/agents)
* [Agent pools](https://docs.microsoft.com/azure/devops/pipelines/agents/pools-queues)
* [Self-hosted Linux agents](https://docs.microsoft.com/azure/devops/pipelines/agents/v2-linux)
* [Self-hosted macOS agents](https://docs.microsoft.com/azure/devops/pipelines/agents/v2-osx)
* [Self-hosted Windows agents](https://docs.microsoft.com/azure/devops/pipelines/agents/v2-windows)
* [Container jobs](https://docs.microsoft.com/azure/devops/pipelines/process/container-phases)
* [Pool (YAML schema)](https://docs.microsoft.com/azure/devops/pipelines/yaml-schema/pool)
* [Build on multiple platforms](https://docs.microsoft.com/azure/devops/pipelines/get-started-multiplatform)

### **Configure release pipelines**

To learn how to configure release pipelines that continuously build, test, and deploy your applications, go to [Deploy applications with Azure DevOps](https://docs.microsoft.com/learn/paths/deploy-applications-with-azure-devops/).

### **Create your own VM images**

If you're interested in creating your own VM images for use with Azure Pipelines, check out the [azure-pipelines-image-generation](https://github.com/actions/virtual-environments) project on GitHub.

### **Practice running VMs on Azure**

For more hands-on practice working with virtual machines on Azure, check out the [Administer infrastructure resources in Azure](https://docs.microsoft.com/learn/paths/administer-infrastructure-resources-in-azure/) learning path.

We also mentioned how you can use Bicep to automate the process of creating build agents. To learn more about Bicep, see [Fundamentals of Bicep](https://docs.microsoft.com/learn/paths/fundamentals-bicep/).
