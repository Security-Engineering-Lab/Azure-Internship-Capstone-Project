

# Introduction to GitHub Copilot
https://learn.microsoft.com/en-us/training/modules/introduction-to-github-copilot/

# GitHub Copilot

GitHub Copilot uses OpenAI Codex to suggest code and entire functions in real time, right from your editor.

## Learning Objectives

In this module, you will:

- Learn how GitHub Copilot can help you code by offering autocomplete-style suggestions
- Learn about the various ways to trigger GitHub Copilot
- Learn about the differences among GitHub Copilot Individual, Business, and Enterprise
- Learn how to configure GitHub Copilot
- Troubleshoot GitHub Copilot

## Prerequisites

- GitHub account
- Basic understanding of GitHub fundamentals

# 1.1 Introduction

GitHub Copilot is the world's first at-scale AI developer tool that can help you write code faster with less work. GitHub Copilot draws context from comments and code to suggest individual lines and whole functions instantly.

Research finds that when GitHub Copilot helps developers code faster, they can focus on solving bigger problems, stay in the flow longer, and feel more fulfilled with their work.

OpenAI created the generative pretrained language model in GitHub Copilot, powered by OpenAI Codex. An extension is available for Visual Studio Code (VS Code), Visual Studio, Neovim, and the JetBrains suite of integrated development environments (IDEs).

## Learning Objectives

By the end of this module, you'll:

- Understand how GitHub Copilot can help you code by offering autocomplete-style suggestions
- Understand the various ways to trigger GitHub Copilot
- Comprehend the differences among GitHub Copilot Free, Pro, Business, and Enterprise
- Know how to configure GitHub Copilot
- Know how to troubleshoot GitHub Copilot

## Prerequisites

- GitHub account
- Basic understanding of GitHub fundamentals



# 1.2  GitHub Copilot, Your AI Pair Programmer


*The logo icon for GitHub Copilot that shows the Copilot icon in the middle with a blue and green swirl around the logo.*

It's no secret that AI is disrupting the technology landscape. AI is profoundly changing the way the world works and how each organization and team operates. These advancements in AI serve as a catalyst and can dramatically improve the productivity of developers around the world as they use and apply it well.

The addition of AI features to the developer tools that you use and love helps you collaborate, develop, test, and ship your products faster and more efficiently than ever before. GitHub Copilot is a service that provides you with an AI pair programmer that works with all of the popular programming languages.

## Research Findings

In recent research, GitHub and Microsoft found that developers experience a significant productivity boost when they use GitHub Copilot to work on real-world projects and tasks. In fact, in the three years since its launch, developers have experienced the following benefits while using GitHub Copilot:

- **46% of new code now written by AI**
- **55% faster overall developer productivity**
- **74% of developers feeling more focused on satisfying work**

Microsoft developed GitHub Copilot in collaboration with OpenAI. GitHub Copilot is powered by the OpenAI Codex system. OpenAI Codex has broad knowledge of how people use code and is more capable than GPT-3 in code generation. OpenAI Codex is more capable, in part, because it was trained on a dataset that included a larger concentration of public source code.

GitHub Copilot is available as an extension for VS Code, Visual Studio, Vim/Neovim, and the JetBrains suite of IDEs.

## GitHub Copilot Features

GitHub Copilot started a new age of software development as an AI pair programmer that keeps developers in the flow by autocompleting comments and code. But AI-powered autocompletion was just the starting point.

Here are some features of GitHub Copilot that truly make it a developer tool of the future. With these features, GitHub Copilot is more than just an editor. It's becoming a readily accessible AI assistant throughout the entire development life cycle.

### Copilot for Chat

GitHub Copilot brings a ChatGPT-like chat interface to the editor. The chat interface focuses on developer scenarios and natively integrates with VS Code and Visual Studio. It's deeply embedded in the IDE, and it recognizes what code a developer has typed and what error messages appear. A developer can get in-depth analysis and explanations of what code blocks are intended to do, generate unit tests, and even get proposed fixes to bugs.

