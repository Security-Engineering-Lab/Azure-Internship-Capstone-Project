

# Designing and Implementing Platform Engineering
https://learn.microsoft.com/en-us/training/paths/designing-implementing-platform-engineering/


This learning path provides a comprehensive guide to designing and implementing platform engineering within modern enterprises. It covers the foundational principles, strategic alignment with business goals, and the practical aspects of building scalable, secure, and future-proof platforms. By following this path, learners will gain the knowledge and skills needed to enhance developer productivity, ensure operational excellence, and drive continuous innovation.

### Prerequisites
Successful learners will have prior knowledge and understanding of the following:

- Cloud computing concepts include understanding PaaS, SaaS, and IaaS implementations.
- Azure administration and Azure development with proven expertise in at least one of these areas.
- Intermediate to advanced DevOps concepts, including version control, Agile software development, and core software development principles. It would be helpful to have experience in an organization that delivers software.




# Foundations of Platform Engineering

This module introduces the core concepts and importance of platform engineering. It explores how platform engineering enhances developer productivity, accelerates time-to-value, and supports digital transformation. Learners will understand the strategic value of platform engineering as the foundation for both technical success and alignment with broader business goals.



# Introduction

Despite continuous efforts geared towards increasing developer productivity, building digital solutions in an optimal manner is getting increasingly complex. One of the important factors affecting this complexity is the dependency on the platform on which developers operate, including the underlying infrastructure, tools, services, and processes that drive development efforts. Optimizing this platform becomes even more challenging considering the pressure organizations place on shortening time-to-value, while, at the same time, expecting the highest levels of software quality and operational stability.

Platform engineering is meant to address these challenges. It's the practice of designing and building integrated platforms that enhance developer experience and accelerate time-to-value. By combining technologies such as infrastructure management, automation, self-service capabilities, and observability, platform engineering empowers developers to focus on delivering value without being burdened by the complexities of the underlying systems. At its core, platform engineering aligns development and operations teams, enabling the seamless delivery of applications and services while meeting business and operational goals.

With continuously growing adoption of cloud-native architectures and DevOps practices, platform engineering has become a critical discipline for any organization that aspires to derive the most value out of its internal development efforts. A well-engineered platform provides developers with the tools and processes they need to innovate faster while maintaining operational excellence. By embedding principles like scalability and resiliency, security and compliance, automation and self-service, as well as observability and continuous improvement into platform development, platform engineers create environments that aren't only developer-friendly but also robust and adaptable to changing business needs.

*"Platform Engineering streamlines development by creating tools that increase systems resiliency and enhance efficiency to accelerate value delivery."* - According to Luiz Macedo

The Platform Engineering learning paths are designed to guide and support you throughout your Platform Engineering learning journey. The module's content includes graphics, reference links, module review questions, and optional hands-on labs.

## Learning objectives

After completing this series, students and professionals can:

- Understand the importance of platform engineering in enhancing developer productivity and accelerating time-to-value.
- Learn how to design and build integrated platforms that optimize the developer experience and streamline development efforts.
- Explore the role of platform engineering in driving digital transformation within an enterprise.
- Recognize the strategic value of platform engineering as the foundation for both technical success and alignment with broader business goals.
- Identify key stakeholders in platform engineering and understand their distinct expectations and requirements
- Gain insights into designing platform architectures that are secure, scalable, and compliant with regulatory standards.
- Explore the role of automation in maintaining consistency, reducing manual errors, and accelerating deployments.
- Understand the importance of capacity planning and estimation for forecasting future resource needs.
- Learn cost optimization strategies to manage resources efficiently and avoid over-provisioning.
- Discover how to implement scalable solutions that can handle increasing demand and complex workflows.
- Learn how to enable developers to independently manage their resources and workflows, fostering agility and innovation.
- Understand the importance of combining flexibility with robust governance to ensure security, compliance, and operational consistency.
- Explore the benefits of developer self-service in accelerating development cycles and reducing bottlenecks.
- Recognize the role of self-service platforms in enhancing developer satisfaction and productivity.
- Identify best practices for implementing and managing self-service capabilities within an organization.
- Discover the significance of observability in providing real-time insights into system performance and identifying inefficiencies.
- Understand how continuous improvement creates a feedback loop that drives platform enhancements and optimizes resources.
- Learn about benchmarking and performance monitoring to track the success of the platform and identify areas for improvement.
- Explore strategies for adapting to market trends and anticipating shifts in user needs or technological landscapes.
- Foster a culture of innovation within platform engineering teams to continuously propose and test new ideas.
- Learn how to align platform engineering initiatives with long-term organizational goals and market trends.
- Explore key principles of strategic platform road mapping, including preparing for technological advancements and fostering innovation.
- Understand the importance of defining a clear platform vision that aligns with broader organizational goals.
- Discover how to build a platform roadmap with actionable milestones and specific deliverables.
- Learn techniques for phased implementation and prioritization to ensure the platform evolves in a way that supports business goals.

## Prerequisites

Successful learners will have prior knowledge and understanding of the following:

- Cloud computing concepts include understanding PaaS, SaaS, and IaaS implementations.
- Azure administration and Azure development with proven expertise in at least one of these areas.
- Intermediate to advanced DevOps concepts, including version control, Agile software development, and core software development principles. It would be helpful to have experience in an organization that delivers software.

If you're new to development practices and DevOps, consider taking the following:

- **Free online:** DevOps foundations: The core principles and practices.
- **Instructor-led course:** AZ-2008: DevOps foundations: The core principles and practices.
- **Free online:**
  - AZ-400: Development for enterprise DevOps.
  - AZ-400: Implement CI with Azure Pipelines and GitHub Actions.
  - AZ-400: Design and implement a release strategy.
  - AZ-400: Implement a secure continuous deployment using Azure Pipelines.
  - AZ-400: Manage infrastructure as code using Azure and DSC.
  - AZ-400: Design and implement a dependency management strategy.
  - AZ-400: Implement continuous feedback.
  - AZ-400: Implement security and validate code bases for compliance.
