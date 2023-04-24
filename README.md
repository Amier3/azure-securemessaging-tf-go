# Tutorial: Secure messaging with Azure and Terraform 

## Introduction

[Azure Service Bus](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview) is a cloud-managed message broker that offers developers a powerful tool for creating decoupled applications. Leveraging Service Bus can unlock various use cases, such as:

- Transferring business data across applications
- Load balancing among worker processes
- Breaking down monolithic applications while maintaining interconnectedness through publish/subscribe systems

While Azure Service Bus is an incredibly powerful tool, it communicates over HTTPS by default. This can raise regulatory and ethical concerns for developers who need to transfer personally identifiable or regulated data between applications. Fortunately, Azure provides the tools to set up messaging between applications over a private network that you control. In this tutorial, we'll explore how to establish secure messaging using Azure Service Bus and private endpoints.

## Architecture 

The following diagram depicts the private network you'll create as you complete the tutorial: 

![diagram](media/diagram%20.jpeg)

In the diagram, a VPC holds a subnet that contains a virtual machine. Two scripts running inside the VM represent different applications sending and receiving messages. Although the applications themselves can access internet, they connect securely through a private endpoint to the Azure Service Bus. The Service Bus is disconnected from internet and can only be reached through the endpoint.

## Intended Audience 

This tutorial is tailored for developers, cloud/platform engineers, and IT professionals who possess familiarity with the following concepts:

- Azure and its common services
- Private networks, subnets, virtual machines, and messaging systems
- Basic Python scripting 
- Command line navigation
- [Terraform and Infrastructure as Code (IAC) Concepts](https://developer.hashicorp.com/terraform/intro)

## Learning Objectives

By the end of this tutorial, you'll:

- Understand the concepts of secure messaging through private endpoints in Azure, and their advantages over default messaging sent over HTTPS.
- Learn how to use Terraform to create and manage Azure Service Bus resources and related messaging services.
- Learn how Python applications can publish and receive messages in an Azure Service Bus

## Before You Begin 

Before you start, you'll need:

- An Azure account with an active subscription that has the permission to create Compute, Networking, and Service Bus resources. 
- The ability to SSH into a remote server 
- This repository cloned onto your local machine 
- A code editor ( vim is fine! )
- Terraform version >= 1.4.5
  - For Terraform install instructions, see [Install Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- Azure CLI version >= 2.47.0
  - Ensure the azure cli is logged in and configured to your subscription via service principal. For more information, see [Authenticate Terraform to Azure](https://learn.microsoft.com/en-us/azure/developer/terraform/authenticate-to-azure?tabs=bash)

## Now what?

Now you're ready to start the lab, which should take approximately 10 minutes. Click [here](/lab/1-Terraform-Setup.md) to start the tutorial or navigate to `/lab` and start working your way the numbered sections. Enjoy! 



