
 # Secure Azure services and workloads with Microsoft Defender for Cloud regulatory compliance controls
 
 https://learn.microsoft.com/en-us/training/paths/secure-azure-services-workloads-defender-cloud/

 
 
This learning path guides you in securing Azure services and workloads using Microsoft Cloud Security Benchmark controls in Microsoft Defender for Cloud via the Azure portal. 

### Prerequisites
 - None


# 1 Examine Defender for Cloud regulatory compliance standards

In this module, we will focus on using Microsoft Defender for Cloud to streamline regulatory compliance by identifying and addressing issues that hinder meeting compliance standards and certifications.


# 1.1 Introduction

This module covers regulatory compliance standards in Microsoft Defender for Cloud, teaching you to manage, implement, and report compliance controls, ensuring your cloud environment meets various regulatory requirements efficiently and securely.

## Scenario

Imagine your work as an IT Security Manager at a multinational corporation. You must ensure cloud deployments comply with various regulatory requirements. Learn to leverage Microsoft Defender for Cloud to manage compliance controls, address key standards, and maintain a secure, compliant cloud environment globally.

## Learning objectives

By the end of this training module, participants will:

* Understand how to use Microsoft Defender for Cloud's compliance management dashboard.
* Identify and interpret key regulatory compliance standards applicable to your industry.
* Implement and manage compliance controls within Microsoft Defender for Cloud.
* Conduct regular compliance assessments and generate comprehensive compliance reports.

## Goals

By the end of this module, you will be able to use Microsoft Defender for Cloud to streamline the regulatory compliance process, understand how to view and interpret compliance standards, and take steps to remediate any identified compliance concerns.



# 1.2 Regulatory compliance standards in Defender for Cloud

Microsoft Defender for Cloud streamlines the regulatory compliance process by helping you to identify issues that are preventing you from meeting a particular compliance standard, or achieving compliance certification.

Industry standards, regulatory standards, and benchmarks are represented in Defender for Cloud as security standards, and appear in the **Regulatory compliance dashboard**.

## Compliance controls

Each security standard consists of multiple compliance controls, which are logical groups of related security recommendations.

Defender for Cloud continually assesses the environment-in-scope against any compliance controls that can be automatically assessed. Based on assessments, it shows resources as being compliant or non-compliant with controls.

> **Note**
> 
> It's important to note that if standards have compliance controls that can't be automatically assessed, Defender for Cloud isn't able to decide whether a resource complies with the control. In this case, the control will show as greyed out.

## Viewing compliance standards

The **Regulatory compliance dashboard** provides an interactive overview of compliance state.

