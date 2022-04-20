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
module: ibm_resource_group_info
short_description: Manage ibm_resource_group info.
author: IBM SDK Generator
version_added: "0.1"
description:
    - This module retrieves one or more ibm_resource_group(s).
requirements:
    - "ResourceManagerV2"
options:
    id:
        description:
            - The short or long ID of the alias.
        type: str
'''

EXAMPLES = r'''
Examples coming soon.
'''


from ansible.module_utils.basic import AnsibleModule
from ibm_cloud_sdk_core import ApiException
from ibm_platform_services import ResourceManagerV2

from ..module_utils.auth import get_authenticator


def run_module():
    module_args = dict(
        id=dict(
            type='str',
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    id = module.params["id"]

    authenticator = get_authenticator(service_name='resource_manager')
    if authenticator is None:
        module.fail_json(msg='Cannot create the authenticator.')

    sdk = ResourceManagerV2(
        authenticator=authenticator,
    )

    # list
    try:
        response = sdk.get_resource_group(
            id=id
        )
        module.exit_json(msg=response.get_result())
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
