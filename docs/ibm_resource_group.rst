
ibm_resource_group -- Manage ibm_resource_group resources.
==========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module creates, updates, or deletes a ibm_resource_group.

By default the module will look for an existing ibm_resource_group.



Requirements
------------
The below requirements are needed on the host that executes this module.

- ResourceManagerV2



Parameters
----------

  account_id (optional, str, None)
    The account id of the resource group.


  name (optional, str, None)
    The new name of the resource group.


  state_ (optional, str, None)
    The state of the resource group.


  id (optional, str, None)
    The short or long ID of the alias.


  state (optional, str, present)
    Should the resource be present or absent.













Authors
~~~~~~~

- IBM SDK Generator

