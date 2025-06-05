

# GitHub Foundations Part 2 of 2

https://learn.microsoft.com/en-us/training/paths/github-foundations-2/

The GitHub Foundations Learning Path Part 2 of 2 is a concise and beginner-friendly journey designed to introduce you to the fundamental concepts and products of GitHub. You'll discover the benefits of using GitHub as a collaborative platform and explore its core features, such as repository management, commits, branches, and merging.

## In this learning path, you'll:

- Gain an understanding of GitHub's essential tools
- Become familiar with Git
- Learn about GitHub Copilot

## Prerequisites

- A GitHub Account

# 9 Introduction

**Completed** • **100 XP** • **1 minute**

Open-source software relies heavily on the community for its long-term sustainability. One way to contribute to open-source projects is by making contributions to the project's repository and conducting code reviews.

Suppose you've been using open-source libraries for your projects and at work for quite some time. In the spirit of open source, you've decided to contribute back to some of these libraries and frameworks.

However, you've never contributed before, and you're not sure how to get started.

In this module, you'll learn how to make meaningful contributions to open-source projects. You'll learn about the kinds of projects and activities that will make an impact and how to familiarize yourself with the project and its community standards. You'll learn how to effectively use git and GitHub to make your improvement to code or documentation. You'll also learn the dos and don'ts of communicating with the project's maintainers, how to ask for help, how to ask for a review, and how to review others' work in GitHub.

By the end of this module, you'll learn how to submit a successful contribution to an open-source project on GitHub by adopting best practices.

## Learning objectives

By the end of this module, you'll be able to:

- Find open-source projects and tasks to contribute to in GitHub
- Create pull requests to open-source projects
- Implement best practices to communicate with open-source maintainers and perform code reviews
- Find and engage with open-source communities

## Prerequisites

- A GitHub account
- The ability to navigate and edit files in GitHub

> **📝 Note**
> 
> This module covers how to make contributions to open-source projects on GitHub. To familiarize yourself with GitHub, complete the following module first:
> 
> - **Introduction to GitHub**


# 9.2 Identify where you can help


In this unit, we'll discuss how you can get started with open-source contributions. We'll also use issues and tags to find tasks to contribute to.

Open-source software can be freely used, modified, and shared by anyone. Using open-source software, anyone can view, modify, and distribute a project for any purpose. The idea behind open-source software is that sharing code leads to better, more reliable software.

There are many ways to contribute to open-source projects. Making your first contribution can often be a scary experience, but it shouldn't be. Open source is a place for everyone, and contributions happen at all levels.

## Find an open-source project that needs contributions

You can get started by thinking about the projects you already use, or want to use. Contributing is easier when you're familiar with the project and its community.

Perhaps while reading a project's README file, you find a broken link or some typos. Maybe you noticed something isn't working as expected, or the documentation is out of date. These are all great opportunities to help and contribute to the project.

> **💡 Tip**
> 
> One important tip: All kinds of contributions are valuable. Your level of experience or knowledge of the project doesn't matter here. We all have something we can contribute. Be confident in yourself. The most important thing here is the will to help.

## Use GitHub search

You can also use GitHub search to explore topics and related projects. Head to GitHub search, and enter your topic word.

Let's say you're interested in machine learning.

*Screenshot showing GitHub search topics.*

You can then narrow your search by selecting **Topics** in the left sidebar.

*Screenshot showing the results of a GitHub narrow search.*

From there, you can find repositories relevant to your search keyword and repositories curated by community members.

## Familiarize yourself with an open-source project

Something worth mentioning here is that every open-source community is different. After you've found a project, you'll need to familiarize yourself with the project and its participation guidelines.

Most projects will have these documents at the top level of the repository:

### Key Project Documents

- **LICENSE**: The project must contain an open-source license. If the project doesn't have a license, it's not open source.
- **README**: The README file usually serves as the welcome page for the project. It generally provides information on how to get started using the project. It's also common for it to add information on how to engage with the community.
- **CONTRIBUTING**: As its name suggests, this document provides guidance on how to contribute to the project. It usually describes how the contribution process works, and includes details on how to set up your development environment.
- **CODE_OF_CONDUCT**: The code of conduct sets ground rules for community members. By doing so, it helps make the community a safe and welcoming environment for all.

Although not all projects have CONTRIBUTING or CODE_OF_CONDUCT documents, having these documents is a good indication of how friendly and welcoming a project is.

### Community Communication Channels

Open-source contributors and maintainers come from all over the world. Projects usually have multiple communication channels to organize discussions and ask for help. A good way to familiarize yourself with the community is by reading through some of these communication channels:

