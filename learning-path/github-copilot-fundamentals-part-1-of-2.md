

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


# 3.4 GitHub Copilot Data

In this unit, we'll cover how GitHub Copilot handles data for different environments, features and configurations.

## Data Handling for GitHub Copilot Code Suggestions

GitHub Copilot in the code editor does not retain any prompts like code or other context used for the purposes of providing suggestions to train the foundational models. It discards the prompts once a suggestion is returned.

GitHub Copilot Individual subscribers can opt-out of sharing their prompts with GitHub which will otherwise be used to finetune GitHub's foundational model.

## Data Handling for GitHub Copilot Chat

GitHub Copilot Chat operates as an interactive platform, allowing developers to engage in conversational interactions with the AI assistant to receive coding assistance. Here are the steps that it carries out which might be distinct from other features like code completion:

### Key Features:

**Formatting:** Copilot meticulously formats the generated response for optimal presentation within the chat interface. It highlights code snippets to improve readability and may include options for direct integration into your code. Copilot showcases the formatted response in the Copilot Chat window within the IDE, allowing you to easily review and interact with the provided information.

**User engagement:** You can actively engage with the response by asking follow-up questions, requesting clarifications, or providing additional input. The chat interface maintains a conversation history to facilitate contextual understanding in subsequent interactions.

**Data retention:** For Copilot Chat used outside the code editor, GitHub typically retains prompts, suggestions, and supporting context for 28 days. Specific retention policies for Copilot Chat within the code editor may vary.

The same goes for CLI, Mobile, and GitHub Copilot Chat on GitHub.com.

## Prompt Types Supported by GitHub Copilot Chat

GitHub Copilot Chat processes a wide range of coding-related prompts, demonstrating its versatility as a conversational coding assistant. Here are some common input types:

### Common Input Types:

**Direct Questions:** You can ask specific questions about coding concepts, libraries, or troubleshooting issues. For example, "How do I implement a quick sort algorithm in Python?" or "Why is my React component not rendering?"

**Code-Related Requests:** You can request code generation, modification, or explanation. Examples include "Write a function to calculate factorial," "Fix this error in my code," or "Explain this code snippet."

**Open-Ended Queries:** You can explore coding concepts or seek general guidance by asking open-ended questions like "What are the best practices for writing clean code?" or "How can I improve the performance of my Python application?"

**Contextual Prompts:** You can provide code snippets or describe specific coding scenarios to seek tailored assistance. For instance, "Here's a part of my code, can you suggest improvements?" or "I'm building a web application, can you help me with the authentication flow?"

Copilot Chat's ability to process diverse input types enhances its utility as a comprehensive coding companion.

## Limited Context Windows

*Illustration of GitHub Copilot context window.*

While GitHub Copilot Chat excels at understanding and responding to prompts, it's essential to acknowledge the limitation of context windows. This refers to the amount of surrounding code and text the model can process simultaneously to generate suggestions. GitHub Copilot's context window typically ranges from approximately 200-500 lines of code or up to a few thousand tokens. This limitation can vary depending on the specific implementation and version of Copilot being used.

Copilot Chat currently operates with a context window of 4k tokens, providing a broader scope for understanding and responding to user queries compared to the standard Copilot.

Despite these advancements, you should be mindful of context window limitations when crafting prompts. Breaking down complex problems into smaller, more focused queries or providing relevant code snippets can significantly enhance the model's ability to provide accurate and helpful responses.

# 3.5 GitHub Copilot Large Language Models (LLMs)

GitHub Copilot is powered by Large Language Models (LLMs) to assist you in writing code seamlessly. In this unit, we focus on understanding the integration and impact of LLMs in GitHub Copilot. Let's review the following topics:

- What are LLMs?
- The role of LLMs in GitHub Copilot and prompting
- Fine-tuning LLMs
- LoRA fine-tuning

## What are LLMs?

