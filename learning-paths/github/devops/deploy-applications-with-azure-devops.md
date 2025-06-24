
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


# 1.2 What is continuous delivery?

Here, you'll follow the Tailspin team as they discuss how a continuous delivery (CD) pipeline can help them with their upcoming release.

The Tailspin team is starting to feel better about their build process. They have an automated process running on Azure Pipelines, which means the build environment is stable. Amita knows immediately when she needs to test an artifact. She finds fewer bugs because Andy and Mara have started to add unit tests and code quality tests. Life is looking good. Let's check in with the team.

## Morning meeting

The team is in the meeting room waiting for Irwin, the product manager, who wants to talk to them. They look forward to telling him about their progress. But when Irwin walks in, he doesn't look happy. He starts talking right away.

**Irwin:** I had a meeting this morning with the management team. They want to know why we're taking so long to release our games and websites. Our closest competitors get new features and new games out there much faster than we do. We need to speed up things. I'm not alerting just you. I'm alerting all the teams. What can we do to help your team deploy faster?

**Andy:** This is a little sudden, but we're a bit ahead of you. We've been automating how we build our websites. Maybe now it's time to extend our automation to our release process.

**Irwin:** How would you do that?

**Mara:** We created an automated build pipeline by using Azure Pipelines. It builds an artifact that Amita can test. We could also build a continuous delivery (CD) pipeline.

**Irwin:** What's a CD pipeline?

Mara begins to explain, but is interrupted when Irwin's cell phone beeps. Irwin reads a text message and mutters under his breath.

**Irwin:** I'm sorry, but this is urgent. I have to go. Why don't you all figure out this CD business and get back to me soon?

Andy looks around at his team.

**Andy:** Coffee?

Andy and the rest of the team head to the coffee shop to create a plan.

## What is continuous delivery?

The team is meeting over coffee to figure how to set up a continuous delivery workflow.

**Andy:** Mara, can you tell us what you know about continuous delivery?

**Mara:** To me, CD and DevOps are inseparable. Remember that we defined DevOps as the union of people, processes, and products to enable continuous delivery of value to our end users.

CD by itself is a set of processes, tools, and techniques that enable rapid, reliable, and continuous delivery of software. So CD isn't only about setting up a pipeline, although that part is important. CD is about setting up a working environment where:

- We have a reliable and repeatable process for releasing and deploying software.
- We automate as much as possible.
- We don't put off doing something that's difficult or painful; instead, we do it more often so that we figure out how to make it routine.
- We keep everything in source control.
- We all agree that done means released.
- We build quality into the process. Quality is never an afterthought.
- We're all responsible for the release process. We no longer work in silos.
- We always try to improve.

We've already put many of these ideas into place, and we all agree they've improved how we work. CD is an extension of what we've already started.

## Why do I need continuous delivery?

CD helps software teams deliver reliable software updates to their customers at a rapid cadence. CD also helps ensure that both customers and stakeholders have the latest features and fixes quickly.

Let's continue to listen in on the team as they talk this out.

**Andy:** Thanks, Mara. We need CD because, as we all know, the world has changed. New features are being released faster. Updates and bug fixes need to be available right away. It isn't just our management that wants to speed up our releases. Management is simply reacting to the demands of our customers. If customers can't get what they want from us, they'll go somewhere else.

**Tim:** Agreed! I can't wait to get started.

**Andy:** Thanks, everyone. I'm going to propose that Mara and I put together a simple proof of concept (POC). I think everything will be a lot easier to understand if you can see a CD pipeline in action.

**Amita:** Good luck, you two.

The team leaves Andy and Mara to work out the details.

## How does continuous delivery compare to right-click publishing?

Many development tools provide ways to publish your application directly to some target environment, such as Microsoft Internet Information Services (IIS) or Azure. For example, you can Publish an ASP.NET Core app to Azure by using Visual Studio. This process is sometimes called **right-click publishing**.

Right-click publishing is a great way to quickly build a prototype. For example, you might right-click publish your application to Azure so that you can share a new idea with your team. However, this technique has limitations.

Continuous delivery provides a consistent way for you and your team to continuously test, deploy, and monitor your application each time you check in your code. When you right-click publish your application, there's no guarantee that the code was properly tested, or will behave as expected under real-world usage.

