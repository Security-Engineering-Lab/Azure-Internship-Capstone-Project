

# Guided project – Build a sample app to evaluate Microsoft Entra External ID for seamless and secure sign-up and sign-in for consumers and business customers
https://learn.microsoft.com/en-us/training/entra-external-identities/

Discover how Microsoft Entra External ID can provide secure, seamless sign-in experiences for your consumers and business customers. Explore tenant creation, app registration, flow customization, and account security.

This is a guided project module where you’ll complete an end-to-end project by following step-by-step instructions.

#### Learning objectives
In this module, you'll practice how to:
- Build a branded, seamless, and secure sign-up and sign-in experiences for your web application
- Assess Microsoft Entra External ID identity provider capabilities against consumer and business customer needs


#### Prerequisites
- An Azure subscription and Azure account
- If you don’t have any Azure subscriptions, you can create a free trial tenant using your existing Outlook or Hotmail account, or GitHub or personal email address (you’ll be prompted to create an Outlook account with your GitHub or personal email)
- (Optional) The latest version of Visual Studio Code
- (Optional) The latest version of PowerShell



## 1 Introduction

## Introduction to Microsoft Entra External ID

Suppose you work for an online grocery retailer, and your team is gearing up to launch a new website. You want to make sure that existing and new customers have a seamless experience signing in or creating an account on your website. The marketing team wants to make sure that the company brand is represented, while the security team is asking to secure user accounts. You need a cloud-hosted identity and access management solution that lets you customize the flows, add branding, manage the accounts customers can sign-in or sign up with, orchestrate verification, and protect with robust security.
Learning objectives
In this module, you'll:

Build a branded, seamless, and secure sign-up and sign-in experiences for your web application
Assess Microsoft Entra External ID identity provider capabilities against consumer and business customer needs

### Prerequisites

An Azure subscription and Azure account
If you don't have an Azure subscription, you can create a free trial tenant using your existing Outlook or Hotmail account, or GitHub or personal email address (you'll be prompted to create an Outlook account with your GitHub or personal email)
(Optional) The latest version of Visual Studio Code
(Optional) The latest version of PowerShell


# 2 Prepare

## Project overview

Our project aims to launch a new website for our online grocery retailer. The primary goal is to ensure seamless sign-in and account creation experiences for both existing and new customers. The marketing team emphasizes brand representation, while the security team focuses on protecting user accounts. To achieve our goal, we'll implement Microsoft Entra External ID, a cloud-hosted identity and access management solution.

## High-level approach

1. **Tenant Creation:** We'll set up a tenant to store user accounts securely.
2. **App Registration:** Register our app to integrate with Microsoft Entra External ID.
3. **Customized User Experiences:**
   - **During Sign-In:** Customize the sign-in process, including branding elements.
   - **During Sign-Up:** Configure account creation, attribute collection, account types, and extension for information verification.
4. **Account Security:** Prompt users to enroll in multifactor authentication for enhanced security.

## Configuration options

Throughout the module, you can select your preferred configuration option to follow along.

