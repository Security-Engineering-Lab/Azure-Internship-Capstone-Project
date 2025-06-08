



# Build community-driven software projects on GitHub
https://learn.microsoft.com/en-us/training/paths/build-community-driven-projects-github/

Whether you manage enterprise or open-source software projects, learn how GitHub enables you to build communities that foster communication and collaboration while reinforcing recommended guidelines, codes of conduct, and security best practices.

In this learning path, you'll learn how to:
* Build community involvement for both proprietary and open-source projects.
* Choose whether your idea is a good candidate for an open-source project.
* Move an existing project to GitHub from your personal computer or from a legacy version control system.
* Keep your GitHub repository secure.
* Contribute to an open-source project.

**Prerequisites**
* A GitHub account

# 1) Introduction to GitHub
# 2) Manage an InnerSource program by using GitHub
# 3) Create an open-source program by using GitHub best practices
Learn to create a successful open-source program by establishing contributor guidance, following proven processes, and by using community standards.

Learn to create a successful open-source program by establishing contributor guidance, following proven processes, and by using community standards.

Learning objectives
In this module, you will:

- Assess your organization's existing open-source efforts.
- Establish the goals of an open-source program.
- Create a repository for your open-source program, complete with contributing and communication guidelines, codes of conduct, templates, and maintainer guides.
- Abide by existing open-source licenses.
- Choose a license for releasing an open-source project.

# 3.1 Introduction

Open-source software programs have enjoyed major success for decades. Although there are different flavors of open-source licenses, they all share similar principles of transparency and inclusiveness that have produced some of the most powerful projects ever.

Suppose you're a leader at a company that has developed some substantial software projects. These projects have been proprietary since inception, but now you're investigating the possibility of open-sourcing one or more of them. You then try to determine which candidates would be best to publish. Now, you begin to realize that running a successful program is more than just uploading source code to a public repository. It requires careful collaboration with stakeholders from across the company. It also introduces a new mindset for exposing intellectual property in a way that might be entirely new for the company. Lastly, it involves lots of work to set up and maintain; but for some projects, you know it's worth it.

In this module, you'll learn how to create a successful open-source program by establishing contributor guidance, following proven processes, and by using community standards.

## Learning objectives

In this module, you'll:
- Assess your organization's existing open-source efforts
- Establish the goals of an open-source program
- Create a repository for your open-source program, complete with contributing and communication guidelines, codes of conduct, templates, and maintainer guides
- Abide by existing open-source licenses
- Choose a license for releasing an open-source project

## Prerequisites

- A GitHub account
- Ability to navigate and edit files in GitHub
- Familiarity with pull requests

This module builds on the concepts described in Manage an InnerSource program by using GitHub. It assumes you've already completed that module first.source project.

**Prerequisites**

* A GitHub account
* Ability to navigate and edit files in GitHub
* Familiarity with pull requests

This module builds on the concepts described in Manage an InnerSource program by using GitHub. It assumes you've already completed that module first.


# 3.2 How to establish an open-source program

Here, we discuss the key considerations for establishing an open-source program.

## What do we mean by "open-source?"

An open-source program is more than public access to a codebase. It's about opening up a living project for participation from anyone who wants to get involved. When executed properly for an appropriate project, an open-source program can help drive substantial improvements in your product's quality.

One of the key reasons companies open-source projects is that they want the community to get involved. Popular projects receive significant contributions from the community, and they get it for free.

It's not necessarily out of altruism. People and organizations consume projects because they see a personal or business benefit. When the project doesn't meet their needs or expectations, they might use the opportunity to address bugs or add features. Rather than hold these improvements back in private forks, they're compelled to contribute those changes back into the source repository to become part of the project baseline. This virtuous cycle of improvement is why many businesses produce software using the open-source model.

## Open-source goals

To recap, there are three dimensions to participation in open-source software:

- **Consumers**, who study or use the repositories of others.
- **Contributors**, who are actively involved in the improvement of the repositories of others.
- **Producers**, who build and maintain their own repositories that are open to others.

As organizations think more deeply about what they want to get out of each dimension, it's a good practice to take stock of where they are today. There are five process levels within each dimension.

*Diagram of open-source process levels.*

