
ibm_iam_access_group_rule -- Manage ibm_iam_access_group_rule resources.
========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module creates, updates, or deletes a ibm_iam_access_group_rule.

By default the module will look for an existing ibm_iam_access_group_rule.



Requirements
------------
The below requirements are needed on the host that executes this module.

- IamAccessGroupsV2



Parameters
----------

  name (optional, str, None)
    The name of the rule.


  expiration (optional, int, None)
    The number of hours that the rule lives for.


  conditions (optional, list, None)
    A list of conditions the rule must satisfy.


    claim (optional, str, None)
      The claim to evaluate against. This will be found in the `ext` claims of a user's login request.


    operator (optional, str, None)
      The operation to perform on the claim.


    value (optional, str, None)
      The stringified JSON value that the claim is compared to using the operator.



  realm_name (optional, str, None)
    The url of the identity provider.


  rule_id (optional, str, None)
    The rule to get.


  access_group_id (optional, str, None)
    The access group identifier.


  if_match (optional, str, None)
    The current revision number of the rule being updated. This can be found in the Get Rule response ETag header.


  transaction_id (optional, str, None)
    An optional transaction ID can be passed to your request, which can be useful for tracking calls through multiple services by using one identifier. The header key must be set to Transaction-Id and the value is anything that you choose. If no transaction ID is passed in, then a random ID is generated.


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

