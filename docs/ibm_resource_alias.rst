
ibm_resource_alias -- Manage ibm_resource_alias resources.
==========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module creates, updates, or deletes a ibm_resource_alias.

By default the module will look for an existing ibm_resource_alias.



Requirements
------------
The below requirements are needed on the host that executes this module.

- ResourceControllerV2



Parameters
----------

  name (optional, str, None)
    The name of the alias. Must be 180 characters or less and cannot include any special characters other than `(space) - . _ :`.


  source (optional, str, None)
    The ID of resource instance.


  target (optional, str, None)
    The CRN of target name(space) in a specific environment, for example, space in Dallas YP, CFEE instance etc.


  id (optional, str, None)
    The ID of the alias.


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

