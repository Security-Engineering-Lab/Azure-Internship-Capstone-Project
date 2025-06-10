

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

# 4.1 Introduction

Azure DevOps can help your team scale their development processes to deliver bigger, more ambitious projects. Let's rejoin the Tailspin Toys team as they tackle common problems that organizations face as they grow. Together, we'll discover what it takes to manage work schedules across multiple teams effectively.

You met the team at Tailspin Toys earlier in this learning path. In the previous module, you watched as they began to manage their work schedule through Azure Boards. Soon, word of their early success began to spread, and now other teams are exploring how they can enjoy the same benefits.

As more teams adopt Azure Boards, the organization begins to see the network effects of having their planning consolidate around a consistent process. Problems that were once written off as a cost of doing business now have achievable solutions. Let's watch the team as they lead their organization in its evolution.

After completing this module, you'll be able to:

* Describe how *delivery plans* enable multiple teams to plan, schedule, and coordinate their work.
* Create a delivery plan and adjust a team's sprint workload to optimize delivery efficiency.
* View dependencies within work items within a team or across teams.
* Resolve dependencies that have issues.

## Prerequisites

The modules in this learning path form a progression. We recommend that you start at the beginning of the Get started with Azure DevOps learning path before you work on this module.

If you'd rather do only this module, go through Introduction to Azure DevOps first to set up your Azure DevOps organization.

## Meet the team

You met the *Space Game* web team at Tailspin Toys in previous modules. As a refresher, here's who you'll work with in this module:

**Andy** is the development lead.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/andy.png)

**Mara** just joined as a developer and reports to Andy.

![](https://learn.microsoft.com/en-us/training/azure-devops/shared/media/mara.png)

Mara has prior experience with DevOps and is helping the team adopt a more streamlined process by using Azure DevOps.


# 4.2 What are delivery plans?

As development organizations grow, they need to reorganize into smaller teams that can efficiently manage portioned units of work. These teams usually have their work schedules, boards, and other processes that meet their unique needs within the context of the organization's larger goals. Over time, organizations might find that they enjoy network benefits by consolidating their processes around a consistent framework.

A delivery plan is a visualization of one or more work schedules. It's intended to provide teams and management an overall view of what each team is planning to produce and when. It allows decisions to be made that optimize the investments across the organization.

Teams must regularly review their delivery plans to ensure that their work schedule aligns with other teams' schedules. These reviews should address questions like:

* Are we sure we can deliver what we've committed to on our current schedule?
* Are we confident that the teams we depend on will deliver what we need on their current schedule?
* Are there lulls in our schedule that we could fill with work?
* Are there issues with dependencies within a team or across teams?

Delivery plans add value at any point in a project's lifecycle. Because they're dynamically generated based on team backlogs, they're always up-to-date and offer the latest insights.

Let's join the Tailspin web team in their discussion.

**Andy:** I just had a great meeting with engineering management. I demoed the work we're doing with Azure Boards, and they're excited about the prospect of getting other teams on board.

**Mara:** Awesome! When will they get started?

**Andy:** That's the best part. They already have! Last night the game engine project lead created a team with some sprints and began adding work items. I took a quick look this morning, and it's shaping up nicely. Let me show you what they're up to.

Andy navigates to the game engine's current sprint board. He and Mara review the work items with great interest.

**Andy:** Hmm...I just noticed that they're not planning to deploy their beta by the end of this sprint. Aren't we expecting to integrate our leaderboard with the beta database during our next sprint? We can't do that if they don't ship the beta first.

**Mara:** That's a good point. We have a dependency on that team to produce that deliverable so we can produce one of our own.

**Andy:** This could have really hurt our productivity next sprint. I'm going to give them a call to find out what's going on.

Unfortunately, more sophisticated team structures can result in gaps or lags in communication. When one team is blocked, they might not be able to produce something another team is dependent on. This might not be a major issue for a small group of teams that have daily meetings for all concerned. However, as teams scale in size and location, it can become untenable for everyone to know everything going on everywhere. It's at this point that organizations need to transition from a pure "push" model (like in-person or email announcements) to a "pull" model (where teams can review and track each other's schedules).

**Andy:** Okay, I just spoke with the dev lead. She told me their team is blocked from shipping the beta until the art team returns from Cliffchella.