Large Language Models (LLMs) are artificial intelligence models designed and trained to understand, generate, and manipulate human language. These models are ingrained with the capability to handle a broad range of tasks involving text, thanks to the extensive amount of text data they're trained on. Here are some core aspects to understand about LLMs:

### Volume of Training Data
LLMs are exposed to vast amounts of text from diverse sources. This exposure equips them with a broad understanding of language, context, and intricacies involved in various forms of communication.

### Contextual Understanding
They excel in generating contextually relevant and coherent text. Their ability to understand context allows them to provide meaningful contributions, be it completing sentences, paragraphs, or even generating whole documents that are contextually apt.

### Machine Learning and AI Integration
LLMs are grounded in machine learning and artificial intelligence principles. They're neural networks with millions, or even billions, of parameters that are fine-tuned during the training process to understand and predict text effectively.

### Versatility
These models aren't limited to a specific type of text or language. They can be tailored and fine-tuned to perform specialized tasks, making them highly versatile and applicable across various domains and languages.

## Role of LLMs in GitHub Copilot and Prompting

GitHub Copilot utilizes LLMs to provide context-aware code suggestions. The LLM considers not just the current file but also other open files and tabs in the IDE to generate accurate and relevant code completions. This dynamic approach ensures tailored suggestions, improving your productivity.

## Fine-tuning LLMs

Fine-tuning is a critical process that allows us to tailor pretrained large language models (LLMs) for specific tasks or domains. It involves training the model on a smaller, task-specific dataset, known as the target dataset, while using the knowledge and parameters gained from a large pretrained dataset, referred to as the source model.

Fine-tuning is essential to adapt LLMs for specific tasks, enhancing their performance. However, GitHub took it a step further by using the LoRA fine tuning method, which we discuss next.

## LoRA Fine-tuning

Traditional full fine-tuning means to train all parts of a neural network, which can be slow and heavily reliant on resources. But LoRA (Low-Rank Adaptation) fine-tuning is a clever alternative. It's used to make large pretrained language models (LLMs) work better for specific tasks without redoing all the training.

### Here's how LoRA works:
- LoRA adds smaller trainable parts to each layer of the pretrained model, instead of changing everything
- The original model remains the same, which saves time and resources

### What's great about LoRA:
- It beats other adaptation methods like adapters and prefix-tuning
- It's like getting great results with fewer moving parts

In simple terms, LoRA fine-tuning is about working smarter, not harder, to make LLMs better for your specific coding requirements when using Copilot.

# 3.6 Module Assessment

## Check Your Knowledge

### 1. What's GitHub Copilot?

- [ ] A platform for code repositories.
- [ ] A model powered by machine learning.
- [x] **An assistant for coding, powered by OpenAI.**
- [ ] A service for web hosting.

**Answer: An assistant for coding, powered by OpenAI.**

*Explanation: GitHub Copilot is an AI-powered coding assistant developed by GitHub in collaboration with OpenAI that helps developers write code more efficiently.*

### 2. What role does prompting play in utilizing GitHub Copilot effectively?

- [ ] It generates instant bug fixes.
- [x] **It enhances the quality of code suggestions.**
- [ ] It automates the coding process entirely.
- [ ] It implements real-time collaboration.

**Answer: It enhances the quality of code suggestions.**

*Explanation: Prompt engineering is crucial for getting high-quality, relevant code suggestions from GitHub Copilot. Clear and well-crafted prompts lead to better code output.*

### 3. Which of the following rules is a principle of the 4S Method of prompt engineering?

- [ ] Summarize code objectives concisely.
- [x] **Specify instructions explicitly and in detail.**
- [ ] Streamline processes for efficient code suggestions.
- [ ] Simplify coding languages for universal understanding.

**Answer: Specify instructions explicitly and in detail.**

*Explanation: The 4S Method includes: Single (focused task), Specific (explicit and detailed), Short (concise), and Surround (provide context). "Specific" means ensuring instructions are explicit and detailed.*

### 4. How does GitHub Copilot handle personal data?