### Copilot for Pull Requests

OpenAI's GPT-4 model adds support in GitHub Copilot for AI-powered tags in pull-request descriptions through a GitHub app that organization admins and individual repository owners can install. GitHub Copilot automatically fills out these tags based on the changed code. Developers can then review or modify the suggested descriptions.

### Copilot for the CLI

Next to the editor and pull requests, the terminal is the place where developers spend the most time. However, even the most proficient developers need to scroll through many pages to remember the precise syntax of many commands. The GitHub Copilot command-line interface (CLI) can compose commands and loops, and it can and throw obscure find flags to satisfy your query.

## Subscription Plans

The service is available through GitHub personal accounts with GitHub Copilot Free and GitHub Copilot Pro, through organization accounts with GitHub Copilot Business, or through enterprise accounts with GitHub Copilot Enterprise.

### GitHub Copilot Free

GitHub Copilot Free allows individual developers to use GitHub Copilot at no cost. To get started, open Visual Studio Code, click on the GitHub Copilot icon, and then click "Sign in to Use GitHub Copilot for Free". Log in to your GitHub account in the window that will open in the browser.

The GitHub Copilot Free tier includes 2000 code completions per month, 50 chat requests per month, and access to both GPT-4o and Claude 3.5 Sonnet models. Learn more.

### GitHub Copilot Business

GitHub Copilot Business allows you to control who can use GitHub Copilot in your company. After you give access to an organization, its admins can give access to individuals and teams.

With GitHub Copilot Business, GitHub Copilot is open to every developer, team, organization, and enterprise.

With the following features, GitHub Copilot Business is focused on making organizations more productive, secure, and fulfilled:

- Code completions
- Chat in IDE and mobile
- Filter for security vulnerabilities
- Code referencing
- Filter for public code
- IP indemnity
- Enterprise-grade security, safety, and privacy

### GitHub Copilot Enterprise

GitHub Copilot Enterprise is available for organizations through GitHub Enterprise Cloud. This subscription plan enables your teams of developers to:

- Quickly get up to speed on your codebase
- Search through and build documentation
- Get suggestions based on internal and private code
- Quickly review pull requests

GitHub Copilot Enterprise includes everything in GitHub Copilot Business, plus a layer of personalization for organizations. It provides integration into GitHub as a chat interface, so developers can converse about their codebase. It also provides action buttons throughout the platform.

GitHub Copilot Enterprise can index an organization's codebase for a deeper understanding and for suggestions that are more tailored. It offers access to GitHub Copilot customization to fine-tune private models for code completion.

In the next unit, you'll learn about how to get started with GitHub Copilot and some common configurations.


# 1.3 Interact with Copilot

This unit explores ways that you can maximize your interaction with GitHub Copilot in your development environment. By understanding the service's features and capabilities, you learn how to use it effectively.

The following sections describe the various ways to trigger and use GitHub Copilot, along with examples and shortcuts to help you get the most out of it.

## Inline Suggestions

Inline suggestions are the most immediate form of assistance in Copilot. As you type, Copilot analyzes your code and context to offer real-time code completions. This feature predicts what you might want to write next and displays suggestions in a subtle, unobtrusive way.

The suggestions that Copilot offers appear as grayed-out text ahead of your cursor.

- **To accept a suggestion**, select the Tab key or the > (right arrow) key
- **To reject a suggestion**, keep typing or select the Esc key

Inline suggestions are especially useful when you're working on repetitive tasks or you need quick boilerplate code.

Here's an example:

```python
def calculate_average(numbers):
    # Start typing here and watch Copilot suggest the function body
```

## Command Palette

The command palette provides quick access to the various functions in Copilot, so you can perform complex tasks with only a few keystrokes.

- Open the command palette in Visual Studio Code by selecting **Ctrl+Shift+P** (Windows or Linux) or **Cmd+Shift+P** (Mac)
- Enter **Copilot** to see available commands
- Select actions like **Explain This** or **Generate Unit Tests** to get assistance

