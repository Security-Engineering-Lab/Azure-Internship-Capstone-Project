

# Get started with Azure DevOps
https://learn.microsoft.com/en-us/training/paths/evolve-your-devops-practices/

DevOps is the union of people, process, and products to enable continuous delivery of value to your end users. Azure DevOps is a set of services that gives you the tools you need to do just that. With Azure DevOps, you can build, test, and deploy any application, either to the cloud or on premises. DevOps practices that enable transparency, cooperation, continuous delivery and continuous deployment become embedded in your software development lifecycle.

This learning path is part of a series. You can choose the topics you're most interested in or progress through each of them. Here are the learning paths in this series:

**Part 1:** Get started with Azure DevOps

**Part 2:** Build applications with Azure DevOps

**Part 3:** Deploy applications with Azure DevOps

In this learning path, you will get started on your DevOps journey. You will:

* See how value stream maps can help you evaluate your current processes and technologies
* Sign up for your free Azure DevOps organization
* Learn how to plan and track work items using Azure Boards
* Optimize sprint workloads across multiple Agile teams

**Prerequisites**
- None


# 1 Assess your existing software development process

Use a value stream map to help you examine your existing processes and technologies.

# 1.1 Introduction

Do you want to improve your release process? Maybe you want to increase the frequency of your releases or the quality of your software. Perhaps you want to get rid of some manual processes, and move toward a more automated approach. Whatever your goals, Azure DevOps can help.

## Learning objectives

After completing this module, you'll be able to:

* Explain the purpose of value stream maps (VSMs).
* Use a VSM to get a sense of where you can improve your release process.
* Compute the activity ratio, or overall efficiency, for your processes.


# 1.2 Meet the team

DevOps has many features and tools to help a team collaborate and improve its processes. Your journey through DevOps begins with an introduction to our fictitious software team members, who are discovering that they need to improve their release process.

Tailspin Toys, or Tailspin for short, is a video game company. Tailspin hosts its game servers and websites in an on-premises datacenter. The company just celebrated the release of a new racing game. They'll be releasing a space shooter game called Space Game in the coming months.

The team with which you'll be working builds websites to support new game titles. These websites provide information about the game, ways to get it, and leaderboards that show top scores. Each website must go live the same day the game is released, which requires coordination among the teams and puts some extra pressure on the web team.

The Space Game website is a .NET app written in C# that's deployed to Linux. The website isn't finished yet, but here's what it looks like right now:

