

# GitHub Foundations Part 1 of 2
https://learn.microsoft.com/en-us/training/paths/github-foundations/


# The GitHub Foundations Learning Path Part 1 of 2

The GitHub Foundations Learning Path Part 1 of 2 is a concise and beginner-friendly journey designed to introduce you to the fundamental concepts and products of GitHub. You'll discover the benefits of using GitHub as a collaborative platform and explore its core features, such as repository management, commits, branches, and merging.

## In this learning path, you'll:

- Gain an understanding of GitHub's essential tools
- Become familiar with Git
- Learn about GitHub Copilot

## Prerequisites

- A GitHub account



# 1. Introduction to Git

Find out what source control is, and get an introduction to Git—the world's most popular version control system.

# 1.1 Introduction

Imagine you're a new software developer at a firm that writes avionics software for commercial airliners. Quality control is critical, and developers work in small teams using Git for version control. You've heard of version control, but you've never used Git, so you're eager to catch up!

You decide to build a website that lets you and your friends share pictures of your cats, so you can learn Git in a fun environment before bringing that knowledge to work. You set out to build the site by using Git to keep track of changes and keep all the source code files backed up in case the server goes down. But before diving head-first into Git, you must cover the basics.

In this module, you'll get an introduction to version control, and Git. Git can seem a little cryptic at first, and it can even be frustrating at times. But if you learn it step by step, you'll find that there's a reason Git is quickly becoming the world's most popular version control system—not just for software developers, but also for teams that write documentation and collaborate on other work.

## Watch a Video

For an overview of the exercises in this module, see the video Introduction to Git Recap.

## Learning Objectives

In this module, you'll:

- Learn what version control is
- Understand distributed version control systems, like Git
- Recognize the differences between Git and GitHub and the roles they play in the software development lifecycle


# 1.2 What is Version Control?

A version control system (VCS) is a program or set of programs that tracks changes to a collection of files. One goal of a VCS is to easily recall earlier versions of individual files or of the entire project. Another goal is to allow several team members to work on a project, even on the same files, at the same time without affecting each other's work.

Another name for a VCS is a software configuration management (SCM) system. The two terms often are used interchangeably—in fact, Git's official documentation is located at git-scm.com. Technically, version control is just one of the practices involved in SCM. A VCS can be used for projects other than software, including books and online tutorials.

## What You Can Do with a VCS

With a VCS, you can:

- See all the changes made to your project, when the changes were made, and who made them
- Include a message with each change to explain the reasoning behind it
- Retrieve past versions of the entire project or of individual files
- Create branches, where changes can be made experimentally. This feature allows several different sets of changes (for example, features or bug fixes) to be worked on at the same time, possibly by different people, without affecting the main branch. Later, you can merge the changes you want to keep back into the main branch
- Attach a tag to a version—for example, to mark a new release

Git is a fast, versatile, highly scalable, free, open-source VCS. Its primary author is Linus Torvalds, the creator of Linux.

## Distributed Version Control

Earlier instances of VCSes, including CVS, Subversion (SVN), and Perforce, used a centralized server to store a project's history. This centralization meant that the one server was also potentially a single point of failure.

Git is distributed, which means that a project's complete history is stored both on the client and on the server. You can edit files without a network connection, check them in locally, and sync with the server when a connection becomes available. If a server goes down, you still have a local copy of the project. Technically, you don't even have to have a server. Changes could be passed around in e-mail or shared by using removable media, but no one uses Git this way in practice.

## Git Terminology

To understand Git, you have to understand the terminology. Here's a short list of terms that Git users frequently use. Don't be concerned about the details for now; all these terms will become familiar as you work your way through the exercises in this module.

**Working tree:** The set of nested directories and files that contain the project that's being worked on.

**Repository (repo):** The directory, located at the top level of a working tree, where Git keeps all the history and metadata for a project. Repositories are almost always referred to as repos. A bare repository is one that isn't part of a working tree; it's used for sharing or backup. A bare repo is usually a directory with a name that ends in .git—for example, project.git.

**Hash:** A number produced by a hash function that represents the contents of a file or another object as a fixed number of digits. Git uses hashes that are 160 bits long. One advantage to using hashes is that Git can tell whether a file has changed by hashing its contents and comparing the result to the previous hash. If the file time-and-date stamp is changed, but the file hash isn't changed, Git knows the file contents aren't changed.

**Object:** A Git repo contains four types of objects, each uniquely identified by an SHA-1 hash. A blob object contains an ordinary file. A tree object represents a directory; it contains names, hashes, and permissions. A commit object represents a specific version of the working tree. A tag is a name attached to a commit.

**Commit:** When used as a verb, commit means to make a commit object. This action takes its name from commits to a database. It means you are committing the changes you have made so that others can eventually see them, too.

**Branch:** A branch is a named series of linked commits. The most recent commit on a branch is called the head. The default branch, which is created when you initialize a repository, is called main, often named master in Git. The head of the current branch is named HEAD. Branches are an incredibly useful feature of Git because they allow developers to work independently (or together) in branches and later merge their changes into the default branch.

**Remote:** A remote is a named reference to another Git repository. When you create a repo, Git creates a remote named origin that is the default remote for push and pull operations.

**Commands, subcommands, and options:** Git operations are performed by using commands like git push and git pull. git is the command, and push or pull is the subcommand. The subcommand specifies the operation you want Git to perform. Commands frequently are accompanied by options, which use hyphens (-) or double hyphens (--). For example, git reset --hard.

These terms and others, like push and pull, will make more sense shortly. But you have to start somewhere, and you might find it helpful to come back and review this glossary of terms after you finish the module.

## The Git Command Line

Several different GUIs are available for Git, including GitHub Desktop. Many programming editors, like Microsoft Visual Studio Code, also have an interface to Git. They all work differently and they have different limitations. None of them implement all of Git's functionality.

The exercises in this module use the Git command line—specifically, Git commands executed in Azure Cloud Shell. However, Git's command-line interface works the same, no matter what operating system you're using. Plus, the command line lets you tap into all of Git's functionality. Developers who see Git only through a GUI sometimes find themselves confronted with error messages they can't resolve, and they have to resort to the command line to get going again.

## Git and GitHub

As you work with Git, you might wonder about differences between the features it offers and the features offered on GitHub.

As mentioned earlier, Git is a distributed version control system (DVCS) that multiple developers and other contributors can use to work on a project. It provides a way to work with one or more local branches and then push them to a remote repository.

GitHub is a cloud platform that uses Git as its core technology. GitHub simplifies the process of collaborating on projects and provides a website, more command-line tools, and overall flow that developers and users can use to work together. GitHub acts as the remote repository mentioned earlier.

### Key Features Provided by GitHub Include:

- Issues
- Discussions
- Pull requests
- Notifications
- Labels
- Actions
- Forks
- Projects

To learn more about GitHub, see the Introduction to GitHub Microsoft Learn module or the Getting started with GitHub help documentation.

The next step is to try out Git for yourself!


# 1.3 Exercise - Try Out Git


## Verify Your Account

Before you can create your first repo, you must make sure that Git is installed and configured. Git comes preinstalled with Azure Cloud Shell, so we can use Git in Cloud Shell to the right.

## Configure Git

In Cloud Shell, to double-check that Git is installed, type `git --version`:

```bash
git --version
```

> **Tip**
> 
> You can use the Copy button to copy commands to the clipboard. To paste, right-click on a new line in the Cloud Shell terminal and select Paste, or use the Shift+Insert keyboard shortcut (⌘+V on macOS).

You should see output that looks something like this example:

```
git version 2.7.4
```

To configure Git, you must define some global variables: `user.name` and `user.email`. Both are required for you to make commits.

Set your name in Cloud Shell with the following command. Replace `<USER_NAME>` with the user name you want to use.

```bash
git config --global user.name "<USER_NAME>"
```

Now, use this command to create a `user.email` configuration variable, replacing `<USER_EMAIL>` with your e-mail address:

```bash
git config --global user.email "<USER_EMAIL>"
```

Run the following command to check that your changes worked:

```bash
git config --list
```

Confirm that the output includes two lines that are similar to the following example. Your name and e-mail address will be different from what's shown in the example.

```
user.name=User Name
user.email=user-name@contoso.com
```

## Set Up Your Git Repository

Git works by checking for changes to files within a certain folder. We'll create a folder to serve as our working tree (project directory) and let Git know about it, so it can start tracking changes. We tell Git to start tracking changes by initializing a Git repository into that folder.

Start by creating an empty folder for your project, and then initialize a Git repository inside it.

1. Create a folder named Cats. This folder will be the project directory, also called the working tree. The project directory is where all files related to your project are stored. In this exercise, it's where your website and the files that create the website and its contents are stored.

```bash
mkdir Cats
```

2. Change to the project directory by using the `cd` command:

```bash
cd Cats
```

3. Now, initialize your new repository and set the name of the default branch to main:

**If you're running Git version 2.28.0 or later, use the following command:**

```bash
git init --initial-branch=main
```

**Or use the following command:**

```bash
git init -b main
```

**For earlier versions of Git, use these commands:**

```bash
git init
git checkout -b main
```

After you run the initialize command, you should see output that's similar to this example:

```
Initialized empty Git repository in /home/<user>/Cats/.git/

Switched to a new branch 'main'
```

4. Now, use a `git status` command to show the status of the working tree:

```bash
git status
```

