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

from ansible.modules.cloud.ibm import resource_manager_resource_groups_info
from units.compat.mock import patch
from units.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

from .common import DetailedResponseMock


class TestResourceGroupListModuleInfo(ModuleTestCase):
    """
    Test class for ResourceGroupList module testing.
    """

    def test_read_resource_groups_success(self):
        """Test the "read" path - successful."""
        datasource = {
            'id': 'testString',
        }

        patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_groups_info.ResourceManagerV2.get_resource_group')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(datasource)

        set_module_args({
            'id': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_MANAGER_AUTH_TYPE'] = 'noAuth'
            resource_manager_resource_groups_info.main()

        assert result.exception.args[0]['msg'] == datasource

        mock.assert_called_once_with(
            id='testString',
        )

        patcher.stop()

    def test_read_resource_groups_failed(self):
        """Test the "read" path - failed."""
        patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_groups_info.ResourceManagerV2.get_resource_group')
        mock = patcher.start()
        mock.side_effect = ApiException(400, message='Read resource_groups error')

        set_module_args({
            'id': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_MANAGER_AUTH_TYPE'] = 'noAuth'
            resource_manager_resource_groups_info.main()

        assert result.exception.args[0]['msg'] == 'Read resource_groups error'

        mock.assert_called_once_with(
            id='testString',
        )

        patcher.stop()

    def test_list_resource_groups_success(self):
        """Test the "list" path - successful."""
        patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_groups_info.ResourceManagerV2.list_resource_groups')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock([])

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_MANAGER_AUTH_TYPE'] = 'noAuth'
            resource_manager_resource_groups_info.main()

        assert result.exception.args[0]['msg'] == []

        mock.assert_called_once()

        patcher.stop()

    def test_list_resource_groups_failed(self):
        """Test the "list" path - failed."""
        patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_groups_info.ResourceManagerV2.list_resource_groups')
        mock = patcher.start()
        mock.side_effect = ApiException(400, message='List resource_groups error')

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_MANAGER_AUTH_TYPE'] = 'noAuth'
            resource_manager_resource_groups_info.main()

        assert result.exception.args[0]['msg'] == 'List resource_groups error'

        mock.assert_called_once()

        patcher.stop()