- [ ] It saves all personal data for future references.
- [ ] It shares personal data with other users for collaborative projects.
- [ ] It encrypts personal data.
- [x] **It actively filters out personal data to protect user privacy.**

**Answer: It actively filters out personal data to protect user privacy.**

*Explanation: GitHub Copilot includes toxicity filtering mechanisms that actively filter out personal data such as names, addresses, or identification numbers to protect user privacy and data security.*

### 5. What is LoRA in the context of fine-tuning Large Language Models (LLMs)?

- [x] **A method that adds trainable elements to each layer of the pretrained model without a complete overhaul.**
- [ ] A technology optimizing communication between different coding languages.
- [ ] A specialized software library enhancing Copilot's performance.
- [ ] A new programming paradigm supported exclusively by Copilot.

**Answer: A method that adds trainable elements to each layer of the pretrained model without a complete overhaul.**

*Explanation: LoRA (Low-Rank Adaptation) fine-tuning adds smaller trainable parts to each layer of the pretrained model instead of changing everything, which saves time and resources.*

### 6. How does Copilot use the context to provide code suggestions?

- [ ] It considers only the prompt text you provide.
- [ ] It considers the file type but not the content of the file.
- [x] **It considers the surrounding code, file type, and content of parallel open tabs in the code editor.**
- [ ] It randomly selects context from the internet.

**Answer: It considers the surrounding code, file type, and content of parallel open tabs in the code editor.**

*Explanation: GitHub Copilot gathers comprehensive context including code before and after the cursor, filename and file type, information about adjacent open tabs, and project structure to provide relevant suggestions.*

### 7. Which of these strategies helps to improve prompt effectiveness in GitHub Copilot?

- [x] **Providing detailed contextual information with clarity.**
- [ ] Making the prompt as general as possible.
- [ ] Keeping the prompt lengthy and detailed.
- [ ] Avoiding examples in the prompt to not restrict Copilot's creativity.

**Answer: Providing detailed contextual information with clarity.**

*Explanation: Following the 4S principles (Single, Specific, Short, Surround), providing clear contextual information while maintaining specificity and conciseness leads to better code suggestions from Copilot.*

# 3.7 Summary

In this module, we unveiled the intricacies of optimizing GitHub Copilot through effective prompting. Harnessing the tool's maximum potential lies in the art and science of prompt engineering. Now, you're equipped with refined skills and insights to elevate your coding experience and output.

## With the completion of this module, you have learned:

- Prompt engineering principles, best practices, and how GitHub Copilot learns from your prompts to provide context-aware responses
- The underlying flow of how GitHub Copilot processes user prompts to generate responses or code suggestions
- The data flow for code suggestions and chat in GitHub Copilot
- LLMs (Large Language Models) and their role in GitHub Copilot and prompting
- How to craft effective prompts that optimize GitHub Copilot's performance, ensuring precision and relevance in every code suggestion
- The intricate relationship between prompts and Copilot's responses
- How Copilot handles data from prompts in different situations, including secure transmission and content filtering

## References

- Inside GitHub: Working with the Large Language Models (LLMs) behind GitHub Copilot - The GitHub Blog
- How to use GitHub Copilot: Prompts, tips, and use cases - The GitHub Blog
- How GitHub copilot handles data


# 4 Using advanced GitHub Copilot features

Use advanced GitHub Copilot features with a Python application.


# 4.1 Introduction

GitHub Copilot is an AI coding partner that provides autocomplete suggestions while you code. Get suggestions by typing code or interactively using natural language.

Copilot analyses your file and related files, offering suggestions in your text editor. It uses context from written code and comments, and then suggests new lines or entire functions.

GitHub Codespaces is a hosted developer environment operating in the cloud that can be run with Visual Studio Code. You can customize the development experience for any development project on GitHub, preinstalling dependencies, libraries, and even Visual Studio Code extensions and settings.

## Scenario: Working with an Existing Project

As a developer, you want to be more productive typing code faster both for net new projects and existing ones. For this task, you want to use advanced features from an AI assistant that helps improve your developer workflows in code writing, documentation, testing, and more.

