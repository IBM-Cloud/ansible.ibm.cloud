
ibm_resource_bindings_info -- Manage ibm_resource_bindings info.
================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module retrieves one or more ibm_resource_bindings(s).



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


  name (optional, str, None)
    The human-readable name of the binding.


  limit (optional, int, None)
    Limit on how many items should be returned.


  start (optional, str, None)
    An optional token that indicates the beginning of the page of results to be returned. Any additional query parameters are ignored if a page token is present. If omitted, the first page of results is returned. This value is obtained from the 'next_url' field of the operation response.


  guid (optional, str, None)
    The GUID of the binding.


  resource_id (optional, str, None)
    The unique ID of the offering (service name). This value is provided by and stored in the global catalog.


  updated_to (optional, str, None)
    End date inclusive filter.


  region_binding_id (optional, str, None)
    The ID of the binding in the target environment. For example, `service_binding_id` in a given IBM Cloud environment.













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

