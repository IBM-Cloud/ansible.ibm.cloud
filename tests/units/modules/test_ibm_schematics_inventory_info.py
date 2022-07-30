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

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

from .common import DetailedResponseMock
from ansible.modules.cloud.ibm import ibm_schematics_inventory_info
from units.compat.mock import patch
from units.modules.utils import ModuleTestCase, AnsibleFailJson, AnsibleExitJson, set_module_args

try:
    from ibm_cloud_sdk_core import ApiException
except ImportError:
    pass


class TestInventoryResourceRecordModuleInfo(ModuleTestCase):
    """
    Test class for InventoryResourceRecord module testing.
    """

    def test_read_ibm_schematics_inventory_success(self):
        """Test the "read" path - successful."""
        datasource = {
            'inventory_id': 'testString',
            'profile': 'summary',
        }

        patcher = patch('ansible.modules.cloud.ibm.ibm_schematics_inventory_info.SchematicsV1.get_inventory')
        mock = patcher.start()
        mock.return_value = DetailedResponseMock(datasource)

        set_module_args({
            'inventory_id': 'testString',
            'profile': 'summary',
        })

        with self.assertRaises(AnsibleExitJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_inventory_info.main()

        assert result.exception.args[0]['msg'] == datasource

        mock.assert_called_once_with(
            inventory_id='testString',
            profile='summary',
        )

        patcher.stop()

    def test_read_ibm_schematics_inventory_failed(self):
        """Test the "read" path - failed."""
        patcher = patch('ansible.modules.cloud.ibm.ibm_schematics_inventory_info.SchematicsV1.get_inventory')
        mock = patcher.start()
        mock.side_effect = ApiException(400, message='Read ibm_schematics_inventory error')

        set_module_args({
            'inventory_id': 'testString',
            'profile': 'summary',
        })

        with self.assertRaises(AnsibleFailJson) as result:
            os.environ['SCHEMATICS_AUTH_TYPE'] = 'noAuth'
            ibm_schematics_inventory_info.main()

        assert result.exception.args[0]['msg'] == 'Read ibm_schematics_inventory error'

        mock.assert_called_once_with(
            inventory_id='testString',
            profile='summary',
        )

        patcher.stop()