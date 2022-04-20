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
module: ibm_iam_access_group_members_info
short_description: Manage ibm_iam_access_group_members info.
author: IBM SDK Generator
version_added: "0.1"
description:
    - This module retrieves one or more ibm_iam_access_group_members(s).
requirements:
    - "IamAccessGroupsV2"
options:
    access_group_id:
        description:
            - The access group identifier.
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


from ansible.module_utils.basic import AnsibleModule
from ibm_cloud_sdk_core import ApiException
from ibm_platform_services import IamAccessGroupsV2

from ..module_utils.auth import get_authenticator


def run_module():
    module_args = dict(
        access_group_id=dict(
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
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    access_group_id = module.params["access_group_id"]
    offset = module.params["offset"]
    transaction_id = module.params["transaction_id"]
    limit = module.params["limit"]
    sort = module.params["sort"]
    type = module.params["type"]
    verbose = module.params["verbose"]

    authenticator = get_authenticator(service_name='iam_access_groups')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = IamAccessGroupsV2(
        authenticator=authenticator,
    )

    # list
    try:
        response = sdk.list_access_group_members(
            access_group_id=access_group_id,
            transaction_id=transaction_id,
            limit=limit,
            offset=offset,
            type=type,
            verbose=verbose,
            sort=sort
        )
        module.exit_json(msg=response.get_result())
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
