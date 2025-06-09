


# Automate your workflow with GitHub Actions Part 1 of 2
https://learn.microsoft.com/en-us/training/paths/github-actions/

Learn how GitHub Actions enables you to automate your software development cycle. This is part 1 of a two part series.

In this learning path, you'll:

* Plan automation of your software development life cycle with GitHub Actions workflows.
* Use GitHub Actions to automatically build your application.
* Use GitHub Script to interact with the GitHub API.
* Publish automatically and securely your code libraries or Docker images with GitHub Packages.

## Prerequisites

* A GitHub account


# 1 Automate development tasks by using GitHub Actions

Create a basic GitHub Action and use that action in a workflow.

### Learning objectives

In this module, you will:
- Describe GitHub Actions, the types of actions, and where to find them.
- Plan an automation of your software development lifecycle with GitHub Actions workflows.
- Create a container action and have it run in a workflow triggered by a push event to your GitHub repository.

# 1.1 Introduction

GitHub Actions optimize code-delivery time, from idea to deployment, on a community-powered platform.

Suppose you manage a team that's developing a web site that will improve your customers' experience when they contact product support. This project is important to upper management. They want a high-quality site, and they want to publish it soon. You need to make sure your team is producing code that tests, builds, and deploys quickly once a feature is implemented. On top of that, your IT department wants to automate creating and tearing down the project's infrastructure. You decide to use continuous integration (CI) and continuous delivery (CD) to automate all the build, test, and deployment tasks. You're also going to adopt infrastructure as code (IaC) to automate the IT tasks.

There are several tools available to help you achieve these goals. However, because you're already using GitHub for your code repository, you decide to investigate GitHub Actions to see if it provides the automation you need.

In this module, you'll be introduced to GitHub Actions and workflows. In subsequent modules, you'll use what you learn here to implement continuous integration, continuous delivery, and infrastructure as code.

## Learning objectives

In this module, you'll:

* Learn what GitHub Actions are, the types of actions, and where to find them.
* Identify the required components within a GitHub Actions workflow file.
* Plan the automation of your software-development lifecycle with GitHub Actions workflows.
* Create a container action and have it run in a workflow that's triggered by a push event to your GitHub repository.



# 1.2 How does GitHub Actions automate development tasks?

Here, we'll introduce GitHub Actions and workflows. You'll learn the types of actions you can use and where to find them. You'll also look at examples of these types of actions and how they fit in a workflow.

## GitHub decreases time from idea to deployment
GitHub is designed to help teams of developers and DevOps engineers build and deploy applications quickly. There are many features in GitHub that enable this, but they generally fall into one of two categories:

**Communication**: Consider all of the ways that GitHub makes it easy for a team of developers to communicate about the software development project: code reviews in pull requests, GitHub issues, project boards, wikis, notifications, and so on.

**Automation**: GitHub Actions lets your team automate workflows at every step in the software-development process, from integration to delivery to deployment. It even lets you automate adding labels to pull requests and checking for stale issues and pull requests.

When combined, these features have allowed thousands of development teams to effectively decrease the amount of time it takes from their initial idea to deployment.

## Use workflow automation to decrease development time
We'll focus on automation in this module. Let's take a moment to understand how teams can use automation to reduce the amount of time it takes to complete a typical development and deployment workflow.

Consider all of the tasks that must happen after the code is written, but before you can reliably use the code for its intended purpose. Depending on your organization's goals, you'll likely need to perform one or more of the following tasks:

* Ensure the code passes all unit tests.
* Perform code quality and compliance checks to make sure the source code meets the organization's standards.
* Check the code and its dependencies for known security issues.
* Build the code integrating new source from (potentially) multiple contributors.
* Ensure the software passes integration tests.
* Version the new build.
* Deliver the new binaries to the appropriate filesystem location.
* Deploy the new binaries to one or more servers.
* If any of these tasks don't pass, report the issue to the proper individual or team for resolution.

The challenge is to do these tasks reliably, consistently, and in a sustainable manner. This is an ideal job for workflow automation. If you're already relying on GitHub, you'll likely want to set up your workflow automation using GitHub Actions.

## What is GitHub Actions?
GitHub Actions are packaged scripts to automate tasks in a software-development workflow in GitHub. You can configure GitHub Actions to trigger complex workflows that meet your organization's needs. The trigger can happen each time developers check new source code into a specific branch, at timed intervals, or manually. The result is a reliable and sustainable automated workflow, which leads to a significant decrease in development time.

## Where can you find GitHub Actions?
GitHub Actions are scripts that adhere to a yml data format. Each repository has an Actions tab that provides a quick and easy way to get started with setting up your first script. If you see a workflow that you think might be a great starting point, just select the Configure button to add the script and begin editing the source yml.

