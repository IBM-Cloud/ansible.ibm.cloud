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
module: ibm_resource_quotas_info
short_description: Manage ibm_resource_quotas info.
author: IBM SDK Generator
version_added: "0.1"
description:
    - This module retrieves one or more ibm_resource_quotas(s).
requirements:
    - "ResourceManagerV2"
options:
'''

EXAMPLES = r'''
Examples coming soon.
'''


from ansible.module_utils.basic import AnsibleModule
from ibm_cloud_sdk_core import ApiException
from ibm_platform_services import ResourceManagerV2


from ..module_utils import config
def run_module():
    module_args = dict(
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )


    sdk = config.get_resource_manager_sdk()

    # list
    try:
        response = sdk.list_quota_definitions(
        )
        module.exit_json(msg=response.get_result())
    except ApiException as ex:
        module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