In this module, you understand how you can use advanced features of GitHub Copilot with applied examples modifying a repository using different techniques to add new HTTP API (Application Programming Interface) endpoints, write unit tests, and document existing code.

## What will I learn?

By the conclusion of this module, you acquire the skills to:

- Work with a preconfigured GitHub repository in Codespaces with the GitHub Copilot extension
- Use interactive features of GitHub Copilot to generate useful suggestions for an existing project
- Apply advanced GitHub Copilot features to learn more about a new project, write documentation, and create unit tests

## What is the main objective?

After successfully finishing this module, you'll be capable of using interactive prompts and other advanced GitHub Copilot features to enhance a software project.

## Prerequisites

- Basic understanding of Python and text editors
- Basic comprehension of Git and GitHub Fundamentals and running basic `git` commands like `git add` and `git push`
- A GitHub Account with an active subscription for GitHub Copilot is required for either your personal GitHub account or a GitHub account managed by an organization or enterprise. For learning purposes, the Copilot Free option with usage limits should be sufficient


# 4.2  Advanced GitHub Copilot Features

Often, when you work with code, you need to review the project's documentation in addition to libraries and framework documentation. In order to write code or documentation, you must have a good understanding of the codebase. Tasks like fixing bugs and writing tests can be time intensive, but at the same time necessary for most projects. Fortunately, GitHub Copilot has several advanced features that can make these tasks easier and more efficient.

## The Basics

When GitHub Copilot is enabled, it provides you with suggestions. These suggestions are called ghost text. You can either ignore the ghost text, or accept it by pressing the **Tab** key. The suggestions don't require a prompt because by default GitHub Copilot uses the files you have open as context. However, you can provide a prompt using a comment, the chat window, or the inline chat within your code.

## Chatting with GitHub Copilot

GitHub Copilot allows you to have an interactive discussion using the chat feature. In Visual Studio Code, you can click the chat icon on the left sidebar, which opens the chat interface in a dedicated pane.

In this pane, you can ask questions about the code you're currently working on or other software-related questions.

## Using Inline Chat

Besides the dedicated chat pane, you can use the inline chat. It allows you to interact with GitHub Copilot without leaving your code.

Access the inline chat by using **Ctrl+i** on Windows or **Command+i** on a Mac. One of the benefits of using the inline chat is that you don't have to switch context by going to a different pane. The suggestions and interactions happen closer to the code.

## Slash Commands

Within the chat pane or when using the inline chat, you can use slash commands. These commands allow GitHub Copilot to use a specific intent for quickly solving common development tasks.

If you type a forward slash in the chat pane or inline chat, you should see a drop-down menu with all the slash commands available. For example, the `/tests` slash command helps you write tests, while the `/docs` command is intended for writing documentation.

Using specific slash commands to create a question is a good way to get better responses without having to write longer prompts.

## Agents

Visual Studio Code has a feature called *agents* that allows you to interact with GitHub Copilot. These agents allow you to ask questions using a specific context. For example the `@terminal` agent helps you chat with GitHub Copilot to interact with the terminal.

Another agent is `@workspace`, which is aware of your entire workspace. It allows you to ask questions about the entire project. To use an agent, prefix your question with the agent, for example: `@workspace how can I package this project?`.


# 4.3 Exercise - Set up GitHub Copilot to Work with Visual Studio Code

In this exercise, we create a new repository using the GitHub template for a web API that uses the Python programming language.

## Environment Setup

First you need to launch the Codespaces environment, which comes preconfigured with the GitHub Copilot extension.

1. Open the Codespace with the preconfigured environment in your browser.

2. On the **Create codespace** page, review the Codespace configuration settings, and then select **Create new codespace**.

3. Wait for the Codespace to start. This startup process can take a few minutes.

4. The remaining exercises in this project take place in the context of this development container.

