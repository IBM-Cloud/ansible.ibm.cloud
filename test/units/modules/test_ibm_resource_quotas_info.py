# coding: utf-8

# (C) Copyright IBM Corp. 2022.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os

from ibm_cloud_sdk_core import ApiException
from units.compat.mock import patch
from units.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

from .common import DetailedResponseMock
from ansible.modules.cloud.ibm import ibm_resource_quotas_info


class TestQuotaDefinitionListModuleInfo(ModuleTestCase):
    """
    Test class for QuotaDefinitionList module testing.
    """

    def test_list_ibm_resource_quotas_success(self):
        """Test the "list" path - successful."""
        patcher = patch('ansible.modules.cloud.ibm.ibm_resource_quotas_info.ResourceManagerV2.list_quota_definitions')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock([])

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_MANAGER_AUTH_TYPE'] = 'noAuth'
            ibm_resource_quotas_info.main()

        assert result.exception.args[0]['msg'] == []

        mock.assert_called_once()

        patcher.stop()

    def test_list_ibm_resource_quotas_failed(self):
        """Test the "list" path - failed."""
        patcher = patch('ansible.modules.cloud.ibm.ibm_resource_quotas_info.ResourceManagerV2.list_quota_definitions')
        mock = patcher.start()
        mock.side_effect = ApiException(400, message='List ibm_resource_quotas error')

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_MANAGER_AUTH_TYPE'] = 'noAuth'
            ibm_resource_quotas_info.main()

        assert result.exception.args[0]['msg'] == 'List ibm_resource_quotas error'

        mock.assert_called_once()

        patcher.stop()
