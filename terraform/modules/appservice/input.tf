# Azure GUIDS
variable "subscription_id" {
    default = "10fb07bc-4e3e-4785-b8a8-8129a3fa9385"
}
variable "client_id" {
    default = "2a45b22f-7cfb-4543-804d-44e4c60f404d"
}
variable "client_secret" {
    default = "RW7ke8dklcNZJJvM8TZvgfv-jG_7Y__D0L"
}
variable "tenant_id" {
    default = "0dba3d0a-e527-4136-a298-071e8cac8109"
}

# # Terraform
# variable "access_key" {
#     default = "KRzhEFskmKkdNYUnJkA7LtgiJ7DtZ/ZQYoZBEkxySwAYuQ3oKFaf9gKqs6blDbfzsOvxIKCgg1YTN5EZs95XLw=="   
# }

# Resource Group/Location
variable "location" {
    default = "East US"
}

variable "application_type" {
    default = "capstone-appservice"
}
variable "resource_type" {
    default = "azure-appservice"
}

variable "resource_group" {
    default = "proj-capstone-rg"
}