![](https://learn.microsoft.com/en-us/training/azure-devops/assess-your-development-process/media/2-space-game-top.png)

*Screenshot of a web browser showing the Space Game website. The page shows graphics from the game and a button to download the game.*

And here's what the leaderboard looks like:

![](https://learn.microsoft.com/en-us/training/azure-devops/assess-your-development-process/media/2-space-game-leaderboard.png)
*Screenshot of a web browser showing the Space Game leaderboard. The leaderboard shows the top 10 players and their high scores.*

You can filter the leaderboard by mode or by game map. You can also select a player's name to see their profile and game achievements:

![](https://learn.microsoft.com/en-us/training/azure-devops/assess-your-development-process/media/2-player-profile.png)

*Screenshot of the Space Game website showing the top player's profile information.*

Here are your team members:

**Andy** is the development lead who's been working with computers since he was a kid. He enjoys working on personal coding projects in his spare time. Andy always wishes he had more spare time.

*A cartoon depiction of Andy.*

**Amita** is in QA. She's calm, which helps with some temperamental developers. She's good at organizing and setting priorities and lives to find edge cases.

*A cartoon depiction of Amita.*

**Tim** is in operations. He likes practical solutions and he's very cautious (although some people might use the word "paranoid"), which makes sense because he's the person who gets the 3 A.M. call when something goes wrong.

*A cartoon depiction of Tim.*

**Irwin** is the product manager. He's been in the video game industry for decades. Irwin acts friendly towards the development teams, but everyone knows he favors a tight schedule over people. Irwin has a relatively fixed mindset, but if there's anything that can help teams get games to market faster with less effort, he's all ears.

*A cartoon depiction of Irwin.*

**Mara** is new. She just joined Tailspin as a developer and reports to Andy. She joined Tailspin because she likes games and she thought a smaller company would have lots of opportunity for innovation. She's a big fan of DevOps.

*A cartoon depiction of Mara.*

## Good morning

The team's product manager, Irwin, has called everyone into a meeting, and he's in a bad mood. The leaderboard for the racing game was updated with several new features, and he showed it at a local gaming group. Players' reactions were disappointing, to say the least. He reads off a list of the top problems:

* Some features work correctly for only some game modes.
* Updating the leaderboard takes too long, even with a few players.
* Multiple scores per player show up as multiple players.
* The new ranking feature returns incorrect results.
* There's no way to group scores according to a specific date or game session.
* It took months to produce the new release, and it's broken.

He demands, "How long before these problems are fixed?"

**Andy thinks:** *I bet it'll take me a month to write that code.*

**Amita thinks:** *It'll take me at least a week to test this code, and I can't start until Andy is finished. Plus he always wants to sneak in new code.*

**Tim thinks:** *It'll take me at least a week to set up the environments and deploy this code to production. I can't start until Amita is finished, and she's never willing to call something a release candidate.*

**Mara wonders:** *Was taking this job a mistake?*

Andy looks around at his teammates and says, "We'll get back to you."


# 1.3 The team's release process

The first step to setting up a DevOps practice is to assess your current process. This means analyzing:

* Your existing artifacts, like deployment packages and NuGet, and your container repositories.
* Your existing test-management tools.
* Your existing work-management tools.
* Recommending migration and integration strategies.

Let's do that with the Tailspin team and see how DevOps can help.

After Irwin the product manager leaves, Amita says, "We need help. I don't know when these fixes are due, but I do know it's soon. We're not set up for a fast turnaround. Plus, the new *Space Game* website will have to wait until we get this mess solved, and that game is coming up fast."

Andy looks at Mara. "This information is a lot to take in during your first few weeks."

"That's okay," Mara answers. "Maybe you can explain to me how things work around here. How does a game move from dev to production?"

"That's a great question," says Andy. "I'm not sure we can give you a simple answer, but let's try."

The team decides to go to a coffee shop to relax and have an informal discussion. Together, they try to figure out why they're having so many problems.

Over coffee, Mara listens and tries to take notes. There's a lot of information, and it's not organized. Mara's overall thoughts about the team are:

* They use a waterfall approach. Management sets the priorities. Developers write code and hand the build off to QA. QA tests and then hands off to ops for deployment.
* The waterfall approach could be acceptable for a small team, but here the goals aren't always clear. They also seem to change frequently.
* Testing is delayed until late in the process. That means it's harder and more expensive to fix bugs and make changes.
* There's no clear definition of what *done* means. Each team member has their own idea. There's no overall business goal that everyone agrees on.
* Some code is in a centralized version-control system. Many tools and scripts exist only on network file shares.
* There are many manual processes.
* Communication is haphazard and depends on email, Word docs, and spreadsheets.
* Feedback is also infrequent and inconsistent.
* On the plus side, the team seems to get along, and they want to make things better.

When she looks at her pile of notes, Mara knows she needs to organize all this information. Organizing it makes it easier to evaluate the processes. She's convinced a DevOps approach solves many of the team's problems, but she needs a way to present her case to the team.

A DevOps practice often begins with understanding your existing processes. From there, you can evaluate what's working well, what's not, and focus on what to fix first.

![](https://learn.microsoft.com/en-us/training/azure-devops/assess-your-development-process/media/3-taking-notes.jpg)

Mara asks, "Have any of you ever completed a *value stream mapping* exercise?"

Andy rolls his eyes, Amita sighs, and Tim says, "We don't need more paperwork."

Mara says, "I get it. Leave it to me."

Glad to let the newbie handle it


# 1.4 Assess process efficiency with value stream maps

When you create a VSM, it helps you analyze your current release-cycle process. The purpose of a VSM is to visually show where in the process a team creates value and where there's waste. The goal is to arrive at a process that delivers maximum value to the customer with minimum waste. A VSM can help you pinpoint those areas that either don't contribute any value, or that actually reduce the value of the product.

Let's see how Tailspin measures up.

Mara, who's new to the team, is going to create a VSM to help her understand the existing process. With a VSM, she'll get a sense of where the team fits into the DevOps maturity model. As it turns out, more mature teams typically release faster, with greater confidence, and with fewer bugs than less mature teams.

Mara knows she doesn't understand everything yet, so she's going to create a quick VSM on the whiteboard in the meeting room. There will be some gaps and unanswered questions. That's okay, it's a start. When she's done as much as she can, she'll share it with the team. The VSM gives everyone a common starting point for identifying the first steps toward improving how Tailspin develops and releases its websites.

Let's take a look at her map.

## Understand the current process

Mara gathers the team in the meeting room to present her VSM.

![](https://learn.microsoft.com/en-us/training/azure-devops/assess-your-development-process/media/4-vsm-whiteboard2.png)

*Photo of a whiteboard showing the value stream map. The image highlights six important phases in the development process.*

**Mara:** A VSM helps us measure where a process has value to the customer and where it's eating up time without producing any value. Our map begins with the functional specification for the software. Let's follow just one feature to see how it moves through our current release cycle.

Some people roll their eyes, but Mara presses on.

### Development processes

Creating a new feature currently starts with creating a label in source control ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-01.png). We have one person who can create labels, Andy. We request a label by email. We use a centralized version-control system, so Andy waits until all the existing code is checked in and stable before he creates the label. After the label is created, we get an email saying we can begin work. This process takes up to three days and has no value to the customer. Things with no value to the customer should take as little time as possible.

Coding a feature takes about four days for one person after we get access to all the files we need.![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-02.png) We have to be on the corporate network in order to access source control. This time has value to the customer. They want this feature.

### Test processes

After we decide that we have a stable build, we update a spreadsheet to tell Amita that there's a build ready for testing and where to find it. ![](https://github.com/user-attachments/assets/85b97056-3ddc-4db5-88a6-ecf8c561fb6d) It takes her two days to get notified.

Amita manually tests the build ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-04.png). This process gets longer as the codebase grows. For now, let's say three days. She then emails Andy with bug reports. Testing doesn't add value, but it's necessary.

Andy then has to take time to triage the bugs and assign work ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-04.png). It can take another three days for Andy to understand the issues and get them to the right developers.

### Operations processes

When Amita approves a build, she hands it off to Tim. Tim needs to deploy this build to the preproduction servers for more testing. Often, the preproduction servers are out of sync with the latest patches and updates needed to run the website. It takes Tim about two days to deploy to preproduction and run some tests. Again, while deploying to preproduction doesn't add value, it's necessary. ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-05.png)

After a build is ready for production, leadership needs to approve the release before it can be deployed. The approval happens in a meeting. It takes four days to get leadership to meet and review the release.

Eventually, Tim deploys the feature, and the feature makes it to the customer here on the upper-right corner of the VSM. If the production server configuration has drifted so it's out of sync with preproduction, Tim first needs to update it, which takes one day. ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/callout-06.png)

## Calculate the customer value metrics

Now we can look at the key performance metrics and see how we measure up.

**Total lead time** is the time it takes for a feature to make it to the customer. Here, the total time is 22 days. **Process time** is the time spent on a feature that has value to the customer. Here, the process time includes four days for coding plus one day to deploy the feature, which gives a total of five days.

The **activity ratio** is process time divided by total lead time:

**Activity ratio = Process time ÷ Total lead time**

This is our efficiency. Multiply efficiency by 100 to get a percentage. The result is greater than 0% and typically less than 100%. A higher percentage indicates greater efficiency.

Substitute our numbers and we get:

**Activity ratio = 5 ÷ 22 = 0.23**

Multiply the result by 100 and you get 23%.

As you can see, we have a lot of room for improvement. And taking 22 days to develop a feature is too long.

**Tim:** So how does this help us?

## Where do we go from here?

**Mara:** It helps to see where we're at now so that we can pinpoint the areas where there's waste. We want to minimize the time we spend that has no value to the customer. I believe we can improve our efficiency by adopting a DevOps approach. For one thing, we can automate many of these steps, which definitely cuts down on the time.

I'm not suggesting we drop our current processes. I think we can work toward a more efficient process in small increments without disrupting what we currently have in place.

Let's look at just a couple of areas where we can improve.

**Andy:** We might as well start at the beginning. It takes me a long time to get a label on the code so we can start the new feature. I have to walk around to the developers and ask them to check in what they have so we can build and test. If you can figure out how to speed that up, you'll have my attention.

Also, I noticed that you don't have time in there for the build itself. That takes half a day right now. It would be nice to see that time improve.

**Amita:** And dev doesn't always update the spreadsheet to let me know there's a new build that needs testing. It would save time if there was some way to make sure that part gets done.

**Mara:** Great! I think DevOps can help us out with all of these concerns.

**Andy:** We don't have time to change the process now. You heard Irwin. We're in crisis mode here!

**Mara:** I understand. For now, let's do what we always do. But we can all think about our part in the process and how we can improve. We can start making small changes in parallel to our current processes. We can then see if DevOps helps us without disrupting what we have. I'll keep this map and the performance metrics. If we end up adopting Azure DevOps practices, then we can revisit the numbers. Maybe we can update the VSM at some point.

## Check your knowledge

**1. What's the purpose of the value stream map?**

It helps you think about your existing processes and where you fit in the DevOps maturity model. ✅
It helps you gain official DevOps accreditation.
It's just extra paperwork.

**2. What do we mean by waste?**

Waste is time between tasks.
Waste means we're having to rewrite code and throw away the old code.
Waste is time spent on tasks that don't have direct customer value. ✅


# 1.5 Summary

As you can see, Mara and her team face a number of challenges. Although releases happen eventually, Mara feels they can happen much more frequently and efficiently.

Mara hopes she can convince the team it's at least worth testing out a DevOps approach. Perhaps they can apply a few DevOps practices as they finish up work on the *Space Game* website.

## What is DevOps?

At this point, we haven't yet defined DevOps. We'll do that in the next module. But for now, think of DevOps as something that brings together people, processes and products, automating software delivery to provide continuous value to your users.

Azure DevOps is a suite of services that spans the entire DevOps life cycle. Azure DevOps starts with planning and goes all the way through deployment and monitoring. If you already have some pieces in place, you can select which services you want to use. Azure DevOps integrates with many tools, like Jenkins.

We'll go deeper into Azure DevOps in future modules. You can also check out these resources:

* Azure DevOps
* DevOps Resource Center



# 3 Choose an Agile approach to software development
Learn to foster the DevOps values of transparency and team cooperation with Azure Boards.

# 3.1 Introduction

You've met the Tailspin team and learned a bit about their problems. Mara, the newest team member, is trying to convince her teammates that a DevOps approach, using the services in Azure DevOps, is a great way to solve them. She's taken it upon herself to do a *value stream mapping* (VSM) exercise, and she's shown everyone the results.

Her next goal is to convince the Tailspin team to take their first DevOps steps by using an Agile approach and Azure Boards, a part of the Azure DevOps suite. Azure Boards helps teams collaborate and plan their work better. This module shows how the team creates its first board.

After completing this module, you'll be able to:

* Define the term Agile.
* Begin to make recommendations for incorporating Agile practices into your organization.
* Create a project in Azure DevOps.
* Add work items to Azure Boards by using the Basic process.

## Prerequisites

The modules in this learning path form a progression. We recommend you start at the beginning of the Get started with Azure DevOps learning path before you work on this module.

If you'd rather do only this module, go through Introduction to Azure DevOps first to set up your Azure DevOps organization.

## Meet the team

You met the *Space Game* web team at Tailspin Toys in previous modules. As a refresher, here's who you'll work with in this module:

**Andy** is the development lead.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/andy.png)