- **Instructor-led course:** AZ-400: Designing and Implementing Microsoft DevOps solutions.

If you're new to Azure and cloud computing, consider one of the following resources:

- **Free online:** Azure Fundamentals.
- **Instructor-led course:** AZ-900: Azure Fundamentals.

If you're new to Azure Administration, consider taking the:

- **Free online:** Prerequisites for Azure Administrators.
- **Instructor-led courses:** AZ-104: Microsoft Azure Administrator.

If you're new to Azure Developer, consider taking the:

- **Free online:** Create serverless applications.
- **Instructor-led courses:** AZ-204: Developing Solutions for Microsoft Azure.


# The Role of Platform Engineering in Modern Enterprises

Imagine you work for a rapidly growing e-commerce company striving to stay ahead in a fiercely competitive market. Your organization is expanding its digital presence to meet increasing customer demands for faster delivery, personalized experiences, and seamless transactions. However, as the number of services, applications, and systems grows, so does the complexity of managing them. Development teams struggle with inconsistencies across environments, long provisioning times, and fragmented tooling, while operational teams are overwhelmed by the need to maintain reliability and security across diverse infrastructures. To address these challenges, your company is exploring the role of platform engineering to build a unified system that fosters agility and innovation.

In this scenario, the importance of an efficient and scalable platform becomes evident. The platform must not only support developers with automated workflows and self-service capabilities but also act as a reliable backbone for business operations and innovation. By following the principles of platform engineering, your organization can connect its platform strategy to tangible business outcomes, such as reduced operational costs, accelerated feature delivery, and on-demand scalability.

## Overview of Platform Engineering

Platform engineering is about creating and managing a cohesive, integrated platform that supports developers in building, deploying, and maintaining applications. At its core, it combines infrastructure, tools, and processes into a unified framework that enhances developer productivity and operational efficiency. It is central to digital transformation, as it addresses the growing complexity of modern IT environments by abstracting away operational overhead and providing teams with streamlined, consistent workflows.

By automating repetitive tasks, incorporating security and compliance guidelines, and standardizing operations, platform engineering ensures organizations can scale their technology ecosystems while maintaining agility. Whether enabling cloud-native development, facilitating DevOps practices, or supporting hybrid infrastructures, platform engineering is the foundation for modern innovation.

## The Role of Platforms in Enterprise Ecosystems

In modern enterprises, platforms function as the backbone of digital ecosystems, providing the necessary infrastructure and tools to support a wide array of business functions. Platforms serve as the connective layer that links developers, operations teams, and end-users, ensuring seamless communication and collaboration. While developers are the primary consumers of these platforms, other contributors, such as data scientists and machine learning professionals, also rely on them to deliver data-driven insights and predictive models. It is important to address unique needs of all these users to drive innovation across the organization.

By centralizing resources and capabilities, platforms enable businesses to adapt to market changes more effectively. They facilitate the rapid deployment of new features or services, ensuring that enterprises remain competitive. They also enhance operational reliability by standardizing best practices across the organization, reducing risk and improving overall stability.

## Platform Engineering vs. Application Engineering

While platform engineering and application engineering are closely related, they have distinct roles within an organization. Platform engineering focuses on building and maintaining the infrastructure and tools that developers use to create applications. This includes creating self-service portals, standardizing environments, and embedding security and compliance measures.

Application engineering is primarily concerned with building user-facing applications or services. Since application engineers use platforms to streamline their workflows, the two disciplines are interdependent. A well-engineered platform can significantly enhance application development by reducing complexity and allowing developers to focus on delivering value. Similarly, feedback from application teams can help refine platform capabilities to better meet organizational needs.

## Business Value of Platforms

The business benefits derived from robust platform engineering are profound, since they directly contribute to tangible outcomes such as cost efficiency and faster time to market. By centralizing infrastructure and standardizing tools, platforms help reduce waste and duplication of efforts, as well as eliminate inefficiencies associated with fragmented systems. Automation further drives cost savings by minimizing manual effort and reducing operational errors.

Scalability is another important advantage. A well-designed platform can support rapid growth, accommodating highly dynamic workloads and business demands without compromising performance or security. Platforms accelerate innovation cycles by providing developers with the resources they need to build and deploy new features quickly, ensuring that businesses can respond to market demands in real time. This way, platforms become a strategic asset, driving both operational excellence and competitive advantage.


# Core Principles of Platform Design

A well-designed platform combines several core principles, such as security and compliance, scalability and resiliency, self-service and automation, observability and continuous improvement, and alignment with business goals. These core principles not only enhance user productivity but also enable platforms to evolve as new technologies emerge and organizational requirements change. By embedding advanced capabilities and robust processes, platform engineering teams create systems that deliver exceptional performance and foster continuous improvement.

## Security and Compliance

Security and compliance are foundational to any platform, particularly in industries like government, health, or financial services, where regulatory requirements are especially stringent. Practices such as adopting a zero-trust security model, embedding data encryption by default, and applying AI-driven threat detection tools are commonly implemented to address potential risks.

## Scalability and Resiliency

Scalability and resiliency ensure the platform remains operational and efficient during periods of increased demand or temporary disruption. Techniques such as multicloud architectures, proactive load testing, and predictive scaling algorithms help keep platforms adaptable to unanticipated events. Resiliency is reinforced by implementing self-healing mechanisms, such as automated instance recovery and by distributed fault-tolerant architectures, which minimize downtime and maintain service continuity.

