
ibm_iam_access_group_members -- Manage ibm_iam_access_group_members resources.
==============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module creates, updates, or deletes a ibm_iam_access_group_members.

By default the module will look for an existing ibm_iam_access_group_members.



Requirements
------------
The below requirements are needed on the host that executes this module.

- IamAccessGroupsV2



Parameters
----------

  members (optional, list, None)
    An array of member objects to add to an access group.


    iam_id (optional, str, None)
      The IBMid, service ID or trusted profile ID of the member.


    type (optional, str, None)
      The type of the member, must be either "user", "service" or "trusted profile".



  access_group_id (optional, str, None)
    The access group identifier.


  iam_id (optional, str, None)
    The IAM identifier.


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


  state (optional, str, present)
    Should the resource be present or absent.













Authors
~~~~~~~

- IBM SDK Generator