Git responds with this output, which indicates that main is the current branch. (It's also the only branch.) So far, so good.

```
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

5. Use an `ls` command to show the contents of the working tree:

```bash
ls -a
```

Confirm that the directory contains a subdirectory named `.git`. (Using the `-a` option with ls is important because Linux normally hides file and directory names that start with a period.) This folder is the Git repository—the directory in which Git stores metadata and history for the working tree.

You typically don't do anything with the `.git` directory directly. Git updates the metadata there as the status of the working tree changes to keep track of what's changed in your files. This directory is hands-off for you, but it's incredibly important to Git.

## Get Help from Git

Git, like most command-line tools, has a built-in help function that you can use to look up commands and keywords.

Type the following command to get help with what you can do with Git:

```bash
git --help
```

The command displays the following output:

```
usage: git [--version] [--help] [-C <path>] [-c name=value]
       [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
       [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
       [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
       <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   branch     List, create, or delete branches
   checkout   Switch branches or restore working tree files
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   merge      Join two or more development histories together
   rebase     Forward-port local commits to the updated upstream head
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
```

Read through the different options available with Git and note that each command comes with its own help page, for when you start digging deeper. Not all these commands will make sense yet, but some might look familiar if you have experience using a VCS.

In the next lesson, you learn more about the commands you just tried and the basics of Git.



# 1.4 Basic Git Commands

Git works by remembering the changes to your files as if it's taking snapshots of your file system.

We'll cover a few basic commands to start tracking files in your repo. Then, you'll save your first "snapshot" for Git to compare against.

## `git status`

The first and most commonly used Git command is `git status`. You've already used it once, in the preceding exercise, to see that you had initialized your Git repo properly.

`git status` displays the state of the working tree (and of the staging area—we'll talk more about the staging area soon). It lets you see which changes are currently being tracked by Git, so you can decide whether you want to ask Git to take another snapshot.

## `git add`

`git add` is the command you use to tell Git to start keeping track of changes in certain files.

The technical term is *staging* these changes. You'll use `git add` to stage changes to prepare for a commit. All changes in files that have been added but not yet committed are stored in the *staging area*.

## `git commit`

After you've staged some changes for commit, you can save your work to a snapshot by invoking the `git commit` command.

*Commit* is both a verb and a noun. It has essentially the same meaning as when you commit to a plan or commit a change to a database. As a verb, committing changes means you put a copy (of the file, directory, or other "stuff") in the repository as a new version. As a noun, a commit is the small chunk of data that gives the changes you committed a unique identity. The data that's saved in a commit includes the author's name and e-mail address, the date, comments about what you did (and why), an optional digital signature, and the unique identifier of the preceding commit.

## `git log`

The `git log` command allows you to see information about previous commits. Each commit has a message attached to it (a commit message), and the `git log` command prints information about the most recent commits, like their time stamp, the author, and a commit message. This command helps you keep track of what you've been doing and what changes have been saved.

## `git help`

You've already tried out the `git help` command, but it's worth reminding you about. Use this command to easily get information about all the commands you've learned so far, and more.

Remember, each command comes with its *own* help page, too. You can find these help pages by typing `git <command> --help`. For example, `git commit --help` brings up a page that tells you more about the `git commit` command and how to use it.

# 1.5 Module Assessment

## 1. Which of the following scenarios is a common use case for a version control system?

- [ ] Deleting earlier versions of a project or file, so you know you are working only with the most current file or data.
- [x] **Making experimental changes to your project in an isolated branch.**
- [ ] Gathering feature requirements for a large project and communicating them to stakeholders.

**Answer: Making experimental changes to your project in an isolated branch.**

*Explanation: Version control systems like Git allow you to create branches where changes can be made experimentally. This feature allows different sets of changes to be worked on at the same time without affecting the main branch.*

## 2. What is another name for a version control system?

- [ ] Version management software (VMS)
- [ ] Software control management (SCM) system
- [x] **Software configuration management (SCM) system**

**Answer: Software configuration management (SCM) system**

*Explanation: A version control system (VCS) is also known as a software configuration management (SCM) system. The two terms are often used interchangeably.*

## 3. What's the difference between Git and GitHub?

- [x] **Git lets you work with one or more local branches and push changes to a remote repository. GitHub acts as the remote repository, which is accessed through a website or command-line tools.**
- [ ] Git is a distributed version control system (DVCS) that runs in the cloud. GitHub is an interface layer that provides access to Git technology.
- [ ] Git is used by an individual contributor. GitHub is used by multiple contributors to simplify group development work.

**Answer: Git lets you work with one or more local branches and push changes to a remote repository. GitHub acts as the remote repository, which is accessed through a website or command-line tools.**

*Explanation: Git is a distributed version control system that allows you to work with local branches and push to remote repositories. GitHub is a cloud platform that uses Git as its core technology and acts as the remote repository.*

## 4. What Git command gives information about how to use Git?

- [ ] `git init`
- [ ] `git status`
- [x] **`git help`**

**Answer: `git help`**

*Explanation: The `git help` command provides information about Git commands and how to use them. You can also use `git <command> --help` for specific command help.*


# 1.6 Summary

Congratulations! In this module, you learned the basics of using Git.

## You Learned:

- An overview of Version Control Systems (VCS)
- Important Git terminology
- The differences between Git and GitHub
- How to configure Git
- Some basic Git commands

At this point, you know enough about Git to use version control by yourself on a basic project. Collaboration with other developers is where version control shines. Check out the other modules in this learning path for more about using Git with others!

## Resources

If you'd like to dig deeper, here are more resources:

- Run the `git help tutorial` and `git help tutorial-2` commands
- Visit the Everyday Git site or use the `git help everyday` command
- Review Git and GitHub learning resources
- Watch the Introduction to Git Recap video
- Check out the documentation section of Git's official website


# 2 Introduction to GitHub

Learn to use key GitHub features, including issues, notifications, branches, commits, and pull requests.

# 2.1 Introduction

GitHub provides an AI-powered developer platform to build, scale, and deliver secure software. Whether you're planning new features, fixing bugs, or collaborating on changes, GitHub is where over 100 million developers from across the globe come together to create things and make them even better.

In this module, you'll learn the basics of GitHub and gain a better understanding of its fundamental features with a hands-on exercise all within a GitHub repository.

## Learning Objectives

In this module, you'll:

- Identify the fundamental features of GitHub
- Learn about repository management
- Gain an understanding of the GitHub flow, including branches, commits, and pull requests
- Explore the collaborative features of GitHub by reviewing issues and discussions
- Recognize how to manage your GitHub notifications and subscriptions

## Prerequisites

- A GitHub account


# 2.2 What is GitHub?

In this unit, we review the following learning objectives:

- Brief overview of the GitHub Enterprise Platform
- How to create a repository
- Adding files to a repository
- How to search for repositories
- Introduction to gists and wikis

## GitHub

![](https://learn.microsoft.com/en-us/training/github/introduction-to-github/media/github-enterprise-platform.png)

*A conceptual image of the GitHub Platform with layers from top to bottom: AI, Collaboration, Productivity, Security, and Scale.*

GitHub is a cloud-based platform that uses Git, a distributed version control system, at its core. The GitHub platform simplifies the process of collaborating on projects and provides a website, command-line tools, and overall flow that allows developers and users to work together.

As we learned earlier, GitHub provides an AI powered developer platform to build, scale, and deliver secure software. Let's break down each one of the core pillars of the GitHub Enterprise platform, AI, Collaboration, Productivity, Security, and Scale.

### AI

Generative AI is dramatically transforming software development as we speak. The GitHub Enterprise platform is enhancing collaboration through AI-powered pull requests and issues, productivity through Copilot, and security by automating security checks faster.

### Collaboration

Collaboration is at the core of everything GitHub does. We know inefficient collaboration results in wasted time and money. We counteract that with a suite of seamless tools that allow collaboration to happen effortlessly.

Repositories, Issues, Pull Requests, and other tools help to enable developers, project managers, operation leaders, and others at the same company. It enables them to work faster together, cut down approval times, and ship more quickly.

### Productivity

Productivity is accelerated with automation that the GitHub Enterprise Platform provides. With built-in CI/CD (Continuous Integration and Continuous Delivery) tools directly integrated into the workflow, the platform gives users the ability to set tasks and forget them, taking care of routine administration and speeding up day-to-day work. This gives your developers more time to focus on what matters most, creating innovative solutions.

### Security

GitHub focuses on integrating security directly into the development process from the start. GitHub Enterprise platform includes native, first-party security features that minimize security risk with a built-in security solution. Plus, your code remains private within your organization. At the same time, you're able to take advantage of security overview and Dependabot.

GitHub has continued to make investments to ensure that our features are enterprise-ready. Microsoft and highly regulated industries trust GitHub, and we meet global compliance requirements.

### Scale

GitHub is the largest developer community of its kind with real-time data on over 100M+ developers, 330M+ repositories, and countless deployments. We've been able to understand the shifting needs of developers and make changes to our product to match.

This has translated into an incredible scale that is unmatched and unparalleled by any other company on the planet. Everyday we're gaining more insights from this impressive community and evolving the platform to meet their needs.

In essence, the GitHub Enterprise Platform focuses on the developer experience. It has the scale to provide industry-changing insights, collaboration capabilities for transformative efficiency, the tools for increased productivity, security at every step, and AI to power it all to new heights in a single, integrated platform.

Now let's get into the backbone of GitHub, repositories.

## Introduction to Repositories

Let's first review:

- What is a repository?
- How to create a repository
- Adding files to a repository
- How to search for repositories
- Introduction to gists, wikis, and GitHub pages

### What is a repository?

A repository contains all of your project's files and each file's revision history. It's one of the essential parts that helps you collaborate with people. You can use repositories to manage your work, track changes, store revision history, and work with others. Before we dive too deep, let's first start with how to create a repository.

### How to create a repository

You can create a new repository on your personal account or any organization where you have sufficient permissions.

Let's tackle creating a repository from github.com.

1. In the upper-right corner of any page, use the drop-down menu, and select **New repository**.

![](https://learn.microsoft.com/en-us/training/github/introduction-to-github/media/2-new-repo-option.png)

*A screenshot of the drop-down menu of the plus sign in the top right corner of GitHub.com, with the first option being New repository.*

2. Use the **Owner** drop-down menu to select the account you want to own the repository.

![](https://learn.microsoft.com/en-us/training/github/introduction-to-github/media/2-selecting-repo-owner.png)

*A screenshot of the drop-down menu of who should be the owner of the new repository.*

3. Type a name for your repository, and an optional description.

![](https://learn.microsoft.com/en-us/training/github/introduction-to-github/media/2-repo-name-text-box.png)

*An image of the text box of the repository name highlighted.*

4. Choose a repository visibility.

   - **Public repositories** are accessible to everyone on the internet.
   - **Private repositories** are only accessible to you, people you explicitly share access with, and, for organization repositories, certain organization members.

5. Select **Create repository** and congratulations! You just created a repository!

Next up, let's review how to add files to your repository.

### How to add a file to your repository

Files in GitHub can do a handful of things, but the main purpose of files is to store data and information about your project. It's worth knowing in order to add a file to a repository that you must first have minimum Write access within the repository you want to add a file.

Let's review how to add a file to your repository.

1. On GitHub.com, navigate to the main page of the repository.

2. In your repository, browse to the folder where you want to create a file by selecting the creating a new file link or uploading an existing file.

3. Once added, above the list of files select the **Add file ᐁ** drop-down menu. Then select **Create new file**.

![](https://learn.microsoft.com/en-us/training/github/introduction-to-github/media/add-file-options.png)

*A screenshot of the option to add a file to your new repository highlighted in red with the add file button towards the right of the screen.*

4. In the file name field, type the name and extension for the file. To create subdirectories, type the `/` directory separator.

5. In the file contents text box, type content for the file.

6. To review the new content, above the file contents, select **Preview**.

![](https://learn.microsoft.com/en-us/training/github/introduction-to-github/media/2-preview-option-in-a-file.png)

*Screenshot showing a yml file with the preview button highlighted in the top left.*

7. Select **Commit changes**.

8. In the **Commit message** field, type a short and meaningful commit message that describes the change you made to the file. You can attribute the commit to more than one author in the commit message.

9. If you have more than one email address associated with your account on GitHub.com, select the email address drop-down menu. Then select the email address to use as the Git author email address. Only verified email addresses appear in this drop-down menu. If you enabled email address privacy, then `[username]@users.noreply.github.com` is the default commit author email address.

![](https://learn.microsoft.com/en-us/training/github/introduction-to-github/media/2-commit-description-box.png)
*Screenshot showing a commit change with a description box and the drop-down menu of the email to select as the author of the commit.*

10. Below the Commit message fields, decide whether to add your commit to the current branch or to a new branch. If your current branch is the default branch, you should choose to create a new branch for your commit, and then create a pull request.

![](https://learn.microsoft.com/en-us/training/github/introduction-to-github/media/2-create-a-new-branch.png)

*Screenshot showing creating a new branch from a commit option select with the textbox of the new branch below it.*

11. Select **Commit changes** or **Propose changes**.

Congratulations, you just created a new file in your repository! You have also created a new branch and made a commit.

Before we review branches and commits in the next unit, let's quickly review gists, wikis, and GitHub pages because they're similar to repositories.

## What are gists

Now that we have a good understanding of repositories, we can review gists. Similarly to repositories, gists are a simplified way to share code snippets with others.

Every gist is a Git repository, which you can fork and clone and be made either public or secret. Public gists are displayed publicly where people can browse new ones as they're created. Public gists are also searchable. Conversely, secret gists aren't searchable, but they aren't entirely private. If you send the URL of a secret gist to a friend, they'll be able to see it.

To learn more about gists, see the linked article in our Resources section at the end of this module titled Creating Gists.

## What are wikis?

Every repository on GitHub.com comes equipped with a section for hosting documentation, called a wiki. You can use your repository's wiki to share long-form content about your project, such as how to use it, how you designed it, or its core principles. While a README file quickly tells what your project can do, you can use a wiki to provide additional documentation.

It's worth a reminder that if your repository is private, only people who have at least read access to your repository will have access to your wiki.


# 2.3 Components of the GitHub Flow

In this unit, we're reviewing the following components of the GitHub flow:

- Branches
- Commits
- Pull Requests
- The GitHub Flow

## What are branches

In the last section, we created a new file and a new branch in your repositories.

Branches are an essential part to the GitHub experience because they're where we can make changes without affecting the entire project we're working on.

Your branch is a safe place to experiment with new features or fixes. If you make a mistake, you can revert your changes or push more changes to fix the mistake. Your changes won't update on the default branch until you merge your branch.

> **Note**
> 
> Alternatively, you can create a new branch and check it out by using git in a terminal. The command would be `git checkout -b newBranchName`

## What are commits

In the previous unit, you added a new file into the repository by pushing a commit. Let's briefly review what commits are.

A commit is a change to one or more files on a branch. Every time a commit is created, it's assigned a unique ID and tracked along with the time and contributor. Commits provide a clear audit trail for anyone reviewing the history of a file or linked item, such as an issue or pull request.

*A screenshot of a list of GitHub commits to a main branch.*

Within a git repository, a file can exist in several valid states as it goes through the version control process. The primary states for a file in a Git repository are **Untracked** and **Tracked**.

**Untracked:** An initial state of a file when it isn't yet part of the Git repository. Git is unaware of its existence.

**Tracked:** A tracked file is one that Git is actively monitoring. It can be in one of the following substates:

- **Unmodified:** The file is tracked, but it hasn't been modified since the last commit.
- **Modified:** The file has been changed since the last commit, but these changes aren't yet staged for the next commit.
- **Staged:** The file has been modified, and the changes have been added to the staging area (also known as the index). These changes are ready to be committed.
- **Committed:** The file is in the repository's database. It represents the latest committed version of the file.

These states and substates are important to collaborating with your team to know where each and every commit is in the process of your project. Now let's move on to pull requests.

## What are pull requests?

A pull request is the mechanism used to signal that the commits from one branch are ready to be merged into another branch.

The team member submitting the pull request asks one or more reviewers to verify the code and approve the merge. These reviewers have the opportunity to comment on changes, add their own, or use the pull request itself for further discussion.

Once the changes have been approved (if required), the pull request's source branch (the compare branch) is merged into the base branch.

*A screenshot of a pull request and a comment within the pull request.*

Now that we know of all the ingredients, let's review the GitHub flow.

## The GitHub flow

*Screenshot showing a visual representation of the GitHub Flow in a linear format that includes a new branch, commits, pull request, and merging the changes back to main in that order.*

The GitHub flow can be defined as a lightweight workflow that allows for safe experimentation. You can test new ideas and collaboration with your team by using branching, pull requests, and merging.

Now that we know the basics of GitHub we can walk through the GitHub flow and its components.

### Steps in the GitHub Flow:

1. **Start by creating a branch** so that the changes, features, and fixes you create don't affect the main branch.

2. **Next, make your changes.** We recommend deploying changes to your feature branch before merging into the main branch. Doing so ensures the changes are valid in a production environment.

3. **Now, create a pull request** to ask collaborators for feedback. Pull request review is so valuable that some repositories require an approving review before pull requests can be merged.

4. **Then review and implement your feedback** from your collaborators.

5. **Once you feel great about your changes**, it's time to get your pull request approved and merge it into the main branch.

6. **Finally, you can delete your branch.** Deleting your branch signals your work on the branch is complete and prevents you or others from accidentally using old branches.

That's it, you've been through a GitHub flow cycle!

Let's move onto the next section where we'll cover the differences between issues and discussions.

# 2.4 GitHub is a Collaborative Platform

Collaboration is at the core of everything GitHub does. We went over repositories in the first unit of the module and learned that repositories help you organize your project and its files. In the last unit, we learned about pull requests, which is a way to keep track of changes made to your project.

In this unit, we're learning about issues and discussions. These are two other pieces that contribute to the collaborative nature of the GitHub Enterprise Platform.

## Issues

GitHub Issues were created to track ideas, feedback, tasks, or bugs for work on GitHub. Issues can be created in various ways, so you can choose the most convenient method for your workflow.

For this walkthrough, we'll go over how to create an issue from a repository. But issues can also be created from:

- An item in a task list
- A note in a project
- A comment in an issue or pull request
- A specific line of code
- A URL query

### Creating an issue from a repository

1. On GitHub.com, navigate to the main page of the repository.

2. Under your repository name, select **Issues**.

*Screenshot showing the top portion of the main page of a repository with the Issues section highlighted.*

3. Select **New issue**.

4. If your repository uses issue templates, next to the type of issue you'd like to open select **Get started**.

   If the type of issue you'd like to open isn't included in the available options, select **Open a blank issue**. If not using templates, skip to Step 5.

*A screenshot of the issue templates menu, with the Open a blank issue option highlighted.*

5. In the **Add a title** field, enter a title for your issue.

6. In the **Add a description** field, type a description of your issue.

7. If you're a project maintainer, you can assign the issue to someone, add it to a project board, associate it with a milestone, or apply a label.

8. When you're finished, select **Submit new issue**.

Some conversations are more suitable for GitHub Discussions. You can use GitHub Discussions to ask and answer questions, share information, make announcements, and conduct or participate in conversations about a project.

In the next section, we'll review Discussions and how to best utilize the feature.

## Discussions

Discussions are for conversations that need to be accessible to everyone and aren't related to code. Discussions enable fluid, open conversation in a public forum.

In this section we go over:

- Enabling a discussion in your repository
- Creating a new discussion and various discussion categories

Let's dive into enabling a discussion in your repository.

### Enabling a discussion in your repository

Repository owners and people with Write access can enable GitHub Discussions for a community on their public and private repositories. The visibility of a discussion is inherited from the repository the discussion is created in.

When you first enable GitHub Discussions, you're invited to configure a welcome post.

1. On GitHub.com, navigate to the main page of the repository.

2. Under your repository name, select **Settings**.

*A screenshot of the top portion of the main page of a repository with the Settings section highlighted.*

3. Scroll down to the **Features** section and under **Discussions**, select **Setup discussions**.

*A screenshot of the Discussions box with the green Setup discussion button highlighted.*

4. Under **Start a new discussion**, edit the template to align with the resources and tone you want to set for your community.

5. Select **Start discussion**.

You're now ready to create a new discussion.

### Create a new discussion

Any authenticated user who can view the repository can create a discussion in that repository. Similarly, since organization discussions are based on a source repository, any authenticated user who can view the source repository can create a discussion in that organization.

1. On GitHub.com, navigate to the main page of the repository or organization where you want to start a discussion.

2. Under your repository or organization name, select **Discussions**.

*A screenshot of the top portion of the main page of a repository with the Discussions section highlighted.*

3. On the right side of the page, select **New discussion**.

4. Select a discussion category by selecting **Get started**. All discussions must be created in a category. For repository discussions, people with maintain or admin permissions to the repository define the categories for discussions in that repository.

*A screenshot of the select a discussion category menu selection, with the top option Announcements and the get started button highlighted.*

Each category must have a unique name, emoji pairing, and a detailed description stating its purpose. Categories help maintainers organize how conversations are filed. They're customizable to help distinguish categories that are Q&A or more open-ended conversations. The following table shows the default categories for discussions and their purpose.

| **Category** | **Purpose** | **Format** |
|--------------|-------------|------------|
| 📣 Announcements | Updates and news from project maintainers | Announcement |
| #️⃣ General | Anything and everything relevant to the project | Open-ended discussion |
| 💡 Ideas | Ideas to change or improve the project | Open-ended discussion |
| 🗳️ Polls | Polls with multiple options for the community to vote for and discuss | Polls |
| 🙏 Q&A | Questions for the community to answer, with a question/answer format | Question and Answer |
| 🙌 Show and tell | Creations, experiments, or tests relevant to the project | Open-ended discussion |

5. Under **Discussion title** enter a title for your discussion, and under **Write** enter the body of your discussion.

*A screenshot of starting a new discussion page with the Discussion title box and content box empty.*

6. Select **Start discussion**.

That covers a little about how GitHub inspires collaboration. Now let's move to how you can manage notifications, subscribe to threads, and get started with GitHub pages.


# 2.5 GitHub Platform Management

Now that you know the basics of the GitHub platform, let's go over some platform management.

In this unit, we'll cover:

- Managing notifications and subscriptions
- Subscribing to threads and finding threads where you're mentioned
- Publicizing your project or organization on GitHub pages

## Managing Notifications and Subscriptions

You can choose to receive ongoing updates about specific activity on GitHub.com through a subscription. Notifications are the updates that you receive for specific activity to which you're subscribed.

### Subscription Options

You can choose to subscribe to notifications for:

- A conversation in a specific issue, pull request, or gist
- CI activity, such as the status of workflows in repositories set up with GitHub Actions
- Repository issues, pull requests, releases, security alerts, or discussions (if enabled)
- All activity in a repository

In some instances, you're automatically subscribed to conversations on GitHub. Examples include opening a pull request or issue, commenting on a thread, or being assigned to an issue or pull request.

If you're no longer interested in a conversation, you can unsubscribe, unwatch, or customize the types of notifications you'll receive in the future.

If you're ever interested in issues that mention a certain user, you can use *mentions:* as the qualifier to find those specific issues.

## What are GitHub Pages?

To round out our journey of GitHub, let's tackle GitHub pages. You can use GitHub Pages to publicize and host a website about yourself, your organization, or your project directly from a repository on GitHub.com.

GitHub Pages is a static site-hosting service that takes HTML, CSS, and JavaScript files straight from a repository on GitHub. Optionally, you can run the files through a build process and publish a website. Edit and push your changes, and your project is live for the public in a visually organized way.

## Next Steps

Next up, we'll walk through an exercise to get you started with GitHub. In the next exercise, you'll:

- Create a new repository
- Create a new branch
- Commit a file
- Open a pull request
- And merge a pull request


# 2.6 Exercise - A Guided Tour of GitHub

This exercise checks your knowledge of GitHub key features, including committing a branch, committing a file, opening a pull request, and merging a pull request.

## Getting Started

When you select the **Start the exercise on GitHub** button below, you'll be navigated to a public GitHub template repository that prompts you to complete a series of small challenges.

When you've finished the exercise in GitHub, return here for:

- A quick knowledge check
- A summary of what you've learned
- A badge for completing this module

> **Note**
> 
> You don't need to modify any of the workflow files to complete this exercise. **Altering the contents in this workflow can break the exercise's ability to validate your actions, provide feedback, or grade the results**.

https://github.com/skills/introduction-to-github


# 2.7 Summary

In this module, you:

- Identified the fundamental features of GitHub
- Learned about repository management
- Gained an understanding of the GitHub flow including branches, commits, and pull requests
- Explored the collaborative features of GitHub by reviewing issues and discussions
- Recognized how to manage your GitHub notifications and subscriptions

Now that you're familiar with the basics of GitHub, learn to Upload your project by using GitHub best practices.

## Learn More

Here are some links to more information on the topics we discussed in this module:

- Set up Git
- Repositories documentation
- Creating gists
- About wikis
- About branches
- About commits
- About pull requests
- About issues
- Quickstart for GitHub Discussions
- Configuring notifications
- GitHub Pages documentation


# 3 Introduction to GitHub's products

This module provides an overview of GitHub products, including the account types, plan options, associated features, and billing. It also covers how to access GitHub on-the-go using GitHub Desktop and GitHub Mobile.

# 3.1 Introduction

Whether you're just learning to code, working as a developer at a start-up, or a C-level executive at a Fortune 500 company, the GitHub platform can help you build, scale, and deliver secure software.

Depending on your specific situation, it's important to know what GitHub plans fit your needs.

In this module, you learn about the many different types of GitHub accounts, plans, and their associated features. You also discover how other features are licensed.

## Learning objectives

After completing this module, you're able to:

- **Define the difference** between the different types of GitHub accounts: Personal, Organization, and Enterprise
- **Explain each GitHub plan**: GitHub Free for personal accounts and organizations, GitHub Pro for personal accounts, GitHub Team, and GitHub Enterprise
- **Distinguish the features** associated with accessing GitHub on GitHub Mobile and GitHub Desktop
- **Describe a brief overview** of GitHub billing and payments


# 3.2 GitHub accounts and plans

In this unit, you learn about GitHub account types and plans.

## GitHub account types

It's important to understand that there's a difference between the types of GitHub accounts and the GitHub plans. Here are the three types of GitHub accounts:

- **Personal**
- **Organization** 
- **Enterprise**

Let's review each of these account types in detail.

### Personal accounts

Every person who uses GitHub.com signs into a personal account (sometimes referred to as a user account). Your personal/user account is your identity on GitHub.com and has a username and profile.

Your personal/user account can own resources such as repositories, packages, and projects and has a straightforward way to manage your permission. Actions that you take on GitHub.com, such as creating an issue or reviewing a pull request, are attributed to your personal account.

Each personal account uses either GitHub Free or GitHub Pro. All personal accounts can own an unlimited number of public and private repositories, with an unlimited number of collaborators on those repositories. If you use GitHub Free, private repositories owned by your personal account have a limited feature set.

### Organization accounts

Organization accounts are shared accounts where an unlimited number of people can collaborate across many projects at once. Unlike personal/user accounts, permissions with organization accounts are done with a tiered approach.

Similar to personal accounts, organizations can own resources such as repositories, packages, and projects. However, you can't sign into an organization. Instead, each person signs into their own personal account, and any actions the person takes on organization resources are attributed to their personal account. Each personal account can be a member of multiple organizations.

The personal accounts within an organization can be given different roles in the organization to grant different levels of access to the organization and its data. All members can collaborate with each other in repositories and projects. But only organization owners and security managers can manage the settings for the organization and control access to the organization's data with sophisticated security and administrative features.

### Enterprise accounts

Enterprise accounts on GitHub.com allow administrators to centrally manage policies and billing for multiple organizations and enable inner sourcing between their organizations. An enterprise account must have a handle, like an organization or user account on GitHub.

Organizations are shared accounts for enterprise members to collaborate across many projects at once. In the enterprise settings, enterprise owners can invite existing organizations to join your enterprise account, transfer organizations between enterprise accounts, or create new organizations.

Your enterprise account allows you to manage and enforce policies for all the organizations owned by the enterprise. Each enterprise policy controls the options available for a policy at the organization level.

## GitHub plans

Now that you have a better understanding of the different types of accounts you can have with GitHub, let's look at the different plans available to improve your software management process and team collaboration.

There are several free GitHub products, in addition to the paid ones:

- **GitHub Free** for personal accounts and organizations
- **GitHub Pro** for personal accounts
- **GitHub Team**
- **GitHub Enterprise**

### GitHub Free

GitHub Free provides the basics for individuals and organizations. Anyone can sign up for the free version of GitHub.

#### GitHub Free for personal accounts

Signing up for GitHub Free gives a new user a personal user account. A personal user account includes unlimited public and private repositories and unlimited collaborators.

With GitHub Free, a personal account includes:

- GitHub Community Support
- Dependabot alerts
- Two-factor authentication enforcement
- 500-MB GitHub Packages storage
- 120 GitHub Codespaces core hours per month
- 15-GB GitHub Codespaces storage per month
- **GitHub Actions:**
  - 2,000 minutes per month
  - Deployment protection rules for public repositories

#### GitHub Free for organizations

With GitHub Free for organizations, you can work with unlimited collaborators on unlimited public repositories, with a full feature set. Or, unlimited private repositories with a limited feature set.

In addition to the features available with GitHub Free for personal accounts, GitHub Free for organizations includes:

- Team access controls for managing groups

### GitHub Pro

GitHub Pro is similar to GitHub Free but comes with upgraded features. The plan is designed for individual developers (using their personal account) who want advanced tools and insight within their repositories but don't belong to a team.

GitHub Pro accounts include all of the features of a GitHub Free account, plus the following advanced features:

- GitHub Support via email
- 3,000 GitHub Actions minutes per month
- 2-GB GitHub Packages storage
- 180 GitHub Codespaces core hours per month
- 20-GB GitHub Codespaces storage per month
- **Advanced tools and insights in private repositories:**
  - Required pull request reviewers
  - Multiple pull request reviewers
  - Protected branches
  - Code owners
  - Autolinked references
  - GitHub Pages
  - Wikis
  - Repository insight graphs for pulse, contributors, traffic, commits, code frequency, network, and forks

### GitHub Team

GitHub Team is the version of GitHub Pro for organizations. GitHub Team is better than GitHub Free for organizations because it provides increased GitHub Actions minutes and extra GitHub Packages storage.

Let's go over the extra features in GitHub Team that help with team collaboration:

- GitHub Support via email
- 3,000 GitHub Actions minutes per month
- 2-GB GitHub Packages storage
- **Advanced tools and insights in private repositories:**
  - Required pull request reviewers
  - Multiple pull request reviewers
  - Draft pull requests
  - Team pull request reviewers
  - Protected branches
  - Code owners
  - Scheduled reminders
  - GitHub Pages
  - Wikis
  - Repository insight graphs for pulse, contributors, traffic, commits, code frequency, network, and forks
- The option to enable or disable GitHub Codespaces

### GitHub Enterprise

GitHub Enterprise accounts enjoy a greater level of support and extra security, compliance, and deployment controls.

You can create one or more enterprise accounts by signing up for the paid GitHub Enterprise product. When you create an enterprise account, you're assigned the role of enterprise owner. As an enterprise owner, you can add and remove organizations to and from the enterprise account. You can manage other administrators, enforce security policies across organizations, and so on.

In addition to the features available with GitHub Team, GitHub Enterprise includes:

- GitHub Enterprise Support
- More security, compliance, and deployment controls
- Authentication with security assertion markup language (SAML) single sign-on
- Access provisioning with SAML or System for Cross-domain Identity Management (SCIM)
- Deployment protection rules with GitHub Actions for private or internal repositories
- GitHub Connect
- The option to purchase GitHub Advanced Security

#### GitHub Enterprise options

There are two different GitHub Enterprise options:

- **GitHub Enterprise Server**
- **GitHub Enterprise Cloud**

The significant difference between GitHub Enterprise Server (GHES) and GitHub Enterprise Cloud is that GHES is a self-hosted solution that allows organizations to have full control over their infrastructure.

The other difference between GHES and GitHub Enterprise Cloud is that GitHub Enterprise Cloud includes a dramatic increase in both GitHub Actions minutes and GitHub Packages storage.

Here are the extra features of GitHub Enterprise Cloud:

- 50,000 GitHub Actions minutes per month
- 50-GB GitHub Packages storage
- A service level agreement for 99.9% monthly uptime
- Option to centrally manage policy and billing for multiple GitHub.com organizations with an enterprise account
- Option to provision and manage the user accounts for your developers, by using Enterprise Managed Users



# 3.3 GitHub Mobile and GitHub Desktop

There are multiple ways to access your GitHub account aside from github.com. GitHub Mobile and GitHub Desktop allow you to have a seamless experience while accessing your account on the go.

Let's briefly review GitHub Desktop and GitHub Mobile and their features.

## GitHub Mobile

GitHub Mobile gives you a way to do high-impact work on GitHub quickly and from anywhere. GitHub Mobile is a safe and secure way to access your GitHub data through a trusted, first-party client application.

### With GitHub Mobile you can:

- **Manage, triage, and clear notifications** from github.com
- **Read, review, and collaborate** on issues and pull requests
- **Edit files** in pull requests
- **Search for, browse, and interact** with users, repositories, and organizations
- **Receive a push notification** when someone mentions your username
- **Schedule your push notifications** for specific custom hours
- **Secure your GitHub.com account** with two-factor authentication
- **Verify your sign in attempts** on unrecognized devices

## GitHub Desktop

GitHub Desktop is an open-source, stand-alone software application that enables you to be more productive. It facilitates collaboration between you and your team and the sharing of Git and GitHub best practices within your team.

### Here are a few of the many things you can do with GitHub Desktop:

- **Add and clone repositories**
- **Add changes to your commit interactively**
- **Quickly add coauthors** to your commit
- **Check out branches** with pull requests and view CI statuses
- **Compare changed images**



# 3.4 GitHub billing

Now let's review billing and payments for your GitHub account.

## Overview

GitHub bills separately for each account. You receive a separate bill for your personal account and for each organization or enterprise account you own.

The bill for each account is a combination of charges for your **subscriptions** and **usage-based billing**.

### Subscriptions
Include your account's plan, such as GitHub Pro or GitHub Team, and paid products that have a consistent monthly cost, such as GitHub Copilot and apps from GitHub Marketplace.

### Usage-based billing
Applies when the cost of a paid product depends on how much you use the product. For example, the cost of GitHub Actions depends on how many minutes your jobs spend running and how much storage your artifacts use.

> **📝 Note**
> 
> Your plan might come with included amounts of usage-based products. For example, with GitHub Pro, your personal account gets 3,000 minutes of GitHub Actions usage for free each month. You can control usage beyond the included amounts by setting spending limits.

Understanding GitHub's billing structures is crucial for effective administration and cost management. This document focuses on differentiating how GitHub products are billed, including seat licenses, GitHub Actions, GitHub Packages, and the new billing platform's capabilities.

## Pricing for GitHub Actions

GitHub Actions enables automation of workflows directly within repositories. Its pricing model varies based on repository visibility and account type:

### Public Repositories
Usage of GitHub Actions is **free** for public repositories, providing unlimited minutes on GitHub-hosted runners.

### Private Repositories
Each account receives a certain amount of free minutes and storage for GitHub-hosted runners, depending on the account's plan. For example, GitHub Free for personal accounts includes 2,000 CI/CD minutes per month. Usage beyond the included amounts is controlled by spending limits.

It's important to monitor usage to avoid unexpected costs, especially for private repositories with high activity.

## Pricing and Support Options for Organizations

GitHub offers various plans tailored to organizational needs, each with distinct features and support options:

### GitHub Free for Organizations
**Features:**
- Unlimited public/private repositories
- Community support
- 2,000 CI/CD minutes per month

### GitHub Team
**Features:**
- Everything in Free, plus:
- Additional collaboration tools
- Code owners
- Required reviews
- Enforced branch protections
- Email support

### GitHub Enterprise
**Features:**
- Everything in Team, plus:
- SAML single sign-on
- Advanced auditing
- GitHub Connect
- 24/7 support
- Enterprise-level security features

For more information about available features and pricing tiers, see [GitHub's pricing page](https://github.com/pricing).

Organizations should evaluate their collaboration needs and security priorities to choose the plan that best fits their goals.

## Usage-Based Billing for Licenses (Metered Billing)

With the enhanced billing platform, GitHub has introduced a usage-based billing model for licenses:

### Monthly Billing
Organizations are billed monthly for the exact number of GitHub Enterprise and GitHub Advanced Security licenses used.

### Pro Rata Charges
If a user starts consuming a license partway through the month, the organization is charged a pro rata amount for that user's usage.

### Dynamic Adjustments
If a user stops consuming a license during the month, the billing for the following month reflects this change, ensuring organizations only pay for active users.

This model eliminates the need to purchase a predefined number of licenses in advance, offering flexibility and cost efficiency.

## Billing Platform's New Capabilities

GitHub's enhanced billing platform provides improved tools for financial management:

### Granular Spending Controls
Administrators can set specific spending limits for services like GitHub Actions and GitHub Packages, preventing unexpected overages.

### Detailed Usage Insights
The platform offers in-depth visibility into product usage, allowing organizations to monitor consumption patterns and optimize resource allocation.

### Automated Reporting
Features for automating usage reporting streamline financial oversight and facilitate internal chargebacks.

These capabilities enhance an organization's ability to manage expenses effectively and align GitHub usage with budgetary constraints.


# 3.5 License Usage Stats

In this unit, you'll learn how to track and manage GitHub Enterprise license usage across organizations, enterprise accounts, and server instances using the admin console, APIs, and best practices for optimizing license allocation and cost.

As a **GitHub Enterprise administrator**, tracking **license usage** is crucial for managing costs, optimizing resources, and ensuring compliance. GitHub provides various methods for obtaining license statistics at **organization, enterprise, and instance levels**.

## Finding License Usage for a Specific Organization

To find **license usage statistics** for a single **GitHub organization**:

### Method 1: Using GitHub Enterprise Cloud (GHEC) Admin Console

1. Navigate to **GitHub Enterprise Cloud Admin Panel**
2. Go to **Settings > Billing & plans**
3. Locate the **License usage** section
4. View details such as:
   - **Total seats assigned**
   - **Active seats in use**
   - **Available licenses**
   - **Pending invitations**

### Command-Line Alternative (GraphQL API)

For more granular data, admins can use **GraphQL API**:

```json
{
  organization(login: "org-name") {
    billingInfo {
      totalSeats
      seatsUsed
      seatsAvailable
    }
  }
}
```

## Method 2: Finding License Usage Across Multiple Organizations

For organizations under the same **enterprise account**, admins can analyze usage across all organizations.

### Using the Enterprise Account Billing Page

1. Navigate to **GitHub Enterprise Cloud > Enterprise settings**
2. Go to **Billing** > **License Usage**
3. Review license usage for **each organization under the enterprise account**

### GraphQL API Query for All Organizations

To fetch usage data for all organizations in an enterprise:

```json
{
  enterprise(slug: "enterprise-name") {
    organizations(first: 50) {
      nodes {
        name
        billingInfo {
          totalSeats
          seatsUsed
          seatsAvailable
        }
      }
    }
  }
}
```

## Method 3: Finding License Usage for Enterprise Accounts

For enterprises using **GitHub Enterprise Cloud or GitHub Enterprise Server**, admins can track licenses at the **enterprise level**.

### GitHub Enterprise Server (GHES) Dashboard

Next, you'll dive into how to gain access to view track these licenses.

1. Log in to the **GitHub Enterprise Server Admin Console**
2. Go to **Settings > License Usage**
3. View:
   - **Total allocated licenses**
   - **Active users**
   - **Available seats**
   - **Historical license usage trends**

### REST API Alternative

For **programmatic access**, use the REST API:

```bash
curl -H "Authorization: token YOUR-TOKEN" \
"https://api.github.com/enterprises/YOUR-ENTERPRISE/license"
```

## Method 4: Finding License Usage Across Multiple GitHub Instances

For **large enterprises** with multiple GitHub Enterprise **Server instances**, admins must track **license consumption** across deployments.

### GitHub Enterprise Metrics API

1. Access **GitHub Enterprise Server** admin settings
2. Use the **Metrics API**:

```bash
curl -H "Authorization: token YOUR-TOKEN" \
"https://api.github.com/enterprise/settings/licenses"
```

3. Extract:
   - **Total enterprise-wide licenses**
   - **Usage per GitHub instance**
   - **Available capacity per region**

## Best Practices for License Usage Management

The following strategies can help you manage licenses more efficiently across your organization:

- **Automate Monitoring**: Use **GraphQL/REST API queries** to **track usage trends**
- **Optimize Unused Seats**: Identify **inactive users** and **reclaim unused licenses**
- **Enable Usage-Based Billing**: Ensure **billing reflects actual consumption**
- **Regular Audits**: Conduct **monthly/quarterly** **license reviews** to optimize cost



# 3.6 License Usage Stats in Machine and Peripheral Devices


In this unit, you'll learn how machine accounts and peripheral services impact GitHub Enterprise license usage. You'll explore methods to track their consumption, identify inefficiencies, and apply best practices to improve cost control and security.

Tracking license usage is essential for cost optimization and security compliance. Machine accounts (used for automation) and peripheral services (such as CI/CD, integrations, and API consumers) can consume licenses, impacting enterprise costs and resource management.

## Understanding Machine Accounts and Peripheral Services

### Machine Accounts

Machine accounts are GitHub accounts used for automation, running scripts, or integrating with third-party tools.

Characteristics: - They act independently of human users. - Often used by CI/CD tools (e.g., GitHub Actions, Jenkins, CircleCI). - Each machine account consumes a GitHub license, like a standard user.

### Peripheral Services

Peripheral Services are external integrations that interact with GitHub via API requests.

Examples: - CI/CD Pipelines (e.g., GitHub Actions, GitHub Runners, Jenkins). - Security Scanning Tools (e.g., Dependabot, Snyk, CodeQL). - Third-party Integrations (e.g., Slack, Jira, Datadog). - Self-hosted GitHub Runners.

### Why Track These?

To identify unused or excessive licenses.
To optimize costs and prevent unnecessary spending.
To monitor security risks from inactive or misconfigured automation accounts.

## Finding License Usage Statistics for Machine Accounts

### Method 1: GitHub Enterprise Admin Console

Navigate to Enterprise Settings.
Select Billing & License Management.
Look for a Machine Accounts section (if available).
Identify:
Number of active machine accounts.
License consumption per machine account.
Last active date.

### Method 2: GraphQL API Query for Machine Accounts

To retrieve machine account usage statistics, use the GraphQL API:

JSON

Copy
```
{
  enterprise(slug: "enterprise-name") {
    organizations(first: 50) {
      nodes {
        name
        machineAccounts {
          totalCount
          nodes {
            login
            createdAt
            lastActiveAt
          }
        }
      }
    }
  }
}
```

Why Track These?

To identify inactive machine accounts.
To track when each machine account was last active.
To help reduce unnecessary license allocation.

## Finding License Usage for Peripheral Services

### Method 1: GitHub Actions & Runners Usage Metrics

Go to Enterprise Settings** → Actions.
View:
Total GitHub-hosted runner minutes used.
Self-hosted runner usage.
Billing for extra runner minutes.

### Method 2: REST API for Self-Hosted Runners

To track self-hosted runners and their license usage:

Bash

Copy
```
curl -H "Authorization: token YOUR-TOKEN" \
"https://api.github.com/enterprises/YOUR-ENTERPRISE/actions/runners"
```

Key Insights:

Identifies how many runners are consuming licenses.
Tracks idle runners that may be wasting resources.
Helps optimize billing for GitHub-hosted runner minutes.

### Method 3: Peripheral Services API Usage Tracking

Monitor API-based integrations using:

Bash

Copy
```
curl -H "Authorization: token YOUR-TOKEN" \
"https://api.github.com/enterprises/YOUR-ENTERPRISE/audit-log"
```

This helps you:

Detect Inactive Services: Find services no longer in use.
Audit Third-Party Tools: Ensure external tools are necessary and properly configured.
Reduce Costs: Disable services that are not providing value."

## 4. Best Practices for Managing Machine Accounts & Peripheral Services Licenses

The following best practices will help you audit usage, enforce policies, and streamline your automation footprint:

Audit Machine Accounts Regularly: Identify and deactivate unused machine accounts.
Over time, organizations accumulate unused or stale machine accounts that may still have access to repositories and systems.
Unused accounts increase security risks, as they can be exploited if compromised.
Regular audits ensure that only active and necessary machine accounts exist, reducing exposure to unauthorized access.

Monitor API Usage: Track third-party tools consuming enterprise licenses.
Many third-party applications, CI/CD pipelines, and integrations consume GitHub API resources and enterprise licenses.
Excessive API calls can lead to rate limits, affecting developers' workflows.
Unauthorized or unknown API usage can expose sensitive data and security vulnerabilities.

Optimize Runner Usage: Identify idle self-hosted runners and reduce GitHub-hosted runner costs.
Self-hosted and GitHub-hosted runners execute CI/CD workflows. Inefficient use leads to unnecessary costs.
Idle self-hosted runners waste computing resources and may expose organizations to security risks if left unmonitored.
GitHub-hosted runners operate on a pay-as-you-go basis, and optimizing usage can significantly reduce costs.

Restrict Machine Accounts: Limit their permissions and enforce security policies.
Machine accounts should not have unnecessary access to repositories, reducing the risk of privilege escalation.
If compromised, machine accounts can be exploited to manipulate source code, deploy malicious changes, or expose secrets.
Enforcing security policies helps ensure compliance and minimizes potential breaches.

Tracking license usage for machine accounts and peripheral services is crucial for cost optimization, security, and compliance in GitHub Enterprise. Admins should leverage GitHub UI, GraphQL, and REST APIs to identify inactive accounts, optimize usage, and prevent unnecessary spending.



# 3.7 Metered Usage Reports

In this unit, you'll learn how to monitor and manage billing for GitHub's metered products, including Actions minutes, storage, licenses, and advanced features like Copilot and GHAS.

GitHub provides detailed billing and consumption reports to track the usage of metered products. These reports help administrators monitor costs, allocate resources efficiently, and ensure compliance with organizational policies.

## GitHub Actions Minutes

GitHub Actions is a CI/CD automation tool where workflows run on virtual machines. The minutes consumed in these workflows are metered based on repository type, runner type, and usage.

### Tracking Consumption

Navigate to Settings → Billing in your GitHub organization or account.
Under the GitHub Actions section, you can see the number of minutes used.
Usage is broken down by repository, runner type (Linux, macOS, Windows), and remaining quota.

### Billing Details

Free Allocation:
Public repositories get unlimited free minutes.
Private repositories receive free minutes based on the plan:
GitHub Free: 2,000 minutes/month
GitHub Pro: 3,000 minutes/month
GitHub Team: 3,000 minutes/month
GitHub Enterprise: 50,000 minutes/month

Pricing per Runner Type (as of 2024):
Linux: $0.008 per minute
Windows: $0.016 per minute
macOS: $0.08 per minute

### Optimization Strategies

Use self-hosted runners for high-volume workflows to reduce costs.
Optimize workflow scripts by caching dependencies and reducing redundant jobs.
Limit workflows to only trigger when necessary (e.g., push to main branch only).

## Storage for GitHub Packages

GitHub Packages allows storing artifacts, container images, and dependencies. Storage is metered based on the volume of stored data and data transfer usage.

### Tracking Consumption

Navigate to Settings → Billing → GitHub Packages to view storage usage.
Breakdown includes storage (GB) and data transfer (GB) used per repository.

### Billing Details

Free Allocation:
Public repositories: Free storage and bandwidth.
Private repositories:
Storage up to 2GB
Data transfer up to 1GB per month

For details on storage limits and usage beyond the free allocation, see GitHub's pricing page.

### Optimization Strategies

Regularly delete unused packages or enable retention policies.
Store frequently accessed images in a centralized registry to reduce duplication.
Use compressed formats to reduce storage consumption.

## GitHub Enterprise (GHE) Licenses

GitHub Enterprise provides advanced features for organizations, and the number of active users determines license consumption.

### Tracking Consumption

Go to Enterprise Settings → Billing to view license usage reports.
Monitor active users vs. allocated licenses.

### Billing Details

Pricing Model:
Each user with access to private repositories consumes one license.
Organizations pay per user annually or monthly.

Inactive Users:
If an admin removes a user, the license remains assigned for the billing period but can be reallocated.

### Optimization Strategies

Audit inactive users and revoke access to free up licenses.
Use SSO and SCIM provisioning to automate user management.

## GitHub Advanced Security (GHAS) Licenses

GitHub Advanced Security (GHAS) offers code scanning, secret scanning, and dependency review for enhanced security.

### Tracking Consumption

View reports in Settings → Billing → GHAS Usage to see active committers.
The report shows unique committers per billing period.

### Billing Details

Pricing Model:
Charged per unique committer per month.
If a committer contributes to multiple repositories, they only count once.
Free Tier: Not available (only for public repositories).

### Optimization Strategies

Restrict GHAS to repositories that truly need advanced security.
Use branch protections to limit unnecessary scans on feature branches.

## GitHub Copilot

GitHub Copilot provides AI-driven code completion and suggestions, billed per user.

### Tracking Consumption

Admins can track Copilot usage under Billing → Copilot in organization settings.
The report shows active users and monthly billing estimates.

### Billing Details

Access Model:
Available for individuals and businesses with different subscription options.

Free Access:
Free for students and verified open-source maintainers.
Free for select enterprise customers (trial-based).

For current Copilot plans and subscription details, see GitHub Copilot pricing.

### Optimization Strategies

Regularly review and deactivate Copilot for users who don't need it.
Encourage developers to disable Copilot in projects where AI-generated code is unnecessary.

## Large File Storage (LFS)

GitHub LFS is used for storing large binary files separately from Git repositories.

### Tracking Consumption

View LFS usage in Billing → LFS Usage.
Report includes storage (GB) and bandwidth usage (GB).

### Billing Details

Free Tier:
1GB of storage per repository
1GB of bandwidth per month

For more information on Git Large File Storage (LFS) usage and limits, see GitHub's LFS documentation.

### Optimization Strategies

Use external storage services (e.g., AWS S3, Azure Blob Storage) for large files.
Delete unused large files to optimize storage.
Enable Git LFS file pruning to remove unreferenced objects


# 3.8 Module assessment

## Check your knowledge

### 1. What's the difference between GitHub organization accounts and GitHub personal/user accounts?

- [x] **Organizational accounts are shared accounts, while personal/user accounts are for individuals.** ✅
- [ ] You pay more for organization accounts versus personal/user accounts.
- [ ] They're exactly the same.
- [ ] Personal/user accounts have more access than organization accounts.

**Explanation:** Organization accounts are shared accounts where an unlimited number of people can collaborate across many projects at once, while personal/user accounts are individual accounts that serve as your identity on GitHub.

### 2. What's the best reason to decide to upgrade to the GitHub Enterprise product?

- [ ] Because you want to use GitHub Actions and Codespaces.
- [ ] Because your VP needs to use GitHub Insights.
- [x] **Because you want to centrally manage users and repositories across multiple organizations.** ✅
- [ ] Because you want to use the team pull request reviewers feature.

**Explanation:** GitHub Enterprise accounts allow administrators to centrally manage policies and billing for multiple organizations and enable inner sourcing between their organizations. This is the primary advantage of Enterprise over other plans.

### 3. What's the purpose of a team?

- [ ] A team allows you to manage an organization account.
- [ ] A team allows you to control permission levels for an enterprise.
- [ ] A team allows a single user to sign in using different accounts credentials.
- [x] **A team is intended to reflect a company or group's structure. It's used to provide cascading access permissions and make it easy to notify all team members via mentions.** ✅

**Explanation:** Teams are designed to reflect organizational structure and provide a way to manage permissions and communicate with groups of people efficiently.

### 4. What's a function you can execute on GitHub Mobile?

- [ ] Check out branches with pull requests and view CI statuses.
- [ ] Compare changed images.
- [ ] Add and clone repositories.
- [x] **Manage, triage, and clear notifications from github.com.** ✅

**Explanation:** GitHub Mobile allows you to manage, triage, and clear notifications from github.com. The other options (checking out branches, comparing images, and adding/cloning repositories) are GitHub Desktop features.

### 5. Which of these features is unique to GitHub Enterprise Cloud (GHEC)?

- [ ] Requires on-premises deployment and infrastructure management
- [x] **Provides centralized user management with identity provider integration** ✅
- [ ] Must be installed and maintained by the organization's IT team
- [ ] Operates entirely within a private cloud environment

**Explanation:** GitHub Enterprise Cloud provides centralized user management with identity provider integration through features like SAML SSO and SCIM provisioning. The other options describe GitHub Enterprise Server (GHES), not GHEC.

### 6. What actions can you take at enterprise level to manage the use of GitHub Actions in your enterprise instance?

- [ ] Create workflow templates
- [x] **Configure a GitHub Actions use policy** ✅
- [ ] Manually sync public actions in Enterprise Cloud

**Explanation:** At the enterprise level, administrators can configure GitHub Actions use policies to control how Actions are used across the enterprise.

### 7. What actions can you take to configure self-hosted runners for your enterprise use?

- [x] **Create and add custom labels to your runners** ✅
- [ ] Add proxy configurations to your runners after they start.
- [ ] Add the IP address or IP address range of your runners at repository level.

**Explanation:** You can create and add custom labels to self-hosted runners to help organize and target specific runners for workflows.

### 8. What are encrypted secrets?

- [ ] Encrypted secrets are authentication tokens you can generate in your account settings.
- [ ] Encrypted secrets are the equivalent of SSH keys in GitHub.
- [x] **Encrypted secrets are encrypted environment variables you can create to store sensitive information.** ✅

**Explanation:** Encrypted secrets are encrypted environment variables that allow you to store sensitive information (like API keys, passwords, etc.) securely in your repository or organization settings for use in GitHub Actions workflows.



# 3.9 Summary

In this module, you learned:
* The different types of GitHub accounts: Personal, Organization, and Enterprise.
* The GitHub plans: GitHub Free for personal accounts and organizations, GitHub Pro for personal accounts, GitHub Team, and GitHub Enterprise.
* The features associated with accessing GitHub on GitHub Mobile and GitHub Desktop.
* A brief overview of GitHub billing and payments.

Your understanding of GitHub's product platform, accounts, plans, how to access GitHub, and the different billing options helps you to optimize its usage within your organization.

**Further reading**
* GitHub's plans
* GitHub's billing and payments
* Managing your license for GitHub Enterprise


# 4 Configure code scanning on GitHub

This module introduces you to code scanning and its features. You'll learn how to implement code scanning using CodeQL, third party tools, and GitHub Actions.

# 4.1 Introduction

Imagine that you're the GitHub administrator for a project, and you want to make sure that the code doesn't include any security vulnerabilities or errors. It can be very time consuming to manually check your code base, especially if it's large. Your company just purchased a GitHub Advanced Security license that helps save time and effort by allowing you to use code scanning. With code scanning, you receive alerts indicating any problematic code. Then, you can quickly find the problem areas and make the necessary changes. In order to enable code scanning, you need to know what tools are available and what their features are. You also need to understand how often to perform code scanning and the types of events you can use to trigger scans.

This module introduces you to code scanning and its features. You'll learn how to implement code scanning using CodeQL, third-party tools, and GitHub Actions. You'll also learn about the different ways you can configure code scanning to optimize your experience.

## Learning Objectives

After completing this module, you'll be able to:

- Describe code scanning
- List the steps for enabling code scanning in a repository
- List the steps for enabling code scanning with third-party analysis
- Contrast how to implement CodeQL analysis in a GitHub Actions workflow versus a third-party continuous integration (CI) tool
- Explain how to configure code scanning on a repository using triggering events
- Contrast the frequency of code scanning workflows (scheduled vs triggered by events)

## Prerequisites

- A GitHub account
- Familiarity with managing GitHub administrative settings
- Basic knowledge of GitHub Actions


# 4.2 What is code scanning?

Code scanning uses CodeQL to analyze the code in a GitHub repository to find security vulnerabilities and coding errors. Code scanning is available for all public repositories, and for private repositories owned by organizations where GitHub Advanced Security is enabled. If code scanning finds a potential vulnerability or error in your code, GitHub displays an alert in the repository's Security tab. After you fix the code that triggered the alert, GitHub closes the alert.

You can use code scanning to find, triage, and prioritize fixes for existing problems in your code. Code scanning also prevents developers from introducing new problems. You can schedule scans for certain days and times, or trigger scans when a specific event occurs in the repository, such as a push.

In this unit, you'll learn about CodeQL, the three options for setting up code scanning, and how to add the CodeQL workflow to your repository.

## About code scanning with CodeQL

CodeQL is the code analysis engine GitHub developed to automate security checks. You can analyze your code using CodeQL and display the results as code scanning alerts. There are three main ways to set up CodeQL analysis for code scanning:

Use default setup to quickly configure CodeQL analysis for code scanning on your repository. The default setup handles choosing the languages to analyze, query suite to run, and events that trigger scans with the option to manually configure the languages and query suites. This setup option runs code scanning as a GitHub Action.
Use advanced setup to add the CodeQL workflow directly to your repository. Adding the CodeQL workflow directly into your repository generates a customizable workflow file, which uses the github/codeql-action to run the CodeQL CLI as a GitHub Action.
Run the CodeQL CLI directly in an external CI system and upload the results to GitHub.

CodeQL treats code like data, allowing you to find potential vulnerabilities in your code with greater confidence than traditional static analyzers. You generate a CodeQL database to represent your codebase, then run CodeQL queries on that database to identify problems in the codebase. The query results are shown as code scanning alerts in GitHub when you use CodeQL with code scanning.

CodeQL supports both compiled and interpreted languages, and it can find vulnerabilities and errors in code written in the following supported languages:

- C or C++
- C#
- Go
- Java/Kotlin
- JavaScript/TypeScript
- Python
- Ruby
- Swift

The next section explains how to add the CodeQL workflow to your repository. You'll learn how to set up CodeQL using external tools in the Enable code scanning with third party tools unit.

## Enable CodeQL in your repository with the Default Setup

If you have write permissions to a repository, you can set up or configure code scanning for that repository.

Follow these steps to set up code scanning using the CodeQL GitHub Actions workflow:

On GitHub.com, navigate to the repository's main page.

Under your repository name, select Security.

Screenshot of the security tab.

Select Set up code scanning. If this option isn't available, ask an organization owner or repository administrator to enable GitHub Advanced Security.

Screenshot of the set up code scanning button.

In the Set up drop-down, select Default.

Review the default options. If needed, select the Edit button in the bottom left corner of the new window to customize how CodeQL runs.

The on:pull_request and on:push triggers are the default for code scanning are each useful for different purposes. You'll learn more about these triggers in the Configure Code Scanning unit.

Select Enable CodeQL once you're ready to turn on code scanning.

In the default CodeQL analysis workflow, code scanning is configured to analyze your code each time you either push a change to any protected branches or raise a pull request against the default branch. Once the push is made, code scanning runs automatically.

In the previous section, we enabled code scanning using the default setup, which runs code scans as a GitHub Action without needing to maintain a workflow file. The other option is Advanced setup, which generates the default workflow file you can edit for advanced configuration and more steps. We'll cover using the advanced setup for configuring code scanning in a later unit.

Running code scanning with GitHub Actions affects your monthly billing minutes. If you want to use GitHub Actions beyond the storage or minutes included in your account, you'll be billed for more usage.

## About Billing for Actions

Code scanning uses GitHub Actions, and each run of a code-scanning workflow consumes minutes for GitHub Actions. GitHub Actions usage is free for both public repositories and self-hosted runners. For private repositories, each GitHub account receives a certain number of free minutes and storage, depending on the product used with the account. Spending limits control any usage beyond the included amounts. If you're a monthly billed customer, your account has a default spending limit of zero US dollars (USD), which prevents extra usage of minutes or storage for private repositories beyond the amounts included with your account. If you pay your account by invoice, your account will have an unlimited default spending limit. Minutes reset every month, while storage usage doesn't.


# 4.3 Enable code scanning with third party tools

Completed 100 XP 4 minutes

Instead of running code scanning in GitHub, you can perform analysis elsewhere and then upload the results. Alerts for code scanning that you run externally are displayed in the same way as those you run within GitHub. You can upload Static Analysis Results Interchange Format (SARIF) files generated outside GitHub or with GitHub Actions to see code scanning alerts from third-party tools in your repository.

In this unit, you'll learn how to enable code scanning with third-party tools and how to use and upload SARIF files.

## About SARIF file uploads for code scanning

GitHub creates code-scanning alerts in a repository using information from SARIF files. You can generate SARIF files using many static analysis-security testing tools, including CodeQL. The results must use SARIF version 2.1.0.

You can upload the results using the code-scanning API, the CodeQL CLI, or GitHub Actions. The best upload method will depend on how you generated the SARIF file.

## Code-scanning API

The code-scanning API lets you retrieve information on code scanning alerts, analyses, databases, and default setup configuration from a repository. Additionally, you can update code-scanning alerts and the default setup configuration. You can use the endpoints to create automated reports for the code-scanning alerts in an organization or upload analysis results generated using offline code-scanning tools.

You can access the GitHub API over HTTPS from https://api.github.com. All data is sent and received as JSON. The API uses custom media types to let consumers choose the format of the data they wish to receive. Media types are specific to resources, allowing them to change independently and support formats that other resources don't.

There's one supported custom media type for the code scanning REST API, application/sarif+json.

You can use this media type with GET requests sent to the /analyses/{analysis_id} endpoint. When you use this media type with this operation, the response includes a subset of the actual data that was uploaded for the specified analysis, rather than the summary of the analysis that's returned when you use the default media type. The response also includes additional data such as the github/alertNumber and github/alertUrl properties. The data is formatted as SARIF version 2.1.0.

The following is an example cURL command using the API to list the code scanning alerts for an organization:

```
Copy
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/orgs/ORG/code-scanning/alerts
```

Review the GitHub REST API docs for more information about the using the code scanning API.

## CodeQL CLI

The CodeQL CLI is a standalone product that you can use to analyze code. Its main purpose is to generate a database representation of a codebase, a CodeQL database. Once the database is ready, you can query it interactively, or you can run a suite of queries to generate a set of results in SARIF format and upload the results to GitHub.com. The CodeQL CLI is free to use on public repositories maintained on GitHub.com, and it's available to use on customer owned private repositories with an Advanced Security license. Download the CodeQL bundle from https://github.com/github/codeql-action/releases.

The bundle contains:

CodeQL CLI product
A compatible version of the queries and libraries from https://github.com/github/codeql
Precompiled versions of all the queries included in the bundle

You should always use the CodeQL bundle, because this ensures compatibility and also gives much better performance than a separate download of the CodeQL CLI and checkout of the CodeQL queries.

## Code-scanning analysis with GitHub Actions

To use GitHub Actions to upload a third-party SARIF file to a repository, you'll need a GitHub Actions workflow. A GitHub Actions workflow is an automated process, made up of one or more jobs, configured as a .yml file. Workflows are stored in the .github/workflows directory for your repository.

Your workflow uses the upload-sarif action, which is part of the github/codeql-action repository. This workflow includes input parameters that you can use to configure the upload.

The main input parameter is sarif-file, which configures the file or directory of SARIF files to be uploaded. The directory or file path is relative to the root of the repository.

The upload-sarif action can be configured to run when the push and scheduled event occurs.

This example outlines the elements of the upload-sarif action yml file:

```
Copy
name: 'Code Scanning : Upload SARIF'
description: 'Upload the analysis results'
author: 'GitHub'
inputs:
  sarif_file:
    description: |
      The SARIF file or directory of SARIF files to be uploaded to GitHub code scanning.
      See https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/
      uploading-a-sarif-file-to-github#uploading-a-code-scanning-analysis-with-github-actions
      for information on the maximum number of results and maximum file size supported by code scanning.
    required: false
    default: '../results'
  checkout_path:
    description: "The path at which the analyzed repository was checked out. 
    Used to relativize any absolute paths in the uploaded SARIF file."
    required: false
    default: ${{ github.workspace }}
  token:
    default: ${{ github.token }}
  matrix:
    default: ${{ toJson(matrix) }}
  category:
    description: String used by Code Scanning for matching the analyses
    required: false
  wait-for-processing:
    description: If true, the Action will wait for the uploaded SARIF to be processed before completing.
    required: true
    default: "false"
runs:
  using: 'node12'
  main: '../lib/upload-sarif-action.js'
```

Each time the results of a new code scan are uploaded, the results are processed and alerts are added to the repository. GitHub uses properties in the SARIF file to display alerts. For example, to prevent duplicate alerts for the same problem, code scanning uses fingerprints to match results across various runs so they only appear once in the latest run for the selected branch. SARIF files created by the CodeQL analysis workflow include this fingerprint data in the partialFingerprints field. If you upload a SARIF file using the upload-sarif action and this data is missing, GitHub attempts to populate the partialFingerprints field from the source files.

If your SARIF file doesn't include partialFingerprints, the upload-sarif action will calculate the partialFingerprints field for you and attempt to prevent duplicate alerts. GitHub can only create partialFingerprints when the repository contains both the SARIF file and the source code used in the static analysis.

SARIF upload supports a maximum of 5,000 results per upload. Any results over this limit are ignored. If a tool generates too many results, you should update the configuration to focus on results for the most important rules or queries.

For each upload, SARIF upload supports a maximum size of 10 MB for the gzip-compressed SARIF file. Any uploads over this limit will be rejected. If your SARIF file is too large because it contains too many results, you should update the configuration to focus on results for the most important rules or queries.

## Upload SARIF files generated outside your repository

You can also create a new workflow that uploads SARIF files after you commit them to your repository. This is useful when the SARIF file is generated as an artifact outside of your repository.

In the following example, the workflow runs anytime commits are pushed to the repository. The action uses the partialFingerprints property to determine if changes have occurred.

In addition to running when commits are pushed, the workflow is scheduled to run once per week. This workflow uploads the results.sarif file located in the root of the repository. You could also modify this workflow to upload a directory of SARIF files. For example, you could place all SARIF files in a directory in the root of your repository called sarif-output and set the action's input parameter sarif_file to sarif-output.

```
Copy
name: "Upload SARIF"

// Run workflow each time code is pushed to your repository and on a schedule. 
//The scheduled workflow runs every Thursday at 15:45 UTC.

on:
  push:
  schedule:
    - cron: '45 15 * * 4'

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      security-events: write
  steps:
    # This step checks out a copy of your repository.
    - name: Checkout repository
      uses: actions/checkout@v2
    - name: Upload SARIF file
      uses: github/codeql-action/upload-sarif@v1
      with:
        # Path to SARIF file relative to the root of the repository
        sarif_file: results.sarif
```

## Upload SARIF files generated as part of a CI workflow

If you generate your third-party SARIF file as part of a continuous integration (CI) workflow, you can add the upload-sarif action as a step after running your CI tests. If you don't already have a CI workflow, you can create one using a starter workflow in the https://github.com/actions/starter-workflows repository.

In this example, the workflow runs anytime commits are pushed to the repository. The action uses the partialFingerprints property to determine if changes have occurred. In addition to running when commits are pushed, the workflow is scheduled to run once per week.

This example shows the ESLint static analysis tool as a step in a workflow. The Run ESLint step runs the ESLint tool and outputs the results.sarif file. The workflow then uploads the results.sarif file to GitHub using the upload-sarif action.

```
name: "ESLint analysis"

// Run workflow each time code is pushed to your repository and on a schedule.
// The scheduled workflow runs every Wednesday at 15:45 UTC.
on:
  push:
  schedule:
    - cron: '45 15 * * 3'

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      security-events: write
    steps:
      - uses: actions/checkout@v2
      - name: Run npm install
        run: npm install
      // Runs the ESlint code analysis
      - name: Run ESLint
        // eslint exits 1 if it finds anything to report
        run: node_modules/.bin/eslint build docs lib script spec-main -f node_modules/@microsoft/eslint-formatter-sarif/sarif.js -o results.sarif || true
      // Uploads results.sarif to GitHub repository using the upload-sarif action
      - uses: github/codeql-action/upload-sarif@v1
        with:
          // Path to SARIF file relative to the root of the repository
          sarif_file: results.sarif
```


# 4.4 Configure code scanning

You can configure how GitHub scans the code in your project for vulnerabilities and errors. When you choose your own configuration, you save time and decide the best frequency of code scanning for your project. In this unit, you'll learn the basics of code scanning configuration. You'll also learn how to configure the frequency of scans and schedule them to best fit your repository and development needs.

As we discussed in the previous units, you can run code scanning on GitHub, using GitHub Actions, or from your continuous integration (CI) system. Selecting the Advanced setup option on GitHub generates a customizable workflow file that you can then commit directly to your repository. You usually don't need to edit this workflow. However, if necessary, you can customize some of the settings.

For example, you can edit GitHub's CodeQL analysis workflow to specify the frequency of scans, the languages or directories to scan, and what CodeQL code scanning looks for in your code. You might also need to edit the CodeQL analysis workflow if you use a specific set of commands to compile your code. CodeQL analysis is just one type of code scanning you can perform in GitHub. The GitHub Marketplace contains several other code scanning workflows.

## Switching from Default to Advanced Code Scanning Setup

If you already have a repository set up to use code scanning using the default setup method, you can switch to using the Advanced setup in the settings. Navigate to the Code scanning section under Settings > Code security and analysis, and then select the three dots overflow icon (...). In the drop-down, select Switch to advanced. Then, follow the prompts to disable CodeQL, and re-enable it with the advanced setup's generated workflow file.

## Edit code-scanning workflow

GitHub saves workflow files in the .github/workflows directory of your repository. You can find a workflow you have added by searching for its file name. For example, by default, the workflow file for CodeQL code scanning is called codeql-analysis.yml.

Follow these steps to edit a workflow file:

1. To open the workflow editor, select the Edit icon in the upper-right corner of the file view.

*Screenshot of the Edit button*

2. Make your edits.

3. After you have edited the file, select Commit changes and complete the Commit changes form. You can choose to commit directly to the current branch, or create a new branch and start a pull request.

*Screenshot of the Commit changes form.*

Review the following sections for some common code scanning configuration options.

## Configure frequency

A common edit to the workflow file is to adjust the frequency with which code scanning occurs. You can configure the CodeQL analysis workflow to scan code on a schedule or when specific events occur in a repository. You can also edit the workflow file to scan code when someone pushes a change and whenever a pull request is created. Adjusting this frequency prevents developers from introducing new vulnerabilities and errors into the code. Scanning code on a schedule informs you about the latest vulnerabilities and errors that GitHub, security researchers, and the community discover. Even when developers aren't actively maintaining the repository.

### Scan on Push

By default, the CodeQL analysis workflow uses the on:push event to trigger a code scan on every push to the default branch of the repository and any protected branches. For code scanning to be triggered on a specified branch, the workflow must exist in that branch. If you scan on push, the results appear in the Security tab for your repository.

Additionally, when an on:push scan returns a result that can be mapped to an open pull request, these alerts automatically appear on a pull request in the same place as other pull request alerts. The alerts are identified by comparing the existing analysis of the head of the branch to the analysis for the target branch.

### Scan on PR

The default CodeQL analysis workflow uses the pull_request event to trigger a code scan on pull requests targeted against the default branch. If a pull request is from a private fork, the pull_request event is only triggered if you've selected the "Run workflows from fork pull requests" option in the repository settings. If you scan pull requests, the results appear as alerts in a pull-request check.

If you use the pull_request trigger, configured to scan the pull request's merge commit rather than the head commit, it produces more efficient and accurate results than scanning the branch head on each push. However, if you use a CI/CD system that can't be configured to trigger on pull requests, you can still use the on:push trigger so that code scanning maps the results to open pull requests on the branch and adds the alerts as annotations on a pull request.

### Define the severities causing pull request check failure

By default, only alerts with the severity level of Error or security severity level of Critical or High cause a pull-request check failure. Pull-request failures don't stop a code scan but represent a blocker when trying to merge code. You can find the list of pull-request failures in the Code scanning alerts tab under your repository's Security. In your repository settings, you can change the levels of alert severities and of security severities that cause a pull request check failure.

1. On GitHub.com, navigate to the repository main page. Under your repository name, select Settings.

*screenshot of the Settings button*

2. In the left sidebar, select Code security and analysis.

*screenshot of the Code security and analysis button.*

3. In the Code scanning section under Protection rules, use the drop-down menu to select the severity level you would like to trigger a pull request check failure.

*screenshot of the code scanning alert severity drop-down menu.*

### Avoid unnecessary scans of pull requests

You might want to avoid a code scan being triggered on specific pull requests targeted against the default branch, irrespective of which files have been changed. You can configure this setting by specifying on:pull_request:paths-ignore or on:pull_request:paths in the code-scanning workflow. For example, if the only changes in a pull request are to files with the file extensions .md or .txt you can use the following paths-ignore array.

```yaml
on:
   push:
      branches: [main, protected]
   pull_request:
      branches: [main]
      paths-ignore:
         - '**/*.md'
         - '**/*.txt'
```

### Adjust scanning schedule

If you use the default CodeQL analysis workflow, the workflow scans the code in your repository once a week at a randomly generated day and time, in addition to the scans triggered by events. To adjust this schedule, edit the cron value in the workflow.

The following example shows a CodeQL analysis workflow for a repository with a default branch called main and one protected branch called protected:

```yaml
on:
   push:
      branches: [main, protected]
   pull_request:
      branches: [main]
   schedule:
      - cron: '20 14 * * 1'
```

This workflow scans:
- Every push to the default branch and the protected branch
- Every pull request to the default branch
- The default branch every Monday at 14:20 UTC


# 4.5 Configure code scanning exercise

This exercise checks your knowledge on configuring code scanning for your repository.This GitHub exercise is graded automatically once you have attempted a solution to the challenge. The results of your actions, as well as helpful feedback, are provided in real-time within the `grade-learner` workflow logs.Here are some helpful tips before you begin the exercise:
* Read the **About this exercise** section in the exercise's repository README to understand how the exercise works.
* Follow the steps provided in the **Instructions** section to successfully complete the exercise.
* To see the results of your exercise, navigate to the **Actions** tab of your cloned repository and click on the most recent run on the **Grading** workflow.
* Stuck on what to do? Revisit the content in the last unit or check out the **Useful resources** section in the exercise's repository README for some additional resources.

**Note**
A grading script exists under `.github/workflows/grading.yml`. You do not need to modify this workflow to complete this exercise. **Altering the contents in this workflow can break the exercise's ability to validate your actions, provide feedback, or grade the results**.

This exercise is a challenge based on content covered in this module. It might take several attempts to complete the exercise. You can revisit previous content in this module, or navigate to some of the additional resources provided as many times as you want to find the solution.When you've finished the exercise in GitHub, return here for:
* A quick knowledge check
* A summary of what you've learned
* A badge for completing this module​

https://github.com/skills/introduction-to-codeql



# 4.6 Module assessment

## Check your knowledge

### 1. When code scanning is enabled, what is one default event that triggers a scan?

- [ ] Creating a new branch.
- [x] **Pushing a change.** ✅
- [ ] Deleting a branch.

**Explanation:** By default, the CodeQL analysis workflow uses the `on:push` event to trigger a code scan on every push to the default branch of the repository and any protected branches. This is one of the primary triggering events for code scanning.

### 2. Which of the following are the tools used to upload a SARIF file?

- [x] **The tools used are GitHub Actions, the code scanning API, and the CodeQL CLI.** ✅
- [ ] The tools used are GitHub Actions, the ESLint analysis tool, the code scanning API, and the CodeQL CLI.
- [ ] The tools used are the partialFingerprints property, GitHub Actions, the code scanning API, and the CodeQL CLI.

**Explanation:** According to the documentation, you can upload SARIF files using three main methods: the code-scanning API, the CodeQL CLI, or GitHub Actions. ESLint is a static analysis tool that generates SARIF files, and partialFingerprints is a property within SARIF files, but they are not upload tools.

### 3. What is the difference between scheduled versus triggered events in code scanning?

- [ ] Scheduled events are more difficult to configure than triggered events.
- [x] **Scheduled events run based on a specified schedule and triggered events run on code events such as a push.** ✅
- [ ] Triggered events run less frequently than scheduled events.

**Explanation:** Scheduled events run at predefined times (using cron syntax) regardless of repository activity, while triggered events respond to specific repository events like pushes, pull requests, or other code-related activities. The frequency depends on the specific configuration, not the type of event.


# 4.7 Summary

In this module, you learned how to enable and configure code scanning for your repository. Code scanning works with the integrated GitHub CodeQL action or with third party tools. You can schedule or trigger it based on specific events, saving time and ensuring your code stays free of errors and security vulnerabilities. Without code scanning, you'd need to manually verify the code base, which can take a lot of time and has a higher potential for mistakes. Code scanning alerts you of any problems and lets you review these issues in a single location.

**Learn More**
Here are some links to more information about code scanning:
* Learn more about GitHub Advanced Security
* Learn more about GitHub Actions
* Learn more about using SARIF files with Code Scanning
* Troubleshooting code scanning
* REST API endpoints for code scanning



# 6 Code with GitHub Codespaces

GitHub Codespaces is a fully configured development environment hosted in the cloud. By using GitHub Codespaces, your workspace, along with all of your configured development environments, is available from any computer with access to the internet.

# 6.1 Introduction

GitHub Codespaces is an instant, cloud-based development environment that uses a container to provide you with common languages, tools, and utilities for development.

In this module, we:
* Explore the Codespaces lifecycle and processes.
* Review the ways you can customize your Codespace set up.
* Compare the differences between GitHub Codespaces and GitHub.dev.
* Complete an exercise to practice coding in Codespaces.


# 6.2 The Codespace lifecycle

Completed 100 XP 6 minutes

GitHub Codespaces is configurable, allowing you to create a customized development environment for your project. By configuring a custom development environment for your project, you can have a repeatable Codespace configuration for all users of your project.

A Codespace's lifecycle begins when you create a Codespace and ends when you delete it. You can disconnect and reconnect to an active Codespace without affecting its running processes. You can stop and restart a Codespace without losing the changes that you make to your project.

Diagram of a circular lifecycle of a Codespace that starts with creating and ends with deleting.

## Create a Codespace

You can create a Codespace on GitHub.com, in Visual Studio Code, or by GitHub CLI. There are four ways to create a Codespace:

- From a GitHub template or any template repository on GitHub.com to start a new project.
- From a branch in your repository, for new feature work.
- From an open pull request, to explore work-in-progress.
- From a commit in a repository's history to investigate a bug at a specific point in time.

You can temporarily use a Codespace in order to test code or you can return to the same Codespace to work on long-running feature work.

You can create more than one Codespace per repository or even per branch. However, there are limits to the number of Codespaces you can create and run at the same time. When you reach the maximum number of Codespaces and try to create another, a message is displayed. The message tells you that an existing Codespace needs to be removed/deleted before a new Codespace can be created.

You can create a new Codespace each time you develop in GitHub Codespaces or keep a long-running Codespace for a feature. If starting a new project, create a Codespace from a template and publish it to a repository on GitHub later.

When creating a new Codespace each time you work on a project, you should regularly push your changes to ensure that any new commits are on GitHub. When using a long-running Codespace for a new project, pull from the repository's default branch each time you start working in Codespace to enable your environment to get the latest commits. The workflow is similar to working with a project on a local machine.

Repository administrators can enable GitHub Codespaces prebuilds for a repository to speed up Codespace creation.

For an in-depth walkthrough and step-by-step guidance, see the resources titled A beginner's guide to learning to code with GitHub Codespaces and Developing in a Codespace located in the Summary unit at the end of this module.

## Codespace creation process

Diagram of a GitHub codespace and how it connects from your code editor and into a docker container.

When you create a GitHub Codespace, four processes occur:

1) A virtual machine and storage are assigned to your Codespace.
2) A container is created.
3) A connection to the Codespace is made.
4) A post-creation setup is made.

## Save changes in a Codespace

When you connect to a Codespace through the web, AutoSave is automatically enabled to save changes after a specific amount of time passes. When you connect to a Codespace through Visual Studio Code running on your desktop, you must enable AutoSave.

Your work saves to a virtual machine in the cloud. You can close and stop a Codespace and return to the saved work at a later time. If you have unsaved changes, you receive a prompt to save them before exiting. However, if your Codespace is deleted, then your work is lost. To save your work, you must commit your changes and push them to your remote repository or publish your work to a new one if you created your Codespace from a template.

## Open an existing Codespace

You can reopen any of your active or stopped Codespaces on GitHub.com, in a JetBrains IDE, in Visual Studio Code, or by using GitHub CLI.

To resume an existing Codespace, you can go to the repository where the Codespace exists, select the , key and then select Resume this codespace. Or, you can open https://github.com/codespaces in the browser, select the repository, and then select the existing Codespace.

## Timeouts for a Codespace

If a Codespace is inactive, or if you exit your Codespace without explicitly stopping, the application times out after a period of inactivity and stops running. The default timeout is after 30 minutes of inactivity. When a Codespace times out, your data is kept from the last time your changes were saved.

## Internet connection while using GitHub Codespaces

A Codespace requires an internet connection. If the connection to the internet is lost while working in a Codespace, you aren't able to access your Codespace. However, any uncommitted changes are saved. When you reestablish the internet connection, you can access the Codespace in the same state that it was left in when the connection was lost.

If you have an unstable internet connection, you should frequently commit and push your changes.

## Close or stop a Codespace

If you exit the Codespace without running the stop command or leave the Codespace running without interaction, the Codespace and its running processes continue during the inactivity timeout period. The default inactivity timeout period is 30 minutes. You can define your personal timeout setting for the Codespaces you create, but an organization's timeout policy can overrule the setting.

Only running Codespaces incur CPU charges. A stopped Codespace incurs only storage costs.

You can stop and restart a Codespace to apply changes. For example, if you change the machine type used for your Codespace, you need to stop and restart it for the change to take effect. When you close or stop your Codespace, all uncommitted changes are preserved until you connect to the Codespace again.

You can also stop Codespace and choose to restart or delete it if you encounter an error or something unexpected.

## Rebuild a Codespace

You can rebuild your Codespace to implement changes to your dev container configuration. For most uses, you can create a new Codespace as an alternative to rebuilding a Codespace. When you rebuild your Codespace, images from the cache speed-up the rebuild process. You can also perform a full rebuild to clear the cache and rebuild the container with fresh images.

When you rebuild the container in a Codespace, changes you made outside the /workspaces directory are cleared. Changes you made inside the /workspaces directory, including the clone of the repository or template you created the Codespace from, are preserved over a rebuild.

## Delete a Codespace

You can create a Codespace for a particular task. After you push your changes to a remote branch, then you can safely delete that Codespace.

If you try to delete a Codespace with unpushed git commits, the editor notifies you that you have changes that aren't yet pushed to a remote branch. You can push any desired changes and then delete your Codespace. You can also continue to delete your Codespace and any uncommitted changes or export the code to a new branch without creating a new Codespace.

Stopped Codespaces that remain inactive for a specified amount of time are deleted automatically. Inactive Codespaces delete after 30 days, but you can customize your Codespace retention intervals.



# 6.3  Personalize your Codespace

GitHub Codespaces is a dedicated environment for you. You can configure your repositories with a dev container to define their default GitHub Codespaces environment and personalize your development experience across all of your Codespaces with dotfiles and Settings Sync.

## What you can customize

There are many ways you can customize your Codespace. Let's review each one.

### Settings Sync
You can synchronize your Visual Studio Code (VS Code) settings between the desktop application and the VS Code web client.

### Dotfiles
You can use a dotfiles repository to specify scripts, shell preferences, and other configurations.

### Rename a Codespace
When you create a Codespace, an autogenerated display name is assigned to it. If you have multiple Codespaces, the display name helps you to differentiate between Codespaces. You can change the display name for your Codespace.

### Change your shell
You can change your shell in a Codespace to keep the setup you're used to. When you're working in a Codespace, you can open a new terminal window with a shell of your choice, change your default shell for new terminal windows, or install a new shell. You can also use dotfiles to configure your shell.

### Change the machine type
You can change the type of machine that's running your Codespace, so that you're using resources appropriate for the work you're doing.

### Set the default editor
You can set your default editor for Codespaces in your personal settings page. Set your editor preference so that when you create a Codespace or open an existing Codespace, it opens to your default editor.

- **Visual Studio Code (desktop application)**
- **Visual Studio Code (web client application)**
- **JetBrains Gateway** - for opening Codespaces in a JetBrains IDE
- **JupyterLab** - the web interface for Project Jupyter

### Set the default region
You can set your default region in the GitHub Codespaces profile settings page to personalize where your data is held.

### Set the timeout
A Codespace will stop running after a period of inactivity. By default this period is 30 minutes, but you can specify a longer or shorter default timeout period in your personal settings on GitHub. The updated setting applies to any new Codespaces you create, or to existing Codespaces the next time you start them.

### Configure automatic deletion
Inactive Codespaces are automatically deleted. You can choose how long your stopped Codespaces are retained, up to a maximum of 30 days.

Additional information and step-by-step instructions regarding customization are located in the Summary unit at the end of this module.

## Add to your Codespace with extensions or plugins

You can add plugins and extensions within a Codespace to personalize your experience in JetBrains and VS Code.

### VS Code extensions

If you work on your Codespaces in the VS Code desktop application or the web client, you can add any extensions you need from the Visual Studio Code Marketplace. Refer to Supporting Remote Development and GitHub Codespaces in the VS Code documentation for information on how extensions run in GitHub Codespaces.

If you already use VS Code, you can use Settings Sync to automatically sync extensions, settings, themes, and keyboard shortcuts between your local instance and any Codespaces you create.

### JetBrains plugins

If you work on your Codespaces in a JetBrains IDE, you can add plugins from the JetBrains Marketplace.


# 6.4 Codespaces versus GitHub.dev editor

You're probably asking yourself, when should I use GitHub Codespaces and when should I use GitHub.dev?

You can use GitHub.dev to navigate files and sources code repositories from GitHub, and make and commit code changes. You can open any repository, fork, or pull request in GitHub.dev editor.

If you want to do more heavy lifting like testing your code, use GitHub Codespaces. It has compute associated with it so you can build your code, run your code, and have terminal access. GitHub.dev doesn't have compute in it. With GitHub Codespaces, you get the power of a personal Virtual Machine (VM) with terminal access, the same way you could use your local environment, just in the cloud.

## Comparison of Codespaces and GitHub.dev

The following table lists the main differences between Codespaces and GitHub.dev:

| Feature | GitHub.dev | GitHub Codespaces |
|---------|------------|-------------------|
| **Cost** | Free | Free monthly quota of usage for personal accounts. |
| **Availability** | Available to everyone on GitHub.com. | Available to everyone on GitHub.com. |
| **Startup** | GitHub.dev opens instantly with a key-press and you can start using it right away without having to wait for configuration or installation. | When you create or resume a Codespace, the Codespace is assigned a VM. The container is then configured based on the contents of a devcontainer.json file. This setup takes a few minutes to create the development environment. |
| **Compute** | There are no associated compute resources, so you can't build and run your code or use the integrated terminal. | With GitHub Codespaces, you get the power of a dedicated VM to run and debug your application. |
| **Terminal access** | None | GitHub Codespaces provides a common set of tools by default, meaning that you can use the Terminal exactly as you would in your local environment. |
| **Extensions** | Only a subset of extensions that can run on the web appear in the extensions view and can be installed | With GitHub Codespaces, you can use most extensions from the Visual Studio Code Marketplace. |

## Continue working on Codespaces

You can start your workflow in GitHub.dev and continue working on a Codespace. If you try to access the Run and Debug View or the Terminal, you see a notification that they're not available in GitHub.dev.

To continue your work in a Codespace, select **Continue Working on…**. Select **Create New Codespace** to create a Codespace on your current branch. Before you choose this option, you must commit any changes.


# 6.5 Exercise - Code with Codespaces and Visual Studio Code

Now that you understand the Codespaces lifecycle and processes, it's time to practice coding in Codespaces and Visual Studio Code (VS Code). Use the following instructions to complete this exercise.

## Instructions

1. **Right-click the GitHub exercise link** to open it in a new tab.

2. **On the GitHub Exercise Welcome page**, right-click the **Start course** button to open it in a new tab.
   - In the new tab, most of the prompts automatically fill-in for you.
   - For owner, choose your personal account or an organization to host the repository.
   - We recommend creating a public repository, as private repositories use Actions minutes.

3. **Scroll down and select the "Create repository" button** at the bottom of the form.

4. **After your new repository is created**, wait about 20 seconds, then refresh the page. Follow the step-by-step instructions in the new repository's README.

## When you finish the exercise in GitHub, return here to:

- Complete a knowledge check
- Review a summary of what you learned in this module
- Earn a badge for completing this module


# 6.6 Module assessment

### 1. Which directory is the clone placed in after creating a Codespace?

- [x] **/workspaces directory** ✅
- [ ] /temp directory
- [ ] ~/.bashrc directory
- [ ] Linux directory

**Explanation:** According to the documentation, when you rebuild the container in a Codespace, changes you made inside the /workspaces directory, including the clone of the repository or template you created the Codespace from, are preserved over a rebuild. This indicates that the clone is placed in the /workspaces directory.

### 2. What's the maximum number of Codespaces that you can create per repository or branch?

- [ ] You can only create two Codespaces.
- [ ] You can create a total of 10 Codespaces.
- [ ] You can create a total of 30 Codespaces.
- [x] **You can create an unlimited number of Codespaces per repository or branch, depending upon available space. When you reach an upper amount of resources, a message displays that an existing Codespace needs to removed/deleted before a new Codespace can be created.** ✅

**Explanation:** The documentation states that "You can create more than one Codespace per repository or even per branch. However, there are limits to the number of Codespaces you can create and run at the same time. When you reach the maximum number of Codespaces and try to create another, a message is displayed."

### 3. What happens when Codespace loses internet connectivity?

- [x] **If the connection to the internet is lost while working in a Codespace, you aren't able to access your Codespace.** ✅
- [ ] Codespace doesn't require an internet connection. I can access my Codespace regardless if I lose connectivity.
- [ ] If you lose internet connection while working on your Codespace, your changes aren't saved.

**Explanation:** The documentation clearly states that "A Codespace requires an internet connection. If the connection to the internet is lost while working in a Codespace, you aren't able to access your Codespace. However, any uncommitted changes are saved."

### 4. What defines the beginning of a Codespace's lifecycle?

- [x] **A Codespace's lifecycle begins when you create a Codespace and ends when you delete it.** ✅
- [ ] A Codespace's lifecycle begins immediately when GitHub is opened and ends when the software is closed.
- [ ] A Codespace's lifecycle begins when a repository is created and ends when you delete it.

**Explanation:** The documentation explicitly states at the beginning of the lifecycle section: "A Codespace's lifecycle begins when you create a Codespace and ends when you delete it."


# 6.7 Summary

In this module, you learned about GitHub Codespaces, a fully configured development environment hosted in the cloud.

## What you've learned

You should now be able to:

- **Describe GitHub Codespaces**
- **Explain the GitHub Codespace lifecycle** and how to perform each step
- **Define the different customizations** you can personalize with GitHub Codespaces
- **Discern the differences** between GitHub.dev and GitHub Codespaces

## Resources

Here are links to more information on the subjects we discussed in this module:

- [A beginner's guide to learning to code with GitHub Codespaces](https://docs.github.com/en/codespaces/getting-started/quickstart)
- [Developing in a Codespace](https://docs.github.com/en/codespaces/developing-in-codespaces)
- [Customizing your Codespace](https://docs.github.com/en/codespaces/customizing-your-codespace)

## Provide feedback

Use this issue form to provide content feedback or suggested changes for this Microsoft Learn module. GitHub maintains this content and a team member will triage the request. Thank you for taking the time to improve our content!


# 7 Manage your work with GitHub Projects

Learn to use GitHub Projects to create issues, break them into tasks, track relationships, add custom fields, and have conversations.


# 7.1 Introduction

We know your work is dynamic. Priorities can change quickly and needing to stay current and aware of everything is how you and your team can be successful.

Luckily, GitHub Projects can help you stay organized, connected, and up-to-date in order to keep your team on track.

Projects connect your planning directly to the work your team is doing and flexibly adapts to whatever your team needs at any point. Project tables are built like a spreadsheet and give you a live canvas to filter, sort, and group issues and pull requests. You can use Project tables, Project boards, and custom fields to track a sprint, plan a feature, or manage a large-scale release.

## Learning objectives:

- Discern the differences between Projects and Projects (Classic)
- Learn how to build an organization level Project
- Understand how to organize your Project
- Gain insight on how to edit the visibility, access, and management of your Project
- Know how to develop automation and insights from your Project

## Prerequisites:

- A GitHub account
- Access to an organization


# 7.2 Projects versus Projects Classic

Before we dive into learning how to utilize the new and improved Projects, let's take a moment to walk through what has changed from Projects (Classic).

Let's first go over some of the enhancements in a side-by-side glance and then dive deeper into each section of updates.

## Projects vs Projects (Classic)

| Feature | Projects | Projects (Classic) |
|---------|----------|-------------------|
| **Tables and Boards** | Boards, Lists, Timeline Layout | Boards |
| **Data** | Sort, rank, and group items by custom fields such as text, number, date, iteration and single select | Columns and Cards |
| **Insights** | Create visuals to help understand your work through historical and current charts with Projects | Progress bar |
| **Automation** | Use GraphQL API, Actions, and Column presets to manage your Project | Configure Column presets for when issues and pull requests are added, edited, or closed |

The new GitHub Projects provides a richer experience that enables you to keep track of your work, where you work. Let's dive a bit deeper into the changes that have been made.

## Comprehensive lists of Project enhancements

### Tables and boards

- Plan and track work in a table or board view
- Rank, sort, and group within a table by any custom field
- Create draft issues with detailed descriptions and metadata
- Materialize any perspective with tokenized filtering and saved views
- Customize cards and group-by in Project boards
- Real-time Project updates and user presence indicators

### Data

- Define custom fields of type: text, number, date, iteration, and single select
- Configure iterations with flexible date ranges and breaks to represent your sprints, cycles, or quarterly roadmap
- View linked pull requests and reviewers in both table and board views

### Insight

- Create and configure custom bar, column, line, and stacked area charts
- Use aggregation functions like sum, count, average, min, and max to get the proper insight
- Persist charts and share them with a URL to keep everyone in the know

### Automation

- GraphQL ProjectsV2 API
- GitHub app Project scopes
- Webhooks events for Project item metadata updates
- GitHub Action to automate adding issues to Projects

Now let's dive into how to create a Project!


# 7.3 How to create a project

Imagine you want to organize your team's feature backlog. Projects, GitHub's built-in program-management tool, is a perfect way to organize and prioritize your team's work in a single space.

## In this unit, you learn how to:

- Create a Project
- Set the name, description, and README of your Project
- Add issues and pull requests to your Project

## Creating an organization-level Project

First, you want to lay the foundation by creating a new Project. Creating is relatively quick and simple.

1. In the top right corner of GitHub.com, select your profile photo, then select **Your organizations**.

*Screenshot of the Profile Dropdown Menu.*

*Screenshot of the Profile Dropdown Menu that includes Your profile, Your repositories, Your Codespaces, Your organizations, and Your enterprises with Your Organization option highlighted.*

2. Scroll down to select the organization for your new Project.

3. Navigate from the **Overview** tab to the **Projects** tab.

4. Select the green button labeled **New Project**.

5. A pop-up prompts you to select either a template or start from scratch. Let's choose the **Start from scratch** option and select **Table**.

6. Select the green **Create project** button.

You just created a Project!

You can also create a personal Project by selecting your profile photo and navigating to **Your projects**. Once you're on your Projects page, select the green button titled **New project**.

## Set your Project's name, description, and README

Let's define your Project in a couple of different ways so that your team can easily understand what you're tracking.

1. Navigate to your newly created Project to edit your Project's name, description, and README.

2. At the top right of the page, select the three dots to open the menu and select **Settings**.

3. **Project Name** is where you edit the name of the Project.

4. **Short description** allows you to add a few words about the Project.

5. **README** lets you add information for your team to understand why you created this Project and what you hope to accomplish with it. Once finished, select **Save changes**.

*Screenshot of a Project README that is highlighted with example text that describes the user's Project.*

## Add issues and pull requests to your Project

Adding issues and pull requests to your Project is what makes the tool so powerful. Projects enable you to know the status of tasks your team is working on to coordinate and complete your goals.

Let's go through the different ways to add issues and pull requests to your Project.

### Add an existing issue and pull request

1. Copy the url of an existing issue or pull request.

2. Place your cursor in the bottom row of the Project next to the **+** and paste the URL of your issue or pull request.

*Screenshot of a Project in List view with an example of a URL of an Issue pasted into the Project.*

3. Press **Enter** and your issue or pull request appears as a task in your Project.

### Search for an existing issue and pull request

You can search for existing issues or pull requests by adding a new item.

1. Enter **#** to search repositories. You can type part of the repository name to narrow down your options.

*Screenshot of a Project in List view, focused on searching for an existing issue or pull request by adding a # and typing in key phrases.*

2. Select the repository where the pull request or issue is located, which prompts to search issues and pull requests.

3. Start typing the title of the issue or pull request to find the one you want.

4. Select the issue or pull request.

### Bulk add issues and pull requests

You can bulk add issues and pull requests to an existing repository to save time. It allows you to start organizing your team faster.

1. Select **+** in the bottom row of the Project.

2. Select **Add item from repository**.

3. To change the repository, select the dropdown and choose a repository. The issues and pull requests then populate.

4. You can either select all or select those issues or pull requests you want to include.

*Screenshot of bulk adding issues and pull requests from a repository, with the option to search for specific issues or pull requests highlighted.*

5. Once you're ready to add the issues and pull requests to your Project, select the green button titled **Add selected items** in the bottom right corner.

In the next unit, you'll learn how to organize and prioritize your Project in order to keep your tasks on track.



# 7.4 How to organize your project

Now that you added issues and pull requests to your Project, it's time to organize to keep track of the great work you and your team are doing.

## In this unit, you learn how to:

- Create a field to track and group by priority
- Add an iteration field
- Create a board view

## Create a field to track and group by priority

To group a set of issues and pull requests by priority, you need to first create a new field.

1. In the table view, in the rightmost field header, select **+**.

2. Select **New field**.

*Screenshot of the top of a Project showing the columns for Notes and Priority. The New Field Button as a plus sign is highlighted.*

3. Type the name of your field. In this case, it's **Priority**.

4. Select the **Field Type** drop-down.

5. To create your own classification for your new field, select the **Single select** option.

*Screenshot of the drop-down menu for a New Field.*

*Screenshot of the drop-down menu for a New Field that contains Text, Number, Date, Single select, and Iteration with the Single Select option highlighted.*

6. In the **Options** text box, start to add your different priority levels. You can label them as **Urgent**, **High**, **Medium**, and **Low**.

7. Select **Save**.

Now that you have your priority classification set up, you need to classify your issues and pull requests based on priority. To make a classification, select the issue or pull request you want to classify in the field row titled **Priority**. Now, in the drop-down field, select the priority you want to choose for this particular issue or pull request.

Repeat for your remaining pull requests and issues.

Great!

Now, let's group your issues and pull requests by priority to make it easier to focus on urgent and high priority items.

1. Select the down arrow next to the name of your currently opened view.
2. Select the **Group by** option.
3. Select **Priority**.

Now you should be able to view issues and pull requests based on the priority you assigned them. One of the great features of this particular view is you can now drag and drop issues into new priority fields easily.

*Screenshot example of Priority Classification within Project List view.*

*Screenshot example of Priority Classification within Project List view with Issues and Pull Requests that are organized and grouped as High, Medium, and Low classifications.*

Now that you have your work prioritized, let's tackle timelines and iterations.

If you want to save this view, select the **Save changes** button on the top-right of the list view.

## Add an iteration field

Adding an iteration field to your Project can help you and your team visualize the balance of upcoming work in order to help everyone stay on track. An iteration field enables you to set up phases for your tasks in a tangible timeframe to keep you and your team organized.

To add an iteration field, go to your Project's table view.

1. In the rightmost field header, select **+**.

2. Select **New field**.

3. Add a **Field name**, such as **Project Phase** or **Sprint**.

4. Under **Field Type**, select **Iteration**.

5. Choose a **Starts On** date.

6. Change the **Duration** of each iteration by typing a new number, and select the drop-down for either **days** or **weeks** as follows.

*Screenshot of the Iteration Field Date Editing Field with the options to edit start date and duration in weeks.*

7. Select **Save and create**.

Once you have your iteration field set up, you can now assign what iteration phase you want each of your issues and pull requests to fall under.

Now that you've prioritized and organized your Project, let's take a look at how to view your Project from a board view perspective.

## Create a board view

A board view of your Project enables you to view upcoming tasks in a more visual way.

Let's walk through how to get your board view up and running.

1. On the currently open view, select the down arrow.
2. Under **Layout**, select **Board**. When you change the layout, your Project displays an indicator to show the view was modified.
3. Select the **Save** button at the top-right of the board.
4. You can rename the view by double-clicking the view's tab, and selecting out of the tab to automatically save.

**Note:** these steps can also be accomplished by selecting **New View** to the right of your existing views.

Now, you can drag and drop issues and pull requests to the various columns.

*Screenshot example of a Project board with four columns labeled; no status, todo, in-progress, done.*


# 7.5 How to organize and automate your project

You created your Project, added issues and pull requests, and organized it. Now, let's talk about how to:

- Provide visibility and access to your Project
- Close and delete your Project

## Project visibility and access

In this portion of the unit, you learn how to:

- Control visibility to your Project
- Manage access to your Project
- Invite collaborators and change roles
- Add a Project to a team
- Add a Project to a repository

### Control visibility to your Project

You have the ability to control whether your Project is public or private. When your Project is public, everyone on the internet can view it. When your Project is private, only users granted at least read access can see your Project.

To change your Project's visibility:

1. Navigate to your Project.

2. In the top-right, select the three dots at the top menu and choose **Settings**.

3. Scroll down to **Danger zone**, and under **Visibility** select **Private** or **Public** from the drop-down.

*Screenshot of the Danger Zone settings with the option to make your Project Public or Private.*

### Manage access to your Project

Access to your Project depends on if your Project is an organization-level Project or a personal/user-level Project. Managing access is similar between the two levels.

Admins of organization-level Projects can manage access for the entire organization, for teams, for individual organization members, and for outside collaborators. Admins of user-level Projects can invite individual collaborators and manage their access.

#### Organization-level Project

- **No access**: Only organization owners and users granted individual access can see the Project. Organization owners are also admins for the Project.
- **Read**: Everyone in the organization can see the Project. Organization owners are also admins for the Project.
- **Write**: Everyone in the organization can see and edit the Project. Organization owners are also admins for the Project.
- **Admin**: Everyone in the organization is an admin for the Project.

#### Personal/User-level Project

- **Read**: The individual can view the Project.
- **Write**: The individual can view and edit the Project.
- **Admin**: The individual can view, edit, and add new collaborators to the Project.

### Invite collaborators and change roles

1. Navigate to your Project.

2. In the top right, select the three dots to open the menu and choose **Settings**.

3. In the left-hand navigation bar, select **Manage access**.

4. Once on the page you can either:
   - Invite individuals and teams by searching in the **Invite collaborators** search bar.
   - Change their role or remove them under **Manage access**.

*Screenshot of the Manage access settings with the ability to add a single collaborator or team and select their role or remove them.*

### Add a Project to a team

You can add Projects to your team to give them collaborator access to their Projects. Adding lists them on the team's Projects page, which makes it easier for members to identify which Project a particular team uses. Teams are granted read permissions on any Project they get added to.

Here's how to add Projects to teams:

1. In the top right corner of GitHub.com, select your profile photo and choose **Your organizations**.
2. Select the name of your organization.
3. Navigate to the **Teams** tab and select the name of the team to which you want to grant access.
4. Select **Projects** and choose **Link a project**.
5. Start typing the name of the Project you want to add and then select the Project in the list of matches.

### Add a Project to a repository

You can list relevant Projects in a repository so your team can access information they need to stay up to date. However, you can only list Projects if the same user or organization owns both the Projects and the repository. In order for repository members to see a Project listed in a repository, they must have visibility to the Project.

Here are the steps to add a Project to a repository:

1. Navigate to the main page of your repository.

2. Select the **Projects** tab and choose to **Link a project**.

*screenshot of the green Link a project button to add to a repository.*

3. Search for Projects owned by the same user or organization as the repository owner.

4. Select a Project to list the Project in your repository.

## Close and delete Projects

Once you complete a Project or you no longer need to use it, you can either close or delete it.

**Closing** a Project enables you to remove it from the list of Projects but retain the content and ability to reopen the Project later. We recommend this option to preserve your data.

However, **deleting** a Project permanently removes it from the platform along with any saved views, custom fields and associated values, insights data, and drafted issues.

Regardless of which option you choose, both closing and deleting Project settings are in the same location.

Here are steps on how to navigate to them:

1. Navigate to your Project.

2. In the top-right, select the three dots to open the menu and choose **Settings**.

3. Scroll down to the **Danger zone** section and either select **Close project** or **Delete project**.

   - Selecting **Delete project** prompts you to read the warnings, and then type the name of your Project into the text box.

*Screenshot of the Danger zone section with the option to change visibility, close Project and delete Project with delete Project highlighted.*

Next up, we'll review insights and automation in Projects.



# 7.6 Insight and automation with projects

Now let's talk about how Projects can provide you with insights and how to make life a bit easier with automation.

## Insights with Projects

In this section, you learn about:

- Insights and how they can be useful
- Current charts and historical charts
- Creating and customizing charts

### Insights and how they can be useful

Insights with Projects enables you to view, create, and customize charts that use items added to your Project as source data. When you create a chart, you set the filters, chart type, and information displayed. The chart is available to anyone who can view the Project. You can generate two types of charts: current charts and historical charts. Let's dive into the differences between the two.

### Current charts

You can create current charts to visualize your Project items. For example, you can create charts to show the number of items assigned to each individual, or the number of issues assigned to each upcoming iteration.

You can use filters to manipulate the data used to build your chart. For example, you can create a chart showing how much upcoming work you have, but limit those results to particular labels or assignees.

*Screenshot example of a current bar chart that tracks the number of hours spent per seven iteration phases. Color coded by amount of time spent on Bugs, Feedback, Backend, and UI work.*

### Historical charts

Historical charts are available with GitHub Team and GitHub Enterprise Cloud for organizations. Historical charts are time-based charts that allow you to view your Project's trends and progress. You can view the number of items over time grouped by status and other fields. The default Burn up chart shows item status over time, allowing you to visualize progress and spot patterns.

*Screenshot example of a historic stacked area line graph showing progress during the month of July.*

*Screenshot example of a historic stacked area line graph showing the number of hours spent on to dos, in progress, and completed tasks during the month of July.*

### Create and customize charts

Follow these steps to create a new chart:

1. Navigate to your Project.
2. In the top-right, select the line graph button. When you hover over the button, the **Insights** label appears.
3. In the menu on the left, select **New chart**.
4. Filter by keyword or field to change the data used to build the chart.
5. To the right of the filter text box, select **Save**.

Now that you created a new chart, let's customize your new chart to fit your needs.

1. In the menu on the left, select the chart you'd like to configure.
2. On the right side of the page, select **Configure**, and a panel opens.
3. Select the **Layout** dropdown to change the type of chart you want to use.
4. Select the **X-axis** dropdown and choose the field you want to use.
5. Optionally, select **Group by** to group items on your X-axis. Choose the field you want to use or **None** to disable grouping.

## Automation with Projects

Let GitHub do some of the work for you by automating your Project. There are three different ways you can do so:

- Built-in automated workflows
- GraphQL API
- GitHub Actions with workflows

The easiest way to automate your Project is built-in workflows. GraphQL and Actions give more control over customizing automation. In the following sections, you learn how to utilize Project's built-in automation and briefly go over GraphQL API and GitHub Actions automation.

### Configure built-in workflows

Built-in workflows help you stay aware of all your work. Your Project takes newly created issues or pull requests and automatically puts them into your Project with a Todo status. Here's how to enable:

1. In the top-right corner of your Project, select the three dots menu and choose **Workflows**.

*Screenshot of the Workflows menu on Projects that contains the options, Workflows, Archived items, and Settings with Workflows highlighted.*

2. In the left column, under **Default workflows**, select **Item added to project**.

*Screenshot of the menu to enable workflows once an action occurs.*

*Screenshot of the menu to enable workflows once an action occurs. Options include Item added to Project, Item reopened, Item closed, Code changes requested, Code review approved, Pull request merged with Item added to Project highlighted.*

3. Select the **Edit** button to make changes to the workflow.

4. In the **When an item is added to the project** section, ensure that both **issues** and **pull requests** are selected.

5. In the **Set Value** section, select **Status:Todo**.

6. Select **Save and turn on workflow**.

Congratulations, you automated your Project!

### GitHub Actions with workflows

GitHub Actions enables the most customization for your Project's automation. You can use GitHub Actions to automate your project management tasks by creating workflows. Each workflow contains a series of tasks that are performed automatically every time the workflow runs. An example workflow triggers upon issue creation that adds a label, leaves a comment, and moves the issue to a project board.

*An issue creation triggers a workflow that adds a label, leaves a comment, and moves the issue to a project board.*

Learn more about automating workflows for your Project in the article **Automating Projects using Actions** at the end of this module.

### GraphQL API

If you're using GraphQL in GitHub, you can utilize an API to help automate your Project. For more information on using GraphQL API, see the article, **Using the API to Manage Projects** at the end of this module.



# 7.7 Module assessment

## Check your knowledge

### 1. What Project descriptor automatically saves when you change it?

- [x] **Project name** ✅
- [ ] Project description
- [ ] Project README

**Explanation:** According to the documentation, you can rename the view by double-clicking the view's tab, and selecting out of the tab to automatically save. This indicates that the Project name automatically saves when changed.

### 2. What does an iteration field help you do in Projects?

- [ ] Allows you to keep track of the various changes made to an issue or pull request.
- [ ] Allows you to reverse the changes you made to your Project.
- [x] **Allows you to create sequential phases of your project and group issues and pull requests based on the phase.** ✅

**Explanation:** The documentation states that "An iteration field enables you to set up phases for your tasks in a tangible timeframe to keep you and your team organized" and helps "visualize the balance of upcoming work."

### 3. What field can you use in order to make a Priority grouping like High, Medium, and Low in your Project?

- [ ] Date
- [x] **Single select** ✅
- [ ] Iteration field

**Explanation:** The documentation specifically mentions creating a priority field using the "Single select" option to create classifications like "Urgent, High, Medium, and Low."

### 4. What is the easiest way to add automation to your Project?

- [ ] GraphQL API
- [x] **Built-in Automation** ✅
- [ ] GitHub Actions

**Explanation:** The documentation clearly states: "The easiest way to automate your Project is built-in workflows. GraphQL and Actions give more control over customizing automation."

### 5. What is the name of the section where you can change the visibility of your Project, close your Project, or delete your Project?

- [ ] Red zone
- [ ] Visibility and Access
- [x] **Danger zone** ✅

**Explanation:** The documentation repeatedly refers to the "Danger zone" section where you can change visibility, close projects, or delete projects. It's specifically mentioned as "Scroll down to Danger zone" in multiple sections.


# 7.8 Summary

In this module, you learned about GitHub Projects. GitHub's project management tool connects your planning directly to the work your teams are doing in GitHub, and flexibly adapts to whatever your team needs at any point.

## What you've learned

You learned how to:

- Build an organization Project
- Automate and organize your Project

## Learn more

Here are some links to more information on the topics we discussed in this module:

- [On the go with GitHub Projects on GitHub Mobile (public beta)](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-your-project-on-github-mobile)
- [Using the API to Manage Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects)
- [Automating Projects using Actions](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/automating-projects-using-actions)
- [Archiving Items Automatically](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/archiving-items-automatically)


# 8 Communicate effectively on GitHub using Markdown

Learn to use Markdown to communicate with brevity, clarity, and expression.

# 8.1 Introduction

Markdown allows you to organize and emphasize what you're trying to communicate on GitHub.

A markup language, Markdown offers a lean approach to content editing. It defines a concise, lightweight syntax that strips out the overhead inherent to HTML, providing a more approachable creation experience. It's become the standard for sites like GitHub, and enjoys broad editor support in both client and browser forms.

In this module, you'll learn how to use Markdown in order to communicate more expressively throughout GitHub.

## Learning objectives

In this module, you'll:

- Use Markdown to add lists, images, and links in a comment or text file
- Determine where and how to use Markdown in a GitHub repository
- Learn about syntax extensions available in GitHub (GitHub-flavored Markdown)



# 8.2 What is Markdown?

Markdown is a markup language that offers a lean approach to content editing by shielding content creators from the overhead of HTML. While HTML is great for rendering content exactly how it was intended, it takes up a lot of space and can be unwieldy to work with, even in small doses. Markdown offers a great compromise between the power of HTML for content description and the ease of plain text for editing.

In this unit, we'll discuss Markdown's structure and syntax. We'll also cover features of GitHub-Flavored Markdown (GFM), which are syntax extensions that allow you to integrate GitHub features into content.

> **📝 Note**
> 
> This unit is intended to give you a taste of what Markdown is about. For a more in-depth review, reference the Markdown syntax description and GitHub-Flavored Markdown Spec articles in this module's Summary unit.

## Emphasize text

The most important part of any communication on GitHub is usually the text itself, but how do you show that some parts of the text are more important than others?

Using italics in text is as easy as surrounding the target text with single asterisks (*) or single underscores (_). Just be sure to close an emphasis with the same character with which you opened it. Be observant of how you combine the use of asterisks and underscores. Here are several examples:

```markdown
This is *italic* text.
This is also _italic_ text.
```

*Result:* This is *italic* text. This is also *italic* text.

Create bold text by using two asterisks (**) or two underscores (__).

```markdown
This is **bold** text.
This is also __bold__ text.
```

*Result:* This is **bold** text. This is also **bold** text.

You can also mix different emphases.

```markdown
_This is **italic and bold** text_ using a single underscore for italic and double asterisks for bold.
__This is bold and *italic* text__ using double underscores for bold and single asterisks for italic.
```

*Result:* *This is **italic and bold** text* using a single underscore for italic and double asterisks for bold. **This is bold and *italic* text** using double underscores for bold and single asterisks for italic.

To use a literal asterisk, precede it with an escape character; in GFM, that's a backslash (\\). This example results in the underscores and asterisks being shown in the output.

```markdown
\_This is all \*\*plain\*\* text\_.
```

*Result:* \_This is all \*\*plain\*\* text\_.

## Declare headings

HTML provides content headings such as the `<h1>` tag. In Markdown, this is supported via the `#` symbol. Just use one `#` for each heading level from 1 to 6.

```markdown
###### This is H6 text
```

*Result:*
###### This is H6 text

## Link to images and sites

Image and site links use a similar syntax.

```markdown
![Link an image.](/learn/azure-devops/shared/media/mara.png)
```

*Result:* ![Link an image.](/learn/azure-devops/shared/media/mara.png)

```markdown
[Link to Microsoft Training](/training)
```

*Result:* [Link to Microsoft Training](/training)

## Make lists

You can define ordered or unordered lists. You can also define nested items through indentation.

- Ordered lists start with numbers.
- Unordered lists can use asterisks or dashes (-).

Here's the Markdown for an ordered list:

```markdown
1. First
1. Second
1. Third
```

*Result:*
1. First
2. Second
3. Third

Here's the Markdown for an unordered list:

```markdown
- First
  - Nested
- Second
- Third
```

*Result:*
- First
  - Nested
- Second
- Third

## Build tables

You can construct tables using a combination of pipes (|) for column breaks and dashes (-) to designate the prior row as a header.

```markdown
First|Second
-|-
1|2
3|4
```

*Result:*

| First | Second |
|-------|--------|
| 1     | 2      |
| 3     | 4      |

## Quote text

You can create blockquotes using the greater than (>) character.

```markdown
> This is quoted text.
```

*Result:*
> This is quoted text.

## Fill the gaps with inline HTML

If you come across an HTML scenario not supported by Markdown, you can use that HTML inline.

```markdown
Here is a<br />line break
```

*Result:* Here is a<br />line break

## Work with code

Markdown provides default behavior for working with inline code blocks delimited by the backtick (`) character. When decorating text with this character, it's rendered as code.

```markdown
This is `code`.
```

*Result:* This is `code`.

If you have a code segment spanning multiple lines, you can use three backticks (```) before and after to create a fenced code block.

````markdown
```
var first = 1;
var second = 2;
var sum = first + second;
```
````

*Result:*
```
var first = 1;
var second = 2;
var sum = first + second;
```

GFM extends this support with syntax highlighting for popular languages. Just specify the language as part of the first tick sequence.

````markdown
```javascript
var first = 1;
var second = 2;
var sum = first + second;
```
````

*Result:*
```javascript
var first = 1;
var second = 2;
var sum = first + second;
```

## Cross-link issues and pull requests

GFM supports various shortcode formats to make it easy to link to issues and pull requests. The easiest way to do this is to use the format #ID, such as #3602. GitHub automatically adjusts longer links to this format if you paste them in. There are also additional conventions you can follow, such as if you're working with other tools or want to specify other projects/branches.

| Reference type | Raw reference | Short link |
|---------------|---------------|------------|
| Issue or pull request URL | https://github.com/desktop/desktop/pull/3602 | #3602 |
| # and issue or pull request number | #3602 | #3602 |
| GH- and issue or pull request number | GH-3602 | GH-3602 |
| Username/Repository# and issue or pull request number | desktop/desktop#3602 | desktop/desktop#3602 |

For more information, refer to the Autolinked references and URLs article in this module's Summary unit.

## Link specific commits

You can link to a commit by either pasting in its ID or simply using its secure hash algorithm (SHA).

| Reference type | Raw reference | Short link |
|---------------|---------------|------------|
| Commit URL | https://github.com/desktop/desktop/commit/8304e9c271a5e5ab4fda797304cd7bcca7158c87 | 8304e9c |
| SHA | 8304e9c271a5e5ab4fda797304cd7bcca7158c87 | 8304e9c |
| User@SHA | desktop@8304e9c271a5e5ab4fda797304cd7bcca7158c87 | desktop@8304e9c |
| Username/Repository@SHA | desktop/desktop@8304e9c271a5e5ab4fda797304cd7bcca7158c87 | desktop/desktop@8304e9c |

## Mention users and teams

Typing an @ symbol followed by a GitHub username sends a notification to that person about the comment. This is called an "@mention", because you're mentioning the individual. You can also @mention teams within an organization.

```markdown
@githubteacher
```

*Result:* @githubteacher

## Track task lists

You can create task lists within issues or pull requests using the following syntax. These can be helpful to track progress when used in the body of an issue or pull request.

```markdown
- [x] First task
- [x] Second task
- [ ] Third task
```

*Result:*
- [x] First task
- [x] Second task
- [ ] Third task

*Screenshot of a GitHub task list.*

## Slash commands

Slash commands can save you time by reducing the typing required to create complex Markdown.

You can use slash commands in any description or comment field in issues, pull requests, or discussions where that slash command is supported.

| Command | Description |
|---------|-------------|
| /code | Inserts a Markdown code block. You choose the language. |
| /details | Inserts a collapsible detail area. You choose the title and content. |
| /saved-replies | Inserts a saved reply. You choose from the saved replies for your user account. If you add %cursor% to your saved reply, the slash command places the cursor in that location. |
| /table | Inserts a Markdown table. You choose the number of columns and rows. |
| /tasklist | Inserts a tasklist. This slash command only works in an issue description. |
| /template | Shows all of the templates in the repository. You choose the template to insert. This slash command works for issue templates and a pull request template. |



# 8.3 Exercise - Communicate using Markdown

This exercise allows you to practice the content covered in this module: using Markdown to communicate effectively on GitHub.

## Get started

When you select the **Start the exercise on GitHub** button below, you're directed to a public GitHub template repository that prompts you to complete a series of small challenges. Before you can begin the exercise, complete the following tasks:

- Select the **Start course** button or the **Use this template** feature within the template repository. This prompts you to create a new repository. We recommend creating a public repository, because private repositories use Actions minutes. After you make your own repository from the template, wait about 20 seconds and refresh.

- Follow the instructions in the repository's README file to understand how the exercise works, its learning objectives, and how to successfully complete the exercise.

## When you finish the exercise in GitHub, return here to:

- Complete a quick knowledge check
- Review a summary of what you've learned
- Earn a badge for completing this module

> **📝 Note**
> 
> You don't need to modify any of the workflow files to complete this exercise. **Altering this workflow's contents can break the exercise's ability to validate your actions, provide feedback, or grade the results**.

## Start the exercise on GitHub

**[Start the exercise on GitHub]** *(button placeholder)*

https://github.com/skills/communicate-using-markdown


# 8.4 Module assessment

Choose the best response for each question, then select **Check your answers**.

## Check your knowledge

### 1. Which of the following Markdown snippets produces the text ***Hello, world!*** in bold italics?

- [ ] `*Hello, *world*!*`
- [ ] `**Hello, *world*!**`
- [x] **`***Hello, world!***`** ✅
- [ ] `### Hello, world!`

**Explanation:** To create bold italics text in Markdown, you need to use three asterisks (`***`) before and after the text. This combines both bold (two asterisks) and italic (one asterisk) formatting.

### 2. How do you print certain characters, like asterisks (`*`) and underscores (`_`), literally on your output?

- [ ] Use three in a row, like `***` or `___`.
- [x] **Escape them with a backslash, like `\*` or `\_`.** ✅
- [ ] Unfortunately, this isn't supported at this time.

**Explanation:** To display literal asterisks, underscores, and other special Markdown characters, you need to escape them with a backslash (`\`). For example, `\*` will display as `*` and `\_` will display as `_`.

### 3. Suppose there's an HTML snippet that you want to include on your GitHub Pages web site, but Markdown doesn't offer a way to render it. What should you do?

- [x] **Just add the HTML inline.** ✅
- [ ] Cut the content. If it's not supported in Markdown, then it's probably not worth including.
- [ ] Open an issue that requests Markdown support for your specialized scenario.

**Explanation:** Markdown supports inline HTML. If you come across an HTML scenario not supported by Markdown, you can use that HTML inline within your Markdown document. This is one of the key features that makes Markdown flexible and powerful.


# 8.5 Summary

In this module, you learned about Markdown and GitHub-flavored Markdown to communicate more expressively throughout GitHub.

## What you've learned

You learned:

- How to use Markdown to add lists, images, and links in a comment or text file
- Where and how to use Markdown in a GitHub repository
- Syntax extensions available in GitHub (GitHub-flavored Markdown)

Now that you know how to use Markdown on GitHub, learn to Create and host web sites by using GitHub Pages.

## Learn more

Here are some links to more information on the topics we discussed in this module.

- [Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [GitHub-Flavored Markdown Spec](https://github.github.com/gfm/)
- [Writing on GitHub](https://docs.github.com/en/get-started/writing-on-github)
- [GitHub Markdown emojis](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)
- [Autolinked references and URLs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls)