- **Issue tracker**: Where folks discuss issues and tasks related to the project. To find the issues in GitHub, you can go to the main page of the repository on GitHub and add `/issues` to the end of the URL, for example: `https://github.com/jupyter/notebook/issues`.
- **Pull request**: Where folks discuss and review changes to the project. You can find it in GitHub by adding `pulls` to the project's URL, for example, `https://github.com/jupyter/notebook/pulls`.
- **Chat channels and forums**: Some projects use chat channels, such as Slack, Gitter, and IRC, or forums like Discourse for conversations and discussions.

## Identify tasks to work on

You've found a project, you've read the contribution guidelines, and now you're ready to contribute.

Perhaps you've already identified something to work on, such as fixing broken links or updating the docs. A good way to find beginner-friendly issues to help with is by visiting the project's `/contribute` URL, for example: `https://github.com/jupyter/notebook/contribute`.

*Screenshot showing the Contribute to a project section on GitHub.*

You'll notice that most of the issues displayed in the contribute URL will have labels such as **good-first-issue**, **help wanted**, **beginner-friendly**, and so on. Labels are often used to provide top-level information of the issue and the type of help needed.

You can head to the labels page, for example: `https://github.com/jupyter/notebook/labels`. Then, select issues that have labels like **help wanted**, **discussion**, or other labels relevant to the type of contribution in which you're interested.

As you explore issues, you might also notice that some have other issues or pull requests linked.

*Screenshot showing a pull request linked to an issue.*

## Sponsor a project

There are many ways to contribute to open source. You can financially support the folks who build and maintain the open-source ecosystem through code, leadership, mentorship, design, and beyond.

Open source heavily relies on volunteer work. GitHub Sponsors allow you to fund projects and individuals to help them keep doing their open-source work, while giving them the recognition they deserve.

If a project is eligible for sponsorship through GitHub Sponsors, you'll find a **Sponsor** button on the project's main page.

*Screenshot showing the sponsoring box on a GitHub project page.*

You can select the sponsorship tier and if you want your contribution to be public.

*Screenshot showing sponsorship tiers.*

## Unit recap

In this unit, you learned how to get started with open-source contributions. You now know how to choose a project to work on and use GitHub issues and labels to identify tasks to work on.

Here's a handy checklist to use when you interact with a project for the first time:

- [ ] Does it have a license?
- [ ] Are issues and pull request discussions used actively by maintainers and contributors?
- [ ] Does the project use labels like **help wanted** or **good first issue** for newcomers?
- [ ] Does the project have a code of conduct?
- [ ] Does the project have clear Contributing Guidelines?

Finally, remember that all contributions are welcome, and the open-source ecosystem greatly benefits from your ideas and participation. There are many ways to contribute to open source, from submitting code or engaging in project discussions to sponsoring projects through GitHub Sponsors.


# 9.3 Contribute to an open-source repository

After you identify an area where you can contribute, the next step is to prepare your contribution. We'll review here how you can communicate your intent to participate in a project, forge a pull request, and improve your chances of getting it accepted.

When it comes to contributing work to an open-source project, communication is a key success factor. You might find it uncomfortable to communicate with others on your proposed changes or improvements. Often, this dialogue will lead to discussions and compromises on your original vision.

Avoiding active communication with others who are involved in an open-source project means risking your time working on tasks that someone else is already working on. Or, you might work on features or improvements that don't align with the project's values or best practices. In either case, everyone's time is wasted. Conversely, committing to active communication ensures that your work will be well received and impactful.

How can you ensure success when you communicate with other project members about new features and changes? First, try to keep an open mind. Be open to feedback and practice patience. Open-source project maintainers most likely have a day job and a private life to tend to. If you don't get an answer immediately, wait a little longer before you ping the maintainers.

## Communicate your intent to maintainers

You should always start by communicating your intent to contribute before you do any actual work. Unless indicated otherwise in the README file, the issue tracker is usually the best place for doing that.

If you want to work on an existing issue, check that nobody is assigned to it by looking at the **Assignees** section. Also check the **Linked pull requests** section. A linked pull request means somebody is already working on it. Look through the comments to see if someone stated their interest to work on the issue. If everything's clear, post a comment on the issue to indicate your interest to work on it. That way, you're telling people who might come later that someone's working on the issue. Also, if needed, maintainers can reply to you with guidance and advice.

*Screenshot showing the Assignees and Linked pull requests sections.*

If you want to work on a new feature or a bug that's not already present in the issue tracker, create a new issue. Make sure to follow the issue template if one is proposed, and clearly express your intent to work on the issue. If it's a new feature proposition or if the issue requires many changes, make sure to get the maintainers' approval before you move on to the next step.

## Create a pull request on a GitHub repository

After you've communicated your intent to help the project, you're now ready to start working on your actual contribution.

Your contribution will take the form of a **pull request** or **PR**. A pull request is a special place on GitHub that contains a few things:

