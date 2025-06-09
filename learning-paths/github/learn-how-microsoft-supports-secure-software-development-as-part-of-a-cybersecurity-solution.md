

#   Learn how Microsoft supports secure software development as part of a cybersecurity solution

https://learn.microsoft.com/en-us/training/paths/secure-software-development-for-cybersecurity/


# 1 Microsoft Azure Well-Architected Framework - Security

Learn how to incorporate security into your architecture design, and discover the tools that Azure provides to help you create a secure environment through all the layers of your architecture.


# 1.1 Introduction

The Azure Well-Architected Framework is a design framework that can improve the quality of a workload by helping it to:

* Be resilient, available, and recoverable.
* Be as secure as you need it to be.
* Deliver a sufficient return on investment.
* Support responsible development and operations.
* Accomplish its purpose within acceptable timeframes.

A Well-Architected workload must be built with a zero-trust approach. A secure workload is resilient to attacks and incorporates the interrelated security principles of confidentiality, integrity, and availability (also known as the CIA triad) in addition to meeting business goals. Any security incident has the potential to become a major breach that damages the brand and reputation of the workload or organization. To measure the security efficacy of your overall strategy for a workload, start with these questions:

* Do your defensive investments provide meaningful cost and friction to prevent attackers from compromising your workload?
* Will your security measures be effective in restricting the blast radius of an incident?
* Do you understand how controlling the workload could be valuable for an attacker? Do you understand the impact to your business if the workload and its data are stolen, unavailable, or tampered with?
* Can the workload and operations quickly detect, respond to, and recover from disruptions?

The concepts described in this module are not all-inclusive of security in a workload, but they represent the core principles and some of their key approaches when you're designing a workload. For a complete perspective, across all of the Well-Architected Framework pillars, visit the Azure Well-Architected Framework as you start planning and designing your architecture.

Each unit in this module focuses on one design principle and three approaches associated with that principle. The approaches in each unit are supported through the use of examples to help demonstrate how they can be applied to real-world scenarios. The examples are all based on a fictional company.

## Learning objectives

By the end of this module, you'll understand the five principles of the Security pillar and learn three approaches for each of the following:

* Create a security readiness plan that's aligned with business priorities.
* Properly handle confidentiality requirements.
* Strengthen the integrity of your workload against security risks.
* Strengthen the availability of your workload against security incidents.
* Continuously maintain and improve your workload's security posture

## Prerequisites

* Experience building or operating solutions by using core infrastructure technology such as data storage, compute, and networking
* Experience building or operating technology systems to solve business problems


# 1.2 Plan your security readiness

*Strive to adopt and implement security practices in architectural design decisions and operations with minimal friction.*

As a workload owner, you have a shared responsibility with the organization to protect assets. Create a security readiness plan that's aligned with business priorities. It will lead to well-defined processes, adequate investments, and appropriate accountabilities. The plan should provide the workload requirements to the organization, which also shares responsibility for protecting assets. Security plans should factor into your strategy for reliability, health modeling, and self-preservation.

In addition to organizational assets, the workload itself needs to be protected from intrusion and exfiltration attacks. All facets of Zero Trust and the CIA triad should be factored into the plan.

Functional and non-functional requirements, budget constraints, and other considerations shouldn't restrict security investments or dilute assurances. At the same time, you need to engineer and plan security investments with those constraints and restrictions in mind.

## Example scenario

Contoso Supermarket has never had a customer loyalty program before, but have decided it makes business sense to build one. NFC functionality on customer phones will be used as the solution at point-of-sale for both self-checkout and cashier-assisted checkout. A self-registration kiosk at the store entrance and exit will enable customers to enroll in the program. The backend processing solution will be cloud hosted, but the design isn't finalized yet.

## Optimize security through segmentation
Use segmentation as a strategy to plan security boundaries in the workload environment, processes, and team structure to isolate access and function.

Your segmentation strategy should be driven by business requirements. You can base it on criticality of components, division of labor, privacy concerns, and other factors.

You'll be able to minimize operational friction by defining roles and establishing clear lines of responsibility. This exercise also helps you identify the level of access for each role, especially for critical-impact accounts.

Isolation enables you to limit exposure of sensitive flows to only roles and assets that need access. Excessive exposure could inadvertently lead to information flow disclosure.

### Contoso's challenge

In the spirit of simplicity, the team has historically favored low overhead approaches. These approaches have included co-locating disparate workload components to reduce management surface area and organizing disparate individuals into security groups to simplify access management.

Unfortunately, a QA intern who was granted broad access to the new deployment environment due to their security group membership was subject to a social engineering attack that led to a compromise of their account.

The attacker was able to compromise the confidentiality of not just that deployment, but all of the others running on the same application platform.

### Applying the approach and outcomes

Luckily, the compromised environment was hosting an early test prototype of the workload; while they are designing the new customer loyalty program system for the point-of-sale system, so no production systems were breached.

