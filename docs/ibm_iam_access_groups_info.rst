
ibm_iam_access_groups_info -- Manage ibm_iam_access_groups info.
================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module retrieves one or more ibm_iam_access_groups(s).



Requirements
------------
The below requirements are needed on the host that executes this module.

- IamAccessGroupsV2



Parameters
----------

  account_id (optional, str, None)
    Account ID of the API keys(s) to query. If a service IAM ID is specified in iam_id then account_id must match the account of the IAM ID. If a user IAM ID is specified in iam_id then then account_id must match the account of the Authorization token.


  iam_id (optional, str, None)
    Return groups for member ID (IBMid, service ID or trusted profile ID).


  offset (optional, int, None)
    The offset of the first result item to be returned.


  transaction_id (optional, str, None)
    An optional transaction ID can be passed to your request, which can be useful for tracking calls through multiple services by using one identifier. The header key must be set to Transaction-Id and the value is anything that you choose. If no transaction ID is passed in, then a random ID is generated.


  limit (optional, int, None)
    Return up to this limit of results where limit is between 0 and 100.


  show_federated (optional, bool, None)
    If show_federated is true, each group listed will return an is_federated value that is set to true if rules exist for the group.


  sort (optional, str, None)
    Sort the results by id, name, description, or is_federated flag.


  hide_public_access (optional, bool, None)
    If hide_public_access is true, do not include the Public Access Group in the results.













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

