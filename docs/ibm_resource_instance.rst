
ibm_resource_instance -- Manage ibm_resource_instance resources.
================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module creates, updates, or deletes a ibm_resource_instance.

By default the module will look for an existing ibm_resource_instance.



Requirements
------------
The below requirements are needed on the host that executes this module.

- ResourceControllerV2



Parameters
----------

  resource_group (optional, str, None)
    The ID of the resource group.


  plan (optional, str, None)
    The unique ID of the plan associated with the offering. This value is provided by and stored in the global catalog.


  allow_cleanup (optional, bool, None)
    A boolean that dictates if the resource instance should be deleted (cleaned up) during the processing of a region instance delete call.


  name (optional, str, None)
    The name of the instance. Must be 180 characters or less and cannot include any special characters other than `(space) - . _ :`.


  parameters (optional, dict, None)
    Configuration options represented as key-value pairs that are passed through to the target resource brokers.


  location (optional, str, None)
    The deployment location where the instance should be hosted.


  tags (optional, list, None)
    Tags that are attached to the instance after provisioning. These tags can be searched and managed through the Tagging API in IBM Cloud.


  entity_lock (optional, bool, None)
    Indicates if the resource instance is locked for further update or delete operations. It does not affect actions performed on child resources like aliases, bindings or keys. False by default.


  id (optional, str, None)
    The ID of the instance.


  recursive (optional, bool, None)
    Will delete resource bindings, keys and aliases associated with the instance.


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

