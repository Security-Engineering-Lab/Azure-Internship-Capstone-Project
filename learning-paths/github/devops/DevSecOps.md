


# What is DevSecOps?

Learn how to integrate security practices into every phase of the software development lifecycle across your multicloud environment.

**Microsoft Defender Cloud Security Posture Management**

- [DevSecOps defined](#devsecops-defined)
- [DevSecOps versus DevOps](#devsecops-versus-devops)
- [Importance of DevSecOps](#importance-of-devsecops)
- [DevSecOps components](#devsecops-components)
- [DevSecOps implementation](#devsecops-implementation)
- [DevSecOps tools and technologies](#devsecops-tools-and-technologies)
- [DevSecOps best practices](#devsecops-best-practices)
- [FAQs](#faqs)

## DevSecOps defined

DevSecOps, which stands for development, security, and operations, is a framework that integrates security into all phases of the software development lifecycle. Organizations adopt this approach to reduce the risk of releasing code with security vulnerabilities. Through collaboration, automation, and clear processes, teams share responsibility for security, rather than leaving it to the end when issues can be much more difficult and costly to address. DevSecOps is a critical component of a multicloud security strategy.

## DevSecOps versus DevOps

In traditional software development, projects are split into distinct phases for planning, design, development, integration, and testing, which happen sequentially over several months or even years. Although this approach is very methodical, many organizations have found it to be too slow, making it difficult to meet customers' expectations for continuous product improvements. Additionally, security typically gets bolted on at the very end, which puts companies at risk of a breach.

To remain competitive, many companies have adopted a DevOps model that prioritizes delivery of smaller packets of high-quality code rather than feature-rich projects that take longer. In this framework, software development and operations teams collaborate to incorporate testing and integration throughout the process. Automation, standardized processes, and collaboration help teams move quickly without sacrificing quality.

DevSecOps is an enhancement to DevOps that builds security into all aspects of the process. The goal is to address security issues from the very start of the project. In this framework, not only does the entire team take responsibility for quality assurance and code integration but also security. In practice, this means teams discuss security implications during planning and begin testing for security issues in development environments, rather than waiting until the end. Another name for this approach is shift left security.

## Why is DevSecOps Important?

There are many methods that attackers use to gain access to an organization's data and assets, but a common tactic is to exploit software vulnerabilities. These types of breaches are costly, time consuming, and depending on the severity, damaging to a company's reputation. The DevSecOps framework reduces the risk of deploying software with misconfigurations and other vulnerabilities that bad actors can take advantage of.

## Key Components of DevSecOps

A successful DevSecOps process includes the following components:

### Continuous integration

With continuous integration developers commit their code to a central repository multiple times a day. Then the code is automatically integrated and tested. This approach enables teams to catch integration issues and bugs early in the process rather than waiting until the end when there could be several issues that need to be resolved.

### Continuous delivery

Continuous delivery builds upon continuous integration to automate the process of moving code from the build environment to a staging environment. Once in staging, in addition to unit testing, the software is automatically tested to ensure the user interface is working, the code is successfully integrated, that APIs are reliable, and that the software can handle the expected traffic volumes. The goal of this approach is to consistently deliver production-ready code that provides value to customers.

### Continuous security

Building security into the entire software development lifecycle is a key component of DevSecOps. This includes threat modeling early in the process and automated security testing throughout the entire lifecycle, starting with developers' own environments. By thoroughly testing the software for security issues early and frequently, organizations can efficiently deliver software with minimal issues.

### Communication and collaboration

DevSecOps is highly dependent on individuals and teams working closely together. Continuous integration requires people to collaborate to address conflicts in code, and teams need to effectively communicate to unify around the same goals.

## How to implement DevSecOps

Adding security to your DevOps process requires careful planning. Start slowly with processes that introduce the least friction for the team and offer the biggest security payoff. Here are a few ways to add security to a typical DevOps sprint.

### Planning and development

Introducing security early into development sprints not only helps reduce vulnerabilities later down the line, but it also saves time because it's easier to address issues before code has been built and integrated. During planning and development, use threat modeling to identify and mitigate potential threats to the application. This will help you build security into the application right from the start. To uncover security issues before code is committed to the shared repository, implement automated checks, such as integrated development environment security plugs-ins, which give developers immediate feedback if there's a potential security risk in the code they've written. During code review, have someone with security expertise provide recommendations for making improvements.

### Code commit

One of the keys to a successful DevSecOps process is continuous integration. Developers typically commit their code to a central repository several times a day to ensure integration issues are caught early. It's important to add automated security checks to this phase. This can include scanning third-party libraries and dependencies, unit testing, and static application security testing. It's also important to deploy role-based access controls to protect your continuous integration and continuous delivery infrastructure from attackers seeking to run malicious code or steal credentials.

### Building and testing

Running automated security scripts on the test environment helps uncover potential issues that weren't previously detected. Some of the security tests you can run during this phase include dynamic application security testing, infrastructure scanning, container scanning, cloud configuration validation, and security acceptance testing.

### Production

Once the application is deployed to production, some organizations engage in penetration testing to try to find weaknesses in the live environment. In penetration testing, people adopt the mindset of an attacker and search for ways to breach the application.

### Operation

Even the best DevSecOps process won't catch everything, so it's critical to continuously monitor applications for vulnerabilities and threats. Analytics data can help you evaluate if your security posture is improving and highlight areas for optimization.

## DevSecOps Tools and Technologies

When choosing security tools, it's important to select ones that work well with your current DevOps technology. This will make it easier to incorporate security into your entire process. The following are a few of the types of tools you may need:

### Infrastructure as code scanning

To improve their efficiency, DevSecOps teams typically use open source tools like Terraform to manage and provision infrastructure like networks, virtual machines, and load balancers through code rather than doing it manually. Terraform helps ensure that infrastructure is set up and updated consistently across hundreds or thousands of servers. To reduce the risk that misconfigurations are deployed to the production environment, infrastructure as a code scanning tools automatically check the infrastructure at the code level for noncompliance with security policies and standards.

### Static application security testing

Before their code is compiled, DevSecOps developers begin testing their custom code for security vulnerabilities. This helps them fix issues without affecting the build. Static application security testing tools make this process easier with automatic checks and real-time feedback. Many tools identify exactly which code is risky and offer suggested fixes.

### Software composition analysis

One way that teams build applications and features more efficiently is by using third-party plug-ins and frameworks. These prebuilt tools save time, but they may also introduce risks, such as issues with the licensing, poorly written code, or security vulnerabilities. Software composition analysis tools identify open source components in applications and evaluate them against proprietary or free databases to detect license violations and security and quality issues.

### Interactive application security testing

During quality assurance testing or when an application is being used, interactive application security tools scan the code to find vulnerabilities and provide reports that identify where in the code the issue is.

### Dynamic application security testing

Dynamic application security testing emulates the methods a bad actor might use to attack an application. This testing occurs while the application is running and is based on predefined use cases.

### Container scanning

Containers are widely used in DevSecOps because they help developers easily deploy self-contained units of code. Within a container is a container image that includes the code that runs processes for the container. However, these images are often built using existing images or pulled from public repositories. Container scanning tools, scan containers and compare them against public or proprietary vulnerability databases to uncover potential security issues.

## DevSecOps Best Practices

DevSecOps is as much about culture change as process and tools. Here are some best practices to help make adopting this framework as smooth as possible.

### Shift the culture

Recognize that people may have a difficult time changing the way they work, and conflicts may arise. To help them adapt, clearly communicate the organization's goals and expectations, provide lots of opportunities for open dialog, and anticipate that you'll need to be flexible until teams find the tools, process, and cadence that work best for them.

### Define requirements and metrics

Establish a minimum-security baseline. For guidance refer to industry and regulatory requirements or The Open Worldwide Application Security Project® (OWASP) Top Ten critical risks to web applications and the SANS Top 25 software errors. Once you've defined requirements, determine which metrics you want to track to help you monitor your progress.

### Start small

Security automation tools offer many options for checking code for issues, but turning them all on, especially early in your adoption of DevSecOps, may overwhelm your team. Be judicious about which tools you implement and how many issues you scan for.

### Perform threat modeling

Develop a threat modeling process, which can be as simple or as detailed and technical as you need it to be. Use this approach to document a realistic security view of your application that includes:

- How attackers can abuse the application's design.
- How to fix vulnerabilities.
- Priority of different issues.

### Implement automation

Automation is key to enabling both quality and speed in the DevSecOps process. By embedding automated security scans during all phases of the continuous integration and continuous delivery lifecycle, you'll be able to improve the security of your applications without significantly slowing down the process.

### Manage dependencies

Most developers use third-party packages and libraries to efficiently build applications. The problem is that some of these solutions have security flaws, and developers aren't always diligent about keeping them up to date. To reduce your risk, make sure the components you use are vetted for security risks and develop a standardized process for updating them.

### Evaluate and improve

Regularly assess how the process is working and adjust as needed to ensure your organization is meeting its goals. A no-blame post-mortem after the completion of a sprint can help uncover opportunities for improvement. Analytics data and threat intelligence can also help you determine if there are security needs that aren't being met by your current approach.

## DevSecOps for cloud-native applications

Cloud-native applications are architected for the cloud and are usually vendor neutral, allowing them to be ported from one cloud to another. Designed to be highly scalable and resilient, development teams typically build them using microservices, containers, and automation, making them ideally suited for a DevSecOps process. Building continuous security, continuous integration, and continuous delivery into the development process for cloud-native applications enables scalability without compromising on security. Cloud security posture management (CSPM) solutions, like Microsoft Defender Security Posture Management, discover and address misconfigurations and vulnerabilities across your environment to help you secure your code and the entire DevOps pipeline. Once you've deployed your application to the cloud, cloud workload protection platforms (CWPP) help safeguard them and the underlying data by detecting and mitigating threats to workloads across multicloud environments.

## Learn more about Microsoft Security

### Microsoft Defender for Cloud
Protect multicloud and hybrid environments from development to runtime with a comprehensive cloud-native application protection platform.

[Learn more](#)

### Microsoft Defender for Cloud Apps
Modernize how you secure your apps, protect your data, and elevate your app security posture with this software as a service solution.

[Learn more](#)

### Microsoft Defender for Cloud Security Posture Management
Focus on your most critical risks across your multicloud environment with contextual cloud security posture management.

[Learn more](#)

## Frequently asked questions

**Expand all** | **Collapse all**

### How does DevSecOps work?

### What is DevSecOps in simple terms?

### What is shift left in DevSecOps?

### What is the DevSecOps framework?

The DevSecOps framework includes continuous integration, continuous delivery, and continuous security. It is a method by which security, operations, and security teams work together and share the responsibility for quickly delivering quality software, while reducing security vulnerabilities.

### What is the DevSecOps process?

There is no one DevSecOps process, but a common way that people run these projects is by dividing work into sprints each of which includes the following components: planning and development, build and test, and production. Throughout the sprint, teams use automation to continuously address quality assurance issues, continuously integrate, and continuously test for security risks.






# Reference
 - What is DevSecOps?, https://www.microsoft.com/en-us/security/business/security-101/what-is-devsecops
 - 
