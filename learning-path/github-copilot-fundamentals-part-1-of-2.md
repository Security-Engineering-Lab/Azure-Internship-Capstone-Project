

 # GitHub Copilot Fundamentals Part 1 of 2
 https://learn.microsoft.com/en-us/training/paths/copilot/

# Explore the Fundamentals of GitHub Copilot

Explore the fundamentals of GitHub Copilot and its potential to enhance productivity and foster innovation for both individual developers and businesses. Discover how to implement it within your organization and unleash its power for your own projects.

## In this learning path, you'll:

- Gain a comprehensive understanding of the distinctions between GitHub Copilot Individuals, GitHub Copilot Business, and GitHub Copilot Enterprise
- Understand how to utilize GitHub Copilot across various environments responsibly and securely
- Learn advanced functionalities of GitHub Copilot and how to best use them

## Prerequisites

- Basic understanding of GitHub fundamentals

# 1 Responsible AI with GitHub Copilot

This module explores the responsible use of AI in the context of GitHub Copilot, a generative AI tool for developers. It will equip you with the knowledge and skills to leverage Copilot effectively while mitigating potential ethical and operational risks associated with AI usage.

# 1.1 Introduction

This module explores the responsible use of AI in the context of GitHub Copilot, a generative AI tool for developers. It equips you with the knowledge and skills to use Copilot effectively while mitigating potential ethical and operational risks associated with AI usage.

## Learning Objectives

By the end of this module, you'll be able to:

- Understand and apply the principles of Responsible AI usage
- Identify limitations and mitigate risks associated with AI
- Learn best practices for ensuring AI-generated code aligns with ethical standards and project-specific requirements
- Recognize the importance of transparency and accountability in AI systems in building trust and maintain user confidence

# 1.2  Mitigate AI Risks

Artificial Intelligence (AI) presents numerous opportunities for innovation and efficiency, but it also comes with significant risks that need to be carefully managed.

One of the primary concerns is that AI systems can sometimes make decisions that are difficult to interpret, leading to a lack of transparency and accountability. Additionally, AI can result in unintended and harmful outcomes, such as biased decision-making or privacy violations.

To mitigate these risks, it is essential to implement robust governance frameworks, ensure transparency in AI processes, and incorporate human oversight. By doing so, organizations can harness the benefits of AI while minimizing potential negative impacts.

In the next section, we'll discuss the concept of responsible AI and how to apply its principles to reduce the risks associated with AI tools like GitHub Copilot.

## What is Responsible AI?

Responsible AI is an approach to developing, assessing, and deploying artificial intelligent systems in a safe, trustworthy, and ethical way. AI systems are the product of many decisions made by the people who develop and deploy them. From system purpose to how people interact with AI systems, Responsible AI can help proactively guide these decisions toward more beneficial and equitable outcomes. That means keeping people and their goals at the center of system design decisions and respecting enduring values like fairness, reliability, and transparency.

In the next unit, we'll cover Microsoft and GitHub's Six Principles of Responsible AI.



# 1.3 Microsoft and GitHub's Six Principles of Responsible AI

*Diagram showing six key principles that should guide AI development and usage.*

Microsoft is a global leader in Responsible AI, identifying six key principles that should guide AI development and usage. These principles are:

- **Fairness:** AI systems should treat all people fairly
- **Reliability and safety:** AI systems should perform reliably and safely
- **Privacy and security:** AI systems should be secure and respect privacy
- **Inclusiveness:** AI systems should empower everyone and engage people
- **Transparency:** AI systems should be understandable
- **Accountability:** People should be accountable for AI systems

Now, let's explore each of these principles in greater detail to understand how they guide responsible AI practices.

## Fairness: AI systems should treat all people fairly

AI systems should treat everyone fairly, avoiding differential impacts on similarly situated groups. In contexts like medical treatment, loan applications, or employment, AI should provide consistent recommendations to individuals with similar symptoms, financial situations, or qualifications.

### Employs techniques to detect bias and mitigate unfair impacts such as:

- Reviewing training data
- Testing models with balanced demographic samples
- Using adversarial debiasing
- Monitoring model performance across user segments
- Implementing controls to override unfair model scores

Training AI models on diverse and balanced data can help reduce biases, ultimately promoting fairness.

## Reliability and safety: AI systems should perform reliably and safely

