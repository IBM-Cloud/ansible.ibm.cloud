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
module: iam_access_groups_iam_access_groups_info
short_description: Manage iam_access_groups info.
author: IBM SDK Generator
version_added: "0.1"
description:
    - This module retrieves one or more iam_access_groups(s).
requirements:
    - "IamAccessGroupsV2"
options:
    access_group_id:
        description:
            - The access group identifier.
        type: str
    account_id:
        description:
            - Account ID of the API keys(s) to query. If a service IAM ID is specified in iam_id then account_id must match the account of the IAM ID. If a user IAM ID is specified in iam_id then then account_id must match the account of the Authorization token.
        type: str
    iam_id:
        description:
            - Return groups for member ID (IBMid, service ID or trusted profile ID).
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
    show_federated:
        description:
            - If show_federated is true, each group listed will return an is_federated value that is set to true if rules exist for the group.
        type: bool
    sort:
        description:
            - Sort the results by id, name, description, or is_federated flag.
        type: str
    hide_public_access:
        description:
            - If hide_public_access is true, do not include the Public Access Group in the results.
        type: bool
'''

EXAMPLES = r'''
Examples coming soon.
'''

def run_module():
    module_args = dict(
        access_group_id=dict(
            type='str',
            required=False),
        account_id=dict(
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
        show_federated=dict(
            type='bool',
            required=False),
        sort=dict(
            type='str',
            required=False),
        hide_public_access=dict(
            type='bool',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    access_group_id = module.params["access_group_id"]
    account_id = module.params["account_id"]
    iam_id = module.params["iam_id"]
    offset = module.params["offset"]
    transaction_id = module.params["transaction_id"]
    limit = module.params["limit"]
    show_federated = module.params["show_federated"]
    sort = module.params["sort"]
    hide_public_access = module.params["hide_public_access"]

    sdk = IamAccessGroupsV2.new_instance()

    if access_group_id:
        # read
        try:
            response = sdk.get_access_group(
                access_group_id=access_group_id,
                transaction_id=transaction_id,
                show_federated=show_federated
            )
            module.exit_json(msg=response.get_result())
        except ApiException as ex:
            module.fail_json(msg=ex.message)

    # list
    try:
        response = sdk.list_access_groups(
            account_id=account_id,
            transaction_id=transaction_id,
            iam_id=iam_id,
            limit=limit,
            offset=offset,
            sort=sort,
            show_federated=show_federated,
            hide_public_access=hide_public_access
        )
        module.exit_json(msg=response.get_result())
    except ApiException as ex:
        module.fail_json(msg=ex.message)

def main():
    run_module()

if __name__ == '__main__':
    main()