## Copilot Chat

Copilot chat is an interactive feature that enables you to communicate with Copilot by using natural language. You can ask questions or request code snippets, and Copilot provides responses based on your input.

- Open the Copilot chat panel in your IDE
- Enter questions or requests in natural language, and then evaluate the Copilot response

For example, you might enter: "How do I implement a binary search in Python?" Copilot chat is ideal for exploring new coding concepts or getting help with unfamiliar syntax.

Copilot might respond with:

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## Inline Chat

Inline chat enables context-specific conversations with Copilot directly within your code editor. You can use this feature to request code modifications or explanations without switching contexts.

- Place your cursor where you want assistance
- Use the keyboard shortcut **Ctrl+I** (Windows or Linux) or **Cmd+I** (Mac) to open inline chat
- Ask questions or request changes specific to that code location

Inline chat helps you focus on a specific section of your code and receive targeted advice. Additionally, you can utilize slash commands for more efficient interaction.

### Slash Commands

Slash commands are shortcuts that allow you to quickly perform actions in Copilot. These commands provide a convenient way to interact with Copilot without needing to navigate through menus.

Here are some common slash commands and their usage:

- **/explain** - Provides an explanation of the selected code
- **/suggest** - Offers code suggestions based on the current context
- **/tests** - Generates unit tests for the selected function or class
- **/comment** - Converts comments into code snippets

To use a slash command, just type the command in your editor and press Enter. For example:

```python
# Select the function, use the shortcut to open the inline chat, and type: /explain
def calculate_average(numbers):
```

## Comments to Code

Copilot uses natural language processing to convert comments into code. You can describe the functionality that you want in a comment. When you select the Enter key, Copilot generates code based on your description.

Here's an example:

```python
# Function to reverse a string
def reverse_string(s):
    # Copilot suggests the function body here
```

```python
# Function to reverse a string
def reverse_string(s):
    return s[::-1]
```

This approach is beneficial for drafting code quickly, especially when your task is straightforward.

## Multiple Suggestions

For complex code snippets, Copilot can offer multiple alternatives.

- When Copilot offers a suggestion, look for the light bulb icon
- Select the icon or use **Alt+]** (Windows/Linux) or **Option+]** (Mac) to cycle through alternatives

Multiple suggestions help you explore different coding approaches and select the most appropriate one.

## Explanations

Understanding existing code is crucial, especially in large projects. You can use the Explain This feature to get explanations for code snippets.

- Select a block of code
- Right-click the code block, and then select **Copilot: Explain This** on the shortcut menu
- Read the explanation that Copilot provides for the selected code

This feature is useful for learning purposes and when you're reviewing code that someone else wrote.

## Automated Test Generation

Unit tests are essential for ensuring code quality and reliability. Copilot can save you time and effort by generating unit tests for your functions or classes.

- Select a function or class
- Use the command palette to select **Copilot: Generate Unit Tests**
- Review the test cases that Copilot suggests for your code

Here's an example:

