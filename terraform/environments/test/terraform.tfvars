# Azure subscription vars
subscription_id = "ba125c39-a888-44aa-a026-4c430b1ce555"
client_id       = "08a1beff-6683-4682-a6fe-24d151ffd083"
client_secret   = "8r~1Jyhdm7x59Bc1AqVwB.eJXOchbldyrk"
tenant_id       = "ae5dc272-d68b-4a82-85a8-5b1b8efe5393"

# Terraform variables
storage_account_name = "tstate24171"
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