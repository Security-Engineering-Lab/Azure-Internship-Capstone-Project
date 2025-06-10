

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
- **✅ They used Azure Storage Service Encryption to encrypt data in their storage accounts.
-  They used Azure Key Vault to encrypt data in their storage accounts.**

**Explanation:** According to the scenario, Contoso formalized a process that all backups must be encrypted at rest and the encryption keys must be secured in Key Vault. This shows they used Azure Key Vault to manage encryption keys for protecting their backup data, which helps protect data confidentiality (not integrity as the question incorrectly states).




# 1.4 Design to protect integrity

*Prevent corruption of design, implementation, operations, and data to avoid disruptions that can stop the system from delivering its intended utility or cause it to operate outside the prescribed limits. The system should provide information assurance throughout the workload lifecycle.*

The key is to implement controls that prevent tampering of business logic, flows, deployment processes, data, and even the lower stack components, like the operating system and boot sequence. Lack of integrity can introduce vulnerabilities that can lead to breaches in confidentiality and availability.

## Example scenario

Contoso Paint Systems creates vapor sensing and ventilation control systems for industrial spray painting machines. The system is also used to automatically capture air quality data for environmental impact reporting purposes. They have a cloud-based application backing their IoT devices that are distributed throughout painting booths. On-premises components of the application run on Azure Stack HCI and custom IoT devices. The system is in early prototype phase, and the workload team plans to release the production version within a year.

## Defend your supply chain
Continuously protect against vulnerabilities and detect them in your supply chain to block attackers from injecting software faults into your infrastructure, build system, tools, libraries, and other dependencies. Vulnerabilities should be scanned for during build time and runtime

Knowing the origin of software and verifying its authenticity throughout the lifecycle will provide predictability. You'll know about vulnerabilities well in advance so that you can proactively remediate them and keep the system secure in production.

### Contoso's challenge

The engineering team is implementing their build and release pipelines, but haven't yet addressed the integrity of the build system.

They've opted to use a few open-source solutions in both the firmware and the cloud components.

They've heard how a supply chain compromise or malicious insiders can corrupt code which can then be used to disrupt systems or even exfiltrate data. If their customer's environmental reporting were impacted in such a way that resulted in a failure to report or a misrepresentation that is found in an audit, the effect on Contoso and their customer could be catastrophic.

### Applying the approach and outcomes

The team modifies their build processes for both firmware and the backend cloud systems, and now include security scanning steps to alert on known common vulnerabilities and exposures (CVEs) in dependencies. Additionally, they now include malware scanning of the code and packages as well.

They also look at antimalware options for running on Azure Stack HCI, such as Windows Defender Application Control.

These measures help increase confidence that the firmware and software that get deployed as part of this solution won't perform unexpected actions, impacting the integrity of the system or the customer's environmental reporting requirements.

## Employ strong cryptographic mechanisms
Establish trust and verify by using cryptography techniques like code signing, certificates, and encryption. Protect those mechanisms by allowing reputable decryption.

By adopting this approach, you'll know that changes to data or access to the system is verified by a trusted source.

Even if encrypted data is intercepted in transit by a malicious actor, the actor won't be able to unlock or decipher the content. You can use digital signatures to ensure that the data wasn't tampered with during transmission.

### Contoso's challenge

The devices selected for sensing and data transfer are currently not capable of enough processing power to support HTTPS or even custom encryption.

The workload team plans to use network boundaries as primary isolation technique.

A risk analysis review highlighted that unencrypted communication between IoT devices and control systems can lead to tampering, and network segmentation shouldn't be considered sufficient.

### Applying the approach and outcomes

Working with the manufacturer of their custom IoT device, the team decides to use a higher powered device that supports not only certificate based communication, but also supports code signing validation on chip, so that only signed firmware will execute.

## Optimize the security of your backups
Ensure backup data is immutable and encrypted when data is replicated or transferred.

By adopting this approach, you'll be able to recover data with confidence that backup data wasn't changed at rest, inadvertently or maliciously.