**Amita** is in QA.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/amita.png)

**Tim** is in operations.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/tim.png)

**Mara** just joined as a developer and reports to Andy.
![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/mara.png)

Mara has prior experience with DevOps and is helping the team adopt a more streamlined process by using Azure DevOps.


# 3.2 What is Agile?

Agile is a term that's used to describe approaches to software development, emphasizing incremental delivery, team collaboration, continual planning, and learning. Agile isn't a process as much as it's a philosophy or mindset for planning the work that a team will do. It's based on iterative development and helps a team better plan for and react to the inevitable changes that occur in software development. Let's listen in on Mara's discussion with Andy after the latest release.

Mara felt she'd made a few small steps toward interesting the team in DevOps, but progress has stalled. The team has been too busy fixing bugs in the last release to think about anything else.

Recall that Irwin, the product manager, provided the team with some rather critical customer feedback about the racing game website. Resolving these issues wasn't fun. Andy and Mara would write code and then hand it to Amita, the tester. Amita always seemed to find new bugs and had to hand the code back. The build server failed. Tim couldn't get the game's website to work in production, even after it worked in dev and test. Everyone worked long hours and lost a couple of weekends.

After they shipped the release, Mara and Andy sat down for coffee. They were both tired. Mara was discouraged, but Andy had a different attitude.

