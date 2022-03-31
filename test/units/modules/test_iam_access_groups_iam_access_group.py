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

from ansible.modules.cloud.ibm import iam_access_groups_iam_access_group
from ibm_platform_services import *  # pylint: disable=wildcard-import,unused-wildcard-import
from units.compat.mock import patch
from units.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

from .common import DetailedResponseMock


class TestGroupModule(ModuleTestCase):
    """
    Test class for Group module testing.
    """

    def test_read_iam_access_group_failed(self):
        """Test the inner "read" path in this module with a server error response."""

        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group.IamAccessGroupsV2.get_access_group')
        mock = patcher.start()
        mock.side_effect = ApiException(500, message='Something went wrong...')

        set_module_args({
            'access_group_id': 'testString',
            'transaction_id': 'testString',
            'show_federated': False,
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group.main()

        assert result.exception.args[0]['msg'] == 'Something went wrong...'

        mock.assert_called_once_with(
            access_group_id='testString',
            transaction_id='testString',
            show_federated=False,
        )

        patcher.stop()

    def test_create_iam_access_group_success(self):
        """Test the "create" path - successful."""
        resource = {
            'account_id': 'testString',
            'name': 'Managers',
            'description': 'Group for managers',
            'transaction_id': 'testString',
        }

        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group.IamAccessGroupsV2.create_access_group')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_access_group_patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group.IamAccessGroupsV2.get_access_group')
        get_access_group_mock = get_access_group_patcher.start()

        set_module_args({
            'account_id': 'testString',
            'name': 'Managers',
            'description': 'Group for managers',
            'transaction_id': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            account_id='testString',
            name='Managers',
            description='Group for managers',
            transaction_id='testString',
        )

        mock.assert_called_once_with(**mock_data)

        get_access_group_mock.assert_not_called()

        get_access_group_patcher.stop()
        patcher.stop()

    def test_create_iam_access_group_failed(self):
        """Test the "create" path - failed."""

        get_access_group_patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group.IamAccessGroupsV2.get_access_group')
        get_access_group_mock = get_access_group_patcher.start()

        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group.IamAccessGroupsV2.create_access_group')
        mock = patcher.start()
        mock.side_effect = ApiException(400, message='Create iam_access_group error')

        set_module_args({
            'account_id': 'testString',
            'name': 'Managers',
            'description': 'Group for managers',
            'transaction_id': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group.main()

        assert result.exception.args[0]['msg'] == 'Create iam_access_group error'

        mock_data = dict(
            account_id='testString',
            name='Managers',
            description='Group for managers',
            transaction_id='testString',
        )

        mock.assert_called_once_with(**mock_data)

        get_access_group_mock.assert_not_called()

        get_access_group_patcher.stop()
        patcher.stop()

    def test_update_iam_access_group_success(self):
        """Test the "update" path - successful."""
        resource = {
            'access_group_id': 'testString',
            'if_match': 'testString',
            'name': 'Awesome Managers',
            'description': 'Group for awesome managers.',
            'transaction_id': 'testString',
        }

        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group.IamAccessGroupsV2.update_access_group')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_access_group_patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group.IamAccessGroupsV2.get_access_group')
        get_access_group_mock = get_access_group_patcher.start()
        get_access_group_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'access_group_id': 'testString',
            'if_match': 'testString',
            'name': 'Awesome Managers',
            'description': 'Group for awesome managers.',
            'transaction_id': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            access_group_id='testString',
            if_match='testString',
            name='Awesome Managers',
            description='Group for awesome managers.',
            transaction_id='testString',
        )

        mock.assert_called_once_with(**mock_data)

        get_access_group_mock_data = dict(
            access_group_id='testString',
            transaction_id='testString',
            show_federated=False,
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_access_group_mock_data:
            get_access_group_mock_data[param] = mock_data.get(param, None)

        get_access_group_mock.assert_called_once_with(**get_access_group_mock_data)

        get_access_group_patcher.stop()
        patcher.stop()

    def test_update_iam_access_group_failed(self):
        """Test the "update" path - failed."""
        resource = {
            'access_group_id': 'testString',
            'if_match': 'testString',
            'name': 'Awesome Managers',
            'description': 'Group for awesome managers.',
            'transaction_id': 'testString',
        }

        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group.IamAccessGroupsV2.update_access_group')
        mock = patcher.start()
        mock.side_effect = ApiException(400, message='Update iam_access_group error')

        get_access_group_patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group.IamAccessGroupsV2.get_access_group')
        get_access_group_mock = get_access_group_patcher.start()
        get_access_group_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'access_group_id': 'testString',
            'if_match': 'testString',
            'name': 'Awesome Managers',
            'description': 'Group for awesome managers.',
            'transaction_id': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group.main()

        assert result.exception.args[0]['msg'] == 'Update iam_access_group error'

        mock_data = dict(
            access_group_id='testString',
            if_match='testString',
            name='Awesome Managers',
            description='Group for awesome managers.',
            transaction_id='testString',
        )

        mock.assert_called_once_with(**mock_data)

        get_access_group_mock_data = dict(
            access_group_id='testString',
            transaction_id='testString',
            show_federated=False,
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_access_group_mock_data:
            get_access_group_mock_data[param] = mock_data.get(param, None)

        get_access_group_mock.assert_called_once_with(**get_access_group_mock_data)

        get_access_group_patcher.stop()
        patcher.stop()

    def test_delete_iam_access_group_success(self):
        """Test the "delete" path - successfull."""
        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group.IamAccessGroupsV2.delete_access_group')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_access_group_patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group.IamAccessGroupsV2.get_access_group')
        get_access_group_mock = get_access_group_patcher.start()
        get_access_group_mock.return_value = DetailedResponseMock()

        args = {
            'access_group_id': 'testString',
            'transaction_id': 'testString',
            'force': False,
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'deleted'

        mock_data = dict(
            access_group_id='testString',
            transaction_id='testString',
            force=False,
        )

        mock.assert_called_once_with(**mock_data)

        get_access_group_mock_data = dict(
            access_group_id='testString',
            transaction_id='testString',
            show_federated=False,
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_access_group_mock_data:
            get_access_group_mock_data[param] = mock_data.get(param, None)

        get_access_group_mock.assert_called_once_with(**get_access_group_mock_data)

        get_access_group_patcher.stop()
        patcher.stop()

    def test_delete_iam_access_group_not_exists(self):
        """Test the "delete" path - not exists."""
        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group.IamAccessGroupsV2.delete_access_group')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_access_group_patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group.IamAccessGroupsV2.get_access_group')
        get_access_group_mock = get_access_group_patcher.start()
        get_access_group_mock.side_effect = ApiException(404)

        args = {
            'access_group_id': 'testString',
            'transaction_id': 'testString',
            'force': False,
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group.main()

        assert result.exception.args[0]['changed'] is False
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'not_found'

        mock_data = dict(
            access_group_id='testString',
            transaction_id='testString',
            force=False,
        )

        mock.assert_not_called()

        get_access_group_mock_data = dict(
            access_group_id='testString',
            transaction_id='testString',
            show_federated=False,
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_access_group_mock_data:
            get_access_group_mock_data[param] = mock_data.get(param, None)

        get_access_group_mock.assert_called_once_with(**get_access_group_mock_data)

        get_access_group_patcher.stop()
        patcher.stop()

    def test_delete_iam_access_group_failed(self):
        """Test the "delete" path - failed."""
        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group.IamAccessGroupsV2.delete_access_group')
        mock = patcher.start()
        mock.side_effect = ApiException(400, message='Delete iam_access_group error')

        get_access_group_patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group.IamAccessGroupsV2.get_access_group')
        get_access_group_mock = get_access_group_patcher.start()
        get_access_group_mock.return_value = DetailedResponseMock()

        set_module_args({
            'access_group_id': 'testString',
            'transaction_id': 'testString',
            'force': False,
            'state': 'absent',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group.main()

        assert result.exception.args[0]['msg'] == 'Delete iam_access_group error'

        mock_data = dict(
            access_group_id='testString',
            transaction_id='testString',
            force=False,
        )

        mock.assert_called_once_with(**mock_data)

        get_access_group_mock_data = dict(
            access_group_id='testString',
            transaction_id='testString',
            show_federated=False,
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_access_group_mock_data:
            get_access_group_mock_data[param] = mock_data.get(param, None)

        get_access_group_mock.assert_called_once_with(**get_access_group_mock_data)

        get_access_group_patcher.stop()
        patcher.stop()
