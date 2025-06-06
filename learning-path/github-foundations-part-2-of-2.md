

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

## Summary

These questions test understanding of:
1. **InnerSource Definition**: The fundamental concept that InnerSource applies open-source practices within organizational boundaries
2. **Best Practices**: Using GitHub features like issue templates to improve contribution quality
3. **Success Metrics**: Recognizing that increased external contributions (pull requests) indicate program success rather than decreased activity


# 10.5 Summary

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



# 11 Maintain a secure repository by using GitHub best practices

In this module, you'll learn best practices for building, hosting, and maintaining a secure repository on GitHub.


# 11.1 Introduction

Software security is always important, and it spans the entire software-development lifecycle. Focus is often dedicated towards writing secure code and locking down infrastructure. It's also important to protect the processes that occur during every stage of the software-development lifecycle.

Suppose you're managing an important GitHub repository. You want to enforce the highest level of security, but also want to offer a welcoming experience for contributors. Unfortunately, being secure often introduces friction that obstructs everyone's productivity. To mitigate this overhead, GitHub offers various automated features that allow you to efficiently administer a secure repository without slowing everyone down throughout the entire development process.

## Learning Objectives

In this module, you'll:

- [ ] Recognize the importance of securing your repository and shifting left in the development lifecycle
- [ ] Identify the tools, GitHub features, and best practices to establish a secure development strategy
- [ ] Keep sensitive files out of your repository by applying the use of a `.gitignore` file
- [ ] Identify how to detect and fix outdated dependencies with security vulnerabilities
- [ ] Recognize advanced security features such as code scanning and secret scanning

## Prerequisites

- A GitHub account
- The ability to navigate and edit files in GitHub


# 11.2 How to Maintain a Secure GitHub Repository

Here, we discuss some of the essential security tools and techniques available to GitHub repository administrators.

> **📝 Note**
> 
> The following content doesn't cover the fundamentals of writing secure code, but rather important security considerations, tools, and features to use within a GitHub repository.

## The Importance of a Secure Development Strategy

Application security is important. News services frequently carry stories about some breach of a company's systems and private company and customer data that was stolen.

So, what are the issues to think about when planning a secure development strategy? Clearly, we need to protect information from being disclosed to people that shouldn't have access to it, but more importantly, we need to ensure that information is only altered or destroyed when it's appropriate.

We need to make sure we properly authenticate who's accessing the data and that they have the correct permissions to do so. Through historical or archival data or logs, we need to be able to find evidence when something is wrong.

### Three Key Considerations

There are many aspects to building and deploying secure applications. Here are three things to consider:

1. **General Knowledge Problem**: Many developers and other staff members assume they understand security, but they don't. Cybersecurity is a constantly evolving discipline. A program of ongoing education and training is essential.

2. **Code Must Be Created Correctly and Securely**: We need to be sure that the code is created correctly and securely implements the required features. We also need to make sure that the features were designed with security in mind.

3. **Applications Must Comply with Rules and Regulations**: We need to make sure that the code complies with required rules and regulations. We have to test for compliance while building the code and then retest periodically, even after deployment.

## Security at Every Step

![GitHub shield with security written underneath](security-shield.png)

Security isn't something you can just add later to an application or a system. **Secure development must be part of every stage of the software-development life cycle**. This concept is even more important for critical applications and those applications that process sensitive or highly confidential information.

### Shifting Left

In practice, to hold teams accountable for what they develop, processes need to **shift left**, or be completed earlier in the development lifecycle. By moving steps from a final gate at deployment time to an earlier step, fewer mistakes are made, and developers can move more quickly.

Application-security concepts weren't a focus for developers in the past. Apart from the education and training issues, it's because their organizations emphasized fast development of features.

However, with the introduction of **DevOps practices**, security testing is easier to integrate into the pipeline. Rather than being a task performed by security specialists, security testing should just be part of the day-to-day delivery processes.

> **💡 Key Insight**
> 
> When the time for rework is taken into account, adding security to your DevOps practices earlier in the development lifecycle allows development teams to catch issues earlier. Catching issues earlier can actually reduce the overall time it takes to develop quality software.

**Shifting left** is a process change, but it isn't a single control or specific tool. It's about making all of your security more developer-centric and giving developers security feedback where they are.

## Security Tab Features

GitHub offers security features that help keep data secure in repositories and across organizations. 

### How to Access the Security Tab

1. On GitHub.com, go to the repository's main page
2. Under the repository name, select **Security**

![Screenshot showing where to locate the Security tab in GitHub](security-tab-location.png)

### Available Security Features

From the Security tab, you can add features to your GitHub workflow to help avoid vulnerabilities in your repository and codebase:

- **🛡️ Security policies** that allow you to specify how to report a security vulnerability in your project by adding a `SECURITY.md` file to your repository
- **🚨 Dependabot alerts** that notify you when GitHub detects that your repository is using a vulnerable dependency or malware
- **📋 Security advisories** that you can use to privately discuss, fix, and publish information about security vulnerabilities in your repository
- **🔍 Code scanning** that helps you find, triage, and fix vulnerabilities and errors in your code