**Andy:** I don't know why you're surprised. Getting software out the door is hard. It's always a slog. Have you ever done it differently?

**Mara:** I have, and I think we could make things easier here, too. I really believe DevOps can help us.

**Andy:** I remember we did a value-stream mapping exercise, but now what? We've got to get started on the new release. I thought we were done with DevOps.

**Mara:** There's a lot more we can do. I think we should take the first step and do some Agile planning. We can use Azure Boards to help us.

**Andy:** What do you mean by Agile?

**Mara:** Agile is an approach to software development. The term "Agile" was coined in 2001 in the Agile Manifesto. The manifesto established some guiding principles for a better approach to software development. The manifesto says:

We value:

* Individuals and interactions over processes and tools.
* Working software over comprehensive documentation.
* Customer collaboration over contract negotiation.
* Responding to change over following a plan.

**Andy:** Look, if you know some magic way to make life easier, I'm all for it. My kids are always asleep by the time I get home. But this sounds very touchy-feely without any concrete solutions.

**Mara:** It's not magic, but we can do it bit by bit. Azure DevOps gives us the tools we need to implement Agile practices. For now, when we want to plan, we can use Azure Boards. First, can you explain the build process to me and help me identify the big problems?

After lots of coffee, Mara and Andy identify the biggest problems in the build process. All the issues came up during the last release. After Andy leaves, Mara looks at her scribbled notes and decides to do a little Agile planning herself. On her own, she uses the Basic process on Azure Boards to get all the problems in one place.