![](https://learn.microsoft.com/en-us/training/github/github-actions-automate-tasks/media/github-actions-automate-development-tasks-01.png)

Screenshot of the *Actions tab* in GitHub Actions displaying a simple workflow and a button to set up this workflow.

However, beyond those GitHub Actions featured on the Actions tab, you can:

* Search for GitHub Actions in the GitHub Marketplace. The GitHub Marketplace allows you to discover and purchase tools that extend your workflow.
* Search for open-source projects. For example, the GitHub Actions organization features many popular open-source repos containing GitHub Actions you can use.
* Write your own GitHub Actions from scratch. You can make them open source, or even publish them to the GitHub Marketplace.

### Using open-source GitHub Actions
Many GitHub Actions are open source and available for anyone who wants to use them. However, just like with any open-source software, you need to carefully check them before using them in your project. Similar to recommended community standards with open-source software such as including a README, code of conduct, contributing file, and issue templates, you can follow these recommendations when using GitHub Actions:

* Review the action's action.yml file for inputs, outputs, and to make sure the code does what it says it does.
* Check if the action is in the GitHub Marketplace. This is a good check, even if an action doesn't have to be on the GitHub Marketplace to be valid.
* Check if the action is verified in the GitHub Marketplace. This means that GitHub has approved the use of this action. However, you should still review it before using it.
* Include the version of the action you're using by specifying a Git ref, SHA, or tag.

## Types of GitHub actions
There are three types of GitHub actions: container actions, JavaScript actions, and composite actions.

With **container actions**, the environment is part of the action's code. These actions can only be run in a Linux environment that GitHub hosts. Container actions support many different languages.

**JavaScript actions** don't include the environment in the code. You'll have to specify the environment to execute these actions. You can run these actions in a VM (virtual machine) in the cloud or on-premises. JavaScript actions support Linux, macOS, and Windows environments.

**Composite actions** allow you to combine multiple workflow steps within one action. For example, you can use this feature to bundle together multiple run commands into an action, and then have a workflow that executes the bundled commands as a single step using that action.

## The anatomy of a GitHub action
Here's an example of an action that performs a git checkout of a repository. This action, actions/checkout@v1, is part of a step in a workflow. This step also builds the Node.js code that was checked out. We'll talk about workflows, jobs, and steps in the next section.

**yml**

```
steps:
  - uses: actions/checkout@v1
  - name: npm install and build webpack
    run: |
      npm install
      npm run build
```

Suppose you want to use a container action to run containerized code. Your action might look like this:

**yml**

```
name: "Hello Actions"
description: "Greet someone"
author: "octocat@github.com"

inputs:
    MY_NAME:
      description: "Who to greet"
      required: true
      default: "World"

runs:
    uses: "docker"
    image: "Dockerfile"

branding:
    icon: "mic"
    color: "purple"
```

Notice the inputs section. Here, you're getting the value of a variable called MY_NAME. This variable will be set in the workflow that runs this action.

In the runs section, notice you specify docker in the uses attribute. When you do this, you'll need to provide the path to the Docker image file. Here, it's called Dockerfile. We won't get into the specifics of Docker here, but if you'd like more information, check out the Introduction to Docker Containers module.

The last section, branding, personalizes your action in the GitHub Marketplace if you decide to publish it there.

You can find a complete list of action metadata at Metadata syntax for GitHub Actions.

## What is a GitHub Actions workflow?
A GitHub Actions workflow is a process that you set up in your repository to automate software-development lifecycle tasks, including GitHub Actions. With a workflow, you can build, test, package, release, and deploy any project on GitHub.

To create a workflow, you add actions to a .yml file in the .github/workflows directory in your GitHub repository.

In the exercise coming up, your workflow file main.yml will look like this:

**yml**

```
name: A workflow for my Hello World file
on: push
jobs:
  build:
    name: Hello world action
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v1
    - uses: ./action-a
      with:
        MY_NAME: "Mona"
```

Notice the on: attribute. This is a trigger to specify when this workflow will run. Here, it triggers a run when there's a push event to your repository. You can specify single events like on: push, an array of events like on: [push, pull_request], or an event-configuration map that schedules a workflow or restricts the execution of a workflow to specific files, tags, or branch changes. The map might look something like this:

**yml**

```
on:
  # Trigger the workflow on push or pull request,
  # but only for the main branch
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  # Also trigger on page_build, as well as release created events
  page_build:
  release:
    types: # This configuration doesn't affect the page_build event above
      - created
```

An event will trigger on all activity types for the event unless you specify the type or types. For a comprehensive list of events and their activity types, see: Events that trigger workflows in the GitHub documentation.

A workflow must have at least one job. A job is a section of the workflow associated with a runner. A runner can be GitHub-hosted or self-hosted, and the job can run on a machine or in a container. You'll specify the runner with the runs-on: attribute. Here, you're telling the workflow to run this job on ubuntu-latest.

Each job will have steps to complete. In our example, the step uses the action actions/checkout@v1 to check out the repository. What's interesting is the uses: ./action-a value, which is the path to the container action that you build in an action.yml file.

The last part of this workflow file sets the MY_NAME variable value for this workflow. Recall the container action took an input called MY_NAME.

For more information on workflow syntax, see Workflow syntax for GitHub Actions

## GitHub-hosted versus self-hosted runners
We briefly mentioned runners as being associated with a job. A runner is simply a server that has the GitHub Actions runner application installed. In the previous workflow example, there was a runs-on: ubuntu-latest attribute within the jobs block, which told the workflow that the job will run using the GitHub-hosted runner that's running in the ubuntu-latest environment.

When it comes to runners, there are two options from which to choose: GitHub-hosted runners or self-hosted runners. If you use a GitHub-hosted runner, each job runs in a fresh instance of a virtual environment. The GitHub-hosted runner type you define, runs-on: {operating system-version} then specifies that environment. With self-hosted runners, you need to apply the self-hosted label, its operating system, and the system architecture. For example, a self-hosted runner with a Linux operating system and ARM32 architecture would look like the following: runs-on: [self-hosted, linux, ARM32].

Each type of runner has its benefits, but GitHub-hosted runners offer a quicker and simpler way to run your workflows, albeit with limited options. Self-hosted runners are a highly configurable way to run workflows in your own custom local environment. You can run self-hosted runners on-premises or in the cloud. You can also use self-hosted runners to create a custom hardware configuration with more processing power or memory. This will help to run larger jobs, install software available on your local network, and choose an operating system not offered by GitHub-hosted runners.

## GitHub Actions may have usage limits
GitHub Actions has some usage limits, depending on your GitHub plan and whether your runner is GitHub-hosted or self-hosted. For more information on usage limits, check out Usage limits, billing, and administration in the GitHub documentation.

## GitHub hosted larger runners
GitHub offers larger runners for workflows that require more resources. These runners are GitHub-hosted and provide increased CPU, memory, and disk space compared to standard runners. They are designed to handle resource-intensive workflows efficiently, ensuring optimal performance for demanding tasks.

### Runner sizes and labels
Larger runners are available in multiple configurations, providing enhanced vCPUs, RAM, and SSD storage to meet diverse workflow requirements. These configurations are ideal for scenarios such as:

* Compiling large codebases with extensive source files.
* Running comprehensive test suites, including integration and end-to-end tests.
* Processing large datasets for data analysis or machine learning tasks.
* Building applications with complex dependencies or large binary outputs.
* Performing high-performance simulations or computational modeling.
* Executing video encoding, rendering, or other multimedia processing workflows.

To use a larger runner, specify the desired runner label in the runs-on attribute of your workflow file. For example, to use a runner with 16 vCPUs and 64 GB of RAM, you would set runs-on: ubuntu-latest-16core.

**yml**

```
jobs:
  build:
    runs-on: ubuntu-latest-16core
    steps:
      - uses: actions/checkout@v2
      - name: Build project
        run: make build
```

These larger runners maintain compatibility with existing workflows by including the same preinstalled tools as standard ubuntu-latest runners.

For more details on runner sizes for larger runners, refer to the GitHub documentation [https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#machine-sizes-for-larger-runners]

### Managing larger runners
GitHub provides tools to manage larger runners effectively, ensuring optimal resource utilization and cost management. Here are some key aspects of managing larger runners:

**Monitoring usage**
You can monitor the usage of larger runners through the GitHub Actions usage page in your repository or organization settings. This page provides insights into the number of jobs run, the total runtime, and the associated costs.

**Managing access**
To control access to larger runners, you can configure repository or organization-level policies. This ensures that only authorized workflows or teams can use these high-resource runners.

**Cost management**
Larger runners incur additional costs based on their usage. To manage costs, consider the following:

* Use larger runners only for workflows that require high resources.
* Optimize workflows to reduce runtime.
* Monitor billing details regularly to track expenses.

**Scaling workflows**
If your workflows require frequent use of larger runners, consider scaling strategies such as:

* Using self-hosted runners for predictable workloads.
* Splitting workflows into smaller jobs to distribute the load across standard runners.


# 1.3 Identify the components of GitHub Actions

Here, you'll learn about the basic components of a GitHub Actions workflow file.

## The components of GitHub Actions

![](https://learn.microsoft.com/en-us/training/github/github-actions-automate-tasks/media/github-actions-workflow-components.png)

There are several components that work together to run tasks or jobs within a GitHub Actions workflow. In short, an event triggers the *workflow*, which contains a *job*. This job then uses *steps* to dictate which *actions* will run within the workflow. To better see how these components work together, let's take a quick look at each one.

## Workflows
A workflow is an automated process that you add to your repository. A workflow needs to have at least one job, and different events can trigger it. You can use it to build, test, package, release, or deploy your repository's project on GitHub.

## Jobs
The job is the first major component within the workflow. A job is a section of the workflow that will be associated with a runner. A runner can be GitHub-hosted or self-hosted, and the job can run on a machine or in a container. You'll specify the runner with the `runs-on:` attribute. Here, you're telling the workflow to run this job on `ubuntu-latest`. We'll talk more about runners in the next unit.

## Steps
A step is an individual task that can run commands in a job. In our preceding example, the step uses the action `actions/checkout@v2` to check out the repository. What's interesting is the `uses: ./action-a` value. This is the path to the container action that you'll build in an `action.yml` file.

## Actions
The actions inside your workflow are the standalone commands that are executed. These standalone commands can reference GitHub actions such as using your own custom actions, or community actions like the one we use in the preceding example, `actions/checkout@v2`. You can also run commands such as `run: npm install -g bats` to execute a command on the runner.



# 1.4 Configure a GitHub Actions workflow

Here, you'll learn some common configurations within a workflow file. You'll also explore the categories of event types, disabling and deleting workflows, and using specific versions of an action for security best practices.

## Configure workflows to run for scheduled events
As mentioned previously, you can configure your workflows to run when specific activity occurs on GitHub, when an event outside of GitHub happens, or at a scheduled time. The schedule event allows you to trigger a workflow to run at specific UTC times using POSIX cron syntax. This cron syntax has five * fields, and each field represents a unit of time.

Diagram of the five unit-of-time fields for scheduling an event in a workflow file.

![](https://learn.microsoft.com/en-us/training/github/github-actions-automate-tasks/media/scheduled-events.png)

For example, if you wanted to run a workflow every 15 minutes, the schedule event would look like the following:

**yml**

```
on:
  schedule:
    - cron:  '*/15 * * * *'
```

And if you wanted to run a workflow every Sunday at 3:00am, the schedule event would look like this:

**yml**

```
on:
  schedule:
    - cron:  '0 3 * * SUN'
```

You can also use operators to specify a range of values or to dial in your scheduled workflow. The shortest interval you can run scheduled workflows is once every five minutes, and they run on the latest commit on the default or base branch.

## Configure workflows to run for manual events
In addition to scheduled events, you can manually trigger a workflow by using the workflow_dispatch event. This event allows you to run the workflow by using the GitHub REST API or by selecting the Run workflow button in the Actions tab within your repository on GitHub. Using workflow_dispatch, you can choose on which branch you want the workflow to run, as well as set optional inputs that GitHub will present as form elements in the UI.

**yml**

```
on:
  workflow_dispatch:
    inputs:
      logLevel:
        description: 'Log level'     
        required: true
        default: 'warning'
      tags:
        description: 'Test scenario tags'  
```

In addition to workflow_dispatch, you can use the GitHub API to trigger a webhook event called repository_dispatch. This event allows you to trigger a workflow for activity that occurs outside of GitHub. It essentially serves as an HTTP request to your repository asking GitHub to trigger a workflow off an action or webhook. Using this manual event requires you to do two things: send a POST request to the GitHub endpoint /repos/{owner}/{repo}/dispatches with the webhook event names in the request body, and configure your workflow to use the repository_dispatch event.

**Bash**

```
curl \
  -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/octocat/hello-world/dispatches \
  -d '{"event_type":"event_type"}'
```

**yml**

```
on:
  repository_dispatch:
    types: [opened, deleted]
```

## Configure workflows to run for webhook events
Lastly, you can configure a workflow to run when specific webhook events occur on GitHub. You can trigger most webhook events from more than one activity for a webhook. If multiple activities exist for a webhook, you can specify an activity type to trigger the workflow. For example, you can run a workflow for the check_run event, but only for the rerequested or requested_action activity types.

**yml**

```
on:
  check_run:
    types: [rerequested, requested_action]
```

## Repository_dispatch
repository_dispatch is a custom event in GitHub Actions that allows external systems (or even other GitHub workflows) to manually trigger workflows by sending a POST request to the GitHub API. It enables flexible automation and integration with outside tools, scripts, or systems that need to start workflows in your repo.

### Use cases
* Trigger workflows from external CI/CD tools.
* Coordinate multi-repo deployments (e.g., Repo A finishes build → triggers Repo B).
* Start automation based on external events (webhooks, monitoring alerts, CRON jobs outside GitHub).
* Chain workflow executions between repositories or within monorepos.

### Example workflow that listens to repository_dispatch

**yml**

```
name: Custom Dispatch Listener

on:
  repository_dispatch:
    types: [run-tests, deploy-to-prod]  # Optional filtering

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - name: Echo the payload
        run: |
          echo "Event type: ${{ github.event.action }}"
          echo "Payload value: ${{ github.event.client_payload.env }}"
```

**Key elements:**
* **types**: Optional. Defines custom event types like run-tests, deploy-to-prod, etc.
* **github.event.client_payload**: Access to any additional custom data passed in the dispatch event.
* **github.event.action**: Name of the event_type sent.

### Triggering the event via API
You must send a POST request to the GitHub REST API v3 endpoint:

**sh**

```
POST https://api.github.com/repos/OWNER/REPO/dispatches
```

**Authorization**
* Requires a personal access token (PAT) with repo scope.
* For organizations, ensure proper access settings for your token.

**Sample command structure**

**sh**

```
curl -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  https://api.github.com/repos/OWNER/REPO/dispatches \
  -d '{"event_type":"run-tests","client_payload":{"env":"staging"}}'
```

**Payload structure**

**JSON**

```
{
  "event_type": "run-tests",
  "client_payload": {
    "env": "staging"
  }
}
```

### Parameters

| Field | Type | Description | Required |
|-------|------|-------------|----------|
| event_type | string | A custom name for the event. This maps to the types value in your workflow trigger | Yes |
| client_payload | object | Arbitrary JSON payload to send custom data to the workflow (github.event.client_payload) | No |

### Repository_dispatch parameters breakdown
When making a POST request to the GitHub API endpoint, you must pass a JSON body with two main parameters:

* event_type
* client_payload

#### event_type
This is a required custom string you define that GitHub will treat as the "action" or "type" of the dispatch. It's used to identify what triggered the workflow and filter workflows that are listening for specific types.

**Format:**

* Type: string
* Example: "deploy", "run-tests", "sync-db", "build-docker"
* Use in Workflow: Used in listening for specific event types and accessing the value inside the workflow. This helps with the reuse of a single workflow for multiple purposes and makes automation more organized and event-driven.

**Example:**

```
- name: Print event type
  run: echo "Event type: ${{ github.event.action }}"
```

#### client_payload
This is a free-form JSON object that lets you send custom data along with the dispatch. You define the structure, and it's accessible inside the workflow.

**Format:**

* Type: object
* Custom keys and values
* Use in Workflow: Used for multi-environment deployments, versioned releases, or passing context from another system or pipeline and enables parameterized workflows, similar to input arguments.

**Example:**

```
- name: Show payload values
  run: |
    echo "Environment: ${{ github.event.client_payload.env }}"
    echo "Version: ${{ github.event.client_payload.version }}"
```

**Example payload breakdown**

```
{
  "event_type": "deploy-to-prod",
  "client_payload": {
    "env": "production",
    "build_id": "build-456",
    "initiator": "admin_user",
    "services": ["web", "api", "worker"]
  }
}
```

## Use conditional keywords
Within your workflow file, you can access context information and evaluate expressions. Although expressions are commonly used with the conditional if keyword in a workflow file to determine whether a step should run or not, you can use any supported context and expression to create a conditional. It's important to know that when using conditionals in your workflow, you need to use the specific syntax ${{ <expression> }}. This tells GitHub to evaluate an expression rather than treat it as a string.

For example, a workflow that uses the if conditional to check if the github.ref (the branch or tag ref that triggered the workflow run) matches refs/heads/main. In order to proceed, the workflow would look something like this:

**yml**

```
name: CI
on: push
jobs:
  prod-check:
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      ...
```

Notice that in this example, the ${{ }} are missing from the syntax. With some expressions, as in the case of the if conditional, you can omit the expression syntax. GitHub automatically evaluates some of these common expressions, but you can always include them in case you forget which expressions GitHub automatically evaluates.

For more information about workflow syntax and expressions, check out Workflow syntax for GitHub Actions.

## Disable and delete workflows
After adding a workflow to your repository, you might find a situation where you want to temporarily disable the workflow. You can stop a workflow from being triggered without having to delete the file from the repo, either on GitHub or through the GitHub REST API. When you wish to enable the workflow again, you can easily do it using the same methods.

![](https://learn.microsoft.com/en-us/training/github/github-actions-automate-tasks/media/disable-workflow.png)

Screenshot of disabling a workflow on GitHub.

Disabling a workflow can be useful in some of the following situations:

* An error on a workflow is producing too many or wrong requests impacting external services negatively.
* You want to temporarily pause a workflow that isn't critical and is consuming too many minutes on your account.
* You want to pause a workflow that's sending requests to a service that is down.
* You're working on a fork, and you don't need all the functionality of some workflows it includes (like scheduled workflows).

You can also cancel a workflow run that's in progress in the GitHub UI from the Actions tab or by using the GitHub API endpoint DELETE /repos/{owner}/{repo}/actions/runs/{run_id}. Keep in mind that when you cancel a workflow run, GitHub will cancel all of its jobs and steps within that run.

## Use an organization's templated workflow
If you have a workflow that multiple teams use within an organization, you don't need to re-create the same workflow for each repository. Instead, you can promote consistency across your organization by using a workflow template that's defined in the organization's .github repository. Any member within the organization can use an organization template workflow, and any repository within that organization has access to those template workflows.

You can find these workflows by navigating to the Actions tab of a repository within the organization, selecting New workflow, and then finding the organization's workflow template section titled "Workflows created by organization name". For example, the organization called Mona has a template workflow as shown here.

![](https://learn.microsoft.com/en-us/training/github/github-actions-automate-tasks/media/mona-workflow.png)

Screenshot of a template organization workflow called greet and triage by Mona.

## Use specific versions of an action
When referencing actions in your workflow, we recommend that you refer to a specific version of that action rather than just the action itself. By referencing a specific version, you're placing a safeguard from unexpected changes pushed to the action that could potentially break your workflow. Here are several ways you can reference a specific version of an action:

**yml**

```
steps:    
  # Reference a specific commit
  - uses: actions/setup-node@c46424eee26de4078d34105d3de3cc4992202b1e
  # Reference the major version of a release
  - uses: actions/setup-node@v1
  # Reference a minor version of a release
  - uses: actions/setup-node@v1.2
  # Reference a branch
  - uses: actions/setup-node@main
```

Some references are safer than others. For example, referencing a specific branch will run that action off of the latest changes from that branch, which you may or may not want. By referencing a specific version number or commit SHA hash, you're being more specific about the version of the action you're running. For more stability and security, we recommend that you use the commit SHA of a released action within your workflows.



# 1.5 Exercise - Create and run a basic GitHub Actions workflow

This exercise checks your knowledge on creating a GitHub Action and using it in a workflow.

## Getting started

When you select the **Start the exercise on GitHub** button, you'll be navigated to a public GitHub template repository that will prompt you to complete a series of small challenges. Before you can begin the exercise, complete the following tasks:

* Select the **Start course** button or the **Use this template** feature within the template repository. This prompts you to create a new repository. We recommend creating a public repository because private repositories will use Actions minutes.
* After you make your own repository from the template, wait about 20 seconds and refresh.
* Follow the instructions in the repository's README to understand how the exercise works, its learning objectives, and how to successfully complete the exercise.

When you've finished the exercise in GitHub, return here for:

* A quick knowledge check
* A summary of what you've learned
* To earn a badge for completing this module

**Note**  
You don't need to modify any of the workflow files to complete this exercise. **Altering the contents in this workflow can break the exercise's ability to validate your actions, provide feedback, or grade the results**.



# 1.6 Module assessment

Choose the best response for each question.

AI-generated content The question and answer choices in this module assessment were created with AI.

**Provide feedback**

### 1.
**Your organization is integrating GitHub Actions to automate various development tasks. Which platform should you visit to discover and purchase tools that extend your workflow?**

- GitHub Issues
- GitHub Wiki
- **✅ GitHub Marketplace**

**Explanation:** GitHub Marketplace is the platform specifically designed for discovering and purchasing tools, actions, and integrations that extend GitHub functionality and workflows. GitHub Issues is for tracking bugs and features, while GitHub Wiki is for documentation.

### 2.
**Which GitHub Actions component is used to structure a workflow into individual tasks that can run in sequence or parallel?**

- Steps
- **✅ Jobs**
- Actions

**Explanation:** Jobs are the components that structure a workflow into individual tasks. Jobs can run in sequence or parallel, and each job contains steps. Steps are individual tasks within a job, while Actions are the reusable units of code that steps can execute.

### 3.
**Which section of a GitHub Actions workflow file allows you to define inputs for a container action?**

- steps
- **✅ inputs**
- jobs

**Explanation:** The `inputs` section in an action.yml file is specifically designed to define the input parameters that a container action can accept. Steps and jobs are workflow components, not sections for defining action inputs.

### 4.
**You want to create a container action that runs Docker images. What key information must be specified in the action.yml file to ensure the correct Docker image is used?**

- steps section with 'uses' attribute set to 'Dockerfile'
- inputs section with 'Dockerfile' as a default value
- **✅ runs section with 'uses' attribute set to 'docker' and 'image' attribute pointing to the Dockerfile**

**Explanation:** For container actions, the `runs` section must specify `uses: 'docker'` and include an `image` attribute that points to the Dockerfile. This tells GitHub Actions how to build and run the Docker container.

### 5.
**Which attribute in the action metadata is crucial for defining the Docker image used in a container action?**

- author
- icon
- **✅ image**

**Explanation:** The `image` attribute in the `runs` section specifies which Docker image to use for a container action. The `author` and `icon` attributes are metadata for identification and branding, not for defining the Docker image.

### 6.
**What is the role of the 'on' attribute in a GitHub Actions workflow file?**

- To list the steps involved in a job
- **✅ To specify the events that trigger the workflow**
- To define the environment for running jobs

**Explanation:** The `on` attribute defines the events (like push, pull request, schedule) that trigger the workflow to run. Steps are defined in the `steps` section, and environments are defined with `runs-on` or environment-specific settings.

### 7.
**Which section of a GitHub Actions workflow file is responsible for defining the specific activities that occur when the workflow is triggered?**

- Actions
- **✅ Jobs**
- Steps

**Explanation:** The `jobs` section defines all the specific activities (collections of steps) that occur when a workflow is triggered. Steps are individual tasks within jobs, while Actions are reusable units that steps can execute.

### 8.
**You need to create a GitHub Actions workflow to automate the deployment process of your application. Which component is crucial to specify the event that triggers the workflow?**

- **✅ on: attribute**
- jobs: attribute
- steps: attribute

**Explanation:** The `on:` attribute is crucial for specifying which events (push, pull request, schedule, etc.) will trigger the workflow. Without this, the workflow won't know when to run. Jobs and steps define what happens after the workflow is triggered.

### 9.
**In a GitHub Actions workflow, what is the correct order of components from trigger to execution of a container action?**

- **✅ Event -> Workflow -> Job -> Step -> Action**
- Step -> Action -> Job -> Workflow -> Event
- Workflow -> Event -> Action -> Job -> Step

**Explanation:** The correct hierarchy is: Event (trigger) → Workflow (overall process) → Job (group of steps) → Step (individual task) → Action (executable unit). This represents the logical flow from what triggers the workflow to the actual execution of code.



# 1.7 Summary

In this module, you learned about GitHub Actions and how to use them in a workflow.

You can now:

* Describe GitHub Actions, the types of actions, and where to find them.
* Use GitHub Actions workflows to plan the automation of your software-development lifecycle.
* Create a container action, and have it run in a workflow triggered by a push event to your GitHub repository.

## Next steps

To continue your journey with GitHub Actions, check out the next two modules on this learning path. You expand on what you learned here, and use GitHub Actions in continuous integration, continuous delivery, and implementing infrastructure as code.

## Learn more

Here are some links to more information on the topics we discussed in this module.

* GitHub Actions documentation
* GitHub Marketplace
* GitHub created actions
* actions/checkout@v1
* Metadata syntax or GitHub Actions
* Workflow syntax for GitHub Actions
* Events that trigger workflows
* GitHub Actions usage limits
* Introduction to Docker Containers
* Using GitHub-hosted runners
* About self-hosted runners
* The components of GitHub Actions
* Manually running a workflow
* Webhook events and payloads
* Disabling and enabling a workflow
* Sharing workflows, secrets, and runners with your organization
* Scheduled events


# 2 Build continuous integration (CI) workflows by using GitHub Actions

Learn how to create workflows that enable you to use Continuous Integration (CI) for your projects.


# 2.1 Introduction

GitHub Actions can be used to implement *continuous integration* (CI) for code that is maintained in GitHub repositories. CI is the practice of using automation to build and test software every time a developer commits changes to version control. CI helps teams discover issues early in the development process and fix them quickly.

Suppose you want to set up a CI pipeline for your team. The team is developing a website to improve the experience customers have when they contact product support. A number of features are under development and you want to make sure the team can build and test them easily so that each one can be quickly added to the website. Because the code for the project is stored in a GitHub repository, you decide to use GitHub Actions for your CI project.

In this module, you learn how to implement continuous integration using GitHub Actions and workflows in your GitHub repositories.

## Learning objectives

In this module, you:

* Build and test a Node.js project by using GitHub Actions and a templated workflow.
* Debug a failed test using the GitHub Actions Log.
* Customize your workflow with GitHub Actions.

## Prerequisites

* A GitHub account
* The ability to navigate and edit files in GitHub
  * For more information about GitHub, see Introduction to GitHub.
* Basic familiarity with GitHub Actions and workflows
  * If you're unfamiliar with GitHub Actions or workflows, check out Automate development tasks by using GitHub Actions
 


# 2.2 How do I use GitHub Actions to create workflows for CI?

Here, you'll learn about GitHub Actions and workflows for CI.

You learn how to:

* Create a workflow from a template.
* Understand the GitHub Actions logs.
* Test against multiple targets.
* Separate build and test jobs.
* Save and access build artifacts.
* Automate labeling a PR on review.

## Create a workflow from a template
To create a workflow, you start by using a template. A template has common jobs and steps preconfigured for the particular type of automation you're implementing. If you're not familiar with workflows, jobs, and steps, check out the Automate development tasks by using GitHub Actions module.

On the main page of your repository, select the Actions tab and then select New workflow.

On the Choose a workflow page, you can choose from many different templates. One example is the Node.js template, which does a clean install of node dependencies, builds the source code, and runs tests for different versions of Node. Another example is the Python package template, which installs Python dependencies, and runs tests, including lint, across different versions of Python.

In the search box, enter Node.js.


Screenshot showing GitHub Actions tab with the search box highlighted and containing the text 'Node.js'.

![](https://learn.microsoft.com/en-us/training/github/github-actions-ci/media/2-workflow-template-node-js.png)

In the search results, in the Node.js pane, select Configure.

![](https://learn.microsoft.com/en-us/training/github/github-actions-ci/media/2-workflow-template-node-js.png)

Screenshot showing GitHub Actions tab with the Node.js pane highlighted and the Node.js template selected.

You see this default Node.js template workflow, in the newly created file node.js.yml.

**yml**

```
name: Node.js CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:

    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [14.x, 16.x, 18.x]

    steps:
    - uses: actions/checkout@v3
    - name: Use Node.js ${{ matrix.node-version }}
      uses: actions/setup-node@v3
      with:
        node-version: ${{ matrix.node-version }}
        cache: 'npm'
    - run: npm ci
    - run: npm run build --if-present
    - run: npm test
```

Notice the on: attribute. This workflow is triggered on a push to the repository, and when a pull request is made against the main branch.

There's one job in this workflow. Let's review what it does.

The runs-on: attribute specifies that, for the operating system, the workflow runs on ubuntu-latest. The node-version: attribute specifies that there are three builds, one each for Node version 14.x, 16.x, and 18.x. We describe the matrix portion in depth later, when we customize the workflow.

The steps in the job use the GitHub Actions actions/checkout@v3 action to get the code from your repository into the VM, and the actions/setup-node@v3 action to set up the right version of Node.js. We specify that we're going to test three versions of Node.js with the ${{ matrix.node-version }} attribute. This attribute references the matrix we previously defined. The cache attribute specifies a package manager for caching in the default directory.

The last part of this step executes commands used by Node.js projects. The npm ci command installs dependencies from the package-lock.json file, npm run build --if-present runs a build script if it exists, and npm test runs the testing framework. Notice that this template includes both the build and test steps in the same job.

To learn more about npm, check out the npm documentation:

* npm install
* npm run
* npm test

Beyond individual npm commands, teams can benefit from reusable workflows to streamline and standardize repeated automation steps. By leveraging reusable workflows, you can reduce redundancy, improve maintainability, and ensure consistency across your CI/CD pipelines.

### How to utilize reusable workflows to avoid duplication
As teams scale and projects grow, it's common to see the same steps, such as code checkout, dependency installation, testing, and deployment—repeated across multiple workflow files. This kind of duplication not only clutters your codebase but also increases maintenance time when changes are needed. Reusable workflows solve this problem by allowing you to define automation logic once and call it from other workflows. Reusable workflows are special GitHub Actions workflows that can be called by other workflows, much like functions in programming. You create them to share repeated logic like build steps, testing procedures, or deployment strategies. Once created, you can reference them from any other workflow in the same repository or even across different repositories.

Diagram illustrating the concept of reusable workflows in GitHub Actions, showing how a central workflow can be referenced by multiple repositories or workflows.

![](https://learn.microsoft.com/en-us/training/github/github-actions-ci/media/reusable-workflow.png)

**Why use them?**
* **Consistency**: Teams can follow the same automation standards across all projects.
* **Efficiency**: Instead of copying and pasting steps, you just point to a reusable workflow.
* **Ease of Updates**: When a process changes (e.g., a new test step), you update it in one place, and all workflows using it benefit automatically.
* **Scalability**: Ideal for platform or DevOps teams managing multiple services.

Let's explore how to use reusable workflows to improve your projects.

### How to implement reusable workflows
To utilize reusable workflows:

1. Create a reusable workflow in your repo's folder. This file will include the automation steps you want to share—like testing, building, or deploying.
2. You must explicitly enable a workflow to be reusable by configuring it with the workflow_call event.
3. In your main workflows (caller workflows), you then reference this reusable file and provide any required inputs or secrets.

To illustrate the advantages of reusable workflows, consider the following real-world scenario.

### Real-world example
Imagine your organization has 10 microservices and all of them need the same steps to:

* Run tests
* Lint code
* Deploy to a specific environment

Without reusable workflows, every repo contains duplicated logic. With reusable workflows, you:

1. Define the process once in a central file (e.g., ci-standard.yml)
2. Call this file from every service's own workflow, passing in variables like environment or app name

Now, if a new security step or tool is added (like scanning for vulnerabilities), you only need to add it once in the reusable workflow. All 10 services will immediately use the updated process without modifying each one.

By understanding how reusable workflows function and their benefits, you can adopt best practices to maximize their effectiveness and ensure seamless integration into your CI/CD pipelines.

### Best practices
* Centralize your reusable workflows in one repository if you plan to share them across teams.
* Use branches or tags to version your workflows (e.g., use @v1), so changes won't break everything unexpectedly.
* Document inputs and secrets clearly—reusable workflows often rely on inputs and secrets, and teams need to know what to supply.
* Combine with composite actions if you only need to reuse a few steps, not a full workflow.

### Summary
Reusable workflows are a powerful way to enforce consistency, reduce duplication, and scale DevOps practices in any engineering team. Whether you're managing a monorepo, microservices, or open-source libraries, reusable workflows can simplify automation, making CI/CD faster, cleaner, and easier to manage.

## Identify the event that triggered a workflow from its effects
Understanding what triggered a GitHub Actions workflow—whether it was a push to a branch, a pull request, a scheduled job, or a manual dispatch—is crucial for debugging, auditing, and improving CI/CD pipelines. You can identify the triggering event by examining the workflow run, the repository changes, or the issue/pull request involved.

![](https://learn.microsoft.com/en-us/training/github/github-actions-ci/media/workflow-triggers.png)

Diagram illustrating various workflow triggers in GitHub Actions, such as push, pull request, schedule, and manual dispatch.



### What is a workflow trigger?
A workflow trigger is an event that causes a workflow to start. GitHub supports various types of triggers, including:

* push or pull_request (based on code changes)
* workflow_dispatch (manual trigger)
* schedule (cron jobs)
* repository_dispatch (external systems)
* Issue, discussion, and PR events (e.g., issues.opened, pull_request.closed)

### Where to identify the trigger event?
You can identify the trigger event in several ways:

**From the GitHub Actions UI**
1. Navigate to the Actions tab in your repository.
2. Click on a workflow run.
3. The event type (e.g., push, pull_request, workflow_dispatch) is displayed at the top of the workflow run summary.

**Using github.event_name in Logs or workflow**
* GitHub exposes context data during a workflow run. The github.event_name variable tells you which event triggered the workflow.
* You can print it in a step for debugging:

**yml**

```
-name: Show event trigger
  run: echo "Triggered by ${{ github.event_name }}"
```

**Using workflow Run details**
* If you're inspecting workflow runs programmatically (e.g., via the API), the run object includes an event property that specifies the trigger.
* You can also find the commit SHA, actor, and timestamp to trace what caused the trigger.

### Infer the trigger from repository effects
Sometimes you may not have direct access to the workflow run but want to infer what triggered it based on repository activity. Here's how:

| Observed Behavior | Trigger Event |
|-------------------|---------------|
| A new commit pushed to main and workflow ran | push event |
| A new pull request opened or updated | pull_request event |
| A contributor manually ran a workflow | workflow_dispatch |
| Workflow runs every night at a specific time | schedule (cron) |
| Workflow ran after an external service call | repository_dispatch |
| Workflow ran when an issue was labeled or commented on | issues.* event |

By reviewing timestamps, pull request activity, or commit history, you can often pinpoint what action caused the workflow to run.

### Summary
To identify what triggered a workflow:

* Check the workflow run summary in the Actions tab.
* Print or log github.event_name inside the workflow for visibility.
* Compare timestamps and repo activity (commits, PRs, issues) to infer the trigger.
* Use the full event context for deeper investigation.

These practices help with debugging, auditing, and improving workflow reliability across your development and deployment pipelines.

## Describe a workflow's effects from reading its configuration file
To describe a workflow's effects from reading its configuration file, you need to analyze the structure and contents of the ".yml" file stored in .github/workflows/. This file outlines when the workflow runs, what it does, and how it behaves under different conditions.

### Interpret a workflow's effects:

**1. Identify the trigger (on:)** This section tells you when the workflow is initiated. For example:

**yml**

```
on:
  push:
    branches: [main]
  pull_request:
    types: [opened, synchronize]
  workflow_dispatch:
```

**Effect:**

* Runs automatically when code is pushed to the main branch.
* Runs when a pull request is created or updated.
* Can also be triggered manually by a user

**2. Understand the jobs and steps (jobs:)** Jobs describe what the workflow will do. For instance:

**yml**

```
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Install dependencies
        run: npm install
      - name: Run tests
        run: npm test
```

**Effect:**

* Uses a Linux virtual environment (ubuntu-latest).
* Checks out the repository's code.
* Installs project dependencies.
* Runs automated tests.

**3. Evaluate the purpose and outcome**
By reading the configuration, you can describe the intended outcome of the workflow: "This workflow is a Continuous Integration (CI) pipeline. It ensures that any new code pushed to the repository or submitted via pull request is automatically tested. If tests fail, the workflow will indicate this in the GitHub UI, helping maintain code quality."

### Optional features affecting behavior
* **env:** sets environment variables.
* **if:** adds conditional logic to run certain steps only when criteria are met.
* **timeout-minutes:** or **continue-on-error:** influence execution behavior and error handling.

### Summary
From reading a workflow's configuration file, you can describe its effects by identifying:

* **When** it runs (on: section),
* **What** it does (jobs and steps),
* **Where** it runs (runs-on),
* **Why** it runs (its purpose: testing, deploying, linting, etc.),
* **How** it behaves under certain conditions (environment, filters, logic).

## Diagnose a failed workflow run

### 1. Go to the Actions Tab
Navigate to the Actions tab of your repository, then:

* Find the failed run (usually marked with a red ❌)
* Click the failed workflow to open the run summary.

### 2. Review the error in Logs
In the run summary:

* Expand each job and step until you find the one marked as failed.
* Click to view its logs.
* Look for:
  * Error messages
  * Stack traces
  * Exit codes

For example, a failed test might show npm ERR! Test failed. or exit code 1.

### 3. Check the workflow configuration file
Use the .yml file to determine:

* What was each step trying to do?
* If there are environment variables (env:) or conditionals (if:) affecting execution.
* If the failure is due to a missing dependency, syntax error, or misconfigured step.

If this step failed, check:

* Were dependencies installed successfully in the previous step?
* Do test files exist and pass locally?

### 4. Common failure scenarios

| Symptom | Likely Cause |
|---------|--------------|
| Step fails with "command not found" | Missing dependency or wrong setup |
| npm install fails | Corrupt package-lock.json, network issue |
| Test step fails | Unit test issues, missing config or invalid test syntax |
| Permission denied | Incorrect file permissions or missing secrets |

## Identify ways to access the workflow logs from the user interface

### 1. Go to the repository
Navigate to the repository that contains the workflow.

### 2. Click on the Actions tab
Navigate to Actions tab located in the top navigation bar of the repo. This tab shows a history of all workflow runs for that repository.

### 3. Select the workflow name
Choose the relevant workflow from the list. For example, if your .yml file has:

**yml**

```
name: CI Workflow
```

You'll see a link named CI Workflow in the list.

### 4. Choose a specific run
* You'll see a list of runs with status indicators
* Click on the timestamp or commit message of the specific run you want to inspect.

### 5. Expand each job and step
* The run summary page displays jobs as defined in the workflow file (e.g., build, test).
* Click on a job to expand it.
* Inside the job, expand individual steps (e.g., "Install dependencies", "Run tests").

### 6. View log output
* Clicking a step shows the full log output (e.g., console logs, error messages, debug info).
* You can copy, search, or download these logs.

### Summary

| Action | Purpose |
|--------|---------|
| Actions tab | View all workflow runs |
| Select workflow name | Filter runs by workflow |
| Click on a run | See specific job/step results |
| Expand steps | View detailed logs |
| Download logs | For offline or team troubleshooting |

## Action logs for the build
When a workflow runs, it produces a log that includes the details of what happened and any errors or test failures.

If there's an error or if a test fails, you see a red ❌ rather than a green check mark in the logs. You can examine the details of the error or failure to investigate what happened.

![](https://learn.microsoft.com/en-us/training/github/github-actions-ci/media/2-log-details.png)

Screenshot of GitHub Actions log with details on a failed test.

## Customize workflow templates
At the beginning of this module, we described a scenario where you need to set up CI for your team. The Node.js template is a great start, but you want to customize it to better suit your own team's requirements. You want to target different versions of Node and different operating systems. You also want the build and test steps to be separate jobs.

Let's take a look at how you customize a workflow.

**yml**

```
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node-version: [16.x, 18.x]
```

Here, we configured a build matrix for testing across multiple operating systems and language versions. This matrix produces four builds, one for each operating system paired with each version of Node.

Four builds, along with all their tests, produce quite a bit of log information. It might be difficult to sort through it all. In the following sample, we show you how to move the test step to a dedicated test job. This job tests against multiple targets. Separating the build and test steps makes it easier to understand the log.

**yml**

```
test:
  runs-on: ${{ matrix.os }}
  strategy:
    matrix:
      os: [ubuntu-latest, windows-latest]
      node-version: [16.x, 18.x]
  steps:
  - uses: actions/checkout@v3
  - name: Use Node.js ${{ matrix.node-version }}
    uses: actions/setup-node@v3
    with:
      node-version: ${{ matrix.node-version }}
  - name: npm install, and test
    run: |
      npm install
      npm test
    env:
      CI: true
```

## Locate a workflow in a repository

### What are artifacts?
When a workflow produces something other than a log entry, the product is called an artifact. For example, the Node.js build produces a Docker container that can be deployed. This artifact, the container, can be uploaded to storage by using the action actions/upload-artifact and later downloaded from storage by using the action actions/download-artifact.

Storing an artifact preserves it between jobs. Each job uses a fresh instance of a virtual machine (VM), so you can't reuse the artifact by saving it on the VM. If you need your artifact in a different job, you can upload the artifact to storage in one job, and download it for the other job.

### Artifact storage
Artifacts are stored in storage space on GitHub. The space is free for public repositories and some amount is free for private repositories, depending on the account. GitHub stores your artifacts for 90 days.

In the following workflow snippet, notice that in the actions/upload-artifact@main action there's a path: attribute. The value of this attribute is the path to store the artifact. Here, we specify public/ to upload everything to a directory. If we just wanted to upload a single file, we use something like public/mytext.txt.

**yml**

```
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: npm install and build webpack
        run: |
          npm install
          npm run build
      - uses: actions/upload-artifact@main
        with:
          name: webpack artifacts
          path: public/
```

To download the artifact for testing, the build must complete successfully and upload the artifact. In the following code, we specify that the test job depends on the build job.

**yml**

```
test:
    needs: build
    runs-on: ubuntu-latest
```

In the following workflow snippet, we download the artifact. Now the test job can use the artifact for testing.

**yml**

```
steps:
    - uses: actions/checkout@v3
    - uses: actions/download-artifact@main
      with:
        name: webpack artifacts
        path: public
```

For more information about using artifacts in workflows, see Storing workflow data as artifacts in the GitHub documentation.

## Automate reviews in GitHub using workflows
So far, we described starting the workflow with GitHub events such as push or pull-request. We could also run a workflow on a schedule, or on some event outside of GitHub.

Sometimes, we want to run the workflow only after a person performs an action. For example, we might only want to run a workflow after a reviewer approves the pull request. For this scenario, we can trigger on pull-request-review.

Another action we could take is to add a label to the pull request. In this case, we use the pullreminders/label-when-approved-action action.

**yml**

```
    steps:
     - name: Label when approved
       uses: pullreminders/label-when-approved-action@main
       env:
         APPROVALS: "1"
         GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
         ADD_LABEL: "approved"
```

Notice the block called env:. This block is where you set the environment variables for this action. For example, you can set the number of approvers needed. Here, it's one. The secrets.GITHUB_TOKEN authentication variable is required because the action must make changes to your repository by adding a label. Finally, you supply the name of the label to add.

Adding a label could be an event that starts another workflow, such as a merge. We cover this event in the next module on continuous delivery with GitHub Actions.



# 2.3 Customize your workflow with environment variables and artifact data

Here, you learn how to use default and custom environment variables, custom scripts, cache dependencies, and pass artifact data between jobs. You'll also learn how to access the workflow logs from both the GitHub website and REST API endpoints.

## Default environment variables and contexts
Within the GitHub Actions workflow, there are several default environment variables that are available for you to use, but only within the runner that's executing a job. These default variables are case-sensitive, and they refer to configuration values for the system and for the current user. We recommend that you use these default environment variables to reference the filesystem rather than using hard-coded file paths. To use a default environment variable, specify $ followed by the environment variable's name.

**yml**

```
jobs:
  prod-check:
    steps:
      - run: echo "Deploying to production server on branch $GITHUB_REF"
```

In addition to default environment variables, you can use defined variables as contexts. Contexts and default variables are similar in that they both provide access to environment information, but they have some important differences. While default environment variables can only be used within the runner, context variables can be used at any point within the workflow. For example, context variables allow you to run an if statement to evaluate an expression before the runner is executed.

**yml**

```
name: CI
on: push
jobs:
  prod-check:
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying to production server on branch $GITHUB_REF"
```

This example is using the github.ref context to check the branch that triggered the workflow. If the branch is main, the runner is executed and prints "Deploying to production server on branch $GITHUB_REF". The default environment variable $GITHUB_REF is used in the runner to refer to the branch. Notice that default environment variables are all uppercase where context variables are all lowercase.

### The contextual information available in a workflow
Contexts allow you to access information about workflow runs, variables, runner environments, jobs, and steps. Each context is an object that contains properties which can be other objects or strings. The contexts available include: github, env, vars, job, jobs, steps, runner, secrets, strategy, matrix, needs and inputs. Here's a table presents these contexts with their descriptions.

| Context | Description |
|---------|-------------|
| github | Information about the workflow run. For more information, see github context. |
| env | Contains variables set in a workflow, job, or step. For more information, see env context. |
| vars | Contains variables set at the repository, organization, or environment levels. For more information, see vars context. |
| job | Information about the currently running job. For more information, see job context. |
| jobs | For reusable workflows only, contains outputs of jobs from the reusable workflow. For more information, see jobs context. |
| steps | Information about the steps that ran in the current job. For more information, see steps context. |
| runner | Information about the runner that is running the current job. For more information, see runner context. |
| secrets | Contains the names and values of secrets that are available to a workflow run. For more information, see secrets context. |
| strategy | Information about the matrix execution strategy for the current job. For more information, see strategy context. |
| matrix | Contains the matrix properties defined in the workflow that apply to the current job. For more information, see matrix context. |
| needs | Contains the outputs of all jobs that are defined as a dependency of the current job. For more information, see needs context. |
| inputs | Contains the inputs of a reusable or manually triggered workflow. For more information, see inputs context. |

The different contexts are available throughout a workflow run. For example, the secrets context may only be used at certain places within a job. In addition, you may only use some functions in certain places. For example, the hashFiles function isn't available everywhere.

The following table lists the restrictions on where each context and special function can be used within a workflow. The listed contexts are only available for the given workflow key, and you may not use them anywhere else. Unless listed in the table here, you may use a function anywhere.

| Workflow Key | Context | Special Functions |
|--------------|---------|-------------------|
| run-name | github, inputs, vars | None |
| concurrency | github, inputs, vars | None |
| env | github, secrets, inputs, vars | None |
| jobs.<job_id>.concurrency | github, needs, strategy, matrix, inputs, vars | None |
| jobs.<job_id>.container | github, needs, strategy, matrix, vars, inputs | None |
| jobs.<job_id>.container.credentials | github, needs, strategy, matrix, env, vars, secrets, inputs | None |
| jobs.<job_id>.container.env.<env_id> | github, needs, strategy, matrix, job, runner, env, vars, secrets, inputs | None |
| jobs.<job_id>.container.image | github, needs, strategy, matrix, vars, inputs | None |
| jobs.<job_id>.continue-on-error | github, needs, strategy, vars, matrix, inputs | None |
| jobs.<job_id>.defaults.run | github, needs, strategy, matrix, env, vars, inputs | None |
| jobs.<job_id>.env | github, needs, strategy, matrix, vars, secrets, inputs | None |
| jobs.<job_id>.environment | github, needs, strategy, matrix, vars, inputs | None |
| jobs.<job_id>.environment.url | github, needs, strategy, matrix, job, runner, env, vars, steps, inputs | None |
| jobs.<job_id>.if | github, needs, vars, inputs | always, canceled, success, failure |
| jobs.<job_id>.name | github, needs, strategy, matrix, vars, inputs | None |
| jobs.<job_id>.outputs.<output_id> | github, needs, strategy, matrix, job, runner, env, vars, secrets, steps, inputs | None |
| jobs.<job_id>.runs-on | github, needs, strategy, matrix, vars, inputs | None |
| jobs.<job_id>.secrets.<secrets_id> | github, needs, strategy, matrix, secrets, inputs, vars | None |
| jobs.<job_id>.services | github, needs, strategy, matrix, vars, inputs | None |
| jobs.<job_id>.services.<service_id>.credentials | github, needs, strategy, matrix, env, vars, secrets, inputs | None |
| jobs.<job_id>.services.<service_id>.env.<env_id> | github, needs, strategy, matrix, job, runner, env, vars, secrets, inputs | None |
| jobs.<job_id>.steps.continue-on-error | github, needs, strategy, matrix, job, runner, env, vars, secrets, steps, inputs | hashFiles |
| jobs.<job_id>.steps.env | github, needs, strategy, matrix, job, runner, env, vars, secrets, steps, inputs | hashFiles |
| jobs.<job_id>.steps.if | github, needs, strategy, matrix, job, runner, env, vars, steps, inputs | always, canceled, success, failure, hashFiles |
| jobs.<job_id>.steps.name | github, needs, strategy, matrix, job, runner, env, vars, secrets, steps, inputs | hashFiles |
| jobs.<job_id>.steps.run | github, needs, strategy, matrix, job, runner, env, vars, secrets, steps, inputs | hashFiles |
| jobs.<job_id>.steps.timeout-minutes | github, needs, strategy, matrix, job, runner, env, vars, secrets, steps, inputs | hashFiles |
| jobs.<job_id>.steps.with | github, needs, strategy, matrix, job, runner, env, vars, secrets, steps, inputs | hashFiles |
| jobs.<job_id>.steps.working-directory | github, needs, strategy, matrix, job, runner, env, vars, secrets, steps, inputs | hashFiles |
| jobs.<job_id>.strategy | github, needs, vars, inputs | None |
| jobs.<job_id>.timeout-minutes | github, needs, strategy, matrix, vars, inputs | None |
| jobs.<job_id>.with.<with_id> | github, needs, strategy, matrix, inputs, vars | None |
| on.workflow_call.inputs.<inputs_id>.default | github, inputs, vars | None |
| on.workflow_call.outputs.<output_id>.value | github, jobs, vars, inputs | None |

## Setting custom environment variables in a workflow
You can define environment variables that are scoped to the entire workflow utilizing env at the top level of the workflow file. Scoping the contents of a job within a workflow using jobs.<job_id>.env. As well you can scope an environment variable within at a specific step within a job utilizing jobs.<job_id>.steps[*].env.

Next is an example displaying all three scenarios in a workflow file:

**yml**

```
name: Greeting on variable day

on:
  workflow_dispatch

env:
  DAY_OF_WEEK: Monday

jobs:
  greeting_job:
    runs-on: ubuntu-latest
    env:
      Greeting: Hello
    steps:
      - name: "Say Hello Mona it's Monday"
        run: echo "$Greeting $First_Name. Today is $DAY_OF_WEEK!"
        env:
          First_Name: Mona
```

## Use default context in a workflow
Default environment variables are set by GitHub and not defined in a workflow. They're available to use in a workflow in the appropriate context. Most of these variables, other than CI, begin with GITHUB_* or RUNNER_*. The latter two types can't be overwritten. As well, these default variables have a corresponding, and similarly named, context property. For instance, the RUNNER_* series of default variables have a matching context property of runner.*. An example of accessing default variables in a workflow applying these methods can be viewed here:

**yml**

```
on: workflow_dispatch

jobs:
  if-Windows-else:
    runs-on: macos-latest
    steps:
      - name: condition 1
        if: runner.os == 'Windows'
        run: echo "The operating system on the runner is $env:RUNNER_OS."
      - name: condition 2
        if: runner.os != 'Windows'
        run: echo "The operating system on the runner is not Windows, it's $RUNNER_OS."
```

For more information, see Default environment variables in the GitHub user documentation.

## Pass custom environment variables to a workflow
You can pass customer environment variables from one step of a workflow job to subsequent steps within the job. Generate a value in one step of a job, and assign the value to an existing or new environment variable. Next, you write the variable/value pair to the GITHUB_ENV environment file. The environment file can be used by an action, or from a shell command in the workflow job by using the run keyword.

The step that creates or updates the environment variable doesn't have access to the new value, but all subsequent steps in a job have access.

You can view an example here:

**yml**

```
steps:
  - name: Set the value
    id: step_one
    run: |
      echo "action_state=yellow" >> "$GITHUB_ENV"
  - name: Use the value
    id: step_two
    run: |
      printf '%s\n' "$action_state" # This will output 'yellow'
```

## Add environment protections
You can add protection rules for environments defined for your GitHub repository. To add an environment, in your repository:

1. Click on **Settings** Navigation bar of a web interface with tabs like Code, Issues, and Wiki; 'Settings' is highlighted."

![](https://learn.microsoft.com/en-us/training/github/github-actions-ci/media/2b-environments.png)


2. Click on **Environment** on the left panel.

   Screenshot of a settings menu under 'General' with sections for Access, Code and automation, Security, and Integrations. The 'Environments' option is highlighted in red.

3. Use the **New environment** button to add and configure an environment and add protections. GitHub repository settings page showing the 'Environments' section with a message indicating no environments exist and a 'New environment' button highlighted.

![](https://learn.microsoft.com/en-us/training/github/github-actions-ci/media/2b-new-environment.png)

### About environments
Environments are used to describe a general deployment target like production, staging, or development. When a GitHub Actions workflow deploys to an environment, the environment is displayed on the main page of the repository. You can use environments to require approval for a job to proceed, restrict which branches can trigger a workflow, gate deployments with custom deployment protection rules, or limit access to secrets.

Each job in a workflow can reference a single environment. Any protection rules configured for the environment must pass before a job referencing the environment is sent to a runner. The job can access the environment's secrets only after the job is sent to a runner.

When a workflow references an environment, the environment appears in the repository's deployments.

### Environment protection rules
Environment deployment protection rules require specific conditions to pass before a job referencing the environment can proceed. You can use deployment protection rules to require a manual approval, delay a job, or restrict the environment to certain branches. You can also create and implement custom protection rules powered by GitHub Apps to use third-party systems to control deployments referencing environments configured on GitHub. Here's an explanation of these protection rules:

**Required reviewers protection rules**: Use required reviewers to require a specific person or team to approve workflow jobs that reference the environment. You can list up to six users or teams as reviewers. The reviewers must have at least read access to the repository. Only one of the required reviewers needs to approve the job for it to proceed.

You also have the option to prevent self-reviews for deployments to protected environments. If you enable this setting, users who initiate a deployment can't approve the deployment job, even if they're a required reviewer. By enabling self-reviews, it ensures that deployments to protected environments are always reviewed by more than one person.

For more information on reviewing jobs that reference an environment with required reviewers, see Reviewing deployments.

**Wait timer projection rules**: You can use a wait timer protection rule to delay a job for a specific amount of time after the job is initially triggered before the environment deployment is allowed to proceed. The time (in minutes) must be an integer between 1 and 43,200 (30 days).The wait time won't count towards your billable time.

**Branch and tag protection rules**: You can use deployment branch and tag protection rules to restrict which branches and tags are utilized to deploy to the environment. You have several options for deployment branch and tag protection rules for an environment.

* **No restriction** sets no restriction on which branch or tag can deploy to the environment. 
* **Protected branches only** allows only branches with branch protection rules enabled to deploy to the environment. If no branch protection rules are defined for any branch in the repository, then all branches can deploy. 
* The **Selected branches and tags** setting ensures Only branches and tags that match your specified name patterns can deploy to the environment.

If you specify releases/* as a deployment branch or tag rule, only a branch or tag whose name begins with releases/ can deploy to the environment. (Wildcard characters won't match /. To match branches or tags that begin with release/ and contain an additional single slash, use release/*/*.) If you add main as a branch rule, a branch named main can also deploy to the environment.

**Custom deployment protection rules**: You can enable your own custom protection rules to gate deployments with third-party services. For instance, you can use observability systems, change management systems, code quality systems, or other manual configurations that you use to assess readiness and provide automated approvals for deployments to GitHub.

Once custom deployment protection rules are created and installed on a repository, you can enable the custom deployment protection rule for any environment in the repository.

![](https://learn.microsoft.com/en-us/training/github/github-actions-ci/media/2b-protection-rules.png)

Settings page for configuring 'Environment1' with options for reviewers, wait timer, custom rules, and branch restrictions.

**Note**

If you are on a GitHub Free, GitHub Pro, or GitHub Team plan, the enviroment deployment projection rules are only available for public repositories; with the exception of branch & tag protection rules. For users of GitHub Pro or GitHub Team plans, branch and tag protection rules are also available for private repositories.

## Scripts in your workflow
In the preceding workflow snippet examples, the run keyword is used to print a string of text. Because the run keyword tells the job to execute a command on the runner, you use the run keyword to run actions or scripts.

**yml**

```
jobs:
  example-job:
    steps:
      - run: npm install -g bats
```

In this example, you're using npm to install the bats software testing package by using the run keyword. You can also run a script as an action. You can store the script in your repository, often done in a .github/scripts/ directory, and then supply the path and shell type using the run keyword.

**yml**

```
jobs:
  example-job:
    steps:
      - name: Run build script
        run: ./.github/scripts/build.sh
        shell: bash
```

## Cache dependencies with the cache action
When building out a workflow, you'll often find the need to reuse the same outputs or download dependencies from one run to another. Instead of downloading these dependencies over and over again, you can cache them to make your workflow run faster and more efficiently. Caching dependencies reduces the time it takes to run certain steps in a workflow, because jobs on GitHub-hosted runners start in a clean virtual environment each time.

To cache dependencies for a job, use GitHub's cache action. This action retrieves a cache identified by a unique key that you provide. When the action finds the cache, it then retrieves the cached files to the path that you configure. To use the cache action, you need to set a few specific parameters:

| Parameter | Description | Required |
|-----------|-------------|----------|
| Key | Refers to the key identifier created when saving and searching for a cache. | Yes |
| Path | Refers to the file path on the runner to cache or search. | Yes |
| Restore-keys | Consists of alternative existing keys to caches if the desired cache key isn't found. | No |

**yml**

```
steps:
  - uses: actions/checkout@v2

  - name: Cache NPM dependencies
    uses: actions/cache@v2
    with:
      path: ~/.npm
      key: ${{ runner.os }}-npm-cache-${{ hashFiles('**/package-lock.json') }}
      restore-keys: |
        ${{ runner.os }}-npm-cache-
```

In the preceding example, the path is set to ~/.npm and the key includes the runner's operating system and the SHA-256 hash of the package-lock.json file. Prefixing the key with an ID (npm-cache in this example) is useful when you're using the restore-keys fallback and have multiple caches.

## Pass artifact data between jobs
Similar to the idea of caching dependencies within your workflow, you can pass data between jobs within the same workflow. You can do this by using the upload-artifact and download-artifact actions. Jobs that are dependent on a previous job's artifacts must wait for the previous job to complete successfully before they can run. This is useful if you have a series of jobs that need to run sequentially based on artifacts uploaded from a previous job. For example, job_2 requires job_1 by using the needs: job_1 syntax.

**yml**

```
name: Share data between jobs
on: push
jobs:
  job_1:
    name: Upload File
    runs-on: ubuntu-latest
    steps:
      - run: echo "Hello World" > file.txt
      - uses: actions/upload-artifact@v2
        with:
          name: file
          path: file.txt

  job_2:
    name: Download File
    runs-on: ubuntu-latest
    needs: job_1
    steps:
      - uses: actions/download-artifact@v2
        with:
          name: file
      - run: cat file.txt
```

The preceding example has two jobs. job_1 writes some text into the file file.txt. Then it uses the actions/upload-artifact@v2 action to upload this artifact and store the data for future use within the workflow. job_2 requires job_1 to complete by using the needs: job_1 syntax. It then uses the actions/download-artifact@v2 action to download that artifact, and then print the contents of file.txt.

## Enable step debug logging in a workflow
In some cases, the default workflow logs don't provide enough detail to diagnose why a specific workflow run, job, or step fails. For these situations, you can enable additional debug logging for two options: runs and steps. Enable this diagnostic logging by setting two repository secrets that require admin access to the repository to true:

* To enable runner diagnostic logging, set the ACTIONS_RUNNER_DEBUG secret in the repository that contains the workflow to true.
* To enable step diagnostic logging, set the ACTIONS_STEP_DEBUG secret in the repository that contains the workflow to true.

## Access the workflow logs from the user interface
When you think about successful automation, you aim to spend the least amount of time looking at what's automated so you can focus your attention on what's relevant. However, sometimes things don't go as planned, and you need to review what happened. That debugging process can be frustrating. GitHub provides a clear layout structure that enables a quick way to navigate between the jobs, while keeping the context of the currently debugging step. To view the logs of a workflow run in GitHub, you can follow these steps:

1. Navigate to the Actions tab in your repository.
2. In the left sidebar, click the desired workflow.
3. From the list of workflow runs, select the desired run.
4. Under Jobs, select the desired job.
5. Read the log output.

If you have several runs within a workflow, you can also select the Status filter after choosing your workflow and set it to Failure to only display the failed runs within that workflow.

## Access the workflow logs from the REST API
In addition to viewing logs using GitHub, you can also use GitHub's REST API to view logs for workflow runs, re-run workflows, or even cancel workflow runs. To view a workflow run's log using the API, you need to send a GET request to the logs endpoint. Keep in mind that anyone with read access to the repository can use this endpoint. If the repository is private, you must use an access token with the repo scope.

For example, a GET request to view a specific workflow run log would follow this path:

**HTTP**

```
GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs
```

## Identify when to use an installation token from a GitHub App
Once your GitHub App is installed on an account, you can authenticate it as an app installation using the 'installation access token' for REST and GraphQL API requests. This allows the app to access resources owned by the installation, assuming the app was granted the necessary repository access and permissions. REST or GraphQL API requests made by an app installation are attributed to the app. In the following example, you replace INSTALLATION_ACCESS_TOKEN with the installation access token:

```
curl --request GET \
--url "https://api.github.com/meta" \
--header "Accept: application/vnd.github+json" \
--header "Authorization: Bearer INSTALLATION_ACCESS_TOKEN" \
--header "X-GitHub-Api-Version: 2022-11-28"
```

You can also use an installation access token to authenticate for HTTP-based Git access. Your app must have the 'Contents' repository permission. You can then use the installation access token as the HTTP password. You replace TOKEN in the example with the installation access token:

```
git clone https://x-access-token:TOKEN@github.com/owner/repo.git
```


# 2.4 Exercise - Create the CI workflow on GitHub

This exercise checks your knowledge about how to create, customize, and test a continuous integration workflow for a project.

## Getting started

When you select the following *Start the exercise on GitHub* button, you'll go to a public GitHub template repository. That repository prompts you to complete a series of small challenges. Before starting the exercise, complete these tasks:

* Select the *Start course* button or the *Use this template* feature within the template repository. This action will prompt you to create a new repository. We recommend creating a public repository, as private repositories will have GitHub Actions minutes billed.
* After you make your own repository from the template, wait about 20 seconds and refresh.
* Follow the instructions in the repository's README.md to understand how the exercise works, its learning objectives, and how to successfully complete the exercise.

After you've finished the exercise in GitHub, return here for:

* A quick knowledge check
* A summary of what you've learned
* A badge for completing this module

**Note**  
You do not need to modify any of the workflow files to complete this exercise. **Altering the contents in this workflow can break the exercise's ability to validate your actions, provide feedback, and grade the results.**

https://github.com/skills/test-with-actions

# 2.5 Module assessment

Choose the best response for each question.

## Check your knowledge

### 1.
**Artifacts from a GitHub Actions workflow can be saved with what action?**

- **✅ The `actions/upload-artifact` action**
- The `actions/checkout@v3` action
- The `actions/download-artifact` action

**Explanation:** The `actions/upload-artifact` action is specifically designed to save artifacts from a workflow. The `actions/checkout` action is for accessing repository code, and `actions/download-artifact` is for retrieving previously saved artifacts.

### 2.
**What is one way that GitHub Actions workflows can NOT be used?**

- To automatically run test suites on each push
- To kick off a review process
- To automate common repetitive tasks, such as welcoming new contributors to a repository.
- **✅ To upload a new secret to GitHub Secrets.**

**Explanation:** GitHub Actions workflows cannot upload secrets to GitHub Secrets for security reasons. Secrets must be manually added through the repository settings by users with appropriate permissions. All other options are valid use cases for GitHub Actions.

### 3.
**Which action would you use to access a repository's code from the virtual machine provided by GitHub Actions?**

- `actions/upload-artifact`
- **✅ `actions/checkout`**
- `npm install`
- `actions/setup-node`

**Explanation:** The `actions/checkout` action downloads the repository's source code to the GitHub Actions runner, making it available for subsequent steps. `actions/upload-artifact` saves files, `npm install` installs dependencies, and `actions/setup-node` configures Node.js environment.

### 4.
**How many builds will the following matrix produce?** `os: [ubuntu-latest, windows-latest] node-version: [14.x, 16.x, 18.x]`

- **✅ 6**
- 3
- 5

**Explanation:** A matrix creates builds for every combination of the specified values. With 2 operating systems and 3 Node.js versions, this produces 2 × 3 = 6 builds: ubuntu-latest with each Node version (3 builds) and windows-latest with each Node version (3 builds).

### 5.
**How can you pass data between jobs in a GitHub Actions workflow?**

- **✅ By using the `needs` keyword**
- By using the `outputs` keyword
- By using the `env` keyword
- By using the `secrets` keyword

**Explanation:** The `needs` keyword establishes job dependencies and allows access to outputs from previous jobs. While `outputs` are used to define what data a job produces, `needs` is the mechanism that enables one job to access another job's outputs. `env` and `secrets` are for environment variables and sensitive data, not for passing data between jobs.



# 2.6 Summary

In this module, you implemented a CI solution using GitHub Actions and workflows.

You can now:

* Build and test a Node.js project by using GitHub Actions and a templated workflow.
* Debug a failed test using the GitHub Actions log.
* Customize your workflow with GitHub Actions to:
  * Create a build artifact and save it.
  * Get access to your build artifacts.
  * Test against multiple targets.
  * Add labels to your pull requests.

## Next steps

To continue your journey with GitHub Actions, check out the next module on this learning path. You can expand on what you learned here and use GitHub Actions for continuous delivery and implementing infrastructure as code.

## Learn more

Here are some links to more information on the subjects we discussed in this module.

* GitHub Actions documentation
* GitHub Marketplace
* GitHub created actions
* actions/checkout@v3
* actions/upload-artifact
* actions/download-artifact
* pullreminders/label-when-approved-action
* Metadata syntax for GitHub Actions
* Workflow syntax for GitHub Actions
* Events that trigger workflows
* GitHub Actions usage limits
* About GitHub Actions: Job
* About CI: Job
* npm install
* npm run
* npm test
* Default environment variables
* Contexts
* Understanding GitHub Actions
* Using the cache action
* Passing data between jobs in a workflow
* Enabling debug logging
* Using workflow run logs


# 3 Build and deploy applications to Azure by using GitHub Actions

Create two deployment workflows using GitHub Actions and Microsoft Azure.


# 3.1 Introduction

Continuous Delivery (CD) is the practice of using automation to build, test, configure, and deploy from the build environment all the way to the final production environment.

Suppose that your development team is working on the company's product support website. You previously set up continuous integration (CI) by using GitHub Actions and workflows. Now you need to implement CD. Your CI workflow saves a container image. Your CD workflow must deploy this container to your staging and production environments. You talked with IT about how to create and tear down these environments as needed. You all decided to use GitHub Actions and workflows to support infrastructure as code.

In this module, you learn how to use GitHub Actions and workflows to implement a CD solution that deploys to Microsoft Azure Web Apps. The deployment uses a GitHub Action from the GitHub Marketplace. You also automate creating and tearing down the deployment environments by using a workflow.

## Learning objectives

In this module, you will:

* Discover options for triggering a CD GitHub Workflow.
* Understand steps to remove workflow artifacts.
* Identify important environment protections.
* Control workflow execution with job conditionals.
* Deploy to Microsoft Azure with a GitHub deploy action.
* Store credentials with GitHub Secrets.
* Create and destroy Azure resources with GitHub Actions and workflows.

## Prerequisites

* A GitHub account
* The ability to navigate and edit files in GitHub
  * For more information about GitHub, see Introduction to GitHub.
* Basic familiarity with GitHub Actions and workflows
  * If you aren't familiar with workflows, jobs and steps, check out the Automate development tasks by using GitHub Actions module.
* Basic familiarity with continuous integration using GitHub Actions and workflows
  * If you're unfamiliar with continuous integration using GitHub Actions and workflows, check out Build continuous integration workflows by using GitHub Actions
* An Azure subscription


# 3.2 How do I use GitHub Actions to deploy to Azure?

This unit discusses how to use GitHub actions to deploy a container-based web app to Microsoft Azure Web Apps. It covers some options for triggering a workflow. Next, you learn how to work with conditionals in the workflow. Finally, you learn about how to create and delete Azure resources by using GitHub Actions.

## Options for triggering a CD workflow
There are several options for starting a CD workflow. In the previous module on CI with GitHub Actions, you learned how to trigger a workflow from a push to the GitHub repository. However, for CD, you might want to trigger a deployment workflow on some other event.

One option is to trigger the workflow with ChatOps. ChatOps uses chat clients, chatbots, and real-time communication tools to run tasks. For example, you might leave a specific comment in a pull request that can kick off a bot. That bot might comment back with some statistics or run a workflow.

Another option, and the one we use in our example, is to use labels in your pull request. Different labels can start different workflows. For example, add a stage label to begin a deployment workflow to your staging environment, or add a spin up environment label to run the workflow that creates the Microsoft Azure resources for you to deploy to. To use labels, your workflow looks like this:

**yml**

```
on:
  pull_request:
    types: [labeled]
```

## Control execution with a job conditional
Often, you only want to run a workflow if a certain condition is true.

GitHub workflows provide the if conditional for this scenario. The conditional uses an expression that's evaluated at runtime. For example, you want to run this workflow if a stage label is added to the pull request.

**yml**

```
if: contains(github.event.pull_request.labels.*.name, 'stage')
```

## Store credentials with GitHub Secrets
You never want to expose sensitive information in the workflow file. GitHub Secrets is a secure place to store sensitive information that your workflow needs. Here's an example:

In order to deploy to an Azure resource, the GitHub Action must have permission to access the resource. You don't want to store your Azure credentials in plain sight in the workflow file. Instead, you can store your credentials in GitHub Secrets.

To store information in GitHub Secrets, create a secret on the portal.

![](https://learn.microsoft.com/en-us/training/github/github-actions-cd/media/2-secrets.png)

Screenshot of the GitHub portal interface for creating a secret.

Then, use the name of the secret you created in your workflow wherever you need that information. For example, use the Azure credential that was stored in GitHub Secrets in the creds: attribute of an Azure login action.

**yml**

```
steps:
      - name: "Login via Azure CLI"
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}
```

## Deploy to Microsoft Azure using GitHub Actions
The GitHub Marketplace has several actions that help you automate Azure-related tasks.

![](https://learn.microsoft.com/en-us/training/github/github-actions-cd/media/2-marketplace-azure.png)

Screenshot of the GitHub Marketplace showing search results for Azure.

You can also search and browse GitHub Actions directly in a repository's workflow editor. From the sidebar, you can search for a specific Action, view featured Actions, and browse featured categories.

To find an Action:

1. In your repository, browse to the workflow file that you want to edit.
2. Select the Edit icon in the upper-right corner of the file view.
3. Use the GitHub Marketplace sidebar to the right of the editor to browse Actions.

Suppose you want to deploy a container-based web app to Azure Web Apps. If you search the GitHub Marketplace, you find these actions:

* azure/webapps-deploy@v1
* azure/login@v1 that we saw previously
* azure/docker-login@v1

If you add these actions to the Deploy-to-Azure job, your workflow looks like this:

**yml**

```
  Deploy-to-Azure:
    runs-on: ubuntu-latest
    needs: Build-Docker-Image
    name: Deploy app container to Azure
    steps:
      - name: "Login via Azure CLI"
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - uses: azure/docker-login@v1
        with:
          login-server: ${{env.IMAGE_REGISTRY_URL}}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Deploy web app container
        uses: azure/webapps-deploy@v1
        with:
          app-name: ${{env.AZURE_WEBAPP_NAME}}
          images: ${{env.IMAGE_REGISTRY_URL}}/${{ github.repository }}/${{env.DOCKER_IMAGE_NAME}}:${{ github.sha }}

      - name: Azure logout
        run: |
          az logout
```

Notice that this job depends on a previous job, Build-Docker-Image. The previous job creates the artifact that gets deployed.

The azure/login@v1 action needs credentials to sign in to your Azure account so that it can access the Azure resources to which you want to deploy. Here, use the credentials that we stored in GitHub Secrets.

The same is true for the azure/docker-login@v1 action. Since you're deploying a container image, you need to sign in to your private container registry.

The azure/webapps-deploy@v1 action performs the deployment. It depends on the two preceding actions.

## Create and delete Azure resources by using GitHub Actions
Because CD is an automated process, you've already decided to use infrastructure as code to create and take down the environments you deploy to. GitHub Actions can automate these tasks on Azure, and you can include these actions in your workflow.

**Note**

Remember that it's important to tear down resources that you're no longer using as soon as possible to avoid unnecessary charges.

One option is to create a new workflow with two jobs, one that spins up resources and one that deletes them. Then, use a conditional to run only the job you want. In this example, the conditional looks for a label in the pull request and runs the set-up-azure-resources job if the label is spin up environment and the destroy-azure-resources job if the label is destroy environment.

**yml**

```
jobs:
  set-up-azure-resources:
    runs-on: ubuntu-latest

    if: contains(github.event.pull_request.labels.*.name, 'spin up environment')

    ...

  destroy-azure-resources:
    runs-on: ubuntu-latest

    if: contains(github.event.pull_request.labels.*.name, 'destroy environment')

    ...
```

The jobs use the Azure CLI to create and destroy the Azure resources. For more information about Azure CLI, see Overview of Azure CLI.

Here's an example of the steps in the set-up-azure-resources job:

**yml**

```
steps:
  - name: Checkout repository
    uses: actions/checkout@v2

  - name: Azure login
    uses: azure/login@v1
    with:
      creds: ${{ secrets.AZURE_CREDENTIALS }}

  - name: Create Azure resource group
    if: success()
    run: |
      az group create --location ${{env.AZURE_LOCATION}} --name ${{env.AZURE_RESOURCE_GROUP}} --subscription ${{secrets.AZURE_SUBSCRIPTION_ID}}
  - name: Create Azure app service plan
    if: success()
    run: |
      az appservice plan create --resource-group ${{env.AZURE_RESOURCE_GROUP}} --name ${{env.AZURE_APP_PLAN}} --is-linux --sku F1 --subscription ${{secrets.AZURE_SUBSCRIPTION_ID}}
  - name: Create webapp resource
    if: success()
    run: |
      az webapp create --resource-group ${{ env.AZURE_RESOURCE_GROUP }} --plan ${{ env.AZURE_APP_PLAN }} --name ${{ env.AZURE_WEBAPP_NAME }}  --deployment-container-image-name nginx --subscription ${{secrets.AZURE_SUBSCRIPTION_ID}}
  - name: Configure webapp to use GitHub Packages
    if: success()
    run: |
      az webapp config container set --docker-custom-image-name nginx --docker-registry-server-password ${{secrets.GITHUB_TOKEN}} --docker-registry-server-url https://docker.pkg.github.com --docker-registry-server-user ${{github.actor}} --name ${{ env.AZURE_WEBAPP_NAME }} --resource-group ${{ env.AZURE_RESOURCE_GROUP }} --subscription ${{secrets.AZURE_SUBSCRIPTION_ID}}
```

Notice that you use GitHub actions to check out the repository and to sign in to Azure. After that, you create the resources you need and deploy the container by using the Azure CLI.


# 3.3 Remove artifacts, create status badges, and configure environment protections

In this unit, you learn how to remove workflow artifacts from GitHub and change the default retention period. Next, you learn how to create a workflow status badge and add it to your README.md file. Finally, you identify some important workflow environment protections and learn how to enable them.

## Remove workflow artifacts from GitHub
By default, GitHub stores any build logs and uploaded artifacts for 90 days before it deletes them. You can customize this retention period based on the type of repository and the usage limits set for your specific GitHub product. There's a lot more information about usage limits and artifact retention in Usage limits, billing, and administration.

But suppose you're reaching your organization's storage limit for GitHub artifacts and packages. You want to remove old artifacts without increasing your usage limits and blocking your workflows. You can reclaim used GitHub Actions storage by deleting artifacts before they expire on GitHub. You can do this two ways, as described in the following sections. Both methods require write access to the repository.

**Warning**

Keep in mind that once you delete an artifact, it can't be restored.

### Manually delete artifacts from your repository
To manually delete an artifact on GitHub, navigate to the Actions tab, select the workflow from the left sidebar, and then select the run you want to see.

![](https://learn.microsoft.com/en-us/training/github/github-actions-cd/media/select-workflow-run.png)

Screenshot that shows an example workflow run on GitHub.

Under Artifacts, delete the artifact you want to remove.

![](https://learn.microsoft.com/en-us/training/github/github-actions-cd/media/delete-artifact.png)

Screenshot that shows the trash can icon to delete an artifact on GitHub.

You can also use the Artifacts REST API to delete artifacts. This API also allows you to download and retrieve information about work artifacts.

### Change the default retention period
You can change the default artifact and log retention period for your repository, organization, or enterprise account. Keep in mind that changing the retention period only applies to new artifacts and log files. It doesn't apply to existing objects. The process to configure these settings is a bit different for a repository, organization, or enterprise. Check the summary at the end of this module for more information on configuring artifacts and log retentions.

In addition to configured settings across a repository, organization, or enterprise, you can define a custom retention period for individual artifacts right within the workflow file. This practice is good for individual use cases where you want a specific artifact's retention to be different than the default or configured setting. You can do this using a retention-days value within the step with the upload-artifact action.

The following example uploads an artifact that persists for 10 days instead of the default 90 days:

**yml**

```
- name: 'Upload Artifact'
  uses: actions/upload-artifact@v2
  with:
    name: my-artifact
    path: my_file.txt
    retention-days: 10
```

## Add a workflow status badge to your repository
It's helpful to know a workflow's status without having to visit the Actions tab to see if it successfully completed. Adding workflow status badges to your repository README.md file allows you to quickly see if your workflows are passing or failing. While it's common to add a status badge to a repository README.md file, you can also add it any web page. By default, status badges display the workflow statuses on your default branch, but you can also display workflow status badges on other branches using the branch and event parameters.

Here's an example of what you need to add to a file to see a workflow status badge:

**yml**

```
![example branch parameter.](https://github.com/mona/special-octo-eureka/actions/workflows/grading.yml/badge.svg?branch=my-workflow)
```

For example, adding the branch parameter along with the desired branch name at the end of the URL shows the workflow status badge for that branch instead of the default branch. This practice makes it easy to create a table-like view within your README.md file to display workflow statuses based on branches, events, services, or environments to name a few.


![](https://learn.microsoft.com/en-us/training/github/github-actions-cd/media/my-workflow-status-badge.png)

Screenshot that shows an example workflow status badge with the my-workflow branch.

You can also create a status badge using GitHub. Navigate to the workflows section within the Actions tab and select a specific workflow. The Create status badge option allows you to generate the markdown for that workflow and set the branch and event parameters.

![](https://learn.microsoft.com/en-us/training/github/github-actions-cd/media/create-status-badge.png)

Screenshot that shows the option to create a status badge from the workflows section on GitHub.

## Add workflow environment protections
Security is a big deal, so it makes sense to configure your workflow environment with protection rules and secrets. With these elements in place, a job doesn't start or access any defined secrets in the environment until all of the environment's protection rules pass. Currently, protection rules and environment secrets only apply to public repositories.

There are two environment protection rules that you can apply to workflows within public repositories, required reviewers and wait timer.

* **Required reviewers** allow you to set a specific person or team to approve workflow jobs that reference the job's environment.
* You can use **Wait timer** to delay a job for a specific amount of time after the job has been triggered.

Suppose you need to create a workflow to a production environment that a dev team needs to approve before the deployment occurs. Use the following steps:

1. Create a production environment within the repository.
2. Configure the required reviewers environment protection to require an approval from the specific dev team.
3. Configure the specific job within the workflow to look for the production environment.

You can create and configure new repository environments from the repository's Settings tab under Environments.


# 3.4 Exercise - Create a workflow that deploys a web app to Azure

This exercise checks your knowledge on content covered in this module by using GitHub Actions and Microsoft Azure to create two deployment workflows.

## Getting started

When you select the *Start the exercise on GitHub* button, you navigate to a public GitHub template repository that prompts you to complete a series of small challenges. Before you can begin the exercise, complete the following tasks:

* Select the *Start course* button or the *Use this template* feature within the template repository. This action prompts you to create a new repository. We recommend that you create a public repository. Private repositories use Actions minutes.
* After you make your own repository from the template, wait about 20 seconds and refresh.
* Follow the instructions in the repository's README to understand how the exercise works, its learning objectives, and how to successfully complete the exercise.

When you finish the exercise in GitHub, return here for:

* A quick knowledge check
* A summary of what you've learned
* To earn a badge for completing this module

**Note**  
You do not need to modify any of the workflow files to complete this exercise.

**Altering the contents in this workflow can break the exercise's ability to validate your actions, provide feedback, or grade the results**.

https://github.com/skills/deploy-to-azure

# 3.5 Module assessment

Choose the best response for each question.

## Check your knowledge

### 1.
**How do you grant your GitHub repository access to Azure?**

- It happens automatically.
- Authenticate to Azure with GitHub.
- **✅ Manage credentials using GitHub Secrets and use that secret name in the workflow.**
- Manage credentials by generating tokens locally

**Explanation:** To grant GitHub repository access to Azure, you need to store Azure credentials (such as service principal credentials) in GitHub Secrets and then reference those secrets in your workflow using `${{ secrets.AZURE_CREDENTIALS }}`. This is the secure and recommended way to authenticate with Azure from GitHub Actions.

### 2.
**What can trigger a workflow for deploying to Microsoft Azure?**

- Only commit events
- Any events that affect the repository's default branch
- **✅ Any event, just like any other Action**

**Explanation:** GitHub Actions workflows for Azure deployment can be triggered by any GitHub event, just like any other workflow. This includes push events, pull requests, labels, schedules, manual triggers (`workflow_dispatch`), and many others. Azure deployment workflows are not limited to specific types of events.

### 3.
**How do you make sure that your Azure credentials are not stored in plain text in your repository?**

- **✅ Use GitHub Secrets to securely store your Azure credentials.**
- Use your GitHub token to authenticate into Azure.
- Put your credentials directly in your workflow file.

**Explanation:** GitHub Secrets provide a secure way to store sensitive information like Azure credentials. These secrets are encrypted and only accessible to authorized workflows. Putting credentials directly in workflow files would expose them in plain text, and GitHub tokens cannot be used to authenticate with Azure services.


# 3.6 Summary

In this module, you learned how to use GitHub Actions and workflows to implement a CD solution that deploys a container-based web app to Microsoft Azure Web Apps. You also automated the creation and teardown of the deployment environments by using a workflow.

You learned about:

* Options for triggering a CD workflow.
* Controlling workflow execution with job conditionals.
* Deploying to Microsoft Azure with a GitHub `deploy` action.
* Storing credentials with GitHub Secrets.
* Using GitHub actions to create and delete Azure resources.

## Learn more

Here are some links to more information on the topics discussed in this module.

* GitHub Actions documentation
* GitHub Marketplace
* GitHub created actions
* Metadata syntax for GitHub Actions
* Workflow syntax for GitHub Actions
* GitHub Actions usage limits
* Introduction to Docker Containers
* actions/checkout@v1
* actions/upload-artifact
* actions/download-artifact
* azure/webapps-deploy@v1
* azure/login@v1
* azure/docker-login@v1
* Artifact and log retention policy
* Artifacts REST API
* Adding a workflow status badge
* Environments



# 4 Automate GitHub by using GitHub Script

Learn to interact with the GitHub API from GitHub Actions by using GitHub Script.

# 4.1 Introduction

GitHub Script is a workflow action that provides you with access to the GitHub API from within GitHub Actions. It offers convenient support for any API usage that's available in octokit/rest.js.

Suppose you maintain a vibrant GitHub repository. Your project has a substantial number of consumers and contributors, and you want to make sure they have a welcoming experience. You also find that the responsibilities of managing the team's planning and workload can really add up. You need a solution that enables you to hand off some of the mundane tasks to automation so that you can focus on areas where you really add value. You know that GitHub provides an API that lets you automatically reply to new issues and begin the triage workflow for new bug reports. You just haven't invested the time in figuring it all out, until now.

In this module, you'll learn how to interact with the GitHub API from a GitHub Actions workflow by using GitHub Script.

## Learning objectives

In this module, you'll:

* Use GitHub Script in your workflow.
* Comment on issues by using Octokit.
* Add issues to a project board by using Octokit.
* Use the workflow expression syntax to filter when jobs run in a workflow.

## Prerequisites

* A GitHub account
* The ability to navigate and edit files in GitHub
* Familiarity with GitHub Actions
* Familiarity with CI/CD

We recommend that you complete Automate development tasks by using GitHub Actions before beginning this module.

# 4.2 What is GitHub Script?

In this unit, you'll learn how GitHub Script enables you to automate common GitHub processes by using GitHub Actions workflows.

## What is GitHub Script?
GitHub Script is an action that provides an authenticated Octokit client and enables JavaScript to be written directly in a workflow file. It runs in Node.js, so you have the power of that platform available when you write scripts.

## What is Octokit?
Octokit is the official collection of clients for the GitHub API. One of these clients, rest.js, provides JavaScript access to the GitHub REST interface.

You have always been able to automate the GitHub API via octokit/rest.js, although it could be a chore to properly set up and maintain. One of the great advantages to using GitHub Script is that it handles all of this overhead so you can immediately start using the API. You don't need to worry about dependencies, configuration, or even authentication.

## What can octokit/rest.js do?
The short answer is that it can do virtually anything with respect to automating GitHub. In addition to having access to commits, pull requests, and issues, you also have access to users, projects, and organizations. You can retrieve lists of commonly used files, like popular licenses or .gitignore files. You can even render Markdown.

If you're creating something that integrates GitHub, the odds are good that you'll find what you're looking for in the full octokit/rest.js documentation.

## How is using GitHub Script different from octokit/rest.js?
The main difference in usage is that GitHub Script provides a preauthenticated octokit/rest.js client named github.

So instead of

```
octokit.issues.createComment({
```

you use

```
github.issues.createComment({
```

In addition to the github variable, the following variables are also provided:

* **context** is an object that contains the context of the workflow run.
* **core** is a reference to the @actions/core package.
* **io** is a reference to the @actions/io package.

## Creating a workflow that uses GitHub Script
GitHub Script actions fit into a workflow like any other action. As a result, you can even mix them in with existing workflows, like those you might have already set up for CI/CD. To illustrate the convenience of GitHub Script, you'll now construct a complete workflow that uses it to automatically post a comment to all newly created issues.

You'll start off with a name and an on clause that specifies that the workflow runs when issues are opened:

**YAML**

```
name: Learning GitHub Script

on:
  issues:
    types: [opened]
```

Next, you'll define a job named comment that runs on Linux with a series of steps:

**YAML**

```
jobs:
  comment:
    runs-on: ubuntu-latest
    steps:
```

In this case, there's only one step: the GitHub Script action.

**YAML**

```
      - uses: actions/github-script@0.8.0
        with:
          github-token: ${{secrets.GITHUB_TOKEN}}
          script: |
            github.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: "🎉 You've created this issue comment using GitHub Script!!!"
            })
```

Using GitHub Actions can really help automate the events that take place in your repositories. Imagine that a repository visitor opened a new issue containing information about a critical bug. You might want to thank them for bringing the bug to your attention, but this simple task can become overwhelming as your repository attracts more visitors. By automating an issue comment, you can automate the process of thanking visitors every time.

## Using actions/github-script@0.8.0
The actions/github-script@0.8.0 action, also known as GitHub Script, does all the difficult work for your integration with the GitHub API.

This action requires a github-token that's provided at runtime so that requests are authenticated. This is automatically done for you, so you can use that code as-is.

The script parameter can be virtually any JavaScript that uses the octokit/rest/js client stored in github. In this case, it's just one line (split across multiple lines for readability) that creates a hardcoded comment.

After the workflow runs, GitHub Script logs the code it ran for review on the Actions tab:

Screenshot of a completed GitHub Script workflow.

## Running from a separate file
You might sometimes need to use a significant amount of code to meet your GitHub Script scenario. When that happens, you can keep the script in a separate file and reference it from the workflow instead of putting all the script inline.

Here's an example of a simple workflow that uses that technique:

**YAML**

```
on: push

jobs:
  echo-input:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/github-script@v2
        with:
          script: |
            const path = require('path')
            const scriptPath = path.resolve('./path/to/script.js')
            console.log(require(scriptPath)({context}))
```

Check out more GitHub Script examples.




# 4.3 Exercise - Using GitHub Script in GitHub Actions

In this unit, you'll learn more about how you can use GitHub Script to improve your workflow.

## Add issues to a project board
In addition to using octokit/rest.js to create comments and open pull requests, you can also use octokit/rest.js to manage GitHub Projects. In the following code sample, you create a workflow that runs whenever anyone adds a new issue to the repository. This adds the issue to a project board, which makes it easier for you to triage your work.

```
name: Learning GitHub Script
on:
  issues:
    types: [opened]
jobs:
  comment:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/github-script@0.8.0
      with:
        github-token: ${{secrets.GITHUB_TOKEN}}
        script: |
            github.issues.createComment({
            issue_number: context.issue.number,
            owner: context.repo.owner,
            repo: context.repo.repo,
            body: "🎉 You've created this issue comment using GitHub Script!!!"
            })
            github.projects.createCard({
            column_id: {{columnID}},
            content_id: context.payload.issue.id,
            content_type: "Issue"
            });
```

The first section of this workflow creates a comment whenever a new issue is created, which is covered in the previous unit. The next section creates a card based on this issue and adds it to the project board.

## Separate workflow into steps
One benefit of using actions is that you can separate jobs into smaller units of work called steps. In the preceding example workflow, you can separate the workflow into two steps.

One advantage of breaking the current workflow into multiple steps is that it enables you to use expressions to apply logic. Using steps allows you to create rules around when steps are allowed to run and can help optimize your workflow run.

To separate the example workflow into steps:

* Name each step so that you can track it from the Actions tab.
* Use expressions to determine whether a step should run (optional).

In this example, the two tasks in the original workflow file are separated into individual steps:

```
name: Learning GitHub Script
on:
  issues:
    types: [opened]
jobs:
  comment:
    runs-on: ubuntu-latest
    steps:
    - name: Comment on new issue
      uses: actions/github-script@0.8.0
      with:
        github-token: ${{secrets.GITHUB_TOKEN}}
        script: |
            github.issues.createComment({
            issue_number: context.issue.number,
            owner: context.repo.owner,
            repo: context.repo.repo,
            body: "🎉 You've created this issue comment using GitHub Script!!!"
            })
    - name: Add issue to project board
      if: contains(github.event.issue.labels.*.name, 'bug')
      uses: actions/github-script@0.8.0
      with:
        github-token: ${{secrets.GITHUB_TOKEN}}
        script: |
            github.projects.createCard({
            column_id: {{columnID}},
            content_id: context.payload.issue.id,
            content_type: "Issue"
            });
```

Each step includes a descriptive name element that also helps you track it from the Actions tab.

The Add issue to project board step also includes an if statement that specifies that the issue should be added to the project board only if it's labeled bug.

## Use the Node.js environment
GitHub Script also grants you access to a full Node.js environment. Although we don't recommend using GitHub Script to write the logic for complex actions, you can use it to add more functionality to the octo/rest.js API.

For example, you could use Node.js to display a contribution guide whenever an issue is opened. You can use the Node.js file system to read a file and use it as the body of the issue comment. To access files within the repository, include the actions/checkout action as the first step in the workflow.

The following example makes the following changes to the workflow file:

* Adds the action/checkout action to read the templated response file that's located at .github/ISSUE_RESPONSES/comment.md
* Adds JavaScript to use the Node.js File System module to place the contents of our templated response as the body of the issue comment

```
name: Learning GitHub Script
on:
  issues:
    types: [opened]
jobs:
  comment:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v2
      - name: Comment on new issue
        uses: actions/github-script@0.8.0
        with:
          github-token: ${{secrets.GITHUB_TOKEN}}
          script: |
             const fs = require('fs')
             const issueBody = fs.readFileSync(".github/ISSUE_RESPONSES/comment.md", "utf8")
             github.issues.createComment({
             issue_number: context.issue.number,
             owner: context.repo.owner,
             repo: context.repo.repo,
             body: issueBody
             })
      - name: Add issue to project board
        if: contains(github.event.issue.labels.*.name, 'bug')
        uses: actions/github-script@0.8.0
        with:
          github-token: ${{secrets.GITHUB_TOKEN}}
          script: |
            github.projects.createCard({
            column_id: {{columnID}},
            content_id: context.payload.issue.id,
            content_type: "Issue"
            });
```

GitHub Script helped you create a comprehensive response to a new issue. This response is also based on a template in the repository, so it's easy to change. Finally, you also included a trigger to add the issue to the project board so you can easily triage it for future work.


# 4.4 Module assessment

Choose the best response for each question.

## Check your knowledge

### 1.
**What is GitHub Script?**

- A programming language that compiles to JavaScript.
- An automation syntax for GitHub shell.
- **✅ A workflow action that enables GitHub API access from GitHub Actions.**

**Explanation:** GitHub Script is a workflow action that provides an authenticated Octokit client and enables JavaScript to be written directly in a workflow file. It gives you access to the GitHub API from within GitHub Actions workflows without needing to handle authentication or dependencies yourself.

### 2.
**What is the difference between GitHub Script and GitHub Actions?**

- GitHub Actions is for automating build and release pipelines. It was written in the GitHub Script programming language.
- **✅ GitHub Actions is a workflow engine that automates the execution of actions. GitHub Script is one of the actions available for use in a workflow.**
- GitHub Actions automates workflows that run inside GitHub. GitHub Script automates workflows that run outside of GitHub.

**Explanation:** GitHub Actions is the broader platform/workflow engine that automates various tasks, while GitHub Script is a specific action that you can use within GitHub Actions workflows. GitHub Script provides convenient access to the GitHub API using JavaScript within those workflows.

### 3.
**Why would someone use the following YAML in a GitHub Script action:** `if: contains(github.event.issue.labels.*.name, 'bug')`?

- **✅ To ensure that the script runs only when the target issue is labeled as a bug.**
- To make sure that new issue names don't violate the bug reporting policy when issues are created.
- To automatically flag any commits containing code matching the `github.event.issue.labels.*.name` namespace pattern as a bug.

**Explanation:** This is a conditional statement that checks if the issue has a label named 'bug'. The script will only execute when this condition is true, making it useful for running specific automation only on issues that are labeled as bugs. This helps control when certain actions should take place based on the issue's labels.


# 4.5 Summary

In this module, you learned how to interact with the GitHub API from GitHub Actions by using GitHub Script.

You learned about:

* Using GitHub Script in your workflow.
* Commenting on issues by using Octokit.
* Adding issues to a project board by using Octokit.
* Using the workflow expression syntax to filter when jobs run in a workflow.

GitHub Script is great for interacting with GitHub from GitHub Actions. But what if you want to interact with the API from somewhere else? In that case, you can learn to Automate DevOps processes by using GitHub Apps.

## Learn more

Here are some links to more information on the topics discussed in this module:

* GitHub Script
* Octokit