1. **Ad hoc**, which have no process in place. Success depends on individual efforts.
2. **Managed**, which have a partially documented process. Success depends on discipline.
3. **Defined**, which have a documented, standardized, and integrated process. Success depends on automation.
4. **Measured**, which have a quantitatively managed process. Success depends on measuring metrics against business goals.
5. **Optimized**, which have a process that's continually and reliably improving through both incremental and innovative changes. Success depends on reducing the risk of change.

To get a better understanding of where your organization stands, check out the Open-source self assessments.

## What should you open-source?

Many projects aren't destined for open-source greatness. While your criteria might vary based on your company's goals and process level, here are some recommended criteria to consider before open-sourcing a project:

- **Does your project contain intellectual property that you want to protect?** If so, then opening its source would give away its value. Don't open-source those kinds of projects unless you feel the benefits outweigh the risks.

- **Is the project in a stable state with good code quality?** The project doesn't have to be perfect, but potential contributors might walk away if the project is in terrible shape to begin with.

- **Is your project useful to people outside of your company?** If not, then you probably aren't getting any participation.

- **Are people outside your company able to contribute?** They need access to all project dependencies, build processes, and whatever else is needed to run the project. If they can't run it, they can't contribute.

- **Does your team have the bandwidth to support an open-source program?** If not, wait until you do. If you open-source a project and don't support it, you might lose your opportunity to build a trusting community.

These questions are just a few of the most common considerations. Your organization might have other business or compliance issues to keep in mind.

## Designing an open-source program

Running an open-source program is similar to running an InnerSource program, but for a public audience. As a result, there are a few more considerations.

### Setting community expectations

Files like `README.md` and `CONTRIBUTING.md` are even more important because they're being exposed to people who don't have your organizational context. They need to be evaluated from the perspective of someone outside the company to ensure clarity.

In addition, your code of conduct is an important policy to express. The standard is to add a `CODE_OF_CONDUCT.md` file to your repository's root and use it to explain the behavior expected from participants in your community. Multiple groups in your organization should review this document, including your legal team. Fortunately, there are many standard codes of conduct available from which to start. Many projects use these codes as-is without modification. Learn more in the Guide to open-source codes of conduct.

### Preparing employees to maintain a repository

Employees might not have experience working with the open-source community. To help them prepare, we recommend that the company offer a set of guides that cover the key things everyone should know before they get started. These guides should be posted to an internal repository or portal that's regularly maintained and only accessible to company employees. The following guides are a few of the most important:

- **A "Should we open-source this project?" guide** that provides a framework for deciding whether or not a candidate project should be open-sourced. This guide could be structured as a flowchart, set of questions, or list of considerations.

- **A setup checklist** that includes all of the work items a team needs to complete before and after the launching an open-sourced project. This list should include acquiring approval to open-source the project, code reviews to ensure sensitive data is removed before the project goes live, a trademark or open-source project search to ensure there isn't a naming conflict, and so on.

- **A contact list** for key people in your organization that might need to be contacted in case direct support from the maintainers is required. This list should include people from software security, site security, legal, public relations, and so on.

- **A link to a starter repository** that can be cloned as a starting point. It should contain a sample README, license, code of conduct, contributing guide, and any other supporting files every open-source project from your company needs to have. It shouldn't contain anything you wouldn't want accidentally pushed to a public audience.

- **A maintainer's guide** that explains the responsibilities a maintainer has in keeping the repository healthy. These responsibilities include keeping repository documentation up to date, ensuring issues and pull requests get the attention of the right people in a timely manner, and so on.

- **A communications guide** that offers repository maintainers guidance for some of the topics you'd prefer not to include in public files like `README.md`, `CONTRIBUTING.md`, or `CODE_OF_CONDUCT.md`. These subjects might be sensitive business topics, such as not discussing competitors; or more general conduct topics, like how to appropriately recognize top contributors.

- **An internal FAQ** that provides approved answers to common questions. This list is especially useful if there are legal subtleties to the topics your company might discuss in the course of maintaining an open-source program.

- **A license policy** that lists which licenses have been approved or rejected by the legal department for open-source consuming or contributing.

# 3.3 Exercise - Create an open-source program

In this guide, you'll learn more about the world of open source and the steps you can take to get ready to launch your own open source project.

The first two sections titled **The "what" and "why" of open source** and **Should I launch my own open source project?** mostly cover content that we already discussed in the previous unit. Feel free to review these sections, but we'll focus on the following sections for this exercise.

