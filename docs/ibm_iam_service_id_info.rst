
ibm_iam_service_id_info -- Manage ibm_iam_service_id info.
==========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module retrieves one or more ibm_iam_service_id(s).



Requirements
------------
The below requirements are needed on the host that executes this module.

- IamIdentityV1



Parameters
----------

  include_history (optional, bool, None)
    Defines if the entity history is included in the response.


  id (optional, str, None)
    Unique ID of the service ID.


  include_activity (optional, bool, None)
    Defines if the entity's activity is included in the response. Retrieving activity data is an expensive operation, so please only request this when needed.













Authors
~~~~~~~

- IBM SDK Generator