For more information, see [GitHub security features](https://docs.github.com/en/code-security).

## Communicate a Security Policy with SECURITY.md

GitHub's community benefits are substantial, but they also carry potential risks. The fact that anyone can propose bug fixes publicly comes with certain responsibilities. The most important is the **responsible disclosure** of information that could lead to security exploits before their underlying bugs can be fixed. 

Developers looking to report or address security issues look for a `SECURITY.md` file in the root of a repository in order to responsibly disclose their concerns. Providing guidance in this file ultimately speeds up the resolution of these critical issues.

To learn more about SECURITY.md, see [Adding a security policy to your repository](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository).

## GitHub Security Advisories

GitHub Security Advisories allow repository maintainers to privately discuss and fix a security vulnerability in a project. After repository maintainers collaborate on a fix, they can publish the security advisory to publicly disclose the security vulnerability to the project's community. 

### Benefits of Security Advisories

By publishing security advisories, repository maintainers make it easier for their community to:
- Update package dependencies
- Research the consequences of the security vulnerabilities

GitHub stores the published advisories in the **Common Vulnerabilities and Exposures (CVE)** list. This list is used for automatically notifying affected repositories that use software that has a listed vulnerability. 

For more information, see [About repository security advisories](https://docs.github.com/en/code-security/security-advisories/repository-security-advisories/about-repository-security-advisories).

## Keep Sensitive Files Out of Your Repository with .gitignore

It's easy for developers to overlook files included in a commit. Sometimes these overlooked files are benign, such as intermediate build files. However, there's always the risk that someone might inadvertently commit sensitive data. For example, someone could commit an API key or private configuration data that a malicious actor could use. 

One technique to help avoid this risk is to build and maintain **`.gitignore`** files. These files instruct client tools, such as the git command line utility, to ignore paths and patterns when aggregating files for a commit.

### Sample .gitignore File

```gitignore
# User-specific files - Ignore all files ending in ".suo"
*.suo

# Mono auto generated files - Ignore all files starting with "mono_crash."
mono_crash.*

# Build results - Ignore all files in these folders found at any folder depth
[Dd]ebug/
[Rr]elease/
x64/
x86/

# Root config folder - Ignore this directory at the root due to leading slash
# Removing the slash would ignore "config" directories at all depths 
/config

# Ignore intermediate JS build files produced during TypeScript build at any 
# folder depth under /Web/TypeScript. This won't ignore JS files elsewhere. 
/Web/TypeScript/**/*.js
```

### .gitignore File Management

Your repository might include multiple `.gitignore` files. Settings are inherited from parent directories, with overriding fields in new `.gitignore` files taking precedence over parent settings for their folders and subfolders. 

It's significant effort to maintain the root `.gitignore` file, although adding a `.gitignore` file into a project directory can be helpful when that project has specific requirements that are easier to maintain separately from the parent.

To learn more about `.gitignore`, see [Ignoring files](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files). Also check out the collection of starter `.gitignore` files offered for various platforms in the [gitignore repository](https://github.com/github/gitignore).

## Remove Sensitive Data from a Repository

While `.gitignore` files can be useful in helping contributors avoid committing sensitive data, they're just a strong suggestion. Developers can still work around a `.gitignore` file to add files if they're motivated enough, and sometimes files might slip through because they don't meet the `.gitignore` file configuration. 

Project participants should always be on the lookout for commits that contain data that shouldn't be included in the repository or its history.

> **⚠️ Important**
> 
> You should assume that any data committed to GitHub at any point has been compromised. Simply overwriting a commit isn't enough to ensure the data won't be accessible in the future. For the complete guide to removing sensitive data from GitHub, see [Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

## Branch Protection Rules

You can create a branch protection rule to enforce certain workflows for one or more branches. For example, you can require an approving review or passing status checks for all pull requests merged into the protected branch.

### Workflow Protection Examples

You can use the workflows that protect the branch to:

- ✅ **Run a build** to verify the code changes can be built
- ✅ **Run a linter** to check for typos and conformation to the internal coding conventions
- ✅ **Run automated tests** to check for any behavior changes of the code
- ✅ **And so on**

## Add a CODEOWNERS File

By adding a `CODEOWNERS` file to your repository, you can assign individual team members or entire teams as code owners to paths in your repository. These code owners are then required for pull-request reviews on any changes to files in a path for which they're configured.

### Sample CODEOWNERS File

```
# Changes to files with the js extensions need to be reviewed by the js-owner user/group:
*.js    @js-owner

# Changes to files in the builds folder need to be reviewed by the octocat user/group:
/build/ @octocat
```

### CODEOWNERS File Location

You can create the `CODEOWNERS` file in either:
- The **root** of the repository
- The **docs** folder
- The **.github** folder




# 11.3 Automated Security

Here, we discuss some ways you can automate security checks in a repository that are available to GitHub repository administrators.

## Detect and Fix Outdated Dependencies with Security Vulnerabilities

Virtually every project these days takes dependencies on external packages. While these components can offer substantial benefits in productivity, they can introduce other security risks. Staying on top of these packages and their vulnerability status can be time consuming, especially given how each dependency might have its own dependencies that can become difficult to track and maintain. Fortunately, GitHub provides features that reduce this workload.

### Repository Dependency Graphs

One default feature every repository includes is **dependency graphs**. GitHub scans common package manifests, such as `package.json`, `requirements.txt`, and others. These graphs allow project owners to recursively track all of the dependencies their project relies on.

![Screenshot of a GitHub dependency graph](dependency-graph.png)

For the list of supported dependency manifests, see [About the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph).

### Dependabot Alerts

Even with a visual dependency graph, it can still be overwhelming to stay on top of the latest security considerations for every dependency a project has. To reduce this overhead, GitHub provides **Dependabot alerts** that watch your dependency graphs for you. 

#### How Dependabot Alerts Work

- 🔍 **Cross-references** target versions with versions on known vulnerability lists
- 🚨 **Alerts the project** when a risk is discovered
- 📊 **Uses input** from GitHub Security Advisories for analysis

![Screenshot of Dependabot alerts for vulnerable dependencies](dependabot-alerts.png)

### Automated Dependency Updates with Dependabot

A dependency alert can lead to a project contributor bumping the offending package reference to the recommended version and creating a pull request for validation. Wouldn't it be great if there was a way to automate this effort? Well, good news! **Dependabot does just that**.

#### Dependabot Process

1. 🔍 **Scans** for dependency alerts
2. 📝 **Creates pull requests** with recommended updates
3. ✅ **Allows contributors** to validate the update and merge the request

To learn more about Dependabot's flexibility, see [Configuring Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates).

## Automated Code Scanning

Similar to how Dependabot scans your repository for dependency alerts, you can use **code scanning** to analyze and find security vulnerabilities and errors in the code in a GitHub repository.

### Benefits of Code Scanning

Code scanning has several benefits:

- 🔍 **Find, triage, and prioritize** fixes for existing problems or potential security vulnerabilities
- 🛡️ **Help prevent developers** from introducing new security problems into the code
- 🔧 **Customize scanning** processes to match your repository's needs

### CodeQL Integration

Another advantage to code scanning is its ability to use **CodeQL**. 

#### What CodeQL Offers

- 📊 **Query code as data** - lets you treat your codebase like a database
- 🔧 **Create custom queries** or use queries maintained by the open-source community
- 🎯 **Freedom to customize** and maintain how the code within your repository is being scanned

### Enabling Code Scanning

You can enable code-scanning alerts and workflows in the **security tab** of a GitHub repository:

![Screenshot of a list of policies, advisories, and alerts with links to more information](security-policies-list.png)

Learn more about [Code scanning](https://docs.github.com/en/code-security/code-scanning) and [CodeQL](https://codeql.github.com/).

## Secret Scanning

Another automated scanning feature within a GitHub repository is **secret scanning**. Similar to the previous security scanning features, secret scanning looks for known secrets or credentials committed within the repository.

### Purpose of Secret Scanning

Secret scanning is designed to:
- 🚫 **Prevent fraudulent behavior**
- 🔒 **Secure the integrity** of any sensitive data

### How Secret Scanning Works

#### Availability
- ✅ **Public repositories**: Secret scanning occurs **by default**
- 🔒 **Private repositories**: Can be enabled by repository administrators or organization owners

#### Process Flow
1. 🔍 **Detection**: Secret scanning detects a set of credentials
2. 📧 **Notification**: GitHub notifies the service provider who issued the secret
3. ✅ **Validation**: The service provider validates the credential
4. 🎯 **Action**: Service provider decides whether to:
   - Revoke the secret
   - Issue a new secret
   - Reach out to you directly
   
> **📝 Note**: The action depends on the associated risks to you or the service provider.

Learn more about [Secret scanning for public and private repositories](https://docs.github.com/en/code-security/secret-scanning).

---

## Summary of Automated Security Features

| Feature | Purpose | Availability |
|---------|---------|--------------|
| **Dependency Graphs** | Track all project dependencies recursively | Default for all repositories |
| **Dependabot Alerts** | Alert when vulnerable dependencies detected | Available for all repositories |
| **Dependabot Updates** | Automatically create PRs for dependency updates | Configurable |
| **Code Scanning** | Find security vulnerabilities and errors in code | Configurable via Security tab |
| **Secret Scanning** | Detect committed secrets and credentials | Public repos (default), Private repos (configurable) |



# 11.4 Exercise - Secure Your Repository's Supply Chain

In this exercise, we secure your repository's supply chain through Dependency graph, Dependency alerts, Dependency security updates, and Dependency version updates.

This GitHub exercise is graded automatically once you attempt a solution to the challenge. The results of your actions and your helpful feedback are provided in real time within the `grade-learner` workflow logs.

## Helpful Tips Before You Begin

Here are some helpful tips before you begin the exercise:

* Read the **Welcome** section of the README file in the exercise's repository to understand more about the exercise.
* Follow the steps provided in the **How to start this course** section to successfully complete the exercise.
* To see the results of your exercise, navigate to your cloned repository's **Actions** tab and select the most recent run on the **Grading** workflow.
* Stuck on what to do? Revisit the content in the last unit or check out the README file in the exercise's repository.

## Important Note

> **Note**
> 
> There's a grading script under `.github/workflows/grading.yml`. You don't need to modify this workflow to complete this exercise. **Altering the contents in this workflow can break the exercise's ability to validate your actions, provide feedback, or grade the results.**

This exercise is a challenge based on content covered in this module, and there could be more than one way to successfully complete the exercise. If you get stuck, revisit previous content in this module or navigate to some of the other resources provided.

When you finish the exercise in GitHub, return here for your next unit.


# 11.5 Module Assessment

Choose the best response for each question.

## Check your knowledge

### **Question 1**
**What's the best way to make sure you're integrating the most secure versions of your project dependencies?**

- [ ] Configure your package files to always use the latest versions of dependencies.
- [ ] Check each project's security details closely before adding it to your dependencies by confirming its version status across multiple advisory sites.
- [x] **Enable Dependabot for your repository.**

> **✅ Correct Answer**: Dependabot automatically monitors your dependencies for security vulnerabilities and creates pull requests to update to secure versions. This provides automated, continuous monitoring rather than manual checking.

---

### **Question 2**
**Suppose one of your source projects relies on secrets kept in a folder called `.secrets`. You would like to make sure that the files kept in this folder on development machines aren't inadvertently committed to the repository. Which of these files best helps enforce this policy?**

- [ ] `SECURITY.md`
- [x] **`.gitignore`**
- [ ] `CONTRIBUTING.md`

> **✅ Correct Answer**: The `.gitignore` file instructs Git to ignore specified files and folders when committing. Adding `.secrets/` to `.gitignore` would prevent files in that folder from being accidentally committed to the repository.

---

### **Question 3**
**What does secret scanning do?**

- [x] **Looks for known secrets or credentials committed within the repository.**
- [ ] Analyzes and finds security vulnerabilities and errors in the code in a GitHub repository.
- [ ] Secret scanning uses CodeQL to query your code as data.

> **✅ Correct Answer**: Secret scanning specifically looks for known secrets, API keys, passwords, and other credentials that may have been accidentally committed to the repository. The other options describe code scanning (option 2) and CodeQL functionality (option 3).

## Summary

These questions test understanding of:
1. **Automated Dependency Management**: Dependabot provides the most effective automated solution for keeping dependencies secure
2. **File Exclusion**: `.gitignore` is the standard mechanism for preventing sensitive files from being committed
3. **Security Scanning Types**: Understanding the difference between secret scanning (credentials) and code scanning (vulnerabilities)


# 11.6 Summary

In this module, we talked about the importance of securing and maintaining a GitHub repository.

## You learned about:

- [x] The importance of securing your repository and shifting left in the development lifecycle
- [x] Security features and best practices within a GitHub repository
- [x] Detection of outdated dependencies with security vulnerabilities
- [x] How to add a `.gitignore` file to a repository
- [x] Advanced security features such as code scanning and secret scanning

## Next Steps

Now that you're familiar with security best practices, learn to **Automate DevOps processes by using GitHub Apps**.

---

## Learn More

Here are some links to more information on the topics we discussed in this module:

### 🔧 Dependency Management
- [Viewing and updating Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/viewing-and-updating-dependabot-alerts)
- [Dependabot official site](https://dependabot.com/)

### 🛡️ Security Tools & Policies
- [Security apps on GitHub Marketplace](https://github.com/marketplace?category=security)
- [Adding a security policy to your repository](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository)

### 📁 File Management & Data Protection
- [Ignoring files](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files)
- [Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)



# 12 Introduction to GitHub administration

Understand the security and control measures available to GitHub administrators within an organization or enterprise.

# 12.1 Introduction

GitHub administrators work to protect their organization's code and content assets while providing each team access to the repositories they rely on to collaborate and share their work.

Imagine that your CIO (Chief Information Officer) asks you for an adoption plan to help the entire company benefit from GitHub. You want to ensure every group has adequate access to the right repositories and that there's a sustainable way to provide adequate permissions to the appropriate software development and content teams. You'll need to think through the kinds of tasks that administrators need to perform and assign them the right level of access. But first, you really need to understand what options are available to you from GitHub.

## What You'll Learn

In this module, you'll learn about:

- **GitHub administrative tasks** and their purpose at each hierarchical level
- **Authentication configuration** - various ways administrators can configure authentication so users can access GitHub via web browser and git client
- **Hierarchical permission levels** and what these permissions allow you to do in GitHub

## Learning Objectives

By the end of this module, you'll be able to:

- [ ] **Summarize** the organizational structures and permission levels that GitHub administrators can use to organize members to control access and security
- [ ] **Identify** the various technologies that enable a secure authentication strategy, allowing administrators to centrally manage repository access
- [ ] **Describe** the technologies required to centrally manage teams and members using existing directory information services and how you can use GitHub itself as an identity provider for authentication and authorization


# 12.2 What is GitHub administration?


As a GitHub administrator, your goal is to keep everything working smoothly for your users. In this unit, you learn about the different levels in the GitHub organizational hierarchy and the administration tasks associated with each level.

## Administration at team level

Screenshot of the organization screen with the Teams tab highlighted.

In GitHub, each user is an organization member that you can add to a team. You can create teams in your organization with cascading access permissions and mentions reflecting your company or group's structure. A team is a useful substructure for refining repository permissions on a more granular level and enabling communication and notification between team members.

Additionally, GitHub allows you to sync your teams with identity provider (IdP) groups such as Microsoft Entra ID. When you synchronize a GitHub team with Microsoft Entra ID, you can replicate changes to GitHub automatically. This sync reduces the need for manual updates and custom scripts. You can use Microsoft Entra ID with team synchronization to manage administrative tasks such as onboarding new members, granting new permissions, and removing member access to the organization.

Members of a team with team maintainer or repository admin permissions can:

* Create a new team and select or change the parent team.
* Delete or rename a team.
* Add or remove organization members from a team, or synchronize a GitHub team's membership with an IdP group.
* Add or remove outside collaborators (people who aren't explicitly members of your organization, such as consultants or temporary employees) from team repositories.
* Enable or disable team discussions on the team's page.
* Change the visibility of the team within the organization.
* Manage automatic code review assignment for pull requests, utilizing GitHub's review assignment routing algorithm.
* Schedule reminders.
* Set the team profile picture.

## Best practices for team-level administration

Creating teams in your organization enables greater flexibility for collaboration and can make it easier to separate repositories and permissions. The following are some best practices for setting up teams on GitHub:

* Create nested teams to reflect your group or company's hierarchy within your GitHub organization.
* Help streamline PR review processes by creating teams based on interests or specific technology (JavaScript, data science, etc.). Individuals can choose to join these teams according to their interests or skills.
* Enable team synchronization between your IdP and GitHub to allow organization owners and team maintainers to connect teams in your organization with IdP groups. When you synchronize a GitHub team with an IdP group, you can replicate changes to GitHub automatically, reducing the need for manual updates and custom scripts. You can use an IdP with team synchronization to manage administrative tasks such as onboarding new members, granting new permissions, and removing member access to the organization.

## Administration at organization level

In GitHub, organizations are shared spaces enabling users to collaborate across many projects at once. Owners and administrators can manage member access to the organization's data and repositories with sophisticated security and administrative features.

Members of an organization with the owner permission can perform a wide range of activities at the organization level including:

* Invite users to join the organization, and remove members from the organization.
* Organize users into a team, and grant team maintainer permissions to organization members.
* Add or remove outside collaborators (people who aren't explicitly members of your organization, such as consultants or temporary employees) to organizational repositories.
* Grant repository permission levels to members, and set the base (default) permission level for a given repository.
* Set up organization security.
* Set up billing or assign a billing manager for the organization.
* Extract various types of information about repositories via the use of custom scripts.
* Apply organization-wide changes such as migrations via the use of custom scripts.

We recommend setting up only one organization for your users and repositories. If specific constraints in your company require you to create multiple organizations, you should be aware of the following points:

* Duplicating an organization or sharing configurations between two organizations isn't possible. This means that you must set up everything from scratch every time you create an organization, which increases the risk of errors in your settings.
* Depending on your software providers' policies, you might incur extra costs if you need to install some applications in multiple organizations.
* Managing multiple organizations is more difficult!

## Administration at enterprise level

Enterprise accounts include GitHub Enterprise Cloud and Enterprise Server instances and enable owners to centrally manage policy and billing for multiple organizations.

At the enterprise level, members of an enterprise with the owner permissions can:

* Enable security assertion markup language (SAML) single sign-on for their enterprise account, allowing each enterprise member to link their external identity on your IdP to their existing GitHub account.
* Add or remove organizations from the enterprise.
* Set up billing or assign a billing manager for all organizations in the enterprise.
* Set up repository management policies, project board policies, team policies, and other security settings that apply to all the organizations, repositories, and members in the enterprise.
* Extract various types of information about organizations via the use of custom scripts.
* Apply enterprise-wide changes such as migrations via the use of custom scripts.


# 12.3 How does GitHub authentication work?


In the previous unit, you learned about typical administration tasks at the team, organization, and enterprise level. In this unit, you'll deep dive into one of the most common administrative tasks performed by organization owners, which is setting up and controlling users' authentication to GitHub.

## GitHub's authentication options

There are several options for authenticating with GitHub:

### Username and password
Administrators can allow users to continue using the default username and password authentication method, sometimes known as the "basic" HTTP authentication scheme. In recent years, basic authentication has proven to be too risky when dealing with highly sensitive information. We strongly recommend using one (or several) of the other options listed in this unit.

### Personal access tokens
Screenshot of the personal access token screen.

Personal access tokens (PATs) are an alternative to using passwords for authentication to GitHub when using the GitHub API or the command line. Users generate a token via the GitHub's settings option, and tie the token permissions to a repository or organization. When users interact with GitHub by using the git command-line tool, they can enter the token information when they're asked for their username and password.

### SSH keys
As an alternative to using personal access tokens, users can connect and authenticate to remote servers and services via SSH with the help of SSH keys. SSH keys eliminate the need for users to supply their username and personal access token for every interaction.

When setting up SSH, users generate an SSH key, add it to the ssh-agent, and then add the key to their GitHub account. Adding the SSH key to the ssh-agent ensures that the SSH key has a passphrase as an extra layer of security. Users can configure their local copy of git to automatically supply the passphrase, or they can supply it manually each time they use the git command-line tool to interact with GitHub.

You can even use SSH keys with a repository owned by an organization that uses SAML single sign-on (SSO). If the organization provides SSH certificates, users can also use it to access the organization's repositories without adding the certificate to their GitHub account.

### Deploy keys
Deploy keys are another type of SSH key in GitHub that grants a user access to a single repository. GitHub attaches the public part of the key directly to the repository instead of a personal user account, and the private part of the key remains on the user's server. Deploy keys are read-only by default, but you can give them write access when adding them to a repository.

## GitHub's added security options

GitHub also offers the following extra security options.

### Two-factor authentication
Screenshot of the two-factor authentication screen.

Two-factor authentication (2FA), sometimes known as multifactor authentication (MFA), is an extra layer of security used when logging into websites or apps. With 2FA, users have to sign in with their username and password and provide another form of authentication that only they have access to.

For GitHub, the second form of authentication is a code generated by an application on a user's mobile device or sent as a text message (SMS). After a user enables 2FA, GitHub generates an authentication code anytime someone attempts to sign into their GitHub account. Users can only sign into their account if they know their password and have access to the authentication code on their phone.

Organization owners can require organization members, outside collaborators, and billing managers to enable 2FA for their personal accounts. This action makes it harder for malicious actors to access an organization's repositories and settings.

Enterprise owners can also enforce certain security policies for all organizations owned by an enterprise account.

### SAML SSO
If you centrally manage your users' identities and applications with an IdP, you can configure SAML SSO to protect your organization's resources on GitHub.

This type of authentication gives organization and enterprise owners on GitHub a way to control and secure access to organization resources like repositories, issues, and pull requests. Organization owners can invite GitHub users to join the organization that uses SAML SSO, which allows those users to contribute to the organization and retain their existing identity and contributions on GitHub.

When users access resources within an organization that uses SAML SSO, GitHub will redirect them to the organization's SAML IdP for authentication. After they successfully authenticate with their account on the IdP, the IdP redirects to GitHub to access the organization's resources.

GitHub offers limited support for all identity providers that implement the SAML 2.0 standard with official support for several popular identity providers including:

* Active Directory Federation Services (AD FS).
* Microsoft Entra ID.
* Okta.
* OneLogin.
* PingOne.

### LDAP
Lightweight directory access protocol (LDAP) is a popular application protocol for accessing and maintaining directory information services. LDAP lets you authenticate GitHub Enterprise Server against your existing accounts and centrally manage repository access. It's one of the most common protocols used to integrate third-party software with large company user directories.

GitHub Enterprise Server integrates with popular LDAP services like:

* Active Directory.
* Oracle Directory Server Enterprise Edition.
* OpenLDAP.
* Open Directory.


# 12.4 How does GitHub organization and permissions work?

In the previous unit, you explored the different ways that users can authenticate themselves with GitHub. In this unit, you'll learn about permissions for each hierarchical level:

* Repository permissions
* Team permissions
* Organization permissions
* Enterprise permissions

## Repository permission levels

You can customize access to a given repository by assigning permissions. There are five repository-level permissions:

* **Read**: Recommended for non-code contributors who want to view or discuss your project. This level is good for anyone that needs to view the content within the repository but doesn't need to actually make contributions or changes.
* **Triage**: Recommended for contributors who need to proactively manage issues and pull requests without write access. This level could be good for some project managers who manage tracking issues but don't make any changes.
* **Write**: Recommended for contributors who actively push to your project. Write is the standard permission for most developers.
* **Maintain**: Recommended for project managers who need to manage the repository without access to sensitive or destructive actions.
* **Admin**: Recommended for people who need full access to the project, including sensitive and destructive actions like managing security or deleting a repository. These people are repository owners and administrators.

You can give organization members, outside collaborators, and teams different levels of access to repositories owned by an organization. Each permission level progressively increases access to a repository's content and settings. Choose the level that best fits each person or team's role in your project without giving more access to the project than necessary.

After you create a repository with the correct permissions, you can make it a template so that anyone who has access to the repository can generate a new repository that has the same directory structure and files as your default branch. To make a template:

1. On GitHub.com, go to the main page of the repository.

2. Under the repository name, select Settings. If you can't see the Settings tab, open the dropdown menu, and then select Settings.

Screenshot showing where to locate the settings button in your GitHub repository.

3. Select Template repository.

## Ways Users Receive Repository Access

### Actions of a User Given a List of Their Repository Permissions

A user's effective permissions in a repository are influenced by various factors, including:

* **Repository Role**: (e.g., Admin, Write, Read)
* **Team Membership**: (e.g., inherited permissions from a team)
* **Organization Membership**: (e.g., default organization permissions, SSO requirements)

When you combine these different permission sources, GitHub applies the highest level of access granted to the user. For example, if a user has Read access through a team but also has Write access directly assigned as a collaborator, they will effectively have Write permissions.

### Repository Membership Options

When granting access to a repository, there are several ways a user can become a collaborator:

| Membership Type | Description |
|-----------------|-------------|
| **Direct Collaborator** | Added explicitly to the repository with a specific role (Read, Triage, Write, Maintain, or Admin). Recommended for external contributors or small teams. |
| **Team Membership** | A user inherits repository access via their team membership. Team permissions are often set at the organization level for consistent, scalable management. |
| **Organization Default Permissions** | If the repository is part of an organization, there may be a default permission level for all organization members (e.g., None, Read). Owners can override these defaults for specific teams or users. |
| **Outside Collaborator** | A user who is not a member of the organization but has explicit access to a repository. Useful for contractors, freelancers, or open-source contributors needing limited access. |

## Monitoring and Auditing Repository Access

Regularly auditing who has access to a repository ensures proper security and compliance. Here are some recommended steps and tools:

### View Access in Repository Settings:
* Navigate to Settings > Manage access (for the repository).
* Review the list of users and teams, along with their permission levels.

### Organization Audit Log (GitHub Enterprise or Organization-level):
* Organization owners can view changes to membership, repository access, and permissions in the Audit log.
* Filter events by repository name or access changes for a more focused view.

### Enterprise Audit Log (GitHub Enterprise):
* If you manage multiple organizations, use the Enterprise account's audit log to track changes across all organizations and repositories.
* This is especially valuable for compliance reporting or large-scale security reviews.

### Automated Scripting:
* Use the GitHub REST API or GraphQL API to programmatically list collaborators, teams, and permissions.
* Integrate scripts with your CI/CD pipeline or security dashboards to continuously monitor and flag anomalies.

**Tip**: Set up branch protection rules and required reviews to add another layer of security and accountability for all code changes.

## Team permission levels

A team in a GitHub organization is a group of users who collaborate on shared repositories. Teams help streamline access management and communication by applying consistent permissions across multiple repositories at once. Key benefits include:

* **Centralized Access Control**: Assign repository permissions (e.g., Read, Write) to the entire team instead of managing each user individually.
* **Structured Collaboration**: Organize members by department, project, or role for more efficient collaboration.
* **Visibility & Communication**: Each team can have its own discussion board, making it easier to share updates and coordinate efforts.

Teams provide an easy way to assign repository permissions to several related users at once. Members of a child team also inherit the permission settings of the parent team, providing an easy way to cascade permissions based on the natural structure of a company.

There are two levels of permissions at the team level:

| Permission level | Description |
|------------------|-------------|
| **Member** | Team members have the same set of abilities as organization members |
| **Maintainer** | Team maintainers can do everything team members can, plus: <br>• Change the team's name, description, and visibility.<br>• Request that the team change parent and child teams.<br>• Set the team profile picture.<br>• Edit and delete team discussions.<br>• Add and remove organization members from the team.<br>• Promote team members to also have the team maintainer permission.<br>• Remove the team's access to repositories.<br>• Manage code review assignment for the team.<br>• Manage scheduled reminders for pull requests. |

An organization owner can also promote any member of the organization to be a maintainer for a team.

To audit access to a repository that you administer, you can view a combined list of teams and users with access to your repository in your settings:

Screenshot of the manage access screen.

GitHub offers several permission levels that can be assigned to teams. When you grant a team access to a repository, you can choose from the following permission models:

### Permission Models

| Permission Level | Description | Best For |
|------------------|-------------|----------|
| **Read** | Users can view and clone the repository. Can open and comment on issues and pull requests. | Individuals who need read-only or review access. |
| **Triage** | Users can manage issues and pull requests (e.g., label, assign, comment). Cannot push changes to the repository. | Project managers or contributors who need to triage and organize issues without contributing code. |
| **Write** | Users can push to branches (except protected branches). Can manage issues and pull requests. | Active contributors who need to commit code or update documentation. |
| **Maintain** | Users can manage repository settings, issues, and pull requests. Cannot delete or transfer the repository. | Project maintainers who handle routine repository management but don't require full admin rights. |
| **Admin** | Users have full control over the repository, including setting permissions, deleting the repository, and managing all settings. | Those who need top-level administrative access. |

**Tip**: Always follow the Principle of Least Privilege—assign the lowest permission level necessary for each team to perform its tasks effectively. This approach reduces the risk of accidental or unauthorized changes.


# 12.5 Managing enterprise access, permissions, and governance

In the previous unit, you explored how repository and team permissions work in GitHub and how users are granted access at those levels. In this unit, you'll learn how to manage permissions and access at a broader scale across organizations and enterprises:

* Organization permissions
* Enterprise permissions
* Internal vs. external collaborators
* Least privilege strategies
* Security and governance best practices

## Organization permission levels

GitHub organizations provide a centralized way for teams to collaborate on projects while maintaining controlled access to repositories and sensitive data. Organization permissions determine what members and teams can do within the organization, ensuring that each user has the appropriate level of access.

There are multiple levels of permissions at the organizational level:

| Permission level | Description |
|------------------|-------------|
| **Owner** | Organization owners can do everything that organization members can do, and they can add or remove other users to and from the organization. This role should be limited to no less than two people in your organization. |
| **Member** | Organization members can create and manage organization repositories and teams. |
| **Moderator** | Organization moderators can block and unblock nonmember contributors, set interaction limits, and hide comments in public repositories that the organization owns. |
| **Billing manager** | Organization billing managers can view and edit billing information. |
| **Security managers** | Organization security managers can manage security alerts and settings across your organization. They can also read permissions for all repositories in the organization. |
| **Outside collaborator** | Outside collaborators, such as a consultant or temporary employee, can access one or more organization repositories. They aren't explicit members of the organization. |

In addition to these levels, you can also set default permissions for all members of your organization:

Screenshot of the member privileges screen with the base permissions dropdown displayed.

For improved management and security, you might also consider giving default read permissions to all members of your organization and adjusting their access to repositories on a case-by-case basis. If you have a relatively small organization with a low number of users, a low number of repositories, or a combination of the two, this level of restriction might be unnecessary. If you trust everyone with pushing changes to any repository, you might prefer to give all members write permissions by default.

## Enterprise permission levels

Recall from earlier that enterprise accounts are collections of organizations. By extension, each individual user account that is a member of an organization is also a member of the enterprise. You can control various settings related to authentication from this higher level.

There are three levels of permission at the enterprise level:

| Permission level | Description |
|------------------|-------------|
| **Owner** | Enterprise owners have complete control over the enterprise and can take every action, including:<br>• Managing administrators.<br>• Adding and removing organizations to and from the enterprise.<br>• Managing enterprise settings.<br>• Enforcing policies across organizations.<br>• Managing billing settings. |
| **Member** | Enterprise members have the same set of abilities as organization members. |
| **Billing manager** | Enterprise billing managers can only view and edit your enterprise's billing information and add or remove other billing managers. |
| **Guest collaborator** | Can be granted access to repositories or organizations, but has limited access by default (Enterprise Managed Users only) |

In addition to these three levels, you can also set a policy of default repository permissions across all your organizations:

Screenshot of the policies screen with the default permissions dropdown displayed.

For improved management and security, you can give default read permissions to all members of your enterprise and adjust their access to repositories on a case-by-case basis. In a smaller enterprise, such as one with a single, relatively small organization, you might prefer to trust all members with write permissions by default.

To further streamline enterprise-scale access control:

* **Nested Teams**: Enterprise accounts can use nested team structures to reflect departmental hierarchies. A parent team's permissions cascade down to child teams, simplifying complex access management.
* **Automation & Auditing**: You can use GitHub's API or GitHub Actions to automate team creation and permission assignments, and audit access via organization or enterprise audit logs.

## Enterprise Permissions and Policies via Ruleset

This section covers how to manage enterprise permissions and policies through rulesets. We'll explore best practices for structuring organizations, setting default permissions, synchronizing teams via Active Directory (AD), automating multi-org scripting, and aligning policies with your company's trust and control positions.

### Weighing the pros and cons of deploying a single versus multiple organizations

When structuring your enterprise, one of the key decisions is whether to use a single organization or multiple organizations. Each approach has unique benefits and trade-offs.

#### Single Organization

| Pros | Cons |
|------|------|
| **Simplified Management**: Centralized control of permissions and policies. | **Limited Flexibility**: One-size-fits-all policies might not suit all teams. |
| **Consistency**: Uniform application of rules and streamlined collaboration. | **Security Risks**: A single breach could impact the entire organization. |
| **Resource Sharing**: Easier asset sharing across teams. | **Scalability Issues**: Managing permissions can become complex as the organization grows. |
| **Cost Efficiency**: Reduced overhead in administrative tooling and licensing. | |

#### Multiple Organizations

| Pros | Cons |
|------|------|
| **Tailored Policies**: Customize permissions to fit the specific needs of each team. | **Increased Complexity**: More organizations mean more administrative overhead. |
| **Enhanced Isolation**: Limits the impact of a security breach to a single organization. | **Redundancy**: Potential duplication of settings and management efforts. |
| **Decentralized Administration**: Teams can manage their own policies and permissions. | **Inter-Org Collaboration**: May require extra tools or processes for cross-organization projects. |

### Setting default read versus default write across organizations

Deciding on the default permission level is critical to balancing security and collaboration within your enterprise.

#### Default Read vs Default Write

| Default Read | Default Write |
|--------------|---------------|
| **Enhanced Security**: Minimizes the risk of unintended modifications. | **Improved Collaboration**: Empowers users to contribute and modify content directly. |
| **Control**: Easier to audit and monitor changes. | **Efficiency**: Reduces bottlenecks in content creation and updates. |
| **Best For**: Environments where the majority of users only need to view resources. | **Risks**: Increases the chance of accidental changes or misconfigurations if not carefully managed. |

**Recommendation**:
Use a default read permission model and grant write access selectively, ensuring adherence to the principle of least privilege.

### Team synchronization through Active Directory (AD)

Using Active Directory (AD) for team synchronization makes user management and access control easier and more efficient.

#### Why use AD sync?
* **Single source of truth**: Keeps user identities consistent across your organization.
* **Automated access management**: Streamlines onboarding, offboarding, and role updates.
* **Seamless role alignment**: Ensures AD groups match enterprise roles and permissions.

#### Things to consider before implementing
* **Role mapping**: Clearly define how AD groups align with your organization's roles.
* **Sync frequency**: Set a schedule that balances performance and security.
* **Compliance & auditing**: Log all changes to meet compliance requirements.

By planning ahead, you can ensure a smooth integration that keeps your organization secure and well-organized.

### Maintainability: scripting for multiple organizations and access rights

As your enterprise scales, automating the management of permissions across multiple organizations is essential for maintainability.

#### Key Practices:

Automating the management of permissions across multiple organizations is crucial for maintaining efficiency and security as your enterprise grows. This section provides key practices for scripting and automation to ensure consistent and scalable permission management. By following these practices, you can streamline administrative tasks, reduce manual errors, and maintain a secure and well-organized environment.

* **Modularity**: Develop scripts in modular components to handle different organizations with minimal changes.
* **Reusability**: Create reusable functions or modules to perform common permission tasks.
* **Testing**: Thoroughly test scripts in a controlled environment before deployment.
* **Logging**: Implement detailed logging to track changes and facilitate troubleshooting.
* **Version Control**: Use version control systems (like Git) to manage script revisions and collaborate with team members.


# 12.6 Module assessment

## Check your knowledge

### **1.**
**You want to grant a user the permissions required to add and remove organization members to and from a team. Which permission would you need to grant that user?**

- [ ] The admin permission on a repository
- [ ] The maintain permission on a repository
- [ ] Organization billing manager
- [x] **Team maintainer**

> **✅ Correct Answer**: Team maintainer permissions allow users to add and remove organization members from a team, among other team management capabilities.

---

### **2.**
**As an organization owner, you want to ensure that everyone who is signed in to your corporate network can access the GitHub website without requiring a second sign-in. Which technology would you enable to accomplish this?**

- [x] **Single sign-on**
- [ ] Two-factor authentication
- [ ] Personal Access Tokens
- [ ] SSH keys

> **✅ Correct Answer**: Single sign-on (SSO) allows users to authenticate once with their corporate identity provider and access GitHub without additional sign-in requirements.

---

### **3.**
**What's the appropriate repository permission level for contributors who need to actively push changes to your repository?**

- [ ] Admin
- [x] **Write**
- [ ] Triage
- [ ] Maintain

> **✅ Correct Answer**: Write permission is the standard permission level for contributors who actively push code changes to the repository.

---

### **4.**
**Which role within a team can add or remove team members?**

- [x] **Team Maintainer**
- [ ] Team Member
- [ ] Organization Owner
- [ ] Billing Manager

> **✅ Correct Answer**: Team Maintainers have the ability to add and remove organization members from the team, while Team Members do not have this capability.

---

### **5.**
**What permission level is best for project managers who need to triage and organize issues without contributing code?**

- [x] **Triage**
- [ ] Read
- [ ] Write
- [ ] Maintain

> **✅ Correct Answer**: Triage permission allows users to manage issues and pull requests (label, assign, comment) without being able to push code changes.

---

### **6.**
**What is a benefit of integrating Active Directory (AD) for team synchronization?**

- [x] **Centralized Identity Management**
- [ ] Increased administrative overhead
- [ ] Decentralized administration
- [ ] Enhanced isolation

> **✅ Correct Answer**: AD integration provides centralized identity management, creating a single source of truth for user identities and automating access management.

---

### **7.**
**Which of the following actions is exclusive to Organization Owners in GitHub?**

- [ ] Collaborate on repositories based on assigned roles or team memberships
- [ ] Contribute code and participate in discussions
- [x] **Manage organization settings, including security and billing**
- [ ] Access resources as defined by team or repository-specific permissions

> **✅ Correct Answer**: Only Organization Owners can manage organization-level settings, including security policies and billing information.

---

### **8.**
**What is a key difference between an organization member and an outside collaborator?**

- [x] **Organization members are included in the organization's internal directory.**
- [ ] Outside collaborators have access to all repositories.
- [ ] Organization members do not appear in the organization's internal member list.
- [ ] Outside collaborators inherit organization-wide settings.

> **✅ Correct Answer**: Organization members are part of the organization's internal directory and inherit organization-wide settings, while outside collaborators have limited access to specific repositories only.

---

### **9.**
**Which permission level allows users to manage repository settings but not delete or transfer the repository?**

- [x] **Maintain**
- [ ] Write
- [ ] Admin
- [ ] Triage

> **✅ Correct Answer**: Maintain permission allows users to manage repository settings, issues, and pull requests but prevents destructive actions like deleting or transferring the repository.



# 12.7 Summary

The goal of this module was to help you develop a mental model of the roles and responsibilities of users who perform GitHub administrative tasks for companies.

GitHub supplies administrators with the tools they can use flexibly to control and protect their company's GitHub usage. Administrators can set up authentication schemes and enforce organization-wide or enterprise-wide policies. They can also design cascading permission structures that represent the natural groupings within the company.

Hierarchical levels like teams, organizations, and enterprises enable ways of setting up and controlling authentication and other security measures. Permission levels allow for fine-grained control of specific tasks. Repository permissions apply to individual users or teams of users and cascade to child teams.

Without these types of administrative controls, it would be impossible to adequately secure a company's GitHub implementation.

GitHub administrators perform vital tasks that ensure the security and viability of company repositories.

## Learn more

Here are some links to more information on the topics we discussed in this module:

* [Organizations](https://docs.github.com/en/organizations)
* [Managing team synchronization for your organization](https://docs.github.com/en/organizations/managing-saml-single-sign-on-for-your-organization/managing-team-synchronization-for-your-organization)
* [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
* [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
* [Deploy keys](https://docs.github.com/en/developers/overview/managing-deploy-keys)
* [Requiring two-factor authentication in your organization](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-two-factor-authentication-for-your-organization/requiring-two-factor-authentication-in-your-organization)
* [Enforcing policies for security settings in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-security-settings-in-your-enterprise)
* [About identity and access management with SAML single sign-on](https://docs.github.com/en/organizations/managing-saml-single-sign-on-for-your-organization/about-identity-and-access-management-with-saml-single-sign-on)
* [Using LDAP](https://docs.github.com/en/enterprise-server@latest/admin/identity-and-access-management/using-ldap-for-enterprise-iam/using-ldap)
* [Repository roles for an organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization)
* [Managing teams and people with access to your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository)
* [Assigning the team maintainer role to a team member](https://docs.github.com/en/organizations/organizing-members-into-teams/assigning-the-team-maintainer-role-to-a-team-member)
* [Roles in an organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization)
* [Setting base permissions for an organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/setting-base-permissions-for-an-organization)
* [Roles in an enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/user-management/managing-users-in-your-enterprise/roles-in-an-enterprise)
* [Enforcing repository management policies in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise)



## 13 Authenticate and authorize user identities on GitHub

This module provides an overview of the authentication and authorization options available to you in your GitHub organization or GitHub Enterprise.

# 13.1 Introduction

User authentication has traditionally been achieved using a User ID and password. A password is a single-factor form of authentication. The fundamental issue with single-factor authentication is that it's easier for any bad actor with knowledge of the sign-on information to impersonate the valid user. To prevent a breach of security for a user account, GitHub has authentication tools available to promote security best practices. You can even enforce a security policy for all GitHub users within the organization.

Controlling access to your company's data is foundational for a secure GitHub Enterprise. GitHub is committed to helping enterprises on their security journey with authentication methods to allow for more secure account access and a better user experience. In a GitHub Enterprise, most organizations want to require extra levels of authentication for better security. Enterprise System Administrators can enforce authentication and authorization security policies across an organization. These security features allow you to ensure that users are required to sign on securely to access the correct permissions in repositories. These features also include access and tools for auditing user access and activity, identity maintenance, and authentication compliance. As an administrator, you should work with your internal resources to identify what type of authentication and authorization is appropriate. This module provides an overview of the authentication and authorization options available to you in your GitHub organization or GitHub Enterprise.

## Learning goals

By the end of this module, you'll be able to:

* Describe the GitHub authentication and authorization Model.
* Understand how to manage user access to your GitHub organization through Authorization and Authentication tools.
* Identify the identity providers and technologies that support secure repository access.
* Understand the implications of enabling SAML SSO.
* Identify the authorization and authentication options available, and understand the administrator's role in enforcing a secure access strategy for a GitHub enterprise.
* Describe how users access private information in a GitHub organization.
* Evaluate the benefits of enabling Team Synchronization to manage team membership.

## Prerequisites

* Administrative access to your GitHub organization or GitHub Enterprise


# 13.2 User identity and access management

Authentication is the gateway to your enterprise's software development ecosystem. Every user's interaction with GitHub begins with identity verification. While individual accounts can rely on usernames and passwords, strong enterprise security mandates two-factor authentication (2FA) or more advanced methods like passkeys and biometric login. Balancing usability with security is key—especially in a fast-paced development environment.

## Modern Authentication in GitHub Enterprise

To ensure a secure and streamlined authentication experience, GitHub supports multiple modern methods that integrate with your identity management systems:

### Passkeys and WebAuthn
* Passkeys are a passwordless login method, tied to a physical device, and resistant to phishing.
* WebAuthn supports biometric factors and hardware tokens like YubiKey.
* These methods significantly reduce credential-based attacks and improve login UX.

### GitHub Mobile for 2FA
Users can authenticate with GitHub Mobile, which supports push notifications for quick, secure approval—enhancing 2FA without disrupting workflows.

### OAuth and GitHub Apps
* OAuth Apps use GitHub's OAuth 2.0 flow to authenticate users and grant scoped access to external applications.
* GitHub Apps authenticate as individual installations with fine-grained permissions and are ideal for CI/CD and automation pipelines.

### Enterprise Managed Users (EMU)
In GitHub Enterprise Cloud, EMUs ensure that authentication happens strictly through your Identity Provider (IdP). This model:

* Restricts access to enterprise-managed accounts only.
* Enforces centralized control over identity, credentials, and session policies.

## Organization Management with SAML SSO

One foundational capability for enterprise-grade authentication is SAML Single Sign-On (SSO). SAML links your IdP with GitHub, enabling users to sign in across services using one set of credentials. GitHub uses the IdP to verify user identity before granting access to organization or enterprise resources.

When users log into GitHub, they can see the enterprises they belong to—but access to repository data requires SAML reauthentication via the IdP.

As an Enterprise Admin, your responsibilities include:

* Authorizing access based on role and need-to-know.
* Monitoring and auditing user activity.
* Scoping permissions and minimizing surface area for attacks.

Screenshot of an example of admin repository permission list review.

To configure SAML SSO for your organization, integrate your IdP with GitHub. Supported providers include:

* Active Directory Federation Services (AD FS)
* Microsoft Entra ID
* Okta
* OneLogin
* PingOne
* Shibboleth

> **Note**
> 
> GitHub provides limited support for identity providers that implement the SAML 2.0 standard.

## Enterprise Access and Authorization Controls

Access in GitHub is governed by a robust, multi-layered authorization model:

### Fine-Grained Personal Access Tokens (PATs)
Unlike classic PATs, fine-grained PATs:

* Restrict access to specific repositories and scopes.
* Support automatic expiration for reduced risk exposure.
* Offer enhanced traceability and compliance controls.

### Custom Repository Roles
Admins can define custom roles that extend beyond the default permission sets. This supports:

* Delegated access tailored to unique workflows.
* Least-privilege enforcement for sensitive repositories.

### Security Policy Enforcement
You can enforce global security controls such as:

* Mandatory 2FA for all users.
* IP allowlists to restrict access to approved networks.
* Blocking unverified OAuth apps unless explicitly approved.

### Organizational and Enterprise-Level Controls
* Organization-level controls include default roles, team-based access, and the management of external collaborators.
* Enterprise-level governance includes:
  * Centralized SAML enforcement.
  * IdP-based login restrictions.
  * Global policy enforcement via GitHub Enterprise Cloud.

## Repository Visibility and Internal Access

When organization members create repositories, they can choose among public, private, or internal visibility options:

* **Public**: Available to anyone on the internet.
* **Private**: Restricted to selected users.
* **Internal**: Visible to all members within the enterprise but hidden from external users.

This granularity ensures that source code, documentation, and other assets are only shared with appropriate stakeholders.


# 13.3 User authentication

When it comes to user authentication, security should be the number one consideration that comes to mind. Strong security is essential. It seems like every month or so, a company reports a data breach. Credentials are stolen because of inefficient security processes, or simply because of a lack of up-to-date security features within the company. Establishing secure user authentication can be a difficult task if user adoption requires long and frustrating steps to authenticate.

GitHub Enterprise supports two recommended methods for secure user authentication:

* SAML Single Sign-On(SSO)
* Two-Factor Authentication(2FA)

## SAML SSO Authentication

SAML(Security Assertion Markup Language) SSO integrates GitHub with your organization's identity provider (IdP), allowing centralized access control, and improved compliance. When enabled, GitHub redirects users to the IdP for authentication before granting access to organization resources.

### Enabling and Enforcing SAML SSO

You can configure SAML SSO at either the organization or enterprise level, depending on the scope of enforcement you require.

#### Organization-Level SAML SSO
* **Setup**: In your org settings under Security, input your IdP's SAML SSO URL and public certificate. Test and save the configuration.
* **Enforcement**: Select Require SAML SSO authentication to remove noncompliant members automatically.
* **Use Case**: Ideal for phased rollouts or testing with limited impact.

> **Note**
> 
> GitHub removes only organization members who fail to authenticate. Enterprise members remain until they next access the resource.

#### Enterprise-Level SAML SSO
* **Setup**: In your enterprise account settings, enable SAML SSO similarly to org-level.
* **Enforcement**: Apply SSO across all organizations in your enterprise.
* **Benefits**: Ensures unified policies and reduces risk from fragmented configurations.

**Note**: GitHub does not immediately remove noncompliant enterprise members. They are prompted to authenticate upon access.

### Choosing the Right SSO Scope

| Criteria | Org-Level | Enterprise-Level |
|----------|-----------|------------------|
| **Scope** | Individual organization | Entire enterprise |
| **User Removal** | Immediate upon enforcement | Deferred until next access |
| **Policy Consistency** | Varies by org | Unified across enterprise |
| **Setup Complexity** | Lower | Higher |
| **Use Case** | Pilot/test | Broad compliance |

### Step-by-Step: Enabling and Enforcing SAML SSO

| Scope | Steps |
|-------|-------|
| **Organization** | 1. Navigate to Your organizations → Settings → Security.<br>2. Enable SAML with your IdP's details.<br>3. Test configuration and save.<br>4. Select Require SAML SSO, then remove noncompliant users. |
| **Enterprise** | 1. Navigate to Your enterprises → Settings → Security.<br>2. Enable SAML with your IdP's details.<br>3. Test configuration and save.<br>4. Enforce SSO across all orgs and review noncompliant users. |

Screenshot of the setting to require SSO authentication for all members of an organization.

## Two-Factor Authentication (2FA)

2FA adds a second verification step beyond username and password. You can require 2FA for organization members, outside collaborators, and billing managers.

> **Warning**
> 
> When you require the use of two-factor authentication for your organization, all accounts that don't use 2FA is removed from the organization and lose access to its repositories. Accounts that are affected include bot accounts.

For more detailed information about 2FA, see Securing your account with two-factor authentication (2FA).

### Enforcing 2FA
1. Navigate to your org's Security settings.
2. Enable the checkbox labeled Require two-factor authentication.
3. Communicate the requirement in advance to prevent loss of access.

Screenshot of the checkbox requiring two-factor authentication for members in the organization.

### 2FA Methods in GitHub

| Method | Description |
|--------|-------------|
| **Security Keys** | Most secure method. Physical USB or NFC devices that prevent phishing. Requires prior setup with TOTP(Time-based one-time passwords) or SMS(Short Message Service). |
| **TOTP Apps** | Recommended. Generates time-based one-time passwords, supports backup, and works offline. |
| **SMS** | Least secure. Should only be used where TOTP isn't viable. GitHub SMS support varies by region. |

#### Time-based one-time passwords
Screenshot of the time-based one-time password code.

#### GitHub SMS support
Screenshot of the SMS code.

> **Note**
> 
> Security keys store credentials locally and never expose secrets. GitHub recommends FIDO2/U2F keys.

### Auditing 2FA Compliance

To review who has enabled 2FA:

1. Go to Your organizations → select org → People tab.
2. Select the 2FA filter.
3. From here, you can identify noncompliant users and follow up outside of GitHub, typically via email.

Screenshot of the account-security setting.


# 13.4 User authorization

After a user successfully authenticates through your identity provider (IdP) using SAML single sign-on (SSO), the next critical step is authorization—granting tools like personal access tokens (PATs), SSH keys, or OAuth apps the ability to access organization resources.

## Automating User Authorization with SAML SSO and SCIM

SAML SSO enables enterprise and organization owners to control access to GitHub resources like repositories, issues, and pull requests. Integrating SCIM (System for Cross-domain Identity Management) enhances this by automating user provisioning and deprovisioning.

Screenshot of the SCIM setting.

With SCIM, new employees added to your IdP are granted access to GitHub automatically, while departing users are removed, reducing manual steps and improving security.

> **Note**
> 
> Without SCIM, SAML SSO alone does not support automatic deprovisioning of organization members.

SCIM also revokes stale tokens after a session ends, reducing security risks. Without SCIM, this must be done manually.

## Managing SSH Keys and PATs with SAML SSO

SAML SSO and SCIM work together to reflect identity changes in GitHub. To support this:

* NameID and userName must match between the SAML IdP and SCIM client.
* Group changes in your IdP trigger SCIM updates in GitHub.
* Users accessing APIs or Git must use an authorized PAT or SSH key. These are auditable and securely tied to SAML SSO.

Screenshot of the SSH key.

To simplify onboarding, provision users using: https://github.com/orgs/ORGANIZATION/sso/sign_up. Display this link in your IdP dashboard.

When users first authenticate, GitHub links their account and SCIM data to your organization. Admins can later audit or revoke sessions and credentials to automate offboarding.

## SCIM Integration with GitHub

SCIM streamlines identity management in GitHub Enterprise Cloud by supporting both native integrations and custom configurations.

### Supported SCIM Providers

GitHub natively supports:

* Okta
* Azure AD
* OneLogin
* Ping Identity
* Google Workspace

These integrations ensure reliable configuration and compatibility.

### Custom SCIM Integrations

If your IdP isn't natively supported, use GitHub's SCIM API to build custom integrations.

#### SCIM API Overview

The SCIM 2.0 API allows you to:

* Create, update, and delete users
* Manage groups

#### Example Request to Provision a User:

```http
POST /scim/v2/Users
Content-Type: application/json

{
  "userName": "jdoe",
  "name": {
    "givenName": "John",
    "familyName": "Doe"
  },
  "emails": [
    {
      "value": "jdoe@example.com",
      "primary": true
    }
  ]
}
```

GitHub processes this request and adds the user to your organization.

#### Getting Started

**For Supported Providers:**
1. Log into your IdP admin console.
2. Enable SCIM provisioning.
3. Provide GitHub's SCIM base URL and bearer token.

Screenshot of SCIM configuration steps in IdP's administrative console.

**For Custom IdPs:**
1. Use GitHub's SCIM REST API.
2. Authenticate with a PAT.
3. Test the integration with sample requests.

#### Key Benefits of SCIM Integration

* **Provisioning**: Automatically create accounts.
* **Updates**: Synchronize roles and departments.
* **Deprovisioning**: Remove access promptly upon user exit.

### SCIM vs. Manual User Management

| Aspect | SCIM-Based Management | Manual Management |
|--------|----------------------|-------------------|
| **Automation** | Automates provisioning and deprovisioning | Manual intervention required |
| **Consistency** | Standardized user data across systems | Risk of inconsistencies |
| **Security** | Timely deactivation of access | Delayed or missed revocations |
| **Scalability** | Scales with large user bases | Cumbersome at scale |
| **Compliance** | Helps meet policy and audit requirements | Harder to track and report |

## Connecting Your IdP to GitHub

You can use a supported identity provider or bring your own SAML 2.0 IdP.

### Supported (Paved Path) IdPs:
* Okta
* Azure Active Directory
* Google Workspace

Some advantages of using the supported IdPs are:

* Seamless integration
* GitHub-supported
* Lower setup effort

### Bring Your Own IdP:

Bringing your own IdP requires it isSAML 2.0 support. The advantage of this is that it allows for full flexibility.

#### Integration Steps

| Type | Steps |
|------|-------|
| **Paved Path:** | 1. Navigate to enterprise security settings.<br>2. Select your IdP.<br>3. Follow setup instructions. |
| **Custom IdP:** | 1. Go to security settings.<br>2. Choose custom IdP.<br>3. Enter SAML metadata.<br>4. Validate the connection. |

### Comparing IdP Integration Paths

| Feature | Paved Path | Bring Your Own IdP |
|---------|------------|-------------------|
| **Setup Process** | ✅ Guided setup | ⚠️ Manual configuration |
| **Flexibility** | ⚠️ Limited to listed IdPs | ✅ Any SAML 2.0 IdP |
| **Maintenance** | ✅ GitHub-managed | ⚠️ Organization-managed |
| **Customization** | ⚠️ Minimal | ✅ Fully customizable |
| **Support & Updates** | ✅ GitHub-supported | ⚠️ Self-managed |

## Managing Identities and Access

### SAML SSO Configuration
* Configure your SAML SSO URL.
* Provide your public certificate.
* Add IdP metadata.

### Credential Management
PATs and SSH keys must be explicitly authorized and linked to IdP identities to access organization resources securely.

### Auditing SAML Sessions
* View active sessions in settings.
* Revoke individual sessions as needed.

## GitHub Membership Considerations

| Type | Consideration |
|------|---------------|
| **GitHub Instance Membership** | - Access to public repositories<br>- Create personal projects<br>- Public profile visibility |
| **Organization Membership** | - Role-based internal access<br>- Profile visible to org admins<br>- May affect billing |
| **Multiple Organization Memberships** |  |


# 13.5 Team synchronization

If your company uses Microsoft Entra ID or Okta as your identity provider (IdP), you can manage GitHub team membership through team synchronization. When enabled, team sync automatically reflects changes in IdP groups on GitHub—reducing the need for manual updates or custom scripts. This centralized approach simplifies onboarding, permissions management, and access revocation.

| Feature | Description |
|---------|-------------|
| **Sync Users** | Keep GitHub Teams aligned with IdP (for example, Active Directory) group membership |
| **Sync on New Team** | Automatically populate teams at creation |
| **Custom Team Mapping** | Use syncmap.yml to define custom mappings between team slugs and group names |
| **Dynamic Config** | Use a settings file to derive sync settings from your directory structure |

## Team Synchronization Use Cases

Team sync is ideal for enterprises looking to streamline membership management within GitHub organizations. Admins can map GitHub teams to IdP groups and manage memberships automatically. This is useful for:

* Onboarding new employees
* Adjusting access as users move between teams
* Removing users who leave the organization

⚠️ To use team sync, your IdP admin must enable SAML SSO and SCIM.

## Enterprise Managed Users

If you're using Enterprise Managed Users in GitHub Enterprise Cloud, all members are provisioned through your IdP. Users don't self-manage GitHub accounts and can't access resources outside the enterprise.

With this model, you can:

* Manage organization/team membership directly through your IdP
* Ensure GitHub users are enterprise-scoped and isolated

For more, see Getting started with GitHub Enterprise Cloud.

## Team Synchronization vs. SCIM for GHES

In GitHub Enterprise Server (GHES), managing user access and team memberships can be achieved through various methods, including team synchronization and System for Cross-domain Identity Management (SCIM). Understanding these methods is essential for effective administration.

### Team Sync in GHES

Team synchronization allows you to link GitHub teams with groups in your Identity Provider (IdP). This integration ensures that any changes in the IdP group—such as adding or removing members—are automatically reflected in the corresponding GitHub team. This approach streamlines team management by centralizing user access control within the IdP.

However, it's important to note that team synchronization isn't a user provisioning service and doesn't invite non-members to join organizations in most cases. Therefore, a user will only be successfully added to a team if they're already an organization member.

Consider the following scenario to understand how team synchronization works in practice:

* When Azure AD group "DevOps Engineers" maps to GitHub team "DevOps"
* When Alice is added to the IdP group → automatically added to the GitHub team
* When she leaves the group → automatically removed from the team

> **Note**
> 
> Team Sync in GHES doesn't provision accounts. Users must already be GitHub organization members.

#### Team Sync Configuration

1. Enable Security Assertion Markup Language(SAML) Single Sign-On(SSO) and SCIM in your IdP.
2. Map GitHub teams to IdP groups via GitHub UI or API.
3. Changes in group membership sync automatically to GitHub.

**Supported IdPs:**

* **Microsoft Entra ID**: Requires permissions for profile reading and directory access.
* **Okta**: Requires SAML SSO, SCIM, tenant URL, and Single Sign-on for Web Systems(SSWS) token with read-only admin access.

#### Disable Team Sync

To disable:

1. Navigate to Settings > Organization security
2. Click Disable team synchronization

Screenshot of the organization setting to disable team synchronization.

> **Note**
> 
> Disabling sync removes users from teams if they were added via IdP mapping.

### SCIM in GHES

SCIM is an open standard protocol designed to automate the exchange of user identity information between identity domains and IT systems. In the context of GHES, SCIM enables administrators to provision, update, and deprovision user accounts directly through the GitHub API. This means you can create, update, and delete user accounts, and sync group information to map GitHub team memberships.

SCIM is useful for managing user lifecycles at scale, ensuring that user data remains consistent across systems.

Consider the following scenario to understand how SCIM works in practice:

* Okta SCIM integration provisions GitHub users automatically
* Bob is added to Okta → GitHub account is provisioned
* Bob changes roles → access and teams update
* Bob leaves → account is deprovisioned

**Key Benefit**: Full automation for account lifecycle management.

## Team Sync vs. Group SCIM

GitHub supports two primary identity integration approaches:

* **Team Sync**: Focused on syncing group membership to GitHub teams
* **Group SCIM**: Focused on full lifecycle management of users and groups

### Differences Between Team Sync and Group SCIM

| Feature | Team Sync | Group SCIM |
|---------|-----------|------------|
| **Focus** | Team-level mapping | User and group provisioning |
| **Setup** | Manual group-to-team mapping | Automated via IdP SCIM config |
| **Automation Level** | Syncs group membership only | Full lifecycle automation |
| **Ideal Use Case** | GitHub Teams management | Large orgs with high user turnover |
| **Deprovisioning** | Manual or IdP-group dependent | Fully automated |
| **Identity Model** | Classic | Managed Users |

### Choosing the Right Approach

The choice between Team Sync and Group SCIM depends on your organization's needs, size, and existing identity management infrastructure:

| Use Case | Recommended Solution |
|----------|---------------------|
| Manage repository access by teams | Team Sync |
| Automate user lifecycle | Group SCIM |
| Need full IdP-based governance | Group SCIM |
| GitHub Teams is core to workflow | Team Sync |

## Usage Limits

When using team synchronization, observe these limits:

* Max members per team: 5,000
* Max members per organization: 10,000
* Max teams per organization: 1,500

Exceeding these may result in performance issues or sync failures.

# 13.6 Module assessment

## **1.**
**What type of user authentication is used to verify a user identity against a known identity provider?**

- [ ] Two-factor authentication (2FA)
- [ ] Time-based One-time Password (TOTP)
- [x] **SAML Single Sign-on (SAML SSO)**
- [ ] Short Message Service (SMS)

> **✅ Correct Answer**: SAML SSO integrates GitHub with your organization's identity provider (IdP), allowing centralized access control by verifying user identity against the IdP.

---

## **2.**
**You're an admin and want to enable team synchronization for your organization. What installation permissions do you need to configure team synchronization for Microsoft Entra ID?**

- [ ] Provide the tenant URL
- [x] **Read all users' full profiles**
- [ ] Generate a valid Single Sign-on for Web Systems (SSWS) token
- [ ] Enable SAML Single Sign-on (SSO)

> **✅ Correct Answer**: For Microsoft Entra ID team synchronization, you need permissions for profile reading and directory access, which includes reading all users' full profiles.

---

## **3.**
**Where does a user authenticate after enabling SAML Single sign-on?**

- [ ] With a GitHub login
- [ ] With the organization credentials
- [x] **With the Identity Provider (IdP)**

> **✅ Correct Answer**: When SAML SSO is enabled, GitHub redirects users to the Identity Provider (IdP) for authentication before granting access to organization resources.

---

## **4.**
**What two-factor authentication method supports the secure backup of your authentication codes in the cloud?**

- [x] **Time-based One-time Password (TOTP)**
- [ ] Short Message Service (SMS)
- [ ] Security Key

> **✅ Correct Answer**: TOTP Apps generate time-based one-time passwords, support backup, and work offline. They can securely backup authentication codes in the cloud, unlike SMS or Security Keys.



# 13.7 Summary

In this module, you learned about allowing access to your users, and how the authentication systems available for your GitHub organization help keep your sensitive data secure. You also learned about auditing which users and teams have access to the repositories in your organization. Your goal as a GitHub administrator should be to give your users access to your enterprise data with robust security restrictions that are painless to use. Securing who has access to your organization ensures that only the users who legitimately *need* access to your organization's data have it.

You learned:

* How SAML SSO and 2FA are more secure than username/password authentication.
* Which identity providers are supported by GitHub.
* How user authorization with SCIM is supported by GitHub.
* What options users have to identify with two-factor authentication.
* How team synchronization through your IdP can automate team membership and help keep access to your data secure.

The goal of managing access to your enterprise is to create a strong and secure GitHub development environment for your users. Without these authorization and authentication tools in place, your enterprise could be compromised by bad actors who take advantage of the susceptibility of username and password vulnerabilities to access your data. Use the security features you learned about in this module to build a secure way to authenticate and authorize your users within your organization. These systems of authentication and authorization, along with team synchronization, allow you to ensure organizational security, control user lifecycle management, and automate the user onboarding and off-boarding process with efficiency and security.

## Learn more

Here are some links to more detailed information on the topics we discussed in this module:

* [Managing SAML single sign-on for your organization - GitHub Docs](https://docs.github.com/en/organizations/managing-saml-single-sign-on-for-your-organization)
* [Viewing and managing a member's SAML access to your organization - GitHub Docs](https://docs.github.com/en/organizations/managing-saml-single-sign-on-for-your-organization/viewing-and-managing-a-members-saml-access-to-your-organization)
* [Preparing to require two-factor authentication in your organization - GitHub Docs](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-two-factor-authentication-for-your-organization/preparing-to-require-two-factor-authentication-in-your-organization)
* [Authorizing a personal access token for use with SAML single sign-on - GitHub Docs](https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on)
* [Authorizing an SSH key for use with SAML single sign-on - GitHub Docs](https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/authorizing-an-ssh-key-for-use-with-saml-single-sign-on)
* [Synchronizing a team with an identity provider - GitHub Docs](https://docs.github.com/en/organizations/organizing-members-into-teams/synchronizing-a-team-with-an-identity-provider-group)


# 14 Manage repository changes by using pull requests on GitHub

Learn how to manage changes to your repository source by using pull requests.

# 14.1 Introduction

Change is inevitable, especially in software repositories. Project improvements often require the coordination of many people working together in parallel to produce the right output. Responsibly tracking and merging those changes is a complex and substantial challenge.

Fortunately, pull requests offer the right balance of control and convenience. Whether you're interested in making changes, reviewing changes, or understanding the effect of changes across the repository, pull requests are the way GitHub users collaborate on code.

In this module, you learn how to manage changes to your repository source by using pull requests.

## Learning objectives

In this module, you'll:

* Review branches and their importance to pull requests.
* Define what a pull request is.
* Learn how to create a pull request.
* Understand the different pull request statuses.
* Walk through how to merge a pull request to a base branch.

## Prerequisites

* A GitHub account


# 14.2 What are pull requests?

We begin by:

* Reviewing branches and their importance to pull requests.
* Defining what a pull request is.
* Learning how to create a pull request, review pull request statuses, and merge a pull request.

## Branches

First, let's define what branches are, why they're important to developers, and how they're related to pull requests.

Branches are isolated workspaces where you can develop your work without affecting others in the repository. They allow you to develop features, fix bugs, and safely experiment with new ideas in a contained area of your repository.

Developers working on independent branches is a common concept in modern software development. By having their own branch, a developer can make any changes, called commits, without worrying about how their commits affect other developers working on their own branches.

### Merging branches

Although having each developer work on a separate branch is great for individual productivity, it opens a new challenge. At some point, each developer's branch needs to be merged into a common branch, like main. As projects scale, there can be many merges that need to happen, and it becomes increasingly important to track and review each merge. Needing to keep track of multiple changes to a project is where pull requests come in.

## What is a pull request?

A pull request is a way to document branch changes and communicate that the changes from the developer's branch are ready to be merged into the base (main) branch. Pull requests enable stakeholders to review and discuss the proposed changes to ensure that the code quality in the base branch is kept as high as possible.

In order for the two branches to be merged, they must be different from one another:

* **The compare branch** is the developer's own branch, which contains the specific changes they made.
* **The base branch**, also referred to as the main branch, is the branch that the changes need to be merged into.

The most common use of compare is to compare branches, such as when you're starting a new pull request. You're always taken to the branch comparison view when starting a new pull request.

## Create a pull request

Now let's review how to create a pull request!

1. On GitHub.com, navigate to the main page of the repository.

2. In the Branch menu, select the branch that contains your commits.

Screenshot of creating a new branch and naming it.

3. Above the list of files, in the yellow banner, select the Compare & pull request button to create a pull request for the associated branch.

Screenshot of a yellow text box, highlighting the green compare and pull request button.

4. In the base branch dropdown menu, select the branch you'd like to merge your changes into. Then select the compare branch dropdown menu to select the branch you made your changes in.

5. Enter a title and description for your pull request.

6. To create a pull request that's ready for review, select the Create Pull Request button. To create a draft pull request, select the dropdown and select Create Draft Pull Request, then select Draft Pull Request.

## Pull request statuses

Now let's review the different statuses of a pull request.

* **Draft pull request** - When you create a pull request, you can choose to either create a pull request that's ready for review or a draft pull request. A pull request with a draft status can't be merged, and code owners aren't automatically requested to review draft pull requests.

* **Open pull request** - An open status means the pull request is active and not yet merged to the base branch. You can still make commits and discuss and review potential changes with collaborators.

* **Closed pull request** - You can choose to close a pull request without merging it into the base/main branch. This option can be handy if the changes proposed in the branch are no longer needed, or if another solution is proposed in another branch.

* **Merged pull request** - The merged pull request status means that the updates and commits from the compare branch were combined with the base branch. Anyone with push access to the repository can complete the merge.

## Merge a pull request

1. Under your repository name, select Pull requests.

Screenshot of the top navigation bar of a repo with the Pull request tab highlighted.

2. In the Pull requests list, select the pull request you'd like to merge.

3. Scroll down to the bottom of the pull request. Depending on the merge options enabled for your repository, you can:

   * **Merge all of the commits into the base branch** by selecting the Merge pull request button. If the Merge pull request option isn't shown, select the merge dropdown menu, choose the Create a merge commit option, and then select the Create a merge commit button.

   Screenshot of the dropdown menu of the green merge pull request button with the Create a merge commit selected.

   * **Squash and merge** allows you to take all of your commits and combine them into one. This option can help you keep your repository history more readable and organized. Select the Squash and merge option, and then select the Squash and merge button.

   * **The Rebase and merge** option allows you to make commits without a merge commit. This option enables you to skip a merge by maintaining a linear project history. Select the merge dropdown menu, then choose the Rebase and merge option, and then select the Rebase and merge button.

4. If prompted, enter a commit message, or accept the default message.

5. If you have more than one email address associated with your account on GitHub.com, select the email address dropdown menu and select the email address to use as the Git author email address. Only verified email addresses appear in this dropdown menu. If you enabled email address privacy, then a no-reply GitHub email is the default commit author email address.

Screenshot of a commit change with a description box and the drop-down menu of the email to select as the author of the commit.

6. Select Confirm merge, Confirm squash and merge, or Confirm rebase and merge.

7. Optionally, you can delete the compare branch to keep the list of branches in your repository tidy.

Next, you complete an exercise that takes what you reviewed and applies it to a real-life example.


# 14.3 Exercise - Reviewing pull requests

This exercise checks your knowledge on using pull requests to request, review, and incorporate changes to your source repository.

## Getting started

Select the *Start the exercise on GitHub* button to navigate to a public GitHub template repository that prompts you to complete a series of small challenges. Before you can begin the exercise, complete the following tasks:

* Select the *Start course* button or the *Use this template* feature within the template repository. This prompts you to create a new repository. We recommend creating a public repository since private repositories use Actions minutes. After you make your own repository from the template, wait about 20 seconds and refresh.
* Follow the instructions in the repository's *README* file to understand how the exercise works, its learning objectives, and how to successfully complete the exercise.

After you finish the exercise in GitHub, return here for:
* A quick knowledge check
* A summary of what you've learned
* To earn a badge for completing this module

**Note**

You don't need to modify any of the workflow files to complete this exercise. **Altering the contents in this workflow can break the exercise's ability to validate your actions, provide feedback, or grade the results**.

https://github.com/skills/review-pull-requests


# 14.4 Module assessment

Choose the best response for each question.

AI-generated content The question and answer choices in this module assessment were created with AI.

**Provide feedback**

## 1. Why is it important to have separate branches for different features in a project?

- [ ] To ensure each branch is automatically merged upon completion.
- [x] **To allow simultaneous development without interfering with the main codebase.** ✅
- [ ] To limit the number of contributors on the main branch.

**Explanation:** Separate branches allow multiple developers to work on different features simultaneously without interfering with each other's work or the stable main codebase. This enables parallel development and reduces conflicts.

## 2. In GitHub, what is the role of a pull request in the development workflow?

- [x] **To facilitate code review and discussion before merging changes into the base branch.** ✅
- [ ] To permanently lock the feature branch to prevent further changes.
- [ ] To automatically merge changes from the feature branch to the base branch without review.

**Explanation:** Pull requests are designed to facilitate code review, discussion, and collaboration before changes are merged into the base branch. They provide a structured way to review code quality, discuss changes, and ensure standards are met.

## 3. When initiating a pull request, what is the 'compare branch' typically used for?

- [ ] It is a backup branch for the main branch.
- [ ] It is the branch where changes are merged automatically.
- [x] **It contains the specific changes made by the developer.** ✅

**Explanation:** The compare branch (or source branch) contains the specific changes that the developer wants to merge into the base branch. It's the branch with the new features or fixes that are being proposed for integration.

## 4. If a pull request is marked as 'Closed' in GitHub, what does this status signify?

- [ ] The pull request is open and pending review.
- [x] **The pull request was not merged into the base branch.** ✅
- [ ] The pull request has been successfully merged into the base branch.

**Explanation:** A "Closed" status means the pull request was closed without merging the changes into the base branch. If a pull request is successfully merged, it shows as "Merged" status, not "Closed."

## 5. Your organization uses GitHub for managing code changes. A developer has submitted a pull request but realizes the changes are no longer needed. What is the most appropriate action to handle this situation?

- [ ] Merge the pull request and revert the changes later.
- [x] **Close the pull request without merging it.** ✅
- [ ] Convert the pull request into a draft status.

**Explanation:** If changes are no longer needed, the most appropriate action is to close the pull request without merging it. This avoids introducing unnecessary code into the codebase and keeps the project history clean.

## 6. In a collaborative coding environment, why is it important to review pull request statuses before merging?

- [x] **To ensure code quality and compatibility before integration.** ✅
- [ ] To automatically reject any changes from external contributors.
- [ ] To lock the repository for maintenance updates.

**Explanation:** Reviewing pull request statuses helps ensure code quality, compatibility, and that all required checks (tests, reviews, etc.) have passed before integrating changes into the main codebase.

## 7. Which pull request status indicates that the proposed changes cannot be merged until further actions are taken?

- [ ] Open pull request
- [ ] Merged pull request
- [x] **Draft pull request** ✅

**Explanation:** A draft pull request indicates that the changes are still work-in-progress and cannot be merged until the author marks it as "Ready for review." This status prevents accidental merging of incomplete work.

## 8. You've completed work on a feature branch and want to propose these changes to be merged into the main branch. What steps should you take in GitHub?

- [ ] Directly merge the feature branch into the main branch without creating a pull request.
- [x] **Create a pull request from the feature branch to the main branch and ensure it is reviewed before merging.** ✅
- [ ] Delete the feature branch after pushing changes to the main branch.

**Explanation:** The proper workflow is to create a pull request from the feature branch to the main branch, allowing for code review, discussion, and quality checks before merging. This follows best practices for collaborative development.

## 9. When merging a pull request, which option helps maintain a linear project history without creating a merge commit?

- [ ] Merge pull request
- [x] **Squash and merge** ✅
- [ ] Rebase and merge

**Explanation:** "Squash and merge" combines all commits from the feature branch into a single commit and adds it to the base branch, maintaining a linear history without creating a merge commit. This creates a cleaner, more readable project history.


# 14.5 Summary

In this module, you learned how to manage changes to your repository source by using pull requests.

You learned about:
* Reviewing branches and their importance to pull requests.
* Defining what a pull request is.
* Learning how to create a pull request.
* Understanding the different pull request statuses.
* Merging a pull request to a base branch.

Now that you're familiar with merging commits using pull requests, learn to Settle competing commits by using merge conflict resolution on GitHub.

**Learn more**
* Proposing changes to your work with pull requests
* Reviewing changes in pull requests
* Incorporating changes from a pull request
* About code owners



# 15 Search and organize repository history by using GitHub

Learn to search and organize repository history by using filters, blame, and cross-linking on GitHub.

# 15.1 Introduction

GitHub projects support virtually unlimited scale. The upside of this scale is that your projects can grow to include countless files, commits, issues, pull requests, and more. The downside is, well, the same.

Suppose you're a developer working on a rapidly growing project. As more contributors come on board, they're able to add features and fix bugs at an incredible rate. However, every one of those changes likely includes a lot of contextual information buried in issues, discussions, commits, and pull requests. While that information seems fresh in everyone's mind at the time, the risk of losing that context as time passes could cost you some significant productivity down the road. What happens when a bug is reported that traces back to work that hasn't been touched for more than a year? Fortunately, GitHub offers a few ways to help you quickly ramp up for any task.

In this module, you'll learn how to search and organize repository history by using filters, blame, and cross-linking on GitHub.

**Learning objectives**

In this module, you'll:
* Find relevant issues and pull requests.
* Search history to find context.
* Make connections within GitHub to help others find things.

**Prerequisites**

* A GitHub account
* The ability to navigate and edit files in GitHub


# 15.2 How to search and organize repository history by using GitHub

Here, we'll discuss how you can use filters, blame, and cross-linking to search and organize repository history.

Put yourself in the position of a developer who has just joined a large project. Someone just posted a new issue reporting a bug related to the web app's sidebar, and you've been assigned to fix it. You've already read through the report a few times and understand the problem being described, so now you need to figure out how to get started with the fix.

As a new team member, you're not yet familiar with the codebase. You also haven't been part of the planning discussions, code reviews, or anything else that would provide you with the context you need to start implementation. You'll first need to acquire that background knowledge to best determine the right fix.

## Searching GitHub

Although you weren't around for the events that led to the sidebar's implementation, many of those events live on in the project's history. Searching the project's repository for "sidebar" will give you a starting point.

There are two search methods available on GitHub: the global search at the top of the page and the scoped search available on certain repository tabs. They support the same syntax and function in the same way, but with some key differences.

### Global search

The global search lets you use the complete search syntax to search across all of GitHub.

A screenshot of a search across GitHub.

The search results are comprehensive and include everything from code to issues to the Marketplace (and even users). This is the best way to find mentions of key terms across multiple result types and repositories.

A screenshot of global search results.

> **📝 Note**
> 
> The filter clause is:pr filters out issues returned from the issues/pull requests store. Some filter clauses, such as is:pr, are only supported by certain search providers and ignored by others. For example, the code-search provider doesn't support that clause, so it will ignore it and return the same code results either way.

In our scenario, using the global search scoped to the current repository is a good way to find code and commits that mention the term "sidebar". You'll also likely get hits for issues and pull requests, although they're not as easy to filter further in the global search results view.

To craft a complex global search, try the advanced search.

### Context search

Context searches are available on certain tabs, such as Issues and Pull requests. These searches are scoped into the current repository and only return results of that type. The benefit to this scoping is that it allows the user interface to expose known type-specific filters such as authors, labels, projects, and more.

Screenshot of a context search within a repository.

Using the context search is the preferred option when you're looking for something in the current repository. In our scenario, this is a good way to find search results mentioning "sidebar," which you could then easily refine using the filter dropdowns.

## Using search filters

There are an infinite number of ways to search using the complete search syntax. However, most searches only make use of a few common filters. While these are often available from context search dropdowns, it's sometimes more convenient to type them in directly.

Here are some example filter queries:

| Query | Explanation |
|-------|-------------|
| `is:open is:issue assignee:@me` | Open issues assigned to the current user (@me) |
| `is:closed is:pr author:contoso` | Closed pull requests created by @contoso |
| `is:pr sidebar in:comments` | Pull requests where "sidebar" is mentioned in the comments |
| `is:open is:issue label:bug -linked:pr` | Open issues labeled as bugs that do not have a linked pull request |

Learn more about Understanding the search syntax

## What is git blame?

Despite its ominous name, git blame is a command that displays the commit history for a file. It makes it easy for you to see who made what changes and when. This makes it much easier to track down other people who have worked on a file in order to seek out their input or participation.

> **📝 Note**
> 
> Some Git systems alias git praise onto git blame to avoid the implication of judgment.

### Blame in GitHub

GitHub extends the basic git blame functionality with a more robust user interface.

A screenshot of GitHub blame.

In our scenario, there are a few ways you might get to this view. You might've found some sidebar code from the global search and selected the Blame option to see who worked on it last, or maybe you found a pull request and tracked that back to the last commit that seems related to the bug description. However you got here, the blame view is an effective way to locate a subject matter expert for the task at hand.

## Cross-linking issues, commits, and more

Part of what makes GitHub great for collaborative software projects is its support for linking disparate pieces of information together. Some of this happens automatically, such as when you create a pull request from a series of commits on a branch. Other times, you can use the interface to manually link pull requests or projects to issues using the dropdown options.

### Autolinked references

To make it even easier to cross-link different items throughout your project, GitHub offers a shorthand syntax. For example, if you leave a comment like Duplicate of #8, GitHub will recognize that #8 is an issue and create the appropriate link for you.

Screenshot of an autolinked issue.

GitHub also links commits for you if you paste in the first seven or more characters of its ID.

Screenshot of an autolinked commit.

In our scenario, these links could prove very valuable for ramping up if someone thought ahead to leave the context. For example, the sidebar's current state might have had some known issues related to a JavaScript dependency. If the issue with that dependency was discussed in another issue that didn't explicitly mention "sidebar," then it would be difficult to find. However, if someone had thought ahead to link the issue in the discussion, then it could save you a lot of time now. Keep that in mind the next time you're documenting issues and pull requests.

Learn more about Autolinked references and URLs.

### Looping in users with @mention

Besides linking issues and commits, it's often helpful to associate other people with discussions. The easiest way to do this is by using an @mention. This kind of mention notifies the mentioned user so that they can participate in the discussion. It's also a good way to identify people associated with issues long after they have been closed.

Screenshot of an @ mention.



# 15.3 Exercise - Connect the dots in a GitHub repository

This exercise checks your knowledge on the ability to search and organize your repository using GitHub. In this exercise, you'll build a repository with existing commits, duplicated issues, and fix a content defect.

## Getting started

When you select the following **Start the exercise on GitHub** button, you'll be directed to a public GitHub template repository that will prompt you to complete a series of small challenges. Before you can begin the exercise, complete these tasks:

* Select the **Start course** button or the **Use this template** feature within the template repository. This prompts you to create a new repository. We recommend creating a public repository, as private repositories will use Actions minutes. After you make your own repository from the template, wait about 20 seconds and refresh.
* Follow the instructions in the repository's README to understand how the exercise works, its learning objectives, and how to successfully complete the exercise.

When you've finished the exercise in GitHub, return here for:
* A quick knowledge check
* A summary of what you've learned
* To earn a badge for completing this module

**Note**

You don't need to modify any of the workflow files to complete this exercise. **Altering the contents in this workflow can break the exercise's ability to validate your actions, provide feedback, or grade the results**.

https://github.com/skills/connect-the-dots

# 15.4 Module assessment

Choose the best response for each question.

## Check your knowledge

### 1. How does GitHub's top-level search bar differ from the search options available on repository tabs?

- [ ] Other than being located in different parts of the user interface, they're otherwise the same.
- [ ] They support different filter syntax options.
- [x] **The top-level search bar supports searching everything across all of GitHub, whereas the repository tab searches are scoped to cover specific types in the current repository.** ✅

**Explanation:** The top-level (global) search allows you to search across all of GitHub including code, issues, marketplace, and users, while repository tab searches (context searches) are scoped to the current repository and return only specific result types like issues or pull requests for that repository.

### 2. What does `git blame` do?

- [ ] It creates a bug assigned to the last person who committed changes to the specified file.
- [x] **It displays the commit history of the file.** ✅
- [ ] It reverts the effects of a `git praise` command.

**Explanation:** Despite its name, `git blame` is a command that displays the commit history for a file, showing who made what changes and when. This makes it easier to track down people who have worked on a file to seek their input or participation.

### 3. Suppose a bug issue is reported on your project, and you know which pull request introduced the problem. Which of the following options is not a cross-linking best practice?

- [x] **Don't create cross-links when the root cause of the issue is already known.** ✅
- [ ] Add a comment to the bug report that includes the pull request's author by using an @mention.
- [ ] Add a comment to the bug report that links the pull request to it using the #ID syntax.

**Explanation:** This is NOT a best practice. Even when the root cause is known, cross-linking is still valuable for providing context, documentation, and helping future developers understand the relationship between issues and pull requests. Creating these connections helps maintain project history and makes information discoverable later.


# 15.5 Summary

In this module, you learned to search and organize repository history by using filters, blame, and cross-linking on GitHub.

You learned about:
* Finding relevant issues and pull requests.
* Searching history to find context.
* Making connections within GitHub to help others find things.

Now that you're familiar with finding and organizing information on GitHub, learn to Maintain a secure repository by using GitHub best practices.

**Learn more**

Here are some links to more information on the topics we discussed in this module:
* About searching on GitHub
* Understanding the search syntax
* git blame documentation
* Viewing and understanding files
* Autolinked references and URLs

# 16  Using GitHub Copilot with Python

GitHub Copilot is an AI pair programmer that offers autocomplete-style suggestions as you code in Python.

# 16.1 Introduction

GitHub Copilot is an AI coding partner that provides autocomplete suggestions while you code. You get suggestions from Copilot by typing code or describing it in natural language.

Copilot analyses your file and related files, offering suggestions in your text editor. It uses OpenAI Codex, a new AI system developed by OpenAI, to help derive context from written code and comments, and then suggests new lines or entire functions.

GitHub Codespaces is a hosted developer environment operating in the cloud that can be run with Visual Studio Code. You can customize the development experience for any development project on GitHub, preinstalling dependencies, libraries, and even Visual Studio Code extensions and settings.

**Scenario: Improving a project**

As a developer, you want to be more productive when you're typing code for new projects and existing ones. For this task, you want to find out if an AI assistant is what you need to improve your developer workflows in code writing, documentation, testing, and more.

In this module, you learn how you can use GitHub Copilot to modify a project by using a prompt to customize a Python API. You also learn how to use live suggestions after typing initial code.

By the conclusion of this module, you have:
* Configured a GitHub repository in Codespaces and installed the GitHub Copilot extension.
* Crafted prompts to generate suggestions from GitHub Copilot.
* Learned how to apply GitHub Copilot to improve your Python projects.

**What is the main objective?**

After successfully finishing this module, you're capable of using a prompt to customize a Python project with GitHub Copilot in GitHub Codespaces.

**Prerequisites**

* Basic understanding of Python and text editors.
* Basic comprehension of Git and GitHub Fundamentals. Particularly, running basic `git` commands like `git add` and `git push`.
* A GitHub account with an active subscription for GitHub Copilot is required for either your personal GitHub account or a GitHub account managed by an organization or enterprise. For learning, the Copilot Free option with usage limits should be sufficient.

# 16.2 What is GitHub Copilot?

Often, when you write code, you need to consult official documentation or other web pages to remember syntax or how to solve a problem. You can also spend hours trying to resolve a problem when the code isn't working. Additionally, you also spend time writing tests and documentation. All these tasks are time consuming. To be more efficient, you could use code snippets or rely on tooling in your integrated development environment (IDE). But is there a better way?

## How does it work?

GitHub Copilot is an AI assistant that you use from within your IDE that's capable of generating code and much more. GitHub Copilot uses *prompts*. A prompt is natural language text that you type. Copilot uses the text to provide suggestions based on what you type.

A prompt can look like the following example:

```python
# Create a web API using FastAPI with a route to products.
```

Copilot then uses the prompt to generate a response that you can choose to accept or reject. A response to the prompt might look like the following code:

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/products")
def read_products():
    return []
```

## How it recognizes prompts

Copilot can tell that something is a prompt or an instruction if you:

- Type it as a comment in a code file with a file ending like `.py` or `.js`.
- Type text in a markdown file and wait a few seconds for Copilot to return a response.

## Accepting suggestions

What you get back from Copilot is a *suggestion*, or text that shows itself as gray code, if you use black as your text color. To accept the suggestion, you need to press the **Tab** key.

Copilot might suggest more than one thing. In this case, you can cycle between suggestions by using **Ctrl + Enter**, and select the most appropriate one.


# 16.3 Exercise - Set up GitHub Copilot to work with Visual Studio Code

In this exercise, we create a new repository using the GitHub template for the Python personal portfolio frontend web application.

## How to set up GitHub Copilot

To use GitHub Copilot, you need to complete the following steps:

### 1. GitHub Account
- Create a GitHub account. Since Copilot is a GitHub service, you need a GitHub account to use it. If you don't have an account, visit the GitHub webpage to create one for free.

### 2. Sign up and enable GitHub Copilot
- You can set up a GitHub Copilot Free account or sign up for a subscription to GitHub Copilot Pro trial with a one-time 30-day trial. For learning purposes, the Copilot Free option with usage limits should be sufficient.
- It's important to be aware of the GitHub Copilot free trial conditions: if you choose the free trial offer for GitHub Copilot, a form of payment is requested at sign-up. Charges aren't applied until the trial is over, unless you cancel before the conclusion of the 30-day period.

> **💡 Tip**
> 
> GitHub Copilot offers a free tier with **2,000 code autocompletes and 50 chat messages per month**. To get started, open Visual Studio Code, click on the GitHub Copilot icon, and then click "Sign in to Use GitHub Copilot for Free". Log in to your GitHub account in the window that will open in the browser. **Learn more**. Educators, Students and select open-source maintainers can receive Copilot Pro for free, learn how at: **https://aka.ms/Copilot4Students**.

### 3. Install the Extension
- GitHub Copilot is available as an extension for major IDEs, including Visual Studio, Visual Studio Code, JetBrains IDEs, VIM, and XCode.
- To install, search for "GitHub Copilot" in your IDE's extension marketplace and follow the installation instructions. For example, in the VS Code marketplace, you will find GitHub Copilot, GitHub Copilot Chat, and GitHub Copilot for Azure as options to install.

## Environment setup

First you need to launch the Codespaces environment, which comes preconfigured with the GitHub Copilot extension.

1. Open the Codespace with the preconfigured environment in your browser.
2. On the **Create codespace** page, review the codespace configuration settings, then select **Create new codespace**.
3. Wait for the codespace to start. This startup process can take a few minutes.
4. The remaining exercises in this project take place in the context of this development container.

> **⚠️ Important**
> 
> All GitHub accounts can use Codespaces for up to 60 hours free each month with 2 core instances. For more information, see **GitHub Codespaces monthly included storage and core hours**.

## Python Web API

When complete, Codespaces loads with a terminal section at the bottom. Codespaces installs all the required extensions in your container. Once the package installs are completed, Codespaces executes the `uvicorn` command to start your web application running within your Codespace.

When the web application successfully starts, a message in the terminal shows that the server is running on port 8000 within your Codespace.

## Testing the API

In the **Simple Browser** tab of your Codespace, on the **Containerized Python API** page, select the **Try it out** button. A **FastAPI** page opens in the **Simple Browser** tab that allows you to interact with the API by sending a request using the self-documented page.

To test the API, select the **POST** button and then the **Try it Out** button. Scroll down the tab and select **Execute**. If you scroll down the tab further, you can see the response to your sample request.


# 16.4 Use GitHub Copilot with Python

In previous units, we showed you how to set up Copilot and mentioned how it can make you faster as a developer starting to write code.

In this unit, we discuss how Copilot can help you with existing projects and with more complicated tasks.

## Developing with GitHub Copilot

Often when we build out projects, we need to continuously ensure our code is fresh and updated. Additionally, we might need to fix any bugs that come up or add new features to improve functionality and usability. Let's explore some ways to make updates with GitHub Copilot and GitHub Copilot Chat, an interactive chat interface that lets you ask and receive answers to code-related questions.

## Prompt engineering

GitHub Copilot can suggest code as you enter it, but you can also create useful suggestions by building prompts. A prompt, which is our input, is a collection of instructions or guidelines that help generate code. A prompt is useful to generate specific responses from Copilot. The prompt might be a comment or input when using GitHub Copilot Chat that steers Copilot to generate code on your behalf or writing code that Copilot autocompletes.

The quality of output from Copilot depends on how well you craft your prompt. Designing an effective prompt is crucial to ensuring you achieve your desired outcome.

For example, consider the following prompt:

```python
# Create an API endpoint
```

The prompt is ambiguous and vague, so the result from GitHub Copilot might not be what you need. It could, for example, suggest code that uses a framework that you don't know, or an endpoint that requires data that you don't recognize.

Now consider this prompt:

```python
# Create an API endpoint using the FastAPI framework that accepts a JSON payload in a POST request
```

The prompt is specific, clear, and allows GitHub Copilot to understand the goal and scope of the task. You can provide context and examples to Copilot using comments or code, but you can also use the chat option of GitHub Copilot Chat to enhance your prompt. Having a good prompt ensures that the model generates a high-quality output.

## Best practices using GitHub Copilot

Copilot supercharges your productivity but requires some good practices to ensure quality. Some best practices when using Copilot are:

Keep your prompts simple then add more elaborate components as you keep going. For example:

```text
create an HTML form with a text field and button
```

Next, elaborate more on the prompt to get more specific suggestions:

```text
Add an event listen to the button to send a POST request to /generate endpoint and display response in a div with id "result"
```

Cycle between suggestions. You can do this using `Ctrl+Enter` (or `Cmd+Enter` on a Mac). You get various suggestions from Copilot, and you can pick the best output. Optionally, when using GitHub Copilot Chat, you can use the chat input to add your prompt and interact with the output.

If you're not getting the results you want, then you can reword the prompt or start writing code for Copilot to autocomplete.

**Note**

GitHub Copilot uses open files in your text editor as additional context. This is helpful because it provides useful information in addition to the prompt or code you may be writing. If you need GitHub Copilot to provide suggestions based on other files you can open those or use `@workspace` with your prompt when using GitHub Copilot Chat.


# 16.5 Exercise - Update a Python web API with GitHub Copilot

**Completed** • **100 XP** • **5 minutes**

Let's explore how you can modify a Python repository using code suggestions from GitHub Copilot to create an interactive HTML form and an Application Programming Interface (API) endpoint. By working with this repository, you quickly get hands-on with a Python web app that serves an HTTP API that generates a pseudo-random token, commonly used in identification routines.

## What is an API?

An API acts as the intermediary that allows different applications to communicate with each other. For example, a weather website can either share historical data or provide forecast functionality through its API. Using the API, you can embed the data into your website or create an application sharing weather data with other features.

## Extend the Web API

The API already has a single endpoint to generate a token. Let's update the API by adding a new endpoint that accepts text and returns a list of tokens.

> **📝 Note**
> 
> For this exercise, use the **Codespace with the preconfigured environment** in your browser.

### Step 1: Add a Pydantic model

Go to the `main.py` file, and add a comment so that GitHub Copilot can generate a `Pydantic` model for you. The generated model should look like this example:

```python
class Text(BaseModel):
    text: str
```

### Step 2: Generate a new endpoint

Next, generate a new endpoint with GitHub Copilot by adding the comment:

```python
# Create a FastAPI endpoint that accepts a POST request with a JSON body containing a single field called "text" and returns a checksum of the text
```

### Step 3: Add necessary imports

The generated code can cause the application to crash if the `base64` and `os` modules aren't imported. Use GitHub Copilot Chat to ask Copilot to help you add the missing imports.

Alternatively, add the following lines to the top of the file:

```python
import base64
import os
```

Finally, verify the new endpoint is working. Try it out by going to the `/docs` endpoint and confirming that the endpoint shows up.

## Conclusion

Congratulations, through the exercise, you not only used Copilot to generate code, but you also did it in an interactive and fun way! You can use GitHub Copilot to generate code, write documentation, test your applications, and more.

When you finish the exercise in GitHub, return here for:
* A quick knowledge check
* A summary of what you've learned
* A badge for completing this module


# 16.6 Module assessment

## Check your knowledge

### 1. How does GitHub Copilot work?

- [x] **GitHub Copilot uses prompts and natural language text that you type to provide coding suggestions.** ✅
- [ ] GitHub Copilot uses lights, that you type, and it provides suggestions based on what you type.
- [ ] GitHub Copilot uses radio language, that you type, and it provides suggestions based on what you type.

**Explanation:** GitHub Copilot works by analyzing prompts and natural language text that you type (usually as comments in code files) to generate relevant coding suggestions based on the context and your input.

### 2. What are some GitHub Copilot Free features?

- [ ] It's a free unrestrticted AI tool that works independent of code editors.
- [x] **It provides several suggestions and chats per month directly in your IDE and on github.com.** ✅
- [ ] An option to enable slower responses, preservering your Copilot Pro quota.

**Explanation:** GitHub Copilot Free provides a limited number of code autocompletes (2,000) and chat messages (50) per month, working directly within your IDE and on GitHub.com. It's not unlimited and requires integration with supported code editors.

### 3. How can you accept GitHub Copilot's suggestions?

- [x] **Press the Tab key.** ✅
- [ ] Press the F1 key.
- [ ] Press the F4 key.

**Explanation:** To accept GitHub Copilot's suggestions, you press the Tab key. The suggestions appear as gray text (ghost text) in your editor, and pressing Tab accepts and inserts the suggested code.

### 4. Identify which statement is valid and select the correct answer:

- [ ] A prompt, which is our output, is a collection of songs that tells our copilot what to generate.
- [x] **A prompt, which is our input, is a collection of instructions or guidelines that tell our copilot what to generate.** ✅
- [ ] A prompt, which is our document, is a collection of laptops that tells our Copilot what to generate.

**Explanation:** A prompt is the input you provide to GitHub Copilot - it's a collection of instructions or guidelines (usually written as natural language comments) that tell Copilot what kind of code to generate.

### 5. What does the quality of the output from GitHub Copilot depend on?

- [ ] Your code editor.
- [ ] How well your extensions were installed.
- [x] **How well you crafted your prompt.** ✅

**Explanation:** The quality of GitHub Copilot's output directly depends on how well you craft your prompt. Clear, specific, and detailed prompts lead to better, more relevant code suggestions, while vague or ambiguous prompts may result in less useful output.


# 16.7 Summary

In this module, we looked at how GitHub Codespaces can significantly improve the software development lifecycle, offering features that range from creating a repository from a GitHub template to adding animations with live suggestions. GitHub Codespaces allows you to customize your coding experience and GitHub Copilot guides you in each step of the way.

## What you've learned

After finishing this module, you should be able to:

- Configure a GitHub repository in Codespaces and install the GitHub Copilot extension
- Engineer prompts for your project that follow best practices to generate suggestions from GitHub Copilot
- Use GitHub Copilot Chat to ask and receive coding-related questions

## Delete your Codespaces resources

To avoid consuming all of your monthly GitHub Codespaces time, it's important to delete your resources after you upload your changes to your repository.

Use the following steps to delete your Codespace instance:

1. Go to [GitHub Codespaces](https://github.com/codespaces).
2. Find your Codespace instance in the list, and select the **...** menu to display your options.
3. Select **Delete** to remove your Codespace instance.

> **⚠️ Note**
> 
> If you don't commit your changes to your repository, you will lose all your work. Therefore, it's important to commit and push your changes before deleting your Codespace instance.

## References

- [What is GitHub Copilot?](https://docs.github.com/en/copilot/overview-of-github-copilot/about-github-copilot-for-individuals)
- [Introduction to GitHub Copilot](https://docs.github.com/en/copilot/quickstart)
- [Code with GitHub Codespaces](https://docs.github.com/en/codespaces)
