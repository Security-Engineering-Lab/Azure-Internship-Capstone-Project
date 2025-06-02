

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

# 3 Introduction to prompt engineering with GitHub Copilot

Discover the essentials of creating effective prompts with GitHub Copilot. Uncover techniques to transform your coding comments into precise, actionable code, enhancing your development workflow.


# 3.1 Introduction

GitHub Copilot, powered by OpenAI, is changing the game in software development. GitHub Copilot can grasp the intricate details of your project through its training of data containing both natural language and billions of lines of source code from publicly available sources, including code in public GitHub repositories. This allows GitHub Copilot to provide you with more context-aware suggestions.

But to get the most out of GitHub Copilot, you need to know about prompt engineering. Prompt engineering is how you tell GitHub Copilot what you need. The quality of the code it gives back depends on how clear and accurate your prompts are.

## In This Module, You'll Learn About:

- Prompt engineering principles, best practices, and how GitHub Copilot learns from your prompts to provide context-aware responses
- The underlying flow of how GitHub Copilot processes user prompts to generate responses or code suggestions
- The data flow for code suggestions and chat in GitHub Copilot
- LLMs (Large Language Models) and their role in GitHub Copilot and prompting
- How to craft effective prompts that optimize GitHub Copilot's performance, ensuring precision and relevance in every code suggestion
- The intricate relationship between prompts and Copilot's responses
- How Copilot handles data from prompts in different situations, including secure transmission and content filtering


# 3.2 Prompt Engineering Foundations and Best Practices

In this unit, we'll cover:

- What is prompt engineering?
- Foundations of prompt engineering
- Best practices in prompt engineering
- How Copilot learns from your prompts

## What is prompt engineering?

Prompt engineering is the process of crafting clear instructions to guide AI systems, like GitHub Copilot, to generate context-appropriate code tailored to your project's specific needs. This ensures the code is syntactically, functionally, and contextually correct.

Now that you know what prompt engineering is, let's learn about some of its principles.

## Principles of prompt engineering

Before we explore specific strategies, let's first understand the basic principles of prompt engineering, summed up in the 4 Ss below. These core rules are the basis for creating effective prompts.

### The 4 Ss

**Single:** Always focus your prompt on a single, well-defined task or question. This clarity is crucial for eliciting accurate and useful responses from Copilot.

**Specific:** Ensure that your instructions are explicit and detailed. Specificity leads to more applicable and precise code suggestions.

**Short:** While being specific, keep prompts concise and to the point. This balance ensures clarity without overloading Copilot or complicating the interaction.

**Surround:** Utilize descriptive filenames and keep related files open. This provides Copilot with rich context, leading to more tailored code suggestions.

These core principles lay the foundation for crafting efficient and effective prompts. Keeping the 4 Ss in mind, let's dive deeper into advanced best practices that ensure each interaction with GitHub Copilot is optimized.

## Best practices in prompt engineering

The following advanced practices, based on the 4 Ss, refine and enhance your engagement with Copilot, ensuring that the generated code isn't only accurate but perfectly aligned with your project's specific needs and contexts.

### Provide enough clarity

Building on the 'Single' and 'Specific' principles, always aim for explicitness in your prompts. For instance, a prompt like "Write a Python function to filter and return even numbers from a given list" is both single-focused and specific.

*Screenshot of a Copilot chat with a Python prompt.*

### Provide enough context with details

Enrich Copilot's understanding with context, following the 'Surround' principle. The more contextual information provided, the more fitting the generated code suggestions are. For example, by adding some comments at the top of your code to give more details to what you want, you can give more context to Copilot to understand your prompt, and provide better code suggestions.

*Screenshot of comments added to code for better Copilot suggestions.*

In the example above, we used steps to give more detail while keeping it short. This practice follows the 'Short' principle, balancing detail with conciseness to ensure clarity and precision in communication.

> **Note**
> 
> Copilot also uses parallel open tabs in your code editor to get more context on the requirements of your code.

### Provide examples for learning

Using examples can clarify your requirements and expectations, illustrating abstract concepts and making the prompts more tangible for Copilot.

*Screenshot of an example used to clarify prompts for Copilot.*

### Assert and iterate

One of the keys to unlocking GitHub Copilot's full potential is the practice of iteration. Your first prompt might not always yield the perfect code, and that's perfectly okay. If the first output isn't quite what you're looking for, treat it as a step in a dialogue. Erase the suggested code, enrich your initial comment with added details and examples, and prompt Copilot again.

Now that you learned best practices to improve your prompting skills, let's take a closer look at how you can provide examples Copilot can learn from.

## How Copilot learns from your prompts

GitHub Copilot operates based on AI models trained on vast amounts of data. To enhance its understanding of specific code contexts, engineers often provide it with examples. This practice, commonly found in machine learning, led to different training approaches such as:

