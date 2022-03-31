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
from ibm_platform_services import IamAccessGroupsV2 # Todo: change this to external python package format

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: iam_access_groups_iam_access_group_rule_info
short_description: Manage iam_access_group_rule info.
author: IBM SDK Generator
version_added: "0.1"
description:
    - This module retrieves one or more iam_access_group_rule(s).
requirements:
    - "IamAccessGroupsV2"
options:
    rule_id:
        description:
            - The rule to get.
        type: str
    access_group_id:
        description:
            - The access group identifier.
        type: str
    transaction_id:
        description:
            - An optional transaction ID can be passed to your request, which can be useful for tracking calls through multiple services by using one identifier. The header key must be set to Transaction-Id and the value is anything that you choose. If no transaction ID is passed in, then a random ID is generated.
        type: str
'''

EXAMPLES = r'''
Examples coming soon.
'''

def run_module():
    module_args = dict(
        rule_id=dict(
            type='str',
            required=False),
        access_group_id=dict(
            type='str',
            required=False),
        transaction_id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    rule_id = module.params["rule_id"]
    access_group_id = module.params["access_group_id"]
    transaction_id = module.params["transaction_id"]

    sdk = IamAccessGroupsV2.new_instance()

    if rule_id:
        # read
        try:
            response = sdk.get_access_group_rule(
                access_group_id=access_group_id,
                rule_id=rule_id,
                transaction_id=transaction_id
            )
            module.exit_json(msg=response.get_result())
        except ApiException as ex:
            module.fail_json(msg=ex.message)

def main():
    run_module()

if __name__ == '__main__':
    main()