![Screenshot showing an example of the regulatory compliance dashboard in Microsoft Defender for Cloud.](https://learn.microsoft.com/en-us/training/wwl-azure/regulatory-compliance-standards/media/regulatory-compliance-dashboard.png)

In the dashboard you can:

- Get a summary of standards controls that have been passed.
- Get of summary of standards that have the lowest pass rate for resources.
- Review standards that are applied within the selected scope.
- Review assessments for compliance controls within each applied standard.
- Get a summary report for a specific standard.
- Manage compliance policies to see the standards assigned to a specific scope.
- Run a query to create a custom compliance report.
- Create a "compliance over time workbook" to track compliance status over time.
- Download audit reports.
- Review compliance offerings for Microsoft and third-party audits.

## Compliance standard details

For each compliance standard you can view:

- Scope for the standard.
- Each standard broken down into groups of controls and subcontrols.

When you apply a standard to a scope, you can see a summary of compliance assessment for resources within the scope, for each standard control.

The status of the assessments reflects compliance with the standard. There are three states:

- A **green circle** indicates that resources in scope are compliant with the control.
- A **red circle** indicates that resources are not compliant with the control.
- **Unavailable controls** are those that can't be automatically assessed and thus Defender for Cloud is unable to access whether resources are compliant.

You can drill down into controls to get information about resources that have passed/failed assessments, and for remediation steps.

## Default compliance standards

By default, when you enable Defender for Cloud, the following standards are enabled:

- **For Azure**: Microsoft Cloud Security Benchmark (MCSB).
- **For AWS**: Microsoft Cloud Security Benchmark (MCSB) and AWS Foundational Security Best Practices standard.
- **For GCP**: Microsoft Cloud Security Benchmark (MCSB) and GCP Default.

## Available compliance standards

The following standards are available in Defender for Cloud:

| Standards for Azure subscriptions | Standards for AWS accounts | Standards for GCP projects |
|-----------------------------------|----------------------------|----------------------------|
| Australian Government ISM Protected | AWS Foundational Security Best Practices | Brazilian General Personal Data Protection Law (LGPD) |
| Canada Federal PBMM | AWS Well-Architected Framework | California Consumer Privacy Act (CCPA) |
| CIS Azure Foundations | Brazilian General Personal Data Protection Law (LGPD) | CIS Controls |
| CMMC | California Consumer Privacy Act (CCPA) | CIS GCP Foundations |
| FedRAMP 'H' & 'M' | CIS AWS Foundations | CIS Google Cloud Platform Foundation Benchmark |
| HIPAA/HITRUST | CRI Profile | CIS Google Kubernetes Engine (GKE) Benchmark |
| ISO/IEC 27001 | CSA Cloud Controls Matrix (CCM) | CRI Profile |
| New Zealand ISM Restricted | | CSA Cloud Controls Matrix (CCM) |
| NIST SP 800-171 | ISO/IEC 27001 | Cybersecurity Maturity Model Certification (CMMC) |
| NIST SP 800-53 | ISO/IEC 27002 | FFIEC Cybersecurity Assessment Tool (CAT) |
| PCI DSS | NIST Cybersecurity Framework (CSF) | |
| RMIT Malaysia | NIST SP 800-172 | ISO/IEC 27001 |
| SOC 2 | PCI DSS | ISO/IEC 27002 |
| SWIFT CSP CSCF | | ISO/IEC 27017 |
| UK OFFICIAL and UK NHS | | NIST Cybersecurity Framework (CSF) |
| | | NIST SP 800-53 |
| | | NIST SP 800-171 |
| | | NIST SP 800-172 |
| | | PCI DSS |
| | | Sarbanes Oxley Act (SOX) |
| | | SOC 2 |

**Next unit**: Microsoft cloud security benchmark in Defender for Cloud


# 1.3 Microsoft cloud security benchmark in Defender for Cloud

Industry standards, regulatory standards, and benchmarks are represented in Microsoft Defender for Cloud as security standards. These standards are assigned to scopes such as Azure subscriptions, AWS accounts, and GCP projects.

Defender for Cloud continuously assesses your hybrid cloud environment against these standards, and provides information about compliance in the **Regulatory compliance dashboard**.

When you onboard subscriptions and accounts to Defender for Cloud, the **Microsoft cloud security benchmark (MCSB)** automatically starts to assess resources in scope.

This benchmark builds on the cloud security principles defined by the Microsoft Security Benchmark and applies these principles with detailed technical implementation guidance for Azure, for other cloud providers (such as AWS and GCP), and for other Microsoft clouds.

The compliance dashboard gives you a view of your overall compliance standing. Security for non-Azure platforms follows the same cloud-neutral security principles as Azure. Each control within the benchmark provides the same granularity and scope of technical guidance across Azure and other cloud resources.

From the compliance dashboard, you're able to manage all of your compliance requirements for your cloud deployments, including automatic, manual, and shared responsibilities.

> **Note**
> 
> Shared responsibilities are only compatible with Azure.



# 1.4 Improve your regulatory compliance in Defender for Cloud

Microsoft Defender for Cloud helps streamline the process for meeting regulatory compliance requirements, using the regulatory compliance dashboard. Defender for Cloud continuously assesses your hybrid cloud environment to analyze the risk factors according to the controls and best practices in the standards that you've applied to your subscriptions. The dashboard reflects the status of your compliance with these standards.

When you enable Defender for Cloud on an Azure subscription, the Microsoft cloud security benchmark is automatically assigned to that subscription. This widely respected benchmark builds on the controls from the Center for Internet Security (CIS), PCI-DSS and the National Institute of Standards and Technology (NIST) with a focus on cloud-centric security.

The regulatory compliance dashboard shows the status of all the assessments within your environment for your chosen standards and regulations. As you act on the recommendations and reduce risk factors in your environment, your compliance posture improves.

## Assess your regulatory compliance

The regulatory compliance dashboard shows your selected compliance standards with all their requirements, where supported requirements are mapped to applicable security assessments. The status of these assessments reflects your compliance with the standard.

Use the regulatory compliance dashboard to help focus your attention on the gaps in compliance with your chosen standards and regulations. This focused view also enables you to continuously monitor your compliance over time within dynamic cloud and hybrid environments.

The dashboard provides you with an overview of your compliance status and the set of supported compliance regulations. You'll see your overall compliance score, and the number of passing vs. failing assessments associated with each standard.

**Example: Microsoft Defender for Cloud - Regulatory compliance dashboard**

![Screenshot showing an example of the regulatory compliance dashboard and network security controls.](https://learn.microsoft.com/en-us/training/wwl-azure/regulatory-compliance-standards/media/regulatory-compliance-dashboard-network-security.png)

The following list has a numbered item that matches each location in the image above, and describes what is in the image:

1. **Select a compliance standard** to see a list of all controls for that standard.
2. **View the subscription(s)** that the compliance standard is applied on.
3. **Select a Control** to see more details. Expand the control to view the assessments associated with the selected control. Select an assessment to view the list of resources associated and the actions to remediate compliance concerns.
4. **Select Control details** to view Overview, Your Actions and Microsoft Actions tabs.
5. In the **Your Actions tab**, you can see the automated assessments associated to the control.

Automated assessments show the number of failed resources and resource types, and link you directly to the remediation experience to address those recommendations.

Recommendations give you suggestions on how to better secure your resources. You implement a recommendation by following the remediation steps provided in the recommendation.

> **Note**
> 
> Assessments run approximately every 12 hours, so you will see the impact on your compliance data only after the next run of the relevant assessment.

## Remediation steps

After reviewing all the recommendations, decide which one to remediate first. We recommend that you prioritize the security controls with the highest potential to increase your secure score.

1. From the list, select a recommendation.
2. Follow the instructions in the **Remediation steps** section. Each recommendation has its own set of instructions. The following screenshot shows remediation steps for configuring applications to only allow traffic over HTTPS.

![Screenshot showing an example of manual remediation steps for storage accounts.](https://learn.microsoft.com/en-us/training/wwl-azure/regulatory-compliance-standards/media/remediation-steps-storage-accounts.png)

## Remediate an automated assessment

The regulatory compliance has both automated and manual assessments that may need to be remediated. Using the information in the regulatory compliance dashboard, improve your compliance posture by resolving recommendations directly within the dashboard.

**To remediate an automated assessment:**

1. Sign in to the Azure portal.
2. Navigate to Defender for Cloud then click, **Regulatory compliance**.
3. Select a regulatory compliance standard.
4. Select a compliance control to expand it.
5. Select any of the failing assessments that appear in the dashboard to view the details for that recommendation. Each recommendation includes a set of remediation steps to resolve the issue.
6. Select a particular resource to view more details and resolve the recommendation for that resource. For example, in the Azure CIS 1.1.0 standard, select the recommendation **Disk encryption should be applied on virtual machines**.

![Screenshot showing an example of affected resources that require remediation.](https://learn.microsoft.com/en-us/training/wwl-azure/regulatory-compliance-standards/media/affected-resources-remediation.png)

In this example, when you select **Take action** from the recommendation details page, you arrive in the Azure Virtual Machine pages of the Azure portal, where you can enable encryption from the **Security** tab:

![Screenshot showing an example of a virtual machines disk setting.](https://learn.microsoft.com/en-us/training/wwl-azure/regulatory-compliance-standards/media/virtual-machine-disk-settings.png)

For more information about how to apply recommendations, see **Implementing security recommendations in Microsoft Defender for Cloud**.

After you take action to resolve recommendations, you'll see the result in the compliance dashboard report because your compliance score improves. Assessments run approximately every 12 hours, so you'll see the impact on your compliance data only after the next run of the relevant assessment.

## Remediate a manual assessment

The regulatory compliance has automated and manual assessments that may need to be remediated. Manual assessments are assessments that require input from the customer to remediate them.

**To remediate a manual assessment:**

1. Sign in to the Azure portal.
2. Navigate to Defender for Cloud then click, **Regulatory compliance**.
3. Select a regulatory compliance standard.
4. Select a compliance control to expand it.
5. Under the **Manual attestation and evidence** section, select an assessment.
6. Select the relevant subscriptions.
7. Select **Attest**.
8. Enter the relevant information and attach evidence for compliance.
9. Select **Save**.



# 1.5 Module assessment

Choose the best response for each of the questions below.

## Check your knowledge

### 1.
**A security analyst is tasked with improving the compliance posture of their hybrid cloud environment. They're using Microsoft Defender for Cloud's regulatory compliance dashboard to monitor the status of all assessments within the environment. How can they increase their overall compliance score?**

- By disabling the automated assessments.
- By ignoring the recommendations and focusing on manual assessments.
- **By acting on the recommendations and reducing risk factors in the environment.**

### 2.
**A system administrator is tasked with improving the compliance posture of their organization's Azure environment. They're using the regulatory compliance dashboard in Microsoft Defender for Cloud to resolve recommendations. What should they do to remediate an automated assessment?**

- Manually attest the compliance control and attach evidence for compliance.
- Wait for the next run of the relevant assessment to see the impact on compliance data.
- **Select a failing assessment from the dashboard, follow the provided remediation steps, and resolve the recommendation for a particular resource.**

### 3.
**A team is using Microsoft Defender for Cloud to continuously assess their hybrid cloud environment against security standards. They want to understand their overall compliance standing. What does the Regulatory Compliance dashboard provide?**

- It automatically starts to assess resources in scope when subscriptions and accounts are onboarded to Defender for Cloud.
- It provides a detailed technical implementation guidance for Azure, AWS and GCP.
- **It gives a view of the overall compliance standing.**

### 4.
**An IT Security Manager at a multinational corporation is tasked with ensuring cloud deployments comply with various regulatory requirements. They need to leverage Microsoft Defender for Cloud to manage compliance controls and maintain a secure, compliant cloud environment globally. What should they do to achieve this?**

- They should only rely on external audits for compliance assessments and reports.
- They should ignore the compliance management dashboard and manually check each component for compliance.
- **They should use Microsoft Defender for Cloud's compliance management dashboard, implement and manage compliance controls within it, and conduct regular compliance assessments and generate comprehensive compliance reports.**


# 1.6 Summary

In this module, you learned for using Microsoft Defender for Cloud to streamline regulatory compliance by managing compliance controls, identify standards, leveraging the compliance dashboard, and conduct assessments to generate detailed compliance reports.


