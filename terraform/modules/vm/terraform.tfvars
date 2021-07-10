# Resource Group/Location
location                = "East US"
resource_group          = "quality-releases-rg"
application_type        = "quality-releases"

# Virtual Machine
vm_size                 = "Standard_B1s"
vm_admin_username       = "user"

# Network
public_ip_address_id    = "/subscriptions/79f93199-ea71-4fc7-a0c1-a0f75c5ea7e1/resourceGroups/quality-releases-rg/providers/Microsoft.Network/publicIPAddresses/quality-releases-publicip"
subnet_id               = "/subscriptions/79f93199-ea71-4fc7-a0c1-a0f75c5ea7e1/resourceGroups/quality-releases-rg/providers/Microsoft.Network/virtualNetworks/quality-releases-NET-subnet1"