> **Important**
> 
> All GitHub accounts can use Codespaces for up to 60 hours free each month with two core instances. For more information, see **GitHub Codespaces monthly included storage and core hours**.

> **Tip**
> 
> GitHub Copilot offers a free tier with **2,000 code autocompletes and 50 chat messages per month**. To get started, open Visual Studio Code, click on the GitHub Copilot icon, and then click "Sign in to Use GitHub Copilot for Free". **Learn more**. Educators, Students and, select open-source maintainers can receive Copilot Pro for free, learn how at: **https://aka.ms/Copilot4Students**.

## Python Web API

When complete, Codespaces loads with a terminal section at the bottom. Codespaces installs all the required extensions in your container. Once the package installs are complete, Codespaces executes the `uvicorn` command to start your web application running within your Codespace.

When the web application starts successfully, a message in the terminal **Ports** tab shows that the server is running on port 8000 within your Codespace.

## Sign up for GitHub Copilot

If you haven't already, you need to register by setting up a free trial or subscription for your account.

> **Note**
> 
> Educators, Students and select open-source maintainers can sign up for Copilot for free, learn how at **Setting up GitHub Student and GitHub Copilot as an Authenticated Student Developer**.

# 4.4 Applied GitHub Copilot Techniques

In previous units, we showed how to set up Copilot and mentioned how it can make you faster as a developer starting to write code.

In this unit, let's discuss how Copilot can help you with existing projects and help you with more complicated tasks.

## Advanced Tasks with GitHub Copilot

It's common to work with an existing project as an engineer. When fixing code or implementing features, we need to write documentation and tests and work with terminal commands. Let's go through some ways you can accomplish this using GitHub Copilot.

## Implicit Prompts

Although you can be specific in prompts for getting GitHub Copilot guidance, you can take advantage of features that implicitly provide a precrafted prompt to get a good answer.

For example, if you're working on a Python project, and you have a file open with the following code that has a bug in it:

```python
with open("file.txt", "r") as file:
    # Read the file and print the content
    contents = file.read
```

After selecting the code and using **Ctrl+i** on Windows or **Command+i** on a Mac, you can ask GitHub Copilot to help you fix the code using the inline chat and the `/fix` slash command.

If you only type `/fix`, you might get a response from GitHub Copilot similar to this suggestion: "To fix the code, I would add parentheses after file.read to call the read method and fix the typo in the method name."

### Available Slash Commands

Slash commands can be used to both in the inline chat and the chat interface. In addition to the `/fix` command, here are some of the most useful slash commands you can use in Copilot chat:

- `/doc`: Adds comments to the specified or selected code
- `/explain`: Gets explanations about the code
- `/generate`: Generates code to answer the specified question
- `/help`: Gets help on how to use Copilot chat
- `/optimize`: Analyzes and improves the runtime of the selected code
- `/tests`: Creates unit tests for the selected code

Using slash commands allows for easier interaction with GitHub Copilot and helps you get better responses without having to write longer prompts.

Combining features like slash commands with inline chat allows you to choose the way that works best for you and the code you're working on.

## Selective Context

GitHub Copilot can be customized to provide suggestions based on the context you're working on. For example, you can ask GitHub Copilot to provide suggestions based on the entire workspace or the terminal output.

GitHub Copilot can give you an accurate suggestion for your project without requiring you to open many files. Imagine you need to package your project using a Dockerfile. A Dockerfile is a special file that needs to have specific instructions to package your project. You can use the `@workspace` agent to ask GitHub Copilot how to help you out. For example, open GitHub Copilot Chat and type the following command:

```text
@workspace I need to create a Dockerfile for this project, can you generate one that will help me package it?
```

You'll get a response back that explains the steps to create a Dockerfile for your project, along with some explanation on what the steps of the file are going to do.

As always, if the suggestions aren't exactly what you are looking for, you can reword the prompt and be more specific. For example, you could ask GitHub Copilot to use a specific step when creating the Dockerfile:

```text
@workspace help me create a Dockerfile to package this project but make sure you are using a Virtual Environment for Python.
```

