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
from ibm_platform_services import CatalogManagementV1 # Todo: change this to external python package format

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: catalog_management_cm_catalog
short_description: Manage cm_catalog resources.
author: IBM SDK Generator
version_added: "0.1"
description:
    - This module creates, updates, or deletes a cm_catalog.
    - By default the module will look for an existing cm_catalog.
requirements:
    - "CatalogManagementV1"
options:
    state:
        description:
            - Should the resource be present or absent.
        type: str
        default: present
        choices: [present, absent]
    short_description:
        description:
            - Description in the requested language.
        type: str
    resource_group_id:
        description:
            - Resource group id the catalog is owned by.
        type: str
    owning_account:
        description:
            - Account that owns catalog.
        type: str
    kind:
        description:
            - Kind of catalog. Supported kinds are offering and vpe.
        type: str
    rev:
        description:
            - Cloudant revision.
        type: str
    catalog_icon_url:
        description:
            - URL for an icon associated with this catalog.
        type: str
    label:
        description:
            - Display Name in the requested language.
        type: str
    tags:
        description:
            - List of tags associated with this catalog.
        type: list
    features:
        description:
            - List of features associated with this catalog.
        type: list
    disabled:
        description:
            - Denotes whether a catalog is disabled.
        type: bool
    id:
        description:
            - Unique ID.
        type: str
    catalog_filters:
        description:
            - Filters for account and catalog filters.
        type: dict
    syndication_settings:
        description:
            - Feature information.
        type: dict
    catalog_identifier:
        description:
            - Catalog identifier.
        type: str
'''

EXAMPLES = r'''
Examples coming soon.
'''

def run_module():
    module_args = dict(
        short_description=dict(
            type='str',
            required=False),
        resource_group_id=dict(
            type='str',
            required=False),
        owning_account=dict(
            type='str',
            required=False),
        kind=dict(
            type='str',
            required=False),
        rev=dict(
            type='str',
            required=False),
        catalog_icon_url=dict(
            type='str',
            required=False),
        label=dict(
            type='str',
            required=False),
        tags=dict(
            type='list',
            required=False),
        features=dict(
            type='list',
            required=False),
        disabled=dict(
            type='bool',
            required=False),
        id=dict(
            type='str',
            required=False),
        catalog_filters=dict(
            type='dict',
            required=False),
        syndication_settings=dict(
            type='dict',
            required=False),
        catalog_identifier=dict(
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

    short_description = module.params["short_description"]
    resource_group_id = module.params["resource_group_id"]
    owning_account = module.params["owning_account"]
    kind = module.params["kind"]
    rev = module.params["rev"]
    catalog_icon_url = module.params["catalog_icon_url"]
    label = module.params["label"]
    tags = module.params["tags"]
    features = module.params["features"]
    disabled = module.params["disabled"]
    id = module.params["id"]
    catalog_filters = module.params["catalog_filters"]
    syndication_settings = module.params["syndication_settings"]
    catalog_identifier = module.params["catalog_identifier"]

    state = module.params["state"]

    sdk = CatalogManagementV1.new_instance()

    resource_exists=True

    # Check for existence
    if catalog_identifier:
        try:
            sdk.get_catalog(
                catalog_identifier=catalog_identifier,
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
                sdk.delete_catalog(
                    catalog_identifier=catalog_identifier,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                payload = {"id": catalog_identifier , "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": catalog_identifier , "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.create_catalog(
                    id=id,
                    rev=rev,
                    label=label,
                    short_description=short_description,
                    catalog_icon_url=catalog_icon_url,
                    tags=tags,
                    features=features,
                    disabled=disabled,
                    resource_group_id=resource_group_id,
                    owning_account=owning_account,
                    catalog_filters=catalog_filters,
                    syndication_settings=syndication_settings,
                    kind=kind,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.replace_catalog(
                    catalog_identifier=catalog_identifier,
                    id=id,
                    rev=rev,
                    label=label,
                    short_description=short_description,
                    catalog_icon_url=catalog_icon_url,
                    tags=tags,
                    features=features,
                    disabled=disabled,
                    resource_group_id=resource_group_id,
                    owning_account=owning_account,
                    catalog_filters=catalog_filters,
                    syndication_settings=syndication_settings,
                    kind=kind,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)

def main():
    run_module()

if __name__ == '__main__':
    main()