In this short video, Abel Wang, Cloud Advocate at Microsoft, explains more.

## How does continuous delivery compare to continuous deployment?

In the DevOps community, you might hear the terms **continuous delivery** and **continuous deployment**. Do these terms mean the same thing? In this short video, Abel explains the difference.

## What continuous delivery tools can I use?

After the meeting ends, Andy and Mara plan the next steps. They use Azure Pipelines to build their software. They want to consider what tools, including Azure Pipelines, are available to help them with their release process.

**Mara:** Where do you want to start?

**Andy:** First, we need to agree on our release-management tool. Let's make sure the tool we choose:

- Supports our version control system.
- Can deploy to multiple environments so that we can test and validate our work.
- Makes it easy to define our deployment tasks.
- Is easy to extend.

**Mara:** Azure DevOps integrates with several other continuous integration (CI) and CD solutions. Many solutions are out there, and we're not invested in any of them. If we were, it would make sense to use that one. Popular CI and CD systems include Jenkins, Circle CI, GitLab, Travis CI, and Azure Pipelines.

These tools have similarities, but each of them also has particular strengths. Some of these tools are open source, some are free, and some you have to pay for. They also provide built-in integrations with other software tools.

For example, Jenkins is open source. It has many plug-ins, and many companies use it. You can run Circle CI in the cloud or on-premises. I think we'd need to customize it. GitLab is a single application for the entire software development life cycle. It might be bigger than we want right now. We can keep using Azure Pipelines.

Here's a short video where Abel talks about using DevOps best practices to deploy code to Azure.

**Mara:** My vote is to stay with Azure Pipelines.

**Andy:** I agree. Azure Pipelines has worked great for us so far, and we don't have to learn another new technology.

**Mara:** Great. Let's get started on the pipeline details.

Andy and Mara move to a conference room to plan their CD pipeline.


#  1.3  Plan a release pipeline by using Azure Pipelines

In this section, you'll follow along with Andy and Mara as they plan a basic CD pipeline that runs on Azure Pipelines.

When it's done, they'll demo it to the rest of the team. The pipeline will serve as a POC on which they'll improve and expand as they learn more and get feedback from Tim and Amita.

## What are the parts of a basic CD pipeline?

A basic CD pipeline contains a trigger to get the process going and at least one stage, or deployment phase. A stage is made up of jobs. A job is a series of steps that defines how to build, test, or deploy your application.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/3-whiteboard-1.png)

**Andy:** We already have the ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-01.png) build artifact. It's the .zip file that our existing build pipeline creates. But how do we deploy it to a ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-02.png) live environment?

## What is a pipeline stage?

A stage is a part of the pipeline that can run independently and be triggered by different mechanisms. A mechanism might be the success of the previous stage, a schedule, or even a manual trigger. You'll learn more about these mechanisms in the next module.

**Mara:** We could have a stage that builds the app and another stage that runs tests.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/3-whiteboard-3.png)

**Mara:** We've already defined the tasks for the build stage in our pipeline. Our deployment stage can be similar, including tasks that deploy the build to an environment.

The question is, where should we deploy the artifact?

## What is an environment?

You've likely used the term environment to refer to where your application or service is running. For example, your production environment might be where your end users access your application.

Following this example, your production environment might be:

- A physical machine or virtual machine (VM).
- A containerized environment, such as Kubernetes.
- A managed service, such as Azure App Service.
- A serverless environment, such as Azure Functions.

An artifact is deployed to an environment. Azure Pipelines makes it easy to deploy to almost any kind of environment, whether it's on-premises or in the cloud.

In Azure Pipelines, the term environment has a second meaning. Here, an environment is an abstract representation of your deployment environment, such as a Kubernetes cluster, an App Service instance, or a virtual machine.

An Azure Pipelines environment records the deployment history to help you identify the source of changes. By using Azure Pipelines environments, you can also define security checks and ways to control how an artifact is promoted from one stage of a pipeline to another. What an environment includes depends on what you want to do with the artifact. An environment where you want to test the artifact is probably defined differently than one where you want to deploy the artifact for your end users.

One way to define an Azure Pipelines environment is with a YAML file. Your YAML file includes an environment section, which specifies the Azure Pipelines environment, where you'll deploy your artifact.

