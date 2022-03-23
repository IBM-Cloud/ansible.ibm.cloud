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

# pylint: disable=missing-function-docstring


from ibm_cloud_sdk_core import ApiException

from ansible.module_utils.basic import AnsibleModule
# pylint: disable=line-too-long,fixme
from ibm_platform_services import ResourceManagerV2 # Todo: change this to external python package format

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: resource_manager_resource_groups_info
short_description: Manage resource_groups info.
author: IBM SDK Generator
version_added: "0.1"
description:
    - This module retrieves one or more resource_groups(s).
requirements:
    - "ResourceManagerV2"
options:
    date:
        description:
            - The date in the format of YYYY-MM which returns resource groups. Deleted resource groups will be excluded before this month.
        type: str
    default:
        description:
            - Boolean value to specify whether or not to list default resource groups.
        type: bool
    account_id:
        description:
            - The ID of the account that contains the resource groups that you want to get.
        type: str
    name:
        description:
            - The name of the resource group.
        type: str
    include_deleted:
        description:
            - Boolean value to specify whether or not to list default resource groups.
        type: bool
    id:
        description:
            - The short or long ID of the alias.
        type: str
'''

EXAMPLES = r'''
Examples coming soon.
'''

def run_module():
    module_args = dict(
        date=dict(
            type='str',
            required=False),
        default=dict(
            type='bool',
            required=False),
        account_id=dict(
            type='str',
            required=False),
        name=dict(
            type='str',
            required=False),
        include_deleted=dict(
            type='bool',
            required=False),
        id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    date = module.params["date"]
    default = module.params["default"]
    account_id = module.params["account_id"]
    name = module.params["name"]
    include_deleted = module.params["include_deleted"]
    id = module.params["id"]

    sdk = ResourceManagerV2.new_instance()

    if id:
        # read
        try:
            response = sdk.get_resource_group(
                id=id
            )
            module.exit_json(msg=response.get_result())
        except ApiException as ex:
            module.fail_json(msg=ex.message)

    # list
    try:
        response = sdk.list_resource_groups(
            account_id=account_id,
            date=date,
            name=name,
            default=default,
            include_deleted=include_deleted
        )
        module.exit_json(msg=response.get_result())
    except ApiException as ex:
        module.fail_json(msg=ex.message)

def main():
    run_module()

if __name__ == '__main__':
    main()