**Mara:** The mountaintop music festival?

**Andy:** Yeah, apparently, it's a huge deal in the design community, and their entire team just drops off the grid for a whole week to attend. The game engine team is pretty upset because it slipped their schedule by three weeks. Had they known it was coming, they would have made sure to get the artifacts they needed ahead of time. They also apologized for not letting us know sooner. They didn't realize we would be waiting on their beta to ship our part.

**Mara:** Well, at least we can be glad that the game engine team is publishing their sprint plans. It helped us find this dependency issue early enough to adjust our schedule.

**Andy:** I just wish there was a way to see these potential risks coming more easily. Our teams have so many dependencies across the company that there's no way we can attend every meeting and subscribe to every distribution group.

**Mara:** We should create a delivery plan so that we can see our team sprints side-by-side. This will help both teams more easily identify how our schedules affect each other.

## Recommendations for managing multiple Agile teams

An Agile approach, along with Azure DevOps can substantially improve project transparency and predictability. However, projects might still run into traditional challenges, often related to personnel or miscommunication. Here are a few things to consider as you scale your Agile efforts.

### Build trust in your people and processes

Early detractors of Agile implementations are often skeptical about their ability to improve team performance. It's important for thought leaders within the organization to build trust by illustrating how the tools and processes produce results. Sometimes these results are improvements in productivity, which are easy to quantify. However, don't forget to highlight the team wins that occur by circumventing potential problems, such as avoidable schedule slips or quality issues. As people begin to associate the benefits with the process that achieved them, you'll get more enthusiasm.

### Elevate the organization above the team (and individual)

Some teams and individuals get territorial when new processes or policies are proposed. Rather than framing new policies as negatively exposing the performance of specific teams or individuals, highlight how the new transparency across the organization informs everyone of expectations. Having a single place where anyone can trace how their work relates to the organization meeting its goals will drive home the importance of their commitment to the process.

### Foster a culture of transparency

Unfortunately, the term "transparency" gets a bad rap. Nobody asks for more transparency when everything is going great. Instead, transparency (or lack thereof) is often blamed when teams are struggling. Even with all of the opportunities for transparency afforded for Agile teams, it's still subject to the honesty of individuals and teams. Emphasize that one of the reasons for transparency is to be able to identify and address potential issues before it's too late. Everyone understands that people sometimes run into circumstances that prevent them from meeting schedule deadlines. But if they don't feel safe in reporting disappointing news until the last possible moment, it can have a much more destructive impact. Building a comfort level with transparency can start with thanking people for reporting expected delays as early as possible.


# 4.3 What is Delivery Plans?

Delivery Plans is a hub in Azure DevOps that helps organizations plan and review work schedules across multiple teams. The Tailspin team can use this hub to get a better idea of how their work relates to the work of other teams.

Mara created a delivery plan and added the sprints for her team and the game engine team. Excited to show off the potential, she invites Andy over for a quick demo.

**Mara:** After our last conversation, I looked into our options for managing delivery plans. I found the Delivery Plans hub that seems to give us everything we need.

**Andy:** I'm interested to see what you've come up with. There's a lot of stress throughout the organization about the beta slip, so anything we can do to improve schedule efficiency will be welcome.

**Mara:** Okay, here it is. See those red icons. Those indicate we've got some issues with dependencies between work items.

*Screenshot of a delivery plan showing schedules for the Web team and the Engine team.*

**Mara:** Delivery Plans allows us to create a "delivery plan." Once we create that, we can add in the backlogs of teams within the organization. They're shown in parallel so that we can see what each team is planning to deliver against a calendar backdrop.

**Andy:** This view looks great! Now we know when something we're dependent on won't be available in time. We can even gauge the likelihood of delay based on how much other work and dependencies those teams have taken on. This should help mitigate some of the "schedule chicken" behavior that sometimes goes on around here.

> **Note**
> 
> Schedule chicken is when two or more teams are at risk of not meeting deadlines, but none of them want to admit it. Instead, each wait for another to slip their schedule first and then uses the other team's slip as a pretext for delaying their delivery.

**Mara:** Yes, and we can also use this as an opportunity to let other teams know if we're going to slip something they're dependent on. It helps us build trust in our people and processes.