Her next step is to show the board to the team and get them involved.

## Recommendations for adopting Agile

The team is getting ready to take their first steps toward adopting Agile. Here are some general recommendations that any team can use to incorporate Agile into their organization.

### Create an organizational structure that supports Agile practices

For most organizations, adopting Agile can be difficult. It requires a mind shift and a culture shift that challenges many existing policies and processes within the organization. Traditionally, most companies use a horizontal team structure. In practice, this means teams correspond to the software architecture. For example, there might be a team responsible for an application's user interface, another team responsible for data, and another team responsible for the service-oriented architecture.

However, vertical teams provide better results for Agile projects. Vertical teams span the architecture and are aligned with product outcomes. For example, there might be a team responsible for the app's email portion, and team members come from all three of the previously mentioned disciplines. Another benefit of the vertical team structure is that scaling occurs by adding teams.

### Mentor team members on Agile techniques and practices

When they first start to adopt Agile techniques and practices, some teams decide to hire external coaches. Coaches might even work with multiple teams to help remove organizational roadblocks and silos, so they often have both teaching and managerial skills. They can also train team members in Agile techniques, like how to run stand-up and review meetings. Over time, though, it's important for team members to develop an ability to mentor each other. This means that most work should be done collaboratively and not by individuals who spend most of their time working alone.

### Enable in-team and cross-team collaboration

If collaboration is the key to becoming successful at Agile, what are some of the ways you can encourage it? Here are some ideas.

#### Cultural change

When changing a culture, keep a few things in mind. It's important that team members have a quiet, comfortable place to work. They need spaces where they can focus, without a lot of distractions and noise.

Meetings are a fact of life, and they can feel like they take over a person's working life. To give team members more control, meetings need an agenda and strict time frames.

Asynchronous communications, like email and messages, can feel overwhelming and people often feel they have to be answered right away. Make it clear that not all of these communications need an immediate response.

Remote team members are now the norm in many companies. Everyone needs to feel comfortable with all their team members and to treat them equally, whether they're in the office or working offsite. Collaboration via communication should become part of the organization's DNA.

We can't overemphasize the importance of good communication, even when there are disagreements. Conflict resolution is a good skill for any Agile team to have.

#### Cross-functional teams

