
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


# 1.6 Exercise - Monitor the health of your pipeline


In this exercise, you examine the analytics features that Azure Pipelines provide.

Irwin asked the Tailspin team on how they can release faster. Building an automated release pipeline is a great step toward releasing quickly and reliably. As you release more often and more rapidly, it's important to understand the health and history of your releases. Looking at health trends regularly can help you diagnose potential problems before they become critical.

Before we take a look at some of your pipeline's analytics, let's listen in on the Tailspin team at their morning meeting.

## How can I track the health of my pipeline?

It's the following morning. At the team meeting, Andy and Mara have finished demonstrating the build and release pipeline that they set up.

**Amita:** This is fantastic! The build pipeline was a great start, but I still had to manually install the build artifact in my lab so I could test it. If I can get these releases to my test environment on a regular schedule, I can move new features through QA much faster.

**Mara:** Exactly! And remember, we can always expand our release pipeline to include more stages. The goal is to create a complete deployment workflow.

**Tim:** A staging environment would be great. I could do more stress testing before we present new features to management for final approval.

The team is excited to see what the new pipeline can do. They all start talking at the same time.

**Andy:** I'm excited too. But let's focus on one step at a time. Yes, I think we can make all of these changes and more, but this is just a proof of concept. We'll work on expanding it over time.

**Amita:** So how do we track the health of our release pipelines?

**Andy:** Remember the dashboard we created to monitor the build health? We can set up the same kind of system for our releases.

**Tim:** Irwin will like that.

**Andy:** Let's hold off on building a release dashboard until we have a complete release workflow. For now, let's look at some of the built-in analytics that Azure Pipelines provides.

The team gathers around Andy's laptop.

## What information does pipeline analytics provide?

Every pipeline provides reports that include metrics, trends, and insights. These reports can help you improve the efficiency of your pipeline.

Reports include:

- The overall pass rate of your pipeline.
- The pass rate of any tests in your pipeline.
- The average duration of your pipeline runs; including the build tasks, which take the most time to complete.

Here's a sample report that shows the pipeline failures, test failures, and pipeline duration.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/6-analyticstab.png)

You can filter the results to focus on a specific time period or on the overall activity of a GitHub branch. Azure DevOps also provides this information as an OData feed. Use this feed to publish reports and notifications to systems such as Power BI, Microsoft Teams, or Slack. You can learn more about analytics feeds at the end of this module.

## Explore your pipeline's analytics

1. In Azure DevOps, select **Pipelines**, then select your pipeline.

2. Select the **Analytics** tab.


![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/6-pipeline-analytics-overview.png)

3. Review the pass rates and average duration of your pipeline runs.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/6-pipeline-analytics-overview.png)

4. Under **Pipeline pass rate**, select **View full report** to view the detailed report.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/6-pipeline-failure-report.png)

**Amita:** That's the information I want, but I don't see much data yet.

**Andy:** That's right. We'll collect more data as we perform more runs over time. We'll use this data to gain insights and learn how we can make it more efficient.

**Mara:** I see that the npm install task takes the longest to complete. Perhaps we can make it run faster by caching the npm packages.

**Andy:** That's a great idea! We can investigate this further as we have more pipeline runs.



# 1.7 Exercise - Clean up your environment

Congratulations! You're all done with creating pipelines and resources. In this unit, you're going to clean up your Azure resources and Azure DevOps environment.

## Clean up Azure resources

1. Navigate to [Azure portal](https://portal.azure.com).

2. Select **Resource groups** from the left panel.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-pipelines-settings-button.png)

4. Select your resource group (**tailspin-space-game-rg**).

5. Select **Delete resource group**.

6. Type your resource group name in the text box, and then select **Delete**.

7. Select **Delete** again to confirm deletion.

## Disable pipeline or delete project

Each module in this learning path provides a template you can run to create a clean environment. When you run multiple templates, you will create multiple projects each pointing to the same GitHub repository. This setup can trigger multiple pipelines to run every time you push a change to your GitHub repository consuming free build minutes on our hosted agents. That's why it's important to disable or delete your pipeline before you move on to the next module in this learning path.

### Option 1: Disable your pipeline

Choose this option if you want to keep your project and your build pipeline for future reference. You can re-enable your pipeline later if you need to.

1. In your Azure DevOps project, select **Pipelines** and then select your pipeline.

2. Select the ellipsis button at the far right, and then select **Settings**.

3. Select **Disabled**, and then select **Save**. Your pipeline will no longer process new run requests.

### Option 2: Delete your project

Choose this option if you don't need your DevOps project for future reference. This will delete your Azure DevOps project.

1. Navigate to your Azure DevOps project.

2. Select **Project settings** in the lower-left corner.

3. Under **Overview**, scroll down to the bottom of the page and then select **Delete**.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-delete-project.png)

4. Type your project name in the text box, and then select **Delete**.



# 1.9 Summary

Great work! You've successfully deployed the *Space Game* website to Azure App Service by using Azure Pipelines. Continuous delivery helps you release reliable software updates to your customers as rapidly as the business demands. Your customers can have the latest features and fixes as soon as you're ready to release them. By using the analytics provided by Azure Pipelines, your team can pinpoint hot spots and areas for improvement.

Setting up Azure Pipelines to publish the *Space Game* website to App Service is a great first step for the team, but this accomplishment is just the beginning. In the modules that follow, you'll help the team expand their release pipeline to include additional stages and tests. Each improvement will give the team more confidence in the quality of their releases.

## Learn more

Here are some additional resources to learn more about Azure resources, App Service, and many other topics.

### Choose the right compute option for your app

In this module, you deployed a website to App Service. You can use Azure Pipelines to deploy to just about any kind of environment, including a virtual machine or containerized environment.

The [Describe Azure compute services](https://docs.microsoft.com/learn/modules/azure-compute-fundamentals/) module goes into further detail about the kinds of compute options Azure provides.

The [Deploy a website to Azure with Azure App Service](https://docs.microsoft.com/learn/paths/deploy-a-website-with-azure-app-service/) learning path is also a great resource to learn more about Azure App Service.

### Deploy to your preferred environment

After you choose where to deploy your applications, learn how to use Azure Pipelines to deploy to that specific environment:

* [Deploy to App Service using Azure Pipelines](https://docs.microsoft.com/azure/devops/pipelines/targets/webapp)
* [Deploy apps to a Linux virtual machine](https://docs.microsoft.com/azure/devops/pipelines/apps/cd/deploy-linuxvm-deploygroups)
* [Deploy apps to a Windows virtual machine](https://docs.microsoft.com/azure/devops/pipelines/apps/cd/deploy-webdeploy-iis-deploygroups)
* [Build and deploy to Azure Kubernetes Service with Azure Pipelines](https://docs.microsoft.com/azure/aks/devops-pipeline)

### Integrate with other CI/CD tools

Learn how you can use Azure Pipelines with Jenkins and ServiceNow.

* [Continuously deploy from a Jenkins build](https://docs.microsoft.com/azure/devops/pipelines/release/integrate-jenkins)
* [Integrate with ServiceNow change management](https://docs.microsoft.com/azure/devops/pipelines/release/approvals/servicenow)

### Go deeper

Learn more about some of the topics mentioned in this module.

* [When should you right-click publish?](https://docs.microsoft.com/aspnet/core/host-and-deploy/visual-studio-publish-profiles)
* [Specify jobs in your pipeline](https://docs.microsoft.com/azure/devops/pipelines/process/phases)
* [Deployment jobs](https://docs.microsoft.com/azure/devops/pipelines/process/deployment-jobs)
* [Create and target an environment](https://docs.microsoft.com/azure/devops/pipelines/process/environments)
* [Manage service connections](https://docs.microsoft.com/azure/devops/pipelines/library/service-endpoints)
* [Pipeline reports](https://docs.microsoft.com/azure/devops/pipelines/reports/pipelinereport)



# 2 Create a multistage pipeline by using Azure Pipelines

Design and create a realistic release pipeline that promotes changes to various testing and staging environments.

#### Learning objectives
After completing this module, you'll be able to:
- Identify the stages, or major divisions of the pipeline, that you need to implement a multistage pipeline.
- Explain when to use conditions, triggers, and approvals to promote changes from one stage to the next.
- Promote a build through these stages: Dev, Test, and Staging.
#### Prerequisites
- An Azure subscription
- An Azure DevOps organization with access to parallel jobs
- Visual Studio Code
- .NET 8.0 SDK
- Git
- A GitHub account



# 2.1 Introduction

In **Create a release pipeline in Azure Pipelines**, you built a basic release pipeline. That pipeline has a *Build* stage that builds the artifact, and a *Deploy* stage that installs the web app on Azure App Service. Mara and Andy built this pipeline as a proof of concept that they showed to the rest of the team.

An actual release pipeline has more stages. Each stage has its own set of tasks that can potentially take an artifact all the way to production.

In this module, you join the Tailspin Toys web team as they design a realistic release pipeline that contains multiple stages. You also learn different ways to control how an artifact is promoted from one stage to the next.

A good release-management workflow lets you release more frequently and more consistently. In practice, you want to define a process that maps to your team's needs. Here, you create a basic workflow. That means first designing the environments. The environments define the runtimes of each stage in the pipeline. Then, you deploy the *Space Game* web app to these stages: *Dev*, *Test*, and *Staging*. Each stage deploys the app to its own App Service instance.

## Learning objectives

After completing this module, you should able to:

* Identify the *stages*, or major divisions of the pipeline, that you need to implement in a multistage pipeline.
* Explain when to use conditions, triggers, and approvals to promote changes from one stage to the next.
* Promote a build through these stages: *Dev*, *Test*, and *Staging*.

## Prerequisites

The modules in this learning path form a progression. To follow the progression from the beginning, be sure to first complete these learning paths:

* Get started with Azure DevOps
* Build applications with Azure DevOps

We also recommend you start at the beginning of this learning path: **Deploy applications with Azure DevOps**.

If you want to go through just this module, you need to set up a development environment on your Windows, macOS, or Linux system. You need:

* An Azure DevOps organization with access to parallel jobs. If your organization does not have access to parallel jobs, you can request parallel jobs for free for public or private projects using [this form](https://aka.ms/azpipelines-parallelism-request). Your request takes 2-3 business days.
* An Azure subscription
* A GitHub account
* Visual Studio Code with the Azure Pipelines for VS Code extension.
* .NET 8.0 SDK
* Git

You can get started with Azure and Azure DevOps for free. You don't need an Azure subscription to work with Azure DevOps. But in this module, you use Azure DevOps to deploy to Azure resources that exist in your Azure subscription.

Use this environment to complete the exercises in this and future modules. You can also use it to apply your new skills to your own projects.

> **Note**
> 
> Azure Pipelines support a vast array of **languages and application types**. In this module, you'll be working with a .NET application but you can apply the patterns you learn here to your own projects that use your favorite programming languages and frameworks.

## Meet the team

You met the *Space Game* web team at Tailspin Toys in previous modules. As a refresher, here's who you work with in this module.

![Andy](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/andy.png) **Andy** is the development lead.

![Amita](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/amita.png) **Amita** is in QA.

![Tim](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/tim.png) **Tim** is in operations.

![Mara](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/mara.png) **Mara** just joined as a developer and reports to Andy.

Mara has prior experience with DevOps. She's helping the team adopt a more automated process that uses Azure DevOps.



# 2.2 Design the pipeline

In this unit, you follow the Tailspin web team as they define their release pipeline for the Space Game website.

When you plan a release pipeline, you usually begin by identifying the stages, or major divisions, of that pipeline. Each stage typically maps to an environment. For example, in the previous module, Andy and Mara's basic pipeline had a Deploy stage that mapped to an Azure App Service instance.

In this module, you promote changes from one stage to the next. Within each stage, you deploy the Space Game website to the environment associated with that stage.

After you define which stages you need, consider how changes are promoted from one stage to the next. Each stage can define the success criteria that must be met before the build can move to the next stage. Azure Pipelines provides several ways to help you control how and when changes move through the pipeline. As a whole, these approaches are used for release management.

In this section, you:

- Learn the differences between common pipeline stages, such as Build, Dev, Test, and Staging.
- Understand how to use manual, scheduled, and continuous deployment triggers to control when an artifact moves to the next stage in the pipeline.
- See how a release approval pauses the pipeline until an approver accepts or rejects the release.

## The meeting

The entire Tailspin web team is gathered together. In **Create a release pipeline in Azure Pipelines**, the team planned their tasks for the current sprint. Each task relates to building their release pipeline for the Space Game website.

Recall that the team decided on these five tasks for their sprint:

1. Create a multistage pipeline
2. Connect the web app to a database
3. Automate quality tests
4. Automate performance tests
5. Improve release cadence

The team meets to talk about the first task, **Create a multistage pipeline**. After the team defines the pipeline, it can move from its basic proof of concept to a release pipeline that includes more stages, quality checks, and approvals.

Amita and Tim are watching Andy and Mara demonstrate the release pipeline a second time. They see that the artifact is built and installed on App Service.

## What pipeline stages do you need?

When you want to implement a release pipeline, it's important to first identify which stages you need. The stages you choose depend on your requirements. Let's follow along with the team as they decide on their stages.

**Tim:** OK, I understand the idea of an automated pipeline. I like how it's easy to deploy to Azure. But where do we go from this demo? We need something we can actually use for our releases.

**Amita:** Right! We need to add other stages. For example, presently, we have no place for a testing stage.

**Tim:** Plus, we need a stage where we can show new features to the management. I can't send anything to production without management approval.

**Andy:** Absolutely! Now that it's up to speed on what a release pipeline does, how do we make this pipeline do what we need?

**Mara:** Let's sketch out our requirements to help us plan our next steps. Let's start with what we have.

Mara moves to the whiteboard and sketches the existing pipeline.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/2-build-deploy.png)

**Mara:** The Build stage builds the source code and produces a package. In our case, that package is a .zip file. The Deploy stage installs the .zip file, which is the Space Game website, on an App Service instance. What's missing from our release pipeline?

### Add the Dev stage

**Andy:** I might be biased, but I think we need a Dev stage. This stage should be the first stop for the artifact after it's built. Developers can't always run the entire service from their local development environment. For example, an e-commerce system might require a website, product database, and payment system. We need a stage that includes everything the app needs.

In our case, the Space Game website's leaderboard feature reads high scores from an external source. Right now, it reads fictitious scores from a file. Setting up a Dev stage would give us an environment where we can integrate the web app with a real database. That database might still hold fictitious scores, but it brings us one step closer to our final app.

**Mara:** I like it. We won't integrate with a real database yet. But in a Dev stage, we can deploy to an environment where we can add a database.

Mara updates her drawing on the whiteboard. She replaces "Deploy" with "Dev" to show the Dev stage.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/2-add-dev-stage.png)

**Andy:** You bring up an interesting point. We build the app each time we push a change to GitHub. Does that mean each build is promoted to the Dev stage after it finishes?

**Mara:** Building continuously gives us important feedback about our build and test health. But we want to promote to the Dev stage only when we merge code into some central branch: either main or some other release branch. I'll update the drawing to show that requirement.

![Diagram that shows whiteboard illustrating build and dev stages. A condition promotes to the Dev stage only when changes happen on a release branch.](whiteboard-condition.png)

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/2-add-dev-stage-trigger.png)

**Mara:** I think this promotion will be easy to accomplish. We can define a condition that promotes to the Dev stage only when changes happen on a release branch.

## What are conditions?

In Azure Pipelines, use a condition to run task or job based on the state of the pipeline. You worked with conditions in previous modules.

Remember, some of the conditions that you can specify are:

- Only when all previous dependent tasks have succeeded
- Even if a previous dependency has failed, unless the run was canceled
- Even if a previous dependency has failed, even if the run was canceled
- Only when a previous dependency has failed
- Some custom condition

Here's a basic example:

```yaml
steps:
  - script: echo Hello!
    condition: always()
```

The `always()` condition causes this task to print "Hello!" unconditionally, even if previous tasks failed.

This condition is used if you don't specify a condition:

```yaml
condition: succeeded()
```

The `succeeded()` built-in function checks whether the previous task succeeded. If the previous task fails, this task and later tasks that use the same condition are skipped.

Here you want to build a condition that specifies:

- The previous task succeeded.
- The name of the current Git branch is release.

To build this condition, you use the built-in `and()` function. This function checks whether each of its conditions is true. If any condition isn't true, the overall condition fails.

To get the name of the current branch, you use the built-in `Build.SourceBranchName` variable. You can access variables within a condition in a few ways. Here you use the `variables[]` syntax.

To test a variable's value, you can use the built-in `eq()` function. This function checks whether its arguments are equal.

With that in mind, you apply this condition to run the Dev stage only when the current branch name is "release":

```yaml
condition: |
  and
  (
    succeeded(),
    eq(variables['Build.SourceBranchName'], 'release')
  )
```

The first condition in the `and()` function checks whether the previous task succeeded. The second condition checks whether the current branch name equals release.

In YAML, you use the pipe (`|`) syntax to define a string that spans multiple lines. You could define the condition on a single line, but we write it this way to make it more readable.

> **Note**
> 
> In this module, we use the release branch as an example. You can combine conditions to define the behavior that you need. For example, you could build a condition that runs the stage only when the build is triggered by a pull request against the main branch.

In the next unit, when you set up the Dev stage, you work with a more complete example.

For a more complete description of conditions in Azure Pipelines, see [expressions documentation](https://docs.microsoft.com/azure/devops/pipelines/process/expressions).

**Mara:** By using conditions, you can control which changes are promoted to which stages. We can produce a build artifact for any change to validate our build and confirm that it's healthy. When we're ready, we can merge those changes into a release branch and promote that build to the Dev stage.

### Add the Test stage

**Mara:** So far, we have the Build and Dev stages. What comes next?

**Amita:** Can we add the Test stage next? That seems like the right place for me to test out the latest changes.

Mara adds the Test stage to her drawing on the whiteboard.

![Diagram that shows the whiteboard illustrating build, dev and test stages. The Test stage deploys the build to Azure App Service.](whiteboard-with-test.png)

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/2-add-test-stage.png)

**Amita:** One concern I have is how often I need to test the app. An email notifies me whenever Mara or Andy makes a change. Changes happen throughout the day, and I never know when to jump in. I think I'd like to see a build once a day, maybe when I get in to the office. Can we do that?

**Andy:** Sure. Why don't we deploy to Test during nonworking hours? Let's say we send you a build every day at 3 A.M.

**Mara:** That sounds good. We can always manually trigger the process as well if we need to. For example, we can trigger it if we need you to verify an important bug fix right away.

Mara updates her drawing to show that the build moves from the Dev stage to the Test stage at 3 A.M. each day.

![Diagram that shows the whiteboard showing Build, Dev, and Test stages. The schedule promotes the change from Dev to Test at 3 A.M. each morning.](whiteboard-with-schedule.png)

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/2-add-test-stage-schedule.png)

## What are triggers?

**Amita:** I'm feeling better now that we know how one stage moves to another. But how do we control when a stage runs?

**Mara:** In Azure Pipelines, we can use triggers. A trigger defines when a stage runs. Azure Pipelines provides a few types of triggers. Here are our choices:

- Continuous integration (CI) trigger
- Pull request (PR) trigger
- Scheduled trigger
- Build completion trigger

CI and PR triggers let you control which branches participate in the overall process. For example, you want to build the project when a change is made in any branch. A scheduled trigger starts a deployment at a specific time. A build completion trigger runs a build when another build, such as one for a dependent component, completes successfully. It seems like we want a scheduled trigger.

## What are scheduled triggers?

A scheduled trigger uses cron syntax to cause a build to run on a defined schedule.

On Unix and Linux systems, cron is a popular way to schedule jobs to run on a set time interval or at a specific time. In Azure Pipelines, scheduled triggers use the cron syntax to define when a stage runs.

A cron expression includes fields that match certain time parameters. Here are the fields:

```
mm HH DD MM DW
 \  \  \  \  \__ Days of week
  \  \  \  \____ Months
   \  \  \______ Days
    \  \________ Hours
     \__________ Minutes
```

For example, this cron expression describes "3 A.M. every day": `0 3 * * *`

A cron expression can include special characters to specify a list of values or a range of values. In this example, the asterisk (*) matches all values for the Days, Months, and Days of week fields.

Put another way, this cron expression reads as:

- At minute 0,
- At the third hour,
- On any day of the month,
- On any month,
- On any day of the week,
- Run the job

To specify 3 A.M. only on days Monday through Friday, you would use this expression: `0 3 * * 1-5`

> **Note**
> 
> The time zone for cron schedules is Coordinated Universal Time (UTC), so in this example, 3 A.M. refers to 3 A.M. in UTC. In practice, you might want to adjust the time in your cron schedule relative to UTC so that the pipeline runs at the expected time for you and your team.

To set up a scheduled trigger in Azure Pipelines, you need a `schedules` section in your YAML file. Here's an example:

```yaml
schedules:
- cron: '0 3 * * *'
  displayName: 'Deploy every day at 3 A.M.'
  branches:
    include:
    - release
  always: false
```

In this `schedules` section:

- `cron` specifies the cron expression.
- `branches` specifies to deploy only from the release branch.
- `always` specifies whether to run the deployment unconditionally (`true`), or only when the release branch has changed since the last run (`false`). Here, you specify `false` because you need to deploy only when the release branch has changed since the last run.

The entire pipeline runs when Azure Pipelines executes a scheduled trigger. The pipeline also runs under other conditions, such as when you push a change to GitHub. To run a stage only in response to a scheduled trigger, you can use a condition that checks whether the reason for the build is a scheduled run.

Here's an example:

```yaml
- stage: 'Test'
  displayName: 'Deploy to the Test environment'
  condition: and(succeeded(), eq(variables['Build.Reason'], 'Schedule'))
```

This stage, `Test`, runs only when the previous stage succeeds and the built-in `Build.Reason` pipeline variable equals `Schedule`.

You see a more complete example later in this module.

**Amita:** I like this. I don't even have to pick up the release manually and install it. It's ready for me.

**Andy:** And remember, if we want to automate more later, we can. Nothing's written in stone. The pipeline evolves as we improve and learn.

### Add the Staging stage

**Tim:** It's my turn. I need a stage to run more stress tests. We also need a stage where we can demo to management to get their approval. For now, we can combine those two needs into a stage that we can call Staging.

**Andy:** Well said, Tim. Having a staging, or preproduction environment is important. This staging environment is often the last stop before a feature or bug fix reaches our users.

Mara adds Staging to her drawing on the whiteboard.

![Diagram where the whiteboard is showing the Build, Dev, Test, and Staging stages. The Staging stage deploys the build to Azure App Service.](whiteboard-with-staging.png)

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/2-add-staging-stage.png)


**Amita:** We use a scheduled trigger to promote changes from the Dev stage to the Test stage. But how do we promote changes from Test to Staging? Does that promotion also have to happen on a schedule?

**Mara:** I think the best way to handle that would be a release approval. A release approval lets you manually promote a change from one stage to the next.

**Amita:** That sounds like exactly what I need! A release approval would give me the time to test out the latest changes before we present the build to management. I can promote the build when I'm ready.

Mara updates her drawing to show that the build moves from Test to Staging only when Amita approves it.

![Diagram where the whiteboard shows the Build, Dev, Test, and Staging stages. Changes move from Test to Staging only after approval.](whiteboard-with-approval.png)

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/2-add-staging-stage-approval.png)

**Tim:** I could also imagine us using release approvals to promote from Staging to Production after management signs off. I can never predict how long that takes. After they sign off, I can approve the release and promote it to production manually. But how do release approvals work?

## What are release approvals?

A release approval is a way to pause the pipeline until an approver accepts or rejects the release. To define your release workflow, you can combine approvals, conditions, and triggers.

Recall that in **Create a release pipeline in Azure Pipelines**, you defined an environment in your pipeline configuration to represent your deployment environment. Here's an example from your existing pipeline:

```yaml
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
```

Your environment can include specific criteria for your release. The criteria can specify which pipelines can deploy to that environment and what human approvals are needed to promote the release from one stage to the next.

Later in this module, you define the staging environment, and assign yourself as an approver to promote the Space Game web app from the Test stage to Staging.

## Automate as little or as much as you need

Azure Pipelines gives you the flexibility to automate some stages while manually controlling stages that aren't ready for automation.

**Tim:** I like how we can define the criteria that promote changes from one stage to the next. But we defined some manual criteria in our pipeline. I thought DevOps was about automating everything.

**Mara:** You raise a good point. DevOps is really about automating repetitive and error-prone tasks. Sometimes human intervention is necessary. For example, we get approval from management before we release new features. As we get more experience with our automated deployments, we can automate more of our manual steps to speed up the process. For example, we can automate more quality checks in the Test stage, so Amita doesn't have to approve each build.

**Tim:** Sounds great. Let's go with this plan for now, and see how we can speed up the system later.

**Amita:** Speaking of our plan, can we summarize our next steps?

## The plan

Let's review the Tailspin team's plan as they move toward next steps.

**Mara:** Here's the release pipeline we want to build.

Mara points to the whiteboard.

![Diagram of the final whiteboard showing the Build, Dev, Test, and Staging stages.](whiteboard-final.png)

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/2-add-staging-stage-approval.png)

**Mara:** To summarize, our steps are to:

1. Produce a build artifact each time we push a change to GitHub. This step happens in the Build stage.
2. Promote the build artifact to the Dev stage. This step happens automatically when the build stage succeeds and the change is on the release branch.
3. Promote the build artifact to the Test stage each morning at 3 A.M. We use a scheduled trigger to promote the build artifact automatically.
4. Promote the build artifact to Staging after Amita tests and approves the build. We use a release approval to promote the build artifact.
5. After management approves the build, we can deploy the build artifact to a production environment.

**Amita:** Is this going to be hard to do? It seems like a lot of work.

**Mara:** I don't think it's too bad. Every stage is separate from every other stage. Stages are discrete. Each stage has its own set of tasks. For example, what happens in the Test stage stays in the Test stage.

Every deployment stage in our pipeline also has its own environment. For example, when we deploy the app to Dev or Test, the environment is an App Service instance.

Finally, we test only one release at a time. We never change releases in the middle of the pipeline. We use the same release in the Dev stage as in the Staging stage, and every release has its own version number. If the release breaks in one of the stages, we fix it and build it again with a new version number. That new release then goes through the pipeline from the very beginning.

## A few words about quality

You just saw the team design a pipeline that takes their app all the way from build to staging. The whole point of this pipeline isn't just to make their lives easier. It's to ensure the quality of the software they're delivering to their customers.

How do you measure the quality of your release process? You can't measure it directly. What you can measure is how well your process works. If you're constantly changing the process, it might be an indication that there's something wrong. Releases that fail consistently at a particular point in the pipeline might also indicate that there's a problem with the release process.

Do the releases always fail on a particular day or time? Do they always fail after you deploy to a particular environment? Look for these and other patterns to see if some aspects of the release process are dependent or related.

A good way to keep track of your release process quality is to create visualizations of the quality of the releases. For example, add a dashboard widget that shows you the status of every release.

When you want to measure the quality of a release itself, you can perform all kinds of checks within the pipeline. For example, you can execute different types of tests, such as load tests and UI tests while running your pipeline.

Using a quality gate is also a great way to check the quality of your release. There are many different quality gates. For example, work item gates can verify the quality of your requirements process.

You can also add more security and compliance checks. For example, do you comply with the four-eyes principle or do you have the proper traceability?

As you progress through this learning path, you see many of these techniques put into practice.

Lastly, when you design a quality release process, think about what kind of documentation or release notes that you need to provide to the user. Keeping your documentation current can be difficult. You might want to consider using a tool, such as the Azure DevOps Release Notes Generator, which is a function app that contains an HTTP-triggered function. By using Azure Blob Storage, it creates a Markdown file whenever a new release is created in Azure DevOps.

---

## Check your knowledge

### 1. Your pipeline includes many tests and quality checks that take several minutes to finish. Which kind of trigger is best for running tests only on code that was peer reviewed?

- [ ] A build completion trigger
- [ ] A CI trigger or PR trigger
- [ ] A scheduled trigger

### 2. What's the best way to pause the pipeline until an approver signs off on a change?

- [ ] Use a release approval.
- [ ] Install a Marketplace extension that provides Azure Pipelines tasks that can pause the pipeline.
- [ ] Ask your approver to look at the change. Then manually trigger the pipeline to run.

### 3. You want to deploy your web app to the Test environment each time a build finishes. What's the easiest way to set up the process?

- [ ] Use a scheduled trigger.
- [ ] Watch for build notification emails and manually trigger your build when the other one finishes successfully.
- [ ] Use a build completion trigger.

---

## Відповіді на запитання:

**1. Your pipeline includes many tests and quality checks that take several minutes to finish. Which kind of trigger is best for running tests only on code that was peer reviewed?**
✅ **A CI trigger or PR trigger**

PR trigger найкраще підходить для запуску тестів тільки на код, який пройшов peer review, оскільки він активується при створенні або оновленні pull request.

**2. What's the best way to pause the pipeline until an approver signs off on a change?**
✅ **Use a release approval.**

Release approval є найкращим способом призупинити pipeline до отримання схвалення від відповідальної особи.

**3. You want to deploy your web app to the Test environment each time a build finishes. What's the easiest way to set up the process?**
✅ **Use a build completion trigger.**

Build completion trigger найлегше налаштувати для автоматичного розгортання у Test середовище після завершення кожної збірки.




# 2.3 Exercise - Set up your Azure DevOps environment


In this section, you make sure that your Azure DevOps organization is set up to complete the rest of this module. You also create the Azure App Service environments that you deploy to later.

To accomplish these goals, you:

- Add a user to ensure Azure DevOps can connect to your Azure subscription.
- Set up an Azure DevOps project for this module.
- On Azure Boards, move the work item for this module to the Doing column.
- Make sure your project is set up locally so that you can push changes to the pipeline.
- Create the Azure App Service environments by using the Azure CLI in Azure Cloud Shell.
- Create pipeline variables that define the names of your App Service environments.
- Create a service connection that enables Azure Pipelines to securely access your Azure subscription.

## Add a user to Azure DevOps

To complete this module, you need your own Azure subscription. You can get started with Azure for free.

You don't need an Azure subscription to use Azure DevOps, but here you use Azure DevOps to deploy to Azure resources that exist in your Azure subscription. To simplify the process, use the same Microsoft account to sign in to both your Azure subscription and your Azure DevOps organization.

If you use different Microsoft accounts to sign in to Azure and Azure DevOps, add a user to your DevOps organization under the Microsoft account that you use to sign in to Azure. For more information, see [Add users to your organization or project](https://docs.microsoft.com/azure/devops/organizations/accounts/add-organization-users). When you add the user, select the **Basic** access level.

Next, sign out of Azure DevOps and sign in. Use the Microsoft account that you use to sign in to your Azure subscription.

## Get the Azure DevOps project

Here, you make sure that your Azure DevOps organization is set up to complete the rest of this module. To do so, you run a template that creates a project in Azure DevOps.

The modules in this learning path form a progression. You follow the Tailspin web team through their DevOps journey. For learning purposes, each module has its own Azure DevOps project.

### Run the template

Run a template that sets up your Azure DevOps organization.

1. Get and run the ADOGenerator project in Visual Studio or the IDE of your choice.

2. When prompted to **Enter the template number from the list of templates**, enter **30** for **Create a multi-stage pipeline with Azure Pipelines**, then press **Enter**.

3. Choose your authentication method. You can set up and use a Personal Access Token (PAT) or use device login.

   > **Note**
   > 
   > If you set up a PAT, make sure to authorize the necessary scopes. For this module, you can use **Full access**, but in a real-world situation, you should ensure you grant only the necessary scopes.

4. Enter your Azure DevOps organization name, then press **Enter**.

5. If prompted, enter your Azure DevOps PAT, then press **Enter**.

6. Enter a project name such as **Space Game - web - Multistage**, then press **Enter**.

7. Once your project is created, go to your Azure DevOps organization in your browser (at `https://dev.azure.com/<your-organization-name>/`) and select the project.

### Fork the repository

If you haven't already, create a fork of the `mslearn-tailspin-spacegame-web-deploy` repository.

1. On GitHub, go to the [mslearn-tailspin-spacegame-web-deploy](https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web-deploy) repository.

2. Select **Fork** at the top-right of the screen.

3. Choose your GitHub account as the **Owner**, then select **Create fork**.

> **Important**
> 
> In this module, the **Clean up your Azure DevOps environment** page contains important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes. Even if you don't complete this module, be sure to follow the cleanup steps.

### Set your project's visibility

Initially, your fork of the Space Game repository on GitHub is set to public while the project created by the Azure DevOps template is set to private. A public repository on GitHub can be accessed by anyone, while a private repository is only accessible to you and the people you choose to share it with. Similarly, on Azure DevOps, public projects provide read-only access to non-authenticated users, while private projects require users to be granted access and authenticated to access the services.

At the moment, it is not necessary to modify any of these settings for the purposes of this module. However, for your personal projects, you must determine the visibility and access you wish to grant to others. For instance, if your project is open source, you may choose to make both your GitHub repository and your Azure DevOps project public. If your project is proprietary, you would typically make both your GitHub repository and your Azure DevOps project private.

Later on, you may find the following resources helpful in determining which option is best for your project:

- [Use private and public projects](https://docs.microsoft.com/azure/devops/organizations/projects/about-projects)
- [Change project visibility to public or private](https://docs.microsoft.com/azure/devops/organizations/projects/make-project-public)
- [Setting repository visibility](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)

## Move the work item to Doing

Here, you assign a work item to yourself on Azure Boards. You also move the work item to the Doing state. In practice, you and your team would create work items at the start of each sprint or work iteration.

This work assignment gives you a checklist from which to work. It gives other team members visibility into what you're working on and how much work is left. The work item also helps enforce work-in-progress (WIP) limits so that the team doesn't take on too much work at one time.

Recall that the team settled on the following top issues for the current sprint.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/deploy-all-tasks.png)

> **Note**
> 
> Within an Azure DevOps organization, work items are numbered sequentially. In your project, the number for each work item might not match what you see here.

Here you move the first item, **Create a multistage pipeline**, to the Doing column. Then you assign yourself to the work item. **Create a multistage pipeline** relates to defining each stage of deploying the Space Game website.

To set up the work item:

1. From Azure DevOps, go to **Boards**. Then, from the menu, select **Boards**.


![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-boards-menu.png)

2. In the **Create a multistage pipeline** card, select the down arrow. Then, assign the work item to yourself.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-boards-down-chevron.png)

3. Move the work item from the **To Do** column to the **Doing** column.


![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/3-azure-boards-wi1-doing.png)

At the end of this module, you'll move the card to the **Done** column, after you complete the task.

## Set up the project locally

Here you load the Space Game project in Visual Studio Code, configure Git, clone your repository locally, and set the upstream remote so that you can download starter code.

> **Note**
> 
> If you're already set up with the `mslearn-tailspin-spacegame-web-deploy` project locally, you can move to the next section.

### Open the integrated terminal

Visual Studio Code comes with an integrated terminal. Here you both edit files and work from the command line.

1. Start Visual Studio Code.

2. On the **View** menu, select **Terminal**.

3. In the dropdown list, select **Git Bash**. If you're familiar with another Unix shell that you prefer to use, select that shell instead.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/vscode-terminal-git-bash.png)

In the terminal window, you can choose any shell that's installed on your system. For example, you can choose Git Bash, or PowerShell, or another shell.

Here you'll use Git Bash, part of Git for Windows, which makes it easy to run Git commands.

> **Note**
> 
> On Windows, if you don't see Git Bash listed as an option, make sure you've installed Git, and then restart Visual Studio Code.

4. Run the `cd` command to go to the directory where you want to work. Choose your home directory (`~`) or a different directory if you want.

```bash
cd ~
```

### Configure Git

If you're new to Git and GitHub, first run a few commands to associate your identity with Git and authenticate with GitHub. For more information, see [Set up Git](https://docs.github.com/get-started/quickstart/set-up-git).

At a minimum, you need to complete the following steps. Run the commands from the integrated terminal.

1. Set your username.
2. Set your commit email address.
3. Cache your GitHub password.

> **Note**
> 
> If you already use two-factor authentication with GitHub, create a personal access token. When you're prompted, use your token in place of your password.
> 
> Treat your access token like a password. Keep it in a safe place.

### Set up your project in Visual Studio Code

In the **Build applications with Azure DevOps** learning path, you forked and then cloned a Git repository. The repository contains the source code for the Space Game website. Your fork was connected to your projects in Azure DevOps so that the build runs when you push changes to GitHub.

> **Important**
> 
> In this learning path, we switch to a different Git repository, `mslearn-tailspin-spacegame-web-deploy`. When you ran the template to set up your Azure DevOps project, the process forked the repository automatically for you.

In this part, you clone your fork locally so that you can change and build out your pipeline configuration.

#### Clone your fork locally

You now have a copy of the Space Game web project in your GitHub account. Now you'll download, or clone, a copy to your computer so you can work with it.

A clone, just like a fork, is a copy of a repository. When you clone a repository, you can make changes, verify that they work as you expect, and then upload those changes to GitHub. You can also synchronize your local copy with changes that other authenticated users have made to the GitHub copy of your repository.

To clone the Space Game web project to your computer:

1. Go to your fork of the Space Game web project (`mslearn-tailspin-spacegame-web-deploy`) on GitHub.

2. Select **Code**. Then, from the **HTTPS** tab, select the button next to the URL that's shown to copy the URL to your clipboard.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/github-clone-button.png)

3. In Visual Studio Code, go to the terminal window.

4. In the terminal, move to the directory where you want to work. Choose your home directory (`~`) or a different directory if you want.

```bash
cd ~
```

5. Run the `git clone` command. Replace the URL that's shown here with the contents of your clipboard:

```bash
git clone https://github.com/your-name/mslearn-tailspin-spacegame-web-deploy.git
```

6. Move to the `mslearn-tailspin-spacegame-web-deploy` directory. This is the root directory of your repository.

```bash
cd mslearn-tailspin-spacegame-web-deploy
```

#### Set the upstream remote

A remote is a Git repository where team members collaborate (like a repository on GitHub). Here you list your remotes and add a remote that points to Microsoft's copy of the repository so that you can get the latest sample code.

1. Run this `git remote` command to list your remotes:

```bash
git remote -v
```

You see that you have both fetch (download) and push (upload) access to your repository:

```
origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (fetch)
origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (push)
```

**Origin** specifies your repository on GitHub. When you fork code from another repository, the original remote (the one you forked from) is often named **upstream**.

2. Run this `git remote add` command to create a remote named **upstream** that points to the Microsoft repository:

```bash
git remote add upstream https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web-deploy.git
```

3. Run `git remote` again to see the changes:

```bash
git remote -v
```

You see that you still have both fetch (download) access and push (upload) access to your repository. You also now have fetch access to the Microsoft repository:

```
origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (fetch)
origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (push)
upstream        https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web-deploy.git (fetch)
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

## Create the Azure App Service environments

Here, you create the environments that define the pipeline stages. You create one App Service instance for each stage: Dev, Test, and Staging.

In **Create a release pipeline with Azure Pipelines**, you brought up App Service through the Azure portal. Although the portal is a great way to explore what's available on Azure or to do basic tasks, bringing up components such as App Service can be tedious.

In this module, you use the Azure CLI to bring up three App Service instances. You can access the Azure CLI from a terminal or through Visual Studio Code. Here, you access the Azure CLI from Azure Cloud Shell. This browser-based shell experience is hosted in the cloud. In Cloud Shell, the Azure CLI is configured for use with your Azure subscription.

> **Important**
> 
> To complete the exercises in this module, you need your own Azure subscription.

### Bring up Cloud Shell through the Azure portal

1. Go to the [Azure portal](https://portal.azure.com) and sign in.

2. From the menu, select **Cloud Shell**. When prompted, select the **Bash** experience.


![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-portal-menu-cloud-shell.png)

> **Note**
> 
> Cloud Shell requires an Azure storage resource to persist any files that you create in the Cloud Shell. When you first open the Cloud Shell, you're prompted to create a resource group, storage account, and Azure Files share. This setup is automatically used for all future Cloud Shell sessions.

### Select an Azure region

A region is one or more Azure datacenters within a geographic location. East US, West US, and North Europe are examples of regions. Every Azure resource, including an App Service instance, is assigned a region.

To make commands easier to run, start by selecting a default region. After you specify the default region, later commands use that region unless you specify a different region.

1. From the Cloud Shell, to list the regions that are available from your Azure subscription, run the following `az account list-locations` command.

```bash
az account list-locations \
  --query "[].{Name: name, DisplayName: displayName}" \
  --output table
```

2. From the **Name** column in the output, select a region that's close to you. For example, choose `eastasia` or `westus2`.

3. Run `az configure` to set your default region. Replace `<REGION>` with the name of the region you selected.

```bash
az configure --defaults location=<REGION>
```

This example sets `westus2` as the default region:

```bash
az configure --defaults location=westus2
```

### Create the App Service instances

Here, you create the App Service instances for the three stages you deploy to: Dev, Test, and Staging. Here's a brief overview of the process you follow:

1. Generate a random number that makes your web app's domain name unique.

   This step is for learning purposes. In practice, you would choose a domain name that matches the name of your app or service.

2. Create a resource group that contains all of your App Service instances.

   For learning purposes, here you create one resource group that contains all of your App Service instances. In practice, you might create a separate resource group for each App Service instance so that you can better control the life cycle of each instance.

3. Create an App Service plan.

   An App Service plan defines the CPU, memory, and storage resources for your web app. Here, you use the **B1 Basic** plan. This plan is intended for apps that have low traffic requirements. The Standard and Premium plans are for production workloads. These plans run on dedicated virtual machine instances.

4. For each of the Dev, Test, and Staging environments, create an App Service instance.

5. Get the host name for each environment.

6. Verify that each environment is running, and that the home page is accessible.

> **Note**
> 
> For learning purposes, you use the default network settings here. These settings make your site accessible from the internet. In practice, you could configure an Azure virtual network that places your website in a network that's not internet routable, and that only you and your team can access. Later, you could reconfigure your network to make the website available to your users.

To create your App Service instances, follow these steps:

1. From the Cloud Shell, generate a random number that makes your web app's domain name unique.

```bash
webappsuffix=$RANDOM
```

2. To create a resource group named `tailspin-space-game-rg`, run the following `az group create` command.

```bash
az group create --name tailspin-space-game-rg
```

3. To create the App Service plan named `tailspin-space-game-asp`, run the following `az appservice plan create` command.

```bash
az appservice plan create \
  --name tailspin-space-game-asp \
  --resource-group tailspin-space-game-rg \
  --sku B1 \
  --is-linux
```

The `--sku` argument specifies the **B1** plan. This plan runs on the Basic tier. The `--is-linux` argument specifies to use Linux workers.

> **Important**
> 
> If the B1 SKU isn't available in your Azure subscription, select a different plan, such as **S1** (Standard).

4. To create the three App Service instances, one for each environment (Dev, Test, and Staging), run the following `az webapp create` commands.

```bash
az webapp create \
  --name tailspin-space-game-web-dev-$webappsuffix \
  --resource-group tailspin-space-game-rg \
  --plan tailspin-space-game-asp \
  --runtime "DOTNETCORE|8.0"

az webapp create \
  --name tailspin-space-game-web-test-$webappsuffix \
  --resource-group tailspin-space-game-rg \
  --plan tailspin-space-game-asp \
  --runtime "DOTNETCORE|8.0"

az webapp create \
  --name tailspin-space-game-web-staging-$webappsuffix \
  --resource-group tailspin-space-game-rg \
  --plan tailspin-space-game-asp \
  --runtime "DOTNETCORE|8.0"
```

For learning purposes, you apply the same App Service plan, **B1 Basic**, to each App Service instance here. In practice, you'd assign a plan that matches your expected workload.

For example, for the environments that map to the Dev and Test stages, **B1 Basic** might be appropriate because you want only your team to access the environments.

For the Staging environment, you'd select a plan that matches your production environment. That plan would likely provide greater CPU, memory, and storage resources. Under the plan, you can run performance tests, like load tests, in an environment that resembles your production environment. You can run the tests without affecting live traffic to your site.

5. To list each App Service instance's host name and state, run the following `az webapp list` command.

```bash
az webapp list \
  --resource-group tailspin-space-game-rg \
  --query "[].{hostName: defaultHostName, state: state}" \
  --output table
```

Note the host name for each running service. You need these host names later when you verify your work. Here's an example:

```
HostName                                                 State
-------------------------------------------------------  -------
tailspin-space-game-web-dev-21017.azurewebsites.net      Running
tailspin-space-game-web-test-21017.azurewebsites.net     Running
tailspin-space-game-web-staging-21017.azurewebsites.net  Running
```

6. As an optional step, go to one or more of the host names. Verify that they're running, and that the default home page appears.

Here's what you see:

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/app-service-default.png)

> **Important**
> 
> The **Clean up your Azure DevOps environment** page in this module contains important cleanup steps. Cleaning up helps ensure that you're not charged for Azure resources after you complete this module. Be sure to perform the cleanup steps even if you don't complete this module.

## Create pipeline variables in Azure Pipelines

In **Create a release pipeline with Azure Pipelines**, you added a variable to your pipeline that stores the name of your web app in App Service. Here you do the same. But this time, you add one variable for each App Service instance that corresponds to a Dev, Test, or Staging stage in your pipeline.

You could hard-code these names in your pipeline configuration, but if you define them as variables, your configuration is more reusable. Additionally, if the names of your App Service instances change, you can update the variables and trigger your pipeline without modifying your configuration.

To add the variables:

1. In Azure DevOps, go to your **Space Game - web - Multistage** project.

2. Under **Pipelines**, select **Library**.


![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/5-pipelines-library.png)

3. Select **+ Variable group**.

4. Under **Properties**, enter **Release** for the variable group name.

5. Under **Variables**, select **+ Add**.

6. For the name of your variable, enter **WebAppNameDev**. For the value, enter the name of the App Service instance that corresponds to your Dev environment, such as `tailspin-space-game-web-dev-1234`.

7. Repeat the previous two steps twice more to create variables for your Test and Staging environments. Here are examples:

| Variable name | Example value |
|---------------|---------------|
| WebAppNameTest | tailspin-space-game-web-test-1234 |
| WebAppNameStaging | tailspin-space-game-web-staging-1234 |

Be sure to replace each example value with the App Service instance that corresponds to your environment.

> **Important**
> 
> Set the name of the App Service instance, not its host name. In this example, you would enter `tailspin-space-game-web-dev-1234` and not `tailspin-space-game-web-dev-1234.azurewebsites.net`.

8. Near the top of the page, select **Save** to save your variable in the pipeline.

Your variable group resembles this one:


![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/pipelines-environments.png)

## Create the dev and test environments

In **Create a release pipeline with Azure Pipelines**, you created an environment for the dev environment. Here, you repeat the process for both the dev and test environments. Later, you set up the staging environment, which includes more criteria.

To create the dev and test environments:

1. From Azure Pipelines, select **Environments**.

![A screenshot of Azure Pipelines showing the location of the Environments menu option.](azure-pipelines-environments.png)

2. To create the dev environment:
   - Select **Create environment**.
   - Under **Name**, enter **dev**.
   - Leave the remaining fields at their default values.
   - Select **Create**.

3. To create the test environment:
   - Return to the **Environments** page.
   - Select **New environment**.
   - Under **Name**, enter **test**.
   - Select **Create**.

## Create a service connection

Here, you create a service connection that enables Azure Pipelines to access your Azure subscription. Azure Pipelines uses this service connection to deploy the website to App Service. You created a similar service connection in the previous module.

> **Important**
> 
> Make sure that you're signed in to both the Azure portal and Azure DevOps under the same Microsoft account.

1. In Azure DevOps, go to your **Space Game - web - Multistage** project.

2. From the lower-left corner of the page, select **Project settings**.

3. Under **Pipelines**, select **Service connections**.

4. Select **Create service connection**, then select **Azure Resource Manager**, and then select **Next**.

5. At the beginning of the page, select **App registration (automatic)**. Then, select **Next**.

6. Fill in these fields:

| Field | Value |
|-------|-------|
| Scope level | Subscription |
| Subscription | Your Azure subscription |
| Resource Group | tailspin-space-game-rg |
| Service connection name | Resource Manager - Tailspin - Space Game |

During the process, you might be prompted to sign in to your Microsoft account.

7. Ensure that you select **Grant access permission to all pipelines**.

8. Select **Save**.

To verify that it can connect to your Azure subscription, Azure DevOps performs a test connection. If Azure DevOps can't connect, you have the chance to sign in a second time.


# Exercise - 2.4 Promote to the Dev stage

The team has a plan and is ready to begin implementing their release pipeline. Your Azure DevOps project is set up, and your Azure App Service instances are ready to receive build artifacts.

At this point, remember that the team's pipeline has only two stages. The first stage produces the build artifact. The second stage deploys the Space Game web app to App Service. Here, you follow along with Andy and Mara as they modify the pipeline. They're going to deploy to the App Service environment that corresponds to the Dev stage.

The Dev stage resembles the deployment stage that you made in the **Create a release pipeline in Azure Pipelines** module. There, you used a CI trigger to start the build process. Here you do the same.

## Fetch the branch from GitHub

Here, you fetch the `release` branch from GitHub. You also check out, or switch to, the branch.

This branch serves as your release branch. It contains the Space Game project used in previous modules. It also contains an Azure Pipelines configuration to start with.

To fetch and switch to the branch:

1. In Visual Studio Code, open the integrated terminal.

2. To fetch a branch named `release` from the Microsoft repository, and to switch to that branch, run the following git commands.

```bash
git fetch upstream release
git checkout -B release upstream/release
```

The format of these commands enables you to get starter code from the Microsoft GitHub repository, known as `upstream`. Shortly, you're going to push this branch up to your GitHub repository, known as `origin`.

3. As an optional step, from Visual Studio Code, open `azure-pipelines.yml`. Familiarize yourself with the initial configuration.

The configuration resembles the basic one that you created in the **Create a release pipeline with Azure Pipelines** module. It builds only the app's release configuration. For learning purposes, this configuration doesn't run the quality or security checks that you set up in previous modules.

> **Note**
> 
> A more robust configuration might specify the branches that participate in the build process. For example, to help verify code quality, you might run unit tests each time you push up a change on any branch. You might also deploy the application to an environment that performs more exhaustive testing. But you do this deployment only when you have a pull request, when you have a release candidate, or when you merge code to main.
> 
> For more information, see [Implement a code workflow in your build pipeline by using Git and GitHub](https://docs.microsoft.com/learn/modules/implement-code-workflow/) and [Build pipeline triggers](https://docs.microsoft.com/azure/devops/pipelines/build/triggers).

## Promote changes to the Dev stage

Here, you modify your pipeline configuration to promote the build to the Dev stage.

1. In Visual Studio Code, modify `azure-pipelines.yml`.

```yaml
trigger:
- '*'

variables:
  buildConfiguration: 'Release'
  releaseBranchName: 'release'

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

- stage: 'Dev'
  displayName: 'Deploy to the dev environment'
  dependsOn: Build
  condition: |
    and
    (
      succeeded(),
      eq(variables['Build.SourceBranchName'], variables['releaseBranchName'])
    )
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
              appName: '$(WebAppNameDev)'
              package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/*.zip'
```

This configuration resembles the one that you built in the previous module. There, you and the team built a proof of concept for continuous deployment. But note these differences, which are highlighted in the preceding code example:

- This configuration defines variables at the beginning of the file. The variables are used throughout the pipeline. They define which configuration to build (Release). They also define the name of your release branch (release).
- The Deploy stage from the proof of concept is now named Dev.
- The Dev stage uses a condition that directs the system to run the stage only when the previous stage succeeds and the current branch is release. This setup ensures that release features are deployed only to the Dev environment.
- The deployment step uses the `WebAppNameDev` variable to deploy to the App Service instance associated with the Dev environment.

> **Note**
> 
> In practice, you might deploy from some other branch, such as main. You can include logic that allows changes to be promoted to the Dev stage from multiple branches, such as release and main.

2. From the integrated terminal, add `azure-pipelines.yml` to the index. Commit the change, and push it up to GitHub.

> **Tip**
> 
> Before you run these Git commands, save `azure-pipelines.yml`.

```bash
git add azure-pipelines.yml
git commit -m "Deploy to the Dev stage"
git push origin release
```

3. In Azure Pipelines, go to the build. As it runs, trace the build.

4. After the build finishes, to return to the summary page, select the back button.

![A screenshot of Azure Pipelines showing the completed stages.](azure-pipelines-dev-complete.png)

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/4-pipeline-dev-stage-summary.png)

You see that the deployment finished successfully.

5. From a web browser, go to the URL associated with the App Service instance for your Dev environment.

If you still have the browser tab open, refresh the page. If you don't remember the URL, find it in the Azure portal, on the App Service details page.

You see that the Space Game website is deployed to App Service, and is running.

![A screenshot of a web browser showing the Space Game web site in the Dev environment.](space-game-dev-environment.png)

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/4-pipeline-dev-stage-summary.png)

6. As an optional step, in Azure Pipelines, select **Environments**. Then, select the **dev** environment.

Azure Pipelines records your deployment history. In the history, you can trace the environment's changes back to code commits and work items.


![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/4-environment-dev.png)



# 2.5 Exercise - Promote to the Test stage

Your release pipeline still has two stages, but they're now different than before. The stages are Build and Dev. Every change you push to GitHub triggers the Build stage to run. The Dev stage runs only when the change is in the release branch. Here, you add the Test stage to the pipeline.

Recall that the team decided to use a scheduled trigger to promote the build from the Dev stage to the Test stage at 3 A.M. each morning. To set up the scheduled trigger:

- Define the schedule in your build configuration.
- Define the Test stage, which includes a condition that runs the stage only if the build reason is marked as Schedule.

For learning purposes, here, you define the schedule but allow the build to go directly from Dev to Test. This setup avoids the need to wait for the schedule to be triggered. After you complete this module, try experimenting with different cron expressions to run the Test stage only at the scheduled time.

## Promote changes to the Test stage

Here, you modify your pipeline configuration to deploy the build to the Test stage.

1. In Visual Studio Code, modify `azure-pipelines.yml` as follows:

```yaml
trigger:
- '*'

variables:
  buildConfiguration: 'Release'
  releaseBranchName: 'release'

schedules:
- cron: '0 3 * * *'
  displayName: 'Deploy every day at 3 A.M.'
  branches:
    include:
    - release
  always: false 

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

- stage: 'Dev'
  displayName: 'Deploy to the dev environment'
  dependsOn: Build
  condition: |
    and
    (
      succeeded(),
      eq(variables['Build.SourceBranchName'], variables['releaseBranchName'])
    )
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
              appName: '$(WebAppNameDev)'
              package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/*.zip'

- stage: 'Test'
  displayName: 'Deploy to the test environment'
  dependsOn: Dev
  #condition: eq(variables['Build.Reason'], 'Schedule')
  jobs:
  - deployment: Deploy
    pool:
      vmImage: 'ubuntu-20.04'
    environment: test
    variables:
    - group: 'Release'
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
              appName: '$(WebAppNameTest)'
              package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/*.zip'
```

The `schedules` section defines one cron expression. You can define more than one expression in your configuration. The expression triggers the pipeline to run against the release branch at 3 A.M. each day. The `always` flag is set to `false` so that the pipeline runs only when the release branch contains changes from the prior run.

The Test stage defines a condition that runs the stage only when the build reason equals `Schedule`. (The built-in variable `Build.Reason` defines the build reason.) If this condition is false, the stage is skipped, but the prior stages continue to run.

> **Note**
> 
> This condition is shown for learning purposes. It's commented to enable the change to go from Dev to Test without waiting for the schedule to be triggered.

2. From the integrated terminal, to the index, add `azure-pipelines.yml`. Then, commit the change, and push it up to GitHub.

> **Tip**
> 
> Before you run these Git commands, save `azure-pipelines.yml`.

```bash
git add azure-pipelines.yml
git commit -m "Deploy to the Test stage"
git push origin release
```

3. In Azure Pipelines, go to the build. Trace the build as it runs.

4. After the build finishes, to return to the summary page, select the back button.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/5-pipeline-test-stage-summary.png)

You see that the deployment finished successfully.

5. From a web browser, go to the URL associated with the App Service instance for your Test environment.

If you still have the browser tab open, refresh the page. If you don't remember the URL, find it in the Azure portal, on the App Service details page.

You see that the Space Game website is deployed to App Service, and it's running.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/5-app-service-test.png)

6. As an optional step, in Azure Pipelines, select **Environments**. Then, select the **test** environment.

Azure Pipelines records your deployment history. In the history, you can trace changes in the environment back to code commits and work items.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/5-environment-test.png)

Andy and Mara add the Test stage to the pipeline. They show the results to Amita.

**Amita:** I like that changes are built and deployed so that I can test them each morning. But I don't see how I can control when changes arrive at Staging.

**Mara:** Yes, deploying through automation saves lots of time. Remember that we included only the scheduled trigger. Let's add a release approval for you when we set up the Staging environment for Tim. That way, changes move to Staging only when you're ready.



# 2.6 Exercise - Promote to Staging

Your release pipeline now has three stages: Build, Dev, and Test. You and the Tailspin team have one more stage to implement: Staging.

In this part, you'll:

- Create the staging environment in Azure Pipelines, and assign yourself as an approver.
- Define the Staging stage, which runs only after an approver verifies the results of the Test stage.

## Create the staging environment

Here, you create an environment in Azure Pipelines for Staging. For learning purposes, you assign yourself as the approver. In practice, you would assign the users who are required to approve changes before those changes move to the next stage. For the Tailspin team, Amita approves changes so that they can be promoted from Test to Staging.

Earlier in this module, you specified environment settings for both Dev and Test stages. Here's an example for the Dev stage.

```yaml
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
```

You can define an environment through Azure Pipelines that includes specific criteria for your release. This criteria can include the pipelines that are authorized to deploy to the environment. You can also specify the human approvals that are needed to promote the release from one stage to the next. Here, you specify those approvals.

To create the staging environment:

1. From Azure Pipelines, select **Environments**.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/pipelines-environments.png)

2. Select **New environment**.

3. Under **Name**, enter **staging**.

4. Leave the remaining fields at their default values.

5. Select **Create**.

6. On the staging environment page, select the **Approvals and checks** tab.

7. Select **Approvals**.

8. Under **Approvers**, select **Add users and groups**, and then select your account.

9. Under **Instructions to approvers**, enter **Approve this change when it's ready for staging**.

10. Select **Create**.

## Promote changes to Staging

Here you modify your pipeline configuration to deploy the build to the Staging stage.

1. In Visual Studio Code, modify `azure-pipelines.yml` as follows:

```yaml
trigger:
- '*'

variables:
  buildConfiguration: 'Release'
  releaseBranchName: 'release'

schedules:
- cron: '0 3 * * *'
  displayName: 'Deploy every day at 3 A.M.'
  branches:
    include:
    - release
  always: false 

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

- stage: 'Dev'
  displayName: 'Deploy to the dev environment'
  dependsOn: Build
  condition: |
    and
    (
      succeeded(),
      eq(variables['Build.SourceBranchName'], variables['releaseBranchName'])
    )
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
              appName: '$(WebAppNameDev)'
              package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/*.zip'

- stage: 'Test'
  displayName: 'Deploy to the test environment'
  dependsOn: Dev
  #condition: eq(variables['Build.Reason'], 'Schedule')
  jobs:
  - deployment: Deploy
    pool:
      vmImage: 'ubuntu-20.04'
    environment: test
    variables:
    - group: 'Release'
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
              appName: '$(WebAppNameTest)'
              package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/*.zip'

- stage: 'Staging'
  displayName: 'Deploy to the staging environment'
  dependsOn: Test
  jobs:
  - deployment: Deploy
    pool:
      vmImage: 'ubuntu-20.04'
    environment: staging
    variables:
    - group: 'Release'
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
              appName: '$(WebAppNameStaging)'
              package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/*.zip'
```

This code adds the Staging stage. The stage deploys to the staging environment, which includes a release approval.

> **Tip**
> 
> You probably noticed that all three of your deployment stages follow similar steps. You can use templates to define common build tasks one time and reuse them multiple times. You already used this technique in the **Create a build pipeline with Azure Pipelines** module. For learning purposes, we repeat the steps in each stage.

2. From the integrated terminal, add `azure-pipelines.yml` to the index. Next, commit the change and push it up to GitHub.

> **Tip**
> 
> Before you run these Git commands, save `azure-pipelines.yml`.

```bash
git add azure-pipelines.yml
git commit -m "Deploy to Staging"
git push origin release
```

3. In Azure Pipelines, go to the build. Trace the build as it runs.

4. When the build reaches Staging, you see that the pipeline waits for all checks to pass. In this case, there's one check - the manual release approval.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/7-pipeline-review.png)

You can configure Azure DevOps to send you an email notification when the build requires approval. Here's an example:

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/6-email-notification.png)

5. Select **Review > Approve**.

In practice, to verify that they meet your requirements, you would inspect the changes.

6. After the build finishes, open a web browser. Go to the URL associated with the App Service instance for your staging environment.

If you still have the browser tab open, refresh the page. If you don't remember the URL, find it in the Azure portal, on the App Service details page.

You see that the Space Game website is deployed to App Service and is running.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/6-app-service-staging.png)

7. As an optional step, in Azure Pipelines, select **Environments**. Next, select the **staging** environment.

Azure Pipelines records your deployment history, which enables you to trace changes in the environment back to code commits and work items.

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/6-environment-staging.png)

The Tailspin team gathers to discuss their progress. Amita approves changes in the Test stage while the others watch.

**Tim:** To tell you the truth, at first I was a little nervous about automated release pipelines. But I really like this now that I see it working. Each stage can have its own environment, associated tests, and approvers. The pipeline automates many things that we had to do manually. But we still have control where we need it.

**Amita:** I could imagine us doing something similar to promote changes from Staging to Production. Speaking of, when do we add a production environment?

**Andy:** Shortly. I think we still need to fill in a few pieces here first before we add that.


# 2.7 Exercise - Clean up your Azure DevOps environment

You're finished with the tasks for this module. In this unit, you clean up your Azure resources, move the work item to the Done state on Azure Boards, and clean up your Azure DevOps environment.

> **Important**
> 
> This page contains important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes. It also helps ensure that you're not charged for Azure resources after you complete this module.

## Clean up Azure resources

Here, you delete your Azure App Service instances. The easiest way to delete the instances is to delete their parent resource group. When you delete a resource group, you delete all resources in that group.

In the **Create a release pipeline with Azure Pipelines** module, you managed Azure resources through the Azure portal. Here, you can tear down your deployment by using the Azure CLI through Azure Cloud Shell. The steps are similar to the steps that you used when you created the resources.

To clean up your resource group:

1. Go to the [Azure portal](https://portal.azure.com), and sign in.

2. From the menu bar, select **Cloud Shell**. When prompted, select the **Bash** experience.

![A screenshot of the Azure portal showing the location of the Cloud Shell menu item.](azure-portal-cloud-shell.png)

3. To delete the resource group that you used, `tailspin-space-game-rg`, run the following `az group delete` command.

```bash
az group delete --name tailspin-space-game-rg
```

When prompted, to confirm the operation, enter `y`.

4. As an optional step, after the previous command finishes, run the following `az group list` command.

```bash
az group list --output table
```

You see that the resource group `tailspin-space-game-rg` no longer exists.

## Move the work item to Done

Now, move the work item that you assigned to yourself earlier in this module. Move **Create a multistage pipeline** to the **Done** column.

In practice, "Done" often means putting working software into the hands of your users. For learning purposes, here, you mark this work as done because you fulfilled the goal for the Tailspin team. They wanted to define a complete multistage pipeline to deliver new features.

At the end of each sprint, or work iteration, you and your team can hold a retrospective meeting. In the meeting, share the work you completed, what went well, and what you can improve.

To complete the work item:

1. From Azure DevOps, go to **Boards**, and from the menu, select **Boards**.

2. Move the **Create a multistage pipeline** work item, from the **Doing** column to the **Done** column.

![A screenshot of Azure Boards, showing the card in the Done column.](azure-boards-done-column.png)

## Disable the pipeline or delete your project

Each module in this learning path provides a template. You can run the template to create a clean environment for the module.

Running multiple templates gives you multiple Azure Pipelines projects. Each project points to the same GitHub repository. This setup can trigger multiple pipelines to run each time you push a change to your GitHub repository. The pipeline runs use up free build minutes on our hosted agents. To avoid losing those free build minutes, disable or delete your pipeline before you move to the next module.

Select one of the following options.

### Option 1: Disable the pipeline

Disable the pipeline so that it doesn't process build requests. You can re-enable the build pipeline later if you want to. Select this option if you want to keep your DevOps project and your build pipeline for future reference.

To disable the pipeline:

1. In Azure Pipelines, go to your pipeline.

2. From the dropdown, select **Settings**.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-portal-menu-cloud-shell.png)

3. Under **Processing of new run requests**, select **Disabled**, and then select **Save**.

Now, your pipeline no longer processes build requests.

### Option 2: Delete the Azure DevOps project

Delete your Azure DevOps project, including the contents of Azure Boards and your build pipeline. In future modules, you can run another template that brings up a new project in a state where this project leaves off. Select this option if you don't need your DevOps project for future reference.

To delete the project:

1. In Azure DevOps, go to your project. Earlier, we recommended that you name this project **Space Game - web - Multistage**.

2. Select **Project settings** in the lower-left corner of your Azure DevOps page.

3. In the **Project details** area, scroll down and select **Delete**.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-delete-project.png)

4. In the window that appears, enter the project name. Select **Delete** again.

Your project is now deleted.


# 2.8 Summary

Nice job! Your pipeline is taking shape. You and the Tailspin team moved from a basic proof of concept to a realistic release pipeline. You can use this pipeline to build an artifact and test it before you give it to your users.

In this module, you learned ways to control how changes move from one stage of a pipeline to the next. Let's review the pipeline you built in this module. This image shows your pipeline's overall shape:

![](https://learn.microsoft.com/en-us/training/azure-devops/create-multi-stage-pipeline/media/2-add-staging-stage-approval.png)

The *Dev*, *Test*, and *Staging* stages each deploy the build artifact to their own Azure App Service environment.

* When a change is pushed to GitHub, a *trigger* causes the *Build* stage to run. The *Build* stage produces a build artifact as its output.
* The *Dev* stage runs only when the change happens in the *release* branch. You use a *condition* to specify this requirement.
* The *Test* stage runs at 3 A.M. each day. This stage runs only when the *release* branch contains changes since the last run. You use a *scheduled trigger* to specify when the *Test* stage runs.
* The *Staging* stage runs only after you approve the changes in the *Test* stage. You add a *release approval* to the **staging** environment to pause the pipeline until you approve or reject the change.

This pipeline satisfies the requirements of the Tailspin team. Your pipeline's shape and how changes flow through it depend on the needs of your team, and of the apps and services that you build.

Although the team is improving their release cadence, there's room for more improvement. For example, Amita from QA must manually test and approve builds before the team can present new features to management. In the next module, you'll work with the Tailspin team to automate more testing so that changes can move through the pipeline even faster.

## Learn more

In this module, you worked with conditions, triggers, and approvals. To learn more, explore these resources.

* [Conditions](https://docs.microsoft.com/azure/devops/pipelines/process/conditions)
* [Build pipeline triggers](https://docs.microsoft.com/azure/devops/pipelines/build/triggers)
* [Approvals and other checks](https://docs.microsoft.com/azure/devops/pipelines/process/approvals)





# 3 Run functional tests in Azure Pipelines

Run Selenium UI tests, a form of functional testing, in Azure Pipelines.
#### Learning objectives
After completing this module, you'll be able to:
- Define the role of functional tests and identify some popular kinds of tests you can run.
- Map manual testing steps to automated test cases.
- Run automated UI tests locally and in the pipeline by using Selenium.
#### Prerequisites
- An Azure subscription
- An Azure DevOps organization with access to Microsoft-hosted parallel jobs. Check your parallel jobs and request a free grant.
- Visual Studio Code
- .NET 8.0 SDK
- Git
- A GitHub account



# 3.1 **Introduction**

In this module, you'll add functional tests to the pipeline. These tests verify an application's behavior.

In the **Create a multistage pipeline by using Azure Pipelines** module, you helped the Tailspin Toys web team design and build a multistage release pipeline. The team uses the pipeline to move changes through a series of stages. Changes move through the *Dev* stage, the *Test* stage, and finally the *Staging* stage, which resembles a production environment.

The stages that you and the team defined provide the overall shape of the pipeline, but you can add more to each stage. For example, in the *Test* stage, Amita still tests the web application manually as she always has. When she's satisfied, she manually promotes the application to *Staging*. In *Staging*, management reviews the new features and decides whether to make the release publicly available.

In the **Run quality tests in your build pipeline using Azure Pipelines** module, you incorporated unit and code coverage tests into the build process. These tests help avoid regression bugs and ensure that the code meets the company's standards for quality and style. But what kinds of tests can you run after a service is operational and deployed to an environment?

## **Learning objectives**

After completing this module, you'll be able to:

* Define the role of functional tests and identify some popular kinds of tests you can run.
* Map manual testing steps to automated test cases.
* Run automated UI tests locally and in the pipeline using Selenium.

## **Prerequisites**

The modules in this learning path form a progression. To follow the progression from the beginning, complete these learning paths first:

* **Get started with Azure DevOps**
* **Build applications with Azure DevOps**

We also recommend that you start at the beginning of the **Deploy applications with Azure DevOps** learning path.

If you want to go through just this module, you need to set up a development environment on your Windows, macOS, or Linux system. You need these assets:

* An Azure subscription
* An Azure DevOps organization with access to parallel jobs. If your organization does not have access to parallel jobs, you can request parallel jobs for free for public or private projects using [this form](https://aka.ms/azpipelines-parallelism-request). Your request takes 2-3 business days.
* A GitHub account
* Visual Studio Code
* .NET 8.0 SDK
* Git

You can get started with Azure and Azure DevOps for free. You don't need an Azure subscription to work with Azure DevOps, but here you'll use Azure DevOps to deploy to resources that exist in your Azure subscription.

This environment lets you complete the exercises in this module and future modules. You can also use it to apply your new skills to your own projects.

> **Note**
> 
> Azure Pipelines support a vast array of **languages and application types**. In this module, you'll be working with a .NET application but you can apply the patterns you learn here to your own projects that use your favorite programming languages and frameworks.

## **Meet the team**

You met the *Space Game* web team at Tailspin Toys in previous modules. As a refresher, here's who you'll work with in this module.

**Andy** is the development lead.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/andy.png)

**Amita** is in QA.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/amita.png)

**Tim** is in operations.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/tim.png)

**Mara** just joined as a developer and reports to Andy.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/mara.png) 
Mara has prior experience with DevOps. She's helping the team adopt a more automated process that uses Azure DevOps.





# 3.2 **What is functional testing?**

In this section, you join the Tailspin team as they define functional tests for their pipeline. Functional tests verify whether each function of the software does what it should.

The team first defines what a functional test covers. They explore some types of functional tests. Then they decide on the first test to add to their pipeline.

## **Weekly meeting**

The team is having their weekly meeting. Andy is demonstrating the release pipeline. The team watches a successful build move through the pipeline, from one stage to another. Finally, the web app is promoted to Staging.

**Amita:** I'm so happy with the pipeline. It makes my life much easier. For one thing, I automatically get a release deployed to the test environment. That means I don't have to manually download and install build artifacts on my test servers. That's a significant time saver.

Also, the unit tests that Mara and Andy wrote eliminate all the regression bugs before I get the release. That removes a major source of frustration. I don't spend time finding and documenting regression bugs.

But I'm worried that all of my testing is still manual. The process is slow, and we can't show anything to management until I finish. It's hard because testing is important. Testing ensures that the users get the right experience. But the pressure is on to deliver faster.

**Andy:** I'm sure we can help you. What kind of tests take up most of your time?

**Amita:** I think the UI tests do. I have to click through every step to make sure I get the correct result, and I have to do that for every browser we support. It's very time-consuming. And as the website grows in complexity, UI testing won't be practical in the long run.

**Mara:** UI tests are considered to be functional tests.

**Tim:** As opposed to what, nonfunctional tests?

**Mara:** Exactly. And nonfunctional tests are something that you in particular, care about.

**Tim:** Okay, I'm confused.

## **What are functional and nonfunctional tests?**

**Mara:** Functional tests verify that each function of the software does what it should. How the software implements each function isn't important in these tests. What's important is that the software behaves correctly. You provide input and check that the output is what you expect. That's how Amita tests the UI. For example, if she selects the top player on the leaderboard, she expects to see that player's profile.

Nonfunctional tests check characteristics like performance and reliability. An example of a nonfunctional test is checking how many people can simultaneously sign up in to the app. Load testing is another example of a nonfunctional test. Those performance and reliability concerns are things you care about, Tim.

**Tim:** They are, indeed. I need to think about this for a bit. I might want to add some automation to the pipeline too, but I'm not sure what I want to do. What kinds of automated tests can I run?

**Mara:** For now, let's focus on functional testing. It's the kind of testing that Amita does, and it sounds like an area where we want to improve.

## **What kinds of functional tests can I run?**

There are many kinds of functional tests. They vary by the functionality that you need to test and the time or effort that they typically require to run.

The following sections present some commonly used functional tests.

### **Smoke testing**

Smoke testing verifies the most basic functionality of your application or service. These tests are often run before more complete and exhaustive tests. Smoke tests should run quickly.

For example, say you're developing a website. Your smoke test might use curl to verify that the site is reachable and that fetching the home page produces a 200 (OK) HTTP status. If fetching the home page produces another status code, such as 404 (Not Found) or 500 (Internal Server Error), you know that the website isn't working. You also know that there's no reason to run other tests. Instead, you diagnose the error, fix it, and restart your tests.

### **Unit testing**

You worked with unit tests in the **Run quality tests in your build pipeline using Azure Pipelines** module.

In short, unit testing verifies the most fundamental components of your program or library, such as an individual function or method. You specify one or more inputs along with the expected results. The test runner performs each test and checks to see whether the actual results match the expected results.

As an example, let's say you have a function that performs an arithmetic operation that includes division. You might specify a few values that you expect your users to enter. You also specify edge-case values such as 0 and -1. If you expect a certain input to produce an error or exception, you can verify that the function produces that error.

The UI tests that you'll run later in this module are unit tests.

### **Integration testing**

Integration testing verifies that multiple software components work together to form a complete system. For example, an e-commerce system might include a website, a products database, and a payment system. You might write an integration test that adds items to the shopping cart and then purchases the items. The test verifies that the web application can connect to the products database and then fulfill the order.

You can combine unit tests and integration tests to create a layered testing strategy. For example, you might run unit tests on each of your components before running the integration tests. If all unit tests pass, you can move on to the integration tests with greater confidence.

### **Regression testing**

A regression occurs when existing behavior either changes or breaks after you add or change a feature. Regression testing helps determine whether code, configuration, or other changes affect the software's overall behavior.

Regression testing is important because a change in one component can affect the behavior of another component. For example, say you optimize a database for write performance. The read performance of that database, which is handled by another component, might unexpectedly drop. The drop in read performance is a regression.

You can use various strategies to test for regression. These strategies typically vary by the number of tests you run to verify that a new feature or bug fix doesn't break existing functionality. However, when you automate the tests, regression testing might involve just running all unit tests and integration tests each time the software changes.

### **Sanity testing**

Sanity testing involves testing each major component of a piece of software to verify that the software appears to be working and can undergo more thorough testing. You can think of sanity tests as being less thorough than regression tests or unit tests, but sanity tests are broader than smoke tests.

Although sanity testing can be automated, it's often done manually in response to a feature change or a bug fix. For example, a software tester who's validating a bug fix might also verify that other features are working by entering some typical values. If the software appears to be working as expected, it can then go through a more thorough test pass.

### **User interface testing**

User interface (UI) testing verifies the behavior of an application's user interface. UI tests help verify that the sequence, or order, of user interactions, leads to the expected result. These tests also help verify that input devices, such as the keyboard or mouse, affect the user interface properly. You can run UI tests to verify the behavior of a native Windows, macOS, or Linux application. Or you can use UI tests to verify that the UI behaves as expected across web browsers.

A unit test or integration test might verify that the UI receives data correctly. But UI testing helps verify that the user interface displays correctly and that the result functions as expected for the user.

For example, a UI test might verify that the correct animation appears in response to a button click. A second test might verify that the same animation appears correctly when the window is resized.

In this module, you work with UI tests that are coded by hand. But you can also use a capture-and-replay system to automatically build your UI tests.

### **Usability testing**

Usability testing is a form of manual testing that verifies an application's behavior from the user's perspective. The team that builds the software typically does the usability testing.

Whereas UI testing focuses on whether a feature behaves as expected, usability testing helps verify that the software is intuitive and meets the user's needs. In other words, usability testing helps verify whether the software is "usable."

For example, say you have a website that includes a link to the user's profile. A UI test can verify that the link is present and that it brings up the user's profile when the link is selected. However, if humans can't easily locate this link, they might become frustrated when they try to access their profile.

### **User acceptance testing**

User acceptance testing (UAT), like usability testing, focuses on an application's behavior from the user's perspective. Unlike usability testing, UAT is typically done by real end users.

Depending on the software, end users might be asked to complete specific tasks. Or they might be allowed to explore the software without following specific guidelines. For custom software, UAT typically happens directly with the client. For more general-purpose software, teams might run beta tests. In beta tests, users from different geographic regions or those with particular interests receive early access to the software.

Feedback from testers can be direct or indirect. Direct feedback might come in the form of verbal comments. Indirect feedback can come in the form of measuring testers' body language, eye movements, or the time they take to complete certain tasks.

We've already covered the importance of writing tests. But just to emphasize it, here's a short video where Abel Wang, Cloud Advocate at Microsoft, explains how to help ensure quality in your DevOps plan.

**Ask Abel**

[Video placeholder]

## **What does the team choose?**

**Tim:** All of these tests sound important. Which should we tackle first?

**Andy:** We already have working unit tests. We're not yet ready to perform user acceptance testing. Based on what I hear, I think we should focus on UI testing. Right now, it's the slowest part of our process. Amita, do you agree?

**Amita:** Yes, I do agree. We still have some time left in this meeting. Andy or Mara, do you want to help me plan an automated UI test?

**Mara:** Absolutely. But let's get a few preliminaries out of the way. I'd like to discuss what tool we should use and how we'll run the tests.

## **What tools can I use to write UI tests?**

**Mara:** When it comes to writing UI tests, what are our options? I know there are many. Some tools are open source. Others offer paid commercial support. Here are a few options that come to mind:

* **Windows Application Driver (WinAppDriver):** WinAppDriver helps you automate UI tests on Windows apps. These apps can be written in Universal Windows Platform (UWP) or Windows Forms (WinForms). We need a solution that works in a browser.
* **Selenium:** Selenium is a portable open-source software-testing framework for web applications. It runs on most operating systems, and it supports all modern browsers. You can write Selenium tests in several programming languages, including C#. In fact, you can use NuGet packages that make it easy to run Selenium as NUnit tests. We already use NUnit for our unit tests.
* **SpecFlow:** SpecFlow is for .NET projects. It's inspired by a tool called Cucumber. Both SpecFlow and Cucumber support behavior-driven development (BDD). BDD uses a natural-language parser called Gherkin to help both technical teams and nontechnical teams define business rules and requirements. You can combine either SpecFlow or Cucumber with Selenium to build UI tests.

Andy looks at Amita.

**Andy:** I know these options are new to you, so do you mind if we pick Selenium? I have some experience with it, and it supports languages I already know. Selenium also gives us automatic support for multiple browsers.

**Amita:** Sure. It's better if one of us has some experience.

## **How do I run functional tests in the pipeline?**

In Azure Pipelines, you run functional tests just like you run any other process or test. Ask yourself:

* In which stage will the tests run?
* On what system will the tests run? Will they run on the agent or on the infrastructure that hosts the application?

Let's join the team as they answer these questions.

**Mara:** One thing I'm excited about is that now we can test in an environment that's like production, where the app is actually running. Functional tests like UI tests make sense in that context. We can run them in the Test stage of our pipeline.

**Amita:** I agree. We can maintain the same workflow if we run automated UI tests in the same stage in which I run manual tests. Automated tests will save us time and enable me to focus on usability.

**Tim:** Amita tests the website from her Windows laptop because that's how most of our users visit the site. But we build on Linux and then deploy Azure App Service on Linux. How do we handle that?

**Mara:** Great question. We also have a choice about where we run the tests. We can run them:

* **On the agent:** either a Microsoft agent or an agent that we host.
* **On test infrastructure:** either on-premises or in the cloud.

Our existing Test stage includes one job. That job deploys the website to App Service from a Linux agent. We can add a second job that runs the UI tests from a Windows agent. The Windows agent that's hosted by Microsoft is already set up to run Selenium tests.

**Andy:** Again, let's stick with what we know. Let's use a Microsoft-hosted Windows agent. Later, we can run the same tests from agents that run macOS and Linux if we need additional test coverage.

## **The plan**

**Mara:** OK. Here's what we're going to do:

* Run Selenium UI tests from a Microsoft-hosted Windows agent.
* Have the tests fetch the web content from the app that's running on App Service, in the Test stage.
* Run the tests on all the browsers that we support.

**Andy:** I'll work with Amita on this one. Amita, let's meet tomorrow morning. I'd like to do a bit of research before we meet.

**Amita:** Great! See you then.

## **Create a functional test plan**

We've seen the team decide on how they'll implement their first functional tests. If your team is just starting to incorporate functional tests into their pipeline (or even if you're already doing that), remember that you always need a plan.

Many times, when someone asks team members about their performance testing plan, it's common for them to respond with a list of tools they're going to use. However, a list of tools isn't a plan. You must also work out how the testing environments will be configured. You need to determine the processes to use, and determine what success or failure looks like.

Make sure your plan:

* Takes the expectations of the business into account.
* Takes the expectations of the target users into account.
* Defines the metrics you'll use.
* Defines the KPIs you'll use.

Performance testing needs to be part of your planning, right from the start. If you use a story or Kanban board, you might consider having an area near it where you can plan out your testing strategy. As part of the iteration planning, you should highlight gaps in the testing strategy. It's also important to work out how you'll monitor performance once the application has been deployed, and not just measure performance before it's released.

## **Check your knowledge**

### **1. Your customer service team receives too many refund requests from customers who accidentally make purchases from your mobile application. Customers report that the Purchase button and Cancel button are too close together. Which kind of functional testing might help catch this sort of problem before it reaches your users?**

❌ UI testing

❌ Integration testing

✅ **Usability testing**

### **2. Your user experience (UX) team proposed some drastic changes to your website's home page. Which kind of functional testing can you use to ensure that each button on the page performs the correct function?**

✅ **UI testing**

❌ Integration testing

❌ Unit testing

### **3. Which kind of functional testing is typically performed by humans rather than through automation?**

❌ Unit testing

✅ **Usability testing**

❌ Smoke testing

---

## **Відповіді на запитання:**

**Запитання 1:** Usability testing - цей тип тестування допомагає виявити проблеми зручності використання, такі як розташування кнопок занадто близько одна до одної.

**Запитання 2:** UI testing - перевіряє, чи функціонують кнопки правильно та чи виконують вони потрібні дії.

**Запитання 3:** Usability testing - зазвичай виконується людьми для оцінки зручності та інтуїтивності інтерфейсу.




# 3.3 **Exercise - Set up your Azure DevOps environment**

In this section, you make sure that your Azure DevOps organization is set up to complete the rest of this module. You also create the Azure App Service environments that you'll deploy.

To accomplish these tasks, you:

* Add a user to ensure that Azure DevOps can connect to your Azure subscription.
* Set up an Azure DevOps project for this module.
* Move the work item for this module on Azure Boards to the Doing column.
* Create the Azure App Service environments by using the Azure CLI in Azure Cloud Shell.
* Create pipeline variables that define the names of your App Service environments.
* Create a service connection that enables Azure Pipelines to access your Azure subscription securely.

## **Add a user to Azure DevOps**

To complete this module, you need your own Azure subscription. You can get started with Azure for free.

Although you don't need an Azure subscription to work with Azure DevOps, you'll use Azure DevOps here to deploy to resources that exist in your Azure subscription. To simplify the process, sign in to both your Azure subscription and your Azure DevOps organization under the same Microsoft account.

If you use different Microsoft accounts to sign in to Azure and Azure DevOps, add a user to your DevOps organization under the Microsoft account that you use to sign in to Azure. For more information, see [Add users to your organization or project](https://docs.microsoft.com/azure/devops/organizations/accounts/add-organization-users). When you add the user, choose the **Basic** access level.

Then, sign out of Azure DevOps and sign in again under the Microsoft account that you use to sign in to your Azure subscription.

## **Get the Azure DevOps project**

Here, you make sure that your Azure DevOps organization is set up to complete the rest of this module. You accomplish this task by running a template that creates a project in Azure DevOps.

The modules in this learning path form a progression as you follow the Tailspin web team through their DevOps journey. For learning purposes, each module has an associated Azure DevOps project.

### **Run the template**

Run a template that sets up your Azure DevOps organization.

1. Get and run the ADOGenerator project in Visual Studio or the IDE of your choice.

2. When prompted to **Enter the template number from the list of templates**, enter **32** for **Run functional tests in Azure Pipelines**, then press Enter.

3. Choose your authentication method. You can set up and use a Personal Access Token (PAT) or use device login.

> **Note**
> 
> If you set up a PAT, make sure to authorize the necessary scopes. For this module, you can use Full access, but in a real-world situation, you should ensure you grant only the necessary scopes.

4. Enter your Azure DevOps organization name, then press Enter.

5. If prompted, enter your Azure DevOps PAT, then press Enter.

6. Enter a project name such as **Space Game - web - Functional tests**, then press Enter.

Once your project is created, go to your Azure DevOps organization in your browser (at https://dev.azure.com/<your-organization-name>/) and select the project.

### **Fork the repository**

If you haven't already, create a fork of the mslearn-tailspin-spacegame-web-deploy repository.

1. On GitHub, go to the [mslearn-tailspin-spacegame-web-deploy](https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web-deploy) repository.

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

In this part, you assign yourself a work item in Azure Boards that relates to this module. You also move the work item to the **Doing** state. In practice, your team would create work items at the start of each sprint or work iteration.

Assigning work in this way gives you a checklist from which to work. It gives your team visibility into what you're working on and how much work is left. It also helps the team enforce limits on work in progress (WIP) to avoid taking on too much work at one time.

Recall that the team settled on these top issues for the current sprint:

*A screenshot of Azure Boards, showing the tasks for this sprint.*

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/deploy-all-tasks.png)

> **Note**
> 
> Within an Azure DevOps organization, work items are numbered sequentially. In your project, the number for each work item might not match what you see here.

Here you move the third item, **Automate quality tests**, to the **Doing** column. Then you assign yourself to the work item. **Automate quality tests** relates to automating UI tests for the Space Game website.

To set up the work item:

1. From Azure DevOps, go to **Boards**, and then select **Boards** from the menu.

*A screenshot of Azure DevOps showing the location of the Boards menu.*

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-boards-menu.png)

2. On the **Automate quality tests** work item, select the down arrow at the bottom of the card, then assign the work item to yourself.

*A screenshot of Azure Boards showing the location of the down arrow.*

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-boards-down-chevron.png)

3. Move the work item from the **To Do** column to the **Doing** column.

*A screenshot of Azure Boards, showing the card in the Doing column.*

![](https://learn.microsoft.com/en-us/training/azure-devops/run-functional-tests-azure-pipelines/media/3-azure-boards-wi3-doing.png)

At the end of this module, after you complete the task, you'll move the card to the **Done** column.

## **Set up the project locally**

Here you load the Space Game project in Visual Studio Code, configure Git, clone your repository locally, and set the upstream remote so that you can download starter code.

> **Note**
> 
> If you're already set up with the mslearn-tailspin-spacegame-web-deploy project locally, you can move to the next section.

### **Open the integrated terminal**

Visual Studio Code comes with an integrated terminal. Here you both edit files and work from the command line.

1. Start Visual Studio Code.

2. On the **View** menu, select **Terminal**.

3. In the dropdown list, select **Git Bash**. If you're familiar with another Unix shell that you prefer to use, select that shell instead.

*A screenshot of Visual Studio Code showing the location of the Git Bash shell.*

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/vscode-terminal-git-bash.png)

In the terminal window, you can choose any shell that's installed on your system. For example, you can choose Git Bash, or PowerShell, or another shell.

Here you'll use Git Bash, part of Git for Windows, which makes it easy to run Git commands.

> **Note**
> 
> On Windows, if you don't see Git Bash listed as an option, make sure you've installed Git, and then restart Visual Studio Code.

4. Run the `cd` command to go to the directory where you want to work. Choose your home directory (`~`) or a different directory if you want.

```bash
cd ~
```

### **Configure Git**

If you're new to Git and GitHub, first run a few commands to associate your identity with Git and authenticate with GitHub. For more information, see [Set up Git](https://docs.github.com/get-started/quickstart/set-up-git).

At a minimum, you need to complete the following steps. Run the commands from the integrated terminal.

* Set your username.
* Set your commit email address.
* Cache your GitHub password.

> **Note**
> 
> If you already use two-factor authentication with GitHub, create a personal access token. When you're prompted, use your token in place of your password.
> 
> Treat your access token like a password. Keep it in a safe place.

### **Set up your project in Visual Studio Code**

In the **Build applications with Azure DevOps** learning path, you forked and then cloned a Git repository. The repository contains the source code for the Space Game website. Your fork was connected to your projects in Azure DevOps so that the build runs when you push changes to GitHub.

> **Important**
> 
> In this learning path, we switch to a different Git repository, **mslearn-tailspin-spacegame-web-deploy**. When you ran the template to set up your Azure DevOps project, the process forked the repository automatically for you.

In this part, you clone your fork locally so that you can change and build out your pipeline configuration.

### **Clone your fork locally**

You now have a copy of the Space Game web project in your GitHub account. Now you'll download, or clone, a copy to your computer so you can work with it.

A clone, just like a fork, is a copy of a repository. When you clone a repository, you can make changes, verify that they work as you expect, and then upload those changes to GitHub. You can also synchronize your local copy with changes that other authenticated users have made to the GitHub copy of your repository.

To clone the Space Game web project to your computer:

1. Go to your fork of the Space Game web project (**mslearn-tailspin-spacegame-web-deploy**) on GitHub.

2. Select **Code**. Then, from the **HTTPS** tab, select the button next to the URL that's shown to copy the URL to your clipboard.

*Screenshot that shows how to locate the URL and copy button from the GitHub repository.*

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/github-clone-button.png)

3. In Visual Studio Code, go to the terminal window.

4. In the terminal, move to the directory where you want to work. Choose your home directory (`~`) or a different directory if you want.

```bash
cd ~
```

5. Run the `git clone` command. Replace the URL that's shown here with the contents of your clipboard:

```bash
git clone https://github.com/your-name/mslearn-tailspin-spacegame-web-deploy.git
```

6. Move to the mslearn-tailspin-spacegame-web-deploy directory. This is the root directory of your repository.

```bash
cd mslearn-tailspin-spacegame-web-deploy
```

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/app-service-default.png)

### **Set the upstream remote**

A remote is a Git repository where team members collaborate (like a repository on GitHub). Here you list your remotes and add a remote that points to Microsoft's copy of the repository so that you can get the latest sample code.

1. Run this `git remote` command to list your remotes:

```bash
git remote -v
```

You see that you have both fetch (download) and push (upload) access to your repository:

```
origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (fetch)
origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (push)
```

Origin specifies your repository on GitHub. When you fork code from another repository, the original remote (the one you forked from) is often named upstream.

2. Run this `git remote add` command to create a remote named upstream that points to the Microsoft repository:

```bash
git remote add upstream https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web-deploy.git
```


3. Run `git remote` again to see the changes:

```bash
git remote -v
```

You see that you still have both fetch (download) access and push (upload) access to your repository. You also now have fetch access to the Microsoft repository:

```
origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (fetch)
origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (push)
upstream        https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web-deploy.git (fetch)
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

## **Create the Azure App Service environments**

Here, you create the environments that define the pipeline stages. You create one App Service instance that corresponds to each stage: Dev, Test, and Staging.

In the **Create a multistage pipeline by using Azure Pipelines** module, you used the Azure CLI to create your App Service instances. Here you'll do the same.

> **Important**
> 
> You need your own Azure subscription to complete the exercises in this module.

### **Bring up Cloud Shell through the Azure portal**

1. Go to the [Azure portal](https://portal.azure.com) and sign in.
2. From the menu bar, select **Cloud Shell**. When you're prompted, select the **Bash** experience.

### **Select an Azure region**

Here, you specify the default region, or geographic location, where your Azure resources are to be created.

1. From Cloud Shell, run the following `az account list-locations` command to list the regions that are available from your Azure subscription.

```bash
az account list-locations \
  --query "[].{Name: name, DisplayName: displayName}" \
  --output table
```

2. From the **Name** column in the output, choose a region that's close to you. For example, choose **eastasia** or **westus2**.

3. Run `az configure` to set your default region. Replace `<REGION>` with the name of the region you chose.

```bash
az configure --defaults location=<REGION>
```

Here's an example that sets **westus2** as the default region:

```bash
az configure --defaults location=westus2
```

### **Create the App Service instances**

Here, you create the App Service instances for the three stages you'll deploy to: Dev, Test, and Staging.

> **Note**
> 
> For learning purposes, here, you use the default network settings. These settings make your site accessible from the internet. In practice, you could configure an Azure virtual network that places your website in a network that's not internet routable, and that's accessible only to you and your team. Later, when you're ready, you could reconfigure your network to make the website available to your users.

1. From Cloud Shell, generate a random number that makes your web app's domain name unique.

```bash
webappsuffix=$RANDOM
```

2. Run the following `az group create` command to create a resource group that's named **tailspin-space-game-rg**.

```bash
az group create --name tailspin-space-game-rg
```

3. Run the following `az appservice plan create` command to create an App Service plan that's named **tailspin-space-game-asp**.

```bash
az appservice plan create \
  --name tailspin-space-game-asp \
  --resource-group tailspin-space-game-rg \
  --sku B1 \
  --is-linux
```

The `--sku` argument specifies the **B1** plan, which runs on the **Basic** tier. The `--is-linux` argument specifies to use Linux workers.

> **Important**
> 
> If the B1 SKU isn't part of your Azure subscription, choose a different plan, such as S1 (Standard).

4. Run the following `az webapp create` commands to create the three App Service instances, one for each of the Dev, Test, and Staging environments.

```bash
az webapp create \
  --name tailspin-space-game-web-dev-$webappsuffix \
  --resource-group tailspin-space-game-rg \
  --plan tailspin-space-game-asp \
  --runtime "DOTNETCORE|8.0"

az webapp create \
  --name tailspin-space-game-web-test-$webappsuffix \
  --resource-group tailspin-space-game-rg \
  --plan tailspin-space-game-asp \
  --runtime "DOTNETCORE|8.0"

az webapp create \
  --name tailspin-space-game-web-staging-$webappsuffix \
  --resource-group tailspin-space-game-rg \
  --plan tailspin-space-game-asp \
  --runtime "DOTNETCORE|8.0"
```

For learning purposes, you apply the same App Service plan (B1 Basic) to each App Service instance here. In practice, you'd assign a plan that matches your expected workload.

5. Run the following `az webapp list` command to list the hostname and state of each App Service instance.

```bash
az webapp list \
  --resource-group tailspin-space-game-rg \
  --query "[].{hostName: defaultHostName, state: state}" \
  --output table
```

Note the hostname for each running service. You'll need these hostnames later when you verify your work. Here's an example:

```
HostName                                                 State
-------------------------------------------------------  -------
tailspin-space-game-web-dev-21017.azurewebsites.net      Running
tailspin-space-game-web-test-21017.azurewebsites.net     Running
tailspin-space-game-web-staging-21017.azurewebsites.net  Running
```

6. As an optional step, copy and paste one or more of the names into your browser to verify that they're running and that the default home page appears.

You should get a page similar to this one:

*The default home page on Azure App Service.*

> **Important**
> 
> The **Clean up your Azure DevOps environment** page in this module contains important cleanup steps. Cleaning up helps ensure that you're not charged for Azure resources after you complete this module. Be sure to perform the cleanup steps even if you don't complete this module.

## **Create pipeline variables in Azure Pipelines**

In the **Create a multistage pipeline by using Azure Pipelines**, you added one variable for each of the App Service instances, which correspond to the Dev, Test, and Staging stages in your pipeline. Here, you do the same.

Each stage in your pipeline configuration uses these variables to identify which App Service instance to deploy to.

To add the variables:

1. In Azure DevOps, go to your **Space Game - web - Functional tests** project.

2. Under **Pipelines**, select **Library**.

*A screenshot of Azure Pipelines, showing the Library menu option.*

![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/5-pipelines-library.png)

3. Select **+ Variable group**.

4. Under **Properties**, for the variable group name, enter **Release**.

5. Under **Variables**, select **+ Add**.

6. For the name of your variable, enter **WebAppNameDev**. For its value, enter the name of the App Service instance that corresponds to your Dev environment, such as **tailspin-space-game-web-dev-1234**.

7. Repeat steps 5 and 6 twice more to create variables for your Test and Staging environments, as shown in this table:

| Variable name | Example value |
|---------------|---------------|
| WebAppNameTest | tailspin-space-game-web-test-1234 |
| WebAppNameStaging | tailspin-space-game-web-staging-1234 |

Be sure to replace each example value with the App Service instance that corresponds to your environment.

> **Important**
> 
> Set the name of the App Service instance, not its host name. In this example, you would enter **tailspin-space-game-web-dev-1234** and not **tailspin-space-game-web-dev-1234.azurewebsites.net**.

8. Near the top of the page, select **Save** to save your variable to the pipeline.

Your variable group should resemble this one:

*A screenshot of Azure Pipelines, showing the variable group. The group contains three variables.*

![](https://learn.microsoft.com/en-us/training/azure-devops/run-functional-tests-azure-pipelines/media/3-library-variable-group.png)

## **Create the dev, test, and staging environments**

In **Create a multistage pipeline by using Azure Pipelines**, you created environments for the dev, test, and staging environments. Here, you repeat the process. This time, however, you omit additional criteria such as the requirement for human approval to promote changes from one stage to the next.

To create the dev, test, and staging environments:

1. From Azure Pipelines, select **Environments**.

*A screenshot of Azure Pipelines showing the location of the Environments menu option.*

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/pipelines-environments.png)

2. To create the dev environment:
   * Select **Create environment**.
   * Under **Name**, enter **dev**.
   * Leave the remaining fields at their default values.
   * Select **Create**.

3. To create the test environment:
   * Return to the **Environments** page.
   * Select **New environment**.
   * Under **Name**, enter **test**.
   * Select **Create**.

4. To create the staging environment:
   * Return to the **Environments** page.
   * Select **New environment**.
   * Under **Name**, enter **staging**.
   * Select **Create**.

## **Create a service connection**

Here, you create a service connection that enables Azure Pipelines to access your Azure subscription. Azure Pipelines uses this service connection to deploy the website to App Service. You created a similar service connection in the previous module.

> **Important**
> 
> Make sure that you're signed in to both the Azure portal and Azure DevOps under the same Microsoft account.

1. In Azure DevOps, go to your **Space Game - web - Functional tests** project.

2. From the bottom corner of the page, select **Project settings**.

3. Under **Pipelines**, select **Service connections**.

4. Select **Create service connection**, then choose **Azure Resource Manager**, then select **Next**.

5. Near the top of the page, **App registration (automatic)**.

6. Fill in these fields:

| Field | Value |
|-------|-------|
| **Scope level** | Subscription |
| **Subscription** | Your Azure subscription |
| **Resource Group** | tailspin-space-game-rg |
| **Service connection name** | Resource Manager - Tailspin - Space Game |

During the process, you might be prompted to sign in to your Microsoft account.

7. Ensure that **Grant access permission to all pipelines** is selected.

8. Select **Save**.

Azure DevOps performs a test connection to verify that it can connect to your Azure subscription. If Azure DevOps can't connect, you have the chance to sign in a second time.



# 3.4 Plan the UI tests

In this section, you follow along with Amita and Andy as they talk about how to incorporate Selenium UI tests into the release pipeline. They begin by walking through the tests that Amita normally does manually. Then they map Amita's manual steps to automated test cases.

## Run UI tests manually

Amita is waiting for Andy to show up. Andy is going to help Amita write a UI test that will be added to the Test stage of the pipeline. When he arrives, Andy sees Amita scribbling in her notebook, crossing out something, muttering, and then tearing out the page.

**Andy:** Hi. You don't look happy.

**Amita:** I'm not happy. I'm trying to figure out how to write an automated test, but I don't know where to start. I don't code. I feel like I'm obsolete.

**Andy:** Wow, I don't think it's that bad. For one thing, we'll always need someone who has the user's perspective in mind. There's no way to automate that. For another, no one starts out knowing how to automate tests. We were all beginners at some point. Hopefully, I can make the learning process a bit easier.

I think the best way to start is to automate something you regularly do manually. Pick a UI test. Then let's walk through it and write down the steps. Next we'll figure out how to automate those steps. What test should we pick?

Amita takes a deep breath.

**Amita:** Let's automate the modal window tests. When I select certain things, like the Download game button for example, I want to verify that the correct modal window appears. Then when I click away from the modal window, I want to verify that the modal window disappears and that the main window is active again.

**Andy:** That sounds like a great place to start. You run the test. I'll write down the procedure.

Amita opens a Windows laptop and launches Google Chrome. She goes to the web app and verifies that the home page opens.

> **Tip**
> 
> If you want to follow along with Amita's manual tests, you can run a local copy of the Space Game website. In the Visual Studio Code terminal run the following commands, then select the link that looks like Now listening on: http://localhost:5000.
> 
> ```
> git fetch upstream selenium
> git checkout -B selenium upstream/selenium
> dotnet build --configuration Release
> dotnet run --configuration Release --no-build --project Tailspin.SpaceGame.Web
> ```

**Andy:** OK. What do you check next?

**Amita:** I check that when I select the Download game button, the correct modal window appears.

Amita selects the Download game button. The modal window appears.

*Screenshot of a browser showing the Download game modal window on the Space Game website.*

![](https://learn.microsoft.com/en-us/training/azure-devops/run-functional-tests-azure-pipelines/media/4-website-download-game-modal.png)

**Andy:** Great. What modal windows do you check next?

**Amita:** Next I check the four game screens. After that, I select the top player on the leaderboard. I verify that the player's profile appears.

Amita selects each of the four thumbnail images to show the example game screens.

*Screenshot of a browser showing the game screen modal window on the Space Game website.*

![](https://learn.microsoft.com/en-us/training/azure-devops/run-functional-tests-azure-pipelines/media/4-website-game-screens.png)

Next Amita selects the top player on the leaderboard. The player's profile appears.

*Screenshot of a browser showing the leaderboard modal window on the Space Game website.*

![](https://learn.microsoft.com/en-us/training/azure-devops/run-functional-tests-azure-pipelines/media/4-website-leaderboard.png)

**Amita:** That covers the modal window tests. I run these tests on Windows because that's what most players use to visit our site. I run the tests on Chrome, and when I have time I also run them on Firefox and Microsoft Edge.

If I had time, I would run all the tests again on macOS and Linux, just to ensure we're compatible with any operating system that the players use to visit the site. But I need to run many other tests.

## What are locators in Selenium?

In a Selenium test, a locator selects an HTML element from the DOM (Document Object Model) to act on. Think of the DOM as a tree or graph representation of an HTML document. Each node in the DOM represents a part of the document.

In a Selenium test, you can locate an HTML element by its:

- **id** attribute.
- **name** attribute.
- **XPath** expression.
- **Link text** or partial link text.
- **Tag name**, such as body or h1.
- **CSS class name**.
- **CSS selector**.

The locator you use depends on the way your HTML code is written and the kinds of queries you want to perform.

In an HTML document, the **id** attribute specifies a unique identifier for an HTML element. Here, you'll use the **id** attribute to query for elements on the page because each identifier must be unique. This makes the **id** attribute one of the easiest ways to query for elements in a Selenium test.

## Get the ID for each HTML element

Here, you follow along with Amita and Andy as they collect the ID for each button that Amita selects and for each resulting modal window.

**Andy:** I can see why these tests take so long and can be so frustrating. You're going to love automating them. I promise.

Here's what we'll do. We'll get the **id** attribute for each button you select and for the modal window that appears. The automated tests that we write can use these expressions to know which buttons to select and which modal windows to expect.

Let's start by getting the **id** attribute for the Download game button.

> **Note**
> 
> You can follow these steps if you want to, or just read along. The next section provides all of the **id** attributes that you need when you run the automated tests.

1. In Google Chrome, go to the Space Game home page.

2. Right-click the **Download game** button, then select **Inspect**.

3. The developer tools window opens. The HTML code for the **Download game** button is highlighted.

4. Examine the highlighted code and note the **id** attribute. Copy the id for later.

*Screenshot of a browser showing the developer tools window and a selected HTML element.*

![](https://learn.microsoft.com/en-us/training/azure-devops/run-functional-tests-azure-pipelines/media/4-website-inspect-button.png)


5. Select the **Download game** button. Then repeat steps 2 and 3 to get the **id** attribute for the modal window that appears.

6. Repeat the process for the four game screens and the top player on the leaderboard.

Amita opens Microsoft Word and adds a table. The table contains the **id** attribute for each link and the **id** attribute for the corresponding modal window. To keep the table basic, Amita records:

- The Download game button.
- Just one of the game screens.
- The top player on the leaderboard.

Here's what Amita's table looks like:

| Feature | Link id | Modal id |
|---------|---------|----------|
| Download game button | download-btn | pretend-modal |
| First game screen | screen-01 | screen-modal |
| Top leaderboard player | profile-1 | profile-modal-1 |

## Plan the automated tests

**Amita:** OK. We have the **id** attribute for each button I select. We also have the resulting modal window. What's next?

**Andy:** I think we're ready to write our tests. Here's what we'll do:

1. Create an NUnit project that includes Selenium. The project will be stored in the directory along with the app's source code.
2. Write a test case that uses automation to select the specified link. The test case verifies that the expected modal window appears.
3. Use the **id** attribute we saved to specify the parameters to the test case method. This task creates a sequence, or series, of tests.
4. Configure the tests to run on Chrome, Firefox, and Microsoft Edge. This task creates a matrix of tests.
5. Run the tests and watch each web browser come up automatically.
6. Watch Selenium automatically run through the series of tests for each browser.
7. In the console window, verify that all the tests pass.

**Amita:** I'll be excited to see how quickly the tests run. Can we try the tests now?

**Andy:** Absolutely. Let's move over to my laptop. I have the app code ready.

---




# 3.5 Write the UI tests


In this section, you help Andy and Amita write Selenium tests that verify the UI behaviors that Amita described.

Amita normally runs tests on Chrome, Firefox, and Microsoft Edge. Here, you do the same. The Microsoft-hosted agent that you use is preconfigured to work with each of these browsers.

## Fetch the branch from GitHub

In this section, you fetch the selenium branch from GitHub. You then check out, or switch to, that branch. The contents of the branch will help you follow along with the tests that Andy and Amita write.

This branch contains the Space Game project that you worked with in previous modules. It also contains an Azure Pipelines configuration to start with.

1. In Visual Studio Code, open the integrated terminal.

2. To download a branch named selenium from the Microsoft repository, switch to that branch, and run the following git fetch and git checkout commands:


   ```Bash
   git fetch upstream selenium
   git checkout -B selenium upstream/selenium
   ```

   > **Tip**
   > 
   > If you followed along with Amita's manual test in the previous unit, you may have run these commands already. If you already ran them in the previous unit, you can still run them again now.

   Recall that upstream refers to the Microsoft GitHub repository. Your project's Git configuration understands the upstream remote because you set up that relationship. You set it up when you forked the project from the Microsoft repository and cloned it locally.

   Shortly, you'll push this branch up to your GitHub repository, known as origin.

3. Optionally, in Visual Studio Code, open the azure-pipelines.yml file. Familiarize yourself with the initial configuration.

   The configuration resembles the ones that you created in the previous modules in this learning path. It builds only the application's Release configuration. For brevity, it also omits the triggers, manual approvals, and tests that you set up in previous modules.

   > **Note**
   > 
   > A more robust configuration might specify the branches that participate in the build process. For example, to help verify code quality, you might run unit tests each time you push up a change on any branch. You might also deploy the application to an environment that performs more exhaustive testing. But you do this deployment only when you have a pull request, when you have a release candidate, or when you merge code to main.
   > 
   > For more information, see Implement a code workflow in your build pipeline by using Git and GitHub and Build pipeline triggers.

## Write the unit test code

Amita is excited to learn to write code that controls the web browser.

She and Andy work together to write the Selenium tests. Andy has already set up an empty NUnit project. Throughout the process, they refer to the Selenium documentation, a few online tutorials, and the notes that they took when Amita did the tests manually. At the end of this module, you'll find more resources to help get you through the process.

Let's review the process that Andy and Amita use to write their tests. You can follow along by opening HomePageTest.cs in the Tailspin.SpaceGame.Web.UITests directory in Visual Studio Code.

### Define the HomePageTest class

**Andy:** The first thing we need to do is define our test class. We can choose to follow one of several naming conventions. Let's call our class HomePageTest. In this class, we'll put all of our tests that relate to the home page.

Andy adds this code to HomePageTest.cs:

```cs
public class HomePageTest
{
}
```

**Andy:** We need to mark this class as public so that it's available to the NUnit framework.

### Add the IWebDriver member variable

**Andy:** Next, we need an IWebDriver member variable. IWebDriver is the programming interface that you use to launch a web browser and interact with webpage content.

**Amita:** I've heard of interfaces in programming. Can you tell me more?

**Andy:** Think of an interface as a specification or blueprint for how a component should behave. An interface provides the methods, or behaviors, of that component. But the interface doesn't provide any of the underlying details. You or someone else would create one or more concrete classes that implement that interface. Selenium provides the concrete classes that we need.

This diagram shows the IWebDriver interface and a few of the classes that implement this interface:

![](https://learn.microsoft.com/en-us/training/azure-devops/run-functional-tests-azure-pipelines/media/5-selenium-webdriver.png)


The diagram shows three of the methods that IWebDriver provides: Navigate, FindElement, and Close.

The three classes shown here—ChromeDriver, FirefoxDriver, and EdgeDriver—each implement IWebDriver and its methods. There are other classes, such as SafariDriver, that also implement IWebDriver. Each driver class can control the web browser that it represents.

Andy adds a member variable named driver to the HomePageTest class, like this code:

```cs
public class HomePageTest
{
    private IWebDriver driver;
}
```

### Define the test fixtures

**Andy:** We want to run the entire set of tests on Chrome, Firefox, and Edge. In NUnit, we can use test fixtures to run the entire set of tests multiple times, one time for each browser that we want to test on.

In NUnit, you use the TestFixture attribute to define your test fixtures. Andy adds these three test fixtures to the HomePageTest class:

```cs
[TestFixture("Chrome")]
[TestFixture("Firefox")]
[TestFixture("Edge")]
public class HomePageTest
{
    private IWebDriver driver;
}
```

**Andy:** Next, we need to define a constructor for our test class. The constructor is called when NUnit creates an instance of this class. As its argument, the constructor takes the string that we attached to our test fixtures. Here's what the code looks like:

```cs
[TestFixture("Chrome")]
[TestFixture("Firefox")]
[TestFixture("Edge")]
public class HomePageTest
{
    private string browser;
    private IWebDriver driver;

    public HomePageTest(string browser)
    {
        this.browser = browser;
    }
}
```

**Andy:** We added the browser member variable so that we can use the current browser name in our setup code. Let's write the setup code next.

### Define the Setup method

**Andy:** Next, we need to assign our IWebDriver member variable to a class instance that implements this interface for the browser we're testing on. The ChromeDriver, FirefoxDriver, and EdgeDriver classes implement this interface for Chrome, Firefox, and Edge, respectively.

Let's create a method named Setup that sets the driver variable. We use the OneTimeSetUp attribute to tell NUnit to run this method one time per test fixture.

```cs
[OneTimeSetUp]
public void Setup()
{
}
```

In the Setup method, we can use a switch statement to assign the driver member variable to the appropriate concrete implementation based on the browser name. Let's add that code now.

```cs
// Create the driver for the current browser.
switch(browser)
{
    case "Chrome":
    driver = new ChromeDriver(
        Environment.GetEnvironmentVariable("ChromeWebDriver")
    );
    break;
    case "Firefox":
    driver = new FirefoxDriver(
        Environment.GetEnvironmentVariable("GeckoWebDriver")
    );
    break;
    case "Edge":
    driver = new EdgeDriver(
        Environment.GetEnvironmentVariable("EdgeWebDriver"),
        new EdgeOptions
        {
            UseChromium = true
        }
    );
    break;
    default:
    throw new ArgumentException($"'{browser}': Unknown browser");
}
```

The constructor for each driver class takes an optional path to the driver software Selenium needs to control the web browser. Later, we'll discuss the role of the environment variables shown here.

In this example, the EdgeDriver constructor also requires additional options to specify that we want to use the Chromium version of Edge.

### Define the helper methods

**Andy:** I know we'll need to repeat two actions throughout the tests:

- Finding elements on the page, such as the links that we click and the modal windows that we expect to appear
- Clicking elements on the page, such as the links that reveal the modal windows and the button that closes each modal

Let's write two helper methods, one for each action. We'll start with the method that finds an element on the page.

#### Write the FindElement helper method

When you locate an element on the page, it's typically in response to some other event, such as the page loading or the user entering information. Selenium provides the WebDriverWait class, which allows you to wait for a condition to be true. If the condition isn't true within the given time period, WebDriverWait throws an exception or error. We can use the WebDriverWait class to wait for a given element to be displayed and to be ready to receive user input.

To locate an element on the page, use the By class. The By class provides methods that let you find an element by its name, by its CSS class name, by its HTML tag, or in our case, by its id attribute.

Andy and Amita code up the FindElement helper method. It looks like this code:

```cs
private IWebElement FindElement(By locator, IWebElement parent = null, int timeoutSeconds = 10)
{
    // WebDriverWait enables us to wait for the specified condition to be true
    // within a given time period.
    return new WebDriverWait(driver, TimeSpan.FromSeconds(timeoutSeconds))
        .Until(c => {
            IWebElement element = null;
            // If a parent was provided, find its child element.
            if (parent != null)
            {
                element = parent.FindElement(locator);
            }
            // Otherwise, locate the element from the root of the DOM.
            else
            {
                element = driver.FindElement(locator);
            }
            // Return true after the element is displayed and is able to receive user input.
            return (element != null && element.Displayed && element.Enabled) ? element : null;
        });
}
```

#### Write the ClickElement helper method

**Andy:** Next, let's write a helper method that clicks links. Selenium provides a few ways to write that method. One of them is the IJavaScriptExecutor interface. With it, we can programmatically click links by using JavaScript. This approach works well because it can click links without first scrolling them into view.

ChromeDriver, FirefoxDriver, and EdgeDriver each implement IJavaScriptExecutor. We need to cast the driver to this interface and then call ExecuteScript to run the JavaScript click() method on the underlying HTML object.

Andy and Amita code up the ClickElement helper method. It looks like this code:

```cs
private void ClickElement(IWebElement element)
{
    // We expect the driver to implement IJavaScriptExecutor.
    // IJavaScriptExecutor enables us to execute JavaScript code during the tests.
    IJavaScriptExecutor js = driver as IJavaScriptExecutor;

    // Through JavaScript, run the click() method on the underlying HTML object.
    js.ExecuteScript("arguments[0].click();", element);
}
```

**Amita:** I like the idea of adding these helper methods. They seem general enough to use in almost any test. We can add more helper methods later as we need them.

### Define the test method

**Andy:** Now, we're ready to define the test method. Based on the manual tests that we ran earlier, let's call this method ClickLinkById_ShouldDisplayModalById. It's a good practice to give test methods descriptive names that define precisely what the test accomplishes. Here, we want to select a link defined by its id attribute. Then we want to verify that the proper modal window appears, also by using its id attribute.

Andy adds starter code for the test method:

```cs
public void ClickLinkById_ShouldDisplayModalById(string linkId, string modalId)
{
}
```

**Andy:** Before we add more code, let's define what this test should do.

**Amita:** I can handle this part. We want to:

1. Locate the link by its id attribute and select the link.
2. Locate the resulting modal.
3. Close the modal.
4. Verify that the modal was displayed successfully.

**Andy:** Great. We'll also need to handle a few other things. For example, we need to ignore the test if the driver couldn't be loaded, and we need to close the modal only if the modal was successfully displayed.

After refilling their coffee mugs, Andy and Amita add code to their test method. They use the helper methods that they wrote to locate page elements and click links and buttons. Here's the result:

```cs
public void ClickLinkById_ShouldDisplayModalById(string linkId, string modalId)
{
    // Skip the test if the driver could not be loaded.
    // This happens when the underlying browser is not installed.
    if (driver == null)
    {
        Assert.Ignore();
        return;
    }

    // Locate the link by its ID and then click the link.
    ClickElement(FindElement(By.Id(linkId)));

    // Locate the resulting modal.
    IWebElement modal = FindElement(By.Id(modalId));

    // Record whether the modal was successfully displayed.
    bool modalWasDisplayed = (modal != null && modal.Displayed);

    // Close the modal if it was displayed.
    if (modalWasDisplayed)
    {
        // Click the close button that's part of the modal.
        ClickElement(FindElement(By.ClassName("close"), modal));

        // Wait for the modal to close and for the main page to again be clickable.
        FindElement(By.TagName("body"));
    }

    // Assert that the modal was displayed successfully.
    // If it wasn't, this test will be recorded as failed.
    Assert.That(modalWasDisplayed, Is.True);
}
```

**Amita:** The coding looks great so far, but how do we connect this test to the id attributes that we collected earlier?

**Andy:** Great question. We'll handle that next.

### Define test case data

**Andy:** In NUnit, you can provide data to your tests in a few ways. Here, we use the TestCase attribute. This attribute takes arguments that it later passes back to the test method when it runs. We can have multiple TestCase attributes that each test a different feature of our app. Each TestCase attribute produces a test case that's included in the report that appears at the end of a pipeline run.

Andy adds these TestCase attributes to the test method. These attributes describe the Download game button, one of the game screens, and the top player on the leaderboard. Each attribute specifies two id attributes: one for the link to select and one for the corresponding modal window.

```cs
// Download game
[TestCase("download-btn", "pretend-modal")]
// Screen image
[TestCase("screen-01", "screen-modal")]
// // Top player on the leaderboard
[TestCase("profile-1", "profile-modal-1")]
public void ClickLinkById_ShouldDisplayModalById(string linkId, string modalId)
{

...
```

**Andy:** For each TestCase attribute, the first parameter is the id attribute for the link to select. The second parameter is the id attribute for the modal window that we expect to appear. You can see how these parameters correspond to the two-string arguments in our test method.

**Amita:** I do see that. With some practice, I think I can add my own tests. When can we see these tests running in our pipeline?

**Andy:** Before we push changes through the pipeline, let's first verify that the code compiles and runs locally. We'll commit and push changes to GitHub and see them move through the pipeline only after we verify that everything works. Let's run the tests locally now.



# 3.6 Exercise - Run the UI tests locally and in the pipeline

Before Andy and Amita run their tests in the pipeline, they want to verify that their new UI tests do what they should. In this section, you'll follow along by running the Selenium UI tests first locally and then in the pipeline.

Writing automated tests is an iterative process, just like writing any other type of code. For your own apps, you'll likely need to try a few approaches, refer to reference documentation and example code, and fix build errors.

## Optional: Install the Selenium driver for Microsoft Edge

Follow this section if you want to see the tests run locally on Microsoft Edge.

The NuGet package for Chrome and Firefox installs driver software under the bin directory, alongside the compiled test code. For Edge, you need to manually install the driver. To do so:

1. Install Microsoft Edge.

2. Open Edge and navigate to **edge://settings/help**. Note the version number. Here's an example:

![](https://learn.microsoft.com/en-us/training/azure-devops/run-functional-tests-azure-pipelines/media/6-edge-version.png)

3. Navigate to the Microsoft Edge Driver downloads page and download the driver that matches the Edge version number. Here's an example:

![](https://learn.microsoft.com/en-us/training/azure-devops/run-functional-tests-azure-pipelines/media/6-edge-driver-install.png)

4. Extract the .zip file to the **bin/Release/net6.0** directory under your project's **Tailspin.SpaceGame.Web.UITests** directory. Create these directories if they don't exist.

5. On macOS, you might need to update your system policy to allow **msedgedriver** to run. To do so, in Visual Studio Code, run the following **spctl** command from the terminal:

 
   ```Bash
   spctl --add Tailspin.SpaceGame.Web.UITests/bin/Release/net6.0/msedgedriver
   ```

## Export environment variables

Later in this module, you'll run Selenium tests on Windows Server 2019. The documentation lists the software that's preinstalled for you.

The section **Selenium Web Drivers** lists the Selenium driver versions that are available for Chrome, Firefox, and Edge. Here's an example:

![](https://learn.microsoft.com/en-us/training/azure-devops/run-functional-tests-azure-pipelines/media/6-readme-selenium-drivers.png)

For each driver, you have the environment variable that maps to the location of that driver. For example, **ChromeWebDriver** maps to the location of the Chrome driver.

The unit tests code is already set up to read these environment variables. These variables tell Selenium where to find the driver executable files. To run the unit tests locally, you need to export these same environment variables.

From Visual Studio Code, go to the terminal. Then run these commands. Replace the path shown with the full path to your **mslearn-tailspin-spacegame-web-deploy** project.

> **Important**
> 
> Make sure to run these commands and set the environment variables in the same terminal window that you use to run the tests.

**Windows**  
**macOS**

```Bash
driverDir="C:\Users\user\mslearn-tailspin-spacegame-web-deploy\Tailspin.SpaceGame.Web.UITests\bin\Release\net6.0"
```


```Bash
export ChromeWebDriver=$driverDir
export EdgeWebDriver=$driverDir
export GeckoWebDriver=$driverDir
```

## Run the UI tests locally

The Setup method in **HomePageTest.cs** navigates to the Space Game home page after it sets the driver member variable.

Although you could hard-code the site URL, here we read the URL from an environment variable named **SITE_URL**. This way, you can run the tests multiple times against different URLs.

```cs
// Navigate to the site.
// The site name is stored in the SITE_URL environment variable to make 
// the tests more flexible.
string url = Environment.GetEnvironmentVariable("SITE_URL");
driver.Navigate().GoToUrl(url + "/");
```

Because you haven't yet deployed the Space Game website to your App Service environment, you'll use the site that Microsoft hosts to run the tests locally.

To run the tests locally:

1. In Visual Studio Code, go to the integrated terminal and open a new terminal window.

2. Run the following commands in the new terminal window.

   **.NET CLI**
   ```
   dotnet build --configuration Release
   dotnet run --configuration Release --no-build --project Tailspin.SpaceGame.Web
   ```

3. Make a note of the local website link; in this example, it's **http://localhost:5000**.

4. Switch back to the terminal window where you set the environment variables in the previous step, and ensure that you're in your project's root directory. Here's an example:


   ```Bash
   cd ~/mslearn-tailspin-spacegame-web-deploy
   ```

5. Export the **SITE_URL** environment variable. Use the locally running link that you got from the previous step.


   ```Bash
   export SITE_URL="http://localhost:5000"
   ```

   This variable points to the Space Game website that Microsoft hosts.

6. Run the UI tests.


   ```Bash
   dotnet test --configuration Release Tailspin.SpaceGame.Web.UITests
   ```

   This code runs the tests that are located in the **Tailspin.SpaceGame.Web.UITests** project.

   As the tests run, one or more browsers appear. Selenium controls each browser and follows the test steps that you defined.

   > **Note**
   > 
   > Don't worry if all three browsers don't appear. For example, you won't see the tests run on Chrome if you don't have Chrome installed or have an incompatible version. Seeing just one browser will help give you confidence that your tests are working. In practice, in your local development environment, you might want to set up all browsers that you want to test against. This setup will allow you to verify that your tests behave as expected in each configuration before you run your tests in the pipeline.

7. From the terminal, trace the output of each test. Also note the test-run summary at the end.

   This example shows that out of nine tests, all nine tests succeeded and zero tests were skipped:

   **Output**
   ```
   Passed!  - Failed:     0, Passed:     9, Skipped:     0, Total:     9, Duration: 5 s 
   ```

## Add the SITE_URL variable to Azure Pipelines

Earlier, you set the **SITE_URL** environment variable locally so that your tests know where to point each browser. You can add this variable to Azure Pipelines. The process is similar to how you added variables for your App Service instances. When the agent runs, this variable is automatically exported to the agent as an environment variable.

Let's add the pipeline variable now, before you update your pipeline configuration. To do so:

1. In Azure DevOps, go to your **Space Game - web - Functional tests** project.

2. Under **Pipelines**, select **Library**.

3. Select the **Release** variable group.

4. Under **Variables**, select **+ Add**.

5. For the name of your variable, enter **SITE_URL**. As its value, enter the URL of the App Service instance that corresponds to your test environment, such as **http://tailspin-space-game-web-test-10529.azurewebsites.net**.

6. Near the top of the page, select **Save** to save your variable to the pipeline.

Your variable group should resemble this one:

![](https://learn.microsoft.com/en-us/training/azure-devops/run-functional-tests-azure-pipelines/media/6-library-variable-group.png)

## Modify the pipeline configuration

In this section, you modify the pipeline configuration to run your Selenium UI tests during the Test stage.

In Visual Studio Code, open the **azure-pipelines.yml** file. Then modify the file like this:

> **Tip**
> 
> This file contains a few changes, so we recommend that you replace the entire file with what you see here.

```yml
trigger:
- '*'

variables:
  buildConfiguration: 'Release'
  dotnetSdkVersion: '8.x'

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
      dotnetSdkVersion: '8.x'

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
        projects: '$(System.DefaultWorkingDirectory)/**/Tailspin.SpaceGame.Web.csproj' 
        publishWebProjects: false
        arguments: '--no-build --configuration $(buildConfiguration) --output $(Build.ArtifactStagingDirectory)/$(buildConfiguration)'
        zipAfterPublish: true

    - publish: '$(Build.ArtifactStagingDirectory)'
      artifact: drop

- stage: 'Dev'
  displayName: 'Deploy to the dev environment'
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
              appName: '$(WebAppNameDev)'
              package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/*.zip'

- stage: 'Test'
  displayName: 'Deploy to the test environment'
  dependsOn: Dev
  jobs:
  - deployment: Deploy
    pool:
      vmImage: 'ubuntu-20.04'
    environment: test
    variables:
    - group: 'Release'
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
              appName: '$(WebAppNameTest)'
              package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/*.zip'
  - job: RunUITests
    dependsOn: Deploy
    displayName: 'Run UI tests'
    pool:
      vmImage: 'windows-2019'
    variables:
    - group: 'Release'
    steps: 
    - task: UseDotNet@2
      displayName: 'Use .NET SDK $(dotnetSdkVersion)'
      inputs:
        version: '$(dotnetSdkVersion)'
    - task: DotNetCoreCLI@2
      displayName: 'Build the project - $(buildConfiguration)'
      inputs:
        command: 'build'
        arguments: '--configuration $(buildConfiguration)'
        projects: '$(System.DefaultWorkingDirectory)/**/*UITests.csproj'
    - task: DotNetCoreCLI@2
      displayName: 'Run unit tests - $(buildConfiguration)'
      inputs:
        command: 'test'
        arguments: '--no-build --configuration $(buildConfiguration)'
        publishTestResults: true
        projects: '$(System.DefaultWorkingDirectory)/**/*UITests.csproj'

- stage: 'Staging'
  displayName: 'Deploy to the staging environment'
  dependsOn: Test
  jobs:
  - deployment: Deploy
    pool:
      vmImage: 'ubuntu-20.04'
    environment: staging
    variables:
    - group: 'Release'
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
              appName: '$(WebAppNameStaging)'
              package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/*.zip'
```

The file includes these three changes:

1. The **dotnetSdkVersion** variable is moved to the top of the file so that multiple stages can access it. Here the Build stage and Test stage require this version of .NET Core.

2. The Build stage publishes only the Space Game website package as the build artifact. Previously, you published the artifacts like this:

   ```yml
   - task: DotNetCoreCLI@2
     displayName: 'Publish the project - $(buildConfiguration)'
     inputs:
       command: 'publish'
       projects: '**/*.csproj'
       publishWebProjects: false
       arguments: '--no-build --configuration $(buildConfiguration) --output $(Build.ArtifactStagingDirectory)/$(buildConfiguration)'
       zipAfterPublish: true
   ```

   This task generates two build artifacts: the Space Game website package and the compiled UI tests. We build the UI tests during the Build stage to ensure that they'll compile during the Test stage, but we don't need to publish the compiled test code. We build it again during the Test stage when the tests run.

3. The Test stage includes a second job that builds and runs the tests. This job resembles the one that you used in the **Run quality tests in your build pipeline by using Azure Pipelines** module. In that module, you ran NUnit tests that verified the leaderboard's filtering functionality.

Recall that a deployment job is a special type of job that plays an important role in your deployment stages. The second job is a normal job that runs the Selenium tests on a Windows Server 2019 agent. Although we use a Linux agent to build the application, here we use a Windows agent to run the UI tests. We use a Windows agent because Amita runs manual tests on Windows, and that's what most customers use.

The **RunUITests** job depends on the **Deploy** job to ensure that the jobs run in the correct order. You'll deploy the website to App Service before you run the UI tests. If you don't specify this dependency, jobs within the stage can run in any order or run in parallel.

In the integrated terminal, add **azure-pipelines.yml** to the index, commit the changes, and push the branch up to GitHub.

**Bash**
```
git add azure-pipelines.yml
git commit -m "Run Selenium UI tests"
git push origin selenium
```

## Watch Azure Pipelines run the tests

Here, you watch the pipeline run. The pipeline runs the Selenium UI tests during the Test stage.

1. In Azure Pipelines, go to the build and trace it as it runs.

   During the build, you see the automated tests run after the website is deployed.

  ![](https://learn.microsoft.com/en-us/training/azure-devops/run-functional-tests-azure-pipelines/media/6-stages-test-running.png)

3. After the build finishes, go to the summary page.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/run-functional-tests-azure-pipelines/media/6-stages-complete.png)

   You note that the deployment and the UI tests finished successfully.

5. Near the top of the page, note the summary.

   You note that the build artifact for the Space Game website is published just like always. Also note the **Tests and coverage** section, which shows that the Selenium tests have passed.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-pipelines-build-summary-tests.png)

7. Select the test summary to see the full report.

   The report shows that all nine tests have passed. These tests include three tests across three browsers.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/run-functional-tests-azure-pipelines/media/6-test-summary.png)

If any test fails, you get detailed results of the failure. From there, you can investigate the source of the failure, fix it locally, and then push up the necessary changes to make the tests pass in the pipeline.

**Amita:** This automation is exciting! I now have UI tests that I can run in the pipeline. The tests will really save us time in the long run. I also have a pattern to follow to add more tests. Best of all, the UI tests give us added confidence in our code quality.

**Andy:** All true. Remember, tests that you repeatedly run manually are good candidates for automation. Good luck adding more. If you get stuck or need a code reviewer, you know where to find me.



# 3.7 Exercise - Clean up your Azure DevOps environment

You're done with the tasks for this module. Here, you'll clean up your Azure resources, move the work item to the Done state in Azure Boards, and clean up your Azure DevOps environment.

> **Important**
> 
> This page contains important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes. It also helps ensure that you're not charged for Azure resources after you complete this module.

## Clean up Azure resources

Here you delete your Azure App Service instances. The easiest way to delete the instances is to delete their parent resource group. Deleting a resource group deletes all resources in that group.

To clean up your resource group:

1. Go to the Azure portal and sign in.

2. From the menu, select **Cloud Shell**. When you're prompted, select the **Bash** experience.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-portal-menu-cloud-shell.png)

4. Run the following **az group delete** command. The command deletes the resource group that you used in this module, **tailspin-space-game-rg**.

   **Azure CLI**
   ```
   az group delete --name tailspin-space-game-rg
   ```

5. When you're prompted, enter **y** to confirm the operation.

6. As an optional step, run the following **az group list** command after the previous command finishes.

   **Azure CLI**
   ```
   az group list --output table
   ```

   You find that the resource group **tailspin-space-game-rg** no longer exists.

## Move the work item to Done

Here, you'll finish the work item that you assigned to yourself earlier in this module. You'll move **Automate quality tests** to the **Done** column.

In practice, **done** often means putting working software into the hands of your users. For learning purposes, here you'll mark this work as complete because you set up working UI tests in your pipeline.

At the end of each sprint, or work iteration, your team might want to hold a retrospective meeting. In the meeting, you share the work you completed, what went well in the sprint, and what you could improve.

To complete the work item:

1. In Azure DevOps, go to **Boards**, and then select **Boards** from the menu.

2. Move the **Automate quality tests** work item from the **Doing** column to the **Done** column.


   ![](https://learn.microsoft.com/en-us/training/azure-devops/run-functional-tests-azure-pipelines/media/7-azure-boards-wi3-done.png)

## Disable the pipeline or delete your project

Each module in this learning path provides a template. You can run the template to create a clean environment for the duration of the module.

Running multiple templates gives you multiple Azure Pipelines projects, each pointing to the same GitHub repository. This setup can trigger multiple pipelines to run each time you push a change to your GitHub repository. These runs can consume free build minutes on our hosted agents, so it's important to disable or delete your pipeline before you continue to the next module.

Choose one of the following options.

### Option 1: Disable the pipeline

This option disables the pipeline so that it doesn't process further build requests. You can reenable the build pipeline later if you want to. Choose this option if you want to keep your DevOps project and your build pipeline for future reference.

To disable the pipeline:

1. In Azure Pipelines, navigate to your pipeline.

2. From the drop-down menu, select **Settings**:

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-pipelines-settings-button.png)

4. Under **Processing of new run requests**, select **Disabled**, then select **Save**.

Your pipeline will no longer process build requests.

### Option 2: Delete the Azure DevOps project

This option deletes your Azure DevOps project, including the content on Azure Boards and in your build pipeline. In future modules, you can run another template that brings up a new project in a state where this template leaves off. Choose this option if you don't need your DevOps project for future reference.

To delete the project:

1. In Azure DevOps, go to your project. Earlier, we recommended that you name this project **Space Game - web - Functional tests**.

2. Select **Project settings** in the lower corner.

3. At the bottom of the **Project details** area, select **Delete**.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-delete-project.png)

5. In the window that appears, enter the project name, then select **Delete** again.

Your project is now deleted.



# 3.8 Summary

Great work! In this module, we defined a *functional test* as a test that verifies that a given function of the software does what it should. We also defined some popular kinds of functional tests, including smoke tests, unit tests, and UI tests.

The Tailspin team chose one type of functional test to automate first: UI tests. Amita had been running these tests manually. The manual tests were tedious and time-consuming. By automating the tests, Amita can now focus more on usability testing, which is usually best done by humans.

When you incorporate functional tests in your pipeline, focus on the kinds of tests that matter most. For example, if your application distributes work among various components, you can write integration tests that verify that all components work together to form a complete system.

In the next module, you'll switch to another type of important testing: *nonfunctional testing*. The team will define nonfunctional testing and focus on one type of performance test.

## Learn more

Use the following resources to learn more.

### Learn more about NUnit

In this module, you worked with NUnit tests. If you're interested in unit-testing .NET applications, consider these additional resources:

- NUnit.org
- Unit test tools and tasks
- Unit testing C# with NUnit and .NET Core

### Learn about parallel jobs

You have set up UI tests that run on Windows. But you can also run your tests on other platforms, such as macOS and Linux. To speed up the testing process, you can run all of these jobs in parallel. For more information, see Jobs and Parallel jobs.

### Learn more about Selenium tests

If you're interested in testing UI by using Selenium, check out these resources to help you go further:

- SeleniumHQ.org
- Selenium IDE
- UI test with Selenium
- UI testing considerations
- Use WebDriver to automate Microsoft Edge

### Improve code quality by using Azure Test Plans

Now that you're familiar with automated tests, let's talk about Azure Test Plans, which provides all the tools you need to test your applications. You can create and run manual test plans, generate automated tests, and collect feedback from users.

### Manage test plans, test suites, and test cases

Azure Test Plans provides three main types of test-management artifacts: test plans, test suites, and test cases.

- **Test plans** group together test suites and individual test cases. Test plans include static test suites, requirement-based suites, and query-based suites.
- **Test suites** group test cases into separate testing scenarios within a single test plan. By grouping test cases, you can better see which scenarios are complete.
- **Test cases** validate individual parts of your code or app deployment. You can ensure your code works correctly, has no errors, and meets business and customer requirements.

### Use the Test & Feedback extension

The Test & Feedback extension enables exploratory testing techniques in Azure Test Plans. With it, you can:

- Capture your findings along with rich diagnostic data. This data includes comments, screenshots with annotations, and audio or video recordings that describe your findings and highlight issues. In the background, the extension captures additional information such as user actions. The extension uses the image action log, page load data, and system information about the browser, operating system, and more. This information later helps you debug or reproduce the issue.
- Create work items such as bugs, tasks, and test cases from within the extension. The captured information automatically becomes part of the filed work item and helps with end-to-end traceability.
- Collaborate with your team by sharing your findings. Export your session report or connect to Azure Test Plans for a fully integrated experience.



# 4 Run nonfunctional tests in Azure Pipelines

Run automated load tests by using Apache JMeter, a form of nonfunctional testing, in Azure Pipelines.

### Learning objectives
After completing this module, you'll be able to:
- Define the role of nonfunctional tests and explain how they compare to functional tests.
- Identify some popular kinds of nonfunctional tests you can run.
- Run automated load tests in the pipeline by using Apache JMeter.
- Convert test results to a format that Azure Pipelines can visualize for you.


# 4.1 Introduction


In this module, you'll add nonfunctional tests to your pipeline. These tests check characteristics like performance and reliability.

In **Run functional tests in Azure Pipelines**, you and the Tailspin Toys web team added UI tests to the pipeline. UI tests are a form of functional testing. Functional tests verify the functionality—or behavior—of software. In other words, functional tests verify that each function of the software does what it should.

But what about the nonfunctional aspects of an application, such as performance and reliability? After your service is operational and deployed to an environment, how can you determine the application's performance under both realistic and heavy loads? Does your application expose any loopholes or weaknesses that might cause an information breach?

In this module, you'll explore the types of nonfunctional tests you can run. You'll run load tests in your pipeline by using Apache JMeter.

## Learning objectives

After completing this module, you'll be able to:

* Define the role of nonfunctional tests and explain how they compare to functional tests.
* Identify some popular kinds of nonfunctional tests you can run.
* Run automated load tests in the pipeline by using Apache JMeter.
* Convert test results to a format that Azure Pipelines can visualize for you.

## Prerequisites

The modules in this learning path are part of a progression. To follow the progression from the beginning, be sure to first complete these learning paths:

* Get started with Azure DevOps
* Build applications with Azure DevOps

We also recommend that you start at the beginning of the **Deploy applications with Azure DevOps** learning path.

If you want to go through just this module, you need to set up a development environment on your Windows, macOS, or Linux system. You need the following resources:

* An Azure DevOps organization with access to parallel jobs. If your organization does not have access to parallel jobs, you can request parallel jobs for free for public or private projects using [this form](https://aka.ms/azpipelines-parallelism-request). Your request will take 2-3 business days.
* An Azure subscription
* A GitHub account
* Visual Studio Code
* .NET 6.0 SDK
* Git

You can get started with Azure and Azure DevOps for free. You don't need an Azure subscription to work with Azure DevOps, but here you'll use Azure DevOps to deploy to resources that exist in your Azure subscription.

The development environment lets you complete the exercises in this and future modules. You can also use it to apply your new skills to your own projects.

> **Note**
> 
> Azure Pipelines support a vast array of **languages and application types**. In this module, you'll be working with a .NET application but you can apply the patterns you learn here to your own projects that use your favorite programming languages and frameworks.


# 4.2 What is nonfunctional testing?

In **Run functional tests in Azure Pipelines**, you added Selenium UI tests to the pipeline. UI tests are a form of functional testing. In this part, you explore the kinds of nonfunctional tests you can run in a pipeline.

The team first defines nonfunctional tests. They talk about some types of these tests. Then they decide on a nonfunctional test to add to their pipeline.

## How do nonfunctional tests compare to functional tests?

In **Run functional tests in Azure Pipelines**, we defined functional tests and nonfunctional tests.

In short, functional tests verify that each function of the software does what it should. In other words, functional tests verify an application's functionality.

Nonfunctional tests check nonfunctional aspects of an application, such as performance and reliability. You can also run nonfunctional tests on systems that aren't apps, such as infrastructure components. One example of a nonfunctional test is determining how many people can simultaneously sign in to an application without causing a problem, such as slower response times.

On the Space Game website as an example, a functional test might verify that the leaderboard appears correctly and that it shows the correct records when the user selects a filter. A nonfunctional test might verify that leaderboard filtering finishes in less than one second, even when many users connect to the website at the same time.

Nonfunctional testing always tests something that's measurable. The goal is to improve the product. You might do that, for example, by improving how efficiently the application uses resources, or by improving response times when many customers use it simultaneously. Here are some of the questions that nonfunctional tests can answer:

- How does the application perform under normal circumstances?
- How does the application perform when many users sign in concurrently?
- How secure is the application?

## What kinds of nonfunctional tests can I run?

There are many kinds of nonfunctional tests. Many of them fit in the broad categories of performance testing and security testing.

### Performance testing

The goal of performance testing is to improve an application's speed, scalability, and stability. Testing for speed determines how quickly an application responds. Testing for scalability determines the maximum user load an application can handle. Testing for stability determines whether the application remains stable under different loads. Two common types of performance tests are load tests and stress tests.

#### Load testing

Load tests determine an application's performance under realistic loads. For example, load tests can determine how well an application performs at the upper limit of its service-level agreement (SLA). Basically, load testing determines the application's behaviors when multiple users need it at the same time.

Users aren't necessarily people. For example, a load test for printer software might send the application large amounts of data. A load test for a mail server might simulate thousands of concurrent users.

Load testing is also a good way to uncover problems that exist only when the application is operating at its limits. That's when issues such as buffer overflow and memory leaks can surface.

In this module, you'll use Apache JMeter to perform load tests. You'll use a set of simulated users that access the website simultaneously.

#### Stress testing

Stress tests determine an application's stability and robustness under heavy loads. The loads go beyond what's specified for the application. The stress tests determine whether the application will crash under these loads. If the application fails, the stress test checks to ensure that it fails gracefully. A graceful failure might, for example, issue an appropriate, informative error message.

Scenarios in which applications must operate under abnormally heavy loads are common. For example, in case your video goes viral, you'll want to know how well the servers can handle the extra load. Another typical scenario is high traffic on shopping websites during holiday seasons.

### Security testing

Security testing ensures that applications are free from vulnerabilities, threats, and risks. Thorough security testing finds all the system's possible loopholes and weaknesses that might cause an information breach or a loss of revenue.

There are many types of security testing. Two of them are penetration testing and compliance testing.

#### Penetration testing

Penetration testing, or pen testing, is a type of security testing that tests the insecure areas of the application. In particular, it tests for vulnerabilities that an attacker could exploit. An authorized, simulated cyber attack is usually a part of penetration testing.

#### Compliance testing

Compliance testing determines whether an application is compliant with some set of requirements, inside or outside the company. For example, healthcare organizations usually need to comply with HIPAA (Health Insurance Portability and Accountability Act of 1996), which provides data privacy and, security provisions for safeguarding medical information.

An organization might also have its own security requirements. Software must be tested to make sure that it follows these requirements. For example, on Linux systems, the default user mask must be 027 or more restrictive. A security test needs to prove that this requirement is met.

## The plan

In the rest of this module, you'll set up your Azure DevOps environment, learn about planning load tests by using Apache JMeter, and run load tests in Azure Pipelines.

## Check your knowledge

**1. You recently connected your web app to a database. Database records appear when the page loads. You want to verify that database calls don't cause the page to take more than one second to load. Which kind of nonfunctional testing might you use?**

- Load testing.
- Stress testing.
- Compliance testing.

**2. Your website sells concert tickets for a local venue. The venue is hosting a multiple-day event that includes many popular performers. You're nervous that the site won't be able to handle the sudden surge in traffic. What kind of testing might help ease your mind?**

- Load testing.
- Stress testing.
- Penetration testing.

**3. You suspect that your website exposes a vulnerability that would allow a hacker to access sensitive data. Which kind of nonfunctional testing might you run to discover this vulnerability?**

- Penetration testing.
- Compliance testing.
- Stress testing.


## Відповіді на запитання:

**1. Правильна відповідь: Load testing.**
**Пояснення:** Load testing визначає продуктивність додатка під реалістичними навантаженнями та може перевірити, чи виконуються викликі бази даних у певному часовому обмеженні (менше однієї секунди).

**2. Правильна відповідь: Stress testing.**
**Пояснення:** Stress testing визначає стабільність та надійність додатка під важкими навантаженнями, які перевищують звичайні специфікації. Це ідеально підходить для тестування раптових сплесків трафіку.

**3. Правильна відповідь: Penetration testing.**
**Пояснення:** Penetration testing спеціально тестує небезпечні області додатка та шукає вразливості, які можуть бути використані зловмисниками для доступу до чутливих даних.




# 4.3 Exercise - Set up your Azure DevOps environment

In this section, you'll make sure that your Azure DevOps organization is set up to complete the rest of this module. You'll also create the Azure App Service environments to which you'll deploy.

To set up your system, you'll:

- Add a user to ensure that Azure DevOps can connect to your Azure subscription.
- Set up an Azure DevOps project for this module.
- On Azure Boards, move the work item for this module to the Doing column.
- Create the Azure App Service environments by using the Azure CLI in Azure Cloud Shell.
- Create pipeline variables that define the names of your App Service environments.
- Create a service connection that enables Azure Pipelines to access your Azure subscription securely.

## Add a user to Azure DevOps

To complete this module, you need your own Azure subscription. You can get started with Azure for free.

Although you don't need an Azure subscription to work with Azure DevOps, in this module you'll use Azure DevOps to deploy to resources that exist in your Azure subscription. To simplify the process, you should use the same Microsoft account to sign in to both your Azure subscription and your Azure DevOps organization.

If you use different Microsoft accounts to sign in to Azure and Azure DevOps, add a user to your DevOps organization under the Microsoft account that you use to sign in to Azure. For more information, see **Add users to your organization or project**. When you add the user, choose the **Basic** access level.

Then, sign out of Azure DevOps and sign in again under the Microsoft account that you use to sign in to your Azure subscription.

## Get the Azure DevOps project

Here, you'll make sure that your Azure DevOps organization is set up to complete the rest of this module. You'll start by running a template that creates your project in Azure DevOps.

The modules in this learning path are part of a progression that follows the Tailspin web team through their DevOps journey. For learning purposes, each module has an associated Azure DevOps project.

### Run the template

Run a template that sets up your Azure DevOps organization.

1. Get and run the **ADOGenerator** project in Visual Studio or the IDE of your choice.

2. When prompted to **Enter the template number from the list of templates**, enter **33** for **Run non-functional tests in Azure Pipelines**, then press Enter.

3. Choose your authentication method. You can set up and use a Personal Access Token (PAT) or use device login.

   > **Note**
   > 
   > If you set up a PAT, make sure to authorize the necessary scopes. For this module, you can use **Full access**, but in a real-world situation, you should ensure you grant only the necessary scopes.

4. Enter your Azure DevOps organization name, then press Enter.

5. If prompted, enter your Azure DevOps PAT, then press Enter.

6. Enter a project name such as **Space Game - web - Nonfunctional tests**, then press Enter.

7. Once your project is created, go to your Azure DevOps organization in your browser (at https://dev.azure.com/<your-organization-name>/) and select the project.

### Fork the repository

If you haven't already, create a fork of the **mslearn-tailspin-spacegame-web-deploy** repository.

1. On GitHub, go to the **mslearn-tailspin-spacegame-web-deploy** repository.

2. Select **Fork** at the top-right of the screen.

3. Choose your GitHub account as the **Owner**, then select **Create fork**.

> **Important**
> 
> The **Clean up your Azure DevOps environment** page in this module contains important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes. Be sure to perform the cleanup steps even if you don't complete this module.

### Set your project's visibility

Initially, your fork of the Space Game repository on GitHub is set to public while the project created by the Azure DevOps template is set to private. A public repository on GitHub can be accessed by anyone, while a private repository is only accessible to you and the people you choose to share it with. Similarly, on Azure DevOps, public projects provide read-only access to non-authenticated users, while private projects require users to be granted access and authenticated to access the services.

At the moment, it is not necessary to modify any of these settings for the purposes of this module. However, for your personal projects, you must determine the visibility and access you wish to grant to others. For instance, if your project is open source, you may choose to make both your GitHub repository and your Azure DevOps project public. If your project is proprietary, you would typically make both your GitHub repository and your Azure DevOps project private.

Later on, you may find the following resources helpful in determining which option is best for your project:

- Use private and public projects
- Change project visibility to public or private
- Setting repository visibility

## Set up the project locally

Here you load the Space Game project in Visual Studio Code, configure Git, clone your repository locally, and set the upstream remote so that you can download starter code.

> **Note**
> 
> If you're already set up with the **mslearn-tailspin-spacegame-web-deploy** project locally, you can move to the next section.

### Open the integrated terminal

Visual Studio Code comes with an integrated terminal. Here you both edit files and work from the command line.

1. Start Visual Studio Code.

2. On the **View** menu, select **Terminal**.

3. In the dropdown list, select **Git Bash**. If you're familiar with another Unix shell that you prefer to use, select that shell instead.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/vscode-terminal-git-bash.png)

   In the terminal window, you can choose any shell that's installed on your system. For example, you can choose Git Bash, or PowerShell, or another shell.

   Here you'll use Git Bash, part of Git for Windows, which makes it easy to run Git commands.

   > **Note**
   > 
   > On Windows, if you don't see Git Bash listed as an option, make sure you've installed Git, and then restart Visual Studio Code.

5. Run the **cd** command to go to the directory where you want to work. Choose your home directory (~) or a different directory if you want.

   **Bash**
   ```
   cd ~
   ```

### Configure Git

If you're new to Git and GitHub, first run a few commands to associate your identity with Git and authenticate with GitHub. For more information, see **Set up Git**.

At a minimum, you need to complete the following steps. Run the commands from the integrated terminal.

1. Set your username.
2. Set your commit email address.
3. Cache your GitHub password.

> **Note**
> 
> If you already use two-factor authentication with GitHub, create a personal access token. When you're prompted, use your token in place of your password.
> 
> Treat your access token like a password. Keep it in a safe place.

### Set up your project in Visual Studio Code

In the **Build applications with Azure DevOps** learning path, you forked and then cloned a Git repository. The repository contains the source code for the Space Game website. Your fork was connected to your projects in Azure DevOps so that the build runs when you push changes to GitHub.

> **Important**
> 
> In this learning path, we switch to a different Git repository, **mslearn-tailspin-spacegame-web-deploy**. When you ran the template to set up your Azure DevOps project, the process forked the repository automatically for you.

In this part, you clone your fork locally so that you can change and build out your pipeline configuration.

#### Clone your fork locally

You now have a copy of the Space Game web project in your GitHub account. Now you'll download, or clone, a copy to your computer so you can work with it.

A clone, just like a fork, is a copy of a repository. When you clone a repository, you can make changes, verify that they work as you expect, and then upload those changes to GitHub. You can also synchronize your local copy with changes that other authenticated users have made to the GitHub copy of your repository.

To clone the Space Game web project to your computer:

1. Go to your fork of the Space Game web project (**mslearn-tailspin-spacegame-web-deploy**) on GitHub.

2. Select **Code**. Then, from the **HTTPS** tab, select the button next to the URL that's shown to copy the URL to your clipboard.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/github-clone-button.png)

4. In Visual Studio Code, go to the terminal window.

5. In the terminal, move to the directory where you want to work. Choose your home directory (~) or a different directory if you want.

   **Bash**
   ```
   cd ~
   ```

6. Run the **git clone** command. Replace the URL that's shown here with the contents of your clipboard:

   **Bash**
   ```
   git clone https://github.com/your-name/mslearn-tailspin-spacegame-web-deploy.git
   ```

7. Move to the **mslearn-tailspin-spacegame-web-deploy** directory. This is the root directory of your repository.

   **Bash**
   ```
   cd mslearn-tailspin-spacegame-web-deploy
   ```

#### Set the upstream remote

A remote is a Git repository where team members collaborate (like a repository on GitHub). Here you list your remotes and add a remote that points to Microsoft's copy of the repository so that you can get the latest sample code.

1. Run this **git remote** command to list your remotes:

   **Bash**
   ```
   git remote -v
   ```

   You see that you have both fetch (download) and push (upload) access to your repository:

   **Output**
   ```
   origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (fetch)
   origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (push)
   ```

   **Origin** specifies your repository on GitHub. When you fork code from another repository, the original remote (the one you forked from) is often named **upstream**.

2. Run this **git remote add** command to create a remote named **upstream** that points to the Microsoft repository:

   **Bash**
   ```
   git remote add upstream https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web-deploy.git
   ```

3. Run **git remote** again to see the changes:

   **Bash**
   ```
   git remote -v
   ```

   You see that you still have both fetch (download) access and push (upload) access to your repository. You also now have fetch access to the Microsoft repository:

   **Output**
   ```
   origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (fetch)
   origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (push)
   upstream        https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web-deploy.git (fetch)
   ```

#### Open the project in the file explorer

In Visual Studio Code, your terminal window points to the root directory of the Space Game web project. To view its structure and work with files, from the file explorer, you'll now open the project.

The easiest way to open the project is to reopen Visual Studio Code in the current directory. To do so, run the following command from the integrated terminal:

**Bash**
```
code -r .
```

You see the directory and file tree in the file explorer.

Reopen the integrated terminal. The terminal places you at the root of your web project.

If the **code** command fails, you need to add Visual Studio Code to your system PATH. To do so:

1. In Visual Studio Code, select **F1** or select **View > Command Palette** to access the command palette.
2. In the command palette, enter **Shell Command: Install 'code' command in PATH**.
3. Repeat the previous procedure to open the project in the file explorer.

You're now set up to work with the Space Game source code and your Azure Pipelines configuration from your local development environment.

## Create the Azure App Service environments

Here, you'll create the environments that define the pipeline stages. You'll create one App Service instance that corresponds to each stage: Dev, Test, and Staging.

In previous modules, you used the Azure CLI to create your App Service instances. Here, you'll do the same.

> **Important**
> 
> Remember that you need your own Azure subscription to complete the exercises in this module.

### Bring up Cloud Shell through the Azure portal

1. Go to the Azure portal and sign in.
2. On the menu bar, select **Cloud Shell**. When you're prompted, select the **Bash** experience.

### Select an Azure region

Here you specify the default region, or geographic location, where your Azure resources are to be created.

1. In Cloud Shell, run the following **az account list-locations** command to list the regions that are available from your Azure subscription.

   **Azure CLI**
   ```
   az account list-locations \
     --query "[].{Name: name, DisplayName: displayName}" \
     --output table
   ```

2. From the **Name** column in the output, choose a region that's close to you. For example, choose **eastasia** or **westus2**.

3. Run **az configure** to set your default region. Replace **<REGION>** with the name of the region that you chose.

   **Azure CLI**
   ```
   az configure --defaults location=<REGION>
   ```

   Here's an example that sets **westus2** as the default region:

   **Azure CLI**
   ```
   az configure --defaults location=westus2
   ```

### Create the App Service instances

Here, you'll create the App Service instances for the three stages to which you'll deploy: Dev, Test, and Staging.

> **Note**
> 
> For learning purposes, use the default network settings. These settings make your site accessible from the internet. In practice, you could configure an Azure virtual network that places your website in a network that's not routable from the internet, and that's accessible to only your team. Later, when you're ready, you could reconfigure your network to make the website available to your users.

1. In Cloud Shell, generate a random number that makes your web app's domain name unique.

   **Bash**
   ```
   webappsuffix=$RANDOM
   ```

2. Run the following **az group create** command to create a resource group that's named **tailspin-space-game-rg**.

   **Azure CLI**
   ```
   az group create --name tailspin-space-game-rg
   ```

3. Run the following **az appservice plan create** command to create an App Service plan that's named **tailspin-space-game-asp**.

   **Azure CLI**
   ```
   az appservice plan create \
     --name tailspin-space-game-asp \
     --resource-group tailspin-space-game-rg \
     --sku B1 \
     --is-linux
   ```

   The **--sku** argument specifies the **B1** plan, which runs on the **Basic** tier. The **--is-linux** argument specifies to use Linux workers.

   > **Important**
   > 
   > If the B1 SKU isn't available as part of your Azure subscription, choose a different plan, such as S1 (Standard).

4. Run the following **az webapp create** commands to create the three App Service instances, one for each of the Dev, Test, and Staging environments.

   **Azure CLI**
   ```
   az webapp create \
     --name tailspin-space-game-web-dev-$webappsuffix \
     --resource-group tailspin-space-game-rg \
     --plan tailspin-space-game-asp \
     --runtime "DOTNET|6.0"

   az webapp create \
     --name tailspin-space-game-web-test-$webappsuffix \
     --resource-group tailspin-space-game-rg \
     --plan tailspin-space-game-asp \
     --runtime "DOTNET|6.0"

   az webapp create \
     --name tailspin-space-game-web-staging-$webappsuffix \
     --resource-group tailspin-space-game-rg \
     --plan tailspin-space-game-asp \
     --runtime "DOTNET|6.0"
   ```

   For learning purposes, here, you apply the same App Service plan, **B1 Basic**, to each App Service instance. In practice, you'd assign a plan that matches your expected workload.

5. Run the following **az webapp list** command to list the host name and state of each App Service instance.

   **Azure CLI**
   ```
   az webapp list \
     --resource-group tailspin-space-game-rg \
     --query "[].{hostName: defaultHostName, state: state}" \
     --output table
   ```

   Note the hostname for each running service. You'll need these host names later when you verify your work. Here's an example:

   **Output**
   ```
   HostName                                                 State
   -------------------------------------------------------  -------
   tailspin-space-game-web-dev-21017.azurewebsites.net      Running
   tailspin-space-game-web-test-21017.azurewebsites.net     Running
   tailspin-space-game-web-staging-21017.azurewebsites.net  Running
   ```

6. As an optional step, go to one or more of the listed names to verify that they're running and that the default home page appears.

   You see this page:

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/app-service-default.png)

> **Important**
> 
> The **Clean up your Azure DevOps environment** page in this module contains important cleanup steps. Cleaning up helps ensure that you're not charged for Azure resources after you complete this module. Be sure to follow the cleanup steps even if you don't complete this module.

## Create pipeline variables in Azure Pipelines

In **Run functional tests in Azure Pipelines**, you added one variable for each of the App Service instances. The instances correspond to the Dev, Test, and Staging stages in your pipeline. Here, you'll follow the same pattern.

Each stage in your pipeline configuration uses the variables to identify which App Service instance to deploy to.

To add the variables:

1. In Azure DevOps, go to your **Space Game - web - Nonfunctional tests** project.

2. Under **Pipelines**, select **Library**.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/5-pipelines-library.png)

4. Select **+ Variable group**.

5. For the variable group name, under **Properties**, enter **Release**.

6. Under **Variables**, select **+ Add**.

7. For the name of your variable, enter **WebAppNameDev**. For its value, enter the name of the App Service instance that corresponds to your Dev environment, such as **tailspin-space-game-web-dev-1234**.

8. Repeat steps 5 and 6 twice more to create variables for your Test and Staging environments, as shown in this table:

   | Variable name | Example value |
   |---------------|---------------|
   | WebAppNameTest | tailspin-space-game-web-test-1234 |
   | WebAppNameStaging | tailspin-space-game-web-staging-1234 |

   Be sure to replace each example value with the App Service instance that corresponds to your environment.

   > **Important**
   > 
   > Make sure that you set the name of the App Service instance, not its host name. In this example, you would enter **tailspin-space-game-web-dev-1234** and not **tailspin-space-game-web-dev-1234.azurewebsites.net**.

9. To save your variable to the pipeline, select **Save** near the top of the page.

Your variable group resembles this one:

![](https://learn.microsoft.com/en-us/training/azure-devops/run-non-functional-tests-azure-pipelines/media/3-library-variable-group.png)

## Create the dev, test, and staging environments

In **Run functional tests in Azure Pipelines**, you created environments for the dev, test, and staging environments. Here, you'll repeat the process.

To create the dev, test, and staging environments:

1. From Azure Pipelines, select **Environments**.

      ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/pipelines-environments.png)

3. To create the **dev** environment:
   - Select **Create environment**.
   - Under **Name**, enter **dev**.
   - Leave the remaining fields at their default values.
   - Select **Create**.

4. To create the **test** environment:
   - Return to the **Environments** page.
   - Select **New environment**.
   - Under **Name**, enter **test**.
   - Select **Create**.

5. To create the **staging** environment:
   - Return to the **Environments** page.
   - Select **New environment**.
   - Under **Name**, enter **staging**.
   - Select **Create**.

## Create a service connection

Here, you'll create a service connection that enables Azure Pipelines to access your Azure subscription. Azure Pipelines uses this service connection to deploy the website to App Service. You created a similar service connection in the previous module.

> **Important**
> 
> Make sure that you're signed in to both the Azure portal and Azure DevOps under the same Microsoft account.

1. In Azure DevOps, go to your **Space Game - web - Nonfunctional tests** project.

2. From the bottom corner of the page, select **Project settings**.

3. Under **Pipelines**, select **Service connections**.

4. Select **New service connection**, then choose **Azure Resource Manager**, then select **Next**.

5. Near the top of the page, **Service principal (automatic)**. Then select **Next**.

6. Fill in these fields:

   | Field | Value |
   |-------|-------|
   | Scope level | Subscription |
   | Subscription | Your Azure subscription |
   | Resource Group | tailspin-space-game-rg |
   | Service connection name | Resource Manager - Tailspin - Space Game |

   During the process, you might be prompted to sign in to your Microsoft account.

7. Ensure that **Grant access permission to all pipelines** is selected.

8. Select **Save**.

Azure DevOps performs a test connection to verify that it can connect to your Azure subscription. If Azure DevOps can't connect, you have the chance to sign in a second time.



# 4.4  Plan load tests by using Apache JMeter

In this section, you'll explore load testing and learn how to add load tests to the pipeline. The load tests use Apache JMeter to simulate multiple users who access the web app simultaneously. The tests fetch the web content from the app that runs on Azure App Service in the Staging environment.

Tim starts by bringing up the Apache JMeter user interface on a laptop. He runs a basic test plan. Then Tim and Mara export the test plan to a file that can be run from the command line. Finally, they add tasks to Azure Pipelines to run the load tests during Staging.

> **Note**
> 
> For brevity, you don't need to install Apache JMeter on your local computer. You can just read along.

## Run load tests from Apache JMeter

Apache JMeter is an open-source load-testing tool that analyzes and measures performance. The report it generates is an XML file.

Azure Pipelines can read the Apache JMeter report and generate a graph. You don't need any special hardware to run these tests, so you can use a Microsoft-hosted agent to run them. In the Space Game scenario, you'd likely run these tests in Staging.

### Create the test plan

Here's what Apache JMeter looks like on a laptop running Linux:

![](https://learn.microsoft.com/en-us/training/azure-devops/run-non-functional-tests-azure-pipelines/media/4-apache-jmeter-new.png)


You'd create a new test plan file; for example, **LoadTest.jmx**. You'd then add a **Thread Group** to the file. Each simulated user runs on its own thread. A thread group controls the number of users and the number of each user's requests.

The following example shows 10 simulated users (threads). Each user makes 10 request, so the system gets a total of 100 requests.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-non-functional-tests-azure-pipelines/media/4-apache-jmeter-thread-group.png)

A **sampler** is a single request made by JMeter. JMeter can query servers over HTTP, FTP, TCP, and several other protocols. Samplers generate the results that are added to the report.

Next, you'd add **Http Request Defaults** and an **Http Request** sampler to the thread group. You'd provide the hostname of the Space Game website that runs in the staging environment on Azure App Service.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-non-functional-tests-azure-pipelines/media/4-apache-jmeter-http-request.png)

The preceding scenario creates a basic test plan.

### Run the test plan

JMeter enables you to run many kinds of tests. It's possible to run your test plan from the JMeter graphical user interface. For load tests, however, the JMeter documentation recommends that you run the test plan from the command line.

You'd run the test plan by using this command:

**Bash**
```
apache-jmeter-5.4.1/bin/./jmeter -n -t LoadTest.jmx -o Results.xml
```

The **-n** argument specifies to run JMeter in non-GUI mode. The **-t** argument specifies the test plan file, **LoadTest.jmx**. The **-o** argument specifies the report file, **Results.xml**.

JMeter runs and produces the report file, **Results.xml**. This example of the file shows the first few results:

**XML**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<testResults version="1.2">
<httpSample t="180" it="0" lt="95" ct="35" ts="1569306009772" s="true" lb="HTTP Request" rc="200" rm="OK" tn="Thread Group 1-1" dt="text" by="40871" sby="144" ng="1" na="1">
  <java.net.URL>http://tailspin-space-game-web-staging-1234.azurewebsites.net/</java.net.URL>
</httpSample>
<httpSample t="174" it="0" lt="96" ct="38" ts="1569306009955" s="true" lb="HTTP Request" rc="200" rm="OK" tn="Thread Group 1-1" dt="text" by="40869" sby="144" ng="1" na="1">
  <java.net.URL>http://tailspin-space-game-web-staging-1234.azurewebsites.net/</java.net.URL>
</httpSample>
<httpSample t="160" it="0" lt="121" ct="35" ts="1569306010131" s="true" lb="HTTP Request" rc="200" rm="OK" tn="Thread Group 1-1" dt="text" by="40879" sby="144" ng="2" na="2">
  <java.net.URL>http://tailspin-space-game-web-staging-1234.azurewebsites.net/</java.net.URL>
</httpSample>
```

Each sample produces a node in the report. The **t** attribute specifies the response time in milliseconds (ms). Here, you see three requests that took 180 ms, 174 ms, and 160 ms.

The ideal request times should average less than one second. No more than 10 percent of requests should take more than one second. You can configure JMeter to report statistics such as the minimum, maximum, and average response times or the standard deviation. You could write a script to help provide this information.

To visualize the test results, you need to provide them in a format that Azure Pipelines understands. Azure Pipelines can parse an XML file that contains test results, but the file needs to be in a supported format. Supported formats include CTest, JUnit (including PHPUnit), NUnit 2, NUnit 3, Visual Studio Test (TRX), and xUnit 2. You could write an XSLT file that converts the JMeter results to JUnit.

## Transform the report to JUnit

XSLT stands for XSL Transformations, or eXtensible Stylesheet Language Transformations. An XSLT file resembles an XML file, but it enables you to transform an XML document to another XML format.

Recall our requirements for load tests:

- The average request time should be less than one second.
- No more than 10 percent of requests should take more than one second.

Here's what an XSLT file that meets those requirements looks like:

**XML**
```xml
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:math="http://exslt.org/math">
  <xsl:output method="xml" indent="yes" encoding="UTF-8"/>
  <xsl:template match="/testResults">
    <xsl:variable name="times" select="./httpSample/@t" />
    <xsl:variable name="failures" select="./httpSample/assertionResult/failureMessage" />
    <xsl:variable name="threshold" select="1000" />
    <testsuite>
      <xsl:attribute name="tests"><xsl:value-of select="count($times)" /></xsl:attribute>
      <xsl:attribute name="failures"><xsl:value-of select="count($failures)" /></xsl:attribute> 
      <testcase>
          <xsl:variable name="avg-time" select="sum($times) div count($times)" />
          <xsl:attribute name="name">Average Response Time</xsl:attribute>
          <xsl:attribute name="time"><xsl:value-of select="format-number($avg-time div 1000,'#.##')"/></xsl:attribute>
          <xsl:if test="$avg-time > $threshold">
            <failure>Average response time of <xsl:value-of select="format-number($avg-time,'#.##')"/> exceeds <xsl:value-of select="$threshold"/> ms threshold.</failure>
          </xsl:if> 
      </testcase>
      <testcase>
          <xsl:variable name="exceeds-threshold" select="count($times[. > $threshold])" />
          <xsl:attribute name="name">Max Response Time</xsl:attribute>
          <xsl:attribute name="time"><xsl:value-of select="math:max($times) div 1000"/></xsl:attribute>
          <xsl:if test="$exceeds-threshold > count($times) * 0.1">
            <failure><xsl:value-of select="format-number($exceeds-threshold div count($times) * 100,'#.##')"/>% of requests exceed <xsl:value-of select="$threshold"/> ms threshold.</failure>
          </xsl:if>
      </testcase>
    </testsuite>
  </xsl:template>
</xsl:stylesheet>
```

We won't delve into how XSL works here. But to summarize, this file first collects the following data from the JMeter output:

- **Each HTTP request time.**

  It collects this data by selecting the **t** attribute from each **httpSample** element. (**./httpSample/@t**)

- **Each failure message.**

  It collects this data by selecting all **failureMessage** nodes from the document. (**./httpSample/assertionResult/failureMessage**)

The XSLT file also sets the threshold value to 1,000 ms. This response time is the maximum that we defined earlier.

Given these variables, the XSLT file provides the total number of tests and the total number of failures. It then provides these two test cases:

1. The average response time, and a failure if the average exceeds the threshold of 1,000 ms.
2. The maximum response time, and a failure if more than 10 percent of requests exceed the threshold of 1,000 ms.

The results of the XSLT match the JUnit format, which Azure Pipelines understands. You could name your XSLT file **JMeter2JUnit.xsl**.

Next, you'd need an XSLT processor. In this example, we'll use **xsltproc**, which is a command-line tool for applying XSLT stylesheets to XML documents.

You could install **xsltproc** as follows:

**Bash**
```
sudo apt-get install xsltproc
```

Next, you'd run **xsltproc** to transform the JMeter report to JUnit:

**Bash**
```
xsltproc JMeter2JUnit.xsl Results.xml > JUnit.xml
```

Here's the resulting JUnit file, **JUnit.xml**:

**XML**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<testsuite xmlns:math="http://exslt.org/math" tests="100" failures="0">
  <testcase name="Average Response Time" time="0.17"/>
  <testcase name="Max Response Time" time="0.373"/>
</testsuite>
```

In this example, the average response time is 170 ms. The maximum response time is 373 ms. Neither test case generates a failure, because both times fall below the threshold of 1,000 ms.

Shortly, you'll run these tests in the pipeline. You can think about **Results.xml**, the file that JMeter writes, as an intermediate file that's not published to the pipeline's test results. **JUnit.xml** is the final report file. This file gets published to the pipeline so that the team can visualize the results.


# 4.5 Exercise - Run load tests in Azure Pipelines

In this section, you'll run the test plan that you created in the release pipeline. The test plan uses Apache JMeter to run load tests.

Here's how you run the tests:

1. Fetch and check out a Git branch that implements the tests.
2. Modify your pipeline to install JMeter, run the test plan, transform the results to JUnit, and publish the results to Azure Pipelines.
3. Push your branch to GitHub, watch the tests run in Azure Pipelines, and then examine the results.

## Fetch the branch from GitHub

In this section, you'll fetch the **jmeter** branch from GitHub and check out, or switch to, that branch.

This branch contains the Space Game project that you worked with in previous modules. It also contains an Azure Pipelines configuration to start with.

1. In Visual Studio Code, open the integrated terminal.

2. To download a branch named **jmeter** from the Microsoft repository and switch to that branch, run the following **git fetch** and **git checkout** commands:

   **Bash**
   ```
   git fetch upstream jmeter
   git checkout -B jmeter upstream/jmeter
   ```

   Recall that **upstream** refers to the Microsoft GitHub repository. Your project's Git configuration understands the upstream remote because you set up that relationship when you forked the project from the Microsoft repository and cloned it locally.

   Shortly, you'll push this branch up to your GitHub repository, known as **origin**.

3. Optionally, in Visual Studio Code, open the **azure-pipelines.yml** file. Review the initial configuration.

   The configuration resembles the ones that you created in previous modules in this learning path. It builds only the application's Release configuration. For brevity, it omits the triggers, manual approvals, and tests that you set up in previous modules.

   > **Note**
   > 
   > A more robust configuration might specify the branches that participate in the build process. For example, to help verify code quality, you might run unit tests each time you push up a change on any branch. You might also deploy the application to an environment that performs more exhaustive testing. But you do this deployment only when you have a pull request, when you have a release candidate, or when you merge code to main.
   > 
   > For more information, see **Implement a code workflow in your build pipeline by using Git and GitHub** and **Build pipeline triggers**.

4. Optionally, in Visual Studio Code, you can check out the JMeter test plan file, **LoadTest.jmx**, and the XLST transform, **JMeter2JUnit.xsl**. The XLST file transforms the JMeter output to JUnit so that Azure Pipelines can visualize the results.

## Add variables to Azure Pipelines

The team's original test plan provides a hard-coded value for the hostname of the Space Game website that runs in the staging environment.

To make the test plan more flexible, your version uses a JMeter property. Think of a property as a variable that you can set from the command line.

Here's how the hostname variable is defined in JMeter:


![](https://learn.microsoft.com/en-us/training/azure-devops/run-non-functional-tests-azure-pipelines/media/5-jmeter-hostname-variable.png)

Here's how the hostname variable uses the **__P** function to read the hostname variable.

![](https://learn.microsoft.com/en-us/training/azure-devops/run-non-functional-tests-azure-pipelines/media/5-jmeter-httprequest-server-name.png)

The corresponding test plan file, **LoadTest.jmx**, specifies this variable and uses it to set the hostname.

When you run JMeter from the command line, you use the **-J** argument to set the hostname property. Here's an example:

**Bash**
```
apache-jmeter-5.4.3/bin/./jmeter -n -t LoadTest.jmx -o Results.xml -Jhostname=tailspin-space-game-web-staging-1234.azurewebsites.net
```

Here, you set the **STAGING_HOSTNAME** variable in Azure Pipelines. This variable points to your site's hostname that runs on App Service in your staging environment. You also set the **jmeterVersion** to specify the version of JMeter to install.

When the agent runs, these variables are automatically exported to the agent as environment variables, so your pipeline configuration can run JMeter this way:

**Bash**
```
apache-jmeter-5.4.3/bin/./jmeter -n -t LoadTest.jmx -o Results.xml -Jhostname=$(STAGING_HOSTNAME)
```

Let's add the pipeline variables now, before you update your pipeline configuration. To do so:

1. In Azure DevOps, go to your **Space Game - web - Nonfunctional tests** project.

2. Under **Pipelines**, select **Library**.

3. Select the **Release** variable group.

4. Under **Variables**, select **+ Add**.

5. For the name of your variable, enter **STAGING_HOSTNAME**. For its value, enter the URL of the App Service instance that corresponds to your staging environment, such as **tailspin-space-game-web-staging-1234.azurewebsites.net**.

   > **Important**
   > 
   > Don't include the **http://** or **https://** protocol prefix in your value. JMeter provides the protocol when the tests run.

6. Add a second variable named **jmeterVersion**. For its value, specify **5.4.3**.

   > **Note**
   > 
   > This is the version of JMeter that we last used to test this module. To get the latest version, see **Download Apache JMeter**.

7. To save your variable to the pipeline, select **Save** near the top of the page.

Your variable group resembles the one shown in the following image:

![](https://learn.microsoft.com/en-us/training/azure-devops/run-non-functional-tests-azure-pipelines/media/5-library-variable-group.png)

## Modify the pipeline configuration

In this section, you'll modify the pipeline to run your load tests during the Staging stage.

In Visual Studio Code, open the **azure-pipelines.yml** file. Then modify the file as follows:

> **Tip**
> 
> You can replace the entire file or just update the part that's highlighted.

```yml
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

- stage: 'Dev'
  displayName: 'Deploy to the dev environment'
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
              appName: '$(WebAppNameDev)'
              package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/*.zip'

- stage: 'Test'
  displayName: 'Deploy to the test environment'
  dependsOn: Dev
  jobs:
  - deployment: Deploy
    pool:
      vmImage: 'ubuntu-20.04'
    environment: test
    variables:
    - group: 'Release'
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
              appName: '$(WebAppNameTest)'
              package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/*.zip'

- stage: 'Staging'
  displayName: 'Deploy to the staging environment'
  dependsOn: Test
  jobs:
  - deployment: Deploy
    pool:
      vmImage: 'ubuntu-20.04'
    environment: staging
    variables:
    - group: 'Release'
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
              appName: '$(WebAppNameStaging)'
              package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/*.zip'
  - job: RunLoadTests
    dependsOn: Deploy
    displayName: 'Run load tests'
    pool:
      vmImage: 'ubuntu-20.04'
    variables:
    - group: Release
    steps:
    - script: |
        wget -c archive.apache.org/dist/jmeter/binaries/apache-jmeter-$(jmeterVersion).tgz
        tar -xzf apache-jmeter-$(jmeterVersion).tgz
      displayName: 'Install Apache JMeter'
    - script: apache-jmeter-$(jmeterVersion)/bin/./jmeter -n -t LoadTest.jmx -o Results.xml -Jhostname=$(STAGING_HOSTNAME)
      displayName: 'Run Load tests'
    - script: |
        sudo apt-get update
        sudo apt-get install xsltproc
        xsltproc JMeter2JUnit.xsl Results.xml > JUnit.xml
      displayName: 'Transform JMeter output to JUnit'
    - task: PublishTestResults@2
      inputs:
        testResultsFormat: JUnit
        testResultsFiles: JUnit.xml
```

Here's a summary of the changes:

- The **RunLoadTests** job does load testing from a Linux agent.
- The **RunLoadTests** job depends on the **Deploy** job to ensure that the jobs are run in the correct order. You need to deploy the website to App Service before you can run the load tests. If you don't specify this dependency, jobs within the stage can run in any order or run in parallel.
- The first script task downloads and installs JMeter. The **jmeterVersion** pipeline variable specifies the version of JMeter to install.
- The second script task runs JMeter. The **-J** argument sets the hostname property in JMeter by reading the **STAGING_HOSTNAME** variable from the pipeline.
- The third script task installs **xsltproc**, an XSLT processor, and transforms the JMeter output to JUnit.
- The **PublishTestResults@2** task publishes the resulting JUnit report, **JUnit.xml**, to the pipeline. Azure Pipelines can help you visualize the test results.

In the integrated terminal, add **azure-pipelines.yml** to the index, commit the changes, and push the branch up to GitHub.

**Bash**
```
git add azure-pipelines.yml
git commit -m "Run load tests with Apache JMeter"
git push origin jmeter
```

## Watch Azure Pipelines run the tests

Here, you'll watch the pipeline run. You'll see the load tests run during Staging.

1. In Azure Pipelines, go to the build and trace it as it runs.

   During Staging, you see the load tests run after the website is deployed.

2. After the build finishes, go to the summary page.

  ![](https://learn.microsoft.com/en-us/training/azure-devops/run-non-functional-tests-azure-pipelines/media/5-stages-complete.png)

   You see that the deployment and the load tests finished successfully.

4. Near the top of the page, note the summary.

   You see that the build artifact for the Space Game website is published just like always. Also note the **Tests and coverage** section, which shows that the load tests have passed.

   ![A screenshot of Azure Pipelines, showing the test summary.](screenshot-test-summary.png)

5. Select the test summary to see the full report.

   The report shows that both tests have passed.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-pipelines-build-summary-tests.png)

   If any test were to fail, you'd see detailed results of the failure. From those results, you could investigate the source of the failure.

   Recall that the XSLT file produces a JUnit file called **JUnit.xml**. The JUnit file answers these two questions:

   - Is the average request time less than one second?
   - Do fewer than 10 percent of requests take more than one second to complete?

   The report proves that these requirements are met. To see more details, select the **Outcome** arrow in the report. Then make sure that only **Passed** is selected.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/run-non-functional-tests-azure-pipelines/media/5-tests-outcome-filter.png)

   You see that the **Average Response Time** and **Max Response Time** test cases both succeeded.


   ![](https://learn.microsoft.com/en-us/training/azure-devops/run-non-functional-tests-azure-pipelines/media/5-tests-junit-details.png)

> **Note**
> 
> You're using the B1 App Service plan, which runs on the Basic tier. This plan is intended for apps that have low traffic requirements, such as apps in a test environment. Because of this plan, the performance of your website might be less than you expect. In practice, you'd choose a plan for the staging environment that more closely matches your production environment. For example, the Standard and Premium plans are for production workloads. These run on dedicated virtual machine instances.


# 4.6 Exercise - Clean up your Azure DevOps environment


You're all done with the tasks for this module. Here, you'll clean up your Azure resources, move the work item to the **Done** state in Azure Boards, and clean up your Azure DevOps environment.

> **Important**
> 
> This page contains important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes. It also helps ensure that you're not charged for Azure resources after you complete this module.

## Clean up Azure resources

Here, you'll delete your Azure App Service instances. The easiest way to do that is to delete their parent resource group. Deleting a resource group deletes all resources in that group.

To clean up your resource group:

1. Go to the Azure portal and sign in.

2. On the menu bar, select **Cloud Shell**. When you're prompted, select the **Bash** experience.

3. Run the following `az group delete` command to delete the resource group that you used in this module, **tailspin-space-game-rg**:

   **Azure CLI**
   ```
   az group delete --name tailspin-space-game-rg
   ```

   When you're prompted, enter **y** to confirm the operation.

4. As an optional step, after the previous command finishes, run the following `az group list` command.

   **Azure CLI**
   ```
   az group list --output table
   ```

   You'll see that the resource group **tailspin-space-game-rg** no longer exists.

## Disable the pipeline or delete your project

Each module in this learning path provides a template. You can run the template to create a clean environment for the duration of the module.

Running multiple templates gives you multiple Azure Pipelines projects. Each project points to the same GitHub repository. This setup can trigger multiple pipelines to run each time you push a change to your GitHub repository, which can cause you to run out of free build minutes on our hosted agents, so it's important to disable or delete your pipeline before you move on to the next module.

Choose one of the following options.

### Option 1: Disable the pipeline

Disable the pipeline so that it doesn't process further build requests. You can later reenable the build pipeline if you want to. Choose this option if you want to keep your DevOps project and your build pipeline for future reference.

To disable the pipeline:

1. In Azure Pipelines, navigate to your pipeline.

2. From the drop-down menu, select **Settings**:

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-pipelines-settings-button.png)

4. Under **Processing of new run requests**, select **Disabled**, then select **Save**.

Your pipeline will no longer process build requests.

### Option 2: Delete the Azure DevOps project

You can also delete your Azure DevOps project, including the contents of Azure Boards and your build pipeline. In future modules, you can run another template that brings up a new project in a state where this module leaves off. Choose this option if you don't need your DevOps project for future reference.

To delete the project:

1. In Azure DevOps, navigate to your project. Earlier, we recommended that you name this project **Space Game - web - Nonfunctional tests**.

2. Select **Project settings** in the lower corner.

3. At the bottom of the **Project details** area, select **Delete**.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-delete-project.png)

4. In the window that appears, enter the project name and select **Delete** again.

Your project is now deleted.



# 4.7 Summary

Nice job! In this module, we defined a nonfunctional test as a test that checks characteristics like performance and reliability. Compare this type of test to a functional test, which verifies that a given function of the software does what it should. We also defined some popular kinds of nonfunctional tests, including load tests, stress tests, and penetration tests.

You and your team chose one type of nonfunctional test to automate the load tests first. By using a few commands, you took a test plan that was created in Apache JMeter and ran it in the pipeline. Now with each code change, the team can track the performance of the site under a normal load. If performance begins to drop, you know which change caused it.

Just as you did when you incorporated functional tests into your pipeline, focus on the types of nonfunctional tests that matter most. For example, if your team must adhere to certain compliance requirements, consider adding automated tests that provide a detailed status report.

## Learn more
If you're interested in performance testing in Apache JMeter, here are some resources to help you go further:

- JMeter.Apache.org
- Apache JMeter - User's manual: Best practices


# 5 Manage release cadence in Azure Pipelines by using deployment patterns

Choose and implement a deployment pattern that helps you smoothly roll out new application features to your users.

#### Learning objectives
After completing this module, you'll be able to:
- Explain why deployment patterns matter.
- Compare different deployment patterns so that you can choose the one that best suits your needs.
- Apply the blue-green deployment pattern in your pipeline.
#### Prerequisites
- An Azure subscription
- An Azure DevOps organization with access to parallel jobs
- Visual Studio Code
- .NET 6.0 SDK
- Git
- A GitHub account



# 5.1 Introduction

In this learning path, you've been helping the Tailspin Toys team set up an automated release pipeline. The pipeline includes multiple stages, and both functional and nonfunctional tests.

In this module, you help the team solve another problem, which is how to implement a deployment pattern to release to production in a way that's best for the company and their users. You'll help them evaluate the possibilities and then implement the one they choose.

## Learning objectives

After completing this module, you'll be able to:

* Explain why deployment patterns matter.
* Compare different deployment patterns so that you can choose the one that best suits your needs.
* Apply the blue-green deployment pattern in your pipeline.

## Prerequisites

The modules in this learning path are part of a progression.

To follow the progression from the beginning, be sure to first complete these learning paths:

* Get started with Azure DevOps
* Build applications with Azure DevOps

We also recommend that you start at the beginning of this learning path, **Deploy applications with Azure DevOps**.

If you want to go through just this module, then you need to set up a development environment on your Windows, macOS, or Linux system. You'll need the following resources:

* An Azure DevOps organization with access to parallel jobs. If your organization does not have access to parallel jobs, you can request parallel jobs for free for public or private projects using [this form](https://aka.ms/azpipelines-parallelism-request). Your request will take 2-3 business days.
* An Azure subscription
* A GitHub account
* Visual Studio Code
* .NET 6.0 SDK
* Git

You can get started with Azure and Azure DevOps for free. You don't need an Azure subscription to work with Azure DevOps, but here you'll use Azure DevOps to deploy to resources that exist in your Azure subscription.

This environment lets you complete the exercises in this and future modules. You can also use it to apply your new skills to your own projects.

> **Note**
> 
> Azure Pipelines support a vast array of **languages and application types**. In this module, you'll be working with a .NET application but you can apply the patterns you learn here to your own projects that use your favorite programming languages and frameworks.

## Meet the team

You met the *Space Game* web team at Tailspin Toys in previous modules. As a refresher, here's who you'll work with in this module.

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

Mara has prior experience with DevOps. She's helping the team adopt a more automated process that uses Azure DevOps.



# 5.2 What are deployment patterns?

A deployment pattern is an automated way to smoothly roll out new application features to your users. An appropriate deployment pattern helps you minimize downtime. Some patterns also enable you to roll out new features progressively. That way, you can validate new features with select users before you make those features available to everyone.

In this section, you'll learn about some common deployment patterns. You'll also learn how Azure App Service will help implement the pattern that the Tailspin team chooses.

## Morning meeting

The Tailspin team is feeling good. Their pipeline has sped up their process. The team has a development environment where they can integrate the web app with a database. Both Tim and Amita are happy to have automated tests that simplify their jobs. In general, they see fewer delays and fewer bugs.

But there is, as always, a problem. Let's drop in on the team meeting, where Tim is talking.

**Tim:** It's so hard to keep everyone happy. Irwin thinks it takes too long to release new features. I can't do anything until management approves the release and, right now, there's no smooth way to roll out the features after they give the OK. The process isn't only long but messy. It's manual, and there's downtime. The whole process can take five days. I know that's too long, but what am I supposed to do? Maybe if I just drink more coffee the solution will come to me.

**Andy:** Coffee is essential to effective problem solving, no doubt.

I think the solution we need is a good deployment pattern. A deployment pattern is an automated way to do the cutover. It's how we move the software from the final pre-production stage to live production.

Picking the right pattern would definitely help you, like by minimizing downtime. Another advantage of a deployment pattern is that it gives us a chance to run tests that should really happen in production.

Andy starts writing on the whiteboard.

Here are the possibilities we should consider:

- Blue-green deployment
- Canary releases
- Feature toggles
- Dark launches
- A/B testing
- Progressive-exposure deployment

Let's briefly discuss each pattern.

## Blue-green deployments

A blue-green deployment reduces risk and downtime by running two identical environments. These environments are called blue and green. At any time, only one of the environments is live. A blue-green deployment typically involves a router or load balancer that helps control the flow of traffic.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-release-cadence/media/2-blue-green-deployment.png)

Let's say blue is live. As we prepare a new release, we do our final tests in the green environment. After the software is working in the green environment, we just switch the router so that all incoming requests go to the green environment.

Blue-green deployment also gives us a fast way to do a rollback. If anything goes wrong in the green environment, then we just switch the router back to the blue environment.

## Canary releases

A canary release is a way to identify potential problems early without exposing all users to the issue. The idea is that we expose a new feature to only a small subset of users before we make it available to everyone.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-release-cadence/media/2-canary-deployment.png)

In a canary release, we monitor what happens when we release the feature. If the release has problems, then we apply a fix. After the canary release is known to be stable, then we move it to the actual production environment.

## Feature toggles

Use feature toggles to "flip a switch" at runtime. We can deploy new software without exposing any other new or changed functionality to our users.

In this deployment pattern, Mara and I build new features behind a toggle. When a release occurs, the feature is "off" so that it doesn't affect the production software. Depending on how we configure the toggle, we can flip the switch to "on" and expose the feature how we want.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-release-cadence/media/2-feature-toggles.png)

For example, we could expose the feature first to a few users to see how they react. That random sample of users sees the feature. Or we could just let the feature go live to everyone.

But this deployment pattern might benefit Mara and me more than anyone else. A big advantage to the feature toggles pattern is that it helps us avoid too much branching. Merging branches can be painful.

## Dark launches

A dark launch is similar to a canary release or switching a feature toggle. Rather than expose a new feature to everyone, in a dark launch we release the feature to a small set of users.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-release-cadence/media/2-dark-launches.png)

Those users don't know they're testing the feature for us. We don't even highlight the new feature to them. That's why it's called a dark launch. The software is gradually or unobtrusively released to users so we can get feedback and can test performance.

## A/B testing

A/B testing compares two versions of a webpage or app to determine which one performs better. A/B testing is like a classical experiment.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-release-cadence/media/2-a-b-testing.png)

In A/B testing, we randomly show users two or more variations of a page. Then we use statistical analysis to decide which variation performs better for our goals.

## Progressive-exposure deployment

Progressive-exposure deployment is sometimes called ring-based deployment. It's another way to limit how changes affect users while making sure those changes are valid in a production environment.

Rings are basically an extension of the canary stage. The canary release itself releases to a stage to measure effect. Adding another ring is essentially the same idea.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-release-cadence/media/2-progressive-exposure-deployment.png)

In a ring-based deployment, we deploy changes to risk-tolerant customers first. Then we progressively roll out to a larger set of customers.

## Implementing the blue-green deployment

Andy looks at Tim.

**Andy:** That's a lot, I know. Do you want to take some time to think about it? Or you and I could ...

**Tim:** Blue-green.

Everyone in the room laughs.

**Mara:** Is that the coffee talking?

**Tim:** Feature toggles involve a change in how you and Andy work. Let's do one thing at a time. The methods that gradually expose a feature require statistical analysis or feature toggles.

A blue-green deployment is something I can control. Switching a router is straightforward. It's easy and sounds safe. And in a blue-green deployment, management has an environment to evaluate. When they give the OK, we can easily switch. Let's start there.

So the question is, how do we implement a blue-green deployment in our pipeline?

## What are deployment slots?

**Andy:** Because we're using Azure App Service, we can take advantage of deployment slots. Deployment slots are running apps that have their own host names.

I know we're not yet ready to deploy the Space Game website to production as part of the automated pipeline. But as a test, we can add a deployment slot to our staging environment.

Instead of setting up a load balancer or a router, we can just add a second slot to the App Service instance that we use in our existing Staging environment. We can call the primary slot blue and the secondary slot green.

![](https://learn.microsoft.com/en-us/training/modules/manage-release-cadence/2-what-are-deployment-patterns)

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-release-cadence/media/2-zero-downtime-deployment.png)

This way we can deploy new features without any downtime. We swap an application and its configuration between the two deployment slots. Basically we're swapping the IP addresses of the two slots.

**Tim:** I like that! You might call this variation of a blue-green deployment a zero-downtime deployment.

**Andy:** Great! Tim and I'll work on implementing this deployment pattern. We can all meet later to see the results.

## Recommendations for using feature flags

Feature flags were one of the release-cadence methods that the team considered. The team decided not to use feature flags, but many people have found them useful. This section provides more information about feature flags.

Feature flags, sometime called feature toggles, allow you to change how a system works without changing the code. These flags allow you to push new code into your central development branch and have the code deployed but not necessarily functional. The flags are commonly implemented as the value of variables that control conditional logic.

Imagine that your team is working in the central development branch of a bank application. You decided to do all the work in the main branch to avoid messy merge operations later. But you face a problem. You're substantially changing the interest calculations, and people depend on that code every day. Worse, the changes will take you weeks to complete. You can't leave the main code broken for so long.

In this scenario, a feature flag might be a good solution. You can change the code so that users who don't have the feature flag set can keep using the original interest calculation code. Meanwhile, your team does have the feature flag set, so they can see the code that they're changing.

Another type of feature flag is a release flag. Imagine that after you complete the work on the interest calculation code, you want to try it out before you release it publicly. You have a group of users who are well positioned to deal with new code and any possible issues. You'll let them try the feature first. You change the configuration so that they also have the feature flag set and can test the new code. If problems happen, then you can quickly disable the flag.

## Check your knowledge

**1. The marketing team has asked you to add a banner to your company's website. They have two versions of this banner. They want to know which version produces more clickthroughs. Which deployment pattern might you use to help the marketing team identify the better version?**

- Blue-green deployment
- A/B testing
- Feature toggles

**2. You have a new feature for your website, and you're ready to deploy it. However, this feature is risky because it changes the way your users interact with the site. Which deployment patterns might you use to release to a small group of early adopters who have signed up to see new features?**

- Canary release or progressive-exposure deployment
- A/B testing or a dark launch
- Blue-green deployment or feature toggles

**3. You're not sure how your users will react to your new feature. You want to release your feature to a small, random sample of users to see how they react. Which deployment pattern might you use?**

- Blue-green deployment
- Dark launch
- A/B testing


**Відповіді на запитання:**

1. **A/B testing** - найкращий варіант для порівняння двох версій банера та визначення, яка дає більше кліків.

2. **Canary release or progressive-exposure deployment** - ідеально підходить для поступового розгортання ризикованих функцій серед раннього прийняття користувачів.

3. **Dark launch** - дозволяє випустити функцію для невеликої випадкової вибірки користувачів, які не знають, що тестують нову функцію.



# 5.3 Exercise - Set up your environment

In this section, you make sure that your Azure DevOps organization is set up to complete the rest of this module. You also create the Azure App Service environments that you'll deploy to.

To meet these objectives, you:

- Add a user to ensure that Azure DevOps can connect to your Azure subscription.
- Set up an Azure DevOps project for this module.
- In Azure Boards, move the work item for this module to the Doing column.
- Make sure that your project is set up locally so that you can push changes to the pipeline.
- Create the Azure App Service environments by using the Azure CLI in Azure Cloud Shell.
- Create pipeline variables that define the names of your App Service environments.
- Create a service connection that enables Azure Pipelines to securely access your Azure subscription.
- Perform an initial deployment.

## Add a user to Azure DevOps

To complete this module, you need your own Azure subscription. You can get started with Azure for free.

Although you don't need an Azure subscription to work with Azure DevOps, here you'll use Azure DevOps to deploy to resources that exist in your Azure subscription. To simplify the process, use the same Microsoft account to sign in to both your Azure subscription and your Azure DevOps organization.

If you use different Microsoft accounts to sign in to Azure and Azure DevOps, then add a user to your DevOps organization under the Microsoft account that you use to sign in to Azure. For more information, see **Add users to your organization or project**. When you add the user, choose the **Basic** access level.

Then sign out of Azure DevOps and sign in again under the Microsoft account that you use to sign in to your Azure subscription.

## Get the Azure DevOps project

Here you make sure that your Azure DevOps organization is set up to complete the rest of this module. You set it up by running a template that creates a project in Azure DevOps.

The modules in this learning path are part of a progression. You follow the Tailspin web team through their DevOps journey. For learning purposes, each module has an associated Azure DevOps project.

### Run the template

Run a template that sets up your Azure DevOps organization.

1. Get and run the **ADOGenerator** project in Visual Studio or the IDE of your choice.

2. When prompted to **Enter the template number from the list of templates**, enter **34** for **Manage release cadence in Azure Pipelines with deployment patterns**, then press Enter.

3. Choose your authentication method. You can set up and use a Personal Access Token (PAT) or use device login.

   > **Note**
   > 
   > If you set up a PAT, make sure to authorize the necessary scopes. For this module, you can use **Full access**, but in a real-world situation, you should ensure you grant only the necessary scopes.

4. Enter your Azure DevOps organization name, then press Enter.

5. If prompted, enter your Azure DevOps PAT, then press Enter.

6. Enter a project name such as **Space Game - web - Deployment patterns**, then press Enter.

7. Once your project is created, go to your Azure DevOps organization in your browser (at https://dev.azure.com/<your-organization-name>/) and select the project.

### Fork the repository

If you haven't already, create a fork of the **mslearn-tailspin-spacegame-web-deploy** repository.

1. On GitHub, go to the **mslearn-tailspin-spacegame-web-deploy** repository.

2. Select **Fork** at the top-right of the screen.

3. Choose your GitHub account as the **Owner**, then select **Create fork**.

> **Important**
> 
> The **Clean up your Azure DevOps environment** page in this module contains important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes. Be sure to follow the cleanup steps even if you don't complete this module.

### Set your project's visibility

Initially, your fork of the Space Game repository on GitHub is set to public while the project created by the Azure DevOps template is set to private. A public repository on GitHub can be accessed by anyone, while a private repository is only accessible to you and the people you choose to share it with. Similarly, on Azure DevOps, public projects provide read-only access to non-authenticated users, while private projects require users to be granted access and authenticated to access the services.

At the moment, it is not necessary to modify any of these settings for the purposes of this module. However, for your personal projects, you must determine the visibility and access you wish to grant to others. For instance, if your project is open source, you may choose to make both your GitHub repository and your Azure DevOps project public. If your project is proprietary, you would typically make both your GitHub repository and your Azure DevOps project private.

Later on, you may find the following resources helpful in determining which option is best for your project:

- Use private and public projects
- Change project visibility to public or private
- Setting repository visibility

## Move the work item to Doing

In this part, in Azure Boards you assign yourself a work item that relates to this module. You also move the work item to the **Doing** state. In practice, your team would create work items at the start of each sprint, or work iteration.

Assigning work in this way gives you a checklist to work from. It gives your team visibility into what you're working on and how much work is left. It also helps the team enforce limits on work in progress (WIP) so that the team doesn't take on too much work at one time.

Recall that the team settled on these top issues for the current sprint:

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/deploy-all-tasks.png)

> **Note**
> 
> Within an Azure DevOps organization, work items are numbered sequentially. In your project, the number for each work item might not match what you see here.

Here you move the fifth item, **Improve release cadence**, to the **Doing** column. Then you assign yourself to the work item. **Improve release cadence** relates to choosing a deployment pattern that enables you to quickly release changes to your users.

To set up the work item:

1. In Azure DevOps, go to **Boards**, and then select **Boards** from the menu.

     ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-boards-menu.png)

3. At the bottom of the **Improve release cadence** work item, select the down arrow. Then assign the work item to yourself.

     ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-boards-down-chevron.png)

5. Move the work item from the **To Do** column to the **Doing** column.

      ![](https://learn.microsoft.com/en-us/training/azure-devops/manage-release-cadence/media/3-azure-boards-wi5-doing.png)

At the end of this module, you move the card to the **Done** column after you complete the task.

## Set up the project locally

Here you load the Space Game project in Visual Studio Code, configure Git, clone your repository locally, and set the upstream remote so that you can download starter code.

> **Note**
> 
> If you're already set up with the **mslearn-tailspin-spacegame-web-deploy** project locally, you can move to the next section.

### Open the integrated terminal

Visual Studio Code comes with an integrated terminal. Here you both edit files and work from the command line.

1. Start Visual Studio Code.

2. On the **View** menu, select **Terminal**.

3. In the dropdown list, select **Git Bash**. If you're familiar with another Unix shell that you prefer to use, select that shell instead.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/vscode-terminal-git-bash.png)

   In the terminal window, you can choose any shell that's installed on your system. For example, you can choose Git Bash, or PowerShell, or another shell.

   Here you'll use Git Bash, part of Git for Windows, which makes it easy to run Git commands.

   > **Note**
   > 
   > On Windows, if you don't see Git Bash listed as an option, make sure you've installed Git, and then restart Visual Studio Code.

5. Run the **cd** command to go to the directory where you want to work. Choose your home directory (~) or a different directory if you want.

   **Bash**
   ```
   cd ~
   ```

### Configure Git

If you're new to Git and GitHub, first run a few commands to associate your identity with Git and authenticate with GitHub. For more information, see **Set up Git**.

At a minimum, you need to complete the following steps. Run the commands from the integrated terminal.

1. Set your username.
2. Set your commit email address.
3. Cache your GitHub password.

> **Note**
> 
> If you already use two-factor authentication with GitHub, create a personal access token. When you're prompted, use your token in place of your password.
> 
> Treat your access token like a password. Keep it in a safe place.

### Set up your project in Visual Studio Code

In the **Build applications with Azure DevOps** learning path, you forked and then cloned a Git repository. The repository contains the source code for the Space Game website. Your fork was connected to your projects in Azure DevOps so that the build runs when you push changes to GitHub.

> **Important**
> 
> In this learning path, we switch to a different Git repository, **mslearn-tailspin-spacegame-web-deploy**. When you ran the template to set up your Azure DevOps project, the process forked the repository automatically for you.

In this part, you clone your fork locally so that you can change and build out your pipeline configuration.

#### Clone your fork locally

You now have a copy of the Space Game web project in your GitHub account. Now you'll download, or clone, a copy to your computer so you can work with it.

A clone, just like a fork, is a copy of a repository. When you clone a repository, you can make changes, verify that they work as you expect, and then upload those changes to GitHub. You can also synchronize your local copy with changes that other authenticated users have made to the GitHub copy of your repository.

To clone the Space Game web project to your computer:

1. Go to your fork of the Space Game web project (**mslearn-tailspin-spacegame-web-deploy**) on GitHub.

2. Select **Code**. Then, from the **HTTPS** tab, select the button next to the URL that's shown to copy the URL to your clipboard.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/github-clone-button.png)

4. In Visual Studio Code, go to the terminal window.

5. In the terminal, move to the directory where you want to work. Choose your home directory (~) or a different directory if you want.

   **Bash**
   ```
   cd ~
   ```

6. Run the **git clone** command. Replace the URL that's shown here with the contents of your clipboard:

   **Bash**
   ```
   git clone https://github.com/your-name/mslearn-tailspin-spacegame-web-deploy.git
   ```

7. Move to the **mslearn-tailspin-spacegame-web-deploy** directory. This is the root directory of your repository.

   **Bash**
   ```
   cd mslearn-tailspin-spacegame-web-deploy
   ```

#### Set the upstream remote

A remote is a Git repository where team members collaborate (like a repository on GitHub). Here you list your remotes and add a remote that points to Microsoft's copy of the repository so that you can get the latest sample code.

1. Run this **git remote** command to list your remotes:

   **Bash**
   ```
   git remote -v
   ```

   You see that you have both fetch (download) and push (upload) access to your repository:

   **Output**
   ```
   origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (fetch)
   origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (push)
   ```

   **Origin** specifies your repository on GitHub. When you fork code from another repository, the original remote (the one you forked from) is often named **upstream**.

2. Run this **git remote add** command to create a remote named **upstream** that points to the Microsoft repository:

   **Bash**
   ```
   git remote add upstream https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web-deploy.git
   ```

3. Run **git remote** again to see the changes:

   **Bash**
   ```
   git remote -v
   ```

   You see that you still have both fetch (download) access and push (upload) access to your repository. You also now have fetch access to the Microsoft repository:

   **Output**
   ```
   origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (fetch)
   origin  https://github.com/username/mslearn-tailspin-spacegame-web-deploy.git (push)
   upstream        https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web-deploy.git (fetch)
   ```

#### Open the project in the file explorer

In Visual Studio Code, your terminal window points to the root directory of the Space Game web project. To view its structure and work with files, from the file explorer, you'll now open the project.

The easiest way to open the project is to reopen Visual Studio Code in the current directory. To do so, run the following command from the integrated terminal:

**Bash**
```
code -r .
```

You see the directory and file tree in the file explorer.

Reopen the integrated terminal. The terminal places you at the root of your web project.

If the **code** command fails, you need to add Visual Studio Code to your system PATH. To do so:

1. In Visual Studio Code, select **F1** or select **View > Command Palette** to access the command palette.
2. In the command palette, enter **Shell Command: Install 'code' command in PATH**.
3. Repeat the previous procedure to open the project in the file explorer.

You're now set up to work with the Space Game source code and your Azure Pipelines configuration from your local development environment.

## Create the Azure App Service environments

Here you create the environments that define the pipeline stages. You create one App Service instance that corresponds to each stage: Dev, Test, and Staging.

In previous modules, you used the Azure CLI to create your App Service instances. Here you'll do the same.

> **Important**
> 
> You need your own Azure subscription to complete the exercises in this module.

### Bring up Cloud Shell through the Azure portal

1. Go to the Azure portal and sign in.
2. On the menu, select **Cloud Shell**. When you're prompted, select the **Bash** experience.

### Select an Azure region

Here you specify the default region, or geographic location, where your Azure resources will be created.

1. In Cloud Shell, run the following **az account list-locations** command to list the regions that are available from your Azure subscription.

   **Azure CLI**
   ```
   az account list-locations \
     --query "[].{Name: name, DisplayName: displayName}" \
     --output table
   ```

2. From the **Name** column in the output, choose a region that's close to you. For example, choose **eastasia** or **westus2**.

3. Run **az configure** to set your default region. Replace **<REGION>** with the name of the region that you chose.

   **Azure CLI**
   ```
   az configure --defaults location=<REGION>
   ```

   This example sets **westus2** as the default region:

   **Azure CLI**
   ```
   az configure --defaults location=westus2
   ```

### Create the App Service instances

Here you create App Service instances for the three stages that you'll deploy to: Dev, Test, and Staging. You'll add a deployment slot to Staging later in this module.

> **Note**
> 
> For learning purposes, here you use the default network settings. These settings make your site accessible from the internet. In practice, you could configure an Azure virtual network that places your website in a network that's not routable from the internet but that only your team can access. Later, when you're ready, you could reconfigure your network to make the website available to your users.

1. In Cloud Shell, generate a random number that makes your web app's domain name unique:

   **Bash**
   ```
   webappsuffix=$RANDOM
   ```

2. Run the following **az group create** command to create a resource group that's named **tailspin-space-game-rg**.

   **Azure CLI**
   ```
   az group create --name tailspin-space-game-rg
   ```

3. Run the following commands to create two App Service plans.

   **Azure CLI**
   ```
   az appservice plan create \
     --name tailspin-space-game-test-asp \
     --resource-group tailspin-space-game-rg \
     --sku B1 \
     --is-linux

   az appservice plan create \
     --name tailspin-space-game-prod-asp \
     --resource-group tailspin-space-game-rg \
     --sku P1V2 \
     --is-linux
   ```

   > **Important**
   > 
   > If the B1 SKU isn't available as part of your Azure subscription, then choose a different plan, such as S1 (Standard).

   Recall that an App Service plan defines the CPU, memory, and storage resources that are provided for your web app to run.

   The first command specifies the **B1** plan. This plan runs on the **Basic** tier. The App Service environments use this plan for the Dev and Test stages. The B1 Basic plan is intended for apps that have low-traffic requirements, such as in a development or test environment.

   The second command specifies the **P1V2** plan, which runs on the **Premium** tier. This plan is used for Staging. The Premium P1V2 plan is for production workloads. It runs on dedicated virtual machine instances.

   The Basic plan tier offers no additional deployment slots. However, the Premium plan does. That's why you need the Premium plan for your Staging environment.

4. Run the following **az webapp create** commands to create the three App Service instances, one for each of the Dev, Test, and Staging environments.

   **Azure CLI**
   ```
   az webapp create \
     --name tailspin-space-game-web-dev-$webappsuffix \
     --resource-group tailspin-space-game-rg \
     --plan tailspin-space-game-test-asp \
     --runtime "DOTNET|6.0"

   az webapp create \
     --name tailspin-space-game-web-test-$webappsuffix \
     --resource-group tailspin-space-game-rg \
     --plan tailspin-space-game-test-asp \
     --runtime "DOTNET|6.0"

   az webapp create \
     --name tailspin-space-game-web-staging-$webappsuffix \
     --resource-group tailspin-space-game-rg \
     --plan tailspin-space-game-prod-asp \
     --runtime "DOTNET|6.0"
   ```

   Notice that here you apply the same App Service plan, **B1 Basic**, to the App Service instances for Dev and Test. You apply the App Service plan **Premium P1V2** to the App Service instance for Staging.

5. Run the following **az webapp list** command to list the host name and state of each App Service instance.

   **Azure CLI**
   ```
   az webapp list \
     --resource-group tailspin-space-game-rg \
     --query "[].{hostName: defaultHostName, state: state}" \
     --output table
   ```

   Note the host name for each running service. You'll need these host names later when you verify your work. Here's an example of the host names:

   **Output**
   ```
   HostName                                                 State
   -------------------------------------------------------  -------
   tailspin-space-game-web-dev-21017.azurewebsites.net      Running
   tailspin-space-game-web-test-21017.azurewebsites.net     Running
   tailspin-space-game-web-staging-21017.azurewebsites.net  Running
   ```

6. As an optional step, go to one or more of the names. Verify that they're running and that the default home page appears.

   You see this page in each environment:

    ![](https://learn.microsoft.com/en-us/training/azure-devops/manage-release-cadence/media/3-app-service-default-tailspin.png)

> **Important**
> 
> The **Clean up your Azure DevOps environment** page in this module contains important cleanup steps. Cleaning up helps ensure that you're not charged for Azure resources after you complete this module. Be sure to perform the cleanup steps even if you don't complete this module.

## Create pipeline variables in Azure Pipelines

In **Create a multistage pipeline by using Azure Pipelines**, you added one variable for each of the App Service instances that correspond to the Dev, Test, and Staging stages in your pipeline. Here you do the same.

Each stage in your pipeline configuration uses these variables to identify which App Service instance to deploy to.

To add the variables:

1. In Azure DevOps, go to your **Space Game - web - Deployment patterns** project.

2. Under **Pipelines**, select **Library**.

   
   ![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/5-pipelines-library.png)

4. Select **+ Variable group**.

5. Under **Properties**, for the variable group name, enter **Release**.

6. Under **Variables**, select **+ Add**.

7. For the name of your variable, enter **WebAppNameDev**. As its value, enter the name of the App Service instance that corresponds to your Dev environment, such as **tailspin-space-game-web-dev-1234**.

8. Repeat steps 5 and 6 twice more to create variables for your Test and Staging environments, as shown in this table:

   | Variable name | Example value |
   |---------------|---------------|
   | WebAppNameTest | tailspin-space-game-web-test-1234 |
   | WebAppNameStaging | tailspin-space-game-web-staging-1234 |

   Be sure to replace each example value with the App Service instance that corresponds to your environment.

   > **Important**
   > 
   > Set the name of the App Service instance, not its host name. In this example, you would enter **tailspin-space-game-web-dev-1234** and not **tailspin-space-game-web-dev-1234.azurewebsites.net**.

9. Near the top of the page, select **Save** to save your variable to the pipeline.

Your variable group resembles this one:

![](https://learn.microsoft.com/en-us/training/azure-devops/create-release-pipeline/media/5-pipelines-library.png)

## Create the dev, test, and staging environments

In previous modules, you created environments for the dev, test, and staging environments. Here, you repeat the process.

To create the dev, test, and staging environments:

1. From Azure Pipelines, select **Environments**.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/pipelines-environments.png)

3. To create the **dev** environment:
   - Select **Create environment**.
   - Under **Name**, enter **dev**.
   - Leave the remaining fields at their default values.
   - Select **Create**.

4. To create the **test** environment:
   - Return to the **Environments** page.
   - Select **New environment**.
   - Under **Name**, enter **test**.
   - Select **Create**.

5. To create the **staging** environment:
   - Return to the **Environments** page.
   - Select **New environment**.
   - Under **Name**, enter **staging**.
   - Select **Create**.

## Create a service connection

Here you create a service connection that enables Azure Pipelines to access your Azure subscription. Azure Pipelines uses this service connection to deploy the website to App Service. You created a similar service connection in the previous module.

> **Important**
> 
> Make sure that you're signed in to both the Azure portal and Azure DevOps under the same Microsoft account.

1. In Azure DevOps, go to your **Space Game - web - Deployment patterns** project.

2. From the bottom corner of the page, select **Project settings**.

3. Under **Pipelines**, select **Service connections**.

4. Select **New service connection**, then choose **Azure Resource Manager**, then select **Next**.

5. Near the top of the page, **Service principal (automatic)**. Then select **Next**.

6. Fill in these fields:

   | Field | Value |
   |-------|-------|
   | Scope level | Subscription |
   | Subscription | Your Azure subscription |
   | Resource Group | tailspin-space-game-rg |
   | Service connection name | Resource Manager - Tailspin - Space Game |

   During the process, you might be prompted to sign in to your Microsoft account.

7. Ensure that **Grant access permission to all pipelines** is selected.

8. Select **Save**.

Azure DevOps performs a test connection to verify that it can connect to your Azure subscription. If Azure DevOps can't connect, you have the chance to sign in a second time.

## Fetch the branch from GitHub

Here you fetch the **blue-green** branch from GitHub. Then you check out, or switch to, that branch.

This branch contains the Space Game project that you worked with in the previous modules and an Azure Pipelines configuration to start with.

1. In Visual Studio Code, open the integrated terminal.

2. Run the following **git** commands to fetch a branch named **blue-green** from the Microsoft repository and to switch to that branch.

   **Bash**
   ```
   git fetch upstream blue-green
   git checkout -B blue-green upstream/blue-green
   ```

   The format of these commands enables you to get starter code from the Microsoft GitHub repository, known as **upstream**. Shortly, you'll push this branch up to your GitHub repository, known as **origin**.

3. As an optional step, open **azure-pipelines.yml** from Visual Studio Code. Familiarize yourself with the initial configuration.

   The configuration resembles the ones that you created in the previous modules in this learning path. It builds only the application's Release configuration. For brevity, it omits the triggers, manual approvals, and tests that you set up in previous modules.

   For learning purposes, this configuration promotes changes from any branch to Dev, Test, and Staging. A more robust approach might promote changes from only a release branch or main. You used this robust approach in the **Create a multistage pipeline by using Azure Pipelines** module.

## Run the pipeline and see the deployed website

Here you push the initial configuration to GitHub so that you're up to date with the team. Later, you'll add a slot to the Staging environment so that you can implement a blue-green deployment.

1. In Visual Studio Code, open the integrated terminal.

2. Run the following **git commit** command to add an empty entry to your commit history.

   **Bash**
   ```
   git commit --allow-empty -m "Trigger the pipeline"
   ```

   This step is for learning purposes. It isn't typical. We provide starter code that you don't need to modify now. The **--allow-empty** flag ensures that the next step successfully pushes the branch to GitHub and triggers Azure Pipelines to run.

   If you omitted this step, then the **git push** command that you run in the next step wouldn't take any action. So it wouldn't trigger Azure Pipelines to run.

3. Run the following **git push** command to upload the branch to your GitHub repository.

   **Bash**
   ```
   git push origin blue-green
   ```

4. In Azure Pipelines, go to the build. Then trace the build as it runs. When prompted, select **Permit** to grant deployment permissions to the different stages.

5. After your pipeline run has been completed, navigate to the summary page to see your pipeline status.

 ![](https://learn.microsoft.com/en-us/training/azure-devops/manage-release-cadence/media/3-stages-complete.png)

7. Navigate to the URL that corresponds to each stage. Your web app should be deployed to each environment.

   ![[](https://learn.microsoft.com/en-us/training/azure-devops/manage-release-cadence/media/3-app-service-dev.png)


# 5.4 Exercise - Implement the blue-green deployment pattern


In Create a multistage pipeline by using Azure Pipelines, you built a basic deployment pipeline that deploys a web application to Azure App Service in these stages: Dev, Test, and Staging.

Here you add to that workflow by applying the blue-green deployment pattern during Staging.

To do so, you:

- Add a deployment slot to the App Service instance that corresponds to Staging.
- Add a task to the pipeline to swap the deployment slots.

## Add a deployment slot

Here you add a deployment slot to the App Service instance that corresponds to Staging.

By default, every App Service instance provides a default slot, named production. You deployed to the production slot when you set up the pipeline in the previous section.

An App Service instance can have multiple slots. Here you add a second deployment slot to the App Service instance that corresponds to Staging. The deployment slot is named swap.

### To add the slot:

1. Go to the Azure portal and sign in.

2. On the menu, select Cloud Shell. When you're prompted, select the Bash experience.

3. Run the following command to get the name of the App Service instance that corresponds to Staging and to store the result in a Bash variable that's named staging.

   **Azure CLI**
   ```bash
   staging=$(az webapp list \
     --resource-group tailspin-space-game-rg \
     --query "[?contains(@.name, 'tailspin-space-game-web-staging')].{name: name}" \
     --output tsv)
   ```

   The `--query` argument uses JMESPath, which is a query language for JSON. The argument selects the App Service instance whose name field contains "tailspin-space-game-web-staging".

4. Print the staging variable to verify that you get the correct name.

   **Bash**
   ```bash
   echo $staging
   ```

   Here's an example of the output:

   **Output**
   ```
   tailspin-space-game-web-staging-1234
   ```

5. Run the following command to add a slot named swap to your staging environment.

   **Azure CLI**
   ```bash
   az webapp deployment slot create \
     --name $staging \
     --resource-group tailspin-space-game-rg \
     --slot swap
   ```

6. Run the following command to list your deployment slot's host name.

   **Azure CLI**
   ```bash
   az webapp deployment slot list \
       --name $staging \
       --resource-group tailspin-space-game-rg \
       --query [].hostNames \
       --output tsv
   ```

   The result resembles this output:

   **Output**
   ```
   tailspin-space-game-web-staging-25391-swap.azurewebsites.net
   ```

   Make note of this host name for later.

7. As an optional step, go to your site in a browser. You see the default home page because you haven't yet deployed your code to this slot.

 
 ![](https://learn.microsoft.com/en-us/training/azure-devops/manage-release-cadence/media/3-app-service-dev.png)

By default, a deployment slot is accessible from the internet. In practice, you could configure an Azure virtual network that places your swap slot in a network that's not routable from the internet but that only your team can access. Your production slot would remain reachable from the internet.

## Swap deployment slots in Staging

Here you use the `AzureAppServiceManage@0` task to swap deployment slots in your Staging environment.

You can also use this task to start, stop, or delete a slot. Or you can use it to install site extensions or to enable continuous monitoring on App Service.

1. In Visual Studio Code, modify `azure-pipelines.yml` by using this code:

   > **Tip**  
   > You can replace the entire file or just update the part that's highlighted.

   **yml**
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

   - stage: 'Dev'
     displayName: 'Deploy to the dev environment'
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
                 appName: '$(WebAppNameDev)'
                 package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/*.zip'

   - stage: 'Test'
     displayName: 'Deploy to the test environment'
     dependsOn: Dev
     jobs:
     - deployment: Deploy
       pool:
         vmImage: 'ubuntu-20.04'
       environment: test
       variables:
       - group: 'Release'
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
                 appName: '$(WebAppNameTest)'
                 package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/*.zip'

   - stage: 'Staging'
     displayName: 'Deploy to the staging environment'
     dependsOn: Test
     jobs:
     - deployment: Deploy
       pool:
         vmImage: 'ubuntu-20.04'
       environment: staging
       variables:
       - group: 'Release'
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
                 deployToSlotOrASE: 'true'
                 resourceGroupName: 'tailspin-space-game-rg'
                 slotName: 'swap'
                 appName: '$(WebAppNameStaging)'
                 package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/*.zip'
             - task: AzureAppServiceManage@0
               displayName: 'Swap deployment slots'
               inputs:
                 azureSubscription: 'Resource Manager - Tailspin - Space Game'
                 resourceGroupName: 'tailspin-space-game-rg'
                 webAppName: '$(WebAppNameStaging)'
                 sourceSlot: 'swap'
                 targetSlot: 'production'
                 action: 'Swap Slots'
   ```

   Note these changes:

   - The `AzureWebApp@1` task now specifies these values:
     - `deployToSlotOrASE`, when set to true, deploys to an existing deployment slot.
     - `resourceGroupName` specifies the name of the resource group. This value is required when `deployToSlotOrASE` is true.
     - `slotName` specifies the name of the deployment slot. Here you deploy to the slot that's named swap.
   - The new task, `AzureAppServiceManage@0`, swaps the deployment slots.
     - `sourceSlot` and `targetSlot` specify the slots to swap.
     - `action` specifies the action to take. Recall that you can use this task to start, stop, or delete a slot. Here, "Swap Slots" specifies to swap the source and target slots.

   This configuration always deploys to the swap slot. It then swaps the production and swap slots. The swap process ensures that production points to the more recent deployment.

2. In the integrated terminal, add `azure-pipelines.yml` to the index. Commit the changes, and then push the branch up to GitHub.

   > **Tip**  
   > Save `azure-pipelines.yml` before you run these Git commands.

   **Bash**
   ```bash
   git add azure-pipelines.yml
   git commit -m "Swap deployment slots"
   git push origin blue-green
   ```

3. In Azure Pipelines, trace the build through each of the steps.

   > **Note**  
   > If your run into the following error ...'staging' slot did not respond to http ping. (CODE: 417) try restarting your app service. If the problem persists, reset auto swap for your slot.

4. As an optional step, in a browser, go to the URL that corresponds to each stage.

   Although you haven't yet made changes to the website, you see that the Space Game website successfully deployed to each App Service environment.

   ![Screenshot of a browser that shows the Space Game website in the Dev environment.](#)


# 5.5 Exercise - Push a change through the pipeline

In this part, you see your deployment slots in action. On the website's home page, you change the background color and the text on the hero banner. You then push your changes to GitHub, watch the pipeline run, and verify the changes.

To further practice the process, you then revert your changes and watch the pipeline run as a way of rolling forward.

## Change the text on the hero banner

Here you change the text on the hero banner. Later you'll see the change when you deploy to App Service.

1. In Visual Studio Code, in the `Tailspin.SpaceGame.Web/Views/Home` directory, open `Index.cshtml`.

2. Look for this text near the top of the page:

   **HTML**
   ```html
   <p>An example site for learning</p>
   ```

   > **Tip**  
   > Visual Studio Code provides a way to search for text in files. To access the search pane, select the magnifying glass icon in the side pane.

3. Replace the example text with the following text, and then save the file.

   **HTML**
   ```html
   <p>Welcome to the official Space Game site!</p>
   ```

## Change the background color

Here you change the background color of the hero banner from gray to green.

1. In Visual Studio Code, in the `Tailspin.SpaceGame.Web/wwwroot/css` directory, open `site.scss`.

   > **Important**  
   > Open `site.scss`, not `site.css`. The Build stage runs node-sass to convert `site.scss` (a Sass file) to `site.css` (a standard CSS file).

2. Locate the following code near the top of the file:

   **css**
   ```css
   .intro {
     height: 350px;
     background-color: #666;
     background-image: url('/images/space-background.svg');
     background-size: 1440px;
     background-position: center top;
     background-repeat: no-repeat;
     background-attachment: fixed;
   ```

3. In the code, replace the highlighted text as shown in the following example. Then save the file.

   **css**
   ```css
   .intro {
     height: 350px;
     background-color: green;
     background-image: url('/images/space-background.svg');
     background-size: 1440px;
     background-position: center top;
     background-repeat: no-repeat;
     background-attachment: fixed;
   ```

## Push the change through the pipeline

Normally you would build and run the site locally to verify the change. You might also run any associated unit tests to verify that your change doesn't break existing functionality.

For brevity, here you commit the changes to your branch, push your branch to GitHub, and watch the pipeline run.

1. Add `Index.cshtml` and `site.scss` to the index, commit the changes, and then push the changes up to GitHub.

   **Bash**
   ```bash
   git add Tailspin.SpaceGame.Web/Views/Home/Index.cshtml Tailspin.SpaceGame.Web/wwwroot/css/site.scss
   git commit -m "Change text and colors on the home page"
   git push origin blue-green
   ```

2. In Azure Pipelines, trace the build through each step.

3. Go to the URL that corresponds to the production slot for your Staging environment. This slot is the default slot that you configured when you set up the pipeline earlier.

   You see that the deployed website shows the color and text changes.

    ![](https://learn.microsoft.com/en-us/training/azure-devops/manage-release-cadence/media/5-app-service-staging.png)

5. Go to the URL that corresponds to the swap slot for your Staging environment. The URL includes "-swap.azurewebsites.net" in its name.

   You see the previous version of the website, without the color and text changes.

    ![](https://learn.microsoft.com/en-us/training/azure-devops/manage-release-cadence/media/5-app-service-staging-swap.png)

   You see no changes because you swapped the production slot and the swap slot. In other words, here you always deploy to the swap slot, and then you swap the production slot and swap slot. The swap process ensures that the production slot points to the more recent deployment.

## Revert the change

Let's say that you deployed a change that you want to revert. At this point, you could roll back the change by swapping the production slot and swap slot again. For example, you could swap the slots manually through the Azure portal. Or, instead of rolling back the changes, you could roll forward by pushing another change through the pipeline.

That's what you'll do here. You'll revert your latest code changes and push another change through the pipeline. To do so, you use the `git revert` command.

In Git, you seldom remove commits from a file's history. Unlike the "undo" operation in a text editor, the `git revert` command creates a new commit that's essentially the opposite of the specified set of commits. To see the commits, you first run the `git log` command to trace your commit history during the revert process.

1. In your terminal, run the following `git log` command to view your commit history.

   **Bash**
   ```bash
   git --no-pager log --oneline
   ```

   Your output resembles the following code example. In your output, you'll see additional commits and different commit IDs.

   **Output**
   ```
   d6130b0 (HEAD -> blue-green, origin/blue-green) Change text and colors on the home page
   ce56955 Swap deployment slots
   0d6a123 Trigger the pipeline
   ```

   In the output, trace the commit history. The latest commit is on top.

2. Run the following `git revert` command to revert by one commit.

   **Bash**
   ```bash
   git revert --no-edit HEAD
   ```

   Think of HEAD as the current state of your branch. HEAD refers to the latest commit. This command specifies to revert only the HEAD, or latest, commit.

3. Run `git log` again to see your updated commit history.

   **Bash**
   ```bash
   git --no-pager log --oneline
   ```

   At the top of your output, you see an additional commit that reverts the previous commit. Here's an example:

   **Output**
   ```
   e58896a (HEAD -> blue-green) Revert "Change text and colors on the home page"
   d6130b0 (origin/blue-green) Change text and colors on the home page
   ce56955 Swap deployment slots
   0d6a123 Trigger the pipeline
   ```

## Push the reverted change through the pipeline

Here you push your reverted change through the pipeline and see the results.

1. Run the following `git push` command to upload the blue-green branch to your GitHub repository.

   **Bash**
   ```bash
   git push origin blue-green
   ```

2. In Azure Pipelines, go to the build. Trace the build as it runs.

3. Go to the URLs that correspond to the swap slot and production slot for your Staging environment.

   The production slot now points to your reverted change, which is the original website.

   ![Screenshot of a browser that shows the original Space Game website after reverting the changes. The website doesn't include the color and text changes.](#)

   The swap slot now points to the previous change.

   ![Screenshot of a browser that shows the Space Game website after reverting the change. The website shows the color and text changes.](#)

Great work! The team now has a way to automate the releases. They can get new features to their users without incurring downtime.

---

## Team meeting

The team gathers to demo the pipeline. This time, Tim pushes a change through the pipeline while everyone watches. But not everyone's convinced.

**Andy:** It's great seeing deployment slots at work. But I don't get it. How do we benefit from zero-downtime deployments here? Staging is only for our team and management.

**Tim:** Indeed, we won't see much benefit right now. But imagine when we apply blue-green deployments to a Production stage. We'll still have the manual approval from management before we promote to Production. But when we do release new features, the swap process will make the rollout nearly instantaneous. It will be seamless to our users.

**Andy:** OK, I think I understand now. I like this improvement. The system of deployment slots was easy to set up, and it will benefit our users. Everyone wins.

**Amita:** Speaking of improvements, why don't we revisit our value-stream mapping exercise we did a few weeks ago? I bet we'll see progress in how quickly we can release new features.

**Mara:** Great, let's put that on the agenda for our next team meeting.




# 5.6 Exercise - Clean up your environment


You're done with the tasks for this module. Here you clean up your Azure resources, move the work item to the Done state in Azure Boards, and then clean up your Azure DevOps environment.

> **Important**  
> This page contains important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes. It also helps ensure that you're not charged for Azure resources after you complete this module.

## Clean up Azure resources

Here you delete your Azure App Service instances. The easiest way to do that is to delete their parent resource group. Deleting a resource group deletes all resources in that group.

### To clean up your resource group:

1. Go to the Azure portal and sign in.

2. From the menu, select Cloud Shell. When you're prompted, select the Bash experience.

  
   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-portal-menu-cloud-shell.png)

4. Run the following `az group delete` command to delete the resource group that you used in this module, `tailspin-space-game-rg`.

   **Azure CLI**
   ```bash
   az group delete --name tailspin-space-game-rg
   ```

   When you're prompted, confirm the operation by entering `y`.

5. As an optional step, after the previous command finishes, run the following `az group list` command.

   **Azure CLI**
   ```bash
   az group list --output table
   ```

   You see that the resource group `tailspin-space-game-rg` no longer exists.

## Move the work item to Done

Earlier in this module, you assigned the **Improve release cadence** work item to yourself. Here you move that work item to the **Done** column.

In practice, "Done" often means putting working software into the hands of your users. For learning purposes, here you mark this work as complete because you can now choose a deployment pattern that enables you to release changes more quickly to your users.

At the end of each sprint, or work iteration, your team might want to hold a retrospective meeting. In the meeting, you can share the work that you completed in the sprint, what went well, and what could be improved.

### To complete the work item:

1. In Azure DevOps, go to **Boards**, and then select **Boards** from the menu.

2. Move the **Improve release cadence** work item from the **Doing** column to the **Done** column.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/manage-release-cadence/media/5-azure-boards-wi5-done.png)

## Disable the pipeline or delete your project

Each module in this learning path provides a template that you run to create a clean environment for the module.

Running multiple templates gives you multiple Azure Pipelines projects. Each project points to the same GitHub repository. This setup can trigger multiple pipelines to run each time you push a change to your GitHub repository. These pipeline runs can consume free build minutes on our hosted agents. So it's important to disable or delete your pipeline before you move to the next module.

Choose one of the following options.

### Option 1: Disable the pipeline

Here you disable the pipeline so that it processes no further build requests. You can reenable the build pipeline later if you want to. Choose this option if you want to keep your DevOps project and your build pipeline for future reference.

#### To disable the pipeline:

1. In Azure Pipelines, navigate to your pipeline.

2. From the drop-down menu, select **Settings**:

      ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-pipelines-settings-button.png)

4. Under **Processing of new run requests**, select **Disabled** and then select **Save**.

   Your pipeline will no longer process build requests.

### Option 2: Delete the Azure DevOps project

Here you delete your Azure DevOps project, including what's in Azure Boards and your build pipeline. In future modules, you can run another template that brings up a new project in a state where this module leaves off. Choose this option if you don't need your DevOps project for future reference.

#### To delete the project:

1. In Azure DevOps, go to your project. Earlier we recommended that you name this project **Space Game - web - Deployment patterns**.

2. Select **Project settings** in the lower corner.

3. At the bottom of the **Project details** area, select **Delete**.


   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-delete-project.png)

5. In the window that appears, enter the project name, and then select **Delete** again.

   Your project is now deleted.


# 5.7 Summary

In this module, you defined a deployment pattern as an automated way to smoothly roll out new application features to your users. A good deployment pattern can help you minimize downtime. It can also enable you to roll out new features progressively to your users.

You can choose from several deployment patterns. The deployment pattern you choose depends on your reasons for the deployment and your resources. Do you have canary testers in place? Will you employ a dark launch and choose testers who don't know that they're testers? If you have a trusted set of testers that progressively increases from a small set to a larger set, then you could choose a progressive-exposure deployment. Or, if you want to know if one version performs better than another version, you could choose A/B testing.

The Tailspin team chose to implement the blue-green deployment pattern, using deployment slots in Azure App Service. Deployment slots are live apps that have their own host names. The team can swap two deployment slots. By swapping, they can promote changes to production instantly. Although the team isn't ready to release their website to the public, they've proven that they can get new features to their users without incurring downtime.

As a bonus, in this module you also learned how to roll forward an unintended change by reverting a Git commit and then pushing the reverted change through the pipeline.

## How is the team measuring up?

In the **Assess your existing software development process** module, Mara did a value-stream mapping exercise. The exercise helped the team analyze their current release-cycle process.

Recall that the activity ratio, or efficiency, is process time divided by total lead time:

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mrow data-mjx-texclass="ORD">
    <mi>A</mi>
    <mi>c</mi>
    <mi>t</mi>
    <mi>i</mi>
    <mi>v</mi>
    <mi>i</mi>
    <mi>t</mi>
    <mi>y</mi>
    <mtext>&#xA0;</mtext>
    <mi>r</mi>
    <mi>a</mi>
    <mi>t</mi>
    <mi>i</mi>
    <mi>o</mi>
    <mtext>&#xA0;</mtext>
    <mo>=</mo>
    <mtext>&#xA0;</mtext>
  </mrow>
  <mrow data-mjx-texclass="ORD">
    <mstyle displaystyle="true" scriptlevel="0">
      <mfrac>
        <mrow>
          <mi>P</mi>
          <mi>r</mi>
          <mi>o</mi>
          <mi>c</mi>
          <mi>e</mi>
          <mi>s</mi>
          <mi>s</mi>
          <mtext>&#xA0;</mtext>
          <mi>t</mi>
          <mi>i</mi>
          <mi>m</mi>
          <mi>e</mi>
        </mrow>
        <mrow>
          <mi>T</mi>
          <mi>o</mi>
          <mi>t</mi>
          <mi>a</mi>
          <mi>l</mi>
          <mtext>&#xA0;</mtext>
          <mi>l</mi>
          <mi>e</mi>
          <mi>a</mi>
          <mi>d</mi>
          <mtext>&#xA0;</mtext>
          <mi>t</mi>
          <mi>i</mi>
          <mi>m</mi>
          <mi>e</mi>
        </mrow>
      </mfrac>
    </mstyle>
  </mrow>
</math>




The Tailspin web team initially used this metric to determine that they were 23 percent efficient.

The team first reduced some inefficiencies when they implemented continuous integration (CI). By applying continuous delivery (CD), they have now reduced inefficiencies even further.

In previous learning paths, the team reduced:

- **The time it takes to set up source control for new features.** The required time went from three days to zero days.

  The team achieved this improvement by moving from centralized source control to Git, a form of distributed source control. By using distributed source control, they don't need to wait for files to be unlocked.

- **The time it takes to deliver code to Amita, the tester.** The required time went from two days to zero days.

  The team achieved this improvement by moving their build process to Azure Pipelines. Azure Pipelines automatically notifies Amita when a build is available. Developers no longer need to update Amita's spreadsheet to notify her.

- **The time it takes Amita to test new features.** The required time went from three days to one day.

  The team achieved this improvement by unit-testing their code. They run unit tests each time a change moves through the build pipeline, so fewer bugs and regressions reach Amita. The reduced workload means that Amita can complete each manual test faster.

The release pipeline that you and the team built in this learning path reduced:

- **The time it takes to get the build into the Test stage.** The required time went from three days to one day.

  The team achieved this by using a scheduled trigger to deploy to Test every day at 3:00 AM.

- **The time it takes to get the tested build into Staging.** The required time went from two days to zero days.

  The team achieved this improvement by adding Selenium UI tests, a form of functional testing, to the Test stage. These automated tests are much faster than the manual versions.

- **The time it takes to get the approved build from Staging to live.** The required time went from one day to less than one day.

  The team achieved this improvement by adding manual approval checks to the pipeline. When management signs off, Tim can release the changes from Staging to live.

These changes reduce the total lead time from 22 days to 10 days. When we substitute these numbers into the equation:


  <mrow data-mjx-texclass="ORD">
    <mi>A</mi>
    <mi>c</mi>
    <mi>t</mi>
    <mi>i</mi>
    <mi>v</mi>
    <mi>i</mi>
    <mi>t</mi>
    <mi>y</mi>
    <mtext>&#xA0;</mtext>
    <mi>r</mi>
    <mi>a</mi>
    <mi>t</mi>
    <mi>i</mi>
    <mi>o</mi>
    <mtext>&#xA0;</mtext>
    <mo>=</mo>
    <mtext>&#xA0;</mtext>
  </mrow>
  <mrow data-mjx-texclass="ORD">
    <mstyle displaystyle="true" scriptlevel="0">
      <mfrac>
        <mrow>
          <mn>5</mn>
          <mtext>&#xA0;</mtext>
          <mi>d</mi>
          <mi>a</mi>
          <mi>y</mi>
          <mi>s</mi>
        </mrow>
        <mrow>
          <mn>10</mn>
          <mtext>&#xA0;</mtext>
          <mi>d</mi>
          <mi>a</mi>
          <mi>y</mi>
          <mi>s</mi>
        </mrow>
      </mfrac>
    </mstyle>
  </mrow>
  <mrow data-mjx-texclass="ORD">
    <mo>=</mo>
    <mn>0.50</mn>
  </mrow>
</math>



Multiply the result by 100 percent, and we get a 50 percent reduction.

Although there's always room for improvement, this change is a win for the team. Not only do customers get value more quickly, the Tailspin team now spends less time waiting and more time doing what they enjoy most: delivering features that they know their customers will love.

---

## Learn more

Use these additional resources to learn more about App Service, deployment slots, and rolling back changes:

- [App Service documentation](#)
- [Deploy a website to Azure by using App Service](#)
- [Stage a web app deployment for testing and rollback by using App Service deployment slots](#)
- [Set up staging environments in App Service](#)


# 6 Automate Azure Functions deployments with Azure Pipelines

Create an Azure DevOps pipeline that builds and deploys an ASP.NET web app and an Azure Function app to Azure.

### Learning objectives
After completing this module, you'll be able to:
- Describe when to use Azure Functions for app development projects
- Create Azure App Service and Azure Functions environments
- Deploy to Azure App Service and Azure Functions simultaneously with Azure Pipelines
#### Prerequisites
- Ability to create a basic Azure DevOps pipeline and an understanding of the components of a pipeline (tasks, stages, jobs)
- Ability to navigate the Azure portal and run Cloud Shell commands
- An Azure subscription
- An Azure DevOps organization with access to parallel jobs
- A GitHub account


# 6.1 Introduction

In the **Create a release pipeline with Azure Pipelines** learning path, you built a basic release pipeline that deployed an ASP.NET Core application to Azure App Service. Although that scenario works for a single application, modern solutions often require a combination of applications, services, and other components. This module shows you how to build a more complicated pipeline.

In this module, you learn how to add an Azure Functions project to an existing CI/CD pipeline and deploy to both Azure App Service and Azure Functions in a single process. This module focuses on the core build and deployment tasks.

## Learning objectives

After completing this module, you'll be able to:

- Describe when to use Azure Functions for app development projects
- Create Azure App Service and Azure Functions environments
- Deploy to both Azure App Service and Azure Functions in a single pipeline with Azure Pipelines

## Prerequisites

The modules in this learning path form a progression:

- Get started with Azure DevOps
- Build applications with Azure DevOps

This module also assumes you have basic familiarity with Azure Functions. That knowledge isn't required to complete the module. If you're new to Azure Functions, you can complete the **Create serverless applications** learning path first.

## Meet the team

You met the *Space Game* web team at Tailspin Toys in previous modules. As a refresher, here's who you work with in this module.

**Andy** is the development lead.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/andy.png)

**Irwin** is the product manager.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/irwin.png)

**Tim** is in operations.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/tim.png)

**Mara** just joined as a developer and reports to Andy.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/mara.png)

Mara has prior experience with DevOps. Mara is helping the team adopt a more automated process that uses Azure DevOps.



# 6.2 What is Azure Functions?


You follow the Tailspin Space Game web team as they discuss how to best deliver on new marketing requirements driven by management. The team needs to integrate some serverless technology, specifically Azure Functions, into their DevOps process.

You can check in with the team.

## The new requirements

**Irwin:** Thanks for meeting on such short notice. Things are heating up, and the marketing team has made some promises that could complicate things for all of us. They really like our site. They think the leaderboard can be used to promote the game as we head toward the final launch and beyond. They want to scale it out way beyond what we'd originally planned.

**Mara:** That's great, right? We're on Azure, so we can scale out the service as much as needed.

**Irwin:** They just want the ability for anyone to integrate leaderboard data into their own applications. They think it would be really cool to have the same leaderboard options on our site, in the game, on gaming-review sites, and even on external blogs and personal sites. One challenge is that the game engine team currently owns the production database that we pull leaderboard data from. They think they should build and own the API moving forward.

**Andy:** Mara, do you have any thoughts?

**Mara:** I'm sure we can come up with something. Here are my notes:

- We need to deliver quickly, so we have to find a solution where we can use our code and skills.
- We need to refactor a small piece of functionality into an independent service.
- We need to minimize administrative overhead in production.
- We need to have massive scale without making a massive commitment.

The team nods in agreement.

## It works on my machine

The meeting breaks up. The next morning, Andy excitedly pops into Mara's office for an impromptu chat.

**Andy:** I've got it! I found a solution that meets all of our requirements for the leaderboard API. It's a serverless offering called Azure Functions.

**Mara:** That's great! How long before we have something we can demo?

**Andy:** I have already spiked something out. I forked our GitHub repo and refactored the leaderboard code into a new Azure Functions project. It exposes the leaderboard data via a simple HTTP GET request. I also updated the web site to use that endpoint when requesting the leaderboard, and anyone else can do the same.

**Mara:** This sounds like exactly what we need. I can help extend the existing CI/CD pipeline to support building and deploying it like we do for the main site project.

> **Note**  
> This module doesn't focus on how to connect your app to Azure Functions. If you're interested, review the source code. The code uses the Azure Functions runtime for C# to read leaderboard data from Azure Functions.

## What is Azure Functions?

Azure Functions is a specific offering within the broader spectrum of Azure serverless computing technologies. It provides an easy way for developers to build straightforward functions that exist in a stateless, serverless environment. Functions can be triggered using various methods, such as HTTP requests, changes to data in storage, and receipt of a message from a queue. You can learn more about the trigger bindings in Azure Functions triggers and bindings concepts.

The Tailspin team selected Azure Functions for this scenario because it met all their needs:

- **We need to deliver quickly, so we have to find a solution where we can use our code and skills.**  
  We can build the solution quickly as an ASP.NET Core application applying code we already have.

- **We need to refactor a small piece of functionality into an independent service.**  
  We can deliver an independent function with no other application surface area to worry about.

- **We need to minimize administrative overhead in production.**  
  Azure Functions removes the need to worry about hosting environments.

- **We need to have massive scale without making a massive commitment.**  
  Serverless technologies have virtually unlimited scale that can automatically ramp up and down faster than virtual machines or app services.

Azure Functions and other serverless technologies aren't always the right fit for every solution. Later on, learn about where you can find resources to help you select the right technology for the job.

---

## Check your knowledge

### 1. Which of these projects is a good candidate for serverless computing?

- **✅ A service that recognizes people in images.**
- ❌ A peer-to-peer file sharing network.
- ❌ A service that manages an online shopping cart.

**Explanation:** Image recognition is a perfect use case for serverless computing because it's event-driven, stateless, and has variable workloads. Peer-to-peer networks require persistent connections, and shopping carts need state management, making them less suitable for pure serverless architectures.

### 2. Which of the following isn't a good reason to use Azure Functions?

- ❌ They don't require any special configuration to be massively scalable.
- ❌ They can be written in virtually any mainstream language.
- **✅ They're a replacement for app services and virtual machines.**

**Explanation:** Azure Functions are not a universal replacement for all hosting options. They're designed for specific use cases like event-driven, stateless workloads. Complex applications with persistent state, long-running processes, or specific infrastructure requirements may be better suited for App Services or VMs.

### 3. Which of the following isn't a supported way to directly trigger an Azure Functions app?

- ❌ Making an HTTP request over the public Internet.
- ❌ Detecting a new message on a message queue.
- **✅ Receiving a carefully filled-out form via fax machine.**

**Explanation:** Azure Functions support various digital triggers like HTTP requests, queue messages, database changes, timer schedules, etc. However, physical fax machines are not supported as direct triggers since they're not part of the digital cloud ecosystem.


# 6.3 Exercise - Set up your Azure DevOps environment

In this unit, make sure that your Azure DevOps organization is set up to complete the rest of this module. You also create the Azure App Service environments that you deploy to.

To accomplish these goals, you do these tasks:

- Add a user to ensure Azure DevOps can connect to your Azure subscription.
- Set up an Azure DevOps project for this module.
- On Azure Boards, move the work item for this module to the Doing column.
- Make sure your project is set up locally so that you can push changes to the pipeline.
- Create the Azure App Service and Azure Functions app using the Azure CLI in Azure Cloud Shell.
- Create pipeline variables that define the names of your App Service and Azure Functions instance.
- Create a service connection that enables Azure Pipelines to securely access your Azure subscription.

## Add a user to Azure DevOps

To complete this module, you need your own Azure subscription. You can get started with Azure for free.

Although you don't need an Azure subscription to work with Azure DevOps, this exercise uses Azure DevOps to deploy to Azure resources in your Azure subscription. To simplify the process, use the same Microsoft account to sign in to both your Azure subscription and your Azure DevOps organization.

> **Important**  
> If you sign in with different accounts, add a user to your DevOps organization under the Microsoft account that you use to sign in to Azure. For more information, see Add users to your organization or project. When you add the user, choose the Basic access level.
>
> Then, sign out of Azure DevOps and sign in with the new user account. Use the Microsoft account that you use to sign in to your Azure subscription.

## Get the Azure DevOps project

Make sure that your Azure DevOps organization is set up to complete the rest of this module. To do so, run a template that creates a project in Azure DevOps.

The modules in this learning path form a progression as you follow the Tailspin web team through their DevOps journey. For learning purposes, each module has its own Azure DevOps project.

### Run the template

Run a template that sets up your Azure DevOps organization.

1. Get and run the ADOGenerator project in Visual Studio or the IDE of your choice.

2. When prompted to **Enter the template number from the list of templates**, enter **38** for **Automate Azure Function deployments with Azure Pipelines**, then press Enter.

3. Choose your authentication method. You can set up and use a Personal Access Token (PAT) or use device login.

   > **Note**  
   > If you set up a PAT, make sure to authorize the necessary scopes. For this module, you can use Full access, but in a real-world situation, you should grant only the necessary scopes.

4. Enter your Azure DevOps organization name, then press Enter.

5. If prompted, enter your Azure DevOps PAT, then press Enter.

6. Enter a project name such as **Space Game - web - Azure Functions**, then press Enter.

7. After your project is created, go to your Azure DevOps organization in your browser (at `https://dev.azure.com/<your-organization-name>/`) and select the project.

### Fork the repository

If you haven't already, create a fork of the `mslearn-tailspin-spacegame-web-azure-functions` repository.

1. On GitHub, go to the [mslearn-tailspin-spacegame-web-azure-functions](https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web-azure-functions) repository.

2. Select **Fork** at the top-right of the screen.

3. Choose your GitHub account as the Owner, then select **Create fork**.

> **Important**  
> The **Clean up your Azure DevOps environment** page in this module contains important steps that you must complete, even if you don't complete this module. Cleaning up helps ensure that you don't run out of free build minutes.

### Set your project's visibility

Initially, your fork of the Space Game repository on GitHub is set to public while the project created by the Azure DevOps template is set to private. A public repository on GitHub can be accessed by anyone, while a private repository is only accessible to you and the people you choose to share it with. Similarly, on Azure DevOps, public projects provide read-only access to non-authenticated users, while private projects require users to be granted access and authenticated to access the services.

At the moment, it is not necessary to modify any of these settings for the purposes of this module. However, for your personal projects, you must determine the visibility and access you wish to grant to others. For instance, if your project is open source, you may choose to make both your GitHub repository and your Azure DevOps project public. If your project is proprietary, you would typically make both your GitHub repository and your Azure DevOps project private.

Later on, you may find the following resources helpful in determining which option is best for your project:

- [Use private and public projects](#)
- [Change project visibility to public or private](#)
- [Setting repository visibility](#)

## Assign a work item and move it to the Doing state

Here, you assign a work item to yourself on Azure Boards and set the work item state to **Doing**. In practice, you and your team would create work items at the start of each sprint, or work iteration.

This exercise creates a checklist from which to work. It gives other team members visibility into what you're working on and how much work is left. The work item also helps enforce work-in-progress (WIP) limits so that the team doesn't take on too much work at one time.

1. From Azure DevOps, navigate to **Boards** category, and then select **Boards** from the menu.

     ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-boards-menu.png)

3. Open the **Refactor leaderboard API as an Azure Function** work item by selecting the title. Assign this work item to yourself, and then select **Save & Close**.

4. Select the down arrow at the bottom of the card and select **Doing** or select the card and drag it to the **Doing** column.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-boards-down-chevron.png)

   The work item is moved from the **To Do** column to the **Doing** column.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-azure-functions/media/3-azure-boards-wi1-doing.png)

At the end of this module, move the card to the **Done** column after you complete the task.

## Create the Azure App Service and Azure Functions environments

Here, you create the App Service and Azure Functions app required to deploy the new version of the site and API.

In the **Create a release pipeline with Azure Pipelines** Learn module, you brought up App Service through the Azure portal. Although the portal is a great way to explore what's available on Azure or to do basic tasks, bringing up components such as App Service can be tedious.

In this module, you use the Azure CLI to bring up an App Service instance. You can access the Azure CLI from a terminal or through Visual Studio Code. Used Azure CLI from Azure Cloud Shell. This browser-based shell experience is hosted in the cloud. In Cloud Shell, the Azure CLI is configured for use with your Azure subscription.

> **Important**  
> You need your own Azure subscription to complete the exercises in this module.

### Bring up Cloud Shell through the Azure portal

1. Sign in to the [Azure portal](https://portal.azure.com).

2. From the global controls in the page header, select **Cloud Shell**.

  ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-portal-menu-cloud-shell.png)

   A terminal opens and connects to the Azure Cloud Shell.

4. If necessary, select **Bash** from the terminal menu.

   > **Note**  
   > Cloud Shell requires an Azure storage resource to persist any files that you create in Cloud Shell. When you first open Cloud Shell, you're prompted to create a resource group, storage account, and Azure Files share. This setup is automatically used for all future Cloud Shell sessions.

### Select an Azure region

A region is one or more Azure datacenters within a geographic location. East US, West US, and North Europe are examples of regions. Every Azure resource, including an App Service instance, is assigned a region.

To make commands easier to run, start by setting a default region. After you specify the default region, commands you enter use that region until you specify a different region.

1. From Cloud Shell, run the following `az account list-locations` command to list the regions that are available from your Azure subscription:

   **Azure CLI**
   ```bash
   az account list-locations \
     --query "[].{Name: name, DisplayName: displayName}" \
     --output table
   ```

2. From the **Name** column in the output, choose a region that's close to you. For example, choose `eastasia` or `westus2`.

3. Run `az configure` to set your default region. Replace `<REGION>` with the name of the region you chose.

   **Azure CLI**
   ```bash
   az configure --defaults location=<REGION>
   ```

   This example sets `westus2` as the default region:

   **Azure CLI**
   ```bash
   az configure --defaults location=westus2
   ```

### Create Bash variables

Here, create Bash variables to make the setup process more convenient and less error-prone. Using variables for shared text strings helps avoid accidental typos.

1. From Cloud Shell, generate a random number, which you use to create globally unique names for certain services in the next step.

   **Bash**
   ```bash
   resourceSuffix=$RANDOM
   ```

2. Create three globally unique names for your App Service, Azure Function, and storage accounts. These commands use double quotes, which instruct Bash to resolve the variables using inline syntax.

   **Bash**
   ```bash
   webName="tailspin-space-game-web-${resourceSuffix}"
   leaderboardName="tailspin-space-game-leaderboard-${resourceSuffix}"
   storageName="tailspinspacegame${resourceSuffix}"
   ```

3. Create two more Bash variables to store the names of your resource group and service plan.

   **Bash**
   ```bash
   rgName='tailspin-space-game-rg'
   planName='tailspin-space-game-asp'
   ```

### Create the Azure resources required

Your solution requires several Azure resources for deployment, which you create now.

> **Note**  
> This exercise uses the default network settings, so your site is accessible from the internet. In practice, you could configure an Azure virtual network to put your website in a network that only you and your team can access. Later, you could reconfigure your virtual network to make the website available to your users.

1. Run the following `az group create` command to create a resource group using the name defined earlier:

   **Azure CLI**
   ```bash
   az group create --name $rgName
   ```

2. Run the following `az appservice plan create` command to create an App Service plan using the name defined in the previous task:

   **Azure CLI**
   ```bash
   az appservice plan create \
     --name $planName \
     --resource-group $rgName \
     --sku B1 \
     --is-linux
   ```

   The `--sku` parameter specifies the B1 plan. This plan runs on the Basic tier. The `--is-linux` parameter specifies Linux workers (threads used in events and task scheduling).

   > **Important**  
   > If the B1 SKU isn't available in your Azure subscription, choose a different plan, such as S1 (Standard).

3. Run the following `az webapp create` command to create the App Service instance:

   **Azure CLI**
   ```bash
   az webapp create \
     --name $webName \
     --resource-group $rgName \
     --plan $planName \
     --runtime "DOTNETCORE|8.0"
   ```

4. Azure Functions requires a storage account for deployment. Run the following `az storage account create` command to create it:

   **Azure CLI**
   ```bash
   az storage account create \
     --name $storageName \
     --resource-group $rgName \
     --sku Standard_LRS
   ```

5. Run the following `az functionapp create` command to create the Azure Functions app instance. Replace the `<region>` with your preferred region.

   **Azure CLI**
   ```bash
   az functionapp create \
     --name $leaderboardName \
     --resource-group $rgName \
     --storage-account $storageName \
     --functions-version 4 \
     --consumption-plan-location <region>
   ```

6. Run the following `az webapp list` command to list the host name and state of the App Service instance:

   **Azure CLI**
   ```bash
   az webapp list \
     --resource-group $rgName \
     --query "[].{hostName: defaultHostName, state: state}" \
     --output table
   ```

   Note the host name for your running service. It should look similar to the following, but with a different random-number. You need the web host name later when you verify your work.

   **Output**
   ```
   HostName                                        State
   ----------------------------------------------  -------
   tailspin-space-game-web-4692.azurewebsites.net  Running
   ```

7. Run the following `az functionapp list` command to list the host name and state of the Azure Functions instance.

   **Azure CLI**
   ```bash
   az functionapp list \
     --resource-group $rgName \
     --query "[].{hostName: defaultHostName, state: state}" \
     --output table
   ```

   Note the host name for your running service. It should look similar to the following, but with a different random number identifier. You need the leaderboard host name later when you verify your work.

   **Output**
   ```
   HostName                                                State
   ------------------------------------------------------  -------
   tailspin-space-game-leaderboard-4692.azurewebsites.net  Running
   ```

8. Copy these two host names to a location you can easily access later.

9. As an optional step, open a browser and enter a host name to verify that it's running. The default home page appears.

> **Important**  
> The **Clean up your Azure DevOps environment** page in this module contains important cleanup steps. Cleaning up helps ensure that you're not charged for Azure resources after you complete this module. Be sure to perform the cleanup steps even if you don't complete this module.

## Create pipeline variables in Azure Pipelines

In the **Create a release pipeline with Azure Pipelines** module, you added a variable to your pipeline that stores the name of your web app in App Service. Here, do the same. Also, add the name of your leaderboard app for the Azure Functions instance.

You could hard-code these names in your pipeline configuration, but if you define them as variables, your configuration is more reusable. Plus, if the names of your instances change, you can update the variables and trigger your pipeline without modifying your configuration.

### Add a variable group to your project

1. Your **Space Game - web - Azure Functions** project should be open in Azure DevOps.

2. In the menu, select **Pipelines**, and then, under **Pipelines** select **Library**. The Library pane appears.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-azure-functions/media/3-pipelines-library.png)

4. In the command bar or in the middle of the pane, select **Variable group**. The **New variable group** page appears.

5. For the variable group name, enter **Release**.

6. Under **Variables**, select **Add**.

7. For the name of your variable, enter **WebAppName**. For the value, enter the name of the App Service instance that was created for your web app, such as `tailspin-space-game-web-4692`.

   > **Important**  
   > Set the name of the App Service instance, not its full host name. In this exercise, for example, `tailspin-space-game-web-4692` is the instance part of the host name `tailspin-space-game-web-4692.azurewebsites.net`.

8. Add another variable named **LeaderboardAppName** with the value of your leaderboard instance, for example, `tailspin-space-game-leaderboard-4692`.

9. Add a final variable named **ResourceGroupName** with the value `tailspin-space-game-rg`.

10. In the command bar near the top of the page, select **Save** to save your **Release** variable group to the pipeline.

   The variables in your variable group should be similar:

  
   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/pipelines-environments.png)

## Create the spike environment

In previous modules, you created environments for dev, test, and staging environments. Here, do the same. This time, create an environment named **spike**.

1. From the Azure DevOps menu, under **Pipelines**, select **Environments**.

   ![A screenshot of Azure Pipelines showing the location of the Environments menu option.](#)

2. Select **Create environment**. The **New environment** pane appears.

3. For **Name**, enter **spike**.

4. Leave the remaining fields at their default values.

5. Select **Create**.

## Create a service connection

Here, you create a service connection that enables Azure Pipelines to access your Azure subscription. Azure Pipelines uses this service connection to deploy the website to App Service. You created a similar service connection in the previous module.

> **Important**  
> Make sure that you're signed in to both the Azure portal and Azure DevOps under the same Microsoft account.

1. In Azure DevOps, **Space Game - web - Azure Functions** pipeline project, below the menu, select **Project settings**. The **Project details** pane appears.

2. In the menu, under **Pipelines**, select **Service connections**.

3. On the **Service connections** page, select **New service connection**, and then in the **New service connection** pane, select **Azure Resource Manager**, and then select **Next**.

4. In the **New service connection** pane, select **Service principal (automatic)**, and then select **Next**.

5. In the **New Azure service connection** pane, select or enter the following settings:

   | Field | Value |
   |-------|-------|
   | Scope level | Subscription |
   | Subscription | Select your Azure subscription |
   | Resource Group | tailspin-space-game-rg |
   | Service connection name | Resource Manager - Tailspin - Space Game |

   During the process, you might be prompted to sign in to your Microsoft account.

6. Ensure that **Grant access permission to all pipelines** is selected.

7. Select **Save**.

   Azure DevOps performs a test connection to verify that it can connect to your Azure subscription. If Azure DevOps can't connect, you have the chance to sign in a second time.



# 6.4 Exercise - Deploy an Azure Functions app to Azure

Your project came with a pipeline that builds the projects in the solution and deploys the web app to Azure App Service. Now it's time to extend that pipeline to also deploy the new Azure Functions project.

In this part, you do these tasks:

- Review the Build stage.
- Add a task to deploy your function app.
- Add a task configure the published App Service to use the published function.
- Save the pipeline to trigger a CI/CD workflow.

## Review the Build stage

Here, review the existing CI/CD pipeline defined in `azure-pipelines.yml`.

1. From Azure DevOps, navigate to **Pipelines**.

2. Select the pipeline.

3. Select **Edit**. Ensure that the branch is set to **main** by selecting it from the dropdown menu. This brings up the `azure-pipelines.yml` file that defines the existing CI/CD pipeline.

Because of the use of wildcards to the project paths, the highlighted tasks in this file automatically restore, build, and publish the new Azure Functions project.

**yml**
```yaml
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
      dotnetSdkVersion: '6.0.x'

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

**Andy:** This was our previous build stage. I didn't change it from the original project because the tasks were already configured to run against all projects based on the wildcard matching pattern.

**Mara:** Yes, this should work as-is. I don't think we need to make any changes here. After this build task runs, the zip file artifacts for both the web and leaderboard projects will be published for the Deploy stage to use.

## Add a task to deploy the Azure Function

**Andy:** I think we can also reuse the App Service deployment task as-is. Hopefully there's something similar we can use for deploying a function app.

**Mara:** I have good news. After a little research, it looks like there's a task that's conceptually similar to the App Service deployment task, but for Azure Functions deployments. Let's review it now.

### Azure Function App Task

The `AzureFunctionApp@1` task is designed to deploy function apps. It's conceptually similar to the `AzureWebApp@1` task and includes everything needed for this function-app scenario:

- `azureSubscription` refers to the name of your Azure service connection pipeline variable.
- `appType` indicates whether the app is being deployed for Linux (`functionAppLinux`) or Windows (`functionApp`).
- `appName` specifies the name of the Azure Functions app instance in your Azure account.
- `package` specifies the path to the package to be deployed.
- `runtimeStack` indicates which image the function should be run on, which is required for Linux deployments.
- `startUpCommand` specifies the startup command to run after the function has been deployed, which is required for Linux deployments.

You can learn more about the flexibility of this task in the documentation for the Azure Function App task.

Add the following highlighted code to the end of your pipeline.

**yml**
```yaml
- stage: 'Deploy'
  displayName: 'Deploy the web application'
  dependsOn: Build
  jobs:
  - deployment: Deploy
    pool:
      vmImage: 'ubuntu-20.04'
    environment: spike
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
              appType: webAppLinux
              package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/Tailspin.SpaceGame.Web.zip'

          - task: AzureFunctionApp@1
            displayName: 'Azure Function Deploy: leaderboard'
            inputs:
              azureSubscription: 'Resource Manager - Tailspin - Space Game'
              appType: functionAppLinux
              appName: '$(LeaderboardAppName)'
              package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/Tailspin.SpaceGame.LeaderboardFunction.zip'
              runtimeStack: DOCKER|microsoft/azure-functions-dotnet:4
              startUpCommand: 'func azure functionapp publish $(functionAppName) --no-bundler'
```

> **Tip**  
> In a YAML file, whitespace is important. Ensure that the task you add here uses the same indentation as the previous task.

## Add a task to update the App Service's app settings

**Andy:** Now all we need to do is to configure the web app to use the published leaderboard API. We usually configure variables in the portal, but it would be better if we could do it here. It expects an AppSettings parameter named `LeaderboardFunctionUrl`.

**Mara:** I agree. Adding a task for that to our pipeline will help us avoid accidental oversights down the road if we change either service. We can put it right at the end.

Add the following highlighted code to the end of your pipeline. Be sure to match the indentation of the task above it. If you'd like to learn more about this task, you can review the docs for Azure App Service Settings task.

**yml**
```yaml
- task: AzureFunctionApp@1
  displayName: 'Azure Function Deploy: leaderboard'
  inputs:
    azureSubscription: 'Resource Manager - Tailspin - Space Game'
    appType: functionAppLinux
    appName: '$(LeaderboardAppName)'
    package: '$(Pipeline.Workspace)/drop/$(buildConfiguration)/Tailspin.SpaceGame.LeaderboardFunction.zip'
    runtimeStack: DOCKER|microsoft/azure-functions-dotnet:4
    startUpCommand: 'func azure functionapp publish $(functionAppName) --no-bundler'

- task: AzureAppServiceSettings@1
  displayName: 'Update web app settings'
  inputs:
    azureSubscription: 'Resource Manager - Tailspin - Space Game'
    appName: $(WebAppName)
    resourceGroupName: $(ResourceGroupName)
    appSettings: |
      [
        {
          "name": "AppSettings__LeaderboardFunctionUrl",
          "value": "http://$(LeaderboardAppName).azurewebsites.net/api/LeaderboardFunction",
          "slotSetting": false
        }
      ]
```

## Save the pipeline to trigger a build and release

1. Select **Save** from the top right corner of the page. Confirm the **Save** to trigger a run.

2. In Azure Pipelines, go to the build. Trace the build as it runs.

3. After the build succeeds, select the web site's deploy task and select the URL to view the deployed site.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-azure-functions/media/4-deploy-url.png)

5. You get a page with the site running on App Service. Scroll down to confirm that the leaderboard has real data in it. This feature is powered by the function app.

     ![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-azure-functions/media/4-space-game.png)

   > **Note**  
   > If there's an error loading the leaderboard, double-check the steps you followed in this module. If you see the exception message "An attempt was made to access a socket in a way forbidden by its access permissions", make sure that the app service's `AppSettings__LeaderboardFunctionUrl` setting is being set correctly.

7. You can also test out the function app directly. Just navigate to your URL using the following format. The response is JSON, which should just render as text in your browser.

   **HTTP**
   ```
   http://<leaderboard function name>.azurewebsites.net/api/LeaderboardFunction?pageSize=10
   ```

   such as

   **HTTP**
   ```
   http://tailspin-space-game-leaderboard-4692.azurewebsites.net/api/LeaderboardFunction?pageSize=10
   ```

**Andy:** This turned out great! Everyone should be pretty impressed with the potential we've shown here.





# 6.5 Exercise - Clean up your Azure DevOps environment

You're finished with the tasks for this module. Here, you clean up your Azure resources, move the work item to the Done state on Azure Boards, and clean up your Azure DevOps environment.

> **Important**  
> This page contains important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes. It also helps ensure that you're not charged for Azure resources after you complete this module.

## Clean up Azure resources

Here, you delete your Azure App Service and Azure Functions instances. The easiest way to delete the instances is to delete their parent resource group. When you delete a resource group, you delete all resources in that group.

In the **Create a release pipeline with Azure Pipelines** module, you managed Azure resources through the Azure portal. Tear down your deployment by using the Azure CLI through Azure Cloud Shell. The steps are similar to the steps that you used when you created the resources.

### To clean up your resource group:

1. Go to the Azure portal and sign in.

2. From the menu bar, select **Cloud Shell**. When prompted, select the **Bash** experience.

     ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-portal-menu-cloud-shell.png)

4. Run the following `az group delete` command to delete the resource group that you used, `tailspin-space-game-rg`.

   **Azure CLI**
   ```bash
   az group delete --name tailspin-space-game-rg
   ```

   When prompted, enter `y` to confirm the operation.

5. As an optional step, after the previous command finishes, run the following `az group list` command.

   **Azure CLI**
   ```bash
   az group list --output table
   ```

   You see that the resource group `tailspin-space-game-rg` no longer exists.

## Move the work item to Done

Here, move the work item that you assigned to yourself earlier in this module. You move **Refactor leaderboard API as an Azure Functions app** to the **Done** column.

In practice, "Done" often means putting working software into the hands of your users. For learning purposes, here you mark this work as done because you fulfilled the goal for the Tailspin team. They wanted to refactor their project to extract a leaderboard API as a function app.

At the end of each sprint, or work iteration, you and your team can hold a retrospective meeting. In the meeting, share the work you completed, what went well, and what you can improve.

### To complete the work item:

1. From Azure DevOps, navigate to **Boards**, then select **Boards** from the menu.

2. Move the **Refactor leaderboard API as an Azure Functions app** work item from the **Doing** column to the **Done** column.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-azure-functions/media/5-azure-boards-wi1-done.png)

## Disable the pipeline or delete your project

Each module in this learning path provides a template. You can run the template to create a clean environment for the module.

Running multiple templates gives you multiple Azure Pipelines projects. Each project points to the same GitHub repository. This setup can trigger multiple pipelines to run each time you push a change to your GitHub repository. The pipeline runs use up free build minutes on our hosted agents. To avoid losing those free build minutes, disable or delete your pipeline before you move to the next module.

Choose one of the following options.

### Option 1: Disable the pipeline

Disable the pipeline so that it doesn't process build requests. You can re-enable the build pipeline later if you want to. Choose this option if you want to keep your DevOps project and your build pipeline for future reference.

#### To disable the pipeline:

1. In Azure Pipelines, navigate to your pipeline.

2. From the dropdown menu, select **Settings**:

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-pipelines-settings-button.png)

4. Under **Processing of new run requests**, select **Disabled** and then select **Save**.

   Your pipeline no longer processes build requests.

### Option 2: Delete the Azure DevOps project

Delete your Azure DevOps project, including the contents of Azure Boards and your build pipeline. In future modules, you can run another template that brings up a new project in a state where this project leaves off. Choose this option if you don't need your DevOps project for future reference.

#### To delete the project:

1. In Azure DevOps, navigate to your project. Earlier, we recommended that you name this project **Space Game - web - Azure Functions**.

2. Select **Project settings** in the lower corner.

3. In the **Overview** area, go to the bottom and select **Delete**.


   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-delete-project.png)

5. In the window that appears, enter the project name. Select **Delete** again.

   Your project is now deleted.



# 6.6 Summary

Great work! In this module, you extended a release pipeline to add support for deploying an Azure Functions app. The single release pipeline now builds a multi-project solution and deploys different components to different cloud targets in Azure.

While this module focused on an app that uses Azure App Service and Azure Functions, the fundamentals covered apply across a wide range of build and deployment targets. You can also see how Azure Pipelines can scale to support even the most sophisticated scenarios.

## Learn more

In this module, you worked with Azure Functions, which are one of the development models within the broader Azure serverless computing offerings. Azure Functions was a great solution for the Tailspin team, but your needs might vary, and it's important to understand which compute options are best for your scenario. To learn more, explore these resources.

There are quite a few serverless offerings under the Azure umbrella, and there's some overlap between various services. For a more in-depth review of some key serverless options, including Azure Functions, Microsoft Flow, Azure Logic Apps, and Azure App Service WebJobs, see [Choose the right integration and automation services in Azure](#).

Azure Functions is also a great option for microservice solutions like the one the Tailspin team is evolving towards here. To understand the different options for microservices on Azure, including Azure Functions, Kubernetes, and Service Fabric, see [Choosing an Azure compute option for microservices](#).

However, serverless isn't always appropriate for every situation. Stateful applications, for example, aren't a good fit for serverless computing. Fortunately, Azure provides many different compute offerings that cover virtually every cloud scenario. For help with finding the right one for your application, see [Choose an Azure compute service for your application](#).




# 7 Automate Docker container deployments with Azure Pipelines

Use Azure Pipelines to deploy Docker containers to Azure App Service.
### Learning objectives
After completing this module, you'll be able to:
- Create Azure resources to support a Docker container web application.
- Use YAML pipelines to build, publish, and deploy a Docker container.
- Monitor the build and deployment of your project.

If you just want to learn how to deploy Docker containers to Azure Web App for Containers, please refer to the Deploy to Azure Web App for Containers guide.

#### Prerequisites
- An Azure subscription
- An Azure DevOps organization with access to Microsoft-hosted parallel jobs. Check your parallel jobs and request a free grant.
- A GitHub account


# 7.1  Introduction


In **Create a release pipeline with Azure Pipelines**, you built a basic release pipeline that deploys an ASP.NET Core application to Azure App Service. Although this process covers the needs for basic applications, modern solutions often require a combination of applications, services, and other components.

Azure provides great support for traditional app deployments, such as to virtual machines or application services. Another option you might consider is to deploy your app by using a container. A *container* app is one that's packaged and published as a single artifact that can be deployed with all of its dependencies to run in an isolated environment.

In this module, you'll join the Tailspin Toys web team as they explore one way to use containers in Azure. You'll learn how to update your CI/CD pipeline to build a Docker container, publish the container to Azure Container Registry, and deploy the container to App Service.

While this module focuses on the core tasks that are required to build and deploy your container app, it's important to understand that all of the other features of Azure Pipelines are still available for Docker container deployments. You can integrate testing, define multiple stages, and perform other tasks just like you would for your existing applications. We omit these tasks here to keep things focused.

## Learning objectives

After completing this module, you'll be able to:

- Create Azure resources to support a Docker container web application.
- Use YAML pipeline to build, publish, and deploy a Docker container.
- Monitor the build and deployment of your project.

## Prerequisites

The modules in this learning path form a progression. If you want to follow the progression from the beginning, complete the following learning paths:

- Get started with Azure DevOps
- Build applications with Azure DevOps

This module assumes you have basic familiarity with Docker, although that knowledge isn't required to complete it. If you're new to the topic, it's recommended that you complete the **Introduction to Docker containers** module first.

> **Note**  
> Azure Pipelines support a vast array of **languages and application types**. In this module, you'll be working with a .NET application but you can apply the patterns you learn here to your own projects that use your favorite programming languages and frameworks.

## Meet the team

You met the *Space Game* web team at Tailspin Toys in previous modules. As a refresher, here's who you'll work with in this module.

**Andy** is the development lead.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/andy.png)


**Amita** is in QA.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/amita.png)

**Tim** is in operations.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/tim.png)

**Mara** just joined as a developer and reports to Andy.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/mara.png)

Mara has prior experience with DevOps. She's helping the team adopt a more automated process that uses Azure DevOps.


# 7.2 Why are containers important?

In this unit, you'll follow the Tailspin team as they discuss some much-needed improvements to their DevOps process. In this scenario, the team uses Docker to containerize their web application. The team then updates their CI/CD pipeline to support it.

## It's been a few rough weeks

The past few weeks have been a challenging time at Tailspin. Teams struggle to meet deadlines for a number of reasons, and there's been concern over productivity across the company. Andy has called some key stakeholders from the Space Game website team together to gather feedback for an upcoming presentation to management.

**Andy:** Thanks for stopping by. I know the last few weeks have been rough for everyone, but I have some good news. Management is holding an offsite tomorrow to hear proposals on changes we can make to improve performance. They've invited me to present a case study on our DevOps successes and said they're also open to any other ideas we might have. I was hoping we could use this meeting as an opportunity to brainstorm. Who wants to go first?

Everyone looks at Amita. She has been especially frustrated lately.

**Amita:** I'll go first. As you know, I test for multiple teams, and it can be challenging because each team uses their own technology stack. Even when they use the same underlying platforms, like .NET or Java, they often target different versions. I feel like I sometimes spend half of my day simply getting test environments in a state where they can run the code I need to test. When something doesn't work, it's hard to tell whether there's a bug in the code or if I accidentally configured version 4.2.3 instead of 4.3.2.

Andy writes "Dependency versioning challenges for QA" on the whiteboard.

**Tim:** I'd like to add operations to that frustration. We have a few teams with unique version requirements, so we have to publish their apps on their own virtual machines just to ensure their version and component requirements don't conflict with our other apps. Besides the overhead involved in maintaining the extra set of VMs, it also costs us more than it would if those apps could run side by side.

Andy writes "Overhead due to solving app isolation with VMs" on the whiteboard.

**Mara:** I have something from the development side. A few weeks ago, I was working on the peer-to-peer update system and had it all working on my machine. But when I handed it off for deployment, it didn't work in production. I had forgotten that I needed to open port 315 as part of the service. It took us over a day of troubleshooting to realize what was going on. Once we opened that up in production, things worked as expected.

Andy writes "Configuration inconsistencies between deployment stages" on the whiteboard.

**Andy:** I think this conversation is a good start. Let me research these issues and see what I can come up with. Here are the concerns that I heard:

- Dependency versioning challenges for QA
- Overhead due to solving app isolation with VMs
- Configuration inconsistencies between deployment stages

## Putting it all together (in one container)

The next morning, Andy calls a meeting to present a new idea to the team.

**Andy:** I spoke with some colleagues yesterday about the challenges we're facing, and they made some interesting suggestions. The one I'm excited to try out is Docker. It's a technology for packaging entire applications as containers.

**Amita:** What's a container? Is that like a .zip file?

**Andy:** Not exactly. It's more like a lightweight virtual machine designed to run directly on the host operating system. When you build your project, the output is a container that includes your software and its dependencies. However, it's not a complete virtualized system, so it can spin up in as little as less than one second.

**Tim:** How does it handle security and isolation?

**Andy:** Security and isolation are handled by the host operating system. When your container runs in a host process, the container is isolated from the other processes on that same host machine. This isolation allows your container to load whatever versions of components it needs, regardless of what other containers are doing. It also means you can easily run multiple containers on the same host simultaneously.

**Amita:** That sounds great for the production environment, but does it solve the challenges we're facing earlier in the pipeline?

**Andy:** Absolutely! Instead of shipping source code or a set of binaries, the entire container becomes the artifact. That means that when Mara is developing, her debugging sessions run locally against the container hosted on her machine. When Amita tests, she tests against a copy of that same container, which already includes all the required versions of its dependencies. When Tim manages our production environment, the containers he monitors are standalone copies of the same containers developed by Mara and tested by Amita.

**Mara:** How hard is it to develop a container application? Do we have to make significant changes to our existing code?

**Andy:** Containers are more of a packaging and deployment technology. They don't impact the fundamental software we're writing. We can just instruct our tools to produce a Docker container at the end of the build. Then, when we debug, the application runs out of that local container instead of our local web server. In fact, tools like Visual Studio even let you switch between debug environments like Docker and IIS Express to give us the flexibility we need. I actually forked our web site project last night and converted it to build as a Docker container to test out the process. I only needed to add some basic container configuration; I didn't need to change any of our existing code.

**Mara:** That's great to know. I bet we can even update the release pipeline in Azure Pipelines from your fork to build and deploy the Docker version.

**Andy:** You read my mind.

## What is Docker?

Docker is a technology for automating the packaging and deployment of portable, self-sufficient containers. Docker containers can run anywhere a Docker host is found, whether on a development machine, a departmental server, an enterprise datacenter, or in the cloud. Azure provides multiple ways to run container-based applications, including App Service or as part of clusters managed with orchestration technologies like Kubernetes.

The Tailspin team selected Docker containers for this scenario because it met all their needs:

- **Dependency versioning challenges for QA:** Applications are packaged as containers that bring the correct versions of their dependencies with them.

- **Overhead due to solving app isolation with VMs:** Many isolated containers can run on the same host with benefits over virtual machines including faster startup time to greater resource efficiency.

- **Configuration inconsistencies between DevOps stages:** Containers ship with manifests that automate configuration requirements, such as which ports need to be exposed.

Adopting Docker containers can be a key step towards a microservices architecture. We'll discuss more about that later on.

---

## Check your knowledge

### 1. Which of the following options is not a good reason to use Docker?

- **✅ You build mobile apps and want a single mobile container to run across different operating systems.**
- ❌ Your application has specific dependency requirements and you want to package them along with the app itself for deployment.
- ❌ You want the different stages of your pipeline to use the same environment used in production.

**Explanation:** Docker containers run on the host operating system, so they cannot run a mobile app across different operating systems. Mobile apps are platform-specific and require different runtimes for iOS, Android, etc. Docker is better suited for server-side applications that need consistent environments and dependency management.

### 2. How are containers and virtual machines similar?

- ❌ They both run their own virtualized operating systems.
- **✅ They both provide isolation for the applications they contain.**
- ❌ They both offer the same performance.

**Explanation:** Both containers and virtual machines provide isolation for applications, but they achieve it differently. VMs run complete virtualized operating systems, while containers share the host OS kernel. Containers typically offer better performance due to lower overhead compared to VMs.

### 3. How much overhead does migrating an existing .NET Core application to use a Docker container require?

- ❌ A lot. Docker uses its own programming languages and development framework, so applications need to be rebuilt.
- ❌ Quite a bit. Application code will need to be adjusted to load Docker settings and configuration data.
- **✅ Very little. The application should require no changes, but a Docker manifest that specifies application requirements will need to be added.**

**Explanation:** Docker is primarily a packaging and deployment technology. Existing applications typically require minimal changes - mainly adding a Dockerfile that specifies how to build the container image. The application code itself usually remains unchanged.


# 7.3 Exercise - Set up your Azure DevOps environment


In this section, you'll lean how to set up your Azure DevOps organization and create the Azure App Service environment that you'll deploy to.

You'll learn how to:

- Set up your Azure DevOps project.
- Manage your work items with Azure Boards.
- Create your Azure App Service environment.
- Create pipeline variables in Azure Pipelines.
- Create a service connection to authenticate with your Azure subscription.

## Add a user to Azure DevOps

To complete this module, you need your own Azure subscription. You can get started with Azure for free.

You don't need an Azure subscription to work with Azure DevOps, but in this module you'll use Azure DevOps to deploy to Azure resources. To simplify the process, use the same Microsoft account to sign in to both Azure and Azure DevOps.

If you use different Microsoft accounts to sign in to Azure and Azure DevOps, add a user with Basic access level to your DevOps organization under the Microsoft account that you use to sign in to Azure. See [Add users to your organization or project](#) for more details.

Then, sign out of Azure DevOps and sign back in using the same account you used to sign in to your Azure subscription.

## Get the Azure DevOps project

Here, you'll ensure that your Azure DevOps organization is set up to complete the rest of this module. To do so, you'll run a template that creates a project in Azure DevOps.

The modules in this learning path form a progression. You follow the Tailspin web team through their DevOps journey. For learning purposes, each module has its own Azure DevOps project.

### Run the template

Run a template that sets up your Azure DevOps organization.

1. Get and run the ADOGenerator project in Visual Studio or the IDE of your choice.

2. When prompted to **Enter the template number from the list of templates**, enter **39** for **Automate Docker container deployments with Azure Pipelines**, then press Enter.

3. Choose your authentication method. You can set up and use a Personal Access Token (PAT) or use device login.

   > **Note**  
   > If you set up a PAT, make sure to authorize the necessary scopes. For this module, you can use Full access, but in a real-world situation, you should ensure you grant only the necessary scopes.

4. Enter your Azure DevOps organization name, then press Enter.

5. If prompted, enter your Azure DevOps PAT, then press Enter.

6. Enter a project name such as **Space Game - web - Docker**, then press Enter.

7. Once your project is created, go to your Azure DevOps organization in your browser (at `https://dev.azure.com/<your-organization-name>/`) and select the project.

### Fork the repository

If you haven't already, create a fork of the `mslearn-tailspin-spacegame-web-docker` repository.

1. On GitHub, go to the [mslearn-tailspin-spacegame-web-docker](#) repository.

2. Select **Fork** at the top-right of the screen.

3. Choose your GitHub account as the Owner, then select **Create fork**.

> **Important**  
> In this module, the **Clean up your Azure DevOps environment** page contains important cleanup steps. Cleaning up helps ensure that you don't run out of free build minutes. Be sure to follow the cleanup steps even if you don't complete this module.

### Set your project's visibility

Initially, your fork of the Space Game repository on GitHub is set to public while the project created by the Azure DevOps template is set to private. A public repository on GitHub can be accessed by anyone, while a private repository is only accessible to you and the people you choose to share it with. Similarly, on Azure DevOps, public projects provide read-only access to non-authenticated users, while private projects require users to be granted access and authenticated to access the services.

At the moment, it is not necessary to modify any of these settings for the purposes of this module. However, for your personal projects, you must determine the visibility and access you wish to grant to others. For instance, if your project is open source, you may choose to make both your GitHub repository and your Azure DevOps project public. If your project is proprietary, you would typically make both your GitHub repository and your Azure DevOps project private.

Later on, you may find the following resources helpful in determining which option is best for your project:

- [Use private and public projects](#)
- [Change project visibility to public or private](#)
- [Setting repository visibility](#)

## Move the work item to Doing

Here, you'll assign a work item to yourself on Azure Boards. You'll also move the work item to the **Doing** state. In practice, you and your team would create work items at the start of each sprint, or work iteration.

This work assignment gives you a checklist to work from. It gives other team members visibility into what you're working on and how much work is left. The work item also helps enforce work-in-progress (WIP) limits so that the team doesn't take on too much work at one time.

Here, you'll move the first item, **Create container version of web site using Docker**, to the **Doing** column, then assign yourself to the work item.

### To set up the work item:

1. From Azure DevOps, navigate to **Boards**. Then select **Boards** from the menu.

   
   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-boards-menu.png)

3. In the **Create container version of web site using Docker** work item, select the down arrow at the bottom of the card, then assign the work item to yourself.

    ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-boards-down-chevron.png)

5. Move the work item from the **To Do** column to the **Doing** column.

    ![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-docker/media/3-azure-boards-wi1-doing.png)

At the end of this module, you'll move the card to the **Done** column after you complete the task.

## Create the Azure App Service environment

In the **Create a release pipeline with Azure Pipelines** module, you created an App Service instance using Azure portal. Although the portal is an excellent tool for exploring Azure's offerings, setting up components like App Service can become cumbersome.

In this module, you'll employ the Azure CLI to launch the resources necessary for deploying and running an App Service instance. You can access the Azure CLI from a terminal or through Visual Studio Code.

> **Important**  
> You must have your own Azure subscription to complete the exercises in this module.

### Launch Cloud Shell inn Azure portal

1. Navigate to the [Azure portal](https://portal.azure.com) and sign in.

2. Select the **Cloud Shell** from the menu bar, and then select the **Bash** experience.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-portal-menu-cloud-shell.png)

   > **Note**  
   > Cloud Shell requires an Azure storage resource to persist any files that you create in Cloud Shell. When you first open Cloud Shell, you're prompted to create a resource group, storage account, and Azure Files share. This setup is automatically used for all future Cloud Shell sessions.

### Select an Azure region

A region is one or more Azure datacenters located within a particular geographic location. East US, West US, and North Europe are a few examples of regions. Each Azure resource, such as an App Service instance, is allocated to a specific region.

To simplify the process of running commands, begin by selecting a default region. Once the default region is specified, subsequent commands will use that region by default unless a different region is explicitly specified.

1. Run the following command to list the available regions for your Azure subscription.

   **Azure CLI**
   ```bash
   az account list-locations \
     --query "[].{Name: name, DisplayName: displayName}" \
     --output table
   ```

2. Select a region that is in proximity to your location from the **Name** column in the output. For example, you can choose `eastasia` or `westus2`.

3. Run the following command to set your default region. Replace the placeholder with the name of the region you've selected.

   **Azure CLI**
   ```bash
   az configure --defaults location=<REGION>
   ```

   This example sets `westus2` as the default region:

   **Azure CLI**
   ```bash
   az configure --defaults location=westus2
   ```

### Create Bash variables

In this section, you'll create Bash variables to make the setup process more convenient and less error-prone. Using variables for shared text strings helps avoid accidental typos.

1. From Cloud Shell, generate a random number. This will make it easier to create globally unique names for certain services in the next step.

   **Bash**
   ```bash
   resourceSuffix=$RANDOM
   ```

2. Create globally unique names for your App Service Web App and Azure Container Registry. Using double quotes in these commands prompts Bash to interpolate the variables using the inline syntax.

   **Bash**
   ```bash
   webName="tailspin-space-game-web-${resourceSuffix}"
   registryName="tailspinspacegame${resourceSuffix}"
   ```

3. Create two more Bash variables to store the names of your resource group and App Service plan.

   **Bash**
   ```bash
   rgName='tailspin-space-game-rg'
   planName='tailspin-space-game-asp'
   ```

### Create the Azure resources

> **Note**  
> For learning purposes, you'll the default network settings here. These settings make your site accessible from the internet. In practice, you could configure an Azure virtual network that places your website in a network that's not internet routable and that only you and your team can access. Later, you could reconfigure your network to make the website available to your users.

1. Run the following `az group create` command to create a resource group using the name defined earlier.

   **Azure CLI**
   ```bash
   az group create --name $rgName
   ```

2. Run the following `az acr create` command to create an Azure Container Registry using the name defined earlier.

   **Azure CLI**
   ```bash
   az acr create --name $registryName \
     --resource-group $rgName \
     --sku Standard \
     --admin-enabled true
   ```

3. Run the following `az appservice plan create` command to create an App Service plan using the name defined earlier.

   **Azure CLI**
   ```bash
   az appservice plan create \
     --name $planName \
     --resource-group $rgName \
     --sku B1 \
     --is-linux
   ```

   The `--sku` argument specifies the B1 plan. This plan runs on the Basic tier. The `--is-linux` argument specifies to use Linux workers.

   > **Important**  
   > If the B1 SKU isn't available in your Azure subscription, choose a different plan, such as S1 (Standard).

4. Run the following `az webapp create` command to create the App Service instance.

   **Azure CLI**
   ```bash
   az webapp create \
     --name $webName \
     --resource-group $rgName \
     --plan $planName \
     --deployment-container-image-name $registryName.azurecr.io/web:latest
   ```

5. Run the following `az webapp list` command to list the host name and state of the App Service instance.

   **Azure CLI**
   ```bash
   az webapp list \
     --resource-group $rgName \
     --query "[].{hostName: defaultHostName, state: state}" \
     --output table
   ```

   Note the host name for the running service. You'll need it later when you verify your work. Here's an example:

   **Output**
   ```
   HostName                                        State
   ----------------------------------------------  -------
   tailspin-space-game-web-4692.azurewebsites.net  Running
   ```

6. Run the following `az acr list` command to list the login server of the Azure Container Registry instance. You'll need this server name when creating pipeline variables later.

   **Azure CLI**
   ```bash
   az acr list \
     --resource-group $rgName \
     --query "[].{loginServer: loginServer}" \
     --output table
   ```

   Note the login server. You'll need it later when you configure the pipeline. Here's an example:

   **Output**
   ```
   LoginServer
   ---------------------------------
   tailspinspacegame4692.azurecr.io    
   ```

> **Important**  
> The **Clean up your Azure DevOps environment** page in this module contains important cleanup steps. Cleaning up helps ensure that you're not charged for Azure resources after you complete this module. Be sure to perform the cleanup steps even if you don't complete this module.

## Create pipeline variables in Azure Pipelines

In **Create a release pipeline with Azure Pipelines**, you added a variable to your pipeline that stores the name of your web app in App Service. You'll do the same thing here. In addition, you'll add the name of your Azure Container Registry.

You could hard-code these names in your pipeline configuration, but if you define them as variables, your configuration will be more reusable. Plus, if your instance names change, you can update the variables and trigger your pipeline without modifying your configuration.

### To add the variables:

1. In Azure DevOps, go to your **Space Game - web - Docker** project.

2. Under **Pipelines**, select **Library**.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-docker/media/3-pipelines-library.png)

4. Select **+ Variable group**.

5. Under **Properties**, enter **Release** for the variable group name.

6. Under **Variables**, select **+ Add**.

7. For the name of your variable, enter **WebAppName**. For the value, enter the name of the App Service instance created above, such as `tailspin-space-game-web-4692`.

   > **Important**  
   > Set the name of the App Service instance, not its host name. In this example, you would enter `tailspin-space-game-web-4692` and not `tailspin-space-game-web-4692.azurewebsites.net`.

8. Repeat the process to add another variable named **RegistryName** with the value of your Azure Container Registry login server, such as `tailspinspacegame4692.azurecr.io`.

9. Select **Pipeline permissions**, and then select the **+** sign to add a pipeline. Select **mslearn-tailspin-spacegame-web-docker** to give your pipeline permission to access the variable group.

10. Select **Save** at the top of the page to save your variables. Your variable group should look like the following:

    ![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-docker/media/3-library-variable-group.png)

## Create required service connections

Here, you'll create a service connection that enables Azure Pipelines to access your Azure subscription. Azure Pipelines uses this service connection to deploy the website to App Service. You created a similar service connection in the previous module. You'll also create a Docker Registry connection to publish your container to the Azure Container Registry.

> **Important**  
> Ensure that you're signed in to both the Azure portal and Azure DevOps under the same Microsoft account.

1. In Azure DevOps, go to your **Space Game - web - Docker** project.

2. From the bottom corner of the page, select **Project settings**.

3. Under **Pipelines**, select **Service connections**.

4. Select **New service connection**, then choose **Azure Resource Manager**, then select **Next**.

5. Near the top of the page, **Service principal (automatic)**. Then select **Next**.

6. Fill in these fields:

   | Field | Value |
   |-------|-------|
   | Scope level | Subscription |
   | Subscription | Your Azure subscription |
   | Resource Group | tailspin-space-game-rg |
   | Service connection name | Resource Manager - Tailspin - Space Game |

   During the process, you might be prompted to sign in to your Microsoft account.

7. Ensure that **Grant access permission to all pipelines** is selected.

8. Select **Save**.

   Azure DevOps performs a test connection to verify that it can connect to your Azure subscription. If Azure DevOps can't connect, you have the chance to sign in a second time.

9. Select **New service connection**, then choose **Docker Registry**, then select **Next**.

10. Near the top of the page, select **Azure Container Registry**.

11. Fill in these fields:

    | Field | Value |
    |-------|-------|
    | Subscription | Your Azure subscription |
    | Azure container registry | Select the one you created earlier |
    | Service connection name | Container Registry Connection |

12. Ensure that **Grant access permission to all pipelines** is selected.

13. Select **Save** when you're done.



#  7.4 Exercise - Deploy a Docker container to Azure

Your project came with a release pipeline that builds the projects in the solution and deploys the web app to its App Service. Now, it's time to update that pipeline build and deploy the project as a container instead.

In this unit, you'll:

- Define some pipeline variables to make the build pipeline easier to maintain.
- Replace the existing Build tasks with a unified task to build and push a Docker container.
- Replace the existing Deploy task with one that updates the App Service Web App with the new container image.
- Save the pipeline to trigger a build and release.

## Define variables to be shared within the pipeline

Here, you'll add a new pipeline variable to your existing YAML pipeline defined in `azure-pipelines.yml`.

1. From Azure DevOps, navigate to **Pipelines**.

2. Select the pipeline.

3. Select **Edit**. Ensure that the branch is set to **main** by selecting it from the drop-down menu. This brings up your `azure-pipelines.yml` file.

4. Add the highlighted line below to add a pipeline variables named `webRepository` and `tag`. These will be used in multiple tasks to uniquely identify the specific version of the container being referenced. You can also remove the `buildConfiguration` variable; you won't need it anymore.

   **yml**
   ```yaml
   trigger:
   - '*'

   variables:
     buildConfiguration: 'Release'
     webRepository: 'web'
     tag: '$(Build.BuildId)'
   ```

## Replace the build stage tasks

**Andy:** I don't think we need any of these build tasks anymore, because the Dockerfile in the project folder already defines the build we want. However, I haven't had the chance to see what we can use to build the image using a Dockerfile yet. Any ideas?

**Mara:** I was just looking that up. It seems like should be able to build the container and even push it to the repository with a single task. Let's add it now.

### Docker task

You can use the Docker task to build and deploy Docker images. Replace the entire Build stage with the YAML snippet below.

- `command`: Specifies the Docker command to run.
- `buildContext`: Specifies the path to the build context.
- `repository`: Specifies the name of the repository.
- `dockerfile`: Specifies the path to the Dockerfile.
- `containerRegistry`: Specifies the name of the Docker registry service connection.
- `tags`: Specifies a list of tags on separate lines. These tags are used in build, push, and buildAndPush commands.

**yml**
```yaml
- stage: 'Build'
  displayName: 'Build and push'
  jobs:  
  - job: 'Build'
    displayName: 'Build job'
    pool:
      vmImage: 'ubuntu-20.04'
    steps:
    - task: Docker@2
      displayName: 'Build and push the image to container registry'
      inputs:
        command: buildAndPush
        buildContext: $(Build.Repository.LocalPath)
        repository: $(webRepository)
        dockerfile: '$(Build.SourcesDirectory)/Tailspin.SpaceGame.Web/Dockerfile'
        containerRegistry: 'Container Registry Connection'
        tags: |
          $(tag)
```

## Replace the deploy stage task

**Andy:** Well, that seems pretty straightforward. Now all we need is to find a task that will instruct App Service to use the newly pushed version of the container image.

**Mara:** I'm already on it. It's a bit different from deploying a build to Azure Pipelines, but still direct enough that we can get the job done in one task. Let's add it now.

### Azure Web App for Container task

The Azure Web App for Container task is designed to deploy Docker containers to Azure App Service. Replace the entire Deploy stage with the YAML snippet below.

- `appName`: Specifies the name of an existing Azure App Service.
- `azureSubscription`: Specifies the name of the Azure Resource Manager subscription for the deployment.
- `imageName`: Specifies the fully qualified container image name; for example, `myregistry.azurecr.io/nginx:latest` or `python:3.7.2-alpine/`.

**yml**
```yaml
- stage: 'Deploy'
  displayName: 'Deploy the container'
  dependsOn: Build
  jobs:
  - job: 'Deploy'
    displayName: 'Deploy job'
    pool:
      vmImage: 'ubuntu-20.04'
    variables:
    - group: Release
    steps:
    - task: AzureWebAppContainer@1
      inputs:
       appName: $(WebAppName)
       azureSubscription: 'Resource Manager - Tailspin - Space Game'
       imageName: $(RegistryName)/$(webRepository):$(build.buildId)
```

## Save the pipeline to trigger a build and release

1. Select **Save** from the top-right corner of the page. Type your commit message and select **Save** to confirm.

2. Select **Run**, and make sure your branch is set to **main**. Select **Run** when you're done.

3. Select your pipeline to view the logs. After the build has succeeded, select the **AzureWebAppContainer** task and then select the **App Service Application URL** to view your deployed web app.

     ![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-docker/media/4-deploy-url.png)

5. You should see your web app running on App Service.

     ![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-docker/media/4-space-game.png)

**Andy:** This turned out great! I think adopting containers could be a huge win for our team.



# 7.5 Exercise - Clean up your Azure DevOps environment


You've completed all the tasks for this module. Here, you'll clean up your Azure resources, move the work item to the Done state in Azure Boards, and clean up your Azure DevOps environment.

## Clean up Azure resources

The easiest way to delete your Azure App Service instances is to delete their parent resource group. When you delete a resource group, you delete all resources within that group. To delete your resource group:

1. Navigate to [Azure portal](https://portal.azure.com) and sign in.

2. From the menu bar, select **Cloud Shell**. When prompted, select the **Bash** experience.

     ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-portal-menu-cloud-shell.png)

4. Run the following command to delete your resource group (`tailspin-space-game-rg`). When prompted, enter `y` to confirm your choice.

   **Azure CLI**
   ```bash
   az group delete --name tailspin-space-game-rg
   ```

5. To confirm the deletion, execute the following command and ensure that your resource group is not listed anymore.

   **Azure CLI**
   ```bash
   az group list --output table
   ```

## Move the work item to Done

Here, you'll move the work item that you assigned to yourself earlier in this module. You'll move **Create container version of web site using Docker** to the **Done** column.

In practice, "Done" often means putting working software into the hands of your users. For learning purposes, you'll mark this work as "Done" because you fulfilled the goal for the Tailspin team. They wanted to package and deploy their web app as a Docker container.

At the end of each sprint, or work iteration, you and your team can hold a retrospective meeting. In the meeting, share the work you completed, what went well, and what you can improve.

### To complete the work item:

1. From Azure DevOps, navigate to **Boards** and then select **Boards** from the menu.

2. Move the **Create container version of web site using Docker** work item from the **Doing** column to the **Done** column.


   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-pipelines-settings-button.png)

## Disable the pipeline or delete your project

Each module in this learning path provides a template. You can run the template to create a clean environment for the module.

Running multiple templates gives you multiple Azure Pipelines projects. Each project points to the same GitHub repository. This setup can trigger multiple pipelines to run each time you push a change to your GitHub repository. The pipeline runs use up free build minutes on our hosted agents. To avoid losing those free build minutes, disable or delete your pipeline before you move to the next module.

Choose one of the following options:

### Option 1: Disable the pipeline

Disable the pipeline so that it doesn't process build requests. You can re-enable the build pipeline later if you want to. Choose this option if you want to keep your DevOps project and your build pipeline for future reference.

#### To disable the pipeline:

1. In Azure Pipelines, navigate to your pipeline.

2. From the **More actions (...)** drop-down menu, select **Settings**:

  ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-pipelines-settings-button.png)

4. Under **Processing of new run requests**, select **Disabled**, then select **Save**. Your pipeline will no longer process new build requests.

### Option 2: Delete the Azure DevOps project

Delete your Azure DevOps project, including the contents of Azure Boards and your build pipeline. In future modules, you can run another template that brings up a new project in a state where this project leaves off. Choose this option if you don't need your DevOps project for future reference.

#### To delete the project:

1. In Azure DevOps, navigate to your project. Earlier, we recommended that you name this project **Space Game - web - Docker**.

2. Select **Project settings** in the lower corner.

3. Navigate to the bottom of the **Project details** section and choose the **Delete** option.


    ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-delete-project.png)


5. Once the new window appears, input the project name and select **Delete** once more.




# 7.6 Summary


Great work! In this module, you created a release pipeline to build, publish, and deploy the team's web site project to Azure as a Docker container.

While this module specifically focused on a Docker container app, the fundamentals covered apply across a wide range of build and deployment targets. You can also see how Azure Pipelines can scale to support even the most sophisticated scenarios.

## Learn more

In this module, you worked with Docker, which is the leading standard for container technologies.

- To learn more about the fundamentals of Docker containers, see [Introduction to Docker containers](#).
- To learn more about packaging web apps so that they can be deployed as Docker images, see [Build a containerized web application with Docker](#).
- To learn more about running containerized apps using Docker containers with Azure Container Instances (ACI), see [Run Docker containers with Azure Container Instances](#).


# 8 Automate multi-container Kubernetes deployments with Azure Pipelines

Deploy multiple containers to an Azure Kubernetes Service cluster with Azure Pipelines.

#### Learning objectives
After completing this module, you'll be able to:
- Explain the benefits of Kubernetes and when to use it.
- Create Azure resources to support a Kubernetes cluster.
- Update a basic release pipeline to build, publish, and deploy multiple Docker containers to the Kubernetes cluster.
- Monitor the build and deployment of your project.

### Prerequisites
- An Azure DevOps organization with access to Microsoft-hosted parallel jobs. Check your parallel jobs and request a free grant.
- An Azure subscription.
- An Azure DevOps organization.
- A GitHub account.



# 8.1 Introduction


By following the instructions outlined in **Automate Docker container deployments with Azure Pipelines**, you were able to enhance a release pipeline to build and publish an ASP.NET Core application as a Docker container, which was then deployed to Azure App Service. This migration to a container-based project resulted in numerous benefits for the product team. Moreover, the adoption of container technologies has the potential to unlock various innovative opportunities for the future.

As development organizations expand, the complexity of the solutions they provide also grows. As various products and services become more interdependent, different development and operations requirements arise for various components within a given application. One way to enhance architectural efficiency is by refactoring those components into separate microservices.

A microservice is a small, independent service designed to be self-contained and fulfill a specific business capability. Containers provide an excellent technical foundation for building and deploying these services, but a new question arises: how do we manage all of these containers that are in use?

This is where orchestration technologies such as Kubernetes can be useful. Kubernetes is a platform designed to manage containerized workloads and services. It's an excellent choice for organizations that have an increasing number of containers that must be deployed, integrated, and monitored across various environments.

In this module, you join the Tailspin Toys web team as they explore one way to use Kubernetes on Azure. You learn how to update a release pipeline to build, publish, and deploy multiple Docker containers to a Kubernetes cluster.

While this module focuses on the core tasks that are required to build and deploy your container app, it's important to understand that all the other features of Azure Pipelines are still available for container deployments to Kubernetes. You can integrate testing, define multiple stages, and perform other tasks just like you would for your existing applications. We omit these tasks here to keep things focused.

## Learning objectives

After completing this module, you'll be able to:

- Explain the benefits of Kubernetes and when to use it.
- Create Azure resources to support a Kubernetes cluster.
- Update a basic release pipeline to build, publish, and deploy multiple Docker containers to the Kubernetes cluster.
- Monitor the build and deployment of your project.

## Prerequisites

The modules in this learning path form a progression. To follow the progression of this series from the beginning, complete the **Get started with Azure DevOps** and **Build applications with Azure DevOps** learning paths.

To begin this learning path from the start, follow the link here: **Deploy applications with Azure DevOps**. This module picks up where **Automate Docker container deployments with Azure Pipelines** leaves off.

This module also assumes you have basic familiarity with Kubernetes, although that knowledge isn't required to complete it. If you're new to the topic, we recommend that you complete the **Administer containers in Azure** learning path learning path first.

> **Note**  
> Azure Pipelines support a vast array of **languages and application types**. In this module, you'll be working with a .NET application but you can apply the patterns you learn here to your own projects that use your favorite programming languages and frameworks.

## Meet the team

In earlier modules, you met the Space Game web team at Tailspin Toys. The Space Game web team is here again to work with you in this module:


![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/andy.png)

**Andy** is the development lead.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/amita.png)

**Amita** is in QA.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/tim.png)

**Tim** is in operations.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/mara.png)

**Mara** just joined as a developer and reports to Andy.

Mara has prior experience with DevOps. She's helping the team adopt a more automated process that uses Azure DevOps.




# 8.2 Why is container orchestration important?

In this unit, you can follow the Tailspin team as they explore strategies for delivering on a new directive from management. The team examines how Kubernetes can assist in their transition to a microservices architecture.

## The future is smaller

Things are looking up at Tailspin. At a recent management offsite, Andy presented his team's recent successes with Azure DevOps, which were well received. Andy also presented a demo of the team's recent proof-of-concept project using Docker containers. These demonstrations led to a series of productive conversations on the technical future of the organization. The next day, Andy returns to share the news with the Space Game web team.

**Andy:** Things went really well at my offsite presentation yesterday. Management is impressed with the work we've done so far, and has issued us a special assignment.

**Tim:** Uh oh. I've been around long enough to see a trap like that coming from a mile away.

**Andy:** No, this is a great opportunity for us. Management loved our Docker container demo and wants us to explore adopting a microservices architecture.

**Amita:** Microservices? Like apps for phones and watches?

**Andy:** No, microservices are typical apps, like our web app. The main difference is that instead of building and deploying a single monolithic app, we refactor any components that would be better maintained and managed as autonomous services. We then build those services to be good at what they do and deploy them to operate independently.

**Tim:** I'm not sure I like the sound of that. I'm already dealing with so many services across our environments. I don't know if I want more on my plate.

**Andy:** That's an understandable concern. Fortunately, there are some great tools for managing a multitude of containers in a given environment. We've been asked to spike out a multi-container solution for our web app that is orchestrated using Kubernetes. They also want to know how it will impact our DevOps process.

**Mara:** I've been reading up on Kubernetes. Azure has great support for it through Azure Kubernetes Service, and I know there's pipeline support for it in Azure DevOps.

**Amita:** This process sounds like it's going to get complex. How will it impact testing?

**Mara:** It shouldn't be a significant change. Kubernetes offers a way for us to deploy to different namespaces. This enables us to partition our deployments so that we can have entire environments dedicated to testing versus production. And since they all run in the same cluster and use the same containers, the testing experience should offer what we expect to see in production.

**Amita:** Is it going to be hard to keep track of what environment is where?

**Mara:** No, we can use Azure DevOps environments to do all of that. You'll be able to find out where each service is and how it got there by using the portal. It's all automated through the pipeline, so there will be nothing that we have to manually keep track of. The only concern I have now is how much impact it will have on our development experience to build this.

**Andy:** The good news is that the impact is minimal. Assuming we have our projects set up to build Docker containers, all we need to deploy to Kubernetes are some manifest files that describe the services and their deployments.

**Mara:** Have you thought about what we will refactor out as the second container? I know there have been several teams asking us to make our leaderboard available through a web API.

**Andy:** I'm one step ahead of you. I forked the Docker project last night and refactored the leaderboard data functionality into its own microservice. This leaves us with one container for the website and another for a leaderboard API. Both containers are configured to have their own public endpoints that we can share with anyone who wants to use the site or API, regardless of what technology stack their app uses. If the load grows substantially for either, we can scale its containers independently.

**Mara:** This project sounds awesome! Let's get started on updating the release pipeline.

## What is Kubernetes?

Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. It provides a framework for running distributed systems in a declarative, responsive fashion and can run containers across multiple hosts, providing efficient use of resources and increased reliability.

The Tailspin team selected Kubernetes for this scenario because it met all their needs:

- **Complexity of multi-container deployments:** Kubernetes is designed, first and foremost, to automate the processes around deploying and maintaining container deployments.

- **Consistency across environments and stages:** just as containers ensure a consistent deployment for the apps they contain, Kubernetes ensures a consistent deployment for the containers a cluster manages.

- **Azure DevOps support:** Azure DevOps offers first-class support for working with Kubernetes.

- **Ease of development:** the impact of Kubernetes on a source project is comparable to that of adding Docker support, which is minimal and limited to declarative configuration.

Adopting Kubernetes drastically simplifies the process of adopting a microservices architecture that makes use of multiple Docker containers.

---

## Check your knowledge

### 1. Which of the following isn't a good reason to use microservices?

- **✅ You need to deploy software to really small devices, like watches.**
- ❌ You want to modernize your monolithic application functionality into smaller services that can be developed and maintained independently.
- ❌ You want to empower different teams to use the best technologies for each independent service in an overall solution.

**Explanation:** Microservices refer to application architecture patterns, not device size. The term "micro" relates to the scope and functionality of the service, not the physical size of the deployment target. Watches and small devices typically run mobile apps or embedded software, not microservices architectures which are designed for server-side distributed systems.

### 2. How are Docker and Kubernetes similar?

- ❌ They're both effective at packaging applications into self-sufficient containers.
- **✅ They both use declarative manifests to define how their constituent components are exposed.**
- ❌ They're both designed for orchestrating deployed containers.

**Explanation:** Both Docker and Kubernetes use declarative configuration files (Dockerfiles for Docker, YAML manifests for Kubernetes) to define how their components should be configured and exposed. Docker is primarily for containerization, while Kubernetes is for orchestration. Only Kubernetes is designed specifically for orchestrating containers.

### 3. Suppose your team has multiple .NET Core projects in a solution that produces multiple Docker containers. How much overhead does adding Kubernetes support require?

- ❌ A lot. Kubernetes uses its own programming languages and development framework, so applications need to be rebuilt.
- ❌ Quite a bit. Containers will need to be adjusted to load Kubernetes settings and configuration data.
- **✅ Very little. The application should require no changes and the containers can be produced as before. Only one or more Kubernetes manifest files that specify container requirements will need to be added.**

**Explanation:** Kubernetes is primarily an orchestration platform that manages existing containers. The applications and containers themselves typically don't need changes. You only need to add Kubernetes manifest files (YAML) that describe how the containers should be deployed, scaled, and managed within the cluster.




# 8.3 Exercise - Set up your Azure DevOps environment


In this section, you'll configure your Azure DevOps organization to proceed with the rest of this module and create an Azure Kubernetes Service (AKS) environment to deploy your application to.

To achieve these objectives, you will:

- Add a user to your Azure DevOps organization.
- Set up your Azure DevOps project.
- Manage your workflow with Azure Boards.
- Create Azure resources using Azure CLI.
- Create pipeline variables in Azure Pipelines.
- Create a service connection tto authenticate with Azure.
- Update your Kubernetes deployment manifest.

## Add a user to your organization

To complete this module, an Azure subscription is required. You can get started with Azure for free.

Although not necessary to work with Azure DevOps, an Azure subscription is necessary to deploy to Azure resources via Azure DevOps. To make the process more straightforward, use the same Microsoft account to sign in to both your Azure subscription and your Azure DevOps organization.

If you sign in to Azure and Azure DevOps using different Microsoft accounts, you can still proceed by adding a user to your DevOps organization under the Microsoft account associated with your Azure subscription. See [Add users to your organization or project](#) for more details. While adding the user, select the **Basic** access level.

After adding the user with Basic access level, sign out of Azure DevOps and sign back in using the Microsoft account associated with your Azure subscription.

## Get the Azure DevOps project

In this section, you run a template to create your project in Azure DevOps.

### Run the template

Run a template that sets up your Azure DevOps organization.

1. Get and run the ADOGenerator project in Visual Studio or the IDE of your choice.

2. When prompted to **Enter the template number from the list of templates**, enter **40** for **Automate multi-container deployments to Azure Kubernetes Services with Azure Pipelines**, then press Enter.

3. Choose your authentication method. You can set up and use a Personal Access Token (PAT) or use device login.

   > **Note**  
   > If you set up a PAT, make sure to authorize the necessary scopes. For this module, you can use Full access, but in a real-world situation, you should ensure you grant only the necessary scopes.

4. Enter your Azure DevOps organization name, then press Enter.

5. If prompted, enter your Azure DevOps PAT, then press Enter.

6. Enter a project name such as **Space Game - web - Kubernetes**, then press Enter.

7. Once your project is created, go to your Azure DevOps organization in your browser (at `https://dev.azure.com/<your-organization-name>/`) and select the project.

### Fork the repository

If you haven't already, create a fork of the `mslearn-tailspin-spacegame-web-kubernetes` repository.

1. On GitHub, go to the [mslearn-tailspin-spacegame-web-kubernetes](#) repository.

2. Select **Fork** at the top-right of the screen.

3. Choose your GitHub account as the Owner, then select **Create fork**.

> **Important**  
> The unit **Clean up your Azure DevOps environment** in this module includes crucial steps for cleanup. It is recommended to perform these steps to avoid running out of free build minutes. Even if you don't finish this module, it is important to follow the cleanup steps.

### Set your project's visibility

Initially, your fork of the Space Game repository on GitHub is set to public while the project created by the Azure DevOps template is set to private. A public repository on GitHub can be accessed by anyone, while a private repository is only accessible to you and the people you choose to share it with. Similarly, on Azure DevOps, public projects provide read-only access to non-authenticated users, while private projects require users to be granted access and authenticated to access the services.

At the moment, it is not necessary to modify any of these settings for the purposes of this module. However, for your personal projects, you must determine the visibility and access you wish to grant to others. For instance, if your project is open source, you may choose to make both your GitHub repository and your Azure DevOps project public. If your project is proprietary, you would typically make both your GitHub repository and your Azure DevOps project private.

Later on, you may find the following resources helpful in determining which option is best for your project:

- [Use private and public projects](#)
- [Change project visibility to public or private](#)
- [Setting repository visibility](#)

## Move the work item to Doing

In this step, you assign a work item to yourself on Azure Boards and move it to the **Doing** state. In real-world scenarios, you and your team would create work items at the beginning of each sprint or work iteration.

Assigning work items provides you with a checklist to work from and gives other team members visibility into your progress and remaining work. It also helps enforce work-in-progress (WIP) limits to prevent the team from taking on too much work at once.

1. Navigate to **Boards** in Azure DevOps, and then select **Boards** from the menu.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-boards-menu.png)

3. Assign the **Create multi-container version of web site orchestrated with Kubernetes** work item to yourself by selecting the down arrow located at the bottom of the card.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-boards-down-chevron.png)

5. Drag and drop the work item from the **To Do** column to the **Doing** column. You'll move the task to the **Done** column at the end of this module after you complete it.

![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-kubernetes/media/3-azure-boards-wi1-doing.png)

## Create the Azure Kubernetes Service environment

In this step, you create the necessary Azure Kubernetes Service resources to deploy the new container version of the website.

In the previous module, **Create a release pipeline with Azure Pipelines**, you used the Azure portal to create Azure resources. While the portal is useful for exploring Azure capabilities and performing basic tasks, creating components like Azure Kubernetes Service can be a time-consuming process.

In this module, you use the Azure CLI to create the resources required to deploy and run your application on Azure Kubernetes Service. The Azure CLI can be accessed from a terminal or through Visual Studio Code. However, in this module, you access the Azure CLI from Azure Cloud Shell. Cloud Shell is a browser-based shell experience hosted in the cloud, which comes preconfigured with the Azure CLI for use with your Azure subscription.

> **Important**  
> To complete the exercises in this module, you need your own Azure subscription.

### Launch Cloud Shell

1. Navigate to [Azure portal](https://portal.azure.com) and sign in.

2. Select **Cloud Shell** option from the menu, and then choose the **Bash** experience when prompted.

      ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-portal-menu-cloud-shell.png)

   > **Note**  
   > Cloud Shell requires an Azure storage resource to persist any files that you create in Cloud Shell. When you first open Cloud Shell, you're prompted to create a resource group, storage account, and Azure Files share. This setup is automatically used for all future Cloud Shell sessions.

### Select an Azure region

A region refers to one or more Azure datacenters located in a geographic area. Regions such as East US, West US, and North Europe are examples of such areas. Each Azure resource, including an App Service instance, is associated with a region.

To simplify the execution of commands, begin by setting a default region. Once you set a default region, subsequent commands use that region by default, unless you explicitly specify a different region.

1. From Cloud Shell, run the following command to list the regions available in your Azure subscription:

   **Azure CLI**
   ```bash
   az account list-locations \
     --query "[].{Name: name, DisplayName: displayName}" \
     --output table
   ```

2. Select a region from the **Name** column in the output that is geographically close to you. For instance, you could choose `eastasia` or `westus2`.

3. Run the following command to set your default region. Replace `REGION` with the name of the region you chose earlier.

   **Azure CLI**
   ```bash
   az configure --defaults location=<REGION>
   ```

   This example sets `westus2` as the default region.

   **Azure CLI**
   ```bash
   az configure --defaults location=westus2
   ```

### Create Bash variables

Using Bash variables can make the setup process more convenient and less error-prone. This approach helps avoid accidental typos by defining shared text strings as variables that can be used throughout your script.

1. From Cloud Shell, generate a random number to simplify the creation of globally unique names for certain services in the next step.

   **Bash**
   ```bash
   resourceSuffix=$RANDOM
   ```

2. Create globally unique names for your Azure Container Registry and Azure Kubernetes Service instance. Note that these commands use double quotes, which instruct Bash to interpolate the variables using the inline syntax.

   **Bash**
   ```bash
   registryName="tailspinspacegame${resourceSuffix}"
   aksName="tailspinspacegame-${resourceSuffix}"
   ```

3. Create another Bash variable to store the name of your resource group.

   **Bash**
   ```bash
   rgName='tailspin-space-game-rg'
   ```

4. Find the latest AKS version.

   **Azure CLI**
   ```bash
   az aks get-versions
   ```

   Make note of the latest version.

### Create Azure resources

> **Note**  
> In this tutorial, default network settings are used for learning purposes. These settings enable your website to be accessed from the internet. However, in practice, you might choose to configure an Azure virtual network that places your website in a network that isn't internet-routable and is only accessible by you and your team. Later, you could reconfigure your network to make the website available to your users.

1. Run the following command to create a resource group with the name you defined earlier:

   **Azure CLI**
   ```bash
   az group create --name $rgName
   ```

2. Run the `az acr create` command to create an Azure Container Registry with the name you defined earlier:

   **Azure CLI**
   ```bash
   az acr create \
     --name $registryName \
     --resource-group $rgName \
     --sku Standard
   ```

3. Run the `az aks create` command to create an AKS instance with the name you defined earlier. Replace `<latest-AKS-version>` with the version you noted earlier.

   **Azure CLI**
   ```bash
   az aks create \
     --name $aksName \
     --resource-group $rgName \
     --enable-addons monitoring \
     --kubernetes-version <latest-AKS-version> \
     --generate-ssh-keys
   ```

   > **Note**  
   > AKS deployment completion might take 10-15 minutes.

4. Create a variable to store the ID of the service principal configured for the AKS instance:

   **Azure CLI**
   ```bash
   clientId=$(az aks show \
     --resource-group $rgName \
     --name $aksName \
     --query "identityProfile.kubeletidentity.clientId" \
     --output tsv)
   ```

5. Create a variable to store the ID of the Azure Container Registry:

   **Azure CLI**
   ```bash
   acrId=$(az acr show \
     --name $registryName \
     --resource-group $rgName \
     --query "id" \
     --output tsv)
   ```

6. Run the `az acr list` command to retrieve the login server URL for your Azure Container Registry (ACR) instance:

   **Azure CLI**
   ```bash
   az acr list \
    --resource-group $rgName \
    --query "[].{loginServer: loginServer}" \
    --output table
   ```

   Make sure to take note of the login server for your container registry. You need this information later when configuring your pipeline. Here's an example:

   **Output**
   ```
   LoginServer                      
   --------------------------------
   tailspinspacegame4692.azurecr.io
   ```

7. Run the `az role assignment create` command to create a role assignment to authorize the AKS cluster to connect to the Azure Container Registry:

   **Azure CLI**
   ```bash
   az role assignment create \
     --assignee $clientId \
     --role AcrPull \
     --scope $acrId
   ```

> **Important**  
> The unit **Clean up your Azure DevOps environment** in this module includes crucial steps for cleanup. It's recommended to perform these steps to avoid running out of free build minutes. Even if you don't finish this module, it's important to follow the cleanup steps.

## Create a variable group

In this section, you'll add a variable to your pipeline to store the name of your Azure Container Registry. Defining the name of your Azure Container Registry instance as a variable in your pipeline configuration is recommended over hard-coding it. This makes your configuration more reusable and in case the name of your instance changes, you can easily update the variable and trigger your pipeline without having to modify your configuration.

1. Sign in to your Azure DevOps organization, and then navigate to your project.

2. Select **Pipelines**, and then select **Library** from the left navigation pane.

 ![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-kubernetes/media/3-pipelines-library.png)

4. Select **Variable groups**, and then select **+ Variable group** to add a new variable group.

5. In the **Properties** section, enter **Release** for the variable group name.

6. Under the **Variables** section, select **Add**.

7. Enter **RegistryName** for the variable name, and for the value, enter the login server of your Azure Container Registry, such as `tailspinspacegame4692.azurecr.io`.

8. At the top of the page, select **Save** to save your pipeline variable. This is an example of what your variable group might look like

   
   ![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-kubernetes/media/3-library-variable-group.png)

## Create service connections

The next step is to create service connections that allow Azure Pipelines to access your Azure Container Registry and Azure Kubernetes Service instances. By creating these service connections, Azure Pipelines can push your containers and instruct your AKS cluster to pull them in to update the deployed service.

> **Important**  
> Make sure that you're signed in to the Azure portal and Azure DevOps with the same Microsoft account.

### Create a Docker Registry service connection

1. Sign in to your Azure DevOps organization, and then navigate to your project.

2. Select **Project settings** from the bottom corner of the page.

3. Select **Service connections** under the **Pipelines** section.

4. Select **New service connection**, then select **Docker Registry**, and then select **Next**.

5. Near the top of the page, select **Azure Container Registry**, and then select **Service Principal** for authentication type.

6. Enter the following values for each setting:

   | Setting | Value |
   |---------|-------|
   | Subscription | Your Azure subscription |
   | Azure container registry | Select the one you created earlier |
   | Service connection name | Container Registry Connection |

7. Make sure that the checkbox for **Grant access permission to all pipelines** is selected.

8. Select **Save** when you're done.

### Create ARM service connection

Now you'll create an Azure Resource Manager service connection to authenticate with your AKS cluster. We're using an ARM service connection instead of Kubernetes because long-lived tokens are no longer created by default since Kubernetes 1.24. Check out this DevOps blog post for more details: [Service Connection guidance for AKS customers using Kubernetes tasks](#).

1. Select **New service connection**, select **Azure Resource Manager**, and then select **Next**.

2. Select **Service Principal (automatic)**, and then select **Next**.

3. Select **Subscription** for scope level.

4. Enter the following values for each setting.

   | Setting | Value |
   |---------|-------|
   | Subscription | Your Azure subscription |
   | Resource group | Select the one you created earlier |
   | Service connection name | Kubernetes Cluster Connection |

5. Make sure that the checkbox for **Grant access permission to all pipelines** is selected.

6. Select **Save** when you're done.

## Create a pipeline environment

1. Select **Pipelines**, and then select **Environments**.

  
   ![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-kubernetes/media/3-pipelines-environments.png)

3. Select **Create environment** to create a new environment.

4. In the **Name** field, enter **Dev**.

5. Select **None** from the **Resource** section, and then select **Create** to create your pipeline environment.

## Update the Kubernetes deployment manifest

In this section, you'll update the Kubernetes manifest `deployment.yml` to point to the container registry you created earlier.

1. Navigate to your GitHub account and select the repository you forked for this module: `mslearn-tailspin-spacegame-web-kubernetes`.

2. Open the `manifests/deployment.yml` file in edit mode.

     ![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-kubernetes/media/3-github-edit-mode.png)

4. Change the container image references to use your ACR login server. The following manifest uses `tailspinspacegame2439.azurecr.io` as an example.

   **yml**
   ```yaml
   apiVersion : apps/v1
   kind: Deployment
   metadata:
     name: web
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: web
     template:
       metadata:
         labels:
           app: web
       spec:
         containers:
           - name: web
             image: tailspinspacegame4692.azurecr.io/web
             ports:
             - containerPort: 80

   apiVersion : apps/v1
   kind: Deployment
   metadata:
     name: leaderboard
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: leaderboard
     template:
       metadata:
         labels:
           app: leaderboard
       spec:
         containers:
           - name: leaderboard
             image: tailspinspacegame4692.azurecr.io/leaderboard
             ports:
             - containerPort: 80
   ```

5. Commit the changes to your main branch.




# 8.4 Exercise - Deploy a multi-container solution to a Kubernetes cluster


The release pipeline provided with your project is designed to build the solution as a Docker container and deploy it to Azure App Service. To support the deployment of multiple containers to a Kubernetes cluster, you need to modify this pipeline.

In this unit, you'll learn how to:

- Update the pipeline to trigger on a commit to the main branch.
- Define variables to be shared across the pipeline.
- Build and publish Docker images.
- Publish Kubernetes manifests.
- Add a task to create an image pull secret for use between your Kubernetes and container registry instances.
- Deploy updated images to a Kubernetes cluster.

## Update the pipeline to support triggers

1. Sign in to your Azure DevOps organization, and then navigate to your project.

2. Select **Pipelines**, and then select your pipeline.

3. Select **Edit** to edit your `azure-pipelines.yml`.

**Andy:** This was the build stage we had in place for the previous single-container solution. I knew it wasn't going to run properly, so I disabled it. We can start off by re-enabling triggers on commits to the main branch.

4. Replace the existing trigger line at the top of the file with the following snippet. This triggers a pipeline run every time a commit is made to the main branch.

   **yml**
   ```yaml
   trigger:
   - 'main'
   ```

## Define variables accessible across pipeline

**Andy:** We're going to need to add two pipeline variables. One for specifying the name of the leaderboard repository, which is `leaderboard`. The other is for the name of the image pull secret used for sharing between AKS and ACR instances during deployment.

Add the following highlighted code to the variables section.

**yml**
```yaml
variables:
  buildConfiguration: 'Release'
  leaderboardRepository: 'leaderboard'
  webRepository: 'web'
  tag: '$(Build.BuildId)'
  imagePullSecret: 'secret'
```

## Build and publish Docker image to Azure Container Registry

**Andy:** We already have a task for building the web app as a Docker container, which we publish to our container registry. We can just use a second task to do the same for our leaderboard.

Add a second `Docker@2` task to build and publish the leaderboard container using the following highlighted snippet. Add this task right after the web container task.

**yml**
```yaml
- task: Docker@2
  displayName: 'Build and push the web image to container registry'
  inputs:
    command: buildAndPush
    buildContext: $(Build.Repository.LocalPath)
    repository: $(webRepository)
    dockerfile: '$(Build.SourcesDirectory)/Tailspin.SpaceGame.Web/Dockerfile'
    containerRegistry: 'Container Registry Connection'
    tags: |
      $(tag)

- task: Docker@2
  displayName: 'Build and push the leaderboard image to container registry'
  inputs:
    command: buildAndPush
    buildContext: $(Build.Repository.LocalPath)
    repository: $(leaderboardRepository)
    dockerfile: '$(Build.SourcesDirectory)/Tailspin.SpaceGame.LeaderboardContainer/Dockerfile'
    containerRegistry: 'Container Registry Connection'
    tags: |
      $(tag)
```

> **Tip**  
> Make sure that the task you add here uses consistent indentation with the previous task as whitespace is important in a YAML file.

## Publish the Kubernetes manifests

**Andy:** I think we can move on to the next stage. Do you see anything missing?

**Mara:** You mentioned that there were some manifest files in the source project that define the deployment, and services Kubernetes needs when we deploy. We should publish those before we finish this stage.

**Andy:** Do we need to? Won't they still be on the local disk?

**Mara:** They would be if we were adding the deployment tasks within the same stage as the build. However, since our deployment tasks happen in their own Deploy stage, it runs on a fresh environment, probably even on a different agent. We should be sure to publish anything this stage produces that the other stage needs.

**Andy:** That's a great point. Is it easy to do? We just need to ensure the manifests folder is copied to the new agent.

**Mara:** That's what the `PublishBuildArtifacts@1` task is for. It's so common that there's even a shorthand for it, `publish`.

Add a `publish` task that stores the manifests folder for a future stage as shown in the following code snippet. Make sure that the indentation of this task matches that of the previous task.

**yml**
```yaml
- task: Docker@2
  displayName: 'Build and push the leaderboard image to container registry'
  inputs:
    command: buildAndPush
    buildContext: $(Build.Repository.LocalPath)
    repository: $(leaderboardRepository)
    dockerfile: '$(Build.SourcesDirectory)/Tailspin.SpaceGame.LeaderboardContainer/Dockerfile'
    containerRegistry: 'Container Registry Connection'
    tags: |
      $(tag)

- publish: '$(Build.SourcesDirectory)/manifests'
  artifact: manifests
```

## Replace the deploy stage

**Mara:** I'm going to replace our existing Deploy stage with one that uses a deployment job. A deployment job is a special kind of job that allows us to associate our deployment with the Azure DevOps environment created earlier. This makes it easier to track deployment history, which will be especially useful as our solutions get more sophisticated.

Remove the existing Deploy stage (everything after the build stage) and replace it with the following snippet. Take note of the highlighted line that indicates the deployment environment to be utilized.

**yml**
```yaml
- stage: 'Deploy'
  displayName: 'Deploy the containers'
  dependsOn: Build
  jobs:
  - deployment: Deploy
    displayName: Deploy
    pool:
      vmImage: 'ubuntu-20.04'
    environment: 'Dev'
    variables:
    - group: Release
    strategy:
      runOnce:
        deploy:
          steps:
```

**Mara:** The first step we'll add in the deployment stage is to download the manifest artifacts published earlier using the `DownloadBuildArtifacts@0` task.

**Andy:** Let me guess, is there a download shorthand for that task?

**Mara:** Exactly correct! We can use the `current` specifier to indicate that we want the artifact from the current run of the pipeline.

Add the highlighted lines as the first step of the Deploy stage.

**yml**
```yaml
- stage: 'Deploy'
  displayName: 'Deploy the containers'
  dependsOn: Build
  jobs:
  - deployment: Deploy
    displayName: Deploy
    pool:
      vmImage: 'ubuntu-20.04'
    environment: 'spike.default'
    variables:
    - group: Release
    strategy:
      runOnce:
        deploy:
          steps:
          - download: current
            artifact: manifests
```

**Andy:** Now we need to create an image pull secret that will be shared between our ACR and AKS instances. Do you know if there's a task we can use?

**Mara:** I was just looking that up, and we're in luck. The `KubernetesManifest@0` task supports an action to create the secret needed.

### Kubernetes manifest task

The Kubernetes manifest task is designed to manage all of the mainstream deployment operations required for Kubernetes. It supports multiple action options that range from creating secrets to deploying images. In this case, the `createSecret` action is used, along with the following parameters:

- `action` indicates the feature to run. In this case, `createSecret` creates the shared secret.
- `connectionType` specifies the type of service connection to use. Options: `azureResourceManager` or `kubernetesServiceConnection`.
- `secretName` specifies the name of the secret to create.
- `dockerRegistryEndpoint` specifies the name of the Azure Container Registry Services connection.
- `azureSubscriptionConnection` specifies the name of the ARM Services connection.
- `azureResourceGroup` specifies the name of your resource group.
- `kubernetesCluster` specifies the name of your AKS cluster.
- `namespace` specifies the Kubernetes namespace this action applies to.

Add the following snippet to the end of your pipeline. Make sure that both the resource group name and the cluster name match the names of the ones you created earlier. Ensure that the indentation of this task matches that of the download task.

**yml**
```yaml
- task: KubernetesManifest@1
  displayName: Create imagePullSecret
  inputs:
    action: createSecret
    connectionType: azureResourceManager
    secretName: $(imagePullSecret)
    dockerRegistryEndpoint: 'Container Registry Connection'
    azureSubscriptionConnection: 'Kubernetes Cluster Connection'
    azureResourceGroup: 'tailspin-space-game-rg'
    kubernetesCluster: 'tailspinspacegame-24591'
    namespace: 'default'
```

**Andy:** The final step is to trigger the deployment of our images to the Kubernetes cluster. Based on the documentation, it looks like we can use the same task but with a different action and parameters.

- `action` indicates the feature to run. In this case, `deploy` to deploy to AKS cluster.
- `connectionType` specifies the type of service connection to use. Options: `azureResourceManager` or `kubernetesServiceConnection`.
- `azureSubscriptionConnection` specifies the name of the ARM Services connection.
- `azureResourceGroup` specifies the name of your resource group.
- `kubernetesCluster` specifies the name of your AKS cluster.
- `namespace` specifies the Kubernetes namespace this action applies to.
- `imagePullSecrets` specifies the list of secrets needed to pull from the container registry.
- `containers` specifies the list of container images to deploy.

Add the following snippet to the end of the pipeline. Make sure that both the resource group name and the cluster name match the names of the ones you created earlier. Ensure that the indentation of this task matches that of the previous task.

**yml**
```yaml
- task: KubernetesManifest@1
  displayName: Deploy to Kubernetes cluster
  inputs:
    action: deploy
    connectionType: azureResourceManager
    azureSubscriptionConnection: 'Kubernetes Cluster Connection'
    azureResourceGroup: 'tailspin-space-game-rg'
    kubernetesCluster: 'tailspinspacegame-24591'
    namespace: 'default'
    manifests: |
      $(Pipeline.Workspace)/manifests/deployment.yml
      $(Pipeline.Workspace)/manifests/service.yml
    imagePullSecrets: |
      $(imagePullSecret)
    containers: |
      $(RegistryName)/$(webRepository):$(tag)
      $(RegistryName)/$(leaderboardRepository):$(tag)
```

## Run your pipeline

1. Select **Save** from the upper-right corner of the page. Select **Save** to confirm your commit message.

2. Select **Run**, confirm your branch name and then select **Run** to trigger a pipeline run.

3. Select **Pipelines**, and then select your pipeline to view the logs as your pipeline runs.

4. After the pipeline run is complete, select **Environments** from the left pane, and then select the **Dev** environment to view your deployment jobs.

Now let's go check out our deployed web app and API endpoint. To do so, we need to get the external IP addresses for both the web and leaderboard services.

5. Navigate to [Azure portal](https://portal.azure.com), select your AKS cluster, and then select **Services and ingresses**.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-kubernetes/media/aks-external-ip.png)

7. Select the **External IP** for your web service to view your site on AKS.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-kubernetes/media/4-space-game.png)

9. Go back to your Azure portal window where you left off and then copy the **External IP** for your leaderboard service. This IP address is where the leaderboard API is publicly hosted.

10. Replace the placeholder in the following link with the external IP you copied. You can also add a `pageSize=10` query parameter to make it easier to view the JSON response in your browser. Use a URL like the following one in a new browser tab.

   ```
   http://[IP]/api/Leaderboard?pageSize=10
   ```

11. You can view the raw JSON response from the leaderboard API hosted in your AKS cluster. You now have a REST API that you can call from other applications.


   ![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-kubernetes/media/4-leaderboard-api.png)

**Andy:** This turned out great! I think using Kubernetes would be a great way for us to adopt a broader microservices strategy.




# 8.5 Exercise - Clean up your Azure DevOps environment


After completing the assigned tasks for this module, the next steps involve cleaning up your Azure resources, transitioning the work item to the **Done** state on Azure Boards, and cleaning up your Azure DevOps environment.

> **Important**  
> Performing this cleanup is essential in order to to prevent incurring charges for Azure resources beyond the completion of this module.

## Clean up Azure resources

The easiest way to clean up your Azure resources is to delete their parent resource group. When you delete a resource group, you delete all resources in that group. To delete your resource group:

1. Navigate to the Azure portal and sign in.

2. Select **Cloud Shell** from the menu, and then select **Bash**.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-portal-menu-cloud-shell.png)

3. Run the following command to delete the resource group you created. Type in **y** when prompted to confirm the deletion.

   **Azure CLI**
   ```bash
   az group delete --name tailspin-space-game-rg
   ```

4. Optionally, after the previous command finishes, you can run the following command to confirm the deletion. You'll notice that the resource group *tailspin-space-game-rg* no longer appears in the list.

   **Azure CLI**
   ```bash
   az group list --output table
   ```

## Move the work item to Done

In this step, you move the work item that you previously assigned to yourself in this module to the **Done** column. In practice, **Done** typically means delivering working software to users. However, for the purposes of this learning module, it means that the specific goal was accomplished. To complete the work item:

1. Navigate to your Azure DevOps project, and then select **Boards** then **Boards**.

2. Move the **Create multi-container version of web site orchestrated with Kubernetes** work item to the **Done** column.

![](https://learn.microsoft.com/en-us/training/azure-devops/deploy-kubernetes/media/5-azure-boards-wi1-done.png)

## Disable the pipeline or delete your project

This learning path provides a template for each module that you can use to create a fresh environment. If you run multiple templates, you end up with multiple Azure Pipelines projects that point to the same GitHub repository. This setup can cause multiple pipelines to run each time you push a change to your GitHub repository, which can create issues. Therefore, before moving to the next module, you should disable or delete the pipeline to avoid losing free build minutes.

Choose one of the following options:

### Option 1: Disable the pipeline

Disable the pipeline to stop it from processing new requests. You can choose to re-enable your pipeline later if you wish to. This option is suitable if you want to retain your DevOps project and deployment pipeline for future reference.

#### To disable the pipeline:

1. Select **Pipelines**, and then select your pipeline.

2. Select **Settings** from the drop-down menu.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-pipelines-settings-button.png)

4. Select **Disabled** and then select **Save**.

### Option 2: Delete the Azure DevOps project

If you don't need your DevOps project for future reference, you can delete it. For future modules, you can run another template that spins up a new project in the state where this project leaves off. This option is suitable if you're certain you won't need this project again.

#### To delete the project:

1. Navigate to your project in the Azure DevOps portal.

2. Select **Project settings** from the bottom-left corner.

3. From the **Overview** section, scroll all the way down and then select **Delete**.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/azure-devops-delete-project.png)

5. Confirm the project name and then select **Delete** to delete your project.


# 8.6 Summary

Great work! In this module, you updated a release pipeline to build, publish, and deploy the team's multi-container solution to Azure Kubernetes Service. The team is now well on its way to implementing a broader microservices strategy that offers increased agility in its development and operations.

While this module focused on orchestrating a collection of Docker containers using Kubernetes, the fundamentals covered apply across a wide range of build and deployment targets. You can also see how Azure Pipelines can scale to support even the most sophisticated scenarios.

## Learn more

In this module, you worked with a microservices solution using containers. However, there are many ways to implement microservice solutions in Azure using a wide variety of technologies. To learn more, see [Building microservices on Azure](#).

The microservices solution in this module had been refactored from a larger monolithic application. To learn more about migrating larger applications into smaller services, see [Decompose a monolithic application into a microservices architecture](#).

The microservices solution in this module used various platforms and services, including Docker, Azure Container Registry, and Kubernetes. To learn more about these and related container-centric technologies in Azure, such as Azure Container Instances and App Service, see the [Administer containers in Azure](#) learning path.

## Learning path summary

Congratulations. You completed the final module in the *Deploy applications with Azure DevOps* learning path. The main focus of this learning path is deploying applications by using Azure Pipelines.

In this learning path, you accomplished a lot, including:

- Building a basic release pipeline that deploys a web application to App Service.
- Expanding your basic release pipeline to a multistage pipeline that deploys to various development, test, and staging environments.
- Running both functional and nonfunctional tests in the pipeline.
- Implementing a blue-green deployment that updates the application and requires minimal downtime.
- Extending pipelines to add support for different deployment targets, such as Azure Functions and Kubernetes.

You can apply what you learned to the applications and services that you work on.




