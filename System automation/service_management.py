import shutil
import psutil
import os
import paramiko

#ssh to the server and execute the command
def check_disk_usage():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.124.11', username='root', password="k3nun02p.")
    stdin, stdout, stderr = ssh.exec_command('df -h')
    print(stdout.read().decode())

#Check the disk usage, CPU usage and memory usage

def find_big_files():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.124.11', username='root', password="k3nun02p.")
    stdin, stdout, stderr = ssh.exec_command('find / -type f -size +50M -exec du -h {} \; | sort -rh')
    print(stdout.read().decode())

def check_cpu_usage():
    print(psutil.cpu_percent(2))

def check_memory_usage():
    print(psutil.virtual_memory().percent)

check_disk_usage()
find_big_files()
check_cpu_usage()
check_memory_usage()