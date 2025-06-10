

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

Coding a feature takes about four days for one person after we get access to all the files we need. We have to be on the corporate network in order to access source control. This time has value to the customer. They want this feature.

### Test processes

After we decide that we have a stable build, we update a spreadsheet to tell Amita that there's a build ready for testing and where to find it. It takes her two days to get notified.

Amita manually tests the build. This process gets longer as the codebase grows. For now, let's say three days. She then emails Andy with bug reports. Testing doesn't add value, but it's necessary.

Andy then has to take time to triage the bugs and assign work. It can take another three days for Andy to understand the issues and get them to the right developers.

### Operations processes

When Amita approves a build, she hands it off to Tim. Tim needs to deploy this build to the preproduction servers for more testing. Often, the preproduction servers are out of sync with the latest patches and updates needed to run the website. It takes Tim about two days to deploy to preproduction and run some tests. Again, while deploying to preproduction doesn't add value, it's necessary.

After a build is ready for production, leadership needs to approve the release before it can be deployed. The approval happens in a meeting. It takes four days to get leadership to meet and review the release.

Eventually, Tim deploys the feature, and the feature makes it to the customer here on the upper-right corner of the VSM. If the production server configuration has drifted so it's out of sync with preproduction, Tim first needs to update it, which takes one day.

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


