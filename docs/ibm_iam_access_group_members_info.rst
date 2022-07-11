
ibm_iam_access_group_members_info -- Manage ibm_iam_access_group_members info.
==============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module retrieves one or more ibm_iam_access_group_members(s).



Requirements
------------
The below requirements are needed on the host that executes this module.

- IamAccessGroupsV2



Parameters
----------

  access_group_id (optional, str, None)
    The access group identifier.


  offset (optional, int, None)
    The offset of the first result item to be returned.


  transaction_id (optional, str, None)
    An optional transaction ID can be passed to your request, which can be useful for tracking calls through multiple services by using one identifier. The header key must be set to Transaction-Id and the value is anything that you choose. If no transaction ID is passed in, then a random ID is generated.


  limit (optional, int, None)
    Return up to this limit of results where limit is between 0 and 100.


  sort (optional, str, None)
    If verbose is true, sort the results by id, name, or email.


  type (optional, str, None)
    Filter the results by member type.


  verbose (optional, bool, None)
    Return user's email and name for each user ID or the name for each service ID or trusted profile.













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

