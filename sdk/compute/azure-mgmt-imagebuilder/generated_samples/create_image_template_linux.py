# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.imagebuilder import ImageBuilderClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-imagebuilder
# USAGE
    python create_image_template_linux.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ImageBuilderClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscription-id}",
    )

    response = client.virtual_machine_image_templates.begin_create_or_update(
        resource_group_name="myResourceGroup",
        image_template_name="myImageTemplate",
        parameters={
            "identity": {
                "type": "UserAssigned",
                "userAssignedIdentities": {
                    "/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/rg1/providers/Microsoft.ManagedIdentity/userAssignedIdentities/identity_1": {}
                },
            },
            "location": "westus",
            "properties": {
                "customize": [
                    {
                        "name": "Shell Customizer Example",
                        "scriptUri": "https://example.com/path/to/script.sh",
                        "type": "Shell",
                    }
                ],
                "distribute": [
                    {
                        "artifactTags": {"tagName": "value"},
                        "imageId": "/subscriptions/{subscription-id}/resourceGroups/rg1/providers/Microsoft.Compute/images/image_it_1",
                        "location": "1_location",
                        "runOutputName": "image_it_pir_1",
                        "type": "ManagedImage",
                    }
                ],
                "source": {
                    "imageId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.Compute/images/source_image",
                    "type": "ManagedImage",
                },
                "vmProfile": {
                    "osDiskSizeGB": 64,
                    "vmSize": "Standard_D2s_v3",
                    "vnetConfig": {
                        "subnetId": "/subscriptions/{subscription-id}/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/vnet_name/subnets/subnet_name"
                    },
                },
            },
            "tags": {"imagetemplate_tag1": "IT_T1", "imagetemplate_tag2": "IT_T2"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/imagebuilder/resource-manager/Microsoft.VirtualMachineImages/stable/2022-07-01/examples/CreateImageTemplateLinux.json
if __name__ == "__main__":
    main()
