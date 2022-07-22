
ibm_cm_version -- Manage ibm_cm_version resources.
==================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module creates, updates, or deletes a ibm_cm_version.

By default the module will look for an existing ibm_cm_version.



Requirements
------------
The below requirements are needed on the host that executes this module.

- CatalogManagementV1



Parameters
----------

  content (optional, str, None)
    byte array representing the content to be imported.  Only supported for OVA images at this time.


  tags (optional, list, None)
    Tags array.


  target_kinds (optional, list, None)
    Target kinds.  Current valid values are 'iks', 'roks', 'vcenter', and 'terraform'.


  repo_type (optional, str, None)
    The type of repository containing this version.  Valid values are 'public_git' or 'enterprise_git'.


  zipurl (optional, str, None)
    URL path to zip location.  If not specified, must provide content in the body of this call.


  version_loc_id (optional, str, None)
    A dotted value of `catalogID`.`versionID`.


  catalog_identifier (optional, str, None)
    Catalog identifier.


  offering_id (optional, str, None)
    Offering identification.


  target_version (optional, str, None)
    The semver value for this new version, if not found in the zip url package content.


  include_config (optional, bool, None)
    Add all possible configuration values to this version when importing.


  is_vsi (optional, bool, None)
    Indicates that the current terraform template is used to install a VSI Image.


  state (optional, str, present)
    Should the resource be present or absent.













Authors
~~~~~~~

- IBM SDK Generator

