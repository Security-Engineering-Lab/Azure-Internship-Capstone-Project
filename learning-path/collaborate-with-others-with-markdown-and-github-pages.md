

# Collaborate with others with Markdown and GitHub Pages
https://learn.microsoft.com/en-us/training/paths/collaborate-markdown-github-pages/


# 1 Introduction to GitHub

# 3 Create and host web sites by using GitHub Pages

Learn how to host your personal, organization, and project sites for free with GitHub Pages

# 3.1 Introduction

GitHub Pages are free static web sites hosted directly from your GitHub repository. Anyone can use standard technologies like YAML and Markdown, to build and maintain a site in minutes.

Suppose you want to set up a basic web site to share information about the project on which you're working. It might be a personal site, like a resume or portfolio; or it might be a professional site, like a user guide or developer reference. With GitHub Pages, you can spin up the site in minutes and allow anyone with a basic understanding of Markdown to contribute to it. You also get all the benefits of GitHub for source control, including branches and pull requests.

In this module, you learn how to set up and use GitHub Pages to host both personal and professional sites.

**Learning objectives**

In this module, you'll:
* Enable GitHub Pages
* Choose a theme with Jekyll
* Use YAML front matter
* Customize your site
* Create and edit blog posts

**Prerequisites**

* A GitHub account
* The ability to navigate and edit files in GitHub

We recommend that you complete Communicate effectively on GitHub by using Markdown before beginning this module.

# 3.2 What is GitHub Pages?

Here, we discuss the process of creating and maintaining a GitHub Pages web site.

GitHub Pages are static sites hosted directly from your GitHub repository, but they're more than just a collection of static files. By making use of site-generation technologies like Jekyll and Liquid, developers define dynamic templates that are processed into complete static web sites. Every time you commit a change to the source branch associated with the site, the site is regenerated using the latest updates and automatically published to the target URL.

Learn more about Publishing sources for GitHub Pages sites.

## Enabling GitHub Pages

The first step in using GitHub Pages is to enable it from your repository's Settings tab. You can opt to use the main branch, or specify the docs folder within it. If you ever want to disable GitHub Pages, you can do so here.

Enabling GitHub Pages.

## Choosing a theme with Jekyll

Jekyll is the static site generator GitHub uses to build your web site from the contents of your repository. In addition to providing great content convenience, it also conforms to a standard design convention. This style standardization allows for swappable themes, which you can select from the GitHub Pages configuration.

Choosing a Jekyll theme.

GitHub provides various themes. There's also an array of commercial and open-source themes available from the Jekyll community.

Built-in Jekyll themes.

Learn more about Jekyll Themes.

## Using YAML front matter

The term front matter refers to YAML metadata that prepends the content of a file. For Jekyll, this metadata includes generator instructions to indicate the layout style of a Markdown page (post, page, and so on). It might also include page metadata, such as the document title, or page content variables, such as a blog post's author.

The following example uses the post layout. The example assumes there's a _layouts/post.html file that defines the container HTML. Other layout options can be offered by adding their respective HTML files in the _layouts folder.

```yml
---
layout: post
title: This is set as the document title.
---

This is visible body content, which might use Markdown, HTML, and Liquid templating.
```

Learn more about Front Matter.

## Customizing your site

Once your site is up and running, you can customize details about your site via _config.yml. This file includes virtually all site-wide configuration options, including site metadata, navigation menus, theme colors, compiler options, and more.

Learn more about _config.yml Configuration.

## Creating and editing content

Creating and editing pages on your site follows the standard GitHub experience. The files you use for your GitHub Pages web site enjoy all of the same benefits as other files in your GitHub repository. You can edit them with any tools, create and merge branches, and link with issues or pull requests.

In addition to Markdown and HTML, Jekyll supports the Liquid template language syntax. Liquid lets users dynamically insert variables and basic logic flow constructs into their content files. When compiled, the final product is standard HTML.