### Contoso's challenge

Every month the Environment Protection Agency emissions report is generated, but these reports only need to be submitted three times a year.

The report gets generated and then stored in an Azure Storage account until it's needed to be sent. This is done as a backup in case the reporting system experiences a disaster.

The backup report itself isn't encrypted, but is transferred over HTTPs to the storage account.

### Applying the approach and outcomes

After performing a security gap analysis, the team sees that leaving the backup unencrypted is a risk that should be addressed. The team addresses the risk by encrypting the report and storing it in Azure blob Storage's Write One, Read Many (WORM) immutable storage option.

The new approach ensures that the integrity of the backup is maintained.

As an additional integrity measure, the report generated out of the main system now compares a SHA hash against the authoritative backup to detect any tampering with the primary data source.

## Check your knowledge

### 1. Which of the following is a reason to adopt threat scanning in your supply chain

- **✅ Scanning can help detect vulnerabilities in your code.**
- Scanning prevents attackers from exploiting vulnerabilities in your software.
- Scanning ensures that your code is free of vulnerabilities.
- Scanning ensures that your code is free of malware.

**Explanation:** Scanning can help detect vulnerabilities in your code, which is the primary purpose of supply chain threat scanning. While scanning is valuable, it doesn't prevent exploitation, guarantee complete freedom from vulnerabilities, or ensure complete absence of malware - it's a detection and awareness tool that enables proactive remediation.

### 2. Which of these are examples of cryptographic controls?

- Using Azure SQL Database's firewall function to block access to a database.
- **✅ Using code signing and encryption.**
- Using Azure Policy to enforce security baselines.
- Using Microsoft Sentinel to scan your environment.

**Explanation:** Code signing and encryption are cryptographic controls that use mathematical algorithms to protect data integrity and confidentiality. Firewalls, Azure Policy, and Microsoft Sentinel are security controls but not specifically cryptographic in nature.

### 3. How did Contoso ensure that their report backup is immutable?

- They automatically move the report to Archive Storage after it's created.
- The backup is only kept on VM disk storage.
- The report is automatically deleted after 30 days.
- **✅ The report is backed up to Azure Storage using the write-once-read-many (WORM) feature.**

**Explanation:** According to the scenario, Contoso addressed the risk by storing the encrypted report in Azure blob Storage's Write One, Read Many (WORM) immutable storage option. WORM storage ensures that data cannot be modified or deleted once written, providing immutability.


# 1.5 Design to protect availability

*Prevent or minimize system and workload downtime and degradation in the event of a security incident by using strong security controls. You must maintain data integrity during the incident and after the system recovers.*

You need to balance availability architecture choices with security architecture choices. The system should have availability guarantees to ensure that users have access to data and that data is reachable. From a security perspective, users should operate within the allowed access scope, and the data must be trusted. Security controls should block bad actors, but they shouldn't block legitimate users from accessing the system and data.

## Example scenario

Contoso Concierge runs a hotel management software system used in over 50 hotel brands in the United States. It's responsible for booking, guest check-in, and tracks guest services and housekeeping staffing. It's a cloud-based system that runs out of two regions in the United States. It's mostly hosted on virtual machine scale sets. The clients in the hotels are browser-based.

## Enhance reliability through robust security
Use security controls and design patterns to prevent attacks and code flaws from causing resource exhaustion and blocking access.

Adopting this approach helps ensure the system doesn't experience downtime caused by malicious actions, like distributed denial of service (DDoS) attacks.

### Contoso's challenge

The workload team and the workload's stakeholders consider the reliability of this system to be of the utmost importance because so many hotel guests depend on it for business and leisure travel. It must be up for hotels to run their business.

The team has invested considerable resources into testing functional and nonfunctional requirements to ensure reliability stays high, including using safe deployment practices to reliably release application updates.

While they have been focused heavily on reliability, the team has been less attentive to security. Recently, an update was released that contained a code flaw that was exploited by an attacker to bring down the whole system for many hotels. The attack overwhelmed the application servers in one region for over four hours one evening, causing issues for customers and hotel guests.

