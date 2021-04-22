# Azure GUIDS
variable "subscription_id" {
    default = "ba125c39-a888-44aa-a026-4c430b1ce555"
}
variable "client_id" {
    default = "08a1beff-6683-4682-a6fe-24d151ffd083"
}
variable "client_secret" {
    default = "8r~1Jyhdm7x59Bc1AqVwB.eJXOchbldyrk"
}
variable "tenant_id" {
    default = "ae5dc272-d68b-4a82-85a8-5b1b8efe5393"
}

# Resource Group/Location
variable "location" {
    default = "East US"
}
variable "application_type" {
    default = "quality-releases"
}
variable "resource_type" {
    default = "azure-appservice"
}
variable "resource_group" {
    default = "quality-releases-rg"
}
