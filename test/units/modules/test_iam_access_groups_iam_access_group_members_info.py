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

from ansible.modules.cloud.ibm import iam_access_groups_iam_access_group_members_info
from units.compat.mock import patch
from units.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

from .common import DetailedResponseMock


class TestGroupMembersListModuleInfo(ModuleTestCase):
    """
    Test class for GroupMembersList module testing.
    """

    def test_read_iam_access_group_members_success(self):
        """Test the "read" path - successful."""
        datasource = {
            'access_group_id': 'testString',
            'transaction_id': 'testString',
            'limit': 38,
            'offset': 38,
            'type': 'testString',
            'verbose': False,
            'sort': 'testString',
        }

        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group_members_info.IamAccessGroupsV2.list_access_group_members')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(datasource)

        set_module_args({
            'access_group_id': 'testString',
            'transaction_id': 'testString',
            'limit': 38,
            'offset': 38,
            'type': 'testString',
            'verbose': False,
            'sort': 'testString',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group_members_info.main()

        assert result.exception.args[0]['msg'] == datasource

        mock.assert_called_once_with(
            access_group_id='testString',
            transaction_id='testString',
            limit=38,
            offset=38,
            type='testString',
            verbose=False,
            sort='testString',
        )

        patcher.stop()

    def test_read_iam_access_group_members_failed(self):
        """Test the "read" path - failed."""
        patcher = patch('ansible.modules.cloud.ibm.iam_access_groups_iam_access_group_members_info.IamAccessGroupsV2.list_access_group_members')
        mock = patcher.start()
        mock.side_effect = ApiException(400, message='Read iam_access_group_members error')

        set_module_args({
            'access_group_id': 'testString',
            'transaction_id': 'testString',
            'limit': 38,
            'offset': 38,
            'type': 'testString',
            'verbose': False,
            'sort': 'testString',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['IAM_ACCESS_GROUPS_AUTH_TYPE'] = 'noAuth'
            iam_access_groups_iam_access_group_members_info.main()

        assert result.exception.args[0]['msg'] == 'Read iam_access_group_members error'

        mock.assert_called_once_with(
            access_group_id='testString',
            transaction_id='testString',
            limit=38,
            offset=38,
            type='testString',
            verbose=False,
            sort='testString',
        )

        patcher.stop()
