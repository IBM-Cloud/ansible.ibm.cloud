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
module: ibm_iam_access_group_rule
short_description: Manage ibm_iam_access_group_rule resources.
author: IBM SDK Generator
version_added: "0.1"
description:
    - This module creates, updates, or deletes a ibm_iam_access_group_rule.
    - By default the module will look for an existing ibm_iam_access_group_rule.
requirements:
    - "IamAccessGroupsV2"
options:
    name:
        description:
            - The name of the rule.
        type: str
    expiration:
        description:
            - The number of hours that the rule lives for.
        type: int
    conditions:
        description:
            - A list of conditions the rule must satisfy.
        type: list
        suboptions:
            claim:
                description:
                    - The claim to evaluate against. This will be found in the `ext` claims of a user's login request.
                type: str
            operator:
                description:
                    - The operation to perform on the claim.
                type: str
            value:
                description:
                    - The stringified JSON value that the claim is compared to using the operator.
                type: str
    realm_name:
        description:
            - The url of the identity provider.
        type: str
    rule_id:
        description:
            - The rule to get.
        type: str
    access_group_id:
        description:
            - The access group identifier.
        type: str
    if_match:
        description:
            - The current revision number of the rule being updated. This can be found in the Get Rule response ETag header.
        type: str
    transaction_id:
        description:
            - An optional transaction ID can be passed to your request, which can be useful for tracking calls through multiple services by using one identifier. The header key must be set to Transaction-Id and the value is anything that you choose. If no transaction ID is passed in, then a random ID is generated.
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

def run_module():
    module_args = dict(
        name=dict(
            type='str',
            required=False),
        expiration=dict(
            type='int',
            required=False),
        conditions=dict(
            type='list',
            options=dict(
                claim=dict(
                    type='str',
                    required=False),
                operator=dict(
                    type='str',
                    required=False),
                value=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        realm_name=dict(
            type='str',
            required=False),
        rule_id=dict(
            type='str',
            required=False),
        access_group_id=dict(
            type='str',
            required=False),
        if_match=dict(
            type='str',
            required=False),
        transaction_id=dict(
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
    expiration = module.params["expiration"]
    conditions = module.params["conditions"]
    realm_name = module.params["realm_name"]
    rule_id = module.params["rule_id"]
    access_group_id = module.params["access_group_id"]
    if_match = module.params["if_match"]
    transaction_id = module.params["transaction_id"]
    state = module.params["state"]

    sdk = IamAccessGroupsV2.new_instance()

    resource_exists=True

    # Check for existence
    if rule_id:
        try:
            sdk.get_access_group_rule(
                access_group_id=access_group_id,
                rule_id=rule_id,
                transaction_id=transaction_id,
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
                sdk.remove_access_group_rule(
                    access_group_id=access_group_id,
                    rule_id=rule_id,
                    transaction_id=transaction_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                payload = {"id": rule_id , "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": rule_id , "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.add_access_group_rule(
                    access_group_id=access_group_id,
                    expiration=expiration,
                    realm_name=realm_name,
                    conditions=conditions,
                    name=name,
                    transaction_id=transaction_id,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.replace_access_group_rule(
                    access_group_id=access_group_id,
                    rule_id=rule_id,
                    if_match=if_match,
                    expiration=expiration,
                    realm_name=realm_name,
                    conditions=conditions,
                    name=name,
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
