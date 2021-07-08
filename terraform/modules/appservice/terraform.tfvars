# Azure subscription vars
# subscription_id = "79f93199-ea71-4fc7-a0c1-a0f75c5ea7e1"
# client_id       = "cc696564-4afa-474a-8d3c-c41a8badaaaf"
# client_secret   = "tFoZxzMwom.L2xPSNE3Fy9zMn.YbWQA.m1"
# tenant_id       = "e9164a2c-aad6-42f3-8414-2ce4840890e9"

# Resource Group/Location
location = "East US"
resource_group = "quality-releases-rg"
application_type = "quality-releases"

# Network
virtual_network_name = "quality-releases-vnet"
address_space = ["10.5.0.0/16"]
address_prefix_test = "10.5.1.0/24"

# Terraform variables
key                  = "terraform.tfstate"
storage_account_name = "tstate1096"
container_name       = "tstate"

# Tags
# tier = "Test"
# deployment = "Terraform"
