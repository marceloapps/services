from __future__ import absolute_import
import paramiko
import subprocess
from st2common.runners.base_action import Action

class ServiceManagerAction(Action):
    def run(self, host, servicename, status, is_cloud, user, password, port):
        #comando que será executado no host destino
        if is_cloud:
            cmd = "puppet-task --token-file /root/.puppetlabs/token run bolt_shim::command='systemctl {} {} -n {}".format(status, servicename, host)
            subprocess.call([cmd], shell=True)
        else:
            cmd = "systemctl " + status + " " + servicename
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, port, user, password)
            stdin, stdout, stderr = ssh.exec_command(cmd)
            lines = stdout.readlines()            

        return (True, 0)  