* Launching your own open source project
* Naming and branding your project
* Your prelaunch checklist
 
When you've finished the exercise in this open source guide, return here for:

* The benefits of open source
* A quick knowledge check
* A summary of what you've learned
* To earn a badge for completing this module

https://opensource.guide/starting-a-project/#launching-your-own-open-source-project


# 3.4 Describe the benefits of the open-source community

Here, we describe some of the benefits of the open-source community on GitHub. Innovation is built on top of open-source software: 80-90% of any new application created today consists of open-source code. The remaining 10-20% is where you can focus on delivering business value. To compete in the market, you have to use open source, or you lose your head start by developing your own solutions.

## Set up your project and community for success

Let's look forward into the future and suppose that your organization has decided to create an open-source program. After a few months, you've attracted an engaged community of contributors. Congratulations! What do you do next?

Building a welcoming community for your project is a long-term investment in your open-source program. Healthy, safe, and welcoming communities are the power behind the open-source ecosystem. People and their communities are often the main reason for folks to contribute—or to not contribute—to open-source projects.

You want a team of people to move critical infrastructure and popular dependencies forward, even if they're distributed across areas and time zones, rather than an individual. That way, even if a project isn't supported commercially and there's no SLA, you can still count on the community's support for a project's maintenance. Similarly, you wouldn't want your business processes to depend on a single person. What if Bob from accounting gets sick, and salaries can't be paid out until they return because they're the only one who knows how to operate the software?

As folks engage with and interact with your open-source projects, there are some that transition from users to contributors and maintainers. We call the steps involved in this transition "the contributor's journey". As the project maintainers, it's critical that you're mindful of the contributor's journey, because it's crucial for any open-source project's sustainability.

Your goal when running an open-source program is to help reduce friction and enhance the contributors' experience. Even if someone is a casual or one-time contributor, your job is making it easy to contribute to your project. The open-source community has developed an informal way to share meta information about the project, like how to contribute effectively, expected conduct between contributors, and so on. These ways are typically added to files called README and CONTRIBUTING. Think of your project's README as the landing page for your project, rather than a set of instructions to install your tool or framework.

Use your CONTRIBUTING file to provide details about the type of contributions you're looking for and how you review and accept them. Also, explain the criteria for getting triage and commit rights to the repository.

## Open communication

When you work on an open-source project, the documentation focus is often on technical documentation. A great way to include the community in your project is going beyond the technical docs. Items that you can also openly document include your project's roadmap and governance, contribution processes, and meeting minutes.

You can document important discussions and gather community and contributors' feedback using GitHub discussions. This way, you can start discussions with your team and the broader community. You can even reference these discussions in Issues and Pull Requests.

Keeping communication public—except for certain cases such as code-of-conduct incidents—ensures everyone has the same information.

## Project community profiles on GitHub

To see how your project compares to community standards, navigate to the main page of your repository. Under your repository name, select **Insights**. In the left sidebar, select **Community Standards**. Almost all the files are right there to add. Think of adding templates for Issues and Pull Requests, further taking away barriers for people to report bugs, submit code, and just getting involved with your project.

For more community best practices, check out GitHub's Open Source Guides.


# 3.5 Summary

In this module, you learned how to create a successful open-source program by establishing contributor guidance, following proven processes, and by using community standards.

You learned about assessing your organization's existing open-source efforts and establishing an open-source program's goals. You now know how to create a repository for your open-source program, complete with contributing and communication guidelines, codes of conduct, templates, and maintainer guides. You've explored the community features on GitHub and the existing open-source licenses, and you should feel comfortable choosing a license when releasing an open-source project.

Now that you have an open-source program, learn to Maintain a secure repository by using GitHub best practices.

## Learn more

Here are some links to more information on the topics we discussed in this module.

* Open-source self assessments
* Make a README site
* Awesome README examples
* Guide to open-source codes of conduct


# 4 Upload your project by using GitHub best practices

Learn to upload your existing project to GitHub.

# 4.1 Introduction

GitHub is home to millions of software projects, with more joining every day. There are so many great reasons to host your project on GitHub, but getting your project up and running might seem daunting.

Suppose you're working on a software project that is starting to really take shape. Other people want to contribute, and it would be great to get their help. However, you still want to maintain control over the direction of the project, but in a way that doesn't slow down other people from improving it. GitHub offers you all of these features and more.