Andy nods in agreement. It would be nice for the teams to have more faith in each other.

**Andy:** Now that we know about the beta slip, we have to move our associated work out to a future sprint. On the bright side, it gives us an opportunity to pull some new work in to replace it. Let's swap the integration work with those two leaderboard bugs.

Mara drags the integration work item out to the following sprint. She then drags the two leaderboard bugs back in to fill the available capacity.

*Screenshot of the delivery plan after work is reorganized.*

**Mara:** I also added the current beta date as a milestone. Now we'll always have it in place as a reference point for the work we're planning.

**Andy:** We should also add events like Cliffchella and the annual company party.

**Mara:** Why the company party? Does that affect the schedule?

**Andy:** It might. Every year the DBAs enter the pie-eating contest, and they all end up calling in sick the next day. I'm not saying we should expect it to happen again this year, but I do think we should be prepared. And now we have the tools for it.

## Check your knowledge

**1. What is a delivery plan?**

A list of work items scheduled to be completed by a specific date.
A visualization of one or more work schedules against a calendar backdrop. ✅
A document describing when and how a product will be delivered to the customer.

**2. Which of the following isn't a good reason to use a delivery plan?**

You need to gauge the likelihood of other teams producing their deliverables on their current schedules based on their commitments.
You need to plan your team's work schedule at least in part based on the work schedules of other teams.
You need to understand how other teams are going to produce their deliverables. ✅

**3. When is a good time to start using delivery plans?**

You should create a delivery plan before you start planning work sprints.
You should wait until all work is planned before creating a delivery plan.
Creating a delivery plan can be valuable at any point in a project. ✅



# 4.4 Exercise - Set up your environment

In this section, you make sure that your Azure DevOps organization is set up to complete the rest of this module.

To meet these objectives, you:

* Set up an Azure DevOps project for this module.

## Get the Azure DevOps project

Set up your Azure DevOps organization to complete the rest of this module by running a template that creates a project in Azure DevOps.

The modules in this learning path are part of a progression. You follow the Tailspin web team through their DevOps journey. For learning purposes, each module has an associated Azure DevOps project.

### Run the template

Run a template that sets up your Azure DevOps organization.

1. Get and run the ADOGenerator project in Visual Studio or the IDE of your choice.

2. When prompted to **Enter the template number from the list of templates**, enter **37** for **Manage Agile software delivery plans across teams**, then press **Enter**.

3. Choose your authentication method. You can set up and use a Personal Access Token (PAT) or use device login.

   > **Note**
   > 
   > If you set up a PAT, make sure to authorize the necessary **scopes**. In this case, you can use **Full access**.

4. Enter your Azure DevOps organization name, then press **Enter**.

5. If prompted, enter your Azure DevOps PAT, then press **Enter**.

6. Enter a project name such as *Space Game - web - Delivery plans*, then press **Enter**.

7. Once your project is created, go to your Azure DevOps organization in your browser (at `https://dev.azure.com/<your-organization-name>/`) and select the project.

> **Important**
> 
> The **Clean up your Azure DevOps environment** page in this module contains important cleanup steps. Be sure to follow the cleanup steps even if you don't complete this module.


# 4.5 Exercise - Plan a sprint using Delivery Plans

Now you can create a delivery plan and use it to plan a sprint in Azure DevOps.

The Tailspin team is eager to see how Delivery Plans is going to work. They already have two teams with sprints set up in Azure DevOps, so now they can review and optimize the work schedules.

To do this, you:

* Create a delivery plan.
* Add team sprints and milestones.
* Rearrange work items to fit the overall schedule.

## Create a delivery plan

You create a delivery plan from the **Delivery Plans** tab of Azure Boards. You can create as many delivery plans as you need to manage different aspects of your organization.

1. From Azure DevOps, navigate to your project.

2. Under **Boards**, select **Delivery Plans**.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-delivery-plans/media/boards-delivery-plans.png)

3. Select **New plan**.

4. In the form, enter these fields:
   * **Name**: *Space Game Delivery Plan*.
   * Select the **Backlog items** backlog for the **Space Game Web Team**.
   * Add the **Space Game Engine Team's Backlog items** backlog using the **Add team** option.

   The Web team and the Engine team share a common set of backlog items.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-delivery-plans/media/5-create-delivery-plan.png)