### Available Agents

In addition to the `@workspace` agent, you can use other agents like `@terminal`, `@file`, and `@directory` to get context-specific suggestions:

- **@terminal**: Provides suggestions based on the terminal output.
  - Example: `@terminal How do I fix the error message I'm seeing?`

- **@file**: Focuses on the content of a specific file.
  - Example: `@file Can you help me refactor this function in main.py?`

- **@directory**: Considers the contents of a specific directory.
  - Example: `@directory How can I optimize the scripts in the utils directory?`

If you're stuck or not getting the results you want, then you can reword the prompt or start writing code for Copilot to autocomplete.

> **Note**
> 
> Although you can be specific with @workspace, by default GitHub Copilot uses open files in your text editor as additional context.

# 4.5 Exercise - Update a Web API with GitHub Copilot

Let's explore how you can modify a Python repository using advanced GitHub Copilot techniques for an API endpoint. Gain more practical experience by using this repository that contains a Python Web Application that hosts a Travel Weather API.

## What is an API?

An API acts as the intermediary that allows different applications to communicate to each other. For example, a weather website can either share historical data or provide forecast functionality through its API. Using the API, you can embed the data into your website, or create an application sharing weather data with other features.

## Extend the Web API

The current API isn't exposing country/region, which needs to be implemented to list cities. The route should allow only GET HTTP requests with a JSON response providing information from the historical high and low for that country/region, city, and given month.

> **Note**
> 
> For this exercise, use the **Codespace with the preconfigured environment** in your browser.

## Step 1: Add a new route

Open the main.py file, and use the inline chat with the command **Ctrl+i** (on Windows) or **Command+i** (on Mac). This command asks GitHub Copilot to help you create a new API that shows you the cities of a country/region. Use the following prompt:

```text
Create a new route that exposes the cities of a country/region.
```

This prompt should give you something similar like this:

```python
# Create a new route that exposes the cities of a country:
@app.get('/countries/{country}')
def cities(country: str):
    return list(data[country].keys())
```

> **Note**
> 
> Try your new route and refine your prompt until the result is as desired.

## Step 2: Create a test

Now that you created a new route, create a test with Copilot Chat for this route that uses Spain as the country/region. Remember to select your code, and ask Copilot Chat to help you with this specific API that we just created. You can use the inline-chat or the dedicated chat pane with the following prompt:

```text
/tests help me to create a new test for this route that uses Spain as the country/region.
```

Once Copilot helps you create your test, try it. If this isn't functioning as expected, feel free to share those details with Copilot in the chat. For example:

```text
This test is not quite right, it is not including cities that doesn't exist. Only Seville is part of the API.
```

## Step 3: Use an agent to write the documentation

Finally, use the `@workspace` agent to write project documentation and details on how to run the project itself. Open the `README.md` file and use the following prompt in GitHub Copilot Chat:

```text
@workspace I want to document how to run this project so that other developers can get started quickly by reading the README.md file.
```

You should get a response that helps you update the README.md file with the necessary information to run the project.

## Conclusion

Congratulations on completing this exercise. You used GitHub Copilot to generate a new API route, and then wrote a test to verify its correctness. Finally, you added documentation using an agent that will help developers understand how to run this project.

When you've finished the exercise in GitHub, return here for:

- A quick knowledge check
- A summary of what you've learned
- A badge for completing this module


# 4.6 Module Assessment

## 1. What is ghost text in GitHub Copilot?

- [x] **Ghost text in GitHub Copilot are suggestions that appear in your text editor as you type.**
- [ ] Ghost text in GitHub Copilot are options used when typing to provide suggestions.
- [ ] Ghost text in GitHub Copilot involves using prompts and natural language questions within your code or documentation.

**Answer: Ghost text in GitHub Copilot are suggestions that appear in your text editor as you type.**

*Explanation: Ghost text refers to the suggestions that GitHub Copilot provides automatically as you type code, appearing as grayed-out text that you can accept by pressing Tab or ignore.*