In this module, you learn how to prepare and upload a project to GitHub.

**Note**  
If you're uploading a project that is already hosted in a version-control system, consider completing **Migrate your repository by using GitHub best practices** instead.

## Learning objectives

In this module, you'll:

* Identify where your code is stored.
* Introduce code to a repository.
* Create important Git files like a `.gitignore`.
* Identify important next steps to manage your repository and add community involvement.

## Prerequisites

* A GitHub account

# 4.2 How do I prepare and upload an existing project to GitHub?

In this unit, we discuss the important considerations for uploading a project to GitHub.

## Why upload to GitHub?

There are volumes of literature extolling the virtues of GitHub, and it's beyond the scope of this module to convince you to join. However, in this module we recap some of the key benefits within the context of subjects you need to consider when planning your upload.

### Version control

GitHub exclusively uses Git, arguably the best version-control system around. However, Git is incredibly sophisticated and can create some complex scenarios for working with code that your team might not be experienced with. Branches and pull requests are a fundamental part of day-to-day life for developers using Git, so understanding when and how to use them effectively is necessary to be successful on GitHub. It's worthwhile for your team to first be familiar with the GitHub flow so you can hit the ground running.

### Keep your code in the cloud

A large amount of project code is still stored exclusively on developer machines. When you upload to GitHub, you're moving your code to GitHub's cloud platform, where team members can easily access it from anywhere. This change offers a good opportunity to review your team's policy for the kinds of files and data you keep in version control. As a best practice, you should assume that anything you commit to GitHub is potentially compromised. So, be sure not to include sensitive data, such as API keys, passwords, or other files containing comparable information.

**Note**

GitHub offers both public and private repositories, as well as granular access controls for different parts of a repository. This lets you control to whom your projects are visible, as well as what actions a given user can perform.

### Collaboration

GitHub offers excellent support for team collaboration through features like issues, pull requests, and code reviews. However, the GitHub flow might differ from the practices to which your team is currently accustomed. It's a good idea to consider how your team might adapt to GitHub, and whether or not you should retain any existing processes.

If your project is an open-source project that allows outside contributors, there's no better option than GitHub for maximizing those benefits.

## Upload to GitHub

### Plan considerations

The most important thing to consider before executing your upload to GitHub is whether you need to retain anything beyond the current state of your source. For example, you might use a spreadsheet or project-management software to track bugs you plan to fix. Support for migrating these items varies by platform, and is generally available from community projects. This module doesn't cover migrating that type of data.

### Handle binary files currently stored in your project

As a best practice, GitHub repositories should be limited to the files necessary for building projects. Avoid committing large binary files, such as build artifacts. Binary files like spreadsheets and presentations are better suited to be tracked on portals that understand how to serve and version them properly. If you have a need to version large binary files, consider using the Git extension Git LFS (Large File Storage).

### Create important Git files like .gitignore

Git supports `.gitignore` files to help enforce version-control file policies. These files define the search patterns used to exclude files and folders from source-control tracking. The following example recursively excludes any folders called Bin or bin, and their contents, from source-control tracking.

**.gitignore**

```
[Bb]in/
```

Learn more about [Ignoring files](). Also check out the collection of starter `.gitignore` files offered for various platforms in the [gitignore repository]().

There are several other files commonly used in GitHub projects to explain different policies to repository consumers and contributors. Even if your project is private and restricted to a limited audience, it can still be useful to explicitly articulate these policies. While none of these files are required, a few of the common ones are listed here.

| File | Purpose |
|------|---------|
| `README.md` | The landing page for the directory. This page is rendered when its directory is viewed on GitHub. |
| `LICENSE.md` | This file contains the license under which the code is provided. |
| `CONTRIBUTING.md` | Explains how users should contribute to the project, such as pull request expectations. |
| `SECURITY.md` | Explains the security policy for the project. This file provides guidance to users that want to submit sensitive security-related code or feedback that shouldn't be publicly disclosed before being addressed. |

Learn more about [Setting up your project for healthy contributions]().

### Upload your project to GitHub

Once your repository is prepared for upload, create a repository on GitHub. Once created, navigate to the **Code** tab of your GitHub repository. This view provides you with several ways to get your project code uploaded.

