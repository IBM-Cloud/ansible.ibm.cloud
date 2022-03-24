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
module: catalog_management_cm_offering
short_description: Manage cm_offering resources.
author: IBM SDK Generator
version_added: "0.1"
description:
    - This module creates, updates, or deletes a cm_offering.
    - By default the module will look for an existing cm_offering.
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
            - Short description in the requested language.
        type: str
    offering_support_url:
        description:
            - [deprecated] - Use offering.support instead.  URL to be displayed in the Consumption UI for getting support on this offering.
        type: str
    metadata:
        description:
            - Map of metadata values for this offering.
        type: dict
    keywords:
        description:
            - List of keywords associated with offering, typically used to search for it.
        type: list
    hidden:
        description:
            - Determine if this offering should be displayed in the Consumption UI.
        type: bool
    public_publish_approved:
        description:
            - Indicates if this offering has been approved for use by all IBM Cloud users.
        type: bool
    portal_ui_url:
        description:
            - The portal UI URL.
        type: str
    rev:
        description:
            - Cloudant revision.
        type: str
    rating:
        description:
            - Repository info for offerings.
        type: dict
    kinds:
        description:
            - Array of kind.
        type: list
    media:
        description:
            - A list of media items related to this offering.
        type: list
    share_with_ibm:
        description:
            - Denotes IBM employee availability of an Offering.
        type: bool
    features:
        description:
            - list of features associated with this offering.
        type: list
    ibm_publish_approved:
        description:
            - Indicates if this offering has been approved for use by all IBMers.
        type: bool
    provider:
        description:
            - Deprecated - Provider of this offering.
        type: str
    portal_approval_record:
        description:
            - The portal's approval record ID.
        type: str
    public_original_crn:
        description:
            - The original offering CRN that this publish entry came from.
        type: str
    id:
        description:
            - unique id.
        type: str
    share_with_all:
        description:
            - Denotes public availability of an Offering.
        type: bool
    offering_docs_url:
        description:
            - URL for an additional docs with this offering.
        type: str
    crn:
        description:
            - The crn for this specific offering.
        type: str
    disclaimer:
        description:
            - A disclaimer for this offering.
        type: str
    pc_managed:
        description:
            - Offering is managed by Partner Center.
        type: bool
    catalog_name:
        description:
            - The name of the catalog.
        type: str
    share_enabled:
        description:
            - Denotes access list availability of an Offering.
        type: bool
    created:
        description:
            - The date and time this catalog was created.
        type: str
    publish_approved:
        description:
            - Offering has been approved to publish to permitted to IBM or Public Catalog.
        type: bool
    offering_icon_url:
        description:
            - URL for an icon associated with this offering.
        type: str
    label:
        description:
            - Display Name in the requested language.
        type: str
    long_description:
        description:
            - Long description in the requested language.
        type: str
    url:
        description:
            - The url for this specific offering.
        type: str
    tags:
        description:
            - List of tags associated with this catalog.
        type: list
    catalog_id:
        description:
            - The id of the catalog containing this offering.
        type: str
    permit_request_ibm_public_publish:
        description:
            - Is it permitted to request publishing to IBM or Public.
        type: bool
    name:
        description:
            - The programmatic name of this offering.
        type: str
    publish_public_crn:
        description:
            - The crn of the public catalog entry of this offering.
        type: str
    repo_info:
        description:
            - Repository info for offerings.
        type: dict
    updated:
        description:
            - The date and time this catalog was last updated.
        type: str
    support:
        description:
            - Offering Support information.
        type: dict
    provider_info:
        description:
            - Information on the provider for this offering, or omitted if no provider information is given.
        type: dict
    if_match:
        description:
            - Offering etag contained in quotes.
        type: str
    digest:
        description:
            - Return the digest format of the specified offering.  Default is false.
        type: bool
    catalog_identifier:
        description:
            - Catalog identifier.
        type: str
    type:
        description:
            - Offering Parameter Type.  Valid values are 'name' or 'id'.  Default is 'id'.
        type: str
    :
        description:
            - 
        type: List[JsonPatchOperation]
    offering_id:
        description:
            - Offering identification.
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
        offering_support_url=dict(
            type='str',
            required=False),
        metadata=dict(
            type='dict',
            required=False),
        keywords=dict(
            type='list',
            required=False),
        hidden=dict(
            type='bool',
            required=False),
        public_publish_approved=dict(
            type='bool',
            required=False),
        portal_ui_url=dict(
            type='str',
            required=False),
        rev=dict(
            type='str',
            required=False),
        rating=dict(
            type='dict',
            required=False),
        kinds=dict(
            type='list',
            required=False),
        media=dict(
            type='list',
            required=False),
        share_with_ibm=dict(
            type='bool',
            required=False),
        features=dict(
            type='list',
            required=False),
        ibm_publish_approved=dict(
            type='bool',
            required=False),
        provider=dict(
            type='str',
            required=False),
        portal_approval_record=dict(
            type='str',
            required=False),
        public_original_crn=dict(
            type='str',
            required=False),
        id=dict(
            type='str',
            required=False),
        share_with_all=dict(
            type='bool',
            required=False),
        offering_docs_url=dict(
            type='str',
            required=False),
        crn=dict(
            type='str',
            required=False),
        disclaimer=dict(
            type='str',
            required=False),
        pc_managed=dict(
            type='bool',
            required=False),
        catalog_name=dict(
            type='str',
            required=False),
        share_enabled=dict(
            type='bool',
            required=False),
        created=dict(
            type='str',
            required=False),
        publish_approved=dict(
            type='bool',
            required=False),
        offering_icon_url=dict(
            type='str',
            required=False),
        label=dict(
            type='str',
            required=False),
        long_description=dict(
            type='str',
            required=False),
        url=dict(
            type='str',
            required=False),
        tags=dict(
            type='list',
            required=False),
        catalog_id=dict(
            type='str',
            required=False),
        permit_request_ibm_public_publish=dict(
            type='bool',
            required=False),
        name=dict(
            type='str',
            required=False),
        publish_public_crn=dict(
            type='str',
            required=False),
        repo_info=dict(
            type='dict',
            required=False),
        updated=dict(
            type='str',
            required=False),
        support=dict(
            type='dict',
            required=False),
        provider_info=dict(
            type='dict',
            required=False),
        if_match=dict(
            type='str',
            required=False),
        digest=dict(
            type='bool',
            required=False),
        catalog_identifier=dict(
            type='str',
            required=False),
        type=dict(
            type='str',
            required=False),
        =dict(
            type='List[JsonPatchOperation]',
            required=False),
        offering_id=dict(
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
    offering_support_url = module.params["offering_support_url"]
    metadata = module.params["metadata"]
    keywords = module.params["keywords"]
    hidden = module.params["hidden"]
    public_publish_approved = module.params["public_publish_approved"]
    portal_ui_url = module.params["portal_ui_url"]
    rev = module.params["rev"]
    rating = module.params["rating"]
    kinds = module.params["kinds"]
    media = module.params["media"]
    share_with_ibm = module.params["share_with_ibm"]
    features = module.params["features"]
    ibm_publish_approved = module.params["ibm_publish_approved"]
    provider = module.params["provider"]
    portal_approval_record = module.params["portal_approval_record"]
    public_original_crn = module.params["public_original_crn"]
    id = module.params["id"]
    share_with_all = module.params["share_with_all"]
    offering_docs_url = module.params["offering_docs_url"]
    crn = module.params["crn"]
    disclaimer = module.params["disclaimer"]
    pc_managed = module.params["pc_managed"]
    catalog_name = module.params["catalog_name"]
    share_enabled = module.params["share_enabled"]
    created = module.params["created"]
    publish_approved = module.params["publish_approved"]
    offering_icon_url = module.params["offering_icon_url"]
    label = module.params["label"]
    long_description = module.params["long_description"]
    url = module.params["url"]
    tags = module.params["tags"]
    catalog_id = module.params["catalog_id"]
    permit_request_ibm_public_publish = module.params["permit_request_ibm_public_publish"]
    name = module.params["name"]
    publish_public_crn = module.params["publish_public_crn"]
    repo_info = module.params["repo_info"]
    updated = module.params["updated"]
    support = module.params["support"]
    provider_info = module.params["provider_info"]
    if_match = module.params["if_match"]
    digest = module.params["digest"]
    catalog_identifier = module.params["catalog_identifier"]
    type = module.params["type"]
     = module.params[""]
    offering_id = module.params["offering_id"]

    state = module.params["state"]

    sdk = CatalogManagementV1.new_instance()

    resource_exists=True

    # Check for existence
    if offering_id:
        try:
            sdk.get_offering(
                catalog_identifier=catalog_identifier,
                offering_id=offering_id,
                type=type,
                digest=digest,
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
                sdk.delete_offering(
                    catalog_identifier=catalog_identifier,
                    offering_id=offering_id,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                payload = {"id": offering_id , "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": offering_id , "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.create_offering(
                    catalog_identifier=catalog_identifier,
                    id=id,
                    rev=rev,
                    url=url,
                    crn=crn,
                    label=label,
                    name=name,
                    offering_icon_url=offering_icon_url,
                    offering_docs_url=offering_docs_url,
                    offering_support_url=offering_support_url,
                    tags=tags,
                    keywords=keywords,
                    rating=rating,
                    created=created,
                    updated=updated,
                    short_description=short_description,
                    long_description=long_description,
                    features=features,
                    kinds=kinds,
                    pc_managed=pc_managed,
                    publish_approved=publish_approved,
                    share_with_all=share_with_all,
                    share_with_ibm=share_with_ibm,
                    share_enabled=share_enabled,
                    permit_request_ibm_public_publish=permit_request_ibm_public_publish,
                    ibm_publish_approved=ibm_publish_approved,
                    public_publish_approved=public_publish_approved,
                    public_original_crn=public_original_crn,
                    publish_public_crn=publish_public_crn,
                    portal_approval_record=portal_approval_record,
                    portal_ui_url=portal_ui_url,
                    catalog_id=catalog_id,
                    catalog_name=catalog_name,
                    metadata=metadata,
                    disclaimer=disclaimer,
                    hidden=hidden,
                    provider=provider,
                    provider_info=provider_info,
                    repo_info=repo_info,
                    support=support,
                    media=media,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.update_offering(
                    catalog_identifier=catalog_identifier,
                    offering_id=offering_id,
                    if_match=if_match,
                    updates=,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)

def main():
    run_module()

if __name__ == '__main__':
    main()
