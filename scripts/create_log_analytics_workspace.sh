#!/bin/bash

# Use the following microsoft walkthrough: 
# https://docs.microsoft.com/en-us/azure/azure-monitor/logs/quick-create-workspace-cli

# GUIDE:
# az deployment group create --resource-group <my-resource-group> \
#     --name <my-deployment-name> \
#     --template-file deploylaworkspacetemplate.json

az deployment group create --resource-group qr-analytics-rg \
	--name QRWorkspaceTemplate \
	--template-file deployqrworkspacetemplate.json