### Zero-shot learning

Here, GitHub Copilot generates code without any specific examples, relying solely on its foundational training. For instance, suppose you want to create a function to convert temperatures between Celsius and Fahrenheit. You can start by only writing a comment describing what you want, and Copilot might be able to generate the code for you, based on its previous training, without any other examples.

*Screenshot of Copilot creating a temperature conversion code from a comment.*

### One-shot learning

With this approach, a single example is given, aiding the model in generating a more context-aware response. Building upon the previous zero-shot example, you might provide an example of a temperature conversion function and then ask Copilot to create another similar function. Here's how it could look:

*Screenshot of Copilot using an example to create similar temperature conversion code.*

### Few-shot learning

In this method, Copilot is presented with several examples, which strike a balance between zero-shot unpredictability and the precision of fine-tuning. Let's say you want to generate code that sends you a greeting depending on the time of the day. Here's a few-shot version of that prompt:

*Screenshot of Copilot generating greeting code based on multiple examples.*

Now that you know how Copilot uses your prompts to learn, let's take an in-depth look at how it actually uses your prompt to suggest code for you.



# 3.3 GitHub Copilot User Prompt Process Flow

In this unit, we'll break down how GitHub Copilot turns your prompts into smart, usable code. Generally, GitHub Copilot receives prompts and returns code suggestions or responses in its data flow. This process suggests an inbound and outbound flow.

## Inbound Flow:

*Illustration of GitHub Copilot inbound flow.*

Let's walk through all the steps Copilot takes to process a user's prompt into a code suggestion.

### 1. Secure prompt transmission and context gathering

The process begins with the secure transmission of the user prompt over HTTPS. This ensures that your natural language comment is sent to GitHub Copilot's servers securely and confidentially, protecting sensitive information.

GitHub Copilot securely receives the user prompt, which could be a Copilot chat or a natural language comment provided by you within your code.

Simultaneously, Copilot collects context details:

- Code before and after the cursor position, which helps it understand the immediate context of the prompt
- Filename and type of the file being edited, allowing it to tailor code suggestions to the specific file type
- Information about adjacent open tabs, ensuring that the generated code aligns with other code segments in the same project
- Information on project structure and file paths
- Information on programming languages and frameworks
- Pre-processing using Fill-in-the-Middle (FIM) technique to consider both the preceding and following code context, effectively expanding the model's understanding allowing Copilot to generate more accurate and relevant code suggestions by leveraging a broader context

These steps translate the user's high-level request into a concrete coding task.

### 2. Proxy filter

Once the context is gathered and the prompt is built, it passes securely to a proxy server hosted in a GitHub-owned Microsoft Azure tenant. The proxy filters traffic, blocking attempts to hack the prompt or manipulate the system into revealing details about how the model generates code suggestions.

### 3. Toxicity filtering

Copilot incorporates content filtering mechanisms before proceeding with intent extraction and code generation, to ensure that the generated code and responses don't include or promote:

- **Hate speech and inappropriate content:** Copilot employs algorithms to detect and prevent the intake of hate speech, offensive language, or inappropriate content that could be harmful or offensive.
- **Personal data:** Copilot actively filters out any personal data, such as names, addresses, or identification numbers, to protect user privacy and data security.

### 4. Code generation with LLM

Finally, the filtered and analyzed prompt is passed to LLM Models, which generate appropriate code suggestions. These suggestions are based on Copilot's understanding of the prompt and the surrounding context, ensuring that the generated code is relevant, functional, and aligned with project-specific requirements.

## Outbound Flow:

*Illustration of GitHub Copilot outbound flow.*

### 5. Post-processing and response validation

Once the model produces its responses, the toxicity filter removes any harmful or offensive generated content. The proxy server then applies a final layer of checks to ensure code quality, security, and ethical standards. These checks include:

- **Code quality:** Responses are checked for common bugs or vulnerabilities, such as cross-site scripting (XSS) or SQL injection, ensuring that the generated code is robust and secure.
- **Matching public code (optional):** Optionally, administrators can enable a filter that prevents Copilot from returning suggestions over ~150 characters if they closely resemble existing public code on GitHub. This prevents coincidental matches from being suggested as original content. If any part of the response fails these checks, it is either truncated or discarded.

### 6. Suggestion delivery and feedback loop initiation

Only responses that pass all filters are delivered to the user. Copilot then initiates a feedback loop based on your actions to achieve the following:

- Grow its knowledge from accepted suggestions
- Learn and improve through modifications and rejections of its suggestions

### 7. Repeat for subsequent prompts

The process is repeated as you provide more prompts, with Copilot continuously handling user requests, understanding their intent, and generating code in response. Over time, Copilot applies the cumulative feedback and interaction data, including context details, to improve its understanding of user intent and refine its code generation capabilities.