5. Select **Create**.

> **Note**
> 
> The team project generated for this module uses the *Scrum* process, not the *Basic* process used in other modules in this learning path. While the Basic process uses *Issues*, the Scrum process uses *Backlog items*, which are functionally the same for the purposes of this module. You can use Delivery Plans with either process.

## Add schedule milestone markers

Milestone markers can be added to the delivery plan as reference points. They help you plan work within the context of significant or external dates. Let's add a few markers now. To do so:

1. Select your delivery plan.

2. In the top right toolbar, select **Settings**, and then, on the **Plan settings** pane, select **Markers**.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-delivery-plans/media/5-configure-plan-settings.png)

3. From the **Markers** tab, select **Add marker**.

4. In the form, enter these fields:
   * **Date**: Select a date one week from now
   * **Label**: Cliffchella
   * **Color**: Red

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-delivery-plans/media/5-add-marker.png)

5. Repeat the process to add markers with labels, dates, and colors:
   * **Beta**: five weeks from today (blue)
   * **Annual company party**: six weeks from today (green)

6. Select **Save**.

7. Use the **Scroll calendar** and **Zoom out** controls to bring all markers into view.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-delivery-plans/media/5-show-all-markers.png)

8. Select the **Beta** marker at the top of the design plan. A solid line shows the boundary of the beta milestone.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-delivery-plans/media/5-analyze-milestones.png)

## Optimize the work schedule

1. Notice that there's a work item for the Web team to **Integrate with beta DB**. It's scheduled for completion before the beta will be ready. This is a problem because this work item is dependent on that beta.

2. Drag the integration work item from **Sprint 3** to **Sprint 4** to ensure that its dependency will be available.

3. This change opens a significant amount of bandwidth in **Sprint 3**. Because that time is now available for productive work, drag the two **Fix** work items from **Sprint 4** back into **Sprint 3**.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-delivery-plans/media/5-adjust-work-schedule.png)

Your final sprint plan should look similar to this:

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-delivery-plans/media/5-optimized-work-schedule.png)

Although the team has made some adjustments, they haven't addressed all the dependency issues that are identified in the delivery plan. In the next unit, they learn more about dependencies and how to resolve the issues that can occur in the schedule.


# 4.6 Exercise - Track dependencies using Delivery Plans