Just as it's important for team members to work collaboratively, it's also important for teams to collaborate with each other. Cross-functional teams add new skills and perspectives that can broaden everyone's ability to solve challenges creatively. Cross-functional teams also make the entire organization more cohesive. They reduce turf wars and increase the sense that everyone is working toward a common goal.

#### Tools for collaboration

Good tools can help your Agile team members collaborate more effectively, both within the team and with other teams. Here are a few suggestions to help you get started:

**Microsoft Teams:** Teams is an application that provides a workplace for chat, meetings, notes, and file storage.

**Skype:** Skype is easy to use and a good general-purpose tool. Many people already have it installed.

**Slack:** Slack provides many separate communication channels, all from a single interface. You can organize these channels in many ways, such as by project, team, or topic. Conversations are retained and are searchable. It's easy to add both internal and external team members. Slack directly integrates with many third-party tools, like GitHub for source code.

Other common tools include Google Hangouts, Asana, Trello, GoToMeeting, and monday.com. Try to familiarize yourself with the options to see which of them suit the needs of your team and your company.


# 3.3 What is Azure Boards?

Azure Boards is a tool in Azure DevOps to help teams plan the work they need to do. The Tailspin team will use this tool to get a better idea of what work they need to do and how to prioritize it.

Mara created her own project on Azure Boards using the Basic process. It shows the problems in the build process that she and Andy identified. Mara gets the team together for a quick demo.

**Mara:** Hi everyone. I set up Azure Boards and wanted to show you some work items I came up with.

**Andy:** What's a work item?

**Mara:** Work items help us plan and manage a project. A work item can track all types of activities. Maybe it's a task to do, a bug to fix, or some other issue. We can assign them to people, and keep track of their progress.

Perhaps it's easier to show you. Here's Azure Boards using the Basic process:

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/build-initial-tasks.png)

*Screenshot of Azure Boards showing the initial three tasks. Each task is in the To Do column.*

**Amita:** Tell us about the Basic process. Are there other options?

**Mara:** There are four processes from which to choose. We can use:

**Capability Maturity Model Integration (CMMI):** This is really for large organizations, and it's pretty complicated. So I didn't use it.

**Scrum:** Scrum depends on a Scrum master who leads the Scrum team. The Scrum master makes sure everybody understands Scrum theory, practices, and rules. We don't have a Scrum master. That's someone who usually receives some training and certification, so I didn't pick that one either.

**Agile:** This seemed like the obvious choice because I'm always talking about Agile, but it has a few more things to consider than the simplest option.

**Basic:** Basic is, well, basic. It's simple but gives us enough power to start doing effective planning right away. That's why I picked it. In the Basic workflow, you move work from To Do to Doing to Done.

**Amita:** OK, let's use it to get started. We can switch to something else, right?

**Mara:** Right! So, let's pick a few work items we think we can fix in a couple of weeks.

Andy can identify with these issues, but the rest of the team has questions.

**Tim:** These are mostly dev problems. But while we're on the subject, other teams are talking about code vulnerabilities. I've been asked to show that our code is secure. Is there a way we can add that?

**Mara:** I know the list isn't complete. The problems on the board are the ones Andy and I talked about earlier. Some of these problems really need to get broken down into smaller tasks. I understand your concerns about code vulnerabilities. Andy, what do you think?

**Andy:** Right now, just getting a build out the door is hard. Let's start with some of the basic problems. I do like that we have a central place where we can keep track of our issues. We can add issues to the backlog and prioritize them once we're ready.

**Mara:** Before we add any issues, let's talk a bit more about what everyone is working on.

Each team member shares what they're working on and other concerns they have. As a brainstorming activity, they add sticky notes to a whiteboard. Their whiteboard fills up quickly.

![](https://learn.microsoft.com/en-us/training/azure-devops/choose-an-agile-approach/media/3-whiteboard.png)
*Screenshot of a whiteboard containing sticky notes. The contents of the sticky notes aren't legible.*

Eventually, the team settles on seven top issues. Andy volunteers to add tasks to Azure Boards while everyone watches. Here's what the board looks like:

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/build-all-tasks.png)
*Screenshot of Azure Boards showing a backlog of issues.*

**Amita:** Wow, that's a lot of problems. How are we ever going to fix all those?