*Screenshot of importing code to a GitHub repository.*

We recommend that you use the git client or a Git-friendly tool to upload your source. Alternatively, you can manually upload your files using the creating a new file link. Over the long run, you're likely to find that using a git client is the best way to manage changes, branches, and more.



# 4.3 Exercise - Upload your project to GitHub

You can import repositories to GitHub using GitHub Importer, the command line, or external migration tools.

## About GitHub Importer
If you have source code in Subversion, Mercurial, Team Foundation Version Control (TFVC), or another Git repository, you can move it to GitHub using GitHub Importer. GitHub Importer is a tool that quickly imports source code repositories, including commits and revision history, to GitHub for you.

During an import, depending on the version-control system you're importing from, you can perform some of the following tasks. Authenticate with your remote repository, update commit author attribution, import repositories with large files, or remove large files if you don't want to use Git Large File Storage.

| Import Action | Subversion | Mercurial | TFVC | Git |
|---------------|------------|-----------|------|-----|
| Authenticate with remote repository | X | X | X | X |
| Update commit author attribution | X | X | X |  |
| Move large files to Git Large File Storage | X | X | X |  |
| Remove large files from your repository | X | X | X |  |

### Importing a repository with GitHub Importer
If you have a project hosted on another version control system, you can automatically import it to GitHub using the GitHub Importer tool. GitHub Importer isn't suitable for all imports. For example, if your existing code is hosted on a private network, our tool isn't able to access it. In these cases, we recommend importing using the command line for Git repositories or an external source-code migration tool for projects imported from other version-control systems.

If you'd like to match the commits in your repository to the authors' GitHub user accounts during the import. First, make sure that every contributor to your repository has a GitHub account before you begin the import.

Repositories and individual files are subject to size limits. For more information, check out About large files on GitHub.

Follow these steps to import a repository:

1. In the upper-right corner of any page, select +, and then select Import repository.

   Screenshot of the import repository button.

2. Under "Your old repository's clone URL," type the URL of the project you want to import.

   Screenshot of the old repository URL textbox.

3. Choose your user account or an organization to own the repository, then type a name for the repository on GitHub.

   Screenshot of the new import repository owner name.

4. Specify whether the new repository should be public or private. For more information, check out Setting repository visibility.

   Screenshot of the new repository public or private options.

5. Review the information you entered, then select Begin import.

   Screenshot of the begin import button for a new repository import.

6. If your old project was protected by a password, type your sign-in information for that project, then select Submit.

   Screenshot of the location to input your old repository credentials importer.

7. If there are multiple projects hosted at your old project's clone URL, choose the project you'd like to import, then select Submit.

   Screenshot of a selection of projects found at the same URL. project importer.

8. If your project contains files larger than 100 MB, choose whether to import the large files using Git Large File Storage, then select Continue.

   Screenshot of files suitable for Git LFS importer.

When the repository is fully imported, you receive an email.

### Updating commit author attribution with GitHub Importer
During an import, you can match commits in your repository with the GitHub account of the commit author. GitHub Importer looks for GitHub users whose email addresses match the authors of the commits in the repository you're importing. You can then connect a commit to its author using their email address or the author's GitHub username.

#### Updating commit authors
Follow these steps to update a commit author:

1. After importing your repository, on the import status page, select Match authors.

   Screenshot of the match authors button.

2. Next to the author whose information you'd like to update, select Connect.

   Screenshot of the connect commit author process.

3. Type the email address or GitHub username of the author, then press Enter.

#### Attributing commits to a GitHub user with a public email address
If an author of a commit in your imported repository has a GitHub account associated with the email address they used to author the commits, and they don't set their commit email address as private. Then, GitHub Importer matches the email address associated with the commit to the public email address associated with their GitHub account, and attributes the commit to their GitHub account.

#### Attributing commits to a GitHub user without a public email address
If the author of a commit in your imported repository doesn't set a public email address on their GitHub profile, or set their commit email address as private. Then, GitHub Importer might not be able to match the email address associated with the commit with their GitHub account.

The commit author can resolve this issue by setting their email address as private. Their commits are then attributed to `<username>@users.noreply.github.com`, and the imported commits are associated with their GitHub account.

#### Attributing commits using an email address
If the author's email address isn't associated with their GitHub account, they can add the address to their account after the import, and the commits will be correctly attributed.