As you plan your release pipeline, you'll need to decide where your application or service will run. Let's listen in and see what Andy and Mara decide.

**Andy:** At a high level, what type of environment do we want? Do we want to deploy on-premises or to the cloud?

**Mara:** We could ask Tim to create a VM for us in the lab, but he's always running out of hardware. It'll be fast and easy to set up a POC ourselves if we use the cloud.

**Andy:** I agree; but there are so many cloud options to consider, and we can use Azure Pipelines to deploy to any of them. Which should we try?

**Mara:** The teams that develop our games use Azure to host some of their back-end systems. They set it up quickly and seem to like it. I think we should stick with Azure for our cloud.

**Andy:** OK, that makes sense! But Azure provides so many compute options. Which should we pick?

Andy lists these options on the whiteboard:

- Virtual machines
- Containers
- Azure App Service
- Serverless computing

> **Note**
> 
> You'll find more information on each of these compute options at the end of this module.

**Mara:** I know containers and serverless computing are popular right now. Compared to VMs, they're both lightweight in terms of resources. They're also easy to replace and scale out. Both are interesting, but I'm nervous about learning two new technologies at the same time. I'd rather concentrate just on building the pipeline.

**Andy:** I'm with you. That leaves VMs or App Service. I think VMs would be a better choice if we were moving a line-of-business app—one that requires full access to some particular environment—to the cloud. We're not doing anything that significant.

**Mara:** That leaves App Service, which would be my choice. It's designed to work with Azure DevOps, and it comes with advantages. It's a platform as a service (PaaS) environment for web apps, so it takes a lot of the burden off us. We won't have to worry about infrastructure. It also comes with security features and lets us perform load balancing and automatic scaling.

**Andy:** App Service sounds like what we need. Let's use App Service. We're creating just a proof of concept anyway. We can always change the compute option if we want to try something else later.

## How does Azure Pipelines perform deployment steps?

To deploy your application, Azure Pipelines first needs to authenticate with the target environment. Azure Pipelines provides different authentication mechanisms. The one you use depends on the target environment to which you're deploying. You'll find more information about these mechanisms at the end of this module.

**Andy:** We have our build artifact, and we know we'll build and deploy in stages of the pipeline. We've also defined the target environment for our deployment. That's App Service. My question now is, how does Azure Pipelines authenticate with App Service? I know this will be one of Tim's concerns. We need to ensure the process is secure.

After a bit of research, Andy and Mara come up with the general steps that allow Azure Pipelines to deploy to App Service:

1. Specify the target deployment environment in the pipeline configuration.
2. Provide a way for Azure Pipelines to authenticate access to that environment.
3. Use Azure Pipelines tasks to deploy the build artifact to that environment.

**Mara:** According to our research, we need to create a service connection to specify the target environment and authenticate access to it. After we define the service connection, it'll be available for all of our tasks to use. Then we need to use the built-in tasks `DownloadPipelineArtifact@2` to download the build artifact to the pipeline agent and `AzureWebApp@1` to deploy our application to Azure App Service.

## What are jobs and strategies?

Your existing build pipeline defines a build agent, pipeline variables, and the tasks needed to build your software.

The deployment part of your pipeline contains these same elements. Your deployment configuration typically also defines one or more jobs, a pipeline environment, and strategies. You learned about pipeline environments earlier.

Here's an example configuration that you'll run later in this module. This configuration deploys the Space Game website to Azure App Service.

```yaml
- stage: 'DeployDev'
  displayName: 'Deploy to dev environment'
  dependsOn: Build
  jobs:
  - deployment: Deploy
    pool:
      vmImage: 'ubuntu-20.04'
    environment: dev
    variables:
    - group: 'Release Pipeline'
    strategy:
      runOnce:
        deploy:
          steps:
          - download: current
            artifact: drop
          - task: AzureWebApp@1
            displayName: 'Azure App Service Deploy: website'
            inputs:
              azureSubscription: 'Resource Manager - Tailspin - Space Game'
              appName: '$(WebAppName)'
              package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/*.zip'
```

### Jobs

A job is a series of steps—or tasks—that run sequentially as a unit. Every pipeline stage has one job by default, even when that stage doesn't use the job keyword.

A job can run in an agent pool, on a container, or directly on the Azure DevOps server. The example job shown here runs on a Microsoft-hosted Ubuntu agent.

