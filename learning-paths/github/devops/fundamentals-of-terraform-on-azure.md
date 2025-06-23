

# Fundamentals of Terraform on Azure
https://learn.microsoft.com/en-us/training/paths/terraform-fundamentals/

Terraform enables you to deploy Azure resources. Terraform uses a declarative syntax that you treat like application code. Treating your infrastructure as code enables you to track changes to your infrastructure requirements and makes your deployments more consistent and repeatable.

Terraform provides a concise syntax and type safety for your Azure infrastructure declarations.

Take this learning path to get started with Terraform. In it, you'll:
- Decide whether Terraform is the right choice for your deployments to Azure.
- Understand Terraform's declarative syntax and the structure of a Terraform module.
- Apply Terraform features such as variables, outputs, functions, and loops to control how your infrastructure is deployed.
- Define modules that break down complex deployments into smaller reusable components.
- Each module in this learning path provides examples for use with the Azure CLI. Visual Studio Code is used to write and validate your Terraform code.

#### Prerequisites
- Familiarity with Azure Resources and Azure resource groups is recommended, but not required.



# 1 Introduction to infrastructure as code using Terraform

Infrastructure as code can help you quickly and confidently scale your cloud deployments. By using Terraform, you can automate and simplify the provisioning of infrastructure resources.

#### Learning objectives
After completing this module, you'll be able to:
- Describe the benefits of infrastructure as code
- Describe the difference between declarative and imperative infrastructure as code
- Explain what Terraform is, and how it fits into an infrastructure-as-code approach

# 1.1 Introduction

Infrastructure as code, sometimes referred to as IaC, is a way to provision infrastructure resources that's similar to how software is deployed. These resources include virtual machines, virtual networks, and web applications. Infrastructure as code can help automate your deployments, increase confidence in your deployments, and increase efficiency and repeatability.

## Example scenario
Suppose you work as an Azure infrastructure administrator at a toy company that's experiencing significant growth in the global market. As a result, your infrastructure needs to scale with the company's growth, including:

- Deployments of new applications for internal teams and customers.
- Multiple region deployments to support your customers and partners around the world.
- Multiple environment deployments to ensure consistency.

Evaluate whether infrastructure as code might be a valuable approach to resource provisioning at your company. You also need to decide which technology to use when you deploy your Azure infrastructure.

## What we cover
This module covers the concepts of infrastructure as code and its benefits. The module covers the purpose of Terraform as an infrastructure as code language and understand how it works. The module answers these questions:

- What is infrastructure as code?
- Why infrastructure as code help you automate resource provisioning?
- What is Terraform and how does it work?
- Why should you use Terraform instead of other tooling options?

## What is the main goal

After completing this module, you'll be able to determine whether infrastructure as code is the right approach and tool for your organization.

#### Prerequisites
 You should be familiar with:
- Basic cloud computing concepts and terminology.
- Different types of cloud resources.


# 1.2 **What is infrastructure as code?**

Evaluate whether infrastructure as code might be a valuable approach to resource provisioning at your company. You're reviewing the available options for deployment, including:

* Azure portal
* Azure CLI
* Azure PowerShell
* Azure Resource Manager templates (JSON and Bicep)
* Terraform

You're looking for a repeatable option, and you need to decide which technology to use to deploy your Azure infrastructure.

This unit covers why infrastructure as code can help you deploy your Azure infrastructure in an automated and repeatable way.

Azure CLI commands are used to illustrate concepts. This unit covers using commands to deploy resources in other modules of the Terraform learning path.

## **Defining infrastructure as code**

Your company designs new toys for release to the market, and most new toys require some assembly after purchase. The company's design team creates instruction manuals to include with each toy. Each manual provides details about how to properly assemble the toy.

You can think of infrastructure as code as being like the instruction manual for your infrastructure. The manual details the end configuration of your resources and how to reach that configuration state.

Infrastructure as code is the process of automating your infrastructure provisioning. It uses a declarative coding language and versioning system that's similar to what's used for source code. When you create an application, your source code generates the same result on each compilation. In a similar manner, infrastructure-as-code deployments are automated, consistent, and repeatable. Infrastructure as code can automate the deployments of your resources. Such as virtual networks, virtual machines, applications, storage, and even GitHub repositories or user accounts.

