# This script is used to check the disk usage, find big files, check CPU usage and check memory usage of a remote server.
import psutil
import paramiko
from psutil._common import bytes2human

ip = input("Enter the IP address of the server: ")
username = input("Enter the username: ")
password = input("Enter the password: ")

def check_disk_usage():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('df -h')
    print(stdout.read().decode())

def find_big_files():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('find / -type f -size +50M -exec du -h {} \; | sort -rh')
    print(stdout.read().decode())

def check_cpu_usage():
    print(psutil.cpu_percent(interval=1, percpu=True))

def check_memory_usage():
    print(psutil.virtual_memory().free / (1024 * 1024) + psutil.virtual_memory().used / (1024 * 1024))

check_disk_usage()
find_big_files()
check_cpu_usage()
check_memory_usage()