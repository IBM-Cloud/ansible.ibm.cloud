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

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: ibm_resource_alias
short_description: Manage ibm_resource_alias resources.
author: IBM SDK Generator
version_added: "0.1"
description:
    - This module creates, updates, or deletes a ibm_resource_alias.
    - By default the module will look for an existing ibm_resource_alias.
requirements:
    - "ResourceControllerV2"
options:
    name:
        description:
            - The name of the alias. Must be 180 characters or less and cannot include any special characters other than `(space) - . _ :`.
        type: str
    source:
        description:
            - The ID of resource instance.
        type: str
    target:
        description:
            - The CRN of target name(space) in a specific environment, for example, space in Dallas YP, CFEE instance etc.
        type: str
    id:
        description:
            - The ID of the alias.
        type: str
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


from ansible.module_utils.basic import AnsibleModule
from ibm_cloud_sdk_core import ApiException
from ibm_platform_services import ResourceControllerV2

from ..module_utils.auth import get_authenticator


def run_module():
    module_args = dict(
        name=dict(
            type='str',
            required=False),
        source=dict(
            type='str',
            required=False),
        target=dict(
            type='str',
            required=False),
        id=dict(
            type='str',
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

    name = module.params["name"]
    source = module.params["source"]
    target = module.params["target"]
    id = module.params["id"]
    state = module.params["state"]

    authenticator = get_authenticator(service_name='resource_controller')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = ResourceControllerV2(
        authenticator=authenticator,
    )

    resource_exists=True

    # Check for existence
    if id:
        try:
            sdk.get_resource_alias(
                id=id,
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
                sdk.delete_resource_alias(
                    id=id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                payload = {"id": id , "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": id , "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.create_resource_alias(
                    name=name,
                    source=source,
                    target=target,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.update_resource_alias(
                    id=id,
                    name=name,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)


def main():
    run_module()


if __name__ == '__main__':
    main()