# Copyright 2020 The StackStorm Authors.
# Copyright 2019 Extreme Networks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
import paramiko

from st2common.runners.base_action import Action

__all__ = [
    'ServiceManager'
]


class ServiceManagerAction(Action):
    def run(self, host, servicename, status, is_cloud, user, password, port):
        #comando que será executado no host destino
        command = "systemctl " + status + " " + servicename

        if not is_cloud:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, port, user, password)
            stdin, stdout, stderr = ssh.exec_command(command)
            lines = stdout.readlines()            