- A title and description for your changes
- One or more commits that constitute the changes you're proposing
- Comments, where everyone can participate in a discussion about the changes
- Code reviews, where you can find detailed feedback on your changes and eventually commit suggestions
- Status checks that come, for example, from automated tests that the maintainers might have put in place. Status checks can serve different purposes. For example, they can ensure that your changes follow the project's rules, or that your changes don't break the code

After a pull request is created, it can be updated with new commits, comments, or code reviews. This process continues until the project maintainers approve and merge the pull request or reject the changes and close the pull request. When your pull request is merged, it means that your changes have been integrated into the project's codebase.

## Create a pull request step by step

### 1. Fork the repository
Open the GitHub page of the project to which you want to contribute.

Select the **Fork** button to create a copy of the repository on your GitHub account. This step is necessary because, by default, you don't have the permissions to make any changes on a public repository unless it's your own copy. By forking the project, you're creating a copy where you can make changes.

*Screenshot showing the Fork button of a GitHub project.*

### 2. Access your fork
Select **Your repositories** from your account profile menu.

*Screenshot showing the profile drop-down menu and the entry called Your repositories.*

Select the repository fork.

### 3. Clone the repository
Select the **Code** button to get information on how to "clone" the Git repository to your local machine.

*Screenshot showing the options for cloning a GitHub project.*

Select the clipboard icon to copy the repository URL, then enter in a terminal:

```sh
git clone <REPOSITORY_URL>
```

This command will create a copy of the repository on your local machine.

Alternatively, you can use **GitHub Desktop** if you prefer to use an application. Or, you can use **GitHub Codespaces** if the option is proposed to you. If you're a Visual Studio Code user, GitHub Codespaces will feel familiar to you.

### 4. Navigate to the project folder
After the project has finished cloning, enter the project folder:

```sh
cd <PROJECT_FOLDER>
```

### 5. Create a new branch (Optional but recommended)
Create a new branch by using the following command:

```sh
git checkout -b <BRANCH_NAME>
```

This step isn't mandatory, but is highly recommended. With a new branch, you can work on multiple contributions separately, each one using a different branch.

### 6. Make and commit changes
Make the desired changes to the project and commit them:

```sh
git add .
git commit -m "<COMMIT_MESSAGE>"
```

These commands will stage your changes for commit, then create a commit with the specified message. Be sure to describe your changes accurately in the commit message. It's also a good idea to check if there are mentions in the CONTRIBUTING file for commit-message conventions you need to follow.

### 7. Push changes to remote
Push your changes to the remote by using the command:

```sh
git push --set-upstream origin <BRANCH_NAME>
```

This command creates a new branch on the upstream repository on GitHub (your fork), and pushes all your commits to it.

> **📝 Note**
> 
> When we talk about an upstream repository, we refer to the remote repository linked to your local repository. The origin is the default alias for the repository URL, which was created by Git in step 4.

If you didn't create a branch previously, enter only `git push`.

### 8. Create the pull request
Open your project fork on GitHub, and select the **Compare & pull request** button in the suggestion box that appears.

*Screenshot showing the pull request suggestion box on GitHub.*

Fill in the title and description and select **Create pull request**.

*Screenshot showing the pull request creation interface.*

If there's a template for the pull request description, take the time to fill in all the required information. If there isn't one now, make sure to provide enough context for maintainers to understand what changes you're proposing and why. You should also link back to the related issue by mentioning its number by using `#<ISSUE_NUMBER>`. You can find the issue number next to its title.

*Screenshot showing issue number.*

## Pass the status checks

After you've created the pull request, you might see a section with status checks at the bottom, like this:

*Screenshot showing status checks results on a pull request.*

These status checks are automated checks that the maintainers have put in place to ensure a consistent quality of the project.

To get your pull request accepted, it needs to pass all automated checks. If one is failing like in the preceding screenshot, select the **Details** button to learn more about the failure and to find out what you need to do to fix it.

If you're unsure about what to do with a failing check, you can always use the comments to ask for the maintainers' guidance or help to fix it.

## Ask for guidance or reviews on pull requests

You might be unsure about some changes you made and want to get the maintainers' opinions. The best way to do that is to comment directly on the pull requests. If you consider your changes a work-in-progress, you also have the option to create a **draft pull request** instead to ask for guidance or help from other contributors.

*Screenshot showing the draft pull request option.*

After the project maintainers come by your pull request, they can reply to the conversation or directly review your changes. There are multiple possible outcomes following a pull request review:

### Possible Review Outcomes

- **Your changes are approved**: Congratulations!
- **Your pull request requires some changes**: Don't get discouraged! Look closely at the feedback provided. If you make the requested changes, there's a good chance that your pull request will be accepted. If you push new commits to your branch, the pull request will automatically update with the new changes.
- **The reviewer made some comments**: It usually means that more details are needed about your changes or the motivation behind it.

## Respond to comments on your pull request

Remember to always be respectful in all your exchanges and to follow the code of conduct. It's likely that before your changes can be accepted, there will be an ongoing discussion with the maintainers or other contributors.