The following example shows a combination of for looping and variable insertion.

```markdown
<ul>
  {% for post in site.posts %}
    <li>
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>
```

Learn more about Liquid template language.

## Working with blog posts

Despite not having a database to work with, Jekyll still supports the concept of blogging using a specific convention: _posts/2020-06-25-blog-post-name.md. As you can likely infer, all blog posts are stored in the _posts folder and use the date and name convention as shown. During compilation, Jekyll processes the files in this folder to produce a list of HTML blog posts.

The following example illustrates the structure of a simple blog post. It includes metadata for subtitle, tags, and comments. The theme that you choose, might not support this metadata.

```markdown
---
layout: post
title: Blog post title rendered by theme
subtitle: Blog post subtitle rendered by theme
tags: welcoming
comments: true
---

This is the first line of rendered content in the post.
```

Learn more about Adding content to your GitHub Pages site using Jekyll.



# 3.3 Exercise - Enable, create, and update a GitHub Pages web site

This exercise checks your knowledge on setting up and using GitHub Pages.

## Getting started

When you select the *Start the exercise on GitHub* button at the bottom of the page, it takes you to a public GitHub template repository that prompts you to complete a series of small challenges. Before you can begin the exercise, complete the following tasks:

* Select the *Start course* button or the *Use this template* feature within the template repository. This prompts you to create a new repository. We recommend creating a public repository, as private repositories use Actions minutes. After you make your own repository from the template, wait about 20 seconds and refresh.
* Follow the instructions in the repository's README to understand how the exercise works, its learning objectives, and how to successfully complete the exercise.

When you finish the exercise in GitHub, return here for:
* A quick knowledge check.
* A summary of what you've learned.
* To earn a badge for completing this module.

**Note**

You do not need to modify any of the workflow files to complete this exercise. **Altering the contents in this workflow can break the exercise's ability to validate your actions, provide feedback, or grade the results**.

**Start the exercise on GitHub**

https://github.com/skills/github-pages

# 3.4 Module assessment

Choose the best response for each question.

**Check your knowledge**

## 1. How do you enable GitHub Pages for your repository?

- [ ] Email GitHub support and ask for your free web site installation kit.
- [ ] Subscribe to GitHub Enterprise and wait for further instructions in email.
- [x] **Select a Source from the GitHub Pages section of the Settings tab of your repository.** ✅

**Explanation:** To enable GitHub Pages, you need to go to your repository's Settings tab, find the GitHub Pages section, and select a source (like main branch or docs folder). This is done directly through the GitHub interface without needing to contact support or subscribe to enterprise plans.

## 2. Which of the following can't be hosted on GitHub Pages?

- [ ] Personal sites, like your resume or portfolio.
- [x] **Dynamic server-side applications.** ✅
- [ ] Professional sites, like product pages and marketing campaigns.

**Explanation:** GitHub Pages only hosts static websites. Dynamic server-side applications that require server processing, databases, or backend logic cannot be hosted on GitHub Pages. Personal sites, portfolios, and professional marketing sites can all be hosted as static sites.

## 3. What would you most likely use to edit the body content of your GitHub Pages site?

- [x] **Markdown** ✅
- [ ] Jekyll
- [ ] YAML

**Explanation:** Markdown is the primary language used to write the body content of GitHub Pages sites. Jekyll is the static site generator that processes the content, and YAML is used for front matter metadata, but Markdown is what you use to write the actual content that visitors will read.


# 3.5 Summary

In this module, you learned about the key features of a GitHub Pages web site.

You learned about:
* Enabling GitHub Pages
* Choosing a theme with Jekyll
* Using YAML front matter
* Customizing your site
* Creating and editing blog posts

Now that you know how to use GitHub Pages to support your projects, learn to Manage software delivery by using a release based workflow on GitHub.

**Learn more**

Here are some links to more information on the subjects we discussed in this module.
* GitHub Pages official site
* Jekyll official site
* Liquid template language official site


