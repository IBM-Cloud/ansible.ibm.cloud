
ibm_iam_access_group -- Manage ibm_iam_access_group resources.
==============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module creates, updates, or deletes a ibm_iam_access_group.

By default the module will look for an existing ibm_iam_access_group.



Requirements
------------
The below requirements are needed on the host that executes this module.

- IamAccessGroupsV2



Parameters
----------

  name (optional, str, None)
    Assign the specified name to the access group. This field is case-insensitive and has a limit of 100 characters. The group name has to be unique within an account.


  description (optional, str, None)
    Assign an optional description for the access group. This field has a limit of 250 characters.


  access_group_id (optional, str, None)
    The access group identifier.


  account_id (optional, str, None)
    Account ID of the API keys(s) to query. If a service IAM ID is specified in iam_id then account_id must match the account of the IAM ID. If a user IAM ID is specified in iam_id then then account_id must match the account of the Authorization token.


  if_match (optional, str, None)
    The current revision number of the group being updated. This can be found in the Create/Get access group response ETag header.


  transaction_id (optional, str, None)
    An optional transaction ID can be passed to your request, which can be useful for tracking calls through multiple services by using one identifier. The header key must be set to Transaction-Id and the value is anything that you choose. If no transaction ID is passed in, then a random ID is generated.


  show_federated (optional, bool, None)
    If show_federated is true, the group will return an is_federated value that is set to true if rules exist for the group.


  force (optional, bool, None)
    If force is true, delete the group as well as its associated members and rules.


  state (optional, str, present)
    Should the resource be present or absent.













Authors
~~~~~~~

- I
- B
- M
-  
- S
- D
- K
-  
- G
- e
- n
- e
- r
- a
- t
- o
- r