The workload security team plans on investing time and money to design the workload to isolate systems that handle personally identifiable information (PII), such as the address and email of customers, from those components that don't (such as the coupons for products); design access controls that are need-to-know and just-in-time (JIT) where possible; and isolate networks both within the workload to protect other components and back into Contoso to protect the organization.

Through segmentation, a compromise may still have an impact to aspects of the workload, but the blast radius will be contained.

## Respond to incidents efficiently
Make sure there's an incident response plan for your workload. Use industry frameworks that define the standard operating procedure for preparedness, detection, containment, mitigation, and post-incident activity.

At the time of crisis, confusion must be avoided. If you have a well-documented plan, responsible roles can focus on execution without wasting time on uncertain actions. Also, a comprehensive plan can help you ensure that all remediation requirements are fulfilled.

### Contoso's challenge

The workload team is starting to formalize retailer support channels, customer support channels, and technical on-call rotations for support escalations and for outages.

They haven't addressed security specifically in these plans. They also don't know what Contoso, as an organization offers for support.

### Applying the approach and outcomes

The workload team works with the Contoso security team to understand compliance requirements for dealing with PII of this nature, both from an organization perspective and from external compliance perspective.

The team builds a security detection, mitigation, and escalation plan, including standardized communication requirements for incidents.

The workload team now feels just as comfortable with security incident preparedness as they do with their reliability support. They plan on drilling on security incidents to dry run and refine the plan before they go live with the system.

## Codify secure operations and development practices
Define and enforce team-level security standards across the lifecycle and operations of the workload. Strive for consistent practices in operations like coding, gated approvals, release management, and data protection and retention.

Defining good security practices can minimize negligence and the surface area for potential errors. The team will optimize efforts and the outcome will be predictable because approaches are made more consistent.

Observing security standards over time will enable you to identify opportunities for improvement, possibly including automation, which will streamline efforts further and increase consistency.

### Contoso's challenge

After preparing for incident response, the workload team decides they need to invest time and effort to prevent issues in the first place.

They currently don't have any specific secure development lifecycle in mind, and plan on using the same processes they used on prior projects.

### Applying the approach and outcomes

While this workload won't hold highly confidential data like credit card information, the team treats their customers' data with respect and are aware that there are local and federal regulations that must be followed for the types of data that will be held.

The team invests in learning about current industry-standard secure development and operations practices and adopts measures that they had previously lacked.

The team also shares their learnings with the Contoso security team to ensure that best practices are being adopted across the enterprise.

## Check your knowledge

### 1. What is a benefit of using segmentation in your approach to security?

- **✅ Segmentation allows you to isolate access to resources based on the principle of least privilege.**
- Segmentation blocks all access to resources, which prevents attackers from accessing them.
- Segmentation forces all users to use multifactor authentication (MFA) to access resources.
- Segmentation forces all users to use single sign-on (SSO) to access resources.

**Explanation:** Segmentation allows you to isolate access to resources based on the principle of least privilege, ensuring that users and systems only have access to the resources they need to perform their functions. This minimizes the blast radius of potential security incidents and prevents lateral movement by attackers.

### 2. What type of plan should you create to ensure that security events are detected and responded to in a timely manner?

- A disaster recovery plan
- A business continuity plan
- **✅ A security incident response plan**
- A DDoS mitigation plan

**Explanation:** A security incident response plan is specifically designed to ensure that security events are detected and responded to in a timely manner. It defines the standard operating procedures for preparedness, detection, containment, mitigation, and post-incident activities.

### 3. True or false: Contoso's use of secure development practices will help the team ensure that all code is developed in a consistent standard manner.

- **✅ True.**
- False.

**Explanation:** True. Secure development practices help establish consistent standards and processes across the development lifecycle. This reduces the surface area for potential errors, ensures predictable outcomes, and enables the team to identify opportunities for improvement and automation over time.


# 1.3 Design to protect confidentiality

*Prevent exposure to privacy, regulatory, application, and proprietary information through access restrictions and obfuscation techniques.*

Workload data can be classified by user, usage, configuration, compliance, intellectual property, and more. Workload data must not be shared or accessed beyond the established trust boundaries. Efforts to protect confidentiality should focus on access controls, opacity, and keeping an audit trail of activities that pertain to data and the system.

## Example scenario

Contoso Rise Up provides a multitenant, Software-as-a-Service offering that specializes in supporting nonprofits in their fundraising and donation activities. They've been in the market for a few years now with a healthy client base. The solution is built on Azure Red Hat OpenShift (ARO) and Azure Database for PostgreSQL. It offers both isolated tenants and colocated tenants as a more affordable offering.

## Strictly limit access
Implement strong access controls that grant access only on a need-to-know basis.

The workload will be protected from unauthorized access and prohibited activities. Even when access is from trusted identities, the access permissions and exposure time will be minimized because the communication path is open for a limited period.

### Contoso's challenge

