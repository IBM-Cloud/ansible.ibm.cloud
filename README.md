# IBM Cloud Ansible Collection
This collection provides a series of Ansible modules and plugins for interacting with the [IBM Cloud](https://cloud.ibm.com/)

This collection works with Ansible 2.9+

## Prerequisites

1. Install [Python3]

2. [RedHat Ansible] 2.9+

    ```
    pip install "ansible>=2.9.2"
    ```

# Installation
1. Build collection using below command. This will generate a tar.gz file in the current working directory
```bash
ansible-galaxy collection build -f
```
2.  Install the collection using below command.
```bash
ansible-galaxy collection install <above generated tar.gz file name> -f
```
3. The python module dependencies are not installed by ansible-galaxy. They can be manually installed using pip:
```bash
pip install requirements.txt
```

# Resources Supported
|Service|Supported modules|
|------|-----|
|Catalog Management|ibm_cm_catalog<br>ibm_cm_offering<br>ibm_cm_offering_instance<br>ibm_cm_version |
|IAM Access Group |ibm_iam_access_group<br>ibm_iam_access_group_info<br>ibm_iam_access_group_members<br>ibm_iam_access_group_members_info<br>ibm_iam_access_group_rule<br>ibm_iam_access_group_rule_info<br>ibm_iam_access_group_rules_info<br>ibm_iam_access_groups_info |
|Resource Manager |ibm_resource_group<br>ibm_resource_group_info<br>ibm_resource_groups_info <br>ibm_resource_quota_info<br>ibm_resource_quotas_info |
|Resource Controller |ibm_resource_instance<br>ibm_resource_instance_info<br>ibm_resource_instances_info<br> ibm_resource_key<br>ibm_resource_key_info<br>ibm_resource_keys_info <br> ibm_resource_alias<br>ibm_resource_alias_info<br>ibm_resource_aliases_info <br> ibm_resource_binding<br>ibm_resource_binding_info<br>ibm_resource_bindings_info<br>ibm_resource_reclamations_info |
| Schematics |ibm_schematics_action<br>ibm_schematics_action_info<br>ibm_schematics_inventory<br>ibm_schematics_inventory_info<br>ibm_schematics_job<br>ibm_schematics_job_info<br>ibm_schematics_resource_query<br>ibm_schematics_resource_query_info<br>ibm_schematics_state_info<br>ibm_schematics_workspace<br>ibm_schematics_workspace_info|

