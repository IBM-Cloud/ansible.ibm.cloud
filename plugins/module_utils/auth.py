
import os

from ibm_cloud_sdk_core import get_authenticator_from_environment
from ibm_cloud_sdk_core.authenticators import Authenticator, IAMAuthenticator


def get_authenticator(service_name: str) -> Authenticator:
    authenticator = get_authenticator_from_environment(service_name=service_name)
    if authenticator is None:
        apikey = os.getenv('IC_API_KEY', None)
        if apikey is None:
            return None

        authenticator = IAMAuthenticator(apikey=apikey)

    return authenticator