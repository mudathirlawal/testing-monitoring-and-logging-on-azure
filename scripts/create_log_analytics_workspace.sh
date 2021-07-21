#!/bin/bash

# Use the following microsoft walkthrough: 
# https://docs.microsoft.com/en-us/azure/azure-monitor/logs/quick-create-workspace-cli

az deployment group create --resource-group <my-resource-group> \
    --name <my-deployment-name> \
    --template-file deploylaworkspacetemplate.json