**Mara:** We don't have to fix them all right away. For now, we've identified a backlog, or list of work from which we could pull. When we plan work, we get to choose what's most urgent or important.

After some more discussion, the team decides to take on the three issues Mara originally proposed:

* Stabilize the build server.
* Create a Git-based workflow.
* Create unit tests.

**Mara:** These seem like the easiest issues to take on, and they address some recent challenges that came up. Let's set up a project, a team, and a sprint. Then we can decide who does what.

**Tim:** What's a sprint?

**Mara:** Good question. A sprint is the amount of time we have to complete our tasks. Sprints help keep us focused. At the end, we can have a short retrospective meeting to share what we've accomplished. After that, we can plan the next one.

Everyone looks nervous.

**Mara:** We're still learning. A sprint is typically two to four weeks long. Let's just say two weeks and see how that goes. These are mostly tasks Andy and I can tackle. We'll share our progress as we go. Then we can find ways to include everybody.

Mara and the team are off to a good start. Next, you'll set up the project, team, and some tasks on Azure Boards.

## Check your knowledge

**1. The Agile Manifesto states:**

Processes and tools come before the individuals that use them.
You need to fully document new features before you build them.
Responding to change comes before following a plan. ✅

**2. Azure Boards is:**

A way for your customers to provide feedback.
A graphical way to plan and track your work. ✅
A way to list all of your projects.

**3. A sprint is:**

A fixed amount of time a team has to complete a set of tasks. ✅
Another name for a task board.
Time your team sets aside to work on bugs.


# 3.4 Exercise - Plan work using Azure Boards

Here, you'll create a project, a team, and a board in Azure DevOps.

The Tailspin team is eager to see how Azure Boards is going to work. With the pre-planning out of the way, they can start to use the tools and build the solution they planned.

## Set up Azure Boards using the Basic process

In this section, you'll set up an Azure DevOps project and Azure Boards for the Tailspin team.

### Create the project

Here, you'll create an Azure DevOps project.

1. Sign in to your account at dev.azure.com.

2. Select your organization.

3. Select **+ New project**. If you don't already have existing projects in your organization, there won't be a **+ New project** button, and you can proceed to step 3.

   The **Create a project** dialog box opens.

4. In the **Project name** field, enter **Space Game - web**.

5. In the **Description** field, enter **The Space Game website**.

6. Under **Visibility**, choose whether to make your project public or private. For now, you can select **private**.

   Open-source project creators will often choose **public** visibility so that others can view active issues and build status.

7. Select **Advanced**.

8. Under **Version control**, ensure that **Git** is selected. Under **Work item process**, ensure that **Basic** is selected.

9. Select **Create Project**.

After just a few moments, you're taken to your new project.

### Create a team

Here, you'll create a team for the project.

1. Select **Project settings** in the lower corner.

2. On the **Project details** page, under **General**, select **Teams**.

3. Based on the name of the project **Space Game - web Team**, you see that a default team has been created. We'll use this team, but in practice you might have multiple teams that contribute to the same project.

4. Select **Space Game - web Team**.

   You'll see that you're already a member of this team. Let's add more members.

### Add team members

Now's a good time to add members to your team. Although not required, if you'd like to add a coworker to your Azure DevOps organization, here's how:

1. Under **Members**, select **Add**.
2. Enter the email address of the user you'd like to add, and then select **Save**.
3. Repeat the process for any other members you'd like to add.

Mara adds entries for herself and her team members: andy@tailspintoys.com, amita@tailspintoys.com, mara@tailspintoys.com, and tim@tailspintoys.com.

In practice, you might manage your team through an identity and access management service like Microsoft Entra ID, and set the appropriate permission levels for each team member. We'll point you to more resources at the end of this module.

### Create the board

Although Mara and her team identified a number of issues, here you'll add the three work items Mara originally proposed to her team, which you can use to practice the process.

1. In the column on the left, hover over **Boards** and select **Boards** from the menu that appears.

2. Select **Space Game - web Team**. A blank board appears.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/choose-an-agile-approach/media/3-blank-board.png)
   
   *Screenshot of Azure Boards showing an initially empty board.*

   Recall that you're using the Basic process. The Basic process involves three task states: **To Do**, **Doing**, and **Done**.

   If you choose a different process, like Scrum, you'll see a layout that supports that process.

