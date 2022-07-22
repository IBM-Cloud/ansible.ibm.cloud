
ibm_resource_instances_info -- Manage ibm_resource_instances info.
==================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module retrieves one or more ibm_resource_instances(s).



Requirements
------------
The below requirements are needed on the host that executes this module.

- ResourceControllerV2



Parameters
----------

  resource_group_id (optional, str, None)
    The ID of the resource group.


  updated_from (optional, str, None)
    Start date inclusive filter.


  plan (optional, str, None)
    The unique ID of the plan associated with the offering. This value is provided by and stored in the global catalog.


  sub_type (optional, str, None)
    The sub-type of instance, for example, `kms`.


  name (optional, str, None)
    The human-readable name of the instance.


  limit (optional, int, None)
    Limit on how many items should be returned.


  start (optional, str, None)
    An optional token that indicates the beginning of the page of results to be returned. Any additional query parameters are ignored if a page token is present. If omitted, the first page of results is returned. This value is obtained from the 'next_url' field of the operation response.


  guid (optional, str, None)
    The GUID of the instance.


  service (optional, str, None)
    The unique ID of the offering. This value is provided by and stored in the global catalog.


  state_ (optional, str, None)
    The state of the instance. If not specified, instances in state `active` and `provisioning` are returned.


  type (optional, str, None)
    The type of the instance, for example, `service_instance`.


  updated_to (optional, str, None)
    End date inclusive filter.













Authors
~~~~~~~

- IBM SDK Generator