Contributing to open source requires patience. Sometimes you don't get immediate feedback. Don't reach out to the maintainers privately via email, X, or any other means hoping to get a faster answer. This behavior is considered harmful. Discussing things publicly also gives other contributors or passersby the opportunity to learn about the process behind the changes and the best practices to follow.


# 9.4 Exercise - Create your first pull request

You've learned how to create a pull request (PR) when there's guidance either in a pull request template or in a CONTRIBUTING file. But what if a project doesn't offer that guidance and documentation on conventions?

## Describe your changes

To write a good commit message, and subsequently your pull request, follow these practices:

### Git Commit Message Guidelines

- **Your Git commit message subject line should complete the following sentence:**
  - If applied, this commit will `<your subject line here>`.

- **Include a succinct description of the change** by using the imperative, present tense. For example, use *add* not *added* or *adds*.

- **Limit your subject line to 50 characters.**

- **Start with a capital letter, and don't end with a period (.).**

- **You can use emojis** in your subject line and `@mention` other GitHub users, but not everyone is a fan of such frivolity.

### Pull Request Body Guidelines

For the body of your message and pull request, continue to use present tense. Make sure to include the motivation for the change. Contrast your change with the previous behavior. Use the space at your disposal to explain the *what* and *why* versus the *how*.

Your commit message is only as much to the point as the content that you're about to submit. Commit or submit for review small, isolated sets of changes. This practice increases the likelihood of your changes getting merged into the project.

## Add granularity

Before you submit your pull request, check the sidebar for ways to complete your PR. Select **Reviewers** or **Assignees** if you're familiar with the project's team structure. Add *labels* when there's guidance on using labels in, for instance, the CONTRIBUTING.md file. You can use labels as a visual clue for what you're trying to accomplish. A maintainer might also add a label or multiple labels.

### Common Label Examples

Some of the labels we use in the repository for this Learn module are:

- **Bug** (red): Something isn't working
- **Documentation** (blue): Improvements or additions to documentation
- **Duplicate** (gray): This issue or pull request already exists
- **Enhancement** (teal): New feature or request

### Additional Options

Optionally, you can *link issues* in the sidebar, where successfully merging a pull request might close the corresponding issue. You can also customize your subscription to *notifications* on the thread. Some PRs receive many comments, reviews, and CI/CD-related notifications. You can choose from:

- **Not subscribed:** Only receive notifications when you participated or were @mentioned
- **Subscribed:** Receive all notifications for this pull request
- **Custom:** Only be notified for the events you select

## Exercise

Using the **First Contributions** project, practice forking, cloning, and submitting a pull request. The First Contributions project aims to "guide the way beginners make their first contribution." It has guides for both using the command line and several graphical user interfaces (GUIs). The project also has support for several languages. Make sure to check the `Translations` folder.

### Practice Steps

1. **Fork** the First Contributions repository
2. **Clone** your fork to your local machine
3. **Create** a new branch for your changes
4. **Make** your contribution following the project guidelines
5. **Commit** your changes with a well-written commit message
6. **Push** your changes to your fork
7. **Create** a pull request with a clear title and description

### Reflection Exercise

With the lessons from the previous unit and this one in mind, go back to a pull request you opened recently. Or, you can go to the pull requests tab of a project you're watching. Notice how a good subject line can make all the difference. Consider updating a pull request accordingly. Put roughly as much time into writing your PR as you did in making the change to the project. Your efforts will help the maintainers categorize and prioritize (triage) community contributions.

## Bonus: Accessibility Guidelines

**Check Microsoft's Accessibility Guidelines and Requirements.** In particular, see the information about describing interactions with UI to avoid ableist language in your contributions. Customers interact with products by using different input methods. For example, they can use the keyboard, a mouse, touch, voice, and more. You'll want to use generic verbs that work with any input method. For instance, use *select* instead of the input-specific *click* or *swipe*.

### Inclusive Language Examples

| Instead of | Use |
|------------|-----|
| Click | Select |
| Swipe | Navigate |
| Tap | Choose |
| Hit | Press |
| Double-click | Open |

This practice ensures your contributions are accessible to users with different abilities and interaction preferences.



# 9.5 Next steps

You've added context to an issue, contributed a code review, and maybe even submitted a pull request of your own. Now, you want to immerse yourself further in the community around the project.

## Get involved in the community

You'll find frequent contributors to the project in the comment section for issues and pull requests. Or, you can select **Insights** in the repository's navigation, and then select **Contributors** to find other active community members. Visit their GitHub profiles. Sometimes they'll suggest ways to get in touch with them.

### Ways to Connect

- **Follow organizations and enterprises** on GitHub to stay in touch. Your personal dashboard shows public activity for every enterprise, user, or organization you follow.

