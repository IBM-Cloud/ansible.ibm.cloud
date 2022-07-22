
ibm_iam_service_id -- Manage ibm_iam_service_id resources.
==========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module creates, updates, or deletes a ibm_iam_service_id.

By default the module will look for an existing ibm_iam_service_id.



Requirements
------------
The below requirements are needed on the host that executes this module.

- IamIdentityV1



Parameters
----------

  account_id (optional, str, None)
    ID of the account the service ID belongs to.


  apikey (optional, dict, None)
    Parameters for the API key in the Create service Id V1 REST request.


    name (optional, str, None)
      Name of the API key. The name is not checked for uniqueness. Therefore multiple names with the same value can exist. Access is done via the UUID of the API key.


    description (optional, str, None)
      The optional description of the API key. The 'description' property is only available if a description was provided during a create of an API key.


    apikey (optional, str, None)
      You can optionally passthrough the API key value for this API key. If passed, NO validation of that apiKey value is done, i.e. the value can be non-URL safe. If omitted, the API key management will create an URL safe opaque API key value. The value of the API key is checked for uniqueness. Please ensure enough variations when passing in this value.


    store_value (optional, bool, None)
      Send true or false to set whether the API key value is retrievable in the future by using the Get details of an API key request. If you create an API key for a user, you must specify `false` or omit the value. We don't allow storing of API keys for users.



  name (optional, str, None)
    Name of the Service Id. The name is not checked for uniqueness. Therefore multiple names with the same value can exist. Access is done via the UUID of the Service Id.


  unique_instance_crns (optional, list, None)
    Optional list of CRNs (string array) which point to the services connected to the service ID.


  description (optional, str, None)
    The optional description of the Service Id. The 'description' property is only available if a description was provided during a create of a Service Id.


  include_history (optional, bool, None)
    Defines if the entity history is included in the response.


  if_match (optional, str, None)
    Version of the service ID to be updated. Specify the version that you retrieved as entity_tag (ETag header) when reading the service ID. This value helps identifying parallel usage of this API. Pass * to indicate to update any version available. This might result in stale updates.


  entity_lock (optional, str, None)
    Indicates if the service ID is locked for further write operations. False by default.


  id (optional, str, None)
    Unique ID of the service ID.


  include_activity (optional, bool, None)
    Defines if the entity's activity is included in the response. Retrieving activity data is an expensive operation, so please only request this when needed.


  state (optional, str, present)
    Should the resource be present or absent.













Authors
~~~~~~~

- IBM SDK Generator

