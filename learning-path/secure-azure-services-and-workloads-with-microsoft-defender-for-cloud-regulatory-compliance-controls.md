
 # Secure Azure services and workloads with Microsoft Defender for Cloud regulatory compliance controls
 
 https://learn.microsoft.com/en-us/training/paths/secure-azure-services-workloads-defender-cloud/

 
 
This learning path guides you in securing Azure services and workloads using Microsoft Cloud Security Benchmark controls in Microsoft Defender for Cloud via the Azure portal. 

### Prerequisites
 - None


# 1 Examine Defender for Cloud regulatory compliance standards

In this module, we will focus on using Microsoft Defender for Cloud to streamline regulatory compliance by identifying and addressing issues that hinder meeting compliance standards and certifications.


# Introduction

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



# Regulatory compliance standards in Defender for Cloud

**Completed | 100 XP | 7 minutes**

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



