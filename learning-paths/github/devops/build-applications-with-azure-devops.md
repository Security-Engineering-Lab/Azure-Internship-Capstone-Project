


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

   ![Screenshot of the Space Game website running in a web browser.]

   You can interact with the page, including the leaderboard. When you select a player's name, you see details about that player.

2. When you're finished, return to the terminal window, and select **Ctrl+C** to stop the running application.

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

   ![Screenshot of the Space Game website with updated text. The text contains a spelling error.]

7. When you're finished, return to the terminal window, and then press **Ctrl+C** to stop the running application.

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

   ![Screenshot of GitHub showing the new branch.]

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

   ![Screenshot of GitHub confirming that the branch can be merged.]

   **Important:** Again, this step is important because you can't merge your changes into the Microsoft repository.

   When you work directly with your own repository, and not a fork, your **main** branch is selected by default.

6. Enter a title and a description for your pull request.
   * **Title**: *Improve the text at the top of the home page*
   * **Description**: *Received the latest home page text from the product team.*

7. To complete your pull request, select **Create pull request**.

   This step doesn't merge any code. It tells others that you have changes that you're proposing to merge.

   The pull request window is displayed. As before, a pull request triggers Azure Pipelines to build your application by default.

8. Optionally, select the **Details** link or go to your project on Azure DevOps and watch the pipeline run.

9. When the build is finished, go back to your pull request on GitHub.

10. Select **Merge pull request**, and then select **Confirm merge**.

11. Select **Delete branch** to delete the **feature/home-page-text** branch from GitHub.