You can specify the conditions under which each job runs. The example job shown here doesn't define any conditions. By default, a job runs if it doesn't depend on any other job, or if all of the jobs on which it does depend have finished successfully.

You can also run jobs in parallel or sequentially. Using your existing build pipeline as an example, you can use parallel jobs to build your software on Windows, Linux, and macOS agents simultaneously.

A deployment job is a special type of job that plays an important role in your deployment stages. Deployment jobs record the status of your deployments in Azure Pipelines, providing you with an audit trail. Deployment jobs also help you define your deployment strategy, which we'll do shortly.

### Strategies

A strategy defines how your application is rolled out. You'll learn more about strategies such as blue-green and canary in a future module. For now, you'll use the `runOnce` strategy to download the Space Game package from the pipeline and deploy it to Azure App Service.

## How does Azure Pipelines connect to Azure?

To deploy your app to an Azure resource, such as a virtual machine or App Service, you need a service connection. A service connection provides secure access to your Azure subscription by using one of the two methods:

- Service principal authentication
- Managed identities for Azure resources

You can learn more about these security models at the end of this module, but in short:

A **service principal** is an identity with a limited role that can access Azure resources. Think of a service principal as a service account that can do automated tasks on your behalf.

**Managed identities** for Azure resources are a feature of Microsoft Entra ID that simplifies the process of working with service principals. Because managed identities exist on the Microsoft Entra tenant, Azure infrastructure can automatically authenticate the service and manage the account for you.

Managed identities simplify the process of working with service principals; but in this module, we'll be using service principal authentication because a service connection can automatically discover your Azure resources and assign the appropriate service principal roles for you.

## The plan

Andy and Mara are ready to begin. They're going to:

1. Build on their existing Azure Pipelines build configuration.
2. Define a build stage that creates the artifact.
3. Define a deployment stage that deploys the artifact to App Service.


![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/3-whiteboard-4.png)

**Andy:** Is this drawing correct? We use Azure Pipelines ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-01.png) to deploy to Azure App Service ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-02.png). To do that, we take the build artifact ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-03.png) as the input to the deployment stage ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-04.png). The tasks in the deployment stage download the artifact ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-05.png) and use a service connection to deploy the artifact to App Service ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-06.png).

**Mara:** That about sums it up. Let's get started.

---

## Check your knowledge

### 1. You have a great idea for a new web app. You have working code on your laptop, but you want feedback from your team before you continue. What's the fastest way to deploy your app to Azure so you can share it with your team?

- [ ] Build a CI/CD pipeline in Azure Pipelines.
- [ ] Use Visual Studio to right-click publish your app.
- [ ] Run xcopy to upload the web app to a virtual machine (VM) that's running on Azure.

### 2. To deploy to Azure App Service, what resources does Azure Pipelines need?

- [ ] A build artifact and a service connection.
- [ ] A host name and an SSH key.
- [ ] A host name and the encrypted username and password.

### 3. Which of the following statements describes the relationship among tasks, stages, and jobs?

- [ ] A task is another name for a job. A stage can contain either tasks or jobs.
- [ ] Stages break down into jobs, and jobs break down into tasks.
- [ ] Stages break down into tasks. A job schedules when each stage runs.

---

## Відповіді на запитання:

**1. You have a great idea for a new web app. You have working code on your laptop, but you want feedback from your team before you continue. What's the fastest way to deploy your app to Azure so you can share it with your team?**
✅ **Use Visual Studio to right-click publish your app.**

Для швидкого прототипування та демонстрації ідеї команді найшвидшим способом є right-click publishing з Visual Studio, хоча це не підходить для production середовища.

**2. To deploy to Azure App Service, what resources does Azure Pipelines need?**
✅ **A build artifact and a service connection.**

Для розгортання в Azure App Service потрібен build artifact (результат збірки) та service connection (для автентифікації з Azure).

**3. Which of the following statements describes the relationship among tasks, stages, and jobs?**
✅ **Stages break down into jobs, and jobs break down into tasks.**

Ієрархія в Azure Pipelines: Stages (етапи) → Jobs (роботи) → Tasks (завдання). Кожен етап містить роботи, а кожна робота містить завдання.



