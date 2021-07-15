# terraform {
#   required_providers {
#     azurerm = {
#       source  = "hashicorp/azurerm"
#       version = "=2.66.0"
#     }
#   }
# }
# terraform {  
#   backend "azurerm" {
#     # storage_account_name = "tstate1096"
#     # container_name       = "tstate"
#     # key                  = "terraform.tfstate"
#   }
# }
# provider "azurerm" {
#   # tenant_id       = var.tenant_id
#   # subscription_id = var.subscription_id
#   # client_id       = var.client_id
#   # client_secret   = var.client_secret
#   # features {}
# }
resource "azurerm_network_interface" "test" {
  name                = "${var.application_type}-${var.resource_type}-nic"
  location            = var.location
  resource_group_name = var.resource_group

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    public_ip_address_id          = var.public_ip_address_id
    private_ip_address_allocation = "Dynamic"
  }
}

resource "azurerm_linux_virtual_machine" "test" {
  name                  = "${var.application_type}-${var.resource_type}"
  location              = var.location
  resource_group_name   = var.resource_group
  size                  = "Standard_B1s"
  admin_username        = var.vm_admin_username
  network_interface_ids = [azurerm_network_interface.test.id]
  admin_ssh_key {
    username   = var.vm_admin_username
    # public_key = file("~/.ssh/id_rsa.pub")
    public_key = file("/home/azureuser/myagent/_work/_temp/id_rsa.pub")
  }
  
  os_disk {
    caching = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "16.04-LTS"
    version   = "latest"
  }
}
