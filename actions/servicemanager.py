from __future__ import absolute_import
import paramiko
import subprocess
from st2common.runners.base_action import Action

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
            return (True, 0)
        else:
            cloud_cmd = 'puppet-task run ''' + command + ' -n ' + host
            subprocess.call([cloud_cmd])
            return (True, 0)