- **Attend meetups or conferences** on open-source topics. Or, you can meet people if the project or ecosystem is large enough around the project you're interested in. Find archives with talk recordings for past events, podcasts, newsletters, and mailing lists.

- **Join centralized communication channels**, which are often referenced on the project's website or in the README file. There might be:
  - Discord server
  - Slack community
  - Gitter
  - IRC
  - Regular "office hours"

## Code reusability

Code, and solutions, can sometimes be reused across projects. Have you solved a very scoped issue for one project? Chances are other projects can benefit from it as well. You can:

### Option 1: Publish as a stand-alone library (dependency)
**Best for:** Plug-in style code that could be used across web-development projects.

### Option 2: Mirror the project with your added functionality
**Best for:** Solving a narrow use case for a small subset of customers, or even a single customer.

> **⚠️ Consider:** You'll need to keep your fork up to date with the upstream repository if you want to benefit from (for instance) security patches.

### Option 3: Create a GitHub Action
GitHub Actions are packaged scripts that automate tasks in a software-development workflow in GitHub. The two different types of actions are:
- **Container actions**
- **JavaScript actions**

You can submit your action to the **GitHub Marketplace** for discoverability. GitHub Marketplace connects you to developers who want to extend and improve their GitHub workflows. Use this platform to publish actions and share apps with other users for free.

## Consider your commitment as a maintainer

For all three of the suggested paths, consider that **you're now a maintainer of a project**. People will come to you with praise, questions, and complaints. Are you ready for such a commitment?

### Questions to ask yourself:

- **If your project takes off**, people's apps might depend on your bit of code. Can you involve more people to take some of the potential load off?

- **Do you have time** to add documentation, triage issues, and review suggestions from people you've likely never met before?

- **Consider your "bandwidth"** and instead set expectations in your project's README file.

### Alternative approaches:

- **Release your code in a public gist** or a blog post
- **Set clear expectations** in your README about maintenance commitments
- **Consider co-maintainers** from the beginning

> **💡 Remember:** Code doesn't need to be on GitHub to be open source, after all.

## Summary of paths forward

| Path | Best for | Considerations |
|------|----------|----------------|
| **Stand-alone library** | Reusable plug-in functionality | Full maintenance responsibility |
| **Project fork/mirror** | Specific use case solutions | Keep up with upstream changes |
| **GitHub Action** | Workflow automation | Marketplace visibility opportunity |
| **Gist/Blog post** | Simple sharing | No formal maintenance commitment |

Choose the path that aligns with your available time, expertise, and long-term commitment to the open-source community.


# 9.6 Module assessment

**Contribute to an open-source project using GitHub**

## Check your knowledge

### 1. What is the best place on a GitHub repository to find where you can help a project?

- [ ] The README file
- [x] **The issues list** ✅
- [ ] The search bar
- [ ] The LICENSE file

**Explanation:** The issues list is the best place to find where you can help a project. Issues contain specific tasks, bugs, feature requests, and other work that needs to be done. You can filter issues by labels like "good first issue," "help wanted," or "beginner-friendly" to find tasks suitable for your skill level. You can also visit the `/contribute` URL of a repository to see curated beginner-friendly issues.

### 2. What is the preferred way to ask for help or reviews on a pull request?

- [ ] Send a negative or disrespectful comment to the project's maintainers via social media.
- [ ] Create an issue
- [x] **Add comment in the pull request** ✅
- [ ] Send an email to a random committer on the project

**Explanation:** The preferred way to ask for help or reviews on a pull request is to add a comment directly in the pull request. This keeps all communication transparent and public, allows other contributors to learn from the discussion, and follows open-source best practices. Public discussion also gives other contributors the opportunity to help and learn about the process behind the changes.

### 3. What is needed before you can create a pull request on GitHub?

- [ ] Send a patch file to maintainers via email
- [ ] Clone a repo, commit changes, and force push
- [ ] Get accepted as a team member
- [x] **Fork a repo, clone it, commit changes, and push to your fork** ✅

**Explanation:** Before creating a pull request on GitHub, you need to: 1) Fork the repository to create your own copy, 2) Clone your fork to your local machine, 3) Make changes and commit them, and 4) Push the changes to your fork. Only then can you create a pull request from your fork to the original repository. This process ensures you have the necessary permissions to make changes without directly affecting the original repository.

# 9.7 Summary

In this module, you wanted to take part in the open-source community by learning how to provide support and contribute to open-source projects using GitHub.

## What you've learned

You learned how to **find projects to contribute to** on GitHub. You discovered how to **familiarize yourself with the project and its guidelines**. You learned how to use the **issue tracker and labels** to find tasks to work on. You also learned that via **GitHub Sponsors** you can financially support your favorite projects and open-source contributors.

After discovering where you can provide help, you learned how to use GitHub to **create your first contribution and submit a pull request**. You learned that it's important to write a succinct description of the changes you make to a project. Use **imperative, present tense**, and explain *what* and *why* and not *how*. These good practices will increase the likelihood of your changes getting merged. 