The attacker used the Contoso application servers to proxy requests to a regional storage account to receive pregenerated folio information. An inordinately large malicious folio was generated which caused the application servers to exhaust resources on the application server as it was being loaded into memory, and client retries spread the issue across all application servers.

### Applying the approach and outcomes

The team looked into a design pattern to remove their application servers from the folio request flow, opting instead for a Valet Key approach. While this wouldn't have prevented the problem, it would've isolated the impact.

They also added more input validation into the system to sanitize input, which will help prevent malicious attempts like this in the future.

Now with input sanitization and a strengthened design, one type of risk has been mitigated.

## Proactively limit attack vectors
Implement preventative measures for attack vectors that exploit vulnerabilities in application code, networking protocols, identity systems, malware protection, and other areas.

Implement code scanners, apply the latest security patches, update software, and protect your system with effective antimalware on an ongoing basis. Doing so helps to reduce the attack surface to ensure business continuity.

### Contoso's challenge

The VMs used to host the system are Azure Marketplace images with the latest Ubuntu OS. The bootstrapping processes for a VM set up a few certificates, tweaks some SSH configuration, and installs the application code, but no antimalware tools are employed.

While Azure Application Gateway fronts the solution, it's only used as an Internet gateway; the web application firewall (WAF) function is not enabled currently.

Both of these configuration choices leave the compute environment unprotected from vulnerabilities in code or through unintended installation of malware.

### Applying the approach and outcomes

After consulting with the security team in Contoso, the virtual machines are now enrolled in an enterprise-managed antivirus solution.

The team also decides to enable and tune the WAF function to help protect the application code by eliminating known risky requests, such as SQL injection attempts, at the gateway level.

The application and application platform now have additional defense in depth, to help protect against exploits that might impact the availability of the system.

## Secure your recovery strategy
Apply at least the same level of security rigor in your recovery resources and processes as you do in the primary environment, including security controls and frequency of backup.

You should have a preserved safe system state available in disaster recovery. If you do, you can fail over to a secure secondary system or location and restore backups that won't introduce a threat.

A well-designed process can prevent a security incident from hindering the recovery process. Corrupted backup data or encrypted data that can't be deciphered can slow down recovery.

### Contoso's challenge

While the system functions as active-active across regions, the team has a disaster recovery plan in place to help restore business continuity in worst case scenarios.

Part of this plan includes shipping backups to a third region in the US.

Unfortunately, the backups were landing in a system that wasn't frequently monitored and had relatively lax security controls. During a drill, they realized that all of the backups have been infected with malware. If they had a real disaster at that time, they wouldn't have been able to recover successfully.

### Applying the approach and outcomes

The team invested time and effort to secure the backup location, adding additional network and identity controls to protect the data. Backups are now also stored in immutable storage to prevent tampering.

After reviewing their security controls, the team finds that during the recovery process, the application runs without a WAF for a period of time. They change the order of operations to close that gap.

Now the team is confident that the backups and the recovery process for the system are no longer an easy-to-exploit attack vector.

## Check your knowledge

### 1. How did Contoso use security controls to respond to an attack that overwhelmed their system?

- **✅ They adopted a design pattern that minimized the blast radius attacks like this one.**
- They blocked access to public-facing services.
- They invested in a third-party DDoS protection service.
- They increased the number of virtual machines in their application.

**Explanation:** Contoso adopted a Valet Key design pattern to remove their application servers from the folio request flow, which would isolate the impact and minimize the blast radius of similar attacks. They also added input validation to sanitize input and prevent malicious attempts.

### 2. What is an example of a preventative measure that can be used to limit attack vectors?

- Monitoring resource health
- **✅ Using an anti-malware solution**
- Enabling autoscaling on virtual machines
- Using Azure Traffic Manager to block malicious traffic

**Explanation:** Using an anti-malware solution is a preventative measure that helps protect systems from malware infections and reduces the attack surface. This is specifically mentioned in the module as one of the measures Contoso implemented to protect their virtual machines.

