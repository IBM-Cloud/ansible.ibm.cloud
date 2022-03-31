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
from ansible.module_utils.cloud.ibm.ibm_cloud import SchematicsV1 # Todo: change this to external python package format

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: schematics_schematics_action
short_description: Manage schematics_action resources.
author: IBM SDK Generator
version_added: "0.1"
description:
    - This module creates, updates, or deletes a schematics_action.
    - By default the module will look for an existing schematics_action.
requirements:
    - "SchematicsV1"
options:
    outputs:
        description:
            - Output variables for the Action.
        type: list
        suboptions:
            name:
                description:
                    - The name of the variable. For example, `name = "inventory username"`.
                type: str
            value:
                description:
                    - The value for the variable or reference to the value. For example, `value = "<provide your ssh_key_value with \n>"`. **Note** The SSH key should contain `\n` at the end of the key details in case of command line or API calls.
                type: str
            use_default:
                description:
                    - True, will ignore the data in the value attribute, instead the data in metadata.default_value will be used.
                type: bool
            link:
                description:
                    - The reference link to the variable value By default the expression points to `$self.value`.
                type: str
    settings:
        description:
            - Environment variables for the Action.
        type: list
        suboptions:
            name:
                description:
                    - The name of the variable. For example, `name = "inventory username"`.
                type: str
            value:
                description:
                    - The value for the variable or reference to the value. For example, `value = "<provide your ssh_key_value with \n>"`. **Note** The SSH key should contain `\n` at the end of the key details in case of command line or API calls.
                type: str
            use_default:
                description:
                    - True, will ignore the data in the value attribute, instead the data in metadata.default_value will be used.
                type: bool
            link:
                description:
                    - The reference link to the variable value By default the expression points to `$self.value`.
                type: str
    credentials:
        description:
            - credentials of the Action.
        type: list
        suboptions:
            name:
                description:
                    - The name of the variable. For example, `name = "inventory username"`.
                type: str
            value:
                description:
                    - The value for the variable or reference to the value. For example, `value = "<provide your ssh_key_value with \n>"`. **Note** The SSH key should contain `\n` at the end of the key details in case of command line or API calls.
                type: str
            use_default:
                description:
                    - True, will ignore the data in the value attribute, instead the data in metadata.default_value will be used.
                type: bool
            link:
                description:
                    - The reference link to the variable value By default the expression points to `$self.value`.
                type: str
    inputs:
        description:
            - Input variables for the Action.
        type: list
        suboptions:
            name:
                description:
                    - The name of the variable. For example, `name = "inventory username"`.
                type: str
            value:
                description:
                    - The value for the variable or reference to the value. For example, `value = "<provide your ssh_key_value with \n>"`. **Note** The SSH key should contain `\n` at the end of the key details in case of command line or API calls.
                type: str
            use_default:
                description:
                    - True, will ignore the data in the value attribute, instead the data in metadata.default_value will be used.
                type: bool
            link:
                description:
                    - The reference link to the variable value By default the expression points to `$self.value`.
                type: str
    description:
        description:
            - Action description.
        type: str
    source_readme_url:
        description:
            - URL of the `README` file, for the source URL.
        type: str
    bastion_credential:
        description:
            - User editable variable data and system generated reference to the value.
        type: dict
        suboptions:
            name:
                description:
                    - The name of the variable. For example, `name = "inventory username"`.
                type: str
            value:
                description:
                    - The value for the variable or reference to the value. For example, `value = "<provide your ssh_key_value with \n>"`. **Note** The SSH key should contain `\n` at the end of the key details in case of command line or API calls.
                type: str
            use_default:
                description:
                    - True, will ignore the data in the value attribute, instead the data in metadata.default_value will be used.
                type: bool
            link:
                description:
                    - The reference link to the variable value By default the expression points to `$self.value`.
                type: str
    source_type:
        description:
            - Type of source for the Template.
        type: str
    source:
        description:
            - Source of templates, playbooks, or controls.
        type: dict
        suboptions:
            source_type:
                description:
                    - Type of source for the Template.
                type: str
    inventory:
        description:
            - Target inventory record ID, used by the action or ansible playbook.
        type: str
    command_parameter:
        description:
            - Schematics job command parameter (playbook-name).
        type: str
    tags:
        description:
            - Action tags.
        type: list
        elements: str
    user_state:
        description:
            - User defined status of the Schematics object.
        type: dict
        suboptions:
            state:
                description:
                    - User-defined states
              * `draft` Object can be modified; can be used by Jobs run by the author, during execution
              * `live` Object can be modified; can be used by Jobs during execution
              * `locked` Object cannot be modified; can be used by Jobs during execution
              * `disable` Object can be modified. cannot be used by Jobs during execution.
                type: str
            set_by:
                description:
                    - Name of the User who set the state of the Object.
                type: str
            set_at:
                description:
                    - When the User who set the state of the Object.
                type: str
    bastion_connection_type:
        description:
            - Type of connection to be used when connecting to bastion host. If the `inventory_connection_type=winrm`, then `bastion_connection_type` is not supported.
        type: str
    inventory_connection_type:
        description:
            - Type of connection to be used when connecting to remote host. **Note** Currently, WinRM supports only Windows system with the public IPs and do not support Bastion host.
        type: str
    resource_group:
        description:
            - Resource-group name for an action.  By default, action is created in default resource group.
        type: str
    targets_ini:
        description:
            - Inventory of host and host group for the playbook in `INI` file format. For example, `"targets_ini": "[webserverhost] 
 172.22.192.6 
 [dbhost]
 172.22.192.5"`. For more information, about an inventory host group syntax, see [Inventory host groups](https://cloud.ibm.com/docs/schematics?topic=schematics-schematics-cli-reference#schematics-inventory-host-grps).
        type: str
    name:
        description:
            - The unique name of your action. The name can be up to 128 characters long and can include alphanumeric characters, spaces, dashes, and underscores. **Example** you can use the name to stop action.
        type: str
    location:
        description:
            - List of locations supported by IBM Cloud Schematics service.  While creating your workspace or action, choose the right region, since it cannot be changed.  Note, this does not limit the location of the IBM Cloud resources, provisioned using Schematics.
        type: str
    bastion:
        description:
            - Describes a bastion resource.
        type: dict
        suboptions:
            name:
                description:
                    - Bastion Name(Unique).
                type: str
            host:
                description:
                    - Reference to the Inventory resource definition.
                type: str
    state:
        description:
            - Computed state of the Action.
        type: dict
        suboptions:
            status_code:
                description:
                    - Status of automation (workspace or action).
                type: str
            status_job_id:
                description:
                    - Job id reference for this status.
                type: str
            status_message:
                description:
                    - Automation status message - to be displayed along with the status_code.
                type: str
    sys_lock:
        description:
            - System lock status.
        type: dict
        suboptions:
            sys_locked:
                description:
                    - Is the automation locked by a Schematic job ?.
                type: bool
            sys_locked_by:
                description:
                    - Name of the User who performed the job, that lead to the locking of the automation.
                type: str
            sys_locked_at:
                description:
                    - When the User performed the job that lead to locking of the automation ?.
                type: str
    action_id:
        description:
            - Action Id.  Use GET /actions API to look up the Action Ids in your IBM Cloud account.
        type: str
    profile:
        description:
            - Level of details returned by the get method.
        type: str
    propagate:
        description:
            - Auto propagate the chaange or deletion to the dependent resources.
        type: bool
    force:
        description:
            - Equivalent to -force options in the command line.
        type: bool
    x_github_token:
        description:
            - The personal access token to authenticate with your private GitHub or GitLab repository and access your Terraform template.
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
        outputs=dict(
            type='list',
            options=dict(
                name=dict(
                    type='str',
                    required=False),
                value=dict(
                    type='str',
                    required=False),
                use_default=dict(
                    type='bool',
                    required=False),
                link=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        settings=dict(
            type='list',
            options=dict(
                name=dict(
                    type='str',
                    required=False),
                value=dict(
                    type='str',
                    required=False),
                use_default=dict(
                    type='bool',
                    required=False),
                link=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        credentials=dict(
            type='list',
            options=dict(
                name=dict(
                    type='str',
                    required=False),
                value=dict(
                    type='str',
                    required=False),
                use_default=dict(
                    type='bool',
                    required=False),
                link=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        inputs=dict(
            type='list',
            options=dict(
                name=dict(
                    type='str',
                    required=False),
                value=dict(
                    type='str',
                    required=False),
                use_default=dict(
                    type='bool',
                    required=False),
                link=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        description=dict(
            type='str',
            required=False),
        source_readme_url=dict(
            type='str',
            required=False),
        # Represents the VariableData Python class
        bastion_credential=dict(
            type='dict',
            options=dict(
                name=dict(
                    type='str',
                    required=False),
                value=dict(
                    type='str',
                    required=False),
                use_default=dict(
                    type='bool',
                    required=False),
                link=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        source_type=dict(
            type='str',
            required=False),
        # Represents the ExternalSource Python class
        source=dict(
            type='dict',
            options=dict(
                source_type=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        inventory=dict(
            type='str',
            required=False),
        command_parameter=dict(
            type='str',
            required=False),
        tags=dict(
            type='list',
            elements=str,
            required=False),
        # Represents the UserState Python class
        user_state=dict(
            type='dict',
            options=dict(
                state=dict(
                    type='str',
                    required=False),
                set_by=dict(
                    type='str',
                    required=False),
                set_at=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        bastion_connection_type=dict(
            type='str',
            required=False),
        inventory_connection_type=dict(
            type='str',
            required=False),
        resource_group=dict(
            type='str',
            required=False),
        targets_ini=dict(
            type='str',
            required=False),
        name=dict(
            type='str',
            required=False),
        location=dict(
            type='str',
            required=False),
        # Represents the BastionResourceDefinition Python class
        bastion=dict(
            type='dict',
            options=dict(
                name=dict(
                    type='str',
                    required=False),
                host=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        # Represents the ActionState Python class
        state=dict(
            type='dict',
            options=dict(
                status_code=dict(
                    type='str',
                    required=False),
                status_job_id=dict(
                    type='str',
                    required=False),
                status_message=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        # Represents the SystemLock Python class
        sys_lock=dict(
            type='dict',
            options=dict(
                sys_locked=dict(
                    type='bool',
                    required=False),
                sys_locked_by=dict(
                    type='str',
                    required=False),
                sys_locked_at=dict(
                    type='str',
                    required=False),
            ),
            required=False),
        action_id=dict(
            type='str',
            required=False),
        profile=dict(
            type='str',
            required=False),
        propagate=dict(
            type='bool',
            required=False),
        force=dict(
            type='bool',
            required=False),
        x_github_token=dict(
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

    outputs = module.params["outputs"]
    settings = module.params["settings"]
    credentials = module.params["credentials"]
    inputs = module.params["inputs"]
    description = module.params["description"]
    source_readme_url = module.params["source_readme_url"]
    bastion_credential = module.params["bastion_credential"]
    source_type = module.params["source_type"]
    source = module.params["source"]
    inventory = module.params["inventory"]
    command_parameter = module.params["command_parameter"]
    tags = module.params["tags"]
    user_state = module.params["user_state"]
    bastion_connection_type = module.params["bastion_connection_type"]
    inventory_connection_type = module.params["inventory_connection_type"]
    resource_group = module.params["resource_group"]
    targets_ini = module.params["targets_ini"]
    name = module.params["name"]
    location = module.params["location"]
    bastion = module.params["bastion"]
    state = module.params["state"]
    sys_lock = module.params["sys_lock"]
    action_id = module.params["action_id"]
    profile = module.params["profile"]
    propagate = module.params["propagate"]
    force = module.params["force"]
    x_github_token = module.params["x_github_token"]

    state = module.params["state"]

    sdk = SchematicsV1.new_instance()

    resource_exists=True

    # Check for existence
    if action_id:
        try:
            sdk.get_action(
                action_id=action_id,
                profile=profile,
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
                sdk.delete_action(
                    action_id=action_id,
                    force=force,
                    propagate=propagate,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                payload = {"id": action_id , "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": action_id , "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.create_action(
                    name=name,
                    description=description,
                    location=location,
                    resource_group=resource_group,
                    bastion_connection_type=bastion_connection_type,
                    inventory_connection_type=inventory_connection_type,
                    tags=tags,
                    user_state=user_state,
                    source_readme_url=source_readme_url,
                    source=source,
                    source_type=source_type,
                    command_parameter=command_parameter,
                    inventory=inventory,
                    credentials=credentials,
                    bastion=bastion,
                    bastion_credential=bastion_credential,
                    targets_ini=targets_ini,
                    inputs=inputs,
                    outputs=outputs,
                    settings=settings,
                    state=state,
                    sys_lock=sys_lock,
                    x_github_token=x_github_token,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.update_action(
                    action_id=action_id,
                    name=name,
                    description=description,
                    location=location,
                    resource_group=resource_group,
                    bastion_connection_type=bastion_connection_type,
                    inventory_connection_type=inventory_connection_type,
                    tags=tags,
                    user_state=user_state,
                    source_readme_url=source_readme_url,
                    source=source,
                    source_type=source_type,
                    command_parameter=command_parameter,
                    inventory=inventory,
                    credentials=credentials,
                    bastion=bastion,
                    bastion_credential=bastion_credential,
                    targets_ini=targets_ini,
                    inputs=inputs,
                    outputs=outputs,
                    settings=settings,
                    state=state,
                    sys_lock=sys_lock,
                    x_github_token=x_github_token,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)

def main():
    run_module()

if __name__ == '__main__':
    main()