To build trust, AI systems must operate reliably, safely, and consistently.

These systems need to function as designed, respond safely to unexpected conditions, and resist harmful manipulation. Their behavior and the variety of conditions they handle reflect the foresight of developers during design and testing.

Safety in AI refers to minimizing unintended harm, including physical, emotional, and financial harm to individuals and societies. Reliability means that AI systems perform consistently as intended without unwanted variability or errors. Safe and reliable systems are robust, accurate, and behave predictably under normal conditions.

## Privacy and security: AI systems should be secure and respect privacy

As artificial intelligence (AI) becomes more common, it's important to protect user privacy and data security. Microsoft and GitHub are aware of this tenet and both companies include privacy and security as key parts of their Responsible AI plan. This plan focuses on using principles to guide data practices.

Microsoft and GitHub's approach to Responsible AI aims to stop abuse and keep user trust. Key points include:

### Data Collection and Consent
- **Getting users' permission** before collecting their data. Clearly explain how the AI uses their data and get their consent. Don't collect data secretly. Let users choose if they want to share personal data and inform them through clear prompts and policies.
- **Collecting only the data needed** for the AI to work. Avoid gathering extra information and remove sensitive data once the AI is in use. Regularly check data inputs to ensure only essential data is collected.

### Data Protection
- **Anonymizing personal data.** Use methods like pseudonymization and aggregation to protect identities. Pseudonymization replaces personal details with random identifiers, while aggregation groups data into summaries, removing specific individual details.
- **Encrypt sensitive data** both during transfer and when stored. Use strong encryption methods and secure keys through:
  - Hardware Security Modules (HSMs) which store keys in a tamper-proof environment
  - Secure vaults like Microsoft Azure for key storage with controlled access
  - Envelope encryption, which uses two keys for added security

Organizations should control who can access keys and models, rotate keys regularly, and securely back up keys. They should also limit employee access to sensitive models and data, classify them based on sensitivity, and conduct regular security audits to prevent unauthorized access.

## Inclusiveness: AI systems should empower everyone and engage people

Inclusiveness means ensuring that AI systems are fair, accessible, and empower everyone. Microsoft's Responsible AI standard recognizes that AI creators (including GitHub) must proactively design AI to include all people, communities, and geographies - especially those areas of society historically underrepresented.

### Microsoft's Responsible AI standard for inclusiveness means:

- AI systems work well for diverse users and groups. They don't disadvantage some people.
- AI systems are accessible. Anyone can use AI systems easily, regardless of physical or mental abilities.
- AI systems are available worldwide, even in developing countries/regions. AI systems can't exclude certain geographies.
- People from different backgrounds and communities provide input into the development of AI systems.
- AI systems allow all users to benefit equally from their capabilities. They must empower everyone.

### Examples of inclusive AI include:

- Facial recognition that works across skin tones, ages, and genders
- Interfaces that support screen readers for the visually impaired
- Language translation that supports small regional dialects
- Teams that seek diverse perspectives when designing systems

Microsoft's Responsible AI standard requires that everyone can access AI systems, regardless of their disability, language, or infrastructure barriers. Responsible AI solutions must enable full global inclusion by:

- Offering alternative modes of interaction such as voice control, captions, and screen readers
- Supporting adaptation into different languages and local cultural contexts
- Working offline and with limited connectivity and computing resources

## Transparency: AI systems should be understandable

Microsoft's Responsible AI principle of Transparency emphasizes that AI systems must be understandable and interpretable. AI creators should:

- Explain how their systems operate clearly through a clear validation framework
- Justify the design choices behind AI systems
- Be honest about the capabilities and limitations of AI systems
- Enable auditability with logging, reporting, and auditing capabilities

Transparency is essential to build trust, ensure accountability, promote fairness, enhance safety, and support inclusiveness. Implementing transparency involves documenting data and models, creating explanatory interfaces, using AI debugging tools, constructing testing dashboards, and enabling logging and auditing. By being transparent, AI creators can foster trust and responsible AI use.

## Accountability: People should be accountable for AI systems

The Accountability principle states that AI creators should be responsible for how their systems operate. They need to continuously monitor system performance and mitigate risks. Accountability in the AI industry is becoming a pressing issue as high-profile cases of algorithmic harm, bias, and abuse come to light. Critics increasingly argue that without accountability, AI creators hold too much power over opaque systems impacting lives.