If the author doesn't have a GitHub account, GitHub Importer attributes their commits to the email address associated with the commits.

## Importing a GitHub repository using the command line
If GitHub Importer isn't suitable for your purposes, such as if your existing code is hosted on a private network, then we recommend importing using the command line.

Before you start, make sure you know:

* Your GitHub username
* The clone URL for the external repository, such as https://external-host.com/user/repo.git or git://external-host.com/user/repo.git (perhaps with a user@ in front of the external-host.com domain name)

For purposes of demonstration, we use:

* An external account named ext-user
* An external Git host named https://external-host.com
* A GitHub personal user account named ghuser
* A repository on GitHub.com named repo.git

Follow these steps to import your external repository:

1. Create a new repository on GitHub. You import your external Git repository to this new repository.

2. On the command line, make a "bare" clone of the repository using the external clone URL. This command creates a full copy of the data, but without a working directory for editing files, and ensures a clean, fresh export of all the old data.

   **Bash**

   ```
   $ git clone --bare https://external-host.com/ext-user/repo.git
   #Makes a bare clone of the external repository in a local directory 
   ```

3. Push the locally cloned repository to GitHub using the "mirror" option, which ensures that all references, such as branches and tags, are copied to the imported repository.

   **Bash**

   ```
   $ cd repo.git
   $ git push --mirror https://github.com/ghuser/repo.git
   #Pushes the mirror to the new repository on GitHub.com 
   ```

4. Remove the temporary local repository.

   **Bash**

   ```
   $ cd ..
   $ rm -rf repo.git 
   ```

## Adding locally hosted code to GitHub
If you have existing source code or repositories stored locally on your computer or private network, you can add them to GitHub by typing commands in a terminal. Either by typing Git commands directly, or by using GitHub CLI.

GitHub CLI is an open source tool for using GitHub from your computer's command line. GitHub CLI can simplify the process of adding an existing project to GitHub using the command line. To learn more about GitHub CLI, check out About GitHub CLI.

### Adding a local repository to GitHub with GitHub CLI
Follow these steps to add a local repository with GitHub CLI:

1. In the command line, navigate to the root directory of your project.

2. Initialize the local directory as a Git repository.

   **Bash**

   ```
   git init -b main
   ```

3. Stage and commit all the files in your project.

   **Bash**

   ```
   git add . && git commit -m "initial commit"
   ```

4. To create a repository for your project on GitHub, use the gh repo create subcommand. When prompted, select Push an existing local repository to GitHub and enter the desired name for your repository. If you want your project to belong to an organization instead of your user account, specify the organization name and project name with organization-name/project-name.

5. Follow the interactive prompts. To add the remote and push the repository, confirm yes when asked to add the remote and push the commits to the current branch.

   Alternatively, to skip all the prompts, supply the path to the repository with the --source flag and pass a visibility flag (--public, --private, or --internal). For example, gh repo create --source=. --public. Specify a remote with the --remote flag. To push your commits, pass the --push flag. For more information about possible arguments, reference the GitHub CLI manual.

### Adding a local repository to GitHub using Git
Follow these steps to add a local repository using Git:

1. Create a new repository on GitHub.com. To avoid errors, don't initialize the new repository with README, license, or gitignore files. You can add these files after your project is pushed to GitHub.

   Screenshot of new repository creation.

2. Open Git Bash.

3. Change the current working directory to your local project.

4. Initialize the local directory as a Git repository.

   **Bash**

   ```
   $ git init -b main
   ```

5. Add the files in your new local repository. This command also stages them for the first commit.

   **Bash**

   ```
   $ git add .
   # Adds the files in the local repository and stages them for commit. To unstage a file, use 'git reset HEAD YOUR-FILE'.
   ```

6. Commit the files that are staged in your local repository.

   **Bash**

   ```
   $ git commit -m "First commit"
   # Commits the tracked changes and prepares them to be pushed to a remote repository. To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.
   ```

7. At the top of your repository on GitHub.com's Quick Setup page, select the Copy button to copy the remote repository URL.

   screenshot copy remote repository url quick setup

8. In the Command prompt, add the URL for the remote repository. Your local repository is pushed to this location.

   **Bash**

   ```
   $ git remote add origin <REMOTE_URL> 
   # Sets the new remote
   $ git remote -v
   # Verifies the new remote URL
   ```

