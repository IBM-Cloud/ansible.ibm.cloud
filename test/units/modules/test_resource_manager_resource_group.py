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

from ansible.modules.cloud.ibm import resource_manager_resource_group
from ibm_platform_services import *  # pylint: disable=wildcard-import,unused-wildcard-import
from units.compat.mock import patch
from units.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

from .common import DetailedResponseMock


class TestResourceGroupModule(ModuleTestCase):
    """
    Test class for ResourceGroup module testing.
    """

    def test_read_resource_group_failed(self):
        """Test the inner "read" path in this module with a server error response."""

        patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_group.ResourceManagerV2.get_resource_group')
        mock = patcher.start()
        mock.side_effect = ApiException(500, message='Something went wrong...')

        set_module_args({
            'id': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_MANAGER_AUTH_TYPE'] = 'noAuth'
            resource_manager_resource_group.main()

        assert result.exception.args[0]['msg'] == 'Something went wrong...'

        mock.assert_called_once_with(
            id='testString',
        )

        patcher.stop()

    def test_create_resource_group_success(self):
        """Test the "create" path - successful."""
        resource = {
            'name': 'test1',
            'account_id': '25eba2a9-beef-450b-82cf-f5ad5e36c6dd',
        }

        patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_group.ResourceManagerV2.create_resource_group')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_resource_group_patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_group.ResourceManagerV2.get_resource_group')
        get_resource_group_mock = get_resource_group_patcher.start()

        set_module_args({
            'name': 'test1',
            'account_id': '25eba2a9-beef-450b-82cf-f5ad5e36c6dd',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_MANAGER_AUTH_TYPE'] = 'noAuth'
            resource_manager_resource_group.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            name='test1',
            account_id='25eba2a9-beef-450b-82cf-f5ad5e36c6dd',
        )

        mock.assert_called_once_with(**mock_data)

        get_resource_group_mock.assert_not_called()

        get_resource_group_patcher.stop()
        patcher.stop()

    def test_create_resource_group_failed(self):
        """Test the "create" path - failed."""

        get_resource_group_patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_group.ResourceManagerV2.get_resource_group')
        get_resource_group_mock = get_resource_group_patcher.start()

        patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_group.ResourceManagerV2.create_resource_group')
        mock = patcher.start()
        mock.side_effect = ApiException(400, message='Create resource_group error')

        set_module_args({
            'name': 'test1',
            'account_id': '25eba2a9-beef-450b-82cf-f5ad5e36c6dd',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_MANAGER_AUTH_TYPE'] = 'noAuth'
            resource_manager_resource_group.main()

        assert result.exception.args[0]['msg'] == 'Create resource_group error'

        mock_data = dict(
            name='test1',
            account_id='25eba2a9-beef-450b-82cf-f5ad5e36c6dd',
        )

        mock.assert_called_once_with(**mock_data)

        get_resource_group_mock.assert_not_called()

        get_resource_group_patcher.stop()
        patcher.stop()

    def test_update_resource_group_success(self):
        """Test the "update" path - successful."""
        resource = {
            'id': 'testString',
            'name': 'testString',
            'state': 'testString',
        }

        patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_group.ResourceManagerV2.update_resource_group')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_resource_group_patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_group.ResourceManagerV2.get_resource_group')
        get_resource_group_mock = get_resource_group_patcher.start()
        get_resource_group_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'id': 'testString',
            'name': 'testString',
            'state': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_MANAGER_AUTH_TYPE'] = 'noAuth'
            resource_manager_resource_group.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            id='testString',
            name='testString',
            state='testString',
        )

        mock.assert_called_once_with(**mock_data)

        get_resource_group_mock_data = dict(
            id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_resource_group_mock_data:
            get_resource_group_mock_data[param] = mock_data.get(param, None)

        get_resource_group_mock.assert_called_once_with(**get_resource_group_mock_data)

        get_resource_group_patcher.stop()
        patcher.stop()

    def test_update_resource_group_failed(self):
        """Test the "update" path - failed."""
        resource = {
            'id': 'testString',
            'name': 'testString',
            'state': 'testString',
        }

        patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_group.ResourceManagerV2.update_resource_group')
        mock = patcher.start()
        mock.side_effect = ApiException(400, message='Update resource_group error')

        get_resource_group_patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_group.ResourceManagerV2.get_resource_group')
        get_resource_group_mock = get_resource_group_patcher.start()
        get_resource_group_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'id': 'testString',
            'name': 'testString',
            'state': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_MANAGER_AUTH_TYPE'] = 'noAuth'
            resource_manager_resource_group.main()

        assert result.exception.args[0]['msg'] == 'Update resource_group error'

        mock_data = dict(
            id='testString',
            name='testString',
            state='testString',
        )

        mock.assert_called_once_with(**mock_data)

        get_resource_group_mock_data = dict(
            id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_resource_group_mock_data:
            get_resource_group_mock_data[param] = mock_data.get(param, None)

        get_resource_group_mock.assert_called_once_with(**get_resource_group_mock_data)

        get_resource_group_patcher.stop()
        patcher.stop()

    def test_delete_resource_group_success(self):
        """Test the "delete" path - successfull."""
        patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_group.ResourceManagerV2.delete_resource_group')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_resource_group_patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_group.ResourceManagerV2.get_resource_group')
        get_resource_group_mock = get_resource_group_patcher.start()
        get_resource_group_mock.return_value = DetailedResponseMock()

        args = {
            'id': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_MANAGER_AUTH_TYPE'] = 'noAuth'
            resource_manager_resource_group.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'deleted'

        mock_data = dict(
            id='testString',
        )

        mock.assert_called_once_with(**mock_data)

        get_resource_group_mock_data = dict(
            id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_resource_group_mock_data:
            get_resource_group_mock_data[param] = mock_data.get(param, None)

        get_resource_group_mock.assert_called_once_with(**get_resource_group_mock_data)

        get_resource_group_patcher.stop()
        patcher.stop()

    def test_delete_resource_group_not_exists(self):
        """Test the "delete" path - not exists."""
        patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_group.ResourceManagerV2.delete_resource_group')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_resource_group_patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_group.ResourceManagerV2.get_resource_group')
        get_resource_group_mock = get_resource_group_patcher.start()
        get_resource_group_mock.side_effect = ApiException(404)

        args = {
            'id': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['RESOURCE_MANAGER_AUTH_TYPE'] = 'noAuth'
            resource_manager_resource_group.main()

        assert result.exception.args[0]['changed'] is False
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'not_found'

        mock_data = dict(
            id='testString',
        )

        mock.assert_not_called()

        get_resource_group_mock_data = dict(
            id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_resource_group_mock_data:
            get_resource_group_mock_data[param] = mock_data.get(param, None)

        get_resource_group_mock.assert_called_once_with(**get_resource_group_mock_data)

        get_resource_group_patcher.stop()
        patcher.stop()

    def test_delete_resource_group_failed(self):
        """Test the "delete" path - failed."""
        patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_group.ResourceManagerV2.delete_resource_group')
        mock = patcher.start()
        mock.side_effect = ApiException(400, message='Delete resource_group error')

        get_resource_group_patcher = patch('ansible.modules.cloud.ibm.resource_manager_resource_group.ResourceManagerV2.get_resource_group')
        get_resource_group_mock = get_resource_group_patcher.start()
        get_resource_group_mock.return_value = DetailedResponseMock()

        set_module_args({
            'id': 'testString',
            'state': 'absent',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['RESOURCE_MANAGER_AUTH_TYPE'] = 'noAuth'
            resource_manager_resource_group.main()

        assert result.exception.args[0]['msg'] == 'Delete resource_group error'

        mock_data = dict(
            id='testString',
        )

        mock.assert_called_once_with(**mock_data)

        get_resource_group_mock_data = dict(
            id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_resource_group_mock_data:
            get_resource_group_mock_data[param] = mock_data.get(param, None)

        get_resource_group_mock.assert_called_once_with(**get_resource_group_mock_data)

        get_resource_group_patcher.stop()
        patcher.stop()