### 3. True or false: when running in a recovery environment, it's OK to have a relaxed security posture in comparison to the production environment.

- True
- **✅ False**

**Explanation:** False. The module clearly states that you should "apply at least the same level of security rigor in your recovery resources and processes as you do in the primary environment." Recovery environments should maintain the same security standards to prevent security incidents from hindering the recovery process.


# 1.6 Sustain and evolve your security posture

*Incorporate continuous improvement and apply vigilance to stay ahead of attackers who are continuously evolving their attack strategies*

Your security posture must not degrade over time. You must continually improve security operations so that new disruptions are handled more efficiently. Strive to align improvements with the phases defined by industry standards. Doing so leads to better preparedness, reduced time to incident detection, and effective containment and mitigation. Continuous improvement should be based on lessons learned from past incidents.

It's important to measure your security posture, enforce policies to maintain that posture, and regularly validate your security mitigations and compensating controls in order to continuously improve your security posture in the face of evolving threats.

## Example scenario

Contoso Race Day Performance creates data capture systems for professional rally car race teams. Most of the system is embedded in the cars and provides local feedback to the driving crew, but at end of the race all telemetry is uploaded to the cloud for analytical processing. The processing combines track and environmental conditions and vehicle telemetry data into reports that can be used by the race team to evaluate their run and fine tune their strategies. The cloud system uses Azure Spark in Azure Synapse Analytics. Ancillary systems in the workload all use PaaS offerings. The system is already in use by three of the top five race teams in the world.

Race teams are highly protective of their data, and want to know what Contoso Race Day Performance is doing to keep up to date with evolving security threats that might compromise their data.

## Perform threat modeling to identify and mitigate potential threats
Analyze each component of your workflow and evaluate potential threats that each component could be subject to. Classify the identified threats using an industry-standard methodology.

By adopting this approach, you can produce a report of attack vectors prioritized by their severity level. Additionally, you can identify threats and vulnerabilities quickly and set up countermeasures.

### Contoso's challenge

While they haven't had a security incident yet, the workload team doesn't have a standardized way to evaluate if there are any threat vectors that aren't adequately addressed in existing security controls.

The team realizes they have a blind spot with regard to the security of their workload and they are at risk of being caught off-guard if there's a security incident.

### Applying the approach and outcomes

The team engages a security consulting specialist to learn how to perform threat modeling.

After performing an initial threat modeling exercise, they find that they have well-designed controls for most threat vectors, but they do find a gap in one of the data cleanup tasks that happens after Azure Spark jobs are complete and found two insider threat vectors for data exfiltration.

These gaps are scheduled for remediation in the next development cycle.

The team also finds a legacy system used by a race team no longer using the service, which has significant access to race telemetry. Part of the remediation will be to decommission this system.

## Independently verify your controls
Run periodic security tests that are conducted by experts external to the workload team who attempt to ethically hack the system. Perform routine and integrated vulnerability scanning to detect exploits in infrastructure, dependencies, and application code.

These tests enable you to validate security defenses by simulating real-world attacks by using techniques like penetration testing.

Threats can be introduced as part of your change management. Integrating scanners into the deployment pipelines enables you to automatically detect vulnerabilities and even quarantine usage until the vulnerabilities are removed.

### Contoso's challenge

The threat modeling exercise helped the team uncover security gaps and they're now interested in validating their controls, especially after implementing their remediation.

The team has experimented with open source tools in the past to test their security, and found the exercise fun and educational. However, they and the stakeholders would like to bring in security professionals to perform thorough and rigorous testing regularly.

### Applying the approach and outcomes

The team engages with a well-known Microsoft partner specializing in cloud security to discuss penetration testing.

The workload team signs a Statement of Work for quarterly penetration testing service, mixing in one white-box test per year to ensure higher confidence.

The consulting team also helps the dev team get antimalware installed on dev boxes and the self-hosted build agents.

These measures give the workload team and the stakeholders a high degree of confidence that they'll be prepared for evolving threats moving forward.