Contoso Rise Up has always prided itself on amazing customer support. Everyone on the support team has ready-access to customer data to help troubleshoot and advise in real-time.

The support team is regularly trained on ethical access.

Unfortunately, one disgruntled support employee copied and publicly shared the donor list for an organization, breaching the customer's confidentiality. While the employee was fired, the reputation harm to Contoso Rise Up was already done.

### Applying the approach and outcomes

Contoso Rise Up implemented strict segmentation of users into Microsoft Entra ID groups and defined RBAC for those groups to the various resource groups and resources.

All access to data is time limited and goes through an approval and auditing process.

These standards have been applied across the workload and customer support teams. Contoso Rise Up now is confident that there's no standing access to customer data.

## Identify confidential data through classification
Classify data based on its type, sensitivity, and potential risk. Assign a confidentiality level for each. Include system components that are in scope for the identified level.

This evaluation helps you right-size security measures. You'll also be able to identify data and components that have a high potential impact and/or exposure to risk. This exercise adds clarity to your information protection strategy and helps ensure agreement.

### Contoso's challenge

The donor management system stores many different types of data, ranging from information that is confidential to Contoso Rise Up (such as it's customer list), to information that's confidential to its customers (such as the donor list), and information that's confidential to its customers' donors (such as their mailing address).

The system also holds nonsensitive data, like stock images and document templates.

The workload team has never taken the time to classify data, and has simply applied security broadly across the dataset.

### Applying the approach and outcomes

Following the taxonomy lead of the Contoso organization, the workload team spends time to flag data stores, columns, storage accounts, and other storage resources with metadata that indicate what type and sensitivity of data exists there.

This activity gives the team the opportunity to validate that sensitive data is treated with the level of confidentiality required throughout the entire system, including logging statements and backups.

The team finds that they have some relatively sensitive data in a lower security database and have some nonsensitive data in a higher security database. They'll be adjusting storage locations to make sure security controls are aligned with the data they're protecting.

They also plan on implementing data masking on key fields to better protect the confidentiality of data, even when authorized staff access the system.

## Apply encryption at every step of the data lifecycle
Safeguard your data at rest, in transit, and during processing by using encryption. Base your strategy on the assigned confidentiality level.

By following this approach, even if an attacker gets access, they won't be able to read properly encrypted sensitive data.

Sensitive data includes configuration information that's used to gain further access inside the system. Data encryption can help you contain risks.

### Contoso's challenge

Contoso Rise Up takes per-tenant backups of the PostgreSQL databases using the built-in point-in-time restores. Additionally, for added assurances they make one transactionally consistent backup per day to an isolated storage account for full disaster recovery (DR) preparedness.

The storage account used for DR is restricted with just-in-time access and few Microsoft Entra ID accounts are allowed to access it.

During a recovery drill, an employee went through the process to access a backup, and accidentally copied a backup to network share in the Contoso organization.

This backup was discovered and reported to Contoso's privacy team a few months later, launching an investigation into how it was accessed between the point of the incident and the time of discovery. Luckily there was no confidentiality breach detected, and the file was deleted after the forensics and audit review was complete.

### Applying the approach and outcomes

The team has formalized a new process dictating that all backups must be encrypted at rest and the encryption keys must be secured in Key Vault.

Now incidents like this will have a lower chance of privacy breach, as the data contained in the backup file would be useless without the ability to decrypt.

Additionally, the DR plan now includes standard guidance dictating proper handling of the backups, including how and when to safely decrypt a backup.

## Check your knowledge

### 1. Which of the following is an example of a user with a need to have access to confidential customer data?

- **✅ A customer service representative who needs to resolve customer issues.**
- A marketing employee who sends out marketing emails to customers.
- A sales executive who needs to create a report for management.
- A finance employee who needs to create invoices for customers.

**Explanation:** A customer service representative who needs to resolve customer issues has a legitimate business need to access confidential customer data as part of their job function. This follows the principle of least privilege and need-to-know access. The other roles don't require direct access to confidential customer data to perform their primary functions.

### 2. True of false: data classification is a process that you should perform only once.

- True
- **✅ False**

**Explanation:** False. Data classification is an ongoing process that should be performed regularly. As new data is created, modified, or its sensitivity changes, the classification should be updated. Additionally, business requirements, regulatory changes, and security postures evolve over time, requiring periodic review and updates to data classification schemes.

### 3. What is an example of how Contoso applied encryption to protect data integrity?

- They used Azure Disk Encryption to encrypt data on their virtual machines.
- All of the data was encrypted by default.
- They used Azure Storage Service Encryption to encrypt data in their storage accounts.
- **✅ They used Azure Key Vault to encrypt data in their storage accounts.**

**Explanation:** According to the scenario, Contoso formalized a process that all backups must be encrypted at rest and the encryption keys must be secured in Key Vault. This shows they used Azure Key Vault to manage encryption keys for protecting their backup data, which helps protect data confidentiality (not integrity as the question incorrectly states).