## Self-Service and Automation

Self-service platforms empower developers to provision resources, deploy applications, and execute workflows on their own, reducing operational bottlenecks. This autonomy accelerates development cycles, enabling teams to focus on innovation rather than operational dependencies. Features such as infrastructure-as-code (IaC) frameworks, API-first designs, and declarative pipelines simplify platform interactions while maintaining governance.

## Observability and Continuous Improvement

Modern platforms require robust observability to provide real-time insights into performance, reliability, and user interactions. Observability uses such techniques as distributed tracing, real-time log aggregation, and AI-powered anomaly detection. These tools allow platform engineers to identify bottlenecks and preemptively address performance issues, ensuring uninterrupted operations.

Continuous improvement is integral to platform engineering because user requirements and expectations are never static. Platforms should empower teams to proactively use metrics and data trends to address operational challenges and inform the platform roadmap. Encouraging contributions from the broader community fosters innovation and ensures the platform evolves in response to diverse needs. By adopting a product-management mindset, platform teams can prioritize features that deliver value to many users, maintain alignment with organizational goals, and ensure the platform remains relevant and resilient.

## Business Alignment

Aligning the platform's capabilities with business objectives is vital to ensuring its success. Platforms should incorporate analytics to track metrics such as time-to-market, return on investment (ROI), and customer satisfaction, linking technical improvements directly to business outcomes. Features like real-time cost monitoring and resource optimization tools help align platform usage with organizational priorities.

Business alignment also requires collaboration between platform engineers and stakeholders. Establishing cross-functional governance structures and using strategic roadmaps ensures the platform evolves in tandem with organizational goals. Techniques such as scenario planning and AI-driven forecasting enable teams to anticipate future needs and proactively adjust the platform's trajectory.

## Shift-left, Start-right, and Stay-right

An effective internal developer platform not only delivers tools and capabilities to accelerate innovation but also strategically integrates shift-left, start-right, and stay-right practices to ensure the platform are optimized and aligned with organizational goals throughout its product lifecycle. These complementary approaches balance proactive development practices with ongoing operational excellence and compliance.

![Diagram showing the Platform Engineering lifecycle, including practices and tools.] 

**Shift-left** designates addressing issues early in the development process by embedding feedback mechanisms directly into developer workflows. Tools like real-time linting, CI pipeline checks, and IDE-integrated alerts for security or compliance violations empower developers to identify and resolve potential problems before they escalate. **Start-right** templates complement this practice by providing pre-configured, reusable patterns for infrastructure, applications, or deployment pipelines that incorporate best practices from the outset. These templates ensure developers start projects with a solid, compliant foundation, reducing any potential misconfigurations.

**Stay-right** focuses on enforcing governance, compliance, and operational standards during runtime and production. Automated policy enforcement for infrastructure-as-code combined with anomaly detection and self-healing for runtime ensure that systems remain secure, resilient, and performant under real-world conditions. By combining shift-left notifications, start-right templates, and stay-right governance, platform engineering teams establish a robust framework.


# Platform Engineering Capability Model

Platform engineering is meant to be a journey. A gradual, iterative approach is generally more effective than attempting a large-scale, immediate implementation or relying solely on top-down mandates. Incremental progress, starting with minimally viable products (MVPs), allows teams to refine their approach over time while incorporating feedback along the way.

The platform engineering lifecycle represents a structured approach to ensuring a platform is reliable, scalable, and continuously improving. This lifecycle encompasses distinct stages, each contributing to the platform's long-term success.

An essential element of the lifecycle is the Platform Engineering Capability Model, which provides a comprehensive framework for assessing, planning, and implementing platform engineering efforts. The model outlines maturity levels, best practices, and critical capabilities required at each stage of the lifecycle, ensuring alignment with organizational goals and user needs.

The model outlines the progress of maturing platform engineering practices across five stages: **Initial**, **Repeatable**, **Defined**, **Managed**, and **Optimizing**. In the Initial stage, organizations have limited structure, with ad hoc processes and minimal investment in platform capabilities. As they progress to the Repeatable stage, basic processes emerge, but adoption and governance remain inconsistent. The Defined stage marks the establishment of clear standards and processes, with users beginning to adopt platform solutions intentionally. In the Managed stage, platforms are actively governed, resources are provisioned and managed efficiently, and user interactions are consistent through standardized interfaces. Finally, in the Optimizing stage, platforms are continuously improved through robust feedback mechanisms, measured outcomes, and adaptive capabilities aligned with user needs and organizational goals.

The model is evaluated based on six capabilities: **Investment**, reflecting the allocation of resources and funding; **Adoption**, focused on user discovery and utilization; **Governance**, ensuring resource accessibility, cost control, and data/IP protection; **Provisioning & Management**, defining how resources are deployed and maintained; **Interfaces**, addressing user interactions with the platform; and **Measurement & Feedback**, emphasizing continuous improvement through performance metrics and user insights. Together, these capabilities closely align with the key areas outlined in the Cloud Native Computing Foundation's platform engineering maturity model and reflect the level of the organization's platform engineering maturity.

To use the Platform Engineering Capability Model, first assess where your organization currently stands in each of the six capability areas. You can perform this assessment manually or complete the Platform Engineering Capability Model survey. Once you've identified your current stages set future goals for growth and chart your organization's progress for each capability. The progress doesn't need to happen across all capabilities at once. Focus on the areas that make the most sense for your organization.

![Diagram showing key drivers and stages of the Platform Engineering Capability Model.]

## Investment

As the Investment capability evolves through each stage, its focus is on how staff and funds are allocated to platform capabilities, with an emphasis on budget and staffing, scope management, and measuring return on investment (ROI).

