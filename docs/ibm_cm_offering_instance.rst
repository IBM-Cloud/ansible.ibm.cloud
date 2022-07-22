
ibm_cm_offering_instance -- Manage ibm_cm_offering_instance resources.
======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module creates, updates, or deletes a ibm_cm_offering_instance.

By default the module will look for an existing ibm_cm_offering_instance.



Requirements
------------
The below requirements are needed on the host that executes this module.

- CatalogManagementV1



Parameters
----------

  kind_format (optional, str, None)
    the format this instance has (helm, operator, ova...).


  install_plan (optional, str, None)
    Type of install plan (also known as approval strategy) for operator subscriptions. Can be either automatic, which automatically upgrades operators to the latest in a channel, or manual, which requires approval on the cluster.


  metadata (optional, dict, None)
    Map of metadata values for this offering instance.


  cluster_region (optional, str, None)
    Cluster region (e.g., us-south).


  resource_group_id (optional, str, None)
    Id of the resource group to provision the offering instance into.


  rev (optional, str, None)
    Cloudant revision.


  channel (optional, str, None)
    Channel to pin the operator subscription to.


  label (optional, str, None)
    the label for this instance.


  offering_id (optional, str, None)
    Offering ID this instance was created from.


  version (optional, str, None)
    The version this instance was installed from (not version id).


  url (optional, str, None)
    url reference to this object.


  catalog_id (optional, str, None)
    Catalog ID this instance was created from.


  cluster_id (optional, str, None)
    Cluster ID.


  schematics_workspace_id (optional, str, None)
    Id of the schematics workspace, for offering instances provisioned through schematics.


  id (optional, str, None)
    provisioned instance ID (part of the CRN).


  cluster_namespaces (optional, list, None)
    List of target namespaces to install into.


  cluster_all_namespaces (optional, bool, None)
    designate to install into all namespaces.


  crn (optional, str, None)
    platform CRN for this instance.


  last_operation (optional, dict, None)
    the last operation performed and status.


    operation (optional, str, None)
      last operation performed.


    state_ (optional, str, None)
      state after the last operation performed.


    message (optional, str, None)
      additional information about the last operation.


    transaction_id (optional, str, None)
      transaction id from the last operation.


    updated (optional, str, None)
      Date and time last updated.



  instance_identifier (optional, str, None)
    Version Instance identifier.


  x_auth_refresh_token (optional, str, None)
    IAM Refresh token.


  state (optional, str, present)
    Should the resource be present or absent.













Authors
~~~~~~~

- IBM SDK Generator