9. Push the changes in your local repository to GitHub.com.

   **Bash**

   ```
   $ git push origin main
   # Pushes the changes in your local repository up to the remote repository you specified as the origin
   ```

## Source code migration tools
You can use external tools to move your projects to GitHub. We recommend using GitHub Importer to import projects from Subversion, Mercurial, Team Foundation Version Control (TFVC), or another Git repository. You can also use these external tools to convert your project to Git.

### Importing from Subversion
In a typical Subversion environment, multiple projects are stored in a single root repository. On GitHub, each of these projects typically map to a separate Git repository for a user account or organization. We suggest importing each part of your Subversion repository to a separate GitHub repository if:

* Collaborators need to check out or commit to that part of the project separately from the other parts
* You want different parts to have their own access permissions

We recommend these tools for converting Subversion repositories to Git:

* git-svn
* svn2git

### Importing from Mercurial
We recommend hg-fast-export for converting Mercurial repositories to Git.

### Importing from TFVC
We recommend git-tfs for moving changes between TFVC and Git.

For more information about moving from TFVC (a centralized version control system) to Git, see Migrate to Git from centralized version control.


# 4.4 Module assessment

Choose the best response for each question.

## Check your knowledge

### 1.
**What kind of files are best stored in GitHub?**

- Large binary files, like videos.
- Binary project files, like spreadsheets and presentations.
- **✅ Text files, like source code.**

**Explanation:** GitHub is designed for text-based files, particularly source code. Text files work well with Git's version control system, allowing for meaningful diffs, merging, and collaboration. Large binary files and presentations are not ideal for GitHub repositories as they don't benefit from version control features and can make repositories large and slow.

### 2.
**Why is a `.gitignore` file important to your repository?**

- It defines which users aren't allowed to participate in your repository discussions and pull requests.
- **✅ It helps you enforce policy around which files should be excluded from version control.**
- It's just a token file required by GitHub to make sure you're following the migration instructions closely. If you ignore it, your repository migration fails.

**Explanation:** The `.gitignore` file specifies which files and directories Git should ignore and not track. This is crucial for excluding temporary files, build artifacts, sensitive data, and other files that shouldn't be in version control. It has nothing to do with user permissions or migration requirements.

### 3.
**Which of the following methods is not a valid way to upload new project files to GitHub?**

- **✅ Email a password protected zip of your project to GitHub support along with instructions for the repository's creation. Be sure to include the zip password in the same email.**
- Use the `git` client or other Git-friendly tool.
- Use the browser interface at github.com.

**Explanation:** GitHub doesn't accept project uploads via email to support. This would be insecure and not part of their workflow. Valid methods include using Git commands from the command line, GitHub CLI, GitHub Desktop, or the web interface at github.com for smaller uploads.

**Submit answers**


# 4.5 Summary

In this module, you learned how to upload your existing project to GitHub.

You learned about:

* Identifying where your code is stored.
* Introducing code to a repository.
* Creating important Git files like `.gitignore`.
* Identifying important next steps for managing your repository and adding community involvement.

Now that you have your project on GitHub, learn to Manage an InnerSource program by using GitHub and Create an open-source program by using GitHub best practices.

## Learn more

Here are some links to more information on the subjects we discussed in this module:

* Ignoring files with .gitignore
* .gitignore repository for popular platforms
* Setting repository visibility


# 5 Migrate your repository by using GitHub best practices

Learn to move your existing project to GitHub from a legacy version control system.

# 5.1 Introduction

GitHub is home to millions of software projects, with more joining every day. There are so many great reasons to host your project on GitHub, but getting there from a legacy version-control system might seem daunting.

Suppose you're managing the version control for a project and want to move to GitHub. You probably have many questions, like "How do I get started?" and "How is GitHub different from what I use now?" These concerns are valid, but the good news is that you can effectively host virtually any project on GitHub.

In this module, you learn how to prepare and migrate a project to GitHub from a legacy version-control system.

**Note**  
If you're uploading a project that is not yet hosted in a version-control system, consider completing the **Upload your project by using GitHub best practices** module instead.

## Learning objectives

In this module, you'll:

* Prepare your project for a successful migration.
* Handle any binary files currently stored in your project.
* Create important Git files like a `.gitignore`.
* Import your project to GitHub.