![](https://learn.microsoft.com/en-us/training/entra-external-identities/media/prepare/1_inline.png)

- The **Microsoft Entra admin center** provides an intuitive interface for straightforward configuration tasks.
- The **Microsoft Graph API** enables customization and automation of tasks.



# 3 Create an external tenant

## Select a configuration option

### Exercise - Create an external tenant

You'll need to create a tenant with external configuration in the Microsoft Entra admin center to get started. Once this external tenant is created, you can access it in both the Microsoft Entra admin center and the Azure portal. There are two sections to this unit: **If you don't have an Azure subscription** and **If you already have an Azure subscription**. Scroll to the unit that best matches your situation.

> **Note**
> 
> You'll need at least the Tenant Creator directory role to create an external tenant.

Do you have feedback? Please let us know how your proof of concept project is going. We'd love to hear from you!

## If you don't have an Azure subscription

If you don't have an Azure subscription, you can create a trial tenant for free.

> **Important**
> 
> At the end of the 30-day free trial period, extensions are not available. If no Azure subscription is added, your free trial tenant will be disabled and deleted. You have the following options:
> 
> **Upgrade your tenant:** If you're ready to upgrade before the trial period ends, you can upgrade your free trial tenant to a paid subscription.
> **Register for another trial:** Use the same link aka.ms/ciam-free-trial to start a new trial.

To create a trial tenant, navigate to aka.ms/ciam-free-trial.

On the Sign in page, use the sign-in box (label A) to enter your Outlook or Hotmail email. If you don't have any of those, you can select **Create one!** (label B) to create a new Outlook account. Alternatively, you can also sign in with your GitHub account (label C). 

![](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/11_inline.png)

Once you're signed in or have created an account, you'll be redirected to Microsoft Entra admin center. This is the start of setting up your free trial tenant. To customize the tenant domain and name, as well as location, select **Change settings**.

![](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/12_inline.png)

You'll see the following fields are customizable for your free trial tenant:

- **Tenant name:** you can include your company name and the fact that this is a test external tenant. For example, Woodgrove CIAM Dev
- **Domain name:** for best practices, it's good to include the purpose of the tenant. For example, if your developer team is trying out the product with a possibility to upgrade later, you might want to add dev after your company name, like this: woodgrove-ciam-dev.
- **Location:** Specify the location for this trial tenant.


![](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/13_inline.png)

When you're done, check the checkbox to agree to Microsoft Customer Agreement and Privacy Statement, then select **Continue**. It will take a few minutes for the next step to launch.

![](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/14_inline.png)

You may encounter a dialogue twice that asks if you want to leave the site. Select **Leave** twice. This happens because the Microsoft Entra admin center is trying to leave the free trial setup experience and launch the get started guide titled **Sign in your users in 3 easy steps**.


![](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/15_inline.png)

The **Sign in your users in 3 easy steps** guide, also known as get started guide, has launched. You can select how you would like your customers to sign in and the branding they'll see.


![](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/16_inline.png)

You can scroll down to view a preview of your sign-in page. When you're done, select **Continue**.

![](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/17_inline.png)

Wait for a few minutes until the **Run it now** button is ready. When it's ready, select **Run it now** to view the sign-in experience.

![](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/18_inline.png)

The preview will launch, reflecting the customizations you've made so far.

![](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/19_inline.png)

Come back to the Microsoft Entra admin center, and select **Continue**. If you want to make changes to the customizations so far, select **Previous**.

![](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/20_inline.png)

(This step is optional) Finally, you can add your sign-in experience to a sample app. Select from the options **Single Page Application (SPA)**, **Web application**, **Desktop app**, and **Mobile app**.

![Screenshot of Select your app type section highlighted.](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/21_inline.png)

(This step is optional) Depending on the app type you selected earlier, you can view languages to choose from. Under **Set up and run the sample app**, you have the option to download your sample app and run the code in your environment. Select **Continue** when you're done downloading the sample code you need.

![Screenshot of "Select your language" and "Set up and run the sample app" sections highlighted.](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/22_inline.png)

## If you already have an Azure subscription

To create a tenant, sign in to the Microsoft Entra admin center and browse to **Identity > Overview**. Then, select **Manage tenants**.

![Screenshot of the Identity Overview page. The toolbar button titled Manage tenants is highlighted.](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/1_inline.png)

On the **Manage tenants** page, select **Create**.

![Screenshot of the Manage tenants page. The toolbar button titled Create is highlighted.](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/2_inline.png)

Select **External**, and then select **Continue**.

![Screenshot of Choose a configuration for your tenant. The External choice group is selected.](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/3_inline.png)

On the **Basics** tab, in the **Create a tenant** page, enter the following information:
- Type your desired **Tenant Name** (for example Woodgrove live demo).
- Type your desired **Domain Name** (for example woodgrovelive).
- Select your desired **Location**. This selection can't be changed later.

Then, select **Next: Add a subscription**.

![Screenshot of Create a tenant wizard navigation with first step titled Basics selected. The Tenant Name, Domain Name, and Location are filled out.](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/3_inline.png)

On the **Add a subscription** tab, enter the following information:
- Next to **Subscription**, select your subscription from the menu.
- Next to **Resource group**, select a resource group from the menu. If there are no available resource groups, select **Create new**, add a name, and then select **OK**.
- If **Resource group location** appears, select the geographic location of the resource group from the menu.

Then, select **Review + Create**.

![Screenshot of Create a tenant wizard navigation with second step titled Add a subscription selected. The subscription and resource group are filled out.](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/5_inline.png)

If the information that you entered is correct, select **Create**. The tenant creation process can take up to 30 minutes.

![Screenshot of Create a tenant wizard navigation with third and final step titled Review and create selected. The green information box confirms that validation passed. The button at the bottom of the wizard titled Create is highlighted.](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/6_inline.png)

You can monitor the progress of the tenant creation process in the **Notifications** pane. Once the tenant is created, you can access it in both the Microsoft Entra admin center and the Azure portal.

![Screenshot of Notifications pane open on the right with the latest activity log titled Create tenant confirming that tenant creation was successful.](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/7_inline.png)

Use the **Settings** icon in the top menu to **Switch to your customer tenant** you created from the **Directories + subscriptions** menu. If the tenant you created doesn't appear in the list, refresh the page (using the web browser refresh button).

![Screenshot of Directories and subscriptions page with the switch button for the bottom listed directory highlighted.](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/8_inline.png)

Browse to **Home > Tenant overview** to start configuring your tenant.

![Screenshot of Identity Overview page with Overview highlighted in the sidebar.](https://learn.microsoft.com/en-us/training/entra-external-identities/media/create-an-external-tenant/9_inline.png)

**Well done!** At this point, the Microsoft Entra External ID tenant is ready to use.
