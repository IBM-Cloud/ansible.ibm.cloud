# coding: utf-8

# (C) Copyright IBM Corp. 2022.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=missing-function-docstring,too-many-branches


from ibm_cloud_sdk_core import ApiException

from ansible.module_utils.basic import AnsibleModule
# pylint: disable=line-too-long,fixme
from ansible.module_utils.cloud.ibm.ibm_cloud import SchematicsV1 # Todo: change this to external python package format

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: schematics_schematics_inventory
short_description: Manage schematics_inventory resources.
author: IBM SDK Generator
version_added: "0.1"
description:
    - This module creates, updates, or deletes a schematics_inventory.
    - By default the module will look for an existing schematics_inventory.
requirements:
    - "SchematicsV1"
options:
    inventories_ini:
        description:
            - Input inventory of host and host group for the playbook, in the `.ini` file format.
        type: str
    resource_group:
        description:
            - Resource-group name for the Inventory definition.   By default, Inventory definition will be created in Default Resource Group.
        type: str
    resource_queries:
        description:
            - Input resource query definitions that is used to dynamically generate the inventory of host and host group for the playbook.
        type: list
        elements: str
    name:
        description:
            - The unique name of your Inventory definition. The name can be up to 128 characters long and can include alphanumeric characters, spaces, dashes, and underscores.
        type: str
    description:
        description:
            - The description of your Inventory definition. The description can be up to 2048 characters long in size.
        type: str
    location:
        description:
            - List of locations supported by IBM Cloud Schematics service.  While creating your workspace or action, choose the right region, since it cannot be changed.  Note, this does not limit the location of the IBM Cloud resources, provisioned using Schematics.
        type: str
    inventory_id:
        description:
            - Resource Inventory Id.  Use `GET /v2/inventories` API to look up the Resource Inventory definition Ids  in your IBM Cloud account.
        type: str
    propagate:
        description:
            - Auto propagate the chaange or deletion to the dependent resources.
        type: bool
    force:
        description:
            - Equivalent to -force options in the command line.
        type: bool
    state:
        description:
            - Should the resource be present or absent.
        type: str
        default: present
        choices: [present, absent]
'''

EXAMPLES = r'''
Examples coming soon.
'''

def run_module():
    module_args = dict(
        inventories_ini=dict(
            type='str',
            required=False),
        resource_group=dict(
            type='str',
            required=False),
        resource_queries=dict(
            type='list',
            elements=str,
            required=False),
        name=dict(
            type='str',
            required=False),
        description=dict(
            type='str',
            required=False),
        location=dict(
            type='str',
            required=False),
        inventory_id=dict(
            type='str',
            required=False),
        propagate=dict(
            type='bool',
            required=False),
        force=dict(
            type='bool',
            required=False),
        state=dict(
            type='str',
            default='present',
            choices=['absent', 'present'],
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    inventories_ini = module.params["inventories_ini"]
    resource_group = module.params["resource_group"]
    resource_queries = module.params["resource_queries"]
    name = module.params["name"]
    description = module.params["description"]
    location = module.params["location"]
    inventory_id = module.params["inventory_id"]
    propagate = module.params["propagate"]
    force = module.params["force"]

    state = module.params["state"]

    sdk = SchematicsV1.new_instance()

    resource_exists=True

    # Check for existence
    if inventory_id:
        try:
            sdk.get_inventory(
                inventory_id=inventory_id,
            )
        except ApiException as ex:
            if ex.code == 404:
                resource_exists=False
            else:
                module.fail_json(msg=ex.message)
    else:
        # assume resource does not exist
        resource_exists=False

    # Delete path
    if state == "absent":
        if resource_exists:
            try:
                sdk.delete_inventory(
                    inventory_id=inventory_id,
                    force=force,
                    propagate=propagate,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                payload = {"id": inventory_id , "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": inventory_id , "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.create_inventory(
                    name=name,
                    description=description,
                    location=location,
                    resource_group=resource_group,
                    inventories_ini=inventories_ini,
                    resource_queries=resource_queries,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.update_inventory(
                    inventory_id=inventory_id,
                    name=name,
                    description=description,
                    location=location,
                    resource_group=resource_group,
                    inventories_ini=inventories_ini,
                    resource_queries=resource_queries,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)

def main():
    run_module()

if __name__ == '__main__':
    main()
