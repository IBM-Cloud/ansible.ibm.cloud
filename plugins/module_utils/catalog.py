from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ibm_platform_services import GlobalCatalogV1
from .auth import get_authenticator

# catalog_sdk = GlobalCatalogV1.new_instance()
authenticator = get_authenticator(service_name='global_catalog')
if authenticator is None:
    raise ValueError("[ERROR] Cannot create the authenticator.")
catalog_sdk = GlobalCatalogV1(
    authenticator=authenticator,
)

# service_name = "logdna"
# location="us-south"
# plan ="14-day"

def get_serviceID_targetCRN_planID(service_name,plan,location):

    servicePlanID = ""
    catalogCRN = ""
    serviceID = ""

    serviceID, servicePlanID = get_planID(service_name,plan)
    if servicePlanID != "":
        deployments = get_child_objects(servicePlanID)
        for deployment in deployments:
            if deployment['metadata']['deployment']['location'] == location:
                catalogCRN = deployment['catalog_crn']

    if serviceID == "" or catalogCRN == "" or servicePlanID == "":
        raise ValueError("[ERROR] either of service plan or service name or location is invalid or not found")
    else:
        return serviceID, catalogCRN,servicePlanID
    
def get_child_objects(id):
    result = catalog_sdk.get_child_objects(
    id = id,
    kind = '*',
    complete = True,
    ).get_result()
    resources = result['resources']
    return resources

def get_serviceID(service_name):
    serviceID_result = catalog_sdk.list_catalog_entries(
    q = service_name+" rc:true",
    include = "true",
    complete = True,
    ).get_result()

    if len(serviceID_result['resources']) > 0:
        serviceID=serviceID_result['resources'][0]['id']
        return serviceID
    else:
        raise ValueError("[ERROR] service name is invalid or not found")

def get_planID(service_name,plan):
    servicePlanID = ""
    serviceID = ""

    serviceID = get_serviceID(service_name)
    if serviceID != "":
        resources = get_child_objects(serviceID)
        for resource in resources:
            if resource['name'] == plan:
                servicePlanID = resource['id']
    if serviceID == "" or servicePlanID == "":
            raise ValueError("[ERROR] either of service plan or service name is invalid or not found")
    else:
        return serviceID,servicePlanID

# serviceID,catalogCRN,servicePlanID = get_serviceID_targetCRN_planID(service_name,plan,location)
# print (serviceID, catalogCRN,servicePlanID)
# serviceID1 = get_serviceID(service_name)
# print (serviceID1)
# serviceID2,servicePlanID2 = get_planID(service_name,plan)
# print (serviceID2,servicePlanID2)