# 1.4 Exercise - Set up your environment


The team has been slowly integrating a DevOps strategy into their processes. In this section, you make sure that your environment reflects the team's efforts so far.

To do this, you:

- Add a user to ensure Azure DevOps can connect to your Azure subscription.
- Set up an Azure DevOps project for this module.
- Add the build pipeline.

## Add a user to Azure DevOps

To complete this module, you need your own Azure subscription. You can get started with Azure for free.

Although you don't need a subscription to use Azure DevOps to work in it, here you'll use Azure DevOps to deploy to Azure resources that exist in your Azure subscription. To simplify the process, sign in to both your Azure subscription and your Azure DevOps organization under the same Microsoft account.

If you use different Microsoft accounts to sign in to Azure and Azure DevOps, add a user to your DevOps organization under the Microsoft account you use to sign in to Azure. For more information, see [Add organization users and manage access](https://docs.microsoft.com/azure/devops/organizations/accounts/add-organization-users). When you add the user, choose the **Basic** access level.

Then, sign out of Azure DevOps and sign in again under the Microsoft account you use to sign in to your Azure subscription.

## Get the Azure DevOps project

Make sure your Azure DevOps organization is set up to complete the rest of this module. You'll do this by running a template that creates a project for you in Azure DevOps.

The modules in this learning path form a progression as you follow the Tailspin web team through their DevOps journey. For learning purposes, each module has an associated Azure DevOps project.

### Run the template

Run a template that sets up your Azure DevOps organization.

1. Get and run the ADOGenerator project in Visual Studio or the IDE of your choice.

2. When prompted to **Enter the template number from the list of templates**, enter **29** for **Create a release pipeline with Azure Pipelines**, then press **Enter**.

3. Choose your authentication method. You can set up and use a Personal Access Token (PAT) or use device login.

   > **Note**
   > 
   > If you set up a PAT, make sure to authorize the necessary scopes. In this module, you can use **Full access**, but in a real-world situation, you should ensure you grant only the necessary scopes.

4. Enter your Azure DevOps organization name, then press **Enter**.

5. If prompted, enter your Azure DevOps PAT, then press **Enter**.

6. Enter a project name such as **Space Game - web - Release**, then press **Enter**.

7. Once your project is created, go to your Azure DevOps organization in your browser (at `https://dev.azure.com/<your-organization-name>/`) and select the project.

> **Important**
> 
> The **Clean up your Azure DevOps environment** page in this module contains important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes. Be sure to perform the cleanup steps even if you don't complete this module.

### Set your project's visibility

Initially, your fork of the Space Game repository on GitHub is set to public while the project created by the Azure DevOps template is set to private. A public repository on GitHub can be accessed by anyone, while a private repository is only accessible to you and the people you choose to share it with. Similarly, on Azure DevOps, public projects provide read-only access to non-authenticated users, while private projects require users to be granted access and authenticated to access the services.

At the moment, it is not necessary to modify any of these settings for the purposes of this module. However, for your personal projects, you must determine the visibility and access you wish to grant to others. For instance, if your project is open source, you may choose to make both your GitHub repository and your Azure DevOps project public. If your project is proprietary, you would typically make both your GitHub repository and your Azure DevOps project private.

Later on, you may find the following resources helpful in determining which option is best for your project:

- [Use private and public projects](https://docs.microsoft.com/azure/devops/organizations/projects/about-projects)
- [Change project visibility to public or private](https://docs.microsoft.com/azure/devops/organizations/projects/make-project-public)
- [Setting repository visibility](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)

## Prepare Visual Studio Code

Set up Visual Studio Code so you can build the website locally and use the source files.

Visual Studio Code comes with an integrated terminal so you can edit files and work from the command line, all from one place.

1. Start Visual Studio Code.

2. Select **Terminal**, and then select **New Terminal**.

3. In the dropdown list, select **Git bash**. If you're familiar with another Unix shell that you prefer to use, such as Zsh, select that shell instead. Git for Windows provides Git Bash, which makes it easy to run Git commands.

   > **Note**
   > 
   > On Windows, if you don't see Git Bash listed as an option, make sure you've installed Git, and then restart Visual Studio Code.

4. Run the following command to navigate to your home directory.

```bash
cd ~
```

### Configure Git

If you're new to Git and GitHub, you'll first need to run a few commands to associate your identity with Git and authenticate with GitHub. For more information, see [Set up Git](https://docs.github.com/get-started/quickstart/set-up-git).

At a minimum, you'll need to complete the following steps:

1. Download and install the latest version of Git.
2. Set your username.
3. Set your commit email address.

> **Note**
> 
> If you're already using two-factor authentication with GitHub, create a personal access token. Use your token in place of your password when you're prompted later.
> 
> Treat your access token like you would treat a password. Keep it in a safe place.

## Set up your project in Visual Studio Code

1. On GitHub, go to the [mslearn-tailspin-spacegame-web-deploy](https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web-deploy) repository.

2. Select **Fork** at the top-right of the screen.

3. Choose your GitHub account as the **Owner**, then select **Create fork**.

### Clone your fork locally

1. On GitHub, go to your fork of the Space Game web project (`mslearn-tailspin-spacegame-web-deploy`).

2. Select **Code**, and then, from the **HTTPS** tab, select the copy button to copy the URL to your clipboard.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/github-clone-button.png)

3. In Visual Studio Code, go to the terminal window you opened earlier.

4. Run the `git clone` command. Replace the URL that's shown here with the contents of your clipboard:

```bash
git clone https://github.com/your-name/mslearn-tailspin-spacegame-web-deploy.git
```

5. Move to the `mslearn-tailspin-spacegame-web-deploy` directory. This directory is the root of your repository.

```bash
cd mslearn-tailspin-spacegame-web-deploy
```

### Set the upstream remote

A remote is a Git repository where team members collaborate (like a repository on GitHub). Here you list your remotes and add a remote that points to Microsoft's copy of the repository so that you can get the latest sample code.

1. Run the following command to list your remotes:

```bash
git remote -v
```

You see that you have both fetch (download) and push (upload) access to your repository:

```
origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (fetch)
origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (push)
```

**Origin** specifies your repository on GitHub. When you fork code from another repository, the original remote (the one you forked from) is commonly named **upstream**.

2. Run the following command to create a remote named **upstream** that points to the Microsoft repository:

```bash
git remote add upstream https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web-deploy.git
```

3. Run `git remote` a second time to see the changes:

```bash
git remote -v
```

You see that you still have both fetch (download) and push (upload) access to your repository. You also now have fetch access from the Microsoft repository:

```
origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (fetch)
origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (push)
upstream        https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web-deploy.git (fetch)
upstream        https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web-deploy.git (push)
```

### Open the project in Visual Studio Code

1. Run the following command from the root directory of your project.

```bash
code .
```

2. Reopen the integrated terminal. The terminal places you at the root of your web project.

If the `code` command fails, you need to add Visual Studio Code to your system PATH. To do so:

1. In Visual Studio Code, select **F1** or select **View > Command Palette** to access the command palette.
2. Type **shell command** and find the **Shell Command: Install 'code' command in PATH** command.
3. Restart the terminal for the new PATH to take effect.

You're now set up to work with the Space Game source code and your Azure Pipelines configuration from your local development environment.

## Fetch the branch from GitHub

1. In Visual Studio Code, open the integrated terminal.

2. Run the following commands to fetch the `release-pipeline` branch from the MicrosoftDocs repository, and check out a new branch `upstream/release-pipeline`.

```bash
git fetch upstream release-pipeline
git checkout -B release-pipeline upstream/release-pipeline
```

3. As an optional step, in Visual Studio Code, open the `azure-pipelines.yml` file and familiarize yourself with the initial YAML pipeline configuration.

## Run the pipeline

At this point, you have:

- A fork of the `mslearn-tailspin-spacegame-web-deploy` repository in your GitHub account.
- The `mslearn-tailspin-spacegame-web-deploy` repository cloned locally.
- A branch named `release-pipeline` that contains the web site source code and an initial Azure Pipelines configuration.

Next, you'll manually trigger the pipeline to run. This step ensures that your project is set up to build from your GitHub repository. The initial pipeline configuration builds the application and produces a builds artifact.

1. Navigate to your project in Azure DevOps, and then select **Pipelines**.

2. Select the **mslearn-tailspin-spacegame-web-deploy** pipeline. If prompted, make sure you select **Authorize resources** to authorize the service connection.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/4-pipeline-no-runs.png)


3. Select **Run pipeline**, and then select the **release-pipeline** branch from the **Branch/tag** dropdown menu. Select **Run**.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/4-pipeline-run-first.png)

4. In the **Summary** page, select your pipeline job to view the logs.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/pipeline-trace-build.png)