Finally, you learned how to **communicate effectively with project maintainers** and how to **conduct code reviews**.

## Key skills acquired

- **Project discovery:** Finding suitable open-source projects using GitHub search and topics
- **Community research:** Understanding project guidelines, documentation, and communication channels
- **Task identification:** Using issues, labels, and `/contribute` URLs to find beginner-friendly tasks
- **Technical workflow:** Fork → Clone → Branch → Commit → Push → Pull Request process
- **Professional communication:** Writing effective commit messages and PR descriptions
- **Code review participation:** Engaging constructively with maintainers and other contributors
- **Alternative contributions:** Supporting projects through GitHub Sponsors

You're now equipped with the knowledge and skills to make meaningful contributions to the open-source ecosystem and become an active member of the GitHub community.


# 10 Manage an InnerSource program by using GitHub

Learn to manage a successful InnerSource program on GitHub through effective discoverability, guidance, and maintenance.


# 10.1 Introduction

Not long ago, the software-development world offered two sharply distinct models: **open source** and **proprietary**. Open-source software benefited from its trademark openness: anyone is allowed to offer contributions, so many people do. Proprietary software, on the other hand, limits access via a closed system that prizes the privacy of its intellectual property (IP).

Suppose you're a leader at a company that made significant investments in its proprietary software. It doesn't need to be a technology company; businesses of all shapes and sizes build and maintain their own software and other IP to enjoy a competitive edge in their industry. However, you developed a great respect for the patterns used in open source, such as:

- Source-code visibility
- Project bug awareness  
- Feature request transparency

You also like the **pull-request model** that simplifies the integration of external contributions. You'd really like to bring those benefits to your development teams, but don't want to open source the company's valuable software. 

What you really need is a hybrid that delivers the advantages of both approaches. **What you need is InnerSource.**

In this module, learn how to manage a successful InnerSource program on GitHub through effective discoverability, guidance, and maintenance.

## Learning Objectives

In this module, you learn how to:

- [ ] Contrast user- versus organization-owned projects
- [ ] Make recommendations about the number of GitHub organizations you should have
- [ ] Create discoverable repositories
- [ ] Create robust repository READMEs
- [ ] Use issue and pull-request templates
- [ ] Build transparency into repositories
- [ ] Measure the success of InnerSource within your organization
- [ ] Distribute your InnerSource toolkit

## Prerequisites

- A GitHub account
- The ability to navigate and edit files in GitHub
- Familiarity with pull requests


# 10.2 How to Manage a Successful InnerSource Program

Here, we discuss how you can design an InnerSource program to enjoy the best of open-source patterns within any software development organization.

## What is InnerSource?

Anyone can freely use, modify, and share **open-source software**. Using open-source software, anyone can view, modify, and distribute a project for any purpose with the idea that sharing code leads to better, more reliable software.

**InnerSource** is the practice of applying open-source patterns to projects with a limited audience. For example, a company might establish an InnerSource program that mirrors the structure of a typical open-source project, except that it's only accessible to the employees of that company. In effect, it's an open-source program behind your company's firewall.

## InnerSource Benefits

An InnerSource program can offer numerous benefits beyond what traditional closed-source models provide.

### 1. Encourage Transparency
Access to the source code of other company projects can help developers be more productive when working on their own projects. They can:
- See how different teams solve problems similar to the ones they're facing
- Find code and other assets that they can reuse
- Access team issues, pull requests, and project plans for better understanding of velocity and direction

### 2. Reduce Friction
Let's say that a consumer team is dependent on a bug fix or new feature for a project owned by a different team. In an InnerSource program:
- They have a channel through which they can propose the changes they need
- If changes can't be merged, the consumer team has the option of forking the project to meet their needs

### 3. Standardize Practices
Building an InnerSource program is a great opportunity to adopt standard conventions that can be used across every development team. For example:
- Two teams might prefer different processes for accepting contributions
- Having them standardize on the way they communicate their different processes makes it much easier for anyone to contribute to either