- **Initial (Voluntary):** Platform capabilities emerge out of necessity, driven by individual engineers voluntarily addressing immediate tactical needs. Budget and staffing are minimal, with work typically unfunded and performed alongside existing responsibilities. Solutions are narrowly scoped, targeting specific issues with limited knowledge sharing across teams. ROI is measured by how effectively immediate requirements are addressed and their impact on core project outcomes.

- **Repeatable (Ad-hoc Contributions):** Dedicated teams begin to address recurring challenges, such as inconsistent provisioning or security gaps, but efforts remain largely reactive. Budgets and staffing are limited to cross-cutting concerns, with constrained empowerment across the organization. Scope management focuses on specific issues without a broader platform-wide perspective. ROI is gauged by improvements in addressing key challenges, such as backlog reduction.

- **Defined (Operationalized - Dedicated Team):** Centrally funded platform teams emerge, focusing on accelerating software delivery and addressing technical requirements. Leadership begins fostering collaboration and implementing initial DevOps practices, but challenges remain in measuring team value. Budget and staffing are formalized for central teams to meet technical needs. Solutions become broader, addressing common challenges across teams, although the focus remains to be short term. ROI is measured by gains in delivery speed.

- **Managed (Scalable - As Product):** A cultural shift occurs, treating developers as customers with leadership emphasizing empathy and a product-led approach. Platform teams operate like product teams, staffed with developers, product managers, and user experience experts. Scope management aligns with product roadmaps, reviewed collaboratively with engineering teams to meet organization-wide needs. ROI is assessed through enhanced developer satisfaction, reflecting continuous improvements and alignment with user needs.

- **Optimizing (Enabled Ecosystem):** Investment focuses on innovation, maintaining platform relevance with contributions encouraged across the organization. Platform teams introduce advanced capabilities, such as security and performance enhancements, enabling product teams to build without relying on a centralized backlog. Budgets extend beyond central teams, with funding available across the organization. Scope management emphasizes enabling rapid, organization-wide knowledge sharing. ROI is measured through sustained improvements in developer satisfaction.

## Adoption

The Adoption capability focuses on how users discover and use your platform engineering solutions and their offerings, reflected by the discovery, selection, and usage of services, tools, and technologies. As organizations mature, the approach to adoption shifts from informal and sporadic usage to a more structured and participatory model where users actively engage with the platform, contribute to its evolution. This progression reflects how user discovery, decision-making, and usage practices evolve over time, from initial informal discovery to full participation in the platform's development.

- **Initial (Informal):** Adoption is inconsistent, with teams independently improving processes without organization-wide coordination. External tools are often preferred over internal ones. Platforms are discovered informally, mainly through word-of-mouth or chance encounters, with engineering teams selecting services based on their specific needs. Each team maintains its own scripts and tools tailored to its unique requirements.

- **Repeatable (Mandated):** The organization mandates the use of shared platforms, but capabilities are limited to common use cases, making it difficult to accommodate unusual requirements. User discovery relies on platform team guidance, often through internal documentation or directives. Teams may select mandated services through informal discussions with the platform team. Despite processes being built around platform standards, teams may not fully adopt them or may be unsatisfied with the results.

- **Defined (Advertised):** Platform capabilities are actively promoted, aligning with team needs. The platform team collaborates with engineering teams to offer high-quality services that reduce operational overhead. However, some teams might still experience low ROI due to reliance on outdated practices and technical debt. Teams discovers capabilities through directives covering typical use cases, and the platform team encourages usage through collaboration. Advocacy for platform use also occurs informally through team ambassadors.

- **Managed (Value Driven):** Product teams recognize and choose platform capabilities for the clear value they provide in reducing cognitive load and offering high-quality services. Platforms are supported by extensive documentation, ergonomic interfaces, and self-service UX for quick provisioning. Teams now prefers internal platforms over building solutions themselves or relying on external providers. Discovery and decision-making are streamlined, with teams using templates, forums, and documentation to fully support platform adoption.

- **Optimizing (Participatory):** Product teams actively contribute to improving platform capabilities by suggesting new features and fixes. Processes are in place for users to identify requirements and collaborate on contributions. Developer advocates and ambassadors foster an internal community, extending platform ownership to contributors. Platform engineers work closely with product teams to understand needs and suggest new capabilities, empowering users to submit pull requests and engage in reviews.

## Governance

As the Governance capability evolves, its focus is on ensuring that users have access to the resources and capabilities they need, while managing costs, data, and intellectual property. This progression is assessed based on several categories, including defining policies and frameworks, implementing policies, monitoring and mitigating compliance, and managing access. Governance evolves from manual and reactive processes to an integrated, predictive system that balances centralized control with adaptive management for evolving needs.

- **Initial (Independent):** Governance is manual, relying on centralized control and gatekeeping, which hinders scalability. Developers and security teams work independently, responding reactively to policy violations. Compliance is maintained through minimal standards, with security measures often being added as afterthoughts. Access permissions are granted based on immediate needs, without a standardized process.

- **Repeatable (Documented):** The organization starts documenting and sharing policies, but these remain basic and inconsistently applied. Governance tools like ticketing systems are introduced to manage policy reviews, but the process remains manual and slow. Audit processes are established but still reactive. Some roles and permissions are standardized, but enforcement remains uneven.

- **Defined (Standardized):** Governance becomes centralized and standardized to improve consistency and efficiency across all teams. Policies are documented and centrally managed, with some degree of automation in the implementation process. Key governance standards are upheld through regular auditing, and access control is automated with a formal RBAC system, though development teams still have limited control over policy changes.

- **Managed (Integrated):** Security and compliance are seamlessly integrated into workflows, with automation ensuring policies are consistently applied across systems and teams. Real-time monitoring and advanced analytics help detect and prevent gaps in governance. Policies are embedded into CI/CD pipelines, and access management is governed by least privilege principles with automated reviews, ensuring a more proactive and integrated approach to governance.

