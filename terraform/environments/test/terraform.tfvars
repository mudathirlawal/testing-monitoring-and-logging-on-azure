# Azure subscription vars
subscription_id = "10fb07bc-4e3e-4785-b8a8-8129a3fa9385"
client_id       = "2a45b22f-7cfb-4543-804d-44e4c60f404d"
client_secret   = "RW7ke8dklcNZJJvM8TZvgfv-jG_7Y__D0L"
tenant_id       = "0dba3d0a-e527-4136-a298-071e8cac8109"
# access_key      = "KRzhEFskmKkdNYUnJkA7LtgiJ7DtZ/ZQYoZBEkxySwAYuQ3oKFaf9gKqs6blDbfzsOvxIKCgg1YTN5EZs95XLw=="

# Terraform variables
storage_account_name = "tstate19040"
container_name       = "tstate"
key                  = "terraform.tfstate"

# Resource Group/Location
location = "East US"
resource_group = "proj-capstone-rg"
application_type = "capstone-app"

# Network
virtual_network_name = "proj-capstone-vnet"
address_space = ["10.5.0.0/16"]
address_prefix_test = "10.5.1.0/24"

# Tags
tier = "Test"
deployment = "Terraform"