Microsoft emphasizes accountability in AI development and deployment through its Responsible AI Standard, which considers accountability a foundational principle. According to Microsoft, AI systems must be accountable to people, and companies deploying AI systems must take responsibility for their operation.

Now let's do a knowledge check to review what we just learned.


# 1.4 Module Assessment

Choose the best response for each question.

## Check Your Knowledge

### 1. What is the primary goal of Responsible AI?

- [ ] To maximize profits from AI systems.
- [ ] To develop AI systems as quickly as possible.
- [x] **To ensure AI systems are safe, trustworthy, and ethical.**
- [ ] To replace human decision-making with AI.

**Answer: To ensure AI systems are safe, trustworthy, and ethical.**

*Explanation: Responsible AI is an approach to developing, assessing, and deploying artificial intelligent systems in a safe, trustworthy, and ethical way.*

### 2. Which principle is NOT one of the six identified by Microsoft for Responsible AI?

- [ ] Fairness.
- [x] **Innovation.**
- [ ] Inclusiveness.
- [ ] Accountability.

**Answer: Innovation.**

*Explanation: Microsoft's six principles of Responsible AI are: Fairness, Reliability and Safety, Privacy and Security, Inclusiveness, Transparency, and Accountability. Innovation is not one of these principles.*

### 3. What does the principle of Fairness in Responsible AI emphasize?

- [ ] Maximizing AI performance at all costs.
- [x] **Ensuring AI systems perform equally well across all demographic groups.**
- [ ] Prioritizing profitability over ethical concerns.
- [ ] Creating AI systems that are easy to understand.

**Answer: Ensuring AI systems perform equally well across all demographic groups.**

*Explanation: Fairness means AI systems should treat everyone fairly, avoiding differential impacts on similarly situated groups.*

### 4. How does Microsoft address potential biases in AI systems?

- [ ] By ignoring the issue and focusing on other areas.
- [ ] By providing AI systems with more data.
- [x] **By reviewing training data, testing with balanced samples, and using adversarial debiasing.**
- [ ] By allowing users to modify AI system outputs directly.

**Answer: By reviewing training data, testing with balanced samples, and using adversarial debiasing.**

*Explanation: Microsoft employs techniques to detect bias and mitigate unfair impacts including reviewing training data, testing models with balanced demographic samples, and using adversarial debiasing.*

### 5. What is the role of transparency in Microsoft's Responsible AI principles?

- [ ] To keep AI operations secret from the public.
- [x] **To make AI systems' operations and decisions understandable and clear.**
- [ ] To hide the limitations of AI systems.
- [ ] To prioritize efficiency over ethical considerations.

**Answer: To make AI systems' operations and decisions understandable and clear.**

*Explanation: The Transparency principle emphasizes that AI systems must be understandable and interpretable, with clear explanations of how they operate.*

### 6. Why is it important for developers to closely scrutinize AI-generated code?

- [ ] To reduce development time.
- [x] **To ensure that the code aligns with project-specific conventions and requirements.**
- [ ] To enhance the creative aspect of coding.
- [ ] To automatically improve system performance.

**Answer: To ensure that the code aligns with project-specific conventions and requirements.**

*Explanation: Developers need to carefully review AI-generated code to ensure it meets project requirements, follows coding standards, and doesn't introduce security vulnerabilities or other issues.*


# 1.5 Summary

As leaders and innovators in the AI space, Microsoft and GitHub are committed to ensuring that AI systems are developed and used in ways that are safe, trustworthy, and ethically sound.

Our approach is guided by six core principles: fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability.

Our goal is to ensure that AI systems prioritize people and uphold fundamental values like fairness, reliability, and transparency.

We also encourage other organizations to adopt these standards, and we hope that by providing resources like this module, we can help developers create effective, safe, and transparent AI solutions.

We are excited for you to embark on your own AI journey and urge you to approach it with responsibility.

## To Recap, in This Module, We Covered:

- Understand and apply the principles of Responsible AI usage
- Identify limitations and mitigate risks associated with AI
- Learn best practices for ensuring AI-generated code aligns with ethical standards and project-specific requirements
- Recognize the importance of transparency and accountability in AI systems to build trust and maintain user confidence

## For More Information on Responsible AI, Check Out These Resources:

- Microsoft Responsible AI Transparency Report
- Explore the Microsoft approach to AI
