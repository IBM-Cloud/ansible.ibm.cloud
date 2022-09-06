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

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: ibm_schematics_inventory_info
short_description: Manage C(schematics_inventory) for Schematics Service API.
author: Kavya Handadi (@kavya498)
version_added: "1.0.0"
description:
  - This module retrieves one or more C(schematics_inventory) for Schematics Service API.
requirements:
  - "SchematicsV1"
options:
  inventory_id:
    description:
      - Resource Inventory Id.  Use C(GET /v2/inventories) API to look up the Resource Inventory definition Ids  in your IBM Cloud account.
    type: str
  profile:
    description:
      - Level of details returned by the get method.
    type: str
    choices:
      - summary
      - detailed
      - ids
seealso:
  - name: IBM Cloud Schematics docs
    description: Use Schematics to run your Ansible playbooks to provision, configure, and manage IBM Cloud resources.
    link: U(https://cloud.ibm.com/docs/schematics)
notes:
  - |
    Authenticate this module by using an IBM Cloud API key.
    For more information about working with IBM Cloud API keys, see I(Managing API keys): U(https://cloud.ibm.com/docs/account?topic=account-manapikey).
  - |
    To configure the authentication, set your IBM Cloud API key on the C(IC_API_KEY) environment variable.
    The API key will be used to authenticate all IBM Cloud modules that use this environment variable.
'''

EXAMPLES = r'''
- name: Read ibm_schematics_inventory
  ibm_schematics_inventory_info:
'''

RETURN = '''
msg:
  description: |-
    A dictionary that represents the result.
    In case of "read", it's an C(InventoryResourceRecord).
  returned: always
  type: dict
'''

from ..module_utils import config
from ansible.module_utils.basic import AnsibleModule

try:
    from ibm_schematics import SchematicsV1
    from ibm_cloud_sdk_core import ApiException
except ImportError:
    pass


def run_module():
    module_args = dict(
        inventory_id=dict(
            type='str',
            required=False),
        profile=dict(
            type='str',
            choices=['summary', 'detailed', 'ids'],
            required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    inventory_id = module.params["inventory_id"]
    profile = module.params["profile"]

    sdk = config.get_schematicsv1_sdk()

    if inventory_id:
        # read
        try:
            response = sdk.get_inventory(
                inventory_id=inventory_id,
                profile=profile
            )
            module.exit_json(msg=response.get_result())
        except ApiException as ex:
            module.fail_json(msg=ex.message)


def main():
    run_module()


if __name__ == '__main__':
    main()