5. After the build finishes, select the back button to return to the summary page.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/pipeline-navigate-pipeline-summary.png)

6. Select your published artifact.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/pipeline-navigate-published-artifact.png)

The **Tailspin.Space.Game.Web.zip** is your build artifact. This file contains your built application and its dependencies.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/pipeline-view-published-artifact.png)
You now have a build pipeline for the Space Game web project. Next, you'll add a deployment stage to deploy your build artifact to Azure App Service.

**Next unit:** Exercise - Deploy the web application to Azure App Service

# 1.5 Exercise - Deploy the web application to Azure App Service

In this module, you create a multistage pipeline to build and deploy your application to Azure App Service. You learn how to:

- Create an App Service instance to host your web application.
- Create a multistage pipeline.
- Deploy to Azure App Service.

## Create the App Service instance

1. Sign in to the [Azure portal](https://portal.azure.com).

2. Select **App Services** from the left pane.

3. Select **Create > Web App** to create a new Web App.

4. On the **Basics** tab, enter the following values.

| Setting | Value |
|---------|--------|
| **Project Details** | |
| Subscription | your subscription |
| Resource Group | Select **Create new**, and then enter **tailspin-space-game-rg**, and select **OK**. |
| **Instance Details** | |
| Name | Provide a unique name, such as **tailspin-space-game-web-1234**. This name must be unique across Azure. It becomes part of the domain name. In practice, choose a name that describes your service. Note the name for later. |
| Publish | Code |
| Runtime stack | .NET 8 (LTS) |
| Operating System | Linux |
| Region | Select a region, preferably one close to you. |
| **Pricing plans** | |
| Linux Plan | Accept the default. |
| Pricing plan | Select the **Basic B1** pricing tier from the drop-down menu. |

5. Select **Review + create**, review the form, and then select **Create**. The deployment takes a few moments to complete.

6. When deployment is complete, select **Go to resource**. The App Service Essentials displays details related to your deployment.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/5-app-service-details.png)

