
schematics_schematics_inventory -- Manage schematics_inventory resources.
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module creates, updates, or deletes a schematics_inventory.

By default the module will look for an existing schematics_inventory.



Requirements
------------
The below requirements are needed on the host that executes this module.

- SchematicsV1



Parameters
----------

  inventories_ini (optional, str, None)
    Input inventory of host and host group for the playbook, in the `.ini` file format.


  resource_group (optional, str, None)
    Resource-group name for the Inventory definition.   By default, Inventory definition will be created in Default Resource Group.


  resource_queries (optional, list, None)
    Input resource query definitions that is used to dynamically generate the inventory of host and host group for the playbook.


  name (optional, str, None)
    The unique name of your Inventory definition. The name can be up to 128 characters long and can include alphanumeric characters, spaces, dashes, and underscores.


  description (optional, str, None)
    The description of your Inventory definition. The description can be up to 2048 characters long in size.


  location (optional, str, None)
    List of locations supported by IBM Cloud Schematics service.  While creating your workspace or action, choose the right region, since it cannot be changed.  Note, this does not limit the location of the IBM Cloud resources, provisioned using Schematics.


  inventory_id (optional, str, None)
    Resource Inventory Id.  Use `GET /v2/inventories` API to look up the Resource Inventory definition Ids  in your IBM Cloud account.


  propagate (optional, bool, None)
    Auto propagate the chaange or deletion to the dependent resources.


  force (optional, bool, None)
    Equivalent to -force options in the command line.


  state (optional, str, present)
    Should the resource be present or absent.













Authors
~~~~~~~

- IBM SDK Generator

