## Cleanup (~1 minute)

Using Terraform to create our infrastructure makes cleanup fairly simple. Exit from the VM. In `/terraform` , run the Terraform destroy command. When prompted, confirm the destroy. 

```
terraform destroy 
```

### Future Considerations

Once it's all destroyed, that's the end of the lab! There are several ways this lab could be enhanced, albeit at the expense of increased duration:

- Employing Azure AD managed identities for authenticating apps with the Service Bus, as opposed to connection strings. Connection strings can introduce vulnerabilities by requiring secrets to be stored in the code.
- Separating our applications into distinct machines or even utilizing serverless architectures with Azure Functions. With the current size of the applications, deploying them on virtual machines might be considered over-provisioning resources.
- Adopting a more consistent method for preparing the virtual machine for Python applications. This can be achieved with images in a virtual machine or by using runtimes in Azure Functions.
Refactoring the Terraform code to be more modular and standardized, utilizing common modules for resources such as VPCs, virtual machines, and subnets. Implementing standard variables.tf and provider.tf files would also improve the code's readability.