- **Optimizing (Predictive):** Governance becomes dynamic and context-aware, responding to changing conditions and optimizing access control. Predictive analytics help identify potential risks before they occur, enabling proactive mitigation. Policies are continuously refined using advanced analytics, and access control dynamically adjusts based on real-time factors such as user location and access time, ensuring compliance while enabling tailored workflows.

## Provisioning and Management

With the Provisioning and Management capability, the focus is on how users create, deploy, and manage resources. The process evolves from manual, siloed operations to an adaptive, automated system that balances flexibility with governance, ensuring resources are provisioned efficiently while meeting compliance requirements. This progression spans stages categorized by defining provisioning processes, responding to and managing requests, and monitoring resource allocation.

- **Initial (Manual):** Developers manually set up infrastructure based on guidance from IT or Architecture teams, leading to inconsistencies and delays. Without standardized processes, requests are reviewed manually, increasing the risk of errors. This approach becomes unsustainable as demand grows, with siloed operations creating inefficiencies.

- **Repeatable (Coordinated):** The organization begins to centralize provisioning processes by using ticketing systems to manage infrastructure requests. While manual approvals are still required, some errors are reduced, but bottlenecks remain. Teams starts using standard tools for monitoring resources, although the view remains siloed and project-specific.

- **Defined (Paved):** Provisioning processes are formalized across the organization using Infrastructure as Code (IaC), standardizing templates and tools. Requests are handled through structured workflows, though the platform team may struggle with increasing demand. Centralized dashboards allow for monitoring resource allocation, providing better performance insights.

- **Managed (Automated):** Provisioning becomes automated and integrated into CI/CD pipelines, minimizing manual effort and ensuring consistent deployments. Governance and compliance checks are embedded into workflows. Automated self-service capabilities allow users to provision resources within controlled parameters. Scaling is automated based on usage patterns to optimize performance.

- **Optimizing (Adaptive):** Provisioning becomes adaptive, using intelligent systems to anticipate infrastructure needs in real time. This approach ensures efficient resource allocation while maintaining governance and compliance. Systems proactively handle requests, balancing flexibility with governance, while performance and cost-efficiency are optimized through predictive analytics.

## Interfaces

In the Interfaces capability, the primary consideration is how users interact with and consume the platform services and products. Its advancements focus on establishing standards, increasing user autonomy, and seamlessly integrating platform capabilities into existing workflows. The approach evolves from inconsistent, manual processes to a self-service, integrated system that enhances user experience and operational efficiency.

- **Initial (Custom Processes):** Users interact with the platform through various inconsistent, custom processes that address immediate needs but lack standardization. Engineers independently set up environments by consulting colleagues or relying on personal practices, and they select tools and processes for diagnosing application behavior without any established guidelines. Knowledge sharing is informal, and provisioning services often require deep support from providers due to the lack of formalized processes, which limits scalability and efficiency.

- **Repeatable (Local Standards):** Engineers and teams begin informally defining standards to enhance knowledge sharing, though consistency remains a challenge due to reliance on individual commitment. Some teams may use documentation or containers to define their setup processes, but these practices diverge over time, requiring effort to reconcile. Diagnosing application behavior becomes more standardized within teams, with some reliance on DevOps or IT teams for access to deployed resources. While local standards emerge, they remain loosely defined and inconsistent across teams.

- **Defined (Standard Tooling):** Interfaces become more consistent, with the introduction of standardized tooling and documented practices. Central teams manage templates and documentation, with so-called paved roads or golden paths guiding how capabilities should be provisioned and observed. These tools and processes meet broad organizational needs, although expert support is still often required. Teams may modify templates, but changes aren't always integrated back centrally, which can lead to some inefficiencies in maintaining consistency. Diagnosing application behavior follows standardized practices for accessing and analyzing deployed resources, providing greater consistency across teams.

- **Managed (Self-Service Solutions):** The platform enables greater user autonomy by providing self-service solutions with minimal maintainer support. Users have access to consistent, easy-to-use interfaces that allow them to discover and modify templates, creating a user-centric environment that enhances usability. Tools for diagnosing application behavior and observing resources are made available on demand through the platform, ensuring users have the resources they need without heavy dependence on external teams. Knowledge sharing is facilitated through discovery and modification of templates, which increases the value of platform capabilities.

- **Optimizing (Integrated Services):** Platform capabilities are seamlessly integrated into the tools and processes that teams already use, such as CLI or IDEs, making them a natural part of users' workflows. Some capabilities are automatically provisioned based on user needs, and the platform provides flexible building blocks for higher-level use cases that may require deeper customization. Platform teams continuously assess which capabilities are most effective, guiding further investments to optimize platform offerings. The platform automatically sets up observability for deployed applications, offering real-time access to diagnostic data and streamlining the process of monitoring and managing application behavior.

## Measurements and Feedback

The Measurements and Feedback capability involves gathering, analyzing, and incorporating metrics and feedback to assess the success of platform engineering practices. Its maturity is reflected by transitioning from ad-hoc and informal methods to a proactive, data-driven culture where feedback and insights are integrated into continuous improvement processes, guiding strategic decisions and platform development.

- **Initial (Ad-hoc):** In the initial stage, measurement and feedback processes are inconsistent and fragmented. Metrics are gathered without clear alignment to organizational goals, resulting in incomplete and unreliable data. Feedback is collected informally and often anecdotal, with minimal engagement from stakeholders. As a result, decisions are made based on limited information, and measuring the true ROI of platform engineering practices is difficult. Documentation of feedback and outcomes is minimal, and learnings are rarely captured or shared.

