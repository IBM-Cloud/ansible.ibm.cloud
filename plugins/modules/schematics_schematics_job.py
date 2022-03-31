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
module: schematics_schematics_job
short_description: Manage schematics_job resources.
author: IBM SDK Generator
version_added: "0.1"
description:
    - This module creates, updates, or deletes a schematics_job.
    - By default the module will look for an existing schematics_job.
requirements:
    - "SchematicsV1"
options:
    settings:
        description:
            - Environment variables used by the Job while performing Action or Workspace.
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
    data:
        description:
            - Job data.
        type: dict
        suboptions:
            job_type:
                description:
                    - Type of Job.
                type: str
    inputs:
        description:
            - Job inputs used by Action or Workspace.
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
    command_name:
        description:
            - Schematics job command name.
        type: str
    command_object:
        description:
            - Name of the Schematics automation resource.
        type: str
    command_parameter:
        description:
            - Schematics job command parameter (playbook-name).
        type: str
    tags:
        description:
            - User defined tags, while running the job.
        type: list
        elements: str
    command_options:
        description:
            - Command line options for the command.
        type: list
        elements: str
    command_object_id:
        description:
            - Job command object id (workspace-id, action-id).
        type: str
    log_summary:
        description:
            - Job log summary record.
        type: dict
        suboptions:
            job_id:
                description:
                    - Workspace Id.
                type: str
            job_type:
                description:
                    - Type of Job.
                type: str
            log_start_at:
                description:
                    - Job log start timestamp.
                type: str
            log_analyzed_till:
                description:
                    - Job log update timestamp.
                type: str
            elapsed_time:
                description:
                    - Job log elapsed time (log_analyzed_till - log_start_at).
                type: float
            log_errors:
                description:
                    - Job log errors.
                type: list
                suboptions:
                    error_code:
                        description:
                            - Error code in the Log.
                        type: str
                    error_msg:
                        description:
                            - Summary error message in the log.
                        type: str
                    error_count:
                        description:
                            - Number of occurrence.
                        type: float
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
    status:
        description:
            - Job Status.
        type: dict
        suboptions:
            position_in_queue:
                description:
                    - Position of job in pending queue.
                type: float
            total_in_queue:
                description:
                    - Total no. of jobs in pending queue.
                type: float
    refresh_token:
        description:
            - The IAM refresh token for the user or service identity.

  **Retrieving refresh token**: 
  * Use `export IBMCLOUD_API_KEY=<ibmcloud_api_key>`, and execute `curl -X POST "https://iam.cloud.ibm.com/identity/token" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=$IBMCLOUD_API_KEY" -u bx:bx`. 
  * For more information, about creating IAM access token and API Docs, refer, [IAM access token](/apidocs/iam-identity-token-api#gettoken-password) and [Create API key](/apidocs/iam-identity-token-api#create-api-key).  

  **Limitation**: 
  * If the token is expired, you can use `refresh token` to get a new IAM access token. 
  * The `refresh_token` parameter cannot be used to retrieve a new IAM access token. 
  * When the IAM access token is about to expire, use the API key to create a new access token.
        type: str
    job_id:
        description:
            - Job Id. Use `GET /v2/jobs` API to look up the Job Ids in your IBM Cloud account.
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
        # Represents the JobData Python class
        data=dict(
            type='dict',
            options=dict(
                job_type=dict(
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
        command_name=dict(
            type='str',
            required=False),
        command_object=dict(
            type='str',
            required=False),
        command_parameter=dict(
            type='str',
            required=False),
        tags=dict(
            type='list',
            elements=str,
            required=False),
        command_options=dict(
            type='list',
            elements=str,
            required=False),
        command_object_id=dict(
            type='str',
            required=False),
        # Represents the JobLogSummary Python class
        log_summary=dict(
            type='dict',
            options=dict(
                job_id=dict(
                    type='str',
                    required=False),
                job_type=dict(
                    type='str',
                    required=False),
                log_start_at=dict(
                    type='str',
                    required=False),
                log_analyzed_till=dict(
                    type='str',
                    required=False),
                elapsed_time=dict(
                    type='float',
                    required=False),
                log_errors=dict(
                    type='list',
                    options=dict(
                        error_code=dict(
                            type='str',
                            required=False),
                        error_msg=dict(
                            type='str',
                            required=False),
                        error_count=dict(
                            type='float',
                            required=False),
                    ),
                    required=False),
            ),
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
        # Represents the JobStatus Python class
        status=dict(
            type='dict',
            options=dict(
                position_in_queue=dict(
                    type='float',
                    required=False),
                total_in_queue=dict(
                    type='float',
                    required=False),
            ),
            required=False),
        refresh_token=dict(
            type='str',
            required=False),
        job_id=dict(
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

    settings = module.params["settings"]
    data = module.params["data"]
    inputs = module.params["inputs"]
    command_name = module.params["command_name"]
    command_object = module.params["command_object"]
    command_parameter = module.params["command_parameter"]
    tags = module.params["tags"]
    command_options = module.params["command_options"]
    command_object_id = module.params["command_object_id"]
    log_summary = module.params["log_summary"]
    location = module.params["location"]
    bastion = module.params["bastion"]
    status = module.params["status"]
    refresh_token = module.params["refresh_token"]
    job_id = module.params["job_id"]
    profile = module.params["profile"]
    propagate = module.params["propagate"]
    force = module.params["force"]

    state = module.params["state"]

    sdk = SchematicsV1.new_instance()

    resource_exists=True

    # Check for existence
    if job_id:
        try:
            sdk.get_job(
                job_id=job_id,
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
                sdk.delete_job(
                    job_id=job_id,
                    refresh_token=refresh_token,
                    force=force,
                    propagate=propagate,
                )
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                payload = {"id": job_id , "status": "deleted"}
                module.exit_json(changed=True, msg=payload)
        else:
            payload = {"id": job_id , "status": "not_found"}
            module.exit_json(changed=False, msg=payload)

    if state == "present":
        if not resource_exists:
            # Create path
            try:
                result = sdk.create_job(
                    refresh_token=refresh_token,
                    command_object=command_object,
                    command_object_id=command_object_id,
                    command_name=command_name,
                    command_parameter=command_parameter,
                    command_options=command_options,
                    inputs=inputs,
                    settings=settings,
                    tags=tags,
                    location=location,
                    status=status,
                    data=data,
                    bastion=bastion,
                    log_summary=log_summary,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)
        else:
            # Update path
            try:
                result = sdk.update_job(
                    job_id=job_id,
                    refresh_token=refresh_token,
                    command_object=command_object,
                    command_object_id=command_object_id,
                    command_name=command_name,
                    command_parameter=command_parameter,
                    command_options=command_options,
                    inputs=inputs,
                    settings=settings,
                    tags=tags,
                    location=location,
                    status=status,
                    data=data,
                    bastion=bastion,
                    log_summary=log_summary,
                ).get_result()
            except ApiException as ex:
                module.fail_json(msg=ex.message)
            else:
                module.exit_json(changed=True, msg=result)

def main():
    run_module()

if __name__ == '__main__':
    main()