## Prerequisites

* A GitHub account

We recommend that you complete the Introduction to GitHub module before beginning this module.


# 5.2 How do I migrate an existing project to GitHub?

Here, we discuss the important considerations for migrating a project to GitHub from a legacy version-control system.

## Why migrate to GitHub?

There are volumes of literature extolling the virtues of GitHub. It's beyond the scope of this module to convince you to move. But, we can recap some of the key benefits within the context of topics you need to consider when planning your migration.

### Version control

GitHub exclusively uses Git, arguably the best version-control system around. However, Git is incredibly sophisticated and can present some complex scenarios for working with code with which your team might not be experienced. Branches and pull requests are a fundamental part of day-to-day life for developers using Git, so understanding when and how to use them effectively is necessary to being successful on GitHub. It's worthwhile for your team to first become familiar with the GitHub flow so you can hit the ground running.

### Keep your code in the cloud

A large amount of project code is still stored in legacy version-control systems behind corporate firewalls. When you migrate to GitHub, you're moving your code to GitHub's cloud platform, where team members can easily access it from anywhere. This migration offers a good opportunity to review your team's policy for the kinds of files and data you keep in version control. As a best practice, you should assume that anything you commit to GitHub is compromised. Be sure not to include sensitive data such as API keys, passwords, or other files containing comparable information.

**Note**

GitHub offers both public and private repositories, as well as granular access controls for different parts of a repository. This lets you control to whom your projects are visible, as well as what actions a given user can perform.

### Collaboration

GitHub offers excellent support for team collaboration through features like issues, pull requests, and code reviews. However, the GitHub flow might differ from the practices to which your team is currently accustomed. It's a good idea to consider whether the team plans to adapt to GitHub, retain its given process, or meet somewhere in the middle before completing the migration.

If your project is an open-source project that allows outside contributors, there's no better option than GitHub for maximizing the benefits.

## Migrating to GitHub

### Planning considerations

The most important consideration before executing your migration to GitHub is whether you need to retain anything beyond the current state of your source. If you're satisfied with starting a new project with just your current source as-is, your best option is to treat it like a new project and upload the source to your repository.

However, if you want to retain version-control history, you need to import using the GitHub Migrator tool. For more information about the import support for different version-control platforms, check out Importing data from third-party version control systems.

Beyond Git data, you might also want to retain issues, pull requests, or other data. Support for these items varies by platform, and is generally available from community projects. This module doesn't cover migrating non-Git data.

### Handling binary files currently stored in your project

As a best practice, GitHub repositories should be limited to the files necessary for building projects. Avoid committing large binary files such as build artifacts. Binary files like spreadsheets and presentations are better suited to be tracked on portals that understand how to serve and version them properly. If you need to version large binary files, consider using the Git LFS (Large File Storage) Git extension.

### Creating important Git files like .gitignore

Git supports `.gitignore` files to help enforce version-control file policies. These files define the search patterns used to exclude files and folders from source-control tracking. The following simple example recursively excludes any folders called Bin or bin, and their contents, from source-control tracking:

**.gitignore**

```
[Bb]in/
```

You can learn more about [Ignoring files](). You can also check out the collection of starter `.gitignore` files offered for various platforms in the [gitignore repository]().

There are several other files commonly used in GitHub projects to explain different policies to repository consumers and contributors. Even if your project is private and restricted to a limited audience, it can still be useful to explicitly articulate these policies. While none of these files are required, we listed a few of the common ones here.

| File | Purpose |
|------|---------|
| `README.md` | The landing page for the directory. This page is rendered when its directory is viewed on GitHub. |
| `LICENSE.md` | The license that the code is provided under. |
| `CONTRIBUTING.md` | Explains how users should contribute to the project, such as pull-request expectations. |
| `SECURITY.md` | Explains the security policy for the project. Provides guidance to users wanting to submit sensitive security-related code or feedback that shouldn't be publicly disclosed before being addressed. |

Learn more about [Setting up your project for healthy contributions]().

### Importing your project to GitHub

Once you prepare your repository for migration, navigate to the **Code** tab of your GitHub repository. Use the **Import code** option to specify the source repository.

*Screenshot of importing code to a GitHub repository.*

The GitHub Migrator tool takes care of the rest.

*Screenshot of the GitHub Migrator tool.*

