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
from ibm_platform_services import IamAccessGroupsV2 # Todo: change this to external python package format

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: iam_access_groups_iam_access_group_members
short_description: Manage iam_access_group_members resources.
author: IBM SDK Generator
version_added: "0.1"
description:
    - This module creates, updates, or deletes a iam_access_group_members.
    - By default the module will look for an existing iam_access_group_members.
requirements:
    - "IamAccessGroupsV2"
options:
    state:
        description:
            - Should the resource be present or absent.
        type: str
        default: present
        choices: [present, absent]
    members:
        description:
            - An array of member objects to add to an access group.
        type: list
    access_group_id:
        description:
            - The access group identifier.
        type: str
    iam_id:
        description:
            - The IAM identifier.
        type: str
    offset:
        description:
            - The offset of the first result item to be returned.
        type: int
    transaction_id:
        description:
            - An optional transaction ID can be passed to your request, which can be useful for tracking calls through multiple services by using one identifier. The header key must be set to Transaction-Id and the value is anything that you choose. If no transaction ID is passed in, then a random ID is generated.
        type: str
    limit:
        description:
            - Return up to this limit of results where limit is between 0 and 100.
        type: int
    sort:
        description:
            - If verbose is true, sort the results by id, name, or email.
        type: str
    type:
        description:
            - Filter the results by member type.
        type: str
    verbose:
        description:
            - Return user's email and name for each user ID or the name for each service ID or trusted profile.
        type: bool
'''

EXAMPLES = r'''
Examples coming soon.
'''

def run_module():
    module_args = dict(
        members=dict(
            type='list',
            required=False),
        access_group_id=dict(
            type='str',
            required=False),
        iam_id=dict(
            type='str',
            required=False),
        offset=dict(
            type='int',
            required=False),
        transaction_id=dict(
            type='str',
            required=False),
        limit=dict(
            type='int',
            required=False),
        sort=dict(
            type='str',
            required=False),
        type=dict(
            type='str',
            required=False),
        verbose=dict(
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

    members = module.params["members"]
    access_group_id = module.params["access_group_id"]
    iam_id = module.params["iam_id"]
    offset = module.params["offset"]
    transaction_id = module.params["transaction_id"]
    limit = module.params["limit"]
    sort = module.params["sort"]
    type = module.params["type"]
    verbose = module.params["verbose"]

    state = module.params["state"]

    sdk = IamAccessGroupsV2.new_instance()

    resource_exists=True

    # Check for existence
    if iam_id:
        try:
            sdk.list_access_group_members(
                access_group_id=access_group_id,
                transaction_id=transaction_id,
                limit=limit,
                offset=offset,
                type=type,
                verbose=verbose,
                sort=sort,
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
                sdk.remove_member_from_access_group(
                    access_group_id=access_group_id,
                    iam_id=iam_id,
                    transaction_id=transaction_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                payload = {"id": iam_id , "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": iam_id , "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.add_members_to_access_group(
                    access_group_id=access_group_id,
                    members=members,
                    transaction_id=transaction_id,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.add_members_to_access_group(
                    access_group_id=access_group_id,
                    members=members,
                    transaction_id=transaction_id,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)

def main():
    run_module()

if __name__ == '__main__':
    main()