
ibm_cm_catalog -- Manage ibm_cm_catalog resources.
==================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This module creates, updates, or deletes a ibm_cm_catalog.

By default the module will look for an existing ibm_cm_catalog.



Requirements
------------
The below requirements are needed on the host that executes this module.

- CatalogManagementV1



Parameters
----------

  short_description (optional, str, None)
    Description in the requested language.


  resource_group_id (optional, str, None)
    Resource group id the catalog is owned by.


  owning_account (optional, str, None)
    Account that owns catalog.


  kind (optional, str, None)
    Kind of catalog. Supported kinds are offering and vpe.


  rev (optional, str, None)
    Cloudant revision.


  catalog_icon_url (optional, str, None)
    URL for an icon associated with this catalog.


  label (optional, str, None)
    Display Name in the requested language.


  tags (optional, list, None)
    List of tags associated with this catalog.


  features (optional, list, None)
    List of features associated with this catalog.


    title (optional, str, None)
      Heading.


    description (optional, str, None)
      Feature description.



  disabled (optional, bool, None)
    Denotes whether a catalog is disabled.


  id (optional, str, None)
    Unique ID.


  catalog_filters (optional, dict, None)
    Filters for account and catalog filters.


    include_all (optional, bool, None)
      -> true - Include all of the public catalog when filtering. Further settings will specifically exclude some offerings. false - Exclude all of the public catalog when filtering. Further settings will specifically include some offerings.


    category_filters (optional, dict, None)
      Filter against offering properties.


      include (optional, bool, None)
        -> true - This is an include filter, false - this is an exclude filter.


      filter (optional, dict, None)
        Offering filter terms.


        filter_terms (optional, list, None)
          List of values to match against. If include is true, then if the offering has one of the values then the offering is included. If include is false, then if the offering has one of the values then the offering is excluded.




    id_filters (optional, dict, None)
      Filter on offering ID's. There is an include filter and an exclule filter. Both can be set.


      include (optional, dict, None)
        Offering filter terms.


        filter_terms (optional, list, None)
          List of values to match against. If include is true, then if the offering has one of the values then the offering is included. If include is false, then if the offering has one of the values then the offering is excluded.



      exclude (optional, dict, None)
        Offering filter terms.


        filter_terms (optional, list, None)
          List of values to match against. If include is true, then if the offering has one of the values then the offering is included. If include is false, then if the offering has one of the values then the offering is excluded.





  syndication_settings (optional, dict, None)
    Feature information.


    remove_related_components (optional, bool, None)
      Remove related components.


    clusters (optional, list, None)
      Syndication clusters.


      region (optional, str, None)
        Cluster region.


      id (optional, str, None)
        Cluster ID.


      name (optional, str, None)
        Cluster name.


      resource_group_name (optional, str, None)
        Resource group ID.


      type (optional, str, None)
        Syndication type.


      namespaces (optional, list, None)
        Syndicated namespaces.


      all_namespaces (optional, bool, None)
        Syndicated to all namespaces on cluster.



    history (optional, dict, None)
      Feature information.


      namespaces (optional, list, None)
        Array of syndicated namespaces.


      clusters (optional, list, None)
        Array of syndicated namespaces.


        region (optional, str, None)
          Cluster region.


        id (optional, str, None)
          Cluster ID.


        name (optional, str, None)
          Cluster name.


        resource_group_name (optional, str, None)
          Resource group ID.


        type (optional, str, None)
          Syndication type.


        namespaces (optional, list, None)
          Syndicated namespaces.


        all_namespaces (optional, bool, None)
          Syndicated to all namespaces on cluster.



      last_run (optional, str, None)
        Date and time last syndicated.



    authorization (optional, dict, None)
      Feature information.


      token (optional, str, None)
        Array of syndicated namespaces.


      last_run (optional, str, None)
        Date and time last updated.




  catalog_identifier (optional, str, None)
    Catalog identifier.


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