## Get current, and stay current
Stay current on updates, patching, and security fixes. Continuously evaluate the system and improve it based on audit reports, benchmarking, and lessons from testing activities. Consider automation, as appropriate. Use threat intelligence powered by security analytics for dynamic detection of threats. At regular intervals, review the workload's conformance to Security Development Lifecycle (SDL) best practices.

By adopting this approach, you'll be able to ensure that your security posture doesn't degrade over time. By integrating findings from real-world attacks and testing activities, you'll be able to combat attackers who continuously improve and exploit new categories of vulnerabilities. Automation of repetitive tasks decreases the chance of human error that can create risk.

SDL reviews bring clarity around security features. SDL can help you maintain an inventory of workload assets and their security reports, which cover origin, usage, operational weaknesses, and other factors.

### Contoso's challenge

The developers responsible for writing the Apache Spark jobs are hesitant to introduce changes and generally take a "if it's not broken, don't fix it" approach to the jobs. This means that the Python and R packages they bring into the solution are likely to get stale over time.

### Applying the approach and outcomes

After the workload team reviews internal processes, they see that there's a risk of unpatched components being in the workload if the process for maintaining the Spark jobs isn't addressed.

The teams adopt a new standard for the Apache jobs that requires that all technologies in use must be updated along with their regularly recurring update and patch schedules.

By addressing this gap in security controls, the workload as a whole is less likely to be at risk of unpatched components. Their use of PaaS and SaaS services also helps limit their exposure to this risk as they don't have to patch underlying infrastructure.

## Check your knowledge

### 1. What type of exercise can help you identify gaps in your security controls?

- Failure mode analysis
- Health modeling
- Intrusion detection and prevention
- **✅ Threat modeling**

**Explanation:** Threat modeling is specifically designed to analyze each component of your workflow and evaluate potential threats that each component could be subject to. As described in the module, it helps identify gaps in security controls and produces a report of attack vectors prioritized by their severity level.

### 2. True or false: the workload team should handle all security testing.

- True
- **✅ False**

**Explanation:** False. The module emphasizes the importance of independent verification through external experts. It states that security tests should be "conducted by experts external to the workload team who attempt to ethically hack the system" and mentions the value of bringing in security professionals for thorough and rigorous testing.

### 3. In what way was Contoso at risk with their old process for their Apache Spark jobs?

- The jobs were not being monitored for successful runs.
- The jobs were automatically run over night when no one was able to monitor them.
- **✅ The jobs weren't included in the update and patching process.**
- The jobs were not being monitored for failed runs.

**Explanation:** The module describes that developers took a "if it's not broken, don't fix it" approach to the Spark jobs, meaning the Python and R packages would get stale over time. This created a risk of unpatched components being in the workload, which the team addressed by adopting new standards requiring all technologies to be updated along with regular patch schedules.



# 1.7 Summary

In this module, you've looked at the five key principles of the Security pillar of the Azure Well-Architected Framework.

A Well-Architected workload must be built with a zero-trust approach. A secure workload is resilient to attacks and incorporates the interrelated security principles of confidentiality, integrity, and availability (also known as the CIA triad) in addition to meeting business goals. Any security incident has the potential to become a major breach that damages the brand and reputation of the workload or organization.

As you design your system, use the Microsoft Zero Trust model as the compass to mitigate security risks:

* **Verify explicitly** so that only trusted identities perform intended and allowed actions that originate from expected locations. This safeguard makes it harder for attackers to impersonate legitimate users and accounts.
* **Use least-privilege access** for the right identities, with the right set of permissions, for the right duration, and to the right assets. Limiting permissions helps keep attackers from abusing permissions that legitimate users don't even need.
* **Assume breach** of security controls and design compensating controls that limit risk and damage if a primary layer of defense fails. Doing so helps you to defend your workload better by thinking like an attacker who's interested in success (regardless of how they get it).

## Learn more

To learn more about workload security, review the following documentation:

* Security design principles
* Design review checklist for Security
* Cost Optimization tradeoffs
* Cloud design patterns that support security



# 2 Introduction to Azure DevOps

Explore what DevOps is (and isn't) and learn how to get started with Azure DevOps.


# 2.1 Introduction

Azure DevOps can help your team release code in a more efficient, cooperative, and stable manner.

In the previous module, you met the team at Tailspin Toys. They're working on a new game, but their release process has several problems that affect their ability to deliver quality products to their customers. The team knows they need to change, but they don't know how.

The newest team member, Mara, believes DevOps will help. Her goal is to convince her teammates. She'll explain more about the value stream mapping (VSM) exercise she started in the previous module. Hopefully, her explanation will show the team why DevOps is the way forward.

Let's rejoin the team as they learn about DevOps. Together, we'll discover what it takes to get an Azure DevOps practice started.

## Learning objectives

After completing this module, you'll be able to:

* Identify what separates elite performers from low performers.
* List what services Azure DevOps provides.
* Create an Azure DevOps organization.

## Prerequisites

The modules in this learning path form a progression. We recommend that you start at the beginning of the Get started with Azure DevOps learning path before you start this module.

## Meet the team

You met the *Space Game* web team at Tailspin Toys in the previous module. As a refresher, here's who you'll work with in this module:

**Andy** is the development lead.

**Amita** is in QA.

**Tim** is in operations.

**Mara** just joined as a developer and reports to Andy.

Mara has prior experience with DevOps and is helping the team adopt a more streamlined process by using Azure DevOps.



# 2.2 What is DevOps?

DevOps is the union of people, process, and products to enable continuous delivery of value to our customers. However, what exactly does that mean? Let's join the team as Mara explains what DevOps is, what it isn't, and what makes elite performers successful.

Mara has called a short meeting with her teammates. Everyone has shown up, but no one wants to be there. She's put a box of donuts on the table.

**Mara:** Hi, thanks for coming. I wanted to talk more about our value stream map and how we can make our processes more efficient.

Mara's value stream map is still on the whiteboard from their previous meeting:

Screenshot of a whiteboard showing the value stream map.

**Mara:** Our value stream map shows where we lose efficiency in delivering value to our end users. Just like everyone else, we can improve, and we can decide which areas to tackle first.

**Andy:** This shows us where we have problems, but not what to do about them.

**Mara:** Right, it's an exercise that helps point us in the right direction. As for what to do about our problems, I think DevOps can help us. At my last company, our deployment rates went way up, lead times were faster, and operations had far fewer incidents. It took us a while to get there, but it was worth it. DevOps isn't a quick fix.

**Tim:** I know someone who just got a job as a DevOps engineer. I think it's more for developers. That sounds like you, Andy.

**Mara:** DevOps isn't a job title.

**Amita:** Is there any software program we can get that can help us along, or a template? Maybe there's a DevOps spreadsheet.

**Mara:** DevOps isn't a piece of software.

**Andy:** It's more like a methodology.

**Mara:** Not really.

**Andy, Amita, Tim:** So what is it?!

**Mara:** Here's the definition I like to use:

DevOps is the union of people, process, and products to enable continuous delivery of value to our end users.

In fact, Abel Wang, a Cloud Advocate at Microsoft, has a great set of videos with quick answers to some of our questions. Let's see how Abel defines DevOps:

## Ask Abel

Our goal is to give our customers games they'll love. We do that by working together with a shared set of practices and tools.

**Amita:** What does that mean? What shared practices? What shared tools?

**Mara:** Here's what I mean by practices:

**Agile planning:** Together, we'll create a backlog of work that everyone on the team and in management can see. We'll prioritize the items so we know what we need to work on first. The backlog can include user stories, bugs, and any other information that helps us.

**Continuous integration (CI):** We'll automate how we build and test our code. We'll run that every time a team member commits changes to version control.

**Continuous delivery (CD):** CD is how we test, configure, and deploy from a build to a QA or production environment.

**Monitoring:** We'll use telemetry to get information about an application's performance and usage patterns. We can use that information to improve as we iterate.

**Amita:** I don't know about automated testing. My tests are manual and I do them after Andy hands off the code to me. I don't have time to change how I do everything.

**Tim:** There's no way I'm letting any of you deploy to production.

**Andy:** This will scare management. They never think further than the next release and they always want it yesterday.

**Mara:** I know what you mean about management. I put together this handout about what makes an elite performing team.

## What makes an elite performing team?
Here's the handout that Mara prepared. The information is based on DevOps research reports and surveys conducted with technical professionals worldwide.

DevOps helps companies experiment with ways to increase customer adoption and satisfaction. It can lead to better organizational performance, and often to higher profitability and market share.

It uses metrics to create four categories by which to compare elite performers with low performers.

Elite performers:

### Deploy more frequently

In fact, some teams deploy up to dozens of times per day.

Practices such as monitoring, continuous testing, database change management, and integrating security earlier in the software-development process help elite performers deploy more frequently, and with greater predictability and security.

### Reduce lead time from commit to deploy

Lead time is the time it takes for a feature to make it to the customer. By working in smaller batches, automating manual processes, and deploying more frequently, elite performers can achieve in hours or days what once took weeks or even months.

### Reduce change failure rate

A new feature that fails in production or that causes other features to break can create a lost opportunity between you and your users. As high-performing teams mature, they reduce their change failure rate over time.

### Recover from incidents more quickly

When incidents do occur, elite performers are able to recover more quickly. Acting on metrics helps elite performers recover more quickly while also deploying more frequently.

How you implement cloud infrastructure also matters. The cloud improves software delivery performance, and teams that adopt essential cloud characteristics are more likely to become elite performers.

Outsourcing can save money and provide a flexible labor pool, but you must use it in the correct areas. Low-performing teams are more likely to outsource whole functions (like testing and operations) than their high-performing counterparts.

## The bottom line
DevOps is a key reason many elite performers are able to deliver value to customers in the form of new features and improvements, more quickly than their competitors. In this short video, Abel explains why you should learn more about DevOps:

## Ask Abel

## What DevOps isn't
When considering what DevOps is, it's also important to make sure we learn what it's not. DevOps isn't:

* A methodology.
* A specific piece of software.
* A quick fix for an organization's challenges.
* Just a team or a job title (although these titles are reasonably common in the industry).


# 2.3 What is Azure DevOps?

Azure DevOps provides several tools you can use for better team collaboration. It also has tools for automated build processes, testing, version control, and package management. That's quite a bit to cover! We'll get to all the tools eventually. For now, let's follow the team as they begin with an overview of what Azure DevOps is and how they can get started.

**Mara:** Amita asked about tools, and I'm proposing we use Azure DevOps.

**Andy:** How can we use something for Azure if we're not deploying to the cloud? Plus, we deploy to Linux. Does that matter?

**Mara:** These tools are great whether you're in the cloud or on-premises. It also doesn't matter if we're deploying to Linux or Windows or another platform. Azure DevOps is a suite of services that provides a solution for anyone who wants an enterprise-grade tool chain. Those tools help us implement all the practices we just talked about. Here's what you get:

**Expand table**

| Service | Description |
|---------|-------------|
| Azure Boards | These are agile tools that help us plan, track, and discuss our work, even with other teams. |
| Azure Pipelines | These will let us build, test, and deploy with CI/CD that works with any language, platform, and cloud. |
| Azure Test Plans | These are manual and exploratory testing tools. |

Those are the three I was thinking about using right now. There are two other services we can think about later:

**Expand table**

| Service | Description |
|---------|-------------|
| Azure Repos | These provide unlimited, cloud-hosted private, and public Git repos. |
| Azure Artifacts | These let us create, host, and share packages. |

## Ask Abel

Here's a short video where Abel explains the five parts of Azure DevOps:

**Amita:** This sounds like a lot. Where do we start?

**Mara:** Let's just try to do some planning by using Azure Boards. We'll see how that goes. You don't have to use every service Azure DevOps offers. You just use what you need.

**Tim:** What do we have to do?

**Mara:** It's easy. All we do is set up an account and an organization. The whole process only takes a couple of minutes.

## Check your knowledge

### 1.
**What is DevOps?**

- A job title for QA engineers
- **✅ The union of people, process, and products to enable continuous delivery of value to our customers**
- A methodology that teams implement quickly to solve all their challenges

**Explanation:** DevOps is defined as "the union of people, process, and products to enable continuous delivery of value to our customers." It's not a job title or a quick-fix methodology, but rather a cultural and operational approach to software development and delivery.

### 2.
**DevOps is:**

- **✅ A gradual process**
- Only for startups
- A piece of specialized software

**Explanation:** DevOps is a gradual process that takes time to implement and mature. As mentioned in the previous module, "DevOps isn't a quick fix" and "It took us a while to get there, but it was worth it." It's not limited to startups and isn't a single piece of software.

### 3.
**Azure DevOps is:**

- Meant for teams that deploy to Azure
- **✅ A suite of services that provide an end-to-end tool chain**
- A DevOps course offered by Microsoft

**Explanation:** Azure DevOps is a suite of services that provides an end-to-end tool chain for software development and delivery. As Mara explained, "These tools are great whether you're in the cloud or on-premises" and work with any language, platform, and cloud - not just Azure deployments.


# 2.4 Exercise - Create an Azure DevOps organization

Microsoft provides free Azure DevOps accounts for individuals, small teams, and open-source projects. Enterprises can also sign up for Azure DevOps accounts that can scale to thousands of team members. We're going to sign up for a free Azure DevOps organization to see how its services can help us on our DevOps journey.

**Note**

In this learning path, you'll use Azure DevOps Services, which Microsoft hosts for you. There's also **Azure DevOps Server**, the on-premises version of Azure DevOps Services that you can install and run on your own network.

## Create an Azure DevOps organization

Follow along with the team by setting up your own free Azure DevOps organization:

1. Go to dev.azure.com.

2. Sign in by using your **Microsoft account**; or if you don't have a Microsoft account, select **Create One!** and finish the steps.

**Note**

You might have a Microsoft account already. Typically, these end with hotmail.com or outlook.com.

3. Review the Terms of Service, Privacy Statement, and Code of Conduct, and select **Continue** if you agree to them.

**Note**

As the person creating the Azure DevOps organization, you'll automatically become the owner. Please be considerate when deciding on your account name and avoid existing legal entities.

## Create an organization

Next, set up an organization. Here's how:

1. If you've never created an Azure DevOps organization, you'll see a window with a **Create new organization** button. If you have, you'll see a link that reads **New organization**. Select the option you see.

2. In the **Azure DevOps Terms of Service and Privacy notification** window, select **Continue**.

3. Create an organization for the Microsoft Learn modules next to the **dev.azure.com/** field. If you're prompted that the name is already taken, just add some numbers to the end to make it unique; for example, *Tailspin0523*.

4. Choose a location near you where your projects will be hosted.

5. Complete the captcha.

6. Select **Continue**.

The next screen prompts you to create a project. You'll do that in the next module.

Congratulations! In the next module, the team will use Azure Boards to create its first project and backlog.


# 2.5 Summary

In this module, you learned about what DevOps is (and what it's *not*) and about the Microsoft DevOps suite, Azure DevOps. You also set up an account in Azure DevOps and created an organization.

In a comparison between elite performers and low performers, elite performers deploy more frequently, more quickly, and with fewer failures. This mindset helps them better adapt to changing market conditions, experiment with new features, and recover from incidents with greater resiliency. DevOps gives you a path to become an elite performer.

Even for elite performers, change happens gradually, often starting with the most immediate challenges or pain points. Adopting DevOps practices takes time.

## Learn more

We'll go deeper into Azure DevOps in future modules. You can also check out these resources:

* What is DevOps?
* How Microsoft plans with DevOps
* What features and services do I get with Azure DevOps?

