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

from ansible.modules.cloud.ibm import iam_access_groups_iam_access_group_rule
from ibm_platform_services import *  # pylint: disable=wildcard-import,unused-wildcard-import
from units.compat.mock import patch
from units.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

from .common import DetailedResponseMock


class TestRuleModule(ModuleTestCase):
    """
    Test class for Rule module testing.
    """

    def test_read_iam_access_group_rule_failed(self):
        """Test the inner "read" path in this module with a server error response."""

        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group_rule.IamAccessGroupsV2.get_access_group_rule')
        mock = patcher.start()
        mock.side_effect = ApiException(500, message='Something went wrong...')

        set_module_args({
            'access_group_id': 'testString',
            'rule_id': 'testString',
            'transaction_id': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group_rule.main()

        assert result.exception.args[0]['msg'] == 'Something went wrong...'

        mock.assert_called_once_with(
            access_group_id='testString',
            rule_id='testString',
            transaction_id='testString',
        )

        patcher.stop()

    def test_create_iam_access_group_rule_success(self):
        """Test the "create" path - successful."""
        rule_conditions_model = dict(
            claim='isManager',
            operator='EQUALS',
            value='true',
        )

        resource = {
            'access_group_id': 'testString',
            'expiration': 12,
            'realm_name': 'https://idp.example.org/SAML2',
            'conditions': [rule_conditions_model],
            'name': 'Manager group rule',
            'transaction_id': 'testString',
        }

        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group_rule.IamAccessGroupsV2.add_access_group_rule')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_access_group_rule_patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group_rule.IamAccessGroupsV2.get_access_group_rule')
        get_access_group_rule_mock = get_access_group_rule_patcher.start()

        set_module_args({
            'access_group_id': 'testString',
            'expiration': 12,
            'realm_name': 'https://idp.example.org/SAML2',
            'conditions': [rule_conditions_model],
            'name': 'Manager group rule',
            'transaction_id': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group_rule.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            access_group_id='testString',
            expiration=12,
            realm_name='https://idp.example.org/SAML2',
            conditions=[rule_conditions_model],
            name='Manager group rule',
            transaction_id='testString',
        )

        mock.assert_called_once_with(**mock_data)

        get_access_group_rule_mock.assert_not_called()

        get_access_group_rule_patcher.stop()
        patcher.stop()

    def test_create_iam_access_group_rule_failed(self):
        """Test the "create" path - failed."""

        get_access_group_rule_patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group_rule.IamAccessGroupsV2.get_access_group_rule')
        get_access_group_rule_mock = get_access_group_rule_patcher.start()

        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group_rule.IamAccessGroupsV2.add_access_group_rule')
        mock = patcher.start()
        mock.side_effect = ApiException(400, message='Create iam_access_group_rule error')

        rule_conditions_model = dict(
            claim='isManager',
            operator='EQUALS',
            value='true',
        )

        set_module_args({
            'access_group_id': 'testString',
            'expiration': 12,
            'realm_name': 'https://idp.example.org/SAML2',
            'conditions': [rule_conditions_model],
            'name': 'Manager group rule',
            'transaction_id': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group_rule.main()

        assert result.exception.args[0]['msg'] == 'Create iam_access_group_rule error'

        mock_data = dict(
            access_group_id='testString',
            expiration=12,
            realm_name='https://idp.example.org/SAML2',
            conditions=[rule_conditions_model],
            name='Manager group rule',
            transaction_id='testString',
        )

        mock.assert_called_once_with(**mock_data)

        get_access_group_rule_mock.assert_not_called()

        get_access_group_rule_patcher.stop()
        patcher.stop()

    def test_update_iam_access_group_rule_success(self):
        """Test the "update" path - successful."""
        rule_conditions_model = dict(
            claim='isManager',
            operator='EQUALS',
            value='true',
        )

        resource = {
            'access_group_id': 'testString',
            'rule_id': 'testString',
            'if_match': 'testString',
            'expiration': 12,
            'realm_name': 'https://idp.example.org/SAML2',
            'conditions': [rule_conditions_model],
            'name': 'Manager group rule',
            'transaction_id': 'testString',
        }

        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group_rule.IamAccessGroupsV2.replace_access_group_rule')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(resource)

        get_access_group_rule_patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group_rule.IamAccessGroupsV2.get_access_group_rule')
        get_access_group_rule_mock = get_access_group_rule_patcher.start()
        get_access_group_rule_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'access_group_id': 'testString',
            'rule_id': 'testString',
            'if_match': 'testString',
            'expiration': 12,
            'realm_name': 'https://idp.example.org/SAML2',
            'conditions': [rule_conditions_model],
            'name': 'Manager group rule',
            'transaction_id': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group_rule.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg'] == resource

        mock_data = dict(
            access_group_id='testString',
            rule_id='testString',
            if_match='testString',
            expiration=12,
            realm_name='https://idp.example.org/SAML2',
            conditions=[rule_conditions_model],
            name='Manager group rule',
            transaction_id='testString',
        )

        mock.assert_called_once_with(**mock_data)

        get_access_group_rule_mock_data = dict(
            access_group_id='testString',
            rule_id='testString',
            transaction_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_access_group_rule_mock_data:
            get_access_group_rule_mock_data[param] = mock_data.get(param, None)

        get_access_group_rule_mock.assert_called_once_with(**get_access_group_rule_mock_data)

        get_access_group_rule_patcher.stop()
        patcher.stop()

    def test_update_iam_access_group_rule_failed(self):
        """Test the "update" path - failed."""
        rule_conditions_model = dict(
            claim='isManager',
            operator='EQUALS',
            value='true',
        )

        resource = {
            'access_group_id': 'testString',
            'rule_id': 'testString',
            'if_match': 'testString',
            'expiration': 12,
            'realm_name': 'https://idp.example.org/SAML2',
            'conditions': [rule_conditions_model],
            'name': 'Manager group rule',
            'transaction_id': 'testString',
        }

        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group_rule.IamAccessGroupsV2.replace_access_group_rule')
        mock = patcher.start()
        mock.side_effect = ApiException(400, message='Update iam_access_group_rule error')

        get_access_group_rule_patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group_rule.IamAccessGroupsV2.get_access_group_rule')
        get_access_group_rule_mock = get_access_group_rule_patcher.start()
        get_access_group_rule_mock.return_value = DetailedResponseMock(resource)

        set_module_args({
            'access_group_id': 'testString',
            'rule_id': 'testString',
            'if_match': 'testString',
            'expiration': 12,
            'realm_name': 'https://idp.example.org/SAML2',
            'conditions': [rule_conditions_model],
            'name': 'Manager group rule',
            'transaction_id': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group_rule.main()

        assert result.exception.args[0]['msg'] == 'Update iam_access_group_rule error'

        mock_data = dict(
            access_group_id='testString',
            rule_id='testString',
            if_match='testString',
            expiration=12,
            realm_name='https://idp.example.org/SAML2',
            conditions=[rule_conditions_model],
            name='Manager group rule',
            transaction_id='testString',
        )

        mock.assert_called_once_with(**mock_data)

        get_access_group_rule_mock_data = dict(
            access_group_id='testString',
            rule_id='testString',
            transaction_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_access_group_rule_mock_data:
            get_access_group_rule_mock_data[param] = mock_data.get(param, None)

        get_access_group_rule_mock.assert_called_once_with(**get_access_group_rule_mock_data)

        get_access_group_rule_patcher.stop()
        patcher.stop()

    def test_delete_iam_access_group_rule_success(self):
        """Test the "delete" path - successfull."""
        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group_rule.IamAccessGroupsV2.remove_access_group_rule')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_access_group_rule_patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group_rule.IamAccessGroupsV2.get_access_group_rule')
        get_access_group_rule_mock = get_access_group_rule_patcher.start()
        get_access_group_rule_mock.return_value = DetailedResponseMock()

        args = {
            'access_group_id': 'testString',
            'rule_id': 'testString',
            'transaction_id': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group_rule.main()

        assert result.exception.args[0]['changed'] is True
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'deleted'

        mock_data = dict(
            access_group_id='testString',
            rule_id='testString',
            transaction_id='testString',
        )

        mock.assert_called_once_with(**mock_data)

        get_access_group_rule_mock_data = dict(
            access_group_id='testString',
            rule_id='testString',
            transaction_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_access_group_rule_mock_data:
            get_access_group_rule_mock_data[param] = mock_data.get(param, None)

        get_access_group_rule_mock.assert_called_once_with(**get_access_group_rule_mock_data)

        get_access_group_rule_patcher.stop()
        patcher.stop()

    def test_delete_iam_access_group_rule_not_exists(self):
        """Test the "delete" path - not exists."""
        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group_rule.IamAccessGroupsV2.remove_access_group_rule')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock()

        get_access_group_rule_patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group_rule.IamAccessGroupsV2.get_access_group_rule')
        get_access_group_rule_mock = get_access_group_rule_patcher.start()
        get_access_group_rule_mock.side_effect = ApiException(404)

        args = {
            'access_group_id': 'testString',
            'rule_id': 'testString',
            'transaction_id': 'testString',
            'state': 'absent',
        }

        set_module_args(args)

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group_rule.main()

        assert result.exception.args[0]['changed'] is False
        assert result.exception.args[0]['msg']['id'] == 'testString'
        assert result.exception.args[0]['msg']['status'] == 'not_found'

        mock_data = dict(
            access_group_id='testString',
            rule_id='testString',
            transaction_id='testString',
        )

        mock.assert_not_called()

        get_access_group_rule_mock_data = dict(
            access_group_id='testString',
            rule_id='testString',
            transaction_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_access_group_rule_mock_data:
            get_access_group_rule_mock_data[param] = mock_data.get(param, None)

        get_access_group_rule_mock.assert_called_once_with(**get_access_group_rule_mock_data)

        get_access_group_rule_patcher.stop()
        patcher.stop()

    def test_delete_iam_access_group_rule_failed(self):
        """Test the "delete" path - failed."""
        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group_rule.IamAccessGroupsV2.remove_access_group_rule')
        mock = patcher.start()
        mock.side_effect = ApiException(400, message='Delete iam_access_group_rule error')

        get_access_group_rule_patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group_rule.IamAccessGroupsV2.get_access_group_rule')
        get_access_group_rule_mock = get_access_group_rule_patcher.start()
        get_access_group_rule_mock.return_value = DetailedResponseMock()

        set_module_args({
            'access_group_id': 'testString',
            'rule_id': 'testString',
            'transaction_id': 'testString',
            'state': 'absent',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group_rule.main()

        assert result.exception.args[0]['msg'] == 'Delete iam_access_group_rule error'

        mock_data = dict(
            access_group_id='testString',
            rule_id='testString',
            transaction_id='testString',
        )

        mock.assert_called_once_with(**mock_data)

        get_access_group_rule_mock_data = dict(
            access_group_id='testString',
            rule_id='testString',
            transaction_id='testString',
        )
        # Set the variables that belong to the "read" path to `None`
        # since we test the "delete" path here.
        for param in get_access_group_rule_mock_data:
            get_access_group_rule_mock_data[param] = mock_data.get(param, None)

        get_access_group_rule_mock.assert_called_once_with(**get_access_group_rule_mock_data)

        get_access_group_rule_patcher.stop()
        patcher.stop()