![](https://learn.microsoft.com/en-us/training/modules/terraform-introduction-to-infrastructure-as-code/media/iac.svg)

*Diagram that shows the infrastructure as code process using a source code repository with a module that deploys Azure resources.*

If you recall the instruction manual for the new toy, there are multiple ways to write the instruction manual. One option is to detail each step of the build process. Another option is to show an exploded view of the pieces and parts needed to assemble the toy. This unit covers the differences between imperative and declarative code and how they relate to your company's instruction manuals.

## **Why use infrastructure as code?**

Adopting an infrastructure as code approach offers many benefits to resource provisioning. With infrastructure as code, you can:

* Increase confidence in your deployments.
* Manage multiple environments.
* Better understand your cloud resources.

### **Increase confidence**

One of the benefits of using infrastructure as code is the level of confidence you gain in your deployments from improvements in consistency and security.

**Integration with current processes:** If your organization already uses standard software development practices, you can adopt those same processes for your infrastructure deployments. For example, peer reviews and static analysis can help in detecting problems in configurations that might be difficult to detect when making manual changes.

**Consistency:** Adopting an infrastructure as code approach helps your team follow well-established processes to deploy infrastructure. By following these processes, responsibility shifts from a small group of individuals to your automation process and tooling. Infrastructure as code helps reduce human error in resource provisioning and ensure consistent deployments.

**Automated scanning:** Infrastructure as code scanning by automated tooling checks for errors in the code. Automated tooling can also review proposed changes to ensure that security and performance practices are followed.

**Secret management:** Many solutions require secrets, like connection strings, encryption keys, client secrets, and certificates. In Azure, an Azure Key Vault is the service that's used to securely store these secrets. Many infrastructure-as-code tools can integrate with Key Vault to access these secrets securely at deploy time. Or even better, do away with secrets altogether by using Workload identity federation and Managed identities.

**Access control:** With infrastructure as code deployments, you have the option of using managed identities or service accounts to automate resource provisioning. Blocking user access prevents incorrect configurations deployed to production. If necessary, you can override this process by using an emergency access account (often called a break glass account) or by using the Microsoft Entra ID Privileged Identity Management feature.

**Avoid configuration drift:** Idempotence is a term associated with infrastructure as code. When an operation is idempotent, it means that it provides the same result on each run. If you choose tooling that uses idempotent operations, you can avoid configuration drift.

As an example of idempotence, consider the following Azure CLI command. The command creates an Azure resource group named storage-resource-group in the East US region.

```bash
az group create \
  --name storage-resource-group \
  --location eastus
```

If you run this command a second time, you receive the exact same output because this Azure CLI command was designed to be idempotent. You don't receive an error or a duplicate resource group.

When you use infrastructure as code, you can redeploy your environment at each release of your solution. These releases might incorporate small configuration changes or even significant updates. This process helps avoid configuration drift. If an accidental change is made to a resource, it can be corrected by redeploying the configuration. By following this approach, you're documenting your environment by using code.

### **Manage multiple environments**

Many organizations maintain multiple application environments. The developers in your toy company might have multiple versions of application code staged in a repository for release to different environments. The environments might include development, testing, and production. Some organizations maintain multiple production environments for applications that are distributed globally. Other organizations, like independent software vendors (ISVs), maintain multiple tenant environments for their customers.

Here are some of the key ways infrastructure as code can help you manage your environments:

**Provision new environments:** One of the main benefits of cloud computing is the ability to scale. Infrastructure as code can help you scale to multiple instances of your application. These instances can help during times of increased load, or you can deploy them for users in other areas of the world. This agility also can be beneficial when you test your application, like during penetration testing, load testing, and bug testing. With a well-defined code base, you can dynamically provision these new environments in a consistent manner.

**Nonproduction environments:** A common problem organizations face is differentiation between production and nonproduction environments. When you manually provision resources in separate environments, it's possible that the end configurations don't match. An example is when you deploy a new feature to a nonproduction environment that differs from the production environment. It's possible that the new feature doesn't work as expected in the production environment because of the differences between the two environments. Using infrastructure as code can help minimize these problems. You can use the same configuration files for each environment but supply different input parameters to create uniqueness. You can also be cost efficient by tearing down nonproduction environments when they're not in use.

**Disaster recovery:** In some situations, infrastructure as code can be used as part of an organization's disaster recovery plan. For example, you might need to re-create your environment in another region because of a service outage. By using infrastructure as code, you can quickly provision a new instance to fail over to instead of manually deploying and reconfiguring everything.

### **Better understand your cloud resources**

Infrastructure as code can help you better understand the state of your cloud resources:

**Audit trail:** Changes to your infrastructure-as-code configurations are version controlled in the same way as your application source code. These changes are tracked in your tooling, like with Git's version history. This audit trail means that you can review the details of each change, who made the change, and when the change was made. If you're using a continuous delivery tool, you can also refer back to the detailed deployment logs and see exactly what happened on each update.

**Documentation:** You can use many infrastructure-as-code configurations to add metadata, like comments, which describe the purpose of the code in your configuration. If your organization already follows a code documentation process, consider adopting these same procedures with your infrastructure code.

**Unified system:** Many times, when a developer is working on a new feature, they must make changes to application code and infrastructure code. When you use a common system, your organization can better understand the relationship between your applications and your infrastructure.

**Better understanding of cloud infrastructure:** When you use the Azure portal to provision resources, many of the processes are abstracted from view. Infrastructure as code can help provide a better understanding of how Azure works and how to troubleshoot issues that might arise. For example, when you create a virtual machine by using the Azure portal, some created resources are abstracted from view. Managed disks and network interface cards are deployed behind the scenes. When you deploy the same virtual machine by using infrastructure as code, you have complete control over all resources that are created. With Terraform, you also have a state file that contains a wealth of information about your deployed resources that you can mine for information or use to detect drift.

## **Imperative and declarative code**

You can write an instruction manual for new toy assembly in different ways. When you automate the deployment of services and infrastructure, you can take two approaches: imperative and declarative.

With **imperative code**, you execute a sequence of commands, in a specific order, to reach an end configuration. This process defines what the code should accomplish, and it defines how to accomplish the task. The imperative approach is like a step-by-step instruction manual.

With **declarative code**, you specify only the end configuration. The code doesn't define how to accomplish the task. The declarative approach is like the exploded view instruction manual.

When you choose between using an imperative approach and a declarative approach to resource provisioning, consider the tools that might already be in use in your organization. Also consider which approach might match your own skills.

### **Imperative code**

In Azure, an imperative code approach is accomplished programmatically by using a scripting language like Bash or Azure PowerShell. The scripts execute a series of steps to create, modify, and even remove your resources.

This example shows two Azure CLI commands that create a resource group and a storage account.

```bash
#!/usr/bin/env bash
az group create \
  --name storage-resource-group \
  --location eastus

az storage account create \
  --name mystorageaccount \
  --resource-group storage-resource-group \
  --location eastus \
  --sku Standard_LRS \
  --kind StorageV2 \
  --access-tier Hot \
  --https-only true
```

The first command creates a resource group named storage-resource-group in the East US region. The second command creates a storage account named mystorageaccount in the storage-resource-group resource group that was created in the first command. The second command also configures some properties for the storage account, including the kind of storage account and its access tier.

You can use an imperative approach to fully automate resource provisioning, but the approach has some disadvantages. As your architecture matures, scripts can become complex to manage. Commands could be updated or deprecated, which requires reviews of existing scripts.

### **Declarative code**

In Azure, a declarative code approach is accomplished by using templates or modules. Many types are available to use, including:

* Terraform, by HashiCorp
* Bicep
* ARM JSON

> **Note**
> 
> This module focuses on using Terraform modules.

Take a look at the following example of a Terraform module that configures a storage account. The configuration of the storage account matches the Azure CLI example.

```hcl
resource "azurerm_resource_group" "example" {
  name     = "storage-resource-group"
  location = "eastus"
}

resource "azurerm_storage_account" "example" {
  name                      = "mystorageaccount"
  location                  = azurerm_resource_group.example.location
  resource_group_name       = azurerm_resource_group.example.name
  sku                       = "Standard"
  account_replication_type  = "GRS"
  account_kind              = "StorageV2"
  access_tier               = "Hot"
  enable_https_traffic_only = true
}
```

The resource blocks define the resource group and storage account configuration. The azurerm_storage_account block contains the name, location, and properties of the storage account, including its SKU and the kind of account.

You might notice that the Terraform module doesn't specify how to deploy the storage account. It specifies only what the storage account needs to look like. The steps taken to create or update this storage account are left for the Terraform CLI and the azurerm Terraform provider to decide.


# 1.3 **Compare Azure Resource Manager and Terraform State**

Your team knows the benefits of infrastructure as code and the different approaches that are available. Your company is growing at a rapid pace and your team will deploy a significant number of resources to Azure. Declarative infrastructure as code is the right approach to resource provisioning. The team doesn't want to maintain scripts that list every deployment step. Before beginning the process of building your first template, you need to understand how Azure Terraform and Azure Resource Manager works. Investigating the types of templates that are available to use with Azure will help you determine the next steps in your infrastructure-as-code strategy.

This unit covers the difference between Azure Resource Manager and Terraform state.

## **Azure Resource Manager vs Terraform state**

### **Azure Resource Manager**

Azure Resource Manager is the service that's used to deploy and manage resources in Azure with Bicep or ARM templates. You can use Resource Manager to create, update, and delete resources in your Azure subscription. It expects a declarative template that it translates into a set of idempotent commands to create or update your resources.

### **Terraform State**

Terraform state is a json based representation of the resources you're managing with Terraform. Terraform is an agnostic tool that can support anything with an API end point, therefore it requires an agnostic method to manage the lifecycle of resources under management. The state file essentially maps the resource declaration in your template to the ID of the resource in the target environment, in our case Azure.

## **Comparison of Azure Resource Manager and Terraform State**

| Item | Azure Resource Manager | Terraform State |
|------|------------------------|-----------------|
| **State file management** | Not required, state is stored in Microsoft Azure | State file must be stored and secured |
| **Support for other cloud providers and APIs** | Only works with Microsoft Azure and Microsoft Entra ID | Works with any cloud or API that has a provider built for it |
| **Lifecycle (create, update, delete)** | Deployment stacks now allow managing the full life cycle | Terraform is able to manage the full lifecycle |
| **Drift detection / plan** | What If allows checking for updates | Terraform plan enables drift detection and planning |



# 1.4 **What is Terraform?**

You use Terraform for your resource provisioning. You want to learn more about Terraform modules so that you can make an informed decision about which language to use.

This unit covers the Terraform language and the benefits it provides to module authoring.

## **Terraform language - HashiCorp Configuration Language (HCL)**

The language used by Terraform is called HashiCorp Configuration Language normally shortened to HCL. The HCL language is used in other HashiCorp tools, such as Packer, but is most widely known as the language of Terraform.

The HCL language is used to declaratively deploy Azure resources. HCL is a domain-specific language. A domain-specific language is designed for a specific scenario or *domain*. HCL isn't meant to be used as a standard programming language for writing applications. HCL is used only to create Terraform modules. Terraform is intended to be easy to understand and straightforward to learn, regardless of your experience with other programming languages. Any Azure resource type and properties can be specified in Terraform modules.

> **Note**
> 
> If you've previously looked into using ARM templates, you'll notice that Terraform simplifies the template creation experience. It provides a syntax that's easier to understand, better support for modularity and reusable code, and improved type safety. Creating a JSON ARM template requires complicated expressions, and the final result might be verbose.

## **Benefits of Terraform**

Terraform provides many improvements over ARM template authoring, including:

* **Simpler syntax**: Terraform provides a simpler syntax for writing modules. You can reference parameters and variables directly, without using complicated functions. String interpolation is used in place of concatenation to combine values for names and other items. You can reference the properties of a resource directly by using its symbolic name instead of complex reference statements.

* **Modules**: You can break down complex deployments into smaller submodules and reference them in a root module. These modules provide easier management and greater reusability. You can even share your modules with your team or publically.

* **Automatic dependency management**: In most situations, Terraform automatically detects dependencies between your resources. This process removes some of the work involved in module authoring.

* **Type validation and IntelliSense**: The Terraform extensions for Visual Studio Code feature rich validation and IntelliSense for all Azure resource types. This feature helps provide an easier authoring experience.

Take a look at the following example of a Terraform module that defines an Azure storage account. The name of the storage account is automatically generated in the module. After deployment, the resource ID is returned as output to the user who executes the module.

```hcl
variable "name_prefix" {
  type    = string
  default = "storage"
}

locals {
  storage_account_name             = "${var.name_prefix}${random_id.random_suffix.hex}"
  storage_account_replication_type = "RAGRS"
}

resource "random_id" "random_suffix" {
    byte_length = 4
}

resource "azurerm_resource_group" "example" {
  name     = "storage-resource-group"
  location = "eastus"
}

resource "azurerm_storage_account" "example" {
  name                      = local.storage_account_name
  location                  = azurerm_resource_group.example.location
  resource_group_name       = azurerm_resource_group.example.name
  sku                       = "Standard"
  account_replication_type  = local.storage_account_replication_type
  account_kind              = "StorageV2"
  access_tier               = "Hot"
  enable_https_traffic_only = true
}

output "storage_account_resource_id" {
  value = azurerm_storage_account.example.id
}
```