The Tailspin team noted previously that some cards in the delivery plans have green icons ![](https://learn.microsoft.com/en-us/training/azure-devops/manage-delivery-plans/media/6-dependency-green-icon.png)  or red  ![](https://learn.microsoft.com/en-us/training/azure-devops/manage-delivery-plans/media/6-dependency-red-icon.png) icons attached. You'll now learn about how these icons showcase the dependencies that exist between work items and how to resolve dependency issues.

The team created dependencies between several work items using the **Predecessor/Successor** link type. The links they've created automatically appear in the delivery plan they created. Now they need to review these dependencies and address any dependencies that have issues.

To do this, you:

* Review delivery plans for dependencies.
* Identify work items with dependency issues.
* Resolve dependencies that have issues.

## View work items with dependencies

The first thing the team notices when they open the delivery plan is that link icons appear. Cards with a green ![](https://learn.microsoft.com/en-us/training/azure-devops/manage-delivery-plans/media/6-dependency-green-icon.png) icon indicate there are no dependency issues. Cards with a red icon ![](https://learn.microsoft.com/en-us/training/azure-devops/manage-delivery-plans/media/6-dependency-red-icon.png) indicate there are issues with one or more dependencies.

Dependency issues arise when a *predecessor* work item is scheduled to finish after a *successor* work item.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-delivery-plans/media/6-view-dependencies-delivery-plans.png)

## View lines linking work items with dependencies

To view the work items that share in a dependency, select the card with an icon attached. Here, we select the *Update privacy policy* card.

A link appears that indicates which work item is participating in the dependency. In this case, it highlights that the *Complete community interaction training* work item for the Engine Team. The arrow indicates the direction of the dependency, and the black line reinforces that there's no issue.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-delivery-plans/media/6-view-dependency-across-teams-no-issues-delivery-plans.png)

To dismiss the dependency line, select the card or anywhere in the view.

Now, choose a card with an issue. Here we select *Update site branding*. An issue is shown with the link to the *Push beta* item defined for the Engine Team. The red line indicates there's an issue and the arrow indicates that the *Push beta* item is scheduled to complete after *Update site branding*, which depends on it being completed first.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-delivery-plans/media/6-view-dependency-across-teams-with-issues-delivery-plans.png)

## Open the dependency dialog

To review details of the *Push beta* work item, choose the card's icon to open the Dependencies dialog. The first dependency indicates an issue where the *Update site branding* work item requires the *Push beta* work to be completed first. The second dependency listed shows no issue.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-delivery-plans/media/6-open-dependency-dialog-with-issues-delivery-plans.png)


## Resolve dependencies that have issues

The team decides to change the order in which to complete selected work items so as to resolve the dependency issues. They perform the following actions:

* **Web team**:
   * Drag *Create a Git-based workflow* card from **Sprint 1** to **Sprint 2**.
   * Drag *Check open source code for vulnerabilities and licensing terms* card from **Sprint 2** to **Sprint 1**.
   * Drag *Update site branding* card from **Sprint 4** to **Sprint 6**.
* **Engine team**:
   * Drag *Push beta* card from **Sprint 6** to **Sprint 5**.

> **Tip**
> 
> If the icons don't update as expected, refresh your browser by pressing **Ctrl+F5**.

Once these changes have been made, the team sees that all dependency issues have been resolved.

![](https://learn.microsoft.com/en-us/training/azure-devops/manage-delivery-plans/media/6-all-dependency-issues-resolved-delivery-plans.png)

You've just completed some invaluable work that impacts the organization in a meaningful way. Management can feel confident that work will progress without foreseeable delays. Now, instead of waiting on dependencies to be delivered, teams will always have productive work to take on. Sure, things might change as circumstances develop, but at least now everyone knows where to go to stay up to date.


# 4.7 Exercise - Clean up your environment

Now that you're done with the tasks for this module, clean up your Azure DevOps environment.

## Optional - Delete your project

This module provided a template that you ran to create a clean environment for the module.

Delete your Azure DevOps project, including what's in Azure Boards. In future modules, you can run another template that brings up a new project in a state where this module leaves off. Choose this option if you don't need your DevOps project for future reference.

To delete the project:

1. In Azure DevOps, go to your project. Earlier we recommended that you name this project **Space Game - web - Delivery plans**.

2. Select **Project settings** in the lower corner.

3. At the bottom of the **Project details** area, select **Delete**.

4. In the window that appears, enter the project name, and then select **Delete** again.

Your project is now deleted.

# 4.8 Summary

In this module, the Tailspin team took on some common organizational challenges around software delivery and adapted their process to better handle them. Some of the things you learned to do with Azure DevOps include how to:

* Create a delivery plan.
* Add team sprints and milestones to a delivery plan.
* Rearrange work items to fit the overall schedule.
* View dependencies between work items in a delivery plan.
* Resolve dependencies that have issues.

## Learning path summary

Congratulations, you've completed the final module in the *Get started with Azure DevOps* learning path. In this learning path, you:

* Saw how a value stream map can help you examine your existing processes and technologies.
* Saw what DevOps is (and isn't), and created an Azure DevOps organization.
* Learned how Azure Boards helps teams plan the work that needs to be done. You used the Basic process to set up a basic backlog of tasks you'll work on in upcoming modules.
* Learned how to optimize sprint workloads across multiple Agile teams.
* Learned how to view and track dependencies within and across several Agile teams.

## Continue the journey

You've seen the team identify their top-priority problems, but how will they solve them? If you want to work along with them and learn how to configure build pipelines that continuously build, test, and verify your applications, go to Build applications with Azure DevOps.

For more self-paced, hands-on learning around Azure DevOps, also check out Azure DevOps Labs.

## Learn more

This module focused on how delivery plans can help you manage work schedules across multiple teams. However, there are many things to consider when coordinating projects at scale.

To learn more about some of the other features Azure DevOps provides for scaling your team projects, such as team hierarchies, project portfolio management, and dashboards, see Plan for Agile at scale.