- **Repeatable (Structured Processes):** Basic feedback mechanisms, such as surveys or forums, are established to capture user experiences more systematically, but these processes still vary across teams. The measurement of success is often focused on activity-based metrics such as deployments or timelines, providing some insight into performance but lacking a broader, outcome-based perspective. Feedback remains informal and bottom-up, though it starts influencing planning. There's some effort to engage stakeholders, but it's still limited, and initial documentation of processes and feedback is created but isn't comprehensive or consistently utilized.

- **Defined (Consistent):** Feedback collection becomes more formalized and standardized, allowing for deeper insights into user needs and key metrics. Metrics shift towards outcome-based measurements, such as developer productivity, though linking them to financial performance remains a challenge. Feedback analysis is systematic, using both qualitative and quantitative methods, and standard metrics like DORA (DevOps Research and Assessment is a set of metrics that measure software delivery performance, including lead time, deployment frequency, mean time to restore, and change failure rate) or SPACE (Satisfaction and well-being, Performance, Activity, Communication and collaboration, and Efficiency is a framework used to measure developer productivity across these five dimensions) are employed. Regular review sessions with cross-functional teams ensure active engagement with stakeholders. Comprehensive documentation of feedback processes, outcomes, and lessons learned is maintained and shared across teams.

- **Managed (Insights):** At this stage, feedback mechanisms and measurement frameworks are robust and focused on strategic business outcomes. Data-driven insights guide platform operations, and feedback is integrated into platform roadmaps, driving continuous improvements. Advanced analytics are employed to assess the platform's impact on business outcomes, such as revenue growth, and feedback is correlated with performance metrics to identify key areas for strategic improvement. Stakeholders across the organization are deeply involved in the feedback process, with structured collaboration to avoid silos. Real-time, dynamic documentation reflects ongoing feedback and lessons learned, accessible to all stakeholders.

- **Optimizing (Proactive):** Feedback and measurement processes are closely integrated into the organization's culture, creating a proactive approach to anticipating and adapting to future challenges and opportunities. Predictive analytics and advanced metrics are used to forecast future needs and opportunities, enabling the platform to continuously evolve in response to changing conditions. Feedback is fully integrated into a continuous improvement cycle, and a culture of feedback is established across all levels of the organization. Dynamic, real-time documentation reflects ongoing feedback and is continuously updated, ensuring that lessons learned are shared and accessible to all stakeholders.




# 1.5 Core Aspects of Platform Implementation

Platform engineering is a multidisciplinary approach that combines software engineering, system design, and operational excellence to create a reliable and scalable infrastructure for building and deploying applications. At its core, it involves not just building robust platforms, but creating a self-service environment that empowers development teams while ensuring alignment with business goals. A successful platform engineering initiative starts with the right team and a clear understanding of the problem space. This foundation enables the development of systems that streamline operations, reduce friction, and allow developers to focus on building applications rather than managing infrastructure.

Once the team is in place, the focus shifts to automating high-toil areas, identifying manual, repetitive tasks that can be automated to save time and reduce errors. Following this, an inventory of existing resources is essential, allowing teams to centralize tools and services, making them easier to manage and scale. The next step is referred to as blazing paved paths, which involve creating standard workflows and environments that ensure consistency across projects. Afterwards, deploying environments as a service helps to further streamline processes, enabling teams to quickly spin up environments on demand. At that point, the primary objective becomes optimizing self-service developer experiences, empowering developers to manage their workflows independently while ensuring they have the tools and support necessary for success. This approach transforms how development teams interact with infrastructure, creating an agile, high-performing environment for building and delivering applications.