## 2. How do you access GitHub Copilot's inline chat?

- [ ] Access the inline chat by clicking on the chat icon in the left sidebar of Visual Studio Code.
- [x] **Use Ctrl+i on Windows or Command+i on a Mac to open the inline chat.**
- [ ] Access the inline chat by using Alt+i on Windows or Option+i on a Mac.

**Answer: Use Ctrl+i on Windows or Command+i on a Mac to open the inline chat.**

*Explanation: The inline chat feature is accessed using Ctrl+i on Windows or Command+i on Mac, allowing you to interact with GitHub Copilot without leaving your current code context.*

## 3. What are slash commands used for in GitHub Copilot?

- [ ] Slash commands are used to format your codebase according to best practices.
- [ ] Slash commands are used to debug code and detect security vulnerabilities within your projects.
- [x] **Slash commands are shortcuts to quickly solve common development tasks within the chat or inline pane.**

**Answer: Slash commands are shortcuts to quickly solve common development tasks within the chat or inline pane.**

*Explanation: Slash commands like /fix, /doc, /tests, and /explain provide quick shortcuts for common development tasks, allowing for easier interaction with GitHub Copilot without writing longer prompts.*

## 4. What are the benefits of using agents like '@terminal' or '@workspace' when interacting with GitHub Copilot?

- [x] **Agents in Visual Studio Code help you ask questions within a specific context, allowing for more precise and relevant answers from GitHub Copilot.**
- [ ] Agents help enforce a consistent code format based on best practices within Visual Studio Code for improved readability.
- [ ] Agents provide extra security features for detecting vulnerabilities and intrusions within Visual Studio Code projects.

**Answer: Agents in Visual Studio Code help you ask questions within a specific context, allowing for more precise and relevant answers from GitHub Copilot.**

*Explanation: Agents like @workspace, @terminal, @file, and @directory provide specific context to GitHub Copilot, enabling more targeted and relevant responses based on the particular scope or environment you're working with.*

## 5. What are the benefits of using implicit prompts with slash commands in inline chat for fixing code issues with GitHub Copilot?

- [ ] Implicit prompts help enforce a consistent naming convention and syntax based on best practices within Visual Studio Code projects for improved readability.
- [x] **Implicit prompts help get better responses from GitHub Copilot without writing longer prompts, making it easier to interact and fix code issues.**
- [ ] Implicit prompts help detect security vulnerabilities and potential malicious activities within Visual Studio Code projects for increased safety.

**Answer: Implicit prompts help get better responses from GitHub Copilot without writing longer prompts, making it easier to interact and fix code issues.**

*Explanation: Implicit prompts combined with slash commands provide precrafted, focused interactions that yield better responses from GitHub Copilot without requiring lengthy, detailed prompts, making the development process more efficient.*



# 4.7 Summary

GitHub Copilot is a tool that offers many ways to interact with your project, and it helps you become a more efficient developer. Adding tests, fixing bugs, or generating automation allows you to improve the development lifecycle for your projects.

## Learning Outcomes

Now that you have finished this module, you should be able to:

- Use GitHub Copilot features like chat, agents, inline chat, and slash commands, which offer more flexibility to accomplish coding tasks
- Apply the `@workspace` agent using GitHub Copilot Chat to provide more content when trying to get output relevant to your project

## Delete Your Codespaces Resources

To avoid consuming all your monthly GitHub Codespaces time, it's important to delete all your resources after you upload your changes to your repository. Follow these steps to remove your resources:

1. Go to Codespaces on GitHub here.
2. Find your Codespace instance from the list, and select the three dots menu to display your options.
3. Select **Delete** to remove your Codespace instance.

> **Note**
> 
> If you don't commit your changes to your repository, you'll lose all your work. Therefore, it's important to commit and push your changes before deleting your Codespace instance.

## References

- What is GitHub Copilot?
- Introduction to GitHub Copilot
- Code with GitHub Codespaces

