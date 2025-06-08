



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
