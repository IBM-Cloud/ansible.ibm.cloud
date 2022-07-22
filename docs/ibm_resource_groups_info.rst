
ibm_resource_groups_info -- Manage ibm_resource_groups info.
============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module retrieves one or more ibm_resource_groups(s).



Requirements
------------
The below requirements are needed on the host that executes this module.

- ResourceManagerV2



Parameters
----------

  date (optional, str, None)
    The date in the format of YYYY-MM which returns resource groups. Deleted resource groups will be excluded before this month.


  default (optional, bool, None)
    Boolean value to specify whether or not to list default resource groups.


  account_id (optional, str, None)
    The ID of the account that contains the resource groups that you want to get.


  name (optional, str, None)
    The name of the resource group.


  include_deleted (optional, bool, None)
    Boolean value to specify whether or not to list default resource groups.













Authors
~~~~~~~

- IBM SDK Generator