> 💡 These examples are just a few of the benefits enjoyed by InnerSource programs. To learn more, see [An introduction to InnerSource](https://innersourcecommons.org/learn/introduction/).

## Set up an InnerSource Program on GitHub

### Set Repository Visibility and Permissions

You can configure GitHub repositories with **three levels of visibility**:

| Visibility Level | Description | Use Case |
|------------------|-------------|----------|
| **Public** | Visible to everyone | Truly open source projects with access to people inside and outside organization |
| **Internal** | Only visible to organization members | **InnerSource projects** |
| **Private** | Only visible to owner and specific teams/individuals | Projects for specific users and groups only |

> ⚠️ Users who don't meet the visibility requirement see "not found" pages when they try to access your repository.

### Permission Levels

Once you establish repository visibility, you can configure permissions on an individual or team basis:

| Permission Level | Recommended For | Access |
|------------------|-----------------|---------|
| **Read** | Non-code contributors | View or discuss the project |
| **Triage** | Contributors | Manage issues and pull requests without write access |
| **Write** | Active contributors | Push to the project |
| **Maintain** | Project managers | Manage repository without sensitive/destructive actions |
| **Admin** | Full access users | Complete access including sensitive and destructive actions |

[Learn more about repository access permissions by level](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository).

## Create Discoverable Repositories

As an InnerSource program grows, the number of repositories likely scales up significantly. To make it easier for others to find and work with repositories, follow these best practices:

### Best Practices for Discoverability

- ✅ **Use descriptive repository names** (e.g., `warehouse-api` or `supply-chain-web`)
- ✅ **Include concise descriptions** (one or two sentences for potential users to understand if the project fits their needs)
- ✅ **License your repository** so customers know how they can use, change, and distribute the software
- ✅ **Include a README.md file** (GitHub uses this as the landing page)

### Add a README File

A README file communicates expectations for your project and helps manage contributions. README files can:

- **Articulate the purpose and vision** of the project so potential consumers understand whether it fits their needs
- **Offer visual aids** such as screenshots or code samples to illustrate the project in action
- **Include links** to production or demo versions of the app for review
- **Set expectations** for prerequisites and deployment procedures
- **Include references** to projects on which you depend (good way to promote others' work)
- **Use Markdown** to guide readers through properly formatted content

> 📍 **File Location Priority**: GitHub recognizes README files in this order:
> 1. `.github` directory
> 2. Repository's root directory  
> 3. `docs` directory

Check out some [Awesome README examples](https://github.com/matiassingers/awesome-readme).

## Manage Projects on GitHub

As projects gain traction, managing user influx and contributions requires structured approaches.

### Contributing Guidelines

GitHub looks for a `CONTRIBUTING.md` file in the root (or `/docs` or `/.github`) of a repository. Use this file to:

- Explain the contribution policy for the project
- Let potential contributors know what conventions the project follows
- Specify where the team is looking for pull requests
- Detail what information is requested for bug reports

> 💡 If a `CONTRIBUTING.md` exists, GitHub presents a link to it when users create issues or pull requests.

Check out some [Awesome CONTRIBUTING.md examples](https://github.com/mntnr/awesome-contributing).

### Additional Files to Consider

- **`CODEOWNERS` file** - Define individuals or teams responsible for reviewing code modifications

## Create Issue and Pull Request Templates

GitHub supports starter templates for new issues and pull requests:

### Issue Templates
- **Path**: `.github/ISSUE_TEMPLATE.md`
- **Benefit**: Users see template content when creating issues, making it easier to provide required details

### Pull Request Templates  
- **Path**: `.github/PULL_REQUEST_TEMPLATE.md`
- **Benefit**: Provides consistent structure for pull request descriptions

Check out some [Awesome GitHub issue & pull request templates](https://github.com/stevemao/github-issue-templates).

## Define Workflows

For projects encouraging external contributions, specify workflow details:

### Workflow Components
- **Branching strategy** - Where and how branches should be used for bugs and features
- **Pull request process** - How pull requests should be opened
- **Team guidelines** - Details people outside the repository team should know before pushing code

> 🔄 **Consider GitHub Flow**: If you don't yet have a workflow in mind, consider adopting [GitHub flow](https://guides.github.com/introduction/flow/).

### Release and Deployment Strategy
Communicate strategies for:
- Managing releases
- Deployment procedures
- How these affect day-to-day branching and merging

## Measuring Program Success

### Traditional vs. InnerSource Metrics

While traditional metrics like "time to market" and "bugs reported" are still applicable, they don't necessarily illustrate InnerSource benefits.

### Recommended Metrics

#### Process Metrics (Not Output)
- ⏱️ Code review turnaround time
- 📏 Pull request size  
- 🔄 Work in progress
- 📅 Time to open

#### Team-Based Metrics (Not Individual)
- 👥 Number of unique contributors to a project
- 🔄 Number of projects reusing code
- 💬 Number of cross-team @mentions

### Measurement Guidelines

When thinking about measuring InnerSource adoption, consider:

- ✅ **Measure process, not output**
- ✅ **Measure against targets, not absolutes**  
- ✅ **Measure teams, not individuals**

> ⚠️ **Important**: Metrics can harm culture and processes if misused. Use them wisely to support, not undermine, your InnerSource goals.

### Success Indicators

Consider these questions to gauge success:
- Is the repository receiving pull requests from external sources that fix bugs and add features?
- Are there active participants in discussions around the project and its future?
- Is the program inspiring InnerSource expansion that drives benefits elsewhere in the organization?

Learn about the successes others enjoyed in these [InnerSource case studies](https://innersourcecommons.org/stories/).

https://githubtraining.github.io/innersource-theory/#/measuring_success




# 10.3  Exercise - InnerSource fundamentals

An integral part of adopting InnerSource within your team is establishing goals, milestones, and then creating a checklist of items that need to be accomplished within your team to meet those goals.

The following guide provides you with a getting started and expanded checklist of items to include in your GitHub repositories for the following categories:

* Team
* Repository
* Project
* Developers

Using the provided checklists, pick one of these categories and compare the list of items to one of your existing repositories. If you're focusing on the repository itself, what files do you need to add or remove to add clarity around its purpose? How do you contribute to the repository or open up issues?

After reading through the guide and identifying ways to improve your own GitHub repositories, return here for:

* A quick knowledge check
* A summary of what you've learned
* To earn a badge for completing this module

- https://githubtraining.github.io/innersource-theory/#/measuring_success


# 10.4 Module Assessment

Choose the best response for each question.

## Check your knowledge

### **Question 1**
**Which of the following choices best describes the relationship between *open source* and *InnerSource* programs?**

- [ ] Anyone can offer a contribution to an open source program, whereas InnerSource programs only accept contributions from members of the team that owns the repository.
- [ ] InnerSource programs are forked from open source programs by organizations that only use and maintain them privately moving forward.
- [x] **InnerSource programs are fundamentally the same as open source programs, except that their access is limited to people within their organization.**

> **✅ Correct Answer**: InnerSource programs apply open-source patterns and practices within an organization's firewall, maintaining the same collaborative structure but limiting access to organization members only.

---

### **Question 2**
**Suppose your team has been receiving some low-quality bug reports without enough information to properly diagnose. Which of the following choices is the best way to address the issue?**

- [ ] Use GitHub Script to add a workflow action that automatically rejects any issues with a description fewer than 200 characters long.
- [x] **Add an `ISSUE_TEMPLATE.md` file that includes fields for reproduction steps, system properties, and instructions for generating and including important logs.**
- [ ] Add a `CONTRIBUTING.md` file that clearly explains what to include in a bug report. For example, reproduction steps, system properties, and instructions for generating and including important logs.

> **✅ Correct Answer**: Issue templates provide structured forms that guide users to include necessary information when creating bug reports, making it easier for them to provide quality reports from the start.

---

### **Question 3**
**Suppose your team has been tracking data of all kinds since your InnerSource program went live three months ago. Which of the following metrics indicates your program is a great success?**

- [x] **A dramatic rise in pull requests that address bugs in your software.**
- [ ] A growing rate of bug reports that are quickly closed because they can't be reproduced.
- [ ] A steady decline in new issues.

> **✅ Correct Answer**: A rise in pull requests that fix bugs indicates external contributors are actively participating in improving the codebase, which is a key goal of InnerSource programs - enabling collaboration and contributions from across the organization.

## 10.5 Summary

These questions test understanding of:
1. **InnerSource Definition**: The fundamental concept that InnerSource applies open-source practices within organizational boundaries
2. **Best Practices**: Using GitHub features like issue templates to improve contribution quality
3. **Success Metrics**: Recognizing that increased external contributions (pull requests) indicate program success rather than decreased activity


# Summary

In this module, you learned how to manage a successful InnerSource program on GitHub through effective discoverability, guidance, and maintenance.

## You learned about:

- [x] Contrasting user owned projects versus organization owned projects
- [x] Making recommendations about the number of GitHub organizations you should have
- [x] Creating discoverable repositories
- [x] Creating robust repository READMEs
- [x] Using templates for issue requests and pull requests
- [x] Building transparency into repositories
- [x] Measuring the success of InnerSource within your organization
- [x] Distributing your InnerSource toolkit

## Next Steps

Now that you have an InnerSource program together, learn to **Create an open-source program by using GitHub best practices**.

---

## Learn More

Here are some links to more information on the subjects we discussed in this module:

### 📚 Core Resources
- [An introduction to InnerSource](https://innersourcecommons.org/learn/introduction/)
- [Types of GitHub accounts](https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)
- [Setting base permissions for an organization](https://docs.github.com/en/organizations/managing-access-to-your-organizations-repositories/setting-base-permissions-for-an-organization)
- [Managing access to your organization's repositories](https://docs.github.com/en/organizations/managing-access-to-your-organizations-repositories)

### 🔧 Technical Best Practices
- [Git branching strategy](https://docs.github.com/en/get-started/quickstart/github-flow)
- [Best practices for protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches)
- [GitHub Collaboration Best Practices](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests)

### 📖 Templates and Examples
- [Awesome README examples](https://github.com/matiassingers/awesome-readme)
- [Awesome CONTRIBUTING.md examples](https://github.com/mntnr/awesome-contributing)
- [Awesome GitHub issue & pull request templates](https://github.com/stevemao/github-issue-templates)