```python
def add(a, b):
    return a + b

# Copilot might generate a test like this:
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

Automated test generation helps you maintain code integrity and catch bugs early in the development process.

> **Note:** Keep in mind that Copilot learns from context. Keeping your code well structured and commented helps Copilot provide more accurate and relevant assistance. The more you interact with Copilot, the better it becomes at understanding your coding style and preferences.



# 1.4  # Set Up, Configure, and Troubleshoot GitHub Copilot

This unit explains how to sign up for GitHub Copilot, how to configure GitHub Copilot by using VS Code, and how to troubleshoot GitHub Copilot by using VS Code.

## Sign Up for GitHub Copilot

Before you can start using GitHub Copilot, you need to set up a free trial or subscription for your account.

To get started, select your GitHub profile photo, and then select **Settings**. Copilot is on the left menu under **Code, planning, and automation**.

After you sign up, you need to install an extension for your preferred environment. GitHub Copilot supports GitHub.com (which doesn't need an extension), VS Code, Visual Studio, JetBrains IDEs, and Neovim as an unobtrusive extension.

For this module, you'll just review extensions and configurations for VS Code. The exercise that you'll complete in the next unit uses VS Code.

If you're using a different environment, you can find specific links to set up other environments in the "References" section at the end of this module.

## Configure GitHub Copilot in VS Code

### Add the VS Code Extension for GitHub Copilot

1. In Visual Studio Marketplace, go to the GitHub Copilot extension page and select **Install**
2. A popup dialog asks you to open VS Code. Select **Open**
3. In VS Code, on the Extension: GitHub Copilot tab, select **Install**
4. If you didn't previously authorize VS Code in your GitHub account, you're prompted to sign in to GitHub in VS Code. Select **Sign in to GitHub**

GitHub Copilot can autocomplete code as you type when you use VS Code. After installation, you can enable or disable GitHub Copilot, and you can configure advanced settings within VS Code.

### Enable or Disable GitHub Copilot in VS Code

On the bottom pane of the VS Code window, select the status icon, and then select **Enable** or **Disable**.

*Screenshot of the status icon for GitHub Copilot in Visual Studio Code. When GitHub Copilot is enabled, the background color matches the color of the status bar.*

When you're disabling GitHub Copilot, VS Code asks whether you want to disable completions globally or for the language of the file that you're currently editing.

- To disable GitHub Copilot completions globally, select **Disable completions**
- To disable GitHub Copilot completions for a specified language, select **Disable completions for LANGUAGE**

### Enable or Disable Inline Suggestions in VS Code

1. On the **File** menu, select **Preferences > Settings**

*Screenshot of the File menu in Visual Studio Code. The Preferences dropdown submenu is open with the Settings command selected.*

2. On the left-side pane of the Settings tab, select **Extensions**, and then select **GitHub Copilot**

3. Under **Editor: Enable Auto Completions**, select or clear the checkbox to enable or disable inline suggestions

Additionally, you can choose to enable or disable inline suggestions and specify for which languages you want to enable or disable GitHub Copilot.

## Troubleshoot GitHub Copilot in VS Code

In VS Code, the log files are useful for diagnosing connection problems. The GitHub Copilot extension stores the log files in the standard log location for VS Code extensions. You can find the log files by opening the command palette and then entering either **Developer: Open Log File** or **Developer: Open Extensions Logs Folder**.

In rare cases, errors might not be logged in the regular locations. If you encounter errors and nothing is in the logs, you might try to view the logs from the process that's running VS Code and the extension. This process enables you to view the Electron logs. You can find these logs by selecting **Help > Toggle Developer Tools** in VS Code.

Network restrictions, firewalls, or your proxy might cause problems when you're connecting to GitHub Copilot. If a problem occurs, use the following steps to open a new editor with the relevant information that you can inspect yourself or share with the support team:

### Collect Diagnostics

1. Open the VS Code command palette, and then:
   - **For Mac**, use **Shift+Command+P**
   - **For Windows or Linux**, use **Ctrl+Shift+P**

2. Enter **Diagnostics**, and then select **GitHub Copilot: Collect Diagnostics** from the list

For more information on how to troubleshoot in other environments, check out the "References" section at the end of this module.


# 1.5 Exercise - Develop with AI-powered Code Suggestions by Using GitHub Copilot and VS Code

This exercise walks you through the following steps:

- Install GitHub Copilot by using GitHub Codespaces
- Prompt GitHub Copilot for code suggestions
- Accept code suggestions from GitHub Copilot

## Instructions

1. Select the **Start the exercise on GitHub** button at the bottom of this page. It takes you to a public GitHub template repository that prompts you to complete a series of small challenges.

2. Select the **Start course** button or the **Use this template** feature in the template repository. This action prompts you to create a new repository. We recommend that you create a public repository, because private repositories use GitHub Actions minutes.

   After you make your own repository from the template, wait about 20 seconds and refresh.

3. Follow the instructions on the repository's **README** tab to understand how the exercise works, its learning objectives, and how to successfully complete the exercise.

4. When you finish the exercise in GitHub, return to this module for:
   - A quick knowledge check
   - A summary of what you learned
   - A badge for completing this module

> **Note**
> 
> You don't need to modify any of the workflow files to complete this exercise. Altering the contents in this workflow can break the exercise's ability to validate your actions, provide feedback, or grade the results.

---

**Start the exercise on GitHub**
https://github.com/skills/getting-started-with-github-copilot

# 1.6 Module Assessment

## Check Your Knowledge

### 1. What is GitHub Copilot?

- [x] **GitHub Copilot is an AI pair programmer that you can use to get code suggestions.**
- [ ] GitHub Copilot is OpenAI Codex, a new AI system that OpenAI created.
- [ ] GitHub Copilot is a JavaScript public repository and is one of the best-supported languages.
- [ ] GitHub Copilot can write a comment that describes logic, and you can add your suggested code to implement the solution.

**Answer: GitHub Copilot is an AI pair programmer that you can use to get code suggestions.**

*Explanation: GitHub Copilot is an AI-powered tool that acts as a pair programmer, providing real-time code suggestions and completions to help developers write code faster and more efficiently.*

### 2. What are the supported IDE extensions for GitHub Copilot?

- [ ] VS Code and Visual Studio
- [x] **GitHub.com, VS Code, Visual Studio, Neovim, and JetBrains**
- [ ] VS Code, Visual Studio, Neovim, and JetBrains

**Answer: GitHub.com, VS Code, Visual Studio, Neovim, and JetBrains**

*Explanation: GitHub Copilot supports multiple development environments including GitHub.com (which doesn't need an extension), VS Code, Visual Studio, Neovim, and the JetBrains suite of IDEs.*

### 3. What is the difference between GitHub Copilot Business and GitHub Copilot Enterprise?

- [ ] GitHub Copilot Enterprise has code completions, whereas GitHub Copilot Business doesn't.
- [ ] GitHub Copilot Enterprise has chat in IDE and mobile, whereas GitHub Copilot Business doesn't.
- [x] **GitHub Copilot Enterprise has an extra layer of personalization. Organizations use their own codebase to train GitHub Copilot.**
- [ ] GitHub Copilot Enterprise has an extra layer of security, with IP indemnity and enterprise-grade security, safety, and privacy.

**Answer: GitHub Copilot Enterprise has an extra layer of personalization. Organizations use their own codebase to train GitHub Copilot.**

*Explanation: GitHub Copilot Enterprise includes everything in GitHub Copilot Business plus additional personalization features. It can index an organization's codebase for deeper understanding and more tailored suggestions, and offers access to GitHub Copilot customization to fine-tune private models for code completion.*


# 1.7 Summary


GitHub is working to personalize GitHub Copilot for every team, project, and repository that uses it. The goal is to improve the software development life cycle, from writing code to submitting pull requests and beyond.

Together with Microsoft's knowledge model, GitHub is harnessing the reservoir of data and insights that exists in every organization to strengthen the connection between all workers and developers. These insights help every idea to go from code to reality without friction. At the same time, GitHub continues to innovate and update the heart of GitHub Copilot, the AI pair programmer that started it all.

GitHub Copilot is heralding a new generation of more productive, fulfilled, and happy developers who ship better software for everyone.

## Learning Outcomes

Now that you've finished this module, you should be able to:

- Explain the GitHub Copilot features and the subscription plans (Free, Pro, Business, and Enterprise)
- Get started with and configure GitHub Copilot
- Develop by using GitHub Copilot and VS Code

## References

- GitHub Copilot Certification Exam Prep
- GitHub Copilot features
- Research: quantifying GitHub Copilot's impact on developer productivity and happiness
- What is GitHub Copilot?
- About GitHub Copilot and JetBrains IDEs
- About GitHub Copilot and Vim/Neovim
- About GitHub Copilot and Visual Studio
- Viewing logs for GitHub Copilot in your environment
- Subscribing to Copilot as an individual user