7. Select the URL to verify the status of your App Service.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/5-default-home-page.png)

> **Important**
> 
> The **Clean up your Azure DevOps environment** page in this module explains how to tear down your App Service instance after you're done with it. Cleaning up helps ensure that you're not charged for Azure resources after you complete this module. Make sure you follow the cleanup steps even if you don't complete this module.

## Create a service connection

> **Important**
> 
> Make sure that you're signed in to Azure and Azure DevOps under the same Microsoft account.

1. In Azure DevOps, go to your **Space Game - web - Release** project.

2. From the lower-left corner of the page, select **Project settings**.

3. Under **Pipelines**, select **Service connections**.

4. Select **Create service connection**, and then select **Azure Resource Manager** then select **Next**.

5. Select **Service principal (automatic)**, and then select **Next**.

6. Fill out the required fields as follows: If prompted, sign in to your Microsoft account.

| Field | Value |
|-------|-------|
| Scope level | Subscription |
| Subscription | Your Azure subscription |
| Resource Group | tailspin-space-game-rg |
| Service connection name | Resource Manager - Tailspin - Space Game |

7. Ensure that **Grant access permission to all pipelines** is selected.

8. Select **Save**.

## Add the Build stage to your pipeline

A multistage pipeline allows you to define distinct phases that your change passes through as it's promoted through the pipeline. Each stage defines the agent, variables, and steps required to carry out that phase of the pipeline. In this section, you define one stage to perform the build. You define a second stage to deploy the web application to App Service.

To convert your existing build configuration to a multistage pipeline, you add a `stages` section to your configuration, and then you add one or more `stage` sections for each phase of your pipeline. Stages break down into jobs, which are a series of steps that run sequentially as a unit.

1. From your project in Visual Studio Code, open **azure-pipelines.yml** and replace its contents with this code:

```yaml
trigger:
- '*'

variables:
  buildConfiguration: 'Release'

stages:
- stage: 'Build'
  displayName: 'Build the web application'
  jobs: 
  - job: 'Build'
    displayName: 'Build job'
    pool:
      vmImage: 'ubuntu-20.04'
      demands:
      - npm

    variables:
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

    - publish: '$(Build.ArtifactStagingDirectory)'
      artifact: drop
```

2. From the integrated terminal, run the following commands to stage, commit, and then push your changes to your remote branch.

```bash
git add azure-pipelines.yml
git commit -m "Add a build stage"
git push origin release-pipeline
```

3. In Azure Pipelines, navigate to your pipeline to view the logs.

4. After the build finishes, select the back button to return to the summary page and check the status of your pipeline and published artifact.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/5-pipeline-build-stage-summary.png)

## Create the dev environment

An environment is an abstract representation of your deployment environment. You can use environments to define specific criteria for your release, such as which pipeline is authorized to deploy to the environment. You can also use environments to set up manual approvals for specific user/group to approve before deployment is resumed.

1. From Azure Pipelines, select **Environments**.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/pipelines-environments.png)

2. Select **Create environment**.

3. Under **Name**, enter **dev**.

4. Leave the remaining fields at their default values.

5. Select **Create**.

## Store your web app name in a pipeline variable

The Deploy stage that we're creating uses the name to identify to which App Service instance to deploy; for example, **tailspin-space-game-web-1234**.

Although you could hard-code this name in your pipeline configuration, defining it as a variable makes your configuration more reusable.

1. In Azure DevOps, select **Pipelines** and then select **Library**.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/5-pipelines-library.png)

2. Select **+ Variable group** to create a new variable group.

3. Enter **Release** for the variable group name.

4. Select **Add** under **Variables** to add a new variable.

5. Enter **WebAppName** for the variable name and your App Service instance's name for its value: for example, **tailspin-space-game-web-1234**.

6. Select **Save**.

## Add the deployment stage to your pipeline

We extend our pipeline by adding a deployment stage to deploy the Space Game to App Service using the `download` and `AzureWebApp@1` tasks to download the build artifact and then deploy it.

1. From Visual Studio Code, replace the contents of **azure-pipelines.yml** with the following yaml:

```yaml
trigger:
- '*'

variables:
  buildConfiguration: 'Release'

stages:
- stage: 'Build'
  displayName: 'Build the web application'
  jobs: 
  - job: 'Build'
    displayName: 'Build job'
    pool:
      vmImage: 'ubuntu-20.04'
      demands:
      - npm

    variables:
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

    - publish: '$(Build.ArtifactStagingDirectory)'
      artifact: drop

- stage: 'Deploy'
  displayName: 'Deploy the web application'
  dependsOn: Build
  jobs:
  - deployment: Deploy
    pool:
      vmImage: 'ubuntu-20.04'
    environment: dev
    variables:
    - group: Release
    strategy:
      runOnce:
        deploy:
          steps:
          - download: current
            artifact: drop
          - task: AzureWebApp@1
            displayName: 'Azure App Service Deploy: website'
            inputs:
              azureSubscription: 'Resource Manager - Tailspin - Space Game'
              appName: '$(WebAppName)'
              package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/*.zip'
```

Notice the highlighted section and how we're using the `download` and `AzureWebApp@1` tasks. The pipeline fetches the `$(WebAppName)` from the variable group we created earlier.

Also notice how we're using `environment` to deploy to the **dev** environment.

2. From the integrated terminal, add **azure-pipelines.yml** to the index. Then commit the change and push it up to GitHub.

```bash
git add azure-pipelines.yml
git commit -m "Add a deployment stage"
git push origin release-pipeline
```

3. In Azure Pipelines, navigate to your pipeline to view the logs.

4. After the build finishes, select the back button to return to the summary page and check the status of your stages. Both stages finished successfully in our case.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/5-pipeline-deployment-summary.png)

## View the deployed website on App Service

1. If you still have your App Service tab open, refresh the page. Otherwise, navigate to your Azure App Service in the Azure portal and select the instance's URL: for example, `https://tailspin-space-game-web-1234.azurewebsites.net`

![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/5-app-service-details.png)

The Space Game website is successfully deployed to Azure App Service.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/5-deployed-website.png)

Congratulations! You successfully deployed the Space Game website to Azure App Service by using Azure Pipelines.