![](https://learn.microsoft.com/en-us/training/wwl-azure/foundations-platform-engineering/media/platform-engineering-steps-b77624b8.png)

Besides having clearly defined implementation plan, rather than approaching platform engineering as a single, broad concept, it can be helpful to break it down into four main areas to facilitate the implementation process:

**Engineering Systems**, which includes the tools and services that enable development, such as CI/CD, package management, cloud-based coding environments, code scanners and linters, as well as Artificial Intelligence (AI) assistants such as GitHub Copilot.

**Application Platform**, which consists of curated selection of services used as building blocks of commonly used app stacks (for example, Azure Policy, Azure Key Vault, Azure Container Apps, or Cosmos DB).

**Application Templates**, which provide well-defined, organization-specific templates to facilitate workload provisioning and align with best practices.

**Developer Self-Service Capabilities**, which enable developers to autonomously manage their workflows while ensuring governance and compliance with organizational standards.

Incorporating these areas into your implementation strategy reduces developer toil, fosters innovation, and creates a seamless development experience.

![](https://learn.microsoft.com/en-us/training/wwl-azure/foundations-platform-engineering/media/platform-engineering-areas-a3a98aa7.png)

## Build a team

In a platform engineering organization, fostering the right culture is essential for long-term success. Transitioning from a reactive to a proactive culture is key, where platform teams take responsibility for building and maintaining tools to support the organization. This shift is crucial for reducing knowledge silos and operational disruptions. The success of platform engineering efforts aligns with the investment capability outlined in the Platform Engineering Capability Model, which emphasizes moving through stages of organizational maturity—from provisional to optimizing. At the provisional stage, companies recognize the need for platform engineering but may lack full alignment between leadership and development teams. As organizations mature, executive buy-in and cultural shifts encourage a more collaborative, innovative environment where platform teams are empowered to drive meaningful change, enabling organizations to scale effectively.

A platform engineering team requires a diverse set of technical skills and a product-centric mindset to build and scale reliable, efficient, and secure internal developer platforms. Platform engineers are expected to be proficient in several key areas, including container orchestration (for example, Kubernetes), CI/CD pipelines (for example, GitHub Actions, Azure Pipelines), and monitoring tools (for example, Azure Monitor, Prometheus, Grafana). Expertise in Infrastructure as Code (IaC) tools like Terraform and Bicep is critical for automating infrastructure provisioning. Additionally, platform engineers should be comfortable writing code in scripting languages such as Python, PowerShell, or Bash to enable automation and integration across systems. While the talent pool for platform engineers can be challenging to tap into, a successful team should combine expertise from diverse backgrounds, such as software development, site reliability engineering (SRE), and IT operations.

## Automate high toil areas

Automating high-toil areas commonly represents the first paved path on the road to enabling developer self-service capabilities. To implement it, start by identifying frequent, error-prone, or labor-intensive processes, especially those tied to manual or service-desk operations. Next, assess factors like process frequency, complexity, and auditability to prioritize automation targets. Implementing infrastructure as code (IaC) in your continuous delivery (CD) pipelines not only streamlines application deployment but also enables dynamic provisioning of shared infrastructure and tools. Use flexible CI/CD platforms like GitHub Actions and Azure DevOps, or GitOps solutions like Flux and Argo CD to reduce bottlenecks and empower teams.

Over time, adopting the "Everything as Code" (EaC) pattern creates a secure and repeatable automation framework, using centralized Git repositories for IaC templates and configurations (including, for example, Bicep and Azure Resource Manager templates, Terraform manifest files, and Helm charts). These repositories, managed by an operations team, enable developers to submit pull requests that are securely reviewed and audited before merging. The same CI/CD tools can then provision and configure any infrastructure, tools, or services—whether application-specific or shared. This approach supports scalability, developer self-service, and seamless integration with governance processes, ensuring that platform engineering aligns with organizational goals while fostering operational agility.

The "Everything as Code" approach revolves around representing nearly any resource or process as a file in a secure Git repository. Git's robust security features—such as commit history, access controls, pull requests, and branch protections—ensure transparency, enable collaborative reviews, and enforce automated checks before changes are integrated. Combined with CI/CD systems, this creates a versatile, auditable, and secure framework for managing infrastructure, tools, and processes.

## Inventory and centralize

As organizations grow, the volume and complexity of their technical assets expand, often leading to duplication of efforts, orphaned projects, and wasted resources. Centralizing inventory and asset tracking is a critical step in platform engineering to address these challenges. An inventory system allows teams to track and manage assets like code, APIs, containers, virtual machines (VMs), permissions, and more. This process not only improves governance but also promotes reuse and enhances discoverability, enabling teams to operate more efficiently and effectively.

Centralized inventories play a vital role in improving governance by tagging and organizing assets. Proper tagging ensures that resources are associated with their respective owners or teams, making it easier to manage lifecycles and understand the potential impact of changes. Enhanced discoverability is another key benefit, as it reduces technical sprawl by helping teams find and reuse existing resources, preventing unnecessary duplication of effort. Additionally, centralizing inventories helps organizations optimize resources by identifying and cleaning up outdated or unnecessary assets, leading to reduced waste and increased cost savings.

Various tools support inventory and asset tracking, each catering to different aspects of the technical ecosystem. For instance, Azure Deployment Environments (ADE) provides a way to track complex infrastructure created through Infrastructure as Code (IaC). Similarly, Azure API Center enables developers to discover and manage APIs efficiently. Package registries such as GitHub Packages or Azure Artifacts offer extra value by improving supply chain security and managing approved packages and SDKs.

To further enhance the benefits of inventory systems, organizations can establish relational links between assets to create a more comprehensive view of their ecosystem. For example, mapping the relationships between an API definition, its code repository, associated environments, and governance policies allow teams to manage resources with greater precision.

## Blaze paved paths

In platform engineering, the "paved path" analogy conveys the balance between fostering innovation and providing standardized guidance. Initially, teams may take varied, informal paths to achieve their goals, experimenting with different tools and workflows. Over time, platform teams observe the most effective and widely adopted approaches and convert them into "paved paths"—optimized workflows that are efficient, user-friendly, and compelling for teams to adopt.

This process, often described as "blazing paved paths," involves identifying common patterns in team workflows and transforming them into standardized, scalable solutions. These paths seamlessly integrate security, architectural best practices, and compliance requirements, offering a smooth and reliable experience. Developers benefit from reduced cognitive load, consistent APIs for integration, modular capabilities that can be combined as needed, and predictable performance that aligns with operational goals.

The Platform Engineering Capability Model plays a pivotal role in this process, helping organizations determine when to transition from informal paths to paved ones. It identifies areas requiring standardization and provides insights into how to scale these practices effectively. This structured approach ensures innovation isn't stifled while maintaining a focus on quality, compliance, and performance.

The blaze paved paths approach encourages good practices without being overly prescriptive. It supports community contributions, enabling teams to collaborate and shape the platform while retaining flexibility for unique use cases. By balancing innovation and standardization, this methodology fosters an environment where teams can excel while ensuring organizational requirements are consistently met.

![](https://learn.microsoft.com/en-us/training/wwl-azure/foundations-platform-engineering/media/platform-engineering-unsupported-b3a1434a.png)

![](https://learn.microsoft.com/en-us/training/wwl-azure/foundations-platform-engineering/media/azure-deployment-environments-f5fbc834.png)

## Deploy environments as a service

Deploying environments as a service is designed to enable secure, standardized, and automated provisioning of infrastructure. A key principle in this approach is persisting provisioning identities and secrets in a way that prevents developers from accessing them directly. This enforces governance while ensuring infrastructure updates remain secure. For instance, Azure Deployment Environments (ADE) exemplify this model by supporting role separation and centralizing the management of IaC templates.

With ADE, platform engineers and operations teams collaboratively build and maintain a catalog of templates for specific environment types. These templates, enriched with pre-configured settings, integrate managed identities and control access based on roles. Developers can then use CI/CD pipelines to provision infrastructure through tools like the Azure CLI or Azure Developer CLI, without needing direct access to sensitive credentials or the underlying subscription. This separation ensures compliance and security while preserving developer productivity.

![Diagram showing the Platform Engineer workflow with Dev Center Catalog, Environment type mappings, portal and automated deployment pipelines.]

Even if ADE isn't in use, the same principles can be applied more broadly, with infrastructure as code (IaC) content sourced from secure, immutable locations and secret management automated and isolated. By enabling these practices, platform engineering empowers teams to deploy consistent environments while maintaining organizational governance and operational efficiency.

## Optimize self-service developer experience

A seamless self-service developer experience is crucial for platform engineering success, but achieving this often requires meeting users where they are. Every role—developers, operations, and others—gravitate towards specific tools and environments that define their workflows. For new experiences to gain adoption, it's important to align with these existing "centers of gravity." A pragmatic approach involves planning multiple user interfaces tailored to the tools already in use, allowing teams to start with simple enhancements, prove their value, and evolve toward more sophisticated solutions as needs arise.

Instead of creating entirely new experiences, consider enhancing and integrating existing tools. Platforms like editors, Integrated Development Environments (IDEs), DevOps suites, CLI tools, and low-code environments often have extensibility models that allow customization and expansion with minimal overhead. This approach reduces maintenance, applies familiar user experiences, and accelerates adoption. For example, web-based IDE extensions, like those built for VS Code or vscode.dev, provide a flexible, web-compatible starting point that can scale to local development environments. Similarly, ChatOps interfaces in tools like Microsoft Teams or Slack offer intuitive ways to trigger automation workflows and integrate with CI/CD platforms.

For organizations needing a centralized interface, investing in a custom developer portal can provide long-term benefits but requires careful planning and resources. Solutions like Backstage.io, a toolkit initially developed by Spotify, offer highly customizable portals that can integrate plugins and third-party tools, creating a dynamic developer-centric hub. Whether you start with lightweight solutions like Power Pages or build out a comprehensive portal, the goal is to deliver scalable, user-friendly experiences that empower developers while aligning with organizational needs.




# 1.6 Module assessment

Use the following questions to check what you've learned in this module.

## Check your knowledge

### 1.
**What is the primary role of platform engineering in an organization?**

- Building user-facing applications or services.
- Creating marketing strategies for the company's products.
- **✅ Creating and managing a cohesive, integrated platform that supports developers in building, deploying, and maintaining applications.**

**Пояснення:** Platform engineering фокусується на створенні інтегрованих платформ, які підтримують розробників у всьому циклі розробки, розгортання та підтримки додатків.

### 2.
**What is the purpose of implementing shift-left, start-right, and stay-right practices in platform engineering?**

- To enforce governance and compliance only during the runtime and production.
- To focus solely on the development process and ignore operational standards.
- **✅ To ensure the platform is optimized and aligned with organizational goals throughout its product lifecycle.**

**Пояснення:** Ці практики забезпечують оптимізацію платформи та відповідність організаційним цілям протягом усього життєвого циклу продукту - від розробки до виробництва.

### 3.
**What is the primary focus of the Interfaces capability in the Platform Engineering Capability Model?**

- **✅ It considers how users interact with and consume the platform services and products.**
- It focuses on how users create, deploy, and manage resources.
- It involves gathering, analyzing, and incorporating metrics and feedback to assess the success of platform engineering practices.

**Пояснення:** Interfaces capability зосереджується саме на тому, як користувачі взаємодіють з платформою та споживають її сервіси та продукти.

### 4.
**What is the primary goal of deploying environments as a service in platform engineering?**

- **✅ To enable secure, standardized, and automated provisioning of infrastructure.**
- To allow developers direct access to sensitive credentials and underlying subscription.
- To decentralize the management of Infrastructure as Code (IaC) templates.

**Пояснення:** Основна мета - забезпечити безпечне, стандартизоване та автоматизоване розгортання інфраструктури, при цьому розробники НЕ отримують прямий доступ до чутливих даних.



# 1.7 Summary

Our coverage of foundations of platform engineering demonstrates its vital role in enabling organizations to remain competitive, efficient, and innovative. While technical excellence is a foundational component, true success lies in how well the platform integrates with broader organizational objectives. Whether improving developer workflows, enhancing customer experiences, or optimizing operational efficiency, platform engineering is most impactful when its goals and outcomes align with business priorities.

Central to this alignment is the focus on collaboration, adaptability, and continuous improvement. Platform engineering must bridge technical and non-technical domains, ensuring that its capabilities address both the immediate needs of users and the strategic direction of the organization. Through an iterative approach, guided by meaningful metrics and driven by cross-functional cooperation, the platform evolves to meet dynamic market conditions and operational challenges.

Ultimately, platform engineering is more than a technical endeavor; it's a strategic function that unlocks value across the organization. By fostering an ecosystem of innovation, standardization, and responsiveness, platform teams not only support but actively drive business success.

This module explored the key areas that organizations must apply to start their Platform Engineering transformation Journey.

You learned how to describe the benefits and usage of:
- Understand the importance of platform engineering in enhancing developer productivity and accelerating time-to-value.
- Learn how to design and build integrated platforms that optimize the developer experience and streamline development efforts.
- Explore the role of platform engineering in driving digital transformation within an enterprise.
- Recognize the strategic value of platform engineering as the foundation for both technical success and alignment with broader business goals.
- Identify key stakeholders in platform engineering and understand their distinct expectations and requirements.

## Learn more
- Platform engineering guide.
- Platform Engineering Maturity Model.