3. In the **To Do** column, select the **+ New item** button.

4. Enter **Stabilize the build server**, and then press Enter.

5. Select the ellipsis (**...**) on the item you just created, then select **Open**.

6. In the **Description** field, enter this text:

   ```
   The build server keeps falling over. The OS requires security patches and updates. It's also a challenge to keep build tools and other software up to date.
   ```

7. Select **Save & Close**.

8. Follow the same steps for the next two items.

   | Title | Description |
   |-------|-------------|
   | Create a Git-based workflow | Migrate source code to GitHub and define how we'll collaborate. |
   | Create unit tests | Add unit tests to the project to help minimize regression bugs. |

9. Drag **Stabilize the build server** to the top of the stack, then drag **Create a Git-based workflow** to the second item position. Your final board looks like this:

   ![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/build-initial-tasks.png)

   *Screenshot of Azure Boards showing the initial three tasks. Each task is in the To Do column.*

### Define a sprint

**Mara:** This is looking great. Now let's define a sprint.

When you create an Azure Boards project, you get an initial sprint called **Sprint 1**. All you need to do is assign dates to the sprint and add tasks. Here's how to follow along with the team:

1. In the left-side column, select **Sprints**.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/choose-an-agile-approach/media/4-boards-sprints-menu.png)
   
   *Screenshot of Azure DevOps showing the location of the Sprints menu.*

3. Select the **Set dates** link in the upper-right corner.

4. Leave the name as **Sprint 1**.

5. In the **Start date** field, select the calendar and pick today's date.

6. In the **End date** field, select the calendar and pick the date two weeks from today.

7. Select **Save and close**.

### Assign tasks and set the iteration

An iteration is another name for a sprint.

You have an initial set of work items and a timeline for your first sprint. Here, you'll connect work items to your sprint, and assign the tasks to yourself.

1. Under **Boards**, select **Work items**.

2. Select **Stabilize the build server**.

3. In the **Iteration** dropdown, select **Sprint 1**.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/choose-an-agile-approach/media/3-assign-sprint.png)

   *Screenshot of Azure Boards showing the location of the Sprint 1 iteration.*

4. From the same window, select **No one selected**, and set yourself as the task owner.

   ![](https://learn.microsoft.com/en-us/training/azure-devops/choose-an-agile-approach/media/3-assign-owner.png)

   *Screenshot of Azure Boards showing the location of the task owner.*

4. Select **Save**.

6. Repeat the process for the other two work items.

   * Create a Git-based workflow
   * Create unit tests

**Mara:** We did it! We created our first project on Azure Boards and we identified the first tasks we'll take on. It's great! As Andy and I do this work, we'll move each work item to the **Doing** state.

**Amita:** Sounds good. I enjoyed getting together and deciding what's important to us right now. And, like Andy said, now we have a way to see everything all in one place.


# 3.5 Summary

In this module, the Tailspin team took their first steps towards adopting DevOps practices. You worked with them and learned how to use Azure Boards to get started with Agile work planning. A board gives you an easy way to see what's going on with a project and to manage your work. Some of the things you learned to do with Azure Boards include how to:

* Create projects.
* Create work items.
* Associate work items with a sprint, or iteration.

## Learn more

This module touches on Agile and Agile processes, but there's a lot more to learn.

If you're interested in learning more about the benefits of Agile, check out What is Agile Development?

In this module, you followed the Basic process. You'll continue using this process in upcoming modules. For your own projects, learn how to choose a process that best fits your team. You can also learn more about each process Azure Boards supports.

* Agile process
* Scrum process
* CMMI process

Also in this module, you added fictitious team members to your project. Learn more about how to add users to your organization or project.

As you plan and track your work with Azure Boards, you can refer to our complete Azure Boards Documentation to get the most out of them.


# 4 Manage Agile software delivery plans across teams

Learn how to optimize delivery efficiency by improving work plan visibility across teams.

#### Learning objectives
After completing this module, you'll be able to:

- Describe how delivery plans allow multiple teams to plan, schedule, and coordinate their work.
- Create a delivery plan and adjust a team's sprint workload to optimize delivery efficiency.
- Review dependencies between work items shown in a delivery plan.






