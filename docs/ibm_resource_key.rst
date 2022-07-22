
ibm_resource_key -- Manage ibm_resource_key resources.
======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module creates, updates, or deletes a ibm_resource_key.

By default the module will look for an existing ibm_resource_key.



Requirements
------------
The below requirements are needed on the host that executes this module.

- ResourceControllerV2



Parameters
----------

  role (optional, str, None)
    The service or custom role name or it's CRN.


  name (optional, str, None)
    The name of the key.


  source (optional, str, None)
    The ID of resource instance or alias.


  parameters (optional, dict, None)
    Configuration options represented as key-value pairs. Service defined options are passed through to the target resource brokers, whereas platform defined options are not.


    serviceid_crn (optional, str, None)
      An optional platform defined option to reuse an existing IAM serviceId for the role assignment.



  id (optional, str, None)
    The ID of the key.


  state (optional, str, present)
    Should the resource be present or absent.













Authors
~~~~~~~

- IBM SDK Generator

